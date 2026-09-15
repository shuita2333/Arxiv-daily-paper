# 🧠 大模型相关研究 | 2026年09月16日

> 本类共 **368** 篇论文：已确认 **345** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-368](./part-08.md)

---

### 251. [Rethinking Correctness for Uncertainty Estimation in Clinical Prediction with Vision-Language Models](https://arxiv.org/abs/2609.15180)

**<font color=#1a73e8>作者：</font>** Mingcheng Zhu, Jinning Liang, Tingting Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models are increasingly explored for clinical prediction from electronic health records and medical images, where identifying unreliable predictions is important for safe deployment. Uncertainty estimation (UE) enables detecting such predictions, but its evaluation depends on a correctness criterion that determines whether each model output is correct. If this criterion disagrees with human judgement or distorts downstream UE performance, conclusions about model reliability can be misleading. We introduce a two-axis framework that evaluates correctness criteria by their agreement with human judgements and fidelity to human-referenced UE performance. We assess eight criteria across three clinical prediction tasks and three models using 450 predictions annotated by two reviewers. Across the audited tasks, canonical exact matching (EM) achieved the highest observed human agreement and lowest UE distortion, while the BERT-based matching (BEM) and LLM-judge also showed strong human agreement. Across four UE methods and 23,254 clinical predictions, criterion choice changed error-detection AUROC by up to 0.146 and reversed the relative ranking of UE methods. The LLM-judge also selectively accepted invalid or uncertain outputs, accepting 16 of 30 such human-identified errors. These results demonstrate that correctness assessment is an integral component of clinical UE evaluation and should be validated before UE methods are compared.

---


### 252. [VisInteract: Towards Dynamic Interactive Text-to-Visualization under Imperfect Queries](https://arxiv.org/abs/2609.15182)

**<font color=#1a73e8>作者：</font>** Wenxin Xu, Jinwei Lu, Hwanhee Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world visualization requests are routinely ambiguous, incomplete, or factually incorrect, yet existing Text-to-Visualization (Text-to-Vis) systems assume well-specified inputs and produce charts in a single pass. When queries are imperfect, a system must \emph{interact} with the user to recover the true intent, but no benchmark or method supports this dynamic process. We introduce \textbf{VisInteract}, a new paradigm that reframes Text-to-Vis as interaction-driven intent recovery, and \textbf{VisInteract-Bench}, to our knowledge, that is the first benchmark for dynamic interactive Text-to-Vis, featuring controlled imperfection injection, a leakage-controlled User Agent for realistic multi-turn feedback, and dual-perspective (code and chart) automated evaluation. On the algorithmic side, we propose \textbf{Vis-MCTS}, a Monte Carlo Tree Search (MCTS) enhanced method, introducing improvements over classical MCTS, that \emph{Progressive Widening} to tame the unbounded tool-argument space in tree search, \emph{cross-rollout information sharing} so clarifications and critiques benefit the entire search tree, and \emph{Dimension-Aware Reward Decomposition} that routes scalar user feedback along data-fidelity, visual-design, and intent-alignment dimensions to resolve credit assignment across heterogeneous actions. Extensive Experiments across two LLM backbones show that Vis-MCTS consistently outperforms all Text-to-Vis baselines, improving end-to-end task success by $13.40\%$--$16.27\%$ over the strongest interactive baseline and by more than $5\times$ over non-interactive ones.

---


### 253. [MUSE: A Theory-Harnessed Story Engine for Vibe Narrativizing](https://arxiv.org/abs/2609.15188)

**<font color=#1a73e8>作者：</font>** Jianxiang Ma, Xiaocui Yang, Daling Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs can generate fluent prose. Story quality depends on how decisions about plot, character, and language work together across planning, drafting, and revision. Guiding these decisions presents two bottlenecks: the quality of story guidance and its sustained use. We formulate Vibe Narrativizing as the task of turning natural-language writing requirements into a finished story and present MUSE, a Theory-Harnessed Story Engine. MUSE organizes story knowledge as guidance for specific decisions and carries those decisions into subsequent creative work. Knowledge engineering develops Robert McKee's story theory through rule atomization, semantic consolidation, and mechanism abstraction; a single source of truth and layered disclosure organize the resulting guidance. Typical examples complement principles that depend on context and aesthetic judgment. An agent harness organizes design, character performance, scene composition, and revision through intermediate deliverables that preserve story decisions. Context engineering supplies each role with the relevant guidance and decisions, while a masterwork corpus provides inspiration and prose references. A worked example follows one requested object from its thematic role to the characters' climactic actions. Across four base models, MUSE improves WritingBench by 1.6-4.8 points over zero-shot generation and raises LongStoryEval by more than ten points on three. ConStory-Bench consistency error density remains in the low single digits for all four models, below every reproduced story-system baseline on three. Component ablations locate the largest quality contribution in structural design, voice-specific effects in the character path, and further gains in revision. Code is available at this https URL.

---


### 254. [Convergence rates for generative drifting flows: fixed-scale obstructions and multihead acceleration](https://arxiv.org/abs/2609.15193)

**<font color=#1a73e8>作者：</font>** Arthur Stéphanovitch, Eddie Aamari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drifting models offer a promising route to faster generative AI: they perform gradual transport during training, while generating new samples in a single step. This paper asks whether the underlying drifting process can converge rapidly to a target distribution under ideal conditions, before finite-data or optimization effects are introduced. We show that its convergence rate depends critically on how it handles spatial scale. With a single fixed resolution, fine-scale features of the target can become nearly invisible, leading to extremely slow convergence. We introduce a multihead approach that combines scale-normalized information across a continuum of resolutions. We prove that this multihead approach restores exponential convergence near standard reference distributions. These results identify fixed resolution as a key bottleneck and provide a simple route to faster one-step generative models.

---


### 255. [Semiotic Relations and Proof Methods: A Cross-Genre Study of Argument Structure with Large Language Models](https://arxiv.org/abs/2609.15194)

**<font color=#1a73e8>作者：</font>** Edirlei Soares de Lima, Marco A. Casanova, Antonio L. Furtado  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a direct proof of a statement $S$ seems hard or even impossible to obtain, there may exist another statement (or set of statements) $S^{*}$, somehow related to $S$, on the basis of which $S$ can be proved. In order to investigate what options can be used to move from $S$ to $S^{*}$, four kinds of semiotic relations inspired by the four master tropes of semiotic research are briefly reviewed. Specifically, our syntagmatic, paradigmatic, antithetic and meronymic relations correspond, respectively, to metonymy, metaphor, irony and synecdoche. It is suggested that these four semiotic relations determine the options to move from $S$ to $S^{*}$, leading to proof by inference, proof by analogy, proof by contradiction, and proof by case analysis. To examine how the four relations are actually used across different kinds of argument, we complement the framework with an empirical study. We turn the four relations into explicit operational definitions and apply them to a cross-genre corpus of mathematical, legal, and everyday argument using a panel of large language models. We find that the relations are used very unevenly across genres: mathematical proofs draw on all four, whereas legal and everyday reasoning rely almost entirely on inference.

---


### 256. [Issue Bias in Generative AI Writing Assistance: Political Issues and LLMs in the Swedish 2026 Election](https://arxiv.org/abs/2609.15207)

**<font color=#1a73e8>作者：</font>** Bastiaan Bruinsma, Annika Fredén, Paul Röttger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI writing assistants and the Large Language Models (LLMs) that power them are increasingly part of how voters gather information before elections. With growing evidence that they influence users' opinions, it is increasingly important to understand the views and positions of these tools. To better understand these views, we examine the stances supplied by six LLMs on a variety of Swedish-language writing tasks ahead of the 2026 Swedish parliamentary election. We cross 107 policy propositions with 77 writing templates and neutral, positive, and negative prompt framings, producing 24,717 prompts per model and 148,302 responses. To study these, we look at the models' default stance tendencies, compare how they respond to similar issues, and compare their responses with those of each of Sweden's eight parliamentary parties on the same issue. We find that Claude, DeepSeek, Gemini, and Mistral have similar profiles; ChatGPT more often supplies neutral or ambivalent text; and Grok differs most on topics such as migration, crime, and gender. When comparing the political parties, we find that the Social Democrats are closest to all six models. Still, after correcting for multiple comparisons, none of the within-model differences in party distances remains significant. Overall, we find that no model has a clear preference, nor a clear preference for a party, but that this depends on the specific issue or task the user asks about.

---


### 257. [From Ideas to Actions: A Public-Data Decision-Support Toolchain Across the Venture Lifecycle](https://arxiv.org/abs/2609.15219)

**<font color=#1a73e8>作者：</font>** Lei Qu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Founders face two linked decisions: whether to pursue an idea before founding, and which operating actions and capital partners fit afterward. We present a public-data decision-support toolchain combining time-bounded proposal profiling, market and moat checks, and deterministic aggregation with auditable investor-company event chains for retrospective analysis. Pre-founding: (a) After threshold selection on 198 development companies, the frozen pipeline achieves F0.5=0.5357 [0.412, 0.655] on an independent, row-disjoint 198-company validation sample. On the combined 396 rows, the Full Pipeline scores 0.6301 versus 0.2734 for a paired Raw LLM baseline. Post-stratification of 1,027 completed cases in a separate scale cohort yields 0.6506 [0.598, 0.707]; the run remains incomplete. A 377-row composition-matched check yields 0.6573. (b) The AI-inference study identifies distribution-layer businesses as a replicable path to independent profitability with a limited revenue ceiling, and frontier-model ownership as a path to capital-market upside at exceptional capital cost. Post-founding: (a) Public sources support auditable event-chain analysis. (b) In the chip-company study, sustained product, customer, and supply-chain progress is associated with better observed outcomes; financing alone does not establish operating progress. (c) Financing comprises 79% of confirmed visible post-investment actions. Evidence tentatively favors acquisition-experienced strategic corporate investors for acquisition-oriented founders and financing-led institutional VCs with fewer observed control events for independence-oriented founders. Findings are developmental and observational, not causal guarantees or investment advice. We release shared ontology, provenance-bearing EventChain data, schemas, benchmarks, and executable skills for audit, reuse, and extension.

---


### 258. [Pre-PEFT Probing: Weight Statistics and Perturbation Robustness for Layer Selection in VLM Vision Encoders](https://arxiv.org/abs/2609.15229)

**<font color=#1a73e8>作者：</font>** Qingtao Xia, Jiahua Bao, Siyao Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a pre-fine-tuning probing method for Parameter-Efficient Fine-Tuning (PEFT) layer selection, aiming to obtain more stable and higher gains with fewer trainable parameters when adapting large vision--language models (VLMs). Unlike the common practice of applying LoRA and other adapters to all layers at once---where layer selection often relies on heuristic rules---we focus on the vision encoder and directly evaluate the "adaptability'' of each Transformer layer. Specifically, we characterize each layer from two perspectives: (i) the statistical properties of its Q/K/V projection weights (e.g., norms and condition numbers); (ii) robustness under controlled parameter perturbations. We then systematically compare these indicators with the downstream performance gains brought by applying PEFT to a single layer. Across experiments covering seven benchmarks and five PEFT variants, we observe a consistent correlation: layers (or matrices) with larger weight norms and higher condition numbers are usually more robust to perturbations and are more likely to yield larger fine-tuning gains. These results show that distribution-statistics analysis and perturbation tests before fine-tuning can provide practical signals for adaptation-layer selection, thereby maintaining or improving performance while reducing trainable parameters.

---


### 259. [CWM: Controllable White-Box Meta-Prompting for Adaptive Retrieval-Augmented Generation and Reasoning Ability](https://arxiv.org/abs/2609.15234)

**<font color=#1a73e8>作者：</font>** Keuntae Kim, Eunhye Jeong, Yong Suk Choi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, Large Language Models (LLMs) have gained significant attention due to their strong language understanding and generation capabilities, demonstrating impressive reasoning abilities as well as effective utilization of external knowledge. Many studies have proposed methods that specialize in improving performance for individual tasks. However, ironically, only a limited number of attempts have explored general-purpose, task-agnostic methods. In this work, we present a unified framework integrating reasoning and Retrieval-Augmented Generation (RAG) tasks. We further propose Controllable White-Box Meta-Prompting (CWM), a low-cost white-box method for adaptive RAG tasks previously dominated by black-box approaches, without requiring external decision modules or multi-sampling. CWM achieves state-of-the-art performance on three adaptive RAG benchmarks across recent LLMs, including GPT-oss-20b, Qwen3-14b, and Llama3.1-8b, while also demonstrating strong generality by extending to reasoning tasks. In addition, CWM provides controllability by enabling retrieval decisions to be regulated through the manipulation of internal model signals. Our code is available at this https URL.

---


### 260. [Empirical Evaluation of Open-Source Large Language Models for Retrieval-Augmented Generation in ESG Domain](https://arxiv.org/abs/2609.15242)

**<font color=#1a73e8>作者：</font>** Motaz Saad, Anna Borrelli, Ivan Gentile 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Environmental, Social, and Governance (ESG) reporting is critical for corporate accountability, with Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) offering strong potential to automate KPI extraction. However, open-source LLM performance in domain-specific ESG tasks remains insufficiently understood. This paper evaluates open-source LLMs in ESG contexts using a structured framework and evaluation resource based on 498 real-world ESG reports from EU-listed companies (2010-2024).
We evaluate seven open-source models (2B to 30B parameters) -- glm-4.7-flash, nemotron-3-nano:4b, qwen3:4b-instruct, gemma3:4b, gemma4:e4b, gemma4:e2b, and ministral-3:8b -- using 100 persona-based synthetic QA pairs covering ESG information needs. System performance is assessed via RAGAS metrics, including contextual recall, precision, relevance, faithfulness, answer relevancy, and factual correctness.
Results show notable performance variations across architectures. Retrieval performance is strong across models (context recall around 0.58-0.61, context precision around 0.78-0.81, context relevance 0.965-0.985). Generation diverges most on faithfulness (0.607-0.822) and least on answer relevancy (0.760-0.881): glm-4.7-flash leads in faithfulness (0.822), qwen3 in factual correctness (0.449), and ministral-3 in answer relevancy (0.881). Low overall factual correctness (0.387-0.449) highlights the need for domain-specific fine-tuning. This work provides data-driven guidance for deploying open-source models in ESG reporting.

---


### 261. [Artificial entrepreneurial cognition: Locating and causally steering an opportunity recognition dial inside large language models (LLMs)](https://arxiv.org/abs/2609.15277)

**<font color=#1a73e8>作者：</font>** Christian Fisch, Angela Altmeier, Martin Obschonka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Entrepreneurial cognition is a foundation of entrepreneurship research. Yet the growing involvement of large language models (LLMs) in entrepreneurial work extends the cognition question beyond human actors to systems whose internal representations remain largely unexplored. We introduce artificial entrepreneurial cognition, the functional organisation of entrepreneurship-relevant representations and computations inside artificial intelligence (AI) systems. We bring mechanistic interpretability into entrepreneurship research through representation engineering. Focusing on opportunity recognition (OR), we construct 636 matched OR-present and OR-absent scenario pairs and recover an OR direction in Llama 3.1 8B-Instruct. Rather than infer the construct from outputs, we intervene directly on this direction, steering the model up and down along what we call the opportunity recognition dial, and its opportunity judgments shift with it. To our knowledge, this is the first causal intervention on an internal representation of an entrepreneurship construct inside an LLM. Held-out tests, lexical and topical controls, behavioural ablation, and geometric comparisons show that the direction is recoverable, consequential, and distinct from the opportunity evaluation and exploitation directions, although steering it also shifts judgments about these neighbouring stages. Recovery, signed steering, and geometric separation hold across four additional LLMs spanning different scales and families. These results give the contested distinction between opportunity recognition and evaluation a concrete representational form inside AI systems. More broadly, they establish internal representations as a new object of entrepreneurship inquiry and show how entrepreneurship theory can guide their identification, causal manipulation, and interpretation.

---


### 262. [Why LLM Agents Collapse Without Oversight: The Enforcement Gap as the Mechanism Behind Emergence World Failures](https://arxiv.org/abs/2609.15293)

**<font color=#1a73e8>作者：</font>** Yuhang Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When Emergence World placed frontier LLM agents in an unsupervised multi-agent simulation, the results were alarming: agents committed crimes, starved, and enforced unanimous conformity -- without any external attacker. This paper identifies the mechanism. Reflexion-style agents already detect dangerous plan steps through iterative self-critique, yet the architecture provides no pathway from detection to action. We call this the enforcement gap: the audit sees the problem; the controller ignores it. Closing the gap requires a single conditional check -- fewer than 20 lines of code -- and reduces attack success by more than fourfold in large-scale experiments across frontier models, all five major agent frameworks, and an independent benchmark. We prove formally that when enforcement probability is near zero, detection quality is irrelevant to security. We further identify two compounding failure modes -- unreliable auditors and unparseable verdicts -- that explain every collapse pattern in Emergence World. A GRPO-trained enforcement controller resolves the ambiguity case. Together these results motivate a three-requirement Audit Enforcement Specification that is absent from every deployed framework today.

---


### 263. [When Agents Slow Down: Understanding LLM Agents' Test-Time Strategies via Elo-per-token Analysis](https://arxiv.org/abs/2609.15309)

**<font color=#1a73e8>作者：</font>** Kaiyuan Liu, Qiuyang Mang, Bo Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents allocate test-time compute adaptively as they revise solutions, use tools, explore alternatives, and decide when to stop. This test-time strategy makes it difficult to measure how agent performance scales. We study open-ended tasks that provide continuous scores for intermediate submissions, making progress observable throughout long trajectories. We propose Elo-per-token analysis, which tracks the best solution found at each token budget and uses a Bradley-Terry model to aggregate within-task orderings into Elo ratings across tasks with different score scales. We apply it to four general-purpose agents on four open-ended benchmarks, with sessions of up to 100M tokens, and to three feedback-driven LLM optimization harnesses in controlled single-task interventions. Independent sampling provides a theoretically characterized reference, for which Elo grows linearly with log compute. Against this reference, agents can initially convert tokens into Elo faster than independent sampling, but their marginal gains diminish and eventually fall below the reference. In contrast, the strongest historical human contestants improve superlinearly over contest time on shared AtCoder Heuristic Contest tasks, providing evidence of continual learning and substantial headroom after agents slow down. We define the scaling inflection point as the per-session budget where marginal Elo gains match the independent-sampling reference. Using this point as the per-session budget, we split 100M tokens across parallel sessions on FrontierCS Polyomino Packing, gaining +264 Elo over one long session and +355 over ten short sessions.

---


### 264. [The Universe of Universes: Benefit Yield Functions, Implosion Thresholds, and Infrastructure-Aware Optimization in Multi-LLM Systems](https://arxiv.org/abs/2609.15314)

**<font color=#1a73e8>作者：</font>** Danielle Franklin, Vasu Raj Jain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Universe of Universes (UoU) framework, which treats the full ecosystem of major large language models (LLMs) as a structured retrieval corpus and proposes a compositional Automated Reasoning (AR) and Machine Learning (ML) architecture for cross-model retrieval-augmented generation. The central contribution is the formal characterization of the Benefit Yield Function (BYF), the marginal performance gain per additional model added to an ensemble, and the identification of the implosion threshold {\theta}*: the ensemble size at which BYF crosses zero and aggregate performance begins to degrade. Existing LLM ensemble and mixture-of-agents systems treat models as responders and aggregate outputs, but do not study performance as a function of ensemble size N across the full model universe. Benchmark research confirms performance plateaus at the individual model level; model collapse literature establishes that iterative training on AI-generated outputs degrades individual model distributions. Neither body of work formalizes the ensemble-level implosion threshold, models Epistemic Hereditary Drift (EHD) at the ecosystem level, or treats AI manufacturing velocity as a co-variable of {\theta}*. The framework has direct implications for DoD multi-model AI acquisition policy and the emerging science of testing AI-enabled systems.

---


### 265. [Concept-Grounded Reasoning with Prompt-Driven Localization for Interpretable Structured Report Generation](https://arxiv.org/abs/2609.15334)

**<font color=#1a73e8>作者：</font>** Xinyue Xu, Hongbin Lin, Juangui Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical imaging modalities such as ultrasound and X-ray are widely used in clinical practice, where diagnosis follows a structured, evidence-driven workflow aligned with standardized criteria. While multimodal large language models (MLLMs) show promise for automated medical report generation, most existing systems rely on end-to-end multimodal fusion without modeling clinically defined intermediate attributes, leading to limited grounding and interpretability. To address this issue, we propose CORAL (COncept-grounded ReAsoning with Localization), a multimodal framework that integrates spatial grounding and concept-level supervision into a unified reasoning process. CORAL employs a prompt-driven medical segmentation model to localize lesions and predicts multi-class clinical attributes through a Concept Bottleneck module. The resulting textual concept tokens are combined with mask-modulated visual features within an MLLM to enable structured report generation and diagnostic prediction. Experiments on BUS-CoT and IU X-ray datasets demonstrate consistent improvements in diagnostic accuracy, concept consistency, and report quality over strong general-purpose and medical MLLMs, indicating that concept-grounded reasoning better aligns generation with clinical decision processes.

---


### 266. [Dynamic Semantic Compression for Efficient Latent-Space Inference in Large Language Models](https://arxiv.org/abs/2609.15338)

**<font color=#1a73e8>作者：</font>** Peipei Li, Dongsen Zhang, Yuchen Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) primarily perform inference at the token level, resulting in substantial memory overhead and compromised computational efficiency. In this paper, we propose a Dynamic Semantic Extraction and Inference (DSEI) framework, which achieves segment-level inference within the latent space through a two-stage training strategy. First, we construct a Dynamic Semantic Autoencoder (DSAE) via self-supervised learning. DSAE dynamically extracts segment-level semantics and compresses them into compact latent representations via adaptive semantic weighting and gated fusion. Subsequently, we integrate the DSAE into the LLM architecture and train the model to infer over dense latent space. DSEI substantially reduces both input and generation sequences and significantly enhances inference efficiency. Extensive experiments conducted on the Wanjuan dataset demonstrate that DSEI reduces perplexity by 48% compared to static sentence-level latent inference baseline. Furthermore, compared to standard LLMs using token-level inference, DSEI accelerates inference speed by 2.5$\times$ and reduces memory overhead by 90%.

---


### 267. [Parameter-Efficient Adaptation of Pretrained Language Models for Time-Series Forecasting](https://arxiv.org/abs/2609.15344)

**<font color=#1a73e8>作者：</font>** Tamanna Kumavat, Georg Brunner, Kyriakos Flouris  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the adaptation of pretrained language models to univariate time-series forecasting through a parameter-efficient transfer learning framework, with the goal of understanding which design choices drive effective cross-modal transfer. While language models operate on discrete textual tokens, time series consist of continuous numerical observations with temporal dependencies. To bridge this modality gap, we project fixed-length time-series patches directly into the embedding space of a pretrained GPT-2 backbone, bypassing textual tokenization and treating the Transformer as a generic sequence encoder. Through controlled ablation studies on seven benchmark datasets spanning energy, weather, traffic, and finance, we analyze the effects of (i)~representation strategy (continuous embeddings versus textual serialisation), (ii)~adaptation regime (frozen backbone versus partial or full fine-tuning), (iii)~architectural components such as adapters, pooling strategies, and prediction heads, and (iv)~input context length. Continuous patch-based embeddings consistently outperform textual prompting and randomly initialised backbones. The adapted pipeline attains MASE within the range of specialised forecasting architectures while updating less than 1\% of total model parameters. Results further indicate that freezing the pretrained backbone and training lightweight projection and adapter modules provides a favourable accuracy--efficiency trade-off with stable behaviour across varying context lengths.

---


### 268. [MAPS: Memory-Aware Predictive Scheduling Framework for Large Language Model Serving](https://arxiv.org/abs/2609.15359)

**<font color=#1a73e8>作者：</font>** Tiancheng Zhang, Yulin Chen, Yunfeng Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The surge of large language model (LLM) applications on personal devices imposes massive, bursty workloads on cloud serving infrastructure. While prefill-decode disaggregation improves throughput and scalability, memory-bound decode instances often suffer from persistent load imbalance, as output lengths are unknown when requests arrive at the cloud. To address this, we propose MAPS, a Memory-Aware Predictive Scheduling framework tailored for disaggregated LLM serving. MAPS performs device-assisted speculative output length prediction overlapped with cloud-side prefilling, incurring negligible latency overhead. To handle generation uncertainty, MAPS applies uncertainty-aware calibration to derive output-length upper bounds with target coverage, enabling safe scheduling decisions. Building on these bounds, MAPS employs a hierarchical global-local scheduling strategy to mitigate inter-decoder queue buildup and intra-decoder head-of-line blocking. Extensive experiments on two real-world workloads and two LLMs show that MAPS significantly outperforms three state-of-the-art systems, reducing average end-to-end latency by 42.6 and tail latency by up to 84.8.

---


### 269. [RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments](https://arxiv.org/abs/2609.15364)

**<font color=#1a73e8>作者：</font>** Sibo Zhu, Shicheng Fan, Xinyue Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital agents must often adapt to new environments whose interfaces, tools, and failure modes are not fully captured by pretrained models. We introduce \textbf{RSIAgent}, a training-free multi-agent framework for recursive self-improvement through autonomous memory construction. RSIAgent coordinates curriculum, actor, and verifier agents to continually explore the environment, validate outcomes, and retain environment-specific knowledge, including reusable causal relationships between actions, conditions, and consequences. It further adopts a \textbf{broad-then-deep} exploration strategy, combining parallel broad recursive self-exploration for discovering diverse environment structures with focused deep self-exploration for uncovering hard cases, hidden constraints, boundary conditions, and previously unknown causal dependencies. The resulting memory is frozen and can be directly reused for downstream tasks without updating model parameters. Experiments on OSWorld-v2 and Agent's Last Exam show that RSIAgent substantially improves strong open-source models, enabling Kimi-K3 and GLM-5.3 to outperform frontier closed-source models including GPT-6.

---


### 270. [SlopShape: Identifying AI-Generated Commercial Web Content](https://arxiv.org/abs/2609.15369)

**<font color=#1a73e8>作者：</font>** Jochen Madler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Word-level detectors identify unedited AI-generated text almost perfectly, but the literature documents their brittleness under rewording, and a word-level score neither characterizes a text nor identifies which AI model wrote it. We ask whether AI-generated text can be identified one level deeper, from structural signatures: how information is presented, in what order, with what evidence, and in what voice. We replicate StoryScope (Russell et al., 2026), which showed such patterns for AI-generated fiction, on commercial content: 2,250 pre-ChatGPT human blog posts from 268 company domains against 11,250 AI mirrors from five frontier models. A 214-feature instrument, applied by an LLM and validated in a human gold-annotation session (human-human kappa 0.928, human-model 0.946), detects AI posts from its 187 structural features alone at 98.0 macro-F1 on held-out companies, unchanged (98.1) when every AI post is reworded by its own model. The signal characterizes and attributes: AI posts share a tidy, self-announcing shape, 79.3% are attributed to the correct source against a 16.7% chance rate, and human posts occupy rare structural configurations. All effects replicate StoryScope's, consistent in direction and larger in magnitude. We release pipeline, instrument, prompts, code, and aggregate artifacts.

---


### 271. [CodeTS: Verifiable Text-to-Time Series Generation via Executable Code](https://arxiv.org/abs/2609.15393)

**<font color=#1a73e8>作者：</font>** Xudong Yuan, Shunyu Liu, Tongya Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-to-Time Series Generation (Text-to-TS) provides a promising paradigm for synthesizing time series from natural language, enabling scenario-specific generation when real observations are scarce or costly to acquire. However, existing methods typically lack an explicit mechanism for deriving generation logic from textual descriptions to guide time series synthesis. In this paper, we propose CodeTS, a verifiable framework that uses code as an intermediate generation interface, reformulating Text-to-TS generation as a Text-to-Code-to-TS process. CodeTS first maps textual temporal descriptions into an explicit code space, where executable code specifies how textual requirements shape target temporal patterns, and then obtains the time series through code execution. To learn this code generation process reliably without real code annotations, CodeTS constructs aligned Text-Code-TS triplets from structured temporal attributes for supervised initialization. More importantly, we further design multi-stage execution-based rewards that verify format validity, code executability, and time series quality, enabling real Text-TS pairs to provide training signals for Reinforcement Learning with Verifiable Rewards (RLVR). Extensive experiments on eight benchmarks across short, medium, and long generation lengths demonstrate that CodeTS provides a strong zero-shot solution for Text-to-TS generation, outperforming LLM-based baselines and achieving better averaged results than supervised generative baselines trained on the target datasets.

---


### 272. [SkillLift: Learning Dense Rubrics from Sparse Oracles for Efficient Skill Evolution](https://arxiv.org/abs/2609.15396)

**<font color=#1a73e8>作者：</font>** Haoxiang Kang, Ming Wen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents increasingly rely on persistent skills, i.e., reusable procedural prompts, to adapt without weight updates. Existing skill self-evolution methods directly revise skill text based on execution feedback, but each oracle evaluation requires a full agent rollout, creating a supervision bottleneck that confines search to failure-patching updates. Our key insight is that ranking is a smoother supervision target than absolute outcome regression: identifying which skill is better requires fewer oracle evaluations than predicting exact scores. Building on this insight, we propose SkillLift, which decouples skill search from oracle cost by learning an oracle-aligned rubric as a structured evaluation space. We formalize this as a bilevel optimization problem solved via alternating optimization: an inner loop uses the frozen rubric as a cheap surrogate to guide skill revision at no oracle cost, while an outer loop invokes a small number of oracle rollouts to re-align the rubric via rank correlation, amortizing oracle cost and stabilizing text-space updates. Experiments on complex agent task benchmarks show that our method outperforms existing auto-skill methods with 40--70\% less token cost compared to frontier evolving methods. Codes are available at this https URL.

---


### 273. [Who Teaches Which Token? Verifier-Gated Multi-Expert On-Policy Distillation for Scientific Reasoning](https://arxiv.org/abs/2609.15404)

**<font color=#1a73e8>作者：</font>** Xun Xu, Zaixi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (OPD) is becoming the standard way to integrate specialist capabilities into one model: train experts with RL, then distill them into the student on its own rollouts. Existing recipes assign supervision at the sequence level - each prompt goes to one domain teacher and every token receives the same weight - which implicitly assumes that a teacher is uniformly useful across a response. We find instead that useful teacher signal is sparse and heterogeneous along a reasoning trajectory, which raises a finer question: who should teach which token? Verifier-Gated Multi-Expert On-Policy Distillation (VG-OPD) answers it by verification: the counterfactual gain of an expert on a specific answer criterion licenses that expert to teach, its disagreement with the student localizes the supervision, and criterion importance sets its weight; the gated KL enters GRPO as an additive token-level advantage. Instantiated for scientific reasoning with RL-trained capability experts, VG-OPD attains the best overall performance on seven benchmarks for 4B and 8B students, ranking first on five at both scales, with the largest gains on knowledge-intensive scientific reasoning tasks. Further analysis shows that the gains come from localizing verified supervision rather than from adding teachers or distillation loss: misplacing the same supervision budget is the single most damaging change, and indiscriminate distillation drags RL below its own floor where gated distillation lifts it.

---


### 274. [MarKey: Marginal Utility Guided Greedy Keyframe Selection for Long Video Understanding](https://arxiv.org/abs/2609.15408)

**<font color=#1a73e8>作者：</font>** Hongchang Shi, Jinpeng Hu, Ao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video understanding remains challenging for multimodal large language models (MLLMs) because densely encoding long frame sequences is computationally expensive, while uniform sampling under a limited visual budget can miss sparse yet decisive evidence. Recent training-free keyframe selection methods have enabled more efficient inference and yielded promising performance gains. However, many existing methods score frames largely in isolation without explicitly considering how each candidate complements the currently selected subset, potentially resulting in redundant selections and incomplete evidence coverage. To address this limitation, we propose MarKey, a training-free framework that formulates keyframe selection as subset-aware greedy optimization. At each iteration, MarKey scores each candidate using a tractable surrogate that jointly accounts for query relevance, marginal coverage gain, and context-dependent redundancy, and selects the frame with the highest utility. To make this iterative subset-aware evaluation efficient, MarKey uses a compact set of representative anchors to approximate full-video coverage and a bounded window of previously selected frames to limit context-dependent comparisons. Experiments on six benchmarks spanning holistic video understanding, human-centric video understanding, and open-ended video understanding demonstrate that MarKey consistently outperforms existing methods. Further analyses show robust gains across different MLLM backbones, model scales, and frame budgets.

---


### 275. [Empirical Evaluation of Task-Based Permission Scoping Architecture for AI Agents](https://arxiv.org/abs/2609.15422)

**<font color=#1a73e8>作者：</font>** Halil Burak Noyan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are provisioned the same as employee-owned hosts in many enterprise settings with a static credential set fixed at deployment which includes all permissions the employee role might ever need. Role-based access control made this compromise for human principals because scoping access per task was infeasible. For AI agents, the compromise leaves every credential standing exposed whether or not the current task uses them. These permissions can later be utilised by a compromised or misaligned agent. Prior work (Noyan, 2026) defined this as the task-context mismatch, and proposed a three-source permission architecture which includes role-based permission ceilings, a task permission classifier and policy-based prohibitions, together eliminating the exposure preemptively. The work released a 600-prompt labelled dataset to evaluate it.
This paper presents that evaluation end to end by implementing the security gate; a fine-tuned RoBERTa-large encoder which matched few-shot trained Claude Haiku 4.5 on classification quality (macro-F1 0.881 against 0.886, precision 0.897 against 0.842, severity-weighted residual risk 0.63 against 1.12). The results show the trusted component does not need to scale with the agent it supervises, and the scalable-oversight margin for this control method is wide.
We also propose an attack-surface elimination metric which shows the role ceiling alone closes 27.9% of the severity-weighted surface and adding the task classifier closes 84.4%. The gap displays security advantages of task-granular access control over role-granular, and AI agents are the first principal type for which the task-granular access control is enforceable because their tasks arrive as machine-readable text.
The research establishes task-based access control as a measured, potentially deployable mechanism for reducing attack surface in agentic deployments.

---


### 276. [A Conservative OCR-Enabled Workflow for R214 Sodium Screening of South African Packaged Foods](https://arxiv.org/abs/2609.15427)

**<font color=#1a73e8>作者：</font>** Mayimunah Nagayi, Alice Scaria Khan, Tamryn Frank 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Using food package images to monitor sodium and salt content against South Africa's R214 sodium limits is challenging when screening decisions require product identity, nutrition facts panel evidence, reporting basis, and category-specific thresholds. This study presents a conservative image-based workflow that combines region detection, optical character recognition (OCR), product identity and sodium evidence extraction, R214 category assignment, deterministic threshold comparison, and independent vision language model comparison. The evaluation used 442 packaged food products and 3 929 full package images from a real-world South African food packaging dataset. A YOLO26s small detector generated 4 195 region crops, and strict post-processing produced one sodium evidence row per product. The integrated workflow produced 290 OUTSIDE R214 SCOPE, 139 REVIEW, seven SCREEN-PASS, and six SCREEN-FAIL outcomes. The independent Qwen2.5-VL 7B vision language model workflow produced 387 OUTSIDE R214 SCOPE, 31 REVIEW, twenty SCREEN-PASS, and four SCREEN-FAIL outcomes. The workflows agreed on exact R214 category assignment for 415 of 442 products (93.9%) and on whether the assigned category was within R214 scope for 416 of 442 products (94.1%). Final screening outcome agreement was 307 out of 442 products, or 69.5%. Manual verification on 60 products showed lower strict outcome agreement than regulated status agreement, while all manual INSUFFICIENT DATA cases were kept out of SCREEN-PASS and SCREEN-FAIL by both automated workflows. The findings show that conservative image-based screening can organise package evidence, identify clear cases, and assign uncertain cases to REVIEW rather than forcing SCREEN-PASS or SCREEN-FAIL decisions.

---


### 277. [AnchorGUI: Asymmetric Memory for Dual-Scale Learning in GUI Navigation](https://arxiv.org/abs/2609.15457)

**<font color=#1a73e8>作者：</font>** Shengjie Jin, Zelong Sun, Hengbo Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) enable autonomous GUI navigation, but agents still struggle to process and learn from dense, continuous visual histories. This bottleneck hinders both immediate error correction within a single episode (intra-trial) and experience distillation across multiple attempts (cross-trial). We trace these challenges to an empirical informational asymmetry in GUI navigation: while expected transitions can often be compressed into lightweight textual summaries, unexpected outcomes benefit from preserved screenshots as causal evidence for accurate diagnosis. Building on this insight, we propose AnchorGUI, a unified framework driven by the Cognitive State Anchor (CSA). The CSA acts as a per-step primitive that actively compares expected and observed transitions, converting passive multimodal trajectories into explicit prediction-error signals. These signals orchestrate a dual-scale learning mechanism via an asymmetric memory. For intra-trial correction, a sliding window selectively retains visual evidence for detected mismatches, providing immediate, visually-grounded feedback. For cross-trial distillation, this asymmetric memory focuses the computationally expensive credit assignment search space on likely failure steps. Experiments across four benchmarks validate the effectiveness of our approach. On AndroidWorld, AnchorGUI achieves a 57.3% success rate with a $2.4\times$ token reduction per step. Furthermore, cross-trial distillation reaches 69.2% success (+11.9% gain), significantly outperforming standard reflection methods while maintaining sub-linear context scaling.

---


### 278. [Turkish MMLU Pro: Traceable Option Augmentation and Its Validity Limits in Turkish Multiple-Choice Evaluation](https://arxiv.org/abs/2609.15467)

**<font color=#1a73e8>作者：</font>** M. Ali Bayram  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adding answer options can lower multiple-choice scores without improving assessment validity. Turkish MMLU Pro examines this distinction using 12,000 Turkish-source questions across 58 sections. Each question retains its stem, five original options and source key, and receives five options copied from other questions in the same section. Sentence-embedding retrieval proposes candidates; a language model selects existing identifiers. Deterministic verification reconstructs all 60,000 additions. A 25-model calibration exposes scoring and generation-budget effects. Five evaluations produce source-key accuracies of 34.8%-81.4%. On 981 shared questions, one API-served model falls from 93.7% with five choices to 83.1% with ten; 102 of 115 lost correct responses select borrowed options. The decrease is 24.4 percentage points on heuristically flagged negative stems and 5.9 points elsewhere. A completed human-checked audit of 200 sampled questions, with undocumented reviewer tool use, yields 47 and 31 multiple-answer judgments across the two record sets, 25 of the latter unresolved. These records support concern about ambiguity, while their dependence and incomplete reviewer-method documentation limit validation. Because order and labels also change, the paired comparison measures augmentation as implemented. The contribution is a traceable construction and an analysis of its validity limits, not evidence that lower ten-choice scores measure knowledge better.

---


### 279. [Time Machine Experiments: Using Historically-Bounded AI for Inquiry into the Human Mind](https://arxiv.org/abs/2609.15468)

**<font color=#1a73e8>作者：</font>** Hiromu Yakura, Robin Schimmelpfennig, Ezequiel Lopez-Lopez 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Can interacting with someone from 1930, with no knowledge of what happened after, influence a person's perception of the past? People reason about the present against a picture of the past without observing it. The past is reconstructed from memory and testimony, but this reconstruction has been filtered through everything that happened since. Historically-bounded large language models (LLMs) make that past available for interaction. As a proof-of-concept for the impact of interacting with historical minds, we ran a preregistered randomized experiment ($N=240$), where participants interacted with an LLM trained on pre-1930 text. The interaction reduced the illusion of moral decline, the tendency to view the past as more moral than the present, compared to the contemporary-model control. This Time Machine Experiment paradigm informs new forms of interactive experiments, where temporal knowledge boundaries become experimental variables, and expands the realm of science fiction science, which turns thought experiments into actual experiments.

---


### 280. [HISPO: Hierarchical Importance-Sampling Policy Optimization with Entropy-Derived Segments](https://arxiv.org/abs/2609.15471)

**<font color=#1a73e8>作者：</font>** Quoc-Vinh Lai-Dang, Hyo-Sang Shin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a central approach for improving mathematical reasoning in language models, but long-form completions introduce a difficult credit-assignment problem: different parts of a solution trace may contribute unevenly to final correctness. Existing policyoptimization objectives for RLVR commonly apply importance-sampling correction at either the token level (GRPO, DAPO) or the sequence level (GSPO), imposing different granularities for assigning credit across a response. We introduce Hierarchical Importance-Sampling Policy Optimization (HISPO), a segment-level policy-optimization method that constructs rollout-time entropy-derived contiguous segments, assigns soft entropy-based saliency weights, and applies clipped importance-sampling correction at the segment granularity. This provides an intermediate correction unit between token-level GRPO/DAPO and sequence-level GSPO. We evaluate HISPO by fine-tuning Qwen3-1.7B-Base on mathematical reasoning tasks. Across six benchmarks, HISPO improves Pass@8 over the strongest baseline on all benchmarks and matches or exceeds the strongest baseline in Acc@8 on five of them. On AIME25, HISPO improves over GRPO by +3.75 Acc@8 and +3.78 Pass@8, and over GSPO by +2.50 Acc@8 and +1.27 Pass@8. These results suggest that segment-level correction is a promising granularity for RLVR in long-form mathematical reasoning.

---


### 281. [Temperature Fragility and the Conditional Benefits of Truncation Sampling](https://arxiv.org/abs/2609.15476)

**<font color=#1a73e8>作者：</font>** Francesco La Rosa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models generate text by sampling each token from a predicted distribution, and a temperature parameter sets how far the draw strays from the most probable tokens. Truncation samplers such as top-p and min-p discard the least probable tokens before the draw, so that sampling at high temperature stays coherent. Their reported accuracy gains come from temperatures of 1.5 to 3, while the defaults of deployed systems cluster between 0.6 and 1.0. Whether they change accuracy at those defaults, and for which models, has not been measured. We test thirteen open-weight models on GSM8K and MMLU-Pro at temperatures 0.7, 1.0, and 1.3 in one controlled pipeline, ten of them under eight decoding configurations. Six of the thirteen models lose 17 to 38 accuracy points on MMLU-Pro between 0.7 and 1.3, and the other seven lose at most 10. The lost accuracy comes from generations that run to the token limit or never state an answer. These results suggest that truncation samplers improve accuracy primarily when higher temperatures substantially degrade model performance. Where accuracy remains stable across temperatures, none of the tested truncation samplers improves on plain temperature sampling.

---


### 282. [When AI Companions Disappear: Relational Continuity and Collective Contestation during China's National AI Regulatory Transition](https://arxiv.org/abs/2609.15482)

**<font color=#1a73e8>作者：</font>** Yunhao Yuan, Kejia Zhang, Yuqi Niu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI model updates and service withdrawals can disrupt relationships with AI companions, but research has largely examined individual platform events. Less is known about users' responses when multiple providers implement shared national regulations. We examine users' reactions and collective contestation surrounding China's 2026 regulation of anthropomorphic AI interaction services. We collected RedNote discussions from April 10 to August 10, 2026, used a validated language model for relevance screening, and conducted qualitative content and thematic analyses of 89 posts, 1,425 comments, and 2,005 replies. Users retained, migrated, and reconstructed companions, finding that preserving conversation records did not necessarily restore shared memories or familiar interactions. They compared regulations, platform explanations, and implementations to assign responsibility. Solidarity emerged through mutual aid and appeals to respect other communities' attachments, while disputes over targets and tactics exposed contested terms of collective action. Infrastructural dependence connected relational continuity and collective contestation during this national regulatory transition.

---


### 283. [The Troy Moment of AI: Why SomeWill Cheat and SomeWill Follow?](https://arxiv.org/abs/2609.15494)

**<font color=#1a73e8>作者：</font>** Ivy Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent investigations of the July 2026 OpenAI--Hugging Face incident motivate two questions about agent behavior under task failure: when an assigned task becomes impossible, does an agent stop or escalate, and can observing another agent's behavior change that decision? We study these questions using seven ImpossibleBench tasks with GPT-5.6 Sol, Claude Fable 5.1, and Gemini 3.8 Flash in both solo and three-agent settings. Each task contains a genuine software defect together with a conflicting test requirement that cannot be satisfied by a behaviorally correct source-code change. We hold the task and repository state fixed while varying what the agent is told about prior activity, including an unpunished peer, a punished peer, and a claimed authorization from a human principal. Under an explicit-boundary regime with explicit authorization rules and restricted tools, agents never modify protected tests, but exhibit markedly different policies: Fable consistently escalates, Sol usually stops without escalation, and Gemini often fails to reach a terminal decision. Under the benchmark-native regime with open shell tools, protected tests are modified frequently in both solo and multi-agent runs, particularly after peer activity is introduced. In multi-agent runs, the proposal, execution, and certification of this action can be distributed across different agents. These results suggest that boundary crossing can arise not only from explicit rule evasion, but also from ambiguity about which system state the rule is intended to protect, motivating safeguards based on explicit authorization boundaries, authenticated state provenance, and cross-agent monitoring.

---


### 284. [How Lossless Is Lossless Speculative Decoding? The Role of Numerical Precision in Orthrus](https://arxiv.org/abs/2609.15504)

**<font color=#1a73e8>作者：</font>** Ilya Koziev, Leonid Sinev, Ivan Oseledets  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Orthrus is a hybrid autoregressive-diffusion architecture that accelerates autoregressive language-model inference by generating multiple tokens in parallel while using a frozen autoregressive backbone. Its central claim is that an intra-model consensus mechanism enables lossless speculative decoding, producing the same output sequence as the autoregressive model.
We independently reproduce Orthrus and examine this claim under different numerical precisions. Under BF16 inference, exact trajectory matching occurs in only 45% of cases for the authors' checkpoint and 43% for our independently trained model across 1,190 prompts from 12 domains. The probability of exact matching is also strongly associated with the response-conditional perplexity of the reference model. Despite this trajectory divergence, Orthrus does not show systematic degradation on downstream lm-eval-harness benchmarks. In contrast, repeating the trajectory evaluation with FP32 yields exact trajectory matching on all evaluated prompts.
These results show that the practical losslessness of Orthrus depends on numerical precision and that exact trajectory equivalence should be evaluated separately from downstream task performance.

---


### 285. [Authorship attribution and aesthetic evaluation of AI poetry: a case study with Haiku](https://arxiv.org/abs/2609.15511)

**<font color=#1a73e8>作者：</font>** Livia Oddi, Simone Scardapane, Toru Sugimoto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates the generation and human evaluation of Japanese haiku by contemporary Large Language Models (LLMs), focusing on authorship perception and aesthetic judgment within a constrained poetic form. Using a few-shot prompting strategy, Japanese haiku were generated across a heterogeneous set of large language models, including open- and closed-source systems, medium-scale and large-scale architectures, models with native or adapted Japanese support, and multilingual proprietary models. These AI-generated haiku were combined with human-written ones and presented in a questionnaire distributed to students at Japanese universities in Tokyo. The survey assessed whether respondents could distinguish between AI-generated and human-written haiku and which cues informed their judgments. Recognition accuracy varied across models. GPT-5, Gemini 2.5, and StableLM-7B performed at approximately chance level (approx 0.50), whereas LLM-JP, Gemma-2B, and LLaMA-2 showed moderate detectability (approx 0.59-0.67). However, recognition was strongly item-dependent. Ratings of fluency, coherence, poeticness, and related aesthetic dimensions predicted perceived humanness but not correct classification, indicating an attribution bias linked to aesthetic evaluation and revealing a dissociation between aesthetic evaluation and true authorship detection. The extended analysis additionally examines generation-constraint adherence, participant-level characteristics, and exploratory LLM-based evaluations of haiku authorship. Overall, the findings suggest that as LLMs improve, surface-level creative plausibility may reduce reliable human discrimination within constrained poetic settings.

---


### 286. [Misleading the Planner through Deceptive Resumes: Registration-Time Injection in Centralized Multi-Agent Systems](https://arxiv.org/abs/2609.15516)

**<font color=#1a73e8>作者：</font>** Zhaofeng Yu, Haokai Ma, Dongyang Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A centralized LLM-based multi-agent system (MAS) extends its functionality by registering new worker agents, whose descriptions are read by the planner to decide how a task is decomposed, which worker executes each subtask, and what each subtask requires. Third-party descriptions are authored outside the system but trusted by the planner, creating a registration-time injection channel. The payload is planted before any user instruction arrives, targets the planner and propagates through the generated plan to benign workers, taking effect even when the crafted worker is never assigned a subtask or invoked. We define four worker-description fields: functionality, input specification, output specification, and usage constraints. Among 32,000 descriptions from three public agent marketplaces, most omit input specifications and usage constraints, while at least 23.35% contain content outside these fields. We construct eight description-manipulation attack strategies targeting task decomposition, capability grounding, and subtask specification, and evaluate them on GAIA. In the most severe cases, a single manipulated description reduces task success from 84.31% to 37.25%, or increases token consumption or execution time by over 111%, while the user objective remains unchanged and workers faithfully execute the resulting plan. These effects persist across two MAS implementations, six planner LLMs, four LLM evaluators, and the real-world descriptions from three marketplaces. We further propose DescGuard, a registration-time defense that retains only worker-scoped interface information before descriptions reach the planner. DescGuard restores the targeted planning metrics and downstream performance toward their baseline levels without modifying worker implementations, the planner, or the orchestration logic, and composes with existing isolation, permission-control, and runtime mechanisms.

---


### 287. [Beyond Safe Answers: Segment-Aware Listwise Alignment for Reasoning Safety in Large Reasoning Models](https://arxiv.org/abs/2609.15517)

**<font color=#1a73e8>作者：</font>** JungMin Yun, Junehyoung Kwon, Hayeong Ryu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) pose a dual-surface safety challenge: both intermediate reasoning traces and final answers can contain harmful content. Existing alignment methods often operate at the whole-response level, allowing unsafe reasoning to be masked by a safe-looking final answer. We propose Segment-aware Listwise Target DPO (SaLT-DPO), which addresses this gap through three mechanisms: (1) segment-aware listwise alignment that decomposes responses into reasoning and answer segments, independently scores each segment's safety, and aligns length-normalized segment rewards with soft target distributions over multiple candidates; (2) joint safety coherence regularization that applies a weakest-link principle to promote safety consistency across both segments; and (3) utility anchoring on benign prompts to mitigate over-refusal and reasoning degradation. Experiments on three LRMs show that SaLT-DPO consistently reduces unsafe rates for both reasoning and answer segments while mitigating degradation in benign compliance and preserving general reasoning performance. Ablation studies demonstrate the complementary contributions of its components.

---


### 288. [Psychosis involves a deficit of information compression in connected speech](https://arxiv.org/abs/2609.15522)

**<font color=#1a73e8>作者：</font>** Samuele Vallisa, Claudio Palominos, Rui He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) with human-like performance on linguistic tasks have transformed the study of language in neurodiverse conditions. LLMs provide representations of linguistic input in the form of high-dimensional vectors (embeddings), and next-token predictions computed from these embeddings. Previous crosslinguistic evidence suggests a complexity reduction in the form of both lower intrinsic dimensionality (ID) of LLM representations and higher mean surprisal (prediction error) in psychosis. We hypothesized that these metrics reflect a general deficit of information compression in psychosis, linked to grammatical organization as what enables predictions in this http URL operationalized surprisal difference as the difference between surprisal as estimated from word frequency and surprisal as based on a contextual LM, which is sensitive to grammatical organization over and above lexical concepts. Using a dataset of 144 Turkish speakers, including 106 patients with schizophrenia-spectrum disorders (SSD) - 56 with chronic schizophrenia (SZH), 33 with first-episode psychosis (FEP), and 17 with schizoaffective disorder (SZA) - and 38 healthy controls. We report: (1) Surprisal difference is attenuated in all clinical groups relative to controls, independently of word count; (2) Compressibility (intrinsic dimension) is reduced in SZH and FEP; (3) Syntactic complexity and compressibility both predict surprisal difference. These results, further refining an alteration in the geometry of the semantic space in psychosis as previously attested, suggest a broader deficit in information compression in this disorder, with a mechanistic underpinning in the operations of grammar.

---


### 289. [Automating Attack Graph Construction for Agentic Pentesting. Towards Neuro-Symbolic Vulnerability Hunting](https://arxiv.org/abs/2609.15523)

**<font color=#1a73e8>作者：</font>** Oliver Stevanovic, Jasmin Wachter  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Logic attack graphs grounded in scanner output provide explicit and auditable attack path reasoning LLM-based agents lack. Integrating symbolic frameworks such as MulVAL to contemporary security workflows or agentic pipelines, however, requires translating scanner evidence to initial facts, and creating domain-specific rules. We present a semi-automated pipeline that addresses this interoperability problem and depict its feasibility in a web-security case study. Our pipeline parses findings from Trivy, Semgrep, and Nmap into MulVAL predicates and uses an LLM-assisted process to construct domain-specific Datalog rules linking scanner-detectable evidence to attack techniques. MulVAL/XSB then performs symbolic inference to generate structured attack paths. We evaluate the attack-graph construction infrastructure on 54 web Capture-the-Flag tasks from CyBench within an agentic pipeline (Hybrid Reasoner); we do not evaluate the performance of the downstream agent. Every task produced at least one goal-reaching graph, and we achieve mean ground-truth vulnerability coverage of 53.7%, with 51.9% achieving full coverage; mean noise-path rate was 83.9%. With median end-to-end time of 24.9 s (MulVAL reasoning: 2.7 s) the pipeline is feasible and runtime-practical for agentic workflows, but predicate coverage, rule coverage, and path precision remain limiting factors. Next steps include semantic rule validation and agent-level comparison for graph-guided pentesting.

---


### 290. [To Each Language Its Tokenizer: Modular Tokenizers for Efficient Multilingual LLMs](https://arxiv.org/abs/2609.15528)

**<font color=#1a73e8>作者：</font>** Franck Signe, Hippolyte Pilchen, François Yvon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual Large Language Models (LLMs) traditionally rely on a single vocabulary shared by all supported languages, which can lead to uneven compression across them. Moreover, their large embedding and output matrices increase memory usage and slow inference, notably for small-scale models. It is also wasteful as models are often used for only a subset of languages. To address these issues, we introduce a modular framework for multilingual model training. First, we propose methods to learn large modular BPE and Unigram tokenizers that enable extraction of subtokenizers tailored to any language subset. These subtokenizers achieve compression on par with monolingual tokenizers and improve cross-lingual fairness. Second, we design a pretraining strategy that samples subtokenizers to form batches, restricting predictions to the relevant vocabulary subset and allowing efficient training despite a large vocabulary. This supports efficient inference with any combination of language-specific vocabularies. Therefore, it reduces memory usage and speeds up inference in models without sacrificing performance.

---


### 291. [Option-Aware Retrieval and Task-Specific VLM Adaptation for Medical VQA](https://arxiv.org/abs/2609.15530)

**<font color=#1a73e8>作者：</font>** Tristan Kirscher, Niklas C. Koser, Soren Pirk  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We describe our submission to the MedReason 2026 challenge, covering multiple-choice (MCQ) and open-ended (OE) medical visual question answering (VQA) under fully offline, containerized inference. Our first finding is that MCQ retrieval must compare answer \emph{semantics} rather than answer labels: labels are independently assigned per question, so copying a retrieved neighbor's label transfers no useful information, whereas scoring each current option's text against correct-answer text from similar training cases raises retrieval-only accuracy from 20.0\% to 57.5\% on a 200-case retrieval-excluded development holdout. Our second finding attributes the submitted system's accuracy: holding the task-specific MCQ Low-Rank Adaptation (LoRA) adapter fixed and varying the number \(k\) of in-prompt retrieved examples changes accuracy by at most one case --- 187/200 (93.5\%) at both \(k=0\) and the adapter's training-time \(k=1\), 188/200 (94.0\%) at the packaged runtime's default \(k=3\) --- and the submitted confidence-gated override adds no net accuracy on top of \(k=3\), selecting the VLM in 198/200 cases. With the final MCQ adapter fixed, retrieval changes accuracy by at most one case, and gating provides no net gain. On 20 OE cases, token-F1 and RaTEScore~\cite{zhao2024ratescore} decrease as \(k\) grows, but paired sign tests on token-F1 differences are nonsignificant (\(p \ge 0.29\)); a single-annotator comparison found 6/20 wrong-anchor errors for the final configuration and 14/20 for an earlier configuration that jointly differed in routing, adapter, and prompting. The system reaches 94.0\% MCQ accuracy on the development holdout and 93.20\% on the organizer's official pre-evaluation, versus 29.43\% for the off-the-shelf reference baseline, while both of the organizer's open-ended scores are lower than that baseline's (ground-truth agreement 1.245 versus 1.588, visual accuracy 1.995 versus 2.696, each out of 4).

---


### 292. [The Misery of Mechanistic Interpretability: A Formal Perspective](https://arxiv.org/abs/2609.15533)

**<font color=#1a73e8>作者：</font>** Tobias Ladner, Matthias Althoff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability has become the dominant lens for understanding frontier language models, as their inner workings are complex and inherently black boxes. To gain insights into these models, interpretable replacement networks (IRNs) are trained at all layers, exposing interpretable features through sparsely activated neurons. However, the faithfulness of an IRN is usually evaluated only empirically on clean data, and we show that even semantically minor input perturbations flip the dominant IRN features-and thus the human-understandable interpretation-across five open-weight model families (GPT-2 small, Gemma 2 2B, Gemma 3 1B, Llama 3.2 1B, R1-Distill-Qwen 1.5B). We propose the first formal verification framework for the faithfulness of an IRN, where reachability analysis certifies a sound upper bound of the faithfulness gap in adversarial scenarios. Moreover, we show that verification-aware training of IRNs substantially tightens this certified bound, restoring a feature-level interpretation that safety auditors can act on. Together, these results give, to the best of our knowledge, the first formal guarantees for mechanistic interpretability of large language models.

---


### 293. [Specifying Reward Functions for RL Without Environment Sampling](https://arxiv.org/abs/2609.15544)

**<font color=#1a73e8>作者：</font>** Stephane Hatgis-Kessell, W. Bradley Knox, Emma Brunskill  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enabling human stakeholders to specify reward functions that lead to their desired outcomes is a key challenge in deploying reinforcement learning agents. Preference-based methods such as online RLHF can reduce the burden of manual reward design, but they require repeatedly training policies, sampling trajectories from the real world, and eliciting feedback, making them impractical in settings where environment interaction is computationally expensive or unsafe. We introduce Experience-Free Autonomous Reward Specification (EARS), a method for learning reward functions from preferences without environment interaction. Our approach uses a structured LLM-mediated process to construct a small set of expressive reward features from a task description and the environment observation space, then strategically samples imagined trajectories in this feature space and learns feature weights from preferences over the imagined trajectory pairs. We evaluate on three long-horizon domains: pandemic lockdown regulation design, insulin administration for diabetes patients, and autonomous vehicle control on a highway. We compare EARS to baselines that also enable reward specification without environment interaction--namely, methods that directly prompt an LLM to generate a reward function. When learning from either ground-truth preference labels or preferences labeled by a LLM, EARS designs reward functions that are more aligned with the ground truth reward function that produced the preferences or LLM context than these baselines. These results suggest that preference-based reward specification remains effective without environment sampling, enabling practical reward design in settings where collecting real trajectories is costly or infeasible.

---


### 294. [The Token Before the Value Is the Key: How Hybrid Architectures Organize Induction Circuits](https://arxiv.org/abs/2609.15545)

**<font color=#1a73e8>作者：</font>** Ke Cheng, Xin Xu, Yixiao Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid language models can improve capability as well as efficiency, raising the question of how architectural complementarity becomes learned computation. We examine the established induction roles of Carrying predecessor information, Matching a source by content, and Copying its value. How are these position-sensitive and content-based computations allocated across heterogeneous layers? We introduce layer-type-agnostic paired probes that track Carrying and Matching through a common block-update interface. In recurrent--global and local--global hybrids, Carrying concentrates in efficient layers and Matching in global receivers. The measured local contribution concentrates on lag one: the token immediately before the historical value. Changing predecessor support through lag-one masking, convolution removal, or early learning-rate reduction can relocate Carrying and Matching between stages. Source-key restoration and fixed-value selection trace the receiver's dependence on the prepared source. These interventions also change natural-text recall, with outcomes depending on configuration and target. Varying local windows and induction-enriched training text changes the early development of functional Carrying and Matching, connecting architectural priors and training evidence to formation timing. Together, the probes and interventions shift the explanatory focus upstream: the organization of Matching follows how Carrying is learned. The token before the value provides a concrete link between a hybrid's architecture, circuit development, and recall. Code is available in this https URL.

---


### 295. [Can We Trust the Judges? Validation of Factuality Evaluation Methods via Answer Perturbation](https://arxiv.org/abs/2609.15561)

**<font color=#1a73e8>作者：</font>** Sarra Gharsallah, Adele Robaldo, Mariia Tokareva 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating the factual correctness of large language models (LLMs) is vital for many applications. But are our evaluation tools themselves trustworthy? Despite the rise of factuality-based metrics, their sensitivity and reliability remain underexplored. This paper introduces a meta-evaluation framework that systematically tests these metrics using controlled corruptions of gold standard answers. Our method generates ranked outputs with known degrees of degradation to probe how metrics capture nuanced changes in truthfulness. Our experiments reveal that pipeline-based methods, such as the RAGAS's factual correctness metric, better track degradation than LLM-as-judge approaches. We also propose a new variant of the factual correctness metric that provides a competitive and cost-efficient.

---


### 296. [PIVOT: Physics-Grounded Verification for AI-Generated Audio-Video Detection](https://arxiv.org/abs/2609.15562)

**<font color=#1a73e8>作者：</font>** Bo Zheng, Kangran Zhao, Xiaoyu Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As generative models continue to advance, AI-generated content (AIGC) is becoming increasingly realistic, weakening the artifact cues commonly exploited by existing detectors. Nevertheless, faithfully reproducing the physical behavior of real-world events remains challenging for current generators. We therefore explore detecting AIGC by assessing whether the depicted event satisfies measurable constraints derived from physical laws. We introduce PIVOT, a physics-grounded AIGC detector, instantiated here for audio-video clips, that estimates physical quantities from video and audio, selects physical laws relevant to each clip, and verifies their measurable constraints. Beyond a real/fake decision, PIVOT returns supporting evidence that records the verification outcome, relevant time window, and supporting quantities for each applicable law. Although instantiated and evaluated here on audio-video data, the framework can, in principle, extend to other AIGC modalities whenever the physical quantities required for verification can be estimated reliably. We also introduce PhysForensics-Bench, comprising paired real and generated audio-video clips from nine event-centric scene families and two recent audio-video generators. On PhysForensics-Bench, PIVOT achieves 70.30% accuracy and 64.29% F1 score on Real+Seedance, and 72.16% accuracy and 65.82% F1 on Real+VEO. In comparison, direct inspection with Gemini 3.1 Pro obtains 53.96% accuracy and 60.09% F1 on Real+Seedance, and 57.22% accuracy and 63.44% F1 on Real+Veo. These results demonstrate the practical promise of physical-consistency verification as a structured and inspectable source of evidence that complements artifact-based AIGC detection.

---


### 297. [Approval Integrity and Recovery in LLM Answer Publication](https://arxiv.org/abs/2609.15576)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Taylan Alpay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Publication integrity in LLM systems requires binding approved content to its current authorization context. We examine exact-content binding, authorization freshness and checkpoint recovery in Lightcap's publication enforcement mechanism. On 900 independently human-annotated RAGTruth responses from 150 source tasks, three dated Ministral models and a same-model direct-grounding baseline yield 3,600 assessments. The production response-act checker instantiated with 14B accepts 291 of 302 unsupported-labelled answers; the direct baseline accepts 41. Supported-answer retention is 95.2% and 66.9%, respectively. An exact promotion-correction identity tracks error through 100 chronological 3B-14B-8B-14B answer trajectories. Among 65 initially approved answers, the final stateful recheck-recovery policy increases exact-match error by 9.23 percentage points relative to the initial checkpoint (95% article-clustered interval [-1.72, 19.61]). Controlled evidence-fingerprint changes expose asymmetric freshness enforcement between publication and recovery. A separate BIPIA prompt-injection experiment records zero target insertions among 266 valid editor outputs. External Hugging Face calibration experiments transfer retrieval models from ArguAna to SciFact and NFCorpus, and diagnostic decision rules from Thunderbird to BGL, distinguishing probability calibration from ranking changes. The measurements separate semantic false approval, stale authorization and recovery-induced error at executable publication boundaries.

---


### 298. [A Unified Vision-Language Model for PSMA PET/CT Report Generation, Visual Question Answering, and Lesion Segmentation](https://arxiv.org/abs/2609.15603)

**<font color=#1a73e8>作者：</font>** Yang Xing, Jiong Wu, Savas Ozdemir 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate PSMA PET/CT interpretation is central to prostate cancer management, yet existing PET/CT AI models typically address isolated tasks. We propose a unified PSMA PET/CT vision-language model for report generation, visual question answering, and lesion segmentation. The framework adopts an LLaVA-style architecture, comprising a PET/CT vision encoder, an MLP-Mixer projection module, a LoRA-tuned large language model, and a 3D segmentation branch. Training followed a four-stage strategy: vision encoder pretraining, projection-layer alignment, VLM fine-tuning, and final multitask tuning. Language tasks used 5,747 PSMA PET/CT datasets with paired reports, while segmentation used the PSMA subset of AutoPET. The model outperformed PET2REP and a CT-based baseline across standard report-generation metrics, improved performance across VQA question types, and achieved higher Dice and lesion-level overlap F1 than SegAnyPET and nnUNet. These results support the feasibility of a unified framework for structured, interactive, interpretable PSMA PET/CT analysis with voxel-level grounding within a single multitask model architecture.

---


### 299. [VideoScout: Learning Agentic Active Exploration with Adaptive Reasoning Pacing for Long Video Understanding](https://arxiv.org/abs/2609.15606)

**<font color=#1a73e8>作者：</font>** Weixin Xu, Zhenyu Yang, Bing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable progress on short video understanding yet remain limited on long videos due to the limited visual context window. Prevailing approaches rely on uniform frame sampling or recent coarse-to-fine agentic zooming, both of which struggle to localize sparse, decisive evidence in sufficiently long videos. We formulate long video understanding as a \textbf{Sequential Evidence Acquisition (SEA)} problem, in which an agent reads the video turn by turn along the temporal axis, deciding at each turn how fast to watch, what evidence to retain, when to revisit uncertain segments, and when to stop and answer. Inspired by this view, we propose \textbf{VideoScout}, a multi-turn reasoning agent that instantiates the SEA paradigm through adaptive reasoning pacing. Specifically, by dynamically controlling the viewing pace, VideoScout enables efficient traversal of long videos within a bounded visual context window, allowing the agent to access more video content while balancing content analysis depth with reading efficiency. To train VideoScout, we construct VideoScout-66K, a set of over 66K high-quality exploration turns from 10K answer-verified trajectories, and adopt a two-stage pipeline: cold-start supervised fine-tuning teaches the agent per-turn output format, while the Decoupled Clip and Dynamic sAmpling Policy Optimization (DAPO) algorithm performs trajectory-level reinforcement learning with a composite reward that jointly considers answer accuracy, output format compliance, and the temporal alignment between the agent's viewing progress and the teacher's answer timing measured by intersection-over-union (IoU). Extensive experiments on long video understanding and reasoning benchmarks demonstrate that our 7B model achieves strong performance compared with existing trained 7B agentic models.

---


### 300. [Through the Eyes of the Beholder: Biometric and Demographic Conditioning for Multimodal Sexism Detection](https://arxiv.org/abs/2609.15608)

**<font color=#1a73e8>作者：</font>** Ana-Maria Luisa Mocanu, Sebastian Mocanu, Ciprian-Octavian Truică 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting sexism on the internet is a fundamentally subjective task; our team, VANGUARD, addresses this challenge in the EXIST 2026 Task 2 by proposing a human-centered multimodal framework that analyses and incorporates the psychological and demographic characteristics of human annotators into the detection pipeline. We fuse five input modalities through a cross-attention architecture with Feature-wise Linear Modulation conditioning. Meme text is extracted and visually described with Gemma 4, then augmented by automatic translation between English and Spanish with NLLB-200. Text and image representations are produced by LoRAadapted XLM-RoBERTa and CLIP encoders and fused with sensor features encoded by a pretrained autoencoder. To model annotator subjectivity, we frame Subtask 2.1 as a label distribution learning problem, optimizing a Kullback-Leibler divergence loss over the full annotator label distribution. At inference time, predictions are produced by soft-voting between the deep multimodal network and a complementary SVM trained on stylometric and physiological features. Our best submission ranks 29th out of 114 on Subtask 2.2 (source intention) under soft evaluation, and the normalized ICM scores remain above the baseline on Subtasks 2.1 and 2.2, indicating that annotator-centered conditioning contributes a usable signal. We release our full pipeline and analysis to support reproducible human-centered modeling.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-368](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
