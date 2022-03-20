![header](header.jpg)

# Is free dumb really free? Yes.
Yo — Get your free Dumb CryptoPunks! Tweet at us [@DumbMeta](https://twitter.com/dumbmeta) or [@DumbCryptoPunks](https://twitter.com/dumbcryptopunks) or tag us in one of your photos on [IG](https://www.instagram.com/dumbcryptopunks/).

This was encouraged by the [OG CryptoPunks tools dev](https://github.com/cryptopunksnotdead) ([reddit thread](https://www.reddit.com/r/dumbmeta/comments/ssfnc9/history_corner_dumb_solpunks_and_crypto_writing/))

Too shy? Create an issue asking for one. Before we jack up the price to $420B (!!!): [OpenSea](https://opensea.io/collection/dumb-cryptopunks), [NFTrade](https://nftrade.com/assets/polygon/0x5dcb640be243ad3967649a4e85f66d3d7c1208ff).

# Sloppy scripts for NFT devs
*More useful & comprehensive NFT scripts may be added over time. Don't hold your breath.*

These are NFT scripts used for [Dumb CryptoPunks](https://dumbcryptopunks.com), an ERC721 NFT on Polygon Network ([contract](https://polygonscan.com/token/0x5dcb640be243ad3967649a4e85f66d3d7c1208ff)). 

They are quintessially hacker scripts - cobbled up and get the job done. They are stripped from the real scripts. The final scripts used by me ([Satire Labs](https://satirelabs.com)) are more robust, but contain multiple workflows for specific use-cases... Also, they contain private data, which I'm too lazy to clean.

- **twitter-giveaway-eth-address.py** - This script is useful for those give NFTs on Twitter. It extracts the ETH address (and other details) of tweets directed to you into a dataframe.
- **track-nft-transactions.py** - This script is useful to keep proper track of how and who you give out your NFTs.
- **random-nft-generator.py** - This script assists you to make the infinite combinations of NFTs possible. CryptoPunks assets are also provided in this repo for your convenience.
- **cryptopunks-attributes-data-structured.csv** - CryptoPunks data is unstructured. All the attributes are listed under one attributes, which is quite annoying. This spreadsheet cleanly separates the 10 attributes (# attributes, hair	, eyes, mouth,	mouth prop,	facial hair, neck, ears, blemishes, nose)
- **nft-multisender.py** - This script helps send your NFTs to a different address programmatically, without MetaMask.
	- There's a pervasive misunderstanding that one must use Solidity (on remix) and create a separate contract. That'd cost a LOT. What can be done instead is simply interacting (writing) on your verified contract and using the transfer function.
	- Hope this script saves you $3000. The only service that provides anything similar costs 1 ETH to use. Kinda expensive imo.

You may run into some issues (eg nft-multisender.py does not implement checks for checksum addresses, no time.sleep > get_transaction_receipts). But if you know how these scripts work, you're smart enough to figure out the rest.