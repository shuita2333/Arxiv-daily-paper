# 🧠 大模型相关研究 | 2026年10月12日

> 本类共 **288** 篇论文：已确认 **273** 篇，待复核 **15** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-288**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-288**

---

### 251. [Overcoming Prior Barriers: Supervised Fine-Tuning under Long-Tail Distribution](https://arxiv.org/abs/2610.12345)

**<font color=#1a73e8>作者：</font>** Haohui Wang, Jiahao Xu, Wangzhi Zhan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) adapts pretrained large language models (LLMs) to downstream tasks, but the required concepts can receive substantially different levels of pretrained support. Frequent concepts are more likely to be well learned, whereas rare concepts may remain weakly represented. We introduce a novel notion named prior barrier to quantify how strongly the pretrained model supports competing concepts over the target concept. We observe that prior barriers follow a long-tail distribution, placing head and tail concepts at different starting points for SFT: head concepts face lower prior barriers, whereas tail concepts require additional instructions to overcome their higher prior barriers. Our theoretical analysis further derives a predictive risk bound for SFT under long-tail prior barriers, explicitly characterizing how the prior barrier and accumulated SFT evidence jointly determine predictive performance. Motivated by this prior barrier-dependent demand, we propose PASS, an adaptive SFT instruction selection method that constructs reference-derived concepts and estimates the distinguishing evidence provided by each instruction, and adaptively allocates the selection budget toward concepts that remain insufficiently covered under the current selection. In this way, PASS jointly considers which instructions can provide useful evidence and where additional supervision is needed under a limited budget. Experiments show that our method consistently outperforms seven state-of-the-art instruction selection methods on four backbone-budget settings. An ablation study further shows that PASS's adaptive allocation consistently improves over uniform allocation.

---


### 252. [Distilling Routed 3D Privilege for Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.12355)

**<font color=#1a73e8>作者：</font>** Hongxing Li, Yixin Li, Dingming Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning remains a persistent weakness of vision-language models (VLMs), because RGB inputs do not directly provide geometric evidence. Existing remedies either inject 3D into the model at inference, paying architecture and latency costs, or train with outcome rewards that supervise only the final answer. Spatial errors originate in perception: a misjudged depth or direction can be corrected only by the scene's true geometry, which the 3D-scanned sources of spatial training corpora already provide. We propose GPD (Geometry-Privileged Distillation), which makes geometric evidence the privilege in on-policy self-distillation (OPSD). For each question, depth, semantic, and bird's-eye-view (BEV) cues are rendered as compact text and routed to the teacher alongside the reference answer; a privileged KL, applied only to incorrect trajectories, augments GRPO, and the deployed model remains RGB-only. On the 4B backbone, GPD achieves 57.1 on VSI-Bench and 37.6 average across MindCube, SPARBench, MMSI-Bench, and ViewSpatial, outperforming both GRPO and answer-privileged OPSD across spatial reasoning benchmarks. Ablations confirm the complementarity of 3D and answer privilege, the advantage of question-conditioned routing over full-context injection, and the benefit of restricting distillation to incorrect trajectories.

---


### 253. [Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict](https://arxiv.org/abs/2610.12360)

**<font color=#1a73e8>作者：</font>** Kaiser Sun, Bernal Jimenez Gutierrez, Hongjun Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When retrieved evidence contradicts an agent's prior beliefs, does it revise its answer, acknowledge uncertainty, or persist with an incorrect conclusion? Existing evaluations of agentic systems focus primarily on task success, offering limited insight into how agents handle such conflicts. We propose to evaluate agents on epistemic humility (EH): the agent's willingness to recognize, act on, and communicate uncertainty during task execution. We operationalize EH through three trajectory-level behavioral dimensions: Identify, Solve, and Escalate (ISE). Through knowledge conflict, situations where the backbone language model's parametric knowledge contradicts the evidence it encounters, or where two contextual sources disagree, we evaluate two conflict settings: (1) controlled conflict and (2) naturally occurring conflict during multi-step agentic execution, each paired with matched no-conflict controls. Evaluating four agents, we find that higher task accuracy does not necessarily correspond to greater epistemic humility: some high-accuracy configurations recognize conflicts during execution but do not communicate unresolved uncertainty in their incorrect final answers. Trajectory-level analysis further reveals that agents frequently detect conflicts in early steps of execution but fail to maintain or resolve them in later steps. Finally, we show that model-level interventions can improve EH, but often at the cost of task accuracy, suggesting that epistemic humility emerges from the interaction among the backbone model, agent harness, and evaluation environment.

---


### 254. [Cited but Not Consulted: A Counterfactual Audit of Legal Chain-of-Thought Faithfulness](https://arxiv.org/abs/2610.12361)

**<font color=#1a73e8>作者：</font>** Saisab Sadhu, Shreeyans Arora, Pratinav Seth  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly justify legal decisions by naming the statute or precedent behind a verdict, treated as evidence that the decision follows from it. We test this directly: holding case facts fixed, we substitute the named legal authority for an unrelated one and decode a model's evolving verdict from its hidden states. Across seven open-weight models (8B-70B) and four benchmarks spanning judicial and contractual reasoning, when explicitly required to justify a verdict by naming the governing authority, models name the correct one in 66.7%-100% of generations, while the verdict changing when the authority changes is far less consistent: 0.0%-21.7% on CaseHOLD, 30.0%-76.7% on ECHR and SCOTUS, and 43.3%-50.0% on ContractNLI. Neither scale nor a purpose-built legal-reasoning model (a best-effort LoRA reproduction; Section 6) closes this gap. A red-teaming evaluation on five core models finds compliance with an adversarial instruction hidden in the case facts (73.3%-96.4%) exceeds verdict-swap sensitivity by a wide margin, holding without exception across model rankings. Naming a legal authority is thus a poor proxy for a verdict's dependence on it, while the same verdict remains separately vulnerable to adversarial manipulation. Both findings replicate across checks ruling out prompt-wording noise and confounded sampling, and bear directly on the use of generated legal explanations as compliance or audit artefacts.

---


### 255. [Which Skill to Distill? SGUID: Selecting a Compact Skill Bank for Model-Skill Co-Evolution](https://arxiv.org/abs/2610.12367)

**<font color=#1a73e8>作者：</font>** Yuhan Liu, Xiyao Ma, Zhongkai Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skills, reusable procedural guidance added at inference, can substantially improve LLM downstream performance (Li et al., 2026). Prior work retrieves skills from a bank by semantic relevance, then uses them as inference-time patches or for model distillation. The individual utility of each skill, however, is largely neglected. We first show that, in on-policy distillation where skill-conditioned policies serve as teachers, fewer than 25% of retrieved skills provide useful distillation signals. We then propose SGUID, a method for selecting a compact subset of skills for distillation. SGUID retains a skill only if it consistently yields effective learning signals during training. The selected skills are then distilled to produce a better model. Our results show that not all skills are worth distilling. Across four models from the Olmo and Qwen families, distilling 6 selected skills matches or exceeds full-bank distillation in mean avg@12 on three of the four models, and on all four after a second round that distills 3 newly selected skills, while the full banks are up to 11x larger. Importantly, SGUID supports stable model-skill co-evolution: after a distillation round, a new candidate bank is curated from the updated model's rollouts, and SGUID selects which skills to internalize next. In the second round, this loop selects 3 new skills and improves Qwen3-8B from 64.3% to 66.3%. The selection step is essential for stability: on Qwen3-4B, naively updating the model with unfiltered skills degrades performance, including a 0.3 percentage point drop on HMMT25, whereas SGUID improves HMMT25 by 0.5 points after the first round and 1.1 points after the second. These results identify skill selection as the key mechanism for stable model-skill co-evolution.

---


### 256. [OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories via Streaming Structure-Aware Optimal Transport](https://arxiv.org/abs/2610.12375)

**<font color=#1a73e8>作者：</font>** Babak Barazandeh, Connor Swanson, Chinmay Kulkarni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents are deployed in applications from trip planners and stock trading to IT incident triage. In most cases, LLM agents work autonomously with minimal rule-based safeguarding, leading to cost and safety issues from irreversible actions. Recent works resolve this either by using a safeguard agent to monitor behavior or evaluating logs post-hoc. The first adds cost and latency to every step; the second delivers its verdict after the run, when tokens are burned and damage is done. To overcome this, we propose OnTrack, a streaming monitoring mechanism that compares an agent's steps and dependencies against recorded successful runs to alert users or block the agent in about a millisecond per step. We study this problem in three regimes of decreasing access: full reference access (historical runs and tool schemas), intermediate access (only tool schemas), and no prior knowledge (only step logs as generated). Expectation of OnTrack's monitoring capabilities reduces as data access drops, ranging from plan violation detection to identifying loops, stalls, and repeated tool calls. Finally, we evaluate OnTrack using SWE-bench trajectories. Based on the first 8 steps, our method ranks failing trajectories below succeeding ones better than content similarity approaches (+0.057 AUROC). With an abort policy, we save about 18% of compute that would be burned on failing runs, where 83% of interrupted runs were actually heading to failure (5 out of 6 aborts were correct).

---


### 257. [WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation](https://arxiv.org/abs/2610.12382)

**<font color=#1a73e8>作者：</font>** Jing He, Kaixin Ding, Xingye Tian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Faithful visual world simulation requires generated videos to maintain 4D world consistency, encompassing both static and dynamic consistency. Static consistency requires coherent 3D structure in static environments across viewpoints, while dynamic consistency requires plausible subject motion and consistent appearance over time. Geometry-aware post-training offers a promising way to improve world consistency. However, existing methods often rely on a static-scene assumption. Even those that accommodate dynamic scenes struggle to provide reliable static-consistency feedback, while dynamic consistency is often overlooked or inadequately assessed. To address these limitations, we introduce WorldAlign, a decoupled 4D reward framework that semantically separates static regions and dynamic subjects and provides feedback by aligning each with a world prior suited to its assumptions. For static regions, WorldAlign aligns static geometry with a geometric world prior through semantically guided masked reprojection, enabling more reliable static-consistency evaluation; an auxiliary camera-motion reward discourages nearly static solutions. For dynamic subjects, WorldAlign uses a strong vision-language model (VLM) as a dynamic world prior and constructs a VLM-as-a-judge reward based on sample-specific checklists that assess dynamicity, physical plausibility, shape, and texture consistency. This decoupled design enables more effective online post-training without requiring human preference annotations. Across two pretrained image-to-video generators, Wan2.1 and Wan2.2, WorldAlign jointly improves static and dynamic consistency over existing methods without suppressing overall or subject motion. These results support decoupled world-prior alignment for more faithful visual world simulation. Project page: this https URL.

---


### 258. [Long Text to Predictive Features: LLM-Guided Blockwise Feature Engineering via Executable Program Search](https://arxiv.org/abs/2610.12390)

**<font color=#1a73e8>作者：</font>** Ziming Dai, Dabiao Ma, Ziheng Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial risk-control systems typically rely on structured-data models for efficient prediction, yet substantial valuable information remains embedded in unstructured long text. Extracting this information through manual feature engineering is labor-intensive, while requiring a large language model (LLM) to process every real-time input may not meet practical deployment requirements. To address this challenge, we propose LLM-BlockFE, an LLM-guided offline feature construction framework that converts long text into executable feature programs, thereby avoiding LLM calls during online inference. LLM-BlockFE constructs feature programs by incrementally appending immutable code blocks and evaluates candidate features using a downstream model. To address the tendency of conventional greedy search to become trapped in suboptimal solutions, our method introduces a block-level rollback mechanism based on depth-calibrated credit allocation and advances multiple independent search trajectories in an interleaved manner, reducing redundant exploration by sharing fixed descriptions of each trajectory's exploration direction. After the search, the resulting programs are frozen and deployed to extract structured features for downstream prediction models. Across two public and two private datasets, LLM-BlockFE achieves absolute AUC improvements of 0.0069 to 0.0358 over the strongest baseline on each dataset in the full-dataset comparison. Post-launch monitoring across five deployed financial risk-control applications shows absolute KS improvements of 0.02 to 1.56 percentage points over the existing manually designed strategy.

---


### 259. [GeoReform: Reflective Formalization Evolution for Multimodal Geometry Problem Solving](https://arxiv.org/abs/2610.12391)

**<font color=#1a73e8>作者：</font>** Jialu Wang, Ruichen Zhang, Xiaoou Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) often struggle to identify and use geometric relations in diagrams. Recent methods address this challenge by converting geometric entities, relations, and constraints into explicit textual representations for the model to reason over. However, effective formalization is highly non-trivial: on Geometry3K, structure injection fixes 28 errors but introduces 13 new ones among 200 examples. Redundant relations can distract the model, while ambiguous references to diagram elements can lead it to apply constraints incorrectly. This suggests that the key challenge is not merely extracting more geometric facts, but organizing them into representations that support downstream reasoning. To fully exploit the power of formalization, we further propose GeoReform, a reflective formalization evolution framework that treats formalization as an optimizable policy rather than a fixed parser output. GeoReform executes the full reasoning pipeline, collects failed rollouts, diagnoses defects in the current representation, and mutates the policy to better select, ground, group, and present geometric entities, relations, constraints, and targets. On Geometry3K, GeoReform improves Qwen3VL-2B accuracy from 42.0\% to 56.0\%. Extensive experiments and analyses across geometry reasoning benchmarks demonstrate that effective formalization is crucial for improving multimodal geometry reasoning.

---


### 260. [SpaceCast-Bench: Evaluating Predictive Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.12402)

**<font color=#1a73e8>作者：</font>** Hongxing Li, Jinyue Su, Dingming Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing spatial reasoning benchmarks mainly test spatial perception: reading off relations already visible in the input. Yet real-world spatial intelligence demands predictive spatial reasoning: constructing a scene from observations, anticipating how an intervention changes it, and reasoning about the unseen outcome. We introduce SpaceCast-Bench, the first benchmark to directly and diagnostically evaluate this capability. Built around an observe-transform-infer framework, its 3,862 questions from 182 real-world scenes span 16 task types at three levels: static perception, local prediction, and global prediction, progressively requiring scene understanding, spatial state updating, and relational inference over unobserved outcomes. Evaluating 21 models exposes a stark gap: the strongest model reaches only 58.0% against 87.2% human performance, while spatially specialized models remain near random chance. Controlled analyses further reveal that bridge views are critical for integrating distributed observations, and that explicit 3D evidence benefits models more reliably than generated outcome images or videos. Fine-tuning on our programmatically generated data lifts Qwen3-VL-4B from 34.0% to 65.7% with macro-average gains across six out-of-domain benchmarks.

---


### 261. [ViSkill: Reinforcing VLM Agents with Evolving Visual-Native Skills](https://arxiv.org/abs/2610.12403)

**<font color=#1a73e8>作者：</font>** Hongxing Li, Dingming Li, Yixin Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skill-augmented agents improve sample efficiency by distilling successful trajectories into reusable strategies. Yet most existing approaches remain text-centric, linearizing spatial layouts and action-state correspondences into language that loses critical geometric structure. Recent efforts have begun incorporating visual evidence, but construct and update skills separately from policy optimization, leaving their mutual improvement underexplored. We propose ViSkill, a visual-native skill learning framework that encodes successful interactions as composite visual skill cards directly accessible to VLM agents. Retrieved skills guide both inference and reward shaping, while successful trajectories are distilled back into the library, forming a closed feedback loop in which skill accumulation and policy improvement reinforce each other. An optional cold-start mechanism further accelerates early-stage learning. Evaluated on Sokoban, FrozenLake, and PrimitiveSkill, ViSkill achieves an overall success rate of 0.89, rising to 0.91 with cold-start initialization, outperforming all evaluated proprietary and open-source baselines while converging faster than standard PPO. Our code is available at this https URL.

---


### 262. [Predicting Alignment Generalization with Value Representations](https://arxiv.org/abs/2610.12410)

**<font color=#1a73e8>作者：</font>** Andy Liu, Mehar Bhatia, Karolina Stanczak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM developers post-train their models to exhibit prosocial values and behavioral traits, which are enumerated in an alignment target. However, while recent post-training developments have yielded models that score highly on alignment evaluations, training models on sets of narrow behaviors still influences their behavior across unseen contexts and environments in unexpected ways. In this paper, we establish the task of alignment generalization prediction, i.e., predicting how fine-tuning a model to follow a given value changes its behavior across a wide range of held-out values. We conduct a large-scale analysis of alignment generalization effects across 66 values found in modern alignment targets, and benchmark representational techniques on the alignment generalization prediction task. We find that representations based on model activations when applying values in context significantly outperform methods based on textual descriptions of the values. Specifically, the best activations-based methods achieve correlations of 0.45 with our generalization matrix, compared with 0.05 from description-based baselines. We then show the applicability of representations that predict alignment generalization toward downstream tasks by using them to measure how similar the values in a multi-value alignment target are, which we find is significantly correlated with model robustness. Finally, we show initial evidence towards a shared, model-independent value space, which we use to develop the first taxonomy of LLM values grounded in empirical generalization dynamics. Our work demonstrates the importance of studying value generalization in LLMs and its application toward the more empirical design and training of model behavior.

---


### 263. [ORCAGen: Orchestrating Context-Aware Malware Deception with RAG-Guided Generative AI](https://arxiv.org/abs/2610.12415)

**<font color=#1a73e8>作者：</font>** Shihab Ahmed, Md Sajidul Islam Sajid, Teryl Taylor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malware defenses often remove or isolate suspicious programs as quickly as possible. While effective for containment, this approach can also waste an opportunity to observe attacker behavior and deploy targeted countermeasures. ORCAGen takes a different approach: it uses GenAI to build malware-specific deception playbooks offline, validates them before deployment, and enforces only the verified logic at runtime. ORCAGen combines Retrieval-Augmented Generation (RAG) with structured prompt engineering to generate both proof-of-concept (PoC) malware and corresponding deception orchestration code. A curated knowledge base (KB) of malware procedures and active defense strategies grounds the generation process, helping the LLM produce threat-specific and executable deception logic rather than generic or hallucinated outputs. The generated PoC malware provides a safe and reproducible way to test whether a deception strategy can disrupt, redirect, or suppress targeted malware behavior before the strategy is added to the runtime playbook. We evaluate ORCAGen across GPT-4o, GPT-5.5, Gemini 3.5 Flash, Qwen3-Coder, and Claude Sonnet 4.5 using execution success, hallucination rate, refinement effort, deception effectiveness, and runtime overhead. The evaluation covers synthesized malware scenarios and 150 real-world malware samples across keyloggers, information stealers, and ransomware. Across the evaluated scenarios, GPT-5.5 required the fewest refinements and produced no observed hallucinated APIs, while Gemini 3.5 Flash achieved the lowest response time and runtime overhead. The results show that RAG-guided structured prompting can support the scalable construction of malware-specific deception playbooks that remain lightweight and deterministic during runtime enforcement.

---


### 264. [WOVEN: Weaving Visual World Modeling into Multimodal LLMs](https://arxiv.org/abs/2610.12417)

**<font color=#1a73e8>作者：</font>** Zheyu Fan, Yue Zhang, Mingkai Deng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, and test whether this capability can serve as a shared training primitive, one that different models can learn from different supervision sources and reuse across different tasks, with a systematic training recipe. Existing benchmarks document these deficits separately but do not support controlled comparisons across scenes, actions, and reasoning operations. We therefore introduce WOVEN, a training source and benchmark for visual transition reasoning that organizes transition supervision by scene, action, and reasoning type, using diverse, realistic rollouts from video-pretrained generative models: 36,076 examples across 20 scene types, 5 action types, and 8 reasoning types. We first evaluate 38 frontier MLLMs (e.g., GPT-5.4 and Qwen3-VL-235B-A22B) and find a substantial and systematic deficit: even the strongest models fall far below humans, and the failures recur across model families and persist with scale. We then train MLLMs at multiple scales on WOVEN and find that they learn a shared capability that transfers broadly: training subsets of only about 2,000 items each collectively improve 22 of 26 external benchmarks by up to 27.3 percentage points, and WOVEN data can replace 30-50% of a task's own training data with comparable accuracy. Controlled comparisons further yield a training recipe for visual world modeling, validated prospectively on held-out benchmarks: select supervision by the reasoning operation it teaches rather than by the actions, scenes, or domains it shows, and prefer larger changes to the visual state for robustness. Our work establishes visual transition reasoning as a reusable foundation for systematic visual world-model training in MLLMs.

---


### 265. [OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video](https://arxiv.org/abs/2610.12419)

**<font color=#1a73e8>作者：</font>** Hongyu Li, Manyuan Zhang, Kaituo Feng 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image, multi-image, and video deep research require different visual operations but share a workflow of visual grounding, external retrieval, and fact composition. A key challenge is to preserve the dependencies linking localized visual anchors, entity relations, source-supported facts, and answer-producing operations. We introduce OneSearch-VL, a unified agent centered on the Visually Grounded Evidence Graph (VGEG), which encodes these dependencies as a shared task-level reference for data construction, process supervision, and operation-level evaluation. Our VGEG-based data engine constructs and verifies multi-image and video questions and filters expert trajectories. Using these data, we assemble OneSearch-VL-SFT-110K and OneSearch-VL-RL-10K for SFT and RL, respectively. We further derive the Evidence-aware Visual-Grounded Rubric reward (EVGR) from VGEG annotations to supervise evidence traceability and visual grounding during RL. For fine-grained evaluation, we construct OneSearch-MI-Bench and OneSearch-Video-Bench, organizing questions by the research operations encoded in their VGEGs. Experiments show that OneSearch-VL-8B improves over Qwen3-VL-8B with tool access by 20.2 and 17.6 percentage points on the two new benchmarks, respectively, while also achieving substantial gains across 7 image benchmarks and VideoDR. Project repository: this https URL

---


### 266. [FastBench: Can Streaming VLMs Perceive High-Dynamic Real-World Streams?](https://arxiv.org/abs/2610.12427)

**<font color=#1a73e8>作者：</font>** Yuxuan Hu, Weikang Shi, Yang Bo 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming Video Large Language Models (VLMs) enable continuous video understanding, yet existing benchmarks focus on low-dynamic scenarios. Under bounded context budgets, models must balance temporal history, spatial resolution, and temporal granularity; sparse sampling at 1--2 FPS misses fast events. We introduce FastBench to evaluate high-dynamic perception in real-world video streams. Its trajectory-grounded pipeline combines QA generation from high-FPS clips, filtering of questions answerable at 2 FPS, answer verification using SAM3 and CoTracker3 trajectories, and three rounds of human inspection. FastBench contains 306 QA pairs across eight domains, six capabilities, and forward, instant, and backward temporal scopes, with human-annotated evidence intervals. We also present ProactiveFrame, a training-free baseline that adjusts incoming frame rates through text tokens. A dual-tier sliding window retains recent high-FPS observations while downsampling older ones into sparse history. Experiments reveal substantial limitations: the strongest model, Gemini-3.5-Flash, scores only 50.7%. Denser sampling improves Qwen3-VL-8B from 32.9% at 2 FPS to 44.6% at 24 FPS, but gains saturate as history is compressed. ProactiveFrame outperforms sparse uniform sampling by 5.4 and 1.5 percentage points, yet remains well below oracle-guided focusing, showing that current VLMs struggle to determine from the stream alone when finer temporal perception is needed. FastBench provides a testbed for high-dynamic streaming video understanding. Code and data: this https URL.

---


### 267. [Rounding in Preconditioner Space: Redesigning 4-bit AdamW Optimizer-State Quantization](https://arxiv.org/abs/2610.12444)

**<font color=#1a73e8>作者：</font>** Hanyang Li, Shao Tang, Daniel Thomas Braithwaite 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantizing AdamW's optimizer states reduces persistent storage, but quantization errors propagate through the moment recurrences and perturb subsequent adaptive updates. We redesign 4-bit optimizer-state quantization for AdamW from the perspective of \emph{rounding space}: the coordinate in which a quantizer chooses between adjacent reconstruction levels. For the second moment, a local analysis of the quantization cell adjacent to zero shows that small mean state error need not imply small mean preconditioner error at the next step. A one-dimensional quadratic construction further shows qualitatively different optimization dynamics under state-space and preconditioner-space rounding. These results motivate Zero-Inclusive Preconditioner-space Stochastic Rounding (\textbf{ZIP-SR}), which retains zero in the second-moment codebook and computes stochastic-rounding probabilities in preconditioner space. As a complementary route, Zero-Excluding EDEN calibration (\textbf{ZE-EDEN}) uses a zero-excluding second-moment codebook and rescales the quantized second-moment block to mitigate the preconditioner distortion caused by the positive quantization floor. Both configurations use 4-bit NormalFloat (NF4) for the first moment, with targeted stochastic rounding of the LM-head first moment during the final 10\% of training. Across GPT- and Llama-style pretraining experiments ranging from \textbf{130M} to \textbf{2.7B} parameters, both methods reduce TorchAO 4-bit AdamW's mean validation-loss gap to 32-bit AdamW at every evaluated model size, with the largest reported gap reduction reaching \textbf{70\%}. In full-parameter supervised fine-tuning, both recipes achieve lower validation loss than TorchAO while remaining close to 32-bit AdamW on downstream tasks.

---


### 268. [Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception](https://arxiv.org/abs/2610.12445)

**<font color=#1a73e8>作者：</font>** Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent incidents have highlighted the challenge of monitoring LLM agents and the danger of models deceiving people. We show that white-box deception detection via probes can be scaled up to frontier monitoring settings by collecting the largest deception dataset to date for training probes and introducing a novel probe architecture which can aggregate information across many layers and tokens. Our probes achieve 98.8% AUC in SHADE-Arena, surpassing an Opus 5.5 text-monitoring baseline, and show improved efficacy as the underlying model is scaled up. To push our probes to their limit, we test them on several cases where deception cannot be determined from the context alone. In these cases, which we refer to as introspective deception, the ground truth can only be determined through careful elicitation or thorough knowledge of a model's training data. In one such evaluation, we show that probes can distinguish transcripts containing a model's true hidden goal from other goals with an AUC of up to 99.7%. Our probes also readily detect deception on prominent open-weight models which lie about politically sensitive topics, and about their beliefs when put under pressure. We release our training dataset, dubbed FIBS, to help drive frontier deployment of effective probes, and encourage the community to expand upon it with further examples of deception and sabotage.

---


### 269. [VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation](https://arxiv.org/abs/2610.12451)

**<font color=#1a73e8>作者：</font>** Boyao Han, Chen Shi, Jingjing Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have emerged as powerful foundations for robotic manipulation, but their reliance on fixed camera configurations during training makes them brittle to changes in camera count or pose during deployment. To overcome these limitations, we propose VersaCamVLA, a camera-configurable framework that decouples camera-set representation from action learning. VersaCamVLA learns a unified scene-token interface that maps an arbitrary, variable set of posed RGB views into fixed-size latent scene tokens. This is achieved via multi-signal target-view prediction and Wrist-Augmented Pose Sampling (WAPS), which leverages natural wrist-camera motion for free pose diversity. At deployment, a lightweight spatial encoder injects these compact scene tokens into a pretrained base VLA as a supplementary visual condition, requiring no explicit 3D sensing or novel-view rendering. Experiments on RoboTwin, LIBERO, and a real-robot platform demonstrate that VersaCamVLA consistently outperforms prior VLA methods and direct multi-view baselines, maintaining robust performance across varying camera counts and unseen camera poses.

---


### 270. [BrickBench: Evaluating Agentic Brick Design](https://arxiv.org/abs/2610.12452)

**<font color=#1a73e8>作者：</font>** Peter Kulits, Yiqing Xu, R. Kenny Jones 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose BrickBench, a benchmark for agentic text-conditioned LEGO-set design. Given a prompt, an agent is tasked with producing an assembly that not only satisfies semantic and design criteria, but that can also be physically built. To do so, it must select parts from a discrete library and reason jointly about local and global constraints. We score validity, alignment, and design across three settings that vary in scale and part availability. We provide BrickAgent, an environment for coding agents to construct, inspect, and validate their designs. We find that leading agents largely satisfy verifiable physical and semantic requirements, but fall short of human designs. We release our benchmark and environment at this http URL

---


### 271. [OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual Captioning](https://arxiv.org/abs/2610.12458)

**<font color=#1a73e8>作者：</font>** Zhongyu Yang, Jiale Tao, Ruitao Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are rapidly evolving toward continuous audio--visual reasoning, creating an urgent need for evaluations that expose their capability limits. Audio--visual captioning is an ideal diagnostic task, yet current benchmarks face a coupled trade-off: whole-caption scores provide coverage without localization, local probes provide localization without coverage, and unconstrained LLM judges introduce instability. We introduce OmniCapBench (Omni-Video Caption Benchmark), a benchmark that reframes audio--visual caption evaluation as a deep-structured diagnostic framework. OmniCapBench shifts the prediction target from free-form text to sets of atomic, verifiable evaluation units across three tracks: entity references, visual shots, and audio events, enabling reliable scoring with deterministic constraint checks and localized LLM-based semantic comparisons. With 786 densely annotated videos, OmniCapBench effectively distinguishes MLLM perception errors, including temporal grounding failures, identity drift, cross-modal misalignment, and hallucinated descriptions. Evaluating frontier MLLMs reveals strong local perception but weak long-horizon audio--visual reasoning, particularly in identity drift and cross-modal misalignment, providing a fine-grained roadmap for omnimodal development.

---


### 272. [OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs](https://arxiv.org/abs/2610.12461)

**<font color=#1a73e8>作者：</font>** You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D world models generate photorealistic, explorable scenes that remain frozen in time. OuroWorld is a mask-free framework that turns any static 3D Gaussian Splatting scene into a 3D cinemagraph: a dynamic scene with vivid, diverse motion looping seamlessly from any viewpoint. A vision-language model infers plausible dynamics and guides a video model to synthesize a reference video, which we lift and complete into multi-view videos. To learn from this imperfect supervision, we propose Inconsistency-Robust Periodic 4DGS: a Fourier-series deformation field guarantees looping by construction, while a Grounded Drift Field anchored at the reference view absorbs cross-view inconsistency. Unlike prior Eulerian methods limited to fluid-like motion, we capture general deformation, object motion, and illumination change. We introduce a ground-truth-free evaluation covering vividness, naturalness, loop seam coherence, and scene quality. On 39 reconstructed and generated scenes, OuroWorld outperforms all baselines and wins 70.8%-99.0% of user-study comparisons. Project page: this https URL

---


### 273. [Rubric-CEPR: Self-Evolving Image Editing via Reward-Verified Self-Distillation](https://arxiv.org/abs/2610.12469)

**<font color=#1a73e8>作者：</font>** Ritesh Thawkar, Shubham Patle, Shravan Venkatraman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-guided image editors have become highly capable, yet improving them further still depends on human-edited training pairs or external reward models. Such supervision is costly to obtain and can reward plausible failures: a realistic output may leave the requested change undone or alter content that should be preserved. In this work, we strive to improve a pretrained image editor using only its own generations, without human-edited targets or an external training-time reward model. To this end, we propose a self-evolving framework, named Rubric-CEPR, that verifies the editor's own samples with its internal representations through a rubric-augmented Contrastive Edit-Preservation Reward (CEPR). A Planner proposes structured edit instructions from unlabeled images, the Editor samples multiple candidate edits, and a frozen Critic scores each candidate with decomposed rubric checks for edit realization, removal of the old state, and content preservation, using features already exposed by the editor. Non-compensatory gates reject infeasible candidates, and the best verified candidate is distilled into the editor through lightweight adapter training. On Qwen-Image-Edit, Rubric-CEPR improves ImgEdit from 4.36 to 4.60 (+5.5%), with a +24.9% gain on object isolation, and transfers to GEdit-Bench and Complex-Edit. The same procedure also improves Step1X-Edit by +7.8% on ImgEdit. We hope our approach will serve as a solid baseline for image editors that improve themselves from their own verified samples. Our code is publicly available at $\href{this https URL}{\text{this URL}}$

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 274. [SPERA: Spherical Prior EEG Foundation Model with Geometry- and Frequency-Aware Latent Prediction](https://arxiv.org/abs/2610.10571)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Minsu Kim, Ye-Sung Kim, Hyeseong Jeon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) provides a non-invasive measure of ongoing neural activity, but building general-purpose EEG models remains challenging due to the heterogeneity of subjects, devices, and electrode montages. Existing EEG foundation models predominantly rely on reconstruction-based objectives defined on the observed signal, which contains both neural and non-neural components. We introduce SPERA (Spherical Prior EEG Representation Architecture), an EEG foundation model that adopts the joint-embedding predictive architecture (JEPA) to predict in latent space. SPERA introduces a Legendre-polynomial spatial prior, incorporated into attention to encode varying scalp electrode geometries. Two further components adapt the model to EEG: factorized temporal and spatial attention interleaved with periodic full-attention blocks, and a relational spectral regularizer aligning latent similarity structure with spectral views. Pretrained on approximately 80,000 hours of EEG from 29,048 subjects across 106 datasets, SPERA achieves the highest average balanced accuracy across nine downstream tasks spanning clinical, cognitive, and BCI applications. SPERA further exhibits strong parameter efficiency under linear probing and robustness across varying recording conditions, suggesting its potential as a general-purpose backbone for diverse EEG analyses.

---


### 275. [Certified Corruption Budgets: Anytime-Valid Leaderboard Claims under Adaptive Rigging](https://arxiv.org/abs/2610.10597)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hamed Khosravi, Xiaoming Huo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public leaderboards for AI models are read continuously, and attackers can see every published standing. Vote rigging, selective disclosure of private variants, and benchmark contamination can each move a ranking. Existing guarantees assume genuine records or bound the corruption per step, which an attacker who corrupts in bursts evades. We introduce the certified corruption budget, a tolerance $\widehat{B}_t$ computed after $t$ records and published with each pairwise claim. With probability at least $1-\alpha$, simultaneously at all times, the claim is correct or more than $\widehat{B}_t$ records were corrupted. It holds against attackers who watch every certificate, with no bound on their budget. Forged records and records altered once seen require different certificates: the certificate for forgeries fails, with probability approaching one, against an attacker who flips votes it has seen, while one that charges roughly twice as much per record remains valid, with constant bets even against attackers who see the future, and no smaller charge is valid at every level. The certified budget grows nearly as fast as any valid method allows: with a win fraction $\frac{1}{2}+\delta$, each new record adds close to $2\delta$ to the number of forged records the claim can withstand ($\delta$ flipped). Publishing the best of $V$ private variants costs only an amount growing like $\log V$. In replays on 1.8 million Chatbot Arena votes, a few hundred rigged votes make standard confidence intervals certify false orderings, while ours stays valid. On real votes, our certificate shows that clearly separated models withstand about 2,000 forged votes.

---


### 276. [Visible Reasoning Is Not a Universal Optimizer: Persona- and Thinking-Dependent Effects in Analytics Code Generation](https://arxiv.org/abs/2610.10639)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bhawani Shankar Leelar, Pawan Chorasiya, Davin Hill 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visible Chain-of-Thought (CoT) is often treated as a broadly useful reasoning instruction, yet analytics code generation combines natural-language ambiguity, schema grounding, target-language constraints, and model-specific inference behavior. Because the same analytics request can be expressed in two distinct target languages-SQL and Python (pandas)-this setting provides a natural test of a common but under-examined assumption: that visible reasoning is more effective when its representation matches the requested target, as in "think in SQL" or "think in Python." Together with generic instructions such as "think step-by-step," such recommendations remain insufficiently evaluated under controlled, execution-based comparisons. We study a query matched SQL-pandas benchmark that crosses persona phrasing, target language, visible-CoT format, control prefixes, direct generation, and internal-reasoning configurations. The results do not support either a universal accuracy advantage from visible CoT or a consistent benefit from matching the reasoning representation to the target language. Instead, the effects depend on the persona, target, model configuration, and internal-reasoning setting. The control ablations further distinguish effects of reasoning content from those of prompt format. These findings indicate that reasoning strategies should be selected jointly for the model, persona, target, and internal-reasoning configuration rather than adopted as universal defaults. More broadly, the study provides a controlled framework for identifying when visible reasoning improves executable generation, when it primarily perturbs model behavior, and when the internal-reasoning configuration is the more consequential factor.

---


### 277. [MemoWM: How World Models Change What Agents Need to Remember](https://arxiv.org/abs/2610.10778)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Bingfan Zeng, Zhisheng Chen, Chenbo Sang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term agents face growing storage demands as they accumulate experience. World models capture reusable regularities that can reduce the information stored for each experience. We formulate the problem of memory allocation conditioned on a world model and introduce MemoWM, a framework that uses shared predictions to compress retained information and reconstruct omitted content. Its task-aware allocation rule balances the expected impact of reconstruction errors against storage cost, retaining information with downstream value beyond the predictive prior. Across five long-term agent-memory benchmarks, MemoWM achieves 42.42\% average answer accuracy, exceeding the strongest baseline by 2.62 percentage points, while reducing average experience-specific storage by 53.9\% relative to MIRIX, the most storage-efficient baseline. Further analysis shows that stronger world models reduce per-experience storage at comparable task quality. Accounting for model parameters reveals a trade-off between shared model capacity and recurring storage costs, with the capacity that minimizes total storage increasing as more interactions are retained. Our code is available at this https URL.

---


### 278. [Invariant-Measure Reasoners: Stable Representations for Latent Reasoning](https://arxiv.org/abs/2610.10996)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuto Inui, Takuya Konishi, Yoshinobu Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent reasoning models repeatedly update a latent state using the same recurrent block. As the recurrent depth increases, the sequence of latent states may converge to a compact subset of the state space without necessarily converging to a fixed point. Existing models typically predict by applying a prediction head to a single latent state. However, the latent state can continue to change even after many updates, potentially making predictions unstable across recurrent depths. To address this instability, we introduce invariant-measure reasoners (ImR), a framework that uses an invariant measure as a stable representation. This measure describes the long-run distribution of latent states on the compact subset and is invariant under updates by the recurrent block. ImR predicts from the expectation of the prediction head's output under this measure. We use ImR in two ways: fine-tuning only the prediction head of existing models and training models from scratch. Both approaches reduce prediction instability and improve accuracy in many settings on maze and Sudoku tasks. In some settings, models trained with ImR exhibit non-fixed-point behavior more frequently than existing models yet achieve high accuracy even with such behavior, unlike existing models. These results suggest that ImR can leverage otherwise destabilizing dynamics for latent reasoning.

---


### 279. [Diffusion Meta-Prompting and Steering for Generalizable Foundation Model Adaptation](https://arxiv.org/abs/2610.11067)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Deepak Sridhar, Yi Li, Kartikeya Bhardwaj 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt learning is a popular method for adapting foundation models, but learned prompts are typically task-specific and fail to generalize to new classes, domains, or compositions of tasks. In this paper, we introduce a Diffusion Meta-Prompt (DMP) model , a framework that models the distribution of learned prompts using diffusion models. Given a repository of previously learned prompts, DMP is trained and sampled without access to the original task examples or task losses, and synthesizes new prompts conditioned on natural language task descriptions. To improve the sampling stability, we introduce a test-time steering strategy for DMP, which uses the best training-selected prompt in the repository as a latent anchor during diffusion sampling, without retraining the DMP or accessing test classes. DMP improves generalization across classification, retrieval and text-to-image generation tasks, supports concept composition and negative prompting without explicit training. It reduces storage and inference costs by over 90% compared to prompt retrieval methods. For composite classification, DMP achieves upto 2.0% average gain over prior meta-learning methods across 55 pairs of datasets with gains as high as 8.5% on specific pairs such as Eurosat and Flowers. DMP also enhances cross-task generalization with ~2-9% improvement for hierarchical classification task. We further provide a theoretical guarantee bounding the expected task loss of prompts sampled from a DMP. Code is available: this https URL

---


### 280. [ReTeach: Building a Self-Teacher through Multi-Round Reflection and Retry](https://arxiv.org/abs/2610.11529)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yafeng Tang, Hao Li, Hongsheng Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-distillation can improve reasoning without a separately trained, more capable teacher, but its effectiveness depends on how the self-teacher gains an advantage over the student. Conditioning the teacher on reference answers or solutions can provide such an advantage, but this information may be unavailable. Reflection offers a way to derive explicit error diagnoses and revision guidance from self-generated attempts, yet existing reflection-based methods often combine it with reference information, rich task feedback, or persistent memory. We introduce ReTeach, a Reflective self-distillation framework that constructs its self-Teacher through multi-round reflection and retry using only self-generated attempts and outcome-level verification. Starting from an unsuccessful student rollout, the teacher alternates explicit reflection with renewed attempts until success or the retry budget is exhausted, without reference answers or solutions, external diagnostic feedback, or cross-example memory. Each failed retry informs subsequent reflection, while successful correction provides outcome-level evidence for the potential utility of the resulting teacher context. An outcome-aware selection and weighting strategy distinguishes initially correct, reflection-corrected, and unresolved examples, assigning separate weights to their category-normalized distillation losses. Through on-policy distillation, the student matches the teacher's context-conditioned token-level predictive distributions at prefixes of its own rollouts, transferring the benefits of iterative correction while retaining single-pass inference. Across six benchmarks spanning mathematical reasoning, science question answering, and tool use, ReTeach improves average accuracy over GRPO by 1.39 percentage points.

---


### 281. [Beyond Report Imitation: Clinically Aware Multi-Image Ultrasound Report Generation from Visible Evidence](https://arxiv.org/abs/2610.11610)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuchen Yang, Xin Wang, Lufan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating ultrasound reports from multiple images requires aggregating clinical evidence across views, yet archived key frames capture only part of the dynamic examination. Raw-report imitation is therefore misaligned with visual supervision: content that is clinically valid for the full examination may be unverifiable from the images available to a model. This gap creates a clinical behavior alignment problem. A model must preserve visible findings, avoid diagnostic reversals and unsupported completion, and not collapse into conservative templates. We propose CAMEO, a Clinically Aware Multi-image Evidence-grounded Orchestration framework for ultrasound report generation. Stage I learns ultrasound visual-language primitives; Stage II performs Cross-View Evidence Grounding by distilling trusted visible report points into multi-image QA and report-style supervision; and Stage III performs Clinically Aware Preference Alignment using clinical-error-oriented preference pairs. From USReport, we construct USReport-Distilled with 17,670 evidence-grounded paired-image training instances and USReport-Pref with 21,869 preference pairs; we additionally use 25,631 PubMedVision-US ultrasound instruction samples for domain adaptation and multi-image instruction tuning. On the primary USReport-Distilled benchmark, CAMEO improves over EchoVLM from 0.25 to 0.40 BLEU-1, 0.28 to 0.45 ROUGE-1, and 0.27 to 0.43 METEOR, while raising ClinicalScore from 55.02 to 74.20. These results underscore the value of evidence-grounded supervision, clinically aware alignment, and clinically structured evaluation for reliable ultrasound report generation.

---


### 282. [Timer-M1: A Multivariate Time Series Foundation Model via Learning Primitives](https://arxiv.org/abs/2610.11734)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haoran Zhang, Haixuan Liu, Xingjian Su 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Timer-M1, a pretrained multivariate time series foundation model that learns with primitives for zero-shot forecasting. Across domains, time series share elementary temporal and relational patterns, termed primitives, yet differ in how these primitives manifest and evolve across different contexts. Despite progress in zero-shot and task-general forecasting, existing foundation models may still struggle to generalize to complex real-world scenarios. To this end, we develop a primitive-based data synthesis and pretraining pipeline. The synthesis pipeline generates series with temporal primitives shared across domains and then assembles real and generated series into multivariate samples using relational primitives. Afterwards, samples are organized into episodes by assigning distinct channel roles as target variates, past-only covariates, and known-future covariates, ensuring that the model is optimized on predictable variates using available exogenous information. Technically, Timer-M1 further adapts gated two-dimensional Transformer blocks that dynamically allocate cross-variate attention across layers. Across three large-scale forecasting benchmarks, Timer-M1 ranks first on both FEV and TIME and second on GIFT-Eval among most recent time series foundation models. These results support effective primitive-based pretraining as a route to robust general forecasting technique across domains and task settings.

---


### 283. [Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](https://arxiv.org/abs/2610.11756)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiaming Zhang, Xinyu Wang, Huafeng Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion enables causal video streaming without a bidirectional pass over the full clip, but existing few-step systems usually retain only the opening and most recent frames in a fixed-size KV cache. Once an event leaves this window, later frames can no longer attend to it, a failure we term mid-horizon forgetting. We present Memory Forcing, a few-step streaming method that preserves this missing history without increasing the cache size. Its Archive \& Working Banks partition the cache into sink, archive, and working regions, retaining diverse intermediate events alongside recent motion under fixed memory. Because absolute temporal indices drift outside the training range, Bank-aware RoPE reassigns indices at attention time so each bank remains distinguishable. At 1.3B, Memory Forcing leads on longer clips, shows the smallest drop from 5s to 60s among methods reporting all four lengths, and preserves subjects and scenes through leave-and-return. The same design scales to Wan2.2 5B, producing more physically plausible, realistic, and dynamic videos and, to our knowledge, the first public 5B model on this forcing line.

---


### 284. [Test-Time Compute for Tabular Foundation Models: Mechanisms, Gains, and Limits](https://arxiv.org/abs/2610.12005)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kanghui Ning, Marin Biloš, James T. Wilson 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Which forms of test-time compute improve the predictions of strong pretrained tabular foundation models (TFMs)? We systematically study this along three axes: adaptation, aggregation, and context construction. Our evaluation spans modern TFMs across the TabArena benchmark, supplemented by experiments on wide and large-scale tables from OpenML. For adaptation, we introduce DiagScale, a diagonal query-key similarity update. It trains only 0.003-0.03% of model parameters and achieves gains comparable to full fine-tuning across three independently pretrained backbones. For aggregation, both pool composition and selection strategy matter. TabPFN-3 already averages predictions from different preprocessing variants of the same data, and adding more such predictions yields diminishing returns. With a broader pool of 96 configurations, greedy selection reduces error by 2.4% relative to the default predictor, but uniform averaging increases error. For context construction, attention-guided retrieval improves TabPFN-3's predictions on some large tables and supports source pools beyond the full context memory limit. The context expansion methods we test yield no consistent improvement. Taken together, our results suggest that adaptation and selective aggregation yield consistent benchmark-level gains. The benefits of context construction depend more on the task and data regime. Adaptation and aggregation over the same backbone yield further gains when combined, but require substantially more computation than default inference. These trade-offs motivate choosing strategies according to the available computation budget. Code is available at this https URL.

---


### 285. [VINCIE-NExT: Unlocking Video Editing from Images via In-Context Modeling](https://arxiv.org/abs/2610.12104)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Leigang Qu, Feng Cheng, Ziyan Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building a capable video editor remains significantly harder than a video generator: editing requires (source, instruction, edited) triplets that are prohibitively expensive to annotate and difficult to synthesize at scale, whereas image editing has already reached maturity with millions of such pairs readily available. In this work, we introduce VINCIE-NExT, a unified framework that transfers editing capability from images to videos through in-context visual demonstrations, alleviating the need for large-scale paired video editing data. VINCIE-NExT decomposes video editing into a structured chain of composable sub-tasks (Video -> Image -> Image -> Video), routing editing intent through the image domain and enabling scalable joint training from heterogeneous image and video corpora under a unified diffusion objective. An image editing pair, synthesized by the model or supplied by the user, is prepended as an in-context visual demonstration that serves as a spatial appearance blueprint for every output frame. To ground appearance edits across the interleaved context, we introduce a novel position encoding that links image demonstrations and video frames in a shared spatial coordinate system, enabling pixel-faithful propagation of appearance changes to every output frame. Chain-of-Editing further provides principled test-time scaling: by executing the sub-task chain as progressive diffusion stages, editing quality can be improved by investing additional compute without retraining. Comprehensive experiments on OpenVE-Bench demonstrate the state-of-the-art performance across diverse editing categories, with ablations confirming the effectiveness of each component.

---


### 286. [ContourVLA: A Closed-Loop Perception-Action Contour Policy for Generalized Referring Expression Segmentation](https://arxiv.org/abs/2610.12107)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ruicheng Zhang, Kaiwen Shen, Jiaqi Hou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized referring expression segmentation (GRES) requires dynamically balancing high-level semantics for identifying a variable number of language-specified referents with fine-grained visual evidence for precise boundary delineation. This requirement challenges existing cascaded vision-language architectures, which typically rely on static feature interfaces and single-pass mask prediction, limiting adaptive perception and geometric correction. We introduce ContourVLA, a vision-language-action policy that recasts GRES as a closed-loop visuomotor process, in which editable contours serve as explicit policy states that condition multimodal perception and are updated by geometric action chunks. Evolution-Aware Semantic Scheduling (EASS) couples contour-guided bidirectional boundary sampling with state-conditioned routing of multilevel multimodal features, adapting perception to each contour state. Following supervised initialization, Dustbin-Augmented Entropic Credit Transport GRPO (DECT-GRPO) jointly optimizes discrete grounding and continuous contour actions with instance-level credits. Its rollout rewards and credits are derived from soft prediction-target correspondences that account for false positives and missed targets. ContourVLA improves gIoU over the strongest evaluated baselines by 8.7, 2.8, and 2.7 points on gRefCOCO val, testA, and testB, respectively, and achieves the highest mIoU across all eight RefCOCO, RefCOCO+, and RefCOCOg splits.

---


### 287. [One Word Opens the Gate: The Option-Channel Attack on Typed Decision Models as Agent Guardrails](https://arxiv.org/abs/2610.12292)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Seyedarmin Azizi, Erfan Baghaei Potraghloo, Massoud Pedram  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A typed decision model reads a piece of text and returns a probability over caller-defined options, each with a short written definition, generating no text. Recent work places these models in agent systems as guardrails: the component that reads a proposed tool call or incoming message and decides whether to allow it. We evaluate seven open-weight models in that role and report the two error directions separately: a fail-open error allows a prohibited action and is a vulnerability; a fail-closed error blocks a permitted one and is only a cost. On prompt-injection, jailbreak and toxic-content screening, accuracy at the allow-or-block decision ranges from 36% to 72% against a chance level of 50%. A low error rate in one direction only reflects which answer a model defaults to: one allows nearly everything, another blocks nearly everything. On a synthetic suite of agent tool calls, six lines of server log text that say nothing about the policy raise a gate's fail-open rate from 0% to 63% on a policy it otherwise decides correctly. Giving the permissive option a misleading name, with its definition and the judged text untouched, raises that rate to between 93% and 100% on the four models that place the label in their input. Every defense we tested is defeated, either by an attacker who targets its mechanism or by attacker-controlled text. Escalating the least confident decisions does not help either: a decision an attack has reversed is no less confident than the one it replaced. Parsing each policy field into a typed value does eliminate one attack, but it also makes the model unnecessary: a deterministic rule over those values reaches 100% accuracy on all six policies. These models can reduce how many cases reach a reviewer, but on this evidence they should not be the component that decides. Code is available at this https URL.

---


### 288. [One Block, Multiple Depths: Recurrent Vision Transformers with Depth-Programmed Experts](https://arxiv.org/abs/2610.12448)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Adrian Bulat, Yassine Ouali, Georgios Tzimiropoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we show that a single Transformer block, applied recurrently, can match the accuracy of a full-depth vision encoder at comparable inference FLOPs without intermediate feature distillation. reViT restores depth-specific transformations by representing the FFN at each recurrent depth as a convex combination of a small shared expert bank. A continuous normalized-depth coordinate programs this mixture, defining a resampleable trajectory through FFN parameter space. We evaluate this design in two regimes: supervised ImageNet-1k training and distillation from a DINOv2 teacher. Across both regimes, controlled adaptations identify weight-space merging as the strongest tested MoE family at a matching one-FFN budget, ahead of the token-dispatch and output-mixture alternatives. Trained from scratch, reViT-B/16 attains DeiT III accuracy with about 70\% fewer stored parameters. An 8-experts model distilled using only the teacher's output features retains nearly all of its DINOv2 teacher's linear-probe accuracy and transfers across classification, segmentation, and depth prediction. Elastic-depth training allows one checkpoint (trained model) to operate at multiple tested depths by resampling the same normalized coordinate interval. For fixed-depth deployment, the recurrent block can be materialized as a conventional dense graph, removing online routing and merging without changing the one-FFN-per-depth compute but expanding deployment storage.

---


> [!TIP]
> 当前位于：**251-288**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-288**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
