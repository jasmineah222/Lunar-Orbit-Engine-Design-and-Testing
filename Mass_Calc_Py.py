import math
from scipy.optimize import fsolve
import numpy as np 
import pandas as pd


Ce=3270.40 # Effective Exhuast Velocity from CEA Code
go=9.81 #m/s^2
deltaV= 900 #m/s, total for TLI and LOI

mp_solutions = []   
init_guess=[1000]

def find_propellant_mass(vars):
    isp=Ce/go
    mp=vars[0]
    eqn= (mp + .10 * mp + 3000)/(0.10 * mp + 3000)-math.exp(deltaV/Ce)
    return [eqn]

sol=fsolve(find_propellant_mass,init_guess)
mp_solutions.append(sol[0])

isp=[]
ispCe=Ce/go
isp.append(ispCe)

mf=800+3000 # structural mass
mo_solutions = []   
init_guess=[4000]
def find_init_mass(vars):
    mo=vars[0]
    eqn= (mo/mf) - math.exp(deltaV/(Ce))
    return [eqn]
sol=fsolve(find_init_mass,init_guess)
mo_solutions.append(sol[0])

count=0
propmassfrac=[]
for mass in mp_solutions:
    a=mass/mo_solutions[count]
    count+= 1
    propmassfrac.append(a)

propmass = np.vectorize(float)(propmassfrac)


print(f"\nPropellant Masses: {np.vectorize(float)(mp_solutions[0])} kg")
print(f"\nInitial Masses: {np.vectorize(float)(mo_solutions[0])} kg")
print(f"\nEffective Exhaust Velocity: {Ce} m/s")
print(f"\nSpecific Impulse: {np.vectorize(float)(isp[0])} s")
print(f"\nPropellant Mass Fractions: {np.vectorize(float)(propmass[0]*100)} %")

