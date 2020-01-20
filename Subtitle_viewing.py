import ID_finder as id
import Sub_downloader as sd



keepGoing=True
while keepGoing:

	for each in id.JRE_ids:
		print(each)
		sd.yt_search(each, "have you seen ", True)
		keepGoing=False

