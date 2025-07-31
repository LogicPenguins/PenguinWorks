import math

DELTA_V_LEO = 9400
ISP_VAC = 350
G0 = 9.80665

mass_ratio = math.exp(DELTA_V_LEO / (ISP_VAC * G0))
mass_fraction = 1 - 1 / mass_ratio

print(f"Mass ratio required: {mass_ratio:.3f}")
print(f"Propellant mass fraction required: {mass_fraction:.3f}")
