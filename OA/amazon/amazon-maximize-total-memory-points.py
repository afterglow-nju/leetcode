
class Solution:
  def maximizeTotalMemoryPoints(self, memory: List[int]) -> int:
    memory.sort(reverse=True)
    pre=[memory[0]]*len(memory)
    for i in range(1,len(memory)):
      pre[i]=pre[i-1]+memory[i]
    return sum(pre)