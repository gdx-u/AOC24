inp = open("input.txt", "r").read()
muls = inp.split("mul")
sum = 0

for mul in muls:
    args = mul.split(")")[0]
    if args[0] != "(": continue
    args = args[1:]
    args = args.split(",")
    if len(args) != 2: 
        # print(f"Breaking on {args}")
        continue
    for arg in args:
        if arg != arg.strip() or not arg.isnumeric():
            # print(f"Breaking on {arg}")
            break
    else:
        print(args)
        sum += int(args[0]) * int(args[1])

print(sum)
