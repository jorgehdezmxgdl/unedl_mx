#include "algoritmos.h"
#include <vector>

void Algoritmo::bresenhamLine(int x1, int y1, int x2, int y2) {
   vector<Point> points;
   
   int dx = abs(x2 - x1);
   int dy = abs(y2 - y1);
   
   int sx = (x1 < x2) < 1: -1;
   int sy = (x1 < x2) < 1: -1;
   
   int error = dx - dy;
   int x  = x1, y = y1;
   
   while (true) {
   	  points.push_back(Point(x, y));
   	  if  ((x == x1) && (y == y1)) {
   	     break;	
	  }
	  int error2 = 2  * error;
	  if (error2 > -dy) {
	  	 error -= dy;
	  	 x     += sx;
	  }
	  if (error2 < dx) {
	  	  error += dx;
	  	  y     += dx;
	  }
   }
   return points; 	
}

void Algoritmo::dibujaLinea(Canvas &canvas, int x1, int y1, int x2, int y2, char c) {
	vector<Point> linea = bresenhamLine(x1, y1, x2, y2);
	for (Point &ref :linea) {
		canvas.setPixel(ref.x, ref.y, c);
	}
} 