import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.awt.Color; 
import java.util.ArrayList; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class convowithpython extends PApplet {



PrintWriter output;
PImage img;
String[] words;
String singleword;

public void setup() {
  // Set window
  
  background(0);
  fill(255);

  // Load the image
  img = loadImage("../../temp_image/image.jpg");
  
  // Create word file
  output = createWriter("./singleWord.txt");
  
  // Load sample strings
  String[] lines= loadStrings("./data/text.txt"); 
  String wholetext=join(lines," ");
  words= split(wholetext," ");

  // Display the image
  image(img, 0, 0, width, height);
  
  // Get random pixel of the image
  int pixel = img.get(PApplet.parseInt(random(0, width)), PApplet.parseInt(random(0, height)));
  
  // Find the red value of rgb
  int redValue = PApplet.parseInt(red(pixel));
  
  // Find a word match in samples
  singleword = words[redValue].toLowerCase();
 
  // Write the word to word file
  output.println(singleword);
  output.flush(); 
  output.close(); 
  
  // Close program
  exit();
} 
  public void settings() {  size(600, 700); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "convowithpython" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
