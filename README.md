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
![altimg](https://media.geeksforgeeks.org/wp-content/uploads/Thread_Pool.jpg) <br />
For this code I'm asked for academic purposes to implement multi threading in it which as described in geeks for geeks is a way our code to do multitasking by commanding different threads which are the smallest unit of proccessing that can be performed by an OS, however there is always the problem of overheading (taking more resources and time that the problem requires) so to solve that i'm using the architecture of thread pools that enhance overall performance by lowering the overhead of thread generation and destruction through thread reuse.

## Implementation
With that said and done lets start deconstructing the code
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
## The time complexity
The time complexity of this code is one of O(n * k) n being the number of ships in the caravan and k the number of attacks the kraken si going to realize

## The fastest solution following this approach
This isn't the fastest solution for the problem however it is the fastest solution that includes multi threading however because according to the AI github copilot the multi-threading and recursion of my code results taxing in memory and time so it proposes the following solution that has a complexity of O(n).
```python
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
```
## Testing
Since the testing velocities may vary according to the device codeforces lend us to check our results I've created a file replicating the test cases codeforces will throw at us in the input.txt file and the results will be presented in the output.txt file
```txt
11
4 5
1 2 4 3
4 6
1 2 4 3
5 20
2 7 1 8 2
2 2
3 2
2 15
1 5
2 7
5 2
10 9999999999
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
2 2147483648
1000000000 1000000000
2 1000000000
1000000000 1000000000
1 10000000000000
1
2 10
2 2
```
### Bibliography:
[1] https://www.geeksforgeeks.org/multithreading-python-set-1/ <br />
[2] https://www.geeksforgeeks.org/thread-pool-in-cpp/
