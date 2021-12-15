Clock.bpm=92
Scale.default.set("indian", tuning=Tuning.just)

print(SynthDefs)

Clock.reset()

prog1 = var([0,2,[3,1],[1,[-1,-3]]],4)

A = var([1,0],16)
B = var([0,1],16)

p1 >> space(prog1, oct=5, dur=[2,3], sus=p1.dur/2, pan=[1,-1]) + P*(0,2,4,[2,3])
p2 >> blip(prog1, oct=5, dur=[3,2], sus=var([p2.dur/2,p2.dur*3],8), pan=[-1,1]) + P*(0,1,3,[1,2])
Group(p1,p2).amplify=A

p3 >> sinepad(prog1 + [0,0,[1,1,[4,5]],0,[2,3]], oct=var([6,5],[16,8]), dur=1/4, sus=2, pan=PWhite(-1,1), amp=1/2, amplify=B)

p_all.room=10

p_all.hpf=linvar([0,1100],8)

d1 >> play("{Pm}", dur=PDur([5,7,8,[3,6]],8), sample=P[:20].shuffle(2), pshift=-1/2, rate=var([2/3,1/2,3/4],[4,2,8]), pan=[-1,1], room=3)

d2 >> play("(kH)(k[ k])", room=5, sample=P[:20], delay=0, pan=[-1,1])

d3 >> play("s", dur=1/3, sample=P[:20], pan=[-1,1])

d_all.lpf=linvar([250,9_000],32)
d_all.lpr=linvar([.1,1],8)
