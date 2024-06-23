# started at 3:40
def solution(survey, choices):
    #     print(survey, choices)
    #     ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]
    types_list = ['R','T','C','F','J','M','A','N']
    types_dic = dict.fromkeys(types_list,0)
    for i in range(len(survey)):
        ls = survey[i].split()
        disagree,agree = ls[0][0], ls[0][1] 
        choice = choices[i]
        if 1 <= choice <= 3:
            score = 4 - choice
            types_dic[disagree] += score
        elif 5 <= choice <= 7:
            score = choice - 4
            types_dic[agree] += score               
    
    answer = []
    pairs = [['R','T'], ['C','F'], ['J','M'], ['A','N']]
    for i in range(4):
        type_1 = pairs[i][0]
        type_2 = pairs[i][1]
        
        type_1_score = types_dic[type_1]
        type_2_score = types_dic[type_2]
        if type_1_score < type_2_score:
            answer.append(type_2)
        else:
            answer.append(type_1)
    answer = "".join(answer)
    return answer
#fihished at 4:09