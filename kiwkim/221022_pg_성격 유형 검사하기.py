#성격 유형 검사하기 홍리경
#https://school.programmers.co.kr/learn/courses/30/lessons/118666


def a(str):
    if str == "RT" or "RT":
        return 1
    elif str == "CF" or "FC":
        return 2
    elif str == "JM" or "MJ":
        return 3
    elif str == "AN" or "NA":
        return 4

def solution(survey, choices):
    len_survey = len(survey)
    ret_dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'J':0, 'M':0, 'A':0, 'N':0}
    ret_list = []
    for i in range(len_survey):
        t = a(survey[i])
        if choices[i] < 4:
            ret_dic[survey[i][0]] += 4 - choices[i]
            print(survey[i][0] ,ret_dic[survey[i][1]],choices[i]-4 )
        elif choices[i] > 4:
            ret_dic[survey[i][1]] += choices[i] - 4
            print(survey[i][1] ,ret_dic[survey[i][1]])
    if ret_dic['R'] >= ret_dic['T']: 
        ret_list.append('R')
    else:
        ret_list.append('T')
    if ret_dic['C'] >= ret_dic['F']: 
        ret_list.append('C')
    else:
        ret_list.append('F')
    if ret_dic['J'] >= ret_dic['M']: 
        ret_list.append('J')
    else:
        ret_list.append('M')
    if ret_dic['A'] >= ret_dic['N']: 
        ret_list.append('A')
    else:
        ret_list.append('N')
    print(*ret_list, sep='')

solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])