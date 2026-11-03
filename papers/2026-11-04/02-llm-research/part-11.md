# 🧠 大模型相关研究 | 2026年11月04日

> 本类共 **515** 篇论文：已确认 **481** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**501-515**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-515**

---

### 501. [SensOFormer: Foundation Models for Particle Accelerators](https://arxiv.org/abs/2611.02031)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mahindra Rautela, Alexander Scheinker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale scientific facilities, such as particle accelerators, are complex systems composed of thousands of interacting components that must operate collectively to support diagnostics and control, and ensure safe, reliable operation. These facilities rely on extensive sensor networks that generate large volumes of heterogeneous, incomplete, and noisy telemetry, often sampled at different rates across subsystems. In this paper, we adopt the foundation-model paradigm to learn general-purpose sensor representations from historical accelerator data through self-supervised pretraining. We introduce SensOFormer, a denoising masked transformer with a Perceiver-style encoder-decoder architecture designed to handle variable sensor sets, accommodate heterogeneous sampling rates, and learn robust representations from noisy measurements. The model is pretrained on multiple particle-accelerator datasets and transferred to downstream tasks, including missing-data imputation, anomaly detection, cavity identification, and fault identification. Through extensive evaluations and comparisons, we demonstrate that a single self-supervised model can learn reusable representations for diverse operational tasks in large-scale scientific facilities. Project page: this https URL.

---


### 502. [Attribution-based diagnostics for single-cell foundation models](https://arxiv.org/abs/2611.02335)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Farnoush Rezaei Jafari, Tristan Lazard, Kenza Bouzid 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell RNA foundation models (scFMs) are increasingly used for in-silico biological discovery, yet predictive performance alone does not reveal whether their decisions rely on biologically meaningful signals or model-specific shortcuts. We systematically investigate post-hoc attribution of downstream predictions across two tasks: cell-type annotation using pretrained Cell2Sentence and scGPT models, and perturbation prediction using scGPT+STATE in a controlled setting. For cell annotation, we use attribution to assess whether predictions rely on established marker genes and how their relevance varies with model architecture, expression rank, and the surrounding cellular context. For perturbation prediction, we compare attribution patterns with known regulatory ground-truth in a synthetic setting to assess what they reveal about the model's learned computations. Across these tasks, attribution reveals biological feature use, contextual interactions, contributions from different input pathways, learning progression, associations with prediction quality, and potential pitfalls that are not fully captured by standard performance metrics. Experiments with complete and limited regulatory knowledge further demonstrate that conclusions drawn from attribution depend strongly on the choice of biological reference, baseline, and null model. Together, these findings highlight the value of attribution as a flexible post-hoc diagnostic for understanding model behavior, identifying potential issues, and informing the development of scFMs.

---


### 503. [Do Visual RL Gains Scale at Test Time? A Quantile View of Post-Training](https://arxiv.org/abs/2611.02366)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Austin Wang, Lexing Ying  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training improves the single-sample quality of visual generative models, but deployment often provides additional inference compute through Best-of-N sampling. Whether RL gains transfer under such test-time scaling, particularly on difficult held-out tasks, remains poorly understood in the visual domain. Our central contribution is to systematically identify and characterize a failure mode of scaling transfer in visual RL: across multiple RL methods, model backbones, and evaluations spanning compositional generation, text rendering, and preference alignment, higher single-sample reward does not necessarily imply a better quality-compute frontier. RL gains may attenuate, saturate, or even reverse at large sampling budgets, with the base model eventually outperforming its post-trained counterpart. We explain these regimes through a quantile-transfer framework, showing that Best-of-N places increasing weight on the upper tail of the reward distribution as N grows. Consequently, RL can improve typical samples while compressing or degrading the rare high-quality outcomes that test-time scaling exploits. As a simple intervention motivated by this analysis, we introduce Quantile Utility Policy Optimization (QUPO), which optimizes a controllable mixture of quantile utilities corresponding to different inference budgets. Experiments on SD3.5-M and BAGEL show that QUPO better preserves upper-tail quality and substantially improves scaling on challenging held-out prompts relative to standard RL post-training. Our results suggest that visual generative models should be evaluated and optimized not only for single-sample quality, but for how post-training reshapes the full reward distribution that inference-time scaling exploits.

---


### 504. [M3Former: Fine-Grained Cross-Layer Mixing for Transformers](https://arxiv.org/abs/2611.02436)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiasong Han, Yunkai Chai, Tong Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual connections give each Transformer block access to all earlier layers only through one fixed sum, broadcast to all of the block's inputs. This broadcast bottleneck imposes three constraints: the query, key, value and residual inputs of a block, which we call its roles, read the same vector; all hidden dimensions within a role share one set of weights over earlier layers; and every earlier layer has the same fixed weight for every token. We propose the Multi-Role Multi-Group Mixing Residual (M3), which removes all three: every role, and every group of hidden dimensions within a role, reads its own token-dependent mixture of all earlier layers. M3 starts as an exact residual connection and adds as little as 1.4% parameters and 1.8% FLOPs. From 100M to 1.4B parameters, M3Former outperforms the Transformer and coarse-grained cross-layer connections at every size, matching a Transformer 1.19-1.34x the size of the one it modifies, trained with 1.4-1.8x the compute. Relaxing only some of the constraints recovers only part of this gain. M3Former also improves sparse mixture-of-experts models of up to 4.6B parameters and trains more stably in deeper networks. Code: this https URL

---


### 505. [When Prediction Shapes the Future: A BlueSky Agenda for Reflexive Time Series Analysis](https://arxiv.org/abs/2611.02511)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tao Xie, Yiqun Zhang, Yiu-ming Cheung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time-series models are increasingly deployed in operational systems (e.g., inventory management and clinical care) where predictions trigger interventions that alter future observations, producing records we term AI-shaped trajectories. This sequence-prediction coupling deepens as such systems evolve into agents that autonomously predict, act, and remember across long horizons. Such AI-shaped trajectories support immediate performance monitoring, but turn ambiguous once reused as passive data. An algorithm may then misread a prediction-prevented stockout as naturally stable demand, or an averted medical crisis as a false alarm. This ambiguity then propagates into everything built on the record, from retraining and agent memory to downstream predictive tasks. As a result, systems may internalize these intervention effects as natural phenomena, drifting further from the truth at every closed-loop cycle. In this Blue Sky paper, we advocate an agenda for reflexive time-series analysis that shifts the analytical object from the intervention-agnostic sequence to the prediction-action-observation loop. The agenda requires closed-loop provenance to track the operational context (e.g., predictions, policies, and actions), sequence identification to estimate how those actions affect future values under explicit causal assumptions, and closed-loop evaluation to separate intrinsic process prediction from policy-driven effects. This foundation is essential for integrating autonomous agents into such loops at scale, enabling the joint learning of intervention effects and intrinsic dynamics for robust temporal representations.

---


### 506. [Parallelism-Aligned Pruning and Round-Aware Context Reuse for On-Device Multimodal Agents](https://arxiv.org/abs/2611.02601)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Peipei Jiao, Mingkang Liu, Weiming Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-device multimodal agents are limited by two deployment mismatches: pretrained attention structures may not divide evenly across the compute cores of an edge accelerator, causing irregular partitions; and standard prefix caching keeps historical visual tokens in the persistent KV cache, whose capacity grows with the number of rounds. We present PARC, which combines parallelism-aligned structured pruning with lifetime-aware KV-cache reorganization. At the model level, it uses first-order Taylor importance and grouped-query-attention-aware selection to make attention dimensions divisible by the target core count while preserving the query-to-key/value ratio and head dimension. At runtime, it separates the system prompt, persistent text history, and transient visual observations by lifetime, updating text history during tool execution so that historical images leave the persistent cache and more interaction rounds fit a fixed budget. On 2,062 GUI actions, the incremental interface shows no accuracy regression, and task-aware recovery training restores 98.7% of the action-type accuracy gap and the coordinate hit rate to the original level. Under seven-core deployment, hardware-aligned pruning reduces vision-encoder latency by 11.4%, improves decoding throughput by 23.8%, and lowers per-heap high-water memory by 12.7%; a parameter-matched control confirms that the speedup stems mainly from core alignment rather than parameter reduction.

---


### 507. [Chain of Faith: Policy-Internal Rewards for Reasoning Reliance](https://arxiv.org/abs/2611.02672)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fanyu meng, Zhaodan Kong, Xin Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) explanations can sound plausible while having little influence on a model's final answer. We study four rewards that use the policy's own signals to encourage reliance on generated reasoning: gradient sensitivity, confidence gaps, progressive confidence gains, and reasoning--prompt swaps. We add each reward to group relative policy optimization (GRPO) and evaluate two small instruction-tuned models on GSM8K and StrategyQA using reasoning edits, paraphrases, and prompt hints. Several configurations increase answer reliance to reasoning edits, while effects on accuracy and paraphrase robustness vary. We also observe answer copying at a high reward weight and high reliance in decomposition settings with poor task accuracy. The study compares practical objectives for reasoning reliance, confirms the trade-off between reliance and performance, and proposes four lightweight rewards that can improve reasoning reliance.

---


### 508. [What Drives the Zero-to-One Jump? Diagnosing and Steering Hard-Prompt Learning in RLVR](https://arxiv.org/abs/2611.02747)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rui Zhu, Yumou Liu, Zhenzhe Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has substantially improved mathematical reasoning, yet progress on hard prompts often stalls: a prompt can remain unsolved for many training steps before abruptly transitioning to solved--a discrete "zero-to-one" jump whose underlying dynamics and steerability remain poorly understood. We investigate two questions: what drives this transition, and can it be steered? Through event-based analysis measuring the time-to-first-positive (TTFP), we find that negative rollouts preceding successful transitions consistently retain higher early-stage generation entropy, distinguishing near-solvable failures from dead ends. This signal motivates NAPO (Negative-Augmented Policy Optimization), a method integrated with Group Relative Policy Optimization (GRPO) that ranks negatives in unsolved groups via an early-branching driver and assigns graded advantages, injecting informative gradients precisely where standard group-relative updates vanish. Under fixed rollout budgets, NAPO accelerates early solution discovery and improves Pass@256 by 10.0 points on AIME24 and 6.6 points on AIME2025, demonstrating that zero-to-one transitions are diagnosable and steerable through driver-guided negative learning. Our code is available at this https URL.

---


### 509. [Investigating the effects of the patch size in Time Series Foundation Models](https://arxiv.org/abs/2611.02750)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jad Yehya, Andrei-Tiberiu Pantea, Aymeric Dieuleveut 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Patch size is a central design choice in patch-based time-series foundation models, controlling temporal resolution, sequence length, and computational cost. We study how this choice interacts with transformer architecture through a controlled comparison of encoder-only and decoder-only forecasting models trained with the same data mixture and optimization budget. Across 97 GIFT-Eval tasks, encoder-only models consistently benefit from smaller patches, whereas decoder-only performance follows a U-shaped trend, with an intermediate patch size performing best in aggregate. Dataset-level results further show that the preferred decoder patch size increases with the forecasting horizon. For encoder-only models, increasing context length improves performance across patch sizes, although the gains diminish beyond a context length of 2048. Finally, training-compute and CPU-latency Pareto analyses reveal complementary regimes: decoder-only models provide efficient low-cost alternatives, while encoder-only models attain the highest overall accuracy. These results show that the choice of patch size and architecture should be made depending on the forecasting horizon and deployment constraints.

---


### 510. [History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models](https://arxiv.org/abs/2611.02782)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hangyi Kuang, Chengzhi Wang, Yefei He 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step autoregressive video diffusion enables efficient generation, yet maintaining consistency over long rollouts remains challenging, especially when subjects or scenes reappear after going out of sight. Despite progress in fidelity and rollout robustness, existing distillation methods do not fully exploit richer historical information to constrain the student's current prediction. To address this gap, we introduce \textbf{History Forcing}, a unified on-policy distillation framework that strengthens historical supervision for few-step autoregressive video generators. The framework uses the residual between teacher predictions with and without informative historical context to decouple this supervision. Such a historical context can be obtained using earlier generated chunks with less accumulated drift or a fixed-view teacher rollout that keeps the scene visible while the student looks away. The residual is then weighted and added to the score or velocity prediction used for distillation, forming a corrected target. By aligning the student with this corrected target through distillation, History Forcing incorporates long-range historical constraints into autoregressive generation. Our method achieves state-of-the-art performance among 1.3B models, with a VBench quality score of 85.07 for 15s video generation and a VBench-Long aggregate score of 79.82 for 60s generation. For out-of-sight world modeling, evaluations further demonstrate more plausible scene evolution and more consistent states when the camera returns, with Evolution Quality improving from 2.35 to 2.70 on PlayWorld and Object Consistency from 58.43 to 62.18 on MemoBench.

---


### 511. [Why Tabular Foundation Models Excel on Relational Data They Have Never Seen](https://arxiv.org/abs/2611.02936)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Linjie Xu, Yiqun Hu, Jixiang He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Given a relational database (RDB) storing heterogeneous tabular information, how can we predict missing (or future) values in some target column of interest? As candidate targets are numerous in enterprise settings, it is preferable to avoid learning a new model from scratch each time there is a new prediction task. Frozen foundation models (FMs) based on in-context learning (ICL) and RDB-specific pre-training provide a viable solution, but the ideal design still remains largely unresolved. Perhaps unexpectedly, preliminary evidence has recently shown that existing single-table FMs (aka TFMs), when combined with suitable parameter-free relational encoders, can be quite competitive in practice despite zero exposure to RDB pre-training or relational data of any kind. In this work we first empirically confirm this phenomenon with a more diverse array of experiments. We then turn to our main contribution, namely, surfacing multiple complementary explanations for why TFMs behave so effectively. These explanations ultimately hinge on innate synergies whereby parameter-free encoders map relational effects to fixed-length embeddings that loosely mimic distributions for which TFMs were originally designed; in so doing, desirable single-table properties transfer to relational settings (e.g., convergent posterior predictive distributions). Collectively, our analysis forges new pathways for improving RDB FMs, particularly when we prioritize interpretability and inevitable integration within agentic systems.

---


### 512. [Axion 1.0: Open Agent Foundation Models, Simplified](https://arxiv.org/abs/2611.03233)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuqi Jia, Yunjie Tian, Jiayu Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Axion 1.0, a fully open agent foundation model that combines strong and broad agentic capabilities with a remarkably simple training recipe. Axion 1.0 is trained in only three stages: two lightweight supervised fine-tuning stages followed by reinforcement learning, without dedicated mid-training, direct preference optimization (DPO), or on-policy distillation (OPD). The first SFT stage develops strong self-contained reasoning through model-aware data construction, where we synthesize challenging problems and adversarially strengthen them based on the base model's own successful solution strategies. The second stage extends these capabilities to tool-dependent reasoning through a scalable pipeline for constructing diverse and automatically verifiable tasks grounded in real-world data sources and deterministic computation. Finally, reinforcement learning further strengthens long-horizon reasoning and interaction with external tools and environments. Despite this compact training recipe, Axion 1.0 achieves strong performance across a broad suite of agentic benchmarks and is competitive with leading commercial models on several of them. Equally importantly, Axion 1.0 is open beyond model weights: we release the complete recipe, including data construction, generation, filtering, verification, prompts, and training code, enabling the entire development process to be reproduced and extended. Axion 1.0 demonstrates that strong agent foundation models can be both open and simple, offering a practical and reproducible path toward advancing open agentic intelligence.

---


### 513. [A Common Language for Dynamic Graphs: Interaction Tokenization Enables Foundation Models](https://arxiv.org/abs/2611.03246)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fuyuan Ma, Yili Wang, Xin He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic graphs capture evolving interactions in Web systems, including online communication, user engagement, and recommendation. Graph foundation models aim to reuse predictive capabilities across networks, but extending this capability to dynamic graphs faces two challenges. First, node identities are graph-specific, and similar interaction patterns can appear at different temporal and activity scales, making histories difficult to represent consistently across networks. Second, the predictive roles of historical patterns vary across interaction dynamics, limiting transfer from a narrow range of training processes. In this paper, we show that a common interaction language, combined with learning across diverse interaction processes, offers a basis for dynamic graph foundation modeling. We propose CL-DGFM, a Common Language Dynamic Graph Foundation Model for temporal link prediction. Its Dynamic Interaction Tokenizer encodes interaction memory, historical connectivity, and ordered destination transitions into calibrated tabular inputs, making dynamic histories accessible to existing predictors without an additional trainable graph encoder. Its Dynamic Interaction Prior trains a pretrained tabular foundation predictor across diverse synthetic dynamics. Labeled historical context guides prediction, with a Contextual Value Adapter modulating attention values. The model transfers to real graphs without target-graph parameter updates. Experiments on TGB and TGB-Seq demonstrate competitive performance. Further comparisons show that the common language supports basic machine learning and neural models, and enables direct use of frozen tabular foundation models on dynamic graphs.

---


### 514. [RASP: Read-All, Sparse-Plasticity Continual Learning in a Stationary-Size LoRA](https://arxiv.org/abs/2611.03513)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wen-Hsuan Liu, Amara Okonkwo, Tom Saliencro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient continual learning on pre-trained Vision Transformers largely relies on a costly premise: preventing catastrophic forgetting requires either spawning a dedicated LoRA branch per session---causing adapter parameters to scale linearly with task horizon---or applying sparse Mixture-of-Experts gating symmetrically to both forward and backward passes, which sacrifices representational rank at test time. We argue that reading consolidated knowledge and writing new task credit are fundamentally asymmetric operations. Because visual features in a shared low-rank space distribute across rank-1 atoms rather than localizing in disjoint task silos, forward inference should read all atoms at full rank capacity, whereas backward optimization should restrict plasticity to a sparse subset of input-aligned channels. We introduce RASP (Read-All, Sparse-Plasticity LoRA), which adapts a single stationary-size adapter across sequential tasks. At each step, a scene-modulated cosine router selects the top-$q$ unlocked atoms to receive gradients, blocks updates on the remaining $r-q$ channels, and penalizes Frobenius Gram coherence between active and non-updated output directions. Across sessions, the router's empirical activation trace and each atom's exact spectral norm form a zero-overhead geometric consolidation index $\omega_j = \sqrt{\tilde{c}_j \tilde{\sigma}_j}$ that drives Cauchy step attenuation and boundary anchor locking. Across CIFAR-100, CUB-200, ImageNet-R, and ImageNet-A, RASP matches or surpasses branch-expanding LoRA learners under a strictly constant parameter footprint.

---


### 515. [Evaluating Uncertainty Calibration in Probabilistic Time Series Foundation Models](https://arxiv.org/abs/2611.03592)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Thomas Decker, Volker Tresp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) are increasingly used for probabilistic forecasting across diverse domains, yet the reliability of their uncertainty estimates remains poorly understood. In this work, we study uncertainty calibration in probabilistic TSFMs from a broader methodological and empirical perspective. We introduce a taxonomy of how TSFMs represent predictive uncertainty and develop a fine-grained evaluation framework for calibration in multi-horizon forecasting that distinguishes pooled, horizon-wise, and stronger conditional notions of calibration. Using this framework, we conduct a comprehensive empirical evaluation of popular TSFMs across diverse datasets and show that current models exhibit distinct and systematic patterns of miscalibration that standard metrics often obscure. We further analyze common post-hoc recalibration methods and characterize which forms of calibration they can improve and which tend to persist. Our results provide practical guidance for evaluating and improving uncertainty calibration in TSFMs and highlight important limitations of current practice.

---


> [!TIP]
> 当前位于：**501-515**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-515**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
