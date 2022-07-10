import matplotlib.pyplot
from matplotlib.pyplot import *
import numpy
from numpy import arange

#EJERCICIO 1

figure()
x = arange(-10,10,1)
y = arange(-10,10,1)
y1 = 5-2*x
#Crea los valores de x y y, además de las ecuaciones.

xlim(-10,10)
ylim(-10,10)
hlines(0,-10,10,color='k')
vlines(0,-10,10,color='k')
grid(True)
#Establece límites de x,y dentro de la gráfica, además, permite mostrar gráfica como cuadricula.

xlabel('Eje X')
ylabel('Eje Y')
#Establece el nombre de los ejes dentro de la gráfica.

plot(x,y1,color='b')
#Pone la ecuación dentro de la gráfica

title('Ejercicio 1')
legend(['2x+y<5'])
#Añade el título y la leyenda

x = [-99.9, -2.5, 0.0, 2.5, 7.5, -99.9]
y = [99.9, 10.0, 5.0, 0.0, -10.0, -99.9]
#Establece los puntos de intercepción de la ecuación con los ejes.

fill(x,y,'r')
show()
#Rellena el área de solución con rojo y muestra la gráfica.

#Lo mismo aplica para el resto de los ejecicios.

#EJERCICIO 2

figure()
x = arange(-20,20,1)
y = arange(-20,20,1)
y1 = 5+(0*x)

xlim(-10,10)
ylim(-10,10)
hlines(0,-10,10,color='k')
vlines(0,-10,10,color='k')
grid(True)

xlabel('Eje X')
ylabel('Eje Y')

plot(x,y1,color='b')

title('Ejercicio 2')
legend(['y<=5'])

x = [-10.0, -10.0, 0.0, 10.0, 10.0]
y = [-99.0, 5.0, 5.0, 5.0, -99.0]

fill(x,y,'r')
show()

#EJERCICIO 3

figure()
x = arange(-10,10,1)
y = arange(-10,10,1)
y1 = (x+2)/2

xlim(-5,5)
ylim(-5,5)
hlines(0,-5,5,color='k')
vlines(0,-5,5,color='k')
grid(True)

xlabel('Eje X')
ylabel('Eje Y')

plot(x,y1,color='b')

title('Ejercicio 3')
legend(['2(2x-y)<2(x+y)-4'])

x = [-2, -5.0, -2.0, 0.0, 5.0, 2]
y = [399.9, -1.5, 0.0, 1.0, 3.5, 399.9]

fill(x,y,'r')
show()

# EJERCICIO 4

figure()
x = arange(-5,5,1)
y = arange(-5,5,1)
y1 = 3-2*x
y2 = 1/2+(x*0)
y3 = 1*x

xlim(-3,3)
ylim(-3,3)
hlines(0,-3,3,color='k')
vlines(0,-3,3,color='k')
grid(True)

xlabel('Eje X')
ylabel('Eje Y')

plot(x,y1,color='b')
plot(x,y2,color='r')
plot(x,y3,color='m')

title('Ejercicio 4')
legend(['2x+y>3', '2y-1>0', 'x>=y'])

x = [3.0, 1.0, 1.25, 3.0]
y = [3.0, 1.0, 0.5, 0.5]

fill(x,y,'r')
show()

# EJERCICIO 5

figure()
x = arange(-40,40,1)
y = arange(-40,40,1)
y1 = (60-2*x)/3
y2 = x*0
x1 = y*0

xlim(-40,40)
ylim(-40,40)
hlines(0,-40,40,color='k')
vlines(0,-40,40,color='k')
grid(True)

xlabel('Eje X')
ylabel('Eje Y')

plot(x,y1,color='b')
plot(x,y2,color='r')
plot(x1,y,color='m')

title('Ejercicio 5')
legend(['2x+3y<=60', 'y>=0', 'x>=0'])

x = [0.0, 0.0, 30.0]
y = [0.0, 20.0, 0.0]

fill(x,y,'r')
show()

# EJERCICIO 6

figure()
x = arange(-300,300,1)
y = arange(-300,300,1)
y1 = 180-2*x
y2 = (160-x)/2
y3 = 100-x

xlim(-200,200)
ylim(-200,200)
hlines(0,-200,200,color='k')
vlines(0,-200,200,color='k')
grid(True)

xlabel('Eje X')
ylabel('Eje Y')

plot(x,y1,color='b')
plot(x,y2,color='r')
plot(x,y3,color='m')

title('Ejercicio 6 (MAX 520 en P(40,60))')
legend(['2x+y<=180','x+2y<=160','x+y<=100'])

x = [0.0, 0.0, 40.0, 80.0, 90.0]
y = [0.0, 80.0, 60.0, 20.0, 0.0]

fill(x,y,'r')
show()

# EJERCICIO 7

figure()
x = arange(-50,50,1)
y = arange(-50,50,1)
y1 = (105-5*x)/3
y2 = (70-2*x)/4

xlim(-50,50)
ylim(-50,50)
hlines(0,-50,50,color='k')
vlines(0,-50,50,color='k')
grid(True)

xlabel('Eje X')
ylabel('Eje Y')

plot(x,y1,color='b')
plot(x,y2,color='r')

title('Ejercicio 7 (MAX 4200 en P(21,0))')
legend(['5x+3y<=105','2x+4y<=70'])

x = [0.0, 0.0, 15.0, 21.0]
y = [0.0, 17.5, 10.0, 0.0]

fill(x,y,'r')
show()

# EJERCICIO 8

figure()
x = arange(-50,50,1)
y = arange(-50,50,1)
y1 = (100-3*x)/2
y2 = 50-x

xlim(-50,50)
ylim(-50,50)
hlines(0,-50,50,color='k')
vlines(0,-50,50,color='k')
grid(True)

xlabel('Eje X')
ylabel('Eje Y')

plot(x,y1,color='b')
plot(x,y2,color='r')

title('Ejercicio 8 (MIN -150 en P(0,50))')
legend(['3x+2y<=100','x+y<=50'])

x = [0.0, 0.0, 33.3]
y = [0.0, 50.0, 0.0]

fill(x,y,'r')
show()

# EJERCICIO 9

figure()
x = arange(-100,100,1)
y = arange(-100,100,1)
y1 = 120-2*x
y2 = (500-5*x)/7

xlim(-100,100)
ylim(-100,100)
hlines(0,-100,100,color='k')
vlines(0,-100,100,color='k')
grid(True)

xlabel('Eje X')
ylabel('Eje Y')

plot(x,y1,color='b')
plot(x,y2,color='r')

title('Ejercicio 9 (MAX 291 en P(37.7,44.4))')
legend(['2x+y<=120','5x+7y<=500'])

x = [0.0, 0.0, 37.77, 60.0]
y = [0.0, 71.43, 44.44, 0.0]

fill(x,y,'r')
show()