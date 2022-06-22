# LeetCode Learning Journal

## Reference
- [Coding Interview University](https://github.com/jwasham/coding-interview-university)
- [Huahua’s Tech Road](https://zxi.mytechroad.com/blog) 

##  Algorithmic complexity / Big-O / Asymptotic analysis
- [x] [Harvard CS50 - Asymptotic Notation (video)](https://www.youtube.com/watch?v=iOq5kSKqeR4)
- [x] [Big O Notations (general quick tutorial) (video)](https://www.youtube.com/watch?v=V6mKVRU1evU)
- [x] [UC Berkeley Big O (video)](https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98)
- [ ] [Amortized Analysis (video)](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [x] TopCoder (includes recurrence relations and master theorem):
    - [Computational Complexity: Section 1](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-1/)
    - [Computational Complexity: Section 2](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-2/)
- [x] [Cheat sheet](http://bigocheatsheet.com/)


## Data Structures
- ### Arrays
    - [x] About Arrays:
        - [Arrays (video)](https://www.coursera.org/lecture/data-structures/arrays-OsBSF)
        - [UC Berkeley CS61B - Linear and Multi-Dim Arrays (video)](https://archive.org/details/ucberkeley_webcast_Wp8oiO_CZZE) (Start watching from 15m 32s)
        - [Dynamic Arrays (video)](https://www.coursera.org/lecture/data-structures/dynamic-arrays-EwbnV)
        - [Jagged Arrays (video)](https://www.youtube.com/watch?v=1jtrQqYpt7g)


- ### LinkedList
    - [ ] Description:
        - [x] [Singly Linked Lists (video)](https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK)
        - [ ] [CS 61B - Linked Lists 1 (video)](https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0)
        - [ ] [CS 61B - Linked Lists 2 (video)](https://archive.org/details/ucberkeley_webcast_-c4I3gFYe3w)
    - [ ] [C Code (video)](https://www.youtube.com/watch?v=QN6FPiD0Gzo)
            - not the whole video, just portions about Node struct and memory allocation
    - [ ] Linked List vs Arrays:
        - [Core Linked Lists Vs Arrays (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-linked-lists-vs-arrays-rjBs9)
        - [In The Real World Linked Lists Vs Arrays (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/in-the-real-world-lists-vs-arrays-QUaUd)
    - [ ] [why you should avoid linked lists (video)](https://www.youtube.com/watch?v=YQs6IC-vgmo)
    - [ ] Gotcha: you need pointer to pointer knowledge:
        (for when you pass a pointer to a function that may change the address where that pointer points)
        This page is just to get a grasp on ptr to ptr. I don't recommend this list traversal style. Readability and maintainability suffer due to cleverness.
        - [Pointers to Pointers](https://www.eskimo.com/~scs/cclass/int/sx8.html)
    - [x] LeetCode: 
        - [x] Q2
        - [x] Q24
        - [x] Q206
        - [x] Q141
        - [x] Q23

- ### Stack
    - [x] [Stacks (video)](https://www.coursera.org/lecture/data-structures/stacks-UdKzQ)
    - [x] Will not implement. Implementing with array is trivial
    - [x] LeetCode: 
        - [x] Q1003
        - [x] Q496
        - [x] Q1019
        - [x] Q1063
        - [x] Q907
        - [ ] Q2104

- ### Queue
    - [x] [Queue (video)](https://www.coursera.org/lecture/data-structures/queues-EShpq)
    - [x] [Circular buffer/FIFO](https://en.wikipedia.org/wiki/Circular_buffer)
    - [ ] Implement using linked-list, with tail pointer:
        - enqueue(value) - adds value at position at tail
        - dequeue() - returns value and removes least recently added element (front)
        - empty()
      - [ ] LeetCode: 
        - [x] Q1424
        - [x] Q1438
        - [ ] Q239
        - [ ] Q1499
        - [ ] Q862
        - [ ] Q1425


- ### Hash table
    - [ ] Videos:
        - [x] [Hashing with Chaining (video)](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8)
        - [x] [Table Doubling, Karp-Rabin (video)](https://www.youtube.com/watch?v=BRO7mVIFt08&index=9&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
        - [ ] [Open Addressing, Cryptographic Hashing (video)](https://www.youtube.com/watch?v=rvdJDijO2Ro&index=10&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
        - [ ] [PyCon 2010: The Mighty Dictionary (video)](https://www.youtube.com/watch?v=C4Kc8xzcA68)
        - [ ] [PyCon 2017: The Dictionary Even Mightier (video)](https://www.youtube.com/watch?v=66P5FMkWoVU)
        - [ ] [(Advanced) Randomization: Universal & Perfect Hashing (video)](https://www.youtube.com/watch?v=z0lJ2k0sl1g&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=11)
        - [ ] [(Advanced) Perfect hashing (video)](https://www.youtube.com/watch?v=N0COwN14gt0&list=PL2B4EEwhKD-NbwZ4ezj7gyc_3yNrojKM9&index=4)

    - [ ] Online Courses:
        - [x] [Core Hash Tables (video)](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-hash-tables-m7UuP)
        - [ ] [Data Structures (video)](https://www.coursera.org/learn/data-structures/home/week/4)
        - [ ] [Phone Book Problem (video)](https://www.coursera.org/lecture/data-structures/phone-book-problem-NYZZP)
        - [ ] distributed hash tables:
            - [Instant Uploads And Storage Optimization In Dropbox (video)](https://www.coursera.org/lecture/data-structures/instant-uploads-and-storage-optimization-in-dropbox-DvaIb)
            - [Distributed Hash Tables (video)](https://www.coursera.org/lecture/data-structures/distributed-hash-tables-tvH8H)

    - [ ] Implement with array using linear probing
        - hash(k, m) - m is size of hash table
        - add(key, value) - if key already exists, update value
        - exists(key)
        - get(key)
        - remove(key)

    - [x] LeetCode: 
        - [x] Q482
        - [x] Q904
        - [x] Q929
        - [x] Q3
        - [x] Q11
        - [ ] Q15
        - [ ] Q31
        - [ ] Q43
        - [ ] Q48


## More Knowledge

- ### Binary search
    - [x] [Binary Search (video)](https://www.youtube.com/watch?v=D5SrAga1pno)
    - [ ] [Binary Search (video)](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
    - [ ] [detail](https://www.topcoder.com/community/competitive-programming/tutorials/binary-search/)
    - [x] [blueprint](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)
    - [ ] Implement:
        - binary search (on sorted array of integers)
        - binary search using recursion
    - [ ] LeetCode
        - "As for the question "When can we use binary search?", my answer is that, If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search."
        - [x] Q278
        - [x] Q69
        - [x] Q35
        - [x] Q1011
        - [x] Q875
        - [x] Q1482
        - [ ] Q1201
        - [ ] Q1283
 
- ### Bitwise operations
    - [ ] [Bits cheat sheet](https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/bits-cheat-sheet.pdf) - you should know many of the powers of 2 from (2^1 to 2^16 and 2^32)
    - [ ] Get a really good understanding of manipulating bits with: &, |, ^, ~, >>, <<
        - [ ] [words](https://en.wikipedia.org/wiki/Word_(computer_architecture))
        - [ ] Good intro:
            [Bit Manipulation (video)](https://www.youtube.com/watch?v=7jkIUgLC29I)
        - [ ] [C Programming Tutorial 2-10: Bitwise Operators (video)](https://www.youtube.com/watch?v=d0AwjSpNXR0)
        - [ ] [Bit Manipulation](https://en.wikipedia.org/wiki/Bit_manipulation)
        - [ ] [Bitwise Operation](https://en.wikipedia.org/wiki/Bitwise_operation)
        - [ ] [Bithacks](https://graphics.stanford.edu/~seander/bithacks.html)
        - [ ] [The Bit Twiddler](https://bits.stephan-brumme.com/)
        - [ ] [The Bit Twiddler Interactive](https://bits.stephan-brumme.com/interactive.html)
        - [ ] [Bit Hacks (video)](https://www.youtube.com/watch?v=ZusiKXcz_ac)
		- [ ] [Practice Operations](https://pconrad.github.io/old_pconrad_cs16/topics/bitOps/)
    - [ ] 2s and 1s complement
        - [Binary: Plusses & Minuses (Why We Use Two's Complement) (video)](https://www.youtube.com/watch?v=lKTsv6iVxV4)
        - [1s Complement](https://en.wikipedia.org/wiki/Ones%27_complement)
        - [2s Complement](https://en.wikipedia.org/wiki/Two%27s_complement)
    - [ ] Count set bits
        - [4 ways to count bits in a byte (video)](https://youtu.be/Hzuzo9NJrlc)
        - [Count Bits](https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan)
        - [How To Count The Number Of Set Bits In a 32 Bit Integer](http://stackoverflow.com/questions/109023/how-to-count-the-number-of-set-bits-in-a-32-bit-integer)
    - [ ] Swap values:
        - [Swap](https://bits.stephan-brumme.com/swap.html)
    - [ ] Absolute value:
        - [Absolute Integer](https://bits.stephan-brumme.com/absInteger.html)

## Trees

- ### Trees - Notes & Background
    - [x] [Series: Trees (video)](https://www.coursera.org/lecture/data-structures/trees-95qda)
    - basic tree construction
    - traversal
    - manipulation algorithms
    - [x] [BFS(breadth-first search) and DFS(depth-first search) (video)](https://www.youtube.com/watch?v=uWL6FJhq5fM)
        - BFS notes:
           - level order (BFS, using queue)
           - time complexity: O(n)
           - space complexity: best: O(1), worst: O(n/2)=O(n)
        - DFS notes:
            - time complexity: O(n)
            - space complexity:
                best: O(log n) - avg. height of tree
                worst: O(n)
            - inorder (DFS: left, self, right)
            - postorder (DFS: left, right, self)
            - preorder (DFS: self, left, right)
    - LeetCode
        - [x] Q94
        - [x] Q100
        - [x] Q101
        - [x] Q102
        - [x] Q144
        - [x] Q145
        - [x] Q226
        - [x] Q572
        - [x] Q589
        - [x] Q617
        - [x] Q669
        

- ### Binary search trees: BSTs
    - [x] [Binary Search Tree Review (video)](https://www.youtube.com/watch?v=x6At0nzX92o&index=1&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)    
    - [x] [Introduction (video)](https://www.coursera.org/learn/data-structures/lecture/E7cXP/introduction)
    - [x] [MIT (video)](https://www.youtube.com/watch?v=76dhtgZt38A&ab_channel=MITOpenCourseWare)
    - C/C++:
        - [ ] [Binary search tree - Implementation in C/C++ (video)](https://www.youtube.com/watch?v=COZK7NATh4k&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=28)
        - [ ] [BST implementation - memory allocation in stack and heap (video)](https://www.youtube.com/watch?v=hWokyBoo0aI&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=29)
        - [ ] [Find min and max element in a binary search tree (video)](https://www.youtube.com/watch?v=Ut90klNN264&index=30&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [ ] [Find height of a binary tree (video)](https://www.youtube.com/watch?v=_pnqMz5nrRs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=31)
        - [ ] [Binary tree traversal - breadth-first and depth-first strategies (video)](https://www.youtube.com/watch?v=9RHO6jU--GU&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=32)
        - [ ] [Binary tree: Level Order Traversal (video)](https://www.youtube.com/watch?v=86g8jAQug04&index=33&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [ ] [Binary tree traversal: Preorder, Inorder, Postorder (video)](https://www.youtube.com/watch?v=gm8DUJJhmY4&index=34&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [ ] [Check if a binary tree is binary search tree or not (video)](https://www.youtube.com/watch?v=yEwSGhSsT0U&index=35&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
        - [ ] [Delete a node from Binary Search Tree (video)](https://www.youtube.com/watch?v=gcULXE7ViZw&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=36)
        - [ ] [Inorder Successor in a binary search tree (video)](https://www.youtube.com/watch?v=5cPbNCrdotA&index=37&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [ ] Implement:
        - [ ] insert    // insert value into tree
        - [ ] get_node_count // get count of values stored
        - [ ] print_values // prints the values in the tree, from min to max
        - [ ] delete_tree
        - [ ] is_in_tree // returns true if given value exists in the tree
        - [ ] get_height // returns the height in nodes (single node's height is 1)
        - [ ] get_min   // returns the minimum value stored in the tree
        - [ ] get_max   // returns the maximum value stored in the tree
        - [ ] is_binary_search_tree
        - [ ] delete_value
        - [ ] get_successor // returns next-highest value in tree after given value, -1 if none
    - LeetCode
        - [x] Q98
        - [x] Q700
        - [x] Q230
        - [x] Q99
        - [x] Q108

- ### Heap / Priority Queue / Binary Heap
    - visualized as a tree, but is usually linear in storage (array, linked list)
    - [x] [Heap](https://en.wikipedia.org/wiki/Heap_(data_structure))
    - [x] [Introduction (video)](https://www.coursera.org/lecture/data-structures/introduction-2OpTs)
    - [x] [Naive Implementations (video)](https://www.coursera.org/learn/data-structures/lecture/z3l9N/naive-implementations)
    - [x] [Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/GRV2q/binary-trees)
    - [x] [Tree Height Remark (video)](https://www.coursera.org/learn/data-structures/supplement/S5xxz/tree-height-remark)
    - [x] [Basic Operations (video)](https://www.coursera.org/learn/data-structures/lecture/0g1dl/basic-operations)
    - [x] [Complete Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/gl5Ni/complete-binary-trees)
    - [x] [Pseudocode (video)](https://www.coursera.org/learn/data-structures/lecture/HxQo9/pseudocode)
    - [x] [Heap Sort - jumps to start (video)](https://youtu.be/odNJmw5TOEE?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3291)
    - [x] [Heap Sort (video)](https://www.coursera.org/lecture/data-structures/heap-sort-hSzMO)
    - [ ] [Building a heap (video)](https://www.coursera.org/lecture/data-structures/building-a-heap-dwrOS)
    - [x] [MIT: Heaps and Heap Sort (video)](https://www.youtube.com/watch?v=B7hVxCmfPtM&index=4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [ ] [CS 61B Lecture 24: Priority Queues (video)](https://archive.org/details/ucberkeley_webcast_yIUFT6AKBGE)
    - [ ] [Linear Time BuildHeap (max-heap)](https://www.youtube.com/watch?v=MiyLo8adrWw)
    - [ ] Implement a max-heap:
        - [ ] insert
        - [ ] sift_up - needed for insert
        - [ ] get_max - returns the max item, without removing it
        - [ ] get_size() - return number of elements stored
        - [ ] is_empty() - returns true if heap contains no elements
        - [ ] extract_max - returns the max item, removing it
        - [ ] sift_down - needed for extract_max
        - [ ] remove(x) - removes item at index x
        - [ ] heapify - create a heap from an array of elements, needed for heap_sort
        - [ ] heap_sort() - take an unsorted array and turn it into a sorted array in-place using a max heap or min heap

    - LeetCode  
        ```
        heapq  
        ------  
        - heapq.heapify(x:list) -> min-heap  
        - heapq.heappush(heap, item)  
        - heapq.heappop(heap)  
        ```
        - [x] Q1046
        - [x] Q1057
        - [x] Q1642
        - [x] Q1792
        - [ ] Q1882

## Sorting

- [ ] Notes:
    - Implement sorts & know best case/worst case, average complexity of each:
        - no bubble sort - it's terrible - O(n^2), except when n <= 16
    - [ ] Stability in sorting algorithms ("Is Quicksort stable?")
        - [Sorting Algorithm Stability](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability)
        - [Stability In Sorting Algorithms](http://stackoverflow.com/questions/1517793/stability-in-sorting-algorithms)
        - [Stability In Sorting Algorithms](http://www.geeksforgeeks.org/stability-in-sorting-algorithms/)
        - [Sorting Algorithms - Stability](http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/stability.pdf)
    - [ ] Which algorithms can be used on linked lists? Which on arrays? Which on both?
        - I wouldn't recommend sorting a linked list, but merge sort is doable.
        - [Merge Sort For Linked List](http://www.geeksforgeeks.org/merge-sort-for-linked-list/)

- For heapsort, see Heap data structure above. Heap sort is great, but not stable

- [ ] [Sedgewick - Mergesort (5 videos)](https://www.coursera.org/learn/algorithms-part1/home/week/3)
    - [ ] [1. Mergesort](https://www.coursera.org/lecture/algorithms-part1/mergesort-ARWDq)
    - [ ] [2. Bottom up Mergesort](https://www.coursera.org/learn/algorithms-part1/lecture/PWNEl/bottom-up-mergesort)
    - [ ] [3. Sorting Complexity](https://www.coursera.org/lecture/algorithms-part1/sorting-complexity-xAltF)
    - [ ] [4. Comparators](https://www.coursera.org/lecture/algorithms-part1/comparators-9FYhS)
    - [ ] [5. Stability](https://www.coursera.org/learn/algorithms-part1/lecture/pvvLZ/stability)

- [ ] [Sedgewick - Quicksort (4 videos)](https://www.coursera.org/learn/algorithms-part1/home/week/3)
    - [ ] [1. Quicksort](https://www.coursera.org/learn/algorithms-part1/lecture/vjvnC/quicksort)
    - [ ] [2. Selection](https://www.coursera.org/lecture/algorithms-part1/selection-UQxFT)
    - [ ] [3. Duplicate Keys](https://www.coursera.org/lecture/algorithms-part1/duplicate-keys-XvjPd)
    - [ ] [4. System Sorts](https://www.coursera.org/lecture/algorithms-part1/system-sorts-QBNZ7)

- [ ] UC Berkeley:
    - [ ] [CS 61B Lecture 29: Sorting I (video)](https://archive.org/details/ucberkeley_webcast_EiUvYS2DT6I)
    - [ ] [CS 61B Lecture 30: Sorting II (video)](https://archive.org/details/ucberkeley_webcast_2hTY3t80Qsk)
    - [ ] [CS 61B Lecture 32: Sorting III (video)](https://archive.org/details/ucberkeley_webcast_Y6LOLpxg6Dc)
    - [ ] [CS 61B Lecture 33: Sorting V (video)](https://archive.org/details/ucberkeley_webcast_qNMQ4ly43p4)

- [ ] [Bubble Sort (video)](https://www.youtube.com/watch?v=P00xJgWzz2c&index=1&list=PL89B61F78B552C1AB)
- [ ] [Analyzing Bubble Sort (video)](https://www.youtube.com/watch?v=ni_zk257Nqo&index=7&list=PL89B61F78B552C1AB)
- [ ] [Insertion Sort, Merge Sort (video)](https://www.youtube.com/watch?v=Kg4bqzAqRBM&index=3&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
- [ ] [Insertion Sort (video)](https://www.youtube.com/watch?v=c4BRHC7kTaQ&index=2&list=PL89B61F78B552C1AB)
- [ ] [Merge Sort (video)](https://www.youtube.com/watch?v=GCae1WNvnZM&index=3&list=PL89B61F78B552C1AB)
- [ ] [Quicksort (video)](https://www.youtube.com/watch?v=y_G9BkAm6B8&index=4&list=PL89B61F78B552C1AB)
- [ ] [Selection Sort (video)](https://www.youtube.com/watch?v=6nDMgr0-Yyo&index=8&list=PL89B61F78B552C1AB)

- [ ] Merge sort code:
    - [ ] [Using output array (C)](http://www.cs.yale.edu/homes/aspnes/classes/223/examples/sorting/mergesort.c)
    - [ ] [Using output array (Python)](https://github.com/jwasham/practice-python/blob/master/merge_sort/merge_sort.py)
    - [ ] [In-place (C++)](https://github.com/jwasham/practice-cpp/blob/master/merge_sort/merge_sort.cc)
- [ ] Quick sort code:
    - [ ] [Implementation (C)](http://www.cs.yale.edu/homes/aspnes/classes/223/examples/randomization/quick.c)
    - [ ] [Implementation (C)](https://github.com/jwasham/practice-c/blob/master/quick_sort/quick_sort.c)
    - [ ] [Implementation (Python)](https://github.com/jwasham/practice-python/blob/master/quick_sort/quick_sort.py)

- [ ] Implement:
    - [ ] Mergesort: O(n log n) average and worst case
    - [ ] Quicksort O(n log n) average case
    - Selection sort and insertion sort are both O(n^2) average and worst case
    - For heapsort, see Heap data structure above

- [ ] Not required, but I recommended them:
    - [ ] [Sedgewick - Radix Sorts (6 videos)](https://www.coursera.org/learn/algorithms-part2/home/week/3)
        - [ ] [1. Strings in Java](https://www.coursera.org/learn/algorithms-part2/lecture/vGHvb/strings-in-java)
        - [ ] [2. Key Indexed Counting](https://www.coursera.org/lecture/algorithms-part2/key-indexed-counting-2pi1Z)
        - [ ] [3. Least Significant Digit First String Radix Sort](https://www.coursera.org/learn/algorithms-part2/lecture/c1U7L/lsd-radix-sort)
        - [ ] [4. Most Significant Digit First String Radix Sort](https://www.coursera.org/learn/algorithms-part2/lecture/gFxwG/msd-radix-sort)
        - [ ] [5. 3 Way Radix Quicksort](https://www.coursera.org/lecture/algorithms-part2/3-way-radix-quicksort-crkd5)
        - [ ] [6. Suffix Arrays](https://www.coursera.org/learn/algorithms-part2/lecture/TH18W/suffix-arrays)
    - [ ] [Radix Sort](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#radixSort)
    - [ ] [Radix Sort (video)](https://www.youtube.com/watch?v=xhr26ia4k38)
    - [ ] [Radix Sort, Counting Sort (linear time given constraints) (video)](https://www.youtube.com/watch?v=Nz1KZXbghj8&index=7&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [ ] [Randomization: Matrix Multiply, Quicksort, Freivalds' algorithm (video)](https://www.youtube.com/watch?v=cNB2lADK3_s&index=8&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
    - [ ] [Sorting in Linear Time (video)](https://www.youtube.com/watch?v=pOKy3RZbSws&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf&index=14)

As a summary, here is a visual representation of [15 sorting algorithms](https://www.youtube.com/watch?v=kPRA0W1kECg).
If you need more detail on this subject, see "Sorting" section in [Additional Detail on Some Subjects](#additional-detail-on-some-subjects)


## Graphs

Graphs can be used to represent many problems in computer science, so this section is long, like trees and sorting were.

- Notes:
    - There are 4 basic ways to represent a graph in memory:
        - objects and pointers
        - adjacency matrix
        - adjacency list
        - adjacency map
    - Familiarize yourself with each representation and its pros & cons
    - BFS and DFS - know their computational complexity, their trade offs, and how to implement them in real code
    - When asked a question, look for a graph-based solution first, then move on if none

- [ ] MIT(videos):
    - [ ] [Breadth-First Search](https://www.youtube.com/watch?v=oFVYVzlvk9c&t=14s&ab_channel=MITOpenCourseWare)
    - [ ] [Depth-First Search](https://www.youtube.com/watch?v=IBfWDYSffUU&t=32s&ab_channel=MITOpenCourseWare)

- [ ] Skiena Lectures - great intro:
    - [ ] [CSE373 2020 - Lecture 10 - Graph Data Structures (video)](https://www.youtube.com/watch?v=Sjk0xqWWPCc&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=10)
    - [ ] [CSE373 2020 - Lecture 11 - Graph Traversal (video)](https://www.youtube.com/watch?v=ZTwjXj81NVY&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=11)
    - [ ] [CSE373 2020 - Lecture 12 - Depth First Search (video)](https://www.youtube.com/watch?v=KyordYB3BOs&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=12)
    - [ ] [CSE373 2020 - Lecture 13 - Minimum Spanning Trees (video)](https://www.youtube.com/watch?v=oolm2VnJUKw&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=13)
    - [ ] [CSE373 2020 - Lecture 14 - Minimum Spanning Trees (con't) (video)](https://www.youtube.com/watch?v=RktgPx0MarY&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=14)
    - [ ] [CSE373 2020 - Lecture 15 - Graph Algorithms (con't 2) (video)](https://www.youtube.com/watch?v=MUe5DXRhyAo&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=15)

- [ ] Graphs (review and more):

    - [ ] [6.006 Single-Source Shortest Paths Problem (video)](https://www.youtube.com/watch?v=Aa2sqUhIn-E&index=15&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [ ] [6.006 Dijkstra (video)](https://www.youtube.com/watch?v=NSHizBK9JD8&t=1731s&ab_channel=MITOpenCourseWare)
    - [ ] [6.006 Bellman-Ford (video)](https://www.youtube.com/watch?v=f9cVS_URPc0&ab_channel=MITOpenCourseWare)
    - [ ] [6.006 Speeding Up Dijkstra (video)](https://www.youtube.com/watch?v=CHvQ3q_gJ7E&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=18)
    - [ ] [Aduni: Graph Algorithms I - Topological Sorting, Minimum Spanning Trees, Prim's Algorithm -  Lecture 6 (video)]( https://www.youtube.com/watch?v=i_AQT_XfvD8&index=6&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
    - [ ] [Aduni: Graph Algorithms II - DFS, BFS, Kruskal's Algorithm, Union Find Data Structure - Lecture 7 (video)]( https://www.youtube.com/watch?v=ufj5_bppBsA&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=7)
    - [ ] [Aduni: Graph Algorithms III: Shortest Path - Lecture 8 (video)](https://www.youtube.com/watch?v=DiedsPsMKXc&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=8)
    - [ ] [Aduni: Graph Alg. IV: Intro to geometric algorithms - Lecture 9 (video)](https://www.youtube.com/watch?v=XIAQRlNkJAw&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=9)
    - [ ] [CS 61B 2014: Weighted graphs (video)](https://archive.org/details/ucberkeley_webcast_zFbq8vOZ_0k)
    - [ ] [Greedy Algorithms: Minimum Spanning Tree (video)](https://www.youtube.com/watch?v=tKwnms5iRBU&index=16&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
    - [ ] [Strongly Connected Components Kosaraju's Algorithm Graph Algorithm (video)](https://www.youtube.com/watch?v=RpgcYiky7uw)

- Full Coursera Course:
    - [ ] [Algorithms on Graphs (video)](https://www.coursera.org/learn/algorithms-on-graphs/home/welcome)

- I'll implement:
    - [ ] DFS with adjacency list (recursive)
    - [ ] DFS with adjacency list (iterative with stack)
    - [ ] DFS with adjacency matrix (recursive)
    - [ ] DFS with adjacency matrix (iterative with stack)
    - [ ] BFS with adjacency list
    - [ ] BFS with adjacency matrix
    - [ ] single-source shortest path (Dijkstra)
    - [ ] minimum spanning tree
    - DFS-based algorithms (see Aduni videos above):
        - [ ] check for cycle (needed for topological sort, since we'll check for cycle before starting)
        - [ ] topological sort
        - [ ] count connected components in a graph
        - [ ] list strongly connected components
        - [ ] check for bipartite graph

## Even More Knowledge

- ### Recursion
    - [ ] Stanford lectures on recursion & backtracking:
        - [ ] [Lecture 8 | Programming Abstractions (video)](https://www.youtube.com/watch?v=gl3emqCuueQ&list=PLFE6E58F856038C69&index=8)
        - [ ] [Lecture 9 | Programming Abstractions (video)](https://www.youtube.com/watch?v=uFJhEPrbycQ&list=PLFE6E58F856038C69&index=9)
        - [ ] [Lecture 10 | Programming Abstractions (video)](https://www.youtube.com/watch?v=NdF1QDTRkck&index=10&list=PLFE6E58F856038C69)
        - [ ] [Lecture 11 | Programming Abstractions (video)](https://www.youtube.com/watch?v=p-gpaIGRCQI&list=PLFE6E58F856038C69&index=11)
    - When it is appropriate to use it?
    - How is tail recursion better than not?
        - [ ] [What Is Tail Recursion Why Is It So Bad?](https://www.quora.com/What-is-tail-recursion-Why-is-it-so-bad)
        - [ ] [Tail Recursion (video)](https://www.coursera.org/lecture/programming-languages/tail-recursion-YZic1)
    - [ ] [5 Simple Steps for Solving Any Recursive Problem(video)](https://youtu.be/ngCos392W4w)
	
	Backtracking Blueprint: [Java](https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning))
	[Python](https://leetcode.com/problems/combination-sum/discuss/429538/General-Backtracking-questions-solutions-in-Python-for-reference-%3A)
- ### Dynamic Programming
    - You probably won't see any dynamic programming problems in your interview, but it's worth being able to recognize a 
    problem as being a candidate for dynamic programming.
    - This subject can be pretty difficult, as each DP soluble problem must be defined as a recursion relation, and coming up with it can be tricky.
    - I suggest looking at many examples of DP problems until you have a solid understanding of the pattern involved.
    - [ ] Videos:
        - [ ] [Skiena: CSE373 2020 - Lecture 19 - Introduction to Dynamic Programming (video)](https://www.youtube.com/watch?v=wAA0AMfcJHQ&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=18)
        - [ ] [Skiena: CSE373 2020 - Lecture 20 - Edit Distance (video)](https://www.youtube.com/watch?v=T3A4jlHlhtA&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=19)
        - [ ] [Skiena: CSE373 2020 - Lecture 20 - Edit Distance (continued) (video)](https://www.youtube.com/watch?v=iPnPVcZmRbE&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=20)
        - [ ] [Skiena: CSE373 2020 - Lecture 21 - Dynamic Programming (video)](https://www.youtube.com/watch?v=2xPE4Wq8coQ&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=21)
        - [ ] [Skiena: CSE373 2020 - Lecture 21 - Dynamic Programming and Review (video)](https://www.youtube.com/watch?v=2xPE4Wq8coQ&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=21)
        - [ ] [Simonson: Dynamic Programming 0 (starts at 59:18) (video)](https://youtu.be/J5aJEcOr6Eo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3558)
        - [ ] [Simonson: Dynamic Programming I - Lecture 11 (video)](https://www.youtube.com/watch?v=0EzHjQ_SOeU&index=11&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
        - [ ] [Simonson: Dynamic programming II - Lecture 12 (video)](https://www.youtube.com/watch?v=v1qiRwuJU7g&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=12)
        - [ ] List of individual DP problems (each is short):
            [Dynamic Programming (video)](https://www.youtube.com/playlist?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr)
    - [ ] Yale Lecture notes:
        - [ ] [Dynamic Programming](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#dynamicProgramming)
    - [ ] Coursera:
        - [ ] [The RNA secondary structure problem (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/80RrW/the-rna-secondary-structure-problem)
        - [ ] [A dynamic programming algorithm (video)](https://www.coursera.org/lecture/algorithmic-thinking-2/a-dynamic-programming-algorithm-PSonq)
        - [ ] [Illustrating the DP algorithm (video)](https://www.coursera.org/lecture/algorithmic-thinking-2/illustrating-the-dp-algorithm-oUEK2)
        - [ ] [Running time of the DP algorithm (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/nfK2r/running-time-of-the-dp-algorithm)
        - [ ] [DP vs. recursive implementation (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/M999a/dp-vs-recursive-implementation)
        - [ ] [Global pairwise sequence alignment (video)](https://www.coursera.org/lecture/algorithmic-thinking-2/global-pairwise-sequence-alignment-UZ7o6)
        - [ ] [Local pairwise sequence alignment (video)](https://www.coursera.org/learn/algorithmic-thinking-2/lecture/WnNau/local-pairwise-sequence-alignment)

- ### Design patterns
    - [ ] [Quick UML review (video)](https://www.youtube.com/watch?v=3cmzqZzwNDM&list=PLGLfVvz_LVvQ5G-LdJ8RLqe-ndo7QITYc&index=3)
    - [ ] Learn these patterns:
        - [ ] strategy
        - [ ] singleton
        - [ ] adapter
        - [ ] prototype
        - [ ] decorator
        - [ ] visitor
        - [ ] factory, abstract factory
        - [ ] facade
        - [ ] observer
        - [ ] proxy
        - [ ] delegate
        - [ ] command
        - [ ] state
        - [ ] memento
        - [ ] iterator
        - [ ] composite
        - [ ] flyweight
    - [ ] [Series of videos (27 videos)](https://www.youtube.com/playlist?list=PLF206E906175C7E07)
    - [ ] [Book: Head First Design Patterns](https://www.amazon.com/Head-First-Design-Patterns-Freeman/dp/0596007124)
        - I know the canonical book is "Design Patterns: Elements of Reusable Object-Oriented Software", but Head First is great for beginners to OO.
    - [Handy reference: 101 Design Patterns & Tips for Developers](https://sourcemaking.com/design-patterns-and-tips)

- ### Combinatorics (n choose k) & Probability
    - [ ] [Math Skills: How to find Factorial, Permutation and Combination (Choose) (video)](https://www.youtube.com/watch?v=8RRo6Ti9d0U)
    - [ ] [Make School: Probability (video)](https://www.youtube.com/watch?v=sZkAAk9Wwa4)
    - [ ] [Make School: More Probability and Markov Chains (video)](https://www.youtube.com/watch?v=dNaJg-mLobQ)
    - [ ] Khan Academy:
        - Course layout:
            - [ ] [Basic Theoretical Probability](https://www.khanacademy.org/math/probability/probability-and-combinatorics-topic)
        - Just the videos - 41 (each are simple and each are short):
            - [ ] [Probability Explained (video)](https://www.youtube.com/watch?v=uzkc-qNVoOk&list=PLC58778F28211FA19)

- ### NP, NP-Complete and Approximation Algorithms
    - Know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem,
        and be able to recognize them when an interviewer asks you them in disguise.
    - Know what NP-complete means.
    - [ ] [Computational Complexity (video)](https://www.youtube.com/watch?v=moPtwq_cVH8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=23)
    - [ ] Simonson:
        - [ ] [Greedy Algs. II & Intro to NP Completeness (video)](https://youtu.be/qcGnJ47Smlo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=2939)
        - [ ] [NP Completeness II & Reductions (video)](https://www.youtube.com/watch?v=e0tGC6ZQdQE&index=16&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
        - [ ] [NP Completeness III (Video)](https://www.youtube.com/watch?v=fCX1BGT3wjE&index=17&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
        - [ ] [NP Completeness IV (video)](https://www.youtube.com/watch?v=NKLDp3Rch3M&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=18)
    - [ ] Skiena:
        - [ ] [CSE373 2020 - Lecture 23 - NP-Completeness (video)](https://www.youtube.com/watch?v=ItHp5laE1VE&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=23)
        - [ ] [CSE373 2020 - Lecture 24 - Satisfiability (video)](https://www.youtube.com/watch?v=inaFJeCzGxU&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=24)
        - [ ] [CSE373 2020 - Lecture 25 - More NP-Completeness (video)](https://www.youtube.com/watch?v=B-bhKxjZLlc&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=25)
        - [ ] [CSE373 2020 - Lecture 26 - NP-Completeness Challenge (video)](https://www.youtube.com/watch?v=_EzetTkG_Cc&list=PLOtl7M3yp-DX6ic0HGT0PUX_wiNmkWkXx&index=26)
    - [ ] [Complexity: P, NP, NP-completeness, Reductions (video)](https://www.youtube.com/watch?v=eHZifpgyH_4&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=22)
    - [ ] [Complexity: Approximation Algorithms (video)](https://www.youtube.com/watch?v=MEz1J9wY2iM&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=24)
    - [ ] [Complexity: Fixed-Parameter Algorithms (video)](https://www.youtube.com/watch?v=4q-jmGrmxKs&index=25&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
    - Peter Norvig discusses near-optimal solutions to traveling salesman problem:
        - [Jupyter Notebook](http://nbviewer.jupyter.org/url/norvig.com/ipython/TSP.ipynb)
    - Pages 1048 - 1140 in CLRS if you have it.

- ### How computers process a program

    - [ ] [How CPU executes a program (video)](https://www.youtube.com/watch?v=XM4lGflQFvA)
    - [ ] [How computers calculate - ALU (video)](https://youtu.be/1I5ZMmrOfnA)
    - [ ] [Registers and RAM (video)](https://youtu.be/fpnE6UAfbtU)
    - [ ] [The Central Processing Unit (CPU) (video)](https://youtu.be/FZGugFqdr60)
    - [ ] [Instructions and Programs (video)](https://youtu.be/zltgXvg6r3k)

- ### Caches
    - [ ] LRU cache:
        - [ ] [The Magic of LRU Cache (100 Days of Google Dev) (video)](https://www.youtube.com/watch?v=R5ON3iwx78M)
        - [ ] [Implementing LRU (video)](https://www.youtube.com/watch?v=bq6N7Ym81iI)
        - [ ] [LeetCode - 146 LRU Cache (C++) (video)](https://www.youtube.com/watch?v=8-FZRAjR7qU)
    - [ ] CPU cache:
        - [ ] [MIT 6.004 L15: The Memory Hierarchy (video)](https://www.youtube.com/watch?v=vjYF_fAZI5E&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-&index=24)
        - [ ] [MIT 6.004 L16: Cache Issues (video)](https://www.youtube.com/watch?v=ajgC3-pyGlk&index=25&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-)

- ### Processes and Threads
    - [ ] Computer Science 162 - Operating Systems (25 videos):
        - for processes and threads see videos 1-11
        - [Operating Systems and System Programming (video)](https://archive.org/details/ucberkeley-webcast-PL-XXv-cvA_iBDyz-ba4yDskqMDY6A1w_c)
    - [What Is The Difference Between A Process And A Thread?](https://www.quora.com/What-is-the-difference-between-a-process-and-a-thread)
    - Covers:
        - Processes, Threads, Concurrency issues
            - Difference between processes and threads
            - Processes
            - Threads
            - Locks
            - Mutexes
            - Semaphores
            - Monitors
            - How they work?
            - Deadlock
            - Livelock
        - CPU activity, interrupts, context switching
        - Modern concurrency constructs with multicore processors
        - [Paging, segmentation and virtual memory (video)](https://youtu.be/O4nwUqQodAg)
        - [Interrupts (video)](https://youtu.be/iKlAWIKEyuw)
        - Process resource needs (memory: code, static storage, stack, heap, and also file descriptors, i/o)
        - Thread resource needs (shares above (minus stack) with other threads in the same process but each has its own pc, stack counter, registers, and stack)
        - Forking is really copy on write (read-only) until the new process writes to memory, then it does a full copy.
        - Context switching
            - How context switching is initiated by the operating system and underlying hardware?
    - [ ] [threads in C++ (series - 10 videos)](https://www.youtube.com/playlist?list=PL5jc9xFGsL8E12so1wlMS0r0hTQoJL74M)
    - [ ] [CS 377 Spring '14: Operating Systems from University of Massachusetts](https://www.youtube.com/playlist?list=PLacuG5pysFbDQU8kKxbUh4K5c1iL5_k7k)
    - [ ] concurrency in Python (videos):
        - [ ] [Short series on threads](https://www.youtube.com/playlist?list=PL1H1sBF1VAKVMONJWJkmUh6_p8g4F2oy1)
        - [ ] [Python Threads](https://www.youtube.com/watch?v=Bs7vPNbB9JM)
        - [ ] [Understanding the Python GIL (2010)](https://www.youtube.com/watch?v=Obt-vMVdM8s)
            - [reference](http://www.dabeaz.com/GIL)
        - [ ] [David Beazley - Python Concurrency From the Ground Up: LIVE! - PyCon 2015](https://www.youtube.com/watch?v=MCs5OvhV9S4)
        - [ ] [Keynote David Beazley - Topics of Interest (Python Asyncio)](https://www.youtube.com/watch?v=ZzfHjytDceU)
        - [ ] [Mutex in Python](https://www.youtube.com/watch?v=0zaPs8OtyKY)

- ### Testing
    - To cover:
        - how unit testing works
        - what are mock objects
        - what is integration testing
        - what is dependency injection
    - [ ] [Agile Software Testing with James Bach (video)](https://www.youtube.com/watch?v=SAhJf36_u5U)
    - [ ] [Open Lecture by James Bach on Software Testing (video)](https://www.youtube.com/watch?v=ILkT_HV9DVU)
    - [ ] [Steve Freeman - Test-Driven Development (that’s not what we meant) (video)](https://vimeo.com/83960706)
        - [slides](http://gotocon.com/dl/goto-berlin-2013/slides/SteveFreeman_TestDrivenDevelopmentThatsNotWhatWeMeant.pdf)
    - [ ] Dependency injection:
        - [ ] [video](https://www.youtube.com/watch?v=IKD2-MAkXyQ)
        - [ ] [Tao Of Testing](http://jasonpolites.github.io/tao-of-testing/ch3-1.1.html)
    - [ ] [How to write tests](http://jasonpolites.github.io/tao-of-testing/ch4-1.1.html)

- ### String searching & manipulations
    - [ ] [Sedgewick - Suffix Arrays (video)](https://www.coursera.org/learn/algorithms-part2/lecture/TH18W/suffix-arrays)
    - [ ] [Sedgewick - Substring Search (videos)](https://www.coursera.org/learn/algorithms-part2/home/week/4)
        - [ ] [1. Introduction to Substring Search](https://www.coursera.org/lecture/algorithms-part2/introduction-to-substring-search-n3ZpG)
        - [ ] [2. Brute-Force Substring Search](https://www.coursera.org/learn/algorithms-part2/lecture/2Kn5i/brute-force-substring-search)
        - [ ] [3. Knuth-Morris Pratt](https://www.coursera.org/learn/algorithms-part2/lecture/TAtDr/knuth-morris-pratt)
        - [ ] [4. Boyer-Moore](https://www.coursera.org/learn/algorithms-part2/lecture/CYxOT/boyer-moore)
        - [ ] [5. Rabin-Karp](https://www.coursera.org/lecture/algorithms-part2/rabin-karp-3KiqT)
    - [ ] [Search pattern in text (video)](https://www.coursera.org/learn/data-structures/lecture/tAfHI/search-pattern-in-text)

    If you need more detail on this subject, see "String Matching" section in [Additional Detail on Some Subjects](#additional-detail-on-some-subjects).

- ### Tries
    - Note there are different kinds of tries. Some have prefixes, some don't, and some use string instead of bits
        to track the path
    - I read through code, but will not implement
    - [ ] [Sedgewick - Tries (3 videos)](https://www.coursera.org/learn/algorithms-part2/home/week/4)
        - [ ] [1. R Way Tries](https://www.coursera.org/learn/algorithms-part2/lecture/CPVdr/r-way-tries)
        - [ ] [2. Ternary Search Tries](https://www.coursera.org/learn/algorithms-part2/lecture/yQM8K/ternary-search-tries)
        - [ ] [3. Character Based Operations](https://www.coursera.org/learn/algorithms-part2/lecture/jwNmV/character-based-operations)
    - [ ] [Notes on Data Structures and Programming Techniques](http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html#Tries)
    - [ ] Short course videos:
        - [ ] [Introduction To Tries (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/08Xyf/core-introduction-to-tries)
        - [ ] [Performance Of Tries (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/PvlZW/core-performance-of-tries)
        - [ ] [Implementing A Trie (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/DFvd3/core-implementing-a-trie)
    - [ ] [The Trie: A Neglected Data Structure](https://www.toptal.com/java/the-trie-a-neglected-data-structure)
    - [ ] [TopCoder - Using Tries](https://www.topcoder.com/community/competitive-programming/tutorials/using-tries/)
    - [ ] [Stanford Lecture (real world use case) (video)](https://www.youtube.com/watch?v=TJ8SkcUSdbU)
    - [ ] [MIT, Advanced Data Structures, Strings (can get pretty obscure about halfway through) (video)](https://www.youtube.com/watch?v=NinWEPPrkDQ&index=16&list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf)

- ### Floating Point Numbers
    - [ ] simple 8-bit: [Representation of Floating Point Numbers - 1 (video - there is an error in calculations - see video description)](https://www.youtube.com/watch?v=ji3SfClm8TU)

- ### Unicode
    - [ ] [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets]( http://www.joelonsoftware.com/articles/Unicode.html)
    - [ ] [What Every Programmer Absolutely, Positively Needs To Know About Encodings And Character Sets To Work With Text](http://kunststube.net/encoding/)

- ### Endianness
    - [ ] [Big And Little Endian](https://web.archive.org/web/20180107141940/http://www.cs.umd.edu:80/class/sum2003/cmsc311/Notes/Data/endian.html)
    - [ ] [Big Endian Vs Little Endian (video)](https://www.youtube.com/watch?v=JrNF0KRAlyo)
    - [ ] [Big And Little Endian Inside/Out (video)](https://www.youtube.com/watch?v=oBSuXP-1Tc0)
        - Very technical talk for kernel devs. Don't worry if most is over your head.
        - The first half is enough.

- ### Networking
    - **if you have networking experience or want to be a reliability engineer or operations engineer, expect questions**
    - Otherwise, this is just good to know
    - [ ] [Khan Academy](https://www.khanacademy.org/computing/code-org/computers-and-the-internet)
    - [ ] [UDP and TCP: Comparison of Transport Protocols (video)](https://www.youtube.com/watch?v=Vdc8TCESIg8)
    - [ ] [TCP/IP and the OSI Model Explained! (video)](https://www.youtube.com/watch?v=e5DEVa9eSN0)
    - [ ] [Packet Transmission across the Internet. Networking & TCP/IP tutorial. (video)](https://www.youtube.com/watch?v=nomyRJehhnM)
    - [ ] [HTTP (video)](https://www.youtube.com/watch?v=WGJrLqtX7As)
    - [ ] [SSL and HTTPS (video)](https://www.youtube.com/watch?v=S2iBR2ZlZf0)
    - [ ] [SSL/TLS (video)](https://www.youtube.com/watch?v=Rp3iZUvXWlM)
    - [ ] [HTTP 2.0 (video)](https://www.youtube.com/watch?v=E9FxNzv1Tr8)
    - [ ] [Video Series (21 videos) (video)](https://www.youtube.com/playlist?list=PLEbnTDJUr_IegfoqO4iPnPYQui46QqT0j)
    - [ ] [Subnetting Demystified - Part 5 CIDR Notation (video)](https://www.youtube.com/watch?v=t5xYI0jzOf4)
    - [ ] Sockets:
        - [ ] [Java - Sockets - Introduction (video)](https://www.youtube.com/watch?v=6G_W54zuadg&t=6s)
        - [ ] [Socket Programming (video)](https://www.youtube.com/watch?v=G75vN2mnJeQ)

---