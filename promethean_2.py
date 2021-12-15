Scale.default="prometheus"
Clock.bpm=110

ch.chords = P[(0,2,5,9),(1,3,6,10)]

print(SynthDefs)

sp >> saw(PWalk(), dur=PDur([3,[2,5]],[6,[7,9]])*2, amp=linvar([1/4,4/3],17), vib=linvar([1/2,6],17), room=10, formant=P[0:8])

s1 >> gong(PTri([5,0,4,3,1]), dur=var([3/9,2/7,4/5,PDur([6,5],9)],[36,28,30,18]), sus=P[36,28,30,18]/9, amp=linvar([1/6,1/2],P[9,7,10]*2), oct=(6,5,7), room=10, pan=linvar([-1,1],23))

p1 >> swell(ch.chords, sus=7, dur=[13,rest(7)], oct=(2,4,5,3), spin=linvar([0,7],3), room=10, echo=3.5).spread()

p2 >> glass(dur=7, amp=1/2).follow(p1).spread()

b1 >> jbass(p1.degree[0], sus=1, blur=1, dur=4, amp=1/2, room=10, stutter=3)

kd >> play("V", dur=PDur([3,[6,5]],9,P[0:3])*2, lpf=250, room=2).spread()

cp >> play("k", dur=5, coarse=13, hpf=4500, room=10, pan=PRand(-1,1), sample=PRand(10))
