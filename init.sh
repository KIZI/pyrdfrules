#!/bin/bash

wget https://github.com/propi/rdfrules/releases/download/1.7.2/rdfrules-1.7.2.zip -P src/rdfrules
unzip src/rdfrules/rdfrules-1.7.2.zip -d src/rdfrules
rm src/rdfrules/rdfrules-1.7.2.zip