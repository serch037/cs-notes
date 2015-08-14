Title: Two Dimensional Arrays
Date: 2015-02-08 
Tags: Arrays, Fourth_Semester

### Definition
In a fundamental way, two dimensional arrays are rather similar two one dimentional arrays, as the processor treats it as an _extended_ one dimensional array. For the user, however, the net effect is effectively different. Two dimensional arrays are best represented, by a two dimensional matrix of information. However, the notion of an array of arrays is also valid, and, as a matter of fact, useful for grasping the concept of its syntax and declaration. 

### Essential operations
* Declaration and assignment
* Looping 
    * Requires two indexes and loops
* Vertical and/or horizontal rotation

#### C-like syntax

~~~~c
// Declaration
int an_array[3][2] = { 
    {1,2},
    {4,5},
    {7,8},
}
// When used as function argument, its size must be given first.
int an_arrayFunction(int sizex, sizey, anrray[sizey][sizex]);

~~~~

### Additional resources

#### Graphics
[Midpoing line algorithm](http://www.mat.univie.ac.at/~kriegl/Skripten/CG/node25.html)
[Midpoint cirle algorithm](http://www.asksatyam.com/2011/01/midpoint-circle-algorithm.html)



