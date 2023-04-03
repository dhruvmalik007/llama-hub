# The Graph loader:

This  loader fetches the results from the subgraph given the graph name along with graph user. You must supply your own parameters for subgraph which should be functioning and should be publically available (you can check some of the examples [here](https://thegraph.com/hosted-service), [messari](https://thegraph.com/explorer/profile/0x6fa2bacf752dab6cb6e4b922321f03b4cb61d141?view=Subgraphs&chain=mainnet)).

## Usage

For using this loader, you have to initialize with the 

1. https endpoint for the given subgraph.
2. name of the subgraph as defined 

```python

from llama_index import download_loader

TheGraphReader = download_loader("TheGraphReader")

loader = TheGraphReader(subgraph="uniswap/uniswap-v3", url="https://api.thegraph.com/subgraphs/name/")


query = ````
'''
{
  factories(first: 5) {
    id
    poolCount
    txCount
    totalVolumeUSD
  }
  bundles(first: 5) {
    id
    ethPriceUSD
  }
}
'''

documents = loader.load_data(query);

```

This loader is designed to be used as a way to load data into [LlamaIndex](https://github.com/jerryjliu/gpt_index/tree/main/gpt_index) and/or subsequently used as a Tool in a [LangChain](https://github.com/hwchase17/langchain) Agent. See [here](https://github.com/emptycrown/llama-hub/tree/main) for examples.
