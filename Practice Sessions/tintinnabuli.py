Clock.bpm = 92
Root.default = -3
Scale.default.set("justMinor")

triad = P[0,2,4]

p1 >> sinepad(triad.arp(triad.shuffle()) + var([0,3],16), oct=(6,4,5), dur=1/3, sus=p1.dur, blur=8, ampplify=1/2, room=.7, mix=.7)

p2 >> gong(PWalk() + var([0,8],16), oct=(5,7,6), dur=PDur([[4,7],3],8), sus=p2.dur, blur=8, amp=1/2, room=.7, mix=.5)

p3 >> klank(triad.arp(triad), dur=3, room=1, mix=.6).spread()

p4 >> swell(P[0,1,[3,-1]].arp(triad), oct=(5,4), dur=9, sus=p4.dur, blur=3, echo=1/3, echotime=9, room=1, mix=1).spread()

d1 >> play("x-o(-[-x])", dur=1/2, pan=[-1,1], room=.4, mix=linvar([0,1],[16,inf],start=now)).sometimes('stutter',2)

Group(d1).only()
