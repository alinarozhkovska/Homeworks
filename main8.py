import os


folder_name = input()

def get_directory_info(folder_name):
    result_dict = {}
        
    result_dict[folder_name] = []
    result_dict["dirnames"] = []

    for item in os.listdir(folder_name):
        item_path = os.path.join(folder_name, item)
        if os.path.isfile(item_path):
            result_dict[folder_name].append(item)        
        elif os.path.isdir(item_path):
            result_dict["dirnames"].append(item)  
    return result_dict


def sort_dict(result_dict, reverse=False):
    for key_name, contents in directory_info.items():       
        result_dict[key_name] = sorted(contents, reverse=reverse)
    return result_dict



def add_item_to_dict(result_dict, item):
    if "." in item:
        result_dict[folder_name].append(item)         
    else:
        result_dict["dirnames"].append(item)
    return result_dict



def folder_check(result_dict, folder_name):
    
    for item in result_dict["dirnames"]:
        if not os.path.exists(folder_name + '/' + item):
            os.makedirs(folder_name + '/' + item)
   
    for item in result_dict[folder_name]:
        if not os.path.exists(folder_name + '/' + item):
            item_path = os.path.join(folder_name, item)
            open(item_path, 'w').close()
        


    


directory_info = get_directory_info(folder_name)
directory_info = sort_dict(directory_info, reverse=True)
directory_info = add_item_to_dict(directory_info, 'file.txt')
directory_info = add_item_to_dict(directory_info, 'folder')
folder_check(directory_info, folder_name)

print(directory_info)



















