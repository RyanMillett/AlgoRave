print(Scale.names())

Scale.default="egyptian"
Clock.bpm=92
Clock.time_signature=9/4

ch.chords=P[0,3,2,1,-1,0,5,4,2]

nz >> noise(ch.chords, dur=6, sus=9, lpf=linvar([250,1500],6), lpr=linvar([.1,.5],2), room=10, echo=.33, echotime=7, pan=var([-1,1],3), amp=linvar([0,1],9))

p1 >> glass(ch.chords, oct=P[3,4,5,6].shuffle(), dur=6, sus=3, fmod=linvar([-3,3]), spin=18).spread() + (0,1,2,3,4,5,6)


