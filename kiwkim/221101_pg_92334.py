

def solution(id_list, report, k):
    from collections import defaultdict
    dic = defaultdict(set)
    answer = []
    user_idx = defaultdict()
    for i in range(len(id_list)):
        answer.append(0)
        user_idx[id_list[i]] = i
    for rep in report:
        usr, bad = rep.split()
        dic[bad].add(usr)
                
    for key in dic.values():
        if len(key) >= k:
            for r in key:
                answer[user_idx[r]] += 1
    return answer