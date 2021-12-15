print(Scale.names())

Scale.default="bebopMaj"

Clock.bpm=126


sPat=P[3,9,2,7,1,6]

print(sPat.offadd(2,.50))

A = var([1,0],[12*6,12])

Group(p1).solo()

s1 >> gong(PWalk(), oct=(6,5), sus=2, blur=1, dur=PDur([6,7],9), pan=linvar([-1,1],6), amplify=1.5, fmod=linvar([-6,6],36))

b1 >> jbass(sPat, dur=PDur([[6,3],[5,7,8]],9)*2, blur=1, lpf=1000)

p1 >> saw(sPat, oct=(4,5), vib=PRand([0,12]), amp=A, dur=3, blur=1, room=5, shape=linvar([0,1],24), format=P[0:8])

p2 >> blip(sPat, chop=18, dur=6, room=7, amplify=1.5).spread() + (0,[2,1,3],[[4,3],5,7])

hh >> play("<[--(*[-=])]><& K>", sample=PRand(10), room=3, rate=PRand(1,5))

sh >> play("{sH}", room=5, pan=[-1,1], dur=1/3, coarse=3, sample=PRand(10))

tm >> play("m", room=2, pan=[-1,1], dur=s1.dur, sample=PRand(10))

bd >> play("V  ", lpf=linvar([250,4500],16)).spread()

d1 >> play("shroom", pan=PRand(-1,1), shape=linvar([0,2],17), rate=PRand(1,6))

Group(hh,sh,tm,bd,d1).lpf=4500
