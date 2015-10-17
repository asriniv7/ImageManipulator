from PIL import Image
import os
from os.path import isfile,join

for root, dirs, files in os.walk(os.getcwd()):
		print root
		print "\n .......... "
		for f in files:
			if f.endswith('.jpg'):
				path = join(root,f)
				im = Image.open(path)
				new_path = path.replace('.jpg', '_flipped.jpg')
				im.transpose(Image.FLIP_LEFT_RIGHT).save(new_path)
		#print root
		print " \t finished \n"