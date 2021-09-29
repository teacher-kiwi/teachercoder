#삼각형
#wrong_answer

#현재위치정보입력받기


r,c=input().split()
l = [list(map(str, input())) for _ in range(int(r))]

'''
4 5
00110
01000
00000
00001
'''

om=[]
omre=[]
last=[]
for q in range(len(l)):
    for w in range(len(l[q])):
        if l[q][w]=='0':
            continue
        #om.append([chair[q][w],q,w])
        om.append([q,w])

for r in range(len(om)):
    for e in range(len(om)):
        if om[e]==om[r]: #동일반 제외
            continue     
        if om[e][0]==om[r][0] or om[e][1]==om[r][1]: #평행하기 위해 x좌표 혹은 y좌표 동일
                a=[om[r],om[e]]
                b=[om[e],om[r]]
                if b not in omre: #겹치는 경우 제외
                    omre.append(a)
                    
for t in range(len(omre)): #2개 목록에서 
    for d in range(len(om)): # 1반씩 다시 넣어보기 
        if om[d]==omre[t][0] or om[d]== omre[t][1]: #동일한 건 제외
            continue
        if om[d][0]==omre[t][0][0] and om[d][0]==omre[t][1][0]: #x좌표 셋다 같으면 제외
            continue
        if om[d][1]==omre[t][0][1] and om[d][1]==omre[t][1][1]: #y좌표 셋 다 같으면 제외
            continue
        last.append(omre[t]+[om[d]])

largest=0
for s in range(len(last)):
    x1=last[s][0][0]
    x2=last[s][1][0]
    x3=last[s][2][0]
    y1=last[s][0][1]
    y2=last[s][1][1]
    y3=last[s][2][1]
    if x1==x2:
        tri=abs(y1-y2)*abs(x2-x3)/2
    else:
        tri=abs(x1-x2)*abs(y2-y3)/2
    if tri>largest:
        largest=tri    

print(f'{largest:.1f}')
