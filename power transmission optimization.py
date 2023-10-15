from gekko import Gekko
from numpy import pi
m=Gekko()
#
# Constraints
pi=3.14
a=1.67
p=168.5
u=0.8
s=75000
t=0.0092

w=m.Var(lb=0.01 ,ub=0.5)
d=[m.Var(lb=1/5) for i in range(5)]
N_O=[950,650,450,250,150]
N_in=350

weight=m.Var()

#intermediates
#diameter of the ith step of the input pulley

d_in=[m.Intermediate(d[i]*(N_O[i]/N_in)) for i in range (5)]

inter=[m.Intermediate(d[i]**2 +d_in[i]**2 ) for i in range(5)]
# belt length
c=[m.Intermediate((pi*d[i]/2*(1+N_O/N_in) \
  + (((N_O[i]/N_in))-1)**2)*d[i]**2 /(4*a)+2*a) for i in range (5)]
o=[m.Intermediate(pi-2*m.asin(((N_O[i]/N_in))))]

T1=[m.Intermediate(s*t*w) for i in range (5)]
t2=[m.Intermediate(T1[i]/(m.exp(u*o[i]))) for  i in range(5)]

#equation
m.Equation(weight==p*w*(pi/4)*sum[0:5])))
# constraints

belt_length=[m.Equation(c[0]- c[i+1]==0) for i in range (4)]
tension_ratio=[m.Equation(m.exp(u*o[i])>-2) for i in range(5)]
power_transmitted=[m.Equation(((T1[i]-t2[i])*pi*d_in[i]*350)/33000 \
                               >=0.65) for i in range(5)]
m.Minimize(weight)
m.options.IMODE=3
m.options.SOLVER=1
m.solve()

print('optimal solution'+str(weight[0]))
print('optimal  diameter' +str(d))
print('optimal width:'+str(w[0]))





