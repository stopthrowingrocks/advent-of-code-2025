with open('day5.txt') as f:
    raw = f.read()
ranges, ids = raw.split("\n\n")
ranges = ranges.split("\n")
ids = list(map(int, ids.split("\n")[:-1]))
num_fresh = 0
for d in ids:
    for r in ranges:
        start, end = r.split('-')
        start = int(start)
        end = int(end)
        if start <= d and d <= end:
            num_fresh += 1
            break
print(f"Part 1: {num_fresh}")

# sort by start
sorted_ranges = sorted(ranges, key=lambda r: int(r.split('-')[0]))
total_fresh = 0
st_start = None
st_end = None
for r in sorted_ranges:
    start, end = r.split('-')
    start = int(start)
    end = int(end)
    if st_end is None:
        st_start = start
        st_end = end
    elif start <= st_end:
        if end > st_end: st_end = end
    else: # start > st_end
        total_fresh += st_end - st_start + 1 # inclusive
        st_start = start
        st_end = end
total_fresh += st_end - st_start + 1
print(f"Part 2 {total_fresh}")
