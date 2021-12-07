# Part 1
def get_position(lines):
    depth = 0
    horizontal = 0

    for line in lines:
        [direction, length] = str(line).split()
        if direction == 'forward':
            horizontal += int(length)
        elif direction == 'up':
            depth -= int(length)
        elif direction == 'down':
            depth += int(length)
    print('Horizontal: {}, Depth: {}'.format(horizontal, depth))
    print('Horizontal x Depth = {}'.format(horizontal * depth))

# Part 2
def get_position_with_aim(lines):
    depth = 0
    horizontal = 0
    aim = 0

    for line in lines:
        [direction, length] = str(line).split()
        if direction == 'forward':
            horizontal += int(length)
            depth += aim * int(length)
        elif direction == 'up':
            aim -= int(length)
        elif direction == 'down':
            aim += int(length)
    print('Horizontal: {}, Depth: {}, Aim: {}'.format(horizontal, depth, aim))
    print('Horizontal x Depth = {}'.format(horizontal * depth))

# Main
def main():
  file = open('./directions.txt', 'r')
  lines = file.readlines()

#   get_position(lines)
  get_position_with_aim(lines)

if __name__ == "__main__":
  main()