---
tarea: T070
titulo: "Cifras de los CGPE 2000 a 2027 con página y frase: crecimiento previsto, metas de balance y brecha"
nivel: B                      # cita de documentos oficiales; el integrador coteja cada cifra contra su página
destino: claude-code          # sesión de Claude Code en la nube (cuenta Max); no ve Google Drive
replica_en:                   # nivel B: sin réplica ciega
fecha_encargo: 2026-10-28
solicita: alejandro
---

# ENCARGO T070 — cifras de los CGPE 2000 a 2027

> Instrucción a la sesión que ejecuta: responde sólo a lo que pide este archivo. No tienes acceso a
> Google Drive ni a conversaciones previas, y no los necesitas: todo lo que hace falta está aquí. No
> propongas trabajo adicional. Si un documento o una cifra no aparece, deja el hueco y dilo en
> `T070_nota_v01.md`; nunca estimes, calcules ni tomes de memoria una cifra.

## 1. Pregunta exacta

Para cada año presupuestal t de 2000 a 2027 (28 años): ¿qué cifras publicó la Secretaría de Hacienda
en los Criterios Generales de Política Económica para t (CGPE t, entregados al Congreso en septiembre
de t−1, o en noviembre o diciembre en algunos años) sobre:

a. el crecimiento real del PIB de México previsto para t y el estimado para t−1;
b. las metas de balance del sector público para t y su cierre estimado para t−1;
c. la brecha del producto y el crecimiento del PIB potencial, cuando los publica?

Cada cifra, con la página del PDF y la frase o la fila de cuadro de donde sale, copiadas tal cual.

## 2. Fuentes

Usa sólo los sitios de la Cámara de Diputados: `gaceta.diputados.gob.mx` y `[www.diputados.gob.mx](https://www.diputados.gob.mx)`. No
uses otros sitios ni fuentes secundarias (Hacienda, CEFP, prensa, FMI, OCDE, Wikipedia), aunque estén a
tu alcance, ni tu memoria. Si un sitio responde 403 o bloquea una ruta, no intentes rodearlo (otro
agente de usuario, encabezados, espejos): anótalo y sigue. Deja al menos un segundo entre descargas.

Cómo está ordenada la Gaceta Parlamentaria (revisado el 28-10-2026):

- Índice del mes: `https://gaceta.diputados.gob.mx/PDF/<leg>/<aaaa>/<mes>/index.html` (días con PDF)
  y `https://gaceta.diputados.gob.mx/Gaceta/<leg>/<aaaa>/<mes>/index.html` (versión HTML).
- Día: `https://gaceta.diputados.gob.mx/PDF/<leg>/<aaaa>/<mes>/<aaaammdd>.html` lista el PDF principal
  `<aaaammdd>.pdf` y los anexos `<aaaammdd>-<letra o romano>.pdf`. La versión HTML del día es
  `https://gaceta.diputados.gob.mx/Gaceta/<leg>/<aaaa>/<mes>/<aaaammdd>.html`.
- `<mes>`: ene, feb, mar, abr, may, jun, jul, ago, sep, oct, nov, dic.
- `<leg>` (legislatura): 57 = sep 1997 a ago 2000; 58 = sep 2000 a ago 2003; 59 = sep 2003 a ago
  2006; 60 = sep 2006 a ago 2009; 61 = sep 2009 a ago 2012; 62 = sep 2012 a ago 2015; 63 = sep 2015 a
  ago 2018; 64 = sep 2018 a ago 2021; 65 = sep 2021 a ago 2024; 66 = sep 2024 a ago 2027.
- La ruta `/Black/Gaceta/Anteriores/...` responde 403: no la uses.

Copias ya identificadas de 2015 a 2027. El integrador las descargó el 27-10-2026; comprueba que tu
descarga tiene el mismo SHA-256 (primeros 12 caracteres):

| t | URL | Gaceta | SHA-256 |
|---|---|---|---|
| 2015 | https://gaceta.diputados.gob.mx/PDF/62/2014/sep/20140905-D.pdf | 5-09-2014, anexo D | 58d762e9c91c |
| 2016 | https://gaceta.diputados.gob.mx/PDF/63/2015/sep/20150908-E.pdf | 8-09-2015, anexo E | 23cbd1e25fb9 |
| 2017 | https://gaceta.diputados.gob.mx/PDF/63/2016/sep/20160908-I.pdf | 8-09-2016, anexo I | 69da5658fd7e |
| 2018 | https://gaceta.diputados.gob.mx/PDF/63/2017/sep/20170908-C.pdf | 8-09-2017, anexo C | 2ce58a0eb06a |
| 2019 | https://gaceta.diputados.gob.mx/PDF/64/2018/dic/20181215-C.pdf | 15-12-2018, anexo C | 802e08aebf84 |
| 2020 | https://gaceta.diputados.gob.mx/PDF/64/2019/sep/20190908-C.pdf | 8-09-2019, anexo C | cc996351fc84 |
| 2021 | https://gaceta.diputados.gob.mx/PDF/64/2020/sep/20200908-C.pdf | 8-09-2020, anexo C | e9241f31b975 |
| 2022 | https://gaceta.diputados.gob.mx/PDF/65/2021/sep/20210908-C.pdf | 8-09-2021, anexo C | 85af840de478 |
| 2023 | https://gaceta.diputados.gob.mx/PDF/65/2022/sep/20220908-C.pdf | 8-09-2022, anexo C | b66945d5fd81 |
| 2024 | https://gaceta.diputados.gob.mx/PDF/65/2023/sep/20230908-C.pdf | 8-09-2023, anexo C | 10af9f3cfbb5 |
| 2025 | https://gaceta.diputados.gob.mx/PDF/66/2024/nov/20241115-C.pdf | 15-11-2024, anexo C | c9018ea6ef08 |
| 2026 | https://gaceta.diputados.gob.mx/PDF/66/2025/sep/20250908-C.pdf | 8-09-2025, anexo C | 6bfe63a30519 |
| 2027 | https://gaceta.diputados.gob.mx/PDF/66/2026/sep/20260908-C.pdf | 8-09-2026, anexo C | 5978f0631d2c |

El de 2025 es un escaneo sin capa de texto: lee sus páginas como imagen.

Dónde buscar primero de 2000 a 2014. Son pistas, no datos: confirma la fecha en el propio documento.

| t | Dónde buscar primero |
|---|---|
| 2000 | noviembre de 1999 (leg 57) |
| 2001 | diciembre de 2000 (leg 58); la Gaceta del 8-12-2000 tiene un anexo I |
| 2002 | noviembre de 2001 |
| 2003 | noviembre de 2002 |
| 2004 | septiembre a noviembre de 2003 (leg 59) |
| 2005 | septiembre a noviembre de 2004 |
| 2006 | septiembre de 2005; la Gaceta del 8-09-2005 tiene anexos I y II |
| 2007 | diciembre de 2006 (leg 60) |
| 2008 | septiembre de 2007; la Gaceta del 7-09-2007 tiene anexos I a III |
| 2009 | septiembre de 2008; la Gaceta del 8-09-2008 tiene un anexo I |
| 2010 | septiembre de 2009 (leg 61); también `[www.diputados.gob.mx/PEF2010/](https://www.diputados.gob.mx/PEF2010/)` |
| 2011 | septiembre de 2010 |
| 2012 | septiembre de 2011 |
| 2013 | diciembre de 2012 (leg 62); también `[www.diputados.gob.mx/PEF2013/](https://www.diputados.gob.mx/PEF2013/)` |
| 2014 | septiembre de 2013; la Gaceta del 8-09-2013 tiene anexos A a J |

Si para algún año el CGPE no está en esos sitios pero sí la iniciativa de Ley de Ingresos con su marco
macroeconómico (exposición de motivos), úsala y márcala en `tipo` como `exposicion_motivos_LIF`. Si el
documento sólo existe en HTML, guarda el HTML igual que un PDF, usa `pagina_pdf` = 0 y anota en `nota`
la sección. Si no encuentras nada, deja la fila del año en `T070_fuentes_v01.csv` con la nota de dónde
buscaste.

## 3. Definiciones y ámbito

- t es el año del presupuesto: el CGPE 2014 (entregado en septiembre de 2013) da t = 2014 y t−1 = 2013.
- Copia los números tal como están impresos, con sus decimales; punto decimal en `valor`.
- Signo: déficit y brecha negativa con signo menos. «Déficit de 2.5 % del PIB» → `valor` = -2.5, y la
  cita conserva la palabra «déficit».
- Si el documento da un rango, registra sus extremos en las variables `_inf` y `_sup`; si además da un
  puntual «para efectos de las estimaciones de finanzas públicas», ése va en la variable principal.
- Si sólo hay montos en pesos, registra el monto con su unidad; no lo conviertas a porcentaje del PIB.
- Si una variable aparece con valores distintos en el mismo documento (texto contra cuadro, o dos
  definiciones), registra todos, marca uno con `principal` = si y explica en `nota`.

Variables (columna `variable`):

| variable | Qué es | Unidad |
|---|---|---|
| fecha_presentacion | fecha de la Gaceta que publica el documento (aaaa-mm-dd) | fecha |
| pib_crec_t | crecimiento real del PIB previsto para t; el puntual que se usa para las finanzas públicas | % anual |
| pib_crec_t_inf, pib_crec_t_sup | extremos del rango previsto para t | % anual |
| pib_crec_tm1 | crecimiento real del PIB estimado para t−1 | % anual |
| pib_crec_tm1_inf, pib_crec_tm1_sup | extremos del rango estimado para t−1 | % anual |
| pib_nominal_t | PIB nominal previsto para t | miles de millones de pesos |
| inflacion_t | inflación prevista para t (diciembre a diciembre) | % |
| petroleo_t | precio previsto de la mezcla mexicana de exportación para t | dólares por barril |
| eua_pib_crec_t | crecimiento previsto del PIB de Estados Unidos para t | % anual |
| eua_pi_crec_t | crecimiento previsto de la producción industrial de Estados Unidos para t | % anual |
| balance_publico_t | meta de balance público para t con toda la inversión («balance público» o «balance económico»; nombre exacto en `definicion`) | % del PIB |
| balance_publico_sin_inv_t | meta de balance que excluye la inversión que la ley permite excluir (por ejemplo «sin inversión de Pemex» o «sin inversión de alto impacto») | % del PIB |
| balance_primario_t | meta de balance primario para t | % del PIB |
| rfsp_t | requerimientos financieros del sector público previstos para t | % del PIB |
| ingresos_petroleros_t | ingresos petroleros del sector público previstos para t | % del PIB |
| balance_publico_tm1, balance_publico_sin_inv_tm1, balance_primario_tm1, rfsp_tm1, ingresos_petroleros_tm1 | lo mismo, como cierre estimado para t−1 | % del PIB |
| brecha_tm1, brecha_t | brecha del producto que el documento informa para t−1 o para t | % del PIB potencial |
| pib_potencial_crec | crecimiento real del PIB potencial que el documento informa | % anual |

Si un documento no publica una variable, no inventes la fila: anótalo en la tabla de cobertura de la nota.

## 4. Producto esperado

Todo en la carpeta `T070/` del repositorio:

1. `T070_fuentes_v01.csv`: una fila por año t (28 filas), con las columnas exactas `anio_cgpe, url,
   fecha_gaceta, anexo, tipo, titulo_portada, paginas, capa_texto, sha256, bytes, nota`. `tipo`: CGPE |
   exposicion_motivos_LIF | otro. `titulo_portada`: el título literal de la portada. `capa_texto`: si | no.
2. `T070_cgpe_v01.csv`: una fila por cifra, con las columnas exactas `anio_cgpe, variable, valor, unidad,
   principal, definicion, cita_literal, pagina_pdf, pagina_impresa, cuadro, archivo, url, lectura,
   confianza, nota`.
   - `pagina_pdf`: página del archivo PDF, contando desde 1. `pagina_impresa`: el folio impreso, si lo hay.
   - `cita_literal`: la frase, copiada tal cual, que contiene el número; si sale de un cuadro, el
     encabezado de la columna y la fila completa.
   - `cuadro`: nombre o número del cuadro, si la cifra sale de uno.
   - `lectura`: texto (la cita se puede buscar en el texto del PDF) | imagen (leída de la imagen de la página).
   - `confianza`: verificada (la validación del punto 3 la encontró en su página) | probable (leída de
     imagen, o de un cuadro cuyo texto extraído no conserva la fila).
3. `T070_extrae_v01.py`: un programa que corre de principio a fin con `python3 T070_extrae_v01.py` desde
   `T070/` y que (a) descarga a `pdf/` cada URL de `T070_fuentes_v01.csv` que falte, (b) comprueba SHA-256
   y número de páginas, (c) extrae el texto de cada página y (d) valida cada fila de `T070_cgpe_v01.csv`:
   que la cita, con los espacios normalizados, esté en el texto de su página y que el valor esté en la
   cita. Usa la biblioteca que tengas (pdftotext, pypdf o PyMuPDF) y decláralo.
4. `T070_validacion_v01.csv`: la salida del programa, con `anio_cgpe, variable, pagina_pdf,
   cita_en_pagina, valor_en_cita, nota` (si | no | no_aplica para las leídas de imagen).
5. `T070_nota_v01.md`: con el encabezado YAML de abajo, una tabla de cobertura (año × variable: hay / no
   se publica / no encontrado), los huecos con dónde se buscó, y la declaración de la sección 7.

```yaml
---
tarea: T070
titulo: "Cifras de los CGPE 2000 a 2027 con página y frase"
nivel: B
destino: claude-code
replica_en:
fecha_encargo: 2026-10-28
solicita: alejandro
---
```

No subas los PDF al repositorio: pon `T070/pdf/` en `.gitignore`. Haz commit y push a la rama de la
sesión; no abras pull request ni fusiones a `main`.

Mensaje final: (1) el nombre de la rama; (2) los archivos con su SHA-256; (3) la respuesta a
«¿modificaste algo fuera de lo pedido?»; (4) estas dos filas llenas, sin acentos ni eñes, una línea cada una:

```
tarea,fecha_encargo,titulo,nivel,sistema_ejecuta,sistema_replica,insumos,producto,criterio_aceptacion,estado,fecha_cierre,verificado_por,notas
T070,2026-10-28,"Cifras de los CGPE 2000 a 2027 con pagina y frase",B,claude-code (Claude Code en la nube; cuenta Max),,"Gaceta Parlamentaria y sitio de la Camara de Diputados (URL en T070_fuentes_v01.csv)","rama <rama> del repositorio t070-cgpe: T070/T070_cgpe_v01.csv; T070_fuentes_v01.csv; T070_validacion_v01.csv; T070_extrae_v01.py; T070_nota_v01.md","Seccion 5 de ENCARGO_T070_v01.md",EN_COTEJO,<aaaa-mm-dd>,,"<anos sin documento; numero de cifras; numero leidas de imagen>"
```

```
id,fecha,desarrollador,herramienta,version,cuenta_alias,tarea,proposito,insumo,producto,prompt_ref,verificado_por,fecha_verificacion,estado,entra_en_publicacion
U049,<aaaa-mm-dd>,Anthropic,Claude Code (sesion en la nube),<modelo>,claude-max,T070,"Extraccion de cifras de los CGPE 2000-2027 con pagina y frase","Gaceta Parlamentaria (URL en T070_fuentes_v01.csv)","rama <rama>, carpeta T070/","ENCARGO_T070_v01.md, pegado como instruccion",,,PENDIENTE_VERIFICACION,no
```

## 5. Criterio de aceptación

Escrito antes de ejecutar, el 28-10-2026. Lo aplica el integrador, no quien ejecuta.

- `T070_fuentes_v01.csv` tiene las 28 filas: cada una con URL, SHA-256 y páginas, o con la nota de por
  qué no se encontró y dónde se buscó.
- Para cada año con documento hay `fecha_presentacion`, `pib_crec_t`, `pib_crec_tm1` y al menos una meta
  de balance para t, o la nota dice que el documento no la publica.
- Cada fila de `T070_cgpe_v01.csv` tiene `pagina_pdf` y `cita_literal`; las de `lectura` = texto pasan la
  validación (`cita_en_pagina` = si y `valor_en_cita` = si).
- El integrador descarga cada PDF desde su URL, comprueba el SHA-256 y repite la validación con un
  programa propio; la fila que no pasa no entra.
- De 2015 a 2027, `pib_potencial_crec` coincide con las cifras que el integrador ya cotejó contra la
  página (no se dan aquí a propósito).
- El programa corre de principio a fin en una máquina limpia.

## 6. Fuera de alcance

- Cálculos de cualquier tipo: conversiones a porcentaje del PIB, brechas, promedios, regresiones.
- Fuentes distintas de las de la sección 2, y cifras de memoria.
- Cambiar algo del repositorio fuera de `T070/` y `.gitignore`.

## 7. Declaración de quien ejecuta

Llenar en `T070_nota_v01.md`. Obligatorio.

- Capacidades reales en esta sesión (leer, ejecutar código, buscar en la web, escribir archivos):
- Lenguaje, versión y paquetes:
- Años sin documento y dónde se buscó:
- Qué no se pudo hacer y por qué:
- Supuestos que hubo que introducir (uno por línea; si no hubo, escribir «ninguno»):
- Advertencias sobre la calidad del resultado:
- Confirmación de que no se usaron otras fuentes ni la memoria:
