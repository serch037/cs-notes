Title: Linked Lists
Date: 13-04-2015

## General Intro

### Dynamic Data Structure
Generally, a linked list is a linear data structure in which the each of the items contained within, points to a single, following item and is pointed by other item, except the last and first items respectively. This set of items and pointed items defines the order of the linked list. 
* Pointer: An object that points to a node, organizing the list by *atatching* elements. 
* Node: Independent items or elements  stored in memory (also refered as a pointee)

* Dynamic vs static:
    * Static data structures, such as arrays, should be declared along with the size it should be allocated with. 
    * In static data structures insertion and deletion is an expensive operation. 
    * In dynamic data structures the opposite applies, however random access is not allowed, so certain operations, such as binary search are impossible to accomplish. 
    * Extra space is required to store pointers along with the nodes. 
    
* Items in a linked list must be *accessed sequentially*. So it is  important notice, linked list do not easily allow *random access* which in some cases may make the use of a different data structure more suitable. 

## Logical operations
* Linked lists may be reordered simply by changing the node a pointer aims, therefore saving the cost of actually moving data. 

## Implementations and sketches

* Single-linked 
* Double-linked
* Circular

## Appendix
* Basic operations
* Stack and queue implmentation
    * http://www.sanfoundry.com/c-program-stack-using-linked-list/
    * http://www.zentut.com/c-tutorial/c-stack-using-pointers/
    * www.c4learn.com/c-programs/c-program-to-implement-stack-operations-using-singly-linked-list.html

## Experiments

<iframe src="http://hascanvas.com/flowers/embed" frameborder="0" scrolling="no" style="width:600px;height:400px;"></iframe>


<iframe width="748" height="800" scrolling="no" frameborder="0" src="http://www.openprocessing.org/sketch/193632/embed/?width=720&height=720&border=true"></iframe>

#### Resources 
http://www.geeksforgeeks.org/linked-list-vs-array/
http://crunchify.com/how-to-implement-a-linkedlist-class-from-scratch-in-java/
http://www.geeksforgeeks.org/memory-efficient-doubly-linked-list/
http://www.eternallyconfuzzled.com/tuts/datastructures/jsw_tut_linklist.aspx
http://www.cs.cmu.edu/~clo/www/CMU/DataStructures/Lessons/lesson1_2.htm

http://cslibrary.stanford.edu/103/LinkedListBasics.pdf

