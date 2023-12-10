"""
internal randomiser for poissonparler/chowtimechaos
copyright (c) 2023 mark joshwel <mark@joshwel.co>
"""


# use secure random number generator
from secrets import choice
from itertools import permutations


def main() -> None:
    try:
        while True:
            sequence: str = input("sequence> ")

            # generate every possible combination of the sequence
            all_possible_combinations: list[str] = [
                "".join(combination)
                for combination in permutations(sequence)
            ]

            # choose a random combination from the list
            random_combination: str = choice(all_possible_combinations)

            print(random_combination)
    
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
