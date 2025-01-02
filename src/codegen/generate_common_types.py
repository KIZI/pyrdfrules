#!/usr/bin/python

import os
import re

task_classes_scala = []

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("./src/rdfrules_source/http/src/main/scala/com/github/propi/rdfrules/http/formats"):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    
    blocks = []
    current_block = []
    in_block = False
    
    for file in files:
        print(len(path) * '---', file)
        
        with open(root + "/" + file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "implicit val" in line:
                    task_classes_scala.append(line)
                    in_block = True
                    
                if in_block:
                    current_block.append(line)
                    
                if in_block and "}" in line:
                    blocks.append(current_block)
                    current_block = []
                    in_block = False                    