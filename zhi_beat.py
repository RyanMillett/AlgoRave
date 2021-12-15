def morph(c1,c2,dur):
    n = c1
    result = [n]
    for i in range(dur-1):
        n += (c2-c1)/dur
        result.append(n)
    result.append(c2)
    return result
    

s1 = P[0,2,4,3,1,-1]
s2 = P[9,7,5,8,6,4]
mrph = Pattern(morph(s1,s2,18))

print(mrph)

Scale.default.set("zhi", tuning=Tuning.just)

mel = s1 | s2

s1 >> saw()

p1 >> swell(mel | mel.invert(), dur=PSum([[4,3],[5,[7,6]]],9)*6, oct=var([4,5],36), sus=p1.dur, blur=1.5, room=1, mix=linvar([.1,1],18), echo=2/3, echotime=9).spread() + (0,4)

p2 >> klank(dur=3, blur=2, room=1, mix=1, shape=.4).follow(p1).spread()

p3 >> pasha(mel, dur=PDur([7,[5,[4,8]]],9), hpf=linvar([350,2500],32), hpr=linvar([.1,1],9), pan=PWhite())

d1 >> play("V", dur=1, lpf=linvar([350,2500],13))

d2 >> play(" [-(-[--])-(-[----])]", dur=2, pan=[-1,1], sample=P[:10], crush=linvar([0,[16,32]],7), shape=linvar([.1,.9],13))

