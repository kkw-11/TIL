'''
문제
성적 정리 2
엘리스 선생님이 여전히 학생들의 성적을 처리하고 있습니다. 엘리스 선생님이 코딩을 잘한다는 이야기를 듣고 다른 선생님들도 성적 처리를 대신 부탁했다고 합니다.

다른 선생님들의 채점 결과를 보니 엘리스 선생님과는 조금 다르게, 점수 칸을 빈칸으로 비워 둔 경우가 있었습니다.

지난 실습에서 작성한 코드를 수정해서, 다른 선생님들의 채점 결과에도 사용할 수 있도록 만들어 주세요.

매개변수로 주어지는 리스트에는 XX점 꼴의 점수 데이터, 혹은 빈 문자열 ""가 주어질 수 있습니다.
매개변수로 주어진 리스트에 점수 정보가 하나도 없을 수도 있습니다. 이 경우 None을 return 합니다.
빈 문자열은 평균의 분자와 분모에 모두 포함되지 않는 데이터입니다. 무시하고 건너뛰면 됩니다.
'''

def get_average_score(scores):
    sum_scores = 0
    cnt = 0 
    if len(scores)>0:
        for score in scores:
            if len(score)==0:
                continue
            # '점'이라는 글자를 제거합니다.
            point = score[:-1]
            cnt +=1
            sum_scores += int(point)
        if cnt>0:
            average = sum_scores / cnt
            return str(average) + '점'
        else:
            return None
    else:
        return None

print(get_average_score(['20점', '55점', '30점']))
print(get_average_score(['', '30점']))
print(get_average_score(['', '']))


'''
위 문제에서 if, else로 예외처리를 해주었던 부분을 try, except로 처리해주기
'''


def get_average_score(scores):
    sum_scores = 0
    valid_score_count = 0

    for score in scores:
        try:
            sum_scores += int(score[:-1]) # 예외 발생하는 구간, 빈 문자가 들어올 경우 '점'제외하고 int로 바꿀 수 없는 ValueError가 발생
            valid_score_count += 1
        except ValueError:
            pass
            
    try:
        average = sum_scores / valid_score_count
        return str(average) + '점'
    except ZeroDivisionError:
        return None
            

print(get_average_score(['20점', '55점', '30점']))
print(get_average_score(['', '30점']))
print(get_average_score(['', '']))
