from django.utils.timezone import now
from 標記.models import 語料表
from 標記.管理.語料表管理 import 語料表管理


class 基礎句選擇表(語料表):

    class Meta:
        proxy = True
        verbose_name = "基礎句選擇"
        verbose_name_plural = verbose_name


class 基礎句選擇管理(語料表管理):
    list_display = [
        'id', '先標記無',
        '來源',
        '漢字', '羅馬字',
        '揀的時間',
        '備註',
    ]
    ordering = ['id', ]
    search_fields = [
        'id', '漢字', '羅馬字',
    ]

    fieldsets = (
        ('漢字', {
            'fields': ('漢字', '羅馬字', '備註', ),
            'classes': ['wide']
        }),
    )
    actions = [
        '這幾句先標記',
        '這幾句先莫標記',
        '這幾句kap做伙',
    ]

    change_list_template = 'admin/標記/ki1_tshoo2_ku3_change_list.html'

    def 這幾句先標記(self, request, queryset):
        queryset.update(揀的時間=now(), 先標記無=True)

    def 這幾句先莫標記(self, request, queryset):
        queryset.update(揀的時間=now(), 先標記無=False)
