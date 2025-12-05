import time

start_time = time.time()
with open("Dec05/input") as f:
    database = f.read()


ingredient_id_ranges, ingredient_ids = database.split("\n\n")
ingredient_id_ranges = ingredient_id_ranges.split("\n")
ingredient_ids = ingredient_ids.split("\n")
read_time = time.time()
print(f"Time to read: {read_time-start_time}")
expanded_id_ranges = []

for id_range in ingredient_id_ranges:
    start_ind, end_ind = id_range.split("-")
    expanded_id_ranges.append(range(int(start_ind), int(end_ind)+1))

# expanded_id_ranges = chain(expanded_id_ranges)
# for eid in expanded_id_ranges:
#     print(eid)
expand_time = time.time()
print(f"Time to expand: {expand_time-read_time}")
n_fresh = 0
for ingredient_id in ingredient_ids:
    for expanded_id_range in expanded_id_ranges:
        if int(ingredient_id) in expanded_id_range:
            n_fresh += 1
            # print(f"Ingredient {ingredient_id} is fresh!")
            break
count_time = time.time()
print(f"Total fresh items: {n_fresh}")

print(f"Time to count: {count_time-expand_time}")

ingredient_id_tuples = [
    (int(i),int(j)) for i,j in [
        id_range.split('-') for id_range in ingredient_id_ranges
        ]
    ]

ingredient_id_tuples = sorted(ingredient_id_tuples)
total_fresh_ids = sum(v-k+1 for k,v in ingredient_id_tuples)

print(f"Total number of fresh ids including double counts: {total_fresh_ids}")
double_counted = 0
max_range = ingredient_id_tuples[0]
"""Try and account for double counting. Start with the first id range and call it max_range.
For each id_range after that, see if it is fully inside, overlapping or fully outside the max_range.
If fully inside, entire id_range is double counted.
If overlap, only overlap is double counted, update max_range.
If totally outside, no overlap, update max_range.
"""
for i, id_range in enumerate(ingredient_id_tuples):
    if i == 0:
        continue
    
    if id_range[0] >= max_range[0] and id_range[1] <= max_range[1]:
        overlap = id_range[1]-id_range[0]+1
        double_counted += overlap
        
    elif id_range[0] >= max_range[0] and id_range[0] <= max_range[1] and id_range[1] > max_range[1]:
        
        overlap = max_range[1]-id_range[0]+1
        double_counted += overlap
        max_range = (id_range[0], id_range[1])
        
    elif id_range[0] >= max_range[1]:
        max_range = (id_range[0], id_range[1])
        
print(f"Total double counts: {double_counted}")
total_fresh_ids = total_fresh_ids-double_counted

print(f"Total number of fresh ids: {total_fresh_ids}")