Title: Subroutines and Functions
Date: 2015-02-08
Tags: Functions, Fourth_Semester

### Definition
A function is a very useful programming concept, as it relates to the modular nature of problem solving in the computer sciences. It may be stated as a _subprogram_ which inside the _main_ statements, processes information. On a basic level, it saves programmers its time by preventing them from repeating the same lines of code for similar or even identical tasks. As a matter of fact, most programming languages include a core library (which is a collection of functions) so programmers are not required to write code for the most common tasks, such as getting the size of an array, or printing a value.  

Some functions yield a result of the process they carry out, this process is known as _returning_ a value if they do not return any value, they may be known as void functions.

Note: Functions are known by distinct names in different programming languages, the most common alternatives are methods, subroutines, both of which are essentially the same. 

__Use them for repetitive tasks possibly implementing a library.__ 


#### C-like syntax

~~~~c 
// In languages such as C, the standard is to declare functions
// before using them. This is called function prototyping.
// Example: 
int aFunction( int, some_parameters); 

//more code

Calling the function
result = aFunction(The_parameters);

// Declaration
int aFunction( int, some_parameters){
//Data processing
return result;
}
~~~~



