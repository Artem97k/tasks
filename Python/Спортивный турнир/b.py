def b(k, *args):
	largs = []
	str = ''
	for a in args:
		str += a + ' ' #merge all args into one string, слить аргументы в одну строку

	str = str.split(' ') #create list of players names, создать список имен игроков
	str.remove('') #remove space element at the end, убрать лишний пробел
	names = set()
	for s in str:
			names.add(s) #create set of players (no duplicates)
						#создать множество имен игроков без повторений
	li = []
	for n in names:
		j = 0
		for s in str:
			if n in s:
				j += 1

		li.append((n, j)) #number of times each name appears in args
							#посчитать сколько раз встречалось имя игрока в списке аргументов
	li.sort(key = lambda x: x[1]) #sort by tournment stage(1 - lost in 1st game, k - finalist)
	ki = 1							#сортировка по участию в этапах турнира (1 - вылет в первой же игре, k - финалист)
	mas = []
	while ki <= k:
		j = 0
		for l in li:
			if l[1] == ki:
				j += 1

		mas.append((ki, j)) #count amount of players on each stage of tournament
		ki += 1				#посчитать количество участников на каждом этапе турнира

	if len(mas) == k: #measured amount of stages should match input
		pass			#посчитанное кол-во этапов должно равняться введенному
	else:
		return 'NO SOLUTION'

	if mas[-1][0] == k: #remove finalists
		mas.pop()		#убираем финалистов
	else:
		return 'NO SOLUTION'

	i = 1
	j = len(mas)
	while i <= len(mas):
		if ( mas[i-1][0] == i ) and ( mas[i-1][1] == (2**j) ):
			i += 1
			j -= 1
		else:						#each stage of tournament should have twice as little players
			return 'NO SOLUTION'	#на каждом этапе турнира количество участников должно уменьшаться в два раза

	return li[-3][0] + ' ' + li[-4][0]
