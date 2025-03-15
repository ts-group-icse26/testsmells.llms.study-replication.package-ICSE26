# modules/extractors/python_extractor.py

import os
import csv
from bs4 import BeautifulSoup

class PythonCoverageExtractor:
    def extract(self, source_path, output_path):
        if not os.path.isdir(source_path):
            raise ValueError(f"Provided source path does not exist or is not a directory: {source_path}")

        for root, _, files in os.walk(source_path):
            for file in files:
                if file.endswith(".csv"):
                    full_path = os.path.join(root, file)
                    print(f"[INFO] Parsing HTML file: {full_path}")
                    parsed_data = self._parse_html(full_path)

                    if parsed_data:
                        # Gera caminho relativo e constrói estrutura de saída
                        relative_path = os.path.relpath(root, source_path)
                        output_dir = os.path.join(output_path, relative_path)
                        os.makedirs(output_dir, exist_ok=True)

                        file_name = os.path.splitext(file)[0] + ".csv"
                        output_file = os.path.join(output_dir, file_name)
                        self._write_csv(parsed_data, output_file)

    def _parse_html(self, html_path):
        try:
            with open(html_path, "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file, "csv.parser")

            table = soup.find("table")
            if not table:
                print(f"[WARN] No table found in {html_path}")
                return None

            headers = [th.text.strip() for th in table.find_all("th")]
            rows = []

            for tr in table.find_all("tr")[1:]:  # Skip header row
                cols = [td.text.strip() for td in tr.find_all("td")]
                if cols:
                    rows.append(cols)

            return [headers] + rows

        except Exception as e:
            print(f"[ERROR] Failed to parse {html_path}: {e}")
            return None


    def _write_csv(self, data, output_file):
        try:
            with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(data)
            print(f"[INFO] CSV written to {output_file}")
        except Exception as e:
            print(f"[ERROR] Failed to write CSV {output_file}: {e}")
