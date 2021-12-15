Scale.default="bebopMelMin"
Clock.time_signature=9/4

ch.chords = var([0,6,5,0,2,3,1], [2/3,1/3])

p1 >> gong(ch.chords, dur=ch.chords.dur, sus=6, pan=[-1,1], vib=PRand(12), amplify=linvar([1/8,1/3],9), shape=linvar([.05,.55],36))

p2 >> piano(PWalk(), dur=2/3, sus=p2.dur, amplify=linvar([1/8,1],9)) + (0,[[7,8],9],10)

d1 >> play("<x><$> ko {[---]=}", echo=1.5, pshift=P[0,8], sample=PRand(10), pan=[-1,1], room=2, lpf=linvar([500,4500],36)).every([8.5,17.5], 'stutter', 5, rate=5)

d2 >> play("{mM}", dur=PDur([4,[5,7],6],9), sample=PRand(20), pan=[-1,1])

p3 >> glass(ch.chords, dur=[9,rest(6)], shape=linvar([.05,.55],9*3)).spread() + (0,[4,5],[10,9,11])

