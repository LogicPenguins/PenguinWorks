import math

# Low Earth Orbit delta-v requirement in meters per second
DELTA_V_LEO = 9400

# Vacuum specific impulse (Isp) for a Kerosene/LOX engine in seconds
ISP_VAC = 350

# Standard gravity in meters per second squared
G0 = 9.80665

mass_ratio = math.exp(DELTA_V_LEO / (ISP_VAC * G0))
mass_fraction = 1 - 1 / mass_ratio

print(f"Mass ratio required: {mass_ratio:.3f}")
print(f"Propellant mass fraction required: {mass_fraction:.3f}")
