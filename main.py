from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os
import shutil
import warnings
warnings.simplefilter("ignore")

from src.component import Component

# test = Component('teste')
# test.execute()

# Parse command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-c", "--component", default="y", help="Create component [y = yes / n = no]")
parser.add_argument("-t", "--test", default="y", help="Create test component [y = yes / n = no]")
parser.add_argument("-s", "--style", default="y", help="Create styled-component [y = yes / n = no]")
parser.add_argument("-n", "--name", default="componentName", help="Component name <nameForComponent>")
parser.add_argument("-p", "--path", default="./", help="Add other path, ex.: ./src/components/")
args = vars(parser.parse_args())

# print(args["component"])
# print(args["test"])
# print(args["style"])
# print(args["name"])
# print(args["path"])

# os.makedirs(os.path.dirname(args["path"]), exist_ok=True)
# with open(args["path"]+args["name"], "w"):
#   print("created "+args["path"]+args["name"])


shutil.copytree('src/templates', './'+args["name"])
# shutil.copyfile('/src/templates/styles.template', os.path.dirname(args["path"]))
# shutil.copyfile('/src/templates/test.template', os.path.dirname(args["path"]))