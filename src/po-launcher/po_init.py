import os
import sys

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)

def main():
    if len(sys.argv) < 3:
        print("Usage: po init <project_name>")
        return

    # Extract the command and arguments
    command = sys.argv[0]  # This should be the script name, e.g., 'po_init.py'
    action = sys.argv[1]   # This should be 'init'
    project_name = sys.argv[2]  # This should be the project name

    if command.endswith('po_init.py') and action == "init" and project_name:
        if not os.path.exists(project_name):
            os.makedirs(project_name)

            # Create src directory and files
            src_path = os.path.join(project_name, "src")
            os.makedirs(src_path)
            create_file(os.path.join(src_path, "main.po"))
            create_file(os.path.join(src_path, "styles.po"))

            # Create components directory and MyComponent.po
            components_path = os.path.join(src_path, "components")
            os.makedirs(components_path)
            create_file(os.path.join(components_path, "MyComponent.po"))

            # Create dist directory and files
            dist_path = os.path.join(project_name, "dist")
            os.makedirs(dist_path)
            create_file(os.path.join(dist_path, "index.html"))
            create_file(os.path.join(dist_path, "styles.css"))
            create_file(os.path.join(dist_path, "scripts.js"))

            # Create the config file and README
            create_file(os.path.join(project_name, "po.config.js"))
            create_file(os.path.join(project_name, "README.md"))

            print(f"Project {project_name} initialized with the necessary structure.")
        else:
            print(f"Project {project_name} already exists.")
    else:
        print("Invalid command or missing arguments.")

if __name__ == "__main__":
    main()
