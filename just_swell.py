Clock.bpm=62

Scale.default="justMajor"

tf=var([True,False],72)
def change():
    if tf == True:
        Scale.default="justMajor"
        Root.default=0
    else:
        Scale.default="justMinor"
        Root.default=4
    print("Root:", int(Root.default))
    print("Scale:", Scale.default)
    Clock.future(36,change)
    
change()

chords = var([(0,[2,1,3,1],4),(3,[5,6],7)],[9*4,9*2])

seq = P[0,3,2,1]

s1 >> varsaw(seq.offlayer('invert',s1.dur/2), dur=9, blur=1).spread()

p1 >> blip(seq.offadd(5,p1.dur/2), dur=PSum([[3,6,9],[5,7],1],9), sus=7, echo=1.33, echotime=9, crush=1, vib=PRand(6), pan=PWhite(-1,1), amp=linvar([1,0],13))

p2 >> swell(seq, dur=3, sus=3, blur=2, crush=linvar([0,4],11)).spread()

p3 >> prophet(seq, dur=var([9/5,9/3],18), sus=p3.dur, blur=1, chopf=p3.dur*9, pan=PWhite(1,-1)) + chords

b1 >> jbass(p3.degree[0], amp=linvar([0,1/4],18), dur=9/6, blur=1, sus=b1.dur, dist=linvar([0,.15],18))

g1 >> gong(seq, oct=(5,6), dur=3/9, sus=7, pan=linvar([-1,1],5), amp=linvar([0,1.5],13), fmod=PRand(1,6), amplify=2) + chords

g2 >> bell(dur=PDur([[4,2],[3,6,9],5],9), sus=3, oct=7, amp=g1.amp*.67, amplify=1/4).follow(g1)

d1 >> play("     +", echo=.33, echotime=3, pan=[1,-1])
d2 >> play("    k", echo=d1.echo*2/3, echotime=3, pan=[-1,1])

bd >> play("V-", lpf=linvar([100,1500],18)).sometimes('stutter', 2)

p_all.crush=linvar([0,[4,8,16],21])

d_all.room=1
d_all.mix=.7
d_all.hpf=1500
d_all.sample=P[0:4]

p_all.room=1

Master().lpf=linvar([500,5500],36)
Master().lpr=linvar([.1,1],13)
