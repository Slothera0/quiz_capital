import pandas as pd
from src.getter.get_Africa import get_Africa
from src.getter.get_Europe import get_Europe
from src.getter.get_North_America import get_North_America
from src.getter.get_South_America import get_South_America
from src.getter.get_Asia import get_Asia
from src.getter.get_Oceania import get_Oceania
from src.getter.get_world import get_world

def launch_option():
    
    
    option = int(input(
        "Quel mode vous voulez vous faire ?\n" +
            "[1] Le monde, \n" +
            "[2] L'Amérique du Nord, \n" +
            "[3] L'Amérique du Sud, \n" +
            "[4] L'Europe, \n" +
            "[5] L'Asie, \n" +
            "[6] L'Océanie, \n" +
            "[7] L'Afrique, \n" +
            "[8] Les pays souvent échoués, \n" +
            "[9] Statistique \n"
        ))
    
    match option:
        case 1:
            return get_world()
        case 2:
            return get_North_America()
        case 3:
            return get_South_America()
        case 4:
            return get_Europe()
        case 5:
            return get_Asia()
        case 6:
            return get_Oceania()
        case 7:
            return get_Africa()
        case 8:
            print("Pas encore implémenté")
            SystemExit(0)
        case 9:
            df = pd.read_csv("database.csv", sep=";")
            print(df)
            SystemExit(0)
        case _:
            print("Option invalide")
            SystemExit(0)