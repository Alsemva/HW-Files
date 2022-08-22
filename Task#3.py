from os import listdir


def open_file_in_dict(directory):
    files_catalog = {}
    for file in directory:
        with open(f'sorted/{file}', "r", encoding="utf-8") as f:
            files_catalog[file] = f.readlines()
    return files_catalog


def sorting_files(directory):
    files_catalog = open_file_in_dict(directory)
    sort_list_files = {}
    print(sort_list_files)
    max = 0
    for file, text in files_catalog.items():
        print(file)
        print(len(text))
        sort_list_files[len(text)] = {file: text}
    sorted_tuple = sorted(sort_list_files.items(), key=lambda x: x[0])
    print(dict(sorted_tuple))
    return  dict(sorted_tuple)


def merging_files(directory):
    sorted_files = sorting_files(directory)
    with open('output.txt', "w", encoding="utf-8") as f:
        for counter, file in sorted_files.items():
            for name_file, text in file.items():
                f.write(f'{name_file}\n')
                f.write(f'{counter}\n')
                f.writelines(text)
                f.write('\n')
    return 'Sorted'

print(merging_files(listdir('sorted')))
