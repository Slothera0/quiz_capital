import pandas as pd
import json
from pathlib import Path

def init_db():
    
    path = Path("database.csv")
    if path.is_file():
        return
    
    with open("src/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    
    dfs = []
    
    for continent, countries in data.items():
        for country, capital in countries.items():
            new = pd.DataFrame([[continent, country, capital]], columns=["continent", "country", "capital"])
            dfs.append(new)
    
    total = pd.concat(dfs, ignore_index=True)
    
    total.to_csv(
        "database.csv",
        index=False,
        sep=";",
        encoding="utf-8-sig",
    )
