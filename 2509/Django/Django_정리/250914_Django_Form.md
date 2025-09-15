# Form
- 사용자로부터 데이터를 제출 받기위해 활용한 방법


## 유효성 검사
- 데이터베이스 무결성
- 데이터가 유효한지 확인하는 과정
- 보안 강화


## Widget
- widget=forms.Textarea


## Django ModelForm
- field
  * 보여지고 싶은 것
- exclude
  * 노출 제외하고 싶은 것


## save()
- 생성과 수정을 구분하는 법
  * instance 인자 이용


## HTTP 요청 다루기
- 2개의 view 함수를 하나로 구조화


- {{form.필드명.errors}}
- <label for="{{ form.필드명.id_for_label}}">ㅏㄹ베