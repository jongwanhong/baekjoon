# 삽입 정렬
# 먼저 봤던 선택 정렬은 느리므로, 다른 접근 방법 생각
# 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입한다.
#  필요한 때만 위치를 바꾸므로 데이터가 거의 정렬되어 있다면 효율적이다.
# 삽입 정렬은 두 번째 데이터부터 시작한다.
# 정렬이 이루어진 원소는 항상 오름차순을 유지한다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # i부터 처음까지 1씩 감소하면서 비교
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작으면 빠져나온다
            break
print(array)

# 결론 : 선택정렬과 같이 시간 복잡도는 O(N^2)이지만,
# 데이터가 거의 정렬되어 있을 경우에는 매우 빠르게 동작할 수 있다
