# 📦 其他研究 | 2026年04月28日

> 本类共 **154** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-154**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-154**

---

### 151. [Long-tail Internet photo reconstruction](https://arxiv.org/abs/2604.22714)

**<font color=#1a73e8>作者：</font>** Yuan Li, Yuanbo Xiangli, Hadar Averbuch-Elor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Internet photo collections exhibit an extremely long-tailed distribution: a few famous landmarks are densely photographed and easily reconstructed in 3D, while most real-world sites are represented with sparse, noisy, uneven imagery beyond the capabilities of both classical and learned 3D methods. We believe that tackling this long-tail regime represents one of the next frontiers for 3D foundation models. Although reliable ground-truth 3D supervision from sparse scenes is challenging to acquire, we observe that it can be effectively simulated by sampling sparse subsets from well-reconstructed Internet landmarks. To this end, we introduce MegaDepth-X, a large dataset of 3D reconstructions with clean, dense depth, together with a strategy for sampling sets of training images that mimic camera distributions in long-tail scenes. Finetuning 3D foundation models with these components yields robust reconstructions under extreme sparsity, and also enables more reliable reconstruction in symmetric and repetitive scenes, while preserving generalization to standard, dense 3D benchmark datasets.

---


### 152. [Zero-Shot Morphological Discovery in Low-Resource Bantu Languages via Cross-Lingual Transfer and Unsupervised Clustering](https://arxiv.org/abs/2604.22723)

**<font color=#1a73e8>作者：</font>** Hillary Mutisya, John Mugane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a method for discovering morphological features in low-resource Bantu languages by combining cross-lingual transfer learning with unsupervised clustering. Applied to Giriama (nyf), a language with only 91 labeled paradigms, our pipeline discovers noun class assignments for 2,455 words and identifies two previously undocumented morphological patterns: an a- prefix variant for Class 2 (vowel coalescence - the merger of two adjacent vowels - of wa-, 95.1% consistency) and a contracted k'- prefix (98.5% consistency). External validation on 444 known Giriama verb paradigms confirms 78.2% lemmatization accuracy, while a v3 corpus expansion to 19,624 words (9,014 unique lemmas) achieves 97.3% segmentation and 86.7% lemmatization rates across all major word classes. Our ensemble of transfer learning from Swahili and unsupervised clustering, combined via weighted voting, exploits complementary strengths: transfer excels at cognate detection (leveraging ~60% vocabulary overlap) while clustering discovers language-specific innovations invisible to transfer. We release all code and discovered lexicons to support morphological documentation for low-resource Bantu languages.

---


### 153. [Neural Recovery of Historical Lexical Structure in Bantu Languages from Modern Data](https://arxiv.org/abs/2604.22730)

**<font color=#1a73e8>作者：</font>** Hillary Mutisya, John Mugane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether neural models trained exclusively on modern morphological data can recover cross-lingual lexical structure consistent with historical reconstruction. Using BantuMorph v7, a transformer over Bantu morphological paradigms, we analyze 14 Eastern and Southern Bantu languages, extract encoder embeddings for their noun and verb lemmas, and identify 728 noun and 1,525 verb cognate candidates shared across 5+ languages. Evaluating these candidates against established historical resources-the Bantu Lexical Reconstructions database (BLR3; 4,786 reconstructed Proto-Bantu forms) and the ASJP basic vocabulary-we confirm 10 of the top 11 noun candidates (90.9%) align with previously reconstructed Proto-Bantu forms, including *-ntU 'person' (8 languages), *gombe 'cow' (9 languages), and *mUn (9 languages). Extending to verbs, 12 verb cognates align with reconstructed Proto-Bantu roots, including *-bon- 'see' and *-jIm- 'stand', each attested across wide geographic ranges. Cross-model validation using an independent translation model (NLLB-600M) confirms these patterns: both models recover cognate clusters and phylogenetic groupings consistent with established Guthrie-zone classifications (p < 0.01). Cross-lingual noun class analysis reveals that all 13 productive classes maintain >0.83 cosine similarity across languages (within-class > between-class, p < 10^-9). Our dataset is restricted to Eastern and Southern Bantu, so we interpret these results as recovering shared Bantu lexical structure consistent with Proto-Bantu rather than definitively distinguishing Proto-Bantu retentions from later regional innovations.

---


### 154. [Spend Less, Fit Better: Budget-Efficient Scaling Law Fitting via Active Experiment Selection](https://arxiv.org/abs/2604.22753)

**<font color=#1a73e8>作者：</font>** Sijie Li, Shanda Li, Haowei Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws are used to plan multi-million-dollar training runs, but fitting those laws can itself cost millions. In modern large-scale workflows, assembling a sufficiently informative set of pilot experiments is already a major budget-allocation problem rather than a routine preprocessing step. We formulate scaling-law fitting as budget-aware sequential experimental design: given a finite pool of runnable experiments with heterogeneous costs, choose which runs to execute so as to maximize extrapolation accuracy in a high-cost target region. We then propose an uncertainty-aware method for sequentially allocating experimental budget toward the runs most useful for target-region extrapolation. Across a diverse benchmark of scaling-law tasks, our method consistently outperforms classical design-based baselines, and often approaches the performance of fitting on the full experimental set while using only about 10% of the total training budget. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**151-154**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-154**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
