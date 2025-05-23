import numpy as np
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

# input
primary_slot_count = 8 
primary_slot_width = Q_(0.000254, 'meter').magnitude
secondary_slot_count = 8
secondary_slot_width = Q_(0.0001524, 'meter').magnitude

cd = 0.7
mdot_ox = Q_(0.107, 'kg/s').magnitude
density_ox = Q_(805, 'kg/m^3').magnitude
dp_ox = Q_(1379000, 'pascal').magnitude
mdot_fuel = Q_(0.0533, 'kg/s').magnitude
density_fuel = Q_(789, 'kg/m^3').magnitude
dp_fuel = Q_(1172000, 'pascal').magnitude
diam_post = Q_(0.00558, 'meter').magnitude  # 0.2 * chamber diam
length_post = Q_(0.014, "meter").magnitude  # 0.5 * chamber diam

total_ox_flow_area = mdot_ox / (cd * np.sqrt(2 * density_ox * dp_ox))

split_ratios = np.linspace(0.1, 0.9, 9) # 0.1 = 10% mdot to primary

print(f"Total Required Ox Flow Area: {total_ox_flow_area * 1e6:.3f} mm^2\n")

print("Primary %  |  Primary Height (mm)   |  Secondary Height (mm)")
print("-----------|------------------------|-----------------------")

for split in split_ratios:
    A_primary = split * total_ox_flow_area
    A_secondary = total_ox_flow_area - A_primary

    h_primary = A_primary / (primary_slot_count * primary_slot_width)
    h_secondary = A_secondary / (secondary_slot_count * secondary_slot_width)

    print(f"{round(split * 100,3)}%      |{round(h_primary * 1000,3)} mm                |{round(h_secondary * 1000,3)} mm")

fuel_annulus_gap = mdot_fuel / (cd * np.pi * diam_post * np.sqrt(2 * density_fuel * dp_fuel))
print(f"\nFuel Annulus Gap: {fuel_annulus_gap * 1e3:.3f} mm")