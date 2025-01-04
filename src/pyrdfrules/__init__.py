# SPDX-FileCopyrightText: 2023-present Karel Douda <kareldouda1@gmail.com>
#
# SPDX-License-Identifier: MIT

"""
PyRDFRules is a Python wrapper for the RDFRules tool, providing an interface to interact with RDFRules for rule mining from RDF knowledge graphs.

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
pipeline = pyrdfrules.rdfrules.pipeline.Pipeline(
    tasks=[
        pyrdfrules.rdfrules.pipeline.LoadGraph(
            graphName = "<dbpedia>",
            path = "/dbpedia_yago/mappingbased_objects_sample.ttl"
        ),
        pyrdfrules.rdfrules.pipeline.LoadGraph(
            graphName = "<yago>",
            path = "/dbpedia_yago/yagoFacts.tsv",
            settings = "tsvParsedUris"
        ),
        pyrdfrules.rdfrules.pipeline.LoadGraph(
            graphName = "<dbpedia>",
            path = "/dbpedia_yago/yagoDBpediaInstances.tsv",
            settings = "tsvParsedUris"
        ),
        pyrdfrules.rdfrules.pipeline.MergeDatasets(),
        pyrdfrules.rdfrules.jsonformats.AddPrefixes(
            prefixes=[
                pyrdfrules.rdfrules.jsonformats.PrefixFull(prefix="dbo", nameSpace="http://dbpedia.org/ontology/"),
                pyrdfrules.rdfrules.jsonformats.PrefixFull(prefix="dbr", nameSpace="http://dbpedia.org/resource/")
            ]
        ),
        pyrdfrules.rdfrules.pipeline.Index(train=[], test=[]),
        pyrdfrules.rdfrules.pipeline.Mine(
            thresholds=[
                pyrdfrules.rdfrules.commondata.Threshold(name="MinHeadSize", value=100),
                pyrdfrules.rdfrules.commondata.Threshold(name="MaxRuleLength", value=3),
                pyrdfrules.rdfrules.commondata.Threshold(name="Timeout", value=5),
                pyrdfrules.rdfrules.commondata.Threshold(name="MinHeadCoverage", value=0.01),
            ],
            ruleConsumers=[
                pyrdfrules.rdfrules.commondata.RuleConsumer(
                    name=pyrdfrules.rdfrules.commondata.RuleConsumerType.TOP_K,
                    k=1000,
                    allowOverflow=False
                )
            ],
            patterns=[],
            constraints=[
                pyrdfrules.rdfrules.commondata.Constraint(name="WithoutConstants")
            ],
            parallelism=0
        ),
        pyrdfrules.rdfrules.pipeline.ComputeConfidence(confidenceType=ConfidenceType.PCA_CONFIDENCE, min=0.5, topk=50),
        pyrdfrules.rdfrules.pipeline.SortRuleset(by=[]),
        pyrdfrules.rdfrules.pipeline.GraphAwareRules(),
        pyrdfrules.rdfrules.pipeline.GetRules()
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