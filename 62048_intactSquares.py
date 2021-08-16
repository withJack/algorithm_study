def solution(w,h):
    answer = 1
    
    nw = w
    nh = h
    while nw != nh:
        if nw > nh:
            nw -= nh
        else:  
            nh -= nw
    
    return w*h - (w+h-nh)
