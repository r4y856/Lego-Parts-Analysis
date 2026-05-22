import duckdb
import os

conn = duckdb.connect("lego.db")

files = [
    "themes.csv",
    "colors.csv",
    "part_categories.csv",
    "parts.csv",
    "part_relationships.csv",
    "elements.csv",
    "sets.csv",
    "minifigs.csv",
    "inventories.csv",
    "inventory_parts.csv",
    "inventory_sets.csv",
    "inventory_minifigs.csv",
]

for file in files:
    path = os.path.join("inventory_files", file)

    if os.path.exists(path):
        table = file.replace(".csv", "")
        conn.execute(f"""CREATE TABLE IF NOT EXISTS {table} AS SELECT * FROM read_csv_auto('{path}')""")
        
conn.close()




