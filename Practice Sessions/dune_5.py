Scale.default="wholeHalf"
Root.default=3

Clock.bpm=76

print(SynthDefs)

p1 >> dirt(oct=(4,5), dur=2, sus=3, amp=linvar([0,1],16), hpf=linvar([0,4500],5), hpr=linvar([.1,1],3), pan=linvar([-1,1],7), room=10, echo=2/3,echotime=6)

p2 >> noise(dur=3, amp=linvar([0,1],9), amplify=1/3, lpf=linvar([500,4500],7), lpr=linvar([.1,1],5), pan=linvar([-1,1],3), room=10)

p3 >> ripple(oct=4, dur=5, sus=8, shape=linvar([0,1],23), amp=linvar([0,1],19), amplify=1/2, room=10, echo=1, echotime=5, spin=9).spread()

s1 >> varsaw(PRange(8), oct=(4,5), dur=5, blur=1, amp=linvar([0,1],31), vib=PRand(12), crush=linvar([0,31],54)).spread()

s2 >> saw(PWalk(), dur=5, formant=P[0:8], room=5)

d1 >> play("m", dur=PDur([7,5],9), sample=PRand(20), rate=1, pshift=P[0:9], pan=[-1,1], room=3).sometimes('stutter', 2, rate=3)

d2 >> play("<+><A>", dur=PSum([7,5],9), room=8, sample=P[0:8], amp=1/2)

d3 >> play("V")

