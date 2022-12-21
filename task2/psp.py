def psp(n: int, open=0, close=0, answer='') -> str:
    if open + close == 2*n:
        print(answer)
        return
    if open < n:
        psp(n, open+1, close, answer+'(')
    if open > close:
        psp(n, open, close+1, answer+')')


psp(int(input()))
