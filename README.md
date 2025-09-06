# Desafio Back-End — Valcann

>Este repositório reúne as soluções desenvolvidas para o Desafio Back-End.
>Aqui você encontra apenas um resumo das respostas; os detalhes completos estão organizados nas pastas correspondentes a cada questão.

## Questão 1

- Arquivo principal: `1-QUESTAO/Q01.md`
- O MER (modelo entidade-relacionamento) representa **Benchmark, Controle e Histórico de dados.**
- Diagrama disponível em: `assets/benchmark.png`

---

- **Resumo:** Modelo conceitual para organizar benchmarks e acompanhar evolução de controles.

## Questão 2

- Arquivo principal: `2-QUESTAO/cleanup_and_backup.py`
- Arqueivo secundario(Descreve detalhadamente o script): `2-QUESTAO/Q02.md`

### Como executar

1. Editar as variáveis no inicio da função `main()`:

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
    - Deletar arquivos mais antigos que `DIAS_BACKUP`(3 dias).
    - Copiar os arquivos menores ou iguais a `DIAS_BACKUP` para `PASTA_BACKUP`.
    - Gera dois .logs, um como a lista de todos os arquiivos e outro com a lista de ações tomada pelo script.

---

- **Resumo:** Script que remove arquivos antigos, copia os válidos e gera logs de execução.

## Questão 3

- Arquivo principal: `3-QUESTAO/Q03.md`
- Solução: proposta de pipeline CI/CD para automação de build e deploy.
- Diagrama disponível em assets/fluxograma-de-funcionamento.png.

---

### Resumo

- **Problema:** Deploy manual de Node.js + React → retrabalho, erros humanos e demora nas entregas.
- **Causa:** Processo sem automação, sem CI/CD.
- **Solução:** Implantar pipelines de **CI/CD no GitLab** para automatizar build, testes e deploy (homologação e produção).

- A resposta detalhada esta no arquivo **`Q03.md`**.
