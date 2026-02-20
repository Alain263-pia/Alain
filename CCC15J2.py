a= input()
p= a.count(":-)")
q= a.count(":-(")
if p==q and p>0 and q>0:
    print("unsure")
if p==0 and q==0:
    print("none")
if p>q and q>0:
    print("happy")
if p>q:
        print("sad")
