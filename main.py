import os

from arquivo import (salvar_tarefas, carregar_tarefas, popall)

from tarefa import (adicionar_tarefa,lista_tarefas,excluir_tarefa,concluir_tarefa,
pesquisa_tarefa,editar_tarefa)

def main():
    caminho_arquivo = os.path.join("Projetos_e_Portfolio","todo-list","tarefas.json")

    tarefas = carregar_tarefas(caminho_arquivo)

    if tarefas:
        proximo_id = max(tarefa['ID']for tarefa in tarefas) + 1
    else:
        proximo_id = 1

    while True:

        print('\n=== Menu ===')
        print('1. Adicionar tarefa')
        print('2. Pesquisar tarefa')
        print('3. Listar tarefas')
        print('4. Concluir tarefa')
        print('5. Excluir tarefa')
        print('6. Teste editar tarefa')
        print('7. Sair')

        opcao = input('Escolha uma opção: ').strip().lower()

        if opcao == '1':
            proximo_id = adicionar_tarefa(tarefas,proximo_id)
            salvar_tarefas(tarefas, caminho_arquivo)

        elif opcao == '2':
            pesquisa_tarefa(tarefas)

        elif opcao == '3':
            while True:
                if not tarefas:
                    print('Nenhuma tarefa cadastrada!')
                    break
                else:
                    lista_tarefas(tarefas)
                    salvar_tarefas(tarefas, caminho_arquivo)

        elif opcao == '4':
            concluir_tarefa(tarefas)
            salvar_tarefas(tarefas, caminho_arquivo)

        elif opcao == '5':
            excluir_tarefa(tarefas)
            salvar_tarefas(tarefas, caminho_arquivo)

        elif opcao == '6':
            editar_tarefa(tarefas)
            salvar_tarefas(tarefas, caminho_arquivo)
            
        elif opcao == '7':
            print('Programa encerrado.')
            break

        # COMANDO DE DESENVOLVIMENTO
        ## linha adicionada para limpar todas as tarefas de testes
        elif opcao == 'dev':

            popall(caminho_arquivo)

            tarefas.clear()

            print('Todas as tarefas foram removidas.')
            break
        else:
            print('Opção inválida. ''Por favor, escolha uma opção válida.')


if __name__ == '__main__':
    main()