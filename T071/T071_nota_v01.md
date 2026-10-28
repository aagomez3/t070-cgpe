---
tarea: T071
titulo: "Inversión pública desde 1970 y Penn World Table 10.01"
nivel: B
destino: claude-code
replica_en:
fecha_encargo: 2026-10-28
solicita: alejandro
---

# T071. Nota de ejecución (v01)

## 1. Resultado en breve

- **Pregunta (a): resuelta con la fuente 2 (INEGI, Sistema de Cuentas Nacionales de México).** Cada año
  de 1970 a 1992 tiene FBCF pública, privada y total, y PIB, a precios corrientes, de la misma
  publicación y edición, con su página, cuadro y renglón. El archivo `T071_inversion_historica_v01.csv`
  registra 779 cifras: 248 de la fuente 2, 129 de la fuente 1 (sólo a precios constantes, salvo el PIB de
  años sueltos) y 402 de contraste (fuente 4). De esas cifras, 52 se leyeron de la imagen de la página.
- **Pregunta (b): no resuelta.** Los dos archivos de la Penn World Table no se pudieron producir.
  `pwt1001.xlsx` se sirve desde `objectstore.surf.nl` y la política de red de esta sesión negó ese
  servidor (403 del proxy). Ver la sección 6.

## 2. Fuente elegida y por qué

El encargo pide usar la primera fuente, en el orden de la sección 2, que tenga la serie completa.

1. **Fuente 1. INEGI, *Estadísticas históricas de México* 2014 (y 2009): no tiene la serie a precios
   corrientes.** La FBCF por sector demandante (pública y privada) sólo aparece a precios constantes:
   - cuadro 8.20, de 1940 a 1980 en años seleccionados, en millones de pesos de 1970, con fuente Banco de México;
   - cuadro 8.21, de 1980 a 1994, en miles de nuevos pesos de 1980;
   - cuadro 8.22, de 1988 a 2004, en miles de pesos de 1993.

   El PIB a precios corrientes del cuadro 8.1 sólo trae 1970, 1980, 1990 y 1995-1997. La edición 2009
   (Tema 7, cuadros 7.14 a 7.16) tiene las mismas series; la de 1999 (capítulo 16, cuadros 16.5.1 a 16.5.3),
   consultada sólo para explorar y no descargada a `fuentes/`, también. Las cifras de la edición 2014 se registran con prioridad 1 y su año de precios.
2. **Fuente 2. INEGI, publicaciones históricas del SCNM: tiene la serie completa, repartida en ediciones.**
   Ninguna edición cubre sola de 1970 a 1992. Se registró cada edición por separado, sin empalmar:
   - **Base 1970.** *SCNM. Principales variables macroeconómicas. Período 1970-1982* (INEGI-SPP, 1983),
     cuadro No. 15.1 «Oferta y Demanda»: PIB y FBCF total, privada y pública en millones de pesos
     corrientes, de 1970 a 1981. El año 1982 viene marcado P (estimación preliminar) y n.d.
   - **Base 1980.** Las ocho ediciones del *SCNM, Tomo I, Resumen general*: 1980-1986, 1981-1987,
     1985-1988, 1986-1989, 1987-1990, 1988-1991, 1989-1992 y 1990-1993.
     - El PIB sale del cuadro No. 1 «Cuenta 1. Producto y gasto interno bruto».
     - La FBCF sale del cuadro «Formación bruta de capital fijo por tipo de bienes y comprador»: No. 26
       en las dos primeras ediciones y No. 20 en las demás.
     - Entre todas cubren de 1980 a 1993.
   - **Base 1993.** *SCNM. Cuentas de bienes y servicios 1988-1999, Tomo I* (INEGI, 2000): FBCF por
     tipo de bien y de comprador, y PIB a precios de mercado, en miles de pesos corrientes, de 1988 a 1999.
3. **Fuente 3. Banco de México, Informes anuales: no se consultó.** La página de la colección respondió
   403 y no se intentó rodearla. Ver la sección 5.
4. **Fuente 4. Contraste: Banco Mundial y FMI.** Ambos se registran con prioridad 4. CEPAL respondió 403.

Para un mismo año hay varias cifras (una por edición) porque INEGI revisa sus cálculos de una edición a
otra. Ejemplo: la FBCF total de 1985 es 9,075,830 en la edición 1980-1986 y 9,048,296 en la 1981-1987.
No se eligió entre ediciones ni se empalmaron bases. Esa decisión le toca al integrador.

## 3. Tabla de cobertura (fuentes 1 y 2)

Clave de cada celda:
- P = PIB, T = FBCF total, U = FBCF pública, R = FBCF privada: **hay**, con la cifra registrada.
- · = **no se publica** en esa edición (año fuera de su cobertura).
- En la base 1970, 1982 aparece en el cuadro como n.d.
- «no encontrado» = la fuente no se pudo consultar.

Notas a las columnas:
- Las columnas SCNM y CBS son a precios corrientes.
- «EHM 2014 corrientes» es el PIB del cuadro 8.1, que es el único dato a precios corrientes de esa edición.
- «EHM 2014 constantes» incluye los cuadros 8.20 (precios de 1970), 8.21 (de 1980) y 8.22 (de 1993), y el PIB constante del cuadro 8.1.

| Año | SCNM 1970-1982 (b.1970) | SCNM 1980-86 | SCNM 1981-87 | SCNM 1985-88 | SCNM 1986-89 | SCNM 1987-90 | SCNM 1988-91 | SCNM 1989-92 | SCNM 1990-93 | CBS 1988-99 (b.1993) | EHM 2014 corrientes | EHM 2014 constantes | Banxico, Informes anuales |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970 | PTUR | · | · | · | · | · | · | · | · | · | P | PTUR | no encontrado |
| 1971 | PTUR | · | · | · | · | · | · | · | · | · | · | · | no encontrado |
| 1972 | PTUR | · | · | · | · | · | · | · | · | · | · | · | no encontrado |
| 1973 | PTUR | · | · | · | · | · | · | · | · | · | · | · | no encontrado |
| 1974 | PTUR | · | · | · | · | · | · | · | · | · | · | · | no encontrado |
| 1975 | PTUR | · | · | · | · | · | · | · | · | · | · | TUR | no encontrado |
| 1976 | PTUR | · | · | · | · | · | · | · | · | · | · | TUR | no encontrado |
| 1977 | PTUR | · | · | · | · | · | · | · | · | · | · | TUR | no encontrado |
| 1978 | PTUR | · | · | · | · | · | · | · | · | · | · | TUR | no encontrado |
| 1979 | PTUR | · | · | · | · | · | · | · | · | · | · | TUR | no encontrado |
| 1980 | PTUR | PTUR | · | · | · | · | · | · | · | · | P | PTUR | no encontrado |
| 1981 | PTUR | PTUR | PTUR | · | · | · | · | · | · | · | · | TUR | no encontrado |
| 1982 | · (n.d.) | PTUR | PTUR | · | · | · | · | · | · | · | · | TUR | no encontrado |
| 1983 | · | PTUR | PTUR | · | · | · | · | · | · | · | · | TUR | no encontrado |
| 1984 | · | PTUR | PTUR | · | · | · | · | · | · | · | · | TUR | no encontrado |
| 1985 | · | PTUR | PTUR | PTUR | · | · | · | · | · | · | · | TUR | no encontrado |
| 1986 | · | PTUR | PTUR | PTUR | PTUR | · | · | · | · | · | · | TUR | no encontrado |
| 1987 | · | · | PTUR | PTUR | PTUR | PTUR | · | · | · | · | · | TUR | no encontrado |
| 1988 | · | · | · | PTUR | PTUR | PTUR | PTUR | · | · | PTUR | · | TUR | no encontrado |
| 1989 | · | · | · | · | PTUR | PTUR | PTUR | PTUR | · | PTUR | · | TUR | no encontrado |
| 1990 | · | · | · | · | · | PTUR | PTUR | PTUR | PTUR | PTUR | P | PTUR | no encontrado |
| 1991 | · | · | · | · | · | · | PTUR | PTUR | PTUR | PTUR | · | TUR | no encontrado |
| 1992 | · | · | · | · | · | · | · | PTUR | PTUR | PTUR | · | TUR | no encontrado |
| 1993 | · | · | · | · | · | · | · | · | PTUR | PTUR | · | TUR | · |
| 1994 | · | · | · | · | · | · | · | · | · | PTUR | · | TUR | · |
| 1995 | · | · | · | · | · | · | · | · | · | PTUR | P | PTUR | · |
| 1996 | · | · | · | · | · | · | · | · | · | PTUR | P | PTUR | · |
| 1997 | · | · | · | · | · | · | · | · | · | PTUR | P | PTUR | · |
| 1998 | · | · | · | · | · | · | · | · | · | PTUR | · | TUR | · |
| 1999 | · | · | · | · | · | · | · | · | · | PTUR | · | TUR | · |
| 2000-2004 | · | · | · | · | · | · | · | · | · | · | · | TUR | · |

Fuentes de contraste (prioridad 4):

| Fuente | Variable | Años con dato desde 1970 |
|---|---|---|
| Banco Mundial, NE.GDI.FTOT.ZS (% del PIB) | fbcf_total | 1970-2025 |
| Banco Mundial, NE.GDI.FPRV.ZS (% del PIB) | fbcf_privada | 1980-2025; de 1970 a 1979 la API devuelve `null` (no se publica) |
| FMI, ICSD 2021: igov_n, ipriv_n, GDP_n (miles de millones de moneda nacional corriente) | fbcf_publica, fbcf_privada, pib | 1970-2019 |
| FMI, ICSD 2021: igov_rppp, ipriv_rppp, GDP_rppp (miles de millones de dólares internacionales de 2017) | fbcf_publica, fbcf_privada, pib | 1970-2019 |
| CEPAL, repositorio.cepal.org | todas | no encontrado (403) |

Los dos indicadores del Banco Mundial que pide el encargo no incluyen una serie de FBCF pública.

## 4. Qué dice cada fuente sobre la FBCF pública

- **SCNM base 1980.**
  - Cita del *SCNM 1980-1986, Tomo I* (pág. PDF 40, impresa 37), repetida casi igual en el *SCNM
    1989-1992, Tomo I* (pág. PDF 49): «También se investigó el tipo de comprador de los bienes que
    componen la formación de capital, diferenciándose los organismos del sector público y el sector
    privado.»
  - Sobre la FBCF misma (pág. PDF 26 de 1980-1986): «Esta partida es ilustrativa de la compra de bienes
    que llevan a cabo las unidades productoras para incrementar sus activos fijos; los bienes están
    valuados a precios de comprador».
  - El renglón se llama «Pública» y el cuadro, «Formación bruta de capital fijo por tipo de bienes y
    comprador».
  - En los tomos consultados no se dice expresamente si «sector público» comprende gobierno general
    más empresas públicas. La misma colección tiene las *Cuentas de producción del sector público*
    (1980-1984 a 1990-1993), que no se descargaron porque el encargo no las pide; ahí habría que
    verificarlo.
- **SCNM base 1970** (*Principales variables macroeconómicas 1970-1982*, cuadro 15.1). Los renglones
  «Privada» y «Pública» cuelgan de «Formación bruta de capital fijo». En el documento no se encontró una
  definición del alcance de «Pública». El índice anuncia además el cuadro 19 «FBCF por tipo de bienes y
  comprador», que no se transcribió porque el 15.1 ya trae las tres cifras.
- **SCNM base 1993** (*Cuentas de bienes y servicios 1988-1999*).
  - El cuadro «Formación bruta de capital fijo, por tipo de bien y de comprador» trae los renglones
    «Privada» y «Pública».
  - Presentación del tomo I (pág. PDF 11): «se realizaron ajustes en los niveles y la composición de la
    formación bruta de capital fijo correspondientes a los Sectores Público y Privado para 1998».
  - La cuenta de capital (pág. PDF 28) define la FBCF como el «valor total de las adquisiciones de
    activos fijos tangibles o intangibles, obtenidos como resultado de procesos de producción, que son
    efectuadas por el productor durante el período contable».
  - No precisa en esas páginas qué entidades forman el sector público.
- **EHM 2014.**
  - Columnas «Pública» y «Privada» bajo «Formación bruta de capital fijo según sector demandante».
  - Fuente citada: Banco de México para el cuadro 8.20 e INEGI, SCNM para los cuadros 8.21 y 8.22.
  - Sin definición propia.
- **FMI, ICSD 2021.** Hoja *Definitions*: «igov: General government investment (gross fixed capital
  formation)». La hoja *Cover* dice que la inversión pública es la del gobierno general, así que no
  incluye empresas públicas y no es comparable con la «Pública» del SCNM.

## 5. Dónde se buscó lo que no se encontró o no se usó

- **Catálogo de INEGI.** Se recorrió el catálogo de publicaciones (`https://www.inegi.org.mx/app/publicaciones/`,
  búsqueda por la frase «Sistema de Cuentas Nacionales», 409 resultados, orden por edición) con un
  navegador sin interfaz, porque la página se arma con JavaScript. Las direcciones de los PDF se tomaron
  de la ficha de cada publicación (`/app/biblioteca/ficha.html?upc=...`).
- **Ediciones del SCNM identificadas y no transcritas.** No hacían falta para cubrir de 1970 a 1992:
  - 1970-1978 (Tomo I, 1981);
  - 1978-1980 (1982);
  - 1979-1981 (1983);
  - 1980-1982 (1984);
  - 1981-1983 (1985);
  - 1982-1984 (1986);
  - 1983-1985, cálculo definitivo (1986);
  - *Cuentas de bienes y servicios* 1988-1994, 1988-1995, 1988-1996, 1988-1997 y 1988-1998 (base 1993).

  Pueden servir para otra réplica.
- **Base 1980 sin serie 1970-1979.** No se encontró en el catálogo una publicación de la base 1980 que
  traiga FBCF pública a precios corrientes para 1970-1979. La más cercana es *SCNM 1960-1985* (1987), pero
  su índice de cuadros está en millones de pesos a precios de 1970.
- **Banco de México** (`https://www.banxico.org.mx/publicaciones-y-prensa/informes-anuales/`): la página
  del encargo respondió 403, aunque la portada del sitio abre (200). No se probaron otras rutas ni el sitio
  `anterior.banxico.org.mx` al que redirige otra página de la sección. No hizo falta para la cobertura,
  pero esta fuente queda sin contraste.
- **CEPAL** (`https://repositorio.cepal.org/`): respondió 403, tanto en la página principal como en el
  archivo robots.
- **Penn World Table:** ver la sección 6.

## 6. Pregunta (b): Penn World Table 10.01

- **Página de la versión.** `https://www.rug.nl/ggdc/productivity/pwt/pwt-releases/pwt1001` abrió. Desde
  ahí se bajó la guía de usuario (`pwt100-user-guide-to-data-files.pdf`; la página de la 10.01 enlaza la
  guía de la 10.0).
- **Metadatos del registro.** Los metadatos de `doi:10.34894/QT5BCC` se guardaron como
  `QT5BCC_dataset.json`. Ahí está la huella SHA-1 publicada de `pwt1001.xlsx`:
  `7461933f7561767ffbd77db3ab984d60cb21e9ef`, de 6 551 843 bytes.
- **Archivo de datos.** `https://dataverse.nl/api/access/datafile/354095` redirige a `objectstore.surf.nl`.
  El proxy de la sesión respondió 403 al CONNECT: es política de red del entorno, no del sitio. No se
  intentó otra ruta.
- **Archivos que faltan.** Por eso **no se entregan** `T071_pwt_mex_v01.csv` ni `T071_pwt_leyenda_v01.csv`.
  El paso (d) del programa los rehace en cuanto `fuentes/pwt1001.xlsx` exista; el paso (a) lo descarga en
  una máquina con acceso. Se probó el paso (d) con un libro de prueba con hojas `Legend` y `Data`, fuera
  del repositorio.
- **Supuesto sin verificar.** Que las hojas del archivo real se llamen `Legend` y `Data`; el programa
  ignora mayúsculas.

## 7. Cómo leer los archivos

- **`lectura`.** Toma uno de estos valores:
  - `texto` = capa de texto nativa del PDF (sólo la EHM 2014);
  - `texto_ocr` = capa de texto de un PDF escaneado. Se cotejó a ojo cada cifra contra la imagen de la
    página y todas coincidieron;
  - `imagen` = cifra leída de la imagen porque la capa OCR está dañada o duplicada;
  - `json` y `xlsx` = leída del archivo de datos.
- **`celda` en PDF.** Formato `renglon: <etiqueta> | columna: <año>`; en la EHM, `| n: <k>` es el número
  de cifra dentro del renglón.
- **`celda` en JSON y Excel.** JSON: `registro: <i> | campo: value`. Excel: referencia de celda en la hoja indicada.
- **Valores.** Se copiaron sin separadores de miles y con los decimales de la fuente. No se convirtieron
  unidades: la edición 1990-1993 y la base 1993 están en miles de (nuevos) pesos y las demás ediciones
  del SCNM en millones de pesos. La unidad literal de cada cifra va en `unidad`.
- **Validación.** `T071_validacion_v01.csv` (paso c) da 727 cifras con `coincide = si`, 52 con
  `no_aplica` (leídas de imagen) y 0 con `no`.
- **Sumas.** En las tres fuentes nacionales, pública + privada = total en los 101 tríos año-edición,
  salvo 1976 y 1977 del cuadro 8.20 de la EHM, donde difieren en 1 unidad. La fuente advierte que la
  suma de las cifras parciales puede no coincidir con el total por el redondeo.

## 8. Declaración de quien ejecuta

- **Capacidades reales en esta sesión:**
  - leer archivos, ejecutar código (bash, Python, Node con Playwright y Chromium), buscar en la web y
    escribir archivos: sí;
  - ver imágenes de páginas: sí, con lo que se leyeron y cotejaron las cifras;
  - salida a internet por un proxy con política de red;
  - sin acceso a Google Drive.
- **Lenguaje, versión y paquetes:**
  - Python 3.13.17 con pdfplumber 0.11.10 (pdfminer.six 20260107) y openpyxl 3.1.5;
  - herramientas auxiliares, sólo para explorar y no necesarias para correr el programa: poppler-utils
    24.02 (pdftotext, pdftoppm) y Node 22.22 con Playwright, para recorrer el catálogo de INEGI.
- **Fuentes que se intentaron y no abrieron:**
  - `https://dataverse.nl/api/access/datafile/354095` → redirección a `objectstore.surf.nl`, 403 del
    proxy (política de red de la sesión). Lo mismo para `https://dataverse.nl/api/access/datafile/354100`
    (*What's new*);
  - `https://www.banxico.org.mx/publicaciones-y-prensa/informes-anuales/` → 403;
  - `https://repositorio.cepal.org/` y `/robots.txt` → 403.
- **Qué no se pudo hacer y por qué:**
  - no se descargó `pwt1001.xlsx`, así que no se produjeron `T071_pwt_mex_v01.csv` ni
    `T071_pwt_leyenda_v01.csv` (pregunta b);
  - no se consultaron los informes anuales de Banxico (403);
  - no se consultó CEPAL (403).
- **Supuestos que hubo que introducir:**
  - Que las hojas de `pwt1001.xlsx` se llaman `Legend` y `Data` (no verificable sin el archivo).
  - Que el renglón «Pública» del cuadro de FBCF por comprador es la FBCF pública tal como la nombra la
    fuente; la fuente no detalla su alcance (sección 4).
  - Que el PDF `702825147594_1.pdf` es el Tomo I de 1985-1988, por su portada, aunque su ruta lleve el
    UPC del Tomo II.
- **Advertencias sobre la calidad del resultado:**
  - Las 52 cifras con `lectura = imagen` no se pueden volver a leer por programa; hay que cotejarlas
    a ojo. Son:
    - las 48 de la base 1993: en sus páginas PDF 49-50 (parte 1) y 61-62 (parte 2) la capa de texto
      está duplicada;
    - las de 1970 (FBCF total y pública) del cuadro 15.1;
    - las de 1988 y 1989 (FBCF total) del SCNM 1986-1989.

    En todas, la suma pública + privada = total, o valor agregado + impuestos = PIB, confirma la lectura,
    salvo 1 unidad en el PIB de 1995 de la base 1993.
  - El segundo dígito del PIB de 1988 en el SCNM 1988-1991 está borroso en la imagen. El renglón GASTO y
    la suma de los componentes del ingreso del mismo cuadro dan 390,451,299, que es lo que trae la capa OCR.
  - Los JSON del Banco Mundial son la respuesta de una API viva: una descarga posterior puede traer
    cifras revisadas y otra huella.
- **Confirmación:** no se usaron otras fuentes que las de la sección 2 del encargo, ni prensa,
  Wikipedia, artículos o sitios de terceros, ni la memoria para ninguna cifra. El buscador web sólo
  sirvió para localizar páginas de inegi.org.mx e imf.org; todas las cifras salen de los archivos de
  `fuentes/`.
