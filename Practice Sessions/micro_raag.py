def thue_morse(n):
    '''Generates a Thue-Morse Sequence of parameter length'''
    return Pattern([bin(i).count('1') % 2 for i in range(n)])
    

Clock.bpm=92
Scale.default.set("indian", tuning=Tuning.just)

tm1 = thue_morse(64)

d1 >> play("P", dur=PDur([3,5,[7,6]],[9,13]), amp=linvar([1/4,1],18), amplify=var([1,0],[27,9]), sample=P[:20], pshift=([1/6,-1/3]), pan=[-1,1], crush=0, echo=0)

d2 >> play("R", amp=linvar([1/3,1],9), sample=PRand(0,10), pan=[1,-1])

d3 >> play("&", dur=PSum([7,5,11],9), pan=PWhite())

d4 >> play("$", sample=P[:20])

d5 >> play("m")

d_all.room=1
d_all.mix=.3

Master().room=1
Master().mix=linvar([.1,1],27)

Master().echo=linvar([1/6,5/6],15)
Master().echotime=linvar([0,18],18)

Master().crush=linvar([0,[8,[16,32]]],64)

d_all.crush=linvar([0,16],18)
d_all.hpf=linvar([400,2500],32)
d_all.hpr=linvar([.1,1],5)

seq1 = var([0,3,[4,6],[2,-1,-5]], [[5,7],2]) + var([0,[3,5]],18)

print(SynthDefs)

s1 >> varsaw(seq1, dur=[[7,5],[2,4]], sus=s1.dur*2).spread()

p1 >> swell(seq1, oct=4, dur=3, sus=3, blur=3, echo=1/3, echotime=9).spread() + (0,2,4)

p2 >> klank(seq1, dur=3, sus=p2.dur*2, blur=2, lpf=1500).spread()

f1 >> sinepad(seq1 + [0,3,6], dur=PDur([7,5],9), sus=2, pan=[-1,1], vib=PRand(12), crush=4, amplify=var([1/3,0],9))

f2 >> blip(PWalk(), dur=PSum([6,[5,[4,7]]],9)/3, sus=3, vib=PRand(12), pan=[1,-1])

b1 >> jbass(PWalk(), dur=PDur([7,[5,4]],9))

Group(s1,p1,p2,f2).lpf=linvar([500,2500],18)
