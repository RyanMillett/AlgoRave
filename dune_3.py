from opensimplex import OpenSimplex
import numpy as np
import math
import random
import time

startPos=[.67,.1]
tmp=OpenSimplex()

curarr = []
for i in range(0,45):
    vel = tmp.noise2d(startPos[0],startPos[1])
    startPos[0] = math.sin(i/3)
    startPos[1] = (i/3)
    note = math.ceil(10*vel)
    #print(note)
    curarr.append(note)
    
seq1 = Pattern(curarr)

Scale.default="prometheus"
Clock.bpm=72
Clock.time_signature=9/4

p1 >> glass(seq1, oct=[4,5,3,6], dur=3, sus=9, fmod=PRand(-3,3), room=10, spin=18).spread()

p2 >> prophet(seq1, oct=(5,4), dur=6, sus=9, amp=linvar([0,1],36), room=10, vib=.5).spread()

p3 >> swell(seq1, oct=5, dur=9, sus=11, shape=linvar([0,1],36), room=10).spread()

s1 >> blip(PRange(-8,8), oct=(6,5), dur=var([1/4,1/6],[3,3,12]), sus=3, vib=6, room=10, amp=var([1/2,0],[6,12]), amplify=1)

tm >> play("{mMX}", dur=PSum([5,6,7,3],9), sample=PRand(10), pan=[-1,1], room=5, shape=.05, echo=.33, echotime=3, amplify=2)

bd >> play("V(k[--])", lpf=linvar([150,4500],36), amp=linvar([1/4,2/3],18))

b1 >> jbass(PWalk(), dur=PDur([5,6,5,3,7,1],9), blur=1, shape=.15)


print(Scale.default)
