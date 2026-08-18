# TFlexXML.TFXMLDocument

Assembly: `TFlexAPI`
Namespace: `TFlexXML`

## Methods

### `LoadXml(std.basic_string_view<System.Char,std.char_traits{System.Char}>)`

ID: `M:TFlexXML.TFXMLDocument.LoadXml(std.basic_string_view<System.Char,std.char_traits{System.Char}>)`

Loads an XML document using the supplied string.

Parameters:
- `strXML`: A string containing the XML string to load into this XML document object. This string can contain an entire XML document or a well-formed fragment.

Returns: Boolean. Returns True if the XML load succeeded. Returns False and sets the documentElement property of the DOMDocument to Null if the XML load failed.
