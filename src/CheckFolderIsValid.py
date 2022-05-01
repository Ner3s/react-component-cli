class CheckFolderIsValid:
    def execute(pathWithFolder):
    # Check if the folder can be created
      if pathWithFolder:
        print("The folder is not valid :'(")
        exit()
      else: 
        print("The folder is valid :D")
