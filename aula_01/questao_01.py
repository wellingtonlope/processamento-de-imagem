import matplotlib.pyplot as plt
from skimage import io

filename = 'vingadores.jpg'

img = io.imread(filename)
img_out = img.copy()

rows, cols, dim = img.shape

n = 50
x = round(rows / 2) - n
y = round(cols / 2) - n

for i in range(2 * n):
	for j in range(2 * n):
		img_out[x + i, y + j] = [0, 0, 0]

plt.figure('In')
io.imshow(img)
plt.figure('Out')
io.imshow(img_out)
io.show()

io.imsave('img_qt_01.jpg', img_out)