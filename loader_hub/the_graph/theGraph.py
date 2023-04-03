'''
This script does demo for reading the graph data from various subgraphs deployed by given holder
'''

import requests
from typing import Any, List, Optional



from llama_index.readers.base import BaseReader
from llama_index.readers.schema.base import Document

class TheGraphReader(BaseReader):
    """ class to read  data from specfic sub-graph given the value.
    Args:
        subgraph (str): {subgraph}/{name} eg: uniswap/uniswap-v3 or  {  subgraphs/id/{subgraphId} 
        

    eg: messari/uniswap-v3
```
    """

    def __init__(
        self,
        subgraph: str,
        url: str,
    ) -> None:
        """Initialize with parameters."""
        super().__init__()
        self.subgraph = subgraph
        self.url = url
    
    '''
    query (str): is the graphQL query description that you want to execute for the subgraph selected already. 
e.g 
    query = ```
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

```
    '''
    def load_data(self, _query) -> List[Document]:
        """Load data from The Graph."""
        query = _query
        urlComplete = self.url + self.subgraph
        response = requests.post(urlComplete, headers= {'Content-Type': 'application/json'} ,  json={"query": query})
        results = response.json()
        return results


