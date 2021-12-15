Clock.bpm=66
Clock.time_signature=9/4
Scale.default="prometheus"

n1 >> noise(dur=3, sus=3, room=10, echo=1.33, echotime=6, pan=linvar([-1,1],13), amp=linvar([0,[2/3,1/2]],18), lpf=linvar([150,2500],6))

g1 >> gong(PRange(-6,12,[[1,2],3]), oct=[4,5,6], echo=.33, echotime=3, dur=var([1/3,1/5],9), sus=6, amp=var([1/3,0],[18,36]), pan=[-1,1], vib=PRand(3,12), fmod=PRand(-3,3), room=5)

p1 >> glass(oct=[3,4,5,6], dur=3, sus=3, room=10, pan=linvar([-1,1],8), amplify=1, fmod=linvar([0,-3,3],23)) + (0,1,2,3,4,5)

p2 >> prophet(var([0,5],16), oct=(2,3,4), dur=3, sus=4, amp=linvar([0,2/5],16), shape=linvar([0,1],64)).spread() + var([(0,1,3,5),(2,4,6,8)],18)

p3 >> swell(oct=(5,6), crush=linvar([0,1],18), dur=9).spread().follow(p2)

d1 >> play("<k><  +>", dur=PSum([4,3,7],9)/2, room=10, echo=1/6, echotime=6, rate=1/2, sample=PRand(20), pshift=P[0:8], hpf=1500)

d2 >> play("{mM}", dur=PDur([5,3],9), sample=PRand(20), pan=[-1,1], room=5).sometimes('stutter',5,rate=3)

d3 >> play("V", lpf=linvar([250,2500],36))

s1 >> saw(PWalk(), dur=PDur([[3,6],[5,7,9]],9)*2, blur=1, oct=(5,6), vib=PRand(0,12), amplify=1, formant=P[0:8], crush=linvar([0,16],36))

