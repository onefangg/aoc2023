import sys
from dataclasses import dataclass


CUBE_CONFIG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


@dataclass
class Game:
    id: int
    cube_sets: list[str]


def parse_to_game(input_str: str) -> Game:
    split_by_semicolon = input_str.split(": ")
    game_id = int(split_by_semicolon[0].split(" ")[-1])
    return Game(id=game_id, cube_sets=split_by_semicolon[1].split("; "))


def is_cube_set_possibe(input_str: str) -> bool:
    cubes = input_str.split(", ")
    for cube in cubes: 
        num_cube, colour_cube = cube.split(" ")
        if CUBE_CONFIG[colour_cube] < int(num_cube):
            return False
    return True
    

if __name__ == "__main__":
    rolling_sum = 0

    for line in sys.stdin:
        one_game: Game = parse_to_game(line.strip())    
        rolling_sum += one_game.id

        for cube_set in one_game.cube_sets:
            if not is_cube_set_possibe(cube_set):
                rolling_sum -= one_game.id
                break
    print(rolling_sum)



