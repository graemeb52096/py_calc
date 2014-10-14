class function:
    '''
    This class takes mathamatical formulas (e.g. x^2 - 2x + 1)
    '''
    
    
    def split_function(self):
        operators = ['+', '-', '*', '/', '^']
        separators = [ ['[',']'], ['(', ')'] ]
        count = 0
        open_bracket = False
        for item in self.equation:
            for separator in separators:
                if item == separator[0]:
                    open_bracket =  True
                    expected_close_bracket_type = separator[1]
                    bracket_index = count + 1
                elif item == separator[1]:
                    if separator[1] == expected_close_bracket_type:
                        open_bracket = False
                        bracket_segment = self.equation[bracket_index : count]
                        self.split.append(bracket_segment)
                    else:
                        return ('Error: closing bracket does not follow open bracket')
            for operator in operators:
                if item == operator:
                    if not(open_bracket):
                        self.split.append(item)
            count += 1
                    
    def __init__(self, equation):
        self.equation = equation
        self.split = []
        
        
def split_equation(equation):
    open_brackets = []
    close_brackets = []
    segments = []
    operators = ['+', '-', '*', '/', '^']
    count = 0
    for item in equation:
        if item == '(':
            #open bracket
            open_brackets.append(count)
        elif item == ')':
            #close bracket
            close_brackets.append(count)
        count += 1
    
    print (open_brackets)
    print (close_brackets)  
    
    
my_func = function('((x*2)^2) * (2x) + (1)')
split_equation('((x*2)^2) * (2x) + (1)')



