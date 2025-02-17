# Find Longest Sequence
## Description

This project implements an algorithm to find the longest sequence of 
numbers where each subsequent number starts with the last two digits
of the previous one.

The numbers are read from a source.txt file, and a directed graph is 
built, where nodes represent the first two digits of each number, 
and edges connect numbers based on matching last and first digits. 
Depth-first search (DFS) is used to find the longest possible path.

## Features
	•	Reads a set of numbers from source.txt.
	•	Builds a dependency graph based on matching first and last digits.
	•	Uses DFS to find the longest sequence.
	•	Constructs the final output string, appending numbers without repeating overlapping digits.

## Possible Improvements
	•	Optimize search (memoization or greedy algorithm).
	•	Add tests (unittest or pytest).
	•	Visualize the graph connections between numbers.