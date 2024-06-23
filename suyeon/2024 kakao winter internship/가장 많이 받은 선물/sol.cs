using System;
using System.Collections.Generic;

/* 다른 사람 풀이 참고 */
public class Solution {
    public int solution(string[] friends, string[] gifts) {
        int answer = 0;
        
        var dict = new Dictionary<string, int>();  // 친구 이름, 인덱스
        for (int i = 0; i < friends.Length; i++)
        {
            dict.Add(friends[i], i);
        }
        
        var intArray = new int[friends.Length];  // 선물지수배열
        var giftArrays = new int[friends.Length, friends.Length];  // giver-taker 배열
        
        for (int i = 0; i < gifts.Length; i++)
        {
            string[] strs = gifts[i].Split(' ');
            var giverIndex = dict[strs[0]];
            var takerIndex = dict[strs[1]];
            giftArrays[giverIndex, takerIndex]++;   // giver-taker 배열 업데이트
            intArray[giverIndex]++;  // 준 사람의 선물지수 증가
            intArray[takerIndex]--;  // 받은 사람의 선물지수 감소
        }
        
        for (int i = 0; i < intArray.Length; i++)
        {
            int num = 0; // 선물 받은 개수
            for (int j = 0; j < intArray.Length; j++)
            {
                if (i == j)
                {
                    continue;
                }
                
				// 선물을 받아야 하는 조건
                if (giftArrays[j,i] < giftArrays[i,j]  // i 가 준 선물 개수가 더 많거나
                   || giftArrays[j,i] == giftArrays[i,j] && intArray[i] > intArray[j] // 준 선물 개수가 같고 i의 선물지수가 더 많으면
                   )
                {
                    num++;
                }
            }
                
            if (answer < num)  // 최대값 갱신
            {
                answer = num;
            }
        } 
         
        return answer;
    }
}