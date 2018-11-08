import pyexcel 
from collections import OrderedDict

#2 prepate data
music = [
    OrderedDict({
        'name_song': 'mưa',
        'by':'trung'
    }),
    OrderedDict({
        'name_song':'rơi',
        'by':'trung1'
    }),
    OrderedDict({
        'name_song':'xuống',
        'by':'trung2'
    }),
    OrderedDict({
        'name_song':'thềm',
        'by':'trung3'
    }),
]

#3 Save file using save_as
pyexcel.save_as(records = music, dest_file_name="your_file.xls")