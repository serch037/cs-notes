Title: Stacks
Date: 2015-03-18
Tags: Fourth_Semester
Summary: A stack is a LIFO data structure.

## Definition
Within computer science, stacks are one of the most important data structures, which just means that they are containers of objects and organize them in a certain way, following some basic principles.  The stack has a *top*, and a *bottom*, this, respectively, refer to the  last element added to the list and the point in which elements can no longer be removed from the stack. A stack must have a limited size which should be declared at the time of creation, so that as more elements are added, the system may know when the stack is full and therefore, is able to prevent what is known as a stack overflow.  

The basic operations that may be applied to a stack are called **push** and **pop**. This are some CS-specific way, which may be interpreted respectively as insert, and remove. 

A stack may be represented using an array in the following fashion:

<div style="text-align: center">
   <img src=" http://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/pix/array_stack.bmp" alt="Your alt text" title="Title"/>

</div>
## Possible Applications
Stacks are used by computers in order to assign memory and resources to procedures and instructions, so several languages and compilers implement this kind of structure.  These are some classical examples of when the most recent elements are the one that need to be accessed and processed. 


### Excercises
* Code in java the basic stack operations. Make sure to check for stack overflow and underflow. 

~~~~c
int push(int number, int stack[]){
  if ((stack_top >= stack_size-1)){
    //println("TEN");
    return 1;
    
  }
  stack_top++;
  stack[stack_top] = number;
  return 0; 
}


int pop(int stack[]){ //Returns -1 if empty
if (stack_top -1 < stack_bottom){
    println("Stop");
    return -1; 
}
int number = stack[stack_top];
stack[stack_top] = 0; 
stack_top--;
System.out.println(Arrays.toString(stack));
println(stack_top);

return number;
}
~~~~

* Develop a function that takes an array representing a stack, and an integer n, and creates a resized version of the stack of n elements. 

## Additional Resources 
* http://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html
* http://www.cprogramming.com/tutorial/computersciencetheory/stack.html
* www.cs.umd.edu/class/sum2003/cmsc311/Notes/Mips/stack.html
* algs4.cs.princeton.edu/13stacks/
* http://www.algolist.net/Data_structures/Stack/Array-based_implementation
