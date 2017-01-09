"""
Tightens up response content by removed superflous line breaks and whitespace.
By Doug Van Horn

---- CHANGES ----
v1.1 - 31st May 2011
Cal Leeming [Simplicity Media Ltd]
Modified regex to strip leading/trailing white space from every line, not just those with blank \n.

---- TODO ----
* Ensure whitespace isn't stripped from within <pre> or <code> or <textarea> tags.

"""

import re

class StripWhitespaceMiddleware(object):
    """
    Strips leading and trailing whitespace from response content.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.whitespace = re.compile('^\s*\n', re.MULTILINE)
        # self.whitespace_lead = re.compile('^\s+', re.MULTILINE)
        # self.whitespace_trail = re.compile('\s+$', re.MULTILINE)


    def __call__(self, request):
        response = self.get_response(request)
        # FIXME
        # File "/usr/local/lib/python3.6/site-packages/smokeping/middleware.py", line 38, in __call__
        #  response.content = self.whitespace.sub(', response.content)
        # TypeError: cannot use a string pattern on a bytes-like object
        return response
        if "text" in response['Content-Type']:
            if hasattr(self, 'whitespace_lead'):
                response.content = self.whitespace_lead.sub('', response.content)
            if hasattr(self, 'whitespace_trail'):
                response.content = self.whitespace_trail.sub('\n', response.content)
            # Uncomment the next line to remove empty lines
            if hasattr(self, 'whitespace'):
                response.content = self.whitespace.sub('', response.content)
            return response
        else:
            return response
