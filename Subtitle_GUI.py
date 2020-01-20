from tkinter import *
from tkinter import ttk
import Sub_downloader
import threading


def find_subs(*args):
	try:
		# vidID = (url.get())
		the_subs = Sub_downloader.yt_trans(url.get())
		print(the_subs)
		subtitles.set(the_subs)
	except ValueError:
		pass

root = Tk()
root.title("Subtitles from Youtube")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


url = StringVar()
subtitles = StringVar()
feet_entry = ttk.Entry(mainframe, width=30, textvariable=url)
feet_entry.grid(column=1, row=1, columnspan = 2, sticky=(W, E))


s = ttk.Label(mainframe, textvariable=subtitles, wraplength=500).grid(column=1, row=4, sticky=(W, E), columnspan=2)



### Code I can't get working here commented out ###
# scrollbar = ttk.Scrollbar(mainframe, command=s.yview)
#scrollbar.grid(column=3, row=4, sticky=E)
###threading being used to keep TKinter from freezing



ttk.Button(mainframe, text="Find Subtitles", command=threading.Thread(target=find_subs).start()).grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Video URL").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="SUBTITLES BELOW").grid(column=2, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind('<Return>', find_subs)

root.mainloop()
