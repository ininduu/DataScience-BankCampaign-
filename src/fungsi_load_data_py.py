def read_with_sniff(path):
  with open(path, 'r', encoding='utf-8', errors='replace') as f:
    sample = f.read()
    f.seek(0)
    try:
      dialect = csv.Sniffer().sniff(sample, delimiters=[',', ';', '\t', '|'])
      delim = dialect.delimiter
    except Exception:
      delim = ';'

  df = pd.read_csv(path, sep=delim)
  return df, delim

bank, delim1 = read_with_sniff("/content/drive/MyDrive/bank.csv")
bank