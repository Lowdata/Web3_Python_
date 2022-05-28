from charset_normalizer import from_path


from solc import compile_standard

with open("./SimpleStorage", "r") as file:
    simple_storage_file = file.read()

#adding the compiler for solidity

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol":{"content":simple_storage_file}},
        "settings": {
            "outputSelection":{
                "*":{
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]

                }
            }

        }

    }
    solc_version="0.6.0"
)
print(compiled_sol)