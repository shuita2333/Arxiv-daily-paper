# 🧠 大模型相关研究 | 2026年10月07日

> 本类共 **505** 篇论文：已确认 **467** 篇，待复核 **38** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**501-505**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-505**

---

### 501. [EMG-FM-Bench: A Comprehensive Benchmark for Foundation Model Transfer and Adaptation on Electromyography](https://arxiv.org/abs/2610.06450)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tianhao Wu, Xu Wu, Amirmohammad Radmehr 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models (FMs) are increasingly being developed for general time series and physiological signals, yet their transferability to downstream physiological tasks remains poorly understood. This question is particularly challenging for electromyography (EMG), where signal distributions vary substantially across users, sensing configurations, acquisition hardware, and downstream tasks. We introduce EMG-FM-Bench, a systematic benchmark for studying foundation-model transfer and adaptation on EMG. EMG-FM-Bench unifies 20 public datasets with over 1 million EMG segments and evaluates nine pretrained foundation models across four questions: how pretrained models perform when frozen or fully fine-tuned, how much pretraining helps compared with training the same model from scratch, how well models generalize to new users with limited labeled data, and how performance changes across different EMG tasks. Across the benchmark, linear probing provides useful information about pretrained representations, but full fine-tuning can substantially change downstream EMG performance. Comparing each pretrained model with the same model trained from scratch shows that the benefit of pretraining varies substantially across models and is not universal. Performance decreases when models are evaluated on new users, while five-shot adaptation improves macro-F1 in 70.2% of evaluated model-dataset combinations but recovers only part of the lost performance. Model performance is highly consistent between upper- and lower-limb classification and remains strongly correlated with continuous EMG-to-text decoding. Together, these results provide a systematic view of when pretrained time-series models transfer effectively to EMG and how their performance depends on fine-tuning, user variation, and downstream task.

---


### 502. [Normality Constraint Learning: Adapting Foundation Models for Time Series Anomaly Detection](https://arxiv.org/abs/2610.06453)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaohui Zhou, Yijie Wang, Hongzuo Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time Series Foundation Models (TSFMs) achieve strong generalization by learning to reconstruct or forecast broad temporal patterns from large-scale time series during pre-training. Yet this strength can become a weakness for anomaly detection: TSFMs may model rare anomalous patterns as effectively as normal ones, allowing anomalies to be accurately reconstructed or forecasted and thus diminishing their reconstruction/forecasting error-based anomaly scores. This paper proposes $\underline{\textbf{N}}$$\textbf{ormality}$ $\underline{\textbf{C}}$$\textbf{onstraint}$ $\underline{\textbf{L}}$$\textbf{earning}$ ($\textbf{NCL}$), a lightweight plug-and-play framework that adapts pre-trained TSFMs for accurate anomaly detection without modifying their pre-trained parameters. Our key insight is to constrain the broad pattern space of TSFMs to the normal structure of a target time series, preventing their broad modeling capability from obscuring abnormal deviations. Specifically, NCL constructs a compact normality subspace from a few normal patch features and adaptively steers each patch feature toward normality within this subspace, guided by contrastive constraints that form compact and discriminative normality manifolds. The calibrated features are aggregated to reinforce normal components and fused with the original TSFM output, amplifying the discrepancy between normal and abnormal observations for the reconstruction/forecasting error-based anomaly scoring. Extensive experiments across diverse TSFM families and benchmarks show that NCL consistently improves anomaly detection performance, providing a generalizable framework for adapting TSFMs to anomaly detection.

---


### 503. [Xaurora: Generative Weather Forecasting with Denoising Stochastic Interpolants from a Foundation Model Prior](https://arxiv.org/abs/2610.06509)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Eliot Walt, Miltiadis Kofinas, Nikolaj Mücke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has revolutionised weather forecasting in recent years, especially through atmospheric foundation models, which offer competitive skill for a fraction of the computational costs of classic physics-based models. However, most existing foundation models are deterministic, limiting the generation of large ensembles for accurate uncertainty quantification, extreme weather risk assessment, and long-range weather forecasting. Furthermore, these models incur a large, often prohibitive, computational overhead to train from scratch. To address these shortcomings, we turn a pretrained deterministic prior model, namely the Aurora foundation model, into a generative ensemble-prediction model. To that end, we introduce a novel generative method, Denoising Stochastic Interpolants, combined with a replay buffer for Stochastic Differential Equation (SDE) rollout, enabling probabilistic training of SDE trajectories. Our stochastic foundation model, Xaurora, is finetuned from the small Aurora version, yet it approaches the state-of-the-art on global ensemble metrics and is competitive with the large version of Aurora. Our method is parameter and sample efficient, and generates skilful 15-day forecasts in 13 minutes. Our results demonstrate that deterministic foundation models can be efficiently extended into even stronger stochastic models.

---


### 504. [RealtimeWAM: One-Step Asynchronous World Action Models](https://arxiv.org/abs/2610.06617)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chengtao Lv, Jinyang Du, Shuyi Feng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) incorporate visual representations from video generation backbones to guide action prediction. Recent efficient WAMs adopt Mixture-of-Transformers (MoT) architectures and compute video representations once for reuse by the action expert. However, intra-expert iteration (\ie, multi-step action denoising) and inter-expert waiting (\ie, sequential execution of the video and action experts) still limit inference efficiency. To this end, we present RealtimeWAM, an extremely efficient WAM variant with one-step action generation and asynchronous inference, addressing these two bottlenecks. To reduce intra-expert iteration, we propose Teacher-Anchored Consistency Distillation (TACD) to address a local-global error gap: low local consistency error alone does not guarantee accurate final actions. TACD supplements local consistency with explicit supervision from the frozen teacher's multi-step rollout endpoint, enabling accurate one-step action generation. Additionally, we propose Cross-Expert Wavefront Pipelining (CEWP) to eliminate unnecessary expert-level waiting. It overlaps the two experts through block-wise sharing of the video KV cache, synchronizing only immediately before the corresponding action attention consumes it. Extensive experiments across diverse benchmarks (\eg, LIBERO, LIBERO-Plus and RoboTwin) and model variants (\eg, Fast-WAM and Faster-WAM) demonstrate the superiority of RealtimeWAM. Notably, RealtimeWAM maintains near-lossless performance (\ie, $<1\%$ drop) across these benchmarks while delivering significant end-to-end speedup (\eg, $\sim25\times$ on H100). Our code and checkpoints are available via this \href{this https URL}{link}.

---


### 505. [Less Context, Better Geometry: Masked Geometric Encoder for Robust 3D Foundation Models](https://arxiv.org/abs/2610.06813)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhimin Shao, Xijun Liu, Zhaoliang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in 3D foundation models has enabled rapid 3D reconstruction and camera calibration by leveraging learned 3D priors from vast amount of spatial data. However, the all-to-all global attention design leads to quadratic complexity and limits long-sequence inference; unconstrained cross-view interactions also can propagate unreliable evidence from occluded or visually similar but geometrically distant views. In this paper, We introduce a Masked Geometric Encoder (MGE), which promotes the learning of robust geometric representations under incomplete cross-view context. During training, MGE strategically drops frame tokens from global attention and distills from a pretrained full-context teacher model. This allows the model to learn an intrinsically richer per-frame representation while providing sufficient intermediate supervision to avoid performance degradation. Through extensive experiments, we show that MGE leads to much stronger performance under occlusion and doppelganger views while retaining high performance on standard benchmarks. Such a richer frame representation also leads to more effective token reduction during inference. To this end, we develop a novel Anchor-Guided Adaptive token merging technique that preserves representative anchor frames while jointly merging redundant tokens from the remaining views. Compared to other efficient inference approaches, we can achieve inference speedup while consistently maintaining higher reconstruction quality, particularly in limited-view settings.

---


> [!TIP]
> 当前位于：**501-505**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-505**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
