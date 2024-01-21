def calculate_temperature():
    import scipy.constants

    # Power per unit area in W/m^2
    power_per_unit_area = 355

    # Stefan-Boltzmann constant in W/m^2K^4
    stefan_boltzmann_constant = scipy.constants.Stefan_Boltzmann

    # Calculate temperature
    temperature = (power_per_unit_area / stefan_boltzmann_constant) ** (1/4)

    print(f"The average temperature of the Earth's surface is {temperature} K")

calculate_temperature()

def print_correct_option():
    correct_option = "N0 exp[-(tln2)/T]"
    print(f"The correct expression for the law of radioactive decay is: {correct_option}")

print_correct_option()