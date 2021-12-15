Clock.bpm = 72
Clock.meter = (9,4)
Scale.default.set("prometheus", tuning = Tuning.bohlen_pierce)

var.ch = var([[0,0,2],[-1,1],[-2,3]], [[7,5],[2,4]])

p1 >> varsaw(var.ch, oct=6, dur=3, sus=p1.dur, blur=1.5, amp=expvar([1/3,1],18), mix=.6).spread()

p2 >> swell(var.ch, oct=5, dur=6, sus=p2.dur, blur=3, amp=sinvar([1/2,1],36), mix=.8).spread()

b1 >> dub(var.ch, oct=4, dur=9, sus=b1.dur, blur=2, amp=linvar([1/2,1],42), mix=1).spread()

p_all.room=1

d1 >> play("<Q><#>", dur=18, amp=2/3, room=1, mix=1, echo=3/5, echotime=18, lpf=1500)

d2 >> play("W", dur=9, delay=1/3, room=1, mix=.7, echo=2/5, echotime=9, pshift=var.ch)

d3 >> play("{Pp}", dur=PDur([5,[4,7],[3,2,6]],9), sample=P[:20], room=.4, mix=.5)

d4 >> play("m", dur=PDur([7,[5,[4,3]]],9), room=.3, mix=.4)

s1 >> sinepad(PWalk(), oct=6, dur=PSum([[5,[3,7]],2],6), room=.9, mix=.4, vib=5) + (0,2,4)

s2 >> soprano(PWalk(), dur=1/3)
