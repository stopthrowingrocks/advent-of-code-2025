with open('day1.txt') as f:
    raw = f.read()
lines = raw.split('\n')
password = 0
dial = 50
for line in lines:
    if len(line) > 0:
        sign = 1 if line[0] == 'R' else -1
        count = float(line[1:])
        dial = (dial + sign * count) % 100
        if dial == 0:
            password += 1
print(f"Day 1 pt 1 password: {password}")

password2 = 0
dial = 50
for line in lines:
    if len(line) > 0:
        sign = 1 if line[0] == 'R' else -1
        count = int(line[1:])
        for i in range(count):
            dial = (dial + sign) % 100
            if dial == 0:
                password2 += 1
print(f"Day 1 pt 2 password: {password2}")
