num1_str = input('最初の数字を入力してください：')
num1 = int(num1_str)

num2_str = input('2番目の数字を入力してください：') # 2つ目の数字を入力してもらう
num2 = int(num2_str) # 2つ目の数字を正数に変換

result = num1 + num2 # 2つの数字を足し算する
print('足し算の結果は：', result) # 結果を表示する
# ここまでが足し算のコード

result_sub= num1 = num2 # 2つの数字を引き算する
print('引き算の結果は：' , result_sub) # 結果を表示する

result_mul = num1 * num2 # 2つの数字を掛け算する
print('掛け算の結果は：', result_mul) # 結果を表示する

result_div = num1 / num2 # 2つの数字を割り算する
print('割り算の結果は:', result_div) # 結果を表示する
