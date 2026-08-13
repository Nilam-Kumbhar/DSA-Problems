class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        st=[]

        for i in range(n):
            if(s[i]=='(' or s[i]=='{' or s[i]=='['):
                st.append(s[i])
            else:
                if(st):
                    if(s[i]==')' and st[-1]=='('):
                        st.pop() 
                    elif(s[i]=='}' and st[-1]=='{'):
                        st.pop()  
                    elif(s[i]==']' and st[-1]=='['):
                        st.pop()
                    else:
                        return False 
                        exit()     
                else:
                    return False
                    exit()        
        if not st:
            return True    
        else:
            return False                     
        