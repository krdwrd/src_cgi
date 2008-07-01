import sys

class Hook:

    def __init__(self, logdir=None):
        self.logdir = logdir            # log tracebacks to files if not None

    def __call__(self, etype, evalue, etb):
        self.handle((etype, evalue, etb))

    def handle(self, info=None):
        info = info or sys.exc_info()

        import traceback
        plain = True

        print '''<div style="width: 50%; margin: 5em auto; border: 1px solid #AAA; padding: 1em;"><div style="background-color: #F0F; padding: 1em; color: #000; font-size: x-large;">Error</div><br/>'''
        print info[1]
        print '<br /><br /><i>Please contact <a href="mailto:krdwrd@krdwrd.org">krdwrd@krdwrd.org</a> if you think this is an error on the server side.</i></div>'

        if self.logdir is not None:
            doc = ''.join(traceback.format_exception(*info))
            import os, tempfile
            path = tempfile.mktemp(suffix=".log", dir=self.logdir)
            f = file(path, 'w')
            f.write(doc)
            f.close()

handler = Hook().handle

def enable(logdir=None):
    """Install an exception handler that formats tracebacks as HTML.

    The optional argument 'display' can be set to 0 to suppress sending the
    traceback to the browser, and 'logdir' can be set to a directory to cause
    tracebacks to be written to files there."""
    sys.excepthook = Hook(logdir=logdir)
