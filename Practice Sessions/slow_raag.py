def norg(n):
    '''
    Generates an infinity sequence of n-length
    '''
    pn = [0]*n
    pn[0] = 0
    pn[1] = 1

    for i in range(1,int(n/2)):
        pn[2*i] = pn[2*i-2] - (pn[i]-pn[i-1])
        pn[2*i+1] = pn[2*i-1] + (pn[i]-pn[i-1])

    return Pattern(pn)
    
def rudin_shapiro(n):
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
    for i in range(n):
        b = hamming(i << 1 & i)
        a = (-1)**b
        out.append(a)
        
    pat = P[0]
    for i in range(n):
        pat.append(pat[i] + out[i])

    return Pattern(pat)
    
def arpPat(seq, arp):
    '''Generates an arp pattern based on parameter sequence'''
    #arp = [0,4,2,[[4,5],[3,1]]]
    new_seq = []
    i = 0
    for n in seq:
        if n == 0:
            new_seq.append(0)
        else:
            new_seq.append(arp[i])
            i = (i + 1) % int(len(arp))
    return Pattern(new_seq)
    
def thue_morse(n):
    '''Generates a Thue-Morse Sequence of parameter length'''
    return [bin(i).count('1') % 2 for i in range(n)]
    
# - - - - - - # - - - - - - # - - - - - - # - - - - - - # - - - - - -

Clock.bpm=92
Scale.default.set("indian", tuning=Tuning.just)

rs = rudin_shapiro(128)
tm = thue_morse(128)


z1 >> sitar(PWalk(), oct=6, dur=PSum([[4,[5,3],6],[7,[11,13]],8],9)/var([1,2,3],18), blur=2, vib=var([0,3,5,8],9), amp=1, amplify=var([2/3,0],32), room=1, mix=.5, dist=.1)
z2 >> nylon(PWalk() + tm, dur=PDur([7,[6,3]],9), blur=2, amp=linvar([1/2,1],18), amplify=var([1.5,0],28), dist=.2)
z_all.room=1
z_all.mix=.5


l1 >> bell(PWalk(), dur=var([1/2,[[1/3,2/7],3/5]],18), oct=var([[5,7],6],9), sus=4, amp=linvar([1/2,1],32), amplify=var([1,0],[64,32]), pan=linvar([-1,1],[9,7,5]), mix=.6)
l2 >> gong((0,2,4,6), dur=4, sus=8, fmod=PRand(6), amplify=var([0,1.5],[28,4]), echo=1/3, echotime=6, mix=1).spread()
l_all.room=1


s1 >> sinepad(arpPat(tm,rs), dur=PSum([7,[8,6,3],[5,4]],9), blur=2, amp=linvar([1/2,1],18), amplify=.65, pan=[-1,1], crush=linvar([1,16],32), bits=8, mix=linvar([.2,1],18))
s2 >> blip(norg(128), dur=PDur([[5,4,2],6,[7,3]],9)*4, blur=2, pan=PWhite(), mix=linvar([.5,1],15))
s_all.room=1


p1 >> swell([0,-1,0,[3,4,5],[2,1]], dur=[4,4,3,2,8,2], blur=2, amp=linvar([1/2,1],32), amplify=1, mix=.6, dist=.05).spread() + (0,4)
p2 >> glass(PRand([0,[1,2,3],[4,5],6,7]), dur=4, blur=2, fmod=linvar([-2,6],18), mix=1).spread()
p_all.room=1


d1 >> play("P", dur=PSum([7,[8,6],[5,4,3]],9)/var([1,3,5],[18,9]), sample=P[:20], mix=.4, pan=PWhite())
d2 >> play("k", dur=P[1].loop(6)|P[1/2].loop(3), sample=1, amp=linvar([1/4,1/2],9), mix=.7, pan=linvar([-1,1],7))
d3 >> play(" ([ss][++])", sample=P[:5], mix=.5, amplify=1/2, pan=[-1,1])
d_all.room=1
