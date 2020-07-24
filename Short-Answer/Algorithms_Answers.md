#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

O(n) because the function checks if A is less then N cubed every time AFTER A has been added to by A plus n squared. N cubed divided by N squared leaves us with N. Excluding constants.

b)

O(n log n) because the first loop will go through each item no matter what n times. And the while looop will finish in a logarithmic time because j is doubled each time inside the while loop, which is checked to see if its less then the input size each time. 

c)

O(n)
bunny ears will take input "bunnies" and will check a base case (if input is 0, return 0), othrwise it will return (2 + (function bunnyears called again with input - 1)). for example if the input was 5, the fn would check if 5 is 0, its not. then it would return 2 plus fn(5 - 1) which is fn(4). the fn would evaluate first before its added to 2. fn(4) would then be executed. check to see if input is 0. its not. then it would return 2 + fn(4 - 1), or fn(3). Now you may be seeing the pattern here. the first exectuion of fn(original input) will continue to check if input is zero, and if its not, will return a sum which includes a call to fn with input lessened by 1. This means the recursive function call is converging 1 by 1 to the base case. Once input is indeed 0, the execution context where fn(0) will return a value of 0. Since all these function calls are housed in a stack data structure (FIFO)... the next fn(1) will return, then fn(2) and so on all the way to fn(n). The whole time this happens it will be adding the 2 in the sum statement each time via the call stack ordering. After that is complete the value all added up will be returned to you! It just took n times to do it! 

## Exercise II

In order to find "f" floor, I will need to drop an egg off each floor until an egg breaks, from floor 0 to floor "f". In orer to minimize the number of eggs dropped and broken, I will make sure to collect all eggs dropped for reuse. (assuming the dropping of eggs doesn't cause them to be weaker, thereby ruining the experiement and finding a false "f" floor). Once an egg dropps and breaks, that floor is "F". 

Worst case scenario is N == F. So runtime complexity would be O(n). Linear. It could take testing each floor to find F. This would minimize the number of broken eggs.

However, if I was allowed to use up more eggs by breaking them, I could perform a binary search by starting at floor (n // 2). Then if the egg doesn't break, I know the rest of floors below (n // 2) are not "F". And then grab the new middle from the upper half of floors, or vice versa for the bottom if the egg does break. I would perform that search in O(log n) time, but more eggs would be broken in the process.
