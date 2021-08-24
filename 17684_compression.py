from collections import deque
def solution(msg):
    answer = []
    zxw_dict = { chr(i+64):i for i in range(1,27) }
          
    msg = deque(list(msg))
                    
    while msg:
        curr = msg.popleft()
        if len(msg) == 0:
            answer.append(zxw_dict[curr])
            break
        while True:
            if msg and curr in zxw_dict.keys():
                tmp = msg.popleft()
                tmp_out = zxw_dict[curr]
                curr += tmp
                continue
            elif curr not in zxw_dict.keys():
                zxw_dict[curr] = len(zxw_dict.keys()) + 1
                msg.appendleft(tmp)
                break
            elif not msg:
                tmp_out = zxw_dict[curr]
                break

        answer.append(tmp_out)
    return answer
