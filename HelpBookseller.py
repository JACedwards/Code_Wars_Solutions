
def helpBookseller(L,M):
    
    cd_num = {}
    for s in L:
        cd_num[s[0]] = 0

    ind = L[0].index(' ')
    for c in L:
        cd_num[c[0]] = cd_num.get(c[0]) + int(c[ind+ 1:])
    print(cd_num)

    sub_output = {}
    lst_in_dct = []
    for code in M:
        for k , v in cd_num.items():
            if code == k:
                sub_output[k] = v
                lst_in_dct.append(k)

    for missing in M:
        if missing not in lst_in_dct:
            sub_output[missing] = 0

    return sub_output


print(helpBookseller(L = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"], M = ["A", "B", "C", "D"]))