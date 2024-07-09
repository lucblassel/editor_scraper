from tqdm import tqdm
from glob import glob
import json

if __name__ == "__main__":
    table = str.maketrans("[]_", "() ")
    with open("README.md", "w") as output:
        for file in tqdm(glob("res/*.json")):
            with open(file, "r") as js:
                res = json.load(js)

            fname = file.removesuffix(".json").removeprefix("res/").translate(table)
            output.write(f"## {fname}\n")

            for r in res["organic_results"][:3]:
                t = r["title"]
                blurb = r["snippet"]
                l = r["link"]
                output.write(f" - [{t}]({l}) : {blurb}  \n")

            output.write("\n\n")
