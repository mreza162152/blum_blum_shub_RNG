
if __name__ == '__main__':

    variable = []

    p = 11
    q = 19
    m = p*q
    seed = 3

    #for 10 random bit
    times = 10

    while (times != 0):

        val = (seed**2)%m

        u = val%2

        variable.append(u)

        #print(val)

        seed = val

        times = times - 1

    print("random bits :",variable)