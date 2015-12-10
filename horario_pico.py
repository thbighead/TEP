def histogram(playerListOfStartEndPlayin, globalStart, globalEnd, colSize):
	returnStatement = []
	i = globalStart
	while i < globalEnd:
		contribution = 0
		for player in playerListOfStartEndPlayin:
			if i >= player[0] and i <= player[1]:
				contribution += 1
		returnStatement.append((i, contribution))
		i += colSize

	return returnStatement