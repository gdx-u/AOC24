inp = open("input.txt", "r").read()
rules, updates = list(map(lambda e: e.split("\n"), inp.split("\n\n")))

before = {}

for rule in rules:
    first, second = rule.split("|")
    before[first] = before.get(first, []) + [second]

sum = 0

for update in updates:
    pre = []
    valid = True
    for page in update.split(","):
        for req in before[page]:
            if req in pre:
                valid = False
                break
        else:
            pre += [page]
        
        if not valid: break

    if valid:
        sum += int(update.split(",")[len(update.split(",")) // 2])

print(sum)
