Scale.default="bebopMelMin"
Clock.bpm=132

print(Scale.default)

print(SynthDefs)

mel=var([0,[2,4],[3,5],[1,4]],[8,4,4,8])
p1 >> blip(mel, dur=mel.dur, delay=[0,p1.dur/3], blur=1, vib=5, room=5, pan=[-1,1], echo=2/3, echotime=9)

seq=PTri(0,8) | PRange(0,8).offlayer('rotate',1.67)
pn >> piano(seq, oct=var([6,[7,5]],8), dur=1/2, delay=[0,pn.dur/3], amp=linvar([1/2,2/3],16))

bs >> bass(PWalk(), dur=2,blur=1, chop=0, amp=1/2)

str1="-(-{[-{=&}-]-})"
str2=str1.replace("-","s")

print(str1+str2)

d1 >> play(str1+str2, dur=[2/3,1/3], room=3, pan=[-1,1], sample=P[0:8], amp=1/2)

d2 >> play("X ", sample=PRand(10), amp=1/3)
