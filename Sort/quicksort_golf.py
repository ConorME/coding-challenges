def q(a): return a if len(a)<=1 else q([x for x in a if x<a[len(a)//2]])+[x for x in a if x==a[len(a)//2]]+q([x for x in a if x>a[len(a)//2]])

