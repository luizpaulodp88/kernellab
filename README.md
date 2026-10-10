
💻 KernelLab — Simulador de Gerenciamento de CPU, Memória e Dispositivos 🚀🏥 Caso Prático — MedControl Systems: Uma plataforma de simulação de Sistemas Operacionais projetada para diagnosticar e otimizar o processamento de tarefas críticas em servidores de monitoramento hospitalar.📋 Sumário🚨 O Desafio✨ Funcionalidades⚙️ Algoritmos Implementados📁 Estrutura do Projeto🛠️ Como Executar📊 Resultados & Métricas🤝 Contribuição🚨 O DesafioA MedControl Systems desenvolve softwares para equipamentos médicos conectados. Em cenários de alta carga, o servidor apresentou:⏱️ Atrasos críticos no disparo de alarmes médicos.📉 Ineficiência da CPU devido a alto tempo de espera.💾 Thrashing na memória por alto número de faltas de página (page faults).🔒 Risco de acessos simultâneos não autorizados aos periféricos de hardware.O KernelLab foi criado em Python para simular e avaliar o impacto de diferentes políticas de escalonamento, paginação e concorrência.✨ Funcionalidades⚡ Simulador de CPU: Avalia 4 algoritmos de escalonamento com geração de Diagrama de Gantt e métricas completas (tempo de espera, retorno, resposta e trocas de contexto).🧠 Gerenciador de Memória: Simula a substituição de páginas com memória física configurável (frames).🔒 Controle de Dispositivos: Matriz de acesso e mecanismo de sincronização via Mutex/Semáforos para acesso seguro a Disco, Rede e Áudio.⚙️ Configuração Dinâmica: Suporte a carregamento de processos e sequências de memória via arquivo processes.json.⚙️ Algoritmos Implementados🖥️ Escalonamento de CPU (src/schedulers.py)🟢 FCFS (First-Come, First-Served)⚡ SJF (Shortest Job First) — Não-preemptivo🔄 Round Robin (Quantum $Q = 3$)🎯 Escalonamento por Prioridade Preemptiva (Menor número = maior prioridade)🧠 Substituição de Páginas (src/memory.py)📦 FIFO (First-In, First-Out)🕒 LRU (Least Recently Used)🎯 Optimal (Algoritmo Ótimo - Referência Teórica)📁 Estrutura do Projetokernellab/

## Estrutura do Repositório
```text
kernellab/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── schedulers.py
│   ├── memory.py
│   ├── devices.py
│   └── metrics.py
├── data/
│   └── processes.json
├── tests/
│   └── __init__.py
├── requirements.txt
└── README.md
```
# KernelLab - Simulador de Gerenciamento de Recursos (SO)

Simulador desenvolvido para a plataforma **MedControl Systems**, permitindo avaliar políticas de escalonamento de CPU, algoritmos de substituição de páginas em memória virtual e controle de acesso concorrente a dispositivos.



## Como Executar
Certifique-se de ter o Python 3.8+ instalado. No terminal, navegue até a raiz do projeto e execute:
```bash
python src/main.py
```
