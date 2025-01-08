
[![PyPI - Version](https://img.shields.io/pypi/v/pyrdfrules.svg)](https://pypi.org/project/pyrdfrules)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyrdfrules.svg)](https://pypi.org/project/pyrdfrules)

<p align="center">
  <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg">
</p>

<h1 align="center">
PyRDFRules
</h1>

<p align="center">
  <a href="https://github.com/propi/rdfrules">
    RDFRules
  </a>
  •
  <a href="https://kizi.github.io/pyrdfrules/pyrdfrules.html">
    Documentation
  </a>
  •
  <a href="https://www.vse.cz/">
   VŠE
  </a>
</p>

-----

**Table of Contents**

- [PyRDFRules](#pyrdfrules)
  - [RDFRules](#rdfrules)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Remote instance](#remote-instance)
    - [Local instance](#local-instance)
    - [Run a task](#run-a-task)
- [Developing](#developing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## PyRDFRules

PyRDFRules is a Python wrapper for the graph rule mining tool RDFRules.

### RDFRules

> RDFRules is a powerful analytical tool for rule mining from RDF knowledge graphs. It offers a complex rule mining solution including RDF data pre-processing, rules post-processing and prediction abilities from rules. The core of RDFRules is written in the Scala language. Besides the Scala API, RDFRules also provides REST web service with graphical user interface via a web browser.

Repository for RDFRules can be found at [propi/rdfrules](https://github.com/propi/rdfrules).

## Getting started

PyRDFRules is distributed as a Python library through PyPi. The primary goal of this API is to faciliate the easy use of RDFRules through a Python interface.

### Prerequisites

A minimum Python version of `3.12.2` is required. You can check your Python version using `python --version`.

### Installation

```console
pip install pyrdfrules
```

### Usage

Full documentation is available at [a dedicated documentation site](https://kizi.github.io/pyrdfrules/pyrdfrules.html). Code samples can be found in the sample directory, including a Python notebook.

Currently, using a remote HTTP instance of RDFRules or a local instance of RDFRules is supported. Automatic installation of JVM if not present and of RDFRules is supported, and the library takes care of running the RDFRules application.

#### Remote instance

To connect to a remote instance of RDFRules, create an application and use the start_remote method.

```python
from pydantic_core import Url

import pyrdfrules.application

app = pyrdfrules.application.Application()

rdfrules = await app.start_remote(
    url = Url("http://YOUR_RDFRULES_INSTANCE/api/")
)
```

#### Local instance

To set up a local instance of PyRDFRules

```python
# Recommended: Configure your workspace directory.

config = Config(
    workspace_path=os.path.realpath("YOUR_WORKSPACE_DIRECTORY")
)

app = pyrdfrules.application.Application()
        
app.start_local(
    install_jvm = True, # If you wish for Python to install JVM for you, set to true.
    install_rdfrules = True, # If you wish for Python to install RDFRules, set to true.
    rdfrules_path = "...", # Installation path for RDFRules. If you set install_rdfrules to False, it will expect RDFRule to be installed in this location.
    jvm_path = "", # Installation path for the JVM.
    config = config
)
```

As a last step, launch the pipeline, wait for all results and print the head, body and measures of each mined rule.

#### Run a task

A task is a series of steps (a pipeline) provided to RDFRules. Tasks are used to mine rules, index, cache or otherwise manipulate data...

If you have a JSON task ready, you can execute it in the following way:

```python
from pyrdfrules.common.task.task import Task

task : Task = None

with open("./task.json", "r") as file:        
    task_json_from_file = file.read()
    task = rdfrules.task.create_task_from_string(task_json_from_file)
```

You can also specify the pipeline in code.

```python

pipeline = Pipeline(
    tasks=[
        LoadGraph(
            graphName = "<dbpedia>",
            path = "/dbpedia_yago/mappingbased_objects_sample.ttl"
        ),
        ... # your other tasks go here
        GetRules()
    ]
)

task = self.rdfrules.task.create_task(pipeline)
    
for step in self.rdfrules.task.run_task(task):
      print(step)
  
print(task.result) # access task result dictionary - pure output from RDFRules
print(task.get_result()) # returns formatted outputs
```

Task execution is non blocking and you can stop it, as long as it is not finished in RDFRules.

Full pipeline sample matching the DBpedia & YAGO example from the RDFRules web instance can be found in documentation [doc](https://kizi.github.io/pyrdfrules/pyrdfrules.html), or in `src/tests/test_pipeline.py`.

## Developing

To initialize your environment:

```console
./init.sh
```

To run a build and run jupyter lab:

```console
./run.sh
```

## Roadmap

- [x] Sample interface
- [x] Implement JSON serialization of pipeline
- [x] Implement communication with RDFRules

## Contributing

If you have a suggestion to improve this project, please fork the repo and create a pull request. If you encounter any issues, please do raise an [issue](https://github.com/KIZI/pyrdfrules/issues) with an appropriate tag. Feature requests, enhancements and bug reports are welcome.

To contribute to this project, first:

- Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request

## License

`pyrdfrules` is distributed under the terms of the Apache License. See `LICENSE` for more information.

## Acknowledgments
* [RDFRules@propi/rdfrules](https://github.com/propi/rdfrules)
* [VŠE](https://www.vse.cz/)