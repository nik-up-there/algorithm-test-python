# [Mobeye](https://www.mobeye-app.com) preliminary test

## Guidelines

- [duplicate](https://help.github.com/articles/duplicating-a-repository/) this repository (do **not** fork it)
- Answer the [exercises](https://github.com/Mobeye/algorithm-test-python/blob/master/exercises.py)
- Commit your answers to your repository
- The command ``python main.py`` is expected to run successfully 

## Requirements

- Python 3.6
- No dependencies needed

## Exercises

If you don't find the solution of an exercise, don't worry,
just write your thoughts and what you tried and we will look at it 

### Exercise 1

In this exercise you need to write a function taking 2 strings as input and 
returning `True` if the strings are anagrams and `False` otherwise. <br/>
Two strings are anagrams if they contain exactly the same letters 
in a possibly different order. <br/>
Eg : `"abc"` and `"cab"` are anagrams, `"aab"` and `"bba"` are not

### Exercise 2

Here you will need to write an algorithm that determines if a string is 
properly parenthesized, ie it is of the form "(p)" or "pq" where p and q
are properly parenthesized strings. Any string (including the empty string)
that does not contain any parenthesis is properly parenthesized. <br/>
Eg : `"()()"` is properly parenthesized, `"(()"` is not

### Exercise 3

For this one you will need to find the shortest path in a maze from a start
to an end. The maze is represented by a matrix (more exactly a list of lists)
containing only 0 and 1 - 0 is a wall, 1 is a path. <br/>
Every coordinate in the maze is represented by a tuple `(x, y)` where x and y
are the indices of the point in the list of lists.
This function should return a list of points forming the shortest_path in the
maze `[(x1, y1), (x2, y2), ...]` between `start` and `end`, or `False`
if there is no path. <br/>
The only movements allowed are UP/DOWN/LEFT/RIGHT
