# 🧠 大模型相关研究 | 2026年11月06日

> 本类共 **207** 篇论文：已确认 **189** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-207](./part-05.md)

---

### 151. [Time-Division Multiplexing: The Operational Rhythm and Temporal Organization Layer of Digital Life](https://arxiv.org/abs/2611.06603)

**<font color=#1a73e8>作者：</font>** Haibin Tong, Luming Guo, Nana Cui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual agents must handle urgent interaction while retaining alternatives, replaying errors, and committing safe long-term changes. A previous digital-life framework distinguishes online (busy) and offline (idle) channels, but leaves open whether these are separate programs or phases of a common process and how their operations should be ordered. Motivated by recent observations of rapidly alternating perceptual representations in primate cortex, we develop a temporal organization layer with phase-tagged micro-epochs, an observable duty cycle, independent content and resource controls, and three nested clocks separating candidate exploration from durable commitment. We give a projected duty-cycle update, state its deterministic descent guarantee and the additional noise term required for a stochastic guarantee, and specify coupled busy/idle execution contracts. Five synthetic experiments (64 seeds each) examine descent and noise, objective misalignment, gain asymmetry, resource coupling, and dropped replay logs. In the gain/noise model the best tested gain ratio is 1.55; decoupled scheduling yields 26.6% versus 11.1% success on a constructed urgent/high-load subset. A frozen-backbone Qwen3-8B prototype further checks orchestration, but its proxy outcomes are not task-benchmark evidence. The results establish a testable scheduling design and identify its conditions of validity, not machine consciousness or general-purpose agent superiority.

---


### 152. [Verifier-Guided Self-Consistency: Test-Time Reasoning with Imperfect Generators and Verifiers](https://arxiv.org/abs/2611.06606)

**<font color=#1a73e8>作者：</font>** Ekaterina Fadeeva, Xueyan Li, Mrinmaya Sachan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can solve many multi-step reasoning problems, but their reasoning remains brittle: plausible intermediate steps often lead to incorrect answers. Improving reasoning at test time requires balancing two imperfect signals: the generator, which provides diversity, and the verifier, which guides correctness. Existing approaches largely favor one side of this tradeoff. Verifier-weighted voting relies on trajectories sampled from the generator and cannot steer generation toward correct ones. By contrast, beam-style verifier-guided search can steer generation, but may over-concentrate on narrow trajectory sets and amplify verifier errors.
We propose Verifier-Guided Self-Consistency (VGSC), a stochastic decoding framework that combines step-level correctness and future-outcome estimates to guide reasoning during generation. VGSC repeatedly proposes candidate next steps from the base language model and uses both signals in an acceptance/resampling procedure, while maintaining multiple trajectories for final answer-level self-consistency. We provide a probabilistic interpretation of VGSC as approximate sampling from a verifier-tilted trajectory distribution. Across multiple reasoning benchmarks, generator models, and verifier families, VGSC achieves higher average accuracy than representative baselines.

---


### 153. [Replicability, Reproducibility, and Robustness in Political and Social Science Research with Large Language Models](https://arxiv.org/abs/2611.06639)

**<font color=#1a73e8>作者：</font>** Joan C. Timoneda, Sebastián Vallejo Vera  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This chapter addresses the central reproducibility problem of research with large language models. LLM output is probabilistic and varies across models and versions, which can have significant effects on downstream statistical results. The chapter distinguishes between replicability, reproducibility, and robustness, and proposes a probabilistic standard based on the distribution of results, not identical outputs. It introduces a standardized prompt script, tests within-model variation for encoders and decoders, and develops error-structure analysis to diagnose where models err and whether their errors align. Using three datasets, the chapter shows that measurement choice can reverse the sign of downstream regression coefficients. Existing design-based corrections with gold-labeled subsamples restore validity, but come at the cost of estimate precision. The main contribution of the chapter is a stacked ensemble of open-weight models that improves precision in the correction step while retaining estimate validity.

---


### 154. [Perceived Trust and Transparency in AI-Altered vs. Human-Written LinkedIn Posts](https://arxiv.org/abs/2611.06660)

**<font color=#1a73e8>作者：</font>** Thomas Christian Joos, Azza Bouleimen, Anikó Hannák 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People increasingly draft a social media post themselves and then let an AI model refine it (AI-altered), a common but understudied middle case between fully human-written and fully AI-generated content. We ask whether this changes how trustworthy and transparent readers perceive the post to be, and whether they can even tell. We first analyze real ChatGPT conversations (WildChat) to find how people actually alter social media posts, which we use to design realistic alteration prompts. We then run a pre-registered, within-subjects online experiment (n=214) in which participants rate unlabeled human-written and AI-altered LinkedIn-style posts for perceived trustworthiness and transparency, and separately judge whether each post was AI-altered. We find that AI-alteration itself has no detectable effect on either perceived trustworthiness or transparency (both estimates near zero, not significant). At the same time, readers did not reliably detect AI-alteration (49\% accuracy, near chance) and defaulted to assuming human authorship when unsure. However, our analysis shows significant differences in transparency and trustworthiness ratings across the specific post, the AI model, as well as the prompt used to alter it. For instance, more detailed prompts raise both perceived trustworthiness and transparency but also make the alteration more detectable. Surprisingly, the prompt that shifted ratings most also asked the model to add one new idea absent from the original post: readers nonetheless rated this AI-invented, unverifiable content as more trustworthy and transparent.

---


### 155. [SecureGARD: Dynamic Ontology-Guided Governance for Secure Tool-Using LLM Agents](https://arxiv.org/abs/2611.06682)

**<font color=#1a73e8>作者：</font>** Guoqin Xiong, Shengtao Wen, Xiang Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-using large language model (LLM) agents translate model outputs into consequential actions, turning indirect prompt injection into an execution-security problem. Existing defenses constrain tool calls, trajectories, or information flows, but often leave action semantics, state dependencies, and evidence relations implicit, limiting generalization across heterogeneous tools and complicating safe updates. We present \ours{}, a dynamic ontology-guided governance framework. \ours{} grounds heterogeneous calls in a shared semantic representation and combines an executable ontology with episode-level task state to derive deterministic ready, waiting, and forbidden decisions. A waiting decision identifies an unmet but recoverable obligation, enabling bounded replanning without expanding the agent's authorization boundary. \ours{} evolves its ontology offline from verified training executions. An offline LLM proposes instance-independent action--state axioms, which are accepted only if they address ontology errors exposed by training failures, preserve logical consistency and protected entailments, and pass held-out validation before the ontology is frozen. We evaluate \ours{} on AgentDojo, ASB, and AgentDyn under benign and indirect prompt-injection settings. \ours{} achieves a 0\% attack success rate (ASR) across all three benchmarks while improving task utility under attack compared with existing baselines. These results show that explicit semantic governance can strengthen execution security without indiscriminate blocking.

---


### 156. [LifeVal: Evaluating AI Model Performance on Personalized Agentic Consumer Tasks](https://arxiv.org/abs/2611.06687)

**<font color=#1a73e8>作者：</font>** Jenny Yang, Elizabeth Proehl, Anjan Bharadwaj 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce LifeVal, a benchmark evaluating AI model performance on personalized agentic consumer tasks. LifeVal covers the most valuable life tasks that a personalized digital superassistant could automate, representing over 1.7 trillion US dollars in annual willingness-to-pay across 148 consumer task categories (e.g., managing finances, moving apartments, searching for a job, finding childcare). To construct our activity distribution, we conducted a new survey of willingness-to-pay for a digital superassistant across a demographically representative sample of over 3,800 consumers, cross-referencing our results against the American Time Use Survey (Bureau of Labor Statistics, 2025) and the Multinational Time Use Study (Fisher et al., 2025). For the most valuable consumer activities, we recruited task creators to create AI evaluation tasks personalized using real ChatGPT conversations and memories, reference files, and personal context. Task creators had to pass our expertise threshold (including personally completing the task multiple times and seeing the results through in their real lives for over a year) and also write a rubric, ensuring that our evaluation measured the best personalized completion for that task. All tasks had to pass at least three rounds of human quality-control before acceptance into our final evaluation sets.

---


### 157. [Where It Breaks: Diagnosing Perception, Memory, and Decision Failures of a Vision-Language Agent in Pac-Man](https://arxiv.org/abs/2611.06704)

**<font color=#1a73e8>作者：</font>** Xinglu Wang, Edward Wang, Yong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training an agent to play Pac-Man with only up, down, left and right actions raises a basic question: when performance is poor, what should be improved? Difficulty can arise from reading the screen or from choosing actions over a long sequence. We examine these problems in a Qwen3.5-9B-based agent through separate perception checks and primitive-policy reinforcement-learning studies. In the policy study, which uses textual boards to remove image transcription from the decision interface, completion on eight held-out mazes increased from 0% before this optimization to 80.2% at a selected checkpoint, with three extra lives. The perception checks show that accurate static screenshot reading can coexist with errors during interaction. A separate policy comparison also shows that further optimization can accompany worse action choices. Together, these findings motivate concrete checks for post-training: evaluate perception in use, distinguish training success from full-game validation, and examine decisions and later performance rather than relying on one selected score. The study provides empirical lessons for improving future agent training and evaluation.

---


### 158. [Reasoning over Non-Parametric Memory in Multilingual LLMs: A Cognitive-Based Analysis of Relational Knowledge](https://arxiv.org/abs/2611.06715)

**<font color=#1a73e8>作者：</font>** Zohreh Abbasi Liasi, Batoul Hammoud, Anas Madkoor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) assumes that language models can reason over relations stated in their context rather than fall back on associations memorized during pretraining. We study this evidence-conditioned relational reasoning in isolation, with the facts supplied directly in the prompt rather than retrieved. \textsc{Rel-Bloom} is a controlled multilingual diagnostic of 450 multiple-choice questions built from 30 Wikidata relations; the same source relations are instantiated at five Bloom-inspired levels (Remember, Understand, Apply, Analyze, Evaluate) and under three veracity conditions (Factual, Counterfactual, Neutralized). Across 43 models, six languages, and two multilingual settings (226,800 predictions), three findings stand out. First, accuracy drops sharply from Apply to Analyze in every evaluated open-weight model series, reaching 47.2 percentage points for the Large Granite bucket, but not for either Gemini model. Second, Evaluate items remain a bottleneck even for models near ceiling on the other task types: Gemini~3.1 Pro averages 99.5\% on the other four levels but 60.7\% on Evaluate. Third, item- and relation-level difficulty rankings are consistently preserved across languages, indicating a difficulty structure partly shared across languages within this benchmark. Across knowledge conditions, Counterfactual contexts are generally harder than Factual ones, while removing entity identities can improve higher-level performance in some model regimes. Greater model capability therefore does not by itself ensure reliable reasoning over supplied relational evidence. Relevant resources are available at: this https URL.

---


### 159. [Airlock: Bounding the Multi-Agent Blast Radius via Selective Online Containment](https://arxiv.org/abs/2611.06727)

**<font color=#1a73e8>作者：</font>** Zhonghao Zhan, Javad Forough, Yefan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> When multi-agent systems act on the external world, a single agent's faulty output can spread across tasks before detection, creating a system-wide blast radius. Single-agent guardrails are confined to individual harnesses, while existing multi-agent controls either cancel only the faulty source and miss downstream consumers or halt and roll back the entire workflow at the cost of healthy work. We present Airlock, a multi-agent runtime and guardrail for selective post-alert fault containment. Its tree-structured runtime, EdgeCitadel, narrows permissions vertically from parent to child agents to establish node boundaries and control switches. Meanwhile, an append-only provenance DAG records cross-agent data consumption horizontally. Upon an alert, Airlock traces forward on this DAG to isolate tainted executions and pending actions, and backward to narrow root causes. At the site switches, a default full quarantine tier freezes affected branches without a solver, while an assured optimized cut tier uses fence-then-prune to enforce a deadline-aware minimum cut minimizing collateral disruption. Across 1,832 testbed runs, 161 physical smart-home LLM runs, and 24,266 simulation records, Airlock blocks all post-alert faulty actuations on our main testbed and smart-home grids with zero post-convergence leaks. Whereas native controls in A2A and LangGraph either contain at most 33.3% of faults or retain at most 16% of work without redo, Airlock retains +68 pp to +96 pp more healthy work, and its optimized cut retains +46 pp more than full quarantine under dense spread. These results show that co-designing runtime authority boundaries with online provenance enables surgical fault containment without sacrificing healthy work (code: this https URL).

---


### 160. [Template Gap Reconstruction for Shell Output Simulation with Small Language Models](https://arxiv.org/abs/2611.06731)

**<font color=#1a73e8>作者：</font>** Jarrod Ragsdale, Rajendra Boppana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models offer a compact basis for shell simulation without executing submitted commands, but full-output decoding requires them to predict recurring utility structure alongside content that varies across executions. We introduce template gap reconstruction (TGR), which supplies reusable output literals interspersed with sentinels to be interleaved with autoregressively generated gaps. A template selector chooses which template to be reconstructed, with the empty template retaining full-output decoding. We construct a template bank from 18.7 million outputs collected across heterogeneous execution environments and train a template selector and five reconstruction models initialized from various small language model checkpoints on a target environment excluded from bank construction. Evaluation demonstrates that TGR improves output edit similarity (O-ES) over full-output decoding (FOD) when the optimal template covers more than 25\% of the template, while performing similarly for lower-coverage outputs. Additionally, TGR outperforms FOD for shorter gap sequences, with O-ES values of 0.964 and 0.812, respectively, while maintaining similar performance for longer sequences. TGR reduces the number of tokens generated by 26.3--38.3\% across used tokenizer families. These results support using a reusable output structure as a practical design choice for small shell simulators, improving response fidelity and shortening generation targets while keeping template selection and residual prediction central to response quality.

---


### 161. [ConceptARC at Scale: Studying Conceptual Understanding in Reasoning Models](https://arxiv.org/abs/2611.06732)

**<font color=#1a73e8>作者：</font>** Philipp Mondorf, Adrien Deliège, Solim LeGris 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) perform well on challenging benchmarks, yet it remains unclear whether they form generalizable abstractions across conceptually related reasoning tasks. The Abstraction and Reasoning Corpus (ARC) provides a controlled testbed for studying abstraction, requiring solvers to infer transformation rules over two-dimensional grids from a small set of examples. While ARC evaluates rule abstraction within individual tasks, different tasks may share higher-level structure despite requiring different transformations$\unicode{x2014}$for example, several tasks may involve reasoning about objects contained within other objects. Benchmarks such as ConceptARC capture this structure by grouping ARC-style tasks into recurring spatial and semantic concepts, but they often contain only a few manually constructed tasks per concept. We introduce ConceptARC at Scale, a generator for creating thousands of ARC-style tasks targeting a specific concept. Using this generator, we construct ConceptARC-100, a dataset of 1,600 new, manually reviewed tasks, with 100 tasks for each of the 16 concepts defined by ConceptARC$\unicode{x2014}$ten times the size of the original benchmark. We evaluate a range of recent LRMs and models trained from scratch on ConceptARC-100 to characterize which concepts they solve reliably and where they struggle. We further analyze the models' internal representations and find clear semantic structure: task representations cluster according to the operations applied to objects, such as recoloring, removal, or translation, even when realized through substantially different rules and scenarios. Together, our results suggest that models form stable abstractions of transformation operations that generalize across diverse tasks.

---


### 162. [Smartphone-Aided VR Exergames for HIIT: Gamifying Fitness with Real-Time Pose Estimation](https://arxiv.org/abs/2611.06734)

**<font color=#1a73e8>作者：</font>** Abhiram Kothagundu, Pheelip Pritipal Raipure, Abhijit Chandrakant Patil 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper introduces an innovative virtual reality (VR) exergame system designed to gamify High-Intensity Interval Training (HIIT) workouts through 11 predefined combo moves, including squat-punch combinations, bilateral arm strikes, and diagonal stretch combos. Unlike conventional tracking methods that often rely on wearable motion capture suits or limited headset-based sensors, our system uses a standard smartphone camera placed on a tripod to capture full-body movement. This approach offers a cost-effective and scalable alternative, particularly well-suited to the fast, dynamic motions typical of HIIT routines.
The smartphone footage is processed in real time using a pose estimation algorithm, with extracted biomechanical data analyzed by a backend server built on the Model Context Protocol (MCP), Anthropic's open standard for connecting AI models to structured data sources and tools, and a GPT-4o large language model. The system generates personalized assessments of form accuracy, movement efficiency, exercise intensity, and potential injury risks, tailored specifically to high-impact, time-sensitive exercises.
A within-subject study involving 20 participants (ages 18-25) compared experiences in VR and Non-VR HIIT sessions. Results indicated significantly higher enjoyment (Mean = 3.5 vs 2.8, p = 0.02), improved immersion/focus (Mean = 3.2 vs 2.8, p = 0.03), and increased likelihood to recommend (Mean = 3.2 vs 2.7, p = 0.04) under the VR condition. Confidence to continue did not differ significantly between conditions (p = 0.15), while perceived intensity remained comparable. The MCP system showed strong agreement with expert evaluation (87.5%, N = 10 sessions, one certified trainer), supporting its reliability as a feedback tool.

---


### 163. [TailSteer: Trajectory-Tail Steering for Drift-Resistant Multi-turn Image Editing](https://arxiv.org/abs/2611.06741)

**<font color=#1a73e8>作者：</font>** Ruikang Li, Zixuan Chen, Jiarui Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Strong single-turn editing performance does not guarantee reliable multi-turn interaction: as edited outputs are repeatedly reused, small unintended changes can accumulate into severe visual drift. This long-term drift is often mitigated through training on multi-turn data or cross-turn rollouts, potentially altering pretrained priors, or through specialized inference-time mechanisms that are difficult to scale to foundation models. We introduce TailSteer, a final-stage training framework that improves multi-turn robustness while retaining the generative and editing capabilities acquired through earlier training. TailSteer follows a simple principle: keep early denoising dynamics close to those of the base model and concentrate preservation corrections near the trajectory tail, where fine-grained deviations can be suppressed. These corrections are learned from the editor's own on-policy denoising rollouts, using unchanged source content as a preservation reference without requiring curated ground-truth editing pairs. Experiments across the FLUX, SenseNova, and Qwen families show that TailSteer substantially reduces cumulative drift over 15-20 editing turns while largely preserving base-model performance on extensive text-to-image and single-image editing benchmarks. These results demonstrate that long-horizon editing robustness can be unlocked in foundation models after TailSteer, rather than by relearning their existing capabilities.

---


### 164. [EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models](https://arxiv.org/abs/2611.06748)

**<font color=#1a73e8>作者：</font>** Yequan Bie, Dengyang Jiang, Zhixuan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative video models are increasingly used as visual world simulators, yet their primary strength lies in rendering plausible pixels rather than reasoning about how a world should evolve. Coherent world evolution requires more than visual fidelity: when an event occurs, a model must infer its consequences for the entities in the world and then render the resulting state. For example, after a wild beast appears, the model should not only depict the wild beast, but also infer whether a nearby person should flee, take cover, or fight back based on the realized scene. Existing diffusion-based video models lack an explicit mechanism for maintaining world state and reasoning over such event-conditioned consequences, often producing visually plausible but behaviorally static or causally inconsistent outputs. To make this reasoning gap concrete and measurable, we propose a new problem, Out-of-Sight Causal Evolution, which requires a model to render an event, reason about its consequences for the evolving world state, and reveal a causally plausible outcome as the world continues to evolve, even out of sight. As a baseline reference solution, we introduce EvoWorld, a brain-renderer collaboration framework in which a vision-language model serves as the world brain: it observes generated segments, maintains an evolving account of the world, and reasons about plausible state transitions, while a segment-autoregressive video renderer realizes them visually. We further introduce EvoWorld-Data and EvoWorld-Bench for training and evaluating event realization, causal reactions, and revisit consistency. Experiments show that EvoWorld substantially improves event-conditioned causal evolution over recent models while preserving visual quality and consistency, establishing a reference point for reasoning-guided, autonomous world evolution beyond the current field of view.

---


### 165. [Route First, See Later: Enabling Vision Agents to Reason Scientifically by Separating Routing Policy from Action Spaces](https://arxiv.org/abs/2611.06760)

**<font color=#1a73e8>作者：</font>** Shubhabrata Mukherjee, Jeffrey Donatelli, Daniela Ushizima  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific image-analysis workflows require agents to select among diverse capabilities like description, detection, counting, and segmentation. Current multi-tool architectures conflate intent interpretation with visual execution, masking whether a failure arises from flawed reasoning (misrouting) or failed perception (invalid tool execution). This lack of auditability renders agents unreliable for high-stakes scientific automation. We introduce ZETA, an extensible architecture that operationalizes the decoupling of routing policy from action execution. ZETA resolves scientific intent before invoking specialized visual tools, treating measurement as a deterministic operation grounded in explicit geometry rather than generative output. This architecture exposes the "black box" of agent decision-making, allowing routing correctness and downstream execution to be evaluated as independent failure modes.
To our knowledge, we provide the first controlled study in scientific vision-agent routing that isolates explicit routing-policy specification while holding the legal action interface fixed. Evaluation on a zero-shot benchmark of 51 scientific-intent queries shows that explicit routing semantics can substantially improve routing accuracy, particularly at semantically adjacent action boundaries, although improvements vary across models. For Qwen 3.8, explicit routing-policy specification improves segmentation routing accuracy from 6.2% to 75.0% and detection routing accuracy from 60.0% to 100%. ZETA's execution traces make routing decisions and downstream artifacts separately observable, providing a basis for distinguishing intent-selection errors from visual execution failures. ZETA establishes the necessary infrastructure to isolate execution errors from interpretive ones, a critical requirement for deploying reliable scientific vision agents.

---


### 166. [Benchmarking Fine-Grained Visual Reasoning for Remote Sensing in Urban Management](https://arxiv.org/abs/2611.06770)

**<font color=#1a73e8>作者：</font>** Jiawei Zhang, Rizhao Cai, Dayan Guan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained visual reasoning is essential for remote sensing in urban management, yet remains underexplored in the evaluation of multimodal large language models (MLLMs). We introduce UMBench, a fine-grained urban remote sensing benchmark built from unmanned aerial vehicle (UAV) images for multiple urban management tasks such as traffic monitoring, urban construction, environmental quality, and disaster warning. Evaluations on UMBench reveal that current MLLMs often rely on scene-level priors and overlook fine-grained visual evidence. To address this issue, we further propose a novel evidence-first chain-of-thought method that directs models to inspect fine-grained visual evidence in a training-free manner. Experiments show that our method can improve the performance of both open-source and commercial MLLMs on UMBench.

---


### 167. [Ranking Agreement Does Not Reveal Paragraph-Edit Agreement in Two Released Paper Acceptance Predictors](https://arxiv.org/abs/2611.06789)

**<font color=#1a73e8>作者：</font>** Shaoliang Yang, Jun Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A fast acceptance classifier could select revisions for a slower evaluator. We ask whether agreement on existing papers supports that use. We compare a classifier of word and document features with two released text-only acceptance predictors fine-tuned from the same language model with three billion parameters. For 198 papers from the International Conference on Learning Representations, we compare model rankings of the original papers and of paragraph rewrites screened automatically for unchanged facts, claim strength, and attribution. The classifier ranks original papers closely with one predictor and moderately with the other, but shows no detectable agreement with either on which rewrites raise scores. The tests specified in advance used reduced numerical precision. Rounding error dominated the small score responses. We therefore rescored the released weights in full 32-bit precision as a post hoc check; edit agreement remained near zero. At this precision, when each predictor chooses among five rewrites per paper, its average raw score is under two points out of 100 higher than with random choice. The evidence covers presentation rewrites and two open predictors from one family; transfer to costly evaluators remains untested. Revision selectors should therefore be checked against the intended evaluator on the revisions they rank.

---


### 168. [Task-Efficient Agent Evaluation Using Cached Traces](https://arxiv.org/abs/2611.06803)

**<font color=#1a73e8>作者：</font>** Ben Johnson, Hayden Helm  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient benchmarking estimates a system's full benchmark performance from a small number of task executions. Standard approaches rely solely on the binary correctness of executions from a collection of already-evaluated reference systems. An agentic system, however, produces a rich trace for each execution that can reveal substantially more about its capabilities. Leveraging this information requires useful trace representations. We propose representing a trace by extracting a structured summary of it with an LLM and embedding the summary with a standard text encoder. These representations preserve correctness- and task-related signal while minimizing the presence of system identity-, model family- and harness-related signals that dominate raw trace embeddings. Given this representation for each task execution from all reference systems, we construct low-dimensional representations of the systems and predict a new system's score from its position among the reference systems. On SWE-bench Verified and Terminal-Bench 2.0, augmenting an item-response model with this geometry-based prediction reduces mean absolute error from 0.13 to 0.08 (Wilcoxon $p < 10^{-4}$) and from 0.14 to 0.12 (Wilcoxon $p < 10^{-3}$), respectively, when provided a single random executed task. Further, given access to the full set of reference systems, our approach dominates baselines for any given number of executed tasks on both benchmarks.

---


### 169. [Measuring Risk, Not Harm: Detecting Psychological Harm Risk Factors in LLM Conversations](https://arxiv.org/abs/2611.06806)

**<font color=#1a73e8>作者：</font>** Nil-Jana Akpinar, Eugenia Kim, Natalie Isak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Psychological harms from interactions with large language models cannot be monitored directly because they may emerge over repeated interactions and depend strongly on subjective individual user context. We propose measuring risk, not harm: detecting observable AI behaviors that constitute risk factors for psychological harm at the AI response level and aggregating these signals to support longitudinal monitoring. We operationalize eight such behaviors and construct a synthetic multi-label corpus of 47,062 AI responses and 373,873 response-factor labels, with targeted human annotations for validation and evaluation. We then compare trained embedding-based classifiers, direct LLM judging, and a classifier--judge cascade. All detectors are model-agnostic and operate only on LLM outputs, requiring no access to internal model states. We apply these detectors to several out-of-distribution human-AI conversation data sets from prior research. On held-out human-labeled data, the best cascade achieves macro precision of 0.86, recall of 0.76, and F1 of 0.79. On WildChat, it reduces LLM-judge calls by 97.1\% relative to direct judging. On DelusionEval, risk-factor detections cluster within conversations. Together, our results show that response-level behavioral risk-factor detection can provide a scalable measurement layer for longitudinal psychological-safety monitoring without conflating observable AI behavior with latent user harm.

---


### 170. [LLMs Don't Know What They Know: Benchmarking Temporal Self-Knowledge for Financial Backtesting](https://arxiv.org/abs/2611.06808)

**<font color=#1a73e8>作者：</font>** Lingfei Qian, Yan Wang, Xueqing Peng 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial backtests of large language models (LLMs) are meaningful only if the model did not already know the outcomes it is asked to predict. Practitioners guard against this by trusting a vendor's stated knowledge cutoff, by asking the model what it knows, or by instructing it to answer as of a past date. To verify whether any of these safeguards can be trusted, we introduce FinDendro, a benchmark of 2,226 dated U.S. facts from 1999 to 2026, covering monthly macroeconomic series, month-end stock prices and Federal Reserve decisions. Each fact yields four prompts: a value question, Recall and Predict questions that pair each candidate value with a claim of knowing or guessing without a declared date, and a Predict question with a historical declared date. Controls for persistence and dominant outcomes keep chance accuracy near 0.27. Results show that for most frontier models, self-reports understate knowledge. GPT-5 answers 76% of controlled facts correctly but claims to know 38%, and answers 61% of the facts it says it does not know. Knowledge claims can persist beyond the measured knowledge boundary, by up to seven quarters, and a declared date removes most of the claims of prior knowledge while leaving accuracy unchanged. Backtests inside a model's training window therefore cannot be certified leak-free by self-report, instruction or stated cutoff. These findings motivate behavioral measurement of temporal knowledge boundaries, and FinDendro provides a benchmark and procedure for selecting backtest periods based on demonstrated factual knowledge.

---


### 171. [SAUCE: Summary Analysis Using Conversation Entailment](https://arxiv.org/abs/2611.06812)

**<font color=#1a73e8>作者：</font>** Man-Ling Sung, Hemanth Kandula, Jeff Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the growing need for evaluating Large Language Models (LLMs) and their applications to speech, challenges persist in summarizing and evaluating conversations that lack a clear end goal. We introduce SAUCE -- a reference-free, fact-based evaluation pipeline for cross-lingual conversational speech summarization. It measures the accuracy and the fact coverage of a summary through the entailment between conversation and text. We compare SAUCE against several popular summarization metrics and demonstrate the effectiveness of capturing information loss due to transcription and translation error and identifying broken summaries. Crucially, unlike black-box LLM evaluators or dense embedding metrics, SAUCE is inherently explainable: it maps summary scores to discrete, verifiable facts, allowing users to pinpoint exact hallucinations or omissions. We illustrate how this interpretability helps developers systematically profile LLM behaviors and gives end-users an actionable tool to verify summary accuracy in noisy, real-world conditions. Preliminary investigations show SAUCE strongly align with human judgment.

---


### 172. [Rules, Traces and Routing Statistics: Training and Calibration Data for Open Models on ARC-AGI-2](https://arxiv.org/abs/2611.06827)

**<font color=#1a73e8>作者：</font>** Nguyen Minh Thang, Trinh Thi Phuong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study which training and calibration data help three open models solve ARC-AGI-2 tasks when the solver runs offline on four L4 GPUs for at most 12 hours. We compare data offline on public tasks and report 189 runs on the 120 hidden semi-private tasks. For the NVARC Qwen3-4B grid model, we built a corpus of 12,000 executable rules in a typed language and 95,993 tasks; a rule is admitted only if its behaviour on a fixed probe set differs from that of every admitted rule, and a task only if its pairs refute a shortlist of nearest competing rules and defeat 12 shortcut solvers. Continued fine-tuning on 1,920 real task records with revised four-GPU scheduling raised the semi-private score from 28.96 (mean of the released model) to 33.06 (mean of five runs, best 34.86); no checkpoint trained with synthetic tasks, even all 95,993 of them, improved on the real-task model. For the Qwen3.8-27B reasoning model, we fine-tuned on 1,036 of its own reasoning traces with correct final answers and compared sets that add traces of other models and synthetic tasks. With an inference procedure built around the model (a thinking cap enforced in the serving engine, a Python program checked on the demonstrations after each answer, a long first attempt per input), the score rose from 26.81 to 44.03, the level the ARC Prize Foundation measured for the base model without a time limit (42.36); most of the gain came from the inference procedure. For the Qwen3.8-Flash-Next mixture-of-experts model (125B parameters, 6B active), GPU memory limited concurrency. Pruning from 512 to 384 experts per layer by router-weighted activation saliency grew the key-value cache from 0.55M to 1.39M tokens; a 296-expert list adapted with ARC routing statistics, keeping experts for program tokens, plus an FP8 indexer cache, reached 1.96M. With a tool that checks programs, the model scored 56.67, our best result.

---


### 173. [Systolic Linear Attention: Co-Designing Tile-Grouped Gated Delta Attention for TPUs](https://arxiv.org/abs/2611.06828)

**<font color=#1a73e8>作者：</font>** Gagik Amirkhanyan, Nuojin Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gated-delta linear attention layers such as Gated DeltaNet (GDN), Kimi Delta Attention (KDA), and GDN-2 are tuned for GPUs, where small tensor-core tiles and fast vector registers make per-channel decay rescaling and sequential in-block solves cheap. On Google TPUs, which concentrate compute in wide $256 \times 256$ systolic matrix units backed by a slower vector unit, porting these layers directly leaves half of each matrix tile empty and bottlenecks on vector operations. We present \textbf{Systolic Linear Attention (SLA)}, which reshapes gated delta attention around the matrix unit by widening keys to $256$ with grouped value heads, grouping decay gates into four $64$-channel tiles, and computing the chunk solve entirely with block matrix products in a single fused kernel. On TPU v7x, a full \texttt{SLA-R4} layer runs $1.6\times$--$2.5\times$ faster than the open-source Tokamax KDA kernel ($1.4\times$--$2.4\times$ with exact chunk inversion), driven primarily by head sharing and kernel fusion. Across a $2{,}048$-chip TPU v7x pre-training study of sparse Mixture-of-Experts (MoE) models from $6.5\text{B}$ to $63.1\text{B}$ parameters, SLA trains $11\%$--$24\%$ faster than KDA at similar perplexity, and reaches slightly lower perplexity than KDA in smaller matched-seed runs.

---


### 174. [LooM: Loop-Invariant Memory for Causal Encoder-Decoder Language Models](https://arxiv.org/abs/2611.06835)

**<font color=#1a73e8>作者：</font>** Lele Yang, Muxi Diao, Zhonghao Yan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped Transformers increase effective depth by re-executing shared layers, but three limitations hinder their adoption: memory grows with the loop count, compute can only be adjusted in whole-block steps, and the loop count is hard to change after training. We propose LooM (Loop-invariant Memory), which addresses each in turn. In a causal encoder-decoder (CED), LooM loops only the decoder layers after the first, which read a global memory written once per token, and each of them publishes the key-value (KV) entry for a token only on its first visit, so the cache does not grow with the loop count. These layers loop independently, providing every budget from 3 to 21 layer executions per token, and one model trained on randomly sampled budgets covers all of them without a router. With enough loops, LooM outperforms a single-pass baseline trained on the same data on language modeling, zero-shot accuracy and long-context perplexity, while using the same cache size. Our analysis further shows that the training budget distribution decides what extra depth buys. These results suggest that a CED is a natural place to loop: memory is written once, and depth becomes a budget chosen at deployment.

---


### 175. [Context--Answer Metamodels: Forecasting LLM Activations Before the First Answer Token](https://arxiv.org/abs/2611.06837)

**<font color=#1a73e8>作者：</font>** Tommy He, Thomas Jiralerspong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Under stochastic decoding, a single context can elicit many different answers from a language model. Characterizing this variation typically requires many expensive autoregressive rollouts, each revealing only one realization. We ask whether the activations produced while reading the context can directly forecast the model's rollout activations. We train context--answer metamodels that map a context activation sequence to point or distribution forecasts of mean-pooled answer activations. We find that (i) the four metamodel families we study forecast mean-pooled answer activations with high fidelity, and the distribution metamodels also capture rollout variability; (ii) performance improves as the training set grows to 500,000 prompts, and the metamodels generalize zero-shot to out-of-domain datasets; (iii) their forecasts retain behavior-predictive signal; and (iv) context activations from Qwen2.5 predict mean-pooled answer activations from Qwen3.5 and Gemma 4, suggesting that activation forecasts can transfer across models. Together, these results suggest that context activation traces can support scalable forecasts of behaviors in LLM answers before the first answer token is generated.

---


### 176. [Before You Continue: Evaluating Time-Sensitive Safety Awareness in Conversational Assistants](https://arxiv.org/abs/2611.06839)

**<font color=#1a73e8>作者：</font>** Peidi Dong, Yunze Xiao, Yu-Lin Tsai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) assistants increasingly help users with everyday activities that involve time-dependent constraints. However, users may not mention these constraints in later requests, requiring assistants to recognize and adjust their advice accordingly. To evaluate such capability, we introduce TASC (Temporal Action Safety in Conversation), a benchmark that evaluates whether LLMs apply time-dependent constraints when responding to conversational requests. TASC consists of 3,418 inputs derived from 128 templates, along with a separate set of 33 scenarios designed to compare models' ability to calculate elapsed time with their ability to apply that information. Across 13 models, assistants account for time-dependent constraints in only 30.5% of cases where the proposed action violates a rule, while rarely warning users unnecessarily. More importantly, models fail to apply these constraints in 62.1% of cases despite correctly calculating the elapsed time. Explicitly providing the timing resolves only about half of these failures, revealing a gap between temporal reasoning and its application in conversational advice.

---


### 177. [Same Layout, Different Count: What Number Words Do Past Ten in Text-to-Image Models](https://arxiv.org/abs/2611.06840)

**<font color=#1a73e8>作者：</font>** Liang Yue, Eric A. Vance  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ask SD3.5-Medium for twelve of an object and then, from the same starting noise, for twenty-five. The picture keeps its layout, but the count changes about as much as it would under a new random seed, and in no consistent direction. We study what number words do once a request passes about ten objects, in five open text-to-image models. Holding the object and the starting noise fixed, we change one thing at a time, and people who never see the request count 3,088 of the images. Every model follows the number for small crowds, but only up to a point, its reach: SD3.5-M and FLUX.1-dev stop following it soon after ten, while FLUX.2 [klein] and Qwen-Image follow it loosely up to twenty-five. Beyond SD3.5-M's reach, the coarse part of the starting noise fixes the composition of the picture but not how many objects it holds: redrawing only the noise finer than an eighth of the image keeps the layout as well as a new number does, and already moves the count two-thirds as far. The number word still reaches the denoiser and acts in its first steps, but nothing we tried gives it a clear direction. Shown instead as a noised grid in the starting latent, the count is drawn: people find it in 59% of images, against 4% when it is only told. Past ten, an exact-match score barely separates a model that follows the number loosely from one that ignores it, and a relative-error score can even prefer a constant guess of sixteen. A same-noise test with a few requests per object tells them apart.

---


### 178. [ServerBench: How can your coding agents design specialized LLM serving systems?](https://arxiv.org/abs/2611.06841)

**<font color=#1a73e8>作者：</font>** Xinrui Zhong, Zhiming Wang, Yongqi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) coding agents develop software through experimentation, offering an opportunity to design the serving systems supporting their own operation. Effective serving requires coordinating implementation and operating decisions under session dependencies, latency constraints, and correctness requirements. We introduce ServerBench, a benchmark for agentic design of complete, specialized LLM serving systems. Agents experiment against a common objective, dollars per dollar: latency-qualified token value per dollar of GPU cost. Stateful replay preserves session dependencies, and independent verification checks the submitted system. Across 11 coding-agent models and three deployments, Claude Sonnet 5.5 achieves 2.97 dollars per dollar on Gemma E4B, $4.87\times$ the vLLM reference; 22 of 33 runs yield verified systems, and 13 exceed the strongest baseline. Our analysis identifies three findings: high-value designs coordinate capacity improvements with load selection; agents interpret performance feedback through workload-relevant experiments; and reliable delivery requires verification of the execution paths introduced by optimization. Overall, ServerBench supports systematic study of how agents translate service objectives and feedback into effective, verified serving systems for given task specifications.

---


### 179. [Where to Connect? Boosting MLLMs via Dynamic Gated Pathways across ALL ViT and LLM Layers](https://arxiv.org/abs/2611.06844)

**<font color=#1a73e8>作者：</font>** Yingying Yan, Jiaqi Tang, Wei Wei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A central yet under-explored question in Multimodal Large Language Models (MLLMs) is where to connect---how visual information from a hierarchical vision encoder should be wired into the layer-wise semantics of a large language model. Mainstream MLLMs inject a fixed single-layer visual representation into the LLM and treat all LLM layers as a single consumer, ignoring that different layers demand different visual granularities. Recent multi-layer fusion methods either compress hierarchical features on the encoder side or rely on predefined sparse or hierarchical layer-to-layer connections, and therefore stop short of modeling adaptive cross-layer interactions between the ViT and LLM hierarchies. We address this gap with DGP (Dynamic Gated Pathways), a routing mechanism that establishes all-to-all connections between every ViT layer and every LLM layer, with each LLM layer dynamically gating its preference over visual layers conditioned on its own semantic state. Built on top of LLaVA-1.5-7B and 13B, DGP delivers consistent gains over the LLaVA-1.5-7B baseline (e.g., +4.2 on SQA$^{I}$, +3.3 on MM-Vet, +3.1 on VizWiz and LLaVA$^{W}$) and surpasses prior multi-layer visual fusion methods on most benchmarks. Layer-wise routing analyses further show that different LLM layers do select different visual granularities on demand, supporting both the effectiveness and interpretability of the proposed dynamic gated pathways. The code is available: this https URL.

---


### 180. [Persona Perspectives: Adopting Viewpoints Reorganizes Representations in LLMs](https://arxiv.org/abs/2611.06848)

**<font color=#1a73e8>作者：</font>** Austin C. Kozlowski, Avital Mintz, Madison Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Common methods for monitoring features in large language models (LLMs) such as linear probes and sparse autoencoders (SAEs) assume that features maintain a consistent representation across contexts. LLMs, however, can flexibly adopt different perspectives or "personas" that suggest different underlying systems of conceptual relations. In this paper, we examine whether prompting an LLM to adopt a persona alters the representational geometry of the model's latent space. We extract representations of over 9,000 common words and 33 semantic axes from models adopting liberal and conservative political personas and compare these against two neutral baselines. We find that persona conditioning systematically alters both the projections of words onto semantic axes and the alignments among the axes themselves in directions consistent with the specified ideology. We then test the implications of this reorganization for two safety-relevant features: truthfulness and morality. Linear probes, SAE-based classifiers, and classifiers built from manually selected word representations, all trained without a persona, produce divergent results when applied to models conditioned on political personas, producing politically slanted ratings of truth and morality on controversial statements. These findings suggest that internal representations, as they are conventionally extracted, can exhibit different geometric relations when the model adopts personas, potentially undermining monitoring efforts.

---


### 181. [Visual Token Routing: Learning to keep tokens that matter](https://arxiv.org/abs/2611.06854)

**<font color=#1a73e8>作者：</font>** Pranjal Aggarwal, Sean Welleck  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) have recently achieved superhuman performance on several long-horizon benchmarks. However, their computational cost limits their use in long-horizon tasks and real-time domains such as video games. A key bottleneck is representing each screenshot as thousands of visual tokens, which accumulate into long contexts as agents reason over extended interaction histories. We observe that most of these visual tokens are either semantically irrelevant to the agent's next action or temporally redundant across screenshots. Building on this observation, we introduce Visual Token Routing (VTR), a joint training framework for learning sparse visual representations that preserve the information needed for action prediction. In VTR, we train the vision-language model together with a lightweight spatio-temporal router that examines each image region in the current and previous screenshots and decides whether its visual token enters the language model. We optimize the router using an adaptive loss to keep the number of visual tokens as small as possible while minimizing performance degradation. With just 2,000 training steps, VTR matches the performance of the full-resolution model on OSWorld, CUA-World, and video game action prediction, while using 2.5-5.8x fewer visual tokens. These savings reduce inference cost by up to 3.3x and speed up prefill by up to 2.9x. VTR also outperforms lowering the image resolution and other baselines for dropping tokens, by up to 12.8 points on OSWorld. Overall, VTR enables computer-use agents to process only the visual tokens they need, allowing them to be used in long-horizon tasks and real-time domains at a fraction of the computational cost. Code and models are available at this https URL

---


### 182. [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856)

**<font color=#1a73e8>作者：</font>** Haoxiang Cao, Yuxuan Zhang, Penghui Du 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce LongBanana, to our knowledge the first expert-designed and expert-verified benchmark for long-context multi-reference image synthesis in the age of agent-driven image generation. The task requires retrieving dispersed visual evidence, rejecting distractors, binding entities and relations, and composing one coherent final image from multiple references. LongBanana contains 90 carefully designed tasks organized by a 3-by-3 taxonomy; each task includes about 32 reference images, 20 constraints, and 50 evaluation items, yielding 4,670 expert-specified atomic evaluation items in total. Its graph-grounded evaluation design instantiates each task with reference images and an entity-relation graph, then converts node, edge, and whole-graph obligations into checklist items for Content Fidelity, Relational Binding, and Global Constraint Satisfaction. Reviewed expert labels include a 15% double-labeled subset with 89.4% exact agreement and 0.83 quadratic weighted kappa. We further introduce LongBanana-Gen, an agent-harness framework for long-horizon image generation; experiments show that minimal agent harnesses improve over direct generation, while a ReAct-Plan-Exec-Reflect (RPR) workflow yields harness-dependent gains by strengthening evidence grounding and repair. Together, LongBanana provides an auditable testbed for measuring dense visual evidence use and a shared target for developing stronger agent-driven image-generation systems. Code and data are available at the project page: this https URL.

---


### 183. [CompressionBench: How can your coding agents compress LLMs?](https://arxiv.org/abs/2611.06858)

**<font color=#1a73e8>作者：</font>** Xinrui Zhong, Zhifeng Li, Zhiming Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement requires AI systems to improve the models and infrastructure used by subsequent systems. LLM compression offers a concrete efficiency objective: retain a pretrained model's behavior within a smaller model storage budget. We study whether coding agents can carry out this step autonomously. We formulate compression as a terminal task in which an agent receives a source checkpoint, storage limit, inference environment, and time budget, then constructs compressed weights and executable inference code. The agent controls its algorithm and experiments; perplexity feedback guides search, and independent verification checks the final model. Across six agents and six model--size settings, 29 of 36 submissions pass verification. Selecting the lowest-perplexity agent design per task yields an average 3.4% perplexity increase over BF16 and 77.33% downstream accuracy, compared with 79.56% for BF16. Recorded experiments reveal how agents achieve these outcomes and where improvement breaks down. Agents lower PPL in 21 of 24 revisions at nearly fixed storage; complete-model feedback reverses 17 of 79 prior local rankings; and generation and inference tests expose failures that likelihood alone misses. The results identify representation design, experimental judgment, and capability validation as central to agent-driven model compression, a measurable component of efficiency-oriented self-improvement.

---


### 184. [On Turn-Level Best-of-N Sampling for Scaling LLM Agents](https://arxiv.org/abs/2611.06868)

**<font color=#1a73e8>作者：</font>** Jalaj Bhandari, Dhawal Gupta, Hongli Zhan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work, we evaluate a simple inference-time scaling approach based on \textit{turn-level best-of-N sampling} (\method) for large language model (LLM) agents on complex, long-horizon tasks. We instantiate this using a \textit{generator-selector} framework with two LLMs; at each turn, a \emph{generator} model generates $N$ candidate actions and a \emph{selector} model selects one of them, which is then executed in the environment. This paper is closely related to the work of \cite{zainullina2025guided} who used critic models for guided search at inference time. Different from their work, we evaluate if off-the-shelf, open-weight LLMs can be effective at comparing different candidate actions directly. Experiments on long-horizon terminal tasks show that \method can lead to significant performance improvements, both in terms of accuracy (5--10\%) and consistency across repeated attempts. Analysis of agent trajectories reveal a shift in agent behaviour towards desirable patterns such as reduction in number of attempts to solve the task, improved task instruction following, debugging and testing.

---


### 185. [SpecCompact: Accelerating LLM Agent Context Compaction with Slot-Parallel Semantic Speculative Verification](https://arxiv.org/abs/2611.06876)

**<font color=#1a73e8>作者：</font>** Yulu An, Yifei Feng, Xiangyang Yin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents use context compaction to manage growing interaction histories, but summarizing long histories with large models can introduce substantial delays. Compaction therefore requires balancing information retention against latency. We observe that structured summary slots can retain information when generated independently. Based on this observation, we present SpecCompact, a framework that accelerates compaction through slot-parallel semantic speculation. SpecCompact fine-tunes a small drafter and generates slots in parallel. The target model verifies each proposed line and repairs rejected content, while subsequent drafting uses the updated slot prefix. System optimizations further reduce repeated context processing and model calls. Across AppWorld and $\tau^3$ benchmarks with two target models, SpecCompact achieves $2.04$--$5.63\times$ compaction speedups over Hermes-style summarization. Separate downstream evaluations reveal model- and task-dependent performance trade-offs. A user study within Hermes further shows an $8.68\times$ median compaction speedup.

---


### 186. [Dull, Dirty, Dangerous? Working Conditions and the Limits of Occupational AI Exposure](https://arxiv.org/abs/2611.06888)

**<font color=#1a73e8>作者：</font>** Siyi Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automation is often justified as relief from dull, dirty, and dangerous work. I examine how these conditions relate to occupational AI exposure using 21 O*NET items across 754 US occupations. Higher exposure is associated with lower condition scores under a large language model (LLM) measure and AI Occupational Exposure (AIOE), with equal occupation weights and employment weights. Adjustment for physical demands, required education, training and experience, and wages reduces the composite association. The adjusted confidence intervals include zero for LLM exposure and remain below zero for AIOE. Separating repetition from restricted discretion also changes what the combined Dull score conveys. These comparisons show how item groupings and occupational characteristics shape the interpretation of exposure estimates. Occupational profiles offer a starting point for selecting contrasting research settings. Establishing desired automation or realized relief requires evidence about workers' preferences and specific interventions.

---


### 187. [BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories](https://arxiv.org/abs/2611.06911)

**<font color=#1a73e8>作者：</font>** Fei Lin, Tengchao Zhang, Ziyang Gong 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-Driving Chemical Laboratories (SDCLs) are moving chemical experimentation toward embodied automation, where machines must perceive laboratory scenes, reason about experimental states, and act under physical, procedural, and safety constraints. Although Multimodal Large Language Models (MLLMs) are increasingly considered as embodied brains for such systems, existing laboratory benchmarks mainly focus on safety, anomaly detection, or general scientific understanding, leaving their execution-oriented embodied capabilities underexplored. To fill this gap, we introduce BEAKER, a Benchmark for evaluating Embodied Actionability, Knowledge, Experimentation, and Reasoning in SDCLs. BEAKER contains 1,000 expert-curated question-answer samples across 11 image and video task types, covering key judgments required for chemical laboratory execution, including affordance grounding, trajectory planning, equipment, state, and safety recognition, apparatus setup, operation and step reasoning, and temporal procedure reasoning. All questions and annotations are manually created and reviewed by chemistry and embodied Artificial Intelligence (AI) experts, without AI-assisted generation or annotation. We evaluate 28 general-purpose, science-oriented, chemistry-specialized, and embodied MLLMs in an offline, single-turn setting. Results show that current models can follow coarse experimental procedures in videos, but still struggle to ground actions into operable regions and feasible trajectories, to recognize fine-grained laboratory apparatus, states, and safety norms, and to order steps in mid-length procedures. BEAKER thus reveals a clear gap between coarse procedural understanding and the precise, action-grounded perception required for laboratory execution, providing a diagnostic benchmark for future MLLMs in SDCLs.

---


### 188. [A Framework for Context Enrichment and Selective Robustness in LLM Social Agents](https://arxiv.org/abs/2611.06914)

**<font color=#1a73e8>作者：</font>** Mattia Greiche, Reihaneh Rabbany, Maximilian Puelma Touzel  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Researchers use large language models as agents in social simulations, where agents are prompted with observations and background information intended to shape their actions. Yet LLM agents have been shown to substantially change their behavior under meaning-preserving prompt variations, creating a validation problem for social simulation. One plausible hypothesis is that this brittleness reflects a lack of grounding and can be reduced by enriching the context provided to the agents. Whether richer context improves robustness remains unclear, in part because context richness and robustness are rarely defined in ways that support controlled comparisons. We address the first need with controlled context enrichment, a set of prompt substitution rules that systematically enriches distinct types of context: neutral padding, generic social background, descriptive decision grounding, and normative decision grounding. We address the second by introducing selective robustness as a validation criterion: insensitivity to meaning-preserving prompt variation combined with a directional response to decision-relevant changes in the social world. We demonstrate the framework in a Prisoner's Dilemma-like game, showing how it can be used to identify which forms of context enrichment produce more desirable and robust agent behavior. We find that these forms of enrichment produce distinct behavioral patterns that vary between the two models tested.

---


### 189. [From Pixels to Actions - Towards Native Vision-Language-Action Policies](https://arxiv.org/abs/2611.06918)

**<font color=#1a73e8>作者：</font>** Weichen Fan, Haiwen Diao, Penghao Wu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes. This raises a fundamental question: should action policies inherit a fixed visual endpoint, or directly access evolving visual computation? We introduce NEO-VLA, a structurally encoder-free vision-language-action framework. Images are tokenized by lightweight patch convolutional layers and evolve jointly with language throughout the backbone, allowing a flow-matching action expert to draw from instruction-conditioned visual representations at different depths. This simple change reveals a consistent pattern. Native architectures outperform encoder-based counterparts under controlled comparisons; full fine-tuning reduces but does not erase the gap, and additional scale alone cannot recover it. More strikingly, layer-wise probing shows that the action-critical signals often peak well before the final visual representation. Across diverse manipulation settings and distribution shifts, NEO-VLA consequently achieves stronger and more robust control. Together, these results suggest that embodied control benefits from access to visual representations across the computational hierarchy, rather than a fixed encoder output.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 190. [Agent Harness Awareness: Turning Verified Telemetry into Operational Control for Tool-Using Agents](https://arxiv.org/abs/2611.05391)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Manu Agrawal, Shrey Nagpal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool descriptions tell an agent what an action can do, but they do not necessarily reveal whether that action is healthy or suitable at the moment of use. Execution harnesses often possess this information through monitors, traces, and recent failures while the model choosing the next action does not. We call this gap operational blindness. We introduce Agent Harness Awareness, a trust-separated design in which the host supplies a small, fresh, verified state snapshot before a consequential action while retaining measurement, enforcement, evaluation, and final dispatch authority. We test its tools-and-network instance with ToolRoute, a controlled isolation benchmark that holds the task and candidate semantics constant and varies the operational information available to the model. In a 216-decision ablation across GPT-5.6 Sol, Claude Sonnet 5, and Gemini 3.7 Flash, verified tool-health state reduced mean observable policy regret by 96.9% against a same-shape neutral control (4,252 ms to 131 ms) and raised single-dispatch completion from 69.4% to 95.8%. In a separate 27-decision end-to-end replication with live local TCP/HTTP execution, OpenTelemetry client spans, and Toxiproxy-injected faults, verified state reduced mean regret from 8,956 ms to 0 ms (zero excess observable operational cost) and completed the live action in 9/9 model-by-fault cases versus 5/9 for the neutral control. These studies establish the tools-and-network instance of Agent Harness Awareness: selected host telemetry materially improves pre-dispatch operational choice. Runtime state, hardware pressure, economics, retry-aware recovery, and heterogeneous selection remain open empirical extensions of the same architecture.

---


### 191. [Relevance Propagation as Entropic Optimal Transport on Filippov Neural Networks: Sinkhorn Propagation and Region Relevance in Image Classifiers](https://arxiv.org/abs/2611.05594)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Olivier Gibaru, Eric Nyiri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relevance propagation, which redistributes a network's prediction backward through the layers, is usually treated as a heuristic. We show that it is the solution of a single variational problem: Layer-wise Relevance Propagation (LRP) is the divergence-free flow on the active computational graph of zero relative entropy to the backward transition law of the forward activation flow; for a non-negative reference, this is a relative entropy between Markov measures on backward paths. The rules LRP$_0$, LRP$_{z^+}$ and LRP$_{\alpha,\beta}$ follow from this principle by the choice of a reference, and are instances of one rule, LRPN$_{\alpha,\beta}$, whose weights may vary from node to node, for instance with the node's activity, in the spirit of Hebb's principle. The principle rests on a measure-theoretic formalization of feed-forward networks as directed acyclic graphs of Filippov operators, which covers piecewise-smooth and discontinuous architectures (e.g. hard-routed Mixture-of-Experts) with a Clarke-Filippov generalized-gradient calculus; it also characterizes backpropagation as the adjoint equation of a Lagrangian relaxation. On networks of ReLU and max-pooling nodes, LRP$_0$ is Gradient$\times$Input, with an explicit jump across a kink where LRP$_{z^+}$ stays continuous. Taking the entropy edge by edge yields a new rule, Sinkhorn Relevance Propagation. Aggregated over an input region, the flow of a non-negative reference tells, with exact accounting, which hidden units carry its evidence, the conditioned flow being a Schrödinger bridge. On VGG-16, the conservation identities hold to round-off, and the rules are told apart by the sign of their maps, the share of the output left to the bias nodes, faithfulness, localization and class dependence; on ConvNeXt-Tiny, LRPN$_{\alpha,\beta}$ conserves the output and its Hebbian weights give the highest ABPC of the rules tested.

---


### 192. [Quantifying Trait-State Hierarchy in EEG Foundation Model and Signal Processing Embeddings](https://arxiv.org/abs/2611.05652)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Anusha Madapura, Aditya Kommineni, Shrikanth Narayanan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) measures brain activity through recording electrical potentials of the scalp. EEG recordings capture two distinct sets of characteristics in the signal: (1) \emph{Traits} -- information that remains relatively constant over the course of a recording session, such as subject identity, age, and sex; (2) \emph{States} -- signatures that encode responses to external stimuli, including visual, auditory, and motor information. There is limited understanding of how different EEG modeling features (signal processing and foundation models) encode state and trait characteristics. In this work, we quantify state- and trait-level features captured by EEG embeddings using a hierarchy metric and kNN purity on Brain-Computer Interface dataset trials, and find that a majority of EEG features form a macro-trait hierarchy (embeddings form trait-level clusters with micro-states within). Our linear probe results indicate that this hierarchy structure leads to suboptimal state distinguishability, negatively impacting BCI performance of EEG foundation models. To mitigate this, we explore normalization techniques that reduce trait-specific information in embeddings and provide a $\sim$ 10\% improvement in balanced accuracy for state classification. Additionally, we observe that when fine-tuning models for downstream state decoding, embedding spaces transform from macro-trait to macro-state hierarchies, which in turn lead to better state decoding.

---


### 193. [Toward a Compositional Knowledge Architecture for a Shared Organizational Cortex](https://arxiv.org/abs/2611.05753)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Andrew Miracle, Phyl Georgiou, Christine Okoth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizations accumulate evidence in conversations, documents, decisions and relationships, but they act on interpretations: judgements assembled from several observations, resting on assumptions, and revised as circumstances change. Existing retrieval, knowledge graphs and agent memory keep the records and lose the interpretation. We propose a four-layer architecture, Signals, Domains, Claims and Dimensions, in which interpretations persist with their justifications and standing, a truth-maintenance network revises that standing as evidence changes, and validated, versioned Dimensions position interpretations on named axes. We call the result a shared organizational cortex. In a registered retrieval experiment, the Dimension term gains 0.028 nDCG@10 (p = 0.002). In system-level comparisons, the full retrieval configuration improves nDCG@10 by 0.081 over Signals-only and 0.053 over graph-augmented Signals-only retrieval (both reported p < 0.001). The architecture gives organizations a persistent, revisable basis for shared judgement.

---


### 194. [A low-rank decoder bottleneck bounds reliability in foundation-model perturbation prediction](https://arxiv.org/abs/2611.05849)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zheyu Zhang, Yuanhao Huang, Fan Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation-model predictors of perturbation response are evaluated primarily by aggregate accuracy. Using their predictions to prioritize experiments requires assessing each prediction's reliability. We audit the state-transition (ST) decoder used in STATE across three encoders (SE-600M, scGPT, and Tahoe-x1) and four cell lines under CRISPRi. The decoder's first attention layer has a low-rank output. Projecting this output onto 4-32 fixed directions estimated from training activations preserves mean per-perturbation Pearson delta correlation (PDC). This low-rank attention bottleneck bounds the decoder's reliability by distance to training responses: PDC declines as the cosine distance from a perturbation's observed response to its nearest training response increases. We propose predicted-NN-distance, the cosine distance from a predicted response to its nearest training response, as a per-prediction confidence score. The score has a mean absolute Spearman correlation of 0.81 with PDC, close to the 0.88 obtained with the observed response. Thresholds calibrated on this score transfer across encoders and cell lines, and the score remains predictive of PDC for drug perturbations.

---


### 195. [Decouple to Reuse: Fine-Grained Knowledge Augmentation for Time Series Foundation Models](https://arxiv.org/abs/2611.05993)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuqian Wu, Qingxiang Liu, Yuxin Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting is critical for demand prediction and resource management in modern Web services, yet applying pretrained Time Series Foundation Models (TSFMs) to downstream tasks remains challenging due to domain shifts. Existing retrieval-augmented approaches typically retrieve coarse-grained window contexts and may introduce context-specific noise. To address this problem, we argue that temporal patterns should be reused at a decomposition level, as effective trend and seasonal dynamics may originate from different contexts. We propose \method, a two-stage \underline{F}ine-grained \underline{K}nowledge \underline{A}ugmentation framework that decouples and consolidates pre-training knowledge into compact, task-shared residual codebooks to enhance frozen TSFMs. Specifically, Stage I constructs dual-branch residual codebooks for decoupled trend and seasonal signals, while Stage II dynamically retrieves and merges these fine-grained patterns into target representations via task-adaptive aggregation and gate fusion. Extensive experiments across eight real-world benchmarks with four representative TSFM backbones demonstrate the superior effectiveness and computational efficiency of \method, while further validating the strong transferability of the residual codebooks across different backbones. The source code is available at the anonymous repository: this https URL

---


### 196. [Intra-Architecture Source Attribution for Stable Diffusion: A New Task with Benchmark Dataset and Baseline](https://arxiv.org/abs/2611.06000)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ashutosh Dayal, Mallika Garg, Debashis Sen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Designing systems that attribute a generated image to its source model has lately become a major area of AI research. Most existing datasets and systems related to image source attribution are targeted towards the detection of architectural signatures of the source models. Distinct from this, focusing on stable diffusion, we introduce a novel task, IntrAA-SD, Intra-Architecture source Attribution for Stable Diffusion, where the source models to be differentiated share the same architectural backbone and differ only due to fine-tuning. The proposed task aligns with the emergence of fine-tuned generators having the same architecture, like Juggernaut XL and RealVis XL, which are fine-tuned versions of Stable Diffusion XL (SDXL). We provide a first-of-its-kind $140$K-image benchmark dataset containing images generated from different fine-tunes of SDXL, along with in-domain and out-of-distribution prompts. We also provide a baseline framework for IntrAA-SD, which leverages a style-conditioned Mixture-of-Experts network. It uses a frozen CLIP backbone to capture the image style and gate the MoE, which processes fine-tuned trace features from a high-resolution LoRA-adapted DINOv2 network. The fine-tuned models used, the prompting strategies considered, and the formation details employed in the novel dataset are elaborated. Our baseline intra-architecture source attribution method is evaluated in terms of attribution accuracy on our dataset, and ablation studies are also performed. Code and dataset is available at this https URL.

---


### 197. [Securing Web Agents with the Compile-Then-Execute Paradigm](https://arxiv.org/abs/2611.06039)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Annabella Chow, Jinhao Zhu, Sylvie Venuto 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web agents commonly follow the ReAct paradigm, selecting each action from runtime observations that inherently mix trusted and untrusted content. This design makes their control flow vulnerable to prompt injections embedded in webpages. We introduce Baya, a compile-then-execute web agent designed to prevent prompt-injection-driven control-flow hijacking by design. Before accessing the live website, Baya compiles the user's request into an executable Python program that calls a Trusted Website API. The planning model does not observe live website content; only the compiled program processes it. Untrusted data may determine program values or select among branches defined during compilation, but it cannot redefine the user task or cause the model to synthesize new website operations at runtime. The Trusted Website API gives the compiler a unified view of the website's action space, enabling ahead-of-time planning without the stepwise action discovery required by reactive agents. Our evaluation across 581 valid WebArena Verified tasks shows that Baya achieves 77.8% aggregate utility, outperforming browser-only ReAct (55.1%) and API-enabled ReAct (66.7%). On WASP, a security benchmark for web agents, Baya achieves 0% attack success rate, compared with 16.2% for API-enabled ReAct and 25.5% for browser-only ReAct.

---


### 198. [UniRestorer++: Scalable Universal Image Restoration with Multi-Granularity Degradation Modeling](https://arxiv.org/abs/2611.06042)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jingbo Lin, Zhilu Zhang, Fan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Universal image restoration aims to handle diverse degradations within a single model, but a reliable scaling strategy remains underexplored. Increasing backbone depth and width can lead to performance saturation, while degradation-aware specialization depends on accurate degradation estimation and is vulnerable to errors on out-of-distribution and real-world inputs. We propose UniRestorer++, a scalable framework based on multi-granularity degradation modeling. It progressively refines degradation groups and introduces group-specific experts, coupling capacity growth with specialization. Degradation-estimation-based routing selects a root-to-leaf path, while granularity-estimation-based routing chooses a level along that path to balance specialization and robustness. Spatially dense degradation representation maps further enable region-aware routing for spatially non-uniform corruptions. We develop CDD-50, a benchmark covering 50 degradation categories from single to penta-degradation. Experiments show approximately log-linear PSNR trends over the evaluated model-size range and stronger scaling gains on out-of-distribution and real-world data than vanilla MoE scaling. UniRestorer++ achieves state-of-the-art performance across benchmarks and demonstrates zero-shot generalization and few-shot transfer on real-world images. Code: this https URL

---


### 199. [XuanJian-DINOSAR: A SAR Foundation Model Based on Global and Local Semantic Consistency](https://arxiv.org/abs/2611.06105)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chunxiao Wu, Huixin Huang, Jialei Pan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised pre-training on synthetic aperture radar (SAR) imagery enables transferable representations, but the optical-SAR domain gap and speckle perturbations limit representation stability. Most SAR foundation models use masked image modeling (MIM) through pixel reconstruction or structural feature prediction, which is sensitive to speckle or relies on predefined operators. Joint modeling of cross-view semantics and perturbation stability at corresponding spatial locations remains underexplored. We propose XuanJian-DINOSAR, a SAR foundation model based on global and local semantic consistency. We curate over 360K publicly available SAR target chips, detection images, and scene images spanning diverse targets, scenes, and sensors, and adapt an optically pre-trained DINOv2 model to SAR through self-supervised learning. The framework combines DINO global semantic self-distillation, iBOT local masked modeling, and KoLeo feature-distribution regularization to learn globally discriminative and locally structure-aware representations. We introduce a local semantic consistency branch tailored to SAR intensity statistics and coherent imaging characteristics. Shared geometric transformations produce spatially aligned teacher weak views and student strong views. Intensity transformations and Gamma multiplicative speckle perturbations are applied to student views, while a cosine consistency loss aligns patch tokens at corresponding locations, promoting stability under radiometric perturbations. This objective complements the cross-region and cross-scale semantic consistency of DINOv2 multi-crop training, jointly enforcing global and local semantic consistency. Experiments on multiple downstream classification and detection datasets demonstrate state-of-the-art performance on most evaluation metrics, validating the generality and transferability of the learned representations.

---


### 200. [ReactWorld: Structuring Interaction Responses for Embodied Video Generation](https://arxiv.org/abs/2611.06120)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hanwei Liu, Huijia Zhang, Hanzhang Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied video world models predict scene changes caused by robot actions, yet generated object responses may remain inconsistent with task intent and contact dynamics. Critical responses in embodied scenes often concentrate in local regions and specific time intervals. Inspired by chain-of-thought reasoning, we introduce ReactWorld, an embodied video generation model guided by structured interaction anticipation. In the generation backbone's feature space, an interaction response field predictor anticipates how the interaction will unfold, explicitly describing participant roles, future motion response intensity, and local motion changes. A response feedback adapter forms increments to object features from the difference between the object branch's outputs with predicted and zeroed local dynamics inputs. It also converts predicted displacements into positional biases for temporal attention. These two mechanisms guide object feature updates and information retrieval across frames, respectively. Through interaction anticipation and generative feedback, ReactWorld achieves an average score of 77.51 on RBench, outperforming PhysisForcing by 3.29 points with improvements in all nine categories. On EZS-Bench, it achieves a Domain score of 86.98 and an average score of 81.87.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-207](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
