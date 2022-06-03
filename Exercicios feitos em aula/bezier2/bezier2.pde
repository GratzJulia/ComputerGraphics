ArrayList<PVector> pontos = new ArrayList<PVector>();
PVector pontoSelecionado = null;

void setup()
{
  size(800,600);
}

void ajustaSelecionado() {
  if(pontoSelecionado != null) {
    pontoSelecionado.x = mouseX;
    pontoSelecionado.y = mouseY;
  }
}

void desenhaPontos() {
  for(int i=0; i<pontos.size(); i++) {
    PVector p = pontos.get(i);
    if(p == pontoSelecionado) {
      fill(255,0,0);
    } 
    else {
      fill(0,0,0);
    }
    circle(p.x,p.y,10);
  }  
}

void bezierG2()
{
  if(pontos.size() != 3) {
    return;
  }
  float p1x = pontos.get(0).x;
  float p1y = pontos.get(0).y;
  float p2x = pontos.get(1).x;
  float p2y = pontos.get(1).y;
  float p3x = pontos.get(2).x;
  float p3y = pontos.get(2).y;
  beginShape();
  vertex(p1x, p1y);
  for(float t = 0; t <= 1; t += 0.01)
  {
    float ax = p1x + t*(p2x-p1x);
    float bx = p2x + t*(p3x-p2x);
    float cx = ax + t*(bx-ax);
    float ay = p1y + t*(p2y-p1y);
    float by = p2y + t*(p3y-p2y);
    float cy = ay + t*(by-ay);
    vertex(cx,cy);  
  }
  vertex(p3x, p3y);
  endShape(CLOSE);
}

void draw() {
  background(200);
  fill(255,255,255);
  ajustaSelecionado();
  bezierG2();
  desenhaPontos();
}

void mouseReleased() {
  pontoSelecionado = null;
}

void mousePressed() {
  
  PVector p = new PVector(mouseX, mouseY);
  
  for(int i=0; i<pontos.size(); i++) {
    PVector p2 = pontos.get(i);
    if(p.dist(p2) < 10) {
      pontoSelecionado = p2;
      return;
    }
  }
  if(pontos.size() < 3) {
    pontoSelecionado = p;
    pontos.add(p);
  }
}
