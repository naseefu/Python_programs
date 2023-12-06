class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        s = []

        for i in asteroids:
            while s and i<0 and s[-1]>0:
                if abs(i)>s[-1]:
                    s.pop()
                elif abs(i)==s[-1]:
                    s.pop()
                    break
                else:
                    break
            else:
                s.append(i)
        return s