#include <iostream>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

void menu();
void escalagrises();

int main(int argc, char** argv) {
	menu();
}

void menu() {
	int opcion;	
	do {
		cout << "Menu de opciones" << endl;
		cout << "1. Imagen a escala de grises" << endl;
		cout << "2. Dibujar lineas usando bresenhamLine" << endl;
		cin  >> opcion;
		switch(opcion) {
			case 1:
				break;
			case 2:
			   break;	
   } while (opcion != 3);
}

void escalagrises() {
	string mi_imagen = "C:\\Users\\JorgeFausto\\Downloads\\no-image.png";
	
	Mat imagenColor = imread(mi_imagen, IMREAD_COLOR);
	if (imagenColor.empty()) {
		cout << "Error al procesar la imagen"  << endl;
		return -1;
	}
	cout << "Informacion de la imagen" << endl;
	cout << "Dimensiones: (" << imagenColor.rows << "," << imagenColor.cols << ")" << endl;
	cout << "Tamaño total: " << imagenColor.total() << endl;
	cout << "Informacion detalle del vector de la imagen" << endl;
	
	for (int i = 0; i < imagenColor.rows; i++) {
		for (int j = 0; j < imagenColor.cols; j++) {
			cout << imagenColor.at(i,j) << "\t";
		}
		cout << endl;
	}
}
