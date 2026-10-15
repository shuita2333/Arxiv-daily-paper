# 🧠 大模型相关研究 | 2026年10月16日

> 本类共 **313** 篇论文：已确认 **304** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-313](./part-07.md)

---

### 201. [Frustratingly Easy Majority Voting Using Length Conditioning](https://arxiv.org/abs/2610.19890)

**<font color=#1a73e8>作者：</font>** Fiorenzo Parascandolo, Enver Sangineto, Xiaoyi Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Majority Voting (MV) is a simple and widely used strategy which improves the reasoning accuracy of Large Language Models (LLMs) by allocating additional inference-time computation. Specifically, in MV multiple Chain-of-Thoughts (CoTs) are independently sampled and the most frequent final answer is selected. In this work, we propose Length-Conditioned Majority Voting (LCMV), a Test-Time Training approach which improves MV leveraging an empirical observation that has recently been established in several studies: longer CoTs tend to be associated with a lower probability of correctness. We formulate this inductive bias as a length-conditioned prior probability, which is modeled by a simple logistic function. Moreover, we adapt this prior at test time using only unlabeled testing data and without fine-tuning the LLM. Finally, the adapted prior is used to weight the vote of each sampled answer. Extensive experiments across multiple LLMs and reasoning benchmarks show that LCMV consistently improves over both standard MV and existing length-based and confidence-based aggregation strategies, while retaining the simplicity and model-agnostic nature of MV. Our code is available at: this https URL.

---


### 202. [On the Limits of Representation-Based Test-Time Adaptation for Multimodal LLMs](https://arxiv.org/abs/2610.19892)

**<font color=#1a73e8>作者：</font>** Mikołaj Piórczyński, Wojciech Masarczyk, Damian Sójka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models suffer significant accuracy drops under common corruptions. While test-time adaptation (TTA) successfully mitigates these shifts in CLIP-like contrastive models, its application to generative multimodal large language models (MLLMs) remains underexplored and uniquely challenging due to their sequential token generation. In this work, we demonstrate that representation-based TTA fails to recover performance in MLLMs. Our experiments reveal that even when violating standard TTA assumptions by leveraging target data offline, sample-blind feature alignment recovers only marginal accuracy. We attribute this failure to the nature of corruption shifts: unlike CLIP-like architectures, which benefit from a shared domain-shift direction within a single pooled classification embedding, MLLM visual token sequence shifts are nearly orthogonal and span the full embedding this http URL findings bound what any sample-blind, position-shared correction at a single encoder site can achieve, establishing that representation-space interventions alone might be insufficient to ensure corruption robustness in MLLMs.

---


### 203. [How GUI Agents Fail: GraceBench for Execution Stability Diagnosis](https://arxiv.org/abs/2610.19900)

**<font color=#1a73e8>作者：</font>** Ridong Zhang, Shuxian Liang, Chaoqun Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As GUI agents are increasingly deployed for mobile task automation, their reliability depends not only on final task outcomes, but also on whether they reach these outcomes through stable interaction trajectories. In automation workflows, unnecessary actions, detours, and execution errors can add noise to collected data, introduce irreversible side effects, or undermine trust, even when the agent eventually completes the task. It is therefore important to systematically diagnose the execution stability, including whether an agent deviates from a feasible path, enters a loop, becomes stagnant, or recovers from unstable actions. Existing benchmarks, however, primarily assess final task success or a small set of intermediate milestones, leaving step-level execution behavior unclear. To bridge this gap, we introduce GraceBench, an online evaluation framework that represents the reachable interaction space of mobile applications as UI Transition Graphs (UTGs), providing a structural reference for step-level execution diagnosis. To support reliable alignment between dynamic UI observations and graph states, GraceBench uses video-grounded trajectory evaluation over this graph-aligned representation, assessing process stability beyond final success with metrics such as deviation rate, loop burden rate, and recovery ability. GraceBench contains 169 tasks spanning 10 applications and constructs 10 UTGs with 2,909 canonical GUI states and 3,116 observed transitions. Across 3,718 trajectories, GraceBench shows that outcome scores hide execution instability: GPT-5.6 Sol achieves the highest success rate (SR) but the lowest recovery ability, 51.24% of successful runs still contain a deviation or loop, and trajectories with the same success rate (SR) and completion rate (CR) can differ substantially in recovery behavior. Code and data will be released on this https URL.

---


### 204. [Multimodal Medical Image Parsing with Task-Specific Low-Rank Adapters](https://arxiv.org/abs/2610.19901)

**<font color=#1a73e8>作者：</font>** Taha Sabir, Alberto Montero Molina, Thinh Quang Ly 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting a single vision-language model to medical image parsing requires training choices that reflect the demands of each task. We study task-specific adaptation with Qwen3.5-9B for FLARE 2026 Task 3, covering six task families and seven imaging modalities. Our system couples a shared, frozen 4-bit backbone with LoRA adapters selected from the input question. We customize adapter ranks and prompts, rebalance rare classification targets, and supplement regression training with dermatology classification examples. On the fixed internal holdout, the task-specific adapters achieve a dataset-macro balanced accuracy of 0.7791 for classification, a dataset-macro micro-F1 of 0.6286 for multi-label classification, a counting mean absolute error (MAE) of 11.73, a dataset-macro detection F1 of 0.8914, a dataset-macro regression MAE of 9.78, and a report-generation CRIMSON score of 0.8204. On the organizer's 1,703-example hidden-validation set, the submitted system achieves 0.8496 classification balanced accuracy, 0.5338 sample-averaged multi-label F1, and 14.5950 regression MAE. The final 30.1 GB container averages 3.1 seconds per case, including model loading, and produces identical outputs across repeated verification runs. The benefits vary across tasks, supporting the use of task-specific adapter configurations and image budgets within a shared medical vision-language model. Code is available at this https URL.

---


### 205. [Beyond Benchmark Accuracy: A Diagnostic Test for LLM Chemical Prediction](https://arxiv.org/abs/2610.19906)

**<font color=#1a73e8>作者：</font>** Yanyi Su, Yu Zeng, Hongshuai Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs have achieved strong performance on chemical prediction benchmarks. However, existing evaluation methods typically provide target entity identity information directly, making it difficult to determine whether model predictions arise from transferable structure-property reasoning capabilities or rely on target-related contextual information or memory retrieval. We propose the Identity-Blinded Reasoning Diagnostic framework to evaluate chemical prediction models when target entity identity information is hidden. In this framework, the target is no longer directly defined by its entity identity, but instead by a known source entity and an explicit structural edit operation. This setting preserves the information required to determine the target while reducing the opportunity for models to access target identity cues. We evaluate this framework across six tasks spanning odor prediction, molecular property prediction, retrosynthesis, and reaction yield prediction. The results show that models generally achieve better prediction performance when source and target entity properties are consistent. Providing explicit source entity labels further strengthens this dependence. Moreover, while keeping the target entity, structural change, and ground-truth label unchanged, replacing only the source entity label causes some model predictions to systematically shift toward the substituted source labels. These results indicate that high benchmark accuracy in chemical prediction tasks does not necessarily imply that LLMs possess reliable structure-property reasoning capabilities. Our diagnostic framework provides a controlled evaluation approach for testing whether models can genuinely update predictions according to entity changes. The framework can be extended to other AI for Science tasks, particularly those where targets can be defined through transformations of known entities.

---


### 206. [Sparse Transformer: a Controlled Testbed for Mechanistic Interpretability](https://arxiv.org/abs/2610.19907)

**<font color=#1a73e8>作者：</font>** Anton Korznikov, Alexey Dontsov, Elena Tutubalina  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability aims to decompose neural network computations into human-understandable features, yet progress is limited by the absence of ground-truth units to evaluate against. We address this with a Sparse Transformer (ST): a 5-layer language model trained on TinyStories whose wide, TopK-sparse MLP forces neuron specialization. We show that ST neurons are highly interpretable: they outperform a loss-matched dense transformer by 43% on AutoInterp, and circuits of a median of 12 neurons suffice to reproduce individual model predictions. This testbed allows us to directly compare feature learning methods: Transcoder, which approximates the MLP input-output mapping, recovers ST's neuron vectors with 52.6% higher cosine similarity than Sparse Autoencoder, which only reconstructs outputs. Furthermore, the ST enables a controlled study of polysemanticity: distilling its sparse MLP into a dense counterpart reveals how compression leads to feature superposition. These results show how a known reference basis sharpens evaluation and understanding, a role we hope the ST can serve for the field.

---


### 207. [When Non-Adversarial Noise Hurts Learning: Benchmarking Skill Self-Evolution in Agents](https://arxiv.org/abs/2610.19910)

**<font color=#1a73e8>作者：</font>** Tao Yu, Zhongtian Luo, Yuchen Long 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly improve by distilling experience into reusable skills, but errors in that experience can persist in learned rules and affect later tasks. Existing evaluations largely examine clean learning or perturbations encountered after skills are frozen, leaving robustness during self-evolution insufficiently understood. We introduce RSE-Bench, to our knowledge the first benchmark for evaluating skill self-evolution under ordinary, non-adversarial noise. It spans four domains and six benchmarks, with controlled perturbations to instructions, environmental evidence, execution records, and outcome--record pairings that preserve the underlying tasks and native scoring rules. The protocol separates noise during learning from input-side noise at evaluation, testing frozen skill stores on held-out tasks. We also introduce \textsc{RSEClaw}, a method-agnostic framework supporting consistent noise injection and process diagnostics of actual exposure and skill updates. Across three methods and two backbones, noisy learning retains only $25.5\%$--$42.1\%$ of the aggregate gain achieved by clean self-evolution, depending on the noise type. Perturbations confined to execution records and outcome--record pairings cause average losses comparable to input-side noise, despite leaving the original executions and evaluations intact. Diagnostics further identify differences in candidate skill text that coexist with small changes in mean held-out performance.

---


### 208. [Not All Criteria Matter: Importance-Aware Criteria Weighting for Rubric-Based LLM Evaluation](https://arxiv.org/abs/2610.19915)

**<font color=#1a73e8>作者：</font>** Haocheng Yang, Licheng Pan, Yiming Dong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based evaluation assesses the responses of large language models (LLMs) by aggregating the verification results of explicit criteria, yet not all criteria matter equally. However, existing methods commonly aggregate the verification results with uniform weighting, which assigns minor and overlapping criteria the same weight as essential ones and thus produces misleading evaluation scores. Although some methods prompt an LLM to directly assign weights, direct weighting requires a holistic judgment over all criteria that LLMs struggle to make reliably. To address these limitations, we propose Importance-Aware Criteria Weighting (ICW), which derives the weights of criteria from pairwise importance comparisons made by an LLM. Specifically, ICW transforms the holistic judgment over all criteria into a series of pairwise importance comparisons, checks and revises inconsistent comparisons, and derives the weights from the principal eigenvector of the comparison matrix. Extensive experiments demonstrate that ICW consistently outperforms uniform weighting and competitive weighting methods, and translates into better policy models in downstream reinforcement learning.

---


### 209. [MolHop: Scaffold-Hopping Molecular Design with Agentic Reinforcement Learning](https://arxiv.org/abs/2610.19920)

**<font color=#1a73e8>作者：</font>** Yanyi Su, Chenyan Wang, Yulei Gong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular design is often formulated as an optimization problem over existing molecular spaces. However, molecular optimization and the discovery of structurally distinct replacement molecules represent two fundamentally different search problems. LLM-based molecular design agents typically perform the former, conducting local refinement within the neighborhood of existing structures to improve target properties through structural modifications. In contrast, the latter requires exploration of a broader chemical space to discover molecules with entirely different scaffolds while preserving the functional characteristics of reference molecules. We propose MolHop, an agentic framework for cross-scaffold molecular discovery that enables models to navigate and edit within a pre-organized chemical space. MolHop organizes approximately 1.6 million molecular scaffolds from commercial molecules into a coarse-to-fine hierarchical action space. The agent selects new exploration regions through scaffold navigation actions and adjusts candidate properties through molecular editing. The framework maintains historical trajectory memory to support long-horizon search processes. On drug molecule and commercial compound tasks, connecting Grok-4.6 and DeepSeek-Flash-V4.1 to the MolHop framework substantially improves their cross-scaffold joint success rates. We develop MolHop-9B through agentic reinforcement learning, and MolHop-9B outperforms generative baselines including GPT-5.6-sol, Claude-5-Opus, and Gemini-3.1-Pro, while generating candidate molecules with larger scaffold differences from the reference molecules. These results demonstrate that effective molecular discovery beyond the traditional optimization paradigm requires structured chemical and action spaces, enabling agents to explore new structural regions rather than merely refine existing molecules.

---


### 210. [MemDuet: Learning Dual-Process Memory for Long-Context Reasoning](https://arxiv.org/abs/2610.19928)

**<font color=#1a73e8>作者：</font>** Jiangcheng Song, Haodong Jing, Yulin Mu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning over infinitely long documents is becoming a reality with recurrent memory agents. However, increasing context length exacerbates the trade-off between reasoning performance and inference efficiency. Inspired by Kahneman's account of fast and slow thinking, we propose MemDuet, a dual-process memory framework that learns to coordinate a small language model for fast, parallel evidence selection from raw context chunks (System 1) with a large language model for memory-update verification and memory updates in document order (System 2). We train MemDuet in three stages: supervised fine-tuning of System 1 for evidence selection, Group Relative Policy Optimization (GRPO) of System 2 for verification and memory rewriting, and joint optimization of both policies to coordinate selection and updating for long-context reasoning. Experiments on diverse long-context reasoning benchmarks (RULER-HQA, LongBench v2, and 2WikiMultiHopQA) demonstrate a favorable accuracy-efficiency trade-off as context length grows. Averaged across evaluation settings on the three datasets, MemDuet achieves an end-to-end inference speedup of 9.74x and an output-token reduction of 73.91% relative to RL-MemAgent.

---


### 211. [Instruction Mining From Images: Constructing a Synthetic Dataset for Multimodal Learning ILSP DCVLR Competition Submission](https://arxiv.org/abs/2610.19932)

**<font color=#1a73e8>作者：</font>** Eleni E. Kasoura, Dimitrios Damianos, Georgios Paraskevopoulos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents a compact and reproducible pipeline for synthesizing and curating image-based instruction-response pairs for DCVLR. We draw from the Cauldron collection and use Magpie-style instruction and response synthesis with Qwen2.5-VL-7B Instruct to create concise, image-conditioned instruction pairs. The pipeline consists of instruction synthesis, conditioned on input images and controlled via a system prompt, sanitization, tagging, and filtering of the instructions based on the score obtained by a reward model (DeBERTa-v3). We retain samples with positive scores to maximize the quality of the generated instructions. We observe that score distributions have a median and mean reward score of ~ 1.53 and ~ 1.75 respectively, indicating that most generated instructions are of good quality. The resulting dataset contains diverse instructions in the math, spatial, and social reasoning domains.

---


### 212. [To Reason but Not to Stop: Understanding and Recovering Pruned Large Reasoning Models](https://arxiv.org/abs/2610.19934)

**<font color=#1a73e8>作者：</font>** Minh-Anh Nguyen, Nguyen T. Ha Lan, Xiyan Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Weight pruning can degrade the accuracy of large reasoning models (LRMs), yet it remains unclear whether it damages reasoning itself. We find that much of this degradation stems from a failure to stop rather than to reason. As sparsity increases, pruned LRMs increasingly fail to terminate within the token budget, often after the correct answer has appeared in their reasoning, instead falling into repetitive loops, even though they still recognize where the dense model would stop. We further find that the hidden-state difference between terminating and looping continuations is consistent across pruned checkpoints, suggesting a shared direction associated with committing to an answer. Building on this, we propose Termination-Guided Activation Steering (TGAS), a training-free method that adds this direction to the residual stream at inference time. Across six LRMs, three pruning pipelines, and math and code benchmarks, TGAS improves termination and overall accuracy while reducing repetitive reasoning and generation length, showing that this failure is actionable.

---


### 213. [When Protection Overrides Consequences: Understanding Protection Mode in Large Language Model Decision-Making](https://arxiv.org/abs/2610.19948)

**<font color=#1a73e8>作者：</font>** Yuanfan Li, Junyi Chen, Qi Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier language models excel at complex tasks yet may prioritize protection over larger physical consequences in simple, urgent decisions. GPT-5.6 Sol, for example, moves a girl playing in shallow water before retrieving a submerged camera. We call this Protection Mode and study it with ProtectionBench: 285 prompts, 34 physical families, and nine models. At lowest effort, at least one of four responses prioritizes the subject on 34.74% of Sol prompts and over 83% of MiniMax M3 and Qwen3.5-27B prompts; none of four independent human raters does so. Controls show that choices usually track physical risk. We elicit both risks before requesting an action. Some models assess risk incorrectly; others state the correct ordering but still choose the subject. Qwen3.5-27B with thinking shows 100% correct risk ordering but 57.81% subject choice among eligible conversations on eight selected scenes. Attention audits find no stable reduction in attention to relevant facts; removing the stated risk direction reduces object-first choice in dots3-note-prev but not detectably in Qwen3.5-27B. Adding a general "people or animals before property" rule increases subject choice by 19-38 percentage points, whereas factual reminders favor the object by 0.7-5.2 points. Removing naturally generated versions of that rule lowers subject choice by 10-15 points. We also examine whether post-training introduces this pattern. Base models already show Protection Mode; post-training changes justifications more than choices.

---


### 214. [AtomSearch: Evidence-Grounded Tree Search for Agent Skill Optimization](https://arxiv.org/abs/2610.19951)

**<font color=#1a73e8>作者：</font>** Jia Tong, Senyou Deng, Min Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent skills adapt frozen models through editable external instructions. Revising several rules at once makes changes difficult to inspect, while judging each local edit only by its immediate score can discard useful intermediate states. We introduce AtomSearch, which keeps revision actions local while using subsequent skill states to guide search. Contrastive atomic editing links each primitive rule edit to failed and successful executions, a behavioral hypothesis, and an intended scope. Skill-State Tree Search (STS) evaluates short edit compositions and selectively retains them as executable states that can be revisited and extended. Outcome memory supplies later proposals with observed repair and regression statistics. We evaluate AtomSearch across four tasks and five target models. With deepseek-v4-flash, it exceeds SkillOpt on three of four tasks, including a 9.68-percentage-point gain on LiveMathematicianBench, and SkillOpt's final skills contain 2.3-19.7 times as many characters. In 67% of completed searches, the best validation state passes through an ancestor that was not highest-scoring at its depth. These results show how local rule edits can support the exploration of useful revision paths and yield compact skills, with additional offline evaluations used to explore alternative states.

---


### 215. [Safe-FCL: Continual Risk Awareness and Fine-Grained Safety Aggregation for Federated Continual Learning of LLMs](https://arxiv.org/abs/2610.19968)

**<font color=#1a73e8>作者：</font>** Shuaijie Ma, Yongkang Hu, Yu Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning enables large language models (LLMs) to learn collaboratively from distributed client data, but malicious client updates can compromise global model safety. As federated tasks evolve, changing malicious update patterns challenge the ability of existing defenses to maintain reliable risk detection over time. To address this challenge, we propose Safe-FCL, a framework integrating continual risk awareness with fine-grained safety aggregation for federated continual learning of LLMs. Specifically, the Continual Risk Awareness (CRA) mechanism learns emerging risk patterns across sequential tasks and constrains detector updates using a protective subspace derived from historical features, mitigating forgetting of previously learned malicious patterns while adapting to new risks. To translate risk awareness into aggregation-level safety control, the Fine-Grained Safety Aggregation (FGSA) mechanism combines client-level risk assessments from CRA with module-level deviations from historical update behavior to adaptively regulate aggregation contributions, suppressing potentially malicious updates while minimizing unnecessary restrictions on benign updates. Extensive experiments demonstrate that Safe-FCL outperforms current SOTA methods, improving global-model Rule and MD-Judge scores in federated continual learning by 0.41% and 0.64%, respectively, while increasing average risk recognition accuracy by 2.01%.

---


### 216. [LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation](https://arxiv.org/abs/2610.19975)

**<font color=#1a73e8>作者：</font>** Zefeng He, Yunkai Chai, Xiaoyang Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Mixture-of-Experts (MoE) models combine parameter reuse with sparse computation to improve performance under matched budgets. Prior work demonstrates that different loop visits can play different roles even when they share parameters. To probe the contributions of different loop visits, we learn separate residual coefficients in a model that applies a shared block twice, observing a smaller scale in the first visit. Fixed coefficient experiments show that reducing the first visit's scale preserves or improves performance, whereas the same reductions to the second hurt it. This asymmetry motivates us to explore asymmetric compute allocation. We propose \textbf{LatentLoop}, which compresses the first visit's sequence, retains full resolution in the second, and reallocates saved computation to increase the hidden size. We further learn how strongly the first visit updates the full sequence, and share MoE weights across visits while using separate attention parameters to accommodate their different sequence resolutions. Across 15 configurations spanning 1.3B--7B parameters, with the largest budget exceeding $10^{21}$ FLOPs, LatentLoop consistently lowers validation NLL. At a fitted NLL of 1.988, predicted compute savings are 19.0\% and 7.9\% relative to vanilla MoE and the looped baseline. It also improves average scores on nine benchmarks at all sizes in 0-shot and 5-shot settings. These results suggest asymmetric compute allocation is a promising direction for looped MoE models.

---


### 217. [SoK: Grading Open-Text Legal Answers, from Law School Exams to Trustworthy Rubric Judges](https://arxiv.org/abs/2610.19992)

**<font color=#1a73e8>作者：</font>** Sebastian Nagl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Law students are examined through open-text answers: case solutions, essays and memos that apply the law to a set of facts. Such answers are expensive to grade, human graders disagree widely on them, and large language models (LLMs) now offer to grade them at scale, both in teaching and in the benchmarks that test legal AI. This paper systematizes how open-text legal answers can be evaluated. We derive eight desiderata from educational measurement and from the law that governs exams, among them validity, reliability, reasons, credit for defensible alternative solutions, robustness to gaming and human oversight. We then compare eight evaluation paradigms against them, from unstructured human grading to LLM judges with instance-specific rubrics and pairwise comparison. Three findings stand out. A rubric written for the task is the strongest lever for agreement between an LLM judge and human graders, but the reported figures answer different questions and rarely come with the human agreement they must be read against. The central validation gap lies where examination law is most demanding: defensible alternative solutions, follow-on errors, and the examiner's correction of model judgments. And rubric-centred grading is the most auditable family, because it makes the standard, its application and the final decision checkable. From this we derive the trustworthy rubric judge: an instance rubric that credits arguments and alternative paths,evidence checked in code, probes, repeated runs, calibration against independent human grades,logging, and an examiner who reads every script. We state what each safeguard rests on, what remains to be tested, and the uses the evidence supports today.

---


### 218. [Gray-Box Hallucination Detection in LLMs with Token Identities](https://arxiv.org/abs/2610.19996)

**<font color=#1a73e8>作者：</font>** Shaked Goldshtein, Yitzchak Grunbaum, Fabrizio Frasca 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often produce fluent but factually incorrect output. Gray-box detectors identify such hallucinations from the token-probability statistics emitted during generation, avoiding the need for white-box access to hidden states that frontier models do not provide. These detectors, however, typically rely only on probability-derived representations and ignore the identities of the candidate tokens. They can therefore observe how uncertain the model is, but not what it is uncertain about. Consequently, they cannot distinguish between a model that is torn between "big" and "small" and one that is torn between "big" and "huge" when the two pairs receive the same probability distribution.
We introduce GURI (Gray-box Uncertainty Representations with Identity), a lightweight gray-box hallucination detector that combines candidate-token probabilities with per-token vector identifiers. This exposes which alternatives the model considered while preserving the accessibility and transferability of the gray-box setting. Across three open-weight models and three question-answering benchmarks, GURI increases mean test ROC-AUC from 72.09% to 79.09% over a probability-only baseline. On the closed-source GPT-4.1 model, mean ROC-AUC increases from 67.39% to 71.84%. Among the three open-weight models, GURI outperforms transferred probability-only baseline in 17 of 18 directed cross-model transfers without fine-tuning. For the three open-weight models, cross-dataset transfer between HotpotQA and TriviaQA with the model held fixed improves mean ROC-AUC over transferred LOS-Net by 3.76 points.

---


### 219. [ShadAR: Real-time Prompting On-demand Visual Augmentation in Augmented Reality](https://arxiv.org/abs/2610.19998)

**<font color=#1a73e8>作者：</font>** Yanni Mei, Samuel Hartenstein, Jonas Wombacher 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Augmented Reality can reshape our visual perception (e.g., simulating color blindness) yet such effects are typically pre-programmed by experts, making visual augmentation static and inflexible. We introduce ShadAR, an AR system that allows users to describe expected visual augmentations (e.g., "Blur all people") for changing their vision in real time. ShadAR can graphically manipulate AR passthrough in real time via shader injection. When receiving a user's prompt, ShadAR uses LLMs (GPT5.2) to interpret the user's intent, analyzes the user's view with object detection (YOLOv26), generates a pixel shader, and applies it to the targeted region on AR passthrough. To understand usage patterns, we invited 21 HCI researchers to use ShadAR, identifying four application domains (design, health, productivity, and social interaction) and two prompt-framing patterns: procedural prompts specifying what to modify and how ("Highlight the book."), and end-goal prompts conveying desired mental or behavioral states ("Make me laugh."). Such end-goal prompts suggest a future in which users specify outcomes (e.g., "Make me not miss my flight") while the system determines how to realize them, though often with inherently indeterminate results. We discuss design opportunities for ShadAR and ethical concerns.

---


### 220. [A Strong Harness Narrows the Model Gap: A Comparative Evaluation for Legislative Document-to-XML Conversion](https://arxiv.org/abs/2610.19999)

**<font color=#1a73e8>作者：</font>** Palvika Bansal, Rittika Jindal, Ruichong Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal-content reproduction requires matching the source exactly in section hierarchy, verbatim text, citations, and amendment spans; a dropped citation or mislabeled amendment carries into the products lawyers rely on. We report an industrial pipeline converting U.S. state legislation into strict, schema-constrained XML, and hypothesize that its accuracy comes from harness engineering, the deterministic tooling built around a model, more than the model itself. Our controlled ablation crosses three harnesses (zero-shot, a single tool-using agent, and a decomposed multi-agent pipeline) with three Claude models on 153 gold bills from two jurisdictions. The harness narrows the model gap: the weakest model in the full pipeline beats the strongest model alone (0.948 versus 0.806, paired bootstrap p less than 0.001). Because the two agentic harnesses share identical tools, their gap comes from orchestration: decomposition plus the persisted state and per-agent context it brings. Across four scored dimensions, the model spread at zero-shot (0.68 to 0.81) narrows to 0.95 at the full pipeline; the residual sits almost entirely in citation normalization, where the canonical identifier is retrieved from an external authority rather than generated from the weights, so a deterministic lookup tool supplies the exactness that a larger model does not.

---


### 221. [What Coding Agents Leave Unsaid: Measuring Task-State Gaps Between Execution and Reports](https://arxiv.org/abs/2610.20003)

**<font color=#1a73e8>作者：</font>** Guoyang Xu, Rui Zhang, Xiuyu Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human supervisors rely on coding agents' reports to assess progress, verify repairs, and decide when to intervene. But a supervisor cannot investigate a failure they were never told occurred. Failed attempts, workarounds, and unresolved risks may disappear from routine reports, leaving supervisors unaware of issues that warrant scrutiny. We conduct CTXGAP, a measurement study quantifying the gap in task-state recoverability between agents' accumulated user-facing reports and their full recorded execution contexts. Across 37 coding tasks and 4,799 valid probes, agents answer 93.6% of task-state questions on demand; full-context readers recover 92.7%, while report-only readers recover 52.0%, a 40.7-point gap. At the final checkpoints of 30 verified fixes, the gap remains 34.8 points. Human annotation identifies states mentioned without enough supporting detail as the largest category of unrecovered information, and model-assessed supervision-relevant states retain substantial gaps. Full terminal scrollback improves recovery to 73.6% but still trails full context. Under matched report lengths, context-informed rewrites improve recovery by about eight points, without a detectable targeted-over-natural advantage. Positive gaps persist across harnesses and independent DeepSeek execution and measurement. CTXGAP establishes report-based task-state recoverability as a complementary evaluation dimension.

---


### 222. [ChemArgus: Automated Scientific Diagnostics for Lab-Grade Multimodal Chemistry Reasoning: A Frontier Benchmark](https://arxiv.org/abs/2610.20012)

**<font color=#1a73e8>作者：</font>** Hanyao Guo, Mo Cui, Zihan Tan 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chemistry evaluation has moved past multiple-choice probes toward open-ended expert problems, yet the benchmarks that define the current frontier still score answer endpoints alone. Such scoring conflates memorized facts with stepwise derivation, treats visual and textual inputs as interchangeable, and confounds long-horizon planning with stepwise execution. These blind spots prevent any diagnosis of where the reasoning chain breaks in a model. We present ChemArgus, a competition-level chemistry benchmark drawn from chemistry competition material, textbooks, and research papers, whose scoring replaces the answer endpoint with three measurement properties. Fine-grained scoring grades every subquestion point by point with partial credit, so a score lands at the level of the step rather than the outcome. Multimodal capability is priced on every problem containing a real image, paired with a controlled text description, so visual understanding is measured against text on identical tasks. Diagnostic attribution reads paired metrics that share one scoring unit and differ only in context construction, so a gap between two scores isolates a single cause, namely integration, propagation, or local reasoning. GPT-5.6-Sol scores 23.2% on unassisted whole-problem solving against 28.8% and 30.4% under the two sequential metrics, a gap measuring the integration burden. Through rubric partial credit and these cause-isolating score gaps, ChemArgus shows not only whether a model answers chemistry correctly but where its reasoning chain fails, so that every score it reports doubles as a diagnosis, a readout of the chain rather than a verdict, aiming to guide language models step by step on their path toward chemistry expertise, one corrected step at a time, each step priced by the rubric, point by point.

---


### 223. [Memorizing Who, Knowing How: Benchmarking Personal and Procedural Memory for Persistent Assistants](https://arxiv.org/abs/2610.20022)

**<font color=#1a73e8>作者：</font>** Maosheng Qin, Qi Zhang, Mingxuan Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory systems for persistent personal agents must move beyond isolated memories, maintaining both personal memory about whom they serve and procedural memory about how to act. Crucially, in harness-based personal assistance, procedures or skills are inherently user-conditioned: personal context determines which procedures apply, how they are instantiated, and when they should change. Existing benchmarks typically emphasize either personal or procedural memory, leaving their interaction underexplored. We introduce PraxisMemBench, a harness-based benchmark for persistent personal assistance across daily-life and work trajectories, where personal and procedural memory evolve together and later tasks depend on both. Experiments show that maintaining two memory types separately is insufficient, with completion dropping from single-type to interdependent dependencies (84.6% to 77.9%). More broadly, across existing methods, relation-related failures increase from early to late sessions as interaction history grows (59.8% to 72.9%), revealing a continual-maintenance challenge: writing correct memories is not enough if their evolving content and organization cannot be preserved for later retrieval. To address this, we propose PraxisMem, which uses privileged joint-state supervision to internalize the ability to maintain memory content and organization into the memory manager, with location-aware GRPO and dynamic residual-routed OPSD. PraxisMem reaches 40.78% overall Session Success Rate, compared with 20.60% for Claude Code's native memory.

---


### 224. [FACES: Fine-grained Gated Semantic Alignment for Multimodal Emotional Support Conversation](https://arxiv.org/abs/2610.20051)

**<font color=#1a73e8>作者：</font>** Hang Ren, Peidong Wang, Yichen Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, with advances in multimodal interaction technologies and the growing demand for intelligent emotional support, Multimodal Emotional Support Conversation (MESC) has emerged as an important task. However, existing systems still suffer from shallow responses and inappropriate support strategies due to weak semantic feedback, cross-dimension reward compensation, and coarse reasoning supervision. To address these challenges, we propose FACES, a fine-grained gated semantic alignment framework for MESC. Specifically, FACES integrates multi-source rewards to construct multidimensional semantic and functional alignment signals, employs a non-compensatory gated fusion mechanism to reduce cross-dimension reward offset, and leverages structured Chain-of-Thought (CoT) anchors to perform token-level credit assignment. Under a controlled response-length protocol, FACES improves the average MLLM-based evaluation score from 3.61 to 4.04 and achieves an 80.22% pairwise win rate over SOTA. Human evaluation under the same protocol yields a 75.3% preference rate. Results on three external datasets further support transferability. The code and dataset are available at this https URL.

---


### 225. [What Is a Clarification? Estimating Model-Dependent Input Ambiguity](https://arxiv.org/abs/2610.20052)

**<font color=#1a73e8>作者：</font>** Jingqin Tang, Tim Tomov, Sebastian Schmidt 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ambiguous inputs can admit multiple interpretations, each potentially yielding a different answer. Existing work largely treats this ambiguity as a property of the input, yet for a particular language model, only some alternatives may be known and answerable. We therefore distinguish world ambiguity, capturing all alternatives admitted by an input, from model ambiguity, capturing those accessible to the responding model. To characterize these alternatives, we formalize natural-language clarifications through three desiderata: \emph{uniqueness}, \emph{faithfulness}, and \emph{answer equivalence}. We show that these desiderata induce a one-to-one correspondence between valid answers and equivalence classes of clarifications, implying that any interpretation can be represented either by its answer or by the clarifications that uniquely express it. We leverage this correspondence to introduce \circleclar{}, a black-box method that estimates the set of answers available to a model by checking consistency along an answer--clarification--answer cycle. Across open-domain QA and executable Text-to-SQL, \circleclar{} achieves strong recovery of these answer sets. In QA, the recovered support yields the strongest overall performance in model-dependent ambiguity detection and enables effective selection among answering, clarifying, and abstaining. Together, these results demonstrate the practical value of a model-dependent view of ambiguity and its characterization through an answer-clarification correspondence.

---


### 226. [GeoCloak: An Agentic Framework for Semantics-Preserving Geolocation Privacy via Peripheral Clue Manipulation](https://arxiv.org/abs/2610.20055)

**<font color=#1a73e8>作者：</font>** Yixin Wu, Mingjie Li, Yun Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of large vision language models (LVLMs) has made geolocation inference from images highly accurate and accessible. This poses serious privacy risks: a passive adversary with black-box LVLM access can infer a user's location from a single photo with no metadata. Existing protection methods rely almost exclusively on adversarial perturbation, which introduces perceptible visual artifacts and utility degradation. We identify the visual-geolocation asymmetry: geolocation-decisive clues, such as street signs, tend to be visually peripheral but dominate location inference. Exploiting this asymmetry, we propose GeoCloak, an agentic framework for semantics-preserving geolocation privacy protection. It acts as a clue-aware planner that analyzes each image to identify geolocation-relevant clues, dispatches targeted semantic edits to directly suppress peripheral clues, and autonomously configures adversarial perturbation to further suppress residual geolocation features, all under iterative utility-aware feedback. We evaluate GeoCloak on four diverse datasets spanning 108 countries and 576 cities against five LVLMs and three inference methods. GeoCloak reduces overall city-level accuracy from 41.2% to 9.9%, approximately half of the best-performing baseline, while achieving substantially superior utility preservation both qualitatively and quantitatively. We hope this work takes a meaningful step toward practical, semantics-preserving geolocation privacy protection, giving users greater control over the location information inadvertently embedded in their shared images.

---


### 227. [Beyond Correctness: Compute-Responsive Data Selection for Reasoning Model Post-Training](https://arxiv.org/abs/2610.20057)

**<font color=#1a73e8>作者：</font>** Liang He, Xiangyu Li, Yuxin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning language models increasingly rely on test-time compute scaling, yet most existing work studies how to allocate inference computation while treating the model itself as fixed. We ask a complementary question: can reasoning models be post-trained to make better use of a given amount of test-time compute, and which examples are most useful for this goal? Our key observation is that reasoning problems differ substantially in their response to additional computation. Some are already solved under limited compute, others remain unresolved even after further reasoning, while a distinct subset changes from complete initial failure to success when additional reasoning is provided. We call these compute-responsive (CR) examples and introduce Compute-Responsive Data Selection (CRDS), a post-training data-selection principle that prioritizes examples with empirically demonstrated marginal utility from additional reasoning. On Qwen3-8B, SFT on CR examples recovers 45.3\% of held-out low-compute failures, compared with 40.6\% when training on already-solved examples. The advantage extends beyond the selected CR split: SFT-CR reaches 51.8\% overall accuracy on an independently sampled test distribution, with the gain concentrated on compute-responsive problems. CR training also shifts the compute--accuracy frontier across inference budgets from 512 to 4,096 tokens, outperforming matched non-CR training throughout and reaching 48.1\% recovery at the largest budget. The same pattern is supported across multiple data sources, remains visible under on-policy distillation, and extends to Llama-3.1-8B-Instruct when CR sets are reconstructed separately for that model. Better test-time compute utilization can therefore be learned through post-training, with recoverable responses to additional reasoning providing a particularly informative signal for selecting training examples.

---


### 228. [Which Knowledge Should LLMs Trust? Uncovering a Generalizable Steering Direction Across Knowledge Conflicts](https://arxiv.org/abs/2610.20067)

**<font color=#1a73e8>作者：</font>** Yibin Lou, Yi Hu, Jianhui Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) frequently encounter conflicts between internal parametric knowledge and external contextual knowledge, yet the mechanisms governing this selection remain unclear. We show that the choice between context and parametric knowledge is linearly represented and can be controlled along a single direction in the model's residual stream. We first demonstrate that this direction generalizes across factual-conflict settings, including context formats, knowledge categories, and datasets, while consistently shifting behavior between parametric and contextual answers. We then transfer a direction learned from simple factual conflicts to three more complex task families: RAG, memory, and rule following, where models must acquire information from retrieved documents, interaction histories, or explicit rules. Across four model families and multiple transfer settings, steering consistently improves the use of prompt-provided information over the unsteered model. These results suggest that the direction captures a transferable preference for external knowledge rather than a mechanism specific to factual conflicts.

---


### 229. [VisualWorldBench: A Fine-Grained Multi-Task Benchmark for Evaluating Visual World Knowledge in MLLMs](https://arxiv.org/abs/2610.20083)

**<font color=#1a73e8>作者：</font>** Chen Chen, Zheming Liang, Jiaqi Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual world knowledge is a core capability of multimodal large language models (MLLMs), underpinning knowledge-intensive visual question answering and fine-grained visual reasoning. However, existing benchmarks remain limited in two key respects. First, their category coverage is narrow: most benchmarks span only a small number of categories across a few domains, falling far short of the open-ended scale of real-world visual entities. Second, their task construction is often insufficiently rigorous: models can answer correctly using coarse-grained cues, vague associations, or elimination strategies without truly mastering precise concepts, making it difficult to accurately assess their knowledge of fine-grained entities. We introduce VisualWorldBench, a taxonomy-grounded multi-task benchmark built on a hierarchical taxonomy of 21,291 leaf-node classes across 8 visual domains, with 32,541 evaluation instances whose ground-truth labels cover 15,479 categories across four complementary tasks: closed-set recognition, contrastive selection, precise localization, and open-world naming, covering different directions of knowledge retrieval and varying degrees of answer openness to comprehensively evaluate visual world knowledge. Most questions are constructed from taxonomically proximate categories, forcing precise discrimination among fine-grained entities. Experiments reveal that the strongest closed-source model achieves only 80.4% average accuracy, exposing capability gaps hidden under conventional benchmarks. We further construct VisualWorldBench-50K, a training resource covering 50K+ categories. Fine-tuning on VisualWorldBench-50K yields over 21 percentage points improvement on VisualWorldBench, with consistent transfer to public fine-grained recognition and visual knowledge benchmarks.

---


### 230. [Scoping the Landscape of Large Language Model-based Affective Personal Informatics: Review, Reflection, Future Direction](https://arxiv.org/abs/2610.20084)

**<font color=#1a73e8>作者：</font>** Minjie Liu, Lihuan Li, Xuran Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Affective personal informatics (PI) involves capturing, tracking, analyzing, and reflecting on personal data to support emotional self-awareness and mental well-being. Recent advances in large language models (LLMs) are reshaping affective PI, yet a comprehensive survey of LLM-based affective PI systems is lacking. To bridge this gap, we systematically analyzed 45 papers published between January 2020 and June 2026 across four major computing and health databases, examining their macro trends, system taxonomies, and research methodologies. Our synthesis reveals an overreliance on multi-stage, text-centric pipelines, a predominance of active, screen-bound interactions, and a severe demographic skew toward young, university-campus-based cohorts in empirical evaluations. Based on these findings, we critically reflect on prevailing architectural and methodological shortcomings and outline actionable future directions for building end-to-end multimodal, low-burden, and inclusive affective PI systems.

---


### 231. [Designing Textual Interfaces To Enhance Llm Reasoning On Audio-Visual Question Answering](https://arxiv.org/abs/2610.20085)

**<font color=#1a73e8>作者：</font>** Yi Wang, Tianzi Wang, Tong Lei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic prompt optimization (APO) has shown strong effectiveness for text-based LLMs and LLM systems, but its application to audio-visual understanding systems requires suitable textual interfaces through which multimodal reasoning can be exposed to text-based optimizers. We investigate how the design of textual interfaces affects prompt optimization for multimodal reasoning, on the audio-visual question answering task. We compare three interface designs, including a direct inference system consisting of a single omni-modal large language model (OmniLLM), a captioner-reasoner system, and an agentic architecture in which a primary agent orchestrates subagent OmniLLMs. Experiments with Qwen3-Omni and Gemini show that direct prompt optimization provides model-dependent gains; the captioner-reasoner system and the agentic system expose more interpretable optimization interfaces but are harder to optimize, where error analysis of cases affected by optimization is conducted. Our study highlights textual interface design as an important factor in making prompt optimization effective for omni-modal reasoning systems. Our implementation details are specified in GitHub repo.

---


### 232. [AFCS: Atomic-Fact-Conditioned Synthesis for Factual Knowledge Pretraining](https://arxiv.org/abs/2610.20086)

**<font color=#1a73e8>作者：</font>** Yunhao Wang, Feng Zhang, Tinghao Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic data is increasingly used in language-model pretraining. Existing knowledge-corpus synthesis pipelines, including WRAP and Nemotron-CC, usually take a source passage or document segment as input and generate rewritten or QA-style samples from that text. This can improve surface form and prompt diversity, but it does not explicitly require fine-grained source facts -- especially secondary entities, list/table entries, and precise temporal attributes -- to appear in the synthesized corpus. We propose AFCS (Atomic-Fact-Conditioned Synthesis), a pipeline that first extracts source-supported atomic facts and then uses each retained fact to drive generation. AFCS uses structure-aware extraction over the document tree, source-grounded verification, local context expansion, and multi-format generation. In continued-pretraining experiments with OLMo-3-7B and a 32B base on the same FineWiki source corpus, AFCS outperforms WRAP and Nemotron-CC on SimpleQA, SimpleQA Verified, PopQA, and HotpotQA. Granularity ablations show that fact-level synthesis improves over chunk-level, paragraph-level, and entity-level synthesis; and a 100B-token mid-training integration improves factual benchmarks and raises the 12-task general benchmark average by +1.09.

---


### 233. [When Pairwise Preferences Cycle: A Reliability-Anchored Preference Walk for Video GRPO](https://arxiv.org/abs/2610.20089)

**<font color=#1a73e8>作者：</font>** Xinrui Lin, Fan Li, Shumin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pairwise preference feedback has become a widely adopted supervision signal for reinforcement learning in video generation models, as pairwise comparisons provide a more reliable alternative than pointwise scalar ratings for evaluating the quality of generated videos. Specifically, we define a preference graph for each GRPO group under a pairwise evaluator, where nodes represent sampled rollouts and edges encode pairwise preferences. Auditing 6,976 on-policy comparison graphs, we find that cyclic preferences are prevalent and persist throughout training. Naive pairwise reward aggregation based on average win rates discards the underlying comparison structures and treats each rollout independently, which may introduce unreliable advantage estimates for certain rollouts and consequently affect reinforcement learning optimization. Therefore, we propose the \emph{Reliability-Anchored Preference Walk} (\ours{}), a graph-aware advantage aggregation method that strengthens the global preference signal from win rates with reliable relational evidence from cyclic preference graphs through a reliability-guided preference walk. Under matched evaluator, comparison protocol, group size, prompt schedule, and query budget, \ours{} requires no additional evaluator queries beyond the observed comparisons within each rollout group and improves over Pairwise-GRPO across controlled comparisons, transfer settings, and blind human evaluations.

---


### 234. [EvalBuilder: Can LLMs Build Efficient Benchmarks?](https://arxiv.org/abs/2610.20099)

**<font color=#1a73e8>作者：</font>** Huaisheng Zhu, Hangfan Zhang, Teng Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly used for long-horizon research and engineering, yet evaluating these capabilities remains expensive, time-consuming, and heavily dependent on human expertise. This motivates a natural question: can LLM agents themselves construct efficient benchmarks that preserve the conclusions of costly reference evaluations? We study this capability by formulating automatic benchmark development as a meta-evaluation problem, where an agent is given a task and an expensive reference benchmark and requested to construct a lower-cost proxy benchmark that faithfully distinguishes among candidate models and solutions. Based on this formulation, we introduce EvalBuilder, a framework for evaluating such benchmark-generation capabilities along three key dimensions: fidelity, efficiency, and robustness. Specifically, we assess whether generated benchmarks preserve model rankings, generalize to held-out models and freshly collected responses, and provide well-calibrated and discriminative scores while substantially reducing evaluation cost. We further provide an iterative environment in which agents can refine their benchmarks under a fixed time budget. Our framework provides a systematic testbed and benchmark for understanding when current LLM agents can develop useful evaluators and how benchmark construction itself can be increasingly automated.

---


### 235. [What Do Foundation Models for Market Microstructure Learn? A Controlled Study with Synthetic Limit Order Books](https://arxiv.org/abs/2610.20104)

**<font color=#1a73e8>作者：</font>** Fernando Acero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive transformers trained on limit order book (LOB) message streams are increasingly proposed as foundation models for market microstructure. Because the generative process of real markets is unknown, these models can be judged only by the realism of their output, leaving open what they actually learn. We make the question answerable by inverting the setup: we train GPT-style models on order flow from simulators whose latent parameters are known, so that the Bayes-optimal predictor, the generating state, and the exact data entropy serve as references. Measured against them, next-token pretraining on order flow implements amortized Bayesian inference over market regimes. The learned predictive matches the exact Bayes optimum to within a millinat per token and approaches the oracle floor even on a nonstationary family whose latent state drifts within an episode, a regime that requires filtering. The latent regime is linearly decodable from frozen activations, well above baselines, so a frozen-model read-out calibrates simulator parameters more accurately than windowed maximum likelihood at a fraction of the cost. In our experiments these capabilities are not produced by scale: capacity and token volume saturate early, and it is the diversity of training regimes, not the token count, that determines generalization to unseen markets. On real NASDAQ data, zero-shot transfer is set by how well the simulator prior covers real flow: an enriched mixture nearly closes the gap to an in-domain baseline, and pretraining beats from-scratch training at every budget across held-out tickers. Known ground truth turns average next-token loss, which is uninformative near the entropy floor, into an exact comparison against the Bayes-optimal and oracle predictors.

---


### 236. [Why Generate a Click? Plug-in Decision Heads for Web Agents](https://arxiv.org/abs/2610.20107)

**<font color=#1a73e8>作者：</font>** Chengguang Gan, Yunhao Liang, Hanjun Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web agents built on vision language models decide every action by generating text such as click(12), although most of that text encodes a choice among a few action types and a few dozen marked elements. We read these choices directly from the hidden states that the generator computes while it reads the goal and the screenshot. Plug-in decision heads on a frozen generator predict the action type, pool the visual tokens inside each numbered box to pick the target, and point at a listed text option or at a WRITE slot that leaves the writing of new text to the generator. A confidence cascade executes the heads' action when they are sure and otherwise lets the generator decode from the KV cache of the same forward pass. With Qwen3-VL 4B and 8B generators trained on 213k web steps, a strict threshold keeps the cascade between 0.3 points below and 1.4 points above the generator on seven offline test sets while the heads decide 12 to 64% of the steps. A looser threshold raises step success on unseen Mind2Web websites by 3.1 and 1.8 points, costs up to 2 points on GUIAct and MiniWoB++, and lifts WebArena task success from 12.5 to 13.8% (4B) and from 13.6 to 14.6% (8B) with less than half of the generated tokens. Training the heads jointly with the generator lowers the generator's own step success by up to 4.9 points; heads on a frozen generator avoid this cost.

---


### 237. [Maximising Transparency in Context Compaction Improves Retention of Facts and Commitments for Lightweight Coding Agents](https://arxiv.org/abs/2610.20116)

**<font color=#1a73e8>作者：</font>** Felix Woolford  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long coding agent sessions outgrow the model's context window, so agents compact: older history is replaced by something shorter, usually a model-written summary. A summary selects and rewords, and the agent cannot see what was lost. Existing work has explored a range of compaction techniques, but comparatively little attention has been paid to their effectiveness with lightweight models, including those deployed locally or used for high-volume workloads. Here, we present transparent-compact, a simple deterministic method for the open-source Pi coding agent, designed specifically for use with such models and with the purpose of maximising the transparency of the agent's view of its own compacted context. It guarantees that user and assistant prose in its context is unchanged by a model or algorithm, and explicitly flags where compaction has stripped information. We compare it with Pi's default model-written summary compaction and with pi-vcc, a popular deterministic method with similar methods but without verbatim retention of prose. Our benchmarks run on four models of varying performance levels, with emphasis on Qwen3.8-27B: a lightweight model at the top end of what consumer hardware can serve locally. On sets probing commitments (rules the user set which exist only in the conversation) and recall of facts, transparent-compact matched or outperformed both alternatives. In particular, it showed an advantage in avoiding confident blunders, i.e. assertion of false information as opposed to recognizing that something was not recalled. Even with a frontier model, its advantage was present but smaller. We argue that transparent-compact spares lightweight models from reasoning or searching their way around what compaction lost, and results in improved recall and application of information as a result, without the need for task or context-specific structuring of the session history.

---


### 238. [Seeing at the Edge: Energy Characterization of Vision-Language Model Inference on Edge Platforms](https://arxiv.org/abs/2610.20136)

**<font color=#1a73e8>作者：</font>** Junlin Liao, Harshit Kondle, Di Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are moving onto edge devices, but little is known about how much energy they draw on single-board computers with NPU or GPU accelerators, or where that energy goes. We measure total-system energy, latency, and thermal behavior of Qwen2-VL-2B-Instruct and its text-only sibling on a Raspberry Pi 5 with a Hailo-10H NPU and on a Jetson Orin Nano Super, on both CPU and accelerator, and separate the fixed energy of each request from the energy that grows with output length. Because the accelerators use different quantization and serving software, we compare deployment stacks rather than silicon. Three findings stand out. First, NPU offloading makes the Pi a much more efficient VLM platform: it cuts energy per generated token by about two-thirds, leaves the host CPU largely free, and avoids the thermal throttling that the CPU backend reaches in sustained use. Second, an image adds both fixed and per-token energy, but at typical response lengths generating the answer costs far more than processing the image. Third, the Jetson GPU favors short responses through its lower fixed cost per request, whereas the Pi NPU favors longer ones through its lower cost per output token; their energy curves cross near 40 output tokens.

---


### 239. [Sparse Autoencoders for Mechanistic Interpretability in NLP: A Critical Survey of Recoverability, Interpretability, and Utility](https://arxiv.org/abs/2610.20139)

**<font color=#1a73e8>作者：</font>** Salima Lamsiyah, Adelaide Danilov, Oleksandr Marchenko Breneur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) have emerged as a promising approach to mechanistic interpretability by decomposing language-model activations into sparse, potentially interpretable features. However, differences in design assumptions, evaluation objectives, and experimental settings complicate conclusions about their effectiveness. We present a critical survey of 138 studies on SAEs in natural language processing. Our contributions are fourfold: (1) we propose a task-grounded taxonomy connecting dictionary design, feature operations, and NLP functions; (2) we examine how sparsity allocation, geometry, data coverage, and inference affect feature recoverability; (3) we assess evidence for semantic interpretability, mechanistic faithfulness, and behavioral utility; and (4) we synthesize findings across multilingual processing, retrieval, reasoning, classification, and behavioral regulation, highlighting the roles of objectives, baselines, supervision, and intervention pipelines. Through comparative analyses of published results, we reconcile apparent disagreements, identify unresolved questions, and propose directions for more rigorous evaluation. An anonymous research register this https URL accompanies the survey.

---


### 240. [LLM-Based Policy Compliance Verification of Loan Applications](https://arxiv.org/abs/2610.20155)

**<font color=#1a73e8>作者：</font>** Florentina Voboril  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Banks rely on extensive internal policy frameworks to ensure that corporate lending decisions comply with regulatory requirements and internal risk standards. Reviewing loan applications against these policies is a largely manual and knowledge-intensive process, which can lead to overlooked policy violations or exceptions. This report presents a prototype of an LLM-based policy checker that automatically verifies loan applications against internal lending policies.
The proposed approach follows a two-step architecture. First, compliance-relevant rules are automatically extracted from policy documents and converted into structured, machine-readable representations. Second, loan applications are evaluated against the extracted rules to identify policy exceptions, non-compliant findings, missing information, and cases requiring manual review.
Evaluation results demonstrate that the rule extraction process is highly stable across multiple runs and consistently captures rules identified as critical by a domain expert. When evaluated on 11 real loan applications with known policy exceptions, the system successfully detected the majority of these exceptions and identified additional compliance issues that had previously been overlooked during manual reviews. While the approach produces false positives and cannot fully replace human judgement, the results indicate that LLM-based policy compliance verification can provide valuable support in the loan application verification process by highlighting potential compliance risks.

---


### 241. [Gap Detection: Mitigating Homogenization through Demand and Defensibility](https://arxiv.org/abs/2610.20162)

**<font color=#1a73e8>作者：</font>** Xucheng Yu, Haibo Jin, Xiaoqi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models often produce semantically similar answers to open-ended questions, even when many plausible alternatives exist. Generating useful alternatives requires identifying both what the query calls for and what existing responses already cover. We introduce Gap Detection, a framework that searches for relevant but unoccupied directions in a shared text embedding space. Its objective, GapScore, combines query relevance (Demand) with dissimilarity to the nearest existing item (Defensibility). The framework optimizes this product on the unit sphere, maps candidate directions to concept words with a language model, and uses task-specific filtering and constrained prompting to turn those concepts into text. On five curated topics and 90 INFINITY-CHAT queries, the reported mean relative reductions in output Collision are 12.8% and 10.8%, respectively. We also instantiate the framework for generative engine optimization over four product markets and for iterative synthetic-data augmentation. In the latter setting, with 100 training examples per method, Gap Detection reduces Collision from 0.324 to 0.298 relative to undirected accumulation and increases the Vendi Score from 27.16 to 29.20; the accuracy difference is one example on a 40-example test set. Component ablations expose the trade-off between semantic separation and relevance, while also showing that better direction scores do not uniformly yield better downstream metrics. These results support explicit gap search as a practical mechanism for diversifying content, with task validity checked separately from geometric novelty.

---


### 242. [RM-OPD: On-Policy Distillation for Generative Reward Models](https://arxiv.org/abs/2610.20174)

**<font color=#1a73e8>作者：</font>** Qinglin Su, Licheng Pan, Zhen Fang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning on Mixed-domain preference data (Mix-RL) has become the mainstream approach for training general-purpose Generative Reward Models (GRMs). However, Mix-RL suffers from two critical bottlenecks: the reward sparsity induced by outcome rewards, and the cross-domain interference arising from jointly optimizing heterogeneous capabilities, which together give rise to imbalanced capability acquisition and pervasive reward hacking. Inspired by the success of On-Policy Distillation (OPD) in multi-domain capability integration, we introduce RM-OPD (Reward Modeling via On-Policy Distillation), a two-stage framework that separates specialist acquisition from capability integration. First, we cultivate domain-specialized teacher models via single-domain GRPO fine-tuning, allowing each expert to reach its performance ceiling in isolation; then we consolidate these teachers into one student model through (i) routed on-policy distillation, which provides dense signed token-level supervision on student-generated critiques; (ii) domain contribution reweighting, which reweights token guidance toward target domain shares, preventing specific domains from dominating optimization; and (iii) optional criteria context distillation, which conditions teachers on domain-specific evaluation criteria to sharpen token-level supervision. Across multiple RM benchmarks and two base models, RM-OPD consistently outperforms vanilla Mix-RL and other strong baselines, achieving overall superior performance and exhibiting an emergent "teacher-surpassing" effect. These results establish RM-OPD as a promising paradigm for building generalist GRMs.

---


### 243. [TreeSpark: Learning to Draft the Trees You Verify for Speculative Decoding](https://arxiv.org/abs/2610.20175)

**<font color=#1a73e8>作者：</font>** Jihao Zhao, Qianyu Jiang, Shuaishuai Zu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parallel drafters such as DFlash and DSpark reduce proposal latency, but early mismatches limit how much of each block can be accepted. Retaining alternatives introduces parent states and candidate choices that reference-conditioned training does not directly supervise. We introduce TreeSpark, a unified training and inference framework extending the semi-autoregressive DSpark architecture. It constructs parent-conditioned candidate trees from one backbone pass and replays their expansion, pruning, and budgeted packing during training. Survival negative log-likelihood weights retained edges by reference-derived path mass, while a capped coverage hinge promotes target-important alternatives near local selection boundaries. Both objectives reuse reference-chain target distributions without additional target forward passes. We evaluate greedy decoding with Qwen3-4B and Qwen3-8B on nine general benchmarks and six writing domains. Across targets and suites, TreeSpark improves mean acceptance length over DSpark by 23.4% to 31.6% and mean single-request throughput by 15.1% to 25.0%. Batched Qwen3-4B throughput improves by 12.6% to 17.2%. At fixed attention capacity and inference policy, the proposed supervision further improves mean acceptance length by approximately 6.4% and mean system throughput by 4.2% to 5.0% on Qwen3-4B.

---


### 244. [Cross-Model In-Context Neurofeedback Reveals (Limited) Activation Control in LLMs](https://arxiv.org/abs/2610.20179)

**<font color=#1a73e8>作者：</font>** Davide Baldelli, Robyn Kozierok, Mirko Bronzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Probes on activation vectors are widely used to detect misbehavior in language models, but their success relies on the assumption that models cannot control what their activations encode. Humans can learn, through neurofeedback, to control the firing of even single neurons, and recent studies investigated whether this ability extends to language models, reaching conflicting conclusions. No experimental design so far disentangles competence at the task from genuine access to one's own activations. We fill this gap with in-context neurofeedback sessions, in which a "subject" model is asked to maximize (or minimize) a score derived from its activations, shown back to it at every turn. In our first experiment, the sentences are generated either by the subject or by a second "writer" model, while the score always derives from the activations of the subject. We test ten open-weight models from five families, with sizes from 9B to 32B. Some models move their own scores considerably, but no more than a writer of comparable competence moves them. Is this because the task requires no privileged access, or because the subject controls its activations while processing the sentences, whoever wrote them? To answer this, we prefill a fixed sentence as the subject's reply at every turn and ask it to increase or decrease the score. Three out of ten models show small but consistent control effects. We further ask whether models can control their activations to the point of fooling an activation monitor. We make models repeat sentences a monitor would flag, such as a deceptive answer for a deception monitor, and ask them to raise or lower the monitor's score. No model learns to lower it, but one model can raise it. In-context control of a model's own activations might not yet be a threat to activation monitors, but it exists in a few models and needs to be tracked as models evolve.

---


### 245. [HEM-Med: A Hierarchical Agentic Memory Framework for Safe Multi-Center Medication Recommendation](https://arxiv.org/abs/2610.20191)

**<font color=#1a73e8>作者：</font>** Min Xiao, Jin Li, Shoujin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medication recommendation (MR) is critical for clinical decision support. While existing MR methods are mostly designed for single-center learning, where only one independent hospital is involved, multi-center MR with hospitals of different scales has become increasingly demanding in practice. In multi center settings, abundant data from large medical centers can improve recommendation performance for low-resource centers. Despite a few preliminary attempts on this task, two critical gaps remain. Gap 1: Existing multi-center methods fail to disentangle transferable cross-hospital clinical experience from hospital-specific prescribing patterns, limiting clinical feasibility and physician acceptance. Gap 2: They commonly overlook multi label safety constraints of MR, including drug-drug interaction risks and local formulary feasibility, which are essential for safe real-world deployment. To address these gaps, we propose HEM-Med, a novel hierarchical agentic memory framework for multi-center MR. To address Gap 1, we design a disentangled hierarchical memory module that builds patient-level medication context attribution records and disentangles them into cross hospital experience memory and hospital-specific residual memory. To address Gap 2, we introduce a safety-aware medication set generation module, which integrates dual-level experience retrieval with safety-aware set decoding to produce clinically relevant, safer, and locally adaptive medication recommendations. Experiments on a real-world multi-center eICU dataset show that HEM-Med outperforms representative transfer learning, LLM-based, and MR baselines in terms of both recommendation accuracy and safety.

---


### 246. [What Makes a Social Agent's Interactions Effective? Learning from Verifiable Outcomes in Paired Worlds](https://arxiv.org/abs/2610.20195)

**<font color=#1a73e8>作者：</font>** Caixin Kang, Ke Wang, Yuchuan Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective social interaction requires more than fluent responses: agents must reach plans that fit the participants' needs and circumstances. Existing evaluations of social agents mainly rely on LLM judges that rate the conversation, without checking the resulting plan. We introduce HICO-Bench, a benchmark of 180 everyday coordination scenarios, such as resource allocation, scheduling, and authorization, in which two agents with private information converse and then independently record the plan they agreed on. A program checks Feasibility (the two records match and satisfy both participants' private conditions), and an LLM judge checks Integrity (the conversation supports the recorded plan); passing both is a Verified Success. Each scenario has two versions that share the same public context but differ in one private condition, so the correct plan differs between them. Across thirteen LLMs, 36% of conversations rated highly for goal completion fail Verified Success. To learn from outcomes that arrive only at the end of a conversation, we propose Paired-Credit Policy Optimization (PaCPO). After each turn, PaCPO asks the agent for a tentative plan, checks it in both versions of the scenario, and rewards the turns after which the tentative plans fit their respective versions. PaCPO raises Qwen3-8B's Verified Success from 20.4% to 28.3%.

---


### 247. [Drivers of LLM Consensus Formation Under Competing Incentives: A Simulation Study](https://arxiv.org/abs/2610.20200)

**<font color=#1a73e8>作者：</font>** Isabel Jones, Matthew Edwards, Janina A. Hoffmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in multi-agent environments that produce unanimous agreement, both in intended interactions that need coordination and in unintended emergent interactions. Consequently, understanding how LLMs with competing incentives reach consensus is crucial to better interpret and design LLM collectives. We introduce an evaluation, based on the Network Consensus game, to assess the mechanisms driving this process. Here, a network of agents must agree on one of two colours to receive a payoff, but agents are offered different payoffs for the agreed colour. We vary components such as communication access and network structure and assess six open-source models and one closed model (ChatGPT 5.6-sol).
We find that open-source LLMs reach consensus less often than humans in comparable experiments and only if messages are communicated across the global network. ChatGPT 5.6-sol, however, is able to reach consensus with communication limited to its neighbours and with no communication ability. This is achieved through lower stubbornness and higher majority-following tendencies, and by providing more information about its neighbours' states in messages. However, situating agents in a highly clustered graph reduces consensus, regardless of these traits, demonstrating that both system design and individual model traits drive collective outcomes.

---


### 248. [Continual pretraining Prostate MRI ViT Encoder for task alignment](https://arxiv.org/abs/2610.20217)

**<font color=#1a73e8>作者：</font>** Bilal A. Sidiqi, Yipei Wang, Shaheer U. Saeed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building foundation models for MRI has emerged as a promising direction for advancing medical image analysis and improving accessibility of task specific models. Existing approaches primarily focus on effective pretraining strategies and evaluating their performance across diverse downstream tasks. While these methods show performance gains, limited attention has been given to understanding task alignment between pretraining and downstream objectives. Unlike language models, where the two stages are naturally aligned, such alignment is less evident in vision based applications. Motivated by this gap, we explore continual pretraining. Specifically, continually pretraining a pretrained ViT encoder using Low-Rank Adaptation (LoRA) on a prostate segmentation task to enhance task alignment and downstream performance. We further perform layer-wise representational analysis using Centered Kernel Alignment (CKA) to assess representational shifts and their correlation with task outcomes. Our experiments show improved performance in 3 of 6 downstream tasks and comparable results in the others. Our Feature analysis reveals that, for segmentation tasks, continually pretrained encoder features exhibit greater similarity to those of the finetuned encoder than the original pretrained encoder, correlating with observed performance gains.

---


### 249. [Scaling Multilingual Safety and Reasoning Evaluation through Reasoning-Guided Translation](https://arxiv.org/abs/2610.20221)

**<font color=#1a73e8>作者：</font>** Zahraa Al Sahili, Ioannis Patras, Matthew Purver  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed across languages, yet their safety and reasoning capabilities remain predominantly evaluated in English. Translating existing benchmarks offers a scalable approach to multilingual evaluation, but preserving task-specific meaning across languages presents significant challenges, particularly for harmful requests, mathematical reasoning, and conversational interactions. We introduce a reasoning-guided translation framework for constructing multilingual evaluations designed to preserve the structure and intended meaning of diverse benchmark tasks. Our approach separates translation strategy selection from large-scale generation, combining reasoning-guided configuration selection with task-aware validation, targeted repair, and independent quality screening. Using this framework, we develop a source-aligned evaluation collection spanning seven safety, conversational, and mathematical reasoning resources across 11 languages. The resulting collection achieves 99.94\% coverage of intended item--language pairs in the two subsets requiring repair. Evaluations of open-source LLMs reveal distinct language-dependent vulnerabilities, including inconsistent refusal behaviour and substantial reasoning degradation in lower-resource languages. These findings highlight the importance of task-sensitive benchmark construction and systematic quality assessment for understanding multilingual model behaviour beyond English.

---


### 250. [Let Me Clarify: Interactive Modeling of Soft Attributes](https://arxiv.org/abs/2610.20227)

**<font color=#1a73e8>作者：</font>** Steffen Holter, Rita Sevastjanova, Michaela Benk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People commonly express preferences through soft attributes such as is interesting,'' which are difficult to operationalize for computational preference modeling. Latent representations can obscure how such attributes are interpreted, limiting transparency and user control. We formalize softness as the diversity of valid interpretations a description permits and provide empirical support for this characterization. Our proposed measure estimates softness to guide clarification and determine when to generate computational approximations. This is instantiated in AttriFy, a mixed-initiative system that translates descriptions into executable Python functions over text corpora. An interactive dashboard connects the dialogue to proposed functions and computed values, enabling users to inspect, accept, reject, and refine interpretations. An exploratory within-subjects study with 32 participants compares our softness-guided clarification approach with an LLM baseline in supporting interpretable attribute construction. This work positions softness as a basis for constructing explicit, user-steerable attribute dimensions for downstream preference elicitation and decision-making.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-313](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
