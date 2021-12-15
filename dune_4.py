Scale.default="prometheus"

ch.chords=var([0,[3,-2]],8)
p1 >> jbass(ch.chords, blur=1, dur=PDur(5,8), root=[0,[0.67,.75]]).spread()

p2 >> gong(ch.chords, oct=(5,6,7), sus=4, dur=1/2, pan=[-1,1], fmod=linvar([0,3,-3],32), room=10, echo=1, echotime=3) + (0,2,4)

d1 >> play("V", dur=var([2,1],16), lpf=500).every(15.5, 'stutter', 2)

s1 >> varsaw(PWalk(), blur=1.5, dur=P[[[5,7],4],[[3,1],[4,12]]], oct=(4,5,6), vib=linvar([0,12],32), amp=linvar([1/4,2/3],32), amplify=1, echo=.33, echotime=2).spread()

s2 >> saw(PWalk(), blur=1, dur=PDur([[3,5],[2,4,1]],8)*2)

tf = var([True,False],32)
def solo():
    if tf == True:
        s_all.solo()
        print("SOLOS")
    else:
        s_all.solo(0)
        print("ENS")
    Clock.future(8,solo)
    
solo()
