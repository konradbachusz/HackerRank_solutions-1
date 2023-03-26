# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    list_of_diffs=[]
    index=1
    B=A.copy()
    B.reverse()

    for i in range(len(A)-1):
        # print(i)
        list_slice=A[:index]
        a=sum(list_slice)
        diff_list=B[:-index]
        diff=sum(diff_list)

        difference=abs(a-diff)
        list_of_diffs.append(difference)

        index+=1
    return min(list_of_diffs)
