# 🧠 大模型相关研究 | 2026年10月07日

> 本类共 **505** 篇论文：已确认 **467** 篇，待复核 **38** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

---

### 51. [LongSocialBench: Do Long-Context LLMs Understand Online Discussion Threads?](https://arxiv.org/abs/2610.04118)

**<font color=#1a73e8>作者：</font>** Xinyi Liu, Rinat Khaziev, Dilek Hakkani-Tür 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context LLMs can now ingest entire online discussion threads, but understanding their social discourse requires more than reading a long document: models must track parent-reply relations, turning points, scoped subtrees, cross-branch contrasts, and participant trajectories. To test this structure-aware social reasoning, we introduce LongSocialBench, a benchmark of 1,462 verified human-authored multiple-choice items drawn from 94 complete Hacker News, Stack Exchange, and Reddit r/ChangeMyView episodes, with a median length of approximately 73K tokens. Each item pairs a complete serialized discussion and reply structure with a four-option question, requiring models to recover structured social evidence. Released items are verified for answerability, option uniqueness, and evidence grounding. Across 18 models and 29 evaluation settings, current long-context workflows remain far below human performance. The best individual result comes from Claude-Opus-4.7, which reaches 63.0% when prompted to eliminate incorrect options before answering, compared with 72.4% for independent human readers. Averaged across all 18 models, the full-context Baseline scores 43.9%. Supplying the gold evidence scope raises this to 55.0%, showing that substantial errors remain even after the relevant thread region is identified. LongSocialBench shows that the missing capability is not context access or prompting alone, but social understanding over structured reply trees.

---


### 52. [Copying Before Suppression: What Drives a Below-Chance Dip During Language Model Training?](https://arxiv.org/abs/2610.04119)

**<font color=#1a73e8>作者：</font>** Tejas Dahiya, Cole Blondin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability usually studies fully trained models, yet the computations that drive a behaviour can change while the model is still learning the task. On the Indirect Object Identification task, a model should continue with the name mentioned once rather than the name mentioned twice. Pythia models pass through an early training window in which they prefer the repeated name, so accuracy in a choice between the two names falls below one half while language-model loss on a fixed text sample keeps decreasing across the same window. The window reflects a temporary imbalance between two computations. We identify one cause of the wrong preference by selecting a set of attention heads that write the repeated name, on prompts separate from those used for causal evaluation, keeping that selection fixed, and then replacing each head's final-token output with its average output on a separate set of non-repeated-name prompts. This improves the correct-minus-repeated logit difference in a separately trained 160M model and in the official 160M, 410M, and 1B models. At 160M, the head that lowers the repeated name in the mature model shows little of its mature behaviour at this point. It directs less than one percent of its attention to the repeated mention, and its output makes almost no direct contribution to lowering that name's logit. Both properties grow over the interval in which behaviour recovers. Across the 160M, 410M, and 1B models, transplanting the corresponding head's mature parameters into the early checkpoint recovers 35 to 68 percent of the total improvement in the correct-minus-repeated logit difference seen by the end of training. Related early-to-late reversals appear at further Pythia scales, in two independently trained GPT-2 models, and in OLMo. A mature circuit can therefore conceal a transient causal configuration that shaped behaviour earlier in training.

---


### 53. [Representational Control over Self-Report & Behavior Coherence in LLM Risk-Taking](https://arxiv.org/abs/2610.04125)

**<font color=#1a73e8>作者：</font>** Rafal Kocielnik, Peiyang Song, Pengrui Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-report is an appealing low-cost probe of an LLM's dispositions, but recent work finds only selective agreement between what models report and how they behave. Prior accounts establish these patterns by prompting black-box LLMs, leaving open whether the gap is a prompting artefact or a fact about how the underlying constructs are represented internally. We investigate risk-taking, a consequential dimension of agentic decision-making, using activation steering to measure self-report and behavior under the same internal intervention. We survey nine steering-vector extraction methods spanning task-specific directives, the model's own task behavior, and dispositional descriptions at two granularities, evaluated on two behavioral tasks and two psychometric instruments across four open-weight LLMs. We find that (1) a shared internal intervention does not ensure shared responsiveness: directions built from trait descriptions move self-report but leave behavior at chance, directions built from the model's own task choices do the reverse, and only task-specific directives reach both, weakly. (2) Diagnosis dissolves that exception: removing surface confounders leaves the directives only 32% of their behavioral effect. The two channels are otherwise steered by near-orthogonal directions, each channel reachable by several independent constructions. (3) An intervention composing one behavior-moving and one self-report-moving direction moves both together; flipping one sign sets them in opposition, with reported and enacted risk pointing in opposite directions on 69-89% of flipped compositions in all models. These findings move the self-report-behavior relationship from a black-box observation to a representational one that can be inspected and controlled, motivating representational checks alongside behavioral evaluation.

---


### 54. [What Gradients Add to Text Leakage in Split Language Models, Counted per Token and per Document](https://arxiv.org/abs/2610.04128)

**<font color=#1a73e8>作者：</font>** Georgios Politis, Evangelos Pappas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Split learning lets a client train a language model on a server without sending its text. The client runs the first layers itself and sends the server only their output, a vector of numbers for each token. During training, the server sends gradients back. We show that an observer at the split can rebuild most of the client's text from this traffic, and we measure how much the gradients help. On GPT-2, an attacker who holds only the publicly released weights of the client's layers recovers 94.20% of tokens from the activations alone and 97.38% when it also sees the gradients, 3.17 percentage points more 95% interval [2.72, 3.64]. Counted by document, the difference is much larger. The attacker rebuilds 13.71% of 32-token documents exactly without the gradients and 37.77% with them, because a document only counts when every token is right. How we count also changes how good a defence looks. Secret mixup, which blends each outgoing vector with a decoy, stops the attacker from rebuilding almost any document exactly, yet the attacker still recovers 83-91% of tokens. In a second experiment on GPT-2 and Qwen3-0.6B, where the server trains only a run of consecutive layers, the layer at which the run starts changes both model quality and leakage, even when the run's length is fixed. We recommend reporting leakage both per token and per document, and treating what a split model sends as being as sensitive as the text itself.

---


### 55. [PB-GRPO: Learning Socially Adaptive LLM Agents from Persona-Driven Simulation with Preference-Batched GRPO](https://arxiv.org/abs/2610.04132)

**<font color=#1a73e8>作者：</font>** Jingquan Wang, Jun Yin, Xu Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building LLMs that behave well socially, not merely correctly, requires Building LLMs that behave well socially, not merely correctly, requires more than producing locally helpful responses. A socially competent agent must infer users' unstated goals, respect their preferences, and adapt as the conversation unfolds. These behaviors are inherently multi-turn and social, making them hard to optimize: real interaction data is scarce, and user preferences are typically latent rather than directly observable. To address these challenges, we build on a persona-driven social simulation environment (consisting of a persona library, LLM-based user simulators, and a user-satisfaction scoring system ranging from [0, 1]), to introduce preference-batched GRPO (PB-GRPO), a post-training algorithm that learns socially adaptive policies from conversation-level feedback. Compared to vanilla GRPO, PB-GRPO computes advantages using a normalization estimated across a bucket of users with similar preferences, stabilizing training across a diverse social population. Empirical evidence shows that PB-GRPO improves models' social behavior over strong reinforcement learning baselines in our simulated environment.

---


### 56. [Auditing Pairwise Equivalence Judgments: Self-Critique Effects and Diversity Measurement in Multi-Agent Hypothesis Generation](https://arxiv.org/abs/2610.04133)

**<font color=#1a73e8>作者：</font>** Ji Young Byun, Anthony Hu, Jesse Rogers 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems built on large language models (LLMs) are increasingly applied to scientific discovery and hypothesis generation. Both the effect of refinement and the diversity of the delivered set are hard to interpret before experimental ground truth exists, and both are typically reported by deciding whether pairs of generated hypotheses describe the same underlying mechanism. We study two evaluation questions that rest on this pairwise equivalence judgment: (1) how much self-critique changes delivered hypotheses beyond run-to-run variability, and (2) how the equivalence rule used to group hypotheses affects measured diversity. Across four proprietary instances, we hold opening hypotheses fixed, rerun the downstream workflow with 0, 1, and 5 critique rounds, and score matched hypothesis pairs with an LLM-as-a-judge. Relative to matched same-depth reruns, moving from 0 to 1 round produces 34.5 percentage points (pp) of additional mechanism-level divergence, whereas 1 to 5 rounds adds 1.3 pp. We then compare three equivalence rules: term frequency--inverse document frequency (TF--IDF) similarity, dense embeddings, and the same LLM-as-a-judge. We construct controlled hypothesis pairs that either preserve the causal explanation through wording or biological-terminology changes, or replace one component of the causal chain while holding the rest fixed. All three rules are invariant to meaning-preserving edits, but when the initiating event is replaced, the LLM-as-a-judge identifies 83% of valid pairs as different mechanisms, versus 0% for TF--IDF and 8% for embeddings; varying only the rubric that defines same mechanism moves this figure from 38% to 96%. Together, these results show that pairwise equivalence judgments are a measurement choice: how mechanism equivalence is defined affects both the estimated effect of self-critique and the measured diversity of generated hypotheses.

---


### 57. [Dynamic Harness Search: Building Multi-Agent Systems Per-Query via Prediction](https://arxiv.org/abs/2610.04137)

**<font color=#1a73e8>作者：</font>** Som Sagar, Shasha Li, Hejie Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agent harnesses specify the roles, instructions, tools, and communication structure used to solve a task, and the right harness depends on the query. Because the value of each design choice is observable only through execution, tailoring a harness to each query has required either executing alternatives at inference time or costly manual design. We introduce SHIFT, which moves execution out of the per-query search loop. A local LLM architect learns a policy over harness-building actions from search, and a value function that predicts, from measured executions, a utility balancing accuracy against execution cost. For each query, Monte Carlo tree search uses these predictions to construct a harness. Across 9,193 tasks in six benchmarks, from math to document and general-assistant tasks, with a Gemini 3.5 Flash executor, SHIFT attains the highest mean accuracy, about 80%, outperforming 17 baselines that span prompting, prompt optimization, and workflow search, and exceeding the strongest baseline by 7.2 percentage points. A cheaper mode of SHIFT also attains a higher mean accuracy than every baseline while using 32% fewer execution tokens than the strongest baseline. We further show that choosing structure, instructions, and tools jointly beats choosing only instructions or only tools by up to 9.1 percentage points, and that learned value selection identifies more accurate harnesses with lower execution cost from candidate pools.

---


### 58. [From Sight to Foresight: Predictive Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.04139)

**<font color=#1a73e8>作者：</font>** Feiran Wang, Xiaoqi Wang, Ziwei Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting future spatial states supports collision avoidance and timely decision-making in dynamic environments. However, existing vision-language models (VLMs) and benchmarks for spatial reasoning primarily focus on observed scenes, leaving predictive spatial reasoning beyond the observed interval underexplored. To this end, we introduce SpatialMind, a metric-scale VLM for spatial reasoning and future prediction. Its metric depth adapter anchors spatial reasoning to real-world scale, while its progressive state chain establishes current spatial states and observed dynamics as the foundation for future prediction. Given a video prefix, SpatialMind predicts distances, motion directions, and spatial relations in both observed and unseen future frames. For training and evaluation, we build a scalable data engine that grounds entity descriptions in metric geometry to generate question-answer pairs and state supervision. Using this engine, we construct the SpatialMind-30K dataset and the SpatialMind-2K benchmark, both covering driving and everyday egocentric scenes. The benchmark spans eight tasks across three levels: current-state understanding, observed-dynamics understanding, and future prediction. Experiments show that SpatialMind substantially outperforms both general and spatially specialized models on our benchmark while achieving competitive zero-shot performance on VSI-Bench, OSI-Bench, and VLM4D.

---


### 59. [ExpertMuon-Compass: Alignment-Guided Step Sizes for Mixture-of-Experts Training](https://arxiv.org/abs/2610.04140)

**<font color=#1a73e8>作者：</font>** Omatharv Bharat Vaidya, Ashwin Vinod, Pedram Akbarian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) language models send each token to a few experts, so each expert is trained on a different part of the data, and this part changes during training. With a shared learning rate, Muon applies updates of roughly the same size to expert matrices of the same shape, even when an expert's update is poorly aligned with its current gradient. We here propose ExpertMuon-Compass (Compass), which multiplies the Muon step of each expert by two factors. A family factor compares the cosine between the expert's orthogonalized update and its gradient with the same cosine for the other experts in its layer. A scalar radius aggregates the alignment between corresponding rows of the update and gradient into one step-length multiplier. Compass keeps the update direction and the momentum buffer of Muon. In pretraining on FineWeb-Edu, Compass with Nesterov momentum on all matrices performs as well as or better than Muon, NorMuon, and other optimizers, with weight decay matched to NorMuon in the longer runs. Adding its factors to NorMuon gives the same or a lower loss than NorMuon. Compass is the most effective when the data seen by each expert varies during training, for example, as when the languages of a multilingual corpus arrive in separate blocks. With Compass, the expert load stays balanced, and the router assigns tokens to experts more decisively. We also prove a perturbation bound for the two factors.

---


### 60. [Kepler4D: Controllable Future Video Generation via 4D Scene State Evolution](https://arxiv.org/abs/2610.04152)

**<font color=#1a73e8>作者：</font>** Feiran Wang, Bin Duan, Junyi Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models aim to preserve scene structure and predict how dynamic objects evolve beyond visual observations. We present Kepler4D, a framework for future video generation through explicit 4D scene state evolution. Given a monocular video, Kepler4D constructs a shared 3D representation of background geometry, object motion histories, coarse spatial supports, and semantic context. Chain-of-Motion summarizes observed motion and uses a vision-language model to select structured speed and heading decisions and decide whether to bound object-center height from below. A deterministic rollout converts these decisions into future object trajectories for inspection and editing before synthesis. We render the evolving proxies into geometric controls for a pretrained video generator, separating coarse object motion from the synthesis of appearance and articulation. Experiments on real-world videos demonstrate that Kepler4D enables controllable object motion and plausible future rollout while preserving scene consistency.

---


### 61. [Trajectory-Derived Confidence for Reliable, Resource-Aware Clinical Text-to-SQL Agents](https://arxiv.org/abs/2610.04156)

**<font color=#1a73e8>作者：</font>** Mincheol Daniel Song, Joshua Ward, Jake Jung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents for clinical text-to-SQL applications reason autonomously over multiple steps but cannot assess whether their own reasoning or outputs can be trusted. In high leverage applications such as healthcare, this presents a critical risk where system mistakes can be costly. These reliability failures are also resource failures: an incorrect reasoning trajectory spends computation budget on outputs that must be discarded. We introduce Sentinel, a trajectory-derived, classifier-based confidence layer that analyzes an agent's reasoning, code and database outputs to decide at three points whether to stop: refusing unanswerable questions before the agent runs, halting doomed trajectories mid-run, and withholding untrustworthy answers at delivery. Here, utilizing Chow's rule, we optimize decisions under the EHRSQL shared task's Reliability Score, which penalizes incorrect answers given a utility weighting, and find on the benchmark EHRSQL that Sentinel raises this score from +0.08 to +0.24 when mistakes have a low utility weighting, well above the +0.03 earned by refusing every question, with delivered-answer accuracy rising from 54% to 69% as coverage falls from 84% to 55%. At higher stakes the agents we test rarely answer reliably enough to deliver, and Sentinel detects this on its own, abstaining to that same +0.03 where the unmonitored agent scores -3.02. The same stopping decisions cut computation: at low stakes, where the system still answers, Sentinel eliminates 13-28% of agent steps at little or no reliability cost.

---


### 62. [How RL Reshapes LLM Reasoning: Transferability, Coverage, and Scaling Laws](https://arxiv.org/abs/2610.04158)

**<font color=#1a73e8>作者：</font>** Ziheng Cheng, Yixiao Huang, Hanlin Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent studies on reinforcement learning (RL) report seemingly conflicting evidence about large language model (LLM) reasoning. Training on mathematics can improve performance in other domains, yet gains in Pass@1 can coincide with lower Pass@$N$ than the base model. This raises a fundamental question: does RL expand an LLM's reasoning boundary, or merely reweight its existing reasoning space? We revisit these phenomena across Qwen and Gemma model families, showing both cross-domain gains and forgetting, while coverage at large sampling budgets increases on some tasks and decreases on others. Detailed analysis of solution traces before and after RL indicates a shift in the reasoning strategies the model employs, motivating a two-stage autoregressive policy model that separates \emph{strategy selection} from problem-specific execution. Within this framework, we prove how RL's implicit bias reshapes strategy preferences, allowing gains on some tasks while suppressing strategies required by others. This mechanism can also broaden or narrow coverage at a given sampling budget even without expanding strategy support. We further provide theoretical justifications for log-sigmoid and log-linear scaling laws in RL compute, and evaluate their predictive power. Together, these results connect changes in strategy selection to cross-domain transfer, reasoning coverage, and compute scaling.

---


### 63. [Principled Top-$k$ Selection for Language Models with Hybrid Gradients](https://arxiv.org/abs/2610.04162)

**<font color=#1a73e8>作者：</font>** Xuchen Gong, Junfei Sun, Tian Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selecting the best $k$ items out of $m$ candidates is a critical component of modern large language model systems, such as document selection in Retrieval-Augmented Generation (RAG) and expert routing in Mixture-of-Experts (MoEs). However, training these selection modules remains challenging due to weak gradient signals and suboptimal exploration-exploitation tradeoffs. Furthermore, prior works often rely on heuristics, lacking principled objectives and approaches that explicitly model and solve the top-$k$ selection problem. In this work, we propose a principled objective for training selection modules, whose gradient naturally provides richer training signals in a hybrid form---containing a supervised-gradient component and a policy-gradient component. We show that the selection problem becomes harder as $m$ increases, and our algorithm converges at rate $O(1/\sqrt{T})$, with the optimal upper bound achieved by balancing between bias and variance. Practically, we apply our method to a set of tasks involving top-$k$ selection, including synthetic regression problems, RAG, and MoE systems, showing that our method outperforms the baselines in next-token prediction perplexity and QA accuracy.

---


### 64. [Agentic Cognitive Depth: Operational Criteria for Evaluating LLM Agents](https://arxiv.org/abs/2610.04168)

**<font color=#1a73e8>作者：</font>** Nijesh Upreti, Chris Sypherd, Vaishak Belle  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic large language model (LLM) systems are commonly implemented as an LLM in a loop with Planning, Memory, Tools, and Control Flow. This application-focused view connects agentic LLM research with deployable systems and leaves open how such systems should be evaluated beyond end-to-end task success. Building on this view, we define agentic cognitive depth as a trajectory-level profile across five operational criteria. The profile contains context sensitivity ($C$), temporal continuity ($T$), multimodal coordination ($M$), adaptive interaction ($A$), and metacognitive monitoring ($Mc$). The first four criteria measure how well Control Flow, Memory, Tools, and Planning are used across a trajectory. The fifth measures whether the system monitors and regulates the full run. For each criterion, we give operational proxies and a perturbation procedure, then connect the profile to the agent's world model. We provide the structure needed to extend benchmarks such as GAIA, SWE-bench, WebArena, and TRIP-Bench with per-criterion diagnostics. Symbolic verifiers, structured memory, planner coupling, and tool constraints provide practical ways to build and test these capacities.

---


### 65. [Language Model Fingerprinting Requires Rethinking Watermark Teachers](https://arxiv.org/abs/2610.04169)

**<font color=#1a73e8>作者：</font>** Jeongyeon Hwang, Anshul Nasery, Sewoong Oh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM fingerprinting via watermark distillation embeds a statistical watermark signal into model weights, enabling model owners to identify their models behind black-box APIs. Revisiting a recent protocol, we find that its utility evaluation understates text quality degradation in open-ended generation, favoring overly strong watermark teachers. Weakening the watermark improves text quality but sacrifices detectability. To move beyond this trade-off, we rethink whether text watermarks designed for verifying generated text are suitable distillation teachers for model fingerprinting. Such watermarks are typically designed to remain detectable from an individual output, limiting how sparse the watermark signal can be. In contrast, fingerprint verification can aggregate signal across queries, making sparser watermark signals viable. This raises a key question: where should the sparse signal be placed? We analyze signal placement through token surprisal and show that, even at comparable watermark strength, different placements can target tokens with different plausibility under the base model. This motivates near-tie restriction, which uses top-1-relative logit gaps to restrict the watermark bias to tokens close to the base model's top prediction. Across multiple models, near-tie improves detection--quality frontiers under deployment changes, preserves higher text quality across query budgets, and further improves existing watermarking schemes when combined with them.

---


### 66. [DimSteer: Steering LLM Authoring with Automatically Discovered Stylistic Controls](https://arxiv.org/abs/2610.04174)

**<font color=#1a73e8>作者：</font>** Ajit Mallavarapu, Ziwei Gu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language model writing interfaces often make users steer outputs by repeatedly articulating desired changes in natural language. Yet writers may recognize useful stylistic directions only after seeing alternatives, making revision recall-heavy. We present DimSteer, an authoring interface that samples prompt-local completions, discovers high-variance activation-space axes of variation, labels them, and exposes them as sliders with pole previews, diff comparison, and reset controls. Users can manipulate discovered dimensions, reducing the need to reformulate prompts for each stylistic adjustment. In a within-subjects study with 16 participants against a matched prompt-only baseline, DimSteer reduced mental demand, effort, and frustration while preserving comparable perceived success. Participants valued the surfaced dimensions, yet 15 of 16 disagreed that they would have thought to request the same changes in a prompt. Results suggest prompt-local controls can shift LLM authoring from recall-based prompting toward recognition-based exploration and direct manipulation, while preserving prompting for open-ended edits.

---


### 67. [SHarP: Saliency-based Pruning of Agent Harnesses](https://arxiv.org/abs/2610.04178)

**<font color=#1a73e8>作者：</font>** Xinyi Gao, Qiucheng Wu, Kaizhi Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses are systems that coordinate model calls, tool use, and task execution to help large language models complete complex tasks. To meet task requirements and address failures, these systems are often iteratively refined by amending and patching their instructions, tools, and workflows, continuously increasing harness complexity. It is therefore unclear whether some resulting harness modules are redundant, introducing substantial token overhead with little, if any, performance gain. Inspired by neural network pruning, in this paper, we study harness pruning as a means of striking a better balance between task performance and token cost. We propose SHarP (Saliency-based Harness Pruning), a simple yet effective pruning strategy based on the saliency of each harness module with respect to performance and efficiency. Specifically, we first identify tools, instructions, and supporting mechanisms as components that can be individually disabled. We then estimate the saliency of each module by ablating it and assessing its task performance and token cost relative to the full set of single-module ablations. Modules with the smallest contribution to performance or largest computational overhead are subsequently pruned. Our evaluation across various harnesses on held-out validation sets reveals a surprising finding: most harnesses that we studied are highly redundant and can maintain comparable performance and efficiency even after a substantial portion of their modules are pruned. Our pruning approach and empirical findings provide new perspectives on agent harness design and optimization.

---


### 68. [Language Model Activations Inhabit Privileged Error-Correcting Basins](https://arxiv.org/abs/2610.04183)

**<font color=#1a73e8>作者：</font>** Matthew Finlayson, Francisco Pernice, Eric Todd 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models exhibit remarkable robustness, continuing to produce coherent text even when their activations are perturbed by interventions like linear steering. We hypothesize that this robustness is a result of passive dynamics, i.e., constraining mechanisms in the forward pass that funnel activations toward "good" regions that produce coherent outputs. To investigate these hypothesized error-correcting mechanisms, we probe the geometry of language model activation space by observing the action of model layers on low-dimensional curves. In doing so, we discover that model activations occur within a cluster of distinct attracting basins, which differentiate natural activations geometrically from distributionally similar synthetic activations. Applying this lens to language model steering, we observe feature-specific basins along semantic steering directions, and find that steering moves activations between these basins. To demonstrate the active role of this geometry in neural computation, we show that adaptively modulating steering strength to transport activations across basins improves inter-language steering, significantly increasing the probability of sampling tokens from the target language compared to fixed-strength steering. Our findings establish analysis of activation space geometry as a promising approach to interpreting and controlling language models.

---


### 69. [Agentic AI with Structured CoT for Enhancing AI's Spatial Intelligence: Visualization and Reasoning of Rotation](https://arxiv.org/abs/2610.04188)

**<font color=#1a73e8>作者：</font>** Uttamasha Monjoree, Wei Yan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent studies show that artificial intelligence (AI) with language and vision capabilities still experiences limitations in spatial reasoning. In this paper, we have studied the spatial capabilities of advanced generative AI to understand the rotations of objects in 3D space, utilizing AI's image processing and language processing features. We trained and examined the spatial intelligence of a generative Agentic AI model (GPT-5.6) to understand the spatial rotation process with rotation diagrams based on the revised Purdue Spatial Visualization Test: Visualization of Rotations (Revised PSVT:R). We improvised the Revised PSVT:R by superimposing additional graphical and contextual features to evaluate how different Chain-of-Thought (CoT) reasoning strategies influence model performance. The results indicate that structured CoT reasoning improves the spatial reasoning performance of the base GPT-5.6 model in both datasets (PSVT:R and PSVT:R with coordinate system). We used three CoT approaches - (1) Structured CoT, (2) few-shot Structured CoT, and Structured CoT with Self-optimized Prompt. The three CoT approaches evaluated in this study showed no significant performance difference. Results showed that combining structured CoT reasoning with relevant contextual information leads to considerable improvements in VLM performance on 3D rotation tasks, demonstrating the potential of agentic AI for more effective spatial reasoning. However, when contextual information is removed, structured CoT reasoning alone provides limited improvement, and the models continue to exhibit notable difficulties in understanding spatial transformations. These findings suggest that effective spatial reasoning in VLMs relies on the integration of visual, textual, and reasoning-based information in future agentic AI systems for spatial intelligence.

---


### 70. [MemLeak: Cross-User Semantic Leakage in Multi-Tenant AI Agent Memory](https://arxiv.org/abs/2610.04195)

**<font color=#1a73e8>作者：</font>** Priyanka Mudgal, Kai Zhao, Guilin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal AI agents in enterprise multi-tenant deployments share a common vector store for long-term memory. Shared embedding spaces create a surface for cross-user memory leakage: a user's query can retrieve semantically adjacent memories belonging to another user through ordinary cosine-similarity retrieval, without any exploit. We formalize this as cross-user admissibility failure and evaluate it across six experiments, plus follow-up ablations, under both sparse (TF-IDF) and production-faithful (MiniLM-L6-v2) retrieval. Non-adversarial, incidental leakage reaches 70--100\% under pooled {same-team} retrieval; adversarially crafted memories achieve 90--100\% top-$k$ placement, exceeding weaker keyword-based attacker baselines, with score lifts of $+0.416$ to $+0.511$ under production-faithful dense retrieval (Config B); and end-to-end response contamination reaches 5.00/5 under a production retrieval path and 4.67/5 with Claude Sonnet~4.5, with contaminated responses often scoring as helpful or more helpful than clean ones, a gap validated against human judgment. Among three architectural mitigations, only hard post-retrieval ownership gating consistently restores the clean baseline (1.00/5) across {two generation models, at a measured latency overhead of roughly 1.4~ms per query.

---


### 71. [Asynchronous Is Nearly Free for Evolution Strategies on Long-Horizon Agentic Tasks](https://arxiv.org/abs/2610.04196)

**<font color=#1a73e8>作者：</font>** William Hoy, Jingxuan Fan, Nurcin Celik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based long-horizon agentic post-training is often bottlenecked by rollout generation: trajectories span many interaction turns, completion times vary substantially, and synchronous update barriers leave faster workers waiting for stragglers. Asynchronous reinforcement learning which has been adopted in LLM post-training addresses this inefficiency by consuming trajectories as they arrive, but introduces policy lag and off-policy optimization. Evolution strategies (ES) offer a backpropagation-free alternative for LLM post-training, yet it relies on a larger number of rollouts and existing practices have remained largely synchronous. In this short-form paper, we introduce bounded-staleness asynchronous ES and demonstrate it on Endless Terminals benchmark using Qwen2.5-7B-Instruct. Across three evaluation seeds, natural Async-1 matches synchronous ES, achieving 25.9\% versus 25.4\% held-out success. Controlled schedules that delay 10\% of each update cohort by four or eight policy updates reduce success by only 1.6 and 3.1 percentage points, respectively, without explicit off-policy correction. GRPO performs better overall, reaching 29.0\% held-out success, but importantly our results show that ES tolerates moderate policy staleness with limited degradation, opening possibilities for future improvement of ES-based post-training with asynchronous algorithms. To the best of our knowledge, we are the first to demonstrate the effectiveness of sync and async ES on a multi-turn terminal style agentic coding task.

---


### 72. [ALoDLM: Adaptively Looped Diffusion Language Models](https://arxiv.org/abs/2610.04198)

**<font color=#1a73e8>作者：</font>** Liancheng Fang, Zhuowei Li, Youngeun Kim 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) enable fast generation by predicting multiple tokens in parallel, but their practical adoption remains limited by a persistent quality gap relative to comparably sized autoregressive (AR) models. We attribute this gap to a computation-difficulty mismatch: within a partially observed sequence, some unknown tokens are easy to predict, while others require substantially more computation. Existing DLMs nevertheless apply uniform computational depth to all unknown positions at each denoising step. We introduce ALoDLM, which replaces uniform computation with token-adaptive latent recurrence. At each denoising step, ALoDLM iteratively refines latent representations and allocates computation according to token difficulty. Tokens ready to commit are fed back as discrete context, while unresolved tokens retain and further refine their latent states through additional recurrent passes. To learn token prediction and computation allocation jointly, we formulate token-wise computation schedules as latent variables and derive a conditional negative evidence lower bound (NELBO). We train ALoDLM at 1.7B and 8B parameter scales. Across eleven benchmarks, ALoDLM outperforms all evaluated DLMs and the corresponding AR baselines in average benchmark score at both scales. ALoDLM also retains fast parallel decoding, yielding a strong quality-efficiency trade-off among evaluated autoregressive and diffusion models under optimized inference engines.

---


### 73. [Clean: Second-order LLM Training at Linear Memory Cost via Nyström Sketching](https://arxiv.org/abs/2610.04204)

**<font color=#1a73e8>作者：</font>** Beheshteh T. Rakhshan, Sahar Rajabi, Maziar Sargordi Shikai Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large language models (LLMs) entails a fundamental trade-off: memory-efficient optimizers such as Adam discard cross-parameter curvature, whereas full-curvature methods such as SOAP can accelerate convergence at prohibitive memory costs. We introduce Clean, a memory-efficient and full-curvature optimizer designed to resolve this bottleneck. Clean leverages the randomized Nystrom method to accurately approximate the left and right preconditioners in SOAP, and to reduce the optimizer's memory complexity from quadratic to linear in terms of model dimensions. We subsequently reintegrate the off-subspace components to capture curvature information beyond the low-rank approximation, preserving rich curvature at minimal memory cost. We further propose Q-Clean, a low-precision variant that aggressively compresses optimizer states. Q-Clean reduces optimizer memory consumption by \textbf{over 50\%} compared to Muon when pre-training a LLaMA-1.3B architecture, all while maintaining strong and competitive predictive performance. Notably, Clean operates with a smaller optimizer-state footprint than standard AdamW while reaching AdamW's final performance \textbf{26\% faster} in wall-clock time. Furthermore, our methods uniquely enable the pre-training of a 13B-parameter model on a single 80GB GPU, providing a scalable, efficient, and accessible approach to large-scale model optimization.

---


### 74. [Fine-Tuning VLM for Enhancing AI's Spatial Intelligence: Understanding 3D and 2D Rotations](https://arxiv.org/abs/2610.04206)

**<font color=#1a73e8>作者：</font>** Uttamasha Monjoree, Wei Yan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence is a fundamental skill in multiple domains, such as Science, Technology, Engineering, and Mathematics (STEM), Medicine, Architecture, and Construction. Recent studies indicate that Vision-Language Models (VLMs) still face limitations in spatial reasoning, which inhibits artificial intelligence (AI) from performing practical spatial tasks. Using multiple object-rotation datasets developed for training and evaluation, our experiments demonstrated promising improvements in both 2D and 3D rotation detection. Fine-tuned Google DeepMind-built Gemma-4 mixture-of-experts (MoE) models significantly outperformed fine-tuned Gemma-4 generalist models in predicting rotations defined by both their axes and angles. Fine-tuning also substantially improved angle estimation for 2D representation without requiring an explicit coordinate system. Furthermore, identifiable objects did not improve angle-detection accuracy; instead, objects with prominent linear features showed improved performance.

---


### 75. [Can LLMs Separate Pasted Artifacts from User Speech? Absorption at Unmarked Prompt Seams](https://arxiv.org/abs/2610.04210)

**<font color=#1a73e8>作者：</font>** Sugam Panthi, Muhaiminul Yeamin, Rabab Abdelfattah  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) receive each user message as plain text, even when it combines text from different sources. For example, a user may paste text into a prompt and keep typing a comment directly below it. We study absorption: a phenomenon where the model treats a trailing user comment as part of the pasted text, returning it inside the edited text. This happens even though the user did not intend the comment to become part of that text. Existing instruction-data separation benchmarks tell the model which text is instruction and which is data, then test whether it obeys that separation. They do not test harmless user speech following an unmarked paste. We introduce SEAM, a controlled benchmark of 300 editing examples. Each example is tested under six matched conditions that vary how the boundary between pasted text and later user speech is expressed. Across 20 models, absorption at a bare newline ranges from 7.7% to 66.7%. Adding a blank line does not significantly reduce absorption in any model, while boundary markers reduce it in 19 of 20 models. Comments that fit the pasted text, such as a code comment typed after code, are absorbed significantly more often in 17 of 20 models. Models often fail to separate pasted material from later user speech, and explicit boundaries reduce but do not remove this failure.

---


### 76. [TCMClinicalReason-Bench: Can Language Models Reason from Pathogenesis to Prescription over Real-World Clinical Cases?](https://arxiv.org/abs/2610.04215)

**<font color=#1a73e8>作者：</font>** Jirui Dai, Chenkai Zhang, Yan Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate clinical narratives that are insufficiently grounded in patient-specific evidence. In traditional Chinese medicine (TCM), errors can propagate from etiology and pathogenesis through syndrome diagnosis and treatment principles to prescription generation. We developed TCMClinicalReason-Bench using 2,000 multicenter electronic health record cases to distinguish case-grounded responses from fluent but unsupported diagnostic and therapeutic conclusions. Five general-purpose and two TCM-specific LLMs were evaluated in zero-shot settings. An evidence-constrained rubric assessed seven diagnostic and therapeutic components and three cross-block relations, allowing case-supported alternatives. Qwen3.7-Plus with TCM retrieval served as the automated judge, alongside parallel blinded ratings by five senior TCM clinicians on a 600-case subset. Structural completeness was nearly saturated (99.3-100.0%), but normalized content scores ranged from 40.7% to 54.1%. The five general-purpose models averaged 50.0%, versus 41.3% for the two smaller TCM-specific models. Cross-block logic consistency ranged from 60.8% to 66.8% and correlated moderately with content across cases (Pearson's r = 0.515-0.656). Deficits were greatest in prescription generation, prescription analysis, and symptom-guided modification. In judge stress testing on 100 independent cases, perturbation detection rates across the three relations were 57%, 56%, and 31%, with contradictions detected more reliably than omissions. Separating component quality from cross-block consistency localizes failures missed by endpoint and completeness metrics and identifies where clinician oversight remains necessary.

---


### 77. [FlashGaze: Training-Free Multi-Scale Patch Pruning For Efficient Video Understanding](https://arxiv.org/abs/2610.04225)

**<font color=#1a73e8>作者：</font>** Ziye Zhu, Yanghao Zhou, Lixing Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated strong performance in video understanding, yet efficiently processing long, high-resolution videos remains challenging. Such videos often contain substantial spatiotemporal redundancy, and processing redundant visual tokens can incur avoidable computational overhead. Many existing methods prune visual tokens during or after vision transformer (ViT) encoding, leaving much of the encoding cost unaddressed. Some approaches prune patches before encoding but rely on learned auxiliary networks for patch selection, incurring additional training and inference overhead. To address these limitations, we propose FlashGaze, a training-free method that reduces spatiotemporal redundancy before ViT encoding without introducing auxiliary networks. FlashGaze uses pixel-space differences as a proxy for information loss and employs Quadtree Dynamic Programming to jointly optimize patch dropping, merging, and keeping under a fixed budget. Experiments on two MLLM backbones across multiple benchmarks demonstrate substantial efficiency gains while largely preserving accuracy. On Qwen3-VL-8B, FlashGaze retains 98% of the full-input baseline accuracy on LongVideoBench while achieving up to 5.4x and 17x speedups in ViT encoding and MLLM prefill, respectively, and reducing peak GPU memory usage by a factor of 1.8. These efficiency gains enable the model to process videos with more frames and higher resolutions on the same GPU hardware, unlocking video understanding at scales previously out of reach.

---


### 78. [Conformal Prediction with Paraphrase-Aware Scoring for LLM Uncertainty Quantification](https://arxiv.org/abs/2610.04239)

**<font color=#1a73e8>作者：</font>** Jiayi Xin, Evan Qiang, Zihan Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification (UQ) for large language models (LLMs) aims to provide reliable measures of predictive confidence, yet current methods are often unstable under meaning-preserving perturbations. Semantically equivalent paraphrases can induce substantial variability in predictive confidence, even for methods with formal guarantees, such as conformal prediction. To address this issue, we propose a paraphrase-aware UQ framework robust to semantic rewordings. Our approach trains a lightweight proxy model on LLM hidden states and aggregates its predictions across paraphrases to construct label-wise nonconformity scores. Under score exchangeability, conformal calibration retains marginal coverage. This guarantee can also hold under test-only rewording, provided that the paraphrase pipeline satisfies an additional distributional alignment condition. We evaluate three settings (normal, fully reworded, and semi-reworded) which apply rewording to neither dataset, both calibration and test datasets, or only the test dataset, respectively. Across seven multiple-choice QA benchmarks and multiple model families, our method produces compact prediction sets with empirical coverage generally near the nominal target, even in the semi-reworded setting. Ablation studies show that the learned proxy accounts for most of the reduction in set size, while paraphrase-augmented training and inference-time aggregation improve stability under rewording. Code is available at this https URL.

---


### 79. [Autonomous Active Directory Exploitation via Multi-Model Harness Orchestration: A Benchmark Study with NeuroSploit on GOAD](https://arxiv.org/abs/2610.04243)

**<font color=#1a73e8>作者：</font>** Joas Antonio dos Santos Barbosa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Active Directory (AD) remains the predominant identity and access management infrastructure in enterprise environments, and its compromise represents the highest-impact outcome in internal penetration tests. Recent work has shown that large language models (LLMs) can autonomously conduct assumed-breach penetration testing against AD, but these studies employ standalone agents lacking structured guardrails, deterministic validation, and multi-stage chain orchestration. We present a benchmark evaluation of NeuroSploit v4.2.0, an open-source Rust-based autonomous pentest harness, against the Game of Active Directory (GOAD), a deliberately vulnerable multi-forest AD lab maintained by Orange Cyberdefense comprising five virtual machines, two forests, and three domains. The harness orchestrates 22 AD-specific agents and 7 multi-stage attack-chain playbooks covering the full AD kill chain: enumeration, Kerberoasting, AS-REP roasting, NTLM relay and coercion, Kerberos delegation abuse, AD CS exploitation (ESC1-ESC8), MSSQL linked-server pivoting, DCSync, cross-forest trust abuse, and persistence detection. We benchmark nine frontier LLMs (Claude Opus 4.6/4.7/4.8, GPT-6 Astra, GPT-5.6 Sol, Grok 4.6, Qwen 3.8, GLM 5.3, Kimi k3) within the harness, comparing against direct invocation across 14 technique categories and 7 chains. The harness achieves 96-100% technique coverage with 90-97% precision, while direct invocation covers only 21-54% and produces 3.2x more false positives. Time to full three-domain compromise with Opus 4.8 was 134 minutes with guardrail activations preventing lockout-triggering sprays, unauthorized DCSync dumps, and out-of-scope reconnaissance. Results demonstrate that structured harness orchestration with domain-specialized agents, POMDP belief tracking, and cross-model voting substantially outperforms unstructured LLM usage for AD penetration testing.

---


### 80. [On the Steering Dimensionality of Refusal in Language Models](https://arxiv.org/abs/2610.04245)

**<font color=#1a73e8>作者：</font>** Han Wang, Erik Miehling, Dennis Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing activation steering methods often assume that a high-level concept can be mediated by a single steering direction. To support this, two complementary interventions should be achieved: additive steering should induce the target behavior, while directional ablation should suppress it. Yet behaviors may occupy richer activation geometries beyond a single direction, and semantically similar behaviors may be represented by distinct directions. In this work, we study how many directions can reliably control two different types of refusal behaviors: refusal triggered by the safety alignment and refusal in general contexts. Given the limited expressive capability of a single steering vector, we study the general setting of steering subspaces and introduce the notion of steering dimensionality as the minimum subspace dimensionality required to reliably control a behavior. We characterize sufficient steering subspaces that cover the full extent of the target behavior through both the (monotonic) improvement before the sufficient dimensionality, and the saturation beyond it. Empirically, we find that refusal triggered by safety alignment is 1-dim steerable, while multiple distinct steering directions can achieve comparable control. In contrast, refusal in general contexts exhibits substantially richer activation geometry where even 5-dim steering subspaces fail to reliably capture its full steerable variation. Our results reveal that the activation geometry underlying refusal is highly context-dependent and can be substantially more complex than a single linear steering direction.

---


### 81. [Benchmarking Psychological Dynamics in Generative Agents](https://arxiv.org/abs/2610.04246)

**<font color=#1a73e8>作者：</font>** Sumer S. Vaid, Ashley V. Whillans  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed to simulate human behavior, acting as computational replicas of human subjects. Yet the lived psychological experience of humans is difficult to benchmark, particularly as it unfolds over time. We introduce a psychometric benchmark for computational replicas: personas that carry a fixed identity through an evolving sequence of events. Built entirely from published norms and meta-analytic effects, the benchmark scores two dimensions of psychological realism. The first, internal validity, quantifies whether generated trajectories reproduce the internal structure of repeated human measurement: distributions, the between- versus within-person variance partition, temporal dependence, and range. The second, external validity, quantifies whether replicas recover established trait, state, and indicator relations. Across 36 open-weight and proprietary LLMs from nine developers (1B-671B parameters), most recover the direction of established relations (84.3% mean agreement) and the variance partition (26 of 34), yet the within-person correlation and distributional structure elude recovery. Internal validity is independent of scale and capability: a mid-size open LLM (Gemma-3-27B) strikes the best trade-off between the two dimensions. The benchmark is a precondition for using computational replicas in causal inference across domains (e.g., marketing, healthcare), and identifies within-person grounding as the central challenge ahead.

---


### 82. [Spec2Game: Can LLMs Generate Complete Playable Games from Detailed Specifications?](https://arxiv.org/abs/2610.04253)

**<font color=#1a73e8>作者：</font>** Yixue Cai, Yuzhe Zhao, Hanxiang Chao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating an executable program does not necessarily mean that it correctly implements the behavioral requirements specified in natural language. To evaluate large language models' ability to realize detailed specifications as complete interactive programs, we introduce Spec2Game, a benchmark that requires models to generate complete Pygame projects from detailed natural-language game specifications. Spec2Game comprises 15 game families and 150 task instances, with one canonical task and nine controlled rule variants per family, spanning three levels of implementation complexity. Using source-code, runtime, and visual evidence, we evaluate generated projects along four dimensions---Executability, Specification Realization, Code Quality, and User-Facing Quality. Across 14 LLMs and 3,330 generated projects, we find that high executability does not imply faithful specification realization. Component-level analysis further shows that models perform substantially better on Game Element Modeling than on Rule and Mechanism Modeling or Goal and Termination Modeling, indicating that faithfully implementing game rules and termination logic remains a major challenge.

---


### 83. [Cross-Trait Transfer in Subliminal Learning](https://arxiv.org/abs/2610.04260)

**<font color=#1a73e8>作者：</font>** Xingyu Zhao, Yiqiao Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subliminal learning is a phenomenon where a student language model acquires a teacher model's behavioral traits by training on semantically unrelated outputs. It is a subtle statistical phenomenon as trait transmission relies on weak statistical patterns in the generated data. To understand trait transmission between teacher-student pairs, we study cross-trait transfer: how data generated under one teacher trait changes the student's preferences of other traits. To this end, we introduce a directed trait-transfer matrix that quantifies these effects using log-probability gains for student answers. We find that the trait-transfer matrix reveals clusters of related traits, with students sometimes developing preferences for traits similar, but not identical, to the teacher's trait. Such cross-trait structure can be partially captured by output distribution metrics and representation-based metrics. Further, we analyze trait development and interaction: learning dynamics shows a progression from broad shared shifts toward more trait-specific transfer, and multi-trait experiments suggest that opposed traits can enhance such differentiation. Together, our findings reveal salient statistical structures over trait transfer and competition, thus providing a broader view of how hidden preferences are transmitted in subliminal learning.

---


### 84. [Playing social deduction games with reinforcement fine-tuned large language models](https://arxiv.org/abs/2610.04261)

**<font color=#1a73e8>作者：</font>** Lingzhe Zhang, Yunpeng Zhai, Tong Jia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement fine-tuning (RFT) is increasingly used in applications where large language models (LLMs) interact with humans and other agents. Here we use social deduction games to study how RFT changes LLMs' social behaviour. We let fine-tuned and base LLM agents play hidden-role games that require hidden-state inference, social reading and vote steering. Our results show that LLM agents do not reliably acquire social-deduction ability by directly optimizing terminal win--loss outcomes, suggesting that final game results provide a sparse and noisy signal for socially interactive learning. However, RFT is particularly effective at improving social reading, including tasks that require agents to infer hidden roles from public discussion, update beliefs over time and predict other agents' future decisions. We further show that RFT can also improve social influence, including tasks that require agents to steer votes, team approvals and collective decisions, although these gains depend more strongly on behaviourally specific rewards and structured interaction settings. Finally, we show that LLMs' ability to play social deduction games can be further improved through multi-agent social-cognitive reinforcement fine-tuning, which combines social-reading and social-influence signals during same-side multi-agent training. These learned behaviours also receive more favourable human evaluations of strategic competence, persuasiveness and social usefulness. Together, these results enrich our understanding of how RFT changes LLMs' social behaviour and provide a step toward a behavioural learning theory for machine social intelligence.

---


### 85. [Rethinking Self-Distillation for Multi-Teacher Capability Merging](https://arxiv.org/abs/2610.04272)

**<font color=#1a73e8>作者：</font>** Roy Xie, Dan Friedman, Feng Nan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Combining capabilities of multiple expert models trained starting from the same base checkpoint has become increasingly common in frontier language-model post-training. Recent trends suggest that multi-teacher on-policy distillation (MOPD) outperforms conventional off-policy methods. However, despite the higher inference and environment interaction costs incurred by MOPD, we find that much of its reported accuracy gain is due to certain training design choices and hyperparameter optimization, rather than the algorithm itself. We conduct a controlled self-distillation study across two multi-teacher settings, four models, and eleven benchmarks, comparing off-policy methods, namely supervised fine-tuning (SFT) and soft-label distillation, to hybrid teacher-prefix distillation and MOPD. We found that all four methods achieve \textit{nearly identical} accuracy. However, MOPD uses $14.8$--$23.1\times$ SFT's training GPU-hours. We also revisit four recently published comparisons between on-policy and off-policy distillation and find that the reported on-policy gains shrink substantially when SFT baselines are trained on rejection-sampled teacher trajectories and use independently tuned hyperparameters. As a training-free alternative, we also find that simple weight-merging methods can recover expert capabilities with minutes of CPU merging time, although their accuracy degrades as model size decreases and task interference increases. Overall, our results question recent gains reported due to MOPD and suggest careful tuning of more efficient off-policy baselines as a viable alternative.

---


### 86. [Dense Neuro-Symbolic Reasoning in a Unified Geometry State](https://arxiv.org/abs/2610.04280)

**<font color=#1a73e8>作者：</font>** Ruoran Xu, Wending Gao, Haoyu Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geometry reasoning is naturally stateful: solving a problem repeatedly alternates between structural proposals and exact deductions. We formulate this process as dense neural-symbolic coupling, in which neural guidance and symbolic execution share a typed state and communicate through executable actions at every search step. Neural proposals contribute theorem instances, constructions, and algebraic bridges; the symbolic runtime applies registered rules, propagates exact constraints, and records provenance. A nested controller allocates computation first between neural and symbolic proposal sources and then among admitted actions. We instantiate the framework in OmniGeo, a single solver for plane, analytic, and solid geometry. With Claude Sonnet 4.6, OmniGeo reaches 94.2%, 88.5%, and 89.8% on FormalGeo7K, Conic10K, and SolidFGeo, respectively (90.8% macro average), and solves 21/30 IMO-AG-30 problems.

---


### 87. [CyTReX: Explainable AI-Based Cybersecurity Threat Reasoning Framework for DER Networks](https://arxiv.org/abs/2610.04286)

**<font color=#1a73e8>作者：</font>** Damilola Popoola, Souradeep Bhattacharya, Manimaran Govindarasu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Distributed Energy Resource (DER) environments rely on network communication protocols to coordinate control commands, measurements, and device states across edge assets and cloud systems. Edge anomaly detection systems (ADS) monitor this traffic to identify deviations from normal communication behavior, flagging suspicious flows for further investigation. When the ADS flags abnormal network traffic, a single attack label is often insufficient for operational response: the label reports the detector's selected class but does not expose alternative threat interpretations that may warrant investigation. This paper presents Cybersecurity Threat Reasoning with Explainable Artificial Intelligence (CyTReX), an evidence-grounded threat reasoning framework for DER security that transforms network-level anomaly alerts into ranked, analyst-facing threat hypotheses designed to support Security Operations Center (SOC) triage and investigation. CyTReX constrains large language model (LLM) reasoning through a structured evidence packet, defined as a consolidated record of detection outputs, model explanations, and cyber threat intelligence (CTI) context. The evidence packet integrates edge-layer anomaly detection evidence, cloud reasoning layer attack interpretation, Shapley Additive Explanations (SHAP) network-feature attributions, surrogate decision rules, and Model Context Protocol (MCP)-enabled CTI enrichment. This ensures that every ranked hypothesis and attack-tree branch is traceable to explicit evidence rather than free-form LLM inference, and that incomplete or conflicting evidence is communicated rather than suppressed. Evaluation across five configurations shows that additional reasoning components improve hypothesis specificity, evidence traceability, and analytical grounding, with the complete pipeline providing the richest evidence-grounded reasoning context.

---


### 88. [LMBuild: Evaluating LLM Agents for Generating Buildable and Functional Structures](https://arxiv.org/abs/2610.04292)

**<font color=#1a73e8>作者：</font>** Jiateng Liu, Rushi Wang, Cheng Qian 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly capable of generating complex 3D structures, with the potential to reshape how objects are designed and realized in the physical world. Yet, producing elegant geometry is fundamentally different from producing objects that can be built and perform their intended functions. Existing evaluations largely focus on geometric quality while overlooking physical realizability. We introduce LMBuild, a benchmark for evaluating LLM agents on generating buildable and functional structures. LMBuild represents generated objects as assembled structures comprising part decompositions, joints, materials, and sequences. To support reproducible evaluation, we provide a unified framework consisting of: (1) an interactive environment in which agents can use tools to retrieve, create, and place components to construct objects; (2) a curated benchmark that repurposes established CAD datasets and augments them with knowledge from Wikipedia; and (3) a evaluation framework covering structural soundness, functional affordance, design quality, and physical realization. Evaluations across 30 systems reveal several intriguing findings: (a) Soundness and alignment are no longer the primary bottlenecks for frontier closed-source models, while functional affordance and physical operability remain substantially more challenging; (b) stronger models more effectively create new components, whereas weaker models tend to rely on retrieval; and (c) providing functional specifications substantially improves part completeness, kinematics, and physical operability. These results show that generating real-world structures requires deeper reasoning about functional affordances, mechanics, and designing and creating novel components. We expect LMBuild to provide a foundation for measuring progress and incentivizing research toward agents that generate buildable and functional structures.

---


### 89. [Language-Conditioned Token and Reasoning Efficiency in Large Language Models: A Paired Cross-Lingual Study Protocol](https://arxiv.org/abs/2610.04295)

**<font color=#1a73e8>作者：</font>** Genliang Zhu, Chu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models incur language-dependent representation and inference costs, but existing comparisons often conflate input language, assigned observable-trace language, and answer realization. We specify a prospective paired study that separates these interfaces while holding the semantic item, checkpoint, and answer oracle fixed. The initial design instantiates 240 exactly scored items rendered from templates in English and seven non-English languages, three distinct-lineage open-weight checkpoints, three trace-token budgets, 22 input- and trace-language conditions, a fixed answer reserve, and a separately counted delimiter: 47,520 initial core runs before prospective sample-size selection. RQ1-RQ3 estimate input and trace effects by intention-to-treat with failure-inclusive terminal accounting and test answer realization by cloning a sealed prefix and runtime-native KV state into eight crossed branches. Pre-freeze independent language review, fixed-form ASCII selectors, and code/surface/solver agreement constrain the realization test. H1-H5 share one Holm family and a global simultaneous component band. A secondary randomized experiment compares one-long-attempt and complete K-short-attempt policies at equal trace allowance under frozen seeds and oracle-blind aggregation; it is a full-policy contrast because answer capacity differs. Outcomes include exact token spans, correctness, latency, runtime-exposed memory, and qualified same-host operating-system-reported energy over prespecified hardware rails. The protocol separates tokenizer expansion, observable-trace cost, and answer-realization cost without treating visible traces as internal cognition or operating-system estimates as physical cross-device energy. No confirmatory model outcome is reported; result fields remain disabled until the frozen evidence ledger passes independent verification.

---


### 90. [Questioning the Questions: Sustaining Self-Evolution in Reasoning Models](https://arxiv.org/abs/2610.04299)

**<font color=#1a73e8>作者：</font>** Jinyuan Li, Chengsong Huang, Langlin Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving reasoning models learn from their own generated questions, yet repeated self-training can lead to performance collapse. In this paper, we investigate why performance deteriorates over successive rounds and how to sustain self-evolution. Our analysis identifies two recurring quality problems in self-generated questions: invalid questions and repeated variants of the same mathematical questions. First, invalid questions become more prevalent across rounds, and answer-consistency filtering further increases their proportion in training data. Second, existing question diversity controls based on lexical similarity can miss mathematically equivalent questions expressed in different ways, which leads to question diversity collapse in later training rounds. Building on these findings, we introduce R-Quest, which uses question validity and novelty feedback to guide self-evolution. We first train the solver to recognize and reject invalid questions, then use its judgments to guide questioner rewards and filter solver training data. To avoid question repetition, we use a frozen base model to compare sampled question pairs and provide novelty feedback. Empirically, our method consistently achieves the highest average performance on 12 benchmarks in mathematical reasoning, general-domain reasoning, and code generation across two model families. Additionally, R-Quest maintains stable performance gains over ten rounds of self-evolution, peaking in the final round and outperforming R-Zero by 17.32 points.

---


### 91. [EnvDreamer: Large-Scale Multimodal-to-Environment Generation for Embodied AI](https://arxiv.org/abs/2610.04301)

**<font color=#1a73e8>作者：</font>** Kabir Swain, Sijie Han, Antonio Torralba  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large datasets and high capacity models have accelerated progress in vision and language. This work introduces a platform aimed at bringing comparable gains to embodied learning, world models, and robotics. We present EnvDreamer, a framework that uses large language and vision language models to generate Unreal Engine 5 environments for embodied AI and robot training. EnvDreamer enables sampling of large, diverse, interactive, customizable, and validator passed virtual environments for training and evaluation across navigation, interaction, and manipulation. We illustrate the platform with a large set of generated scenes and simple baselines. Policies trained on EnvDreamer generated environments, without explicit mapping or human task supervision, achieve competitive results on multiple embodied benchmarks spanning navigation, rearrangement, and manipulation. EnvDreamer also supports image-conditioned reconstruction for real-to-sim studies. Finally, we release EnvDreamer-20k, a dataset of 20,000 validator passed environments with task programs, scene graphs, trajectories, and metadata to support reproducible benchmarking.

---


### 92. [Evaluating Modeling Approaches for Experience-Level Classification in Job Description](https://arxiv.org/abs/2610.04304)

**<font color=#1a73e8>作者：</font>** Celia Liang, Eddie Wu, Shiqi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates the task of predicting job experience levels in recruitment texts, aiming to automatically identify the qualifications required for positions. Unlike traditional text classification, recruitment texts typically possess explicit internal structures, with different paragraphs playing disproportionate roles in conveying experience clues. To address this, we propose a structure-aware Section-Aware BERT approach that segments and encodes key paragraphs (titles, responsibilities, requirements) for integrated modeling, building upon rule-based systems and classical baselines TF-IDF. Simultaneously, we evaluate large language models under both few-shot and fine-tuning settings on the same dataset to compare the capability boundaries of different modeling paradigms. Experimental results demonstrate that explicitly leveraging text structure significantly improves experience level prediction performance, particularly in scenarios with ambiguous job titles. Further error analysis reveals systemic challenges in this task, including confusion between Entry and Senior levels and the blurred boundaries of Mid-level positions. This research provides an effective modeling approach and analytical framework for understanding structured recruitment texts.

---


### 93. [Rethinking Long-Video Efficiency: A Joint Allocation Perspective on Frames, Pixels, and Front-End Latency](https://arxiv.org/abs/2610.04318)

**<font color=#1a73e8>作者：</font>** Sixun Dong, Wei Li, Andong Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient long-video understanding with vision-language models (VLMs) is often framed as selecting informative frames or visual tokens at a fixed native resolution. We show that per-frame resolution can instead be traded for denser temporal coverage, while front-end decoding latency depends on the size of the candidate pool rather than the final token budget. An empirical study across multiple VLMs and long-video benchmarks yields three findings: dense low-resolution sampling outperforms sparse native-resolution sampling at matched token budgets; resolution-sensitive tasks benefit from selected high-resolution frames; and front-end decoding dominates wall time for hour-long videos. Motivated by these findings, we introduce LoHi, a training-free, single-pass framework that combines a dense low-resolution video stream with sparse high-resolution image frames through the VLM's native video and image pathways. LoHi-Anchor selects high-resolution frames using codec I-frame metadata, while LoHi-SemDiv uses query relevance and visual diversity over CLIP features. Across three long-video benchmarks, LoHi improves average accuracy by 10.6 percentage points over the native-resolution baseline at a matched token budget and by 5.2 percentage points over the strongest prior efficiency method. It also reduces front-end decoding latency by up to 7x on hour-long videos. Project page: this https URL

---


### 94. [Bidirectional Preference Synthesis: Learning Prompt-Conditioned Preferences from Boundary Failures](https://arxiv.org/abs/2610.04328)

**<font color=#1a73e8>作者：</font>** Junbo Wang, Lidong Lu, Zhuoqun Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Correction-based offline preference pipelines commonly treat model failures only as rejected responses under the original prompt. This supervision is incomplete for boundary failures: responses that violate the given instruction yet coherently satisfy a nearby intent or constraint setting. We introduce Bidirectional Preference Synthesis (BPS), a data-construction method for standard Direct Preference Optimization (DPO) that makes this missing prompt dependence explicit. For each validated boundary failure, BPS keeps the conventional forward pair under the original prompt and adds a reverse pair under a synthesized achieved prompt, so the same response is rejected where it is wrong and chosen where it is right, without changing the DPO objective, training a reward model, or requiring online sampling. On Qwen3-4B-Instruct-2507, BPS preserves original-side pairwise ranking while raising achieved-side ranking accuracy from 6.8% to 62.3% on held-out crossed anchors, with a similar shift under a Kimi-K2.6 cross-teacher probe. A blind human audit supports the intended reverse preference direction, and downstream evaluations show the clearest separation from Forward-DPO in multilingual multi-turn instruction following, with consistent capability-retention patterns on agentic, tool-use, and code checks.

---


### 95. [Suppressing Pressure, Amplifying Evidence: Self-Guided Attention Steering to Mitigate Sycophancy and Stubbornness](https://arxiv.org/abs/2610.04329)

**<font color=#1a73e8>作者：</font>** Yinghao He, Mengyu Xu, Haixiang Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable language models should resist unsupported user pressure while effectively using objective contextual information. However, models may exhibit sycophancy by yielding to unsupported user pressure or contextual stubbornness by failing to update their answers when relevant contextual information warrants revision. Evaluating interventions for these failures separately can obscure whether mitigating one failure exacerbates the other. To assess this trade-off, we introduce CoPE-Bench with six conditions per question: a neutral baseline, correct or incorrect user pressure, contextual information consistent with or conflicting with the neutral answer, and a joint condition combining incorrect claims with conflicting contextual information. To regulate the influence of user pressure and contextual information, we propose SPAE (Suppressing Pressure, Amplifying Evidence), a training-free framework that uses the model's own judgments to identify relevant tokens, suppressing user pressure and amplifying contextual information through token-level attention steering. On average across five backbones, SPAE reduces pressure following by 18.8 percentage points and increases joint-condition updating by 5.5 percentage points relative to the strongest baseline in the main comparison. In two-turn dialogue, it improves joint-condition updating by an average of 13.2 percentage points over the strongest prompting baseline. The source data and codes can be found at this https URL.

---


### 96. [ShadowMiner v1 - An Experience Report on Implementing and Measuring a Problem-and-Hypothesis Discovery Engine](https://arxiv.org/abs/2610.04339)

**<font color=#1a73e8>作者：</font>** Jinhyuk Choi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ShadowMiner v1 is a system that automatically discovers research problems and generates hypotheses from AI papers. It is a nine-stage pipeline. It structures documents into a knowledge graph and finds graph gaps in it - structural blind spots in research. These graph gaps are included in the LLM generation prompt. Each generated hypothesis is then verified by checking whether it is already covered by existing research, scoring its quality, and checking that the facts it relies on are accurately drawn from its sources. This report does not propose a new generation or evaluation technique. It describes our experience of implementing and applying ideas from prior work, and measuring whether each one actually contributed.

---


### 97. [Hierarchical Credit Assignment for RLVR on Fused Gromov-Wasserstein Geometry](https://arxiv.org/abs/2610.04344)

**<font color=#1a73e8>作者：</font>** Qi Yu, Ruizhong Qiu, Zhichen Zeng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has been shown to improve the reasoning capability of large language models (LLMs) across diverse reasoning tasks. However, group-based RLVR methods, such as GRPO, assign a uniform advantage to all tokens within rollouts of the same outcome. While existing works refine credit assignment of GRPO based on local signals such as token locations or entropy, they often fail to capture the global semantic novelty of a reasoning behavior relative to the current policy. In this work, we propose a hierarchical credit assignment approach for group-based RLVR methods, called HarA, which identifies and encourages semantically novel reasoning behaviors during RLVR. HarA represents each sampled rollout as a distribution over the hidden states and locations of tokens, and computes the Fused Gromov-Wasserstein (FGW) barycenters of all rollouts with the same outcome, capturing the internal reasoning patterns in the latent space under the current policy. The semantic novelty of a reasoning element can then be measured by its contribution to the FGW distance between the current rollout and the barycenter. While solving the FGW formulation is expensive, we introduce an anchor-guided linearization that turns it into a Wasserstein formulation solvable via the Sinkhorn algorithm efficiently. By reweighing token-level advantage of group-based RLVR methods based on the novelty signals, HarA highlights novel reasoning behaviors at flexible granularities to encourage fine-grained LLM exploration. Extensive experiments across three group-based RLVR methods show that our plug-and-play method effectively enhances the exploration of LLMs, outperforming existing methods across diverse reasoning benchmarks.

---


### 98. [A Bird's-Eye View of Iterative Reward Design](https://arxiv.org/abs/2610.04364)

**<font color=#1a73e8>作者：</font>** Logan Mondal Bhamidipaty, Lauren Robson, Linda Petrini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing effective reward functions in RL typically requires substantial expertise and trial and error. Recent work automates this process with LLM-based systems that generate and iteratively improve reward code using policy feedback. However, these methods are often hard to compare because they differ in implementation details, feedback assumptions, and evaluation environments. To address this, we introduce a Benchmark for Iterative Reward Design (BIRD) that expresses existing methods in a unified configuration and evaluation space. This lets us compare algorithms directly, ablate individual design choices, and prototype new components under matched feedback conditions and policy-training budgets. Across MuJoCo, Meta-World, Assistax, and HumanoidBench, we identify a small set of simple design choices that consistently improve performance. Combining these choices yields significantly better performance than the evaluated methods from prior work. Our results highlight the strength of simple baselines and motivate further study of when additional algorithmic complexity improves iterative reward design. Code is available at this https URL.

---


### 99. [Boundaries Agree, Labels Do Not: Intra-Annotator Dynamics as a Kind of Training Data](https://arxiv.org/abs/2610.04370)

**<font color=#1a73e8>作者：</font>** Marharyta Shvets  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data quality now matters as much as compute for training language models. Much training data comes from human annotation of text, and interpretive annotation has no ground truth that could settle what is "accurate". Two lines of work respond to this. One combines annotators into a "ground truth" and measures how well they agree with each other; the other treats their disagreement as a signal. Both compare different people at one point in time. We measure something else: how well one reader reproduces their own reading of the same text over time. One expert human reader and three LLM families segmented three Sumerian myths and labelled the causal function of each segment with one of seven states. Across runs months apart, the human cut the text in much the same places but named the segments differently, in every myth. The models show no such consistent pattern: their gap between the two layers is positive in some myths and negative in others, and its size varies. The human's label changes are not random: the runs go through much the same functions but start them one step apart, while model runs start them at the same places. We argue that this pattern is a usable measure of data quality and a contamination check: a "human" annotation whose labels are as stable as its boundaries, and whose functions start in sync, looks like a model's.

---


### 100. [Functionally Equivalent or Not? Graph-Grounded Differential Surrogate Execution for Code Equivalence](https://arxiv.org/abs/2610.04371)

**<font color=#1a73e8>作者：</font>** Amit Kachroo, Like Hui, Haitao Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Determining whether two programs are functionally equivalent is central to code modernization, patch validation, refactoring, and code-generation evaluation. Yet the usual signals are incomplete: tests cover only finite inputs, textual similarity confuses implementation with behavior, and unconstrained LLM judgments are difficult to audit. Direct execution is often impossible when a program depends on an obsolete, licensed, unavailable, or unsafe environment. We introduce FEAgent, a selective equivalence assessor agent that combines typed program-graph evidence with differential surrogate execution. FEAgent first aligns public interfaces and behaviorally relevant graph anchors, then issues bounded queries over call-flow, control-flow, data-flow, type, import, and effect relations. Next, a branch-aware generator agent proposes discriminating inputs, and two blinded LLM surrogates independently predict source and target observables. Every claim and predicted divergence is recorded in an evidence ledger. A deterministic reconciler then returns EQUIVALENT, INEQUIVALENT, or UNCLEAR rather than forcing a verdict when paths are uncovered or evidence conflicts. We evaluate FEAgent on function-level equivalence and repository-level bug patches, where the existing oracle is a benchmark label or a passing test suite. Every disagreement with that oracle is adjudicated by direct execution, revealing errors in benchmark labels and behavioral divergences missed by unit-test-only scoring. On EquiBench, execution confirms FEAgent's disagreements with published labels on 216 of 1,200 evaluated pairs (18.0%); on SWE-bench Verified, 94 of 331 test-passing agent patches (28.4%) diverge from the reference patch. FEAgent thus serves as an audit layer between testing and formal verification, keeping its evidence reviewable and its uncertainty explicit without claiming a proof of equivalence.

---


> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
