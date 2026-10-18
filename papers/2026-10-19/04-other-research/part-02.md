# 📦 其他研究 | 2026年10月19日

> 本类共 **278** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-278](./part-06.md)

---

### 51. [Defining and Generating Compositional Structure](https://arxiv.org/abs/2610.20922)

**<font color=#1a73e8>作者：</font>** Eric Elmoznino, Tejas Kasetty, Blaise Agüera y Arcas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compositional structure is pervasive in nature and across scales: atoms combine into molecules, molecules into cells, and cells into organisms, while further compositional hierarchies appear within each level. More broadly, compositionality, the reuse and recombination of parts into novel structures, is a fundamental source of interesting complexity in both natural and artificial systems. Yet despite its importance, and despite our apparent ease in recognizing it, mathematical accounts capturing what we intuitively mean by compositional structure remain limited. Here, we fill this gap by formalizing a simple idea: compositional structure emerges when parts, considered together, reveal shared structure that is not captured when those parts are modeled separately. We express this idea using algorithmic information theory, the mathematics of information and compression, which provides a natural way to identify structure in arbitrary data without specifying in advance what that structure must look like. Applied across scales, our definition informs where and how compositional structure emerges within an object. Using tractable approximations, we then invert the framework to generate compositional objects: we specify the desired form of their compositional structure without prescribing their particular content, and optimize directly over strings and images. The resulting objects exhibit readily recognizable hierarchical reuse and part-whole organization, suggesting that the definition captures compositional structure rather than merely complexity, regularity, or shared information. Finally, we discuss implications for machine learning, including a new perspective on depth in neural architectures and principles for constructing compositional data curricula capable of supporting open-ended learning.

---


### 52. [RAC: A Relational Agent Contract for Constraint-Governed Engineering Tasks](https://arxiv.org/abs/2610.20935)

**<font color=#1a73e8>作者：</font>** Kaiyuan Zheng, Fengqing Jiang, Yichen Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Engineering agents must produce artifacts that satisfy exact, coupled constraints. Existing solutions often require agents to make semantic decisions and also derive consequences such as precise geometry or timing from those decisions, leading to failures in constraint-governed engineering tasks. In this paper, we introduce RAC, a harness-agnostic contract for the action and feedback layer of engineering agents. It specifies authoritative observations, semantic actions, tool-based realization, independent verification, and repair evidence. The agent decides which relations an artifact should satisfy; specialized tools derive their concrete consequences. On PCB placement, routing, and repair tasks, RAC achieves the highest clean-pass rate for all nine evaluated models, averaging 90.9%, compared with 74.0% for the strongest baseline, requirements-only delegation. In job-shop scheduling, direct relational actions achieve 96.3% quality pass versus 59.6% for code-mediated delivery with access to the same scheduling backend. Our evaluations on 141 embedded-code tasks across four microcontroller identify the action contract as a source of agent capability: preserving semantic control while delegating mechanically derivable outputs improves the reliability of constrained artifacts.

---


### 53. [MAI-Gym: An Open All-in-One Platform for GUI Agent Evaluation and RL Training across Mobile and Computer Environments](https://arxiv.org/abs/2610.20939)

**<font color=#1a73e8>作者：</font>** Panrong Tong, Quyu Kong, Pengxiang Li 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online reinforcement learning (RL) with verifiable rewards has driven rapid progress in mathematics, coding, and tool use, but scaling this success to GUI agents remains challenging due to the high cost of interactive environments and the scarcity of realistic training tasks. We introduce MAI-Gym, an open all-in-one platform that unifies GUI agent evaluation, data collection, and online RL training across mobile, computer, and web environments. Through a shared rollout pipeline, MAI-Gym ensures consistent agent behavior across evaluation and training, supports ten established benchmarks, and scales to 20,000 parallel environment instances. Beyond scalable infrastructure, MAI-Gym enables automated synthesis of diverse GUI applications and challenging tasks, including resettable mocked apps and coherent cross-app worlds with execution-validated task verifiers. Using MAI-Gym, we train MAI-Gym-9B, a unified 9B agent for mobile and computer use, achieving state-of-the-art performance among open GUI agents under 10B parameters: 78.4% on MobileWorld and 76.2% on OSWorld-Verified. Importantly, RL in a mocked train-ticketing app transfers to its real-world counterpart, improving task success on a phys- ical phone from 28.8% to 48.1%. We release the framework, synthesis skills, mocked apps, 2,000 verified tasks, and the model checkpoint to support repro- ducible research and further advances in scalable GUI agent training.

---


### 54. [Does Client Diversity Protect the Lightning Network? Evidence from the 2026 Core Lightning Shutdown](https://arxiv.org/abs/2610.20952)

**<font color=#1a73e8>作者：</font>** Saurabh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Client diversity is often cited as the Lightning Network's defence against a bug in any one implementation, yet LND runs 84% of public nodes and holds 84% of public channel capacity, a share that has barely moved since 2023. We test what diversity buys with a natural experiment. On 26 August 2026, amid security fixes in every implementation, Core Lightning (CLN) maintainers told operators who could not upgrade to disconnect their nodes. Using 805 daily gossip snapshots, 132,360 on-chain channel closes and a client classifier validated against self-identifying aliases and against the wallet that builds each node's funding transactions, we find that 22% of CLN nodes went dark overnight, ten times the usual rate, mostly Tor-reachable ones; a third were still dark five weeks later. The rest of the network barely noticed. Reachability among all node pairs fell by 7.8 percentage points, a loss exceeded in 4 of 94 ordinary two-day windows and half that of a Tor denial-of-service wave in July, while among CLN pairs it fell by 24.5 points, more than in any ordinary window. Calibrated failure scenarios explain the containment: the blast radius depends on whether a failure reaches the hubs, not on how many nodes run the failing software. Losing ACINQ's Eclair node alone costs the surviving network four times the reachability lost with all 619 routable CLN nodes, and minority clients' reliance on LND for connectivity is what their size implies; CLN nodes in fact peer with each other more than chance. Diversity statistics that count nodes mislead; the quantity to track is which software the hubs run.

---


### 55. [StepSafe: Learning Timely Intervention with Context-Aware Safety Reasoning](https://arxiv.org/abs/2610.20960)

**<font color=#1a73e8>作者：</font>** Siyi Gu, Kunhan Gao, Chao Peter Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety in agentic systems is inherently sequential: whether an action is safe depends on prior actions, tool outputs, information disclosures, and interactions among agents. Recent work has shifted agent safety guardrails from post-hoc trajectory-level assessment toward step-level action diagnosis and proactive risk prediction, yet existing training objectives provide limited supervision for how step evidence accumulates over time and when it becomes sufficient to justify intervention. We propose \methodlong~(ASPO): a training framework for step-level timely intervention. Pre-fix level stage alignment allows crediting each decision at its own step: it compares each response with the other responses sampled at the same prefix and rewards the action that fits the stage, continuing before the risk is visible, asking while clarification can still avert harm, and stopping before harm is irreversible. Adaptive feedback self-distillation further credits the reasoning behind each decision, with the model itself as a teacher that sees the step annotations on intervention steps and rules mined from its own false alarms on safe steps. Its training data carry a violation taxonomy and an intervention window at every step and are extended through self-evolving multi-agent red-teaming. Finally we present \textsc{StepSafe}, a step-level reasoning guardrail with timely intervention, that achieves the state-of-the-art peformance among open-source guardrails across five agent-safety benchmarks on safety-utility pareto curve with Youden's $J$ of 53.0 (4B) against 46.2.

---


### 56. [DeSpatial: The devil of Agentic Spatial Reasoning Lies in 3D Itself](https://arxiv.org/abs/2610.20990)

**<font color=#1a73e8>作者：</font>** Yifei Liu, Xiaolong Zhou, Ziyang Gong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial agents have access to reconstruction and segmentation tools, yet inconsistent predictions and fragmented object identities can prevent their outputs from becoming reliable 3D scene information. A simple oracle experiment exposes this perception bottleneck: replacing tool-predicted perception with ground-truth 3D bounding boxes raises an agent to nearly full score across five object-centric VSI-Bench tasks, while retaining the same reasoning tools. Motivated by this finding, we believe the devil of spatial reasoning lies in 3D itself, and introduce DeSpatial(Devil of Spatial), which explicitly decomposes spatial understanding into perception and reasoning. DeSpatial has a shared 3D perception tool to reconcile independent perception outputs into a unified, metric, gravity-aligned 3D scene. This perception tool has two core components: a) a joint segmentation--depth co-refinement module that consolidates masks of the same object and removes projection artifacts caused by inconsistent segmentation and depth within a single frame; b) a cross-view instance fusion module that consolidate voxel-overlapping instances but not allowed to merge same-frame instances. This fusion module additionally fuses spatially disjoint fragments caused by insufficient multi-view observations, by checking their 3D structure and source mask appearance. After receiving the complete and unified 3D scene information, the agent chooses reasoning or computational tools to solve the spatial problem. DeSpatial achieves leading performance on VSI-Bench, MindCube-Tiny, and ViewSpatial, with additional long-video results on VSI-SUPER, revealing the bottleneck of spatial understanding lies in a precise 3D perception itself.

---


### 57. [One Bias Score, Two Factors: How Mitigations Affect Option Bias in Multiple-Choice Evaluation](https://arxiv.org/abs/2610.20993)

**<font color=#1a73e8>作者：</font>** Hyunjong Ok, Minjae Park, Jaeho Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reordering multiple-choice options can change a model's answer, an effect studied as selection bias (a preference for certain option letters) and as order sensitivity (changes in answers across option orderings). We connect these perspectives through the pooled selection-rate standard deviation (pooled SD), which measures how unevenly option letters are selected across questions and orderings. When every option of each question appears equally often at each position, the pooled SD is exactly the product of two label-free factors: the flip rate and the positional skew. The flip rate is the fraction of questions whose chosen option changes across orderings; the positional skew is the standard deviation of option-letter selection rates among those questions. Across 41 checkpoints and 12 benchmarks, the flip rate tracks accuracy and output uncertainty, while the positional skew tracks the estimated option-symbol prior. Prior correction for selection bias mainly reduces the positional skew. Aggregating each ordering with its reversal, a mitigation for order sensitivity, mainly reduces the flip rate. Both reduce the range of accuracy across correct-answer letters by similar amounts, but aggregation leaves fewer model-rank reversals. Applying prior correction before aggregation reduces both factors and further narrows this accuracy range. However, aggregation lowers the flip rate partly by settling questions on the same wrong option. We therefore recommend reporting both factors to distinguish mitigation effects, alongside accuracy to distinguish stability from correctness.

---


### 58. [Halve-Then-Greedy: Adaptive Sampling for Posterior Success with Near-Optimal Instance Dependence](https://arxiv.org/abs/2610.20997)

**<font color=#1a73e8>作者：</font>** Yinan Li, Kwang-Sung Jun, Kapilan Balagopalan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study fixed-budget adaptive experimentation aimed at maximizing the probability of obtaining sufficient posterior evidence that a recommended design's mean performance exceeds a target. Unlike best-arm identification, this objective does not require finding the best design. For Gaussian bandits with a Gaussian prior, we propose \emph{Halve-Then-Greedy} (HTG), which combines a large initial balanced allocation, successive halving, and posterior-greedy sampling. We prove instance-dependent, finite-budget exponential bounds on posterior-failure probability that capture both separation from unfavorable arms and the presence of multiple favorable arms. On one-positive-arm families, we establish an asymptotic sample-complexity lower bound that HTG matches up to a logarithmic factor. We further analyze uniform sampling and sequential halving, revealing regimes where they require more samples than HTG by linear and logarithmic factors, respectively. Simulations illustrate HTG's sample-efficiency advantages and their dependence on instance structure.

---


### 59. [EigDiff: Eigensample Diffusion - or how to significantly reduce training dataset size with marginal performance variation?](https://arxiv.org/abs/2610.20999)

**<font color=#1a73e8>作者：</font>** Andrei Jarca, Vlad Hondru, Florinel-Alin Croitoru 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models are notoriously expensive to train, requiring large-scale datasets to learn how to gradually reverse the noise from images over multiple small denoising steps. Current approaches focus on distilling the number of diffusion steps, neglecting potential redundancies of the training data. In this paper, we explore the potential of harnessing eigensamples to train diffusion models on significantly smaller datasets, while preserving model performance. To mitigate the sensitivity to affine transformations of eigenimages, we harness the latent space of a pre-trained CLIP model. We next compute latent eigenvectors by performing principal component analysis (PCA) in CLIP space. Further, we employ eigenvectors as reference points to guide the selection of a representative training set comprising comprising both exemplars (images whose embeddings are closest to eigenvectors) and diverse images. Our comprehensive experiments with different diffusion models applied on multiple datasets indicate that our approach (EigDiff) can reduce training data by up to 14x and accelerate subset selection by up to 1607x, with marginal performance differences.

---


### 60. [Imperfect Is Perfect: Learned Column Prefilling for Branch-Price-and-Cut](https://arxiv.org/abs/2610.21001)

**<font color=#1a73e8>作者：</font>** Haoran Liu, Yu Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Column generation folklore warns that initial columns hurt: a warm start may bias the dual and slow the root of branch-price-and-cut. We show the opposite once the columns are imperfect in the right way. Preloading the support of the optimal root LP, the best columns one could know in advance, fails to finish on half of our hardest instances; a pool of ordinary routes that need not belong to any optimal solution, held outside the master and priced at the current smoothed dual, speeds the root up. Because the columns need not be optimal, producing them becomes a learning task: a neural edge scorer guides a constructive generator that builds the pool in seconds. A second network predicts the initial center of Wentges smoothing from the instance file, and with it the direction of the smoothed pricing queries; the solver's own updates run unchanged. With prefill and center in place, exact pricing dominates root pricing time, so we rebuild bucket-graph labeling around its dominance test for the GPU and certify on the CPU. Inside RouteOpt, the state-of-the-art exact solver for capacitated vehicle routing, the pipeline reaches the same certified root bound in 13.2% of vanilla RouteOpt's root pricing time over 95 instances with 300 to 1000 customers, prefill alone in 26.1%, and 17.5 times faster in the best case. In an exact branch-price-and-cut solver for unrelated parallel machine scheduling, prefill with smoothing and the learned center certifies all 25 benchmark instances, 12 times faster than the solver's own column generation, which certifies 20 of them.

---


### 61. [Mind the Tail: Data Selection Through Sparse Concepts](https://arxiv.org/abs/2610.21007)

**<font color=#1a73e8>作者：</font>** Ziheng Zhang, Neha Hulkund, Colin Lee 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data selection reallocates training support across visual concepts, including objects, attributes, color, texture, and backgrounds. Different allocation strategies may produce varied downstream model behavior, especially for tail concepts supported by only a few samples. Discarding them can hurt test-time robustness, while overemphasizing samples lying on category boundaries may introduce unstable training signals. This work explicitly investigates this relationship across fine-grained, spurious-correlation, and general image classification, as well as multimodal pretraining. Specifically, we use sparse autoencoders (SAEs) to extract concept activations from individual images. During selection, we accumulate the dataset-level concept support for each added sample. Applying diminishing returns to this distribution down-weights well-represented concepts and shifts the focus to the distribution tail. We then incorporate local support to find samples that reliably strengthen under-supported concepts. Empirical results show consistent improvements over strong data selection baselines across all benchmarks. We also reveal the connection between concepts our method enhances and the induced behavioral changes, including improved robustness against out-of-distribution and spurious contexts. This work establishes concept support, beyond individual sample importance, as a useful principle for data-efficient and robust learning.

---


### 62. [Deep Reinforcement Learning for HPC Job Scheduling: A Statistical Evaluation](https://arxiv.org/abs/2610.21008)

**<font color=#1a73e8>作者：</font>** Justin M. Cheney, Clement N. Nyirenda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep Reinforcement Learning (DRL) offers learned job selection for High-Performance Computing (HPC), but performance against heuristics alone does not establish value beyond action masking. Six DRL treatments are compared: Proximal Policy Optimization (PPO), Advantage Actor-Critic (A2C), and Deep Q-Network (DQN), each with and without masking. Three heuristics and a seed-paired masked uniform random control provide baselines across ten seeds on two real Slurm (Simple Linux Utility for Resource Management) workload traces, one homogeneous and one heterogeneous, under a common non-parametric framework. All masked treatments complete evaluation, whereas unmasked treatments are truncated. On the homogeneous trace, no masked DRL treatment significantly improves average waiting time or average and maximum bounded slowdown over the control. On the heterogeneous trace, MaskablePPO improves all three metrics relative to the control. Its average waiting time is equivalent to that of the three heuristics within a 10% margin, and its maximum bounded slowdown is 22% lower than that of Last-Come, First-Served (LCFS). MaskablePPO has the leading average waiting-time rank among complete treatments on both traces, but Nemenyi comparisons detect no significant difference from MaskableA2C. Among masked variants, MaskablePPO has the lowest recorded mean training time, while MaskableDQN has the lowest mean decision latency. These findings distinguish completion from baseline-specific scheduling gains and support including a masked random control when assessing the value of learned selection.

---


### 63. [Audio-Visual Dog Identification and Tracking in Real-World Videos](https://arxiv.org/abs/2610.21011)

**<font color=#1a73e8>作者：</font>** Aryahvishwa Babu, Kingsley Jin, Lillian Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identifying individual dogs from barks in real-world videos remains challenging and largely unexplored. Solving this problem would enable long-term behavioral analysis, veterinary monitoring, and animal welfare monitoring by attributing vocalizations and behaviors to the correct individual. Real-world videos are challenging because multiple dogs may bark simultaneously, become occluded, or move in and out of view. Prior studies show that canine vocalizations and visual appearance contain discriminative identity information, but these modalities have largely been studied independently. We present a multimodal dog-fingerprinting framework combining visual identification, multiple-object tracking, and canine vocal fingerprinting to associate bark events with individual dogs while maintaining persistent profiles. The framework synchronizes bark events with tracked dogs and updates profiles using visual appearance and vocal characteristics, enabling identification despite occlusion, overlapping vocalizations, and off-screen barking. We also introduce a benchmark of 46 real-world videos containing 213 manually annotated bark events. Our framework correctly localizes the active visible dog in 61.83% of visible events at IoU $\geq 0.30$ and achieves a 91.33% F1 score for visible versus off-screen barking detection.

---


### 64. [Blind Watermarking of Software Repositories via Module Placement](https://arxiv.org/abs/2610.21031)

**<font color=#1a73e8>作者：</font>** Khadija Mohamed, Khaled Fathy, Mamdouh Farouk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Source-code watermarking supports provenance tracking by embedding a recoverable identifier in a software artifact. Many existing approaches encode this identifier in tokens or program syntax, exposing the watermark to transformations that modify the source text. We present PlaceMark, a blind watermarking system that encodes a payload in the placement of modules within a repository. Each eligible module is identified by its filename and top-level definition names. A secret key determines its ordered candidate destinations and its position in the reading order; the module's location within its candidate list determines the encoded symbol. Embedding relocates selected modules and updates their import references. Extraction uses the distributed repository, the key, and agreed decoding parameters, without an original copy or placement ledger. Capacity measurements on ten Python repositories yield nominal capacities of 249 to 2,166 bits in nine repositories, while one provides no placement channel. In 216 trials of the evaluated text transformations, the payload is recovered exactly. Relocation degrades recovery gradually on Django, Airflow and Salt, while on Pylint a path-based exclusion in our implementation lets relocation change carrier membership, and we measure it for an untargeted adversary and for one that concentrates its budget on the public carrier set. Changes to filenames or definition names alter the identity input and are measured separately. Exact recovery also depends on placement feasibility. The results characterize module placement as a carrier that can complement watermarks embedded in source text.

---


### 65. [Can Autonomous Vehicles Keep Their Cool? A Survey of Thermal Side-Channel and Perception Attacks](https://arxiv.org/abs/2610.21034)

**<font color=#1a73e8>作者：</font>** Harsh Aaryan, Ce Zhou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles (AVs) couple safety-critical perception to thermally constrained compute. Interfaces built for night perception and package thermal reliability were never engineered as confidentiality boundaries, and closing one such path leaves the other intact. Physical adversaries can spoof thermal infrared (IR) sensors used for night driving, while unprivileged software co-tenants can fingerprint perception workloads from thermal, dynamic voltage and frequency scaling (DVFS), and thermal event interrupt (TEI) telemetry required for package safety. These paths differ in mechanism and privilege; both exploit interfaces that AV stacks cannot disable without compromising Safety of the Intended Functionality (SOTIF). Classical microarchitectural and cyber-physical systems (CPS) surveys address cache timing, adversarial machine learning, and camera or LiDAR spoofing; no prior survey jointly frames physical thermal IR attacks and unprivileged silicon thermal telemetry as one residual-risk class. This survey systematizes thirteen representative works into thermal perception integrity, telemetry leakage, and model-information extraction, comparing them by privilege, timescale, co-tenancy, deployability, and AV relevance. We distinguish attack family from adversary class and map defenses to residual risk while thermal management remains operational. A commodity proxy supports the software co-tenant branch only; physical IR evidence comes from cited literature. We identify open problems in on-target automotive evaluation, fusion trust under IR spoofing, chiplet thermal coupling, capability-based telemetry, and standards-ready threat analysis, aiming to motivate co-design across sensors, operating systems, silicon, and automotive standards.

---


### 66. [Recursive Reward Improvement via Adversarial Meta-Prompt Evolution](https://arxiv.org/abs/2610.21040)

**<font color=#1a73e8>作者：</font>** Wei Dai, Qianchu Liu, Guanghui Qin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive Self-Improvement (RSI) has gained wide attention for its ability to work with limited data. In a proposer-solver loop, a proposer model writes training tasks and a solver model learns to solve them through reinforcement learning. Such loops have succeeded in mathematics and coding, where every answer can be checked automatically. Open-ended expert tasks, like clinical report generations, have no answer key, which makes simple question-answer generation not viable. Here the proposer must also write a rubric that lists the content an answer should include and the errors it should avoid. However, the unique challenge behind model-written rubric is the comprehensiveness of it. For naively generated rubric, solvers tend to exploit it, naming the expected topics without the substance behind them, which corrupts the learning process. To solve this problem, we introduce RRI, Recursive Reward Improvement, which uses a reward hacking adversary to supervise the reward. Before the solver trains on a generated task, an adversary writes an answer that games its rubric while being as useless as possible, the same model writes an honest answer without seeing the rubric, and up to two repair steps revise the rubric to make the honest answer win. The exploits found also rewrite how future tasks and rubrics are generated. On HealthBench Professional, RRI improves the adjusted score over the Generation Only self-improvement baseline by 10.9 points at 9B and 12.4 at 27B, and by 10.3 points without any external model. In particular, the gains are largest on difficult and writing tasks. We show that the 27B model trained on the HealthBench Professional description improves by 6.6 points on PRBench Hard and 8.0 on ProfBench without seeing a task from either. We further analyze the exploitable points of model-generated question-rubric pairs to facilitate future research on open-ended self-play.

---


### 67. [SHIP: Structured and Hierarchical Insight with Privacy](https://arxiv.org/abs/2610.21048)

**<font color=#1a73e8>作者：</font>** Kai Chen, Guisi Ni, Albert Cheu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracting insights from textual data while protecting user privacy is increasingly important. Existing methods produce private insights in diverse forms for different analytical purposes, making their utility difficult to assess and compare. In this work, we formulate differentially private (DP) insights as reusable representations for answering analytical queries, providing a common basis for utility assessment. Answering these queries, however, requires fine-grained details and cross-attribute statistics that existing representations may omit. To capture this information, we introduce Structured and Hierarchical Insight with Privacy (SHIP), which automatically maps queries to attributes, builds a hierarchical hybrid taxonomy, and releases a DP synthetic table for further analysis. We also develop an evaluation protocol based primarily on QA performance and structured fidelity. Our experiments demonstrate SHIP's strong performance on both measures relative to existing private insight baselines, while identifying queries that remain challenging for structured representations.

---


### 68. [SALTO: Solver-Anchored Lifted Transfer Operators for Nonlinear Event Inference](https://arxiv.org/abs/2610.21049)

**<font color=#1a73e8>作者：</font>** Qi Wang, Rylie Foster  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned dynamical models can accurately predict trajectories while producing unreliable sensitivities when differentiated or transposed, limiting their use in inverse problems and scientific decision-making. Classical adjoints provide exact local derivatives, but a single adjoint cannot represent the nonlinear response of a system to a family of finite-amplitude perturbations. We introduce SALTO (Solver-Anchored Lifted Transfer Operators), a Koopman-based framework for inferring finite-amplitude sources. In the lifted space, the nonlinear dynamics are approximated by a linear propagator, and its transpose carries each sensor backward in a single solve. The result is a reusable lifted adjoint that predicts the measurement produced by any candidate localized event with one encoder pass and an inner product. To give the model the simulator's exact local behavior, SALTO imposes three structural constraints: it anchors the physical-state dynamics to the simulator's linearized propagator, centers the learned observables so that they vanish to second order at the reference state, and uses a block-triangular lifted propagator. These constraints guarantee that the model reduces to the simulator's tangent dynamics and classical adjoint as the amplitude vanishes, while the learned observables carry only the finite-amplitude correction. On three nonlinear PDE systems, SALTO predicts the measurements of finite-amplitude sources to within 2-8% where the classical adjoint is in error by 41-165%, recovers source position and intensity from sparse sensors nearly as accurately as inversion through the solver, and samples the joint posterior of two interacting sources, matching the solver's posterior on reaction-diffusion at a twentieth of its cost. One trained model serves new sensor layouts and measurement times with a single backward solve.

---


### 69. [NOMAI: Scalable Federated Learning with Private Weights](https://arxiv.org/abs/2610.21059)

**<font color=#1a73e8>作者：</font>** Yiyi Sun, Mushtari Sadia, Amrita Roy Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The twin goals of privacy-preserving federated learning (FL) -- harnessing distributed data while protecting the parties who contribute it -- demands three properties: model privacy, data privacy, and integrity. Achieving all three in a realistic deployment -- with a single coordinator and millions of users -- remains an open challenge that prior work has yet to fully resolve. We present NOMAI, the first scalable MPC-based FL system to provide all three guarantees simultaneously. NOMAI operates under an honest-majority assumption in the semi-honest model, with an extension to the malicious-with-abort setting. At its core, NOMAI combines a multi-committee MPC architecture with packed Shamir secret sharing, enabling SIMD-style secure computation that scales far beyond what monolithic n-party protocols can support. We further introduce ML-aware optimizations and new cryptographic primitives that substantially reduce per-user overhead. Our evaluation shows NOMAI is practically deployable at unprecedented scale: it reduces per-user computation to just <350 ms (semi-honest) and <700 ms (malicious) for per iteration of training MNIST, achieving three orders-of-magnitude improvements over prior work while seamlessly supporting populations of over 106 users. This demonstrates, for the first time, that MPC-based FL can meet the scale demands of real-world systems without compromising on privacy or integrity.

---


### 70. [OmicsBench: a long-horizon multi-turn benchmark of AI agents on research-study-scale bioinformatics](https://arxiv.org/abs/2610.21074)

**<font color=#1a73e8>作者：</font>** Gideon Shaked, Siddharth Nagisetty  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computational biologists increasingly delegate substantial analyses to AI agents in long-horizon, multi-turn sessions, yet most benchmarks of agents' bioinformatics capabilities pose a single short task with a single-shot prompt. We present OmicsBench, a long-horizon, multi-turn bioinformatics benchmark for AI agents. Each of its 97 tasks links dependent subtasks into a directed acyclic graph, for 662 underlying subtasks in all. Each subtask is posed as one user turn and graded deterministically against an answer key, with optional in-context feedback on incorrect answers. Across 12 models on three harnesses, the slowest agent averages 3.6 hours per task, and no combination comes near saturating the benchmark, with mean scores of 0.43 to 0.57 out of a possible 1 without in-context feedback and 0.54 to 0.67 with it. Multi-turn evaluation also uncovers behavior that single-shot prompts cannot, as agents score lower on subtasks that depend on earlier subtasks, and in-context feedback helps agents recover some of that loss. Because deterministic scoring gives no qualitative account of how an agent failed, we also introduce an unsupervised failure mode discovery pipeline that describes, embeds, and clusters agents' failed attempts to surface emergent failure modes. Applied to OmicsBench, this pipeline exposes qualitative shortcomings in how agents carry out bioinformatics analyses, ranging from agents applying their own statistical filters in place of the specified ones to agents writing whole answers from memory.

---


### 71. [StochLOB: Heavy-Tailed Score Matching for Robust Limit Order Book Trend Prediction](https://arxiv.org/abs/2610.21081)

**<font color=#1a73e8>作者：</font>** Arshia Abolghasemi, Seyed Reza Tavakoli, Parsa Naderi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based diffusion methods usually perturb data with Brownian Gaussian noise, corresponding to a light-tailed forward stochastic differential equation (SDE). For market time series this SDE can be a poor abstraction: limit order book (LOB) order flow is heavy-tailed, bursty, and occasionally jump-like. We study STOCHLOB, a training-only score-matching framework that changes the forward diffusion corruption law while leaving the deployed predictor deterministic. Instead of Brownian-only Gaussian corruption, the noising process uses two non-Gaussian SDE-inspired alternatives: jump-Lévy noise through a compound-Poisson variance mixture, and clipped $\alpha$-stable noise through a positive-stable Gaussian scale mixture. These corruptions inject finite jumps and heavy-tailed residuals into training without requiring reverse-time diffusion sampling at inference. The resulting score target has a useful interpretation: its radial factor $h_t(r)$ is the posterior expected corruption precision, so large residuals are weighted according to the latent corruption scale that most plausibly generated them. On chronologically held-out Coinbase LOB data, the proposed variants remain competitive on uncorrupted BTC and altcoin test horizons and improve several realized tail-window stress diagnostics. An exploratory Feishu A-share transfer study further tests whether the probability outputs remain usable under transaction costs and trading-rule constraints. Code and configuration files are available at this https URL.

---


### 72. [RoPE-Flow: Monocular Vision-based Robot Pose Estimation via 2D Graph-Conditioned 3D Flow Matching](https://arxiv.org/abs/2610.21086)

**<font color=#1a73e8>作者：</font>** Liangjing Shao, Wanhao Liu, Zhiwei Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-to-robot pose estimation from a monocular image is significant for vision-based robot navigation and control. However, recovering 3D structural features from 2D observations remains a challenging task. Existing camera-to-robot pose estimation methods either rely on time-consuming iterative rendering or involve sophisticated 2D-3D registration which suffers from projection ambiguity, accumulated errors for distal joints and imbalanced learning for different joints. In this work, we propose RoPE-Flow, an end-to-end flow matching-based framework for camera-to-robot pose estimation. From the predicted 2D heatmaps, we propose a Keypoint-centered Feature Extractor to obtain positional features along with contextual representations from keypoints-centered multi-scale patches. Moreover, we introduce Graph-guided Condition Generator, which embeds a learnable adjacency map to generate condition for flow matching based on correlation among keypoints. Besides, we introduce Bone Length Loss and Ray-Depth Loss for topological consistency and scale stability, with joint-wise weighting to mitigate varied prediction difficulty across joints. The proposed method outperforms state-of-the-art methods for pose estimation across different types of robots with mutiple cameras. Besides, we establish a novel cross-scene benchmark to demonstrate the outstanding performance of RoPE-Flow on zero-shot cross-scene robot pose estimation. Meanwhile, animated visualizations are shown on the website: this http URL

---


### 73. [SIEVE: Overcoming Topological Obstruction in Equivariant Self-Supervised Learning](https://arxiv.org/abs/2610.21087)

**<font color=#1a73e8>作者：</font>** Jongann Lee, Sun Woo Park, Yun Young Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We identify a theoretical incompatibility between 3D point cloud masked autoencoding and SE(3)-equivariant networks. We prove that standard masking triggers a topological collapse, effectively forcing the model to hallucinate orientation without a reference frame. To resolve this, we introduce SIEVE (Scalar Invariant Extraction Via Equivariance), an SE(3)-equivariant self-supervised framework that compresses point cloud geometry into invariant scalar embeddings. At its core is the spherical projection mask, which preserves global pose while obfuscating local semantics, sidestepping the obstruction by construction. Experiments confirm that SIEVE circumvents the predicted collapse where constant and noise masks fail. On downstream point cloud tasks, the resulting embeddings improve over coordinate-based baselines and hand-crafted geometric descriptors, with the largest gains on generalization to unseen shape categories.

---


### 74. [Probe-and-Resume: When and How to Evaluate Agent Execution](https://arxiv.org/abs/2610.21088)

**<font color=#1a73e8>作者：</font>** Jiakai Xu, Tiancheng Ge, Tujie Guan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time search can improve agent performance by exploring alternative actions and using a critic to select promising branches. We study this approach in terminal-based computer-use environments, which expose only a partial view of a large underlying state, and find that the Monte Carlo tree search (MCTS) configuration we evaluate does not significantly improve task success. We identify two sources of poor critic performance: the agent's observations omit environment state needed for evaluation, and intermediate states offer limited evidence of whether a trajectory will succeed. At intermediate states, critics rank continuations only modestly better than chance, and environment access improves this little. We study when to invoke a critic and what access to give it to evaluate a node. Our findings motivate a policy that invokes the critic only at nodes the agent believes are final, rather than during partial progress. Further, the policy gives the critic read, write, and execute access to a fork of the computer's current and initial state, allowing it to probe and perform potentially destructive actions to surface any hidden state the trajectory omits. We call the resulting design Probe-and-Resume: when the agent claims to be done, the critic probes a fork of its state, and a rejected agent resumes where it stopped. On Terminal-Bench 2.1, this raises success by 8.4 percentage points over MCTS with conventional critics, and approaches the success rate of the Codex CLI agent with the same underlying model at less than half its cost.

---


### 75. [RoboCloth: A Large-Scale Real Cloth Material Dataset for Neural Reflectance Reconstruction](https://arxiv.org/abs/2610.21090)

**<font color=#1a73e8>作者：</font>** Zhen Li, Haoran Qin, Francesco Di Sario 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present RoboCloth, a dataset of 500 real cloth materials captured under flexible, calibrated camera and lighting configurations, where both are robotically controlled during acquisition. Each material is imaged in approximately 580 high-dynamic range frames spanning a wide view-light hemisphere; camera poses are refined via structure-from-motion and aligned to the robot frame, yielding per-material sparse surface geometry and structured per-point reflectance observations ready for neural material training. We demonstrate the value of this data through a two-stage neural reconstruction pipeline: Stage 1 trains a shared MLP decoder on our corpus to learn cloth material priors; Stage 2 then freezes the decoder and fits a dense 2048x2048 latent texture to each target material. Evaluating on held-out materials from our own dataset and on the independent UBO2014 benchmark, we show that a decoder trained on our captures outperforms decoders trained on existing measured reflectance datasets and analytic PBR fitting, transferring to unseen acquisition systems without modification. The dataset, calibration files, observation tensors, and train/test splits are released under CC BY 4.0 on the Hugging Face Hub.

---


### 76. [Can World and Action Modeling Benefit Each Other under Unified Causal Training?](https://arxiv.org/abs/2610.21095)

**<font color=#1a73e8>作者：</font>** Yue Su, Bokai Lin, Xinkai Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World and action modeling are closely related, yet their reciprocal benefits under unified causal training remain unclear. We introduce OneWM, a simple framework for unified causal training that treats actions as both conditions for world prediction and targets for policy learning within a shared video-action architecture. Using this framework, we investigate whether learning forward dynamics conditioned on specified actions improves action learning, and whether learning to generate actions in turn improves action-conditioned world modeling. We use LIBERO, LIBERO-Plus, and RoboCasa365 as embodied testbeds to evaluate both policy learning and world modeling, complemented by real-world policy experiments. Learning the visual consequences of specified actions improves policy performance and generalization across changing scenes. In turn, action learning improves multi-view world-prediction fidelity under the same architecture. Together, these results answer both questions positively, supporting reciprocal benefits between world modeling and action generation under unified causal training.

---


### 77. [ToolBottleneckBench: Measuring Tool-Agent Performance under Controlled Pressures and Fixed Harness Budgets](https://arxiv.org/abs/2610.21098)

**<font color=#1a73e8>作者：</font>** Zichuan Xu, Yuyang Dong, Makoto Onizuka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The success score of a tool agent reflects both its model and the budgets of the harness that runs it. We present ToolBottleneckBench, a benchmark that measures tool-agent performance under controlled pressures and fixed harness budgets. Synthetic enterprise tasks stay fixed while one pressure varies: the registered tool catalog, the visible tool menu, the certified workflow, or the encoding of returned records. An exact grader records the first unmet obligation of each failed episode and the harness limit, if any, that ended it. Across 21 model and harness configurations, the visible menu is the only one of the three pressures that act on the model with a large penalty, and this penalty tracks truncation at the completion cap. Raising the cap sixteenfold removes most of the penalty in the truncation-heavy configurations. Most failures end at a harness limit, and the failure record identifies the assigned pressure no more reliably than a count of tool calls. The repairs that help change which tools reach the model or who issues the calls, and only two repairs, neither improving model behavior, beat every configuration switch. We recommend reporting pressure effects with the harness budgets under which they were measured. We release the benchmark at this https URL.

---


### 78. [Kolab: Benchmarking Human-Agent Collaboration in Long-Horizon Workflows](https://arxiv.org/abs/2610.21109)

**<font color=#1a73e8>作者：</font>** Shirley Anugrah Hayati, Patricia Anugrah Setiani, Ruizi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When humans collaborate with AI agents on long-horizon tasks, what happens to the agents' contributions? For solving long-horizon tasks, humans place greater importance on ongoing interaction with AI agents (e.g., revising plans) than on an agent's ability to complete the task in a single attempt. However, most agentic benchmarks have focused more on automation. Strong performance on such benchmarks does not imply effective real-world collaboration. Professional workflows offer a useful setting, as they often involve interdependent steps. To address this gap, we introduce Kolab, a new dataset of 115+ hours of screen recordings of 50 professionals from 40 occupations collaborating with agents on realistic, long-horizon problems. Kolab also contains participants' collaboration and output quality judgments. Our analysis reveals diverse collaboration patterns, highlighting the importance of when and how professionals coordinate with agents. A collaborative agent must do two things that automation benchmarks never test: anticipate whether experts will adopt, modify, or reject its contribution once it leaves the chat window to guide its next steps, and assess collaboration quality from the unfolding workflow without constant expert feedback. Our benchmark operationalizes both: (1) forecasting how professionals use agent contributions at diverse workflows, and (2) verifying their judgments of collaboration satisfaction and output quality. Findings show that frontier models, both agentic and non-agentic, overestimate collaboration with experts and struggle to distinguish between high- and low-quality collaboration. Longer workflow context does not consistently improve these predictions. As frontier agents cannot yet understand long-horizon collaboration with experts, we position Kolab as a valuable dataset for studying human-agent collaboration grounded in real professional workflows.

---


### 79. [Spectral-Spatial Interpretation](https://arxiv.org/abs/2610.21114)

**<font color=#1a73e8>作者：</font>** Haotian Ma, Ruqi Yang, Philip Townsend  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc image explanations usually show where a model looks using spatial heatmaps or indicate which channels matter using global channel scores. These separate views are limiting for multispectral data because channel relevance is often spatially localized and physically meaningful. We introduce Spectral-Spatial Interpretation (SSI), a full-grid attribution method over position-channel players (g,c). For each spatial position, SSI fixes the observed surrounding context, defines a conditional game over the channels at that position, and applies the Shapley value to this local game. The result is a full spectral-spatial attribution matrix rather than a single heatmap or a global channel ranking. SSI has a clear local interpretation. It satisfies Shapley fairness within each position, and aggregating its channel attributions exactly recovers the position-level contextual contrast obtained by replacing that position with the baseline. SSI also differs from context-averaged Owen-style hierarchical accounting, which uses the same position-channel grouping but averages over external spatial coalitions. On HLS Burn Scar, SSI outperforms an MC-Owen estimator across retained attribution metrics while using only about 6% of its evaluation budget. Across CUB-200, EuroSAT, and HLS Burn Scar under both per-channel mean and zero baselines, SSI achieves the best joint deletion and insertion AUC over dense, flat, and rank-1 baselines, yields the strongest spectral hit rates and channel deletion, and leads spatial localization on both annotated datasets. Code is available at this https URL.

---


### 80. [DST-Net: Decomposed Spatio-Temporal Network for Time Series Forecasting](https://arxiv.org/abs/2610.21123)

**<font color=#1a73e8>作者：</font>** Yaohua Zha, Hai Wu, Shu-Tao Xia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Series decomposition has emerged as a widely acknowledged paradigm in deep time series forecasting models. However, existing approaches predominantly employ a homogeneous modeling strategy for all subsequences, thereby overlooking the distinct inductive biases inherent in different components. We identify that the trend component exhibits dominant spatial coupling across channels but carries significant temporal redundancy, whereas the seasonal component is characterized by local temporal evolution but remains susceptible to attention distraction. To address this, we propose a novel disentangled architecture that tailors specific modeling strategies to align with the intrinsic properties of each component. For the trend branch, we design a Latent Graph Block, employing latent graph modeling to capture global topological dependencies and system-wide co-movements. Conversely, for the seasonal branch, we introduce a Gaussian Multi-scale Attention mechanism to mitigate attention distraction. By injecting learnable Gaussian priors, we impose structural constraints that compel the model to focus on multi-granular local contexts, effectively filtering out global noise and accurately capturing local evolutionary phases. Extensive experiments on multiple real-world benchmarks demonstrate the effectiveness of our proposed model.

---


### 81. [Reaction Attack on CKKS Deployments with Asymptotically Optimal Query Complexity](https://arxiv.org/abs/2610.21127)

**<font color=#1a73e8>作者：</font>** Song Bian, Hyeongmin Choe, Jiseung Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study a protocol-level reaction leakage in CKKS deployments where public coefficient-to-slot (C2S) evaluation keys are combined with a client's 1-bit validity response. Under this deployment surface, a malicious evaluator can recover a ternary secret key using asymptotically optimal $O(H)$ reaction queries, where $H$ is the entropy of the secret key.
The attack does not break RLWE or CKKS IND-CPA security. Instead, it exploits the interaction between client-side validity reactions and public homomorphic linear transformations. A shift of a public encryption key yields a ciphertext whose plaintext is a function of the secret key; the public ${\sf C2S}$ layer then repacks this information to construct a ciphertext whose validity depends strictly on whether a targeted secret coefficient matches a guessed value. Furthermore, each submitted query is independently randomized with a fresh encryption of zero, so that each resulting malicious ciphertext appears entirely distinct, thereby allowing the attack to simply evade trivial detection mechanisms on the client side.
We implemented the full end-to-end attack in Lattigo v6.2.0 and recovered the full secret key across four parameter sets drawn from standard CKKS presets. For uniform ternary secrets, the attack uses $O(N)$ queries and is within a factor $2/\log_2 3 < 2$ of the oracle-only entropy lower bound. For sparse ternary secrets, a tailored variant further reduces the number of queries in practice. Our results show that observable validity reactions form a practical key-recovery channel in CKKS deployments exposing this surface, even when the underlying cryptographic assumptions remain intact.

---


### 82. [When Judges Agree and Are Wrong: Consistency-Accuracy Dissociation as a Blind Spot for Label-Free Evaluation](https://arxiv.org/abs/2610.21128)

**<font color=#1a73e8>作者：</font>** Xiang Zhang, Lovedeep Gondara, Jekaterina Novikova  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Label-free evaluation methods, such as self-consistency filtering, majority-vote aggregation, and agreement-based reliability scoring, rely on an implicit assumption that consistency can serve as a proxy for correctness when ground-truth labels are unavailable or expensive to obtain. In this paper, we test this assumption directly. Using four financial QA datasets (multiple-choice and free-form), ten consistency dimensions, and two frontier model families, we measure the joint distribution of consistency and accuracy at the level of individual examples rather than in aggregate. We find that 60% of all incorrect answers fall in the high-consistency region (consistency $\geq$ 0.8), and that 77.7% of these show complete answer collapse, i.e. identical wrong answers across all perturbation variants. This high-consistency/incorrect quadrant cannot be detected by any evaluation signal that is built on agreement alone, as the model appears maximally reliable while being wrong. We show that the phenomenon is robust to the choice of consistency threshold t (it persists from t=0.50 to t=1.00), is shared across model families, and is concentrated in specific intersections of perturbation dimension and domain. We map where this quadrant occurs, analyze its stability properties, and discuss the implications for evaluation pipelines that use agreement-based signals in place of human labels.

---


### 83. [Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search](https://arxiv.org/abs/2610.21129)

**<font color=#1a73e8>作者：</font>** Yun Dai, Yuyun Chen, Jiarui Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) dominate video generation but suffer from high inference cost due to the quadratic complexity of self-attention. Sparse attention mitigates this by skipping unnecessary computation in the attention matrix, but existing methods apply a fixed sparsity ratio throughout denoising and struggle to accurately determine which computations to skip. To address these limitations, we analyze attention dynamics through attention entropy and mean attention distance, and find that attention becomes increasingly concentrated across denoising steps. We further observe that blocks selected early continue to capture a large fraction of the total attention weight at later steps. These findings suggest two acceleration opportunities: the sparsity ratio should grow as denoising progresses, and earlier search results can be reused to reduce the search space. Based on these findings, we propose Growing Sparsity and Reduced Search (GSRS), a training-free framework that retains more computation early and progressively reduces it later, while restricting subsequent searches to an early candidate set to reduce search overhead. GSRS adopts Top-p selection for adaptive sparsity control, supported by a precise evaluation scheme that computes exact attention weights within the FlashAttention computation at negligible overhead. Experiments on HunyuanVideo and Wan 2.1 validate that GSRS achieves 1.55$\times$--2.21$\times$ speedup while maintaining generation quality comparable to full attention.

---


### 84. [Trajectory Prediction Method for person under WSN with Hierarchical Envelope Adversarial Domain Adaptation](https://arxiv.org/abs/2610.21132)

**<font color=#1a73e8>作者：</font>** Wenqian Jiang, Qifeng Sun, Xiaosong Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian trajectory prediction holds significant applications across autonomous driving, intelligent surveillance, and smart cities. However, the complexity and unpredictability of pedestrian interactions make this task a persistent challenge. Current models face two common limitations: 1) Consider only a single type of social coupling. This introduces redundant interactions. More critically, it fails to account for the varying nature of trajectory coupled across different scenarios and between different pedestrians. Consequently, models cannot deeply adapt to diverse scenes. 2) Inadequate domain shift handling. Although very few methods address domain shift, they rely on statistical criterion-based domain distribution alignment. Such approaches exhibit strong dependency on predefined statistical metrics. This leads to significant limitations in complex and dynamic environments. To address these problems, a Hierarchical Envelope Adversarial Domain Adaptation with Loosely-Tightly coupled model (HEADA-LTCTPM) is proposed. First, an envelope sample construction mechanism was proposed. It constructs envelope samples and extends them into graph structures. Secondly, an adversarial domain adaptation module was proposed. This integrates both local and global domain adaptation strategies. It dynamically adapts to diverse coupled relationships across scenarios. These innovations collectively enhance prediction accuracy and robustness. In the experimental section, two representative public datasets were employed for validation and comprehensive comparisons with six relevant baseline algorithms were conducted. Results demonstrate that our model achieves significantly higher accuracy compared to existing methods, with the ADE and FDE metrics reduced by 17.6% and 19.1% respectively. The time overhead meets practical requirements, which verifies the effectiveness of our key innovations.

---


### 85. [CoSTA: Compressed Speech Token Adaptation for Efficient Spoken Dialogue Models](https://arxiv.org/abs/2610.21143)

**<font color=#1a73e8>作者：</font>** Yingzhuo Deng, Chong Li, Bingxin Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spoken Dialogue Models (SDMs) typically share a speech-token space for generation and synthesis, leading to long autoregressive sequences and costly inference. Lower-rate speech tokenizers shorten sequences but may introduce compression-quality trade-offs and costly replacement without breaking this coupling. To address this limitation, we propose CoSTA, a compatibility-preserving post-hoc framework that decouples generation and synthesis token spaces while retaining the original speech tokenizer and decoder. CoSTA extends the generation token space with compressed representations via mean-initialized vocabulary extension, pronunciation adaptation, and dialogue adaptation, followed by deterministic expansion back to the original speech-token space before synthesis. On bilingual speech-dialogue benchmarks, CoSTA achieves approximately $1.7\times$ expanded speech-token generation speed, lower full-response latency, and higher throughput while preserving response quality. Analyses show more sustained interaction under limited budgets and a practical trade-off among compression, decoding efficiency, and quality. Further experiments demonstrate cross-architecture transfer and complementarity to low-rate tokenization.

---


### 86. [ExecWeave: Cross-Layer Execution Provenance for Observable Agentic Software](https://arxiv.org/abs/2610.21146)

**<font color=#1a73e8>作者：</font>** Guo-Wei Wong, Meng Chang Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic software invokes tools, launches processes, accesses files, and communicates with local or remote services. Application traces describe logical operations, whereas operating-system telemetry records machine activity without necessarily identifying the responsible agent action. Relating these evidence planes is a reconstruction problem: a plausible but unsupported association can assign an effect to the wrong principal.
We present ExecWeave, a local-first system that materializes provider semantics and independently observed runtime events into a typed execution graph. The implementation retains separate source artifacts, distinguishes logical occurrences from repeated evidence, and records attribution, inference, and causal-status metadata. An optional command-to-process correlator emits a non-causal inferred bridge only when its bounded search yields one compatible observed process; uniqueness within this observed candidate set is not a guarantee of causal correctness. OS-observed file and network effects acquire a semantic tool or agent principal only through an observed process plus a justified command-to-process association; session-correlated file-system events do not by themselves provide that principal.
Source code is available at this https URL.

---


### 87. [Stop Training Against Soft Users: Mentalized Adversarial Self-Play for Proactive Dialogue](https://arxiv.org/abs/2610.21156)

**<font color=#1a73e8>作者：</font>** Zanwu Liu, Dan Zhang, Xiaodi Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Proactive dialogue agents must guide multi-turn interactions toward task goals while adapting to users whose intentions and attitudes evolve. Existing planners improve system side action selection through search, learned policies, or user aware planning, but are often trained and evaluated against fixed or overly compliant simulators; as a result, high simulated success can reflect soft user bias rather than robust dialogue ability. We introduce MASP, a Mentalized Adversarial Self Play framework that treats proactive dialogue as a partially observable game between a system and a rationally resisting user. MASP represents the user's evolving mental state with a BDI based latent state, separates reward side teacher mentalization from policy side student mentalization, and alternates self play updates for the system and user policies. This turns robustness to rational resistance into a training objective rather than only an evaluation condition. Across diverse proactive dialogue benchmarks, compared with the widely used SFT and Planner-only approaches, MASP substantially improves success rate (SR) and rationality constrained success (RCSR), reduces average turns (AT), and performs better against hard users who make the task goal more difficult to achieve.

---


### 88. [Automatic Sentence Completion Using Bengali Audio Speech with a Transformer-Based Early Speech Recognition System](https://arxiv.org/abs/2610.21164)

**<font color=#1a73e8>作者：</font>** Md Asif Akram, Arif Faisal, Sakir Hossain Faruque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dementia severely impairs communication abilities and turns everyday conversations into challenging experiences. Individuals affected by dementia frequently struggle to express their thoughts or complete sentences, making it difficult for family members and caregivers to understand their needs. This study proposes a novel approach to assist dementia patients by developing an integrated system that detects signs of dementia through Bangla speech and text analysis and provides sentence auto-completion support during conversations. To achieve this, recorded voices from individuals with and without dementia were analysed, and key acoustic features were extracted to capture vocal patterns associated with cognitive decline. A transformer-based model was employed to transcribe voice signals into text for linguistic analysis. In the classification task, several Machine Learning (ML) and Deep Learning (DL) models were evaluated using both acoustic and textual representations, and the LSTM model architectures demonstrated strong capabilities for modelling contextual patterns in speech and language data. For the sentence auto-completion task, a sequential learning model based on a Bidirectional LSTM (Bi-LSTM) network with an attention mechanism was developed to sequentially complete partially expressed Bangla sentences during conversation. This research bridges the gap in dementia analysis in an underrepresented language and implements a sentence auto-completion framework for cognitive disorders.

---


### 89. [GRADS: Graph-Regulated Agentic Data Synthesis with Controllable Difficulty](https://arxiv.org/abs/2610.21167)

**<font color=#1a73e8>作者：</font>** Gaocheng Yang, Ruijie Tao, Kai Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research agents are increasingly deployed to retrieve precise information from large corpora, yet multi-hop, long-horizon tasks remain challenging. Synthetic data generation has emerged as a scalable solution, with existing pipelines typically expanding seed tasks to increase their apparent depth and breadth. However, this expansion does not reliably translate into necessary reasoning: newly introduced evidence may be only weakly coupled to the answer, creating a mismatch between intended and empirical difficulty. To address this problem, we introduce GRADS, a graph-guided agentic data synthesis framework with explicit difficulty control. GRADS runs a closed loop of seed selection, evidence expansion, question--answer construction, and verification while maintaining a graph of the evidence and inference dependencies required to derive each answer. At each step, it conditions generation on a relevant subgraph, preserving indispensable inference without accumulating irrelevant context. Experiments across security, software-engineering, and scientific-document domains show that GRADS consistently generates verified tasks with empirically separated difficulty distributions, as measured by independent solvers. Moreover, under matched training budgets, post-training on this data delivers consistent gains at every level: SFT raises the solution-termination rate to over 95% while cutting tool calls and turns by up to 75%, RL trims tool use by up to a further 19.5%, and on our held-out, domain-specific benchmarks, the resulting 4B model matches Sonnet~4 on software engineering and surpasses it on the scientific and security domains.

---


### 90. [AgentEval: Evidence-Bounded Assessment of Stateful Agents](https://arxiv.org/abs/2610.21177)

**<font color=#1a73e8>作者：</font>** Ruiqi Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Task completion alone does not determine whether a stateful agent satisfied its obligations, and a recorded judgment does not guarantee that its supporting evidence remains valid. We present AgentEval, a system that carries a contract-bound assessment record through tool execution, state and event capture, report qualification, and case maintenance. It separates what the agent did, what the evidence establishes, and whether the conclusion is supported for present use. On 32 tool-world administrations, independent checks agree on all 30 complete episodes, distinguishing satisfied, violated, and unresolved obligations; two interrupted administrations are retained. Controlled interventions on 48 evidence views expose 36 binding faults missed by hash-only checks without changing agent behavior. Scenario Studio connects reviewed cases to 12 two-turn reports with 24 independently checked answers. A separate public-benchmark study on 192 held-out executions reveals ten completed return subgoals within broader task failures and isolates the effect of missing evidence. These studies show how an executable assessment record makes scope, evidential support, and report reuse inspectable across an agent evaluation workflow.

---


### 91. [Mine, Sample, Render: Test-Time Diversity Alignment Of Generative Models](https://arxiv.org/abs/2610.21185)

**<font color=#1a73e8>作者：</font>** Kostas Triaridis, Morris E. Sharp, Nebojsa Jojic  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern generative models produce high-quality individual outputs but struggle to sample diversely, even when explicitly instructed to do so. We introduce MINE-SAMPLE-RENDER (MSR), a test-time approach that externalizes the diversity into an explicit, corpus-derived sampling procedure. Our pipeline (i) mines an interpretable categorical schema from a corpus of real artifacts and supplies statistics for sampling; (ii) samples attribute configurations from the corpus-derived statistics; (iii) uses a generative model purely as a conditional renderer of a sampled configuration. Across weather report generation, user simulation, webpage design, text-to-image generation, and agent-generated 3D assets, we evaluate the diversity and output quality of MSR-guided generation and show that MSR improves alignment with corpus distributions and diversity of generated outputs.

---


### 92. [Sensor Diagnosis for Fuel and Emissions Monitoring in Heavy-Duty Diesel Vehicles](https://arxiv.org/abs/2610.21188)

**<font color=#1a73e8>作者：</font>** Tejas Dahiya, Saurabh Kumar Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Faulty sensor readings can distort estimates of fuel use and carbon dioxide emissions from diesel engines. We evaluate two procedures that use relationships learned from healthy measurements to diagnose faults and guide fuel correction. The diagnosis procedure tests whether replacing a suspected faulty reading with an estimated healthy value helps a model predict another sensor's recorded reading more accurately. It then predicts the fault type and decides whether to report the diagnosis. We evaluate five synthetic fault types on 217 steady-state operating points from a heavy-duty diesel engine, excluding all measurements at selected engine speeds from training. Across 31,500 fault-injected groups of 20 operating points, it issues diagnoses for 77.3% of groups, with 92.1% of diagnoses issued on these groups correct. The fuel correction procedure uses a different sensor-selection rule at individual operating points, testing how each replacement changes the largest prediction error across all six sensors. Fuel correction requires a fault alarm and engine speed and torque close to the training conditions. A fuel reading is replaced only when its replacement reduces the largest prediction error sufficiently more than replacements for the other sensors. Assuming faults in 1% of one-hour scenarios, equally likely sensors and fault types, and equal time at each measured condition, selected fuel corrections reduce mean absolute error in calculated combustion CO2 by 83.8%. On this engine map, learned relationships support complete sensor diagnoses and fuel corrections that improve emissions accounting while preserving unaffected readings.

---


### 93. [ControlFlow3D: Distilling Multi-View Knowledge into Latent Flow Matching for Point Cloud Upsampling](https://arxiv.org/abs/2610.21190)

**<font color=#1a73e8>作者：</font>** Yuang Liu, Zhi Zuo, Zhengkai Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud upsampling is essential for 3D applications but remains challenging due to sparse, under-constrained observations. Multi-view images can resolve geometric ambiguity, but existing multi-modal methods do not fully exploit visual cues. We propose ControlFlow3D, a framework that distills knowledge from pretrained foundation models into a lightweight generation network during training, enabling strong performance without multi-view images available at test time. Specifically, our method performs conditional flow matching in a structured latent space defined by a frozen 3D encoder. Multi-view image tokens and 3D latent tokens are jointly clustered into shared prototypes via unsupervised soft KMeans; the resulting prototypes guide the flow trajectory through velocity control and are aligned by a consistency loss that progressively transfers image knowledge into the base network. A Mamba-based geometry decoder then maps latent features to dense coordinates with linear complexity. We also construct ShapeNetPU, a 35K-object multi-modal benchmark that is 31 times larger than prior datasets. Extensive experiments across multiple benchmarks demonstrate the effectiveness of our method and its strong generalization capability.

---


### 94. [FedSumUp: User-Auditable Privacy-Aware Representation Sharing for Resource-Constrained Federated Intelligence](https://arxiv.org/abs/2610.21194)

**<font color=#1a73e8>作者：</font>** Jingwei Zhao, Tiantong Sun, Yuanyuan Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing federated data condensation methods face privacy risks, as uploaded synthetic data may preserve sensitive information and remain vulnerable to reconstruction attacks. Moreover, their generation often incurs considerable client-side computational overhead, limiting deployment on resource-constrained devices. To address these issues, we propose FedSumUp, which employs a learnable lossy compressor on clients to generate compact and visually interpretable representations. By controlling information capacity, FedSumUp reduces privacy leakage while allowing users to directly assess the privacy-utility tradeoff. We further introduce a dual-objective optimization mechanism to preserve task-relevant semantics while suppressing reconstruction risks. The compressor is trained on the server and only performs lightweight inference on clients. Since the server cannot access raw data, we develop a data-free closed-loop optimization strategy that optimizes the compressor by minimizing the discrepancy between original and twice-compressed representations after structure-preserving upsampling. Experiments on BloodMNIST, CIFAR-10, and ChestMNIST demonstrate reconstruction PSNR as low as 8.56 dB (with synthetic PSNR as low as 5.45 dB), client runtime reductions up to 96.5% (from 778s to 27s on ChestMNIST), and competitive classification accuracy (89.72% ChestMNIST, 82.24% BloodMNIST, 65.63% CIFAR-10), while remaining inherently robust to non-IID data distributions.

---


### 95. [Poisoning the corpora of protein design systems during pre-training and retrieval](https://arxiv.org/abs/2610.21200)

**<font color=#1a73e8>作者：</font>** Charalampos Koilakos, Kimon-Antonios Provatas, Michail Patsakis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein foundation models increasingly support the generation of novel biological sequences, yet their reliance on large public datasets creates opportunities for adversarial manipulation of the material they learn from and retrieve. We investigate two data-only poisoning attacks against protein design systems, targeting the pre-training corpus of autoregressive protein language models and the retrieval corpus of a text-guided protein generator. For the first, we pre-trained ProtGPT2 and ProGen2 variants of 300 million parameters, introducing poisoned protein sequences containing one of two triggers followed by one of three payloads. Across all poisoned runs, both architectures acquired highly reliable trigger-dependent generation under uniform and ramped poisoning schedules. Under ramped exposure, the earliest majority activation occurred after only 200 contaminated examples, while for the uniform schedule earliest activation occurred around 5000 poisoned samples. For the second attack, we inserted records into a retrieval corpus system without modifying its weights or decoding procedure. A single query-aware record captured a top-16 retrieval position for 58\% of templated requests and 97\% of free-text requests. Conditional on successful poisoned retrieval, 62\% of requests produced altered sequences, while 19-21% acquired the inserted domain by profile-HMM homology. A universal query-unaware attack using 1,500 records also achieved substantial retrieval capture and domain transfer. Together, these findings demonstrate that adversarial protein sequence contributions can establish persistent, sequence-specific behaviour during pre-training or redirect protein generation at inference, while leaving ordinary model behaviour largely preserved. Our work establishes the integrity and biological provenance of protein sequence data as critical safeguards for generative protein design systems.

---


### 96. [Hard Way, The Only Way: Provable Merits of Training on Hardest Examples](https://arxiv.org/abs/2610.21201)

**<font color=#1a73e8>作者：</font>** Elvis Dohmatob  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite a surge of empirical interest in the ``unreasonable effectiveness'' of drastic data pruning for AI systems, a unified theoretical understanding of this phenomenon remains elusive. In this work, we provide a precise high-dimensional theory of learning under data pruning via weighted empirical risk minimization (ERM). As in previous work, we analyze a setting where pruning is performed along a one-dimensional subspace of the input space. Our analysis precisely characterizes the limiting test error curves in the regime where the input dimension N and sample size P tend to infinity with a fixed ratio N/P. The resulting theory recovers several recent results in the literature as special cases and provides a general lens to evaluate how pruning strategies interact with the loss function and label noise. Crucially, we characterize the optimal pruning strategy in the high-sample regime where P greatly exceeds N. We demonstrate that strategic pruning can accelerate the decay of classification test error from the classical sqrt(N/P) rate, typical of vanilla ERM with loss functions without exponential tail (e.g., quadratic loss), to the much faster Bayes-optimal scaling of order N/P. In this setup, we prove that, surprisingly, this optimal performance is achieved by a drastic pruning strategy: discarding almost all training data except for a small proportion, consisting strictly of the 2N hardest training examples.

---


### 97. [UltraDiff: Transferring High-Fidelity Priors to Compressed Latent Spaces for High-Resolution Image Generation](https://arxiv.org/abs/2610.21202)

**<font color=#1a73e8>作者：</font>** Jingjing Ren, Haitian Zheng, Haoyu Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution synthesis with Latent Diffusion Models (LDMs) faces a fundamental trade-off between computational cost and generative fidelity. This trade off is largely governed by the latent compression factor f (e.g. f8 denotes f=8 and f32 f=32). While aggressive compression (f32) significantly improves efficiency, it suffers from severe information loss and ambiguity compared to standard f8 models. We propose UltraDiff, a framework that reformulates this challenge as joint latent diffusion learning followed by marginal score distillation. We introduce MixTeacher, a dual branch DiT that models the joint f8-f32 distribution, utilizing shared attention to resolve the ambiguity of the compressed space with high fidelity f8 priors. Crucially, we propose vector field distillation in the native f32 space. Theoretically, this compels the student to learn the conditional expectation of the teacher trajectory, effectively filtering out compression artifacts. Across the evaluated 1K to 4K settings, UltraDiff approaches f8 level quality while preserving f32 efficiency. With 20 sampling steps on a single A100 GPU, it generates a 2K image in 6.2 seconds over 40 times faster than our f8 baseline.

---


### 98. [SpaceCache: Intermediate Feature Reuse for Efficient Semantic Segmentation on Point Cloud Streams](https://arxiv.org/abs/2610.21207)

**<font color=#1a73e8>作者：</font>** Dongheon Yang, Beomseok Kang, Jae-Joon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point-cloud streams are central to autonomous driving and robotics, yet existing segmentation networks process every frame from scratch, although consecutive frames largely overlap. We observe that the intermediate features of point-cloud transformers remain semantically consistent across frames for the same spatial region, especially in deep stages. Building on this, we present SpaceCache, a training-free feature cache that reuses these features across frames. Tokens of previously observed regions skip a sequence of transformer blocks and take their cached features, only the remaining tokens are computed, and the full token layout is restored for dense prediction. Lightweight cache management keeps reused features reliable by limiting each entry's age and evicting low-confidence entries. Unlike token merging, SpaceCache selects tokens at negligible cost and runs its cache operations once per encoder stage. On both outdoor and indoor benchmarks, such as nuScenes, Waymo, and ScanNet, with two transformer backbones of Utonia and LitePT-B, SpaceCache achieves up to 1.65x speedup with less than 1-point mIoU drop and consistently outperforms token-merging methods.

---


### 99. [Clean Data Can Still Carry Backdoors: Support-Persistent Backdoors for Model Reuse](https://arxiv.org/abs/2610.21208)

**<font color=#1a73e8>作者：</font>** Junhoo Lee, Baekseung Kim, Seungyeon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional backdoor attacks inject artificial trigger patterns into training data, causing models to misclassify triggered inputs while maintaining normal behavior on clean samples. Since these artificial triggers are absent in clean datasets, standard knowledge distillation (KD) typically eliminates them, leading to the common belief that KD serves as an effective purification defense. In this paper, we propose DAR (Discover-and-Relabel), a support-persistent backdoor method that retains its behavior even after clean-data distillation. DAR identifies naturally abundant patterns in low-dimensional feature subspaces using subspace clustering and applies label-only poisoning to samples that inherently satisfy the discovered rule. At test time, the backdoor is activated by locally modifying the corresponding subspace of the target images. By instantiating spatial and frequency operators, DAR achieves attack accuracy comparable to state-of-the-art backdoor attacks in ImageNet classification and CLIP-based prompt tuning. Notably, DAR keeps attack success above 96% after clean KD and remains defense-resistant in practice. Project page: this https URL

---


### 100. [Mylar: Exploring Self-Curation as a Reflexive Creative Practice](https://arxiv.org/abs/2610.21213)

**<font color=#1a73e8>作者：</font>** Kate Chier, Shm Garanganao Almeda, Bjoern Hartmann  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The container holding an artist's work can itself be just as expressive as the work it presents. We investigate self-curation as a creative practice, asking how artists explore and express their identity through the design of their own artwork presentations. Drawing on a study of artists' existing presentation practices, we developed Mylar, a malleable art presentation system that lets artists rapidly generate and compare provisional portfolios, seeing their work anew through different montages. We observed how 12 artists articulated, probed, negotiated, and foraged in Mylar, using rapidly generated portfolios as epistemic artifacts for reflection. We characterize self-curation as a reflexive and plural practice, in which artists use presentation design to shape the legibility of their self and their work and reflexively correspond with provisional presentations to reshape their curatorial intentions. We share design implications for expressivity in online art platforms and for malleable prototyping as a formative design method.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-278](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
