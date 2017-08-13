import os
import zipfile
from pathlib import Path
def groot():
	my_file = Path("/home/dinesh/work/text.zip")
	if my_file.is_file():
		s=(text.zip).extractall()
		for each in s:
			if each.is_file():
				text_file = open("groot.txt", "r")
				print text_file.read()
				text_file.close()
print(groot())
	