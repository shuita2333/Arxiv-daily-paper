# 🧠 大模型相关研究 | 2026年06月17日

> 本类共 **270** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

---

### 101. [MosaicQuant: Inlier-Outlier Disaggregation for Unified 4-Bit LLM Quantization](https://arxiv.org/abs/2606.15652)

**<font color=#1a73e8>作者：</font>** Yangjia Hu, Haodong Wang, Zicong Hong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> 4-bit quantization significantly reduces the memory footprint and accelerates the inference of large language models (LLMs). However, its limited bit-width representation struggles to faithfully capture both dense common values (\emph{inliers}) and rare large-magnitude values (\emph{outliers}), causing substantial accuracy degradation. Existing mixed-precision methods mitigate this by retaining outliers in high precision, but at the cost of breaking the uniformity of low-bit execution, introducing precision conversion and extra data movement that undermine practical speedup. We propose \textbf{MosaicQuant}, a unified 4-bit LLM quantization paradigm built on a novel principle of \emph{inlier--outlier disaggregation}. Rather than elevating outlier precision, MosaicQuant quantizes the full weight matrix into a dense 4-bit base component, where inliers are captured faithfully while outlier are inevitably quantized. A sparse 4-bit residual component is then introduced to compensate for these quantization errors, selectively targeting the most error-critical weight blocks where output distortion is shown to be concentrated. However, a unified representation alone is insufficient, as naïvely executing the sparse residual as a separate kernel still breaks the unified low-bit inference pipeline. To bridge this gap, we introduce \textbf{ZipperEngine}, which fuses sparse block computation into the dense 4-bit GEMM kernel via an overlapped pipeline, unifying not only the representation but also the execution into a single coherent low-bit inference pipeline. Extensive experiments on LLaMA3 and Qwen3 demonstrate that MosaicQuant preserves near-FP16 accuracy while achieving up to $1.24\times$ speedup over the W16A16 baseline.

---


### 102. [Overcoming the Impedance Mismatch: A Theoretical Roadmap for Fusing Foundation Models and Knowledge Graphs](https://arxiv.org/abs/2606.15656)

**<font color=#1a73e8>作者：</font>** Sahil Rajesh Dhayalkar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern artificial intelligence remains fundamentally divided between the continuous, probabilistic spaces of Foundation Models and the discrete, deterministic structures of Knowledge Graphs. While Retrieval-Augmented Generation (RAG) attempts to connect them by serializing graph data into text, we argue this lexical bridging is merely a superficial patch. In this paper, we formalize the underlying structural and geometric friction as the \textit{Impedance Mismatch}. By categorizing current neuro-symbolic integration strategies into a three-tiered hierarchy, we demonstrate that neither surface-level prompt injection nor continuous representation alignment can preserve the strict logical motifs required for reliable multi-hop reasoning. We define the specific mathematical limits, such as the Lexical Bottleneck and Topological Collapse, that show current architectures will eventually hallucinate or conflate semantic nodes. To achieve true semantic fusion, we propose a rigorous theoretical roadmap. We advocate for natively internalizing discrete symbolic structures through Structured Residual Streams, utilizing Vector Symbolic Architectures for latent sub-graph injection, and performing model updates via Orthogonal Subspace Editing. This actionable framework paves the way for models that seamlessly fuse the precision of symbolic logic with the expressivity of parametric memory.

---


### 103. [OneFocus: Enabling Real-World X-ray Security Screening with a Unified Vision-Language Model](https://arxiv.org/abs/2606.15663)

**<font color=#1a73e8>作者：</font>** Jiali Wen, Hongxia Gao, Litao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> X-ray contraband detection is critical for security in large-scale logistics and transportation, yet conventional detectors struggle to adapt to emerging contraband types and lack fundamental visual understanding. Vision-language models (VLMs) offer strong generalization but are hindered by the scarcity of high-quality X-ray image-caption data. To bridge this critical gap, we present MMXray, a meticulously curated benchmark of 52,124 image-caption pairs spanning 28 fine-grained classes of X-ray contraband. To enrich MMXray with realistic occlusion patterns, we further introduce CleanDET, a dedicated synthesis dataset containing clean foreground contraband images from 28 categories and background images with diverse density levels, together with AnyContraSyn, a controllable synthesis method designed to operate on CleanDET. We also develop OnePipe, an extensible pipeline for systematic data curation. Built on MMXray, we propose OneFocus, a unified VLM that supports four core tasks: visual question answering, contraband localization, classification, and image understanding. OneFocus achieves state-of-the-art performance in X-ray contraband understanding and demonstrates robust cross-domain generalization, establishing a strong vision-language baseline for security screening.

---


### 104. [Recurrent Reasoning on Symbolic Puzzles with Sequence Models](https://arxiv.org/abs/2606.15686)

**<font color=#1a73e8>作者：</font>** Gowrav Mannem, Chowdhury Marzia Mahjabin, Jason Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models often appear strong on symbolic and algorithmic tasks, yet this apparent strength can hide brittle behaviour when problems become longer, harder, or slightly out of distribution. A major limitation of current reasoning benchmarks is that many primarily test whether a model can produce a valid answer, while paying less attention to whether the solution is minimal, robust, and stable under controlled difficulty scaling. We introduce RecurrReason, a difficulty-controlled benchmark of four recurrent logic puzzles (Tower of Hanoi, River Crossing, Block World, and Checkers Jumping) with BFS-optimal trajectories and a single interpretable difficulty parameter $N \in \{1,\dots,10\}$, totalling 10{,}817 unique puzzles and 285{,}933 moves. We benchmark two Transformer families, an encoder-decoder model (T5-style) and a decoder-only model (GPT-2-style), under consistent data splits and evaluation criteria, training on $N{=}1$ to $7$ and evaluating on both held-out in-distribution instances and harder out-of-distribution instances at $N{=}8$ to $10$. Fine-tuned pre-trained T5 achieves 97.27\% validation and 81.00\% OOD accuracy on Block World; all models score 0.00\% on River Crossing under all conditions. Failure mode analysis reveals that architecture is a stronger determinant of success than scale. Pre-training transfers only to puzzles with locally structured transition functions. Our code and dataset will be open-sourced upon acceptance.

---


### 105. [Do LLMs Reliably Identify Correct Information Units in Aphasic Discourse?](https://arxiv.org/abs/2606.15696)

**<font color=#1a73e8>作者：</font>** Jason M Pittman, Yesenia Medina-Santos, Anton Phillips Jr. 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Correct Information Units (CIUs) are central to discourse assessment in aphasia because they quantify communicative informativeness rather than linguistic form alone. However, CIU scoring is time intensive and requires trained raters. This study examined whether instruction-tuned large language models (LLMs) can reliably perform token-level CIU classification from aphasic discourse transcripts. Sixteen picture-description transcripts elicited with the Cat Rescue stimulus were annotated for CIU status according to Nicholas and Brookshire (1993). The sample spanned four severity strata: control, mild, moderate, and severe aphasia. Four publicly available instruction-tuned LLMs were benchmarked under zero-shot and two few-shot prompting conditions across five stratified random seeds. Performance was evaluated against consensus human labels using accuracy, precision, recall, F1, and Cohen's kappa. Zero-shot prompting was insufficient across models. In contrast, few-shot prompting yielded substantial gains and produced competitive performance for three viable models. Mean few-shot F1 scores ranged from 0.776 to 0.817 across Llama-3.1-8B, Qwen2.5-7B, and Mistral-7B, with no significant differences between fixed global and per-chunk local example selection. Phi-3-mini was unstable and did not yield reliable performance. Viable models showed high recall but lower precision, suggesting systematic over-classification of tokens as CIUs. Performance also varied by discourse severity, with the weakest results in more severe aphasia. Few-shot LLM prompting can support automated CIU identification without gradient-based task training, but agreement with human annotation remains insufficient for fully autonomous use. These findings support LLM-based CIU scoring as a promising human-in-the-loop component of discourse assessment systems.

---


### 106. [AI-Driven Framework for Adaptive Water Network Management with Proof-of-Concept Implementation: Addressing Non-Revenue Water in Jordan](https://arxiv.org/abs/2606.15709)

**<font color=#1a73e8>作者：</font>** Mohammed Fasha, Nahel Al-Maayta, Bilal Sowan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Jordan faces severe water scarcity with 50\% of water produced is lost to leakage, theft and metering issues also known as non-revenue water (NRW). Traditional reactive approaches have proven insufficient for sustained NRW reduction. This paper proposes an intelligent framework integrating EPANET hydraulic modeling, digital twin technology, SCADA systems, and large language model (LLM)-based AI agents for continuous network monitoring and adaptive decision-making. The system combines real-time data streams with physics-based simulation to detect anomalies, employing retrieval-augmented generation (RAG) for policy interpretation and function calling for network control. A proof-of-concept implementation validates technical feasibility using EPYT with offline LLMs (llama3.1:8b via Ollama) on a 1,164-junction Amman district network. The system demonstrates automated hydraulic simulation, flow-based anomaly detection aligned with water distribution zone (DZ) practice, and AI-generated health reports with response times under 2 minutes and zero API costs. Burst detection relies on local flow anomaly analysis: a 30.1~L/s simulated leak produces measurable flow redistribution in 15 pipes, flagging a 15-junction cluster that localises the burst -- confirming alignment with water distribution zone (DZ) monitoring practice. The framework accommodates Jordan's intermittent supply patterns and limited automation through phased implementation, offering a scalable pathway for water-scarce regions to leverage intelligent automation for NRW reduction and operational efficiency.

---


### 107. [Beyond English: Uncovering the Multilingual Gap in Vision-Language-Action Models](https://arxiv.org/abs/2606.15714)

**<font color=#1a73e8>作者：</font>** Hanyang Chen, Hongliang Li, Jiarui Cao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action models have recently demonstrated promising capabilities in learning generalist robot policies from large-scale multimodal data. However, most existing VLA systems are trained and evaluated primarily with English instructions, leaving their ability to understand and execute instructions in other languages largely unexplored. While the underlying large language models often possess multilingual capabilities, it remains unclear whether these multilingual capabilities transfer to VLAs during training. In this work, we present the first systematic study of multilingual instruction following in VLA models. We first construct multilingual instructions by extending existing benchmarks with translations of their instructions. Using these instructions, we evaluate several representative VLA models across a range of tasks in simulation settings. Our experiments reveal a significant multilingual gap: models trained primarily on English instructions exhibit substantial performance degradation when evaluated on other languages, even when the underlying language backbone is multilingual. We provide several findings and analyses to understand the multilingual gap. Cross-lingual transfer behavior analysis shows that performance drops correlate with both instruction understanding and action execution. Representation analyses suggest that multilingual instruction-caused representation shifts may contribute to the multilingual gap. Motivated by these findings, we further explore strategies to improve multilingual performance in VLAs. We propose a simple yet effective multilingual fine-tuning approach, Multilingual Principal Component Alignment, which leverages Principal Component Analysis to get the principal component subspace and align projected multilingual representations, effectively reducing the multilingual performance gap.

---


### 108. [How to Score Experts for One-Shot MoE Expert Pruning: A Unified Formulation and Selection Principle](https://arxiv.org/abs/2606.15716)

**<font color=#1a73e8>作者：</font>** Zongfang Liu, Jinghui Zhang, Zijian Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) language models reduce per-token computation through sparse expert activation, yet deployment still requires storing the full expert pool, making one-shot expert pruning a practical approach for reducing memory usage. Although effective, existing criteria are largely heuristic, and no single criterion is universally optimal. Thus, establishing a principle for selecting pruning criteria suited to different deployment objectives remains an important yet largely underexplored problem in one-shot expert pruning. To this end, we introduce a unified formulation for one-shot MoE expert pruning organized around three factors: routing frequency, gate weighting, and activation strength. The formulation yields a criteria selection principle: task-agnostic pruning should favor routed-token-averaged, gate-free activation-based criteria, whereas task-specific pruning can benefit from retaining routing-frequency and gate-weight information. Beyond this principle, the formulation also provides a systematic view of existing heuristic criteria and gives rise to two new task-agnostic criteria, Mean Activation Norm (MAN) and Mean Squared Activation Norm (MSAN). Across four representative MoE models and 16 diverse benchmarks, MAN and MSAN are consistently strong in the task-agnostic setting, obtain the top-two average ranks, and improve average performance by up to 8.8 points over the strongest baseline.

---


### 109. [Vernier: Probing Representational Misalignment Behind Lexical Gaps in Causal Reasoning](https://arxiv.org/abs/2606.15733)

**<font color=#1a73e8>作者：</font>** Zhenyu Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction-tuned language models can answer the same causal-reasoning question differently after its English variable names are replaced by type-preserving placeholders, although the structural causal model and the gold answer are unchanged. We ask whether this lexical gap reflects information loss in the placeholder view or a misaligned read-out from a representation that still carries answer-relevant content. Vernier uses a paired-view weight update as an instrument and then inspects the mechanism left after the gap closes. In the working regimes, the evidence favours representational misalignment. A variable-name probe becomes more accurate on the placeholder view, and activation patching on Qwen-7B, Qwen-14B, and Llama-3.1-8B shows that the decision-token representation can transfer answer identity between views. The update that realigns the views is counterfactual augmentation over original and placeholder prompts, while the answer-subspace KL mainly sharpens intermediate answer-belief agreement. Success is bounded by model family, scale, and task. CRASS transfer is reliable across Qwen scales and Llama, e-CARE remains weak, and preliminary non-causal rename tasks show a similar qualitative pattern.

---


### 110. [Retrievable Gradients: Continual Post-Training Without Cumulative Weight Drift](https://arxiv.org/abs/2606.15734)

**<font color=#1a73e8>作者：</font>** Weihang Su, Jiacheng Kang, Jingyan Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual post-training enables models to absorb emerging knowledge after deployment, but repeatedly updating shared parameters can accumulate weight drift, potentially causing catastrophic forgetting and degrading general capabilities. Retrieval-augmented generation avoids such parameter drift, yet often lacks the depth of parametric knowledge integration. In this paper, we propose ReGrad (Retrievable Gradients), a new paradigm that treats gradients as retrievable units of knowledge. ReGrad pre-computes document-specific gradients offline, stores them in an indexed Gradient Bank, and retrieves only query-relevant gradients at inference time for temporary weight adaptation. However, raw language-modeling gradients are optimized for token-level document reconstruction rather than for query-driven knowledge use. We therefore introduce a bi-level meta-learning objective that reshapes document-derived gradients into generalizable adaptation signals for downstream tasks. Experiments across general and domain-specific settings show that \textsc{ReGrad} outperforms CPT and RAG baselines, enabling scalable and reversible parametric knowledge injection without accumulating weight drift.

---


### 111. [Unsupervised Learning for Missing Modalities in Multimodal Learning](https://arxiv.org/abs/2606.15743)

**<font color=#1a73e8>作者：</font>** Hassan Ismkhan, Hamid Bouchahcia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper addresses the missing-modality challenge in multi-modal learning by introducing Unsupervised Learning for Missing Modalities in Multi-Modal Learning (UL4M4), a flexible framework that imputes missing feature embeddings in a task-independent manner before supervised prediction. We propose modality-specific
normalization and a novel partial-modality distance metric to enable fair clustering of incomplete observations, capturing cross-modal structures while preserving scale-invariance across varying dimensionalities and modality counts. Cluster centers from this unsupervised stage guide an iterative greedy imputation process for any
missing modalities during training or inference, supporting arbitrary numbers of modalities and arbitrary missing patterns per sample. The imputation module is lightweight, uses frozen encoders, and decouples from the downstream task, allowing easy integration with any fusion/prediction architecture. Extensive experiments under diverse and highly incomplete regimes demonstrate UL4M4's robustness, achieving, to
the best of our knowledge, the first consistent F1-Micro scores above 0.7 on challenging missing configurations even when more than 50\% of modality slots are missing. Results are also stable across cluster sizes and significantly outperform state-of-the-art baselines. Code is available here: this https URL.

---


### 112. [OmniTraffic: A Controllable Generation Pipeline and Benchmark for Spatio-Temporal Traffic Reasoning](https://arxiv.org/abs/2606.15749)

**<font color=#1a73e8>作者：</font>** Maonan Wang, Zhengyan Huang, Kemou Jiang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic scene understanding requires models to reason beyond object recognition, including lane topology, multi-view geometry, temporal evolution, and signal-phase semantics. However, existing traffic-oriented multimodal benchmarks largely emphasize passive visual recognition or isolated video understanding, offering limited support for evaluating structure-aware traffic reasoning under controlled conditions. We introduce OmniTraffic, a controllable generation pipeline and benchmark for spatio-temporal traffic reasoning. Built around 12 real-world intersections reconstructed into editable 3D traffic environments and complemented by surveillance footage from two countries, OmniTraffic supports both controlled and natural-condition evaluation. It defines a three-level task hierarchy spanning scene perception, multi-view and temporal reasoning, and decision support. Using structured traffic metadata, OmniTraffic generates synchronized multi-view VQA samples covering vehicle states, lane functions, view--BEV correspondence, temporal dynamics, and signal-phase analysis, resulting in 8M VQA samples and a 3K human-verified test set. Evaluation of eleven frontier MLLMs reveals a large human--model gap, with the most pronounced failures in topology-grounded and spatio-temporal reasoning tasks. Fine-tuning a lightweight MLLM on simulated OmniTraffic data further improves performance on real-world traffic scenes, demonstrating the value of simulation-generated supervision for traffic-specific multimodal reasoning. Beyond a fixed dataset, OmniTraffic provides an extensible pipeline with configurable intersections, camera views, traffic demands, signal phases, visual conditions, and rare events.

---


### 113. [RoboPIN: Grounded Embodied Reasoning via Pinned Chain-of-Thought](https://arxiv.org/abs/2606.15753)

**<font color=#1a73e8>作者：</font>** Yaoting Huang, Yifu Yuan, Linqi Han 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied reasoning requires models to perceive task-relevant objects and spaces in physical environments and maintain consistent visual grounding throughout multi-step reasoning. However, current vision-language models rely on text-only or coordinate-augmented chain-of-thought, where entity references remain implicit and ambiguous. This may cause the reasoning process to decouple from visual evidence, entity references to drift across steps, and a causal disconnection between the reasoning trajectory and the final answer, with these problems further amplified in multi-view scenarios due to cross-view appearance changes. To address these issues, we propose Pinned Chain-of-Thought (\pincot{}), a structured reasoning paradigm that pins every reasoning step to visual evidence. \pincot{} introduces the concept of \reasoninganchor{}, which binds each task-relevant entity to a structured visual anchor with entity name, unique identity, view index, and spatial grounding, enabling consistent entity tracking across reasoning steps and views. We build a fully automated data generation pipeline to construct \dataset{}, a high-quality \pincot{}-formatted reasoning dataset. We then train \method{} through three-stage post-training that progressively injects embodied knowledge, structured reasoning ability, and process-supervised alignment, with rewards that directly constrain both anchor localization and identity consistency during reasoning. On 14 benchmarks covering embodied spatial reasoning, multi-view reasoning, and pointing, \method{} with only 4B parameters consistently outperforms 7B level open-source embodied models, achieving a 12\% average improvement over the strongest 7B baseline, Mimo-Embodied. Further analysis shows that \pincot{} improves grounding accuracy and cross-step identity consistency, validating the effectiveness of process supervision.

---


### 114. [Task-Instructed Causal Routing of Vision Foundation Models for Multi-Task Learning](https://arxiv.org/abs/2606.15765)

**<font color=#1a73e8>作者：</font>** Donghyun Han, Yuseok Bae, Jung Uk Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models (VFMs) have demonstrated strong robustness and transferability across a wide range of visual tasks. However, each model typically encodes strong inductive biases shaped by its pre-training objective and data domain, resulting in fragmented yet complementary visual knowledge. As a result, a single model often struggles to capture the diverse visual representations required across multiple dense prediction tasks. To address this limitation, we propose TIGER (Task-Instruction-Guided Expert Routing), a framework that coordinates multiple heterogeneous VFMs for multi-task dense prediction. Instead of naively aggregating expert features, TIGER leverages natural-language task instructions to guide a routing network that assigns token-level expert weights conditioned on task semantics, enabling adaptive integration of complementary expert features. TIGER further introduces a counterfactual loss that aligns routing decisions with each expert's causal contribution by measuring prediction changes when experts are excluded, encouraging more reliable and interpretable routing. We evaluate TIGER on two multi-task dense prediction benchmarks, NYUD-v2 and Pascal Context, where it consistently outperforms recent multi-task learning baselines while keeping all VFMs frozen. These results demonstrate that combining instruction-guided expert routing with counterfactual causal alignment enables effective coordination of heterogeneous vision foundation models.

---


### 115. [Rethinking Scaffolding in LLM Tutors: The Interactional Mismatch Between Benchmarks and Real-World Deployments](https://arxiv.org/abs/2606.15766)

**<font color=#1a73e8>作者：</font>** Alexandra Neagu, Jeffrey T. H. Wong, Marcus Messer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A central pedagogical value evaluated in AI tutor benchmarks is scaffolding: guiding students through graduated steps toward a solution. Alignment and evaluation methods for embedding scaffolding behaviour into chatbots, however, rest on an implicit assumption: that students will take up the scaffolding and engage in the conversation. To examine whether this assumption holds, we introduce an evaluation pipeline around two metrics - Chatbot Scaffolding and Student Uptake - and apply them across nine datasets of 9,490 chats, spanning AI tutor benchmarks and real-world deployments of educational chatbots. Our analysis reveals that while benchmarks assume a high-scaffolding, high-student-uptake environment, students in real-world settings exhibit lower levels of uptake overall - frequently bypassing the chatbot's pedagogical framing to drive the interaction toward their own learning goals at little interpersonal cost. We argue that bypassing scaffolding is not necessarily detrimental; rather, it frequently highlights a mismatch between a chatbot's pedagogical framing and the student's learning goals. To meaningfully evaluate the effectiveness of a chatbot's assistance, future benchmarks must move beyond the assumption that students will simply take up the scaffolding, and instead evaluate how these chatbots navigate diverse learning contexts and student-driven interaction patterns.

---


### 116. [ttda704 at SemEval-2026 Task 6: Structured Chain-of-Thought Prompting for Political Evasion Detection](https://arxiv.org/abs/2606.15770)

**<font color=#1a73e8>作者：</font>** Tai Tran Tan, An Dinh Thien  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes our system for SemEval-2026 Task 6, which addresses the classification of political evasion strategies in English question-answer pairs extracted from U.S. presidential interviews. We systematically compare two distinct paradigms: (1) Parameter-Efficient Fine-Tuning of Qwen3 models (4B-32B) using QLoRA, enhanced with tiered upsampling and weighted cross-entropy loss to address severe class imbalance, and (2) structured Chain-of-Thought (CoT) prompting of reasoning-capable API models, namely DeepSeek-V3.2 and Grok-4-Fast. Our evaluation demonstrates that structured CoT prompting of reasoning-enabled models substantially outperforms our baseline parameter-efficient fine-tuning implementation in absolute Macro F1. Our best system, Grok-4-Fast with extended reasoning and few-shot hierarchical CoT prompting, achieves a Macro F1 of 0.5147 on Subtask 2 (9-class evasion) and 0.7979 on Subtask 1 (3-class clarity), ranking 8th out of 33 teams on Subtask 2 and 13th out of 41 teams on Subtask 1 on the official leaderboard. Furthermore, our ablation studies reveal key insights into effective prompt design for evasion detection: presenting labels within a hierarchical taxonomy helps structure model reasoning, while few-shot exemplars provide task calibration. However, the strongest prompt variants are not statistically distinguishable in Macro F1, and explicitly enabling extended reasoning modes yields substantial performance gains by facilitating the multi-step pragmatic analysis required to detect evasive intent.

---


### 117. [DYNA : Dynamic Episodic Memory Networks for Augmenting Large Language Models with Temporal Knowledge Graphs in Continuous Learning](https://arxiv.org/abs/2606.15778)

**<font color=#1a73e8>作者：</font>** Ali Sarabadani, Mahtab Tajvidiyan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) struggle to incorporate new knowledge without forgetting or costly retraining. We propose DYNA, a lightweight framework that augments a frozen LLM with a temporal knowledge graph where events are nodes and temporal relations are directed, timestamped edges. The graph serves as an external, updatable memory. At query time, DYNA retrieves relevant nodes via random walks and centrality measures, then augments the LLM's response. Evaluated on three temporal recall tasks, DYNA reduces catastrophic forgetting by ~7% compared to fine-tuning and improves temporal ordering by ~5% over standard RAG. Higher graph clustering coefficients correlate with better retrieval, showing that graph structure matters. Contributions: (1) episodic memory as temporal KG, (2) retraining-free LLM augmentation, (3) graph properties as predictors of retrieval performance.

---


### 118. [Mitigating Visual Hallucinations in Multimodal Systems through Retrieval-Augmented Reliability-Aware Inference](https://arxiv.org/abs/2606.15782)

**<font color=#1a73e8>作者：</font>** Pratheswaran Hariharan, Haiping Xu, Donghui Yan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have demonstrated strong capabilities in vision-language understanding and natural-language response generation. However, these systems can still produce overconfident predictions and hallucination-like outputs, particularly when the visual evidence is weak, ambiguous, or semantically inconsistent. Most existing approaches focus on improving multimodal representation alignment or retrieval-augmented generation, while providing limited mechanisms to quantify instance-level prediction reliability or identify incorrect visual outputs. This work proposes a retrieval-augmented reliability-aware inference framework for trustworthy multimodal visual understanding. The proposed framework constructs an external visual evidence database using pretrained visual embeddings and nearest-neighbor retrieval over normalized feature representations. Retrieved evidence is used to estimate prediction trustworthiness through multiple reliability indicators, including similarity strength, class-support agreement, evidence margin, entropy-based uncertainty, and an aggregate reliability score. Based on these signals, a decision gate determines whether the system should accept the prediction, answer with caution, or abstain/fallback when evidence is insufficient. A multimodal response-generation layer then produces a final user-facing response conditioned on the reliability decision. Experiments on ImageNet-100 demonstrate that the proposed reliability-aware framework improves accepted prediction accuracy from 85.84\% to 88.88\% at 89.04\% coverage. The hallucination-like accepted wrong-answer rate is reduced from 14.16\% to 11.12\%. These results show that integrating retrieval evidence, reliability estimation, and selective decision gating can improve calibration and reduce overconfident visual errors without retraining large multimodal models.

---


### 119. [ttda704 at SemEval-2026 Task 4: Modeling Narrative Structures via Pseudonymization and Multi-View Sentence Alignment](https://arxiv.org/abs/2606.15783)

**<font color=#1a73e8>作者：</font>** Tai Tran Tan, An Dinh Thien  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present our approach to SemEval 2026 Task 4: Narrative Story Similarity and Narrative Representation Learning. Our solution uses contrastive learning with fine-tuned sentence transformers to capture narrative similarity across abstract themes, course of action, and outcomes. We develop two pipelines: (Track A) a single-view method that encodes full narratives with smart layer freezing to reduce overfitting, and (Track B) a multi-view method that models theme, plot, and outcome with view-specific projection heads and self-supervised alignment. Both pipelines build on sentence-transformers models and are trained with contrastive loss on synthetic data. The code is available at the following GitHub repository: this https URL.

---


### 120. [Mean-Field Parallel Decoding for Discrete Diffusion Language Models](https://arxiv.org/abs/2606.15805)

**<font color=#1a73e8>作者：</font>** Tamim Zoabi, Ameen Ali, Liran Ringel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language models enable parallel token generation, offering a pathway to low-latency decoding. However, selecting tokens independently by marginal confidence limits effective parallelism: tokens that appear reliable in isolation can form incompatible configurations when several positions are updated at once. We introduce a training-free decoding framework that coordinates these parallel updates. At each forward pass, the method assigns a commit score to each masked position and refines these scores using pairwise interactions derived from the model's predictive distributions. A variational relaxation yields a simple fixed-point update that suppresses conflicting simultaneous commitments within a single forward pass. This mechanism allows the decoder to commit more tokens in parallel while maintaining competitive generation quality. The method is lightweight, requires no auxiliary model or retraining, and drops into existing diffusion decoding pipelines without modification. Experiments on reasoning and code-generation benchmarks show consistent improvements in the quality-latency trade-off.

---


### 121. [The Truth Stays in the Family: Enhancing Contextual Grounding via Inherited Truthful Heads in Model Lineages](https://arxiv.org/abs/2606.15821)

**<font color=#1a73e8>作者：</font>** Miso Choi, Seonga Choi, Mincheol Kwon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have produced many specialized multimodal LLMs (MLLMs) that share common foundational LLMs, forming distinct model lineages. It remains unclear whether a fundamental behavioral link exists between the foundational LLMs and downstream variants. We investigate this question by quantifying head-level context-truthfulness scores. Across diverse LLM and MLLM lineages, including Vicuna-, Qwen2.5-, LLaMA2-, and Mistral-based models, we find that Truth Scores are strongly preserved within model families, even after instruction tuning or multimodal adaptation. We further show that this inheritance is consistent with attention-head weight preservation, and that context-truthful heads attend to query-relevant evidence. Building on this finding, we propose TruthProbe, a soft-gating strategy that amplifies context-truthful heads while preserving other head contributions. TruthProbe improves contextual truthfulness on HaluEval and reduces multimodal hallucination on POPE and CHAIR, with base-LLM Truth Scores transferring effectively to their fine-tuned LLM and MLLM descendants. Code is available at this https URL.

---


### 122. [TrustedARI: Towards Trust-Native Agentic Routing Infrastructure for Agentic AI](https://arxiv.org/abs/2606.15822)

**<font color=#1a73e8>作者：</font>** Qi Li, Zhenhua Zou, Shuo Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly access external models, tools, and services through Agentic Routing Infrastructure (ARI) to manage the overhead of heterogeneous interfaces and fragmented subscriptions. Yet, the architecture of ARI introduces fundamental trust risks: it obtains plaintext access to agent queries and service responses, while leaving agents unable to verify that their queries are routed to intended service providers or that requests and responses remain untampered. To address this problem, we present TrustedARI, the first trust-native agentic routing infrastructure for agentic AI. Architecturally, TrustedARI is built upon three core innovations: (i) an ARI-adapted three-party TLS handshake that enables the agent and ARI to jointly authenticate the service provider through role-specific distribution of TLS key materials; (ii) a privacy-preserving query-construction protocol that allows the agent and ARI to collaboratively construct well-formed queries without exposing their respective private inputs; and (iii) a verifiable billing protocol that supports fair usage-based settlement while preserving the integrity and confidentiality of service responses.
We implemented and extensively evaluated a prototype of TrustedARI to validate its performance. Experiments confirm that TrustedARI is highly efficient: our ARI-adapted handshake protocol reduces communication overhead by 39.34% compared to the existing three-party TLS handshake. Furthermore, the privacy-preserving query-construction protocol imposes negligible overhead-averaging 0.19 seconds in computation time and 0.58 MB in communication costs-while the verifiable billing protocol speeds up proof generation by 28.20x. Crucially, TrustedARI is readily deployable without any modification to the service providers.

---


### 123. [Heteroskedastic Signals in Budgeted LLM Verification: Structural Heterogeneity Limits Optimization Gains](https://arxiv.org/abs/2606.15841)

**<font color=#1a73e8>作者：</font>** Jinlong Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) systems increasingly use uncertainty signals to allocate limited computation across verification, test-time scaling, tool execution, and other selective-compute decisions. Such policies rely on a \emph{global signal comparability assumption}: equal scores should carry comparable decision value across inputs. Using budgeted verification as a controlled diagnostic setting, we identify a failure mode of this assumption: uncertainty quality is heteroskedastic across cost strata, with some regions exhibiting near-random discriminability despite concentrating many errors. Under an explicit local model, we characterize the resulting distortion of global allocation and show that its upper bound scales with cross-stratum signal-quality dispersion. We separate weak signals, optimization instability, and structural heterogeneity through a controlled intervention hierarchy: Threshold, MP-Adapt, MP-Strat, and a deliberately simple cost-stratified thresholding intervention (CST). Across MBPP and MATH using Qwen3-8B, LLaMA3-8B, and GPT-4o-mini, global online adaptation yields inconsistent gains over static thresholding; MP-Strat partially recovers performance, while CST improves hit rate by up to 17 percentage points in strongly heterogeneous settings without gradient updates. These results identify structural heterogeneity, rather than optimizer weakness alone, as the primary bottleneck in the observed settings. More broadly, misaligned feedback structure cannot always be repaired by stronger optimization.

---


### 124. [RetailBench: Benchmarking long horizon reasoning and coherent decision making of LLM agents in realistic retail environments](https://arxiv.org/abs/2606.15862)

**<font color=#1a73e8>作者：</font>** Linghua Zhang, Jun Wang, Jingtong Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have made rapid progress on short-horizon, well-scoped tasks, yet their ability to sustain coherent decisions in dynamic long-horizon environments remains uncertain. We introduce RetailBench, a data-grounded simulation benchmark for evaluating tool-using LLM agents in single-store supermarket operation. RetailBench models retail management as a partially observable decision process and is designed to support thousand-day-scale simulations. In this environment, agents must manage pricing, replenishment, supplier selection, shelf assortment, inventory aging, customer feedback, external events, and cash-flow constraints. We evaluate seven contemporary LLMs under representative agent frameworks over a 180-day evaluation horizon and compare them with a privileged oracle policy. Results show substantial variation across models: only a small subset survives the full evaluation horizon, and even the strongest LLM runs remain substantially behind the oracle policy in final net worth and sales outcomes. Behavioral analysis attributes these gaps to incomplete evidence acquisition, surface-level decision making, and the lack of a consistent long-horizon policy. RetailBench provides a controlled testbed for studying reliable autonomy in economically grounded long-horizon decision-making.

---


### 125. [David vs. Goliath in Next Activity Prediction: Argmax vs. LSTM, Transformer, and LLM](https://arxiv.org/abs/2606.15868)

**<font color=#1a73e8>作者：</font>** Hans Weytjens, Ingo Weber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Next activity prediction (NAP) is a cornerstone of predictive process monitoring (PPM), enabling organizations to move from retrospective analysis to proactive process steering. The PPM field has progressed from classical machine learning through deep learning architectures such as LSTMs and Transformers to large language models (LLMs). Despite growing model complexity, no benchmark jointly compares LLMs, Transformers, LSTMs, and simple baselines in a direct sequence modeling setting for NAP. In this paper, we fill this gap with a systematic benchmark. We compare vocabulary-adapted LLMs, Transformers trained from scratch, LLM-distilled Transformers, and LSTMs against a simple counting-based argmax baseline across seven real-life event logs. Our results tell a David vs. Goliath story: pretraining confers no consistent improvement over training from scratch, model size shows little effect on performance, and on most datasets the argmax baseline matches or approaches the performance of billion-parameter LLMs.

---


### 126. [SciOrch: Learning to Orchestrate Expert LLMs for Solving Frontier Multimodal Scientific Reasoning Tasks](https://arxiv.org/abs/2606.15872)

**<font color=#1a73e8>作者：</font>** Jingru Guo, Xiangyuan Xue, Lian Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier scientific reasoning remains a major challenge for large language models (LLMs), where even the strongest commercial systems fall short of expert-level performance. A closer look at model behavior reveals substantial complementarity that single-model evaluation hides: different frontier models excel on different question types, and no single model captures the full picture. We present SciOrch, a framework that trains a lightweight 8B model to orchestrate frontier LLMs for scientific reasoning. The orchestrator decomposes each question, delegates sub-problems to selected commercial models through API calls, and synthesizes a final answer. Training such an orchestrator is fundamentally harder than conventional agentic RL: each action triggers an API call that is expensive in both dollar cost and latency, making standard online rollouts infeasible. We address this with MCTS-based approach, producing diverse orchestration trajectories, extracting per-node single-turn samples, and optimizing the orchestrator with GRPO-style training. On a 240-question test set spanning SGI-Reasoning and Scientists' First Exam, SciOrch reaches 56.66% average accuracy, outperforming the strongest single commercial model by 3.74% and the strongest multi-agent baseline by 3.33%. It also attains the best accuracy on both SGI and SFE with less than half the API cost of typical multi-agent methods.

---


### 127. [LLM-as-Code Agentic Programming for Agent Harness](https://arxiv.org/abs/2606.15874)

**<font color=#1a73e8>作者：</font>** Junjia Qi, Zichuan Fu, Jingtong Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every major LLM agent framework gives the LLM the role of orchestrator; the model decides what to do next, when to call tools, and when to stop. We argue that token explosion, control-flow hallucination, and unreliable completion are not implementation bugs but architectural consequences of assigning the deterministic work of looping, branching, and sequencing to a probabilistic system. A better prompt or a stronger model cannot guarantee the reliability of the LLM agent. We therefore propose Agentic Programming, in which the program governs all control flow, and the LLM is itself part of it, an adaptive component we call LLM-as-Code and invoke only where a task calls for reasoning or generation. Within each call the model keeps full flexibility, but it cannot alter the program's execution path. With control in the program, the LLM's context is built from the execution history's call tree and forms a directed acyclic graph (DAG). Each call's context length is then determined by its call depth rather than by accumulation over steps. A case study of computer-use agents shows that the design is practical, not just a theoretical stance, substantially improving the stability of long visual operation sequences.

---


### 128. [Deep Residual Injection for Full-Spectrum Forensic Signal Perception in Multimodal Large Language Models](https://arxiv.org/abs/2606.15880)

**<font color=#1a73e8>作者：</font>** Kaiqing Lin, Zhiyuan Yan, Ruoxin Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have been increasingly adopted in forensics for their robust semantic understanding. As AI-generated images become realistic, semantic-level inconsistencies alone are often insufficient for reliable detection. This motivates a critical question: whether MLLMs can achieve full-spectrum forensic signal perception, i.e., capturing low-level generator artifacts without sacrificing pre-trained semantic knowledge. We further perform a layer-wise analysis of forensic signal perception in MLLMs, showing that semantic information is primarily formed in the early-to-middle layers, whereas direct fine-tuning for artifact learning disrupts these semantic representations. Based on this insight, we propose Deep Visual Residual MLLM (Deep-VRM) to preserve early semantic processing while injecting artifact-specific visual signals as a residual path into an intermediate layer, where they are fused with semantic token representations and propagated through subsequent trainable layers. This enables later layers to jointly model semantic reasoning and signal-level forensic cues, and surprisingly, the model learns to adaptively leverage different levels of forensic signals depending on the input, achieving robust and generalizable detection performance. Extensive experiments show that our method achieves state-of-the-art across most benchmarks. The code and data are available at this https URL.

---


### 129. [Neuron Level Analysis of Large Language Model in Legal Domain Reasoning](https://arxiv.org/abs/2606.15884)

**<font color=#1a73e8>作者：</font>** Eri Onami, Youmi Ma, Shuhei Kurita 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We presented a neuron-level analysis of legal-domain reasoning in LLMs, comparing it with other applied domain tasks across seven open-weight models. Using neuron attribution scores to rank and suppress influential neurons, we confirmed that suppressing the identified neurons collapses accuracy on the target task, whereas suppressing the same number of random neurons does not. We further found a small subset of neurons influential across all seven tasks; once these are removed, suppressing the remaining neurons degrades only the task they were identified from, revealing genuinely task-specific neurons in every model studied. Within the legal domain, the three benchmarks exhibit relatively high neuron overlap and tend to be affected jointly, suggesting of legal components neurons that span jurisdictions. The distribution of identified neurons in our experiments suggests that the hypothesis that influential neurons are concentrated in middle MLP layers may depend on the input format and content, rather than being a universal phenomenon.

---


### 130. [Intelligence Is Not the Bottleneck: Validating an LLM First-Pass Manuscript Score Against Peer-Review Outcomes](https://arxiv.org/abs/2606.15887)

**<font color=#1a73e8>作者：</font>** Costa Georgantas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) systems are increasingly proposed to assist peer review, yet most evaluations judge the prose of machine-generated review text, not the validity of the numeric score a system assigns. We validate AIPR, which reads a submitted manuscript and emits five 0-100 quality dimensions and a weighted overall score, against the public decision outcomes of a major machine learning venue. AIPR grades by prompting alone, with no fine-tuning on reviews or decisions. Across 300 ICLR submissions with public decision tiers and reviewer ratings, graded under a frozen pipeline with hypotheses pre-registered before any score met any outcome, the overall score separates rejected from accepted submissions (AUROC 0.82, 95% CI 0.78-0.87), rises monotonically across tiers, and tracks the mean reviewer rating. The signal is strongest where we claim it: the lowest-scoring fifth is rejected far above the base rate, with oral papers absent. The validity comes mostly from the model: a one-paragraph prompt on the same model discriminates almost as well as the full pipeline (the small gap favours the pipeline but does not meet the pre-declared criterion, p = 0.09). What the engineering adds is reliability and a grounded review: AIPR's score barely moves across repeated runs (0.7 vs. 2.8 points within-paper SD) where the bare prompt swings, and the same pass returns a rubric-structured, evidence-grounded review rather than a bare number, with the human keeping the decision.

---


### 131. [UrbanWell: Benchmarking Multimodal Large Language Models for Spatio-Temporal Urban Wellbeing Analytics](https://arxiv.org/abs/2606.15890)

**<font color=#1a73e8>作者：</font>** Yanxin Xi, Xiang Su, Jie Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding urban wellbeing from multimodal data requires integrating heterogeneous spatial and temporal signals, posing significant challenges for current multimodal large language models (MLLMs). We introduce UrbanWell, a large-scale benchmark designed to systematically evaluate the spatio-temporal reasoning capabilities of MLLMs for urban wellbeing analytics through joint modeling of satellite and street view imagery. UrbanWell spans 38 cities across multiple years and includes diverse indicators covering (1) environmental conditions (CO$_2$, NO$_2$, PM${2.5}$, and Normalized Difference Vegetation Index), (2) spatial accessibility (minimum distance to supermarkets and restaurants), (3) urban form (road length, road density, and land use), (4) urban vitality (population, economic activity diversity, and land use diversity), and (5) subjective perception attributes (e.g., safety, beauty, liveliness, wealth, and quietness). All indicators are aligned at grid level to enable standardized evaluation. Beyond static prediction, UrbanWell defines temporal reasoning tasks, including future value forecasting from historical observations and temporal trend classification. We benchmark 15 state-of-the-art representative MLLMs in a zero-shot setting, providing a comprehensive comparative evaluation across spatial and temporal dimensions. Experimental results indicate that while MLLMs capture salient spatial and perceptual cues, their performance varies substantially across heterogeneous urban indicators spanning environment and subjective perception. UrbanWell serves as a unified benchmark for evaluating multimodal spatial and temporal reasoning in urban wellbeing analytics, offering a standardized testbed for systematic assessment and future research on multimodal urban intelligence. Our codes and datasets are accessible via this https URL.

---


### 132. [BALTO: Balanced Token-Level Policy Optimization for Hallucination Mitigation](https://arxiv.org/abs/2606.15893)

**<font color=#1a73e8>作者：</font>** Ning Li, Zixuan Guo, Yan Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucinations remain a major obstacle to deploying large language models (LLMs) in knowledge-intensive settings, where generated responses must be faithfully grounded in provided evidence. Reinforcement learning (RL) is a promising direction for hallucination mitigation, but response-level faithfulness rewards suffer from a granularity mismatch: localized hallucinations can cause supported content to receive spurious penalties. Although recent work introduces fine-grained feedback such as claim-level verification and token-level rewards, unbalanced credit assignment can still induce length, verbosity, or optimization-noise biases. We propose BALTO, a Balanced Token-level Policy Optimization framework for hallucination mitigation. BALTO extracts checkable factual claims, verifies them against the reference context, and projects claim-level judgments to token-level labels. A balanced token-level credit assignment mechanism is introduced into the framework. This design redistributes probability mass from unsupported content toward faithful content, rather than suppressing the entire response. We systematically analyze the limitations of response-level rewards from a theoretical standpoint, and prove BALTO's advantages in training stability and optimization efficiency for hallucination mitigation. Experiments on ConFiQA, RAGTruth, and FinLLM-Eval show that BALTO achieves the highest faithfulness across all six model--benchmark settings and consistently outperforms existing post-training baselines in Q-Score, demonstrating a stronger faithfulness--informativeness trade-off.

---


### 133. [Calibrated Triage, Not Autonomy: Confidence Estimation for Medical Vision-Language Models](https://arxiv.org/abs/2606.15910)

**<font color=#1a73e8>作者：</font>** Reza Khanmohammadi, Kundan Thind, Mohammad M. Ghassemi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A vision-language model can answer a question about a medical image fluently and confidently while barely using the image, leaning instead on language priors. In medicine this is the failure that matters most, because the answer looks trustworthy and is not, and the only protection is a confidence score reliable enough to tell the system when to abstain. We ask a deployment question rather than an accuracy one: how much imaging work a model can safely handle alone, and which confidence signal makes that possible. We evaluate seven confidence estimators across five open-weight LVLMs and three medical visual-question-answering datasets spanning broad clinical imaging, radiology, and pathology, with every probe trained only on natural images and applied without adaptation. Recast as bounded selective prediction (automate a case only when confidence clears a threshold, defer the rest), the comparison is cautionary. The standard metrics are poor guides: discrimination barely separates the methods, and the weak calibration of a cheap self-report is cheaply removed by off-domain temperature scaling without changing deployable yield. What distinguishes a usable estimator is the high-confidence region a clinician acts on: the weakest baselines are confidently wrong on 41 to 45 percent of their errors against 1 to 4 percent for the best probe, and no estimator is reliably best across domains or models. Safe handoff is governed at two levels: base-model competence sets a ceiling, so a well-calibrated score recovers roughly a third of radiology cases at a 20 percent error tolerance but almost none of pathology; the confidence layer then decides how much of that ceiling is reachable. The usable role today is calibrated triage, not autonomy: automate the cases a calibrated score marks safe, route the rest to a clinician. We release all outputs, correctness judgments, and confidence scores, with code.

---


### 134. [Interactor: Agentic RL oriented Iterative Creation for Ad Description Generation in Sponsored Search](https://arxiv.org/abs/2606.15911)

**<font color=#1a73e8>作者：</font>** Penghui Wei, Jiayu Wu, Chao Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper focuses on automatically generating informative ad descriptions in sponsored search. Unlike ad titles which are usually optimized to attract user click feedbacks, ad descriptions have a longer text span and possess the potential of incorporating world knowledge to address user search intents while presenting the fine-grained selling points of the ads. We propose Interactor, a multi-turn iterative creation framework optimized with agentic RL for ad description generation. The generation model acts as a policy that interacts with a customized environment consisting of multiple generative reward models. Given initial generations by the policy, the customized GenRMs evaluate multi-dimensional qualities including knowledge capacity and landing page consistency, providing both binary signals and reasoning feedbacks. The policy then iteratively refines the descriptions based on such feedbacks to ensure continuous improvement. Experiments on industrial datasets show that the Interactor framework significantly outperforms state-of-the-art approaches in generating knowledge-rich and faithful ad descriptions. Since May 2026, it has been deployed online in a leading search ads system, contributing to both ad revenue and user experience.

---


### 135. [Contaminated Collaboration: Measuring Gender Bias Transfer in LLM-Assisted Student Writing](https://arxiv.org/abs/2606.15914)

**<font color=#1a73e8>作者：</font>** Ariyan Hossain, Kazi Kamruzzaman Rabbi, Farig Sadeque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gender bias in LLMs has been studied extensively in model outputs, with biased prompts shown to amplify stereotyped generations. Whether such bias propagates into text produced by humans who use these systems, however, remains underexplored. We investigate whether gender bias in an LLM writing assistant transfers into career plan essays written by students. We first verify that a gender-biased prompt induces gender-differentiated language in LLM-generated essays, while a neutral prompt does not. We then recruited participants (N = 123) in a controlled environment to write career plan essays for paired biographical profiles differing only in gender under three conditions: no AI assistance, neutral LLM assistance, or gender-biased LLM assistance. Students in the biased condition produced essays with a significantly larger agentic gap and more gender-stereotypic occupation suggestions than those in the control and neutral conditions. Our results also reveal that this bias transfer is asymmetric: agency is suppressed in female-target essays while male-target writing remains largely unaffected. Our findings highlight the risk of bias propagation in AI-assisted writing, calling for fairness-aware design in educational AI tools.

---


### 136. [Reinforcement Learning for LLM-based Event Forecasting](https://arxiv.org/abs/2606.15917)

**<font color=#1a73e8>作者：</font>** Amit Arnold Levy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We use Group Relative Policy Optimization (GRPO), a recently devised sample and memory efficient reinforcement learning method, to finetune pretrained LLMs in the range of 1.5B to 14B parameters equipped with the ability to get current information through the use of a Wikipedia revisions tool, or news summaries, to forecast real events beyond the knowledge cutoff of the LLM, as well as problems made to simulate different aspects of the dynamics of that training.
We use the results of these experiments to comment on the scaling capability of LLMs for forecasting, as well as classify how judgmental forecasting fits into the verifiable/unverifiable domain taxonomy, considering the impact of the inherent aleatoric uncertainty when forecasting future events (e.g. the roll of a die).
As a result of the GRPO training, we manage to bring a 1.5B parameter transformer (Qwen 2.5 1.5B) to forecasting performance superior to Claude Sonnet 3.5 over the same dataset as measured by cross entropy from the market agreed probabilities. We also discuss various dead ends on the path to this result.

---


### 137. [Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises?](https://arxiv.org/abs/2606.15919)

**<font color=#1a73e8>作者：</font>** Markos Stamatakis, Omkar Gavali, Joshua Berger 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Chatbots based on large language models (LLMs) are increasingly adopted for information retrieval, text generation, and writing assistance. In educational settings, their use is also rapidly increasing. Students leverage these systems to complete tasks, access information, and support learning. However, the role of LLM-based chatbots in supporting learning and assessment in university-level computer science education is still underexplored. To address this gap, we investigate the performance of several LLM-based chatbots in solving multiple-choice questions (MCQs) at the university level and evaluate their capabilities to assist student learning. We developed 70 MCQs for a university lecture on interactive visual data analysis and evaluated the chatbots' performance using different prompt designs. We further compared the results with students' performance. Finally, we conducted a user study in two lectures (interactive visual data analysis, computer vision) to investigate how chatbot-generated answers and explanations affect students' performance. The chatbot performance showed significant differences between smaller models and GPT-4o and GPT-5 models, which achieved the best results. The results of the user study show that presenting ChatGPT answers together with an explanation does not improve students' performance in general.

---


### 138. [OmniOPSD: Rationale-Privileged On-Policy Self-Distillation for Affective Computing](https://arxiv.org/abs/2606.15920)

**<font color=#1a73e8>作者：</font>** Zebang Cheng, Shuimu Chen, Boxue Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for multimodal large language models (MLLMs) is often hindered by severe reward sparsity in complex reasoning tasks. This challenge is particularly pronounced in human-centered scenarios involving states, emotions, intentions, and behaviors, where heterogeneous multimodal signals and subjective human factors make high-quality chain-of-thought (CoT) annotations expensive and difficult to obtain. Although many multimodal datasets provide expert-annotated ground-truth labels, directly using these labels for supervised fine-tuning may encourage shortcut learning in multimodal perception and provides limited transparency for safety-critical human--AI interaction. To address these limitations, we propose OmniOPSD, a Rationale-Privileged On-Policy Self-Distillation framework that uses frontier-generated rationales as teacher-side privileged evidence rather than student imitation targets. OmniOPSD uses frontier-generated evidence-aware rationales only as training-time privileged evidence context for a local teacher. The student samples its own rollout from the original multimodal input, while the rationale-privileged teacher scores the same tokens and provides dense token-level supervision. Thus, the student learns on its own trajectory distribution without directly imitating frontier-model completions, and inference requires no labels, rationales, CoT annotations, or closed-source model access. Experiments on MER-UniBench show that OmniOPSD achieves state-of-the-art performance with an average score of $84.19$, and ablations further support the value of rationale-privileged teacher guidance.

---


### 139. [Beyond NL2Code: A Structured Survey of Multimodal Code Intelligence](https://arxiv.org/abs/2606.15932)

**<font color=#1a73e8>作者：</font>** Xuanle Zhao, Qiushi Sun, Jingyu Xiao 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While LLMs have substantially advanced text-to-code synthesis, many real programming tasks specify intent through visual artifacts such as screenshots, charts, documents, vector drawings, videos, and interactive states. These tasks require models to connect visual perception to executable programs, because correctness depends not only on syntax but also on layout, geometry, data semantics, editability, interaction behavior, and domain-specific constraints that apply after execution. This survey examines Multimodal Code Intelligence, covering systems that generate, edit, refine, execute, or reason with code under visually grounded inputs and outputs. We first formulate the field by the role that code plays in each task, distinguishing code as a rendered artifact, an editable symbolic structure, a scientific representation, an intermediate reasoning trace, or an executable policy or tool interface. We then organize benchmarks and methods into four domains: Graphical User Interface, Scientific Visualization, Structured Graphics, and Frontier Tasks and Frameworks. This taxonomy connects mature artifact-generation problems to emerging agentic and unified settings and allows us to compare how different tasks treat evidence of correctness. Looking ahead, we argue that future research may benefit from four verification-centered directions. Multi-signal validation can combine complementary evidence of correctness, multi-state verification can test behavior across execution trajectories, cross-task transfer testing can probe reusable visual-code skills, and verifiable agent traces can reveal whether agent actions are grounded in visual evidence. Together, these directions may move multimodal code generation from single-output imitation toward evidence-grounded executable systems.

---


### 140. [SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges](https://arxiv.org/abs/2606.15971)

**<font color=#1a73e8>作者：</font>** Yuchao Wu, Junqin Li, XingCheng Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) offers an effective approach for large language models to access external knowledge. However, existing methods rely on dense similarity retrieval and face inherent limitations in handling structured constraints and multi-hop reasoning. Incorporating knowledge graphs partially alleviates these issues, but at the cost of semantic fragmentation, high maintenance overhead, and difficult incremental updates. This paper introduces SAG (SQLRetrieval Augmented Generation), a structured architecture for retrieval and agent systems. Instead of pre-building a global static graph, SAG converts each chunk into one semantically complete event and a set of indexing entities, then uses SQL join queries to dynamically link events that share entities into local hyperedges,constructing, at query time, a dynamically instantiated local index structure. This design avoids the need for global graph rebuilding and ongoing maintenance; the system naturally supports incremental writes, concurrent processing, and continuous scaling through its reliance on standard database infrastructure. Across HotpotQA, 2WikiMultiHop, and MuSiQue, three standard multi-hop benchmarks,SAG achieves the best results on 8 out of 9 Recall@K metrics, reaching 80.0% Recall@5 on MuSiQue, the benchmark with the highest multi-hop reasoning this http URL has also been deployed at a production scale of hundreds of millions of data items, with online retrieval latency kept within seconds. Project site and code are available at this https URL.

---


### 141. [Formalize Once, Edit the Rest: Efficient Lean-Based Answer Selection for Math Reasoning](https://arxiv.org/abs/2606.15972)

**<font color=#1a73e8>作者：</font>** Ji Feng, Zhouxing Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With large language models (LLMs) increasingly applied to mathematical reasoning, formal proof assistants such as Lean can be leveraged to verify reasoning outputs with machine-checkable rigor, enabling use cases such as answer selection in test-time scaling with K sampled candidate answers. However, employing Lean requires that LLM outputs, originally in natural language, first be formalized. Existing Lean-based answer-selection work uses an autoformalization model to generate a formal statement in Lean for each candidate answer independently, incurring a significant computational cost. We propose BASE, a base-and-edit pipeline that formalizes a single base candidate per problem and derives the remaining K-1 statements by editing the answer expression in place. To facilitate this, we train a rewriter model LEANSCRIBE to localize the answer in the base formalization and generate a reusable edit function for the other K-1 candidates. BASE simultaneously improves selection accuracy and reduces formalization cost - a Pareto improvement that holds on all 12 (dataset, solver) configurations across four benchmarks and three solvers, cutting autoformalizer calls by about 5x at K=8, with the reduction expected to become larger as K grows. Code is available at this https URL.

---


### 142. [A Large-Scale Multi-Dimensional Empirical Study of LLMs for Conversation Summarization](https://arxiv.org/abs/2606.15974)

**<font color=#1a73e8>作者：</font>** Weixiao Zhou, Gengyao Li, Xianfu Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the significant advancement of LLMs in conversation summarization, their evaluation remains limited by insufficient scenarios, input lengths, and sample sizes. Furthermore, existing benchmarks often omit frontier reasoning systems and efficient small models, or lack fine-grained, multi-dimensional assessments. To bridge these gaps, we propose OmniCSEval, a unified benchmark comprising 1,800 diverse conversations across six real-world scenarios, featuring context lengths ranging from 128 to 32k tokens. For fine-grained evaluation, we employ a bidirectional fact-checking framework that integrates key fact matching to assess completeness and conciseness, alongside summary fact verification to evaluate faithfulness. To ensure reliable assessment, we establish a human-LLM collaborative pipeline for key fact extraction and a multi-LLM consensus verifier for summary fact decomposition. Leveraging this framework, we evaluate 28 LLMs across four distinct categories grouped by reasoning capability and model scale. Our extensive empirical study reveals critical insights regarding the cross-scenario challenges current LLMs continue to face, the impacts of reasoning and scale, and the efficiency and adaptability of reasoning models. We also provide guidance for system selection in real-world deployments.

---


### 143. [Agentic Framework for Deep Learning workload migration via In-Context Learning](https://arxiv.org/abs/2606.15994)

**<font color=#1a73e8>作者：</font>** Qiyue Liang, Steven Ingram, George Vanica 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Translating deep learning models from PyTorch's flexible, object-oriented design to JAX's functional, stateless setup is usually a manual and error-prone task. Automated migration is challenging because Large Language Models (LLMs) struggle with strict and dynamic API alignment and are prone to mistakes for exacting operations. We propose a fully autonomous system that combines In-Context Learning (ICL) with oracle-driven self-debugging. First, we curated an ICL context that serves as a strict reference for idiomatic JAX styling and test case generation. Second, instead of depending on the LLM to deduce mathematical outputs, we run the source PyTorch modules to get their actual dynamic tensor states. This creates an unchangeable execution oracle. We then use an autonomous agentic loop to synthesize tests based on the oracle data. The test cases are executed repeatedly, and the traceback is sent back to the LLM for self-correction. Ablations show that combining ICL references with oracle grounding and self-debugging greatly outperforms pure instructional and basic agentic baselines. This improvement does not add an excessive computational overhead. Our lightweight pipeline achieves 91% numerical equivalence (compared to baseline: 9%, instruction + self-debugging: 27%) on neural modules, providing a highly reliable, scalable blueprint for cross-framework migration. This has been validated across several state-of-the-art models including SAM (segment anything), T5, Code Whisper amongst others showing high numerical equivalency. Code: this https URL

---


### 144. [SciText2Eq: Assessing LLMs for Explainable Equation Generation for Scientific Creativity](https://arxiv.org/abs/2606.16003)

**<font color=#1a73e8>作者：</font>** Yifan Mo, Xiao Fu, Yue Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work investigates the ability of large language models (LLMs) to generate mathematical equations from scientific texts. Prior work faces challenges in unstructured grounding, multi-equation dependency, and humanaligned evaluation. To this end, we construct a dataset of AI research papers, pairing contextual passages with ground-truth equations and variable descriptions. We develop an explainable equation generation workflow and evaluate it across diverse open- and closed-source LLM backbones. We introduce an evaluation protocol combining automatic metrics, LLM-based rubrics, and human judgments to assess accuracy, explainability, and human-LLM alignment. Results indicate that LLMs perform moderately on lexical- and syntactic-based similarity, while struggling with semantic accuracy. Comparisons between LLM-based evaluations and human judgments reveal limited alignment, highlighting challenges in using LLMs to assess equation quality. These findings offer insights for improving equation generation models and developing more reliable evaluation methods for scientific text. We provide code and data for reproducibility.

---


### 145. [Who Flips? Self- and Cross-Model Counterarguments Reveal Answer Instability in LLMs](https://arxiv.org/abs/2606.16011)

**<font color=#1a73e8>作者：</font>** Nafiseh Nikeghbal, Amir Hossein Kargaran, Shaghayegh Kolli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard accuracy benchmarks are designed to test how closely large language models (LLMs) approach correct answers, but are not suitable for testing whether LLMs stick with a correct answer when that answer is challenged by a plausible counter-argument. We introduce a controlled protocol for evaluating answer stability: after a model answers a multiple-choice question correctly, we challenge the model's answer with a coherent argument for an incorrect option and measure whether the model flips. The setup a) isolates argumentative content from overt social pressure and b) varies argument length, self-attribution, and cross-model source. Across seven frontier models and 57 MMLU subjects, flip rates range from 17.5% to 97.3%, revealing large differences in stability that are not captured by accuracy metrics alone. We find that self-attribution consistently increases flip rates (mean +7.1pp, up to +18.7pp). Also, pooling wrong-answer arguments across models and selecting the most effective one per question yields stronger adversarial challenges than relying on any single source model. We further construct MaxFlip, a curated challenge set that amplifies flips by up to +23.6pp over standard self-generated challenges. We release the protocol, challenge records, and MaxFlip to support stability evaluation alongside standard accuracy benchmarks. Materials are available at this https URL and this https URL.

---


### 146. [Orchestrated Reality: From Role-Play to Living, Playable Game Worlds -- LLM-Driven World Simulation as a Parameterized-Action POMDP](https://arxiv.org/abs/2606.16014)

**<font color=#1a73e8>作者：</font>** Yuhang Huang, Chenmiao Li, Chaowei Fang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Many games rely on storytelling combined with systems that track levelling, NPC behaviour, and consequence simulation; bridging tightly-authored narrative with deeply-simulated worlds -- most acute in sandbox and open-world settings -- has been prohibitively expensive. LLM-driven worlds open a new path: a single harness can coordinate numerical state, narrative voice, storytelling pacing, and rule logic together. Realising this requires the LLM system to sustain a persistent world (who is where, what has just happened, what is currently true), which today's deployed systems do not: the narrative voice asserts state in free prose without any validated representation, so a fully autonomous game engine remains infeasible. We treat this as an architectural choice, not a limitation of language models, and report work in progress on a framework -- orchestrated reality -- that makes the world a canonical object owned by a singleton orchestration agent analogous to the tabletop-RPG Game Master (GM). We formalise an LLM-driven game world for a human player as a Parameterized-Action POMDP: state is a tree of canonical JSON entities, actions decompose as $a=(k, x_k)$ (a discrete intent kind plus structured JSON parameters), the agent observes only a narrative projection $o=O(s)$ of state, and the transition kernel $F$ is an LLM-driven Plan-Diff-Validate-Apply (PDVA) pipeline that commits schema-validated, content-hashed JSON deltas. We give the formal model, a JSON-state example, a worked single-turn example, and a catalogue of 15 illustrative incidents drawn from a real deployment showing the framework in action. Empirical validation through a planned human player study -- together with multi-NPC concurrent agency and deployment as an RL environment -- is situated as future work.

---


### 147. [Circuit Tracing in Autoregressive Protein Language Models](https://arxiv.org/abs/2606.16044)

**<font color=#1a73e8>作者：</font>** Darin Tsui, William Deinzer, Daniel Saeedi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein language models (pLMs) can generate novel protein sequences with properties beyond those observed in nature, yet the mechanisms underlying protein generation remain poorly understood. Existing mechanistic interpretability methods based on sparse autoencoders and transcoders primarily focus on protein representation learning models and do not capture the computation required for autoregressive generation. Here, we introduce ProGenMech, a mechanistic interpretability framework for generative protein language models that extends cross-layer transcoders (CLTs) to ProGen3, a sparse Mixture-of-Experts model trained for both causal generation and span infilling. Unlike per-layer approaches, CLTs reconstruct each layer using sparse latent variables from all preceding layers, enabling faithful recovery of inter-layer generative computation. We further develop a zero-shot circuit discovery framework to identify sparse latent circuits responsible for protein generation and fitness prediction. In causal generation and zero-shot fitness estimation tasks, ProGenMech outperforms local transcoder baselines in recovering ProGen3's probability distribution and functional scoring behavior, while matching the original model's generative distribution in span infilling tasks. Moreover, the recovered circuits reveal biologically meaningful motifs and functional regions associated with conserved sequence patterns and protein fitness landscapes, establishing a foundation for interpretable and steerable protein generation.

---


### 148. [From Argument Components to Graphs: A Multi-Agent Debate with Confidence Gating for Argument Relations](https://arxiv.org/abs/2606.16047)

**<font color=#1a73e8>作者：</font>** Jakub Bąba, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly assessed and utilized in the field of Argument Mining (AM), thanks to their strong general reasoning capabilities. However, standard training-free models often miss sophisticated details, specifically in contexts where two parts of the text have to be analyzed together. Furthermore, self-correction mechanisms tend to reinforce initial hallucinations in reasoning. Overcoming these limitations typically requires expensive, domain-specific supervised fine-tuning. Recent work has shown that a multi-agent paradigm can address such weaknesses for the component classification task through dialectical refinement with a Proponent-Opponent-Judge architecture, setting a promising direction for training-free approaches in the field. In this paper, we extend and evaluate this framework on the Argument Relation Identification and Classification (ARIC) task, reformulating it as a debate over component pairs. Besides that, we introduce a confidence gating mechanism that enables debating only on the uncertain cases and accepting the initial prediction when confidence is high. On the UKP Argument Annotated Essays v2 corpus, we demonstrate that the selective debate achieves the highest Macro F1 among all training-free methods, while debate over all samples degrades performance below that of one of the baselines. All generative approaches also outperform fine-tuned RoBERTa models on Macro F1, suggesting that the under-representation of the Attack class was more damaging to supervised fine-tuning than to inference-only models. Additionally, our framework produces human-readable debate transcripts, offering interpretability absent from both single-agent and supervised classifiers.

---


### 149. [Stepwise Token Selection for Efficient Multimodal Large Language Models](https://arxiv.org/abs/2606.16067)

**<font color=#1a73e8>作者：</font>** Landi He, Shawn Young, Lijian Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In multimodal large language models (MLLMs), inference cost is largely dominated by the visual token prefix rather than the language backbone, making token reduction a key factor for improving efficiency. Existing approaches typically assign independent importance scores to visual tokens and retain a fixed number of top-ranked tokens, implicitly assuming token independence and a uniform compression ratio across inputs. In this work, we reformulate visual token pruning as a sequential decision-making process. Specifically, we introduce a pointer-style selection mechanism that iteratively chooses informative tokens, conditioning each decision on previously selected ones, and dynamically determines when to stop via a learned termination action. This enables joint optimization of both the selected subset and its size. To enable end-to-end training under standard language modeling objectives, we design a differentiable relaxation based on a variance-preserving noise interpolation scheme, allowing gradients to propagate through the discrete selection process. Extensive experiments on LLaVA-v1.5-7B and Qwen2.5-VL-7B demonstrate that our approach consistently outperforms fixed-ratio baselines across different compression levels. Under aggressive pruning that removes 88.9% of visual tokens, our method preserves 94.6% of the original accuracy while achieving a 1.88x speed-up in prefill latency.

---


### 150. [Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games](https://arxiv.org/abs/2606.16070)

**<font color=#1a73e8>作者：</font>** Yifei Dong, Mingen Zheng, Linquan Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World-model synthesis aims to turn interaction experience into an internal model of environment dynamics. Existing symbolic approaches often fit observed transitions or mixtures of local rules, but they do not produce a complete executable program that can run independently of the real environment. We present Mind-Studio, a framework that synthesizes executable pygame-style world models from state-action-next-state trajectories using large language models. Mind-Studio combines entropy-selected traces with a lightweight game skill file containing object, action, and static scene information extracted from screenshots. We evaluate synthesis quality with a K-step lookahead fidelity protocol that compares generated world-model rollouts against Real-ALE rollouts from the same state. On Montezuma's Revenge, Mind-Studio improves chosen-action next-state prediction from 0.3% for PoE-World to 48.7% while verifying 5 of 8 subgoals; across Alien, Assault, and Skiing, it achieves stronger branch-level fidelity than prior learned lookahead sources.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
