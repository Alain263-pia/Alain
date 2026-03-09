
+v=input()
A= v.count("v")
B= v.count("v")
if A==B:
    print("tie")
elif A>B and A>0 and B>0:
    print("A")
elif A<B and A>0 and B>0:
    print("B")
