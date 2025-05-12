import numpy as np
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

# ---------- dynamic thermal stress ----------
# inputs
chamber_diameter = Q_(0.0283, 'meter').magnitude
throat_diameter = Q_(0.01266, 'meter').magnitude

cooling_inner_wall_thickness = Q_(0.0006, 'meter').magnitude
tensile_yield_6061_chamber = Q_(75000000, 'pascal').magnitude # Chamber sees ~500K
tensile_yield_6061_throat = Q_(13000000, 'pascal').magnitude # Throat sees ~630K

chamber_working_pressure = Q_(1378952, 'pascal').magnitude
throat_working_pressure = Q_(946655, 'pascal').magnitude

# outputs
chamber_inner_wall_hoop_stress = (chamber_working_pressure*chamber_diameter)/(2*cooling_inner_wall_thickness)
throat_inner_wall_hoop_stress = (throat_working_pressure*throat_diameter)/(2*cooling_inner_wall_thickness)

print(f'chamber hoop: {chamber_inner_wall_hoop_stress} Pa')
print(f'throat hoop: {throat_inner_wall_hoop_stress} Pa')

print(f'chamber hoop stress FOS: {round(tensile_yield_6061_chamber/chamber_inner_wall_hoop_stress,2)}')
print(f'throat hoop stress FOS: {round(tensile_yield_6061_throat/throat_inner_wall_hoop_stress,2)}')

# ---------- static stress calcs ----------

jacket_outer_diameter = Q_(0.0508, 'meter')
jacket_thickness = Q_(0.00927, 'meter') # update
jacket_working_pressure = Q_(3791700, 'pa')
al6061_t6_tensile_yield = Q_(275760000, 'pa')
al6061_t6_bearing_yield = Q_(386064000, 'pa')

carrier_jacket_bolt_major_dia = Q_(0.00284480569, 'meter') # update
carrier_jacket_bolt_minor_dia = Q_(0.002184404369, 'meter') # update
carrier_jacket_bolt_tensile_strength = Q_(1171980000, 'pa') # update
carrier_jacket_bolt_count = 8  # update

pintle_inner_diameter = Q_(0.009448818898, 'meter') # update
pintle_shank_thickness = Q_(0.003022606045, 'meter') # update
pintle_tip_thickness = Q_(0.001524003048, 'meter') # update
pintle_shank_working_pressure = Q_(3791700, 'pa') # update
pintle_tip_working_pressure = Q_(3447000, 'pa') # update

copper_110_tensile_yield = Q_(68940000, 'pa')

carrier_pintle_bolt_major_dia = Q_(0.002184404369, 'meter')
carrier_pintle_bolt_minor_dia = Q_(0.001625603251, 'meter')
carrier_pintle_bolt_tensile_strength = Q_(1171980000, 'pa')
carrier_pintle_bolt_count = 16 # update