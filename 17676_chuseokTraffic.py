def solution(lines):
    answer = 0
    if len(lines) == 1:
        return 1
    
    times = []
    for line in lines:
        h,m,s = map(float, line.split(" ")[1].split(":"))
        t = float(line.split(" ")[2].strip('s'))
        times.append((h*60*60+m*60+s-t+0.001,h*60*60+m*60+s))
        
    results = []
    for t in times:
        start = t[0]
        end = t[0] + 1
        tmp = 0
        for tt in times:
            if start <= tt[0] < end:
                tmp += 1
            elif start <= tt[1] < end:
                tmp += 1
            elif tt[0] <= start <= tt[1] and tt[0] <= end < tt[1]:
                tmp += 1
        results.append(tmp)
        
        start = t[1]
        end = t[1] + 1
        tmp = 0
        for tt in times:
            if start <= tt[0] < end:
                tmp += 1
            elif start <= tt[1] < end:
                tmp += 1
            elif tt[0] <= start <= tt[1] and tt[0] <= end < tt[1]:
                tmp += 1
        results.append(tmp)
    
    return max(results)
