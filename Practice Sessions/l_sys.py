def algea(n):
    axioms = {'A':'AB','B':'CA','C':'B'}
    seq = 'A'
    for i in range(n):
        out = ""
        for ch in seq:
            out += axioms[ch]
        seq = out
    return seq

print(pat1)

print(pat2)

print(pat3)

print(struct)

pat1 = Pattern(algea(7).replace("A","P").replace("B","+").replace("C","p"))

pat2 = Pattern(algea(9).replace("A","k").replace("B","S").replace("C","[ss]"))

pat3 = Pattern(algea(5).replace("A","V").replace("B"," ").replace("C","[----]"))

struct = var(Pattern(algea(11)),16)

tb >> play(pat1, dur=1/2, pan=[-1,1], sample=P[:20])

sh >> play(pat2, dur=2/3, pan=[1,-1], sample=P[:20])

kd >> play(pat3, dur=1/2, pan=0, sample=P[:20])

perc = Group(tb,sh,kd)
perc.room=.4
perc.mix=.2

p1 >> swell(oct=4,dur=2,sus=p1.dur,blur=3, shape=expvar([0,.4],32)).spread() + (0,4)
p2 >> varsaw(oct=5,dur=2,sus=p2.dur,blur=3).spread() + (0,4)

p3 >> pasha(P[0].arp([0,3,1,2,4]),dur=1,amp=1)

p4 >> pasha(P[0].arp([0,3,1,2,4]),dur=1)

p_all.amp=linvar([1/2,1],16)
p_all.room=1

def update():
    if struct == 'A':
        p_all.mix=1
        p_all.lpf=900
    elif struct == 'B':
        p_all.mix=.5
        p_all.lpf=0
    elif struct == 'C':
        kd >> play(pat3, dur=1/2, pan=0, sample=P[:20])
    Clock.future(1,update)
    
update()
