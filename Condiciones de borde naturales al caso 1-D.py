from matplotlib.pylab import *
from numpy import *

L = 1.
n = 100     # Discretización
dx = L/n

x = linspace(0, L, n+1)

# Arreglo solución
dt = 2.
Nt = 50000
u = zeros((Nt,n+1))

# Condiciones de borde
u[:,0] = 0.     # Izq. u(t,0)
u[:,-1] = 20.    # Der. u(t,L)

# Cond. inicial
u[0, 1:n] = 20. # u(0,x)

k = 79.5    # m^2 / s
c = 450.    # J / kg C
ρ = 7800.   # kg / m^3
α = k *dt / (c*ρ*dx**2)

for k in range(Nt-1) :
    t = dt * k
    print(f"k= {k} t = {t}")
    #u[k,n] = 10 *dx + u[k,n-1] # Der du/dx(t,L)
    u[k,0] = -5 *dx + u[k,1]
    for i in range(1, n):
        u[k+1, i] = u[k,i] + α * (u[k, i+1] - 2*u[k,i] + u[k,i-1])

    if k % 1000 == 0 :
        plot(x,u[k,:])

title("k = {}  t = {} s".format(k, k*dt))

show()
