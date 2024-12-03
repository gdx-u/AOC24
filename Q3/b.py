inp = open("input.txt", "r").read()
muls = inp.split("mul")
sum = 0
enabled = True

for mul in muls:
    valid = enabled
    args = mul.split(")")[0]
    if args[0] != "(": 
        valid = False
    args = args[1:]
    args = args.split(",")
    if len(args) != 2: 
        # print(f"Breaking on {args}")
        valid = False
    for arg in args:
        if arg != arg.strip() or not arg.isnumeric():
            # print(f"Breaking on {arg}")
            break
    else:
        # print(args)
        if valid:
            sum += int(args[0]) * int(args[1])

    if "do()" in mul and "don't()" in mul:
        idxa = mul.index("do()")
        idxb = mul.index("don't()")
        if idxb > idxa:
            enabled = False
        else:
            enabled = True
    elif "do()" in mul:
        enabled = True
    elif "don't()" in mul:
        enabled = False 


print(sum)
