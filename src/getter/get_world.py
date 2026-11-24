import pandas as pd

def get_world():
    
    df = pd.read_csv("database.csv", sep=";")
    
    return (df.loc[["country", "capital"]])