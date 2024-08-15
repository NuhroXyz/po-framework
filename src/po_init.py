import sys
import commands


def main():

    if sys.argv[1] == "po_init.py":
        command = "po"
        action = sys.argv[1]
    else:
        command = sys.argv[1]
        action = sys.argv[2]

    try:
        func = getattr(commands,action)
        func()
    except:
        print ("invalid command")
    

    # if command == "po" and action == "init":
    #     if not os.path.exists(project_name):
    #         create_paths(project_name,schema," ")
    # else:
        

if __name__ == "__main__":
    main()