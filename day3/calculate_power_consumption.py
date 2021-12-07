# Part 1
def get_power_consumption(lines):
    counts = get_counts(lines)

    gamma_rate = ''
    epsilon_rate = ''

    for num in counts:
        if num > len(lines) / 2:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
    print('Binary - Gamma rate: {}, Epsilon rate: {}'.format(gamma_rate, epsilon_rate))
    print('Decimal - Gamma rate: {}, Epsilon rate: {}'.format(int(gamma_rate,
          2), int(epsilon_rate, 2)))
    print('Power consumption: {}'.format(
        int(gamma_rate, 2) * int(epsilon_rate, 2)))


# Part 2
def get_life_support_rating(lines):
    counts = get_counts(lines)
    oxygen_copy = lines.copy()
    co2_copy = lines.copy()
    val = counts[0]

    # Get oxygen generator rating
    for pos in range(len(counts)):
        arr = []
        val = get_counts(oxygen_copy)[pos]
        for line in oxygen_copy:
            # Common number = 1
            if val >= len(oxygen_copy) / 2 and line[pos] == '1':
                arr.append(line)
            # Common number = 0
            if val < len(oxygen_copy) / 2 and line[pos] == '0':
                arr.append(line)
        oxygen_copy = arr
        if len(arr) == 1:
            break

    # Get co2 scrubber rating
    for pos in range(len(counts)):
        arr = []
        val = get_counts(co2_copy)[pos]
        for line in co2_copy:
            # Least common number = 0
            if val >= len(co2_copy) / 2 and line[pos] == '0':
                arr.append(line)
            # Least common number = 1
            if val < len(co2_copy) / 2 and line[pos] == '1':
                arr.append(line)
        co2_copy = arr
        if len(arr) == 1:
            break

    oxygen_generator_rating = ''
    co2_scrubber_rating = ''

    if len(oxygen_copy) == 1:
        oxygen_generator_rating = oxygen_copy[0]
    if len(co2_copy) == 1:
        co2_scrubber_rating = co2_copy[0]

    print('Oxygen generator rating: {}, CO2 scrubber rating: {}'.format(
        int(oxygen_generator_rating, 2), int(co2_scrubber_rating, 2)))
    print('Life support rating: {}'.format(
        int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)))


# Helper functions
def get_counts(lines):
    counts = []
    for line in lines:
        if len(counts) < 1:
            counts = [0 for s in range(len(line) - 1)]
        for i, char in enumerate(line):
            if char == '1':
                counts[i] += 1
    return counts


# Main
def main():
    file = open('./binary.txt', 'r')
    lines = file.readlines()

    # get_power_consumption(lines)
    get_life_support_rating(lines)


if __name__ == "__main__":
    main()
