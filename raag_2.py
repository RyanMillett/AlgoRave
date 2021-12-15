Scale.default="indian"
Clock.bpm=92
Clock.time_signature=(9,8)

rm >> play("k", dur=PDur([5,7],9), pan=[-1,1], sample=PRand(20))
sh >> play("s", dur=PDur(7,9), pan=[1,-1], sample=PRand(20))
cl >> play("+", dur=PDur(8,9), pan=[-1,1], sample=PRand(5))
tm >> play("m", dur=PDur([4,5],9), pan=[1,-1], sample=PRand(20), pshift=PRand(10))
bd >> play("V*[--]", lpf=550)

Group(rm,sh,cl,tm,bd).lpf=linvar([250,2000],36)

seq1=PRange(P[0:8].shuffle())
p1 >> blip(seq1 + seq1.invert(), oct=4, dur=PDur([8,7,6,5],9)*1.5, sus=2, pan=[-1,1], vib=PRand(1,12), shape=linvar([0,.25],36))
p1.lpf=linvar([200,1500],18)

p2 >> saw(PWalk(), oct=var([5,6],[36,18]), dur=var([PDur(2,9),1/3],[36,18]), pan=linvar([1,-1],9), vib=3, formant=P[0:8].shuffle())

s1 >> soprano(PRange([8,0]), dur=P[3,4,2], oct=3, vib=linvar([0,6],9))

p3 >> glass(PRange(P[0:8]), dur=9, oct=(4,5,6,3)).spread() + var([([0,0,-1],[1,2],4), (1,[2,3],5)],18)
p3.fmod=linvar([0,1,-1],36)
p3.spin=linvar([0,36],18)
