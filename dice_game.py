from __future__ import division
from random import uniform

def dice_game_tester(times_to_roll, faces_probability):
	score = {"three_dices_in_a_row": 0, "two_pairs_of_dices_in_a_row": 0}
	for x in xrange(0, times_to_roll):
		if two_pairs_of_dices_in_a_row(faces_probability):
			score["two_pairs_of_dices_in_a_row"] += 1
		if three_dices_in_a_row(faces_probability):
			score["three_dices_in_a_row"] += 1
	print "The score rolling", times_to_roll, "dices for each win case, ended like this:", score
	print "The probabilities of winning of each of them are:"
	print "three_dices_in_a_row =", (score["three_dices_in_a_row"] * 100)/times_to_roll, "%"
	print "two_pairs_of_dices_in_a_row =", (score["two_pairs_of_dices_in_a_row"] * 100)/times_to_roll, "%"

def three_dices_in_a_row(faces_probability):
	first_result = dice_roll(faces_probability)
	if first_result == dice_roll(faces_probability):
		if first_result == dice_roll(faces_probability):
			return True
	return False

def two_pairs_of_dices_in_a_row(faces_probability):
	result = dice_roll(faces_probability)
	if result == dice_roll(faces_probability):
		result = dice_roll(faces_probability)
		if result == dice_roll(faces_probability):
			return True
	return False

def they_see_me_rollin_they_hatin(times_to_roll, faces_probability):
	number_of_faces = len(faces_probability)
	results = {}
	for i in xrange(1, number_of_faces + 1):
		results[i] = 0
	for x in xrange(0, times_to_roll):
		results[dice_roll(faces_probability)] += 1
	return results

def dice_roll(faces_probability):
	faces_probability_sum = sum(faces_probability)
	# print "faces_probability: ", faces_probability
	# print "faces_probability_sum: ", faces_probability_sum
	if faces_probability_sum >= 1:
		faces_probability = map(lambda x: x / faces_probability_sum, faces_probability)
	# print "faces_probability: ", faces_probability

	roll = uniform(0, 1)
	# print "roll: ", roll
	i = 1
	result = 1
	faces_probability_sum = faces_probability[0]
	while roll > faces_probability_sum:
		# print "faces_probability_sum: ", faces_probability_sum
		faces_probability_sum += faces_probability[i]
		# print "faces_probability[i]: ", faces_probability[i]
		result = i + 1  # there's no 0 face on my dice
		# print "i: ", i
		i += 1

	# print result
	return result

# print "escreva a lista de probabilidades das faces do seu dado numa lista em ordem (entre com [] para finalizar):"
# faces_probability_input = input("--> ")
# while not faces_probability_input == []:
# 	print dice_roll(faces_probability_input)
# 	faces_probability_input = input("--> ")

# faces_probability_input = input("escreva a lista de probabilidades das faces do seu dado numa lista em ordem ([] naum eh valido):")
# times_to_roll = input("quantas vezes rodar:")
# print they_see_me_rollin_they_hatin(times_to_roll, faces_probability_input)

dice_game_tester(100000, [1, 1, 1, 1, 1, 1])