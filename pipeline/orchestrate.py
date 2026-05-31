from dagster import job, op
import os

@op
def ingest():
    os.system("python pipeline/ingest.py")
    return "ok"

@op
def validate(prev):  # ← rename _ to anything real
    os.system("python pipeline/validate.py")
    return "ok"

@op
def transform(prev):  # ← same here
    os.system("cd dbt_pipeline && dbt run --profiles-dir .")
    return "ok"

@op
def test_data(prev):  # ← and here
    os.system("cd dbt_pipeline && dbt test --profiles-dir .")
    return "ok"

@job
def ventes_pipeline():
    test_data(transform(validate(ingest())))