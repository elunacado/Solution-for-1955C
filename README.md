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

With that said and done lets start deconstructig the code
## Implementation

## Time Complexity

## Analysis
