from os import listdir


def open_file_in_dict(directory):
    file_text = {}
    counter_file_text = {}
    for file in directory:
        with open(f'sorted/{file}', "r", encoding="utf-8") as f:
            file_text[file] = f.readlines()
        counter_file_text[len(file_text[file])] = file_text.copy()
        file_text.clear()
    return counter_file_text


def sorting_files(directory):
    files_catalog = open_file_in_dict(directory)
    sorted_tuple = sorted(files_catalog.items(), key=lambda x: x[0])
    return dict(sorted_tuple)


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
