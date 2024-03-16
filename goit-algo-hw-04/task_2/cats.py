def get_cats_info(path) -> list:                                                    # creating function for path
    try:
        with open('cats_file.txt', 'r') as file:                                    # open 'cats_file.txt' in read mode
            list = [el.strip() for el in file.readlines()]                          # making a list without '\n' symbol
            sep_list = [el.split(',') for el in list]                               # making a list of lists with separation for elements by ','
            cats_info = []
            for el in sep_list:
                dict_cat = {'id': el.pop(0), 'name': el.pop(0), 'age': el.pop(0)}   # making a list of dictionaries with information for cats
                cats_info.append(dict_cat)
            return cats_info
    except FileNotFoundError:
        return print('File not found!')                                             # making an exception for function if file was not found

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)

