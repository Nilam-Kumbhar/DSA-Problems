class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp={}
        j=0
        mx=0

        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i],0)+1

            while( mp[s[i]]>1):
                mp[s[j]]-=1
                j+=1
            mx=max(mx,i-j+1)   
        return mx     


        # n=len(s)
        # substring={}
        # count=0
        # for i in s:
        #     if i in substring:
        #         substring[i] +=1
        #     else:
        #         substring[i] = 1

        # for key,value in substring.items():
        #     if(key): 
        #         count+=1
        # return count              
        