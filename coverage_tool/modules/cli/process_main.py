import os
import argparse
from ..extractors.coverage_extractors import extract_coverage, list_datasets_files
from ..processors.original_processor import process_original_project_sum
from coverage_tool.utils.utils import get_original_project_sum  # Assumindo que essa função esteja aqui


def main():
    # Argumentos de entrada
    parser = argparse.ArgumentParser(description="Process test coverage reports")
    parser.add_argument("--language", required=True, choices=["java", "python"], help="Programming language")
    parser.add_argument("--source", required=True, help="Path to the source coverage report")
    parser.add_argument("--output", required=True, help="Path to the output CSV folder")
    parser.add_argument("--dataset_path", required=True,
                        help="Path to the original dataset")  # Adicionando o dataset_path

    args = parser.parse_args()

    # Passo 1: Extração dos dados brutos
    print(f"Extraindo dados de cobertura para {args.language}...")
    extract_coverage(args.language, args.source, args.output)
    print("Extração de dados concluída!")

    # Passo 2: Obter soma dos arquivos originais
    if get_original_project_sum():  # Função que pergunta ao usuário se deve somar os arquivos
        print("Processando soma dos arquivos originais...")
        process_original_project_sum(args.language, args.dataset_path)
        print("Soma dos arquivos concluída!")
    else:
        print("Iniciando processamento das diferenças de projetos refatorados...")

        # Passo 3: Processar as diferenças dos arquivos
        original_files = list_datasets_files(args.language, args.dataset_path)

        for original_file in original_files:
            print(f"Processando o arquivo original: {original_file}")
            # Aqui você pode adicionar a lógica para comparar ou calcular as diferenças
            # com o arquivo refatorado, conforme seu fluxo anterior.
            # Exemplo de processamento que você já configurou no fluxo anterior
            # process_refactored_projects(...) ou outras funções de comparação
            # podem ser chamadas aqui.

    print("Processamento finalizado!")


if __name__ == "__main__":
    main()
