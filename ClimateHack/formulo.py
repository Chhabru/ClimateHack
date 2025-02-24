import math

# Constants for molar masses
M_CO2 = 44.01  # g/mol (CO2)
M_CARB = 60.01  # g/mol (carbonate)
M_LIMESTONE = 100.09  # g/mol (limestone)
lbs_per_gram = 1 / 453.592  # conversion factor from grams to pounds


def limestone(co2,carb,climate_factor):
    co2 = float(co2)  # Convert to float
    carb = float(carb)  # Convert to float

    float(climate_factor)
    V_m3 = (4 / 3) * math.pi * (1000 * 1) ** 3
    limestone_pounds_adjusted = (
    ((co2 * 10**-6 * M_CO2 + carb * 10**-6 * M_CARB) * V_m3)  # total grams of limestone
    * lbs_per_gram  # convert grams to pounds
    * M_LIMESTONE  # molar mass of limestone
    * climate_factor  # climate factor
    )
    return limestone_pounds_adjusted
