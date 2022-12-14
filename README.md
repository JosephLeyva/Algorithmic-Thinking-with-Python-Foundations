# Algorithmic Thinking with Python: Foundations
This is the repository for the LinkedIn Learning course Algorithmic Thinking with Python: Foundations. The full course is available from [LinkedIn Learning](https://www.linkedin.com/learning/).

## 100 Door Challenge

### *Problem Statement*

Imagine you have 100 doors in a row that are all initially closed. You are going to make 100 passes by each of these doors. On the first pass, you are going to visit each door in sequence and toggle it state (if it’s closed it becomes open and vice versa). For the second pass you visit every second door and toggle it state. For the third pass you visit every third door, and so on and so forth, until you only visit the 100th door on the 100th pass. Which doors are open and which are closed after the last pass?

## The Fizz Buzz Coding Challenge

### *Problem Statement*

It’s a game for two or more players and you take it turns to count aloud from one to 100, but each time you are going to say a multiple of 3, replace it with the word **“fizz”**, and each time you are going to say a multiple of 5, you replace it with the word **“buzz”**, and for numbers which are multiple of both 3 and 5, you say **“fizzbuzz”**

### *Example*

```one, two, fizz, fout, buzz, fizz, seven, eight, fizz, ...```

----
## Brute Force Search

Many computational problems can be solved by trying all possible candidate solutions until the correct solution is found. This approach is often called exhaustive search or brute force search. Although clumsy and inefficient, a brute force version of an algorithm is often well worth trying to get a feel of the problem before attempting to implement a better solution.The reason a better solution is often needed is that for many problems, the brute force method takes an impractical amount of time.

## Linear Search

A classic example of a brute force algorithm is a **linear search**. This involves checking each item in the collection if it is the one we are looking for

## Selection Sort

Selection Sort is an intuitive sorting algorithm. The basic idea of selection sort is to find the smallest element in the array and exchange it with the element in the first position. Then we need to repeat this process for the <u>remaining items</u>. So we next find the second smallest element in the array and exchange it with the element in the second position. We keep continuing this until the array is sorted.

## Find Minimum Value

The algorithm of finding a minimum value is:

- Create a variable called `min_index` and set it to the first position on the list (usually 0). Notice that we are talking about the index rather than the value
- Once we set our `min_index`, we iterate through the list, and if a value of the given index is greater than the one at `min_index`, then we update `min_index` to the new position.

---

## Analysis of Algorithms

The efficiency of algorithms is important. When we discuss analysis in the context of algorithms, we are generally referring to the efficiency of an algorithm or the lack of it. The opposite of efficiency is often referred to as complexity.

### Algorithm Analysis

- There are two types of efficiency we are interested in:
    - Time Complexity: The time taken by an algorithm to execute
    - Space Complexity: The amount of memory used by an algorithm while executing.

## Big-O Notation

In terms of algorithm analysis, big-o notation is a way of expressing an upper bound on the execution time or space requirements of an algorithm.

---

## Greedy Algorithms

A Greedy Algorithm is one which makes locally optimal choices at any given point. Once a choice is made, it does not revisit it.

This can make the algorithm “short sighted”, and it may not always find the optimal solution. However there are advantages to the greedy approach.

### Advantages

- Often quite fast
- Relatively easy to implement

### Disadvantages

- Short sighted ⇒ may not provide optimal solution.
- May fail on some instances of the problem.

### Features

- Make locally optimal choices
- Do not revisit choices once made

## The Change-Making Problem

The Change-Making Problem has become something of a classic due to what it can show us about different approaches to algorithmic problem solving. Here we are going to solve it using a greedy approach

### *Problem Statement*

Find the minimum number of coins from a set of denominations that add up to a given amount of money.

## Dijkstra Shortest Path Algorithm

Another classic greedy algorithm is Dijkstra Shortest Path Algorithm, which is used to find the shortest path between two vertices of a weighted graph. Dijkstra’s algorithm is optimal, meaning it will always find the shortest path, provided the weights in the graph are not negative. As a bonus, it actually gives us the shortest path to all vertices in the graph.