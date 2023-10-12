import random
import string

def generate_password(length):
   # 使用する文字の範囲
   characters = string.ascii_letters + string.digits + string.punctuation
   # ランダムな文字からパスワードを生成
   password = ''.join(random.choice(characters) for _ in range(length))
   return password

if __name__ == "__main__":
   while True:
       length_input = input("パスワードの長さを入力してください: ")

       if length_input.strip() == '':
           print("エラー: 長さが空欄です。再度入力してください。")
       elif length_input.isdigit():
           length = int(length_input)
           password = generate_password(length)
           print("生成されたパスワード:", password)
           break
       else:
           print("エラー: 数字以外が入力されています。再度入力してください。")