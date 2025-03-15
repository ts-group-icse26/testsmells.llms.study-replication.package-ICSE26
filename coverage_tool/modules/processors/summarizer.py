# modules/processors/summarizer.py

import pandas as pd
from coverage_tool.utils.helpers import sums_calculate


def process_column_summary(df_column: pd.Series, column_name: str) -> dict:
    total, positive_sum, negative_sum = sums_calculate(df_column)

    if column_name in ['missing_diff', 'LINE_MISSED']:
        return {
            'total': total,
            'lost_coverage_lines': positive_sum,
            'improve_coverage_lines': negative_sum
        }
    else:  # statements_diff, LINE_COVERED
        return {
            'total': total,
            'lost_coverage_lines': negative_sum,
            'improve_coverage_lines': positive_sum
        }
