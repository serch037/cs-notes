Title: Queues  
Date: 2015-03-20
Tags: Fourth_Semester
Summary: A queue is a FIFO data structure.

## Definition
A queue is a container of objects --otherwise known as a data structure--, that stores elements in such a way that new elements are added to the back, and the ones to be processed are chosen from the bottom. 
<div style="text-align: center">
   <img src=" http://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Queue_algorithmn.jpg/400px-Queue_algorithmn.jpg" alt="Your alt text" title="Title"/>

</div>


The basic queue operations are enqueue() and dequeue(), this respecively insert and delete elements from what is known as the rear, and front of the queue. This parts are analogous to the stack’s top and bottom. 

## Differences from  Stacks
An important difference from the stack data structure to be considered, is the way both handle removal of items. Within a queue, the process is not as simple as only declaring certain item as able to be overwritten, as this would lead to a scenario in which space in the queue is simply inaccessible and wasted. Therefore two alternatives are possible: 
    1. To displace each element of the array 
    2. To implement the queue using a *circular array*
While the first solution is more straight forward, it is also severely inefficient, so (2) would be much more appropriate, even though the implementation is not as simple. 

<div style="text-align: center">
   <img src="http://www.codeproject.com/KB/threads/LockFree/circular_queue___conceptual-view.jpg" alt="Your alt text" title="Title"/>

</div>

### Exercise 
1. Develop the basic queue operations using a circular array.
~~~java
void enQ(int value, int q[]){
  if (!(count+1 > SIZE)){
  //Calculate new top
  top = (top+1)% SIZE;
  count ++;
  q[top] = value;
  }
  //System.out.println(Arrays.toString(QUEUE));
}

int deQ(int q[]){
  int number = 0;
  if ((count-1 >= 0)){
  //Calculate new bottom
  bottom = (bottom +1) % SIZE;
  count--;
  number = q[bottom];
  q[bottom] = 0;
  println("Count: "+ count +" Top: " +top +" Bottom: "+bottom);
  }
  //System.out.println(Arrays.toString(QUEUE));
  return number;
}
~~~
2 Develop a peek() function that returns the element in the front of the queue without removing it. 

## Possible Applications
Queues are often implemented within an operating system for determining the priority of certain instructions, this is known as *scheduling*, and is useful both for CPU time allocation, as well as I/O resources. 

## Additional Resources 
* [Stacks and Queues]( http://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html )
* [Implementation in C++]( http://www.cprogramming.com/tutorial/computersciencetheory/queue.html )
