Scale.default.set("halfWhole", tuning=Tuning.just)
Root=7
Clock.bpm=72
Clock.time_signature=9/4

print(Scale.default)

print(SynthDefs)

s1 >> varsaw([0,[2,2,1],[5,6]] + var([0,[1,-1]],9), oct=(4,5), blur=1, dur=9, amp=1/2).spread()

p1 >> glass((0,[2,2,1],[5,6]) + var([0,[1,-1]],9), oct=PRand(3,6), dur=6, sus=9, root=7).spread()

p2 >> swell(p1.degree[0], oct=4, dur=3, sus=9, amp=linvar([0,1/2],18), lpf=linvar([150,2500],18*2), crush=linvar([0,8],21)).spread()

p3 >> prophet(root=0, oct=4, dur=7, shape=linvar([0,.33],36), amp=linvar([1/4,2/3],18)).spread()

p_all.room=10

f1 >> gong(PRange(0,9) | PTri(9), oct=[6,5,7], amp=linvar([0,1],18), pan=linvar([-1,1],5), dur=1/6, sus=6)

b1 >> jbass([0,[2,6],[3,4,5]], dur=PDur([[5,7],3],9), amp=linvar([0,1],6), lpf=linvar([250,1500],36), blur=1, slide=.05, dist=linvar([0,.15],18))

d1 >> play("m", dur=PDur([[5,7],3],9), pan=[1,-1], sample=PRand(10), pshift=P[0:9], room=5, dist=.05, rate=1/2)

d2 >> play("  s", room=7, sample=PRand(20), amp=2/3, echo=.5, echotime=5)

bd >> play("V", dur=9, room=5, dist=.15, echo=.33, echotime=6, lpf=800)
