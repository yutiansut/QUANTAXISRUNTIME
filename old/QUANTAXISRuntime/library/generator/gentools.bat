 .\protoc.exe --python_out ..\precompile  --proto_path ..\protolibrary --cpp_out ..\precompile --csharp_out ..\precompile --grpc_out ..\precompile --plugin=protoc-gen-grpc=.\grpc_csharp_plugin.exe ..\protolibrary\quotation.proto

.\protoc.exe --python_out ..\precompile  --proto_path ..\protolibrary --cpp_out ..\precompile --csharp_out ..\precompile  --grpc_out ..\precompile --plugin=protoc-gen-grpc=.\grpc_csharp_plugin.exe ..\protolibrary\tradergateway.proto
  
.\protoc.exe --python_out ..\precompile  --proto_path ..\protolibrary --cpp_out ..\precompile --csharp_out ..\precompile --grpc_out ..\precompile --plugin=protoc-gen-grpc=.\grpc_csharp_plugin.exe ..\protolibrary\query.proto