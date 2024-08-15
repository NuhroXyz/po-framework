import sys
import commands


def main():

    if sys.argv[1] == "po_init.py":
        sys.argv = sys.argv[1:]

    
    func = getattr(commands,sys.argv[1])
    func()
    

    # if command == "po" and action == "init":
    #     if not os.path.exists(project_name):
    #         create_paths(project_name,schema," ")
    # else:
        

if __name__ == "__main__":
    main()