import pandas as pd

def get_Europe():
    
    df = pd.read_csv("database.csv", sep=";")
    
    return (df.loc[df["continent"] == "Europe", ["country", "capital"]])