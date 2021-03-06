# 내가 제일 많이 만나는 에러. - IndexError
# 슬라이싱은 IndexError가 안난다고함. -> check
# 왜지..?
abc = '1232131'
print(abc[123141:])

# 리스트에 문자열처럼 연산자 활용을 많이 안했었던거 같다. (+, * ..)
print([1, 2, 3] + [4, 5, 6])
# 그 이유를 혼자 생각해보면, 이것은 원본을 유지하기 때문이었다. 쓰일 일이 있겠지
# 파괴적 vs 비파괴적 함수,(알고리즘 + 혼공스 하면서 개념을 명확하게 했는데 이제야 제대로 이해한 것 같다.)
a = [1, 2, 3]
b = a + [4]
print(a, b)

# 리스트 요소 제거 - 이것또한 pop만 많이 사용해왔다.
# pop()를 사용하지 않고 인덱스나 밸류로 접근하게 되면 시간복잡도가 O(N)이기 때문, 하지만 리마인드 차원에서 다시 정리
# 인덱스로 제거
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1 del
del a[1]
del a[0:3]
# 2 pop()
a.pop()
a.pop(1)
print(a)

# 값으로 제거 - 내부에 값이 여러개 있어도 가장 앞에 있는 애만 제거
a.remove(7)

a = []  # 다시 초기화
a.clear()  # 특별한 경우...

# format 문 Remind
numbers = [1, 22, 333, 4444, 55555]

for number in numbers:
    print("{}는 {}자리수입니다.".format(number, len(str(number))))


# 2차원 행렬 값넣기
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]
for number in numbers2:
    output[(number - 1) % 3].append(number)  # 인덱스 접근 확인
print(output)
