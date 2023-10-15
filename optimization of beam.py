from gekko import Gekko
from numpy import pi
m=Gekko(remote=False)
px=10  #Transverse load(lb)
py=25   #Axial Load(Lb)
Ln=50   #Beam length
rho=0.3   #Material density(lb/m^3)
sy=3000   #yield stress
E=306  #youngs's modulus
b=m.Var(lb=0.5)     # Beam width (in)
d=m.Var(lb=1e-3)     # Beam Depth (in)
weight=m.Var(lb=1e-3) # Beam  Weight(lb)
MOFI=b*d**3/12
x_stress=m.Var(ub=sy)
y_stress=m.Var(ub=sy)

py_ab=m.Intermediate(pi**2*E*MOFI/(4*Ln**2))
m.Equations([
    weight == b*d*Ln*rho,
    y_stress*(b*d)==py,
    x_stress*(2*MOFI)==px*Ln*d,
    py_ab>= py,
    b<= 2*d
])
m.Minimize(weight)
m.options.SOLVER= 2
m.solve()
print('weight:' +str(weight[0]))
print('depth:' +str(d[0]))
print('width:' +str(b[0]))
print('vertical stress :' + str(x_stress[0]))
print('horizontal stress :' + str(y_stress[0]))
print('Axial Buckling Load :' + str(x_stress[0]))

