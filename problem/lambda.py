import string
import random

# nameを受け取り、文字列を返す関数
def greetingFn(name):
   return "Hello there " + name + " from Fn."

# nameを受け取り文字列を返す無名関数を変数へ代入
greetingLambdaFn = lambda name: "Hello there " + name + " from Lambda."

# 文字をランダムに選び、名前を作る関数
def nameGenerator():
   data = string.digits + string.ascii_lowercase
   return ''.join([random.choice(data) for _ in range(10)])

# 入力として関数への参照を受け取ることができます。
def multiCall(f, fInputF, message):
   return f(fInputF()) + "......" + message

print(multiCall(greetingFn, nameGenerator, "Thank you"))
print(multiCall(greetingLambdaFn, nameGenerator, "Thank you"))