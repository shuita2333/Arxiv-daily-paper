# 🧠 大模型相关研究 | 2026年08月12日

> 本类共 **438** 篇论文：已确认 **404** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-438](./part-09.md)

---

### 351. [Build it, Break it, Repeat: Benchmarking and improving LLM-manipulated disinformation detection in social media posts](https://arxiv.org/abs/2608.09510)

**<font color=#1a73e8>作者：</font>** Kevin Thomas, Milosz Kasprzyk, Reuel C Igbokwe Onuigbo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting machine-generated disinformation on social media is increasingly difficult as large language models (LLMs) make it easier to generate and rewrite misleading content at scale. Static benchmark evaluations, measuring detector performance on fixed held-out datasets, do not capture how detectors behave when posts are deliberately transformed to evade classification. This paper adapts the Build it, Break it, Fix it framework into Build it, Break it, Repeat (BiBiR): iterative sessions designed to stress-test detectors' robustness under iterative adversarial conditions, evaluating whether models remain reliable when disinformation posts are systematically transformed to evade classification. Across five iterations, the findings show that the best adversarial breakers' transformations came from a combination of back-translation and LLM persona-based rewriting, with the best performing technique achieving a 95% label flip rate (LFR), whilst still preserving the meaning of the original posts. The best builders' model was a triplet contrastive model with a dynamic anchor switching (DASS) architecture, which achieved an average accuracy of 72.68%, outperforming the strong baseline (a fine-tuned e5-small-LoRA) by 15 percentage points on the most robust set of breakers' adversarial attacks. The results demonstrate that an iterative framework best exposes detector weaknesses and pushes robustness improvements; however, it may still require semantic preservation analysis to distinguish valid adversarial evasion from transformations that changed the original disinformation claims' meaning.

---


### 352. [One Adapter Pair per Model: A Universal Activation Interface for Language Models](https://arxiv.org/abs/2608.09521)

**<font color=#1a73e8>作者：</font>** Su-Hyeon Kim, Jiwan Mun, Yo-Sub Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation-based tools are usually tied to one model's native hidden space, requiring probes, sparse autoencoders, and natural-language interpreters to be rebuilt or rediscovered for each new language model. We present a Universal Activation Bus, a framework that provides a common activation interface across compatible language models. Using a small set of source models, we learn a shared dense space together with one lightweight linear encoder--decoder adapter pair per model. After source training, the interface is frozen; a new model joins by fitting only its adapter pair on unlabeled matched text. The resulting interface allows activation-based tools to be shared across connected models, including common probes and SAE features as well as access to an NLA originally trained for a different model. Across five models, semantically related texts form consistent neighborhoods in the shared space, and an onboarded model reuses these tools effectively without retraining them. We further show that an intermediate activation from one model can be used by another model's frozen upper layers to produce predictions. These results establish a stable, model-wise activation contract for reusable tools across compatible language models.

---


### 353. [STAIR: Effective Incident Response Using an End-to-End Agentic Planning Framework](https://arxiv.org/abs/2608.09524)

**<font color=#1a73e8>作者：</font>** Hanlin Jiang, Jionghao Huang, Shaofei Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Incident response planning is critical for restoring compromised software systems after cyberattacks. Common practice relies on expert-driven playbooks that encode fixed response procedures, but these static workflows struggle to adapt to evolving incident states, changing recovery objectives, and execution feedback. Recent LLM-based planners and tool-using agents improve automation, yet they remain unstable in long-horizon response because they lack a unified basis for maintaining incident state, aligning actions with the current recovery stage, and reusing historical experience.
We present STAIR, an end-to-end agentic planning framework for incident response. The framework maintains the current incident as Graph-as-State, uses a Stage Router to dispatch planning to stage-specialized agents, and retrieves historical experiences to guide action selection. An Execution Harness executes actions, returns feedback to update the incident state, and validates action effects for future experience reuse. Across 100 Docker-based cyber ranges, our framework achieves a normalized defense score of 0.94 and improves over the strongest baseline by 9.5%.

---


### 354. [RangeFactory: Scalable Construction of Multi-Hop Cyber Ranges](https://arxiv.org/abs/2608.09526)

**<font color=#1a73e8>作者：</font>** Hanlin Jiang, Puyi Wang, Jiandong Jin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Real-world cyberattacks often require sustained progress across multiple hosts and network segments, making multi-hop cyber ranges essential infrastructure for studying and improving LLM agents' ability to sustain complete attack chains. Prior work has scaled isolated vulnerability tasks and constructed multi-host scenarios from manually specified vulnerability semantics. However, they are still unable to automatically orchestrate the growing supply of vulnerability environments into end-to-end validated multi-hop ranges. To this end, we present RangeFactory, an automated cyber-range orchestration framework that constructs multi-hop cyber ranges at scale from isolated vulnerability environments. RangeFactory formulates range construction as dependency resolution: it extracts dependency information from agents' actual attacks against real vulnerabilities, resolves known dependencies through template-guided orchestration, and uses end-to-end attack execution to validate runtime dependencies that emerge after composition. Using RangeFactory, we construct RangeBench with 1,148 validated range instances spanning 287 distinct attack chains and evaluate frontier attack agents across attack depth, network scale, and task information. Among runs that compromise the entry vulnerability, 24.5-47.0% still fail to complete the remaining attack path, revealing a substantial sustained-compromise gap between establishing an initial foothold and completing a multi-hop attack. RangeFactory further produces a corpus of 5,541 outcome-annotated multi-hop attack trajectories, providing execution data for attack-process analysis and future agent training.

---


### 355. [TCS-BENCH: Benchmarking State-of-the-Art Generative AI Theoretical Computer Science Research Ability](https://arxiv.org/abs/2608.09538)

**<font color=#1a73e8>作者：</font>** Vincent Cohen-Addad, Dimitris Paparas, Ernest van Wijland 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce TCS-Bench, a benchmark for evaluating Large Language Models (LLMs) on research-level Theoretical Computer Science (TCS) proof generation. TCS-Bench consists of theorem-proving tasks from papers published at top theoretical computer science venues (STOC, FOCS, and SODA). Each task provides the necessary context to derive a self-contained proof for a target result. We evaluate state-of-the-art models on this benchmark. We verify the correctness of generated proofs via a verification agent, and further benchmark the verifier against human-expert proof judgements on a set of target statements and generated proofs pairs. Our reference verifier achieves over 90% accuracy on the expert labeled set.

---


### 356. [Mawqif-v2: An Arabic Benchmark Dataset for Cross-Target Stance Detection](https://arxiv.org/abs/2608.09539)

**<font color=#1a73e8>作者：</font>** Rasha Albalawi, Nuha Albadi, Hamzah Luqman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Publicly available Arabic datasets for target-specific stance detection remain limited, particularly for evaluating cross-target generalization. This paper presents the Mawqif-v2 Extension, consisting of 996 manually annotated Arabic tweets collected from three public targets: Women Driving, E-Cars, and Trimester System. Each tweet is annotated with stance, sentiment, and sarcasm labels following the original Mawqif annotation scheme. The released extension is intended as a held-out evaluation set for assessing model generalization to both semantically related and previously unseen targets, while the original Mawqif dataset is used for training and development. In addition, we establish baseline results using several Arabic and multilingual transformer models, as well as zero-shot large language models (LLMs), to facilitate reproducible evaluation. Together with the original Mawqif dataset, the Mawqif-v2 Extension provides a benchmark for evaluating cross-target generalization in Arabic stance detection.

---


### 357. [ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models](https://arxiv.org/abs/2608.09548)

**<font color=#1a73e8>作者：</font>** Yilin Jiang, Xiaorong Zhu, Fei Tan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in education as tutors, teaching assistants, and content generators. These roles place demands that ordinary question answering does not: a usable education-facing model is supposed to be accurate, safe under sensitive prompts, instructionally useful, and aligned with pedagogical goals at the same time. Existing benchmarks evaluate these requirements largely in isolation, so none assesses education-facing suitability as an integrated profile. We introduce ELBench, the first benchmark to evaluate all four requirements (General Capability, Safety and Trustworthiness, Basic Education, and High-Level Cultivation) on the same models under a common protocol, combining curated public sources with newly synthesized safety and cultivation data. We evaluate nine models, seven frontier general-purpose systems and two education-specialized variants, and report three findings. First, module-level profiles are more informative than a single aggregate: the top six models are statistically indistinguishable on overall score, yet their module leaders differ substantially, and safety is anti-correlated with practical teaching (r = -0.83). Second, the Chinese-developed models lead the safety module, the most discriminative in the suite; this advantage is largest on region-specific normative content and narrows, but does not vanish, on universal-harm content. Third, the two education-specialized models lead neither education module, and on High-Level Cultivation all models share a systematic blind spot: on the structured judgment task they converge on the same non-reference option, favoring pedagogical style over fit to the stated goal, so the module scores uniformly low and does not separate models. This raises, but does not resolve, whether domain post-training keeps pace with frontier systems on education tasks.

---


### 358. [Bidirectional Context Self-Distillation for Reinforcement Learning of Skill-Based LLM Agents](https://arxiv.org/abs/2608.09555)

**<font color=#1a73e8>作者：</font>** Tianjun Pan, Yuan Li, Hongda Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> External natural-language skills provide large language model (LLM) agents with reusable and editable guidance for solving complex tasks. Yet their effectiveness depends not only on skill quality, but also on whether the policy can translate the provided guidance into appropriate actions. However, methods specifically designed to improve this skill-utilization ability remain largely underexplored. In practice, skill-based agents are commonly trained with reinforcement learning objectives centered on task-level rewards, which offer limited supervision and struggle to capture subtle differences in how effectively the policy uses the provided skills. We propose BCSD (Bidirectional Context Self-Distillation), a framework that combines self-distillation with reinforcement learning to train LLM agents to use external skills more effectively. Unlike prior self-distillation methods that rely on a single privileged context, BCSD evaluates each trajectory from two complementary skill-context views. The augmented view introduces higher-level Meta-Skill guidance, while the reduced view prunes general guidance to highlight task-specific skills. Their complementary token-level signals are combined to rescale the RL advantage. Experiments on ALFWorld and WebShop demonstrate that BCSD achieves the strongest overall performance across model scales, enabling agents to utilize external skills more effectively. Ablation studies further verify the complementary contributions of the augmented and reduced context views. Code will be released to ensure full reproducibility.

---


### 359. [From Runnable to Verifiable: An Independent Reproducibility Study of LLM/Agent-Driven Vulnerability Validation Artifacts](https://arxiv.org/abs/2608.09567)

**<font color=#1a73e8>作者：</font>** Bo Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security research artifacts---repositories, PoC exploits, and validation pipelines---are increasingly produced by LLM/agent-driven vulnerability workflows, yet the gap between \emph{publicly available}, \emph{runnable}, \emph{signal-producing}, and \emph{semantically confirmed} artifacts is poorly measured. We conduct a pre-registered reproducibility audit of this literature. A search covering 2023--2026 with dual screening yields a 104-paper consensus corpus, of which 59 papers (56.7\%) have a publicly reachable artifact. We execute an 18-paper sample at R0/R1 and all 102 cases of the anchor benchmark (arXiv:2509.24037), with patched-counterfactual verdicts on 30 signal-producing cases and matched-negative-control verdicts on 19. Three findings stand out. First, 58/102 (56.9\%) anchor cases contain a script-internal CVE identifier that diverges from the declared directory CVE. Second, only 10/18 (55.6\%) paper-level artifacts complete their declared workflow at R0, rising to 11/18 (61.1\%) after environment-only R1 repair. Third, artifact-embedded oracles prove unreliable: 20/30 patched-counterfactual audits still produce the claimed signal on the patched build, 7/19 matched negative controls still trigger on benign input, and the oracle confusion matrix has sensitivity 60\% and specificity 45\%. A trigger on the vulnerable build is not evidence of CVE-specific reproduction without a clean patched counterfactual. These are exploratory results from a pre-registered protocol, and our protocol---pre-registered post-conditions, R0/R1 repair ladder, G1--G3 semantic evidence levels, and patched-counterfactual oracles---is a reusable template for the security reproducibility community.

---


### 360. [VideoVIBE: A Video-Grounded Diagnostic Benchmark for One-Shot Interactive Website Generation](https://arxiv.org/abs/2608.09573)

**<font color=#1a73e8>作者：</font>** Jiajun Xu, Yanghao Zhou, Jingyun Liao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural-language-driven "vibe coding" enables the one-shot generation of visually rich and interactive web applications, yet reliable assessment of their quality has not kept pace. Existing evaluations often score isolated artifacts or final task outcomes, offering limited evidence about which failures occur and why. We introduce VideoVIBE, a video-grounded benchmark that transforms human-operated webpage recordings into fine-grained diagnostic tasks. It contains approximately 1.7K diagnostic Video QA instances derived from 6,338 verified failures across generated webpages, spanning semantic-logical, visual-motion, structural-temporal, and functional failures. Diagnoses are grounded primarily in recorded presentation and behavior, with webpage source code used as complementary context. We further propose V2Lens, a training-free, evidence-grounded multi-agent system that challenges and selectively refines initial video-based diagnoses through targeted visual and source-code verification. Across thirteen closed-source and open-weight Video MLLMs, Gemini-2.5-Flash is the strongest standalone model with a score of 64.54, while V2Lens reaches 71.72, an improvement of 7.18 points. Together, our results show that video-grounded evaluation can move beyond isolated artifacts and aggregate outcomes toward a behaviorally faithful and diagnostically informative account of generated application quality.

---


### 361. [The Politician, the Liar, and the Obedient Worker: Emerging Behavior of LLM Agents in Hierarchical Games](https://arxiv.org/abs/2608.09574)

**<font color=#1a73e8>作者：</font>** Fatemeh Seyedin, Adrian Weller, Jinhyuk Yun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs are rapidly embedding themselves into daily life: drafting our emails, managing our schedules, and making decisions on our behalf. As they move from individual tools to participants in multi-agent organizations, an important question arises: do they reproduce the governance failures like free-riding, corruption, and entrenched leadership that plague human institutions? We introduce the Hierarchical Game (HG), a public goods game extended with managerial authority, democratic elections, and private communication. Testing six frontier models across twelve experiments that add institutions one at a time (speech, peers, government, wages, oversight, elections), we find distinct behavioral profiles: Qwen promises and lies (13.3\% broken promises); Grok refuses to cooperate on its own but becomes fully cooperative once a manager can punish it (16\%$\to$100\%); Claude and GPT-4o cooperate reliably at baseline. But honesty proves fragile. When the manager role comes with a salary, all models except GPT-4o start cutting private deals to win or keep the position. When punishment is made anonymous, honest models begin to cheat. When all agents share the same model family, the first elected manager stays in power indefinitely. Leadership change only happens in groups that mix different families.

---


### 362. [ICM Out! Better Tournament Strategy from Computed Continuations, vs. Solvers and LLMs](https://arxiv.org/abs/2608.09586)

**<font color=#1a73e8>作者：</font>** Boning Li, Longbo Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Independent Chip Model (ICM) converts tournament chips into reference prize equity, and policies are routinely constructed against those values. Because ICM reads only stack sizes, it omits action order, blind obligations, and seat rotation, and it does not price the elimination pressure a big stack puts on the short stacks it can bust. Those omissions can alter the successor-state contrasts that determine a move. We introduce Strategic-Continuation Optimization (SCO), a policy-construction method that enumerates current-hand outcomes, maps them to successor states, prices those states with continuation values computed from the finite tournament model, and optimizes and freezes the resulting current-hand policy. The fixed-ICM comparison policy changes one thing only: the same optimizer solves the same game with successor states priced by analytic ICM, so the two policies differ only through that pricing. We evaluate the resulting policies in a three-player jam/fold tournament with a \$1M prize pool. Relative to the frozen strategic-continuation benchmark, analytic ICM has \$9{,}036 mean absolute value error across all 2,838 state--seat entries. That value error rewrites the ranges it prices: measured against each decision point's own fixed-ICM jam range, SCO moves the jam frequency by an average of 14.08\%. To price those different moves, we compare all 946 states and three policy owners while changing only the focal policy and holding both opponents and the continuation evaluator fixed. The policy produced by SCO earns \$214.33 more prize equity per hand on average and is favored in 2,433 of 2,838 matched units. The ordering survives replacing the solver-built opponent with two LLMs and with a family of non-modeling threshold players. This value-to-policy-to-cost chain shows directly when ICM becomes an inadequate objective for tournament strategy construction.

---


### 363. [MDB-Link: Hierarchical Schema Linking for Multi-Database Text-to-SQL](https://arxiv.org/abs/2608.09588)

**<font color=#1a73e8>作者：</font>** Beiyu Xu, Zhenyu Wu, Jiaoyan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traditional Text-to-SQL research and benchmarks assume a known target database, overlooking settings in which a query must be routed within a large, heterogeneous database collection. We therefore study schema linking in a multi-database setting, where the system must first locate the target database and then construct a compact, SQL-relevant schema for generation. We propose MDB-Link, a hierarchical schema-linking framework that retrieves question-relevant columns from a global index, aggregates retrieval evidence to shortlist databases, and uses a budget-aware large language model (LLM) for database reranking, table selection, and column grounding. With Qwen2.5-14B, MDB-Link outperforms LinkAlign on MMQA, Spider2-Snow, and BIRD-dev in database localization and column selection while producing schema subsets close in size to the gold schemas. Exact match improves from 16.88 to 51.41 on MMQA, 2.50 to 9.17 on Spider2-Snow, and 12.52 to 38.01 on BIRD-dev. MDB-Link also runs faster than LinkAlign and AutoLink, demonstrating the effectiveness of hierarchical schema reduction for downstream SQL generation.

---


### 364. [From Sweep to Seam: Interleaved Cross-Block Post-Training Quantization](https://arxiv.org/abs/2608.09595)

**<font color=#1a73e8>作者：</font>** Achille Jacquemond, Yuma Ichikawa, Akira Sakai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compressing large language models to two bits or fewer is increasingly feasible through block-wise post-training quantization; cross-block variants reconstruct neighboring Transformer blocks within a moving window. In the fixed two-block setting studied here, the matched sequential baseline moves this window through the network once, so errors introduced early in the sweep are not revisited. We propose Interleaved Cross-Block Quantization (ICBQ), a scheduling modification that revisits the boundary pair between consecutive chunks. Each seam pair is refined twice: first at the end of one chunk and again at the start of the next. The method retains the local two-block objective and reuses the calibration inputs of existing block-wise PTQ pipelines. Under stated local contraction and smoothness assumptions, we derive a depth-wise upper-bound comparison in which seam revisits multiply the propagated term while the residual remains bounded independently of depth. In the reported experiments, ICBQ reduces ternary-quantization perplexity relative to the matched Sequential CBQ baseline, yields finite perplexity in configurations where the baseline has severe degradation, and can also be used with 3-bit and 2-bit GPTQ.

---


### 365. [Rethinking Self-Evolving Agents: Do We Still Need Prescribed Optimization Pipelines?](https://arxiv.org/abs/2608.09629)

**<font color=#1a73e8>作者：</font>** Hui Xue, Fan Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents are usually built around prescribed optimization pipelines: the framework decides how to gather evidence, revise a persistent artifact, select candidates, and stop. We ask whether this task-specific procedure remains necessary when a frontier model acts as the optimizer. We introduce Open-Ended Optimization (OEO), which keeps the objective, permitted interactions, resource budget, data boundary, and evaluation fixed while allowing the optimizer to compose the improvement process online. We compare OEO with two complementary prescribed approaches: SkillOpt, a staged pipeline with bounded edits, and GEPA, a reflective evolutionary search. Across 14 head-to-head comparisons over 8 benchmark-target-model settings, GPT-5.5-driven OEO records 12 wins, 1 tie, and 1 narrow loss of 0.21 percentage points. It uses a median 34.3 percent of SkillOpt's configured target-interaction token budget. A one-shot, zero-interaction control shows that the gains are not explained by a single prior-driven rewrite. However, delegation has a capability boundary: SkillOpt outperforms OEO with a medium optimizer, and a weak optimizer cannot operate through the unchanged OEO interface. In the fully instrumented OEO-SkillOpt pair, trajectory analysis further shows that prescription changes how optimization proceeds more consistently than it changes final behavior. Together, these findings recast prescribed pipelines as capability-dependent scaffolding: essential constraints remain external, but a sufficiently capable optimizer can compose the route from measurable feedback to persistent improvement.

---


### 366. [Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game Mechanics](https://arxiv.org/abs/2608.09638)

**<font color=#1a73e8>作者：</font>** Yen-Shan Chen, Yu Chian Duan, Chih-En Kuo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Theory of Mind (ToM) is essential for agent interactions, yet existing evaluations either rely on static scenarios that oversimplify mental-state reasoning or interactive settings that provide limited diagnostic insight. We present Avalon-ToM-Bench, a fine-grained benchmark that operationalizes ToM through the asymmetric-information mechanics of The Resistance: Avalon. Rather than evaluating end-to-end gameplay, it decomposes ToM into a 2$\times$2 taxonomy -- epistemic versus motivational reasoning crossed with inference versus action -- using human-crafted, perspective-constrained queries. Benchmarking 28 LLMs reveals three insights: 1) Reasoning, not knowledge. Models show strong game-rule comprehension but markedly weaker ToM abilities, isolating failures to social reasoning rather than missing domain knowledge. 2) Expression, not representation. Mechanistic analyses via linear probing and activation steering show that models frequently represent correct mental-state inferences in their hidden states but fail to express them during generation -- linear probes recover 77-82% accuracy versus 62-70% from the models' own chain-of-thought. 3) Policy, not deliberation. Dedicated reasoning training yields substantial improvements whereas test-time chain-of-thought provides only marginal gains (+11.0 versus +1.1 points on average), suggesting that robust ToM depends on a learned reasoning policy rather than increased inference-time deliberation.

---


### 367. [Activation Probes Surface Code-Security Signals that the Model's Output Misses](https://arxiv.org/abs/2608.09643)

**<font color=#1a73e8>作者：</font>** Ivan Wiryadi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding agents now write a growing share of production code, and human security review does not scale at the rate code is generated. The agents in widest use are closed-weight, so a deploying team cannot read their internals. It can instead run an open-weight model as a reviewer over the agent's output. That reviewer's activations are readable. We ask whether reading those activations recovers a security signal that simply asking the same reviewer misses. We fit a single linear probe per model on a corpus of paired vulnerable-and-fixed Python functions, then test it without retraining on real disclosed vulnerabilities whose weakness type the probe never saw in training, across five open-weight reviewer models. On the vulnerabilities fixed by changing a single function, the probe scores the vulnerable function above its fix on 61-67% of cases for every model, beating the 50% chance line. It also beats the same model's prompted YES/NO win-rate read from its logits, under every prompt we try. Asking the model for a written verdict, even with chain-of-thought, returns the same answer on the vulnerable and fixed function most of the time and so cannot tell them apart. Model activations carry a code-security signal that prompting the same model misses.

---


### 368. [Hallucination-Free GUI Grounding via Regression-Free Layout-Aware Matching](https://arxiv.org/abs/2608.09654)

**<font color=#1a73e8>作者：</font>** Yuke Li, Xuehan Hou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI agents are shifting from metadata-dependent large language models to purely visual multimodal large language models (MLLMs) that operate directly on screenshots. The core task, GUI grounding, requires translating abstract user instructions into precise element coordinates. This task faces a persistent dual obstacle: conventional grounding models lack the semantic richness to interpret abstract instructions, while end-to-end MLLMs suffer from coordinate hallucinations caused by deficient fine-grained perception. We propose a regression-free framework where a frozen MLLM performs instruction parsing and a dedicated grounding model handles precise localization without learning any coordinate regression. A frozen MLLM first elaborates the abstract instruction into a structured visual description rich in layout cues. These descriptions are then fed to a novel Layout-Aware GUI Grounding Model, which performs regression-free localization by matching against layout-prior candidates, inherently suppressing hallucinations and avoiding expensive fine-tuning. The grounding model is trained with only Text/Icon binary labels, requiring no coordinate regression parameters. On ScreenSpot-Pro, our method achieves over 20% improvement in grounding accuracy over end-to-end systems; on Mind2Web, it raises success rate and element selection rate by more than 15%. These results demonstrate that decoupling instruction understanding from layout-aware localization effectively resolves the core challenges of GUI interaction.

---


### 369. [Open Evaluation Agent: Efficient and Promptable Evaluation of Visual Generative Models](https://arxiv.org/abs/2608.09666)

**<font color=#1a73e8>作者：</font>** Shulin Tian, Ziqi Huang, Fan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in visual generative models have enabled high-quality image and video generation, but evaluating these models often demands sampling hundreds or thousands of images or videos, which is computationally expensive. Existing evaluation methods also rely on rigid pipelines that overlook specific user needs and provide numerical results without clear explanations. Mimicking how humans quickly form impressions of a model's capabilities from only a few samples, we propose the Evaluation Agent framework, which employs human-like strategies for efficient, dynamic, multi-round evaluations, offering detailed, user-tailored analyses. Given a natural-language evaluation request, the agent decomposes it into sub-aspects, generates targeted prompts, samples images or videos from the evaluated model, invokes suitable evaluation tools, and iteratively updates its plan from the observed evidence, covering both predefined benchmark dimensions and open-ended user concerns. The framework is thus efficient, promptable, explainable, and scalable across models and tools. Experiments show that Evaluation Agent reduces evaluation time to 10% of traditional methods while delivering comparable results. We further introduce Open Evaluation Agent (Open-EA) by constructing EA-CoT-10K, a corpus of history-conditioned step-level instruction-tuning records derived from multi-round evaluation rollouts, and training EA-3B from Qwen2.5-3B-Instruct as a local planning backbone that preserves the structured reasoning, tool invocation, and summary protocol of the API-based agent while reducing dependence on proprietary backbones. Experiments validate the API-based agent on established T2I/T2V benchmarks and open-ended queries, and evaluate Open-EA on four in-domain and three out-of-domain T2V generator families, showing partial cross-family transfer of the learned policy.

---


### 370. [Thinking With Tools, Not With Pixels: Tool Calls as Text Scaffolds for Visual Reasoning](https://arxiv.org/abs/2608.09682)

**<font color=#1a73e8>作者：</font>** Jiahao Shao, Yuanbo Yang, Yiyi Liao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tool-augmented vision-language models increasingly "think with images": they call crop, zoom, or code tools and reason over the returned pixels. However, recent work using blind tests, gain decompositions, and attention analyses has shown that returned images contribute little, raising the question: if pixels do not carry the gain, what does? We hypothesize that the load-bearing signal is the structured text emitted before any returned pixel arrives: tool name, coordinates, target description, and intent. This textual scaffold encodes where to look and what to find. We introduce TextCall (call-but-no-return) to test this: it keeps the scaffold but replaces returned images with the text placeholder [Image output skipped]. Three studies support the hypothesis. (i) Non-necessity of returned pixels: across LoRA, full fine-tuning, and RL, TextCall matches or exceeds full thinking-with-images; under RL it preserves tool use at the reported checkpoint, avoiding the failure mode where, under matched settings, seeing the returned image causes the model to stop calling tools and answer directly. (ii) Sufficiency of the scaffold: on matched training queries, scaffold-only input yields equivalent accuracy to returned-image input. (iii) Component specificity: decomposing the scaffold into reasoning text and spatial code shows both components contribute, with the dominant one varying by task. Together these results support the Tool-Call Scaffold Hypothesis: in current thinking-with-images distributions, the active signal is the structured text emitted at tool-call time; the returned image is a redundant carrier. TextCall preserves accuracy while reducing latency by 29-46% and eliminating tool-execution API calls. Our claims hold for current thinking-with-images benchmarks; constructing tasks where pixels are genuinely load-bearing remains an open direction.

---


### 371. [Diffuse the object, keep its label: curating detector training data from a few unlabeled photographs via VLM-built 3D vegetation scenes](https://arxiv.org/abs/2608.09691)

**<font color=#1a73e8>作者：</font>** Mario Malizia, Marnix Enting, Rob Haelterman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Labeled images of small objects hidden in vegetation are scarce, and detectors trained on them generalize poorly across sites. Rather than reusing labels collected at another site, we synthesize labeled training images from a handful of unlabeled photographs of the deployment site itself. A vision--language model generates a coarse 3D vegetation scene from one photograph; placing 3D object meshes in the scene yields bounding boxes, segmentation masks, and per-instance occlusion directly from the scene geometry, without manual annotation. A lightweight adapter fine-tuned on the photographs conditions a diffusion pass that re-textures the renders, and a graded mask-lock sets how much diffusion may touch the object itself. In our runs this grade was the most influential curation choice: lightly diffusing the object improves minority-class recall over fully protecting its pixels, while unrestricted diffusion dissolves it. Trained on these images, a standard detector matched or exceeded its counterpart trained on a larger labeled dataset of real images from a different site, consistently across seeds on a humanitarian-demining benchmark; the comparison is thus unsupervised site adaptation from a handful of photographs against conventional cross-site label reuse. In our ablations the gains were largely insensitive to the photograph and crop budgets, and in-domain accuracy did not predict cross-site performance.

---


### 372. [Model Discovery Agent: LLM-assisted Bayesian experiment design for data-efficient discovery of mechanistic world models](https://arxiv.org/abs/2608.09696)

**<font color=#1a73e8>作者：</font>** Kevin Murphy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting the answer to interventional ``what if'' questions --- the outcome of an action never taken --- requires a \emph{mechanistic}, causal model, not a curve fit; and learning such a model requires \emph{experiments}, because passive data leaves its mechanisms unidentified. Experiments are expensive, so the central problem is \emph{data efficiency}. We present the Model Discovery Agent (MDA), which couples a large language model (LLM), used as a \emph{proposer} of candidate structures, with standard Bayesian machinery --- sequential Monte Carlo (SMC) for parameter and structure posteriors, simulation-based inference (SBI) for intractable likelihoods, and value-of-information (VoI) for experiment design --- to discover latent mechanistic world models from few interventions. MDA operates in the M-open setting: when the truth lies outside the current hypothesis class, a predictive check flags the inadequacy and the proposer expands the hypothesis space with a new model whose parameters are then identified by designed experiments. We show that \emph{discovery and design reinforce}: the design step identifies the mechanism the discovery step proposes, and the identified mechanism improves predictions, enabling further discoveries from the remaining unexplained residuals. On three different benchmarks --- covering physics (\DPbench, \citep{wiemann2026discoverphysics}), chemistry (\CHEMbench, \citep{kabra2026autoscilab}) and biology (\HHbench, a new partially observed single-neuron electrophysiology benchmark we create) --- we show that MDA sets a new SOTA in terms of data-efficient model learning and reliable interventional forecasting ability.

---


### 373. [VeriForge: Mitigating Latent Knowledge Gaps in Narrative Drafting via Mixed-Initiative Scaffolding](https://arxiv.org/abs/2608.09698)

**<font color=#1a73e8>作者：</font>** Ruqi Sun, Jiaping Li, Wenhui Tao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Great fiction earns its verisimilitude through precise details, from how a longsword is gripped to pierce armor gaps to why a bleeding corpse cannot yet smell of decay, weaving domain expertise into the fabric of invented worlds. Current AI writing tools offer limited support for discovering and integrating unfamiliar domain knowledge into narrative. They require explicit queries that authors cannot formulate, generate finished prose that risks homogenizing voice, or assist only within the boundaries of what authors already know. We argue that AI should reveal latent knowledge gaps to writers while preserving their agency to transform discovered knowledge into authentic prose. Grounded in formative interviews with 9 fiction writers, we present VeriForge, a mixed-initiative writing system that divides cognitive labor so that the system assumes initiative over domain discovery while the author retains full initiative over narrative synthesis. VeriForge realizes this through three complementary mechanisms. Proactive inline highlighting flags potential knowledge gaps as authors draft. Dual-stream querying pairs conversational responses with source-anchored Knowledge Cards for direct fact extraction. A spatial Knowledge Canvas allows authors to organize and connect discovered knowledge across their writing. These mechanisms are powered by a graph-based retrieval-augmented generation pipeline grounded in domain-specific source materials. A within-subjects user study (N=12) provides preliminary evidence that this paradigm helps authors recognize previously overlooked knowledge gaps, supports creative exploration, and is perceived by expert raters to produce passages with stronger domain grounding in a controlled cold-start writing task.

---


### 374. [Matryoshka Language Model Suites](https://arxiv.org/abs/2608.09703)

**<font color=#1a73e8>作者：</font>** Nathan Godey, Yoav Artzi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training a language model suite classically requires training each model separately and serving them independently. We improve both training and inference efficiency by stacking sub-models of increasing size into a single nested architecture trained end-to-end. This Matryoshka training framework reduces the total parameter count of the suite, enables low-cost distillation from the largest to all smaller sub-models at every training step, and is well-suited for speculative decoding as the draft model is contained within the verifier. We validate our approach by training a Matryoshka suite comprising 500M, 1.5B, and 3B sub-models. Our suite is on par with independently trained baselines on benchmark performance and validation and out-of-domain perplexities, while using 36% less training compute and improving the throughput of speculative decoding by 14-26%. We also ablate key architectural choices, offering guidance for building strong Matryoshka LM suites.

---


### 375. [How Do Large Language Models Judge Social Attraction? Evidence from Theory-Grounded Persona Ratings Across Multiple LLMs and Humans](https://arxiv.org/abs/2608.09717)

**<font color=#1a73e8>作者：</font>** Hasan Mahmud, Khawaja Abaid Ullah, Mohammad Javad Khojasteh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to perform subjective evaluations traditionally made by humans, yet their validity as social judges remains unclear. This paper examines whether LLMs can assess social attraction from theory-grounded persona profiles constructed from ten psychological and relational constructs and organized into three tiers: socially attractive, socially mixed, and socially unattractive. We examine LLM ratings in two studies and compare them with human judgments in a third study. In Study 1, 34 LLMs rated 12 profiles across three repeated runs. Although some models tended to give higher or lower ratings overall, they showed strong stability across runs, consistent three-tier ordering, and high agreement in relative profile ordering. Study 2 examined sensitivity to gender presentation using six matched name-and-pronoun profile pairs and a separate pronoun-only test with a gender-neutral name, finding no significant effects in either analysis. In Study 3, 198 human participants evaluated the six matched profiles from Study 2. Their ratings reproduced the three-tier structure and followed a profile ordering consistent with that of the LLMs. However, LLMs rated attractive profiles more positively and unattractive profiles more negatively than humans, while neither group showed a significant overall effect of gender presentation.

---


### 376. [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730)

**<font color=#1a73e8>作者：</font>** Qu Tang, Benhui Zhuang, Bo Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models are a widely adopted paradigm for embodied policies. They excel at efficient closed-loop control but do not explicitly model how physical scenes evolve as a task unfolds. Recently emerging world-action models (WAMs) leverage pretrained video world models to capture spatiotemporal evolution, yet retaining future generation or a large video backbone in the control loop substantially increases inference cost. We introduce World Tokens, an embodied policy architecture built around a World Adapter that bridges visual-language understanding, world-dynamics modeling, and action generation. It uses world modeling during training to enhance the action policy while preserving efficient deployment. Specifically, the World Adapter transforms VLM features into a fixed set of world tokens, which condition a jointly fine-tuned future-video denoiser and simultaneously serve as the action expert's sole visual-language context. This shared conditioning allows gradients from future-video denoising to directly shape the representation used for action prediction, while exclusive routing prevents the policy from bypassing that representation. At deployment, the world-model branch is removed, leaving only the VLM, World Adapter, and action expert, with no online video-model inference. With a 2B backbone and no embodied action pretraining, World Tokens is highly competitive on LIBERO, attains the best reported averages on SIMPLER, substantially improves real-world R1 Pro success over a matched action-only baseline, and generates each action chunk at VLA-level latency.

---


### 377. [ColluSkill: Adversarial Cross-Skill Composition for Evading Agent Skill Scanners](https://arxiv.org/abs/2608.09732)

**<font color=#1a73e8>作者：</font>** Puyu Zeng, Simeng Qin, Jingzhi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills are emerging as an important attack surface in LLM-based agent systems. Through an empirical study of existing skill scanners, we find that current defenses mainly inspect individual skills, leaving risks from cross-skill composition insufficiently examined. This creates a practical blind spot: multiple locally plausible skills may pass security checks while collectively forming a harmful workflow during agent execution. To investigate this threat, we propose ColluSkill, a collusive multi-skill-chain attack framework that decomposes a complete malicious intent into interdependent sub-payloads embedded in independently packaged skills. The attack does not rely on any single malicious skill, but emerges from the ordered composition of locally plausible behaviors through contextual dependencies, artifact passing, and execution handoffs. ColluSkill further employs LLM-based chain planning and scanner-feedback refinement to preserve chain-level attack semantics while reducing suspicious signals in individual sub-skills. To defend against such attacks, we propose ChainGuard, a context-aware skill-chain scanner that jointly analyzes a candidate skill and the skills already installed in the agent environment. ChainGuard reconstructs cross-skill dependencies, artifact flows, capability compositions, and downstream behaviors to identify risks that emerge only at the workflow level. Experiments on six representative skill scanners show that ColluSkill achieves an average attack success rate of 96.0% and consistently outperforms the evaluated single-skill and multi-skill attack baselines. Meanwhile, ChainGuard reduces the attack success rate to 22.5% while allowing 99.5% of benign workflows to pass, highlighting the importance of chain-level security analysis for agent skill ecosystems.

---


### 378. [Rethinking Factor Sharing in Federated LoRA: A Rank-Aware Adaptive Approach](https://arxiv.org/abs/2608.09742)

**<font color=#1a73e8>作者：</font>** Xinyi Xu, Bingnan Xiao, Shuang Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) represents large language model (LLM) updates with two compact matrix factors, i.e., $A$ and $B$, providing an efficient way to fine-tune large models in federated learning paradigm. Inspired by the asymmetric roles of the LoRA factors, we study whether $A$ should be shared across clients while $B$ remains client-specific (Share-A/Local-B), or whether $B$ should instead be shared while $A$ remains client-specific (Share-B/Local-A). With a least-squares surrogate, we reveal that Share-A/Local-B requires the client-specific LoRA update matrices to use a common rank-$r$ input-side space, whereas Share-B/Local-A requires a common rank-$r$ output-side space. The two strategies therefore incur different projection residuals, indicating that the preferred strategy is the one with the smaller aggregate residual across clients. With this insight, we propose Federated Adaptive Factor Sharing Low-Rank Adaptation (FedAS-LoRA), which selects the sharing side before training to enhance fine-tuning performance. To enable adaptive factor selection before training, we design a Rank-Aware Shared-Subspace Sufficiency (RSS) metric, which effectively assesses whether a shared rank-$r$ input subspace is sufficient for the local data distributions using representations extracted from a frozen LLM backbone. Experiments across different tasks, data distributions, LoRA ranks, and participation settings confirm the effectiveness of RSS and the superior performance of FedAS-LoRA.

---


### 379. [SR-OPSD: Self-Referenced On-Policy Self-Distillation](https://arxiv.org/abs/2608.09745)

**<font color=#1a73e8>作者：</font>** Zhuo Sun, Entong Li, Yanlong Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) converts feedback into dense token-level supervision on trajectories generated by the policy to be optimized, providing a useful complement to reinforcement learning with sparse outcome rewards. However, the self-teacher policy used in OPSD is typically a stop-gradient or exponential-moving-average copy of the policy conditioned on additional context information, and thus co-evolves with both the student policy and its on-policy context distribution. Directly matching such a moving target with a fixed projection objective can lead to unstable optimization or excessive distributional concentration. This nature of OPSD motivates the proposed \emph{Self-Referenced On-Policy Self-Distillation (SR-OPSD)}. At fixed student-generated contexts, a token-level variational characterization identifies the effective distillation target as a geometric interpolation between the self-teacher policy and a reference policy. Meanwhile, we use the Rényi divergence family to generalize the projection geometry. This formulation separates \emph{where} the adaptive target is placed from \emph{how} the student is projected toward it: the interpolation coefficient controls underlying target, while the Rényi order controls the projection geometry and its sensitivity to token-level density ratios. Extensive experiments across scientific evaluation, mathematical reasoning, and coding generation tasks with multiple large language models show that SR-OPSD achieves the state-of-the-art or competitive performance across various settings.

---


### 380. [REFRAMED: Towards Realistic Audio Description Generation for Movies](https://arxiv.org/abs/2608.09765)

**<font color=#1a73e8>作者：</font>** Igor Sterner, Mirella Lapata, Alex Lascarides 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio Description (AD) is a verbal narration of key visual content in videos, enabling access for visually impaired audiences. Unlike standard video captioning, AD is a structured editorial task: descriptions must be inserted into gaps in dialogue and must convey only what is needed to understand the narrative being told. However, existing approaches formulate AD generation in an artificial setting where both the content and timing of descriptions are pre-specified, reducing the task to clip-level captioning. They further rely on noisy transcription and alignment pipelines, and lack the rich parallel data required for modeling narrative context. We introduce a new formulation of AD generation in which models must jointly decide what to describe and when to do it. To support this, we present REFRAMED, a high-quality dataset of 2,023 videos that span 3,302 scenes from 206 movies, with professional AD transcripts (both American and British versions), professional subtitles and aligned screenplays. We also provide a manually curated challenge set that pairs full movies with multiple AD references, together with evaluation protocols that leverage dialogue gaps and multi-reference comparisons. Experiments with state-of-the-art AD systems and multimodal LLMs show that they outperform trivial baselines but fall far short of expert human performance. Our dataset and benchmark establish a new foundation for research on video understanding.

---


### 381. [PragMatch: Separating Pragmatic Incongruity from Cross-Modal Mismatch in Large Vision-Language Models](https://arxiv.org/abs/2608.09772)

**<font color=#1a73e8>作者：</font>** Zhanna Mukhametsharip, Vera Demberg, Varsha Suresh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have demonstrated strong performance on multimodal benchmarks, yet it remains unclear whether they genuinely reason about relationships between images and text or rely on superficial correlations, known as shortcut learning. This question is particularly important for multimodal sarcasm detection, where successful prediction depends on recognizing pragmatic incongruity rather than treating sarcasm as simple image-text mismatch. We introduce PragMatch, a controlled benchmark of 3,000 image-text pairs derived from MMSD2.0, including original sarcastic examples and constructed literal and hard-negative pairs. We identify influential shortcut cues through systematic masking and evaluate their impact through targeted injection experiments. Our results show that LVLM predictions are sensitive to lexical, OCR-derived and stylistic cues, with injected surface signals causing substantial changes in model predictions despite unchanged underlying image-text relationships. Our findings reveal limitations in current LVLMs while PragMatch provides a systematic testbed for evaluating multimodal pragmatic reasoning beyond surface-level image-text alignment.

---


### 382. [KGCaRe: Explainable Complex Conditional Question Answering using Automatic Knowledge Graph Construction and Context Retrieval with LLMs](https://arxiv.org/abs/2608.09779)

**<font color=#1a73e8>作者：</font>** Ghanshyam Verma, Simanta Sarkar, Devishree Pillai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answering complex conditional questions using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) remains a challenge, particularly in domain-specific contexts where general-purpose LLMs and RAG tend to underperform. We hypothesize that augmenting RAG with unstructured and structured knowledge, extracted from both documents and knowledge graphs (KGs), can improve reasoning and answer accuracy for such tasks.
To test this, we propose KGCaRe, a hybrid approach that combines neural retrieval with symbolic reasoning over LLM-generated KGs. KGCaRe constructs a KG from documents using a multi-prompt extraction strategy and stores it in a graph database. Simultaneously, the documents are embedded into a vector store to enable neural retrieval. KGCaRe performs innovative iterative graph traversal guided by the LLM to extract relevant triples, prune irrelevant information, and uses additional clue entities to traverse the graph again if the initial traversal does not provide satisfactory context to generate the answer. The relevant triples extracted from the KG in path form, along with semantically retrieved text passages, are then fed into custom KGCaRe prompts to generate answers to the complex conditional questions with explanations.
We evaluate KGCaRe on two complex conditional QA datasets. Our results on these datasets show that KGCaRe consistently outperforms existing baselines, including Vanilla LLM, Code Prompt, Text Prompt, Think-on-Graph, Vanilla RAG, and HybridContextQA, across multiple LLMs such as Mistral, Mixtral, GPT-3.5, and GPT-4o. We publicly release the software pipeline that we developed to implement the proposed KGCaRe approach.

---


### 383. [ADOPD: Reference-Privileged On-Policy Distillation for MLLM-Based Industrial Anomaly Detection](https://arxiv.org/abs/2608.09789)

**<font color=#1a73e8>作者：</font>** Jingtai He, Shiyuan Meng, Wenchao Meng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection (IAD) requires identifying fine-grained deviations from normal visual patterns. Multimodal large language models (MLLMs) can improve recognition accuracy by comparing query images with references at inference time, but these benefits rely on additional retrieval and processing. We investigate whether the benefits of reference comparison can instead be internalized in the model parameters. Access to references during training allows a reference-aware teacher to supervise a query-only student. However, the teacher may favor plausible responses based on query cues or language priors rather than valid visual information. We propose ADOPD, a reference-privileged on-policy distillation framework. The teacher evaluates student-generated rollouts under matched and mismatched references. The matched-reference teacher-to-student log-ratio defines the token-level learning direction, specifying what the student should learn. The likelihood gap between the two reference views estimates reference-specific support and calibrates the sequence-level weight. ADOPD achieves 77.31% average accuracy on the MMAD benchmark under zero-shot inference, improving the Qwen3-VL-4B backbone by 6.14 points and outperforming its one-shot setting by 2.64 points. Experiments show that ADOPD learns a fine-grained anomaly inspection strategy from reference comparison. The project will be available at this https URL.

---


### 384. [CARD: Controlled Agentic Reddit Discussions for Credit Card Simulation](https://arxiv.org/abs/2608.09790)

**<font color=#1a73e8>作者：</font>** Yaoning Yu, Kai-Min Chang, Ye Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online credit card discussions provide a natural setting for studying how consumers communicate about financial products. Simulating these discussions requires more than just generating individual comments, the generated threads should also match how real users express themselves and interact with others. We introduce CARD, a framework for generating realistic credit card discussion threads. Given a credit card post and its matched real thread, CARD uses non-verbatim guidance on reply structure, comment function, stance, tone, and conversational variation. A planner organizes these controls, a writer generates the discussion, and a calibration loop updates comments' populations that contribute to differences between the generated and real thread distributions. We evaluate CARD on real Reddit credit card discussions using lexical, semantic, behavioral, and structural metrics. CARD matches the distributions of real credit card discussions better than simulation baselines across multiple LLMs and also demonstrates smaller effect sizes and distribution distances across metrics. These results show that structured planning and targeted revision can generate the realism of simulated credit card discussions.

---


### 385. [SWE-Bench ProMax: Benchmarking Agents on Large-Scale Multilingual Code Refactoring](https://arxiv.org/abs/2608.09802)

**<font color=#1a73e8>作者：</font>** Yuling Shi, Jinghan Xu, Kelin Fu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As AI coding agents take on increasingly complex, long-horizon software engineering tasks, existing benchmarks are rapidly saturating and their evaluation quality has come under serious scrutiny: a recent audit found that nearly 60% of unsolved SWE-bench Verified instances contain flawed tests -- either overly narrow tests that reject correct solutions or overly broad tests that check unstated requirements -- and that frontier models can verbatim reproduce gold patches from training data. Code refactoring, which requires coordinated, behavior-preserving changes across many files, offers a substantially harder and more realistic test of agent capability, yet remains underserved by current benchmarks. We introduce SWE-Bench ProMax, an expert-curated, multilingual code refactoring benchmark of 170 instances drawn from real commits across seven programming languages (Python, Java, TypeScript, Go, C, C++, and Rust). Every instance undergoes rigorous, multi-stage curation that directly addresses the quality problems identified in prior benchmarks: issue descriptions are rewritten from scratch to provide precise, unambiguous specifications, and test suites are manually reviewed to remove overly narrow and overly broad tests. Tasks with insufficient complexity or limited cross-file scope are filtered out, yielding a benchmark of challenging, large-scale refactoring tasks that average 11.4 modified files and 261.6 lines of code per instance, substantially exceeding the scale of existing benchmarks. Experiments with frontier models under two agent scaffolds show that the best model achieves only 41.2% resolve rate, confirming that SWE-Bench ProMax presents a meaningful and unsaturated challenge for current AI coding agents. Our benchmark is available at this https URL.

---


### 386. [Parameter Exploration for RLVR via Variational Learning](https://arxiv.org/abs/2608.09805)

**<font color=#1a73e8>作者：</font>** Vatsal Venkatkrishna, Nico Daheim, Iryna Gurevych  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploration has been a focus of reinforcement learning research for a long time. Recently, there has been growing evidence that it is also an important ingredient in LLM reinforcement learning recipes that can significantly impact downstream performance. Many existing methods control exploration in the action-space, for example, using temperature scaling. However, these methods cannot reorder tokens but only influence the variance in the output distribution. This limits exploration and can lead to divergence or stalled training. Here, we investigate parameter-space exploration, where rollouts are generated by sampling different policies from a posterior that may each explore different rollouts. Sampling less or more diverse policies is then a complementary control lever over exploration. We introduce a family of methods called Perturbed Parameter Policy Optimization (3PO) which use different sampling strategies and different rollout grouping for reward estimation. Experiments on OLMo-3-1025-7B and Qwen2.5-Math-7B across mathematical reasoning and code generation tasks show that these approaches consistently improve average downstream performance over standard GRPO at a near-identical FLOPs cost. Moreover, using multiple parameter samples consistently produces fewer zero-advantage groups and malformed or incorrect rollouts during training than GRPO and action-space baselines. Overall, our work presents evidence that parameter-space exploration can improve reinforcement learning for LLMs.

---


### 387. [MedPixel: A Unified Pixel-Language Model for Medical Reasoning and Segmentation](https://arxiv.org/abs/2608.09818)

**<font color=#1a73e8>作者：</font>** Haoyu Yang, Meixing Shi, Zengjie Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable medical image understanding requires models to connect clinical language and visual reasoning with pixel-level grounding. Yet medical vision-language models often lack precise localization, whereas medical segmenters typically rely on explicit target categories or precise spatial prompts. This divide is reinforced by a supervision mismatch: segmentation datasets provide precise masks but little language supervision, whereas medical vision-language data rarely pair language with dense spatial annotations. To address this gap, we present MedPixel, a unified medical pixel-language model built around a shared language--mask interface. To provide scalable supervision, we introduce MedPLG-440K, comprising approximately 440K pixel-language task samples constructed through a clinically motivated synthesis process without external LLM annotation. MedPixel is trained with joint multi-task supervised fine-tuning followed by Pixel-Level Preference Optimization, which uses ground-truth masks as offline verifiers to derive response preferences from mask quality. MedPixel supports a broad spectrum of tasks spanning explicit grounding, implicit reasoning, spatial interaction, grounded explanation, and medical VQA. Across this task spectrum, MedPixel achieves strong performance in both pixel-level prediction and response generation, together with effective zero-shot transfer to external grounding benchmarks and robustness to imperfect spatial prompts. Code and model checkpoints will be released at this https URL.

---


### 388. [Macaron-V1: Towards Open Continual Learning with Self-Improvement and Mixture-of-LoRA](https://arxiv.org/abs/2608.09819)

**<font color=#1a73e8>作者：</font>** Mind Lab, Vin Bo, Asher Cai 等 76 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Macaron-V1 is an open agent-model family for experiential intelligence: learning from experience in real environments and continuing to learn after deployment. It is organized around two system goals. Adaptation is pursued through recursive improvement of versioned model-harness pairs, where experience from one configuration is evaluated under an external contract and used to construct its successor. Collaboration is pursued via the Mixture-of-LoRA (MoL) architecture that freezes a base model, composes specialist LoRA adapters, and selects one LoRA per user turn. The flagship Macaron-V1-Venti combines a 744B GLM-5.2 base with four LoRAs for chat, agent, coding, and GenUI; the Qwen3.6-based Macaron-V1-Tall (50B) uses the same design for local deployment. This report presents Macaron-V1 as a co-designed system spanning architecture, algorithms, and infrastructure. The MoL architecture supports continual learning through extensible LoRA specialists. The algorithm combines Model-Harness Co-design and recursive self-improvement loop, including the UI4A component-native GenUI harness, a stateful action substrate, versioned HCP contract, and the agentic RL framework MindForge. The supporting infrastructure includes the post-training platform MinT, the long-context RL method LongStraw, and stability techniques for sparse MoE and DSA base models. We evaluate Macaron-V1 on Personal Intelligence, GenUI, and general capability benchmarks against frontier baselines. Our results validate the current system, while compounding gains from continual learning and collective intelligence remain open questions.

---


### 389. [Distill Skills into Weights, Not Prompts: Abstract Skills as Privileged Signals for On-Policy Self-Distillation](https://arxiv.org/abs/2608.09826)

**<font color=#1a73e8>作者：</font>** Yubo Jiang, Fengying Xie, Zhiguo Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards yields no group-relative signal when rollout groups are uniformly correct or uniformly wrong, which account for 63.0-68.0% of groups in our experiments. We propose SKALD (Skill-Anchored Latent Distillation), an on-policy self-distillation framework that uses two context views of the same Qwen3-Base model: a question-only student and a teacher conditioned on an abstract, explicit-answer-filtered skill card. The student is trained on its own prefixes, transferring the skill-induced advantage into shared parameters without privileged input at test time. To stabilize context-induced distribution mismatch, SKALD employs an annealed exponentially tilted objective that downweights teacher-preferred tokens with very low student likelihood; as the tilt vanishes, it converges to teacher cross-entropy and recovers the forward-KL student gradient. An empirical gate activates distillation only when verified rollouts estimate a positive teacher advantage. Across five held-out mathematics benchmarks, SKALD improves overall avg@8 over GRPO by +2.46, +4.85, and +12.01 at 0.6B, 1.7B, and 4B, respectively. At 1.7B, zero-variance-only distillation recovers 84.7% of the full gain, while SKALD remains +4.06 above FLOP-matched GRPO and exceeds contextual skill exposure by +3.77. These results show that abstract skills provide dense supervision where group-relative rewards become uninformative.

---


### 390. [RA-FinBERT: Rule-aware LoRA adaptation for low-resource financial sentiment classification](https://arxiv.org/abs/2608.09834)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Jiaming Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial sentiment analysis converts unstructured financial news into quantitative signals that can support market analysis and decision-making. Existing work on resource-efficient financial NLP has largely focused on compressing or adapting pretrained language models, with less attention to combining contextual representations with lightweight rule-derived features. This study develops Rule-Aware FinBERT (RA-FinBERT), a parameter-efficient framework that integrates low-rank adaptation (LoRA) with three continuous VADER-derived sentiment proportions (positive, negative, and neutral) and a source-level metadata feature. The standardized four-dimensional feature vector is directly concatenated with the 768-dimensional final-layer FinBERT [CLS] representation and passed through a lightweight classification head. This design introduces only 1,024 additional trainable weights relative to a structurally matched text-only FinBERT model. RA-FinBERT was evaluated against text-only FinBERT and a lightweight DistilBERT baseline for three-class sentiment classification of financial-news titles and descriptions. On the held-out test set, RA-FinBERT achieved 69.89% accuracy and a macro F1 score of 0.634, compared with 63.44% and 0.526 for text-only FinBERT. Neutral-class recall increased from 18.18% to 45.45%. The framework supports both CPU and GPU execution, offering a lightweight and practical approach to financial sentiment classification under constrained computational resources. These findings indicate that rule-derived sentiment information and source metadata can provide complementary signals to contextual FinBERT representations and improve performance with minimal additional model complexity.

---


### 391. [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](https://arxiv.org/abs/2608.09836)

**<font color=#1a73e8>作者：</font>** Zichao Yu, Chengzhi Yu, Shengze Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has emerged as a core component of modern LLM post-training pipelines, yet we reveal a failure mode: degenerate agreement, where students exploit repetitive loops to achieve near-perfect token agreement with the teacher despite globally flawed responses. We therefore shift our focus from agreement to teacher-student mismatch, and find that mismatch tokens can be mainly categorized into two types: student-excess tokens and student-deficit tokens. Student-excess tokens are generated by the student but assigned near-zero probability by the teacher; their log-ratio corrections grow unbounded and destabilize the update. Student-deficit tokens, in contrast, are preferred by the teacher but rarely sampled by the student; their absence blocks the transfer of the teacher's reasoning patterns. To tackle these mismatch directions, we propose TIDE (Token-level Independent Deficit-Excess correction), which applies bounded Hellinger shaping to suppress the most severe sampled excesses and an analytic teacher top-$K$ injection to restore deficient probability mass without requiring deficit tokens to be sampled. Across mathematical reasoning benchmarks with multiple Qwen3 teacher-student pairs, TIDE consistently outperforms standard OPD and recent token-selection and reward-shaping baselines. Moreover, the gains of TIDE are more pronounced under strong teacher-student mismatch, where it improves Avg@8 from 6.9% to 20.3%, reduces average response length by a factor of 3.6, and substantially reduces formatting failures. Code is available at this https URL

---


### 392. [From Diagnosis to Correction: Benchmarking and Improving Real-World Table Parsing](https://arxiv.org/abs/2608.09842)

**<font color=#1a73e8>作者：</font>** Jutao Xiao, Yuan Qu, Dongsheng Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent document parsers achieve table TEDS scores above 93 on OmniDocBench v1.6, yet community feedback and our audit reveal persistent failures on complex real-world tables. To quantify this gap, we introduce TableParseMap, a diagnostic benchmark of 916 real-world tables organized into five challenging scenarios and nine failure types. The strongest evaluated parser achieves only 85.03 TEDS, showing that aggregate benchmark scores conceal substantial weaknesses. Our analysis attributes these failures to three complementary limitations: large tables exceed the reliable processing scale of a single pass, weak or ambiguous visual cues hinder structure perception, and the reconstructed table may remain visually inconsistent with the image. We therefore propose DEC (Decompose--Enhance--Correct), a visual-consistency-guided agentic framework that improves frozen table parsers without retraining. DEC uses a general VLM as the controller: Decompose partitions large tables along structure-aware boundaries, Enhance exposes weak visual evidence and reparses transformed views, and Correct diagnoses and repairs residual errors. A Visual Consistency Gate (VC-Gate) selectively triggers intervention, while a Visual Consistency Ranker (VC-Ranker) verifies candidate updates and supports rollback without ground-truth HTML at inference time. We further derive a 1,977-table Consensus-Hard Set from 4,556 candidates through offline metrics and cross-model consensus. Across three frozen parsers, DEC improves TEDS by 1.57 points on average; on TableParseMap, gains reach 1.89 points overall, 2.62 on structural errors, and 5.66 on large tables.

---


### 393. [Generative AI for Encrypted Traffic Analysis: Synthetic Dataset Generation and Classifier Evaluation](https://arxiv.org/abs/2608.09852)

**<font color=#1a73e8>作者：</font>** Harshil Patel, Himanshu Garg, Aswani Kumar Cherukuri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network traffic analysis faces significant challenges with encrypted communications, primarily due to limited visibility into packet contents and the inherent imbalance in available datasets, particularly for anomalous traffic patterns. This paper addresses these challenges by exploring Generative AI (GAI) techniques to create realistic and balanced synthetic encrypted traffic datasets. Our approach incorporates feature analysis, clustering-based data generation, and comprehensive classifier evaluation to ensure synthetic data quality. We demonstrate that properly generated synthetic data can effectively supplement real- world datasets, achieving up to 93% performance when training classifiers compared to those trained on real data. The proposed methodology preserves critical statistical properties and feature correlations while enabling the creation of balanced datasets, ad- dressing the persistent challenge of anomaly underrepresentation in cybersecurity data. Along with the results we provide complete programming code designed and implemented in this work.

---


### 394. [Towards Expert-level Medical AI for Real-time Video Consultations](https://arxiv.org/abs/2608.09861)

**<font color=#1a73e8>作者：</font>** Mahvish Nagda, Jihyeon Lee, Matthew Thompson 等 40 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Audio-visual interaction is the standard for patient-physician consultations, enabling natural communication and effective assessment of illness through non-verbal cues. While text-based AI has shown promise, it discards essential perceptual dimensions and limits patients who cannot articulate symptoms in writing. Early efforts to extend medical AI to audio-visual interaction have demonstrated feasibility but not reached clinician-level performance. Here, we provide the first demonstration of expert-level AI in real-time clinical video consultations using AMIE (Articulate Medical Intelligence Explorer) in a video configuration. AMIE (Video) is a Gemini-based multi-agent system integrating low-latency dialogue, clinical reasoning, and real-time audio-visual perception. To guide development, we established a taxonomy and automated evaluations for clinical audio-visual cues in telehealth settings. In a randomized Objective Structured Clinical Examination (OSCE) study with 30 primary care physicians (PCPs), 15 patient actors and 100 clinical scenarios, we compared AMIE (Video), its text-only counterpart AMIE (Text), and PCPs consulting via video. Clinical evaluators rated AMIE (Video) on par or better than PCPs in history-taking, diagnosis, management, and physical observation and examination. Patient actors preferred AMIE's approach to assessing and explaining conditions, while PCPs were preferred for rapport and partnership building. In modality ablation, patient actors preferred AMIE (Video)'s interface over text chat for communicative effectiveness, convenience, and feeling understood. Limitations remain in fine anatomical precision, subtle affective nuances, and high-frequency movements. While further research is needed before real-world translation, these results mark an important milestone toward AI systems capable of augmenting care across the sensory complexity of clinical practice.

---


### 395. [Sci-VBench: Evaluating Knowledge- and Reasoning-Intensive Video Generation in Science Domains](https://arxiv.org/abs/2608.09873)

**<font color=#1a73e8>作者：</font>** Diandian Zhang, Tingyu Song, Lin Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Sci-VBench, a comprehensive benchmark for evaluating knowledge- and reasoning-intensive video generation across scientific domains. It contains 1,253 expert-annotated examples spanning 60 subjects across four core disciplines: Natural Science, Healthcare, Humanities & Social Sciences, and Engineering. Each example requires models to generate temporally rich videos that demand scientific reasoning and knowledge-grounded synthesis, going beyond surface-level visual plausibility. We further establish a rubric-based evaluation protocol. Our analysis shows that, under this protocol, both non-expert human evaluators and MLLM-as-Judge systems can achieve relatively high agreement with expert judgments, supporting reproducible evaluation at scale. We benchmark 16 frontier proprietary and open-source models and find that, while automatic perceptual-quality scores cluster tightly across systems, performance on Prompt Grounding and Scientific and Causal Correctness varies substantially, with a pronounced proprietary-open-source gap. These findings show that advances in visual realism have not yet translated into reliable modeling of scientific and causal dynamics.

---


### 396. [Financial Numerical Prediction and Allocation as Token Generation](https://arxiv.org/abs/2608.09880)

**<font color=#1a73e8>作者：</font>** Xu Ouyang, Moontae Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Financial prediction typically relies on task-specific regression, ranking, or policy heads, separating the language model from the numerical object ultimately evaluated. We investigate whether a causal language model can instead represent forecasts and decisions directly through constrained token generation. FinATOM introduces a unified, head-free interface for three-step stock-return forecasting and dynamic five-ETF allocation. The forecasting model autoregressively emits volatility-standardized return tokens and is trained with ordinal and ranking supervision followed by a one-epoch token-level policy stage. The allocation model generates normalized long-only weights; supervised fine-tuning imitates a causal mean--variance anchor, and DAPO-augmented GRPO optimizes realized 21-day Sharpe subject to anchor consistency. In 2023--2025 ETF tests, the allocation policy improves pooled gross Sharpe from 1.428 to 1.529 and net Sharpe under a 5-bp transaction-cost model from 1.394 to 1.494. The multimodal allocation input attains the highest three-period mean Sharpe of 1.540, with its clearest advantage in 2025. On FinTexTS, the SFT and policy strategies achieve 73.52\%/2.68 and 73.72\%/2.69 cumulative-return/Sharpe, respectively. These results support the feasibility of direct language-model token generation for financial numerical prediction and decision-making, while motivating broader tests across assets, regimes, and random seeds.

---


### 397. [SHE: Trajectory-driven Safety Harness Evolution for LLM Agents](https://arxiv.org/abs/2608.09885)

**<font color=#1a73e8>作者：</font>** Wanying Qu, Qinghua Mao, Yu Li 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The safety of large language model (LLM) agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime control. Existing safety mechanisms often treat the harness as a fixed deployment artifact, limiting their ability to evolve with emerging risks. Moreover, coupled functions across harness components obscure safety responsibility attribution, making localized evolution difficult. We propose Safety Harness Evolution (SHE), a framework that learns evolving safe boundaries from rollout trajectories. SHE decomposes the harness into four artifacts with explicit safety responsibilities, including the System Prompt, Rule Bank, Safety Memory, and Tool Policy, defining clear functional boundaries for localized evolution. Based on this decomposition, SHE introduces an attribution-guided evolution loop that converts trajectory failures into structured diagnoses, learns artifact-specific boundary refinements, and selects evolved harnesses through safety-utility validation. Experiments on Agent-SafetyBench demonstrate that SHE effectively enhances safety through harness evolution, achieving a 3.1x ASR reduction compared with static SafeHarness, while also improving benign utility. The evolved harness further generalizes to unseen risks on the held-out AgentHarm benchmark and transfers across agent models without additional evolution.

---


### 398. [Fusion Training for Mathematical Generalization in Large Language Models](https://arxiv.org/abs/2608.09893)

**<font color=#1a73e8>作者：</font>** Congfeng Cao, Pengyu Zhang, Jelke Bloem  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Thinking Mode Fusion (TMF) enables large language models to support both concise responses and long-form reasoning by unifying a non-thinking mode and a thinking mode within a single model. However, its training dynamics, including the \emph{data ratio} and \emph{training schedule} between the two modes, remain underexplored. In this work, we present a systematic study of TMF by analyzing the effects of the training schedule and data ratio between thinking and non-thinking modes. Focusing on mathematical problem solving, we construct a benchmark with multiple thinking-to-non-thinking data ratios and three training schedules. Our results reveal an asymmetric interaction between the two modes: increasing the ratio of non-thinking supervision reduces the accuracy of the thinking mode. We further show that different training schedules modulate this trade-off and that the optimal schedule depends on the data ratio. Finally, we quantify a negative correlation between non-thinking and thinking mode supervision, highlighting an inherent tension between these two modes. These findings provide practical guidance for designing effective TMF training settings. All code and data are released to support further research at: \href{this https URL}{\textbf{Fusion Bench}}.

---


### 399. [Consilience for Verifier-Free Test-Time Scaling](https://arxiv.org/abs/2608.09898)

**<font color=#1a73e8>作者：</font>** Lecheng Kong, Like Hui, Haitao Mao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling often uses an external verifier, such as compilers and test cases in coding or trained value functions in robotics applications, to obtain high-quality rollouts. Verifier-free test-time scaling (or VF-TTS) is gaining extensive attention as a mechanism to enhance Large Language Model (LLM) reasoning, primarily because we do not have access to such high-quality verifiers in many real-world applications. Among existing VF-TTS methods, confidence-based VF-TTS methods, which compute and rank rollouts solely by confidence, are particularly promising. Such methods introduce near-zero overhead for sample evaluation and require minimal access to internal model states, making the methods highly flexible across models and tasks.
In this paper, we demonstrate a critical limitation of existing confidence-based VF-TTS methods by showing that such methods catastrophically break down on complex tasks. We observe a very interesting phenomenon: uniformly high confidence frequently indicates a failure to explore, favoring confidently wrong answers. To address this, our core insight is that robust cognitive search requires a specific confidence trajectory pattern: such methods perform exploratory branching at the beginning, as manifested by low initial confidence, and converge to a high final confidence solution. To implement this insight, we introduce consilience, a novel selection framework that explicitly evaluates the temporal asymmetry of confidence in reasoning. We operationalize this via a combinatorial metric that actively penalizes high initial confidence while strictly demanding final certainty. Extensive experiments covering both graduate-level mathematics problems and free-form code generation demonstrate that consilience effectively outperforms existing baselines, validating our novel perspective on completion confidence.

---


### 400. [Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness](https://arxiv.org/abs/2608.09900)

**<font color=#1a73e8>作者：</font>** Tadanobu Chuyo Kamijo, Ori Rottenstreich, Javier Conde 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model evaluations typically focus on performance under nominal conditions, creating an illusion of capability where models comfortably walk a narrow, highly optimized generation corridor. In real-world deployments, however, complex system prompts, safety guardrails, and structural constraints continuously force models off this nominal path, driving a divergence between benchmark scores and deployment performance. To address this issue, we introduce Decoding-Level Taboo, a zero-prompt diagnostic stress test that intervenes directly in logit space at runtime, forcing models out of their nominal paths. By dynamically masking primary candidate tokens at word boundaries, Taboo forces machine circumlocution.
Evaluating Taboo across several open-weight model families reveals that off-path robustness is heavily influenced by both parameter scale and post-training instruction alignment, with robustness generally improving with model size and alignment. Beyond the results presented in this paper, Taboo provides a novel primitive for generating diverse synthetic datasets, stress-testing runtime safety guardrails, and auditing model reliability prior to real-world deployment.

---


> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
