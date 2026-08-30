# 📦 其他研究 | 2026年08月31日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-202**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-202**

---

### 201. [Beyond F1: Evaluating Coverage and Failure Recovery in AI Model Security Scanners](https://arxiv.org/abs/2608.27424)

**<font color=#1a73e8>作者：</font>** Qianlong Lan, Vinothini Pandurangan, Anuj Kaul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static scanners are increasingly used to identify executable or otherwise unsafe content in machine- learning artifacts, yet conventional evaluation metrics characterize only cases where a scanner yields a usable security judgment. We evaluate ModelScan, ModelAudit, and Fickling using a controlled, artifact-backed benchmark on a synthetic corpus of 170 Pickle and PyTorch focused artifacts across 145 specimen families, 135 of which have binary security ground truth and 10 of which are intentionally malformed without labels. We explicitly distinguish non-N/A coverage, analysis completion, definitive security decisions, non-security findings, and unsupported outcomes. On labeled families, ModelAudit produced definitive security decisions for all 135 families (100%), Fickling for 110 (81.5%), and ModelScan for 67 (49.6%). Conditional on making a definitive judgment, ModelScan achieved 100% precision, recall, and F1. Fickling identified no unique true- positive families beyond those found by the combination of ModelAudit and ModelScan. Furthermore, for the 48 malicious families where ModelScan failed to complete its analysis, both ModelAudit and Fickling generated detections consistent with ground truth. These findings underscore the need to separate judgment accuracy from judgment availability, as well as incremental detection coverage from tool-level redundancy.

---


### 202. [Mechanistic Reaction Prediction via Discrete Flow Matching on Graph-Structured Electron Occupation](https://arxiv.org/abs/2608.27429)

**<font color=#1a73e8>作者：</font>** Nguyen Xuan-Vu, Octavian Susanu, Daniel Armstrong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chemical reactions are fundamentally transformations in electron space, yet most machine learning approaches model them either through \textit{de novo} generation of product molecules or through heuristic graph edits that operate directly on molecular topology.
We introduce MAELLE (\textbf{M}ech\textbf{A}nistic \textbf{E}dit f\textbf{L}ow-matching on e\textbf{L}ectron r\textbf{E}arrangements), which instead models reactions as discrete flow matching over electron occupation vectors.
Concretely, we formulate the reactant-to-product mapping as a Continuous-time Markov Chain (CTMC) over the graph-structured integer-valued electron occupation space defined on all bonding, non-bonding, and hydrogen sites.
To construct the intermediate edit trajectories, we generalize the discrete flow matching mixture path to discrete electron rearrangements using Optimal Transport, yielding a sequence of mechanistically interpretable edit moves without requiring elementary step annotations.
MAELLE achieves competitive performance on the USPTO-480K benchmark compared with leading reaction prediction models.
Beyond in-distribution accuracy, we evaluate robustness across two out-of-distribution settings - structural complexity and reaction type - and find that MAELLE maintains strong performance where existing methods degrade.
Finally, because the learned flow operates over the full electron redistribution, MAELLE naturally recovers mechanistic trajectories that align with known chemistry and can predict side products of a reaction.

---


> [!TIP]
> 当前位于：**201-202**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-202**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
