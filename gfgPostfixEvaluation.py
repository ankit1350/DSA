class Solution:
    def evaluatePostfix(self, arr):
        # code here
        stack=[]
        for token in arr:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                if len(stack)<2:
                    raise ValueError("Invalid Postfix Expression")
                b=stack.pop()
                a=stack.pop()
            
                if token=="+":
                    stack.append(a+b)
                elif token=="-":
                    stack.append(a-b)
                elif token=="*":
                    stack.append(a*b)
                elif token=="/":
                    stack.append(a//b)
                elif token=="^":
                    stack.append(a**b)
                else:
                    raise ValueError("unknown error")
        if len(stack)!=1:
            raise ValueError("Invalid Postfix Expression")
        return stack[0]