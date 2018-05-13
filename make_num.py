with open('birth.txt','w') as fp:
    for a in range(10):
        for b in range(10):
            for c in range(0,9,2):
                for d in range(10):
                    fp.write(str(a)+str(b)+str(c)+str(d)+'\n')
                fp.write(str(a)+str(b)+str(c)+'x\n')