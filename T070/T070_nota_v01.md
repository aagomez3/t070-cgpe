---
tarea: T070
titulo: "Cifras de los CGPE 2000 a 2027 con página y frase"
nivel: B
destino: claude-code
replica_en:
fecha_encargo: 2026-10-28
solicita: alejandro
---

# T070 — nota de ejecución

## Resumen

- Hay documento para los 28 años. Para 26 años es el CGPE y para 2008 y 2012 es la exposición de motivos de la Iniciativa de Ley de Ingresos (`tipo` = `exposicion_motivos_LIF`), porque el CGPE de esos años no está en los sitios permitidos.
- 2007 tiene el CGPE incompleto: en el PDF de la Gaceta (20061206-VI.pdf) las páginas 76 a 150 están en blanco. Lo que falta para t se tomó, cuando existe, de la exposición de motivos de la Iniciativa de LIF 2007 publicada el mismo día (anexo I, 20061206-I.pdf). Ese archivo complementario se cita en `T070_cgpe_v01.csv` (5 filas) y el programa lo descarga también.
- `T070_cgpe_v01.csv` tiene 582 cifras.
  - Lectura texto: 531. Pasan la validación 528 (`cita_en_pagina` = si y `valor_en_cita` = si).
  - Lectura imagen: 51 (confianza probable). Son 22 de 2001 a 2004, 8 de 2006 y 2007 y 21 de 2025.
  - Las 3 filas de texto que no pasan son metas escritas sólo en palabras («en equilibrio»), registradas con valor 0: 2007 `balance_publico_t`, 2008 `balance_publico_t` y 2008 `balance_publico_tm1`. La cita sí está en la página, pero el número no está en la cita. El integrador decide si las acepta.
- Las 13 copias de 2015 a 2027 tienen el SHA-256 que da el encargo (12 caracteres).

## Convenciones del programa (`T070_extrae_v01.py`)

- Biblioteca: `pdftotext` y `pdfinfo` de poppler-utils 24.02.0, con la biblioteca estándar de Python 3.13. El texto de cada página se extrae en dos modos: lectura (`pNNN.txt`) y `-layout` (`pNNN_layout.txt`). La cita pasa si aparece en cualquiera de los dos.
- Normalización:
  - Unicode NFC.
  - Espacios colapsados a uno.
  - Se unen los cortes de palabra con guion al fin de renglón, en la cita y en la página.
- Cuadros: la cita trae el encabezado de la columna y la fila separados por « | ». Cada segmento debe estar en la página.
- `valor_en_cita`: el valor sin signo debe aparecer en la cita como número completo. «1,234.5» cuenta como 1234.5. Para `fecha_presentacion` se busca la fecha escrita («5 de septiembre de 2014»).
- Los HTML (2000 y 2008) se tratan como una sola página 0, con las etiquetas quitadas.
- Las filas con `lectura` = imagen no se validan (no_aplica).

## Cobertura (año × variable)

H = hay al menos una fila; — = no se publica (se buscó y el documento no da cifra); NE = no encontrado (la cifra podría existir pero no se pudo leer o no se halló).

Columnas: 1 = `fecha_presentacion`; 2 = `pib_crec_t`; 3 = `pib_crec_t_inf`; 4 = `pib_crec_t_sup`; 5 = `pib_crec_tm1`; 6 = `pib_crec_tm1_inf`; 7 = `pib_crec_tm1_sup`; 8 = `pib_nominal_t`; 9 = `inflacion_t`; 10 = `petroleo_t`; 11 = `eua_pib_crec_t`; 12 = `eua_pi_crec_t`; 13 = `balance_publico_t`; 14 = `balance_publico_sin_inv_t`; 15 = `balance_primario_t`; 16 = `rfsp_t`; 17 = `ingresos_petroleros_t`; 18 = `balance_publico_tm1`; 19 = `balance_publico_sin_inv_tm1`; 20 = `balance_primario_tm1`; 21 = `rfsp_tm1`; 22 = `ingresos_petroleros_tm1`; 23 = `brecha_tm1`; 24 = `brecha_t`; 25 = `pib_potencial_crec`.

| año | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2000 | H | H | — | — | H | — | — | NE | H | H | NE | NE | H | — | H | — | NE | H | — | NE | — | NE | — | — | — |
| 2001 | H | H | — | — | H | — | — | H | H | H | H | — | H | — | H | — | — | H | — | H | — | — | — | — | — |
| 2002 | H | H | — | — | H | — | — | H | H | H | H | — | H | — | H | H | — | H | — | H | H | — | — | — | — |
| 2003 | H | H | — | — | H | — | — | H | H | H | H | — | H | — | H | H | H | H | — | H | H | H | — | — | — |
| 2004 | H | H | — | — | H | — | — | H | H | H | H | H | H | — | H | H | H | H | — | H | H | H | — | — | — |
| 2005 | H | H | — | — | H | — | — | NE | H | H | H | H | H | — | NE | H | NE | H | — | H | H | H | — | — | — |
| 2006 | H | H | — | — | H | — | — | H | H | H | H | H | H | — | H | H | H | H | — | H | H | H | — | — | — |
| 2007 | H | H | NE | NE | H | — | — | NE | H | NE | NE | NE | H | NE | H | NE | H | H | — | H | H | H | — | NE | NE |
| 2008 | H | H | — | — | H | — | — | — | H | — | — | — | H | — | H | — | — | H | — | H | — | — | — | — | — |
| 2009 | — | H | — | — | H | — | — | H | H | H | H | H | H | — | H | H | H | H | — | H | H | H | — | — | — |
| 2010 | — | H | — | — | H | — | — | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | — | — | — |
| 2011 | H | H | — | — | H | — | — | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | — | H | — |
| 2012 | H | H | — | — | H | — | — | — | H | — | H | H | — | H | — | — | — | — | H | — | — | — | — | — | — |
| 2013 | H | H | — | — | H | — | — | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | — | — | — |
| 2014 | H | H | — | — | H | — | — | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H |
| 2015 | H | H | — | — | H | — | — | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H |
| 2016 | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H |
| 2017 | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | — | H | H |
| 2018 | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | — | H | H |
| 2019 | H | H | H | H | H | — | — | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | — | — | H |
| 2020 | H | H | H | H | — | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | — | — | H |
| 2021 | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | — | — | H |
| 2022 | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | — | — | H |
| 2023 | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | — | — | H |
| 2024 | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | H | — | — | H |
| 2025 | H | H | H | H | H | H | H | H | H | H | H | H | H | — | H | H | H | H | — | H | H | H | NE | NE | H |
| 2026 | H | H | H | H | H | H | H | H | H | H | H | H | H | — | H | H | H | H | — | H | H | H | — | — | H |
| 2027 | H | — | H | H | — | H | H | H | H | H | H | H | H | — | H | H | H | H | — | H | H | H | — | — | H |

Totales de celdas: hay: 499; no se publica: 180; no encontrado: 21.


Cuando una variable tiene una fila con `principal` = no además de la principal, la tabla cuenta «H» igual. Las cifras de la brecha de t−1 de 2015 y 2016 son estimaciones del CGPE anterior que el documento cita; van con `principal` = no.

## Huecos y dónde se buscó

- **2000** (19991111-II.html). Es el único formato que existe: el HTML de la Gaceta. El PDF del anexo da 404 y el PDF del día no lo incluye. El HTML no trae los cuadros ni las «láminas» a los que remite el texto. Por eso no se encontraron `pib_nominal_t`, las variables de EUA, los ingresos petroleros de t y t−1, ni el balance primario de t−1 (el texto sólo da una diferencia de 0.36 puntos y no se calcula). Búsquedas por grep: «potencial», «brecha», «producción industrial», «petroler», «primario», «RFSP|requerimientos», «barril». El concepto de RFSP no aparece. El balance de t−1 (−1.25) sólo está en la «Presentación» que antecede al CGPE dentro del mismo HTML.
- **2001 a 2004.** Los cuadros (anexos de marco macroeconómico y de finanzas públicas) son imágenes sin capa de texto y se leyeron de la imagen. La producción industrial de EUA no se publica de 2001 a 2003. Los ingresos petroleros no se publican en 2001 ni 2002: sólo vienen los ingresos de Pemex como organismo.
- **2005** (20040909-IV.pdf). Los cuadros son imágenes JPEG de 72 ppp, ilegibles aun ampliadas: pp. 42, 44, 46, 47, 50, 51, 54, 57 y 58, incluido el Anexo I. No se encontraron `pib_nominal_t`, `balance_primario_t` ni `ingresos_petroleros_t`: se buscaron «nominal», «miles de millones», «primario» y «petroleros» en el texto de las pp. 25 a 60. La inflación registrada es el objetivo de Banxico (3.0 ± 1), no un pronóstico dic/dic.
- **2007** (20061206-VI.pdf + 20061206-I.pdf).
  - Las pp. 76 a 150 del PDF del CGPE están en blanco: sólo tienen el encabezado de la Gaceta. Se comprobó renderizando las páginas. Faltan las secciones VI «Perspectivas económicas para 2007», VII y VIII y los anexos.
  - No existe versión HTML: Gaceta/60/2006/dic/20061206-VI.html responde 404, igual que www.diputados.gob.mx/PEF2007/.
  - De la exposición de motivos de la LIF 2007 se tomaron `pib_crec_t`, `inflacion_t` (objetivo de Banxico), `balance_primario_t`, `balance_primario_tm1` e `ingresos_petroleros_t`.
  - Siguen sin encontrarse `pib_nominal_t`, `petroleo_t`, las variables de EUA y `rfsp_t`. La LIF 2007 sólo da la plataforma de petróleo, no el precio. Se buscaron «barril», «precio», «Estados Unidos» y «requerimientos».
- **2008** (exposición de motivos de la LIF 2008, HTML).
  - El CGPE 2008 no está en la Gaceta. La página del paquete (Gaceta/60/2007/sep/pf2008.html) sólo enlaza los anexos A a D.
  - Los anexos del 7-09-2007 (I a III) y del 11-09-2007 (I a VI) son otros asuntos. El VI es un PDF escaneado de 88 p. con informes de grupos parlamentarios y de la ASF.
  - www.diputados.gob.mx/PEF2008/ responde 404.
  - La exposición de motivos no publica PIB nominal, petróleo, EUA, RFSP ni ingresos petroleros.
- **2009 y 2010** (cgpe2009.pdf, cgpe_2010.pdf). Son PDF sin portada ni fecha, enlazados desde las páginas del paquete económico de la Gaceta. No hay fila `fecha_presentacion` porque el documento no imprime fecha. La fecha de la Gaceta que lo enlaza está en `T070_fuentes_v01.csv`: 2008-09-09 y 2009-09-10.
- **2012** (exposición de motivos de la LIF 2012).
  - El anexo F del 9-09-2011 (20110909-F.pdf) tiene sólo 2 páginas: la portada «Criterios Generales de Política Económica…» y la página legal, sin el documento.
  - Gaceta/61/2011/sep/20110909-F.html responde 404, igual que www.diputados.gob.mx/PEF2012/.
  - La exposición de motivos sólo publica el crecimiento de t y t−1, la inflación («alrededor de 3.0»), PIB y producción industrial de EUA, y el déficit sin inversión de Pemex. El dato de t−1 es el aprobado, no un cierre.
- **2010, 2011 y 2013.** La brecha y el PIB potencial sólo aparecen en prosa o en gráficas sin cifras. 2011 sí da la brecha de t (−2.0).
- **2019 a 2027.** Ningún documento publica la brecha del producto con cifra. 2020 y 2021 la mencionan sin número. En 2026 y 2027 se hizo grep de «brecha» y «potencial» en todas las páginas. 2019 tampoco publica rango para t−1.
- **2025** (escaneo). Se revisaron como imagen las pp. 5–11, 13–38 y 54–60, y los cuadros II.5, II.6, III.1 y III.2. No se revisaron página por página las pp. 39–53 ni 61–94 en busca de una cifra de brecha; por eso la brecha de 2025 queda «no encontrado» y no «no se publica».
- **2027.** Sólo da rangos de crecimiento: [1.5, 2.5] para 2027 y [1.0, 2.0] para 2026. No da el puntual «para estimaciones de finanzas públicas», así que `pib_crec_t` y `pib_crec_tm1` no tienen fila; los extremos van en `_inf` y `_sup`. El 1.90 % de la p. 25 es el crecimiento real del gasto corriente estructural, no del PIB.
- **Rangos de 2003 y 2004.** Los rangos 3.5–4.9 y 3.7–5.8 son escenarios del Pronafide, no pronósticos del CGPE; no se registraron.

## Advertencias sobre el resultado

1. **Signo de los RFSP.** Todos los RFSP van con signo menos, como déficit amplio, por la regla de déficit del encargo, aunque muchos documentos los imprimen sin signo («RFSP de 2.7 por ciento del PIB»). Cada fila lo dice en `nota`. Si el integrador usa el signo impreso, basta quitar el signo a las filas `rfsp_*`.
2. **Columna t−1 «aprobado» frente a «estimado».** En los CGPE 2017 a 2019, la columna t−1 del cuadro B.2 reproduce lo aprobado. Para t−1 se tomó como principal el cierre estimado del texto o de los cuadros de cierre; B.2 va con `principal` = no. El balance primario de 2016 en el CGPE 2017 (−0.6) sólo sale de B.2 y probablemente es la cifra aprobada.
3. **Discrepancias internas registradas con `principal`.**
   - 2003: ingresos petroleros 6.9 en el texto y 6.86 en el cuadro.
   - 2004: balance de 2003 de −0.6, −0.4 y −0.5.
   - 2006: PIB de EUA 3.5 frente a 3.3; RFSP de 2005 2.2 frente a 2.3.
   - 2010: RFSP con dos metodologías.
   - 2015: balance de 2014 de −3.6 frente a −3.5.
   - 2018: cierre de 2017 con y sin remanente del Banco de México.
   - 2019: producción industrial de EUA 2.7 frente a 2.6.
   - 2020: RFSP de 2.6 (meta ajustada) frente a 2.3.
   - 2022: PIB de EUA 4.5 frente a 4.4.
   - 2027: balance primario 0.6 frente a 0.5.
4. **Asignaciones interpretativas.**
   - 2010: `balance_publico_sin_inv_t` = −0.5 es el «Balance público de transición», impreso en positivo como fuente de financiamiento.
   - 2014: `pib_potencial_crec` = 3.5 («de cerca de 3.5 por ciento a 5.4 por ciento» con reformas; 5.4 con `principal` = no).
   - Inflación de 2005, 2007, 2008 y 2012: es el objetivo de Banxico o una frase «alrededor de», no un pronóstico dic/dic.
   - Metas «en equilibrio» registradas con valor 0.
5. **PIB potencial de 2019 a 2027.** Es la tasa del art. 11 C del Reglamento de la LFPRH, calculada para el límite del gasto corriente estructural. Se registraron todas sus menciones; las del mismo valor van con `principal` = no. En 2023 se excluyeron dos cifras que no son tasas de crecimiento del PIB potencial: contribuciones de 0.3 pp (litio) y 0.21 pp (participación laboral femenina).
6. **Texto extraído defectuoso.** En 2013 (Anexo B) y 2019 (cuadros B.2 y otros) el texto separa letras y números («Nomi na l», «20 1 9», «-2. 0»). Las citas copian el texto extraído tal como sale, para que se puedan buscar; las cifras citadas se leen completas.
7. **Erratas del original anotadas en `nota`.**
   - Portada del CGPE 2021: dice «ejercicio fiscal de 2020».
   - Índice del CGPE 2010: «2007-2008».
   - Título del cuadro II.5 del CGPE 2027: «2025-2026».
   - «equilibro» en el CGPE 2007.
   - «INICITIVA» en la LIF 2008.
   - PIB nominal de 2000 impreso «5.496.8».
   - Otras se anotan en la fila correspondiente.
8. **Folio impreso.** En las Gacetas de 2011 en adelante el folio impreso suele ser la página del PDF menos 1. Se registró el folio visible cuando aparece en el texto o en la imagen.
9. **Cifras leídas de imagen.** Las 51 filas de imagen son transcripciones. El ejecutor cotejó una muestra contra la imagen y coincidió: 2004 p. 38 y 2025 pp. 30 y 33.

## Declaración de quien ejecuta (sección 7)

- **Capacidades reales en esta sesión:** leer y escribir archivos; ejecutar código (bash y Python) en un contenedor Linux en la nube; acceso de red por un proxy a los sitios de la Cámara de Diputados; ver imágenes de páginas renderizadas; git commit y push a la rama. Había herramientas de búsqueda web disponibles y no se usaron. La extracción de cifras se repartió entre seis subagentes de la misma sesión (Claude), uno por bloque de años, con instrucciones escritas comunes. Cada uno validó su parte con el mismo validador. El ejecutor principal consolidó, corrigió signos y documentos complementarios, y cotejó una muestra contra la imagen. No había OCR instalado (tesseract): las páginas escaneadas se leyeron visualmente.
- **Lenguaje, versión y paquetes:** Python 3.13.17 (biblioteca estándar: csv, hashlib, html, re, subprocess, unicodedata, urllib); poppler-utils 24.02.0 (`pdftotext`, `pdfinfo`, `pdftoppm` para renderizar páginas). No se usaron pypdf ni PyMuPDF.
- **Años sin documento y dónde se buscó:** ninguno sin documento.
  - 2008 y 2012 usan la exposición de motivos de la LIF; dónde se buscó el CGPE está arriba, en «Huecos».
  - 2007 tiene el CGPE truncado en la Gaceta y se complementó con la exposición de motivos de la LIF 2007.
  - La búsqueda recorrió los índices mensuales y los días de la Gaceta (HTML y PDF) de los meses indicados, las páginas «pf20xx.html» de cada paquete económico, y las portadas Flash de www.diputados.gob.mx/PEF2010, PEF2013 y PEF2014; los nombres de los PDF se leyeron del propio archivo `index.swf`. PEF2007, 2008, 2009, 2011 y 2012 responden 404.
  - No se usó la ruta /Black/.
- **Qué no se pudo hacer y por qué:**
  - Leer los cuadros de 2005: son imágenes de 72 ppp ilegibles.
  - Leer las secciones VI a VIII y los anexos del CGPE 2007: páginas en blanco en el PDF.
  - Leer los cuadros del CGPE 2000: el HTML no los trae.
  - Revisar página por página las pp. 39–53 y 61–94 del CGPE 2025 en busca de la brecha.
  - Hacer fila `fecha_presentacion` para 2009 y 2010: los PDF no imprimen fecha.
  - Hacer que las 3 metas «en equilibrio» pasen `valor_en_cita`: no hay número impreso.
- **Supuestos que hubo que introducir:**
  - RFSP con signo menos (déficit amplio), aunque el documento los imprima sin signo.
  - Meta o cierre «en equilibrio» = 0.
  - `fecha_gaceta` de 2009 y 2010 = primer día de la Gaceta que enlaza la página del paquete económico.
  - 2010: el «Balance público de transición» se asigna a `balance_publico_sin_inv_t` y `_tm1`.
  - Cuando el documento da el objetivo de inflación de Banxico (3 ± 1) en lugar de un pronóstico dic/dic, se registra como `inflacion_t` con la salvedad en `nota`.
  - Para t−1, si un cuadro trae lo aprobado y otro lo estimado, la principal es la estimada.
  - Las cifras de brecha de un CGPE anterior citadas en un CGPE posterior se registran con `principal` = no.
  - 2007: lo que falta del CGPE se complementa con la exposición de motivos de la LIF 2007 del mismo día, que es un segundo documento para ese año.
- **Advertencias sobre la calidad del resultado:** ver la sección «Advertencias» de arriba.
  - Las 51 cifras leídas de imagen no tienen verificación automática.
  - 2000, 2005, 2007, 2008 y 2012 tienen cobertura parcial.
  - La elección de la fila principal es juicio de quien ejecuta, explicado en `nota`.
- **Confirmación:** no se usaron otras fuentes que gaceta.diputados.gob.mx y www.diputados.gob.mx, ni cifras de memoria. Todas las cifras se copiaron de los documentos citados; no se hizo ningún cálculo ni conversión.
