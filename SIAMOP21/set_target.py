from matplotlib import pyplot as plt
import math
import numpy as np

obj1 = []
obj2 = []

w = 1.5;
slope = -1.0/w;
for i in range(101):
    obj1.append(i/100);
    obj2.append((i/100 - 1.0) ** 2.0 - 0.2 * math.cos(2.0 * math.pi * (i / 100 - 1.0)));

ptx = 0.45;
pty = 0.75;
dx = 0.0; dy = -0.2;

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
plt.fill_between(ran, s1, s2,alpha=0.1)
plt.axvline(x=0.5, color='k', linestyle='--')
plt.plot(0.5,0.45,'ko')
plt.arrow(ptx,pty,dx,dy, head_width=0.01)
plt.arrow(ptx+dx,pty+dy,0.5*(0.5-ptx-dx),0.5*(0.45-pty-dy), head_width=0.01)
plt.text(ptx-0.07,pty-0.05,"$w$",fontsize=25)
plt.savefig('set_target.eps',format='eps')

