path = """alt_data1/"""
# %%
from os import walk

alt_data_dict = {}
for (dirpath, dirnames, filenames) in walk(path):
    for filename in filenames:
        ticker = filename[filename.find("ITB_") + len("ITB_"):filename.rfind("_daily")].upper() + "-USDT"
        df = pd.read_csv(dirpath + filename)
        df.rename(columns={"DateTime": "datetime", "Price": "price"}, inplace=True)
        df.datetime = pd.to_datetime(df.datetime)
        df["startRange"] = df.datetime
        df.set_index("datetime", inplace=True)
        df = df.sort_index()
        alt_data_dict[ticker] = df
# %%
final_indexes = None
for ticker in alt_data_dict.keys():
    df = alt_data_dict[ticker]
    indexes = list(df.index)
    if final_indexes is None:
        final_indexes = indexes
    final_indexes = list(set(final_indexes) & set(indexes))

for ticker in alt_data_dict.keys():
    df = alt_data_dict[ticker]
    alt_data_dict[ticker] = df[df.index.isin(final_indexes)]
# %%
plt.figure(figsize=(30, 10))
for ticker in alt_data_dict.keys():
    df = alt_data_dict[ticker]
    plt.plot(df.price / np.max(df.price), label=ticker)
    plt.legend()
# %%
ticker = "BUSD-USDT"
df = alt_data_dict[ticker]
plt.figure(figsize=(30, 10))
plt.plot(df.price / np.max(df.price), label=ticker);
plt.legend()
plt.figure(figsize=(30, 10));
# %%
# remove stable coin
_ = alt_data_dict.pop("BUSD-USDT")
# %%
alt_data = AlternativeDataHolder('ad')
alt_data.set_data(alt_data_dict)
# %%
alt_data.tickers
# %%
alt_data.data
# %%
alt_data.get_data("New Addresses")
# %%
alt_data.get_data("Active Addresses")
# %%
alt_data.get_data("Zero Balance Addresses")
# %% md
## example 2
# %% md
You
can
get
required
dataset("altData.zip")
from this link:  https: // disk.yandex.ru / d / DAb1b52cByhA_A
# %%
path = """alt_data2/"""
# %%
from os import walk

# %%
alt_data_dict = {}

for (dirpath, dirnames, filenames) in walk(path):
    for filename in filenames:
        if not ".csv" in filename or "checkpoint" in filename:
            continue
        ticker = filename[:filename.rfind(".csv")].upper() + "-USDT"
        df = pd.read_csv(dirpath + filename)
        df.rename(columns={"time": "datetime", "PriceUSD": "price"}, inplace=True)
        df.datetime = pd.to_datetime(df.datetime)
        df["startRange"] = df.datetime
        df.set_index("datetime", inplace=True)
        df = df.sort_index()
        alt_data_dict[ticker] = df
# %%
to_drop = []
for key in alt_data_dict.keys():
    df = alt_data_dict[key]
    p = df.price.isnull().sum() * 100 / len(df)
    if p > 2:
        print("drop " + key + " because of the percentage of nan data = " + str(p))
        to_drop.append(key)

for drop in to_drop:
    alt_data_dict.pop(drop)
# %%
final_indexes = None
for ticker in alt_data_dict.keys():
    df = alt_data_dict[ticker]
    indexes = list(df.index)
    if final_indexes is None:
        final_indexes = indexes
    final_indexes = list(set(final_indexes) & set(indexes))

for ticker in alt_data_dict.keys():
    df = alt_data_dict[ticker]
    alt_data_dict[ticker] = df[df.index.isin(final_indexes)]
# %%
final_columns = None
for ticker in alt_data_dict.keys():
    df = alt_data_dict[ticker]
    columns = list(df.columns)
    if final_columns is None:
        final_columns = columns
    final_columns = list(set(final_columns) & set(columns))

for ticker in alt_data_dict.keys():
    df = alt_data_dict[ticker]
    new_df = copy.deepcopy(df)
    for column in df.columns:
        if not column in final_columns:
            new_df.drop(columns=[column], inplace=True)
    alt_data_dict[ticker] = new_df
# %%
for key in alt_data_dict.keys():
    print(len(alt_data_dict[key]))
# %%
alt_data = AlternativeDataHolder('ad')
alt_data.set_data(alt_data_dict)
# %%
alt_data.tickers
# %%
list(alt_data.data['ICP-USDT'].columns)
# %%
alt_data.get_data("price")
# %%
alt_data.get_data('TxCnt')
# %%
alt_data.get_data('AssetEODCompletionTime')
# %%

# %%
