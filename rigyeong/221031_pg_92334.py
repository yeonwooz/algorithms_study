#맞았습니다!
def solution(id_list, report, k):
    answer = [0] * len(id_list) 
    dict = {id : [] for id in id_list}
    id_dict = {id : idx for idx, id in enumerate(id_list)}
    
    for r in set(report):
        user = r.split()[0]
        reported = r.split()[1]
        dict[reported].append(user)
    
    for key in dict.keys():
        if len(dict[key]) >= k:
            for a in dict[key]:
                answer[id_dict[a]] += 1
    return answer