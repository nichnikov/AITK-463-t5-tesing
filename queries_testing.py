import os
import re
import pandas as pd
import requests

queies_df = pd.read_csv(os.path.join("data", "test_queries.csv"), sep="\t")
print(queies_df)
queies_dicts = queies_df.to_dict(orient="records")
test_results = []
for num, d in enumerate(queies_dicts):
    print(num, "/", len(queies_dicts))
    # q = d["Query"]
    q_request = {"pubid": 9, "text": re.sub("\n", " ", d["Query"])}
    res = requests.post("http://0.0.0.0:8090/api/search", json=q_request)
    # res = requests.post("http://srv01.nlp.dev.msk2.sl.amedia.tech:4011/api/search", json=q_request)
    res_dict = {**d, **res.json()}
    test_results.append(res_dict)

test_results_df = pd.DataFrame(test_results)
print(test_results_df)
test_results_df.to_csv(os.path.join("results", "all_sys_with_answers.csv"), sep="\t", index=False)