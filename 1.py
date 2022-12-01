from aoc import get_input

data = get_input(1).split('\n\n')

sums = [sum(map(int, d.split('\n'))) for d in data]

print("Part 1:", max(sums))
print("Part 2:", sum(sorted(sums)[-3:]))
