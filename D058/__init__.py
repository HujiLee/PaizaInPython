input_lines = raw_input().split(" ")
input_lines = map(lambda x: int(x), input_lines)
output = ""

for index, element in enumerate(input_lines):
    output = output + (('A' if (index % 2 == 0) else 'B') * element)

print output
'''
提出コード結果詳細

テスト番号
入力ケース番号	ジャッジ結果	実行時間
テスト 1
ケース 1（基本データ）
通過
0.02 秒
テスト 2
ケース 1（基本データ）
通過
0.02 秒
テスト 3
ケース 1（基本データ）
通過
0.02 秒
テスト 4
ケース 1（基本データ）
通過
0.02 秒
テスト 5
ケース 1（基本データ）
通過
0.02 秒
テスト 6
ケース 1（基本データ）
通過
0.04 秒
テスト 7
ケース 1（基本データ）
通過
0.02 秒
テスト 8
ケース 1（基本データ）
通過
0.02 秒
テスト 9
ケース 1（基本データ）
通過
0.02 秒
テスト 10
ケース 1（基本データ）
通過
0.02 秒
'''