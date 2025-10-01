# Corpus español sobre depresión (v1.0)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17240022.svg)](https://doi.org/10.5281/zenodo.17240022)


**Descripción breve.** Colección de mensajes en español etiquetados binariamente: `label=0` (no depresión) y `label=1` (depresión). Este repositorio contiene los **archivos de datos**, scripts auxiliares y metadatos para facilitar el uso y la citación del corpus.

>  **Aviso ético:** Este dataset es para investigación y docencia. **No** sustituye diagnósticos clínicos ni debe usarse para evaluación individual de personas. Se aplicó anonimización básica (e-mails, teléfonos, URLs, @usuarios).

---

## Contenido
- `data/corpus.csv` — Datos tabulares en UTF-8 con cabeceras: `id,text,label`.
- `data/splits/` — Particiones sugeridas (`train.csv`, `val.csv`, `test.csv`).
- `scripts/` — Utilidades (anonimización, conversión desde .txt, estadísticas, *splits*, checksums).
- `CITATION.cff` y `CITATION.bib` — Cómo citarnos.
- `LICENSE` — Licencia de uso (CC BY 4.0).
- `DUA.md` — Acuerdo de uso de datos (opcional).
- `.zenodo.json` — Metadatos para Zenodo (para mintar DOI).
- `CHANGELOG.md` — Historial de cambios.

## Especificación del formato
CSV con cabeceras:
```csv
id,text,label
1,"me siento mejor hoy, salí a caminar",0
2,"no tengo ganas de nada y todo me pesa",1
```
- `id`: entero único por registro.  
- `text`: mensaje en español, limpio de PII (e-mails, @usuarios, teléfonos, URLs).  
- `label`: `0` = no depresión, `1` = depresión.

## Estadísticas
- N total: 2955
- Clase 0: 2421 (81.93%)
- Clase 1: 534 (18.07%)
- Longitud media (caracteres): 94
- Splits: train=2363, val=295, test=297 (seed=42, 80/10/10)

_Puedes regenerarlas con:_
```bash
python scripts/compute_stats.py data/corpus.csv
```

## Origen y anotación
- **Fuente:** textos **públicos** de redes sociales recopilados en **2023**, respetando los Términos de Servicio de las plataformas. Se comparten solo textos procesados y anonimizados.  
- **Criterios de inclusión/exclusión:** idioma español; eliminación de duplicados/spam; filtrado de entradas vacías; longitud mínima > 1 token.  
- **Guía de etiquetado (0/1):** `1` cuando el mensaje contiene señales explícitas relacionadas con depresión (p. ej., tristeza persistente, anhedonia, desesperanza, búsqueda de ayuda por depresión); `0` en caso contrario. _Las etiquetas no constituyen diagnóstico clínico._  
- **Anotadores y control de calidad:** **5 psicólogos** con experiencia clínica; resolución de discrepancias por consenso.  
- **Preprocesamiento:** anonimización básica (e-mails, teléfonos, URLs, @usuarios) y normalización ligera.

## Particiones
Se proporcionan `train/val/test` estratificadas (80/10/10) con semilla fija. Para recrearlas:
```bash
python scripts/make_splits.py data/corpus.csv --seed 42 --train 0.8 --val 0.1 --test 0.1 --outdir data/splits
```

## Licencia
Este dataset está bajo **Creative Commons Attribution 4.0 (CC BY 4.0)**. Puedes compartir y adaptar el material siempre que des **crédito** al autor. Texto legal: https://creativecommons.org/licenses/by/4.0/legalcode

## Cómo citar

**APA 7**  
Núñez-Prado, C. J., Talavera-Ortega, C., Sidorov, G., & Chanona-Hernández, L. (2025). *Corpus español etiquetado de depresión (v1.0)* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.17240022

**IEEE**  
C. J. Núñez-Prado, C. Talavera-Ortega, G. Sidorov, and L. Chanona-Hernández, “Corpus español etiquetado de depresión (v1.0),” Zenodo, Dataset, 2025. doi: 10.5281/zenodo.17240022.

## Contacto
Autor responsable: **César Jesús Núñez-Prado** · correo: **cnunezp@ipn.mx** · ORCID: **https://orcid.org/0000-0003-1700-9194**
