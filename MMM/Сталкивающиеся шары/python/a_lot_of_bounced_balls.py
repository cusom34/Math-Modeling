from tkinter import *

import numpy as np

root = Tk()
root.resizable(False, False)

width=1000
height=500
c=Canvas(root, width = width, height = height)
c.pack(fill="both", expand=True)
r=0.1
N=15
x=np.zeros(N)
y=np.zeros(N)
coef=100
rad=r*coef
vx=np.zeros(N)
vy=np.zeros(N)
dt=0.01
x_scr0=10
y_scr0=10
ball=[]

def motion():
   global vx, vy, x, y
   for i in range(N):
       ax=0
       ay=0
       vx[i]+=ax*dt
       vy[i]+=ay*dt
       dx=vx[i]*dt
       dy=vy[i]*dt
       x[i]+=dx
       y[i]+=dy 
       c.move(ball[i], dx*coef, dy*coef)
       
       if x[i]<r or x[i]>width/coef-2*r:
           vx[i]=-vx[i]
           #x-=dx
       if y[i]<r or y[i]>height/coef-2*r:
           vy[i]=-vy[i]
           #y-=dy
       """
       if (x[i]**2+y[i]**2>=(L+r)**2):
           vx[i], vy[i]=-vy[i], -vx[i]
       """
       for j in range(N):
           if j!=i:
               dist=np.sqrt( (x[i]-x[j])**2+(y[i]-y[j])**2 )
               if dist<2.2*r:
                   vx[i], vx[j] = vx[j], vx[i]
                   vy[i], vy[j] = vy[j], vy[i]
   root.after(20, motion)
       

for i in range(N):
    vx[i]=-1+8*np.random.random()
    vy[i]=-1+8*np.random.random()
    x[i]=4*r+(width/coef*np.random.random()-4*r)
    y[i]=4*r+(height/coef*np.random.random()-4*r)
    x_scr=x_scr0+x[i]*coef
    y_scr=y_scr0+y[i]*coef
    ball.append(c.create_oval(x_scr-rad, y_scr-rad, x_scr+rad, y_scr+rad, fill="pink", outline="black"))


motion()
root.mainloop()
