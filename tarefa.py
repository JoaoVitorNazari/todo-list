# ============================================================
# FUNÇÃO DE ESCOLHA
# ============================================================

def escolha(mensagem):
    """Solicita uma resposta de sim ou não. Retorna True para 's' e False para 'n'."""

    while True:
        resposta = input(mensagem).strip().lower()

        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print('Opção inválida, digite "s" para sim ou "n" para não.')

def status_tarefa(tarefa):
    if tarefa['concluida']:
        return '[Concluída]'
    return '[Pendente]'

# ============================================================
# ADICIONAR TAREFA
# ============================================================

def adicionar_tarefa(tarefas, proximo_id):

    while True:

        nome = input('Digite o nome da tarefa: ').strip()

        if not nome:
            print('O nome da tarefa não pode ser vazio. ''Por favor, digite um nome válido.')
            continue
            
        tarefa = {'ID': proximo_id,'nome': nome,'concluida': False}

        tarefas.append(tarefa)

        print(f'Tarefa "{nome}" 'f'(ID {proximo_id}) adicionada com sucesso!')
        proximo_id += 1

        if not escolha('Deseja adicionar mais tarefas? (s/n): '):
            return proximo_id

# ============================================================
# PESQUISAR TAREFA
# ============================================================

def pesquisa_tarefa(tarefas):

    if not tarefas:
        print('Nenhuma tarefa cadastrada!')
        return

    print('\nMenu de pesquisa de tarefas:')
    print('\n1. Pesquisar por ID ou nome da tarefa')
    print('\n2. Filtrar por status da tarefa (concluída/pendente)')
    input_opcao = input('\nEscolha uma opção: ').strip()

    if input_opcao == '1':
        while True:
            pesquisa = input('Pesquise pelo ID ou nome da tarefa: ').strip().lower()

            tarefas_encontradas = [tarefa for tarefa in tarefas if pesquisa == str(tarefa['ID']) or pesquisa in tarefa['nome'].lower()]

            if tarefas_encontradas:
                print('\nTarefas encontradas:')

                for tarefa in tarefas_encontradas:
                    status = status_tarefa(tarefa)

                    print(f'ID {tarefa["ID"]}: 'f'{tarefa["nome"]} - 'f'Status: {status}')
            else:
                print('Nenhuma tarefa encontrada ''com o termo de pesquisa.')

            if not escolha('Deseja pesquisar mais tarefas? (s/n): '):
                return

    elif input_opcao == '2':
        while True:
            filtro_status = input('Digite o status desejado (concluida/pendente): ').strip().lower()

            if filtro_status not in {'concluida', 'pendente'}:
                print('Status inválido. Digite "concluida" ou "pendente".')
                continue

            tarefas_filtradas = [tarefa for tarefa in tarefas
                if (filtro_status == 'concluida' and tarefa['concluida']or filtro_status == 'pendente' and not tarefa['concluida'] )
            ]

            if tarefas_filtradas:
                print('\nTarefas filtradas:')

                for tarefa in tarefas_filtradas:
                    status = status_tarefa(tarefa)

                    print(f'ID {tarefa["ID"]}: 'f'{tarefa["nome"]} - 'f'Status: {status}')
            else:
                print('Nenhuma tarefa encontrada 'f'com o status "{filtro_status}".')

            if not escolha('Deseja filtrar mais tarefas? (s/n): '):
                return
    else:
        print('Opção inválida.')

# ============================================================
# BUSCAR TAREFA PELO ID
# ============================================================

def buscar_tarefa_por_id(tarefas, id_desejado):
    """Procura uma tarefa pelo ID."""

    for tarefa in tarefas:

        if tarefa['ID'] == id_desejado:
            return tarefa

    return None

# ============================================================
# LISTAR TAREFAS
# ============================================================

def lista_tarefas(tarefas):

    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return

    print('\nLista de tarefas:')

    for tarefa in tarefas:

        status = status_tarefa(tarefa)

        print(
            f'ID {tarefa["ID"]}: '
            f'{tarefa["nome"]} - '
            f'Status: {status}'
        )

# ============================================================
# CONCLUIR TAREFA
# ============================================================

def concluir_tarefa(tarefas):

    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return

    lista_tarefas(tarefas)

    while True:
        try:
            id_desejado = int(input('Digite o ID da tarefa que deseja concluir: '))

            tarefa_encontrada = buscar_tarefa_por_id(tarefas,id_desejado)

            if tarefa_encontrada:
                if tarefa_encontrada['concluida']:
                    print(f'A tarefa ' f'"{tarefa_encontrada["nome"]}"'f'(ID {id_desejado}) 'f'já está concluída.')
                else:
                    tarefa_encontrada['concluida'] = True

                    print(f'Tarefa 'f'"{tarefa_encontrada["nome"]}" 'f'(ID {id_desejado}) 'f'concluída com sucesso!')
            else:
                print('ID não encontrado. ''Por favor, digite um ID válido.')
        except ValueError:
            print('Entrada inválida. ''Por favor, digite um número de ID válido.')
            continue

        if not escolha('Deseja concluir mais tarefas? (s/n): '):
            return

# ============================================================
# EXCLUIR TAREFA
# ============================================================

def excluir_tarefa(tarefas):

    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return

    lista_tarefas(tarefas)

    while True:
        try:
            id_desejado = int(input('Digite o ID da tarefa que deseja excluir: '))

            tarefa_encontrada = buscar_tarefa_por_id(tarefas,id_desejado)

            if tarefa_encontrada:
                tarefas.remove(tarefa_encontrada)

                print(f'Tarefa 'f'"{tarefa_encontrada["nome"]}" 'f'(ID {id_desejado}) 'f'excluída com sucesso!')

                if not tarefas:
                    print('Nenhuma tarefa na lista.')
                    return
            else:
                print('ID não encontrado. ''Por favor, digite um ID válido.')
        except ValueError:
            print('Entrada inválida. ''Por favor, digite um número de ID válido.')
            continue

        if not escolha('Deseja excluir mais tarefas? (s/n): '):
            return

# ============================================================
# Editar TAREFA
# ============================================================

def editar_tarefa(tarefas):

    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return

    lista_tarefas(tarefas)

    print('\n Menu de edição de tarefas:')
    print('1. Editar nome da tarefa')
    print('2. Editar status da tarefa (concluída/pendente)')
    print('3. Voltar')

    opcao = input('Escolha uma opção: ').strip()

    if opcao == '1':
     while True:
        try:
            id_desejado = int(input('Digite o ID da tarefa que deseja editar: '))

            tarefa_encontrada = buscar_tarefa_por_id(tarefas,id_desejado)

            if tarefa_encontrada:

                novo_nome = input('Digite o novo nome da tarefa: ').strip()

                if not novo_nome:
                    print('O nome da tarefa não pode ser vazio. ''Por favor, digite um nome válido.')
                    continue

                tarefa_encontrada['nome'] = novo_nome

                print(f'Tarefa 'f'"{novo_nome}" 'f'(ID {id_desejado}) 'f'editada com sucesso!')
                break
            else:
                print('ID não encontrado. ''Por favor, digite um ID válido.')
        except ValueError:
            print('Entrada inválida. ''Por favor, digite um número de ID válido.')
            continue

    elif opcao == '2':
        while True:
            try:
                id_desejado = int(input('Digite o ID da tarefa que deseja editar: '))

                tarefa_encontrada = buscar_tarefa_por_id(tarefas,id_desejado)

                if tarefa_encontrada:

                    tarefa_encontrada['concluida'] = not tarefa_encontrada['concluida']

                    status = status_tarefa(tarefa_encontrada)

                    print(f'Tarefa 'f'"{tarefa_encontrada["nome"]}" 'f'(ID {id_desejado}) 'f'editada com sucesso! Novo status: {status}')
                    break
                else:
                    print('ID não encontrado. ''Por favor, digite um ID válido.')
            except ValueError:
                print('Entrada inválida. ''Por favor, digite um número de ID válido.')
                continue
    elif opcao == '3':
                    return 
    else:
        print('Opção escolhida é inválida.')

