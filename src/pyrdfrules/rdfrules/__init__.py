"""Represents internal RDFRules representations of entities, and constants.

We provide a set of classes that represent RDFRules entities, such as rules, constraints, and thresholds. These classes are used to interact with the RDFRules engine, and are serialized or deserialized from JSON.

## Pipeline operations

### Pipeline

`pyrdfrules.rdfrules.pipeline.Pipeline` is a class that represents a sequence of tasks that can be executed by the RDFRules engine.

Items to the pipeline are added as a list of tasks, represents the exact order in which they will be executed.

### Pipeline tasks

A pipeline task is a unit of work that can be executed by the RDFRules engine.
Parameters are passed to the task to configure its behavior. For example, a `LoadGraph` task requires a `graphName` and a `path` parameter.

```python
from pyrdfrules.rdfrules.pipeline import LoadGraph

load_task = LoadGraph(
    graphName = "<dbpedia>",
    path = "/dbpedia_yago/mappingbased_objects_sample.ttl"
)
```

Arbitrary parameters can be passed to the task as a dictionary.

```python
from pyrdfrules.rdfrules.pipeline import LoadGraph

load_task = LoadGraph(
    graphName = "<dbpedia>",
    path = "/dbpedia_yago/mappingbased_objects_sample.ttl",
    extra = {
        "key": "value"
    }
)
```

Be aware that this extra behaviour is not very maintainable, as the parameters are not checked for correctness.

### ArbitraryPipelineTask

The ArbitraryPipelineTask operation is a placeholder for any task that is not yet implemented in the library, or the parameters of the task are not represented yet.

Sample usage:
```python
from pyrdfrules.rdfrules.pipeline import ArbitraryPipelineTask

task = ArbitraryPipelineTask(
    name = "SomeName",
    parameters = {
        "key": "value"
    }
)
```

### List of operations

<!--- AUTOMATICALLY GENERATE DOC --->
| Operation                                                                                                                      | Class                                                     |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| ArbitraryPipelineTask                                                                                                          | pyrdfrules.rdfrules.pipeline.ArbitraryPipelineTask()      |
| [LoadGraph](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#load-graph)                                     | pyrdfrules.rdfrules.pipeline.LoadGraph()                  |
| [LoadDataset](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#load-dataset)                                 | pyrdfrules.rdfrules.pipeline.LoadDataset()                |
| [LoadRulesetWithoutIndex](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#load-ruleset-without-index)       | pyrdfrules.rdfrules.pipeline.LoadRulesetWithoutIndex()    |
| [LoadPredictionWithoutIndex](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#load-prediction-without-index) | pyrdfrules.rdfrules.pipeline.LoadPredictionWithoutIndex() |
| [MergeDatasets](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#merge-datasets)                             | pyrdfrules.rdfrules.pipeline.MergeDatasets()              |
| [MapQuads](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#map-quads)                                       | pyrdfrules.rdfrules.pipeline.MapQuads()                   |
| [FilterQuads](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#filter-quads)                                 | pyrdfrules.rdfrules.pipeline.FilterQuads()                |
| [Shrink](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#shrink)                                            | pyrdfrules.rdfrules.pipeline.Shrink()                     |
| [Split](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#split)                                              | pyrdfrules.rdfrules.pipeline.Split()                      |
| [AddPrefixes](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#add-prefixes)                                 | pyrdfrules.rdfrules.pipeline.AddPrefixes()                |
| [Prefixes](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#prefixes)                                        | pyrdfrules.rdfrules.pipeline.Prefixes()                   |
| [Discretize](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#discretize)                                    | pyrdfrules.rdfrules.pipeline.Discretize()                 |
| [DiscretizeInBulk](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#discretize-in-bulk)                      | pyrdfrules.rdfrules.pipeline.DiscretizeInBulk()           |
| [Cache](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#cache)                                              | pyrdfrules.rdfrules.pipeline.Cache()                      |
| [Index](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#index)                                              | pyrdfrules.rdfrules.pipeline.Index()                      |
| [ExportQuads](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#export-quads)                                 | pyrdfrules.rdfrules.pipeline.ExportQuads()                |
| [ExportIndex](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#export-index)                                 | pyrdfrules.rdfrules.pipeline.ExportIndex()                |
| [ExportPrediction](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#export-prediction)                       | pyrdfrules.rdfrules.pipeline.ExportPrediction()           |
| [GetQuads](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#get-quads)                                       | pyrdfrules.rdfrules.pipeline.GetQuads()                   |
| [Size](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#size)                                                | pyrdfrules.rdfrules.pipeline.Size()                       |
| [Properties](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#properties)                                    | pyrdfrules.rdfrules.pipeline.Properties()                 |
| [Histogram](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#histogram)                                      | pyrdfrules.rdfrules.pipeline.Histogram()                  |
| [LoadIndex](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#load-index)                                     | pyrdfrules.rdfrules.pipeline.LoadIndex()                  |
| [CacheIndex](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#cache-index)                                   | pyrdfrules.rdfrules.pipeline.CacheIndex()                 |
| [ToDataset](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#to-dataset)                                     | pyrdfrules.rdfrules.pipeline.ToDataset()                  |
| [ToDatasetWithIntervals](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#to-dataset-with-intervals)         | pyrdfrules.rdfrules.pipeline.ToDatasetWithIntervals()     |
| [ToDatasetPrediction](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#to-dataset-prediction)                | pyrdfrules.rdfrules.pipeline.ToDatasetPrediction()        |
| [ToDatasetPredictionTasks](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#to-dataset-prediction-tasks)     | pyrdfrules.rdfrules.pipeline.ToDatasetPredictionTasks()   |
| [ToPredictions](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#to-predictions)                             | pyrdfrules.rdfrules.pipeline.ToPredictions()              |
| [ToPredictionTasks](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#to-prediction-tasks)                    | pyrdfrules.rdfrules.pipeline.ToPredictionTasks()          |
| [DiscretizeTask](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#discretize-task)                           | pyrdfrules.rdfrules.pipeline.DiscretizeTask()             |
| [Mine](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#mine)                                                | pyrdfrules.rdfrules.pipeline.Mine()                       |
| [LoadRuleset](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#load-ruleset)                                 | pyrdfrules.rdfrules.pipeline.LoadRuleset()                |
| [LoadPrediction](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#load-prediction)                           | pyrdfrules.rdfrules.pipeline.LoadPrediction()             |
| [Predict](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#predict)                                          | pyrdfrules.rdfrules.pipeline.Predict()                    |
| [Prune](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#prune)                                              | pyrdfrules.rdfrules.pipeline.Prune()                      |
| [FilterRules](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#filter-rules)                                 | pyrdfrules.rdfrules.pipeline.FilterRules()                |
| [FilterPrediction](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#filter-prediction)                       | pyrdfrules.rdfrules.pipeline.FilterPrediction()           |
| [FilterPredictionTasks](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#filter-prediction-tasks)            | pyrdfrules.rdfrules.pipeline.FilterPredictionTasks()      |
| [SelectPredictions](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#select-predictions)                     | pyrdfrules.rdfrules.pipeline.SelectPredictions()          |
| [WithModes](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#with-modes)                                     | pyrdfrules.rdfrules.pipeline.WithModes()                  |
| [GroupPredictions](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#group-predictions)                       | pyrdfrules.rdfrules.pipeline.GroupPredictions()           |
| [Evaluate](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#evaluate)                                        | pyrdfrules.rdfrules.pipeline.Evaluate()                   |
| [ShrinkRuleset](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#shrink-ruleset)                             | pyrdfrules.rdfrules.pipeline.ShrinkRuleset()              |
| [ShrinkPrediction](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#shrink-prediction)                       | pyrdfrules.rdfrules.pipeline.ShrinkPrediction()           |
| [ShrinkPredictionTasks](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#shrink-prediction-tasks)            | pyrdfrules.rdfrules.pipeline.ShrinkPredictionTasks()      |
| [SortRuleset](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#sort-ruleset)                                 | pyrdfrules.rdfrules.pipeline.SortRuleset()                |
| [SortPrediction](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#sort-prediction)                           | pyrdfrules.rdfrules.pipeline.SortPrediction()             |
| [ComputeConfidence](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#compute-confidence)                     | pyrdfrules.rdfrules.pipeline.ComputeConfidence()          |
| [ComputeSupport](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#compute-support)                           | pyrdfrules.rdfrules.pipeline.ComputeSupport()             |
| [MakeClusters](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#make-clusters)                               | pyrdfrules.rdfrules.pipeline.MakeClusters()               |
| [FindSimilar](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#find-similar)                                 | pyrdfrules.rdfrules.pipeline.FindSimilar()                |
| [CacheRuleset](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#cache-ruleset)                               | pyrdfrules.rdfrules.pipeline.CacheRuleset()               |
| [CachePrediction](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#cache-prediction)                         | pyrdfrules.rdfrules.pipeline.CachePrediction()            |
| [CachePredictionTasks](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#cache-prediction-tasks)              | pyrdfrules.rdfrules.pipeline.CachePredictionTasks()       |
| [Instantiate](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#instantiate)                                  | pyrdfrules.rdfrules.pipeline.Instantiate()                |
| [GraphAwareRules](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#graph-aware-rules)                        | pyrdfrules.rdfrules.pipeline.GraphAwareRules()            |
| [ExportRules](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#export-rules)                                 | pyrdfrules.rdfrules.pipeline.ExportRules()                |
| [PropertiesCardinalities](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#properties-cardinalities)         | pyrdfrules.rdfrules.pipeline.PropertiesCardinalities()    |
| [GetRules](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#get-rules)                                       | pyrdfrules.rdfrules.pipeline.GetRules()                   |
| [GetPrediction](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#get-prediction)                             | pyrdfrules.rdfrules.pipeline.GetPrediction()              |
| [GetPredictionTasks](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#get-prediction-tasks)                  | pyrdfrules.rdfrules.pipeline.GetPredictionTasks()         |
| [RulesetSize](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#ruleset-size)                                 | pyrdfrules.rdfrules.pipeline.RulesetSize()                |
| [PredictionSize](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#prediction-size)                           | pyrdfrules.rdfrules.pipeline.PredictionSize()             |
| [PredictionTasksSize](https://github.com/propi/rdfrules/blob/master/gui/webapp/README.md#prediction-tasks-size)                | pyrdfrules.rdfrules.pipeline.PredictionTasksSize()        |
<!--- END AUTOMATICALLY GENERATE DOC --->

"""