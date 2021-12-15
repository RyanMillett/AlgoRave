Clock.bpm=92
Scale.default.set("minorPentatonic", tuning=Tuning.just)

A=var([0,1],32)
a=var([0,1],16)
B=var([1,0],32)
b=var([1,0],16)

s1 >> orient(var([0,[5,[3,P*(1,-1)]]]) + (0,3),dur=4,vib=5,pan=[-1,1],oct=6,room=5, echo=.33, echotime=5, amplify=A)

s2 >> charm(PRange(10) + (0,4),dur=var([1/2,[2/5,1/3]],[12,4]),amplify=B)

t1 >> blip(P[:6].offadd(5,1/2), oct=var([5,6],16),dur=var([2,[1/2,2/3]],16),sus=var([1,2],16), vib=PRand(6), shape=linvar([0,.25],32), pan=PWhite(-1,1), amplify=a)

t2 >> pulse(PRange(0,len(Scale.default)*2,[1,3]),oct=4,dur=PSum([7,[3,6]],8),crush=linvar([0,[8,16]],32),amplify=b)

p3 >> klank(dur=4,sus=8,oct=4,amp=linvar([1/8,1],16),dist=linvar([0,.05],32),room=10,lpf=linvar([250,9500],23),lpr=linvar([.1,1],11),amplify=2/3).spread()

p4 >> sinepad(var([0,[3,[4,2]]],16),dur=8,sus=8).spread() + (0,1,2)

b1 >> jbass(PWalk(8),dur=PDur(3,[6,[7,5]],[8,16]),shape=0,dist=0)

d1 >> play("({mM} )m{o{-=}}((Ik)K)",pan=[-1,1],sample=P[:20],dur=PDur([7,[5,[3,6]]],[8,12]))

d2 >> play("+", dur=PSum([7,3],8),sample=P[:10],pan=[1,-1])
d3 >> play("(SH)", dur=PSum([5,9],8),sample=P[:10],pan=[-1,1])

d4 >> play("s", dur=P[1,1/2,1/2]/2,sample=P[:10],pan=[-1,1])

d_all.room=5

bd >> play("V-",dur=var([1/2,[1/6,[1/5,[1/7,1/9]]]],[14,2]),rate=var([1,[3,[5,7]]],[14,2]))

Group(d1,d2,d3,d4,bd).lpf=linvar([350,15_000],32)
Group(d1,d2,d3,d4,bd).lpr=linvar([.1,1],8)

t_all.stop()

p_all.hpf=linvar([0,2_500],21)
p_all.hpr=linvar([1,.1],7)

Master().room=linvar([.5,10],32)
Master().spin=linvar([0,64],64)

Master().degrade()

print(Player.get_attributes())
