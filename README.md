# Random Tweet Grabber
Grabs a random tweet based on a keyword.

## Requirements
* virtualenv
* python 3.5.1 (should work with 2.7 also)

## Setup
```
git clone https://github.com/keithyong/random-tweet-grabber
cd random-tweet-grabber
virtualenv -p python3 ENV
source ENV/bin/activate
pip install -r requirements.txt
cp sample_config.py config.py
```

Then, fill out `config.py` with consumer key and secret obtained from a registered Twitter app, at https://apps.twitter.com/:

Create New App > use a placeholder like http://test.com for "Website" field > manage keys and access tokens

When finished, be sure to unsource by using `deactivate`.

## Usage
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
