print(Scale.names())

Scale.default="bebopMelMin"

Clock.bpm=132


sPat=P[3,9,2,7,1,6]

print(sPat.offadd(2,.50))

p1 >> blip(sPat, oct=6, dur=PDur([8,[9,6]]*3,12)*2, sus=2)
