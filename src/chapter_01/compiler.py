#!/usr/bin/env python3
"""
This program compiles a Vyper smart contract and prints:
  - ABI
  - Bytecode (constructor/deployment bytecode)
  - Runtime Bytecode

Usage:
    python compile_vyper.py <path_to_vyper_file>
Example:
    python compile_vyper.py SimpleStorage.vy
"""

import argparse
import sys
import json
from vyper import compile_code

def compile_vyper_contract(file_path: str):
    # Read the source code from the given file.
    try:
        with open(file_path, 'r') as f:
            source_code = f.read()
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(1)
    
    # Compile the Vyper source code.
    # Specify the output_formats as a keyword argument to avoid API errors.
    # The outputs we want: 'abi', 'bytecode', and 'bytecode_runtime'.
    try:
        compiled_data = compile_code(
            source_code,
            output_formats=["abi", "bytecode", "bytecode_runtime"]
        )
    except Exception as e:
        print(f"Compilation error: {e}")
        sys.exit(1)

    return compiled_data

def main():
    # Parse command-line arguments.
    parser = argparse.ArgumentParser(
        description="Compile a Vyper smart contract and display its ABI, bytecode, and runtime bytecode."
    )
    parser.add_argument(
        'file',
        help="Path to the Vyper source file (e.g., SimpleStorage.vy)"
    )
    args = parser.parse_args()

    # Compile the Vyper contract from the specified file.
    compiled = compile_vyper_contract(args.file)

    # Extract the outputs.
    abi = compiled.get("abi")
    bytecode = compiled.get("bytecode")
    runtime_bytecode = compiled.get("bytecode_runtime")

    # Print the outputs in a readable format.
    print("\n=== ABI ===")
    print(json.dumps(abi, indent=2))

    print("\n=== Bytecode ===")
    print(bytecode)

    print("\n=== Runtime Bytecode ===")
    print(runtime_bytecode)

if __name__ == "__main__":
    main()