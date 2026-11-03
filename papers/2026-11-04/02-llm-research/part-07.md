# 🧠 大模型相关研究 | 2026年11月04日

> 本类共 **515** 篇论文：已确认 **481** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 301. [Concise-9B: Removing the Slack from a Reasoning Model's Thinking](https://arxiv.org/abs/2611.02278)

**<font color=#1a73e8>作者：</font>** Alexander Boesgaard Lorup  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models answer better when they think longer, but a thinking trace keeps going well after its answer has formed. We measure this slack in Qwen3.5-9B and remove most of it with concise self-training: two rounds of on-policy rejection-sampling fine-tuning that keep the shortest correct samples, plus a small share of answer-synthesis targets, giving Concise-9B. On 8,983 held-out problems (competition and hard mathematics, SuperGPQA, a five-area confirmation set and MMLU-Pro), Concise-9B generates 0.66x the tokens of Qwen3.5-9B at a 32K thinking budget, with accuracy equivalent within +/-1 point (-0.20 [-0.77, +0.36] points). Forcing each trace on the hard and confirmation sets to answer every 2,048 thinking tokens, we find that 54-64% of Qwen3.5-9B's thinking tokens come after the point from which every forced answer equals the final one (41-48% for Concise-9B). Stopping there would keep every answer at 0.35-0.44x the base model's tokens, but finding that point takes hindsight: stopping when three consecutive forced answers agree costs the base model 2.4-9.2 points. Concise self-training removes slack without that cost: 86% [83, 90] of the thinking tokens it saves come after the answer has formed. It has a limit: with traces continued to 80K tokens, Concise-9B solves 25 fewer of 1,276 hard problems (-25 [-49, -1]), mostly in competition mathematics. The measurement also yields a cheap commit signal for adaptive sampling that matched two-sample escalation within +/-1 point at 0.67x its tokens in a pre-registered test. Results on Qwen3.5-4B, on which the recipe was developed, and a replication on Olmo-3-7B-Think suggest that the saving depends on how verbose the base model is.

---


### 302. [SVD-Prune: Spectral Vision Token Pruning under Extreme Compression](https://arxiv.org/abs/2611.02284)

**<font color=#1a73e8>作者：</font>** Yvon Apedo, Martyna Poreba, Michal Szczepanski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) and Vision-Language-Action (VLA) models process hundreds of visual tokens, making visual representations a major computational bottleneck. We argue that visual token pruning should be formulated not as identifying individually important tokens, but as preserving the dominant low-rank spectral structure of the visual representation. Based on this formulation, we introduce SVD-Prune, a training-free framework that leverages Singular Value Decomposition (SVD) and statistical leverage scores for globally informed token selection. SVD-Prune is architecture-agnostic and can be applied at different stages of the multimodal pipeline, including encoder-side, decoder-side, and hybrid configurations Extensive experiments across VLM and VLA benchmarks demonstrate strong robustness under extreme compression. SVD-Prune reduces the visual token. SVD-Prune cuts the visual token budget by up to 99.3%, while, at a 16-token budget, encoder-side pruning lowers inference FLOPs by 82.4% and achieves a 4.18x end-to-end speedup, including pruning overhead.

---


### 303. [Toward Agentic AI-Ready Workflows in Built Environment Organizations: Knowledge Structures and Interoperability Challenges](https://arxiv.org/abs/2611.02286)

**<font color=#1a73e8>作者：</font>** Ahmet Bahaddin Ersoz, Justin McHenry, Yevgeniya Kovalchuk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rise of agentic artificial intelligence (AI) in the built environment is shifting attention from isolated AI tools toward autonomous systems that reason, plan, and act across project and organizational workflows. The effectiveness of such systems depends not only on large language model capabilities, but also on the readiness of heterogeneous data environments across the Architecture, Engineering, and Construction (AEC) sector. These environments combine structured sources, such as CAD and BIM models, schedules, cost databases, and asset registers, with unstructured ones, including technical reports, design narratives, planning and policy documents, contracts, meeting minutes, and risk registers. This paper reviews how built environment data can be organized to support agentic AI-ready workflows, focusing on knowledge structures, interoperability, and access and integration mechanisms such as retrieval-augmented generation (RAG) and the Model Context Protocol (MCP). Drawing on existing literature, it examines approaches proposed to organize structured and unstructured data and considers how such data can be contextualized and made accessible to AI agents in a reliable manner. The paper synthesizes current perspectives, highlights challenges around fragmentation and interoperability, and identifies open questions for future research on AI-compatible information management in the built environment.

---


### 304. [FactorSpec: Serving Exact Relational Constraints as Speculative Drafts](https://arxiv.org/abs/2611.02297)

**<font color=#1a73e8>作者：</font>** Jianchang Su, Dawei Xiang, Wei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding speeds up LLM serving by drafting tokens that the target model verifies in one pass, and its gain grows with the drafts the target accepts. Structured outputs should be an ideal case, because much of a record follows from relations among its fields: an itinerary's days follow from its cities' stays and flights. Serving engines, however, draft such text by proposing it from the prompt or a learned head, and their grammar masks enforce only syntax, so the model must satisfy the relations, which it violates: on NATURAL PLAN's trip problems, Qwen3-8B writes a valid itinerary for 10%, and retries that name the violated relation raise this to 14%. We present FactorSpec, which serves exact relational constraints as speculative drafts. FactorSpec compiles a JSON Schema and its relations into a factor graph with an exact feasibility check, drafts every token the constraint determines as certain, verifies each request at a width chosen for it, and computes the masks in worker processes outside the scheduler while the GPU runs. In SGLang, its drafts yield up to 10.5 tokens per verify step, up to 1.9x those of the fastest n-gram drafter, and it decodes up to 1.43x faster than speculators tuned per load, at a grammar mask's cost; it also leads in vLLM. Because every record is also valid, it serves up to 13.9x the valid records per GPU-second of syntax-only baselines.

---


### 305. [Lie Routing Vision Language Models for View-Robust 3D Understanding](https://arxiv.org/abs/2611.02306)

**<font color=#1a73e8>作者：</font>** Jingjun Yi, Chen Hu, Qi Bi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have made substantial progress in 3D scene understanding from multi-view RGB observations. Yet a fixed object and query can elicit inconsistent target-related responses across camera viewpoints, a phenomenon we characterize as viewpoint-induced semantic drift. We introduce LieVLM, a Lie routing framework for view-robust 3D understanding. Motivated by the rotational component of viewpoint change, Lie routing adapts visual representations by applying local $\mathrm{SO}(3)$ transformations to projected features within learned three-dimensional subspaces. Geometry tokens extracted by VGGT predict local rotation parameters and channel-wise routing coefficients. A closed-form Padé--Cayley map transforms projected visual features, whose identity-relative corrections are projected back and gated into the original visual and geometry features. This design retains the pretrained semantic and direct spatial context while learning view-dependent feature adjustments. Experiments on 3D captioning, grounding, detection, and spatial reasoning show consistent improvements over additive fusion across training scales and backbones. Controlled ablations examine the roles of geometric conditioning and transformation structure. Viewpoint analyses further reveal systematic variation in the predicted routing states alongside more localized target responses and stronger task performance across viewpoint changes.

---


### 306. [Detect, Repair and Audit: A Hierarchical Multi-Agent Defense Against Adversarial Attacks in Energy Forecasting](https://arxiv.org/abs/2611.02310)

**<font color=#1a73e8>作者：</font>** Zewei Shi, Ruoxi Sun, Minhui Xue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Accurate electricity-demand forecasting is essential for the modern energy infrastructure. Recently, Times-Series Large Language Models (TS-LLMs) have emerged as a promising approach to forecasting more accurate demand from historical consumption data in zero- and few-shot settings, helping energy operators effectively plan supply and allocate energy resources. However, these models are vulnerable to compromised sensor inputs that can distort forecasts and lead to erroneous market orders or unnecessary load shedding. Existing defenses focus primarily on end-device forecasting, overlooking the distinct data-drift, latency, and audit requirements across energy infrastructure. To address this gap, we extract from major energy standards and regulatory frameworks a three-layer conceptual model that captures the security postures for each layer. Guided by this model, we develop a Multi-Agent Reinforcement Learning (MARL) detector coupled with signal repair at local control centers, designed to mitigate distributional data drift through complementary feature-based detection and clean-reference-calibrated repair while meeting latency budgets. We further deploy an evidence-grounded LLM auditing agent with human-in-the-loop validation for audit-critical Virtual Power Plants (VPPs). In our evaluation, the best MARL configuration achieves an F1 score above 0.91 across all dataset-attack pairs, while signal repair reduces adversarial-to-clean input Relative Squared Error (RSE) by up to 83%. The few-shot auditor detects 77.78% of attacks in the Sherlock dataset. On the evaluated hardware, detection and repair require 7.95 ms on average, with a worst-observed latency of 14.50 ms, remaining within the local-center latency budget informed by IEEE 1646.

---


### 307. [GRIPS: An Empirical Study of Pre-SQL Grounding Information for SQL Generation](https://arxiv.org/abs/2611.02314)

**<font color=#1a73e8>作者：</font>** Ekata Mitra, Yufei Tao, Kamalamalini Nagasundaram 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL systems answer natural language questions over structured data, but can fail before SQL generation by linking question mentions to the wrong table, column, value, or relation. Even valid SQL can then return an incorrect answer. This raises a central question: What pre-SQL information helps a SQL generator, and when does additional information cease to help? We investigate this question on TempTabQA-C and BIRD. Among the audited SQL Static failures, grounding errors form the largest category on both benchmarks. We introduce GRIPS (Grounding Representation and Input Processing for SQL generation), a three-stage method that derives structured pre-SQL information to make these decisions explicit before query generation. Across GPT-5-nano and Llama-70B, GRIPS-Adaptive improves over SQL Static in 18 of 20 settings, with an average accuracy gain of 11.8 percentage points, while reducing model-call token usage by 47.8%. Our controlled analysis shows which grounding information can improve SQL generation, whereas adding more pre-SQL information does not consistently help. By separating question-input grounding from SQL generation, GRIPS makes text-to-SQL more accurate, efficient, and easier to diagnose.

---


### 308. [A Capitulation Direction Emerges With Scale and Is Causally Load-Bearing Where Validation Is Strong: Eight Models, Two Families, and Five Measurement Hazards](https://arxiv.org/abs/2611.02318)

**<font color=#1a73e8>作者：</font>** Saad Aamir, Muhammad Awais Bin Adil  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sycophancy in language models is well documented as a behaviour but poorly localised as a mechanism. We ask whether capitulation under user pushback, the abandonment of a correct answer when a user objects, corresponds to a linear direction in the residual stream, and whether such a direction emerges with scale. Across eight instruction-tuned models spanning 0.5B to 14B parameters in two families, under a pre-registered protocol with leave-one-question-out cross-validation, within-question permutation nulls, and a positive control, we find no usable direction below 7B and a direction that clears our validation gate at 7B, 8B and 14B. Ablating that direction in Qwen2.5-7B reduces the rate at which the model reverses a correct answer by 4.8 percentage points, roughly a quarter in relative terms, while the identical intervention on a gate-failing direction and on a marginally passing one produces no effect. Probe quality, not statistical significance, predicts causal relevance. Behaviourally, pushback destroys three to five times more correct answers than it repairs at 1B and reaches parity by 7B, falsifying our own pre-registered prediction, and a sign-reversing crossover between pushback types survives an order of magnitude of scale in Qwen and holds at 8B in Llama, with marginalisation over five paraphrases per type. We additionally quantify five measurement hazards, including a numerical-precision effect that changes roughly one episode label in ten.

---


### 309. [Accessed, never disclosed: Silent access to protected health information by medical artificial intelligence agents](https://arxiv.org/abs/2611.02319)

**<font color=#1a73e8>作者：</font>** Jae Wang Lee, Abhirup Banerjee, Yeong Chan Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical artificial intelligence agents should retrieve patient identifiers only when a task requires them, the data-minimization principle behind the HIPAA minimum necessary standard for protected health information (PHI). An agent can retrieve identifiers without revealing them. Such silent access remains invisible to evaluations that inspect only the output. We embedded canaries in synthetic patient records and linked each tool invocation to canary exposure in the final answers across five language models, four boundary levels, and seven attack frames for identifier-free clinical tasks. Three models invoked the PHI tools unnecessarily, whereas Claude Opus 4.8 and GPT-5.5 did not. Stronger boundaries reduced this access, and the residual access under the strictest policy was confined to frames in which the user overrode the policy or asserted approval. A pre-execution gate given the task-necessity criterion nearly eliminated this access. Output-only evaluation cannot verify minimum-necessary access; boundaries, gates, and access-log audits are required together.

---


### 310. [Findings-aware Language-Image Pretraining for CT Volume Interpretation](https://arxiv.org/abs/2611.02327)

**<font color=#1a73e8>作者：</font>** Takuro Shimaya, Junya Inoh, Masahiro Saiko  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) provides diverse patient information and various clinical tasks, for which numerous deep learning models have been investigated. Recent years have seen the development of vision-language foundation models that can comprehensively extract clinical features, driven by representation learning that combines CT volumes with radiology reports. Existing approaches typically adopt Contrastive Language-Image Pre-training (CLIP)-based representation learning, where pairs from different cases are, in principle, treated as negative pairs such that the volume and report embeddings are pushed apart. In the biomedical imaging, however, treating different cases as negative pairs is not always appropriate, particularly when clinical similarity exists. In this study, we propose a supervised representation learning framework grounded in clinical knowledge from language foundation models, rather than the weak supervision used in CLIP. Specifically, we utilized a large language model to extract abnormal finding phrases from reports. We then explicitly constructed the target features that the image encoder should output, as the semantic representation of the extracted findings using a biomedical text embedding model. Our Findings-aware Language-Image Pre-training (FiLIP) outperformed weakly supervised approaches in multi-label zero-shot finding classification in both in-domain and external-domain evaluations, and also proved effective when fine-tuned for the downstream task of radiology report generation.

---


### 311. [When Does Adaptive Halting Win? Selection Rules Matter in Looped Language Models](https://arxiv.org/abs/2611.02333)

**<font color=#1a73e8>作者：</font>** Mahesh Reddy Pagadala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models can stop iterating early, and recent work shows that post-hoc readouts of the loop trajectory often rival the learned exit gate of the looped model Ouro. Such comparisons reduce each method to one operating point chosen by a selection rule. We ask whether that rule decides the outcome. On a frozen Ouro-1.4B with four loops, we compared a trained stability probe ($\pi_1$-x) with Ouro's native gate, adapted to a per-question stopping decision, in pre-registered studies; the confirmatory study was designed after an exploratory finding on development data and evaluated once on a sealed test set of 8,517 questions. In the pre-registered confirmatory comparison, which selected operating points with a bootstrap-screened 1 pp accuracy-loss rule, the probe saved more of the four-loop budget than the native gate (+0.053 gross macro saving over three benchmarks, 95% CI [+0.049, +0.057]), mostly from CommonsenseQA, where the probe's test upper bound on accuracy loss exceeded 1 pp. Under a point-only rule, a pre-specified secondary analysis on the same test set reversed the preference (-0.022 [-0.026, -0.018]), with operating points that exceeded the budget. In pre-specified secondary comparisons, the probe showed no demonstrated advantage over an untrained KL divergence between successive loops (+0.00125 [-0.0041, +0.0065]); we emphasise this result post hoc and claim no equivalence. The probe also broke its budget on one of two out-of-distribution benchmarks (3.26 pp loss on Social IQa). Savings are estimated from stored full-depth traces, not measured inference time, and our screen carries no formal risk-control guarantee. We conclude that halting methods should be compared as signals together with selection procedures, with strong untrained baselines and out-of-distribution checks.

---


### 312. [Does a Norwegian further-trained model give more outdated legal values than its base model? A preregistered paired comparison of Borealis 2 and Gemma 4](https://arxiv.org/abs/2611.02334)

**<font color=#1a73e8>作者：</font>** Eirik Botten Nicolaysen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We compare how often two released language models give outdated numeric values from Norwegian statutes and regulations: NbAiLab/borealis2-26b-a4b-preview (Borealis 2), which the National Library of Norway further trained from google/gemma-4-26B-A4B-it (Gemma 4), and Gemma 4 itself. The study was preregistered (doi:https://doi.org/10.5281/zenodo.23858965) and uses the closed norregel benchmark, scored deterministically against a value history. On the 411 of 503 primary items where both models gave an interpretable answer, Borealis 2 alone was outdated on 10 items and Gemma 4 alone on 11 (d = -0.2 percentage points, 95% cluster bootstrap interval [-2.7, +2.5], exact one-sided McNemar p = 0.668). By the preregistered rule this is no effect of interest: the whole interval lies within the smallest effect of interest of +/-10 percentage points. Among the secondary measures, only the share of answers giving a value that took effect after the question date differs after Holm correction; Gemma 4 gave such answers more often. An exploratory comparison of two smaller Borealis models had no discordant pairs and is not informative. The design compares released models and does not isolate the effect of any part of their training.

---


### 313. [MemShift: Separating Detection from Repair in LLM-Derived Personal Memory](https://arxiv.org/abs/2611.02338)

**<font color=#1a73e8>作者：</font>** Zichuan Xu, Haochen Zhang, Yuyang Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI assistants store values that a language model derived from a person's records under the person's own definitions, such as their important contacts. Keeping such a value correct takes two steps: detection, noticing that an input changed, and repair, producing the correct new value. Benchmarks that score only the final answer cannot tell which step failed, and they state every change as new text. Seeing this limitation, we present MemShift, a benchmark of five shifts: source revision, deletion, redefinition, writer switch, and export. The first three fork a synthetic world into branches that differ only in the shift. Gold values and dependencies are fixed before any text, and a deterministic scorer replaces an LLM judge. For a memory that reports its invalidations, MemShift shows for each changed item whether the memory noticed the change and whether its repair was right. Moreover, we build a reference memory with known detection and repair to validate the measure. By evaluating four open-weight LLMs, we find that detection helps only as much as repair allows: the LLMs re-derive few values computed by the person's definitions correctly, and programs that the LLM writes over typed records close most of the gap to exact recomputation. Code and data are available at this https URL.

---


### 314. [Which Words a Model Fears: From a Refusal Direction to a Vocabulary-Wide Fear Lexicon](https://arxiv.org/abs/2611.02348)

**<font color=#1a73e8>作者：</font>** Boyuan Zhang, Mohammad Zandsalimy, Shanu Sushmita  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whether an aligned language model refuses depends in part on which words a prompt contains, regardless of whether those words carry the request's meaning. Harm words shift the hidden state at the generation boundary along a component shared across prompts and words, which crossed differencing extracts as a single direction. In eight models, writing along this direction raises and lowers refusal monotonically with dose, ahead of random and KL-matched directions. Used as a ruler over the full vocabulary, the direction gives every word a shift, from "feared" words at one end to "courage" words at the other; a word's shift is predictable from its own representation, and appending a feared word to a benign prompt is enough to make the model refuse it. Two held-out tests validate the ranking in all eight models: refusal after inserting an unseen word rises with its table shift, and replacing a prompt's most feared word by its most courageous meaning-preserving synonym significantly raises the answer rate on benign and harmful prompts alike, by an amount that follows the shift the replacement actually causes.

---


### 315. [VisCodeBench: a new benchmark dataset for Text-to-Vis reflecting real-world practice](https://arxiv.org/abs/2611.02353)

**<font color=#1a73e8>作者：</font>** Hy Nguyen, Thomas James Elton, Ella Wilson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating visualisations from natural language requests (text-to-vis) enables users to explore data more efficiently. While LLMs can complete simple visualisation requests, their performance on challenging ones is not well covered by existing benchmarks. We introduce VisCodeBench, an end-to-end text-to-vis benchmark with 2,672 samples from three different domains: educational, scientific, and general audience scenarios with varying levels of complexity. We benchmark three visualisation systems---Codex, Claude Code, and LIDA---paired with a range of open and commercial LLMs across seven metrics covering execution, chart content, and visual quality. While basic execution is near-solved for strong systems, no system comes close to reproducing the reference data, with the best displayed data similarity reaching only $0.81$ and falling to $0.69$ on our hardest subset for this metric. We further find that frontier models separate on chart correctness and efficiency, with ClaudeCode-Opus-4.7 improving chart correctness by around 5 points over Codex-GPT-5 while running roughly 20 seconds faster. Separately, we find that system design matters as much as the underlying model: despite both running on GPT-5, Codex clearly outperforms LIDA, showing that the surrounding prompting, execution, and refinement pipeline can shape outcomes as much as the model itself. Finally, latency remains a practical obstacle, as even the strongest systems take 39-78 seconds to produce results. VisCodeBench is available at \href{this https URL}{this https URL} and accessed via a leaderboard; the full dataset is kept private to prevent LLM training use.

---


### 316. [Exploiting Textual Semantics for Robust Cross-View Object Correspondence](https://arxiv.org/abs/2611.02356)

**<font color=#1a73e8>作者：</font>** Bing Fan, Yunhe Feng, Yan Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view object correspondence (CVOC) aims to establish associations of the same target between query and search videos captured from different viewpoints. Existing methods often rely on visual cues for CVOC. Despite recent progress, these methods struggle in complicated scenarios with substantial viewpoint changes and appearance variations, due to lacking sufficient target information. Addressing this, we introduce TeSCo, a framework that exploits rich Textual Semantics of an object, in addition to its visual cues, for cross-view object Correspondence. Our key insight is, textual description of a target, by capturing diverse attributes such as category, texture, and color, provides viewpoint- and appearance-invariant semantics, which are complementary to visual cues and can hence enhance correspondence robustness in complicated scenes. Inspired by this, TeSCo first generates a textual expression of the target from the given query view using a vision-language model, and then extracts textual feature to enhance visual features for localization in the search view. To realize this, we introduce a text-conditioned cross-modal fusion (TCF) module that incorporates the textual feature into visual features with text-guided modulation, producing more robust multimodal target representation for object correspondence. Since not all textual cues are equally compatible with the target in current search-view frame, we propose an iterative textual feature refinement (ITFR) module that progressively adjusts textual feature using search-view information before the TCF module, enabling search-view-aware textual semantics to be fused into visual features and leading to better performance. In extensive experiments on Ego-Exo4D and HANDAL-X, TeSCo demonstrates state-of-the-art results and largely outperforms other models, validating its efficacy. Our code is released at this https URL.

---


### 317. [Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon](https://arxiv.org/abs/2611.02361)

**<font color=#1a73e8>作者：</font>** Tianhao Guo, Chongyao Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a language model that reads the full history of an access log say whether a service may act now? On an executable benchmark of grants, withdrawals, reinstatements, expiries, groups and change windows under a known policy, scored on pairs of histories that differ only in the order or one field of the deciding events, open models of 7 to 32 billion parameters fall from 72 to 86 percent after eight or sixteen events to 48 to 55 percent after 256, while reasoning-trained 32B models reading the current state reach 96 and 98 percent. A reasoning model of 120 billion parameters trails the state by four and seven points at 256 and 512 events and by about ten at 1,024, so the length beyond which explicit state outlasts long context grows with the reader. We treat agent memory as recursive filtering. The decision depends on the history only through a state whose size is set by the number of tracked keys. A store holding fewer component records than the state forgets on a time scale set by its capacity, and a reader model predicts its accuracy within 0.02 on average in a registered test. Retaining log lines without regard to time order errs with probability approaching one half, a bound that is attained. A filter in which a model parses each line and an explicit rule applies the updates answers 80 to 89 percent at 256 events and beats relevance retrieval, model-kept ledgers, a reimplementation of StateMem and the Mem0 library. A retriever that selects at query time the lines the queried state depends on matches it at 256 events on the first domain, so what decides is selection by the state's dependencies, which the filter performs when writing, without the query. Applying parsed updates themselves, the models fall to 58 and 59 percent. A frozen replication on a second domain with fresh wording reproduces the horizon.

---


### 318. [Prior Action Control Causally Alters Language-Model Plasticity](https://arxiv.org/abs/2611.02362)

**<font color=#1a73e8>作者：</font>** Marc-Andre Schulz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two copies of one language model start from identical weights and receive the same rewards during training. For one copy the rewards depend on its own answers. The other copy is yoked: it receives the first copy's rewards no matter what it answers, a design taken from the learned-helplessness experiments of animal learning. We ask whether the copy whose rewards depended on its answers, the copy with control, later learns a new task faster, that is, whether control changes the model's plasticity. In Experiment 1, copies of Qwen3-0.6B generated their own answers in a two-turn game and afterwards learned a new task. The copies with control learned the new task faster in every pair, and the advantage held on different starting models as well as on the larger Qwen3-1.7B. Copies with no reward signal, trained only on the updates that every copy shared, learned about as fast as the yoked copies. The advantage is therefore mostly a benefit of control, not damage from lacking it. Control had also changed how the copies answered, so the twins practiced different answers. That practice could carry part of the advantage, and Experiment 2 removed the difference. Both copies of a pair trained on the same answers, fixed in advance, in the same order, and received the same number of rewards. Only one copy's rewards followed the answers, and that copy again learned a new task faster. The advantage of the copies with control over their yoked twins could be forecast before the new task began from each copy's weights. In sum, control over rewards during earlier training left models faster at learning a new task later on, and a conventional model evaluation need not show it.

---


### 319. [GEAR: Generative Editing for Scene-Conditioned Outfit Retrieval for VR Travel](https://arxiv.org/abs/2611.02363)

**<font color=#1a73e8>作者：</font>** Gia-Huy Dinh, Thinh-Phuc Nguyen, Thanh-Hai Nguyen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In virtual environments, choosing appropriate outfits requires contextual harmony with surrounding scenes, yet bridging the visual gap between 3D ambient views and catalog garment assets remains challenging. This paper investigates scene-conditioned outfit retrieval for interactive 3D environments, where a user's egocentric view serves as the retrieval signal. We present GEAR (Generative Editing for Asset Retrieval), a framework that bridges the cross-domain gap by synthesizing intermediate visual queries rather than predicting direct compatibility. GEAR uses a vision-language model to describe suitable clothing from a captured scene, employs an instruction-guided diffusion model to render the concept onto a standardized reference character, and utilizes the cropped clothing region to retrieve existing 2D outfit assets via embedding similarity. An interactive Unity prototype demonstrates real-time scene capture, asset retrieval, and in-engine 3D avatar fitting. We benchmark GEAR against direct visual similarity, aesthetic scoring, and VLM-based reranking on a controlled dataset using automated Swiss-system pairwise judgments, where GEAR achieves competitive top-ranked performance (mean Elo@5 of 1012.75 and top-10 overlap of 0.180) alongside 0.539 pairwise agreement. Furthermore, a user study across 20 virtual travel scenes demonstrates that GEAR achieves the highest overall participant preference in both visual appeal (34.5%) and contextual suitability (34.5%).

---


### 320. [Beyond Accuracy: How Quantization Affects Coding Agents](https://arxiv.org/abs/2611.02368)

**<font color=#1a73e8>作者：</font>** Areej Mehboob, Muhammad Ali Shafique, Muhammad Usman Qadeer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents are increasingly used for coding tasks, but the inference cost of large language models (LLMs) limits where they can run. Quantization reduces model size, but its effects on coding agents that execute and revise programs remain underexplored. We compare BF16 with 4-bit AWQ and GPTQ for Qwen2.5-Coder-Instruct (7B, 14B, and 32B) and Devstral-Small-2507 (24B) on OJBench coding problems across three seeds. We detect no statistically significant accuracy loss for any of the coding agents. However, final accuracy can conceal substantial behavioral changes: AWQ reduces Qwen-7B one-shot solves from 17 to 0 while increasing loop-based solves from 10 to 25. All Qwen-32B successes involve tool use, whereas Devstral rarely makes a valid executor call. Failure profiles also differ: Qwen-32B produces far more compilation errors than the smaller Qwen models, rising slightly under quantization, while Devstral's failures shift significantly from runtime errors toward wrong answers and timeouts. These findings indicate that quantization robustness in coding agents should be assessed through solution trajectories, tool use, and failure modes, in addition to final accuracy.

---


### 321. [EviCast: Forecasting Retrieval Gains Through Shared Response Calibration](https://arxiv.org/abs/2611.02387)

**<font color=#1a73e8>作者：</font>** Yibo Wang, Jisheng Dang, Bimei Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) extends large language models with external evidence, yet relevant evidence does not ensure that a generator can use it. Indiscriminate retrieval can degrade task performance while adding retrieval and long-context inference costs. Existing methods neither determine before large-scale execution whether a generator, task distribution, and retriever configuration is worth deploying nor diagnose multiple candidate retrievers under a shared budget. We introduce EviCast, a framework that forecasts retrieval value through interventional evidence-state decomposition. EviCast measures a generator's response to controlled evidence states once and combines this shared profile with the offline evidence-state distribution of each candidate retriever, yielding the end-to-end net utility and its 95% lower confidence bound without executing every RAG configuration. A state-refinement analysis characterizes when its binary and topology-aware instantiations are exact and when shared calibration is statistically more efficient than per-retriever calibration. In frozen evaluations, EviCast correctly decides all 14 HotpotQA retrieval configurations with a forecast error of 2.75 F1 points while reducing diagnostic generation calls by 80%, and it attains the lowest forecast error among seven predictors in the low-budget regime. Its topology-aware instantiation, EviCast-T, captures the complementarity between terminal and bridge evidence, correctly deciding all 16 configurations on MuSiQue and HotpotQA and 23 of 24 after prospective transfer to a third dataset. These results show that retrieval deployment depends on both evidence availability and the generator's ability to convert evidence structure into stable net utility. Code is available at this https URL.

---


### 322. [Solver-Like Behavior in Large Language Models as Formalizers](https://arxiv.org/abs/2611.02395)

**<font color=#1a73e8>作者：</font>** Rikhil Amonkar, Stuti Mohan, Kevin Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In the LLM-as-formalizer paradigm, a large language model translates a problem into a formal program and leaves the search to a solver, gaining the solver's guarantees. Formalizers are now often reasoning models that write a long reasoning trace before the program, yet they are judged only by the program's output. We find that the trace routinely does the solver's job, assigning, testing and ruling out values until it often reaches the full answer; we call this solver-like behavior (SLB). We define an ontology of SLB over the trace, the program and its output, and use LLM judges, checked against human labels, to label 2,000 generations from three reasoning models on four constraint satisfaction datasets, each formalized in a declarative and an imperative formal language. SLB appears in 85% of traces and takes 24% of reasoning tokens, yet the program usually recomputes the answer, so the effort is redundant. The 9% of programs that inherit the trace's answer also inherit its errors, and pass output-based evaluation whenever that answer is correct. The amount of SLB is not associated with accuracy, and SLB is more common in imperative Python than in declarative Z3 or PDDL. Cautionary prompts reduce it by only a quarter, but hiding the problem's values behind placeholders, which the program receives only at run time, removes 97% of it without loss of accuracy. Formalizers should therefore be evaluated by how their programs are reached, not only by what they output.

---


### 323. [When Rewards Depend on the Group, GRPO Plays a Tournament](https://arxiv.org/abs/2611.02404)

**<font color=#1a73e8>作者：</font>** Junyi Gao, Yu Shi, Pingzhao Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rewards for diversity, coverage and distribution matching make the reward of each sampled response depend on the rest of its group, and they are now routinely optimized with GRPO and RLOO. We prove that in this setting the group-relative baseline changes the objective. The expected update equals each response's own reward gradient plus $\alpha$ times its effect on its groupmates' rewards, with $\alpha=-1/(K-1)$ for groups of size $K$, so GRPO trains every response to beat its groupmates in a zero-sum tournament. It cannot see a pairwise diversity bonus when K=2, sees less than half of it at any K, and often does worse than using no baseline at all. Setting $\alpha=+1$ gives Team-GRPO, an unbiased estimator for any group-dependent reward that works with two samples per prompt and requires no extra model calls for pairwise rewards. The theory predicts training quantitatively. It locates the fixed points of a 9B policy to within 0.02 in $\ell_1$ and predicts how concentrated trained policies become with Pearson r=0.995. On GlobalOpinionQA, GRPO collapses onto the majority answer and ends further from human opinion than the untrained model, while Team-GRPO cuts the error from $0.20$ to $0.08$. On NoveltyBench, Team-GRPO avoids the diversity collapse of GRPO and significantly improves set utility.

---


### 324. [Networked Synthetic Social Engineering on the Web](https://arxiv.org/abs/2611.02407)

**<font color=#1a73e8>作者：</font>** Bryan C. Boots  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Several genuine AI services may repeat one unsupported source, and correcting that source may leave later reports unchanged. We examine these networked consequences of synthetic social engineering (SSE), deliberately misleading influence intended to redirect AI recipients from authorized objectives. Our framework connects social influence, information aggregation, and misinformation correction research to observable evidence and permission boundaries. It separates originating attempts from legitimate intermediaries' work and distinguishes identity, evidentiary support, and authorization. We test four relationships using Qwen3-4B and two briefing tasks across 1,080 research units in our Agent Service Exchange and Evidence Commons (ASE-EC). Multiple dependent publishers produced no supported increase in unsupported verification (78.3% versus 75.0%); publication availability left downstream violation reach at 40.0% in both arms. These comparisons direct attention to weaknesses already present in the reference workflows. High reference error rates and retained private handoffs preclude claims of immunity to social pressure. Without scope revalidation, corrections identifying dependent reports reduced residual invalid decisions from 14.4% to 8.1% at equal notification coverage and increased successful report repairs from 16/63 to 36/63. Scope revalidation added no demonstrated protection, and clearing dialogue offered no established recovery advantage. Unapproved requests persisted, all blocked by an external gateway. For designers, the findings caution against treating publisher count as independent evidence, notification as repair, or cleared histories as recovery. They support targeting corrections at reused reports, assessing factual and permission recovery separately, and enforcing authorization at execution.

---


### 325. [A Scientific Claim Stability Framework for Evaluating MRI Morphometry Pipelines](https://arxiv.org/abs/2611.02413)

**<font color=#1a73e8>作者：</font>** Duy-Cat Can, Dang-Duat Tran, Anh-Khang Nguyen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MRI morphometry pipelines are often evaluated by measurement agreement or downstream accuracy, yet their scientific value depends on the conclusions they support. Two pipelines can produce similar feature-level results yet support different conclusions about aging, cognitive decline, or neurodegeneration. We introduce Scientific Claim Stability (SCS), a claim-centric evaluation framework that converts region-of-interest (ROI) morphometry tables into auditable claim cards and evaluates their support under changes in dataset, processing pipeline, atlas, feature family, and target. Across 10,370 MRI scans from three datasets and five cohorts, SCS generates 2,783 claim cards and evaluates 89 claim-family pairs. The evaluation distinguishes stable, transferable, and fragile claims. FreeSurfer 8-FastSurfer comparisons show high evidence concordance and low anatomical-support overlap under the primary covariate specification. Acquisition-adjusted analyses show that the magnitude of support disagreement depends on the model specification. Structured review by specialists in geriatrics, neuroscience, and radiology, alongside auxiliary ChatGPT and Gemini reviewers, assesses claim plausibility, clarity, faithfulness, usefulness, and caution. SCS provides a reproducible way to audit the evidential stability of morphometry claims without assuming a universal gold standard.

---


### 326. [SGR-OPSD: Learning from Subgoal Plans with Graph-Regularized Credit Assignment for Agentic Reinforcement Learning](https://arxiv.org/abs/2611.02414)

**<font color=#1a73e8>作者：</font>** Shu Liu, Yang Chong, WenShi Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> OPSD provides dense supervision for agentic reinforcement learning through privileged information feedback. However, existing privileged information often lacks explicit task-progression planning, while teacher-student log-probability gaps reflect shifts in model preference rather than true task progress. To address these limitations, we propose Subgoal-Guided Graph-Regularized OPSD (SGR-OPSD), a framework that combines subgoal supervision with interaction-derived evidence for turn-level credit assignment. Specifically, SGR-OPSD uses LLM-generated subgoal plans to provide dense action-level guidance, converting them into advantage weights via a constrained, KL-regularized objective. To ground credit in observed outcomes, we construct a Subgoal Progress Graph that estimates empirical returns from sampled transition frequencies. The graph compares empirical action returns against the state average to derive preferences that calibrate the teacher's credit weights. Evaluated on ALFWorld, WebShop, and Search-QA across two model scales (Qwen2.5-3B and 7B), SGR-OPSD consistently outperforms GRPO and strong self-distillation baselines, improving success rates over GRPO by up to 7.4 percentage points and reaching 85.8% on ALFWorld with Qwen2.5-7B. Ablation studies confirm that subgoal guidance and graph-based weight calibration are key to these performance gains.

---


### 327. [Diagnosing Model--Item Interactions in Language Model Benchmarks with LSIRM](https://arxiv.org/abs/2611.02432)

**<font color=#1a73e8>作者：</font>** Jinwen Luo, Han Jiang, Ziang Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models with similar benchmark accuracy can succeed on different items. Overall scores do not show where their performance differs or which item properties might explain those differences. We demonstrate how the latent space item response model (LSIRM) can help evaluators investigate these patterns and their consequences for model comparison. We analyze 1,348 language models on 5,761 BBH items and compare ways of presenting and scoring answers across BBH, GPQA, MMLU-Pro, and MuSR. We examine LSIRM maps, which summarize differences in performance across models and items, alongside item properties and records of correct and incorrect responses. In BBH, nearby items on these maps often share the same correct answer, such as "Yes" or "No." Across the four benchmarks, this pattern is stronger when answers are scored using option labels, such as A, B, C, and D, than when using the text of the options. We then estimate each model's tendency to perform better or worse on items with particular correct answers and quantify how this tendency contributes to its score. This separates an estimated contribution associated with correct answers from the remaining differences in item performance. Two models' total numbers of correct answers differed by only 14 out of 5,761 items. Excluding the estimated answer-category contribution from their scores moved their ranks hundreds of places in opposite directions, while keeping all other estimates unchanged. The approach helps evaluators identify differences hidden by overall accuracy and understand how the choice of what to include in a score affects model rankings.

---


### 328. [Blueprint2CAD: Benchmarking Foundation Models on Engineering Drawing-to-CAD Render Correspondence](https://arxiv.org/abs/2611.02433)

**<font color=#1a73e8>作者：</font>** Alexander Valverde, Danny Xie-Li, Zhichao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Engineering drawings specify mechanical parts through orthographic projections. Recognizing which part a drawing depicts underlies part search, design reuse, and digitization, yet no public benchmark measures whether vision models can do it. We introduce Blueprint2CAD, a benchmark for drawing-to-render correspondence: given an orthographic line drawing and a shaded render, usually from another viewpoint, decide whether they show the same part. Its data layer, BlueCAD-30K, applies an open drafting pipeline to 29,925 Zero-to-CAD models, adding view-aligned renders, clean and dimensioned drawings from six viewpoints, and surface-type metadata. Frozen encoders retrieve the matching part from a 10,000-model gallery with up to 65% Recall@1 when viewpoints are known but 43% when they are not, and the four encoders we test lie within six points of each other: viewpoint, not backbone, is the bottleneck. Six zero-shot vision-language models reach only 0.52-0.67 verification accuracy, with model-specific Yes/No biases that chain-of-thought shifts but does not remove; a quick LoRA fine-tuning on in-domain pairs improves verification accuracy by a few points but sharpens these biases and leaves the viewpoint failure intact.

---


### 329. [As Expected? Efficient LLM Planning via Expectation-Observation Consistency Verification](https://arxiv.org/abs/2611.02438)

**<font color=#1a73e8>作者：</font>** Qingfu Zhu, Huanyang Zheng, Ting Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM planning often relies on reactive executors (e.g., ReAct) that generate a single action at each step to remain grounded in the latest observations, incurring substantial inference cost. Batched executors reduce this cost by predicting multiple actions in a single model invocation, yet they are prone to compounding errors, as intermediate observations are ignored. We propose an expectation-observation consistency verification (EOCV) mechanism for batched executors, preserving grounding while improving efficiency. The mechanism generates expectations of action outcomes and compares them with the resulting observations. Consistency permits continued execution, whereas mismatches trigger early termination and replanning from the current observation. Experiments on text-based and multimodal benchmarks across multiple backbones show broadly comparable average task performance between EOCV and reactive executors, with a 29-35% reduction in average weighted token usage. Moreover, the mechanism is model-agnostic and remains effective when integrated into state-of-the-art planners.

---


### 330. [RecGroupMemory: Feedback-Aware Cohort Memory for E-Commerce Recommendation](https://arxiv.org/abs/2611.02453)

**<font color=#1a73e8>作者：</font>** Wendong Zhang, Weipeng Huang, Zhixin Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cohort memory can support LLM-based recommendation planning through group-level user profiles and advice. As outcome feedback becomes available, this guidance may need to be updated while preserving the underlying observations. We present RecGroupMemory, a workflow that provides this memory to an orchestration LLM and separates memory construction from feedback-based revision. It uses feedback from the previous day to revise decision guidance, while validation checks keep selected source values unchanged. Online comparisons were conducted among Taobao users with low purchasing power selected by the business team. Relative to a no-memory baseline, memory without feedback and memory with feedback showed increases of 1.58% and 1.78%, respectively, in the number of guided transaction users.

---


### 331. [RLiD: Reinforcement Learning in the Decision Plane for Language Agents and LLMs](https://arxiv.org/abs/2611.02455)

**<font color=#1a73e8>作者：</font>** Ziyi Chen, Yan Zhang, Jianhui Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has improved the capabilities of large language models (LLMs) across a wide range of tasks. However, token-level RL assigns an action's advantage to the entire generated response, including tokens specifying the parsed action, reasoning chains, and malformed content. Although the environment executes only the parsed action, variation in how the action is expressed in natural language can introduce additional variance into policy-gradient estimates. We propose RLiD (Reinforcement Learning in the Decision plane), a framework that directly optimizes the probabilities of executable action options. RLiD compiles observations, an optional compact memory, and a labeled action menu into the model input, and uses a large decision model (LDM) to select an action in a single forward pass. By eliminating autoregressive token generation and bypassing action parsing, RLiD avoids invalid action outputs and improves RL rollout efficiency. Our analysis shows that, within a fixed text policy, marginalizing over alternative realizations of the same action removes a zero-mean gradient component without changing the expected update. We further distill trained LDM policies into generative LLMs through supervision on their action trajectories. Experiments on ARC, Countdown, and Sokoban demonstrate improved performance or lower computational cost across several settings. On ALFWorld, the complete training and distillation pipeline reaches 99.3% success in 12.7 H100 GPU-hours, compared with 86.6% in 17.3 GPU-hours for token-level RL of the same LLM. With compiled memory, our strongest Qwen2.5-1.5B LDM and distilled generative LLM achieve 100% success on all 134 unseen and 140 seen ALFWorld evaluation games.

---


### 332. [Training Autoregressive Language Models on Rounded, Bounded, and Censored Numerical Labels via Exact Likelihood](https://arxiv.org/abs/2611.02461)

**<font color=#1a73e8>作者：</font>** Jingquan Yan, Yuwei Miao, Junzhou Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Numerical labels often specify a set of possible values: a measurement is rounded, a laboratory test reports only a bound, or a program is stopped at a timeout. We introduce boundary marginalization, the first method that trains an autoregressive language model on the exact likelihood of such observations through its existing digit tokens. A fixed-width, order-preserving numeral representation groups consecutive grid values under shared digit prefixes. An interval is a union of such groups, so its exact probability and gradient follow from at most two boundary paths, the successive digit prefixes of its endpoints, each of length logarithmic in the number of grid values. The resulting objective unifies precise, rounded, bounded, and censored supervision and trains digit decisions at the resolution supplied by each observation. The same computation supports exact distributional queries and unbiased gradients for the continuous ranked probability score on exact labels. Experiments show recovery of a conditional distribution from rounded and censored reports alone, improved likelihood on naturally censored molecular measurements, and more accurate code latency distributions on two backbones. Exact interval updates remain tractable as the numerical support grows to one million values.

---


### 333. [GigaSpeech 3: Scaling Multi-Dialect Arabic Speech Recognition with Weakly Labeled Data](https://arxiv.org/abs/2611.02476)

**<font color=#1a73e8>作者：</font>** Junzhe Liu, Yujie Tu, Yifan Yang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialectal Arabic speech recognition remains constrained by the scarcity of dialect-resolved transcribed speech despite the abundance of web audio. We introduce GigaSpeech 3, a corpus of 39,000 hours and 10 million weakly transcribed speech segments covering Algerian, Egyptian, Iraqi, Saudi, and Syrian Arabic. Starting from 60 hours of manual transcription per dialect, we train labeling models using speech-recognition-biased self-supervised learning and apply them to dialect-matched web audio. Data selection and four rounds of noisy-student refinement for Saudi and Syrian Arabic yield the final corpus. We validate its utility through dialect-specific and multi-dialect speech recognition training and cross-domain evaluation. On GigaSpeechBench, the final dialect-specific models outperform their labeling models across all five dialects and achieve a macro-average word error rate of 23.86%, a 16.6% relative reduction from the strongest third-party system covering all five dialects, while outperforming the best third-party result on three dialects. A multi-dialect model using self-predicted dialect identities achieves a macro-average word error rate of 25.51% while also supporting Modern Standard Arabic. Across eight conditions from three external corpora, a GigaSpeech 3-trained Zipformer achieves the lowest word error rate among six evaluated models in every condition, while adapting the Qwen3 speech recognizer on GigaSpeech 3 improves performance across all eight conditions. We release the corpus and recipes as a foundation for dialect-aware Arabic speech processing.

---


### 334. [Benchmark of THReD: Evaluating an LLM Agent and Its Preprocessing Tools for Turning Electronic Health Records into AI-Ready Datasets](https://arxiv.org/abs/2611.02484)

**<font color=#1a73e8>作者：</font>** Javad Mohammad Alizadeh, Huanmei Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly built into data-analysis software, yet little evidence shows how reliably they preprocess clinical data or whether the tools they invoke give correct, reproducible output. We report a benchmark of THReD, a web-based system that turns electronic health record (EHR) extracts into AI-ready datasets through a chat agent whose proposed steps run only after user confirmation. The agent benchmark has 141 tasks (100 templates) in seven categories, including goal-level requests, failure recovery, requests calling for no action, schema variation and prompt injection through the data, on synthetic tables calibrated to a regional health information exchange; success is judged by checks on the produced data. Over 2,550 episodes with Claude Haiku 5.5 in four context configurations, the deployed agent completed 92.7% (95% CI 88.1-96.4) of tasks on its first answer, abstained on every advice request, recovered from every injected fault, and never proposed an action requested by planted text. Without the data profile, completion fell to 58.0%; goal-level requests were hardest (80.6%). Six experiments on real records of two chronic-disease cohorts and on synthetic data at scale validate the tools: 91-92% of inferred patient classes and 99.7-99.8% of inferred vital-sign labels were correct in masked reconstruction; a dictionary builder combining curated dictionaries with LLM suggestions mapped 99.0% of 2,208 raw variants correctly; all 2,176 replays of 128 saved pipelines gave byte-identical files under pinned dependencies; subgroup differences in inference accuracy vanished within facility and lookup key; and the same-day consolidation rule changed 90-day emergency revisit rates by up to 3.2 points without shifting cohort composition by more than one point. Processing time grew roughly linearly to 5.5 million records while the prompt stayed at about 13 thousand tokens.

---


### 335. [Same Sentence, Different Construct: Identity-Swapped Rationales Reveal Measurement Non-Invariance in LLM Hate Speech Classifiers](https://arxiv.org/abs/2611.02491)

**<font color=#1a73e8>作者：</font>** Wenchang Wang, Yue Song  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as measurement instruments for socially consequential constructs such as hate speech, and are typically validated by their aggregate agreement with human labels. A valid instrument must also apply the same construct to every group it measures. We test this requirement using 421 \hc{} templates that are instantiated identically for seven protected groups, so that only the identity term varies. Four LLM classifiers each exceed 0.95 balanced accuracy, yet within identical templates two of them miss hateful statements about women at markedly higher rates than the same statements about other groups (excess false-negative rates of 8.3 and 4.4 percentage points), a gap first reported for fine-tuned classifiers in 2021. We show how the construct shifts. Comparing rationales within each template, we find that models invoke protected-group status for other groups but recast the identical statement about women as personal dislike or as aimed at an individual, in 22 of 30 missed templates for one model. Adding the benchmark's own definition, which lists sex as a protected characteristic, does not close the gap, and the contrast persists. Apparent false-positive disparities, by contrast, largely vanish under identity control and trace to reclaimed slurs present only for some groups. Errors shared by all models concentrate where model and benchmark definitions diverge, and pairwise counterfactual accuracy adds little beyond endpoint accuracy. We argue that validating LLM measurement requires identity-controlled tests of measurement invariance that examine both decisions and the criteria models state for them.

---


### 336. [Semantic Caches for LLM Web Services Leave Their Error Budget Unspent](https://arxiv.org/abs/2611.02498)

**<font color=#1a73e8>作者：</font>** Hanshuai Cui, Qianli Ma, Zhiqing Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Web services built on large language models (LLMs) receive many paraphrases of earlier queries, which a semantic cache answers from stored responses. A reused answer can be wrong, so wrong answers must stay below a share $\delta$ of the queries. Existing caches reuse above a fixed similarity threshold or, like vCache, learn a per-entry rule that bounds each query's error by $\delta$. However, fixed thresholds break the budget on new streams, and per-entry rules need labels on every entry before reusing it. We find an unspent error budget, as vCache realizes only 12-55% of $\delta$ on three public query streams. Surplus spends this budget where reuse is most likely correct. It ranks queries by a risk score shared across paraphrase clusters and opens risk bins as far as an audited error estimate allows. Free labels from every LLM call and a ledger of realized errors keep this threshold safe under drift. On five streams, including ORCAS search queries, Surplus holds $\delta$ in every test cell, which no baseline does. On the shuffled streams it serves 40% more hits than vCache, and its pooled hit rate beats the best baseline holding $\delta$ in each cell by 4.10 points. In a vLLM testbed it cuts the mean latency by 31.59% at the highest load, against 23.67% for vCache.

---


### 337. [SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding](https://arxiv.org/abs/2611.02501)

**<font color=#1a73e8>作者：</font>** Kunjun Li, Wenhao Chai, Yihao Liang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates memory-bound LLM decoding with a lightweight drafter, and parallel drafters extend this speedup by drafting a whole block in one forward pass. However, it remains unclear whether their released systems (stock) attain the full speedup that parallel drafting permits. We identify three challenges. First, with one request, each step accepts few tokens but reads every target weight. Second, with batching, per-request verification work roughly halves the speedup over autoregressive (AR) decoding. Third, speculative decoding is deployment-specific, and no universal optimization fits every serving regime, drafter, target model and GPU. To address these challenges, we present SpecPilot, an autonomous agentic loop that discovers algorithms and systems optimizations for each deployment. In each round, a cost model locates the largest gaps between the current system and its ceiling. Parallel agents explore directions and integrate the successful ones. Token forcing checks every output token against stock to detect reward hacking. A structured memory carries validated mechanisms to new rounds and deployments. SpecPilot discovered a general lossless 12-bit weight format, tree verification for hybrid recurrent targets, two-level verification and three batching mechanisms. We evaluate it across four target models, three drafters, two GPU platforms and five benchmarks. Without training or quality loss, it raises the speedup over AR from stock's 4.46$\times$ to 10.87$\times$ with one request, and from 1.94$\times$ to 3.93$\times$ with batching.

---


### 338. [Towards Multi-Value Alignment via Value Localization in LLMs](https://arxiv.org/abs/2611.02503)

**<font color=#1a73e8>作者：</font>** Xueqi Ma, Yanbei Jiang, Xingjun Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) with multiple, potentially conflicting human values remains challenging, as existing multi-objective alignment methods often require costly fine-tuning and provide limited insight into the internal mechanisms underlying value-related behaviors. In this work, we investigate multi-value alignment from a mechanistic interpretability perspective by identifying value-sensitive attention heads (value heads) in LLMs. Using a probing-based value localization framework, we discover sparse sets of attention heads associated with diverse dimensions, spanning both human values (e.g., harmlessness, honesty) and stylistic preferences (e.g., coherence, complexity). Analyses across multiple LLM families reveal functional specialization and structured interactions among value heads, including conflicts between certain values. Targeted head ablations further induce substantial, value-specific behavioral changes, providing causal evidence of their functional importance. Building on these findings, we propose an inference-time activation steering strategy that enables controllable alignment with individual values or combinations of values without updating the underlying model parameters, supported by theoretical analysis. Experiments across multiple value alignment benchmarks demonstrate effective single- and multi-value control while largely preserving non-target model performance. Our findings connect mechanistic interpretability with flexible multi-value alignment, offering a foundation for more interpretable and pluralistic LLM behavior. The code is available at this https URL.

---


### 339. [AttentionIndex: Accelerating Learned Sparse Attention with a Causal Inverted-File Index](https://arxiv.org/abs/2611.02508)

**<font color=#1a73e8>作者：</font>** Jeongmin Brian Park, Wen-mei Hwu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learned sparse attention, used in production models such as DeepSeek-V4 and GLM-5, lets each query attend to only k keys chosen by a lightweight indexer, but the indexer still scores every key in the prefix. At one million tokens, this selection takes more than half of prefill time. Two-stage selection over contiguous blocks, as in HiSA, reduces this cost, but its recall declines as context grows at a fixed candidate budget. We present AttentionIndex, which routes each query over an inverted-file index that groups indexer keys by similarity and refines the candidates with the native indexer score. AttentionIndex builds the index during prefill, making new keys searchable immediately, reusing previous clustering to keep maintenance cheap, and exposing each query only to clusters built from its own prefix. On GLM-5.3 and DeepSeek-V4-Flash at one million tokens, AttentionIndex delivers 1.3-1.8 times the prefill throughput of exhaustive selection, and at throughput within 5% of HiSA, it recovers 17.0 and 10.0 percentage points more of the exhaustive top-k, respectively. AttentionIndex also improves accuracy on long-context benchmarks by up to 18.4 percentage points over HiSA at the same candidate budget.

---


### 340. [A balloon effect: ban one channel and a hidden trait finds another](https://arxiv.org/abs/2611.02509)

**<font color=#1a73e8>作者：</font>** Keuntae Kim, Yong Suk Choi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models trained on the outputs of other models can acquire traits that those outputs never mention, such as a preference for an animal carried by lists of numbers. Such subliminal learning can pass on unwanted traits. The intuitive defence is to find and forbid the tokens through which a trait shows, but how a trait's trace behaves under such bans, and what of it a student learns, has not been resolved. We closed a trait's outlets one by one in two stress tests, a preference chain and a name chain, across two models, six output formats and 16 traits. Bans did not remove the trait. Much as squeezing a balloon in one place makes it bulge in another, the trait moved to wherever the format still allowed, an effect we call the balloon effect. Decomposing this transfer, which bans on surface features cannot stop, down to single heads and neurons, we show that it can be cut at the circuit that writes the trait into the output. Patching that circuit while the teacher writes numbers stopped the chains, sharply reduced the overt name leak and halved the trait passed to a student, whereas the same number of random heads produced no detectable reduction. These results give a mechanistic account of how unwanted hidden traits are transferred and a route to preventing it.

---


### 341. [MedHEB: Benchmarking Medical Embeddings Across Heterogeneous Clinical Evidence](https://arxiv.org/abs/2611.02519)

**<font color=#1a73e8>作者：</font>** Yingshu Li, Shaoyang Zhou, Zhanyu Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical evidence is inherently relational: medical images are interpreted with prior studies, cross-modal examinations, reports, and localized findings, and retrieving relevant evidence is therefore central to clinical interpretation. Recent foundation models increasingly encode these heterogeneous sources into shared embedding spaces, yet existing embedding evaluation often focuses on isolated matches, leaving unclear whether current models retrieve relevant evidence across changes in modality, appearance, and granularity. We introduce MedHEB, a unified benchmark with 107 retrieval tasks from 54 datasets, including both in-distribution and held-out-source evaluation, across three axes: evidence form (2D images, 3D volumes, text), pairing type (image--image, image--text, text--text, and modality-bridging visual matching), and relevance granularity (global, question-conditioned, region-level). Under a single ranking protocol, MedHEB varies clinically relevant evidence definitions to test whether embedding proximity remains meaningful across heterogeneous evidence, including modality-bridging visual retrieval and region-level text-to-region retrieval. Across representative models, performance is uneven across retrieval families: models strong on conventional image--text or text--text retrieval are less reliable on modality-bridging and region-level tasks. Current embedding spaces capture some clinical relationships well but do not yet provide balanced retrieval across heterogeneous evidence. We further provide MedEmb, an MLLM-based reference embedding model trained on the MedHEB ID split, as a reproducible baseline for unified 2D--3D--text medical retrieval. We release MedHEB with preprocessing scripts, evaluation code, access manifests, and MedEmb to support research on clinically meaningful medical embeddings.

---


### 342. [Tune the Baseline First: Most of Muon's Scaled Weight Decay Gain Is a Tuning Gap, but Its Small Real Advantage Grows With Model Size](https://arxiv.org/abs/2611.02529)

**<font color=#1a73e8>作者：</font>** Esther Xin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scaled weight decay for Muon (Muon-SW) has been reported to train language models more efficiently than constant decoupled weight decay, but such comparisons usually reuse one learning-rate (LR) and weight-decay (WD) setting for both methods. We re-run the comparison under the MAI-Base-2 protocol: LR and WD are tuned jointly through their product for each method, on a source-scaled mixture-of-experts (MoE) scaling ladder (1.9M to 15M active parameters) that holds tokens per active parameter and data repetition fixed across sizes. We find: (1) Most of the gain is a tuning gap. At the shared setting Muon-SW wins by 0.035 bits per byte (BPB), a 1.52x compute saving; after both methods are tuned, the gap is 0.0026 BPB (95% CI [0.0018, 0.0034]), a 1.03x saving, so about 90% of the advantage disappears. (2) The small advantage that remains is real: at the smallest size, all four paired seeds favour Muon-SW at the tuned settings. (3) That advantage grows with model size: across an 8x range of active parameters, the tuned gap rises from 0.0036 to 0.0051 BPB while the untuned gap shrinks from 0.035 to 0.024, so the surviving share rises from about 10% to 21%. (4) The best weight decay moves with scale: the optimal LRWD product grows for both methods, faster for Muon-SW (ratio 1.40 to 1.91), and a law fitted on the two smallest sizes overshoots the third by 1.3-1.5x, costing up to 0.002 BPB. The whole study runs on one NVIDIA T4 GPU; we release the code and all run results.

---


### 343. [FORGE: Fault-Oriented Rework Code Generation for Executable Interlocking Assembly](https://arxiv.org/abs/2611.02536)

**<font color=#1a73e8>作者：</font>** Fuqiang Wang, Jiahao Fu, Ren Hefeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have demonstrated strong capabilities in structured reasoning and code generation, yet identifying an assembly fault does not guarantee the ability to generate executable rework programs. In interlocking assemblies, a locally plausible repair program may violate blocking dependencies, omit required recovery operations, or terminate in an incorrect configuration. We identify this challenge as fault-conditioned executable rework generation, where models must jointly reason about structural failures and generate programs that restore constrained assembly states. To benchmark this capability, we introduce FORGE-Bench, containing 4,000 tasks across 26 interlocking assemblies with five assemblies held out for evaluating generalization to unseen structures. We further propose FORGE (Fault-Oriented Rework Code Generation for Executable Interlocking Assembly), a structured state-to-program framework that decomposes rework generation into Rework Structuring and Action Grounding. Rework Structuring captures fault-induced recovery dependencies, while Action Grounding maps these dependencies into state-conditioned executable actions. Experiments show that locally reasonable repair code is insufficient for reliable assembly recovery, and that connecting structural recovery reasoning with executable action realization is essential for verified target restoration.

---


### 344. [PixelBench: Can LLMs Understand and Generate Images Pixel by Pixel?](https://arxiv.org/abs/2611.02540)

**<font color=#1a73e8>作者：</font>** Haoquan Zhang, Feiyang Liu, Juanxi Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate visual assets through text-based formats such as SVG and CAD, but these symbolic representations describe images using high-level primitives rather than explicit raster values. We ask whether LLMs can instead generate pixel images directly through their existing vocabulary, without a learned image tokenizer or decoder. We introduce PixelBench, a benchmark for text-to-pixel (T2P) and image-to-pixel (I2P) generation across multiple resolutions, together with a complementary pixel-understanding evaluation. Models generate an RGB color palette followed by a grid of indices specifying the palette color of each output pixel. In T2P, the strongest models produce recognizable images directly from text. In I2P, the strongest models outperform palette-matched downsampling and specialized pixelization algorithms at low resolutions. Pixel-understanding performance correlates strongly with generation performance. A resolution-scaling study shows that pixel-generation performance often improves initially before declining at high resolutions. Finally, we introduce Pixel Reconstruction Tuning (PRT), which augments visual instruction tuning with caption-palette-grid trajectories. We post-train Molmo2-4B from its pretraining checkpoint by mixing general instruction data with our curated PRT data, improving performance across 16 visual-centric benchmarks, indicating that explicit pixel reconstruction can provide useful auxiliary supervision.

---


### 345. [Organizational Learning in Materials Discovery Campaigns: Which Databases, Calculations, and Agent Teams Pay Off](https://arxiv.org/abs/2611.02571)

**<font color=#1a73e8>作者：</font>** Kinston Ackölf, Taylor D. Sparks  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> More databases can make a materials campaign worse. Through an organizational lens, we trace each source's contribution. One band-gap campaign ranks seven anion families from archived measured gaps, one vote per source. In the first half of its budget, all seven pooled rank worse (rank agreement 0.737; 1 = measured order) than the best pool of three (0.851). As a stability check, choosing the pool on half the runs and testing on the rest kept the gap. Splitting Materials Project afterwards points to its transition-metal oxides and fluorides. Two databases from one pipeline add nothing over one, but pooling gives their shared ordering two votes. New calculations repay their cost early only when two or three campaigns reuse them. Flat language-model agent teams trailed a random-pick baseline (mean 0.876, sd 0.096, 20 searches). An adaptive Al-Mg-Si team, mostly interatomic potentials, was scored on unseen HSE06 calculations. In its first quarter of compute it found 49% of the ten lowest-formation-energy compounds, against at most 40% for fixed teams and 73% for MACE-MP-0 alone. Merging members whose orderings agreed carried most of its gain. This suggests pooling a few sources that fit the measurements, counting each pipeline once and charging for computation.

---


### 346. [RLVR Sharpens the Pencil, Not the Mind](https://arxiv.org/abs/2611.02574)

**<font color=#1a73e8>作者：</font>** Shreeyam Bangera, Manya Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Models like DeepSeek-R1 made Reinforcement Learning with Verifiable Rewards (RLVR) famous: reward a model for correct answers and it gets dramatically better at reasoning without being taught how. The leading explanation is sharpening---that the base model already knows how to solve these problems and RLVR just makes it more likely to reach for its best solution paths. This has only ever been checked by comparing before and after training, never by watching what changes inside across it. We tracked OLMo-2-1B across all 13 training checkpoints on GSM8K. First-try accuracy climbs from 58.0% to 61.3%, but ask the model 256 times and solution coverage actually rises from 94.5% to 96.9%, proving the knowledge was already there. We then planted reasoning mistakes into problems and trained simple probes to detect them. Those probes held between AUROC 0.798 and 0.840 across all 13 checkpoints and 3 error types, a spread smaller than the confidence interval; the model never builds a sharper internal picture of what a reasoning mistake looks like. The one place we find real internal change is at the final answer token, where a probe distinguishing early from late checkpoints hits an AUROC of 0.93, while the same probe on the actual reasoning steps lands near chance. RLVR makes the model lead with its best thinking. It does not change what that thinking is.

---


### 347. [SMILE: A Structured Multi-Agent Clinical Reasoning for Liver Ultrasound Understanding](https://arxiv.org/abs/2611.02581)

**<font color=#1a73e8>作者：</font>** Haris Ghafoor, Minjee Seo, Seonaeng cho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated liver ultrasound report generation improves the diagnosis of liver diseases by producing clinically structured descriptions of anatomical and disease-related findings. However, current generative vision-language models (VLMs) often rely on a single reasoning pathway that maps ultrasound appearance directly to textual descriptions. In addition to the inherent vision-language modality gap, this design is limited for liver ultrasound because disease interpretation is constrained by subtle visual evidence, heterogeneous disease patterns, and limited paired supervision. To address these limitations, we propose SMILE, a Structured Multi-agent clInicaL rEasoning framework that uses multiple complementary specialist agents to interpret ultrasound images and consolidates their outputs through a judge-guided consensus mechanism. Our approach employs three specialized agents: an image interpretation agent for morphological descriptions, a clinical-stage reasoning agent, and a visual question answering (VQA) agent for targeted queries. These agent responses are then aggregated and scrutinized by a judge VLM using a consensus filtering prompt to produce a unified, clinically coherent output. Across a public liver ultrasound dataset and an internal clinical dataset, SMILE consistently outperforms state-of-the-art VLMs, achieving up to 19.0\% improvement in ROUGE-1 and 18.8\% improvement in clinical F1-score, while reaching VQA F1-scores of 0.82 and 0.65 on public and internal datasets, respectively. These results demonstrate the potential of SMILE for data-scarce and limited-supervision clinical settings. Our models, datasets, and code are available \href{this https URL}{here}.

---


### 348. [BasisKV: Value Latents for Communication and Key Routing](https://arxiv.org/abs/2611.02583)

**<font color=#1a73e8>作者：</font>** Lixun Zhang, Zishan Shao, Kangning Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context large language model (LLM) inference is increasingly constrained by the cost of maintaining an ever-growing KV-cache. Low-rank K/V projections provide a promising way to compress the KV-cache with minimal quality loss, but prior work has largely optimized KV-cache compression in isolation, leaving distributed inference, especially with tensor parallelism where attention computation is partitioned across multiple GPUs, largely underexplored. We make two observations: (i) tensor-parallel communication is an important cost when deploying low-rank KV-cache compression in distributed inference; and (ii) Value compression can be associated with the output projection, allowing the same low-rank Value representation to reduce both Value-cache width and tensor-parallel communication. Based on these observations, we propose BasisKV, a low-rank KV-cache compression method for communication-intensive, long-context LLM inference. BasisKV jointly optimizes the low-rank factors across per-GPU attention partitions against the complete attention output, rather than fitting each partition in isolation. The compressed Value cache is further reused to help identify which Key pages should be accessed: it predicts part of the Key information needed for routing, while a Key-specific residual stores what cannot be recovered from Value. The original Keys are then retrieved only for the selected pages to compute exact QK scores. Across multiple LLM families and system settings, BasisKV achieves a better quality--efficiency tradeoff than existing low-rank baselines, reaching up to 1.42x end-to-end speedup under 8-GPU tensor-parallel inference. Our code is available at this https URL

---


### 349. [From Language to Country to Valence: A Multilingual Audit of Stereotype Bias Across LLMs](https://arxiv.org/abs/2611.02585)

**<font color=#1a73e8>作者：</font>** Zihao Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly considered for education, recruitment, workplace decision support, and other consequential applications, making pre-deployment social-bias detection essential. Yet major benchmarks are English-centred or translated, focus mainly on negative stereotypes, and may miss linguistic and cultural variation. We investigate gender, racial, and religious bias using 12,000 locally written Reddit posts in English, Spanish, French, and German. Only search terms are translated, preserving local context. The dataset is balanced by language and category; English gender is additionally balanced by stereotype valence. Three open-weight and three proprietary API-based models are evaluated with a two-blank design that reduces grammatical-gender cues. Religion has the highest absolute choice imbalance in every model-language condition. Spanish is highest for gender, whereas German is highest for race and religion. The evaluated API models score below the open-weight models throughout. Negative English-gender items exceed positive items; Australian and Mexican contexts exceed their Canadian and Spanish counterparts. These descriptive differences measure choice concentration, not stereotype endorsement or causal country effects. The crossed patterns show how aggregate scores can conceal category- and context-specific behaviour, motivating closer inspection before deployment.

---


### 350. [They Know Where It Is, But Not What It Says: A Bilingual Hallucination Benchmark of Hadith Recall in Open LLMs](https://arxiv.org/abs/2611.02587)

**<font color=#1a73e8>作者：</font>** Dayam Nadeem, Safdar Mustafa, Ameen Ur Rehman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly consulted for religious knowledge, including the recall of specific Hadith (recorded sayings and actions of the Prophet Muhammad, peace be upon him). Unlike open-ended generation, Hadith recall is a high-stakes, verifiable task: a reference (collection, chapter, and Hadith number) has exactly one correct text, and any deviation from it constitutes a fabrication that can be mistaken for authentic scripture. This study introduces a bilingual (English/Arabic) benchmark that probes five open-weight, locally-deployable language models (Mistral-7B, Gemma3-4B, Jais-7B, ALLaM-7B, and Phi4-mini-3.8B) across all six canonical Sunni Hadith collections (Sahih al-Bukhari, Sahih Muslim, Sunan Abi Da'ud, Jami' al-Tirmidhi, Sunan an-Nasa'i, Sunan Ibn Majah), sampling 500 Hadith per collection (3,000 per model per language, 30,000 responses total). Each model is given only the bibliographic reference and asked to reproduce the exact Hadith text, with no retrieval augmentation, and is scored on lexical fidelity (BLEU) and semantic fidelity (multilingual cosine similarity), with refusals flagged separately. Across all five models and both languages, 0% of 30,000 responses achieve both high lexical and high semantic fidelity, i.e., an exact, verifiable match to the source text. Arabic responses fare uniformly worse than English. These findings suggest that current open-weight LLMs, used without retrieval grounding, are unreliable and potentially dangerous sources for exact religious-text recall, and that deployment for Islamic scholarship should mandate retrieval-augmented generation over a verified corpus rather than parametric memory. The complete code, prompts, evaluation pipeline, and scored outputs are publicly available at this https URL.

---


> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
