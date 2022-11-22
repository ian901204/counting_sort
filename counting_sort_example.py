def counting_sort(A):
    B = [0] * len(A)
    c = [0] * 6
    for i in A:
        c[i] += 1
    for i in range(len(c)):
        if i == 0:
            continue
        c[i] = c[i] + c[i - 1]
    for i in range(len(A) - 1, -1, -1):
        B[c[A[i]] - 1] = A[i]
        c[A[i]] -= 1
    return B


input_list = [3,5,2,3,5,4,0,1,0,2]
ans_list = counting_sort(input_list)
for i in ans_list:
    print(i)
