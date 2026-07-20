# 🧠 大模型相关研究 | 2026年07月20日

> 本类共 **119** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-119**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-119**

---

### 101. [AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation Learning](https://arxiv.org/abs/2607.15094)

**<font color=#1a73e8>作者：</font>** Sarthak Jain, Qiran Hu, Zhen Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal models such as CLIP learn a shared embedding space for cross-modal retrieval, but continual adaptation to sequentially arriving data can disrupt the cross-modal alignment acquired from earlier phases. Conventional continual-learning methods return a single checkpoint, which commits every retrieval direction to the same stability-plasticity trade-off. We propose AlphaWiSE, a post-hoc weight-space interpolation method that composes two frozen source checkpoints. For each aligned parameter tensor identified by its checkpoint key, AlphaWiSE fits one scalar interpolation coefficient shared by all tensor entries. The coefficients are fitted on a smaller exemplar memory and used to materialize one interpolated checkpoint. The deployed model has the same architecture and parameter count as either source checkpoint, which does not require additional inference time. Extensive experiments on audio-image-text retrieval show consistent improvements over strong continual-learning baselines across multiple retrieval directions and evaluation metrics.

---


### 102. [Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents](https://arxiv.org/abs/2607.15095)

**<font color=#1a73e8>作者：</font>** Dylan Van Mulders, Matthias Bogaert, Dirk Van den Poel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The formation of political coalitions is a complex negotiation driven by both concrete policy objectives and deep-seated ideological convictions. While Large Language Models (LLMs) open new avenues for computational political science, the neutrality and helpfulness biases instilled by Reinforcement Learning from Human Feedback (RLHF) prevent them from sustaining steadfast partisan behaviour. We present a multi-agent framework that reconciles factual grounding with ideological alignment by combining Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and Retrieval-Augmented Generation (RAG): DPO instils aggressive party-specific personas, while a per-party RAG pipeline keeps each agent bounded to its official manifesto. We operationalize the framework on the 2019 Flemish election, deploying the partisan agents in a hub-and-spoke negotiation arbitrated by a formateur. To make the emergent negotiation interpretable, we introduce a Multi-Layered Information Lineage Topology (MILT) that traces every clause in the final agreement back to its manifesto origin and classifies it into five provenance states, a Coalition Influence Score (CIS) that aggregates these traceable contributions to identify which party shaped the agreement, and a real-world grounding pass that benchmarks each simulated provision against the historically adopted coalition agreement. Across three independent simulations the framework yields a stable winner and ranking (N-VA ahead of CD\&V and Open Vld), and manifesto-anchored lineage reliably predicts real-world materialization whereas hallucinated content does not. The result is a transparent, scalable testbed for the ex-ante exploration of party compatibility and formateur-mediated compromise.

---


### 103. [Long-Context Fine-Tuning with Limited VRAM](https://arxiv.org/abs/2607.15105)

**<font color=#1a73e8>作者：</font>** Vladimir Fedosov, Aleksandr Sazhin, Artemiy Grinenko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning reduces model and optimizer memory, but dense attention still makes long training sequences expensive. We combine Hierarchical Global Attention (HGA) with segment-wise backpropagation and tiered KV storage. Only the active segment remains differentiable in VRAM; older KV is detached into RAM or NVMe, and HGA loads a bounded set of exact historical tokens for each query block. On Qwen3-8B with 4-bit QLoRA and PG19, dense training on a 16 GB Quadro RTX 5000 fits 2,048 tokens but fails at 4,096, whereas HGA reaches 16,384 tokens with 15.28 GB peak VRAM. Under evaluation the same adapter runs through 131,072 tokens on this card; VRAM is not constant but grows gently with the resident chunk summaries, so RAM and NVMe capacity set the practical limit beyond these lengths. At the shared 2K training length, HGA-trained and dense-trained adapters obtain 2.7405 and 2.7383 nat under the same dense-attention readout, while the stock model obtains 2.9541. At this boundary HGA training is already marginally faster (217.75 vs. 207.02 tokens/s), and the HGA-to-dense throughput ratio improves from 1K to 2K; because HGA keeps the attended historical set per token approximately constant while dense work per token grows, we expect this lead to widen as context grows. Dense attention is used for the main quality and retrieval comparisons so that they measure the learned weights and remain compatible with standard generation frameworks. HGA can also be used for retrieval and generation; an optimized production-grade serving implementation is under development.

---


### 104. [Concept-Guided Spatial Regularization for World Models in Atari Pong](https://arxiv.org/abs/2607.15142)

**<font color=#1a73e8>作者：</font>** Yukuan Lu, Zaishuo Xia, Weyl Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are usually evaluated as components of model-based reinforcement learning (MBRL) systems, while the world models themselves are rarely studied in isolation.
We examine five representative visual world-model agents in Atari Pong: DreamerV3, DIAMOND, TWISTER, Simulus, and STORM. After reproducing their training pipelines and matching the reported agent performance, we freeze the learned world models and evaluate them with a closed-loop rollout diagnostic: a policy trained separately from the corresponding MBRL agent interacts with each frozen model, and the generated video trajectories are inspected for visual and dynamical errors. Across all five models, the rollouts contain clear failures, including ball disappearance, incorrect ball motion, and invalid ball-paddle interactions.
Beyond visual trajectories, we further evaluate them with pixel-space zero-shot MBRL, where a new policy is trained entirely inside a frozen world model and then evaluated in the real environment. Across all five models, the resulting policies substantially underperform those produced by the corresponding original MBRL training pipelines. The gap is particularly large for DreamerV3, whose mean return drops from -5.5 to -20.9, near the minimum Pong return of -21.
We hypothesize that insufficient modeling of task-critical concepts, such as the ball in Pong, may contribute to these failures. We therefore propose Concept-Guided Spatial Regularization (CGSReg), an auxiliary pixel reconstruction loss applied to segmented concept regions. Experiments show that CGSReg improves both closed-loop rollouts and pixel-space zero-shot MBRL in DreamerV3, DIAMOND, and TWISTER. Its effects vary across the remaining models and evaluation metrics, indicating that CGSReg alone does not address all world-model bottlenecks.

---


### 105. [Grokipedia vs Wikipedia: An LLM-Based Audit of Political Neutrality along Ideologies](https://arxiv.org/abs/2607.15146)

**<font color=#1a73e8>作者：</font>** Filippos Vlahos, Guillaume Bied, Tijl De Bie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online encyclopedias shape political opinion and, through it, democratic discourse. In late 2025, Grokipedia was released, an encyclopedia written entirely by the LLM Grok. One motivation behind the project was to provide an unbiased alternative to Wikipedia, which has faced accusations of "left-wing" and "liberal" bias. But does an encyclopedia written by an LLM deliver greater neutrality, or does it simply embed a different ideology? We conduct a large-scale political bias study on Grokipedia and Wikipedia, analysing 1,394 article pairs describing members of government for neutrality along nine expert-coded ideology dimensions employing four LLM judges, Grok, Claude, Mistral, and DeepSeek. As the LLMs could themselves be biased, we also investigate patterns in their judgments. We find all LLM-judges, including Grok, to rate Grokipedia less neutral than Wikipedia. Both encyclopedias are rated as portraying politicians favourably overall, but towards different ideological groups. Grokipedia particularly favours economically right-wing politicians and penalises socially liberal ones, while Wikipedia is rated as favourably biased towards the latter.

---


### 106. [Linear representations of grammaticality in neural language models](https://arxiv.org/abs/2607.15175)

**<font color=#1a73e8>作者：</font>** Jane Li, Najoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whether neural language models (NLMs) possess the ability to distinguish strings on the basis of their grammaticality remains a debated topic in the computational linguistics literature. Existing evidence has largely relied on probability-based measures, testing whether models assign higher probabilities to grammatical than ungrammatical strings. However, probability comparisons have been criticized as a measure for grammatical knowledge based on the assumption that grammaticality is inherently entangled with likelihood. Model-assigned probability is a function of many related sentence properties, such as lexical frequency, plausibility, and world knowledge. In this work, we move beyond probability-based evaluations and investigate whether grammaticality is encoded in the internal representations of NLMs. Using mass-mean probing, we test whether grammatical and ungrammatical sentences are systematically separated in representational space. We further examine the extent to which these representations are independent of sentence properties that are correlated with grammaticality, as well as their generalization across grammatical phenomena and languages. Our results provide evidence that grammaticality is robustly encoded in sentence representations of a wide range of pretrained NLMs, yielding clear representational separation on the dimension of grammaticality that cannot be fully explained by alternative sentence-level factors. Moreover, this encoding generalizes across a broad range of grammatical phenomena and to some degree, across languages, suggesting that grammaticality constitutes a coherent representational dimension in contemporary NLMs. These findings contribute new evidence to debates about the nature of syntactic knowledge in language models and offer a complementary framework for evaluating grammatical competence that is not dependent on string probabilities alone.

---


### 107. [Benchmarking Multimodal Large Language Models for Scientific Visualization Literacy](https://arxiv.org/abs/2607.15176)

**<font color=#1a73e8>作者：</font>** Patrick Phuoc Do, Chau M. Ta, Chaoli Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly used to interpret visualizations, yet current evaluations remain largely chart-centric and provide limited evidence of understanding of scientific visualization (SciVis). We benchmark six MLLMs on the scientific visualization literacy assessment test, a standardized SciVis literacy assessment comprising 49 items based on 18 scientific visualizations and illustrations, spanning 8 techniques and 11 task types. We evaluate three closed-source and three open-source models under a closed-world protocol and compare their performance using data from 485 human participants. Results show that current MLLMs do not exhibit uniform SciVis literacy. Gemini is the strongest model overall, exceeding the human mean across the evaluated subsets, whereas the open-source models remain below the human baseline. Performance is highly uneven across techniques and tasks: models perform best on scientific illustration, search, and spatial understanding, but struggle on texture-based and integration-based visualizations and on quantitative estimation. Error analysis reveals recurring failures in fine-grained quantitative estimation, flow-direction interpretation, and grounded encoding interpretation. These findings position SciVis literacy as a necessary benchmark dimension for evaluating multimodal AI systems. Our code and model outputs are publicly available at this https URL.

---


### 108. [Mask-Aware Policy Gradients for Diffusion Language Models](https://arxiv.org/abs/2607.15200)

**<font color=#1a73e8>作者：</font>** Haran Raajesh, Kulin Shah, Adam Klivans 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has proven effective for improving reasoning in large language models, but extending it to Masked Diffusion Language Models (MDLMs) remains challenging due to the intractability of the log-likelihood estimation. Existing approaches approximate this log-likelihood by modeling only the token predictions, ignoring the order in which positions are unmasked during generation. We observe that MDLM generation involves two decisions at each step: what tokens to place at each masked position and which positions to remask. We formalize this as a two-stage action MDP, showing that the policy gradient naturally decomposes into a token term and a masking term. Combining optimization of both terms leads to state-of-the-art outcomes on mathematical reasoning and coding benchmarks, with scores of 87.1% on GSM8K and 53.4% on MBPP.

---


### 109. [Self-Evolving Human-Centered Framework for Explainable Depression Symptom Annotation](https://arxiv.org/abs/2607.15202)

**<font color=#1a73e8>作者：</font>** Hoang-Loc Cao, Van Pham, Truong Thanh Hung Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Annotation quality is a major bottleneck in building reliable and explainable artificial intelligence (XAI) systems for mental health research. In depression-related datasets, labels are often assigned without structured evidence, symptom-level justification, or traceable alignment with the criteria of the Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR), limiting both transparency and downstream model interpretability. We propose a self-evolving, expert-in-the-loop annotation framework for Major Depressive Disorder (MDD) that combines large language model (LLM)-assisted labeling with expert verification. The framework is intended to support the construction of explainable, DSM-5-TR-aligned datasets rather than to perform clinical diagnosis. It operates in three stages: candidate evidence selection from textual records, criterion-level DSM-5-TR analysis, and case-level synthesis that produces label-level diagnostic and severity annotations. A dual-memory architecture, composed of Example Memory and Reflection Memory, is designed to internalize expert feedback and iteratively improve future annotations without retraining. We describe this mechanism and leave its evaluation across multiple feedback cycles to future work. In addition to final labels, the framework exports clinical evidence, reasoning traces, and edit histories, enabling comprehensive auditability. In a pilot study using expert-reviewed samples, the proposed approach improves annotation consistency and explainability while reducing manual revision effort.

---


### 110. [Symbal: Detecting Systematic Misalignments in Model-Generated Captions](https://arxiv.org/abs/2607.15216)

**<font color=#1a73e8>作者：</font>** Maya Varma, Jean-Benoit Delbrouck, Sophie Ostmeier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) often introduce errors when generating image captions, resulting in misaligned image-text pairs. Our work focuses on a class of captioning errors that we refer to as systematic misalignments, where a recurring error in MLLM-generated captions is closely associated with the presence of a specific visual feature in the paired image. Given a vision-language dataset with MLLM-generated captions, our aim in this work is to detect such errors, a task we refer to as systematic misalignment detection. As our first key contribution, we present Symbal, which utilizes a structured, dual-stage setup with off-the-shelf foundation models to identify systematic misalignments and summarize results in natural language. As our second key contribution, we introduce SymbalBench, a benchmark designed to evaluate automated methods on our proposed task. SymbalBench consists of 1.7 million image-text pairs from two domains (natural and medical images), organized into 420 vision-language datasets with annotated systematic misalignments. Symbal exhibits strong performance on this benchmark, correctly identifying systematic misalignments in 63.8% of datasets, a nearly 4x improvement over the closest baseline. We supplement our evaluations on SymbalBench with real-world evaluations, showing that (1) Symbal can accurately surface systematic misalignments in captions generated by four MLLMs and (2) Symbal is a powerful tool for auditing off-the-shelf image-caption datasets. Ultimately, our novel task, method, and benchmark can aid users with auditing MLLM-generated captions and identifying critical errors, without requiring access to the underlying MLLM. Code is available at this https URL.

---


### 111. [When Words Are Safe But Actions Kill: Probing Physical Danger Beyond Text Safety in Hidden-State Risk Space](https://arxiv.org/abs/2607.15218)

**<font color=#1a73e8>作者：</font>** Weimeng Wang, Ziqiang Wang, Zihang Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly serve as high-level planners for embodied agents, where linguistically benign instructions can become unsafe once grounded in the physical world. We study whether this physically grounded danger is the same safety problem as ordinary text-level content danger. Through hidden-state direction analysis and random-split null tests, we show that content danger (CD) and physical danger (PD) form separable signals in LLM representations across Qwen2.5-3B/7B/14B/32B, Phi-3.5 and SmolLM2. Building on the CD/PD separability, we propose PRISM, a single-layer L2-regularized logistic probe over full hidden states. PRISM achieves 86.2--87.7\% accuracy on SafeAgentBench with 11.7--13.7\% FPR, while same-scale LLM judges over-block safe tasks at 24.7--39.0\% FPR. We further introduce PhysicalSafetyBench-1K (PSB-1K), a contrastive benchmark of 1{,}000 physical-risk pairs without direct harm keywords, to test whether methods detect physically grounded danger rather than explicit unsafe wording. On PSB-1K, PRISM reaches 99.6\% accuracy and 0.7\% FPR, whereas a Qwen2.5-3B judge rejects 67.8\% of safe tasks. PRISM also replicates on SafeText and EARBench, supporting hidden-state probing as a representation-level method for physical safety beyond text moderation.

---


### 112. [In-Place Tokenizer Expansion for Pre-trained LLMs](https://arxiv.org/abs/2607.15232)

**<font color=#1a73e8>作者：</font>** Jimmy T.H. Smith, Tarek Dakhran, Alberto Cabrera 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A tokenizer fixed at the start of pre-training allocates vocabulary in proportion to the pre-training corpus, reflecting the deployment priorities at that time. When those priorities shift, languages added later are split into many more tokens per word, which can raise latency, compute, and energy consumption for users of those languages. Cloud models can afford a broad vocabulary because the embedding and LM-head matrices are a small fraction of their parameters. On a compact model those matrices are a material share of per-token decode bandwidth, so on-device models ship small vocabularies and accept fragmentation outside a fixed language set. We present tokenizer expansion, an in-place recipe for upgrading a pre-trained model's tokenizer when the model producer controls its design. We continue the existing tokenizer's BPE merges on a multilingual corpus, so most source tokens carry over unchanged as single tokens and every new token has an exact decomposition into source tokens. We copy the carried-over embedding rows unchanged and initialize new rows as the mean of their source sub-token embeddings. A two-stage adaptation, embedding-only training then full-model continued pre-training, recovers source-checkpoint quality. We apply the recipe to a continued pre-trained checkpoint of LFM2-8B-A1B, an 8B-parameter Mixture-of-Experts model, to help produce LFM2.5-8B-A1B with a 128K tokenizer. The expanded tokenizer encodes Hindi and Vietnamese in roughly $2.4\times$ and $2.6\times$ fewer tokens than the source (up to $4.0\times$ on Thai). Combining these reductions with the measured per-token cost of the larger vocabulary, we estimate a $2.2$-$3.7\times$ per-character decode speedup for these languages across our reference devices. We release the model weights and the expanded tokenizer, and report the negative findings that shaped the recipe.

---


### 113. [TikStance: A Multimodal and Hierarchical Dataset for Multi-target Stance Analysis in TikTok Political Conversations](https://arxiv.org/abs/2607.15240)

**<font color=#1a73e8>作者：</font>** Yazhi Zhang, Fuqiang Niu, Bowen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Political discourse has increasingly moved to short-video platforms, yet computational analysis of such content remains constrained by the scarcity of datasets that jointly preserve audiovisual information and hierarchical conversations. Here we present TikStance, a multimodal and context-aware dataset comprising 161 videos and 13,876 comments from TikTok, designed for stance detection in political discussions. The dataset covers three major political figures in the 2024 U.S. election cycle--Donald Trump, Joe Biden, and Kamala Harris--with content collected between September 2023 and January 2025. Each discussion unit links a host video and its metadata to a parent-linked comment tree, enabling stance analysis within both audiovisual and conversational context. Each item was independently labeled by three annotators using a three-class scheme (Favor, Against, None) for video-to-target and comment-to-target stance; items with disagreement were re-annotated, and the final Krippendorff's \(\alpha\) reached 0.743, 0.723, and 0.722 for the Trump, Biden, and Harris subsets, respectively. Descriptive analysis further reveals target-dependent differences in stance distributions and conversational depth, with nested replies accounting for 23.3\% of all comments. By combining multi-target coverage, hierarchical conversations, and reliable multi-level human annotations, TikStance supports research in multimodal stance detection, political communication, computational social science, and context-aware natural language processing.

---


### 114. [Beyond the Leaderboard: Design Lessons for Trustworthy Multimodal VQA](https://arxiv.org/abs/2607.15241)

**<font color=#1a73e8>作者：</font>** Sushant Gautam, Vajira Thambawita, Michael A. Riegler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Healthcare multimodal AI must combine visual and textual evidence while remaining reliable and interpretable. Using MediaEval Medico 2025 as a retrospective GI endoscopy case study, we analyze design choices across nine documented systems for question answering and explanation quality. Parameter-efficient adaptation of pretrained backbones provides strong challenge performance, but answer-level gains do not consistently translate into faithful and complete clinical reasoning. Methods enforcing structured reasoning and explicit grounding show more reliable behavior across heterogeneous question types, although the evidence is correlational rather than ablation-based. These results motivate evaluation beyond lexical overlap, standardized evidence-linked explanations, leakage-aware data governance, and lightweight robustness and calibration checks. The findings support trustworthy multimodal healthcare AI based on data fusion, explainability, and resilient evaluation.

---


### 115. [ARMOR++: Agentic Orchestration of a Multi-Domain Primitive Set for Transferable Attacks on Deepfake Detectors](https://arxiv.org/abs/2607.15246)

**<font color=#1a73e8>作者：</font>** Christos Korgialas, Gabriel Lee Jun Rong, Dion Jia Xu Ho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The reliability of deepfake detectors frequently degrades under black-box adversarial transfer, as these models often rely on fragile, architecture-dependent forensic cues. Existing transfer attacks often lack semantic awareness and struggle to maintain effectiveness under strict no-query constraints, particularly when perturbations are transferred from convolutional surrogates to transformer-based targets. To address these limitations, this paper introduces ARMOR++, a robust multi-agent framework designed for high-transferability deepfake evasion. The framework leverages the Qwen2.5-VL Vision-Language Model (VLM) to supply spatial semantic priors, while the Qwen3 Large Language Model (LLM) orchestrates primitive selection, adaptive hyperparameter reparameterization, and entropy-regularized perturbation mixing. By integrating five complementary primitives, spanning dense optimization, saliency-based methods, spatial transformations, frequency-domain perturbations, and block-structured modifications, ARMOR++ effectively targets heterogeneous inductive biases. Rigorous evaluation on the AADD-2025 benchmark demonstrates that ARMOR++ significantly outperforms existing agentic and non-agentic baselines across both low- and high-quality image regimes. Statistical analysis confirms a substantial gain in blind-target Attack Success Rate (ASR) over the state-of-the-art agentic baseline, with further performance advantages evidenced against non-agentic benchmarks and under robust defensive configurations. These findings highlight a significant residual reliability gap in current deepfake detector deployments and demonstrate the efficacy of agentic orchestration in identifying latent vulnerabilities.

---


### 116. [AutoSynthesis: An agentic system for automated meta-analysis](https://arxiv.org/abs/2607.15247)

**<font color=#1a73e8>作者：</font>** Moein Taherinezhad, Sebastian Maier, Gerardo Vitagliano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evidence synthesis is crucial for turning primary research into reliable knowledge for science, medicine, education, and policy. Yet, quantitative evidence synthesis remains largely manual and difficult to scale. Here, we introduce AutoSynthesis, an end-to-end multi-agent system for automated meta-analysis. Given a research question in natural language, AutoSynthesis formulates a search strategy, retrieves scientific literature, screens candidate studies, assesses full-text eligibility, extracts quantitative statistics, computes standardized effect sizes, and finally performs random-effects meta-analysis. AutoSynthesis further supports heterogeneity analysis to examine how effect sizes vary across moderators, as well as risk-of-bias assessment. As output, AutoSynthesis produces a transparent report aligned with PRISMA guidelines. In our application, AutoSynthesis screened over 28 studies and extracted more than 20 quantitative claims. The pooled effect estimates produced by AutoSynthesis are similar to Hedges' $g$ of expert-conducted meta-analyses, indicating close agreement with manual evidence synthesis. Together, these results show that AutoSynthesis can make quantitative evidence synthesis more scalable, thereby supporting evidence-based decision-making across disciplines.

---


### 117. [teLLMe Why (Ain't Nothing but a Jam): Exploratory Causal Analysis of Urban Driving Data](https://arxiv.org/abs/2607.15254)

**<font color=#1a73e8>作者：</font>** Qiwei Li, Jorge Ortiz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traffic agencies now have access to large volumes of video-derived data for studying safety and congestion. Most of these data are observational and collected without interventions, which makes causal questions such as "How would rain change traffic density?" difficult to answer. We present teLLMe, a system for exploratory causal analysis of urban driving datasets. The system starts from a structured event table built from dashcam annotations and combines causal structure learning with the PC algorithm, bootstrap-based stability checks, and query-specific effect estimation using linear regression and DoWhy. Natural-language questions are mapped to structured causal queries through a schema-aware LLM, enabling users to specify treatments, outcomes, and subpopulations. teLLMe returns a "Causal Card" that summarizes effect estimates, adjustment sets, DAG support, and assumptions, followed by a short natural-language explanation. Case studies on BDD-derived traffic events show that the system can surface plausible relationships involving weather, peak hours, and traffic density, while making uncertainty and modeling choices explicit. The system is designed as a tool for hypothesis generation and expert reasoning rather than a source of definitive causal claims.

---


### 118. [MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators](https://arxiv.org/abs/2607.15273)

**<font color=#1a73e8>作者：</font>** Yushi Huang, Xiangxin Zhou, Jun Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MeanFlow generators achieve fast few-step sampling by predicting average velocities over time intervals, making them attractive for efficient generation. Reinforcement learning (RL) has become a powerful way to align diffusion and flow models with human preferences and task-specific objectives. In particular, DiffusionNFT offers an efficient forward-process RL framework that does not require reverse-process trajectories or likelihood estimation. However, applying such RL methods to MeanFlow remains underexplored. DiffusionNFT optimizes instantaneous velocities, whereas MeanFlow samples with average velocities. To bridge this gap, we introduce MeanFlowNFT. Inspired by the MeanFlow identity, which bridges average and instantaneous velocities, we construct an induced instantaneous-velocity predictor. We apply the DiffusionNFT objective to this predictor, making reward optimization well-defined for MeanFlow. Sampling remains based on the average velocity, preserving MeanFlow's fast few-step generation. We further prove that MeanFlowNFT inherits DiffusionNFT's strict policy-improvement guarantee. Experiments on image and video generation show that MeanFlowNFT consistently improves baselines. Moreover, it outperforms prior state-of-the-art RL-tuned few-step generators on most metrics ($6$ of $8$ on SD3.5-M), and can even surpass multi-step RL-tuned diffusion while using only a few sampling steps. For instance, on Wan 2.1, $4$-step MeanFlowNFT reaches a VBench score of $84.33$, surpassing $50$-step LongCat-Video RL ($82.57$).

---


### 119. [Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models](https://arxiv.org/abs/2607.15277)

**<font color=#1a73e8>作者：</font>** Patrik Wolf, Thomas Kleine Buening, Andreas Krause 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning is commonly interpreted as a form of conditional inference, in which the prompt specifies a context and the model's output is treated as an estimate of the corresponding conditional distribution. If this interpretation holds, then LLM estimates should satisfy basic probabilistic identities. In particular, the law of total probability asserts that prior-weighted conditional distributions aggregate into population-level marginals over any valid partition of the population. In this work, we investigate to what extent LLM estimates adhere to this self-consistency principle. We use binary trees as an evaluation scaffold to recursively partition a population into increasingly fine-grained subpopulations. We then prompt LLMs with verbalized subpopulation descriptions in context, aggregate the resulting estimates back into population-level estimates, and compare them across partitions of varying granularity. Applying this protocol across problem domains and state-of-the-art frontier models, we show widespread violations of basic consistency properties. An in-depth study of persona prompting reveals a pattern we call the macro fallacy: estimates reconstructed from more fine-grained subpopulation responses are often better aligned with human reference data than direct population-level estimates. This effect persists across variations in tree structure and estimation task, and can be partially recovered through implicit prompting. Together, these findings suggest that models possess relevant subpopulation knowledge but do not reliably propagate it into aggregate estimates. This gap establishes statistical self-consistency as an unsaturated, reference-free criterion for evaluating LLMs.

---


> [!TIP]
> 当前位于：**101-119**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-119**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
