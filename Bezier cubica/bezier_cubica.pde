
float p0x = 100;
float p0y = 100;
float p1x = 100;
float p1y = 300;
float p2x = 700;
float p2y = 300;
float p3x = 700;
float p3y = 100;
boolean arrastandoP1 = false;
boolean arrastandoP2 = false;

void setup()
{
  size(800,600);
}

void draw()
{
  background(128);
  
  if(arrastandoP1)
  {
    p1x = mouseX;
    p1y = mouseY;
  }
  if(arrastandoP2)
  {
    p2x = mouseX;
    p2y = mouseY;
  }
  pontos(p0x,p0y);
  pontos(p1x,p1y);
  pontos(p2x,p2y);
  pontos(p3x,p3y);
  
  beginShape();
  vertex(p0x,p0y);
  vertex(p1x, p1y);
  for(float t = 0; t <= 1; t += 0.01)
  {
    float ax = p1x + t*(p2x-p1x);
    float bx = p2x + t*(p3x-p2x);
    float dx = p0x + t*(p1x-p0x);
    float cx = ax + t*(bx-ax);
    float ex = dx + t*(ax-dx);
    float fx = ex + t*(cx-ex);
    
    float ay = p1y + t*(p2y-p1y);
    float by = p2y + t*(p3y-p2y);
    float dy = p0y + t*(p1y-p0y);
    float cy = ay + t*(by-ay);
    float ey = dy + t*(ay-dy);
    float fy = ey + t*(cy-ey);
    vertex(fx,fy);
  }
  vertex(p2x,p2y);
  vertex(p3x, p3y);
  
  endShape(CLOSE);
}
void pontos(float px,float py)
{
  circle(px,py,10);
}

void mousePressed()
{
  if(dist(p1x,p1y,mouseX,mouseY)<10)
  {
    arrastandoP1 = true;
  }
  if(dist(p2x,p2y,mouseX,mouseY)<10)
  {
    arrastandoP2 = true;
  }
}
void mouseReleased()
{
  arrastandoP1 = false;
  arrastandoP2 = false;
}
