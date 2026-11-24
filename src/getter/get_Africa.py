import pandas as pd

def get_Africa():
    
    df = pd.read_csv("database.csv", sep=";")
    
    return (df.loc[df["continent"] == "Africa", ["country", "capital"]])