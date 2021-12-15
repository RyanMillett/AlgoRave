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
    
pattern = Pattern(curarr)

print(pattern)

Scale.default="lydian"
Clock.bpm=76

g1 >> gong(PRange(-8,7), dur=PDur([[3,6],[4,8]],8), sus=3, pan=[-1,1], root=[0,0.33])

p1 >> swell(pattern, oct=(4,5), dur=8, blur=1.5, shape=linvar([0,.5],32), lpf=linvar([500,7500],16), lpr=linvar([.1,1],4), hpf=250, amplify=1/2).spread()

p2 >> glass(PTri(0,8), oct=PRand(3,7), dur=2, sus=6, amp=linvar([1/4,2/3],16)).spread()

p3 >> blip(pattern.arp([0,4,[3,2]]), oct=[6,7,5], dur=1/4, amp=linvar([1/8,1/2],8), sus=4, amplify=1.5, shape=linvar([0,.15],16), vib=PRand(1,6))

p4 >> pluck(pattern.arp([0,4,[3,2]]), oct=(6,7), dur=1/4, sus=1, amp=linvar([1/8,1/2],16), amplify=.5)

b1 >> jbass(pattern, dur=PDur([6,[5,7,5],3,[4,8]],8), blur=1, shape=.25, lpf=450)

s1 >> saw(PWalk(), oct=(5,6), dur=PSum([5,3],8), blur=1, vib=PRand(1,6), pan=linvar([-1,1],5), formant=2, amplify=1.5)

d1 >> play("V(-[-{-=}])", lpf=linvar([250,4500],16)).every(7.5, 'stutter', 2)

d2 >> play("  (I[IS]) ", room=5)

d3 >> play("$", dur=PDur([3,5],8), sample=PRange(0,20), amp=1, pan=[-1,1], room=5).sometimes('stutter', 3)
