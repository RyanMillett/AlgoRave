Scale.default="justMajor"
Clock.bpm=72
Clock.time_signature=9/4

seq = PRange(-12,12)

p1 >> glass(seq, dur=3, sus=9, oct=PRand(4,7), pan=[-1,1], fmod=linvar([0,[3,1],-3],18), spin=linvar([0,36],36)).spread()

p2 >> swell(mel, dur=3, sus=6, oct=5, lpf=linvar([500,4500],36), amp=linvar([1/4,2/3],18), shape=linvar([0,.15],18), echo=1/3, echotime=6).spread()

ch=var([0,[3,4],[2,5],[1,6]])
p3 >> varsaw(ch, dur=6, oct=(4,5), vib=3, blur=1, lpf=1500).spread() + (0,2,4)

mel = PTri(8) | PTri(7).splice(ch)
p4 >> saw(mel, dur=PSum([[3,6],5,7,1],9), oct=5, blur=1, formant=3, vib=PRand(12), lpf=2500)

p5 >> keys(mel.invert(), oct=6, dur=PDur([[2,2,5],3,[6,9],1],9), sus=2, pan=[-1,1])

d1 >> play("<{mM}k>< [ (SH)]>", dur=3, room=7, sample=P[0:20], lpf=1200, echo=[0,.67],echotime=6).every(9, 'stutter', 3)

bd >> play("V", dur=1, room=5, sample=0).sometimes('stutter', 2/3)

d2 >> play("<s><+><h>", dur=PDur([[6,5],9],9), room=5, sample=P[0:20], lpf=linvar([500,4500],36))


tf = var([True,False],36)
def change():
    if tf == True:
        Root=0
        Scale.default="justMajor"
    else:
        Root=4
        Scale.default="justMinor"
    Clock.future(1,change)
    
change()
