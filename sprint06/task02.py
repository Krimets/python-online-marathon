import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def parse_user(output_file, *input_files):
    new_data = []
    keywords = []
    for file in input_files:
        try:
            with open(file) as f:
                data = json.load(f)
                for _ in data:
                    for key in _:
                        if _[key] in keywords:
                            break
                        else:
                            if key == 'name':
                                keywords.append(_[key])
                                new_data.append(_)
        except:
            logging.error(f"File {file} doesn't exist")
    with open(output_file, 'w') as f2:
        json.dump(new_data, f2, indent=4)
