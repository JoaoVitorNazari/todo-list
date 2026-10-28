import json
import os

# ============================================================
# FUNÇÕES DE ARQUIVO
# ============================================================

def salvar_tarefas(tarefas, caminho_arquivo):
    """Salva a lista de tarefas no arquivo JSON."""
    try:
        diretorio = os.path.dirname(caminho_arquivo)

        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio)

        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(
                tarefas,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

    except PermissionError:
        print(f'Sem permissão para escrever em {caminho_arquivo}.')

    except Exception as erro:
        print(f'Erro ao salvar tarefas: {erro}')


def carregar_tarefas(caminho_arquivo):
    """Carrega as tarefas do arquivo JSON."""

    if not os.path.exists(caminho_arquivo):
        return []

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)

    except PermissionError:
        print(f'Sem permissão para ler {caminho_arquivo}.')
        return []

    except json.JSONDecodeError:
        print('Erro: o arquivo JSON está corrompido.')
        return []

    except Exception as erro:
        print(f'Erro ao carregar tarefas: {erro}')
        return []

##
## CODIGO ADICIONAL PARA REMOVER TODAS AS TAREFAS DE TESTES DO ARQUIVO JSON 
def popall(caminho_arquivo):
    """Remove todas as tarefas do arquivo JSON."""
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump([], arquivo, ensure_ascii=False, indent=4)
    except PermissionError:
        print(f'Sem permissão para escrever em {caminho_arquivo}.')
        return []
    except Exception as erro:
        print(f'Erro ao limpar tarefas: {erro}')
        return []