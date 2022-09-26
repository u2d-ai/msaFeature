<p align="center">
  <img src="http://logos.u2d.ai/msaFeature_logo.png?raw=true" alt="msaFeature Logo"/>
</p>

------
<p align="center">
    <em>msaFeature - Feature switch management with conditions or simple decorators</em>
<br>
    Optimized for use with Starlette/FastAPI/Pydantic.
<br>
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

**Documentation**: <a href="https://msaFeature.u2d.ai/" target="_blank">msaFeature Documentation (https://msaFeature.u2d.ai/)</a>

------

## Features
This library includes two versions for FastAPI Feature Flags Management:

- **Simple**: Just a decorator and configuration with json from a file, dict or via url.
- **Complex with Switch & Conditions**: Complex version with switches and conditions based on your pydantic model and their business logic.


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
