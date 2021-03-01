
from main import ExerciseList, PackedExercise
import matplotlib.pyplot as plt
import random
exercise_decorator = ExerciseList()


@exercise_decorator
def pressure_on_depth_easy():
    depth = random.randint(20, 1e3)
    rho_w = random.randint(1000, 1025)
    text = """Calculate hydrostatic pressure.
Depth : {} m 
Water density: {} kg/m3""".format(depth, rho_w)

    answer = 9.81 * depth * rho_w
    solution = """After ignoring the change in water's density with increased pressure
Pressure can be calculated by following formula: p = g*rho*h
Where:
p - pressure [Pa]
rho - water density [kg/m3]
h - depth [m]
g - earth's acceleration [m/s^2]"""
    return PackedExercise(text=text, answer=answer, solution=solution)

@exercise_decorator
def mass_given_specific_weight():
    s_weight = random.randint(11, 13) * 1000
    volume = random.randint(4, 8) * 100
    gamma = "\u03B3"
    rho = "\u03C1"
    text = """Fluid has specific weight {}kN.
Calculate mass of the fluid in tank with a capacity of {}cm^3.""".format(s_weight/1000, volume)
    answer = volume*1e-6*s_weight/9.81
    solution = """Specific weight is weight per unit volume of a material
Calculated by following formula: {0} = {1} * g
Where:
{1} - m/V [kg/m^3]
g - Earth's acceleration 9.81 [m/s^2]
After rewriting density as mass/volume
{0} = m/V * g
So:
m = {0}*V/g""".format(gamma, rho)
    return PackedExercise(text=text, answer=answer, solution=solution)
