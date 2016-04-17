import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt
import matplotlib as mp

def odeFunc(y, t, a,b):
    y0, y1=y
    ode_eqn=[a*(y0-y0*y1), b*(-y1 + y0*y1)]
    return ode_eqn
    
def solve(a,b,t,init_cond,name):
    mp.rcParams['font.size'] = 14
    sols = si.odeint(odeFunc, init_cond, t, args=(a, b)) #solve the ode
    
    #plot y0 and y1 against t
    fig = plt.figure(1)
    plt.plot(t, sols[:, 0], 'r', label='y0(t)')
    plt.plot(t, sols[:, 1], 'b', label='y1(t)')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend(loc='best')
    fig.set_size_inches(10, 10)
    plt.grid()
    temp='{}{} {}{}'.format('Plot of y against t with initial condition of y0=',init_cond[0],'and y1=', init_cond[1])
    plt.title(temp)
    plt.show()
    figName='{}{}'.format(name,'_init1.jpg')
    fig.savefig(figName, dpi=600) #save the plot
    
    #plot y1 against y0
    fig=plt.figure(2)
    plt.plot(sols[:,0],sols[:,1],'g')
    plt.xlabel('y0')
    plt.ylabel('y1')
    fig.set_size_inches(10, 10)
    plt.grid()
    temp='{}{} {}{}'.format('Plot of y1 against y0 with initial condition of y0=',init_cond[0],'and y1=', init_cond[1])
    plt.title(temp)
    plt.show()
    figName='{}{}'.format(name,'_init2.jpg')
    fig.savefig(figName, dpi=600) #save the plot
   
    
if __name__ == "__main__":
    
    a=1.0
    b=0.2
    t=np.linspace(0,5,101)
    mp.rcParams['font.size'] = 16
    
    #part1
    init_cond1=[0.1,1.0]
    solve(a,b,t, init_cond1,'first')
    
    #part2
    init_cond2=[0.11,1.0]
    solve(a,b,t, init_cond2,'second')