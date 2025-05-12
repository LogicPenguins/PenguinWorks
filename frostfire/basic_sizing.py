import numpy as np
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

# Inputs
thrust = Q_(300, 'newton')
OF = 2
p_c = Q_(1723689, 'pascal')
p_e = Q_(101325, 'pascal')
t_c = Q_(1900, 'kelvin')
gamma_c = 1.2757
gamma_t = 1.2809
gamma_e = 1.2424
R_c = Q_(426.73, 'J/(kg*K)') # R = specific gas constant
R_t = Q_(426.71, 'J/(kg*K)')
R_e = Q_(425.27, 'J/(kg*K)')
l_star = Q_(0.381, 'meter') 
c_r = 5                      # c_r = contraction ratio

# Calcs
p_t = ((2/(gamma_t+1))**(gamma_t/(gamma_t-1))) * p_c
print(f'Throat Pressure: {p_t} pascal')
t_t = t_c/((p_c/p_t)**((gamma_t-1)/gamma_t))
v_e = np.sqrt(
    (2 * gamma_e / (gamma_e - 1)) * R_e * t_c *
    (1 - (p_e / p_c) ** ((gamma_e - 1) / gamma_e))
)
v_t = np.sqrt(
    (2*gamma_t) / (gamma_t - 1) * R_t * t_c * 
    (1- (p_t / p_c)**((gamma_t - 1) / gamma_t))
)
SV_i = (R_c*t_c)/p_c
SV_t = (SV_i*((gamma_t+1)/2)**(1/(gamma_t-1)))
SV_e = (SV_i*(p_c/p_e)**(1/gamma_e))
mdot = thrust/v_e
print(f'mdot: {mdot.magnitude} kg/s')
a_t = (mdot*SV_t)/v_t
d_t = np.sqrt((a_t/np.pi))*2
a_e = (mdot*SV_e)/v_e
d_e = np.sqrt(a_e/np.pi)*2
V_c = a_t*l_star
a_c = c_r*a_t
l_c = V_c/a_c
d_c = np.sqrt(a_c/np.pi)*2

# Results
print(f"""
Chamber Diameter: {d_c.to("meter")} 
Throat Diameter: {d_t.to("meter")}
Exit Diameter: {d_e.to("meter")}
Chamber Length: {l_c.to("meter")}
      
      """)

