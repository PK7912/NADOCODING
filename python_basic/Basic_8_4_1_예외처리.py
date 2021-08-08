try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}" .format(num1, num2, int(num1/num2)))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")  # 잘못된 입력값을 넣었을때, ex) 삼,넷 ....한글등 입력시 오류
except ZeroDivisionError as err:  # 0을 입력했을시 나오는 에러
    print(err)
except:
    print("알 수 없는 에러가 발생하였습니다.")

    # except 에 정확한 에러 내용작성시 알아보기가 쉬움, 그외에 통합에러 지정시 정확한 에러 이유는 알수 없음
