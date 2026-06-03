# 🎓 Sistema de Gerenciamento de Notas Acadêmicas

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![License](https://img.shields.io/badge/Projeto-Educacional-orange)

Sistema desenvolvido em **Python** para registrar e acompanhar o desempenho acadêmico de estudantes. O projeto permite calcular médias, verificar aprovação e gerar relatórios consolidados utilizando listas e dicionários.

---

## ✨ Funcionalidades

✅ Cadastro de alunos e notas

✅ Cálculo automático de médias

✅ Verificação de aprovação ou reprovação

✅ Relatório formatado no terminal

✅ Testes automatizados com `doctest`

---

## 🛠️ Tecnologias Utilizadas

* Python 3.10+
* Biblioteca Padrão do Python
* Doctest

---

## 📂 Estrutura do Projeto

```text
sistema-notas/
│
├── funcoes_documentadas.py
├── gerar_relatorio.py
└── README.md
```

---

## 🚀 Como Executar

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/PalomaAraujo03/sistema-notas.git
cd sistema-notas
```

### 2️⃣ Executar o sistema

```bash
python funcoes_documentadas.py
```

---

## 📊 Exemplo de Saída

```text
================================================
  NOME                    MÉDIA  SITUAÇÃO
================================================
  Ana Beatriz Lima         7.80  Aprovado
  Carlos Eduardo Melo      5.06  Reprovado
  Diana Ferreira           8.70  Aprovado
  Eduardo Santos           4.20  Reprovado
  Fernanda Oliveira        7.30  Aprovado
================================================
```

---

## 🧪 Executando os Testes

### Modo detalhado

```bash
python -m doctest funcoes_documentadas.py -v
```

### Modo resumido

```bash
python -m doctest funcoes_documentadas.py
```

✔️ Se nenhuma mensagem for exibida, todos os testes passaram com sucesso.

---

## ⚙️ Configuração da Aprovação

A nota mínima para aprovação é definida pela constante:

```python
MEDIA_MINIMA_APROVACAO = 7.0
```

Caso deseje alterar o critério de aprovação, basta modificar esse valor.

---

## 💻 Exemplo de Uso

```python
from funcoes_documentadas import calcular_media, verificar_aprovacao

notas = [8.5, 7.0, 9.0]

media = calcular_media(notas)
status = verificar_aprovacao(media)

print(f"Média: {media:.2f} - {status}")
```

---

## 📈 Boas Práticas Aplicadas

| Item            | Descrição    |
| --------------- | ------------ |
| 🐍 Linguagem    | Python 3.10+ |
| 📚 Documentação | Docstrings   |
| 🧹 Convenções   | PEP 8        |
| 🧪 Testes       | doctest      |
| 🔤 Codificação  | UTF-8        |

---

## 👩‍💻 Sobre a Autora

**Paloma Araújo**

🎓 Estudante de Engenharia de Software

💡 Interessada em desenvolvimento de sistemas, programação e tecnologia.

🚀 Desenvolvendo projetos para aprimorar conhecimentos em Python, lógica de programação e boas práticas de desenvolvimento.

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!

