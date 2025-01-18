import os
from typing import List



def format_markdown_table(data: List[dict]):
    from markdown_table_generator import generate_markdown, table_from_string_list
    table = table_from_string_list(data)
    return generate_markdown(table)
    

def format_rdfrules_module_docstring():

    pipeline_file = "src/pyrdfrules/rdfrules/pipeline.py"
    docfile = "src/pyrdfrules/rdfrules/__init__.py"

    def get_pipeline_tasks():
        class_names = [["Operation", "Class"]]

        with open(pipeline_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "class" in line and "RDFRulesTaskModel" in line:
                    class_name = line.split(" ")[1].split("(")[0]
                    
                    if class_name == "RDFRulesTaskModel": # skip the base class
                        continue
                    
                    if class_name == "ArbitraryPipelineTask":
                        class_names.append(["ArbitraryPipelineTask", f"pyrdfrules.rdfrules.pipeline.{class_name}()"])
                        continue
                    
                    # camel case to slug
                    slug_name = ''.join([f"-{i.lower()}" if i.isupper() else i for i in class_name]).lstrip("-")
                    
                    link = "https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#{0}".format(slug_name)
                    
                    markdown_link = f"[{class_name}]({link})"
                    
                    class_names.append([markdown_link, f"pyrdfrules.rdfrules.pipeline.{class_name}()"])
                    

        return class_names
    
    docstring_rdfrules = ""
    
    with open(docfile, "r") as f:
        lines = f.read()
        print(lines)
        
        start = lines.find("<!--- AUTOMATICALLY GENERATE DOC --->") + 37
        end = lines.find("<!--- END AUTOMATICALLY GENERATE DOC --->")
        
        print(start, end)
        
        first_part = lines[:start]
        second_part = lines[end:]
        
        lines = first_part + "\n" + format_markdown_table(get_pipeline_tasks()) + "\n" + second_part
        
        docstring_rdfrules = lines
        
    print(docstring_rdfrules)        
        
    with open(docfile, "w") as f:
        f.write(docstring_rdfrules)
        
        
format_rdfrules_module_docstring()        