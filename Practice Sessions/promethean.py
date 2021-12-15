print(SynthDefs)

Scale.default="prometheus"

s1 >> charm(PTri([9,7,6,3]), amp=linvar([1/4,2/3],9), room=7, dur=[7,3,9,2,13])
s1.vib=linvar([0,6],9)
s1.oct=(4,3)
s1.formant=P[0:8]
s1.hpf=linvar([250,5000],23)

g1 >> pulse(PTri([5,9,7,3] + var([0,[1,-1],0,[2,3],0,4],7)), dur=[7,9,5,11,3,2], sus=4, oct=(4,6,5), amp=1/5, amplify=1)
g1.room=10
g1.pan=linvar([-1,1],9)
g1.spin=linvar([0,6],11)


p2 >> prophet(g1.pitch, oct=(4,5)).spread() + (0,2,[5,6])
p2.room=10
p2.spin=linvar([3,9],19)

g2 >> blip(g1.pitch.map(
    { 0: 2,
        4: lambda x: x + P([0,0,-1],[2,5]),
            lambda x: x in (5,3): lambda y: y + PRand([0,2,1,3])
    }))
g2.amp=var([2/3,1/2],8,16)    
g2.dur=var([PDur([3,5,7],8)*2,[1/3,2]],8,16)
g2.sus=4
g2.blur=g2.sus*1.5
g2.oct=var([5,6],8,16)
g2.room=5

cp >> play("k", dur=2, room=8, amp=1/2, sample=PRand(10), coarse=7).sometimes('stutter',5)
tm >> play("m", dur=g2.dur, room=8, amp=var([1,1/3],8,16), sample=PRand(10), chop=5, pshift=P[0:8]*1.33)
sh >> play("s", dur=2/5, sample=PRand(10), amp=linvar([0,1],13), hpf=3500, pan=PRand(-1,1)).sometimes('stutter',6)
bd >> play("V-", amp=linvar([1/4,4/5],17), sample=PRand(10)).sometimes('stutter', 1.5)

Group(cp,tm,sh).lpf=linvar([50,5500],23)
