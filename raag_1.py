Scale.default="indian"
Clock.bpm=92
Clock.time_signature=5/4

p1 >> blip(PRange([0,-8],[8,12,16],[1,2,3]), sus=4, dur=var([1,1/5],[10,5]), pan=[-1,1], amplify=linvar([1/4,2/3],15), room=5, vib=PRand(0,12), fmod=linvar([-3,3],25))

p2 >> ambi([0,3,2,1], oct=(4,5), dur=5, room=8).spread() + (0,[2,1],4,6)

p3 >> sawbass(PWalk(), dur=PSum([4,2,3],5), sus=p3.dur)

d1 >> play("M", dur=PDur([3,2,5],5), sample=PRand(20), pan=[1,1], shap=linvar([.05,.50],10))

d2 >> play("V-v-kI", dur=PSum([2,4,5],3), lpf=linvar([250,4500],15))

d3 >> play("ssSsH", sample=PRand(20), room=3, hpf=1500, pan=[-1,1])

d_all.lpf=linvar([250,2500],15)

s1 >> saw(PWalk(), oct=var([4,5,6],15), vib=linvar([0,6],5), dur=PSum([3,2,10,1],5), blur=s1.dur, room=2)
s1.formant=P[0:8]


s2 >> pluck(PTri(8,16), dur=var([5,1/5],10)*2, sus=4, amplify=1/3, pan=linvar([-1,1],3), room=5)
s2.echo=1/3
s2.echotime=5




