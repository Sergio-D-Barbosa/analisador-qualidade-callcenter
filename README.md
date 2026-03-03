# Analisador de Qualidade para Call Center (Projeto 01)

Estou estudando desenvolvimento web back end, decidir aplicar o que aprendi em Python e SQL para criar uma ferramenta que automatize processos de qualidade.

### O que o código faz:
1. **Lê logs de atendimento:** Ele pega um arquivo `.txt` (simulando a exportação de um sistema real).
2. **Mineração de Dados:** Varre a transcrição em busca de termos críticos como "PROCON", "cancelar" ou "absurdo".
3. **Inteligência de Banco de Dados:** Salva tudo num banco SQLite, com utilização UNIQUE para que o mesmo protocolo não seja duplicado, mesmo se rodar o script várias vezes.
4. **Relatório Real:** No final, ele retorna o percentual de criticidade da operação.

### Aprendizado:
- **Tratamento de Erros:** Usei `try/except` para o código não quebrar se encontrar uma linha mal formatada.
- **SQL Além do Básico:** Entendi a importância do `INSERT OR IGNORE` e de como o banco pode ajudar na integridade dos dados.
- **Organização:** Separei a lógica de análise em funções (`def`) para deixar o código limpo e fácil de mexer depois.

---
