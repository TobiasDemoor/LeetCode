class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = [c for c in senate]
        vetoedDires = 0
        vetoedRadiants = 0
        while len(queue) > max(vetoedDires, vetoedRadiants):
            e = queue.pop(0)
            if e == 'R':
                if vetoedRadiants > 0:
                    vetoedRadiants -= 1
                else:
                    vetoedDires += 1
                    queue.append(e)
            else:
                if vetoedDires > 0:
                    vetoedDires -= 1
                else:
                    vetoedRadiants += 1
                    queue.append(e)
        if queue[0] == 'R':
            return 'Radiant'
        else:
            return 'Dire'



sol = Solution()
print(sol.predictPartyVictory('DR'))
print(sol.predictPartyVictory('DDR'))
# print(sol.predictPartyVictory('DRD'))
# print(sol.predictPartyVictory('D'))
print(sol.predictPartyVictory("DDRRR"))
