import matplotlib.pyplot as plt
from skimage import io

filename = 'vingadores.jpg'

img = io.imread(filename)

rows, cols, dim = img.shape

for n in range(3):
	img_out = img.copy()
	for i in range(rows):
		for j in range(cols):
			if n != 0: img_out[i, j, 0] = 0
			if n != 1: img_out[i, j, 1] = 0
			if n != 2: img_out[i, j, 2] = 0
	plt.figure(n)
	io.imshow(img_out)

io.show()