# Introduceti vectorul nesortat in input.txt
#Inputul va fi de forma 1 2 3...
#Se poate genera un input random de aici: https://www.random.org/integer-sets/
#Daca doriti sa testati corectitudinea unei sortari, apelati in main testsort(v,*metoda*(v))
#Quicksort nu functioneaza la seturi mai mari de 990 de numere

import time

def testsort(v1, v2):
    v1.sort()
    if v1 == v2:
        print("Vectorul este sortat corect")
    else:
        print("Vectorul NU este sortat corect")


def bubblesort(v):
    for i in range(len(v) - 1):
        for j in range(len(v)):
            if v[i] < v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
    return v


def countsort(v):
    m = max(v)
    freq = [0] * (m + 1)
    x = []
    for i in range(len(v)):
        freq[v[i]] = freq[v[i]] + 1
    for i in range(len(freq)):
        for j in range(freq[i]):
            x.append(i)
    return x


def merge(v, s, d):
    m = (s + d) // 2
    if s != d:
        x = merge(v, s, m)
        y = merge(v, m + 1, d)
        i = j = 0;
        z = []
        while i < len(x) and j < len(y):
            if x[i] < y[j]:
                z.append(x[i])
                i = i + 1
            else:
                z.append(y[j])
                j = j + 1
        if i == len(x):
            for k in range(j, len(y)):
                z.append(y[k])
        elif j == len(y):
            for k in range(i, len(x)):
                z.append(x[k])
        return z
    else:
        return [v[s]]


def mergesort(v):
    return merge(v, 0, len(v) - 1)


def part(v, low, high):
    i = low - 1
    pivot = v[high]
    for j in range(low, high):
        if v[j] < pivot:
            i = i + 1
            aux = v[i]
            v[i] = v[j]
            v[j] = aux

    i = i + 1
    aux = v[i]
    v[i] = v[high]
    v[high] = aux
    return i


def qs(v, low, high):
    if low < high:
        pi = part(v, low, high)
        qs(v, low, pi - 1)
        qs(v, pi + 1, high)


def quicksort(v):
    qs(v, 0, len(v) - 1)
    return v


def countsortdigit(v, cif):
    out = [0] * len(v)
    fq = [0] * 10
    for i in range(len(v)):
        ind = v[i] // cif
        fq[ind % 10] = fq[ind % 10] + 1
    for i in range(1, 10):
        fq[i] += fq[i - 1]

    i = len(v) - 1
    while i >= 0:
        ind = v[i] // cif
        out[fq[ind % 10] - 1] = v[i]
        fq[ind % 10] = fq[ind % 10] - 1
        i = i - 1

    for i in range(0, len(v)):
        v[i] = out[i]


def radixsort(v):
    m = max(v)
    cif = 1
    while m / cif > 0:
        countsortdigit(v, cif)
        cif = cif * 10
    return v


def rapid(v):
    v1=v
    mintimp = 100000.00
    start = time.time()
    v1 = radixsort(v)
    end = time.time()
    if end - start < mintimp:
        mintimp = end - start
        out = (mintimp, "radixsort")

    v1=v
    start = time.time()
    v1 = countsort(v)
    end = time.time()
    if end - start < mintimp:
        mintimp = end - start
        out = (mintimp, "countsort")
    v1=v
    start = time.time()
    v1 = bubblesort(v)
    end = time.time()
    if end - start < mintimp:
        mintimp = end - start
        out=(mintimp,"bubblesort")
    v1=v
    start = time.time()
    v1 = quicksort(v)
    end = time.time()
    if end - start < mintimp:
        mintimp = end - start
        out = (mintimp, "quicksort")
    v1=v
    start = time.time()
    v1 = mergesort(v)
    end = time.time()
    if end - start < mintimp:
        mintimp = end - start
        out = (mintimp, "mergesort")
    return out

with  open("input.txt", "r") as f:
    intrare = f.read()
intrare = intrare.split()
for i in range(len(intrare)):
    intrare[i] = int(intrare[i])
v = intrare
print(v)
rapiditate=rapid(v)
print("Cea mai rapida sortare este",end=" ")
print(rapiditate[1],end=" ")
print("cu viteza aproximativa de aproximativ",end=" ")
print(rapiditate[0],end=" secunde.")


