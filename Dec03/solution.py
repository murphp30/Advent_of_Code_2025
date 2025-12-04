def calculate_max_joltage(bank:str):
    # bank_list = [int(j) for j in bank]
    """get max excluding last entry because we need
    two digits"""
    first_max = max(bank[:-1])
    max_index = bank.index(first_max)
    next_max = max(bank[max_index+1:])
    max_joltage = int(first_max+next_max)
    return max_joltage

def calculate_max_joltage_recursive(bank:str, n_batteries:int):

    
    return


joltages = []
with open("Dec03/input") as file:
    while line:=file.readline():
        bank = line.rstrip()
        max_joltage = calculate_max_joltage(bank)
        print(f"Max Joltage from {bank}: {max_joltage}")
        joltages.append(max_joltage)

print(f"Total joltage: {sum(joltages)}")
