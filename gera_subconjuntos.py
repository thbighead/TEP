# TAH ERRADO, devia pegar somente os subconjuntos com tamanho entre t_min e t_max, eu fiz pensando em pegar os
# subconjuntos que podem ser gerados com os itens do conjunto original que estam nas posicoes entre t_min e t_max XD

# explicacao marota:
# para aproveitar os mesmos lacos jah feitos para encontrar os subconjuntos que sao apenas 'cortes' do conjunto original,
# esse teste eh feito para encontrar os subconjuntos que sao um pouco mais complicados que simplesmente 'tapar' parte do inicio
# e/ou do fim do conjunto original.

def gera_subconjuntos(n, t_min, t_max):
	subconjuntos = []
	subconjuntos_unitarios = [] # na verdade isso aqui eh soh uma lista que vai 'marcar' os elementos do conjunto pelos quais jah passei
	k = 0
	conjunto = range(1, (n + 1)) # conjunto com os elementos {1, 2, 3, ..., n}

	for i in xrange(t_min, (t_max + 1)):
		subconjunto = []
		subconjuntos_unitarios += [conjunto[i]]

		if len(subconjuntos_unitarios) > 2: # ver 'explicacao marota'
			subconjunto_especial = [subconjuntos_unitarios[k]]

		for j in xrange(i, (t_max + 1)):
			subconjunto += [conjunto[j]]
			elem = tuple(subconjunto)
			subconjuntos.append(elem)

			if len(subconjuntos_unitarios) > 2: # ver 'explicacao marota'
				subconjunto_especial += [conjunto[j]]
				elem = tuple(subconjunto_especial)
				subconjuntos.append(elem)

				print "especial:", subconjunto_especial

			print subconjunto

		if len(subconjuntos_unitarios) > 2: # ver 'explicacao marota'
			k += 1

	print subconjuntos

	return subconjuntos

# main
print 'gera_subconjuntos(10, 3, 7):'
gera_subconjuntos(10, 3, 7)