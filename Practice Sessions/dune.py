Clock.bpm=66
Scale.default="prometheus"

p1 >> glass(oct=(3,4,5,6), dur=1, sus=3, room=10, pan=linvar([-1,1],8), amplify=1/4) + (0,1,2,3,4,5)

p2 >> prophet(var([0,5],16), oct=(2,3,4), dur=1, sus=4, amp=linvar([0,2/5],16), shape=linvar([0,1],64)).spread() + [(0,1,3,5),(2,4,6,8)]

p3 >> swell(oct=(5,6), crush=linvar([0,1],18), dur=9).spread().follow(p2)

d1 >> play("k", dur=PSum([4,3,7],9), room=10, echo=1/6, echotime=6, rate=1/2, sample=PRand(20), pshift=P[0:8])

d2 >> play("{mM}", dur=PDur([5,3],9), sample=PRand(20), pan=[-1,1], room=5).sometimes('stutter',5,rate=3)

d3 >> play("V", lpf=250)

s1 >> saw(PWalk(), dur=PDur([[3,6],[5,7,9]],9), blur=1, oct=6, vib=6, amplify=1, formant=P[0:8])

