### Date created
2022-01-24

### Project Title
Explore US Bikeshare Data

### Description
Use Python to understand U.S. bikeshare data.  Calculate statistics and build an interactive environment where a user chooses the data and filter for a dataset to analyze.

### Files used
```console
.gitignore
chicago.csv
README.md
```

### Commands
```console
# 1
git clone git@github.com:liviubalan/pdsnd_github.git
git add .
git commit
git push origin master

# 2
git checkout -b documentation
git add .
git commit
git push origin documentation
git status
git checkout master
git status

# 3
git checkout documentation
git add .
git commit
git push origin documentation
git checkout master
git log --oneline --decorate --graph --all

# 4
git checkout -b refactoring
git add .
git commit
git push origin refactoring
git checkout master

# 5
git checkout master
git remote add upstream https://github.com/udacity/pdsnd_github.git
git remote -v
git fetch
git pull upstream master
git pull origin documentation
git push origin master
git pull origin refactoring
git push origin master
```

### Credits
Resources:
* https://stackoverflow.com/questions/51212631/user-input-against-a-list-python
* https://careerkarma.com/blog/python-check-if-file-exists/
* https://stackoverflow.com/questions/285289/exit-codes-in-python
* https://datascientyst.com/convert-datetime-day-of-week-name-number-in-pandas/
* https://stackoverflow.com/questions/60214194/error-in-reading-stock-data-datetimeproperties-object-has-no-attribute-week
* https://stackoverflow.com/questions/48590268/pandas-get-the-most-frequent-values-of-a-column/48590361
* https://stackoverflow.com/questions/20303826/highlight-bash-shell-code-in-markdown-files
* https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
* https://stackoverflow.com/questions/10665889/how-to-take-column-slices-of-dataframe-in-pandas
* https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
