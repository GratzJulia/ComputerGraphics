ArrayList<PVector> pontos = new ArrayList<PVector>();
PVector pontoSelecionado = null;

void setup() {
  size(600,600);
}

void draw() {
  background(200);
  if(pontoSelecionado != null) {
    pontoSelecionado.x = mouseX;
    pontoSelecionado.y = mouseY;
  }
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
  pontoSelecionado = p;
  pontos.add(p);
}
