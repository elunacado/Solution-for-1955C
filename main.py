from concurrent.futures import ThreadPoolExecutor

t = int(input())

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

for _ in range(t):
    n, k = map(int, input().split())
    ships = list(map(int, input().split()))
    result = recursive_attack(k, ships)
    print(result)


