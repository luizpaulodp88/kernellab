import json
import os
import threading
from schedulers import CPUScheduler
from memory import MemorySimulator
from metrics import MetricsCalculator
from devices import DeviceManager

def load_processes():
    path = os.path.join(os.path.dirname(__file__), '../data/processes.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def run_simulation():
    processes = load_processes()
    print("=" * 60)
    print("      KERNELLAB - SIMULADOR DE SISTEMAS OPERACIONAIS")
    print("      Plataforma MedControl Systems")
    print("=" * 60)

    # Etapa 1 & 2: Escalonamento
    schedulers = {
        "FCFS": CPUScheduler.fcfs,
        "SJF": CPUScheduler.sjf,
        "Round Robin (q=3)": lambda p: CPUScheduler.round_robin(p, quantum=3),
        "Prioridade": CPUScheduler.priority_scheduling
    }

    print("\n[ETAPA 1 & 2] ESCALONAMENTO DE CPU E MÉTRICAS:")
    for name, func in schedulers.items():
        procs, gantt, ctx_switches = func(processes)
        metrics, summary = MetricsCalculator.calculate(procs)
        print(f"\nAlgoritmo: {name}")
        print(f"  Gantt: {gantt}")
        print(f"  Trocas de Contexto: {ctx_switches}")
        print(f"  Espera Média: {summary['avg_waiting']:.2f} | Retorno Médio: {summary['avg_turnaround']:.2f} | Resposta Média: {summary['avg_response']:.2f}")

    # Etapa 3: Memória
    ref_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5, 2, 1, 5, 3, 2]
    frames_count = 4
    print(f"\n[ETAPA 3] GERENCIAMENTO DE MEMÓRIA (Frames = {frames_count}):")
    mem_algos = {
        "FIFO": MemorySimulator.fifo,
        "LRU": MemorySimulator.lru,
        "Optimal": MemorySimulator.optimal
    }
    for name, func in mem_algos.items():
        history, hits, faults = func(ref_string, frames_count)
        rate = (faults / len(ref_string)) * 100
        print(f"  {name:8s} -> Hits: {hits:2d} | Faults: {faults:2d} | Taxa de Faltas: {rate:.2f}%")

    # Etapa 4: Dispositivos
    print("\n[ETAPA 4] CONTROLE DE DISPOSITIVOS E MUTEX/CONCORRÊNCIA:")
    dev_mgr = DeviceManager()
    p4_audio = dev_mgr.check_permission("P4", "Áudio", "utilizar")
    print(f"  Permissão do Alarme Crítico (P4) no dispositivo 'Áudio': {p4_audio}")
    
    t1 = threading.Thread(target=dev_mgr.access_device_concurrently, args=("P3", "Disco"))
    t2 = threading.Thread(target=dev_mgr.access_device_concurrently, args=("P5", "Disco"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("\nSimulação concluída com sucesso! Verifique os relatórios e documentações.")

if __name__ == "__main__":
    run_simulation()
