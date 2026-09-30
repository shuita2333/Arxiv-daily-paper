# 🧠 大模型相关研究 | 2026年10月01日

> 本类共 **515** 篇论文：已确认 **473** 篇，待复核 **42** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**501-515**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-515**

---

### 501. [HyperSAM: A Promptable Foundation Model for Hyperspectral Remote Sensing](https://arxiv.org/abs/2609.37340)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Li Pang, Xinqiao Wu, Jing Yao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral remote sensing provides dense spectral measurements that are indispensable for material-level Earth observation, yet the construction of a general-purpose hyperspectral foundation model remains difficult. Two bottlenecks are especially limiting. First, large hyperspectral corpora rarely provide high spatial resolution together with reliable dense annotations. Second, many hyperspectral models are still trained almost from scratch, so the geometric and interactive priors learned by modern vision foundation models are not fully reused. To alleviate these issues, we \highlight{present} \textbf{HyperSAM}, a promptable hyperspectral foundation model that couples a data-centric hyperspectral synthesis pipeline with a spectral adaptation architecture based on Segment Anything Model 3 (SAM3). On the data side, HyperSAM synthesizes full-spectrum hyperspectral cubes from high-resolution SpaceNet multispectral imagery through a physics-informed abundance-transfer generator, while SAM3-derived pseudo-masks provide object-centric supervision. On the model side, the latest implementation uses a frozen SAM3 RGB image branch, a trainable hyperspectral side encoder initialized from the RGB vision transformer (ViT), ControlNet-style zero-initialized feature injection, and a lightweight mixture-of-experts mask refiner. To enhance training robustness against noisy pseudo-labels, Cross-modal Sample Selection (CromSS)-style confidence selection is incorporated for noisy-label weighting. Extensive experiments show that HyperSAM obtains strong generalization on diverse hyperspectral tasks (e.g., classification, anomaly detection, change detection, target detection, and airborne oil-spill mapping) and that high-quality synthetic hyperspectral data can be more effective than simply scaling noisy hyperspectral supervision.

---


### 502. [Think Before You Score: Thinking Reward Model for Visual Generation](https://arxiv.org/abs/2609.37372)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xuehai Bai, Zhenchen Tang, Yang Shi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual reward models are essential for evaluating and improving visual generation models, yet existing approaches typically map task conditions and candidate outputs directly to scalar rewards, leaving implicit what should be evaluated for each individual case. We introduce Think Before You Score, a paradigm that explicitly determines what matters for each case before judging how well the candidate performs. Following this principle, we propose the Thinking Reward Model (TRM), which formulates case-adaptive rubrics, performs rubric-guided assessment, and produces fine-grained pointwise rewards. We further observe that conventional pairwise preference optimization can induce score polarization, and introduce Pairwise Dual-Group Relative Policy Optimization (PD-GRPO), which leverages pairwise supervision to improve reward discrimination while preserving fine-grained pointwise scoring. Extensive experiments on image generation and editing reward-modeling benchmarks demonstrate that TRM achieves state-of-the-art performance among open-source reward models while remaining highly competitive with proprietary alternatives. Moreover, using TRM as a reward for reinforcement learning consistently improves diverse visual generation models, demonstrating that its fine-grained, case-adaptive rewards translate into effective optimization signals for visual generation.

---


### 503. [MG-Thinker: Bi-Axial Self-Reflection for Multi-Image Reasoning Grounding](https://arxiv.org/abs/2609.37374)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Heyu Huang, Chi Chen, Zonghao Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has recently delivered substantial gains in multimodal reasoning, opening a promising route for fine-grained visual perception. Yet for multi-image reasoning grounding (MRG), reasoning over real-world multi-image contexts toward pixel-precise localization, existing RL-based approaches overlook two characteristics intrinsic to this paradigm: a coarse-to-fine hierarchical reasoning pattern, and heterogeneously distributed task--sample difficulties. In this work, we present MG-Thinker, a post-training RL framework that advances a new MRG paradigm featuring such hierarchical reasoning, supported by a curated 25K MRG dataset with task-adaptive Chain-of-Thought (CoT) annotations that elicit multi-perspective evidence before conclusion. To remedy the heterogeneous task--sample difficulties, we further propose Bi-Axial DAPO (BiA-DAPO), which decomposes rollout advantages along an intra-group signal axis and an inter-group competence axis through two complementary mechanisms, both grounded on our defined candidate pool for stable group-level statistics. Extensive experiments show that MG-Thinker achieves state-of-the-art performance on multi-image reasoning grounding while consistently improving generalization across multi-image understanding and diverse multimodal benchmarks.

---


### 504. [Looped Transformers as Optimizers](https://arxiv.org/abs/2609.37379)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yulong Huang, Chen Jiang, Zhanpeng Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers provide a parameter-efficient approach to depth scaling by repeatedly applying shared Transformer blocks. Recent reasoning models have likewise highlighted the value of scaling test-time computation through longer computation trajectories. However, the principles for designing effective loop transitions remain poorly understood. We view the looped hidden state as a fast weight that is updated throughout the depth. We formulate loop transitions as local gradient-based updates, with recurrent blocks predicting implicit targets at each depth. Our framework derives loop transitions in closed form from a projection, a local objective and an optimizer update rule. Mapping representative loop transitions into this framework reveals mismatches between their transitions and projections. We first align the input maps of existing transitions. We then derive OperLoop, which combines explicit weight decay, adaptive step size and a delta objective. The aligned variants reduce training loss and improve average commonsense accuracy. OperLoop improves average generative performance over the compared looped and non-looped baselines under matched training FLOPs. These results support the framework's usefulness for loop design. We extend the analysis to additional loop models and outline a roadmap for future loop transition design.

---


### 505. [Anatomy-Aware Prediction of Bronchoscopic Accessibility from 3D CT](https://arxiv.org/abs/2609.37386)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Linkai Peng, Cuiling Sun, Bin Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-operative planning for bronchoscopy is critical for the diagnosis of lung lesions. Current accessibility assessment relies on subjective manual inspection of CT scans, which is time-consuming and prone to inter-observer variability. In this paper, we formalize bronchoscopy accessibility prediction as a novel supervised learning task and present the first end-to-end framework to address it. We propose an Anatomy-Aware Mixture-of-Experts (MoE) model that integrates specialized modules: a CT Expert for local morphological features, a Lobe Expert for anatomical priors, and a Path Geometry Expert that encodes the sequential constraints of the bronchial tree. To support this task, we curated the first clinical dataset of 438 cases with pre-operative CT scans and documented procedural outcomes. Experimental results demonstrate that our method achieves an AUROC of 0.8052, significantly outperforming both state-of-the-art baselines and experienced human experts. This work establishes a new benchmark for computer-aided interventional planning in pulmonary medicine. Our data and code will be publicly available at this https URL.

---


### 506. [Label Less, Learn More: Resource-Efficient Active Semi-Supervised Learning for Onboard Satellite Image Annotation](https://arxiv.org/abs/2609.37481)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ahmed Abdelnaby, Mohamed Elmahallawy, Marius Bernahrndt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale pervasive sensing increasingly relies on high-resolution satellite imagery, yet task-specific onboard vision is constrained by costly annotation and limited computation, memory, energy, and communication resources. Existing approaches largely rely on either data-hungry supervised learning or large vision-language foundation models, limiting efficient adaptation and deployment under these constraints. We present SatLabel, a resource-aware learning framework that transforms limited satellite labels into progressively refined onboard models through adaptive sample acquisition and semi-supervised model adaptation. Rather than repeatedly training on uniformly sampled labels, SatLabel closes the loop between model uncertainty, class imbalance, and pseudo-label quality to selectively acquire informative samples while exploiting abundant unlabeled imagery. This enables a compact student to adapt to target sensing domains with reduced annotation and inference costs. We further introduce an optional Mixture-of-Experts (MoE) student with graph-based feature refinement to enhance representation capacity while retaining a lightweight footprint. We evaluate SatLabel on 11 remote-sensing datasets spanning core, extended, and unseen domains against RemoteCLIP zero-shot inference. SatLabel improves Macro-F1 on most core and extended datasets while maintaining strong cross-dataset transfer to unseen domains. More importantly, the Balanced student contains only 11.2 M parameters and occupies approximately 42.8 MB, compared with 151.3M parameters and 577 MB for RemoteCLIP, while requiring 3.65 versus 5.89 GFLOPs. Across four efficiency benchmarks, it achieves approximately 2x higher GPU-forward throughput and reduces energy per image on datasets.

---


### 507. [GeoSET: Generalist Foundation Model for SAR-to-EO Image Translation](https://arxiv.org/abs/2609.37496)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jeonghyeok Do, Munchurl Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Paired synthetic aperture radar (SAR) and electro-optical (EO) imagery is increasingly available across sensors, resolutions, and geographic regions. Yet existing SAR-to-EO image translation (SET) methods are typically trained on a single, limited-scale dataset, producing models specialized to particular sensing conditions. We introduce GeoSET, the first generalist model for SET, built around a single pretrained parent that is adapted to downstream datasets under a common protocol. We curate over 3 million high-quality SAR--EO pairs from a collection of more than 10 million SAR observations, spanning diverse sensors, spatial resolutions, and ground sampling distances. To bridge the modality gap between SAR observations and a pretrained image generator, we develop a speckle-robust SAR encoder and pretrain the conditional generator on this heterogeneous corpus. The resulting parent supports efficient adaptation across downstream datasets through low-rank adaptation (LoRA), updating only 0.60% of the generator parameters and requiring approximately one hour per dataset. Across six downstream benchmarks, GeoSET achieves state-of-the-art results in FID and DISTS with full fine-tuning or LoRA, demonstrating effective transfer across heterogeneous SAR-EO domains.

---


### 508. [Rational Clarification by Assistive Agents via Value-of-Information Reasoning](https://arxiv.org/abs/2609.37588)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** T. Duy Nguyen-Hien, Yee Whye Teh, Wee Sun Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Users of language-based assistive agents often make ambiguous requests. In response, an assistant can either directly act on its interpretation of the request --- risking misalignment with the user --- or ask a clarifying question. Which option is the most safe and helpful? A common approach is to ask questions that minimize uncertainty about the user's intent until a threshold is reached. However, this neglects the impact of uncertainty reduction on downstream performance, the costs of asking versus acting immediately, and the possibility that users may provide corrections without being asked. To navigate these trade-offs, we introduce Rational Enquiry via Value-of-Information Reasoning (REVOIR). REVOIR makes clarification decisions via inference-time reasoning about the value-of-information of a question, which captures the expected improvement in task reward due to the answer received. In two assistive tasks --- ambiguous question answering (CondAmbigQA) and preference-aligned household task planning (ADAPT) --- we show that REVOIR achieves greater success with fewer questions than approaches based on prompting, chain-of-thought, fine-tuning, or information gain, improving preference satisfaction on ADAPT by 13-15% over a fine-tuned clarification policy while requiring no training and asking five times fewer questions. Furthermore, when the assistant can receive cheap user corrections after acting, REVOIR naturally infers that asking questions is not always efficient, demonstrating the adaptivity of our approach. In contrast, we find that vanilla reasoning agents fail to adaptively clarify user requests, and request fewer clarifications as reasoning effort increases.

---


### 509. [TomoTransformer: Towards a Foundation Model for CT Reconstruction](https://arxiv.org/abs/2609.37605)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** AmirEhsan Khorashadizadeh, Benjamín Béjar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised deep learning has advanced sparse-view tomographic reconstruction. However, conventional models, which typically map filtered back-projection (FBP) images or sinograms to clean reconstructions, are brittle under distribution shifts. Because they require retraining whenever projection counts and angles, detector resolutions, or data distributions change, their deployment in real-world applications remains limited. To address this, we introduce TomoTransformer, a transformer-based architecture that treats each \textit{local} filtered projection as an individual token and predicts missing views via self-attention. Crucially, TomoTransformer operates in a \emph{back-projection space} that separates projections across spatial locations, making view interpolation geometrically well-posed and invariant to detector size. This design yields a single foundation model that can process any number of input projections, at arbitrary angular locations and detector dimensions, and query any number of target angles without retraining. Trained on a large-scale dataset spanning diverse medical CT anatomies and natural images, TomoTransformer generalizes effectively across anatomies, materials, and resolutions. Extensive evaluations on several benchmark sparse-view datasets show that TomoTransformer significantly outperforms concurrent multi-purpose models like ViewTrans and matches or exceeds strong protocol-specific baselines, while remaining fully agnostic to the number of input and target projections. Furthermore, the model demonstrates robust zero-shot generalization on real experimental nanoscale brain data collected from an X-ray synchrotron, showcasing its practical utility for real-world applications.

---


### 510. [PolyOCR-Venus: Unified OCR Foundation Models for Text-Centric Visual Intelligence](https://arxiv.org/abs/2609.37712)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** GuangJian Team, Kaili Huang, Yongshuo Zhang 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Character Recognition (OCR) is evolving from plain-text transcription toward general visual intelligence, requiring models to recognize, localize, and reason over textual information in complex visual environments. However, existing OCR systems often excel at only some tasks and struggle to balance recognition, parsing, and reasoning across scenarios. In this report, we present PolyOCR, a family of unified OCR foundation models of varying scales. PolyOCR combines a shared instruction-following framework with a large-scale data engine that converts heterogeneous visual resources into quality-verified OCR supervision. We introduce Competence-Guided Policy Optimization, which combines verifier-based Group Relative Policy Optimization with on-policy distillation through sample-wise routing based on teacher reliability and the teacher--student competence gap. We also introduce OCRBench v2.1, our revision of OCRBench v2 with manually verified annotation corrections and task-aligned scoring metrics. Extensive experiments across OCRBench v2.1, CC-OCR, in-house KIE Benchmark, OmniDocBench v1.6 and MDPBench demonstrate that PolyOCR achieves state-of-the-art or highly competitive performance.

---


### 511. [ReCaVSR: One-Step Streaming Diffusion Video Super-Resolution with Recycled Latents and Learned Cache Routing](https://arxiv.org/abs/2609.37831)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xijun Wang, Xin Li, Suhang Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time diffusion-based video super-resolution (VSR) is in high demand for online streaming, yet stringent latency requirements often compromise generative fidelity. We propose ReCaVSR, a Wan2.2-based, one-step framework for streaming VSR that builds on two observations: recycled SR latents retain local temporal context, reducing the need for full historical Key-Value (KV) caches; and individual transformer layers benefit from distinct temporal scopes. ReCaVSR combines three complementary designs: (i) layer-wise cache routing with recycled SR latents: each DiT layer learns its KV-cache temporal scope under a cache budget and exports a static inference schedule, while recycled SR latents propagate local context by conditioning each new block on the model's own preceding predictions. (ii) Multi-Scope Query (MSQ) Discriminator: a compositional discriminator combining global, spatial-window, and temporal-tube feedback for holistic realism, local texture generation, and temporal stability. (iii) LR-conditioned adaptation of FlashDecoder: a VAE decoder that incorporates LR observations for efficient latent decoding. ReCaVSR enables streaming VSR without iterative sampling or full historical KV-cache materialization. Experiments on synthetic and real-world VSR benchmarks show better perceptual quality, temporal consistency, and streaming efficiency than representative VSR baselines. At $1080{\times}1920$ output resolution on a single NVIDIA A100-80GB, ReCaVSR achieves 21.20 FPS with 15.16 GB peak allocated GPU memory, running 2.72$\times$ faster while using 38.0\% less peak allocated memory than FlashVSR Tiny. The code is available at this https URL.

---


### 512. [Learning Beyond What You Sample: Off-Policy-Aware Cross-Model Trajectory Exchange for RLVR](https://arxiv.org/abs/2609.37868)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Doohyuk Jang, Yoonsik Park, Gyouk Chu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) methods such as GRPO rely on successful self-generated trajectories, but finite rollout budgets can produce all-fail groups with no reward-based policy-gradient signal. While additional rollouts improve the chance of success at higher cost, successful trajectories missing from one model's rollouts may already have been discovered by another. Indeed, we observe that heterogeneous models often succeed on complementary prompts, creating opportunities for mutual learning without a designated stronger teacher. To exploit this complementarity, we propose GRAFT (Gated Replacement of Answer-Failed groups with peer Trajectories), an off-policy-aware framework that replaces all-fail groups with informative peer groups. GRAFT transfers both successful and unsuccessful peer responses with peer-computed advantages, while controlling cross-model mismatch through sequence-level compatibility weighting and token-level importance ratio clipping. Across three heterogeneous model pairs and five mathematical reasoning benchmarks, GRAFT consistently improves both models over GRPO with the same per-model rollout budget, gaining 2.1 points on average and up to 4.5 points in model-level average performance. Stored peer trajectories preserve most of the gains, improving over GRPO by 1.8 points on average without simultaneous co-training.

---


### 513. [Retrieval-Augmented Skill Optimization via Cross-Harness Adaptation](https://arxiv.org/abs/2609.38024)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jaewon Chu, Ji Soo Lee, Jihwan Park 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent skill is a reusable, actionable natural-language artifact that guides an agent to perform a task effectively under a given harness. Recent studies have explored the optimization of agent skills, contributing to a growing collection of publicly available skills spanning diverse tasks, domains, and harnesses. Despite millions of publicly shared skills, existing skill optimization methods largely overlook this accumulated knowledge, instead relying solely on expensive agent rollouts to iteratively refine skills for a target task. To address this, we propose \textbf{Retrieval-Augmented Skill Optimization (RASO)}, a framework that leverages an external skill corpus as prior knowledge throughout skill optimization. RASO retrieves relevant knowledge from existing skills and adapts it to the target task and harness via Cross-Harness Adaptation, accounting for mismatches in both domain and harness. RASO comprises two complementary stages: \textbf{Retrieval-Augmented Skill Initialization (RASI)} constructs a knowledge-grounded initial skill without requiring agent rollouts, while \textbf{Retrieval-Augmented Skill Update (RASU)} iteratively refines the skill by retrieving external knowledge guided by execution feedback. Across four agent benchmarks and two models, extensive experiments show that RASO consistently outperforms baselines without retrieval-augmented skill initialization and updating.

---


### 514. [A foundation model for energy and radiation systems built on heterogeneous scientific interfaces](https://arxiv.org/abs/2609.38067)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Samrendra Roy, Tapas Tripura, Yoon Pyo Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific foundation models are commonly evaluated after heterogeneous physical problems have already been translated into a compatible gridded, tokenized or symbolic representation. This leaves the scientific interface outside both the pretrained model and the audit of what is actually reused. We study the complementary setting in which boundary histories, sparse monitor records and loading histories retain their native inference classes and their outputs remain on Cartesian, latitude-longitude and unstructured domains. GEODE couples task-specific scientific interfaces to a shared routed library of wavelet operators. A single jointly pretrained model represents cavity flow, radiation dose and elastoplastic stress, then acquires a heat exchanger and a reactor subchannel by training a private interface containing 2.1% of its parameters. Earlier predictions remain unchanged by parameter isolation, whereas unrestricted fine-tuning degrades them by factors of 14-29. Crucially, preservation alone does not establish reuse: norm-matched randomized-library controls show that the contribution of pretrained computation is conditional on the task and data regime. A separate decomposition shows that full-field relative L2 error can substantially understate error relative to spatial variation when field level dominates the norm. Task-specific operators remain more accurate on three of the five problems. These results distinguish multi-task coverage, preservation and pretrained reuse as separate properties that must be tested independently when scientific foundation models span heterogeneous interfaces.

---


### 515. [Character Training for Risk-Averse Agents](https://arxiv.org/abs/2609.38093)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Arav Dhoot, Punya Syon Pandey, Jamie Johnson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Risk aversion in resources could prevent misaligned AI agents from causing catastrophic harm. Misaligned but risk-averse agents would tend to favor safer strategies like making deals with humans over riskier strategies like rebelling. We train agents to be risk averse through character training, finding that persona traits provide a robust mechanism for instilling risk preferences. To do this, we construct a model constitution describing constant absolute risk aversion (CARA) over an agent's resources and instill it through on-policy distillation. Despite never seeing the benchmark's decision format during training, character-trained models are competitive with baselines trained directly on it, and generalise better than them out of distribution on two of our four models. We also modulate different aspects of the constitution, finding that token budget and model choice are the most influential aspect of character training to instill risk aversion. We conclude from these results that character training is a promising and scalable way to instil broad dispositions, which we can use to our advantage in mitigating risk from misaligned AI agents.

---


> [!TIP]
> 当前位于：**501-515**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-515**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
