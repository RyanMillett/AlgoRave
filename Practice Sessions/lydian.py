
Scale.default.set("lydian", tuning=Tuning.just)
Root.default=5

Clock.bpm=76

print(Scale.default)

ch.chords = var([0,-1,0,4,3,1],8)

print(SynthDefs)

s1 >> nylon(PRange(0,8,[1,2]) | PTri(8).arp([0,2]) | PRange(16).offadd(4,s1.dur/2), dur=var([1/2,1/4],[12,4]), amplify=1/2)

p1 >> soft(ch.chords, oct=5, sus=2, crush=linvar([0,[4,8]],16), vib=5, pan=PWhite(-1,1)) + P*(0,[2,2,3],4)

p2 >> ambi(ch.chords, dur=8, crush=linvar([0,[8,16]],32)).spread()

p3 >> charm(PWalk(), oct=6, dur=PDur([[3,6],5,[4,2,1]],8), amp=linvar([1/2,1],8), amplify=var([0,1],[8,16]), blur=1, vib=3, pan=PWhite(1,-1)) + (0,2)

p4 >> viola(ch.chords, dur=8, blur=1)

g1 >> bell(oct=6, dur=1, sus=4, amp=linvar([1/4,1],16), amplify=1/2, pan=[-1,1]).follow(p1)

g2 >> gong(ch.chords, dur=8, echo=.67, echotime=8) + (0,2,4,6)

sh >> play("s", dur=1/4, pan=[1,-1], amp=[1/2,2/3], sample=P[:3])

cl >> play("+", dur=p3.dur, sample=P[:5], pan=[1,-1])

hh >> play("---[-{-=}]", dur=1/2, pan=[-1,1])

bd >> play("(xk)((kI){o[ x]})", dur=1, sample=P[:5], echo=[0,0,0,.5], echotime=4).every(4, 'stutter', 2)

