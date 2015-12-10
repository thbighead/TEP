from random import randint # from module import function
from time import time
from math import ceil

# global variables to use as inputs
global_start = 0
global_end = 24 * 3600 # seconds
min_duration = 60
max_duration = 5 * 3600

def generate_tuples(n):
	tuples = []
	for i in range(n):
		duration = randint(min_duration, max_duration)
		start = randint(global_start - duration, global_end)
		end = start + duration
	tuples += [(start, end)] # equivalent to tuples.append((start, end))
	return tuples

def compute_histogram_naive(player_times, columns):
	players_online = 0
	step = (global_end - global_start) // columns # integer division (ignores rest)
	histogram = []
	moment = global_start
	while moment <= global_end:
		for times_tuple in player_times:
			if times_tuple[0] <= moment and times_tuple[1] >= moment:
				players_online += 1
		histogram += [(moment, players_online)]
		moment += step
	return histogram

def compute_histogram_linear_naive(player_times, columns):
	step = (global_end - global_start) // columns
	histogram = []

	players_by_start_time = {}
	players_by_end_time = {}

	for times_tuple in player_times:
		start = times_tuple[0]
		end = times_tuple[1]
		if end < global_start:
			continue
		start = max(start, global_start)

		adjusted_start = global_start + step * ceil((start - global_start) / step)
		adjusted_end = global_start + step * ceil((end - global_start) / step)

		players_by_start_time[adjusted_start] = players_by_start_time.get(adjusted_start, 0) + 1
		players_by_end_time[adjusted_end] = players_by_start_time.get(adjusted_end, 0) + 1

	moment = global_start
	players_online = 0
	while moment <= global_end:
		players_online += players_by_start_time.get(moment, 0)
		players_online -= players_by_end_time.get(moment, 0)
		histogram += [(moment, players_online)]
		moment += step

	return histogram

def print_histogram(histogram):
	times = sorted(histogram.keys())
	for time in times:
		print("time = %d, players = %d" % (time, histogram[time]))

# def main():
player_times = generate_tuples(40000)
elapsed_time_naive = time()
histogram = compute_histogram_naive(player_times, 2400)
elapsed_time_naive = time() - elapsed_time_naive

# print_histogram(histogram)
print("elapsed time (naive) = %.6f" % elapsed_time_naive)

elapsed_time_naive = time()
histogram = compute_histogram_linear_naive(player_times, 2400)
elapsed_time_naive = time() - elapsed_time_naive

# print_histogram(histogram)
print("elapsed time (naive) = %.6f" % elapsed_time_naive)