class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s1 = abc
        #[lec]abee, l[eca]bee, le[cab]ee
        dq = deque(s2[:len(s1)])
        count = 0
        if sorted(dq) == sorted(s1):
            return True

        for i in range(len(s1), len(s2)):
            dq.popleft()
            dq.append(s2[i])  
            if sorted(dq) == sorted(s1):
                return True            
                
        return False

