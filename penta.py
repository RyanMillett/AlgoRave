Clock.bpm=72

Scale.default.set("minorPentatonic", tuning=Tuning.just)

print(SynthDefs)

p_all.room=10

mel = P[:5]
s1 >> saw(mel | mel.offadd(3, s1.dur/2), dur=[4,4,6,2], pan=linvar([-1,1],5), blur=1, oct=(5,6))

ch.chords = var([[[4,3],2],0,1,3,[5,4,3]],[5,3,4,4,8])
p1 >> soft(ch.chords, oct=(6,5), dur=1, sus=4, blur=1, amp=linvar([0,1],16)).spread() + P*(0,[1,0],[2,2,[3,4]])

p2 >> swell(ch.chords, oct=(4,5,6), dur=ch.chords.dur, sus=p2.dur*2, amp=linvar([0,1],32)).spread() + P*(0,1,2)

p3 >> glass(ch.chords, oct=(4,5,6), dur=ch.chords.dur, sus=8).spread() + (0,1,2,3)

p4 >> blip(dur=PSum([[3,6],5,[7,[8,12]],[1,4,2]],8), oct=var([5,6],[12,4]), sus=linvar([1,4],12), pan=PWhite(-1,1), vib=PRand(12), crush=linvar([0,8],16), echo=.33, echotime=9).accompany(p2)

p5 >> varsaw(ch.chords, dur=1, sus=3, oct=(4,5,6), amp=linvar([0,1],16), amplify=1, crush=linvar([0,[16,32,64]],32)).spread()

b1 >> jbass(PWalk(), dur=PSum([[3,6],[4,2,4],5,2],8), blur=1)

sh >> play("<s><+>", dur=PDur([[5,3],4],8), pan=[1,-1], sample=P[:10])

cp >> play("   ((H[KK])S)", room=6)

hh >> play("{<-><#>}- {---[---]} -- --[--{-=}] -- -", dur=1/4, pan=[-1,1])

sn >> play(" I", room=7)

bd >> play("V", lpf=linvar([250,5500],32))

Master().lpf=linvar([500,[2500,5000]],32)
Master().lpr=linvar([.1,1],11)
