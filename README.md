# Requirements
* virtualenv version 14.0.6
* python 3.5.1

# Setup
```
git clone
virtualenv -p python3 ENV
source ENV/bin/activate
pip install -r requirements.txt
cp sample_config.py config.py
```

Then, fill out `config.py` with consumer key and secret obtained from a registered Twitter app, at https://apps.twitter.com/

When finished, be sure to unsource by using `deactivate`.

# Usage
```
python3 main.py <keyword>
```

