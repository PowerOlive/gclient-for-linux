#!/bin/bash
path=$(dirname $0)
path=${path/\./$(pwd)}
cd $path && sudo java -jar gfw.press.jar client
