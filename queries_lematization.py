import os
import re
import pandas as pd
from src.start import tokenizer

qrs_df = pd.read_csv(os.path.join("results", "all_sys_with_answers.csv"), sep="\t")
print(qrs_df)
qrs_df["Query"] = qrs_df["Query"].apply(lambda tx: re.sub("\n", " ", tx))
print(list(qrs_df["Query"])[:5])
qrs_df["lm_query"] = qrs_df["Query"].apply(lambda tx: " ".join(tokenizer([tx])[0]))
print(qrs_df)
"""
lm_queries = [" ".join(tx) for tx in tokenizer(qrs_df["Query"])]
print(lm_queries[:5])
print(len(lm_queries))
lm_queries_df = pd.DataFrame(lm_queries, columns=["lm_query"])
print(lm_queries_df)
qrs_lem_qrs_df = pd.concat([qrs_df, lm_queries_df], axis=1)
print(qrs_lem_qrs_df)
qrs_lem_qrs_df.to_csv(os.path.join("results", "all_sys_with_answers_lm_qrs.csv"), sep="\t", index=False)
"""
qrs_df.to_csv(os.path.join("results", "all_sys_with_answers_lm_qrs.csv"), sep="\t", index=False)