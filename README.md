# Orchid genera information

![Static Badge](https://img.shields.io/badge/python-3.9-blue?logo=python&label=python)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/parzival1918/orchids-genera-db)

This repo has information of the orchid genera, scrapped with python and bs4 from [https://www.aos.org](https://www.aos.org).

## JSON data

The data can be found in JSON format in [db/json](db/json) folder.

The data is stored by genera starting letter. For example, genera starting with letter `A` are stored in [db/json/letter-a.json](db/json/letter-a.json).

Inside the file the data is stored in an array of entries like:

```json
[
    {
        "name": "str",
        "discovery": "str or null",
        "description": "str",
        "species": "str",
        "distribution": "str",
    },
    {
        "..."
    }
]
```

## CSV data

The data can be found in CSV format in [db/csv](db/csv) folder.

The data is stored by genera starting letter. For example, genera starting with letter `A` are stored in [db/csv/letter-a.csv](db/csv/letter-a.csv).

Inside the file the data is stored in a table like:

| name | discovery | description | species | distribution |
| ---- | --------- | ----------- | ------- | ------------ |
| str  | str or null | str | str | str |

## SQL data

The data can be found in SQL format in [db/sql](db/sql) folder.

The data is stored in a table called orchids with the following columns:

| name | discovery | description | species | distribution |
| ---- | --------- | ----------- | ------- | ------------ |
| str  | str or null | str | str | str |