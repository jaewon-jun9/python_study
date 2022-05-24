[파이썬(python) 리스트 중복 요소 개수 찾기 (카운팅) or 제거,삭제하기 (try , except , count) (tistory.com)](https://infinitt.tistory.com/78)

### ***중복요소 카운팅하기**

 

> ***try, except 문 사용**

```
count={}
lists = ["a","a","b",'apple','w','wf']
for i in lists:
    try: count[i] += 1
    except: count[i]=1
print(count)

결과값 : {'a': 2, 'b': 1, 'apple': 1, 'w': 1, 'wf': 1}
```

**예외처리할때 사용하는 try except를 이런식으로 사용하는것은 생각 못해보았다.** 

**for문을 통해 lists의 요소를 하나씩 꺼내어 , count라는 이름의 딕셔너리에 넣는다.**

**이때 count(딕셔너리)에 이미 존재하는 key값이라면, try문이 실행되며 value에 +1을 하게된다.**

**count(딕셔너리)에 없는 key값이라면 except가 실행되며 value는 그냥 1로 저장된다.**