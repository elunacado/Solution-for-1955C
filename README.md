# Hand in the evidence 4
## Problem
For this hand in I decided to solve a Codeforces problem <a>https://codeforces.com/problemset/problem/1955/C</a> which describe us a situation in which a kraken is attackin ship caravan and we have to alternate between subtracting 1 from the head of the array that represents the caravan or one from the tail for each attack of the kraken however the kraken cannot attack the sunken ships (those that reach zero). So a example of how the situation should be like this: </br>

## How the solution should work
Number of attacks of the kraken: 5
* [1,2,3,4,5,3] the caravan meets the kraken and gets attacked
* [0,2,3,4,5,3] the kraken attacks the head of the caravan and sunks a ship removing it from the array, Number of attacks: 4
* [2,3,4,5,2] the kraken attacks the bottom of the caravan removing 1 its health pool, Number of attacks: 3
* [1,3,4,5,2] the kraken attacks the head of the caravan removing 1 its health pool, Number of attacks: 2
* [1,3,4,5,1] the kraken attacks the bottom of the caravan removing 1 its health pool, Number of attacks: 1
* [0,3,4,5,3] the kraken attacks the head of the caravan and sunks a ship removing it from the array, Number of attacks: 0
  
Leaving the following amount of fallen ships equal to 2 <br />


## Modal

With that said and done lets start deconstructing the code
## Implementation
```python
from concurrent.futures import ThreadPoolExecutor

t = int(input())

def recursive_attack(numberOfAttacks, ships, attack_count=0, sunken_ships=0):
    sunken_ships += len([ship for ship in ships if ship <= 0])  # Count sunken ships
    ships = [ship for ship in ships if ship > 0]  # Remove sunken ships

    if numberOfAttacks == 0 or not ships:
        return sunken_ships

    if attack_count % 2 == 0:  # Attack the head
        ships[0] -= 1
    else:  # Attack the tail
        ships[-1] -= 1

    with ThreadPoolExecutor(max_workers=20) as executor:
        future = executor.submit(recursive_attack, numberOfAttacks - 1, ships, attack_count + 1, sunken_ships)
        return future.result()

# Iterate through each test case
for _ in range(t):
    # Read input for each test case
    n, k = map(int, input().split())
    ships = list(map(int, input().split()))
    result = recursive_attack(k, ships)
    print(result)
```

At last we needed to make this code compatible with the codeforces so we added the following steps <br />

We import the ThreadPool
```python
  from concurrent.futures import ThreadPoolExecutor
```
We asign a variable for the number of tests that we're running
```python
  t = int(input())
```
We create the recursive function which receive the number of attacks of the kraken, the array of the health of the ships, the attack counter that'll help us asignate where the attack is going to land, and finally the number of sunken ships, and we start the function by adding to the amount of sunken ships 1 for every zero in the array to eliminate them after
```python
def recursive_attack(numberOfAttacks, ships, attack_count=0, sunken_ships=0):
    sunken_ships += len([ship for ship in ships if ship <= 0])  # Count sunken ships
    ships = [ship for ship in ships if ship > 0]  # Remove sunken ships
```
After this we stablish the limit that when the number of attacks reaches 0 we're returning the number of sunken ships and it will make the decision if the kraken is attacking the head or the tail of the caravan
```python
 if numberOfAttacks == 0 or not ships:
        return sunken_ships

    if attack_count % 2 == 0:  # Attack the head
        ships[0] -= 1
    else:  # Attack the tail
        ships[-1] -= 1
```
Using the Thread Pool in with 20 threads (in this code called workers) we submit to the executor the call of the recursive function subtracting 1 to the variable of number of attacks and adding 1 to the attack count asigning a new thread to each time we call the recursive function and we return the result 

We read the number of ships, number of attacks of the kraken and finally the health of each ship printing the result of the amount of sunken ships
```python
for _ in range(t):
    n, k = map(int, input().split())
    ships = list(map(int, input().split()))
    result = recursive_attack(k, ships)
    print(result)
```
