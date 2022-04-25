#s + 1
#s + 3
#s * 4

def win_for_one_step(s, require_value):
    return (s + 3 >= require_value) or (s + 1 >= require_value) or (s * 4 >= require_value)

def lose_for_one_step(s, require_value):
    return ( not (win_for_one_step(s,require_value)) and win_for_one_step(s + 1, require_value) and win_for_one_step(s + 3, require_value) ) and win_for_one_step(s * 4, require_value)

def win_for_two_steps(s, require_value):
    return lose_for_one_step(4 * s,require_value) or lose_for_one_step(s + 1,require_value) or lose_for_one_step(s + 3, require_value)

def t19(s, require):
    return win_for_one_step(s + 1, require) or win_for_one_step(s + 3, require) or win_for_one_step(s * 4, require)  

def lose_for_two_steps(s, require):
    if ( win_for_one_step(s + 1,require) and win_for_two_steps(s + 3,require) and win_for_one_step(s * 4, require) ) or (win_for_one_step(s + 1,require) and win_for_two_steps(s + 3,require) and win_for_two_steps(s * 4, require)) or (win_for_one_step(s + 1,require) and win_for_one_step(s + 3,require) and win_for_two_steps(s * 4, require)) or (win_for_two_steps(s + 1,require) and win_for_one_step(s + 3,require) and win_for_two_steps(s * 4, require)) or (win_for_two_steps(s + 1,require) and win_for_one_step(s + 3,require) and win_for_one_step(s * 4, require)) or (win_for_two_steps(s + 1,require) and win_for_two_steps(s + 3,require) and win_for_one_step(s * 4, require)): 
        return True
    else:
        return False
    

def task_19(require_value, max_start):
    for s in range(1, max_start + 1):
        if (t19(s, require_value)):
            print(s)
            break
        
def task_20(require, max_start):
    for s in range(1, max_start + 1):
        if (win_for_two_steps(s, require)):
            print(s)
            
def task_21(require,max_start):
    for s in range(1, max_start + 1):
        if (lose_for_two_steps(s, require)):
            print(s)
            break

max_start = 77 # максимальное стартовое количество камней в куче
require = 78 #сколько камней должно быть в куче, чтобы подебить

task_19(require,max_start)
task_20(require,max_start)
task_21(require,max_start)