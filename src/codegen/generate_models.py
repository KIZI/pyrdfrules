import os
import re

scala_file_path = "./src/rdfrules_source/http/src/main/scala/com/github/propi/rdfrules/http/formats/PipelineJsonReaders.scala"
output_file_path = "./src/codegen/generated_pydantic_classes.py"

# Read the Scala file
with open(scala_file_path, 'r') as file:
    scala_content = file.read()

# Regex to capture class definitions and their parameters
class_regex = re.compile(r"implicit def (\w+Reader)\(.*\): RootJsonReader\[(\w+)\] = \(json: JsValue\) => \{\s+val fields = json.asJsObject.fields\s+new (\w+)\(([^)]*)\)", re.MULTILINE)

print(f"Reading Scala file {scala_file_path}")

# Extract class definitions and their parameters
matches = class_regex.findall(scala_content)

# Template for Pydantic class definitions
pydantic_class_template = """
class {class_name}(BaseModel):
    {parameters}
"""

# Convert Scala types to Python types
type_mapping = {
    "String": "str",
    "Int": "int",
    "Double": "float",
    "Boolean": "bool",
    "Seq": "List",
    "Option": "Optional",
    "URL": "AnyUrl",
    "TripleItem.Uri": "AnyUrl"
}

# Generate Pydantic class definitions
pydantic_classes = []

for match in matches:
    reader_name, scala_class_name, class_name, params = match
    
    # Convert parameters to Python types
    param_list = []
    if params:
        param_pairs = params.split(", ")
        for param in param_pairs:
            param_name, param_type = param.split(": ")
            param_type = type_mapping.get(param_type, param_type)
            param_list.append(f"{param_name}: {param_type}")
    
    parameters = "\n    ".join(param_list) if param_list else "pass"
    
    pydantic_class = pydantic_class_template.format(class_name=class_name, parameters=parameters)
    pydantic_classes.append(pydantic_class)

# Template for the Python module
python_module_template = """
from __future__ import annotations

from typing import List, Optional
from pydantic import AnyUrl, BaseModel

{pydantic_classes}
"""

# Write the generated Pydantic classes to the output file
with open(output_file_path, 'w') as file:
    file.write(python_module_template.format(pydantic_classes="\n".join(pydantic_classes)))

print(f"Pydantic classes generated and written to {output_file_path}")