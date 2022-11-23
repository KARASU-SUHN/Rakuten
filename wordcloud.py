from wordcloud import WordCloud
# import re
# from PIL import Image
# import numpy as np

# text = open('/Users/karasu/Downloads/top.txt').read()
# wordcloud = WordCloud(
#             font_path='/Library/Fonts/Arial Unicode.ttf', # フォントファイルの指定
#             background_color="whitesmoke",
#             colormap="tab10",
#             width=400,
#             height=200
#             ).generate(text)
# wordcloud.to_file("/Users/karasu/Downloads/1.png")

#colormap: https://karupoimou.hatenablog.com/entry/2019/05/17/153207

text = open('/Users/karasu/Downloads/genre.txt').read()
wordcloud = WordCloud(
            font_path='/Library/Fonts/Arial Unicode.ttf', # フォントファイルの指定
            background_color="whitesmoke",
            colormap="tab10",
            width=400,
            height=200
            ).generate(text)
wordcloud.to_file("/Users/karasu/Downloads/genre.png")
