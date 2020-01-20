import ID_finder as id
import Sub_downloader as sd



keepGoing=True
while keepGoing:

	for each in id.JRE_ids[70:100]:
		print(each)
		sd.yt_search(each, "was talking", True)
		keepGoing=False

