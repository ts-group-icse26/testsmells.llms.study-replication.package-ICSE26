import os


def get_original_project_sum(ask_user=True):

    if ask_user:
        original_file_sum = input("Get original project sum? (y/n)\n")
        return original_file_sum.lower() == 'y'
    return False  # Retorna False se não for para perguntar ao usuário


def list_folders_to_menu(root, word):

    folders = [f for f in os.listdir(root) if os.path.isdir(os.path.join(root, f))
               and not f.startswith('.')
               and not f.startswith('_')]
    print('\n')

    for i, pastas in enumerate(folders):
        print('{} - {}'.format(i, pastas))

    folder = int(input(f'\nWhich {word} do you want to do with?\n'))
    return os.path.join(root, folders[folder])


def list_files_2_menu(root, word):
    files = [f for f in os.listdir(root) if not os.path.isdir(os.path.join(root, f))
             and not f.startswith('.')
             and not f.startswith('_')]

    print('\n')
    for i, file in enumerate(files):
        print(f'{i} - {file}')
    choice = int(input(f'\nWhich {word} do you want to do with?\n'))
    return os.path.join(root, files[choice])