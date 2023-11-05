python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

pytest tests/*.py --alluredir=./allure-results

npm install --save-dev allure-commandline

npx allure-commandline serve