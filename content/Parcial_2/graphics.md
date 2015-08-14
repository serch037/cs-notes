Title: 3D Graphics  
Date: 2015-03-19
Tags: Fourth_Semester
Summary: Computer graphics is an advantage topic within computer science, which combines knowledge from programming, mathematics and design. 

## Definition
This topic refers to the techniques used to represent images using algorithmically in a computer for several purposes, such as animation, data visualization, etc. It includes both the processing and the representation of two-dimentional and three-dimensional graphics. 

## Mathematical topics
* Geometry
* Vectors
* Matrixes
* Etc. 

## 3D Models
As previously established, computers require certain abstractions for representing graphics. The most basic one, is the use of triangles in intersecting surfaces. This triangles are described using a series of vertexes. The process by which a 3D object is converted into a model suitable for graphical representation in a computer is called modeling. As the numbers of such base figure increases, the resolution of the image increases as well, but so does the expensiveness of the calculations involved. 

<div style="text-align: center">
   <img src="http://xoo.me/template/7820/p16laf9eb4otd6etedj1fki1qhh9-thumb.jpg " alt="Your alt text" title="Title"/>
</div>

Therefore, most 3d objects may be represented combining some basic figures, this are known as *primitives*, in processing the primitives are called as follows: 
* box(int size);
* sphere(int radius);

More complex models, may be defined using the beginShape(), vertex(x,y,z), and endShape() functions. Refer to the processing documentation for further information. 

## Transformations
Once modeled, objects may be rotated, scaled or translated (displaced). This procedures are applied in what is known as a *transformation matrix*, which is the medium that represents the space in which the object is placed. 

<div style="text-align: center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/vQ60rFwh2ig" frameborder="0" allowfullscreen></iframe>
</div>

## Basic Animation
Animation may be considered as a series of sequential animations applied to a graphical object, so in order to transmit the illusion of movement, an object may be translated several times, following small steps and a determined path. Scale and rotation may be used to create other effects. The most important aspect, is that the object should be redrawn in each frame with a slight difference, so that when the transformation is applied throughout the frames, an effect of animation takes place.  



## Lights, Materials, Textures
Another aspect of 3D graphics, is the consideration of lightning. This has a qualitative impact on the nature of the scene to be rendered, and is closely related to other topics, such as materials and textures. Lightning helps to illustrate the relative distance between a model and a lightning source. Then, a texture refers to how the model should be filled so that it does not appear as a monochromatic mesh. A material may be simulated in the way an object reflects light and, when related to its texture, gives a more realistic effect, therefore, a “metallic” model, may reflect light differently than a “plastical” model, this may be accomplished by a combinations of the shininess() and specularity() methods in processing, among other techniques.

<div style="text-align: center">
   <img src="http://graphics.cs.yale.edu/site/sites/files/images/Aging Materials_teaser.png" alt="Your alt text" title="Title"/>
</div>

## Tools
According to the abstraction level & the optimization requirement different tools are available for programmers. Some of them include: 

* OpenGl
* DirectX
* Processing (which is the one to be used during this course)
* Unity
* Blender
* Unreal Engine

## Additional Resources
* [Processing Transformations](https://processing.org/tutorials/transform2d/)
* [Computer Graphics course]( https://www.edx.org/course/foundations-computer-graphics-uc-berkeleyx-cs184-1x )
*  Graphics series with John Chapman:
    * [Universe of Triangles]( http://youtu.be/KdyvizaygyY )
    * [Power of the Matrix]( http://youtu.be/vQ60rFwh2ig )
    * [Triangles to Pixels]( http://youtu.be/aweqeMxDnu4 )
    * [Visibility Problem]( http://youtu.be/OODzTMcGDD0 )
