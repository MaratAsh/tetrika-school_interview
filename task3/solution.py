import heapq

class IntervalPresenceObject:
	entry_time: int
	def __init__(self, entry_time=None, name=None):
		self.entry_time = entry_time
		self.name = name
	@property
	def is_online(self) -> bool:
		return False if self.entry_time is None else True
	
	@is_online.setter
	def is_online(self, status: bool):
		if type(status) != bool:
			raise TypeError
		if status != False:
			raise ValueError
		self.entry_time = None
	
	def __repr__(self):
		return 'IntervalPresenceObject(name=\'{name}\', entry_time={time})'.format(
			name=self.name,
			time=self.entry_time)

def appearance(intervals: dict[str, list[int]]) -> int:
	objs = []
	time_mapping = {}
	heap = list(heapq.merge(*intervals.values()))
	heapq.heapify(heap)
	for i, name in enumerate(intervals.keys()):
		ipobj = IntervalPresenceObject(name=name)
		objs.append(ipobj)
		for ts_i, ts in enumerate(intervals[name]):
			if ts not in time_mapping:
				time_mapping[ts] = []
			time_mapping[ts].append({
				'object': ipobj,
				'status': 'entry' if ts_i % 2 == 0 else 'exit'
			})
	_time = heapq.heappop(heap)
	last_entry = None
	_res = 0
	while (_time):
		ipo = time_mapping[_time].pop()
		if len(time_mapping[_time]) == 0:
			del time_mapping[_time]
		if ipo['status'] == 'exit':
			if all(o.is_online for o in objs):
				full_appearence_time = _time - last_entry
				_res += full_appearence_time
			ipo['object'].is_online = False
		if ipo['status'] == 'entry' and not ipo['object'].is_online:
			ipo['object'].entry_time = _time
			if all(True if o == ipo['object'] else o.is_online for o in objs):
				last_entry = _time
		try:
			_time = heapq.heappop(heap)
		except IndexError:
			_time = None
	return _res

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

