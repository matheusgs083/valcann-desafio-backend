# Desafio Back-End — Valcann

> Este repositório reúne as soluções desenvolvidas para o **Desafio Back-End**.
> Este arquivo apresenta apenas um **resumo das respostas**; os detalhes completos estão organizados nas pastas correspondentes a cada questão.

---

## Questão 1

* **Arquivo principal:** `1-QUESTAO/Q01.md`
* **Descrição:** O MER (modelo entidade-relacionamento) representa **Benchmark, Controle e Histórico de dados**.
* **Diagrama:** `assets/benchmark.png`
* **Resumo:** Modelo conceitual para organizar benchmarks e acompanhar a evolução de controles.

---

## Questão 2

* **Arquivo principal:** `2-QUESTAO/cleanup_and_backup.py`
* **Arquivo detalhado:** `2-QUESTAO/Q02.md`
* **Descrição:** Script em Python para gerenciamento de arquivos, que remove arquivos antigos, copia os válidos e gera logs de execução.

### Como executar

1. Editar as variáveis no início da função `main()`:

   ```python
   DIAS_BACKUP = 3
   PASTA_ORIGEM = "/home/usuario/backupsFrom"
   PASTA_BACKUP = "/home/usuario/backupsTo"
   LOG_COMPLETO = "/home/usuario/backupsFrom.log"
   LOG_ACOES = "/home/usuario/backupsTo.log"
   ```

2. Rodar no terminal:

   ```bash
   python cleanup_and_backup.py
   ```

3. O script vai:

   * Deletar arquivos mais antigos que `DIAS_BACKUP`.
   * Copiar arquivos com até `DIAS_BACKUP` dias para `PASTA_BACKUP`.
   * Gerar dois logs (`.log`): um completo e outro resumido com as ações tomadas.

* **Resumo:** Script que remove arquivos antigos, realiza backup dos arquivos válidos e gera logs detalhados.

---

## Questão 3

* **Arquivo principal:** `3-QUESTAO/Q03.md`

* **Descrição:** Proposta de pipeline CI/CD para automação de build e deploy de Node.js + React.

* **Diagrama:** `assets/fluxograma-de-funcionamento.png`

* **Resumo:**

  * **Problema:** Deploy manual → retrabalho, erros humanos e demora nas entregas.
  * **Causa:** Processo sem automação, sem CI/CD.
  * **Solução:** Implementar pipelines de **CI/CD no GitLab** para automatizar build, testes e deploy (homologação e produção).

* A resposta detalhada está no arquivo **`Q03.md`**.
