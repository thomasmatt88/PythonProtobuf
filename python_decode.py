import python_out.searchrequest_pb2

searchrequest = python_out.searchrequest_pb2.SearchRequest()

# Read the existing searchrequst
f = open("serializedbypython.bin", "rb")
searchrequest.ParseFromString(f.read())
f.close()

print(searchrequest)
