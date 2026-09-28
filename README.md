# TaskTracker

Aplicação de linha de comando (CLI) desenvolvida em Python 3 para gerenciar tarefas pessoais: cadastro, listagem e acompanhamento de status, prioridade e data limite.

Projeto do **Bootcamp II — Engenharia de Software**, Fase 2 (Entrega Intermediária).

## Descrição Funcional

O TaskTracker executa no terminal com um menu contínuo que oferece:

1. **Cadastrar nova tarefa** — registra título, descrição, prioridade e data limite. O status é definido automaticamente como `Pendente`.
2. **Visualizar tarefas cadastradas** — lista todas as tarefas com todos os campos, ou informa que não existem registros.
3. **Sair da aplicação** — encerra o programa.

### Regras de Negócio

| Campo | Regra |
|---|---|
| Título | Obrigatório. Entradas vazias ou só com espaços são rejeitadas e o prompt é repetido. |
| Descrição | Livre. |
| Prioridade | Aceita exclusivamente `Alta`, `Média` (ou `Media`) e `Baixa`. Entradas fora do padrão geram erro e repetem o prompt. |
| Data Limite | Formato livre (recomendado `DD/MM/AAAA`). |
| Status | Definido automaticamente como `Pendente` no cadastro. |

## Estrutura do Repositório

```
tasktracker-projeto/
├── README.md                      # Documentação principal
├── .gitignore                     # Regras de ignore para Python
├── docs/
│   └── planejamento_logico.pdf    # Planejamento lógico da Fase 1
└── src/
    └── main.py                    # Código-fonte da aplicação
```

## Tecnologias

- **Python 3** (testado na versão 3.8+)
- **Git / GitHub** — versionamento e publicação
- Bibliotecas padrão da linguagem (nenhuma dependência externa)

## Instalação e Execução

Requisitos: Python 3 instalado e disponível no `PATH`.

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>.git
cd tasktracker-projeto

# 2. (Opcional) crie um ambiente virtual
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 3. Execute a aplicação
python src/main.py
```

Não há dependências externas para instalar — o projeto usa apenas a biblioteca padrão.

## Exemplo de Uso

```
===== TASKTRACKER =====
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
Escolha uma opção: 1

Título: Revisar entregas do Bootcamp
Descrição: Conferir itens do barema da Fase 2
Prioridade (Alta/Média/Baixa): Alta
Data limite (DD/MM/AAAA): 30/09/2026
Tarefa cadastrada com sucesso!

Escolha uma opção: 2

--- Tarefas cadastradas ---
[1] Título: Revisar entregas do Bootcamp
    Descrição: Conferir itens do barema da Fase 2
    Prioridade: Alta
    Data limite: 30/09/2026
    Status: Pendente
```

## Versionamento

O histórico do repositório segue a evolução exigida pela Fase 2:

1. Inicialização do projeto e estrutura de pastas
2. Commit inicial (README, `.gitignore` e documento da Fase 1)
3. Estrutura principal da aplicação (menu e loop)
4. Funções de validação (título não vazio e prioridades)

## Fase 3 (Próximos Passos)

- Empacotamento da aplicação
- Containerização com Docker
- Testes automatizados e deploy
