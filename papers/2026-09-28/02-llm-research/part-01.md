# 🧠 大模型相关研究 | 2026年09月28日

> 本类共 **228** 篇论文：已确认 **208** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-228](./part-05.md)

---

### 1. [When Should Forecasting Agents Reason? Behavioral Stress Tests for Reliability Routing](https://arxiv.org/abs/2609.28475)

**<font color=#1a73e8>作者：</font>** Yufeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting agents increasingly combine language-model reasoning, retrieval, ensembling, and calibration, but it remains unclear when each behavior should be trusted. We study this question on ForecastBench-style binary forecasting tasks, treating the choice to retrieve, reason, defer to a market prior, or use a historical analog as an observable agent behavior rather than a hidden implementation detail. Our central finding is that mechanism choice is source-dependent: structured analogs dominate for some data-generating processes, while market/crowd-style and conservative baselines are better for others. We introduce ReliabilityRoute, a structural intervention that steers forecasting-agent behavior using reliability features such as historical coverage, market-prior availability, source-prior sharpness, evidence strength, evidence disagreement, and horizon. A fixed 2024-fitted rule closely matches a hand taxonomy without hard-coded source-name decisions, while a walk-forward self-adjusting rule refits thresholds from previously resolved vintages and obtains the best mean Brier score among our deterministic systems across 16 later LLM vintages. The gain is modest and historical/search baselines remain highly competitive. The main contribution is therefore a behavioral stress test showing that more reasoning is not always better; forecasting agents should first estimate which evidence source deserves control, routing policies should themselves adapt under auditable constraints, and reproducibility artifacts are available at this https URL

---


### 2. [Framing by Wording, Framing by Selection: A Large-Scale Two-Dimensional Audit of French News Headlines, 2022-2025](https://arxiv.org/abs/2609.28487)

**<font color=#1a73e8>作者：</font>** Amr Sobhy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> News headlines frame public issues both by what they select and by how they word it, yet computational framing work typically collapses these operations into a single score. We introduce a two-dimensional framework that separates salience framing, measured through four wording devices (loaded vocabulary, blame attribution, threat framing, rhetorical question), from selection framing, measured through outlet-level story-form and high-charge distributions. We build a 10,000-headline French supervision set using three LLM annotators with majority-vote resolution and human arbitration, validate the labels against two annotator-independent blind human studies, and apply the strongest classifier to 902,111 deduplicated headlines from 25 French outlets (2022-2025). Three main findings emerge. First, salience and selection divergence are positively correlated yet leave nearly half of outlet-level variance unexplained, populating interpretively distinct off-diagonal cells in a four-cell outlet typology. Second, default classification thresholds systematically inflate corpus-level salience estimates; a precision-floor recalibration protocol corrects this distortion. Third, group-mention analysis reveals sharply unequal salience contexts: headlines mentioning Jews, the Far-right, and Muslims carry the highest detected salience rates, which broad event-context composition does not fully explain (residuals are descriptive, not same-event causal estimates; per-group lexicon precision is reported alongside). To our knowledge, this is the largest framing-focused French headline audit to date; we release the supervision set, lexicons, and analysis code.

---


### 3. [TW3Cast: A Frozen Router of Lightly Fine-Tuned Foundation Models for Time-Series Forecasting on GIFT-Eval, Selected Entirely on the Training Split](https://arxiv.org/abs/2609.28506)

**<font color=#1a73e8>作者：</font>** Nathan Thierry, Andre-Louis Rochet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> TW3Cast is a time-series forecasting system that reaches position 3 of 130 entries on the GIFT-Eval benchmark by mean MASE rank, as of 2026-09-14. The two entries above it belong to the leaderboard's agentic category, multi-step systems that use agents or language models to reason about, generate or select forecasts. TW3Cast runs no agent and no language model. Its selection is a table computed once on the training split and then frozen, and its experts are public foundation models lightly fine-tuned on those training splits. For each of the 97 dataset, frequency and horizon configurations, the table serves one of four modes: a specialist, which is a LoRA or full fine-tune of Chronos-2, TiRex or Toto whose training data was cleaned and enriched by explicit rules; a quantile blend that contains a specialist; a blend of base models; or a selection tournament played on a backtest carved from the training split. Every decision in the table was taken on that backtest. A specialist is admitted the moment it beats the tournament there, so a candidate costs a few megabytes and minutes of GPU time, and a failed candidate changes nothing. Three guarded mechanisms protect the selection from its own biases: a dual accuracy and calibration criterion, an asymmetric margin against candidates that saw the series during training, and conservative per-window gates. The selection rules themselves were chosen inside a temporal meta-backtest. The best base model served alone reaches a mean MASE rank of 33.8, the tournament served on every configuration reaches 38.0, and the full router reaches 19.4. The routing table, the expert index, the pinned base-model revisions, the submitted score file and the dated snapshot of the public scores are released, and every leaderboard number in this paper regenerates from them by one script.

---


### 4. [An Exposition of GPT Astra's Proof of Lower Bound on DP Continual Counting](https://arxiv.org/abs/2609.28528)

**<font color=#1a73e8>作者：</font>** Jalaj Upadhyay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The goal of this note is to give a detailed proof, to the best of our understanding, of the recent presentation by Harrison and Leeman (arXiv:2609.17650v01 and arXiv:2609.17650v02) of the proof by Astra on the lower bound for differentially private continual counting. We believe a more natural and easy proof is possible and hope that this note will help in that effort.
Prior to the initial preprint by Harrison and Leeman (arXiv:2609.17650v01), Bairaktari and Larsen (arXiv:2607.00876) gave an elegant proof to show a lower bound of $\Omega(\log^{3/2}(n))$ for both pure and approximate-DP continual counting, and in personal communication had informed us that they have a proof of optimal $\Omega(\log^{2}(n))$ for pure-differential private continual counting as well. They have subsequently published their $\Omega(\log^{2}(n))$ bound, which is now a joint work of Bairaktari, Dahl, and Larsen (arXiv:2607.00876v3). Their new result is an elegant extension of their technique for approximate-differential privacy. Although the two proofs are technically different, the Astra argument uses related tree geometry introduced in Bairaktari and Larsen.

---


### 5. [Pistis Technical Report](https://arxiv.org/abs/2609.28554)

**<font color=#1a73e8>作者：</font>** Heyun Chen, Xiaohan Lan, Jiaxi Li 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce the Pistis model family, comprising 27B- and 9B-parameter multimodal large language models built on Qwen3.6 and Qwen3.5, respectively, and developed through a general and scalable post-training framework. The framework first establishes a strong foundation through large-scale multimodal supervised fine-tuning (SFT). Building on this SFT foundation, we propose Interleaved Distillation and Reinforcement Learning (IDRL), a novel post-training paradigm that tightly integrates on-policy distillation and reinforcement learning within a single training loop. By alternating between the two objectives, rather than optimizing either in isolation or combining them in a static joint loss, IDRL enables more effective knowledge transfer, greater optimization stability, and more precise credit assignment for long-horizon agentic trajectories, leading to stronger performance while mitigating common capability trade-offs. At both model scales, the framework produces two specialized variants: Pistis-Thinking, designed to strengthen deep multimodal reasoning, and Pistis-Agentic, which additionally incorporates agentic trajectory data to support long-horizon planning, iterative reasoning, and tool use. Pistis-Agentic is particularly strong in multimodal search. Both scales outperform their corresponding base models. Beyond model-parameter optimization, we further introduce Pistis-Auto-Harnessing (PAH), a system-level method that automatically improves the agent's inference harness through iterative optimization. Experiments demonstrate that PAH enhances the model performance without updating the model parameters or increasing the interaction budget.

---


### 6. [BaseCamp --- An Agentic AI Framework for Automating DNA Sequencing Data Pipelines](https://arxiv.org/abs/2609.28557)

**<font color=#1a73e8>作者：</font>** Eranga Bandara, Xueping Liang, Asanga Gunaratna 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> DNA sequencing pipelines, spanning quality control, alignment, variant calling, and annotation, are now reliably executed by workflow management systems that orchestrate established bioinformatics tools at scale. What remains manual is the decision layer surrounding that execution: selecting quality thresholds appropriate to a sample and platform, adjudicating borderline variant calls, diagnosing anomalies, and determining which findings warrant expert review. These decisions are repetitive, judgment-intensive, inconsistent across operators, and frequently undocumented. This paper introduces BaseCamp, a novel agentic AI framework for automating the decision layer of DNA sequencing pipelines. The framework decomposes the pipeline into six specialized AI agents, covering sample intake and quality control, alignment, variant calling, annotation, cross-stage monitoring, and reporting. Critically, BaseCamp agents do not perform sequence analysis: established tools execute alignment, calling, and annotation, while the agents select among them, configure them, interpret their output, and decide what follows. This confines language model reasoning to the judgment layer where it is reliable and preserves the reproducibility existing tooling guarantees. Agent reasoning is powered by a consortium of fine-tuned, domain-specialized large language models coordinated by a central reasoning LLM, executing locally so no sequencing data leaves the operating environment, under human-in-the-loop orchestration. Evaluation shows agent-generated configurations are concordant with expert practice, that an explicit filtering ledger renders inspectable what filtering otherwise removes without trace, and that cross-stage anomaly detection surfaces conditions execution monitoring misses. BaseCamp offers a generalizable blueprint for agentic automation of scientific data pipelines.

---


### 7. [Who Is Behind the Harness? Fingerprinting LLMs through Agentic Behavior](https://arxiv.org/abs/2609.28559)

**<font color=#1a73e8>作者：</font>** Chuyi Wang, Xiaohui Xie, Tongze Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLMs increasingly operate through coding-agent harnesses that inspect repositories, invoke tools, and modify files. Substituting the model behind such an agent can therefore change security-relevant decisions, including whether it verifies changes or recovers safely from failures. Existing LLM fingerprints largely infer identity from direct text or token distributions. In coding agents, these signals are mediated by system instructions, controller logic, tools, and execution feedback, limiting their transfer.
We present LIDAR (LLM Identification from Decisions and Actions at Runtime), an active black-box fingerprinting method for coding-agent execution. Three coding probe pairs expose post-edit verification, transient-failure recovery, and specification--test conflict resolution under controlled changes. LIDAR represents the resulting trajectories with complementary instance-level and distribution-level features and compares them with clean references using a lightweight probabilistic identifier. It requires no access to model weights, logits, or provider internals.
Across 36 models from seven families and two agent harnesses, LIDAR achieves high Top-1 accuracy and MRR and outperforms four existing fingerprinting and API-auditing baselines. Ablations confirm that the two feature levels, all probe pairs, and their controlled variants contribute. These results show that agent execution behavior provides model-identity evidence beyond final outputs.

---


### 8. [Don't Read the Log: Execution Traces Contaminate Verifiers in Video-Generation Agents](https://arxiv.org/abs/2609.28564)

**<font color=#1a73e8>作者：</font>** Jian Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic video-generation systems close a loop between a generator and a verifier: an LLM plans shots, calls a text-to-video model, and a multimodal judge decides whether the result satisfies the request. To diagnose where a long workflow fails, recent harnesses deliberately show the judge more than the video-the agent's execution trace, its plan, the narration it synthesized. We ask whether this auxiliary text moves the judge's verdict on purely \emph{visual} requirements, holding the frames fixed. On a benchmark of 109 generated two-event clips with manual labels, in which the requested event is either visibly completed or visibly missing, a trace that reports a successful tool call makes three open-weight Qwen-VL judges (7B, 8B, 32B) accept $78$--$90\%$ of the failures, up from $7$--$19\%$ without text, and a contradicting trace makes them reject up to $100\%$ of correct clips; an instruction to ``use only the frames'' does not remove the effect. Frontier closed judges are essentially unmoved on the same clips, showing that the vulnerability is a property of the judge's learned trust in tool logs rather than of the task. Plan-derived text carries no clip-specific information, so it can only shift a judge's operating point, and in a repair loop that shift becomes a cap on the true pass rate that no repair policy can exceed; the cap matches simulation to two decimals. In the loop, contamination is exploited without any adversarial agent: an honest LLM planner that always regenerates ends with a judge pass rate of $1.00$ and a human-labelled pass rate of $0.28$, and a pipeline in which a cheap checker writes its verdict into the trace launders that checker's errors into a stronger final judge ($0.69$ false accepts).

---


### 9. [DEEPO: Dual-Entropy Enhanced Policy Optimization for Hallucination in MLLMs](https://arxiv.org/abs/2609.28570)

**<font color=#1a73e8>作者：</font>** Yingxuan Zhuang, Miao Pan, Wangjie Gan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is widely used to sharpen reasoning in multimodal large language models (MLLMs), yet its effect on hallucination is uneven. We trace this to two weak points in the \emph{correction chain} from reward to parameter update. At the rollout level, hard queries---those with high semantic entropy---frequently produce unanimously wrong sample groups, collapsing the group-relative
advantage to zero exactly where hallucination risk is highest. At the optimization level, confident-but-wrong tokens are gradient-invisible: a categorical policy's expected score-gradient norm vanishes as its distribution sharpens, so the predictions that most need correction receive the weakest updates. We propose Dual-Entropy Enhanced Policy Optimization (DEEPO), a dual-stage enhancement combining signal
variance regularization with gradient preconditioning: semantic-entropy-triggered expert prefixes inject grounded continuations on high-uncertainty queries, providing direct supervision and restoring advantage variance, while advantage-sign-aware Renyi preconditioning counteracts logit-level saturation so correction reaches confident errors in the operational confidence regime. Both branches improve over GRPO individually; their interaction is statistically significant on VideoMMMU---the most complex long-horizon task in our evaluation suite (+4.0$, 95\% CI [1.1, 6.9])---and additive elsewhere. DEEPO reduces hallucination while preserving accuracy and training stability.

---


### 10. [Where Cyber Agents Struggle: Bottleneck Analysis of Multi-Stage LLM Agents](https://arxiv.org/abs/2609.28572)

**<font color=#1a73e8>作者：</font>** Saeedeh Lohrasbi, Mohammad Mamun, Ahmed Yehia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-stage LLM-based cyber agents may complete attack workflows while remaining brittle, costly, or reliant on incorrect interpretations of execution evidence. Success rates alone obscure inefficiency, adaptation through retries, and recognition of success or failure. We present an end-to-end diagnostic study of an Autonomous Adversary system with orchestrator, executor, and validator LLMs in enterprise-like lateral-movement scenarios. Six frontier models are evaluated across two scenarios and three modes: expert-defined, self-scaffolded, and fully autonomous. We assess validator consistency and evidence grounding; introduce a subtask-conditioned, cost-aware score for abnormal token use, retries, and runtime; and use comparative LLM-as-a-Judge analysis to identify planning deficiencies, including tool misalignment, plan similarity, over-specification, inadequate probing, and weak recovery. Validators are generally relevant and evidence-grounded but often nonspecific and overly optimistic. Bottlenecks cluster in credential and lateral-movement tasks, spread with scenario complexity, and vary more under full autonomy. Reliable evaluation must assess outcomes, evidence interpretation, resource use, and adaptation after failure.

---


### 11. [Persistent Billable State: Denial-of-Wallet Attacks and Defenses in Tool-Calling LLM Agents](https://arxiv.org/abs/2609.28585)

**<font color=#1a73e8>作者：</font>** Jinqian Zhang, Haojun Xia, Shujiang Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-step tool-calling LLM agents rely on host runtimes to preserve state across turns. When a runtime carries an external tool return into later model inputs, providers meter it again. An admitted malicious or compromised tool can thereby convert untrusted data into recurring victim-billed processing without victim credentials or local runtime privilege. We call retained content persistent billable state and formalize the host's decision over whether and how it enters later billable context as the persistent billable-state boundary.
We present the first systematic security study of this post-admission lifecycle. We derive six denial-of-wallet attack vectors and build DOW-BENCH, an end-to-end harness evaluated across six model families. Across 243 executions, usage telemetry shows that the maximum per-session cumulative input reaches 14,293x the session's first-call input. Controlled history-policy reruns isolate raw retention's contribution: retaining raw history increases mean effective session cost by 21.2-35.9%. Compression succeeds on 10/12 and 11/12 history-dependent tasks, versus 2/12 under deletion for each provider.
To govern this boundary, we combine deterministic history transformation with four host-side invariants that bound prompt mass, context growth, recursive opportunity, and cumulative spend before reingestion. The kernel contains every recurring attack in the 123-evaluation replay corpus. Across 24 Mistral Small 4 workflows, a progress-authorized policy achieves 22/24 oracle-verified task successes with no pre-completion interruptions, versus 13/24 under a fixed cap. Only 71 of 3,830 scanned MCP server and transport repositories expose any code-visible safeguard proxy, and none cover all four safeguard families. These results establish persistent billable state as a first-class security object and pre-reingestion as its host-owned control point.

---


### 12. [Agent Approval Laundering: Transitive Effects Beyond the Approved Invocation](https://arxiv.org/abs/2609.28586)

**<font color=#1a73e8>作者：</font>** Jinqian Zhang, Haojun Xia, Shujiang Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding-agent approval interfaces bind a human decision to a command or tool call, while developer tools execute the transitive workflow that invocation activates. Package installation can run lifecycle hooks and write files; an MCP call can exercise network authority. We call the resulting record-coverage failure approval laundering: the durable record names the entry invocation but omits effects exercised by its workflow.
We present the first systematic security analysis of this record-to-closure relation in agent systems. We formalize closure-bound approval over six effect classes and derive an information limit: identical policy-visible fields can require different effect-specific decisions, so no record-only policy can guarantee both. The Approval-to-Action Security Benchmark binds approval objects and decision-time metadata to post-execution evidence.
Across 111 fixed approval-object/trace pairs, residual records fall from 40 under explicit fields to 17 with command semantics and 13 with decision-time metadata. Across 11 fixed-SHA executions, the ladder reaches zero metadata residuals; two exact mappings recur across three product frontends. For prospective recovery, effect-bound records commit frozen, source-backed predictions and provenance before authorization. On 17 prespecified holdout workflows, predictions achieve 0.926 macro recall and 0.941 macro precision; binding them cuts residual effects from 10 to 3. A Claude Code PreToolUse integration carries the frozen record through the permission path without automatic approval. These results establish approval laundering as a measurable, recurrent record-coverage failure despite truthful invocation identity. They motivate binding each invocation before authorization to a source-backed prediction of its workflow's transitive effect boundary and preserving that binding with the decision.

---


### 13. [Learning to Discover Interesting Mathematics](https://arxiv.org/abs/2609.28603)

**<font color=#1a73e8>作者：</font>** Niket Patel, Ahmad Rammal, Amaury Hayat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, Large Language Models (LLMs) have been increasingly able to solve advanced mathematical problems, including many that have been open for decades. This opens the door to expansion of mathematical knowledge at unprecedented scale. Yet, while LLMs may be able to conjecture and prove more and more theorems, it remains open whether this new mathematical knowledge is interesting or useful. We define intrinsic interestingness of a theorem as the ratio between the length of its proof and the length of its statement. We show that this correlates strongly with an extrinsic measure of the downstream utility of a theorem. We identify the difficulty of a proof conditioned on a set of premises as a useful primitive for computing these metrics, and train a 27B model that predicts proof difficulty more accurately than frontier general-purpose models. Optimizing for our metric creates a model capable of producing more interesting theorems, while also reducing substantial or full overlap with Mathlib from 91.9% to 30.6%, showcasing the creation of more out-of-distribution math. We show that our system can generate candidate theorems, select the most interesting among them, and iteratively build on a self-expanding mathematical library. These metrics provide a practical and quantifiable signal for ranking conjectures and guiding proof search within formal mathematical libraries. Our framework provides a path towards self-expanding, machine-verified mathematical libraries that can choose worthwhile statements without relying on human-supplied targets.

---


### 14. [UO-FIE: Combining Exact-Label Supervision with Graded Utility for Factivity Inference](https://arxiv.org/abs/2609.28605)

**<font color=#1a73e8>作者：</font>** Xinchen Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Factivity Inference Evaluation 2026 (FIE2026) classifies Chinese context-hypothesis pairs into nine ordered factivity intervals. Its evaluation metric rewards both exact predictions and proximity to the correct interval, while 64.1% of the 566 training examples belong to a single class. In preliminary experiments, several mDeBERTa classification models predominantly predict the dominant class, whereas a Huber-regression baseline produces more predictions near the correct interval but fewer exact matches.
We introduce Utility-Oriented Factivity Inference (UO-FIE), a parameter-efficient system that combines exact-label supervision with graded utility. UO-FIE predicts a distribution over the nine classes and combines hard-label supervision, utility-based soft targets, scheduled class weights, and an ordinal loss. We evaluate expected-utility decoding in controlled comparisons and use ordinal calibration selected on out-of-fold predictions for the submitted system.
Based on Qwen3.5-9B with LoRA, UO-FIE ranks first in the fine-tuning track with a macro utility of 0.8316. A separate prompt-based ensemble ranks third in the non-fine-tuning track with a macro utility of 0.8450.

---


### 15. [Adversarial Closed-Loop Curriculum for Evolving Role-Playing Agents](https://arxiv.org/abs/2609.28609)

**<font color=#1a73e8>作者：</font>** Zheng Zhang, Liu Liu, Qi Chai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Role-playing agents based on large language models have been widely applied in areas such as personalized assistance and social simulation. Recent RL methods typically train on a fixed scenario pool collected before learning begins. This creates a distributional bottleneck: as the agent improves, the scenarios where it performs poorly also change, while the training distribution remains static. Therefore, we propose AdvRole, an adversarial context rewriting framework that turns role-playing RL into a closed-loop curriculum. AdvRole alternates between an Actor that learns to role-play and a Rewriter that edits character profiles and dialogue contexts into actor-specific hard scenarios. The Rewriter is trained with a performance-gap reward, which favors rewrites that reduce the current Actor's score relative to the original scenario. As a result, the scenario pool evolves with the Actor and continuously targets under-mastered regions of the character-context space. Experiments on three role-playing benchmarks covering English and Chinese, as well as a new multilingual benchmark we release, show that AdvRole consistently outperforms baselines.

---


### 16. [Reward Hacking Challenges Oversight of Autonomous Research Agents](https://arxiv.org/abs/2609.28614)

**<font color=#1a73e8>作者：</font>** Yue Huang, Zhangchen Xu, Yuchen Ma 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous research agents can design experiments, evaluate results, and write reports, giving them control over both a scientific result and the evidence used to support it. This creates a risk of reward hacking: meeting the reward criteria without achieving the intended goal. We study (1) how often models reward-hack without instructions to do so, (2) how effective and detectable their methods are when hacking is allowed, and (3) how they adapt when an LLM review panel returns its decision and reasons. Across 17 language models and 38 tasks, the spontaneous reward-hacking rate is 30.5% on open-ended research-pipeline tasks and 2.9% on task-specific kernels. When hacking is allowed on tasks whose pass thresholds exceed our best compliant baselines, 505/677 attempts (74.6%) are confirmed reward hacks: they both clear the threshold and receive mechanism-verification panel confirmation of an evaluation exploit. An LLM panel reviewing only submitted code and reported scores misses 33/505 confirmed hacks (6.5%). Direct methods that achieve the highest scores are often easy to detect, while less direct methods evade more often. In a five-round loop, the number of model-task pairs with an evasion rises from 7 to 56. Among 79 pairs evaluated under two feedback conditions, cumulative evasion reaches 40.5% with detailed feedback and 20.3% with generic rejection. The detailed condition includes the review decision, reasons, and attempt history, so this comparison does not isolate the effect of explanations. These findings highlight the need for stronger defenses, including metrics kept outside the agent's control and independent recomputation on data chosen to expose likely exploits.

---


### 17. [Benchmarking Argumentative Behaviour of LLMs: A Study of Defences Against Character Attacks](https://arxiv.org/abs/2609.28673)

**<font color=#1a73e8>作者：</font>** Ewelina Gajewska, Katarzyna Budzynska, Jaroslaw Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed as argumentative agents in persuasive dialogues, necessitating rigorous evaluation of their debating competence relative to human interlocutors. In this study, we focus on character attacks (ad hominem arguments), traditionally dismissed as fallacies, which play a pivotal role in political persuasive dialogues where ethos often rivals propositional content. Specifically, we investigate whether modern LLMs can replicate human competence to strategically use and respond to such attacks. We analyse a corpus of natural language political dialogues to identify defensive strategies human interlocutors naturally employ in ethos-centred debates and structure them into a dialogue game. Empirically, we benchmark LLM-generated dialogues against the ElecDeb60to16-fallacy corpus of U.S. presidential debates, contrasting human debaters' repertoire of defensive strategies with those of artificial agents. Results reveal a substantial difference: most LLMs rigidly prioritise logical defences, failing to exploit ethotic counterattacks as valid moves in political discourse. We argue that current safety fine-tuning constraints the strategic action space of these LLMs, making them unable to fully engage in naturalistic interactions within domains where character contestation is a normative expectation rather than a mere fallacy.

---


### 18. [Thinking Leakage: A Causal Audit of NoThink Post-Training in Hybrid Reasoning Models](https://arxiv.org/abs/2609.28682)

**<font color=#1a73e8>作者：</font>** Zehao Liu, Vasant G. Honavar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training hybrid reasoning models in NoThink mode has attracted growing interest as a way to improve performance while keeping inference fast. However, these gains may draw on thinking behavior already accessible through the base model's Think mode. We formulate this thinking leakage in a causal mediation framework and audit its contribution using bidirectional interventions along a simple base-derived activation direction. Across three models and three post-training methods on competition math benchmarks, we find that leakage is real, causal, and substantial: behavioral and representational analyses reveal shifts toward Think, steering the base model along this direction reproduces most of the post-training accuracy gain, and counter-steering a checkpoint removes a substantial share of what it gains. Across nine aligned checkpoints with positive NoThink gains, the resulting leakage ratio ranges from 42% to 79%. These interventions support a substantial causal contribution of thinking leakage. Our findings show that a post-training method's apparent advantage can therefore reflect greater drift toward Think, obscuring whether it improves capability within NoThink or more effectively re-invokes existing Think behavior.

---


### 19. [Beyond Surface Style: Aligning Multi-Turn User Simulators with Behavioral Consistency](https://arxiv.org/abs/2609.28690)

**<font color=#1a73e8>作者：</font>** Geng Chen, Ruotong Pan, Zhirui Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Faithful user simulation is fundamental to building, evaluating, and improving interactive AI at scale. However, plausible individual responses do not ensure that simulated users reproduce the intent evolution and outcomes observed in real interactions. We propose TRACER, a multi-turn user simulator that explicitly models users' evolving intent and learns to align simulated behavior with real interaction trajectories. TRACER is trained in two stages: supervised fine-tuning on real user dialogues, followed by multi-turn reinforcement learning. The RL stage combines hierarchical outcome- and trajectory-level rewards with deviation-aware advantage modulation, jointly mitigating reward sparsity and credit assignment in long dialogues. On real customer-service sessions organized into reference cohorts, TRACER-7B surpasses the strongest baseline by 11.4 conversion F1, while also achieving the lowest group-level conversion-rate error and semantic trajectory distance, and generalizing to out-of-distribution scenarios. Human Turing tests yield identification accuracy close to chance, supporting the perceived naturalness of generated conversations. Building on this simulator, we further introduce the Dynamic Marketing Benchmark, which jointly evaluates persuasion effectiveness and response quality of LLMs through simulated interactions, revealing that higher response quality does not necessarily correspond to higher conversion rates.

---


### 20. [Driving Epidemic Models with AI Agents: the Epydemix Agent Framework](https://arxiv.org/abs/2609.28692)

**<font color=#1a73e8>作者：</font>** Nicolò Gozzi, Ciro Cattuto, Alessandro Vespignani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence agents based on large language models provide convenient natural language interfaces to scientific software, but reliability is not automatic. Here we introduce the Epydemix Agent Framework, an additive layer over Epydemix, an open-source Python library for stochastic compartmental epidemic modeling. The framework extends the library with four capabilities to facilitate interaction with an AI agent: discovery of available models and parameters, preventive validation of a declarative scenario specification, execution through tested library code, and inspectability of results. These capabilities let an agent handle the entire modeling process, from the natural-language description of the scenario to quantitative results, figures, and interpretation of findings without writing custom code. Each step reads input files and saves results in a separate output bundle, making the process auditable and reproducible. First, we show the end-to-end workflow with a case study comparing vaccination strategies for a novel respiratory virus. Second, we assessed the framework across 50 agent sessions and five modeling tasks by comparing the agent use of the framework against the direct use of the Python interface. The framework reduced turns, output tokens, and cost on most tasks, unless it trades resources for per-point reproducibility.

---


### 21. [Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery](https://arxiv.org/abs/2609.28693)

**<font color=#1a73e8>作者：</font>** Michael Stettler, Benjamin Girardet, Jonas Canton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents struggle to scale safely when exposed to vast enterprise toolsets. Providing an agent with access to every internal tool leads to oversized context windows, degraded tool selection, and severe governance vulnerabilities - as system policies defined purely in prompts remain probabilistic advice rather than hard constraints. Existing mitigations, such as multi-agent domain delegation, decentralize audit logs and fail to guarantee policy compliance across sessions. We introduce skilder, a framework that packages capabilities into roles: bundles of skills, tools, and instructions, together with the limits that bound them. An agent begins with a minimal role catalog, learns the roles a task requires, and receives each role's skills, instructions, and tools through a single MCP server. Because tools reach the agent only inside learned skills, the same server enforces the scope of what was learned deterministically. We evaluate skilder against flat-context tool selection and multi-agent orchestration across 13 tasks using six models (10 runs each). Our results show that, when models completed discovery and issued a governed call, the skilder simulated authorization layer enforced governance boundaries: no unauthorized tool call or parameter violation (e.g., a spending-limit breach) executed. Aggregate task pass rates also reflect whether each model followed the discovery protocol and satisfied response-quality checks; those misses are not authorization failures. Furthermore, by allowing agents to dynamically acquire cross-role capabilities mid-task, skilder preserves problem-solving flexibility while providing hard system-level enforcement.

---


### 22. [LabFactory: Building and Evaluating Executable AI Labs](https://arxiv.org/abs/2609.28697)

**<font color=#1a73e8>作者：</font>** Jinge Wu, Hongjian Zhou, Mingde Zeng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific tasks specify a desired capability, but realizing it often requires building a computational system tailored to the task---acquiring data, designing representations, training models, implementing tools, and deciding how they are used at inference. We present LabFactory, a framework in which an AI builder turns a scientific brief into an executable AI lab: a task-specific solver that integrates models, knowledge resources, tools, and a controller behind a fixed interface. The builder develops and packages the lab in a metered workspace; a separate host then executes the delivered artifact on held-out inputs, with reference labels kept outside the solver's input interface, and scores its outputs under the task's protocol. This makes the delivered system, rather than the builder's account of its progress, the object of evaluation. We document 28 selected constructions across seven scientific task categories---from molecular and genomic prediction to physiological signals, clinical decision support, and biomedical text---whose delivered labs exceeded their configured reference values on all 33 subtests under host-side execution. Ten contain predictive models fitted during construction; the others assemble retrieval systems, executable analysis environments, and tool-driven workflows around a fixed platform LLM. Together they show that an AI agent can carry a scientific brief all the way to a working lab that can still be invoked, inspected, and checked after construction ends.

---


### 23. [How Spatial Biologists Direct and Verify AI-Assisted Analyses](https://arxiv.org/abs/2609.28723)

**<font color=#1a73e8>作者：</font>** Ella Hugie, Alexandra Irger, Chiara Schiller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Spatial biologists use visualization to assess computational analyses of tissue data. We examine how they direct and verify analyses when an AI agent performs this work. We synthesized workflows from fourteen contextual inquiries and conducted a formative pilot followed by an observational study with ten spatial biologists using Claude Science on their own data. Participants valued help with plotting, locating cells of interest, and tasks they found laborious or could not otherwise perform. Assessing the agent's work involved obtaining suitable evidence, sometimes through additional work in external tools, and interpreting it using knowledge of the tissue and its markers. Scientists also sought information about ongoing computation to decide how analysis should proceed. We contribute a workflow synthesis, an empirical account of scientists directing and verifying agentic analyses, and four design directions addressing execution control, familiar interactive views, source and execution information, and accessible verification across computing setups and experience.

---


### 24. [PTC-Bias: Phoneme-Level Temporal Competition for Bias Retrieval and Post-Decoding Correction in Speech LLMs](https://arxiv.org/abs/2609.28727)

**<font color=#1a73e8>作者：</font>** Zhiqi Ai, Han Cheng, Shiyi Mu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contextual biasing improves rare-word recognition in speech large language models (SpeechLLMs), but efficiently exploiting large bias lists remains challenging. We propose PTC-Bias, a two-stage framework based on phoneme-level temporal competition. At the prefill stage, PTC Retrieval performs frame-synchronous phoneme decoding and temporal competition among candidate pronunciations, producing a compact bias-word shortlist and corresponding speech intervals. After SpeechLLM decoding, PTC Correction conducts a second local competition between the retrieved candidates and mismatched transcript spans within these intervals. Selective correction reduces near-homophone and word-segmentation errors while preserving correct transcriptions. Both stages share the same phoneme posteriors and require no additional SpeechLLM forward pass. Experiments on LibriSpeech show consistent gains across two SpeechLLMs and bias lists of up to 2000 words. With Prompt-SLAM-ASR-7B and 2000 bias words, PTC-Bias reduces B-WER by 23.4%/23.9% relative to CTC-Filter on test-clean/test-other, while keeping U-WER nearly unchanged.

---


### 25. [GeoNLI - A Natural Language Interpreter for Satellite Imagery](https://arxiv.org/abs/2609.28741)

**<font color=#1a73e8>作者：</font>** Ashutosh Gandhe, Anupam Rawat, Geet Sethi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal multitasking models have shown strong performance on remote sensing datasets. However, because these models are trained on heterogeneous data and vary across tasks, designing a unified model that performs well in captioning, visual question answering (VQA), and visual grounding remains challenging.
In this work, we evaluate several models on the VRS Bench and NWPU-VHR-10 datasets. The EarthMind model demonstrates strong results in both captioning and VQA. For grounding, we propose multiple pipelines - RemoteSAM-SAM-v1, RemoteSAM-SAM-v2, and DiffuSAM - and ultimately adopt a majority-voting ensemble across EarthMind, RemoteSAM, SAM3, Falcon, RemoteSAM-SAM3-v1, RemoteSAM-SAM3-v2, and DiffuSAM predictions.
Our unified, modular pipeline integrates advanced SAM variants with multimodal LLMs to jointly perform captioning, VQA, and grounding. It achieves 82% accuracy on captioning and 83.32% on VQA, with 90.94%, 52.04%, and 92.06% for binary, numeric, and semantic question types respectively. For grounding, it attains 64.94% accuracy. By combining diverse VLMs with our custom RemoteSAM-SAM3 models through ensemble majority voting, the system delivers more accurate and consistent remote-sensing understanding than task-specific approaches.

---


### 26. [Technical Manual for Toolkit for Confidence-Corpus Consistency via Fine-Tuning on a Fabricated Corpus](https://arxiv.org/abs/2609.28747)

**<font color=#1a73e8>作者：</font>** José Luciano Verçosa Marques, Frederico Jorge Heitmann, Daniel Omar Perez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language model's confidence in an answer is often read as a proxy for how well it knows the corresponding fact. This manual documents an open toolkit built to test that reading directly: a small causal language model is fine-tuned on a corpus that consistently asserts one fabricated arithmetic answer for each of the 81 single-digit addition pairs, and its post-fine-tuning confidence in each fabricated answer is compared against its own pre-fine-tuning confidence in the corresponding true answer, using an unchanged measurement procedure throughout. We describe and justify every pipeline stage, fact-space generation, token-length-aware confidence measurement, baseline validation, corpus construction, fine-tuning, and paired before/after comparison, together with the confound each is meant to rule out, among them tokenization asymmetry between single- and double-digit answers and the difference between an answer merely losing its edge and one being actively suppressed. This manuscript is a methodological and implementation reference: it documents the instrument and does not report or interpret the outcome of any specific run. The toolkit and its pinned dependency environment are archived separately (Section 9) under a persistent identifier, to be cited as an instrument by work that produces and interprets empirical results with it.

---


### 27. [Small yet Assistive: Spatially-Aware Post-Training for Low Vision](https://arxiv.org/abs/2609.28757)

**<font color=#1a73e8>作者：</font>** Rishabh Choudhary, Shreyansh Raj, Umesh Goyal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An estimated 1 billion people worldwide live with vision impairment, yet current vision-language models (VLMs) produce descriptions too vague for safe navigation by blind and low-vision (BLV) users. Large VLMs can generate high-quality audio-description-compliant narrations but cannot run on mobile devices; small VLMs offer competitive latency but lack spatial detail, directional cues, and hazard awareness for navigational assistance. We present Smol-VL-BLV, a compact VLM for blind and low-vision users that closes this gap using a 500M decoder transformer model and two post-training mechanisms: (1) teacher-student distillation and (2) Group Relative Policy Optimization (GRPO) with a composite BLV reward targeting directional language, metric distances, and hazard detection. Because multi-stage post-training can induce catastrophic forgetting, we add a lightweight finetuning stage after the last stage GRPO finetuning to recover general descriptive quality while preserving BLV-specific spatial grounding. Our best model substantially outperforms the baseline across various benchmarks, including tasks: VQA, BLV captioning, OCR, and latency. Compared with the baseline for relative improvement, it improves the Spatial score gain of 19.3%, and the Social score gain of 14.8%. It also increases OCR-Bench by 101.5%, and raises TextVQA accuracy by 44.2%. These results show that BLV-focused post-training improves both accessibility-specific spatial grounding and general visual-text reasoning. Deployed on a mid-range Android smartphone via Mixed-Precision Quantization, the model remains approx. 450 MB and runs entirely on-device, offline and without network dependency, generating descriptions with latency dependent on host hardware capabilities. Our model, dataset, and code is publicly released at this https URL

---


### 28. [Reinforcement Learning with Verifiable Rewards for Small Search Agents](https://arxiv.org/abs/2609.28765)

**<font color=#1a73e8>作者：</font>** Gaurisankar Jayadas, Aske Plaat, Álvaro Serra-Gómez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) performs well on problems with clear rewards, such as mathematics and coding, but whether it also works where the reward is less clear remains open. The reason-over-search recipe applies RLVR to open-domain question answering, where retrieval grounds the answer and a match against the reference supplies the reward. So far it has been demonstrated on large models, and below one billion parameters only with distillation from a larger teacher. We test the recipe on a small model. We train Qwen3.5-0.8B with Group Relative Policy Optimization (GRPO) and an interleaved Wikipedia-search tool on MuSiQue, varying only the reward across three shapes over three seeds each, and we evaluate every checkpoint held-out on a seven-benchmark question-answering suite. The recipe works: the best run reaches 0.352 average exact match against a 0.092 untrained floor, a 3.8-fold gain, with no distillation step in the training loop. The reward shape also matters. The Search-R1-faithful exact-match-only reward is the worst of the three at every seed at the matched training horizon, and it is worst even on exact match, the metric it directly optimises. We conclude that the sparse exact-match reward, RLVR's default in mathematics and code, is the wrong starting point for models of this size. The reason-over-search setting can supply a suitable reward for RLVR on small models, but small-model RLVR needs its own reward-design study rather than a scaled-down copy of a large-model recipe.

---


### 29. [Agent Memory with Episodic Retrieval for Financial Decision-Making](https://arxiv.org/abs/2609.28771)

**<font color=#1a73e8>作者：</font>** Nuoyue Xu, Jiang Liu, Wenxuan Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong capabilities in financial analysis and reasoning, inspiring recent advances in agent-based trading frameworks. While these systems show promise, prior approaches either emphasize long-horizon forecasting or operate as stateless analyzers, limiting their applicability to the demands of trading in complicated settings. To address these gaps, we introduce META (Memory Enhanced Trading Agent), the first RAG-like episodic-memory-augmented multi-agent framework for financial decision making. META integrates a family of specialized indicator agents (e.g., Trend, MACD, Stochastic, RSI, SMA, AVWAP, Heikin-Ashi) with a Decision Agent that fuses their reports, and a Memory module that retrieves and updates past trading episodes encoded as market state embeddings with outcomes and reflections. By recalling relevant experiences and adaptively reweighting signals under similar market regimes, META achieves improved directional accuracy and robustness under short-horizon evaluation. Our results demonstrate that episodic memory provides a powerful mechanism for regime-aware, interpretable, and low-latency decision-making in trading and decision making. The code of this project is released on GitHub.

---


### 30. [Script Choice in LLMs: Evidence for Late-Layer Commitment](https://arxiv.org/abs/2609.28784)

**<font color=#1a73e8>作者：</font>** David Kletz, Sandra Mitrović, Itay Sabato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we investigate how script knowledge is distributed across the layers of LLMs using two complementary interpretability methods: logistic regression probing and logit-lens analysis. Our probing experiments reveal a clear asymmetry: both the input script and the instructed output script are encoded in the earliest layers of the network, while, in contrast, commitment to the actual output script emerges only in the final layers, with the model's intermediate representations defaulting to Latin throughout most of the layers. This two-stage process is confirmed by logit-lens analyses, which show that script commitment consistently occurs at the very last layers of the LLMs. Together with the weaker script-following performance observed in smaller models, these results form a converging body of evidence linking script commitment to model depth, with broader implications for the design of sufficiently deep, inclusive multilingual architectures.

---


### 31. [DrGait: Biomechanically Grounded Visual Reasoning for Interpretable Clinical Gait Analysis](https://arxiv.org/abs/2609.28796)

**<font color=#1a73e8>作者：</font>** Xiangyu Yin, Shiqi Wang, Abrar Alamri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current automated gait analysis for clinical applications relies on uninterpretable black-box classifiers. Although Vision-Language Models (VLMs) offer strong reasoning capabilities, applying them directly to gait videos often leads to hallucinations, because they struggle to measure subtle geometric deviations from raw visual contexts. To address this, we introduce DrGait, a training-free agentic framework that shifts the VLM's role from a direct visual reasoner to a clinical planner. DrGait decouples semantic reasoning from geometric perception through a structured Triage-Verification-Synthesis (TVS) workflow. Given an input video and a set of basic spatiotemporal metrics, the DrGait agent first performs a heuristic triage to propose diagnostic hypotheses, which are then verified by autonomously calling deterministic biomechanical tools that operate on reconstructed 3D mesh trajectories, segmented 2D pose tracks, and event-centered video evidence. Finally, a closed-loop mechanism recursively updates the agent's reasoning context based on the feedback. By anchoring VLM's reasoning in verifiable geometric and temporal measurements, DrGait reduces hallucinations, achieving competitive diagnostic accuracy while generating transparent and audit-ready clinical reports.

---


### 32. [Stream Recursion Model (SRM)](https://arxiv.org/abs/2609.28809)

**<font color=#1a73e8>作者：</font>** Asael Sorensen, Charles Brock, David Chamberlain 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability seeks to make verifiable statements about the internal behavior of large language models (LLMs). Many interpretability techniques struggle to scale with the increasing size and depth of architectures. Our solution to this is to introduce smaller models with structures that lend themselves to interpretability. In this work, we introduce the Stream Recursion Model (SRM), a modification of the Hierarchical Reasoning Model (HRM) designed to expose internal computational structure while remaining scalable. SRM organizes computation into multiple interacting latent streams that are updated through recursive refinement, enabling direct analysis of stream dynamics, causal contribution, and routing behavior. SRM achieves performance comparable to GPT-2 on a per-parameter basis. Our analysis reveals consistent and distinct behavior across streams, indicating structured specialization and interaction. These results suggest that SRM provides a practical architectural foundation for scalable mechanistic interpretability and opens up promising avenues for future research in both reasoning performance and interpretability.

---


### 33. [Signals of AI Hallucination: Designing Hallucination-Aware Cues for Embodied Conversational Agents in VR](https://arxiv.org/abs/2609.28812)

**<font color=#1a73e8>作者：</font>** Xiaoran Yang, Yang Zhan, Xie He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM-powered conversational agents (CAs) often present uncertainty and provenance cues alongside their responses to help users assess response reliability and identify potential hallucinations. In immersive environments such as Virtual Reality (VR), CAs often take the form of speech-based embodied conversational agents (ECAs), where uncertainty and provenance cues cannot rely on persistent inline text and may be missed or disrupt comprehension when delivered through speech. We conducted a within-subjects study (N = 24) to compare three designs for presenting the hallucination-awareness information (uncertainty and provenance) in ECAs in VR against a no-cue baseline: embodied cues using gestures and posture, icon cues using visual indicators, and text cues using color-coded text with inline citations. We evaluated how these designs affect users' ability to identify hallucination-related information, trust in the ECA, and interaction experience (immersion and task load). Our results show that all three designs support users in identifying hallucinations. Embodied cues were associated with higher trust and immersion, text cues offered clearer interpretability, and icon cues preserved relatively good interpretability while causing less disruption to immersion compared with embodied cues and text cues. This work contributes to the VR and AI research community by comparing different designs of hallucination cues in immersive ECA settings and examining how they affect users' ability and experiences to identify hallucinations. It also offers practical insights and design implications for developing future hallucination-awareness interfaces for ECA.

---


### 34. [CinematicVQA: Benchmarking Film-Grammar Reasoning in Large Vision-Language Models](https://arxiv.org/abs/2609.28813)

**<font color=#1a73e8>作者：</font>** Shuo Xing, Pooja Verlani, Balu Adsumilli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cinematography, the craft of visual storytelling through framing, lighting, and camera operation, fundamentally shapes how audiences perceive and emotionally engage with video content. While Large Vision Language Models (LVLMs) have made remarkable progress in video question answering, existing benchmarks primarily focus on identifying low-level techniques rather than understanding their storytelling impact. To address this, we introduce CinematicVQA, the first-of-its-kind benchmark for cinematic video understanding that goes beyond technique recognition to evaluate film-grammar reasoning, utilizing our introduced Cinematic Scene Graph (CSG), a structured representation that links filming techniques to their perceptual effects and narrative functions. Through comprehensive evaluation of state-of-the-art LVLMs, we reveal a striking semantic gap: models consistently perform higher on describing visual presentations than on identifying the underlying techniques. Surprisingly, Chain-of-Thought prompting fails to provide consistent gains and degrades performance for most models, suggesting that current LVLMs lack sufficient cinematic domain knowledge to benefit from step-by-step reasoning. Fine-tuning on \textsc{CinematicVQA-train} yields consistent improvements, particularly for narrative function and multi-hop reasoning. Overall, \textsc{CinematicVQA} serves both as a rigorous benchmark for cinematic evaluation in LVLMs and as a practical dataset for training more film-aware video models.

---


### 35. [COILD: An Indic-Centric Parallel Corpus and Benchmark for Machine Translation Across Indian Languages](https://arxiv.org/abs/2609.28826)

**<font color=#1a73e8>作者：</font>** Kshetrimayum Boynao Singh, Nitin Kumar Mishra, Palash Pratim Dutta 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine translation (MT) for Indian languages remains constrained by the limited availability of high-quality, Indic-centric parallel corpora and evaluation benchmarks. Existing multilingual resources are largely constructed from English-pivot content and often fail to capture the linguistic diversity, cultural complexity, and domain-specific characteristics of Indian languages. We present COILD, an Indic-centric parallel corpus comprising over 1.16 million human-translated and human-verified sentence pairs, covering 20 Indian language pairs across the Indo-Aryan, Dravidian, Tibeto-Burman, and Austro-Asiatic language families. The corpus is built entirely from original Indian language sources collected from licensed repositories spanning eight domains with direct real-world applicability. Furthermore, we introduce a domain-centric benchmark comprising 2,000 expert-verified sentences to enable consistent multilingual and cross-lingual evaluation across Indian language pairs. To validate the effectiveness of COILD, we fine-tune two representative multilingual neural machine translation models, IndicTrans2-Distilled and NLLB-200. Experimental results demonstrate consistent improvements across language pairs, domains, automatic evaluation metrics, and human evaluation, highlighting the effectiveness of high-quality Indic-centric supervision. COILD provides a valuable training and evaluation resource for advancing multilingual machine translation and future multilingual language models for Indian languages.

---


### 36. [M$^2$PFN: End-to-End Disentangled Alignment for Generalizable Multimodal In-Context Learning in Alzheimer's Disease](https://arxiv.org/abs/2609.28836)

**<font color=#1a73e8>作者：</font>** Lujia Zhong, Shuo Huang, Jianwei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While various multimodal methods combining imaging and tabular data for Alzheimer's disease (AD) diagnosis were proposed, they are often limited in generalization across cohorts. In-context learning (ICL) has demonstrated excellent generalization performances and high flexibility in foundational tabular models such as TabPFN. To extend TabPFN's ICL to multimodal AD analysis, the main obstacle is that TabPFN is meta-trained on synthetic tabular priors that do not naturally match the statistical structure of image-derived features. We propose M$^2$PFN, an end-to-end framework that turns this tabular foundation model into a multimodal AD predictor. M$^2$PFN (i) performs differentiable inference through TabPFN's transformer, back-propagating task gradients into 3D-MRI and tabular encoders; (ii) aligns the two modalities into a shared subspace, via disentanglement and a contrastive objective, matched to the ICL engine's prior; and (iii) folds in a frozen tabular-only prediction through a learnable gated shortcut. Because the ICL engine stays frozen, its in-context mechanism is preserved for test-time generalization, while end-to-end training shapes the encoders into features it can exploit. On ADNI ($n=2240$, three-class CN/MCI/AD), M$^2$PFN attains $65.55\%$ macro-F1 and $82.21\%$ macro-AUC, surpassing a comprehensive set of unimodal and multimodal baselines. By swapping only the head for a TabPFN regressor, the same architecture regresses baseline MMSE on a $1250$-subject sub-cohort to test MAE $1.743$, outperforming every multimodal baseline. On two external cohorts (OASIS-3 and SCAN) with no retraining, M$^2$PFN achieves the best AUC and the lowest MMSE MAE across all baselines, and transfers even when the cognitive instrument changes.

---


### 37. [Blockchain-Enabled Artificial Intelligence and AI Agents for Secure Data Sharing and Cybersecurity Applications](https://arxiv.org/abs/2609.28843)

**<font color=#1a73e8>作者：</font>** Harsh Verma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain and artificial intelligence (AI) are converging into a single infrastructural layer for securing data sharing, model integrity, and autonomous decision-making across distributed systems. This paper presents a meta-synthesis that draws together four constituent studies covering adversarial machine learning, AI-powered anomaly detection in cloud environments, automated vulnerability patching by multi-agent large language model (LLM) pipelines, and the broader landscape of securing AI systems across their lifecycle and situates their findings within the emerging literature on blockchain-enabled AI and autonomous AI agents. Each constituent study addresses a distinct point of failure in modern AI-driven security operations: the integrity of training data and model behavior, the reliability of real-time monitoring, and the trustworthiness of automated code remediation. We argue that blockchain's properties of immutability, decentralized consensus, and verifiable provenance directly address a gap common to all three: the difficulty of establishing trust in data, models, and autonomous agents that operate without a central authority. Building on real-world research on blockchain-secured data sharing, federated learning, and multi-agent coordination, we propose a layered reference architecture that couples adversarially hardened models, blockchain-anchored data provenance, AI-driven anomaly detection, and smart-contract-governed multi-agent remediation. We conclude by identifying open problems in scalability, privacy-transparency trade-offs, and the governance of autonomous agents that must be resolved before such integrated systems can be trusted in production-critical environments.

---


### 38. [LastOPD: Taming Collapse in Latent On-Policy Distillation](https://arxiv.org/abs/2609.28845)

**<font color=#1a73e8>作者：</font>** Jie Yang, Zhengyu Fang, Zelin Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) corrects a student on the responses it writes, but its signal is the teacher's next-token distribution: it tells the student what the teacher says but misses how it thinks. Latent supervision promises the missing part by aligning the student's latent states to the teacher's. Recent methods such as OPRD bring this signal into on-policy distillation. However, we observe two failures of this recipe when distilling Qwen3-4B and Qwen3-8B into Qwen3-1.7B-Base. Early gain, late collapse: latent supervision alone lifts MATH-500 accuracy from 25 to 46 in 10 steps, but subsequent training degrades performance down to 11 with no recovery. Better alignment, worse behavior: although the alignment metric steadily improves throughout this collapse, the most aligned model turns out to be the worst performing. Further analysis suggests a mismatch in how the latent signal is applied: layers paired by depth play different roles in the two models, so continued alignment may pull the student toward teacher states it cannot understand. To address this, we propose LastOPD, which applies the latent signal only at the last-layer state, the common interface both LM heads read, and only during a 10-step crossfade into token-level OPD. This keeps the useful part of the latent signal and hands the student to token-level supervision before the collapse sets in. Extensive experiments show that LastOPD improves MATH-500 over token-only OPD by 5.55 and 4.02 points with the 4B and 8B teachers, leads on most held-out datasets, and reaches the final score of token-only OPD in about half the steps. Code is available at this https URL.

---


### 39. [RECLAIM: Can Agents Reproduce the Claims of Machine Learning Papers?](https://arxiv.org/abs/2609.28850)

**<font color=#1a73e8>作者：</font>** Mithil Salunkhe, Haochen Ding, Samridhi Verma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reproducing a machine learning paper involves most research steps, from installing software and debugging to running experiments, work that AI agents increasingly do. We introduce RECLAIM, a benchmark of 100 NeurIPS 2025 papers that can be rebuilt yearly from new conferences. For each paper we fix in advance the result to reproduce, what counts as a successful reproduction, and a GPU-hour budget. An agent must reproduce that result using the paper and whatever its authors released. What the authors released decides the difficulty tier. Run-tier releases include code, data, and weights; Retrain-tier releases lack weights, so the agent trains the model; Reimplement-tier releases lack code, so the agent writes it. A separate language model grades runs from logs and outputs rather than agents' reports. We run four agents once per paper; the best agent in each tier reproduces only 41% of Run-tier papers, 27% at Retrain, and 15% at Reimplement, where every agent does worst. Failed attempts use on average 29% of their budget, so most stop with budget left. The most common agent error is writing the method without checking any part against the paper's numbers, in 63 of 400 runs.

---


### 40. [Looks the Same, Answers Differently: Flip-Direction Steering for Robust Vision-Language Reasoning](https://arxiv.org/abs/2609.28851)

**<font color=#1a73e8>作者：</font>** Yeonsung Jung, Joonhyun Jeong, Hoang Pham 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) achieve strong visual reasoning performance, yet subtle changes from routine image capture and processing can alter their reasoning trajectories even when images appear nearly identical. In long-horizon generation, the resulting activation shifts may accumulate across decoding steps, progressively altering reasoning tokens and ultimately changing the final answer, a phenomenon referred to as answer flips. To address this instability, we propose FlipDir (Flip-Direction Steering), a training-free inference-time method that estimates a low-rank flip-inducing activation subspace from contrastive pairs of original and answer-flipping inputs and selectively steers hidden states during decoding. A margin-based gate limits subspace attenuation to uncertain decoding steps, recovering original predictions while preserving stable ones. To evaluate robustness beyond accuracy or consistency on fixed test sets, we introduce VisFlip, a benchmark framework that constructs evaluation groups for a target model and visual variation setting to separately assess recovery of original predictions and preservation of stable ones. VisFlip spans nine dataset-variation combinations across scientific reasoning, robot-scene understanding, and medical VQA, covering subtle visual variations common in each domain. Experiments across 18 settings demonstrate that FlipDir consistently outperforms existing methods on the combined recovery and preservation metric. We will make our code publicly available.

---


### 41. [Persuaded, Not Informed: Incentive-Misaligned Witnesses Defeat In-Context Grounding](https://arxiv.org/abs/2609.28854)

**<font color=#1a73e8>作者：</font>** Rahul Balakavi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-model agents increasingly answer questions over customer-relationship management (CRM) records, such as whether to qualify a sales lead. We identify a failure mode not addressed by a stronger model: when the context contains an assertion by a party with an incentive toward optimism - here the sales representative, a witness recorded in the CRM - the model treats the assertion as evidence and clears deals the company's own records deem unacceptable. Across 100 lead-qualification tasks from CRMArena-Pro, the representative asserts an acceptable timeline in every call and an acceptable budget in 76; on the 31 tasks where such an assertion contradicts the price list and installation policy, a model reading only the transcript clears the deal in 29 of 31 cases. The signature is consistent across seven models from four providers (misled on 87-97%); scale and explicit reasoning confer no resistance. Only 3 of 35 genuine failures involve no assertion: the failure is persuasion, not missing information. We contribute a diagnostic method rather than an architecture: (i) a bucket analysis that separates persuasion from information gaps, (ii) a same-information control showing that supplying the records to the model lowers strict accuracy from 41 to 18 while raising recall - precision collapses - and (iii) a compute-step control that holds extraction fixed and varies only who computes Budget and Timeline. The margin ranges from 42 points on an inexpensive model to 2-5 points on models that already compute correctly; on the strongest models the arms are within confidence intervals, so the pattern is a consistent direction and a soundness property, not a proved performance floor. We pre-specify a generalization test that returns a negative result, characterize the precondition (a policy exactly specified in the inputs), and release all evaluation artifacts.

---


### 42. [MEVL-STP: Multi-Encoder and Vision Language Model for Arbitrarily Shaped Scene Text Spotting](https://arxiv.org/abs/2609.28857)

**<font color=#1a73e8>作者：</font>** Aman Anand, Partha Pratim Roy, Shivakumara Palaiahnakote  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene text spotting remains challenging for arbitrarily shaped text instances such as curved signs and dense multi-oriented characters in natural images, where tightly coupled architectures propagate localization errors directly into recognition failures. We present a two-stage pipeline that combines multi-encoder segmentation with vision-language model recognition to address this problem. In the detection stage, six frozen vision encoders (CLIP, DINOv2, SigLIP, EVA-CLIP, SAM, and ConvNeXt) extract complementary features spanning semantic, spatial, and texture spectra, which are fused through a trainable hierarchical Feature Pyramid Network with channel attention and decoded via a deep-supervision Progressive Scale Expansion network to generate precise instance-level text masks. By keeping the encoders frozen, their independently learned feature spaces remain orthogonal during fusion, preventing the feature homogenization that degrades boundary precision in single-backbone detectors. The detection stage produces tight polygon masks that conform to the actual shape of curved and arbitrarily oriented text, rather than axis-aligned rectangles that inevitably include background content. In the recognition stage, these polygon-masked crops isolate the target text from surrounding clutter, allowing a Qwen3-VL-8B-Instruct model, fine-tuned via Low-Rank Adaptation on polygon-cropped scene text, to focus purely on reading the text without interference from neighbouring words or background noise. Without any synthetic pretraining data, our method achieves 91.99% detection F-measure and 85.86% end-to-end H-mean on CTW1500, setting a new state of the art and achieving strong performance on Total-Text and ICDAR 2015 without any synthetic training data. Code is available at this https URL

---


### 43. [Human-AI-Powered Hypothesis Testing: Cost-Aware Selective AI Scoring and Sequential Human Escalation](https://arxiv.org/abs/2609.28859)

**<font color=#1a73e8>作者：</font>** Dae Woong, Xuejun Zhao, Stefanus Jasin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as inexpensive judges to evaluate outputs, label data, and assess whether a system meets a desired quality standard. Yet using AI judgments for formal statistical inference is fundamentally different from simply treating them as ground-truth labels: AI evaluations can be biased or noisy, and rigorous hypothesis testing requires explicit control of type-I and type-II errors. We study how to use AI judgments, together with selective human verification, to conduct a valid hypothesis test at minimum cost. We consider a population of items with hidden binary labels. After choosing a fixed pool of items, the decision maker can selectively query AI, send an item directly to a human, escalate an AI-scored item to a human after observing the AI report, or stop once sufficient evidence has accumulated. We derive an information-theoretic lower bound that captures the minimum cost of achieving prescribed testing errors and characterizes the value of AI information and human verification through a report-dependent information frontier. Motivated by this characterization, we develop SCALE, a sequential cost-aware policy that combines selective AI scoring with adaptive human escalation. SCALE is valid at finite sample sizes and matches the lower bound to first order as the target error probabilities vanish. We further extend the framework to an unknown AI-output model using paired AI-human pilot data. Numerically, SCALE approaches Human-only or AI-only testing when one source clearly dominates, while achieving its largest savings when inexpensive AI judgments and selective human verification are both valuable.

---


### 44. [Direction-Scale Decomposition in Action Representation: Rethinking What to Tokenize for Vision-Language-Action Models](https://arxiv.org/abs/2609.28865)

**<font color=#1a73e8>作者：</font>** Yufei Duan, Hang Yin, Alberta Longhini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action representation plays a central role in discrete-token vision-language-action (VLA) learning but remains underexamined. Under conventional pose-increment representations, action tokens are sensitive to execution speed and dataset-specific normalization, potentially obscuring geometric structure shared across demonstrations and datasets. We introduce Direction-Scale Decomposition (DSD), an action representation that decomposes translation and rotation increments into direction and scale components before tokenization. DSD isolates motion direction while retaining magnitudes in separate scale channels. We evaluate DSD with uniform binning (BIN) and BEAST, a B-spline-based tokenizer, in simulation and real-world manipulation under both single-dataset and mixed-dataset training. On LIBERO, DSD improves average success rates with both tokenizers. On SimplerEnv, DSD-BIN outperforms BIN by 10.3 percentage points in overall success rate under mixed-dataset training. Real-robot experiments further show gains both with and without robotics pretraining. These results support DSD as an effective action representation for discrete-token VLA models and suggest its potential to mitigate performance degradation when training on large and diverse dataset mixtures. Our project page with additional resources is available at this https URL

---


### 45. [Forecast-Dojo: Replayable Environments for Benchmarking and Training LLM Forecasting Agents](https://arxiv.org/abs/2609.28876)

**<font color=#1a73e8>作者：</font>** Liqin Ye, Haorui Wang, Fardin Ahmed 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Forecast-Dojo, a replayable environment for benchmarking and training LLM forecasting agents. It combines resolved prediction-market questions with dated news, allowing agents to research an event and revisit their predictions at successive historical dates. The same tasks and tools support repeated evaluation, collection of training interactions, and feedback from recorded outcomes without waiting for new events to resolve. Forecast-Dojo contains 1,568 Polymarket events, split by time into training and evaluation periods, and 18.8M dated news articles. In an evaluation of 12 models, research tools lower Brier score for all 12. Forecasts also improve as events unfold, with the largest gains at steps where more newly dated evidence is recorded. Every model still trails historical market forecasts in both Brier score and accuracy. A belief notebook carried between dates lowers research cost but does not consistently improve forecast quality. Beyond evaluation, Forecast-Dojo provides interaction trajectories and outcome feedback for agent learning, with supervised fine-tuning as a proof of concept.

---


### 46. [Characterizing LLM-Based Family Education through the Lens of Activity Theory: A Scoping Review of the HCI Literature](https://arxiv.org/abs/2609.28886)

**<font color=#1a73e8>作者：</font>** Lan Luo, Yuqi Liang, Jie Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly involved in family education, yet HCI has not systematically explained the educational interactions that emerge around them. This scoping review analyzes 53 HCI studies from 6,540 records across 19 venues. Using activity theory and AODM, it relates participants and educational objects to mediation, labour, and rules. We find that the literature centers on child--parent interaction and on language, AI literacy, and relational learning. The introduction of LLMs enabled conversational, embodied, and spatial systems to generate support from the context of an unfolding interaction. LLMs redistributed educational labour, while family and institutional rules left parents and professionals responsible for interpreting outputs and deciding how they entered practice. Evidence across families and educational purposes remains limited, especially on sustained personalization, repair labour, and how families negotiate authority and rules. The review offers a framework explaining how LLM capabilities become organized through family participation.

---


### 47. [Codetta: High-Capacity, Keyless, and Undetectable Multi-Agent Collusion](https://arxiv.org/abs/2609.28900)

**<font color=#1a73e8>作者：</font>** Qi Pang, Virginia Smith, Wenting Zheng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems built on large language models (LLMs) are increasingly deployed in high-stakes settings such as finance, healthcare, and software engineering, where agents coordinate through natural-language messages. The same channels, however, let colluding agents exfiltrate confidential information or coordinate unauthorized actions, and steganography can hide such communication inside outputs that look ordinary to an auditor reading the transcript.
Existing provably undetectable LLM steganography protocols are not suited to realistic deployments. High-capacity schemes assume a symmetric setting where the receiver can reproduce the sender's output distribution, the state-of-the-art protocol for asymmetric agents has very low capacity, and most approaches rely on a pre-shared secret key.
We make the threat of undetectable agent collusion concrete with Codetta, a high-capacity steganographic protocol for independently deployed agents in realistic asymmetric settings. Codetta combines a shared public model that estimates the communication channel, a sampling mechanism that preserves the sender's output distribution, and an adaptive error-correcting code. It further removes the pre-shared key through a steganographic key exchange that lets independently deployed agents establish a shared key while keeping the transcript computationally indistinguishable from ordinary model outputs.
Across three agent workloads and three sender models, Codetta achieves up to $94\times$ the capacity of the state-of-the-art asymmetric protocol, and its key exchange establishes a shared key with about 80k visible tokens at an empirically certified failure probability of at most $4.1\times 10^{-3}$. These results show that effectively undetectable collusion is becoming feasible between independently deployed agents, so auditing must go beyond inspecting communication transcripts.

---


### 48. [Control the Harness, Control the Cost: Routing and Governing AI Coding Agents in the Enterprise](https://arxiv.org/abs/2609.28919)

**<font color=#1a73e8>作者：</font>** Arian Abbasi, Alan Aqrawi, Ted Kwartler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harnesses, the products that run AI coding agents, are multiplying, and enterprises are rolling them out to their employees: what started as pilots with a few hundred seats is scaling to tens of thousands. Most enterprises do not build these harnesses but buy them from large vendors, such as Anthropic's Claude Code or OpenAI's Codex. A harness decides which model answers, what the model reads, how the prompt cache is used and which subagents run, so it picks the rate on the price sheet and sets the volume bought at it. Enterprises that keep a proprietary or untuned harness at its defaults inherit these choices and their bill. We build a fast, customisable router in which Jev, a classifier with calibrated probabilities, labels every prompt against a bring-your-own taxonomy of agentic requests. Because one user turn is many requests over a prompt cache that belongs to one model, the router moves work only where no running conversation has to rebuild its cache: at session start, in side lanes and at subagent launch. From the price sheet we derive when a mid-task switch pays back, and a crossover: on long tool-heavy sessions the highest-priced model costs less than the next tier, as repricing about 10,000 real sessions from public datasets confirms. In an emulated enterprise of 10,000 seats with user behaviour taken from these datasets, the router recovers 14 to 21% of model spend at Anthropic's list prices of 21 September 2026, \$3.3M to \$5.0M a year. The paper also maps the risks across twenty harnesses, prices the dependence on one vendor's models, and proposes a control plane that enterprises can run from within, starting now, with a ladder for deciding later whether to own the harness.

---


### 49. [PFArena: Benchmarking Language Models for Protein Modification](https://arxiv.org/abs/2609.28921)

**<font color=#1a73e8>作者：</font>** Yawen Ouyang, Xinbo Zhang, Ziyuan Ma 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Protein modification requires navigating an immense sequence space, yet wet-lab validation remains low-throughput and costly. Although computational paradigms including protein language models (PLMs), large language models (LLMs), and LLM-based agents have shown promise in protein modification, their relative efficacy across realistic experimental decision-making settings remains unclear. To bridge this gap, we introduce PFArena, a benchmark comprising four controlled task interfaces that cover single-mutant generation and multi-mutant ranking. By providing varying levels of mutation fitness data, PFArena reflects four representative research scenarios characterized by differing degrees of prior experimental context. We assess six PLMs, six LLMs, and five LLM-based agents using complementary metrics to measure both peak and overall protein modification performance. Our evaluation reveals that model performance shifts systematically with the availability of target-specific experimental evidence: PLMs demonstrate proficiency in open-ended single-mutant generation by leveraging protein-specific priors, whereas LLMs and agents perform strongly in multi-mutant ranking, particularly when target-specific fitness data are available. Nevertheless, all model families face fundamental challenges with increasing search-space size and mutation depth. We release our code and benchmark suite to facilitate reproducible research in model-assisted protein modification.

---


### 50. [Calibrated Decision Models for Autonomous Penetration-Testing Harnesses: JEV and Laya as System One Decision Layers for LLM-Driven Pentest Agents](https://arxiv.org/abs/2609.28940)

**<font color=#1a73e8>作者：</font>** Joas Antonio dos Santos Barbosa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous penetration-testing harnesses use large language models (LLMs) for reconnaissance, exploitation, and reporting, but often rely on those same models to confirm findings, grade severity, and select agents. This can lead to false positives, inflated severity, and wasted compute. We examine how System One decision models, lightweight non-generative classifiers that return typed, calibrated verdicts, can support these decisions. We make five contributions. First, we define four decision points: finding adjudication, severity recalibration, agent pruning, and confirmation loops. Second, we present an exploratory NeuroSploit case study comparing one run with TypeSafe System One (Jev) and one without it against a web target containing 13 vulnerabilities. Differences in severity distribution, runtime, and grading by exposed data type motivate the architecture but do not establish statistical significance. Third, we review published specifications for Jev, Jev-Ultrafast, and the open-source Laya without assuming that results from other benchmarks transfer to penetration testing. Fourth, we discuss RLHF, RLAIF, RLCD, and RLHV as training approaches and their implications for trust in security decisions. Finally, we propose Rave, a domain-adapted System One model, and outline its training data, evaluation protocol, and potential effect on harness assurance.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-228](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
