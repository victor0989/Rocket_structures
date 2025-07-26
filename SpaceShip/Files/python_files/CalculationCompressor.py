import math
from utils.constants import cp, R

def slip_factor(C_theta2, U2):
    return 1 - (C_theta2 / U2)

def temp_rise(U1, C_theta1, U2, C_theta2):
    return (U2 * C_theta2 - U1 * C_theta1) / cp

def mass_flow_rate(P01, T01, A, C1):
    rho = P01 / (R * T01)
    return rho * A * C1

def rotational_speed(U1, D1):
    return U1 / (math.pi * D1)
