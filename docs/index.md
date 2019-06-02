# crime_searcher | Exam Project, Python Elective Spring 2019
crime_searcher is a terminal application to search for crimes committed in Sacramento. Based on the dataset in the [SacramentocrimeJanuary2006.csv](../csv-files/SacramentocrimeJanuary2006.csv) file.

![Last Commit](https://img.shields.io/github/last-commit/martinloesethjensen/crime_searcher.svg) ![Top Language](https://img.shields.io/github/languages/top/martinloesethjensen/crime_searcher.svg) [![License: MIT](https://img.shields.io/github/license/martinloesethjensen/crime_searcher.svg)](../LICENSE) ![Repo Size](https://img.shields.io/github/repo-size/martinloesethjensen/crime_searcher.svg) ![PyPi Implementation](https://img.shields.io/pypi/implementation/geopy.svg) ![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed/martinloesethjensen/crime_searcher.svg)

## Installation 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [simple-colors](https://pypi.org/project/simple-colors/), [geopy](https://pypi.org/project/geopy/), and [geographiclib](https://pypi.org/project/geographiclib/).

You might need to to make a new python environment to install it. You can find further information on [how to make a python environment and activate it](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments). 

```bash
pip install simple-colors | pip install geographiclib | pip install geopy

```

## Usage
Run the `app.py` to start the program. 

> Remember to be in the same folder as the `app.py` file.

```bash
python app.py
```

### Searching Using Category:
First thing printed out is the menu.

```
--- Main Menu ---
Enter 1: Search for a crime
Enter 2: Report a crime
Enter 3: Find crimes in proximity
Enter -1: Quit

Please enter a number: 
```

To search for a crime on a specific category you'd have to input `1` in the console.

The next being displayed is a list of categories with examples to search for.

```
--- Categories ---
Enter 1: Date and time '1/1/06 0:00'
Enter 2: Address '3108 OCCIDENTAL DR'
Enter 3: District '2'
Enter 4: Grid '508'
Enter 5: Crime description '10851(A)VC TAKE VEH W/O OWNER'
Enter 6: UCR NCIC CODE '2404'
Enter -1: Go back

Please enter a number: 
```

For example input `1` to search by date and time. We will use the example.

```
Please enter a number: 1
Search: 1/1/06 0:00
```

The results would be as following:

```
...

Result 20:
	cdatetime:           1/1/06 0:00
	address:             5641 DORSET WAY
	district:            4
	beat:                4C        
	grid:                1225
	crimedescr:          484J PC PUBLISH CARD INFO
	ucr_ncic_code:       2605
	latitude:            38.52459987
	longitude:           -121.5203609
Results: 20
```

The user can then choose if he/she wants to export the results in either HTML or JSON format.

```
--- Export Options ---
Enter 1: JSON format
Enter 2: HTML format
Enter -1: Don't export

Please enter a number: 
```

If user chose to export the results, then he/she can find the files in `output-files` folder.

> The file will automatically get opened.


### Tests
Tests can be found in `test` folder and can be run as following. 

> Unittest supports simple [test discovery.](https://docs.python.org/3/library/unittest.html#test-discovery) 

```bash
python -m unittest discover -s test -p "*_test.py"
```

> Discovers all files ending with: `_test.py`

```bash
python -m unittest discover -s test -p "value_test.py"
```

> Discovers a specific file: `value_test.py`

#### Examples:

##### Indexed filenames:
`value_test.py`
`gps_test.py`

##### Unindexed filenames:
`value.py`
`gps_test2.py`


## Exam Requirements
* The project should be finished, meaning: don´t hand in and show up at the exam with something half done.  
* Your code will be evaluated in terms of readability  
* Your project will be evaluated in relation to the extent to which it is perceived as a finished product.  
* The code should be documented and you should be able to explain why you documented your code in the way you did.  
* The code should be tested and you should at the exam be abel to talk about your tests and demonstrate them.


## Application Requirements
* In the application you should be able to search for crimes based on the data in the different columns in the dataset.
* The application should be able to take a gps point (lon-lat) and return a list of crimes made within a radius of 5 km.
* The data output should be readable (for normal users).
* The application should furthermore be able to add new records to the dataset. (this includes writing to the csv file.)
* The application should be able to export the whole dataset into json and html formats, and should be able to export search results in json and and html formats as well.

## License
[![License: MIT](https://img.shields.io/github/license/martinloesethjensen/crime_searcher.svg)](../LICENSE)
