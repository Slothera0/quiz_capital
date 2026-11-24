import pandas as pd

def get_North_America():
    
    df = pd.read_csv("database.csv", sep=";")
    
    return (df.loc[df["continent"] == "North_America", ["country", "capital"]])