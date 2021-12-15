Scale.default="justMajor"

print(Scale.default)

p1 >> blip(PWalk(), oct=6, dur=1/3, blur=1, amp=var([1,1/4],[32,8]), pan=[-1,1,], vib=5, shape=var([0,.25],18), echo=var([.5,0],[.5,31.5]), echotime=6, room=5, formant=P[0:8]) 

p2 >> swell(PWalk(), oct=(5,6), dur=9, chop=18, room=5).spread() + (0,1,3)

b1 >> jbass(PWalk(), dur=PSum([5,3],8)/2, blur=1, lpf=200)

g1 >> piano(dur=PDur([3,5,2,4],8)*2, sus=3, oct=(5,6)).spread().follow(p2)

d1 >> play("{mM} (+k)( [sss])", room=3, pan=PRand(-1,1), sample=PRand(10))

bd >> play("V", dur=3).every(6.5, 'stutter', 2)

Group(b1).solo()

tf = var([True, False],32)

def change():
    if tf == True:
        Scale.Root=0
        Scale.default="bebopMaj"
    else:
        Scale.Root=4
        Scale.default="bebopMelMin"
    Clock.future(16,change)
    
change()
