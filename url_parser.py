import base64
import collections
import requests
from urlparse import urlparse

from backports import lzma
import yaml

import restaurantlist_pb2

class UrlParser(object):
    """
        Support class for parsing Infatuation imessage restaurant lists
        Stores data internally as dictionary

        Expecting: https://api.theinfatuation.com/services/v3/lists/{:id}?content={base64(lzma(pbf(:list)))}

        init (with url)
        parse url
        call for desired output type
    """
    raw_url = ""
    url_data = {}

    def __init__(self, input_url):
        self.raw_url = input_url
        self.url_data = {
            "status": "Unprocessed"
        }

    def process_url(self):
        """ turns raw URL into organized dictionary
            Will make calls to The Infatuation API
        """

        # HTTP convert
        parsed_url = http_parse(self.raw_url)

        url_content = parsed_url["content"]

        decoded_content = step_decode(url_content)

        # Decompress
        decompressed_content = lzma.decompress(decoded_content)

        list_details = protocol_parsing(decompressed_content)

        self.url_data = {
            "imessaage_id": parsed_url["id"],
            "data": list_details,
            "status": "Process complete"
        }

    def __str__(self):
        """ keeping output simple by outputting in yaml format
        """
        utf8_dict = dict_unicode_to_utf8(self.url_data)
        return yaml.dump(utf8_dict, default_flow_style=False)

### Helper functions
def http_parse(url):
    """
        lifts relevant information out put url
        returns json with information
            id, content
    """

    # HTTP convert
    parsed_url = urlparse(url)

    # ID is the last segment in the path
    url_id = parsed_url.path.split("/")[-1]

    # Unprocessed query
    # Look for "content="
    #  More a python3
    #query_content = urlparse.parse_qs(parsed_url.query)
    #url_content = query_content.get("content", "")
    # Remove "content=" (length of 8) and add padding
    url_content = parsed_url.query[8:]

    return {
        "id": url_id,
        "content": url_content
    }

def step_decode(url_content):
    """
        url content was encoded with url safe base64

        returns decoded string
    """
    # Unprocessed query
    # Remove "content=" (length of 8) and add padding
    url_content = url_content + "=="

    # replace _- with /+ with respectively
    url_content = url_content.replace ("_", "/")
    url_content = url_content.replace ("-", "+")

    decoded_content = base64.urlsafe_b64decode(url_content)

    return decoded_content


def protocol_parsing(unpacked_content):
    """
        given a "protobuf" string, lift out desired data using restaurantlist_pb2

        Hierarchy ATM: List -> Item
                          -> Annotation -> User
    """

    parsed_list = restaurantlist_pb2.List()
    parsed_list.ParseFromString(unpacked_content)

    # strings are unicode, turn them into utf8
    return_list = {
        "list_id": parsed_list.id,
        "list_label": parsed_list.label,
        "image_url": parsed_list.image_url,
        "items": []
    }

    # Annotation
    return_list["list_blurb"] = protobuf_annotation(parsed_list.blurb)

    # Items
    for item in parsed_list.items:
        return_list["items"].append (protobuf_item(item))

    return return_list


# Helper functions for protobuf processing
def protobuf_annotation (annotation):
    """
        given a "restaurantlist_pb2" Annotation
        return a dictionary of annotation details

        annotation == restaurantlist_pb2.Annotation
    """

    # convert to string, and encode unicode
    return_annotation = {
        "timestamp": annotation.timestamp.ToJsonString(),
        "message": annotation.msg
    }

    # user = restaurantlist_pb2.User
    #  encode unicode
    return_annotation ["user"] = {
        "user_id": annotation.user.id,
        "name": annotation.user.name
    }

    return return_annotation


def protobuf_item (item):
    """
        given a "restaurantlist_pb2" Item
        return a dictionary of item details

        item == restaurantlist_pb2.Item
    """

    # Make a request to https://api.theinfatuation.com/services/v3/venues/{:id}
    request_url = "https://api.theinfatuation.com/services/v3/venues/%s" % item.infatuation
    r = requests.get(request_url)
    # expect json output
    venue_info = r.json()

    # currently must be infatuation instead of foursquare
    return_item = {
        "venue_info": venue_info,
        "annotations": []
    }

    for annotation in item.annotations:
        return_item["annotations"].append (annotation)

    return return_item

def dict_unicode_to_utf8 (unicode_json):
    """ quick helper function to convert all unicode in a dict to utf8
    """
    if isinstance(unicode_json, basestring):
        return unicode_json.encode('utf-8')
    elif isinstance(unicode_json, collections.Mapping):
        return dict(map(dict_unicode_to_utf8, unicode_json.iteritems()))
    elif isinstance(unicode_json, collections.Iterable):
        return type(unicode_json)(map(dict_unicode_to_utf8, unicode_json))
    else:
        return unicode_json
