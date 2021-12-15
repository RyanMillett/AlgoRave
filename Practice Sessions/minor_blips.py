Scale.default="justMinor"

Clock.bpm="92"

print(SynthDefs)

pat = P[0,3,2,5]

seq1 = var([pat],8) 

s1 >> blip(PWalk(), dur=var([4,1,1/4],[12,8,4]), oct=7, amp=2/3, blur=1, vib=PRand(12), crush=linvar([0,4],16), amplify=1.5)

p1 >> donk(pat | pat.invert(), oct=var([5,6],8), dur=PDur([[3,3,6],[5,7]],8), sus=var([1,2],8), pan=PWhite(-1,1))

p2 >> swell(var([0,2,[1,3],[[4,5],-1]],[8,4,2,2]), dur=[8,4,2,2], room=5).spread()

p3 >> pasha(amp=2/3, chop=4, pan=[-1,1]).follow(p2) + (0,2,4)

b1 >> jbass(p2.degree[0], dur=PDur(3,8))

d1 >> play("(K(+k))", room=5, dur=var([[4,2],p1.dur],[8,4]), sample=0, rate=var([1,2],[8,4]))

bd >> play("V", dur=2, lpf=250)
