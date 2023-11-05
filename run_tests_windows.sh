python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt

pytest tests/*.py --alluredir=./allure-results

npm install --save-dev allure-commandline

npx allure-commandline serve
