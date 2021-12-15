Clock.bpm=154
Scale.default="justMajor"

def generateSequence(seqLength):
    return [bin(n).count('1') % 2 for n in range(seqLength)]

def arpSeq(seq):
    arp_pat = [0,4,2,[[4,5],[3,1]]]
    new_seq = []
    i = 0
    for n in seq:
        if n == 0:
            new_seq.append(0)
        else:
            new_seq.append(arp_pat[i])
            i = (i + 1) % int(len(arp_pat))
    return new_seq
    
thue_seq = Pattern(generateSequence(32))

arp_seq = Pattern(arpSeq(thue_seq))

print(arp_seq)

p1 >> blip(arp_seq + var(thue_seq,8), sus=8, amp=linvar([1/2,1],8), amplify=1.5, oct=thue_seq + 5, pan=[-1,1], vib=PRand(6), crush=linvar([0,4],16))

p2 >> swell(arp_seq, oct=5, dur=16, sus=8, echo=.67, echotime=12, crush=0).spread() + var(thue_seq,8)

b1 >> jbass(arp_seq + P[:7], amplify=thue_seq.invert(), amp=.5)

d1 >> play("x", amplify=thue_seq.invert())

d2 >> play("((kS)(io))", amplify=thue_seq, amp=1/2)

d3 >> play("[--][-(-=)]", amplify=(thue_seq+1)*.5, pan=[1,-1])

ss >> play("[ss]", amp=1/2, amplify=thue_seq, pan=[-1,1])
cl >> play("+", amp=1, amplify=thue_seq.invert(), pan=[1,-1])

d_all.room=4
d_all.sample=thue_seq + P[:20]

