# 🧠 大模型相关研究 | 2026年07月24日

> 本类共 **92** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-92**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-92**

---

### 51. [Auto-Fill: Learning to Predict Missing Values Accurately with Specialist Language Models](https://arxiv.org/abs/2607.19847)

**<font color=#1a73e8>作者：</font>** Yurong Liu, Yeye He, Haoyu Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting missing cell values in tabular data is a fundamental problem in data cleaning. While state-of-the-art reasoning models show great promise in predicting missing values in tables, by reasoning holistically across rows and columns, they are costly to deploy at scale and tend to be overconfident, often generating hallucinated or false-positive predictions.
In this paper, we observe that achieving high-precision missing-value prediction in tables requires a distinct combination of three capabilities: (1) world knowledge, (2) text-based reasoning, and (3) code-based reasoning. We systematically explore design choices for combining these capabilities, and propose an Auto-Fill approach that post-trains three specialist small language models (SLMs), each optimized for one capability. We develop a calibrated ensemble mechanism that either dynamically selects the most confident specialist or abstains, ensuring high accuracy.
Extensive experiments on 11 benchmarks with 2200 real tables drawn from diverse domains show that Auto-Fill achieves superior accuracy compared to state-of-the-art reasoning models (e.g., o3-pro, Gemini 3 Pro, and DeepSeek R1), while operating at a fraction (less than 1%) of the cost of these frontier models. Our results highlight the effectiveness of specialization and calibrated abstention in the important domain of tabular data. Auto-Fill is publicly available at this https URL.

---


### 52. [Memory-Augmented Multimodal Large Language Models for Small Object Understanding in Streaming Aerial Videos](https://arxiv.org/abs/2607.19857)

**<font color=#1a73e8>作者：</font>** Penglei Sun, Yehua Huang, Zhuoli Tao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-guided aerial perception aims to understand user-specified tiny targets in complex unmanned aerial vehicle (UAV) scenes. In real UAV deployment, the UAV must respond while it flies, so such perception runs in an online streaming manner, where frames arrive sequentially and the model responds to each one without access to future frames. However, applying current Multimodal Large Language Models (MLLMs) to this setting raises two challenges. First, targets viewed from the air are often tiny, yet the visual compression in existing MLLMs treats all regions equally and discards their fine-grained details. Second, understanding a continuous stream requires past-frame context, yet retaining the entire history is infeasible on resource-constrained onboard hardware, whereas discarding it causes the target to drift or disappear. We address the tiny object and streaming challenges from both data and method perspectives. From the data perspective, we present \textbf{DroneEyes}, the \textbf{first} pixel-level and open-vocabulary referring-segmentation dataset for tiny aerial targets, comprising $2,140$ high-definition videos and $176,623$ pairs across Object Description and Referring Expression tasks, with dense per-frame masks. From the method perspective, we propose \textbf{SkyAnchor}, an MLLM with two designs to the above challenges: a Semantics-Aware Token Router that preserves small-target under a reduced visual-token budget, and a Hierarchical Memory Bank that keeps the target consistently understood on streams.

---


### 53. [MTVDiff: Multimodal Conditional Latent Diffusion for Enhanced Thermal-to-Visible Face Translation](https://arxiv.org/abs/2607.19886)

**<font color=#1a73e8>作者：</font>** Zhiyuan Xia, Haojie Li, Jingyu Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal-to-visible face translation presents fundamental challenges including geometric discontinuities, semantic attribute mismatches, and identity degradation. We propose MTVDiff, a novel multimodal latent diffusion framework that synergistically integrates depth and textual information to address these limitations while preserving identity characteristics. The MTVDiff framework presents three core technical contributions: (1) a Dual-Branch Cross-Attention Fusion (DBCAF) module for multi-scale thermal-depth feature extraction and fusion; (2) a Gated Text-to-Visual Feature Alignment mechanism for semantically-guided generation; and (3) Spatial Feature Transformations (SFT) for adaptive multimodal prior integration. Extensive experiments on the MCXFace and SpeakingFaces datasets demonstrate that our multimodal approach significantly outperforms existing GAN-based and diffusion-based approaches across multiple metrics, achieving substantial improvements in both image quality and face verification performance, with FID reductions of up to 48.3% and Rank-1 accuracy improvements of up to 8.9\%. Our work provides a robust solution for face recognition systems operating under varying illumination conditions and advances the state-of-the-art in cross-spectral facial image translation through effective multimodal integration.

---


### 54. [LAVIFT: Latent-Action-Guided Vision Fine-Tuning for Surgical Interaction Recognition](https://arxiv.org/abs/2607.19889)

**<font color=#1a73e8>作者：</font>** Jiajun Cheng, Subarna Tripathi, Sainan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding instrument-tissue interactions is essential for context-aware surgical AI and autonomous robotic surgery. Pretrained vision-language models (VLMs) and vision encoders offer an alternative to conventional interaction classifiers by transferring broad visual and semantic knowledge. However, adapting them to fine-grained surgical interactions remains challenging: (1) freezing the vision encoder depends entirely on pretrained representations that may retain noise and provide weak spatial localization, while (2) full fine-tuning can improve global semantic alignment without ensuring that the encoder learns meaningful features in the correct action region. We address these limitations by introducing LAViFiT, an end-to-end latent-action-guided framework for vision-language fine-tuning. An inverse dynamics model captures the visual changes induced by each action, while a forward world model drives the encoder to represent action-relevant regions. A patch-level SIG Regularizer further prevents local feature collapse without additional supervision, such as bounding boxes or pseudo-labels. Experiments across multiple encoders and datasets improve recognition and image-text alignment, while representation analyses show stronger grounding over the complete instrument-tissue interaction region and more spatially coherent features.

---


### 55. [MV-Bench: Benchmarking Multimodal Large Language Models for Coordinated Multi-View Interface Construction](https://arxiv.org/abs/2607.19910)

**<font color=#1a73e8>作者：</font>** Yue Zhao, Hongxu Liu, Feiyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly expected to automate visualization development by generating code directly from visual designs. However, existing evaluations mainly focus on single-chart generation and overlook coordinated multi-view interface construction, which requires joint reasoning about data semantics, view coordination, and interaction logic. Consequently, MLLM capabilities in this setting remain underexplored, and the field lacks a dedicated benchmark for systematic assessment. We introduce MV-Bench, a benchmark for evaluating MLLMs on coordinated multi-view interface construction. Instead of relying on incomplete or inconsistent open-source implementations, we use Tableau workbook files as ground truth because they explicitly encode data bindings, visual mappings, and interactions. We develop a multi-stage pipeline that converts these specifications into executable web interfaces through structured intermediate representations. The benchmark contains 92 base interfaces and 1,048 verified instances created by recombining chart types, datasets, and interaction patterns. Each instance includes executable code, a rendered interface, a dataset, and interaction annotations. We evaluate five state-of-the-art MLLMs in a single-pass setting using metrics for visual fidelity, data binding correctness, and interaction completeness. The strongest model achieves 75.45 percent accuracy in visual layout reproduction, but only 21.71 percent in data binding and 11.68 percent in interaction completeness. These results show that current MLLMs can reproduce visual appearance but remain limited in generating the data semantics and interactive logic required by coordinated multi-view interfaces. Iterative refinement improves code executability but does not substantially reduce the gap in data binding and interaction generation.

---


### 56. [WearWow: Native 2K Multi-Garment Virtual Try-On via Adaptive Token Packing and Preference Alignment](https://arxiv.org/abs/2607.19923)

**<font color=#1a73e8>作者：</font>** Xujie Zhang, Runyan Du, Song Chang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing native 2K multi-garment virtual try-on is a formidable frontier in digital fashion, critically bottlenecked by two fundamental limitations: the O(N^2) memory explosion induced by 2k conditions, and the spectral bias of diffusion models that over-smooths high-frequency fabric details. We present WearWow, an end-to-end, mask-free generative framework that pioneers ultra-high-resolution multi-garment synthesis. To mitigate the memory explosion , we propose Adaptive 2D Token Packing (ATP). ATP leverages inherent garment sparsity to algorithmically pack heterogeneous items onto a unified 2D canvas and prune uninformative background tokens, minimizing the effective sequence length and subsequent memory overhead while rigorously preserving 2D spatial priors. To rectify texture degradation, we introduce the Multi-dimensional Try-on Reward (MTR) system. MTR synergizes a Semantic Guidance Reward to explicitly drive tactile restoration with a Cloth Distribution Reward to implicitly anchor the physical distribution, a joint formulation that effectively mitigates the severe reward hacking. Furthermore, we curate WearWow-2K, an extreme-quality dataset comprising native 2K triplets, providing physically correct spatial interactions that naturally empower the model's mask-free generation. Extensive experiments demonstrate that WearWow establishes a new state-of-the-art, exceeding existing commercial baselines in native 2K multi-garment synthesis.

---


### 57. [Efficient Chain-of-Modality Reasoning via Progressive Compression for Spoken Language Models](https://arxiv.org/abs/2607.19932)

**<font color=#1a73e8>作者：</font>** Pengchao Feng, Chao-Hong Tan, Qian Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spoken language models (SLMs) enable natural human-computer interaction, but their reasoning ability still lags behind that of text-based large language models, especially on spoken mathematical question answering tasks. One important reason is that SLMs reason over purely verbalized mathematical expressions, which are harder to interpret than symbolic text. However, directly transferring text-based reasoning to SLMs is nontrivial due to architectural constraints and the additional computational requirements. To address this challenge, we propose Efficient Chain-of-Modality Reasoning (ECoM Reasoning), the first framework to introduce compressed reasoning into SLMs. By compressing the textual component so that it jointly serves as speech guidance and reasoning representation, ECoM Reasoning improves reasoning accuracy while using a smaller token budget than the standard Chain-of-Modality (CoM) architecture, which generates intermediate text before speech. To train this capability, we further propose Progressive Compression, a curriculum-based strategy that gradually trains the model from full-form reasoning to compressed reasoning. Experiments on spoken mathematical question answering benchmarks show that ECoM Reasoning improves accuracy by 21% over standard CoM without explicit reasoning, and by 3% over CoM with full reasoning traces while using only 40% of the text tokens, demonstrating that it enhances SLM reasoning while remaining inference-efficient.

---


### 58. [MOF-Sleuth: Tool-Grounded Reward Alignment for Explainable Fine-Grained MOF CIF Auditing](https://arxiv.org/abs/2607.19935)

**<font color=#1a73e8>作者：</font>** Yu Liu, Zhiwei Yang, Diandian Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large metal-organic framework (MOF) databases support simulation, screening, and machine learning through crystallographic information files (CIFs). Subtle chemical and structural errors in these inputs can compromise downstream results and hinder manual inspection. LLM advances in computational chemistry offer paths beyond predictive screening toward fine-grained diagnosis with evidence-grounded explanations. However, two challenges remain: (i) limited fine-grained attribution: MOF-specific validators and machine-learning models scale detection but provide fixed checks, readiness scores, or coarse labels rather than evidence-grounded explanations; and (ii) unreliable CIF reasoning: direct LLM auditing is costly and unreliable because chemical evidence is implicit across atom-site records and requires geometric, connectivity, occupancy, and charge calculations. Both stem from weak coupling between chemical evidence and language-model explanation. We introduce MOF-Sleuth, a reinforcement-guided CIF auditing agent with two modules: a deterministic Forensic Lab and a Sleuth reasoning engine. The Lab derives composition, geometry, connectivity, occupancy, coordination, and charge evidence, and Sleuth uses this evidence to produce an evidence-grounded explanation, error types, and a binary decision. Reward-guided reinforcement learning (RL) turns tool measurements into chemical explanation-level supervision, rewarding not only the final answer but also cited chemical evidence and evidence-supported diagnoses. We introduce Chemically Grounded Diagnosis (Chem-GD), a metric that assesses whether a correct diagnosis is explained by factual, relevant CIF-derived evidence. Across four benchmarks, MOF-Sleuth establishes state-of-the-art performance among LLM-based approaches and MOF-specific machine-learning methods, demonstrating gains in detection, attribution, and grounded explanation quality.

---


### 59. [ETPDesigner: Multi-Agent Orchestration for Interactive Multimodal Electronic Theater Program](https://arxiv.org/abs/2607.19947)

**<font color=#1a73e8>作者：</font>** Mengtian Li, Xinru Guo, Xiaoru Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Electronic Theater Programs (ETPs) serve as critical promotional media in the performing arts, comprising a multi-page collection of heterogeneous visual assets such as theatrical posters, performance details, and character portraits. However, existing text-to-image paradigms struggle with such complex design tasks due to their inability to comprehend long-context narratives and maintain visual consistency across multiple distinct pages. To address this, we introduce ETPDesigner, a collaborative Multi-Agent framework that directly synthesizes high-quality ETPs from raw dramatic scripts. Emulating a professional design pipeline, our framework orchestrates specialized agents for semantic script analysis, core poster synthesis, functional background generation, and the stratified composition of character assets. Central to ETPDesigner is a global style anchor mechanism that extracts visual priors from the core poster to enforce strict aesthetic uniformity across all generated components. Furthermore, we elevate the ETP from a static publication to an immersive interactive companion. By integrating portrait animation, customized speech synthesis, and persona-grounded Large Language Models (LLMs), our system enables users to engage in real-time, voice-enabled conversations with the generated virtual characters. To rigorously benchmark this task, we construct ETP-Pro, a domain-specific benchmark of professional theater posters and high-quality character portraits. Extensive evaluations demonstrate our method's superiority in producing semantically faithful, aesthetically consistent, and highly interactive program sets.

---


### 60. [EvoThink: Evolving Thinking in Large Reasoning Models via Self-Pruning and Aha-Moment Preference Optimization](https://arxiv.org/abs/2607.19962)

**<font color=#1a73e8>作者：</font>** Xinbang Dai, Zheyu Xin, Huikang Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) often suffer from overthinking due to redundant verification steps. Existing approaches for mitigating overthinking, such as fast-slow thinking switching and reasoning trajectory compression, fail to make a fine-grained distinction between beneficial and redundant steps within the LRM's reasoning process, and may thus impair reasoning capability in their pursuit of efficiency. To simultaneously improve reasoning efficiency and capability, we propose EvoThink, a framework that reduces redundant verification and encourages the exploration of new reasoning paths. EvoThink comprises two key components: Self-Pruning Training (SPT), an unsupervised method that iteratively prunes redundant reasoning steps and self-trains on the concise trajectories; and Aha-Moment Preference Optimization (AMPO), which, inspired by genetic algorithms, identifies valuable failed reasoning attempts, synthesizes from-wrong-to-right aha-moment data, and optimizes the model to internalize this reasoning pattern. Extensive evaluations across mathematical reasoning and code generation benchmarks demonstrate that EvoThink not only substantially reduces inference-time token usage but also improves the reasoning capability of LRMs.

---


### 61. [Forecasting the Number of Harvest-ready Fruits of Sweet Peppers Using Multimodal Time-Series Data](https://arxiv.org/abs/2607.19975)

**<font color=#1a73e8>作者：</font>** Enrico Pallotta, Mohamed Farag, Esra Guclu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate yield forecasting at the individual-plant level is critical for precision agriculture and supply-chain planning, yet public datasets capturing both visual growth dynamics and per-plant measurement labels are scarce. In this paper, we introduce a novel, annotated image time-series dataset of 691 sweet pepper plants monitored over two growing seasons, comprising 4837 images with per-plant fruit counts categorized by maturity. We propose a multimodal deep learning framework that fuses high-dimensional image features, extracted using the DinoV3 encoder, with numerical count measurements. Our architecture utilizes a Long Short-Term Memory (LSTM) network to model temporal dependencies and handles irregular sampling intervals common in greenhouse monitoring. Through quantitative experiments, we demonstrate that this multimodal approach reduces RMSE over a persistence baseline by 33% and 38% in the 2022 and 2023 seasons, respectively, with a further 1.2% average gain over a measurement-only model. Furthermore, we employ Deep Ensembles and Gaussian Negative Log-Likelihood (NLL) to provide calibrated uncertainty estimates, with an Uncertainty Calibration Error (UCE) ranging from 0.39 to 0.89 depending on the cross-season evaluation direction, offering a principled confidence signal for real-world agricultural decision-making. We release the dataset and code to support reproducible research and to accelerate development of data-driven yield forecasting methods for horticultural crops.

---


### 62. [TINY_SCHILLER: A Drop-In German Drama Corpus for Small Language Models](https://arxiv.org/abs/2607.19992)

**<font color=#1a73e8>作者：</font>** Mark Schutera  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> tiny_schiller closes the small-language-model prototyping, fine-tuning, education, and research gap for German literary text, providing a single-file, drop-in counterpart to Karpathy's tiny_shakespeare. The available German literary corpora are larger and richer, but require parser engineering before a single line of training or fine-tuning code can run. tiny_schiller is a 2.07-megabyte single file of eleven public-domain Schiller dramas, sourced from DraCor's GerDraCor export (CC0) and processed by deterministic parser engineering. Character-level, GPT-2 byte-pair encoding, and cl100k_base tokenization splits, an instruction-formatted dialogue-completion split, and 89 per-character persona splits load from a single HuggingFace call. A small language model literally reaches German literary text in one line of code.

---


### 63. [Post-Training in Time Series Foundation Models: A Unifying Framework](https://arxiv.org/abs/2607.20002)

**<font color=#1a73e8>作者：</font>** Shifeng Xie, Ambroise Odonnat, Zehao Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) have emerged as general-purpose models for time series analysis, but pretraining alone is often insufficient for reliable downstream deployment. Bridging this gap requires further intervention to handle domain shift, task heterogeneity, limited supervision, and computational constraints, which motivates post-training as a broad class of methods to adapt, augment, compose, calibrate, or specialize pretrained TSFMs for downstream tasks. In this work, we analyze TSFM post-training methods based on their locus of intervention in the prediction pipeline, yielding five categories: parameter adaptation, context augmentation, model composition, output processing and uncertainty control, and compression and specialization. Within each category, we study main representative methods and discuss their current limitations. We further identify future directions toward controlled adaptation, reliable context construction, uncertainty-aware model composition, calibrated output processing, and deployment-aware specialization. Overall, by providing a unifying framework for the emerging TSFM post-training landscape, this work aims to support future research to navigate the design space between a pretrained TSFM and its reliable downstream deployment.

---


### 64. [EvoDRC: A Self-Evolving Agentic Framework for Automated DRC Violation Repair](https://arxiv.org/abs/2607.20019)

**<font color=#1a73e8>作者：</font>** Bing-Yue Wu, Chia-Tung Ho, Haoyu Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Design rule check (DRC) closure remains a major bottleneck in advanced-node physical design. Although detailed routers are rule-aware, residual design rule violations (DRVs) often require manual engineering change order iterations. Automating this process is challenging because repairs must account for complex geometric interactions, preserve circuit connectivity, and avoid introducing new violations. We present EvoDRC, a skill-evolution framework for agentic block-level DRC repair. EvoDRC initializes layer-specific repair skills using knowledge distilled from an unrelated reference design and continuously evolves these skills using traceable repair experience collected from the target design. EvoDRC decomposes the layout into bounded repair regions and assigns an LLM repair agent to each region. Local DRC analysis, connectivity-checking, and impact-preview tools provide feedback on proposed modifications. Repair operations and their resulting DRV changes are stored in a knowledge database and used to evolve the repair skills. Experiments on seven block-level designs from the DAC26 DRC Benchmark show that EvoDRC achieves a 73.5\% overall reduction compared to the reported baseline.

---


### 65. [Zero-Shot Heart Rate Variability Forecasting from Consumer Wearables Using Time Series Foundation Models](https://arxiv.org/abs/2607.20027)

**<font color=#1a73e8>作者：</font>** Luukas Peräkylä, Fahad Sohrab, Ville Hautamäki 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short-term Heart Rate Variability (HRV) forecasting could provide clinicians with actionable lead time for detecting autonomic dysfunction and adverse cardiac events. Consumer wearable devices generate fragmented, artifact-rich HRV signals that challenge conventional forecasting approaches. In this study, we evaluated the forecasting ability of three Time Series Foundation Models (TSFMs), TimesFM, Chronos, and MOIRAI, against traditional baselines (Mean, Exponential Smoothing, and Exponentially Weighted Moving Average) on real-world wearable data collected from 49 healthy individuals. To address data fragmentation, we introduce a variability-preserving imputation method that augments linear interpolation with locally adaptive stochastic noise, retaining physiological dynamics essential for accurate forecasting. The results show that TSFMs outperformed all baselines without fine-tuning, achieving average Mean Absolute Scaled Error (MASE) between 0.81 and 0.87 across TSFMs and both context lengths (32 and 64 time steps), with Chronos and TimesFM as the top models, though MOIRAI showed limited gains over baselines. With up to a 2-hour forecast horizon, the results establish a baseline for TSFMs' performance on a real-world dataset, highlighting domain-specific fine-tuning as a promising direction for clinical deployment.

---


### 66. [Language-Specific versus Cross-Lingual Knowledge Graphs for Implicit Aspect Identification in Arabic: A Comparative Study of Reasoning and Adaptation Strategies](https://arxiv.org/abs/2607.20056)

**<font color=#1a73e8>作者：</font>** Lujain A. Alawwad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect-based sentiment analysis (ABSA) in Arabic must recover both explicitly stated aspects and implicit aspects that are never named in the text. Implicit identification typically relies on an auxiliary knowledge source (e.g., a knowledge graph (KG)) linking opinion cues to aspect categories, but for a lower-resource language the practitioner faces a design choice: reuse a mature English KG through multilingual embeddings, or build a smaller native Arabic KG. This paper reports a controlled comparison of the two strategies within a single hybrid pipeline, evaluated on three Arabic benchmarks (M-ABSA, SemEval-2016 Arabic, and HAAD). We further compare two adaptation strategies for the generative extractor that feeds the KG -- zero-shot prompting versus task-specific fine-tuning of an 8B-parameter large language model (LLM). The native Arabic KG (Strategy 2) outperforms the cross-lingual English KG (Strategy 1) by +0.199 micro-F1 on M-ABSA and +0.251 on SemEval-2016, gaining on both precision and recall. Task-specific fine-tuning raises explicit-extraction micro-F1 from <= 0.13 (zero-shot) to 0.66-0.76 on M-ABSA and SemEval-2016 (0.45 on the smaller HAAD), confirming that task adaptation, rather than model scale, is decisive in a morphologically rich language.

---


### 67. [Reading and Steering Representations of Materials-Science Mechanisms in an Open-Weight Language Model](https://arxiv.org/abs/2607.20058)

**<font color=#1a73e8>作者：</font>** Markus J. Buehler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can answer scientific questions, yet a correct output does not reveal whether the model represents or uses the governing physics. Here we show that materials science mechanism information in the open-weight google/gemma-4-E4B-it model has three experimentally separable forms: concepts are readable in individual hidden states, constitutive orientation is carried by controlled transformations between states, and selected internal representations causally control engineering answers. We combine matched direct and Jacobian vocabulary readouts, option-free state geometry, a 60-law counterfactual benchmark and causal interventions. In 50 held-out materials descriptions, three independently fitted Jacobian lenses reproduced concept ranks, and target-free word sets from both readouts enabled blinded identification of 9 of 10 mechanism families. A separate 72-prompt benchmark produced mechanism-specific hidden-state neighborhoods, but an exact graph audit showed that this apparent physical organization was equally explained by numerical comparison. We therefore compared otherwise identical prompts in which only the direction of the physical input was reversed, asking whether the resulting hidden-state movement followed the supplied constitutive law. These state transformations ordered direct, physically neutral and inverse laws across 60 frozen relations and correctly oriented 39 of 40 directional laws, whereas lexical controls were near chance. Bidirectional interventions shifted answer probabilities toward or away from the physically appropriate outcome across all 12 matched cases, while counterfactual state patches transferred opposing decision signals across mechanisms and answer formats. Physical relationships were therefore more visible in controlled state changes than in absolute states alone.

---


### 68. [Solar Open 2 Technical Report](https://arxiv.org/abs/2607.20062)

**<font color=#1a73e8>作者：</font>** Sungrae Park, Sanghoon Kim, Gyoungjin Gim 等 53 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Solar Open 2, a 250B-A15B Mixture-of-Experts language model built for long-horizon agentic tasks, scaled up from Solar Open 1 (Solar Open 100B). To hold entire agent trajectories in a single context, Solar Open 2 reaches a 1M-token window through a hybrid attention stack that interleaves one softmax layer among every three linear-attention layers, using no positional encoding and a gated delta rule extended to negative eigenvalues. To train at this scale under a fixed compute budget, we make training efficient in two ways: a stronger starting point, and higher-value data. For the starting point, we initialize Solar Open 2 from Solar Open 1, transferring the 5.69B-parameter shared skeleton that survives the architectural change and learning everything else through full pre-training. For the data, we curate for value per token: quality- and rarity-aware data curation and mixture-ratio optimization refine a 20T pool into a 10T mixture that, at equal token budget, outperforms the Solar Open 1 recipe. To build its agent skills, we train twelve domain specialists across purpose-built scenarios, then consolidate them into a single model by Multi-teacher On-Policy Distillation (MOPD). Against comparably sized open-weight models on English benchmarks, Solar Open 2 leads on MMLU-Pro, LiveCodeBench, and the APEX-Agents agentic suite, and stays competitive with the strongest (DeepSeek-V4-Flash and MiMo-V2.5) elsewhere. On Korean benchmarks, Solar Open 2 records the highest average of any model compared, including fast-tier closed APIs, and on Ko-GDPval, an in-house Korean officework-agent benchmark, it is competitive with DeepSeek-V4-Pro (1.6T) at less than a sixth of its size.

---


### 69. [PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning](https://arxiv.org/abs/2607.20064)

**<font color=#1a73e8>作者：</font>** Alexis Fox, Junlin Wang, Paul Rosu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon tasks require sustained perception, reasoning, and exploration, and are a persistent challenge for large language model (LLM) agents. This gap is reflected in their limited performance on continual learning benchmarks such as ARC-AGI-3, especially when models are evaluated out of the box. Various agent harnesses have been proposed to close this gap, and each commits to a strategy for handling long sequences of observations, i.e., what information to save from the environment and how to load it into model context, a choice we argue is particularly consequential. Existing methods for context management face a significant tradeoff, as preserving more information makes retrieving relevant details less tractable. We propose PRO-LONG, a minimal context management framework built around programmatic memory for LLM agents in long-horizon, exploratory settings. PRO-LONG addresses the tradeoff by keeping a complete, structured interaction log and capitalizing on recent progress in coding agents to search this history efficiently. On the full ARC-AGI-3 public game set, PRO-LONG improves over a base coding agent by an average of 18.0 percentage points across frontier models, and matches or exceeds state-of-the-art specialized harnesses (up to 76.1% pass@1) while using 4.2-5.8x fewer tokens. With Fable 5, PRO-LONG achieves 97.4% best@2 at a total cost of \$1,750. Relevant code and logs are available at this https URL.

---


### 70. [Co-Evolving LLM Evaluators and Policies via DynamicRubric](https://arxiv.org/abs/2607.20083)

**<font color=#1a73e8>作者：</font>** Beining Wang, Weihang Su, Hongtao Tian 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training with evaluator feedback on policy-induced samples serves as a major mechanism for improving large language models. As policies improve, these sampled responses become close in quality. These close candidates create a bottleneck for policy optimization: collapsed relative evaluator score gaps yield weak or misleading policy supervision. We theoretically characterize why these gaps matter through a probability allocation view, showing that the directional gain of shifting probability mass from one response to another is exactly the evaluator score gap between them. This identifies relative score gaps as the policy optimization signals that guide updates. Motivated by this view, we propose DynamicRubric, a response-set-conditioned evaluator--policy co-evolution framework that generates weighted binary rubric items for each candidate set and aggregates the resulting judgments into response-level scores. In our experiments with 8B backbones, DynamicRubric improves evaluator performance and provides stronger policy supervision than baselines using a 70B reward model or a 235B static rubric generator. DynamicRubric-optimized policies also show gains on verifiable reasoning and coding tasks. A DynamicRubric-optimized model is fully deployed in WeChat Search's AI answering scenario, where it serves all online traffic across tens of millions of requests per day and improves key online metrics. These results suggest a principle for evaluator-guided post-training: evaluators should evolve with the policies they supervise.

---


### 71. [Development of an automated, reliable, and clinically meaningful artificial intelligence (AI) tool for diagnosing cardiac disease from conventional cardiovascular magnetic resonance (CMR) images](https://arxiv.org/abs/2607.20087)

**<font color=#1a73e8>作者：</font>** Sina Amirrajab, Volker Vehof, Michael Bietenbeck 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aims: Cardiovascular magnetic resonance (CMR) imaging enables non-invasive assessment of myocardial structure, function, and pathology, but requires substantial experience in interpretation of CMR images that could be supported by artificial intelligence (AI)-based models. However, use of AI models for enhanced CMR reading is limited by labor-intensive data curation, suboptimal model performance, and unclear implementation pathways. Methods and results: We developed an automated data curation pipeline for CMR-based cardiovascular disease (CVD) diagnosis, integrating open-source locally-run large language models (LLMs) to extract diagnostic labels from narrative CMR reports and preprocessing multimodal imaging data, including cine and late-gadolinium-enhancement (LGE) CMR sequences. Three vision foundation models (DINO, VST, UMedPT) were fine-tuned across these modalities in a two-stage approach. The dataset comprised hypertrophic cardiomyopathy (HCM), dilated cardiomyopathy (DCM), ischemic cardiomyopathy (ICM), cardiac amyloidosis (CA), and normal controls (NOR). A total of 988 curated cases were randomly divided into 742 for training and 246 for validation. Fine-tuned AI-models achieved high discriminative diagnostic performance on an independent test set comprising 1067 patients , with individual AUC-ROC values of up to 0.937 for the correct diagnosis of HCM and 0.945 for cardiac amyloidosis. Ensemble strategies combining multiple models and modalities further improved AI-based diagnostic accuracy and robustness, achieving the highest overall diagnostic performance for HCM (AUC=0.959, CI [0.936-0.978]), CA (AUC=0.966, CI [0.939-0.986]), NOR (AUC=0.872, CI [0.852-0.894]), DCM (AUC=0.848, CI [0.808-0.885]) and ICM (AUC=0.840, CI [0.809-0.868]). All training and inference code, along with the trained model weights, are publicly available on this https URL.

---


### 72. [Reinforcement Learning for Large Language Model Selective Evidence Adoption from Contaminated Retrieval Results](https://arxiv.org/abs/2607.20090)

**<font color=#1a73e8>作者：</font>** Yanyu Chen, Yue Li, Yongyi Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented large language models frequently face contexts that interleave useful evidence with misleading statements or instruction-like content. Blanket refusal discards valid evidence, whereas uncritical adoption yields incorrect or unsafe answers. The ability to selectively adopt relevant information while rejecting deceptive or harmful content is therefore critical for reliable deployment in real-world retrieval settings. We introduce SelectBench, a controlled benchmark and training set for selective evidence adoption, and post-train Qwen3.5-4B directly with DAPO using either deterministic rule rewards or a frozen semantic judge. On the corrected 325-example SelectBench-v2 test set, strict success rises from 22.46% for the original checkpoint to 25.54% with DAPO-Rule and 26.46% with DAPO-DeepSeek. Both trained policies reduce forbidden-content adoption and produce shorter, more focused responses, yet prompt-injection following does not improve. The paired gains are modest and fail to survive Holm correction, suggesting that stronger reward shaping or additional training iterations may be needed for more robust gains. DAPO-DeepSeek exhibits no material degradation on MMLU or clean HotpotQA, indicating that the post-training procedure preserves general capabilities. These results demonstrate a directional improvement in selective evidence use, while identifying injection resistance and statistical robustness as important remaining challenges for future work.

---


### 73. [ENTRAP-VL: A Taxonomic Probe for Dual Contextual Entrainment in Vision-Language Models](https://arxiv.org/abs/2607.20092)

**<font color=#1a73e8>作者：</font>** Karan Goyal, Afreen Hossain, Debojyoti Das 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contextual entrainment is the tendency of a model to let auxiliary context in its input pull its output, independently of whether that context is relevant, true, or even meaningful. Recently, it has been identified and given a mechanistic account in unimodal language models. Whether and how it manifests in vision-language models (VLMs) is, by contrast, largely unexamined, and the field lacks a purpose-built instrument with which to investigate it. We take the position that studying contextual entrainment in VLMs requires more than porting an existing text-only benchmark to the multimodal setting: it requires a taxonomically structured, dual-modality instrument whose conditions are constructed around the item at hand (the depicted image in the textual stream, the textual query in the visual stream). We argue that the move to VLMs is substantive rather than incremental. It makes entrainment a dual phenomenon, drivable independently by textual and by visual context, and it opens a veracity distinction (context that is false of the depicted scene yet possible in the world) that has no counterpart in the unimodal, world-knowledge-only formulation of prior work. To make this position concrete and actionable, we introduce ENTRAP-VL (ENTRainment Assessment Probe for Vision and Language), a manually curated dataset of 1,500 items across eight categories, organized by a taxonomy that spans two axes, i.e., the association of context with the item and its relationship to truth, and split into a textual-entrainment stream (eight context conditions) and a visual-entrainment stream (three context conditions). We do not claim to measure entrainment in any particular model; we provide the instrument, the taxonomy that motivates it, and the evaluation protocols it enables, so that the community can investigate the phenomenon rigorously. We will release the dataset and its documentation publicly.

---


### 74. [Understanding the Impact of Linguistic Realization Choices on LLM Stance with Causal Tracing](https://arxiv.org/abs/2607.20115)

**<font color=#1a73e8>作者：</font>** Langchen Huang, Sebastian Padó, Franziska Weeber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are known to be sensitive to prompt and input formulations. However, existing studies have focused on lexical realization and largely ignored constructional choice. This paper studies whether linguistic construction can systematically shift LLM decisions and where these shifts can be causally localized inside the model. We use political stance judgment as a meaning-sensitive case study and extend an English political statements dataset, resulting in six controlled linguistic rewrite types that preserve or invert the meaning of a statement. Experiments on four open-weight models show that stance instability affect both meaning-preserving and meaning-inversing rewrites. Because output shifts reveal that rewrites affect stance, but not where in the model, we apply activation patching, where activations from the original statement are substituted into the forward pass for the rewritten statement and measure which components recover the original stance distribution. The results show that mid-to-late decoder layers, especially block outputs at the final prompt position, provide the strongest restoration signal.

---


### 75. [CUSUM-Shaped Inference-Time Monitoring and Targeted Re-Decoding for Quantized Small Language Model Reasoning](https://arxiv.org/abs/2607.20129)

**<font color=#1a73e8>作者：</font>** El Hassane Ettifouri, Ayoub Belfatmi, Mahaman Sanoussi Yahaya Alassan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantized small autoregressive reasoning models can enter long, repetitive, or unproductive trajectories, yet inference-time compute is usually allocated without observing how a trajectory develops. Building on an earlier token-level e-CUSUM controller, we develop MGT-B (Monitoring-Guided Test-time Backtracking), a revised external controller that maps overlapping windows of pre-sampling uncertainty and degeneration features to position-conditional empirical tail probabilities, accumulates mixture betting factors with a CUSUM-shaped reset, and responds to an alarm by estimating a rollback point, restoring token and key-value-cache state, and performing constrained re-decoding. To audit whether the effect persists on problem identities first observed after the manual choice of log threshold h = 10, we retrospectively exclude 260 IDs present in pre-threshold artifacts and retain the chronologically first post-threshold pair for each remaining ID, yielding a 240-pair chronology-audit set. On this set, accuracy changes from 82/240 to 88/240 (+2.50 percentage points; 13 corrections, 7 regressions; exact McNemar p = 0.2632; paired bootstrap 95% interval [-1.25, +6.25]). A broader 467-pair historical-coverage set of seed-matched pairs changes accuracy from 146/467 to 167/467 (+4.50 points; McNemar p = 0.000753), but includes 200 seed-1 IDs available before or during threshold selection and is reported only as an exploratory estimate. All 316 no-alarm outputs in the 467-pair set are identical to vanilla, while the 151 alarmed trajectories contain 29 corrections and 8 regressions. Neither analysis is confirmatory, and the empirical factors are not established as a valid e-process or e-detector. The results support a selective monitoring-and-repair mechanism for the studied MATH-500 setting, rather than a general or theoretically certified reasoning improvement.

---


### 76. [SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD](https://arxiv.org/abs/2607.20145)

**<font color=#1a73e8>作者：</font>** Dongfang Li, Xiaodong Luo, Ruoyu Sun 等 65 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-parameter post-training of trillion-parameter-scale MoE models introduces substantial system-level challenges for large-scale distributed training, including severe memory pressure, non-overlapped communication overhead, and inefficient kernel execution. While most large-scale LLM training systems are built around GPU-based clusters, this report presents an end-to-end optimization practice on the Ascend NPU SuperPOD. Using the DeepSeek-V4 model family as the target workload, we develop a hierarchical optimization framework spanning model-level parallelism, computation-communication orchestration, and low-level kernel execution. The resulting system achieves 34.22% Model FLOPs Utilization (MFU) with a 2.93x improvement over the open-source baseline recipe while maintaining training stability. Building on this optimized infrastructure, we further establish a CPT and SFT workflow for complex Operations Research (OR) tasks. We refer to the integrated framework as SLAI T-Rex. Using DeepSeek-V4-Flash, we develop OR-oriented CPT and SFT data pipelines that combine collected domain resources with solver-verified synthetic optimization documents. The resulting dataset contains 10K high-quality SFT samples spanning four task categories and three problem representations. The specialized model achieves the highest average zero-shot Pass@1 score among the evaluated models, reaching 71.81% and outperforming GPT-5.4-Mini and the base DeepSeek-V4-Flash model by 3.98 and 11.27 percentage points, respectively. Overall, this work demonstrates a full-stack pathway from efficient trillion-parameter model post-training on Ascend infra to domain-specialized Flash models for solver-grounded mathematical modeling, advancing frontier-model systems for complex reasoning.

---


### 77. [OLEDLM: A Unified Language Model for OLED Molecular Design](https://arxiv.org/abs/2607.20194)

**<font color=#1a73e8>作者：</font>** Fukang Wen, Yuchong Tang, Jingyuan Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The development of organic light-emitting diode (OLED) materials faces the compounded challenges of an astronomically large chemical space, stringent quantum-chemical constraints, and a scarcity of labeled data. Although the question of OLED generation is important, few models have been trained effectively for this specific domain. We propose an inverse molecular design framework based on causal language models: given target optoelectronic properties (e.g., excitation energy, oscillator strength), our model directly generates OLED SMILES sequences satisfying the specified constraints. We employ a multi-stage strategy: first, we establish a foundational chemical language model using a LLaMA-style transformer architecture. To the best of our knowledge, this represents the first successful adaptation of LLMs specifically for the OLED domain, bridging the gap between generic molecular generation and the stringent structural requirements of optoelectronic materials. Second, we fine-tune property predictors based on a BERT model pre-trained on our large-scale OLED dataset. Then, we perform Reinforcement Learning on our fine-tuned model, leveraging our property predictor, for better SMILES generation. Finally, through DFT verification, we demonstrate that our framework can efficiently navigate the OLED chemical space, generating novel candidates with high structural validity and optimized optoelectronic properties.

---


### 78. [HalluTruthQA: A Fine-Grained Benchmark for Hallucination Detection, Localization, and Explanation in Arabic Question Answering](https://arxiv.org/abs/2607.20219)

**<font color=#1a73e8>作者：</font>** Abdessalam Bouchekif, Mohammed-En-Nadhir Zighem, Salah Eddine Bekhouche 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate fluent Arabic answers, yet factual errors remain difficult to detect, localize, explain, and verify. Existing hallucination benchmarks often provide response-level labels, with limited support for identifying the exact erroneous content, explaining why it is incorrect, or selecting the correct factual answer. We introduce \textsc{HalluTruthQA}, a fine-grained benchmark for hallucination evaluation in Arabic question answering. The benchmark contains 2,400 expert-curated examples across four knowledge-intensive domains: Islamic knowledge, history, science, and geography. Each example pairs an Arabic question and a model-generated answer with a verified reference answer, a binary hallucination label, six candidate answers for factual verification, and, for hallucinated answers, character-level erroneous spans, human-written explanations, and macro and micro hallucination types.
We evaluate four open-source LLMs, \textsc{Allam}, \textsc{Falcon-H1}, \textsc{Qwen32}, and \textsc{Silma}, in a zero-shot setting across hallucination detection, span-level localization, factual verification, and explanation evaluation. Results show that these tasks capture different abilities: no single model achieves the strongest performance across all tasks, with best scores of 0.880 Macro-F1 for detection, 0.516 F1-Sp for localization, 0.852 LO-Score for factual verification, and 0.644 final score for explanation evaluation. Our taxonomy shows that hallucination evaluation should move beyond detection toward localizing, verifying, and explaining factual errors. The code, dataset, prompts, and evaluation scripts are available at this https URL.

---


### 79. [Not All Patches are Equal: Sampling Matters for Visible-Infrared Pre-Training](https://arxiv.org/abs/2607.20238)

**<font color=#1a73e8>作者：</font>** Qiwei Ma, Bin Deng, Junjie Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible-infrared (VIS-IR) alignment is a key pre-training task for robust multi-sensor perception. Most existing methods use uniform patch-wise contrastive learning, but this can be unreliable in VIS-IR data because imaging-physics differences make some spatially paired regions inherently less comparable, and aligning them with equal strength hinders representation learning and downstream transfer. In this paper, we revisit VIS-IR pre-training from a sampling perspective and propose Importance-Aware Sampling (IAS), which adjusts training emphasis based on patch reliability. Specifically, IAS (i) derives patch weights from infrared structural cues and uses them to reweight the contrastive objective; (ii) learns a soft importance mask with a lightweight sampler, optionally warm-started from the hand-crafted prior; and (iii) employs a patch curriculum learning strategy that gradually expands from high-reliability regions to harder patches. It is worth noting that IAS is plug-and-play and works with both patch-/correlation-level alignment (e.g., UNIV-style) and image-level contrastive baselines (e.g., ImageBind-style). Extensive experiments on multiple VIS-IR benchmarks demonstrate consistent improvements over strong baselines, including for IR semantic segmentation, IR object detection and VIS semantic segmentation and cross-modal retrieval task. Code will be released on this https URL.

---


### 80. [Exposure is Optional: Learning Unlike Coordination in Language Models](https://arxiv.org/abs/2607.20251)

**<font color=#1a73e8>作者：</font>** Jiamu Luo, Shane Steinert-Threlkeld  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coordination, a fundamental linguistic structure, remains a subject of intense debate, and its exact nature continues to elude theoretical linguistics. A common view holds that only same-category constituents can be conjoined, which has been challenged by the many grammatical unlike coordinations found in natural language. Treating language models as a computational testbed, we investigate whether the acquisition of unlike coordination requires direct exposure in the training data, or whether it can emerge organically from general compositional abilities. Using Filtered-Corpus Training (FiCT), we train GPT-2 models on corpora from which all instances of unlike coordination have been removed. We find that direct exposure is not necessary: models trained on filtered data successfully generalize to unlike coordination, achieving perplexity and grammaticality judgments comparable to models trained on unfiltered text. Furthermore, our analyses of internal representations indicate that language models process unlike coordination by treating the conjoined elements as belonging to similar structural categories or through a mechanism akin to deletion, both of which appear learnable from exposure to alike coordination alone. This work contributes to the growing understanding of how language models internally represent linguistic structures, while also adding to the broader debate on coordination by showing how models generalize and process unlike coordination without direct exposure.

---


### 81. [The Maskability Index: Predicting Task-Objective Alignment in Pretrained Language Models](https://arxiv.org/abs/2607.20265)

**<font color=#1a73e8>作者：</font>** Ahmad Pouramini, Mahsa Afsharzadeh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale pretrained language models such as T5 and BERT have demonstrated strong capabilities for generating structured knowledge. However, their performance depends on how closely the prompting strategy matches the objectives used during pretraining. We introduce the Maskability Index (MI), a quantitative metric that estimates whether a knowledge relation is better suited to masked-style prompting or prefix-style prompting in few-shot generation. MI is computed from differences in DepthRank scores between masked and unmasked templates, providing a principled measure of objective-template alignment. We evaluate MI on a diverse set of relations from the ATOMIC2020 knowledge base completion benchmark and show that it is positively correlated with downstream generation performance. These results indicate that MI can help select appropriate prompting templates and adaptation strategies for extracting relational knowledge from pretrained language models, especially in low-resource settings.

---


### 82. [Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study](https://arxiv.org/abs/2607.20270)

**<font color=#1a73e8>作者：</font>** Andrei Chetvergov, Stepan Ukolov, Timofei Sivoraksha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly evaluated through the values they endorse, but such evaluations presuppose that models can identify the value expressed in a concrete situation. We study this prerequisite as controlled top-1 recognition over Schwartz's ten basic values. Our evaluation set contains 1,000 Russian situational texts, balanced across the ten values and independently labeled by two human annotators per item. We evaluate 21 instruction-tuned LLM runs under a fixed ranked-response protocol; 20 runs with reliable outputs form the semantic panel. Pooled Acc@1 is 0.683 and Acc@3 is 0.892, showing that models often locate the correct motivational region while ranking close alternatives unstably. Adjacent values account for 50.9% of semantic errors, compared with 24.4% under a checkpoint-specific null. Eight directed confusions recur across checkpoints and human-confirmed subsets. Several are strongly asymmetric, including Universalism to Benevolence, Tradition to Conformity, and Security to Power, whereas Stimulation-Hedonism forms a bidirectional boundary. Their severity is checkpoint-specific and can bias higher-order value profiles. The results motivate value-recognition evaluation that combines exact accuracy, ranked recovery, and directed error analysis.

---


### 83. [Self-supervision drives representational convergence in medical foundation models more than clinical supervision](https://arxiv.org/abs/2607.20274)

**<font color=#1a73e8>作者：</font>** Soroosh Tayebi Arasteh, Sebastian Ziegelmayer, Mahshad Lotfinia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image encoders from different groups are increasingly treated as interchangeable, on the assumption that scale and clinical supervision concentrate their representations onto a shared structure. Whether this convergence is real, what produces it, and whether it is clinically usable are untested, and the similarity measures behind such claims are fragile. We present a controlled dissection across 18 image and 7 text encoders, all open-weight and run locally, spanning 7M to 27B parameters and five imaging modalities, including 650,982 chest radiographs from six datasets. To isolate cause, we train encoders that vary only the objective under fixed data, architecture, and scale, and reproduce the effect in a synthetic model. Convergence is modest but above a random floor, driven by the self-supervised objective, not clinical supervision: matched self-supervised encoders aligned most (40.4% on chest radiography), with label-supervised (21.1%) and image-text (3.3%) far lower, and did not grow with size (Spearman 0.302, p=0.223) or capability. It is within-modality, does not reach clinical language, and does not reproduce how radiologists judge case similarity. Yet a linear classifier transfers across encoders and to five held-out hospitals, retaining about 85% of within-encoder performance. Convergence in medical imaging is therefore set by the pretraining objective, not inherited from scale or clinical supervision. Interoperability is accordingly something to design for through that objective, and to validate where the shared geometry is weakest, across patient subgroups and against clinical judgment.

---


### 84. [Multimodal Large Language Models for Remote Sensing Image Understanding: Domain-Specific or General-Purpose?](https://arxiv.org/abs/2607.20284)

**<font color=#1a73e8>作者：</font>** Qiwei Ma, Chunping Qiu, Xinjun Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid development of multimodal large language models (MLLMs) has introduced a flexible paradigm for remote sensing image scene understanding (RSISU), enabling natural-language interaction with remote sensing imagery. However, a systematic understanding of the capability boundaries, cross-task generalization, and task-specific limitations of existing remote sensing MLLMs (RS-MLLMs) is still lacking. This paper presents a systematic survey and diagnostic evaluation of MLLMs for RSISU. We review the technical evolution of RS-MLLMs, focusing on model design, multimodal learning, training data, and downstream capabilities. We further compare RS-MLLMs with general-purpose computer vision MLLMs (CV-MLLMs) across diverse RSISU tasks and benchmarks. RS-MLLMs remain competitive in domain-specific settings, particularly remote sensing visual grounding and high-resolution visual question answering. More notably, general-purpose CV-MLLMs can match or even outperform these specialized models on several RSISU tasks without remote sensing-specific fine-tuning. These findings demonstrate the strong transferability of general-purpose CV-MLLMs and show that current RS-MLLMs do not consistently outperform them across diverse RSISU tasks. Current MLLMs also face limitations in spatial and relational reasoning, fine-grained visual understanding, instruction diversity, and generalization across heterogeneous task formats. Based on these findings, we outline future directions toward reliable evaluation, multimodal and high-resolution reasoning, efficient deployment, and tool-augmented remote sensing agents. This survey provides a systematic reference for developing robust, generalizable, and practical MLLMs for RSISU.

---


### 85. [Sound Probabilistic Safety Bounds for Large Language Models](https://arxiv.org/abs/2607.20286)

**<font color=#1a73e8>作者：</font>** Mahdi Nazeri, Anne-Kathrin Schmuck, Sadegh Soudjani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a novel framework for computing rigorous bounds on the probability that a large language model (LLM) generates harmful output to a given prompt. We study a new application of the Clopper-Pearson confidence intervals to obtain probably approximately correct (PAC) bounds for this problem. As our main technical contribution, we propose an algorithm that leverages features in the latent space to prioritize exploring branches in the auto-regressive generation tree that are more likely to produce harmful outputs. Our approach in particular enables the efficient computation of useful lower bounds, even in scenarios where the true harm probability is extremely small, and crucially, the obtained lower bounds are sound, i.e., formally proven to be less than the actual harmfulness probability: our experimental results demonstrate the effectiveness of our method by computing non-trivial lower bounds on state-of-the-art LLMs. This study newly enables the evaluation and statistical certification of LLMs.

---


### 86. [The Blessing of Dimensionality: How Near-Orthogonality in High-Dimensional Spaces Explains Temporal Portability](https://arxiv.org/abs/2607.20301)

**<font color=#1a73e8>作者：</font>** Abigail Woodring, Adrian Chan, Rana Muhammad Shahroz Khan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning has been widely used to adapt large language models (LLMs) for domain-specific tasks. Parameter efficient fine-tuning (PEFT) methods such as low-rank adaptation (LoRA) are frequently used to reduce computational costs. PortLLM is a training-free and data-free scheme used to adapt LLMs after continual pretraining. Although the initial PortLLM results show that LoRA patches exhibit short-term temporal portability, the long-term performance of PortLLM across several updates of continual pretraining remains underexplored. Furthermore, the intriguing effectiveness of PortLLM is not well understood from a theoretical standpoint. We address these two open questions by (1) performing an extensive empirical study of the long-term temporal portability of PortLLM patches across 10 continual pretraining steps using base models Mistral, Gemma, and Qwen; and (2) offering two theoretical analyses to explain our observation that the simple PortLLM method achieves competitive performance. We find empirically that the portability persists across longer time duration, indicating that repeated fine-tuning is not required when the base model is periodically updated. We find theoretically that near-orthogonality of high-dimensional vectors is a key justification for temporal portability. Our analyses also demonstrate a geometric perspective of the loss landscape in facilitating the theoretical comparison of different adaptation options.

---


### 87. [PyroDash: Cost-Efficient Token-Level Small-Large Language Model Collaborative Inference](https://arxiv.org/abs/2607.20327)

**<font color=#1a73e8>作者：</font>** Niqi Lyu, Pengtao Shi, Wei Qiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) provide strong reasoning capabilities but are expensive to serve at scale, whereas small language models (SLMs) are cheaper but less reliable on difficult problems. We introduce PyroDash, a cost-aware framework for token-level SLM-LLM collaborative inference. During generation, the SLM decides whether to request assistance by emitting a control token. A Collaborate Engine then sends the query and partial reasoning trace to a frozen LLM for completion through a single handoff. The policy is internalized in the SLM, requiring neither a separate router, LLM retraining, nor access to LLM logits. PyroDash trains the SLM in three stages: control-token embedding learning, offloading-oriented supervised fine-tuning, and cost-aware alignment with Group Relative Policy Optimization. Its reward balances answer accuracy against inference cost normalized by LLM-only inference. Across five mathematical reasoning benchmarks, PyroDash supports different accuracy-cost operating points. With $\lambda=0.05$, it achieves 64.04 percent average accuracy, 6.36 percentage points above the LLM-only baseline, while reducing cost by 20.4 percent. With $\lambda=0.6$, it achieves 54.55 percent accuracy with a 1.90 percent LLM token ratio and 0.012 LLM calls per example, reducing total cost from USD 49.36 to USD 1.78. These results show that learned token-level handoffs can reduce LLM use while preserving strong reasoning performance.

---


### 88. [Test-Time Training for Modality Order Consistency in Vision-Language Models](https://arxiv.org/abs/2607.20351)

**<font color=#1a73e8>作者：</font>** Aditi Gupta, Yossi Gandelsman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We find that vision-language models are sensitive to a specific semantically irrelevant change: the order in which the image and question are presented. Across three models and three benchmarks, image first prompting consistently outperforms question-first prompting, revealing a repeatable modality order failure. We use this gap to design an order-consistent test-time training method. Our method substantially closes the modality-order gap across all evaluated settings. Surprisingly, it also yields consistent improvements in the stronger image-first branch over the baseline, hence bootstrapping both orderings toward mutual consistency. Activation patching localizes the ordering failure to a narrow mid-network region where representations diverge sharply between prompt orders. We find that the test-time training method repairs this misalignment across layers. Together, our results identify modality-order sensitivity as a circuit-level failure in VLMs and demonstrate that simple, asymmetric test-time adaptation can effectively mitigate it and even improve performance over the baseline.

---


### 89. [Look Less, Think Faster: Joint Token-Compute Adaptation for Multimodal LLMs](https://arxiv.org/abs/2607.20357)

**<font color=#1a73e8>作者：</font>** Pengcheng Wang, Zhiquan Wang, Jayoung Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have recently demonstrated strong performance across vision-language tasks. However, their high inference cost, arising from both the large number of input visual tokens and the heavy computation of the large language model (LLM), remains a key barrier to practical deployment. Recent work attempts to reduce the cost by adaptively optimizing individual dimensions, e.g., pruning redundant visual tokens or skipping LLM layers and heads. Nonetheless, prior approaches typically treat these dimensions independently and overlook a fundamental coupling: the available compute resources must be dynamically allocated across all dimensions based on the input content. To bridge the gap, we propose SmartVL, a unified adaptive inference framework that jointly controls vision token number and model compute capability in response to varying input contents and compute budgets. SmartVL introduces a vision-side token controller that dynamically selects informative visual tokens and an LLM-side compute controller that adaptively adjusts LLM computation. Importantly, these controllers are trained to coordinate with each other so that the overall inference cost satisfies a target budget. To allow this joint scheduling, we connect the controllers using a shared budget encoding and leverage a differentiable latency estimator for end-to-end training. This design enables SmartVL to learn cross-stage allocation strategies that adapt to both input complexity and runtime compute constraints. Experiments across multiple MLLM benchmarks demonstrate that, with joint scheduling, SmartVL consistently outperforms prior adaptive methods and achieves superior accuracy-efficiency Pareto frontiers. Project page: this https URL.

---


### 90. [Notes to Self: Can LLMs Benefit from Experiential Abstractions?](https://arxiv.org/abs/2607.20372)

**<font color=#1a73e8>作者：</font>** Chang Liu, Xinyu Li, Artur Dubrawski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans distill experience into reusable abstractions, e.g., strategies and cautionary reminders, and apply them to gradually solve problems more effectively. We study whether Large Language Models (LLMs) can similarly benefit from such experiential abstractions. From LLMs' solution traces on the MATH training set, a stronger teacher or the LLMs themselves extract natural-language abstractions into a retrievable library. We explore two usage modes: (1) inference-time retrieval and (2) reinforcement learning (RL) with abstraction-augmented training prompts. Experiential abstractions improve LLM performance on mathematical and logical reasoning benchmarks. Self-extracted abstractions match teacher-extracted ones, and our abstraction usage framework can transfer to other datasets and models. These findings suggest LLMs can extract and apply experiential abstractions much as humans leverage distilled experience.

---


### 91. [PercepCap: Video Captioner with Structured Spatio-Temporal Perception](https://arxiv.org/abs/2607.20389)

**<font color=#1a73e8>作者：</font>** Yifan Xu, Zihao Wang, Zhixiao Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video captioning requires fine-grained spatio-temporal understanding of videos, including spatial perception of where objects are located and temporal perception of when events occur. Existing MLLMs usually generate captions directly from video inputs without exposing the perceptual evidence behind descriptions. As a result, mistakes in spatiotemporal perception are only observed in the final caption, making it difficult to identify the underlying perceptual errors directly. To address these issues, we present PercepCap, a perception-aware video captioning framework that makes perceptual evidence explicit before producing the final caption. Specifically, PercepCap follows a perceive-describe generation chain, where the model first produces a spatiotemporal perception trace comprising object trajectories and temporal events, and then generates the final caption conditioned on the perceived evidence. To support this, we design a two-stage training strategy. Perceive-then-Describe Supervised Fine-tuning adapts the model from caption-only generation to the proposed perceive-describe chain, while Perception-Grounded Reinforcement Learning optimizes perception trace and caption quality with joint rewards over perception chain and the final caption. To support our two-stage training, we introduce Caption-Anchored Perception Data Construction. This pipeline builds the SFT and RL training data by first generating a caption-only description, extracting the objects and events it mentions, and grounding them back in the video with boxes and timestamps. This yields caption-aligned perception data that provides solid training ground truth, ensuring that the explicit perception trace and final caption refer to the same objects and events. Across direct caption and caption-to-QA evaluation, PercepCap consistently improves upon the Qwen3-VL baseline and demonstrates leading caption quality.

---


### 92. [LKValues: Aligning Large Language Models with Sri Lankan Societal Values](https://arxiv.org/abs/2607.20410)

**<font color=#1a73e8>作者：</font>** Nethmi Muthugala, Supryadi, Surangika Ranathunga 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Value alignment of Large Language Models (LLMs) has been shown to be culturally biased toward Western norms. This results in the mishandling of local values in multilingual societies such as Sri Lanka that have their unique cultural dynamics. Existing benchmarks overlook Sri Lankan-contextualized values in its official language Sinhala, hindering culturally sensitive evaluation and fine-tuning. To bridge this gap, we propose LKValues, the first survey-grounded resource suite for Sri Lankan value alignment. From a trilingual survey of 205 respondents, blending adapted global frameworks and LLM-elicited local constructs, we derive 40 majority-endorsed societal values. Using these values, we construct LKvaluesIT, a Sinhala-English news-derived instruction corpus containing 150k scenario-based instances, and LKvaluesBench, a value-sensitive evaluation benchmark of 1,000 instances. We evaluate a set of proprietary and open-weight LLMs with LKvaluesBench. We fine-tune three open-weight base models (Qwen3.5-4B-Base, Qwen3.5-9B-Base, and Aya-Expanse-8B-Base). Our experiments show that newer and larger LLMs still exhibit low-resource and cultural value-alignment gaps. LKValues fine-tuning improves Qwen-family models in English and Sinhala, reducing invalid outputs and cross-lingual disparities, though gains remain model-family dependent. These highlight LKValues efficacy in embedding Sri Lankan values, offering a replicable pipeline for low-resource, country-specific pluralist value alignment. The dataset is publicly available at this https URL.

---


> [!TIP]
> 当前位于：**51-92**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-92**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
