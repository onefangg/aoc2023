import sys

from part1 import Game, parse_to_game


def parse_cube(cube: str) -> (int, int, int):
    cubes = cube.split(", ")
    red, green, blue = 0, 0, 0

    for c in cubes:
        num, color = c.split(" ")
        if color == "red":
            red = int(num)
        if color == "green":
            green = int(num)
        if color == "blue":
            blue = int(num)
    return (red, green, blue)


if __name__ == "__main__":
    rolling_sum = 0
    for line in sys.stdin:
        one_game = parse_to_game(line.strip())
        all_cubes = [parse_cube(cube) for cube in one_game.cube_sets]
        max_red = max(all_cubes, key=lambda x: x[0])[0]
        max_green = max(all_cubes, key=lambda x: x[1])[1]
        max_blue = max(all_cubes, key=lambda x: x[2])[2]
        rolling_sum += max_red * max_green * max_blue
    print(rolling_sum)
