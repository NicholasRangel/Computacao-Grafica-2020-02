

void setup() 
{
  size(500,500);
}

void draw()
{
  background(200);
  int margem = 20;
  float n = round(map(mouseX,0,width,3,20));
  float a2 = TWO_PI/n;
  float a1 = a2/2;
  float r2 = (width/2)-margem;
  float r1 = r2/3;
  translate(width/2,height/2);
  noFill();
  circle(0,0,2*r1);
  circle(0,0,2*r2);
  beginShape();
  
  for(int i=0; i<n; i++)
  {
    
    float x = r2*cos(i*a2);
    float y = r2*sin(i*a2);
    vertex(x,y);
    
    x = r1*cos(i*a2+a1);
    y = r1*sin(i*a2+a1);
    vertex(x,y);
    
  }
  rotate((PI*3)/2);
  fill(0,0,255);
  endShape(CLOSE);
}
