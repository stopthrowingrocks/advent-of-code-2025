with open('day6.txt') as f:
    raw = f.read()
lines = raw.split('\n')[:-1]

def process_val_line(line):
    return list(map(int, filter(lambda s: s != '', line.split(' '))))

val_lines = lines[:-1]
pval_lines = list(map(process_val_line, val_lines))

last_line = lines[-1]
plast_line = list(filter(lambda s: s != '', last_line.split(' ')))

count = 0
for i, op in enumerate(plast_line):
    if op == '+':
        val = 0
        for j in range(len(pval_lines)):
            val += pval_lines[j][i]
        count += val
    else:
        val = 1
        for j in range(len(pval_lines)):
            val *= pval_lines[j][i]
        count += val
print(f"Part 1: {count}")

count2 = 0
val = None
for i, c in enumerate(last_line):
    if c == '*':
        op = '*'
        val = 1
    elif c == '+':
        op = '+'
        val = 0
    num = 0
    updated = False
    for j in range(len(val_lines)):
        if val_lines[j][i] != ' ':
            num *= 10
            num += int(val_lines[j][i])
            updated = True
    if updated:
        if op == '*': val *= num
        if op == '+': val += num
    else:
        count2 += val
count2 += val
print(f"Part 2: {count2}")
