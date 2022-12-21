def solution(answers):
    answer = []
    count = [0,0,0]
    num = len(answers)//5
    arr1 = [1,2,3,4,5]*(10000//5)
    arr2 = [2,1,2,3,2,4,2,5]*(10000//8)
    arr3 = [3,3,1,1,2,2,4,4,5,5]*(10000//10)

    for i in range(len(answers)):
        if arr1[i] == answers[i]:
            count[0] += 1
        if arr2[i] == answers[i]:
            count[1] += 1
        if arr3[i] == answers[i]:
            count[2] += 1
        print(" ")

    maxNum = max(count)
    for i in range(len(count)):
        if count[i] == maxNum:
            answer.append(i+1)
    return answer