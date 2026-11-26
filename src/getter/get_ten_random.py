import pandas as pd
import random

def get_ten_random():
    
    df = pd.read_csv("database.csv", sep=";")
    df = df.sample(10)
    
    return (df[["country", "capital"]])