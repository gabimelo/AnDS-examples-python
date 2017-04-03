"""
@author Gabriela Melo
@since 21/05/2015
"""

from minHeap import *
from task2 import *
from task3 import *

def test_append():
	correct = True
	heap = MinHeap()
	heap.append([3])
	heap.append([5])
	heap.append([6])
	heap.append([2])
	heap.append([4])
	heap.append([1])
	if str(heap) != '[1][3][2][5][4][6]':
		correct = False
	try:
		heap.append(2)
		correct = False
	except:
		pass
	return correct

def test_serve():
	correct = True
	heap = MinHeap()
	heap.append([3])
	heap.append([5])
	heap.append([6])
	heap.append([2])
	heap.append([4])
	heap.append([1])
	served = str(heap.serve())
	if served != '[1]':
		correct = False
	served = str(heap.serve())
	if served != '[2]':
		correct = False
	served = str(heap.serve())
	if served != '[3]':
		correct = False
	served = str(heap.serve())
	if served != '[4]':
		correct = False
	served = str(heap.serve())
	if served != '[5]':
		correct = False
	served = str(heap.serve())
	if served != '[6]':
		correct = False
	try:
		heap.serve()
		correct = False
	except:
		pass
	return correct

def test_create_arrival_events():
	correct = True
	heap = MinHeap()
	create_arrival_events(heap, 4)
	for _ in range(4):
		event = heap.serve()
		if event[0] < 0 or event[0] > 600:
			correct = False
		if event[1] != 'arrival':
			correct = False
	return correct

def test_convert_time():
	correct = True
	if convert_time(30) != '8.30':
		correct = False
	if convert_time(61) != '9.01':
		correct = False
	return correct

def test_arrive():
	correct = True
	heap = MinHeap()
	arrive(heap, [1,'arrival'])
	event = heap.serve()
	if event[0] < 0 or event[0] > 605:
		correct = False
	if event[1] != 'served':
		correct = False
	return correct

def test_serve_cust():
	correct = True
	heap = MinHeap()
	serve(heap, [1,'served'])
	event = heap.serve()
	if event[0] < 0 or event[0] > 635:
		correct = False
	if event[1] != 'leaving':
		correct = False
	return correct

def test_create_status_events():
	correct = True
	heap = MinHeap()
	create_status_events(heap)
	if heap.serve() != [60, 'status']:
		correct = False
	if heap.serve() != [120, 'status']:
		correct = False
	if heap.serve() != [180, 'status']:
		correct = False
	if heap.serve() != [240, 'status']:
		correct = False
	if heap.serve() != [300, 'status']:
		correct = False
	if heap.serve() != [360, 'status']:
		correct = False
	if heap.serve() != [420, 'status']:
		correct = False
	if heap.serve() != [480, 'status']:
		correct = False
	if heap.serve() != [540, 'status']:
		correct = False
	if heap.serve() != [600, 'status']:
		correct = False
	try:
		heap.serve()
		correct = False
	except:
		pass
	return correct

def test_arrive_and_wait(): 
	correct = True
	priority_queue = MinHeap()
	service_queue = MinHeap()
	arrive_and_wait(priority_queue, service_queue, [0,'arrival'])
	arrive_and_wait(priority_queue, service_queue, [1,'arrival'])
	arrive_and_wait(priority_queue, service_queue, [2,'arrival'])
	arrive_and_wait(priority_queue, service_queue, [3,'arrival'])
	if str(service_queue) != "[0, 'arrival'][1, 'arrival'][2, 'arrival'][3, 'arrival']":
		print(str(service_queue))
		correct = False
	test = priority_queue.serve()
	if test[0] < 0 or test[0] > 5:
		correct = False
	if test[1] != 'served':
		correct = False
	return correct

def test_new_serve():
	correct = True
	priority_queue = MinHeap()
	service_queue = MinHeap()
	arrive_and_wait(priority_queue, service_queue, [0,'arrival'])
	arrive_and_wait(priority_queue, service_queue, [1,'arrival'])
	
	test = priority_queue.serve() 
	new_serve(priority_queue, service_queue, test)
	test = priority_queue.serve() 
	test1 = priority_queue.serve() 
	
	if test[1] == 'leaving':
		if test1[1] != 'served':
			correct = False
	elif test[1] == 'served': 
		if test1[1] != 'leaving':
			correct = False

	test = service_queue.serve()
	if test[1] != 'arrival':
		correct = False
	try:
		test = priority_queue.serve()
		correct = False
	except:
		pass
	try:
		test = service_queue.serve()
		correct = False
	except:
		pass
	return correct

if not test_append():
	print('append not working properly')
elif not test_serve():
	print('serve not working properly')
elif not test_create_arrival_events():
	print('create_arrival_events not working properly')
elif not test_convert_time():
	print('convert_time not working properly')
elif not test_arrive():
	print('arrive not working properly')
elif not test_serve_cust():
	print('serve not working properly')
elif not test_create_status_events():
	print('create_status_events not working properly')
elif not test_arrive_and_wait():
	print('arrive_and_wait not working properly')
elif not test_new_serve():
	print('new_serve not working properly')
else:
	print('All functions are working properly!')