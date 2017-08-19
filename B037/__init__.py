# coding:utf8
'''https://paiza.jp/challenges/161/page/problem'''

[M, D] = map(int, raw_input().split(" "))  # 一行输入两个值的技巧
[a1, a2, a3, a4] = map(int, raw_input().split(" "))
[b1, b2, b3, b4] = map(int, raw_input().split(" "))
[m1, m2, m3, m4] = map(int, raw_input().split(" "))
[w, x, y, z] = [0, 0, 0, 0]
MD = map(lambda x: x if (len(x) > 1) else '0' + x, map(str, [M, D]))
MD = map(int,MD[0]+MD[1])#字符串'0303'变成数组[0,3,0,3]
MD.sort()

def isLucky(x, y, z, w):
    list = map(lambda x: x % 10, [x, y, z, w])
    list.sort()
    if MD == list:
        return True

count = 0
while True:
    w = (a1 * w + b1) % m1
    x = (a2 * x + b2) % m2
    y = (a3 * y + b3) % m3
    z = (a4 * z + b4) % m4
    count+=1
    if(isLucky(x,y,w,z)):
        print count
        break
'''
提出コード結果詳細

テスト番号
入力ケース番号	ジャッジ結果	実行時間
テスト 1
ケース 1（境界値データ）
通過
0.02 秒
ケース 2（基本データ）
通過
0.02 秒
テスト 2
ケース 1（基本データ）
通過
0.03 秒
テスト 3
ケース 1（基本データ）
通過
0.03 秒
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
0.02 秒
テスト 7
ケース 1（基本データ）
通過
0.03 秒
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
