# Part 1
def simple_increases(lines):
  count = 0
  total = 0
  prev = None

  for line in lines:
    if prev == None:
      prev = int(line)
    else:
      if int(line) > prev:
        count += 1
    prev = int(line)
    total += 1
  
  print('Total: {}'.format(total))
  print('Count: {}'.format(count))

# Part 2
def sliding_sum_increases(lines):
  length = len(lines)

  count = 0 

  for i in range(length - 3):
    window1 = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
    window2 = int(lines[i + 1]) + int(lines[i + 2]) + int(lines[i + 3])
    print('Index {}: window 1 = {}, window 2 = {}'.format(i, window1, window2))
    if window2 > window1:
      count += 1
      print('INCREASED: {}'.format(count))
  
  print('Count: {}'.format(count))


# Main
def main():
  file = open('./depth_measurements.txt', 'r')
  lines = file.readlines()

  # simple_increases(lines)
  sliding_sum_increases(lines)

if __name__ == "__main__":
  main()