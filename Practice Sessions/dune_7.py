Clock.bpm=62

Scale.default="justMinor"

ch.chords = var([5,[4,4,6],2,3,[1,-1],0],[6,2,4,4,8,12,rest(4)])

p_all.room=10
d_all.room=10

d1 >> swell([0], dur=8, sus=12, oct=4, amp=linvar([1/2,1],16), shape=linvar([0,.55],32)).spread()

d2 >> dub(dur=5, sus=12, amp=linvar([0,1],d2.dur*3), amplify=1/2).spread().follow(d1)

p1 >> varsaw(ch.chords, dur=ch.chords.dur, oct=(4,5,6), blur=1, crush=linvar([0,8],32)).spread()

p2 >> prophet(oct=(6,7,5), pan=PWhite(-1,1), blur=1, crush=linvar([0,8],64)).follow(p1)

f1 >> blip(ch.chords, oct=(5,6), amp=linvar([0,1],16), amplify=f1.amp*1.5, sus=linvar([1,4],16), dur=PSum([[3,6],[5,7],4],8), shape=linvar([0,.5],16), vib=PRand(12), pan=PWhite(-1,1)) + P*(0,2,4)

tm >> play("M", dur=PDur([[3,6],4,[5,5,7],2],8), rate=1/2, dist=0, shape=0, crush=linvar([0,128],32), pan=[-1,1], room=6, pshift=P[:8])

hh >> play("<{-#}><{X }>- [-{-=}-] ---- [-{-=}]", pan=[-1,1], dur=1/4, crush=linvar([0,64],64))

bd >> play("Vk", dur=PSum([5,3,7],8), crush=linvar([0,8],32)).sometimes('stutter', 2)

Group(tm,hh,bd).lpf=linvar([250,9000],32)
Group(tm,hh,bd).lpr=linvar([.1,1],8)

Group(tm,hh,bd).room=10
