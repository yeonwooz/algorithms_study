def solution(id_list, report,k):
    answer = []
    report = set(report) # 중복 신고 제거
    # reporters = defaultdict(set) # 이메일 보낼 대상들 (초기값 => [])
    # reported_cnts = defaultdict(int) # 신고당한 횟수 (초기값  => 0)
    reporters = {id: [] for id in id_list}
    reported_cnts = dict.fromkeys(id_list, 0)
    
    for r in report:
        cur_user, reported = r.split()
        # 신고자가 신고한 id 추가
        reporters[cur_user].append(reported)
        # 신고당한 id의 신고 횟수 추가
        reported_cnts[reported] += 1
    
    for i in id_list:
        reporting_targets = reporters[i]  # i번째 유저가 신고한 대상들
        cnt = 0   # 신고한 대상들 중 몇명이 정지될까?
        for target in reporting_targets:  
            if reported_cnts[target]>=k: # 이번 대상이 정지되었다
                cnt += 1     
        answer.append(cnt)
    return answer