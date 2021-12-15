Scale.default="justMinor"

p1 >> swell(var(P[(0,[1,2],4),(-1,1,3),(2,4,6)],32), dur=8, chop=16, oct=(4,5), amplify=1).spread()

a1 >> gong(dur=8, sus=1, room=6, spin=15, fmod=linvar([0,1/2,-1/2],8)).follow(p1)

p2 >> blip(p1.degree[0] + [1,2,[4,5]], oct=(5,6,7), sus=2, vib=2, dur=PDur([5,7],8), room=2, lpf=1200, pan=[-1,1], amp=linvar([0,1/2],8))

b1 >> bass(p1.degree[0], dur=PDur([3,5],8)*2, amp=1/2)

v1 >> saw(PWalk(), dur=var([4,[1/2,1/3]],[32,16]), amp=1, room=5, formant=PRand(0,8), pan=linvar([-1,1],[32,16]))

d1 >> play("x I( x)", room=1, sample=0, pan=0)
d2 >> play(" H", hpf=1200, amp=1/2,sample=0, room=2, pan=[-1,1])

d_all.lpf=linvar([250,4500],8)

