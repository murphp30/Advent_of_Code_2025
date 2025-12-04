import re

def sum_around(grid:list, index:tuple, max_rows:int, max_cols:int):
    surrounding_indices = []
    for i in [-1,0,1]:
        if index[0]+i < 0  or index[0]+i>max_rows:
            continue
        for j in [-1,0,1]:
            if index[1]+j < 0  or index[1]+j>max_cols:
                continue
            if i == 0 and j == 0:
                continue
            surrounding_indices.append((index[0]+i, index[1]+j))
    
    roll_in_grid = [ind in grid for ind in surrounding_indices]
    
        
    return sum(roll_in_grid)

paper_roll = re.compile("@")

paper_indices = []
with open("Dec04/input") as file:
    for i, line in enumerate(file):
        row = line.rstrip()
        paper_matches = paper_roll.finditer(row)
        for match in paper_matches:
            paper_indices.append((i, match.start()))

n_rolls = 0
for index in paper_indices:
    if sum_around(paper_indices, index,i, len(row)) < 4:
        n_rolls+=1

print(f"Total number of accessible rolls: {n_rolls}")