from test_kadr_hotels_page import *
import os
from glob import *
import asttokens, ast


def find_function_name(file_path, page_link):
    
    all_test_case = []
    for module in glob(file_path):
        tree = ast.parse(open(module, "rt").read(), filename=module)
        for item in [x.name for x in ast.walk(tree) if isinstance(x, ast.FunctionDef)]:
            if item is not None:
                all_test_case.append(str(item + "('{}')".format(page_link)))
        return all_test_case

         

def get_input_case_name(page_link, input_file_name):
    input_file_name = str(input_file_name).replace("'" , "").replace("'", "")
    input_file_name = str(input_file_name).replace("[" , "").replace("]", "")
    file_name = "test_kadr_hotels_page.py"
    if input_file_name in file_name:
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),  "{}".format(input_file_name))
        all_function_name_list = find_function_name(file_path, page_link)
        return all_function_name_list

    else:
        all_test_folder_path =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_kadr_hotels_page.py")
        function_name_list = find_function_name(all_test_folder_path, page_link)
        return function_name_list

def test_runner(page_link, input_file_name):
    test_folder_path = "/home/erida-employee/Desktop/ssh/page_class/Kadr_POM_Model/test_kadr_hotels_page.py"
    case_name = get_input_case_name(page_link, input_file_name)
    for i in input_file_name:
        serch_test = i + "('{}')".format(page_link)
        try:
            if serch_test in case_name:
                eval(serch_test)
        except TypeError:
            print("This test name is not found: ")

def run_all_test_case(input_file_name, page_link):
    run_case_name = get_input_case_name(page_link, input_file_name)
    for test in run_case_name:
        eval(test)

def main():    
    get_path("/home/erida-employee/Desktop/ssh/page_class/Kadr_POM_Model/Test")
    page_link = get_page_link()
    input_file_name = input("Enter name of input file: ")
    input_file_name = input_file_name.split()
    file_name = "test_kadr_hotels_page.py"
    if file_name in input_file_name:
        run_all_test_case(input_file_name, page_link)
    else:
        test_runner(page_link, input_file_name)


if __name__ == '__main__':
    main()


