
[![PyPI - Version](https://img.shields.io/pypi/v/pyrdfrules.svg)](https://pypi.org/project/pyrdfrules)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyrdfrules.svg)](https://pypi.org/project/pyrdfrules)

<h1 align="center">
PyRDFRules
</h1>

<p align="center">
  <a href="https://github.com/propi/rdfrules">
    RDFRules
  </a>
  •
  <a href="">
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
    - [Local instance](#local-instance)
- [Developing](#developing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## PyRDFRules

PyRDFRules is a Python wrapper for the graph rule mining tool RDFRules.

### RDFRules

> RDFRules is a powerful analytical tool for rule mining from RDF knowledge graphs. It offers a complex rule mining solution including RDF data pre-processing, rules post-processing and prediction abilities from rules. The core of RDFRules is written in the Scala language. Besides the Scala API, RDFRules also provides REST web service with graphical user interface via a web browser.

Repository for RDFRules can be found at [propi/rdfrules](https://github.com/propi/rdfrules). A live demo can be accessed at https://br-dev.lmcloud.vse.cz/rdfrules/.

## Getting started

PyRDFRules is distributed as a Python library through PyPi.

### Prerequisites

A minimum Python version of `3.12.2` is required. You can check your Python version using `python --version`.

### Installation

```console
pip install pyrdfrules
```

### Usage

Full documentation is available at [a dedicated documentation site](#documentation). Code samples can be found in the sample directory, including a Python notebook.

Currently, using a remote HTTP instance of RDFRules and a local instance of RDFRules is supported. Automatic installation of JVM if not present and of RDFRules is supported.

#### Local instance

First, start by opening a workspace and loading a workspace graph.

```python
# Open a new workspace.
workspace = Workspace(
    path.abspath("./workspace")
)

# load local workspace graph

dbpedia_graph = WorkspaceGraph(
  "<dbpedia>",
  workspace.open('mappingbased_objects_sample.ttl')
)
```

Create a pipeline, a sequence of operations applied on the dataset. All pipeline objects can be found at DOCUMENTATION LINK.

```python
# Create a pipeline
pipeline = Pipeline(
    items=[
        LoadGraph(
            graph=dbpedia_graph
        ),
        # ...
    ]
)
```

Next, create an instance of RDFRules. This is a wrapper for the HTTP interface of RDFRules and spawns the actual process when it is needed. During this step, JVM is installed. You can install it ahead of time by running a separate function on the `rdfrules` instance (todo).

```python
rdfrules = RDFRules(
    workspace=workspace
)
```

As a last step, launch the pipeline, wait for all results and print the head, body and measures of each mined rule.

```python

ruleset = await rdfrules.launch(pipeline)

for rule in ruleset:
    print(rule.head)
    print(rule.body)
    
    for measure in rule.measures:
        print(measure)
```

Full pipeline sample matching the DBpedia & YAGO example from the RDFRules web instance can be found in `sample/dbpedia.py` or DOCUMENTATION LINK (todo).

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
- [ ] Implement JSON serialization of pipeline
- [ ] Implement communication with RDFRules

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