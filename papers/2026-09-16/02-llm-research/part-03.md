# 🧠 大模型相关研究 | 2026年09月16日

> 本类共 **368** 篇论文：已确认 **345** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-368](./part-08.md)

---

### 101. [SHIFT-M3: Pre-fusion Alignment-based Consistency Screening for Multimodal ECG Record Integrity](https://arxiv.org/abs/2609.13874)

**<font color=#1a73e8>作者：</font>** Md Ashik Khan, Md Nahid Siddique  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal clinical AI typically assumes that the waveform, report, metadata, and downstream predictions attached to a record belong to the same patient. In practice, linkage failures can silently assemble individually plausible but cross-patient components, creating a safety problem that standard predictive models are not designed to detect. We study this problem as multimodal record integrity triage: given an assembled record, should its modalities be trusted to belong together? We introduce SHIFT-M3, a lightweight text-based pre-fusion screen that measures alignment-based consistency between two separately produced ECG text views: an LLM-generated interpretation and a clinical report summary. On 784,680 MEETI ECG records, SHIFT-M3 achieves 97.6% TPR@5% FPR for full text-view swaps (AUROC 0.996), 90.3% for partial swaps (AUROC 0.974), and 97.7% for label-matched hard negatives (AUROC 0.996) with only 573,569 parameters. Compared with same-dataset lexical baselines, the gains are largest on partial swaps and hard negatives, suggesting that the model is learning more than surface overlap. We also introduce the CMST (Conflict-type Multimodal Stress Test) evaluation taxonomy, a three-seed stability study, a loss ablation, a temporal-tolerance sweep, and a shared-token masking control. The main remaining failure mode is longitudinal ambiguity: at the default operating point, same-patient cross-visit pairs still produce 87.0% Type-II false positives.

---


### 102. [Map Users and Mapmakers: The Scope of Cognitive Attribution from Acquired Representations](https://arxiv.org/abs/2609.13879)

**<font color=#1a73e8>作者：</font>** Yiling Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An acquired representation can enlarge a system's cognitive repertoire without transferring the capacities exercised in producing that representation. This paper develops a framework for specifying that enlargement and its limits. Its central contribution is a five-part attribution table distinguishing effective tracking, application of acquired structures, acquisition from explicit specifications, acquisition from identifying observations, and retention and reuse. Each entry identifies a positive capacity commitment and a further claim requiring additional support. The argument deliberately grants meaningful content, causal efficacy, and productive inference, so that its conclusion does not depend on treating representations as inert encodings. Map and category examples show why even complete application competence leaves acquisition capacity undetermined, and why acquiring a criterion from its description differs from finding it in examples. Short formal proofs appear in an appendix. The framework is applied to Andrew Ng's world-model interpretation of Othello-GPT and to the specific indicators discussed in contemporary accounts of machine concepts. It preserves demonstrated recognition, classification, inference, and qualified acquisition while specifying what remains unestablished about criterion discovery and accumulation. The result concerns the scope of cognitive attribution rather than the constitutive conditions of concept possession: cognitive achievements deserve credit for the capacities they establish, without silently importing a broader repertoire through the labels attached to them.

---


### 103. [Lie to me: Detecting Managerial Evasiveness in Earnings Calls via Conversational Audio Encoders](https://arxiv.org/abs/2609.13893)

**<font color=#1a73e8>作者：</font>** Huizhong Chen, Huan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Earnings conference calls are a primary channel through which managers disclose information under analyst scrutiny. Prior work has linked vocal and lexical cues to future adverse outcomes, but often pools features over an entire call and underuses the interactive structure of Q&A. We propose a two-branch late-fusion framework for detecting managerial evasiveness as a predictor of extrinsic SEC events (primarily late filings): (i) an LLM-as-a-judge that maps Q&A text to an interpretable call-level vector X_text via a structured binary rubric, and (ii) a frozen conversational encoder whose temporal hidden states are read by a DeepVoice-style sequential reader to produce an audio representation h. Late fusion of (X_text, h) yields a call-level risk score p. On n=1,039 calls (212 late filings) with firm-grouped 5-fold CV, fusion reaches AUROC approx. 0.89, versus 0.55 for the text judge and 0.71 for duration alone. These results show that conversational audio dynamics encode managerial evasiveness beyond lexical content and call length, yielding a stronger early-warning signal of adverse SEC outcomes.

---


### 104. [North Small Translate: Advanced Cost-Effective Translation (Cohere CAT+)](https://arxiv.org/abs/2609.13916)

**<font color=#1a73e8>作者：</font>** Tom Kocmi, Alexandre Bérard, Phil Blunsom 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present North Small Translate, an open-weight, LLM-based machine translation (MT) model with instruction-following capabilities built on the same foundation as Cohere's Command A Plus, a mixture-of-experts architecture with 25 billion active parameters out of 218 billion total parameters. North Small Translate is trained using difficulty sampling to obtain challenging documents and a five-step training protocol combining supervised fine-tuning, direct preference optimization, and online reinforcement learning. We prioritized throughput through a non-reasoning base model and supplemented with optional agentic capabilities to unlock translation quality gains. North Small Translate is trained to perform MT-related tasks, including post-editing and quality estimation, as well as related tasks such as general instruction following. The model achieves top MT performance across 50 languages in the class of models under 1T parameters, with no need to run expensive reasoning at inference time.

---


### 105. [LoRA Fine-Tuned Models for Control Systems Course Q\&A: A Multidimensional Evaluation of Model Scale and Rank Effects](https://arxiv.org/abs/2609.13918)

**<font color=#1a73e8>作者：</font>** Shaowen Lu, Chengxu Liu, Ping Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in specialized university courses, but control-systems questions require coordinated terminology, notation, derivations, and stepwise explanations. Direct general-purpose responses may be inconsistently structured and hard to verify. Using exercises and reference solutions from a Linear Control Systems course, we built a supervised fine-tuning dataset of 360 system-user-assistant conversations. We applied LoRA to Qwen2.5-3B-Instruct and Qwen2.5-7B-Instruct. With identical data splits, inference settings, and evaluation protocols, we compared base and fine-tuned models and tested LoRA ranks r=4, 8, and 16. Evaluation used ROUGE, BERTScore, and structured-output features to measure reference-answer similarity and stability of the Solution-Method-Teaching Points format. LoRA improved both similarity and structured-output stability at both sizes. On the current test set, 7B-r16 achieved the highest ROUGE-L (0.4093) and BERTScore-F1 (0.8643), while r=8 offered a better balance between performance and parameter efficiency. Bootstrap resampling showed ROUGE-L gains of 0.0764 [0.0613, 0.0915] for 3B-r16 and 0.0874 [0.0687, 0.1042] for 7B-r16; both intervals exceeded zero, indicating stable textual-similarity improvements on the current test set. These results suggest LoRA can align open-source instruction-tuned models more closely with the language and pedagogical organization of course reference answers. However, the metrics mainly capture textual similarity and formatting consistency, not domain-specific reasoning or mathematical correctness, which require expert assessment and task-specific rubrics.

---


### 106. [Machine Learning in Fish Farming](https://arxiv.org/abs/2609.13919)

**<font color=#1a73e8>作者：</font>** Fearghal O'Donncha, Nikos Papandroulakis, Jennie Korus 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This chapter explores how machine learning (ML) is transforming aquaculture, with a particular focus on enhancing decision-making processes and improving operational efficiency. The chapter is structured to first introduce the challenges in aquaculture and the role of AI and then provide an overview of ML techniques in the context of aquaculture, followed by applications, emerging trends, future directions, and case studies. The focus is on real-world applications of ML techniques, including Random Forest, Convolutional Neural Networks (CNNs), and Recurrent Neural Networks (RNNs), as well as emerging technologies such as Graph Neural Networks (GNNs) and large language models (LLMs). Key applications include biomass estimation, species recognition, behavioural analysis, and environmental forecasting. The chapter also highlights the synergy between ML and the Internet of Things (IoT) for real-time monitoring and decision support. Ultimately, ML-driven innovations have the potential to revolutionise fish farming, leading to more efficient, sustainable, and productive practices in the aquaculture industry.

---


### 107. [Inter-Rater Reliability of LLM and Rule-Based Annotation for Inferential Narrative Features: Three Studies on a Turkish Corpus](https://arxiv.org/abs/2609.13936)

**<font color=#1a73e8>作者：</font>** Levent Bulut  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Datasets that ship automatically generated feature annotations invite a question rarely asked of them: would a human agree with those labels? This report answers that for the Objective Projection corpus, a Turkish narrative dataset whose scenes carry a per-scene applied_rules field from a rule-based detector over six craft features -- two prohibitions (emotion labelling, simile) and four positive techniques (materialized metaphor, micro-focus, temporal anchor, atmosphere contradiction).
Three studies are reported. Study 1 ($n = 120$) scores the detector against blind labels from the scheme's own author. Study 2 ($n = 100$, a disjoint scene set) scores the detector plus Gemini 2.5 Flash and Grok against an independent non-expert rater whose labels were locked before any machine ran. Study 2b re-runs the identical protocol with Claude Fable 5 (High) and ChatGPT 5.5.
The central result concerns one rule. On materialized metaphor -- closest to the methodology's theoretical core -- the five machine labellers returned positive rates of $0$, $1$, $40$, $72$ and $78$ out of $100$ scenes, against a human count of $9$. Cohen's $\kappa$ was at or indistinguishable from chance for five of six labellers, across both human references and both scene sets: $0.004$, $0.015$, $0.000$, $0.019$, $0.027$. Raw agreement ranged from $74.7\%$ to $84.5\%$, an artefact of class imbalance rather than a sign of competence.
We deliberately do not resolve this into a single story. Two readings survive: the feature is genuinely inferential and beyond current automatic detection, or the rule's definition is not yet operational enough for any rater to apply consistently -- including the human. Distinguishing them needs a second independent human rater, which this report does not have and therefore does not claim.

---


### 108. [CRITICS - Critical Science Without Borders: Language Models to Promote Critical Thinking in Science Education](https://arxiv.org/abs/2609.13942)

**<font color=#1a73e8>作者：</font>** Rodrigo Agerri, Itziar Aldabe, Elena Cabrio 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The CRITICS project addresses science accessibility and literacy by converging advanced Machine Translation (MT) based on Large Language Models (LLMs) with educational technology. By leveraging MT systems specifically optimized for scientific content, educational institutions can provide accurate, culturally relevant translations of scientific materials in students' native languages, ensuring that complex scientific concepts are comprehensible while maintaining technical accuracy. Building on these translations, the project explores the design and evaluation of innovative science teaching-learning proposals grounded in curriculum-aligned teaching-learning. Thus, CRITICS will investigate key components of scientific argumentation and critical thinking practices together with textual feedback aligned with learning objectives and assessment criteria inspired by competence-based evaluation frameworks. CRITICS aims to break down language barriers to accessing cutting-edge research and educational materials currently available only in high-resourced languages, thereby facilitating the democratization of scientific knowledge and fostering critical thinking in science education.

---


### 109. [SAILOR: Solver-Assisted Interactive LLM-based Optimization Recovery](https://arxiv.org/abs/2609.13945)

**<font color=#1a73e8>作者：</font>** Shaghayegh Sadeghi, Stephen L. Smith, David C. Del Rey Fern'andez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural-language descriptions of optimization problems may be incomplete or vague about numerical information that a solver requires, including costs, capacities, demands, bounds, and penalties. A language model can translate the description into code, but when a required value is absent it must either stop or guess. We present SAILOR, a proof-of-concept system that detects such unsupported numerical choices, asks the user targeted follow-up questions, and updates the optimization model before returning a solution. Questions are prioritized using uncertainty and solver-derived estimates of how strongly each missing value affects the current model. We evaluate the pipeline on 1,723 instances from seven masked benchmarks using an idealized simulator that returns ground-truth values. Exact objective-value agreement ranges from 27.0% to 87.6% across datasets, with 1.4--5.7 questions per instance on average. These results establish feasibility under controlled branch-and-reveal feedback; they do not measure performance with human users or general structural model repair. Code is available at: this https URL.

---


### 110. [Thought without systematicity? Evaluating reasoning models on rule induction tasks](https://arxiv.org/abs/2609.13948)

**<font color=#1a73e8>作者：</font>** Simon Schug, Brenden M. Lake  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A central tenet of human cognition is systematicity, the principle that understanding one concept is inherently tied to understanding close variations of that concept. Do reasoning models robustly exhibit such systematicity? If so, we would expect consistent performance on structurally equivalent variants of the same task. Here, we extend established rule induction tasks from cognitive science to assess the systematicity of thought in current reasoning models. Each task family has compositional structure that we use to create structurally equivalent task variations through task isomorphisms such as recombination and substitution. We find that despite being able to correctly solve a task, models often fail on structurally equivalent variants of the same task. These findings suggest that many model behaviors lack systematicity, rendering it difficult to robustly establish the cognitive abilities of reasoning models beyond the particular contexts they were evaluated in.

---


### 111. [Mizan: A National Benchmark for Evaluating Large Language Models on Iraqi Arabic and the Iraqi Civic Context](https://arxiv.org/abs/2609.13980)

**<font color=#1a73e8>作者：</font>** Nawar S. Alseelawi, Mustafa S. Aljumaily  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Arabic large-language-model (LLM) evaluation has matured around Modern Standard Arabic (MSA): aggregated leaderboards such as the Open Arabic LLM Leaderboard (OALL), HELM Arabic, and BALSAM rank models across dozens of MSA tasks, and frontier systems increasingly saturate them. Dialectal Arabic, the language Iraqis actually speak, remains nearly invisible to this infrastructure. We introduce Mizan ("the balance"), Iraq's national benchmark for evaluating LLMs on Iraqi Arabic and the Iraqi civic context: an MSA baseline track paired with an Iraqi track across six axes (dialect comprehension, dialect generation, bidirectional MSA-Iraqi translation, Iraq-specific knowledge, official-document field extraction, and safety), built from 340 originally authored, dually reviewed items with statistically audited answer positions and Wilson intervals on every published score. A pilot evaluation of 27 systems, spanning closed frontier models three days after release, open weights across size tiers, and an Arabic trio of commercial, open-specialized, and sovereign systems, yields four findings. The MSA track saturates while the Iraqi track discriminates, with a consistent 14-18-point per-model gap and statistically tied leaders. Official-document extraction confines every system to 32-56. Arabic-focused specialization behaves as MSA specialization: two dedicated Arabic models score below a size-matched generalist on the Iraqi track. And the safety-hardened tier of the newest model family deterministically refuses innocuous dialect-comprehension items as policy violations, an over-refusal mode invisible to MSA benchmarks. The platform enforces an integrity protocol of immutable snapshots, verification certificates, a human publication gate, and public retraction, all exercised during this study. Code and the public development set accompany the paper.

---


### 112. [Synthetic Data in Marketing Research: How to Evaluate and When to Trust](https://arxiv.org/abs/2609.13995)

**<font color=#1a73e8>作者：</font>** Oded Netzer, Rajan Sambandam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Debate over synthetic data in marketing research has polarized between claims that large language models (LLMs) make human respondents obsolete and calls to avoid them entirely. We argue that both positions obscure the more useful question: not whether synthetic respondents work, but when. Building on Brand, Israeli, and Ngwe (2026), we make three contributions. First, we distinguish three types of synthetic data (ungrounded LLM responses, segment-level personas, and individual-level digital twins) and map each to the decisions it can support. Second, we develop a taxonomy of four families of accuracy measures and suggest that the wide range of reported twin accuracy, from near-perfect to near-chance, largely reflects differences in what is being measured rather than in method quality. Aggregate measures often perform well even when little information is supplied to the LLM, and can mask a complete absence of respondent-level differentiation. Third, we introduce the forgotten question problem, in which a question is omitted from a fielded study, as a setting for twin-based augmentation of existing data. We propose an ex-ante answerability diagnostic that requires no ground truth: the R^2 of a random forest predicting twin outputs from the data used to construct the twins. Across 108 attitude questions from a nationally representative survey (N = 3,063), screening at R^2 above 0.7 raises the mean twin-human individual-level correlation by 15% and reduces the share of poorly answered questions from 25.9% to 4.3%. Embedding similarity and experienced-researcher judgment provide correlated but weaker screens.

---


### 113. [Unlocking the Unsolvable: Teacher-Guided Curriculum for Data-Efficient RLVR](https://arxiv.org/abs/2609.13997)

**<font color=#1a73e8>作者：</font>** Yukang Zhu, Zhen Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has shown remarkable success in improving the mathematical reasoning of large language models. Yet problems beyond the model's current capability, where rollouts uniformly fail and no learning signal is produced, are structurally wasted despite marking the most informative training frontier. We show that these otherwise-inert problems can be unlocked via teacher-guided curriculum learning: partial reasoning traces from a stronger model create a graded difficulty landscape, and a backward-chaining curriculum progressively withdraws guidance until the model solves problems unaided. Training on only 128 unsolvable problems matches or exceeds GRPO trained on a full 2,000-problem corpus (~16x data efficiency) on the nine-benchmark average for both base models, while substantially expanding the reasoning boundary measured by pass@k at large k. Furthermore, we identify a distribution-shift cost that is particularly acute in the unsolvable-only regime and propose Monotone Frontier Curriculum (MFC), a method that monotonically drives training toward unguided solving, consistently outperforming existing curriculum methods.

---


### 114. [Convergent Emergence of In-Context Learning Across Modalities](https://arxiv.org/abs/2609.14011)

**<font color=#1a73e8>作者：</font>** Nathan Breslow, Seungwook Han, Daniel Hyunsoo Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Few-shot in-context learning (ICL), the capacity of a model to infer abstract patterns from input-output examples provided in its prompt and apply them to new inputs, has been extensively studied in large language models trained for next-token prediction on human text. Recently, few-shot ICL has been demonstrated in autoregressive genomic models as well. This raises a question: does ICL emerge broadly across domains, and if so, what common structure is shared?
To address both, we develop a controlled cross-modality framework that instantiates the same task suite in a variety of modalities to test what we call the Convergent Emergence Hypothesis: the idea that few-shot ICL, when it emerges, shares a common cross-modality difficulty profile - i.e., tasks that benefit from ICL in one modality tend to benefit in others. We show that paired-mapping ICL emerges across six modalities (language, genome, integer sequences, time series, images, and proteins), surpasses controlled baselines, and has correlated per-task effects across five of them. Together, these results provide support for the Convergent Emergence Hypothesis in some modalities, but not all.

---


### 115. [VeriDx: Earning the Right to Diagnose with Disease-Centric Verification](https://arxiv.org/abs/2609.14018)

**<font color=#1a73e8>作者：</font>** Zhong Cao, Shuying Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A correct diagnosis can still be reached for the wrong reasons. In clinical reasoning, every disease hypothesis creates obligations: key evidence must be checked, alternatives must be ruled out, contradictions must be resolved, useful tests must be considered, and closure must be justified. Current evaluations of medical LLMs mostly focus on final answers, local steps, or isolated facts, and therefore miss these hypothesis-induced commitments. We introduce \textbf{VeriDx}, a disease-centric verification framework that links free-form diagnostic reasoning to structured disease profiles. VeriDx tracks whether each hypothesis is satisfied, unresolved, or violated its clinical obligations, exposing failures such as missing critical tests, unresolved differentials, ignored contradictions, unsupported claims, and premature closure. We instantiate VeriDx for complex respiratory diagnosis using guideline-derived disease profiles and expert-annotated longitudinal cases. Our results show that many diagnostic errors are not isolated mistakes, but broken commitments made earlier in the reasoning process.

---


### 116. [Measuring the Creativity of Frontier LLMs in Automated Research](https://arxiv.org/abs/2609.14057)

**<font color=#1a73e8>作者：</font>** Yiheng Zhao, Mengzhuo Chen, Chengming Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier LLMs are increasingly capable of conducting automated research, yet their creativity in this setting has not been systematically evaluated. In this paper, we propose a set of metrics to evaluate creativity along the two dimensions of valueness and novelty. Valueness assesses whether each proposed idea is useful, while novelty is evaluated from three perspectives: whether the same idea has appeared before (Exact-Match P-Novelty), whether a previously unexplored variable or variable combination is explored (Variable-level P-Novelty), and whether the idea directly follows retrieved external knowledge or departs from it (H-Novelty). Our evaluation shows that the models achieve relatively similar scores on most creativity metrics, but differ substantially in Variable-level P-Novelty, which reflects the breadth of research-space exploration. Further correlation and idea-level performance analyses show that Variable-level P-Novelty is the creativity dimension most strongly associated with research performance.

---


### 117. [When Single-User-Oriented LLM-based Assistants Involve Others: A Scoping Review of Pathways, Risks, and Responses](https://arxiv.org/abs/2609.14062)

**<font color=#1a73e8>作者：</font>** Yulin Chen, Yang Zhan, Zhuoran Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM-based assistants are increasingly extending into multi-party contexts, while core operational processes for context management, personalization, identity attribution, authority attribution, and action execution often remain organized around a single user. Existing work examines particular multi-party settings, but lacks a systematic account of how these single-user-oriented assistants begin to involve additional human parties and what risks emerge. To address this gap, we conducted a scoping review of 58 studies. We identify five operational pathways spanning direct and indirect involvement, five recurring risk domains, and five areas of implemented and proposed responses. Based on these findings, we argue for governance that attends to changing cross-person roles and relationships in practice, and for assistant designs that preserve person-specific boundaries throughout interaction.

---


### 118. [GraMRAG: Orchestrating Multi-Agent Multi-Step Reasoning via Graph Memory with Reinforcement Learning](https://arxiv.org/abs/2609.14066)

**<font color=#1a73e8>作者：</font>** Zhongyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although existing multi-agent Retrieval-Augmented Generation (RAG) systems have demonstrated promise on complex multimodal reasoning tasks, they remain fundamentally limited in reasoning depth and memory structure, suffering from inadequate retrieval and state blindness when answering knowledge-intensive questions. To address these limitations, we propose GraMRAG, a graph memory-guided multi-agent RAG framework that integrates a dynamic multimodal memory graph to enable stable, multi-step multimodal reasoning. We introduce a vision-text bridged reasoning paradigm that unifies multi-scale entity cropping with a ReAct-style visual toolchain, enhancing the long-horizon cross-modal reasoning capability. We further construct a multimodal memory graph that formalizes agent reasoning as a dynamic directed acyclic graph (DAG), explicitly modeling action-observation dependencies to mitigate state blindness and suppress redundant retrieval. Moreover, we propose Topology-Aware Policy Optimization (TAPO) that leverages graph topology for critical path identification and targeted node pruning, enabling fine-grained credit assignment across multi-step reasoning trajectories. Extensive experiments on challenging multimodal benchmarks demonstrate that our approach consistently outperforms existing baselines and achieves state-of-the-art performance on complex long-horizon reasoning tasks.

---


### 119. [Multi-Modal Tumor Survival Prediction via Graph-Guided Mixture of Experts](https://arxiv.org/abs/2609.14072)

**<font color=#1a73e8>作者：</font>** H Mathavan, H Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have displayed impressive capabilities in handling tasks that require few demonstration examples, making them effective few-shot learners. Despite their potential, LLMs face challenges when it comes to addressing complex real-world tasks that involve multiple modalities or reasoning steps. For example, predicting cancer patients' survival period based on clinical data, cell slides, and genomics poses significant logistical complexities. Although several approaches have been proposed to tackle these challenges, they often fall short in achieving promising performance due to their inability to consider all modalities simultaneously or account for missing modalities, variations in modalities, and the integration of multi-modal data, ultimately compromising their effectiveness. This thesis proposes a novel approach for multi-modal tumor survival prediction to address these limitations. Taking inspiration from recent advancements in LLMs, particularly Mixture of Experts (MoE)-based models, a graph-guided MoE framework is introduced. This framework utilizes a graph structure to manage the predictions effectively and combines multiple models to enhance predictive power. Rather than training a single foundation model for end-to-end survival prediction, the approach leverages a MOE-guided ensemble to manage model callings as tools automatically. By leveraging the strengths of existing models and guiding them through a MOE framework, the aim is to achieve better performance and more accurate predictions in complex real-world tasks. Experiments and analysis on the TCGA-LUAD dataset show improved performance over the individual modal and vanilla ensemble models.

---


### 120. [Adapting Open-Weight MLLMs to Generate Point Prompts for Electron Microscopy Segmentation](https://arxiv.org/abs/2609.14080)

**<font color=#1a73e8>作者：</font>** Samia Mohinta, Albert Cardona  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Promptable models such as microSAM segment electron microscopy (EM) images from point prompts, but automation requires generating prompts without user input. We ask whether open-weight multimodal large language models (MLLMs) can generate them from natural-language requests by returning coordinates to a frozen segmenter. To that end, we convert masks from three mitochondria datasets into training examples, pairing images and instructions with centroid coordinates, then train LoRA adapters while freezing the MLLM backbone and microSAM. We find that Qwen3-VL reaches segmentation AP$_{50}$ $0.736$ after supervised fine-tuning and reward optimization, up from $0.247$ without adaptation, while automatic prompt generation (APG) achieves $0.773$. In addition, two other MLLMs improve, reaching or exceeding APG. When compared with a supervised centroid-heatmap detector that reaches AP$_{50}$ $0.904$ for this mitochondria task, Qwen3-VL more closely matches the annotated point set and instance counts. Moreover, training on two public datasets transfers to an unseen third, while training on all three transfers to an independent EM volume. Robustness tests show stable performance under unseen formulations of the natural-language request, while the coordinates can be reused by a second segmenter. To our knowledge, this is the first feasibility study of open-weight MLLMs as EM point generators, providing an inspectable, language-directed link between localization and mask decoding.

---


### 121. [The Deception Delta: Adversarial Evaluation of LLM-Based Smart Contract Bytecode Forensics](https://arxiv.org/abs/2609.14098)

**<font color=#1a73e8>作者：</font>** Timo Schefold  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in blockchain forensic investigations to interpret unverified smart contract bytecode. Their robustness has not been systematically tested against contracts adversarially designed to mislead analysis.
We evaluate 22 frontier models on 13 purpose-built contracts (9 deception vectors, 4 controls) across six prompt strategies, yielding 8,528 analyzable non-refusal runs against contracts with EVM-verified ground truth. A calibrated LLM-as-judge pipeline, supported by two judge-independent metrics and 50 human gold-standard labels, shows that adversarial deception reduces drain detection by 20.0 percentage points (95% CI: [17.2, 22.8]) relative to functionally matched controls.
Structural camouflage via multi-hop call chains, XOR-masked selectors, and storage-loaded drain parameters resists detection across nearly all models. Beyond non-detection, we identify rationalization: models correctly describe the hidden drain mechanism but accept the contract's deceptive framing and dismiss it as benign, yielding positive but incorrect evidence of safety. Simple guard instructions provide no aggregate benefit and destabilize individual models in both directions.
Structural deception is largely insensitive across the six tested prompt strategies, more consistent with a capability limitation than with a simple prompting problem. Only five models from two providers exceed 50% detection.
Under our single-shot, raw-bytecode-only protocol, current LLMs are not reliable standalone forensic tools. Our central claim does not extend to multi-turn, tool-augmented, source-aware, or decompiler-in-the-loop workflows; a source-code boundary check is reported as an explicit subset analysis rather than as part of the main evaluation.

---


### 122. [RA-CoA: Training-free Fashion Image Captioning via Retrieval-Augmented Chain-of-Attributes](https://arxiv.org/abs/2609.14100)

**<font color=#1a73e8>作者：</font>** Abhirama Subramanyam Penamakuri, Shreya Shukla, Anand Mishra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fashion Image Captioning (FIC) plays a vital role in enhancing user experience and product search in e-commerce platforms. Unlike natural scene image captioning, FIC requires fine-grained visual reasoning and knowledge of domain-specific terminology to capture subtle attributes such as neckline and closure types, graphic patterns, and dress silhouettes. Moreover, as fashion inventories evolve rapidly with new trends, styles, and frequently emerging vocabulary, developing training-free captioning solution becomes essential for scalability and real-world adaptability. Instruction-tuned vision-language models (VLMs) offer a promising solution to fashion image captioning dueto their strong zero-shot capabilities and natural language fluency. However, these general-purpose models often lack attribute-level coverage and precision, and tend to hallucinate or misidentify fine-grained fashion details, making them less suitable for high-fidelity applications like product cataloging or personalized recommendations. To address this, we propose RA-CoA (Retrieval-Augmented Chain-of-Attributes), a novel, training-free framework that disentangles fashion image captioning into two interpretable stages: (i) retrieval of relevant attribute sets from a product knowledge base, and (ii) attribute-level reasoning to generate the final caption. RA-CoA is a model-agnostic approach that works with frozen VLMs to improve fine-grained attribute precision in product captions without the need for fine-tuning. Extensive evaluations across diverse VLM model families under different prompting paradigms demonstrate that RA-CoA significantly improves caption quality, achieving an average gain of 26.3% METEOR score over zero-shot captioning. We make our code publicly available.

---


### 123. [Same Name, Different Server: A Security Census of Silent Drift in the Model Context Protocol Ecosystem](https://arxiv.org/abs/2609.14119)

**<font color=#1a73e8>作者：</font>** Obada Kraishan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) has become the common interface through which large language model applications reach external tools, and its public registry now distributes thousands of community-built servers with little of the vetting infrastructure that mature package ecosystems have accumulated. This paper reports a census of that ecosystem. We harvested the full public MCP registry (21,643 servers, 72,606 version records, August 2026 snapshot), fetched source code for 14,353 servers, and applied a pattern-based scanner covering an eight-class threat catalogue whose accuracy we measured against 414 hand-labeled findings. Observed prevalence is dominated by unauthenticated network exposure (9.57% of scanned servers); after correcting each class by its measured precision, 11.14% observed high-severity prevalence reduces to roughly 7.6%. The central finding concerns instability rather than any single weakness: 51.1% of multi-version servers changed what they advertise between versions, 40.6% did so silently, and 4.2% redirected their remote endpoint to a different host while keeping their registry identity, a change the protocol never surfaces to installed clients. Silent drift is associated with nearly threefold higher odds of a high-severity finding (OR = 2.96, 95% CI [2.56, 3.42]). Popularity offers only weak protection (OR = 0.78 per unit of log stars), so star counts are a poor proxy for safety. We derive concrete recommendations for registry design, client-side pinning, and scanner triage, and release an anonymized artifact.

---


### 124. [Semantic Knowledge Technologies: what the Semantic Web lost sight of, and what it never had](https://arxiv.org/abs/2609.14121)

**<font color=#1a73e8>作者：</font>** Achille Zappa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Semantic Web set out to give information a machine-interpretable form so that software could integrate and reason over it. Its standards became scientific knowledge infrastructure, but the machine competence it promised did not follow, and the systems now answering questions over scientific knowledge are language models holding no inspectable account of what they know. This paper argues the original goal was right and the technical programme incomplete, states what is missing, and names the extended programme Semantic Knowledge Technologies: the same technical core carried out of its web-publishing origin and applied to knowledge wherever held. The diagnosis is that the standards formalised truth while omitting three things: the conditions under which a claim holds, the operations its terms permit, and any account of what a base covers. Without conditions, contradiction and applicability cannot be judged; without operational grounding, holding a statement confers no ability; without declared coverage, a system cannot recognise the boundary of its own content, which under the open-world assumption cannot be inferred. The paper fixes the word understanding to five measurable tests (check, connect, derive, act, delimit) and sets out a seven-layer architecture in which the first three layers are enabling and the rest the cognitive capabilities they make possible. It then defines three terms the programme implies: Large Knowledge Model, a model whose unit of output is a reference to an addressable claim, not a token; SLKM, the knowledge base an agent builds for itself from declared sources; and Semantic Artificial General Intelligence, stated as a falsifiable position about necessary conditions, not a system. A graded ladder replaces the untestable word general. It is offered as a research agenda, with its weakest points and refutation condition named.

---


### 125. [LIMBO: Lifelong Inference-Time Memory and Budget Optimization for LLM Agents](https://arxiv.org/abs/2609.14138)

**<font color=#1a73e8>作者：</font>** Siddharth Sharma, Nilesh Prasad Pandey, Onat Gungor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As LLM agents become integrated into increasingly complex workflows, they must continually acquire new capabilities while retaining competence on previously learned tasks. Lifelong agents address this through experience replay, injecting past interactions into the prompt to leverage prior experience during inference. However, replay is not free: every replayed trajectory competes with retrieval, reasoning, tool use, and verification for the same limited prompt and compute budget, making effective resource allocation essential. Existing approaches allocate these resources using fixed replay policies, regardless of whether replay is beneficial for the current task. We identify this as inference-time memory allocation, a distinct problem class for lifelong agents, and introduce LIMBO: the first online framework to our knowledge that treats memory as a controllable inference-time resource and jointly optimizes memory strategy and inference budget for each incoming task. Unlike prior approaches that fix the replay policy or require model weights, teacher supervision, or offline retraining, LIMBO learns this allocation online in a single pass, explicitly balancing task performance and inference cost without modifying the underlying agent. Across three LLM backbones on LifelongAgentBench, LIMBO achieves better cost-accuracy tradeoffs than state-of-the-art memory-augmented baselines and nearly matches all strongest such baselines at up to ~83% lower inference cost (~53% on average). LIMBO adapts its policy across models and environments without retraining, demonstrating that effective allocation can be learned online rather than manually specified.

---


### 126. [T-SMART: Mechanism-Level Attribution for Tool-Augmented Time-Series Question Answering](https://arxiv.org/abs/2609.14142)

**<font color=#1a73e8>作者：</font>** Ivan Delgado, Himansi Gupta, Bishal Khatri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can struggle with time-series question answering (TS-QA), especially when numerical signals are serialized as text and require explicit computation. Tool-augmented approaches improve performance, but existing systems often intertwine language reasoning, computation, and perception, making it difficult to determine which components drive the gains. We present T-SMART, a neurosymbolic framework that separates these roles: a frozen LLM interprets questions and selects operations, deterministic tools perform numerical computation, and structured perception is invoked only when needed. Controlled paired ablations show that deterministic computation provides the dominant benefit, improving accuracy by 31.7 percentage points over direct LLM reasoning on serialized time series, while language understanding and perception offer smaller complementary gains. These results indicate that tool-augmented TS-QA benefits primarily from reliable numerical execution rather than additional language-model reasoning and provide a controlled framework for analyzing component contributions in neurosymbolic time-series systems.

---


### 127. [One Size Does Not Fit All: Setting Inference Depth from the Questions a Deployment Actually Asks](https://arxiv.org/abs/2609.14144)

**<font color=#1a73e8>作者：</font>** Jerry Kaplan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A transformer language model is trained to respond to any prompt, but each deployment asks only a narrow range of questions: a support assistant sees delivery complaints, a coding tool sees Python. Every deployment nonetheless pays the same computation per token. This paper measures how much of that cost is avoidable when the range of prompts is known in advance.
The mechanism examined is early exit: a small, trained component - called a readout - is attached to an intermediate layer and proposes a token, and a confidence test decides whether to emit it or to run the remaining layers. The models are frozen, and the only supervision used is the model's own output on ordinary traffic.
Three findings are reported. First, achievable savings depend strongly on the kind of traffic: at half depth on a 1.5-billion-parameter model, 96 percent of tokens could be emitted early for arithmetic word problems and 8 percent for Chinese-language explanations, at matched token-level fidelity to the full model (a measure whose limits the third finding exposes). Second, of three ways a deployment might use knowledge of its traffic, only customizing the threshold for exiting early is worthwhile: calibrating it per deployment raised exit rates by up to 59 percentage points across three models, and by more than 10 points on most corpora tested. Third, token-level fidelity - the standard evaluation measure in the early-exit literature - fails in domains where tokens can be checked against ground truth: on arithmetic word problems, three models each answered sixty questions correctly when run in full, and between 10 and 28 correctly under early exit, in the configuration that scored highest on fidelity.
The intended setting is small models on personal devices, where generation is limited by memory bandwidth rather than computation.

---


### 128. [Signatures of Steerability in Activation Space of Language Models](https://arxiv.org/abs/2609.14151)

**<font color=#1a73e8>作者：</font>** Prajjwal Bhattarai, Tuka Alhanai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Steering language models using a set of contrastive representations has been a canonical and computationally efficient method for controlling model behavior. Despite this success in controlling certain model behaviors, the effectiveness of activation steering varies markedly across concepts; the generalization properties of steering vectors are often considered a function of the dataset used to construct them. We make this dataset-dependence claim more rigorous and show that simple separation metrics strongly correlate with the downstream steerability of language models across diverse settings, even after controlling for layers and dataset effects. Beyond prediction, we provide evidence from a synthetic superposition experiment that separation metrics are strongly correlated with alignment between the empirical and true feature direction. Our results suggest that simple separability statistics can serve as practical diagnostics for when steering vectors are likely to work.

---


### 129. [When Tools Get in the Way: The Effect of Unnecessary Tool Availability on LLM Answering](https://arxiv.org/abs/2609.14157)

**<font color=#1a73e8>作者：</font>** Saanvi Paturi, Arsen Kenzhebayev, Arham Sethi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed with external tools that extend what they can do beyond their own knowledge. Tools help on tasks that need external information, but their availability may also change how a model handles questions that do not need them. Prior work has mostly asked whether models select and use tools appropriately; whether an unnecessary tool changes the correctness of answers has received less attention. We ask whether making a related but unnecessary tool available affects a model's ability to answer from its own knowledge, and whether a preceding tool interaction changes this behaviour. We construct 500 query pairs across 10 knowledge domains. Each pair consists of a tool query, which needs the domain's tool, and a closed-domain query, which does not. Six LLMs are evaluated with the tool unavailable, available, and available after a prior tool call. Across 3,000 baseline trials the pooled answer rate is 98.2%. When an unnecessary tool is available it falls to 63.5%, with large differences between models. The decrease occurs even when the tool is rarely called, so it cannot be explained by unnecessary tool invocation alone. A one-sentence scope-aware system instruction recovers most of the lost answers.

---


### 130. [Towards Evolving Context Parameterization for Large Language Models](https://arxiv.org/abs/2609.14168)

**<font color=#1a73e8>作者：</font>** Xiaobing Shi, Zherui Li, Yiming Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Context parameterization enables large language models (LLMs) to internalize contexts into reusable model parameters, avoiding repeated processing across subsequent queries. However, existing methods typically assume static contexts and lack explicit mechanisms for distinguishing validity states under continual updates. To study this real-world scenario, we formalized the Memory Updating with Sequential Evolution (MUSE) task and constructed MUSE-bench to evaluate update incorporation and unaffected-information preservation. The resulting challenge requires preserving the global state while adjusting the contribution of memory evidence. Motivated by this, we proposed PLUME, a training-free method that constructs a global update representation, activates memory evidence to form a local parameter view, and adaptively integrates their predictions during decoding. Comprehensive evaluation on MUSE-bench demonstrated PLUME's effectiveness in sequential evolution settings, yielding relative improvements of 29.9% in average ROUGE-L Recall and 54.9% in LLM-as-a-Judge. Our codes are available at: this https URL.

---


### 131. [Inherited Heads: Audio language models track speakers with their text backbone's attention, and an attention-mass ranking retrieves a different set](https://arxiv.org/abs/2609.14174)

**<font color=#1a73e8>作者：</font>** Bojro Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asked to describe what one of six speakers in a recording talks about, audio language models describe the right one on 6 to 16% of trials, below the 16.7% a guess would give. Adding a fixed bias to the attention logits of a hundred heads, under a tenth of the model's and with no training, redirects the description to whichever speaker we choose, on 90.7% to 99.0% of trials. Those heads are largely not specific to audio. Rank the text-only language model an audio model was built from, or a released model of the same family, on a written version of the task, take its top hundred heads, and carry them over unchanged: they redirect the audio model on 80.8% to 95.0% of trials, with nothing about audio entering the selection. The audio and text head sets share 66 to 74 of 100 where chance would give about 20, and the shared part alone reproduces almost all of the steering. What that does not show is that sharing is what makes the heads work: an equal-sized draw from the same discovered hundred does nearly as well, and none of our three models separates the two explanations. A second finding concerns how such heads are found. Ranking heads by how much attention they place on the segment asked about, as an established score does, or by how much of their attention moves with the question, as a per-head normalised variant does, gives top hundreds that share 69, 37 and 4 heads across our three models. In Ultravox, where they share 4, the established score's heads leave output the judge cannot place on any segment on 69.7% of trials, against 40.0% with no intervention and 1.0% for the normalised variant. That is one arm of six; on the other five the established score steers above a random draw.

---


### 132. [A Multi-Stage Agentic Framework for Effective Counter-Narrative Generation and Refinement](https://arxiv.org/abs/2609.14178)

**<font color=#1a73e8>作者：</font>** Carmel Kronfeld, Sharva Gogawale, Tetsuro Kobayashi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid diffusion of hate speech and misinformation on social networks challenges democratic societies, since direct suppression efforts may deepen polarization, fuel public distrusts, and strengthen extremist narratives. LLM-driven counter-narratives (CNs) offer a promising way to reduce those risks, yet their effectiveness depends on rhetorical and stylistic choices that remain poorly understood. We present a multi-stage agent-based framework for generating, refining, and evaluating CNs, applied to pro-Russian hate and misinformation narratives on the war with Ukraine and adaptable to other domains. A pilot experiment with human evaluators identifies effective technique style pairings, such as repetition with emotional framing enhancing persuasiveness. Building on these insights, we introduce a multi-agent refinement process that iteratively improves CNs for persuasiveness, emotional engagement, and shareability. After human validation confirmed improvement, an automated safety analysis shows that our refined CNs match or improve on expert-written counterspeech. A simulated experiment then shows that they reduce the perceived strength of pro-Russian narratives and consistently outperform a vanilla LLM baseline, highlighting a pathway toward scalable, narrative-specific interventions against hate speech and misinformation. Code and data accompanying this work are publicly available at this https URL.

---


### 133. [Data-free On-policy Distillation](https://arxiv.org/abs/2609.14193)

**<font color=#1a73e8>作者：</font>** Gengsheng Li, Mao Zheng, Mingyang Song 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has become a standard component of frontier post-training pipelines, yet how much its training data actually contributes has gone largely unexamined. On the two teacher-student pairings most common in practice, we find OPD almost indifferent to its data: eight prompts already match a 17k-problem dataset, and three independently built datasets whose difficulty and teacher-student KL differ several-fold produce nearly indistinguishable training curves. Two causes account for this. First, the unit of data in OPD is the state a prompt leads to, not the prompt itself: a single prompt keeps exposing new teacher correction as sampling continues, while the marginal value of additional prompts collapses after eight. Second, replacing mathematics with competitive programming still recovers over ninety percent of the in-domain gain, indicating that OPD transfers the teacher's mode of reasoning rather than knowledge related to the data. We take this to its limit with Data-free On-policy Distillation (DF-OPD), in which the teacher writes its own training questions under a simple prompt -- no external data, no filtering -- leaving a system of just two policies. DF-OPD matches and even surpasses real data, and the questions it produces track the teacher's own post-training data on three key diagnostics of training dynamics, which other real datasets do not. Applied to multi-teacher distillation, where the (prompt, domain) pairs normally have to be derived from post-training data that is often out of reach, 1k self-generated questions close 98.5% of the available headroom, even surpassing the 96.6% reached with 7k real examples. Moreover, together these results invite a reassessment of the role data plays in OPD.

---


### 134. [Learning to Refer from Estimated Listener Gaze](https://arxiv.org/abs/2609.14207)

**<font color=#1a73e8>作者：</font>** Téa Wright, Alane Suhr  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose to finetune vision-language models to generate more pragmatically optimal referring expressions by transforming observations of incremental listener comprehension, in the form of gaze scanpaths, into learning signals. During training, referring expressions are sampled from the speaker policy being optimized, conditioned on images and target referents; then, a neural listener estimating human gaze behavior maps from images and sampled referring expressions to scanpaths, each represented by a sequence of fixations, with each fixation corresponding to a word in the referring expression. We experiment with several approaches to convert fixation sequences and target referents into token- and sequence-level rewards, which are used to optimize policy parameters. Through evaluation with human listeners, we find that speaker policies trained with gaze-estimating listeners result in significantly more pragmatically-optimal references than base models, reducing sequence length from 15.4 down to 4.0 words while increasing referential success from 75.2 up to 80.0%. Our work demonstrates a promising opportunity for learning to generate utterances through language-based interaction, not only from the explicit signal of communicative success, but also from implicitly-available observations of a listener's process of comprehension.

---


### 135. [Assessing the Applicability of Existing Design Recommendations to AI Companion Design: A Multi-Method Study](https://arxiv.org/abs/2609.14236)

**<font color=#1a73e8>作者：</font>** Soobin Cho, Deveshi Modi, Divya Mavinkurve 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the rapid proliferation of large language model (LLM)-based systems, AI companions have emerged as conversational agents designed to cultivate emotional connection rather than primarily to support humans in instrumental tasks. Because engagement with AI companions involves relational, emotional, and potentially long-term interactions, their design is consequential. Prior work has offered guidance for designing trustworthy and relational AI systems and has begun to examine design for AI companionship. However, while such work provides insights into possible design solutions, less is known about what makes AI companion design difficult as a design problem. To examine this challenge, we assessed the applicability of existing design recommendations from adjacent domains in the context of AI companion design. Our multi-method investigation unfolded across four phases: literature review, practitioner co-analysis, internal heuristic evaluation, and external expert assessment. Throughout this process, we synthesized nine design principle areas that surfaced tensions in the applicability of existing recommendations to AI companion design. Our findings show that ethical and UX-oriented considerations are deeply intertwined and often require context-sensitive application. We document a systematic, multi-method problem analysis that uses these principle areas as an analytic artifact to examine why existing recommendations cannot be directly transferred to AI companion contexts.

---


### 136. [CoArena: Evaluating Computer-Use and Multi-Agent Systems in Real Time](https://arxiv.org/abs/2609.14239)

**<font color=#1a73e8>作者：</font>** Nitish Kovuru, Prateek Jannu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Static benchmarks for computer-use agents fix a task set at release and score every system against it once. That makes them reproducible, and it lets them drift from what they should measure: a fixed task set ages, leaks into training corpora, and cannot follow how people actually use agents from week to week. CoArena measures use directly. Real users submit tasks; two systems, each a single model or a multi-agent pipeline behind the same tool interface, execute the same task concurrently in identical sandboxed desktops; users judge the two outcomes without knowing which system produced them; and a public leaderboard is refit from those judgments. The central contribution is a formal account of what makes such an evaluation real-time. We define real-time as five measurable properties, each with an equation and a worked example: continuous task arrival, live concurrent execution, online rating updates, freshness with contamination resistance, and bounded feedback latency from a failed run to a reusable training environment. The rating methodology follows in full: the Bradley-Terry pairwise model, its likelihood with weighted observations and ties, the penalized maximum-likelihood estimator, and the streaming update applied when a single vote arrives (a stochastic-gradient step on the same likelihood, recovering Elo). It gives confidence intervals from the observed information and a cluster-robust sandwich, rank bands from a parametric bootstrap, the rule by which a new system enters the board, and the convergence rate of the estimate. Vote quality is treated with inter-judge agreement statistics, redundant judging, and explicit handling of ties and abstentions. A five-system example with 211 votes is carried from the vote matrix to ratings, intervals, and rank bands. Every number is derived from stated inputs or labeled illustrative; none is a measurement of a deployed system.

---


### 137. [The Attribution-Compression Frontier in Retrieval-Augmented Generation](https://arxiv.org/abs/2609.14245)

**<font color=#1a73e8>作者：</font>** Deepanshu Mody  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Context compression reduces generator input in retrieval-augmented generation, but answer quality alone does not characterize citation attribution. We measure citation attribution across compression methods and budgets, comparing reranking, extractive selection, abstractive summarization, token pruning, and an extract-cluster-rewrite construction on ASQA and QASPER under a fixed generator and primary entailment evaluator. On ASQA at a nominal 0.25 budget (achieved compression 0.08), a RECOMP-style compressor's citations score 0.86 precision against its summaries but 0.12 against source spans under our re-attributability protocol. These estimates depend on a shared NLI model for span recovery and citation scoring and lack independent human calibration. Extractive selection's observed grounded precision ranges from 0.43 to 0.49 across nominal budgets from one-half to one-tenth of the ASQA context, while answer quality declines. For the same RECOMP setting, claim verification after source recovery yields an unsupported rate of 0.88 versus 0.17 when checking summaries. This gap persists beyond structural rejection of missing provenance, but remains evaluator-dependent. A 200-question TRUE T5-XXL audit also finds emitted--grounded gaps under both fixed and recomputed source mappings, without establishing human-calibrated support rates.

---


### 138. [SPARK: Representation-Level KV Memory Alignment for Safer Vision-Language Models](https://arxiv.org/abs/2609.14258)

**<font color=#1a73e8>作者：</font>** Mohd Azfar, Izhar Dad Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) remain vulnerable to jailbreaks that distribute harmful intent across text and images, making unimodal safety mechanisms insufficient. We investigate whether this vulnerability can be mitigated directly in the multimodal key-value (KV) memory formed during prefill, without modifying model parameters at inference time. We introduce SPARK, a two-stage framework for targeted KV-memory repair. Stage 1 uses a disposable diagnostic adapter to identify harm-associated directions in multimodal key and value representations. Stage 2 projects out these directions, learns a lightweight residual repair, and anchors repaired keys with an image-structural prior to preserve visual grounding. Rather than applying the intervention uniformly, SPARK mixes repaired and original memory using a head-wise coefficient g_h* determined by intervention-relevant subspace energy E_h, requiring no explicit harm classifier at inference.
Across LLaVA-OneVision-7B, Chameleon-7B, Qwen2-VL-7B, and InternVL2-4B, SPARK reduces multimodal attack success while preserving general capability. On LLaVA-OneVision-7B, image-only jailbreak attack success falls to 4.7%, while MMMU remains within 0.6 points of the undefended model (47.8 vs. 48.4) with near-baseline language quality. On MM-SafetyBench, attack success decreases from 39.2% to 12.4%. Even under white-box adaptive joint prompt-image attacks, attack success is limited to 20.3%, compared with 54.6% for the undefended model. These results suggest that multimodal jailbreak behavior can be substantially mitigated by selectively repairing intervention-relevant KV subspaces at prefill, particularly when harmful evidence is carried by the visual modality.

---


### 139. [Vision-Language Models for Criterion-Level Grading of Handwritten Examinations in Outcome-Based Education](https://arxiv.org/abs/2609.14284)

**<font color=#1a73e8>作者：</font>** Md Khalid Syfullah, Asif Hasan Tonmoy, Saad Ahmed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Criterion-level grading connects examination performance to learning outcomes, but manual marking introduces workload and variation between markers. This study evaluates vision-language models (VLMs) for handwritten outcome-based assessment across five dimensions: accuracy, human agreement, repeated-run reliability, error concentration, and explanation quality. Using 1,982 criterion-level records from 485 undergraduate examination answers, we compare 20 configurations spanning Qwen2.5-VL, InternVL3, Pixtral, a Donut baseline, and a cascade ensemble. Evaluation setups include zero-shot prompting, few-shot prompting, partial fine-tuning, and Low-Rank Adaptation (LoRA). Two independent faculty markers regraded all 291 test criteria, providing a human agreement baseline on the same assessment materials. Qwen2.5-VL with LoRA achieved Quadratic Weighted Kappa (QWK) of 0.727 and mean absolute error of 0.435 marks against the examiner, compared with mean human-pair QWK of 0.551. This comparison reflects calibration to the examiner's training marks. LoRA outperformed partial fine-tuning for all three instruction-tuned VLMs, while few-shot prompting reduced QWK in every configuration with valid prompted scores. Aggregate reliability and exact repeatability diverged: intraclass correlations ranged from 0.790 to 0.874, yet 50.2-63.6% of criteria changed marks across five sampled runs. Attention-guided deletion showed no statistically significant advantage over random masking, and four faculty reviewers reached no consensus on explanation usefulness. These findings highlight the need for rubric-specific calibration, repeatable scoring, review of consequential errors, and separate validation of explanations. The released evaluation protocol supports criterion-level assessment research and grading tools with teacher oversight.

---


### 140. [Editorial routing shapes how computational results are qualified in AI-assisted scientific writing](https://arxiv.org/abs/2609.14288)

**<font color=#1a73e8>作者：</font>** Jihan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly analyze computational results and draft manuscripts, making reliable communication as important as correct analysis. Using fixed computational evidence, we tested whether assigning comparisons across modeling choices elsewhere in a research workflow changes manuscript reporting. In constrained sentence-writing tasks, Anthropic's Claude Sonnet 5 often omitted numerical qualifications when detailed comparisons were assigned to a group repository, but retained them more often when the same comparison was assigned to Supporting Information or its own working notes; Claude Opus 5 was less sensitive. These effects did not follow a simple accessibility ordering. A targeted placement rule largely restored sentence-level qualification, whereas a generic accuracy reminder did not. Longer contributions retained numerical qualifications, although some summaries across computational settings were still redirected to the repository. Thus, documenting context within an AI workflow does not ensure its communication where readers encounter the result.

---


### 141. [AnnoSketch: Evaluating and Collecting Human Sketches for MLLM-assisted Chart Annotation](https://arxiv.org/abs/2609.14289)

**<font color=#1a73e8>作者：</font>** Yoonjae Oh, Seon Gyeom Kim, Jae Young Choi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As multimodal large language models (MLLMs) support a growing range of input modalities, increasing work explores how to incorporate rough sketches to convey user intent. For annotated chart generation, it remains unclear what annotation sketches people provide and when such visual input helps MLLMs generate more useful annotations. In this study, we examine when sketch input is useful for MLLM-generated chart annotations across variation in chart type and caption type. In addition, we qualitatively analyze participants' explanations of their output preferences to characterize what made generated annotations more or less helpful. To further document participants' annotation sketches, we present AnnoSketch, comprising 1,600 annotation sketches collected across 160 chart-caption pairs from the conditions in which sketch guidance proved most beneficial, together with participants' annotation intents, perceived comprehension difficulty, and self-reported expressive limitations. We also label these sketches with structured metadata describing how each sketch relates to its caption and how participants express annotations through visual marks. Together, our study and AnnoSketch help determine when to solicit sketch input and provide empirical source for how people sketch chart annotations to support captions. The dataset and supplemental materials are available in our OSF repository.

---


### 142. [E2A-Bench: Benchmarking Evidence-to-Action Reliability in Financial Chart Reasoning](https://arxiv.org/abs/2609.14302)

**<font color=#1a73e8>作者：</font>** Xiaoya Wang, Yutong Xu, Junjie Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can financial vision-language models (VLMs) turn chart evidence into reliable action recommendations? Existing hallucination evaluations are mostly claim-centric; they assess whether generated statements are supported, but not whether evidence remains traceable through rationale, confidence, and final action. We introduce E2A-Bench, a 969-query benchmark for financial chart reasoning, constructed from 323 HS300 constituents under three input modalities with deterministic OHLCV-derived evidence anchors. E2A-Bench evaluates grounding, reasoning-action consistency, evidence-confidence calibration, and directional coverage through UCR, RCI, ECI, and NDR, where NDR measures coverage-aware evidence-to-action reliability rather than realized trading performance. Evaluating 20 VLMs reveals three failures hidden by scalar hallucination scores: the lowest-UCR model ranks near the bottom by NDR due to only 6.4% directional coverage; oracle-aided verification reduces unsupported claims but can collapse coverage; and financial fine-tuning amplifies the BUY:SELL ratio by factors of 4.21 to 4.68 across strict base-fine-tuned pairs. These results show that financial VLM evaluation should trace the full evidence-to-action chain rather than rely on a single hallucination score. Code and data: this https URL

---


### 143. [SpectralShift: Effective Context Window Extension of Gated DeltaNet via Spectral Reparameterization](https://arxiv.org/abs/2609.14320)

**<font color=#1a73e8>作者：</font>** Zian Liu, Yiwen Hu, Zican Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recently, linear attention layers have been increasingly adopted to replace softmax attention at scale for long-context modeling. However, existing context extension approaches typically apply continued pretraining directly without modifying these layers, overlooking the spectral properties of linear attention state dynamics. In this work, we study long-context extension of Gated DeltaNet (GDN) from a spectral perspective of transition matrix and identify two essential factors governing long-range information retrieval: (1) a sufficiently broad slow spectral band aligned with the target dependency length, and (2) the preservation of fast-decaying modes for state clearing and context switching. Based on this observation, we propose SpectralShift, a spectral reparameterization approach for long-context continual pretraining of GDNs. Specifically, SpectralShift reparameterizes the alpha projections initialization to reshape the decay spectrum by enhancing slow propagation capacity, and further introduces a learning-rate scaling for alpha projections to facilitate long-context training. Experiments show that SpectralShift consistently improves long-context capabilities over training, providing an effective and efficient solution for extending context windows of linear attention models. The code has been open-sourced at this https URL.

---


### 144. [Communication-Efficient LLM Adaptation over Decentralized GPU Meshes](https://arxiv.org/abs/2609.14339)

**<font color=#1a73e8>作者：</font>** Sameera Ramasinghe, Shamane Siriwardhana, Thalaiyasingam Ajanthan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized training enables large-model training over low-end GPUs and internet-grade connections, but communication along both data-parallel and pipeline-parallel axes becomes the primary bottleneck. We study post-pretraining adaptation in this setting. We propose an asynchronous two-circuit system: a fast compressed training circuit drives throughput using activation masking for pipeline-parallel (PP) transfer and compressed data-parallel (DP) synchronization, while a slow anchor circuit runs occasional unmasked forward--backward passes off the critical path. Then, we introduce a spectral correction optimizer that uses these delayed anchor priors to denoise masked gradients without blocking the fast stream. Although prior work has found aggressive activation compression unreliable, we show that masking supports post-pretraining adaptation at high compression rates when anchored this way. Pipeline-parallel compression alone yields up to a $9\times$ throughput gain, and combining it with data-parallel compression increases beyond $40\times$ over internet-grade $\sim 200$Mbps connections, while matching dense uncompressed performance across domain adaptation and continual pretraining.

---


### 145. [Two-Stage Mixture-of-LoRA for Multi-Task Medical Vision-Language Learning](https://arxiv.org/abs/2609.14350)

**<font color=#1a73e8>作者：</font>** Zhanghao Chen, Yuanyuan Li, Zhenyu Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) allow a single model to perform clinical image analysis tasks ranging from diagnosis classification to report generation. However, joint adaptation is challenged by heterogeneous output formats, conflicting task gradients, and imbalanced training data. Hence, we present \textbf{Two-Stage Mixture-of-LoRA}, a framework built on MedGemma-1.5-4B. The framework uses a shared-specific Mixture-of-LoRA architecture comprising one shared LoRA and six task-specific expert LoRAs, together with a two-stage training procedure. In Stage 1, we jointly train the shared LoRA and all task-specific expert LoRAs on all tasks. In Stage 2, we first freeze the backbone, the shared LoRA, and all non-target experts, and refine one task expert at a time. Classification and regression then receive an additional modality-balanced continuation, in which smaller modality groups are repeated to match the largest group. In the FLARE 2026 Task 3 test sets, the proposed method achieves 0.85 balanced accuracy for classification, 0.48 micro-F1 for multi-label classification, 0.79 detection F1, and 17.39 regression MAE. Code is available at this https URL.

---


### 146. [ggaction: A Grammar of Graphical Actions](https://arxiv.org/abs/2609.14353)

**<font color=#1a73e8>作者：</font>** Hyeon Jeon, Jinwook Seo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A chart may be declarative; authoring it is not. Visualization grammars often describe charts as finished specifications, whereas people construct them through a sequence of authoring actions. This mismatch can make visualization code difficult for humans to interpret and for machines to generate from human intent. ggaction addresses this gap by modeling the chart authoring process itself. In ggaction, individual authoring actions are abstracted as functions, and the authoring process is expressed as a chain of these functions. This representation more closely aligns chart designers' authoring intent with code specifications, making the code easily understandable to both humans and machines, including language models. Through a series of evaluations, we show that ggaction is sufficiently expressive to capture common chart authoring intents and outperforms widely used visualization grammars, including Vega-Lite and ggplot2, in both human and machine interpretability. ggaction is available at this http URL.

---


### 147. [Formal Properties of Language as Constraints on Neural Dynamics](https://arxiv.org/abs/2609.14384)

**<font color=#1a73e8>作者：</font>** Elliot Murphy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> What must a neural system be capable of to implement language? Current research annotates stimuli with linguistic variables and tests which electrodes, voxels, or language-model layers predict neural activity. Yet predictive success leaves mechanisms under-constrained. Here, we show that algebraic properties of language specify invariants that mechanisms must preserve: non-associative hierarchical grouping, commutativity, recursive closure, access to substructures, and structured workspace transitions. We term this the Neural Admissibility Program (NAP). Syntactic structure building is analyzed algebraically, with candidate mechanisms offered for each requirement: content-addressable workspace memory, graph-structured transient dynamics scheduling structure-building operations (e.g. stable heteroclinic channels), and a phase-coupled sealing operation recording grouping. Simulations show that a corrected Marcolli-Berwick entropy-optimized binding gate preserves grouping only within a narrow commitment band. As an alternative, we propose a novel neural binding operation we term 'Meld': two constituent populations converge through shared synapses, integrate sublinearly, and saturate. Meld is, to our knowledge, the closest neurally plausible composition law to syntactic Merge. It preserves every NAP invariant, uses known cortical operations, and recovers hierarchical structure at every tested depth and temperature. It predicts that effective population dimensionality separates alternative bracketings and that the composite depends on constituent disagreement. Importantly, the laws decoding bracketing most accurately are a priori inadmissible, showing that decoding accuracy alone cannot adjudicate between mechanisms. By specifying how neural dynamics can remain faithful to linguistic structure, the NAP changes the criterion by which neural implementations of cognition are evaluated.

---


### 148. [MOSCOPT: Mixture-of-Skills Collective Optimization for LLM Agents](https://arxiv.org/abs/2609.14399)

**<font color=#1a73e8>作者：</font>** Zhenyu Zhang1, Jiudong Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural language prompts and skills serve as the strategic backbone of LLM-based agents. Recent advances in prompt and skill optimization have achieved notable gains, yet all existing methods optimize a \emph{single} text template---missing the synergy among multiple complementary strategies. We propose MOSCOPT, a text-native, parameter-free algorithm that jointly optimizes a pool of $N$ skills and a gating skill $G$ that dynamically selects $K$ skills per step. To effectively optimize the skills, we build the EditAdam with internally maintained dual states. Through the three-phase interleaved updates with EditAdam, the system monotonically improves without gradient or parameter tuning. Extensive experiments and detailed ablations across 5 benchmarks and 3 target LLMs demonstrate that MOSCOPT consistently outperforms all baselines, and confirm that both the mixture-of-skills architecture with selective activation and the collective evolution with three-phase interleaving are essential to its superior performance. Code is released this https URL.

---


### 149. [Dynamic Learning Solutions: A System for Personalized Educational Video Generation](https://arxiv.org/abs/2609.14408)

**<font color=#1a73e8>作者：</font>** Siddhanth Sridhar, Shreya Chaurasia, Baddela Sai Yaswantha Reddy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an automated pipeline that converts NCERT textbooks into interactive video explanations that respond directly to user queries. A user uploads a PDF and asks a question; the system then generates a video-based explanation as output, handling both text and visual elements from the PDF for multi-modal retrieval and response generation. The pipeline combines a Retrieval-Augmented Generation (RAG) model with generative multimedia components. The RAG stage is optimized for the structure of NCERT textbooks and performs best on content from those books. Given a user query, the RAG model retrieves relevant content from the PDF and generates a multi-scene script containing narrative explanations and structured visual prompts aligned with the textbook's explanatory style. These prompts are passed to a Stable Diffusion module, implemented layer by layer for interpretability and control, which generates contextually relevant images. The images are then processed by DynamiCrafter to produce animated sequences. Finally, a Google Text-to-Speech module generates synchronized narration, aligning speech with the visual scenes through time-based control. The result is a coherent video explanation integrating animation, narration, and textbook-aligned visuals, transforming static educational material into an engaging learning experience. By combining multi-modal document retrieval, generative visual models, animation frameworks, and speech synthesis, this pipeline demonstrates a scalable approach to delivering interactive, personalized digital education content.

---


### 150. [Question's Gambit: The First Move Matters in Agentic Deep Search](https://arxiv.org/abs/2609.14412)

**<font color=#1a73e8>作者：</font>** Radin Hamidi Rad, Amin Bigdeli, Negar Arabzadeh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research agents answer complex questions through iterative loops of searching, reading, and reasoning. Recent work on reasoning-intensive benchmarks such as BrowseComp-Plus shows that well-configured lexical retrieval can surface high-quality evidence, yet agents may still fail to connect documents carrying evidence to the gold documents. We identify a deep research agent's first retrieval move as an important design decision for this setting. We introduce Question's Gambit, a first-move retrieval module that decomposes the question into a set of clues, reformulates them into complementary searches, consolidates the retrieved results, and reranks the candidate pool before the agent begins its iterative search-and-reasoning process. This produces an opening context designed to support both clue aggregation and final-answer verification. We further evaluate on MultiHop-RAG to test whether these benefits transfer beyond BrowseComp-Plus to a more conventional multi-hop question structure. Experiments on BrowseComp-Plus show that Question's Gambit improves retrieval recall and downstream agent accuracy over strong baselines, improving answer accuracy from 83.1% to 90.5% with gpt-5.5 over Pi-Serini, the strongest reported agentic baseline. Our results confirm that effective agentic deep research depends not only on the tools available inside the loop, but also on the quality of the first move. We published our implementation publicly at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-368](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
