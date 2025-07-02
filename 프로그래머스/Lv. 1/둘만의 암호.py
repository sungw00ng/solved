def solution(s, skip, index):
    result=""
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
    skip=list(skip)
    #26-len(skip)
    for i in skip:
        alphabet.remove(i)
    print(alphabet)
    s=list(s)
    for i in s:
        idx=alphabet.index(i)
        result+=alphabet[(idx+index)%(26-len(skip))]
    return result
