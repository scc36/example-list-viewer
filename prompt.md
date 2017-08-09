https://gist.github.com/buckhx/c5f77145b37e1002e2879304ecb5a6a1

We've buit an [imessage extension](https://www.producthunt.com/posts/the-infatuation-s-imessage-app) to quickly share restaurants and build your own lists to share. The lists are represented as url-safe, base64 encoded,
LZMA compressed protocol buffers in the url's query params.

This serialization works great for machine communication, but is tough to debug because it is not human readable. We'd like for you to build a simple tool for viewing the list contents in a human readable format for debugging. The simplest tool would be a CLI, but feel free to do a service or simple web app if you'd like. Use any language/tools you want, with a preference on Python & Go.

You'll also need to leverage our current API to look up info about items in the list.

Treat this project as if it was an open source utility that you were going to distribute. Things like a README with what it does, how to use it and how to build it locally.

The lists are passed around as URLs in the following structure:

    https://api.theinfatuation.com/services/v3/lists/{:id}?content={base64(lzma(pbf(:list)))}

Protocol Buffers
----------------

You'll need to build a binding for the list definition in the language of your choice
from the following tools. Feel free to add options to the def if it makes working
with easier for the tools/lang you're using. (Use can see there's already a objc option).

* [List Protobuf Definiton](https://gist.github.com/buckhx/f8bb6c5464a6c322db20ada8f9198397)
* protoc 3.0.0+
* fields with // skip comment don't need to be displayed
* The [Google Timestamp Well-Known Type](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) is used and needs to be on the protoc path.
* If you are on OSX and use brew. "brew install protobuf" will install all the needed tools.

Some other resources

* https://developers.google.com/protocol-buffers/
* https://github.com/google/protobuf

Url Safe Base64 Encoding
------------------------

* [base64 rfc](https://tools.ietf.org/html/rfc4648#section-5)
* replace /+ with _- respectively when encoding (vice versa during decoding)
* strip = padding (Will need to re-pad when decoding)

LZMA Compression
----------------

Slow compression w/ very good ratio

* https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm
* Should be a library in any language
* Apple Data Compression Reference: https://developer.apple.com/reference/compression/1665429-data_compression

Infatuation API
---------------
The ID in the items list will be an infatuation venue ID. Use the API to get the name of the restaurant for debugging.

* https://api.theinfatuation.com/services/v3/venues/{:id}
