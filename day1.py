def process_input(input_file):
    xs = []
    ys = []
    with open(input_file, 'r') as file:
        for line in file:
            x, y = line.split("   ")
            xs.append(int(x))
            ys.append(int(y))
    return xs, ys

def solve1(xs, ys):
    xs.sort()
    ys.sort()
    dists = []
    for i in range(0, len(xs)):
        dists.append(abs(xs[i] - ys[i]))
    return sum(dists)

def solve2(xs, ys):
    similarity = 0
    xs_dir = {x: 0 for x in xs}
    for key in ys:
        if key in xs_dir:
            xs_dir[key] += 1
    for key, value in xs_dir.items():
        similarity += key * value
    return similarity


if __name__ == "__main__":
    xs, ys = process_input("inputs/day1.txt")
    result1 = solve1(xs.copy(), ys.copy())
    result2 = solve2(xs, ys)
    print(result1)
    print(result2)