def solution(m, musicinfos):
    answer = ''
    musics = [0,0]
    
    mel = []
    for n in list(m):
        if n == "#":
            last = mel.pop()
            mel.append(last+"#")
        else:
            mel.append(n)
    m = mel
    
    for music in musicinfos:
        rec = music.split(",")
        time = int(rec[1].split(":")[0])*60 + int(rec[1].split(":")[1]) - int(rec[0].split(":")[0])*60 - int(rec[0].split(":")[1])
        name = rec[2]
        
        melody = []
        for n in list(rec[3]):
            if n == "#":
                last = melody.pop()
                melody.append(last+"#")
            else:
                melody.append(n)

        one_rep = len(melody)
        reps, rest = divmod(time, one_rep)
        tmp = melody * reps + melody[:rest]
        
        m_len = len(m)
        for i, t in enumerate(tmp):
            if t == m[0]:
                if tmp[i:i+m_len] == list(m):
                    if musics[1] < time:
                        musics = [name, time]
                        break

    if musics[0] == 0:
        return '(None)'
    return musics[0]
