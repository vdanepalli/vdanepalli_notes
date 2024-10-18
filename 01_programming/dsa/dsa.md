# Algo Experts

<details open>
  <summary> AlgoExperts DS Crash Course </summary>


- problem solving ability
- not much theoretical knowledge is required for coding interviews

<br/>
<br/>


- coding fundamentals
- foundational data structures

<br/>
<br/>

- coding is manipulating data
- strcuture, organize, manage data 
- data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to data

<br/>
<br/>

- complexity analysis 
- single problem can have multiple solutions. some are better than others. some are lot better than others.
- time complexity and space complexity

<br/>
<br/>

- Memory
- memory is finite
- 0 and 1 --- bits
- 8 bits = 1 byte
- endianness -- ordering of bytes 
- ASCII or Unicode encoding
- memory address
- pointers
- Random Access Memory : RAM

<br/>
<br/>


- Big O Notation


<br/>
<br/>

- Logarithm
- log x base b = y iff b ^ y = x
- In computer science, we assume base is 2; Binary Logarithm
- In math, if we don't specify base, we assume base is 10
- log(1) = 0
- 2 ^ ? = N ; in here, as N doubles, the ?, log(N) only increases by one 


<br/>
<br/>

- Arrays

<br/>
<br/>


- LinkedLists
- get -- O(i) T
- set -- O(i) T
- init -- O(n) ST
- copy -- O(n) ST
- Traverse -- O(n) T
- Insertion -- O(1) or O(i)
- Singly Linked List -- one link between two nodes; next pointer
- Doubly linked list -- two links between two nodes; next, prev pointers
- 

<br/>
<br/>


- Hash Tables
- Java Script Object or Python Dictionary
- Key Value store
- every key maps to a value; keys need not be integers. 
- insertion, deletion, searching for value given key -- O(1) on average (Amortized time); O(n) in worst case;
- HashTables are built on top of arrays and linkedlists. 
- Hash Function is used to transform the key into Index -- integer in a range. 
- x mod n gives values between 0 and n-1
- hash collisions -- hash function generates same hash value for different keys
- resizeable hash tables; -- similar to dynamic arrays
- O(n) space;

<br/>
<br/>

- Stacks and Queues
- inserting and deleting only from one end -- O(1) time
- Stacks -- LIFO
- Queue -- FIFO
- enqueue, dequeue -- can be O(1) using linked lists
- push, pop -- can be O(1) using arrays | linkedlists
- priority queue
- max stack
- min stack
- peek or top of stack 

<br/>
<br/>


- Strings
- ASCII -- one byte for character
- traverse -- O(n)
- copy -- O(n)
- get -- O(1)
- strings are mutable in c++ but not in most other languages (python, java, javascript...)

<br/>
<br/>


- Graphs
- collection of nodes that may or may not be connected to each other
- node is vertex
- connection is edges
- virtices and edges
- connected graph -- starting from any node, you can reacn any other node. some connection between any two nodes
- directional graphs -- directed graph; say flights 
- no directions between connected nodes -- undirected graph; say friendships ( hope so )
- cyclic graphs
- acyclic graphs
- cycle -- 3 or more nodes that go in infinite loop; say if you start at a node, and then reach the same node through any path, then there is a cycle. 
- can mark the visited nodes as visited to keep track of the visited nodes and not visit them again 
- adjacency list -- (say something like all the nodes are keys and for each key you have a list of nodes that you can reach from that particular key or node)
- storing a graph -- O(v + e)
- Traversing graph -- breadth-first | depth-first -- O(v + e)

<br/>
<br/>

- Trees 
- Are also a type of graph
- Cannot be disconnected; Cannot be cyclic; Must have some root node. Each node can have multiple children; Each child can have only one parent; Must be directed -- usually downwards
- k-ary trees -- every node can have atmost k childs
- Binary Search Trees -- special type of binary trees
- Min Heap -- special type of binary trees
- Max Heap -- special type of binary trees
- Tries -- typically stores characters in a string
- Storing tree -- O(n)
- Traverse -- O(n) or O(height of the tree)
- Balanced Binary Tree 
- Skewed or Imbalanced Trees
- Balanced Binary -- If it roughly maintains O(log(n)) TC for traversal when we are eliminating subtree at each step
- Red Black Trees or AVL Trees can restructure themselves to maintain above balance. Maintaining O(log(n)) TC is important
- Branch -- any path that strats at root and ends at leaf
- Bottom nodes -- leaf nodes
- levels
- complete -- every level is filled up except the final level which may or may not be filled up but is filled up from left to right if there any nodes
- full -- every node has exactly k children or no children
- perfect -- all leaf nodes have same depth

</details>

-----

# ZTM

<details open>
  <summary> DSA </summary>

## Introduction

- Getting the Interview
- Non Technical Interview Questions
- Offer + Negotiation
- Technical Interviews
- Practice Questions

<br/><br/>

- Discord
- Deliberate Practice
- Take Breaks
- Complete


## Getting More Interviews

- [interview-mind-map](https://coggle.it/diagram/W5u8QkZs6r4sZM3J/t/master-the-interview)
- [technical-interview-mind-map](https://coggle.it/diagram/W5E5tqYlrXvFJPsq/t/master-the-interview-click-here-for-course-link)

<br/><br/>

- Increase the odds of getting an interview -- percentage
- Interviewing is a numbers game

<br/><br/>

- Resume [resumemaker](https://www.resumemaker.online/) | [checklist](https://github.com/aneagoie/resume-checklist)
- decide if you are worth talking to for a potential interview 
- a way to get an interview
- spend no longer than a day
- see that your employers names are on the resume 
- keywords and job descriptions
- One page -- clean and simple
- relevant skills - that make you stand out; why, how, and what were the results
- personalized -- instead of using same resume everywhere
- online link 
- checklist
- use a pre-designed resume template
- one page resume
- include words from job description
- include company name you are applying to 
- does your first item on resume reflect what company is looking for
- experience titles should demonstrate value
- do you have an online link
- remove the word I 
  - Get to the point right away
- No buzzwords dscribing how great you are 
  - don't tell the recruiter what to think about you
- are you using action words
  - show results, quantifiable results
  - impact on business
- measuure everything in terms of impact, don't just describe your responsibilities
- technical knowledge/skills should include what they are looking for. Only show years if it is impressive
- Include only sections/items that are impressive: experience, projects, education, technical skills
- No typos or bad grammar
- be honest with your resume
- [jobscan](jobscan.com)
- [resume article](https://stackoverflow.blog/2020/11/25/how-to-write-an-effective-developer-resume-advice-from-a-hiring-manager/)
- [samples](https://www.cakeresume.com/Engineering-resume-samples)
- [thisresumedoesnotexist](https://thisresumedoesnotexist.com/)
- [rxresume](https://docs.rxresu.me/tutorial/create-a-new-resume)
- [open-resume](https://www.open-resume.com/)
- [ats-compliant-resumes](https://www.jobscan.co/blog/ats-resume/)
- [ats-compliant-templates](https://www.jobscan.co/resume-templates)

<br/><br/>

- experiecne 
- github
- website
- creative tim
-  mashup-template
-  kk.org kevin kelly
- 1-2 big projects
- blog -- medium, hackernoon, ...
- contribute to open-source projects
- partcipate in hackathons
- any skill that gets the job done -- people management skills, decision making.
- [git-history](https://github.com/gelstudios/gitfiti)
- [gitify-alternative](https://github.com/ZachSaucier/github-calendar-customizer)
- [git-readme-appealing](https://www.youtube.com/watch?v=ktN5tDfQ_g8)

<br/><br/>

- Linkedin
- complete your profile
- Skills and Endorsements
- Include keywords that recruiters might be looking for
- Get referrals
- Strategic and Efficient
- Keep changing your profile just so your profile is active in recently updated.
- [community](https://zerotomastery.io/community/?utm_source=academy&utm_medium=MCI)
- [ztm](https://www.youtube.com/watch?v=D48ER-3dlFI)

- Portfolio
- Email

## Solutions

- [Python solutions 1](https://github.com/theja-m/Data-Structures-and-Algorithms)
- [Python solutions 2](https://github.com/VicodinAbuser/ZTM-DS-and-Algo-Python)
- [C/C++ solutions](https://github.com/shree1999/Data-Structures-and-Algorithms)
- [GO Lang Solutions](https://github.com/punitpandey/DS-Algo)
- [Swift Solutions](https://github.com/preetamjadakar/datastructures-swift)
- [Java Solutions 1](https://github.com/nimrod46/Data-Structures-and-Algorithms)
- [Java Solutions 2](https://github.com/satya-verma/Data-Structures-and-Algorithms--using-JAVA)
- [C# Solutions](https://github.com/anirban-s/data-structures-and-algorithms)
- [TypeScript Solutions](https://github.com/CoffeelessProgrammer/Data-Structures-and-Algorithms-TS)
- [Kotlin Solutions](https://github.com/abdurakhmonoff/data-structures-and-algorithms-kotlin)
- [Perl Solutions](https://github.com/KrisMatrix/DS_Algo)
- [Scala Solutions](https://github.com/beneyal/ztm-dsa-scala)
- [Rust Solutions](https://github.com/sethderrick/Data-Structures-and-Algorithms)

<br/>

- [replit](https://repl.it)
- [glot.io](https://glot.io)

<br/>

- resources 
- [github link for replit code](https://github.com/aneagoie/ztm-master-the-coding-interview-ds-algo)

## Big O

- good code
  - readable
  - scalable
  - recipe/instructions --> meal/output
  - ![](assets/2024-08-19-21-26-59.png)
  - 

## How to solve coding problems



## DS: Introduction

- DS : Collection of values; think of containers -- food storage, water bottle, backpack, locker -- organize data; put in and take 
  - Arrangement of data
  - Operations you can do on it
- Algorithms : Processes manipulating DS
- DS + Algo = Programs
- good code
  - readable
  - memory
  - speed
- ds
  - how to build 
  - how to use
- Computer
  - CPU -- 
    - Memory Controller
    - Cache -- say LRU
  - RAM -- volatile
    - Address
      - 8 Bits -- Byte 
    - [Memory](https://www.youtube.com/watch?v=fpnE6UAfbtU)
      - [reading 1](http://statmath.wu.ac.at/courses/data-analysis/itdtHTML/node55.html)
      - Latch -- holds one bit of information. A circuit of logic gates used to store information and remember the last input value: latch onto it. 
      - ![](assets/2024-08-19-21-55-24.png)
        - if set and reset are both zero, the circuit outputs the last input value -- memory
      - gated latch
        - ![](assets/2024-08-19-21-56-43.png)
      - A group of latches, say 8 latches = register. 
      - Number of bits in a register = width
      - 256 bits -- 16 x 16 matrix of wires.  
        - ![](assets/2024-08-19-21-59-28.png)
        - we only need 35 wires -- 1 data wire, 1 write enable wire, 1 read enable wire, 16 rows, 16 cols
        - we store the address as two 4bit numbers
        - 11001000 -- 12 row 8 col
        - address --> Multiplexer --> 
           - ![](assets/2024-08-19-22-00-49.png)
           - one multiplexer to handle rows and other to handle columns
        - ![](assets/2024-08-19-22-03-05.png)
        - 32 bits = 4 bytes = 1 word
        - each octal digit is equivalent to 3 binary digits -- 0 to 7 -- octal -- prefixed by 0
        - hexadecimal -- each digit represents 0 to 16 -- >= 9 replaced by a to f; each hexadecimal is 4 bits -- prefixed by 0x or #
        - hexadecimals as pairs of digits -- each pair represents a byte of information
        - `0  :  6a 75 73 74 20 74 65 73 74 69 6e 67  |  just testing` -- block of memory
           - offset -- which byte is shown first | actual contents | interpretation of memory contents
        - k bits represent 0 to 2^k - 1 values
        - real numbers -- there is a limit to the precision that we can achieve. 
           - real numbers are stored as floating point number
           - mantissa m, exponentt e --> m.2^e = 
        - endianness -- byte ordering not bit ordering; comes into picture only when considering multi-byte values
           - big endian
              - most significant digit is on the left most; left to right; natural way of writing numbers. 
              - most significant digit -- digit with most weight
              - all fields in network headers -- big endian -- RFC 793 
           - little endian
         - text
           - char --> number --> binary : encoding
           - encoding
             - ASCII -- uses 7 bits
             - UNICODE -- first two bytes represent endianness -- Byte Order Mark BOM
             - UTF-8 -- first three bytes represent BOM
          - datetimes
           - current standard uses Gregorian Calender
           - Time Zones
           - January 1 1970
         - color
           - 4 bytes
           - transluency red green blue intensities
  - Storage -- persistent; slow; 
- `Math.pow(6, 1000)` -- infinity. Can't be stored in RAM
- DS
  - Arrays, LinkedLists
  - Stacks, Queues
  - Trees. Tries, Graphs
  - Hash Tables
- Algo
  - Sorting
  - Dynamic Programming
  - BFS DFS Searching 
  - Sorting
- Operations
  - Insertion
  - Deletion
  - Traversal
  - Searching
  - Sorting
  - Access


## DS: Arrays



## DS: Hash Tables



## DS: Linked Lists



## DS: Stacks + Queues



## DS: Trees



## DS:Graphs



## Algorithms : Recursion



## Algorithms : Sorting



## Algorithms : Searching + BFS + DFS



## Algorithms : Dynamic Programming 



## Non Technical Interviews



## Offer + Negotiation


## Extra Questions



## Bonus : Extra Bits

</details>

-----

# Programming Pathshala


<details open>
  <summary> DSA </summary>

## Module 1 : Begin with Programming



## Module 2 : Gearing Up 7w

### Arrays and Dynamic Arrays

- Fundamentals
  - collection of elements of same data type
  - fixed size | static arrays
  - contiguous memory
  - dynamic arrays
    - amortized time complexity
  - pass by reference (default) -- pointer or address is passed
    - `fun (vector<int> &v)` | `fun(arr, size) & fun(arr int[], size)`
  - pass by value -- new copy
- 


### Mathematics

### Time and Space Complexities


### Recursion


### Backtracking



## Module 3 : Fundamental Algorithms 4w



## Module 4 : Fundamental Data Structure 6w



## Module 5 : Advanced DSA 1  4w



## Module 6 : Advanced DSA 2  4w


## Module 7 : CS Fundamentals 4w


## Module 8 : Low Level Design 3w


## Module 9 : High Level Design 4w


</details>

-----


# NEETCODE 

<details open>
  <summary> DSA Begineers </summary>

## Arrays

- RAM : Random Access Memory
- Arrays : Stored at continuous locations 
- Holds similar data types, so that you can access ith element just by using simple math
- index based -- 0 to 1
- ith element address = arr_address + (i * element_size) -- all elelments have same size : homogenous 
- Dynamic Arrays 
  - ![](assets/2024-10-16-14-55-08.png)
- 

| Operation | Time Complexity |
| ----------| --------------- |
| r/w ith element | O(1) | 
| insert/remove at end | O(1) |
| insert/remove middle | O(n) |




## Linked Lists


## Recursion 


## Sorting 


## Binary Search 


## Trees


## Backtracking


## Heap Priority Queue


## Hashing 


## Graphs 


## Dynamic Programming 


## Bit Manipulation 

</details>



<details open>
  <summary> DSA Advanced </summary>

## Arrays

### Kadane's Algorithm

- Q: Find a non-empty sub array with the largest sum
- 

## Linked Lists


## Tries


## Heaps


## Backtracking 


## Graphs 


## Dynamic Programming



</details>




-----

# InterviewCake


<details open>
  <summary> DSA </summary>

## 0. Algorithmic Thinking

### 0.1 Big O Notation 

- runtime in terms of <u>how quickly it grows</u> <u>relative to the input</u>, <u>as input gets large</u>
- O(1), O(n), O(n^2), ... ; throw out constants or less significant terms
- Space complexity -- additional space apart from inputs
- <u>**Tradeoff**</u> -- time and space
- <u>**Sometimes constants matter**</u> -- even if it doesn't effect Big O; say you cut down a script run time by 5 times
- <u>**Beware of premature optimisation**</u> -- might negatively impact readability or coding time


### 0.2 Data Structures for Coding Interviews

#### RAM 

- Random Access Memory -- Working memory -- Volatile
- Storage -- Disk -- Persistent
- Processor --> Memory Controller (unlike Disks has direct access to) --> RAM (addresses -- 8 bits )
- Reading from sequential addresses is faster than jumping around because of caching

#### Binary Numbers

- Base 10 -- Decimal -- powers of 10 
- Base  2 -- Binary  -- powers of  2
- Base 16 -- Hexadecimal -- prefixed with `0x or #`
- Unsigned Integer
- Fractions -- store numerator and denominator
- Decimals -- number with decimal point taken out, position where the decimal point goes from leftmost digit
- Negative numbers -- reserve leftmost digit -- 0 positive, 1 negative

#### Fixed Width Integers

- 2^8 = 256 numbers
- Integer overflow -- say you add `255 + 1` becomes `256 = 1 0000 0000`
- tinyint, smallint, int, bigint -- SQL | Integers, Longs -- Java
- Most integrs are fixed width == fixed length unless told otherwise

#### Arrays

- index -- indices
- `arr[n] = arr + n * size of element in array` -- fast lookup
  - each element in array must be of same size
  - array elements must be contiguous

#### Strings

- Strings -- series of characters
- Character encoding -- mapping of numbers to characters
- ASCII 

#### Pointers

- Imagine pointers (addresses) to baby names being stored in babies array as integers 
- not cache-friendly
- lookups in pointer based arrays are still O(1)

#### Dynamic Arrays 

- word processor -- we don't know how many strings. 
- normal array programmed to resize itself
- python ruby js use these by default, but others like Java have Array and <u>**ArrayList**</u>
- array size and array capacity
- resize
  - make a new big array, twice in size
  - copy old array elements into new array
  - free up old array
  - append your new element -- we can call doubling appends -- special appends -- O(n)
    - each doubling append O(n) gives you double the regular appends O(1)
    - <u>**Amortized cost O(1)**</u> -- paying off the cost of something gradually
    - expensive append buys many cheap appends
    - O(m) actual appends + 2 O(m) for any doubling required
- some appends are expensive; worst case O(n) appends; O(n) prepends always


#### Linked Lists

- Node -- two-item arrays per say
- Linked List -- series of nodes
- Head, tail
- worst case O(1) appends and prepends
- O(i) lookup times; not cache-friendly


#### Hashtables

- Say, we now want to count the frequency of words
- Hash maps or hash tables. 
- counts are the values and words are the keys (analogous to indices)
- key index to array index mapping = hashing function
- <u>**Hash collision**</u> -- two keys map to same hash value
- Say, the value of each key is a pointer to a linked list where each node contains the word itself and the count.  
- Lookups are O(1) on average and only in one direction
- Looking up key given value still takes O(n) time


### 0.3 Logarithms

- what power must we raise this base to, inorder to get this answer
- helps when solving for x when x is exponent
- ![](assets/2024-08-27-22-35-47.png)
- ```py
  def binary_search(nums, key):
    floor_index = -1
    ceil_index = len(nums)

    while floor_index + 1 < ceil_index:
      distance = ceil_index - floor_index
      half_distance = distance // 2
      guess_index = floor_index + half_distance

      if key < nums[guess_index]:
        ceil_index = guess_index
      elif key > nums[guess_index]:
        floor_index = guess_index
      else 
        return True
    return False
  ```

<br/>

- Logarithms in sorting
- Sorting : Best worst case O(n log n)
- If we can tightly bound the range of possible numbers in our list, we can use hash map to do it in O(n) using counting sort
- ```python
  def merge_sort(list_to_sort):
  # Base case: lists with fewer than 2 elements are sorted
  if len(list_to_sort) < 2:
      return list_to_sort

  # Step 1: divide the list in half
  # We use integer division, so we'll never get a "half index"
  mid_index = len(list_to_sort) // 2
  left  = list_to_sort[:mid_index]
  right = list_to_sort[mid_index:]

  # Step 2: sort each half
  sorted_left  = merge_sort(left)
  sorted_right = merge_sort(right)

  # Step 3: merge the sorted halves
  sorted_list = []
  current_index_left = 0
  current_index_right = 0

  # sortedLeft's first element comes next
  # if it's less than sortedRight's first
  # element or if sortedRight is exhausted
  while len(sorted_list) < len(left) + len(right):
      if ((current_index_left < len(left)) and
              (current_index_right == len(right) or
               sorted_left[current_index_left] < sorted_right[current_index_right])):
          sorted_list.append(sorted_left[current_index_left])
          current_index_left += 1
      else:
          sorted_list.append(sorted_right[current_index_right])
          current_index_right += 1
  return sorted_list
  ```

<br/>

- Logarithms in binary tree
- Perfect tree -- each level or tier is full
- Height h = log base 2 of (n+1 / 2) + 1 = log base 2 of (n + 1)
- log base 2 of n == lg n

## 1. Arrays and String manipulation

### 1.1 Array

- <span style="color: #cdf1ae;">O(1) Lookups and Appends</span>
- <span style="color: #ff0000;">O(n) Space, Insert, Delete; fixed size</span>
- Array slicing -- allocates a new array with selected elements; O(n) time O(n) space

<br/>

- Call Stack -- made of stack frames -- one for each function
  - Local variables
  - Arguments passed
  - Information about caller stack frame
  - return address
- <u>**Be careful with recursive function.**</u> Call Stacks result in space complexities. 
- Stack Overflow -- recursion error
- Tail Call Optimization TCO -- very last thing a function does is call another function. This would mean we do not need to store callers stack frame, saving up space
- Python and Java don't implement TCO
- Inplace -- destructive -- modifies input -- have side effects
- Out-of-place -- safer -- no side effects

### 1.2 Dynamic Array

- <span style="color: #cdf1ae;">O(1) Lookups O(1) Appends Average Case | O(1) Appends Worst Case</span>
- <span style="color: #cdf1ae;">fast lookups, variable size, cache-friendly</span>
- <span style="color: #ff0000;">O(n) Insert, Delete, Worst Case Appends</span>

## 2. Hashing and Hashtable

### 2.1 Hashing and Hash Functions

- think of hash as a fingerprint
- we can trust a given file has a unique hash but we can't go back to file from hash
- uses
  - dictionaries 
    - list like data structure with constant time lookups 
    - one way is to define a list, use hash function to hash keys into list indices
  - preventing man in the middle attacks
    - say a software provider provides a hash: indicating their hash value
    - now if nobody tampered with it, the hash remains same.

### 2.2 Hash Table

- map, dictioanry, hash 
- <span style="color: #ff0000;">O(n) space insert lookup delete : Worst case</span>
- <span style="color: #ff0000;">slow worst case lookups</span>, <span style="color: #ff0000;">unordered keys</span>, <span style="color: #ff0000;">single directional lookups</span> (given key get value but not other way around), <span style="color: #ff0000;">not cache-friendly</span> (many hashtable implementations use linked lists)
- worst case lookup O(n) comes from the fact that, <u><span style="color: #ff0000;">when all keys map to same hash value</span></u>, we end up having a big linked list to traverse. Hence O(n)
- Also, <u><span style="color: #ff0000;">when using dynamic array resizing</span></u>, it's O(n); say, things begin to get crowded and we want to double the initial array, rehash everything to find new positions -- all of this is to avoid hash collisons

<br/>

- <span style="color: #cdf1ae;">O(1) insert lookup O(n) space delete : Average case</span>
- <span style="color: #cdf1ae;">fast lookups and flexible keys </span>

<br/>

- x mod n results in a value between 0 and n - 1 inclusive

### 2.3 Sets

- A set is like a hash map but only stores keys without values

## 3. Greedy Algorithms

- A greedy algorithm builds up by greedily choosing the option that looks the best at every step; say you wanna give change for 39 cents using least number of coins. 25 + 10 + 4 ?
- <u><span style="color: #ff0000;">sometimes a greedy algorithm doesn't give you an optimal solution</span></u>
  - <span style="color: #ff0000;">To find the cheapest route visiting a set of cities, choosing to visit the cheapest city you haven't been to yet doesn't produce the cheapest overall itinerary.</span>
  - <span style="color: #ff0000;">When filling a duffel bag with cakes of different weights and values, choosing the cake with the highest value per pound doesn't always produce the best haul.</span>

## 4. Sorting Searching Lograithms

- Binary Search -- O(log n) -- as we cut the posibilities by half at each step

## 5. Trees Graphs

### 5.1 Binary Tree 

- binary tree : every node has two or fewer children
- perfect binary tree : every level of the tree is completely filled
  - number of nodes doubles as we go down the levels
  - number of nodes in the last level = sum of all nodes in other levels + 1
- assuming levels start from 0, nodes at nth level = 2 ^ n or 2 ^ (h-1) where level 0 is considered h = 1
- total nodes = n = 2^h - 1
- h = log base 2 of (n + 1)


### 5.2 Graph

- graph -- interconnected network
- node or vertex -- connected by edges
- representing links; scaling challenges -- most graph algorithms are O(n log n) or slower

<br/>

- directed vs undirected graph
- cyclic vs acyclic graph
- weighted or unweighted graph
- legal coloring -- no two adjancent nodes have the same color

<br/>

- representations
- edge list -- `graph = [[0, 1], [1, 2], [1, 3], [2, 3]]`
- adjacency list -- list index represents node and value is a list of the node's neighbors
  - ```python
    graph = [
      [1],
      [0, 2, 3],
      [1, 3],
      [1, 2],
    ]
    ```
- adjacency matrix
  - ```python
    graph = [
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
    ]
    ```
- Is there a path between two nodes in this undirected graph? Run DFS or BFS from one node and see if you reach the other one.
- What's the shortest path between two nodes in this undirected, unweighted graph? Run BFS from one node and backtrack once you reach the second. Note: **BFS always finds the shortest path, assuming the graph is undirected and unweighted. DFS does not always find the shortest path.**
- Can this undirected graph be colored with two colors? Run BFS, assigning colors as nodes are visited. Abort if we ever try to assign a node a color different from the one it was assigned earlier.
- Does this undirected graph have a cycle? Run BFS, keeping track of the number of times we're visiting each node. If we ever visit a node twice, then we have a cycle.

<br/>

- algorithms 
- **Dijkstra's Algorithm**: Finds the shortest path from one node to all other nodes in a weighted graph.
- **Topological Sort**: Arranges the nodes in a directed, acyclic graph in a special order based on incoming edges.
- **Minimum Spanning Tree**: Finds the cheapest set of edges needed to reach all nodes in a weighted graph.

### 5.3 Breadth First Search BFS

- traverse one step or level at a time
- <span style="color: #cdf1ae;">will find the shortest path </span>
- <span style="color: #ff0000;">bfs on a binary tree requires more memory than a dfs</span>

### 5.4 Depth First Search DFS 

- one path at a time
- <span style="color: #cdf1ae;">easy to implement using recursion. Takes less memory on a binary tree</span>
- <span style="color: #ff0000;">will not necessarily find a shortest path</span>   

## 6. Dynamic Programming and Recursion

- Memoization is a common strategy for dynamic programming problems, which are problems where the solution is composed of solutions to the same problem with smaller inputs (as with the Fibonacci problem, above). 
- The other common strategy for dynamic programming problems is going bottom-up, which is usually cleaner and often more efficient.

### 6.1 Overlapping Subproblems

- A problem has overlapping subproblems if finding its solution involves solving the same subproblem multiple times.
- Ex : Fibonacci 

### 6.2 Memoization 

- Memoization ensures that a function doesn't run for the same inputs more than once by keeping a record of the results for the given inputs (usually in a dictionary).
- To avoid the duplicate work caused by the branching, we can wrap the function in a class with an attribute, memo, that maps inputs to outputs. 
- ```python
  class Fibber(object):

  def __init__(self):
      self.memo = {}

  def fib(self, n):
      if n < 0:
          raise IndexError(
              'Index was negative. '
              'No such thing as a negative index in a series.'
          )

      # Base cases
      if n in [0, 1]:
          return n

      # See if we've already calculated this
      if n in self.memo:
          print("grabbing memo[%i]" % n)
          return self.memo[n]

      print("computing fib(%i)" % n)
      result = self.fib(n - 1) + self.fib(n - 2)

      # Memoize
      self.memo[n] = result

      return result
  ```

### 6.3 Bottom up algorithms

- Going bottom-up is a way to avoid recursion, saving the memory cost that recursion incurs when it builds up the call stack.
- Put simply, a bottom-up algorithm "starts from the beginning," while a recursive algorithm often "starts from the end and works backwards."

## 7. Queues and Stacks

### 7.1 Queues

- 
### 7.2 Stacks

## 8. Linked Lists


## 9. System Dessign 


## 10. General Programming 


## 11. Bit Manipulation


## 12. Combinatorics Probability and Math


## 13. Javascript


## 14. Coding Interview Tips


## 15. Interview Tips


## 16. Questions by Company


## 17. Questions by Topics

- Arrays 
  - index based
  - ordered
  - array slicing
  - in-place destructive; out-of-place safe 
  - dynamic array
    - array size is not constant anymore
  - adv 
    - fast lookups / appends
    - variable size 
    - cache friendly -- place items together in memory
  - dis adv
    - slow worst-case appends
    - costly inserts and deletes -- scooting over of elements is required
  - dynamic array size vs dynamic array capacity
  - amortized cost
    - Amortize is a fancy verb used in finance that refers to paying off the cost of something gradually. 
    - With dynamic arrays, every expensive append where we have to grow the array "buys" us many cheap appends in the future. 
    - Conceptually, we can spread the cost of the expensive append over all those cheap appends.
    - O(m) + O(2m) for doubling along the way of adding m elements
  - Python lists
    - Ordered, 0-indexed, list.append()

  - Python tuples 
    - ordered, indexed
    - immutable

  - Q1 : 
    - ```python
      def merge_ranges(meetings):

      # Merge meeting ranges
      
      sorted_meetings = sorted(meetings)
      merged_meetings = [sorted_meetings[0]]
      
      for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
          last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
          
          if (current_meeting_start <= last_merged_meeting_end):
              merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, 
              current_meeting_end))
          else:
              merged_meetings.append((current_meeting_start, current_meeting_end))
      
      return merged_meetings
      ```
  - Q2:
    - ```python
      
      ```


<br/>




</details>

-----




