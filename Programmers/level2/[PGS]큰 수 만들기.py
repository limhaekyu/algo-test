def solution(number, k):

    answer = []
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop(-1)
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)

    if k > 0:
        while k > 0:
            answer.pop(-1)
            k -= 1

    return ''.join(answer)