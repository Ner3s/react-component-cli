import shutil
import json
import os

from src.CommandLine import CommandLine
from src.ReplaceText import ReplaceText
from src.CheckPathIsValid import CheckPathIsValid
from src.CheckFolderIsValid import CheckFolderIsValid

# Execute command-line
params = CommandLine.execute()

# Convert values to json
params = json.loads(params)

# Get absolute project path
absPath = os.path.dirname(__file__)+'/src/templates'

# All files types
allFiles = ['index.tsx', 'styles.ts', 'test.tsx']

# Transform string in CammelCase
componentName = params["name"][0].upper() + params["name"][1:]

# Check folder valid
CheckFolderIsValid.execute(os.path.isdir(params["path"]+componentName))

# Check path is correct
CheckPathIsValid.execute(params["path"])

# Create files and folder structure
try:
    shutil.copytree(absPath, params["path"]+componentName)
except:
    print('Somenthing went wrong')
    exit()

# Replace {{ComponentName}} to ComponentName of the CLI
for index, fileName in enumerate(allFiles):
    ReplaceText(params["path"]+componentName+'/'+fileName,
                "{{ComponentName}}", componentName)

# Get all file should delete
deleteFiles = [params["component"][0].lower() == 'n' and 'index.tsx', params["style"][0].lower(
) == 'n' and 'styles.ts', params["test"][0].lower() == 'n' and 'test.tsx']

# Iterate and delete file
for index, fileName in enumerate(deleteFiles):
  if(fileName):
    os.remove('./'+componentName+'/'+fileName)

print('Component created! =D')
