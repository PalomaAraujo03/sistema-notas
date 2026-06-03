Sistema de Gerenciamento de Notas Acadêmicas
Sistema desenvolvido em Python para registrar e acompanhar o desempenho
acadêmico de estudantes. Permite calcular médias, verificar aprovação e
gerar relatórios consolidados a partir de uma estrutura de lista de dicionários.

Funcionalidades

Armazenamento de alunos e notas em lista de dicionários
Cálculo de média aritmética por aluno
Verificação de aprovação com critério de corte configurável
Geração de relatório formatado no terminal


Pré-requisitos

Python 3.10 ou superior instalado
Sem dependências externas — usa apenas a biblioteca padrão do Python

Para verificar a versão do Python instalada, execute no terminal:
bashpython --version

Estrutura do projeto
sistema-notas/
│
├── funcoes_documentadas.py   # funções principais + estrutura de dados
├── gerar_relatorio.py        # função de relatório isolada
└── README.md                 # este arquivo

Como executar o sistema
1. Clone ou baixe o projeto
Se estiver usando Git:
bashgit clone https://github.com/seu-usuario/sistema-notas.git
cd sistema-notas
Ou simplesmente salve os arquivos .py em uma pasta local.
2. Execute o arquivo principal
bashpython funcoes_documentadas.py
Saída esperada no terminal:
================================================
  NOME                    MÉDIA  SITUAÇÃO
================================================
  Ana Beatriz Lima         7.80  Aprovado
  Carlos Eduardo Melo      5.06  Reprovado
  Diana Ferreira           8.70  Aprovado
  Eduardo Santos           4.20  Reprovado
  Fernanda Oliveira        7.30  Aprovado
================================================
3. Execute apenas o relatório
bashpython gerar_relatorio.py

Como acionar os testes
Os testes automatizados estão embutidos no arquivo principal e cobrem
as funções calcular_media e verificar_aprovacao, incluindo casos
normais, valores limite e critérios personalizados de corte.
Executar os testes diretamente
bashpython -m doctest funcoes_documentadas.py -v
A flag -v (verbose) exibe cada teste individualmente com o resultado:
Trying:
    calcular_media([8.0, 6.0, 10.0])
Expecting:
    8.0
ok
...
3 items passed all tests
12 tests in 3 items.
12 passed and 0 failed.
Test passed.
Executar sem saída detalhada
bashpython -m doctest funcoes_documentadas.py
Nenhuma saída significa que todos os testes passaram.

Configuração do critério de aprovação
A nota mínima para aprovação está definida como constante no topo do arquivo:
pythonMEDIA_MINIMA_APROVACAO = 7.0
Para alterar o critério institucional, edite apenas essa linha.
Todas as funções que dependem dessa constante serão atualizadas automaticamente.

Exemplo de uso programático
pythonfrom funcoes_documentadas import calcular_media, verificar_aprovacao

notas  = [8.5, 7.0, 9.0]
media  = calcular_media(notas)           # 8.17
status = verificar_aprovacao(media)      # 'Aprovado'

print(f"Média: {media} — {status}")

Padrões adotados
ItemPadrãoLinguagemPython 3.10+Nomenclaturasnake_case (PEP 8)Documentação internaDocstrings Google StyleTestesdoctest (biblioteca padrão)EncodingUTF-8
