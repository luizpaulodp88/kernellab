import copy

class CPUScheduler:
    @staticmethod
    def fcfs(processes_data):
        procs = sorted(copy.deepcopy(processes_data), key=lambda x: x['arrival'])
        current_time = 0
        gantt = []
        context_switches = 0
        
        for p in procs:
            if current_time < p['arrival']:
                current_time = p['arrival']
            
            p['response_time'] = current_time - p['arrival']
            start_time = current_time
            current_time += p['burst']
            p['completion_time'] = current_time
            
            gantt.append((p['id'], start_time, current_time))
            context_switches += 1
            
        return procs, gantt, max(0, context_switches - 1)

    @staticmethod
    def sjf(processes_data):
        procs = copy.deepcopy(processes_data)
        current_time = 0
        completed = 0
        n = len(procs)
        gantt = []
        context_switches = 0
        executed = set()

        while completed < n:
            available = [p for p in procs if p['arrival'] <= current_time and p['id'] not in executed]
            if not available:
                current_time = min(p['arrival'] for p in procs if p['id'] not in executed)
                continue
            
            p = min(available, key=lambda x: (x['burst'], x['arrival']))
            
            p['response_time'] = current_time - p['arrival']
            start_time = current_time
            current_time += p['burst']
            p['completion_time'] = current_time
            
            gantt.append((p['id'], start_time, current_time))
            executed.add(p['id'])
            completed += 1
            context_switches += 1
            
        return procs, gantt, max(0, context_switches - 1)

    @staticmethod
    def round_robin(processes_data, quantum=3):
        procs = copy.deepcopy(processes_data)
        for p in procs:
            p['remaining_burst'] = p['burst']
            p['response_time'] = -1

        current_time = 0
        queue = []
        gantt = []
        context_switches = 0
        completed = 0
        n = len(procs)
        
        procs_sorted_arrival = sorted(procs, key=lambda x: x['arrival'])
        arrived_idx = 0

        while completed < n:
            while arrived_idx < n and procs_sorted_arrival[arrived_idx]['arrival'] <= current_time:
                queue.append(procs_sorted_arrival[arrived_idx])
                arrived_idx += 1

            if not queue:
                current_time = procs_sorted_arrival[arrived_idx]['arrival']
                continue

            p = queue.pop(0)

            if p['response_time'] == -1:
                p['response_time'] = current_time - p['arrival']

            exec_time = min(quantum, p['remaining_burst'])
            start_time = current_time
            current_time += exec_time
            p['remaining_burst'] -= exec_time
            
            gantt.append((p['id'], start_time, current_time))
            context_switches += 1

            while arrived_idx < n and procs_sorted_arrival[arrived_idx]['arrival'] <= current_time:
                queue.append(procs_sorted_arrival[arrived_idx])
                arrived_idx += 1

            if p['remaining_burst'] > 0:
                queue.append(p)
            else:
                p['completion_time'] = current_time
                completed += 1

        return procs, gantt, max(0, context_switches - 1)

    @staticmethod
    def priority_scheduling(processes_data):
        procs = copy.deepcopy(processes_data)
        current_time = 0
        completed = 0
        n = len(procs)
        gantt = []
        context_switches = 0
        executed = set()

        while completed < n:
            available = [p for p in procs if p['arrival'] <= current_time and p['id'] not in executed]
            if not available:
                current_time = min(p['arrival'] for p in procs if p['id'] not in executed)
                continue
            
            p = min(available, key=lambda x: (x['priority'], x['arrival']))
            
            p['response_time'] = current_time - p['arrival']
            start_time = current_time
            current_time += p['burst']
            p['completion_time'] = current_time
            
            gantt.append((p['id'], start_time, current_time))
            executed.add(p['id'])
            completed += 1
            context_switches += 1
            
        return procs, gantt, max(0, context_switches - 1)
