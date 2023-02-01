def solution(n, lost, reserve):
    student = [1 for _ in range(n)]

    for i in reserve:
        student[i - 1] = 2
    for i in lost:
        if student[i - 1] == 2:
            student[i - 1] = 1
        else:
            student[i - 1] = 0
    cnt = 0

    for i in range(n):
        # 1이나 2면 cnt 1업
        if student[i] == 1 or student[i] == 2:
            cnt += 1

        # 0일때
        elif student[i] == 0:
            # student[0] == 0일 때 student[1] == 2이면 업
            if i == 0 and student[i + 1] == 2:
                cnt += 1
                student[i + 1] = 1

            # student[1 ~ n-2] == 0일 때 student[i-1] == 2일 때 아니면 student[i+1] == 2일 때 업
            elif 0 < i < n - 1:
                if student[i - 1] == 2:
                    cnt += 1
                    student[i - 1] = 1
                elif student[i + 1] == 2:
                    cnt += 1
                    student[i + 1] = 1

            # student[n-1] == 0 일 때 student[i-1] == 2 이면 업
            elif i == n - 1 and student[i - 1] == 2:
                cnt += 1
                student[i - 1] = 1

    return cnt