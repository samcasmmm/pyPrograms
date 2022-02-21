for t in range(int(input())):
    dsa1, toc1, dm1 = map(int, input().split())
    dsa2, toc2, dm2 = map(int, input().split())
    p1 = dsa1 + toc1 + dm1
    p2 = dsa2 + toc2 + dm2
    if p1 == p2:
        if dsa1 > dsa2:
            print('Dragon')

        elif dsa1 == dsa2:
            if toc1 > toc2:
                print('Dragon')
            elif (dsa1, toc1, dm1) == (dsa2, toc2, dm2):
                print('Tie')
            else:
                print('Sloth')

        else:
            print('Sloth')

    elif p1 > p2:
        print('Dragon')
    elif p1 < p2:
        print('Sloth')

