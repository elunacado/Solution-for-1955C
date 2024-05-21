from concurrent.futures import ThreadPoolExecutor

def removeZeroes(ships):
    while 0 in ships:
        ships.remove(0)

def recursive_attack(numberOfAttacks, ships, attack_count=0):
    if numberOfAttacks == 0 or not ships:
        if ships:
            head = ships[0]
            tail = ships[-1]
        else:
            head = tail = None
        return head, tail

    if attack_count % 2 == 0:  # Ataque a la cabeza
        ships[0] -= 1
        if ships[0] <= 0:
            ships[0] = 0
            removeZeroes(ships)
    else:  # Ataque a la cola
        ships[-1] -= 1
        if ships[-1] <= 0:
            ships[-1] = 0
            removeZeroes(ships)

    with ThreadPoolExecutor(max_workers=10) as executor:
        future = executor.submit(recursive_attack, numberOfAttacks - 1, ships, attack_count + 1)
        return future.result()

ships = [1, 2, 4, 3]
numberOfAttacks = 5
print(recursive_attack(numberOfAttacks, ships))