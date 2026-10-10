# KernelLab - Simulador de Gerenciamento de Recursos (SO)

Simulador desenvolvido para a plataforma **MedControl Systems**, permitindo avaliar políticas de escalonamento de CPU, algoritmos de substituição de páginas em memória virtual e controle de acesso concorrente a dispositivos.

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

## Como Executar
Certifique-se de ter o Python 3.8+ instalado. No terminal, navegue até a raiz do projeto e execute:
```bash
python src/main.py
```
