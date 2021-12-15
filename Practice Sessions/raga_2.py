Scale.default="indian"

Clock.time_signature=9/4
Clock.bpm=92

Scale.Root=var([0,4],[36,18])

p1 >> blip(PRange(-15,15,[1,2,[3,4]]), sus=4, dur=var([1/4,1/3],18), amplify=var([0,1/3],[9,18]), vib=linvar([0,12],18), shape=linvar([0,.25],9), pan=[-1,1]).sometimes('stutter',1.5)
p1.room=10
p1.echo=1.33
p1.hpf=linvar([0,2500],18)

p2 >> ambi(PWalk(), oct=(4,5), dur=9, spin=[3,6,9,18], blur=1, crush=linvar([0,4],18)).spread() + (0,2,4)

p3 >> swell(oct=(3,4), dur=9, spin=5, crush=linvar([0,8],18*2)).spread().follow(p2)

p4 >> prophet(dur=3, chap=6, pan=linvar([-1,1],6)).follow(p2)

s1 >> saw(PWalk(), dur=var([3,1/4],[36,18]), vib=var([3,9],[36,18]), room=2, formant=PRange(8))

b1 >> bass(PWalk(), dur=PDur([5,7,3],9), sus=1/5)

sh >> play("s", dur=1/4, amp=var([0,1/3],[36,18]), sample=PRand(5), room=3, hpf=1500, echo=.33, pan=[-1-1])

cl >> play("<+><S>", dur=PDur([5,3],9), room=5, sample=0, hpf=2500, amp=1/2).every(8.5, 'stutter', 6, rate=2)

tm >> play("{mM}", dur=PSum([5,7],9)/2, sample=PRand(10), pan=[1,-1], pshift=PRange(8))

bd >> play("X", dur=var([3,3/2],[36,18]), lpf=250)


