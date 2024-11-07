class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        d=defaultdict(int)
        folder.sort()
        ret=[folder[0]]
        prev=folder[0]
        for i in range(1,len(folder)):
            t=prev+'/'
            if folder[i].startswith(t):
                continue
            else:
                ret.append(folder[i])
                prev=folder[i]
        return ret

            