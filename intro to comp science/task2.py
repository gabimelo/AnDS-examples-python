"""
@author Gabriela Melo
@since 21/05/2015
"""

from minHeap import *
import random

def create_arrival_events(priority_queue, num):
	'''
	adds arrival events to the queue, their keys are a random integer between 0 and 600
	param priority_queue: an instance of minHeap
	param num: integer, amount of events to be created and added
	complexity: best = O(N), worst = O(N*logN)
	'''
	random.seed(1)
	for _ in range(num+1):
		time = random.randint(0,600)
		priority_queue.append([int(time),'arrival'])

def convert_time(n):
	'''
	converts minutes to string representing the time, by adding the minutes to 8am
	param n: integer, minutes passed since 8am
	return: string
	complexity: O(1)
	'''
	hours = 8 + n//60
	minutes = n % 60
	if minutes < 10:
		time = str(hours)+ '.0' + str(minutes)
	else:
		time = str(hours)+ '.' + str(minutes)
	return(time)

def arrive(priority_queue, event):
	'''
	starts serving a customer that has arrived, serving time will be random integer between 0 and 5
	param priority_queue: minHeap
	param event: array, event[0] is integer (key), event[1] is string
	complexity: best = O(1), worst = O(log N), where N = depth of heap
	'''
	serve_time = random.randint(0,5)
	time = event[0] + serve_time
	priority_queue.append([time,'served'])

def serve(priority_queue, event):
	'''
	serves customer, time that customer will spend in the shop will be random integer between 0 and 30
	param priority_queue: minHeap
	param event: array, event[0] is integer (key), event[1] is string
	complexity: best = O(1), worst = O(log N), where N = depth of heap
	'''
	time = convert_time(event[0])
	print('A customer has been served at ' + time)
	spent_time = random.randint(0,30)
	time = event[0] + spent_time
	priority_queue.append([time,'leaving'])

def leave(event):
	'''
	prints time when a customer is leaving
	param event: event[0] is integer, represents time
	complexity: O(1)
	'''
	time = convert_time(event[0])
	print('A customer is leaving at ' + time)

def serve_customers(priority_queue):
	'''
	serves all customers in priority_queue
	param priority_queue: minHeap instance
	complexity: best = O(N), worst = O(N logN)
	'''
	random.seed(2)
	while not priority_queue.is_empty():
		event = priority_queue.serve()
		if event[1] == 'arrival':
			time = convert_time(event[0])
			print('A customer arrived at ' + time)
			arrive(priority_queue, event)
		elif event[1] == 'served':
			serve(priority_queue, event)
		elif event[1] == 'leaving':
			leave(event)
		else:
			print('Unrecognized event')


def main():
	priority_queue = MinHeap()
	create_arrival_events(priority_queue, 200)
	serve_customers(priority_queue)

if __name__ == '__main__':
	main()