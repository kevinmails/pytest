import jieba

"""
使用中文分词

"""
seg_list = jieba.cut("我心里有个梦，去上嵩山少林学武功！")

for seg in seg_list:
    print(seg)


print(",".join(seg_list))

