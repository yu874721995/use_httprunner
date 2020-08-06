import re
import collections
import numpy as np
import jieba
from PIL import Image
import wordcloud

import matplotlib.pyplot as plt

# 读取文件
fn = open('ls.txt','rt') # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
object_list = []
remove_words = [u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
                u'通常',u'如果',u'我们',u'需要',u'陌声',u'可以',u'用户',u'聊天',u'平台',u'免费',u'回复',u'软件',u'开发者',u'你',u'您',u'我',u'您好',
                u'有',u'就',u'适合',u'祝您',u'认可',u'正规',u'主打',u'真人',u'语音',u'根据',u'视频',u'交友平台',u'真实',u'另一半',u'所有',u'遇见',u'搭讪',u'评论'
                ,u'快速',u'自身',u'同城',u'均',u'理性',u'已经',u'被',u'已',u'已被',u'该条',u'删除'] # 自定义去除词库

for word in seg_list_exact: # 循环读出每个分词
    if word not in remove_words: # 如果不在去除词库中
        object_list.append(word) # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词
print (word_counts_top10) # 输出检查

# 词频展示
mask = np.array(Image.open('girl.jpg')) # 定义词频背景
wc = wordcloud.WordCloud(
    background_color='white',#设置背景颜色
    font_path='C:/Windows/Fonts/simhei.ttf', #设置字体格式
    mask=mask, # 设置背景图
    max_words=200, # 最多显示词数
    max_font_size=100 # 字体最大值
)

wc.generate_from_frequencies(word_counts) # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立字体颜色方案
wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像