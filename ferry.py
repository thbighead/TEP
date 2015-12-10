from random import randint


memo = set()
better_sequence = []

def backtrack(state, vehicles, L, n_boarded_vehicles, max_boarded_vehicles, sequence):
    global better_sequence

    if state[0] > L:
        return sequence  # invalid state

    if tuple(state) in memo:
        return sequence  # already visited

    print sequence
    print state

    if n_boarded_vehicles > max_boarded_vehicles[0]:
        max_boarded_vehicles[0] = n_boarded_vehicles

    length_next_vehicle = vehicles[n_boarded_vehicles]

    new_state = [state[0] + length_next_vehicle, state[1]]
    sequence += ["L"]
    sequence = backtrack(new_state, vehicles, L, n_boarded_vehicles + 1, max_boarded_vehicles, sequence)
    sequence.pop()

    new_state = [state[0], state[1] + length_next_vehicle]
    sequence += ["R"]
    new_state.sort(reverse=True)  # [more_loaded, less_loaded] by convention
    sequence = backtrack(new_state, vehicles, L, n_boarded_vehicles + 1, max_boarded_vehicles, sequence)
    sequence.pop()

    memo.add(tuple(state))
    if len(better_sequence) < len(sequence):
        better_sequence = list(sequence)

    return sequence


def ferry(vehicles, L):
    max_boarded_vehicles = [0]
    state = [0,0]
    sequence = backtrack(state, vehicles, L, 0, max_boarded_vehicles, [])

    print("We can board up to %d vehicles" % max_boarded_vehicles[0])
    print "A possible boarding sequence is: " + str(better_sequence)
    memo = set()



queue = []
for i in xrange(10):
	queue += [randint(100, 200)] # random cars sizes

print queue

ferry(queue, 300)