Clock.bpm=72

Scale.default="justMajor"

def fib(x,y,z):
    F = P[x,y]
    for i in range(2,z):
        F.append(F[i-1] + F[i-2]) 
    return F
    
seq = Pattern(fib(0,1,50))

for i in range(len(seq)):
    print(seq[i] % 7)
    
p_all.room=10

s1 >> charm(seq%3, dur=(seq%7)+1, blur=1, oct=6, echo=.33, echotime=5)

p1 >> swell(seq % 7, dur=8, sus=12, oct=4, crush=linvar([0,8],16)).spread()

p2 >> prophet(seq % 7, dur=[4,2,2,8], blur=1, crush=linvar([0,16],32)).spread()

p3 >> blip(seq % 7, dur=PDur((seq%7)+1,8), sus=4, oct=(5,[6,7]), pan=PWhite(-1,1), vib=PRand(6), amp=linvar([0,1],16))

p4 >> nylon(PRange(0,seq%7), dur=1/4, sus=2, amp=linvar([0,1],8), amplify=var([0,1],8), pan=[-1,1])

b1 >> jbass(seq%5, dur=2)

d1 >> play("<x(-(I[ x]))>< (kS)>", dur=PSum((seq%7)+2,8), pan=[-1,1], sample=P[:5])

d2 >> play("(s+)", dur=(seq%[3,5])*.5, pan=[-1,1], room=5, sample=P[:6], echo=.33, echotime=6)

bb >> play("$", dur=PDur((seq%7)+1,8), sample=P[seq], pan=[-1,1])

