import python_out.searchrequest_pb2

searchrequest = python_out.searchrequest_pb2.SearchRequest()

searchrequest.query = "SELECT * FROM X"
searchrequest.page_number = 8
searchrequest.result_per_page = 5
# searchrequest.timestamp.GetCurrentTime() # set timestamp at write

print(searchrequest)
print(type(searchrequest))

# Write searchrequest to disk.
f = open("serializedbypython.pb", "wb")
f.write(searchrequest.SerializeToString())
f.close()
