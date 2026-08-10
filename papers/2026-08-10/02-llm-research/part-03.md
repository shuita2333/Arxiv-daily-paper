# 🧠 大模型相关研究 | 2026年08月10日

> 本类共 **170** 篇论文：已确认 **159** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-170](./part-04.md)

---

### 101. [ReQuant: Fixed-Grid Discrete Refinement for Post-Training Quantization](https://arxiv.org/abs/2608.07019)

**<font color=#1a73e8>作者：</font>** Yongge Ma, Guoan Wang, Feiyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is widely used to reduce the memory and computational cost of large language models. Existing PTQ methods typically obtain an initial quantized model through heuristic rules or greedy optimization, and once quantization is completed the resulting integer assignments are usually treated as final. This observation motivates a complementary optimization stage within PTQ that keeps quantized weights improvable after an executable quantized model has been produced, while preserving the quantized format. We introduce ReQuant, a backpropagation-free fixed-grid refinement procedure for this stage. Agnostic to the PTQ initializer, ReQuant takes an existing quantized model as a feasible starting point and iteratively revisits its discrete weight assignments on the fixed quantization grid. Accepted updates strictly reduce the mean squared reconstruction error and remain on the original grid. In this way, ReQuant turns the initially fixed PTQ output into an iteratively optimizable discrete solution and serves as a plug-and-play post-processing stage for existing PTQ pipelines. Experiments across diverse model families, bit-widths, and downstream tasks show that ReQuant consistently improves quantized models from heterogeneous PTQ initializers, with especially large gains on simple initializers and lower bit-widths. Notably, ReQuant can refine a simple round-to-nearest initialization across multiple sweeps until it approaches or surpasses GPTAQ under the same quantization format. These results establish ReQuant as a practical complementary stage for further improving existing PTQ pipelines.

---


### 102. [An Agentic Hybrid Top-Down and Bottom-Up Approach to Knowledge Graph Generation](https://arxiv.org/abs/2608.07023)

**<font color=#1a73e8>作者：</font>** Emma Jouffroy, Warren Jouanneau, Marc Palyart  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organizing thousands of unstandardized, multilingual expertise declarations is a persistent challenge for Human Resources (HR) platforms, directly impacting downstream tasks like accurate talent matching. To address this, we propose a hybrid knowledge graph generation pipeline that grounds a Large Language Model (LLM) in the Wikidata multilingual Knowledge Graph (KG) while employing an agentic reflexion pattern to synthesize emerging concepts and their associated metadata. Unlike rigid top-down methods or fragmented bottom-up approaches, our system anchors recognized concepts to stable Knowledge Graph entities while dynamically creating new nodes and relational metadata for unrecognized skills. Executed across five stages, entity reconciliation, multilingual canonicalization, active curation, deduplication, and the iterative recovery of unmapped concepts, the system autonomously adapts to rapidly evolving, noisy skill mentions across five European languages. Ultimately, this pipeline provides a highly scalable, explicable, and self-healing framework for generating a comprehensive skills knowledge graph, from which a structured taxonomy is derived, using unstructured, noisy text.

---


### 103. [Not All Problems Are Best Modeled as MILP: A DSL-Centric Framework for Flexible and Accurate Optimization Modeling](https://arxiv.org/abs/2608.07040)

**<font color=#1a73e8>作者：</font>** Shaofeng Zhang, Hongyuan Su, Qingwen Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Solving combinatorial optimization problems (COPs) requires not only efficient algorithms but also carefully crafted formulations. While recent works have leveraged LLMs to automate optimization modeling, current frameworks predominantly rely on a rigid mixed-integer linear programming (MILP) paradigm. In this paper, we argue that not all problems are best modeled as MILP, as forcing complex domains into linear constraints can induce prohibitive modeling complexity and severely restrict solver flexibility. To address this, we propose OptiDSL, a framework that shifts the focus from rigid MILP formulations to domain-specific language (DSL) representations. By utilizing LLMs to map natural language onto standardized, domain-accepted structures, OptiDSL decouples problem formulation from execution. This paradigm enables seamless integration with a diverse library of specialized solvers, ranging from traditional heuristics to modern learning-based methods. Experimental results on the comprehensive benchmark of 44 COP types show that OptiDSL significantly surpasses MILP-based pipelines, yielding a 51.66% gain in formulation accuracy and a 91.71% decrease in modeling time. Notably, it also outperforms MILP-based pipelines on the existing benchmark, achieving a 23.09% higher formulation accuracy. Our code is available at this https URL.

---


### 104. [YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family](https://arxiv.org/abs/2608.07051)

**<font color=#1a73e8>作者：</font>** Xu Lin, WenJie Nie, Jinlong Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generic parameter-efficient fine-tuning (PEFT) methods transferred from language models can fail silently on real-time detectors, whose heterogeneous operators and detection-specific components impose placement constraints absent from regular Transformer stacks. We propose YOLO-PEFT, a structure-aware framework that formulates adapter placement as an auditable constraint-planning problem. Given a detector graph, a PEFT request, and a resource budget, YOLO-PEFT assigns operator and semantic roles, evaluates explicit operator-validity, detector-semantic, graph-interface, and deployment predicates, records a reason code for each excluded module, and either emits a budgeted target-module plan or returns Refuse before training. Under the official VOC07+12 trainval-to-VOC07 test protocol, planner-selected RS-LoRA reaches 0.7138 and 0.7307 mAP50-95 on YOLO11s and YOLO12s, respectively, compared with 0.6428 and 0.6662 for Full-SFT. On RT-DETR-L, all seven evaluated LoRA-family configurations cross the predefined catastrophic threshold, supporting a calibrated Refuse-to-Full-SFT decision within the evaluated coverage. A controlled YOLO11 audit further shows that LoRA reduces peak training memory by 43.9 percent, although training takes 1.72 times longer. Within the evaluated detector families, placement policies, and calibration coverage, YOLO-PEFT replaces manual target-module trial and error with explicit, inspectable planning while preserving verified train-save-merge-export paths; refusal on unseen detector architectures remains an open validation problem. Project Page: this http URL

---


### 105. [BONSAI: Evolvability-Guided Tree Search over Skills](https://arxiv.org/abs/2608.07056)

**<font color=#1a73e8>作者：</font>** Yash Priya Shastri, Anand Eswaran, Adnan Qidwai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A skill is a naturallanguage document that steers a frozen agent whose weights cannot be updated so any capability the agent lacks must be supplied in prose Optimising a skill is therefore optimising text against a score and the standard recipe which keeps any edit that raises a heldout score is blind in a specific way a single score cannot tell a document perched on a narrow overfit spike from one resting on a broad plateau even though only the second can still be improved We introduce BONSAI a novel skilloptimisation framework that steers instead by evolvability the capacity of a region of documentspace to keep producing viable variation under further mutation a property biology treats as separate from present fitness BONSAI grows skills as a MonteCarlo search tree in which every child document is a mutation of its parent and descends it under an upperconfidence selection rule whose exploitation term blends a skills own fitness with the fitness of its mutational neighbourhood Because every child is a mutation the mean score recorded beneath a node estimates that neighbourhoods evolvability at no extra cost so the rule concentrates budget on regions that keep improving while its exploration term keeps a currently weak branch in contention BONSAI ships the single bestscoring document it finds at no cost beyond the acceptifbetter loop it replaces With a frozen 30B agent and averaged over three benchmarks BONSAI lifts heldout accuracy over the skillfree agent by 2313 points and improves on two budgetmatched baselines GEPA and SkillOpt by 387 and 397 points respectively

---


### 106. [MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents](https://arxiv.org/abs/2608.07068)

**<font color=#1a73e8>作者：</font>** Zhiyuan Liu, Tinghong Ye, Chenghao Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents accumulate growing contexts during interaction, impairing performance and stability. Compact memory mitigates this problem by compressing and rewriting the history retained between model invocations. Learning what to retain typically relies on proximal policy optimization (PPO) with final task rewards, but sparse rewards provide little guidance for individual memory updates. This limitation motivates on-policy distillation (OPD), which supplies dense teacher supervision on student rollouts. For such supervision to be valid, the teacher must evaluate each sampled action under the same state in which it was generated. However, the context rewriting performed during memory compression can break this alignment. When sampled responses are retained and re-encoded for later invocations, flattening the interaction into a persistent history may cause the teacher to score the action under a state that the student never visited during rollout. The action therefore remains on-policy by provenance, but not necessarily by state. We therefore propose Memory-Aligned On-Policy Distillation (MemOPD). MemOPD records the inputs and sampled outputs of each model invocation, restores its original token positions and causal visibility, and packs the reconstructed invocations for efficient teacher scoring. The teacher provides full-vocabulary supervision at the sampled action positions, while PPO preserves the final task objective. Experiments verify state alignment across several context updates and show that it improves F1 by 7.0% over persistent-history teacher scoring in a matched control. Overall, MemOPD-3B improves F1 over PPO by up to 416.2%, while packing yields up to a 1.63x speedup in actor computation during training. The code for this work is publicly available at: this https URL.

---


### 107. [Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking](https://arxiv.org/abs/2608.07077)

**<font color=#1a73e8>作者：</font>** Devin Pereira, Willem Zuidema  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Tower of Hanoi is a simple planning puzzle that in prior work has proven challenging for large reasoning models (LRMs). Current models solve the standard formulation of the puzzle, but still struggle with the flat-to-flat variant (where initial and goal states are not restricted to have all rings on a single peg). This paper presents an in-depth study of how both small, in-house Transformers and large, third-party LRMs solve this task. To understand the failures mechanistically, we first train small Transformers from scratch on precomputed solution traces. Using a variety of interpretability techniques, we show that these Transformers develop an emergent world model: a linearly decodable, geometrically faithful representation of the puzzle's state space (the Sierpinski triangle), that is causally involved in solving the puzzles. Second, we return to the large LLMs and apply our techniques to two frontier reasoning models, Qwen3.6-27B and DeepSeek-R1-Distill-Qwen-32B, that attempt to solve the task through extended chain-of-thought. Surprisingly, we find that both models encode the Sierpinski world model near-perfectly at the end of the prompt, and yet fail at the majority of tasks when there are more than 3 rings. We locate the source of this failure in the decaying representation of the world model. We probe for the representation at different stages during planning, and establish causality by showing that performance can be improved by injecting the prompt-time representation at inference. The failure of the models is thus one of maintenance of the required representations, not their absence, and performance is at least partially recoverable. These results thus reframe the reported collapse in performance from prior work: current Large Reasoning Models build a world model, and then lose it.

---


### 108. [RoRA: Role-Oriented Regional Allocation for Visual Token Pruning in MLLMs](https://arxiv.org/abs/2608.07088)

**<font color=#1a73e8>作者：</font>** Qiyanhui Lu, Han Wu, Rongjian Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) encode images as long visual token sequences, making prefilling and KV-cache storage expensive. Existing training-free pruning methods select tokens by importance, diversity, or spatial coverage, but treat retained tokens as interchangeable and do not explicitly track which object-related regions are already covered. We present RoRA, a training-free framework that casts visual token pruning as role-oriented regional evidence allocation. Given a fixed budget, RoRA partitions tokens into a protected semantic core, complementary context, and fine-grained detail. It first calibrates text-conditioned attention with a positional prior and a prompt-calibrated object prior, then builds Attention-Anchored Regions (AARs) from high-confidence anchors as lightweight proxies for covered object support. Context is explored mainly outside AARs, while a small AAR-guided budget restores local detail; pairwise similarity is used only for context-stage redundancy filtering. Under matched budgets, RoRA consistently outperforms strong training-free baselines across LLaVA and Qwen-VL families, retaining most of the unpruned accuracy even at aggressive pruning ratios, e.g., 96.5% of full performance at 88.9% pruning on LLaVA-1.5, and improving over D2Pruner by about 5% on Qwen3-VL at 75-90% pruning. At a 66.7% pruning ratio, RoRA requires only 0.7 ms for token selection and reduces end-to-end inference time by 24.6%, corresponding to a 1.33x speedup over unpruned inference on an NVIDIA H800.

---


### 109. [Human-Centered Explainable AI for TinyML Edge Devices: A Pareto-Based Selection Framework with LLM-Guided Design](https://arxiv.org/abs/2608.07091)

**<font color=#1a73e8>作者：</font>** Zeinab Dehghani, Dhavalkumar Thakker, Koorosh Aslansefat 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Edge Artificial Intelligence (Edge AI) enables the deployment of AI models directly on local edge devices, while such deployments are subject to strict resource constraints, particularly in clinical applications requiring local and timely inference. In such contexts, explainable artificial intelligence (XAI) can serve as a human-AI interface intended to support healthcare professionals' and patients' understanding of model predictions and informed decision-making. To fulfill this role, XAI method selection for TinyML deployments can be formulated as a human-centered multi-objective design problem that jointly considers qualitative stakeholder preferences, explanation quality, and proxy-based deployment cost. We propose a framework that integrates a large language model (LLM)-guided design interface that maps qualitative stakeholder preferences to candidate XAI methods, followed by deterministic feasibility filtering and Pareto-based optimization. The framework exposes trade-offs among explanation fidelity, stability, and proxy-based deployment cost while characterizing their implications for explanation quality and estimated deployment feasibility. A proof-of-concept evaluation on a skin lesion classification task illustrates how the framework systematically compares candidate XAI methods and identifies Pareto-efficient trade-offs. The present evaluation covers the computational selection stages, while physical MCU deployment and empirical human-expert validation remain outside the scope of this study.

---


### 110. [UncertaintyVis: Preserving Linguistic Uncertainty in Automated Text-to-Chart Generation](https://arxiv.org/abs/2608.07093)

**<font color=#1a73e8>作者：</font>** Songheng Zhang, Emily Aurelia, Anthony Tang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data-rich documents pair narrative text with quantitative claims, and authors routinely qualify those claims with linguistic uncertainty markers such as "nearly," "approximately," or "at least." Automated text-to-chart systems discard these markers, producing visualizations that appear definitive even when the source text expresses hedged or incomplete knowledge. Readers may then over-interpret precision and misjudge author intent. We present UncertaintyVis, a system that preserves linguistic uncertainty during automated chart generation. A formative corpus analysis of 211 uncertainty expressions across 12 documents and 8 domains yielded a four-category taxonomy: Surface Form Normalization, Precision Boundaries, Inferential Derivation, and Non-Inferable Gaps. We mapped each category to chart-specific visual encodings that signal uncertainty without disturbing the spatial integrity readers rely on, and implemented an end-to-end pipeline pairing large language model text analysis with uncertainty-aware rendering. In a two-part study with 12 participants, readers matched charts to source text with 85% accuracy and text to charts with 76%. Uncertainty-aware visualizations trended toward lower cognitive demand (effect sizes 0.460 and 0.769 for mental demand and effort), and 75% of participants preferred them to plain text, describing explicit uncertainty encodings as a basis for verifying data claims. Encoding effectiveness varied by chart type: bar and pie encodings performed consistently, while line chart encodings require redesign.

---


### 111. [MemWM: Memory-Augmented Text-Based World Model](https://arxiv.org/abs/2608.07107)

**<font color=#1a73e8>作者：</font>** Yujun Wang, Tao Zhang, Jinhe Bi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are increasingly used to support planning in agents by predicting how environment states evolve in response to agent actions. Yet fluent next-state predictions can still omit task-critical facts, corrupt product attributes, or apply incorrect transition rules. To address such systematic prediction errors, we introduce MemWM, a memory-augmented text-based world model. MemWM uses world memory, a curated memory bank of transition rules, state caches, and hard-to-predict facts, to condition next-state imagination. We evaluate factual state preservation with Structured State Fidelity (SSF), which scores predicted states through benchmark-specific facts and fields. Compared with SFT, memory-augmented training improves SSF by up to 206.3%. In the full planning setting, we keep the policy model frozen and provide policy-side world skill: retrieved task-level skills and step-wise corrective guidance for action selection. Across ALFWorld, WebShop, and ScienceWorld, memory-augmented agents improve downstream success over an SFT-trained world-model agent, with up to a 65.4% relative gain. Sensitivity analyses further show that retrieved memory improves task success and efficiency under different memory and action-budget settings.

---


### 112. [Modular TTT: Rethinking Test-Time Training as Composable Modules](https://arxiv.org/abs/2608.07110)

**<font color=#1a73e8>作者：</font>** Bohao Tang, Zhen Qin, Yuqi Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time training (TTT) views sequence modeling as an online learning problem in which fast weights are updated by an internal learning rule. Despite the growing number of TTT variants, existing approaches typically hard-code each variant separately, which makes it difficult to design new TTT methods and to isolate the role of each component. To address this, we propose Modular TTT, a framework that represents the inner learner as a directed acyclic graph and exposes the fast-weight network, loss function, learning rate, weight decay, and normalization as explicit design dimensions. Modular TTT automatically composes primitive-level train-view forward, train-view backward, and causal query-view rules into the full graph-level TTT computation, including the fast-weight state transition. Using Modular TTT, we systematically ablate the components of TTT and find that small learning-rate initialization, weight decay, and a single-layer nonlinearity improve performance, while MSE and inner-product losses perform similarly. Deeper fast-weight networks and normalization tend to hurt performance because they induce excessively large activations, while residual connections and gating provide little measurable benefit. Guided by these findings, we train the best resulting variant as 410M- and 1.45B-parameter models on 100B tokens, and observe training loss and benchmark performance comparable to Gated DeltaNet.

---


### 113. [Beyond Fluency: A Clinical Benchmark and Anomaly-Enhanced Baseline for Spine MRI Report Generation](https://arxiv.org/abs/2608.07117)

**<font color=#1a73e8>作者：</font>** Bruno Palau, Franziska Vogt, Daria Laslo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology reporting is time-consuming and subject to inter-rater variability, making automated report generation an attractive clinical application for Vision-Language Models (VLMs). We benchmark state-of-the-art VLMs on lumbar spine MRI with a focus on diagnostic accuracy and demonstrate that standard lexical and semantic metrics poorly reflect clinical correctness: fluent, well-structured reports can score highly while containing clinically meaningful diagnostic errors. To address this failure mode, we propose an architecture-agnostic framework that augments VLM inputs with spatially localized, disc-level anomaly heatmaps generated by a semi-supervised U-Net++ model. These heatmaps both improve anatomical sensitivity through explicit visual grounding and provide an independent interpretability output for clinical oversight, moving us closer to diagnostically reliable, visually grounded VLMs for lumbar spine MRI interpretation.

---


### 114. [How Much, Then Where: Credit-Conserving Action-to-Token Allocation for Multi-Turn Agent Reinforcement Learning](https://arxiv.org/abs/2608.07118)

**<font color=#1a73e8>作者：</font>** Lichao Ma, Yang Sun, Shuaitao Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Credit assignment in multi-turn agent reinforcement learning operates at two levels: assigning trajectory-level credit to actions and distributing each action's credit across its tokens. In this paper, we introduce FACTOR, which separates these decisions. FACTOR uses checkpoint-calibrated TD residuals to assign per-action credits that telescope to the trajectory advantage, and feedback-conditioned teacher-student likelihood gaps to allocate each credit across the realized action tokens. Per-action normalization preserves the action-average coefficient and prevents token-level sign flips. We pair this construction with an action-mean reduction, removing the implicit dependence of an action's scalar surrogate weight on its token length. At the behavior policy and before clipping, each action's inner action-mean surrogate equals its TD credit. FACTOR consistently improves over competitive baselines across ALFWorld, WebShop, and ScienceWorld, with every environment-seed comparison favoring FACTOR and the largest gains emerging on the longest-horizon environment. The same hyperparameters transfer without retuning to a larger backbone and to a different model family. Ablations identify TD action credit as the dominant driver of the improvement, with hindsight token allocation contributing complementary gains.

---


### 115. [PHOENIX: Fine-Tuned SLM-Powered Autonomous Satellite Lifetime Extension via Predictive Self-Healing and Multi-Agent AI Recovery](https://arxiv.org/abs/2608.07126)

**<font color=#1a73e8>作者：</font>** Sumaiya Islam, Harsha Kumara Moraliyage  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Most CubeSats, small and low-cost satellites roughly the size of a shoebox, do not survive as long as they were designed to: a study of 178 missions found that only 48-65% remain operational after two years, against a designed lifetime of 2-5 years. The deeper issue is that a CubeSat in low Earth orbit (LEO) is physically unreachable from the ground for roughly 85 minutes out of every 96-minute orbit, so faults that start during that window go unnoticed until the next contact pass, by which point recovery may no longer be possible. We propose PHOENIX (Predictive Health On-orbit Edge Neural Intelligence eXtension) to give the satellite its own fault reasoning capability. A fine-tuned Small Language Model (SLM) compact enough to run on embedded hardware is deployed onboard the CubeSat, running on the flight-proven Aethero NxN-ECM computer, monitoring all sensor readings continuously, and resolving recurring faults using a memory system that stores past repairs so the same inference does not need to run twice. Once per orbit it sends a short structured health report to the ground instead of a raw data dump; six specialized AI agents on the ground read that report and generate validated satellite commands within the 5-10 minute contact window. A generative diffusion model (DDPM) creates synthetic training data because real fault examples make up only 0.57-1.80% of the dataset. We report preliminary results on the ESA Anomaly Detection Benchmark (14 years, 76 channels, 118 labeled faults).

---


### 116. [Human-AI Perceptual Alignment by Playing Hues and Cues](https://arxiv.org/abs/2608.07141)

**<font color=#1a73e8>作者：</font>** Nuria Alabau-Bosque, Jorge Vila-Tomás, Paula Daudén-Oliver 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating the perceptual alignment between Contrastive Vision-Language Models (CVLMs) and humans is typically constrained by traditional benchmarks that overlook fine-grained semantic and cultural nuances. In this work, we propose a novel evaluation framework that leverages the gamified, discrete color space of the board game Hues and Cues. By mapping the board's 480 color cells to the CIE xy chromaticity diagram, we calculate empirical perceptual distances across a carefully curated 100-word vocabulary spanning seven semantic categories. To properly contextualize model performance, we establish an empirical lower bound of expected error-the Human Consistency baseline-calculated via Leave-One-Out (LOO) cross-validation on a dense dataset of color associations collected from 325 human observers through a custom digital interface. We evaluate 162 models across multiple architectural families and pre-training datasets to assess their semantic color grounding. Our results demonstrate that while CVLMs successfully replicate human cognitive biases, such as idealized memory colors for concrete physical referents (e.g., food and plants), they systematically diverge from the human baseline in abstract, subjective, and pop-culture domains. We identify two distinct failure modes in severely misaligned concepts: semantic misclassification and a systematic uncertainty collapse into a default blue coordinate. Furthermore, we reveal that highly curated pre-training datasets are significantly more effective than massive, uncurated corpora in mitigating these severe misalignments. Ultimately, this work highlights that despite their broad categorization capabilities, current CVLMs still fail to capture the nuanced, localized consensus of human color memory, emphasizing the value of gamified tasks in exposing underlying model biases. The data and code are publicly available to test other metrics.

---


### 117. [DiDPO: Diff-in-Diff Policy Optimization for Coding Agent Training](https://arxiv.org/abs/2608.07147)

**<font color=#1a73e8>作者：</font>** Xucong Wang, Zhe Zhao, Liheng Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with Verifiable Reward (RLVR) has emerged as a powerful paradigm for training coding agents, where the execution feedback from compilation and tests provides objective verification. However, unlike agent tasks, coding agents face a unique and finer-grained credit assignment challenge: at each step, coding actions simultaneously pack varying changes into different regions of a code version, which makes the contribution of independent change indistinguishable. Existing RLVR methods mostly leverage the outcome reward or step-level reward, which fails to dive into a code diff and makes unique properties of coding actions invisible to training. In this paper, we propose Diff-in-Diff Policy Optimization (DiDPO), a critic-free RL method that constructs fine-grained credit units directly from the structure of code diffs. DiDPO organizes multi-turn coding interactions into multiple thought--action steps and discovers code diffs across sampled trajectories. It then selects anchors by aggregating highly similar sub-diffs split from each whole diff by our ``groupability score'', which provides the splitting schema that optimally balances the semantic scope of anchors and the group mass they may form. Finally these anchors form advantage groups and project the diff-level advantage back to individual response tokens. Experiments on long-horizon coding and reasoning benchmarks show that DiDPO significantly outperforms strong agentic RL baselines. On Qwen2.5-7B-Coder, DiDPO exceeds comparable methods by over 10\% and narrows the gap with far larger models, offering a principled framework for fine-grained credit assignment in coding agent training. We also open-source verl-code, an agentic rl codebase that supports various RL methods and coding benchmarks.

---


### 118. [A MARL Centered Reference Architecture for Large Language Model Augmentation in Smart Manufacturing](https://arxiv.org/abs/2608.07148)

**<font color=#1a73e8>作者：</font>** Fouad Bahrpeyma, Dirk Reichelt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern manufacturing imposes six coupled demands on adaptive control: local decisions with global consequences, partial observability, nonstationarity, reflex speed response with long horizon effects, delayed and diffuse outcomes, and dynamics that resist explicit modeling. Cooperative multiagent reinforcement learning (MARL), posed as a Dec-POMDP under centralized training with decentralized execution, is a particularly natural formalism for these demands. This paper adopts a MARL centered scope and asks where large language models (LLMs) should augment, interface with, train, or, in the strongest competitive case, replace that coordination core. A taxonomy organizes the literature through four LLM attachment points: policy, reward design, communication between agents, and hierarchical planning. A conditional capability profile separates native mechanism, reported performance, formal guarantee, and engineering maturity, and a deployment readiness analysis identifies the evidence behind each role. These stages yield the principal contribution: a three layer MARL centered reference architecture, grounded in evidence, for semantic reasoning, adaptive cooperative control, and independently assured execution. The LLM-Augmented Dec-POMDP is a descriptive comparative notation for that architecture, recording four attachment choices without introducing a new decision process class or algorithm. Under the reviewed evidence, conventional MARL is better suited to frequent, structured, decentralized coordination after task specific training, whereas LLM components are promising for semantic interpretation, reward drafting, human interaction, and slower supervisory planning. Current LLM only manufacturing controllers do not yet establish equivalence for strict real time, decentralized, safety critical control; this conclusion is bounded by the available evidence and does not assert impossibility.

---


### 119. [Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](https://arxiv.org/abs/2608.07169)

**<font color=#1a73e8>作者：</font>** Taeil Kim, Kangsan Kim, Sung Ju Hwang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own. We propose Agent Memory Distillation (AMD), a training-free framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory. AMD constructs three complementary memory types from successful teacher trajectories: Workflow memory encodes task-level strategies, Subtask memory provides concrete behavioral examples at an intermediate granularity, and Function memory captures per-function calling conventions and common pitfalls. Workflow and Subtask memories are injected proactively at the start of each task, while Function memory is retrieved reactively upon tool-calling errors. We evaluate AMD on three tool-use benchmarks using four student models (4B-8B parameters) with GPT-5-mini as the teacher, achieving average accuracy gains of 27.2%p, 11.2%p, and 3.4%p on AppWorld, BFCL V3, and ToolSandbox, while consistently outperforming existing memory-based baselines. Further analysis shows that Subtask memory contributes the largest gains, teacher effectiveness depends on both teacher capability and student compatibility, and 4B-sized students benefit most from AMD.

---


### 120. [An AI4AI Framework for Visual Token Pruning](https://arxiv.org/abs/2608.07193)

**<font color=#1a73e8>作者：</font>** Zhen Liu, Wenli Huang, Wei Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual-token pruning can substantially reduce the inference cost of multimodal large language models (MLLMs), yet existing methods largely rely on fixed, handcrafted heuristics and costly expert trial and error. As pruning objectives, budgets, and model architectures diversify, manually navigating the expanding design space becomes increasingly difficult. This paper aims to build an AI4AI framework for visual-token pruning by addressing a natural question: Can large language models automatically design effective visual-token reduction algorithms? Although LLMs possess broad algorithmic knowledge and strong reasoning capabilities, translating such general knowledge into effective solutions for a specialized task remains nontrivial. We argue that the key lies in designing an appropriate search-state representation that connects the internal knowledge of LLMs with the structural requirements and constraints of visual-token pruning. Based on this insight, we propose AutoPrune, a training-free framework for LLM-driven visual-token pruning policy design. At its core, AutoPrune introduces a Token Pruning Domain-Specific Language (TPDSL) comprising 131 reusable atoms for budget control, token scoring, selection constraints, and token reassembly. A key property of TPDSL is that it represents each search state as a residual modification of a strong base policy. This residual formulation narrows the search space and directs the LLM's attention toward the policy components that are most consequential for performance. Experiments on 14 multimodal benchmarks and three MLLM backbones demonstrate the effectiveness, efficiency, and transferability of AutoPrune. Even when removing 94.4% of visual tokens, AutoPrune preserves more than 99% of full-token performance while reducing FLOPs by 9.9x and prefill latency by 6.4x.

---


### 121. [EMAS: Stabilizing Multi-Agent System Evolution through Evidence-Guided Revision](https://arxiv.org/abs/2608.07196)

**<font color=#1a73e8>作者：</font>** Chao Fei, Qingyi Si, Kaihua Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many methods for automated multi-agent system design optimize prompts and topologies during an initial design stage and then deploy the resulting system unchanged on subsequent samples. Experience from these samples is rarely consolidated into reusable system updates, while accuracy-oriented designs may incur high token costs. We introduce EMAS (Evolving Multi-Agent System), which uses this experience to revise MAS topology and prompts without updating LLM parameters, either to improve accuracy or to reduce cost. EMAS converts traces into structured diagnoses that specify a revision operation and target. It generates a candidate revision only when the same diagnosis recurs across samples and applies it only if paired validation against the current MAS meets the corresponding acceptance criterion. Across four benchmarks and two LLMs, EMAS attains the highest task-weighted overall accuracy for both backbones and is best or tied in six of eight model--benchmark settings. Within two evolution epochs, EMAS achieves relative gains of 6.30% and 20.10% in task-weighted accuracy on Kimi-K2-6 and Qwen3.6-27B, respectively. On MBPP with Qwen3.6-27B, EMAS raises accuracy from 55.09% to 89.12% while reducing token use per task by 62.2%. These results show that EMAS can turn experience from new samples into reusable updates to MAS topology and prompts.

---


### 122. [Authoring and Management of Transparent Research Integrity Assessments of Randomised Clinical Trial Publications Using LLM-assisted Tools and Provenance Knowledge Graphs](https://arxiv.org/abs/2608.07202)

**<font color=#1a73e8>作者：</font>** Milan Markovic, Goutham Indukuri, Somayajulu Sripada 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systematic reviews of Randomised Controlled Trials (RCTs) are routinely used as evidence for clinical care guidelines. Such evidence has to meet high research integrity standards to prevent low quality or false research outputs influencing the clinical care. However, assessing research integrity of published RCTs is a complex process requiring manual effort, and potentially resulting in diverse opinions of the human assessors. This paper describes INSPECT-AI, an LLM-based interactive tool that assists human reviewers with research integrity assessments of published RCTs based on the community approved INSPECT-SR framework, and the Research Integrity Provenance and Evidence ontology (RIPE-O) for documenting the provenance of the assessment process. In addition, we present the Research Integrity Provenance and Evidence knowledge graph (RIPE-KG), an initial set of 140 expert research integrity assessments of 95 RCT publications generated by INSPECT-AI and described using RIPE-O.

---


### 123. [Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes](https://arxiv.org/abs/2608.07208)

**<font color=#1a73e8>作者：</font>** Luc Hazenoot, Zhaochun Ren, Amirhossein Zohrehvand  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing measures of how much a text is about a concept read the surface of the text: dictionary word shares, topic proportions, embedding similarities. They score the words a text uses, not the judgment a reader forms about it. Recent work has shown that a gap exists in what Large Language Models (LLMs) know internally versus what they express in their response. This paper asks whether that internal knowledge, read by monitoring the activations of frozen, out-of-the-box LLMs, can stand in for task-specific fine-tuning when measuring concept content, and which extraction method reads it best. We extract such measures via the Recursive Feature Machine (RFM) algorithm and via linear probing, and compare these against an embedding baseline, surface baselines, and the same model's own answer to the question. We demonstrate the approach on financial text, a domain studied extensively and served by established annotated resources, using a human-annotated Environmental, Social and Governance (ESG) dataset. The best linear probe comes within 0.6 percentage points of a fine-tuned domain classifier's accuracy without any task-specific fine-tuning, and outscores the same model's own answer to the question in eleven of twelve comparisons, so the activations carry concept content the response does not report. The simple probe consistently beats the RFM concept vectors, which in turn provide what classification alone does not: a continuous score intended to reflect how strongly a concept is present in a text, whose validation awaits graded labels.

---


### 124. [From Test-Time Scaling to Reusable Memory: Measuring Crystallization in Text-to-SQL](https://arxiv.org/abs/2608.07213)

**<font color=#1a73e8>作者：</font>** Jiaqian Wang, Yutao Qi, Wenjin Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling can correct difficult text-to-SQL queries, but the extra computation is normally discarded after each answer. Systems increasingly retain verified repair episodes, yet evaluations still report one end-to-end score. It cannot distinguish replay on recurring questions from help on unseen questions, or identify the responsible memory choice. We call measuring this future value the crystallization problem. Our controlled evaluation holds the single-shot solver fixed and varies one memory choice at a time. We separately measure replay, cross-question retention, and held-out same-database transfer. On BIRD, storing verified corrected queries improves held-out first-attempt accuracy by 4.34 percentage points. This gain captures 44.4% of the accuracy headroom provided by on-demand repair on the same questions. Controlled interventions identify database-specific content as the main operating ingredient. Reliable verification and broader retrieval coverage yield supported gains; richer formats and elaborate retrievers do not. Open-source code, evaluation artifacts, and reproduction instructions are available at this https URL.

---


### 125. [Skaling: Chinchilla's Exponents Meet Kaplan's Coupling](https://arxiv.org/abs/2608.07222)

**<font color=#1a73e8>作者：</font>** Mathurin Videau, Badr Youbi-Idrissi, David Lopez-Paz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural scaling laws are foundational for language model development, yet standard formulations systematically under- and overestimate loss at data-scarce and overtraining extremes. This failure originates in the underlying assumption that model size and training data impact the loss independently. To address this, we introduce the Skaling law, a generalized functional form that couples model capacity and data through a single interaction exponent. This simple extension reduces the Mean Absolute Percentage Error (MAPE) by 1.5-3x across both interpolation and extrapolation regimes. When paired with a sparse grid strategy restricted to low-compute regimes, the Skaling law achieves accurate full-grid extrapolation using approximately 10x less compute than uniform sweeps. By enabling reliable performance prediction from small-scale experiments, the Skaling law provides a more robust and resource-efficient framework for allocating compute budgets in next-generation model training.

---


### 126. [Stochastic Autoregressive Learning](https://arxiv.org/abs/2608.07224)

**<font color=#1a73e8>作者：</font>** Ilan Doron-Arad, Idan Mehalel, Elchanan Mossel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by LLMs, which generate outputs by iteratively sampling from next-token distributions, we introduce a PAC-learning model for binary stochastic autoregressive learning. This generalizes the deterministic autoregressive learning framework of Joshi et al., COLT 2025. In our model, one fixed generator assigns a Bernoulli next-token distribution to every prompt string. Starting from an input prompt, a token is sampled and appended to the prompt; the same generator is then applied again to this expanded prompt; this procedure is repeated for $M$ steps. Three forms of supervision are considered: base one-step samples, chain-of-thought (CoT) samples that reveal full random trajectories of length $M$, and end-to-end (e2e) samples that reveal only the final token of length $M$ trajectories. For a generator class, we study the minimum number of samples $m_{base}(\varepsilon),m_{CoT}(\varepsilon), m_{e2e}(\varepsilon)$, resp., required to learn the one-step probabilities in the base model, and the final-token probability in the CoT and e2e models, under squared loss error~$\varepsilon$.
We show that stochastic autoregressive learning fundamentally differs from the deterministic theory. At scale $\varepsilon$, there is no universal comparison between the three learning tasks: both $m_{CoT}/m_{base}$ and $m_{e2e}/m_{CoT}$ can be made simultaneously arbitrarily larger than $M/\varepsilon$, the natural analogue for the existing deterministic results. Nevertheless, after altering scales, for every class, CoT learning at scale $\varepsilon$ is upper-bounded by base learning at scale $\varepsilon/M^2$, whereas e2e learning at scale $\varepsilon$ is upper-bounded, up to logarithmic factors, by $(M/\varepsilon) m_{CoT}(\Theta(\varepsilon))$. These dependencies and scales are essentially tight. We complement these bounds by studying dimension $d$ logistic functions in our model.

---


### 127. [Recipes for Creativity: Iterative Generation and Evaluation in Large Language Models](https://arxiv.org/abs/2608.07243)

**<font color=#1a73e8>作者：</font>** Rens Anderson, Tessa Verhoef, Amirhossein Zohrehvand  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models are often evaluated through singular artifacts, whereas human creativity typically emerges through iterative generation, appraisal, and refinement. This pilot study examines whether iterative search improves LLM creativity by adapting FunSearch to recipe generation for the 2024 Pillsbury Bake-Off and evaluating outputs against human benchmarks using TTCT-based LLM evaluation. Across two experiments, we test iteration count, generator temperature, and in-loop selection-scorer model size. Results show that iterative generation-selection can produce recipes with creativity scores comparable to human benchmarks, but additional iterations alone do not improve creativity. The in-loop evaluator matters most: a smaller selection scorer yields significantly higher scores across most TTCT dimensions, while temperature has limited effects except for originality. These findings suggest that evaluator design is a first-order design variable in subjective creative search.

---


### 128. [Stoicheia: Character-Level Masked Diffusion for Ancient Greek Textual Restoration, Parsing, and Metrical Scansion](https://arxiv.org/abs/2608.07249)

**<font color=#1a73e8>作者：</font>** Eric Cullhed, Albin Thörn Cleland  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Stoicheia, a 405M-parameter character-level masked-diffusion encoder for Ancient Greek whose input factors into five aligned, independently maskable planes: letters, word and sentence boundaries, diacritics, capitalization, and punctuation. A single backbone can therefore restore lacunae, re-segment, accentuate, and punctuate unspaced text without task-specific retokenization. We pretrain it on an open, revision-pinned corpus of 380M words and release eleven checkpoints: ten rotated, decontaminated folds, guaranteeing that for any given literary passage at least one released model has never seen its text, and one with no exposure to documentary texts. Three experiments - reconstruction of damaged inscriptions and papyri, morphosyntactic tagging and dependency parsing, and macronization with metrical scansion - each carry a matched random-initialization control, isolating what character-level diffusion pretraining contributes: 5.6 CER points on inscription reconstruction, 12.9 LAS on parsing, and 6.0 points of balanced accuracy on macronization. On Ithaca's own test split, with identical frozen samples and strict scoring, Stoicheia reduces character error relative to both prior state-of-the-art systems, from 24.6 (Ithaca) and 23.5 (its 2025 Aeneas-framework successor) to 15.5, and raises top-1 accuracy from 63.0 and 64.0 to 74.5.

---


### 129. [Why Knowing Both Hops Is Not Enough: Understanding Two-Hop Generalization in Language Models](https://arxiv.org/abs/2608.07261)

**<font color=#1a73e8>作者：</font>** Zili Zhang, Yilin Wang, Heng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can solve complex multi-hop problems yet exhibit puzzling failures on simple two-hop queries: although a model may correctly store each individual hop, it often fails to combine them. To understand the internal mechanisms of this phenomenon, we train transformers from scratch in a controlled symbolic environment. Our experiments reveal a pattern in two-hop generalization: models generalize reliably when the second hop follows the training distribution, but always fail when it deviates.
Through mechanistic analysis, we provide a complete explanation for these distinct generalization behaviors: in settings where models generalize successfully, performance is driven by the emergence of consistent intermediate representations for the same entities across contexts, whereas failures on settings where the second hop is out-of-distribution arise from a mismatch across layers: lower layers correctly construct these intermediate representations, but upper layers, while trained on corresponding atomic facts, primarily learn to map them to outputs rather than to reason over them.
Driven by this insight, we propose a recurrent-style training strategy, which enables transformers to reuse their reasoning circuitry across input forms and substantially improves generalization on out-of-distribution two-hop queries.

---


### 130. [WNM-3D: A World Navigation Model with 3D Scene Conditioning for Closed-Loop VLN](https://arxiv.org/abs/2608.07267)

**<font color=#1a73e8>作者：</font>** Yuehao Huang, Yunzi Wu, Xiaotao Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent vision-language navigation (VLN) systems increasingly adapt pretrained vision-language models (VLMs) into vision-language-action (VLA) policies that map egocentric observations and language instructions directly to navigation actions. Although semantically capable, such action-centric training does not explicitly model how the agent's visual observations should evolve under its predicted motion. Generative world-action models (WAMs) jointly predict future observations and actions, yet existing WAMs for continuous VLN do not condition joint future-view and action generation on geometry-aware representations inferred from the observed history. We present WNM-3D, a generative World Navigation Model with 3D scene conditioning for continuous VLN. To consolidate past observations into persistent scene context, a frozen feed-forward geometry encoder extracts geometry-aware representations from the monocular egocentric RGB history, and a trainable 3D Scene-to-Token Adapter converts them into a fixed-length prefix in the token space of the world-action Diffusion Transformer. Through block-causal attention, this prefix conditions every future video-action block, providing a shared geometric context for both future-view and action generation. We train WNM-3D through supervised world-action fine-tuning on A*-generated demonstrations, DAgger-style adaptation on policy-visited states, and DanceGRPO-based closed-loop policy optimization. Experiments on GN-Bench show that WNM-3D outperforms strong VLM-based navigation policies and its 2D-conditioned counterpart in closed-loop navigation. On a fixed near-goal evaluation set, WNM-3D also achieves higher flow-action consistency and lower visual-motion error.

---


### 131. [Gaze Behavior in Visual World Experiments Can be Modeled With Off-the-shelf Language-Vision Encoders](https://arxiv.org/abs/2608.07282)

**<font color=#1a73e8>作者：</font>** Rahul Murali Shankar, Titus von der Malsburg, Sebastian Padó  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The recent advances in neural language models have also spurred much work in computational psycholinguistics, asking whether neural LMs are also promising models of human language processing. However, work has been overwhelmingly focused on the unimodal case of written or spoken language. In contrast, multimodal experimental paradigms, like visual world studies that present participants with both visual and linguistic input simultaneously, have been neglected. In this paper, we present a novel approach that predicts gaze behavior in visual world studies. It does so by combining a simple multi-modal bi-encoder model of the CLIP family with a bimodal attribution method. We demonstrate the ability of this approach to robustly replicate the results of a seminal English visual world study which shows hu- man predictive processing. Remarkably, it does so without a generative architecture and without the need for fine-tuning, despite not being trained for this task.

---


### 132. [Grammar Engineering Meets LLMs: Development of Cantonese and Irish ParGram Treebanks](https://arxiv.org/abs/2608.07283)

**<font color=#1a73e8>作者：</font>** Chit-Fung Lam, Elaine Uí Dhonnchadha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammar engineering requires expertise in linguistic formalism and computational implementation, especially in parallel grammar projects that balance cross-linguistic consistency with language-specific properties. This paper presents the development of Cantonese and Irish treebanks within the Parallel Grammar (ParGram) Project, where linguistic parallelism is maintained at an abstract functional level. We also investigate the methodological potential and limitations of using multilingual LLMs to support grammar engineering, focusing on Cantonese-Irish translation and the generation of formal syntactic structures using OpenAI's gpt-oss-120b model. The results show that translation performance was generally unsatisfactory and unaffected by prompt language. For syntactic structure generation, the model produced some structurally meaningful outputs, but performed poorly on tasks requiring cross-linguistic abstraction. Nonetheless, LLM-generated outputs may still offer some reference value by suggesting alternative analyses and (partially) capturing predicate-argument relations. Overall, our findings highlight both the potential and limitations of using LLMs in collaborative grammar engineering, while underscoring the continued importance of expert-driven analysis and verification.

---


### 133. [Same Attention, Different Truths: Put Logit-Lens over Visual Attention to Detect and Mitigate LVLM Object Hallucination](https://arxiv.org/abs/2608.07302)

**<font color=#1a73e8>作者：</font>** Zichuan Wang, Songlin Yang, Bo Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) often suffer from object hallucination, generating objects that are absent from the image. Prior work largely attributes this to insufficient visual attention. However, we find that both real and hallucinated objects receive equally strong visual attention in the model's mid-to-late layers, suggesting that the key issue may not be how much the model attends, but what it attends to and why. To this end, we decode the visual features of high-attention regions using Logit Lens, and observe that regions corresponding to real objects can be correctly decoded to the target object tokens, whereas those for hallucinated objects cannot. Building on this, we identify two hallucination mechanisms: (i) visual uncertainty, triggered by semantically similar or confusable regions; masking these regions eliminates the hallucination. (ii) contextual prior, triggered by strong co-occurrence priors; even when the initially attended region is masked, the hallucination persists and attention drifts to other regions. Based on these findings, we propose a simple yet effective training-free Detect-Mitigate framework comprising a Logit-Lens Consistency Check to detect hallucination and targeted remedies: High-Attention Regions Masking (HARM) for visual uncertainty hallucination, and Visual Evidence Enhanced Decoding (VEED) for contextual prior hallucination. Our approach achieves state-of-the-art results on multiple hallucination benchmarks. Code will be available.

---


### 134. [Natural Language Processing Psychometrics](https://arxiv.org/abs/2608.07316)

**<font color=#1a73e8>作者：</font>** Edoardo Sebastiano De Duro, Emma Franchino, Massimo Stella  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Processing (NLP) models predicting mental health outcomes rarely specify what they measure: contextual knowledge, emotional content, or syntactic structure. NLP Psychometrics treats psychological prediction from text as a psychometric problem, linking scores to interpretable linguistic evidence and testing beyond the training text format. Nine LLMs, conditioned on controlled personas (cognitive digital shadows), completed psychometric questionnaires with textual explanations per item. We extracted emotional profiles and syntactic-semantic structure via textual forma mentis networks, combined with personality and sociodemographic variables in ablated random forest (RF) regressors, using SHAP to identify which features drove performance and in which direction. Full RF models explained up to 70.8% of variance in life satisfaction (SWLS), 55.7% in depression (PHQ-9), and, for DASS-21, 68.5% depression, 76.0% anxiety, 72.4% stress. Sociodemographics alone explained no meaningful variance in depression, anxiety, or stress, but did so for life satisfaction, where emotion features and income were the strongest predictors; neuroticism and network topology instead dominated depression and anxiety, reversing direction between them. Without retraining, RF models separated diaries from low- and high-score personas ($r$ up to 0.91) and, using only network/emotion features, classified clinical from control participants in real transcripts with up to 68% accuracy. These results show the promise and limits of synthetic data: LLM personas can expose model biases, recover patterns consistent with clinical rumination, and support psychometric prediction from human text without a matched questionnaire, but cannot substitute for human validation. NLP Psychometrics makes these distinctions explicit, measurable, and testable through interpretable AI and network/emotional features.

---


### 135. [Is SwiGLU's Open Positive Tail Necessary? Evidence from Closed-Tail Gating with MemGLU](https://arxiv.org/abs/2608.07323)

**<font color=#1a73e8>作者：</font>** Yuting Ge, Pengju Yang, Mingkai Nie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We test whether decoder-only language-model FFNs require SwiGLU's open positive tail. We introduce MemGLU as a closed-tail comparator derived from a memristive branch geometry. Across paired 9M and 30M pretraining runs with three seeds, MemGLU remains within about 0.1% of SwiGLU in validation NLL. Trained SwiGLU checkpoints are sensitive to positive-tail suppression, while mechanism diagnostics show that the two models use their gates differently despite similar losses. These results suggest that models adapt to the gate geometry available during pretraining. At the tested scales, SwiGLU's open positive tail is not necessary for decoder-only language-model FFNs.

---


### 136. [Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation and Step-wise Mitigation of Benchmark Contamination](https://arxiv.org/abs/2608.07341)

**<font color=#1a73e8>作者：</font>** Ruijie Hou, Yueyang Jiao, Zhao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test data from public benchmarks inevitably leaks into pretraining corpora, inflating evaluation scores once memorized. \textbf{Contamination mitigation evaluation} intervenes in the decoding process to suppress memorization and restore a contaminated model's genuine capability, but its prevailing metric, the \textbf{G-AP} (\textbf{G}ap of \textbf{A}ggregate \textbf{P}erformance), is flawed. Discrete correct/incorrect readouts cannot characterize per-question performance, averaging before differencing lets over- and under-suppression cancel out, and uniform per-question weighting invites strategies to push solve probabilities onto the clean model's high-frequency values. We propose \textbf{SA-PPG} (\textbf{S}tratified \textbf{A}ggregate of \textbf{P}er-question \textbf{P}robability \textbf{G}aps): estimate each question's solve probability by sampling, difference it against the clean model per question, and aggregate within groups defined by the clean model's solve probability. Existing mitigation strategies first estimate where contamination lies and then operate on the estimate, so they are only as correct as the estimate. \textbf{RailCap} instead judges contamination during generation: whenever a sample falls back onto the greedy trajectory, the next trajectory token is capped to the runner-up, accumulating suppression until the response distribution becomes sufficiently dispersed. Across multiple contaminated models and benchmarks, SA-PPG reveals that prior strategies' restoration is substantially overestimated, while RailCap attains the lowest SA-PPG.

---


### 137. [An End-to-End Agent Auditing Engine](https://arxiv.org/abs/2608.07346)

**<font color=#1a73e8>作者：</font>** Haoning Wang, Mingxun Zhang, Chenyue Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of large language models (LLMs), harnesses have become essential infrastructure for deploying agents across a wide range of domains. The fast-evolving harness ecosystem has also made rigorous capability evaluation increasingly important. However, efficiently building an end-to-end, systematic, and comprehensive evaluation pipeline remains a significant challenge. To address this challenge, we introduce $A^2E$ (Agent Auditing Engine), an end-to-end evaluation engine designed for agent harnesses. $A^2E$ leverages our newly proposed Agent Task Protocol (ATP) to enable the rapid integration of evaluation tasks with different harnesses. Through an automatically instrumented Monitor, it captures and generates standardized execution traces during experiments. In the Evaluation stage, $A^2E$ systematically assesses harness capabilities using a suite of multidimensional metrics. Compared with correctness alone, these metrics provide a more fine-grained characterization of differences among harnesses in execution efficiency, tool use, task planning, and error recovery. Experiments conducted with $A^2E$ further reveal that model-harness combinations exhibit substantial performance variation across different types of tasks, and that no single combination consistently outperforms all others across every task. These findings not only demonstrate the necessity of systematic evaluation but also provide useful guidance for the co-evolving of models and harnesses. Our code is available at this https URL.

---


### 138. [Geo-Spatial Concept Probing of Large Language Models: Abstraction, Compositionality, and Grounding](https://arxiv.org/abs/2608.07353)

**<font color=#1a73e8>作者：</font>** Karim Radouane, Jose G Moreno, Lynda Tamine  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding concepts is fundamental to generalization. Despite their impressive performance on a wide range of tasks, Large Language Models (LLMs) still struggle with genuine concept understanding. Prior work has evaluated conceptual understanding in LLMs using natural-language benchmarks or narrowly scoped synthetic tasks, but these settings often conflate multiple skills or lack precise control over the underlying concepts and their properties. To support controlled probing of concepts in LLMs, we design tests on their core properties: abstraction, compositionality, and groundness. We set up a concept-centric benchmark, targeting spatial concepts such as direction, distance, topology, and their compositions, and use question answering tasks serving as a proxy. We conduct extensive experiments across multiple LLM architectures and training regimes to analyze how model scale and design impact conceptual understanding. The results reveal clear limitations in current LLMs and provide insights into the factors shaping their ability to acquire and compose structured concepts. Our findings shed light on how concept-based LLMs can be redesigned for improved information access and knowledge management. The code will be available at this https URL.

---


### 139. [Curriculum as Code: An AI-Assisted Architecture for Instructional Design in STEM Education](https://arxiv.org/abs/2608.07364)

**<font color=#1a73e8>作者：</font>** Henrique Mohallem Paiva  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contribution: This paper presents a six-phase AI-assisted instructional design architecture based on the Curriculum as Code paradigm, integrating Generative AI with LaTeX and Python to automate the creation of reproducible, visually consistent, and technically precise materials for STEM education. Background: Creating customized instructional materials for active learning imposes a heavy workload on faculty. Standard presentation tools lack robust support for technical content, while current AI applications often hallucinate and fail to formalize the instructional authoring process, limiting their utility for rigorous academic design. Intended Outcomes: The framework aims to reduce preparation time while ensuring mathematical accuracy, adherence to institutional visual identity, and preservation of the instructor's tacit pedagogical knowledge through explicit rules. Application Design: The solution comprises a six-phase pipeline that replaces ad-hoc prompt engineering with a systematic workflow, utilizing text-based interfaces and code-driven generation (LaTeX/Beamer for slides, Python for figures), governed by pedagogical constraints, contextual calibrations, and automated review cycles. Findings: Validated over one year across 8 modules and 28 project contexts in a Project-Based Learning environment, the architecture significantly reduced instructor workload. Generated assets underwent independent peer review and were deployed by six different faculty members, confirming scalability beyond a single author. Based on over 600 voluntary student evaluations, materials achieved high quality ratings from 8.5 to 9.9/10. Results indicate high reproducibility, minimized hallucinations, and sustained pedagogical and visual fidelity, suggesting viability for broad STEM educational applications.

---


### 140. [People Are Not Just Their Countries. Disentangling Social Determinants of LLM Value Alignment Across Europe](https://arxiv.org/abs/2608.07367)

**<font color=#1a73e8>作者：</font>** Maria-Louisa Wightman, Guillaume Bied, Tijl De Bie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly used as a primary source of information and advice, understanding their alignment to humans in terms of values becomes a pressing concern. A growing literature has leveraged large scale surveys to investigate to what extent LLMs' and humans' stated values and opinions align. With limited exceptions, studied populations have been defined country borders or cultural bounds. Yet, this focus neglects the role that socio-demographic divides may play for value alignment disparities.
Relying on the European Social Survey, we address this knowledge gap by considering value alignment displayed with respect to 10 prominent commercial LLMs in terms of 15 socio-demographic variables as well as country of residence. Our analyses reveal that LLMs are indeed unequally aligned to the values of different socio-demographic groups, notably those defined by education, income, occupation and religion. When examining alignment at the individual level, a respondent's country, taken as a stand-alone variable, explains a substantial amount of variation that is on par with the full set of considered socio-demographics. Further disentangling the respective role of country-level and socio-demographic factors, we find they are complementary in explaining value alignment patterns, with their relative weights varying across the subset of questions considered.

---


### 141. [LitTraceQA: A Benchmark for Multi-Stage Grounding and Verification in Scientific Question Answering](https://arxiv.org/abs/2608.07370)

**<font color=#1a73e8>作者：</font>** Xuye Liu, Yimu Wang, Peng Shi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific literature is increasingly used as a knowledge source for language models, retrieval-augmented generation systems, and research assistants, but answering research questions from papers requires more than fluent generation. A reliable system must identify the relevant papers, locate the concrete evidence that supports the answer, and produce a response that is faithful to that evidence. We present LitTraceQA, a benchmark for literature-grounded question answering over scientific papers. Given a research question and a metadata pool of papers, a system must return three connected outputs: canonical paper identifiers, supporting evidence locations, and answers in one or more requested formats, including free-form text, multiple-choice answers, and structured tables. LitTraceQA targets evidence types common in scientific reading: tables, figures, text spans, equations or algorithms, and citation contexts. The public development split contains 55 examples, including 26 hidden-source single-paper questions and 29 multi-paper questions, and provides gold papers, evidence annotations, and answers for local validation. We also analyze a larger final annotation collection with 4,978 unique-question records over 4,859 unique gold papers. By evaluating paper retrieval, evidence grounding, and answer accuracy separately, LitTraceQA provides a testbed for scientific QA systems that produce verifiable answers rather than unsupported summaries.

---


### 142. [Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.07371)

**<font color=#1a73e8>作者：</font>** Haoyu Zheng, Yun Zhu, Qing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent agentic reinforcement learning methods use hindsight to complement sparse outcome rewards. However, a completed rollout can yield many such signals, leaving their appropriate allocation across turns unclear. We introduce TRIAL, a trajectory-relative hindsight distillation framework with a unified turn-aligned scoring protocol. For each decision turn, TRIAL extracts an outcome view of that decision's realized consequence and evaluates the same response under ordinary and hindsight-conditioned contexts. The signed log-probability gap determines the direction and local strength of token-level supervision, while turn-level magnitudes are normalized jointly over the realized trajectory. The resulting allocation multipliers have an eligible-token-weighted mean of one, redistributing dense supervision across turns while fixing its average multiplier. Experiments on WebShop and ALFWorld with different backbones show that TRIAL outperforms GRPO across all eight combinations of backbone, environment, and evaluation metric, while achieving the best or tied-best performance among six methods on six of them. On WebShop with Qwen3-1.7B, TRIAL improves the success rate from 56.4% to 75.2% and the task score from 78.7% to 85.7%. Controlled ablations further show that trajectory-relative turn allocation provides substantial gains beyond those of dense hindsight distillation alone.

---


### 143. [GeoBenchLLM: A Comprehensive Benchmark for Evaluating LLMs on Geo-Related Tasks](https://arxiv.org/abs/2608.07411)

**<font color=#1a73e8>作者：</font>** Rodrigo Ferreira Rodrigues, Karim Radouane, Jose G Moreno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the context of geodata, existing Large Language Models have often been studied in a homogeneous setting, which has considerably limited insights into their generalization capabilities. In this paper, we present \benchName, a comprehensive benchmark for probing LLMs on geo-related tasks. We leverage a careful selection of twelve publicly available datasets from diverse geo-related tasks and domains, and evaluate a set of LLMs on geo-spatial and temporal understanding using our benchmark. Our results show that reasoning and size have a strong impact on overall performance. GeoBenchLLM is publicly available at this https URL.

---


### 144. [I Seek You in Videos: Identity-Conditioned Queries for Person-Centric Video Reasoning](https://arxiv.org/abs/2608.07417)

**<font color=#1a73e8>作者：</font>** Shibo Gao, Chongxiao Wang, Chenglong Huang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world video reasoning often involves multimodal, multi-source inputs, whereas existing video reasoning tasks typically assume a simplified video-text setting, limiting identity matching and person-centric reasoning. To bridge this gap, we introduce the Identity-conditioned Queries (ICQ) task, in which models are required to jointly associate and interpret an input video and a reference image of a person, and leverage this conditioning to address identity grounding, behavior understanding, and temporal reasoning, among other challenges. Building on ICQ, we present ISYV (I Seek You in Videos), a systematic solution comprising three components: (1) ISYV-Bench, a challenging evaluation benchmark with 1,377 real-world complex videos and 1,377 question-answer pairs, organized into six difficulty levels spanning capabilities from identity recognition to causal reasoning; (2) ISYV-75K, a large-scale training set of 75K high-quality samples constructed via automated annotation, multi-stage verification, and manual review; and (3) ISYV-Framework, containing an ICQ-oriented model and training strategy for learning to exploit informative video shots without additional shot-level annotations. Extensive experiments show that both mainstream closed-source and open-source MLLMs struggle on ISYV-Bench, especially in cross-domain identity matching and long-horizon tracking. ISYV-Model outperforms strong baselines and in some aspects approaches closed-source performance. Overall, ISYV provides a unified task definition, scalable datasets/benchmarks, and modeling insights for person-centric video reasoning.

---


### 145. [ResidencyRL: Reinforcement Learning in Simulated Clinical Environments](https://arxiv.org/abs/2608.07418)

**<font color=#1a73e8>作者：</font>** Valentin Liévin, Samuel Schmidgall, Tim Strother 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In medical education, physicians convert academic knowledge into clinical expertise through residency: years of training across thousands of encounters, with diverse sources of feedback and progressively greater autonomy. Much of clinical reasoning relies on the patient encounter, a dialogue in which a clinician elicits history, refines diagnostic hypotheses, and decides management under uncertainty. While large language models (LLMs) excel on static medical benchmarks, methods to optimize the full sequence of clinical decisions remain underdeveloped. We present ResidencyRL, a reinforcement learning (RL) method for training clinical artificial intelligence (AI) agents through simulated multi-turn clinical encounters (up to 60 dialogue turns and 8 tool calls per trajectory). ResidencyRL pairs the policy agent with LLM simulators capable of complex, adversarial behaviors, training against a structured reward aligned to diagnostic accuracy, management quality, communication, documentation, and safety. On held-out evaluations, the ResidencyRL agent improves diagnostic accuracy by 7.0% under adversarial conditions (88.0% vs. 81.0%) and reduces missed red flag rates by 31%, demonstrating rigorous mitigation of premature closure. Blinded expert clinicians validated these gains, preferring the trained agent in 87.6% of side-by-side comparisons. The procedural competencies transfer to unseen benchmarks: the agent outperforms the base model across all six clinical axes of the AMIE multi-visit benchmark, and shows consistent directional improvements on AgentClinic and CRAFT-MD. Our findings demonstrate that sequential clinical decision-making can be effectively learned through multi-turn RL in simulation, yielding robust, generalizable capabilities, paving the way towards clinical mastery. Prospective validation with real-world workflows remains necessary to establish clinical utility.

---


### 146. [Beyond Post-Hoc Temperature Scaling: Bilevel Optimization for LLM Calibration](https://arxiv.org/abs/2608.07419)

**<font color=#1a73e8>作者：</font>** Ruochen Jin, Zhanliang Wang, Zongyu Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference alignment often makes large language models (LLMs) overconfident and poorly calibrated. Traditional post-hoc temperature scaling is inherently domain-dependent: a temperature fitted on one domain does not generalize across domains. This motivates us to modify model parameters during training to improve calibration. We propose maximizing the entropy of predictive distributions as the calibration objective, which directly targets overconfidence by discouraging overly concentrated predictions. Inspired by temperature scaling, we realize this through a bilevel optimization formulation, where the lower level trains the model under a parametric loss and the upper level selects loss hyperparameters to maximize entropy. To make the framework practical at LLM scale, we adopt an efficient first-order approximation that avoids explicit second-order computation. Across both multiple-choice and open-ended generative question answering, experiments demonstrate that our method yields well-calibrated LLMs with particular advantages in out-of-domain generalization.

---


### 147. [CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing](https://arxiv.org/abs/2608.07424)

**<font color=#1a73e8>作者：</font>** Yan Zhou, Yue Ouyang, Kaiyang Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling is often implemented by spending more compute along one axis: sampling more solutions, extending a chain of thought, or applying a stronger evaluator. Under a fixed inference budget, these choices compete. This paper formulates test-time reasoning as a compute-allocation problem in which a system must decide whether the next unit of compute should be spent on generation, verification, or stopping. We introduce CoBa, a compute-balanced routing policy that first obtains a small set of candidates, applies cheap verification broadly, and routes uncertain or high-value candidates to stronger verification. On 3,129 example-generator evaluations spanning MATH-500, AIME 2024/2025, AMC 2023, and procedural symbolic reasoning, CoBa-Routed-Strong reaches 85.13% macro accuracy, statistically matching a self-evaluation weighted-voting proxy at 85.20% while using 49.1% fewer parameter-weighted tokens. It also matches best-of-16 majority voting within 0.01 macro-accuracy points while using 58.9% fewer parameter-weighted tokens; paired tests retain a small best-of-16 edge at substantially higher cost. Paired bootstrap tests show significant gains over single-sample decoding, while the remaining gap to the pool oracle exposes headroom for sharper routing. For local reasoning systems, test-time scaling becomes a question of where the next computation is most valuable.

---


### 148. [A Picture is Worth a Thousand Tokens: How Vision Language Models Cut AI Energy Costs While Improving Accuracy](https://arxiv.org/abs/2608.07427)

**<font color=#1a73e8>作者：</font>** Bhavika Jalli, Nikhil Korati Prasanna, Jayanta Choudhury  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM inference accounts for over 90% of AI operational energy, scaling directly with input token count---a critical inefficiency for telecom network analytics and numerical time-series data analysis (NTSDA), where raw multivariate KPI windows from 4G/5G cell sites expand into thousands of floating-point tokens. Vision-Language Models (VLMs) eliminate this mismatch by encoding time-series as 2D plots, achieving 3.6-10.4x input token reduction across Llama-3.2-90B, Qwen2.5-VL-72B, and Pixtral-12B architectures. This translates to 1.8-2.5x measured inference energy reduction, saving approximately 7.2 MJ/day at telecom edge deployments and CloudRAN that monitor 200 cells per 15-minute interval. Critically, efficiency gains do not sacrifice accuracy: a fine-tuned Llama-3.2-90B-Vision VLM achieves 220.7% higher precision than its text-only counterpart and outperforms LSTM and ARIMA baselines by over 144% on telecom anomaly detection. On public benchmarks, Pixtral-12B achieves a 20.6x improvement in J/F1 score at mean F1 = 0.82. At 24 KPIs, text representations exceed the 128K context window of most production LLMs, rendering text-only processing infeasible without truncation, while visual representations remain within standard limits. These results establish VLMs as an energy-efficient and accuracy-superior modality for numerical time-series workloads, providing empirical grounding for AI inference systems that treat energy consumption as a first-class engineering constraint.

---


### 149. [TEPA: Revoking Stale Memories for Conflict-Robust Language Agents](https://arxiv.org/abs/2608.07429)

**<font color=#1a73e8>作者：</font>** Yan Zhou, Yue Ouyang, Kaiyang Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables language agents to reuse past facts, preferences, and task experience. Persistence also creates a central falsifiability problem: when the world changes, stale memories can remain retrievable and pollute the prompt. We characterize this failure mode as memory pollution: degradation caused by active memories that newer conflicting evidence has superseded. We introduce TEPA, a revocable evidence-memory mechanism that makes validity an explicit state of memory. TEPA represents observations as keyed precedents and revokes active precedents when fresh evidence contradicts them under the same key, allowing retrieval to draw from current evidence while preserving revoked history for audit. Across controlled hidden-regime drift, real file-backed executable drift, and preference-update streams, revocation prevents stale active memory from remaining in the retrieval set after reversal. In controlled drift over 50 seeds, append-only and last-write-wins memory fell below no memory during full reversal (append-only and last-write-wins both 0.210, no memory 0.309, TEPA 0.950), and the same pattern reproduced under real file execution (append-only 0.203, no memory 0.298, TEPA 0.950). On clean MemoryAgentBench SH-6k, TEPA matches a strong last-write-wins cache, confirming that current-key replacement is the decisive operation for single-hop fact consolidation. Boundary tests on multi-hop and very long-context MemoryAgentBench settings expose retrieval-chain and context-selection bottlenecks beyond fact-level validity tracking. Together, these results establish lifecycle revocation as a core memory operation for agents that must falsify, audit, and later re-promote evolving knowledge.

---


### 150. [Conformal Coverage Guarantees for Any Video Temporal Grounder](https://arxiv.org/abs/2608.07434)

**<font color=#1a73e8>作者：</font>** Aseel Mohamed, Rasul Khanbayov, Erchin Serpedin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event boundaries in continuous video are ambiguous: re-annotate the same query-video pair and independent annotators mark moments that overlap by less than half on a large fraction of samples. The ground truth for video temporal grounding is therefore a distribution over intervals, yet every grounder returns a single interval with no statement of reliability, so at deployment a wrong interval is indistinguishable from a right one. COVER changes the output object: a post-hoc, model-agnostic wrapper that turns any grounder, a trained localizer or a black-box video--language model, into one that emits a temporal region containing the true moment with probability at least $1-\alpha$, by calibrating the quantile of a temporal nonconformity score on held-out labels and widening the base prediction by that amount. The guarantee is finite-sample and distribution-free under exchangeability, and requires neither retraining nor white-box access. We give two score families, a two-sided boundary-widening score for grounders that emit an interval and a super-level-set score for grounders that emit a relevance signal, and develop theory specific to grounding that bounds how large the certified region becomes, when coverage survives conditioning on event length, and how it degrades when moments from one video break exchangeability. Across three benchmarks and five grounders, realized coverage tracks the target, and calibration exposes what point metrics hide.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-170](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
