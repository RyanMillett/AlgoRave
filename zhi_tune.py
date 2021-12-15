Clock.bpm=92
Scale.default.set("zhi", tuning=Tuning.just)

print(SynthDefs)

seq = var([0,3,2,[4,1]],[8,4,2,2])

s1 >> bell(seq, dur=var([2,[3,3/2]],12), sus=5, blur=1, vib=3, oct=(6,7), amp=linvar([0,1],12), amplify=var([0,1/2],24)) + P*([5,4],[3,[2,4]],[1,[0,-1]])

s2 >> saw(PWalk(), dur=var([4,[1/2,1/3]],[16,8]), sus=s2.dur, oct=5, blur=1, vib=PRand(6), pan=linvar([-1,1],5)) + var([0,[1,[3,[5,4]]]],8)

p1 >> klank(seq, oct=4, dur=1, amp=linvar([1/4,1],34), lpf=linvar([250,10000],55), lpr=linvar([.1,1],34)).spread()

p2 >> swell(seq, dur=5, sus=8, amp=linvar([1/4,1],89), lpf=linvar([250,10000],21), lpr=linvar([.1,1],13)).spread()

p3 >> blip(seq, dur=seq.dur, sus=4, pan=PWhite(-1,1), vib=PRand(6), crush=0, amplify=1/2) + P*([[0,7],0,[-1,-2]],[2,8,4,2],[1,[4,2]])

p_all.room=10
p_all.crush=linvar([0,8],16)

n1 >> noise(dur=8, sus=13, amp=linvar([0,1],55), lpf=linvar([250,10000],8), lpr=linvar([.1,1],5), pan=linvar([-1,1],3), amplify=1/2, echo=.33, echotime=13, crush=linvar([0,64],144))

dr >> glass(oct=PRand(4,7), dur=5, sus=8, amp=linvar([1/4,1],34), amplify=1.5, room=10, echo=1.33, echotime=13, spin=2).spread() + P*(0,[1,5],2,[3,6,7],[4,0,[2,3],0,1])

b1 >> jbass(seq, dur=PDur([7,7,[5,3]],8), blur=1, amp=linvar([1/2,1],13), crush=linvar([0,4],21))

d1 >> play("mm(c(hk))", dur=PDur(3,8), sample=P[:5], pan=[-1,1])

d2 >> play(" S", dur=2, room=5)

d3 >> play(" I", dur=2, room=5)

bd >> play("V-").sometimes('stutter', 2)


