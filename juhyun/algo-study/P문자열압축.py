def solution(s):
    answer = len(s)
    for x in range(1, len(s) // 2 + 1):

        new_s = ''
        cur_s = ''
        result = 0
        i = 0

        while i < len(s):
            if s[i:i + x] == new_s[-x:]:
                if cur_s == s[i:i + x]:
                    pass
                else:
                    result += 1
                    cur_s = s[i:i + x]
            else:
                result += x
                cur_s = ''

            new_s += s[i:i + x]
            i += x

        if result <= answer:
            answer = result

    return answer

print(solution("abcabcdede"))