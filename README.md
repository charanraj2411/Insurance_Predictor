create env

conda create -n wineq python=3.7 -y
activate env

conda activate wineq
created a req file

install the req

pip install -r requirements.txt
download the data from

https://www.kaggle.com/sonujha090/insurance-prediction?select=insurance.csv

git init
dvc init 
dvc add data_given/winequality.csv
git add .
git commit -m "first commit"
oneliner updates for readme


git add . && git commit -m "update Readme.md"
git remote add origin NAME OF PROJECT

git branch -M main

git push origin main

tox command -

tox
for rebuilding -

tox -r 
pytest command

pytest -v
setup commands -

pip install -e . 
build your own package commands-

python setup.py sdist bdist_wheel