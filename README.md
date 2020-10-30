# MCOC2020-P3

CONDICIONES DE BORDE NATURALES AL CASO 1-D:

Para obtener la condición de borde natural en el lado izquierdo, se aplico la siguiente condicion de borde:

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;}{\partial&space;x}\left(t,0\right)=&space;5" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\frac{\partial&space;}{\partial&space;x}\left(t,0\right)=&space;5" title="\frac{\partial }{\partial x}\left(t,0\right)= 5" /></a>

Aproximando la condición de borde por medio de sus diferencias finitas de primer orden para el tiempo constante, fijandonos en el puesto 0 y comparandolo con el puesto 1:

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;}{\partial&space;x}\left(t,0\right)\approx&space;\frac{u\left&space;[&space;k,1&space;\right&space;]-u\left&space;[&space;k,0&space;\right&space;]}{dx}=&space;5" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\frac{\partial&space;}{\partial&space;x}\left(t,0\right)\approx&space;\frac{u\left&space;[&space;k,1&space;\right&space;]-u\left&space;[&space;k,0&space;\right&space;]}{dx}=&space;5" title="\frac{\partial }{\partial x}\left(t,0\right)\approx \frac{u\left [ k,1 \right ]-u\left [ k,0 \right ]}{dx}= 5" /></a>

Al reordenar la ecuación:

<a href="https://www.codecogs.com/eqnedit.php?latex=u\left&space;[&space;k,0&space;\right&space;]=&space;-5&space;&plus;&space;u\left&space;[&space;k,1&space;\right&space;]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?u\left&space;[&space;k,0&space;\right&space;]=&space;-5&space;&plus;&space;u\left&space;[&space;k,1&space;\right&space;]" title="u\left [ k,0 \right ]= -5 + u\left [ k,1 \right ]" /></a>

De esta forma obtenemos un nuevo stencil de diferencias finitas (pequeño) que nos permite completar el valor faltante.
