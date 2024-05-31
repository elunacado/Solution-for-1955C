# Hand in the evidence 4
## Problem
For this hand-in, I decided to solve a Codeforces problem <a>https://codeforces.com/problemset/problem/1955/C</a> which describes a situation in which a kraken is attacking a ship caravan, and we have to alternate between subtracting 1 from the head of the array that represents the caravan or one from the tail for each attack of the kraken. However, the Kraken cannot attack the sunken ships (those that reach zero). So an example of how the situation should be like this: </br>

## How the solution should work
Number of attacks by the kraken: 5
* [1, 2, 3, 4, 5] The caravan meets the kraken and gets attacked
* [0,2,3,4,5,3] the kraken attacks the head of the caravan and sinks a ship removing it from the array, Number of attacks: 4
* [2, 3, 4, 5] The Kraken attacks the bottom of the caravan, removing 1 of its health pool. Number of attacks: 3
* [1, 3, 4, 5] The Kraken attacks the head of the caravan, removing 1 of its health pool, Number of attacks: 2
* [1, 3, 4, 1] The Kraken attacks the bottom of the caravan, removing 1 of its health pool, Number of attacks: 1
* [0, 3, 4, 5] The Kraken attacks the head of the caravan and sinks a ship, removing it from the array. Number of attacks: 0
  
Leaving the following amount of fallen ships equal to 2 <br />


## Modal
![altimg](https://media.geeksforgeeks.org/wp-content/uploads/Thread_Pool.jpg) <br />
For this code, I'm asked for academic purposes to implement multi-threading in it, which, as described in geeks for geeks, is a way for our code to do multitasking by commanding different threads, which are the smallest unit of processing that can be performed by an OS. However, however there is always the problem of overheading (taking more resources and time than the problem requires), so to solve that, I'm using the architecture of thread pools that enhances overall performance by lowering the overhead of thread generation and destruction through thread reuse.

The way my code works is that every time the function calls itself, a new thread from the thread pool will jump in to solve the problem and set the other will be set on wait this process will be repeated over and over until the base case is reached and all occupied threads are released<br />

## Implementation
With that said and done lets start deconstructing the code
```python
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
```

At last, we needed to make this code compatible with the codeforces, so we added the following steps <br />

We import the ThreadPool
```python
  from concurrent.futures import ThreadPoolExecutor
```
We assign a variable for the number of tests that we're running
```python
  t = int(input())
```
We create the recursive function, which receive the number of attacks of the kraken, the array of the health of the ships, the attack counter that'll help us assign where the attack is going to land, and finally the number of sunken ships. Furthermore, we start the function by adding to the amount of sunken ships 1 for every zero in the array to eliminate them after
```python
def recursive_attack(numberOfAttacks, ships, attack_count=0, sunken_ships=0):
    sunken_ships += len([ship for ship in ships if ship <= 0])  # Count sunken ships
    ships = [ship for ship in ships if ship > 0]  # Remove sunken ships
```
After this, we establish the limit so that when the number of attacks reaches 0, we're returning the number of sunken ships, and it will make the decision if the kraken is attacking the head or the tail of the caravan
```python
 if numberOfAttacks == 0 or not ships:
        return sunken_ships

    if attack_count % 2 == 0:  # Attack the head
        ships[0] -= 1
    else:  # Attack the tail
        ships[-1] -= 1
```
Using the Thread Pool, with 20 threads (in this code called workers), we submit to the executor the call of the recursive function, subtracting 1 from the variable of the number of attacks and adding 1 to the attack count, as well as assigning a new thread to each time we call the recursive function, and we return the result
```python
   with ThreadPoolExecutor(max_workers=20) as executor:
        future = executor.submit(recursive_attack, numberOfAttacks - 1, ships, attack_count + 1, sunken_ships)
        return future.result()
```

We read the number of ships, the number of attacks by the kraken, and finally the health of each ship, printing the result of the amount of sunken ships in the output.txt file
```python
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
```
## The time complexity
The time complexity of this code is one of O(n * k), with n being the number of ships in the caravan and k being the number of attacks the Kraken is going to realize

## The fastest solution following this approach
This isn't the fastest solution for the problem; however, it is the fastest solution that includes multi-threading, because according to the AI GitHub copilot, the multi-threading and recursion of my code result in a tax on memory and time, so it proposes the following solution that has a complexity of O(n).
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
Since the testing velocities may vary according to the device codeforces lend us to check our results, I've created a file replicating the test cases codeforces will throw at us in the input.txt file, and the results will be presented in the output.txt file <br />

Number of test cases
```txt
8
```
Number of ships and number of attacks by the Kraken
```txt
5 15
```
Array with the health of the ships of the caravan
```txt
1 3 4 6
```
```txt
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
2 10
2 2
```
And to run them, you just have to insert the command python main.py and check the output text file
### Bibliography:
[1] https://www.geeksforgeeks.org/multithreading-python-set-1/ <br />
[2] https://www.geeksforgeeks.org/thread-pool-in-cpp/

