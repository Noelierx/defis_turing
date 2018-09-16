def is_prime(nb):
    if nb == 1:
        return False
    if nb == 2:
        return True
    elif nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True

def divisors(nb, extremum = False):
    divisors = []
    inf = 1 if extremum else 2

    for i in range(inf, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb//i)
    return divisors

divs = divisors(20130101)
divs.sort(reverse=True)

for i in divs:
    if is_prime(i):
        print(i)
        break
