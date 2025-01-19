# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/KIZI/pyrdfrules/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                                             |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|--------------------------------------------------------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| src/pyrdfrules/api/cache/cache\_api.py                                           |       10 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/api/cache/cache\_http\_api.py                                     |       16 |        4 |        0 |        0 |     75% |15, 18, 21, 24 |
| src/pyrdfrules/api/http\_api\_urls.py                                            |        7 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/api/http\_rdfrules\_api.py                                        |       12 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/api/http\_rdfrules\_api\_context.py                               |       21 |        1 |        0 |        0 |     95% |        40 |
| src/pyrdfrules/api/rdfrules\_api.py                                              |       12 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/api/rdfrules\_api\_context.py                                     |        2 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/api/task/exception/task\_not\_found\_exception.py                 |        4 |        1 |        0 |        0 |     75% |         9 |
| src/pyrdfrules/api/task/task\_api.py                                             |       16 |        5 |        2 |        0 |     61% |24, 40-43, 48 |
| src/pyrdfrules/api/task/task\_http\_api.py                                       |       49 |       14 |       10 |        3 |     68% |37, 38->41, 56-64, 78-79, 91-101 |
| src/pyrdfrules/api/workspace/exception/workspace\_file\_not\_found\_exception.py |        4 |        2 |        0 |        0 |     50% |       3-4 |
| src/pyrdfrules/api/workspace/workspace\_api.py                                   |       14 |        4 |        0 |        0 |     71% |15, 20, 25, 30 |
| src/pyrdfrules/api/workspace/workspace\_http\_api.py                             |       51 |        9 |       14 |        6 |     74% |22->25, 46-51, 60, 69, 72, 89, 92 |
| src/pyrdfrules/application.py                                                    |       40 |        0 |        4 |        0 |    100% |           |
| src/pyrdfrules/common.py                                                         |       36 |       36 |        0 |        0 |      0% |      5-64 |
| src/pyrdfrules/common/event/event\_dispatcher.py                                 |       16 |        3 |        2 |        0 |     83% | 14, 26-27 |
| src/pyrdfrules/common/exception/pyrdfrules\_exception.py                         |        6 |        3 |        0 |        0 |     50% |   6-7, 10 |
| src/pyrdfrules/common/file/workspace.py                                          |       22 |        1 |        0 |        0 |     95% |        53 |
| src/pyrdfrules/common/file/workspace\_directory.py                               |       16 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/file/workspace\_file.py                                    |       11 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/file/workspace\_item.py                                    |        7 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/file/workspace\_tree.py                                    |       20 |        1 |        6 |        1 |     92% |31->46, 60 |
| src/pyrdfrules/common/format/confusion\_matrix.py                                |       12 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/format/histogram.py                                        |       13 |        0 |        2 |        0 |    100% |           |
| src/pyrdfrules/common/http/get\_http\_client.py                                  |        7 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/http/http\_client.py                                       |       28 |        1 |        0 |        0 |     96% |        24 |
| src/pyrdfrules/common/http/http\_request.py                                      |        0 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/http/url.py                                                |        3 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/logging/logger.py                                          |       24 |        1 |        4 |        1 |     93% |        75 |
| src/pyrdfrules/common/result/evaluation.py                                       |       34 |        0 |        2 |        0 |    100% |           |
| src/pyrdfrules/common/result/histogram.py                                        |       40 |        4 |       10 |        4 |     84% |36->39, 40, 43, 46, 98 |
| src/pyrdfrules/common/result/result.py                                           |       62 |        8 |       16 |        3 |     86% |59-60, 64-65, 87-90 |
| src/pyrdfrules/common/result/resultobject.py                                     |       19 |        9 |        0 |        0 |     53% |18-22, 36-39 |
| src/pyrdfrules/common/rule/measure/measure.py                                    |        4 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/rule/resultrule.py                                         |       21 |        1 |        2 |        0 |     96% |        41 |
| src/pyrdfrules/common/rule/rule/body.py                                          |       16 |        0 |        2 |        0 |    100% |           |
| src/pyrdfrules/common/rule/rule/head.py                                          |       12 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/rule/rule/object.py                                        |        4 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/rule/rule/part.py                                          |        7 |        7 |        0 |        0 |      0% |      1-12 |
| src/pyrdfrules/common/rule/rule/predicate.py                                     |        6 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/rule/rule/subject.py                                       |        4 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/rule/ruleset.py                                            |       14 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/task/event/task\_finished\_message.py                      |        9 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/task/event/task\_log\_message.py                           |        9 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/common/task/task.py                                               |       47 |        3 |       10 |        2 |     91% |57->69, 94, 102-103 |
| src/pyrdfrules/common/task/task\_runner.py                                       |       35 |        3 |        0 |        0 |     91% |66, 72, 78 |
| src/pyrdfrules/common/task/task\_updater.py                                      |       32 |        6 |        2 |        0 |     82% |42-45, 59-62 |
| src/pyrdfrules/config.py                                                         |       14 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/engine/engine.py                                                  |       35 |        9 |        2 |        0 |     70% |9-10, 48, 54, 61, 77, 89-94 |
| src/pyrdfrules/engine/exception/failed\_to\_start\_exception.py                  |        4 |        1 |        0 |        0 |     75% |         8 |
| src/pyrdfrules/engine/http\_engine.py                                            |        9 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/engine/local\_http\_engine.py                                     |       72 |        6 |       10 |        3 |     89% |90, 99->exit, 105-107, 139-140 |
| src/pyrdfrules/engine/remote\_http\_engine.py                                    |       26 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/engine/result/pipeline.py                                         |        2 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/engine/result/used\_memory.py                                     |        6 |        6 |        0 |        0 |      0% |      1-16 |
| src/pyrdfrules/engine/util/jvm.py                                                |      165 |       13 |       42 |       12 |     88% |57->64, 59, 62, 70, 91-92, 103->exit, 131->134, 144, 182, 191, 245-246, 263-264, 277 |
| src/pyrdfrules/rdfrules/commondata.py                                            |      237 |        0 |        4 |        0 |    100% |           |
| src/pyrdfrules/rdfrules/jsonformats.py                                           |       31 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/rdfrules/pipeline.py                                              |      304 |        2 |       12 |        1 |     99% |    46, 68 |
| src/pyrdfrules/rdfrules/rdfrules.py                                              |       29 |        3 |        4 |        1 |     88% | 44, 51-53 |
| src/pyrdfrules/rdfrules/release.py                                               |        4 |        0 |        0 |        0 |    100% |           |
| src/pyrdfrules/rdfrules/workspace.py                                             |       14 |       14 |        0 |        0 |      0% |      1-21 |
| src/pyrdfrules/rdfrules/writers.py                                               |       49 |       49 |        0 |        0 |      0% |      1-70 |
|                                                                        **TOTAL** | **1855** |  **230** |  **162** |   **37** | **86%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/KIZI/pyrdfrules/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/KIZI/pyrdfrules/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/KIZI/pyrdfrules/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/KIZI/pyrdfrules/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2FKIZI%2Fpyrdfrules%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/KIZI/pyrdfrules/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.