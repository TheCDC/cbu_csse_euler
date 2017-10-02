def prob24():
    count,a,b,c,d,e,f,g,h,i,j = (0,)*11
    while (a<=9):
        while (b<=9):
            while (c<=9):
                while (d<=9):
                    while (e<=9):
                        while (f<=9):
                            while (g<=9):
                                while (h<=9):
                                    while (i<=9):
                                        while (j<=9):
                                            if (a != b and a != c and a != d and a != e and a != f and a != g and a != h and a != i and a != j and b!=c and b!=d and b!=e and b!=f and b!=g and b!=h and b!=i and b!=j and c!=d and c!=e and c!=f and c!=g and c!=h and c!=i and c!=j and d!=e and d!=f and d!=g and d!=h and d!=i and d!=j and e!=f and e!=g and e!=h and e!=i and e!=j and f!=g and f!=h and f!=i and f!=j and g!=h and g!= i and g!=j and h!=i and h!=j and i!=j):
                                                count += 1
                                                if (count >= 1000000):
                                                    return "The answer is:", a, b, c, d, e, f, g, h, i, j
                                            j+=1
                                        j=0
                                        i+=1
                                    i=0
                                    h+=1
                                h=0
                                g+=1
                            g=0
                            f+=1
                        f=0
                        e+=1
                    e=0
                    d+=1
                d=0
                c+=1
            c=0
            b+=1
        b=0
        a+=1

prob24( )
