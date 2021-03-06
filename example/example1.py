import os
from hackpad_api.hackpad import Hackpad

hackpad = Hackpad(api_scheme = os.getenv('HACKPAD_API_SCHEME'),
                  api_domain = os.getenv('HACKPAD_API_DOMAIN'),
                  sub_domain = os.getenv('HACKPAD_SUB_DOMAIN'),
                  consumer_key = os.getenv('HACKPAD_CLIENT_ID'),
                  consumer_secret = os.getenv('HACKPAD_SECRET'))

new_html_pad = hackpad.create_hackpad('HTML Pad Title Here', '<html><body><h1>HTML Pad Title Here</h1><p><img class="inline-img" src="https://s3.eu-central-1.amazonaws.com/stekpad/hackpad.com_kqQGLwBTjFe_p.222569_1407665146682_Get_Point.jpg" faketext="*" contenteditable="false"></p><p>And some text in <b>HTML</b>.</p><p><a href="http://cool.com/">Very cool no?</a></p></body></html>', '', 'text/html')

new_txt_pad = hackpad.create_hackpad('Text Pad Title Here', 'And some plain text.\n\nVery cool no?\n', '', 'text/plain')

all_pads = hackpad.list_all()

for padId in all_pads:
    #    hackpad.do_api_request()
    pad = hackpad.get_pad_content(padId)
    print(pad.decode('utf-8'))
    print('-'*79)
