Clock.bpm=67
Clock.time_signature=9/4

Scale.default="wholeHalf"

s1 >> varsaw(PTri(9), oct=(5,6), dur=13, sus=7, amp=linvar([1/4,1],9), amplify=2/3).spread() + (0,[2,3],[5,5,6])

s2 >> saw(PWalk(), oct=(6,7), dur=PSum([[7,5],[9,6],1],9), formant=1, amp=1/2, amplify=1/4, vib=PRand(12))

s_all.room=5

g1 >> gong(PTri([9,6]), oct=(6,7), dur=2/3, amp=linvar([1/4,1],18), amplify=2,pan=linvar([-1,1],6))
g2 >> bell(oct=7, dur=2, amp=linvar([1/4,1],18), amplify=1/3, pan=linvar([1,-1],6)).follow(g1)
g3 >> blip(PRange(0,8), oct=var([5,6],9), dur=1/6, sus=linvar([1,3],9), vib=linvar([0,6],9), amp=var([0,1/2],[18,9]), pan=linvar([-1,1],3), amplify=1/2)

p1 >> ripple(oct=(4,5), dur=5, sus=8, shape=linvar([0,.25],18), crush=linvar([0,4],21)).spread()
p2 >> prophet(oct=(4,5), dur=2, sus=3, shape=linvar([0,.75],55), crush=linvar([0,8],34)).follow(p1).spread()
p3 >> swell(oct=(2,3,4,5), dur=8, sus=13, shape=linvar([0,.5],31), crush=linvar([0,16],15)).spread()

p_all.room=10

b1 >> jbass(dur=PSum([5,7],9), blur=1, pshift=[0,.33], dist=linvar([0,.2],13))

d1 >> play("(E(KE))", dur=PSum([3,4],9), room=10, echo=.33, hpf=2500, pan=[-1,1])

bd >> play("V", room=10, dur=9, echo=var([.33,bd.dur/6],9), echotime=9, dist=linvar([0,.25],9))



Master().lpf=linvar([[200,500],[1500,2500,5500]],9)
Master().lpr=linvar([.1,1],3)
Master().crush=linvar([0,16],18)
Master().amp=linvar([1,0],36)
Master().echo=.33
Master().echotime=9

