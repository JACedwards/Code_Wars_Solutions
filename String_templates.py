def build_string(*args):
    return f"{args}"
    # return f"I like {args.format(",".join)}!".format(",".join(args))



print(build_string('Cheese','Milk','Chocolate'))
