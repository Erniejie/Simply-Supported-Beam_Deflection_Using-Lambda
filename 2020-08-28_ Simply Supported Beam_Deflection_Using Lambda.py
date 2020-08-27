##Example_04_UDL Deflection using LAMBDA
# l : m
# w: Kn/m
#E : N/ mm^2
# I : mm^4
UDLDeflection = lambda w,l,E,I: 5*w*l**4/(384*E*I)

print(round(UDLDeflection(22.8,8000,210000,371e6),3))
