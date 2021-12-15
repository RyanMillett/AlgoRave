Scale.default="indian"

Clock.bpm=92

num = P[3,4,5,7,9]
denom = P[9,11,13,17]

d1 >> play("{kK}", dur=PDur(num.shuffle(),denom.shuffle()), pan=[-1,1])
d2 >> play("{hH}", dur=PDur(num.shuffle(),denom.shuffle()), pan=[1,-1])
d3 >> play("{sS}", dur=PDur(num.shuffle(),denom.shuffle()), pan=[-1,1])
d4 >> play("<+><$>", dur=PDur(num.shuffle(),denom.shuffle()), pan=[1,-1])

bd >> play("V", dur=1).every(8.5, 'stutter', 4)

d_all.sample=P[:20]
d_all.room=5

print(SynthDefs)

b1 >> blip(var([[0,0,[3,4]],[[2,5],[-3,-1]]],9), oct=var([5,[6,7]],18), dur=PDur(num.shuffle(),denom.shuffle())*3, blur=1, room=5, vib=PRand(6), sus=4, crush=linvar([0,8],36), amplify=2/3) + P*([0,-3],1,[2,[3,4]])

p1 >> swell(b1.degree[0] + (0,3), dur=3, sus=9, amp=linvar([0,1],18), shape=linvar([0,.25],36)).spread()

p2 >> creep(dur=[8,rest(5)], sus=5, vib=PRand(6), crush=PRand([2,4,8]), echo=.5, echotime=5).spread().follow(p1)

dr >> klank(dur=3, sus=5, amp=linvar([0,1],18), oct=4, dist=linvar([0,.1],36)).spread()

bs >> jbass(b1.degree[0], dur=var([1/2,1/3],[18,9]), blur=1, dist=linvar([0,.1],36))
