"""
internal randomiser for poissonparler/chowtimechaos
copyright (c) 2023 mark joshwel <mark@joshwel.co>
"""


# use secure random number generator
from secrets import choice
from itertools import permutations
from typing import Generator
from sys import stderr


def randomise(sequence: str, times: int = 1) -> Generator[str, None, None]:
    randomised: set[str] = set()

    print("1", end="\r", file=stderr)
    all_possible_combinations: list[str] = [
        "".join(combination) for combination in permutations(sequence)
    ]

    # shuffle
    print("2", end="\r", file=stderr)
    while len(randomised) < len(all_possible_combinations):
        print(f"2: {len(randomised)}/{len(all_possible_combinations)}", end="\r", file=stderr)
        randomised.add(choice(all_possible_combinations))
    
    # pick out randomised
    print("\n", end="", file=stderr)
    everseen: set[str] = set()
    randomised_list: list[str] = list(randomised)

    for _ in range(len(randomised) if times == -1 else times):
        while (chosen := choice(randomised_list)) in everseen:
            chosen = choice(randomised_list)
        everseen.add(chosen)
        yield chosen

def main() -> None:
    try:
        while True:
            sequence: str = input("sequence> ")

            match sequence.split("/", maxsplit=1):
                case ["*", right]:
                    for randomised in randomise(right, times=-1):
                        print(randomised)
                    continue

                case [left, right]:
                    if all([char.isdigit() for char in left]):
                        for randomised in randomise(right, times=int(left)):
                            print(randomised)
                        continue

                    else:
                        for randomised in randomise(right):
                            print(randomised)
                        continue

                case [""]:
                    continue
                
                case _:
                    for randomised in randomise(sequence):
                        print(randomised)
                    continue

    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
