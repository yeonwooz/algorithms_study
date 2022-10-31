# 신고 결과 받기
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    reported = {}
    for i in id_list:
        reported[i] = set()
    
    for i in report:
        new = i.split()
        reported[new[1]].add(new[0])
    
    # print(reported)
    for key, val in reported.items():
        if len(val) >= k:
            for v in val:
                answer[id_list.index(v)] += 1
    # print(answer)
    
    return answer