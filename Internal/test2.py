from sys import _getframe

class LogTag:
    Branch = 'Branch'
    Condition = 'Condition'
    EndBranch = 'EndBranch'
    
    Loop = 'Loop'
    Iteration = 'Iteration'
    EndLoop = 'EndLoop'
    
    Script = 'Script'
    EndScript = 'EndScript'
    
    def Test(self):
        print _getframe(1).f_code.co_name
