Example to show exchange of data via protobuf from one Python application to another

Motivation:
- Protobuf encoding is significantly more efficient in size than either XML or JSON encoding
    - minimizes data storage
    - minimizes network traffic
- Serialization and deserialization may become the bottleneck in data interchange because these 
operations are CPU-intensive. Efficient serialization and deserialization is another Protobuf design goal.


Manually create searchrequest.proto (schema definition)

Now that you have a .proto, the next thing you need to do is generate the classes you'll need 
to read and write SearchRequest messages

get protoc for your system (in my case win64) from https://github.com/protocolbuffers/protobuf/releases/tag/v3.19.4
Save and unzip to ./protoc

Check protoc is working
> \protoc\protoc-3.19.4-win64\bin\protoc.exe –version
libprotoc 3.19.4

protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/searchrequest.proto
> .\protoc\protoc-3.19.4-win64\bin\protoc.exe --python_out="./python_out" searchrequest.proto


Serialize/Encode data to binary with Python
> pip install --upgrade google-api-python-client
https://stackoverflow.com/questions/44577730/file-extension-for-serialized-protobuf-output
> python .\python_encode.py

This will create searializedbypython.pb with data hardcoded in python_encode.py

Decode binary data with Python
> python .\python_decode.py