import re
import time

from itertools import repeat
from multiprocessing import Pool

def sum_around(grid:list, index:tuple, max_rows:int, max_cols:int):
    surrounding_indices = 0
    start_time = time.time()
    for i in [-1,0,1]:
        if index[0]+i < 0 or index[0]+i>max_rows:
            continue
        for j in [-1,0,1]:
            if index[1]+j < 0 or index[1]+j>max_cols:
                continue
            if i == 0 and j == 0:
                continue
            if (index[0]+i, index[1]+j) in grid:
                surrounding_indices += 1
            if surrounding_indices >= 4:
                return False
    return True

def update_grid(grid:list, index:tuple):
    grid[index[0]][index[1]] = "x"
    return grid

if __name__ == "__main__":
    start_time = time.time()
    paper_roll = re.compile("@")

    paper_indices = []
    grid = []
    with open("Dec04/input") as file:
        for i, line in enumerate(file):
            row = line.rstrip()
            grid.append(list(row))
            paper_matches = paper_roll.finditer(row)
            for match in paper_matches:
                paper_indices.append((i, match.start()))
    read_time = time.time()
    n_rolls = 0

    valid_indices = paper_indices
    total_rolls = []
    while True:
        with Pool() as p:
            n_roll_list = p.starmap(
                sum_around,
                zip(
                    repeat(valid_indices),
                    valid_indices,
                    repeat(i),
                    repeat(len(row))
                    )
                )
        
        n_rolls = sum(n_roll_list)
        if n_rolls == 0:
            break
        print(f"Number of rolls removed: {n_rolls}")
        total_rolls.append(n_rolls)
        # update paper_indices to include only valid rolls.
        valid_indices = [valid_indices[ind] for ind in range(len(valid_indices)) if not n_roll_list[ind]]

    calculate_time = time.time()
    print(f"Time to read: {read_time - start_time}")
    print(f"Time to calculate: {calculate_time - read_time}")
    print(f"Total number of accessible rolls: {sum(total_rolls)}")
