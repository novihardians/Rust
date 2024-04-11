## PENJELASAN LENGKAP ADA DI "Fibonacci_penjelasan1.txt" dan "Fibonacci_penjelasan2.txt"

def fibo(n):
    # FORMULA SALAH TDK SEMPURNA
    if n == 0:
        return 0
    # else
    return fibo(n - 1) + fibo(n - 2)    # Looping menurun ke kondisi terkecil, krn blm dapat angka pasti
                                        # menjalankan fungsi yg melibatkan fungsi lagi

print(fibo(6))

## KALAU RUMUS TIDAK TEPAT DAN TIDAK DAPAT NILAI PASTI
# Traceback (most recent call last):
#   File "Fibonacci_penj_kalauError.py", line 10, in <module>
#     print(fibo(6))
#   File "Fibonacci_penj_kalauError.py", line 7, in fibo
#     return fibo(n - 1) + fibo(n - 2)    # Looping menurun ke kondisi terkecil, krn blm dapat angka pasti
#   File "Fibonacci_penj_kalauError.py", line 7, in fibo
#     return fibo(n - 1) + fibo(n - 2)    # Looping menurun ke kondisi terkecil, krn blm dapat angka pasti
#   File "Fibonacci_penj_kalauError.py", line 7, in fibo
#     return fibo(n - 1) + fibo(n - 2)    # Looping menurun ke kondisi terkecil, krn blm dapat angka pasti
#   [Previous line repeated 995 more times]
#   File "Fibonacci_penj_kalauError.py", line 4, in fibo
#     if n == 0:
# RecursionError: maximum recursion depth exceeded in comparison