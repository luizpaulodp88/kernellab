import threading
import time

class DeviceManager:
    def __init__(self):
        # Matriz de Controle de Accesso: [Leitura, Gravação, Execução, Utilizar, Exclusivo]
        self.access_matrix = {
            "P1": {"Disco": [True, True, False, True, False], "Rede": [True, True, True, True, False], "Áudio": [False, False, False, False, False], "Log": [True, True, False, True, False]},
            "P2": {"Disco": [True, False, False, True, False], "Rede": [True, True, True, True, False], "Áudio": [False, False, False, False, False], "Log": [True, True, False, True, False]},
            "P3": {"Disco": [True, True, True, True, True], "Rede": [False, False, False, False, False], "Áudio": [False, False, False, False, False], "Log": [True, True, False, True, True]},
            "P4": {"Disco": [False, False, False, False, False], "Rede": [True, True, True, True, False], "Áudio": [True, True, True, True, True], "Log": [True, True, False, True, False]},
            "P5": {"Disco": [True, True, True, True, True], "Rede": [False, False, False, False, False], "Áudio": [False, False, False, False, False], "Log": [True, True, False, True, True]},
            "P6": {"Disco": [True, True, True, True, False], "Rede": [True, True, True, True, False], "Áudio": [False, False, False, False, False], "Log": [True, True, False, True, False]}
        }
        self.device_mutexes = {
            "Disco": threading.Lock(),
            "Rede": threading.Lock(),
            "Áudio": threading.Lock(),
            "Log": threading.Lock()
        }

    def check_permission(self, process_id, device, permission_type):
        perms = {"ler": 0, "gravar": 1, "executar": 2, "utilizar": 3, "exclusivo": 4}
        idx = perms.get(permission_type, 0)
        return self.access_matrix.get(process_id, {}).get(device, [False]*5)[idx]

    def access_device_concurrently(self, process_id, device_name):
        print(f"[{process_id}] Solicitando acesso ao dispositivo: {device_name}")
        mutex = self.device_mutexes.get(device_name, threading.Lock())
        with mutex:
            print(f"--> [{process_id}] ADQUIRIU o lock/mutex do dispositivo {device_name}. Executando E/S...")
            time.sleep(0.3)
            print(f"<-- [{process_id}] LIBEROU o dispositivo {device_name}.")
