# --------------------------------------------
# BOILING POINT AND PRESSURE RELATIONSHIP SUMMARY
#
# - Every fluid has a saturation pressure linked to its temperature.
# - At a given temperature, if the system pressure is:
#     - ≥ Saturation Pressure → Fluid stays liquid (no boiling).
#     - < Saturation Pressure → Fluid boils to try to reach equilibrium.
# - To find the maximum temperature before boiling at a given pressure,
#   solve for T in Antoine's equation using the system pressure as P_sat.
# - This gives the highest allowable fluid temperature before boiling starts.
# - Beyond that temp, it will begin to boil unless pressure increases.
# --------------------------------------------

import numpy as np
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


T_1 = Q_(351.55, 'kelvin').magnitude
P_1 = Q_(101325, 'pascal').magnitude
P_2 = Q_(3790000, 'pascal').magnitude
heat_vap = Q_(38560, 'J/mol*K').magnitude
R = Q_(8.314, 'J/mol*K').magnitude

boiling_temp = 1/((1/T_1)-((R*np.log(P_2/P_1))/heat_vap))
print(f'{boiling_temp} K')