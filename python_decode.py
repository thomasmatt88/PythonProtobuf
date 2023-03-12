import python_out.searchrequest_pb2

searchrequest = python_out.searchrequest_pb2.SearchRequest()

# Read the existing searchrequst
f = open("serializedbypython.pb", "rb")
searchrequest.ParseFromString(f.read())
f.close()

print(searchrequest)

if not searchrequest.HasField("timestamp"):
    """
    checks if field has been assigned a value in the message instance,
    regardless of whether the field is defined in the schema or not
    """
    searchrequest.timestamp.GetCurrentTime()  # set timestamp at read

print(searchrequest)
