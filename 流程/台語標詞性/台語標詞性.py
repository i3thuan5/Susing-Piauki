
from os.path import join, splitext
from posix import listdir
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.斷詞.語言模型揀集內組 import 語言模型揀集內組
from 臺灣言語工具.語言模型.語言模型 import 語言模型
from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.組 import 組


class 台語斷詞(語言模型):
    def __init__(self):
        self.詞性ngram = KenLM語言模型('詞性.arpa')
        self.詞性詞頭機率 = self.讀詞頭尾機率('詞頭')
        self.詞性詞尾機率 = self.讀詞頭尾機率('詞尾')
        self.全部詞性 = sorted(self.詞性詞尾機率.keys())

    def 讀詞頭尾機率(self, 資料夾):
        lm機率 = {}
        for 檔案 in sorted(listdir(資料夾)):
            if 檔案.endswith('.arpa'):
                lm機率[splitext(檔案)[0]] = KenLM語言模型(join(資料夾, 檔案))
        return lm機率

    def 上濟詞數(self):
        return self.詞性ngram.上濟詞數()

    def 評詞陣列分(self, 詞陣列, 開始的所在=0):
        for 詞物件, ngram機率 in zip(詞陣列[開始的所在:], self.詞性ngram.評詞陣列分(詞陣列, 開始的所在)):
            字頭物件 = 詞物件.篩出字物件()[0]
            字尾物件 = 詞物件.篩出字物件()[-1]
            try:
                詞頭機率 = list(self.詞性詞頭機率[詞物件.詞性].評詞陣列分([詞([字頭物件])]))[0]
                詞尾機率 = list(self.詞性詞尾機率[詞物件.詞性].評詞陣列分([詞([字尾物件])]))[0]
                print(
                    詞物件, 詞物件.詞性, [詞([字頭物件])], [詞([字頭物件])], [詞([字尾物件])],
                    ngram機率 + 詞頭機率 + 詞尾機率,
                    ngram機率, 詞頭機率, 詞尾機率
                )
                yield ngram機率 + 詞頭機率 + 詞尾機率

            except AttributeError:  # </s>
                yield ngram機率


if __name__ == '__main__':
    斷詞 = 台語斷詞()
    print(斷詞.全部詞性)
    句物件 = 拆文分析器.分詞句物件('逐-家｜tak8-ke1 做-伙｜tso3-hue2')
    句物件 = 拆文分析器.分詞句物件('逐-家 做-伙')
    新句物件 = 拆文分析器.建立句物件('')
    print(句物件)
    for 詞物件 in 句物件.網出詞物件():
        新集物件 = 拆文分析器.建立集物件('')
#         for 詞性 in 斷詞.全部詞性:
        for 詞性 in ['Nh', 'D']:
            組物件 = 組([詞物件])
            組物件.網出詞物件()[0].詞性 = 詞性
            新集物件.內底組.append(組物件)
        新句物件.內底集.append(新集物件)
    for 詞物件 in 新句物件.揀(語言模型揀集內組, 斷詞).網出詞物件():
        print(詞物件, 詞物件.詞性)
