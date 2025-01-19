# SPDX-FileCopyrightText: 2023-present Karel Douda <kareldouda1@gmail.com>
#
# SPDX-License-Identifier: MIT

"""
PyRDFRules is a Python wrapper for the RDFRules tool, providing an interface to interact with RDFRules for rule mining from RDF knowledge graphs.

## Features

- Start and stop the RDFRules engine.
- Provision a local instance of RDFRules.
- Create and run tasks.
- Access the results of the tasks.
- Format the results of the tasks.

## Quickstart

If you want to get started with PyRDFRules instantly, you can use one of the two following Google Colab notebooks:

* [Template RDFRules Notebook](https://colab.research.google.com/drive/1KCyv7b6RtQgQXk-V-oTjYpiQsC-_mFHp?usp=sharing) - use this notebook as a start for your analysis workloads, provisions the PyRDFRules library and local RDFRules.
* [Pipeline sample](https://colab.research.google.com/drive/192YaNsbpqoD9-he32OaY2nTi-E_ctXYT?usp=sharing) - a sample pipeline on a local instance of RDFRules, from starting the instance to getting the results.

## Installation

1. Install the package using pip:
```bash
pip install pyrdfrules
```

2. Configure the RDFRules instance ahead of time using the `Config` class:

```python
from pyrdfrules.config import Config

config = Config()
``` 

For config options, click on the `pyrdfrules.config.Config` class in the documentation.

3. Start a local instance of RDFRules:
```python
app = pyrdfrules.application.Application()

rdfrules = app.start_local(
    install_jvm = True,
    install_rdfrules = True,
    config = config
)
```

## Modules

The library is segmented into the following modules:

* `pyrdfrules.api` - internal API classes.
* `pyrdfrules.application` - provides methods to start and stop local or remote instances of RDFRules.
* `pyrdfrules.common` - contains common classes and methods.
* `pyrdfrules.config` - configuration class.
* `pyrdfrules.engine` - contains the engine classes, responsible for the lifetime of the RDFRules instance.
* `pyrdfrules.rdfrules` - contains wrappers around RDFRules objects.

## Supported operations and result types

Supported operations and bindings of serialized items for each domain can be found at:
* `pyrdfrules.rdfrules` - pipeline operations,
* `pyrdfrules.common.result` - result types,
** `pyrdfrules.rdfrules.evaluation` - evaluation results, printing confusion matrix,
** `pyrdfrules.rdfrules.histogram` - histogram results, printing histograms, top N results,
** `pyrdfrules.common.rule.ruleset` - ruleset, printing individual `pyrdfrules.common.rule.rule` rules in text format.

## Sample pipeline

Sample usage:
```python
import pyrdfrules.application
from pyrdfrules.common.task.task import Task
from pyrdfrules.config import Config
from pyrdfrules.rdfrules.commondata import ConfidenceType, Constraint, RuleConsumer, RuleConsumerType, Threshold
from pyrdfrules.rdfrules.jsonformats import PrefixFull
from pyrdfrules.rdfrules.pipeline import ComputeConfidence, GetRules, GraphAwareRules, Index, LoadGraph, MergeDatasets, AddPrefixes, Mine, Pipeline, SortRuleset

# Create an instance of the application.
app = pyrdfrules.application.Application()

# Connect to an existing instance of RDFRules.
rdfrules = app.start_remote(
    url = Url("http://example.com/api/"),
    config=Config(
        task_update_interval_ms=1000
    )
)

# Create a pipeline, a sequence of steps to be executed.
# You do not have to use fully qualified names for the classes, as they are imported in the example.
pipeline = Pipeline(
    tasks=[
        LoadGraph(
            graphName = "<dbpedia>",
            path = "/dbpedia_yago/mappingbased_objects_sample.ttl"
        ),
        LoadGraph(
            graphName = "<yago>",
            path = "/dbpedia_yago/yagoFacts.tsv",
            settings = "tsvParsedUris"
        ),
        LoadGraph(
            graphName = "<dbpedia>",
            path = "/dbpedia_yago/yagoDBpediaInstances.tsv",
            settings = "tsvParsedUris"
        ),
        MergeDatasets(),
        AddPrefixes(
            prefixes=[
                PrefixFull(prefix="dbo", nameSpace="http://dbpedia.org/ontology/"),
                PrefixFull(prefix="dbr", nameSpace="http://dbpedia.org/resource/")
            ]
        ),
        Index(train=[], test=[]),
        Mine(
            thresholds=[
                Threshold(name="MinHeadSize", value=100),
                Threshold(name="MaxRuleLength", value=3),
                Threshold(name="Timeout", value=5),
                Threshold(name="MinHeadCoverage", value=0.01),
            ],
            ruleConsumers=[
                RuleConsumer(
                    name=RuleConsumerType.TOP_K,
                    k=1000,
                    allowOverflow=False
                )
            ],
            patterns=[],
            constraints=[
                Constraint(name="WithoutConstants")
            ],
            parallelism=0
        ),
        ComputeConfidence(confidenceType=ConfidenceType.PCA_CONFIDENCE, min=0.5, topk=50),
        SortRuleset(by=[]),
        GraphAwareRules(),
        GetRules()
    ]
)

# Create a task, which represents the execution of the pipeline.
task : Task = None

# Submit the task to the RDFRules engine.
task = rdfrules.task.create_task(pipeline)
    
# Run the task step by step.
for step in rdfrules.task.run_task(task):
    print(step)
    # You can access the result of the task using the task object, read the logs, or interrupt the task here.

# Access the result of the task.
print(task.result)

# Access the rules from the result.
for rule in task.result.get_ruleset().get_rules():
    print(rule.as_text()) # Print the rule in text format.
```        
"""