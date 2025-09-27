import re
class Solution:
    def infixtoPostfix(self, s):
        #code here
        prec={"^":4,"*":3,"/":3,"+":2,"-":2,"(":1}
        stack=[]
        postfixlist=[]
        tokenlist=re.findall(r'[A-Za-z0-9]+|[\^*/+\-()]',s)
        for token in tokenlist:
            if token.isalnum():
                postfixlist.append(token)
            elif token=="(":
                stack.append(token)
            elif token==")":
                toptoken=stack.pop()
                while toptoken!="(":
                    postfixlist.append(toptoken)
                    toptoken=stack.pop()
            else:
                while (stack and stack[-1]!="(" and ((token!="^" and prec[stack[-1]]>=prec[token])or (token=="^" and prec[stack[-1]]>prec[token]))):
                    
                    
                    postfixlist.append(stack.pop())
                stack.append(token)
        while stack :
            postfixlist.append(stack.pop())
        return "".join(postfixlist)