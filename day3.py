with open('day3.txt') as f:
    raw = f.read()
lines = raw.split('\n')
count = 0
num_batteries = 12 # Or 2 for part 1
for line in lines:
    val = 0
    last_idx = -1
    for b in range(num_batteries):
        digit = 0
        idx = last_idx
        # print(f"start {idx=} {line[1+last_idx:len(line)+1+b-num_batteries]=}")
        for i, c in enumerate(line[1+last_idx:len(line)+1+b-num_batteries]):
            # print(f"process {i=} {c=} {digit=}")
            if int(c) > digit:
                digit = int(c)
                idx = 1+last_idx+i
                # print(f"{i=} {last_idx=} {idx=}")
        # print(f"{idx=}")
        val *= 10
        val += digit
        last_idx = idx
    # print(val)
    count += val
print(count)
