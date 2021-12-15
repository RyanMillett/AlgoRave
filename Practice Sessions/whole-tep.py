Clock.bpm=72
Scale.default.set("wholeTone", tuning=Tuning.just)

prog = var(P[0,[1,2],[4,4,[5,-1]]],[8,4,4])

print(SynthDefs)

s1 >> saw(P[0,3,2,4].arp([0,[[4,3],1]]), dur=var([[[1/3,1/6],2/5],4],8), formant=var(P[:8],4), vib=PRand(9), pan=PWhite(-1,1), room=10, lpf=linvar([600,9_000],16))

g1 >> pulse(prog, dur=3/2, sus=2, oct=var([5,6],8), dist=0, vib=PRand(6), crush=linvar([0,1],16), amp=linvar([1/4,1],8), amplify=1/2, room=5, pan=PWhite(-1,1)).spread() + P*(0,[2,2,3],4,2)

g2 >> blip(prog, dur=2, sus=2, oct=var([5,6],8), dist=0, vib=PRand(6), crush=linvar([0,1],16), amp=linvar([1/4,1],8), amplify=1/2, room=5,pan=PWhite(1,-1)).spread() + P*(0,[2,2,3],4,2)

g_all.room=10

p1 >> sinepad(dur=1/2, sus=2, room=10, amp=linvar([1,1/4],8), amplify=2/3, shape=linvar([0,.25],32)).spread() + var([P*(0,2,4),P*(1,3,5)],8)

b1 >> donk(prog + P[0,3,[4,2],5], dur=PDur([5,[7,4],3],8), sus=1, blur=1, amp=var([1,1/2],8), pan=0, chop=0, crush=0, lpf=1200)

d1 >> play("x(-*)x((ok)[ (x[---{-=}])])".replace("x"," "), dur=1/2, pan=[1,-1], sample=P[:20], crush=1, room=4)

d2 >> play("x(-*)x((ok)[ (x[---{-=}])])".replace("-","f").replace("x","V"), dur=1/2, pan=[-1,1], sample=P[:20], crush=1, room=4)

d_all.lpf=600

Master().pshift=linvar([0,int(len(Scale.default)*-1)],16)
Master().echo=.33
Master().echotime=3
