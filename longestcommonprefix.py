def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        mini=min(strs)
        for i in range(0,len(mini)):
            for j in strs:
                if j[i]!= mini[i]:
                    return(res)
            res+=mini[i]
        return(res)
