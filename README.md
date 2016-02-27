# Requirements
* virtualenv
* python 3.5.1 (should work with 2.7 also)

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
## Example
```
$ python3 main.py cats
@truhmkjilo: いろいろな場所の猫の日常生活 Funny Cats

https://t.co/lFgyg5ExpY …

#猫　#ねこ　#cat
```
