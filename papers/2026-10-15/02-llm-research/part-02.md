# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 51. [ACED-Bench: Evaluating How LLM Agents Acquire and Act on Causal Evidence](https://arxiv.org/abs/2610.14381)

**<font color=#1a73e8>作者：</font>** Yiwei Chen, Amila Weerasinghe, Siddharth Biswal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as scientific assistants, yet we still lack reliable ways to evaluate whether they can investigate a system rather than merely answer a prompt. A useful evaluation must let agents choose experiments, interpret finite evidence, and make causal decisions, while keeping the environment coherent across repeated observations and interventions and preserving objective ground truth. We introduce ACED-BENCH (Active Causal Evidence and Decision Benchmark), a neuro-symbolic benchmark built around this requirement. The key idea is to separate the readable scientific surface from the formal causal world: LLMs generate natural-language scenarios and task text, while hidden probabilistic graphical models define the causal graph, data-generating process, intervention semantics, validation checks, and oracle answers. This yields scientific worlds that are natural for agents to investigate but exact enough for scalable, programmatic evaluation. The main leaderboard ACED-CORE contains 180 tasks: 60 set-valued causal ancestry/descendancy questions and 120 constrained causal-decision tasks. We also report ACED-QUAL, a 150-question yes/no qualification check using the same hidden-PGM interface. We evaluate seven contemporary LLMs and two earlier-generation models across three active agent designs. ACED-QUAL checks whether agents can use the interface to draw conclusions from evidence, while ACED-CORE tests whether they can decide what evidence to collect and when to commit to an answer. Evidence-ledger analysis localizes failures within the investigation: agents test the wrong intervention, lose relevant evidence, or continue after sufficient evidence has appeared. These results suggest that reliable AI co-scientists need explicit support for experiment design, evidence retention, answer commitment, and stopping.

---


### 52. [Measuring the Inference Energy Efficiency of Open-Weight LLMs across Benchmarks, Reasoning Modes, and Hardware](https://arxiv.org/abs/2610.14389)

**<font color=#1a73e8>作者：</font>** Zeyu Yang, Wes Armour  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmark scores tell us what an LLM can do, but not how much energy is required to deliver that capability. We directly measure this trade-off for 86 open-weight model checkpoints, evaluated on seven benchmarks and six hardware platforms ranging from a consumer GPU to an eight-GPU server. We find large differences in energy efficiency even among models with similar capability. Most configurations lie away from the score--energy Pareto frontier: they use a median of 2.6--4.8$\times$ more energy than another configuration that scores at least as well, with differences reaching 27$\times$. Reasoning can improve capability, but enabling thinking increases energy by about 3.7$\times$ on average, and the benefit depends strongly on the model family and output budget. Generated-token count is also an imperfect proxy for energy, misordering 18--24\% of model pairs. In contrast, FP8 reduces energy by roughly a quarter with little change in score, while changing hardware largely rescales energy without changing the relative ranking of models. These results show that capability alone gives an incomplete picture of efficiency. We argue that benchmark scores should be reported together with measured energy consumption under a specified serving regime and output budget.

---


### 53. [SciCurateBench: Curating Experimental Data from Heterogeneous Scientific Literature with Verbal-Action Agents](https://arxiv.org/abs/2610.14393)

**<font color=#1a73e8>作者：</font>** Minuk Ma, Kaiyun Guo, Jiarui Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific research increasingly depends on curating experimental data from literature. Scientific data curation requires verifying exact experimental conditions (e.g., specific assays, clinical outcomes, and data availability) across long, heterogeneous files, which is a highly time-consuming process. Existing benchmarks evaluate only broad relevance on short queries, failing to capture this complexity. We introduce SciCurateBench, a benchmark of 200 expert-annotated papers from major life-science journals that challenges systems to verify conjunctive biological experimental criteria from raw, unprocessed scientific literature. We show that plain LLMs and popular reasoning, tool-using, and feedback-based agents all struggle with this task. To study what makes the task tractable, we further propose LangPoli, an integrative system in which a policy agent generates natural language action guidelines that actor agents convert into executable tools. LangPoli showed strong performance on both Paper Classification (83.16% F1 vs. 58.22% for its base LLM) and Structured Information Retrieval, and also improves re-ranking on the public benchmarks of LitSearch, BEIR, and TREC. We further explore curriculum transfer, a method that distills generalizable strategies from solved tasks to accelerate the solving of related problems. We hope this work facilitates research in truly practical scientific AI assistance. The anonymized pre-release can be found from https://anonymous.4open. science/r/scicuratebench-D885/.

---


### 54. [RealityBench: Simulated Environments to Evaluate a Vision Language Model's Ability to Document Human Physical Work](https://arxiv.org/abs/2610.14397)

**<font color=#1a73e8>作者：</font>** Andrew Perrault, Anmol Takiar, Dominik Wienecki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Augmenting worker capabilities in the physical world through guidance has been a decades-long goal for AI agents. One key supporting capability is to understand what the worker is doing, seeing through the human's camera or smart glasses, and assist them in documentation. Despite advances in vision language models, their capabilities in these settings remain uncertain and are challenging to benchmark because most physical work data is proprietary, and involves too much variability to study in a principled manner. Unlike structured settings such as kitchens and warehouses that have predictable lighting, geometry, and objects, field-facing tasks such as rooftop solar installation and vehicle repair are unconstrained and high variance. Here, we model real-world physical work in Blender across eleven environments, incorporating variants in both image acceptability and documentation. The acceptability task asks whether a particular view would be suitable proof-of-work and documentation asks whether an agent can understand the task-relevant state of the environment from that view. Across 26 vision-language models, we find that top models largely solve documentation when the answer is text in frame, but are weak at reading measurements and at judging small parts and spatial relations, such as whether a tape measure leans. Acceptability is harder to pin down because human raters disagree with each other. Measured against a scorer that agrees with the raters' majority about as often as a single rater does, the best models cannot be distinguished from a single non-author rater, at a cost within the range of a human pass. In the three environments where we can trace acceptability errors, most wrong rejections come from misreading the scene rather than the requirement. On the three documentation questions for which we have real images, model rankings on rendered frames transfer to real images.

---


### 55. [SAT-RL: Training Language Models for Logical Reasoning with Symbolic Solvers](https://arxiv.org/abs/2610.14402)

**<font color=#1a73e8>作者：</font>** Jialiang Sun, Kuldeep Meel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved strong performance in mathematical and logical reasoning, yet they still suffer from the curse of complexity and struggle as problem difficulty increases with the number of constraint interactions and the size of the search space. In contrast, satisfiability solvers such as Z3 provide scalable and verifiable reasoning through constraint solving under formal theories, but lack the flexibility to interpret natural-language problem descriptions. In this work, we propose SAT-RL, a reinforcement-learning (RL) framework that trains LLMs to interact with symbolic solvers through multi-turn tool execution. SAT-RL leverages synthetic data generation with verifiable solutions, supervised warm-up on solver-augmented traces, and solver-grounded reinforcement learning with tool-aware rewards. Experiments show that SAT-RL substantially improves symbolic reasoning with tools on both in-domain and out-of-domain logic tasks. Our code is available on this https URL.

---


### 56. [VisualCoding: Learning Executable Skills for Reliable Visual Reasoning](https://arxiv.org/abs/2610.14403)

**<font color=#1a73e8>作者：</font>** Liu Jiaqi, Jin Ruinan, Li Xiaoxiao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning reusable skills can improve visual reasoning agents, yet applying a skill still requires the agent to implement or invoke a procedure and produce the final answer. Errors and hallucinations at these steps can prevent acquired experience from translating into reliable single-run performance. We propose VisualCoding, which combines execution-guided acquisition of reusable visual programs with direct adoption of their answers on applicable inputs. Execution-Guided Program Acquisition composes visual primitives and additional code into family-level solvers, then iteratively tests and revises them on labeled training instances. Scope-Aware Direct Execution runs a retained solver and returns its valid in-scope answer. We evaluate VisualCoding on four models across four benchmarks spanning 69 task families. VisualCoding exceeds the strongest evaluated baseline in mean accuracy by 4.45 percentage points with Gemini-3.1-Pro and by 14.78 points when reusing the frozen Pro-acquired artifacts with Flash-Lite. Ablations support execution-guided acquisition and show that direct execution outperforms textual or callable reuse of the same programs. Code is available at this https URL.

---


### 57. [Coarse-Graining Recursive Expert Computation: Continuation-Relative Interfaces and Failure Modes](https://arxiv.org/abs/2610.14413)

**<font color=#1a73e8>作者：</font>** Shihua Yu, Yanzhi Wang, Tianchi Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computational coarse-graining aims to replace a sequence of updates with a cheaper module while preserving task performance. We present a continuation-relative evaluation framework that assesses replacements through the computation that follows them, using downstream task quality and total execution cost as joint criteria. The framework distinguishes boundary representations, summaries of skipped computation, executed operations, and downstream loss. It makes interfaces and permitted deployment information explicit, combines fine-path references with directly trained controls using the same shortened architecture, and accounts for selection overhead. An exact loss decomposition separates replacement effects at a fixed downstream action from effects of changing that action. A finite construction shows how retained information can reduce the stipulated cost of zero-error prediction under fixed information and controller restrictions. Experiments in two frozen pretrained language models show that representation fidelity and task loss can favor different fitting objectives. In a prespecified comparison on a 1.7-billion-parameter model, next-token-loss training lowers in-distribution negative log-likelihood by 0.1901 nats per scored token compared with reconstructing the skipped blocks' output, using the same optimizer and update count. This ranking reverses in all nine paired comparisons under distribution shift. In a recursive expert prototype, the jointly adapted candidate lowers task error relative to frozen-bank and router-only baselines, but trails directly trained controls, and the tested input-only selectors fail the joint quality-cost criteria. Together, the protocol and studies provide explicit criteria and diagnostics for distinguishing useful computational replacement from local approximation gains within specified interfaces and evaluation settings.

---


### 58. [Scaling Laws for Multimodal Data Mixtures](https://arxiv.org/abs/2610.14423)

**<font color=#1a73e8>作者：</font>** Aditi Khandelwal, Ayush K. Tarun, Yixuan Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier AI systems are increasingly natively multimodal, jointly pretrained on multiple modalities, such as text, vision, and audio. However, the scientific understanding of the multimodal data mixtures used to pretrain these systems --- how much of each modality to mix, and at what potential interference cost to the others --- is largely absent or gatekept. In this work, we derive data mixing scaling laws for three modalities: text, vision, and audio. Multimodal Large Language Models (MLLMs) increasingly adopt Mixture-of-Experts (MoE) architectures, as MoEs scale efficiently and partially limit cross-modal interference. We therefore use MoEs to conduct 268 experiments ranging from 457M to 8.3B parameters, on up to 150 billion tokens. Our work leads to multiple actionable insights into multimodal data mixing for training MLLMs. First, compute optima are modality-specific: audio modality is model-heavy, favoring scaling parameters over tokens, while text and vision require balanced scaling of model size and data. Second, repeating vision or audio data beyond 2x yields negligible benefits. Finally, cross-modal interactions are highly asymmetric: vision strongly interferes with audio, whereas audio's interference with learning text and vision is negligible. Overall, we provide a principled foundation for understanding the multimodal data mixtures needed to train frontier MLLMs.

---


### 59. [ByteMark: A Unified Byte-Level Watermark for Detection Across Language Models](https://arxiv.org/abs/2610.14427)

**<font color=#1a73e8>作者：</font>** Xiaopu Wang, Runze Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As watermarking of LLM-generated text enters deployment, users increasingly need to check text whose source is unknown. Existing detectors read the watermark through a specific tokenizer or embedding pipeline, and even if all providers adopted the same watermarking method, differences in these representations would leave their watermarks incompatible, and the text alone does not reveal which representation produced it. We propose ByteMark, a unified watermarking scheme that defines its signal on the UTF-8 bytes of published text. Models with different tokenizers embed this signal under one public specification and key, and a single detector verifies the text from the text and key alone. When the tokenizer or embedding model of a baseline detector is replaced, its detection degrades sharply, whereas ByteMark, which uses neither, retains its detection rate; ByteMark also remains detectable when participating models continue or rewrite the text.

---


### 60. [Frustratingly Easy Agentic RAG via Portable Skills: A Case Study in Customer Support](https://arxiv.org/abs/2610.14428)

**<font color=#1a73e8>作者：</font>** Istok Bako, Bonan Min, Tiffany Shao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise workflow automation typically requires retrieving a complete and accurate set of relevant information from large operational document corpora (SOPs, policy documents) given a specific scenario or request. In customer support (CS), for example, human specialists must determine the correct sequence of resolution steps for each case, a task that demands precise grounding in policy documentation. Meeting this bar in production typically requires complex document chunking, indexing, and retrieval pipelines, often layered with learned re-rankers, query rewriters, and bespoke agentic RAG infrastructure.
We report a deployment case study of a simpler alternative: a portable skill consisting of a natural-language instruction, lightweight tools (a retrieval API, format-checking scripts), and a corpus enriched with an LLM-generated navigation layer, which is a structured "Wikipedia-style" index over the underlying documents. This agentic RAG approach is straightforward to implement (1-2 engineer days), portable across capable agentic harnesses (e.g., Claude Code), and performs strongly on the challenging task of CS resolution workflow generation, achieving 99.2% procedural equivalence to human-approved ground truth and 83.3% evidence sufficiency. It is also roughly an order of magnitude slower per case than our deployed production assistant (~90 s vs. ~8-9 s), so we claim no latency advantage. Our claim is scoped to that setting: a mature, well-curated corpus, a latency-tolerant workflow, and human review of every case. There, the skill did the work of a complex RAG stack, and maintenance became a matter of editing text and data rather than retraining models.

---


### 61. [Neither True nor False: Do LLMs Represent Truth-Value Gaps in Plural Predication?](https://arxiv.org/abs/2610.14438)

**<font color=#1a73e8>作者：</font>** Duaa Nakshbandi, Zhiyu An, Yiping Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do Large Language Models (LLMs) genuinely grasp the truth conditions of plural descriptions, or do they force every sentence into true or false? We investigate the Homogeneity Gap, a semantic phenomenon where a plural definite (e.g., the kids laughed) and its negation (the kids didn't laugh) are both neither true nor false when only some of the kids laughed, whereas their quantified counterparts (all, not all) remain strictly bivalent. We introduce HomogeneityNLI, a diagnostic dataset of 1,000 minimal-pair items crossing determiner, polarity, and group composition across ten logical conditions. Evaluating seven open-weight models, we uncover a pervasive Bivalence Bias: models assign plural definites their homogeneous truth conditions, reading the kids as all of them and the kids didn't as none of them, yet collapse the truth-value gap into falsity. In the zero-shot setting, no model recognizes the gap for both polarities in more than 15% of scenarios, and negated definites are judged False in 84% of cases. Explicit linguistic rules, chain-of-thought, and enumeration prompts produce unstable, model-specific effects that often entrench the bias. Taken together, our findings indicate that current open-weight LLMs have acquired the truth conditions of plural predication but not its trivalent logic.

---


### 62. [SceneForesee: Learning Scene Evolution for Spatiotemporal Reasoning](https://arxiv.org/abs/2610.14439)

**<font color=#1a73e8>作者：</font>** Chaoyue Li, Shoudong Han, Haoyang Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large multimodal models (LMMs) need to understand how entities move and interact as a scene develops. This requires following the same entities over time and relating their observed motion to subsequent changes. We formulate Scene Evolution Understanding (SEU), a task for predicting and interpreting this change. Given observed video, a model estimates entity histories and predicts one scene continuation through future trajectories and Events, accompanied by Visual Evidence from observed motion and a scene description. We construct SceneForesee, a benchmark for evaluating entity continuity and scene evolution reasoning through paired observed and future scenes with shared entity identities. It contains 144.57K temporal pairs, 1.05M entity correspondences, and 272.49K Events paired with observed evidence. We propose a spatiotemporal reasoning framework, EvoSee, that learns future geometry and Event semantics through shared candidate states and joint assignment. It selects one continuation per entity from observation and uses the selected changes for entity refinement, retention, and scene representation. On SceneForesee, EvoSee outperforms Qwen3.5-9B by 10.45 points in Combined Point-F1 and 17.24 points in Event Global F1. On the 4D reasoning benchmark Dyn-Bench, it improves question answering accuracy and grounding J&F by 4.8 and 3.58 points over their respective base systems. These results support scene evolution as both a prediction target and a dynamic representation that brings predicted entity changes into spatiotemporal this http URL project is available at this https URL.

---


### 63. [Target-ESS Tempered Policy Optimization (TETPO): Smooth Variance Control via Bridge Importance Sampling](https://arxiv.org/abs/2610.14440)

**<font color=#1a73e8>作者：</font>** Shayan Mohajer Hamidi, Kayhan Behdin, Wenhui Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous reinforcement-learning post-training of large language models is computationally efficient but inherently off-policy: the learner updates on rollouts generated by a stale policy, while correcting this mismatch requires importance weights that can be extremely heavy-tailed. A small number of trajectories may then dominate an update, collapsing the effective sample size (ESS) and increasing the variance and instability of the resulting gradient estimates. Existing stabilizers apply fixed interventions regardless of the realized severity of weight concentration, either discarding selected samples or reweighting them without adapting the correction strength. We introduce \emph{Target--ESS Tempered Policy Optimization} (TETPO), which replaces each importance weight $\rho$ by $\rho^\alpha$ for a data-adaptive exponent $\alpha\in[0,1]$: $\alpha=1$ preserves the original importance weights, whereas $\alpha=0$ assigns uniform coefficients. For each prompt group, TETPO selects the largest $\alpha$ whose tempered weights satisfy a target ESS fraction $\kappa$, applying little tempering to healthy groups and stronger tempering when weight degeneracy is severe. At the population level, the tempered coefficients are exact importance weights for a geometric bridge between the sampler and learner policies. The exponent is efficiently found by one-dimensional bisection, while the resulting weights satisfy deterministic bounds on normalized-weight dispersion and weighted-gradient norm that are independent of policy drift, together with a fixed-$\alpha$ bound on bridge-target discrepancy. Power tempering also introduces no explicit zero-weight mask. On mathematical-reasoning benchmarks under high staleness, TETPO outperforms strong on- and off-policy baselines.

---


### 64. [Evaluating Semantic Relation Knowledge through Bidirectional Relation Prediction from Gloss Pairs](https://arxiv.org/abs/2610.14442)

**<font color=#1a73e8>作者：</font>** Zhihan Cao, Adam Nohejl, Hitomi Yanaka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic relations organise word senses and are fundamental to lexical semantics. In order to evaluate semantic relation knowledge of large language models (LLMs), we propose a challenging task in which an LLM predicts the relation between two glosses (definitions of senses) presented in two different orders. The predictions for the two orders are evaluated for consistency with the symmetry or asymmetry of semantic relations. Our task is designed for both monolingual and cross-lingual evaluation, allowing us to examine whether relation knowledge remains accessible when the same senses are verbalised through glosses in different languages. We construct a dataset of 3,069 sense pairs, with each sense verbalised in English, Greek, Romanian, Turkish, and Japanese. Experiments with 17 LLMs in zero-shot and five-shot settings reveal generally poor performance. In each setting, only eight LLMs achieve a macro-averaged F1 score significantly above a random baseline, and only one (zero-shot) and two (five-shot) significantly outperform a neural baseline. In particular, LLMs often fail to generate bidirectionally consistent predictions for hypernymy and to make correct predictions for holonymy in either direction. Our results suggest limitations in current LLMs' semantic relation knowledge, both in identifying relations and in respecting asymmetry.

---


### 65. [KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization](https://arxiv.org/abs/2610.14448)

**<font color=#1a73e8>作者：</font>** Sihwan Park, Sung-Yub Kim, Doohyuk Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous rollout improves the efficiency of reinforcement learning with verifiable rewards (RLVR) by reducing under-utilization during long-tail generation. Sustained concurrency also concentrates context processing into fewer decode steps, increasing the KV workload per step. We characterize this \emph{KV concentration} and find that KV cache quantization delivers substantially greater acceleration than weight-only and weight-activation quantization in our matched-workload comparisons. However, INT4 KV rollout can degrade learning even with token-level truncated importance sampling (TIS). We propose \emph{KV4-RL}, which combines calibration-free INT4 KV quantization with selective INT8 protection of attention sinks and recent context. Protecting a bounded number of positions reduces sampler mismatch while retaining most of the speedup from INT4. Across 400 iterations of Qwen3-8B-Base GRPO training, KV4-RL achieves $1.80\times$ cumulative rollout speedup and $1.27\times$ cumulative full-iteration speedup over BF16 rollout, reaching $1.97\times$ rollout speedup over the final 50 iterations. Under a common BF16 evaluator, its final six-benchmark mean accuracy is within 0.5 percentage points of BF16-rollout training for both Qwen3-4B-Base and Qwen3-8B-Base.

---


### 66. [SecReason: Vulnerability Detection and In-Stream Self-Repair for LLM Code Generation](https://arxiv.org/abs/2610.14453)

**<font color=#1a73e8>作者：</font>** Ruidong Han, Zhensu Sun, Chengyan Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) may introduce security vulnerabilities into generated code, which can persist into production when verification focuses on functional correctness. Existing defenses act before, during, or after generation, but none inspects the code during generation. Security prompts and retrieved security knowledge act before any code exists, constrained decoding limits token choices but cannot guide repair, and post-hoc repair must regenerate the full response. Reasoning LLMs draft code early in their streamed chain of thought, and in this pre-delivery window the code exists only inside the reasoning stream. We present SecReason, an in-stream defense that monitors this window. Dual-track incremental scanning applies security rules, checking each statement as it is emitted and tracing dataflows across the accumulated code. When a security rule fires, SecReason interrupts generation, inserts an in-stream warning, and resumes decoding, so the model repairs the draft within the same reasoning trace without regenerating the full response. On tasks where unassisted generation introduces vulnerabilities, \system raises the share of runs delivering secure and functionally correct code from below 15\% to 72.8\%--98.1\% on \tool{CWEval} and \tool{SecCodeBench}. \system consumes fewer tokens than post-hoc repair, and when security rules misfire on secure code, it limits the functional regressions from false warnings.

---


### 67. [Evaluating Bias in Chinese Large Language Models across Tasks and Registers: Task Operationalization Effects and Irony Classification Risks](https://arxiv.org/abs/2610.14464)

**<font color=#1a73e8>作者：</font>** Mo Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In Chinese content governance, large language models are increasingly used to identify toxic and discriminatory expressions, yet both task operationalization and ironic expression can alter bias measurement readings. We conducted a preregistered multi-task behavioral audit of multiple Chinese large language models. In the content classification experiment, the core panel's classification error rate rose from 10.9% in the formal register to 23.5% in the yinyang (an echoic-irony register) version, a risk difference of +12.7 percentage points. (95% CI [+9.7, +15.7]). Inter-rater agreement was lower in the yinyang register (majority-vote kappa = 0.299), so the increase contains a component of label uncertainty propagation, but the direction of increase was consistent under both adjudicated and majority-vote reference standards. Explicit irony-aware prompts reduced the intervention panel's error rate by 9.6 percentage points. We operationalized the 29 shared proposition anchors into three task forms: social consensus estimation (Form A), high-stakes decision (Form B), and controlled association rating (Form C); independent manipulation checks found that all 58 A-C comparison units received unanimous agreement, whereas the low A-B convergence was confirmed by calibrated majority adjudication (87.8% supporting the minority judgment); on the irony-probe materials, the interactions of B and C relative to A were +0.577 and +1.121, respectively. Thus, when evaluating large language models for Chinese content governance, the effect of task operationalization on bias readings is an empirical question that requires data to answer, and safety evaluation should incorporate the ironic register as a test condition.

---


### 68. [RES-MR: Risk-Aware Reasoning for Explainable and Safe Medication Recommendation](https://arxiv.org/abs/2610.14474)

**<font color=#1a73e8>作者：</font>** Cong Wang, Jin Li, Shoujin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medication recommendations seek to deliver personalized drug combinations based on patients' clinical information, where ensuring transparent decision-making and personalized safety are of paramount importance. However, existing approaches predominantly operate as ``black boxes'', offering limited interpretability and hindering clinician trust. Furthermore, they typically rely on fixed, patient-agnostic safety constraints, neglecting the heterogeneity of risk tolerance across individuals, which poses significant risks to vulnerable populations. To address these gaps, we propose \textbf{RES-MR}, a novel Risk-aware Reasoning framework for Explainable and Safe Medication Recommendation using LLMs. RES-MR follows a two-stage training paradigm: (1) an explainable clinical reasoning distillation stage to elicit diagnostic capabilities by fine-tuning on synthesized reasoning trajectories, grounded in patient-specific knowledge from graph retrieval; and (2) a risk-aware policy optimization stage to dynamically balance therapeutic efficacy with personalized safety. This stage employs disentangled drug factors to construct patient-specific reference prototypes that capture desired therapeutic drug features and risk features to avoid. These prototypes enable risk boundary calibration and guide the model toward safe recommendations via reward shaping and clipping. Extensive experiments on benchmark datasets demonstrate that RES-MR significantly outperforms state-of-the-art baselines in terms of accuracy, safety, and explainability. Our code and data are available at: this https URL.

---


### 69. [EdgeLLM-Nano: Auditing Polar-Guided Key-Cache Compression and Consistency-Anchored Pruning on a 33.6 MB On-Device Language Model](https://arxiv.org/abs/2610.14475)

**<font color=#1a73e8>作者：</font>** S M Mahbub Murshed, Hayden Bright, Rezaul Karim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deploying language models (LMs) on the edge presents unique memory, latency, and power challenges absent in high-performance computing. KV-cache compression emerges as a promising approach to address these challenges. However, the effectiveness of current KV-cache compression methods has not been thoroughly examined on edge devices. Moreover, we show that existing evaluation methods do not always involve the KV-cache under test. We propose EdgeLLM-Nano, a measurement study of KV-cache compression using a nano-scale decoder-only LM (transformer) testbed that has 8.39M parameters, i.e., 33.6 MB, to enable end-to-end examination of each backend, seed, and power sample. Our results give a negative verdict for a polar-guided key-cache quantizer (round-to-nearest (RTN) control causes an order of magnitude less damage), as well as a consistency-anchored progressive weight pruner (one-shot magnitude-based pruning performs as well as, if not better). We also introduce Long-Context Decode Fidelity (LCDF) evaluation, a token-by-token examination of teacher-forced log-losses using the KV-cache under test. Unlike perplexity that gives the same 5.461 score to all methods, LCDF distinguishes different KV-cache compression backends thanks to its paired statistics across seeds and effect sizes. Our companion Raspberry Pi 5 measurement shows all compression backends we tested to be less energy-efficient per token compared to uncompressed FP16 inference. Except for KIVI that is close to lossless in terms of LCDF, our findings indicate KV-cache compression can be improved. LCDF offers a simple and effective way of shedding light on KV-cache compression methods, whose negative impacts have been overlooked by perplexity.

---


### 70. [Scale, Drivers, and Limits of Representational Alignment Across Large Language Models](https://arxiv.org/abs/2610.14476)

**<font color=#1a73e8>作者：</font>** Jialin Wu, Meenakshi Khosla  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Comparing large language models can reveal shared representational structure and systematic differences between them. However, aggregate similarity measures can obscure how agreement varies across geometric scales and which linguistic properties support it. We introduce two complementary methods to resolve where models agree and what supports that agreement. Standard representational similarity analysis (RSA) summarizes similarity across all stimulus pairs, potentially obscuring differences in alignment between nearby and distant inputs. Neighborhood-Weighted RSA (NW-RSA) addresses this limitation by weighting stimulus pairs according to their proximity in representational space, placing alignment from local neighborhoods to global geometry on a common scale. Counterfactual RSA (CF-RSA) tests which linguistic properties support alignment by comparing intact representations in one model with representations under controlled linguistic perturbations in another. Across diverse language models, we find strong agreement in coarse representational geometry but substantial divergence in local neighborhoods. Alignment is observed both across broadly sampled natural text and within linguistic equivalence classes that preserve particular aspects of meaning or structure. Counterfactual analyses reveal selective sensitivity: changes to logical scope reduce alignment substantially more than the tested changes to hierarchical syntax, event roles, or discourse structure. Alignment also decreases when sentence structure or lexical meaning is disrupted in word lists and jabberwocky sentences, suggesting that the regularities of natural language support stronger convergence. These findings refine claims of representational universality by showing that strong overall similarity need not imply agreement in how models represent finer linguistic distinctions.

---


### 71. [Optimize Once, Execute Fast: Latency-Aware Multi-Agent Workflow Learning for Recurrent Queries](https://arxiv.org/abs/2610.14481)

**<font color=#1a73e8>作者：</font>** Enpei Zhang, Feiyu Qu, Zheng Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large Language Model-based Multi-Agent Systems (LLM-based MAS) have shown remarkable success in solving complex tasks by coordinating specialized agents through multi-step workflows. To overcome the high cost and specificity of manually designed workflows, recent research has shifted toward learning them automatically. However, a key limitation remains: while agent calls introduce significant latency due to model inference time and service congestion, most automated methods optimize solely for downstream performance, ignoring execution time (makespan). This issue is amplified when workflows are reused across recurring queries, making latency accumulate over time. This limits deployment in recurrent applications such as AI customer support and AI cloud troubleshooting, where users expect fast responses. To bridge this gap, we introduce a new problem, termed latency-aware workflow generation, where the objective is to minimize workflow makespan while aiming to retain downstream performance. We propose LAWA (Latency-Aware Workflow optimizAtion), a novel framework that reduces makespan via theoretically grounded graph edits targeting critical-path bottlenecks. By unifying a graph generator with this graph-editing procedure, LAWA supports both de novo workflow generation and refinement of existing ones. Empirical results across seven benchmarks demonstrate that LAWA significantly reduces makespan while achieving competitive task performance, supporting efficient reuse of multi-agent workflows for recurrent queries.

---


### 72. [Names Are Not Objects: Object-Bound Confinement for Compromised AI Coding Agents](https://arxiv.org/abs/2610.14488)

**<font color=#1a73e8>作者：</font>** Daniel Commey  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents read repositories and web pages that anyone can write, and then act with their user's authority. Prompt-injection defenses make it less likely that the model is steered but do not prevent it, so the system around the model must contain an agent that is already compromised. Many exploits against deployed coding agents share one cause: a check approves a name, such as a path, an argument vector, or a directory, and a later step maps that name to a different object: the file behind a symlink, the behavior an option selects, or a repository that git discovers on its own. We present Zero-Trust Agent Cells (ZTAC). A cell runs the agent in a kernel sandbox whose only route to files, programs, and the network is a socket to a broker. The broker resolves each request to the object it will act on, decides on that object, and checks at use that it is acting on the object it authorized. Programs that the broker starts run in a sandbox compiled from the same policy, and approvals are bound to the resolved object and can be used once. Our macOS prototype has 3.2k lines of trusted Rust code, excluding dependencies. We evaluate it against 74 attacks with ground-truth oracles, including replays of 10 publicly disclosed incidents. A tool allowlist loses 66 of them, and an allowlist combined with the kind of command sandbox that deployed agents use loses 56. ZTAC loses 2, both of which encode a secret into traffic to an allowed endpoint, and holds 14 for review. It completes 43 of 46 benign operations, with 8 approval prompts, and 4 of 7 workflows. A no-op brokered request has a median latency of 4.0 ms, and the spawned programs we measured take 8.5 ms to 18.4 ms longer than without ZTAC.

---


### 73. [Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos](https://arxiv.org/abs/2610.14495)

**<font color=#1a73e8>作者：</font>** Wei Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explainer videos -- a worked geometry problem, why the sky is blue, how a dynasty fell -- are usually one more target for pixel video generation. We argue they are a different kind of artifact: a program (script, storyboard and per-frame animation code) that a deterministic renderer turns into frames. A program can be read, diffed, tested and audited; pixels can only be watched. Reels-RSI is an open-source reel director for any agent harness; its self-improvement happens at the program level rather than in weights or prompts. Every revision pass is logged with a code snapshot; a retrospective pairs each check finding with the diff that fixed it and proposes lessons; a lesson that a static check can catch is compiled into a rule with a must-fail and a must-pass example, so the memory is unit-tested; and a rule learned today runs over everything made before it. A bounded, benchmark-gated step lets an agent rewrite the director's playbook, kept only when blind pairwise judgments on held-out topics prefer it; nothing enters memory without a human decision. Across 111 reels -- a field study, two playbook evolutions, a 2x2 memory ablation, a weaker director, a 48-reel learning curve and a judge-reliability study -- we find that the rule learned in the field caught four latent defects in frames authored before it existed and none after; that rules are an audit for a strong director (eight unguarded reels, no violation) and a guard for a weaker one (thirty violations unguarded versus five); that lessons shorten revision loops but do not compound or move the judge; and that the first rewrite's 11--1 verdict was a position bias in our vote design (judges pick the second-shown reel 62--81% of the time), masking scripts that traded thirteen facts for craft. We document four failure modes of the preference signal, which check caught each, and the fixes. Code, rules, lessons and data are public.

---


### 74. [Rethinking Activation Functions: Reducing Bias Can Improve Learning](https://arxiv.org/abs/2610.14500)

**<font color=#1a73e8>作者：</font>** Zirui Peng, Heyi Zheng, Ziming Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many widely used activation functions, including ReLU, GELU, Swish, and Sigmoid, produce predominantly positive outputs, resulting in a nonzero post-activation mean that we term activation bias. Despite its ubiquity, the effect of activation bias on learning dynamics remains poorly understood. Using controlled models, we show that activation bias accelerates initial loss reduction but is accompanied by overshooting, non-smooth trajectories, and a steeper loss landscape. This early advantage also coincides with the model's use of task-relevant information encoded in the activation bias component. In contrast, reducing activation bias slows initial learning but ultimately yields a lower final loss. Experiments on larger vision and language models exhibit a similar pattern: smaller activation bias is associated with better late-stage performance. Thus, this seemingly minor property can substantially redirect learning and warrants explicit consideration in future activation function design.

---


### 75. [Query-Adaptive Neuron Steering for LLMs](https://arxiv.org/abs/2610.14519)

**<font color=#1a73e8>作者：</font>** Yanxi Pan, Jingwen Wu, Yan Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effectively eliciting the capabilities of large language models (LLMs) at inference time remains an important challenge. Existing studies address this challenge through context engineering, which shapes user queries, or fixed steering, which directly intervenes in model computation. However, predefined contexts and fixed intervention strategies may not adequately accommodate the diverse knowledge and reasoning requirements of individual queries. This raises a natural question: Can internal steering in LLMs be made query-adaptive? In this work, we investigate whether query-induced internal activations can guide adaptive steering in LLMs. Our pilot studies reveal subject- and layer-dependent neuron activation patterns and show that amplifying subject-relevant neurons can improve model performance. Based on these findings, we propose Q-NeuS, a query-adaptive neuron steering framework that dynamically determines which neurons to modulate and by how much for each input. Specifically, Q-NeuS constructs a compact subject-guided candidate neuron space and employs a lightweight Query-Adaptive Gate to generate neuron-wise modulation coefficients. To learn effective intervention strategies, we introduce Neu-GRPO, which adapts group-relative optimization to train the Query-Adaptive Gate using the relative performance of multiple neuron intervention configurations. The base LLM remains frozen throughout training and inference, and no task or subject labels are required at inference time. Extensive experiments across multiple LLMs and benchmarks demonstrate that Q-NeuS consistently improves model performance and exhibits broad applicability across model scales and strong cross-benchmark transferability.

---


### 76. [LongHisDoc: A Comprehensive Benchmark for Chinese Long Historical Document Understanding](https://arxiv.org/abs/2610.14531)

**<font color=#1a73e8>作者：</font>** Zeyu Shan, Yongxin Shi, Shihang Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chinese historical documents are invaluable cultural treasures, but their complexity poses significant comprehension challenges for non-specialists. Despite the success of Large Language Models (LLMs) and Large Vision-Language Models (LVLMs) in modern document tasks, their capabilities in Long (full-book) Historical Document understanding remain largely unexplored. To bridge this gap, we introduce LongHisDoc, the first benchmark tailored for long historical document understanding. LongHisDoc comprises 1,012 expert-annotated QA pairs derived from 101 PDF documents, with an average of 85.1 pages and 42,776.4 tokens per document. It spans 10 categories and features four QA types: single-page, cross-page, multi-hop, and unanswerable. Answering these questions requires integrating multimodal evidence from text, layout, and visual elements. Our evaluation reveals that the top-performing LVLM and LLM achieve only 62.9% and 69.9% accuracy, respectively, highlighting a substantial performance gap. Furthermore, we assess various modal retrievers and the end-to-end RAG performance to provide references for Retrieval-Augmented Generation (RAG) systems. We believe that LongHisDoc serves as a comprehensive benchmark to catalyze future research in full-book historical document understanding. The benchmark and evaluation code are available at this https URL and this https URL.

---


### 77. [FrameFold: Response-Guided KV Cache Consolidation for Autoregressive Long Video Generation](https://arxiv.org/abs/2610.14568)

**<font color=#1a73e8>作者：</font>** Muyu Liu, Mingming Liu, Hong Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In autoregressive video generation, retaining all historical key-value (KV) states increases memory usage and per-step attention costs as videos grow longer. A fixed cache budget bounds these costs but raises the challenge of preserving historical content that supports consistent, high-quality generation. Existing methods control cache size through history selection or consolidation, yet deciding what to retain and how to limit the loss of useful content remains a shared challenge. Our analysis shows that spatial queries depend on different historical content and that higher current attention coverage does not necessarily yield better long-video quality. We introduce FrameFold, a training-free KV cache consolidation method that compares the content retrieved by the same recent historical queries before and after merging to guide both representative construction and merge selection. Exploiting temporal redundancy between adjacent historical entries, FrameFold merges their KV states into shared representatives while retaining complete spatial grids. It fits value-merging coefficients in closed form by matching conditional attention responses, then selects the merge with the lowest remaining response distortion. Under matched KV cache budgets, experiments on Self Forcing and Causal Forcing at 30 and 60 seconds and on LongLive at 120 seconds demonstrate improved consistency and visual quality. Continuous eight-minute Self Forcing rollouts further show less quality degradation than the baselines.

---


### 78. [PsyMemBehav: Psychology-Informed and Memory-Grounded Two-Level Identity-to-Action Reasoning for Social-Media Behavior Simulation](https://arxiv.org/abs/2610.14570)

**<font color=#1a73e8>作者：</font>** Wenji Zhang, Xilong Cheng, Yunxiao Qin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) support social simulation, but faithfully reproducing real users requires grounding both structured platform decisions and language in sparse, noisy behavioral evidence. We introduce PsyMemBehav, which maps psychology-informed profiles and retrieved memories to target-first platform behavior through two-level identity-to-action reasoning. To support this approach with comprehensive behavioral traces, we construct a dataset PsyMemBehav-bench from 5.57M observed behaviors of 5,862 real users (approximately 950 per user) across Reddit, Bluesky, and Twitter. Each recorded engagement is modeled as target selection followed by Comment, Like, or Repost and optional response generation. PsyMemBehav combines 41-dimensional user descriptors, top-5 BM25 memories, reverse-CoT supervision, and rubric-guided DPO over complete reasoning-action trajectories. Experiments show that PsyMemBehav 27B ranks first in 11 of 12 reported individual-level metrics, improving average response quality over GPT-5.4 from 54.28 to 59.68 (9.95% relative), and obtains the lowest group-level MAE (0.081) and MSE (0.009) among simulated systems. These results support evidence-grounded user modeling for observed-thread continuation; the benchmark remains conditional on recorded engagement and does not model no-action decisions.

---


### 79. [Reward-Aligned Distillation](https://arxiv.org/abs/2610.14572)

**<font color=#1a73e8>作者：</font>** Yilan Chen, Zian Su, Manish Prajapat 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards improves the reasoning capabilities of large language models, but remains computationally expensive and sample inefficient. On-policy distillation (OPD) provides dense token-level supervision from a stronger teacher, yet standard OPD distills every token regardless of whether the teacher's preference actually improves task reward. Existing token-selection methods rely on proxies such as uncertainty or teacher--student divergence, which need not identify reward-improving supervision. We introduce Reward-Aligned Distillation (RAD), a bilevel framework that weights distillation signals based on their predicted effect on the student's post-update reward. RAD differentiates through a temporary optimizer step to score each token's supervision, then updates the token weights by projected ascent from the initial token weights. The resulting weights can strengthen, suppress, or reverse individual distillation-gradient contributions. At a matched training-response budget, RAD improves mean accuracy on six competition-math benchmarks over the strongest baselines by 6.5 percentage points for Qwen3-1.7B (non-thinking) and 2.5 points for Qwen3-4B-Instruct-2507. RAD-Simple, a simplified variant, achieves comparable math accuracy at the same training-response budget. On LiveCodeBench-v6, RAD reaches 54.69\% and 58.67\% pass@1 with Qwen3-1.7B (non-thinking) and OLMo3-7B-Instruct, respectively, exceeding the strongest baselines by 8.7 and 6.4 points. These results support reward-guided weighting of teacher supervision across model families and tasks.

---


### 80. [CB-Agent: Concept-Based In-Context Learning for Sequential Action Selection](https://arxiv.org/abs/2610.14574)

**<font color=#1a73e8>作者：</font>** Qingyue Zhang, Huaze Tang, Minyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) allows large language models to use demonstrations without updating their parameters. For interactive agents, demonstrations are trajectories of reasoning, actions, and observations that illustrate how to complete a task. Reusing demonstrations in new situations is challenging: directly inputting full trajectories consumes limited prompt space and constrains the overall effectiveness, while natural-language summaries require the agent to translate general guidance into specific action choices. Therefore, we study whether expert action choices can directly supervise a reusable scoring rule. We propose CB-Agent, which extends concept-based ICL to sequential action selection. We extract environment-action decisions from expert trajectories and fit a concept vector by maximum likelihood to model the conditional distribution over candidate actions given the context. This model combines the concept with frozen language-model features and priors. During ReAct interaction, the agent uses this distribution to select environment actions without including demonstrations in the action-scoring context. Across TextWorld, ALFWorld, and ScienceWorld, CB-Agent achieves the highest cross-benchmark average among the evaluated methods at all three tested model sizes and ranks first on TextWorld and ScienceWorld at each size. ALFWorld experiments support the learned concept's contribution beyond prior-only scoring and show further gains when combined with Reflexion. Code is available at this https URL.

---


### 81. [Iterate on an LLM, Serve on an SLM](https://arxiv.org/abs/2610.14576)

**<font color=#1a73e8>作者：</font>** Keegan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As frontier LLMs gain more capabilities, the cost to run them also goes up. At the same time, small language models (SLMs) also gain more capabilities but have largely been able to keep their cost stable, offering 5-40 times cheaper inference for the narrow, repetitive subtasks that agents decompose work into. However, the standing limiting factor is getting the correct behavior out of a small model in a fast, efficient, and economical way. Unfortunately, in most cases, zero-shot small models fail narrow production tasks. Furthermore, retraining one every time the behavior changes is too slow to iterate on. We propose doing both in sequence. First, develop the desired behavior in prompt space, on a frontier model, with immediate feedback from live traffic. Then, once the behavior converges, distill the recorded production behavior (not synthetic imitations of it) into an SLM through supervised fine-tuning (SFT). We show a proper use case of this method through a scheduling agent for home-care agencies that fans out a single yes/no safety decision per caregiver-shift pair on GPT-5.4-nano. A LoRA-tuned Qwen3-8B trained on 11.6k recorded production decisions reaches 0.913 agreement, while the teacher (GPT-5.4-nano), re-run on its own recorded prompts, agrees with itself only 72.7% of the time, pointing to the fact that the SLM may also be more consistent. Furthermore, when the two disagreed, a blinded professional scheduler sided with the student 48-29. Finally, we find that the SLM has approximately 2.5 times lower median latency and is a fraction of the cost. We believe this lifecycle of quick building, live feedback, and cheap inference is a blueprint for others building similar systems.

---


### 82. [Uniform Information Density-Based Preference Optimization](https://arxiv.org/abs/2610.14578)

**<font color=#1a73e8>作者：</font>** Yongyuan Li, Yang Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To enable large language models to generate outputs that align with human preferences, optimization algorithms based on the comparison between chosen and rejected output pairs have been developed and been proven effective. Some recent endeavors have utilized certain linguistically-derived assumptions about the preference pairs to guide the design of more precise optimization directions. However, human preferences are complex and hard to measure by simplistic criteria, and it is important to incorporate broader and more sophisticated insights about preferred vs. not-preferred language. In this study, we adopt a well-established psycholinguistic theory, Uniform Information Density, to develop a novel preference optimization algorithm, UIDPO. The basic assumption is that humans prefer to produce language in which information is uniformly distributed, because uniformity induces less cognitive processing effort. To implement this idea into the algorithm, we derive a compound metric for information uniformity by combining the global standard deviation and the local second-order difference, and integrate it to the objective of preference optimization. We compare UIDPO with SimPO, a previous state-of-the-art method, obtaining comparable and sometimes better performance on AlpacaEval2, ArenaHard, and MT-Bench. Additional linguistic analysis on complement clauses also shows that UIDPO can better reflect the tendencies of keeping information uniform in natural language than baselines. Our results show that the subtle human preference over the information rate in language is a helpful source for achieving better human alignment for LLMs. The code repository is published here: this https URL.

---


### 83. [Attribute-Centric Vision-Language Alignment for Fine-Grained Gait Understanding](https://arxiv.org/abs/2610.14589)

**<font color=#1a73e8>作者：</font>** Saihui Hou, Chenye Wang, Wenpeng Lang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Walking sequences reveal human-interpretable attributes related to body structure, posture, and motion. Gait attribute recognition provides a concrete route to fine-grained gait understanding by predicting these attributes. However, existing benchmarks provide limited fine-grained annotations, while classifier-based gait attribute recognition methods typically represent candidate classes through learned output weights rather than directly matching visual evidence with textual class representations. To address the annotation gap, we present RA-GAR, a large-scale, richly annotated multimodal benchmark for gait attribute recognition, containing 1,001 subjects, 242,729 walking sequences, and annotations for 15 static and motion gait attributes. We further propose Gait-VL, an attribute-centric vision-language alignment framework that recognizes gait attributes by matching attribute-specific multi-frame visual evidence with textual class prototypes. On the visual side, attribute-specific learnable queries aggregate RGB features across spatial locations and frames into per-attribute visual embeddings. On the language side, diverse descriptions expanded by a large language model are combined with context about relevant body regions to construct textual class prototypes. Beyond attribute recognition, we evaluate the transferability of the attribute-pretrained visual encoder by using it to replace generic upstream large vision models in identityoriented gait recognition pipelines; attribute pre-training uses no identity classification or metric-learning objectives. Experiments demonstrate state-of-the-art attribute recognition performance on RA-GAR and consistent improvements in downstream identity recognition across multiple pipelines and benchmarks, supporting the effectiveness and transferability of attribute-centric gait representation learning.

---


### 84. [Decoupling Knowledge Forgetting and Refusal Learning in MLLM Unlearning](https://arxiv.org/abs/2610.14605)

**<font color=#1a73e8>作者：</font>** Haodong Chen, Shengtao Wen, Dong Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current evaluations of multimodal unlearning typically focus on whether a model stops outputting target information. This surface-level criterion, however, masks two critical failure modes. First, knowledge suppression techniques often induce confabulation, leading the model to hallucinate facts about the unlearned subject. Second, refusal training merely alters observable behavior without erasing the underlying knowledge; such models might decline open queries but still identify correct answers under multiple-choice probing. To overcome these limitations, we propose Forget-Aware Self-Distillation (FASD). This method is designed to achieve honest ignorance, a state where the model genuinely loses the target knowledge and learns to acknowledge its absence. FASD separates these goals into two complementary channels. The behavior channel distills appropriate refusals from an ignorance-prompted copy of the model itself. Crucially, target tokens are masked from the teacher distribution to avoid accidentally reteaching the forgotten concepts. Simultaneously, the knowledge channel directly suppresses ground-truth answer spans independently of the model's generated responses. Experiments demonstrate that FASD successfully unlearns target knowledge, prevents information leakage in open-ended tasks, and preserves performance on retained data. The resulting model not only forgets the specified information but accurately recognizes the boundaries of its own knowledge. Code and data will be released upon publication.

---


### 85. [EviScene: Beyond "Is It AI?" for Agentic Image Factuality Assessment](https://arxiv.org/abs/2610.14609)

**<font color=#1a73e8>作者：</font>** ZiAn Wang, Ruiqi Liu, Zhengbo Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Determining whether an image is AI-generated does not establish whether the situation it depicts is factually supported. We formulate Image Factuality Assessment: given an image and a generic verification instruction, a system returns a supported or refuted verdict with an evidence-grounded explanation. Without a supplied textual claim, the system must progressively refine factual questions during investigation and align external evidence with the specific situation depicted. We introduce EviLens, an expert-reviewed benchmark of 10,174 supported and refuted images from controlled construction and web collection, covering twelve factual error types and evaluating both verdict accuracy and evidence sufficiency. We develop EviScene, a multimodal ReAct agent that interleaves visual inspection, external retrieval, and evidence analysis, using new findings to refine its questions and revisit relevant image details. We train a compact policy with supervised fine-tuning on reviewed teacher trajectories, followed by privileged on-policy self-distillation applied to verified decisions from the policy's own investigations. On the 1,527-image test set, the trained Qwen3.5-9B agent achieves 79.05% balanced accuracy and a Strict Evidence Sufficiency Rate (SESR) of 52.26%, improving over the same-backbone base agent by 6.71 and 9.37 percentage points, respectively. Its SESR is the highest among the evaluated this http URL, models, and data will be released at this https URL and this https URL.

---


### 86. [LLM-Augmented Bayesian Optimization with Adaptive Policies for Chiplet Design Space Exploration](https://arxiv.org/abs/2610.14612)

**<font color=#1a73e8>作者：</font>** Hang Liu, Zhengfei Chen, Zhengrui Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chiplet technology is a key approach for extending Moore's Law. However, its design process is constrained by two primary challenges: the scarcity of early-stage platforms for rapidly evaluating chiplet-based heterogeneous systems, and the complex relationships between design parameters and optimization metrics. To address these challenges, we propose a synergistic framework that integrates a Large Language Model (LLM) with Bayesian Optimization (BO), enabling architectural-level simulation and automated optimization for the 2.5D/3D CPU-GPU heterogeneous chiplets. We extend the open-source chiplet simulator to evaluate 3D designs by supporting graph topologies. Further, to enhance the exploration efficiency of BO, we introduce an LLM that generates high-quality policies to guide the optimization process, enabled by our proposed adaptive directional policy reasoning (ADPR) and an exploration gain-aware fine-tuning method. Finally, we use the policy-guided BO to perform an automated and efficient exploration of the complex chiplet design space. Experiments on 2.5D and 3D chiplet reveal that our framework improves design space exploration efficiency.

---


### 87. [From Existing Methods to New Research Ideas: Two Perspectives on Recursive Self-Improvement](https://arxiv.org/abs/2610.14625)

**<font color=#1a73e8>作者：</font>** Leijun Zhou, Yanke Yu, Zhihao Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) offers a route to AI systems that participate in their own continued development. Recent methods allow language agents to retain changes to their parameters, memory, skills, and code for subsequent execution and improvement. We examine how these methods can inform new research ideas through two complementary perspectives. First, we introduce a unified taxonomy with nine design dimensions organized into four groups: update targets, update organization, update schedule and scope, feedback and selection. This taxonomy places existing methods in a shared design space, where examining individual dimensions and their interactions can inspire new research ideas. Second, we examine how existing RSI methods draw on traditional deep learning, for example through optimization, regularization, data augmentation, continual learning, and adversarial learning. We develop further ideas by examining more specific learning mechanisms and drawing on evolutionary computation. We also review how existing benchmarks assess self-improvement under online, offline, and offline-to-online settings. Together, these perspectives help researchers develop new RSI research ideas from existing designs and learning mechanisms. RSI papers and resources are available at this https URL.

---


### 88. [TagBO: LLM-Driven Task-Aware Graph Bayesian Optimization for Scientific Discovery](https://arxiv.org/abs/2610.14626)

**<font color=#1a73e8>作者：</font>** Xinzhe Yuan, Zimu Zeng, Zhuo Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-variable optimization in scientific discovery often requires exploring large combinatorial spaces under costly experimental evaluations, making sample?efficient Bayesian optimization (BO) essential. However, existing BO methods typ?ically rely on structural descriptors to define similarity among categorical variables, implicitly assuming that structural similarity reflects similarity in task performance. In scientific optimization, this assumption is often violated, leading to surrogate representations that are poorly aligned with the optimization objective. To address this limitation, we propose TagBO (Task-aware Graph Bayesian Optimization), a method that integrates LLM-derived relational priors with descriptor-based struc?tural information for mixed-variable Bayesian optimization. Rather than directly using LLM outputs as predictive scores, TagBO treats LLM outputs as a potentially noisy source of task-aware relational priors and extracts coarse ordinal relational signals from LLM reasoning to construct task-aware similarity structures for scien?tific optimization. TagBO then performs constrained Gaussian process Bayesian optimization over the resulting joint discrete-continuous representation space. Ex?periments on diverse chemistry and materials formulation tasks demonstrate that TagBO consistently improves sample efficiency under fixed evaluation budgets across LLMs of varying capabilities.

---


### 89. [PVFH-Bench: Benchmarking Premise-Induced Visual Fixation Hallucinations in Vision-Language Models](https://arxiv.org/abs/2610.14635)

**<font color=#1a73e8>作者：</font>** Xinhao Wang, Junbo Cui, Zhenghao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved remarkable progress across a wide range of multimodal tasks. However, object hallucination remains a persistent challenge, undermining model reliability in applications such as visual question answering, embodied agents, and human-AI decision support systems. In this paper, inspired by cognitive science studies on perceptual bias, we investigate a new failure mode termed Premise-Induced Visual Fixation Hallucination (PVFH). Specifically, PVFH refers to a premise-induced reasoning error in which models become anchored to visually confusable evidence, accept a false textual premise, and subsequently generate responses about an absent yet visually plausible object. To systematically study this phenomenon, we introduce PVFH-Bench, a benchmark that automatically constructs visually confusable but absent targets and pairs the core hallucination setting with diagnostic subsets to trace how models move from object recognition to Premise-Induced Visual Fixation Hallucination. Experimental results on 10 state-of-the-art LVLMs demonstrate that all evaluated models are highly vulnerable to Premise-Induced Visual Fixation Hallucination. Moreover, we find that explicit chain-of-thought reasoning can further exacerbate this failure mode by encouraging models to overinterpret weak visual cues as supporting evidence for hallucinated objects.

---


### 90. [Shaping Latent Mixture-of-Experts: From Expert Geometry to Layerwise Capacity Allocation](https://arxiv.org/abs/2610.14644)

**<font color=#1a73e8>作者：</font>** Yaoxiang Wang, Kai Zhang, Ruobing Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-grained mixture-of-experts (MoE) models commonly increase expert count by narrowing each expert, treating expert shape as a by-product of routing granularity. LatentMoE moves expert computation into a lower-dimensional space, exposing the input dimension and intermediate width of each expert as explicit design choices. We show that an expert's local Jacobian rank is jointly bounded by these two dimensions, and that balancing them maximizes the rank ceiling at fixed per-expert parameters. Controlled shape sweeps across model scales and routing granularities consistently favor near-square experts. We further use layerwise intrinsic dimension (ID) to guide capacity allocation across depth, co-varying the number and shape of experts while keeping per-layer parameter count, activated FLOPs, and communication volume constant. Compared with layer-homogeneous baselines, our ID-guided allocation achieves lower validation loss and stronger downstream performance. These results establish expert shape and layerwise allocation as practical design axes for MoEs.

---


### 91. [TAG: Calibrating SAM3 for Universal Image Segmentation without Dense Supervision](https://arxiv.org/abs/2610.14651)

**<font color=#1a73e8>作者：</font>** Hao Zhu, Heyu Sun, Shuo Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The recent Segment Anything Model 3 (SAM3) extends powerful promptable segmentation from spatial cues to concepts, raising the prospect of a single foundation model for universal image segmentation. However, this promise often fails to translate into reliable performance on downstream segmentation tasks. In this work, we empirically identify concept recognition, rather than mask quality, as the primary bottleneck: SAM3 accurately delineates the objects it recognizes yet struggles to robustly determine which concepts are present. Driven by this, we present \textit{\underline{T}ext \underline{A}nchor re-\underline{G}rounding (\TAG{})}, a simple yet effective framework that rectifies the concept recognition of SAM3 on the target domain without dense annotations. Specifically, \TAG{} introduces an \textit{Anchor Residual Pathway} comprising image-conditioned, low-rank adapters to re-ground text anchors in the target distribution and modulate subsequent text-conditioned interactions. Guided solely by image-level category labels, \TAG{} jointly optimizes binary cross-entropy with \textit{Soft Boundary Ranking} objectives to calibrate presence confidence and distinguish present concepts from confusable negatives. Building upon this, we devise \textit{Confidence-Weighted Distillation} to couple rich semantic context of a multimodal large language model with fine-grained spatial priors of SAM3, thereby achieving effective calibration in the absence of manual annotations. Extensive experiments demonstrate that \TAG{} unlocks SAM3's segmentation potential with only 3.1M trainable parameters, achieving impressive performance across diverse scenarios, and notably, even surpassing leading mask-supervised methods on several metrics. \href{this https URL}{Our code will be publicly available at GitHub \faGithub}.

---


### 92. [SPARE: Shared Perception and Adaptive Retrieval of Evidence for Streaming Video Understanding](https://arxiv.org/abs/2610.14671)

**<font color=#1a73e8>作者：</font>** Senbin Xu, Zijun Zhang, Xinhua Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires answering questions from the observed video, with evidence drawn from recent observations or earlier events. Historical context can improve recall but may interfere with judgments based on recent frames. Its usefulness depends on both when it is introduced and which clips are selected, while relevance alone does not guarantee sufficient evidence for an answer. We propose SPARE, a framework that combines adaptive historical retrieval with visual encoder sharing. A lightweight gate predicts whether recent observations provide sufficient evidence to answer the question. When additional evidence is predicted to be necessary, a multimodal embedding model retrieves relevant historical clips to supplement the current context. LoRA instruction tuning trains the understanding model to use recent observations and retrieved history jointly and abstain when the evidence remains insufficient. To reduce redundant visual parameters, the understanding and retrieval branches share a visual encoder while retaining separate language backbones. Four linear adapters align the shared features with the retrieval model through distillation at the visual token and final retrieval embedding levels. With visual-only inputs, SPARE achieves 77.78% on the evaluated Real-time and Backward task groups of OVO-Bench and 73.31% on StreamingBench. Compared with Qwen3-VL-8B-Instruct evaluated at 2 fps, SPARE improves accuracy by 20.68 percentage points on OVO-Bench and 14.15 percentage points on StreamingBench.

---


### 93. [HumanPhys: A Human-Centric Physical-World Perception Benchmark for Real-World Visual Reasoning](https://arxiv.org/abs/2610.14679)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Enzhi Zhou, Junan Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce HumanPhys, a human-centric benchmark for real-world physical perception, and a training corpus emitted by the same pipeline. Each question targets a physically grounded quantity related to people, including depth, inter-person distance, gaze angle, displacement, velocity, heading-step trajectory, blink count, and contact-deformation strength. The rendered probes additionally test illumination inference from body and face cues and camera ego-motion, both with and without a person in the frame. All labels are derived programmatically from sensor calibration, source metadata, or renderer state, rather than written by annotators or produced by estimators on the benchmark frames. HumanPhys systematically probes six dimensions of human-centric physical perception: spatial state, kinematics, blink events, deformation, illumination, and camera pose. To the best of our knowledge, no existing MLLM benchmark-and-training corpus jointly supervises this set of human-centered physical quantities under direct metadata- or renderer-derived labels. The six dimensions appear only partially dissociable across the tested MLLMs. We benchmark a range of open- and closed-source MLLMs on HumanPhys and find that all six capability dimensions remain challenging for current models. We hope HumanPhys will support future research on multimodal systems that perceive and reason about people in the physical world.

---


### 94. [Triage-PiEvo: Evidence Admission for Principle-Evolving Scientific Agents](https://arxiv.org/abs/2610.14683)

**<font color=#1a73e8>作者：</font>** Peize Li, Yingming Pu, Xingguo Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based AI Scientists advance scientific discovery, yet they suffer from inefficiencies due to noisy observations. Existing principle-evolving agents act on every anomaly, leaving its source unresolved: a new mechanism or an evaluation artifact, so invalid revisions bias evolution. To address this, we formulate revision as evidence admission: anomalies steer search immediately, but only independently verified evidence may rewrite persistent principles, and contradicted principles are retracted. We realize this in TRIAGE-PIEVO , which pairs an anomaly-responsive search portfolio with a staged verification gate that alone controls what enters principle state. Across four scientific tasks with three backbones, TRIAGE-PIEVO (1) attains the highest average solution quality with +7.5%~11.8% over the strongest baseline per backbone, matching the strongest baseline's full-budget quality with one-third of the evaluation budget on Qwen3-235B; and additional stress tests and cross-harness deployment demonstrate that (2) in constructed stress tests, it admits none of the corrupted, hidden-source, or exploit evidence that ungated variants admit, while missing no planted mechanism, and (3) plugged unchanged into three external research harnesses, it cuts false evidence admissions by over 60% and raises verified scores by 31%~43%.

---


### 95. [Accelerating Cross-Model LLM Inference via Attention Map Reuse](https://arxiv.org/abs/2610.14688)

**<font color=#1a73e8>作者：</font>** Zhan Jin, Yuze Luo, Bin Cui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-augmented data workflows often involve multiple heterogeneous models operating over substantial shared context, such as schemas, tool specifications, interaction history, and intermediate results. Although prefix caching can reduce prefilling overhead, existing approaches are largely limited to reuse within the same model because KV states are tightly coupled to model-specific architectures. We present MapFlow, a system for efficient heterogeneous LLM serving via cross-model attention map reuse. Instead of reusing KV states, MapFlow reuses attention maps, which capture token dependency patterns and are more transferable across models. To enable efficient and accurate reuse, we combine partial recomputation with lightweight linear translation across layers and heads. To make attention reuse practical for long contexts, we further introduce block-level sparse compression and a fused retrieval kernel. Experiments show that MapFlow reduces prefilling latency and improves end-to-end serving efficiency while preserving generation quality across heterogeneous model pairs and multi-turn routing workloads. These results suggest that attention maps provide an effective reusable state for heterogeneous LLM serving, especially in prefix-heavy data workflows. Our code is available: this https URL.

---


### 96. [Lingdan-V2: Large language models for clinically grounded reasoning in traditional Chinese medicine](https://arxiv.org/abs/2610.14705)

**<font color=#1a73e8>作者：</font>** Rui Hua, Yu Wei, Ziri Jin 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have advanced medical reasoning, but clinically grounded reasoning in traditional Chinese medicine (TCM) remains challenging because prescription decisions require integrating domain knowledge, syndrome differentiation, treatment principles, herbal prescription composition, and dosage determination. We develop a TCM language model family comprising models with 4 billion, 8 billion, and 14 billion parameters. The artificial intelligence contribution is a staged clinical alignment framework integrating large scale continued pretraining on TCM and clinical records, complementary reasoning supervision, and prescription-centered reinforcement learning (RL). We further formulate herbal prescription generation as a structured RL problem with prescription-level feedback, enabling direct optimization of clinical decision outputs beyond knowledge reproduction and generic instruction following. The engineering application is TCM clinical decision support, particularly herbal prescription recommendation. We evaluate the models on a public benchmark containing 25,620 expert-verified items across 13 TCM knowledge and clinical reasoning tasks and on a private retrospective dataset of 4,348 spleen and stomach disease prescription cases. The 14 billion parameter reinforcement aligned model achieves a prescription generation F1 of 37.0 on the public benchmark, compared with 32.3 for DeepSeek-R1 with 671 billion total parameters, and a herb-level F1 of 52.8 on the clinical dataset with improved dosage agreement. Reinforcement post-training consistently improves prescription recommendation across all scales, while physician-source analysis shows that expert heterogeneity affects reward stability. These findings demonstrate a scalable pathway from domain grounding and reasoning supervision to clinically oriented prescription decision support.

---


### 97. [How to Build a Benchmark That Actually Measures Taste](https://arxiv.org/abs/2610.14707)

**<font color=#1a73e8>作者：</font>** Xiaofan Wu, Xi Zeng, Miaoxia Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Expert-aligned "taste" benchmarks should reward craft judgment, not the ability to game the test. We introduce TasteBench, a pairwise good-vs-bad benchmark across visual, brand, book, and tech items under a frozen rubric with expert-only gold (panel n>=3; percent agreement >=0.60 primary gate; weak engagement labels train/analysis-only), together with a control protocol that separates craft judgment from test-gaming. Applying the protocol to a Round-1 pilot (primary_human_expert; three biological human experts; n=250 pairs) surfaces and quantifies three validity threats: two construction artifacts that inflate the trivial-baseline layer, and a difficulty ceiling that inflates every score. (1) Position: the preferred item is slot A with probability 0.956, so an always_item_a policy scores 0.956 (fair chance 0.5). (2) Lexical leakage: a filename token cue scores 0.912. (3) Difficulty ceiling: craft domains show near-ceiling human agreement (book/brand/tech 1.0), and even under A/B randomization (eval_assignment_seed7; gold_side_A ~0.47) all five VLM cards reach 1.0 on craft, with only visual separating (~0.84-0.91; a post-hoc hard subset, n=107, leaves craft at 1.0). The protocol (expert-only gold, a weak-label firewall, side randomization at construction, filename scrubbing, and hard filters) makes each artifact measurable and, for the two construction artifacts, correctable; we release a reference eval harness and a side-randomization tool, and show the tool removes the position skew (0.916 to 0.495/0.505). The result is a calibrated view of what the benchmark does and does not yet measure: position and leakage are fixable, whereas the craft-domain ceiling is a pair-difficulty limit that Round-2 must address. We do not evaluate engagement, era/circle conditioning, or calibration here, and we claim no general taste SOTA.

---


### 98. [Vela: User Behavior as Supervision Sparks LLM Intelligence](https://arxiv.org/abs/2610.14709)

**<font color=#1a73e8>作者：</font>** Yang Xiao, Yusong Sun, Haoyi Wu 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in applications that act on users' long-term behavior histories, from personal assistants to recommendation and advertising systems. These applications demand the user dimension of LLM intelligence: inferring a person's preferences, intent, and likely future actions from weeks to years of behavior data. Yet current models are trained on static text or synthetic data, neither of which captures how user behavior evolves over time. Real-world behavior records, already available at scale on content platforms and in personal-assistant agents, offer a natural supervisory signal. We propose user behavior as supervision and introduce Vela, a framework that converts real user behavior data into trainable tasks and trajectories. From the anonymized behavior records of 100,000 users, Vela generates 100,000 tasks across 91 real-world task templates; difficulty-based filtering and trajectory acceptance criteria retain approximately 75,000 tasks with selected training trajectories. Fine-tuning Qwen3.6-35B-A3B on these trajectories improves performance over the base model by up to 11.5 points on user-related tasks and by an average of 4 points on general benchmarks. Training on more user behavior data further improves user-related performance, and reinforcement learning after fine-tuning outperforms reinforcement learning from the base model by up to 7.7 points. These gains suggest that real-world user behavior is a scalable source of supervision for both user-centered capabilities and the broader intelligence of LLMs.

---


### 99. [DeKoR: Decomposed Knowledge Routing for Efficient GNN--LLM Fusion](https://arxiv.org/abs/2610.14710)

**<font color=#1a73e8>作者：</font>** Peiyuan Li, Yongqi Huang, Jitao Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong potential for text-attributed graph learning by leveraging rich pre-trained knowledge and language understanding capabilities. Combining LLMs with Graph Neural Networks (GNNs) offers a promising paradigm for expanding the modeling capabilities of graph learning. However, LLMs and GNNs follow distinct learning paradigms, leading to a pronounced mismatch between their knowledge spaces. Such discrepancies make effective knowledge fusion nontrivial. Moreover, existing methods often incur substantial additional computation for only limited performance gains. To address these challenges, we propose DeKoR, an efficient framework for GNN and LLM knowledge fusion. To enable efficient knowledge transfer, DeKoR decomposes LLM knowledge into complementary local and global views and uses the LLM as an offline teacher to distill them into lightweight experts. To enable selective knowledge fusion, an adaptive router learns how much each node should rely on each expert. Extensive experiments on multiple benchmarks demonstrate that DeKoR outperforms existing baselines on both node and subgraph classification, achieving superior effectiveness and efficiency.

---


### 100. [Relational Semantic Grounding for Test-Time Discovery](https://arxiv.org/abs/2610.14721)

**<font color=#1a73e8>作者：</font>** Tianle Liu, Gongbo Cheng, Chenggong Ni 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-Time Discovery (TTD) aims to recognize known classes and detect novel ones from a continuous unlabeled test stream after deployment. Existing TTD methods mainly rely on visual clustering or prototype comparison, and can only assign anonymous labels to discovered classes, leaving them difficult to interpret in open-world applications. In this paper, we propose SEGA, a Semantic Grounding with Attributes framework for TTD. SEGA leverages large language models to generate attribute-rich descriptions for known classes and constructs an attribute-anchored visual-semantic space during training. At test time, we introduce Relational Semantic Grounding (RSG), which grounds unknown samples with similar and dissimilar known-class anchors, prompts the LLM to generate candidate concepts, and reranks them in the learned semantic space. The selected concept is further used for confidence-guided test-time semantic stabilization. By coupling attribute-level semantic alignment with relational concept grounding, SEGA transforms anonymous test-time clusters into interpretable semantic concepts. Experiments show that SEGA improves TTD baselines with the promise of semantic grounding for open-world.

---


> [!TIP]
> 当前位于：**51-100**（第 2/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
