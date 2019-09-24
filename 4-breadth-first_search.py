graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['peggy', 'anuj']
graph['claire'] = ['thom', 'jonny']
graph['peggy'] = []
graph['anuj'] = []
graph['thom'] = []
graph['jonny'] = []


from collections import deque

def person_is_seller(name):
	return name[-1] == 'm'

def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		print(person)
		if not person in searched:
			if person_is_seller(person):
				print(person + ' is a mango seller!')
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

print(search('you'))