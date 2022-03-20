# solc-select use 0.8.7
import web3
from web3 import Web3
from web3._utils.events import get_event_data
import json
import requests
import sys
import time
import pprint
import solcx
from bs4 import BeautifulSoup as bs
from web3.providers.eth_tester import EthereumTesterProvider
from solcx import compile_source
import pandas as pd
from hexbytes import HexBytes
def compile_source_file(file_path):
   with open(file_path, 'r') as f:
	  source = f.read()

   return compile_source(source)
from eth_utils import is_checksum_address
class HexJsonEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, HexBytes):
			return obj.hex()
		return super().default(obj)
infura_url = 'https://polygon-mainnet.infura.io/v3/XXXXXXXXXXXXXX'
web3 = Web3(Web3.HTTPProvider(infura_url))
wallet = '0x38b472c6705F4182dA12a37860D11f9Fa88A257e'
pk = "omitted_key3d97be63a3a650feba26375eea399b3fb1988a63da008a618450e2"

def abi_ftm(contract):
	soup = bs(requests.get(f'https://api.polygonscan.com/api?module=contract&action=getabi&address={contract}&format=raw').content, 'html.parser')
	true = True
	false = False
	return eval(str(soup))
contract = "0x5dcB640Be243aD3967649A4e85f66d3D7C1208Ff"
code_abi = abi_ftm(contract)


account_address = "0xE8F0041FB887D5C8E1e969aaa74659FAd730a741"
contract_address = "0x5dcB640Be243aD3967649A4e85f66d3D7C1208Ff"

account = web3.eth.account.from_key("omitted_key3d97be63a3a650feba26375eea399b3fb1988a63da008a618450e2")
contract = web3.eth.contract(contract_address, abi=code_abi)


def send_nft(address, token_id,secs):
	try:
		del txn_data
	except:
		pass
	gas_price = web3.eth.gas_price
	nonce = web3.eth.get_transaction_count(account.address)
	calldata = contract.encodeABI(fn_name="safeTransferFrom", args=["0x38b472c6705F4182dA12a37860D11f9Fa88A257e",to_address,token_id])
	txn_data = {
	  'from': account.address,
	  'to': contract.address,
	  'nonce': nonce,
	  'value': 0,
	  'data': calldata,
	  'gasPrice': gas_price,
	  'chainId': 80001
	}
	gas = web3.eth.estimate_gas(txn_data)
	txn_data['gas'] = gas
	signed_txn = account.sign_transaction(txn_data)
	transaction = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
	tx_json = json.dumps(transaction, cls=HexJsonEncoder)
	wait_tx = None
	while wait_tx is None:
		time.sleep(secs)
		try:
			wait_tx = web3.eth.get_transaction_receipt(transaction)
			if wait_tx:
				nonce = nonce + 1
		except Exception as e:
			pass
	receipt_row = pd.DataFrame(dict(wait_tx))
	receipt_row = receipt_row[[
							'transactionIndex',
							'type',
							'status',
							'gasUsed',
							'cumulativeGasUsed',
							'effectiveGasPrice',
							'to', 'from',
							'blockNumber',
							'contractAddress',
							'blockHash',
							'logs',
							'logsBloom',
							'transactionHash']]
	return(gas,gas_price,tx_json,receipt_row)

list_addresses = ["0x37Bd7Fab65AdcF0f9Aa3612C58Ae837DadE26b93","0x37Bd7Fab65AdcF0f9Aa3612C58Ae837DadE26b93","0x37Bd7Fab65AdcF0f9Aa3612C58Ae837DadE26b93"]
list_tokens = [40,41,42]

list_txns = []
list_success = []
list_failed = []
list_errors = []
for n, address in enumerate(list_addresses):
	token_id = list_tokens[n]
	try:
		sent = send_nft(address, token_id,3)
		list_txns.append(["success|{}|{}|{}|sent|{}|{}".format(token_id, address,sent[0],sent[1],sent[2]),sent[3].iloc[-1:],sent[3]])
	except Exception as e:
		print(n,e)
		list_failed.append(["failed|{}|{}|{}".format(token_id, address,e),""])
		list_errors.append(e)

list_dfs = []
for n,x in enumerate(list_txns):
	str3 = x[0].split("|")
	x[1]['worked']=str3[0]
	x[1]['nft']=str3[1]
	x[1]['sent_to']=str3[2]
	x[1]['txn_gas']=str3[3]
	x[1]['txn_gasPrice']=str3[5]
	x[1]['txn_hash']=str3[5]
	list_dfs.append(x[1])

final_row = pd.concat(list_dfs)
final_row.to_csv("row.csv")
