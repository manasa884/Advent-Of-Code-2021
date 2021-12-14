import re


# Part 1
def find_overlapping_lines(lines):
    map = {}
    overlaps = []
    for line in lines:
        [x1, y1, x2, y2] = re.split(' -> |,', line)
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        # Vertical lines
        if x1 == x2:
            if y1 > y2:
                # Swap y1 and y2 to make sure y1 is always smaller
                y1, y2 = y2, y1
            for i in range(y1, y2 + 1):
                if x1 not in map:
                    map[x1] = [i]
                elif i in map[x1]:
                    if '{},{}'.format(x1, i) not in overlaps:
                        overlaps.append('{},{}'.format(x1, i))
                else:
                    map[x1].append(i)
            continue
        # Horizontal lines
        if y1 == y2:
            if x1 > x2:
                # Swap x1 and x2 to make sure x1 is always smaller
                x1, x2 = x2, x1
            for i in range(x1, x2 + 1):
                if i not in map:
                    map[i] = [y1]
                elif y1 in map[i]:
                    if '{},{}'.format(i, y1) not in overlaps:
                        overlaps.append('{},{}'.format(i, y1))
                else:
                    map[i].append(y1)
        # Diagonal lines
        if x1 != x2 and y1 != y2:
            if x1 > x2:
                # Swap pairs to make sure x1 is always smaller
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            step = 1
            end = y2 - y1 + 1
            if y1 > y2:
                step = -1
                end = y2 - y1 - 1
            for i in range(0, end, step):
                x = x1 + abs(i)
                y = y1 + i
                if x not in map:
                    map[x] = [y]
                elif y in map[x]:
                    if '{},{}'.format(x, y) not in overlaps:
                        overlaps.append('{},{}'.format(x, y))
                else:
                    map[x].append(y)

    print('Overlaps: {}'.format(len(overlaps)))
    # print(overlaps)


# Main
def main():
    file = open('./line_segments.txt', 'r')
    lines = file.readlines()

    find_overlapping_lines(lines)


if __name__ == "__main__":
    main()
