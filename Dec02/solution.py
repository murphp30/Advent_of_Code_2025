import csv

with open("input.csv") as f:
    input_reader = csv.reader(f)
    inputs = next(input_reader)

part1 = False
invalid_ids = []
for input_range in inputs:
    # print(input_range)
    start, end = input_range.split("-")
    start_int = int(start)
    end_int = int(end)

    for i in range(start_int, end_int+1):
        id_str = str(i)
        
        id_len = len(id_str)
        if part1:
            if id_len%2 == 1:
                    continue
            # print(id_str[:id_len//2], id_str[id_len//2:])
            if id_str[:id_len//2] == id_str[id_len//2:]:
                print(f"ID {id_str} invalid!")
                invalid_ids.append(i)
        else:
            
        

print(f"Total invalid IDs {sum(invalid_ids)}")