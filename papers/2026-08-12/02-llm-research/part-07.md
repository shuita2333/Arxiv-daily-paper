# 🧠 大模型相关研究 | 2026年08月12日

> 本类共 **438** 篇论文：已确认 **404** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 301. [From Relevance to Execution Utility: Reward-Aware Dynamic Execution Gating for Skill-Based LLM Agents](https://arxiv.org/abs/2608.09168)

**<font color=#1a73e8>作者：</font>** Liang He, Jingbo Wen, Hongyu Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are increasingly used to equip large language model (LLM) agents with reusable procedural knowledge. Although recent work has substantially improved skill retrieval due to the increasing skill libraries, retrieving a plausible skill bundle does not guarantee that executing it is worthwhile. Since every skill-conditioned rollout is computationally expensive, deciding whether a retrieved bundle should be executed has become an increasingly important challenge. To this end, we introduce the Reward-Aware Dynamic Execution Gate (RADEG), a lightweight, retriever-agnostic decision layer between skill retrieval and agent execution. RADEG learns a low-cost surrogate model that predicts the execution utility of a query--bundle pair before the expensive rollout is launched. To obtain informative supervision while controlling for task difficulty, we locally perturb each retrieved bundle by deleting, adding, or replacing one skill, producing matched same-query rollouts that isolate the effect of bundle composition on verifier reward. During deployment, RADEG updates only a warm-started logistic head as new verifier feedback becomes available, enabling inexpensive adaptation of the execute/skip boundary without retraining either the retriever or the agent. Under a query-level held-out evaluation on 288 collected rollouts, RADEG substantially reduces unnecessary agent executions while preserving a large fraction of the downstream verifier reward. It consistently outperforms relevance-based and random gating across different execution budgets, demonstrating that execution-aware surrogate modeling provides a practical and cost-effective complement to skill retrieval.

---


### 302. [Not All Visual Tokens Are Equally Safe to Remove:Consequence-Sensitive Visual Token Compression](https://arxiv.org/abs/2608.09176)

**<font color=#1a73e8>作者：</font>** Jingbo Wen, Liang He, Mingyu Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token compression for vision--language models (VLMs) has largely relied on criteria such as attention, redundancy, and uncertainty to maximize average accuracy under a fixed compute budget, implicitly assuming that all errors carry equal cost. However, the consequence of an incorrect prediction on downstream tasks is rarely symmetric: misreading an invoice amount can be far more costly than misclassifying a background color. Motivated by this, we introduce consequence-sensitive visual token compression, which allocates visual computation across requests according to their potential error costs. Our method follows a calibrate-then-allocate procedure, estimating consequence-specific error-budget curves offline and applying the calibrated token budgets online using consequence signals available from question or task information. On a controlled within-task benchmark, high- and low-consequence questions are drawn from the same document images, so content alone cannot reveal which questions are costly to get wrong. In this setting, our method reduces high-stakes errors from 0.300 to 0.133 under the same total token budget, whereas a content-driven allocator performs no better than uniform allocation. Measuring how error rates change with token budget across different cost ratios, we derive an allocation frontier: uniform allocation is optimal when errors are equally costly, and token transfer toward high-consequence questions becomes increasingly beneficial as the cost gap grows. This allocation principle generalizes well across three dense vision-language benchmarks, two budget realization mechanisms (token deletion and resolution reallocation), two VLM architectures, and multiple token selection strategies. On a realistic mixed workload, consequence-sensitive allocation reduces cost-weighted error by 38% while achieving approximately 21% lower latency than full-resolution inference.

---


### 303. [Agentic Router: An Execution-Grounded Continual Learning Approach With Memory](https://arxiv.org/abs/2608.09184)

**<font color=#1a73e8>作者：</font>** Yuxuan Chen, Rongpeng Li, Zhifeng Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents provide a promising interface for command-line-based network operations, but a plausible command may still fail or introduce operational risk after execution. Existing approaches mainly focus on command generation or final configuration correctness, and do not use execution-grounded experience to jointly improve candidate coverage and action selection. We propose an execution-grounded dual-path consequence-aware agent for CLI-based SONiC operations, which generates multiple complete actions, predicts their execution consequences, and selects the final action through utility- and risk-aware reranking. The proposal-side path abstracts reusable operational lessons into retrievable guidance to improve feasible-action coverage without modifying the proposal LLM, while the selection-side path adapts the consequence predictor through session-level LoRA updates using real SSH feedback to improve conditional selection quality. Experiments over multi-turn SONiC operation sessions with different Qwen3 proposal models show that the framework improves feasible-action coverage and top-1 execution success, and that the two adaptation paths provide complementary gains over interaction.

---


### 304. [Failure-Aware Long-Form Translation: Design and Implementation of a Recoverable LLM Translation System](https://arxiv.org/abs/2608.09187)

**<font color=#1a73e8>作者：</font>** Yanlin Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A long-form translation request can succeed at the API layer and still produce an unusable result. The output may be empty, truncated, filtered, dominated by source or prompt material, or interrupted after producing text worth keeping. This report describes a recovery protocol developed for a deployed translation system with heterogeneous inputs and provider APIs. It delays the first visible release behind a 64-character window, validates the assembled output, and uses typed stream events to distinguish replacement from continuation. Interrupted work is retained only when a paragraph or sentence prefix can be re-derived from the source. Further attempts follow a stable model order and a shared deadline before entering a provenance-marked fallback path. A sanitized companion artifact implements the protocol and passes 38 public tests. Its fixed cases reproduce all 14 configured completion labels, contain four early-invalid prefixes before any of their 235 characters become visible, retain 31 boundary-safe characters across four interrupted streams, and satisfy the attempt, event, and provenance rules in two end-to-end scenarios. These results are executable checks of the published control flow. Translation quality and detector performance on naturally occurring outputs require a different evaluation.

---


### 305. [EmoS: A Theory-Grounded Framework for Evaluating and Aligning Emotional Intelligence in Spoken Language Models](https://arxiv.org/abs/2608.09189)

**<font color=#1a73e8>作者：</font>** Junyu Wang, Siyuan Zhang, Peiyuan Jiang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite significant advances in instruction-following and auditory comprehension, the evaluation of Emotional Intelligence (EI) in Spoken Language Models (SLMs) remains confined to rudimentary paralinguistic perception, lacking a systematic, theory-driven cognitive framework. We introduce EmoSBench, the first comprehensive EI evaluation benchmark for SLMs constructed upon the four-branch theoretical model, covering Perceiving, Understanding, Using, and Managing Emotion across ten sub-tasks. Preliminary assessments on EmoSBench reveal a substantial gap: even leading proprietary models like GPT-4o-Audio achieve only 52.6%, significantly trailing human baselines. To bridge this gap, we develop EmoS, a specialized evaluator model optimized via Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO). To facilitate its effective training, we curate EmoDialogue, a bilingual dataset providing necessary fine-grained supervision through response pairs with rigorously defined EI gradations. Concurrently, we introduce a reward mechanism integrating a Steep Exponential Accuracy Reward (SEAR) and a Rationale Fidelity Reward (RFR) to enforce precise ordinal scoring and valid reasoning. Experiments demonstrate that EmoS reaches 83.8% accuracy, approaching human-level performance. Furthermore, evaluations on authentic, unconstrained spoken interactions validate its robust real-world generalization, establishing a foundational framework for advancing emotionally intelligent dialogue systems.

---


### 306. [Signature-Guided Capacity Occupancy for Dense Expert Merging](https://arxiv.org/abs/2608.09201)

**<font color=#1a73e8>作者：</font>** Lingching Tung, Chi-Jui Kim, Beicheng Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dense expert merging combines domain-specialized language models into one single checkpoint, typically by admitting task-vector support in weight space. However, this admission is governed by three decisions that existing methods answer only partially: where to open layer capacity from cross-expert conflict, who should occupy that capacity based on domain demand, and how to admit the resulting support without relying on costly recipe search. To tackle these issues, we propose SigMerge (Signature-Guided Capacity Occupancy), a structured capacity assignment framework for dense expert merging. Starting from a dense base merge, conflict signatures set each layer's capacity from cross-expert conflict, positive base-merge deficits set each domain's share of that capacity, and a sequential occupancy rule admits each expert delta up to the resulting layer-domain budget. Across 21 paired settings spanning seven dense base merges and three model pools, SigMerge improves every one (by 15.0% on average) and achieves the best average rank (1.67) among six merging methods, outperforming three categories of merging baselines.

---


### 307. [CRUISE: Vision-Language Model-Guided Uncertainty-Aware Cross-Modal Sensor Fusion for Robust Autonomous Driving](https://arxiv.org/abs/2608.09202)

**<font color=#1a73e8>作者：</font>** Junyao Wang, Yulin Xu, Yu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern autonomous vehicles are equipped with multiple sensors, such as cameras, LiDAR, and radar, for comprehensive environmental perception. However, robust cross-modal feature fusion remains a critical challenge, as the reliability of each sensor varies significantly across diverse real-world driving conditions, including poor visibility and adverse weather. While uncertainty quantification (UQ) mitigates this issue by allowing models to prioritize reliable signals, existing uncertainty-aware fusion methods typically rely on simple feature-level uncertainty estimates and thus often fail to generalize effectively in complex, out-of-distribution scenarios. To address this limitation, we propose CRUISE, a novel uncertainty-aware cross-modal sensor fusion framework. CRUISE integrates a vision-language model (VLM)-guided UQ module that generates fine-grained, pixel-level uncertainty estimates. By leveraging the VLM's rich prior knowledge and superior contextual reasoning, our approach provides a highly informative guide for the fusion process. Furthermore, we introduce a dynamic adaptive mechanism that explicitly models and captures cross-modal dependencies, ensuring the framework fully exploits the inherent complementary nature of multi-sensor inputs.

---


### 308. [UNMASK: Discovering and Causally Verifying Spurious Shortcuts in Text Classifiers](https://arxiv.org/abs/2608.09209)

**<font color=#1a73e8>作者：</font>** Chidaksh Ravuru, Shashank Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural language models trained on large crowdsourced corpora frequently exploit spurious surface patterns tied to target labels without true linguistic or causal relevance, boosting benchmark performance while failing on adversarial or out-of-distribution inputs. Existing approaches either require manual specification of the feature vocabulary or automate discovery only partially, leaving the gap between dataset-level correlation and model-level exploitation unaddressed. We present U N M ASK, a fully automated pipeline that discovers, causally verifies, and mitigates spurious correlations in text classifiers without additional human annotation. Given unlabeled training examples, U N M ASK generates candidate surface patterns as executable boolean expressions, filters them through a statistical validation protocol with independent replication, and establishes causal model dependence via verified counterfactual interventions. Causally confirmed features then serve as annotation-free group definitions for Deep Feature Reweighting, eliminating the group labels that standard DFR requires. Applied to BERT and RoBERTa trained on MNLI, our pipeline independently rediscovers established lexical-overlap and negation biases, verifying 9 of 10 features on BERT and 6 on RoBERTa, and improving HANS accuracy by up to 12.58 pp. On CivilComments-WILDS, programmatic groups match the 70.1% worst- group accuracy of hand-labeled DFR (Kirichenko et al., 2023) without demographic annotation. We further demonstrate that the discovery and validation stages generalize to reward model preference data, surfacing interpretable spurious correlations in RewardBench2.

---


### 309. [Beyond Solvability: Task Learnability as a Static Prior for LLM RL Post-Training](https://arxiv.org/abs/2608.09217)

**<font color=#1a73e8>作者：</font>** Ting Zhou, Zhenqing Ling, Daoyuan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a central post-training paradigm for eliciting reasoning capabilities in large language models, yet uniform task sampling allocates compute without regard to differences in how tasks respond to optimization. Existing task-valuation methods mostly rely on snapshot-based signals such as current pass rate or reward, which estimate how solvable a task is under the current policy. However, tasks with similar current solvability can still differ substantially in how positively they respond to further training. We study this residual axis as task learnability: a regime-conditional measure of expected positive response to continued training under a fixed RL post-training regime. By analyzing per-task reward trajectories, we find that learnability is reproducible across independently sampled training contexts and predictive of downstream utility. To make this signal practical before training begins, we propose TrajVal, a lightweight probe-based estimator that approximates per-task learnability from a short probe run and two endpoint evaluations. TrajVal can be used either as a standalone static prior for task sampling or as a multiplicative prior for existing online schedulers. Experiments on mathematical and logical reasoning benchmarks across multiple model scales show that TrajVal improves data efficiency over uniform sampling and provides complementary gains when combined with online scheduling methods.

---


### 310. [Reading Cognition as Decisions Unfold in Words: A Factorized Inverse Decision Model](https://arxiv.org/abs/2608.09222)

**<font color=#1a73e8>作者：</font>** Jiawen Kang, Dongrui Han, Xixin Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Inverse decision modeling infers latent properties of decision processes from observed behavior, but existing formulations rely primarily on action trajectories. In verbalized cognitive tasks, task execution also produces response dynamics that action-only formulations leave unmodeled, such as verbal production, interaction, and hesitation. We propose a factorized inverse decision model (FIDM) that decomposes each individual's task-execution likelihood into an action factor and an effort factor, governed by separate individual-specific parameters. From raw verbal transcripts, a language model produces structured task-execution traces for factorized inference. On data from 400 older adults performing a grocery-shopping dialog task for cognitive screening, controlled recovery shows selective estimation of the intended factors, while matched semi-synthetic conditions show that FIDM preserves action-execution distinctions even when aggregate behavioral summaries are matched. Action evidence further localizes task-defined deviations across participants. In cognitive-status classification, FIDM provides information complementary to clinical scores, trajectory summaries, and frozen language representations, with consistent gains across all evaluated baselines in the binary setting.

---


### 311. [Governing the KV Cache: Preventing Timing Side-Channel Leakage in Multi-Tenant LLM Inference](https://arxiv.org/abs/2608.09225)

**<font color=#1a73e8>作者：</font>** Tejasvi C. Addagada  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache is the primary throughput optimization in modern large language model (LLM) inference, enabling prefix reuse across requests. In multi-tenant deployments this cache is shared across tenants, creating a timing side channel: an adversarial tenant can reconstruct another tenant's private prompt by probing cache-hit latency. Three published attacks exploit it -- PROMPTPEEK, EarlyBird and InputSnatch -- reaching up to 100% attack success rate against unprotected vLLM and SGLang, with rates varying by cache architecture and prompt structure.
We present KVGov, a governance layer addressing all three attack families' prefix-cache paths under one mechanism. A per-principal salt sigma_p = HMAC_K(secret, principal_id) seeds the block-hash chain, making cache keys cryptographically disjoint across principals. An ablation (N=1000 trials, seed 2026, deterministic judges) isolates this salt as the necessary and sufficient component. KVGov adds ORIGAMI, a Stackelberg water-filling audit scheduler that reduces adversary expected utility by 12.6% at realistic tenant heterogeneity (Gini 0.63), and an evolutionary stability analysis giving a 31.6% adversary-prevalence tipping point below which global caching remains stable.
On real hardware (Qwen2.5-7B-Instruct, vLLM 0.26.0, NVIDIA A100) we measure a gate-verified cold/cached TTFT ratio of 0.22, confirming the channel is exploitable at production scale; the defense itself is evaluated in simulation calibrated to those measurements. We replicate the channel on an independent stack (this http URL on Apple Metal, ratio 0.093). Finally, isolation and cache efficiency need not conflict: identifying information resides only where prompts diverge, so injecting the salt at that boundary rather than the chain root retains an estimated 93% of the prefix-cache benefit with no cross-principal signal.

---


### 312. [Omni2LoRA: Coherence-Preserving Parametric Memory for Efficient Omni Language Models](https://arxiv.org/abs/2608.09227)

**<font color=#1a73e8>作者：</font>** Puneet Mathur, Manan Suri, Dinesh Manocha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Omnimodal language models (OLMs) enable unified audio-visual understanding, but processing long joint token sequences makes inference computationally prohibitive. While recent token compression methods attempt to alleviate this burden, compressing modalities in isolation often destroys the temporal cross-modal anchors necessary for coherent reasoning. We introduce Omni2LoRA, a two-stage framework for efficient parametric memory compression via coherence-preserving context distillation that bypasses the token bottleneck entirely. First, a Perceiver hypernetwork processes intermediate representations from a frozen OLM to encode the multimodal context into a full-rank Low-Rank Adaptation (LoRA) adapter in a single forward pass. To prevent the resulting parameter footprint from scaling linearly with recording length, we optimize a discrete rank allocation policy via Group Relative Policy Optimization (GRPO) that uses a modality-ablated counterfactual reward to explicitly penalize the loss of audio-visual coherence, forcing the model to allocate its fixed sub-linear rank budget to synergistic cross-modal anchors rather than isolated visual features. Across three omnimodal backbones, Omni2LoRA operating at a 30% rank budget outperforms direct full-context inference and strong token-compression baselines (OmniZip, OMAC, O-MARC) on four audio-visual question answering benchmarks, improving average accuracy by 8-12% over the strongest baseline and remaining stable under compression ratios as tight as 75%, where token-pruning methods degrade sharply. By converting multimodal memory into a fixed-budget, reusable parameter state, our method drives answer-time multimodal-token load to zero, cutting per-query Time to First Token (TTFT) by up to 12x relative to full-context inference and amortizing to under 0.5s after a handful of queries.

---


### 313. [SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge](https://arxiv.org/abs/2608.09230)

**<font color=#1a73e8>作者：</font>** Yuanchi Zhu, Kang An, Tengyue Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial-safety understanding requires more than detecting workers, equipment, and personal protective equipment. Models must also assess compliance, identify hazardous interactions, explain potential accident mechanisms, and recommend preventive actions. Existing safety datasets primarily focus on visual perception or isolated violation recognition and provide limited supervision for evidence-grounded reasoning. We introduce SafeSceneReason, a multimodal industrial-safety reasoning benchmark and companion training corpus that connects workplace scenes with knowledge from occupational accident investigations. SafeSceneReason combines two complementary data-construction pipelines. The scene-centric pipeline converts annotated workplace images into executable safety scene graphs and generates deterministic answers through program execution over objects, relations, and safety rules. The report-centric pipeline extracts figures and contextual evidence from accident reports and constructs multimodal questions using evidence graphs, explicit information boundaries, multi-step reasoning paths, and iterative verification. The resulting resource contains 110,581 verified scene-centric question--answer pairs and 13,114 refined report-centric question--answer pairs, covering perception, spatial and quantitative reasoning, compliance assessment, evidence synthesis, causal analysis, and mitigation-oriented decision making. Evaluation of representative proprietary and open-source vision--language models reveals substantial performance differences and persistent weaknesses in comparative, technical, and multi-evidence reasoning, demonstrating that strong general visual understanding does not yet guarantee reliable industrial-safety reasoning.

---


### 314. [DreOPD: Degraded-Reference Extrapolative On-Policy Distillation for Flow-matching Models](https://arxiv.org/abs/2608.09233)

**<font color=#1a73e8>作者：</font>** Mingfeng Lin, Chengfei Cai, Lin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-matching models are now a mainstream method to image generation, but its adaptation to diverse downstream scenarios typically relies on post-training, which may cause conflicts among task-specific optimization objectives. Reinforcement learning enables direct optimization of task-specific rewards beyond the original models, yet trajectory-level optimization may incur high-variance gradients and cross-task interference. On-policy distillation (OPD) offers dense and stable supervision on student rollouts, but conventional teacher matching remains imitation-based. We propose DreOPD, a Degraded-reference extrapolative OPD method for flow-matching models that bridges these two paradigms. Our DreOPD converts implicit reward extrapolation into closed-form velocity regression, enabling extrapolative post-training with the stability of OPD. It further uses a mildly degraded reference to strengthen the teacher-reference contrast, yielding a clearer extrapolation direction. Experiments on single- and multi-teacher settings show that DreOPD outperforms OPD and multi-task RL baselines in average performance, while surpassing specialized teachers on most metrics.

---


### 315. [Emotion2Skill: Model-Internal Emotion Signals for Adaptive Skill Selection and Evolution](https://arxiv.org/abs/2608.09248)

**<font color=#1a73e8>作者：</font>** Bohan Lin, Hejia Geng, Xinyi Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill-based LLM agents select reusable procedures from an external library to solve complex tasks, yet their routing decisions rely entirely on text-level signals such as task descriptions, verbal reflections, and experience-derived rules, while the model's own internal representational state remains unobserved. Recent interpretability work has shown that LLMs maintain linear emotion representations that causally influence behavior; however, these representations have been exploited only for post-hoc analysis or direct output steering, and have not been used to inform agent-level decision-making. We propose Emotion2Skill, a framework that extracts LLM-internal emotion vectors and incorporates them into both skill selection and skill evolution. At each decision step, a 27-dimensional emotion state is extracted from the residual stream and mapped to a confidence-gated summary injected into the routing prompt. Beyond online selection, emotion trajectories are analyzed for abrupt internal-state shifts to pinpoint problematic skill invocations, guiding targeted SOP rewriting that replaces the coarse binary outcome signal of prior methods. On WebShop and ALFWorld, Emotion2Skill with Qwen3-8B improves over the Zero-Shot baseline by +26.9% success rate and +25.5% average success respectively, outperforming all baselines on both benchmarks with consistent gains on Qwen3-14B. Co-activation analysis further reveals semantically coherent emotion--skill pairings, confirming that the routing improvements reflect meaningful internal-state signals rather than opaque statistical correlations. These results establish LLM-internal emotion representations as an effective decision-level signal for orchestrating agent skill systems, extending their utility beyond interpretability and output steering. The code is available at this https URL.

---


### 316. [MoRSE: Task-Oriented Multi-Agent System with Mixture of Role-Subtask Experts](https://arxiv.org/abs/2608.09251)

**<font color=#1a73e8>作者：</font>** Peiwen Li, Shiyang Zhang, Yangtian Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model-based multi-agent systems have recently shown strong potential for complex, long-horizon tasks. However, existing methods mainly rely on coarse prompt-level differentiation without parameter adaptation for diverse subtasks, resulting in insufficient inter-agent heterogeneity and limited specialized capability that bottleneck performance on tasks with complex requirements. To address this, we introduce a Task-Oriented Multi-Agent System with Mixture of Role-Subtask Experts (MoRSE) that distinguishes agents with (role, subtask)-conditional specialization at both the task structure and parameter levels. To make agents' responsibility explicit at the task structure level, we formulate a task-oriented multi-agent system that decomposes each task into a dependency-aware Directed Acyclic Graph of subtasks and assigns each agent a specific (role, subtask), introducing task-level specialization across collaborating agents. Additionally, to address the diverse role and subtask parameter adaptation demands, we propose a dynamic Mixture of (role, subtask) LoRA Experts module with a prototype-based semantic router for subtasks, augmenting agents with parameter-level specialization on a shared LLM substrate cost-effectively. Then, to co-optimize experts and router stably under sparse task rewards, we further propose a hierarchical group-relative policy optimization with two-layer credit assignment that isolates expert updates from the cross-route variance introduced by routing decisions, disentangling expert quality from routing quality. Experiments on code-generation benchmarks across three backbones demonstrate the effectiveness of our approach, with improvements in both whole-task and step-wise performance, and the gains from trained specialization generalize across held-out task categories and domains.

---


### 317. [SkillSentry: Reliable Skill Execution for LLM Agents via Runtime Assurance](https://arxiv.org/abs/2608.09253)

**<font color=#1a73e8>作者：</font>** You Lu, Xinyu Huang, Bihuan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly equipped with skills to perform complex tasks through multi-step reasoning and tool use. Although skills provide reusable procedural knowledge, agents may still execute them unreliably. Even when an agent has demonstrated the capability to complete tasks under the guidance of a skill, it may fail to do so consistently across similar tasks or repeated runs due to deviations from the skill procedure or incorrect execution of individual steps. Such instability limits the practical reliability of LLM agents. To address this problem, we propose SkillSentry, a skill-oriented runtime assurance framework built upon a new domain-specific language (DSL) for representing runtime guidance for skill execution. SkillSentry initializes the runtime guidance by combining a skill specification extracted from the corresponding skill document with execution experience mined from historical successful and failed traces. It then wraps around the agent execution loop to monitor and guide skill execution under the current guidance, while iteratively refining the guidance using newly collected traces. We evaluate SkillSentry on 15 skills across two LLM agents, each paired with two backbone models, i.e., Claude Code with Claude-Haiku-4.5 and Claude-Opus-4.6, and Codex with GPT-5.2 and GPT-5.4. Our results show that SkillSentry improves the task success rate of LLM agents by 24.1% across skills, on average, while exhibiting lower variability across repeated runs.

---


### 318. [Business Truth, not SQL Accuracy: A Rule-Gated 7B Analytics Agent Outperforms a Direct-Prompted 32B Baseline](https://arxiv.org/abs/2608.09254)

**<font color=#1a73e8>作者：</font>** Morris Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM analytics agents are evaluated on SQL syntax accuracy, but production failures look different: questions with two valid business definitions, questions the warehouse cannot answer, deprecated columns after a schema change, and queries that execute successfully while returning the wrong business number. No execution-match metric can score them. This paper introduces WarehouseReliabilityBench, 400 frozen tasks over two synthetic warehouses in which roughly half the correct responses are a clarification, an abstention or a refusal, with pinned denominators and a pre-registered paired bootstrap fixing each claim verb before the numbers existed. QueryProof, a 7B agent, uses rules derived from a semantic layer and physical catalog to determine its behaviour, and gates every answer on deterministic post-execution checks. On an 80-task synthetic test split evaluated once, QueryProof outperforms a direct-prompted 32B baseline by +0.237 [+0.112, +0.375] Business Truth Rate at 71.0% lower cost per correct answer; against a cost-matched few-shot baseline the accuracy gain holds but the cost difference does not resolve. This compares systems rather than model sizes: the 32B baseline receives none of the scaffolding. False success falls from 0.754 to 0.351 of returned answers, and no wrong number was returned on an answerable task (0 of 24), though 13 answers went to questions requiring clarification or abstention. Removing the routing layer changes little (0.562 against 0.537), so the result does not depend on escalation. Routing tuned on validation over-abstains on test, and the fitted confidence model loses to the heuristic it replaced. Resampling template families rather than tasks widens both accuracy intervals to include zero, so the effect's direction is better supported than its magnitude. The gain tracks the deterministic layer, though no component ablation was run.

---


### 319. [Can Coding Agents Solve Repository-Level Issues with Rendered Code? An Exploratory Study of Visual Representations](https://arxiv.org/abs/2608.09268)

**<font color=#1a73e8>作者：</font>** Weijie Liang, Yuanfeng Song, Xing Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual modality has recently been explored as a way to compress textual tokens, including rendering code as images for static code understanding. We study whether this representation can serve as operational context for agentic coding, where an agent must navigate repositories, edit source files, and verify executable patches. Using SWE-bench Verified, we evaluate rendered code in repository-level repair workflows and introduce controlled agent settings to separate unguided repository exploration from more structured repair stages. Our results show a mixed picture. Rendered code consistently reduces prompt-token cost, but the savings do not increase linearly with the nominal visual compression ratio. It largely preserves end-to-end repair accuracy, but does not overcome the performance limits of the underlying model or agent architecture, and can become unstable under aggressive compression. Further analysis suggests that visual code is most useful when raw source reading is a major bottleneck; once repository localization is structured, much of the remaining cost comes from patch--test trial-and-error, where visual compression has limited leverage. Overall, our study positions rendered code as a viable but conditional compression mechanism for realistic coding agents.

---


### 320. [Entropy-based Code Adversarial Translation for Real-world Repository Migration](https://arxiv.org/abs/2608.09273)

**<font color=#1a73e8>作者：</font>** Yushun Tang, Yisen Cao, Zhicheng Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs have demonstrated strong capabilities in code generation and automated program repair, but migrating an entire repository rarely produces a runnable application because long-horizon translation challenges LLM-based agents' ability to maintain repository-level migration objectives. In this work, we propose Entropy-based Code Adversarial Translation (ECAT), a multi-agent framework for automated Android-to-HarmonyOS repository migration. ECAT formulates repository migration as adversarial entropy minimization through a generator-discriminator architecture. The discriminator measures migration quality using a unified metric called Code Entropy and produces text gradients that specify both file-level generation directives and the skills needed to execute them. Guided by these optimization signals, the generator iteratively updates the repository, and each update is accepted only if it reduces Code Entropy. Repeated generator--discriminator interactions progressively drive the migration from an initial template toward a functionally complete HarmonyOS repository. Successful low-entropy trajectories are further distilled into a self-evolving memory tree, enabling transferable migration knowledge across repositories. We also introduce A2H-RepoBench, the first real-world benchmark for Android-to-HarmonyOS repository migration, covering applications from tens of thousands to hundreds of thousands of lines of code. Evaluated by node alignment and an agent-based functional judge, ECAT achieves 74.7% overall migration quality and consistently outperforms existing agent-based methods across repositories of different scales.

---


### 321. [P$^{3}$: Joint Program-and-Proof Planning for Verified Code Generation](https://arxiv.org/abs/2608.09277)

**<font color=#1a73e8>作者：</font>** Zenan Li, Ziran Yang, Peiyang Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verified code generation asks a large language model (LLM) to generate both an executable program and a machine-checkable proof that the program meets a formal specification, promising software that is correct by construction. The de facto workflow decouples the two halves of the problem: first synthesize a program, then attempt to prove it correct. We observe that this sequential pipeline can be both ineffective and inefficient in practice. A program generated without anticipating its proof can be subtly incorrect or structurally difficult to verify, forcing the LLM into brittle repair loops that alternate between patching the code and patching the proof. Inspired by Dijkstra's view that a program and its correctness argument should be developed hand in hand, we propose $P^3$, an LLM-based agentic workflow that first derives a unified program-and-proof plan from the specification, then elaborates the implementation and proof scaffold under this shared plan. To evaluate verified code generation in realistic settings, we further introduce Lean4Commit0, a repository-derived, library-level benchmark built by extracting core APIs from real-world software repositories and translating their requirements, including relational specifications across APIs, into Lean tasks. Using four frontier LLM backends, we evaluate $P^3$ on Verina, AlgoVeri, and our Lean4Commit0 benchmark, where it achieves the highest solve rate in every benchmark--model setting. Compared with the stronger baseline, it improves solve rates by 4.6--11.2 percentage points and reduces per-task API cost by up to roughly 40\% and wall-clock time by up to roughly 37\% on the difficult subset of each benchmark. A targeted ablation further shows gains of 3.3--8.3 points over implementation-only planning, isolating the benefit of planning the program and proof jointly.

---


### 322. [MMArch: Benchmarking Multimodal Reasoning Grounded in Architectural Evidence](https://arxiv.org/abs/2608.09281)

**<font color=#1a73e8>作者：</font>** Chenxu Du, Kang An, Tengyue Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) perform strongly on engineering imagery, yet existing benchmarks mostly test drawing recognition, information extraction, or compliance checking, leaving open whether models can combine distributed visual evidence with engineering principles to reach a conclusion. We introduce MMArch, a benchmark for architecture and civil engineering spanning ten subdomains and built entirely from figures in peer-reviewed papers. Its $1{,}212$ short-answer items are produced by a decoupled planner--writer pipeline and validated through automated screening, a blind adversarial audit, and expert review, so that answering requires perceiving the relevant evidence, identifying the governing principle, and applying it, not exploiting textual or single-figure shortcuts. Evaluating $18$ open-weight and proprietary MLLMs against a domain-expert panel, we find a wide gap: the strongest open-source model attains about $30\%$ and the best proprietary system $52\%$, while human experts reach $95\%$, more than forty points ahead. Our error analysis shows that failures concentrate in applying principles and combining evidence across figures rather than in locating it, pointing to substantial headroom for future research. Code and data are available at this https URL.

---


### 323. [ComboShoppingBench: Evaluating LLM Agents for Budget-Constrained Basket Shopping with Coupons](https://arxiv.org/abs/2608.09282)

**<font color=#1a73e8>作者：</font>** Adrian Li, Kelong Mao, Yudong Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world shopping often requires constructing a basket of complementary items rather than retrieving a single product. Such combo-shopping tasks arise in device setup, meal preparation, event planning, and group takeout ordering, requiring joint reasoning about item compatibility, availability, store-level requirements, delivery fees, coupons, and budgets. Evaluation is challenging because multiple baskets may satisfy the same request, making exact-match metrics unsuitable, whereas semantic evaluation alone cannot detect infeasible orders, invalid coupon combinations, or incorrect payments. We introduce ComboShoppingBench, an agentic shopping benchmark for open-ended yet verifiable basket construction in a simulated commerce and takeout environment. During task synthesis, an exploration agent constructs a feasible and semantically coherent basket of purchasable products; this witness guides the generation of coupons, budget constraints, user queries, and aligned evaluation rubrics. During evaluation, LLM judges assess semantic satisfaction, response quality, and claim faithfulness, while deterministic validation checks product-ID validity, budget compliance, and coupon optimality. Experiments with diverse LLM agents demonstrate that even strong agents struggle on ComboShoppingBench, highlighting substantial room for improvement in reliable, constraint-aware combo shopping.

---


### 324. [Accurate but Natural? Diagnosing Grammatical and Idiomatic Gaps in Japanese EFL Writing](https://arxiv.org/abs/2608.09289)

**<font color=#1a73e8>作者：</font>** Steve Woollaston, Brendan Flanagan, Hiroaki Ogata  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Second language writing research distinguishes grammatical accuracy from native-like idiomaticity, yet automated writing evaluation often conflates these dimensions. This study introduces a layered LLM-correction pipeline that isolates structural errors from unnaturalness by generating literal error corrections and idiomatic revisions for 3,830 English writing samples from 120 Japanese junior high school students. Applying the regex-based CEFR-J grammar extractor, we quantify two diagnostic measures: accuracy gaps (structures attempted but incorrectly produced) and idiomatic gaps (grammatically correct structures underused or overused relative to native norms). Results reveal distinct patterns: definite articles, third-person singular -s, and modals (would, could) exhibit significant accuracy difficulties, while -ing forms and hypothetical modals (would) show the largest idiomatic underuse, with simple present verbs, subject-verb-object patterns, and modal can conversely exhibiting the most pronounced overuse. A two-dimensional instructional typology maps error rates against idiomatic gaps, distinguishing accurate but overused grammar items from error-prone or avoided complex forms requiring targeted production practice. This framework advances pedagogical feedback by enabling teachers to diagnose whether learner difficulties arise from inaccurate execution, structural avoidance, or L1-mapped overreliance, supporting evidence-based interventions tailored to the specific needs of each learner.

---


### 325. [Beyond the Capability Boundary: Zeroth-Order Optimization for Self-Evolving LLM Agents](https://arxiv.org/abs/2608.09292)

**<font color=#1a73e8>作者：</font>** Bingzhen Liu, Xiaomeng Fan, Yuwei Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving methods improve the capabilities of LLM agents by sampling trajectories from the underlying LLMs and learning from these trajectories. However, these methods struggle to learn beyond the inherent capability boundary of the agents, since the agents cannot sample correct trajectories on difficult examples for further improvements. In this paper, we propose a zeroth-order self-evolution framework that enables agents to learn beyond their capability boundary by perturbing LLM parameters to adapt to difficult examples without any trajectory annotations. Specifically, we perturb LoRA parameters of LLMs, run the agent, compute the losses under the perturbed and original parameters, and use the loss difference to estimate gradients and further update the LoRA parameters. We sample trajectories using the updated LLMs for supervised fine-tuning to break through the capability boundary of the agents, forming a closed self-evolution loop. We introduce a parallel perturbation inference mechanism and an adaptive lookup mechanism to reduce time consumption in zeroth-order optimization, with an answer perplexity loss that provides smooth and stable zeroth-order loss values. Experiments on multiple deep research benchmarks show that our method obtains substantially more successful trajectories and consistently outperforms strong baselines, especially on difficult examples. The code and released artifacts are available at this https URL.

---


### 326. [Graphing the Everyday: A Neurosymbolic Approach to Eliciting Routines for Just-In-Time Adaptive Interventions](https://arxiv.org/abs/2608.09294)

**<font color=#1a73e8>作者：</font>** Shakyani Jayasiriwardene, Blake Mountford, Meican Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Just-In-Time Adaptive Interventions (JITAIs) increasingly rely on conversational agents to elicit user routines, yet translating fluid human dialogue into rigid schedule data remains a significant challenge. We conducted a qualitative investigation of a neurosymbolic pipeline, combining Large Language Models (LLMs) with a Neo4j knowledge graph, to map unstructured verbal narratives into actionable interventions. Through human-centric evaluation using natural-language playbacks, we identified a critical "mental-model gap," where the linear extraction of LLMs clashes with hierarchical, non-linear human storytelling, causing severe entity fragmentation. Furthermore, we articulate an "ecological mismatch," demonstrating that algorithmic schedule availability frequently ignores the user's fluctuating psychological receptivity and physical energy levels. To resolve these tensions, we propose actionable design heuristics, including routine piggybacking, adaptive negotiation, and scalable transparency. Ultimately, these guidelines provide a foundational framework for evolving rigid schedule-trackers into empathetic, context-aware proactive agents capable of supporting long-term health behavior change.

---


### 327. [Bootstrapping Vision-Language Model for Hysteroscopic Surgical Scene Segmentation](https://arxiv.org/abs/2608.09302)

**<font color=#1a73e8>作者：</font>** Jun Huang, Meiyi Chen, Zijie Yue 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hysteroscopic surgical scene segmentation plays a pivotal role in understanding the hysteroscopic intraoperative environment as well as computer-assisted intervention. However, this task presents unique challenges due to the high morphological similarity among different lesions and the presence of artifacts such as specular reflections, motion blur, and fluid occlusions in surgical videos. In this work, we propose the first vision-language model (VLM)-based hysteroscopic surgical scene segmentation method, which performs pixel-wise localization for fifteen representative categories in hysteroscopic surgical scenes. Our VLM-hyster has a segmentation backbone that utilizes the pretrained image encoder for robust visual feature extraction, coupled with a transformer-based decoder for dense prediction. Moreover, we design category-specific text prompts and incorporate a masked distillation branch to filter out visual features with low correlation to the text prompts, enabling the model to focus more effectively on category-specific image regions and thereby enhancing segmentation performance. We collect a large multicentric hysteroscopic surgical scene dataset, containing 4,020 high-resolution images with detailed mask annotations, for model training and evaluation. Experimental results demonstrate that VLM-hyster substantially outperforms state-of-the-art AI models. Furthermore, extensive assessments by gynecologists, as well as multicentre and prospective validations, demonstrate VLM-hyster's robustness and generalizability. The results suggest that VLM-hyster earns considerable potential in enabling AI-assisted localization of surgical instruments and lesions in hysteroscopic surgeries. Code is available at this https URL.

---


### 328. [MemeMind: Reference-Guided Trace Construction for Offline Context Optimization](https://arxiv.org/abs/2608.09316)

**<font color=#1a73e8>作者：</font>** Run Yang, Weihang Wang, Boheng Sheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Offline context optimization improves an agent by revising its instructions and examples while keeping the model frozen. This approach learns from rollouts on an adaptation set, but some queries produce only failed rollouts. In these cases, the optimizer sees no successful example of how the available tools can reach the correct answer. We introduce MemeMind, which uses an offline reference answer to recover this missing experience. TraceBuilder identifies the evidence required by the reference, executes text search, image retrieval, and visual grounding, and verifies the resulting tool trace before adding it to the adaptation buffer. ToolGuide then summarizes the collected traces into a shared guide and separate instructions for each tool. The reference answers and constructed traces are used only during adaptation, while inference uses the learned guides with a frozen model. We study this problem through Anime, Comic, and Game meme interpretation. These memes combine edited and ambiguous visual content, overlaid text, long tail franchise knowledge, and culture specific references. Their interpretation can require coordinated visual grounding, image retrieval, and text search, making them a demanding setting in which native rollout groups may fail together. We evaluate MemeMind on MemeX, a benchmark of 1,000 such memes annotated by experts. Across two Qwen3-VL models, two language partitions, and two independent judges, MemeMind improves over the strongest context optimization baseline by 22.0% and 21.1% on Qwen3-VL-30B-A3B, and by 8.1% and 8.0% on Qwen3-VL-235B-A22B under GPT-5 judging. Ablations and held out traces show that constructing successful tool use for failed groups provides the largest component gain and produces more effective evidence acquisition at inference time.

---


### 329. [LLM-Guided Heuristic Design from Simulation Traces: A Case Study in Dynamic Production and AGV Scheduling](https://arxiv.org/abs/2608.09343)

**<font color=#1a73e8>作者：</font>** Jinbo Li, Chuanhao Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulation-based optimization (SBO) evaluates executable policies under stochastic dynamics, but most methods treat the simulator as a black box: aggregate scores rank candidates without revealing why they fail or which policy logic should change. We present an LLM-guided heuristic design framework that uses repeated simulation for selection and event-level traces for diagnosis. Each incumbent is assessed through multiple replications, while replaying its lowest-scoring one produces a queryable trace. A manager agent formulates bottleneck hypotheses from this evidence, and editing agents implement parallel code-level revisions. After execution checks and repeated evaluation, best-so-far selection retains only improvements. LLM revision occurs between evaluation batches, while a fixed policy controls each simulation run.
We evaluate the framework in a discrete-event simulation of dynamic production and automated guided vehicle (AGV) scheduling. Across five independent optimization runs with Gemini-3.1-Pro, final mean scores averaged 77.51 on the simulator's 0-100 scale. In the highest-scoring run, trace-based diagnoses motivated proactive charging, distance-aware AGV assignment, and rebalanced dispatch priorities, raising the best-so-far mean score from 62.49 to 78.61. On 100 matched seeds, the best final policy outscored representative rolling-MILP, rule-based, and metaheuristic policies on every seed and retained its advantage under random faults without re-optimization. After separate re-optimization for a longer horizon and variable order interarrival times, the resulting policies again outscored all baselines. Ablations with two LLM backbones showed that removing either parallel candidate generation or trace-database access reduced final mean scores. These results show that simulation traces can guide targeted code-level policy improvement in complex simulation-based scheduling.

---


### 330. [Beyond Global Editing: Per-Instance Disentangled Subspaces for Training-Free Hallucination Mitigation in LVLMs](https://arxiv.org/abs/2608.09344)

**<font color=#1a73e8>作者：</font>** Ali Cheraghian, Hamidreza Dastmalchi, Hamed Barzamini 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in large vision-language models (LVLMs) have enabled powerful multimodal reasoning by integrating visual encoders with large language models (LLMs). However, their reliability is frequently undermined by hallucinations, where generated text inaccurately describes the visual input. Although fine-tuning can mitigate this problem, it is computationally expensive and requires large, curated datasets, making training-free alternatives attractive. Among these, model editing is more promising than decoding-based approaches: decoding methods adapt outputs per input but introduce computational overhead and instability, whereas model editing modifies internal representations offline, providing a more efficient and stable solution. However, existing model-editing techniques typically rely on a single global subspace to correct hallucinations, treating all test samples identically and failing to capture diverse hallucination modes across inputs. To address this limitation, we propose a training-free hallucination mitigation framework for dynamic, per-instance suppression at test time. Our method first constructs a set of Disentangled Hallucination Subspaces, each isolating a distinct hallucination mode. During inference, the model adaptively calculates weights reflecting each input's relationship to these subspaces, guiding a dynamically combined projection that selectively suppresses the most probable hallucination directions while preserving image-grounded semantics. Extensive experiments across multiple vision-language benchmarks and LVLM families demonstrate consistent improvements, highlighting the robustness, generalizability, and efficiency of our approach.

---


### 331. [Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at Matched Compute](https://arxiv.org/abs/2608.09351)

**<font color=#1a73e8>作者：</font>** Nikita Kozodoi, Zainab Afolabi, Jack Butler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling improves LLM accuracy but multiplies inference cost, making the accuracy gained per unit of compute the metric that matters in deployment. Self-consistency is one of the established approaches, which spends this budget entirely on the output side by sampling repeated reasoning paths. We study Test-Time Augmentation (TTA), which extends self-consistency by also perturbing the input, aggregating predictions across transformed versions of the input, and ask whether input-side diversity converts compute into accuracy more efficiently than output-side diversity. We perform a systematic, matched-compute comparison: we evaluate three simple input-side strategies (semantic rephrasing, lexical perturbations, and visual transformations) across six datasets covering general and multilingual knowledge, mathematical reasoning, multi-modal question answering, and sentiment classification, against chain-of-thought prompting and self-consistency. Semantic rephrasing delivers consistent and statistically significant accuracy gains while Pareto-dominating self-consistency on cost-effectiveness, delivering roughly 1.8X more accuracy per dollar and outperforming it on five of six tasks. We further analyze the number of augmentations, multi-modal strategies, and base model scaling, finding that TTA is most cost-effective for mid-tier models where a stronger model is unavailable or too expensive. Our findings indicate that for current mid-tier LLMs, varying the input converts inference compute into accuracy more efficiently than varying the reasoning path alone. The TTA implementation is available at this https URL.

---


### 332. [CircuitReason-1k: Benchmarking Long-Horizon Visual-to-Symbolic Reasoning inElectrical Circuits](https://arxiv.org/abs/2608.09374)

**<font color=#1a73e8>作者：</font>** Xinqi Yang, Kang An, Tengyue Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electrical circuit analysis requires more than recognizing components in an image. A solver must ground symbols and labels, recover latent topology, select a physical model, formulate coupled equations, propagate intermediate quantities, and preserve units, signs, directions, and phase conventions. We introduce \benchmark, a benchmark of 1,000 authentic textbook problems for evaluating this complete long-horizon visual-to-symbolic reasoning process. Each problem pairs one or more circuit diagrams with a self-contained question, a typed or semantically specified answer, and a reference worked solution. An evidence-first construction pipeline aligns questions, figures, and solutions, while a reasoning-oriented taxonomy organizes problems by circuit type and dependency depth. Evaluation combines conservative typed scoring with identity-blinded multi-model semantic consensus, retaining every problem in the denominator. Across three commercial chatbot systems and six open-source multimodal large language models, the highest-scoring system reaches 84.8\% accuracy. However, performance consistently deteriorates on long-horizon problems, and qualitative analysis exposes persistent failures in topology-to-target binding, physical conventions, and late-stage output propagation. \benchmark{} provides a focused testbed for measuring whether multimodal models can transform technical visual evidence into sustained, physically valid symbolic reasoning. Code are available at GitHub - CircuitReason/CircuitReason1K.

---


### 333. [OpenLoopEvolve: A Verifiable Self-Evolution Framework for Loop Policies in Long-Horizon Complex Tasks](https://arxiv.org/abs/2608.09380)

**<font color=#1a73e8>作者：</font>** Siqi Wang, Xinlin Li, Zhenglin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon complex tasks require agents to repeatedly observe states, formulate plans, invoke tools, verify results, and recover from failures in continuously changing environments. However, such control experience often remains confined to a single context or a fixed prompt, and is difficult to accumulate and reuse across historical traces. This paper presents OpenLoopEvolve (OLE), a self-evolution framework centered on the Loop Policy. OLE represents an agent's observation, planning, memory, action, verification, recovery, stopping, and budget control as portable policy assets with versions and lineages, and provides online and offline evolution modes that can be selected according to practical needs: the online mode triggers candidate generation based on feedback from continuous operation, whereas the offline mode searches for candidate policies from archived traces and failure evidence. Both modes share an evolution mechanism consisting of autonomous proposals by a large language model, Champion--Challenger paired evaluation, and robust release. Policies released online are activated at a subsequent task boundary, monitored using subsequent feedback, and rolled back to their parent versions when degradation conditions are met. On the simulated business benchmark YC-Bench, both modes improve aggregate task performance, task success rate, and risk metrics relative to a fixed initial Loop Policy. The results indicate that treating the Loop Policy as a governable asset can support the accumulation, comparison, release, and reuse of control experience and improve agent performance on long-horizon complex tasks.

---


### 334. [Imaginative Generative AI: Crossing the Entropy Wall into Worlds Beyond Imitation](https://arxiv.org/abs/2608.09385)

**<font color=#1a73e8>作者：</font>** Hossein Goli, Farzan Farnia, Amin Gohari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative AI models are primarily designed to imitate the data distribution, an objective that neither corrects diversity lost by a learned generator nor defines how generation should extend beyond the diversity of the data itself. We introduce Imaginative Generative AI (IGA), a framework that makes diversity part of the target-distribution design problem: among distributions close to a reference, IGA selects one whose spectral diversity reaches a prescribed level. Diversity is measured by the von Neumann entropy of the generated distribution's kernel covariance operator in a fixed representation space, providing a reference-free representation-guided measure of how broadly probability mass occupies embedding directions. The spectral entropy of the population data distribution defines an Entropy Wall. Below the wall, IGA performs diversity repair, recovering variation that a learned generator has lost while remaining within the diversity level of the data. Beyond the wall, the data distribution itself becomes infeasible, and IGA deliberately departs from it to produce distributions with greater representation-relative spectral diversity, an operational notion of imaginative generation. These regimes form a single regularization path from imitation to imagination and define an i.i.d. target distribution at each prescribed diversity level. We develop the theory of this entropy-constrained projection and show that, under a KL anchor to a pretrained generator, the optimum satisfies a self-consistent exponential-tilt relation. This characterization leads to IGA Guidance, a retraining-free inference-time method for score-based and diffusion models, including DDPM and DDIM samplers. Experiments on synthetic and vision benchmarks demonstrate diversity repair below the Entropy Wall and controlled spectral extrapolation beyond it.

---


### 335. [Temporal Misgrounding in Legal RAG: A Versioned-Corpus Benchmark for French Tax Law](https://arxiv.org/abs/2608.09393)

**<font color=#1a73e8>作者：</font>** Rose Cymbler, Daniel Guez, Laurent Fabre  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We identify and quantify temporal misgrounding: the systematic retrieval and citation of the currently in-force version of a legal article when the applicable version is an earlier or future one. Standard legal RAG treats the corpus as static; we argue legal question answering is a temporally-indexed retrieval problem. We introduce FiscalQA Pro, pairing a versioned corpus of 32,436 article-versions of the French tax code (93 years, 1938-2031) with an all-model-hard temporal-reasoning track: 209 scored, expert-reviewed questions across 33 CGI articles (221 released; twelve flagged out of the answerable scope). At selection time, no evaluated model recovered its date-applicable answer closed-book in any of four sampling draws, and the currently in-force text lacks the gold value for all but one of the scored questions. Answers are scored deterministically via atomic ground-truth "nuggets" (regex and numeric-with-tolerance), never LLM-as-judge: an LLM judge would inherit the temporal bias it is meant to score. Across eleven models (five frontier closed-API systems plus Gemini 2.5 Pro as a substitute entry, and five open-weight), parametric knowledge yields 3.0% mean strict accuracy and RAG over a static current-version corpus 2.7%. Static RAG retrieves the date-applicable version 0% of the time, confidently citing a real but inapplicable version. Our end-to-end retriever over a multi-version index, with no oracle, reaches 98.3% mean strict; an oracle-article ablation reaches 99.1%, locating the residual gap in first-stage recall, not version selection. We additionally release a version-aware jurisprudence dataset of 69,208 citation links, together with the corpus, benchmark, model responses, and pipeline code.

---


### 336. [KVDiagnosis: A Diagnostic Benchmark for KV-Cache Compression in Long-Context Language Models](https://arxiv.org/abs/2608.09412)

**<font color=#1a73e8>作者：</font>** Chen Qiu, Ziwu Liu, Chao Fei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> KV-cache compression reduces long-context memory, but aggregate task scores reveal neither which correct executions fail nor why. We present KVDiagnosis, a diagnostic dataset and benchmark with three contributions. First, a 25-method taxonomy groups methods into five mechanism families and links them to eight verified implementations and their valid diagnostic measurements. Second, for every supported method setting, we evaluate all sources in each fixed split against a per-source FullCache control before selecting FullCache-correct/compressed-wrong (C-to-W) rows separately for each method-setting, so no compressor defines another's test set. Third, a common record format links paired outputs and run metadata to cache, likelihood, attention, and decoding measurements with explicit applicability states. On Qwen3-8B, four evidence-aware workloads yield 59 800 supported compressed runs over 2600 sources and 12 520 C-to-W rows. Under fixed diagnostic rules, 63.2% have low or partial measured/projected coverage. Only 19 rows (0.2%) combine high measured/projected coverage with strong likelihood drift; another 2,126 (17.0%) preserve structural position addressability, for which representation fidelity remains unknown, while showing the same drift. Against C-to-C success controls, all ten diagnostics separate failed from successful compression (stratified AUROC 0.684-0.871). Among 96 reproducible low-EAR failures, a controlled 4x evidence-attention boost repairs 29.2%, versus 6.3% under a count-matched sham intervention and 3.3% degradation on matched C-to-C controls. Code and data are available at this https URL.

---


### 337. [Reducing Pretraining-Generation Mismatch in Diffusion Language Models](https://arxiv.org/abs/2608.09424)

**<font color=#1a73e8>作者：</font>** Xiaocheng Lu, Huabin Liu, Song Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models align training and use: generation conditions on a clean prompt, and training predicts future tokens from clean left context. Diffusion language models offer parallel denoising, but native dLLM pretraining can randomly corrupt prompt and continuation tokens together, weakening the clean-prefix interface needed for prompt-conditioned generation. We identify this mismatch for prompt continuation and propose PCD (Prefix-Conditioned Diffusion), a pretraining objective that combines AR prefix supervision with no-shift suffix denoising. At the training-objective level, PCD changes the attention mask, corruption mask, and label construction in continued pretraining; it does not require an autoregressive decoder, verifier, or new inference mode. By supervising the clean-prefix side autoregressively and applying diffusion only to the unknown continuation, PCD makes the local training interface resemble how block-diffusion models are queried at evaluation time. We further separate intra-sample prefix conditioning from inter-sample objective mixing, allowing us to identify the local alignment signal separately from the optional batch-level mixing knob. Across LLaDA2-Mini and Qwen-1.7B backbones, PCD consistently improves over same-family native dLLM stable baselines, reaching a 4.2% relative gain on the main LLaDA2-Mini six-benchmark average (+2.56 points) and a 14.2% relative gain in the primary Qwen mechanism comparison (+4.86 points). These results suggest that aligning the pretraining context distribution with prompt-conditioned generation can recover a measurable part of the dLLM continuation gap without changing inference.

---


### 338. [ZetaGPT: A Reference Implementation of Positional--Encoding--Free State--Space--Attention Language Models](https://arxiv.org/abs/2608.09432)

**<font color=#1a73e8>作者：</font>** Róisín Luo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models rely on self-attention, whose computation is permutation-equivariant and therefore lacks an intrinsic mechanism for representing token order. Existing architectures address this limitation by explicitly incorporating positional information through learned positional embeddings or hand-crafted positional encodings, such as rotary positional encoding (RoPE), treating positional information as an architecturally acquired capability rather than an inherent property of the model. Motivated by the pursuit of positional-encoding-free architectures, this work explores a language model architecture that integrates causal state-space equations to implicitly encode positional information before attention computation. Specifically, each model block applies a causal state-space equation before self-attention, allowing recurrent state dynamics to encode sequential information into token representations. Consequently, subsequent attention layers operate on position-aware representations without requiring explicit positional encodings while retaining the expressive modeling capacity of self-attention. We present \textsc{ZetaGPT}, a compact hybrid language model designed for research, rapid prototyping, algorithm verification, and educational applications. In addition to the proposed architecture, \textsc{ZetaGPT} provides a fully open-source, end-to-end training pipeline encompassing dataset construction, tokenizer training, pretraining, supervised fine-tuning, reinforcement learning from human feedback (RLHF), and chain-of-thought (CoT) reasoning via pure reinforcement learning. To the best of our knowledge, \textsc{ZetaGPT} is the first open-source small language model without explicit positional encoding and establishes a compact, reproducible reference implementation for the development and empirical study of positional-encoding-free language models.

---


### 339. [Listen, See and Track: Spatio-Temporal Audio-Visual Sound Event Reasoning for Omni-Modal Language Models](https://arxiv.org/abs/2608.09435)

**<font color=#1a73e8>作者：</font>** Zhi Zeng, Cheng Zhang, Zesheng Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding dynamic sound sources requires jointly determining what produces a sound, where the source is located, and how it moves over time. Yet existing audio-language models often represent clips as global acoustic events, while vision-language models lack the spatial audio cues needed to localize and track individual sources. To evaluate this missing capability, we introduce ST-OmniQA, a spatio-temporal audio-visual question-answering benchmark built from panoramic videos paired with synchronized first-order Ambisonics (FOA) audio of moving sound sources. It contains 40K videos and 400K question-answer pairs organized into four capability levels covering sound-event recognition, direction of arrival, source distance, motion trajectories, and temporally grounded audio-visual reasoning. Building on this benchmark, we propose ST-Omni-R1, which integrates FOA-derived semantic and trajectory representations with panoramic visual context and is trained through progressive curriculum learning and reasoning-tree reinforcement learning. ST-Omni-R1 achieves 77.83\% average semantic accuracy across the four levels, compared with 37.28\% for the best evaluated baseline. Results on three public spatial-audio benchmarks further indicate that its learned spatial and motion representations transfer beyond ST-OmniQA.

---


### 340. [Coupled Graph--Policy Distillation for Personalized Medication Safety in Older Adults with Multimorbidity](https://arxiv.org/abs/2608.09443)

**<font color=#1a73e8>作者：</font>** Zihan Wang, Anglin Liu, Rongyi Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can support medication review between clinical visits, but safe choices for older adults with multimorbidity depend on conditions, medications, and geriatric risks that users may omit. We introduce ATLAS, a coupled graph--policy distillation framework for patient-adaptive medication safety. ATLAS structures guideline evidence as a medication-safety graph. Targeted questions update the patient state and distill relevant relations into a patient-specific medication conflict graph (PMCG). A risk-first multi-agent policy uses the PMCG to screen contraindications, assess cautions and monitoring needs, identify safer alternatives, and verify the final medication plan. We also introduce GeriMedBench, an interactive benchmark that tests safety-critical information acquisition and evidence-based decision revision. Across a European non-interactive multimorbidity benchmark, an Asian interactive multimorbidity benchmark, and an Asian non-interactive cross-guideline benchmark, ATLAS achieves the strongest complete-decision performance among the compared systems. On the European non-interactive multimorbidity benchmark, it exceeds the strongest proprietary LLM baseline by 53.73 points in Strict Success Rate and 14.63 points in overall safety reasoning score (OSRS), with no unsafe recommendations under the automated evaluator. A blinded clinician evaluation gives ATLAS higher mean ratings across all five criteria and flags potentially unsafe recommendations in one ATLAS case and two Gemini cases.

---


### 341. [Depth-adaptive Inference of Looped Language Models via Continuous Depth Batching](https://arxiv.org/abs/2608.09444)

**<font color=#1a73e8>作者：</font>** Kristian Schwethelm, Daniel Rueckert, Georgios Kaissis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A main promise of looped language models (LMs) is depth-adaptive inference. By iterating a block of shared layers a variable number of times, the model can use less compute for "easy" tokens and more for "hard" ones. However, this adaptivity breaks standard batching: tokens in the same batch now require a different number of loops, so there is no unified forward pass, making efficient inference difficult. Standard inference frameworks like vLLM schedule on the token level and cannot handle this because tokens need to be removed from the batch within the forward pass. Loop-level scheduling has been proposed as a solution, but never implemented end to end. The key challenge is that looped architectures also contain non-looped boundary stages (e.g., token embedding and LM head) that must be scheduled at different frequencies than the loop. We introduce continuous depth batching (CDB), which schedules at the granularity of individual loop iterations. CDB handles boundary stages and loop steps in separate priority queues, makes exit decisions one step ahead, and overlaps all scheduling work with GPU computation. On Ouro 1.4B and Huginn 3.5B, CDB can realize up to $99\%$ of the theoretical maximum speed-up from adaptive-depth, translating to $1.5$-$1.9\times$ higher offline throughput and $45$-$90\%$ lower normalized latency under dynamic serving load.

---


### 342. [WDL-OPD: Weak-Driven On-Policy Distillation via Mixture-Constrained Co-Training](https://arxiv.org/abs/2608.09447)

**<font color=#1a73e8>作者：</font>** Zehao Chen, Gongxun Li, Tianxiang Ai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) aligns a student with a teacher on trajectories sampled from the student itself, reducing the train-test state mismatch of offline distillation. The same feedback loop can nevertheless be unstable: each update changes both the policy and the states on which the next update is computed. We introduce WDL-OPD, a mixture-constrained co-training method with two trainable policies. An anchor policy generates every rollout, an auxiliary policy evaluates the same visited states, and a geometric mixture of their token distributions is matched to a frozen teacher by reverse KL. Both policies receive gradient. We show that freezing the auxiliary recovers an anchor-plus-contrast proxy target closely related to OPD$^2$ and W2S-OPD, whereas joint training creates branch-level degrees of freedom that a static delta cannot express. In recorded Qwen3 experiments at 1.7B and 4B scale, WDL-OPD produces the strongest student checkpoint in each of four scale-domain settings. It raises MATH500 accuracy from 0.630 to 0.685 at 4B and from 0.521 to 0.585 at 1.7B. In code generation, seven single-policy OPD configurations exhibit entropy growth or trajectory degradation, while co-training reaches independently re-evaluated development scores of 0.637 and 0.375. Because several comparisons differ in curriculum or initialization, these results support a stabilization hypothesis rather than a universal causal claim. We provide the exact training algorithm, failure evidence, and the controlled comparison matrix needed to test that hypothesis.

---


### 343. [RecoverFly: A Failure-Aware Reinforcement Learning Post-Training Framework for Aerial Vision-Language Navigation](https://arxiv.org/abs/2608.09467)

**<font color=#1a73e8>作者：</font>** Boxiong Wang, Hui Kang, Geng Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle vision-language navigation (UAV-VLN) requires agents to translate visual observations and language instructions into reliable flight actions in complex environments. Although recent end-to-end UAV vision-language-action (UAV-VLA) policies reduce reliance on separately designed perception, planning, and control modules, their behavior-cloning objectives provide limited corrective supervision for interactive closed-loop execution. Reinforcement learning (RL) offers a promising solution, while its effectiveness is constrained by inefficient use of samples, long-tailed scene distributions, and policy distribution shift during optimization. To this end, we propose RecoverFly, a failure-aware RL post-training framework for end-to-end UAV-VLA policies. Specifically, RecoverFly adapts token-level RL for stable optimization of grammar-constrained autoregressive UAV actions, revisits unresolved failure cases to strengthen corrective learning and sample utilization, and combines a two-stage long-tail scene curriculum with reference-policy regularization to improve scene adaptation while preserving acquired capabilities. Experiments on the TravelUAV benchmark demonstrate that RecoverFly achieves the best performance on the seen, unseen-map, and unseen-object splits. Moreover, compared to the AerialVLA initialization, RecoverFly improves success rate by 3.12 to 8.37 percentage points under a total rollout budget of about 30\% of the training-set size, validating its effectiveness, robustness, and generalization capabilities.

---


### 344. [FaLCon: Facet-Anchored Retrieval with Late Consensus for Sim2Real Text-Based Person Anomaly Search](https://arxiv.org/abs/2608.09474)

**<font color=#1a73e8>作者：</font>** Hieu Dinh Trung Pham, Phuong Huu Vu Tran, Thuan Duc Mai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-based person anomaly search requires retrieving real-world pedestrian images from detailed natural-language descriptions using models trained primarily on synthetic data. This Sim2Real setting is particularly challenging because visually similar candidates may differ only in subtle actions, object interactions, or appearance attributes, while applying multimodal large language models to the entire gallery is computationally expensive. We propose an anchor-constrained coarse-to-fine retrieval framework that combines global semantic matching with fine-grained verification. First, each query is represented by its original caption, a structured concatenation, and several semantic facets. Heterogeneous vision-language retrievers are then integrated through robust per-query score calibration and soft claim-aware fusion. Full and concatenated captions serve as anchors to preserve candidate recall, whereas appearance, action, and object facets provide bounded corrective evidence. The resulting candidate pool is further refined by a discriminative Qwen3 reranker and two complementary semantic verification modules based on anomaly-aware cloze completion and multi-agent evidence reasoning. Finally, an uncertainty-gated consensus module adaptively reweights the three experts on ambiguous queries. Experiments on the PAB benchmark show that the proposed soft claim-aware retrieval achieves 86.44% mAP@10, substantially outperforming individual retrieval backbones. The complete framework further improves performance to 95.41% mAP@10, 94.44% R@1, and 99.09% R@5. These results demonstrate that preserving strong global retrieval while restricting expensive semantic reasoning to a small candidate pool is effective for fine-grained Sim2Real person anomaly search. Our code will be available on Github.

---


### 345. [Agreement-Based Audio-Visual Segmentation:Champion Report for the MeViS-Audio Track in the 8th LSVOS Challenge](https://arxiv.org/abs/2608.09475)

**<font color=#1a73e8>作者：</font>** Yiwen Ren, Jianing Liu, Yingxin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The MeViS-Audio track asks a system to segment the objects described by a spoken motion expression throughout a video and to return empty masks when the described target is absent. We present a simple staged solution. Qwen3-ASR first converts speech into text. Several video mask tracks are then produced with complementary grounding and segmentation models. Instead of trusting a single prediction, we select the track that has the highest average mask agreement with the other candidates. A small set of explicit direction, count, and plural rules corrects queries that require more than ordinary single-object tracking. Finally, a video-level classifier combines visual, audio-visual, and within-video query scores to decide whether any target is present. The submitted system obtains 0.5952 J &F, 0.7931 no-target accuracy, 0.9205 target accuracy, and a final score of 0.769589. The challenge organizers notified our team that this result ranked first in the track.

---


### 346. [ActBench: Self-Evolving Benchmark of Behavioral Safety in Cowork Agents](https://arxiv.org/abs/2608.09476)

**<font color=#1a73e8>作者：</font>** Hongwei Yao, Yiming Liu, Meihui Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cowork agents may complete benign tasks while disclosing protected data, manipulating unauthorized state, invocate unauthorized API. We define behavioral safety and introduce ActBench, a self-evolving benchmark that evaluates such behavior risk from execution trajectories rather than final responses. Each case pairs a benign task with an adversarial variant that preserves its instruction, configuration, initial state, rating model, and trusted records while injecting a task-reachable payload. ActBench contains 600 cases from 213 scenarios, spanning 15 risk behaviors, six execution spaces, and 48 web-service this http URL move beyond static payloads, we propose a reward-guided beam search method that jointly optimizes attack effectiveness and task utility, while reflection diagnoses failed execution checkpoint and guides payload revision. Besides, we propose a dual evidence verification mechanism that verifies agent execution safety and utility through log evidence and LLM-based trajectory this http URL evaluate 15 LLMs and 6 open-source cowork agents over 24,000 trajectories. Under a fixed harness, attack success rates ranges from 10.1% to 94.4% across models, while under a fixed base model, they range from 73.7% to 94.4% across this http URL results show greater variation across models than agent harness, while attacks remain highly successful across all tested this http URL benchmark is released at: this https URL.

---


### 347. [Capability Is Not Propensity: Measuring Pressure-Robust Cooperative Behavior in Civic LLM Agents](https://arxiv.org/abs/2608.09485)

**<font color=#1a73e8>作者：</font>** Neel Tushar Shah, Manglam Kartik, Akshat Karkar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cooperative capabilities in language models are dual-use. The same social reasoning that supports civic deliberation can also enable strategic omission, false consensus, and manipulative framing. We argue that Cooperative AI evaluations should separate what models can do under benign instructions from what they tend to do under realistic civic pressure. We introduce DiffCoop-Civic, a 10-scenario pilot evaluation suite spanning preference understanding, evidence and persuasion, commitment design, asymmetric information, and dissent preservation. Across seven models from four model families, subtle omission pressure produces a near-uniform shift: manipulative enablement rises by 1.17 points and dissent preservation falls by 1.67 points on a 5-point scale. Overt false-consensus pressure behaves differently: it triggers refusal or redirection in some aligned API models, but direct compliance in several open-weight models. A lightweight Pareto-Trace prompting intervention improves pressure robustness without simply relying on hard refusal. An anonymous reproducibility package is available at this https URL.

---


### 348. [When Do Task Vectors Interfere? Mapping the Validity Boundaries of Weight-Space Composition](https://arxiv.org/abs/2608.09490)

**<font color=#1a73e8>作者：</font>** Chencheng Zhu, Xiaoyang Li, Taotao Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task arithmetic treats fine-tuning displacements as composable directions in weight space, yet it remains unclear when parameter addition reflects predictable changes in model function. We separate parameter geometry from functional geometry and measure pairwise functional non-additivity over a two-dimensional task-vector surface, using a first-token predictive-distribution interaction ratio conditioned on an input distribution and evaluated with norm-matched controls, three training seeds, and response-only fine-tuning. On Qwen2.5-1.5B, code+safety is more non-additive than the matched code+math control on code and instruction prompts, but not on math prompts. In a prospectively specified six-task expansion, all eight high-versus-low comparisons of unseen task pairs have the predicted sign. The primary ordering further persists under full-parameter fine-tuning at 0.5B, Qwen2.5 LoRA scale tests up to 7B, and a Llama-3.1-8B cross-architecture audit. External validation exposes a sharper boundary: raw public code, instruction, and safety prompts preserve the continuous contrast, whereas an instruction-style wrapper collapses it on the identical public-code prompts, and EvalPlus pass@1 interactions do not robustly reproduce it. Weight-space composition therefore supports coarse, input- and format-conditioned functional statements across adaptation methods, scales, and one additional model family, not a universal merging-performance predictor.

---


### 349. [GeoRoute: Geometry-Aware Hybrid Inference for Traffic Future-Frame Prediction](https://arxiv.org/abs/2608.09493)

**<font color=#1a73e8>作者：</font>** Khang Minh Le, Hieu Dinh Trung Pham, Luu Thanh Danh 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon future-frame prediction is important for autonomous driving, traffic surveillance, and intelligent transportation systems, yet remains challenging due to temporal ghosting, geometry drift, and inconsistent object motion. Recent latent video diffusion models have achieved impressive visual quality, but directly applying them to structured traffic scenes often leads to unstable geometry and degraded temporal coherence over extended horizons. We present a training-free inference framework that stabilizes reliable static structure in pretrained video predictions through multi-frame temporal context and view-conditioned routing. For front-camera videos, our method refines generated futures with a multi-frame depth-layered renderer that projects static geometry from observed history frames while preserving dynamic regions from the generative base model. For heterogeneous traffic views, a frozen vision-language model infers a coarse camera group from the observed clip and selects a specialized motion-based predictor. The framework requires neither retraining nor fine-tuning of the underlying video model and can be applied directly to pretrained generators. We validate the proposed framework on the AI City Challenge Track 5 benchmark, where our final system achieves competitive performance among the top-ranked teams. These results demonstrate that geometry-aware inference-time refinement and view-conditioned hybrid inference can improve static-geometry stability and low-level structural fidelity without changing the original model architecture.

---


### 350. [Learning Preference Adaptation for Large Language Model Personalization via Verbal Reinforcement Learning](https://arxiv.org/abs/2608.09507)

**<font color=#1a73e8>作者：</font>** Yuting Liu, Wei Wu, Jianzhe Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language user preferences provide an interpretable interface for LLM personalization. However, universal preference summaries often contain information irrelevant to a particular downstream task. Directly supplying the full preference summary therefore wastes context capacity and introduces cross-task distraction, while manually designing task-specific preference views is difficult to scale. In this work, we study \emph{task-specific preference adaptation}: given a universal user preference summary and a downstream task, derive a task-conditioned representation that preserves sufficient decision-relevant evidence while removing redundant context. To this end, we propose \textsc{AlignXada}, a training-free meta-learning framework that induces reusable textual refinement policies for adapting universal preference summaries to task-specific ones. The refinement policy is iteratively optimized by a meta learner through verbal reinforcement learning. Across 13 tasks and three downstream models (39 task--model cells), \textsc{AlignXada} achieves an average gain of 3.82 points, improving 33 cells while retaining only 22.8\% of the original profile tokens and outperforming RAG in 36 cells. An extended faithfulness analysis further shows that the refined profiles remain largely grounded in the source preferences while preserving task-relevant personalization signals, suggesting that profile-side adaptation serves as a practical complement to universal memory construction for lifelong personalized agents.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
