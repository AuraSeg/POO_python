def suma(array):
    s=0

    for i in array:
        s=s+i

    return(s)

array = []
array = [1, 2, 3]

n=len(array)
suma = suma(array)

print(f"La suma del arreglo {array} es igual a: {suma}")