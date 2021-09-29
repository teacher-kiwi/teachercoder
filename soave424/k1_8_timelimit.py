#삼각형

#현재위치정보입력받기
r,c=input().split()
lm = [list(map(str, input().strip())) for _ in range(int(r))]


l = list(filter(None, lm))

#의자있는 좌표 리스트 생성
om=[[q,w] for q in range(len(l)) for w in range(len(l[q])) if l[q][w]=='1']

largest=0

for a in range(int(r)):
    m=[om[i] for i in range(len(om)) if om[i][0]==a]
    if len(m)<2:
        continue
    else:
        lastone=[om[p] for p in range(len(om)) if om[p] not in m]
        if len(m)==2:
            hori=abs(m[0][1]-m[1][1])
            verti=max([abs(lastone[q][0]-m[0][0]) for q in range(len(lastone))])
            area=hori*verti/2
        elif 2<len(m)<len(om):
            hori=max([abs(m[q][1]-m[0][1]) for q in range(len(m))])
            verti=max([abs(lastone[q][0]-m[0][0]) for q in range(len(lastone))])
            area=hori*verti/2
        else:
            area=0
    if area>largest:
        largest=area

for b in range(int(c)):
    m2=[om[i] for i in range(len(om)) if om[i][1]==b]
    if len(m2)<2:
        continue
    else:
        lastone2=[om[p] for p in range(len(om)) if om[p] not in m2]
        if len(m2)==2:
            hori=abs(m2[0][0]-m2[1][0])
            verti=max([abs(lastone2[q][1]-m2[0][1]) for q in range(len(lastone2))])
            area=hori*verti/2
        elif 2<len(m2)<len(om):
            hori=max([abs(m2[q][0]-m2[0][0]) for q in range(len(m2))])
            verti=max([abs(lastone2[q][1]-m2[0][1]) for q in range(len(lastone2))])
            area=hori*verti/2
        else:
            area=0
    if area>largest:
        largest=area

print(f'{largest:.1f}')

