class Solution:
    def romanToInt(self, s: str) -> int:
        i,v,x,l,c,d,m,iv,ix,xl,xc,cd,cm=0,0,0,0,0,0,0,0,0,0,0,0,0
        for f in range(len(s)):
            if s[f]=="I":
                if f<len(s)-1 and s[f+1]=="V":
                    iv+=1
                elif f<len(s)-1 and s[f+1]=="X":
                    ix+=1
                else:
                    i+=1
            elif s[f]=="V":
                if f!=0 and s[f-1]=="I":
                    continue
                else:
                    v+=1
            elif s[f]=="X":
                if f<len(s)-1 and s[f+1]=="L":
                    xl+=1
                elif f<len(s)-1 and s[f+1]=="C":
                    xc+=1
                else:
                    if f!=0 and s[f-1]=="I":
                        continue
                    else:
                        x+=1
            elif s[f]=="L":
                if f!=0 and s[f-1]=="X":
                    continue
                else:
                    l+=1
            elif s[f]=="C":
                if f!=0 and s[f-1]=="X":
                    continue
                elif f<len(s)-1 and s[f+1]=="D":
                    cd+=1
                elif f<len(s)-1 and s[f+1]=="M":
                    cm+=1
                else:
                    c+=1
            elif s[f]=="D":
                if f!=0  and s[f-1]=="C":
                    continue
                else:
                    d+=1
            elif s[f]=="M":
                if f!=0 and s[f-1]=="C":
                    continue
                else:
                    m+=1
        return ((m*1000)+(d*500)+(c*100)+(l*50)+(x*10)+(v*5)+(i*1)+(iv*4)+(ix*9)+(xl*40)+(xc*90)+(cd*400)+(cm*900))