import matplotlib.pyplot as plt
from skimage import io

path = '../imagens/'
filename_main = 'USF4_Logo.bmp'
filename_background = 'vingadores.jpg'

img_main = io.imread(path + filename_main)
img_background = io.imread(path + filename_background)
img_out = img_main.copy()

rows, cols, dim = img_main.shape

background_color = img_main[0, 0]

for i in range(rows):
	for j in range(cols):
		sets = set(background_color == img_out[i, j])
		if len(sets) <= 1 and sets == {True}:
			img_out[i, j] = img_background[i, j]

plt.figure('InMain')
io.imshow(img_main)
plt.figure('InBackground')
io.imshow(img_background)
plt.figure('Out')
io.imshow(img_out)

io.show()
