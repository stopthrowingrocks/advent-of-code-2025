with open('day2.txt') as f:
    raw = f.read()
groups = raw.split(',')
total_i = 0
for group in groups:
    idx = group.find('-')
    start_s = group[:idx]
    end_i = int(group[idx+1:])
    if len(start_s) % 2 == 1:
        # We need to increase first to be basically 100100
        num_zeros = (len(start_s) - 1) // 2
        start_s = ("1" + "0" * num_zeros) * 2
    assert len(start_s) % 2 == 0
    starthalf1_i = int(start_s[:len(start_s) // 2])
    starthalf2_i = int(start_s[len(start_s) // 2:])
    if starthalf2_i < starthalf1_i: starthalf2_i = starthalf1_i
    if starthalf2_i > starthalf1_i:
        starthalf1_i += 1 # This automatically overflows 9999 -> 10000
        starthalf2_i = starthalf1_i
    while True:
        assert starthalf1_i == starthalf2_i
        id_i = int(str(starthalf1_i) + str(starthalf2_i))
        if id_i <= end_i:
            # Invalid ID
            total_i += id_i
        else:
            break
        starthalf1_i += 1
        starthalf2_i += 1
print(f"Part 1: {total_i}")

import math
max_end = max([len(group[group.find('-')+1:]) for group in groups])

# values = []
# for num_parts in range(2, max_end + 2):
#     for group in groups:
#         idx = group.find('-')
#         start_s = group[:idx]
#         end_i = int(group[idx+1:])
#         if len(start_s) % num_parts != 0:
#             val_i = 10 ** (len(start_s) // num_parts)
#         else:
#             part_size = len(start_s) // num_parts
#             parts = list(reversed([int(start_s[len(start_s) - part_size * (i + 1):len(start_s) - part_size * i] or '0') for i in range(num_parts)]))
#             assert len(parts) == num_parts
#             val_i = parts[0]
#             for i in range(num_parts - 1):
#                 assert val_i == parts[i]
#                 if val_i > parts[i+1]:
#                     # Increase all the rest to val
#                     break
#                 if val_i < parts[i+1]:
#                     # Increase val and then increase the rest to its
#                     val_i += 1
#                     break
#                 # Eventually we prove all are val
#         assert int(str(val_i) * num_parts) >= int(start_s)

#         while True:
#             # Check for repeated substrings, continue if so
#             skip = False
#             val_s = str(val_i)
#             for num_parts_check in range(2, len(val_s)):
#                 if len(val_s) % num_parts_check == 0:
#                     check_size = len(val_s) % num_parts_check
#                     substr = val_s[:check_size]
#                     if all([substr == val_s[check_size * i:check_size * (i+1)] for i in range(1, num_parts_check)]):
#                         # skip this one
#                         skip = True
#                         break
#             if skip:
#                 val_i += 1
#                 continue

#             assert val_s == str(val_i)
#             id_i = int(val_s * num_parts)
#             if id_i <= end_i:
#                 # Invalid ID
#                 values.append(id_i)
#             else:
#                 break
#             val_i += 1
# print(sum(list(set(values))))
# # print(f"Part 2: {total_i} {num_unique}")

values = []
for group in groups:
    idx = group.find('-')
    start_i = int(group[:idx])
    end_i = int(group[idx+1:])
    for i in range(start_i, end_i):
        i_s = str(i)
        for num_parts in range(2, max_end + 2):
            if i_s == i_s[:len(i_s) // num_parts] * num_parts:
                values.append(i)
print(sum(list(set(values))))
