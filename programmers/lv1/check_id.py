# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
import re


def solution(new_id):

    # 1
    new_id = new_id.lower()

    # 2
    for i in new_id:
        if not (i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.'):
            new_id = new_id.replace(i, '')

    # 3 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 정규표현식
    # new_id = re.sub('\.\.+', '.', new_id)

    # 4
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # # 정규표현식
    # new_id = re.sub('^\.|\.$', '', new_id)

    # 5
    if new_id == '':
        new_id = 'a'

    # 6
    # if len(new_id) >= 16:
    #     new_id = new_id[0:15]
    #     if new_id[-1] == '.':
    #         # replace -> 해당하는 것을 다 지운다(new_id[-1]). 그래서 테케 통과 못함
    #         # new_id = new_id.replace(new_id[-1:], '')
    #         new_id = new_id[0:14]

    # 정규표현식
    new_id = re.sub('\.$', '', new_id[0:15])

    # 7
    # if len(new_id) < 3:
    while len(new_id) < 3:  # while문 안의 조건은 true 때만 수행되므로 윗줄이 필요 없었다.
        new_id += new_id[-1:]

    return new_id


print(solution("bat....y.abcdefghjklm"))
print(solution("....bat.y.abcdefghjklm..."))
