with open('day4.txt') as f:
    raw = f.read()
lines=raw.split('\n')[:-1]
def has_roll(lines, i, j):
    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[i]): return False
    return lines[i][j] == '@'
def is_moveable(lines, i, j):
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    num_adj_rolls = sum([has_roll(lines, i+dir[0],j+dir[1]) for dir in dirs])
    return num_adj_rolls < 4
count = sum([has_roll(lines, i, j) and is_moveable(lines, i, j) for i in range(len(lines)) for j in range(len(lines[i]))])
print(f"Part 1: {count}")

def update_lines(lines):
    num_before = sum([has_roll(lines, i, j) for i in range(len(lines)) for j in range(len(lines[i]))])
    newlines = [
        ''.join([
            '@' if has_roll(lines, i, j) and not is_moveable(lines, i, j) else '.'
            for j in range(len(lines[i]))
        ]) for i in range(len(lines))
    ]
    num_after = sum([has_roll(newlines, i,j) for i in range(len(newlines)) for j in range(len(newlines[i]))])
    return num_before - num_after, newlines
countcount = 0
newlines = lines
# print(update_lines(update_lines(lines)[1]))
while True:
    newcount, newlines = update_lines(newlines)
    if newcount == 0:
        break
    # print(f"Removed {newcount}")
    countcount += newcount
print(f"Part 2 {countcount}")
