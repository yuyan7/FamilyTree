# coding: utf-8
"""
Peopleモデルの定義
"""
from django.db import models


SEX_LIST = (
    (None, ''),
    (True, '男'),
    (False, '女')
)

class People(models.Model):
    name = models.CharField(verbose_name='名前', max_length=50)
    birthday = models.DateField(verbose_name='誕生日')
    sex = models.NullBooleanField(verbose_name='性別', default=None, choices=SEX_LIST)
    dieday = models.DateField(verbose_name='没年月日', blank=True, null=True)
    marriage = models.ForeignKey('self', related_name='marriage_people',
                                 verbose_name='婚約者', blank=True, null=True)
    marriage_flg = models.BooleanField(verbose_name='婚約者フラグ', default=False)
    parent = models.ForeignKey('self', related_name='parent_people', verbose_name='親',
                               blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人'
        verbose_name_plural = '人々'

    def toJson(self, generation, parent_node):
        """
        家系図出力用のjsonファイルに変換します。
        """
        disp_dieday = None
        if self.dieday is not None:
            disp_dieday = self.dieday.strftime('%Y/%m/%d')

        return {
            'id': self.name + str(self.pk),
            'name': self.name,
            'birthday': self.birthday.strftime('%Y/%m/%d'),
            'sex': self.sex,
            'dieday': disp_dieday,
            'display': True,
            'generation': generation,
            'marriage_flg': self.marriage_flg,
            'parent_node': parent_node
        }