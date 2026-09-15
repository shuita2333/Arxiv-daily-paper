# 🧠 大模型相关研究 | 2026年09月16日

> 本类共 **368** 篇论文：已确认 **345** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-368**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-368**

---

### 351. [MANAS-2: Constrained Reconstruction for EEG Foundation Models](https://arxiv.org/abs/2609.13717)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Arvasu Kulkarni, Aditya Ray Mishra, Mahir Jain 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Masked reconstruction is widely used for EEG foundation models, but optimizing reconstruction on low-SNR waveforms does not necessarily produce the most useful latent representation. We introduce MANAS-2, a new EEG foundation model that combines a Raw-Band Hybrid (RBH) masked autoencoder with Constrained Reconstruction (ConRec), a physics-motivated regularizer. RBH jointly reconstructs temporal waveform patches and compact spectral-band targets, while ConRec acts only on the temporal decoder output, penalizing differences in RMS energy between adjacent short windows of the reconstructed waveform. ConRec is intended to shape the encoder by biasing it toward the organization of oscillatory-envelope information. Across seven held-out EEG datasets, adding ConRec to an otherwise identical RBH model increases frozen ridge recovery of six-band spectral power from mean R^2=0.860 to 0.906 and recovery of inter-patch band-energy dynamics from R^2=0.283 to 0.354, while temporal waveform information remains highly recoverable from the frozen latents. Applied to a temporal-only masked autoencoder, ConRec also improves frozen downstream transfer and frequency-dependent latent geometry despite receiving no spectral targets: i.e., the effects of ConRec are architecture-independent. MANAS-2 also outperforms leading EEG Foundation Models on most downstream knowledge-transfer tasks. From the effects of ConRec, we see that a physically motivated constraint imposed through the decoder can make for a more spectrally organized and transferable latent space. MANAS-2 therefore provides a new EEG foundation model built around constrained reconstruction as a mechanism for shaping representation--rather than reconstruction--quality.

---


### 352. [Physically Typed and Geometry-Aware Representations for Earth Foundation Models](https://arxiv.org/abs/2609.13868)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rajiv Ranjan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth-observation (EO) foundation models have become exceptionally effective at learning se mantic, high-dimensional geospatial embeddings, while modern weather and climate models have demonstrated that Earth-specific geometry, spherical operators, meshes, and hybrid physical solvers can materially improve prediction. Yet these two advances are not equivalent. A conventional latent embedding has no inherent physical transformation law, whereas scalar fields, tangent polar-vector fields, axial/pseudovector quantities, covectors, and higher-order tensors transform differently under rotations, reflections, and changes of local coordinate frame. This proposal asks whether a general purpose Earth foundation model should preserve those distinctions explicitly, or whether standard embeddings plus augmentation already learn everything that matters. The central contribution is therefore not a more complicated architecture by assumption, but a staged falsification program. A compute-conscious ERA5 dry run first compares conventional, augmentation-matched, typed equivariant, and Hodge/Helmholtz variants under spatial, temporal, orientation, and low-data shifts. Only if explicit geometric typing yields reproducible improvements does the program advance toward a multimodal Earth foundation model in which semantic embeddings coexist with physically typed fields. The proposed gap is narrower and more defensible than claiming that current models ignore geometry entirely: several systems already respect spherical domain geometry, and emerging work explicitly learns scalar/vector fields on spheres. The unresolved question is whether foundation-scale, multimodal, parity-aware field typing produces practical gains beyond those existing approaches.

---


### 353. [A Multi-Resolution Multi-Domain Pre-Training Framework for Universal Traffic Forecasting](https://arxiv.org/abs/2609.13878)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhouyang Liu, Jindong Han, Hao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal traffic data are central to intelligent transportation systems, yet their heterogeneity poses significant challenges for large-scale modeling. Existing pre-trained models often rely on a homogeneous modeling paradigm to handle highly heterogeneous traffic data. This fundamental mismatch not only limits model generalization but also leads to computationally expensive and parameter-inefficient designs. To this end, we propose FlexST, a novel pre-training framework that introduces modularity and adaptivity for traffic modeling. Specifically, we first propose a multi-resolution spatio-temporal diffusion module that captures both short-term fluctuations and long-range trends, effectively reconciling inputs with divergent temporal and spatial resolutions. After that, we construct a domain-adaptive mixture-of-experts that dynamically routes data to specialized sub-networks, enabling selective knowledge transfer while preventing negative interference across diverse domains. Moreover, we devise a unified periodic encoding strategy that injects resolution- and domain-aware inductive biases to harmonize periodic inconsistencies across datasets. Extensive experiments on 23 real-world traffic datasets demonstrate that FlexST significantly outperforms state-of-the-art baselines in zero- and few-shot settings, showcasing superior generalization, adaptability and efficiency. This work offers a new direction for building general-purpose pre-trained models capable of handling the complexity and variability of urban traffic systems.

---


### 354. [Tabby: An Open Pretraining Recipe for Time Series Foundation Models](https://arxiv.org/abs/2609.13956)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shifeng Xie, Bahaeddine Abdessalem, Zehao Xiao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this report, we release Tabby, a long context probabilistic time series foundation model, together with a complete and open recipe of how it was built. Tabby adopts an encoder-only patch Transformer architecture and concentrates the contributions on the data and the training procedure. The pretraining corpus combines an extended real-world collection, GIFT-Eval-Pretrain+ and BLAST, with synthetic data from KernelSynth and CauKerV2, an online generator that composes temporal dynamics through randomly sampled structural causal models. Training couples a progressive convergence schedule, which yields reusable intermediate checkpoints, with a deep quantile supervision objective for intermediate layers. The resulting 145M parameter backbone supports contexts of up to 8,192 observations and serves forecasting, classification, and anomaly detection, while a prompt-tuning module further improves in-distribution forecasting performance with the pretrained weights frozen. Tabby achieves competitive zero-shot forecasting performance on GIFT-Eval and the out-of-distribution TIME benchmark, while the same pretrained backbone also supports classification on the UCR Archive and zero-shot anomaly detection on TSB-AD-U. We release training pipeline and model as open source at huawei-noah/trustworthyAI.

---


### 355. [Parameter-Efficient Fine-Tuning of Foundation Models for Liver Tumor Segmentation in CT](https://arxiv.org/abs/2609.14106)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ramtin Mojtahedi, Mohammad Hamghalam, Jacob J. Peoples 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We evaluated parameter-efficient fine-tuning (PEFT) of the Segment Anything Model (SAM) for liver tumor segmentation in abdominal CT of colorectal liver metastases. We compared Low-Rank Adaptation (LoRA), 4-bit Quantized LoRA (QLoRA), a convolutional adapter (Conv-Adapter), and our Directional Spectral Top-K adapter (DiSCo), training only adapters while freezing the SAM backbone. DiSCo derives spectral bases from singular value decomposition of row-normalized weights and learns rank-gated spectral coefficients, per-output magnitude offsets, and a spectral gain, with optional Top-K rank selection at inference and 0.14 M trainable parameters. We benchmarked five prompting regimes: no prompt, single-point, multi-point, and bounding boxes at intersection over union 0.50 and 0.75. Conv-Adapter and LoRA achieved the highest accuracy (overall Dice 0.793 and 0.792; single-point Dice 0.795 and 0.792; 95th-percentile Hausdorff distance (HD95) 32 mm). QLoRA was close (overall Dice 0.766; single-point Dice 0.768; HD95 36.41 mm), with 0.91 M trainable parameters, 120 ms latency, and 4.9 GB peak memory. DiSCo achieved the highest Dice per million trainable parameters (4.66), with overall Dice 0.653, single-point Dice 0.698, and HD95 49.53 mm. These results show an accuracy-efficiency trade-off and support PEFT for liver tumor segmentation with reduced adaptation costs when compute and labeled data are limited. Code: this https URL

---


### 356. [Multimodal deep learning from spectra for small-molecule structure identification: enhancing robustness with mixed-condition training](https://arxiv.org/abs/2609.14360)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bowen Gao, Lei Zhu, Yiying Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In practical molecular characterization, small-molecule structure identification benefits from complementary spectroscopic evidence, but missing, degraded, or mismatched spectra challenge multimodal models. Herein, we incorporate domain knowledge from spectroscopy and chemistry into mixed-condition training for candidate structure reranking, using a reproducible evaluation protocol and mixture-of-experts (MoE) fusion. The protocol incorporates perturbations tailored to each spectroscopic modality and chemically informed spectrum replacements to cover variations in spectral availability, quality, and consistency. A total of 79,462 test samples were evaluated across 30 predefined conditions using simulated spectra from the Multimodal Spectroscopic Dataset (MSSD) for mass spectrometry (MS), infrared (IR) spectroscopy, and 1H and 13C nuclear magnetic resonance (NMR), with up to 128 hard candidate structures per sample. A controlled two-by-two factorial comparison of complete-input training versus mixed-condition training and vanilla concatenation versus MoE fusion, with matched evaluation conditions, showed that mixed-condition training provided the main gains in both architectures. For MoE, mean reciprocal rank (MRR), averaged equally across conditions, increased from 0.9203 to 0.9763, a relative increase of 6.08%. Recall at rank 1 (R@1), averaged over the same conditions, increased from 89.50% to 96.36%, an increase of 6.86 percentage points and a relative increase of 7.67%. IR-only and MS/MS-only MRR increased from 0.4337 to 0.9307 and from 0.3711 to 0.8575, reaching 2.15 and 2.31 times their respective baseline values, while complete-input performance remained high. These results support integrating domain knowledge into training-condition design to improve robustness, with further gains from MoE under mixed-condition training.

---


### 357. [Retrieval-Guided Fine-Tuning as Noisy Estimation: Risk bounds and Architectural Analysis](https://arxiv.org/abs/2609.14485)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bhargav Lad, Yifan Hao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-Guided Fine-Tuning (RAG-FT) incorporates retrieved data directly into the training objective, but the statistical consequences of noisy retrieval during training remain theoretically undercharacterized. We study this question by modeling RAG-FT as an estimation problem in a multi-task linear regression framework, using an OLS proxy for single-layer linear self-attention to obtain finite-sample risk bounds. Under homoscedastic retrieval noise, we show that retrieval failure decays exponentially with task separation relative to noise, and derive explicit finite-sample conditions under which RAG-FT achieves lower risk than both target-only and full-corpus training. We then introduce a Distance-Proportional Noise (DPN) model, in which retrieval quality degrades with rank, and compare two estimators under the same retrieval process: the OLS proxy and the literal, uniform-weight forward pass of linear self-attention. We prove that the attention estimator's bias diverges as $\Theta(n^{2q})$ even under exact retrieval, while OLS risk remains $\Theta(d/n)$ for every noise exponent $q>0$. These results locate the instability not in noisy retrieval itself, but in the fixed, unweighted aggregation of the literal LSA forward pass, which reweighting by reliability empirically removes. We validate the predicted rate separation through direct simulation of the DPN model.

---


### 358. [EdgeHAR: An Edge-Native Compact Sensor Foundation Model for Human Activity Recognition](https://arxiv.org/abs/2609.14498)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** He Zhang, Siyu Yuan, Siyu Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sensor-based human activity recognition (HAR) is fundamental to ubiquitous and wearable computing, yet existing foundation models are largely designed for cloud-scale deployment and struggle with real-world sensing shifts, including unseen users, devices, sampling rates, and sensor placements. We present \textbf{EdgeHAR}, an edge-native compact sensor foundation model designed for wearable intelligence. Unlike conventional models that entangle activity knowledge with acquisition variations, EdgeHAR learns transferable representations by factorizing sensor signals into three latent codes: an \textbf{(i)Activity-Semantic Code} capturing reusable activity knowledge, a \textbf{(ii)Motion-Dynamics Code} modeling temporal patterns, and an \textbf{(iii)Acquisition-Context Code} representing sensor-specific variations. This disentangled design enables efficient adaptation to new users, devices, placements, and activity classes with limited target-domain data. By incorporating lightweight adaptation modules, EdgeHAR achieves foundation-model-level transferability while satisfying edge constraints in computation, memory, latency, and privacy. Experiments across heterogeneous HAR datasets demonstrate that EdgeHAR maintains competitive recognition performance under distribution shifts with substantially reduced deployment cost. EdgeHAR establishes a practical paradigm for compact, edge-first foundation models for ubiquitous sensing systems.

---


### 359. [Decision-Oriented Uncertainty Quantification for Risk Control in Earth System Spatiotemporal Foundation Models](https://arxiv.org/abs/2609.14821)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ji Lu, Huiran Duan, Bo Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Earth system modeling is shifting from task-specific predictors toward foundation models with general spatiotemporal representation capabilities. Although these models can jointly encode dynamic Earth fields, external forcings, and static geographic context for multistep forecasting, accurate point predictions or statistically calibrated intervals alone are insufficient for high-impact applications such as extremeweather warning, flood control, renewable-energy dispatch, and emergency resource allocation. What matters in practice is whether predictive uncertainty can be translated into reliable decision risk under specific actions, loss functions, and risk preferences. We propose a decision-oriented uncertainty quantification framework for Earth system spatiotemporal foundation models. The framework produces predictive distributions of future states and uses a decision risk adapter to map forecast samples, decision context, and utility functions into action-conditional risks. A utility-aware calibration module further enforces reliability at the downstream decision-loss level rather than only at the forecast-value level. Calibrated risks are then used to select warning, dispatch, inspection, or resource-allocation actions. Compared with the strongest baseline, the proposed method reduces decision regret by 18.7%, lowers the missed-event rate from 14.2% to 9.1%, and improves expected utility by 11.6%, while maintaining 90.4% predictive coverage and reducing decision calibration error from 0.083 to 0.047. These results suggest that decision-oriented uncertainty quantification can improve the robustness and operational value of Earth system foundation models in risk-sensitive applications.

---


### 360. [Towards a knowledge-enhanced single-cell foundation model](https://arxiv.org/abs/2609.14970)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hanqing Zhang, Jie Bao, Mei Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Single-cell foundation models (scFMs) increasingly rely on large-scale transcriptomic pretraining, yet expanding pretraining data can yield diminishing gains while substantially increasing computational cost. Our data scaling analyses showed that incorporating biological knowledge, including cell-level text annotation and gene-level regulatory information, provided additional scaling dimension than simply increasing data size. Motivated by this observation, we present scKITE, a simple yet effective scFM that integrates cell-annotation and gene-regulatory supervision into a shared transcriptomic Transformer encoder through lightweight auxiliary decoders. These decoders are used only during pretraining and subsequently discarded, yielding a general-purpose encoder enriched with biological knowledge for downstream applications. With only 179,067 pretraining samples, i.e., less than 0.5\% of those used by previous strong scFMs, scKITE outperformed these models across diverse downstream tasks, highlighting knowledge-enhanced pretraining as a promising paradigm for biologically grounded scFMs.

---


### 361. [T-LoopFormer: Token-Level Elastic-Depth Looped Transformers for Latent Reasoning With Dynamic Routing](https://arxiv.org/abs/2609.15160)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mingqian Yu, Wenpeng Zhang, Peilin Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Looped Transformers have recently demonstrated strong performance in both reasoning and language tasks by reusing a shared set of parameters across multiple iterations, achieving parameter efficiency without sacrificing representational power. Besides, looped Transformers perform inference directly in the latent space (latent reasoning) to reduce the number of tokens consumed during inference, thereby achieving improved sample efficiency. However, these models typically apply a fixed recursion depth uniformly to every token, leading to suboptimal compute allocation and leaving significant efficiency gains on the table. In this work, we propose \textbf{dynamic token-choice routing} for looped transformers, enabling each token to adaptively determine its own number of loop iterations based on its hidden state. We use a dynamic router to decide whether a token should continue recursing or exit early, allowing simple tokens to bypass unnecessary computation while hard tokens receive deeper processing. To ensure that this adaptive mechanism does not compromise decoding efficiency, we further introduce recursion-wise KV caching, which maintains an independent key-value cache for each recursion loop. This design ensures that tokens at different depths only attend to their corresponding cached states, effectively eliminating redundant computations for exited tokens and enabling fast autoregressive decoding. Extensive experiments show that T-LoopFormer reaches the sota performance under the same parameters on PPL and 10 zero-shot reasoning tasks, even surpassing the base model at 24x FLOPs and our model could reach the lowest inference latency, which validate the effectiveness of token-choice router and recursion-wise KV cache. Code: this https URL.

---


### 362. [Long-to-Short Video Evidence Reasoning for Grounded Question Answering](https://arxiv.org/abs/2609.15224)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kaiyan Chen, Junbin Xiao, Xun Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LOVER, a \underline{L}ong to sh\underline{O}rt \underline{V}ideo \underline{E}vidence \underline{R}einforced model for grounded question answering (GQA). LOVER highlights three innovations over existing reinforcement-learning (RL) based video reasoning models: (1) \textbf{Long-to-short Video Evidence Curriculum Learning}, which organizes RL training according to evidence duration and progressively adapts the model from long-range grounding to short-term reasoning; (2) \textbf{GQA Rewards}, which underscore the benefit of IoP reward over IoU for evidence spotting rather than strict temporal span overlap; (3) \textbf{Adaptive Timestamp Rendering}, which adaptively renders timestamps onto video frames using background-aware position and color selection to enhance temporal observability. The three designs are model-agnostic and reciprocal. They effectively improve QA, grounding, and grounded QA performance over different backbones. Notably, LOVER built on Time-R1 achieves new state-of-the-art (SOTA) results among open-source models on popular GQA benchmarks: NExT-GQA and ReXTime. Comprehensive ablation studies further validate the effectiveness of our three innovative components.

---


### 363. [Reason What Matters: Retrieval-Grounded Reasoning for Universal Multimodal Embeddings](https://arxiv.org/abs/2609.15296)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mingzhou Jiang, Peixi Wu, Hang Cheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Universal multimodal embedding (UME) learns unified representations across modalities, enabling a single model to support diverse retrieval tasks. Recent methods use Chain-of-Thought (CoT) reasoning to better interpret multimodal inputs before generating embeddings for complex retrieval tasks and further optimize this reasoning process through GRPO with retrieval-based rewards. However, two limitations hinder corpus-scale deployment. GRPO assigns all CoT tokens the same advantage, without identifying input-supported claims or evidence that distinguishes the positive from negatives. Moreover, generating a complete CoT before each embedding introduces substantial latency, even when a partial trace already provides sufficient retrieval evidence. To address these limitations, we propose Reason What Matters (ReWAM), a retrieval-grounded reasoning framework that uses retrieval feedback to guide both credit assignment and reasoning computation. Specifically, we introduce Retrieval-aware Self-Distillation (RASD), which constructs privileged guidance from input-supported evidence that distinguishes the positive item from retrieved hard negatives. An on-policy self-teacher uses this guidance to refine trajectory-level feedback into token-specific supervision for retrieval-relevant reasoning. We further develop Retrieval-adaptive Inference (RAI), which uses a retrieval confidence head to estimate the remaining retrieval utility of a partial CoT. It stops unproductive traces early and accelerates useful continuations with speculative decoding. Extensive experiments on MMEB-V2 and MRMR demonstrate that ReWAM achieves state-of-the-art retrieval performance while delivering up to 5x the inference throughput of competitive explicit-CoT UME methods. These results bridge the gap between retrieval quality and inference efficiency, making reasoning-enhanced UME practical for large-scale deployment.

---


### 364. [A Language-Guided Multimodal Foundation Model for Zero-Shot and Multi-Task Brain Signal Analysis](https://arxiv.org/abs/2609.15740)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mingzhi Chen, Yiyu Gui, Guibo Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain signal analysis is essential for both neuroscience research and clinical diagnostics, yet current approaches face critical limitations. End-to-end models require task-specific retraining and exhibit limited generalization, while pre-trained models lack semantic depth and still depend on extensive fine-tuning. Meanwhile, general-purpose multimodal foundation models, though powerful in other domains, struggle to interpret brain signals due to representational misalignment and lack of domain knowledge. This study introduces a multimodal foundation model for zero-shot and multi-task brain signal analysis (METIS) through a unified language-signal alignment framework. METIS is pretrained on the largest and most diverse brain-signal corpus to date, comprising over 70,000 h of recordings from more than 11,000 subjects across 20 datasets. In a comprehensive zero-shot evaluation across 12 datasets, METIS outperformed the leading generalist model by over 20.9% in average accuracy. Remarkably, without any fine-tuning, METIS's performance matches or exceeds that of supervised, task-specific models. Furthermore, METIS demonstrates exceptional data efficiency and strong generalization, achieving an average AUROC advantage of over 16.0% in few-shot settings and 15.9% in cross-dataset transfer. This work establishes a new paradigm for general-purpose brain signal analysis, paving the way for next-generation neurotechnology.

---


### 365. [SURE-Map: Self-Correcting Streaming Geometric Foundation Model](https://arxiv.org/abs/2609.15795)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mingkai Liu, Hao Zhao, Xingxing Zuo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming geometric foundation models are emerging as a compelling alternative to SLAM systems. Yet this streaming nature introduces a fundamental issue: each prediction is made from limited context, which is vulnerable to dynamic objects and weak textures. Small local errors accumulate into severe geometric distortion and long-horizon scale drift. We argue that reliable streaming reconstruction requires geometric foundation models to be not only predictive, but also self-correcting. We introduce SURE-Map, a self-correcting framework built upon two complementary principles. First, we explicitly model cross-view geometric uncertainty. Unlike conventional depth or point confidence, which primarily reflects the reliability of individual-view prediction, our uncertainty directly measures whether the jointly predicted pose and depth induce geometrically consistent cross-view pixel correspondences. Second, because local correction alone cannot eliminate slowly accumulating scale errors, we introduce multi-timescale self-correction: fast consecutive-frame inference preserves streaming efficiency, while sparse keyframe-window inference provides longer-range geometric evidence to periodically recalibrate the scale of recent trajectories. SURE-Map establishes new state-of-the-art performance for online feed-forward reconstruction across long-horizon benchmarks, reducing ATE-RMSE from 24.00 to 17.24 m on KITTI, 5.11 to 4.74 m on Oxford Spires, and 31.37 to 28.58 m on VBR, with further improvements to 15.17, 4.63, and 22.12 m when incorporating loop-closure refinement. Project page: this https URL.

---


### 366. [Authorization Architectures for Tool-Using AI Agents](https://arxiv.org/abs/2609.15906)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rakesh Kumar Surapani, Pradeep Kumar Dolabehera Kakitapelli, Arun Morampudi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using artificial intelligence (AI) agents, systems that autonomously invoke application programming interfaces (APIs), databases, browsers, and inter-agent protocols such as the Model Context Protocol (MCP), are becoming production infrastructure. Yet the security model governing when an agent is authorized to act on a human's behalf remains underdeveloped. Trustworthy human-AI systems require that every consequential agent action be traceable to a human principal, bounded by what that human actually delegated, and contestable after the fact; few documented deployments satisfy all three properties reliably and end to end. Existing literature addresses fragments of this problem in isolation, credential management for non-human identities, classical access control models, prompt injection, and audit trails, while giving little attention to the authorization decision point itself, the moment a tool invocation occurs, and mechanisms that make that decision correct, enforceable, and accountable. This review introduces a principal hierarchy spanning human user, operator/deployer, orchestrator agent, sub-agent, and tool endpoint as an organizing framework, and examines five interdependent layers: agent identity and credential lifecycle; delegation and scope propagation across multi-hop chains; runtime enforcement and just-in-time authorization at policy enforcement points (PEPs); prompt injection as an authorization bypass that breaks the principal hierarchy; and auditability, provenance, and non-repudiation. Drawing on a structured narrative review of 89 primary sources screened from approximately 180 candidates published between 2023 and 2026, we propose seven structural requirements, derive a four-layer reference architecture, apply the requirements to three deployable reference configurations, and identify runtime enforcement and aggregation bounds as the principal unresolved gaps.

---


### 367. [Vulnerability Localization Benchmark: Measuring Agentic Security Analysis at Repository Scale](https://arxiv.org/abs/2609.15939)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aman Priyanshu, Supriti Vijay, Kimia Majd 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language-model agents increasingly operate over complete software repositories, yet cybersecurity evaluations primarily measure whether they can detect, reproduce, or repair vulnerabilities rather than whether they can locate the relevant code. We study vulnerability localization: given a weakness class and an unfamiliar repository, identify the implementation files associated with that weakness. We introduce the Vulnerability Localization Benchmark (VLoc Bench), comprising 500 real world vulnerabilities from 290 repositories across six package ecosystems and 147 CWE categories. Each task pairs repository snapshots immediately before and after a security fix. On the vulnerable snapshot, an agent receives only the CWE description and read-only terminal access and must return the affected files; on the patched snapshot, it must determine that the recorded vulnerability is no longer present. We evaluate 27 language models and four static-analysis tools under a common agent interface. Repository-scale vulnerability localization remains difficult: the strongest system achieves 0.229 File F1, and 38.4% of tasks receive no correct localization from any evaluated model.
We further find that stronger localization does not imply reliable behavior after remediation: systems that identify vulnerable files effectively can still report unsupported locations on patched repositories. These results establish vulnerability localization as a distinct repository-scale capability and provide a setting for studying both how security agents search for vulnerable code and when they should refrain from reporting it.

---


### 368. [Discovery Foundation Models: Toward Open-Ended Discovery Intelligence](https://arxiv.org/abs/2609.15973)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ling Yang, Zhenfei Yin, Yingcheng Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Foundation models have progressed from learning and reasoning over existing knowledge, to increasingly learning through action, tool use, and outcome feedback. We argue that the next frontier is a further transition: from solving and acting within problems specified by humans to participating in the process by which new problems, representations, explanations, and knowledge are created. We refer to this capability as Discovery Intelligence. We formulate Discovery Foundation Models (DFMs) as general-purpose model systems for open-ended discovery. A DFM operates over a revisable research state and supports seven coupled capabilities spanning problem discovery, formulation, representation construction, hypothesis formation, intervention, evidence-grounded revision, and continual discovery improvement. We instantiate this framework with Zetema, which couples explicit research-state dynamics, verification and experimental gating, external grounding, and cross-task Discovery Skill evolution. We further ground the framework with GALILEO, a real therapeutic-discovery system in which Dry-Lab reasoning, robotic and hands-on Wet-Lab experimentation, external biological evidence, and iterative hypothesis and design revision form a closed physical discovery loop. We then formulate a unified approach to capability formation and process-centered evaluation, enabling discovery behavior to be trained, improved, and measured beyond final-answer performance. Together, these components establish discovery as a learnable, executable, and evaluable capability of foundation-model systems. We view this shift as a broader progression in intelligence scaling: from learning over existing knowledge, to learning from action outcomes, and ultimately to participating in the construction, testing, and revision of the structures through which new knowledge is discovered. Code: this https URL

---


> [!TIP]
> 当前位于：**351-368**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-368**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
