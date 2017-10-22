from grpc_tools import protoc


protoc.main(
    (
        '',
        '-I.',
        '--python_out=../precompile',
        '--grpc_python_out=../precompile',
        '--'
        '../protolibrary/event.proto',
    )
)

protoc.main(
    (
        '',
        '-I.',
        '--python_out=../precompile',
        '--grpc_python_out=../precompile',
        '../protolibrary/query.proto',
    )
)

protoc.main(
    (
        '',
        '-I.',
        '--python_out=../precompile',
        '--grpc_python_out=../precompile',
        '../protolibrary/quotation.proto',
    )
)

protoc.main(
    (
        '',
        '-I.',
        '--python_out=../precompile',
        '--grpc_python_out=../precompile',
        '../protolibrary/tradergateway.proto',
    )
)
