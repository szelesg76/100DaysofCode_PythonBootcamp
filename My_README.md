docker építése:
    docker build -t python312 .



mount útvonal powershell alatt:

docker run --name python312 -it -v ${pwd}/src:/app/src python312 bash

docker run --name python312 -it -v ${pwd}/src:/app python312 bash