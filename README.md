# crime_searcher | Exam Project, Python Elective Spring 2019
crime_searcher is a terminal application to search for crimes commited in Sacramento. Based on the dataset in the [SacramentocrimeJanuary2006.csv](csv-files/SacramentocrimeJanuary2006.csv) file.

![Last Commit](https://img.shields.io/github/last-commit/martinloesethjensen/crime_searcher.svg) ![Top Language](https://img.shields.io/github/languages/top/martinloesethjensen/crime_searcher.svg) ![License](https://img.shields.io/github/license/martinloesethjensen/crime_searcher.svg) ![Repo Size](https://img.shields.io/github/repo-size/martinloesethjensen/crime_searcher.svg) ![PyPi Implementation](https://img.shields.io/pypi/implementation/geopy.svg) ![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed/martinloesethjensen/crime_searcher.svg)

## Installation 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [simple-colors](https://pypi.org/project/simple-colors/), [geopy](https://pypi.org/project/geopy/), and [geographiclib](https://pypi.org/project/geographiclib/).

```bash
pip install simple-colors | pip install geographiclib | pip install geopy

```

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
[MIT](https://choosealicense.com/licenses/mit/)
