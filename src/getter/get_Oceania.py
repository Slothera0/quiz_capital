import pandas as pd

def get_Oceania():
    
    df = pd.read_csv("database.csv", sep=";")
    
    return (df.loc[df["continent"] == "Oceania", ["country", "capital"]])