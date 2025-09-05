import os
import shutil
import datetime
import csv
from pathlib import Path

def salvar_log_csv(caminho_log, cabecalho, dados):
    try:
        with open(caminho_log, 'w', newline='', encoding='utf-8') as log_file:
            escritor_csv = csv.writer(log_file, delimiter=';')
            escritor_csv.writerow(cabecalho)
            escritor_csv.writerows(dados)
        print(f"Log salvo com sucesso em '{caminho_log}'")
    except Exception as e:
        print(f"Erro ao salvar o log '{caminho_log}': {e}")

def obter_detalhes_arquivo(caminho_item, acao_tomada=""):
    try:
        stats = caminho_item.stat()
        tipo = "Diretorio" if caminho_item.is_dir() else caminho_item.suffix
        tamanho_bytes = stats.st_size
        tamanho_mb = round(tamanho_bytes / (1024 * 1024), 2)
        data_modificacao = datetime.datetime.fromtimestamp(stats.st_mtime)

        return [caminho_item.name, tipo, tamanho_mb, data_modificacao, acao_tomada]
    except Exception as e:
        print(f"Erro ao obter detalhes de '{caminho_item.name}': {e}")
        return [caminho_item.name, "ERRO", 0, "", ""]

def gerenciar_arquivos(caminho_origem, caminho_backup, dias_para_backup):
    caminho_origem = Path(caminho_origem)
    caminho_backup = Path(caminho_backup)

    if not caminho_origem.is_dir():
        print(f"Erro: O caminho de origem '{caminho_origem}' não existe ou não é um diretório.")
        return [], []

    caminho_backup.mkdir(parents=True, exist_ok=True)
    data_corte = datetime.datetime.now() - datetime.timedelta(days=dias_para_backup)
    
    detalhes_completos = []
    detalhes_acoes = []

    print("--- Gerenciamento de Arquivos em Andamento ---")
    print(f"Arquivos com mais de {dias_para_backup} dias serão DELETADOS.")
    print(f"Arquivos com {dias_para_backup} dias ou menos serão COPIADOS para '{caminho_backup}'.\n")

    for item in caminho_origem.iterdir():
        if item.is_file():
            try:
                data_modificacao = datetime.datetime.fromtimestamp(item.stat().st_mtime)

                # Captura os detalhes antes da ação
                detalhes_item = obter_detalhes_arquivo(item)

                if data_modificacao < data_corte:
                    os.remove(item)
                    acao = "DELETADO"
                else:
                    shutil.copy2(item, caminho_backup / item.name)
                    acao = "COPIADO"

                # Atualiza ação nos detalhes
                detalhes_item[-1] = acao

                detalhes_completos.append(detalhes_item)
                detalhes_acoes.append([item.name, acao, data_modificacao])
                
                print(f"Processado: {item.name} -> {acao}")

            except Exception as e:
                print(f"Erro ao processar '{item.name}': {e}")
                detalhes_acoes.append([item.name, "ERRO", datetime.datetime.now()])
        else:
            print(f"Pulado: {item.name} (é um diretório)")

    return detalhes_completos, detalhes_acoes

def main():
    # Variáveis fixas
    DIAS_BACKUP = 3
    PASTA_ORIGEM = r"/home/valcann/backupsFrom"
    PASTA_BACKUP = r"/home/valcann/backupsTo"
    LOG_COMPLETO = r"/home/valcann/backupsFrom.log"
    LOG_ACOES = r"/home/valcann/backupsTo.log"
    
    CABECALHO_COMPLETO = ['Nome', 'Tipo', 'Tamanho (MB)', 'Data de Modificacao', 'Acao']
    CABECALHO_ACOES = ['Nome do Arquivo', 'Acao', 'Data de Modificacao']

    detalhes_completos, detalhes_acoes = gerenciar_arquivos(PASTA_ORIGEM, PASTA_BACKUP, DIAS_BACKUP)

    if detalhes_completos:
        salvar_log_csv(LOG_COMPLETO, CABECALHO_COMPLETO, detalhes_completos)
    
    if detalhes_acoes:
        salvar_log_csv(LOG_ACOES, CABECALHO_ACOES, detalhes_acoes)
    
    print("\nProcesso de gerenciamento de arquivos concluído.")

if __name__ == "__main__":
    main()
