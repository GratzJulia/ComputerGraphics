//VARIAVEL GLOBAL:
float[] cores = new float[30];
int rSol = 50, rTerra = 40, rLua = 20;
int distanciaSolTerra = 100, distanciaTerraLua = 40;
int NIVEL;

float cor() {
  return random(10, 250);
}

int ciclo2s(int max) {
  // CALCULA TEMPO A PARTIR DO CONTADOR DE FRAMES
  return ((frameCount/120)%(max+1));
}

void setup() {
  size(900, 900);
  // INICIALIZACAO DAS CORES FIXAS DE CADA CELULA:
  for(int i=0; i<30; i++) {
    cores[i] = cor();  // ESCOLHA DE UMA COR ALEATORIA
  }
}

void draw() {  
  desenhaGrid();
  translate(150, 150);      // marca o centro da celula 00
  desenhaPoligono(0, 0, 0); //questao1
  translate(300, 0);        // marca o centro da celula 01
  fractal();                //questao2
  translate(300, 0);        // marca o centro da celula 02
  sol_terra_lua();          //questao3
  translate(-600, 300);     // marca o centro da celula 10
  rastro_lua();             //questao4
  translate(300, 0);        // marca o centro da celula 11
  rastro_lua2();            //questao5
  translate(0, 300);        // marca o centro da celula 12
  desenhaArcoIris();        //questão8
}

void desenhaArcoIris() {
  translate(0,70);
  float maiorArc = 250;
  
  fill(0,0,255);
  arc(0, 0, maiorArc, maiorArc, PI, TWO_PI);
  
  fill(0,255,0);
  scale(0.8);
  arc(0, 0, maiorArc, maiorArc, PI, TWO_PI);
  
  fill(197, 57, 253);
  scale(0.8);
  arc(0, 0, maiorArc,maiorArc, PI, TWO_PI);
  
  fill(255,0,0);
  scale(0.8);
  arc(0, 0, maiorArc, maiorArc, PI, TWO_PI);
  
  fill(255,117,24);
  scale(0.8);
  arc(0, 0, maiorArc, maiorArc, PI, TWO_PI);
  
  fill(255,255,0);
  scale(0.7);
  arc(0, 0, maiorArc, maiorArc, 0, TWO_PI);
}

void fractal() {
  desenhaPoligono(0, 0, 4); // triangulo equilatero base
  NIVEL = ciclo2s(6);
  //NIVEL = round(map(frameCount/3, 0, 120, 1, 6));
  //if(NIVEL >= 7) {
  //  NIVEL = 1;
  //  frameCount = 0;
  //}
  
  KochCurve(120, 0, -60, -103, NIVEL);
  KochCurve(-60, -103, -60, 103, NIVEL);
  KochCurve(-60, 103, 120, 0, NIVEL);
}

void desenhaGrid() {  
  int corSelecionada = 0;
  //pto inicial = (0,0)
  for (int i=0; i<3; i++) {
    for (int j=0; j<3; j++) {
      if(i==0 && j==1) {
        noFill();
      }else {
        fill(cores[corSelecionada], cores[corSelecionada+1], cores[corSelecionada+2]);      
      }
      rect(0 + i*width/3, 0 + j*height/3, width/3, height/3);
      corSelecionada += 3;
    }
  }
  fill(cores[27], cores[28], cores[29]);
}

void desenhaPoligono(int centroX, int centroY, int lados) {
  float n;
  if(lados > 0) {
    noFill();
    n = 3;
  }else {
   // n = round(map(9 * frameCount%120, 0, 120*9, 3, 12)); 
   n = ciclo2s(12-3) +3;
  }
  float a = -TWO_PI/n;
  int r = round(0.4 * width/3);
  translate(centroX, centroY);
  beginShape();
  for (int i=0; i<n; i++) {
      float x = r*cos(i*a);
      float y = r*sin(i*a);
      vertex(x, y);
  }
  endShape(CLOSE);
}

void desenhaSol(boolean flag, int centroSolX, int centroSolY, int raioSol, int raioTerra, int raioLua, int distTerraLua, float angTerra, float angLua) {
  pushMatrix();
  translate(centroSolX, centroSolY);
  fill(255,255,0);
  if(flag) {
      circle(0,0,raioSol);
  }
  desenhaTerra(flag, raioTerra, raioLua, distTerraLua, angTerra, angLua);
  popMatrix();
}

void desenhaTerra(boolean flag, int raioTerra, int raioLua, int distTerraLua, float angTerra, float angLua) {
  pushMatrix();
 //anguloTerra = angTerra;
  rotate(angTerra);
  translate(distanciaSolTerra, 0);
  fill(0,0,255);
  if(flag) {
    circle(0,0,raioTerra);
  }
  desenhaLua(flag, raioLua, distTerraLua, angTerra, angLua);
  popMatrix();
}

void desenhaLua(boolean flag, int raioLua, int distTerraLua, float angTerra, float angLua) {
  pushMatrix();
  rotate(angLua-angTerra);
  translate(distTerraLua, 0);
  if(flag) {
    fill(180);
  }else {
    fill(10);
  }
  circle(0,0,raioLua);
  popMatrix();
}

void sol_terra_lua() {  
  float anguloTerra = frameCount*PI/300; //10 segundos
  float anguloLua = frameCount*PI/50;    //5 segundos
  desenhaSol(true, 0, 0, rSol, rTerra, rLua, distanciaTerraLua, anguloTerra, anguloLua);
}

void rastro_lua() {
  float anguloTerra = frameCount*PI/300;
  float anguloLua = frameCount*PI/50;
  desenhaSol(false, 0, 0, rSol, rTerra, rLua-14, distanciaTerraLua, anguloTerra, anguloLua);
}

void rastro_lua2() {
  float anguloTerra = frameCount*PI/210;  //7 segundos
  float anguloLua = frameCount*PI/10;     //0.3 segundos
  desenhaSol(true, 0, 0, rSol+90, rTerra-25, rLua-15, distanciaTerraLua-25, anguloTerra, anguloLua);
}

void KochCurve(float pto1_x, float pto1_y, float pto2_x, float pto2_y, int nivel) {
  if(nivel == 0) {
      line(pto1_x, pto1_y, pto2_x, pto2_y);
      return;
  }
  
  float pto3_x, pto3_y,  pto4_x,  pto4_y, pto5_x, pto5_y;
  
  pto3_x = (pto2_x - pto1_x)/3 +pto1_x;
  pto3_y = (pto2_y - pto1_y)/3 +pto1_y;
  
  pto4_x = (pto2_x - pto1_x)*2/3 +pto1_x;
  pto4_y = (pto2_y - pto1_y)*2/3 +pto1_y;
  
  pto5_x = (pto4_x - pto3_x)*cos(PI/3) - (pto4_y - pto3_y) * sin(PI/3) + pto3_x;
  pto5_y = (pto4_y - pto3_y)*cos(PI/3) + (pto4_x - pto3_x) * sin(PI/3) + pto3_y;
  
  KochCurve(pto1_x, pto1_y, pto3_x, pto3_y, nivel-1);
  KochCurve(pto3_x, pto3_y, pto5_x, pto5_y, nivel-1);
  KochCurve(pto5_x, pto5_y, pto4_x, pto4_y, nivel-1);
  KochCurve(pto4_x, pto4_y, pto2_x, pto2_y, nivel-1);
}
