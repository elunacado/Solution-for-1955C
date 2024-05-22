from concurrent.futures import ThreadPoolExecutor

max_attacks = 10**15

def recursive_attack(numberOfAttacks, ships, attack_count=0):
    ships = [ship for ship in ships if ship > 0] # Remove ships with 0 health
    if numberOfAttacks == 0 or not ships:
        return (ships[0], ships[-1]) if ships else (None, None)

    if attack_count % 2 == 0:  # Attack the head
        ships[0] -= 1
    else:  # Attack the tail
        ships[-1] -= 1

    with ThreadPoolExecutor(max_workers=max_attacks) as executor:
        future = executor.submit(recursive_attack, numberOfAttacks - 1, ships, attack_count + 1)
        return future.result()

ships = [1, 2, 4, 3]
numberOfAttacks = 5
print(recursive_attack(numberOfAttacks, ships))