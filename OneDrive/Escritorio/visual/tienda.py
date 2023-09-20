
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0

clave = ""

while clave.lower() != "si":
    a+=int(input("cuanta cantidad quiere del producto a: "))
    b+=int(input("cuanta cantidad quiere del producto b: "))
    c+=int(input("cuanta cantidad quiere del producto c: "))
    d+=int(input("cuanta cantidad quiere del producto d: "))
    e+=int(input("cuanta cantidad quiere del producto e: "))
    f+=int(input("cuanta cantidad quiere del producto f: "))
    g+=int(input("cuanta cantidad quiere del producto g: "))
    h+=int(input("cuanta cantidad quiere del producto h: "))
    i+=int(input("cuanta cantidad quiere del producto i: "))
    j+=int(input("cuanta cantidad quiere del producto j: "))
    
    clave=input("¿quieres terminar de usar el programa? ")

productos = [a,b,c,d,e,f,g,h,i,j,]

productomayor = sorted(productos)
mayor= productomayor[-1]
print("el producto que mas se compro fue " + str(mayor))

