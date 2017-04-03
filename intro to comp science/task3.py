"""
@author Gabriela Melo
@since 21/05/2015
"""

from minHeap import *
from task2 import *
import random

def create_status_events(priority_queue):
	'''
	adds 10 status events to the queue, their keys are 60, 120, 180...600
	param priority_queue: an instance of minHeap
	complexity: best = O(1)
	'''
	for x in range(10):
		priority_queue.append([(x+1)*60,'status'])

def arrive_and_wait(priority_queue, service_queue, event):
	'''
	starts serving a customer that has arrived, serving time will be random integer between 0 and 5, 
	if another customer is being served, they get put in queue to wait
	param priority_queue: minHeap
	param service_queue: minHeap
	param event: array, event[0] is integer (key), event[1] is string
	complexity: best = O(1), worst = O(log N), where N = depth of heap
	'''
	time = convert_time(event[0])
	print('A customer arrived at ' + time)

	# if service queue is empty, customer starts being served at this time
	if (service_queue.is_empty()):
		arrive(priority_queue, event)
	# either way, they will stay in service queue until they get served
	service_queue.append(event)

def new_serve(priority_queue, service_queue, event):
	'''
	serves customer, time that customer will spend in the shop will be random integer between 0 and 30
	if another customer was waiting on queue, this customer starts being served
	param priority_queue: minHeap
	param service_queue: minHeap
	param event: array, event[0] is integer (key), event[1] is string
	complexity: best = O(1), worst = O(log N), where N = depth of heap
	'''
	# serves customer when his coffee is ready
	serve(priority_queue, event)
	# customers get out of queue
	service_queue.serve()

	# if there's people waiting on queue, we can now star serving them
	if not service_queue.is_empty():
		# change his time to be arrival time + time waited to start getting served
		serve_event = service_queue.serve()
		serve_event[0] = event[0]
		# starts serving
		arrive(priority_queue, serve_event)
		# customer remais in queue until serving they get their coffee
		service_queue.append(serve_event)

def new_serve_customers(priority_queue, service_queue):
	'''
	serves all customers in priority_queue
	param priority_queue: minHeap instance
	param service_queue: minHeap instance
	complexity: best = O(N), worst = O(N logN)
	'''
	people_served = 0
	customers_in_store = 0
	max_customers = 0
	random.seed(2)

	while not priority_queue.is_empty():
		event = priority_queue.serve()

		if event[1] == 'arrival':
			arrive_and_wait(priority_queue, service_queue, event)

			customers_in_store += 1
			max_customers = max(customers_in_store, max_customers)

		elif event[1] == 'served':
			new_serve(priority_queue, service_queue, event)
			people_served += 1

		elif event[1] == 'leaving':
			leave(event)
			customers_in_store -= 1
			
		elif event[1] == 'status':
			print('It is ' + convert_time(event[0]))
			print('In the last hour ' + str(people_served) + ' people were served.')
			people_served = 0
			print('The maximum number of customers in the shop in the last hour was ' + str(max_customers))
			max_customers = 0
		else:
			print('Unrecognized event')


def main():
	priority_queue = MinHeap()
	service_queue = MinHeap()
	create_status_events(priority_queue)
	create_arrival_events(priority_queue, 200)
	new_serve_customers(priority_queue, service_queue)

if __name__ == '__main__':
	main()