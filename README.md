# smart_contract_python

2025.05.07: chapter_05

// to download the necessary plugins of ape

``` bash
python3 -m pip install eth-ape'[recommended-plugins]'
```

// Check installed plugins

``` bash
ape plugins list
```

//Check specific plugin versions

``` bash
pip show ape-vyper ape-solidity ape-infura
```

// initialise the simple_storage project

``` bash
ape init simple_storage
```

```bash
geth attach /tmp/geth.ipc
```

// under chapter_05/simple_storage/contracts

// 1. Direct path by contract name

``` bash
jq '.contractTypes.simple_storage.deploymentBytecode.bytecode' \
   .build/__local__.json
```

// 2. Generic path for any contract

``` bash
jq '.contractTypes[] | .deploymentBytecode.bytecode' .build/__local__.json
```

// Inspect available keys first

``` bash
jq 'keys' .build/__local__.json
# → ["compilers","contractTypes","manifest","sources"]

jq '.contractTypes | keys' .build/__local__.json
# → ["simple_storage"]
```

``` bash
web3.fromWei(eth.getBalance("0xDDfB8D83dc87f5f0B9252119584040DB35acFe1A"))

web3.fromWei(eth.getBalance("0x1b054EA9026E9354E8EC41eA733598bCF3BCafE0"))
```

``` bash
0x1b054EA9026E9354E8EC41eA733598bCF3BCafE0
```

``` bash
mykey/UTC--2025-05-07T15-52-02.599585000Z--1b054ea9026e9354e8ec41ea733598bcf3bcafe0
```
