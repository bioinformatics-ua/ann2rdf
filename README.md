Ann2RDF
=======

Semantic layer to convert multiple annotations files into RDF data

## Suported Formats:
  - [BioC](http://bioc.sourceforge.net/)
  - [Standoff](http://brat.nlplab.org/standoff.html)
  
## Installation

 pip install -r requirements.txt

## Usage
  

  $python main.py -h
  usage: main.py [-h] [--config file_source] [--input source]
                 [--output output_file] [--debug]
  
  Annotations converter to RDF/XML.
  
  optional arguments:
    -h, --help            show this help message and exit
    --config file_source  Configuration file (default: config.json)
    --input source        File or Folder to convert (default: test_files)
    --output output_file  Output file (default: output)
    --debug               Enable debug (default: True)
  
## Contact

Pedro Sernadela (sernadela at ua dot pt)
