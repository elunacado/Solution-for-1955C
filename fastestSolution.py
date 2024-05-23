#THIS CODE IS NOT WRITTEN BY ME.
#I HAVE TAKEN THIS CODE FROM GITHUB COPILOT.
#I AM USING THIS CODE TO DEMOSTRATE THE FASTEST SOLUTION FOR THE PROBLEM. FOLLOWING THIS APPROACH
from collections import deque

t = int(input())

def attack(numberOfAttacks, ships):
    ships = deque(ships)
    sunken_ships = 0
    attack_count = 0
    
    ships = deque(ship for ship in ships if ship > 0)
    sunken_ships += len(ships) - len(ships)
    
    while numberOfAttacks > 0 and ships:
        if attack_count & 1 == 0:  # Attack the head
            ship = ships.popleft()
            ship -= 1
            if ship <= 0:
                sunken_ships += 1
            else:
                ships.appendleft(ship)
        else:  # Attack the tail
            ship = ships.pop()
            ship -= 1
            if ship <= 0:
                sunken_ships += 1
            else:
                ships.append(ship)

        numberOfAttacks -= 1
        attack_count += 1

    return sunken_ships

for _ in range(t):
    n, k = map(int, input().split())
    ships = list(map(int, input().split()))
    result = attack(k, ships)
    print(result)