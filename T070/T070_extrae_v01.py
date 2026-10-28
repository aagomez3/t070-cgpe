#!/usr/bin/env python3
"""T070 - descarga, comprobacion y validacion de las cifras de los CGPE 2000-2027.

Uso (desde la carpeta T070/):  python3 T070_extrae_v01.py

Pasos:
  (a) descarga a pdf/ cada URL de T070_fuentes_v01.csv que falte (1.1 s entre descargas);
  (b) comprueba SHA-256 y numero de paginas contra T070_fuentes_v01.csv;
  (c) extrae el texto de cada pagina a pdf/texto/<archivo>/pNNN.txt (modo lectura) y
      pNNN_layout.txt (modo -layout); un HTML se trata como una sola "pagina 0";
  (d) valida cada fila de T070_cgpe_v01.csv y escribe T070_validacion_v01.csv.

Biblioteca: pdftotext y pdfinfo de poppler-utils (paquete del sistema; en Debian/Ubuntu
`apt-get install poppler-utils`). El resto es biblioteca estandar de Python 3.

Reglas de validacion:
  - Normalizacion: Unicode NFC, espacios (incluido el no separable) colapsados a uno.
  - Una cita se busca en el texto de su pagina en modo lectura y en modo -layout; basta
    que aparezca en uno. Tambien se compara con los cortes de palabra con guion al fin de
    renglon unidos ("Fede- racion" -> "Federacion") en ambos lados.
  - Si la cita sale de un cuadro, trae el encabezado de la columna y la fila separados por
    " | "; cada segmento debe aparecer en la pagina.
  - valor_en_cita: el valor sin signo (y sin separador de miles) debe aparecer en la cita
    como numero completo; para fecha_presentacion se busca la fecha escrita en espanol
    ("5 de septiembre de 2014").
  - Filas con lectura = imagen: cita_en_pagina y valor_en_cita = no_aplica.
"""
import csv
import hashlib
import html
import os
import re
import shutil
import subprocess
import sys
import time
import unicodedata
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(AQUI, 'pdf')
TEXTO = os.path.join(PDF, 'texto')
FUENTES = os.path.join(AQUI, 'T070_fuentes_v01.csv')
CIFRAS = os.path.join(AQUI, 'T070_cgpe_v01.csv')
SALIDA = os.path.join(AQUI, 'T070_validacion_v01.csv')

MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto',
         'septiembre', 'octubre', 'noviembre', 'diciembre']


def requiere(prog):
    if shutil.which(prog) is None:
        sys.exit(f'Falta {prog}: instale poppler-utils (p. ej. apt-get install poppler-utils).')


def archivo_de(url):
    return url.rstrip('/').split('/')[-1]


def descarga(url, destino):
    print(f'descargando {url}')
    time.sleep(1.1)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=300) as r, open(destino + '.part', 'wb') as f:
        shutil.copyfileobj(r, f)
    os.replace(destino + '.part', destino)


def sha256(ruta):
    h = hashlib.sha256()
    with open(ruta, 'rb') as f:
        for bloque in iter(lambda: f.read(1 << 20), b''):
            h.update(bloque)
    return h.hexdigest()


def paginas_pdf(ruta):
    out = subprocess.run(['pdfinfo', ruta], capture_output=True, text=True, errors='replace').stdout
    m = re.search(r'^Pages:\s+(\d+)', out, re.M)
    return int(m.group(1)) if m else -1


def texto_html(ruta):
    crudo = open(ruta, 'rb').read()
    m = re.search(rb'charset=["\']?([\w-]+)', crudo[:3000], re.I)
    cod = m.group(1).decode() if m else 'latin-1'
    try:
        t = crudo.decode(cod)
    except (LookupError, UnicodeDecodeError):
        t = crudo.decode('latin-1')
    t = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    return html.unescape(t)


def extrae_texto(nombre, ruta, npag):
    """Devuelve {pagina: [texto_lectura, texto_layout]}; cachea en pdf/texto/."""
    d = os.path.join(TEXTO, nombre)
    os.makedirs(d, exist_ok=True)
    if ruta.lower().endswith(('.html', '.htm')):
        t = texto_html(ruta)
        open(os.path.join(d, 'p000.txt'), 'w', encoding='utf-8').write(t)
        return {0: [t, t]}
    res = {}
    for p in range(1, npag + 1):
        par = []
        for modo, suf in (([], ''), (['-layout'], '_layout')):
            f = os.path.join(d, f'p{p:03d}{suf}.txt')
            if not os.path.exists(f):
                subprocess.run(['pdftotext', '-q', '-enc', 'UTF-8', *modo, '-f', str(p), '-l', str(p),
                                ruta, f], check=False)
            par.append(open(f, encoding='utf-8', errors='replace').read() if os.path.exists(f) else '')
        res[p] = par
    return res


def norm(s):
    s = unicodedata.normalize('NFC', s or '')
    s = s.replace('­', '').replace(' ', ' ').replace(' ', ' ').replace(' ', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def sin_guion(s):
    return re.sub(r'(\w)[-‐‑] (\w)', r'\1\2', s)


def cita_en(cita, textos):
    segs = [norm(x) for x in cita.split(' | ') if norm(x)]
    if not segs:
        return False
    for t in textos:
        nt = norm(t)
        nh = sin_guion(nt)
        if all(s in nt or sin_guion(s) in nh for s in segs):
            return True
    return False


def valor_en(valor, cita, variable):
    c = norm(cita)
    if variable == 'fecha_presentacion':
        m = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})', valor.strip())
        if not m:
            return False
        a, me, di = int(m.group(1)), int(m.group(2)), int(m.group(3))
        pat = rf'(?<!\d)0?{di}\s+de\s+{MESES[me - 1]}\s+(?:de|del)\s+{a}'
        return re.search(pat, c, re.I) is not None
    v = valor.strip().lstrip('+-−').replace(',', '')
    if not re.fullmatch(r'\d+(\.\d+)?', v):
        return False
    # cada numero de la cita como token completo; 1,234.5 cuenta como 1234.5
    tokens = re.findall(r'(?<![\d.,])(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?', c)
    return any(t.replace(',', '') == v for t in tokens)


def main():
    requiere('pdftotext')
    requiere('pdfinfo')
    os.makedirs(PDF, exist_ok=True)
    fuentes = list(csv.DictReader(open(FUENTES, encoding='utf-8')))
    textos = {}
    problemas = 0
    for f in fuentes:
        url = f['url'].strip()
        if not url:
            print(f"{f['anio_cgpe']}: sin documento")
            continue
        nombre = archivo_de(url)
        ruta = os.path.join(PDF, nombre)
        if not os.path.exists(ruta):
            try:
                descarga(url, ruta)
            except Exception as e:  # se informa y se sigue
                print(f"{f['anio_cgpe']}: no se pudo descargar {url}: {e}")
                problemas += 1
                continue
        h = sha256(ruta)
        ok_sha = h == f['sha256'].strip()
        es_html = nombre.lower().endswith(('.html', '.htm'))
        npag = 0 if es_html else paginas_pdf(ruta)
        ok_pag = str(npag) == f['paginas'].strip()
        print(f"{f['anio_cgpe']} {nombre}: sha256 {'ok' if ok_sha else 'DISTINTO ' + h[:12]}; "
              f"paginas {npag} {'ok' if ok_pag else 'DISTINTO de ' + f['paginas']}")
        problemas += (not ok_sha) + (not ok_pag)
        textos[nombre] = extrae_texto(nombre, ruta, npag)

    filas = list(csv.DictReader(open(CIFRAS, encoding='utf-8')))
    # documentos complementarios citados en T070_cgpe_v01.csv que no son la fuente principal del año
    # (su SHA-256 esta en la nota de T070_fuentes_v01.csv)
    for url in sorted({r['url'].strip() for r in filas} - {f['url'].strip() for f in fuentes}):
        nombre = archivo_de(url)
        ruta = os.path.join(PDF, nombre)
        if not os.path.exists(ruta):
            try:
                descarga(url, ruta)
            except Exception as e:
                print(f'complemento: no se pudo descargar {url}: {e}')
                problemas += 1
                continue
        npag = paginas_pdf(ruta)
        print(f'complemento {nombre}: sha256 {sha256(ruta)}; paginas {npag}')
        textos[nombre] = extrae_texto(nombre, ruta, npag)

    salida = []
    n_ok = n_no = n_na = 0
    for r in filas:
        nombre = r['archivo'].strip()
        pag = int(r['pagina_pdf']) if r['pagina_pdf'].strip().lstrip('-').isdigit() else -1
        if r['lectura'].strip() == 'imagen':
            salida.append([r['anio_cgpe'], r['variable'], r['pagina_pdf'], 'no_aplica', 'no_aplica',
                           'leida de la imagen de la pagina'])
            n_na += 1
            continue
        nota = ''
        if nombre not in textos:
            ce, ve, nota = 'no', 'no', 'archivo no disponible'
        elif pag not in textos[nombre]:
            ce, ve, nota = 'no', 'no', 'pagina fuera del archivo'
        else:
            ce = 'si' if cita_en(r['cita_literal'], textos[nombre][pag]) else 'no'
            ve = 'si' if valor_en(r['valor'], r['cita_literal'], r['variable']) else 'no'
            if ce == 'si' and ve == 'no' and re.search(r'equilibr', r['cita_literal'], re.I):
                nota = 'valor 0 escrito en palabras (equilibrio); sin numero impreso'
        if ce == 'si' and ve == 'si':
            n_ok += 1
        else:
            n_no += 1
        salida.append([r['anio_cgpe'], r['variable'], r['pagina_pdf'], ce, ve, nota])

    with open(SALIDA, 'w', newline='', encoding='utf-8') as fo:
        w = csv.writer(fo)
        w.writerow(['anio_cgpe', 'variable', 'pagina_pdf', 'cita_en_pagina', 'valor_en_cita', 'nota'])
        w.writerows(salida)
    print(f'filas: {len(filas)}; pasan: {n_ok}; no pasan: {n_no}; leidas de imagen: {n_na}; '
          f'problemas de fuentes: {problemas}')
    print(f'escrito {SALIDA}')


if __name__ == '__main__':
    main()
