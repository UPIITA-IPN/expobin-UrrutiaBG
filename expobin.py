def exponenciacion_binaria(M, e, n):
    # bin(e) devuelve algo como '0b11111010', usamos [2:] para quitar el '0b'
    bits = bin(e)[2:]
    k = len(bits)
    
    # 2. Inicialización:
    # If e_{k-1} == 1, then C = M, else C = 1
    if bits[0] == '1':
        C = M % n
    else:
        C = 1
    
    # 3. Ciclo for i = k-2 downto 0
    for i in range(1, k):
        ei = bits[i]
        
        # a) C = C^2 mod n (Elevado al cuadrado)
        C = (C ** 2) % n
        
        # b) If ei == 1 then C = C * M mod n (Multiplicación por la base)
        if ei == '1':
            C = (C * M) % n
            
    return C

if __name__ == "__main__":
    if len(sys.argv) > 3:
        # Los argumentos vienen como texto, hay que pasarlos a entero
        M = int(sys.argv[1])
        e = int(sys.argv[2])
        n = int(sys.argv[3])
        print(exponenciacion_binaria(M, e, n))

