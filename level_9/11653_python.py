import math
import sys

given = int(sys.stdin.readline().rstrip())

if given !=1:
    div = given
    prime = 2
    while prime <= given:
        if given%prime == 0:
            given /=prime
            print(prime)
            prime = 2
        else :
            prime += 1
            