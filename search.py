
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

import csv




def search():
    """
    リスト検索処理。標準入力（input）とリストの値を照合。
    標準入力の結果がリストに存在しない場合はリストに追加
    """
    source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
    
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    if word in source:
        print('よくご存知で')
    else:
        print('その様なキャラクターは存在しません')
        source.append(word)

    
    with open('kimetu_character.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(source)


if __name__ == "__main__":
    search()
