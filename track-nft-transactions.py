import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pygsheets

block_no = 25689501

chunke_txn2 = requests.get("https://api.polygonscan.com/api?module=account&action=tokennfttx&contractaddress=0x5dcb640be243ad3967649a4e85f66d3d7c1208ff&address=0xE8F0041FB887D5C8E1e969aaa74659FAd730a741&startblock={} &endblock=35473986&page=1&offset=1000&sort=asc&apikey=22E38ZKNI6A5WYXCFJCTKCWUA3Q5XMYIVR&sort=asc&format=raw".format(block_no))

satire_txn2 = bs(chunke_txn2.content, 'html.parser')
contract_wallet = "0x5dcB640Be243aD3967649A4e85f66d3D7C1208Ff"
chunke_wallet = "0xE8F0041FB887D5C8E1e969aaa74659FAd730a741"

list_chunke = []
for n,x in enumerate(eval(str(satire_txn2))['result']):
    row_df = pd.DataFrame([x])
df_all = pd.concat(list_chunke)

txn_cols = [
            'timeStamp',
            'from',
            'to',
            'tokenID',
            'blockNumber',
            'hash',
            'nonce',
            'blockHash',
            'contractAddress',
            'tokenName',
            'tokenSymbol',
            'tokenDecimal',
            'transactionIndex',
            'gas',
            'gasPrice',
            'gasUsed',
            'cumulativeGasUsed',
            'input',
            'confirmations'
            ]

df_all = df_all[txn_cols]
df_all = df_all.sort_values("timeStamp")
df_all.to_csv("all_txn2.csv")

gc = pygsheets.authorize(service_file=gspread_keyfile)
sh = gc.open_by_key(sheet_id)
def write_to_gsheet(service_file_path, spreadsheet_id, sheet_name, data_df):
    """
    this function takes data_df and writes it under spreadsheet_id
    and sheet_name using your credentials under service_file_path
    """
    try:
        sh.add_worksheet(sheet_name)
    except:
        pass
    wks_write = sh.worksheet_by_title(sheet_name)
    wks_write.clear('A1',None,'*')
    wks_write.set_dataframe(data_df, (1,1), encoding='utf-8', fit=True)
    wks_write.frozen_rows = 1

def read_gsheet(service_file_path, spreadsheet_id, sheet_name, data_df):
    try:
        sh.add_worksheet(sheet_name)
    except:
        pass
    wks_write = sh.worksheet_by_title(sheet_name)
    wks_write.clear('A1',None,'*')
    wks_write.set_dataframe(data_df, (1,1), encoding='utf-8', fit=True)
    wks_write.frozen_rows = 1

gspread_keyfile = "[omitted]"
sheet_id = "[omitted]"
sheet_name = "temp"
write_to_gsheet(gspread_keyfile, sheet_id, sheet_name, df_all)