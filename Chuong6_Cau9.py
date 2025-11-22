#Câu 9: Xử lý mảng

M = [3,6,7,8,11,17,2,90,2,5,4,5,8]


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

odd = [x for x in M if x % 2 != 0]
even = [x for x in M if x % 2 == 0]
prime = [x for x in M if isPrime(x)]
not_prime = [x for x in M if not isPrime(x)]

print("Dãy số lẻ:", odd, " --> Tổng:", len(odd))
print("Dãy số chẵn:", even, " --> Tổng:", len(even))
print("Số nguyên tố:", prime)
print("Không phải số nguyên tố:", not_prime)
