# modules/processors/compare.py

import os
from utils.get_original_project_sum import get_original_project_sum
from extractors.coverage_extractors import list_datasets_files
from utils import compare_and_calculate_difference  # Se já estiver definida


def compare_projects(language, dataset_abs_path, extraction_results_path, output_folder):
    if get_original_project_sum(ask_user=True):  # A interação com o usuário acontece aqui
        process_original_project_sum(language, dataset_abs_path)  # Essa função deve ser definida em algum lugar.
    else:
        # Obtém os arquivos e projetos
        original_files = list_datasets_files(language, dataset_abs_path)

        approaches = list_folders_to_menu(extraction_results_path, word='Approach')
        llms = list_folders_to_menu(approaches, word='LLM')
        versions = list_folders_to_menu(llms, word='Version')

        # Lógica para iterar sobre os projetos e calcular diferenças
        for original_project in original_files:
            # ... o restante do código de comparação
            pass
