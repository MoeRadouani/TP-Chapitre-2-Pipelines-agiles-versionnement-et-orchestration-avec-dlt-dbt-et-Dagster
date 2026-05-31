import duckdb

db_path = "ventes.duckdb"
required_columns = {"date", "produit", "categorie", "quantite", "prix_unitaire", "ville"}

# Connexion à la base de données DuckDB
con = duckdb.connect(db_path)

try:
    # 1. Validation du schéma (Vérification des colonnes)
    columns = con.execute("DESCRIBE ventes_raw").fetchall()
    existing_columns = {col[0] for col in columns}
    missing = required_columns - existing_columns
    
    if missing:
        raise ValueError(f"Colonnes manquantes dans la table : {missing}")
        
    # 2. Validation de la qualité (Vérification des valeurs NULL)
    null_count = con.execute("""
        SELECT COUNT(*) 
        FROM ventes_raw 
        WHERE produit IS NULL 
           OR quantite IS NULL 
           OR prix_unitaire IS NULL
    """).fetchone()[0]

    if null_count > 0:
        raise ValueError(f"Données invalides : {null_count} lignes incomplètes détectées.")
    else:
        print("Validation réussie : schéma et qualité minimale OK")

finally:
    # Fermeture propre de la connexion, même en cas d'erreur ou d'exception
    con.close()