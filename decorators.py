def hello(f): #Function 만들기
    def greeting():
        print("^_____^")
        f()
        print("ㅠㅠ")
    return greeting()
    
@hello #데코레이터 -> 이게 위 함수의 인자(f)로 들어가서 실행이 된다.
def korean():
    print("안녕하세요")
    
@hello
def english():
    print("hello")
    
korean()
english()