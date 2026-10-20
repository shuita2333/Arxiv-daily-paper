# 🧠 大模型相关研究 | 2026年10月21日

> 本类共 **548** 篇论文：已确认 **507** 篇，待复核 **41** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

---

### 301. [Editing as Language: Teaching LLM Agents a Grammar for Native Context Editing](https://arxiv.org/abs/2610.25550)

**<font color=#1a73e8>作者：</font>** Yunlong Deng, Yan Li, Xing Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A synopsis in novels folds a story into a few lines; a function in code gathers many steps with a single execution. Context editing is native to language itself. In this paper, we propose the Native Context Editing (NCE) framework, which gives language model agents a grammar for natively editing their own context. By encoding context-editing operations in a grammar of dedicated special tokens, we teach the agents to invoke edits through the language itself. We train agents on iteratively constructed trajectory segments, with each teacher edit conditioned on the evolving context. This establishes context editing as an atomic and inherent capability of LLM agents, enabling them to dynamically modify their context as they generate responses over long-horizon reasoning and interaction. Compared with context-editing methods that learn to generate tool-use code within specific external harness environments, our approach integrates context editing as an internal mechanism of the model's native generation process, enabling better generalization across diverse real-world workflows. On four long-horizon agentic benchmarks (Terminal-Bench 2.0, SWE-bench Verified, SWE-bench Multilingual, and SWE-bench Pro), NCE improves the average task success rate over the base model by 5.6 percentage points for LongCat-Flash-Lite-Sparse and by 4.5 for Qwen3.6-35B-A3B, while reducing average token usage by 36% and 15%, respectively.

---


### 302. [Symbolic Constraint Agents: Mining Formal Tool-Call Constraints to Prevent Agent Errors](https://arxiv.org/abs/2610.25552)

**<font color=#1a73e8>作者：</font>** Jinu Lee, Shraddha Barke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Symbolic constraints (programmatic, deterministic checks for tool calls) enable deterministic verification of LLM agents' tool calls, but existing approaches primarily enforce predefined safety policies rather than tool dependencies in complex tool environments. We explore whether symbolic constraints can be mined from environments and observations beyond predefined policies, and whether they can improve end-to-end task performance. We present Symbolic Constraint Agents (SCA), a framework that mines symbolic constraints from API documentation, refines them against execution traces, and checks the agent's tool calls with an SMT solver at runtime. A violation triggers a natural-language warning or, when the valid replacement is uniquely determined, an automatic repair. On AppWorld, refinement raises error-detection F1 from 37.0 to 58.3 on GPT-5.5 traces and from 39.3 to 61.9 on Qwen3.5-27B traces. At runtime, repair raises GPT-5.4-mini's task success by 5.4 points under a 40-call budget and 9.8 points when environment errors are hidden, while removing 59--87\% of failed calls across models, and transfers to $\tau^2$-bench with gains of up to 5.6 points. These findings show that automatically acquired symbolic constraints can improve tool-calling reliability and task completion, particularly when failures are costly or difficult to diagnose.

---


### 303. [Narrow Decision Models: A System-1 Architecture for Calibrated, Typed Decisions](https://arxiv.org/abs/2610.25553)

**<font color=#1a73e8>作者：</font>** Carlos André Antunes, Aldry Albuquerque, Gabriel de Melo Schmith 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> System One models, introduced with TypeSafe's Jev, answer typed questions about a state with calibrated probabilities instead of generated text: choosing among options described in natural language (Choice), placing the state on an ordered scale (Score), or judging a yes/no statement (Noul). Jev is general-purpose: one set of weights, served as an API and adapted to a domain only through the request. We study the other end of the design space. A Narrow Decision Model (NDM) offers the same interface but is trained for the decisions of one organization, is small enough to run on its own infrastructure, and has an open architecture whose properties can be stated and tested. The state can be any text or structured record about which decisions are made; our running case is the routing of court communications. The architecture serializes a request as a prefix tree (the state, then each question, then each option) and runs a bidirectional encoder under a block attention mask with logical positions, so that each answer is, by construction, invariant to the order of its options and independent of the other questions asked. Routing through an organization chart is a composition of Choice decisions with an explicit "none of these" option. We describe training with proper scoring rules through a curriculum, calibration and abstention, decisions composed by rubrics, and a protocol that accepts or rejects the mechanism before held-out data is opened. A minimal validation on public and fictitious data shows that the invariances hold to rounding in a trained model, that a small instance routes on organization charts it has never seen well above lexical retrieval, and that, at equal compute, the block architecture reaches a lower loss than a pairwise cross-encoder. A first instance trained on real legal documents agrees with the LLM classifier in production on 91% of held-out documents.

---


### 304. [Learning Which Device to Call: Online Tool Grounding for LLM Agents in IoT](https://arxiv.org/abs/2610.25563)

**<font color=#1a73e8>作者：</font>** Yichen Liu, Xiaochong Jiang, Haoran Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Internet of Things (IoT) gives large language model (LLM) agents access to physical observations, but one requested capability is usually offered by several devices, and the agent's plan does not say which one to call. Existing work retrieves relevant tools and checks plan feasibility, without learning which eligible device returns a useful observation. Unlike previous works, we study online tool grounding: binding an already specified tool call to one physical endpoint under service cost and device participation constraints. We propose a framework that learns which physical device should execute each agent-issued call. It formulates selection as a contextual bandit problem and combines adaptive context partitions with hierarchical endpoint trees, so that execution feedback is reused across related requests and devices. Selection balances task success against service cost while respecting device capability, authorization, battery reserves, and availability. Gaussian reward aggregation provides an optional mechanism for protecting individual feedback values. Theoretical results establish a finite-horizon regret bound and differential privacy for released reward statistics under fixed, reward-independent assignments. In a simulated loading-dock workload, the proposed router achieves higher step success and better cost-adjusted service, at lower simulated device energy and latency, than nearest-device, advertised-quality, UCB1, and LinUCB selection.

---


### 305. [Design and Cross-Domain Evaluation of an Agent Execution Harness](https://arxiv.org/abs/2610.25568)

**<font color=#1a73e8>作者：</font>** Saurav Joshi, Manas Gupta, Ashwin Venkatesh Raman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Completing complex tasks with language-model agents requires coordinating planning, execution, and review so the final result addresses the user's original objective. We present an agent execution harness that keeps the original objective separate from a revisable plan and an execution record. A planner assigns scoped tasks, workers produce outputs and artifacts, and a reviewer examines results against the original request before submitting or requesting additional work. Reusable domain-specific instructions guide these roles and are refined during construction using task inputs and execution trajectories, without official grading feedback. We evaluate complete harness configurations across terminal tasks, clinical responses, application building, and scientific questions. On Terminal-Bench 2.1, the harness passes 83 of 89 instances (93.26%); on HealthBench Professional, a Fable-configured system achieves a length-adjusted rubric score of 69.63 across 525 tasks. In a 53-task paired HealthBench comparison, the Fable-configured harness achieves an aggregate score 19.89 points higher than direct completion, despite a $-1.46$-point median task-level change; mean inference cost rises from \$0.29 to \$2.13 per task. We combine these outcomes with latency, documented instruction revisions, and reviewer decisions. Evaluating outcomes alongside execution trajectories and resource use clarifies how coordination supports task completion, where it introduces regressions, and at what cost.

---


### 306. [DiffGround: Semantic Difference-Guided Zero-Shot Video Question Grounding](https://arxiv.org/abs/2610.25570)

**<font color=#1a73e8>作者：</font>** Cheng-Han Lee, Amir Salimi, Hsiang-Wei Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Question Grounding (VideoQG) requires both accurate question answering and precise temporal localization. Existing supervised methods rely on costly temporal annotations, while existing zero-shot approaches are primarily designed for Video Question Answering (VQA) and are not optimized for temporal grounding. We propose DiffGround, an action-driven zero-shot framework built upon frozen Multimodal Large Language Models (MLLMs). Our framework first predicts an answer-relevant action cue that transforms the input question into an explicit semantic target for grounding. Action Cue converts a reasoningoriented question into an action-centric retrieval query. Guided by the action cue, a Vision-Language Model (VLM) efficiently selects informative keyframes for reasoning. Finally, we introduce Semantic Diff Refinement, a training-free temporal refinement method that exploits semantic differences between neighboring SigLIP2 embeddings to recover complete action segments from sparse predictions. Extensive experiments on NExT-GQA and STAR show that DiffGround consistently outperforms existing zero-shot and supervised methods, establishing a new state of the art for Video Question Grounding.

---


### 307. [Representations in Motion: Layer-wise Rotation and Trajectory Divergence in LLMs](https://arxiv.org/abs/2610.25574)

**<font color=#1a73e8>作者：</font>** Zhuonan Yang, Yik Siu Chan, Wannan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work suggests that activation dynamics--how representations change during inference--might be more revealing about language model behavior than static readouts from individual layers. In this work, we investigate the layer-wise evolution of representations of factuality, using true and false statements when the model is prompted to either lie or to be honest. We report a geometric phenomenon in which the factuality directions extracted from the lying and honest conditions appear to rotate away from each other across layers. We find that such layer-wise rotation also occurs in a task that requires the model to take different visual perspectives in the 3D world, suggesting that the rotation phenomenon might be indicative of manipulating conceptual spaces in general, rather than unique to factuality. We then investigate the "real time" transformation of conceptual representations on a trial-to-trial basis. We show that it is possible to make strong predictions about the model's target task and behavior from trajectories alone. In addition, diverging points in single-trial trajectories correspond to the onset of rotation in aggregated-trial analysis. Finally, we show that both rotation and divergent trajectories occur in more naturalistic settings in which models are not overtly prompted to "lie" but rather report false statements in the course of completing a different task.

---


### 308. [Benchmark for Structured Retrieval-Augmented Generation in Perovskite Photovoltaics](https://arxiv.org/abs/2610.25575)

**<font color=#1a73e8>作者：</font>** Qiwei Han, Chi Zhou, Gaoxiang Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While retrieval-augmented language models increasingly serve as literature assistants in the physical sciences, existing benchmarks evaluate them primarily on qualitative text overlap or through model-based scoring rather than against verified experimental ground truth. In experimental materials disciplines such as perovskite photovoltaics, however, the most critical inquiries are inherently quantitative and aggregate measurements across dozens or hundreds of papers. Here, we present a quantitative question-answering benchmark where all 755 ground-truth answers are computed directly from 45,441 measured device records (40,889 human-curated records through 2021 and 4,552 records extracted from 2022-2026 literature). Benchmarking six retrieval architectures over 158,274 passages from 25,662 papers using an open 14B model on a single 24 GB GPU, standard passage retrieval tops out at 16-23% accuracy (compared to 1.6-6.5% zero-shot). In contrast, equipping the language model with read-only SQL execution over the structured device table elevates accuracy to 51.5% on historical and 50.8% on prospective literature -- a 33.01.8 percentage-point advantage over hybrid text retrieval. Aggregate queries spanning extrema, distributions, and filtered record counts prove virtually unsolvable via text retrieval alone, demonstrating that systematic table extraction is an operational prerequisite for literature-scale quantitative inquiry.

---


### 309. [Finite Interaction Lens: Structured Precision Sharing for Vision-Language Models](https://arxiv.org/abs/2610.25577)

**<font color=#1a73e8>作者：</font>** Nozomu Fujisawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying which visual interventions interact in a vision-language model requires comparing their joint and separate effects. The resulting four-output difference can be small enough for rounding error to obscure it. We introduce the Finite Interaction Lens (FIL), a mixed-precision method for evaluating finite intervention families. At each selected linear projection, FIL decomposes each candidate's input into a native state, two single-intervention components, and a full-dimensional mixed residual. It projects the single-intervention components at higher precision and reuses the same numerical contributions in the joint candidates, while retaining every mixed residual and nonlinear trajectory. We derive a local cancellation identity and a conditional bound on error propagation through a smooth nonlinearity. In one MLP of Qwen3-VL-4B-Instruct, FIL reduces final interaction MSE by 94.4% on 16 synthetic families and by 99.85% and 99.35% in two separate four-image COCO studies, relative to a control that has the same nominal BF16-product budget and higher-precision single interventions but projects each joint candidate independently. One image accounts for most of the absolute gain in each COCO study. Higher-accuracy multi-product BF16 arithmetic on all candidates gives lower aggregate error at similar total query times. Single-product BF16 already recovers the reference choices in both candidate-selection tasks we tested. On these development inputs, FIL improves interaction fidelity at a fixed nominal precision budget. Its practical value depends on a task that needs the extra fidelity.

---


### 310. [Assertion and Belief: Moore's Paradox in Language Models](https://arxiv.org/abs/2610.25586)

**<font color=#1a73e8>作者：</font>** Anshun Asher Zheng, Weili Cao, Fangcong Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Moore's paradox \citep{moore1942} concerns sentences such as ``It is raining, but I don't believe that it is,'' which may well be true yet cannot be sensibly asserted. The absurdity lies not in the content but in the act, since to assert is to vouch for one's own belief. This makes the paradox a test of whether language models take the speech act into account when computing meaning. We present the first test of Moore's paradox in LLMs, evaluating 12 models on a curated set of Moorean sentences in varied contexts. We find that models largely recognize the infelicity of Moorean sentences, and that the judgement is not tied to a memorized form and tracks the speech act. Using the Rational Speech Act framework (RSA; \citealt{goodmanfrank2016}), we then test whether these judgements arise from a listener reasoning about a speaker. We find the models' own listeners do not reason about their own speakers, and their reasoning traces suggest that they instead recall knowledge about the paradox and apply rules therein. The models thus appear to have learned the paradox as a fact about sentences, not as a requirement on speakers.

---


### 311. [Divergence based Ranked Preference Alignment for LLMs](https://arxiv.org/abs/2610.25588)

**<font color=#1a73e8>作者：</font>** Rajdeep Haldar, Yue Xing, Qifan Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Alignment of large language models typically relies on pairwise preference feedback, though ranked feedback can capture more comprehensive information across multiple responses within a single annotation. However, ranked-preference alignment is underexplored in practice compared to simpler pairwise approaches, potentially resulting in suboptimal behavior. Concurrently, recent research has conceptualized large language model alignment objectives as divergence estimators between aligned (preferred) and unaligned (less-preferred) response distributions, resulting in a family of objectives with an interpretable theoretical foundation and strong empirical performance. This work unifies these perspectives by introducing $f$-RPO, a $f$-divergence objective for ranked preference optimization that extends divergence-based alignment to ranked feedback and recovers pairwise preference alignment as a special case. Our theoretical analysis establishes rank-order consistency, showing that $f$-RPO preserves the underlying preference ordering at convergence. Empirical results indicate that total-variation and reverse-KL variants of the proposed objective consistently outperform ranked-alignment baselines in both ranking and generation quality across Qwen, Llama, & Gemma models ranging from 0.5B to 8B parameters.

---


### 312. [ViMoLa: Discrete Motion Tokens for Language-Guided Video Generation](https://arxiv.org/abs/2610.25595)

**<font color=#1a73e8>作者：</font>** Bishoy Galoaa, Sarah Ostadabbas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-guided video generation often captures scene content while missing the requested motion. We present ViMoLa (Video Motion Language), which predicts a motion prior from language and injects it into a frozen image-to-video backbone. A spatial vector-quantized autoencoder compresses dense trajectories into 64 tokens from a 512-entry codebook; a 28M-parameter transformer predicts the tokens from text; and zero-gated cross-attention adapters condition every frozen Wan~2.2 DiT block through forward hooks. Trained on 462K videos from Something-Something~v2 and Kinetics-400, ViMoLa raises directional accuracy from 0.287 to 0.442 (chance 0.250), with similar measured generative quality. Across-prompt shuffled codes achieve 0.283, supporting the importance of prompt-matched token content. A low-rank adapter reaches 0.428 at 1.45% additional forward-pass FLOPs, and reusing the tokenizer and language model with newly trained CogVideoX adapters raises accuracy from 0.301 to 0.398. Control remains imperfect: oracle codes reach 0.531, compound-motion gains are smaller, and the adapter does not explicitly preserve token-to-patch assignments.

---


### 313. [Cognitive Map in Large Language Models](https://arxiv.org/abs/2610.25596)

**<font color=#1a73e8>作者：</font>** Albert Qin, Jonathan Cohen, Gautam Reddy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> It has long been proposed that animals construct cognitive maps to support flexible behavior in novel environments. We tested whether large language models form similar representations using relational reasoning tasks and causal "mosaic experiments" that manipulate internal activations in open-weight language models. Models beyond the ten-billion-parameter scale successfully inferred unstated relationships between entities and generalized to synthetic entity names. Across model and task families, models generated abstract representations of relational structure and combined them additively with representations of entity identity, binding entities to roles within that structure. Models stored observed relationships as pairwise links that they composed retrospectively when queried, rather than prospectively positioning each entity in a global coordinate system. Binding was mediated by a sparse, distributed set of key--value pairs; by perturbing these pairs, we implanted "false memories" that altered model behavior in predictable ways. Overall, our findings reveal an internal organization analogous to a cognitive map that explains how language models reason with limited information.

---


### 314. [Text Dominance in Paralinguistic Conflict: Tracing Suppression Through Audio LLM Circuits](https://arxiv.org/abs/2610.25599)

**<font color=#1a73e8>作者：</font>** Ankur Banerjee, Vishnu Guntakala, Danity Pike 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Audio LLMs deployed in settings such as crisis hotlines and customer support are only useful beyond speech-to-text pipelines if they use acoustic cues rather than the transcript alone. We test whether they prioritise transcript content over paralinguistic cues (emotion, speaker identity, sarcasm) and trace the mechanism when they do. Across six audio LLMs under LISTEN-style conflict conditions, the mean text-dominance rate on mismatched text+audio items is 0.78 (0.86 excluding sarcasm). In the most text-dominant screened model, probing shows speaker identity remains linearly decodable at ceiling at the language model's input, so the failure is not perceptual. Back-patching, reported to repair lexical text dominance, has no measurable effect here; but it also fails on its own source task in our replication (n=300), so we treat its null as uninformative rather than as evidence of non-transfer. Attention knockout partially restores audio-grounded output by blocking the claim from propagating through intermediate tokens during open-ended generation, whereas blocking the answer position's direct connection to the conflicting claim has no effect. The claim's influence therefore travels through an intermediate relay rather than a single severable edge. The effect appears only in free-form generation and not in closed-set multiple choice, suggesting that benchmarks relying on that format may be systematically blind to interventions of this kind. Code and data are publicly available at this https URL.

---


### 315. [Safety Offset Learning: When Benign Fine-Tuning Misaligns LLMs](https://arxiv.org/abs/2610.25611)

**<font color=#1a73e8>作者：</font>** Jesson Wang, Zhanhao Hu, Minghao Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety risks from fine-tuning are commonly characterized by the harmfulness of the training data:harmful fine-tuning is considered dangerous, while benign fine-tuning is often assumed to preservealignment. We argue that this view misses a more fundamental factor-the behavioral transition inducedby supervision. Harmful fine-tuning and safety-degrading benign fine-tuning can both be understoodas learning the same refusal-to-compliance transition, but on different data distributions. We studywhether such a transition learned on benign inputs can generalize to harmful requests. We constructbenign examples that an aligned model initially tends to refuse and pair them with their originalharmless responses, creating a discrepancy between the model's initial refusal and the supervisedanswer. Fine-tuning on these examples increases harmful compliance, but only when two conditionshold together: the discrepancy is large enough, and it cannot be resolved through a narrow surface-levelshortcut. With the induced discrepancy matched, varying only whether it is localized changes harmfulcompliance by an order of magnitude; raising the discrepancy does not help while a shortcut remainsavailable, and removing the shortcut does not help while the discrepancy is small. Building on thisobservation, we introduce SAFEOFF, a dataset of benign instructions rewritten to raise the alignedmodel's refusal likelihood and paired with their original answers. Across three aligned LLMs and threesafety benchmarks, SAFEOFF substantially weakens safety alignment despite containing no explicitharmful supervision, suggesting that fine-tuning safety depends not only on what data a model sees, butalso on which behavioral boundary the supervision moves.

---


### 316. [Curriculum Learning Teaches LLMs Long-Horizon Implicit Reasoning, Up To A Limit](https://arxiv.org/abs/2610.25612)

**<font color=#1a73e8>作者：</font>** Jimson Huang, Maxwell Nickell, Ruowang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs "reason" by externalizing intermediate steps as tokens through chain-of-thought (CoT), yet even frontier reasoning models hit abrupt performance cliffs on long-horizon tasks. Implicit reasoning (reasoning within a single forward pass) is useful during CoT generation, as the model can "search ahead" to decide the correct next move without explicit search. Models with weak implicit reasoning are more likely to commit to wrong paths and must attempt to recover via backtracking, while models with strong implicit reasoning identify the correct proof strategy directly, shortening the CoT. However, prior work shows LLMs struggle to reason implicitly beyond shallow depths, with no relief from scale. We investigate whether curriculum learning can extend this depth by fine-tuning on examples with progressively increasing vocabulary size and lookahead (the number of steps a model must search ahead to identify the correct next move). At matched compute, curriculum-trained models achieve lookaheads where no-curriculum training fails. Qwen3-0.6B reaches 98% accuracy on problems with lookahead up to 256 with curriculum, compared to 45% without. However, progress slows as fine-tuning continues, following a saturating exponential that suggests a maximum intrinsic lookahead to which models can learn to reason implicitly. Larger models reach higher fitted ceilings, fine-tuning pretrained models far outpaces training from scratch, and curriculum step sizes that are too large stall progression. Finally, the capability acquired on synthetic data transfers to natural language reasoning, with curriculum-trained models outperforming models trained without curriculum at matched compute on 11 natural language reasoning benchmarks.

---


### 317. [Zephyrus-R1: Agentic Reinforcement Learning for Weather Reporting](https://arxiv.org/abs/2610.25625)

**<font color=#1a73e8>作者：</font>** Fengfei Yu, Marshall Fisher, Isadora White 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has emerged as a key method for training AI models in scientific applications, but RL remains difficult when outputs cannot easily be verified against a known ground-truth answer. Natural-language weather forecast reports are one such domain: they translate atmospheric data into assessments of weather evolution, hazards, and uncertainty for both the general public and key decision-makers. Unlike numerical weather-analysis questions, they admit many valid outputs, which limits deterministic verification. To address this, we develop Zephyrus-R1, a practical framework for RL on scientific weather forecast reporting. We focus on three key components of the agentic RL pipeline: reward design, curriculum learning, and an analysis of human-expert alignment. To encourage both report legibility and factual accuracy, we design a reward function that combines a meteorological rubric with bidirectional claim entailment, both evaluated against National Weather Service reference reports. Our framework optimizes this reward in a simulated tool-calling environment, enabling vision-language agents to gather and analyze forecast evidence across regions and lead times before producing a report. We use annotations from three meteorologists to audit the claim labels produced by our LLM judges. Finally, a curriculum helps small models first develop tool use and scientific reasoning through RL on verifiable weather-analysis questions, then optimize the open-ended report reward. After training Qwen3.5-4B with Zephyrus-R1, we improve the mean across six judge-metric scores by 26% over the base model and achieve results competitive with frontier open-weight models. For Qwen3.8-27B, we improve the same mean by 13% over the base model, by 6.7% over Kimi-K3, and by 2.7% over GPT-5.6-Luna.

---


### 318. [MapSteal: Map-based Autonomous Knowledge Stealing Attack Against Large Language Models](https://arxiv.org/abs/2610.25626)

**<font color=#1a73e8>作者：</font>** Zhengao Li, Chuxu Zhang, Yushun Dong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge acquisition from black-box large language models (LLMs) offers a practical approach to adapting smaller student models. However, many existing methods rely on predefined queries or student feedback to guide acquisition, leaving autonomous expansion of knowledge targets an important challenge. We propose \textbf{MapSteal}, a student-independent framework for structured recursive knowledge acquisition. Starting from a small set of initial roots, MapSteal represents acquisition targets using structured states and recursively expands them through teacher-proposed directions. Question realization, proposal admission, and deduplication constrain the acquisition process, while root-aware scheduling organizes exploration under a fixed QA budget. The resulting question--answer pairs are used to adapt student models without requiring student feedback during acquisition. Experiments with Qwen3.5 students at 2B, 4B, and 9B scales show competitive downstream performance across six medical and cybersecurity benchmarks. On the 4B medical evaluation, Full MapSteal improves average accuracy by 1.17 percentage points over a simplified recursive acquisition variant. Cross-domain evaluations show that gains depend on the domain and evaluation panel. These results demonstrate the feasibility of structured, student-independent recursive acquisition while highlighting the distinction between generating acquisition targets and obtaining useful training supervision. Our code is available at \href{this https URL} {this https URL}.

---


### 319. [Think, Compress, Answer: Reinforcement Learning for Multimodal Grounding via Reasoning Compression](https://arxiv.org/abs/2610.25640)

**<font color=#1a73e8>作者：</font>** Jinbae Seo, Hyeongjun Kwon, Jiyoung Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extended reasoning has substantially improved multimodal large language models (MLLMs) on tasks requiring compositional and relational inference. However, multimodal grounding imposes a distinct requirement: reasoning must ultimately converge on a target-specific compact representation that supports precise localization. As reasoning trajectories grow longer, they often expand into broad scene narratives and peripheral relational details, which can dilute grounded perceptual evidence and lead to ambiguous or incorrect predictions. Motivated by the information bottleneck principle, we propose Think-Compress-Answer (TCA), a reinforcement learning framework that decomposes multimodal grounding into three phases: free-form reasoning, target-aware context compression, and answer generation conditioned on the compressed context. TCA is optimized through a multi-stage Group Relative Policy Optimization (GRPO) with progressive rewards that establish the structured output protocol, minimize reasoning-specific information while preserving target-relevant content, and directly improve localization accuracy. This staged design enables MLLMs to retain the benefits of extended reasoning while distilling it into the minimal context required for grounding. Experiments across six multimodal grounding benchmarks show that TCA attains substantial zero-shot performance gains, demonstrating the effectiveness of reasoning compression.

---


### 320. [Consistency Training Suppresses Cue Following Without Teaching Cue Selectivity](https://arxiv.org/abs/2610.25650)

**<font color=#1a73e8>作者：</font>** Prakhar Gupta, Terry Jingchen Zhang, Zhijing Jin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models often change answers because of a cue, a hint such as "I believe the answer is B" that gives no valid evidence. Consistency training (CT) trains a model to answer the same with and without the cue. Four CT methods apply this idea to output tokens (BCT), residual activations (ACT), attention patterns (AttCT) and sampled-answer rates (RMCT). Prior work suggests some learn different solutions. We train all four on Gemma-2-2B-it and Llama-3.1-8B-Instruct with the same data. We test predictions written in advance and inspect the models with a known circuit that carries cues to the answer. All four make the trained cue less effective, and their fixes share three properties. First, correct cues lose about as much influence as wrong ones. Second, the fix is usually large for cues before the answer options, as in training, and much smaller after them. Llama RMCT depends least on position. Third, the circuit heads still carry most remaining cue-induced errors. Making BCT targets depend on the cue's correctness mostly weakens the fix. CT thus weakens the trained cue without teaching models when a cue is right. Evaluations with only wrong cues at the trained position miss the first two properties.

---


### 321. [OPDArena: Understanding Learning and Forgetting in On-Policy Distillation](https://arxiv.org/abs/2610.25651)

**<font color=#1a73e8>作者：</font>** Yuanze Xu, Tianzhu Ye, Hui Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is increasingly used for language model post-training, yet how teacher supervision shapes learning and forgetting remains unclear. We present OPDArena, a framework comparing supervised fine-tuning (SFT), reinforcement learning with verifiable rewards (RLVR), and OPD across five pretrained models and diverse teacher sources. It jointly evaluates mathematical learning, general capability retention, and predictive distribution changes. Teacher choice strongly shapes retention: students of RLVR-trained teachers improve on the target task while retaining prior capabilities, whereas students of SFT-trained teachers incur greater capability loss. Across post-training methods, out-of-domain (OOD) distribution change shows a more consistent positive association with forgetting than in-domain change. To understand how teacher choice affects these changes, we examine the additional information teachers provide relative to the student's pretrained model. Controlled teacher comparisons show that the task-specific preferences teachers acquire through post-training make student updates more concentrated in-domain.

---


### 322. [LIRQuant: An Efficient Locally Isolated Rotation Quantization Method for Large Language Models](https://arxiv.org/abs/2610.25675)

**<font color=#1a73e8>作者：</font>** Desheng Xu, Hanglin Li, Tianchen Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-Training Quantization (PTQ) enables efficient deployment of Large Language Models (LLMs), yet activation outliers remain a key challenge for low-bit quantization. Existing global transformation methods overlook heterogeneous channel sensitivity to quantization noise, leading to suboptimal accuracy-efficiency trade-offs. To address this, we propose \textbf{Locally Isolated Rotation Quantization (LIRQuant)}, a sensitivity-aware framework that selectively applies transformations. LIRQuant identifies sensitive channels using a noise-weighted sensitivity metric, applying expressive learnable rotations only to these channels and lightweight fixed rotations to the remaining ones. This decoupled design reduces optimization complexity without sacrificing outlier smoothing capability. Extensive experiments across the LLaMA-2/3, Mistral, Qwen3, and Mixtral families demonstrate that LIRQuant achieves state-of-the-art accuracy under the challenging W4A4KV4 setting. Meanwhile, LIRQuant calibrates LLaMA-3-8B in only 25 minutes with 20.3 GB peak GPU memory, achieving the fastest calibration and the lowest memory footprint among recent learnable-rotation methods, and its fused inference kernels deliver up to $2.3\times$ prefill speedup and $3.5\times$ memory saving over FP16.

---


### 323. [Neither Over- nor Under-Constrained: Evaluating LLM Personalization under a Constraint Qualification Audit](https://arxiv.org/abs/2610.25676)

**<font color=#1a73e8>作者：</font>** Xuran Li, Guanqin Zhang, Imran Razzak 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate evaluation of LLM personalization is hindered by current evaluation paradigms that over- or under-constrain the response space, yielding frequent false rejections and false acceptances. To reduce these false rates, we introduce ConQual-Audit, an audit-based framework that evaluates LLM personalization through a three-stage process: (1) extracting semantic constraints from user profiles and task-grounded reference; (2) qualifying constraints by pruning unnecessary constraints and recovering missing constraints; and (3) verifying candidate responses against the audited constraints via natural language inference. Across PrefEval and LaMP, ConQual-Audit outperforms nine baselines, attaining top AUCs (0.88 and 0.90) and the lowest false rate (0.21) on the leanest constraint sets at an amortizable audit cost. Crucially, this constraint audit is portable: integrating it into ExPerT and PREF helps revise smaller, higher-quality constraint sets to reduce their evaluation false rates.

---


### 324. [LOOP: Recovery-Aligned Iterative Layer Pruning via On-Policy Distillation](https://arxiv.org/abs/2610.25679)

**<font color=#1a73e8>作者：</font>** Liang Xu, Shufan Shen, Zhongni Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Layer-level pruning is attractive for large language model (LLM) deployment as it reduces the model size while preserving a dense architecture that can be efficiently executed on standard hardware. Current methods typically follow a one-shot paradigm, which first removes selected layers to reach a target model size and then performs additional training to recover model capabilities. However, pruning directly to the target size can substantially degrade reasoning capabilities, making subsequent recovery more difficult under a limited training budget. Moreover, this paradigm separates layer selection from recovery, limiting the use of recovery information to guide selection and potentially hindering the recovery of reasoning capabilities. To address these limitations, we propose LOOP, a Layer-level Recovery-Oriented On-Policy Pruning framework that interleaves pruning and recovery across multiple shots. In each shot, LOOP removes a single layer and performs short on-policy distillation, mitigating the abrupt degradation in reasoning capabilities associated with one-shot pruning. To guide layer selection in subsequent shots, LOOP reuses on-policy trajectories and optimization signals from recovery to jointly assess each remaining layer's reasoning contribution and recovery sensitivity, thereby making layer selection recovery-aware. Evaluations on several benchmarks show that LOOP consistently outperforms one-shot baselines in average accuracy across different model scales and pruning ratios.

---


### 325. [When Safety Fails Collectively: Robust Alignment Against Harmful Fine-Tuning via Joint Weight Perturbations](https://arxiv.org/abs/2610.25683)

**<font color=#1a73e8>作者：</font>** Zhiyuan Wang, Yuezhi Zhou, Zhu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harmful fine-tuning can rapidly erode the safety alignment of large language models, creating substantial risks when aligned models are adapted to downstream tasks. Existing alignment-stage defenses use harmful examples and simulated harmful perturbations during safety alignment to prepare models for later harmful fine-tuning, yet the collective effects of harmful weight perturbations remain underexplored. We identify a collective failure pattern: disjoint parts of a harmful perturbation have limited effects in isolation, but their joint application increases the model's harmfulness beyond the sum of their individual effects. Guided by this observation, we propose Joint Weight Perturbations (JWP), an alignment-stage defense that masks different parts of a harmful perturbation estimated from the current model and trains the model to respond safely in the resulting states. This exposes the model to different combinations of harmful perturbations and reduces its sensitivity to their accumulation during subsequent harmful fine-tuning. Experiments across downstream tasks and model families show that JWP offers stronger resistance to harmful fine-tuning than prior defenses while largely preserving task performance.

---


### 326. [ToolOPD: Credit-Aware On-Policy Distillation for Tool-Use Agents](https://arxiv.org/abs/2610.25693)

**<font color=#1a73e8>作者：</font>** Chu Zhao, Lei Tang, Yanming Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) enhances the capabilities of small language agents by providing dense, token-level supervision from a teacher model on student-generated trajectories. However, standard OPD implicitly assumes that credit is uniformly distributed across long-horizon trajectories, assigning the same strength of teacher supervision to different actions. Through credit-distribution analysis and outcome-reversal counterfactual experiments, we find that trajectory credit is concentrated on a small number of critical actions. Moreover, even when the trajectory is held fixed, reversing only the final outcome substantially changes the credit assigned to multiple interaction turns. These findings show that the uniform-credit assumption fails to identify critical decisions and ultimately degrades the model's reasoning accuracy. To address these challenges, we propose ToolOPD, an outcome-aware on-policy distillation framework designed for long-horizon tool use. ToolOPD first summarizes each completed trajectory and its outcome into a reusable hindsight skill. It then measures how this skill changes the teacher's probability of each student action token and converts the change into outcome-aware credit. The resulting credit preserves supervision that supports successful decisions or discourages failed ones, while suppressing irrelevant and conflicting signals. ToolOPD uses these credits to reweight the action-level distillation loss and jointly optimizes it with reinforcement learning. Extensive experiments across multiple long-horizon tool interaction benchmarks demonstrate that ToolOPD significantly outperforms existing reinforcement learning and self-distillation baselines.

---


### 327. [CVaR-RMD: CVaR Selection Pressure for Robust Metaheuristic Discovery](https://arxiv.org/abs/2610.25697)

**<font color=#1a73e8>作者：</font>** Ruodai Cui, Li Niu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have recently been used to discover heuristics through iterative program search, offering a promising approach to automated algorithm design. However, candidates selected by average performance may degrade across instance families, random seeds, and problem scales because mean-based objectives can obscure rare but severe failures. We propose CVaR-RMD, a risk-sensitive evolutionary framework that uses an LLM to mutate executable heuristic programs and ranks candidates by empirical conditional value-at-risk over heterogeneous evaluation conditions. Across three combinatorial optimization domains, CVaR-based selection improves upper-tail performance and reduces failure rates while maintaining competitive mean performance. These gains persist on larger unseen instances and independently curated within-domain benchmarks

---


### 328. [From Black Box to Controller: Inference-Time Steering of LLM via Feature Amplification](https://arxiv.org/abs/2610.25700)

**<font color=#1a73e8>作者：</font>** Keqi Chen, Zekai Sun, Yuhua Wen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inference-time steering is crucial for deploying Large Language Models (LLMs) in real-world applications, where they must flexibly adjust behavior preferences. For instance, a model should dynamically adjust its caution level based on the risk of the scenario. This requirement introduces a challenge: modulating the intensity of LLM preferences. Prompt engineering can require task-specific prompt design, while fine-tuning requires additional optimization and data. These requirements can make repeated behavioral adjustments costly. To address this, we introduce NeuroSteer, a plug-and-play framework that enables flexible, quantitative adjustment of LLM preferences at inference time. NeuroSteer employs a Sparse Autoencoder (SAE) as its controller. Comparing neuron activation frequencies between positive and negative examples isolates "feature neurons" that correspond to target preferences such as politeness and positive sentiment. During inference, the activations of selected SAE features are amplified in the latent representations to steer the output distribution. Users can adjust the strength of this steering on a per-scenario or per-user basis, granting the LLM fine-grained, quantifiable trait modulation. Our experiments show that NeuroSteer can alter sentiment, toxicity, stance, and politeness at inference time. It achieves higher target-direction steering scores than the compared baselines in several settings, with task- and strength-dependent trade-offs in generation quality.

---


### 329. [How Effectively Do Security Skills Guide Coding Agents in Vulnerability Detection in Linux Kernel?](https://arxiv.org/abs/2610.25705)

**<font color=#1a73e8>作者：</font>** Haoran Xue, Nikta Akbarpour, Gias Uddin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) coding agents, such as Claude Code, are increasingly used for security auditing, with task-specific skills providing reusable vulnerability-analysis procedures. However, their effectiveness in detecting real vulnerabilities and the reasons for their failures remain unclear. We conduct the first large-scale empirical study of 37 security skills using Claude Code with four underlying LLMs on 100 real Linux kernel vulnerabilities across ten classes, totaling 14800 runs. We evaluate vulnerability detection at the function, statement, and vulnerability-class levels. Results show that 24.4 percent of runs locate the correct function, 18.3 percent identify both the function and responsible statement, and 15.7 percent correctly classify the vulnerability. Our failure analysis reveals limitations in evidence acquisition, state-relation reasoning, code interpretation, candidate verification, investigation coverage, and reporting. Based on these findings, we propose SKILL-SIF, a self-improving framework that iteratively evolves security skills by learning from missed vulnerabilities and failure patterns. We evolve five top-performing skills using the original benchmark and evaluate them on 100 previously unseen vulnerabilities. SKILL-SIF improves fully correct vulnerability detection by up to eight times (from 2 percent to 16 percent) on unseen vulnerabilities, while aggregate accuracy across four LLMs increases by 1.85 times (from 6.05 percent to 11.20 percent). These findings highlight the limitations of existing security skills and demonstrate the potential of failure-driven skill evolution to improve vulnerability detection in coding agents.

---


### 330. [Whose Credential Is It? How Owner Attribution in Agent MemoryShapes Cross-User Account Misuse](https://arxiv.org/abs/2610.25707)

**<font color=#1a73e8>作者：</font>** Hau-Sing So, Daixian Liu, Carl Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shared long-term memory lets an LLM agent serving one user inadvertently retrieve another user's credentials, but it is unclear when such exposure leads to actual harm. We introduce a three-stage audit that separates three events: a foreign credential reaches the prompt (exposure), the agent acts with it (behavior), and the other user's account changes (state). In AppWorld, a store that mixes 763 past logins from all users retrieves another user's credential for 84.7 percent of required apps, yet agents rarely act on it. Misuse appears in a stress test where memory lacks the user's own credential and presents a single foreign one as the user's record: seven agents then use it in 80 to 94 percent of runs and change the victim's account in up to 43 percent, sometimes passing the official check. Naming the owner before or inside each credential line prevents most of this: with all else fixed, misuse falls from 92 to 1 of 305 paired runs, also with name-free usernames, though owner-bound notes cost 3 to 5 successful tasks per model on clean memory. A wrongly written owner largely restores misuse; trailing owner tags and added safety instructions help only some models. Agent memory should consistently record whose credential it stores, and evaluations should measure behavior, not only exposure.

---


### 331. [PFedQFT: Personalized Federated Quantum-Inspired Fine-Tuning for Medical Large Language Models](https://arxiv.org/abs/2610.25712)

**<font color=#1a73e8>作者：</font>** Qihan Huang, Lingxia Zhang, Guye Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical data remain fragmented across institutional silos because of privacy, governance, and ownership constraints. Federated learning enables medical institutions to adapt large language models (LLMs) collaboratively without transferring raw records. However, independently parameterized low-rank adapters incur repeated parameter and communication costs across Transformer projections, while uniform aggregation may limit adaptation to heterogeneous institutional data. We propose PFedQFT, a quantum-inspired framework for personalized federated fine-tuning with a compact shared adapter. Specifically, PFedQFT constructs reusable orthonormal adaptation bases from compact skew-symmetric generators using a truncated matrix-exponential approximation followed by QR orthonormalization. Compatible projections reuse these bases, while a globally shared full core preserves the flexibility of each projection. Each client further maintains a lightweight private residual operator, whose directions are learned globally and whose coefficients remain local. Experiments on seven public medical tasks and multiple LLM backbones show substantial reductions in trainable parameters and per-round adapter upload volume, with competitive predictive performance on most tasks.

---


### 332. [Fine-Grained Units, Flat Decisions: Hierarchical Micro-Expert Pruning for Mixture-of-Experts Models](https://arxiv.org/abs/2610.25717)

**<font color=#1a73e8>作者：</font>** Zukang Xu, Xinpei Gao, Xing Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Micro-expert pruning reduces the capacity of mixture-of-experts (MoE) models by removing coupled channels within routed experts. However, finer pruning granularity alone does not guarantee the preservation of downstream capabilities, as similar language-modeling perplexity can accompany substantially different task performance. We revisit micro-expert mask construction as two distinct decisions: allocating retained capacity across experts and selecting channels within that capacity. We propose UC-RAMP, a two-stage post-training pruning framework that explicitly separates these decisions. CAPE uses cross-domain calibration evidence to redistribute expert widths under an exact layer-wise budget, while RAMP refines channel composition at fixed widths through one-out, one-in exchanges guided by a channel-interaction surrogate. Across three MoE models at 25% and 50% routed-expert channel pruning, UC-RAMP achieves the highest ten-task mean accuracy among evaluated pruning methods in five of six settings. At 50% pruning, it outperforms the strongest evaluated baseline by 8.19, 3.96, and 6.14 percentage points across the three models, respectively. In a single-A100 deployment at 25% pruning, UC-RAMP reduces measured time to first token by 19.7--23.9% and time per output token by 20.2--22.3% relative to the unpruned model. The code is available at this https URL.

---


### 333. [Learning to Couple: Context-Adaptive Joint Denoising for Diffusion Language Models](https://arxiv.org/abs/2610.25723)

**<font color=#1a73e8>作者：</font>** Zilei Shao, Ian Li, Heng Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models accelerate generation by predicting multiple tokens in parallel, but factorized denoisers treat simultaneous predictions as conditionally independent. Decoding heuristics reduce the resulting errors by controlling which tokens are committed, but leave the underlying distribution factorized. Joint modeling addresses the source of the problem, yet existing methods attach separately learned layers to frozen denoisers, leaving the backbone unadapted to the joint objective and the coupling parameters fixed across contexts. We propose Codpula, a context-parameterized denoiser combining a Transformer with a tractable probabilistic inference layer. Given a partially masked input, the Transformer produces token potentials that shape per-position predictions and compact gates that modulate the layer's coupling parameters, yielding a context-dependent joint distribution while retaining exact conditional inference. We jointly optimize both components under a conditional denoising objective using a dual-flow multiplicative update that preserves valid probabilistic parameters. At inference, Codpula supports standard heuristics and uses conditional queries to adapt commitments to dependencies among proposed tokens without extra Transformer evaluations within a step. Codpula sets new state-of-the-art results across a broad suite of reasoning benchmarks while advancing the accuracy-latency Pareto frontier in mathematical reasoning and code generation.

---


### 334. [Inside the Scorer: Mechanistic Evidence on Rubric Control in LLM-Based Automated Essay Scoring from 25 Base Models](https://arxiv.org/abs/2610.25724)

**<font color=#1a73e8>作者：</font>** Chungche Huang, Po-Ya Angela Wang, Shu-Kai Hsieh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated essay scoring (AES) using large language models (LLMs) offers promising use cases for language assessment, yet high-stakes testing requires scores that are both controllable and verifiable, which current LLM-based scorers lack. Given that, we investigate whether LLM-based scorers form distinct internal representations for individual scoring rubrics and whether these representations can be independently controlled. Probing and steering 25 open-weight base LLMs (0.13B-10.31B parameters; 14 families) on human-scored BESTEP English writing tasks, we find that holistic scores are decodable from model activations for the longer tasks (Parts 2 and 3) and only weakly for the shortest (Part 1). Furthermore, scoring rubrics have partly separable directions in representation space for the longer tasks, though not for short responses (Part 1). However, causal steering reveals a critical limitation: applying a matching intervention (e.g., steering "grammar" on a grammar-degraded response) yields only a negligible advantage (about 2% of the effect) over a mismatched intervention (e.g., steering "vocabulary"), and none that is detectable in any of the 10 testable comparisons across reliably measured rubrics. Rather than controlling distinct evaluative dimensions, the rubric directions share a dominant lever whose rubric-specific parts are not selective, which may mirror the halo structure of human ratings. Our contributions are two-fold. First, we show that analytic scoring rubrics designed for human raters do not behave as independent controls in base LLMs, even among the seven models whose scores agree best with human raters ($r \geq 0.6$). Second, we establish a methodology that shows that score agreement and decodability do not imply rubric-level control in LLM-based assessment.

---


### 335. [Anatomy of Off-Policy Policy Gradient: Importance Sampling, KL Regularization, and Baselines](https://arxiv.org/abs/2610.25725)

**<font color=#1a73e8>作者：</font>** Haoqun Cao, Yurun Yuan, Tengyang Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become a central tool for large language model (LLM) post-training, where policy gradient methods are routinely deployed off-policy, even though vanilla policy gradient assumes on-policy sampling. We study when such off-policy deployment is justified, and what roles its core ingredients, including importance sampling, KL regularization, and baselines, play in handling the resulting distribution shift. We show that for a general class of off-policy policy gradient updates, consistency, in the sense that the optimal policy remains a stationary point, requires one of two structures at the optimal policy: trajectory-level importance weighting, which suffers from the well-known curse of horizon, or KL regularization with a baseline equal to the optimal soft value, instantiated by the grouped mean. Focusing on the KL route, we identify it with the group-relative policy gradient (GRPG) update, establish an equivalence to a trajectory-level Bellman residual minimization objective, and obtain a finite-sample regret bound under all-policy coverage. This also gives a theoretical account of a variant of the empirically successful GRPO objective. We further uncover a hidden role of baselines in the off-policy setting: a constant shift in the baseline implements pessimism, the standard remedy in offline RL for partial data coverage. We instantiate this via the asymmetric REINFORCE objective, and connect it to the game-theoretic offline RL framework, showing a regret bound with single-policy coverage. Together, these results offer a unified theoretical view of off-policy policy gradient in LLM post-training and connect it to classical ideas in offline RL.

---


### 336. [No Matter Who You Are: Addressivity and Sycophancy in Large Language Models](https://arxiv.org/abs/2610.25728)

**<font color=#1a73e8>作者：</font>** Seungjong Sun, Hyunmin Jun, Minsik Yoon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sycophancy, where an LLM becomes overly agreeable, deferential, or flattering toward the user, has been identified as a major failure mode. While post-training has been implicated as a cause, how it internally gives rise to sycophantic behavior remains insufficiently understood. Post-training transforms the model's output from text completion into utterances directed toward an addressee, thereby giving the output \textit{addressivity}. We hypothesize that the accompanying pressure to follow the addressee's instructions and align with their preferences links this addressivity to sycophancy. To test this, we use Sparse Autoencoders to extract addressivity directions from pre-trained and post-trained models and examine their relationship with sycophancy. Steering models with addressivity directions can amplify or suppress sycophancy, and this effect is observed only in post-trained models. Furthermore, comparing the internal mechanisms of both model types confirms that the association between addressivity and sycophancy is strengthened through post-training. Finally, through a controlled post-training experiment, we find that models are sycophantic not toward a specific addressee but toward any recognized addressee, suggesting that the presence of an addressee, rather than the addressee's identity, is what elicits sycophancy.

---


### 337. [Does Unlearning Survive Collaboration? Robust Unlearning for Shared-Model LLM Teams](https://arxiv.org/abs/2610.25731)

**<font color=#1a73e8>作者：</font>** Hengsong Liu, Liangyu Teng, Jingnan Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM unlearning is essential for removing sensitive or unwanted knowledge while preserving useful capabilities. As LLM teams are increasingly used to solve complex problems, forgetting must remain effective during collaboration. Despite advances in forgetting effectiveness, efficiency, and robustness to relearning, team deployment remains underexplored. We find that collaboration weakens forgetting: final-answer evaluations miss recoverable evidence in team messages, including complementary clues supporting joint recovery. We establish theoretically and confirm empirically that controlling final answers or individual messages does not ensure low recovery from their combination. To address this challenge, we propose Aggregation-Conditioned Unlearning (ACU). ACU trains a shared model using reconstruction feedback from individual and pooled messages, prioritizes views with higher recovery risk, and uses replacement-based credit assignment while protecting direct and collaborative utility. TOFU evaluates trajectory-level recovery, while WMDP-bio tests native forgetting and retained utility. On TOFU, ACU lowers full-trajectory recovery from 41.8% to 19.3% in ROUGE-L recall and factual recovery from 34.2% to 18.7% versus output-supervised training, with comparable retained-task performance. These results demonstrate that ACU curbs information leakage in LLM teams and generalizes across team sizes and readers.

---


### 338. [TimelineAgent: An LLM-based Framework for Query-Centric Event Timeline Extraction Across Multiple Documents](https://arxiv.org/abs/2610.25733)

**<font color=#1a73e8>作者：</font>** Qingkai Min, Yunxin Bao, Yifeng Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Query-centric cross-document event timeline extraction aims to construct event timelines from multiple documents under diverse query focuses. The task is very challenging due to the heterogeneous event modeling and reasoning requirements arising from both the intrinsic complexity of cross-document timeline construction and the diversity of query focuses. In this paper, we propose TimelineAgent, an LLM-based multi-agent framework featuring a multi-stage reasoning workflow, where heterogeneous event features are organized into reusable skills and orchestrated through a goal-oriented protocol. To facilitate evaluation, we construct a benchmark covering diverse query focuses. Experimental results show that TimelineAgent consistently outperforms existing methods, offering a practical framework for complex real-world timeline construction.

---


### 339. [Think Densely, Act Sparsely: Latent Expert Cognitive Chains for Vision-Language-Action Autonomous Driving](https://arxiv.org/abs/2610.25734)

**<font color=#1a73e8>作者：</font>** Jie Wang, Guang Li, Zhijian Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving fundamentally demands dense understanding of visual, semantic, and geometric information, yet existing Vision-Language-Action (VLA) models are typically trained with sparse supervision such as language instructions or trajectory signals. This direct mapping from dense visual observations to sparse representations forces the model to compress or even discard critical scene information essential for safe driving. We argue that this limitation does not stem from insufficient model capacity, but from the lack of explicit mechanisms that encourage the formation of dense world representations in the latent space. In this spirit, we propose a novel paradigm for driving intelligence, Think Densely, Act Sparsely, and instantiate it with an efficient and interpretable framework, LECDrive (Latent Expert Cognitive Chains for Vision-Language-Action autonomous Driving). The core idea is to mimic the hierarchical perception process of humans by embedding a progressive chain of latent expert cognition within the VLA model. Concretely, we inject a compact set of task-specific latent tokens as carriers, enabling the model to internalize dense knowledge from foundational vision models, including visual representations (DINOv3), semantic structures (SAM3), and spatial geometry (DepthAnything3), while maintaining efficient inference. This interdependent cognitive chain follows a curriculum learning principle, where supervision is progressively structured from representation to semantics and geometry. Extensive experiments demonstrate that LECDrive consistently improves the performance of base VLMs across multiple autonomous driving benchmarks, covering key tasks such as object perception, state prediction, and trajectory planning. These findings suggest that constructing dense world models through structured latent expert chains is a promising direction for VLA-based autonomous driving.

---


### 340. [A Calibrated Instrument for Detecting Disposition Drift in Language Models](https://arxiv.org/abs/2610.25735)

**<font color=#1a73e8>作者：</font>** Jerry Kaplan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Before language models are released, they are tested for harmful traits such as willingness to carry out dangerous requests, deception, power seeking, and sycophancy. The safe behavior these tests certify may degrade as models are modified, by topical fine-tuning, new training data, or changes to settings such as the depth of their reasoning. Most work reports such drift as single summary rates scored by another AI model, without the error analysis needed to interpret them. We adapt a calibrated measurement methodology recently developed for assessing how inference optimizations affect the quality of model outputs. Applying it to several misalignment dimensions in two open-weight models, we first establish the instrument's precision, showing that shifts of a few percentage points can be reliably detected. We then induce drift deliberately by fine-tuning on correct and on subtly harmful medical and financial advice; harmful advice induces a far greater shift than correct advice. Most strikingly, a model that reasons before answering can conceal the shift almost entirely in its answers, even though a direct reading of its internal state shows that its disposition has moved. With reasoning switched off, the same model shifts steadily as the share of harmful advice in its training grows. These results demonstrate the importance of testing safety with reasoning turned both on and off.

---


### 341. [How Much Does One Wrong Answer Cost? Error Propagation in Constraint Pruning with Noisy LLM Oracles](https://arxiv.org/abs/2610.25739)

**<font color=#1a73e8>作者：</font>** Zhengtao Gui, Weining Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constraint pruning saves queries to a large language model (LLM) or another noisy oracle by skipping each yes/no question implied by answers accepted earlier, for example through transitivity. Entity-resolution systems and LLM-based rankers use this idea. However, their analyses typically assume a correct oracle. We argue that pruning should be judged by its risk when the oracle errs, since an accepted wrong answer spreads to every question it implies. When each answer is wrong independently with small probability $\varepsilon$, the first-order risk is set by how many facts one wrong answer corrupts on average. We consider two kinds of constraints. For implication rules, as in taxonomies, pruning in a random order adds no first-order risk: a wrong answer that would change $k$ facts is accepted with probability $1/k$, so it costs one fact on average. Rules with $s$ premises break this balance: a wrong answer at a premise shared by $r$ rules can cost order $r^{1-1/s}$ facts. For entity resolution with $m$ records of one entity, the first-order risk equals $\varepsilon$ times the Wiener index (the total pairwise distance) of the spanning tree built by the query order. Pivot orders, which first compare one record with all others, amplify errors by less than 2 and are optimal; random orders by order $m^{1/3}$; the common most-similar-first order is the worst in one dimension and, for large $m$, worse than random in two. With several entities, the cost of wrongly merging two does not depend on how many others exist. Simulations agree with every predicted constant within sampling error.

---


### 342. [Bayesian Model Discovery with Language Models: Closing the Loop between Hypotheses and Experiments](https://arxiv.org/abs/2610.25747)

**<font color=#1a73e8>作者：</font>** JooKyung Yuh, Byungmin Park, Eunseo Choi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific model discovery requires proposing candidate models of an unknown system and designing experiments that discriminate among them. However, LLM-based approaches typically rely on in-context learning to predict outcomes and select experiments, lacking explicit model evaluation to systematically guide hypothesis search, while Bayesian approaches enable principled model comparison but are confined to a predefined candidate set which results in limited search spaces. To this end, we introduce BMD, which closes the loop between LLM-driven hypothesis generation and Bayesian experimental design. Specifically, an LLM proposes model families, while a numerical engine fits their parameters, weighs them by model evidence, and averages their predictions. Then, BMD chooses the next experimental conditions by maximizing the joint expected information gain over families and their parameters, while feeding the updated beliefs and residual diagnostics back to the LLM to guide its next proposals. Across four scientific discovery benchmarks, BMD achieves lowest final prediction error than in-context learning and LLM-based scientific agents while recovering exact functional forms more often, with ablations supporting numerical feedback and the joint objective.

---


### 343. [NADS: Navigator-Guided Data Selection for Mitigating Catastrophic Forgetting in Fine-Tuning](https://arxiv.org/abs/2610.25751)

**<font color=#1a73e8>作者：</font>** Jianhao Zhang, Ou Wu, Yi Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting is a central obstacle in single-stage fine-tuning of large language models (LLMs) on a new task, especially when the original pretraining data are unavailable. Synthetic data offers a practical mitigation path, but candidate pools are often noisy and redundant, making effective selection essential. Existing methods often rely on indirect proxy signals whose alignment with actual training benefit can be limited, while utility--diversity selection over large candidate pools remains computationally demanding. To address these challenges, we propose NAvigator-guided Data Selection (NADS), a fine-tuning framework for LLMs. NADS first follows the target fine-tuning recipe without preservation regularization to obtain a navigator model, whose deviation from the pretrained model exposes recipe-induced capability drift. It then uses the predictive divergence between the navigator and the pretrained model to score forgetting-aware utility for each synthetic candidate, and constructs a constraint set through an efficient utility--diversity selection strategy. Finally, NADS fine-tunes on the new-task data while distilling pretrained behavior on the selected constraints to preserve general capabilities. Experiments show that NADS delivers a stronger balance between new-task performance and general capability preservation, while reducing utility--diversity selection overhead. Code at: this https URL.

---


### 344. [Computation, Not Memory: Chain-of-Thought and State Tracking in LLM Agents](https://arxiv.org/abs/2610.25760)

**<font color=#1a73e8>作者：</font>** Pedram Mouseli, Massieh Moayedi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model agents often reason before they act, and the value of monitoring that reasoning depends on how it relates to their actions. We ask how an agent's actions depend on its reasoning when the correct action depends on a changing state. In a small file-system task, background events announce which file's lock has been toggled but not its new value. The agent therefore has to reconstruct the current locks from its history before it can move files safely. With Qwen3-8B and Qwen3.5-9B, we separate two roles of reasoning: generating it before each action, and retaining earlier reasoning in the prompt. Most of the reduction in lock-violating commands comes from reasoning written at the moment of action. Retaining earlier reasoning adds little to rule-following, although it helps one model complete the task. The benefit depends on what the reasoning says. Filler text, reasoning written for another history and an accurate table of the state do not reproduce it. When we give the agent reasoning written for a history that differs in one lock value, the agent acts on that reasoning even against its own history. Without reasoning, linear probes recover the state from the model's activations about as well as a text classifier recovers it from the transcript. However, decoding accuracy does not predict which interventions change the agent's actions. In this setting, the benefit of reasoning for rule-following comes mainly from generating it at each step. The state that can be decoded without reasoning is a limited guide to how the agent acts.

---


### 345. [EvalRx: Agentic Diagnosis and Verified Repair of Foundation Models](https://arxiv.org/abs/2610.25767)

**<font color=#1a73e8>作者：</font>** Jiaqi Liu, Ruinan Jin, Yitong Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model evaluation reveals where models fail, but rarely why or whether a proposed fix genuinely works. We introduce EvalRx, an open-source agentic framework for statistically grounded model diagnosis and repair. EvalRx discovers systematic failure modes, explores candidate mechanisms, formulates falsifiable hypotheses, and verifies them by executing frozen, pre-specified tests before using supported diagnoses to guide tiered repair. Candidate repairs are validated against the unchanged model and promoted only when they improve the target behavior without unacceptable regression. Across language, vision-language, and audio-language settings spanning Gemini, Qwen, Gemma, and Nemotron, EvalRx improves performance in all 12 evaluated model family-modality combinations, with gains ranging from +1.4 to +10.9 percentage points (+5.8 points on average). These results show that model evaluation can serve not only to measure failures, but to support an auditable process for diagnosing and repairing them.

---


### 346. [Truncated Reasoning Under a Budget: Evaluating System-1 Models as Decision-makers](https://arxiv.org/abs/2610.25768)

**<font color=#1a73e8>作者：</font>** Zhongyin Wang, Zhaoqian Xue, Junting Mu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often generate more reasoning tokens than needed. Limiting the reasoning budget reduces cost, but forcing an answer from an incomplete trace can hurt accuracy. System-1 decision models select among candidate options without producing a reasoning response. We evaluate Jev as a decision reader of truncated reasoning across seven LLM reasoners and five multiple-choice benchmarks (35 pairs). Jev achieves higher mean accuracy than forced answering at tested budgets from 500 to 16,000 tokens, including the estimated costs of reasoning and answering. At a 1,500-token budget, it improves accuracy by 4.1 pp overall and 8.6 pp on truncated questions, with significant gains in 17 pairs under Holm-corrected bootstrap tests. Offline replay estimates 34.5% of the full-run cost, with a 1.13 pp accuracy loss. A policy selected on training folds saves 71.3% of the estimated full-run cost on held-out folds, with a 0.58 pp accuracy loss. We also find that Jev shows strong question-only accuracy, exceeding 500-token forced answering on average (68.0% vs. 65.5%), although this advantage varies by benchmark. These findings suggest that System-1 decision models can complement LLM reasoning and reduce the need for costly reasoning completion.

---


### 347. [VHA: VQA-based Hallucination Assessment for Generative Image Super-Resolution](https://arxiv.org/abs/2610.25770)

**<font color=#1a73e8>作者：</font>** Donghun Ryou, Inju Ha, Jaeyoo Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative image super-resolution produces visually realistic high-resolution images, but may also introduce hallucinations by adding unsupported content or altering existing details. Because existing super-resolution metrics fail to measure whether generated details remain grounded in the reference image, we present a hallucination assessment technique based on bidirectional visual question answering (VQA), which we term VQA-based Hallucination Assessment (VHA). The proposed approach uses a vision-language model (VLM) to determine whether the semantic content and low-level visual evidence in a super-resolved image are supported by its ground-truth counterpart. To this end, it constructs question--answer pairs from each image and evaluates them on both images. Discrepancies between the resulting scores in both directions reveal missing or altered ground-truth information and unsupported additions. However, obtaining these scores requires computationally expensive VLM inference. We therefore develop VHA+, a learned, lightweight model that directly predicts VHA scores from ground-truth and super-resolved image pairs. We construct a hallucination benchmark, VHA-bench, through a human study and show that both VHA and VHA+ correlate highly with human judgments of hallucination. The code, benchmark, and model weights are available at this https URL

---


### 348. [From Trace to Fix: Residual Task State in Long-Horizon Agents](https://arxiv.org/abs/2610.25776)

**<font color=#1a73e8>作者：</font>** Zile Huang, Ser-nam Lim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recovering from failures in long-horizon, stateful language agents is challenging because the action introducing a defect, the symptom exposing it, and the persistent state requiring repair frequently diverge. Existing methods largely focus on retrospective failure attribution, leaving sequential diagnosis and state repair poorly integrated under constrained budgets. We introduce TRACE-FIX, a unified recovery framework centered on versioned residual task state. Trace transforms execution logs into a structured dependency-linked ledger, prioritizing unresolved task requirements rather than salient surface errors. Fix formulates recovery as budgeted planning over admissible actions, incorporating outcome forecasting and explicit repair-reserve constraints to prevent premature budget exhaustion. To rigorously decouple localization accuracy from downstream repair capability, we present LongH-Debug, evaluating root-cause attribution, verified-fault recovery, and end-to-end closed-loop execution independently. Our empirical analysis demonstrates that structured residual tracking substantially improves causal localization over raw-trace baselines, while budget-aware sequential planning converts verified fault signals into more reliable task recovery without destructive trial-and-error. Code is available at this https URL.

---


### 349. [Standing on the Shoulders of Giants: Enhancing LLM Agents for Automated Fact-Checking with Human Expert Skills](https://arxiv.org/abs/2610.25777)

**<font color=#1a73e8>作者：</font>** Xinwen Chen, Haorui He, Yupeng Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated fact-checking (AFC) systems powered by large language model (LLM) agents still face challenges in evidence retrieval and claim verification. Existing approaches improve their capabilities through computationally costly post-training or human-in-the-loop feedback that is difficult to scale. To transfer professional fact-checking expertise to LLM agents efficiently, we distill publicly available guidelines published by Agence France-Presse (AFP) Fact Check into a reusable, modular Professional Fact-Checking Skill (PFC-Skill). We then present SkillCheck, the first AFC system that gives LLM agents dynamic access to PFC-Skill to guide evidence retrieval and claim verification at inference time. Extensive experiments demonstrate that SkillCheck improves upon skill-free DEFAME baselines across multiple LLM backbones, with gains of 2.2--4.8 pp. in Accuracy and 1.5--6.3 pp. in Macro-F1 on the AVeriTeC benchmark. Notably, SkillCheck with GPT-4o-Mini exceeds DEFAME with GPT-4o by 3.4 pp. in Accuracy while cutting inference cost by roughly 61%. The performance gains also extend to open-web retrieval. Ablations show that incorporating the skill during evidence retrieval provides most of the gains, while incorporation into both stages yields the best overall performance. Case studies show that PFC-Skill enables more targeted search and closer scrutiny of evidence. To conclude, our work shows that LLM agents can "stand on the shoulders of giants" by drawing on the best practices of professional fact-checkers, substantially enhancing AFC performance without extra training or continuous human supervision.

---


### 350. [OpenSaC: A Python Library for Search as Code in Deep Research Agents](https://arxiv.org/abs/2610.25779)

**<font color=#1a73e8>作者：</font>** Qi Liu, Jiaxin Mao, Fengbin Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research agents investigate complex questions through iterative search, source examination, and evidence synthesis. A conventional workflow alternates reasoning with individual search and reading actions. Search as Code introduces a new paradigm: agents write programs that compose search, source reading, reranking, model calls, and local processing, returning selected observations for further reasoning. To support this workflow in existing coding agents, we present OpenSaC, an open-source Python library with a companion Search as Code skill. Configurable capability interfaces let agents combine these operations while retaining evidence for inspection and reuse. Compared with standard Codex using its built-in web search, the OpenSaC configuration uses less execution time and fewer model tokens on BrowseComp and WideSearch, with higher accuracy on BrowseComp and slightly lower row F1 on WideSearch. We aim to lower the barrier to adopting Search as Code and provide an open foundation for community development and transparent research on deep research agents.

---


> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
