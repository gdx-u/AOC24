import copy

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

new = copy.deepcopy(blocks)
j = 0
for i, item in enumerate(new[::-1]):
    if item != ".":
        try:
            while blocks[j] != ".":
                j += 1
        except:
            j = 0
            while blocks[j] != ".":
                j += 1

        bi = len(blocks) - 1 - i

        blocks[bi] = "."

        blocks[j] = item
        j += 1

    if not "".join(blocks[blocks.index("."):]).replace(".", ""):
        break

checksum = 0
j = 0
for i, char in enumerate(blocks):
    if char != ".":
        checksum += int(char) * (i - j)
    else:
        j += 1

print(checksum)
