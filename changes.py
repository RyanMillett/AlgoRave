p1 >> blip(PTri(8).arp([0,2,4]).offadd(7,1.67), dur=2, oct=(4,5), sus=4, pan=[-1,1], amp=linvar([1/8,2/3],32), vib=PRand(0,12), room=5)

print(SynthDefs)

p2 >> keys(var([0,1,0,-1],4), dur=2, oct=6, amp=linvar([1/4,1],8), amplify=.67).spread() + (0,2,4)

p3 >> swell(dur=8, oct=[4,5], amp=1/2, room=5).spread().follow(p2)

d1 >> play("V(-[--])I(-=)", dur=1, room=3, lpf=linvar([250,5500],32)).every([7.5,15.5], 'stutter', 2)

s1 >> saw(PWalk(), oct=var([5,6],16), dur=PSum([5,3,2],8), pan=linvar([-1,1],3), room=5, amplify=1, vib=6, formant=P[0:8])


tf = var([True,False],16)

def my_test():
    if tf == True:
        Scale.default="justMajor"
        Root.default=0
    else:
        Scale.default="justMinor"
        Root.default=4
    Clock.future(16, my_test)

my_test()
