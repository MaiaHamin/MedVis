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
like_paths = []
share_paths = []
for mc in medcos:
	likename = mc + "_likes.json"
	likepath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "jsons", likename))
	sharename = mc + "_shares.json"
	sharepath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "jsons", sharename))
	like_paths.append(likepath)
	share_paths.append(sharepath)


fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
colors = ["xkcd:forest green", "xkcd:light green", "xkcd:green", "xkcd:turquoise", "xkcd:blue green", "xkcd:light blue", "xkcd:periwinkle", "xkcd:royal blue", "xkcd:red", "xkcd:maroon", "xkcd:rose"]


for i in range(len(medcos)):
	like_d=open(like_paths[i]).read()
	like_p = json.loads(like_d)
	share_d=open(share_paths[i]).read()
	share_p = json.loads(share_d)
	like_nums = []
	share_nums = []
	labels = []
	

	for story in like_p[:10]:
		like_nums.append(story["Facebook Likes"])
		share_nums.append(int(story["Facebook Shares"]) + int(story["Facebook Comments"]))
		labels.append(medcos[i] + ": " + story["Headline"])

	scatter = ax.scatter(like_nums, share_nums, s=15**2, alpha=0.5, color=colors[i], label=medcos[i], marker='o')
	tooltip = mpld3.plugins.PointHTMLTooltip(scatter, labels=labels, css=css)
	mpld3.plugins.connect(fig, tooltip)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.set_title('Top Stories by Differing Metrics', fontsize=25)
ax.set_xlabel('Likes', fontsize=18)
ax.set_ylabel('Shares and Comments', fontsize=16)
handles, labels = ax.get_legend_handles_labels() # return lines and labels
interactive_legend = mpld3.plugins.InteractiveLegendPlugin(zip(handles,
                                                         ax.collections),
                                                     labels,
                                                     alpha_unsel=0.0,
                                                     alpha_over=1.5, 
                                                     start_visible=True)
mpld3.plugins.connect(fig, interactive_legend)




mpld3.show(fig)

