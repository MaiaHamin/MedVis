import json
import time
import os
import sqlite3
import numpy as np
import matplotlib.pyplot as plt, mpld3
from matplotlib.font_manager import FontProperties

# Define some CSS to control our custom labels
css = """

text.mpld3-text, div.mpld3-tooltip {
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
  opacity: 1.0;
  padding: 2px;
  border: 0px;

}
"""

medcos = ["WaPo", "NYT", "CNN", "WSJ", "Buzzfeed", "OccupyDems", "UpWorthy", "NowThis", "FFA", "ForAmerica", "Fox"]
cats = ["Link", "Photo", "Native Video", "Live Video", "Status"]
like_paths = []
share_paths = []
com_paths = []
for mc in medcos:
	likename = mc + "_likes.json"
	likepath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "jsons", likename))
	sharename = mc + "_shares.json"
	sharepath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "jsons", sharename))
	comname = mc + "_comments.json"
	compath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "jsons", comname))
	com_paths.append(compath)
	like_paths.append(likepath)
	share_paths.append(sharepath)


fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
colors = ["xkcd:forest green", "xkcd:light green", "xkcd:green", "xkcd:turquoise", "xkcd:blue green", "xkcd:light blue", "xkcd:periwinkle", "xkcd:royal blue", "xkcd:red", "xkcd:maroon", "xkcd:rose"]
like_nums = [0, 0, 0, 0, 0]
share_nums = [0, 0, 0, 0, 0]
com_nums = [0, 0, 0, 0, 0]

for i in range(len(medcos)):
	like_d=open(like_paths[i]).read()
	like_p = json.loads(like_d)
	share_d=open(share_paths[i]).read()
	share_p = json.loads(share_d)
	com_d=open(com_paths[i]).read()
	com_p = json.loads(com_d)

	for story in like_p[:10]:
		like_nums[cats.index(story["Facebook Media Type"])] = like_nums[cats.index(story["Facebook Media Type"])] + 1
	for story in com_p[:10]:
		com_nums[cats.index(story["Facebook Media Type"])] = com_nums[cats.index(story["Facebook Media Type"])] + 1
	for story in share_p[:10]:
		share_nums[cats.index(story["Facebook Media Type"])] = share_nums[cats.index(story["Facebook Media Type"])] + 1

x = np.arange(15)
all_nums = like_nums + share_nums + com_nums
all_cats = cats + cats + cats
ax.bar(x, all_nums)
ax.set_xticks(x, all_cats)

mpld3.to_html(fig)