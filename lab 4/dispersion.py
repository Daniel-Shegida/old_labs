import math


def centralMoment(x):
    N = 1000
    m = 0
    for i in range(N):
        m = m + x[i]
    return m / N


def dispersion(x):
    N = 1000
    s2 = 0
    moment = centralMoment(x)
    for i in range(N):
        s2 = s2 + (x[i] - moment) ** 2
    print('дисп',s2 / N)
    print('момент',moment)
    return s2 / N

def dispersion2(x,m):
    N = 1000
    s2 = 0
    for i in range(N):
        s2 = s2 + (x[i] - m) ** 2
    print('дисп',s2 / N)
    print('момент',m)
    return s2 / N

def neprdispersion(b,a):
    return ((b-a)**2)/12


def gausmoment(u):
    return u

def gausdisp(sigma):
    return sigma

def relmoment(sigma):
    return sigma * math.sqrt(math.pi/2)

def reldisp(sigma):
    return (2-math.pi/2) * (sigma**2)


def expected(x):
    N = len(x)
    m = 0
    for i in range(N):
        m += x[i]
    m = m / N
    print(f"Выборочное m: ", m)
    return variance(x, m)


# Функция нахождения дисперсии
def variance(x, m):
    N = len(x)
    sigma = 0
    for i in range(N):
        sigma += (x[i] - m)**2
    sigma = sigma / N
    print(f"Выборочная дисперсия  c выборочными значениями момента : ", sigma)
    return m, sigma


def varianceTheoria(x, m):
    N = len(x)
    sigma = 0
    for i in range(N):
        sigma += (x[i] - m)**2
    sigma = sigma / N
    print(f"Выборочная дисперсия c теоретическими значениями момента : ", sigma)
    return m, sigma
