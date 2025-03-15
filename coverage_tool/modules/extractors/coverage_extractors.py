# modules/extractors/coverage_extractors.py

import os
from .java_extractor import JavaCoverageExtractor
from .python_extractor import PythonCoverageExtractor


def list_datasets_files(language, dataset_abs_path):
    original_files = os.listdir(os.path.join(language, dataset_abs_path))
    return original_files

def extract_coverage(language, source_path, output_path):
    if language == "java":
        extractor = JavaCoverageExtractor()
    elif language == "python":
        extractor = PythonCoverageExtractor()
    else:
        raise ValueError(f"Unsupported language: {language}")

    extractor.extract(source_path, output_path)
