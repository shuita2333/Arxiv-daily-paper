# 🧠 大模型相关研究 | 2026年04月23日

> 本类共 **132** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-132**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-132**

---

### 101. ['The Order in the Horse's Heart': A Case Study in LLM-Assisted Stylometry for the Discovery of Biblical Allusion in Modern Literary Fiction](https://arxiv.org/abs/2604.19447)

**<font color=#1a73e8>作者：</font>** Ewan Cameron  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a dual-track pipeline for detecting biblical allusions in literary fiction and apply it to the novels of Cormac McCarthy. A bottom-up embedding track uses inverse document frequency to identify rare vocabulary shared with the King James Bible, embeds occurrences in their local context for sense disambiguation, and passes candidate passage pairs through cascaded LLM review. A top-down register track asks an LLM to read McCarthy's prose undirected to any specific biblical passage for comparison, catching allusions not distinguished by word or phrase rarity. Both tracks are cross-validated by a long-context model that holds entire novels alongside the KJV in a single pass, and every finding is checked against published scholarship. Restricting attention to allusions that carry a textual echo--shared phrasing, reworked vocabulary, or transplanted cadence--and distinguishing literary allusions proper from signposted biblical references (similes naming biblical figures, characters overtly citing scripture), the pipeline surfaces 349 allusions across the corpus. Among a target set of 115 previously documented allusions retrieved through human review of the academic literature, the pipeline independently recovers 62 (54% recall), with recall varying by connection type from 30% (transformed imagery) to 80% (register collisions). We contextualise these results with respect to the value-add from LLMs as assistants to mechanical stylometric analyses, and their potential to facilitate the statistical study of intertextuality in massive literary corpora.

---


### 102. [Four-Axis Decision Alignment for Long-Horizon Enterprise AI Agents](https://arxiv.org/abs/2604.19457)

**<font color=#1a73e8>作者：</font>** Vasundra Srininvasan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon enterprise agents make high-stakes decisions (loan underwriting, claims adjudication, clinical review, prior authorization) under lossy memory, multi-step reasoning, and binding regulatory constraints. Current evaluation reports a single task-success scalar that conflates distinct failure modes and hides whether an agent is aligned with the standards its deployment environment requires. We propose that long-horizon decision behavior decomposes into four orthogonal alignment axes, each independently measurable and failable: factual precision (FRP), reasoning coherence (RCS), compliance reconstruction (CRR), and calibrated abstention (CAR). CRR is a novel regulatory-grounded axis; CAR is a measurement axis separating coverage from accuracy. We exercise the decomposition on a controlled benchmark (LongHorizon-Bench) covering loan qualification and insurance claims adjudication with deterministic ground-truth construction. Running six memory architectures, we find structure aggregate accuracy cannot see: retrieval collapses on factual precision; schema-anchored architectures pay a scaffolding tax; plain summarization under a fact-preservation prompt is a strong baseline on FRP, RCS, EDA, and CRR; and all six architectures commit on every case, exposing a decisional-alignment axis the field has not targeted. The decomposition also surfaced a pre-registered prediction of our own, that summarization would fail factual recall, which the data reversed at large magnitude, an axis-level reversal aggregate accuracy would have hidden. Institutional alignment (regulatory reconstruction) and decisional alignment (calibrated abstention) are under-represented in the alignment literature and become load-bearing once decisions leave the laboratory. The framework transfers to any regulated decisioning domain via two steps: build a fact schema, and calibrate the CRR auditor prompt.

---


### 103. [Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning](https://arxiv.org/abs/2604.19459)

**<font color=#1a73e8>作者：</font>** Kyuhee Kim, Auguste Poiroux, Antoine Bosselut  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formal verification guarantees proof validity but not formalization faithfulness. For natural-language logical reasoning, where models construct axiom systems from scratch without library constraints, this gap between valid proofs and faithful translations is especially acute. We investigate whether frontier models exploit this gap when generating Lean 4 proofs, a behavior we term formalization gaming.
We evaluate GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), comparing unified generation against a two-stage pipeline that separates formalization from proving. Despite compilation rates of 87-99%, we find no evidence of systematic gaming in unified generation: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it. However, unfaithfulness that evades our detection signals may still occur. The two-stage pipeline reveals two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation, a reactive fallback detectable via cross-stage comparison, while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely. These findings show that high compilation rates or accuracies should not be equated with faithful reasoning. Code and data are available at this https URL.

---


### 104. [LePREC: Reasoning as Classification over Structured Factors for Assessing Relevance of Legal Issues](https://arxiv.org/abs/2604.19464)

**<font color=#1a73e8>作者：</font>** Fanyu Wang, Xiaoxi Kang, Paul Burgess 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> More than half of the global population struggles to meet their civil justice needs due to limited legal resources. While Large Language Models (LLMs) have demonstrated impressive reasoning capabilities, significant challenges remain even at the foundational step of legal issue identification. To investigate LLMs' capabilities in this task, we constructed a dataset from 769 real-world Malaysian Contract Act court cases, using GPT-4o to extract facts and generate candidate legal issues, annotated by senior legal experts, which reveals a critical limitation: while LLMs generate diverse issue candidates, their precision remains inadequate (GPT-4o achieves only 62%). To address this gap, we propose LePREC (Legal Professional-inspired Reasoning Elicitation and Classification), a neuro-symbolic framework combining neural generation with structured statistical reasoning. LePREC consists of: (1) a neuro component leverages LLMs to transform legal descriptions into question-answer pairs representing diverse analytical factors, and (2) a symbolic component applies sparse linear models over these discrete features, learning explicit algebraic weights that identify the most informative reasoning factors. Unlike end-to-end neural approaches, LePREC achieves interpretability through transparent feature weighting while maintaining data efficiency through correlation-based statistical classification. Experiments show a 30-40% improvement over advanced LLM baselines, including GPT-4o and Claude, confirming that correlation-based factor-issue analysis offers a more data-efficient solution for relevance decisions.

---


### 105. [EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training](https://arxiv.org/abs/2604.19485)

**<font color=#1a73e8>作者：</font>** Chengjun Pan, Shichun Liu, Jiahang Lin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for LLM post-training faces a fundamental design choice: whether to use a learned critic as a baseline for policy optimization. Classical theory favors critic-based methods such as PPO for variance reduction, yet critic-free alternatives like GRPO have gained widespread adoption due to their simplicity and competitive performance. We show that in sparse-reward settings, a learned critic can inject estimation noise that exceeds the state signal it captures, increasing rather than reducing advantage variance. By casting baseline selection as a Kalman filtering problem, we unify PPO and GRPO as two extremes of the Kalman gain and prove that explained variance (EV), computable from a single training batch, identifies the exact boundary: positive EV indicates the critic reduces variance, while zero or negative EV signals that it inflates variance. Building on this insight, we propose Explained Variance Policy Optimization (EVPO), which monitors batch-level EV at each training step and adaptively switches between critic-based and batch-mean advantage estimation, provably achieving no greater variance than the better of the two at every step. Across four tasks spanning classical control, agentic interaction, and mathematical reasoning, EVPO consistently outperforms both PPO and GRPO regardless of which fixed baseline is stronger on a given task. Further analysis confirms that the adaptive gating tracks critic maturation over training and that the theoretically derived zero threshold is empirically optimal.

---


### 106. [CoDA: Towards Effective Cross-domain Knowledge Transfer via CoT-guided Domain Adaptation](https://arxiv.org/abs/2604.19488)

**<font color=#1a73e8>作者：</font>** Jianzhi Yan, Le Liu, Buzhou Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved substantial advances in logical reasoning, yet they continue to lag behind human-level performance. In-context learning provides a viable solution that boosts the model's performance via prompting its input with expert-curated, in-domain exemplars. However, in many real-world, expertise-scarce domains, such as low-resource scientific disciplines, emerging biomedical subfields, or niche legal jurisdictions, such high-quality in-domain demonstrations are inherently limited or entirely unavailable, thereby constraining the general applicability of these approaches. To mitigate this limitation, recent efforts have explored the retrieval of cross-domain samples as surrogate in-context demonstrations. Nevertheless, the resulting gains remain modest. This is largely attributable to the pronounced domain shift between source and target distributions, which impedes the model's ability to effectively identify and exploit underlying shared structures or latent reasoning patterns. Consequently, when relying solely on raw textual prompting, LLMs struggle to abstract and transfer such cross-domain knowledge in a robust and systematic manner. To address these issues, we propose CoDA, which employs a lightweight adapter to directly intervene in the intermediate hidden states. By combining feature-based distillation of CoT-enriched reference representations with Maximum Mean Discrepancy (MMD) for kernelized distribution matching, our method aligns the latent reasoning representation of the source and target domains. Extensive experimental results on multiple logical reasoning tasks across various model families validate the efficacy of CoDA by significantly outperforming the previous state-of-the-art baselines by a large margin.

---


### 107. [Seeing Candidates at Scale: Multimodal LLMs for Visual Political Communication on Instagram](https://arxiv.org/abs/2604.19489)

**<font color=#1a73e8>作者：</font>** Michael Achmann-Denkler, Mario Haim, Christian Wolff  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a computational case study that evaluates the capabilities of specialized machine learning models and emerging multimodal large language models for Visual Political Communication (VPC) analysis. Focusing on concentrated visibility in Instagram stories and posts during the 2021 German federal election campaign, we compare the performance of traditional computer vision models (FaceNet512, RetinaFace, Google Cloud Vision) with a multimodal large language model (GPT-4o) in identifying front-runner politicians and counting individuals in images. GPT-4o outperformed the other models, achieving a macro F1-score of 0.89 for face recognition and 0.86 for person counting in stories. These findings demonstrate the potential of advanced AI systems to scale and refine visual content analysis in political communication while highlighting methodological considerations for future research.

---


### 108. [Beyond Rating: A Comprehensive Evaluation and Benchmark for AI Reviews](https://arxiv.org/abs/2604.19502)

**<font color=#1a73e8>作者：</font>** Bowen Li, Haochen Ma, Yuxin Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of Large Language Models (LLMs) has spurred interest in automated peer review; however, progress is currently stifled by benchmarks that treat reviewing primarily as a rating prediction task. We argue that the utility of a review lies in its textual justification--its arguments, questions, and critique--rather than a scalar score. To address this, we introduce Beyond Rating, a holistic evaluation framework that assesses AI reviewers across five dimensions: Content Faithfulness, Argumentative Alignment, Focus Consistency, Question Constructiveness, and AI-Likelihood. Notably, we propose a Max-Recall strategy to accommodate valid expert disagreement and introduce a curated dataset of paper with high-confidence reviews, rigorously filtered to remove procedural noise. Extensive experiments demonstrate that while traditional n-gram metrics fail to reflect human preferences, our proposed text-centric metrics--particularly the recall of weakness arguments--correlate strongly with rating accuracy. These findings establish that aligning AI critique focus with human experts is a prerequisite for reliable automated scoring, offering a robust standard for future research.

---


### 109. [SimDiff: Depth Pruning via Similarity and Difference](https://arxiv.org/abs/2604.19520)

**<font color=#1a73e8>作者：</font>** Yuli Chen, Shuhao Zhang, Fanshen Meng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Depth pruning improves the deployment efficiency of large language models (LLMs) by identifying and removing redundant layers. A widely accepted standard for this identification process is to measure the similarity between layers using cosine distance. However, we find that methods relying solely on this one-dimensional heuristic can exhibit unpredictable performance and even catastrophic collapse across different architectures. To address this issue, we propose SimDiff, a novel layer importance criterion that jointly evaluates layers from two orthogonal perspectives: representational similarity and transformation difference. The difference is quantified using two distinct metrics: MSSD, which is sensitive to outliers and identifies layers that make decisive corrections, and MASD, which robustly measures a layer's average contribution. Extensive experiments on multiple models ranging from 0.5B to 13B parameters demonstrate that SimDiff significantly outperforms state-of-the-art baselines across various pruning ratios. Notably, our method retains over 91% of LLaMA2-7B's performance at a 25% pruning ratio and achieves up to a 1.49x inference speedup when pruning 12 layers on LLaMA3.1-8B. We also show that pruned models can be effectively recovered with minimal fine-tuning.

---


### 110. [Calibrating Scientific Foundation Models with Inference-Time Stochastic Attention](https://arxiv.org/abs/2604.19530)

**<font color=#1a73e8>作者：</font>** Akash Yadav, Taiwo A. Adebiyi, Ruda Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based scientific foundation models are increasingly deployed in high-stakes settings, but current architectures give deterministic outputs and provide limited support for calibrated predictive uncertainty. We propose Stochastic Attention, a lightweight inference-time modification that randomizes attention by replacing softmax weights with normalized multinomial samples controlled by a single concentration parameter, and produces predictive ensembles without retraining. To set this parameter, we introduce a calibration objective that matches the stochastic attention output with the target, yielding an efficient univariate post-hoc tuning problem. We evaluate this mechanism on two scientific foundation models for weather and timeseries forecasting along with an additional regression task. Across benchmarks against uncertainty-aware baselines, we find that Stochastic Attention achieves the strongest native calibration and the sharpest prediction intervals at comparable coverage, while requiring only minutes of post-hoc tuning versus days of retraining for competitive baselines.

---


### 111. [InvestChat: Exploring Multimodal Interaction via Natural Language, Touch, and Pen in an Investment Dashboard](https://arxiv.org/abs/2604.19537)

**<font color=#1a73e8>作者：</font>** Sarah Lykke Tost, Adson Lucas de Paiva Sales, Henrik Østergaard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We designed and implemented InvestChat, a multimodal tablet-based application that supports stock market exploration with multiple coordinated views and an LLM-powered chat. We evaluated the application with 12 novice investors. Our findings suggest that combining natural language, touch, and pen input during stock market exploration facilitates user engagement. Participants leveraged the modalities in complementary ways, enjoying the freedom of choice and finding natural language most effective.

---


### 112. [Integrating Anomaly Detection into Agentic AI for Proactive Risk Management in Human Activity](https://arxiv.org/abs/2604.19538)

**<font color=#1a73e8>作者：</font>** Farbod Zorriassatine, Ahmad Lotfi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI, with goal-directed, proactive, and autonomous decision-making capabilities, offers a compelling opportunity to address movement-related risks in human activity, including the persistent hazard of falls among elderly populations. Despite numerous approaches to fall mitigation through fall prediction and detection, existing systems have not yet functioned as universal solutions across care pathways and safety-critical environments. This is largely due to limitations in consistently handling real-world complexity, particularly poor context awareness, high false alarm rates, environmental noise, and data scarcity. We argue that fall detection and fall prediction can usefully be formulated as anomaly detection problems and more effectively addressed through an agentic AI system. More broadly, this perspective enables the early identification of subtle deviations in movement patterns associated with increased risk, whether arising from age-related decline, fatigue, or environmental factors. While technical requirements for immediate deployment are beyond the scope of this paper, we propose a conceptual framework that highlights potential value. This framework promotes a well-orchestrated approach to risk management by dynamically selecting relevant tools and integrating them into adaptive decision-making workflows, rather than relying on static configurations tailored to narrowly defined scenarios.

---


### 113. [Mesh Memory Protocol: Semantic Infrastructure for Multi-Agent LLM Systems](https://arxiv.org/abs/2604.19540)

**<font color=#1a73e8>作者：</font>** Hongwei Xu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Teams of LLM agents increasingly collaborate on tasks spanning days or weeks: multi-day data-generation sprints where generator, reviewer, and auditor agents coordinate in real time on overlapping batches; specialists carrying findings forward across session restarts; product decisions compounding over many review rounds. This requires agents to share, evaluate, and combine each other's cognitive state in real time across sessions. We call this cross-session agent-to-agent cognitive collaboration, distinct from parallel agent execution. To enable it, three problems must be solved together. (P1) Each agent decides field by field what to accept from peers, not accept or reject whole messages. (P2) Every claim is traceable to source, so returning claims are recognised as echoes of the receiver's own prior thinking. (P3) Memory that survives session restarts is relevant because of how it was stored, not how it is retrieved. These are protocol-level properties at the semantic layer of agent communication, distinct from tool-access and task-delegation protocols at lower layers. We call this missing protocol layer "semantic infrastructure," and the Mesh Memory Protocol (MMP) specifies it. Four composable primitives work together: CAT7, a fixed seven-field schema for every Cognitive Memory Block (CMB); SVAF, which evaluates each field against the receiver's role-indexed anchors and realises P1; inter-agent lineage, carried as parents and ancestors of content-hash keys and realising P2; and remix, which stores only the receiver's own role-evaluated understanding of each accepted CMB, never the raw peer signal, realising P3. MMP is specified, shipped, and running in production across three reference deployments, where each session runs an autonomous agent as a mesh peer with its own identity and memory, collaborating with other agents across the network for collective intelligence.

---


### 114. [DT2IT-MRM: Debiased Preference Construction and Iterative Training for Multimodal Reward Modeling](https://arxiv.org/abs/2604.19544)

**<font color=#1a73e8>作者：</font>** Zhihong Zhang, Jie Zhao, Xiaojian Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal reward models (MRMs) play a crucial role in aligning Multimodal Large Language Models (MLLMs) with human preferences. Training a good MRM requires high-quality multimodal preference data. However, existing preference datasets face three key challenges: lack of granularity in preference strength, textual style bias, and unreliable preference signals. Besides, existing open-source multimodal preference datasets suffer from substantial noise, yet there is a lack of effective and scalable curation methods to enhance their quality. To address these limitations, we propose \textbf{DT2IT-MRM}, which integrates a \textbf{D}ebiased preference construction pipeline, a novel reformulation of text-to-image (\textbf{T2I}) preference data, and an \textbf{I}terative \textbf{T}raining framework that curates existing multimodal preference datasets for \textbf{M}ultimodal \textbf{R}eward \textbf{M}odeling. Our experimental results show that DT2IT-MRM achieves new \textbf{state-of-the-art} overall performance on three major benchmarks: VL-RewardBench, Multimodal RewardBench, and MM-RLHF-RewardBench.

---


### 115. [Emotion-Cause Pair Extraction in Conversations via Semantic Decoupling and Graph Alignment](https://arxiv.org/abs/2604.19547)

**<font color=#1a73e8>作者：</font>** Tianxiang Ma, Weijie Feng, Xinyu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion-Cause Pair Extraction in Conversations (ECPEC) aims to identify the set of causal relations between emotion utterances and their triggering causes within a dialogue. Most existing approaches formulate ECPEC as an independent pairwise classification task, overlooking the distinct semantics of emotion diffusion and cause explanation, and failing to capture globally consistent many-to-many conversational causality. To address these limitations, we revisit ECPEC from a semantic perspective and seek to disentangle emotion-oriented semantics from cause-oriented semantics, mapping them into two complementary representation spaces to better capture their distinct conversational roles. Building on this semantic decoupling, we naturally formulate ECPEC as a global alignment problem between the emotion-side and cause-side representations, and employ optimal transport to enable many-to-many and globally consistent emotion-cause matching. Based on this perspective, we propose a unified framework SCALE that instantiates the above semantic decoupling and alignment principle within a shared conversational structure. Extensive experiments on several benchmark datasets demonstrate that SCALE consistently achieves state-of-the-art performance. Our codes are released at this https URL.

---


### 116. [Taming Actor-Observer Asymmetry in Agents via Dialectical Alignment](https://arxiv.org/abs/2604.19548)

**<font color=#1a73e8>作者：</font>** Bobo Li, Rui Wu, Zibo Ji 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model agents have rapidly evolved from static text generators into dynamic systems capable of executing complex autonomous workflows. To enhance reliability, multi-agent frameworks assigning specialized roles are increasingly adopted to enable self-reflection and mutual auditing. While such role-playing effectively leverages domain expert knowledge, we find it simultaneously induces a human-like cognitive bias known as Actor-Observer Asymmetry (AOA). Specifically, an agent acting as an actor (during self-reflection) tends to attribute failures to external factors, whereas an observer (during mutual auditing) attributes the same errors to internal faults. We quantify this using our new Ambiguous Failure Benchmark, which reveals that simply swapping perspectives triggers the AOA effect in over 20% of cases for most models. To tame this bias, we introduce ReTAS (Reasoning via Thesis-Antithesis-Synthesis), a model trained through dialectical alignment to enforce perspective-invariant reasoning. By integrating dialectical chain-of-thought with Group Relative Policy Optimization, ReTAS guides agents to synthesize conflicting viewpoints into an objective consensus. Experiments demonstrate that ReTAS effectively mitigates attribution inconsistency and significantly improves fault resolution rates in ambiguous scenarios.

---


### 117. [Detecting Data Contamination in Large Language Models](https://arxiv.org/abs/2604.19561)

**<font color=#1a73e8>作者：</font>** Juliusz Janicki, Savvas Chamezopoulos, Evangelos Kanoulas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) utilize large amounts of data for their training, some of which may come from copyrighted sources. Membership Inference Attacks (MIA) aim to detect those documents and whether they have been included in the training corpora of the LLMs. The black-box MIAs require a significant amount of data manipulation; therefore, their comparison is often challenging. We study state-of-the-art (SOTA) MIAs under the black-box assumptions and compare them to each other using a unified set of datasets to determine if any of them can reliably detect membership under SOTA LLMs. In addition, a new method, called the Familiarity Ranking, was developed to showcase a possible approach to black-box MIAs, thereby giving LLMs more freedom in their expression to understand their reasoning better. The results indicate that none of the methods are capable of reliably detecting membership in LLMs, as shown by an AUC-ROC of approximately 0.5 for all methods across several LLMs. The higher TPR and FPR for more advanced LLMs indicate higher reasoning and generalizing capabilities, showcasing the difficulty of detecting membership in LLMs using black-box MIAs.

---


### 118. [Detecting Hallucinations in SpeechLLMs at Inference Time Using Attention Maps](https://arxiv.org/abs/2604.19565)

**<font color=#1a73e8>作者：</font>** Jonas Waldendorf, Bashar Awwad Shiekh Hasan, Evgenii Tsymbalov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucinations in Speech Large Language Models (SpeechLLMs) pose significant risks, yet existing detection methods typically rely on gold-standard outputs that are costly or impractical to obtain. Moreover, hallucination detection methods developed for text-based LLMs do not directly capture audio-specific signals. We investigate four attention-derived metrics: AUDIORATIO, AUDIOCONSISTENCY, AUDIOENTROPY, and TEXTENTROPY, designed to capture pathological attention patterns associated with hallucination, and train lightweight logistic regression classifiers on these features for efficient inference-time detection. Across automatic speech recognition and speech-to-text translation tasks, evaluations on Qwen-2-Audio and Voxtral-3B show that our approach outperforms uncertainty-based and prior attention-based baselines on in-domain data, achieving improvements of up to +0.23 PR-AUC, and generalises to out-of-domain ASR settings. We further find that strong performance can be achieved with approximately 100 attention heads, improving out-of-domain generalisation compared to using all heads. While effectiveness is model-dependent and task-specific training is required, our results demonstrate that attention patterns provide a valuable tool for hallucination detection in SpeechLLMs.

---


### 119. [Multi-modal Reasoning with LLMs for Visual Semantic Arithmetic](https://arxiv.org/abs/2604.19567)

**<font color=#1a73e8>作者：</font>** Chuou Xu, Liya Ji, Qifeng Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) as post-training is crucial for enhancing the reasoning ability of large language models (LLMs) in coding and math. However, their capacity for visual semantic arithmetic, inferring relationships from images, remains underexplored. The classic text analogy "king"-"man"+"woman" = "queen" illustrates relational reasoning, yet replacing text with images of "king" and "man" significantly reduces performance because it requires commonsense knowledge and the extraction of concise concepts from irrelevant visual details. This capability is important for service and domestic robotics in unstructured environments, where robots must infer semantic relationships among objects, agents, and actions. In a kitchen, recognizing from images that "powder" and "cake" are related by "is made of" grounds symbolic relations in perception, enabling tool substitution, task generalization, and improved semantic reasoning. Prior work approaches semantic arithmetic by decoding image features after vector arithmetic, but suffers from modality gaps and lacks systematic evaluation. In this paper, we formulate two novel tasks, two-term subtraction and three-term operations, and construct the Image-Relation-Pair Dataset (IRPD) for benchmarking. We further propose Semantic Arithmetic Reinforcement Fine-Tuning (SAri-RFT), which post-trains large vision-language models (LVLMs) using a verifiable function and Group Relative Policy Optimization (GRPO). Our method achieves state-of-the-art results on IRPD and the real-world Visual7W-Telling dataset. By equipping LVLMs with robust cross-modal relational reasoning, this work advances domestic robots' ability to ground symbolic reasoning in perception, enhancing decision-making, tool adaptability, and human-robot interaction in complex environments. Datasets and source code are provided in the supplementary material.

---


### 120. [Impact of large language models on peer review opinions from a fine-grained perspective: Evidence from top conference proceedings in AI](https://arxiv.org/abs/2604.19578)

**<font color=#1a73e8>作者：</font>** Wenqing Wu, Chengzhi Zhang, Yi Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of Large Language Models (LLMs), the academic community has faced unprecedented disruptions, particularly in the realm of academic communication. The primary function of peer review is improving the quality of academic manuscripts, such as clarity, originality and other evaluation aspects. Although prior studies suggest that LLMs are beginning to influence peer review, it remains unclear whether they are altering its core evaluative functions. Moreover, the extent to which LLMs affect the linguistic form, evaluative focus, and recommendation-related signals of peer-review reports has yet to be systematically examined. In this study, we examine the changes in peer review reports for academic articles following the emergence of LLMs, emphasizing variations at fine-grained level. Specifically, we investigate linguistic features such as the length and complexity of words and sentences in review comments, while also automatically annotating the evaluation aspects of individual review sentences. We also use a maximum likelihood estimation method, previously established, to identify review reports that potentially have modified or generated by LLMs. Finally, we assess the impact of evaluation aspects mentioned in LLM-assisted review reports on the informativeness of recommendation for paper decision-making. The results indicate that following the emergence of LLMs, peer review texts have become longer and more fluent, with increased emphasis on summaries and surface-level clarity, as well as more standardized linguistic patterns, particularly reviewers with lower confidence score. At the same time, attention to deeper evaluative dimensions, such as originality, replicability, and nuanced critical reasoning, has declined.

---


### 121. [Cross-Model Consistency of AI-Generated Exercise Prescriptions: A Repeated Generation Study Across Three Large Language Models](https://arxiv.org/abs/2604.19598)

**<font color=#1a73e8>作者：</font>** Kihyuk Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study compared repeated generation consistency of exercise prescription outputs across three large language models (LLMs), specifically GPT-4.1, Claude Sonnet 4.6, and Gemini 2.5 Flash, under temperature=0 conditions. Each model generated prescriptions for six clinical scenarios 20 times, yielding 360 total outputs analyzed across four dimensions: semantic similarity, output reproducibility, FITT classification, and safety expression. Mean semantic similarity was highest for GPT-4.1 (0.955), followed by Gemini 2.5 Flash (0.950) and Claude Sonnet 4.6 (0.903), with significant inter-model differences confirmed (H = 458.41, p < .001). Critically, these scores reflected fundamentally different generative behaviors: GPT-4.1 produced entirely unique outputs (100%) with stable semantic content, while Gemini 2.5 Flash showed pronounced output repetition (27.5% unique outputs), indicating that its high similarity score derived from text duplication rather than consistent reasoning. Identical decoding settings thus yielded fundamentally different consistency profiles, a distinction that single-output evaluations cannot capture. Safety expression reached ceiling levels across all models, confirming its limited utility as a differentiating metric. These results indicate that model selection constitutes a clinical rather than merely technical decision, and that output behavior under repeated generation conditions should be treated as a core criterion for reliable deployment of LLM-based exercise prescription systems.

---


### 122. [MOSA: Motion-Guided Semantic Alignment for Dynamic Scene Graph Generation](https://arxiv.org/abs/2604.19631)

**<font color=#1a73e8>作者：</font>** Xuejiao Wang, Bohao Zhang, Changbo Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic Scene Graph Generation (DSGG) aims to structurally model objects and their dynamic interactions in video sequences for high-level semantic understanding. However, existing methods struggle with fine-grained relationship modeling, semantic representation utilization, and the ability to model tail relationships. To address these issues, this paper proposes a motion-guided semantic alignment method for DSGG (MoSA). First, a Motion Feature Extractor (MFE) encodes object-pair motion attributes such as distance, velocity, motion persistence, and directional consistency. Then, these motion attributes are fused with spatial relationship features through the Motion-guided Interaction Module (MIM) to generate motion-aware relationship representations. To further enhance semantic discrimination capabilities, the cross-modal Action Semantic Matching (ASM) mechanism aligns visual relationship features with text embeddings of relationship categories. Finally, a category-weighted loss strategy is introduced to emphasize learning of tail relationships. Extensive and rigorous testing shows that MoSA performs optimally on the Action Genome dataset.

---


### 123. [Time Series Augmented Generation for Financial Applications](https://arxiv.org/abs/2604.19633)

**<font color=#1a73e8>作者：</font>** Anton Kolonin, Alexey Glushchenko, Evgeny Bochkov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating the reasoning capabilities of Large Language Models (LLMs) for complex, quantitative financial tasks is a critical and unsolved challenge. Standard benchmarks often fail to isolate an agent's core ability to parse queries and orchestrate computations. To address this, we introduce a novel evaluation methodology and benchmark designed to rigorously measure an LLM agent's reasoning for financial time-series analysis. We apply this methodology in a large-scale empirical study using our framework, Time Series Augmented Generation (TSAG), where an LLM agent delegates quantitative tasks to verifiable, external tools. Our benchmark, consisting of 100 financial questions, is used to compare multiple SOTA agents (e.g., GPT-4o, Llama 3, Qwen2) on metrics assessing tool selection accuracy, faithfulness, and hallucination. The results demonstrate that capable agents can achieve near-perfect tool-use accuracy with minimal hallucination, validating the tool-augmented paradigm. Our primary contribution is this evaluation framework and the corresponding empirical insights into agent performance, which we release publicly to foster standardized research on reliable financial AI.

---


### 124. [SafetyALFRED: Evaluating Safety-Conscious Planning of Multimodal Large Language Models](https://arxiv.org/abs/2604.19638)

**<font color=#1a73e8>作者：</font>** Josue Torres-Fonseca, Naihao Deng, Yinpei Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models are increasingly adopted as autonomous agents in interactive environments, yet their ability to proactively address safety hazards remains insufficient. We introduce SafetyALFRED, built upon the embodied agent benchmark ALFRED, augmented with six categories of real-world kitchen hazards. While existing safety evaluations focus on hazard recognition through disembodied question answering (QA) settings, we evaluate eleven state-of-the-art models from the Qwen, Gemma, and Gemini families on not only hazard recognition, but also active risk mitigation through embodied planning. Our experimental results reveal a significant alignment gap: while models can accurately recognize hazards in QA settings, average mitigation success rates for these hazards are low in comparison. Our findings demonstrate that static evaluations through QA are insufficient for physical safety, thus we advocate for a paradigm shift toward benchmarks that prioritize corrective actions in embodied contexts. We open-source our code and dataset under this https URL

---


### 125. [Micro Language Models Enable Instant Responses](https://arxiv.org/abs/2604.19642)

**<font color=#1a73e8>作者：</font>** Wen Cheng, Tuochao Chen, Karim Helwani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Edge devices such as smartwatches and smart glasses cannot continuously run even the smallest 100M-1B parameter language models due to power and compute constraints, yet cloud inference introduces multi-second latencies that break the illusion of a responsive assistant. We introduce micro language models ($\mu$LMs): ultra-compact models (8M-30M parameters) that instantly generate the first 4-8 words of a contextually grounded response on-device, while a cloud model completes it; thus, masking the cloud latency. We show that useful language generation survives at this extreme scale with our models matching several 70M-256M-class existing models. We design a collaborative generation framework that reframes the cloud model as a continuator rather than a respondent, achieving seamless mid-sentence handoffs and structured graceful recovery via three error correction methods when the local opener goes wrong. Empirical results show that $\mu$LMs can initiate responses that larger models complete seamlessly, demonstrating that orders-of-magnitude asymmetric collaboration is achievable and unlocking responsive AI for extremely resource-constrained devices. The model checkpoint and demo are available at this https URL.

---


### 126. [The signal is the ceiling: Measurement limits of LLM-predicted experience ratings from open-ended survey text](https://arxiv.org/abs/2604.19645)

**<font color=#1a73e8>作者：</font>** Andrew Hong, Jason Potteiger, Luis E. Zapata  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An earlier paper (Hong, Potteiger, and Zapata 2026) established that an unoptimized GPT 4.1 prompt predicts fan-reported experience ratings within one point 67% of the time from open-ended survey text. This paper tests the relative impact of prompt design and model selection on that performance. We compared four configurations on approximately 10,000 post-game surveys from five MLB teams: the original baseline prompt and a moderately customized version, crossed with three GPT models (4.1, 4.1-mini, 5.2). Prompt customization added roughly two percentage points of within +/-1 agreement on GPT 4.1 (from 67% to 69%). Both model swaps from that best configuration degraded performance: GPT 5.2 returned to the baseline, and GPT 4.1-mini fell six percentage points below it. Both levers combined were dwarfed by the input itself: across capable configurations, accuracy varied more than an order of magnitude more by the linguistic character of the text than by the choice of prompt or model. The ceiling has two parts. One is a bias in how the model reads text, which prompt design can correct. The other is a difference between what fans write about and what they actually decide, which no engineering can close because the missing information is not in the text. Prompt customization moved the first part; model selection moved neither reliably. The result is not that "prompt engineering helps a little" but that prompt engineering helps in a specific and predictable way, on the part of the ceiling it can reach.

---


### 127. [Pause or Fabricate? Training Language Models for Grounded Reasoning](https://arxiv.org/abs/2604.19656)

**<font color=#1a73e8>作者：</font>** Yiwen Qiu, Linjuan Wu, Yizhou Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have achieved remarkable progress on complex reasoning tasks. However, they often implicitly fabricate information when inputs are incomplete, producing confident but unreliable conclusions -- a failure mode we term ungrounded reasoning. We argue that this issue arises not from insufficient reasoning capability, but from the lack of inferential boundary awareness -- the ability to recognize when the necessary premises for valid inference are missing. To address this issue, we propose Grounded Reasoning via Interactive Reinforcement Learning (GRIL), a multi-turn reinforcement learning framework for grounded reasoning under incomplete information. GRIL decomposes the reasoning process into two stages: clarify and pause, which identifies whether the available information is sufficient, and grounded reasoning, which performs task solving once the necessary premises are established. We design stage-specific rewards to penalize hallucinations, enabling models to detect gaps, stop proactively, and resume reasoning after clarification. Experiments on GSM8K-Insufficient and MetaMATH-Insufficient show that GRIL significantly improves premise detection (up to 45%), leading to a 30% increase in task success while reducing average response length by over 20%. Additional analyses confirm robustness to noisy user responses and generalization to out-of-distribution tasks.

---


### 128. [InHabit: Leveraging Image Foundation Models for Scalable 3D Human Placement](https://arxiv.org/abs/2604.19673)

**<font color=#1a73e8>作者：</font>** Nikita Kister, Pradyumna YM, István Sárándi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training embodied agents to understand 3D scenes as humans do requires large-scale data of people meaningfully interacting with diverse environments, yet such data is scarce. Real-world motion capture is costly and limited to controlled settings, while existing synthetic datasets rely on simple geometric heuristics that ignore rich scene context. In contrast, 2D foundation models trained on internet-scale data have implicitly acquired commonsense knowledge of human-environment interactions. To transfer this knowledge into 3D, we introduce InHabit, a fully automatic and scalable data generator for populating 3D scenes with interacting humans. InHabit follows a render-generate-lift principle: given a rendered 3D scene, a vision-language model proposes contextually meaningful actions, an image-editing model inserts a human, and an optimization procedure lifts the edited result into physically plausible SMPL-X bodies aligned with the scene geometry. Applied to Habitat-Matterport3D, InHabit produces the first large-scale photorealistic 3D human-scene interaction dataset, containing 78K samples across 800 building-scale scenes with complete 3D geometry, SMPL-X bodies, and RGB images. Augmenting standard training data with our samples improves RGB-based 3D human-scene reconstruction and contact estimation, and in a perceptual user study our data is preferred in 78% of cases over the state of the art.

---


### 129. [A-MAR: Agent-based Multimodal Art Retrieval for Fine-Grained Artwork Understanding](https://arxiv.org/abs/2604.19689)

**<font color=#1a73e8>作者：</font>** Shuai Wang, Hongyi Zhu, Jia-Hong Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding artworks requires multi-step reasoning over visual content and cultural, historical, and stylistic context. While recent multimodal large language models show promise in artwork explanation, they rely on implicit reasoning and internalized knowl- edge, limiting interpretability and explicit evidence grounding. We propose A-MAR, an Agent-based Multimodal Art Retrieval framework that explicitly conditions retrieval on structured reasoning plans. Given an artwork and a user query, A-MAR first decomposes the task into a structured reasoning plan that specifies the goals and evidence requirements for each step. Retrieval is then conditionedon this plan, enabling targeted evidence selection and supporting step-wise, grounded explanations. To evaluate agent-based multi- modal reasoning within the art domain, we introduce ArtCoT-QA. This diagnostic benchmark features multi-step reasoning chains for diverse art-related queries, enabling a granular analysis that extends beyond simple final answer accuracy. Experiments on SemArt and Artpedia show that A-MAR consistently outperforms static, non planned retrieval and strong MLLM baselines in final explanation quality, while evaluations on ArtCoT-QA further demonstrate its advantages in evidence grounding and multi-step reasoning ability. These results highlight the importance of reasoning-conditioned retrieval for knowledge-intensive multimodal understanding and position A-MAR as a step toward interpretable, goal-driven AI systems, with particular relevance to cultural industries. The code and data are available at: this https URL.

---


### 130. [Unveiling Fine-Grained Visual Traces: Evaluating Multimodal Interleaved Reasoning Chains in Multimodal STEM Tasks](https://arxiv.org/abs/2604.19697)

**<font color=#1a73e8>作者：</font>** Jing Jin, Hao Liu, Yan Bai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown promising reasoning abilities, yet evaluating their performance in specialized domains remains challenging. STEM reasoning is a particularly valuable testbed because it provides highly verifiable feedback, but existing benchmarks often permit unimodal shortcuts due to modality redundancy and focus mainly on final-answer accuracy, overlooking the reasoning process itself. To address this challenge, we introduce StepSTEM: a graduate-level benchmark of 283 problems across mathematics, physics, chemistry, biology, and engineering for fine-grained evaluation of cross-modal reasoning in MLLMs. StepSTEM is constructed through a rigorous curation pipeline that enforces strict complementarity between textual and visual inputs. We further propose a general step-level evaluation framework for both text-only chain-of-thought and interleaved image-text reasoning, using dynamic programming to align predicted reasoning steps with multiple reference solutions. Experiments across a wide range of models show that current MLLMs still rely heavily on textual reasoning, with even Gemini 3.1 Pro and Claude Opus 4.6 achieving only 38.29% accuracy. These results highlight substantial headroom for genuine cross-modal STEM reasoning and position StepSTEM as a benchmark for fine-grained evaluation of multimodal reasoning. Source code is available at this https URL.

---


### 131. [Discovering a Shared Logical Subspace: Steering LLM Logical Reasoning via Alignment of Natural-Language and Symbolic Views](https://arxiv.org/abs/2604.19716)

**<font color=#1a73e8>作者：</font>** Feihao Fang, My T. Thai, Yuanyuan Lei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) still struggle with multi-step logical reasoning. Existing approaches either purely refine the reasoning chain in natural language form or attach a symbolic solver as an external module. In this work, we instead ask whether LLMs contain a shared internal logical subspace that simultaneously aligns natural-language and symbolic-language views of the reasoning process. Our hypothesis is that this logical subspace captures logical reasoning capabilities in LLMs that are shared across views while remaining independent of surface forms. To verify this, we employ Canonical Correlation Analysis on the paired residual activations from natural-language and symbolic-language reasoning chains, learning a low-dimensional subspace with maximum cross-view correlation. Furthermore, we design a training-free approach that steers LLMs reasoning chain along this logical subspace, thereby leveraging the complementary reasoning signals from both views. Experiments on four logical reasoning benchmarks demonstrate the effectiveness of our approach, improving accuracy by up to 11 percentage points and generalizing well on out-of-domain problems.

---


### 132. [CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741)

**<font color=#1a73e8>作者：</font>** Gene Chou, Charles Herrmann, Kyle Genova 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the problem of generating a 3D-consistent, navigable environment that is spatially grounded: a simulation of a real location. Existing video generative models can produce a plausible sequence that is consistent with a text (T2V) or image (I2V) prompt. However, the capability to reconstruct the real world under arbitrary weather conditions and dynamic object configurations is essential for downstream applications including autonomous driving and robotics simulation. To this end, we present CityRAG, a video generative model that leverages large corpora of geo-registered data as context to ground generation to the physical scene, while maintaining learned priors for complex motion and appearance changes. CityRAG relies on temporally unaligned training data, which teaches the model to semantically disentangle the underlying scene from its transient attributes. Our experiments demonstrate that CityRAG can generate coherent minutes-long, physically grounded video sequences, maintain weather and lighting conditions over thousands of frames, achieve loop closure, and navigate complex trajectories to reconstruct real-world geography.

---


> [!TIP]
> 当前位于：**101-132**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-132**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
