# TP Chapitre 2 — Pipeline de données local

Pipeline : `CSV → pandas → DuckDB → dbt → Dagster`

## Installation

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
pip install -r requirements.txt
```

## Exécution

```bash
python pipeline/ingest.py
python pipeline/validate.py
cd dbt_pipeline && dbt run --profiles-dir . && dbt test --profiles-dir . && cd ..
dagster dev -f pipeline/orchestrate.py   # http://localhost:3000
```

## Stack

`pandas` · `DuckDB` · `dbt` · `Dagster` · `Git`
