import json
import os
import pickle

def read_json(path):
    file_name = path
    with open(file_name,r) as f:
        data = json.loads(f)
    return data

 def read_all_json_files(path):
 	all_files =[]
 	for x in os.listdir(path):
 		indiv_path=os.path(x)
 		y = read_json(indiv_path)
 		all_files.append(y)
 	return all_files


 def write_pickle(path, data):
 	path = os.path.join(path,super_smash_characters.pickle)
 	pick_dump(data , path)

 def load_pickle(path):
 	return pickle.loads(path)






read_json("/Users/jkocher/Documents/PythonProjects/PythonFundamentals.Exercises.Part9/data/super_smash_bros/link.json")

read_all_json_files("/Users/jkocher/Documents/PythonProjects/PythonFundamentals.Exercises.Part9/data/super_smash_bros")