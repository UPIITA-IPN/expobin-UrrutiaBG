import sys

def exponenciacion_binaria(M, e, n):
    bits = bin(e)[2:]
    k = len(bits)

    if bits[0] == '1':
        C = M % n
    else:
        C = 1

    for i in range(1, k):
        ei = bits[i]
        C = (C ** 2) % n
        if ei == '1':
            C = (C * M) % n

    return C


datos = sys.stdin.read().split()
M = int(datos[0])
e = int(datos[1])
n = int(datos[2])

print(exponenciacion_binaria(M, e, n))