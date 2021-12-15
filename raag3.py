Scale.default="indian"
Clock.bpm=72

tf = var([True,False],32)
def change():
    if tf == True:
        Root=0
    else:
        Root=4
    print(int(Root))
    Clock.future(8,change)
    
change()

s1 >> saw(PWalk(), oct=6, dur=[[6,4],[2,4]], amp=1, blur=1, vib=5, shape=.15)

p1 >> blip(PRange(-8,8, var([1,2],16)), dur=[1/4], delay=[0,0,(0,1.67)], sus=3, amp=linvar([1/8,2/3],8), amplify=var([1,0],16), pan=[-1,1], echo=3.33, echotime=8, room=10, vib=PRand(0,12))

p2 >> nylon(PWalk(), dur=PSum([[5,7],[3,6],1],8), sus=3, amp=1/2, amplify=var([0,1],16), room=5)

p3 >> swell([0,[3,1],2,[1,4]], oct=(4,5), dur=[8,rest(8)], sus=12, echo=1, echotime=8, room=10).spread()

p4 >> bell(p3.degree, oct=(5,6), dur=1/4, sus=4, amp=linvar([1/8,1/2],16), fmod=PRand(0,1), spin=6) + (0,2,4)

pn >> piano(PTri(-8,8).arp([0,2,3]), oct=(6), sus=2, dur=1/8, amp=linvar([1/4,1],16), amplify=var([1.5,0],16))

b1 >> bass(PWalk(), dur=PDur([[3,6],[5,7]],8))

d1 >> play("m", dur=PDur([3,5],8), pshift=P[0:8], pan=[-1,1], sample=PRand(20), rate=3)

d2 >> play("<s><   S><+ >", dur=1/4, amp=1/3, sample=PRand(20), room=5)

d3 >> play("$", dur=PDur(5,8), amp=1, amplify=1.5, rate=2, pan=[-1,1], sample=P[0:8])

bd >> play("V( (kI))", lpf=4500, echo=var([0,.3],2), echotime=2)


