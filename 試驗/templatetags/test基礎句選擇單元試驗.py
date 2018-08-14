from django.test.testcases import TestCase
from 標記.管理.基礎句選擇 import 基礎句選擇表
from 標記.templatetags.ki1_tshoo2_ku3_tags import _揀的最新一句
from django.utils.timezone import now


class 基礎句選擇Tag單元試驗(TestCase): 

    # template tag
    def test猶未揀_id是None(self):
        基礎句選擇表.objects.create(原本漢字='漢', 原本羅馬字='han')
        self.assertEqual(_揀的最新一句(), 0)

    def test揀2_id是2(self):
        for 資料 in range(2):
            先標記無 = False
            if 資料 == 1:
                先標記無 = True
            基礎句選擇表.objects.create(
                原本漢字=資料, 原本羅馬字=資料, 
                先標記無=先標記無, 揀的時間=now())
        self.assertEqual(_揀的最新一句(), 2)
         
    def test揀23_id是3(self):
        # 1x 2v 3v => 顯示id = 3
        for 資料 in range(3):
            基礎句選擇表.objects.create(
                原本漢字=資料, 原本羅馬字=資料, 揀的時間=now())
        self.fail()
 
    def test莫揀1_id維持3(self):
        # 1v 2v 3v =>  
        # 1x 2v 3v => 顯示id = 3
        self.fail()
    
    def test加莫揀4_id改4(self):
        # 1v 2v 3v =>  
        # 1v 2v 3v 4x => 顯示id = 4
        self.fail()
    
    def test上大3改莫揀_id維持3(self):
        # 1v 2v 3v =>  
        # 1v 2v 3x => 顯示id = 3
        self.fail()

