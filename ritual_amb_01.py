Scale.default="justMinor"

s1 >> saw(PWalk(), blur=1, dur=var([[4,4,[4,8],2],PDur([3,5],8)],[16,8]), amp=linvar([.5,1.5],12), room=6, oct=5, pan=linvar([-1,1],[8,2]))
s1.vib=var([0,5],8)
s1.coarse=2
s1.formant=P[0:8]

p1 >> swell([0,2,5],dur=12, oct=3, vib=linvar([0,12],32), shape=linvar([0,1],64)).spread()
p1.vib=linvar([0,6],8)
p1.formant=P[:8]

p2 >> prophet(var([PWalk(),[0,2]],12), sus=4, amp=linvar([0,.45],16), oct=(4,5), dur=PDur([3,6,9],12)*4) + (0,[4,1,3],[10,7])
p2.shape=linvar([0,.25],24)
p2.vib=1/4
p2.spin=linvar([0,16],32)

rm >> play("{kO}", dur=PDur([3,6,9],16), amp=linvar([0,.67],32), room=7, sample=PRand(5), pshift=[1,2,[3,4]])
sh >> play("{sH}", dur=PDur([3,6],9)*2, room=7, pan=PRand(-1,1), sample=PRand(5), pshift=rm.pshift, hpf=2500)
tm >> play("{mM}", dur=PDur([6,9],13,[1,2,3]*3), room=2, sample=PRand(5), pan=[-1,1]).sometimes('stutter',3)
Group(rm,sh,tm).lpf=linvar([200,5000],16)

bd >> play("V", dur=1, room=1, sus=1/2, amp=linvar([0,1.5],16),sample=PRand(5)).spread()

p_all.hpf=linvar([[250,0],[5000,1000]],24)
p_all.hpr=linvar([1,.1],12)
p_all.amp=1/4

