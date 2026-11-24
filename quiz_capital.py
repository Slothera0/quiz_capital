import pandas as pd

from src.ask_question import ask_question
from src.init_db import init_db
from src.update_db import update_db
from src.launch_option import launch_option

def main():
    
    init_db()
    world = launch_option()

    good_answer = []
    bad_answer = []
    total = len(world)
    
    for i in range(total):
        print(f"{i}/{total} ", end="")
        result, answer = ask_question(world)
        if result != False:
            good_answer.append(answer)
        else:
            bad_answer.append(answer)

    
    print(f"Votre score est {len(good_answer)}/{total}")
    update_db(good_answer, bad_answer)
    
    return (0)

if __name__ == "__main__":
    raise SystemExit(main())