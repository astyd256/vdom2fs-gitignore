from __future__ import print_function
import sys, json, os

file_path = "vdom2fs.conf"
type = "simple"

if len(sys.argv) == 2:
    type = sys.argv[1]
elif len(sys.argv) ==3:
    type = sys.argv[1]
    file_path = sys.argv[2]
elif len(sys.argv) > 3:
    print("Wrong number of arguments")
    exit(1)

try:
    with open(file_path, 'r') as file:
        data = json.load(file)

    aliases = data.get('Aliases', {})
    gitignore_entries = []

    if type == "simple":
        for alias, path in aliases.items():
            gitignore_entries.append(os.path.join(path,'/').replace('\\', '/'))
            
    elif type == "meticulous":      
        for alias, path in aliases.items():
            if path != ".":
                if os.path.isdir(path):
                    for root, dirs, files in os.walk(path):
                        if 'Pages' in dirs:
                            gitignore_entries.append(os.path.join(root, 'Pages/').replace('\\', '/'))
                            dirs.remove('Pages')
                        else:
                            for name in files:
                                gitignore_entries.append(os.path.join(root, name).replace('\\', '/'))
                else:
                    print("Path for alias '{}' is not a directory: {}".format(alias, path))

    
    with open('.gitignore', 'a') as file:
        file.write("\n".join(gitignore_entries))
    
    result = "Files from aliases paths are successfully written to .gitignore."
    
except Exception as e:
    result = "Error: {}".format(e)

print(result)
