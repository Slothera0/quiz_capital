import pandas as pd

def update_db(good_answer, bad_answer):
    
    df = pd.read_csv("database.csv", sep=";")
    
    if "good" not in df.columns:
        df["good"] = 0
    if "bad" not in df.columns:
            df["bad"] = 0
    if "total" not in df.columns:
            df["total"] = 0
        
    
    for country, capital in good_answer:
        df.loc[df["country"] == country, "good"] += 1
        df.loc[df["country"] == country, "total"] += 1
    for country, capital in bad_answer:
        df.loc[df["country"] == country, "bad"] += 1
        df.loc[df["country"] == country, "total"] += 1
    
    df.to_csv(
        "database.csv",
        index=False,
        sep=";",
        encoding="utf-8-sig",
    )