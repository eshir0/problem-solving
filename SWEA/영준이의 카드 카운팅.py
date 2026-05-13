for T in range(1,int(input())+1):
    s = input()
    
    S = ["S01","S02","S03","S04","S05","S06","S07","S08","S09","S10","S11","S12","S13"]
    D = ["D01","D02","D03","D04","D05","D06","D07","D08","D09","D10","D11","D12","D13"]
    H = ["H01","H02","H03","H04","H05","H06","H07","H08","H09","H10","H11","H12","H13"]
    C = ["C01","C02","C03","C04","C05","C06","C07","C08","C09","C10","C11","C12","C13"]

    n = []
    for i in range(0,len(s),3):
        n.append(s[i:i+3])
    
    for i in n:
        try:
            if i in S:
                S.remove(i)
            elif i in D:
                D.remove(i)
            elif i in H:
                H.remove(i)
            elif i in C:
                C.remove(i)
        except:
            pass

    a = []
    cnt = 0
    for i in n:
        if i in a:
           cnt += 1 
        a.append(i)

    if cnt >= 1:
        print(f'#{T} ERROR')
    else:
        print(f'#{T} {len(S)} {len(D)} {len(H)} {len(C)}')