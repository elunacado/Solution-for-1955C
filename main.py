from concurrent.futures import ThreadPoolExecutor

def recursive_attack(numberOfAttacks, ships, attack_count=0, sunken_ships=0):
    if numberOfAttacks == 0 or not ships:
        return sunken_ships

    if attack_count % 2 == 0:  # Attack the head
        ships[0] -= 1
    else:  # Attack the tail
        ships[-1] -= 1

    sunken_ships += len([ship for ship in ships if ship <= 0])  # Count sunken ships
    ships = [ship for ship in ships if ship > 0]  # Remove sunken ships

    with ThreadPoolExecutor(max_workers=20) as executor:
        future = executor.submit(recursive_attack, numberOfAttacks - 1, ships, attack_count + 1, sunken_ships)
        return future.result()

# Read values from a file
with open('input.txt', 'r') as f:
    lines = f.readlines()

# Initialize an empty list to store the results
results = []

# Loop over the lines in the file
for i in range(1, len(lines), 2):
    numberOfShips, numberOfAttacks = map(int, lines[i].split())
    ships = list(map(int, lines[i+1].split()))  # The health of each ship is one line below the number of attacks
    results.append(recursive_attack(numberOfAttacks, ships))

# Write the results to a file
with open('output.txt', 'w') as f:
    for result in results:
        f.write(f"Number of sunken ships: {result}\n")