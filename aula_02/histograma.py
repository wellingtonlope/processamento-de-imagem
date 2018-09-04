class Histograma(object):
	im_h = ''
	im_hn = ''
	im_hEq = ''
	im_hnEq = ''
	im_hCut = ''
	im_hCutN = ''
	img = ''
	img_out = ''
	def __init__(self, im_h, im_hn, im_hEq, im_hnEq, im_hCut, im_hCutN, img, img_out):
		self.im_h = im_h
		self.im_hn = im_hn
		self.im_hEq = im_hEq
		self.im_hnEq = im_hnEq
		self.im_hCut = im_hCut
		self.im_hCutN = im_hCutN
		self.img = img
		self.img_out = img_out


def imgHist(img):
	"""
	Gera dois vetores representando o histograma da imagem
	um absoluto e um normalizado

	:param img:
	:return im_h, im_hn:
	"""
	rows, cols = img.shape
	im_h = [0] * 256
	im_hn = im_h.copy()
	MN = rows * cols

	for i in range(rows):
		for j in range(cols):
			im_h[img[i, j]] += 1
			im_hn[img[i, j]] += 1 / MN

	return im_h, im_hn


def histCut(im_h, v_cut):
	"""
	Realiza o corte de v_cut% no maior valor do histograma e redistribui para
	outros niveis de escala de cinza
	:param im_h, v_cut:
	:return:
	"""

	h_max = max(im_h)  # maior altura (ou valor) do histograma
	h_cut = round(h_max * (1 - v_cut))  # valor de corte
	h_Scut = 0  # total para ser cortado

	for i in range(len(im_h)):
		if h_cut < im_h[i]:  # verifica se a valor é maior que o valor de corte
			h_Scut += (im_h[i] - h_cut)  # salva em uma variavel a diferença do corte
			im_h[i] = h_cut  # atribui o valor de corte ao valor que era maior

	d_cut = h_Scut // len(im_h)  # divisão para saber quanto será atribuido para cada nivel

	for i in range(len(im_h)):  # faz a distribuição dos valores
		im_h[i] = im_h[i] + d_cut

	return im_h


def imEqHistWithCut(img, cut):
	"""
	realiza equalizacao de histograma
	em uma imagem (8 bits) em escala de cinza
	:return: imagem em escala de cinza(vetor) e seus vetores de histogramas
	"""
	rows, cols = img.shape
	MN = rows * cols
	L = 256

	im_h, im_hn = imgHist(img)
	im_hCut = histCut(im_h.copy(), cut)
	im_hCutN = [i / MN for i in im_hCut]
	s_k = [0] * 256

	im_hCut_ac = im_hCutN.copy()
	s_k[0] = round(255 * im_hCut_ac[0])

	su = 0
	for i in range(L):
		su += im_hCut_ac[i]
		s_k[i] = round(su * (L - 1))

	img_out = img.copy()
	for i in range(rows):
		for j in range(cols):
			img_out[i, j] = s_k[img[i, j]]

	im_hEq = [0] * 256
	im_hnEq = im_hEq.copy()

	for i in range(rows):
		for j in range(cols):
			im_hEq[img_out[i, j]] += 1
			im_hnEq[img_out[i, j]] += 1 / MN

	return Histograma(im_h, im_hn, im_hEq, im_hnEq, im_hCut, im_hCutN, img, img_out)


def equalizacao(img):
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

	saida = n_k, pr_rk, out_n_k, out_pr_rk, img, out_img

	return saida
