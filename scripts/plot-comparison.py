import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import common

plt.figure(figsize=(4,2))

summary = pd.read_table(snakemake.input[0])
bio_related = summary.shape[0] - (summary["not_bio_related"] == "x").sum()
# Counts from October 2017
pkg_counts = pd.DataFrame.from_dict({
    "Bioconda": bio_related,
    "Debian Med": 882,
    "Homebrew Science": 622,
    "Gentoo Science": 480,
    "Biolinux": 308,
    "BioBuilds": 118}, orient="index").reset_index()
pkg_counts.columns = ["source", "count"]

sns.barplot(x="source", y="count", data=pkg_counts)
plt.xticks(rotation=45, ha="right")
plt.xlabel("")
plt.ylabel("packages")

# set maximum tick to be that of bioconda
yticks = plt.gca().get_yticks()
yticks[-1] = bio_related
plt.gca().set_yticks(yticks)

sns.despine()
plt.savefig(snakemake.output[0], bbox_inches="tight")
