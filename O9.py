def calculate(*args): return tuple
([sum(args)/len(args),
[x for x in args if x > sum(args)/len(args)]])