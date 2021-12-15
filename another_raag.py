Clock.bpm = 72
Root.default = -2
Scale.default.set("indian", tuning=Tuning.just)

var.roots = var([0,5,[4,6,1],2,[3,1]],[8,4])
Pvar.chords = Pvar([(0,2,4),(0,[1,3],4)], 12)

print(SynthDefs)

l1 >> varsaw(var.roots + 6, oct=(5,6),dur=[4,4,2], sus=l1.dur, blur=1.3)

g1 >> bell(PTri(12), dur=1/8, oct=(5,6,7), amp=linvar([0,1],32), room=1, mix=.5)

s1 >> pulse(Pattern(var.roots).arp([0,4,[2,3,1],4]), dur=1/8, formant=P[:8], pan=PWhite())
s2 >> nylon(Pattern(var.roots).arp([0,4,5,1,2]), dur=PDur([5,3],8), vib=5, pan=[-1,1])

s1.amplify=var([0,1],24)

p1 >> ambi(var.roots, dur=4, sus=p1.dur, blur=2, pan=linvar([-1,1],8), room=.6, mix=.6)
p2 >> klank(var.roots, dur=6, sus=p2.dur, blur=2, room=.8, mix=.5).spread() + Pvar.chords
p3 >> swell(var.roots, dur=6, sus=p3.dur, blur=3, amp=linvar([1/2,1],24), room=.9, mix=.6).spread() + Pvar.chords

d1 >> play("P", dur=PDur([[2,4,5],[3,[6,7]]],12), room=.4, mix=.4, sample=P[:20], pan=[-1,1])
d1 >> play("x-(o-)(-x)", dur=1/2, lpf=linvar([1200,5500],16), pan=[-1,1], sample=P[:20])
d2 >> play("-[--]-(-[----])", dur=1/4, pan=[-1,1], sample=P[:20])

bd >> play("V", dur=1, lpf=900).sometimes('stutter',3,dur=.5)

dd >> play("!", dur=PDur(3,8), sample=PRand(20), room=1, mix=.6)

synths = Group(s1,s2,l1)

Group(bd,synths,g1).solo(0)


