import os
import pandas as pd
from coverage_tool.utils.helpers import sums_calculate, contains_test, get_split_name, generate_aggregate_csv
from coverage_tool.utils.utils import list_files_2_menu


def _generate_column_summaries(df, output_path, param, smell_name=None, original=False):
    column_mappings = {
        'statements_diff': '_statements',
        'missing_diff': '_missing',
        'LINE_COVERED': '_LINE_COVERED',
        'LINE_MISSED': '_LINE_MISSED',
    }

    for column, suffix in column_mappings.items():
        if column in df.columns:
            total, pos, neg = sums_calculate(df[column])

            result = {
                column: {
                    'total': total,
                    'lost_coverage_lines': neg if not original and column in ['statements_diff', 'missing_diff'] else pos,
                    'improve_coverage_lines': pos if not original and column in ['statements_diff', 'missing_diff'] else neg,
                }
            }

            if original:
                filename = f"{param}_{suffix}.csv"
            else:
                filename = f"{param['project']}.{param['llm']}.{param['version']}.{smell_name}{suffix}_results.csv"

            full_path = os.path.join(output_path, filename)

            pd.DataFrame.from_dict(result, orient='index').to_csv(full_path)

            if not original:
                generate_aggregate_csv(output_path, param)


def get_sums_columns(dataframe, output_file_path, param, flag=True):
    if flag:
        print('[ATTENTION] - Original DataFrame ...')
        dataframe = pd.read_csv(dataframe)
        dataframe = dataframe[~dataframe.iloc[:, 0].apply(contains_test)]

        _generate_column_summaries(dataframe[:-1], output_file_path, param, original=True)

    else:
        dataframe = dataframe[:-1]
        dataframe = dataframe[~dataframe.iloc[:, 0].apply(contains_test)]

        smell_name = get_split_name(output_file_path, '.', -2)
        llm_model = param['llm']
        version_number = param['version']
        project_name = param['project']
        language = param['language']

        output_file_path = os.path.join(
            param['parent_dir'],
            language,
            'coverage/data_analysis/_total/refactored/optimization',
            llm_model,
            version_number,
            project_name
        )
        os.makedirs(output_file_path, exist_ok=True)

        _generate_column_summaries(dataframe, output_file_path, param, smell_name=smell_name)

#
# def process_original_project_sum(language, dataset_abs_path, parent_dir, values_test):
#     original_project_file_path = list_files_2_menu(
#         os.path.join(language, dataset_abs_path), word='Project'
#     )
#
#     original_project_name = os.path.basename(original_project_file_path)\
#         .replace("(Original_File)-", "").replace(".csv", "")
#
#     values_test['project'] = original_project_name
#
#     output_file_path = os.path.join(
#         parent_dir,
#         os.path.basename(language),
#         'coverage/data_analysis/_total/originals/'
#     )
#     os.makedirs(output_file_path, exist_ok=True)
#
#     get_sums_columns(original_project_file_path, output_file_path, values_test['project'], flag=True)