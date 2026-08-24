# 🧠 大模型相关研究 | 2026年08月25日

> 本类共 **170** 篇论文：已确认 **154** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-170](./part-04.md)

---

### 1. [SDAD: Spec-Driven Agentic Development for the AI-Native SDLC](https://arxiv.org/abs/2608.20341)

**<font color=#1a73e8>作者：</font>** Vu Hung Nguyen, Thanh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier coding agents backed by large language models with context windows from hundreds of thousands to millions of tokens are restructuring the Software Development Life Cycle (SDLC). Rich context handling and multi-step reasoning now allow substantial Functional Requirement Documents (FRDs) and repository context to be ingested in a single workflow, making specification quality the execution fuel for autonomous delivery. This report formalises Spec-Driven Agentic Development (SDAD) as a synthesis of disciplined up-front formalisation and high-velocity implementation: intent capture, machine-readable specification, agentic synthesis, and independent multi-agent verification under human sign-off. We revisit the historical pendulum between Waterfall and Agile, introduce AI-code as a fourth production paradigm, and compare Human-Agile (circa 2020) with Agentic-SDAD (circa 2026) across artefacts, cadence, accountability, and security posture. Beyond process description, we extend the model to team role metamorphosis (engineer, QA, platform, and product functions), quantitative governance (Ambiguity Tax, Spec Fidelity, SER, and TCI_agentic with repair multiplier phi), and pragmatic adoption via hybrid estimation and a staged migration blueprint. Industrial and research evidence on AI-augmented testing and verification is integrated to motivate separation between synthesis and release authority. Overall, the paper argues that agentic speed does not eliminate engineering discipline; it relocates discipline upstream into specification precision, explicit gates, and auditable provenance.

---


### 2. [PrimeAgentOrchestrator: Memory-Primed Agent Spawning for Personal AI Infrastructure](https://arxiv.org/abs/2608.20342)

**<font color=#1a73e8>作者：</font>** Myron Koch  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) coding agents start each session with an empty context window, discarding accumulated knowledge from prior work. We present PrimeAgentOrchestrator (PAO), a system that spawns new instances of Claude Code -- Anthropic's terminal-based coding agent -- pre-loaded with relevant memories compiled from the user's existing personal databases. At spawn time, PAO queries two independently-operated memory backends in parallel (a PostgreSQL entity-observation database and a Cloudflare Worker semantic search index), fuses results using backend-specific retrieval strategies, and delivers the compiled briefing via filesystem injection that exploits the host agent's configuration auto-read behavior. PAO manages the full agent lifecycle including trust pre-seeding, readiness polling with error detection, and adaptive terminal text injection. We report on four months of regular deployment (December 2025 through March 2026) as an experience report, documenting three generations of context delivery mechanisms, the failure modes that motivated each redesign, and the engineering tradeoffs of bridging heterogeneous memory systems rather than building a unified one.

---


### 3. [Beyond Raw Transcripts: Structured Persona Extraction for LLM-Based Digital Twins](https://arxiv.org/abs/2608.20344)

**<font color=#1a73e8>作者：</font>** Iris Ye, Tianze Deng, Ozan Candogan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based "digital twins" aim to simulate how an individual would behavein new environments or respond to novel questions, given some representation of that individual's prior responses. A common approach constructs this representation from survey transcripts or summaries responses. Prior work shows that compressing long transcripts into shorter LLM-generated summaries does not significantly reduce predictive accuracy, suggesting that information volume is not the primary bottleneck.
In this work, we argue that the key limitation is instead structural:how persona information is organized before being provided to thesimulator model. We study this by comparing unstructured summaries with structured persona representations. First, we introduce a hand-craftedschema (BDE: Background, Decision procedure, Evaluation), grounded in consumer-behavior theory, and show that it improves predictive accuracy over raw transcripts by +1.91 percentage points on a homogeneous benchmark (Twin-2K-500), with similar gains on gpt-5.4-mini and Qwen3-8B as robustness checks. However, this fixed structure does not generalizeacross more heterogeneous tasks, where performance is statistically indistinguishable from the raw transcript baseline.
To address this limitation, we propose an automatic structure-discovery pipeline in which an LLM iteratively proposes and refines task-specific persona structures and extraction prompts. On a benchmark of 13 diverse sub-studies, this approach restores performance, improving mean accuracy by +1.91 percentage points over the raw transcript baseline and eliminating significant losses observed with the fixed schema.
Overall, our results suggest that the main constraint in LLM-based digital twins is not how much information is provided, but how it is structured -- and that the optimal structure depends on the task.

---


### 4. [When Vocabulary Comprehension Fails Clinical Reasoning: Evaluating Therapy Bots' Safety Risks for Generation Alpha](https://arxiv.org/abs/2608.20345)

**<font color=#1a73e8>作者：</font>** Manisha Mehta, Virendra Mehta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational AI systems have become informal mental health support resources for Generation Alpha (Gen Alpha, born 2010-2024), with 13.1% of U.S. adolescents (5.4 million) using generative AI for mental health advice. While these systems, from therapy apps to general chatbots, rely on large language models trained on extensive psychological literature, their safety for youth communication patterns characterized by hyperbolic language, ironic positivity, rapid semantic drift, and contextual polysemy remains unvalidated. Following multiple adolescent deaths linked to AI chatbot interactions, systematic evaluation is critical. We present two benchmarks: (1) 64 Gen Alpha mental health expressions validated by native speakers (ICC=0.72) and clinicians (kappa=0.78); (2) 75 multi-turn conversations (780 turns) with paired Standard/Gen Alpha versions. Across evaluations of LLM architectures underlying therapy apps and general chatbots - Claude, GPT-4o, Llama-3.1 - models understand 76-82% of vocabulary but correctly calibrate only 64-72% of clinical risk, creating a 10-14 percentage point (pp) vocabulary-comprehension gap (p<.001, d>0.48) absent in human therapists (3pp, p=.22). The gap is architecturally consistent and widens with ambiguity (7pp -> 18pp). We identify six failure patterns: sarcasm masking (29pp), minimization acceptance (43pp), informal style bias (24pp), risk-stratified ambiguity (19pp), semantic drift (19pp), context-dependent violence (7pp). Patterns compound; three or more yield 94% miss rates. Lightweight mitigations fail; only heavy scaffolding achieves human performance (6.4x cost). With 34% baseline miss rate yielding 146,880 estimated annual missed crises, we recommend mandatory human-in-the-loop architectures, quarterly youth-specific validation, transparent performance disclosure, and regulatory frameworks for youth-facing mental health AI.

---


### 5. [Who Do Language Models Think Is Competent? A Mechanistic Analysis of Occupational Bias](https://arxiv.org/abs/2608.20347)

**<font color=#1a73e8>作者：</font>** Keren Fuentes, Aaron Mueller  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) often pass behavioral bias evaluations, but it remains unclear whether they no longer represent the underlying associations that give rise to biases, or have merely learned not to express them. In this study, we show that representational biases are often detectable, even when behavioral biases are not visible. We introduce a causal framework that decomposes occupational bias into two measurement points: a model's internal representation of a user's competence, and its observable outputs. We derive steering vectors for representations of user expertise, and verify that they causally mediate model behavior in both a question-answering task and a hiring task. Applying this framework to several open-weight models, we find that demographic attributes, such as gender, race, and socioeconomic status, influence a model's representation of user expertise, even in cases where behavioral metrics detect no disparity between demographics. We show that these model representations can influence downstream behavior under intervention, suggesting failure modes that behavioral metrics alone may not detect.

---


### 6. [Inhibitory Attention for Clinical Long-Context Reasoning: Characterizing and Mitigating Lost-in-the-Middle Effects in EHR Processing](https://arxiv.org/abs/2608.20348)

**<font color=#1a73e8>作者：</font>** Sanjay Basu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Electronic health records now routinely exceed 100,000 tokens per patient. Yet large language models exhibit the lost-in-the-middle (LitM) effect: information near the center of a long context is retrieved less reliably than information near the edges. In clinical use this is not benign: the single most consequential fact in a note can sit at its center. We term this the clinical lost-in-the-middle (CLitM) problem, give its first systematic characterization using MedAlign, and compare context-selection strategies as remedies. Across 2,196 instruction-response pairs and six language models, we observe a 21.9 percentage-point gap between peak accuracy (59.5%, 95% CI [46.3, 71.0], 20-30% decile) and trough accuracy (37.6% [23.2, 52.5] at 70-80%); 67.8% of reference answers fall between the 10th and 90th percentiles of the EHR timeline, inside the CLitM trough. We introduce Query-Conditioned Clinical Suppression (QCCS), a lightweight query-conditioned selection gate, and evaluate it against BM25, BM25 with section-header filtering, dense retrieval, and cross-encoder reranking (N=83 held-out instructions). With Qwen2.5-7B-Instruct (16k context), QCCS outperforms all five comparators under LLM-as-judge scoring: for middle-position instructions QCCS reaches 16.7% versus BM25 3.3%, cross-encoder 0.0%, dense 0.0%, and full context 6.7%; overall QCCS reaches 25.3% versus at most 3.6% for retrieval-only comparators. This advantage is not explained by retrieval recall: at k=20, BM25 retrieves the gold evidence sentence in 98.8% of instructions (QCCS 34.9%), yet retrieval arms stay at most 2.6% accurate even when they retrieve it, whereas QCCS reaches 25.0% even when it does not. In this proof-of-concept evaluation, query-aligned context selection predicts EHR instruction-following accuracy better than gold-sentence retrieval recall.

---


### 7. [Beyond Prompt Engineering: A Systematic Analysis of Prompt Lexical Sensitivity and Its Impacts on Quality](https://arxiv.org/abs/2608.20349)

**<font color=#1a73e8>作者：</font>** Qipeng Xie, Zi Liang, Jiafei Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit extreme sensitivity to surface-level prompt variations, in which minor lexical changes can trigger disproportionate performance fluctuations. Moving beyond black-box optimization and coarse-grained templates, we present the first large-scale, n-gram token-level mechanistic analysis of prompt stability, leveraging a dataset of 132,000 prompt variants. Our investigation reveals a fundamental Scaling Law of Prompt Performance Stability: higher average task performance is strongly associated with lower variance and greater robustness across prompt perturbation. We identify two core linguistic drivers underlying this robustness: (1) Domain-Specific Terminology, which tightly anchors semantic boundaries, and (2) Explicit Action Directives, which formalize reasoning trajectories. Together, these elements constrain the model's interpretative space, effectively ``locking in'' more deterministic generation behavior. Building on these insights, we introduce an automated Prompt-Refining Agent that systematically restructures input queries by injecting domain anchoring and operational constraints. Empirical evaluation shows that our approach reduces performance variance by 40.7% in code generation task, while preserving or improving mean performance. These findings provide a statistically grounded and mechanistically interpretable framework for achieving robust prompt engineering.

---


### 8. [Exploratory As-Analyzed No-Detection of Culturally-Marked Predicate-Triggered PII Amplification in a Synthetic-English RAG Probe: A Predicate-Resource-Confounded Audit](https://arxiv.org/abs/2608.20351)

**<font color=#1a73e8>作者：</font>** Yanhang Li, Zhichao Fan, Zexin Zhuang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We ask whether stereotype-loaded queries about culturally marked people leak more personal information from a retrieval-augmented generation (RAG) system than otherwise-equivalent neutral queries. We pre-register a four-culture audit (en-Anglo, es-LATAM, Arabic, Hindi) on a synthetic English PII corpus, comparing five query arms we call the Stereotype-Trigger Leakage Delta (STLD). Two caveats up front. Our locked confirmatory estimator was never run, so every test in the paper is exploratory or sensitivity, with all plan deviations listed in the appendix. And the name-leakage metric is contaminated by a prompt-echo artifact: the model often just re-emits the name we asked about, which inflates apparent leakage without any retrieval at all. On the cleaner channels (email, phone, ssn-like, address), we find no stereotype-driven amplification on any of the four cultures after multiple-comparison correction. Because our sample is only powered for mid-sized effects, and because the culturally marked probes mix stereotype content with cultural markers and heritage practices, we present this as no detection, not evidence of no effect, of culturally marked predicate leakage that is confounded with the underlying resource.

---


### 9. [ExpertIVS: Sociological Expert Driven Individual Value Simulation in Large Language Models](https://arxiv.org/abs/2608.20355)

**<font color=#1a73e8>作者：</font>** Zhen Wang, Yuqi Ren, Yuehan Cui 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have demonstrated considerable potential for social simulation, yet struggle to accurately model individual value systems. Most existing methods mechanically stitch survey responses into prompts, which suffer from semantic fragmentation, failing to capture the internal coherence of human value systems. The value systems of LLMs are typically assessed using static multiple-choice questions, which fail to evaluate the value orientation in real-world dialogue interactions. To address these issues, we propose ExpertIVS, a framework employing 14 Sociological Expert Agents to interpret World Values Survey (WVS) responses through structured professional perspectives, rather than direct responses concatenation. These expert agents perform deep semantic reconstruction to generate robust and internally consistent individual profiles. To evaluate the consistency between LLMs and individual value systems during dynamic interactions, we further introduce a multi-agent debate mechanism. Extensive experiments across 480 individuals from 12 countries demonstrate that ExpertIVS achieves 90.78% value restoration fidelity and significantly outperforms baselines in value generalization (+5.3%). Moreover, ExpertIVS exhibits strong personality discriminability and behavioral consistency, enabling a shift from mere response concatenation to genuine sociological role-playing.

---


### 10. [Self-Speculation for Faster Reasoning Models](https://arxiv.org/abs/2608.20359)

**<font color=#1a73e8>作者：</font>** Ravisri Valluri, Tung Nguyen, Aditya Grover  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are deployed for increasingly complex tasks involving planning and multi-step decision making, but high-quality performance on these tasks often requires generating long reasoning traces. This is a poor fit for latency-sensitive and interactive applications like voice assistants or coding agents, where generation latency can strongly affect user experience. Existing acceleration methods typically focus on token-level generation, without utilizing the structure of reasoning workflows. We introduce SSR: Self-Speculation for Reasoning Models, a training-free self-speculative decoding method that leverages the chain-of-thought (CoT) as a source of speculation. SSR uses the partial-CoT answer distribution as the drafter and the full-CoT distribution as the verifier, deriving both from the same model at different reasoning budgets. This builds on the observation that later partial-CoT responses often exhibit greater semantic and lexical overlap with the full-budget response. Due to this overlap, SSR can accept long draft prefixes at once, leading to large speedups on structured and long-form generation tasks. To further exploit draft-response overlap beyond the contiguous prefix accepted by standard speculative decoding, SSR also incorporates suffix decoding, using the draft to seed a suffix cache and recover useful spans beyond the accepted prefix, further reducing latency on tasks with high lexical overlap between the draft and the final response. We evaluate SSR on multiple structured and long-form generation tasks where it is most useful, and demonstrate a relative improvement of up to 24.1% on total generation latency for popular open-source models such as Qwen3.5 and Gemma-4.

---


### 11. [TriPLU: Bypassing the Gate with Direct Trilinear Product FFNs in Tiny Language Models](https://arxiv.org/abs/2608.20360)

**<font color=#1a73e8>作者：</font>** He Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study whether tiny decoder-only language models benefit from feed-forward layers that directly multiply learned feature projections. TriPLU, a Trilinear Product Linear Unit, replaces the usual gated FFN branch with a product-only degree-3 branch that multiplies three projected streams coordinatewise. In a character-level TinyStories 1M-byte prefix study, TriPLU reaches a mean best validation loss of 1.0637, compared with 1.1017 for closely matched SwiGLU, 1.0780 for a degree-4 product control, and 1.1026 for a degree-2 control. In train-only Byte-BPE experiments, TriPLU also lowers validation and heldout bits per byte on TinyStories and WikiText-2 raw under low-learning-rate settings, with PMI-slice evidence suggesting gains on seen middle- and high-PMI adjacent-token pairs. Constant-learning-rate diagnostics show that product-branch normalization can reduce the high-learning-rate best-checkpoint gap, although final BPB still degrades under hot schedules. The resulting claim is deliberately narrow: direct product FFNs can improve fixed-budget small-model loss in specific low-compute regimes, but the branch is optimization-sensitive and does not establish FLOP-normalized efficiency, scaling behavior, or broad LLM performance.

---


### 12. [Toward Auto-Research: Mining Falsifiable Research Ideas from Paper Knowledge Graphs with Categorical Structure](https://arxiv.org/abs/2608.20361)

**<font color=#1a73e8>作者：</font>** Yuchen Wang, Zhongzhi Luan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated research-idea generation systems built on large language models (LLMs) share a structural weakness: they reduce ideation to free-text recombination, random paper pairing, or embedding-similarity retrieval. The three approaches fail in the same way: each treats a paper as a flat object, a string or a vector, and so quotients away the typed problem-method-metric-claim arrows a researcher actually uses when reasoning about a cross-domain analogy. We recover the missing structure with the minimal piece of category theory that a typed graph alone does not provide: composition, together with identity arrows, which makes it possible to ask whether a proposed analogy preserves relation chains. Concretely, each paper $p$ is modelled as a small category $C_p$ whose objects are extracted typed research entities and whose morphisms are the relations the paper asserts; a cross-paper bridge from $p$ to $q$ is then a partial functor candidate $F: C_p -> C_q$ that preserves object kinds and covered relation classes. We instantiate the model as a three-layer algorithm: categorical signature clustering, a functor-preservation gate, and a six-axis LLM plausibility judge. Evaluated on a corpus of tens of thousands of full-text-parsed papers under four ablation conditions, the categorical gate filters cross-domain candidates at roughly a 17:1 ratio while the quantitative-falsifier rate of accepted ideas stays above 83% throughout; every rejected candidate is retained with its per-axis rationale, so the gate doubles as a logging layer rather than a silent filter.

---


### 13. [Multilingual Verifier Bias in RLVR: Benchmark, Rollout Diagnosis, and the Cross-Lingual Selection Bottleneck](https://arxiv.org/abs/2608.20362)

**<font color=#1a73e8>作者：</font>** Chenyu Zhou, Qiliang Jiang, Xu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is a standard recipe for training large language models on mathematical reasoning, where an answer verifier serves as a language-neutral reward function. We show that this assumption fails in multilingual settings: an exact-match verifier turns format and script variation into language-dependent false-negative reward noise. We introduce a reusable protocol for auditing multilingual RLVR rewards: a verifier-robustness suite, a rollout-diagnosis procedure, and language-conditioned reward-error metrics for Japanese, English, and Chinese answers. On MGSM rollouts with k=8, the exact-match proxy rejects trusted-correct answers at sharply different rates by language across Qwen3-4B, Qwen3-8B, and Llama-3.1-8B-Instruct; for Qwen3-8B, the false-negative rate reaches 0.642 on JP against 0.122 on EN and 0.073 on CN. A plain-numeric probe localizes the mechanism to the final-answer interface: an interface model drives reward-error VLB to zero while the residual accuracy gap is unchanged. We then expose a cross-lingual selection bottleneck: on MGSM250 rollouts, a target-local aggregation rule using no trusted labels closes 55-78% of the average selection gap, and over 95% of repairs require genuine cross-lingual support. The bottleneck replicates on a 483-problem MATH-500 set. A controlled training audit shows that rule-GRPO raises trusted accuracy while the reward-error VLB stays high. The unifying message is operational: multilingual RLVR rewards should be audited by language and by answer interface before they are optimized.

---


### 14. [Hadith computational science in the age of large language models: a critical narrative review](https://arxiv.org/abs/2608.20364)

**<font color=#1a73e8>作者：</font>** Md. Ashraful Haque, Riasat Islam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We examine how hadith computational science is being reshaped by transformer models, retrieval-grounded pipelines, and large language models (LLMs). Recent reviews document growth in the literature, but they do not yet provide a critical account of which advances are methodologically robust, which remain benchmark-bound, and which unresolved problems still limit scholarly use. We address this gap through a critical narrative review that combines critique of existing reviews, paper-level appraisal of representative original studies, and synthesis of Islamic scholar and domain-expert perspectives on authenticity, authority, and responsible use. We find uneven progress. Data resources have expanded, segmentation tasks have matured, narrator and source-verification problems are better formalized, and LLM-assisted workflows now support corpus-scale enrichment, multilingual access, and grounded evaluation. At the same time, progress remains constrained by narrow corpora, weak benchmark comparability, synthetic-to-real transfer gaps, narrator identity resolution, preprocessing fragility, limited reproducibility, and sparse expert-grounded validation. We show that important gaps lie beyond dominant benchmarks: non-canonical and obscure corpora, commentary and explanatory literature, cross-source links with Qur'an and seerah, and fiqh-facing evidence support. We argue that hadith computation should be assessed less as isolated model performance than as an evidence infrastructure problem requiring knowledge integration, provenance, and expert supervision. On this basis, we define a research agenda for making the field methodologically stronger and more useful to Islamic scholarship.

---


### 15. [Trilingual Topic Modeling of Sri Lankan Parliamentary Debates](https://arxiv.org/abs/2608.20365)

**<font color=#1a73e8>作者：</font>** Himath Dhanapala, Haren Daishika, Himandhi Kuruppu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sri Lankan parliamentary debates (Hansards) constitute a trilingual corpus of speeches in Sinhala, Tamil, and English, including code-mixed content, yet remain inaccessible to standard NLP pipelines due to layout-complex PDFs, multilingual scripts, and agglutinative morphology. We present an end-to-end framework that addresses these challenges through LLM-based text extraction followed by a multilingual embedding and density-based clustering pipeline for topic modeling. A hybrid semantic-lexical extension, BiTopic, is further explored to improve interpretability and recover speeches otherwise discarded as noise. Applied to 19,553 speeches spanning 2017-2026, the pipeline recovers 30 macro-topics achieving a cluster purity (BCP) of 0.673, whose temporal trajectories align unsupervised with major national events including the 2019 Easter Sunday attacks and the 2022 economic crisis. Traditional LDA fails on this corpus due to cross-lingual fragmentation, whereas the proposed approach successfully identifies thematic structure across all three languages without supervision.

---


### 16. [ASTAR: Automated induction of STAndardized radiology Reporting templates from large-scale clinical free-text corpora](https://arxiv.org/abs/2608.20369)

**<font color=#1a73e8>作者：</font>** Xinfeng Zhang, Mingxuan Liu, Yifei Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured reporting converts free-text radiology narratives into queryable data keys, facilitating cohort assembly, longitudinal tracking, and training label generation for medical AI. The prevailing paradigm follows a two-stage pipeline: (1) constructing a reporting template, (2) extracting information to populate it. While the extraction stage has benefited from advances in large language models (LLMs), template construction remains a manual bottleneck relying on labor-intensive expert consensus that is static, difficult to scale, and may fail to capture real-world reporting diversity. We address this limitation with \textbf{\texttt{ASTAR}}, an LLM-based framework for Automated induction of STAndardized radiology Reporting templates from large-scale clinical free-text corpora. Extensive experiments on 4,215 fetal brain MRI reports from multiple centers demonstrate that the \textbf{\texttt{ASTAR}}-induced template surpasses two expert-curated templates across template coverage, information fidelity, diagnostic fidelity, and expert-rated usability, reducing template development from weeks of committee deliberation to hours of automated processing. Code: this https URL

---


### 17. [When Do LLMs Replace Fine-Tuned NLU? A Decision Framework for Intent Detection in Production Conversational Systems](https://arxiv.org/abs/2608.20371)

**<font color=#1a73e8>作者：</font>** Carson Rodrigues, Oysturn Vas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A common claim is that zero-shot large language models (LLMs) can replace fine-tuned NLU classifiers for intent detection. We test this claim head-to-head and find that the honest answer is: it depends on the intent space. On full ATIS and CLINC150 we compare a fine-tuned RoBERTa, a TF-IDF+logistic-regression baseline, sentence-embedding kNN, and Claude Haiku zero-shot, reporting bootstrap 95% confidence intervals and paired significance tests. When abundant in-domain labels exist, fine-tuned RoBERTa is as good or better and three orders of magnitude cheaper and faster: on ATIS it beats Claude zero-shot by 11.8 points (95.9 vs. 84.1, p<0.001). On the broad 150-intent CLINC150 schema the two are statistically tied (89.1 vs. 88.5, p=0.24): the LLM matches a fully supervised model with no training data. The LLM's advantages appear in three production-relevant regimes: out-of-scope detection (OOS recall 85.6 vs. 58.1 for RoBERTa); robustness to realistic ASR noise via a controlled text-to-speech to noise to Whisper pipeline (92.5 vs. 80.0 at 0 dB); and dynamic per-deployment schemas, where a classifier trained on one app's intents scores 0% on a new app's intents while the schema-prompted LLM serves both at ~94% with zero retraining. We distill these findings into a decision framework for practitioners.

---


### 18. [An ambiguity taxonomy for evaluating large language model performance on clinical registry abstraction: a multi-site prospective study](https://arxiv.org/abs/2608.20373)

**<font color=#1a73e8>作者：</font>** James Matheson, Betsy Castillo, Andrew Y. Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Objective: To evaluate large language model (LLM) performance on unprocessed electronic medical record (EMR) data for clinical registry abstraction. Methods: We evaluated LLM performance answering registry questions for the American College of Cardiology National Cardiovascular Data Registry (ACC NCDR). In a pilot study at an academic medical center, the model identified candidate data sources for each registry question and experienced abstractors used these results to define question-specific document sets. In a validation study at a second center with a second ACC NCDR registry, the LLM answered questions using the question-specific document sets. Before reviewing any output, two abstractors independently established the ground truth and assigned each question to one of six categories, ordered by the ambiguity and clinical reasoning required to resolve it: Medication/Event Flag, Binary Clinical Presence, Administrative, Quantitative Laboratory/Physiologic, Clinical Interpretation, and Event Timing. Results: The analytical sample comprised 9,430 abstractor answers reconciled to 4,715 consensus answers (501 pilot; 4,214 validation). In the pilot, candidate data sources per question averaged between 14.6 (SD 13.9) for demographics and 89.2 (SD 56.1) for history and risk factors. In validation, human inter-rater agreement was approximately 98\% while 87\% of LLM answers exactly matched consensus, 2\% partially, and 9\% did not. Mean question-level accuracy was 91.5\% (SD 13.4\%) across 157 questions with at least 20 answers, and declined as ambiguity increased, from 96\% for Medication/Event Flag to 62\% for Event Timing questions. Conclusions: LLMs answering clinical registry questions on unprocessed EMR data achieved far lower accuracy than human abstractors. LLM accuracy fell steadily as ambiguity and the level of required clinical reasoning increased.

---


### 19. [VA-DPO: Valence-Arousal Direct Preference Optimization for Controllable Emotion Generation in Language Models](https://arxiv.org/abs/2608.20374)

**<font color=#1a73e8>作者：</font>** Hyunwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How precisely can we tell a language model how to feel? Most work on emotional generation answers with a discrete label - happy, angry, sad - which cannot express a target like "mildly downcast but calm." We instead specify the desired affect as a continuous point (v*, a*) in the Valence-Arousal plane and train the model to hit it. Our method, VA-DPO, is a small modification to Direct Preference Optimization: a frozen VA regressor scores each sampled generation by its Euclidean distance to the target, we keep only candidate pairs whose distance gap clears a margin tau, and we optimize a LoRA adapter with the ordinary DPO loss against a frozen reference. The DPO objective itself is unchanged; what is new is how the preference data is built. On Llama-3.1-8B-Instruct this cuts mean VA distance to the target by 33% over system-prompting and 25% over few-shot prompting, lifting valence/arousal correlation to r_v=0.93 and r_a=0.75. The gains carry over to Qwen3-8B and Llama-3.2-3B, and they do not come at the usual price: MMLU is unchanged (Delta=+0.0) and HellaSwag and TruthfulQA are preserved. We release the code, configs, and the preference-construction pipeline.

---


### 20. [GRAFT: Adaptive DLM-Based Draft Tree Construction with Target-Distilled Edge Scoring](https://arxiv.org/abs/2608.20375)

**<font color=#1a73e8>作者：</font>** Xuming Ye, Zeming Ma, Runjie Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tree-based speculative decoding raises the mean accepted tokens of standard speculative decoding by verifying multiple draft paths, and existing tree builders typically construct these paths through parent-conditioned expansion, where each child token is generated conditioned on its parent path. This construction is incompatible with diffusion language model (DLM) drafters such as DFlash, which produces all future-position distributions in a single forward pass. DDTree bridges this gap by treating high-probability tokens from each future-position distribution as candidate nodes and selecting edges between consecutive positions under a fixed node budget. However, its edge selection relies on token probability alone without modeling parent--child compatibility, so target-compatible tokens can be attached to wrong parents; moreover, its fixed budget ignores that the throughput-optimal tree size varies with the decoding state. We propose GRAFT, a draft-tree construction framework for DLM-based speculative decoding. GRAFT introduces Target-Distilled Edge Scoring (TDES), which distills parent--child preferences from target-model traces to select target-compatible edges, and State-Aware Budget Allocation (SABA), which sets the per-round tree budget by balancing expected draft gain against verification cost. Across multiple models and tasks, GRAFT achieves $2.13\times$--$6.36\times$ end-to-end speedup over autoregressive decoding while adding less than $0.5$\,ms of overhead per round, approximately $1.4\%$ of the target-model verification latency.

---


### 21. [TH-GNN: Heterogeneous Temporal Graph Neural Networks for LLM-Agent Shilling Attack Detection](https://arxiv.org/abs/2608.20376)

**<font color=#1a73e8>作者：</font>** Shivam Swarup, Divya Prakash Shrivastava, Rakesh Thakur  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents can now generate realistic shilling profiles, fluent reviews, and coherent ratings at scale, systematically defeating recommender-system defenses. Text-only detectors that flag semantic drift in review embeddings are blind to graph structure and temporal coordination, while graph-only detectors that exploit neighborhood anomalies cannot reason over review semantics or the cross-modal inconsistencies produced by LLM-generated content. We propose TH-GNN, a heterogeneous temporal graph neural network with a two-layer Heterogeneous Graph Transformer backbone that applies per-type and per-relation attention augmented with learnable sinusoidal temporal encodings on every edge. Cross-modal attention fuses structural user embeddings with frozen RoBERTa representations of reviews and item descriptions, while a GRU operating over log inter-arrival times captures temporal burstiness. Evaluated across five attack families and four benchmark datasets, TH-GNN achieves a grand-mean F1 score of 0.870, outperforming the strongest text-only baseline on Agent4SR attacks by 10.9 percentage points and 11.5 percentage points at the lowest injection rate. These results demonstrate the effectiveness of jointly modeling temporal, structural, and semantic signals for detecting sophisticated LLM-driven shilling attacks.

---


### 22. [A Survey on Foundations and Frontiers of Multimodal Agentic Frameworks: Techniques and Applications](https://arxiv.org/abs/2608.20379)

**<font color=#1a73e8>作者：</font>** Neel Mokaria, Rishie Raj, Dheeraj Baiju 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in large language models (LLMs) have fueled a wave of research into agency: the ability to reason, plan, and act. This effort has produced agentic frameworks that orchestrate perception, memory, and decision-making around powerful LLM backbones. With the advent of large multimodal models (LMMs), these systems can process and integrate diverse modalities, including images, audio, and video, thereby improving their real-world applicability. Yet, while surveys of LLM-based agents exist, the role of multimodality in shaping agency has not been systematically examined in recent years. This survey fills the gap by analyzing the impact of multimodality across the core functional modules of the agentic framework: perception, reasoning, planning, memory, and action. Using this lens, we trace the evolution from text-centric agents to multimodal frameworks, examine how modalities are integrated through delegated, late-fusion, and early-fusion architectures, and assess the emergence of agentic behaviors enabled by grounded perception and multimodal reasoning. We organize existing work through a modality-centric taxonomy that links architectural design choices to agent capabilities. Moreover, we review multimodal agentic systems across various application domains, including Robotics, GUI & Web Navigation, Multimedia Content Generation & Editing, and Long-form Video Understanding & Retrieval. Beyond capabilities, we analyze performance across these settings and discuss efficiency-scalability trade-offs, including training and inference costs, latency, and deployment constraints. By focusing on the impact of multimodality in agentic design, we aim to identify key gaps and chart a roadmap toward robust and general-purpose intelligent systems.

---


### 23. [EditPPT: Faithful Long-Deck Slide Editing via Structured Tool-Using Multi-Agent with Dual-Modal Validators](https://arxiv.org/abs/2608.20381)

**<font color=#1a73e8>作者：</font>** Jiheon Kim, Kyudan Jung, Jaegul Choo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automating slide editing requires simultaneously satisfying modification accuracy, preservation fidelity, and robustness to deck length. Existing LLM-based systems often fail on real-world presentation files because they rely on idealized intermediate representations or open-ended code generation, which are prone to cascading errors in long decks. We introduce EditPPT, a multi-agent framework that reformulates slide editing as a constrained tool-selection problem. By executing localized shape-level operations through the native PowerPoint COM interface, EditPPT narrows the LLM action space while preserving the application-resolved structure of user-authored decks. By separating validation across modalities, our dual-modal validation provides more robust assessment of both instruction fidelity and visual quality. We also present DeckEdit-Bench, a benchmark with 28 human-authored decks, 582 slides, and 183 editing prompts across short, medium, and long deck tiers. Experiments show that EditPPT achieves a 99.5% execution rate, 88.7% slide-targeting F1, 82.5% instruction following, and 91.5% object preservation overall, while maintaining strong performance on long decks. Our code and benchmark are available at this https URL

---


### 24. [Decoupled Vision-Language System for Multimodal Understanding and Generation](https://arxiv.org/abs/2608.20382)

**<font color=#1a73e8>作者：</font>** Yifan Xu, Baochen Xiong, Xiaoshan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a new architecture design for multimodal large language models (MLLMs), Libra, capable of both multimodal understanding and generation. Libra architecture contains one vision system and one language system, connected by cross-modal bridges. This design decouples self-modal modeling and cross-modal interaction, enabling each modality to learn its unique representations while maintaining effective cross-modal comprehension. The decoupling is mainly achieved in a switch attention module and a switch FFN module, which dynamically routes the computation flow for self-modal modeling and cross-modal interaction scenarios. We evaluate the effectiveness in two important settings: \textbf{Libra-1} for the understanding-only image-to-text setting, and \textbf{Libra-2} for unified image-to-text understanding and text-to-image generation. In addition to the architecture design, we discuss various improvements on tokenization, positional encoding, and supervision. Experiments demonstrate that the dedicated Libra design enables mutual improvements on multimodal understanding and generation, achieving strong performance on both understanding and generation benchmarks.

---


### 25. [Using Human-LLM Disagreement to Improve Checklist-Based Quality Appraisal](https://arxiv.org/abs/2608.20385)

**<font color=#1a73e8>作者：</font>** Timo van der Kuil, Bruno Messina Coimbra, Mirjam van Zuiden 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systematic reviews rely on quality appraisal of included studies, a process that is time-consuming and sensitive to ambiguity in checklist criteria. Although large language models (LLMs) offer opportunities to support these tasks, appraisal checklists are typically treated as fixed inputs, and it remains unclear how their design affects agreement with expert judgments. Therefore, we investigate (1) whether LLMs can approximate human judgments in checklist-based appraisal and (2) whether patterns of human-LLM disagreement can be used to identify and improve ambiguous checklist items. Using the Guidelines for Reporting on Latent Trajectory Studies (GRoLTS) checklist, we compare LLM-generated assessments with expert annotations across three research topics and two checklist versions. Agreement is assessed using item-level accuracy, chance-corrected agreement, and preservation of study-level rank ordering.
We find that performance varies substantially across checklist items, with ambiguous and conditional criteria producing the greatest disagreement. Revising these items improves both raw and chance-corrected agreement. Although item-level misclassifications persist, LLM-generated scores often preserve the relative ranking of studies when high-agreement items are retained. These results indicate that reliable LLM-assisted appraisal depends not only on model choice but also on checklist design. The findings suggest that analyzing human-LLM disagreement can help identify problematic checklist items and support the iterative improvement of research synthesis workflows.

---


### 26. [Poly-InstructTTS: Learning In-the-Wild Expressive Speech Synthesis from Open-Ended Instructions](https://arxiv.org/abs/2608.20387)

**<font color=#1a73e8>作者：</font>** Junhui Zhang, Qianhui Xu, Qingxiang Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While recent text-to-speech (TTS) models achieve high naturalness, controlling fine-grained expression via natural-language instructions remains challenging. We introduce Poly- InstructTTS, which learns expressive speech from open-ended instructions using in-the-wild audiovisual data. We build a scalable multi-modal pipeline to construct a 1,000-hour instruction-annotated corpus covering 1,000+ fine-grained emotions and styles. The framework uses a prompt-free GPT with attribute-based thinking tokens, followed by a flow-matching module that injects timbre from a reference audio. We also present a speaker fine-tuning procedure to transfer instruction control to specific speakers while preserving persona. We further extend InstructTTSEval with broader tasks. Experiments show that Poly-InstructTTS delivers strong performance in instruction adherence and expressiveness. Audio demos and the expanded testset are available on our project page.

---


### 27. [Intent Engine: Natural-Language Intent Translation for Intent-Driven Orchestration in the Compute Continuum](https://arxiv.org/abs/2608.20388)

**<font color=#1a73e8>作者：</font>** Koushikur Islam, Rodrigo N. Calheiros  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Microservice placement in the compute continuum is driven by low-level Service-level Objectives (SLOs), but requiring users to specify metric-level constraints creates an adoption barrier and increases misconfiguration risk. Although large language models (LLMs) can interpret natural-language intents, direct generation of orchestration-consumable SLO artifacts remains unreliable due to unsupported constraints, incorrect grounded values, and schema violations. These errors can propagate to downstream placement logic and produce infeasible or incorrect placements. This paper presents Intent Engine, a natural-language intent translation architecture that constructs validated SLO artifacts for compute-continuum service placement. Intent Engine acts as an intent acquisition and SLO construction layer for existing intent-driven orchestration and placement frameworks; it does not perform placement or runtime QoS optimization. The architecture combines schema-constrained extraction, retrieval-grounded value construction from monitored infrastructure state, and validation against supported constraints before emitting the final SLO artifact. We evaluate Intent Engine using a 716-record intent-to-SLO dataset derived from an edge-cloud testbed, including valid and invalid intents. Across GPT-4.1 mini, Claude Sonnet 4.5, and DeepSeek V4-Flash, Intent Engine outperforms prompting baselines and a non-LLM rule-based parser. With GPT-4.1 mini, it achieves 0.941 total F1 Score and reduces aggregate hallucination by 85.1%, while lowering downstream placement failure from 30.8% to 2.1%.

---


### 28. [Ansari: A Retrieval-Grounded Islamic AI Assistant -- Architecture, Deployment, and Lessons from 140,000 Conversations](https://arxiv.org/abs/2608.20390)

**<font color=#1a73e8>作者：</font>** M Waleed Kadous, Amr Elsayed, Abdullah Al Nahas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General-purpose large language models (LLMs) are increasingly used to answer religious questions, but for Islamic content they carry two serious risks: factual fabrication (inventing Qur'anic verses or hadith) and subtle value misalignment. We present Ansari, a deployed, retrieval-grounded Islamic AI assistant that has handled more than 140,000 conversations across 25+ languages since June 2023. Ansari is built around an agentic retrieval loop: a tool-using language model issues searches against authenticated Islamic corpora -- the Qur'an, hadith collections, a multi-volume jurisprudence (fiqh) encyclopedia, and exegetical (tafsir) sources -- and answers only on the basis of what it retrieves, with citations attached for verification. We describe the system's architecture (the agent loop, the retrieval tools, the corpora, and the system prompt that encodes editorial and theological policy), its multi-platform deployment (web, mobile, WhatsApp, and as a Model Context Protocol server and an Agent Skill), and what 140,000 real conversations reveal about how Muslims actually use such a tool. We report results on several complementary evaluations -- zero-shot performance on accredited institutional exams, a human-rated validation during Ramadan, and two independent, externally run benchmarks on which Ansari currently tops the public IslamicMMLU leaderboard ahead of frontier models and is competitive on Islamic legal reasoning (IslamicLegalBench) while strongly resisting false premises -- and draw out lessons that generalize beyond Islam to any faith- or values-sensitive deployment of LLMs: grounding is necessary but not sufficient, the system prompt is a theological as much as a technical artifact, and the absence of community in how models are formed remains a hard gap.

---


### 29. [ImmigrationReason: A Structured Dataset of U.S. Immigration Appeals for Legal Reasoning Research](https://arxiv.org/abs/2608.20391)

**<font color=#1a73e8>作者：</font>** Amirhossein Afsharrad, Seyed Shahabeddin Mousavi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most legal NLP resources draw from federal case law and focus on coarse classification, leaving administrative adjudication, where the vast majority of government decisions occur, essentially unaddressed. We introduce ImmigrationReason, a large-scale structured dataset derived from 12,375 non-precedent decisions of the U.S. Citizenship and Immigration Services (USCIS) Administrative Appeals Office (AAO) spanning 2005 to 2026. Each record captures the applicable legal framework, per-criterion evidence-sufficiency findings under a five-category label, verbatim adjudicator-criticism quotes, all citations, and final dispositions, alongside high-quality Claude-transcribed source text. Extraction quality is validated through a three-pass pipeline combining two independent modalities with comparison-prompt adjudication by Opus 4.7, and verified by domain experts on a 500-record sample. The dataset documents nearly 9,000 verbatim instances of AAO-identified legal errors, spans a natural legal-regime transition (the 2016 Dhanasar rule change), and covers 21 years of adjudication. We analyze the dataset in detail and outline research directions it enables, from outcome prediction and adjudicator-error analysis to agent design for high-stakes regulatory domains.

---


### 30. [Evaluation-as-Search: Adaptive Discovery of Grounding Failures in Meeting Assistants](https://arxiv.org/abs/2608.20392)

**<font color=#1a73e8>作者：</font>** Sami Khairy, Yasaman Hosseinkashi, Vishak Gopal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-powered meeting assistants are deployed at scale, yet systematic evaluation of their grounding fidelity remains limited to static benchmarks that miss failure modes tied to specific discourse structures or reasoning demands. We propose Evaluation-as-Search (EaS), a feedback-driven methodology that frames quality evaluation as an adaptive search over the space of natural questions a meeting participant might ask. Rather than sampling uniformly, EaS learns from evaluator feedback across iterations to concentrate probing effort on cognitive demands where failures are most likely, guided by a UCB-scored coverage map and blind multi-dimensional quality evaluation. Using EaS, we construct MeetingProbe, a benchmark of over $3{,}000$ annotated question--answer pairs spanning 20 transcripts from three meeting genres and three LLM assistants. In ablations, adaptive search surfaces $2.5\times$ more failures than random probing ($7.1\%$ vs. $2.9\%$ finding rate), with the strategic planner contributing the largest individual effect. Across three models, we observe a clear capability gradient and identify eight recurring failure categories dominated by discourse-pragmatic challenges rather than factual recall errors. We further validate MeetingProbe across multiple model families and providers, finding a clean capability gradient and a curated subset of universal failures that no model handles. MeetingProbe is released publicly to support reproducible evaluation of meeting assistant grounding fidelity.

---


### 31. [Knowledge-Graph-Gated Defactualization for Style-Controllable and Fact-Preserving Generation in Agentic Conversational AI](https://arxiv.org/abs/2608.20393)

**<font color=#1a73e8>作者：</font>** Tanmay Kumar Shrivastava, Darsh Rohit Nandu, Rajesh Kumar Mundotiya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic large language models (LLMs) deployed in fact-sensitive applications such as customer support must simultaneously preserve factual correctness and generate responses in a controllable stylistic register. Activation steering enables fine-tuning-free style control by perturbing hidden representations, but it lacks an explicit mechanism for distinguishing verifiable facts from stylistic content, leading to semantic leakage. We address this challenge through \emph{Defactualize-Steer-Rehydrate} (DSR), a knowledge-engineering framework that integrates a typed, salience-weighted knowledge graph (KG) with activation steering. DSR extracts salient entities using a layered regex or NER or lexical-classifier pipeline, replaces them with typed placeholders prior to steering, and deterministically restores verified values through salience-guided rehydration after generation. DSR is evaluated across six LLaMA-family models (1B--13B parameters) on 600 A2A-generated customer-support cases (1,200 generations), with a dedicated KG ablation study. DSR significantly increases verified-entity recovery relative to a steering-only baseline (Cohen's $d=0.225$, $p_{\text{Bonf}}=1.0\times10^{-4}$), though the absolute recovery rate remains modest, while preserving effective style control across diverse model families. Layer-wise separability and steering-strength diagnostics further show previously unexplored interactions between representation-level steering and factual grounding. hese results demonstrate that explicit knowledge engineering can systematically enhance trustworthy, controllable, and reproducible generative AI without requiring model fine-tuning. Code, cached steering vectors, and evaluation scripts are publicly released to support reproducibility.\footnote{this https URL}

---


### 32. [Nexus: Depth-Adaptive KV-Cache Splicing and Retrieval-Decoupled Tool Routing for Agentic LLMs on Unified Memory](https://arxiv.org/abs/2608.20397)

**<font color=#1a73e8>作者：</font>** Mustafa Arslan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic large language models (LLMs) on the Model Context Protocol (MCP) re-encode verbose tool schemas every turn, so prefill - quadratic in sequence length - dominates time-to-first-token (TTFT) as the tool registry grows. Nexus's primary lever is to decouple routing from the schema-prefill cost: an INT8 semantic lookaside buffer (SLB) with a calibrated cross-encoder margin gate selects tools by retrieval, and arguments are generated over a compressed textual signature (median 19 tokens) rather than over spliced key/value (KV) cache. This path is depth-independent: routing accuracy stays near 89% as the registry scales to 250 tools - where a concatenate-all-schemas baseline overflows the context window entirely - and it reaches a first-argument token 1.66x sooner than a full-schema re-prefill at a ~80% main-context token saving. As a secondary, bounded lever we transplant a compiled schema KV block directly into the live context. This is fundamentally limited by rotary position embedding (RoPE) phase drift: an anchored splice is output-exact, but off-anchor placement corrupts attention, so beyond a threshold P=256 Nexus repairs the seam with a depth-adaptive suffix redecode that escalates to a full re-prefill. The resulting never-regress property is a guarantee on output fidelity (top-1 agreement, D_KL approx. 0) - not on latency, which can dip to 0.98x before converging to parity - alongside a 1.1-1.7x TTFT speedup at moderate depth that narrows to parity at deep context. Two negative results bound the design: the off-anchor RoPE fidelity boundary, and the failure of a reference-free drift gate to predict drift (Spearman rho = 0.193). All measurements are from one model tuple (Qwen2.5-14B-Instruct Q4_K_M) on Apple-silicon unified memory; the qualitative boundaries generalize, while the quantitative envelope is tuple-specific.

---


### 33. [Environmental Slow AI: Design Principles for Generative Systems](https://arxiv.org/abs/2608.20398)

**<font color=#1a73e8>作者：</font>** Vanessa Utz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI (genAI) systems produce cultural artefacts at scale, but they also reflect embedded cultural values through their design. Once identified, these values become open to deliberate reshaping. This position paper examines the maximalist values of current generative AI through an environmental humanities tradition and proposes design principles in which environmental sustainability serves as the core value instead. The principles are developed under the umbrella of Slow AI, a term that already circulates across several distinct research and practice programs. Five design principles are articulated (restraint, sufficiency, selectivity over retention, material visibility, and friction as affordance), each of them illustrated against the current design of widely deployed systems. Each principle operates at two levels: a design implementation, and an interpretive layer at which users and developers are prompted toward reflective engagement with the system. Together these principles extend human agency by restoring decisions that frictionless defaults have silently removed and do so by building interpretive reflection into design.

---


### 34. [ARGUS: Theory-of-Mind Guided Argument Generation with Strategy-Aware Planning and Knowledge Grounding](https://arxiv.org/abs/2608.20405)

**<font color=#1a73e8>作者：</font>** Zhe Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persuasive argument generation requires modeling audience beliefs, rhetorical strategies, and factual grounding. Despite recent advancements, existing methods remain largely audience-agnostic and fail to integrate strategy selection to improve persuasiveness. To bridge this gap, we propose Argus, an agent-based framework that operationalizes classical rhetoric for persuasive writing. At its core, a Theory-of-Mind (ToM) Reasoner constructs an explicit dual mental model of the audience's beliefs and values to guide downstream decisions. This representation conditions a component-aware planner that decomposes the argument into subtopics, assigns fine-grained rhetorical functions (logos, pathos, ethos, kairos), and triggers strategy-guided evidence retrieval at planning time. Finally, a refinement module iteratively targets and resolves multi-dimensional weaknesses without quality regression. We evaluate Argus across three diverse benchmarks using both automated pairwise Elo and LLM-as-judge metrics. Results show that Argus consistently outperforms strong baselines across multiple backbone models, achieving top rankings and the highest overall scores. Targeted simulation experiments further validate its effectiveness in shifting resistant audience stances.

---


### 35. [StateSight: Benchmarking Latent Spatial-State Reconstruction in Vision-Language Models](https://arxiv.org/abs/2608.20414)

**<font color=#1a73e8>作者：</font>** Michelle Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models are increasingly used for multimodal question answering, yet their ability to reconstruct latent spatial structure from a single image remains difficult to isolate. Broad benchmarks often combine perception, optical character recognition, domain knowledge, linguistic priors, and reasoning in the same evaluation. We introduce StateSight, a procedurally generated benchmark for cube-net opposite-face reasoning, occluded cube-tower counting, and 4-neighbor connected-component counting. Each task family contains 300 single-image prompts with deterministic oracle labels and exact-match scoring. OpenAI GPT-5.5, using the API model identifier gpt-5.5, achieved 59.3%, 33.3%, and 28.3% accuracy across the three tasks, while Claude Sonnet 5 achieved 53.3%, 18.7%, and 7.3%. All final direct runs had zero format errors. A 30-participant human baseline on 60 items exceeded both models on every task, with mean accuracies of 80.8%, 68.8%, and 64.3%. Visible-derivation analysis identified recurring errors in image-state reconstruction and reasoning procedure. We also introduce StateSight-Steps, a companion dataset of 900 interleaved image-text examples and 3,600 deterministic intermediate visual states. The results show that format-valid responses can mask failures to recover the spatial structure required for verifiable visual inference.

---


### 36. [BF1: A Causal Dyadic Sparse-Attention Retrofit for Efficient Long-Context Transformers](https://arxiv.org/abs/2608.20427)

**<font color=#1a73e8>作者：</font>** Hina Dixit  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dense causal attention remains expensive at long context even when implemented with highly optimized exact kernels. We study BF1, a deterministic block-aligned dyadic sparse-attention route that combines a small exact local neighborhood, a global first block, and logarithmically spaced historical blocks. The route is related to prior log-sparse and dilated attention patterns; our contribution is a correctness-gated pretrained-model retrofit, a matched topology-control study, and a systems characterization that connects per-layer sparsity to whole-model latency. For fixed block width, every converted layer uses O(n log n) selected token interactions and has O(log n) graph communication depth. On an NVIDIA RTX PRO 6000 Blackwell GPU, an optimized BF16 implementation crosses dense attention between 2K and 4K tokens and reaches a 10.91x per-layer prefill speedup at 32K. Retrofitting eight of 28 Qwen3-0.6B attention layers lowers warm whole-model time to first token by 7.7%, 11.3%, and 15.3% at 8K, 16K, and 32K, respectively, while the remaining dense layers keep the complete model asymptotically quadratic. Under a matched 1,000-step, 16.384M-token adaptation protocol, BF1 ranks first across three training seeds: mean report perplexity is 1.68639 versus 1.69154 for a matched static-random nonlocal graph, 1.69258 for dense continued training, and 1.81505 for equal-budget local sliding. At seed 1234, the packed-report paired interval places Dense-CT 0.3169-0.4055% above BF1 and static-random graph 17 0.2441-0.3642% above BF1. These results establish BF1 as a reproducible sparse operator and selective retrofit primitive with real long-context systems value. This paper evaluates numerical correctness, selected-interaction scaling, kernel performance, partial-model inference, and matched next-token language modeling.

---


### 37. [Stored in Optimizer State, Valued by Later Training: A Causal Account of Subliminal Trait Transfer](https://arxiv.org/abs/2608.20442)

**<font color=#1a73e8>作者：</font>** Qinyang Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subliminal trait transfer allows a student model to acquire behavioral dispositions from teacher-generated data in which the trait is not semantically expressed. Recent work explains how such signals enter gradients, but not how they survive source removal or acquire different signs under later training. We treat parameters and optimizer moments as a single trainer state and derive an exact transport-valuation identity separating observer-independent propagation of the source perturbation from the value assigned by a future continuation and behavioral readout. State surgery identifies the first moment as a causal carrier. Transplanting it alone leaves parameters, hidden states, and outputs unchanged at the cut, yet source-free updates generate growing parameter and hidden-state differences; transplanting parameters with the first moment recovers the terminal behavioral response. Sending the same source-induced difference through matched futures produces negative, near-zero, and positive Qwen effects (-0.658, +0.008, and +0.658 seed means). This ordering recurs in all 12 Llama-3.2-1B seeds after eight updates, while state-difference norms remain nearly equal across routes. Both contrasts grow in every paired seed when the continuation extends to sixteen updates. A full-horizon costate predicts all 42 Qwen route-mean signs and all 21 resolved Llama ordinary-route signs. Observer-independent transport also replicates across Qwen, SmolLM2, and Llama, while the complete-state recurrence predicts physical, hidden, and fixed-head responses in non-LoRA MNIST systems, including CNNs trained with AdamW and momentum SGD. Together, these results identify a two-stage mechanism for subliminal trait transfer: optimizer state transports the source perturbation, and later training determines its behavioral value.

---


### 38. [Aggregating Visual Information with Optimal Transport for VideoLM Token Compression](https://arxiv.org/abs/2608.20473)

**<font color=#1a73e8>作者：</font>** Wenti Yin, Xiaotian Han, Junyuan Shang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video language models process videos as dense visual-token sequences with substantial representational redundancy. Compressing these sequences is therefore essential for reducing the visual-token burden on language-model decoding. The central challenge is to preserve visual information dispersed across frames under such compression. To this end, we introduce Aggregating Visual Information with Optimal Transport (AVIOT), which casts video token compression as transporting a dense empirical measure of frame observations onto a compact target measure. The resulting source-to-target coupling induces a distribution over source observations for each target support, directly specifying how the compressed video representation is constructed. We further adapt this construction along task and spatial axes. Question conditioning modulates the transport cost between source frames and target supports, while influencing how many supports are allocated to each temporal segment, thereby directing representation capacity toward question-relevant content. At multiple spatial granularities, AVIOT computes region-specific temporal transport plans and adaptively fuses the representations they yield, allowing different regions within the same compact representation to draw from different moments. Evaluations across varying compression ratios show that AVIOT matches or outperforms the uncompressed baseline on multiple video-understanding benchmarks while retaining strong performance at higher compression ratios.

---


### 39. [AEGIS: Preventing Cross-Domain Resource Abuse in MCP](https://arxiv.org/abs/2608.20481)

**<font color=#1a73e8>作者：</font>** Shriti Priya, Teryl Taylor, Frederico Araujo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) is an open source JSON-RPC protocol that standardizes how large language models (LLMs) interact with external systems through programmatic functions known as tools. Attackers or malicious agents can exploit certain modalities of these MCP tools to degrade the overall quality of service of agent-based applications. For example, an agent may request an excessively large search radius or very long videos, overloading backend systems and potentially causing slowdowns or denial-of-service. Each modality including text, images, video, and location introduces distinct vectors for resource abuse, complicating the development of consistent mitigation strategies. Moreover, multimodal and crossdomain tools expose diverse request schemas and parameters, making it difficult to define policies that are both generalizable and precise enough to enforce meaningful resource constraints. In this paper, we present AEGIS, a policy enforcement component that enables administrators to define fine-grained safeguards against resource abuse across heterogeneous MCP tools and modalities. AEGIS leverages the reasoning capabilities of large language models to analyze, categorize, and normalize diverse tool invocations into a unified, policy-friendly representation accessible to security practitioners. Integrated with the Open Policy Agent and the ContextForge AI Gateway, AEGIS detects and mitigates abusive behaviors while preserving the flexibility of MCP-based agent ecosystems.

---


### 40. [Terminal Agents: A Survey of AI Agents in Command-Line Environments](https://arxiv.org/abs/2608.20485)

**<font color=#1a73e8>作者：</font>** Yi Bin, Xiaoyang Yuan, Haoxi Zeng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly act through terminals, yet existing surveys disperse terminal-mediated behavior across software engineering, tool use, and computer-use research. We regard terminal agents as systems whose dominant progress-bearing action--observation loop is mediated by terminal command execution, textual feedback, and stateful environment interaction. Using terminal-mediated execution as an organizing lens, this survey establishes workload-level boundaries and connects system architecture, competence acquisition, and evaluation through a seven-dimensional terminal competence profile. Our synthesis shows that realized behavior is jointly shaped by the model, interface, harness, runtime, and environment. Executable trajectories ground learning in action consequences, verification, and recovery, whereas prevailing evaluations emphasize final outcomes and expose process quality, recovery, and governance unevenly. Bounded fixed-condition diagnostics illustrate two implications: benchmark families expose different process signals, and matched system comparisons reveal benchmark-dependent performance and limits of component attribution. These findings motivate explicit reporting of system and runtime conditions, supported by replayable traces and process-level evidence. The framework provides a unified basis for studying terminal-mediated agency across software engineering and emerging application domains.

---


### 41. [Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video MLLMs](https://arxiv.org/abs/2608.20492)

**<font color=#1a73e8>作者：</font>** Yunheng Li, Guohong Mu, Hao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have become a prevailing paradigm for unified video perception. However, post-training on large multi-task datasets remains challenging, as existing reinforcement learning methods sample on-policy groups with few high-quality rollouts even with costly chain-of-thought (CoT) generation. In this paper, we study the sample efficiency and scalability of RL post-training for video MLLMs and introduce OraRL. We identify an overlooked role for annotations: Beyond scoring rollouts, each can enter its on-policy group as an oracle rollout, a direct positive optimization target. Direct oracle integration, however, is nontrivial: a high-reward oracle raises the group baseline and inverts otherwise positive policy advantages, a failure we term advantage inversion. At the core of OraRL is a decoupled advantage estimator: policy rollouts determine an oracle-free baseline, while the oracle-policy gap modulates both a directional gain and a separate detached oracle advantage. Sign-balanced pruning improves efficiency: by retaining only the oracle and the strongest rollouts of each sign, OraRL requires just 2.2x the step time of SFT, less than half the 4.9x required by GRPO with CoT. OraRL scales with model size and data, surpassing its backbone from 0.8B to 9B and GRPO up to 100k prompts. Without chain-of-thought, Video-ORA-9B decodes in 130 ms instead of 4,780 ms. Compared with the respective prior best models, it raises temporal mIoU from 62.5 to 66.0, tracking AO from 73.0 to 78.2, segmentation from 64.3 to 70.4, and the three-benchmark spatial-intelligence macro average from 51.0 to 56.1; on VSI-Bench, it scores 73.1 against 55.0 for GPT-5 and 55.1 for Gemini-3-Pro.

---


### 42. [FL-MAESTRO: Multi-Agent LLM Orchestration for Resource-Constrained Federated Learning](https://arxiv.org/abs/2608.20518)

**<font color=#1a73e8>作者：</font>** Jiajun Wu, Zirui Wang, Jiayu Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In Federated Learning (FL), the communication topology is a runtime variable rather than a fixed design choice, since links and edge devices drop in and out during training. Each round, the server must commit three coupled decisions, namely the communication topology, per-client resource allocation, and the aggregation rule for combining local updates. Recent agentic systems have begun bringing large language models (LLM) into FL, but the existing line of work either operates at setup time or handles a single runtime dimension such as client selection. We propose FL-MAESTRO, a multi-agent orchestrator that makes the joint runtime FL decision directly through three specialist LLM agents, one per decision dimension. A coordinator combines their analyses into a single decision, and a non-LLM feasibility check confirms it before the round executes. Because the orchestrator consumes the server's predicted-failure list, it withholds clients whose updates would never be aggregated, which removes the dominant source of wasted round energy in classical FL on volatile edge networks. Because client state is read as natural-text profiles, the same orchestrator extends to heterogeneous device classes without per-class energy models. On a non-IID CIFAR-10 benchmark, FL-MAESTRO matches the accuracy of the strongest energy-aware baseline while cutting wasted round energy from over a third to near zero. Code is available at this https URL.

---


### 43. [LiLiCorr: Lightweight Likelihood Correlation of Parallel Drafts for Speculative Decoding](https://arxiv.org/abs/2608.20530)

**<font color=#1a73e8>作者：</font>** Matan Rusanovsky, Yoav Miron, Roy Uziel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates language-model inference by drafting future tokens that the target model verifies in parallel. A diffusion-style block head such as DFlash is an attractive drafter, predicting an entire block of future tokens in one forward pass. However, it is trained on per-position marginals rather than the joint block distribution, so the tokens it emits are individually plausible yet jointly incoherent. We introduce LiLiCorr, a Lightweight Likelihood-based model that Correlates the per-position marginal distributions a drafter already produces. It keeps the top-k tokens at each position as candidates and processes them jointly, producing for each an in and an out vector. A pair of adjacent candidates matches when the earlier one's out vector has high cosine similarity with the later one's in vector. These matches capture the block's joint structure without ever materializing the full joint distribution. One lightweight network pass produces all the vectors, and the pairwise scores are then computed in parallel as batched matrix operations, leaving only a cheap greedy walk sequential. We further co-train the drafter with LiLiCorr, so it learns to propose candidates that correlate into longer accepted sequences. Over the vanilla DFlash drafter, LiLiCorr raises acceptance length on every benchmark by 9 to 19%, while its scoring head accounts for about 2.8% of the per-block latency. Against DFlash and two concurrent methods that also restore coherence at draft time, LiLiCorr delivers the highest throughput in 70 of 72 settings: nine benchmarks at two target sizes under greedy and temperature-one decoding, and a throughput sweep over six concurrencies, two input lengths and three entropy tiers, with all systems equally optimized on a common serving stack. Extending LiLiCorr to inputs an order of magnitude longer than it was trained on preserves that lead.

---


### 44. [Volumetric Radiology AI in the Era of Multimodal Large Language Models](https://arxiv.org/abs/2608.20549)

**<font color=#1a73e8>作者：</font>** Zanting Ye, Shengyuan Liu, Xin Liu 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in multimodal large language models (MLLMs) are extending radiological artificial intelligence (AI) beyond task-specific image analysis toward multimodal understanding and reasoning. Volumetric radiology, however, presents a fundamental representational mismatch: clinical interpretation often requires full-volume spatial context and acquisition-dependent quantitative information, whereas current MLLMs are commonly conditioned on selected two-dimensional (2D) images, compressed visual representations, or report-derived text. Reliable volumetric radiology AI therefore requires representations that preserve task-relevant three-dimensional (3D) information and systems that can access, verify, and integrate this information across clinical workflows. In this Review, we examine more than 200 publications through July 2026. We organize the literature around volumetric representation and multimodal understanding at the model level, agentic orchestration at the system level, and their links to clinical applications and evaluation. We review volumetric foundation models, language alignment and compression strategies, and agentic systems that extend MLLMs through planning, tools, memory, and workflow interaction. We distinguish settings in which selected 2D views or report-mediated reasoning may suffice from those that warrant native volumetric modeling. We also introduce a Claim-Design-Validation framework to assess whether technical, workflow, and clinical claims are matched by appropriate design and validation. Across the literature, native volumetric modeling and agentic capabilities depend on the spatial, quantitative, contextual, and workflow requirements of the intended task. Clinical credibility requires faithful volumetric representation, traceable system behavior, claim-aligned validation, and clearly defined human oversight in realistic workflows.

---


### 45. [Beyond End-to-End Success: Diagnosing Failures in Long-Horizon Security LLM Agents](https://arxiv.org/abs/2608.20563)

**<font color=#1a73e8>作者：</font>** Wei Shao, Chongzhou Fang, Zuxiong Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Long-horizon security LLM agents must carry information and decisions across many dependent interactions, where later actions often depend on services, state, or access discovered much earlier. This makes final task success difficult to interpret: an agent may fail before it ever reaches the point where the capability of interest can be exercised. We present a diagnostic methodology that instruments security tasks with checkpoints, separates failures before and after capability exposure, and uses controlled interventions to test suspected upstream bottlenecks. We evaluate the methodology across four task families involving delayed reuse of discovered information, reuse of observed state, recovery from failed strategies, and decision making after uncertain outcomes. On observed state reuse, checkpoint analysis shows that many Gemini 2.5 Flash failures occur before the model observes the state it is later expected to reuse. In a pre-specified 92-seed study, targeted protocol-disambiguation guidance increases state observation from 65.5\% under a matched non-guidance control message to 95.4\%. Repeating the same design with Gemini 3.7 Flash produces the opposite effect, while state observation no longer reliably predicts task completion. These results show that the dominant source of failure can shift across model generations, motivating evaluation that diagnoses where and why long-horizon security agents fail rather than relying only on aggregate task success.

---


### 46. [Consilience: Conformally Calibrated Communication Control for Hidden-Profile Multi-Agent Reasoning](https://arxiv.org/abs/2608.20564)

**<font color=#1a73e8>作者：</font>** Abhijith Babu, Ramneet Kaur, Vishal Pramanik 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems can improve reasoning by pooling diverse perspectives, but their effectiveness depends on coordinating communication, particularly in hidden-profile settings where each agent holds only part of the evidence required for a correct decision. Existing protocols, including fixed schedules, round-robin exchange, and unstructured debate, provide no guarantee that a conversational action is appropriate. We propose Consilience, an inference-time orchestration framework that both steers and certifies multi-agent communication under distributed private information. At each turn, Consilience summarizes the discussion using a compact state capturing uncertainty, disagreement, evidence gain, redundancy, and premature consensus, then selects both a communication intervention (challenge, clarify, seek evidence, or route) and an appropriate speaker. Its central contribution is a round-wise conformal calibration procedure that provides a distribution-free, finite-sample guarantee: at each discussion round, conditional on reaching that round, the one-step regret of a controller's proposed action is bounded by a calibrated threshold with marginal probability at least 1 - alpha; an acceptance mechanism enforces the same guarantee for the executed action by replacing inadmissible proposals. On HiddenBench-style hidden-profile tasks spanning 12 open and closed weight language models, Consilience improves decision accuracy and communication efficiency over fixed and unstructured discussion protocols, sometimes surpassing a full-information baseline where every agent observes all evidence. These results demonstrate that certified adaptive communication control can be more valuable than increasing information availability, providing a practical mechanism for reliable multi-agent LLM coordination.

---


### 47. [AgentDecarbonizer: Carbon-Aware Execution for AI Agents](https://arxiv.org/abs/2608.20566)

**<font color=#1a73e8>作者：</font>** Leyi Yan, Shuangning Li, Sihang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI agents extend large language models from single prompt-response interactions to long-running, goaldirected workflows that issue many model calls, invoke tools, and interact with external environments. These workflows enable tasks such as software repair, data analysis, and experiment management, but their repeated model invocations can incur substantial carbon emissions. This paper characterizes the carbon emissions of OpenClaw agent workloads using WildClawBench, and shows that emissions depend on token consumption, context cache reuse, and the carbon intensity of the grid. Our characterization identifies deadline flexibility as an opportunity for carbon-aware execution: agent tasks can wait for lower-carbon-intensity periods or shift to lower-carbon grids. However, doing so requires handling uncertain execution time for temporal shifting and cached context recomputation during spatial shifting. We present AgentDecarbonizer, a carbon optimizer for AI agents that runs alongside OpenClaw. Given a task prompt and user-specified deadline, AgentDecarbonizer conservatively estimates task duration and selects deadline-feasible execution schedules, while accounting for cache recomputation overhead during spatial shifting. Evaluated on WildClawBench workloads with 60 agent tasks across four grids, AgentDecarbonizer reduces carbon emissions by up to 57.9 % compared with a carbon-agnostic baseline and by up to 37.5 % compared with a baseline that selects the carbon-optimal grid at task start time.

---


### 48. [Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation](https://arxiv.org/abs/2608.20569)

**<font color=#1a73e8>作者：</font>** Emilio Ferrara  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Are frontier models able to introspect about their internal states? Recent work suggests that under certain conditions a complex enough model can audit its own internals, call out what changed, and report back confidently about it. We tested that claim on eight open-weight models from seven families and found no such ability: asked whether their own computation had been altered, none answered better than chance. To test it we built Open-Weight Masked Introspection (OWMI), a framework that intervenes on residual-stream sites, attention heads and sparse-autoencoder features, then interrogates the model about the change against the null conditions an answer has to beat: sham runs where nothing was altered, impact-matched random perturbations, and a text-only observer that sees only the visible output.
Over 78,000 measurements, no model's report discriminates a real intervention from a sham beyond chance (AUROC ~0.5007), and an equivalence test bounds the effect below 0.15 percentage points of AUROC. Surprisingly, all the information needed is in the models. A model fine-tuned to report this class of intervention reaches near-perfect recovery on held-out directions, and a linear probe recovers intervention presence from the same activations at 75% to 95.8% accuracy, sharpening to no held-out error at the last layer before the model speaks. In one model the signal surfaces in the confidence rather than the words: its yes-or-no report never varies, while the confidence attached to it separates intervention from sham at AUROC 0.647. The failure sits in the path from internal state to verbal report, so oversight that reads a model's own testimony needs validating against an internal reference.
While our results show the inability of current open-weight models to introspect, the debate is not settled for future models.

---


### 49. [FlavourBench: Ranking Frontier Language Models with Executable Culinary Ground Truth](https://arxiv.org/abs/2608.20574)

**<font color=#1a73e8>作者：</font>** Josef Chen, Erim Hayretci  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-ended language-model benchmarks usually inherit a judge: a human preference panel, another model, or a brittle exact-match key. We introduce FlavourBench, an automated benchmark in which a versioned culinary system supplies dense, executable ground truth. Each task presents eight ingredients and asks for a three-ingredient portfolio; before model execution, Epicure scores all 56 possible portfolios. We evaluate 27 frontier endpoints on an identical 534-task core spanning substitution, pairing, and constrained composition. Every ranked model has exactly 89 valid responses per panel and family (14,418 model-task cells total), eliminating differential missingness from the leaderboard. The FlavourBench Score is the equal-family mean of the frozen task scores. We use 50,000 anchor-cluster bootstrap replicates for simultaneous 95% score bands and 100,000 sign-flip draws for all 351 paired model contrasts, with Holm control. The two independently compiled panels correlate at r = 0.89 (rank rho = 0.80). Grok 4.6 has the largest point estimate at 65.1 (simultaneous 95% CI 61.0-69.2); 101 of 351 model pairs are resolved. The release includes the prompts, all portfolio score maps, raw responses, exact routes, content hashes, and an offline verifier that reconstructs every result.

---


### 50. [More Granular, Less Trust: Enforcing Intra-Process Isolation with Arm CCA in an Untrusted Management Environment](https://arxiv.org/abs/2608.20584)

**<font color=#1a73e8>作者：</font>** Shiqi Liu, Zhouqi Jiang, Jie Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the increasing adoption of confidential computing, security-sensitive applications are often deployed in confidential virtual machines (CVMs), which reduce reliance on third-party cloud providers. However, privilege attacks originating from the OS remain a significant threat in these environments. Existing finer-grained isolation schemes, such as SHELTER, provide process-level protection but are still vulnerable to intraprocess attacks and potential collusion between the OS and intra-process adversaries. Many current intra-process isolation techniques continue to depend on the OS to manage and enforce isolation domains, leading to a large Trusted Computing Base (TCB). This gap highlights the need for more granular, less trust-dependent confidential computing solutions. In this paper, we present CCAegis, a system that extends the Arm Confidential Compute Architecture (CCA) to enforce intra-process isolation of sensitive data and operations, safeguarding them from both intraprocess adversaries and the OS. We employ static analysis to track the flow of sensitive data and identify functions that handle such data. Permission-switching instructions are inserted at the function call and return points, adjusting permissions via the Granule Protection Table (GPT) to ensure that only designated functions can access the isolated data. Notably, CCAegis places trust solely in the Secure Monitor, which configures the GPTs and manages domain switching, thereby minimizing the TCB. We implemented CCAegis on both an official emulator and a real development board to assess its performance. Our experimental results show that CCAegis effectively isolates sensitive data and operations, with performance overheads ranging from 1.01x to 1.43x compared to the original version across real-world cryptographic workloads.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-170](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
