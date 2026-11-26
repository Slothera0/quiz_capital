import pandas as pd

def get_low_winrate():
    
    df = pd.read_csv("database.csv", sep=";")
    
    to_remove = []
    
    for index, ligne in df.iterrows():
        if ligne["total"] != 0 and ligne["good"] / ligne["total"] >= 0.5:
            to_remove.append(index)
    
    df = df.drop(to_remove)
    
    return (df[["country", "capital"]])