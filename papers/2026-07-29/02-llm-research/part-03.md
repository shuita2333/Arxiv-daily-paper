# 🧠 大模型相关研究 | 2026年07月29日

> 本类共 **240** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-240](./part-05.md)

---

### 101. [Compiler-Grounded Hierarchical Diagnosis for LLM-Based Triton Kernel Optimization](https://arxiv.org/abs/2607.23089)

**<font color=#1a73e8>作者：</font>** Dongjie Chen, Ping Zhao, Bohua Zhan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have enabled automated kernel generation and optimization, but most existing approaches rely on surface signals such as compilation feedback and profiling metrics. These signals reveal that a kernel is slow, but not why the backend compiler fails to realize a profitable optimization, especially on emerging accelerators such as NPUs. We therefore formulate kernel optimization as a progressive cross-layer diagnosis problem that links runtime symptoms to IR structure and compiler behavior before rewriting source. Based on this insight, we present our system, a compiler-grounded and hierarchical optimization framework for Triton kernels. the system escalates from lightweight pattern triage and profiling diagnosis to IR attribution and compiler-grounded analysis only when deeper evidence is needed, then proposes evidence-backed source-level rewrites.
We implement the system on Triton for Ascend NPUs and evaluate it on 37 successfully converted entries from a standardized NPUKernelBench-derived Ascend 950 benchmark. Across these entries, the system attains a geometric-mean speedup of 4.35$\times$ and a median speedup of 2.73$\times$ from the initial to optimized Triton kernel; 22/37 exceed 2$\times$ and 13/37 exceed 5$\times$. The complete distribution ranges from near-baseline entries to large wins, motivating transparent reporting of the current system's scope and limitations.

---


### 102. [AgentOmnia: Scaling Agentic Models for Full-Scenario Applications](https://arxiv.org/abs/2607.23124)

**<font color=#1a73e8>作者：</font>** Hao Jiang, Gangtao Xin, Yingdi Huang 等 38 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents have advanced rapidly, yet progress remains fragmented across domains, capabilities, task difficulty, and interaction settings. We frame this as full-scenario agentic scaling and present AgentOmnia, a framework coordinating task-space definition, data synthesis, post-training, evaluation, and improvement across To-Consumer (ToC), To-Business (ToB), and To-Employee (ToE) applications. An extensible Domain x Capability x Atomic Difficulty taxonomy aligns these stages and enables fine-grained diagnosis with OmniaBench. AgentOmnia combines bidirectional environment-task synthesis with tool-dependency, program-structured, and solver-based pipelines, constructing 5,018 stateful environments with 255,375 tools and 52,361 tasks. Programs, solvers, and verifiers provide correctness signals, while supervised fine-tuning, online agentic reinforcement learning, and a rollback curriculum support post-training. Evaluation failures translate into Product Requirement Documents (PRDs) for targeted self-evolution. Starting from Qwen3-30B-A3B-Thinking-2507, AgentOmnia raises the pass rate on the OmniaBench challenging subset from 9.16% to 37.11% and the macro-average across OmniaBench, $\tau^2$-Bench, DeepPlanning, and VitaBench from 22.86% to 41.69%. Under a unified protocol,it leads the evaluated agentic post-trained baselines on OmniaBench and retains the highest four-benchmark macro-average. It also surpasses Qwen3-235B-A22B-Thinking-2507 on all four benchmarks and exceeds Qwen3.5-35B-A3B on the macro-average. Gains span three application splits, ten capability dimensions, eight atomic-difficulty factors, and 76 of 90 level-1 domains, indicating broad rather than category-specific improvement. A one-round study provides initial evidence for PRD-guided self-evolution, motivating validation at larger scales and in industrial settings.

---


### 103. [Self-Boosting Vision-Language Models with Noisy Student On-Policy Self-Distillation](https://arxiv.org/abs/2607.23125)

**<font color=#1a73e8>作者：</font>** Shuai Wang, Daoan Zhang, Zhe Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training enables vision-language models (VLMs) to understand human instructions and perform various downstream tasks. Current post-training methods usually rely on human-annotated data, distillation from external models, reinforcement learning with human feedback, or verifiable answers. This limits their ability to improve without external supervision. To tackle this, we propose NOPD (Noisy Student On-Policy Self-Distillation), a simple yet effective self-distillation approach that improves VLMs without any external models or ground-truth answers. Our key insight is that prediction discrepancies between clean and corrupted inputs naturally induce a self-supervision signal. In NOPD, the model learns from corrupted inputs while using its own predictions under clean inputs as token-level supervision. We show the effectiveness of NOPD on five visual reasoning tasks; it can match and even outperform reinforcement learning approaches or distillation from external models. Notably, when trained with 2.1K samples from Geometry3K, NOPD improves Qwen2.5-VL-7B by 20 points on its validation set. It also shows generalization on out-of-distribution test sets and achieves 7.4 point gains on MathVista. Furthermore, we demonstrate that NOPD is a general approach to enhance VLMs, achieving improvements across three models on 12 benchmarks.

---


### 104. [DispatchRAG: Grounding Emergency Dispatch Decisions in Real-World Protocols from Traffic Accident Video](https://arxiv.org/abs/2607.23132)

**<font color=#1a73e8>作者：</font>** Muhammad Sulthan Adhipradhana, Ehsan Javanmardi, Naren Bao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assessing the severity of a traffic accident scenario is important to decide which emergency service to dispatch. Missing an ambulance dispatch on a pedestrian accident is a fatal issue that can lead to death. Recently, Vision-Language Models (VLMs) have been a promising tool for accident reasoning, yet many VLMs are not grounded in real-life accident response protocols, making them not usable in accident severity assessment off-the-shelf. We introduced DispatchRAG, an accident assessor and dispatcher framework grounded in real-life Japanese traffic-accident response protocols, designed to enhance VLMs to generate an appropriate emergency response during an emergency scenario. Utilizing a RAG-based retrieval mechanism to retrieve the most relevant accident protocol and an LLM-powered reasoner to suggest the most proper response. To support evaluation, we introduce Accident Dispatch Dataset, a comprehensive dataset of accident assessment and emergency response according to Japanese accident response protocols adapted from the MM-AU dataset. We validate our framework on the Accident Dispatch Dataset, showing strong performance across various accident scenarios compared to the baseline VLM, pointing toward integration in autonomous vehicles that can automatically report both their own and nearby accidents.

---


### 105. [Foundation Models and Fine-Tuning: Toward a New Generation of Models for Time Series Forecasting](https://arxiv.org/abs/2607.23146)

**<font color=#1a73e8>作者：</font>** Morad Laglil, Bertrand Pracca, Emilie Devijver 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inspired by recent breakthroughs in large language models for natural language processing, foundation models have emerged as a promising paradigm for zero-shot time series forecasting, enabling accurate predictions on datasets never seen during pre-training. Ranging from tens to hundreds of millions of parameters, these models are pre-trained on vast and diverse collections of time series, learning generalizable representations that support both point and probabilistic forecasting. This approach alleviates the need for dataset-specific model design and manual tuning, offering a unified solution across forecasting problems. In this work, we review the main architectures, pre-training strategies, and optimization methods underpinning these models. We further investigate post-pre-training fine-tuning of selected foundation models to enhance their performance on specific datasets. Our empirical results demonstrate that this step consistently improves forecasting accuracy over the zero-shot baseline.

---


### 106. [In-Context Learning as Implicit Policy Gradient](https://arxiv.org/abs/2607.23153)

**<font color=#1a73e8>作者：</font>** Masahiro Kaneko, Timothy Baldwin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that large language models (LLMs) can iteratively improve their outputs by incorporating generated samples and their corresponding evaluation scores as in-context examples. Despite these empirical findings, the theoretical foundations underlying this phenomenon remain poorly understood. In this paper, we show that score-conditioned In-Context Learning (ICL) admits a structural correspondence to policy gradient optimization. We first provide a constructive proof that self-attention mechanisms can implement reward-weighted aggregation analogous to the REINFORCE algorithm under specific weight matrix configurations, and discuss the relationship between this construction and the behavior of pretrained transformers. The correspondence is directional in hidden-state space and holds exactly only under the stated simplifying conditions; we quantify its strength empirically. Within our simplified hidden-state model, we furthermore derive an exact upper bound on the distribution shift induced by a bounded attention update, yielding a trust-region-like analogy to KL-constrained policy optimization. We validate our theory through extensive experiments across multiple LLMs, demonstrating that LLMs effectively utilize score information to shift output distributions toward high-scoring exemplars, and that attention weights exhibit a strong correlation with example scores.

---


### 107. [Beyond a Global Norm: Personalizing Toxicity Sensitivity in Language Models Without Retraining](https://arxiv.org/abs/2607.23175)

**<font color=#1a73e8>作者：</font>** Rares A.C. Diaconescu, Iulia Slanina, Alina Florea 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reducing toxicity is often framed as a global alignment problem, yet perceptions of harmful language are subjective and context-dependent. We present the first comparative evaluation of training-free methods for aligning language generation to user-specific toxicity sensitivities across three inference-time intervention stages: pre-decoding (prompt conditioning and rewriting), in-decoding (token, logit, and representation steering), and post-decoding (candidate re-ranking). Evaluated against toxicity sensitivity targets derived from the PRISM dataset, all methods reduce alignment error by 28-47%. However, the results reveal a fundamental trade-off between alignment effectiveness, personalization, and general language quality, showing how toxicity sensitivity alignment is an inherently multi-objective problem.

---


### 108. [OmniScope: Modality-Decoupled Token Compression for Omnimodal Large Language Models](https://arxiv.org/abs/2607.23193)

**<font color=#1a73e8>作者：</font>** Jinsen Su, Yongdong Luo, Yuexiao Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing token compression methods for omnimodal large language models typically rely on one modality to determine what to retain in the other. We show that this assumption often breaks down: for the same query, audio and video relevance often peaks at different moments. This cross-modal salience mismatch makes unidirectional guidance prone to discarding answer-critical cues under aggressive compression. We propose OmniScope, a training-free token compression framework that uses the query as a shared semantic anchor while estimating relevance separately for audio and video. OmniScope allocates modality-specific token budgets, prunes visual tokens with an anchor-delta strategy that preserves both global context and temporal changes, and merges audio tokens within each second to reduce redundancy while maintaining temporal continuity. Across four audio-video benchmarks and two Qwen2.5-Omni model scales, OmniScope achieves the best average accuracy across all compression settings. At 25% overall token retention, it delivers up to 3.53x prefill speedup and more than 15% GPU memory reduction, with only a 0.35-point drop in average accuracy. These results suggest a simple design principle for OmniLLM inference: share the query across modalities, but not the salience estimates. The code is available at this https URL.

---


### 109. [Domain-Prior-Regularized Graph Modeling for Anomaly Detection in Cyber-Physical Systems](https://arxiv.org/abs/2607.23197)

**<font color=#1a73e8>作者：</font>** Youngseok Hwang, Joonsung Kwon, Geonwoo Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection on multivariate sensor time series is critical for industrial monitoring of cyber-physical systems (CPS), where even subtle deviations from normal behavior can indicate process disruption. Recent graph-based approaches have made significant progress, but they often struggle in small-scale physical systems with scarce labeled anomalies and limited normal data. In such settings, graph-based models tend to capture spurious correlations and produce unstable sensor topologies. We propose DPR-GM (Domain-Prior-Regularized Graph Modeling), a forecasting-based framework that incorporates system design knowledge into graph construction. DPR-GM leverages a large language model (LLM) to extract directed physical couplings between sensor pairs from system documentation, which are encoded as a binary domain adjacency matrix serving as a structural gate over sensor relations. This gate is then modulated by Pearson correlations estimated from normal training data. The anomaly score is further weighted by sensor-level reliability derived from the coefficient of variation. All graph and weighting components are fixed prior to training and add no learnable parameters. On the SKAB benchmark, DPR-GM outperforms graph-based, statistical, and deep learning baselines across F1, AUROC, and AUPRC, showing that domain-structured graph priors are a practical alternative to fully learned topologies in data-scarce CPS.

---


### 110. [Beyond Conversations: Spatially-Anchored Previews for Intent Disambiguation in LLM-Assisted Geometry Editing in Virtual Reality](https://arxiv.org/abs/2607.23201)

**<font color=#1a73e8>作者：</font>** Junlong Chen, Amr Gomaa, Jens Grubert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> User intent disambiguation remains a key challenge in intelligent interactive systems. While they have been widely studied in dialogue systems in 2D interfaces, research on how intent disambiguation could be incorporated within Large Language Model (LLM) assisted editing workflows in immersive environments remains limited. Recent advances in LLMs create opportunities to leverage the immersive nature of virtual and augmented reality (VR/AR) environments to provide better disambiguation support. In this paper, we evaluate how traditional dialogue-based disambiguation can be augmented with spatially-anchored graphical previews to resolve ambiguous user commands in LLM-assisted parameter-driven editing workflows. A within-subjects study in which 24 participants completed complex geometry editing tasks in VR simulate scenarios where VR scenes are controlled by numerical parameters. Compared with the condition where disambiguation is not available, quantitative metrics and qualitative feedback indicate that a hybrid approach which combines clarification questions and graphical previews can support better interaction stability with fewer conversation rounds while improving user experience. These findings provide empirical evidence on the effectiveness of disambiguation methods in LLM-assisted editing of parameter-driven immersive scenes and inform design guidelines for future integration of LLMs in advanced VR/AR systems.

---


### 111. [A Taxonomy of Confabulations and the Perception-Reality Gap in LLM-Assisted Immersive Scene Editing](https://arxiv.org/abs/2607.23213)

**<font color=#1a73e8>作者：</font>** Junlong Chen, Per Ola Kristensson  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are being increasingly integrated into immersive environments and design workflows, providing application prospects in areas such as rapid scene prototyping for non-expert users and scene understanding capabilities for accessibility design. While many workflows that incorporate LLMs in immersive spaces are proposed, such systems can exhibit errors, potentially resulting in frustration, loss of user trust, and compromised user safety. This paper studies the underexplored area of LLM confabulations in immersive 3D scene editing contexts. Through an exploratory study with 24 non-expert users, we construct a taxonomy of the different types of confabulation observed in LLM-assisted immersive 3D scene editing. We report their prevalence and disruptiveness, and define the construct perception-reality gap to help understand the gap between the actual and perceived occurrence of confabulations. We highlight the observed saturation of confabulation awareness under load and conclude by discussing design implications for confabulation mitigation in future LLM-assisted systems in immersive 3D scenes.

---


### 112. [SARATR-X-v2: Scale-Aware Structural Pre-Training for SAR Foundation Models](https://arxiv.org/abs/2607.23238)

**<font color=#1a73e8>作者：</font>** Weijie Li, Yafei Song, Yongxiang Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Masked image modeling has become a dominant paradigm for SAR pre-training, yet the design of the reconstruction target remains fundamentally unsettled. This article argues that a SAR pre-training target should satisfy two conditions to produce transferable representations: (i) physics-grounded stability, i.e., approximate invariance of the target operator to multiplicative speckle inherent in coherent imaging; and (ii) semantic scale compatibility, i.e., coverage of the heterogeneous spatial scales that downstream tasks demand. These two conditions are individually achievable but jointly difficult: physics-grounded stability favors fixed operators, while semantic scale compatibility favors data-driven composition. To this end, SARATR-X-v2 reconciles both within a single design. The target is constructed through fixed structural extractors spanning six receptive fields, from blind-spot local aggregation to directional log-ratio region contrast, and fused via learnable weights into one unified supervision signal for masked reconstruction. On twelve SAR benchmarks across classification, detection, and segmentation, SARATR-X-v2 achieves state-of-the-art transfer performance. Under synthetic speckle variation, the proposed target reduces perturbation drift in the learned representation by nearly two orders of magnitude relative to pixel-space supervision. Taken together, these results establish physics-grounded stability and semantic scale compatibility as a principled framework for pre-training target design under coherent imaging, and suggest that effective SAR pre-training is not about reconstructing more signal, but about reconstructing the right structural target.

---


### 113. [WaveZip: Wavelet-Driven Space-Time Decoupling for Video Token Condensation](https://arxiv.org/abs/2607.23265)

**<font color=#1a73e8>作者：</font>** Yuhui Zeng, Wang Chen, Jinfa Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Large Vision-Language Models (LVLMs) struggle with long-form video understanding due to the quadratic computational cost of visual tokens. While recent efficient methods attempt to compress tokens via hard pruning or uniform merging, they operate strictly in the spatial feature domain, where robust structural context and discriminative semantic details are inherently entangled. In this work, we propose WaveZip, a joint signal-frequency-domain framework for efficient video inference. Driven by the insight that temporal redundancy resides in low-pass approximation scales while spatial saliency strongly correlates with high-frequency components, WaveZip leverages Discrete Wavelet Transforms (DWT) to disentangle these signals. Temporally, it employs 1D DWT to analyze query-frame relevance, and the resulting high-frequency coefficients are further gated by inter-frame differences, with both signals jointly driving the dynamic allocation of a precise frame-level token budget. Spatially, a 2D DWT decomposes features into low-frequency approximations and high-frequency detail components, where the high-frequency coefficients are modulated within query-salient regions to regulate spatial reconstruction. Importantly, WaveZip requires no task-specific training and can be seamlessly integrated into off-the-shelf LVLMs to boost inference efficiency. Extensive experiments on long video understanding benchmarks demonstrate that WaveZip retains 99.6% of the full performance under an extreme 10x compression ratio, consistently outperforming state-of-the-art methods.

---


### 114. [What CLIP Knows but Cannot Say: Recovering Negation from Frozen Intermediate Features](https://arxiv.org/abs/2607.23271)

**<font color=#1a73e8>作者：</font>** Chen-Yi Lu, Yueh-Shao Chen, Somali Chaterji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive vision-language models such as CLIP map semantically opposite phrases (e.g., "a dog" vs. "not a dog") to nearly identical embeddings, rendering them insensitive to negation. We attribute this failure to a phenomenon we call Representational Collapse: by tracking compositional divergence and visual alignment across the CLIP text encoder, we show that middle layers build compositional syntax, but the final layers collapse this structure as visual alignment rises, producing a syntax-blind final representation. To recover the lost negation signal without altering pretrained weights, we propose PeakPatch, a lightweight post-hoc correction system that intercepts the encoder at its compositional peak. An Embedding Correction Network (ECN) uses cross-attention to extract a negation-specific signal from the peak layer, anchored to a stable baseline, and predicts a deviation vector that re-injects the lost syntax into the final-layer embedding space. A complementary Score Correction Network (SCN) predicts bounded scalar score offsets for discriminative tasks. Both modules are trained jointly end-to-end while all CLIP parameters remain frozen, adding only 5.2M parameters (3.5% of the backbone) and preserving the standard cosine similarity interface. On NegBench, PeakPatch achieves 74.3% on COCO MCQ (+35.1 over CLIP, +17.8 over the best encoder fine-tuning method) and 65.5% on VOC MCQ, while outperforming all fine-tuning baselines on fully out-of-distribution negation retrieval despite training only 3.5% of the parameters. The corrected embeddings also transfer to text-to-image generation (+18.4 negation score) and generalize across ViT-B/32, ViT-L/14, and SigLIP backbones. Project URL: this https URL.

---


### 115. [TopoFE: topology-aware LLM-guided Automated Feature Engineering](https://arxiv.org/abs/2607.23286)

**<font color=#1a73e8>作者：</font>** Sha Li, Naren Ramakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic feature engineering (AutoFE) for tabular learning can be naturally formulated as a program synthesis problem, where the objective is to discover predictive feature transformations from an exponentially large search space. Recent advances in large language models (LLMs) have expanded the expressiveness of AutoFE by enabling feature program generation beyond predefined operator libraries. However, existing LLM-based approaches remain fundamentally limited by stateless generation and homogeneous search: feature proposals are produced from static prompts without accumulating search experience, while single-population exploration quickly converges to dominant transformation patterns and rarely discovers complementary feature compositions across transformation families. We propose TOPOFE, a topology-aware multi-island evolutionary framework for LLM-guided feature engineering. TOPOFE combines family-specialized exploration, adaptive prompt memory, and topology-guided knowledge transfer to efficiently discover diverse and compositional feature programs. Experiments on 29 public tabular datasets demonstrate consistent improvements over state-of-the-art AutoFE methods across classification and regression tasks. Beyond predictive performance, TOPOFE discovers more diverse and transferable feature programs that generalize across multiple downstream predictors and LLM backbones.

---


### 116. [RareLens: Towards End-to-End Rare Disease Care via Aligning Divergent Large Language Model Reasoning](https://arxiv.org/abs/2607.23290)

**<font color=#1a73e8>作者：</font>** Xi Chen, Hongru Zhou, Shiyu Feng 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rare diseases collectively affect an estimated 3.5% to 5.9% of the population, yet more than 70% of patients are misdiagnosed and many endure years of evaluation before a diagnosis is reached, because early presentations are nonspecific and relevant expertise is scarce and unevenly distributed. Artificial intelligence could provide support, but existing systems address isolated stages of care, overwhelmingly diagnosis. They typically depend on the results of downstream investigations, and they treat the variability between models as noise to be eliminated. Here we present RareLens, a system that supports clinical decision-making across the entire rare disease trajectory by exploiting this variability. When heterogeneous large language models evaluate the same case, they generate divergent but complementary reasoning, which RareLens aligns and calibrates into a single convergent, actionable decision at each stage. Four coordinated modules perform primary-visit risk screening, diagnosis, treatment planning and prognosis. Developed and evaluated on RareBench, a real-world dataset of 157,525 cases spanning all 33 Orphanet categories and more than 7,000 conditions, RareLens outperformed every frontier model tested, including GPT-5, DeepSeek-R1, Claude-3.7-Sonnet and Gemini-2.5-Pro, at each stage. It achieved an area under the curve of 0.917 for screening and top-1 accuracies of 65.5% and 89.8% for diagnosis and treatment. In an external study spanning 1,287 cases and 23 physicians, autonomous RareLens and physicians assisted by RareLens both substantially outperformed unaided physicians. These findings indicate that aligning divergent model reasoning, rather than scaling a single model, offers a generalizable strategy for high-uncertainty clinical decision-making.

---


### 117. [IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems](https://arxiv.org/abs/2607.23322)

**<font color=#1a73e8>作者：</font>** Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction tuning has become the standard method for adapting large language models to follow human intent, yet existing instruction datasets are dominated by English-language general-knowledge tasks and lack coverage of specialized pedagogical domains. This paper presents IKS-Instruct, a dataset of 24,795 instruction-response pairs for teaching language models to deliver educational content grounded in Indian Knowledge Systems (IKS). The dataset spans seven languages (English, Hindi, Sanskrit, Tamil, Telugu, Kannada, and Malayalam), covers 41 pedagogical techniques from the Vedic oral and mathematical traditions, and is aligned with the Central Board of Secondary Education (CBSE) curriculum for classes 6 through 12. The pairs are derived from six source types: classical text corpora (Bhagavad Gita, Thirukkural, Sangam literature, Vedic texts), curriculum-aligned pedagogical templates, Vedic mathematical sutra demonstrations, bilingual instruction pairs, technique-grounded multi-turn dialogues, and cross-tradition comparative analyses. Quality is assessed through a multi-judge evaluation framework in which independent language models score responses on 12 dimensions including technique fidelity, pedagogical quality, factual accuracy, and IKS cultural depth. Under a uniform five-judge external panel (median aggregation over 1,201 stratified items), the strongest IKS-Instruct fine-tune of a compact 7B model reaches a median judge score of 6.39, within 0.15 of a strong general-purpose reference model (Nemotron-Nano at 6.54) at a fraction of its deployment cost, while the base model without IKS fine-tuning scores near zero on the IKS-specific dimensions. Model quality does not increase monotonically with data curation, a result we report together with the corresponding data-quality gains.

---


### 118. [ESF-Bench: Benchmarking Challenging Slot-Filling Scenarios for Real-World Enterprise Applications](https://arxiv.org/abs/2607.23326)

**<font color=#1a73e8>作者：</font>** Toby Liang, Gopal Sarda, Sagar Davasam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid rise of large language models (LLMs) has driven transformative adoption across enterprises. However, deploying these models in real-world settings presents unique challenges due to complex system constraints and unexpected user behaviors. Among these applications, slot filling is essential for converting unstructured input into structured, actionable data. In this work, we introduce ESF-Bench, a challenging Enterprise Slot Filling benchmark consisting of 810 multi-turn samples and 6530 slots over 8 unique domains. Curated using a taxonomy of the 57 most challenging slot-filling scenarios observed during real-world enterprise deployments, ESF-Bench exposes notable limitations in current state-of-the-art LLMs, with GPT-OSS-120b low successfully extracting slots for only 20.7% of benchmark samples. To support continued research in this area, we publicly release the benchmark dataset, taxonomy, and accompanying evaluation code on GitHub.

---


### 119. [AlloBench: Measuring Online Tool Allocation Capability in LLM Agents](https://arxiv.org/abs/2607.23332)

**<font color=#1a73e8>作者：</font>** Daniel Wang, Andrew Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Creating a reusable tool is an investment: an agent pays a fixed cost now in exchange for the potential of future reuse. Therefore, a user should prefer an agent that creates a small number of highly reusable tools, rather than many one-offs. We introduce a paired benchmark that tests whether LLM agents exhibit conscious allocation behavior under a fixed budget in two contexts: an abstract text-based formulation and a code-construction task. We find that every frontier model we test---Claude Haiku, Claude Opus, GPT-5.4-mini, and GPT-5.6 Sol---acts near-optimally in the abstract framing but fails to transfer this ability to script-writing. Through further experiments, we identify the particular failure modes for each model. Notably, the first three models fail even when the scripts are not evaluated, while GPT-5.6 Sol stays selective under that weaker manipulation and collapses only at full construction. Furthermore, an open-source Qwen model policy-trained for abstract allocation generalizes this ability across held-out lexical variations, but sees no improvement at script allocation. Together, these results establish online tool allocation as a significant capability boundary, even for modern frontier models.

---


### 120. [The Gate Always Closes: On Injecting Auxiliary Signals into Frozen Vision-Language Models](https://arxiv.org/abs/2607.23335)

**<font color=#1a73e8>作者：</font>** Moshiur Farazi, Sameera Ramasinghe, Bekir Sait Ciftler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Auxiliary signal pathways in VLMs are routinely fitted with learnable gates so the optimiser can decide how much of the signal to admit. We find that the optimiser almost always decides on zero: across five injection designs, every gated pathway becomes behaviourally closed, with accuracy invariant to ablating the pathway at inference even when the gate parameter would nominally pass 30-45% of the signal. We attribute this suppression phenomenon to two regimes, a dead-gradient regime formalised through the caption-invariance of image-derived signals, and a negative-utility regime in which the auxiliary signal actively hurts the loss. Rather than fight suppression, we exploit it: we regularise LoRA fine-tuning with geometric auxiliary losses from hyperbolic visual relational graphs (IoA-driven entailment cones and angular repulsion on the Lorentz manifold), coupled only through the forward pass at training time and dropped at inference. Disaggregating GQA by question type exposes a clean dissociation. Three configurations without geometric losses at inference lose 2.85-3.39pp on relational questions while gaining ~1pp on attribute questions; a fourth that trains with the losses but infers through a soft prompt loses 5.14pp on rel for only +0.23pp on attr, so training-time regularisation alone does not protect relational accuracy without a geometric inference pathway. Configurations that keep the geometric pathway at inference preserve vanilla-level relational accuracy and match the attribute gain. Out of distribution on VSR, the RMS-prefix recipe preserves the spatial signal; stripping the geometric losses (G2) collapses VSR by 4.6pp, isolating them as the OOD source. A secondary result: embedding-norm alignment is necessary for generation-safe prefix injection, and learnable gates should be replaced with fixed, non-optional injection at matched scales.

---


### 121. [BERT-based Models vs. Large Language Models for Low-Resource Named Entity Recognition: A Comparative Study on Marathi](https://arxiv.org/abs/2607.23344)

**<font color=#1a73e8>作者：</font>** Hariom Ingle, Ronit Ghode, Ishwari Gondkar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Named Entity Recognition (NER) for low-resource languages such as Marathi remains a challenging task due to limited annotated resources and linguistic complexity. Although recent Large Language Models (LLMs) have demonstrated strong performance across a wide range of natural language processing tasks, their effectiveness for language-specific NER in low-resource settings remains uncertain. In this study, we fine-tune MahaBERT-v2 on different variants of the MahaNER dataset and systematically compare the performance of these models with an existing MahaNER baseline and prominent general-purpose LLMs, including Gemini, LLaMA-3.3-70B, and Gemma models. All models are evaluated on a Marathi NER test dataset using standard metrics of precision, recall, and F1-score. The experimental results show that the fine-tuned MahaBERT-based models consistently outperform both the baseline and all evaluated LLMs, with the fine-tuned models achieving F1-scores ranging from 0.88 to 0.91, surpassing the existing MahaNER model (0.8843) and significantly exceeding the performance of LLM-based approaches, whose F1-scores range from 0.57 to 0.69. These findings demonstrate that task-specific, language-focused models trained on domain-relevant data remain more effective than general-purpose LLMs for Marathi NER, highlighting the continued importance of specialized architectures for low-resource language processing.

---


### 122. [UltraViT: Latency-Optimized On-device Vision Encoder for Large Vision-Language Models](https://arxiv.org/abs/2607.23373)

**<font color=#1a73e8>作者：</font>** Ioannis Maniadis Metaxas, Adrian Bulat, Alberto Baldrati 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) remain bottlenecked by massive computational footprints, precluding their deployment on resource-constrained edge devices. While efforts to compress LVLMs focus heavily on vision token reduction or smaller language models, the vision encoder is largely overlooked, typically deployed as a monolithic, computationally heavy feature extractor. Moreover, there is no previous effort that designs a vision encoder for LVLMs directly optimized for on-device latency. In this paper, we present UltraViT, a vision encoder for LVLMs, explicitly designed and optimized for on-device performance. Specifically, by taking into account real on-device latencies, we systematically design a pyramidal architecture that strategically integrates and adapts heterogeneous spatial mixers at the macro-block level. Furthermore, to pre-train UltraViT, we propose a novel two-stage generative pre-training strategy: cultivating rich spatial features via dense distillation, followed by direct generative supervision from a capacity-mixed frozen LLM. Compared to standard contrastive and SSL, we show that our pre-training is much more effective for achieving high-level semantic grounding for UltraViT needed for the subsequent generative multimodal alignment of LVLM training. Extensive experiments demonstrate that our on-device latency-informed design combined with our tailored training strategy establishes a new state-of-the-art for efficient LVLM encoding, significantly outperforming existing encoder-centric baselines while operating on-device at nearly 1.7xthe speed.

---


### 123. [Confidently Wrong: Exception Chain Collapse in Frontier LLM Rule Evaluation](https://arxiv.org/abs/2607.23386)

**<font color=#1a73e8>作者：</font>** Paul Simpson, John Kozak, Lisa Doake  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We document a failure class in frontier large language models -- exception chain collapse -- observed in eligibility evaluation under nested conditional rules of the form "A is required UNLESS B applies, UNLESS C overrides B". The failure reproduces at first observation, but its empirical surface is unstable: between March and April 2026 several failure cells closed silently under the same model alias, with no version bump (GPT-5.4 on construction insurance moved from 96.6% to 100%, same prompt and harness). For regulated workflows, frontier-model accuracy is a moving compliance boundary that shifts without notice. We present the Aethis Eligibility Module, a neuro-symbolic architecture in which LLMs author rules from authoritative sources and an SMT-based layer executes them deterministically, consistent with the authored specification regardless of model drift, reasoning-effort defaults, or prompt format. Three evidence bases: (i) a controlled benchmark of 225 scenarios across four regulatory domains documents the pattern and, in replication, the drift that partially closed it; (ii) a 20-scenario adversarial extension on construction insurance, where the engine scores 20/20, as does one of four frontier configurations (GPT-5.4 at low reasoning effort), while the other three, including Anthropic's strongest model at evaluation time, fail the same coverage-gap edge case; (iii) external validation on nine peer-reviewed LegalBench tasks, 949 held-out cases, where the engine is significantly more accurate than all three frontier models (combined McNemar's p <= 0.003), with margins up to +41 points on the curated multi-prong tasks against the Anthropic models. The contribution is to relocate uncertainty from the inference boundary, where it is silent, to the specification boundary, where it is deliberate and audited. All scenarios, rule encodings, and results are public and reproducible.

---


### 124. [Inference-Time Consensus for Mitigating Hidden Behaviors from LLM Fine-Tuning](https://arxiv.org/abs/2607.23394)

**<font color=#1a73e8>作者：</font>** Adhyyan Narang, Artin Tajdini, Claire Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work shows that fine-tuning language models on even a small amount of poisoned data can install targeted misbehavior, and ostensibly benign data can transmit hidden preferences that generalize broadly. Standard defenses, such as data filtering, mixing in harmless data, and regularization, attenuate these effects but do not eliminate them. We instead pursue robustness through redundancy: collecting multiple datasets from different sources and only learning what is common between them. Thus, if only a subset of sources are malicious, the misbehavior will be blocked. In order to implement this defense strategy, we fine-tune a separate reference model on each source's dataset and aggregate their next-token distributions at decoding time. We introduce two consensus decoders: a token-wise minimum, which caps each token at the lowest probability any source assigns, and a base-relative variant, which reverts to the base probability on any token the sources move in opposing directions. We further relax exact agreement to tolerate partial support across sources and different surface expressions of the same intention. Across controlled poisoning tasks, subliminal learning, and emergent misalignment, consensus decoding suppresses source-specific misbehavior while preserving shared desirable behavior, including cases where union training and weight averaging retain the unwanted behavior.

---


### 125. [LA-RL: Label-Aware Self-Reflection for Reinforcement Learning in Information Extraction](https://arxiv.org/abs/2607.23420)

**<font color=#1a73e8>作者：</font>** Xiao You, Tianwei Yan, Zixu Shan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models show strong promise for information extraction (IE), but existing reflection-based correction methods are often misaligned with structured extraction outputs. Free-form self-reflection can flag an error, yet it rarely identifies whether the failure is a missing span, wrong label, boundary mismatch, invalid relation type, or reversed argument order. We introduce LA-RL (Label-Aware Reflective Reinforcement Learning), an outcome-supervised framework that guides IE self-correction with task-grounded diagnostic labels. A single backbone first predicts an extraction, diagnoses task-specific error labels, and then revises its output conditioned on the diagnosis. Training starts from diagnostic data labeled by an annotation model for cold-start supervised fine-tuning and proceeds through two GRPO stages that reward final extraction quality, format validity, and first-pass correctness, without a process reward model. Experiments on named entity recognition, relation extraction, and event extraction show consistent same-backbone gains over SFT, including 6.83 average F1 on SciER relation extraction, about 20 F1 on out-of-distribution relation extraction, and 14.80 trigger F1 plus 17.50 argument F1 on DuEE1.0. Ablations show that reflection structure is task-sensitive: stronger constraints benefit relation extraction, whereas named entity recognition needs less restrictive correction under domain shift.

---


### 126. [Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels](https://arxiv.org/abs/2607.23438)

**<font color=#1a73e8>作者：</font>** Haining Zheng, Qian Dong, Rodolfo K. Depena 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems increasingly exhibit agentic behavior, discussions of autonomy often conflate what systems are technically capable of doing with what they should be permitted to do in practice. This paper introduces a governance framework that explicitly separates Allowed Autonomy Levels (AAL), which define the degree of autonomy an AI agent is authorized to exercise given risk, oversight, and accountability considerations, from Autonomous Capability Levels (ACL), which characterize an agent's inherent technical abilities. We present a structured set of autonomy levels spanning reactive execution, decision support, supervised action, goal-directed autonomy, and delegated operational authority, and describe how control, reversibility, and accountability change as autonomy increases. To operationalize this framework, we propose a risk-aware decision process for assigning allowed autonomy, analyze how risk and accountability evolve across autonomy levels, and demonstrate its application through a deployed enterprise data engineering agent, illustrating how a system assessed at a high capability level can be deliberately constrained to a lower allowed autonomy based on risk, reversibility, and organizational readiness. By distinguishing authorization from capability, this work provides practical guidance for the design, deployment, and governance of Agentic AI systems.

---


### 127. [Reasoning or Memorization: Can LLMs Understand and Generate Chinese Xiehouyu Riddles?](https://arxiv.org/abs/2607.23440)

**<font color=#1a73e8>作者：</font>** Hai Hu, Siyuan Song, Chongtian Shao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we push the boundary of LLM reasoning by testing them in a Chinese language game, xiehouyu, with novel xiehouyu created by linguists that had not existed before to avoid data contamination. We use multiple-choice questions (MCQ), free-form explanation generation, and new xiehouyu creation to evaluate LLMs' ability to understand and create xiehouyu. In MCQ, we use the delta of accuracy ($\Delta_{acc}$) between existing but low-frequency xiehouyu and novel ones as an index for memorization. $\Delta_{acc}$ for native speakers is very low, suggesting similar processing mechanisms. However, we found that frontier Chinese models have on average a $\Delta_{acc}$ of 23.6\%, while English-centric models tested have a mean $\Delta_{acc}$ of 5.1\%, suggesting that frontier Chinese models are likely trained with much larger Chinese data, thus memorizing more low-frequency xiehouyu. For novel xiehouyu, Gemini 3.1 Pro demonstrated remarkable ability with acc 92.6, which is 24\% higher than human accuracy. In xiehouyu creation, those created by LLMs receive much worse ratings than those by humans. These results suggest that claims about the reasoning abilities of LLMs may need careful re-examination considering the data contamination issue, and that LLMs' creativity in language-related tasks may still be behind human experts, at least in Chinese xiehouyu.

---


### 128. [Do LLM Debates Repeat Arguments Differently Across Languages?](https://arxiv.org/abs/2607.23442)

**<font color=#1a73e8>作者：</font>** Huiqian Lai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM debate is usually evaluated by final answers, but transcripts also reveal whether later turns develop new argumentative content or return to earlier claims in new wording. We study this process with \textit{prior-argument similarity}, an aggregate diagnostic comparing extracted argument units with earlier units in the same debate. In controlled eight-turn debates over 71 motions, six languages, and four model agents, Chinese is the only tested language with a consistently positive gap relative to English across three multilingual embedding models. The gap persists across agents, turn positions, regression adjustment, metric variants, extraction-length controls, a second-extractor subset, and cross-encoder tail rescoring. Manual calibration shows weak item-level alignment but a high-similarity tail enriched for substantive repetition. A diversity-aware prompt lowers prior-argument similarity across languages, yet does not significantly narrow the Chinese--English gap. These findings suggest that multilingual debate evaluation should measure argumentative development over time and report mitigation effects in both average and gap terms.

---


### 129. [Omni-Prune: Query-Aware Unified Token Pruning for Efficient Omnimodal Large Language Models](https://arxiv.org/abs/2607.23445)

**<font color=#1a73e8>作者：</font>** Yiming Zhong, Chang Nie, Caifeng Shan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnimodal large language models (OmniLLMs) are rapidly extending multimodal reasoning to cover synchronized audio and video. However, the resulting audio-video token sequences are long, leading to high prefill latency and GPU memory usage at inference time. Existing token pruning methods, designed mainly for vision-only inputs, miss both the cross-modal links between audio and video and the user query that decides which content matters. To bridge this gap, we present Omni-Prune, a training-free, query-aware audio-visual token pruning framework that jointly removes redundancy from both modalities while keeping task-relevant cross-modal evidence. Specifically, Omni-Prune first splits the token sequence into adaptive time windows placed at audio saliency peaks, then scores audio and video tokens on a single scale that combines encoder attention with text-query relevance, and pairs related audio-video tokens so that they are kept together. Within each window, a final K-medoids step then selects a few representative tokens, adding diverse cues that score-based selection alone would miss. Extensive experiments demonstrate that Omni-Prune outperforms established baseline methods, delivering up to 3.25x prefill speedup and 1.3x memory reduction while retaining over 99% of full-model performance.

---


### 130. [Do Small Models Use the Law You Give Them? Context-Injected Fine-Tuning for Legal QA in Bangladesh](https://arxiv.org/abs/2607.23446)

**<font color=#1a73e8>作者：</font>** Moniruzzaman Mahadi, Abrar Mohammed Tanzim Alam, Sayma Siddika Monalisa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A small language model can receive the governing statutory provision and still answer incorrectly. We test whether fine-tuning on examples containing relevant law improves later use of retrieved law. We curate 2{,}165 bilingual QA records from six Bangladeshi acts and three schedules, then fine-tune Qwen3.5 at 0.8B, 2B, and 4B. Evaluation uses the 2022 and 2023 Bangladesh Bar Council exams in Bangla and machine-translated English, with no retrieval, BM25, or FAISS, scored by strict consistency over three seeded runs. At 0.8B, fine-tuning raises the 2022 English FAISS score from 2 to 34 of 100. Gains at 0.8B and 2B survive paired testing, but the 4B model has no detectable net gain: Bangla improves while several English conditions regress. Fine-tuning also reduces answers that drift from Bangla into mostly English from 44.0--53.2\% to 0.2--0.7\%, with adjusted $p<.001$ at every scale. Retrieval quality is therefore not the only bottleneck. Small bilingual legal models also differ in how they use supplied law and whether they answer in the requested language. The dataset is publicly available at this https URL.

---


### 131. [VIPER: Visual In-Context Physics Reasoning for Physically Plausible Video Generation](https://arxiv.org/abs/2607.23472)

**<font color=#1a73e8>作者：</font>** Tianxiao Chen, Hanmo Chen, Huajin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video generation models can synthesize visually compelling and temporally coherent clips, yet controlling their physical behavior remains difficult with standard text and image conditions. The core challenge is a conditioning bottleneck: material response, contact interaction, deformation, and motion trajectory are continuous and relational physical cues that are hard to specify exhaustively in language but can be demonstrated naturally by video. We propose VIPER, a Visual In-Context Physics Reasoning framework for reference-guided image-to-video generation. Given a target image, a brief target prompt, and a reference video, VIPER treats the reference as a dense visual demonstration of the desired physical process rather than an appearance template. It uses a Multimodal Large Language Model (MLLM) to extract reference-derived physical cues and guide a pretrained image-to-video generator through a hierarchical training strategy, enabling physical behavior transfer while preserving the visual prior of the base generator. To support this setting, we construct VIPER-19K, a curated dataset with material, trajectory, and physical-impact annotations, together with filtered reference-target pairs. Experiments on an unseen validation set show that VIPER achieves stronger reference-video physical similarity and higher human preference than representative video generation and video-as-prompt baselines, while maintaining competitive general video quality. Qualitative results further demonstrate that VIPER can transfer reference-derived physical behavior to new target scenes without requiring carefully engineered prompts.

---


### 132. [Mwando: Leveraging AI to Preserve and Teach shiKomori](https://arxiv.org/abs/2607.23481)

**<font color=#1a73e8>作者：</font>** Naira Abdou Mohamed, Haidar Nassur Said Ali, Mohamed Hazra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents Mwando, a virtual educational assistant designed to support the teaching and preservation of shiKomori, the language of the Comoros Islands. The system covers the four main dialectal variants (shiNgazidja, shiMwali, shiNdzuani and shiMaore) through a knowledge base constructed from phrases, proverbs, dictionaries and grammar lessons. A multi-agent architecture combining vector search, a knowledge graph and web search fallback enables accurate and context-aware responses. Evaluation on 500 queries demonstrates strong performance on vocabulary lookup and grammar explanations, while qualitative case studies illustrate both capabilities and current limitations. This work represents an initial step toward computational support for shiKomori and provides a blueprint for developing AI-powered educational tools for other low-resource languages.

---


### 133. [Multimodal Data Comprehension: Understanding How Visual-Textual Chains of Information Influence Data Interpretation](https://arxiv.org/abs/2607.23489)

**<font color=#1a73e8>作者：</font>** Arran Zeyu Wang, Fuling Sun, Danielle Albers Szafir  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visualizations and text often work together to support effective data communication. Despite this common paradigm, we know little about how the interplay of these modalities affects people's data comprehension. We present a novel experimental paradigm to investigate multimodal data comprehension---the process of people comprehending information from multimodal visual and textual data---across both crowdsourced and think-aloud environments. Our methodology employs two sequential chains for presenting multimodal information---a visualization-first chain and a text-first chain---asking people to describe the data presented iteratively. By comparing how people's data comprehension changes across the chain, we can assess the information contribution of each modality and how they shape subsequent comprehension. We found that the visualization-first chain facilitates exploratory comprehension with hypothesis-driven discovery, whereas the text-first chain yields confirmatory comprehension akin to framing effects where visualizations serve to reinforce and confirm observations drawn from text. Our findings provide empirical insights into multimodal information integration, with implications for designing more effective data-driven communication.

---


### 134. [Token-Region Guided Cross-Attention Fusion for Multimodal Affect Interpretation](https://arxiv.org/abs/2607.23493)

**<font color=#1a73e8>作者：</font>** Musa Tur Farazi, Nufayer Jahan Reza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated analysis of multimodal content on social networks has become a critical task for understanding public sentiment and information diffusion in the digital age. However, classifying internet memes remains computationally challenging due to the intricate interplay between visual cues and embedded, often stylized, text, particularly in low-resource languages like Bengali Language. This paper addresses the detection of political intent in Bengali memes by introducing Multimodal Cross-Attention Fusion framework. We first leverage a Vision-Language Model to extract high-fidelity OCR text from noisy meme images. Subsequently, we encode visual and textual features and synthesize them through a cross-modal multi-head attention mechanism that aligns semantic tokens with visual regions. We also investigate the integration of a domain-specific political lexicon as a knowledge prior. Experimental evaluation on the PoliMemeDecode1 dataset shows that our attention-based fusion significantly outperforms unimodal baselines and standard concatenation methods, achieving a state-of-the-art Macro-F1 of approximately 0.94. Interpretability analyzes further confirm that the model effectively learns to ground textual semantics in visual evidence.

---


### 135. [Do LLMs Know Their Vulnerable Scenarios?](https://arxiv.org/abs/2607.23496)

**<font color=#1a73e8>作者：</font>** Ziheng Peng, Huiqi Deng, Haoran Jing 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety-aligned large language models are trained to refuse harmful requests, yet embedding the same requests in particular scenarios can bypass their safeguards. Existing red-teaming methods empirically identify effective scenarios through observed attack outcomes, but why particular scenarios weaken refusal remains mechanistically unclear. Meanwhile, mechanistic interpretability studies have characterized both refusal directions and jailbreak-associated features, without explaining the relationship between the two representations. In this work, we show that scenario-wrapped prompts activate internal scenario directions whose causal steering consistently reduces refusal scores. Building on this finding, we propose \textsc{Concept2Scenario}, a concept-based attribution framework for vulnerable scenario discovery. It instantiates a broad concept space with a sparse autoencoder, attributes refusal suppression to individual concepts, translates the identified concepts into interpretable natural-language scenarios, and identifies synergistic scenario combinations through interaction attribution. Across three open-source models, two safety benchmarks, and six black-box jailbreak methods, the discovered scenarios serve as reusable priors that improve average attack success rates by up to $18.2$ percentage points. They also transfer to GPT-5, Claude-Haiku-4.5, and Gemini-3-Flash, suggesting that some scenario-level refusal vulnerabilities are shared across model families. Moreover, the identified combinations outperform their individual constituents and enable iterative attacks to succeed in fewer turns.

---


### 136. [MemVLN: Episodic and Procedural Memory for Vision-and-Language Navigation](https://arxiv.org/abs/2607.23504)

**<font color=#1a73e8>作者：</font>** Yuqi Liu, Shengju Qian, Tianyuan Qu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires agents to maintain long-horizon visual history for trajectory consistency while executing actions with low latency. Existing video-based VLN approaches typically struggle to satisfy both demands simultaneously. To address these challenges, we propose MemVLN, a novel VLN framework that achieves state-of-the-art performance with real-time inference efficiency (14 FPS). MemVLN utilizes a visual encoder to process continuous observations and a Large Language Model (LLM) to interpret instructions and generate actions. Central to our approach is an Episodic Memory management that applies pyramidal resolutions. This mechanism concentrates computation on immediate percepts while retaining compressed long-term history. Complementing to this design, we introduce Procedural Memory for fast action with a compact vocabulary of atomic mid-level actions to bypass auto-regressive decoding latency. Experiments on VLN-CE show that MemVLN-4B surpasses the baseline Qwen3-VL-4B architecture by 5.8\% SR in R2R and 9.7\% SR in RxR, while achieving a 7$\times$ speedup in inference latency.

---


### 137. [Do Diagrams Help Large Language Models Reason? Evidence from Syllogistic Reasoning](https://arxiv.org/abs/2607.23513)

**<font color=#1a73e8>作者：</font>** Risako Ando, Koji Mineshima  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diagrams are widely used to support logical reasoning, and prior studies suggest that representations such as Euler diagrams can improve human reasoning performance. Recent work has also explored their effects on large language models (LLMs). In this paper, we compare four representational conditions for syllogistic reasoning: natural language, logical notation, linear diagrams, and Euler diagrams. Using 285 problems from Ando et al. (2024), we evaluate two contemporary LLMs, Claude 3.5~Sonnet and GPT-4o-mini. Our results show that diagrammatic representations do not consistently improve performance. Although the models perform well on entailment and contradiction problems, they struggle with neutral problems and often make systematic conversion errors. Overall, the results suggest that the tested models gain limited benefit from diagrams in logical reasoning tasks.

---


### 138. [Novel Claim or Déjà Vu? Rethinking "Contamination-Free'' Dynamic Evaluation for Multimodal Automated Fact-Checking](https://arxiv.org/abs/2607.23514)

**<font color=#1a73e8>作者：</font>** Haorui He, Xinwen Chen, Dacheng Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal automated fact-checking (MAFC) verifies claims by retrieving and reasoning over external evidence. However, most existing static benchmarks risk contamination: they primarily consist of outdated claims verifiable using an LLM's internal knowledge without external evidence. This can inflate performance estimates and fail to reflect true capability on novel claims that require up-to-date information. To address this, emerging dynamic benchmarks collect claims published after LLMs' knowledge cut-off dates, assuming they are uncontaminated. This work revisits this assumption by empirically studying contamination risks in both the state-of-the-art (SOTA) static AVeriTeC benchmark and our newly constructed dynamic ClaimReview2025Q4 benchmark, as well as their impact on MAFC evaluation. Our experiments yield 16 findings, highlighting three key results: (1) Dynamic evaluation reduces but does not eliminate contamination risks, as 17.09\%--29.30\% of post-cut-off claims remain potentially contaminated; (2) Many newly published claims can be verified either directly or by synthesizing multiple pieces of public knowledge available before the cut-off; and (3) Contamination can induce statistically significant inflation in MAFC performance, increasing Macro-F1 by up to 11.34 points and distorting system rankings. In light of these findings, we re-evaluate SOTA LLMs under a strictly contamination-controlled setting. Our study provides practical guidelines for trustworthy MAFC evaluation.

---


### 139. [Real-Time Human-Centric World Modeling for Upper-Body Human-Object Interaction](https://arxiv.org/abs/2607.23517)

**<font color=#1a73e8>作者：</font>** Chaonan Ji, Jinwei Qi, Peng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a real-time human-centric world model for upper-body interactive generation, aiming to synthesize coherent local world dynamics centered on a person, where coordinated body, hand, and facial motions evolve jointly with controllable human-object discrete interaction. To this end, we adopt a continuous-discrete joint control scheme with two complementary components: a continuous human state and a discrete interaction state. For continuous human-state control, we introduce a unified implicit representation based on multi-scale motion encoding, in which motion latents from the upper body, hands, and face are fused into a shared latent space. This multi-scale design improves expressiveness across different spatial scales, captures fine-grained human dynamics more effectively, and enables direct control without explicit retargeting. For discrete object interaction-state control, we represent object contact using a small set of language-encoded discrete interaction states, where text serves as an explicit interaction-state command, such as \emph{no contact} or \emph{grasp}, rather than an open-ended generation prompt, and we further construct a dedicated rendering pipeline for human-object interaction data to supervise such discrete interaction states. By combining continuous implicit human-state control with discrete interaction-state control, our model enables precise modeling of how a person moves and interacts with the local environment, including controllable changes to nearby scene states. Finally, we distill the model for efficient streaming real-time inference, achieving 25 FPS on two H100 GPUs. Experiments demonstrate improved fine-grained motion fidelity, more realistic hand-object coordination, and effective real-time interaction, establishing a practical step beyond motion reproduction toward real-time human-centric world modeling.

---


### 140. [ObsDriveBench: Benchmarking Multimodal Understanding under Adverse Weather with Observability Awareness](https://arxiv.org/abs/2607.23537)

**<font color=#1a73e8>作者：</font>** Qiao Yan, Yihan Wang, Zhenghao Xing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous driving under adverse weather remains a critical challenge, yet existing vision-language benchmarks mainly evaluate under standard conditions, synthetic corruptions, or single modality. As a result, it remains unclear how vision-language models behave under real-world adverse weather with multi-modal inputs. We argue that a key difficulty lies in degraded environmental observability: under fog, rain, snow, and low illumination, multi-modal observations become unreliable and cross-modally inconsistent, posing challenges to scene understanding, and subsequent decision-making. To study this, we introduce \textbf{ObsDriveBench}, a real-world multi-modal benchmark for adverse-weather autonomous driving. Our benchmark is designed with three capability dimensions: \textbf{observability awareness}, \textbf{spatial reliability}, and \textbf{risk-aware decision-making}, enabling fine-grained diagnosis of model behavior under degraded observations. We construct the benchmark through observability meta-annotation, scene description, and capability oriented multiple-choice tasks over synchronized camera, LiDAR, and radar inputs, forming a benchmark with over 14k training and 13k test questions. Experiments reveal consistent performance degradation of existing vision-language models. We further introduce \textbf{ObsDrive} model with normal-weather supervised fine-tuning and adverse-weather reinforcement learning, improving robustness across all three capabilities. The dataset and evaluation code will be released at \href{this https URL}{\texttt{ObsDriveBench}}.

---


### 141. [Guiding Language Models to Be More Empathetic: Culturally Sensitive Mental Health Advice Generation Through Human-LLM Collaboration](https://arxiv.org/abs/2607.23538)

**<font color=#1a73e8>作者：</font>** Fatema Tuj Johora Faria, Mukaffi Bin Moin, Md. Mahfuzur Rahman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in large language models (LLMs), their ability to generate empathetic mental health counseling responses in low-resource languages remains largely unexplored. To address this gap, we curate 625 authentic mental health cases from three complementary sources: (1) publicly available Facebook posts discussing mental health concerns, (2) transcripts from the Bangladeshi television program "Ami Akhon Ki Korbo", and (3) anonymized student questionnaire responses covering diverse emotional and psychological challenges. Based on these cases, we build an evaluation corpus comprising advice written by licensed clinical psychologists and responses generated by three modern proprietary LLMs: GPT-4o Mini, Claude 4.5 Haiku, and Gemini 2.5 Pro. We further propose the Role-Playing Reflective Chain-of-Thought Advisory Framework (RP-RCAF), a task-specific prompting strategy that combines expert-authored few-shot examples with structured self-reflection to produce supportive, culturally aware, and ethically aligned counseling through a compassionate advisor persona. We also introduce the Grok 4-Based Response Evaluation and Scoring Framework (G-REFS), which integrates automated assessment with expert psychologist validation across emotional sensitivity, cultural appropriateness, linguistic clarity, and ethical soundness. Experimental results show that RP-RCAF consistently outperforms conventional prompting across all evaluated models and produces responses that more closely align with professional psychological counseling.

---


### 142. [GaitFace: A Multimodal Dataset for Long-Range Person Identification](https://arxiv.org/abs/2607.23542)

**<font color=#1a73e8>作者：</font>** Alain Komaty, Luis S. Luevano, Vidit Vidit 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient border control is becoming a significant global challenge, mainly due to severe congestion and extended passenger waiting times. To mitigate these bottlenecks and facilitate passenger flow, biometric technologies are increasingly deployed to streamline identity verification and enhance crossing efficiency. Technical limitations frequently impede biometric identification, particularly in long-range surveillance, where systems must deal with adverse atmospheric conditions and degraded image quality. While high-quality frameworks like BRIAR exist, they are frequently restricted to specific government agencies. This paper introduces GaitFace, a new public dataset that contains face and gait data captured at long distances. To ensure that the research reflects authentic border scenarios, we use Pre-Enrollment data, where a traveler registers via a mobile device, and "In-the-Wild" captures, which records individuals at a distance across multiple viewing angles and different cameras. Benchmarking SOTA face and gait models reveals that current architectures fail under low-resolution and elevated viewpoints despite success with optical assistance. GaitFace exposes these critical vulnerabilities, providing a rigorous public benchmark to drive more robust, unconstrained biometric research.

---


### 143. [Language Shapes Instruction Hierarchy Compliance in Multilingual LLMs](https://arxiv.org/abs/2607.23545)

**<font color=#1a73e8>作者：</font>** Jiwon Moon, Yerin Hwang, Kyomin Jung  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction hierarchy (IH) requires models to prioritize instructions by source, ensuring that higher-priority instructions override lower-priority ones. Despite its importance for safe and controllable deployment, existing evaluations have focused almost exclusively on English, leaving it unclear whether IH compliance remains stable in multilingual settings. We introduce XIH-Bench, a benchmark for multilingual IH evaluation with both same-language and cross-language conflicts across six languages, four domains, and three IH settings. Across models, we find two consistent patterns. First, IH compliance exhibits a clear language-dependent asymmetry: a language that strengthens compliance in the higher-priority position can become disruptive in the lower-priority position. Second, cross-language conflicts yield higher compliance than same-language conflicts, a phenomenon we term the Language Boundary Effect. We further show that language specialization can make lower-priority instructions in model-favored languages harder to override, creating multilingual reliability and security risks.

---


### 144. [Verification-Notebook Learning for Source-Aware Multimodal Misinformation Detection](https://arxiv.org/abs/2607.23581)

**<font color=#1a73e8>作者：</font>** Junyuan Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal misinformation verification is challenging because misleading signals may come from different parts of a post and require different forms of evidence. LVLMs are well suited to this task, but their verification performance often depends on the inference procedure applied to each instance. Existing methods improve this procedure through stronger prompting, retrieval, or deliberation, but rarely retain the verification patterns learned from previous examples. We propose Verification-Notebook Learning (VNL), a non-parametric framework that learns an external verification procedure for a frozen LVLM before inference. VNL builds a compact notebook of decision principles, evidence cues, and recurring pitfalls from prior verification experience. The notebook remains fixed during inference and guides the verification of new examples. Rather than updating model parameters or storing demonstrations, VNL records learned knowledge in an artifact that can be inspected directly. Experiments show that VNL consistently outperforms a range of competitive baselines. Further analyses show that the Verification Notebook improves fine-grained source attribution while remaining compact and interpretable, providing an effective way to accumulate verification knowledge without model training.

---


### 145. [JarvisHub: An Open Harness for Canvas-Native Multimodal Creative Agents](https://arxiv.org/abs/2607.23588)

**<font color=#1a73e8>作者：</font>** Yunlong Lin, Zixu Lin, Zhaohu Xing 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creative AI is moving from single-step asset generation toward long-horizon multimodal production. Although recent generative models can synthesize high-quality images, videos, audio clips, UI elements, storyboards, slides, and other creative assets, real-world creative work requires more than isolated prompt-output interactions. It involves references, drafts, alternatives, edits, failed attempts, version relations, tool actions, evaluation signals, and human feedback, which together form an evolving project state. Existing prompt-based, chat-based, and node-based generation systems only partially support this state, as they often discard intermediate context, rely on linear conversations, or require manually specified workflows. Recent commercial systems indicate a shift toward agent-assisted creative production, but their closed architectures make it difficult to study how agents represent context, choose tools, revise artifacts, recover from failures, and maintain consistency over time. To address this gap, we introduce JarvisHub, a canvas-native creative agent harness for long-horizon multimodal creation. JarvisHub treats an editable canvas as the user workspace, the agent's external memory, action space, and shared project state, representing multimodal artifacts, dependencies, versions, and feedback as typed canvas nodes and links. Through a three-layer architecture of canvas state, protocol bridge, and agent runtime, JarvisHub enables agents to act within an inspectable and editable creative state. This design moves creative agents beyond isolated tool use toward sustained, human-steerable creative automation, where agents can progressively plan, generate, revise, and organize multimodal projects while users remain able to inspect, guide, and intervene throughout the process.

---


### 146. [ConFusion: Continuous Fusion Space Learning for Fine-Grained Controllable Infrared and Visible Image Fusion](https://arxiv.org/abs/2607.23600)

**<font color=#1a73e8>作者：</font>** Guo Yurong, He Yufei, Li Yonghao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable infrared-visible image fusion aims to integrate complementary thermal and structural information with flexible region-aware modulation, producing fused images that adapt to diverse user requirements and downstream tasks. However, existing methods typically rely on predefined discrete control conditions, leading to a sparse space that fails to support fine-grained modulation demands. To address this, we propose ConFusion, a novel framework that learns the continuous fusion space via Gaussian-conditioned spatial-aware modulation, enabling instance-level fine-grained controllable infrared and visible image fusion. ConFusion employs a dual-branch architecture to disentangle modality-invariant and modality-specific representations under joint reconstruction and text-guided semantic alignment. Gaussian-conditioned instance modulation variables coupled with Grounded SAM-based instance masks guide instance-level fine-grained modulation through the Mask-Guided Specific Feature Modulator, while the Text-Driven Invariant Feature Enhancer improves semantic consistency and enhances fusion. During inference, the multimodal large language model parses user intents into instance-level modulation variables to guide image fusion. Extensive experiments show that ConFusion achieves state-of-the-art performance across multiple metrics in both fusion quality and downstream tasks, while supporting fine-grained controllable image fusion. Our code is available at this https URL

---


### 147. [Hybrid Advantage Estimation with Unified Critic for VLM Agentic Reinforcement Learning](https://arxiv.org/abs/2607.23605)

**<font color=#1a73e8>作者：</font>** Wenxuan Zhang, Yuhui Wang, Donggang Jia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (VLMs) now act as agents in interactive environments, where success requires coherent reasoning and decision-making across turns. Although end-to-end training in agentic environments can improve such multi-turn decision-making abilities, current methods mainly rely on either token-wise optimization over concatenated token trajectories or turn-wise optimization with uniform within-turn credit. In this work, we establish theoretical formulations for the two levels of optimization and derive a hybrid advantage that serves both objectives. Furthermore, with an appropriate choice of discount factor and learning target, we prove that a unified critic model can estimate values for both turn-wise and token-wise. As such, we propose HyGAE, an actor-critic framework that jointly optimizes token- and turn-level objectives with the hybrid advantage and unified critic. We conduct extensive evaluations of HyGAE across five multi-turn decision-making environments, where it achieves an average success rate of 91% and a significant improvement of 10% over other methods. Furthermore, we provide an in-depth analysis showing that the exact analytic form of the hybrid advantage and return is crucial for optimization. Project Page: this https URL.

---


### 148. [MS-GPT: Rethinking MS/MS De Novo Structure Elucidation as Spectrum-Induced Posterior Querying of a Molecule-Language Model](https://arxiv.org/abs/2607.23607)

**<font color=#1a73e8>作者：</font>** Xin Zhao, Yumin Liu, Zhuo Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular structure elucidation from tandem mass spectra (MS/MS) is a central inverse problem in analytical chemistry. Most existing approaches to MS/MS identification remain tied to reference libraries or predefined candidate sets, whereas de novo methods aim to generate structures directly from spectra. A common de novo route predicts a molecular fingerprint from the spectrum and then decodes structures from it, enabling decoder pretraining on large molecule-only corpora. However, this paradigm creates a training-inference mismatch: the decoder is trained on oracle fingerprints computed from molecules, but at inference it is queried with a noisy spectrum-induced fingerprint posterior that is typically collapsed to a single thresholded fingerprint. We introduce MS-GPT, which recasts fingerprint-mediated de novo elucidation as spectrum-induced posterior querying of a conditional molecule-language model. MS-GPT conditions a molecule-language model on fingerprints and formulas, then converts the spectrum-induced posterior into a band of fingerprint queries near the oracle-fingerprint manifold through active-bit density calibration. Candidates sampled across this band are pooled and ranked by generation-frequency consensus. A lightweight LoRA adapter further mitigates domain-specific posterior bias while preserving the pretrained molecular prior. On NPLIB1 and MassSpecGym, MS-GPT sets a new state of the art, reaching Top-1/Top-10 exact-match accuracy of 29.8\%/41.1\% and 23.9\%/28.7\%, respectively. Candidate-pool scaling shows that efficient autoregressive molecular generation continues to improve recall with a little additional inference cost. The source code and model checkpoints are available at this https URL.

---


### 149. [PathSelect: Sequential Token Selection for Whole Slide Pathology](https://arxiv.org/abs/2607.23631)

**<font color=#1a73e8>作者：</font>** Jingzhi Chen, Landi He, Zehong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gigapixel Whole-Slide Images (WSIs) present a fundamental computational bottleneck for vision-language models (VLMs) due to extreme sequence lengths. Existing approaches predominantly rely on spatial sampling or training-free pruning, which risk diluting weak but informative signals, leading to the loss of critical diagnostic evidence due to the spatially diffuse nature of pathological cues. We reformulate WSI token pruning as a sequential selection process, enabling the model to autonomously learn an optimal routing strategy rather than relying on static heuristics. We herein propose a decoupled routing framework integrated as an active plugin into the fully pre-trained SlideChat base model, leaving both the slide encoder and large language model frozen. To provide continuous gradients for the non-differentiable pruning operation during training, we introduce PathSelect. PathSelect employs a variance-preserving noise gate to modulate each patch's information flow via a differentiable Soft Top-K operator, paired with a diagonal-attention Denoiser that recovers the perturbed representations without semantic leakage. At inference, the PathSelect module is entirely detached. Relying solely on the trained Scorer, a deterministic Hard Top-K operator executes adaptive, data-dependent trajectory termination, significantly accelerating downstream generative processing with exceptionally low sequential token selection latency. Driven by an empirical average of only 44.86 tokens under a maximum constraint of K = 128, our framework achieves 74.00% overall accuracy on SlideBench (TCGA), representing an approximate 36.6x spatial token reduction relative to the uncompressed baseline average while consistently outperforming sampling-based counterparts.

---


### 150. [CALMRec: Causally Aligned Language Memory for Long-Horizon Recommendation](https://arxiv.org/abs/2607.23647)

**<font color=#1a73e8>作者：</font>** Gengyu Zhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can summarize heterogeneous user evidence in natural language, but current LLM recommenders often collapse enduring preferences, transient intent, and exposure-induced behavior into one profile. This makes recommendation vulnerable to feedback loops: repeated exposure is mistaken for preference, immediate clicks dominate delayed satisfaction, and fluent explanations need not reflect the ranking decision. We propose our method, a model-agnostic framework for long-horizon recommendation. Our method uses a frozen multimodal language model to convert item content and feedback into evidence-grounded semantic atoms, then maintains separate short-term, long-term, and exposure memories. Propensity-weighted updates reduce policy-induced exposure bias, while a conservative offline critic reranks candidates for delayed satisfaction under a behavior-support constraint. Explanations use only influential evidence atoms and are checked by counterfactual deletion. We provide an identification result and evaluate the framework in e-commerce-like, news-like, and short-video-like environments. Across ten seeds, our method improves discounted long-term value over the strongest alternative by 6.1%, 7.6%, and 6.7%, respectively. Twenty-seed paired ablations show significant value drops after removing propensity correction (0.739 +/- 0.191) or conservative support regularization (0.523 +/- 0.234). A frozen instruction language model also more than doubles semantic-atom NDCG over TF-IDF on a held-out paraphrase benchmark.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-240](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
