def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # Iterate and Push to Stack
        stack = []
        for elements in tokens:
            
            # Operand
            if elements not in '/*+-':
                stack.append(int(elements))
                
            # Operator
            else:
                right = stack.pop()
                left = stack.pop()
                
                # Eval:
                if elements == '+':
                    stack.append(left + right)
                    
                elif elements == '-':
                    stack.append(left - right)
                
                elif elements == '*':
                    stack.append(left * right)
                    
                elif elements == '/':
                    stack.append(left / right)
                    
        # Final Ans:
        return stack.pop()