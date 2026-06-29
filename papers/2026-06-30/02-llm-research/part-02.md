# 🧠 大模型相关研究 | 2026年06月30日

> 本类共 **84** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-84**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-84**

---

### 51. [Grounded Iterative Language Planning: How Parameterized World Models Reduce Hallucination Propagation in LLM Agents](https://arxiv.org/abs/2606.27806)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Zekun Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models for language agents come in two useful forms. An agent-based world model calls an LLM API and reasons flexibly in language, but its errors appear as hallucinated state changes that are hard to score with ordinary regression losses. A parameterized world model is a trained transition predictor; its errors are easier to measure with quantities such as NodeMSE, delta accuracy, and validity accuracy, but it is usually weaker as a standalone planner. We compare these two families on four graph-structured planning benchmarks and introduce operational hallucination metrics for the agent-based case. The comparison motivates \textbf{Grounded Iterative Language Planning} (GILP), which trains only a small parameterized backbone and combines it with API-based agent reasoning. The backbone supplies valid actions, predicted state deltas, risk, and value; the LLM drafts an action and imagined delta; and a consistency gate asks for revision when the two disagree. On real GPT-4o-mini calls, GILP reduces hallucinated-state rate from 0.176 to 0.035. In calibrated simulator ablations, it raises success from 0.668 to 0.838 while adding only ~22% extra LLM calls.

---


### 52. [NormAct: A Benchmark for Hidden Social Norm Compliance in Embodied Planning](https://arxiv.org/abs/2606.27826)

**<font color=#1a73e8>作者：</font>** Shiyun Zhao, Xinwei Song, Tianyu Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly deployed as embodied planners in egocentric environments, where task success requires not only achieving instructed goals but also acting in socially appropriate ways. While explicit goals may render certain actions optimal, implicit social norms often impose hidden constraints. Existing evaluations typically focus on explicit goal achievement or direct norm knowledge, seldom assessing whether planners can infer and apply these hidden constraints within action sequences. We introduce NormAct, a benchmark for embodied social-norm interactions that evaluates plans on Goal Achievement, Norm Compliance, and overall Task Success. NormAct uniquely embeds hidden norms within ordinary tasks, testing whether models can realize them without explicit instruction. Experiments with state-of-the-art MLLMs (GPT-5.4, Claude Opus 4.7, Gemini 3 Pro) reveal a significant gap: models achieve explicit goals in 67.3\% of cases, but comply with hidden norms in only 26.4\%. Cue-condition experiments indicate that this gap stems not from a lack of general social knowledge, but from challenges in activating and grounding relevant norms in context. To address this, we propose NormPerceptor, a context-conditioned cue generator that infers scene-relevant norms prior to planning, increasing Task Success from 24.2\% to 46.7\%. Our results underscore the importance of enabling embodied agents to proactively detect hidden norms, ground them in visual evidence, and integrate them as action-planning constraints. Our benchmark is publicly available at this https URL.

---


### 53. [Video-MME-Logical: A Controlled Diagnostic Benchmark for Video Temporal-Logical Reasoning](https://arxiv.org/abs/2606.27828)

**<font color=#1a73e8>作者：</font>** Hohin Kwan, Hongyu Li, Ray Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent interest in multimodal large language models (MLLMs) raises a central question: can they reason over dynamic visual evidence rather than merely recognize objects or events in individual frames? This ability, which we refer to as video temporal-logical reasoning, requires models to maintain, update, and compose evidence as visual states evolve across frames. Existing video benchmarks often conflate this capability with scene complexity, static recognition, or uncontrolled temporal variation. To isolate this capability, we introduce Video-MME-Logical, a controlled benchmark organized around five temporal-logical operations: state tracking, sequential counting, temporal ordering, dynamic spatiality, and structural composition. The benchmark contains 25 fine-grained task categories generated with controlled object states, transitions, temporal dependencies, and logical compositions. It enables difficulty-controlled final-answer evaluation by varying temporal horizon and reasoning complexity, and supports intermediate-state diagnostics by verifying whether models recover the required logical reasoning trace before producing the final answer. Experiments with state-of-the-art MLLMs reveal a substantial human-model gap, especially as temporal-logical complexity increases. Supervised fine-tuning on up to 500K generated samples improves performance but remains insufficient to close the reasoning gap, positioning Video-MME-Logical as a scalable testbed for analyzing and improving temporal-logical reasoning in MLLMs.

---


### 54. [FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models](https://arxiv.org/abs/2606.27866)

**<font color=#1a73e8>作者：</font>** Fan Mo, Yuxuan Han, Geng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) language models scale model ability with sparsely activated experts, making this architecture a standard recipe for modern large models. However, sparse activation does not remove the deployment burden of storing and serving all experts, and the available deployment budget can vary substantially across devices, users, and workloads. Existing MoE compression methods are still largely fixed-budget, typically optimizing one compressed endpoint at each chosen target budget. We study a different setting: converting a large pretrained MoE LLM into a nested family of deployable subnetworks across budgets. Our method first ranks expert FFN channels by their importance, then lets each expert learn a discrete action to prune its channels. By gradually increasing cost pressure, a single action-training run exports a series of action masks from high to low budgets, each of which identifies a reliable smaller subnetwork nested in the ranked base model. Moreover, we use a single recovery fine-tune at a mid pruning budget (40%) to recover degraded model quality and transfer the recovered model to other unseen budgets. Overall, our framework surpasses recent MoE compression baselines. Specifically, on Qwen2-57B-A14B, our method retains ~99.8% of base performance while pruning 50% of routed expert parameters even without fine-tuning. For deployment, our pruned subnetworks deliver real memory reduction and throughput gains, and further support realtime online budget switching with kernel-level co-design.

---


### 55. [Triadic Werewolf: A Jester Role for Multi-Hop Theory of Mind in LLMs](https://arxiv.org/abs/2606.27909)

**<font color=#1a73e8>作者：</font>** Avni Mittal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Theory-of-mind evaluations of large language models typically use dyadic social-deduction games, where every observable cue points to a single hidden side, so a model with strong language priors can score well without ever simulating opponents' incentives. We extend the Werewolf game with a Jester, a third faction whose utility on peer suspicion is inverted because it wins by being voted out, so optimal play requires reasoning across three opposing utility functions. Across 60 games on GPT-4.1, DeepSeek-V3.1, and Llama-3.3-70B with Jester self-learning on and off, the Jester wins 60-70% of games while Werewolves never exceed 20%, and GPT-4.1 wolves vote the Jester out on day 1 in 60-70% of games, a strictly self-defeating action. Self-learning helps DeepSeek and Llama but hurts GPT-4.1, with the cost landing on Villagers rather than Werewolves. Only DeepSeek learns the subtle strategy of looking suspicious without looking intentionally suspicious, and it gains the most from the loop. Triadic incentive structure exposes a layer of multi-agent reasoning that dyadic deduction games leave invisible.

---


### 56. [Verifiable Geometry Problem Solving: Solver-Driven Autoformalization and Theorem Proposing](https://arxiv.org/abs/2606.27926)

**<font color=#1a73e8>作者：</font>** Can Li, Ting Zhang, Junbo Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geometry Problem Solving have increasingly adopt the neuro-symbolic paradigm, combining neural intuition with symbolic rigor. However, current frameworks suffer from severe bottlenecks in two core stages: autoformalization, which treats multimodal translation as a static task decoupled from downstream solver compatibility, and theorem prediction, where solvers frequently hit a deductive impasse due to fixed rule libraries. To address these, we propose SD-GPS, a solver-driven framework that treats the symbolic solver as an execution oracle throughout both formalization and deduction. First, Solver-Driven Autoformalization unifies supervised formal-language adaptation and solvability-guided reinforcement learning into a single module built on QwenVL3-2B, making executability the central training signal. Second, Verified Theorem Proposing introduces an impasse-aware agent that proposes local auxiliary lemmas from current proof states, ensuring soundness by filtering all proposals through symbolic verification. Empirical evaluations on Geometry3K and PGPS9K demonstrate that SD-GPS consistently outperforms existing MLLM, neural, and neuro-symbolic methods across standard completion, multiple-choice, and cross-modal reference regimes, proving that closing the loop between multimodal perception and symbolic execution significantly improves geometric reasoning, offering profound insights into how neural agents can be grounded by formal systems to achieve verifiable problem-solving capabilities.

---


### 57. [Two-Stage Fine-Tuning for Protein Sequence Generation with Targeted Amino-Acid Composition](https://arxiv.org/abs/2606.27939)

**<font color=#1a73e8>作者：</font>** Violeta Basten-Romero, Rubén Muñoz-Tafalla, Anna María Díaz-Rovira 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein language models are standard priors for biological sequence generation, but steering them toward explicit distributional design targets remains largely unexplored. We study a constrained protein generation problem in which sequences must match a desired amino-acid (AA) composition profile while preserving plausible sequence statistics and diversity. The motivating application is synthetic feed protein design, where the AA composition of dietary proteins directly determines their nutritional value. We propose a two-stage pipeline in which domain-adaptive fine-tuning (FT) on an in-domain protein dataset is followed by iterative reward-weighted FT via reinforcement learning (RL) anchored against the FT model as a frozen reference. We evaluate the pipeline on two AA compositions and find that FT brings the average composition close to the target, while the subsequent RL enforces specific sequence constraints that FT alone cannot satisfy. We additionally evaluate the design choices of the proposed composition reward term against two baselines and an ablated variant, isolate the contribution of each training stage, and verify that AA composition alignment is achieved without degrading sequence quality.

---


### 58. [Understanding How MLLMs Describe Artworks Using Token Activation Maps](https://arxiv.org/abs/2606.27947)

**<font color=#1a73e8>作者：</font>** Nicola Fanelli, Pasquale De Marinis, Raffaele Scaringi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) describe artworks with remarkable fluency, yet the visual reasoning behind their outputs remains opaque. When an MLLM names a style, identifies a subject, or recognizes an iconographic symbol, does it ground each claim in the relevant region of the canvas, draw on an undifferentiated visual signal, or rely primarily on textual priors? We study this using the Token Activation Map (TAM), which produces, for each generated token, a heatmap isolating the visual evidence specific to that token from prior-context interference. Applying TAM to a curated set of paintings spanning multiple periods and genres, we analyze grounding patterns across five semantically distinct token categories: common visual objects, style descriptors, metadata, iconographic tokens, and affective expressions. We find that visual grounding varies substantially with token semantics. We further show that MLLMs attempt to identify artworks and artists, achieving higher accuracy in artist attribution than in title prediction, where hallucinations are more frequent. Finally, we compare TAM with SAM~3 open-vocabulary segmentation. To ensure reproducibility, we release our code, experimental configurations, prompts, and qualitative results on the project page at this https URL.

---


### 59. [An Empirical Analysis of Factual Errors in Human-Written Text and its Application](https://arxiv.org/abs/2606.27959)

**<font color=#1a73e8>作者：</font>** Kazuma Iwamoto, Kazumasa Omura, Shotaro Ishihara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Factual Error Detection (FED), which is the task of identifying factually incorrect spans in a given text, has long been recognized as an important research problem. However, with the rapid rise of large language models (LLMs), research attention has shifted toward factual errors specific to LLM-generated text (hallucinations) and their detection. As a result, the detection of factual errors in human-written text has been relatively neglected. To address this gap, we first distill a taxonomy of human-induced factual errors by analyzing corrections of newspaper articles, a representative source of text that is guaranteed to be human-written and contains few grammatical errors. Our analysis revealed that there are characteristic categories such as kanji misconversions and numeral classifier errors, which are not focused in existing hallucination benchmarks. Based on the taxonomy, we then evaluate the FED capability of vanilla LLMs on synthesized realistic test cases and real corrections. Experimental results demonstrated that even high-performance LLMs such as GPT-5.4 achieved only word-level F1 score of 52% on the synthetic evaluation data, highlighting the task difficulty. Furthermore, a detailed analysis by detection difficulty revealed the current state of FED.

---


### 60. [From Black-Box to Clinical Insight: A Multi-Stage Explainable Framework for Speech-Based Cognitive Impairment Detection](https://arxiv.org/abs/2606.27973)

**<font color=#1a73e8>作者：</font>** Yasaman Haghbin, Sina Rashidi, Ali Zolnour 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-based cognitive impairment detection offers a noninvasive, accessible alternative to costly biomarker assays, yet transformer-based models remain clinically uninterpretable. We propose a multi-stage explainability framework that translates black-box transformer predictions into clinically grounded narratives by integrating SHapley Additive exPlanations (SHAP)-based token attribution, theory-informed linguistic features, and a four-stage LLM reasoning pipeline using LLaMA-3.1-70B-Instruct. Built on the SpeechCARE-Adaptive Gating Network multimodal screening model (F1 = 72.11% on the NIA PREPARE benchmark), the framework maps model outputs to four cognitive-linguistic dimensions, including lexical richness, syntactic complexity, and semantic coherence. Physician evaluation on 70 stratified English samples demonstrated strong alignment with patient-level cognitive profiles, and a System Usability Scale score of 82/100 indicated high potential for clinical workflow integration.

---


### 61. [ProMSA:Progressive Multimodal Search Agents for Knowledge-Based Visual Question Answering](https://arxiv.org/abs/2606.27974)

**<font color=#1a73e8>作者：</font>** ZhengXian Wu, Hangrui Xu, Kai Shi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge-based Visual Question Answering (KB-VQA) requires models to combine image understanding with external knowledge. Most prior methods use a fixed retrieve-then-generate pipeline with a pre-selected retriever and a static top-k setting, which is not adaptive during reasoning. We propose ProMSA, a progressive multimodal search agent for KB-VQA. Given an image-question pair, the agent iteratively chooses image search, text search, or stop, under explicit tool-call budgets and with deduplication to avoid redundant retrieval. For training, we first use rejection-sampling SFT to learn valid tool-use formats, then optimize the agent with TN-GSPO, a sequence-level RL objective that normalizes updates by both generation length and tool-interaction depth. Experiments on E-VQA and InfoSeek show consistent gains over strong RAG and agent baselines, and improved retrieval and end-to-end accuracy. The code is available at this https URL.

---


### 62. [HumanMoveVQA: Can Video MLLMs reason about human movement in videos?](https://arxiv.org/abs/2606.27999)

**<font color=#1a73e8>作者：</font>** Pulkit Gera, Faegheh Sardari, Asmar Nadeem 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the rapid advance of Multimodal Large Language Models (MLLMs) in high-level video understanding, a fundamental bottleneck remains: these models collapse complex human motion into coarse semantic labels. Existing benchmarks mostly focus on scene-centric events or local joint articulations, failing to probe global human motion in space over time (trajectory and orientation changes). We introduce HumanMoveVQA, the first comprehensive benchmark designed to evaluate global trajectory and orientation reasoning from an exocentric perspective. Our benchmark utilizes a first-frame anchored world coordinate system, preserving translation and rotation relative to a fixed starting point. We propose a scalable, multi-stage pipeline that lifts 2D video observations into world-consistent 3D motion tracks to generate over 10K structured question-answer pairs across seven reasoning categories, including motion aggregation, sequential ordering, and trajectory-level inference. Our extensive evaluation reveals a critical capability gap in state-of-the-art proprietary models on deep human motion understanding. However, we demonstrate that this is a learnable problem; by fine-tuning an open-source baseline with our targeted, world-consistent supervision, we achieve a significant this http URL establishes a rigorous geometric foundation for developing next-generation, movement-aware video understanding models.

---


### 63. [Dialogue to Detection: A Multimodal Hybrid NLP Pipeline for Insurance Fraud Detection](https://arxiv.org/abs/2606.28002)

**<font color=#1a73e8>作者：</font>** Muhammad Shakeel Akram, Amal Htait, Abdul Hamid Sadka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Insurance fraud imposes substantial financial losses and operational inefficiencies, raising premiums and impacting trust among legitimate policyholders. Early detection at FNOL remains a persistent challenge. Existing approaches rely largely on private, text-only datasets, limiting progress on multimodal methods that integrate linguistic, behavioural, and speaker-based indicators. We introduce a synthetic multimodal framework that replicates FNOL conditions. It generates agent-customer dialogue transcripts and two-speaker audios, performs ASR and diarisation. Downstream modules combine NER, regex-based feature extraction, LLM-RAG retrieval, and speaker embeddings in a rule-based risk score to flag narrative reuse, structural inconsistencies, and cross-case voice repetition while balancing sensitivity and false positives. Dataset validation and component-level evaluations show stability and transfer potential, offering a reproducible baseline beyond text-only fraud detection.

---


### 64. [The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization](https://arxiv.org/abs/2606.28013)

**<font color=#1a73e8>作者：</font>** Chengxiao Dai, Zhaokun Yan, Zhanhui Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Headline type-correctness (TC\%) of LLM autoformalization has climbed from $\sim$53\% to $\sim$76\% in two years, yet this scalar conceals which errors each method resolves. We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF). On ProofNet\# and MiniF2F-test with DeepSeek V4-Pro across Vanilla, Lean-Retry, Sample-Filter, and Stratified Autoformalization (SAF): (1) the +34 to +36 TS gain across the three elab-feedback methods is $\sim$64\% type-stratum recovery, with SO flat on net (87.5\% of original semantic errors rescued, 8 newly created). (2) The TO-to-TS rate is 23/61 for each method (Wilson 95\% CI [26.6\%, 50.3\%]), and this stratum-level recovery rate predicts $\Delta$TS on held-out methods to within 2/186 and renders $\Delta$TC linear in the Vanilla elab-fail rate across six (model, dataset) cells ($R^2=0.96$). (3) The two judges disagree by 26 to 37 pp on elab-feedback outputs (vs. 7 pp on Vanilla), with 30 to 56\% of symbolic-judge false negatives traceable to elaborator-forced rewrites. The persistent residual reduces to two gold-formalization errors. TC\% gains should be credited by which cell moved, not by the scalar alone.

---


### 65. [A Tree-of-Thoughts Inspired Hybrid Approach for Legal Case Judgement Summarization using LLMs](https://arxiv.org/abs/2606.28044)

**<font color=#1a73e8>作者：</font>** Aniket Deroy, Kripabandhu Ghosh, Saptarshi Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent times, Large Language Models (LLMs) are increasingly being used for legal case judgement summarization. Most prior works have tried traditional extractive and abstractive summarization of case judgements. However, hybrid or extractive-abstractive techniques have not been explored much. In this work, we propose a novel tree-of-thoughts inspired extractive-abstractive summarization approach for legal judgement summarization. We conduct experiments using two popular LLMs, DeepSeek and LLama, and compare among extractive, abstractive and extractive-abstractive summarization. Our experiments show that the proposed extractive-abstractive prompt provides better summaries compared to other types of LLM prompts.

---


### 66. [AirGroundBench: Probing Spatial Intelligence in Multimodal Large Models under Heterogeneous Multi-View Embodied Collaboration](https://arxiv.org/abs/2606.28049)

**<font color=#1a73e8>作者：</font>** Haotian Li, Yida Wang, Leyuan Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, multimodal large language models (MLLMs) have shown strong potential for embodied intelligence, yet their ability to maintain geometrically consistent spatial understanding across heterogeneous views remains under-evaluated. Existing benchmarks largely focus on single-agent, single-view perception, leaving a gap in the systematic assessment of collaborative air-ground settings, where multi-scale observations are complementary but introduce scale mismatch, asymmetric occlusion, and reference-frame inconsistencies. We present AirGroundBench, a diagnostic benchmark for evaluating multi-view spatial intelligence in heterogeneous UAV-UGV collaboration. AirGroundBench is built from 11 high-fidelity simulated environments with 1,021 synchronized air-ground observation pairs, yielding approximately 62,000 dual-view, four-option single-choice visual question answering instances and 115 closed-loop vision-language navigation episodes. It covers 10 task types organized into four progressively demanding capability dimensions: spatial perception, cross-view alignment, spatial transformation and reasoning, and embodied decision-making. To support geometry-grounded evaluation and analysis, we provide structured spatial annotations, including cross-view object identities and metric 2D and 3D bounding boxes. Evaluations of 13 representative MLLMs under UAV-only, UGV-only, and dual-view input settings reveal consistent bottlenecks: models perform relatively well on spatial perception but struggle with cross-view alignment and transformation-intensive reasoning, and these deficits propagate to sequential decision-making in vision-language navigation. Although dual-view inputs provide measurable gains over single-view variants, a persistent gap from human performance remains, highlighting geometric consistency as a key limitation of current embodied MLLMs.

---


### 67. [Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA](https://arxiv.org/abs/2606.28050)

**<font color=#1a73e8>作者：</font>** Sambaran Bandyopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge and self-evaluation pipelines implicitly assume that evaluation is easier than generation. We test this in a controlled in-context QA setting where a context passage is the sole information source and each model judges the answer it generated, removing the parametric-knowledge confound of open-domain comparisons. Across four benchmarks (SQuAD 2.0, DROP, HotpotQA, MuSiQue) and two models, evaluation is not uniformly easier: generation accuracy exceeds self-evaluation on three of four, with multi-hop MuSiQue the exception. Attention analysis reveals why: evaluation attends to context 3--5x less than generation does and barely reads the candidate answer. LoRA fine-tuning confirms the asymmetry is not a training artifact: generation fine-tuning induces over-acceptance and evaluation fine-tuning degrades generation. These findings challenge core assumptions in self-evaluation pipelines.

---


### 68. [MultiHashFormer: Hash-based Generative Language Models](https://arxiv.org/abs/2606.28057)

**<font color=#1a73e8>作者：</font>** Huiyin Xue, Atsuki Yamaguchi, Nikolaos Aletras  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) represent tokens using embedding matrices that scale linearly with the vocabulary size. To constrain the parameter footprint, prior work proposes hashing many tokens into a single vector within encoder-only models. While this offers parameter efficiency, many-to-one collisions prevent its use in causal LMs. In this paper, we propose MultiHashFormer, a new framework that allows hash-based autoregression. Each token is represented as a unique hash signature, a short sequence of discrete hash IDs, generated by multiple independent hash functions. A Hash Encoder compresses this signature into a single latent vector for processing by a Transformer decoder. Then, a Hash Decoder generates the hash signature of the next token, which is then mapped back to text. We evaluate our approach at the 100M, 1B and 3B parameter scales, demonstrating that MultiHashFormer consistently outperforms standard Transformer LMs across multiple benchmarks. Furthermore, we show that our model handles multilingual vocabulary expansion with a constant parameter footprint without any modifications.

---


### 69. [ReScene: Structured Indoor Scene Reconstruction from Multi-View Captures](https://arxiv.org/abs/2606.28060)

**<font color=#1a73e8>作者：</font>** Haoran Xu, Lechao Zhang, Daoguo Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Constructing simulation-ready 3D scenes from multi-view captures is a key bottleneck for Embodied Artificial Intelligence, as downstream tasks require object-level structure, explicit inter-object relations, and physical plausibility. Existing approaches either rely on specialized capture hardware, suffer from single-view bias in object reconstruction, or yield layouts that are geometrically reasonable but physically inconsistent. We identify that the problem is not single-object reconstruction but cross-view relation fusion and physically plausible scene assembly. To address this challenge, we present ReScene, a framework that threads multi-view geometry throughout the pipeline as a unifying prior. Our method consists of two main components: HierView prioritizes reconstruction views based on semantic consistency and 3D coverage completeness, replacing the largest-mask heuristic that conflates image occupancy with object coverage; and Relation-Aware Assembly fuses multi-frame relation predictions from a vision-language model with geometric and room-shell priors into a confidence-weighted scene graph, enabling physically consistent scene assembly. ReScene sets a new state of the art across geometry, rendering, and perceptual quality on a set of ScanNet scenes, achieving a 17% reduction in Chamfer Distance and 26% in LPIPS over the strongest prior baseline, while running up to 10x faster than prior multi-view methods. Based on the reconstructed scenes, we also generate an embodied visual question answering dataset, on which fine-tuned Qwen-VL approaches the performance of strong closed-source models on several spatial reasoning tasks.

---


### 70. [JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications](https://arxiv.org/abs/2606.28070)

**<font color=#1a73e8>作者：</font>** Oxygen AIIC, Chan Long, Chao Liu 等 55 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> this http URL, one of the world's largest e-commerce platforms, serves over 700 million active users and millions of merchants, with a catalog of tens of billions of SKUs. At this scale, high-quality, structured item knowledge underpins a better consumer experience, lower management costs, and higher operational efficiency-yet producing and serving it poses three industrial-scale challenges: fast-emerging concepts, high-quality knowledge production for massive SKUs, and diverse downstream requirements. To address these challenges, we present the JD Oxygen AI Item Center (Oxygen AIIC), an industrial-scale platform built on LLMs/VLMs for item-knowledge production and service. Oxygen AIIC is built around four core pillars: (i) ontology engineering driven by efficient human-AI collaboration, which supports the dynamic evolution and agile expansion of an ontology with millions of entries; (ii) a "Semantic Search then Discrimination"(S2D) knowledge identification architecture that, combined with throughput improvement strategies, enables scalable, extensible, and high-throughput AI Item Library production for tens of billions of SKUs; (iii) self-evolving item-understanding LLMs/VLMs that improve in a stable and controllable manner, enabling knowledge production with 94.2% precision and 82.8% recall; and (iv) a unified item tunnel that serves as the data and service hub. Oxygen AIIC now covers tens of thousands of JD categories and processes hundreds of millions of item updates per day on Huawei Ascend NPUs. It has accumulated hundreds of billions of item-knowledge assets. Deployed across core business scenarios-including search, recommendation, operations, category planning-Oxygen AIIC has delivered measurable gains at scale. Search-traffic coverage reaches 80.4%, item-information quality issues drop by 37%, the automated fill rate of core attributes during item listing exceeds 80%.

---


### 71. [TextDS: Parameter-Efficient Representation Alignment for Scene Text Detection under Distribution Shifts](https://arxiv.org/abs/2606.28077)

**<font color=#1a73e8>作者：</font>** Boyuan Chen, Zichen Dang, Chuang Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world deployments, scene text detectors inevitably face distribution shifts beyond the training distribution. Prior work often depends on large-scale scene-text pretraining, yet evaluation under cross-domain changes and real-world imaging degradations remains limited. We propose TextDS, an efficient framework for scene text detection under distribution shifts. First, we propose a data-efficient dual-encoder design with visual foundation models, eliminating the reliance on large-scale scene-text pretraining. Second, we introduce Step-wise LoRA adaptation (SWLoRA), which performs progressive low-rank refinement with a dynamic early-exit mechanism for effective feature adaptation. Third, we propose Common Subspace Fusion (CSF) to align and fuse the two branches in a shared subspace while retaining complementary, shift-robust information. Finally, we construct adverse-condition scene text detection datasets to address the gap in evaluating under imaging degradation. Experiments show that TextDS achieves competitive performance in scene text detection, demonstrating robustness across domains and adverse imaging conditions with only 4.9M trainable parameters.

---


### 72. [Typing Behavior in Human-LLM Interaction: Keystroke Dynamics Reveal Cognitive Effort During Prompting](https://arxiv.org/abs/2606.28090)

**<font color=#1a73e8>作者：</font>** Laura Schütz, Yousri Cherif, Clara Sayffaerth 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) become increasingly integrated into daily routines, understanding how users interact with these systems is crucial for effective human-AI collaboration. This work investigates keystroke dynamics as a behavioral measure of user mental effort and perceived output usefulness in human-LLM interaction. We conducted a user study (N = 36) to examine how task difficulty (easy vs. hard) and device type (desktop vs. mobile) influence typing behavior and workload (NASA-TLX) during interactions. Our results indicate that hard tasks led to significantly more keystrokes, slower typing, increased pauses, and higher self-reported workload. Device type had weaker effects, with mobile use slightly reducing input length and typing speed. While keystrokes captured differences in cognitive effort, they did not predict perceived LLM output usefulness. These findings highlight the potential of keystroke dynamics as real-time indicators of cognitive effort during LLM prompting, while also showing their limitations in capturing perceived collaboration success.

---


### 73. [Cross-view Multimodal Vision-Based Assessment Framework for Traditional Chinese Medicine Rehabilitation Training](https://arxiv.org/abs/2606.28104)

**<font color=#1a73e8>作者：</font>** Francis Xiatian Zhang, Hao Yao, Shengxuan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based assessment can provide convenient and cost-effective evaluation in Traditional Chinese Medicine (TCM) rehabilitation training, where action quality assessment (AQA) from computer vision offers a promising solution. Existing automatic AQA frameworks for physical therapy typically rely on skeletal data captured from a single viewpoint, which is inefficient for TCM techniques such as acupuncture or Tuina that involve dense hand self-occlusion and complex hand-object interactions. To address these challenges, we propose CME-AQA, a cross-view, multimodal vision-based assessment framework that integrates visual-pose fusion to enhance understanding of environmental context and leverages both first-person and third-person videos during training to improve inference robustness. We collected two dual-view datasets, TCM-AQA61-A (Acupuncture) and TCM-AQA61-T (Tuina), each containing synchronized first-person and third-person recordings of 61 subjects with expert annotations. Experimental results show that our approach achieves superior or comparable mean performance against competitive baselines, achieving over 10% relative improvement in weighted F1 over the best competing method on key rating tasks such as Needle Depth and Quick Needle Insertion, while also reducing mean absolute error in quantitative measures such as insertion time and manipulation frequency. Testing on a CPR dataset further demonstrates comparable performance on several posture-based criteria, suggesting applicability to related structured simulated clinical skill assessments where participant motion is central to evaluation. Overall, CME-AQA enhances assessment accuracy for structured TCM rehabilitation training and facilitates more convenient and effective training-oriented skill evaluation.

---


### 74. [Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability](https://arxiv.org/abs/2606.28116)

**<font color=#1a73e8>作者：</font>** Ruixuan Huang, Yipei Wang, Wenyi Fang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier large language model training consumes massive accelerator fleets and long wall-clock computation, making stability failures costly when they occur. After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal. We study mechanism-driven detection of training instability by deriving internal monitors from the functional role of each critical module and from the earliest computational sites where failures are expected to produce measurable signatures. For low-precision flash attention, we monitor the spectral entropy of a QK bilinear decomposition, whose first-order term becomes abnormal before the loss fully collapses. For MoE routers, we derive indicators from their role in expert selection. Our fault-injection experiments on low-precision attention, large learning-rate, and combined faults show that these signals provide distinct signatures for different failures, triggering thousands of steps before loss divergence.

---


### 75. [When One Adapter Speaks for Many: Discovering Low-Rank Redundancy in Continual Fine-Tuning](https://arxiv.org/abs/2606.28117)

**<font color=#1a73e8>作者：</font>** Tanguy Dieudonné, Giulia Lanzillotta, Enis Simsar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) has become the standard tool for parameter-efficient fine-tuning of large pretrained models. When applied sequentially across tasks in Continual Learning (CL), the standard assumption is that each new task requires a dedicated low-rank adapter. In this work, we challenge this assumption empirically and structurally. We show that task-specific LoRA adapters in CL exhibit significant low-rank redundancy: the subspaces spanned by adapters trained on different tasks substantially overlap, and in many cases earlier adapters can faithfully represent later tasks. Building on this observation, we propose LiteLoRA, a plug-and-play gating mechanism that learns at train time whether to recruit a new adapter or reuse existing low-rank representations. Our method reduces the number of active adapters by 20-70% while matching or exceeding state-of-the-art performance on standard CL benchmarks, revealing that structural redundancy is pervasive and that selective learning is sufficient to achieve stability without sacrificing plasticity.

---


### 76. [From Tokens to States: LLMs as a Special Case of World Models and the Continuous Path Beyond](https://arxiv.org/abs/2606.28127)

**<font color=#1a73e8>作者：</font>** Paul Dubois  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The AI community has framed the relationship between large language models (LLMs) and world models as a dichotomy: LLMs predict tokens; world models simulate reality. Yann LeCun argues in 2022 that reaching general intelligence requires abandoning autoregressive token prediction in favour of latent-space architectures. This framing is unnecessarily binary. Two claims will be defended. First, LLMs are a degenerate special case of world models: the state space is the set of all token sequences, the only action is appending one token, and world models are therefore a strict generalisation of LLMs, not a replacement. Second, there is a natural continuous spectrum from NTP to JEPA, with multi-token prediction, future-summary prediction, and next-latent prediction as intermediate stations already populated by current research. Moving along this spectrum relaxes the LLM constraints one by one. It also progressively surrenders the two practical advantages that make LLMs trainable at scale: internet-scale self-supervised data, and a transformer architecture co-designed for discrete token prediction. Both are examined as open research questions: the data question (the cliff from self-supervised text to instrumented action-labelled environments) and the architecture question (whether the transformer generalises to continuous-state prediction, or whether a new primitive is needed).

---


### 77. [EchoSonar-R: A Multi-View Reasoning-Enabled Model for Disease Classification and Report Generation in Echocardiography](https://arxiv.org/abs/2606.28164)

**<font color=#1a73e8>作者：</font>** Darya Taratynova, Ahmed Aly, Numan Saeed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Echocardiography is the most widely used non-invasive cardiac imaging modality, providing essential information for cardiovascular diagnosis. Interpreting an echocardiogram requires synthesizing complementary evidence across multiple heart views to identify abnormalities and produce structured clinical reports. While recent efforts focus on improving classification performance, most models lack explicit diagnostic reasoning and spatially grounded anatomical evidence, limiting clinician trust. We present EchoSonar-R, a multi-view reasoning-enabled vision-language model that jointly performs multi-label disease classification and report generation from echocardiography studies. EchoSonar-R combines a spatiotemporal video encoder with a structure-aware cardiac detector that provides spatially grounded anatomical cues to improve interpretability and clinician trust during cross-view reasoning. EchoSonar-R is trained in two stages: supervised fine-tuning (SFT) on reasoning-annotated targets, followed by Group Relative Policy Optimization (GRPO) with task-specific rewards that jointly align classification and report generation within a unified reinforcement-learning framework. Across a private multi-view dataset and two public benchmarks, EchoSonar-R improves macro balanced accuracy by 17.1% on the private set and 6.1% on MIMICEchoQA over the strongest baseline, achieves a GREEN clinical faithfulness score of 0.800, and produces interpretable reasoning traces grounded in multi-view visual evidence.

---


### 78. [CPAgents: Agentic Composite Phenotype Generation for Cardiac Disease Association](https://arxiv.org/abs/2606.28179)

**<font color=#1a73e8>作者：</font>** Zuoou Li, Wenlong Zhao, Kelly Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying robust associations between cardiac imaging phenotypes and clinical diseases is fundamental to population-scale cardiovascular research and reliable risk stratification. However, current phenome-wide association studies rely on pre-defined, single-variable phenotypes or expert-crafted features, which limits their ability to capture clinically meaningful non-linear effects and cross-phenotype interactions. To address this, we propose CPAgents, an iterative phenotype-Composition framework for cardiovascular Phenome-wide association study (PheWAS) that automatically constructs and validates interpretable composite phenotypes (e.g., polynomial, ratio, and interaction forms) from base imaging features. Specifically, our system coordinates three agents: (i) an Analyst that identifies statistical pathologies and nominates candidate transformations; (ii) a Proposer that generates constrained, medically and statistically motivated expressions under numerical safety rules; and (iii) a Verifier that evaluates candidates using multi-stage criteria and produces transparent evidence trails for accepted phenotypes. Evaluated on a population-scale cardiac imaging cohort, the discovered composite phenotypes markedly improve disease discrimination: across 72 classifier-disease-metric combinations, our variants achieve the top rank in 56 cases versus 18 for baselines, with gains observed across all nine clinical disease categories. Our framework yields compact, clinically interpretable phenotype formulas with transparent evidence trails, enabling scalable discovery of stronger phenotype-disease associations beyond expert-driven feature selection.

---


### 79. [LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior](https://arxiv.org/abs/2606.28182)

**<font color=#1a73e8>作者：</font>** Qinhong Zhou, Chuang Gan, Anoop Cherian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Embodied agents operating in decentralized and partially observable environments have attracted growing attention in recent years. However, existing large language model (LLM)-based agents often exhibit behaviors that are misaligned with their partners or inconsistent with the environment state, leading to inefficient cooperation and poor task success. To address this challenge, we propose a novel framework, Learning Laws of Cooperation (LLawCo), that enables embodied agents to autonomously align with both their partners and task objectives. Our framework allows agents to reflect on past failures to extract misaligned behavioral patterns, which are used to derive high-level behavioral laws, such as "Talk when necessary" and "Wait for partner." These laws are explicitly incorporated into the agents' chains of thought via supervised fine-tuning, aligning their reasoning with task requirements and the behavior of other agents. To evaluate our approach, we introduce PARTNR-Dialog, a large-scale multi-agent communicative and cooperative planning benchmark built on the PARTNR environment. Experiments on existing tasks and our new benchmark demonstrate significant improvements in cooperative efficiency and task success rates. Across four backbone LLMs, our method achieves average success rate improvements of 4.5% on the PARTNR-Dialog benchmark and 6.8% on the TDW-MAT benchmark over state-of-the-art open-source communicative agent frameworks. See the LLawCo project page for details: this https URL

---


### 80. [Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction](https://arxiv.org/abs/2606.28186)

**<font color=#1a73e8>作者：</font>** Chenguang Wang, Ming Li, Xinyue Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Predicting human item difficulty is central to educational assessment, where reliable estimates support fairness and effective test construction. Existing methods often depend on costly human calibration or item-level textual representations, providing limited evidence about the cognitive processes that make items difficult. We argue that difficulty should be viewed not only as a property of item text, but also as an observable consequence of the problem-solving burden an item induces. Large Reasoning Models (LRMs) offer scalable process evidence through reasoning traces, but such evidence must be structured to support interpretable modeling. To this end, we introduce Epi2Diff (Episode to Difficulty), a framework that maps LRM reasoning traces into cognitively grounded episode sequences. These episodes group trace segments into functional problem-solving states, enabling difficulty to be modeled through reasoning scale, effort allocation, and state transitions. Epi2Diff extracts compact episode-dynamic features and combines them with semantic item representations for human difficulty prediction. Experiments on four real-world human difficulty datasets show that Epi2Diff consistently outperforms strong baselines, including fine-tuned small language models, LLM in-context learning, and supervised LLM adaptation. On SAT-derived classification benchmarks, Epi2Diff achieves an 8.1% average relative gain over supervised LLM fine-tuning baselines. Further analyses show that harder items induce more effortful, iterative, and implementation-centered episode dynamics, rather than merely longer responses. These results demonstrate that cognitive episodes in LRM reasoning traces provide a predictive and interpretable process representation for human item difficulty, offering a new lens for educational measurement with reasoning models.

---


### 81. [GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems](https://arxiv.org/abs/2606.28187)

**<font color=#1a73e8>作者：</font>** Xiaocheng Yang, Abdulrahman Alrabah, Dilek Hakkani-Tür 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) built on large language models (LLMs) provide a promising framework for solving complex tasks through role specialization and structured interaction. However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents. Existing approaches typically rely on coarse-grained feedback, making it difficult to identify which agents or interaction steps are responsible for errors. We propose Gradient-Based Connections (GBC), an approach for fine-grained attribution and optimization of multi-agent systems. GBC models a MAS as a computational graph and introduces gradient-based connection weights to quantify the influence of each agent's output on downstream agents at the token level. By constructing an attribution graph and propagating task-specific loss signals backward, our method enables precise identification of error sources and targeted prompt optimization. We further develop AgentChord, an efficient implementation that leverages prefix-based gradient computation. Experiments on MultiWOZ and {\tau}-bench show that GBC improves multi-agent performance and outperforms strong single-agent and multi-agent baselines, and higher attribution quality is associated with greater optimization effectiveness. Code is available at: this https URL.

---


### 82. [RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning](https://arxiv.org/abs/2606.28266)

**<font color=#1a73e8>作者：</font>** Yelin Wang, Zijia Song, Shuo Ye 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote Sensing Image Change Captioning (RSICC) aims to describe changes between bi-temporal remote sensing images and holds significant research and application value. However, most existing methods rely on conventional deep learning architectures, and the limited model capacity constrains performance. Although large-model post-training techniques have achieved great success in general domains, their direct transfer to RSICC remains challenging due to data scarcity and the need for fine-grained change understanding. To address this, we propose RSICCLLM, the first post-training framework for large vision-language models in RSICC. Specifically, we design a data generation paradigm, release the instruction dataset RSICI, and establish a task-specific RSICC benchmark. We further introduce Difference-aware Supervised Fine-tuning to explicitly extract change representations and guide the model in perceiving and understanding temporal differences. In addition, we propose Dual-Negative Preference Optimization (DNPO), which employs two complementary negative-sample construction strategies to construct the preference dataset RSICP and further refine model performance. Extensive experiments validate the superior capability of RSICCLLM, which achieves outstanding results with only 7B parameters, surpassing models of substantially larger scales. The code and dataset will be made publicly available at this https URL.

---


### 83. [Vision-Default, Prior-Override: Causal Mechanisms of Perception-Knowledge Conflict in Vision-Language Models](https://arxiv.org/abs/2606.28273)

**<font color=#1a73e8>作者：</font>** Niclas Lietzow, Danielle Bitterman, Carsten Eickhoff 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models must reconcile visual evidence with memorized world knowledge when the two conflict. How they resolve this conflict shapes the reliability of multimodal systems, yet prior work characterizes it behaviorally without a component-level causal account. We combine activation patching across three granularities (residual stream, attention heads, and MLP sublayers) with model-component ablation studies and mechanistic analysis. Across three VLM families, we find that visual grounding emerges by default, whereas prior grounding depends on a small set of causally necessary attention heads (2.5-4.8%) concentrated in the second half of the network. These heads enable answers from stored world knowledge (e.g., "red" for a strawberry) despite conflicting visual input. Ablating them flips predictions from knowledge-grounded to visually grounded answers in 68-96% of cases under prior-knowledge prompts, but changes only 0.8-7.5% of visually grounded predictions, establishing an asymmetric causal structure. The identified heads decompose into routing heads, which modulate information flow, and writing heads, which directly project answer tokens into the residual stream. This structure is consistent across model families and scales, revealing a sparse causal circuit underlying perception-knowledge conflict in VLMs.

---


### 84. [PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception](https://arxiv.org/abs/2606.28322)

**<font color=#1a73e8>作者：</font>** Yana Wei, Hongbo Peng, Yanlin Lai 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce PerceptionRubrics, a rubric-based evaluation framework that addresses the gap between saturated benchmark scores and real-world brittleness. Shifting evaluation from holistic semantic matching to rigorous atomic auditing, PerceptionRubrics pairs 1,038 information-dense images with over 12,000 instance-specific rubrics. These criteria are derived from golden captions constructed via a novel Circular Peer-Review consensus pipeline and then distilled into a dual-stream system of Must-Right (essential facts) and Easy-Wrong (fine-grained details) rubrics. Crucially, PerceptionRubrics implements a Gated Scoring mechanism: unlike linear averages, failure on mandatory visual facts triggers sharp binary penalties. Extensive evaluation yields critical insights: (1) The Reliability Gap: models often verify fragmented elements correctly yet fail strict conjunctive constraints, exposing brittleness in dense domains; (2) Open-Closed Stratification: contrary to reasoning trends, we reveal a persistent 8% perception deficit between open-source and proprietary frontiers; and (3) Human-Aligned Rigor: our gated metrics substantially out-align conventional benchmarks, validating that strict perceptual fidelity is the prerequisite for reliable generation.

---


> [!TIP]
> 当前位于：**51-84**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-84**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
