
from Punto import Punto

mipunto1=Punto()
mipunto2=Punto()

a=mipunto1.calcular_distancia(mipunto2)

mipunto1.x=8
mipunto1.y=2

mipunto2.x=9
mipunto2.y=9

a=mipunto1.calcular_distancia(mipunto2)

print(a)