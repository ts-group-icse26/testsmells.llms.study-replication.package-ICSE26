import os
from coverage_tool.utils.utils import list_files_2_menu
from coverage_tool.utils.analysis_utils import get_sums_columns

def process_original_project_sum(language, dataset_abs_path, parent_dir, values_test):
    original_project_file_path = list_files_2_menu(
        os.path.join(language, dataset_abs_path), word='Project'
    )

    original_project_name = os.path.basename(original_project_file_path)\
        .replace("(Original_File)-", "").replace(".csv", "")

    values_test['project'] = original_project_name

    output_file_path = os.path.join(
        parent_dir,
        os.path.basename(language),
        'coverage/data_analysis/_total/originals/'
    )
    os.makedirs(output_file_path, exist_ok=True)

    get_sums_columns(original_project_file_path, output_file_path, values_test['project'], flag=True)
