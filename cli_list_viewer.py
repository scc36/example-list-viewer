import sys

from url_parser import UrlParser

try:
    # Assume first argument is the url
    input_url = sys.argv[1]
except IndexError:
    print "URL is a required input"
else:
    parser = UrlParser(input_url)

    parser.process_url()

    print "---iMessage Details---"
    print str(parser)
