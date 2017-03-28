# Batch downloading

The *main.py* script uses *info.json* file to make batch downloading.

Everything you have to do to use this script is alter the *info.json* file with your data and execute *main.py*.

### info.json
The *info.json* file is a JSON object which contains the self explainable fields *main_url* and *mime_type*.\
Besides, the *files* array contains the possibles finals parts of the downloadable URL.

### main.py
This script will make a request for every element in the *info.json > files* array to download the file from the base url indicated in *info.json > main_url*.
