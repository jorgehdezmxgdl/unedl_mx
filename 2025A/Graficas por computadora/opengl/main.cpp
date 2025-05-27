#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <iostream>
#include <cmath>
#include <time.h>

#define MAX 7
using namespace std;


// Tamaño de la ventana
const int ANCHO = 800;
const int ALTO  = 600;

// Estructura del asteroide
struct Asteroide {
    float x;          // Posición X
    float y;          // Posición Y
    float radio;      // Tamaño
    float velocidad;  // Velocidad de caída
    float angulo;     // Ángulo de rotación
    float velAngular; // Velocidad de rotación
};


Asteroide asteroide[MAX];


void iniciarAsteroide() {
	srand(time(NULL));
	for (int i= 0; i < MAX; i++) {
	    asteroide[i].x = -0.8f;        
        asteroide[i].y =  0.4f -(i * 0.15f);  
        asteroide[i].radio = 0.05f;  
        asteroide[i].velocidad = 0.005f +(i * 0.0012f);  
        asteroide[i].angulo = (float)i * 30.0f;    
        asteroide[i].velAngular = 0.5f + (i * 0.0002f);  
    }
}

void dibujaAsteroide(Asteroide &asteroide) {
	glPushMatrix();
	glTranslatef(asteroide.x, asteroide.y, 0.0f);
	
	glBegin(GL_TRIANGLE_FAN);
	glColor3f(0.6f, 0.4f, 0.2f); //color cafe
	
	int puntosIrregulares = 7;
	for (int i=0; i <= puntosIrregulares; i++) {
		float angulo = 2.0f * M_PI * i / puntosIrregulares;
		float irregularidad = 0.2f * sinf(3.0f * angulo);
		float r = asteroide.radio * (1.0f + irregularidad);
		
		glVertex2f(r * cosf(angulo), r * sinf(angulo));
	}
	
	glEnd();
	glPopMatrix();
}

void mueveAsteroide(Asteroide &asteroide) {
	asteroide.x += asteroide.velocidad * (rand() % 2);
}

int main() {
    // Inicializar GLFW
    if (!glfwInit()) {
        std::cerr << "Error al inicializar GLFW" << std::endl;
        return -1;
    }
    
    // Crear ventana (tamaño doble)
    GLFWwindow* ventana = glfwCreateWindow(ANCHO * 2, ALTO * 2, "Asteroide en movimiento", NULL, NULL);
    if (!ventana) {
        std::cerr << "Error al crear ventana" << std::endl;
        glfwTerminate();
        return -1;
    }
    
    // Configurar la ventana
    glfwMakeContextCurrent(ventana);
    glfwSwapInterval(1); // VSync
    
    // Inicializar GLEW
    if (glewInit() != GLEW_OK) {
        std::cerr << "Error al inicializar GLEW" << std::endl;
        return -1;
    }
    
    iniciarAsteroide();
    
    // Bucle principal
    while (!glfwWindowShouldClose(ventana)) {
        // Limpiar pantalla
        glClearColor(0.0f, 0.0f, 0.1f, 1.0f); 
        glClear(GL_COLOR_BUFFER_BIT);
        
        for (int i = 0; i < MAX; i++) {
        	mueveAsteroide (asteroide[i]);
            dibujaAsteroide(asteroide[i]);    
        }	
        
        // Intercambiar buffers y procesar eventos
        glfwSwapBuffers(ventana);
        glfwPollEvents();
    }
    
    // Limpiar
    glfwDestroyWindow(ventana);
    glfwTerminate();
    
    return 0;
}