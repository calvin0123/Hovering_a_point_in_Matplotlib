import matplotlib.pyplot as plt 
import numpy as np


pizza = ['Honey Cheese', 'Margarita', 'Seafood', 'Onion pork']			# xLabel is the flavor of pizza
num = [10, 12 , 5, 7]													# yLabel is the total sales of each flavor

num_d = {'family':[4,4,2,2], 'couple':[3,4,1,3], 'alone':[3,4,2,2]}		# Dict shows the sales of flavor of each group 

fig,ax = plt.subplots()
sc = plt.scatter(pizza, num)

# annotation
annot = ax.annotate("", xy=(0,0), xytext=(20,20), textcoords='offset points',
					  bbox=dict(boxstyle='round', fc='w'),
					  arrowprops=dict(arrowstyle='->'))
annot.set_visible(False)


def update_annot(ind):
	"""
	This function updates the annotation.
	:param ind:(dict)
	"""
	pos = sc.get_offsets()[ind["ind"][0]]
	annot.xy = pos

	k_lst = []
	v_lst = []
	for k, v in num_d.items():
		k_lst.append(k)
		v_lst.append(v)

	ans_lst = []
	for line in v_lst:
		ans_lst.append(line[int(ind['ind'])])
	
	text = f"{k_lst[0]}:{ans_lst[0]}\n{k_lst[1]}:{ans_lst[1]}\n{k_lst[2]}:{ans_lst[2]}"
						  							 
	annot.set_text(text)


def hover(event):
	# bool
	vis = annot.get_visible()
	# if on the point, update the annot and show on the canvas
	if event.inaxes == ax:
 		cont, ind = sc.contains(event)
 		if cont:
 			update_annot(ind)
 			annot.set_visible(True)
 			fig.canvas.draw_idle()
 		else:
 			# not on the point, so will not show any annot
 			if vis:
 				annot.set_visible(False)
 				fig.canvas.draw_idle()


fig.canvas.mpl_connect("motion_notify_event", hover)
plt.show()

