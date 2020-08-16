import re
def solve(N,M,Words,Q,Query):
    res=[]
    text = " ".join(Words)
    #print(text)
    for i in range(Q):
        tempstr = "".join(Query[i])
        if(tempstr.count('?')==M):
            res.append(N)
        else:
            strtem = tempstr.replace('?',"\w")
            #print(strtem)
            pattern = str(strtem)
            #print(pattern)
            count = len(re.findall(pattern,text))
            res.append(count)
    return res

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    Words = []
    for _ in range(N):
        Words.append(input())
    Query = []
    Q = int(input())
    for _ in range(Q):
        Query.append(input())

    result = solve(N,M,Words,Q,Query)
    print(result)