# modules/cli/full_pipeline.py

import os
from coverage_tool.modules.extractors.coverage_extractors import extract_coverage
from coverage_tool.modules.processors.original_processor import process_original_project_sum
from coverage_tool.utils.utils import get_original_project_sum, list_folders_to_menu

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../datasets'))

def main():
    language_path = list_folders_to_menu(parent_dir, word='Language')
    dataset_abs_path = os.path.join(parent_dir, language_path, 'raw')
    output_path = os.path.join(parent_dir, language_path, 'processed')
    language = language_path.split('/')[-1]

    # Etapa 1: Extração dos dados brutos
    print("\n[1] Extraindo dados brutos...")
    extract_coverage(language, dataset_abs_path, output_path)

    # Etapa 2: Verifica se o usuário quer calcular soma do projeto original
    print("\n[2] Processando soma dos projetos originais...")
    values_test = {}

    if get_original_project_sum():
        # process_original_project_sum(language, output_path, values_test)
        process_original_project_sum(language, output_path, parent_dir, values_test)
    else:
        print("[!] Ainda vamos integrar aqui o fluxo do cálculo de diferença (próxima etapa)")

    print("\nPipeline finalizado com sucesso! 🎉")

if __name__ == "__main__":
    main()
