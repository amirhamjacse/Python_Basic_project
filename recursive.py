def recu(n):
    if n == 0:
      return 1
    return n * recu(n-1)

result = recu(6)
print(result)