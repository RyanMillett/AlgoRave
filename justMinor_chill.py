Clock.bpm = 72
Root.default = var([-2,0],62)
Scale.default.set("justMinor", tuning=Tuning.just)

print(Scale.default)

var.roots = var([0,[2,[3,4]],[1,-1,-2]], [12,4])
var.chords = var([(0,2,4),(0,[1,3],4)],8)

arp1 = P[0,1,[2,[3,4]]]
arp2 = P[0,4,[3,2,1],[4,4,4,4,5]]

Pvar.arps = Pvar([arp1,arp2],16)

p1 >> swell(var.roots, dur=4, sus=p1.dur, blur=3, amp=linvar([1/4,1],16), mix=.6).spread() + var.chords

p2 >> sinepad(Pattern(var.roots).arp(Pvar.arps), oct=var([5,6],16), dur=PSum([[5,3,6],7,[[9,11],13]],8), sus=p2.dur, blur=expvar([1,4],32), amplify=.7, mix=.5)

p3 >> klank(var.roots, dur=2, sus=p3.dur, blur=4, mix=.8, spin=6).spread() + (0,[1,3,1],[2,4])

pads = Group(p1,p2,p3)

pads.room=.8

s_all.room=.6
s1 >> varsaw(var.roots + 6, oct=(4,5), dur=6, sus=s1.dur, blur=2, mix=.4).spread()

d1 >> play("x-(o-)(-x)", dur=var([[1/2,1],1/4],32), lpf=expvar([1200,5500],32), pan=[-1,1], room=.5, mix=.5).sometimes('stutter', 2)
d2 >> play("  <S><H>", dur=2, room=.7, mix=.6)
d3 >> play("-[--]{-~}(-[---(-=)])", dur=1/4, hpf=2500, pan=PWhite(), sample=P[:20], room=.6, mix=.4)

kd >> play("V", dur=1, lpf=500)

bb >> play("$", dur=PDur([3,[5,[4,8]]],8), sample=P[:20], room=.3, mix=.5)

perc = Group(d1,d2,d3,bb)

synths = Group(pads,s1)

perc.hpf = linvar([900,4500],32)
perc.hfr = expvar([1,.1],13)
synths.lpf = linvar([3500,900],28)
synths.lpr = sinvar([.1,1],11) 

