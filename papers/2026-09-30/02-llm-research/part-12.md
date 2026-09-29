# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**551-600**（第 12/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 551. [From Attack Success to Attack Severity: Counterfactual Memory Attacks on LLM Agents](https://arxiv.org/abs/2609.34132)

**<font color=#1a73e8>作者：</font>** Mingxi Zou, Langzhang Liang, Zhuo Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents increasingly rely on persistent memory for long-horizon and personalized behavior, they can retain and reuse information across interactions, but this also creates a lasting channel through which malicious memory writes can influence future behavior. Persistent-memory attacks are typically evaluated by whether they succeed, yet successful attacks can leave persistent states with substantially different downstream consequences. We study this severity as a distinct attack-design objective and formalize it with counterfactual memory regret (CMR), the paired increase in expected downstream loss relative to clean memory. We introduce MemHarm, which predeclares a finite class of sparse, grounded semantic edits, evaluates candidates through the normal agent memory interface using offline paired-loss feedback, and certifies resolved selections within that class. Compared with attack-success optimization, CMR-guided selection produces substantially larger downstream loss while retaining most of the success-rate gain. Across two agent benchmarks and diverse memory designs, MemHarm attains the highest CMR point estimates among the evaluated general attacks on identical support. Factor-removal interventions link this harm to the selected semantic factor, and native-agent deployments verify the write-to-fresh-process attack path.

---


### 552. [StateGuard: Analytical-State Management with Validity-Aware Intervention for Long-Horizon Data Agents](https://arxiv.org/abs/2609.34134)

**<font color=#1a73e8>作者：</font>** Wenle Liao, Zhao Wang, Jingchao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents have shown strong capabilities in automated data analysis and are increasingly moving toward long-horizon, multi-stage analytical workflows. However, as the analytical process evolves, constraints, variables, and conclusions remain implicitly embedded in interaction histories, making it difficult for agents to track which analytical artifacts remain valid over increasingly long horizons and changing dependencies. Consequently, stale artifacts may be silently inherited, propagating errors to downstream stages. To address this challenge, we propose StateGuard, an analytical-state validity management framework for long-horizon data agents. StateGuard externalizes evolving analytical progress into a state graph containing constraints, versioned variables, intermediate conclusions, and cross-state relations, treating each state as an executable, verifiable, and traceable object rather than textual memory alone. StateGuard maintains state validity through evidence-grounded verification and hierarchical intervention. To equip StateGuard with these capabilities, we first introduce Manager-Oriented Counterfactual Supervision, which constructs 3K state-centric trajectories through counterfactual runtime synthesis to fine-tune StateGuard for state maintenance, verification, and repair. We then apply Validity-Guided Policy Optimization, using runtime validity evidence to provide fine-grained learning signals for protocol correctness, state grounding, and intervention quality. Experiments on three diverse long-horizon data-analysis benchmarks show that StateGuard consistently improves data-agent performance while reducing dependency-induced downstream error propagation, demonstrating the advantages of explicit analytical-state management for reliable long-horizon data analysis.

---


### 553. [Evo2Team: When Do Evolved Skills Transfer? From Selection to Deployment](https://arxiv.org/abs/2609.34135)

**<font color=#1a73e8>作者：</font>** Renxiang Wang, Jiaming Cui  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A skill bank that helps one multi-agent system may leave another's behavior unchanged. A transferred rule helps only when target agents act on it successfully. We study this path for routing and communication skills in Count-Frequency and AgentsNet, using teams of 4--32 agents and GPT and Qwen model ladders. Source evolution meets a joint quality, cost, model-tier, and confirmation goal in 14 of 16 settings. We then evaluate Evo2Team, which selects, adapts, and confirms source skills for the target team, alongside six frozen selectors across 28 transfer directions. Evo2Team's target-side exploration cost is below that of evolving a new target bank in every direction, even when reused reference evaluations are charged once. Twenty of 28 held-out outcomes meet the positive-transfer criterion, including three saved diagnostic tests. Selection alone does not explain these outcomes: KNN and CORAL choose different banks in two AgentsNet directions but produce identical recorded executions. When Evo2Team changes execution, gains can reach many tasks, as in a Count-Frequency direction that improves 28 of 32 tasks over KNN. Seven positive AgentsNet outcomes save 6.1--14.6\% in deployment cost while using transferred skills on only three to six of fifteen tasks. In five earlier accepted directions, all 22 task records using transferred skills pass three fixed-graph confirmations, but four fail in recorded executions on new graphs. Graphs and model responses change together in this comparison. These results show that skill transfer must be assessed through the actions agents take, the tasks those actions reach, and the quality and cost of the final deployment.

---


### 554. [Waggle: Learning One Anonymous Local Law for Self-Organizing LLM Swarms](https://arxiv.org/abs/2609.34136)

**<font color=#1a73e8>作者：</font>** Mingxi Zou, Wei Zhu, Zhuo Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents increasingly collaborate on complex tasks, how to organize their interactions becomes a central design question. Existing multi-agent systems typically learn or adapt explicit roles, hierarchies, routing policies, or communication topologies. We shift the learning target to a reusable local law that can be shared across interchangeable agents and adapt coordination as populations or interaction conditions change, without redefining a global organization. We introduce Waggle, a shared anonymous policy over bounded local views that jointly selects task actions, semantic communication, and local commitment updates. Repeated execution of the same law allows coordination to form, persist, and reorganize online without explicit roles or global topology. To learn this law across interchangeable agents and evolving coordination, we develop Swarm-Consistent Distillation (SCD), combining anonymous-orbit consistency with rollout-grounded prediction of the next local coordination field, with no added inference-time components. Across diverse coordination settings, the same learned law remains effective as populations and interaction budgets change, retains over 96% of substrate-specific oracle quality, and transfers without retraining; SCD further improves reorganization after counterevidence. Together, these results show that LLM-agent organization can emerge and adapt through repeated execution of a learned local law.

---


### 555. [Same Tasks, Different Apps: Why Mobile GUI Agents Fail to Generalize?](https://arxiv.org/abs/2609.34139)

**<font color=#1a73e8>作者：</font>** Tien Tran, Namho Koh, Daiki E. Matsunaga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents deployed in real settings must work across different applications that support the same functionality. Most existing benchmarks test each task in only one app, so a high score can mean the agent understands the task, or only that it knows that particular app. We introduce AnyAppBench, a category-controlled live Android benchmark that evaluates cross-application generalization while keeping the user goal fixed. It spans 10 functional categories, 100 task templates, and 520 task--application pairs over 52 applications. Agents run from raw instructions and with app-independent sub-goals, and a VLM judge labels every failed run under a fixed failure taxonomy whose reliability is measured by human annotation. We find that, across 13 agents, success on the original application does not transfer reliably to new applications with the same goal. Furthermore, providing high-level sub-goal decomposition produces only small, category-dependent changes that do not close the gap, and the mix of failure types changes with the target interface. Based on those insights, we believe the AnyAppBench benchmark provides an important stepping stone toward robust real-world deployment of mobile GUI agents. Our code, data and the leaderboard can be found at the project website this https URL.

---


### 556. [Geometric Encoding for Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2609.34148)

**<font color=#1a73e8>作者：</font>** Antonio Jun, Haoshui Yu, Zhengyi Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are far more reliable at recognizing what appears in a video than at reasoning about its spatial and temporal properties, such as metric distances, object dimensions, and consistent object identities across frames. We present Geometric Code, a perception-to-geometry pipeline that computes explicit spatial structure from video and supplies it to VLMs as context to augment reasoning. A perception layer segments and classifies objects and recovers depth, camera pose, and intrinsics from monocular RGB video. A deterministic geometric engine then back-projects, merges, and cleans these outputs into a spatial code, including per-object positions, dimensions, counts, inter-object distances, appearance order, and room geometry. The code is serialized into VLMs' prompts, either alongside the video or replacing it entirely. Specifically, there is no component trained or fine-tuned in our approach. On VSI-Bench, augmenting 2B and 4B open models with the spatial code improves average accuracy by +4.1 points over the frames-only baseline, with the largest gains on numeric estimation tasks such as absolute distance (+24.1 points). The results suggest that explicitly computed geometry, delivered through the language channel, recovers spatial competence that small VLMs cannot extract from pixels alone.

---


### 557. [Quantitative Measurement of Language Distance among Closely Related Indo-European Languages Using Pretrained Language Models: A Case Study on the North Germanic Branch](https://arxiv.org/abs/2609.34152)

**<font color=#1a73e8>作者：</font>** Yiping Bai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Among closely related North Germanic languages, the quantification of language distance has traditionally relied on qualitative methods, lacking a unified multi-dimensional computational framework. Multilingual pretrained models based on the Transformer architecture can map texts from different languages into a shared vector space, enabling quantitative measurement of language distance. This paper focuses on the three North Germanic languages---Danish, Norwegian (Bokmål), and Swedish---and proposes a three-metric quantitative framework based on pretrained language models: (1)~sentence-level semantic distance, computed as cosine similarity between LaBSE and mBERT encodings of parallel sentences; (2)~orthographic fragmentation rate, measuring subword tokenization efficiency when cross-applying monolingual BERT vocabularies to parallel texts; (3)~MLM predictability, comparing prediction confidence and entropy in masked language modeling using mBERT across languages. Using 150 trilingual parallel sentence triplets from the Tatoeba corpus as controlled samples, we obtain consistent distance rankings on two independent models: LaBSE: da--no $0.012 < $ no--sv $0.016 < $ da--sv $0.020$; mBERT: da--no $0.016 < $ no--sv $0.045 \approx $ da--sv $0.046$. This ranking is consistent with the historical linguistic conclusion that ``400 years of Danish rule over Norway (1380--1814) led to highly cognate written languages.'' The three metrics---semantic, orthographic, and predictability---converge on the same conclusion, providing a reproducible computational framework for the quantitative study of distance among closely related languages, extensible in principle to more branches of the Indo-European language family, pending validation on additional language groups.

---


### 558. [TableSeek: Structure-Preserving Agentic Evidence Seeking over Heterogeneous Table Corpora](https://arxiv.org/abs/2609.34157)

**<font color=#1a73e8>作者：</font>** Jiaming Tian, Liyao Li, Wentao Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-domain table retrieval seeks tables that contain sufficient evidence for answering a question or verifying a claim. Yet semantic relevance is often misleading: topically similar tables may lack the required facts, while answer-bearing evidence is often confined to a few cells whose meaning depends on surrounding schema and table context. Heterogeneous schemas, value formats, and serializations further weaken one-shot matching.
We present TableSeek, a structure-preserving agentic search framework for heterogeneous table corpora. Instead of ranking tables once, an LLM agent iteratively follows sparse clues, inspects schema-preserving previews, identifies schema- and value-level mismatches, and refines its investigation. TableSeek uses cells and schemas as evidence anchors while retaining complete tables as evidence units, enabling fine-grained localization without losing the context required for interpretation and answerability checking.
Without relying on retriever training or a precomputed semantic index, TableSeek produces transparent evidence-seeking trajectories and achieves competitive end-to-end performance against strong retrieval-and-reranking pipelines on heterogeneous table benchmarks. These results suggest that active, structure-preserving evidence seeking is a promising paradigm for open-domain table retrieval.

---


### 559. [Toward a Graded Measure of Belief Stability in Large Language Models](https://arxiv.org/abs/2609.34158)

**<font color=#1a73e8>作者：</font>** Samantha Dies, Branden Fitelson, Tina Eliassi-Rad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly mediate how people access and reason with information, yet factual reliability is usually evaluated one judgment at a time. We introduce graded belief stability, a relational measure of how well a belief persists within an LLM's broader belief system. Unlike individual belief probability, it asks whether support for a claim persists when that claim is considered alongside the model's other epistemic commitments. We operationalize this idea with a Direct Conditional estimator that uses internal model representations to estimate conditional belief probabilities. Across 12 LLMs and three domains, lower-stability beliefs exhibit greater mean behavioral movement under conversational challenge in 83.3% of model-domain settings after matching on individual belief probability. Graded belief stability therefore extends reliability assessment beyond how strongly an LLM supports a claim to how robustly that belief is supported within its broader system of beliefs.

---


### 560. [RoutePrism: Tracing Construction Order Effects in Agent Memory](https://arxiv.org/abs/2609.34160)

**<font color=#1a73e8>作者：</font>** Dong Xu, Zhangfan Yang, Jiantao Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Processing the same records in a different order can discard different evidence, yet endpoint accuracy alone cannot reveal what changed or whether it mattered. We introduce RoutePrism, a diagnostic protocol that builds memory twice from the same source pool in two processing orders, then traces which sources, compiled contexts, and answers differ. Because record content, timestamps, policy, and the answer model all stay fixed, any observed difference is localized to the memory construction step. A matched four-condition intervention tests whether a record displaced by reordering actually carried task-relevant evidence: restoring that single record recovers over 60 percentage points of lost accuracy, while substituting a non-supporting record of equal length does not. We evaluate the protocol on PersonaMem-32K (63 primary queries, 29 users) and 470 LongMemEval-S questions with histories spanning 38 to 62 sessions, replicating the core intervention across five answer models. Survivor selection, defined as the choice of which record a cluster retains, drives most source-level changes, while different memory policies (compaction, bounded recency, MemoChat-style summarization, A-MEM) produce distinct failure signatures at the source, context, and metadata layers.

---


### 561. [ReplayLens: Auditing Agents' Use of Outcomes](https://arxiv.org/abs/2609.34177)

**<font color=#1a73e8>作者：</font>** Dong Xu, Zhangfan Yang, Jiantao Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an agent reuses logged experience, a changed decision may reflect the recorded score, the action's name, or the record's position in storage. Standard memory evaluations do not reveal which relationship drives that change. We introduce ReplayLens, a black-box audit that changes one relationship in the stored history at a time, holds the remaining interface fixed, and measures the resulting decision. Four interventions target four relationships. Outcome reassignment swaps which scores belong to which actions. Pair transport moves intact action-score pairs to new record slots. Consistent renaming relabels actions in both history and menu. Key-slot reassignment changes both score attachment and position. A constructive separation shows why the audit is needed: two memory writers with identical endpoint accuracy respond differently to the same replay, so conventional evaluation cannot resolve the underlying dependence. On black-box LLM interfaces, swapping scores changes decisions while moving intact pairs does not, separating score attachment from record order. A bounded-memory study exposes ingestion-order sensitivity that endpoint comparison misses. In sequential experiment planning, altered historical scores redirect exploration and reduce final utility despite fresh measurements. A code-debugging agent with sealed hidden tests shows the same pattern outside model selection. ReplayLens provides a relationship-level audit for deciding whether logged experience can be merged, reordered, or reindexed safely.

---


### 562. [RAGWarrant: Evidence-Preserving Governance for RAG Policy Promotion Under Quality, Cost, Latency, and Risk Constraints](https://arxiv.org/abs/2609.34179)

**<font color=#1a73e8>作者：</font>** Richard Krueger, Lucas Krause, Zach Pocquette  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation systems are extensively instrumented with metrics, benchmarks, traces, and automated judges, but these tools do not decide whether a proposed policy change is safe to release. We present RAGWarrant, an open-source promotion-control framework that treats deployment as a constrained evidence decision rather than a leaderboard choice. RAGWarrant normalizes evaluator outputs and operational telemetry, applies predeclared quality and hard-risk gates, assigns evidence-class claim ceilings, preserves negative outcomes, and emits auditable PROMOTE, BLOCK, REJECT, or INCONCLUSIVE decisions. We evaluate the framework across T2-RAGBench, MultiHop-RAG, CRAG, HotpotQA, synthetic reproduction, and bounded local generative experiments. On HotpotQA, operational savings were blocked because answer quality fell beyond the declared margin. A bounded CRAG study selected a lower-cost quality-tied policy, but related generative gains were unstable and a held-out guardrail failed closed. We claim an auditable promotion-control abstraction, not optimizer superiority, human validation, or production readiness. The tagged artifact reproduces from a fresh clone, runs as a hardened Docker job, accepts external evaluator exports, and verifies artifact integrity.

---


### 563. [Decision Readouts for Text-Mediated Video Anomaly Detection: An Exploratory Evaluation of Jev and Qwen](https://arxiv.org/abs/2609.34180)

**<font color=#1a73e8>作者：</font>** Xukui Qin, Youting Wang, Xinjie He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How much does the decision readout matter when video-derived textual evidence is held fixed? We evaluate Jev typed decisions and three Qwen readouts on a sparse development sample of 40 videos and 400 target anchors from UCF-Crime and XD-Violence, each presented as a summary and ordered captions. Each dataset contributes 20 source groups and 200 anchors, including only 10 and 37 positives, respectively. The original five-backend pilot requested 4,000 predictions; Jev Choice returned 776 valid responses out of 800 under the study's strict numerical policy, blocking its full-coverage quality comparison. On XD captions, Jev Noul achieved 75.99% average precision versus 48.47% for Qwen generated probability and 57.81% for the stronger local ordinal-likelihood expectation. The latter paired difference was 18.18 percentage points (95% source-group bootstrap interval 5.53-31.50). UCF did not show a corresponding advantage: caption ROC-AUC was 52.26% for Noul and 65.95% for ordinal likelihood. Both probability readouts had higher, hence worse, UCF Brier scores than the evaluation-prevalence reference of 0.0475. We additionally audit historical LAVAD scores at exactly matched anchors and distinguish response structure from numerical consistency. A binary-likelihood control is missing. These exploratory offline results characterize ranking, probability quality and interface failures; they establish neither a causal typed-interface benefit nor general superiority, calibration or end-to-end acceleration.

---


### 564. [CRF Loss is How Networks Should Learn Boundaries in Weakly Supervised Segmentation](https://arxiv.org/abs/2609.34183)

**<font color=#1a73e8>作者：</font>** Joshua Li, Yuri Boykov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly Supervised Semantic Segmentation (WSSS) learns pixel-level predictions from image-level tags. Recent work focuses on improving coarse CAMs extracted from large vision-language models (commonly CLIP), but does little to improve their accuracy along segment boundaries. That job is instead delegated to a post-processing method like DenseCRF. However, because DenseCRF relies on low-level colour cues, it can flip correct labels to incorrect ones when neighbouring pixels share similar colours. SAM has recently been adopted as a natural alternative, yet it simply takes on DenseCRF's role as an intermediate "refinement" step that outputs one-hot pseudo-labels in prior work. By discarding the valuable uncertainty in CAMs, these one-hot pseudo-labels turn borderline errors into confidently wrong targets. Our key insight is that CAMs should supervise training alongside SAM boundaries, each through its own loss, rather than being fused together into a single hard target. Inspired by CRF potentials, we propose a framework that disentangles soft pseudo-labels as unary supervision and binary edge maps as pairwise supervision. We realize our framework in a single-stage model, DS-CRF, using CAMs from this http URL and boundaries from SAM. DS-CRF sets a new state-of-the-art of 56.5% mIoU on MS COCO.

---


### 565. [CASS: Contribution-Aware Structured Sparsity for Model Merging](https://arxiv.org/abs/2609.34184)

**<font color=#1a73e8>作者：</font>** Yan Li, Guiping Cao, Meng Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model merging integrates task-specific fine-tuned models into a single multi-task model, but often suffers from parameter interference caused by conflicting task-vector updates. Existing methods typically mitigate conflicts by pruning task vectors based on weight magnitude or random heuristics, treating Transformers as unstructured ``bags of parameters'' and overlooking their inherent modularity. In this paper, we propose \textbf{C}ontribution-\textbf{A}ware \textbf{S}tructured \textbf{S}parsity (CASS), a unified framework that reduces parameter interference by identifying and preserving task-specific components. At the core of CASS is a contribution-aware structured mask that identifies task-relevant attention heads and FFN neurons. We instantiate this mask in two settings: CASS-Merging, the primary post-hoc setting where masks serve as a plug-and-play denoising filter for existing merging operators, and CASS-Tuning, an extension for scenarios with fine-tuning access where masks constrain gradients to reduce structural overlap between task vectors. Our analysis shows that task-relevant components are sparse and partially disjoint, supporting structured component-level filtering as an effective way to reduce merging interference. Extensive experiments across vision (ViT, 20 tasks) and language (RoBERTa, 8 tasks; Qwen2.5, 4 tasks) benchmarks demonstrate that CASS improves a range of representative merging baselines.

---


### 566. [LLMs are not stochastic parrots: Evidence for meaning-mediated abstraction from conlang-like tasks](https://arxiv.org/abs/2609.34187)

**<font color=#1a73e8>作者：</font>** Julia Witte Zimmerman, Calla G. Beauregard, Tabia Tanzin Prama 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The strong version of the stochastic parrot argument claims that, although large language models (LLMs) may exceed rote regurgitation, they cannot move beyond statistical pattern matching into abstraction or reasoning, remaining ontologically near the lower bound of pattern reuse despite producing alluringly fluent text. We test this hypothesis using conlang-like tasks. Several LLMs are given only natural-language descriptions of fictional languages that subvert prominent superficial patterns in training data by combining statistically uncommon and unattested features. Crucially, no example outputs are given. We argue that if the models exhibit rule-following behaviour, they cannot be relying solely on superficial statistical patterns; such patterns often work against the correct output. Instead, successful performance requires representations of the constraints specified in the prompt. Across three complementary task families, models systematically move in the meaning-predicted direction: they distinguish prompt exposure from instructed use, alter semantic relationships in response to novel constraints, and sometimes produce exact matches to complex translation answer keys. Although performance varies across the spectrum of models used, these results provide evidence for meaning-mediated abstraction in LLMs and refute the strong stochastic parrot hypothesis. Our work shows that, under appropriate architectural and contextual constraints, statistical learning can produce meaning-mediated abstractions, although generation remains strongly constrained by superficial plausibility. We discuss implications for model development and for understanding how increasingly abstract representations may emerge from plausible-text-generation objectives.

---


### 567. [PainterBench: A Figural Divergent-Thinking Benchmark for Tool-Using Language Models](https://arxiv.org/abs/2609.34195)

**<font color=#1a73e8>作者：</font>** Shane K.A. Dalumura Hettige, Jonas Oppenlaender  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Figural divergent thinking is the ability to develop a given shape fragment into an original drawing. In humans, this ability is assessed with incomplete-drawing tasks. We introduce PainterBench, a benchmark that ports the incomplete-drawing task to the agentic setting. The agent draws on a canvas through tool calls and observes the result after every turn. The canvas includes a starting shape which cannot be erased, and the agent's goal is to incorporate this shape into the most original drawing it can produce. The task is open-ended, and the agent itself decides when the drawing is finished. The benchmark tests incremental visual planning over a short horizon and the transfer of creative ability from pretraining to multi-turn tool use. We evaluate 14 multimodal language models from small to frontier scale. Across the primary study and six sensitivity analyses, we collect 2,700 drawings and crowdsource creativity and recognizability ratings for every drawing and for 300 human reference drawings. We also present ViDrA-adapted, an automated scorer that predicts human creativity ratings of agent drawings (r = 0.85 on random held-out test split). Figural divergent thinking varies widely across the 14 models, and GPT-6 Astra produces the most creative drawings. Relative to the human drawings, the agent drawings score higher in creativity but lower in recognizability. We release the final drawings, per-round canvas snapshots, tool call traces, stimulus bank, benchmark harness, crowdsourced ratings (N = 72,000), and ViDrA checkpoint.

---


### 568. [ConvCue: Complementary Visual Inductive Biases for Vision-Language Models](https://arxiv.org/abs/2609.34196)

**<font color=#1a73e8>作者：</font>** Zixuan Lan, Shichu Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision-language models (VLMs) achieve strong performance across a broad range of multimodal tasks, yet still struggle with visual questions that require fine-grained discrimination and spatial understanding. These limitations motivate investigating whether supplementary visual representations can improve existing VLMs without replacing their native visual encoders. Pretrained convolutional networks offer a candidate feature source, motivated by their local connectivity and spatial weight sharing. We introduce CONVCUE, which augments the native visual representations of a pretrained VLM with final-stage features from a parallel, frozen pretrained CNN. A learnable adapter maps convolutional features to the native visual feature dimension, while gated cross-attention allows the original visual tokens to retrieve information from the CNN features. The enhanced tokens are passed through the original visual-to-language projector, and the model is adapted through a two-stage training procedure. We evaluate CONVCUE on Qwen3-VL-2B, Qwen3-VL-4B, and LLaVA-OneVision-7B across 13 multimodal benchmarks covering visual question answering, document and chart understanding, and multimodal reasoning. CONVCUE improves average benchmark performance over both the original models and matched two-stage fine-tuning controls on all three backbones. On Qwen3-VL-4B, it improves over the original model on all 13 benchmarks and raises the average score from 75.00 to 78.82 relative to the matched fine-tuning control. These results show that pretrained convolutional representations, when integrated through learned adaptation and fusion, can improve the visual understanding of existing VLMs without replacing their original visual encoders.

---


### 569. [Frozen Judges, Moving Agents: Version-Dependent LLM-Judge Error and the Limits of Judge-Assisted Agent Evaluation](https://arxiv.org/abs/2609.34198)

**<font color=#1a73e8>作者：</font>** Jiapeng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model judges compare agent upgrades with their predecessors, but a fixed judge can make version-dependent mistakes. We analyze 35 public coding-agent submissions (20 prespecified version pairs on 250 SWE-bench Verified issues), two customer-service agents (155 tau-bench tasks), and 1,106 expert-labeled AgentRewardBench trajectories. An upstream outage left three judges for the primary SWE-bench analysis (8,743 aligned agent-task cells); the fourth is descriptive. All three coding-agent judges and all four tau-bench judges reject task-conditioned error invariance after multiplicity adjustment. On SWE-bench, 32 of 60 judge-by-pair units have a detectable differential comparison component; eight judge-only intervals declare improvements that execution-based intervals cannot establish, despite rank correlations of 0.71-0.79. In tau-bench, one judge confidently reverses a nine-point reference-reward gap by penalizing a procedural habit the reward ignores. False acceptance of failed coding patches rises with agent capability conditional on task and reference outcome, while a task-solvability prediction from AgentRewardBench reverses sign in SWE-bench. Transporting old-version calibration raises mean absolute comparison error on SWE-bench from 3.8 to 19.5 percentage points; 24.6% of ratio-bootstrap draws are undefined near the correction boundary. A tuned paired audit narrows a classical interval by only about 5% at 80 labeled tasks. A randomized three-arm test does not support the predicted increase in false acceptance from showing the agent's final report (all three Holm-adjusted p-values = 1.0). These results favor explicit reference standards and paired audits of current outputs over judge-only release decisions or transported old-version calibration.

---


### 570. [Learning to Optimize through Solver-Grounded Self-Play](https://arxiv.org/abs/2609.34205)

**<font color=#1a73e8>作者：</font>** Xia Jiang, Yaoxin Wu, Chenyu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization modeling is central to many decision-making scenarios, but traditionally requires extensive domain expertise. While Large Language Models (LLMs) have shown promise in automating this process, current training paradigms mainly rely on human-annotated or teacher-generated datasets. This dependence introduces a Generalization Ceiling, where models overfit to narrow data distributions, and Capability Anchoring, where models' reasoning is bounded by annotator proficiency and teacher model capability. In response, we propose OPT-Zero, the first fully self-play training framework for optimization modeling that requires zero external training data. OPT-Zero employs a single LLM in a dual-role closed loop: a Proposer that synthesizes increasingly challenging optimization problems alongside their mathematical formulations and solving code, and a Solver that attempts to resolve the problems given only natural-language problem descriptions. Grounded in execution feedback from external optimization solvers, we alternately train both roles using reinforcement learning. This process fosters an auto-curriculum in which the Proposer and Solver co-evolve: generating harder valid problems by the Proposer seamlessly enhances the structural reasoning ability of the Solver. Extensive results indicate that with zero curated data, OPT-Zero matches state-of-the-art data-dependent methods while exhibiting substantially stronger generalizability, establishing self-play training as a highly scalable paradigm for advancing LLM reasoning in modeling and solving optimization problems.

---


### 571. [WorldGuide: Learning Success-Failure Boundaries in Latent World Models for Vision-Language-Action Policies](https://arxiv.org/abs/2609.34206)

**<font color=#1a73e8>作者：</font>** Lin Liu, Lu Zhang, Ziying Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent world models offer a promising way to improve Vision-Language-Action policies by capturing the consequences of actions. However, models trained primarily on expert demonstrations have limited exposure to failure outcomes and may struggle to distinguish visually similar successful and failed interactions. We propose \textbf{WorldGuide}, a framework that learns these distinctions in latent space and uses them to guide policy training. WorldGuide combines predictive pretraining on successful and failed trajectories with contrastive learning on matched success--failure pairs. The learned predictor then provides a differentiable reward to guide joint optimization of the policy and visual encoder. The predictor is discarded after training, so deployment requires no additional world-model inference. Extensive experiments show that WorldGuide substantially improves VLA reliability and achieves state of the art performance on LIBERO 100 and SimplerEnv, reaching \textbf{96.8\%} and \textbf{72.0\%}, respectively. Code will be publicly available.

---


### 572. [Behavior-Grounded Semantic Enrichment for Financial Fraud Modeling and Reasoning](https://arxiv.org/abs/2609.34211)

**<font color=#1a73e8>作者：</font>** Linbo Shao, Huilin He, Yating Lou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In financial fraud detection, rich semantic context can provide important evidence for transaction behavior modeling and fraud reasoning. However, public real-world financial datasets often lack rich semantics due to privacy constraints. Consequently, synthetic datasets incorporate generated semantics, but at the cost of behavioral realism; textual descriptions for contextual reasoning remain scarce. We address this gap through a semantic enrichment framework grounded in original transaction behavior to simulate multimodal financial data. We (1) propose a multi-agent semantic enrichment framework that generates interpretable financial semantics grounded in transaction behavior through role-specialized agents and consistency refinement, and (2) newly contribute a valuable multimodal financial fraud dataset, MS-FFSD, enriched with structured semantics and textual semantics while preserving real-data-grounded transaction behavior. Furthermore, we systematically analyze the quality and utility of semantic enrichment. Results demonstrate statistical fidelity and framework generalizability, while showing that richer semantics benefit fraud modeling and context-aware LLM reasoning. Overall, this work advances multimodal financial fraud research and bridges emerging LLM and multi-agent capabilities with operational anti-fraud practice. The framework and dataset are released at this https URL.

---


### 573. [GlyphBench: A Playground for Language-Model Reinforcement Learning](https://arxiv.org/abs/2609.34214)

**<font color=#1a73e8>作者：</font>** Roger Creus Castanyer, Marc-Alexandre Côté, Matthew James Sargent 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce GlyphBench, an environment suite for reinforcement learning (RL) post-training of language-model agents, with over 360 tasks spanning diverse games. GlyphBench renders spatial observations as two-dimensional Unicode grids and connects training, evaluation, and trajectory replay through a unified interface designed to support efficient and reproducible research. We use GlyphBench to study how observation interfaces, reasoning effort, and agent harnesses affect performance, and how RL configurations shape learning dynamics. Our results show that glyph observations outperform native text and pixels in our Craftax experiments, with further gains on several BALROG environments. RL on 100 GlyphBench tasks improves Qwen3.5-4B on held-out Reasoning Gym problems, reaching 63.48% accuracy and outperforming the base model, a math-trained baseline, and a code-trained baseline. These experiments provide empirical evidence that reasoning gains from gameplay can yield stronger transfer than math or code. Together, these results highlight GlyphBench's value as a testbed for systematic research on how language-model agents learn, interact, and generalize.

---


### 574. [Same Winners, Different Success Rates: Evaluating How LLM Agents Recover from Failures](https://arxiv.org/abs/2609.34215)

**<font color=#1a73e8>作者：</font>** Dong Xu, Zhangfan Yang, Jiantao Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating how LLM agents recover from mid-task failures is central to deploying reliable agentic systems. Existing checkpoint-based benchmarks measure recovery by comparing which action is selected as best across independent runs, a quantity known as set agreement. However, set agreement is a purely ordinal measure that records which action wins without reflecting the absolute level of performance. When all actions fail, they tie at zero reward, and independent runs produce the same tied set with high probability, creating an illusion of stability that masks near-zero recovery success. We formalize this limitation through a set-path symmetry result, proving that for equal-cost Bernoulli actions the success probabilities (0.9, 0.8) and (0.2, 0.1) yield identical best-action-set distributions at every sample size. No procedure based solely on which action wins can distinguish these two regimes. We further prove that certifying exact population ties is impossible in finite time, and that the assignment of outcomes to checkpoints carries information beyond marginal outcome distributions. The pooled success probability is the missing scalar that resolves the ordinal ambiguity. Experiments on 864 frozen RecoveryBench episodes and two planning cohorts totaling 3,456 responses confirm the theoretical predictions. Agreement and held-out quality can move in opposite directions, and permuting checkpoint-to-action bindings changes 8 to 13 percent of cell-level conclusions. Based on these findings, we propose reporting four diagnostic quantities (agreement, all-zero fraction, held-out success, and pooled success) that expose this failure mode with no additional data collection.

---


### 575. [Loop Dropout: Regularizing Shared Updates in Looped Language Models](https://arxiv.org/abs/2609.34218)

**<font color=#1a73e8>作者：</font>** Zirui Zhu, Hailun Xu, Xuanlei Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models separate computational depth from parameter count by repeatedly applying the same transformer block. Adapting these models requires a shared update that remains effective as hidden states evolve throughout the recurrent computation. Our empirical analysis reveals a pronounced late-loop bias in standard low-rank adaptation (LoRA): the shared update is more effective at later loop positions. This imbalance motivates training shared updates under varying combinations of their applications. Randomly omitting adapter applications alone, however, does not improve task performance; it reduces expected update strength during training while leaving inference unchanged. We introduce Loop Dropout, which couples stochastic masking of adapter applications with inverse-survival rescaling to preserve expected update strength and promote effective adaptation across loops. Extensive experiments demonstrate improved mathematical reasoning across model sizes, adapter ranks and training recipes, with benefits extending to general instruction tuning and code generation. Loop Dropout outperforms existing LoRA variants and adapter regularizers, while further analysis shows stronger early-loop adaptation. Every backbone loop remains active, and inference applies the adapter at all loops using standard LoRA without additional trainable parameters or inference computation.

---


### 576. [Uncovering Ordinal-Matching Bias in Audio-Visual LLMs](https://arxiv.org/abs/2609.34223)

**<font color=#1a73e8>作者：</font>** Jihoo Jung, Youngjoon Jang, Hyebin Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work aims to improve how audio-visual large language models (AVLLMs) associate speech with the correct visible speaker in multi-speaker scenes. We find that current AVLLMs frequently fail at this task, and analyze the nature of these failures. To this end, we construct a synthetic diagnostic dataset in which multiple visible speakers each utter a single word. Analysis on this corpus reveals a consistent error pattern across three recent open-source AVLLMs: models attribute utterances by simply matching the order of spoken sentences with the left-to-right, top-to-bottom arrangement of visible faces, rather than relying on audio-visual cues such as lip synchronization. We term this behavior \emph{ordinal-matching bias}. We further show that this bias can be substantially mitigated through a simple remedy, Ordinal-Decoupled Fine-Tuning (OD-FT), in which models are fine-tuned on synthetic videos where spatial positions of speakers and speaking order are independently randomized. Despite using only 400 synthetic training videos, OD-FT not only suppresses ordinal-matching bias but also improves audio-visual understanding on real-world videos, yielding average gains of 8.27\% for Qwen2.5-Omni and 2.57\% for video-SALMONN2+ across three audio-visual benchmarks.

---


### 577. [USA: Update-aware SAM for Cross-domain On-Policy Disitllation of Language Agents](https://arxiv.org/abs/2609.34225)

**<font color=#1a73e8>作者：</font>** Qiyong Zhong, Mao Zheng, Mingyang Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation instils multi-turn agentic reasoning through dense token-level supervision on the student's own trajectories, but a single domain saturates early, so further supervision has to be drawn from other domains. Multi-domain data mixing is the most direct way of incorporating them, at the cost of conflicts between their data distributions and of retraining the entire model whenever one domain is revised. Model merging avoids both by distilling every domain independently and fusing the resulting task vectors afterwards. We find instead that the benefit polarizes across domain pairs: on those exhibiting negative transfer, every merging operator we evaluate falls below the single-domain reference. We attribute this to cross-domain update coupling, where a substantial fraction of coordinates is updated comparably by both domains and a merge can therefore displace them by as much as their own updates. To overcome this limitation, we propose USA, which converts per-parameter update magnitudes measured during a brief warm-up into per-coordinate perturbation radii, reducing curvature precisely on the coordinates that carry most of the merging displacement. Experiments across mathematics, science and code at two student scales show USA strongest in all six transfer directions, ahead of the single-domain reference by more than four points on average, and reverse the negative transfer of the conflicting pairs.

---


### 578. [When Does Selection Replace Extraction? A Pre-Registered Test of Agent Memory with a Typed Decision Model](https://arxiv.org/abs/2609.34227)

**<font color=#1a73e8>作者：</font>** Rishabh Sharma, Rishika Lall  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Does conversational memory need LLM-extracted facts, or is selecting the right raw turns enough? Published results disagree. Extraction-based systems report gains from distilled facts. Recent studies find raw history with good ranking does as well, but disagree about whether ranking matters. We ran a pre-registered study on held-out LoCoMo conversations and LongMemEval. At a tight budget on LoCoMo, raw turns selected by a single call to Jev, a typed decision model, are non-inferior to an LLM-extraction memory (one-sided 95% bound -3.0 points against a -5-point margin). Blind human grading narrows the margin but does not change the result. Raw turns cost 3,061 times less to write, and the result holds with a second answer model. Within this study, reranking's gain shrinks as the budget grows. It adds 17.4 points on LoCoMo and 9.1 on LongMemEval when three of 30 candidates are kept. At generous budgets it adds 1.5 and 1.1, and extraction systems are more accurate. This suggests why published results disagree. At matched context, Jev selects as accurately as an LLM reranker (non-inferiority bound -2.0) at a third of the latency, and more accurately than a multi-call graph traversal. Reranking lowers correct abstention. Plans, code and graded answers are released.

---


### 579. [SleuthBench: Benchmarking Statistical LLM Evaluation Using Tabular Hidden Signals](https://arxiv.org/abs/2609.34228)

**<font color=#1a73e8>作者：</font>** Jingyun Jia, Antoine Remond-Tiedrez, Aaron Alvarez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating statistical discovery by large language model (LLM) agents requires verifiable analytical ground truth. Establishing such ground truth for real-world datasets is costly, and prior knowledge of public datasets can influence agent responses. We introduce SLEUTHBENCH, a benchmark that addresses both problems by injecting controlled data-quality problems and feature effects into public tabular datasets: the injected pattern determines the answer, so reference answers are computed automatically and memorized knowledge of the original table is insufficient, while the table keeps its background structure. The injected patterns are modeled on phenomena reported in real data analyses. The benchmark defines 17 question templates in two families: data-quality questions and feature-contribution questions. We evaluate six state-of-the-art LLMs that analyze the data using a Python coding tool, on data-science and business phrasings of 70 validated dataset-template combinations, yielding 1680 graded responses in total. The models detect data-quality problems reliably (83.8% accuracy) but recover feature contributions poorly (41.9%). Finding how features shape the target requires searching over both candidate variables and analytical procedures. To address this issue, we propose the Empirical Layer, a set of precomputed statistical artifacts comprising summaries, fitted feature and interaction effects, and dataset descriptions, which exposes candidate patterns for direct inspection. Access to these artifacts raises feature-contribution accuracy from 41.9% to 68.0%.

---


### 580. [MAS-OPD: On-Policy Distillation for Multi-agent Systems](https://arxiv.org/abs/2609.34234)

**<font color=#1a73e8>作者：</font>** Qiyong Zhong, Mao Zheng, Mingyang Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) split a task across specialized roles and are promising on complex tasks, yet a prevailing approach relies on inference-time orchestration alone. General-purpose APIs are costly and hard to customize, while small models with role prompts rarely develop stable role competence or reliable collaboration, so post-training a MAS jointly is central. Most attempts use reinforcement learning, whose team-level reward leaves undetermined which step of which agent brought about the outcome, while local rewards need redesigning per task. On-policy distillation (OPD) gives token-level teacher supervision on trajectories the student samples, a denser signal needing no local reward, yet is underexplored for the interdependent agents of a MAS. Two difficulties arise: building complementary specialization from a judgement of which role a behavior belongs to while preserving the knowledge all roles need, and turning cross-agent collaborative information into supervision OPD can exploit. We present MAS-OPD, where Role-Advantage Specialization defines the role advantage as the difference between the teacher signals under target and non-target role conditions, and Privileged Attribution for Coordination attributes an interaction conflict to its source and supplies it to the teacher alone as privileged information. Extensive experiments on code and mathematics benchmarks show that MAS-OPD attains the highest mean score at both student scales and leads the agents to develop clearer role specialization and more effective collaborative behavior.

---


### 581. [SegBanana: Steering Unified Multimodal Models into Medical Segmenters](https://arxiv.org/abs/2609.34235)

**<font color=#1a73e8>作者：</font>** Xiaoye Liang, Ye Yan, Mingze Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation remains challenging in practical deployment, as models often struggle to generalize beyond the distributions covered by their training data and high-quality pixel-level annotations are typically unavailable for adaptation. Inspired by the cross-task transferability of large language models, we investigate whether unified multimodal models (UMMs) can transfer their pretrained visual understanding, reasoning, and generation capabilities to medical image segmentation without task-specific post-training. By recasting segmentation as structured visual generation, we find that frontier UMMs (e.g., Nano Banana) already exhibit basic segmentation capabilities across diverse clinical scenarios, but still struggle with challenging tasks requiring specialized anatomical or domain-specific knowledge. We further show that these limitations can be effectively mitigated by incorporating visual anatomical knowledge from in-context exemplars, expanding candidate solutions through repeated sampling, and refining suboptimal predictions via targeted this http URL by these observations, we propose SegBanana, to our knowledge, the first agentic visual generation framework for training-free medical image segmentation. SegBanana builds on a frozen UMM as the core generative model, augmented with Anatomy-Aware Knowledge Retrieval and Comparative Quality Critique to unlock its potential segmentation capability. A State-Aware Multimodal Controller maintains structured state and iteratively orchestrates these tools, repeatedly refining intermediate predictions toward higher-quality masks. Across eight medical segmentation datasets, SegBanana achieves an average mDice of 77.45%, outperforming representative generalist (SAM3 and SegGPT) and medical-specific (BiomedParse and MedSAM3) baselines by at least 14.93 points, while remaining robust to out-of-domain visual supports.

---


### 582. [Coherence-Aware Distributional Evaluation of Open-Ended Text Generation](https://arxiv.org/abs/2609.34240)

**<font color=#1a73e8>作者：</font>** Jinnuo Liu, Junhao Zhu, Weifeng Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing metrics for open-ended text generation measure likelihood, lexical diversity, or distributional similarity in generic representation space, yet they can miss fundamental dimensions of quality. A prominent blind spot is global coherence: a generated passage may be locally fluent while remaining globally contradictory, causally inconsistent, or topically disconnected. Such failures can still preserve the token-level and lexical statistics that existing metrics rely on. We identify representation as a central bottleneck in detecting these failures and introduce CHORD (Coherence-aware Hidden-state Open-generation Reference Distance), a coherence-sensitive distributional metric. CHORD encodes generated and human-written corpora in the hidden-state space of a frozen LLM using a coherence-eliciting prompt, and compares the resulting distributions using MMD with an RBF kernel. To validate that the metric responds to coherence degradation but not generic textual change, we construct a counterfactual evaluation suite that pairs graded coherence-degrading perturbations with meaning-preserving controls. CHORD selectively detects relation, discourse, structural, and mixture failures that perplexity, entropy, MAUVE, FBD, and MMD-based baselines either miss or cannot separate from benign rewriting. Factorial ablations show that representation is the primary source of coherence sensitivity,while RBF-MMD improves sample efficiency once the relevant distinctions become visible. Larger backbones capture finer-grained distinctions, but coherence prompting improves selectivity only when the backbone can follow the this http URL unconditional generation and prefix continuation, CHORD yields model rankings that strongly align with human judgments of whether outputs make sense and appear human-written. Together, these results establish representation design as central to reliable distributional evaluation.

---


### 583. [AdaGuard: An Adaptive Guard Model with User-defined Policies](https://arxiv.org/abs/2609.34241)

**<font color=#1a73e8>作者：</font>** Yunhao Feng, Yifan Ding, Yuxiang Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Guard models support the safe deployment of language model agents, but fixed risk taxonomies limit their ability to accommodate requirements that vary across applications and tasks. Under user-defined policies, detecting violations requires interpreting both the applicable rules and the agent's behavior, since identical actions can receive different judgments under different policies. To support learning this capability, we introduce AdaptiveSafety, a dataset of 10,939 training examples and 1,000 test examples covering policies with 1--100 rules. The dataset combines trajectories from multiple sources with policy and behavioral counterfactuals, pairing each example with an explanation and the complete set of violated rules. These counterfactuals expose changes that alter compliance, while structural augmentations provide supervision for consistency under rule reordering and identifier remapping. Building on this supervision, we propose SafePO, a reinforcement learning algorithm for refining violation identification while balancing explanatory reasoning and final verdicts. SafePO uses structured rewards to assess prediction correctness, retains group-relative advantages at the response level, and employs a separately trained value model to modulate token weights within explanation and verdict regions. Separate normalization controls their relative contribution to training despite differences in length. Through supervised initialization followed by SafePO, we develop AdaGuard, a family of 0.6B, 4B, and 8B guard models that assess agent trajectories under policies supplied at inference time. Our 4B model achieves binary accuracies of 89.30\% on AdaptiveSafety and 71.82\% on DynaBench. The project repository is available at this https URL

---


### 584. [Stashbird: Efficient Speaker-Indexed Memory for Conversational Agents](https://arxiv.org/abs/2609.34242)

**<font color=#1a73e8>作者：</font>** Chidera Biringa, Lucas Yannul, Xiaowen Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents require memory that preserves information across user-agent exchanges, user-to-user conversations, and group conversations with or without agent participation, while supporting updates as evidence changes or is removed. We present Stashbird, an agent memory system that links source episodes to derived memory state through explicit provenance. Stashbird organizes memory into episodic records, semantic relations, community summaries, and persisted graph state, with lifecycle operations for incremental updates and episode-level deletion. We evaluate question-answering accuracy and model-facing workload across four long-term memory benchmarks. On LoCoMo, Stashbird uses 76.4x fewer ingestion prompt tokens than Graphiti. Compared with reproduced Hindsight on the same benchmark, it uses 8.1x fewer retrieval prompt tokens, with accuracy 1.6 percentage points lower. It achieves higher accuracy than Hindsight on LongMemEval-S and GroupMemBench and comparable accuracy on EverMemBench.

---


### 585. [When Models Choose the Question: Pedagogical Constraints in Bottom-Up Multi-Agent Inquiry](https://arxiv.org/abs/2609.34243)

**<font color=#1a73e8>作者：</font>** Yeri Hong, Lauren Hyoseo Yoon  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> What shapes a model-generated inquiry when no discussion question is supplied? We introduce a bottom-up forum framework inspired by Philosophy for Children, in which language-model agents read a philosophical narrative, propose and select questions, and develop a shared conclusion without a privileged model facilitator or aggregator. Across 576 forums, contrasting Aristotelian value personas interacted with a blank-slate participant receiving no value-specific instruction. The blank slate remained neutral and was selected more often for conclusions than questions. Yet inquiry narrowed in both form and source: varied initial questions increasingly became either/or alternatives, while discussion concentrated on directions already explicit in the text. Our ECO framework traces this source focus by distinguishing explicit philosophical framing, characters' modeled inquiry, and open-ended narrative material. Across analyzed chapters, participants drew most often on explicit framing. We describe this as a pedagogical constraint: freedom to formulate questions did not necessarily produce freedom from source framing.

---


### 586. [Certified Multi-Source Integrity for Structured Agent Actions](https://arxiv.org/abs/2609.34245)

**<font color=#1a73e8>作者：</font>** Anmol Pandey, Aditya Jain, Liang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly take privileged, often irreversible structured actions, such as paying an invoice. They assemble each action from action-critical fields in documents and tool outputs that an adversary can corrupt, and indirect prompt injection can drive the model itself to extract attacker-chosen values. Current defenses gate on a source's trust label or certify free-text answer quality. None certifies the integrity of a coupled, policy-bound structured action under a corruption budget that accounts for shared upstream sources. We characterize when such an action is safely certifiable and give the maximally live safe certifier. It admits an action only when each field clears the rule its evidence structure supports: a bounded corruption radius over corruption-distinct evidence classes, counted by a minimum hitting set so that re-publishing or laundered copies cannot manufacture a quorum, deterministic reconciliation for complementary fields, and a trusted anchor where the evidence leaves a field single-sourced. We formalize two robustness notions, validate each mechanism by ablation, and measure how often the multi-source precondition holds on sanctions designations (70,966 entities) and software supply-chain provenance (450 packages). Under upper-bound proxies, genuine corroboration is a minority phenomenon in both, and naive attestation counting overstates it, since witnesses that look independent collapse to two corruption-distinct domains once shared origin is counted. Across five current models in a real agent loop, a realistic injection fools every model but one and a naive agent then executes the fraudulent action on most attacks. The certifier admits no unsafe action and recovers the correct value where corroboration permits, while action-gating and provenance baselines are broken in every world of our harness by some attack in its space.

---


### 587. [SALMONN-duo: Adaptive Dual-System Coordination for Full-Duplex Voice Agents](https://arxiv.org/abs/2609.34247)

**<font color=#1a73e8>作者：</font>** Wenyi Yu, Siyin Wang, Terumi Chiba 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech large language models (LLMs) enable low-latency, natural voice interaction. However, real-world agents must also use tools and perform deliberative reasoning-operations whose variable latency and computational cost conflict with the stringent timing requirements of real-time conversation. To reconcile these demands, we propose SALMONN-duo, an adaptive dual-system voice agent inspired by dual-process theories of cognition. SALMONN-duo separates real-time interaction from deliberative computation by pairing an always-on, fast-thinking full-duplex speech LLM (system 1) with a powerful asynchronous slow-thinking LLM agent (system 2). Beyond handling real-time interaction, system 1 learns when to answer directly and when to delegate, remaining responsive during backend execution and seamlessly integrating returned information into the ongoing dialogue without exposing tool traces or losing conversational context. Evaluations on single-turn spoken question answering (QA) and multi-turn conversations demonstrate that adaptive delegation substantially improves accuracy on knowledge-intensive and multi-hop reasoning questions, while knowledge-boundary-aware training avoids unnecessary system 2 invocations. On a customized version of $\tau$-Voice, SALMONN-duo further demonstrates its ability to complete environment-grounded, policy-constrained tasks through multi-turn interactions in realistic business scenarios. Finally, cost-aware reinforcement learning further enhances the trade-off between task performance and backend usage across the QA and conversation tasks, while improving task success and response safety on $\tau$-Voice with an acceptable increase in the delegation rate.

---


### 588. [Evolving Support Priorities in Empathetic Reinforcement Learning](https://arxiv.org/abs/2609.34249)

**<font color=#1a73e8>作者：</font>** Pengyu Huang, Zhiyuan Han, Wenwen Tong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We identify a fundamental mismatch in empathetic reinforcement learning: support priorities evolve with the dialogue state, yet existing methods typically optimize predefined reward specifications that remain fixed across turns. To model these evolving support priorities, we organize empathetic support along cognitive, affective, and proactive empathy, and propose Context-Adaptive Rubric Evolution (CARE). At each turn, CARE generates a context-adaptive rubric by adjusting both the weights of these three empathy dimensions and their fine-grained evaluation criteria. The rubric generator is trained with turn-level rubric supervision and human preference data through supervised fine-tuning followed by preference-based reinforcement learning, and then serves as an adaptive reward interface for online empathetic RL. Integrated with both RLVER and MICA, CARE achieves state-of-the-art performance across SentientBench, EQBench3, and EMPA under three independent LLM judges. Notably, on EMPA, CARE improves EPM-Idx over the strongest baseline by at least 13 points under all three judges, including an increase from 28.11 to 83.54 under Gemini-2.5-Pro. Further analyses show that learned rubric priorities systematically vary across dialogue stages and user emotions, demonstrating that CARE adapts what is rewarded as support needs evolve.

---


### 589. [RADNPO: Reference-free Adaptive Negative Preference Optimization for LLM Unlearning](https://arxiv.org/abs/2609.34251)

**<font color=#1a73e8>作者：</font>** Shenghan Tan, Ziyi Zhou, Wenpeng Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can memorize sensitive, private, or copyrighted content during pre-training, making machine unlearning necessary for removing targeted knowledge. Recent preference optimization (PO)-based unlearning methods improve stability over gradient ascent (GA)-based methods by introducing alignment-style objectives, which effectively suppress the probability of forget targets. However, target suppression alone does not sufficiently constrain the next-token distribution after unlearning. Existing methods provide limited control over how suppressed probability mass is redistributed and insufficiently adapt forgetting strength to target confidence and distributional concentration. Even after target suppression, probability mass may remain concentrated on a few non-target tokens, potentially producing repetitive or uninformative outputs. To address these limitations, we propose Reference-free ADaptive Negative Preference Optimization (RADNPO), which explicitly guides next-token probability redistribution. Specifically, RADNPO contrasts each forget target with alternative tokens favored by the current next-token distribution and adaptively modulates token-level forgetting strength using target confidence and next-token concentration. Experiments on TOFU and MUSE demonstrate that RADNPO achieves a better trade-off between forgetting quality and model utility than current baselines.

---


### 590. [DreamingGoose: Staged Distillation from Autoregressive Transformers to Bidirectional Recurrent Diffusion Language Models](https://arxiv.org/abs/2609.34253)

**<font color=#1a73e8>作者：</font>** Julian Boesch, Andrew Wee, Alexander Stranzl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained autoregressive Transformers represent a large sunk investment in compute. Existing conversion methods reuse that investment by changing either the architecture (attention to recurrence) or the objective (next-token prediction to denoising), never both. We convert Qwen3 teachers at 1.7B and 8B into attention-free, bidirectional, gated-delta-rule diffusion students in three stages, so that each capability can be traced to the stage that kept or lost it. Language modeling transfers only partially and in-distribution; in-context retrieval does not transfer. On a multi-query recall probe where the teachers score 0.34-0.58, both converted students score 0.000, and diffusion pretraining alone does not restore retrieval. A retrieval curriculum in the final stage, which gradually lengthens the gap between a key-value table and the queries that address it, restores it only stochastically: on a fixed schedule, one seed in three learns to retrieve. Advancing the gap only while a running accuracy estimate stays above a threshold works for all three of those seeds, holds on real text, and carries unchanged to 8B, where two of three seeds succeed. The third had not learned within its fixed 16k-step budget: retrieval switches on abruptly at a seed-dependent step (6.5k and 11k in the other two), so a fixed budget can cut a late run off. One boundary survives every intervention: every model that learns retrieval scores 0.000 on tokens that never appeared in a retrieval episode, and an arm that resamples the key and value tokens every batch shows this is a coverage limit, not memorization of particular bindings. Separately, we convert a 7B code model into a 3:1 recurrent-attention block-diffusion hybrid over 85k steps and report two negative training results.

---


### 591. [Recursive LLM Degradation in Biomedical Question Answering: A Cross-Generation Study](https://arxiv.org/abs/2609.34257)

**<font color=#1a73e8>作者：</font>** Bibek Bhandari, Kshitij Lingthep  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Repeatedly training language models on their own generated data may create a synthetic-data feedback loop in which errors and distributional biases are reintroduced into subsequent training datasets. This paper studies that process in biomedical question answering (QA) using PubMedQA and two Qwen2.5 model sizes, 0.5B and 3B parameters. The study compares a recursive synthetic-data condition, in which generation G(k+1) is trained on answers produced by G(k), against a Human-Control condition that repeatedly uses the original human training data. The study evaluates across four generations from G0-G3 with two random seeds (42 and 123) and a fixed evaluation set of 1,000 expert-labeled samples. The evaluation includes disease and chemical entity F1, context-supported rate, lexical and semantic similarity, answer length, repetition rate, and other evaluation metrics. The Recursive condition for both model sizes and both seeds showed larger declines than the Human-Control condition in disease entity F1, chemical entity F1, context-supported rate, ROUGE-L, and cosine similarity. Under the fixed no-repeat 3-gram decoding constraint, the main observed behavioral change was increased answer length, while the measured 3-gram repetition rate did not increase. The magnitude of the difference-in-change was larger for the 3B model than for the 0.5B model. This difference was particularly apparent in disease F1, context-supported rate, cosine similarity, and answer length. These results show domain-specific changes associated with using recursive synthetic-data training in biomedical QA, but do not establish clinical hallucination rates or universal model collapse.

---


### 592. [QuantaSpike: Short-Window Spike-Driven Quantization for Large Language Models](https://arxiv.org/abs/2609.34259)

**<font color=#1a73e8>作者：</font>** Bang Hu, Guowei Zhu, Changze Lv 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong performance across many tasks but rely on dense multiply-accumulate (MAC) operations during inference, resulting in high energy cost. Spiking neural networks (SNNs) offer an event-driven alternative in which synaptic integration uses lightweight accumulation. However, spike-driven LLM inference remains difficult because outlier-heavy activations typically require long firing windows or auxiliary non-spiking paths. We propose QuantaSpike, a short-window spike-driven quantization framework for LLMs built around Logarithmic Ternary Integrate-and-Fire (LTIF) neurons. LTIF uses ternary events with power-of-two membrane-response quanta, improving the information represented by each firing step while retaining shift-ACC-compatible computation. QuantaSpike combines this neuron with group-adaptive gain and selective outlier admission: normal values use residual LTIF steps, whereas admitted outliers receive one additional onset spike before entering the same residual dynamics. Across OPT and Llama-2, QuantaSpike achieves state-of-the-art or competitive perplexity and zero-shot accuracy among spike-driven LLM quantization methods. It also transfers to newer dense LLMs, remaining close to the FP16 reference on Llama-3-8B and Qwen3-8B under the same four-step firing window. Analytical linear-energy projections show that QuantaSpike reduces the energy of one linear transformation by about $80.0\%$ on OPT models and $67.1\%$ on Llama-2 models relative to SpikeQuant, providing an accurate and energy-efficient spike-driven path for LLM inference.

---


### 593. [Maintaining Benchmarks Against Increasingly Capable Agents: Detection and Remediation of Unearned Passes](https://arxiv.org/abs/2609.34262)

**<font color=#1a73e8>作者：</font>** Weijun Luo, Kelvin Luu, Xinyi Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic benchmarks guide model selection and training. Yet an agent can pass a task without demonstrating the intended capability. Such outcomes constitute unearned passes; their proportion among all passes defines the integrity gap. As agents improve, benchmark surfaces that once seemed harmless can become exploitable, making benchmark validity an ongoing maintenance problem. We introduce a process-verification framework that audits passing trajectories, distinguishes evidenced reward hacking from verifier weakness, and localizes exploitable surfaces for repair. Across 3,810 passing trajectories from 29 model-benchmark cohorts, confirmed violations often increase with model generation but not monotonically. On SWEBench Pro V1.0, confirmed violation rates rise from 24% to 73% between Opus 4.7 and Fable 5 on matched tasks; later cohorts fall to 11% for Fable 5.1 and 0% for GPT-6 Astra. These comparisons are descriptive: configurations were not normalized, and the latest models also pass fewer exploitable tasks. Violations concentrate around a small set of recurring surfaces, especially unintended access to reference solutions through git history. Three repair case studies across two benchmarks show why blocking a recorded exploit is insufficient: the same protected information can remain accessible through another route. Therefore, we combine minimal patches with exploit replay and fresh agent evaluation, auditing new passes under the original standard. No evaluated attempt against the final patches reached the protected channel, and every post-patch pass was judged legitimate. Benchmark integrity requires ongoing maintenance: audit passing behavior, repair the enabling surface, and re-evaluate both exploit access and legitimate solvability.

---


### 594. [Query Expansion and Key Specialization in Transformer Attention Geometry](https://arxiv.org/abs/2609.34273)

**<font color=#1a73e8>作者：</font>** Vidit Gupta, Siddhesh Nadkarni, Mihik Chaudhari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The projection of queries and keys are central to the attention mechanism in Transformer architectures. While they are mathematically symmetric, they play different roles in attention mechanisms. The question of whether there is an effect from their functional distinction on their geometric development in training remains unanswered. We investigate the problem through the training of small GPT-like Transformers on character-level WikiText-103 for three different depths (4, 6, and 8 layers), three types of initialization for queries and keys, and four random seeds, resulting in 36 runs and 54 trajectories of average layers across seeds. We track the effective dimensionality of those layers using participation ratios and discover that effective dimension of queries expand while keys shrink, and that $PR_Q - PR_K$ is positive in all trajectories studied. In connection to attention, the shrinking of keys leads to a narrower spectrum of $QK^\top$ and more peaked attention weights. In order to determine if this connection is causal or coincidental, we directly control the spectrum of keys during training across five seeds: restricting it to make it shrink sharpens the attention with high directional confidence, while keeping it constant to the level of initial dispersion makes attention softer. Additional token-level checkpoint analyses show that the monotonic paired-contrast trend is not universal across pretrained families, but survives as an early-training regime that later decays over a full pretraining run, and the link between interaction-rank geometry and attention entropy remains visible in several models.

---


### 595. [BIABench: Evaluating AI agents on real-world bioimage analysis tasks](https://arxiv.org/abs/2609.34274)

**<font color=#1a73e8>作者：</font>** Zixuan Pan, Davide Panzeri, Lukas Johanns 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial-intelligence (AI) agents hold promise for automating bioimage analysis, yet no benchmark evaluates whether they can carry out real-world analyses end to end. Such analyses are hard for agents because 2D images, 3D volumes and time-lapse sequences are often too large to read as context, so an agent must choose and run an analysis through code, specialized software and rendered views. Published studies make this capability testable, because each pairs raw images with a peer-reviewed result. We introduce BIABench, a benchmark of 16 tasks reconstructed from published biological studies that retain their scientific questions, imaging data and ground truth. The tasks span eleven analysis subtasks and modalities from H&E histology to single-molecule localization microscopy. Each submission receives an outcome score, which compares the output files with the ground truth using field-standard metrics, and a process score, in which a vision-language model judges method choice and quality control against an expert-written rubric. We evaluated general-purpose and biology-specific agents across several language models, with repeated runs of every task. Routine two-dimensional tasks were solved well, but on some tasks that added a third dimension or a time axis no agent scored above 0.19. Neither biological specialization, stronger models nor detailed expert instructions closed this gap. The agents were also unreliable, with scores varying more between repeated runs of one agent than between different agents, and without ground truth a correct run could not be told from a wrong one by its process score or by the time spent. Released openly with its data and code, BIABench provides a verifiable framework for evaluating, and eventually training, agents for reliable long-horizon bioimage analysis.

---


### 596. [See, Measure, and Reason: Learning Visually Grounded Reasoning in Pathology](https://arxiv.org/abs/2609.34277)

**<font color=#1a73e8>作者：</font>** Chengyang Zhang, Wenchuan Zhang, Bo Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathological assessment relies on recognizing fine-grained visual details in histological images. Vision-language models (VLMs) increasingly support pathology interpretation, yet their ability to perceive these details remains inadequate. This weakness leads to inaccurate cellular observations that can persist even when final answers are correct. In this paper, we propose ASPECT to improve visually grounded reasoning through explicit supervision of cellular appearance and abundance. ASPECT trains intermediate visual tokens through pathology feature reconstruction, cell feature alignment, and count supervision. Three-stage supervised fine-tuning teaches the model to perceive, generate visual tokens, and reason, followed by reinforcement learning that rewards answer correctness and consistency with reported measurements. We also introduce PathoVernier, a benchmark of 759 expert-reviewed questions from five pathology datasets covering four cellular composition tasks. It evaluates both final answers and intermediate measurements to expose errors hidden by answer accuracy. On PathoVernier, ASPECT achieves relative accuracy gains of approximately 19.2% over the strongest baseline, Gemini-3.1-Pro, and 99.3% over its Qwen3-VL-8B backbone, while reducing RAWR, which measures counting errors within correct responses, by 28.1% and 42.7%, respectively. ASPECT also improves over its backbone on three external pathology benchmarks covering classification and question answering beyond cellular composition tasks.

---


### 597. [Direct Self-Evolving Optimization: Evolving LLMs without Challenger Training](https://arxiv.org/abs/2609.34279)

**<font color=#1a73e8>作者：</font>** Yuyang Deng, Yu Wang, Jiayun Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving language models improve by generating tasks and learning from their own feedback, but adapting the task generator often requires a separate challenger-training loop. Can we generate tasks adapted to the current solver without explicitly training a challenger? We introduce \textbf{D}irect Self-\textbf{E}volving \textbf{O}ptimization (DEO), which replaces challenger parameter updates with solver-guided task sampling. The KL-regularized challenger objective defines an exponential tilt of a fixed base task distribution. DEO uses this distribution as a sampling target: a frozen LLM generates and mutates tasks, the solver scores them, and an approximate Metropolis selection rule refines the training pool. Only the solver is trained. Theoretically, for an idealized variant that samples exactly from the tilted distribution, and under regularity, local gradient-dominance, and initialization conditions, we show that DEO learns distributionally robust reasoning ability. In experiments, DEO achieves reasoning performance competitive with R-Zero while using over $50\%$ less wall-clock training time, and improves reasoning accuracy over a no-walk ablation. Replacing the task generator with a frozen API-only LLM further improves the local solver, illustrating a capability enabled by removing challenger training.

---


### 598. [Agentic High-Dimensional Bayesian Optimization with Hypothesis- and Evidence-Guided Search](https://arxiv.org/abs/2609.34281)

**<font color=#1a73e8>作者：</font>** Zhixuan Gao, Ke Xue, Rongxi Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional Bayesian optimization (HDBO) seeks sample-efficient optimization when the number of variables is large relative to the evaluation budget. Recent LLM-based and agentic BO methods incorporate task knowledge and adapt search decisions during a run, but have primarily been evaluated on low- and moderate-dimensional problems. We ask whether this paradigm can transfer to the higher-dimensional regime. Our experiments show that these methods do not remain reliable in the high-dimensional regime, where the challenge is not only where to evaluate, but also which modeling assumption and search geometry to use when the objective's useful structure is unknown. We therefore introduce HERA, a Hypothesis- and Evidence-guided Research Agent that uses task context, optimization feedback, and structural diagnostics to revise search hypotheses, select and configure HDBO strategies, and determine their execution length. PRISM, its numerical optimization engine, generates and evaluates candidates sequentially within each search block, updating numerical models after each observation. HERA remains competitive with strong numerical HDBO baselines and outperforms the evaluated LLM-based and agentic methods on four metadata-free synthetic functions. Across eight real-world tasks, HERA achieves the best mean final objective among all evaluated systems on most benchmarks. Further analyses show that structural diagnostics change strategy use, metadata effects vary across tasks, and adaptive search blocks reduce inference cost.

---


### 599. [Over-Personalization Is a Decision Failure: Generation-Induced Apply Bias in LLMs](https://arxiv.org/abs/2609.34284)

**<font color=#1a73e8>作者：</font>** Haeun Jang, Yonghyun Jun, Hwanhee Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized LLMs must decide, for each stored preference, whether the current context calls for applying or suppressing it, which we call its applicability. They frequently over-personalize, applying preferences the context rules out, yet existing benchmarks score only the final response and cannot tell where this failure arises. We decompose preference handling into three stages and measure each separately: (1) knowing whether a preference applies, (2) deciding on an explicit Apply/Suppress label, and (3) generating a response consistent with that label. Using linear probes, we first show that this applicability signal remains decodable from hidden states during generation. By making the decision explicit, we then find that in most settings wrong decisions faithfully followed outnumber correct decisions lost in generation. We thus locate the failure in the decision, which breaks once the model is also asked to answer. To determine whether this reflects lost sensitivity or a response bias, we propose ABIDE (Apply-Bias Investigation via Decision-score), which adapts signal detection theory to Apply-vs-Suppress decision scores read directly from logits. ABIDE reveals a generation-induced Apply bias: merely stating an answer-generation objective shifts the decision score toward Apply while sensitivity is largely preserved, and the shift persists under controls for prompt structure, cascades across preference slots, and prompt wording. Finally, we show that subtracting a single bias scalar, estimated on a held-out split, from the decision score at decoding time reduces leakage while largely preserving fulfillment.

---


### 600. [ReScraper: Unified Scraping and Cleaning of Web Data for Effective LLM Pretraining](https://arxiv.org/abs/2609.34287)

**<font color=#1a73e8>作者：</font>** Zichun Yu, Jiarui Yan, Shlok Sanghvi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM pretraining corpora are normally cleaned by a stack of hand-written heuristics. A heuristic scraper extracts the main content from HTML, and dozens of rule-based filters then clean it, so corpus quality is capped by the coarseness and accuracy of the rules. In this work, we propose ReScraper, a unified language model of only 0.6B parameters that replaces this entire stack. To train ReScraper, we carefully curate supervised data from the outputs of three teacher models, so it learns to first extract the main content from raw data and then choose among four operations: keeping the page as extracted, editing out noisy lines and spans, deleting it entirely, or rewriting it when it is poorly written but informative. Based on the same crawled data pool, pretraining 400M, 1.4B, and 2.8B models on our curated data improves the DCLM Core score by a relative 3.8--4.7% over the strongest baseline at each scale, including the costly multi-agent curation. Our analyses show that each operation plays a distinct and complementary role, and that extracting and cleaning in one model outperforms a cascade of separate models. ReScraper also concentrates its operations on the pages that need them, raising the quality of poor pages the most while keeping the corpus diverse. These results demonstrate the feasibility and effectiveness of AI4AI for pretraining data curation, where a small learned model takes over an entire stage of the pipeline from hand-written heuristics. We open-source our code at this https URL

---


> [!TIP]
> 当前位于：**551-600**（第 12/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
