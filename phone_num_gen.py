for n in (5,6,7):
    for u in range(0,10):
        for m in range(0,10):
            for b in range(0,10):
                for e in range(0,10):
                    for r in range(0,10):
                        for a in range(0,10):
                            for d in range(0,10):
                                for o in range(0,10):
                                    for z in range(0,10):
                                        with open('>/ add a directory to store generated nums', "a") as f:
                                            print('>/ country code', n,u,b,e,r,a,d,o,z,sep='', file=f)