res = {}
def tribonacci(n):
    # TODO : write your code here
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n in res:
        return res[n]
    ans =tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    res[n] = ans
    return ans

print(tribonacci(0)) #output should be 0
print(tribonacci(1)) #output should be 0
print(tribonacci(2)) #output should be 1
print(tribonacci(6)) #output should be 7
print(tribonacci(10)) #output should be 81
print(tribonacci(33)) #output should be 98950096
