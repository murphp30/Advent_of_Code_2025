import csv

def factorise(n):
    factors = []
    for i in range(1,n):
        if n%i == 0:
            factors.append(i)
    return sorted(factors)

def check_invalid(id_str:str) -> Bool:
    id_len = len(id_str)
    if id_len == 2 or id_len == 3:
            id_factors = [1]
    else:
        id_factors = factorise(id_len)
    
    for factor in id_factors:
        id_split = [id_str[j:j+factor] for j in range(0,len(id_str),factor)]
        if all(id_part == id_split[0] for id_part in id_split):
            print(f"ID {id_str} invalid!")
            return True
        else:
            continue


with open("Dec02/input.csv") as f:
    input_reader = csv.reader(f)
    inputs = next(input_reader)

part1 = False
invalid_ids = []
for input_range in inputs:
    print(input_range)
    start, end = input_range.split("-")
    start_int = int(start)
    end_int = int(end)

    for i in range(start_int, end_int+1):
        id_str = str(i)
        id_len = len(id_str)
        if part1:
            if id_len%2 == 1:
                    continue

            if id_str[:id_len//2] == id_str[id_len//2:]:
                print(f"ID {id_str} invalid!")
                invalid_ids.append(i)
        else:

            if check_invalid(id_str):
                    invalid_ids.append(i)

print(f"Total invalid IDs {sum(invalid_ids)}")