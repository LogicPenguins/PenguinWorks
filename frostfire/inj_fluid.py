import numpy as np
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

# inputs
cd = 0.7
mdot_ox = Q_(0.107, 'kg/s').magnitude
density_ox = Q_(805, 'kg/m^3').magnitude
dp_ox = Q_(1379000, 'pascal').magnitude
orifice_count = 40
mdot_fuel = Q_(0.0533, 'kg/s').magnitude
density_fuel = Q_(789, 'kg/m^3').magnitude
dp_fuel = Q_(1172000, 'pascal').magnitude
diam_post = Q_(0.00566, 'meter').magnitude

# outputs 
total_ox_flow_area = mdot_ox/(cd*np.sqrt(2*density_ox*dp_ox))
single_ox_orifice_area = total_ox_flow_area/orifice_count
single_ox_orifice_diameter = np.sqrt((4*single_ox_orifice_area)/np.pi)
fuel_annulus_gap = mdot_fuel/(cd*np.pi*diam_post*np.sqrt(2*density_fuel*dp_fuel))

print(f'Single ox orifice diam (mm): {single_ox_orifice_diameter*1000}')
print(f'Fuel annulus gap (mm): {fuel_annulus_gap*1000}')