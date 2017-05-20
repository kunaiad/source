n = int(input());

for y in range(0, n):
    #print(y)
    for x in range(0, n):
        p = min(x,y,n-x-1,n-y-1)
        #print(p)
        if x>=y:
            q = x+y - 2*p

        else:
      	    q = (n-1 - 2*p)*4 - (x-p+y-p)

        q += 4 * (p*n - (p*p))
        print(q)
        print("{:3d}".format(q), end="")
    print()

