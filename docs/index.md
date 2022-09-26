<p align="center">
  <img src="http://logos.u2d.ai/msaFeature_logo.png?raw=true" alt="msaFeature Logo"/>
</p>

------
<p align="center">
    <em>msaFeature - Feature switch management with conditions or simple decorators</em>
<br>
    Optimized for use with Starlette/FastAPI/Pydantic. 
    Allows to create feature switches and to setup conditions those switches will be enabled
    for. Once configured, switches can then be checked against inputs (requests, user objects, etc) to see if the switches are active/enabled.
<br>
  <a href="https://pypi.org/project/msaFeature" target="_blank">
      <img src="https://img.shields.io/pypi/v/msaFeature?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://pypi.org/project/msaFeature" target="_blank">
      <img src="https://img.shields.io/pypi/pyversions/msaFeature.svg?color=%2334D058" alt="Supported Python versions">
  </a>
</p>

------

## Features
This library includes two versions for FastAPI Feature Flags Management:

- **Simple**: Just a decorator and configuration with json from a file, dict or via url.
- **Complex with Switch & Conditions**: Complex version with switches and conditions based on your pydantic model and their business logic.



## Main Dependencies

- **fastapi[all]~=0.85.0** : FastAPI framework, high performance, easy to learn, fast to code, ready for production
- **starlette~=0.20.4** : Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
- **msaStorageDict>=0.0.3**: Dict with a Storage Backend like memory, redis or Zookeeper


## License Agreement

- `msaFeature`Based on `MIT` open source and free to use, it is free for commercial use, but please show/list the copyright information about msaFeature somewhere.


## How to create the documentation

We use mkdocs and mkdocsstring. The code reference and nav entry get's created virtually by the triggered python script /docs/gen_ref_pages.py while ``mkdocs`` ``serve`` or ``build`` is executed.

### Requirements Install for the PDF creation option:
PDF Export is using mainly weasyprint, if you get some errors here pls. check there documentation. Installation is part of the msaFeature, so this should be fine.

We can now test and view our documentation using:

    mkdocs serve

Build static Site:

    mkdocs build


## Build and Publish
  
Build:  

    python setup.py sdist

Publish to pypi:

    twine upload dist/*
