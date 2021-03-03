from PackedExercise import PackedExercise
from ExerciseList import ExerciseList
from greek_letters import greek_letters
import matplotlib.pyplot as plt
import random
exercise_decorator = ExerciseList()


@exercise_decorator
def pressure_on_depth_easy():
    rho_greek = greek_letters["Small"]["Rho"]
    depth = random.randint(20, 1e3)
    rho_w = random.randint(1000, 1025)
    text = """Calculate hydrostatic pressure.
Depth : {} m 
Water density: {}={} kg/m3""".format(depth, rho_greek, rho_w)

    answer = 9.81 * depth * rho_w
    solution = """After ignoring the change in water's density with increased pressure
Pressure can be calculated by following formula: p = g*rho*h
Where:
p - pressure [Pa]
{} - water density [kg/m3]
h - depth [m]
g - earth's acceleration [m/s^2]""".format(rho)
    return PackedExercise(text=text, answer=answer, solution=solution)


@exercise_decorator
def mass_given_specific_weight():
    s_weight = random.randint(11, 13) * 1000
    volume = random.randint(4, 8) * 100
    gamma_greek = greek_letters["Small"]["Gamma"]
    rho_greek = greek_letters["Small"]["Rho"]
    text = """Fluid has specific weight {}={}kN.
Calculate mass of the fluid in tank with a capacity of V={}cm^3.""".format(gamma_greek, s_weight/1000, volume)
    answer = volume*1e-6*s_weight/9.81
    solution = """Specific weight is weight per unit volume of a material
Calculated by following formula: {0} = {1} * g
Where:
{1} - m/V [kg/m^3]
g - Earth's acceleration 9.81 [m/s^2]
After rewriting density as mass/volume
{0} = m/V * g
So:
m = {0}*V/g""".format(gamma_greek, rho_greek)
    return PackedExercise(text=text, answer=answer, solution=solution)


@exercise_decorator
def volume_of_water_leaked_pipeline():
    xi=5e-10
    xi_greek = greek_letters["Small"]["Xi"]
    delta_greek = greek_letters["Capital"]["Delta"]
    pi_greek = greek_letters["Capital"]["Pi"]
    p1 = random.randint(4, 9)
    p_delta = -random.randint(1, 3)
    p2 = p1+p_delta
    D = random.randint(1, 20) / 10
    L = random.randint(1, 4) * 1000
    V = D**2/4*3.1415*L
    answer = xi * V * p_delta*1e6
    text = """During hydraulic test in pipeline with diameter D and length L
manometer showed pressure p1. After some time pressure dropped to p2.
Calculate volume V of water leaked from pipeline.
D={}m
L={:.1e}m
p1={}MPa
p2={}MPa
Compressibility factor {}=5e-10Pa-1""".format(D, L, p1, p2, xi_greek)
    solution = """Compressibility factor during isothermal change of pressure:
{0} = 1/V1 * {1}V/{1}p
To calculate the leak's volume {1}V is needed:
{1}V = {0} * {1}p * V1
Where:
{1}p = p2-p1
V1 = d^2/4 * {2} * L""".format(xi_greek, delta_greek, pi_greek)
    return PackedExercise(text=text, answer=answer, solution=solution)

