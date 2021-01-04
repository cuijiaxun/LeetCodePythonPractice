class Solution:
    def decodeString(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        """Solution 1: Using one stack O(max K^{coutK} *n)"""
        code = [char for char in s]
        decode = []
        #if len(s) <= 3: return ""
        i=0
        while i < len(code):
            if code[i].isdigit():
                n=[]
                while code[i].isdigit():
                    n.append(code[i])
                    i+=1
                num=''.join(x for x in n)
                decode.append(num)
                continue
            elif code[i] != "]":
                decode.append(code[i])
            else:
                local = []
                while decode[-1] != "[":
                    last = decode.pop(-1)
                    #if last not in["[","]"]:
                    local.insert(0,last)
                local_string = ''.join(e for e in local)
                decode.pop(-1)
                number = int(decode.pop(-1))
                local_string_syn = ''
                for j in range(int(number)):
                    local_string_syn += local_string 
                decode.append(local_string_syn)
            i+=1
        result = ''.join(str(e) for e in decode)
        return result
