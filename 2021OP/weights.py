from matplotlib import pyplot as plt
import math
import numpy as np

obj1 = []
obj2 = []
lx = []
ly = []

w = 1.5;
slope = -1.0/w;
for i in range(101):
    obj1.append(i/100);
    obj2.append((i/100 - 1.0) ** 2.0 - 0.2 * math.cos(2.0 * math.pi * (i / 100 - 1.0)));
    lx.append(i/100);
    ly.append(0.44 + slope*(i/100));

ptx = 0.92;
pty = 0.44 + slope*ptx;
dx = .05; dy = w*dx+dx;

s1 = []
s2 = []
ran = []
for i in range(101):
    x = i*0.01;
    s1.append((x - 1.0) ** 2.0 - 0.2 * math.cos(2.0 * math.pi * (x - 1.0)));
    s2.append(0.8);
    ran.append(x)

#plt.rcParams["font.family"] = "Times New Roman"
plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
#plt.rcParams["mathtext.default"] = "it"
#plt.title("A nonconvex Pareto front for $p=2$", fontsize=12);
plt.xlabel("objective $f_1$", fontsize=25);
plt.ylabel("objective $f_2$", fontsize=25);
plt.plot(obj1,obj2,'k', linestyle='-')
plt.fill_between(ran, s1, s2,alpha=0.25)
plt.plot(lx,ly,'k')
plt.plot(ptx,pty,'ko')
plt.arrow(ptx+1.3*dx,pty+1.3*dy,-dx,-dy, head_width=0.01)
plt.text(ptx-0.05,pty+0.12,"$w$",fontsize=25)
plt.savefig('weights.eps',format='eps')

