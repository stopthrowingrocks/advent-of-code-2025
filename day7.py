with open("day7.txt") as f:
    raw = f.read()
lines = raw.splitlines()
flines = list(filter(lambda line: line == '.' * len(line), lines))
beams = set()
beams.add(lines[0].find('S'))
num_splits = 0
for line in lines:
    newbeams = set()
    for beam in beams:
        if line[beam] == '^':
            num_splits += 1
            newbeams.add(beam - 1)
            newbeams.add(beam + 1)
        else:
            newbeams.add(beam)
    beams = newbeams
print(f"Part 1: {num_splits}")

quantum_beams = [int(c == 'S') for c in lines[0]]
for i, line in enumerate(lines):
    newbeams = [quantum_beam for quantum_beam in quantum_beams]
    for i, num in enumerate(quantum_beams):
        if line[i] == '^' and quantum_beams[i] > 0:
            newbeams[i - 1] += quantum_beams[i]
            newbeams[i + 1] += quantum_beams[i]
            newbeams[i] -= quantum_beams[i]
    quantum_beams = newbeams
print(f"Part 2: {sum(quantum_beams)}")
