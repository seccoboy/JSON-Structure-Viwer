import os
import json
import argparse
from glob import glob

def get_unique_structure(data, parent_keys=None, processed=None, output_file=None):
    """
    Recursively display the unique structure of the JSON, avoiding repetitions.
    """
    if parent_keys is None:
        parent_keys = []
    if processed is None:
        processed = set()  # Keep track of already seen paths to avoid repetitions

    indent = '    ' * len(parent_keys)
    
    if isinstance(data, dict):
        for key, value in data.items():
            # Create a tuple representing the full path to this key
            path_tuple = tuple(parent_keys + [key])
            if path_tuple not in processed:
                if isinstance(value, (str, int, float, bool, type(None))):
                    # Print key and type on the same line
                    value_type = type(value).__name__
                    print(f"{indent}{key} - ({value_type})", file=output_file)
                elif isinstance(value, list):
                    # Print key and "- (array)" on the same line
                    print(f"{indent}{key} - (array)", file=output_file)
                    processed.add(path_tuple)
                    # Process the first element of the list
                    if value:
                        get_unique_structure(value[0], parent_keys + [key], processed, output_file)
                        # Indicate if there are more elements
                        if len(value) > 1:
                            more_elements_tuple = path_tuple + ('... (more elements)',)
                            if more_elements_tuple not in processed:
                                indent_more = '    ' * (len(parent_keys) + 1)
                                #print(f"{indent_more}... (more elements)", file=output_file)
                                processed.add(more_elements_tuple)
                else:
                    # It's a dictionary, print key and recurse
                    print(f"{indent}{key} - (object)", file=output_file)
                    processed.add(path_tuple)
                    get_unique_structure(value, parent_keys + [key], processed, output_file)
    elif isinstance(data, list):
        # Use parent key
        key_path = tuple(parent_keys)
        if key_path and key_path not in processed:
            key_name = parent_keys[-1]
            print(f"{indent}{key_name} - (array)", file=output_file)
            processed.add(key_path)
        if data:
            get_unique_structure(data[0], parent_keys, processed, output_file)
            # Indicate if there are more elements
            if len(data) > 1:
                more_elements_tuple = key_path + ('... (more elements)',)
                if more_elements_tuple not in processed:
                    indent_more = '    ' * len(parent_keys)
                    #print(f"{indent_more}... (more elements)", file=output_file)
                    processed.add(more_elements_tuple)
    elif isinstance(data, (str, int, float, bool, type(None))):
        # For primitives under a list or at the root
        path_tuple = tuple(parent_keys)
        if path_tuple not in processed:
            value_type = type(data).__name__
            print(f"{indent}- ({value_type})", file=output_file)
            processed.add(path_tuple)
    else:
        # Handle other data types if necessary
        pass

def process_files(file_paths):
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            input_json = json.load(file)
            output_filename = f"estrutura_{os.path.splitext(os.path.basename(file_path))[0]}.txt"
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                print(f"Processing file: {file_path}", file=output_file)
                get_unique_structure(input_json, parent_keys=[], processed=set(), output_file=output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process JSON files to display their unique structure.')
    parser.add_argument('json_path', nargs='?', default='*.json',
                        help='Path to a JSON file or folder containing JSON files')
    args = parser.parse_args()

    if os.path.isdir(args.json_path):
        file_paths = glob(os.path.join(args.json_path, '*.json'))
    else:
        file_paths = glob(args.json_path)

    process_files(file_paths)
