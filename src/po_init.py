import os
import sys

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)

def main():
    if len(sys.argv) < 4:
        print("Usage: po init <project_name>")
        return

    # Adjust arguments when running directly with Python
    if sys.argv[1] == "po_init.py":
        command = "po"
        action = sys.argv[1]
        project_name = sys.argv[2]
    else:
        command = sys.argv[1]
        action = sys.argv[2]
        project_name = sys.argv[3]

    if command == "po" and action == "init":
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
        print("Invalid command.")

if __name__ == "__main__":
    main()
