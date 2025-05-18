import os
from pathlib import Path

package_name="chatbot_theme_identifier"

list_of_files=[
    
    f"{package_name}/__init__.py",
    f"{package_name}/backend/__init__.py",
    f"{package_name}/backend/app/api.py",
    f"{package_name}/backend/app/core.py",
    f"{package_name}/backend/app/models.py",
    f"{package_name}/backend/app/service.py",
    f"{package_name}/backend/app/main.py",
    f"{package_name}/backend/app/config.py",
    f"{package_name}/backend/data",
    f"{package_name}/logger.py",
    f"{package_name}/exception.py",
   
    "Dockerfile",
    "Readme.md",
    "requirements.txt",
    "setup.py",
    "init_setup.sh",
]


# here will create a directory

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")

# here will use the file handling
