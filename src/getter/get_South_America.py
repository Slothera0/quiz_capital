import pandas as pd

def get_South_America():
    
    df = pd.read_csv("database.csv", sep=";")
    
    return (df.loc[df["continent"] == "South_America", ["country", "capital"]])