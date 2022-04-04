import shutil
import json
import os

from src.CommandLine import CommandLine
from src.ReplaceText import ReplaceText
from src.CheckPathIsValid import CheckPathIsValid

# Execute command-line
params = CommandLine.execute()

# Convert values to json
params = json.loads(params)

# Get absolute project path
absPath = os.path.dirname(__file__)+'/src/templates'

# Transform string in CammelCase
componentName = params["name"][0].upper() + params["name"][1:]

# Check path is correct
CheckPathIsValid.execute(params["path"])

# Create files and folder structure
try:
  shutil.copytree(absPath, './components/Tester')
except:
  print('Somenthing went wrong')
  exit()
  
# ReplaceText(params["path"]+componentName+'/index.tsx', "{{ComponentName}}", componentName)
# shutil.copyfile('/src/templates/styles.template', os.path.dirname(args["path"]))
# shutil.copyfile('/src/templates/test.template', os.path.dirname(args["path"]))