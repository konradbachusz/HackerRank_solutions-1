# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here

    max_n=max(A)
    expected_set=set([*range(1, max_n+1, 1)])

    actual_set=set(A)
    len_actual=len(A)


    if actual_set==expected_set and len(actual_set)==len_actual:
        return 1
    else:
        return 0
