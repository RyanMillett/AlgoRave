Scale.default="bebopMelMin"


Clock.time_signature=7/4
Clock.bpm=110

p1 >> play("$", dur=PDur([3,5],7), sample=PRange(0,20)).every([13.5,6.5], 'stutter', 3, pan=[-1,1], rate=5, amplify=linvar([0,1/3],14))
p1.room=var([0,10],[5,1])
p1.lpf=linvar([1500,7500],7)
p1.lpr=linvar([1,.1],3)

p2 >> play("k", sample=PRand(0,20), dur=PDur([6,4],7, PRange(10)), room=5, hpf=linvar([5000,0],14), pan=[1,-1]).sometimes('stutter', 1.5, rate=5)

p3 >> play("m", sample=PRange(20), pan=[-1,1], dur=PDur([5,4,3,2],7))

p4 >> play(var(["{HSI}","<{*&}><+>"],[28,14,7]), sample=PRange(20), pan=[1,-1], dur=PDur([5,4,3,2],7)*2, pshift=P[8], echo=1.5)

print(SynthDefs)

v1 >> jbass(var([0,3,0,5,4,2,-1],7), dur=PSum([8,4,6],7), lpf=750)

prog=var([(0,2,4),(3,5,7)],14)

v2 >> piano(var([0,3,0,5,4,2,-1],7), oct=(5), dur=PSum([4,6,3],7)) + prog

