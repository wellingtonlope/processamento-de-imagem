import matplotlib.pyplot as plt
from skimage import io


def equalizacaoHistograma(img):
	rows, cols = img.shape
	L = 256
	n_k = [0] * L
	pr_rk = [0] * L
	t_rk = [0] * L
	s_k = [0] * L

	out_n_k = [0] * L
	out_pr_rk = [0] * L
	out_img = img.copy()

	MN = rows * cols
	for i in range(rows):
		for j in range(cols):
			n_k[img[i, j]] += 1
			pr_rk[img[i, j]] += 1 / MN

	su = 0
	for i in range(L):
		su += pr_rk[i]
		t_rk[i] = su * (L - 1)

	s_k = [round(i) for i in t_rk]

	for i in range(rows):
		for j in range(cols):
			out_img[i, j] = s_k[img[i, j]]


	for i in range(rows):
		for j in range(cols):
			out_n_k[out_img[i, j]] += 1
			out_pr_rk[out_img[i, j]] += 1 / MN

	plt.figure('n_k')
	plt.bar(range(256), n_k)

	plt.figure('pr_rk')
	plt.bar(range(256), pr_rk)

	plt.figure('out_n_k')
	plt.bar(range(256), out_n_k)

	plt.figure('out_pr_rk')
	plt.bar(range(256), out_pr_rk)

	plt.figure('img')
	io.imshow(img)

	plt.figure('out_img')
	io.imshow(out_img)

	io.show()


filename = 'pout.tif'
img = io.imread(filename)

equalizacaoHistograma(img)
