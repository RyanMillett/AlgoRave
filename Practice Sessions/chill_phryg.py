Clock.bpm = 67
Root.default = -3
Scale.default.set("phrygian", tuning=Tuning.just)

triad = P[0,2,4]
sus = P[0,[1,3],[3,4]]

Pvar.ch = Pvar([triad,sus],32)

p1 >> sinepad(Pvar.ch, dur=1, oct=var([5,6],16), sus=p1.dur, blur=4, amp=linvar([1/4,1],16), amplify=var([1,.5],16), pan=sinvar([-1,1],4))

p2 >> gong(PTri(0,len(Scale.default)), oct=var([5,6],16), dur=1, amp=linvar([1/4,1],16), amplify=.5)

p3 >> space(sus.arp(triad), dur=1/3, sus=p3.dur, blur=2, amp=linvar([1/4,1],32), pan=PWhite())

ens_arp = Group(p1,p2,p3)

ens_arp.room=.7
ens_arp.mix=.6

ens_arp.crush = 0

s1 >> swell(sus, dur=8, sus=s1.dur, blur=1.5).spread() + (0,2,4)
s2 >> klank(triad, dur=4, oct=6).spread()

pads = Group(s1,s2)

pads.room=1
pads.mix=.8
pads.crush=0

d1 >> play("x-x(o[cc])".replace("x"," "), dur=1/2, lpf=linvar([700,4500],16)).sometimes('stutter')
d2 >> play(" (SH)", dur=2, echo=1/3, echotime=4)
d3 >> play("V", dur=1, lpf=700).sometimes('stutter')


perc = Group(d1,d2,d3)

perc.room=.4
perc.mix=.2
