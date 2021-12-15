Clock.bpm = 67
Root.default = 6
Scale.default.set("justMinor", tuning=Tuning.just)

var.roots = var([0,[3,[4,5]],[2,1]],72)

Pvar.chords = Pvar([(0,2,4),(0,1,4),(0,4,6)],[18,9,9])

p1 >> swell(var.roots, oct=4, dur=3, sus=p1.dur, blur=2, amp=linvar([1/3,1],18), amplify=1, vib=0, shape=linvar([0,.5],36), mix=1).spread() + Pvar.chords

p2 >> ambi(var.roots, oct=PRand([4,5,6]), dur=6, sus=p2.dur, blur=2, amp=expvar([1/3,1],18), amplify=2/3, fmod=0, shape=0, pan=PWhite(), spin=18, mix=1).spread() + Pvar.chords

p3 >> noise(var.roots, dur=6, sus=p3.dur, blur=2, amp=expvar([0,1],18), amplify=1/3, echo=2/3, echotime=9, dist=expvar([0,.4],36), mix=1, pan=linvar([-1,1],36))

pads = Group(p1,p2,p3)

pads.room=1

p1.lpf=linvar([500,1500],9)
p2.hpf=linvar([500,1100],18)
p3.bpf=linvar([500,4500],15)

s1 >> pulse(Pattern(var.roots).arp([0,[2,[3,1]],[4,4,[5,6]]]), dur=var([[1/3,[1/5,[1/7,1/9]]],[1,3]],18), sus=s1.dur, blur=1, vib=PRand(5), room=.6, mix=.5, pan=sinvar([-1,1],6))

s2 >> pluck(Pattern(var.roots).arp([0,[2,[4,5],3]]), oct=4, dur=1/6, sus=s2.dur, blur=1)

print(SynthDefs)

leads = Group(s1,s2)

leads.amplify=var([0,1],36)
leads.hpf=2500

d1 >> play("X", dur=9, echo=1/3, echotime=9, mix=.5)

tb >> play("{Pp}", dur=PDur([3,[5,4]],9), mix=.4, pan=[-1,1], sample=var.roots + P[:5])

tm >> play("m", dur=var([1,[2/3,1/3]],18), mix=.3, sample=P[:10])

gg >> play("#", dur=9, fmod=6, echo=2/3, echotime=9, mix=.8, sample=2)

perc = Group(d1,tb,tm,gg)

perc.room=.5
