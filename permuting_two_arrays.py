'''
def twoarrays(k, A, B):
  """
  Esta función devuelve una cadena, ya sea `sí` o `no`.

  Parámetros:
    k: un entero
    A[n]: un vector de enteros
    B[n]: un vector de enteros

  Devuelve:
    Una cadena, ya sea `sí` o `no`.
  """

  n = len(A)

  # Ordenar los vectores A y B.
  A.sort()
  B.sort()

  # Si el primer elemento de A + B es mayor que k,
  # entonces existe una permutación válida.
  if A[0] + B[0] > k:
    return "sí"

  # Si el último elemento de A + B es menor o igual que k,
  # entonces no existe una permutación válida.
  if A[n - 1] + B[n - 1] <= k:
    return "no"

  # Búsqueda binaria para encontrar el primer elemento de B
  # tal que A[i] + B[j] > k.
  j = 0
  for i in range(n):
    while j < n and A[i] + B[j] <= k:
      j += 1

    # Si encontramos un elemento que satisface la condición,
    # entonces existe una permutación válida.
    if j < n:
      return "sí"

  # Si no encontramos ningún elemento que satisfaga la condición,
  # entonces no existe una permutación válida.
  return "no"

'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    count = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        if (A[i] + B[i]) >= k:
            count += 1

    if count >= len(A):
        return 'YES'
    else:
        print(count)
        return 'NO'

print(twoArrays(10, [2,1,3], [7,8,9]))