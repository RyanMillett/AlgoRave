Scale.default="prometheus"
Clock.bpm=92

d1 >> play("<{k[ssss]}><{+S}>", dur=1/2, sample=PRand(20), pan=[1,-1]).every(8, 'stutter', cycle=3).every(5, 'reverse',ident=1)
d1.shape=linvar([.1,.75],8)
d1.lpf=1500

d2 >> play("({mM}(:%))", dur=PDur([3,5],8), room=1/2, sample=PRand(10), pan=PRand(-1,1)).every(8.5, 'stutter', 2)
d2.echo=.33
d2.echotime=1.5

bd >> play("V(-[-{-[-=]}])", lpf=linvar([250,4500],16))

b1 >> jbass(PWalk(), oct=4, dur=PDur([5,3,4],8)*2, hpf=250).slider()

p1 >> blip(PRange(-6,[12,24],[1,3]), dur=1/4, amp=linvar([0,1/4],8), room=10, sus=4, shape=linvar([.05,.55],16), pan=linvar([-1,1],5), vib=PRand(0,12), lpf=1500) 

p2 >> prophet(var([0,[3,5]],16), oct=(3,4,5), dur=[12,rest(4)], formant=P[0:8], room=10, vib=linvar([0,12],4)).spread()
p2.shape=linvar([0,.1],16)
p2.echo=6
p2.echotime=12
p2.lpf=linvar([250,4500],32)
