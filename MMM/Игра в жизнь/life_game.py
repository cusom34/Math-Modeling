import numpy as np
import tkinter as tk

root=tk.Tk()
c=tk.Canvas(root, width=600, height = 600, bg='pink')
c.pack()
x_scr0=10
y_scr0=10
box=5
N=100
mas=np.zeros([N, N], dtype=int)
newmas=np.zeros([N, N], dtype=int)
p=0.3

for i in range(N):
    for j in range(N):
        r=np.random.random()
        if(r<p):
            mas[i][j]=8
            newmas[i][j]=8
            
rect=[]
for i in range(N):
    for j in range(N):
        if mas[i][j]==8: col="black"
        else: col='pink'
        rect.append(c.create_rectangle(x_scr0+i*box, y_scr0+j*box, x_scr0+(i+1)*box, y_scr0+(j+1)*box, fill=col, outline = 'white'))
        
def motion():
    for i in range(N):
        for j in range(N):
            if i==0: l=N-1
            else: l=i-1
            if i==N-1: r=0
            else: r=i+1
            if j==0: u=N-1
            else: u=j-1
            if j==N-1:b=0
            else: b=j+1
            sum=mas[l][b]//8+mas[l][j]//8+mas[l][u]//8+ \
                mas[i][b]//8+            +mas[i][u]//8+ \
                mas[r][b]//8+mas[r][j]//8+mas[r][u]//8
            if sum==2 or sum==3: newmas[i][j]=mas[i][j]
            elif sum==2: newmas[i][j]=8
            else: newmas[i][j]=0
    
    for i in range(N):
        for j in range(N):
            if mas[i][j]>0:
                mas[i][j]-=1
            mas[i][j]=newmas[i][j]
            if mas[i][j]==8: c.itemconfig(rect[i*N+j], fill='black' )
            else:c.itemconfig(rect[i*N+j], fill='pink')
    
    root.after(10, motion)
motion()       
root.mainloop()