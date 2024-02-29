![Bali Blockchain](_bali_.jpg)




<br />



![On-Chain Messaging](_Alice_Bob_.png)



<br />


```json:

class Chain :
    
    def __init__(self, change_of_state="initialized methods chaining") :
        self.change_of_state = change_of_state
        return None
    
    def setKeypair(self) :
        self.change_of_state = "new keypair"
        return self
    
    def setBootstrap(self) :
        self.change_of_state = "estalish bootstrap"
        return self
    
    def setPeersDiscovery(self) :
        self.change_of_state = "Peers list discovery"
        return self
    
    def setLiveNetwork(self) :
        self.change_of_state = "connect to live! market"
        return self
    
    def setInventory(self) :
        self.change_of_state = "fetch Block height"
        return self
    
    def setDownload(self) :
        self.change_of_state = "downloading block #"
        return self
    
    def setConsensus(self) :
        self.change_of_state = "establish Consensus Governance"
        return self




>>> c =  Chain()
>>> c.change_of_state
'initialized methods chaining'
>>> 
>>> 
>>> 
>>> 
>>> c.setKeypair().setBootstrap()
<__main__.Chain object at 0x7f69149b83a0>
>>> 
>>> c.change_of_state
'estalish bootstrap'
>>> 
>>> 
>>> 
>>> 
>>> c.setPeersDiscovery().setLiveNetwork().setInventory().setDownload().setConsensus()
<__main__.Chain object at 0x7f69149b83a0>
>>> 
>>> c.change_of_state
'establish Consensus Governance'

```


<br />



![message ecryption](_message_.png)



<br />



##   MM : Money! Maker



```json:

Block
{
    #  Need To Know basis
    #  Confidential
    #  between Alice & Bob

    "block_height" : 0,
    "header_hash"  : "",

    "header" : {
        "version" : "",
        "brand" : "Money! Maker",
        "chunk_count" : 3,
        "checksum" : "",
        "nonce" : "",
        "timestamp" : 0,
    },

    #  download & sync
    #  locked shields & stealth

    #  only Alice & Bob
    #  can decipher

    #  No Need Storage Fee

    "chunk" : [
        {
            "000" : "32-bytes"
        },
        {
            "001" : "32-bytes"
        },
        {
            "002" : "32-bytes"
        },
    ],
}

```



<br />



```json:

on-chain Auction
New Account Activation =
{
    "sell 1 MM" : "buy 1 IDR",
    "holders" : 100,
    "minimal buy" : 1.000.000 IDR",
    "scarcity" : "100.000.000. IDR"
}

```


<br />


```json:

Exchange Rate =
{
    "1 XLM" : "2.000 IDR",
}

```


<br />


```

  1st deliverable
  Android based smartphone

  retrieve encrypted Message
  Hidden & Isolated endpoint

  New Account Activation 
  Minimal Balance 
  1.000.000 IDR

  All Operations
  Instant Liquidity

  Storage
  relevant end-to-end Replication

  KYC
  Know You Client
  Must provide Real Name

  Preserving Privacy
  Assets Values Holdings

```
