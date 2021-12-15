import subprocess

def neckam_pat(length, ones, parts):
    pathname = "/Users/ryanmillett/Downloads/abrazol/creatingrhythmsprogs/"
    filename = "neckam"
    args = str(length) + " " + str(ones) + " " + " ".join(str(p) for p in parts)
    
    make_file = "gcc -lm -o " + filename + " " + pathname + filename + ".c;" 
    run_file = "./" + filename
    command = make_file + run_file + " " + args
    
    output = subprocess.check_output([command], shell=True).decode("utf-8").strip().split('\n')
    output = [list([int(ch) for ch in s]) for s in output]
    return Pattern(output)

neckams_1 = Pvar([neckam_pat(16,6,[2,3,5])], 16)
neckams_2 = Pvar([neckam_pat(16,7,[1,2,3])], 16)
neckams_3 = Pvar([neckam_pat(16,4,[2,3,5])], 16)
neckams_4 = Pvar([neckam_pat(16,5,[1,2,3,5])], 16)

pitch_seq = [int(i) for i in list("0314253647556677657071727374454606162633435051522324041121300102")]

pitch_seq = Pattern(pitch_seq)
seq_len = len(pitch_seq)

print(pitch_seq)

print(PDur(3,seq_len))

Clock.bpm = 132
Scale.default.set("wholeTone")

p1 >> space(Pattern(p2.pitch[0]).arp([0,[2,1],[4,3]]), oct=var([5,6],seq_len), dur=1/3, sus=p1.dur, blur=1, amplify=.3).spread()

p2 >> swell(var(pitch_seq | pitch_seq.invert(), 16), oct=(4,5), dur=2, sus=p2.dur, blur=p2.sus*2.5).spread() + (0,4)
p2.amp = expvar([.1,1],16)
p2.amplify = 1.5

p2.lpf = linvar([650,4500],32)

p2.room = 0.7
p2.mix = 0.6

b1 >> jbass(p2.pitch[0], oct=5, dur=1, sus=b1.dur, blur=1)
b1.amp = (1/p2.amp)/10
b1.amplify = .5

b1.lpf = 350

bd >> play("V", dur=1, amp=neckams_1, amplify=1, lpf=150).sometimes('stutter', 2, dur=1)
sn >> play("(+k)", dur=1/2, amp=neckams_3, amplify=.6, pan=[-1,1], sample=PRand(20))
hh >> play("(-:)".replace("-","<s><->"), dur=1/4, amp=1, amplify=(neckams_2+0.5), hpf=5500, pan=linvar([-1,1],8), sample=P[:3]).sometimes('stutter', 4, dur=1/4)
hh.echo = 0
hh.echotime = 0
tb >> play("P", dur=var([1/2,[1/4,1/8]],[32,16]), amp=neckams_4, amplify=.5, pan=[1,-1], sample=P[:10])
bb >> play("$", dur=tb.dur*2, amp=neckams_2, amplify=.2, sample=P[:10])
gn >> play("(Qq)", dur=16, room=1, mix=1, amp=0.5, echo=0.5, echotime=gn.dur*1.5, lpf=950)
vn >> play("z", dur=15.5, amp=0.2, room=.6, mix=0.3, echo=0.5, echotime=4, sample=PRand(10), pshift=PRand(9))
perc = Group(hh, sn, tb, bb)
perc.room = .5
perc.mix = .3


