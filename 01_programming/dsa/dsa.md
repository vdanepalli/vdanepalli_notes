# Algo Experts DS Crash Course

- problem solving ability
- not much theoretical knowledge is required for coding interviews

<br/>
<hr/>
<br/>


- coding fundamentals
- foundational data structures

<br/>
<hr/>
<br/>

- coding is manipulating data
  - strcuture, organize, manage data 
- data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to data

<br/>
<hr/>
<br/>

- complexity analysis 
- single problem can have multiple solutions. some are better than others. some are lot better than others.
- time complexity and space complexity

<br/>
<hr/>
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
<hr/>
<br/>


- Big O Notation


<br/>
<hr/>
<br/>

- Logarithm
- log x base b = y iff b ^ y = x
- In computer science, we assume base is 2; Binary Logarithm
- In math, if we don't specify base, we assume base is 10
- log(1) = 0
- 2 ^ ? = N ; in here, as N doubles, the ?, log(N) only increases by one 


<br/>
<hr/>
<br/>

- Arrays

<br/>
<hr/>
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
<hr/>
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
<hr/>
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
<hr/>
<br/>


- Strings
- ASCII -- one byte for character
- traverse -- O(n)
- copy -- O(n)
- get -- O(1)
- strings are mutable in c++ but not in most other languages (python, java, javascript...)

<br/>
<hr/>
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
<hr/>
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


# ZTM Data Structures and Algorithms

<details open>
    <summary> Master the Coding Interview : DSA </summary>

## Contents
1. Getting the Interview
2. Offer + Negotiation
3. Non-Technical Interviews
4. Data Structures
5. Algorithms


## Getting the interview 

- Increase the odds; interviewing is a numbers game
- 1% to 5%

1. Resume 
   - decide if you are worth talking to for a potential interview
   - a way to get interviews 
   - spend no longer than a day
   - Make it personal to each job you apply, having employers name and everything
   - Include words and characteristics describing the job postings
   - [resumemaker](https://resumemaker.online)
   - ATS 
   - One Page
   - Relevant Skills
   - Personalized
   - Online Link -- github blogpost portfolio
   - Cheatsheet
     - use a predesigned resume template
     - one page resume
     - include words from job description 
     - include company name you are applying to
     - does first item on your resume reflect what they are looking for 
     - experience titles demostrate value; first item should demostrate value
     - do you have an online link
     - remove the word I 
     - No buzzwords describing how great you are; don't put garbage that doesn't mean anything
     - are you using action words; what did you do and what were the results
     - measure everything in terms of impact, don't just describe your responsibilities
     - technical knowledge / skills should include what they are looking for. Only show years if it is impressive
     - Include only sections / items that are impressive : experience, projects, education, technical skills
     - no typos or bad grammar
- Be honest with your resume. 
- resources
  - [jobscan](https://jobscan.co)
  - [article](https://stackoverflow.blog/2020/11/25/how-to-write-an-effective-developer-resume-advice-from-a-hiring-manager/)
  - [samples](https://www.cakeresume.com/Engineering-resume-samples)
  - [thisresumedoesnotexist](https://thisresumedoesnotexist.com/)
  - [rxresume](https://docs.rxresu.me/tutorial/create-a-new-resume)
  - [open-resume](https://www.open-resume.com/)
  - [ats resumes](https://www.jobscan.co/blog/ats-resume/)
  - [ats templates](https://www.jobscan.co/resume-templates)
- if it is tough, that is what you need
- dream big
- every application should be a long shot
- what if you have less to put on a resume 
  - github 
  - contribute and participate in open source projects
  - website -- your own 
    - mashup template
    - creative-tim template
    - [kevin kelly](https://kk.org)
    - 1 to 2 big projects
    - Blog 
      - say write on medium and publish it to hackernoon
- past experience, made any good decisions, worked on a challenging problem and solved them?

- [create artiicial git history using gitfiti](https://github.com/gelstudios/gitfiti)
- [easy gitfiti](https://github.com/ZachSaucier/github-calendar-customizer)
- [professional and visually appealing README](https://www.youtube.com/watch?v=ktN5tDfQ_g8)
  
1. Linkedin
   - Keep updating your linkedin profile time to time even if it means to fix a typo, just to make your profile visible to recruiters as updated recently. 
   - Include keywords that recruiters might use to search for candidates ; say including my favorite tools and technologies in one of your experiences
   - Be strategic and efficient
   - 
2. Portfolio
3. Email

Experience? When am I ready? Where are the jobs?

</details>


# ZTM DSA

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
  - 


- Portfolio
- Email

## Big O



## How to solve coding problems



## DS: Introduction



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


# 