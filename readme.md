# Gitignore Generator Script for VDOM apps
## Overview
This script dynamically generates a .gitignore file based on the contents of a specified JSON configuration file. It is designed to facilitate the management of file and directory exclusions in a git repository, especially useful in projects with complex or frequently changing structures.


## Usage
To use the script, you have several options depending on the desired mode of operation:

### Default Mode:

`python script.py`

This will run the script using the default settings and the default JSON configuration file *(vdom2fs.conf simple mode)*.

### Changing Modes:

`python script.py [mode]`

- Simple Mode: Triggered with the flag type="simple". This mode adds only the directory paths from the JSON configuration to .gitignore.
  
-  Meticulous Mode: Activated with the flag type="meticulous". This mode performs a detailed scan, adding both files and directories to .gitignore, **with special handling of directory "Pages" - it will not go inside it cosider changing code if using this script**.

### Custom Configuration Path:

`python script.py [mode] [path_to_json]`

Replace [path_to_json] with the path to your custom JSON configuration file.

### Input:

As of input, script expects it to be a JSON dictionary inside of a file with another dict named `"Aliases"`

```
{
	"Aliases": {
		"aliasname1": "path",
		"aliasname2": "path",
		"aliasname3": "path"
	},
    ...
}
```
## Requirements
Script is compatable with Python 2 and Python 3.
