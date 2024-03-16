def total_salary(path) -> tuple:
    try:
        with open("salary_file.txt", 'r') as file:                                          # open "salary_file.txt" in read mode
            text = file.readlines()                                                         # converting file content in list for future processing
            worker_salary = [el.strip() for el in text]                                     # removing el "\n" from list
            name_salary = [el.split(',') for el in worker_salary]                           # spliting elements in list by ','
            name_salary_list = [el for element in name_salary for el in element]            # unpacking lists from list into one list
            salary_number_list = []
            for el in name_salary_list:
                try:                                                                        # converting str -> int and adding elements to a new list with exception if operation could not be proceeded
                    salary_number = int(el)
                    salary_number_list.append(salary_number)
                except ValueError:
                    pass
            total = sum(salary_number_list)                                                 # totsl sum of salary
            average_salary = total//len(salary_number_list)                                 # equation for determining average salary
        return print(f'Total sum of salary: {total}\nAverage salary: {average_salary}')
    except FileNotFoundError:                                                               # exception for function if file was not found
        return print('File not found')

total_salary("path/to/salary.txt")
