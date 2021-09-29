#삼각형 크기
#correct

#현재위치정보
chair=[[1,2,0,4,0],
       [0,0,3,0,0],
       [0,0,0,0,6],
       [8,0,0,7,5]]
om=[]#위치정보
omre=[]#평행고르기
last=[]#나머지 고르기 

for q in range(len(chair)):
    for w in range(len(chair[q])):
        if chair[q][w]!=0:
            om.append([chair[q][w],q,w])

for r in range(len(om)):
    for e in range(len(om)):
        if om[e][0]==om[r][0]: #동일반 제외
            continue     
        if om[e][1]==om[r][1] or om[e][2]==om[r][2]: #평행하기 위해 x좌표 혹은 y좌표 동일
                a=[om[r],om[e]]
                b=[om[e],om[r]]
                if b not in omre: #겹치는 경우 제외
                    omre.append(a)

for t in range(len(omre)): #2개 목록에서 
    for d in range(len(om)): # 1반씩 다시 넣어보기 
        if int(d+1)==omre[t][0][0] or int(d+1)== omre[t][1][0]: #동일한 건 제외
            continue
        if om[d][1]==omre[t][0][1] and om[d][1]==omre[t][1][1]: #x좌표 셋다 같으면 제외
            continue
        if om[d][2]==omre[t][0][2] and om[d][2]==omre[t][1][2]: #y좌표 셋 다 같으면 제외
            continue
        last.append(omre[t]+[om[d]])

largest=0
for s in range(len(last)):
    x1=last[s][0][1]
    x2=last[s][1][1]
    x3=last[s][2][1]
    y1=last[s][0][2]
    y2=last[s][1][2]
    y3=last[s][2][2]
    if x1==x2:
        tri=abs(y1-y2)*abs(x2-x3)/2
    else:
        tri=abs(x1-x2)*abs(y2-y3)/2
    if tri>largest:
        largest=tri    

print(f'{largest:.1f}')

