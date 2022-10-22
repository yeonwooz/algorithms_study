#성격 유형 검사하기 홍리경
#https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    ans = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    for idx, choice in enumerate(choices):
        if choice > 4:
            grade = choice - 4
            ans[survey[idx][1]] += grade
        elif choice < 4:
            grade = 4 - choice 
            ans[survey[idx][0]] += grade
    if ans["R"] >= ans["T"]: answer += "R"
    else: answer += "T"
    if ans["C"] >= ans["F"]: answer += "C"
    else: answer += "F"
    if ans["J"] >= ans["M"]: answer += "J"
    else: answer += "M"
    if ans["A"] >= ans["N"]: answer += "A"
    else: answer += "N"
    return answer