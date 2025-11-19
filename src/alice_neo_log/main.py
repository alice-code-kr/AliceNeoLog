from email import message
from neo_chat_bot import NeoChatBot
import people_1
import people_2
import people_3





def main():
 one_grade = people_1.Student1("다연",1,"흰색")
 two_grade = people_2.Student2("도경",2,"노란색")
 three_grade = people_3.Student3("승연",3,"하늘색") 

 while True:  
    grade = int(input("학년을 입력하세요. (숫자만): "))

    school_dic = {
      1: one_grade,
      2: two_grade,
      3: three_grade 
    }
    if grade in school_dic:
        print(school_dic[grade])
    else:
        print("1~3만 가능합니다.")

   

       

#  def test_decorator(func):
#     def wrapper():
#         print("이건 출력 전임")
#         func()
#         print("이건 출력 후라고 그러더라고")

#     return wrapper
# #데코레이터
#  @test_decorator
#  def hello():
#    print("안녕")

# #  hello = test_decorator(hello)
#  hello()
# #()를 붙이면 실행, ()를 안 붙이면 함수 그 자체를 값으로 전달

#  def plus(*numbers):
#     print(numbers)
#  plus(2,3,4)

#  def name_color(**data):
#     print(data)
#  name_color(name = "승연",color = "보라색")   

# #  def add(x):
# #     return x + 1 은 아래의 코드와 같다.(람다로 나타내면 일케 됨)
# #람다는 함수다!
# #  lambda x: x + 1

# #보통 변수에 저장해 사용
#  hehe = lambda x: x + 1
#  print(hehe(99))

#  hi = ["안","녕","하","세","요"]
#  print(len(hi))
#  print(hi[0])

#  tel = {'m': 4345, 'n': 2048}
#  tel['b'] = 10
#  print(tel['m'])
#  print(tel)


#  for k in reversed(range(10)):
#     print(k)
#  print("웃기노")
#  cookie = [3,2,3,5,2,1,5,2,4,3,4,1,4,2,3,2,4,12,4,2,3,2,1,4,5,3,5,2,4,2,42,2]
#  for i in sorted(cookie):
#     print(i)


 


#     neo_chat_bot =  NeoChatBot()
#     message = input("메세지를 입력하세요: ")
#     neo_chat_bot.ask(message)




#  if __name__ == "__main__":
#     main()
main()