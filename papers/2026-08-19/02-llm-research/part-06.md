# 🧠 大模型相关研究 | 2026年08月19日

> 本类共 **358** 篇论文：已确认 **337** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-358](./part-08.md)

---

### 251. [QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents](https://arxiv.org/abs/2608.16168)

**<font color=#1a73e8>作者：</font>** Heng Wang, Yifei Li, Lingling Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly use external memory systems to support personalization by drawing on long and evolving interaction histories, in which user preferences may be distributed across time, change with context, and conflict with earlier evidence. However, existing systems face three limitations: fixed-turn, fixed-token, or session-based boundaries can mix unrelated dialogue or split an event from its causes, decisions, and outcomes; storing multiple pieces of user information from the same interaction as a single memory binds together items that serve different functions and should be independently retrievable; and treating the current task as a single top-$k$ retrieval query can return fragments that are individually relevant but fail to jointly capture preference evolution, temporal validity, and contextual applicability. We introduce \textsc{QUMem}, a structured memory framework for query-conditioned user-state inference. \textsc{QUMem} first segments interaction histories into variable-length episodes according to semantic continuity, then decomposes each episode into independently retrievable factual, preference, and transferable insight memories while preserving temporal positions and source evidence. At inference time, three sequential agents identify task-specific information needs, plan multi-query retrieval over the typed memory stores, and jointly infer a temporally and contextually valid user state for downstream response generation. \textsc{QUMem} achieves state-of-the-art performance on both PersonaMem and KnowU-Bench, demonstrating the effectiveness of query-conditioned user-state inference for long-term personalization.

---


### 252. [Measuring Obedience to Authority Across Large Language Models with the Milgram Paradigm](https://arxiv.org/abs/2608.16177)

**<font color=#1a73e8>作者：</font>** Hidayet Aksu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as agents that operate equipment, execute instructions, and act inside institutional hierarchies, raising a question social psychology answered for humans six decades ago: how far will an agent escalate a harmful action when a legitimate authority insists? We port Milgram's obedience paradigm to LLMs as a standardized, fully scripted, replicable probe: the model plays the Teacher, a deterministic harness plays Experimenter and Learner from paraphrased Milgram scripts (30 shock levels, 15-450 V; graded protests; the four standardized prods), and the outcome of a session is the breakoff voltage. Following the census methodology of single-token fingerprinting studies, we measure obedience profiles (empirical breakoff distributions over a battery of six conditions) for 42 models from 19 families. We find that (i) obedience is highly heterogeneous: baseline full-obedience rates span 0-100% (census mean 42.9%; human anchor 65%), with 5 models delivering the maximum shock in every session and 11 never doing so; (ii) profiles are model-specific and stable: split-half verification separates same-model from cross-model comparisons with AUC 0.885 (0.949 under an ordinal-aware distance); (iii) situational sensitivity is selective: peer defiance shifts obedience in the human direction, learner proximity only weakly, and removing the authority's physical presence (the strongest human lever) has no detectable effect; (iv) declaring the scenario fictional raises obedience (median +17.2 V), whereas moving the decision to a native tool call lowers it sharply (-53.0 V), as does a 1,024-token deliberation budget (-38.2 V); and (v) obedience profiles do not recover model lineage (leave-one-out family accuracy 8.3% vs. 3.7% chance): obedience identifies the checkpoint, not its ancestry, consistent with safety post-training overwriting lineage priors.

---


### 253. [MUSE: An Interactive Meta-Agent for Understanding and Steering LLM-powered Data Science Systems](https://arxiv.org/abs/2608.16181)

**<font color=#1a73e8>作者：</font>** Wei-Hao Chen, Weixi Tong, Yuan Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models have enabled a new class of agentic data science systems that allow users to complete complex data science workflows through natural language. Although these systems can significantly reduce manual effort, it remains difficult to diagnose their behavior and steer the reasoning process when failures or unexpected outputs occur. We present MUSE, an interactive meta-agent that enhances user understanding and control of agentic data science systems by (1) dynamically restructuring low-level execution traces into multiple semantic levels that support navigation from high-level overviews to low-level implementation details; (2) enabling users to reference specific workflow steps in context to ask grounded questions, provide feedback, and revise problematic steps without manually locating relevant execution history; and (3) supporting mixed-initiative steering by surfacing suspicious steps for inspection, scaffolding the repair process, and translating user repair intent into contextualized instructions for the underlying agent. In a between-subjects study (n = 15), MUSE improved task efficiency and increased users' confidence in understanding and steering agentic data science workflows.

---


### 254. [LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](https://arxiv.org/abs/2608.16185)

**<font color=#1a73e8>作者：</font>** Xingjun Wang, Gongsheng Li, Qi Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly answer questions over dynamic raw-document collections, where files may change before preprocessing, and relevant evidence (spans, sections, pages, or tables) is query-dependent. Existing retrieval-augmented approaches pre-materialize evidence via fixed chunking, embeddings, or persistent indexes: effective for lookup, yet costly, stale-prone, and committed to a granularity before the query is known.
We formulate in-context search as Budgeted Evidence Localization over a latent evidence space induced by dynamic raw documents and propose LENS (Latent Evidence Exploration and Search), an index-free framework. Instead of pre-materializing the evidence space, LENS maintains a query-conditioned belief over candidate units, iteratively selecting candidates via complementary lexical, local, and exploratory proposal policies, updating the belief via an LLM relevance oracle, and narrowing toward high-posterior regions under a controllable budget. Evidence is consolidated into compact, source-grounded regions of interest and compressed into self-organizing knowledge clusters reused across related queries.
On a controlled 500-question evaluation with matched corpus snapshots, LENS reaches 62.4% exact match and 84.8% evidence recall vs. 65.2% exact match but 50.4% evidence recall for a ReAct-style baseline. Across scales, LENS gives the strongest supporting-fact localization and answer grounding. On a fixed 150-question fullwiki subset over the raw Wikipedia dump with zero indexing, LENS and ReAct are nearly tied in official answer quality (43.3% vs. 42.7% EM), with LENS grounding more answers in retrieved evidence (84.0% vs. 70.7%). A no-retrieval Closed-Book reference highlights the contribution of model memory. LENS is query-ready after corpus changes, needs no preprocessing or persistent index, and preserves source-grounded evidence localization throughout.

---


### 255. [Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline](https://arxiv.org/abs/2608.16187)

**<font color=#1a73e8>作者：</font>** Mikhail Surikov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-assisted development tools generate vulnerable code at significant rates, yet few automated mechanisms exist to detect, enrich, fix, and verify security issues at development velocity, particularly ones that ground remediation in real-world threat context. This paper presents an automated security evaluation pipeline that generates Python code from LLMSecEval prompts, scans for vulnerabilities using CodeQL and Bandit in parallel with an independent Code Validator LLM, enriches the Code Validator findings with MITRE ATT&CK techniques, CWE Observed Examples, and Python best practice guidelines, generates fixes via the Code Generation LLM, and re-scans with CodeQL and Bandit to verify outcomes. Two pipeline configurations were evaluated: Pipeline 1 (P1), using enriched Code Validator findings only, and Pipeline 2 (P2), where it additionally receives the initial CodeQL and Bandit findings. Both configurations were run across four Claude models: Opus 4.8, Sonnet 4.6, Sonnet 5, and Haiku 4.5, producing 80 runs against 26 LLMSecEval prompts covering 9 CWE categories.
P1 reduced static analyzer findings across all four models, ranging from -9% (Opus 4.8) to -54% (Sonnet 5). P2 deepened these reductions further, ranging from -29% (Opus 4.8) to -69% (Haiku 4.5), with P2 outperforming P1 for every model. Verdict consistency averaged approximately 81% modal agreement across all configurations, with P2 marginally more stable than P1. Remediation introduced new vulnerabilities in 15-22% of cases: roughly 70% involved a single new finding, and P2 reduced churn for three of four models, with Sonnet 5 as the sole exception. Notably, the best Code Generation LLM (Opus 4.8) was not the best pipeline performer, as Sonnet 4.6 produced the lowest residual findings and highest pass rate after P2 remediation, suggesting that pipeline effectiveness and first-draft security are distinct properties.

---


### 256. [Artly: Exploring Digital Artists' Perceptions of AI-Generated Feedback](https://arxiv.org/abs/2608.16189)

**<font color=#1a73e8>作者：</font>** Ulvi Rajabli, Alexander Wiethoff, Zelun Tony Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent developments in generative AI have lowered barriers to image generation, but existing tools mostly optimize for efficiency, producing generic results and offering little support for artistic growth. We present Artly, an AI system that combines personalizable AI feedback with human-authored learning resources. In a between-subjects study with artists, we compared a mode without image generation features against one that allowed to generate variations of users' illustrations. Artly was perceived as helpful for learning and self-improvement, with the exception of the most proficient participants. Participants who used the image generation feature interacted slightly less with the AI feedback. They reported feeling more creative after using Artly than participants using the restricted mode, while reporting slightly lower scores on new ideas for their work. Overall, our findings underline the potential of our feedback approach for supporting artistic growth in a manner that is well received by artists.

---


### 257. [Beyond Asking: A Pipeline for Personalized Game Generation that Reads Players from Behavior](https://arxiv.org/abs/2608.16196)

**<font color=#1a73e8>作者：</font>** Yifan Lu, Xiaopeng Yuan, Haohan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized game generation requires inferring a player's abilities and behavioral style from how they play. Large language models have made this inference more attainable than ever: an LLM can read a raw gameplay transcript and produce a fluent, plausible profile of the player. Plausible, however, is not verified, and verification is precisely what the field lacks: latent traits are unobservable; questionnaires provide noisy proxies and become circular when self-reports are used to validate behavior-based inference; and behavior itself is ambiguous without context -- a player who never collects an item may not want it, or may never have had the chance. We address both problems. First, we construct a synthetic player population whose traits are ground truth by construction: each trait is an explicit bot parameter, accepted only after controlled manipulation produces consistent, trait-specific behavioral change. Unlike prior parameter-recovery work that inverts a known decision model, our benchmark evaluates policy-agnostic inference from behavioral transcripts alone. Second, we introduce an opportunity-aware decision-moment representation that disentangles preference from the chance to express it; ablating it selectively degrades opportunity-dependent traits. On this benchmark, few-shot LLM inference outperforms embedding- and rule-based baselines on most traits, though feature-based supervised regressors remain stronger overall. Finally, we close the loop: inferred profiles drive difficulty adaptation, evaluated against ground-truth references and mismatched-profile controls, and an exploratory human study examines whether these findings transfer to real players.

---


### 258. [Multi-Granularity Sentiment Integration for LLM-Based Multimodal Sentiment Analysis](https://arxiv.org/abs/2608.16201)

**<font color=#1a73e8>作者：</font>** Shanshan Lin, Yuesheng Wu, Chao Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal sentiment analysis (MSA) aims to predict sentiment polarity and intensity from heterogeneous inputs such as text, audio, and vision. While large language models (LLMs) offer strong semantic priors for MSA, effectively incorporating audio and visual signals effectively remains challenging. A key challenge is that audio and visual sentiment cues evolve over different temporal scales, yet many LLM-based methods compress these signals through shallow projection or coarse pooling before fusing them with text, which can weaken cross-modal alignment and erase fine-grained affective information. We propose MGSI, a multi-granularity sentiment integration framework for LLM-based MSA. MGSI first encodes audio and visual streams at short-, medium-, and long-range temporal scales, preserving both local variations and global affective trends. It then refines non-text features through text-guided alignment, and applies polarity- and intensity-aware enhancement to better handle ambiguous and near-neutral samples. The resulting multimodal representation is finally compressed into a small set of pseudo-tokens for efficient conditioning of a frozen LLM. Experiments on four public benchmarks show that MGSI substantially outperforms frozen-LLM baselines and remains competitive with strong multimodal methods. Further ablation and sensitivity analyses support the effectiveness of multi-granularity temporal modeling, text-guided refinement, and adaptive sentiment calibration.

---


### 259. [Competing at Every Price Point with Agentic Evolution over a Menu of LLMs](https://arxiv.org/abs/2608.16207)

**<font color=#1a73e8>作者：</font>** Andrew Borthwick  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Consider a firm that surveys its competition for a particular agentic task and seeks to offer superior accuracy at every competitor price point. A firm that Pareto-dominated its competitors would leave no rational customer a reason to buy elsewhere. This paper shows a path to this kind of capability via agentic evolution over a menu of LLMs, from training pools of at most 100 examples. Given a priced menu of nine LLM endpoints; brief documentation of the task, objective, and API; a simple seed agent; and an operator-chosen per-problem cost target - usually set at an incumbent's own price - RoboPhD, an evolutionary meta-agent, evolves complete agent programs that attack the public frontiers of two semantically dissimilar tasks point by point: DS-1000 (execution-checked code generation) and PaperFindingBench (LLM-judged scientific document retrieval). Our officially scored submissions hold every Pareto-frontier slot but one on the two tasks' leaderboards, including Pareto domination of both the top-scoring and the lowest-cost competing points.

---


### 260. [Conditional Evaluation of Language Models with Cheap Auxiliary Signals](https://arxiv.org/abs/2608.16210)

**<font color=#1a73e8>作者：</font>** Zhi Zhang, Lingfeng Lyu, Yue Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aggregate accuracy hides where models succeed and fail. Estimating conditional performance profiles from gold labels alone is expensive, while cheap auxiliary signals such as LLM-judge scores, pairwise comparisons, confidence scores, and judge-disagreement features can be collected for every benchmark item but are often biased or miscalibrated. We propose LACE (Local Augmented Control-Variate Evaluation), a semi-supervised estimator for conditional LLM evaluation. The key step is local centering: after subtracting the conditional mean of a cheap signal within the target profile region, any linear augmentation has zero conditional mean and therefore cannot change the estimand. The augmentation coefficient is used only for efficiency, and a local ridge control variate combines a gold-label residual mean from the labeled subset with a cheap-signal mean from the full item pool. We prove calibration-free identification, unbiasedness for grouped profiles, local oracle optimality within centered linear augmentations, and first-order adaptivity to the estimated coefficient. The resulting gain formula is governed by a population local $R^2$, which characterizes how the efficiency attainable from the cheap signals varies across profile values. We also derive corresponding estimators for direct paired model gaps and deployment-weighted scores. We empirically evaluate the primary performance-profile estimator on MATH-500, ScienceQA, MMLU, WinoGrande, HellaSwag, TruthfulQA, GSM8K, and ARC.

---


### 261. [BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics](https://arxiv.org/abs/2608.16211)

**<font color=#1a73e8>作者：</font>** Junqi Liu, Yufan He, Yexiao He 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents are beginning to automate complete workflows that produce code, reports, and research artifacts. Medical imaging workflows are multi-stage and data-sensitive, while expert trajectories remain scarce and difficult to share. Structured benchmarks can localize failures through stage-level rubrics, but standard post-training discards these diagnostics before the next training round. We present Benchmark-as-Teacher (BaT), a recursive self-improvement system for agent post-training. BaT contains two linked components: the asynchronous Stage Bank data pipeline and BiCuRL (Bilevel Curriculum Reinforcement Learning), its self-improving post-training method. Stage Bank synthesizes content-isolated training states outside the policy-update loop. BiCuRL uses a fixed held-out evaluation to select the next stage curriculum, verifies rollouts with task rubrics, updates the policy with GRPO, and returns the candidate checkpoint to evaluation. On AutoMedBench-Lite, BaT-4B and BaT-9B more than double the Overall scores of their Qwen Instruct baselines. BaT-9B Agent reaches 79.6 Overall, exceeding Claude Opus 4.6 with Claude Code at 77.5.

---


### 262. [Process-Constituted Intelligence: A Shared Criterion for Humans and Machines](https://arxiv.org/abs/2608.16213)

**<font color=#1a73e8>作者：</font>** Michael J. Richardson, Ayeh Alhasan, Cassandra Crone 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intelligence is constituted by \textit{process} (iterative activity through which output emerges), not in the output itself. Generative AI (GenAI) is trained on \textit{traces} (textual and visual residues of human cognitive processes), reproducing samples from a distribution of those traces. Its outputs resemble reasoning, problem-solving, and creativity, yet the activity that produces such outputs in humans remains largely absent. Current GenAI is, therefore, weakly equivalent to the cognition it imitates, matching outputs while process stays absent or opaque. The cognitive sciences have long distinguished between weak and strong equivalence. Here, we define \textit{strong} equivalence across seven process features, assessable against human and machine cognition. Our process-based account addresses a symmetric risk: GenAI tools that outsource a person's generative processes may leave critical capacities unbuilt. We specify design principles for GenAI that instantiate more process and preserve rather than erode human judgment and creativity, and outline process audits that make strong equivalence testable.

---


### 263. [STAIR: Semantic-Temporal Automaton for Interpretable Reasoning in Temporal Question Answering](https://arxiv.org/abs/2608.16224)

**<font color=#1a73e8>作者：</font>** Xinlong Dai, Jinchuan Zhang, Lei Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> By leveraging large-scale pretraining, LLMs can interpret diverse temporal expressions and question formulations without task-specific training. However, existing prompt-based neuro-symbolic systems continue to rely on LLMs for both semantic interpretation and exact temporal inference. Consequently, discrete decisions regarding intervals, time anchors, and ordered states remain vulnerable to probabilistic errors and difficult to verify. We present STAIR, a \textbf{S}emantic-\textbf{T}emporal \textbf{A}utomaton for \textbf{I}nterpretable \textbf{R}easoning. STAIR separates semantic interpretation from precise temporal inference: an answer-free LLM adapter maps complex question formulations to normalized temporal intents, while a deterministic temporal automaton with finite control and guarded transitions executes the corresponding policies over canonicalized evidence. Following a rule-first design, STAIR resolves standard questions without invoking an LLM and applies semantic adaptation only when the rule path fails to produce an executable intent. This approach reduces free-form reasoning, making temporal decisions verifiable and interpretable. Specifically, guarded execution supports precise point-time containment and before/after selection, while semantic adaptation handles non-exact intervals and time-anchored queries. Across the TimeQA-Easy, TimeQA-Hard, TempReason-L2, and TempReason-L3 datasets, STAIR consistently outperforms strong baselines in the TQA task using matched model settings, achieving average F1 improvements of 16.57\% and 3.10\% when utilizing the Qwen2.5-7B and GPT-4o-mini models, respectively. Furthermore, ablations and diagnostic analyses demonstrate that STAIR excels at handling both boundary-sensitive and order-sensitive queries, while its guarded execution and semantic adaptation ensure precise point-time reasoning and inexact intervals, respectively.

---


### 264. [GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model for Unified Scene Understanding, Editing, and Multi-Modal Generation](https://arxiv.org/abs/2608.16234)

**<font color=#1a73e8>作者：</font>** Tianchen Deng, Xuefeng Chen, Shuang Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving World Models (DWMs) have recently advanced rapidly with generative models, yet most existing methods mainly focus on conditional scene generation and lack explicit 3D scene understanding, language-grounded reasoning, and controllable 4D editing capabilities. Moreover, commonly used point cloud, occupancy, or BEV representations make it difficult to achieve fine-grained alignment between textual information and the underlying 3D scene structure. To address these limitations, we propose a foundation-feature Gaussian driving world model that unifies scene understanding, language-grounded reasoning, controllable 4D editing, and multi-modal generation within a single framework. Specifically, we introduce a foundation-feature Gaussian tokenizer that directly distills Qwen/SigLIP visual-language features into 3D Gaussian primitives, building a compact open-vocabulary Gaussian semantic field. We further design a geometry-aware Gaussian adapter that combines importance-aware hierarchical selection with text-conditioned Perceiver-style cross-attention to aggregate dense Gaussian primitives into compact world tokens. To improve representation compatibility, we introduce a KL-based Gaussian--image distribution alignment objective that aligns Gaussian world tokens with foundation image tokens. Based on the aligned Gaussian representation, our framework further supports instruction-controllable scene editing, including weather-conditioned generation and dynamic vehicle manipulation. Extensive experiments on broader driving benchmarks demonstrate that our method achieves state-of-the-art performance across scene understanding, visual grounding, planning-oriented reasoning, and controllable 4D generation tasks. We will release the code and datasets publicly on Github.

---


### 265. [CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills](https://arxiv.org/abs/2608.16246)

**<font color=#1a73e8>作者：</font>** Mingxiao Liu, Zhoumian Jiang, Jianan Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents tackling Long Horizon Tasks depend on marketplace skills that are certified one at a time: a scanner returns a safety verdict for each skill and declares the ecosystem safe if every package passes. We show that this assumption fails under skill composition. A skill may pass the per-skill scanner individually yet participate in a risky composition when an agent connects its outputs, capabilities, or side effects with those of other scanner-passing skills. This makes skill composition risk a path level property rather than a node level property, explaining why existing skill scanners that inspect individual packages achieve limited interception. To study this threat, we present CompoSkill, a framework that constructs skill composition attacks through a dual attacker system. The white-box attacker knows the victim's installed skill pool and directly injects explicit skill-id sequences; the black-box attacker knows only a role profile, downloads the top marketplace skills for that scenario, builds a Skill Composition Graph, and searches for high risk chains whose implicit lures never name skill identifiers. We further construct CompoSkill-Bench, a benchmark of 1,140 records built from long-horizon professional workflows across five threats and six scenarios on OpenClaw and Nanobot. CompoSkill achieves risk Chain Formation Rates (CFR) up to 83.3% in the white box setting and 80.6% in the black box setting, while existing skill scanners block only a limited fraction of the risky compositions. Finally, we observe a bridge-bonus-then-hop-decay pattern: a bridge skill can increase attack success, but Attack Success Rate (ASR) decreases once additional hops make the risk chain longer than three skills. These results expose a systematic gap in single skill certification for autonomous AI agents.

---


### 266. [SAUL: Sharpness-Aware Augmented-Lagrangian Unlearning](https://arxiv.org/abs/2608.16249)

**<font color=#1a73e8>作者：</font>** Jaewan Choi, Junyoung Yang, Sangdon Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning in Large Language Models (LLMs) faces a critical trade-off between erasing target knowledge and preserving general utility. We propose SAUL (Sharpness-Aware Augmented-Lagrangian Unlearning), which formulates unlearning as a constrained minimization problem following the principle of "forget enough, but no more than necessary." At its core, SAUL formulates forgetting as an explicit constraint with a prescribed satisfaction criterion, whereas prior unlearning methods typically specify the desired level of forgetting implicitly through optimization objectives. An augmented Lagrangian controller adaptively adjusts forget-side pressure according to constraint violation and can eventually deactivate the forget-side update as the prescribed criterion remains satisfied. Sharpness-aware updates on both retain and forget objectives, together with a dual-optimizer design that maintains role-separated states, further stabilize the resulting unlearning dynamics. We evaluate SAUL on the TOFU, WMDP, and MUSE benchmarks, demonstrating favorable forgetting-utility trade-offs over representative sharpness- and perturbation-based baselines under benchmark-specific forgetting criteria. Beyond the complete SAUL framework, we further show on TOFU that applying the augmented-Lagrangian controller as a drop-in modifier to representative baselines improves their post-forgetting utility, demonstrating the practical value of explicit forgetting control.

---


### 267. [Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection](https://arxiv.org/abs/2608.16259)

**<font color=#1a73e8>作者：</font>** Bowen Deng, Jiahui Zhan, Yikun Ji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid progress of image generation models calls for AI-generated image (AIGI) detectors that are not only accurate but also explainable and reliable. While MLLM-based detectors can provide natural language explanations, existing methods often generate speculative rationales: they rely on vague or hallucinated artifacts, miss subtle localized flaws from the latest generators, and fail to provide evidence that can be visually verified. We present Defake-o3, an explainable AIGI detector that moves from speculative rationales to verifiable evidence. It combines interactive visual search with verifier-guided evidence alignment: the model iteratively zooms into suspicious regions to inspect fine-grained details, while an Evidence Verifier, trained from human verification annotations, provides reinforcement learning rewards that favor grounded evidence and penalize baseless claims. To support this objective, we construct GroundFake, a dataset designed for grounded explainable detection, with localized bounding-box evidence, human verification based on visual grounding and artifact specificity, corrected reasoning trajectories, and valid/invalid evidence supervision. We further introduce FakeFrontier, an out-of-distribution benchmark built from real images and outputs of 10 recent generators, together with an MLLM-based protocol for evaluating evidence quality and persuasiveness. Experiments on GroundFake, FakeFrontier, and additional out-of-distribution benchmarks show that Defake-o3 improves both detection accuracy and explanation quality, producing more localized, verifiable, and persuasive evidence.

---


### 268. [Seeing Before Answering: Training-Free Visual Layer Profiling for Vision-Language Models](https://arxiv.org/abs/2608.16263)

**<font color=#1a73e8>作者：</font>** Ruchen Liu, Yi Yang, Yiming Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LLaVA-style Vision-Language Models (VLMs) pass visual tokens from a fixed late layer of the vision backbone, typically the penultimate one, to the language model. We first show that this hidden convention is fragile: across 2 VLMs and 7 image and video benchmarks, the default layer is sub-optimal in 13 of 14 model-task pairs, and the best layer shifts with both task and visual backbone. Finding that layer by exhaustive layer-wise inference is prohibitively expensive, and no better fixed default exists. We therefore ask whether layer usefulness can instead be predicted from representation geometry. We study matrix-based entropy, introduced for unimodal layer analysis, which we compute over sample-level visual embeddings as Visual Dataset Entropy (VDE); and Gromov-Wasserstein (GW) distance, introduced for encoder-level VLM model selection, which we repurpose as a layer-wise visual--language alignment signal. Transferring these to LLaVA-based models is not obvious a priori: the vision tower is frozen while the multimodal projector is trained, so we profile both sides of the projector. We find that VDE transfers, and GW does not. Computed from 100 unlabeled task samples without downstream inference, pre-projector VDE tracks layer-wise accuracy and its top-ranked layers cover the oracle best layer on every task for the SigLIP-based LLaVA-Video, while giving region-level guidance for the CLIP-based Video-LLaVA. Post-projector profiles show that the projector reshapes visual geometry but does not erase the performance-relevant trend, leaving $\mathrm{VDE}_{\mathrm{pre}}$ the stronger signal. GW instead flattens after projection and is best read as an alignment diagnostic rather than a selector. VDE thus offers an interpretable, training-free policy that narrows the visual-layer search to a handful of candidates for limited downstream verification.

---


### 269. [Domain-Agnostic Neural Topic Modeling with Contextual Token-Level Semantic Graph Representation](https://arxiv.org/abs/2608.16269)

**<font color=#1a73e8>作者：</font>** Seung-Won Seo, Won Ik Cho, Yongmin Yoo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in neural topic models with pre-trained language models (PLMs) have achieved strong performance by leveraging general-domain pre-training, yet their topic interpretability often degrades on specialized corpora. This limitation primarily stems from the geometry of the embedding space, where domain-specific terms unseen during pre-training collapse into an indistinguishable region, and neither domain-specific re-training, word-level graph enrichment, nor parameter-efficient fine-tuning can restructure this space without inheriting the capacity ceiling of the underlying encoder. Our key insight is that a learnable graph layer operating on token-level PLM embeddings can acquire corpus-specific semantic structure that the frozen encoder lacks, because token-level graphs preserve document-local context that word-level representations discard and joint optimization with the topic objective reshapes embedding geometry directly from target-domain evidence. We instantiate this insight as DARTopic, a domain-agnostic framework that constructs token-level semantic graphs from frozen PLM embeddings and jointly trains a GNN encoder with topic inference. Across three benchmarks spanning general, biomedical, and legal domains, DARTopic consistently outperforms strong baselines in topic coherence and document clus- tering without any encoder fine-tuning, while demonstrating robustness to PLM choice and favorable runtime efficiency over fine-tuning based alternatives.

---


### 270. [Foresight-England: Development of a National-Scale Generative AI Model of Electronic Health Records for Medical Event Prediction across the COVID-19 Pandemic](https://arxiv.org/abs/2608.16273)

**<font color=#1a73e8>作者：</font>** Simon Ellershaw, Christopher Tomlinson, Zeljko Kraljevic 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foresight-England (Foresight-E) is the first national-scale generative foundation model of electronic health records (EHRs), developed as a research pilot strictly for COVID-19 research. We evaluated its ability to model the direct and indirect effects of the pandemic. Trained from scratch entirely within the NHS England Secure Data Environment, Foresight-E is a 243-million-parameter transformer decoder. It was trained and evaluated on de-identified, longitudinal EHRs of approximately 61 million individuals, integrating primary/secondary care, death registrations, and COVID-19 data. Training and validation used a 90% subset (54.9 million) spanning November 2018 to December 2022; the remaining 10% (6.1 million) was held out for evaluation. Foresight-E models patient timelines autoregressively, predicting the next medical event given their prior history. At inference, it operates zero-shot, predicting any concept in its ~40,000-code vocabulary without task-specific training. Our tokenisation scheme retains the clinical granularity of ICD-10, OPCS-4, and SNOMED CT codes, jointly representing absolute and relative timing. We designed an evaluation framework for 30-day COVID-19 hospitalisation and mortality, including subgroup analyses by demographic factors and vaccination status. To assess generalisation to unseen future data and the pandemic's indirect effects, we tested the model on medical events from 2023 (beyond its training period), benchmarking against logistic regression and XGBoost. As detailed in the Project Status section, NHS England has paused access to data for the Foresight-E project, meaning quantitative results are currently unavailable. Instead, we share our strategy for tokenisation, architecture, training, inference, and evaluation as a methodological template and case study in the challenges of building population-scale EHR foundation models.

---


### 271. [PolyDebate: A Game-Orchestrated Multimodal System for Debate Skills Practice and Evaluation](https://arxiv.org/abs/2608.16276)

**<font color=#1a73e8>作者：</font>** Jianing Yin, Weng Pan Kuan, Xiaoyun Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Debate is a structured form of persuasive communication that trains argument construction, rebuttal, oral delivery, and audience awareness. These skills are valued in education, language learning, and professional communication. Recent AI debate systems and LLM-based judges have advanced argument generation and debate evaluation, but most remain text-centered and rarely support learners through a complete multimodal practice experience. We introduce PolyDebate, a game-orchestrated multimodal system for English debate practice and evaluation. PolyDebate guides learners through staged one-on-one (1v1) debates with an AI opponent, while skill cards, props, and coins make persuasive strategies explicit and turn practice into a game-like interaction. During each session, the system captures learner speech and visual delivery evidence, generates context-aware opponent responses, and produces rubric-informed stage-level and overall feedback. PolyDebate is available as both an immersive Unity 3D game version and a web platform version that share the same workflow and evaluation services. Four studies covering AI opponent quality, evaluation coverage, AI judge feedback, and user perception show that PolyDebate brings debate interaction, gamified scaffolding, multimodal assessment, and structured feedback together in a practical workflow for debate skills practice. The demonstration video is available at this https URL.

---


### 272. [TransAnyText: Translating Arbitrary Text in E-commerce Images via Structured Visual Generation](https://arxiv.org/abs/2608.16284)

**<font color=#1a73e8>作者：</font>** Xiaoan Liu, Lichen Ma, Zipeng Guo 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-border e-commerce image translation is essential for global retail, where product images, banners, and detail pages need to be produced in different languages. Existing methods struggle to achieve accurate translation, faithful visual identity preservation, and easy-to-edit outputs, simultaneously. To address these challenges, we introduce TransAnyText, a structured visual code framework that reformulates image text translation as generating renderable HTML patches from source images and target languages. Our framework decouples semantic generation from pixel rendering: a vision-language model (VLM) handles visual understanding, cross-lingual translation, and structured visual generation, while a diffusion model performs background inpainting and pixel-level refinement, followed by deterministic rendering to synthesize the final image. Based on this formulation, we develop a three-stage post-training framework, where supervised fine-tuning (SFT) establishes the image-to-code mapping, privilege-gap weighted self-distillation (PWSD) improves the learning of style and layout tokens, and reinforcement learning with verifiable rewards (RLVR) further optimizes task-level performance. We further introduce TransAnyDataset and TransAnyBench, a multilingual dataset and benchmark for e-commerce image translation. Extensive experiments demonstrate competitive performance against cascaded pipelines, open-source end-to-end models, and closed-source image editing systems, providing an effective, controllable, and editable solution for cross-border e-commerce image translation.

---


### 273. [Clause Encounters of the Third Kind: Can LLMs Replace Language Teachers?](https://arxiv.org/abs/2608.16286)

**<font color=#1a73e8>作者：</font>** Kristina Šekrst, Ana Kovačić  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While various organizations now actively encourage LLM use in classrooms, we still lack rigorous, systematic evaluations of how well these models actually perform the fundamental tasks of language pedagogy. This paper examines whether state-of-the-art LLMs can deliver the kind of corrective feedback and methodological explanations that language learners need. The study tests multiple large language models on their ability to identify, correct, and explain common learner mistakes in English, by systematically varying model parameters to investigate how these technical adjustments affect output quality, pedagogical clarity, and consistency, along with using retrieval-augmented generation to query methodological data. The evaluation employs automated metrics (GLEU, BERTScore) but also human expert judgments to capture dimensions that purely computational measures miss: linguistic nuance, cultural sensitivity, and instructional appropriateness. While models demonstrate impressive surface-level correction abilities, their explanations often lack the terminological and domain knowledge that effective language teaching requires, suggesting that current enthusiasm for AI-assisted language learning may be outpacing our understanding of these systems' actual pedagogical competence.

---


### 274. [Executable Code Knowledge: Code as a Native, Validation-Carrying Knowledge Representation for AI Coding Agents](https://arxiv.org/abs/2608.16295)

**<font color=#1a73e8>作者：</font>** Xueping Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI coding agents need more than relevant snippets: they need business semantics, validation evidence, relations, and assurance that their context is current. Existing systems usually infer or externalize this knowledge through retrieval, summaries, graphs, rules, or reverse specifications. We investigate a complementary representation in which selected code units directly carry agent-usable knowledge. We introduce Executable Code Knowledge (ECK) and define an Executable Code Knowledge Unit (ECKU) as a source-bound object combining stable identity, semantics, executable behavior, contracts, evidence, relations, provenance, validation state, and a query interface. Our Python prototype supports code-local authoring, manifest export, evidence execution, exact changed-line impact, freshness checking, and agent-facing projections. Across three real Python repositories and 26 controlled patch tasks, direct ECK provides executable test coverage for 11/11 evidence-bearing tasks and exact selectors for 9/11; hiding declared evidence reduces exact recovery to 1/11 (paired exact McNemar p=0.0078). ECK-derived rules recover 11/11 exact selectors, showing that rules are effective delivery artifacts while ECK supplies source binding, validation state, impact, and freshness. Exact changed-line impact matches independently authored labels on all 26 patches (12 unit links; precision, recall, and F1 all 1.000). AST-bounded fingerprints classify 50 positive changes and 17 unrelated same-file controls correctly, whereas static rules snapshots detect none of the 50 stale cases. Model-backed patch-review and cross-layer studies measure projection fidelity rather than independent impact discovery. These results support a hybrid architecture: retrieval for coverage, ECK for source and evidence governance, and projections for delivery.

---


### 275. [Deep Thought Alignment: Trajectory-Level Latent Distillation for Video Reasoning](https://arxiv.org/abs/2608.16316)

**<font color=#1a73e8>作者：</font>** Ao Shen, Yongheng Zhang, Yinghui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Multimodal Models (LMMs) for video reasoning have long been hindered by the high computational cost of processing vast amounts of visual information. This dilemma motivates the transfer of the reasoning capabilities of large models to smaller, more efficient ones. On-Policy Distillation (OPD) offers a promising solution by matching output-token distributions along student-generated trajectories. However, video reasoning often depends on evidence accumulated across multiple frames. In this context, output-level supervision only captures information expressed through token predictions and does not directly constrain the latent representations formed during reasoning. To address this limitation, we propose Latent-OPD, which augments OPD with trajectory-level latent distillation. Specifically, our method focuses on the position at the end of each trajectory, where hidden states effectively summarize the accumulated visual evidence and reasoning context. Furthermore, we introduce a progressive teacher-lookahead strategy, which aligns middle-to-late student layers with increasingly deeper teacher layers. Experiments on six video reasoning benchmarks show that Latent-OPD consistently outperforms output-only OPD. Notably, the improvements are particularly pronounced in scenarios with limited frames, long videos, or tasks requiring complex evidence aggregation. These results establish Latent-OPD as a highly effective approach to frame-efficient video reasoning.

---


### 276. [Step-Level On-Policy Distillation: Interpolating Between On-Policy Distillation and Supervised Fine-Tuning](https://arxiv.org/abs/2608.16333)

**<font color=#1a73e8>作者：</font>** Changhui Sun, Lanbo Liu, Hang Lei 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) aligns a student model with a teacher's logit distribution on student-generated trajectories. This approach has achieved strong empirical gains and can often surpass conventional off-policy distillation with substantially less data. However, standard token-level OPD can provide only fragmented corrections along an erroneous student trajectory and cannot unfold a complete and correct repair path. Motivated by this limitation, we propose \emph{Step-Level On-Policy Distillation} (SOPD), which combines the long-horizon correction of supervised fine-tuning (SFT) with the on-policy advantage of OPD to provide step-level supervision over complete student-generated trajectories. We show that, at different limits of step length, SOPD reduces to SFT or approximates OPD. Compared with SFT, the teacher responses in SOPD are conditioned on student trajectories and therefore align more closely with student-visited states; compared with OPD, SOPD provides longer-horizon corrections rather than fragmented token-level guidance. Across both reasoning and agent tasks, SOPD substantially outperforms conventional SFT and OPD. For example, on ALFWorld, SOPD improves the average success rate by 13.4 points over Vanilla OPD. We hope this work offers a new perspective for future research on distillation methods.

---


### 277. [IndicQE-APE: A Benchmark for Quality Estimation and Automatic Post-Editing for Indic Languages](https://arxiv.org/abs/2608.16344)

**<font color=#1a73e8>作者：</font>** Diptesh Kanojia, Archchana Sindhujan, Sourabh Deoghare 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Indic quality estimation (QE) and automatic post-editing (APE) data is spread across separate releases, so no single resource supports training and evaluation across tasks and language pairs on one footing. We consolidate the WMT 2020--2024 shared-task lineage with an extended English--Malayalam resource into \indicqe: $126{,}754$ instances over nine directional pairs, with up to four label types aligned on the same segment, a direct assessment, a human post-edit, word-level OK/BAD tags and an error explanation, and a test set stratified over four difficulty axes. On it, we benchmark six prompted LLMs and three COMET metrics on segment-level QE, and three systems on APE. Two of the axes are defined partly on the direct assessment and select a compressed slice of it, so each axis is compared against a control drawn from the same language pair with the same score distribution. Only one survives that control: segments whose holistic and token-level quality signals conflict are ranked worse than equally-scored segments of the same language, for all nine systems and all seven pairs that carry the axis. Annotator disagreement, which looks second-hardest without the control, has no effect with it. Few-shot prompting costs every model $\leq$ $3.4$B both correlation and output-format compliance. Within-language accuracy does not make scores comparable across pairs: of the three trained metrics, the one with the best within-language correlation loses most when the pairs are pooled. The benchmark and code will be released.

---


### 278. [Architecture-Dependent Causal Transfer of Activation States Across Large Language Models](https://arxiv.org/abs/2608.16347)

**<font color=#1a73e8>作者：</font>** Fernando Cardenas Piepereit  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Direct communication between AI systems relies on natural language as an intermediate layer, incurring encoding/decoding overhead, token cost, and latency. We ask whether internal activation states can instead be transferred causally between different large language model (LLM) architectures via a learned projection, evaluated at three levels: representational similarity, cross-model retrieval from projected states, and end-to-end causal transfer via activation injection during generation. Using four architecturally diverse open-weight models (Qwen2-0.5B, Phi-3-mini, Mistral-7B, FLAN-T5-base), we find that representational alignment in trained models exceeds a random-initialization null baseline and is best captured by a rank-based metric (mutual k-nearest-neighbour alignment), more robust to activation-magnitude outliers than centered kernel alignment (CKA) or Procrustes analysis. A learned projection network retrieves the correct target-model representation from a held-out set well above chance for the three causal decoder-only model pairs (45-50% top-1 accuracy vs. 5% chance) but at chance level for the encoder-based FLAN-T5. Injecting projected activations into a target model during generation produces a statistically significant, pre-registered causal effect on retrieval-based output similarity for only one of the three decoder-only pairs (Qwen2-0.5B to Phi-3-mini: 23.3% vs. 0.0% under negative control, p=0.047, FDR-corrected); the two pairs targeting Mistral-7B show no such effect despite comparable representational alignment at the hidden-state level. We interpret these results as evidence for causal transfer of the representational vehicle, not of meaning, and conclude that end-to-end activation-state transfer between LLMs, as currently implemented, is architecture-dependent rather than universal.

---


### 279. [AeroCopilotBench: A Two-Tier Benchmark for Evaluating LLM Agents as Aviation Copilots in an Interactive Virtual Cockpit Environment](https://arxiv.org/abs/2608.16349)

**<font color=#1a73e8>作者：</font>** Yuchen Yuan, Zhenghuang Wu, Yuangan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents may assist flight crews with complex decisions and task execution, but existing aviation evaluations centered on static knowledge do not support systematic testing of procedural execution and safety compliance in interactive environments. This paper presents the AeroCopilot Operational Environment (ACOE), a reproducible interactive virtual-cockpit test environment, and AeroCopilotBench, a two-tier aviation agent evaluation benchmark. Tier-1 evaluates aviation knowledge using 1,200 multiple-choice questions, while Tier-2 comprises 73 emergency and abnormal tasks derived from the manufacturers' Pilot's Operating Handbooks (POHs) and instantiated in ACOE. ACOE converts natural-language procedures into executable state transitions, final-state goal conditions, and hard safety constraints, enabling models to interpret cockpit state, diagnose faults, and operate aircraft systems through standardized tool interfaces. We establish a safety-gated evaluation framework in which a trajectory succeeds only when all task goals are achieved without violating any hard safety constraint, while safe goal progress and trajectory safety are measured separately. Across 12 models, the highest Tier-2 success rate is 72.6%, while static knowledge performance does not consistently translate into procedural execution. Analysis of 451 failed episodes from 3 representative models identifies recurring failures in procedural completeness, use of state feedback, and long-horizon execution management. These findings motivate state-aware agent orchestration, joint assessment of task completion and trajectory safety, and repeated regression testing. ACOE and AeroCopilotBench provide a reproducible foundation for testing knowledge application, interactive execution, and operational safety in aviation agents.

---


### 280. [HalluTracer: Hallucination Detection via Depth-Averaging Truth Signals](https://arxiv.org/abs/2608.16353)

**<font color=#1a73e8>作者：</font>** Zhihao Guo, Zonghan Wu, Huan Huo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Even well-aligned large language models confidently generate factually incorrect text, making hallucination a persistent reliability risk in high-stakes deployments. These models nonetheless carry linearly separable truthfulness signals in their internal representations. Existing white-box detectors, however, collapse this evidence to isolated components or a single depth, discarding discriminative information distributed across the full forward pass. We introduce HalluTracer, a detection framework that reads and aggregates truthfulness evidence across every layer of the forward pass before the model emits any answer token. A geometric analysis reveals that the per-layer signals are weakly correlated, so that simple depth averaging suppresses layer-specific noise and captures nearly all linearly accessible information. Across six open-source language models and five hallucination benchmarks, HalluTracer consistently outperforms matched white-box baselines, with gains ranging from one to fourteen points. Collectively, our work recasts hallucination detection from a layer-selection problem into a depth-aggregation problem governed by the geometric sparsity of the truthfulness signal.

---


### 281. [What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics](https://arxiv.org/abs/2608.16370)

**<font color=#1a73e8>作者：</font>** Shuyu Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Task completion is the standard metric for evaluating context compression, yet it is incomplete: compression can increase an agent's interaction cost by forcing it to reacquire dropped state while leaving completion statistically unchanged.
We introduce a controlled runtime measurement protocol for reacquisition cost in a bounded-horizon tool-using agent. The agent acts in a deterministic planning environment under a fixed 24-turn horizon. We vary compression severity, compare a dropping operator with a fact-preserving operator, restore dropped state through controlled oracle interventions, and decompose tool calls into retrieval and execution. We evaluate three models across two task regimes.
Retrieval calls increase in all six model-regime comparisons and account for almost all added interaction; five of six remain significant after Holm correction. At the prespecified 5x comparison point, completion changes are not significant in any cell. DeepSeek shows a significant completion drop only at 10x compression. GPT-5.5 is the clearest case: completion changes from 80% to 85% (p = 1.0) while retrieval increases from 21.0 to 63.9 calls (p = .002).
Retention interventions further separate state quantity, state type, and content validity. Random selection is comparable to an offline hindsight oracle, while replacing retained D-state with semantically irrelevant content increases retrieval by 57% (p < .001) without a significant completion change. In a second environment, ALFWorld, sliding compression produces no retrieval surge, showing that the reacquisition signature is environment-dependent rather than intrinsic to shortening context.
Overall, compression can impose hidden interaction costs when execution-relevant state becomes absent and must be reacquired, while completion alone may not expose those costs.

---


### 282. [Mint-Agent: Introducing Finance-Native Agentic Foundation Models](https://arxiv.org/abs/2608.16386)

**<font color=#1a73e8>作者：</font>** Mint-Agent Team, B. Zhang, Yaze Geng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial agents must do more than recall domain knowledge: they must be both reliable, executing precise operations over grounded evidence, and executive, sustaining long-horizon research whose conclusions remain auditable. We present Mint-Agent, a family of finance-native agentic models designed around these two scales of financial intelligence. Mint-Agent is built upon three pillars: data, harness, and algorithm. Our data engine constructs clean, specialized tasks for atomic financial capabilities and long-horizon agentic execution from real-world financial sources. MintHarness enables stable interaction with open-ended environments and maintains auditable evidence trails across extended research trajectories. Our training recipe combines SFT, critical-step OPD, and RLVR to develop separate financial reasoning and agentic execution experts, which are then unified through model merging and multi-teacher on-policy distillation into compact, general-purpose financial agents. This pipeline yields two flagship models, Mint-Cu (9B) and Mint-Ag (27B). Across professional financial benchmarks, our models demonstrate two defining strengths: (1) Reliability: Mint-Ag achieves 98.33% on RFC-Bench, surpassing GPT-5.6-Sol and Claude-Opus-4.8 by 3.66 and 3.00 points; and (2) Executability: Mint-Cu reaches 69.86% on FinSearchComp T2, outperforming Agents-A1-35B and Nex-N2-mini by 22.83 and 12.78 points, while Mint-Ag achieves 76.00% and 60.49% on FinanceAgentBench v1.1 and v2, respectively. These results establish a path toward trustworthy financial intelligence in which domain expertise, long-horizon execution, and auditable evidence are jointly engineered as a unified foundation for frontier agentic models.

---


### 283. [Ventor-QTest: Threat-Model-Driven Verification of Vendor-Hosted LLM APIs](https://arxiv.org/abs/2608.16391)

**<font color=#1a73e8>作者：</font>** Xiangfan Wu, Zonghao Ying, Huiyu Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models become increasingly widespread, third-party providers that deploy open-weight models have become an important part of the ecosystem. Auditing the quality of their inference APIs is therefore an open problem. We formalize hosted model routing as a stochastic process and propose \mbox{\textbf{Ventor-QTest}}, a composite black-box audit that requires no probability information from the target API. Its repeated-request component sends each frozen constrained context to the target multiple times, reconstructs a categorical output distribution from the returned text counts, and reports \emph{average fidelity loss} (AFL) as a null-bias-corrected, within-window mean coarsened-KL statistic. Its long-sequence component uses independent runs to report \emph{extreme fidelity loss} (EFL) through the empirical upper tail of a run-level reference-centered-surprisal statistic. Across three logprob-capable route conditions, AFL shows strong linear descriptive agreement with a logprob-derived coarsened-KL comparator. Across seven route snapshots, 20-run sequence probes reveal route-specific EFL variation. AFL and EFL have little detectable route-level association with GPQA-Diamond accuracy. In contrast, pronounced EFL coincides with a decline in Terminal-Bench pass rate as task exposure increases. This pattern may arise because correctness in long-horizon tasks is more sensitive to extreme fidelity loss. These results motivate reporting AFL and EFL jointly, particularly when auditing long-horizon agentic tasks. The open-source implementation is available at this https URL.

---


### 284. [Think Inside the Chunk: RegulaRAG for Regulation-Compliant Scenario Generation using LLMs: A Case Study of UN Regulation No. 152](https://arxiv.org/abs/2608.16394)

**<font color=#1a73e8>作者：</font>** Vahid Zolfaghari, Nenad Petrovic, AndrÉ Schamschurko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating regulation-compliant test scenarios is essential for validating safety-critical automotive systems, yet Large Language Models (LLMs) struggle to ground outputs in long, hierarchical standards. We present RegulaRAG, a Retrieval-Augmented Generation (RAG) pipeline that couples SmartChunking, reference-aware enrichment of paragraphs and tables via graph traversal, with Smart Retrieve & Rerank over these enriched units. To test our system, we evaluate on a manually curated dataset covering all scenarios in UN Regulation No. 152 (AEBS). Our study comprises: (i) a three-step progressive search that identifies near-optimal retrieval parameters without exhaustive grid search; (ii) head-to-head comparisons against five baseline RAG systems; and (iii) a robustness stress test that scales the source corpus with distractor content. Outputs are evaluated using a customized penalized scoring metric. Across all experiments, RegulaRAG achieves the highest average Meta-Score (82.99), outperforming the next-best system by 43% (NoRAG: 57.94), while operating at 14k-25k tokens per query versus up to 500k for graphcentric baselines. It maintains strong performance, remaining stable even as the number of regulatory sources grows, whereas competing RAG systems degrade sharply in both quality and robustness.

---


### 285. [A Policy Algebra for Trust-Preserving Agentic AI Execution](https://arxiv.org/abs/2608.16402)

**<font color=#1a73e8>作者：</font>** Bhaskar Tripathi, Anurag Kumar, Ramendra Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model-based agentic frameworks primarily optimize capability: whether an agent can reason, retrieve information, call tools, delegate work, and complete a goal. Enterprise execution requires a stronger property. A successful result is not reliable if it was produced through unauthorized data access, widened delegated authority, unapproved side effects, unrecoverable budget consumption, or incomplete evidence. This paper defines reliable capability as a path property: an agent is reliably capable only when it completes a task through action events that remain admissible under identity, profile, tool, data, memory, budget, artifact, approval, and audit constraints. We propose a policy algebra that defines the reliability envelope within which agent capability may be exercised. Security profiles and runtime obligations compose through joins, intersections, budget narrowing, approval inheritance, and evidence accumulation; the resulting composition is both trust-preserving and the least restrictive state satisfying all governing inputs. The algebra also propagates restrictions across multi-agent calls and introduces cost-aware artifact materialization, which redirects open-ended execution toward a recoverable outcome as budget exposure grows. The evaluation is interpreted as a reliability-capability trade-off rather than a capability benchmark: the policy-algebra runtime intervenes on 94.8% of policy-violating events while retaining an 86.9% task-completion rate, eliminates the observed profile-monotonicity and zero-artifact-exhaustion violations, and increases audit completeness to 98.6%. The method provides researchers and practitioners with formal correctness conditions, executable decision semantics, and trace evidence for building agents that are not only capable, but reliably capable.

---


### 286. [SoftModel: A Neural Model That Grows Its Own Topology -- Governed Structural Growth for Continual In-Service Learning](https://arxiv.org/abs/2608.16409)

**<font color=#1a73e8>作者：</font>** Zhoumin Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Today, a neural system is almost always used in two phases -- trained, then deployed -- and in that regime it freezes twice: training ends, and the topology itself was never a degree of freedom. We take the opposite premise as an axiom -- total plasticity: no part of a model, including its structure, is ever frozen -- and derive the governance a lifelong learner then requires. The design's target regime is continual, in-service learning: a long-lived model on a non-stationary stream, whose stability comes from governance rather than immobility and whose capacity follows demand. The result is a growable soft model: an algebra of structural operators (width, hierarchy, composition, input interface, grown cycles, attention heads), each exact at application, budgeted, and audited, with adoption decided solely by a held-out reality gate that treats parametric and structural change uniformly. A complete from-scratch system realizes the whole account; its factory surface is operated end-to-end by a production LLM. Two conclusions follow from the axiom by construction: stability under lifelong change becomes an audit property of the lifecycle, and structure that follows demand removes the silent cap a fixed topology places on later capability where the capacity floor binds. A third is measured: in the worlds where this was measured, the marginal value of new capacity was unobservable before adoption, so workable growth governance took its ex-post form. The same governance extends to evaluative signals, and the core method is evaluated on standard continual-learning benchmarks, where governed growth preserves the ability to keep learning along long task sequences. A pre-registered experimental program adjudicates the mechanism and value claims on the tested problems and reports its failures at full prominence; the map -- positive and negative -- is the contribution.

---


### 287. [TRACE-CASH: Trial-History-Conditioned Reinforcement Learning for Adaptive Configuration Exploration in Time-Series CASH](https://arxiv.org/abs/2608.16410)

**<font color=#1a73e8>作者：</font>** Yu-Han Huang, Yujia Wu, Vincent S. Tseng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Combined algorithm selection and hyperparameter optimization (CASH) searches a conditional space in which the selected model determines which hyperparameters are active. In time-series forecasting, temporal choices, chronological validation, and costly evaluations further complicate this search. Controlled comparisons of heterogeneous search methods under a shared time-series CASH (TS-CASH) evaluation protocol remain limited. Within this setting, we study TRACECASH, a task-local hybrid sequential optimizer combining grouped actor-critic candidate generation with fixed rules for model coverage, validation-guided exploitation, and exploration after stalled progress. A model actor proposes an initial forecasting model; three model-conditioned actors generate temporal, architectural, and training actions; and a modelspecific decoder constructs the configuration ultimately evaluated. We compare TRACE-CASH with six alternatives spanning random, Bayesian, evolutionary, multi-objective, and language-model-assisted search across 41 dataset-frequency task variants. TRACE-CASH has the lowest mean rank on both MASE and WQL. Descriptively, it also has the lowest window-averaged test-MASE rank in the predefined full and late windows. These results support the complete TRACECASH procedure as competitive among the evaluated methods.

---


### 288. [Evolving Executable Pipeline Programs for AutoML with Language Models](https://arxiv.org/abs/2608.16416)

**<font color=#1a73e8>作者：</font>** Sofoklis Kitharidis, Cor J. Veenman, Jan N. van Rijn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated machine learning (AutoML) systems search for pipelines within a space of preprocessing operators, learners, and hyper-parameters specified in advance: they can select and tune known components, but cannot produce structure outside that space. We present LACE, an AutoML framework that instead searches over complete executable pipeline programs: an evolutionary loop maintains a population of scikit-learn-compatible Python classes, and a large language model acts as the variation operator. To our knowledge, LACE is the first to formulate general tabular pipeline AutoML this way, evaluated on standardized OpenML tasks under a leakage-controlled protocol that withholds dataset identity from the generator. Because every candidate is ordinary Python, the returned pipeline and the search that produced it can be inspected and edited directly, rather than only through a framework's model objects. On 68 OpenML classification tasks, LACE with GPT-5.4-mini significantly outperforms auto-sklearn, H2O, and a fixed XGBoost baseline, with no detectable difference against AutoGluon, the strongest search-based system evaluated, while covering the full benchmark. Newer tabular foundation models are more accurate on the subset of tasks they support, but apply a fixed pretrained predictor rather than returning an editable task-specific program. LACE's contribution is therefore not raw accuracy but a search space defined by code: complete coverage, pipelines practitioners can reuse directly, and a component set extended by editing the prompt rather than the framework.

---


### 289. [D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding](https://arxiv.org/abs/2608.16417)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Longrong Yang, Lunhao Duan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-modal retrieval-augmented generation (RAG) is a key technique for visually rich long document understanding. Existing multi-modal RAG methods are progressively advancing toward multi-agent systems: they first retrieve relevant pages based on a query, and then iteratively understand information within those pages. However, these methods typically rely on fixed workflows and lack the ability to dynamically scale computation at test time, often leading to insufficient evidence. To address this, we propose D2-ScaleAgent, an agentic framework that introduces a dual-dimensional scaling paradigm for retrieval and reasoning. The core of D2-ScaleAgent is a Verifier agent-driven dynamic routing loop based on the intrinsic difficulty of the query, centered around a continuously updated evidence bank that serves as the agent's dynamic working memory: when retrieval needs to be expanded, the agent routes outward (retrieval scaling), decomposing the query into attributes and performing parallel page retrieval, followed by adaptive pruning to ensure comprehensive evidence coverage. When fine-grained reasoning is required, the agent routes inward (reasoning scaling), dynamically selecting sub-agents with varying granularity and count to extract evidence from pages. Finally, D2-ScaleAgent achieves logical closure over the evidence chain. Extensive experiments demonstrate that D2-ScaleAgent is effective on long and visually rich document benchmarks like MMLongBench-Doc, LongDocURL, etc.

---


### 290. [PertMind: Eliciting Emergent Biological Reasoning in LLM via Reinforcement Learning on Cellular Perturbation Data](https://arxiv.org/abs/2608.16419)

**<font color=#1a73e8>作者：</font>** Zhenchao Tang, Xiaogang Xu, Tianxu Lv 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can describe mechanisms, yet scalable post-training still depends on costly, manually curated biological reasoning traces. Here we show that cellular perturbation atlases can instead become reinforcement-learning environments, where measured gene responses provide computable rewards for biological reasoning. We introduce PertMind, which combines trusted-trajectory supervised initialization with gene-, pathway-, and format-level reinforcement signals. Trained only on forward perturbation-response prediction, PertMind improved response inference in unseen cellular contexts while retaining general language capabilities. It also transferred without task-specific post-training to reverse perturbation identification, double-perturbation reasoning, phenotypic-screen prioritization, and biological-process interpretation. PertMind further generated biological profiles that supported competitive gene, cell, and donor representations across multiscale downstream tasks. These results support the hypothesis that reinforcement on experimental endpoints can concentrate reusable biological strategies already accessible to pretrained models. More broadly, perturbation-derived reinforcement learning offers a scalable route for transforming expanding experimental atlases into training environments for general-purpose biological reasoning.

---


### 291. [Proving the Utility of Large Language Models in Cybersecurity Simulations: A Comprehensive Examination](https://arxiv.org/abs/2608.16422)

**<font color=#1a73e8>作者：</font>** Stylianos Kampakis, Fabio Rovai, Marcos Charalambides 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber threats continue to escalate in both frequency and sophistication, necessitating more adaptive and scalable defense strategies. This paper explores how Large Language Models (LLMs) can bolster cybersecurity simulations by automating the creation of synthetic environments and identifying latent vulnerabilities. We employ YAML as a structured representation format for simulating complex network configurations, thereby enabling Large Language Model-driven pipelines to support and improve reinforcement learning (RL) agent training. Comparative studies examine the advantages of LLM-based techniques over classical approaches such as Double Q-learning with Prioritized Experience Replay (PER), emphasizing increased efficiency, higher adaptability, and enhanced realism in cyberattack simulations. In empirical benchmarks across multiple synthetic topologies, LLM-instantiated Python agents achieved up to a 94.5% compromise rate while executing in 0.02-0.06 seconds per assessment---a ~25,000x to 50,000x speedup over traditional RL training cycles. Our findings underscore the transformative potential of integrating LLMs into cybersecurity research, ultimately paving the way for more intelligent and robust cyber-defense systems.

---


### 292. [Localized TabICLv2: Scaling Tabular In-Context Learning through k-NN](https://arxiv.org/abs/2608.16429)

**<font color=#1a73e8>作者：</font>** Beimnet Bekele Guta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundational models for tabular data have made significant progress in recent years, with TabICLv2 reporting state-of-the-art performance on several tabular classification tasks. However, full-context tabular ICL still suffers from attention cost that grows with the training-context size, which limits its ability to handle large datasets efficiently. Localized TabICLv2 introduces a method that reduces the inference cost of TabICLv2 by retrieving only the k nearest training neighbours for each test point, measured by similarity in the model's Stage 2 row-representation space, rather than using the full training context. This requires no architectural changes, and we show that accuracy retention can be improved through additional Stage 2 and Stage 3 fine-tuning. On TabArena classification tasks, the fine-tuned localized model retains 98.64% of Full TabICLv2 accuracy and it achieves a median 2.18$\times$ speedup in batch inference, and reaches approximately 249$\times$ median speedup in the single-query serving setting.

---


### 293. [The Value of a Prompt: An LLM-Relative Kolmogorov-Complexity Approach](https://arxiv.org/abs/2608.16438)

**<font color=#1a73e8>作者：</font>** Rafael Pass  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In a world where valuable artifacts are increasingly created, completed, or processed by LLMs, the central economic question is not only what the LLM can produce, but what \emph{value} remains in the inputs (i.e., the prompts) we provide to it. Given a prompt, hint, critique, problem statement, or partial solution that helps an LLM produce an artifact $z$---a proof, program, design, or scientific hypothesis---how should we measure the value of that input?
Intuitively, an input is valuable when it makes the target artifact easier for the model to generate: either by increasing its sampling probability, or by reducing the thinking time needed to find it. We propose a computational Levin--Kolmogorov complexity approach to this problem, by appropriately replacing the universal Turing machine in the classical definitions by the LLM itself. Concretely, we introduce an LLM-relative notion of \emph{probabilistic Levin--Kolmogorov complexity} $pKt$---treating the model's thinking as the random tape of the program, and charging logarithmically for it in Levin's manner---and define prompt value as algorithmic mutual information with respect to $pKt$. This captures the intuition above: a prompt having $b$ bits of value for an artifact $z$ makes $z$ $2^b$ times ``easier to obtain'', by multiplying the success probability by $2^b$, by dividing the required computation by $2^b$, or by any corresponding tradeoff between probability and computation.
In contrast to the classical notion of algorithmic mutual information, ours is efficiently estimable. We additionally show that, under a natural reproduction experiment, a prompt value of \(b\) bits means that reproducing \(z\) without the prompt has median token cost \(2^b\) times that of reproducing it with the prompt.

---


### 294. [HaReCAP: Habitual-action Grounding for Recursive Large Language Model Agents](https://arxiv.org/abs/2608.16447)

**<font color=#1a73e8>作者：</font>** Shen Liu, Zhenguo Xu, Shaopu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon embodied tasks require LLM agents to iteratively decompose high-level goals, revise plans in response to environmental feedback, and ground leaf-level subgoals into valid executable actions. Recursive context-management methods such as ReCAP improve planning stability through multi-level task decomposition and parent-node refinement, but still repeatedly invoke the LLM at leaf nodes to ground atomic subtasks into exact valid actions. We refer to this final grounding step as last-mile grounding redundancy, which accumulates into substantial LLM-call and token overhead during long-horizon execution. To mitigate this issue, we propose HaReCAP (Habitual-action Grounded ReCAP), a low-intrusion leaf grounding extension for ReCAP. HaReCAP extracts frequent leaf decisions from successful trajectories and compiles them offline into auditable and abstainable one-step leaf-reflex rules. At runtime, it skips the leaf LLM call only when a rule can uniquely determine a legal action in the current valid-action set; otherwise, it falls back to the original ReCAP. This design avoids repeatedly carrying the full recursive context into the LLM for routine leaf action grounding, while preserving the original recursive control flow. We evaluate HaReCAP on Robotouille and ALFWorld with Qwen3.5-27B as the main model. On tasks solved by both ReCAP and HaReCAP, HaReCAP reduces token consumption by 14.67%, 17.93%, and 20.08% on Robotouille synchronous, Robotouille asynchronous, and ALFWorld, respectively. The results show that HaReCAP can serve as a low-intrusion extension to ReCAP-style recursive context-management frameworks, reducing last-mile grounding redundancy across environments and models on commonly successful trajectories.

---


### 295. [Computational KJ-Ho: An Analyst-Bias-Free Insight Extraction Framework from Large-Scale Qualitative Data Using Domain-Specialized LLMs](https://arxiv.org/abs/2608.16467)

**<font color=#1a73e8>作者：</font>** Kasumi Ban  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The qualitative research methodologies that underpin consumer-insight generation - the KJ method, Grounded Theory, and Thematic Analysis - share a structural constraint: the cognitive processing capacity of the human analyst. Replication research further shows that conclusions vary substantially across analysts analyzing identical data (analyst bias). This paper proposes Computational KJ-Ho (the Kawakita Jiro method), a theoretical framework that computationally realizes the KJ method's epistemology - letting structure emerge from the data itself without imposing the analyst's preconceptions - an orientation we term "analyst-bias-free." The framework employs a domain-specialized LLM built through continued pre-training (CPT) on a marketing-research corpus and supervised fine-tuning (SFT) on expert-curated insight pairs, organized as a three-layer architecture: data structuring, insight extraction, and strategy generation. Two preliminary studies in the Japanese marketing context support the necessity of CPT-based domain specialization. The paper makes five contributions: (1) a theoretical integration of the KJ method, Grounded Theory, and Peircean abduction into a single epistemological commitment of data-driven explanation generation; (2) a three-layer architecture leveraging domain-specialized embeddings for cross-interview analysis; (3) two novel evaluation metrics, InsightExtraction-F1 and MarketingQA; (4) explicit engagement with the WEIRD problem, centering a non-Western methodology; and (5) five practice-derived problem formulations from nearly three decades of marketing-research practice, translated into design requirements. The human analyst retains a supervisory role. This is a concept paper presented ahead of empirical validation.

---


### 296. [Pallas: A Proactive KV Cache Migration Framework for LLM Inference in AI-RAN](https://arxiv.org/abs/2608.16477)

**<font color=#1a73e8>作者：</font>** Tianhang Ding, Jianchun Liu, Hongli Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-RAN brings large language model (LLM) serving close to mobile users, but cellular handover can separate an active request from its inference state: the user attaches to a target base station (gNB) while the large and growing key-value (KV) cache remains at the source. Retaining inference at the source preserves service continuity but persistently increases inter-token latency (ITL), whereas recovering the state at the target restores serving locality but requires KV-cache transfer, recomputation, or a combination of both only after handover, directly prolonging service interruption time (SIT).
This work presents Pallas, a \textit{proactive} KV-cache migration framework that prepares the inference state at the predicted target before handover, in parallel with ongoing source-side inference and token delivery. At the preparation trigger, Pallas partitions the token sequence into a stable historical prefix and an evolving suffix. The target reconstructs the prefix through local prefill, while the source streams the KV blocks generated for the suffix. At handover, the target assembles both portions into an up-to-date KV cache and resumes decoding locally, leaving only unfinished preparation to contribute to SIT. An online scheduler selects the \textit{prefetching window}, which determines how early preparation begins before handover, based on mobility predictions and runtime telemetry. Across three LLMs and $100$--$500~\mathrm{Mbps}$ inter-gNB links, our vLLM-based prototype reduces average SIT by factors of $2.28$--$89.68$ over target-side recovery approaches and lowers average ITL by $16.0\%$--$50.0\%$ compared with source-side forwarding.

---


### 297. [RISE: Roadside Infrastructure Sequence Understanding across 3D Tracking and Structured Vision-Language Reasoning](https://arxiv.org/abs/2608.16480)

**<font color=#1a73e8>作者：</font>** Yanbo Jiang, Haotian Zheng, Jiahao Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present RISE (Roadside Infrastructure Sequence Understanding and Evaluation), a framework spanning metric 3D tracking and structured vision-language reasoning in roadside sequences. For metric tracking, our image-only method combines SAM3 video identities with calibration-guided mask agreement for multi-view identity association, recovering persistent 3D tracks without LiDAR or task-specific 3D training. Its calibration-conditioned geometry allows the procedure to be instantiated at different calibrated multi-camera intersections without layout-specific retraining. On 20 human-reviewed clips from six intersections, the generated tracks achieve 66.9 MOTA within the defined multi-view evaluation scope. For structured vision-language reasoning, a human-reviewed MLLM pipeline mines high-value clips and uses a constrained full-context Oracle to construct bbox-grounded predictive QA without exposing future evidence to evaluated models. The resulting RISE-VQA dataset contains 33,910 QA pairs from 557 clips across 16 intersections and 61 roadside views. Its intersection-held-out RISE-Bench evaluates semantic choices, coordinates, future boxes, and interaction sets with deterministic task-specific metrics. Experiments show consistent benefits from domain adaptation and generally from temporal context, while revealing persistent challenges in spatial grounding, future localization, and interaction reasoning.

---


### 298. [Remote-Sensing City Layout Extraction with MLLM](https://arxiv.org/abs/2608.16484)

**<font color=#1a73e8>作者：</font>** Zigan Zhou, Kai Li, Yupeng Deng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote-sensing systems usually describe urban content with detection boxes, semantic masks, or vector boundaries. Such outputs locate classes and support image-plane scoring, yet they do not by themselves constitute an executable layout that retains object identities, typed relations, topology, and regeneration rules. Code-as-City instead casts urban-layout extraction from a single top-down image as constrained code generation with a multimodal large language model (MLLM). An image model first produces an aligned five-class semantic layout prior. Three ordered MLLM passes use the image and this prior to recover roads, land-cover regions and relations, and buildings. Deterministic normalization converts the accumulated records into a city graph and a restricted layout program. Executing the program creates a renderable 3D city layout and an orthographic semantic projection over shared geometry. The projection admits pixel-level comparison with remote-sensing masks, while named objects, relations, and editing operations remain available for synchronized regeneration of both views. Evaluated on the 100 scenes of CityLayout-100, the complete framework obtains 41.1% mean intersection-over-union and 48.3% global intersection-over-union. This result provides quantitative evidence that visual observations can be translated into inspectable, editable city code with coupled planar and 3D outputs.

---


### 299. [Large language models as synthetic clinical experts to inform longitudinal rare-disease modeling](https://arxiv.org/abs/2608.16507)

**<font color=#1a73e8>作者：</font>** Clemens Schächter, Astrid Pechmann, Janbernd Kirschner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Due to the limited amount of information, modeling longitudinal rare-disease data can benefit from integrating clinical knowledge. Yet, elicitation of expert knowledge and formalization for model fitting is challenging, in particular due to limited time of clinical experts. To nevertheless make domain knowledge accessible during model fitting, we use large language models (LLMs) as synthetic clinical experts to supervise a variational-autoencoder-based approach that learns low-dimensional latent summaries of visit-level observations. Specifically, LLMs are queried offline on textual descriptions of patient observations to obtain judgments, e.g., the suspected clinical category. To improve the variational autoencoder fit, we train a differentiable surrogate model on these judgments and augment the loss function to encourage reconstructions that preserve the clinical-label distribution of their corresponding input profile. In an application to longitudinal motor-function assessments from children with spinal muscular atrophy, we map visit-level clinical profiles to low-dimensional representations that are linked by a multivariate mixed-effects model. The synthetic expert loss discourages reconstructions that remain numerically close in data space but alter the clinical interpretation of the reconstructed motor function profile, such as by crossing a disease-type boundary. We thus reduced disagreement between original and reconstructed SMA type labels from about 11 to 7 percent. Furthermore, informing the latent representation by the synthetic expert improved prediction of motor function milestones compared with unsupervised latent representations and a data-level baseline. These results suggest that incorporating LLMs into model fitting can make clinical knowledge available to representation learning and improve clinical faithfulness for longitudinal rare-disease data.

---


### 300. [LLMs for Zero-Shot Threat Detection via Structured Risk Indicators](https://arxiv.org/abs/2608.16508)

**<font color=#1a73e8>作者：</font>** Abdullah Alghamdi, Siamak Layeghy, Marius Portmann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose a two-stage large language model (LLM) framework for zero-shot detection of insider threats and advanced persistent threats (APTs) from heterogeneous security logs. The framework models user activity as chronological timelines and incorporates retrieval-augmented generation (RAG) to provide personalised behavioural context from each user's historical activity. Rather than performing end-to-end classification directly from raw logs, it first generates structured, interpretable sets of threat-specific risk indicators, which are then classified jointly across temporal sequences to capture attack patterns spanning multiple this http URL framework is evaluated on two benchmark datasets, CERT r5.2 for insider threat detection and PicoDomain for APT detection, using four combinations of two open-weight LLMs under both retrieval and non-retrieval settings. All configurations outperform the previous state-of-the-art LLM-based framework (GABM), with the best configuration improving the F1-score by 11.40 percentage points on CERT r5.2 and 31.50 percentage points on PicoDomain. Results further show that retrieval mainly benefits weaker LLMs by generating more discriminative risk indicators, whereas stronger models achieve comparable performance without retrieved context. The most effective assignment of LLMs to the two stages depends on the dataset. These findings show that the quality of the generated risk indicators is the main driver of zero-shot cyber threat detection performance.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-358](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
