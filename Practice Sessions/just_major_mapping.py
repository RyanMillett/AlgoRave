

Scale.default="justMajor"
Clock.bpm=92

p2 >> piano(P[0:8].offadd(5,p2.dur*2/3), oct=var([6,4],[8,4]), dur=2, sus=1, blur=1, amp=var([1/3,1/2],[8,4]), pan=PWhite(-1,1)).every([8,4],'stutter',3, dur=2, pan=[-1,1]) + var([0,[(0,2,4),(-1,1,3)]],[8,4])
p2.amplify=1/2

p1 >> blip(oct=var([5,6],[16,8]), sus=4, dur=PDur([[3,6,4],[5,7],2],8)*2, amp=linvar([1/4,3/2],16), pan=PWhite(-1,1), vib=PRand(12)) + P*(0,[3,[4,5]],[0,[-1,-3]])
p1.amplify=1.1

p3 >> swell(P[0,[3,-1]].arp([0,[6,5]]), oct=(4,5,6), dur=8, sus=12, crush=linvar([0,8],32, echo=.5, echotime=8)).spread()

p4 >> nylon(oct=6, dur=PDur([[5,8],[3,6],[[2,4],1]],8), pan=[-1,1], vib=PRand(6)).follow(p3) + [0,[4,5,6],[0,-3]]
p4.amplify=1/2

s1 >> varsaw(dur=[6,2], sus=4, oct=(4,5), amp=linvar([0,1],16), shape=.25).spread().follow(p3)



print(Player.get_attributes())

print(PWhite(-1,1))


