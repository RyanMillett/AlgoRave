Clock.bpm=72
Scale.default.set("prometheus", tuning=Tuning.just)
Root=7

print(SynthDefs)

ch.chords = var([5,[4,6],[2,3],[1,2],[0,-1]],[6,2,2,6,8])

sp >> sinepad(ch.chords, oct=5, dur=4, blur=1, sus=vx.dur, amp=linvar([0,1],16), amplify=2/3) + P*([4,[5,6],4],3,[2,[1,-1]],0)

sr >> sitar(PRange(0,5), oct=6, dur=1/6, amplify=var([0,1/4],[12,4]), blur=2, echo=.5, echotime=6).spread()

s1 >> varsaw(var([0,[2,[3,4]]],[12,4]), dur=4, blur=2, amp=linvar([1/2,1],16), amplify=2/3).spread()

s2 >> nylon(s1.degree[0], dur=[2,[4/3,1/2]], oct=6, sus=2, blur=1, crush=2, vib=PRand(12), amp=linvar([1/2,1],8), amplify=var([1/2,0],16)) + P*([0,[-1,-2]],2,[[3,5],4])

p1 >> glass(ch.chords, oct=(5,6), dur=ch.chords.dur, sus=p1.dur*3/2, fmod=PRand(6), dist=.05).spread()
p2 >> swell(ch.chords, oct=4, dur=2, sus=2, blur=3, amp=linvar([1/4,1],8), vib=PRand(5), crush=linvar([0,4],32)).spread()
p3 >> pasha(ch.chords + P*(0,1,[2,[3,4]],[-1,-2]), oct=var([5,[6,7]],[12,4]), dur=ch.chords.dur, blur=1, sus=1, amp=linvar([1/4,1],16), amplify=1/2)
p_all.room=1
p_all.mix=.7

g1 >> bell(ch.chords + P*([5,6,5],4,2,3,[1,0]), oct=var([5,[6,7]],[8,4]), dur=var([2/3,4/5],8), sus=6, fmod=PRand(6), amp=linvar([0,1],8), amplify=var([0,2/3],16), pan=linvar([-1,1],3))
g2 >> gong(ch.chords + (0,1,[2,3]), oct=4, dur=8, echo=1/3, echotime=8, fmod=PRand(12), blur=2, amplify=var([0,2],16)).spread()
g_all.room=1
g_all.mix=.6

b1 >> jbass(PWalk(), dur=PSum([5,[3,6],4],8), blur=1, crush=4)
tm >> play("<mm(Mm)>< s>", dur=PDur([[3,5],4],8), pan=[-1,1], crush=4, sample=PRand(5), pshift=P[:5])

tt >> play("#", dur=16, echo=.67, echotime=12, room=1, mix=1, rate=2/3, crush=3, sample=PRand(3)).spread()

db >> play("X", dur=8, room=1, mix=.6, echo=.33, echotime=6, amplify=var([0,1],16), dist=linvar([0,[.5,.67]],32), crush=2)

Master().lpf=linvar([850,[6_500,1_500]],27)
Master().lpr=linvar([.1,1],13)

Master().room=1
Master().mix=linvar([.2,1],36)

Master().echo=linvar([2/3,1/12],13)
Master().echotime=9

Master().crush=linvar([0,[16,64]],41)
Master().bits=linvar([32,[8,4]],52)

Master().dist=linvar([0,.75],27)

Master().spread()
Master().pshift=(linvar([-1/6,-2/3],17),linvar([1/5,5/6],13))


