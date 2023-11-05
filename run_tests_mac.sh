python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

pytest tests/*.py --alluredir=./allure-results

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash

nvm install 14

nvm use 14

npm install --save-dev allure-commandline

npx allure-commandline serve