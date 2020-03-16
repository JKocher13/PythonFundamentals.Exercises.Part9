import json
import os
import pickle

def read_json(path):
    file_name = path
    with open(file_name) as f:
        data = json.loads(f)
    return data


def read_all_json_files(json_root):
	for root, _, files in os.walk(json_root):
		result = []
		for f in files:
			if f.endswith('.json'):
				json_content = read_json(os.path.join(json_root, f))
				result.append(json_content)
	return result


def write_pickle(file_path, data):
	with open(file_path, "wb") as handler:
		pickle.dump(data, handler)


def load_pickle(file_path):
	with open(file_path, 'rb') as handler:
		data = pickle.load(handler)
	return data




