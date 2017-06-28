# Python-Hackpad-API


A simple wrapper library for the Hackpad API. [Hackpad API Documentation](https://hackpad.co/Hackpad-API-v1.0-KdHQhIEfGJG)

## Installation 

This works best from a virtualenv:

```
virtualenv -p python3 ve3
. ve3/bin/activate
```

Navigate to the folder where you have downloaded this repo, and type

```
pip install -r requirements.txt
```

into your terminal / command prompt.

# Usage

```python
temp = Hackpad('the_hackpad_api_domain', 'your_hackpad_subdomain','your_hackpad_client_id','your_hackpad_secret')
my_hackpads = temp.list_all()
```

Notes:

* For `your_hackpad_subdomain`, just type the stem, not the full domain name (i.e. `mysubdomain`, not `http://mysubdomain.hackpad.com`, etc).
* Your Client ID and Secret for the different subdomains you are signed into. Make sure to use the correct keys for the subdomain you are signing into.

# Running the example

First export the following environment vars (below in Mac OS style):

```
export HACKPAD_SUB_DOMAIN=your_hackpad_subdomain
export HACKPAD_API_DOMAIN=the_hackpad_api_domain
export HACKPAD_CLIENT_ID=your_hackpad_client_id
export HACKPAD_SECRET=your_hackpad_secret
```

Then run it:

```
python example/example1.py
```

# Credits

This repository is based on the work of [Kevin Marshall](https://github.com/Falicon). 

An essential oAuth fix to the original library was made by [Jeremi Joslin](https://github.com/jeremi).

Thanks guys!
