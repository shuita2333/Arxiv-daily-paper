# 🧠 大模型相关研究 | 2026年09月02日

> 本类共 **452** 篇论文：已确认 **431** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**451-452**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-452**

---

### 451. [TSPFN: A Temporal Tabular Foundation Model for Physiological Time Series Classification](https://arxiv.org/abs/2608.31013)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jérémie Stym-Popper, Clément Rambour, Federica Granese 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing models that generalize effectively in low- to medium-data regimes remains a primary challenge in medical machine learning, particularly for physiological time-series classification. While tabular foundation models such as TabPFN offer an attractive alternative to conventional fine-tuning through in-context learning, they are not designed to capture the temporal dependencies inherent to physiological signals. ~In this paper, we introduce TSPFN, a foundation model that redesigns TabPFN's architecture for time series data. TSPFN integrates structured temporal representations and positional embeddings to capture intra-sample temporal and channel dependencies. To fully leverage its spatio-temporal design, the model is pretrained on 140,000 real-world physiological time series across multiple medical domains. This yields a unified, generalizable framework capable of learning the specificities of medical time series. Experiments across diverse physiological benchmarks demonstrate that TSPFN consistently outperforms standard tabular baselines and TabPFN, and achieves superior cross-domain generalization compared to specialized deep time-series models. All our experiments, ablation studies, and pre-processing scheme are publicly available at this https URL

---


### 452. [Stress-Testing Efficient Responsible-AI Evaluation: When Compute Savings Change Benchmark Conclusions](https://arxiv.org/abs/2608.31108)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ahmed El Kady, Aravind Narayanan, Rehana Noorani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient evaluation changes the protocol used to support claims about model behavior, yet it is rarely tested whether those claims remain stable after the evaluation itself is made cheaper. We stress-test conclusion robustness in responsible-AI benchmarking by evaluating three dense and mixture-of-experts models on BBQ and BBQ-V under seven conditions spanning batching, quantization, benchmark reduction, and their combinations. Rather than treating preserved aggregate accuracy as sufficient, we compare accuracy, bias severity and prevalence, reasoning quality, subgroup behavior, subset-membership stability, runtime, and measured GPU energy against a full-benchmark BF16 baseline. Larger batching keeps accuracy within 0.35 percentage points of baseline and produces comparatively small subgroup changes, while reducing energy in five of six model--dataset settings. INT8 largely preserves quality but uses 1.79--4.26$\times$ baseline energy. INT4 causes larger, model- and context-dependent changes. Reduced benchmarks provide the most consistent savings, but very small subsets are substantially more sensitive to which items are retained. Efficient evaluation should therefore be treated as a measurement intervention whose validity must be checked across the conclusions the benchmark is intended to support. Our project website is this https URL and the code is available at this https URL.

---


> [!TIP]
> 当前位于：**451-452**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-452**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
