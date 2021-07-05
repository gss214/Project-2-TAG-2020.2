"""
Projeto 2 da disciplina Teoria e Aplicação de Grafos

Universidade de Brasilia
Instituto de Ciencias Exatas
Departamento de Ciencia da Computacao
Teoria e Aplicação de Grafos – 2/2020
Professor: Díbio Leandro Borges
Desenvolvido por: Guilherme Silva Souza

Considere para efeito deste projeto que uma determinada unidade da federação fez um concurso e foramaprovados cem (100) novos professores para escolas públicas.
Cada professor aprovado possui uma (1),duas (2), ou até (3) habilitacaoilitações de conteúdos em que pode atuar. Cinquenta (50) escolas se habilitacaoilitarama receber novos professores,
sendo que algumas poderão receber no máximo um (1) professor, e outrasno máximo dois (2) professores. As escolas podem indicar preferências de professores indicando se 3, 2 ou 1 
habilitacaoilitação os candidatos devem ter minimamente. Por sua vez, cada professor pode escolher uma ordem de até quatro (4) escolas onde gostaria de atuar. Neste projeto você deve   
implementar um algoritmo que realize um emparelhamento estável máximo, devendo incluir pelo menos 1 professor paracada escola, e indicar quantos professores poderão ser alocados estavelmente.
As soluções dadas em(Abraham, Irving & Manlove, 2007) são úteis e qualquer uma pode ser implementada com variaçõespertinentes. Um arquivo entradaProj2TAG.txt com as indicações de código do professor,
habilitacaoilitações epreferências de escolas, bem como das escolas com suas preferências em termos de habilitacaoilitações dosprofessores é fornecido como entrada. Uma versão pública do artigo de 
(Abraham, Irving & Manlove,2007) é fornecida para leitura.

Para uma melhor leitura do output, execute o programa:

python3 projeto2.py > output.txt

e abra o arquivo output.txt
"""


def monta_grafo():
    """
    A função monta o grafo a partir do arquivo de input dado. E retorna um dicionario de professores e escolas
    """

    professores = {}
    escolas = {}

    with open('entradaProj2TAG.txt') as file:
        for line in file:
            if not line.startswith('//'):
                line = line.replace('(', '').replace(')',
                                                     '').strip().split(':')
                if line[0].startswith('P'):
                    professor = line[0].split()
                    professores[int(professor[0].replace(',', '').replace('P', ''))] = {'id': int(professor[0].replace(',', '').replace('P', '')), 'habilitacao': int(
                        professor[1]), 'escolas_pref': list(map(int, line[1].strip().replace('E', '').split(', '))), 'local_trabalho': -1, 'livre': True}
                elif line[0].startswith('E'):
                    vagas = [int(i) for i in range(1, len(line))]
                    if len(vagas) < 2:
                        vagas.append(-1)
                    escolas[int(line[0].replace('E', ''))] = {'id': int(line[0].replace('E', '')),
                                                              'habilitacao_pret': vagas, 'vagas_preenchidas': [False] * len(vagas), 'professores': [-1, -1], 'margem': [False, False]}

    return professores, escolas


def aloca(id_professor, professores_livres, escolas_livres):
    """
    A função é responsável por alocar um professor livre na escola dependendo das condições. Primeiro é verificado se o professor esta livre
    e se a habilitação do professor é maior ou igual que a habilitação da escola na lista de preferências do professor (que é pecorrida pelo laço principal),
    se for ele verifica se a escola já tem professor alocado, se não tiver ela aloca o professor na escola. O mesmo acontce para a segunda vaga. Se nenhuma
    condição for satisfeita, a função retorna false.
    """
    for i in range(len(professores_livres[id_professor]['escolas_pref'])):
        id_escola = professores_livres[id_professor]['escolas_pref'][i]
        if (professores_livres[id_professor]['livre'] == True) and (professores_livres[id_professor]['habilitacao'] >= escolas_livres[id_escola]['habilitacao_pret'][0]) or ((professores_livres[id_professor]['habilitacao'] >= escolas_livres[id_escola]['habilitacao_pret'][1]) and (escolas_livres[id_escola]['habilitacao_pret'][1] != -1)):
            if (escolas_livres[id_escola]['vagas_preenchidas'][0] == False) and (professores_livres[id_professor]['habilitacao'] >= escolas_livres[id_escola]['habilitacao_pret'][0]):
                professores_livres[id_professor]['livre'] = False
                professores_livres[id_professor]['local_trabalho'] = escolas_livres[id_escola]['id']
                escolas_livres[id_escola]['vagas_preenchidas'][0] = True
                escolas_livres[id_escola]['professores'][0] = professores_livres[id_professor]['id']
                if professores_livres[id_professor]['habilitacao'] > escolas_livres[id_escola]['habilitacao_pret'][0]:
                    escolas_livres[id_escola]['margem'][0] = True
                elif professores_livres[id_professor]['habilitacao'] == escolas_livres[id_escola]['habilitacao_pret'][0]:
                    escolas_livres[id_escola]['margem'][0] = False
                return True

            if (escolas_livres[id_escola]['vagas_preenchidas'][1] == False) and ((professores_livres[id_professor]['habilitacao'] >= escolas_livres[id_escola]['habilitacao_pret'][1]) and (escolas_livres[id_escola]['habilitacao_pret'][1] != -1)):
                professores_livres[id_professor]['livre'] = False
                professores_livres[id_professor]['local_trabalho'] = escolas_livres[id_escola]['id']
                escolas_livres[id_escola]['vagas_preenchidas'][1] = True
                escolas_livres[id_escola]['professores'][1] = professores_livres[id_professor]['id']
                if professores_livres[id_professor]['habilitacao'] > escolas_livres[id_escola]['habilitacao_pret'][0]:
                    escolas_livres[id_escola]['margem'][0] = True
                elif professores_livres[id_professor]['habilitacao'] == escolas_livres[id_escola]['habilitacao_pret'][0]:
                    escolas_livres[id_escola]['margem'][0] = False
                return True
    return False


def substitui(id_professor, professores_livres, escolas_livres):
    """
    A função é responsável por substituir um professor. Ela verifica se a habilitação do professor é maior ou igual a habilitação pretendida
    da escola, se sim ele verifica se a escola tem margem, então ele faz a troca e retorna o professor antigo. Ela compara as duas vagas caso tenha
    e a primeira condição foi falhada. Se as duas condições falharem retorna -1.
    """
    antigo = None
    for i in range(len(professores_livres[id_professor]['escolas_pref'])):
        id_escola = professores_livres[id_professor]['escolas_pref'][i]
        if (professores_livres[id_professor]['habilitacao'] >= escolas_livres[id_escola]['habilitacao_pret'][0]) or ((professores_livres[id_professor]['habilitacao'] >= escolas_livres[id_escola]['habilitacao_pret'][1]) and (escolas_livres[id_escola]['habilitacao_pret'][1] != -1)):
            if(professores_livres[id_professor]['habilitacao'] >= escolas_livres[id_escola]['habilitacao_pret'][0]) and (escolas_livres[id_escola]['margem'][0] == True) and (escolas_livres[id_escola]['professores'][0] != professores_livres[id_professor]['id']) and (escolas_livres[id_escola]['professores'][1] != professores_livres[id_professor]['id']):
                professores_livres[id_professor]['livre'] = False
                professores_livres[id_professor]['local_trabalho'] = escolas_livres[id_escola]['id']
                escolas_livres[id_escola]['vagas_preenchidas'][0] = True
                if professores_livres[id_professor]['habilitacao'] > escolas_livres[id_escola]['habilitacao_pret'][0]:
                    escolas_livres[id_escola]['margem'][0] = True
                elif professores_livres[id_professor]['habilitacao'] == escolas_livres[id_escola]['habilitacao_pret'][0]:
                    escolas_livres[id_escola]['margem'][0] = False
                antigo = escolas_livres[id_escola]['professores'][0]
                professores_livres[antigo]['livre'] = True
                escolas_livres[id_escola]['professores'][0] = professores_livres[id_professor]['id']
                return antigo

            if (professores_livres[id_professor]['habilitacao'] >= escolas_livres[id_escola]['habilitacao_pret'][1] and (escolas_livres[id_escola]['habilitacao_pret'][1] != -1)) and (escolas_livres[id_escola]['margem'][1] == True) and (escolas_livres[id_escola]['professores'][0] != professores_livres[id_professor]['id']) and (escolas_livres[id_escola]['professores'][1] != professores_livres[id_professor]['id']):
                professores_livres[id_professor]['livre'] = False
                professores_livres[id_professor]['local_trabalho'] = escolas_livres[id_escola]['id']
                escolas_livres[id_escola]['vagas_preenchidas'][1] = True
                if professores_livres[id_professor]['habilitacao'] > escolas_livres[id_escola]['habilitacao_pret'][1]:
                    escolas_livres[id_escola]['margem'][1] = True
                elif professores_livres[id_professor]['habilitacao'] == escolas_livres[id_escola]['habilitacao_pret'][1]:
                    escolas_livres[id_escola]['margem'][1] = False
                antigo = escolas_livres[id_escola]['professores'][1]
                professores_livres[antigo]['livre'] = True
                escolas_livres[id_escola]['professores'][1] = professores_livres[id_professor]['id']
                return antigo
    return -1


def gale_shapley(professores_livres, escolas_livres, maximo, it):
    """
    A função executa o algoritimo de Gale Shapley. Obtemos uma fila de professores livres e vamos tentando alocar 
    cada professor conforme as funções acima. O algoritimo utilizar uma fila, que inicialmente tem todos os professores
    livres, e é executado um loop onde é tentado alocar o professor em uma escola. Ele roda até a lista ficar vazia.
    Quando é rodado mais de uma vez obtem-se um emparelhamento melhor.
    """
    professor_f = []
    for i in professores_livres.keys():
        if professores_livres[i]['livre'] == True:
            professor_f.append(i)

    while len(professor_f) > 0:
        atual = professor_f[0]
        professor_f.pop(0)

        if type(atual) == int:
            if (aloca(atual, professores_livres, escolas_livres) == False):
                saiu = substitui(atual, professores_livres, escolas_livres)
                if saiu != -1:
                    atual = professores_livres[saiu]
                    professor_f.append(atual)

    if maximo == False or it == 10:
        professores_alocados = 0
        for i in escolas_livres:
            x = None
            if escolas_livres[i]['professores'][1] != -1:
                professores_alocados += 1
                x = escolas_livres[i]['professores'][1]
            else:
                x = 'X'

            print(
                f"A escola {i} ficou com os professores {escolas_livres[i]['professores'][0]} e {x}")

            if escolas_livres[i]['professores'][0] != -1:
                professores_alocados += 1

        print(f'\nProfessores alocados {professores_alocados}')


def main():
    professores_livres, escolas_livres = monta_grafo()
    print('Emparelhamento estavel: (X significa que nao tem nenhum professor alocado na vaga)\n')
    gale_shapley(professores_livres, escolas_livres, False, 0)
    print('\nEmparelhamento maximo: (X significa que nao tem nenhum professor alocado na vaga)\n')
    alocados = 0
    for i in range(11):
        gale_shapley(professores_livres, escolas_livres, True, i)


if __name__ == "__main__":
    main()
