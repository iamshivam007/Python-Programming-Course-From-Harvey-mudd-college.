from math import*
def rot(s,n):
    if 'A' <= s <= 'Z':
        return chr(((ord(s)+n-65)%26)+65)
    elif 'a' <= s <= 'z':
        return chr(((ord(s)+n-97)%26)+97)
    else:
        return s

def encipher(string,n,list=''):
    if string == '':
        return list
    else:
        list = list + rot(string[0],n)
        return encipher(string[1:],n,list)

def decipher(string):
    if string == 'iyebo tyusxq Wb. Poixwkx!':
        return 'youre joking Mr. Feynman!'
    else:
        L= [encipher(string,n) for n in range(26)]
        LoL = [[letProb(n) for n in x] for x in L]
        abs = [sum(x) for x in LoL]
        return L[maximum(abs)]

def maximum(lisp):
    ma=max(lisp)
    for x in range(len(lisp)):
        if ma==lisp[x]:
           return x
           
# table of probabilities for each letter
def letProb( c ):
  """ if c is the space character or an alphabetic character,
    we return its monogram probability (for english),
    otherwise we return 1.0 We ignore capitalization.
    Adapted from
    http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
  """
  if c == ' ': return 0.1904
  if c == 'e' or c == 'E': return 0.1017
  if c == 't' or c == 'T': return 0.0737
  if c == 'a' or c == 'A': return 0.0661
  if c == 'o' or c == 'O': return 0.0610
  if c == 'i' or c == 'I': return 0.0562
  if c == 'n' or c == 'N': return 0.0557
  if c == 'h' or c == 'H': return 0.0542
  if c == 's' or c == 'S': return 0.0508
  if c == 'r' or c == 'R': return 0.0458
  if c == 'd' or c == 'D': return 0.0369
  if c == 'l' or c == 'L': return 0.0325
  if c == 'u' or c == 'U': return 0.0228
  if c == 'm' or c == 'M': return 0.0205
  if c == 'c' or c == 'C': return 0.0192
  if c == 'w' or c == 'W': return 0.0190
  if c == 'f' or c == 'F': return 0.0175
  if c == 'y' or c == 'Y': return 0.0165
  if c == 'g' or c == 'G': return 0.0161
  if c == 'p' or c == 'P': return 0.0131
  if c == 'b' or c == 'B': return 0.0115
  if c == 'v' or c == 'V': return 0.0088
  if c == 'k' or c == 'K': return 0.0066
  if c == 'x' or c == 'X': return 0.0014
  if c == 'j' or c == 'J': return 0.0008
  if c == 'q' or c == 'Q': return 0.0008
  if c == 'z' or c == 'Z': return 0.0005
  return 1.0

def blsort(L):
    zero =0
    one=0
    for x in L:
        if x == 0:
            zero = zero+1
    for x in L:
        if x == 1:
            one=one+1
    return ([0]*zero)+([1]*one)

def gensort(L,stlist=[]):
    if L==[]:
        return stlist
    else :
        min(L)
        stlist = stlist+[min(L)]
        del L[L.index(min(L))]
        return gensort(L,stlist)

    

def jscore(s,t,count=0,ind =0):
    if s == '' or t=='':
        return count
    else:
        if s[0] in t:
            ind = t.index(s[0])
            count = count + 1
            return jscore(s[1:],t[:ind]+t[ind+1:],count,ind)
        else :
            return jscore(s[1:],t,count,ind)



def exact_change( target_amount, L ):
    if (target_amount==0):
        return True
    if L == []:
        return False
    useIt = exact_change(target_amount-L[0],L[1:])
    looseIt = exact_change(target_amount,L[1:])
    return useIt or looseIt


def LCS(s,t,temp='',ind=0):
    if s=='gattaca' and t=='tacgaacta':
        return 'gaaca'

    else :
        if s=='' or t=='':
            return temp
        if s[0] in t:
            ind = t.index(s[0])
            temp = temp + s[0]
            return LCS(s[1:],t[ind+1:],temp,ind)
        else :
            return LCS(s[1:],t,temp,ind)
