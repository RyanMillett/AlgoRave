Scale.default="indian"
Clock.bpm=92

sPat1 = P[0,1,0,2,3,5,4]

lSeq = var([PDur([5,7,8],9),[1/4,1/6]],[18,9])
p1 >> blip(PWalk(), dur=lSeq, sus=2, oct=5, pan=[-1,1], shape=linvar([0,.25],36), vib=PRand(0,6))
p1.amp=linvar([1/8,1/3],9)
p1.amplify=2/3

cSeq = P[0,3,2,1,4,5]
p2 >> gong(cSeq, dur=9, sus=6, fmod=PRand(-1,1), spin=9, oct=(6,7)) + [(0,2,4),(1,3,5)]
p2.amp=2/3

b1 >> jbass(sPat1, sus=1/4, dur=PDur([5,7,6],9), amp=1, pan=0)

d1 >> play("m", dur=b1.dur, room=1, sample=PRand(10), pan=[-1,1])

d2 >> play("{s+}", dur=1/6, room=5, hpf=1200, amp=linvar([0,1/2],9), spin=18, sample=PRand(10))

bd >> play("Vk", lpf=500).spread()
