import random

import pandas as pd

from .normalize import normalize

def ask_question(df: pd.DataFrame):
    r = random.randint(0, len(df) - 1)
            
    ask = df.iloc[r]
    answer = input(f"Quelle est la capitale de {ask["country"]} ? ")
    
    df.drop(df.index[r], inplace=True)
    
    if (normalize(answer) == normalize(str(ask["capital"]))):
        print("Correct")
        return True, ask
    else:
        print(f"Faux c'est {ask["capital"]}")
        return False, ask
