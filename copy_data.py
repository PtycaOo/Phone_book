from return_data_file import data_file
from print_data import print_file
from choice_file import choice_number_file


def copy_data():
    data_1,nf_1 = data_file()
    data_length = len(data_1)
    if data_length == 0:
        print("Из файла нечего копировать!")
    else:
        input_user = int(input("Введите номер строки\n" 
                              f"от 1 до {data_length}: "))
        while input_user < 1 or input_user > data_length:
            input_user = int(input("Введите номер строки \n" 
                                   f"от 1 до {data_length}: "))
        print()
        print("Куда будем копировать?")    
        data_2,nf_2 = data_file()
        data_2_length = len(data_2)
        data_1 = [f'{data_2_length + 1};{data_1[input_user - 1].split(";")[1]};'
                f'{data_1[input_user - 1].split(";")[2]};'
                f'{data_1[input_user - 1].split(";")[3]};'
                f'{data_1[input_user - 1].split(";")[4]}']
        final_string = ";".join(data_1)
        with open(f'db/data_{nf_2}.txt', 'a', encoding='utf-8') as file:
            file.write(final_string)
    print("Данные успешно скопированы!\n")
            
    




