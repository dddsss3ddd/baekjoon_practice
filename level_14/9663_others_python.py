import sys
import copy

import time


x = int(input())
start = time.time()

def solution(n):
    def backtrack(row = 0, hills = 0, next_row = 0, dales = 0, count = 0):
        if row == n:
            count += 1
        else:
            free_columns = columns & ~(hills | next_row | dales)
            while free_columns:
                curr_column = - free_columns & free_columns
                free_columns ^= curr_column
                
                count = backtrack(row + 1, 
                                    (hills | curr_column) << 1, 
                                    next_row | curr_column, 
                                    (dales | curr_column) >> 1, 
                                    count)
        return count
    columns = (1 << n) - 1
    return backtrack()

print(solution(x))

# ===============================================================================
# def search(col, ld, rd, n):
#     size = ((1 << n) - 1)
#     count = 0

#     if col == size:
#         return 1

#     slots = ~(col | ld | rd) & size
#     while slots:
#         bit = slots & -slots
#         count += search(col | bit, (ld | bit) >> 1, (rd | bit) << 1, n)
#         slots -= bit
#     return count


# def solution(n):
#     return search(0, 0, 0, n)


# print(solution(x))

print('elapse : ',time.time()-start)

