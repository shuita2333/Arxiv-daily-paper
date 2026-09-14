# 🧠 大模型相关研究 | 2026年09月14日

> 本类共 **153** 篇论文：已确认 **145** 篇，待复核 **8** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-153**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-153**

---

### 151. [Target leakage, not model class, explains reported accuracy in survey-based cardiovascular screening: a leakage-tiered audit of glass-box and tabular foundation models](https://arxiv.org/abs/2609.11838)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Raad Bin Tareaf, Murad Al-Rajab, Samia Loucif 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cardiovascular screening models trained on national health surveys routinely report areas under the receiver operating characteristic curve (AUROC) near 0.89. We asked whether that accuracy reflects learning or target leakage, whether tabular foundation models change the answer, and whether the properties deployment requires survive joint examination. We benchmarked ten classifiers spanning linear, tree-ensemble, neural, glass-box, and tabular foundation classes for prevalent myocardial infarction in 442,067 respondents of the 2022 Behavioral Risk Factor Surveillance System across five feature tiers of decreasing leakage risk. Each was audited for discrimination, calibration, fairness at an explicit screening threshold, conformal coverage, explanation faithfulness, and inference cost, then applied -- models and thresholds frozen -- to 430,755 respondents of 2023. Removing two post-diagnostic features cost every model 0.049-0.051 AUROC, collapsing the field into a 0.0045-wide band. The glass-box explainable boosting machine was non-inferior to every alternative within a pre-specified 0.005 margin while scoring the cohort roughly 104 times faster than the strongest foundation model. One threshold detected 75.4% of women's infarctions against 89.0% of men's; editing the model's shape functions reduced the gap to 0.010. Marginal conformal prediction gave 0.86 coverage to men and 0.82 to adults over 60; Mondrian calibration repaired every stratum. Frozen models transported within 0.002 AUROC. Reported headroom in this literature is a property of the feature set, not the learner. Transparency cost nothing measurable and made fairness repair and uncertainty conditioning directly auditable. Evaluation practice, not model capacity, is the binding constraint.

---


### 152. [CausalArena: Benchmarking Causal Discovery in the Foundation Model Era](https://arxiv.org/abs/2609.11897)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zi-Rong Li, Si-Yang Liu, Tian-Zuo Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery aims to uncover causal structures from data and is fundamental to scientific reasoning and intervention-based decision making. Its evaluation relies heavily on structural causal models (SCMs), which specify a causal graph together with the mechanisms that generate data, yet existing studies differ substantially in graph families, mechanisms, and evaluation protocols. The emergence of causal discovery foundation models (CDFMs) further complicates evaluation: performance may reflect not only causal discovery ability, but also overlap between pretraining environments and test SCMs, making results on fixed synthetic benchmarks difficult to interpret. We introduce CausalArena, a unified and evolvable benchmark for causal discovery under a common protocol. Synthetic SCMs supply controlled breadth over structures and mechanisms; semantic operational SCMs provide human-auditable, semantically grounded environments beyond standard synthetic generators; and formula-grounded SCMs test discovery under explicit scientific mechanisms. Public real-world datasets provide an additional external-validity check. Experiments across classical, neural, and pretrained methods reveal substantial ranking shifts across SCM families and protocols, showing that strong performance in one benchmark regime does not reliably transfer to others. These results highlight benchmark diversity and pretraining--evaluation overlap as central challenges for evaluating causal discovery in the foundation model era.

---


### 153. [SenseNova-U1.5: Towards Native Unified Visual Intelligence](https://arxiv.org/abs/2609.11929)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haiwen Diao, Jiahao Wang, Chenjing Ding 等 65 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We launch SenseNova-U1.5, an 8B-MoT native unified multimodal model that understands, reasons about, and generates visual content within an encoder-free and VAE-free architecture. We strengthen its visual interface through spatially coherent patch reconstruction and scale its training with carefully curated generation and editing data, improved task formulation, structural prompt enhancement, and native resolutions of up to 4K. For post-training, we optimize specialized experts for visual aesthetics, bilingual text rendering, infographic generation, and image editing, and consolidate their capabilities through multi-expert on-policy distillation. Across extensive evaluations, SenseNova-U1.5 largely advances image fidelity, text rendering, complex composition, multi-reference editing, and interleaved generation, while improving instruction following and preserving subject identity, geometry, and unmodified regions. Despite limited exposure to structured formats in its generation data, SenseNova-U1.5 generalizes effectively to long, complex, and structured visual instructions, further proving that multimodal understanding can transfer to visual planning and creation. Together, these findings position native unified modelling as a promising path towards systems that perceive, reason and create within a fully end-to-end framework. We will open-source training code, including supervised fine-tuning, reinforcement learning, and on-policy distillation.

---


> [!TIP]
> 当前位于：**151-153**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-153**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
