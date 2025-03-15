# # coverage_tool/cli/generate_reports.py
# import argparse
# from coverage_tool.modules.extractors import extract_python_reports
# from coverage_tool.modules.extractors import extract_java_reports
#
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--lang', choices=['python', 'java'], required=True)
#     parser.add_argument('--source_path', required=True)
#     parser.add_argument('--output_path', required=True)
#     args = parser.parse_args()
#
#     if args.lang == 'python':
#         extract_python_reports(args.source_path, args.output_path)
#     elif args.lang == 'java':
#         extract_java_reports(args.source_path, args.output_path)
#
# if __name__ == '__main__':
#     main()
