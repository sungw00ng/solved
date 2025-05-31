N=int(input())
lst=set()
res=[]
#대소문자 추가
def lettercase(ch):
	if'a'<=ch<='z':
		return ch.upper(),ch
	if'A'<=ch<='Z':
		return ch,ch.lower()
	return ch,ch

#단축키 만들기
for _ in range(N):
	line=input()
	key=line.split()
	found=0
	#첫단어에서 단축키 발견O
	for index,val in enumerate(key):
		w1,w2=lettercase(val[0])
		if w1 not in lst and w2 not in lst:
			lst.add(w1)
			lst.add(w2)
			#[]추가
			key[index]='['+val[0]+']'+val[1:]
			found=1
			break
	#앞에서 발견X,문자하나씩 확인
	if not found:
		for index,val in enumerate(key):
			modified_word=''
			inserted=0
			for c in val:
				if not inserted:
					w1,w2=lettercase(c)
					if w1 not in lst and w2 not in lst:
						lst.add(w1)
						lst.add(w2)
						modified_word+='['+c+']'
						inserted=1
					else:
						modified_word+=c
				else:
					modified_word+=c
			if inserted:
				key[index]=modified_word
				found=1
				break
	res.append(' '.join(key))

for r in res:
	print(r)
