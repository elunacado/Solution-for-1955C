#THIS CODE IS NOT WRITTEN BY ME.
#I HAVE TAKEN THIS CODE FROM GITHUB COPILOT.
#I AM USING THIS CODE TO DEMOSTRATE THE FASTEST SOLUTION FOR THE PROBLEM.
from collections import deque

t = int(input())

def attack(numberOfAttacks, ships):
    ships = deque(ships)
    sunken_ships = 0
    attack_count = 0

    while numberOfAttacks > 0 and ships:
        if attack_count % 2 == 0:  # Attack the head
            ships[0] -= 1
            if ships[0] <= 0:
                ships.popleft()
                sunken_ships += 1
        else:  # Attack the tail
            ships[-1] -= 1
            if ships[-1] <= 0:
                ships.pop()
                sunken_ships += 1

        numberOfAttacks -= 1
        attack_count += 1

    return sunken_ships

for _ in range(t):
    n, k = map(int, input().split())
    ships = list(map(int, input().split()))
    result = attack(k, ships)
    print(result)