for i in range(11, 99):
    for j in range(i+1, 100):
        dec = i / j
        for k in range(1, 10):
            if str(k) in str(i) and str(k) in str(j):
                repl_i = str(i).replace(str(k), '')
                repl_j = str(j).replace(str(k), '')
                if len(repl_i) > 0 and len(repl_j) > 0 and int(repl_j) > 0:
                    if int(repl_i) / int(repl_j) == dec:
                        print("{0} {1} {2}".format(i, j, k))
