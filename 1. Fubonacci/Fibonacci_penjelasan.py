## PENJELASAN LENGKAP ADA DI "Fibonacci_penjelasan1.txt" dan "Fibonacci_penjelasan2.txt"

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # else
    return fibo(n - 1) + fibo(n - 2)    # Looping menurun ke kondisi terkecil, krn blm dapat angka pasti
                                        # menjalankan fungsi yg melibatkan fungsi lagi

print(fibo(6))
# 8

print("\n")

# "for n in range" ADALAH CARA MUTLAK UNTUK MEMJABARKAN KEBENARAN SUATU FORMULA DALAM BENTUK INDEXING
print([fibo(n) for n in range(7)]) # index 0 = F0 /// range(7) means fibo(6)
# [0, 1, 1, 2, 3, 5, 8]


print("\n")

### MEMODIFIKASI CASE

def fibo(n):
    if n <= 1:
        return 1
    return fibo(n - 1) + fibo(n - 2) 

print(fibo(6))
# 13

print("\n")
print([fibo(n) for n in range(7)])
# [1, 1, 2, 3, 5, 8, 13]


print("\n")

def fibo(n):
    if n <= 1:
        return 3
    return fibo(n - 1) + fibo(n - 2) 

print(fibo(6))
# 39

print("\n")
print([fibo(n) for n in range(7)])
# [3, 3, 6, 9, 15, 24, 39]