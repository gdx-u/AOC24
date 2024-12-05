inp = open("input.txt", "r").read()
rules, updates = list(map(lambda e: e.split("\n"), inp.split("\n\n")))

before = {}

for rule in rules:
    first, second = rule.split("|")
    before[first] = before.get(first, []) + [second]

sum = 0
invalid_sum = 0

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
    
    else:
        pages = update.split(",")
        before_counts = [0] * len(pages)
        for i, page in enumerate(pages):
            requirements = before[page]
            requirements = [req for req in requirements if req in pages]
            before_counts[i] = len(requirements)

        correct_order = []
        while len(pages):
            max_ = max(before_counts)
            idx = before_counts.index(max_)
            correct_order += [pages[idx]]
            pages.pop(idx)
            before_counts.pop(idx)

        
        invalid_sum += int(correct_order[len(correct_order) // 2])

print(sum, invalid_sum)
