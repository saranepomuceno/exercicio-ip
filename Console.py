def testaMultiplos4 (num):
    if(num %4 == 0):
        return True
    else:
        return False

def contaDivisores (num):
    soma = 0
    for i in range(1,num+1):
        if(num % i == 0):
            soma += 1
    return soma