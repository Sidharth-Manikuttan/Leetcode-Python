class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        start_l = [i for i in range(len(start)) if start[i] == 'L']
        start_r = [i for i in range(len(start)) if start[i] == 'R']
        target_l = [i for i in range(len(target)) if target[i] == 'L']
        target_r = [i for i in range(len(target)) if target[i] == 'R']
        
        for (s_pos, t_pos) in zip(start_l, target_l):
            if s_pos < t_pos:
                return False
        
        for (s_pos, t_pos) in zip(start_r, target_r):
            if s_pos > t_pos: 
                return False
        
        return True
