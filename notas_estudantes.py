"""
Sistema de Gerenciamento de Notas Acadêmicas
============================================
Registra e acompanha o desempenho de estudantes por meio de
cálculo de médias, verificação de aprovação e geração de relatórios.

Estrutura do módulo:
    BLOCO 1 — Constantes
    BLOCO 2 — Estrutura de dados
    BLOCO 3 — Funções de cálculo
    BLOCO 4 — Funções de relatório
    BLOCO 5 — Testes automatizados
    BLOCO 6 — Execução principal
"""


# ══════════════════════════════════════════════════════════════════
# BLOCO 1 — CONSTANTES
# ══════════════════════════════════════════════════════════════════

MEDIA_MINIMA_APROVACAO = 7.0
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0
LARGURA_RELATORIO = 48


# ══════════════════════════════════════════════════════════════════
# BLOCO 2 — ESTRUTURA DE DADOS
# ══════════════════════════════════════════════════════════════════
#
# Cada estudante é um dicionário com os campos obrigatórios:
#   "nome"  (str)         — nome completo
#   "notas" (list[float]) — uma nota por avaliação
#
# A turma é uma lista desses dicionários.

estudantes = [
    {
        "nome": "Ana Beatriz Lima",
        "notas": [8.5, 7.0, 9.0, 6.5, 8.0],
    },
    {
        "nome": "Carlos Eduardo Melo",
        "notas": [5.0, 4.5, 5.8, 6.0, 4.0],
    },
    {
        "nome": "Diana Ferreira",
        "notas": [9.5, 8.0, 7.5, 9.0, 9.5],
    },
    {
        "nome": "Eduardo Santos",
        "notas": [3.0, 5.5, 4.0, 5.0, 3.5],
    },
    {
        "nome": "Fernanda Oliveira",
        "notas": [7.5, 8.5, 6.0, 7.0, 7.5],
    },
]


# ══════════════════════════════════════════════════════════════════
# BLOCO 3 — FUNÇÕES DE CÁLCULO
# ══════════════════════════════════════════════════════════════════


def calcular_media(notas):
    """
    Calcula a média aritmética de uma lista de notas.

    Aplica a fórmula: média = soma dos valores / quantidade de valores.
    O resultado é arredondado em duas casas decimais para evitar
    imprecisões de ponto flutuante (ex.: 7.000000000000001).

    Args:
        notas (list[float]): Lista com ao menos uma nota numérica.
            Cada elemento deve estar no intervalo 0.0–10.0.

    Returns:
        float: Média aritmética arredondada em duas casas decimais.

    Examples:
        >>> calcular_media([8.0, 6.0, 10.0])
        8.0
        >>> calcular_media([7.0, 7.0, 7.0])
        7.0
        >>> calcular_media([5.5, 6.5])
        6.0
    """
    soma_das_notas = sum(notas)
    quantidade_de_notas = len(notas)
    media_calculada = soma_das_notas / quantidade_de_notas
    return round(media_calculada, 2)


def verificar_aprovacao(media_obtida, media_minima=MEDIA_MINIMA_APROVACAO):
    """
    Verifica se o estudante foi aprovado com base na média obtida.

    O critério usa o operador >= (maior ou igual), portanto uma média
    exatamente igual ao corte resulta em aprovação. O parâmetro
    media_minima tem valor padrão definido pela constante
    MEDIA_MINIMA_APROVACAO, permitindo reutilização para diferentes
    critérios sem alteração do código interno da função.

    Args:
        media_obtida (float): Média aritmética calculada para o estudante.
            Deve estar no intervalo 0.0–10.0.
        media_minima (float): Nota mínima exigida para aprovação.
            Padrão: MEDIA_MINIMA_APROVACAO (7.0).

    Returns:
        str: 'Aprovado'  se media_obtida >= media_minima.
             'Reprovado' se media_obtida <  media_minima.

    Examples:
        >>> verificar_aprovacao(8.0)
        'Aprovado'
        >>> verificar_aprovacao(6.9)
        'Reprovado'
        >>> verificar_aprovacao(7.0)
        'Aprovado'
        >>> verificar_aprovacao(6.5, media_minima=6.0)
        'Aprovado'
        >>> verificar_aprovacao(7.5, media_minima=8.0)
        'Reprovado'
    """
    if media_obtida >= media_minima:
        return 'Aprovado'
    return 'Reprovado'


def calcular_maior_nota(notas):
    """
    Retorna o maior valor encontrado na lista de notas.

    Args:
        notas (list[float]): Lista com ao menos uma nota numérica.

    Returns:
        float: Maior nota da lista.

    Examples:
        >>> calcular_maior_nota([8.5, 7.0, 9.0])
        9.0
        >>> calcular_maior_nota([6.0])
        6.0
    """
    return max(notas)


def calcular_menor_nota(notas):
    """
    Retorna o menor valor encontrado na lista de notas.

    Args:
        notas (list[float]): Lista com ao menos uma nota numérica.

    Returns:
        float: Menor nota da lista.

    Examples:
        >>> calcular_menor_nota([8.5, 7.0, 9.0])
        7.0
        >>> calcular_menor_nota([6.0])
        6.0
    """
    return min(notas)


# ══════════════════════════════════════════════════════════════════
# BLOCO 4 — FUNÇÕES DE RELATÓRIO
# ══════════════════════════════════════════════════════════════════


def gerar_relatorio(lista_de_alunos):
    """
    Percorre a lista de alunos e exibe nome, média e situação de cada um.

    Para cada aluno, a função extrai as notas, calcula a média via
    calcular_media() e determina a situação via verificar_aprovacao(),
    imprimindo uma linha formatada e alinhada no terminal.

    A formatação usa f-strings com especificadores de alinhamento:
        :<22   alinha o nome à esquerda em 22 caracteres.
        :>5.2f alinha a média à direita com duas casas decimais.

    Args:
        lista_de_alunos (list[dict]): Lista de dicionários representando
            os alunos. Cada dicionário deve conter obrigatoriamente:
                - 'nome'  (str):         nome completo do aluno.
                - 'notas' (list[float]): lista com ao menos uma nota.

    Returns:
        None: A função não retorna valor; produz impressão no terminal.

    Examples:
        >>> alunos = [{"nome": "Ana Lima", "notas": [8.0, 7.0, 9.0]}]
        >>> gerar_relatorio(alunos)
        ================================================
          NOME                    MÉDIA  SITUAÇÃO
        ================================================
          Ana Lima                 8.00  Aprovado
        ================================================
    """
    separador = "=" * LARGURA_RELATORIO
    print(separador)
    print(f"  {'NOME':<22}  {'MÉDIA':>5}  SITUAÇÃO")
    print(separador)

    for aluno in lista_de_alunos:
        media_do_aluno = calcular_media(aluno["notas"])
        situacao_do_aluno = verificar_aprovacao(media_do_aluno)
        print(
            f"  {aluno['nome']:<22}"
            f"  {media_do_aluno:>5.2f}"
            f"  {situacao_do_aluno}"
        )

    print(separador)


def exibir_relatorio_individual(estudante):
    """
    Imprime o relatório detalhado de um único estudante.

    Exibe nome, lista de notas, maior nota, menor nota, média
    calculada e situação de aprovação em formato legível.

    Args:
        estudante (dict): Dicionário com os campos:
            - 'nome'  (str):         nome completo do estudante.
            - 'notas' (list[float]): lista com ao menos uma nota.

    Returns:
        None: A função não retorna valor; produz impressão no terminal.
    """
    nome_do_aluno = estudante["nome"]
    notas_do_aluno = estudante["notas"]
    media_do_aluno = calcular_media(notas_do_aluno)
    situacao_do_aluno = verificar_aprovacao(media_do_aluno)
    maior_nota = calcular_maior_nota(notas_do_aluno)
    menor_nota = calcular_menor_nota(notas_do_aluno)

    separador = "=" * LARGURA_RELATORIO
    print(separador)
    print(f"  Estudante : {nome_do_aluno}")
    print(f"  Notas     : {notas_do_aluno}")
    print(f"  Maior     : {maior_nota}")
    print(f"  Menor     : {menor_nota}")
    print(f"  Média     : {media_do_aluno}")
    print(f"  Situação  : {situacao_do_aluno}")
    print(separador)


# ══════════════════════════════════════════════════════════════════
# BLOCO 5 — TESTES AUTOMATIZADOS
# ══════════════════════════════════════════════════════════════════


def executar_testes():
    """
    Executa todos os testes do sistema e reporta os resultados.

    Testa as funções calcular_media, verificar_aprovacao,
    calcular_maior_nota e calcular_menor_nota, cobrindo casos normais,
    valores limite e parâmetros personalizados.

    Args:
        Nenhum.

    Returns:
        None: Imprime os resultados dos testes no terminal.
    """
    total_de_testes = 0
    testes_aprovados = 0
    testes_reprovados = 0

    def checar(descricao_do_teste, valor_obtido, valor_esperado):
        """
        Verifica se o valor obtido é igual ao valor esperado.

        Args:
            descricao_do_teste (str):  Texto descritivo do caso testado.
            valor_obtido (any):        Resultado retornado pela função.
            valor_esperado (any):      Resultado que deveria ser retornado.

        Returns:
            None: Imprime o resultado do teste no terminal.
        """
        nonlocal total_de_testes, testes_aprovados, testes_reprovados
        total_de_testes += 1
        if valor_obtido == valor_esperado:
            print(f"  ✓  {descricao_do_teste}")
            testes_aprovados += 1
        else:
            print(f"  ✗  {descricao_do_teste}")
            print(f"       esperado : {valor_esperado!r}")
            print(f"       obtido   : {valor_obtido!r}")
            testes_reprovados += 1

    separador = "=" * LARGURA_RELATORIO
    print(separador)
    print("  TESTES AUTOMATIZADOS")
    print(separador)

    # ── calcular_media ────────────────────────────────────────────
    print("  calcular_media()")
    print("  " + "-" * (LARGURA_RELATORIO - 2))

    checar(
        "média de três notas iguais",
        calcular_media([7.0, 7.0, 7.0]),
        7.0,
    )
    checar(
        "média de notas variadas",
        calcular_media([8.0, 6.0, 10.0]),
        8.0,
    )
    checar(
        "média com nota única",
        calcular_media([9.5]),
        9.5,
    )
    checar(
        "média com resultado inteiro",
        calcular_media([6.0, 7.0, 8.0]),
        7.0,
    )
    checar(
        "média arredondada em duas casas",
        calcular_media([7.0, 7.0, 7.0, 7.0, 7.1]),
        7.02,
    )

    # ── verificar_aprovacao ───────────────────────────────────────
    print("  verificar_aprovacao()")
    print("  " + "-" * (LARGURA_RELATORIO - 2))

    checar(
        "média acima do corte → Aprovado",
        verificar_aprovacao(8.0),
        'Aprovado',
    )
    checar(
        "média abaixo do corte → Reprovado",
        verificar_aprovacao(6.9),
        'Reprovado',
    )
    checar(
        "média igual ao corte → Aprovado (operador >=)",
        verificar_aprovacao(7.0),
        'Aprovado',
    )
    checar(
        "corte personalizado 6.0 → Aprovado",
        verificar_aprovacao(6.5, media_minima=6.0),
        'Aprovado',
    )
    checar(
        "corte personalizado 8.0 → Reprovado",
        verificar_aprovacao(7.5, media_minima=8.0),
        'Reprovado',
    )

    # ── calcular_maior_nota e calcular_menor_nota ─────────────────
    print("  calcular_maior_nota() / calcular_menor_nota()")
    print("  " + "-" * (LARGURA_RELATORIO - 2))

    checar(
        "maior nota da lista",
        calcular_maior_nota([5.0, 9.0, 7.5]),
        9.0,
    )
    checar(
        "menor nota da lista",
        calcular_menor_nota([5.0, 9.0, 7.5]),
        5.0,
    )
    checar(
        "maior nota com elemento único",
        calcular_maior_nota([6.0]),
        6.0,
    )
    checar(
        "menor nota com elemento único",
        calcular_menor_nota([6.0]),
        6.0,
    )

    # ── resumo ────────────────────────────────────────────────────
    print(separador)
    print(f"  Resultado : {testes_aprovados}/{total_de_testes} testes passaram")
    if testes_reprovados == 0:
        print("  Todos os testes aprovados. ✓")
    else:
        print(f"  {testes_reprovados} teste(s) falharam. Revise o código.")
    print(separador)


# ══════════════════════════════════════════════════════════════════
# BLOCO 6 — EXECUÇÃO PRINCIPAL
# ══════════════════════════════════════════════════════════════════
#
# O bloco if __name__ == "__main__" garante que este código
# só executa quando o arquivo é rodado diretamente:
#
#   python sistema_notas.py   → executa
#   import sistema_notas      → não executa

if __name__ == "__main__":
    executar_testes()

    print()
    print("  Relatório individual — primeiro estudante:")
    exibir_relatorio_individual(estudantes[0])

    print()
    print("  Relatório geral da turma:")
    gerar_relatorio(estudantes)