import os
import shutil

class JavaCoverageExtractor:
    def extract(self, source_path, output_path):
        if not os.path.isdir(source_path):
            raise ValueError(f"Provided source path does not exist or is not a directory: {source_path}")

        for root, _, files in os.walk(source_path):
            for file in files:
                if file.endswith(".csv"):
                    full_input_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_input_path, source_path)
                    full_output_path = os.path.join(output_path, relative_path)

                    os.makedirs(os.path.dirname(full_output_path), exist_ok=True)
                    print(f"[INFO] Copying CSV file: {full_input_path} -> {full_output_path}")

                    try:
                        shutil.copy2(full_input_path, full_output_path)
                    except Exception as e:
                        print(f"[ERROR] Failed to copy {full_input_path} to {full_output_path}: {e}")
