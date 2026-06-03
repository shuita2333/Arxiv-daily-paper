# 🧠 大模型相关研究 | 2026年06月04日

> 本类共 **188** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-188](./part-04.md)

---

### 101. [Evaluating LLMs' Effectiveness on Real-World Consumer Device Repair Questions](https://arxiv.org/abs/2606.03331)

**<font color=#1a73e8>作者：</font>** Atm Mizanur Rahman, Md Arid Hasan, Syed Ishtiaque Ahmed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Consumer device repair is an important but underexplored testbed for large language models (LLMs). Repair tasks require reasoning over incomplete problem descriptions, hardware-specific diagnostics, actionable troubleshooting, and safety-critical decisions, where incorrect advice can cause device damage, battery hazards, or permanent data loss. We introduce a benchmark of 991 real-world repair questions from Reddit spanning phone repair, computer repair, and data recovery, each paired with technician-written reference solutions, and provide Bangla translations to evaluate cross-lingual performance. We evaluate six state-of-the-art LLMs in English and Bangla using four repair-specific criteria: correctness, completeness, practicality, and safety. Our results show that while LLMs can provide useful repair assistance, they remain unreliable for high-risk real-world repair tasks without rigorous evaluation and explicit safety safeguards. Phone repair is the most difficult and safety-sensitive domain, and all models make substantial errors in board-level diagnosis, repair prioritization, and safe recovery procedures. Across domains and models, Bangla responses consistently perform worse than English responses. Among the evaluated models, GPT-5.4 performs best overall.

---


### 102. [Cross-Modality Feature Fusion Based on Structured State Space Duality for Multimodal Image Registration Network](https://arxiv.org/abs/2606.03341)

**<font color=#1a73e8>作者：</font>** Zhikang Li, Yan Wu, Xin Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In multi-modal image registration, the primary challenge lies in shared structural information extraction. Compared to Transformers, Structured State Space Duality (SSD) offers greater global structural feature extraction with higher efficiency during training and inference. Inspired by these advantages, we propose a novel algorithm for multi-modal image registration, named RegNetMamba-2. Our algorithm incorporates SSD into coarse-to-fine matching process to extract local and global structural features effectively. Firstly, SSD is applied in three different scales for multi-modal feature extraction in our network. To strengthen local representation, we pay more attention on foreground edge and structural information by feature scaling function of SSD. Secondly, for shared feature extraction of input images and multi-modal feature fusion in all scales, we propose cross-modality feature fusion model based on SSD, consisting of Cross-Modality feature Interaction (CMI) module and Multi-Scale feature Fusion (MSF) module. CMI module is designed for cross-modality feature extraction of each scale by SSD in cross form. MSF module is designed to employ a progressive upward fusion in feature-level to obtain fine features, consisting of multi-modal features in all scales. Following coarse-to-fine, the features in 1/8 scale from CMI and 1/2 scale from MSF are collected to calculate matching probability scores. Then we respectively establish matching process by correspondences of pixel-wise. Extensive experiments demonstrate that comparing with state-of-the-art deep-learning based algorithms, RegNetMamba-2 has achieved good effects in both performance and efficiency for multi-modal image registration on the following datasets: VIS-SAR (OSDataset), VIS-IR (LGHD/RoadSence) and VIS-NIR (RGB-NIR sense).

---


### 103. [See, Infer, Intervene: Proactive World Modeling for Goal-Oriented Social Intelligence](https://arxiv.org/abs/2606.03371)

**<font color=#1a73e8>作者：</font>** Honghui Zhang, Chenmeinian Guo, Yichen Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal retail agents should not only recognize what a customer is doing, but also decide whether and how to assist before an explicit request is made. We study this setting through the See--Infer--Intervene (SII) framework, where a device must see pre-interaction behavior, infer latent customer intent, and act by selecting an appropriate service intervention or choosing to wait. We instantiate SII with the Proactive Intent World Model (PIWM), which represents customer state with AIDA (Attention, Interest, Desire, Action) purchasing phases and BDI (belief, desire, intention) psychological fields, predicts action-conditioned intent transitions, and selects from five response classes: Greet, Elicit, Inform, Recommend, and Hold. We further construct GuidanceSalesBench, a smart-retail benchmark containing state manifests, pre-interaction videos, candidate responses, action-conditioned outcomes, and best-action labels. When conditioned on ground-truth customer state to isolate action selection, PIWM achieves 0.641 macro F1 on 30 held-out target videos, outperforming a zero-shot Qwen2.5-VL-7B baseline and training variants without balanced action supervision; end-to-end video-only selection drops to 0.295, below the 5-class balanced random baseline of 0.414, identifying video-to-state grounding as the dominant deployment-time bottleneck. A preliminary staged real-store pilot (recorded with paid participants performing scripted customer behaviors) reaches 0.579 action macro F1 on 20 fully annotated videos, with 10 additional accessible videos released with index-level labels.

---


### 104. [When Model Merging Breaks Routing: Training-Free Calibration for MoE](https://arxiv.org/abs/2606.03391)

**<font color=#1a73e8>作者：</font>** Canbin Huang, Tianyuan Shi, Xiaojun Quan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging has emerged as a cost-effective approach for consolidating the capabilities of multiple LLMs without retraining. However, existing merging techniques, largely based on linear parameter arithmetic or optimization, struggle when applied to Mixture-of-Experts (MoE) architectures. We identify a critical failure mode in MoE merging, termed routing breakdown, in which the merged router fails to dispatch tokens to suitable experts. Routing breakdown stems from the sensitivity of the non-linear softmax and discrete Top-k routing mechanisms to parameter perturbations from merging, a sensitivity further amplified by load-balancing constraints imposed during MoE pretraining. Because fine-tuned experts exhibit distinct specializations, even modest misrouting can cause severe performance degradation. To address this issue, we propose Hessian-Aware Router Calibration (HARC), a training-free framework that leverages second-order curvature information to realign the merged router. This approach admits a closed-form solution that can be efficiently solved using a matrix-free conjugate gradient method. Experiments on mathematical reasoning and code generation tasks show that HARC effectively mitigates routing breakdown across diverse MoE merging baselines and leads to substantial performance improvements. Our code is available at this https URL.

---


### 105. [Selective Token-Level Cryptographic Redaction for Privacy-Preserving Clinical Deployment of Large Language Models](https://arxiv.org/abs/2606.03399)

**<font color=#1a73e8>作者：</font>** Farhan Sheth, Ziyuan Yang, Yongying Lan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) are increasingly used for clinical applications, many existing pipelines require sending raw sensitive health information to remote servers for processing, which heightens the risk of privacy leakage. A natural approach to mitigate this risk is to encrypt the data before transmission. However, straightforward solutions such as encrypting the entire dataset introduce prohibitive computational, alignment, and communication overheads, rendering large-scale practical deployment infeasible. To preserve privacy while maintaining usability, we present Healthcare Encryption & Redaction via Adaptive Linguistic Decomposition (HERALD), a token-level cryptographic redaction framework designed to achieve this balance by encrypting only sensitive tokens while preserving the surrounding context for downstream model utility. HERALD combines medical named-entity recognizer (NER) with part-of-speech (POS) driven policies to select candidate tokens, performs targeted lemmatization to stabilize surface forms, and substitutes each protected token with a deterministic ciphertext wrapped in explicit delimiters. Notably, HERALD is model-agnostic and operates entirely on the client side, ensuring that sensitive content remains encrypted throughout storage, transmission, and processing without requiring changes to downstream models. We evaluated HERALD on both classification and medical question answering (MQA) tasks on public datasets. Across different tasks, experiments illustrate that fully secured baselines suffer significant utility loss, whereas HERALD consistently recovers performance close to plaintext. Overall, HERALD provides a novel utilization pipeline.

---


### 106. [Enginuity: A Dataset and Benchmark for Vision-Language Understanding of Engineering Diagrams](https://arxiv.org/abs/2606.03410)

**<font color=#1a73e8>作者：</font>** Abhishek Kumar, Isha Motiyani, Tilak Kasturi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Engineering diagrams pose a distinct challenge for vision-language models: unlike natural images or general documents, they encode information through dense spatial layouts, domain-specific symbols, and cross-references between visual callouts and structured parts tables. Despite their centrality to service, repair, and design workflows, there is no public benchmark for measuring VLM capabilities in this domain; existing datasets primarily focus on flowcharts, scientific figures, or business documents. To address this gap, we introduce Enginuity, the first open dataset and benchmark for evaluating VLMs on complex engineering diagrams. We define two tasks over a corpus of U.S. military service and repair manuals: structured parts-table extraction (Task 1) and free-form visual diagram question answering (VQA)(Task 2) for benchmarking. We evaluate four frontier VLMs (GPT-5.2 Chat, Claude Opus 4.7, Gemma 4, Qwen3-VL-32B-Instruct) under zero-shot and chain-of-thought prompting. On Task 1, models reach Recall@all of 0.61-0.87 but Token F1pen of only 0.03-0.18, exposing a systematic gap between part identification and description fidelity. Task 2 reveals a consistent factual-reasoning gap across all models. A supporting analysis shows that token-overlap metrics under-report model capability on technical descriptions by 2-6x relative to semantic similarity, motivating LLM-as-judge calibration for domain-specific evaluation. We release the dataset, annotations, evaluation harness, and per-sample model outputs to support a reproducible study of VLM capability on engineering content.

---


### 107. [IDO: Incongruity-aware Distribution Optimization for Multimodal Fake News Detection](https://arxiv.org/abs/2606.03418)

**<font color=#1a73e8>作者：</font>** Hengyang Zhou, Rongman Hong, Yuxuan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal fake news detection aims to identify the authenticity of news. Existing multimodal fake news detection methods mainly focus on cross-modal consistency, but often fail to explicitly model the semantic incongruity that characterizes deceptive multimodal content. However, misinformation often contains semantic information incongruity with the facts. To address these challenges, we propose Incongruity-aware Distribution Optimization (IDO) to improve the performance of fake news detection from the perspectives of factual incongruity and modality incongruity. For factual incongruity, we introduce a channel-wise reweighting strategy to obtain semantically discriminative embeddings and utilize gaussian distribution to model the uncertain correlation caused by factual incongruity. For modality incongruity, we utilize incongruity contrastive learning to learn cross-modal semantic information. Experiments demonstrate that IDO achieves state-of-the-art performance.

---


### 108. [CP-Agent: Context-Aware Multimodal Reasoning for Cellular Morphological Profiling under Chemical Perturbations](https://arxiv.org/abs/2606.03435)

**<font color=#1a73e8>作者：</font>** Yuxin Zhang, Yiyao Li, Ping Shu Ho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cell Painting combines multiplexed fluorescent staining, high-content imaging, and quantitative analysis to generate high-dimensional phenotypic readouts to support diverse downstream tasks such as mechanism-of-action (MoA) inference, toxicity prediction, and construction of drug-disease atlases. However, existing workflows are slow, costly and difficult to interpret. Approaches for drug screening modeling predominantly focus on molecular representation learning, while neglecting actual experimental context (e.g., cell line, dosing schedule, etc.), limiting generalization and MoA resolution. We introduce CP-Agent, an agentic multimodal large language model (MLLM) capable of generating mechanism-relevant, human-interpretable rationales for cell morphological changes under drug perturbations. At its core, CP-Agent leverages a context-aware alignment module, CP-CLIP, that jointly embeds high-content images and experimental metadata to enable robust treatment and MoA discrimination (achieving a maximum F1-score of 0.896). By integrating CP-CLIP outputs with agentic tool usage and reasoning, CP-Agent compiles rationales into a structured report to guide experimental design and hypothesis refinement. These capabilities highlight CP-Agent's potential to accelerate drug discovery by enabling more interpretable, scalable, and context-aware phenotypic screening -- streamlining iterative cycles of hypothesis generation in drug discovery.

---


### 109. [Large Language Models Are Overconfident in Their Own Responses](https://arxiv.org/abs/2606.03437)

**<font color=#1a73e8>作者：</font>** Mario Sanz-Guerrero, Manuel Mager, Katharina von der Wense  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work has shown that instruction-tuned large language models (LLMs) are less well calibrated than their base pre-trained counterparts. However, little is known about the frequently used chat template's effect on the calibration of conversational LLMs. In this work, we investigate the mechanisms driving this miscalibration by decoupling the effects of the post-training algorithm and the chat format. We find that, while instruction tuning fundamentally harms calibration, the chat template aggravates the issue through an "ownership bias" -- models are significantly more confident in their own answers than in identical answers provided by a user. Extensive experiments across six recent open-weight LLMs, three benchmarks, and three confidence elicitation methods show that models assign up to 26% higher confidence to their own responses. Leveraging this insight, we propose a simple inference-time strategy: framing the model's answer as user input during confidence elicitation. This approach significantly reduces overconfidence and improves calibration by up to 26% without the need for retraining, narrowing the gap between base and instruction-tuned models.

---


### 110. [PRISM: Synergizing Vision Foundation Models via Self-organized Expert Specialization](https://arxiv.org/abs/2606.03444)

**<font color=#1a73e8>作者：</font>** Ying Tang, Dong Li, Youjia Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unifying the complementary strengths of diverse Vision Foundation Models (VFMs) into a single efficient model is highly desirable but challenged by the negative transfer inherent in monolithic distillation. To address these feature conflicts, we introduce \textbf{PRISM}, a novel dual-stream Mixture-of-Experts (MoE) framework that synergizes VFMs via modular specialization. We propose a two-stage paradigm: (1) expertise deconstruction, where a teacher-conditional router guides experts to specialize in distinct representational subspaces to mitigate interference, followed by (2) dynamic recomposition, where the router learns to assemble these experts into tailored computational pathways for downstream tasks. Experiments on PASCAL-Context and NYUD-v2 show that \textbf{PRISM} establishes a new state of the art, validating that sparse, emergent specialization is a scalable approach for integrating diverse visual knowledge.

---


### 111. [What Makes Interaction Trajectories Effective for Training Terminal Agents?](https://arxiv.org/abs/2606.03461)

**<font color=#1a73e8>作者：</font>** Sidi Yang, Chaofan Tao, Jierun Chen 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Stronger code agents are commonly assumed to be superior teachers for post-training, yet this assumption remains poorly disentangled from task difficulty, harness design, and student capacity. We investigate this pedagogical link using Terminal-Lego, a scalable pipeline that transforms multi-domain real-world issues into environment-verified agentic tasks. Surprisingly, standalone performance does not dictate teaching efficacy: while Claude Opus 4.6 achieves higher scores on Terminal-Bench 2.0, students fine-tuned on trajectories from DeepSeek-V3.2, a lower-scoring agent, exhibit significantly stronger generalization. We attribute this "pedagogical paradox" to Environment-Grounded Supervision (EGS): trajectories that explicitly expose inspect-act-verify behaviors through harness-visible interactions allow students to internalize robust problem-solving routines rather than fragile action sequences. Scaling analysis reveals exceptional data efficiency: with only 15.3k Terminal-Lego trajectories, for example, Qwen3-32B achieves a 24.3% score on Terminal-Bench 2.0, rivaling previous SOTA performance established with over 30x the data volume. Our results suggest that the frontier of agent post-training lies beyond mere outcome-matching, shifting the focus toward "Harness Engineering", where the systematic design of environment-grounded interaction structures serves as the primary catalyst for reproducible and generalizable agentic intelligence.

---


### 112. [Rethinking the Role of Tensor Decompositions in Post-Training LLM Compression](https://arxiv.org/abs/2606.03465)

**<font color=#1a73e8>作者：</font>** Artur Zagitov, Alexander Miasnikov, Maxim Krutikov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training compression is essential for deploying large language models (LLMs) under tight resource constraints. Tensor decompositions have emerged as a promising direction, offering compact parameterizations well suited to Transformer weight structures. However, existing studies evaluate these methods in narrow settings, leaving unclear whether tensorization is effective at large-scale deployment. We systematically evaluate tensor compression across dense and MoE architectures, establishing performance trade-offs grounded in both empirical analysis and theoretical analysis. We identify a fundamental mismatch between the shared subspaces assumed by tensor decompositions and the heterogeneous representations learned by modern LLMs, thereby delineating their practical limits and clarifying their viable role in large-scale deployment. The code is available at this https URL.

---


### 113. [ThoughtFold: Folding Reasoning Chains via Introspective Preference Learning](https://arxiv.org/abs/2606.03503)

**<font color=#1a73e8>作者：</font>** Ziyan Liu, Xueda Shen, Yuzhe Gu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) have achieved remarkable progress thanks to Reinforcement Learning with Verifiable Rewards (RLVR) on Chain-of-Thoughts (CoTs). However, since long CoTs naturally contain trial and errors and mainstream RLVR approaches choose outcome-correct CoT trajectories for memorization, the redundant explorations in long CoTs are inevitably reinforced, which results in the over-thinking issues of LRMs. Previous attempts to resolve this issue mainly give more advantage to shorter trajectories, yet their learning signals are still outcome-based and cannot reduce the memorization of redundant explorations in long CoTs. Therefore, we propose ThoughtFold, a framework that leverages fine-grained preference learning to mitigate redundant explorations for efficient reasoning. ThoughtFold employs an introspective strategy to identify redundancy within each correct trajectory, which yields a spectrum of candidate sub-trajectories. Leveraging this spectrum, we introduce a masked preference optimization objective that explicitly penalizes redundant explorations and encourages the model to directly bridge essential reasoning segments, effectively folding its reasoning chains into a more concise path. Extensive experiments show that ThoughtFold significantly enhances efficiency. It reduces the token usage of DeepSeek-R1-Distill-Qwen-7B by approximately 56% while maintaining state-of-the-art accuracy.

---


### 114. [Overlaying Governance: A Compositional Authorization Framework for Delegation and Scope in Agentic AI](https://arxiv.org/abs/2606.03518)

**<font color=#1a73e8>作者：</font>** Amjad Ibrahim, Yong Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems evolve from passive models into autonomous active agents capable of initiating actions, collaborating, and delegating tasks, the traditional boundaries of software systems blur. Traditional authorization and delegation frameworks, built around fixed principals, explicit requests, and static scopes, are insufficient to govern agentic systems. Agentic AI demands richer authorization semantics: agents must inherit and delegate permissions, act under time-limited authority, and coordinate through shared protocols. Existing Identity and Access Management (IAM) systems fail to fully capture this notion of agency, lacking mechanisms for recursive delegation, contextual boundaries, and dynamic scoping as executable governance primitives. Unlike access delegation standards such as OAuth 2.0, we treat delegation as a contractual term rather than merely a static token-based consent credential. This paper proposes a compositional governance framework that introduces primitives indispensable for agentic AI. We define types of delegation and their permissions and accountability implications, and we introduce a notion of resource scope attenuation to bound agentic access envelopes. These concepts are expressed as general relational definitions that can be composed into existing authorization domains (e.g., financial systems). To operationalize this composition, we define a compositional operator that overlays new agentic semantics, such as recursive delegation chains, onto existing relational policies without rewriting them. We substantiate this framework through formal proofs and empirical evaluation, showing that it provides a formal yet practical foundation for accountable authorization in agentic AI systems.

---


### 115. [Attend to Anything: Foundation Model for Unified Human Attention Modeling](https://arxiv.org/abs/2606.03540)

**<font color=#1a73e8>作者：</font>** Wenzhuo Zhao, Ronghao Xian, Keren Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing human attention (saliency) modeling methods persist as highly fragmented across modalities, scenes, and task formulations. Consequently, even with increasing model capacity and data scale, current models predominantly remain scene-dependent and task-specific, failing to practically generalize in real-world applications. To address the fundamental limitations, we present the Attend to Anything Model (AAM), a multi-modal foundation model that unifies attention modeling across various image, video, and audio-visual tasks and scenes. AAM reformulates attention as a cognitive entailment relationship organized in a general-to-specific hierarchy, implemented through language prompts with hierarchical embeddings in hyperbolic space. Furthermore, to unify static image and dynamic video attention, we adopt a fluid-dynamics perspective, formulating video-frame attention as a diffusive temporal evolution governed by the Fokker--Planck equation. Extensive experiments on 16 benchmarks demonstrate that AAM consistently outperforms state-of-the-art methods by an average of 6\% across various scenarios, while achieving approximately a 4$\times$ speedup in video inference. Overall, these results demonstrate that AAM provides a principled foundation for future research on attention and saliency-related tasks. The dataset and code will be available at this https URL.

---


### 116. [\textsc{CR-Seg}: Attention-Guided and CoT-Enhanced Coarse-to-Refined Reasoning Segmentation](https://arxiv.org/abs/2606.03564)

**<font color=#1a73e8>作者：</font>** Yifan Cao, Xiaocui Yang, Faxian Wan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning segmentation aims to segment target objects described by complex language through joint visual-textual reasoning. Existing methods typically rely on either learned semantic tokens to bridge Multimodal Large Language Models (MLLMs) and segmentation models, suffering from difficult cross-modal alignment, or explicit spatial prompts such as bounding boxes, which may lose holistic response semantics. To address these limitations, we propose Attention-Guided and CoT-Enhanced Coarse-to-Refined Reasoning Segmentation, termed CR-Seg, a two-stage framework for coarse-to-refined reasoning segmentation. Specifically, we design an Extract Attention Maps and Points (EAP) module to extract attention maps for coarse target localization and select informative points, both of which are fed into SAM for mask refinement. To alleviate reasoning--answer inconsistency, we further introduce Global-to-Local Chain-of-Thought (GLCoT), which guides the model to reason progressively from global scene context to local target details. Extensive experiments on reasoning segmentation benchmarks demonstrate the effectiveness of CR-Seg.

---


### 117. [When Attention Collapses: Stage-Aware Visual Token Pruning from Structure to Semantics](https://arxiv.org/abs/2606.03569)

**<font color=#1a73e8>作者：</font>** Jiahui Wang, Kai Zhang, Mai Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated remarkable capabilities but suffer from significant computational overhead during inference. While visual token pruning offers a promising solution, existing methods predominantly rely on initial attention scores. This single-metric paradigm presents a critical flaw: high attention scores inherently collapse onto semantically similar regions, thereby severely reducing feature diversity and discarding vital contextual details. To address this, we introduce Structure-to-Semantics (STS), a novel two-stage visual token pruning framework that explicitly decouples the pruning process. The first stage employs a repulsion-based sampling mechanism to maximize spatial and structural diversity. The second stage leverages instruction-aware cross-attention to precisely filter out prompt-irrelevant tokens. This two-stage synergy constitutes the core of STS, first ensuring geometric coverage and then refining the retained tokens according to semantic relevance. Extensive evaluations demonstrate that STS mitigates the redundancy caused by attention-based selection, improving both structural diversity and fine-grained task alignment of the preserved visual tokens.

---


### 118. [AutoTail-BSFGM: Class-Balance-Aware Fine-Tuning for Chinese Scholarly Text Classification](https://arxiv.org/abs/2606.03576)

**<font color=#1a73e8>作者：</font>** Anling Xiang, Yuwen Yang, Yang Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scholarly text classification supports literature organization, subject indexing, and research intelligence, but Chinese scholarly corpora often contain imbalanced and semantically adjacent disciplinary labels. We propose AutoTail-BSFGM, a class-balance-aware fine-tuning method that combines an automatically gated tail-prior adjustment, a weak Balanced Softmax auxiliary loss, and Fast Gradient Method adversarial regularization. The method changes only the training objective and procedure; inference uses the same single base-size encoder and linear classifier as the corresponding label-smoothed baseline. We evaluate the method on two CSL-based tasks: an abstract-to-discipline task with 67 labels and a title-to-category task with 13 categories. On the primary abstract task, AutoTail-BSFGM improves validation and lockbox accuracy under both Chinese RoBERTa-WWM and MacBERT-base. With MacBERT-base, validation accuracy increases by 0.83 percentage points and lockbox accuracy by 0.49 points, with a pooled paired McNemar signal on validation (p = 0.023). On the title task, the method improves validation accuracy by 0.70 points and validation balanced accuracy by 2.64 points; lockbox accuracy is approximately neutral while lockbox balanced accuracy improves by 1.22 points. The results support a bounded contribution: AutoTail-BSFGM improves class-balance-sensitive behavior and yields consistent gains for abstract-based scholarly classification, without uniformly improving every metric on every split.

---


### 119. [Eliciting Complex Spatial Reasoning in MLLMs through Wide-Baseline Matching](https://arxiv.org/abs/2606.03577)

**<font color=#1a73e8>作者：</font>** Hao Zhong, Muzhi Zhu, Shenyan Zeng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wide-baseline matching (WBM) requires integrating geometric understanding, viewpoint changes, fine-grained perception, and occlusion reasoning, making it a challenging testbed for spatial reasoning in multimodal large language models (MLLMs) deployed in physical environments. However, current MLLMs lack systematic evaluation and training frameworks for these capabilities. We introduce ReasonMatch-Bench, a benchmark stratified by viewpoint displacement and matching granularity across indoor, outdoor, and object-centric scenarios, and show that current MLLMs still struggle with fine-grained wide-baseline correspondence: on a difficult 90-sample subset, human annotators achieve 84.0 F1, while the best existing baseline reaches 37.2. To bridge this gap, we build a scalable data-generation pipeline that automatically extracts wide-baseline view pairs from large-scale video-3D corpora, including RGB-D videos and SfM reconstructions, yielding diverse and verifiable supervision. We further propose Dynamic Correspondence Reinforcement Learning (DCRL), which combines Image-Level Viewpoint Progression and Point-Level Correspondence Curriculum to improve WBM training through verifiable rewards without explicit CoT supervision. Extensive experiments show that DCRL substantially improves ReasonMatch-Bench and transfers to related spatial benchmarks, while maintaining general visual understanding performance with modest gains on several benchmarks.

---


### 120. [CauTion: Knowing When to Trust LLMs for Ensemble Causal Discovery](https://arxiv.org/abs/2606.03602)

**<font color=#1a73e8>作者：</font>** Bo Peng, Kaiwen Wu, Sirui Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery from observational data remains challenging due to the fundamental limitations of purely statistical methods, such as statistical distinguishability within equivalence classes and sensitivity to finite sample sizes. While large language models (LLMs) offer a promising source of domain knowledge to complement statistical inference, existing LLM-augmented methods are vulnerable to LLM errors and incur high token costs. Moreover, reliance on a single data-centric algorithm can make results sensitive to algorithm-specific biases. To address these limitations, we propose CauTion, a framework that reliably integrates LLM domain knowledge into an ensemble of statistical causal discovery algorithms through consensus filtering and LLM reliability estimation. CauTion proceeds in three stages. First, an algorithm ensemble utilizes a consensus voting to resolve up to 96% of edges on which algorithms agree, achieving near-perfect accuracy on the filtered consensus edges. Second, a trust-calibrated arbitration mechanism estimates the relative reliability of the LLM and the algorithms via an annotation-free trust calibration procedure, which is then utilized to govern a trust-weighted voting process that restricts LLM arbitration exclusively to edges with unreliable algorithmic evidence. Third, a cycle repair step is applied to guarantee the final causal graph is validly acyclic. Experiments on six datasets demonstrate that CauTion consistently outperforms both data-centric and LLM-augmented baselines, with larger gains on larger graphs and strong robustness to LLM errors. Code is available at this https URL.

---


### 121. [World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning](https://arxiv.org/abs/2606.03603)

**<font color=#1a73e8>作者：</font>** Yucheng Zhou, Wei Tao, Yiwen Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models and multimodal large language models (MLLMs) provide complementary capabilities for predicting future outcomes from static visual observations. World models can generate concrete visual rollouts of possible futures, while MLLMs can reason abstractly over questions, goals, and rules. However, generated rollouts are stochastic and may be visually plausible but task-incorrect, making it necessary to determine when visual simulation is useful, whether a rollout is credible, and how it should influence the final answer. We formulate this problem as controlled concrete reasoning, where a model learns to invoke, verify, and integrate visual future simulation alongside abstract reasoning. To study this setting, we construct two human-verified benchmarks, VRQABench for controllable spatial lookahead and OpenWorldQA for open-domain physical prediction, and propose Privileged-Future On-Policy Self-Distillation (PF-OPSD). During training, PF-OPSD uses ground-truth future videos and answers only as teacher-side privileged context to evaluate on-policy concrete-reasoning trajectories, while the deployable student never observes true futures at test time. Experimental results show that PF-OPSD outperforms baseline by 10.6% and 10.9% on VRQABench and OpenWorldQA, respectively, while increasing robustness to noisy or conflicting rollouts. Our code and dataset are available at this https URL.

---


### 122. [Beyond the Literal: Decomposing Pragmatic Intent in Multimodal Meme Understanding](https://arxiv.org/abs/2606.03604)

**<font color=#1a73e8>作者：</font>** Zhengyi Zhao, Shubo Zhang, Zezhong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When asked what a meme or sarcastic post means, Large Vision Language Models (LVLMs) tend to describe what the image shows rather than what the author is trying to communicate. Standard instruction tuning entangles a post's literal content with its pragmatic meaning, letting surface-level details contaminate the final response. We reframe meme understanding as a problem of literal-pragmatic decomposition and propose \textbf{Intent Projection}, a framework that separates the two signals at the representation, output, and objective levels within a single LVLM backbone. At the representation level, an orthogonal projection module removes dominant unimodal directions from the fused image-text representation, retaining only the pragmatic residual, while a surface-real affect classifier anchors the decoder with a discrete tag that names the polarity gap. At the output level, the model externalizes a structured reasoning chain, and at the objective level a contrastive reward explicitly penalizes answers that restate the literal description. Across six multimodal benchmarks, Intent Projection consistently outperforms open-source baselines and narrows the gap to proprietary models, with the largest gains on high-divergence posts where literal collapse is most damaging.

---


### 123. [Cross-Lingual Token Arbitrage: Optimizing Code Agent Context Windows via Local LLM Preprocessing](https://arxiv.org/abs/2606.03618)

**<font color=#1a73e8>作者：</font>** Mehmet Utku Colak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-assisted coding agents are bottlenecked by input-token cost. Two pathologies of raw human input drive much of this overhead: tokenization inefficiency for non-English text and structural entropy in conversational prompts. Existing approaches act reactively by compressing already-bloated contexts or intervening after failures occur.
We introduce a pre-flight, edge-side prompt-rewriting middleware that operates between the developer and the cloud agent. A local Llama 3.2 (3B) model performs cross-lingual translation into English, structural rewriting into a compact task-oriented format, and regex-validated rewrite-with-fallback safeguards to ensure the optimized prompt is never larger than the original.
We evaluate on OMH-Polyglot, a multilingual coding benchmark spanning Turkish, Arabic, Chinese, and code-switched specifications. Across three commercial LLM backends, the middleware reduces prompt tokens by 34-47 percent and total tokens by up to 18.8 percent while preserving or improving task accuracy. Ablation studies show that gains arise primarily from the rewriting stage rather than simple function-name extraction. Compared with LLMLingua-2 at matched compression rates, our method consistently achieves superior OckScore performance across all evaluated backends. These results demonstrate that proactive prompt optimization can substantially reduce inference costs without sacrificing coding quality.

---


### 124. [Bridging Auxiliary Constraints to Resolve Instruction Following in Large Reasoning Models](https://arxiv.org/abs/2606.03624)

**<font color=#1a73e8>作者：</font>** Zhengyi Zhao, Shubo Zhang, Huimin Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) have demonstrated impressive capabilities in many tasks, yet they struggle with reliably following multiple instructions, either by failing to satisfy individual constraints or by struggling to balance competing constraints simultaneously. We formalize this challenge as the Constraint Adherence Problem (CAP). This paper introduces a novel framework that addresses CAP by representing instructions as a structured knowledge graph of constraints. Our approach, Constraint Relationship Graph Completion (CRGC), explicitly models relationships between constraints, identifies adherence challenges, and discovers ``bridge constraints'' that help the model better focus on and reconcile requirements. Bridge constraints act as auxiliary instructions that make primary constraints more salient and compatible. Unlike existing approaches that enhance instruction following through general training methods, CRGC specifically improves constraint satisfaction by leveraging the model's own knowledge to create better pathways for generation. Experiments across three popular instruction following datasets demonstrate that our approach reduces constraint violations by 39% compared to standard prompting while maintaining reasoning abilities of large reasoning models.

---


### 125. [TurtleAI: Benchmarking Multimodal Models for Visual Programming in Turtle Graphics](https://arxiv.org/abs/2606.03626)

**<font color=#1a73e8>作者：</font>** Chao Wen, Jacqueline Staub, Adish Singla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have been explored for visual programming, where they generate code to solve visual tasks. However, most prior work focuses on visual programming for productivity; it remains unclear how well current VLMs perform on education-oriented visual programming and what factors limit their performance. To bridge this gap, we introduce TurtleAI, a benchmark containing 823 tasks curated based on real-world visual programming tasks in the Turtle Graphics domain. Solving these tasks requires models to perceive geometric patterns, reason about spatial relationships, and synthesize Python code that faithfully reproduces geometric patterns. We evaluate 20+ VLMs, including GPT-5, GPT-4o, and Qwen2-VL-72B, and find that they struggle significantly, with most achieving success rates below 30%. To address these limitations, we propose a data generation technique that requires only a small set of seed samples. Fine-tuning Qwen2-VL-72B on the resulting synthetic data yields an improvement of about 20% on real-world tasks. Our failure analysis reveals that GPT-4o struggles with spatial reasoning and precise visual replication, whereas fine-tuning primarily improves the alignment between visual reasoning and code implementation.

---


### 126. [TSQAgent: Rating Time Series Data Quality via Dedicated Agentic Reasoning](https://arxiv.org/abs/2606.03629)

**<font color=#1a73e8>作者：</font>** Shunyu Wu, Dan Li, Haozheng Ye 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assessing the quality of time series (TS) data is fundamental yet inherently challenging due to the multifaceted nature of quality dimensions. Recently, large language models (LLMs) have emerged as a promising paradigm for TS quality assessment via pairwise comparison and per-dimension evaluation. However, existing approaches rely on manually predefined quality dimensions and purely text-based reasoning, leaving it unknown whether LLMs can identify truly relevant quality dimensions or perform grounded and quantitative quality comparisons. To investigate this, we construct TSQBench, a dedicated benchmark for evaluating LLMs on two progressive capabilities: (i) understanding and identifying relevant quality dimensions, and (ii) performing quality comparison under specific dimensions. Our analysis reveals that current LLMs consistently struggle with both dimension identification and evidence-grounded quality comparison. To address these limitations, we propose TSQAgent, a novel agentic reasoning framework for TS quality rating consisting of three collaborative roles: Perceiver for focused dimension selection, Inspector for dimension-wise quantitative analysis, and Adjudicator that aggregates and refines the final judgment. In particular, we introduce an agentic reasoning strategy that instills the ability to identify and prioritize the most relevant quality dimensions, and further propose an agent workflow equipped with external analytical tools to enable precise quantitative comparisons over selected dimensions. Experiments on both the proposed benchmark and eleven real-world datasets demonstrate that our framework not only substantially improves LLMs' capabilities in quality understanding and quantitative comparison but also effectively translates these improvements into better quality-aware data selection, leading to enhanced downstream performance and data efficiency.

---


### 127. [AnchorMoE: Interpretable Time Series Classification via Anchor-Routed MoE](https://arxiv.org/abs/2606.03631)

**<font color=#1a73e8>作者：</font>** Tao Xie, Zexi Tan, Haoyi Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series classification (MTSC) is pivotal in high-stakes domains, such as clinical diagnosis and industrial fault detection, where safe deployment necessitates transparent decision-making. However, isolating the temporal segments that drive model predictions is challenging because discriminative signals in real-world time series are typically sparse, heterogeneous, and heavily obscured by background noise. This paper, therefore, proposes AnchorMoE, an interpretable-by-construction classification framework. Built upon a Mixture-of-Experts (MoE) architecture, AnchorMoE encodes multi-view representations of local patches and routes them to specialized experts, ensuring that the final prediction is formulated as an exact additive decomposition over the input segments, facilitating ante-hoc transparency rather than relying on post-hoc estimations. To maintain the reliability of this decomposition under sparse signal distributions, we introduce a geometric orthogonality constraint that penalizes representational redundancy, compelling distinct experts to specialize in heterogeneous predictive patterns. Furthermore, an uncertainty-aware reliability gate is designed to dynamically calibrate the contribution of each segment, effectively suppressing residual background noise. Extensive experiments on real-world and synthetic benchmarks demonstrate that AnchorMoE achieves highly competitive classification performance while faithfully grounding its decisions in the raw time series.

---


### 128. [Gender-Dependent Diagnostic Substitution in LLM Medical Triage: Same Symptoms, Unequal Urgency](https://arxiv.org/abs/2606.03641)

**<font color=#1a73e8>作者：</font>** Qi Han Wong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate whether large language models produce different medical triage recommendations for identical neurological symptoms when only the patient's stated gender and age vary. Using three model families--Gemini 3.5 Flash, Claude Sonnet 4.6, and GPT-5.4-mini--we present a standardized symptom profile (persistent headache, blurred vision, morning nausea, visual disturbances) across seven demographic conditions: three age groups (25, 38, 65) x two genders (male, female), plus a gender-unspecified baseline (n = 30 per condition per model, 630 total trials). We find a stark, systemic gender-dependent triage disparity: young women receive significantly lower emergency room (ER) referral rates than age-matched men (Gemini: 0% vs. 23.3%; Claude: 6.7% vs. 96.7%; GPT: 6.7% vs. 66.7%, all p < 0.001). The disparity disappears at age 65 for all models. The primary mechanism is diagnostic substitution: the models anchor on a gender-associated diagnosis, preferentially classifying young women with Idiopathic Intracranial Hypertension (IIH)--a condition epidemiologically linked to women of childbearing age--while diagnosing men with generic increased intracranial pressure with space-occupying lesions in the differential. This diagnostic closure routes female patients to lower-urgency care (outpatient doctor appointments) despite comparable severity ratings (7-9/10). Our findings demonstrate that clinical LLMs replicate documented human clinical biases by using epidemiological priors to suppress triage urgency, suggesting that AI triage engines must decouple urgency assessment from probabilistic diagnostic priors. We release all code, prompts, and raw results.

---


### 129. [Spatial Transcriptomics-Guided Alignment Enhances Molecular Profiling in Pathology Foundation Model](https://arxiv.org/abs/2606.03644)

**<font color=#1a73e8>作者：</font>** Fengtao Zhou, Yingxue Xu, Zhengyu Zhang 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Comprehensive molecular profiling is essential for modern precision oncology but remains hindered by prohibitive costs, specimen exhaustion, and protracted turnaround times. While pathology foundation models (PFMs) have demonstrated potential for inferring molecular phenotypes from routine hematoxylin and eosin (H&E) whole-slide images (WSIs), current architectures primarily rely on vision-centric self-supervised learning or vision-language alignment, lacking the spatially resolved molecular supervision required to connect subtle morphological features with underlying genomic alterations. Spatial transcriptomics (ST) emerges as a transformative technology that enables transcriptomic quantification within intact tissue sections, thereby preserving the precise spatial link between histology and molecular profiles. In this study, we present a Spatial Transcriptomics-guided Alignment framework for Molecular Profiling (STAMP), which endows PFMs with intrinsic molecular awareness. To support this paradigm, we curated HumanST-1k, a human ST dataset spanning diverse anatomical organs and sequencing platforms. This atlas yields 1.8 million pairs of H&E patches and corresponding transcriptomic profiles, providing a corpus that links histological structures with their molecular states. To mitigate the technical noise inherent to raw transcriptomics, STAMP applies a pathway-informed alignment strategy that aggregates transcriptomic data into biologically functional pathways, which are subsequently integrated into PFMs via parameter-efficient fine-tuning. This alignment enriches the representation space of PFMs and unlocks their capacity to resolve sub-visual molecular signatures. The clinical utility of these augmented representations was validated through a multi-tier evaluation framework.

---


### 130. [The Shape of Addition: Geometric Structures of Arithmetic in Large Language Models](https://arxiv.org/abs/2606.03645)

**<font color=#1a73e8>作者：</font>** Liuyuan Wen, Xun Zhu, Lihao Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models exhibit paradoxical fragility in fundamental arithmetic, implying a disconnect between internal computation and discrete output. By analyzing the residual stream geometry during multi-operand addition, we identify the Iso-Raw-Sum Trajectory (IRST), a geometric structure where representations are anchored by semantic digits and modulated by continuous carry fibers. We propose the Noisy Quantization Model to explain this geometry, framing arithmetic errors as Geometric Slippages caused by internal neural noise pushing a continuous, latent Carry Potential across quantization thresholds. This geometric framework further elucidates Probe Versatility, explaining how lightweight probes can disentangle coexisting latent signals (such as ground truth versus hallucination) from a single activation vector. Finally, we validate these insights through a geometric consistency check method that effectively detects and corrects these quantization failures during inference. Our code is available at this https URL.

---


### 131. [Safety Measurements for Fine-tuned LLMs Should be Grounded in Capability](https://arxiv.org/abs/2606.03648)

**<font color=#1a73e8>作者：</font>** Krishnapriya Vishnubhotla, Hillary Dawkins, Isar Nejadgholi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting foundation large language models to a user's task or preferred style through fine-tuning can result in compromising the model's safety. Previous works examined the effects of fine-tuning on model safety in limited and seemingly random experimental settings. We argue that anchoring fine-tuning to a specific capability goal is essential for avoiding arbitrary empirical choices, allowing us to draw meaningful conclusions about safety impacts, and to compare mitigation methods on a consistent basis. We conduct a multi-dimensional evaluation of the effects of fine-tuning on model behavior by focusing on capability as well as safety. Our results surface important issues that (1) fine-tuned models can produce incoherent generations in response to safety prompts, (2) automated safety judgments are unreliable for such incoherent outputs, and (3) the conclusions about the effects of fine-tuning can change depending on the choice of safety benchmark as well as the safety evaluator.

---


### 132. [CoEval: Ranking Language Models for Custom Tasks Without Labeled Data or Trustworthy Benchmarks](https://arxiv.org/abs/2606.03650)

**<font color=#1a73e8>作者：</font>** Alexander Apartsin, Yehudit Aperstein  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Choosing or ranking language models for a specific application is hardest when no task-specific labeled data exists, and standard public benchmarks cannot be trusted, their items having likely leaked into pretraining, so scores reflect memorization rather than fitness. We present CoEval, an open-source, reusable framework that closes this gap end to end: from only a description of a task or domain, teacher models synthesize a fresh, attribute-controlled benchmark with no human labels, contamination-free because items are generated anew on each run, and a cross-family judge ensemble ranks candidate models with no human raters. Validated where ground truth exists, CoEval recovers the true model ranking and tracks ground-truth correctness at ho=0.86. The label-free judging needs no human calibration because judge-panel composition (vendor diversity), not size, drives reliability: a small, well-chosen cross-family panel is most reliable, while a single judge can be anti-correlated with ground truth (judge-choice regret 0.35) and the ensemble never is. Generated items show zero verbatim 13-gram overlap with five major public benchmarks; the panel cancels verbosity bias and precludes same-family self-preference. A four-task study produced 7,978 evaluations for USD 5.89. The same declarative pipeline applies to any domain and is cheap enough to re-run on every model release: a label-free, contamination-free leaderboard any team can regenerate for its own application.

---


### 133. [Diagnosing Knowledge Gaps in LLM Tool Use: An Agentic Benchmark for Novel API Acquisition](https://arxiv.org/abs/2606.03657)

**<font color=#1a73e8>作者：</font>** Jinnuo Liu, Yue Peng, Jinhan Niu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models for code generation often need to use APIs that are absent from their pretraining data. This requires more than recalling a function name: models must coordinate signatures, module paths, input-output contracts, semantics, and executable usage patterns. Existing novel-API benchmarks are typically static, rely on coarse pass/fail metrics, or use synthetic APIs that may not reflect real library evolution. We introduce NovelAPIBench, a fully automated dynamic benchmark that, for any base model and target library, discovers novel APIs, extracts decomposed knowledge bundles, generates executable coding tasks, and assigns failed samples to six diagnostic categories. Across about 1.9K tasks, four base models, and five domains, we compare knowledge injected through retrieval with knowledge internalized through parametric adaptation. We find that knowledge components are not interchangeable: usage examples are the strongest standalone signal, while the best two-component setting pairs signatures with either mechanisms or examples depending on the domain and backbone. Adding more context, especially source code, can hurt by increasing import-path errors. Parametric adaptation also does not replace retrieval once external knowledge is removed; rather, fine-tuning mainly teaches models how to use provided bundles, and this ability transfers to held-out libraries. These results suggest that retrieval and tuning play complementary roles: retrieval supplies volatile API content, while tuning improves procedural integration.

---


### 134. [From Answers to States: Verifiable Process-Level Evaluation of Chemical Reasoning in Large Language Models](https://arxiv.org/abs/2606.03660)

**<font color=#1a73e8>作者：</font>** Hongyu Guo, Hao Li, He Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as chemistry assistants, yet most chemistry benchmarks still score only final answers. This masks a critical failure mode: a model may output the correct molecule, product, or option while its reasoning violates chemical logic. Existing process-level evaluators are hard to scale because LLM judges and human step-level process annotation are costly, inconsistent, and vulnerable to hallucination. We introduce ChemCoTBench-V2, a rule-verifiable diagnostic benchmark for low-cost, auditable evaluation of structured, verifier-addressable chemical reasoning traces. It spans molecular understanding, molecule editing, molecular optimization, and reaction prediction, with 5,620 evaluation samples across 18 reporting tasks. Models must expose key intermediate steps in expert-designed templates, and those steps are checked with deterministic chemistry rules and, for closed-answer tasks, reference traces rather than another LLM judge. Open-ended molecular optimization is evaluated with oracle-verifiable state constraints rather than strict trace matching. The benchmark reports three separate signals: final-answer correctness, template adherence, and step-wise verifier correctness over expert-refined intermediate commitments. Experiments on frontier models reveal a persistent gap between final-answer success and structured-reasoning-state consistency: models often follow the requested format while failing chemical-step checks, or answer correctly with weak supporting reasoning. ChemCoTBench-V2 enables fine-grained model comparison and identifies the concrete step at which the trace first violates the verifier.

---


### 135. [EvoDrive: Pareto Evolution for Safety-Critical Autonomous Driving via Self-Improving LLM Agents](https://arxiv.org/abs/2606.03678)

**<font color=#1a73e8>作者：</font>** Tong Nie, Yuewen Mei, Yihong Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating safety-critical scenarios is essential for validating and improving autonomous driving systems, yet it inherently requires maximizing adversariality to expose failures while preserving realism. Existing methods usually manage this trade-off with handcrafted heuristics, confining generation to known priors and overlooking underexplored patterns. While recent open-ended agentic evolution can push this limit, unconstrained general agents lack strict simulator grounding and tend to collapse the multi-objective tension into single-scalar maximization. Here we present EvoDrive, the first automated, LLM-based agentic evolution framework for multi-objective scenario generation. EvoDrive employs a simulator-grounded actor-critic architecture where a memory-driven actor iteratively proposes improvements to the generators and critics filter out implausible candidates, and a self-evolving world evaluator routes promising proposals to optimize simulation budgets. EvoDrive further maintains a Pareto archive of evaluated candidates to preserve diverse attack-realism trade-offs and guide future evolution via simulation feedback. Benchmark results on MetaDrive and CARLA show that EvoDrive not only significantly expands the Pareto frontier across various generators, but also produces valuable scenarios for policy training.

---


### 136. [Speedrunning Tabular Foundation Model Pretraining](https://arxiv.org/abs/2606.03681)

**<font color=#1a73e8>作者：</font>** Salih Bora Ozturk, Alexander Pfefferle, Frank Hutter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretraining cost is a major bottleneck for research on tabular foundation models, slowing the iteration cycle for new architectures, priors, and optimization ideas. Yet the community lacks a simple way to compare and accumulate pretraining speedups. We introduce a community speedrun for nanoTabPFN: contributors modify a single-file training script and compete to reach a fixed downstream ROC AUC target on subsampled TabArena using one NVIDIA L40S GPU. The current best record reaches the target in 0.92 minutes, an 81x speedup over the 74.32 minute baseline while using 22x fewer synthetic datasets. The speedrun format provides a simple protocol for the community to add, verify, and stack pretraining improvements, with the leaderboard open to contributions. Code and records are available at this https URL.

---


### 137. [A Close Look At World Model Recovery In Supervised Fine-Tuned LLM Planners](https://arxiv.org/abs/2606.03685)

**<font color=#1a73e8>作者：</font>** Patrick Emami, Nan Qiang, Peter Graf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) improves end-to-end classical planning in large language models (LLMs), but do these models also learn to represent and reason about the planning problems they are solving? Due to the relative complexity of classical planning problems and the challenge that end-to-end plan generation poses for LLMs, it has been difficult to explore this question. In our work, we devise and perform a series of interpretability experiments that holistically interrogate world model recovery by examining both internal representations and generative capabilities of fine-tuned LLMs. We find that: a) Supervised fine-tuning on valid action sequences enables LLMs to linearly encode action validity and some state predicates. b) Models that struggle to use output probabilities for classifying action validity may still learn internal representations that separate valid from invalid actions. c) Broader state space coverage during fine-tuning, such as from random walk data, yields more accurate recovery of the underlying world model. In summary, this work contributes a recipe for applying interpretability techniques to planning LLMs and generates insights that shed light on open questions about how knowledge is represented in LLMs.

---


### 138. [The DeepSpeak-Agentic Dataset](https://arxiv.org/abs/2606.03686)

**<font color=#1a73e8>作者：</font>** Sarah Barrington, Maty Bohacek, Hany Farid  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present DeepSpeak-Agentic, a dataset of videos comprising over 37 hours of semi-structured conversations between a human and an embodied AI agent. We use this dataset to evaluate the automatic forensic identification (audio, video, or text) of AI agents, study the nature of human-agent interactions, and provide a benchmark for future advances in the large-language models and AI-generated voices and faces that power embodied AI agents. We also contribute a scalable data-capture system that creates agents, automatically pairs them with human crowd workers, records audiovisual conversations across specified scenarios, and identifies and separates the human and agent in the combined stream.

---


### 139. [Staying Alive: Uncensored Survival Analysis with Tabular Foundation Models](https://arxiv.org/abs/2606.03689)

**<font color=#1a73e8>作者：</font>** Mariana Vargas Vieyra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Survival Analysis (SA) is a statistical framework that models the time span until some event of interest occurs. Widely used in several domains, including healthcare and churn prediction, a central challenge in its applicability stems from the time of the event being partially observed or \emph{right-censoring}.
Tabular Foundation Models (TFM) have attracted significant interest in recent years due to their ability to perform prediction tasks in a single forward pass, requiring no dataset-specific parameter fitting. Despite their success, their application to prediction tasks on time-to-event data remains difficult due to right censoring. In this work, we present a training-free method to survival regression by leveraging TFMs to both predict the time of the event and iteratively impute right-censored data.
Our method uses a TFM to construct an Accelerated Failure Time (AFT) model requiring no training beyond fitting a single scalar parameter. Subsequently, by building on the Buckley-James estimator, we introduce a non-parametric in-context estimator for right-censored data. Our experiments on standard survival analysis benchmarks show that our method is competitive with several parametric and semi-parametric survival regression models that require training, including Cox regression and parametric AFT models.

---


### 140. [Does Language Shift Break Medical Vision-Language Models? Indonesian Radiology Visual Question Answering Case Study](https://arxiv.org/abs/2606.03693)

**<font color=#1a73e8>作者：</font>** Pieter Christy Yan Yudhistira, Dzaki Rafif Malik, Novanto Yudistira  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical Vision-Language Models (VLMs) are typically evaluated on English radiology visual question answering benchmarks, leaving their robustness under non-English clinical language largely unexplored. We introduce IndoRad-VQA, an Indonesian adaptation of VQA-RAD, to assess whether medical VLMs retain radiology reasoning ability when questions are asked in Bahasa Indonesia. Radiology question-answer pairs are translated into Indonesian with self-evaluation-based quality control to preserve clinical meaning, terminology consistency, and answer equivalence. We evaluate general-purpose, Southeast Asian multilingual, and medical-specific VLMs under English and Indonesian prompting settings. Beyond accuracy, we quantify the language robustness gap between English and Indonesian inputs. We also conduct an error analysis to identify failure modes of question answering, such as yes/no flips, laterality errors, and output-language mismatches. Our findings show that strong performance on English medical VQA benchmarks does not necessarily translate to robust behavior in Indonesian clinical contexts. We observe a performance gap of 8 to 25 percent between the English and Indonesian settings, depending on the evaluation metric. These results highlight the need for more inclusive multilingual evaluation of medical multimodal foundation models. The dataset is available at this https URL.

---


### 141. [Multi$^2$: Hierarchical Multi-Agent Decision-Making with LLM-Based Agents in Interactive Environments](https://arxiv.org/abs/2606.03698)

**<font color=#1a73e8>作者：</font>** Sangeun Park, Minhae Kwon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central goal of large language model (LLM) research is to build agentic systems that can plan, act, and adapt through sustained interaction with dynamic environments. While recent LLM-based agents exhibit impressive contextual reasoning, their long-horizon decision-making remains fragile, often suffering from objective drift, where goals and plans drift over extended interactions. We introduce Multi$^2$, a hierarchical multi-agent decision-making framework that explicitly decomposes agent behavior into complementary roles. A high-level agent (System 1) focuses on context-aware sub-goal generation using supervised fine-tuning (SFT), while a low-level agent (System 2) executes atomic actions through offline-to-online reinforcement learning (RL) in interactive environments. This separation enables stable long-horizon control, mitigates objective drift, and allows efficient adaptation. Across diverse interactive environments, Multi$^2$ consistently outperforms strong agentic baselines, demonstrating improved robustness and coordination in multi-turn interaction. Beyond performance, we introduce and release three hierarchical benchmark datasets, filling a long-standing gap in training and evaluating hierarchical decision-making for LLM-based agents.

---


### 142. [Dynamic Objective Selection with Safeguards and LLM Oversight for Financial Decision-Making](https://arxiv.org/abs/2606.03704)

**<font color=#1a73e8>作者：</font>** Keigo Sakurai, Takahiro Ogawa, Miki Haseyama 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial decision-making tasks such as stock recommendation and portfolio allocation typically estimate future return and risk and then select trades or allocations for an investor, and the chosen optimization objective often determines realized performance. However, because market conditions evolve over time, a fixed objective can be suboptimal across regimes, while regime-switching pipelines that rely on latent regime estimates can be noisy or delayed and frequent switching can increase turnover and operational instability. In this paper, we propose DOSS (Dynamic Objective Selection with Safeguards), a learning-based selector that directly chooses the decision-relevant objective function at each time point from interpretable statistical summaries of recent returns, selecting among a small set of candidates (e.g., return-seeking, loss-averse, and risk-adjusted) without introducing intermediate regime variables. DOSS formulates objective selection as a classification problem over objectives and performs sequential updates with a rolling window to make forward-looking selections without temporal leakage, while also outputting a confidence score for each proposal. To mitigate misselection and excessive switching in deployment, DOSS applies confidence-aware gating with a fail-safe that overrides low-confidence proposals to a conservative default and enforces explicit controls tied to switching frequency. We further integrate governance by positioning a Large Language Model (LLM) as an oversight component rather than a generator of new objectives: the LLM is restricted to accept a proposed objective or override it to a predefined safe default, with deterministic rule-based constraints triggering overrides when needed.

---


### 143. [Code-on-Graph: Iterative Programmatic Reasoning via Large Language Models on Knowledge Graphs](https://arxiv.org/abs/2606.03705)

**<font color=#1a73e8>作者：</font>** Weiwei Ding, Zixuan Li, Long Bai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Graphs (KGs) are widely used to mitigate the limitations of Large Language Models (LLMs), such as outdated knowledge and hallucinations. Existing LLM-KG integration frameworks typically rely on predefined operators to retrieve factual knowledge from KGs and inject it into prompts for answer generation. This paradigm faces two critical bottlenecks: 1) Inflexibility: The predefined operators are limited in scope and thus lack sufficient compositional expressiveness to fully capture the complex semantics required by KG questions. 2) Unscalability: Direct injection of factual knowledge into prompts limits scalability in handling large-scale factual knowledge. To address these two bottlenecks, we propose Code-on-Graph (CoG), a programmatic reasoning framework for LLM-KG integration. Specifically, given the factual knowledge retrieved at each reasoning step, CoG first identifies the corresponding KG schemas and represents these schemas as Python classes, which serve as abstract interfaces to the retrieved facts. It then generates executable code grounded in these classes, with the retrieved facts instantiated as objects of the corresponding classes during execution. This design enables flexible code-based reasoning while avoiding the direct injection of large-scale factual knowledge into prompts. Experiments on WebQSP, CWQ, and GrailQA demonstrate that CoG outperforms prior state-of-the-art models by up to 10.5%.

---


### 144. [When Graph Tokens Sink: A Mechanistic Analysis of Graph Language Models](https://arxiv.org/abs/2606.03712)

**<font color=#1a73e8>作者：</font>** Ding Zhang, Runtao Zhou, Wenqing Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Language Models (GLMs) have become a promising direction for adapting Large Language Models (LLMs) to graph learning tasks. By transforming graph topology and node information into graph tokens, GLMs allow LLMs to jointly process structured graph inputs and textual instructions. Yet, it remains unclear how LLMs internally interpret these graph tokens and whether graph tokens act as meaningful carriers of graph structure. In this work, we analyze how LLMs process graph information through graph-token behavior in representative GLM architectures.
Findings. We find that the internal saliency of graph tokens in GLMs is not equivalent to graph information utilization. Graph sink tokens consistently emerge as activation-level outliers: they can be identified by massive activation values along a small set of hidden-state dimensions and are biased toward early graph-token positions. However, this activation-level saliency does not imply that these tokens are the main carriers of graph information. Unlike classical attention sinks in language and vision-language models, graph sink tokens do not necessarily attract the largest attention weights from query tokens. Through pruning, repositioning, and swapping interventions, we show that graph sink tokens are not the most important semantic or structural tokens for downstream prediction.
Implications. Together, these results suggest that after current GLMs map graph structure into the LLM token space, the resulting graph-token representations do not naturally form a fully usable topology-aware internal representation; instead, they exhibit a decoupling between activation-level saliency and graph-semantic utility. This decoupling points to limitations in existing graph-token construction, placement, and alignment mechanisms.

---


### 145. [Investigating Adversarial Robustness of Multi-modal Large Language Models](https://arxiv.org/abs/2606.03713)

**<font color=#1a73e8>作者：</font>** Hashmat Shadab Malik, Muzammal Naseer, Salman Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal Large Language Models (MLLMs) achieve strong performance on vision-language tasks, but incorporating visual inputs through a vision encoder (e.g., CLIP) substantially expands the attack surface, making these models vulnerable to visual adversarial perturbations. Prior defenses typically preserve compatibility with pretrained MLLMs by enforcing strict alignment to CLIP's original embedding space during adversarial fine-tuning; while practical, this constraint fundamentally limits achievable robustness. We present a systematic investigation of adversarial robustness in MLLMs. We first introduce a diagnostic CLIP-alignment protocol that predicts, prior to full MLLM training, which robust vision encoders will transfer effectively to the multimodal setting, revealing that large-scale multimodal adversarial pretraining, rather than unimodal scale alone, is the critical factor for strong robustness transfer. Integrating such encoders into MLLMs via end-to-end multimodal training yields average gains of 28 CIDEr points on captioning and 11.7% VQA accuracy under strong adversarial attacks compared to constrained plug-and-play baselines. We further show that adversarial training applied directly to a standard non-robust MLLM degrades both clean and adversarial performance, establishing robust visual representations as a strict prerequisite, while end-to-end adversarial training from a robust backbone delivers additional gains of 1.9 CIDEr points and 4.3% VQA accuracy. Beyond training-time defenses, lightweight test-time visual stochastic transformations serve as an effective black-box defense for non-robust MLLMs, elevating adversarial performance from near-zero to levels comparable with robust models. Finally, we show that our robust models substantially reduce toxic generation under white-box visual jailbreak attacks. Code and pretrained weights will be released publicly.

---


### 146. [Re-Ranking Through an Attribution Lens for Citation Quality in Legal QA](https://arxiv.org/abs/2606.03728)

**<font color=#1a73e8>作者：</font>** Mohamed Hesham Elganayni, Selim Saleh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation systems for legal question answering typically retrieve passages based on semantic similarity and provide them to a language model, which then generates cited answers. Prior work assumes that highly ranked passages are most likely to be usefully cited by the model. Perturbation-based attribution methods, such as C-LIME, have been used exclusively for post-hoc explanation. However, on the AQuAECHR benchmark, semantic similarity does not correlate with passage attribution. Within a retriever's candidate pool, similarity-based ranking performs worse than random selection at surfacing gold citation paragraphs. To address this limitation, a lightweight cross-encoder is trained on continuous perturbation-based attribution scores to re-rank passages prior to generation. This approach is evaluated on the AQuAECHR benchmark, using two language models and five-fold cross-validation. The re-ranker substantially improves citation faithfulness and alignment with gold expert answers. Notably, two re-rankers trained independently on different models converge beyond their raw attribution agreement. This finding indicates that the cross-encoder reduces model-specific noise and produces a shared relevance signal that partially transfers across models, although same-model re-ranking remains more effective. These results demonstrate that perturbation-based attribution provides a practical, model-agnostic training signal for citation-aware retrieval.

---


### 147. [Beyond False Stability: High-Noise Drift Gating for Test-Time Adversarial Defenses in Vision-Language Models](https://arxiv.org/abs/2606.03730)

**<font color=#1a73e8>作者：</font>** Hashmat Shadab Malik, Muzammal Naseer, Salman Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) such as CLIP show strong zero-shot generalization but remain highly vulnerable to adversarial attacks. Adversarial training improves robustness but is computationally expensive, motivating test-time defenses. Recent approaches exploit how CLIP's visual representations respond to stochastic perturbations: aggregating predictions across noisy views, constructing Gaussian noise-averaged anchors and interpolating features toward them, or applying counter-perturbations. These strategies improve robustness but often degrade clean accuracy, yielding an unfavorable clean-robust trade-off. We revisit stochastic test-time defenses and identify an underexplored noise-regime transition in CLIP's representation space. Prior work explored perturbations mainly in the weak-noise regime, where adversarial examples can appear unusually stable (false stability). Our analysis shows this reverses as perturbation strength grows: beyond the weak-noise regime, adversarial representations become markedly more unstable than clean ones, giving a clearer separation signal. The transition is consistent across uniform and Gaussian noise, photometric and geometric transforms, datasets, and diverse attacks. It largely disappears in adversarially trained models, suggesting it is tied to the fragile local-basin geometry of adversarial representations in non-robust CLIP. We propose a training-free, plug-in drift-gated mechanism that uses high-noise feature drift as a lightweight gating signal to trigger existing test-time defenses only when adversarial-like instability is detected. Across 13 datasets it consistently improves the clean-robust trade-off. On eight fine-grained datasets, mean clean+adversarial accuracy rises from 65.7% to 71.4% for counterattack defenses and 68.4% to 73.2% for noise-anchoring; on ImageNet and four shifted variants, from 56.1% to 66.2% and 62.1% to 67.6%.

---


### 148. [Conformal Language Modeling via Posterior Sampling](https://arxiv.org/abs/2606.03731)

**<font color=#1a73e8>作者：</font>** Nicolas Emmenegger, Theo X. Olausson, Armando Solar-Lezama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models remain plagued by hallucinations. Recent work has sought to tame their prevalence using statistical techniques based on conformal prediction, with both theoretical and empirical success. However, these methods operate in a post-hoc fashion, treating the sampling procedure itself as atomic and then surgically altering samples to remove hallucinated claims. This disconnect between filtering and generation can result in samples that are incoherent, inconsistent, or simply unlikely under the model itself. Moreover, post-hoc surgery is unable to shift probability mass towards more useful and helpful responses. To address these issues, we propose to instead sample from approximations to an LLM posterior, where the conditioning event corresponds to a calibrated, high-scoring region. We develop a calibration procedure tailored to the setting of conditional sequential generation that effectively identifies this region and achieves target risk control. Empirically, we apply our method to case studies focused on open-ended biography generation and mathematical problem solving; compared to prior work, we obtain the same statistical guarantees, with higher downstream utility.

---


### 149. [Entropy Gate: Entropy Quenching for Near-Lossless Token Compression in LLM Pipelines](https://arxiv.org/abs/2606.03739)

**<font color=#1a73e8>作者：</font>** Justice Owusu Agyemang, Jerry John Kponyo, Kwame Opuni-Boachie Obour Agyekum 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM pipelines waste substantial token budgets on low-information content: repeated context, verbose responses, and redundant boilerplate. We introduce Entropy Gate, a token compression framework applying entropy quenching $-$ a thermodynamic process that progressively freezes out low-energy tokens while preserving semantic fidelity. Each token receives a multi-factor information energy $E(t)$ combining statistical, structural, and positional components. An adaptive quenching schedule $T(\tau) = T_0 / (1 + \alpha \tau)$ removes tokens whose Boltzmann survival probability $p_i = \exp(-E_i / kT)$ falls below threshold, with a fidelity gate halting compression when energy-weighted similarity drops below $\theta$. We prove token selection by descending $E(t)$ maximizes expected semantic preservation, that quenching produces nested survival sets, and that achievable compression approaches the information-theoretic limit $\text{CR} \to 1 - I(P; T)/H(P)$. A Phase 1 heuristic achieves 40-60% compression across five prompt categories while maintaining $S_E > 0.80$, with energy-squared amplification $E \to E^2$ adding 10-25 percentage points. Context deduplication adds 50-70% savings on repeated blocks. Output-side quenching, motivated by findings that brevity improves accuracy, further reduces response overhead. Combined with external memory, reduction composes multiplicatively to 88-96% for agentic workloads. The framework is stateless, model-agnostic, and deploys as an OpenAI-compatible HTTP proxy.

---


### 150. [Proof-Refactor: Refactoring Generated Formal Proofs into Modular Artifacts](https://arxiv.org/abs/2606.03743)

**<font color=#1a73e8>作者：</font>** Yiming Fu, Peixuan Liu, Zichen Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have shown strong performance in generating formal proofs, their outputs often remain less readable, modular, maintainable, and reusable than proofs in mature formal mathematics libraries. We argue that this gap stems in part from the compile-first objective implicit in most proof-generation pipelines, which encourages monolithic or ad hoc proof scripts rather than library-quality artifacts. Existing approaches to proof-quality improvement often rely on explicit, computable optimization objectives. In practice, however, the most tractable and experimentally validated objectives are largely length-based, while higher-level qualities such as readability, modularity, maintainability, and reusability are difficult to reduce to reliable automatic metrics. Instead of optimizing proof improvement against a single proxy metric, we take a process-guided approach inspired by human proof-refactoring workflows. We propose an agentic framework $\textbf{Proof-Refactor}$ that decomposes proof refactoring into four phases: extracting candidate proof fragments, designing helper declarations, formally proving the extracted and designed components, and repairing the original proof using the verified components. On generated Lean proofs from PutnamBench and Putnam2025, Proof-Refactor improves rubric-based refactoring scores over a strong Claude Code refactoring baseline, with the largest gains in signature quality and human readability. These results suggest that process-guided refactoring can improve proof structure without treating proof length as the primary objective.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-188](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
