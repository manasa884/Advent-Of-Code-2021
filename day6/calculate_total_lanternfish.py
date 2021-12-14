# Part 1
def calculate_total_lanternfish(starting_fish, days):
    fish = starting_fish.copy()
    for _ in range(1, days + 1):
        newfish = []
        for idx, f in enumerate(fish):
            if f == 0:
                fish[idx] = 6
                newfish.append(8)
            else:
                fish[idx] = f - 1
        fish = fish + newfish
    print(fish)
    print('Total lanternfish: {}'.format(len(fish)))


# Part 2
def calculate_total_lanternfish_optimized(fish, days):
    map = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    for f in fish:
        if f == 0:
            map[8] = map[8] + 1
            map[6] = map[6] + 1
        else:
            map[f - 1] = map[f - 1] + 1
    for _ in range(days - 1):
        newmap = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }
        newmap[0] = map[1]
        newmap[1] = map[2]
        newmap[2] = map[3]
        newmap[3] = map[4]
        newmap[4] = map[5]
        newmap[5] = map[6]
        newmap[6] = map[0] + map[7]
        newmap[7] = map[8]
        newmap[8] = map[0]
        map = newmap
    print(map)
    total = sum(map.values())
    print("Total lanternfish: {}".format(total))


# Main
def main():
    file = open('./lanternfish.txt', 'r')
    lines = file.readlines()

    # List of all the fish as ints
    fish = list(map(int, lines[0].split(',')))

    days = 256

    calculate_total_lanternfish_optimized(fish, days)


if __name__ == "__main__":
    main()
