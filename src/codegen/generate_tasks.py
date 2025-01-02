#!/usr/bin/python

import os
import re

task_classes_scala = []

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("./src/rdfrules_source/http/src/main/scala/com/github/propi/rdfrules/http/task"):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    
    for file in files:
        print(len(path) * '---', file)
        
        with open(root + "/" + file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "class" in line:
                    if "abstract" in line:
                        break
                    
                    if "extends Task" not in line:
                        break
                    
                    task_classes_scala.append(line)
                    break

print(task_classes_scala)

python_class_template = """
class {class_name}({base_class_name}):
    {parameters}
"""

# Updated regex to capture class name, parameters, and types it extends
regex = r"class (\w+)(\(([^)]*)\))?"

python_classes = []

for scala_class in task_classes_scala:
    matches = re.search(regex, scala_class)
    
    if matches:
        class_name = matches.group(1)
        parameters = matches.group(3)  # This will be None if there are no parameters
        
        print(f"Class: {class_name}")
        print(f"Parameters: {parameters}")
        print()
        
        params = []
        
        if parameters is not None and parameters.strip() != "":
            if "String" in parameters:
                parameters = parameters.replace("String", "str")
                
            if "Option" in parameters:
                parameters = parameters.replace("Option[", "Optional[")
                
            if "Integer" in parameters:
                parameters = parameters.replace("Integer", "int")
                
            if "Int" in parameters:
                parameters = parameters.replace("Int", "int")
            
            if "Double" in parameters:
                parameters = parameters.replace("Double", "float")
            
            if "Boolean" in parameters:
                parameters = parameters.replace("Boolean", "bool")
                
            if "TripleItem.Uri" in parameters:
                parameters = parameters.replace("TripleItem.Uri", "AnyUrl")

            if "URL" in parameters:
                parameters = parameters.replace("URL", "AnyUrl")              
                
            if "Seq" in parameters:
                parameters = parameters.replace("Seq", "List")
                
            if "implicit debugger: Debugger" in parameters:
                parameters = parameters.replace("implicit debugger: Debugger", "")
            
            params = parameters.split(", ")
            
            
        else:
            params = ["pass"]

        python_classes.append(python_class_template.format(class_name=class_name, base_class_name="BaseObject", parameters="\n    ".join(params)))

python_module_template = """
from __future__ import annotations

from enum import Enum
from typing import List, Literal, Optional, Union, Set

from pydantic import AnyUrl, BaseModel, ConfigDict, Field, RootModel

class BaseObject(BaseModel):
    pass

{python_classes}
"""

with open("src/codegen/generated_tasks.py", "w") as f:
    f.write(python_module_template.format(python_classes="\n".join(python_classes)))