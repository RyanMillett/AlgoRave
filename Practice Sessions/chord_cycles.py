Clock.bpm = 92
Root.default = 7
Scale.default.set("phrygian", tuning=Tuning.just)

var.roots = var([0,[[1,3],-1],[2,0]],[9,6,3])

triad = P[0,2,4]
sus2 = P[0,1,4]
sus4 = P[0,3,4]
p5add7 = P[0,4,6]

Pvar.ch = Pvar([triad,[sus2,sus4],p5add7],9)

print(Pvar.ch)

p1 >> blip(Pattern(var.roots).arp(Pvar.ch), dur=PDur([[3,3,6],[5,7]],9), sus=p1.dur, blur=expvar([4,12],36), vib=PRand(9), pan=PWhite(), mix=.6)

p2 >> pasha(Pattern(var.roots).offadd([4,2],p2.dur/2), oct=4, dur=1/2, sus=p2.dur/2, blur=1, shape=.2, mix=.5, pan=linvar([-1,1],3))

p1.hpf=1500

leads = Group(p1,p2)

leads.room=.6
leads.crush=2

s1 >> varsaw(var.roots, dur=3, sus=s1.dur, blur=2, shape=.2, amp=linvar([1/2,1],9), vib=5, mix=.6).spread() + Pvar.ch
s2 >> swell(var.roots, dur=6, sus=s2.dur, blur=3, amp=expvar([1/2,1],18), mix=.7).spread()

pads = Group(s1,s2)

pads.room=.8
pads.crush=4

b1 >> jbass(PWalk(), dur=PDur([[5,7,4],[3,6]],9), sus=b1.dur, blur=1, lpf=250, amplify=PRand([0,1/2,1]))

d1 >> play("V", dur=1, lpf=500)
d2 >> play(" - ( (-[--]))", dur=1/2, pan=1, sample=PRand(20))
d3 >> play("  (S[CC])", dur=2, pan=-1, mix=.7)
d4 >> play("+", dur=PDur([5,4],9), sample=P[2:5], pan=[-1,1])

perc = Group(d_all)

perc.crush=2
perc.room=.4

# BREAK    
perc.hpf=linvar([3500,0],[18,inf], start=now)
pads.lpf=expvar([500,15_000],[18,inf], start=now)
leads.hpf=sinvar([3500,0],[18,inf], start=now)
Group(pads,leads).tremolo=expvar([16,0],[18,inf],start=now)
b1.amp=var([0,1],[18,inf], start=now)


print(Player.get_attributes())


