def get_spaces(blocks):
    frees = []
    curr = None
    num = 0
    for i, char in enumerate(blocks):
        if char == ".":
            if curr: num += 1
            else:
                curr = i
                num = 1
        else:
            if curr:
                frees += [[curr, num]]
                curr = None

    if curr:
        frees += [[curr, num]]

    return frees

inp = open("input.txt", "r").read()
blocks = []

block = True
id_ = 0

for char in inp:
    part = str(id_) if block else "."
    blocks += [part] * int(char)
    if block: 
        id_ += 1

    block = not block

files = []
curr = None
curr_idx = None
num = 0
for i, char in enumerate(blocks):
    if char != ".":
        if curr:
            if char == curr: num += 1
            else:
                files += [[curr, curr_idx, num]]
                curr = char
                curr_idx = i
                num = 1

        else:
            curr = char
            curr_idx = i
            num = 1

if curr:
    files += [[curr, curr_idx, num]]

files.reverse()

for i, file in enumerate(files):
    if i % 1000 == 0:
        print(i, len(files))
    char, idx, length = file
    for free in get_spaces(blocks):
        f_idx, f_length = free
        if f_idx > idx:
            break
        if f_length >= length:
            blocks[f_idx : f_idx + length] = [char] * length
            blocks[idx : idx + length] = ["."] * length
            break


checksum = 0
j = 0
for i, char in enumerate(blocks):
    if char != ".":
        checksum += int(char) * (i - j)

print(checksum)
