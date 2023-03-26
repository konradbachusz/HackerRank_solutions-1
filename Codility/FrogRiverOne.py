# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):

    expected_path=set([*range(1, X+1, 1)])
    actual_path=[]

    # Implement your solution here
    seconds=-1

    for leaf in A:
        if set(actual_path)!=expected_path:
            actual_path.append(leaf)
            seconds+=1
        else:
            path_found=True

            break
    if path_found==True:
        return seconds
    else:
        return -1
