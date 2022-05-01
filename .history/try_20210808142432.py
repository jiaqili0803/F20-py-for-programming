
def many_params(p1=1, p2=2, p3=3, p4=4):
    return p1 + p2 + p3 + p4
   
# many_params can be called many different ways
print(many_params())
print(many_params(2, 4, 6, 8))
print(many_params(p4=10))
print(many_params(30, p3=40))
print(many_params(p3=3, p1=6))



