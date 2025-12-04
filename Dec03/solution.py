def calculate_max_joltage(bank:str):
    """get max excluding last entry because we need
    two digits"""
    first_max = max(bank[:-1])
    max_index = bank.index(first_max)
    next_max = max(bank[max_index+1:])
    max_joltage = int(first_max+next_max)
    return max_joltage

def calculate_max_joltage_recursive(
    bank:str,
    n_batteries:int,
    joltage:str,
    max_index:int):
    total_batteries = 12
    
    if n_batteries == 1:
        max_joltage = max(bank)
        joltage = joltage + max_joltage
        return int(joltage)

    else:
        max_joltage = max(
        bank[:-(n_batteries-1)]
        )
        max_index = bank.index(max_joltage)
        joltage = joltage + max_joltage
        return calculate_max_joltage_recursive(
            bank[max_index+1:],
            n_batteries-1,
            joltage,
            max_index
            )    



joltages = []
with open("Dec03/input") as file:
    while line:=file.readline():
        bank = line.rstrip()
        max_joltage = calculate_max_joltage_recursive(bank,12, "", 0)
        print(f"Max Joltage from {bank}: {max_joltage}")
        joltages.append(max_joltage)

print(f"Total joltage: {sum(joltages)}")
