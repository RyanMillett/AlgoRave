Clock.bpm=154
Scale.default="justMajor"

def thue(seqLength):
    '''Generates a Thue Sequence of parameter length'''
    return Pattern([bin(n).count('1') % 2 for n in range(seqLength)])

def arpPat(seq):
    '''Generates an arp pattern based on parameter sequence'''
    arp_pat = [0,4,2,[[4,5],[3,1]]]
    new_seq = []
    i = 0
    for n in seq:
        if n == 0:
            new_seq.append(0)
        else:
            new_seq.append(arp_pat[i])
            i = (i + 1) % int(len(arp_pat))
    return Pattern(new_seq)

print(arpPat(thue(10)))

arp_seq = arpPat(thue(10))
thue_seq = thue(64)

p1 >> blip(arp_seq + var(thue_seq,int(len(thue_seq/2))), sus=8, amplify=1, oct=thue_seq + 5, pan=[-1,1], vib=PRand(6), crush=linvar([0,4],16))

p2 >> swell(arp_seq + (0,2,4), chop=p2.dur*[4,4,[6,3]], oct=5, dur=16, sus=p2.dur, echo=1/3, echotime=9, crush=linvar([0,4],16), room=1, mix=linvar([.1,1],18)).spread() + var(thue_seq,8)

s1 >> pluck(arp_seq, dur=1/2, sus=s1.dur*3, oct=5, pan=linvar([-1,1],5), vib=PRand(5), amplify=thue_seq.rotate(4))

s2 >> zap(arp_seq.invert(), dur=1/2, sus=s2.dur, amplify=thue_seq.rotate(3), vib=PRand(5), echo=.25, echotime=2, pan=linvar([1,-1],5)) + (0,2,4)

b1 >> jbass(arp_seq + P[:7], amplify=thue_seq.invert(), amp=.95)

d1 >> play("x", amplify=thue_seq.invert())

d2 >> play("((kS)(io))", amplify=thue_seq, amp=1/2)

d3 >> play("[--][--]", amplify=(thue_seq+1)*.5, pan=[1,-1])
d4 >> play("[ss]", amp=1/2, amplify=(thue_seq.invert()+1)*.5, pan=[-1,1])

d_all.room=1
d_all.sample=thue_seq * P[:20]
