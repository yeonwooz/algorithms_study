# 신고 결과 받기 - 프로그래머스
# 프로그래머스 92334 : 2022 KAKAO BLIND RECRUITMENT_신고 결과 받기

def solution(id_list, report, k):
    from collections import defaultdict
    answer = []
    report_dic = defaultdict(set) # key: 신고당한 유저 / value: 신고자 집합
    user_dic = defaultdict() # key: 유저 / value: 유저의 인덱스
    user_dic = defaultdict() # key: 유저 / value: 유저의 인덱스
    
    for i in range(len(id_list)):
        user_dic[id_list[i]] = i
        answer.append(0)

    # report를 확인하여 신고당한 유저별로 신고자를 집합에 저장함
    for r in report:
        reporter, bad_user = r.split()
        report_dic[bad_user].add(reporter)
        
    for reporter_lst in report_dic.values(): 
        if len(reporter_lst) >= k: # report_dic을 확인하여 만약 신고당한 횟수가 k를 넘으면?
            for reporter in reporter_lst:
                answer[user_dic[reporter]] += 1 # 신고자의 인덱스를 user_dic에서 받아와서 answer 해당 칸에 +1
    
    return answer