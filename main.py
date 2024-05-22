import sys
from concurrent.futures import ThreadPoolExecutor

def recursive_attack(numberOfAttacks, ships, attack_count=0):
    ships = [ship for ship in ships if ship > 0] # Remove ships with 0 health
    
    if numberOfAttacks == 0 or not ships:
        return (ships[0], ships[-1]) if ships else (None, None)

    if attack_count % 2 == 0:  # Attack the head
        ships[0] -= 1
    else:  # Attack the tail
        ships[-1] -= 1

    with ThreadPoolExecutor(max_workers=100) as executor:
        future = executor.submit(recursive_attack, numberOfAttacks - 1, ships, attack_count + 1)
        return future.result()

def main():
    input = sys.stdin.read
    data = input().strip().split()

    index = 0
    t = int(data[index])
    index += 1

    results = []
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2

        durabilities = list(map(int, data[index:index + n]))
        index += n

        # Perform the recursive attack and get the remaining ships
        head, tail = recursive_attack(k, durabilities)
        if head is None:
            results.append(0)
        else:
            results.append(len([ship for ship in durabilities if ship <= 0]))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
