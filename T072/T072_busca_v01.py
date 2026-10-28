#!/usr/bin/env python3
"""T072_busca_v01.py — descarga, comprobación y validación de los pasajes de T072.

Uso (desde la carpeta T072/):

    python3 T072_busca_v01.py              # descarga y valida
    python3 T072_busca_v01.py --sin-descarga   # usa lo que ya está en pdf/

Bibliotecas (Python 3.10 o más reciente):
    requests        >= 2.31   descargas
    pypdf           >= 4.0    número de páginas y texto de cada página
    beautifulsoup4  >= 4.12   texto de las páginas HTML
    lxml            >= 4.9    analizador de HTML para beautifulsoup4
    pip install requests pypdf beautifulsoup4 lxml

Pasos:
  (a) descarga a pdf/ cada dirección de T072_documentos_v01.csv con encontrado = si
      (un segundo y medio entre descargas, agente de usuario fijo, sin rodeos);
  (b) comprueba la huella SHA-256, el tamaño y el número de páginas;
  (c) extrae el texto de cada página (pdf/texto/<id>_pNNN.txt);
  (d) comprueba que cada pasaje_literal de T072_pasajes_v01.csv, con los espacios
      normalizados, esté en el texto de su página, y escribe T072_validacion_v01.csv.
Además, con las mismas reglas, comprueba las citas de
T072_especificacion-gutierrez_v01.csv y las filas de contraste de
T072_valores-criticos_v01.csv contra el código de dynamac en CRAN.

Normalización (la misma para el pasaje y para la página): NFKC (separa las
ligaduras), comillas y guiones tipográficos a ASCII, sin guion suave y espacios
colapsados. Se prueban cuatro variantes de la página: tal cual; uniendo las
palabras cortadas a fin de línea ("macroe-\\nconomics" -> "macroeconomics");
conservando el guion ("long-\\nrun" -> "long-run"); y, como último recurso, sin
ningún espacio en ninguno de los dos lados (para PDF cuya capa de texto pega o
separa palabras). La columna nota dice qué variante coincidió.
"""
import csv
import hashlib
import io
import logging
import os
import re
import sys
import tarfile
import time
import unicodedata

import requests
import pypdf
from bs4 import BeautifulSoup

logging.getLogger("pypdf").setLevel(logging.CRITICAL)

AGENTE = "T072-busca/1.0 (python-requests; academic citation check)"
PAUSA = 1.5
DIR = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(DIR, "pdf")
TEXTO = os.path.join(PDF, "texto")

# Documentos cuya capa de texto necesita un tratamiento propio.
# V01b: fuentes Type 3 de dvips sin ToUnicode; pypdf devuelve /Gxx (código hexadecimal)
# y cada código está corrido +3 respecto del ASCII ("Wklv" = "This").
DECODIFICAR = {"V01b": "glifos_hex_menos_3"}

# M03: la página del INEGI arma la lista con esta API (la misma que llama su JavaScript).
INEGI_API = "https://www.inegi.org.mx/app/api/productos/interna_v2/publicaciones/lista/resultados/"
INEGI_CONSULTA = {"tema": "", "enti": "", "titg": "", "edic": "", "form": "", "proy": "1409",
                  "busc": "", "adv": False, "peri": "", "rango": "", "tipob": 2,
                  "orden": 1, "pag": 0, "tam": 50, "desc": True}

CRAN = ["https://cran.r-project.org/src/contrib/dynamac_0.1.12.tar.gz",
        "https://cran.r-project.org/src/contrib/Archive/dynamac/dynamac_0.1.12.tar.gz"]


def leer_csv(nombre):
    with open(os.path.join(DIR, nombre), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def sesion():
    s = requests.Session()
    s.headers["User-Agent"] = AGENTE
    return s


def extension(contenido, tipo):
    if contenido[:5] == b"%PDF-":
        return ".pdf"
    if "json" in tipo:
        return ".json"
    return ".html"


def descargar(s, documentos):
    """(a) Descarga cada documento con encontrado = si. Devuelve {id: ruta}."""
    os.makedirs(PDF, exist_ok=True)
    rutas = {}
    for d in documentos:
        if d["encontrado"] != "si":
            continue
        time.sleep(PAUSA)
        try:
            r = s.get(d["url"], timeout=120)
        except requests.RequestException as e:
            print(f"  {d['id']}: error de red: {e}")
            continue
        if r.status_code != 200:
            print(f"  {d['id']}: HTTP {r.status_code} en {d['url']}")
            continue
        ruta = os.path.join(PDF, d["id"] + extension(r.content, r.headers.get("content-type", "")))
        with open(ruta, "wb") as f:
            f.write(r.content)
        rutas[d["id"]] = ruta
        print(f"  {d['id']}: {len(r.content)} bytes -> {os.path.relpath(ruta, DIR)}")
        if d["id"] == "M03":
            time.sleep(PAUSA)
            a = s.post(INEGI_API, json=INEGI_CONSULTA, timeout=120)
            with open(os.path.join(PDF, "M03_lista.json"), "wb") as f:
                f.write(a.content)
            lista = a.json().get("list", [])
            print(f"  M03: la API del INEGI devolvió {len(lista)} publicaciones (pdf/M03_lista.json)")
    return rutas


def rutas_locales(documentos):
    rutas = {}
    for d in documentos:
        for ext in (".pdf", ".html"):
            ruta = os.path.join(PDF, d["id"] + ext)
            if d["encontrado"] == "si" and os.path.exists(ruta):
                rutas[d["id"]] = ruta
    return rutas


def decodificar(texto, modo):
    if modo == "glifos_hex_menos_3":
        texto = re.sub(r"/G([0-9A-Fa-f]{2})", lambda m: chr(int(m.group(1), 16)), texto)
        return "".join(chr(ord(c) - 3) if 33 < ord(c) < 127 else c for c in texto)
    return texto


def paginas_de(ide, ruta):
    """(c) Texto de cada página. Para HTML, una sola 'página' llamada html."""
    if ruta.endswith(".html"):
        with open(ruta, encoding="utf-8", errors="replace") as f:
            sopa = BeautifulSoup(f.read(), "lxml")
        for x in sopa(["script", "style", "noscript"]):
            x.decompose()
        return {"html": sopa.get_text("\n")}
    lector = pypdf.PdfReader(ruta)
    paginas = {}
    for i, p in enumerate(lector.pages, start=1):
        t = p.extract_text() or ""
        if ide in DECODIFICAR:
            t = decodificar(t, DECODIFICAR[ide])
        paginas[str(i)] = t
    return paginas


def comprobar(documentos, rutas):
    """(b) Huella, tamaño y páginas; (c) guarda el texto. Devuelve {id: {pagina: texto}}."""
    os.makedirs(TEXTO, exist_ok=True)
    textos = {}
    for d in documentos:
        ide = d["id"]
        if ide not in rutas:
            continue
        datos = open(rutas[ide], "rb").read()
        huella = hashlib.sha256(datos).hexdigest()
        h = "igual" if huella == d["sha256"] else f"DISTINTA ({huella})"
        b = "igual" if str(len(datos)) == d["bytes"] else f"distinto ({len(datos)})"
        paginas = paginas_de(ide, rutas[ide])
        np = "html" if "html" in paginas else str(len(paginas))
        pp = "igual" if np == d["paginas_pdf"] else f"distinto ({np} frente a {d['paginas_pdf']})"
        aviso = "  (HTML dinámico: la huella puede cambiar)" if np == "html" and huella != d["sha256"] else ""
        print(f"  {ide}: sha256 {h}; bytes {b}; páginas {pp}{aviso}")
        # Huella del texto extraído: estable aunque el servidor regenere el archivo (DASH, P03).
        texto_unido = "\n".join(paginas[k] for k in paginas).encode("utf-8")
        print(f"      HUELLA_TEXTO {hashlib.sha256(texto_unido).hexdigest()}")
        for pag, t in paginas.items():
            nombre = f"{ide}_p{pag.zfill(3)}.txt" if pag.isdigit() else f"{ide}_{pag}.txt"
            with open(os.path.join(TEXTO, nombre), "w", encoding="utf-8") as f:
                f.write(t)
        textos[ide] = paginas
    return textos


TRADUCE = str.maketrans({"‘": "'", "’": "'", "‚": "'", "‛": "'",
                         "“": '"', "”": '"', "„": '"', "«": '"', "»": '"',
                         "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-",
                         "―": "-", "−": "-", "­": None, " ": " "})


def base(t):
    return unicodedata.normalize("NFKC", t).translate(TRADUCE)


def espacios(t):
    return re.sub(r"\s+", " ", t).strip()


def variantes(pagina):
    p = base(pagina)
    return [("tal cual", espacios(p)),
            ("uniendo palabras cortadas a fin de línea", espacios(re.sub(r"-[ \t]*\n\s*", "", p))),
            ("conservando el guion a fin de línea", espacios(re.sub(r"-[ \t]*\n\s*", "-", p)))]


def buscar(pasaje, pagina):
    """Devuelve (encontrado, variante)."""
    q = espacios(base(pasaje))
    vs = variantes(pagina)
    for nombre, v in vs:
        if q in v:
            return True, nombre
    sin = re.sub(r"\s+", "", q)
    for nombre, v in vs[1:]:
        if sin in re.sub(r"\s+", "", v):
            return True, f"sin espacios ({nombre})"
    return False, ""


def validar_pasajes(pasajes, textos):
    """(d) Una fila de salida por pasaje."""
    filas = []
    for p in pasajes:
        fila = {"id": p["id"], "inciso": p["inciso"], "pagina_pdf": p["pagina_pdf"]}
        if p["relacion"] == "no_aparece" or not p["pasaje_literal"]:
            fila.update(pasaje_en_pagina="no_aplica", nota="sin pasaje (relacion = no_aparece)")
        elif p["nota"].startswith("[imagen]"):
            fila.update(pasaje_en_pagina="no_aplica", nota="leído de imagen o transcrito; cotejar contra la página")
        elif p["id"] not in textos:
            fila.update(pasaje_en_pagina="no", nota="documento no descargado")
        elif p["pagina_pdf"] not in textos[p["id"]]:
            fila.update(pasaje_en_pagina="no", nota=f"no existe la página {p['pagina_pdf']}")
        else:
            ok, como = buscar(p["pasaje_literal"], textos[p["id"]][p["pagina_pdf"]])
            if ok:
                fila.update(pasaje_en_pagina="si", nota=f"coincide: {como}")
            else:
                otras = [k for k, t in textos[p["id"]].items() if buscar(p["pasaje_literal"], t)[0]]
                fila.update(pasaje_en_pagina="no",
                            nota="no está en la página" + (f"; sí en {', '.join(otras)}" if otras else ""))
        filas.append(fila)
    return filas


def validar_especificacion(especificacion, textos):
    """Citas de T072_especificacion-gutierrez_v01.csv contra P11."""
    filas = []
    for e in especificacion:
        if not e["cita_literal"] or not e["pagina_pdf"]:
            continue
        pagina = textos.get("P11", {}).get(e["pagina_pdf"], "")
        ok, como = buscar(e["cita_literal"], pagina)
        filas.append({"id": "P11-especificacion", "inciso": e["campo"], "pagina_pdf": e["pagina_pdf"],
                      "pasaje_en_pagina": "si" if ok else "no",
                      "nota": f"coincide: {como}" if ok else "no está en la página"})
    return filas


def validar_cran(s, valores):
    """Filas CONTRASTE_CRAN contra el código de dynamac 0.1.12."""
    filas = []
    contraste = [v for v in valores if v["fuente"].startswith("CONTRASTE_CRAN")]
    if not contraste:
        return filas
    codigo = None
    for url in CRAN:
        time.sleep(PAUSA)
        try:
            r = s.get(url, timeout=120)
        except requests.RequestException:
            continue
        if r.status_code == 200:
            with open(os.path.join(PDF, "dynamac_0.1.12.tar.gz"), "wb") as f:
                f.write(r.content)
            with tarfile.open(fileobj=io.BytesIO(r.content)) as tar:
                codigo = tar.extractfile("dynamac/R/dynamac.R").read().decode("utf-8").splitlines()
            print(f"  CRAN: {url} ({hashlib.sha256(r.content).hexdigest()})")
            break
    for v in contraste:
        linea = int(v["pagina_pdf"].split(":")[1])
        fila = {"id": "CRAN-dynamac", "inciso": f"k{v['k']}_n{v['n']}_{v['nivel']}", "pagina_pdf": v["pagina_pdf"]}
        if codigo is None:
            fila.update(pasaje_en_pagina="no", nota="no se pudo bajar dynamac de CRAN")
        else:
            numeros = re.findall(r"-?\d+\.\d+", codigo[linea - 1].split("#")[0])
            par = [f"{float(x):.4f}" for x in numeros]
            i = ["0.10", "0.05", "0.01"].index(v["nivel"])
            ok = par[2 * i:2 * i + 2] == [f"{float(v['I0']):.4f}", f"{float(v['I1']):.4f}"]
            fila.update(pasaje_en_pagina="si" if ok else "no",
                        nota="I0 e I1 en la línea del código" if ok else f"la línea dice {numeros}")
        filas.append(fila)
    return filas


def main():
    sin_descarga = "--sin-descarga" in sys.argv
    documentos = leer_csv("T072_documentos_v01.csv")
    pasajes = leer_csv("T072_pasajes_v01.csv")
    especificacion = leer_csv("T072_especificacion-gutierrez_v01.csv")
    valores = leer_csv("T072_valores-criticos_v01.csv")
    s = sesion()

    print("(a) descarga" + (" omitida (--sin-descarga)" if sin_descarga else ""))
    rutas = rutas_locales(documentos) if sin_descarga else descargar(s, documentos)
    print("(b) y (c) huella, páginas y texto")
    textos = comprobar(documentos, rutas)
    print("(d) pasajes")
    filas = validar_pasajes(pasajes, textos)
    filas += validar_especificacion(especificacion, textos)
    filas += validar_cran(s, valores) if not sin_descarga else []

    salida = os.path.join(DIR, "T072_validacion_v01.csv")
    with open(salida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "inciso", "pagina_pdf", "pasaje_en_pagina", "nota"])
        w.writeheader()
        w.writerows(filas)
    cuenta = {}
    for fila in filas:
        cuenta[fila["pasaje_en_pagina"]] = cuenta.get(fila["pasaje_en_pagina"], 0) + 1
    print(f"Escrito {os.path.relpath(salida, DIR)}: {cuenta}")
    malos = [f for f in filas if f["pasaje_en_pagina"] == "no"]
    for f in malos:
        print(f"  NO: {f['id']} {f['inciso']} p. {f['pagina_pdf']}: {f['nota']}")
    return 1 if malos else 0


if __name__ == "__main__":
    sys.exit(main())
