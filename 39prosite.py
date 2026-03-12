#instead of using _ in _, use re.search

pat = '(C.{2,4]C.{3}[LIVMFYWC].{8}H.{3,4}H)'     #pattern is now a variable
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    m = re.search(pat, seq)
    if m: print(m.group(1))