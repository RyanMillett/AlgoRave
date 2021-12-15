Scale.default="yu"
Root.default=1
Clock.bpm=72

print(Scale.yu)
print(int(Root.default))

print(SynthDefs)

ch.chords = var([0,[1,[2,3]]],[3,5])
p1 >> prophet(ch.chords + var([0,[1,2]],8), dur=ch.chords.dur, blur=1.5, chop=8).spread()
p2 >> swell([0] + var([0,[1,2]],8), oct=4, dur=8, sus=8, chop=8).spread()
p3 >> pasha(oct=5, dur=1, sus=4, amp=linvar([0,1],32), amplify=1/3, pan=linvar([-1,1],5)).follow(p1) + (0,1,4)
p4 >> creep(amp=1/2, oct=(4,5), dur=8, echo=.25, echotime=6, shape=linvar([0,.5],32)).follow(p3)

p_all.crush=linvar([0,16],64)

b1 >> jbass(ch.chords, dur=1/2, lpf=200, dist=.05)

s1 >> orient(PWalk(), dur=PSum([3,[5,7]],8), pan=[-1,1])
s2 >> pulse(PTri([6,10]), dur=var([1,[1/4,1/6]],[12,4]), vib=var([5,12],[12,4])) + (0,2)

s3 >> blip(PRange(-6,12), oct=(6,5), lpf=3500, dur=PDur([3,4,5,7],8), crush=linvar([0,4],32), sus=4)

d1 >> play("   <S><+>", room=5, echo=.16, echotime=3, pan=[-1,1], hpf=1500).every(3.5,'stutter',3, rate=3)
d2 >> play("mk(m[ m]):", room=5)
d3 >> play("<[----]><[ssss]>", pan=linvar([-1,1],5), sample=P[0:20], hpf=linvar([500,2500],16))

bd >> play("V", lpf=linvar([250,4500],16))

f1 >> play("    (([MM][II]))", amp=var([0,1],[12,4]), sample=PRand(20), room=10)

tf=var([True,False],32)
def change():
    if tf == True:
        Root.default=(Root.default + 7) % 6
    print("Root: ", int(Root.default))
    Clock.future(32,change)
    
change()


Master().lpf=linvar([250,10000],32)
Master().lpr=linvar([.1,1],16)
