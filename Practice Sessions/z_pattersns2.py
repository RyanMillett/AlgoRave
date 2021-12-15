print(Scale.names())

Scale.Root=5

Scale.default="justMinor"

Clock.bpm=126


sPat=P[3,9,2,7,1,6]

print(sPat.offadd(2,.50))

A = var([1,0],[12*6,12])

Group(p1).solo()

g1 >> ambi(dur=6, sus=3, oct=(3,4,5)).spread() + [(0,2,4),(3,5,7),(-2,1,3)]

s1 >> gong(PWalk(), oct=(6,5), sus=2, blur=1, dur=PDur([6,7],9), pan=linvar([-1,1],6), amplify=1.5, fmod=linvar([-6,6],36))

b1 >> bass(PWalk(), room=2, dist=1,dur=[2/3,1/3], blur=1, lpf=4000)

p1 >> saw(PWalk(), oct=(4), vib=PRand([0,12]), amp=1/2, dur=1, blur=1, room=5, shape=linvar([0,1],24), format=P[0:8])

p2 >> blip(oct=5, sus=2, dur=PDur([2,4,5,3],6)*2, room=7).follow(g1)

hh >> play("<[--(*[-=])]><& K>", dur=1, sample=PRand(10), room=3, rate=PRand(1,10))

sh >> play("+", hpf=linvar([500,2500],18), room=5, pan=[-1,1], dur=1, coarse=3, sample=PRand(10))

tm >> play("s", hpf=linvar([500,2500],18), room=2, pan=[-1,1], dur=PDur([3,5],8), sample=PRand(10), pshift=(P[0:8].shuffle()))

bd >> play("V  ", lpf=linvar([250,4500],16)).spread()

d1 >> play("shroom", pan=PRand(-1,1), shape=linvar([0,2],17), rate=PRand(1,6))

Group(hh,sh,tm,bd,d1).lpf=4500
