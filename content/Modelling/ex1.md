Title: First Exercise  
Date: 2015-08-13
Tags: Fifth-Semester
Summary: This is a program that splatters paint around the mouse.

## Experience
For this program, I had to think about distributions for both the splatter distance, and the rgb distance, however, using Gaussian random numbers, which implement standard distribution and bell curves, this simplified the problem. I solved the problem gradually, first making the splatter around the mouse, and later changing the colors, finally I implemented the mouse following. 


<iframe width="420" height="315" src="https://www.youtube.com/embed/XwpK63nb7d0" frameborder="0" allowfullscreen></iframe>
## Code

:::java
    import java.util.Random;
    Random generator; 
    float redmean,bluemean,greenmean;


    void setup() {
      size(640*2, 360*2);
      background(0);

      generator = new Random();
      redmean = bluemean = greenmean =  255/2;
    }

    void draw() {

      // Get a gaussian random number w/ mean of 0 and standard deviation of 1.0
      float xloc = (float)generator.nextGaussian();
      float yloc = (float)generator.nextGaussian();
      //randomGaussian();

      float sd = 20, csd = 20;                // Define a standard deviation
      float mean = width/2;         // Define a mean value (middle of the screen along the x-axis)
      xloc = ( xloc * sd ) + mouseX;
      yloc = ( yloc * sd ) + mouseY;  // Scale the gaussian random number by standard deviation and mean

      noStroke();
      float redloc = (float)generator.nextGaussian() * csd + redmean; 
      float greenloc = (float)generator.nextGaussian() * csd + bluemean;
     float blueloc = (float)generator.nextGaussian() * csd + greenmean;
      
      fill(redloc, greenloc, blueloc);
      noStroke();
      ellipse(xloc, yloc, 16, 16);   // Draw an ellipse at our "normal" random location
    }
    void keyPressed(){
      switch (key){
       case 'r':
       redmean = 3*(255/3);
       break;
       case 'b':
          bluemean = 3*(255/3);
       break;
       case 'g':
          greenmean = 3*(255/3);
       break;
      }
    }

    void keyReleased(){
      switch (key){
       case 'r':
       redmean = (255/2);
       break;
       case 'b':
          bluemean = (255/2);
       break;
       case 'g':
          greenmean = (255/2);
       break;
       case 'c':
       background(0);
      }
    }

