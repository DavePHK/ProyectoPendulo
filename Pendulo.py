import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin, pi

#Constantes medidas del montaje real. Constante b por determinar. Todo en unidades de S.I.
m=0.2
l=0.1585
d=0.05
b=0.04
g=9.8

#Pendulo simple
w = np.sqrt(g/l)
t=np.linspace(0,60,1000)

#Condiciones de frontera. V(t=0) = 0. 
#Amplitud inicial (t=0). Simulacion para 3 angulos distintos

A= [pi/4.0,pi/6.0,pi/8.0]
B= [(b/(2.0*m*w))*A[0],(b/(2.0*m*w))*A[1],(b/(2.0*m*w))*A[2]]

#Modelo de pendulo amortiguado por friccion del aire. No incluye aproximacion de sin(theta) = theta
#por lo que este modelo es mas preciso
x=[]
y=[]
theta=[]

for i in range(0,len(A)):

	th=A[i]*np.exp((-b/(2*m))*t)*cos(w*t) + B[i]*np.exp((-b/(2*m))*t)*sin(w*t)

	theta.append(th)
	x.append(l*sin(th))
	y.append(-l*cos(th))


#Graficas X vs t, Y vs t, Y vs X.

a=[45.0,30.0,22.5]
for j in range(0,len(A)):
	
	plt.figure()
	plt.plot(t,x[j])
	plt.ylabel('X(m)')
	plt.xlabel('Tiempo (s)')
	plt.title('Angulo '+str(a[j])+' / Posicion X')
	plt.savefig('GrX'+str(a[j])+'.png')
	
	plt.figure()
	plt.plot(t,y[j])
	plt.ylabel('Y(m)')
	plt.xlabel('Tiempo (s)')
	plt.title('Angulo '+str(a[j])+' / Posicion Y')
	plt.savefig('GrY'+str(a[j])+'.png')

	plt.figure()
	plt.scatter(xnew[j],ynew[j])
	plt.ylabel('Y(m)')
	plt.xlabel('X(m)')
	plt.title('Angulo '+str(a[j])+' / Y vs X')
	plt.savefig('GrXY'+str(a[j])+'.png')






