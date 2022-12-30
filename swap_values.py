def swap_values(args):
    second=args[1]
    args.insert(0, second)
    print(args)
    args.pop(-1)
    return args
     



print(swap_values([1,2]))
