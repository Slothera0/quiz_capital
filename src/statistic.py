import pandas as pd

class Statistic(Exception):
    pass

def statistic():
    
    df = pd.read_csv("database.csv", sep=";")
    
    affichage = df.copy()
    affichage["winrate"] = (df["good"] / df["total"] * 100).round(1)
    affichage = affichage.sort_values("winrate", ascending=False)
    affichage["winrate"] = affichage["winrate"].astype(str) + '%'

    print(affichage.to_string(index=False))