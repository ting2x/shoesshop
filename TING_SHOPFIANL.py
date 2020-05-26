a = []
r = 0
while True :
    b = input ('TING SHOES SHOP\n NIKE [j]\n ADIDAS [k]\n REEBOK [l]\n PAN[h]\n SHOW MY LIST [s]\n EXIT [x]\n')
    b = b.lower()
    if b=='j' :
        print("**********NIKE**********\n [1] NIKE REACT 5800 \n [2] NIKE PEGASUS 6400 \n [3] NIKE AIR ZOOM 3600\n")
        c = input('PLAESE SELECT NUMBER --->')
        if c == '1' :
            a.append('NIKE REACT : 5800:30%(1740):4060')
            r+=4060
        elif c == '2' :
            a.append('NIKE PEGASUS : 6400:30%(1920):4480')
            r+=4480
        elif c == '3' :
            a.append('NIKE AIR ZOOM : 3600:30%(1080):2520')
            r+=2520
        print('\n$$$$$$_ADD TO LIST COMPLETE_$$$$$$\n')
    elif b=='k' :
        print("**********ADIDAS**********\n [1] ULTRABOOST 6000\n [2] ALPHAEDGE 9000\n [3] STAN SMITH 4990\n")
        c = input('PLAESE SELECT NUBER --->')
        if c == '1' :
            a.append('ULTRABOOST : 6000:20%(1200):4800')
            r+=4800
        elif c == '2' :
            a.append('ALPHAEDGE : 9000:20%(1800):7200')
            r+=7200
        elif c == '3' :
            a.append('STAN SMITH : 4990:20%(998):3992')
            r+=3992
        print('\n$$$$$$_ADD TO LIST COMPLETE_$$$$$$\n')
    elif b=='l' :
        print("**********REEBOK**********\n [1] REEBOK DRIFTIUM 1990\n [2] REEBOK RUN SUPREME 2990\n [3] REEBOK RUNNER 2690\n")
        c = input('PLAESE SELECT NUBER --->')
        if c == '1' :
            a.append('REEBOK DRIFTIUM : 1990:10%(199):1791')
            r+=1791
        elif c == '2' :
            a.append('REEBOK RUN SUPREME : 2990:10%(299):2691')
            r+=2691
        elif c == '3' :
            a.append('REEBOK RUNNER : 2690:10%(269):2421')
            r+=2421
        print('\n$$$$$$_ADD TO LIST COMPLETE_$$$$$$\n')
    elif b=='h' :
        print("**********PAN**********\n [1] PAN FLASH 1000\n [2] PAN BLADE 2000\n [3] PAN STAR 3000\n")
        c = input('PLAESE SELECT NUBER --->')
        if c == '1' :
            a.append('PAN FLASH : 1000:50%(500):500')
            r+=500
        elif c == '2' :
            a.append('PAN BLADE : 2000:50%(1000):1000')
            r+=1000
        elif c == '3' :
            a.append('PAN STAR : 3000:50%(1500):1500')
            r+=1500
        print('\n$$$$$$_ADD TO LIST COMPLETE_$$$$$$\n')
    elif b=='s' :
        print('{0:-<20}{0:-<10}{0:-<10}{0:-<13}'.format(""))
        print('{0:<20}{1:<13}{2:<12}{3:<15}'.format('BRAND','N PRICE','COST','L PRICE'))
        print('{0:-<20}{0:-<10}{0:-<10}{0:-<13}'.format(""))
        count = 0
        for d in a :
            e=d.split(":")
            count += 1
            print(count,end=".")
            print('{0[0]:<20}{0[1]:<10}{0[2]:<16}{0[3]:<10}'.format(e))
        print('{0:-<20}{0:-<10}{0:-<10}{0:-<13}'.format(""))
        print('TOTAL PRICE                                   ',r)
        print('{0:-<20}{0:-<10}{0:-<10}{0:-<13}'.format(""))
    elif b=='x' :
        print('THANKS FOR SUPPORT TING SHOES SHOP')
        break