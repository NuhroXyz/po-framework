import sys

# init
# //////////////////////////////////////////////////////////////
import json
import os
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"init_schema.json"),'r')
schema = json.loads(file.read())
file.close()

def create_content(str):
    return str

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)

def create_paths(dir_name,dic,tmpStr):
    tmpStr = tmpStr + "  "

    os.makedirs(dir_name, exist_ok=True)
    # print(tmpStr + "")
    print(tmpStr  + " " + dir_name.split("\\")[-1:][0] + "/")

    for i in dic:
        if( isinstance(dic[i], dict)):
            create_paths(os.path.join(dir_name,i),dic[i],tmpStr)
        else:
            # print(tmpStr + "  |")
            print(tmpStr + "  " + " " + i)
            create_file(os.path.join(dir_name, i))

def init():
        project_name = sys.argv[2]
        if not os.path.exists(project_name):
            create_paths(project_name,schema," ")
# ///////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////
def help():
    print("HELP!")