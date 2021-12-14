# Part 1
def calculate_cheapest_fuel_amount(crab_locations):
    map = {}
    amt = None
    for crab in crab_locations:
        if crab not in map:
            # fuel = get_fuel_to_location_1(crab_locations, crab)
            fuel = get_fuel_to_location_2(crab_locations, crab)
            map[crab] = fuel
            if amt == None or fuel < amt:
                amt = fuel
    print("Cheapest fuel amt: {}".format(amt))
    return amt


# [Part 1] Get the amount of fuel to location loc
def get_fuel_to_location_1(crabs, loc):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab - loc)
    return fuel


# [Part 2] Get the amount of fuel to location loc
def get_fuel_to_location_2(crabs, loc):
    # Fuel used up by distance travelled
    def get_fuel_by_distance(distance):
        result = 0
        for i in range(1, distance + 1):
            result += i
        return result

    fuel = 0
    for crab in crabs:
        fuel_per_crab = get_fuel_by_distance(abs(crab - loc))

        fuel += fuel_per_crab
    return fuel


# Main
def main():
    file = open('./crab_locations.txt', 'r')
    lines = file.readlines()

    # List of all the crab locations as ints
    crab_locations = list(map(int, lines[0].split(',')))

    calculate_cheapest_fuel_amount(crab_locations)


if __name__ == "__main__":
    main()
