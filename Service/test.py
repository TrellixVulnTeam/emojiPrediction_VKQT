import numpy as np
import tensorflow as tf
import collections
import pdb
import ptb.conf as conf

src = "💋💕 👶🏻   😂 。 ， test 发 i'm used ! * Please  tɦaռҡs"
l = len(src)
for i in range(l):
    if src[i] in conf.emojiList:
        print(src[i])

# print(isEmoji(r'\U0001F600'))