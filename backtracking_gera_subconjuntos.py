def backtracking(node, conjunto, subconjuntos, t_min, t_max):
	if len(node[0]) >= t_max:
		subconjuntos += [tuple(node[0])] # adiciono o subconjunto pois ele jah atingiu o t_max e soh vai gerar filhos de tamanhos que naum me interessam
	elif node[1] < len(conjunto): # se ainda tiver como gerar mais nodes filhos eu os gero
		ponteiro = node[1] + 1
		backtracking([node[0], ponteiro], conjunto, subconjuntos, t_min, t_max) # naum adiciono novo item
		backtracking([node[0] + [conjunto[ponteiro-1]], ponteiro], conjunto, subconjuntos, t_min, t_max) # adiciono o novo item
	else: # nesse caso, naum tem mais para onde descer na minha arvore (naum tem mais como gerar nodes filhos)
		if len(node[0]) >= t_min:
			subconjuntos += [tuple(node[0])] # adiciono o subconjunto pois ele tem o tamanho minimo estipulado (t_min)

def gera_conjunto(n): # conjunto do tipo {1, 2, 3, ..., n}
	return range(1, n + 1)

def gera_subconjuntos(n, t_min, t_max):
	node = [[], 0]
	conjunto = gera_conjunto(n)
	print "conjunto:", conjunto
	subconjuntos = []
	backtracking(node, conjunto, subconjuntos, t_min, t_max)
	print subconjuntos

# main
gera_subconjuntos(5, 2, 4)