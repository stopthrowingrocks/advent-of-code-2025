import numpy as np
import pandas as pd
df = pd.read_csv('day8.txt', header=None)
pts = df.to_numpy()
D = pts.shape[0]
# print(pts.shape)
dsts = np.linalg.norm(pts[:, None, :] - pts[None, :, :], axis=-1)
# print(dsts.shape)
idxs = dsts.flatten().argsort()[D:]
REP = 0
RANK = 1
SIZE = 2
repmap = np.vstack([np.arange(D), np.zeros(D), np.ones(D)]).T # Representative, rank, circuit_size
# print(repmap.shape)
# Only the reps have accurate circuit_sizes
num_connections = 1000
for idx in idxs:
    i1 = idx // D
    i2 = idx % D
    if i1 >= i2: continue
    # i1 < i2
    # connect i1 to i2, find the representatives for both
    while repmap[i1, REP] != i1: i1 = int(repmap[i1, REP])
    while repmap[i2, REP] != i2: i2 = int(repmap[i2, REP])
    if i1 == i2:
        num_connections -= 1
        if num_connections == 0: break
        # print("skipped!")
        continue
    # now i1 and i2 are distinct representatives
    if repmap[i1, RANK] >= repmap[i2, RANK]:
        # i1 has greater rank, map i2 -> i1
        # print(f"map {i2} -> {i1}")
        repmap[i2, REP] = i1
        if repmap[i1, RANK] == repmap[i2, RANK]: repmap[i1, RANK] += 1
        repmap[i1, SIZE] += repmap[i2, SIZE]
    else:
        # print(f"map {i1} -> {i2}")
        repmap[i1, REP] = i2
        repmap[i2, SIZE] += repmap[i1, SIZE]
    num_connections -= 1
    if num_connections == 0: break
# Identify circuits
sizes = []
for d in range(D):
    if repmap[d, REP] == d:
        # d is a representative
        # print(repmap[d])
        sizes.append(repmap[d, SIZE])
# print(sizes)
sizes.sort()
print(f"Part 1: {sizes[-1]*sizes[-2]*sizes[-3]}")

# Part 2
repmap = np.vstack([np.arange(D), np.zeros(D), np.ones(D)]).T # Representative, rank, circuit_size
# Only the reps have accurate circuit_sizes
num_connections = 0
for idx in idxs:
    i1 = idx // D
    oi1 = i1
    i2 = idx % D
    oi2 = i2
    if i1 >= i2: continue
    # i1 < i2
    # connect i1 to i2, find the representatives for both
    while repmap[i1, REP] != i1: i1 = int(repmap[i1, REP])
    while repmap[i2, REP] != i2: i2 = int(repmap[i2, REP])
    if i1 == i2:
        continue
    # now i1 and i2 are distinct representatives
    if repmap[i1, RANK] >= repmap[i2, RANK]:
        # i1 has greater rank, map i2 -> i1
        # print(f"map {i2} -> {i1}")
        repmap[i2, REP] = i1
        if repmap[i1, RANK] == repmap[i2, RANK]: repmap[i1, RANK] += 1
        repmap[i1, SIZE] += repmap[i2, SIZE]
    else:
        # print(f"map {i1} -> {i2}")
        repmap[i1, REP] = i2
        repmap[i2, SIZE] += repmap[i1, SIZE]
    num_connections += 1
    if num_connections == D - 1:
        x1 = pts[oi1, 0]
        x2 = pts[oi2, 0]
        print(f"Part 2: {x1*x2}")
        break
