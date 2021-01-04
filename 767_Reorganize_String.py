import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        #Greedy method, Use heap to store value and sort by the count
        char_S = [s for s in S]
        #print(char_S)
        dict_S = {}
        for i in range(len(char_S)):
            if char_S[i] not in dict_S.keys():
                dict_S[char_S[i]] = 1
            else:
                dict_S[char_S[i]] += 1
        chars = []
        rep = []
        dict_S = sorted(dict_S.items(), key=lambda x: x[1], reverse=True)
        h = []
        for (key, value) in dict_S:
            chars.append(key)
            rep.append(value)
            heapq.heappush(h, (-value, key))
        #print(chars,rep, h)
        max_rep = rep[0]
        sum_rest_rep = 0
        for i in range(1, len(rep)): sum_rest_rep+=rep[i]
        if sum_rest_rep < max_rep - 1:
            return ''
        res = []
        while len(h) > 0:
            repetition,candidate = heappop(h)
            #print(candidate,-repetition)
            h.sort()
            #print(h)
            res.append(candidate)
            if len(h) > 0:
                repetition_2,candidate_2 = heappop(h)
                #print(candidate_2,-repetition_2)
                res.append(candidate_2)
                if repetition_2 + 1<0:
                    heapq.heappush(h,(repetition_2+1,candidate_2))
            if repetition + 1<0:
                    heappush(h,(repetition+1, candidate))
            #print(h)
        res = ''.join(s for s in res)
        return res
