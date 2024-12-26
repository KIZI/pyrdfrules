#!/bin/bash

datamodel-codegen --url https://raw.githubusercontent.com/propi/rdfrules/refs/heads/master/http/schema/pipeline.json --field-constraints --use-field-description --collapse-root-models --output-model-type pydantic_v2.BaseModel > src/pyrdfrules/rdfrules.py