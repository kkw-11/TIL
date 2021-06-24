from user import User

class Post:

    # 생성자는 매개변수로 작성자와 내용을 받아,
    # 그 값을 속성에 저장합니다.
    def __init__(self, author, content):
        self.author = author
        self.content = content
        
        # 속성들을 초기화합니다.
        # 아래의 pass를 지우고 코드를 작성하세요.
        self.comments = []
        self.likes = 0

# 새로운 사용자 me를 생성합니다.
# User의 생성자에 원하는 이름(문자열)을 넣어주세요.
me = User("elice")

# 아래의 None을 지우고 코드를 작성하세요.
my_post = Post(me,"commit")
