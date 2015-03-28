Title: Recursion
Date: 2015-03-21
Tags: Fourth_Semester
Summary: Recursion is a programming technique which allows for more elegant code under certain circumstances. 

## Definition

<div style="text-align: center">
   <img src=" http://www.pxleyes.com/blog/wp-content/uploads/2010/06/escher-hands.png" alt="Your alt text" title="Title"/>

</div>
Recursion may be thought of as a programming paradigm that considers functions which call themselves in order to process information.  Its complimentary paradigm is iteration.

**Important note:** Recursion requires the declaration of a *limit case*, which determines where the recursive process should stop and return control to a head or main function, otherwise the recursive  method will descend until memory is exhausted.

## Advantages & Disadvantages
Pros:
* Resulting code may be cleaner, smaller, more elegant and better illustrate what the code does.

Cons: 
* Function calls tend to be computationally expensive in most programming languages. 
* If not coded using techniques such as tail-recursion, execution can easily result in a stack overflow. 

## Tail Recursion
Tail recusrion  possible implementation of recursive functions, in which the recursive call is executed in the end, this means that the result of the last recursive call, is the result of the function itself. This allows the compiler to optimize the code by not saving, and duplicating the stack in each recursive call. An important aspect of tail recursive functions is that they may be directly implemented as iterative functions, unlike non-tail recursive ones. A tail recursive function, usually takes an additional argument, and in order to simplify code, implements and additional helper function. 

A graphic tracing of the algorithm reveals the advantages of tail recursion over non-tail recursive methods.
<div style="text-align: center">
   <img src=" http://t1.gstatic.com/images?q=tbn:ANd9GcSHuIW396JU13EzPx5qULmiq5pqPnlw90KWD0VW7EKZuLM5lFn5" alt="Your alt text" title="Title"/>

</div>

## Example
The *de facto* example of a recursive function is the factorial one. Here, we will exemplify two possible of implementation of recursion in factorial. Before looking at the solution try to implement it on pseudocode yourself. 

Simple solution:

~~~~java
  static int fact(int n) {
	
	// Base Case: 
	//    If n <= 1 then n! = 1.
	if (n <= 1) {
	    return 1;
	}
	// Recursive Case:  
	//    If n > 1 then n! = n * (n-1)!
	else {
	    return n * fact(n-1);
	}
~~~~

Tail recursive solution: 

~~~~java
int factorial(int number) {
    if(number == 0) {
           return 1;
        }
        factorial_i(number, 1);
}

int factorial_i(int currentNumber, int sum) {
    if(currentNumber == 1) {
        return sum;
    } else {
        return factorial_i(currentNumber - 1, sum*currentNumber);
    }
}

~~~~
Note that the trace of the second implementation would result in much lower memory used in the stack as the n value gets progressively higher, also note how tail recursion implements an additional function --often called helper function--  

## Excercises 
1. Develop a function that prints the contents of an array, and if possible, implment tail-recursion or some other optimization. 
2. Find the lowest and highest values of an array. 

## Additional Resources 
[Recursion -- Haskell reference]( http://learnyouahaskell.com/recursion )
[Recursion Notes]( http://pages.cs.wisc.edu/~vernon/cs367/notes/6.RECURSION.html )
[Recursion in Java]( http://danzig.jct.ac.il/java_class/recursion.html )
[Factorial using tail recursion]( http://users.dickinson.edu/~braught/courses/cs132f01/classes/code/Factorial.src.html )
