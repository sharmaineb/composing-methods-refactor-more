# By Kami Bigdely
# Remove assignment to method parameter.

class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

def calculate_kinetic_energy(mass, distance, time):
    # convert distance if not in kilometers
    if distance.unit == "ly":  # [ly] for light-year
        distance_in_km = distance.value * 9.461e12
    elif distance.unit == 'km':
        distance_in_km = distance.value
    else:
        print("Distance unit is Unknown")
        return

    # convert mass if not in kilograms
    if mass.unit == "solar-mass":
        mass_in_kg = mass.value * 1.98892e30
    elif mass.unit == 'kg':
        mass_in_kg = mass.value
    else:
        print("Mass unit is Unknown")
        return

    speed = distance_in_km / time 
    kinetic_energy = 0.5 * mass_in_kg * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))