# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1

for T in range(int(input())):
    arr = input()
    M, N, P = map(int, arr.split())

    result = 0
    # john's marks
    john = []
    others = []

    for m in range(1, M+1):
        marks = list(int(x) for x in input().split())

        # if these are john's marks
        if m==P:
            john = marks

        # if these are not john's
        else:
            if len(others) == 0:
                # assign the current marks to others
                others = marks
            else:
                # compare and take the max of each subject
                for i in range(N):
                    if marks[i] > others[i]:
                        others[i] = marks[i]

    print("Case #{}: {}".format(T+1, sum(max((i-j), 0) for i, j in zip(others, john))))
