from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import json

class CommandLine:

    def execute():
        parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
        parser.add_argument("-c", "--component", default="y",
                            help="Create component [y = yes / n = no]")
        parser.add_argument("-t", "--test", default="y",
                            help="Create test component [y = yes / n = no]")
        parser.add_argument("-s", "--style", default="y",
                            help="Create styled-component [y = yes / n = no]")
        parser.add_argument("-n", "--name", default="componentName",
                            help="Component name <nameForComponent>")
        parser.add_argument("-p", "--path", default="./",
                            help="Add other path, ex.: ./src/components/")
        args = vars(parser.parse_args())

        # Create JSON Object
        returnValue = {
          "component": args["component"],
          "test": args["test"],
          "style": args["style"],
          "name": args["name"],
          "path": args["path"]
        }

        return json.dumps(returnValue)
