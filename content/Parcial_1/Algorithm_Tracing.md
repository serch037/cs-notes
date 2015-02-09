Title: Algorithm Tracing
Date: 2015-02-08 
Modified: 2015-02-08
Tags: Algorithms, Fourth_Semester


## Definition 
This refers to a step-by-step analysis of what a computational calculation performs. By making it explicit what is executed in the program and how the variables included are affected in each execution cycle. 

## Example
The following example, coded in (*ref*) C, illustrates the tracing of reversing the contents on an (ref) Array:

Code:

~~~~ {.c}
#include <stdio.h>
int main (void){
int my_array[6] = {1,2,3,4,5,6};
int size=6, x,temp, index = size-1;

for (x=0; x<size/2;x++){
temp = my_array[x];
my_array[x] =my_array[index];
my_array[index--] = temp;
}
~~~~

## Tracing:
* General Information:
    * Times the loop runs: 3
    * Variables & their purpose: _size_: Self-explanatory; *temp*: Aids in swap operation; _x_: For loop counter. 
* State of the variables at end of each loop:

| x | temp | my_array[]  | index |
| - | -    | ------      | -     |
| 0 | 1    | 6,2,3,4,5,1 | 5     |
| 1 | 2    | 6,5,3,4,2,1 | 4     |
| 2 | 3    | 6,5,4,3,2,1 | 3     |


* Final & initial state of the array:
    
    :::text
    {1,2,3,4,5,6} becomes {6,5,4,3,2,1}

## Conclusion
