# Simple programming language visualiser
**for Compilers and Theory of Compilation course**

## Introduction

### Authors
 - Kacper Dłubała - kacperd@student.agh.edu.pl
 - Andre Baron - andrebaron@student.agh.edu.pl
 
### Goal
The goal is to create a compiler for a custom programming language, transpiled not to another language, but to a sequence of simple 2D animations meant to help beginner programmers visualise the inner workings of loops, functions, conditional statements, data structures and more.

### Tech stack
- Python3
- ANTLR4
- PyGame

### Code example
```
fun str:fun1(int a1){
    ret "abcd";
}

str result = fun1(3);

// flo b = 4;
int a = 5;
if(a == 5){
    lst[int] l = [1, 2, 3];

    int sum = 0;
    lop(int a in [1..5]){
        sum = sum + a;
    }
}

int if1 = 7;

lst[int] abcd = [1, 2, 3];
```
