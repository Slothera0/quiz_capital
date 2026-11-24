import pandas as pd

def get_Asia():
    
    df = pd.read_csv("database.csv", sep=";")
    
    return (df.loc[df["continent"] == "Asia", ["country", "capital"]])