Scale.default="egyptian"

Root.set=var([0,2,5,1],13)

seq = var([5,4,0,1],[7,3,2,9])

s1 >> gong(PWalk(), sus=2, blur=1, oct=5, pan=linvar([-1,1],9), amp=1/2)
s1.dur=var([[1,1/3,1/5],PDur(P[3,5,2]*2,17)],9,17)
s1.vib=var([0,linvar([0,6],7)],11)

s2 >> bell(s1.degree + (4,7), sus=1/3, dur=PDur(7,9), amp=1/5, oct=(5,6), spin=linvar([1,9],15)).stop()

p1 >> prophet(seq, sus=1, blur=p1.sus*1.5, oct=(3,4,5)).spread().stop()
p1.amp=linvar([0,1],29)
p1.spin=linvar([0,9],17)

b1 >> bass(seq, chop=linvar([2,7],13), pan=linvar([-1,1],31), amp=2/3).spread().stop()
b1.hpf=linvar([250,1500],11)

d_all.stop()

d1 >> play("V-", amp=2/3).spread().sometimes('stutter',1.5)
d1.lpf=linvar([200,2500],27)
d1.lpr=linvar([1,.1],31)
d1.amp=linvar([1/5,4/7],23)

d2 >> play("k", dur=PDur([5,7,0,9,0],14), pan=PRand(-1,1), sample=PRand(10)).sometimes('stutter',3)
d2.hpf=linvar([500,5000],27)
d2.hpr=linvar([1,.1],31)
d2.pshift=P[0:8]
d2.amp=3/5

d3 >> play(".S.([&&])(.[hk])", dur=1/2, room=3, sample=PRand(10), amp=1/3, spin=PRand(7), pan=PRand(-1,1)).sometimes('stutter',5).sometimes('rotate').stop
d3.formant=P[0:8]
d3.pshift=P[0:8].shuffle()
