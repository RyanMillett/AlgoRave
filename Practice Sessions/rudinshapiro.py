from __future__ import division
import numpy
import matplotlib

def rudinshapiro(N):
    """
    Return first N terms of Rudin-Shapiro sequence
    https://en.wikipedia.org/wiki/Rudin-Shapiro_sequence
    Confirmed correct output to N = 10000:
    https://oeis.org/A020985/b020985.txt
    """
    def hamming(x):
        """
        Hamming weight of a binary sequence
        http://stackoverflow.com/a/407758/125507
        """
        return bin(x).count('1')

    out = []
    for n in range(N):
        b = hamming(n << 1 & n)
        a = (-1)**b
        out.append(a)
        
    pat = P[0]
    for i in range(N):
        pat.append(pat[i] + out[i])

    return Pattern(pat)
    

mel = rudinshapiro(64)

print(mel)

Clock.bpm=92
Scale.default="justMajor"

print(SynthDefs)

p1 >> blip(mel + var([0,4],int(len(mel))), dur=var([1,1/2], int(len(mel))), sus=3, amp=linvar([1/4,1],int(len(mel)/2)), pan=PWhite(-1,1), room=5) + var([P*(0,2),(0,4)],int(len(mel)))

p2 >> sinepad(mel.invert(), dur=[4,2], amp=1/2, room=8) + (0,2,4)

p3 >> swell(mel.invert() + (0,2,4), oct=4, dur=8).spread()

d1 >> play("<-(-k)-(-[--])><  (+{s[ss]})>", dur=1/4, sample=mel, room=3)
