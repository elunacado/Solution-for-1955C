# Hand in the evidence 4
For this hand in I decided to solve a Codeforces problem <a>https://codeforces.com/problemset/problem/1955/C</a> which describe us a situation in which a kraken is attackin ship caravan and we have to alternate between subtracting 1 from the head of the array that represents the caravan or one from the tail for each attack of the kraken however the kraken cannot attack the sunken ships (those that reach zero). So a example of how the situation should be like this: </br>

Number of attacks of the kraken: 5
* [1,2,3,4,5,3] the caravan meets the kraken and gets attacked
* [0,2,3,4,5,3] the kraken attacks the head of the caravan and sunks a ship removing it from the array, Number of attacks: 4
* [2,3,4,5,2] the kraken attacks the bottom of the caravan removing 1 its health pool, Number of attacks: 3
* [1,3,4,5,2] the kraken attacks the head of the caravan removing 1 its health pool, Number of attacks: 2
* [1,3,4,5,1] the kraken attacks the bottom of the caravan removing 1 its health pool, Number of attacks: 1
* [0,3,4,5,3] the kraken attacks the head of the caravan and sunks a ship removing it from the array, Number of attacks: 0
  
Leaving the following array as our output
[3,4,5,3]

With that said and done lets start deconstructing the code
## Implementation
 This imports the threadPoolExecutor class thet is used to create a pool of workers.
```python
  from concurrent.futures import ThreadPoolExecutor
```
This removes the zeroes from the array
```python
  def removeZeroes(ships):
    while 0 in ships:
        ships.remove(0)
```
This function assigns the head and the tail of the array, beside it keeps record from the number of attacks and attack count that'll help us decide if we're attacking the head o f the caravan or the tail of it.
```python
def recursive_attack(numberOfAttacks, ships, attack_count=0):
    if numberOfAttacks == 0 or not ships:
        if ships:
            head = ships[0]
            tail = ships[-1]
        else:
            head = tail = None
        return head, tail
```
The attack count as previously established will tell us where to attack by doing the modular operation and seeing if there is a residue\
```python
 if attack_count % 2 == 0:  # Atacking the head
        ships[0] -= 1
        if ships[0] <= 0:
            ships[0] = 0
            removeZeroes(ships)
    else:  # Atacking the tail
        ships[-1] -= 1
        if ships[-1] <= 0:
            ships[-1] = 0
            removeZeroes(ships)
```
Finally every time we call this recursive functio we'll use a new thread (in this case called executor) which my max is 10

## Time Complexity

## Analysis
