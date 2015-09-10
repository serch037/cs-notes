Title: Second (First Chapter) Exercise
Date: 2015-08-13 
Tags: Fifth-Semester 
Summary: This program simulates a ball attracted towards the pointer.

## Experience 
This program was more frustrating to write, as I wasn't initially sure how to simulate acceleration and deceleration. Finally I added a variable that scales the acceleration vector according to the key the user presses. 

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
