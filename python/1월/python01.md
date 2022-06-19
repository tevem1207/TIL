# python

### 기초 문법

파이썬에서 제공하는 스타일 가이드인 `PEP-8` 준수할것.

- 들여쓰기 4칸
- a = 'apple'
  - 띄어쓰기 잘 하고

### 변수 할당

같은 값을 동시에 할당 가능

```python
x = y = 100
print(x, y)
```

다른 값을 동시에 할당 가능

```python
x, y = 1, 2
print(x, y)
```

- x, y의 값을 서로 바꿀 때

```python
x, y = y, x
```

```python
x = x + y
y = x - y
x = x - y
```

### 식별자

변수, 함수, 모듈 클래스 등을 식별하는데 사용되는 이름

```python
import keyword
print(keyword.kwlist)
```

- 변수를 할당할 때 주의할 것



### input

```python
data = input()
```

input은 항상 문자열의 형태로 반환