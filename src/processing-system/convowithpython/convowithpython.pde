import java.awt.Color;
import java.util.ArrayList;
PrintWriter output;
PImage img;
String[] words;
String singleword;

void setup() {
  // Set window
  size(600, 700);
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
  color pixel = img.get(int(random(0, width)), int(random(0, height)));
  
  // Find the red value of rgb
  int redValue = int(red(pixel));
  
  // Find a word match in samples
  singleword = words[redValue].toLowerCase();
 
  // Write the word to word file
  output.println(singleword);
  output.flush(); 
  output.close(); 
  
  // Close program
  exit();
} 
