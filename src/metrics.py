class MetricsCalculator:
    @staticmethod
    def calculate(processes):
        """
        Calcula tempo de espera, retorno e resposta para cada processo.
        Espera (Waiting) = Retorno - Burst - Chegada (ou tempo acumulado)
        Retorno (Turnaround) = Término - Chegada
        """
        results = []
        total_waiting = 0
        total_turnaround = 0
        total_response = 0
        n = len(processes)

        for p in processes:
            turnaround = p['completion_time'] - p['arrival']
            waiting = turnaround - p['burst']
            if waiting < 0: 
                waiting = 0
            
            total_waiting += waiting
            total_turnaround += turnaround
            total_response += p['response_time']

            results.append({
                "id": p['id'],
                "waiting_time": waiting,
                "turnaround_time": turnaround,
                "response_time": p['response_time']
            })

        summary = {
            "avg_waiting": total_waiting / n,
            "avg_turnaround": total_turnaround / n,
            "avg_response": total_response / n
        }
        return results, summary
