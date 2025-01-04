"""
RDFRules file representations.

Read all files in the workspace:

```python
rdfrules = app.start_remote(
    url = Url("...")
)

rdfrules.workspace.get_files()
```

Upload a file:

```python
with open(path, "r") as file:        
    rdfrules.workspace.upload_file("data/asset.txt", file)
```

Delete a file:

```python
rdfrules.workspace.delete_file("data/asset.txt")
```
"""