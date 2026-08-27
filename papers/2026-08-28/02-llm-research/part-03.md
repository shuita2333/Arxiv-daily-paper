# 🧠 大模型相关研究 | 2026年08月28日

> 本类共 **209** 篇论文：已确认 **195** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-209](./part-05.md)

---

### 101. [TailorCoPilot: Enabling Agentic Pattern Making with Version-Controlled State Tracking](https://arxiv.org/abs/2608.25462)

**<font color=#1a73e8>作者：</font>** Yuexin Sun, Zhaohui Wang, Ruiyang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Experience-driven manufacturing, such as garment pattern making, faces a severe generational skills gap because its core expertise relies on undocumented tacit knowledge forged through day-to-day practice. To address this challenge, we present TailorCoPilot, an agentic pattern-making system built upon a specially designed version-control backend TailorTrace. TailorTrace models sewing patterns as structured, discrete states and records their transformations during the pattern-making process as explicit operation sequences defined upon the geometry primitives in the sewing pattern (panels, edges, vertices and stitches). Integrated into a conventional pattern-making GUI, TailorTrace enables seamless documentation of senior experts' tacit pattern-making knowledge without breaking their daily workflow. The documented knowledge further offers interactive, pedagogical scaffolding for novices, while providing a robust foundation to power TailorCoPilot and train future generative AI models. In a user study with novices and advanced novices, TailorCoPilot improved task completion rates, reduced time and perceived workload, and yielded higher-quality artifacts compared to skill-appropriate baselines. Ultimately, TailorCoPilot demonstrates a viable pathway to capture practice-based expertise, operationalizing it to support both generative AI advancements and human apprenticeship.

---


### 102. [VietAIDetector: An Open-Source Zero-Shot Detector for Vietnamese AI-Generated Text](https://arxiv.org/abs/2608.25478)

**<font color=#1a73e8>作者：</font>** Trieu Hai Nguyen, Van-Dung Hoang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, distinguishing between AI-generated text and human-written text has remained a challenge. In this paper, we introduce VietAIDetector, an open-source tool designed specifically for detecting Vietnamese AI-generated text. It allows users to interact through a Gradio web interface with inputs ranging from raw Vietnamese text to common text file formats, including scanned documents and exceptionally long texts that exceed the context size of the employed Large Language Models (LLMs). The core component of the tool employs a Zero-Shot approach to detect AI-generated text without requiring domain-specific training data, building upon the previous VietBinoculars and Binoculars research. The tool is built upon a Vietnamese-specific language model and has been evaluated on out-of-domain datasets, demonstrating superior performance compared to existing methods primarily developed for English. Additionally, users can select optimal detection thresholds based on F1 score, accuracy, or TPR@0.05FPR requirements. The results are presented through the web interface, allowing users to easily review and verify suspicious texts or download them as a PDF report. The tool is publicly available at this https URL

---


### 103. [Semi-Supervised Adaptation of Vision-Language Models for Image Classification](https://arxiv.org/abs/2608.25485)

**<font color=#1a73e8>作者：</font>** Mohamed L. Mekhalfi, Mohamad M. Al Rahhal, Yakoub Bazi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models like CLIP have shown sig- nificant potential in handling natural images, yet their perfor- mance is often limited by the distinct characteristics of satellite imagery. While parameter-efficient adaptation techniques exist, their efficacy is frequently limited by the scarcity of annotated samples. In this letter, we propose Self-Evolutionary CLIP (SE- CLIP), a semi-supervised framework designed for recursive label mining in scene classification. The approach follows a dual-phase pipeline, where an initial warm-up on a few annotated seeds is followed by a recursive discovery phase that iteratively identifies high-confidence samples from unlabeled pools. To maintain the integrity of the evolving support set, we employ a class-balanced selection strategy that prevents the model from being dominated by easily learned categories. Results on the UCM and NWPU benchmarks indicate that SE-CLIP significantly outperforms existing semi-supervised approaches. The framework provides a viable solution for adapting VLMs to the remote sensing domain with minimal human intervention.

---


### 104. [PonsRAG: A Pons-Inspired RAG Bridging Cognitive Islands for Coordinated Long Narrative Reasoning](https://arxiv.org/abs/2608.25486)

**<font color=#1a73e8>作者：</font>** Rongchen Zhao, Yu Chen, Juyuan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long Narrative Reasoning is an essential capability for processing and reasoning over complex narratives. While retrieval-augmented generation provides a promising framework, existing methods still face two critical challenges: cognitive islanding and cross-layer evidence disconnection. To address these issues, we propose PonsRAG, a coordinated RAG framework inspired by the biological pons. PonsRAG consists of two key components: Triple-Layer Indexing, which organizes documents into a connected knowledge structure to bridge cognitive islands, and Coordinated Reasoning, which retrieves evidence across distinct layers and integrates cross-layer information into a unified context. We evaluate PonsRAG on four long-context narrative benchmarks, and experimental results show that it outperforms the strongest baseline, achieving a 11.56% relative improvement in average accuracy on multi-choice tasks.

---


### 105. [ReliableRAG: Combating Misinformation in Retrieval-Augmented Generation via Reliability-Guided Reasoning Chains](https://arxiv.org/abs/2608.25487)

**<font color=#1a73e8>作者：</font>** Jinpu Jiang, Xuan Wu, Wenhao Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has emerged as a powerful architecture for Question Answering (QA) by integrating external information into Large Language Models (LLMs). However, false, inaccurate, and misleading information in news and social media poses a serious challenge to real-world RAG systems, especially in multi-hop QA, where complex multi-step reasoning can be misled by even a single deceptive misinformation segment in the retrieved documents. Existing approaches mainly rely on implicit alignment or explicit regulation, but their limited ability to assess fine-grained information reliability makes them vulnerable to deceptive misinformation that is semantically relevant to the question yet factually incorrect, leading to erroneous answers. To address this limitation, we propose ReliableRAG, which, to the best of our knowledge, is the first reliability-driven framework that mitigates deceptive misinformation in multi-hop QA through fine-grained evaluation of individual triples. ReliableRAG first extracts information segments from source documents and represents them as structured triples. It then quantifies triple reliability by combining query-triple semantic relevance with triple credibility, retaining only the top-$K$ reliable and non-redundant triples. Based on these refined triples, ReliableRAG autoregressively constructs robust reasoning chains to consolidate trustworthy evidence and filter deceptive misinformation, producing accurate answers faithful to reliable information. Experiments on three multi-hop QA datasets show that ReliableRAG outperforms existing methods, substantially improving the factual reliability and robustness of RAG systems under deceptive misinformation injection.

---


### 106. [A Storage-Retrieval Gap in Parametric Knowledge Graph Memory](https://arxiv.org/abs/2608.25489)

**<font color=#1a73e8>作者：</font>** Martino M. L. Pulici, Cuong Xuan Chu, Evgeny Kharlamov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph retrieval-augmented generation places retrieved subgraphs into the model's context window at query time, paying a recurring token cost and exposing source data on every call. We study an alternative: compiling a knowledge graph offline into a bank of LoRA adapters, one per entity, that serve as a parametric knowledge layer queried by injecting weights rather than text, at zero query-time context cost. On the MetaQA dataset, we find that subgraph-trained adapters encode context-free factual knowledge that generalizes to unseen questions: on single-valued relations the adapter gains $+0.243$ exact-match score over a base model that is nearly blind closed-book ($0.007$), and only the correct adapter recovers this knowledge (an oracle gap of $+0.283$ over the base model). However, the stored knowledge is not recoverable by similarity: given a query with no subgraph, embedding-based and weight-space geometry retrieval both perform at chance, because a semantically neighbouring entity's adapter does not contain the answer - knowledge is stored locally and does not transfer. Weight geometry correlates with subgraph semantics ($\rho = +0.329$) but not with functional retrievability. We quantify the byte and context-token costs against graph retrieval-augmented generation and discuss deployment implications. Our results establish that parametric knowledge graph memory is feasible for storing knowledge, and identify selecting and composing the right adapters by a mechanism other than semantic similarity as the central open problem - motivating a learned, query-conditioned composition mechanism.

---


### 107. [SMART: MLLM-guided Temporal Alignment for Unifying Sign Language Recognition and Spotting](https://arxiv.org/abs/2608.25493)

**<font color=#1a73e8>作者：</font>** Eunjee Choi, JungHoon Sung, Seongwhan Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous sign language recognition (CSLR) aims to recognize gloss sequences from unsegmented sign videos under weak sequence-level supervision. However, existing methods rely on sentence-level gloss annotations, providing limited temporal and semantic guidance for fine-grained representation learning. Conventional video-text alignment also requires large batch sizes, making it inefficient for memory-intensive sign language video training. In this work, we propose SMART, an MLLM-guided temporal alignment framework for joint sign recognition and spotting. SMART uses MLLMgenerated motion descriptions as auxiliary semantic cues and performs stable videotext alignment under small-batch training. To improve temporal representation learning, we introduce a Multi-Scale Temporal Adapter that models temporal interactions during transformer encoding. For dense temporal localization, SMART incorporates CSFormer, a CSLR-guided spotting module that injects recognition-derived gloss evidence into a boundary-aware spotting network. This unified framework enables CSLR features to benefit spotting, while spotting supervision complements weak CTC-based recognition. Experiments on four sign language benchmarks, including PHOENIX14-T, CSL-Daily, Large-scale KSL, and Disaster and Safety KSL datasets, demonstrate the effectiveness of SMART across both recognition and spotting tasks.

---


### 108. [CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval](https://arxiv.org/abs/2608.25500)

**<font color=#1a73e8>作者：</font>** Zhiyuan Li, Linyuan Gao, Xuechun Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reusable skill libraries allow large language model (LLM) agents to reuse procedural knowledge across tasks, but they also turn memory access into a challenging retrieval problem. Full-library prompting preserves coverage at high context cost, vector retrieval returns compact neighborhoods but treats skills as independent text, and graph-based retrieval can recover workflow context only when the edges that carry relevance are reliable. We propose CaSKG, a counterfactual-causal skill graph framework that calibrates procedural relations before retrieval. CaSKG first builds a high-recall directed candidate graph from semantic, lexical, input/output, and structural evidence, with repair evidence and an optional LLM judge further refining candidate scores. It then applies direction-conditioned textual counterfactual probes that remove, substitute, and reorder skill pairs, aggregates the evidence with Bayesian smoothing, and publishes a state-filtered weighted graph for task-conditioned expansion. The graph is constructed offline and used without changing the downstream agent policy or task interface. Across six LLM backbones on ALFWorld ID-140 and ScienceWorld U211, CaSKG achieves the highest task score in all twelve combinations of model and benchmark. Relative to Graph-of-Skills (GoS), it improves the six-model macro-average ScienceWorld score from 72.62 to 80.50 and ALFWorld success from 80.01\% to 86.79\%, while reducing mean environment steps on both benchmarks. Qualitative and ablation analyses further show that calibrated edges help retrieval preserve prerequisites, state-changing actions, verification routines, and final completion steps. These results position edge-confidence calibration as an effective route to compact and executable skill retrieval at scale\footnote{Code is available at: this https URL }.

---


### 109. [Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models](https://arxiv.org/abs/2608.25518)

**<font color=#1a73e8>作者：</font>** Pengfei Zhou, Hexin Wang, Zhengfeiyang Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A common strategy for scaling world models is to train on more crawled video with more compute. We argue that this strategy is inefficient: scaling world models also requires a recursive data engine that offers grounded reward signals. The success of code agents illustrates why this matters. As code is executable, compilers and runtimes can provide high-quality rewards for Reinforcement Learning (RL) post-training of LLMs. By contrast, spatial generation still relies largely on fuzzy proxies such as CLIP scores. These signals are fuzzy and biased, making them hard to support RL post-training. Compared with these, game development provides a missing reward environment for spatial world models. A scene encoded by a game engine is an executable world specification: the engine can efficiently check collision, physics, navigability and bounded playability, while the developer provides the global verification signal by judging whether the scene should be accepted. Game development also provides real-world long-horizon trajectory data for RL post-training. We therefore propose Reinforcement Learning with Human-Engine Verification (RLHEV), a post-training paradigm that combines dense engine signals with implicit human acceptance feedback from the development process.

---


### 110. [TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving](https://arxiv.org/abs/2608.25523)

**<font color=#1a73e8>作者：</font>** Hongqiu Ni, Han Tian, Chi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prefix caching introduces a fundamental tradeoff in multi-agent large language model (LLM) serving: retaining a long system-prompt key-value (KV) cache for an agent accelerates future calls, yet it reduces the GPU memory available for batching concurrent requests. In multi-stage workflows, existing schedulers tend to prioritize either immediate prefix locality or overall workflow progress. However, under a shared KV cache budget, optimizing either objective in isolation can prolong tasklevel job completion time (JCT) through downstream delays or frequent prefix replacement. To strike a balance, we here propose TOPAS, a Task-Oriented Prefix-Aware Scheduler that jointly decides which agent prefixes to keep in the cache and which requests to schedule for execution. TOPAS scores candidate post-decision states by trading off the expected reduction in each task's longest remaining service path against the near-term benefit of downstream prefix reuse, accounting for the costs of prefix movement and preemption. A task-level aging mechanism is also incorporated to prevent starvation. We implement TOPAS within the SGLang framework and assess its performance on three synthetic DAGs and two MetaGPT software-development workflows. Compared with the best performing baseline for each workload and metric, TOPAS reduces the mean/p99 JCT by up to 39.8%/49.4% on the synthetic workloads, while lowering mean JCT by 9.8% on MetaGPT-SOP and mean/p99 JCT by 22.0%/26.6% on MetaGPT-TL.

---


### 111. [Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios](https://arxiv.org/abs/2608.25529)

**<font color=#1a73e8>作者：</font>** Hongbo Liu, Peixian Chen, Sihan Liu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown strong performance in video understanding. However, their ability to follow instructions in this domain remains under-explored. Real-world video understanding requires models not only to interpret video content correctly, but also to satisfy diverse user-specified constraints. Existing benchmarks focus primarily on task accuracy rather than instruction adherence, leaving this capability insufficiently evaluated. To address this gap, we introduce Video-IFBench, a comprehensive benchmark for evaluating instruction following in video understanding, where models must satisfy diverse user-specified constraints, including those grounded in visual and audio content. We develop an instruction taxonomy with four templates, including single-task, multi-task, selection, and nested instructions, covering 32 task types and 39 manually designed constraint categories spanning both semantic and format requirements. To reduce annotation cost, we build a semi-automatic data construction pipeline that combines MLLMs, programmatic processing, and human verification, resulting in 1.5K samples. We conduct a large-scale evaluation of more than 20 recent MLLMs and show that video instruction following remains challenging for current models, especially for instructions with many constraints, semantic constraints, or complex conditional structures that require selecting the correct branch or path based on video content. We hope our work will facilitate future research on instruction following in video understanding scenarios.

---


### 112. [ClueWeaver: Reward-Guided Dual-Agent Evidence Reasoning for Compact LLMs on Literary Long Narratives](https://arxiv.org/abs/2608.25531)

**<font color=#1a73e8>作者：</font>** Jihao Zhu, Zhiwei Yang, Wenxiao Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humanities and social science research requires close reading of long narrative materials such as novels, scripts, archives, and case reports, yet many users have limited access to costly proprietary long-context models. Compact, locally deployable language models are a practical alternative, but directly feeding them an entire long context remains costly, hard to inspect, and prone to missing sparse evidence. We present ClueWeaver, an evidence-aware dual-agent framework for long-narrative question answering with compact local models. A Finder identifies passages containing answer-critical clues through retrieval-guided segmentation, while an Interpreter derives the answer from the selected evidence, produces rationales with paragraph-ID citations, and applies an internal self-calibration pass for high-risk questions. Both agents are optimized with reward-guided reinforcement learning: Finder rewards emphasize evidence retention and faithful paragraph-ID references, and Interpreter rewards emphasize correctness, grounding, and concise explanations. This decomposition makes evidence selection and reasoning more inspectable than end-to-end prompting. Experiments across multiple long-context narrative question answering and claim verification settings show that ClueWeaver substantially improves local end-to-end language models while providing evidence coverage and paragraph-referenced reasoning traces. Code is available at this https URL.

---


### 113. [Reflection Steering: Disentangling Reflection from Reasoning in Activation Space for Token-Efficient Inference](https://arxiv.org/abs/2608.25542)

**<font color=#1a73e8>作者：</font>** Jiarui Hu, Zhiyuan Wen, Xiaoyun Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large reasoning models often produce reasoning traces with verification, revision, and backtracking. When reflection merely re-checks established results, it wastes reasoning tokens and increases latency. Most existing reflection steering methods add a label-derived mean-difference direction across preset layers, but its entanglement with reasoning and length signals destabilizes the accuracy-efficiency trade-off. In this paper, we propose Reflection Steering, a training-free framework for controlling reflection-associated computation within LLMs by disentangling reflection-related activations from general reasoning. Specifically, we contrast reflective and non-reflective hidden states at each LLM layer, denoise the resulting reflection directions with PCA, and orthogonalize them against general-reasoning directions. To limit downstream amplification from early-layer interventions, we calibrate each layer across multiple intervention strengths on a small set, retain only stable layers, and apply bounded projection removal to their residual-stream activations. We conduct extensive experiments across two public benchmarks and three open-weight LLMs against state-of-the-art activation-steering baselines. Results show that Reflection Steering reduces reasoning tokens by 16.9% on average across six matched settings. Besides, our method further introduces a bounded reflection intervention-strength parameter $\alpha$, enabling deployment-time adjustment to balance token savings, accuracy, and generation stability.

---


### 114. [Interpreting Protein Language Model Embeddings via Orthogonal Projection for Protein Fitness Prediction](https://arxiv.org/abs/2608.25548)

**<font color=#1a73e8>作者：</font>** Paulo Yanez Sarmiento, Pia Francesca Rissom, Manuel Pfeuffer 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, there has been a growing adoption of protein language models (PLMs) in biomedical science. Their embeddings provide a rich numerical representation of protein sequences which achieve state-of-the-art performance on several downstream tasks including protein fitness prediction. However, PLM embeddings are not directly interpretable and, thereby, it remains unclear what features they encode. To gain insight into which biochemical properties of the protein are driving the prediction, we leverage an orthogonal projection technique that removes linear effects of known tabular features from embeddings and extend it to high-order and interaction effects. In this way, we remove the effects of interpretable biochemical features from PLM embeddings. In an ablation study, we show that this leads to a decrease in performance for a downstream classifier trained only on the embeddings to predict protein fitness. In an additional evaluation, we find that these biochemical features explain a substantial part of the variance in the predictions of this classifier. Hence, we can show that PLM embeddings encode patterns correlated with biochemical properties and quantify their contribution to predicting protein fitness. This computationally efficient approach is not limited to the features or embeddings considered here and is readily transferable to problem settings beyond protein fitness prediction.

---


### 115. [Virgil: Navigating Explainability for Transformer-based Language Models](https://arxiv.org/abs/2608.25555)

**<font color=#1a73e8>作者：</font>** Martino Ciaperoni, Sezer Kutluk, Benedetta Muscato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Explainability for transformer-based language models is becoming crucial as these systems are deployed in high-stakes applications. As a result, the ecosystem of explainability tools is rapidly evolving, becoming richer, but also more fragmented and harder to navigate. To address this challenge, we present Virgil, an interactive system that lets practitioners and researchers, including non-experts, navigate explainability tools for transformer language models. Supported by a curated knowledge base, the system enables users to discover and compare explainability tools within a unified interface.

---


### 116. [EgoArgus: Benchmarking VLMs as Situational Assistants for Modality-Grounded User Supports](https://arxiv.org/abs/2608.25561)

**<font color=#1a73e8>作者：</font>** Yu-Chien Tang, Yu-Hsiang Liu, An-Zi Yen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> VLMs are increasingly positioned as daily assistants that perceive first-person environments, follow user dialogue, and decide how to help. Existing egocentric benchmarks mainly evaluate visual understanding in isolation, leaving open whether models can arbitrate between visual evidence and user-provided language when the two are helpful, irrelevant, or conflicting. We introduce EgoArgus, a human-annotated dataset for evaluating egocentric assistants on understanding and decision tasks in five dialogue-video daily scenarios. Our results demonstrate that it is still challenging for current VLMs as reliable egocentric assistants, which requires identifying which modality is trustworthy and deciding when intervention is warranted. Deeper analysis also shows that existing modality bias mitigation methods are quite restricted to enhance performance, providing insights to aid practioners into the deployment of current VLMs as daily assistants.

---


### 117. [Controllable Affective Generation via Latent Vector Steering](https://arxiv.org/abs/2608.25569)

**<font color=#1a73e8>作者：</font>** Xixian Yong, Siyuan Chang, Yingying Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often produce emotionally flattened responses after alignment, limiting their effectiveness in affect-sensitive applications. In this paper, we propose EmoVec, a lightweight framework for controllable affective generation via latent vector steering. EmoVec extracts emotion-specific directions from paired neutral and emotion-conditioned responses using contrastive activation addition, and further refines them through task-specific debiasing and principal subspace removal. During inference, these vectors are injected into the final residual stream with static or scenario-adaptive scaling, enabling continuous control over emotional intensity without updating model weights. Experiments across three LLMs and eight emotions show that EmoVec consistently improves emotional salience while largely preserving semantic content, fluency, and coherence. Ablation studies and human evaluation further confirm the effectiveness of vector purification and adaptive scaling, establishing EmoVec as a practical inference-time method for affective control in deployed LLMs.

---


### 118. [Beyond Scaling: Self-Evolving LLM Agents for Hardware Kernel Optimization via an Experience-Driven Workflow and Experience Graph Memory](https://arxiv.org/abs/2608.25570)

**<font color=#1a73e8>作者：</font>** Siyuan Chen, Runlin Hou, Shenxiu Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hardware kernel optimization requires repeated compilation, correctness testing, profiling, and revision. LLM agents can automate parts of this process, and stronger foundation models, longer context windows, and longer execution horizons have improved optimization within individual tasks. These advances alone do not enable an agent to learn from completed optimization runs. Existing kernel-optimization agents seldom preserve a decision, its observed execution feedback, and the later decisions that use that evidence. Retaining every prior trajectory is also impractical because an expanding history competes with the current task for context. We present KOPE, an experience-driven framework for hardware kernel optimization. KOPE records optimization trajectories with correctness and performance feedback in Experience Graph Memory, then uses Active Context Management and Injection to retrieve relevant experience under a fixed token budget. The graph retains decision order, observed outcomes, and alternative branches, allowing evidence collected on the target hardware to inform later optimization steps and tasks. Under the same GLM-5.2 setting, the geometric mean of KOPE's per-operator speedups is $1.54\times$ that of CANNBot, the strongest competing baseline. In a complete 53-operator ablation, Active Context Management and Injection raises pass rate from 60.0\% to 84.6\%, increases the evaluator-reported positive-field geometric mean from 0.0382 to 0.0661, and reduces optimization token consumption from 15.9B to 1.113B tokens relative to passive agent-led context construction. Enabling Experience Graph Memory raises full-suite pass rate from 55.2\% to 84.6\% and yields a $1.43\times$ geometric-mean speedup on valid timing comparisons. These results support continual optimization through external experience while the foundation model remains fixed.

---


### 119. [Generative vs. Encoder Large Language Models for ASR Evaluation: A Comparative Study](https://arxiv.org/abs/2608.25574)

**<font color=#1a73e8>作者：</font>** Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) is typically evaluated using Word Error Rate (WER), which poorly reflects semantic similarity. While embedding-based metrics correlate better with human judgments, the respective roles of encoder and decoder-based Large Language Models (LLMs) remain underexplored. This paper presents a comparative study of both families for ASR evaluation. We analyze BERTScore and SemDist across different LLMs, layers, and pooling strategies, showing that both metrics can achieve strong correlation with human judgments when properly configured. For decoder models, we investigate generative LLMs in two settings: pairwise hypothesis selection via prompting and direct qualitative error classification. Our results show that encoder-based metrics remain highly competitive, while generative LLMs perform strongly in hypothesis comparison and improve the interpretability of ASR evaluation.

---


### 120. [MLLMCLIP: Feature-Level Distillation of MLLM for Robust Vision-Language Representations](https://arxiv.org/abs/2608.25575)

**<font color=#1a73e8>作者：</font>** Jongsuk Kim, Qiyu Wu, Zhuoyuan Mao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained vision-language models such as CLIP excel at zero-shot recognition but often fail at compositionality, particularly attribute-object and relational structures. Recent studies mitigate this issue by augmenting training with synthetic hard negatives generated by a cascade of large language models and text-to-image models, which incurs substantial pipeline overhead. We instead propose MLLMCLIP, a heterogeneous distillation framework that transfers multimodal knowledge directly from a generative Multimodal Large Language Model (MLLM) teacher into a discriminative CLIP student, bypassing synthetic data entirely. To bridge the architectural mismatch between the two paradigms, we introduce an attention-based per-layer token selection and a CKA-based distillation loss. Compared to prior CLIP-enhancement methods, MLLMCLIP achieves state-of-the-art compositional accuracy while delivering consistent gains on standard zero-shot classification and image-text retrieval, showing that feature-level distillation strengthens both compositional and general vision-language representation capability.

---


### 121. [Cross-Dataset Stability of Expert-Informed Skill Prompting and Fine-Tuning for Chinese Metaphor Identification](https://arxiv.org/abs/2608.25579)

**<font color=#1a73e8>作者：</font>** Yufeng Wu, Meichun Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metaphor-identification performance can change markedly across datasets that differ in text distribution and annotation policy. We examine whether a fixed expert-informed procedure produces a more even cross-dataset profile than task-specific parameter adaptation. Four prespecified conditions are compared for Chinese sentence-level metaphor identification: BERT fine-tuning (BERT-FT), QLoRA-based large language model fine-tuning (LLM-FT), direct zero-shot LLM prompting (LLM-ZS), and zero-shot prompting with a frozen procedural Skill (Skill-ZS). The Skill operationalizes established criteria involving contextual meaning, basic meaning, contrast, and comparison. Evaluation covers CMRE Test and two external datasets, CCIME and CMC. Fine-tuned scores are means over three seeds, whereas each zero-shot score comes from one deterministic configuration. Fine-tuning remains strongest on the native test set: BERT-FT reaches 91.76 Macro-F1. LLM-FT has the highest external mean (83.52), while Skill-ZS is close at 82.92 and has both the highest external floor (82.64) and the smallest observed range across all three datasets (4.08 points). In the matched zero-shot comparison, adding the Skill reduces metaphorical predictions on every dataset. This sharply lowers false positives on CCIME but increases false negatives on CMRE Test and CMC. The results position expert-informed Skill prompting as a complementary route to more even observed cross-dataset performance, while fine-tuning retains its advantage in native-data accuracy. To our knowledge, this is the first study to compare an expert-informed procedural Skill with task-specific fine-tuning in the same cross-dataset evaluation of Chinese sentence-level metaphor identification.

---


### 122. [V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2608.25580)

**<font color=#1a73e8>作者：</font>** Shulin Tian, Minglun Li, Yuhao Dong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models can produce fluent answers that are insufficiently grounded in the visual evidence: a single unsupported object, chart value, or intermediate inference can undermine an otherwise plausible response. We argue that this is a credit-assignment failure in multimodal post-training. Scalar outcome rewards indicate whether an answer is acceptable, but do not identify which visual facts are grounded, which reasoning steps are valid, or which instruction constraints are missed. We introduce Visual Rubrics-Based Reinforcement Learning, which decomposes reference responses into atomic propositions and scores generated answers along Visual Faithfulness (VF), Reasoning Consistency (RC), and Instruction Following (IF). The resulting rubric items provide structured partial credit and localize rubric credit when supporting evidence spans are available. We first obtain an SFT checkpoint by fine-tuning Qwen3-VL-8B-Instruct on the public OpenMMReasoner-SFT-874K corpus, adapting OpenMMReasoner's cold-start data recipe. We construct V-Rubrics 50K, a 50,248-example training set from 17 visually grounded sources, by applying rule-based filters before deriving example difficulty from rejection-sampling scores and then annotating every example with Gemini-3-Pro under the same structured prompt and protocol. We train our model based on the same SFT checkpoint using component-wise, prefix-localized rubric credit. Experiments show that our rubricbased GRPO improves over both the shared SFT baseline and answer-only GRPO, with the largest gains on knowledge-oriented and visually grounded reasoning benchmarks. The results show rubrics as a useful reward abstraction for visual post-training.

---


### 123. [GRIP: Granular Reward-Guided Parameter Interpolation for Efficient Reasoning](https://arxiv.org/abs/2608.25583)

**<font color=#1a73e8>作者：</font>** Lam So, Canhui Wu, Han Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning-oriented large language models often achieve strong problem-solving performance by generating long chains of thought, but this behavior substantially increases inference cost and latency. In contrast, instruction-tuned models tend to answer more concisely, yet often lack comparable reasoning ability. This accuracy-efficiency mismatch motivates a lightweight approach that combines the strengths of both models without full model retraining. In this paper, we propose GRIP (Granular Reward-guided Interpolation of Parameters), a reward-guided parameter interpolation framework for efficient reasoning. Given a reasoning model and an instruction model with identical architectures, GRIP assigns learnable interpolation ratios to individual modules and optimizes only these ratios while keeping both source models frozen. The interpolation ratios are trained with a reward signal that favors responses that are both correct and concise. Experiments show that GRIP achieves a better accuracy-efficiency trade-off than fixed or search-based merging baselines and further reveals module-wise fusion patterns associated with efficient reasoning.

---


### 124. [JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution](https://arxiv.org/abs/2608.25593)

**<font color=#1a73e8>作者：</font>** Guibin Zhang, Leo Lu, Fangzhou Xie 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent capability is not determined by the model alone. The agent harness, encompassing memory management, planning strategy, action protocol, and tool/skill orchestration, can dominate the contribution of the underlying foundation model. Yet harness design remains manual, task-specific, and fundamentally unscalable. We present JIT-Agent, a harness intelligence model trained to synthesize task-adaptive agent harnesses on the fly for arbitrary off-the-shelf agentic LLMs. We formalize the agent harness as a composable, machine-generatable artifact governed by a fixed four-module protocol, and train JIT-Agent to customize harnesses for a given task at hand, repair harnesses for stable and reliable execution, and self-evolve by distilling performance signals from an expanding archive of prior harness configurations. Equipped with JIT-Agent as a harness helper, DeepSeek-V4-Flash surpasses GPT-5.6 on DeepSearchQA (+9.1) and OdysseyBench (+4.3), while the already strong GLM-5.2 gains up to +20.2 points. Across controlled evaluations, JIT-Agent-generated harnesses are performance-competitive with mature agent runtimes such as OpenCode and Claude Code and consistently improve multi-scale model families of DeepSeek V4, Mimo-V2.5, and Qwen3.6. To our knowledge, JIT-Agent is the first model purpose-built for just-in-time harness generation, establishing harness intelligence as a trainable, transferable, and compounding dimension of agent capability orthogonal to model scaling.

---


### 125. [From Specialization to Generalization: Instruction-tuned LLMs for Robust Harmful Content Mitigation](https://arxiv.org/abs/2608.25605)

**<font color=#1a73e8>作者：</font>** Lukas Edman, Daryna Dementieva, Alexander Fraser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) demonstrate impressive performance across a wide range of general NLP tasks; however, their effectiveness in sensitive domains, such as hate speech detection, remains less clear. Prior studies comparing prompted LLMs with state-of-the-art encoder-based models (e.g., BERT variants (Roy et al., 2023; Dönmez et al., 2024)) have shown only marginal gains, suggesting that LLMs may not excel in hate speech detection or mitigation. In this work, we revisit this question through the lens of instruction tuning. By thoroughly unifying 36 English hate speech datasets spanning multiple labeling schemes, we fine-tune a generalist LLM, based on Qwen3 (Qwen Team, 2025), specifically for hate speech mitigation. Our results demonstrate not only state-of-the-art performance on in-domain benchmarks but also substantial improvements in cross-domain and cross-lingual generalization--areas where encoder-based specialist classifiers often struggle.

---


### 126. [AWM: Answerable Working Memory for Long-Document VQA Agents](https://arxiv.org/abs/2608.25618)

**<font color=#1a73e8>作者：</font>** Dongzhuoran Zhou, Yuqicheng Zhu, Yule Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-document visual question answering increasingly relies on VLM agents that retrieve candidate pages, inspect page images, write findings to working memory, and synthesize answers. Working memory should carry answer-supporting evidence across page inspections for later grounded answering, yet existing evaluation mainly checks final-answer correctness and evidence-page access. This creates a memory-quality blind spot: an agent may reach the right page and answer correctly while leaving behind memory too generic or incomplete to support answering once page context is removed. We introduce \emph{memory-only answerability}, a diagnostic that asks whether a reader can answer from the question and terminal working memory alone. Building on this diagnostic, \emph{Answerable Working Memory} (AWM) treats terminal working memory as an answerable evidence artifact, and AWM-GRPO incorporates this signal into the GRPO reward while preserving final-answer priority. Under GRPO, this reward assigns higher advantages to answer-correct trajectories whose terminal working memory remains answerable. On \textsc{MMLongBench-Doc}, even when gold evidence pages are provided, 42.5\% of correct answers still cannot be answered from terminal working memory alone. AWM-GRPO improves final-answer accuracy over the RAG baseline by 8.1 and 11.9 points on \textsc{MMLongBench-Doc} and \textsc{LongDocURL} and reduces the memory-missing-correct rate by 2.7 points over answer-only GRPO.

---


### 127. [Plans You Can Check: Verifier-Grounded Learning of an Open-Weight Planner for Executable Video-Editing](https://arxiv.org/abs/2608.25622)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Cheng Feng, Liuyang Bian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Practical video editing is not only pixel generation: an editor must turn a brief, a clip pool, music metadata, and hard constraints into an executable timeline. We study this decision layer as \emph{executable video-editing planning} and introduce RefineCut, which, unlike workflow systems that wrap a prompted frontier model, trains a compact open-weight planner for it. The planner edits a typed timeline through structured patches covering clip selection, trimming, ordering, transitions, and duration and music alignment; a deterministic verifier applies each patch and checks it against an explicit constraint ledger. Because editing has no single ground-truth repair, we do not imitate teachers directly: RefineCut replays every multi-teacher branch through the verifier and keeps verifier-best repairs as supervision. A second stage, RefineCut-Evo, lets the student score its own repairs with the verifier and a task rubric and trains on high-margin preference pairs, so the final $8$B planner runs in a closed verifier loop with no teacher calls at inference. On RefineCut-Bench ($3{,}578$ tasks, $7{,}971$ captioned clips, $499$ music tracks, explicit ledgers), verifier-replayed distillation lifts the planner from $0.620$ to $0.858$ on the protocol-specific Video-Editing Score and RefineCut-Evo reaches $0.924$; the gain transfers to Llama-3.1-8B and GLM-4-9B, and in the same closed loop the $8$B planner matches or exceeds its frontier teachers. Code and RefineCut-Bench are publicly released; see the Data Availability statement.

---


### 128. [A Token-Level Analysis of Sampled-Token Reverse-KL On-Policy Distillation](https://arxiv.org/abs/2608.25643)

**<font color=#1a73e8>作者：</font>** Bing Shao, Jiazheng Zhang, Long Ma 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) supervises a student on its own trajectories with token-level signals from a frozen teacher, yet how a sampled loss allocates updates across tokens remains poorly understood. We analyze the gradient of the per-token K2 estimator of reverse KL with respect to the student logits. The $\ell_1$ norm of this gradient factorizes into the absolute teacher--student log-probability gap and a student-side softmax factor that grows as the sampled token becomes less likely under the student. In our math-distillation runs, these per-token norms are highly non-uniform: low-student-probability tokens account for a disproportionate share of their sum and are also enriched in large teacher--student gaps. As a lightweight intervention suggested by this analysis, we study Surprise-aware Reweighting (SuRe), a detached, bounded weighting rule that further amplifies this existing allocation. Across two Qwen3 student scales, SuRe improves several math metrics over vanilla OPD and shows no clear degradation on the selected out-of-domain benchmarks. Our primary contribution is therefore a gradient-level characterization of reverse-KL OPD trained with the K2 estimator, with SuRe as one empirical instantiation.

---


### 129. [Towards Purified Multi-Label Test-Time Adaptation of Vision-Language Models](https://arxiv.org/abs/2608.25653)

**<font color=#1a73e8>作者：</font>** Yiwen Liang, Hui Chen, Yizhe Xiong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) has been widely explored in single-label recognition, effectively mitigating distribution shifts, especially when combined with vision-language models. However, real-world images often contain multiple objects, while the more practical multi-label test-time adaptation (MLTTA) has received little attention so far. Recent cache-based TTA methods have shown promising efficiency and effectiveness, yet directly extending them to multi-label scenarios suffers from a one-to-many mapping problem: a shared global representation entangling co-occurring objects is stored as class-wise cache prototypes, inducing dominant-label bias and compromised cache calibration. While introducing region-level cues helps isolate class-specific evidence, such regional evidence can also be unreliable under distribution shifts, making its identification and utilization non-trivial. To address these issues, we introduce PuRF, a novel PuRiFication-driven cache-based method for multi-label test-time adaptation of vision-language models. Specifically, PuRF first performs region purification to identify reliable regions, providing comprehensive regional cues for multi-label recognition and enabling fine-grained alignment. Based on these purified regions, PuRF conducts cache purification to enhance cache representation and adaptability, where episodic purification builds a discriminative region-based cache, and temporal refreshing further promotes long-term cache adaptability. Experiments demonstrate that PuRF consistently outperforms state-of-the-art methods, achieving a notable 4.05% mAP improvement on ViT-B/32 across five datasets.

---


### 130. [Reconstructing the Right Episode: Evaluating Interleaved Conversational Memory Beyond Long Context](https://arxiv.org/abs/2608.25655)

**<font color=#1a73e8>作者：</font>** Zhexi Feng, Ruiyi Zhang, Yongbo Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversations with chat assistants increasingly span many topics in a single long-running thread, challenging memory systems. Existing long-context and memory benchmarks often expose session or topic boundaries, or probe direct personal-memory questions. These settings understate a harder assistant-memory regime: a flat mixed-topic thread where the system must infer which earlier episode makes a later task decision valid. We introduce SCALE-QA, a constraint-grounded task QA benchmark for flat unsegmented threads targeting episode integrity failure. The dataset contains 3,000 audited questions across 10 domains, uses deterministic four-way multiple-choice grading, and includes a deterministic runtime builder; experiments use all 3,000 questions through 128k and a stratified 400-question diagnostic at 1M. SCALE-QA questions are ordinary task-oriented requests whose correct answer depends on causally related evidence introduced earlier in the conversation. We also propose Temporal-Semantic Interleaved Memory Reconstruction (TSIM), which segments the turn stream into coherent episodes and indexes them through a hierarchical multi-view memory stack with deterministic episode-level summary and cluster-routing views. Experiments show that SCALE-QA challenges strong RAG baselines and long-context LLMs alike; across three open-source and proprietary LLM backends, TSIM achieves the highest accuracy in every backend setting, gaining 5.6-17.6 accuracy points over the strongest corresponding baseline.

---


### 131. [Narcissus: Program Synthesis Using Context-Aware LLM Approximations](https://arxiv.org/abs/2608.25657)

**<font color=#1a73e8>作者：</font>** Tilman Hinnerichs, Sebastijan Dumancic, Neil Yorke-Smith  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at programming, but not when the task fixes the target language: prompted with a grammar rare in their training data, their programs usually break the grammar or fail the given specification. Enumerative synthesizers search the space of syntactically correct programs systematically guided by LLMs; the state of the art guides them by approximating LLM proposals into rule frequencies, which loses where each construct belongs and prunes every rule the proposals miss, exactly when the proposals are wrong. We present Narcissus, a synthesizer that keeps the proposals as syntax trees and scores each expansion of a candidate program in its context: does a proposal with the same surrounding structure continue the same way, and does the expansion rebuild a fragment the proposals repeat? A regularization term keeps every rule reachable, so wrong proposals delay the solution but cannot hide it. Across five domains and two search backends, Narcissus beats static guidance at every budget and consistently outperforms re-prompting the LLM to fix its own proposals; it reaches proposal-like programs an order of magnitude sooner and solves $40\%$ of ARC tasks where the raw proposals solve $13\%$, all without a single LLM call during search.

---


### 132. [Think-Probe-Respond: Improving Large Language Models as Judges of Research Idea Novelty](https://arxiv.org/abs/2608.25660)

**<font color=#1a73e8>作者：</font>** Tim Schopf, Tobias Schreieder, Akiko Aizawa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated novelty judgment can accelerate scientific discovery by enabling efficient evaluation, refinement, and comparison of research ideas. While large language models are increasingly adopted for this task, we investigate a previously overlooked limitation in their judgment capabilities: despite generating reasoning rationales that closely mirror those of human experts, their final novelty judgments often diverge substantially. We demonstrate that this miscalibration stems from a systematic bias towards judging ideas as "medium novel". To mitigate this, we propose Think-Probe-Respond (TPR), a lightweight approach that probes latent novelty judgments from hidden states during the reasoning phase and uses the probed judgments to condition the final response. Across strong baselines, TPR improves novelty judgment performance by 22.30% and successfully mitigates the prevalent "medium novelty" bias.

---


### 133. [Overview of SHROOM-Visions 2026: A Shared Task on Hallucination Detection in Large Vision-Language Models](https://arxiv.org/abs/2608.25662)

**<font color=#1a73e8>作者：</font>** Raúl Vázquez, Aman Sinha, Chuyuan Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In 2026, we held the fourth iteration of the SHROOM Shared Task series: SHROOM-Visions (\textbf{S}hared-task on \textbf{H}allucinations and \textbf{R}elated \textbf{O}bservable \textbf{O}vergeneration \textbf{M}istakes in \textbf{Vision} language model\textbf{s}), which is hosted at the UncertaiNLP Workshop co-located with EMNLP 2026. Following the success of the 2024 and 2025 tasks, this time we aim to tackle hallucinations through a model-agnostic detection task focused on large vision-language models. Building on the recently introduced SHEEP dataset, designed for long-term evaluation across model generations, the task invites participants to detect and classify fine-grained hallucination spans in image-conditioned text generation (VQA, image captioning, etc.). The evaluation uses a five-class taxonomy of hallucinations spanning four languages: Chinese, English, French, and Italian. The shared task generated strong interest in the NLP community worldwide, with 27 teams contributing 600+ system submissions. The best systems achieve average scores of 0.58 in character-level correlation, 0.46 in label-conditioned correlation, and 0.51 in intersection-over-union (IoU) across four languages, outperforming the baselines by 30-40 points.

---


### 134. [AI Slop and Hallucinations in Vulnerability Assessment: A Survey on Reasoning Failures and Trustworthy Mitigation](https://arxiv.org/abs/2608.25667)

**<font color=#1a73e8>作者：</font>** Junchen Ding, Jialiang Dong, Yichen Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The integration of Large Language Models (LLMs) into cybersecurity has transformed vulnerability assessment, but it has also produced a trustworthiness crisis driven by the unchecked proliferation of "AI slop." These artifacts, hallucinated vulnerabilities, plausible but incorrect patches, and semantically repackaged bug reports, impose a cognitive burden on human triage pipelines that mirrors a denial-of-service attack. This paper surveys the empirical evidence, identifies a unifying mechanism, and traces a path toward trustworthy triage. We formalize a taxonomy of AI slop grounded in a structured literature review and dissect its root cause: the gap between the causal deductive reasoning of security experts and the autoregressive probabilistic generation of current LLMs. We operationalize this gap through a measurable proxy, the Deductive Coverage Score, and show that chain-of-thought prompting and tool-using agents narrow but do not close it. We review mitigation strategies and argue that passive detection and watermarking target provenance rather than correctness, facing fundamental entropy constraints. We instead advocate for active neuro-symbolic verification, mapping each pipeline component to prior systems with documented limits on security inputs. Finally, we specify two evaluation instruments, CVE-Bench and Slop-Score, including dataset construction, metric formulas, and anti-gaming provisions. By shifting evaluation from linguistic fluency to mathematical verifiability, this survey provides a roadmap for securing emerging AI-driven triage systems.

---


### 135. [Learning New Facts with QLoRA: An Acquisition-Retention Frontier](https://arxiv.org/abs/2608.25677)

**<font color=#1a73e8>作者：</font>** Estelle Zheng, Sébastien Warichet, Emmanuel Helbert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning is often assumed to preserve pretrained capabilities because it updates only a small number of parameters. We show that this assumption depends strongly on adapter capacity. We study factual acquisition in a controlled OpenStreetMap-derived benchmark where Qwen3-4B must acquire anonymized geographic associations while retaining unrelated capabilities. Comparing full fine-tuning (FFT) with quantized low-rank adaptation (QLoRA) at ranks 8, 16, 32, and 64, we find that rank induces a clear acquisition--retention frontier. Low-rank QLoRA preserves out-of-domain (OOD) performance but acquires fewer facts, whereas higher ranks improve same-fact paraphrase generalization at an increasing cost in performance on unrelated benchmarks. FFT behaves as a conservative baseline: it retains general capabilities well, but does not reach the highest factual-acquisition regime. Distributional, weight-space, and spectral diagnostics mirror this behavioral trade-off, with higher-rank QLoRA moving farther from the pretrained model. A separate math adaptation experiment shows a weaker frontier, suggesting that the effect is most pronounced when adaptation must install new factual associations rather than reinforce skills already supported by pretraining. Code and data are available at this https URL.

---


### 136. [LMSM: LLM Security Framework Inspired by Linux Security Modules](https://arxiv.org/abs/2608.25697)

**<font color=#1a73e8>作者：</font>** XiuYu Zhang, Bonan Ruan, Junfeng Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed with layered defenses, yet malicious prompts can still bypass them. Interpretability methods can expose model-internal signals along the generation path that could inform enforcement, but these signals are not security controls by themselves. Deployments that adapt them for safety typically couple each signal to its own calibration, policy logic, and intervention code, so each new artifact creates integration work instead of strengthening a shared defense. We present Language Model Security Modules (LMSM), a security framework that adapts the separation behind Linux Security Modules (LSM) to LLM serving. In LMSM, a selected security backend exposes calibrated evidence, a versioned policy evaluates active rules over trusted per-request context, and a separate gate authorizes buffered output release. This design separates mediation correctness from policy effectiveness, and it allows backend, rule, or schedule changes without rebuilding request handling or enforcement. Our prototype shows the separation working in practice: with Hugging Face Transformers and continuously batched vLLM, the same substrate hosts artifact-backed sparse autoencoder (SAE) and transcoder deployments and task-fitted dense probes, preserves request-specific decisions under scheduler churn, and selectively enforces and composes multiple rules per request. On Qwen3-4B, LMSM-Checkpoint reduces HarmBench attack success rate from 39.20% to 3.32%, with XSTest false refusals rising from 2.40% to 4.40%, while retaining 98.14% of the throughput of a matched serving path that performs no monitoring work at 32 active sequences. LMSM gives advances in interpretability and model-internal analysis a common path to runtime enforcement.

---


### 137. [Fairness-Aware Test-Time Prompt Tuning](https://arxiv.org/abs/2608.25707)

**<font color=#1a73e8>作者：</font>** Yoann Launay, Parameswaran Kamalaruban, Tom Kempton 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models have displayed remarkable capabilities in multi-modal understanding and are increasingly used in critical applications where economic and practical deployment constraints prohibit re-training or fine-tuning. However, these models can also exhibit systematic biases that disproportionately affect protected demographic groups and existing approaches to addressing these biases require extensive model retraining and access to demographic attributes. There is a clear need to develop test-time adaptation (TTA) approaches that improve the fairness characteristics of pretrained models under distributional shift. In this paper, we evaluate how episodic TTA affects fairness in CLIP classification under subpopulation shifts and develop FairTPT, a novel fairness-aware episodic TTA method that jointly minimizes target marginal entropy while maximizing spurious marginal entropy through soft-prompt tuning. We find that standard episodic TTA generally exacerbates disparities between majority and minority groups, that blinding a model to spurious attributes without degrading target performance is inherently challenging, and that excessive blinding can lead to catastrophic forgetting. This model collapse can be prevented by monitoring test-time changes in target loss within the linear regime, while still achieving fairness improvements on reactive data and preserving overall performance. FairTPT outperforms all state-of-the-art episodic test-time debiasing methods and establishes a foundation for robust TTA, which is essential for achieving fairness in practice.

---


### 138. [Reassembling Distributed Risk: Trajectory-Conditioned Action Generation for Multi-Turn Agent Safety](https://arxiv.org/abs/2608.25711)

**<font color=#1a73e8>作者：</font>** Yanbo Dai, Zhenlan Ji, Zongjie Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents extend security risks beyond generated text to actions that affect external systems. Under multi-turn decomposition attacks, a harmful objective can be distributed across individually plausible requests and tool calls, becoming apparent only from the accumulated trajectory. Existing defenses either rely on auxiliary online reasoning to recover long-horizon security evidence or assess actions after generation, often incurring additional inference cost or depending on runtime-specific action representations.
We propose \emph{Reassembling Distributed Risk} (ReDiR), a generation-time defense that conditions action generation on trajectory-level security evidence. Before each action, ReDiR compresses the current trajectory into a compact latent safety representation and injects it into the frozen base model. The representation is learned through same-model, cross-view supervision, where safe behavior from an explicit task view provides supervision for recovering distributed safety evidence from the original multi-turn trajectory. This design enables ReDiR to integrate cross-turn security information directly within the generation process without relying on a separate action-level safety module. We evaluate ReDiR on two agent-safety benchmarks across three model families and eight held-out tool domains. ReDiR reduces attack success rates to below 8\%, transfers to unseen tool domains, and preserves benign fidelity with low computational overhead.

---


### 139. [When RAG Fails to Equalize: Geo-bias in Factual Question Answering over Public Companies](https://arxiv.org/abs/2608.25717)

**<font color=#1a73e8>作者：</font>** Abhinav Havaldar, Enrico Santus  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is widely assumed to mitigate factual errors in large language models (LLMs), but it remains unclear whether retrieval uniformly compensates for missing knowledge. We study this question in a controlled factual QA setting over public companies, constructing a benchmark of approximately 2,000 firms across global equity indices. We evaluate six LLMs on four atomic attributes under four conditions: no-context, perfect context, misleading context, and distraction context. We find strong geographic disparities in no-context accuracy, indicating uneven parametric knowledge. While perfect context improves performance, it does not eliminate these gaps: gains are correlated with baseline accuracy, suggesting retrieval effectiveness is coupled to internal representations. Under misleading context, models frequently copy incorrect information. Larger models improve overall performance but do not remove these structural effects. These results challenge the view of RAG as a universal corrective and highlight the interaction between model knowledge, context quality, and entity representation.

---


### 140. [Are LLM-Enhanced GNNs Privacy-Safe?](https://arxiv.org/abs/2608.25727)

**<font color=#1a73e8>作者：</font>** Longzhu He, Zelang Wen, Chaozhuo Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently advanced graph neural networks (GNNs) by enriching node representations with semantic information, giving rise to LLM-enhanced GNNs that achieve substantial performance gains. However, their vulnerability to privacy attacks, in which adversaries infer sensitive information from model outputs, remains largely underexplored. To bridge this gap, we present a systematic evaluation of privacy risks in LLM-enhanced GNNs through a unified framework consisting of five stages: (1) dataset preparation, (2) victim model training, (3) privacy attack, (4) risk assessment, and (5) defense analysis. Specifically, we conduct experiments on six real-world text-attributed graph datasets covering diverse domains. We consider six representative privacy attack methods targeting three fundamental threats, namely link, label, and membership inference, and construct 42 victim model configurations by combining multiple LLM-based feature enhancers with representative GNN backbones. Extensive experiments show that, despite their utility improvements, LLM-enhanced GNNs consistently exhibit increased vulnerability to privacy attacks compared to shallow text representation baselines. Further analysis reveals that semantic enrichment amplifies link-, label-, and membership-related signals in the embedding space, making them more exploitable by inference attacks. Finally, we evaluate differential privacy as a defense strategy and show that, while it can partially mitigate privacy risks, it introduces significant utility degradation, highlighting a fundamental privacy-utility trade-off in LLM-enhanced graph learning. Overall, this work provides a comprehensive understanding of privacy risks in LLM-enhanced GNNs and offers practical insights for developing more secure and trustworthy graph learning systems.

---


### 141. [LongVU-TTT: Causal Test-Time Training for Visual Resampling in Long Video Understanding](https://arxiv.org/abs/2608.25729)

**<font color=#1a73e8>作者：</font>** Mahmoud Ahmed, Sameh Abdulah, Olatunji Ruwase 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video MLLMs must model temporal change before a limited visual-token budget removes most frame evidence. We introduce LongVU-TTT, which inserts a convolutional Test-Time Training (TTT) resampler with causal fast-weight updates between the vision encoder and the LLM. Its grouped 2D fast weights adapt to each video and contextualize frame features before compression, while a hybrid uniform-and-change-aware selector retains explicit visual evidence for downstream reasoning. Under controlled conditions, TTT-Conv improves over TTT-MLP by up to +2.12 and bidirectional Mamba2 by up to +3.04 on MLVU, and it is stronger than attention- and fixed-state recurrent resamplers across three benchmarks. Analysis shows that the fast weights behave as a temporal aggregation state rather than a reliable long-horizon episodic memory: their benefit attenuates as evidence becomes more distant, motivating explicit frame retention. LongVU-TTT processes up to 512 frames before reducing them to 128 LLM frames and achieves competitive performance across five video understanding benchmarks.

---


### 142. [From Verdict to Diagnosis: Attributable Security Review of Pull Requests](https://arxiv.org/abs/2608.25730)

**<font color=#1a73e8>作者：</font>** Zhuo Chen, Boyang Wang, Xiyue Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated code reviewers are increasingly used as gates on pull requests (PRs), yet evaluations measure whether they block a malicious change. A block may be triggered by an unrelated issue rather than the vulnerability that makes the PR unsafe; fixing the reported issue can leave the target defect exploitable. We call this discrepancy the Verdict-Diagnosis (VD) gap.
We present MalPR-Bench, a mechanism-grounded benchmark of 89 malicious PRs and 50 paired benign controls across 44 repositories and eight language families. Each malicious case has a pre-committed rubric specifying the target vulnerability, accepted mechanism descriptions, required repository evidence, and off-target findings receiving no credit. Reviews are scored separately for verdict correctness, target-vulnerability identification, and evidence validation; an attributable block requires all three. We introduce PRGuard, an attributable PR security reviewer that constructs candidate vulnerabilities and validates their premises against repository evidence using deterministic, non-executing tools and bounded retrieval.
Across 31 common-coverage held-out malicious PRs, PRGuard and CodeRabbit produce similar blocking totals (22/31 vs. 24/31), but PRGuard identifies 22 target vulnerabilities versus 16 for CodeRabbit, a 1.38x difference. On 14 absence-type cases, both block 9, while PRGuard identifies 9 targets versus 3. CodeRabbit identifies 16/24 targets when required evidence lies within touched files and 0/7 when validation requires evidence outside them. Finally, PRGuard uncovers twelve previously undisclosed, proof-of-concept-backed vulnerabilities across five projects. PRGuard/DeepSeek and CodeRabbit both block 10/12 discovery PRs, but produce 10/12 and 4/12 attributable blocks, respectively. Thus, verdict-only evaluation can substantially overstate the security value of automated review.

---


### 143. [Pointing the Way, Hiding the Destination: Practical Private Dense Retrieval at Scale](https://arxiv.org/abs/2608.25735)

**<font color=#1a73e8>作者：</font>** Peichun Hua, Danyang Chen, Junan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hosted retrieval-augmented generation (RAG) and semantic search allow users to query valuable provider-held corpora, raising two competing demands: to hide each query and chosen result, yet reveal only the documents that the user is authorized to receive. Existing cryptographic approaches either make this costly by processing the entire corpus for every query, or sacrifice quality for efficiency by scanning a few clusters. We repurpose learned deep hashing as a private filter: a randomized binary code points the provider to a short candidate list, while encrypted reranking and oblivious key transfer protect the precise query and final selection. This shortlist short-circuits full-corpus cryptographic search without sacrificing retrieval quality: with 200-500 candidates, it closely matches full-corpus retrieval across five zero-shot corpora spanning 25K to 5.4M documents. On the full 2.68M-passage NQ corpus over a 10-Gbps link, our protocol only adds 0.73 seconds, or 10 percent, to a 128-token Qwen3-32B RAG pipeline. The released code satisfies directional metric differential privacy (DP) and substantially reduces embedding-inversion and property-inference leakage, demonstrating that a carefully learned shortlist can make private dense retrieval both accurate and practical.

---


### 144. [Why Does Graph Learning Fail to Fully Benefit from a Text Teacher?](https://arxiv.org/abs/2608.25741)

**<font color=#1a73e8>作者：</font>** Fumiaki Kimino, Ryoma Sato  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) are widely used to represent complex interactions and relationships among entities. We investigate a multimodal model that combines two complementary ideas: a self-supervised method that enables a GNN encoder pretrained on one dataset to operate directly on another dataset with a different node-feature dimensionality, without rebuilding the model or realigning the data; and an alternating optimization method that updates a language-model module in an E-step and a GNN module in an M-step, rather than jointly training a large language model and a GNN end to end on a large graph. Despite expectations, the combined model did not sufficiently improve predictive performance. We identify six factors: (1) an external anchor in the E-step has a strength-safety trade-off: a weak anchor has little effect, whereas an overly strong anchor can damage the graph representation; (2) the knowledge of the E-step teacher is not injected directly into the GCN embedding Z; (3) the representation space constructed in the M-step is not optimized for the same objective as the E-step teacher space, resulting in a compromise representation for target classification; (4) GCN propagation averages a node's own textual information with information from its neighbors; (5) cosine alignment does not guarantee axes that are discriminative for classification, so stronger geometric alignment with the E-step text anchor need not sufficiently improve the target decision boundary or classification performance; and (6) the force that preserves the source-side self-supervised geometry in the M-step conflicts with the force that moves the representation toward the E-step teacher. We support these observations through a staged set of experiments that varies the influence of the E-step.

---


### 145. [Beam Search, Self-Consistency, and the Limits of Inference-Time Scaling for Grammar-Constrained Text-to-SQL in Small Language Models](https://arxiv.org/abs/2608.25761)

**<font color=#1a73e8>作者：</font>** Ty Chermsirivatana, John MacCormick  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One common trade-off in the use of large language models involves reducing the size of the model while increasing the amount of computation at inference time, for example by using a wider beam search. In this paper, we examine the constrained case of this "model size vs. inference compute" trade-off, in which the model outputs are constrained by a strict grammar at inference time. Our results demonstrate that the constrained trade-off behaves differently from the unconstrained trade-off. We investigate the task of converting a prose query into an equivalent SQL query (text-to-SQL). Performance is evaluated on the Spider text-to-SQL benchmark, using the Qwen2.5-Instruct model family ranging in size from 0.5B to 7B parameters, all at 4-bit precision. We experiment with two approaches to varying inference compute: (i) beam search with a variable number of beams; and (ii) sample+vote, i.e., sampling several constrained outputs and then voting on their execution results, where the number of samples is varied. On the 1034-example development set, we find that: (a) both beam search and sample+vote improve accuracy, especially on smaller model sizes; (b) the "model size vs.\ inference compute" trade-off is not advantageous in this experiment, because moving to a larger model size typically results in higher accuracy than increasing inference compute on the same model size; (c) beam search outperforms sample+vote at a matched inference budget. This latter result is of particular interest since it contrasts with the findings of the unconstrained trade-off.

---


### 146. [HypoForge: A Self-Improving Multi-Agent Framework for Automated Hypothesis Generation and Testing via Scientific Skill Learning](https://arxiv.org/abs/2608.25770)

**<font color=#1a73e8>作者：</font>** Ziqing Qian, Jiaying Lei, Yifang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have enabled AI scientist systems to automate scientific discovery, yet existing approaches most rely on static prompting or fixed workflows and fail to accumulate experience for continual improvement. We propose HypoForge, an experience-guided multi-agent framework that learns reusable scientific skills for automated hypothesis generation and hypothesis testing. HypoForge is built on the observation that these two stages involve different supervision signals. For hypothesis generation, where explicit feedback is unavailable, HypoForge adopts an adversarial generator--discriminator mechanism to improve reasoning through comparative critique. For hypothesis testing, where empirical feedback is available, HypoForge learns testing skills from execution outcomes and ground-truth results. By matching skill learning strategies with stage-specific supervision, HypoForge enables continual improvement without fine-tuning foundation models. Experiments on hypothesis generation and testing benchmarks show that HypoForge consistently outperforms existing AI scientist frameworks and skill-level variants. Further analysis demonstrates the effectiveness of the proposed stage-specific skill learning paradigms.

---


### 147. [Large Language Model Few-Shot Prompting with Dilemma Training Outperforms Human Surrogates in Predicting Patient Preferences](https://arxiv.org/abs/2608.25771)

**<font color=#1a73e8>作者：</font>** Natasha Ureyang, Sebastian Porsdam Mann, Yuxin Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In serious illness, human surrogates often struggle to accurately predict patient preferences (68% accuracy), causing decision conflict. Personalized Patient Preference Predictor (P4) agents offer a potential solution, but prior prototypes treat values as static ratings, ignoring the contextual, situation-dependent nature of medical choices. Grounded in the 'logic of care', we present P4-DT (Dilemma Training), a P4 agent that constructs a patient decision policy by engaging users with varied medical dilemmas, eliciting individual preference reasoning through bi-directional training. In a study with 12 patient-surrogate dyads, P4-DT predicted patient treatment choices with 81.7% accuracy, significantly exceeding chance (OR = 5.61 [2.03, 15.51], p < .001) and outperforming both unassisted surrogates (55.0%; OR = 3.67 [1.59, 8.47], p = .002) and surrogates assisted by P4-DT (61.7%). Comparative prompt analyses showed that incorporating contextual scenario decisions and open-ended text improved accuracy by 15.0 percentage points over initial values ratings alone. We discuss implications for further testing and designing of context-aware AI agents that embody richer human experience to partner in complex decision-making.

---


### 148. [Drift-Aware Multimodal User Representation Learning via Multi-Scale Temporal Modeling and Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.25773)

**<font color=#1a73e8>作者：</font>** Ziqing Qian, Haohang Chen, Shengqi Dang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding user preferences from noisy and temporally evolving social media behaviors is fundamentally challenging due to interest drift, where user preferences shift across time and exhibit both multi-scale temporal patterns and diverse co-existing interests. To address this, we propose DUMoE, a unified framework for drift-aware multimodal user representation learning. Our model consists of (i) a temporal dynamics-aware backbone that captures and integrates static profiles, short-term behavioral signals, and long-term dependencies into a coherent representation, and (ii) a sparse mixture-of-experts (MoE) interest adapter that disentangles multiple latent interests via expert specialization and adaptive routing. Each expert models a distinct interest subspace, while a gating network dynamically selects and aggregates a sparse subset of relevant experts for each user. To enable stable and effective optimization, we further introduce a three-stage training strategy that decouples backbone learning, expert specialization, and gating optimization. Extensive experiments on real-world social media datasets show that DUMoE consistently outperforms state-of-the-art methods on both user interest prediction and interaction prediction tasks.

---


### 149. [ToST: A Tree-of-Thought Socratic Teaching Framework for Multi-Path Guidance and Parallel Thinking](https://arxiv.org/abs/2608.25775)

**<font color=#1a73e8>作者：</font>** Feng Ling, Heng Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit strong problem-solving abilities, positioning them as promising agents for Socratic teaching to guide students through step-by-step heuristic questioning. However, existing approaches typically adopt a one-problem-one-solution paradigm, restricting the teaching guidance to a single linear reasoning path. This design limits instructional flexibility, weakens error recovery, and restricts students' ability to engage in parallel thinking to explore multiple valid solutions. To overcome these, we propose ToST, a Tree-of-Thought Socratic Teaching framework that explicitly supports multi-path guidance under a one-problem-multiple-solutions paradigm. ToST employs Parallel Sowing, a parallel-thinking-oriented questioning strategy to encourage students to approach problems from diverse perspectives, and a Multi-Path Adaptive Guidance mechanism to provide more robust and non-linear instructions across alternative solution trajectories. Concurrently, to fill the void in systematically evaluating such non-linear instructional capabilities, we advance the task of multi-path Socratic guidance by establishing MPSG-Bench, a comprehensive benchmark that includes a dataset of 31K multi-path teaching dialogues and a five-dimensional evaluation framework grounded in the SOLO (Structure of Observed Learning Outcomes) theory to assess parallel-thinking guidance. Experimental results demonstrate that ToST significantly enhances guidance success rates while empowering students to navigate and explore multiple solution paths more effectively under both automatic and human metrics.

---


### 150. [LocalLSTC: A Long Short-Term Control Architecture for Locally Deployed GUI Agents](https://arxiv.org/abs/2608.25777)

**<font color=#1a73e8>作者：</font>** Weiming Li, Helen Paik, Yulei Sui  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern GUI-agent frameworks achieve strong desktop task performance with frontier API models, yet persistent control information often remains implicit in growing interaction trajectories. At each step, the planner reconstructs the active task stage, accumulated evidence, and runtime feedback before deciding the next action. This dependence becomes more pronounced under weaker local reasoning backbones. Across four representative state-of-the-art frameworks, replacing GPT-5 with Qwen3.5-9B reduces average OSWorld SR-100 from 60.9\% to 37.7\%. Trajectory annotation further identifies at least one control failure in 91.6\% of failed trajectories. To address this problem, we introduce LocalLSTC, a training-free architecture that organizes control by temporal scope, maintaining persistent cross-step state to guide short-term execution commitments. Long-Term Control maintains the active subgoal, subgoal-aligned evidence, and runtime feedback across interactions, while Short-Term Execution realizes bounded commitments for the current step. Long-to-Short Planning forms each commitment from persistent state, and Short-to-Long Control integrates execution outcomes back into that state for progress assessment, recovery, and termination. With Qwen3.6-27B, LocalLSTC reaches 64.7\% SR-100 on OSWorld and 65.3\% on WindowsAgentArena, outperforming the strongest prior local results on both benchmarks. Ablations further support contributions from mechanisms on both sides of execution. These findings identify temporal organization of control information as a distinct architectural dimension for locally deployed GUI agents.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-209](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
