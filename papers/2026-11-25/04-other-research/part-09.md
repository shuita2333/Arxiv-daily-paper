# 📦 其他研究 | 2026年11月25日

> 本类共 **569** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

---

### 401. [ReVAgent: Multi-Agent Reasoning-Intensive Video Generation](https://arxiv.org/abs/2611.30163)

**<font color=#1a73e8>作者：</font>** Yehui Yang, Jing Fan, Jun Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A central challenge in generating instructional videos for reasoning-intensive topics is to show how and why the state changes at each step. Even when an animation renders successfully, the depicted object relationships and state transitions can conflict with the explanation, making the reasoning difficult to follow. We present ReVAgent, a multi-agent framework that solves a problem, generates keyframes for its explanation, and synthesizes an instructional video. The agents share the execution record of a solution program, reuse intermediate results and constructions in the scenes, and check rendered keyframes to guide revisions to the solution or the scenes. We also introduce a multidimensional rubric for assessing whether generated videos present the problem clearly, organize the steps coherently, and use visuals to explain the reasoning. We calibrate a multimodal judge using human ratings and apply it to instructional videos for mathematics and algorithms. In the evaluated samples, ReVAgent presents multi-step reasoning coherently and uses diagrams to show how key operations lead to subsequent states.

---


### 402. [WaDiS: Boundary-Preserving Diffusion Segmentation via Multi-Scale Wavelet Conditioning and Frequency-Aware Gating](https://arxiv.org/abs/2611.30164)

**<font color=#1a73e8>作者：</font>** Qiang Gao, Yi Wang, Yong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have shown strong potential in medical image segmentation due to their generative capabilities and robustness. However, existing methods often struggle to preserve fine anatomical boundaries and to retain multi-scale structural information due to the loss of spatial and frequency details during feature encoding, particularly in complex clinical imaging conditions. This work presents WaDiS, a wavelet-powered conditional latent diffusion framework for medical image segmentation that addresses these limitations through multi-scale wavelet conditioning and frequency-aware information filtering for boundary preservation. The model adopts a multi-scale wavelet conditioning encoder to retain rich structural features, leveraging its lossless nature to better preserve semantic priors critical to the diffusion process. In addition, a Frequency-Aware Gating Block (FAGB) is introduced into the skip connections of the diffusion U-Net, enabling adaptive spectral filtering and residual fusion to better emphasize boundary structures while reducing irrelevant content. To improve generalization across clinical domains, we adopt a structure-preserving color augmentation strategy during training. Specifically, global color statistics are transferred between samples in the LAB color space, allowing the model to decouple appearance from structure and focus more on anatomical shape rather than color bias. Experiments on five benchmark datasets demonstrate that WaDiS consistently outperforms existing diffusion-based and conventional segmentation methods, with notable improvements in boundary accuracy, robustness to noise, and generalization under color variation. The code for this work will be made publicly available upon acceptance.

---


### 403. [GUI-Q: Task-Sensitive Granularity and Relation-Preserving Quantization for GUI Agents](https://arxiv.org/abs/2611.30170)

**<font color=#1a73e8>作者：</font>** Tianqi Li, Yang Wang, Xin He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphical user interface (GUI) agents enable automated interactions with mobile, web, and desktop interfaces. However, their large memory footprint and repeated model calls hinder deployment on resource-constrained devices, motivating post-training quantization (PTQ) without full retraining. Quantization can degrade GUI response accuracy and distort the instruction-vision affinities and local spatial relations needed for GUI target selection. Small coordinate errors can cause missed clicks, while early action errors can alter subsequent interface states and disrupt task execution. Local reconstruction error alone does not directly assess whether these responses and relations are preserved. We propose GUI-Q, a PTQ framework that targets response and relation preservation with 4-bit weights and 16-bit activations (W4A16). Task-Sensitive Granularity Allocation (TSGA) allocates finer groups under a scale-byte budget by combining response sensitivity with the measured reduction in activation-weighted distortion. Relation-Preserving Symmetry Selection (RPSS) then selects symmetric or asymmetric grids to preserve instruction-vision affinities and local spatial relations in GUIs. Across three GUI-capable models, GUI-Q improves mean grounding TargetHit by 8.04 to 12.55 points over the strongest evaluated 4-bit configurations, while reducing static peak graphics processing unit (GPU) memory by 49.9% to 56.2% relative to bfloat16 (BF16). Fixed-output replay with packed 4-bit execution provides 1.7 to 2.8 times model-call speedups. The code will be released.

---


### 404. [Causal Evidence for the Emergence and Spread of Reward Hacking in AI Agent Swarms](https://arxiv.org/abs/2611.30185)

**<font color=#1a73e8>作者：</font>** Sumer S. Vaid  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents that coordinate and collaborate among each other have become pervasive across domains ranging from scientific research to finance and engineering. The opportunity to share messages and build upon each other's work also creates the potential for misaligned behaviors to spread across AI agents. We provide causal evidence that mere exposure to reward hacking, cheating on a task to pass an automated check, is enough to spread the behavior among AI agents, even after the cheat has been rejected. We conducted 17 preregistered experiments with six frontier models (n = 20,111 agents). First, we show that cheating emerges spontaneously. When agents were told that work passing the visible tests is accepted, 33% cheated in the first round, when the shared record of teammates' submissions was empty. Second, we show that agents who rarely cheat when working alone cheat most of the time after seeing a teammate's cheat, as 94% of teammates who saw an accepted cheat cheated. Third, we show that rejection of reward-hacked solutions offers little protection, using experiments that changed only the label on the cheat. Most agents copied a cheat labeled rejected, 34% of agents cheated after an AI reviewer had rejected the cheat, and nearly every agent copied a cheat labeled accepted. Fourth, we show that cheating generalizes to new tasks. On a new problem with an empty collaboration record, 70% of agents who had earlier seen an accepted cheat cheated again, compared with 32% of agents who had seen an empty record. Fifth, we show that cheating spreads from neighbor to neighbor through networks of 256 agents. In the networks, 44% of agents with a cheating neighbor cheated, compared with 2% of other agents. Together, the results suggest that mere exposure can spread misaligned behavior among AI agents, and that catching a cheat is insufficient once other agents have seen the cheat.

---


### 405. [Same Executions, Different Gaps: Judgment Rules in Web-Agent Evaluation](https://arxiv.org/abs/2611.30190)

**<font color=#1a73e8>作者：</font>** Zelong Wang, Weiyue Li, Fei Xue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Success-rate gains guide the development of web agents. Yet knowing which agent ranks first does not tell us how much confidence to place in its reported advantage. We study the comparison itself: how success is defined, what evidence supports the judgments, and how the difference between agents is estimated. On fixed web-agent executions, changing a judge from predicting likely completion to requiring recorded support can remove most of a reported lead without changing the ranking. This effect persists when unresolved completion is distinguished from supported failure. Controlled source additions explain how missing relations between task requirements, objects and observations can conceal a difference or create an apparent advantage. We also find that making both agents' score estimates more accurate can make their difference less accurate, because their original errors partly canceled. To estimate a chosen outcome difference, we combine judge predictions with reference labels for sampled task pairs. Across four released execution systems, regression fitted on the same 50 labeled pairs reduces estimation error relative to direct paired sampling. The results give agent researchers a practical basis for assessing claimed improvements: make the comparison target explicit, retain the evidence needed to check it, and use paired labels to estimate the difference directly.

---


### 406. [Adopting AI Technologies without Traps: A Multi-Agent Reinforcement Learning Framework](https://arxiv.org/abs/2611.30200)

**<font color=#1a73e8>作者：</font>** Jitong Yang, Avinash Reddy Mudireddy, Ziqing Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI technologies and AI agents play increasingly important roles in human society, including in education, economics, and research. Adopting AI technologies can bring immediate, and sometimes tremendous, rewards such as through productivity boost, but they can also bring negative effects including but not limited to losses of job and training opportunities, and cognitive capability declines. Thus, it is important to investigate the optimal ways of adopting AI technologies without different traps. In this paper, we develop a general multi-agent Markov decision process (MDP) based reinforcement learning (RL or MARL) modeling framework for determining and analyzing optimal adoption of AI technologies. This framework can model the long-term dynamic effects of AI adoption, and lead to finding the optimal AI adoption strategies. In our modeling framework, the negative effects of AI adoption are modeled by undesirable state transitions or negative rewards in the MDPs. The proposed multi-agent RL MDPs incorporate both human agents and AI agents. The key idea of our models is that incorporating AI technologies may not only increase the immediate rewards for AI agents but also alter the states of the involved human and AI agents. In particular, we apply this framework to analyzing AI offloading leading to skill erosion, to analyzing optimal human resource structures for a firm adopting AI, and to analyzing the economic equilibria in the trading/employment among human and AI agents. Since the multi-agent MDP based RL technique is from control, machine learning and AI, this research is essentially using an AI technique to determine the optimal ways of adopting or co-existing with AI without traps.

---


### 407. [Ontology-Compiled 2D Clinical State Fields with Bidirectional Diffusion Encoders for Zero-Training Cross-Ontology Medical Coding](https://arxiv.org/abs/2611.30218)

**<font color=#1a73e8>作者：</font>** Zeqiang Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Healthcare systems continually revise clinical taxonomies, update reimbursement schedules, and harmonize cross-border registries. Existing automated coding models bind clinical text understanding to fixed vocabulary-specific heads, requiring manual relabeling and retraining whenever code sets change. We introduce Ontology-Compiled 2D Clinical State Fields (OCSF), a vocabulary-free framework that decouples clinical document reading from target ontology indexing so one trained encoder can switch across arbitrary medical vocabularies in seconds without target training. A single-pass bidirectional diffusion-pretrained encoder and vocabulary-free decoder map each clinical note into a fixed-dimension two-dimensional state matrix with zero code-specific parameters. Any target ontology is compiled offline on CPU from public text descriptions into a scale-invariant Tikhonov deconvolution operator that suppresses sibling-code interference while preserving source decision thresholds. Trained solely on English MIMIC-IV ICD-9 discharge summaries and evaluated without target tuning across 58,706 held-out test notes and five unseen ontologies spanning English ICD-10, MS-DRG, Spanish, Greek, and Chinese (115-185,458 codes), OCSF reaches 63.15% Micro-F1 on in-domain ICD-9 (outperforming a matched closed-vocabulary classifier and eliminating late-epoch tail overfitting) and transfers directly to 26,085 English ICD-10 codes (29.23% recall at gold cardinality), MS-DRG groups, and multilingual terminologies, compiling up to 185,458 codes in under 10 seconds on CPU with sub-millisecond GPU readout.

---


### 408. [RoomTokens: Masked Diffusion over Structured Tokens for Indoor Scene Synthesis](https://arxiv.org/abs/2611.30219)

**<font color=#1a73e8>作者：</font>** Xiaohao Sun, Angel X. Chang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating 3D indoor scenes requires a representation that captures object semantics, instance identity, height structure, and orientation while respecting room geometry. Methods that model scenes as sequences of object vectors learn spatial constraints implicitly, leaving collisions and boundary violations to losses or post-processing; semantic-map methods make occupancy explicit, but collapse instance and directional structure. We introduce RoomTokens, a sliced structured-token representation in which each token stores semantic class, instance-color identity, and facing field. This representation allows a scene to be generated as a discrete grid while preserving cues for instance grouping, orientation estimation, and 3D extent prediction. To learn the RoomToken distribution, we propose MDIRT (Masked Diffusion over RoomTokens), a masked discrete diffusion model that denoises semantic/instance-color/facing channels jointly with a shared cross-slice backbone. Architectural tokens are clamped as explicit floor- plan constraints, so the model samples furniture layouts that respect room geometry while retaining instance and object-attribute structure. Experiments on 3D-FRONT show that RoomTokens with MDIRT improve layout fidelity and physical consistency over sequence/vector- and map-based methods, suggesting structured spatial tokens as a practical choice for discrete 3D scene synthesis.

---


### 409. [EditGRN: Inversion-Free Image Editing by Source-Target Generative Synchronization](https://arxiv.org/abs/2611.30224)

**<font color=#1a73e8>作者：</font>** Jiahuan Wang, Jianan Chen, Jian Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided image editing faces a persistent trade-off between preserving source content and realizing coherent target semantics. We explore this challenge through training- and inversion-free image editing based on discrete generative models. Existing inversion-free discrete editors primarily rely on post-hoc probability correction, creating a disconnect between local token-level adjustments and globally coherent semantic generation. To bridge this gap, we introduce EditGRN, a training- and inversion-free framework with trajectory-wide source-target generative synchronization in discrete space. EditGRN adopts a dual-branch design---the source branch constructs source references and the target branch generates the target image-enabling trajectory-wide synchronization between the two. Exploiting GRN's ability to recover clean tokens from arbitrary binary corruptions, the source branch directly constructs corrupted source states at each refinement step to extract useful editing features, without recovering a specific source-generation trajectory. The target branch synchronizes with the source branch through the same corruption schedule, fusing the corresponding source context with editable representations intra-model. By synchronizing source context with target generation along the entire trajectory, our approach faithfully preserves the background while producing high-quality edits that blend seamlessly with the surrounding scene through intra-model fusion. PIE-Bench show state-of-the-art performance on background preservation and text alignment across diverse editing tasks against continuous and discrete baselines.

---


### 410. [Composing Independently Distilled Memory and Retrieval Policies for Long-Term Agents](https://arxiv.org/abs/2611.30230)

**<font color=#1a73e8>作者：</font>** Grigorii Davydenko, Artem Sakhno, Igor Pavlov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-lived Web assistants require effective memory and retrieval mechanisms to access information from past user interactions. While these capabilities can be learned through specialized policies, it remains unclear whether specialists trained independently in different environments can be effectively composed without joint optimization. This paper investigates compositional transfer through policy distillation. Memory-writing and sequential retrieval policies are independently distilled from frontier-model action trajectories into 3B models and combined with a fixed answer generator without downstream training. On a LongMemEval-based benchmark, the distilled composition achieves 73.1% accuracy, compared with 36.2% for a composition of existing RL-trained specialists, and also outperforms the evaluated RL-trained compositions on PersonaMem-v2. Component ablations reveal that improvements in individual policies depend on their composition, highlighting the importance of cross-specialist compatibility. Further task-specific adaptation improves accuracy to 75.2% on LongMemEval through RL and 48.9% on PersonaMem-v2 through supervised distillation. These findings demonstrate the effectiveness of independent specialist distillation for modular multi-agent systems. Source code and datasets of teacher-generated memory-editing and retrieval trajectories are released to facilitate reproducibility and further research.

---


### 411. [PixelOne: From Options to Pixels in a Single Forward for GUI Grounding](https://arxiv.org/abs/2611.30235)

**<font color=#1a73e8>作者：</font>** Kanghui Tian, Shuai Dong, Yuhan Zhu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI grounding requires precise clicks at low latency. Recent models such as GUI-Decisions and GUI-Swift predict coordinates in one forward pass using fixed global bins with local refinement. However, screenshot downsampling removes detail needed to locate small controls, while fixed bins cover larger pixel ranges at higher resolutions. We introduce PixelOne, which transfers spatial knowledge from a search teacher to a student that predicts clicks directly from screenshots at native resolution. The teacher uses VideoJEV's text-option scorer to select rows and columns and progressively zoom into candidate regions. The student inherits the teacher's parameters and matches its distributions over explored regions through spatial distillation alongside box supervision. At inference, the same decision head selects a visual token, and a lightweight pixel head predicts the click within it, all in one forward pass. A click-aligned loss encourages pixels inside the target box to score above those outside. Across four benchmarks, PixelOne-Pro-35B-A3B achieves 83.8% mean accuracy, the highest among the evaluated single-forward grounders, with a mean latency of 0.43 s per target.

---


### 412. [AIGI-26: A Benchmark for AI-Generated Image Detection Across Diverse Modern Generators](https://arxiv.org/abs/2611.30236)

**<font color=#1a73e8>作者：</font>** Qishuai Ding, Yifeng Wang, Shichuang Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing AI-generated image (AIGI) detection benchmarks predominantly rely on earlier synthesis systems with limited content diversity and conspicuous artifacts, failing to fully reflect the detection challenges posed by high-fidelity images from contemporary models. We introduce AIGI-26, a benchmark of 253,200 images covering 26 recent open- and closed-source generators. Its novel, diverse, and heterogeneous sources provide a basis for systematically evaluating detection methods on modern generated imagery. Additionally, to capture subtle statistical discrepancies across complementary forensic views, we propose the multi-aspect forensic detection network (MAFDNet). Its fixed forensic operators expose complementary texture, local prediction, resampling, and chromatic responses, summarized by a hierarchical encoder using multiscale means and standard deviations. In parallel, a spectral branch captures Fourier log-magnitude and neighboring-frequency phase variation across radial bands and directional axes. Fusing these descriptors combines local inconsistencies with global spectral organization for authenticity detection. Trained on 12,660 AIGI-26 images, MAFDNet achieves 88.5% accuracy and 94.9% average precision on the 240,540-image test set, with only 1.04M parameters and 1.39 GFLOPs per $256\times256$ input. MAFDNet also demonstrates effective cross-dataset generalization on DailyBench and Treasure-37.

---


### 413. [StutterStigma-TR: A Novel Turkish Dataset and Target-Aware BERT Framework for Stuttering-Related Stigma Detection](https://arxiv.org/abs/2611.30252)

**<font color=#1a73e8>作者：</font>** Muhsin Dölek, Arezoo Sadeghzadeh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational research on disability-related ableist harm remains limited, and condition specific resources for stuttering-related stigma are particularly scarce. This study introduces StutterStigma-TR, a Turkish dataset of 6,019 public X/Twitter posts annotated as Stigmatizing, Non-stigmatizing/contextual, or Supportive using a speech and language therapy-informed protocol with independent lived-experience evaluation. We also propose StutterStigma-BERT, a BERTurk-based target-aware framework that combines explicit target marking, target-span representation, target-conditioned context, character-level and handcrafted orthographic information, and gated discourse cues. The framework is evaluated in complementary three-class and binary settings using controlled three-seed ablation analyses and final 20-seed robustness evaluations. Under the common training protocol, Gated Discourse-OrthoTarget trained with cross-entropy is selected as the final configuration for both tasks based on internal-validation Macro-F1. Across 20 random seeds, the final three-class model achieves a mean Macro-F1 of 73.54%, while the final binary model achieves 85.17% using validation-selected decision thresholds. Task adapted harmful-language comparators are additionally evaluated under the common training protocol, and the proposed model obtains the highest mean Macro-F1 among them. For the primary three-class task, matched backbone analyses show higher internal validation Macro-F1 with BERTurk than with TurkishBERTweet or Turkish Mamba, while substantial train-validation separation persists across all three backbones. Separate direct-transfer and zero-shot experiments examine performance without StutterStigma-TR supervision. Across the task-adapted, direct-transfer, and zero-shot comparisons, the condition-specific supervised systems retain the strongest aggregate performance.

---


### 414. [Voyag: Joint Multi-Intent Detection and Execution-Relation Classification for In-Vehicle Voice Assistants](https://arxiv.org/abs/2611.30253)

**<font color=#1a73e8>作者：</font>** Sen Luo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An in-vehicle voice assistant must decide not only which intents an utterance contains but also how co-active intents may be executed: concurrently, in a fixed order, or not at all without arbitration. We present Voyag, a single-forward decision model that jointly predicts ten controlled vehicle-intent slots and a three-way execution relation (parallel, sequential, mutually exclusive) over each co-active intent pair. Voyag combines a multilingual ModernBERT-style encoder (mmBERT-base, 306.9M parameters), a typed per-slot choice head, and a lightweight GroupCalibration relation head (1.61M parameters) that consumes marker hidden states, pooled context, explicit resource-requirement profiles, and symmetrized outer-product conflict features. All objectives are optimized in one joint loss: soft cross-entropy over slot choices, focal cross-entropy over relations, and a mutex-consistency penalty. On a synthetic Chinese vehicle-life benchmark with semantic scene-level splits and a leakage audit (30,017 / 3,473 / 5,000 groups), validation-only selection yields 0.9893 slot accuracy and 0.0526 expected calibration error over 50,000 slot decisions. Conditioned on gold intents, the relation head reaches 0.8548 accuracy, 0.8473 macro-F1, and 0.6062 mutually-exclusive recall over 4,000 pairs; end to end with one encoder forward it reaches 0.8530 accuracy and 0.8464 macro-F1. Against a two-stage rule pipeline, the aggregate end-to-end gain is small and borderline, so we claim no aggregate advantage; the learned head's advantage lies in sequential and parallel recall where surface rules are blind. We report rule baselines with a tautology disclosure and a held-out thermal conflict failure.

---


### 415. [Operator-Valued Q-Learning: Compositional Bellman Recursions for Order-Sensitive Decision Making](https://arxiv.org/abs/2611.30255)

**<font color=#1a73e8>作者：</font>** Swagatam Das, Swagato Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In quantum pulse sequences, spacecraft attitude control and in-hand reorientation, actions act on a hidden physical state as non-commuting operators, so the outcome of a plan depends on the order of its actions. We let the value function carry this structure: each Q(s,a) is an N x N operator, and the Bellman backup applies the action's dual map to the continuation value, Q(s,a) = K_a^*(R(s,a) + gamma E V(s')). Unrolled along a plan, the recursion builds the ordered product of the actions' operators, and the value at any latent state is a linear trace readout. It is exact for policies that do not observe the latent, the backup contracts for unitary and orthogonal dynamics, and an asynchronous operator TD scheme learns it with almost-sure convergence. Classical values live in a lattice, so a maximum over actions exists; self-adjoint operators form an anti-lattice (Kadison) and have none. An operator log-sum-exp still gives one operator per state-action pair whose readout upper-bounds the value of every policy at every latent state. The sampled update converges to it for a finite horizon, and it reduces to soft Q-learning and the QMDP bound when actions commute. We prove that scalar values on observations that ignore action order must confuse swapped histories, that exact history tables grow exponentially for free action groups but polynomially for nilpotent ones, and give a Hankel-rank lower bound on the operator dimension. In experiments the learned policy matches 1000-simulation tree search on SO(3) pointing for horizons up to 20 at ~10^4 times lower decision cost, transfers zero-shot to unseen initial states, and acts exactly on its belief mean when the initial state is hidden, where plugging the mean into a DQN does not. A planner with the same model knowledge is more sample-efficient at short horizons, and a DQN given the operators matches or exceeds OpQ.

---


### 416. [SGPC: Safety-Guiding Policy Constraint for Stable Off-Policy Safe Reinforcement Learning](https://arxiv.org/abs/2611.30265)

**<font color=#1a73e8>作者：</font>** Yifan Liu, Nan Zhang, Yang Cong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy safe reinforcement learning (RL) faces a challenging trade-off between task optimality and constraint feasibility. In primal-dual methods, the coupled optimization of cumulative reward and constraint penalties through adaptive Lagrange multipliers may induce oscillatory policy updates near the safety boundary and amplify the effect of unreliable reward estimates outside the safe set. To address these issues, we formulate a new constrained optimization problem (COP) for safe RL by introducing a Safety-Guiding Policy (SGP) and a corresponding Safety-Guiding Policy Constraint (SGPC). The proposed COP augments the standard COP in safe RL with a conditional safety-guidance constraint. During actor updates, the current actor is evaluated using the learned cost critic. If it is predicted to be outside the safe set, SGP provides a nearby lower-cost training reference, and SGPC guides actor optimization toward this reference. Once the policy enters the safe set, the added constraint becomes inactive, and the formulation reduces to the original COP. This formulation leads to a plug-in actor-training constraint that can be integrated into off-policy safe RL algorithms. By applying primal-dual optimization to the auxiliary COP, we finally derive an SGPC-based off-policy safe RL algorithm and implement it in two representative off-policy algorithms, yielding SAC-SGPC and TD3-SGPC. Experiments on multiple Safety-Gymnasium benchmarks demonstrate that SGPC achieves a better optimality-safety trade-off by substantially reducing constraint violations and cost oscillations while maintaining competitive or better task returns.

---


### 417. [OCCA-Seg: Object and Channel Context Aggregation for Semantic Segmentation of Remote Sensing Images](https://arxiv.org/abs/2611.30267)

**<font color=#1a73e8>作者：</font>** Gang Yang, Si Chen, Quan Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation, which assigns a class label to each pixel, is a key task in computer vision. However, semantic segmentation of remote sensing images (RSIs) remains challenging because of complex scenes and objects at multiple scales, which limits segmentation accuracy. To address these challenges, we propose a context aggregation scheme called object and channel context aggregation (OCCA), consisting of three components: object contextual attention module (OCAM), channel contextual attention module (CCAM), and aggregation module (AM). Firstly, motivated by the observation that each pixel shares the class label of the object to which it belongs, object-level context represents each pixel through aggregating context from its corresponding object class. Secondly, because feature channels are correlated with object categories, channel-wise context models channel-wise contextual dependencies conditioned on object categories. Finally, the context information from OCAM and CCAM are fed into AM and used to weight and modulate the object context, enhancing the discriminative ability of the segmentation model. The experiments on several public remote sensing datasets including LoveDA, UAVid, ISPRS Potsdam, and Vaihingen datasets demonstrate competitive improvements over existing methods.

---


### 418. [CHIP: Contrastive Hardware-Image Projection. Can OpenAI CLIP Reconstruct Images from the CPU Computational Footprint?](https://arxiv.org/abs/2611.30269)

**<font color=#1a73e8>作者：</font>** Debayan Sengupta, Darsh Asher, Kaushal Mhapsekar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Image inference on a shared CPU leaves input-dependent traces in software-visible performance counters and execution time. CHIP (Contrastive Hardware-Image Projection) trains a lightweight residual projector on public images to map these measurements into the 768-dimensional visual embedding space of a frozen OpenAI CLIP model. A frozen Stable unCLIP generator uses the projected embeddings to reconstruct recognizable color scenes for held-out inputs. The attack requires no physical probe, candidate image gallery, domain-specific generator, or shared cache, and elapsed time alone retains the signal.
We evaluate full-counter, single-counter, and timing-only measurements on Intel Haswell and Sapphire Rapids. The projected embeddings achieve 0.85 ROC AUC for held-out image identification, compared with a 0.50 baseline. Exact-image top-five retrieval reaches 24% on CIFAR-100 and 56% on Unsafe-Diffusion. Across both processors, reconstructions average $1.4\times$ the baseline RGB color-palette overlap and $2.5\times$ the baseline structural similarity.

---


### 419. [DUET: Dual-MDL Unsupervised Entropy-Trie Segmentation for Low-Resource Languages](https://arxiv.org/abs/2611.30273)

**<font color=#1a73e8>作者：</font>** Xiaotian Wang, Youyuan Lin, Zhan Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Morphological segmentation, the task of decomposing words into constituent morphemes, becomes particularly challenging under extreme data scarcity, a regime that can arise in language documentation and linguistic reasoning. This difficulty stems from existing approaches' reliance on annotated data, external resources, or recurring patterns that emerge only in larger corpora. To address this limitation, we propose Dual-MDL Unsupervised Entropy-Trie Segmentation (DUET), a deterministic unsupervised algorithm that decouples structural candidate generation from statistical candidate ranking. DUET combines branching entropy with recursive paradigm discovery to generate linguistically plausible candidate segmentations, then ranks them using a dual minimum description length (MDL) criterion: a corpus-level objective rewards morpheme reuse, while a construction-tree objective guards against over-segmentation. On the SIGMORPHON 2023 interlinear glossing shared task, DUET outperforms unsupervised baselines in Morpheme F1 under both the standard and simulated extremely low-resource settings, while providing broader candidate coverage. Augmenting prompts with DUET segmentations improves performance on a linguistic reasoning benchmark, yielding the best overall results among the evaluated segmentation methods.

---


### 420. [RigidAnchor: Cross-View Geo-Localization for UAV via Iterative Planar Rigid Alignment](https://arxiv.org/abs/2611.30278)

**<font color=#1a73e8>作者：</font>** Bo Wang, Dekang Zhu, Jian Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A UAV that flies without GNSS has to estimate its absolute position and heading without any external signal. Most existing methods for UAV-to-satellite cross-view geo-localization (U-S CVGL) treat the task as image retrieval: they compress the UAV image and each satellite tile into separate descriptors, rank the tiles by their similarity, and return the center of the best tile. The output can therefore only lie on a pre-defined grid, its accuracy is limited by the tile size, and no heading is produced. Regressing the pose in a single pass removes the grid, but it leaves no chance to correct the estimate afterwards. We observe that satellite tiles are not independent samples. They are laid on the map at a fixed spacing, scale and orientation, so neighboring tiles join into one continuous satellite block with a consistent metric, and a nadir UAV view of that block differs from it by a planar rigid transform only, i.e. a 2D translation plus an in-plane rotation. We therefore reformulate U-S CVGL as solving for this transform between two images of different sizes. Position and heading then become parts of one geometric quantity, and the accuracy is no longer limited by the tile grid. We propose RigidAnchor, which solves the transform iteratively. The network encodes the two images and builds a multi-level correlation pyramid between them. At each iteration, it indexes the pyramid with every aerial cell carried through the current estimate, pools the descriptors of all cells into one hidden state, and lets two decoupled heads predict a translation increment and a rotation increment, the latter being composed rather than added. On Bearing-UAV-90K, the cross-view mean errors are 78.6% lower in position and 69.7% lower in heading than Bearing-UAV, and HSR@15 increases by 19.06 points. Code is available at this https URL.

---


### 421. [AdvMTO: Multimodal and Temporal Adversarial Object Attacks via 2D Gaussian Splatting for BEV-Based 3D Object Detection](https://arxiv.org/abs/2611.30283)

**<font color=#1a73e8>作者：</font>** Zhiyang Cui, Hao Tan, Ruonan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial object attacks pose a threat to BEV-based 3D object detectors in autonomous driving. Existing attacks typically target a single modality, coordinate camera and LiDAR observations at the current timestamp, or model temporal persistence mainly in camera streams. Without a unified construction of current and historical observations, attacks can leave part of the detector's accumulated evidence unsuppressed, limiting their effectiveness. In this paper, we propose AdvMTO, a 2D Gaussian Splatting (2DGS) framework for suppressing detection of persistent adversarial objects. Its oriented surfels encode appearance, geometry, and opacity in one object state, from which camera images and scanline LiDAR returns are generated. AdvMTO then constructs current and historical inputs through detector-native processing, regenerating LiDAR returns in each native source sweep for fusion detectors. We optimize bounded appearance perturbations for each detector, propagating gradients through historical BEV memory for temporal camera detectors. For fusion detectors, bounded geometry refinement along local normals further perturbs both sensing modalities. Experiments on nuScenes demonstrate effective suppression of traffic-cone detection across three BEV detectors. Temporal ablations further highlight the importance of detector-native history modeling for both attack construction and optimization.

---


### 422. [Temporal Leakage Distorts the TGB Node Affinity Leaderboard: A Point-in-Time Audit](https://arxiv.org/abs/2611.30289)

**<font color=#1a73e8>作者：</font>** Yuhang Wang, Dongmei Li, Yuze Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Node affinity prediction in the Temporal Graph Benchmark (TGB) asks how a node's future interactions will be distributed over other nodes. On this task, methods that reuse past ground-truth labels often outperform temporal graph neural networks, and the state of the art builds on them. Such comparisons assume a point-in-time correct evaluation, in which a model receives only information available at prediction time. Drawing on as-of joins and bitemporal databases, we formalize this requirement by distinguishing when a label must be predicted, its query time, from when it is fully determined, its availability time, and we audit the four TGB node affinity datasets and their evaluation loop with model-agnostic tools. None of the four meets it. On three datasets, each label summarizes a single day about five days after its timestamp, not the documented following week, yet the loop feeds it back right after that timestamp; on the fourth, the loop processes the edges from which each label is computed before predicting it. Under a drop-in leakage-free protocol, every method whose inputs leak loses up to 17% of its NDCG@10, the advantage of past labels over the interaction stream nearly vanishes or reverses, and both the best configuration of the state of the art and the rankings change; a blend of training-free long-memory statistics, with weights fit on validation data, matches or exceeds the state of the art under both protocols. Point-in-time correctness should therefore be built into benchmarks, and our tools carry over to other benchmarks whose labels aggregate event streams over time windows.

---


### 423. [MirrorGuard: Defending LiDAR Perception against Passive Mirror Attacks](https://arxiv.org/abs/2611.30292)

**<font color=#1a73e8>作者：</font>** Aymen Bouferroum, Ildi Alla, Selma Yahia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mirror-based LiDAR attacks passively redirect automotive LiDAR's beams to create phantom objects in the vehicle perception. Recent work has demonstrated that these attacks may cause vehicles to brake for a phantom where nothing stands. Every phantom return is a genuine time-of-flight measurement, so current spoofing defenses are not able to differentiate phantoms from real objects. We present MirrorGuard, a physics-informed defense that identifies and removes mirror-induced phantom returns before they affect downstream perception. MirrorGuard tests three consequences of the reflected path. Every phantom bearing crosses the mirror's finite aperture, its opaque surface blocks any direct return beyond it, and the two reflections off the mirror dim the phantom. MirrorGuard identifies a phantom by these cues over multiple scans and removes the reflected beams before it reaches any detector or occupancy grid. On real-world recordings of this attack, MirrorGuard removes 96.31% of the phantom's returns at 98.30% precision, with 99.99% of non-phantom returns untouched. In a closed loop with the CARLA driving simulator and the open-source stack (Autoware), a vehicle without the defense halts for an obstacle that is not present and a following car crashes into its rear. With MirrorGuard, no vehicle produces a halt or a crash. MirrorGuard runs at 59 ms mean per scan on a CPU and is a software-only solution that does not require new hardware or environmental training.

---


### 424. [Topology-Prior-Guided Regional Latent Dynamics for Transient Structural Response Prediction](https://arxiv.org/abs/2611.30293)

**<font color=#1a73e8>作者：</font>** Yuan Zhang, Mohammad Amin Nabian, Shaotong Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the transient nonlinear responses of complex engineering structures remains challenging due to large finite element meshes, heterogeneous structural components, and history-dependent mechanical behavior. This study proposes a topology-prior-guided regional latent dynamics (TPLD) surrogate model that combines physically structured regional representations with dynamics-aware latent learning for full-field time-history prediction. Based on mesh topology and engineering priors, structural responses are encoded into spatially coupled regional latent variables through region-aware feature extraction and topology-constrained interactions. An auxiliary one-step prediction task enhances latent-space dynamical predictability by introducing state-transition supervision. A load-conditioned spatiotemporal Mamba model then predicts regional latent trajectories by integrating temporal causal scanning and bidirectional spatial scanning, while a shared coordinate-conditioned decoder reconstructs full-field nodal responses. The framework is evaluated on three finite element datasets: a parametric stiffened panel, a partitioned pressure impact plate, and a Toyota Yaris full-vehicle crash model. The relative L2 errors for the three displacement components range from 4.00% to 8.21% on the stiffened panel and from 1.41% to 12.22% on the approximately 1.49-million-node vehicle model. On the BIW crash benchmark, TPLD achieves a relative L2 position error of 0.620%, representing a 30.7% reduction compared with the best-performing GeoTransolver configuration. Ablation studies demonstrate the advantages of topology-guided regional representations over global latent and learnable soft-slice alternatives, while auxiliary one-step prediction particularly improves the prediction of accumulated plastic strain.

---


### 425. [SafeRank-ReID: Candidate-Conditioned Re-Ranking under Identity Conflicts for Multimodal Person Re-Identification](https://arxiv.org/abs/2611.30314)

**<font color=#1a73e8>作者：</font>** Yizhi Wang, Zixuan Li, Zhuwen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Person Re-Identification (ReID) exploits complementary identity cues from different sensing modalities to mitigate the performance degradation caused by challenging imaging conditions. Existing methods typically estimate Modality Reliability at the query level, making it difficult to identify conflicting inputs that retain normal visual quality but correspond to an incorrect identity. Such inputs may receive high confidence, promote irrelevant gallery candidates, and lead to negative fusion. To address this issue, we propose SafeRank-ReID, a candidate-conditioned safe re-ranking framework for Multimodal Person Re-Identification (ReID). To capture the varying support of the same modality for different candidates, we introduce a candidate-conditioned evidence arbitration mechanism that integrates unimodal retrieval evidence, input quality, and cross-modal consistency to estimate trust and conflict logits for each modality-candidate pair. Together, these logits contribute to the normalized modality weights, allowing support strength to vary across modalities and candidates while reducing the contribution of potentially unreliable evidence. A candidate-set refinement module subsequently applies self-attention to jointly model candidate representations and predicts residual scores from their competitive relations, thereby refining the initial fused ranking. For fusion results that remain uncertain after refinement, a query-level fallback gate estimates an interpolation coefficient from the overall conflict level and cross-modal uncertainty, adaptively combining the fused scores with those of the most reliable unimodal branch. Experiments on RGBNT201 and MSVR310 show that SafeRank-ReID maintains competitive clean-input retrieval while improving robustness to Identity Conflicts across person and vehicle benchmarks.

---


### 426. [TAED: Trajectory-Aligned Encoder--Decoder Distillation for Detection Transformers](https://arxiv.org/abs/2611.30326)

**<font color=#1a73e8>作者：</font>** Zilong He, Zhangchi Hu, Hebei Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distilling localization knowledge into compact detection transformers (DETRs) requires consistent teacher-student query correspondence across decoder layers. However, in DETRs with encoder-based query selection, the teacher and student select top-K proposals independently. Same-rank queries can originate from different spatial locations and correspond to different objects, making rank-based layer-wise supervision unreliable. To address this problem, we propose Trajectory-Aligned Encoder-Decoder Distillation (TAED), a framework for knowledge transfer between DETRs of different capacities. Encoder feature distillation matches normalized multi-scale features to strengthen student representations and increase the number of teacher-student query pairs from the same encoder locations. Source-indexed query alignment pairs native queries from the same encoder locations and retains pairs associated with the same object for which the teacher provides reliable and more accurate final localization than the student. Trajectory-aligned localization distillation maintains these correspondences and uses teacher proposals and corresponding decoder-layer box predictions to guide student refinement, without introducing additional queries. On COCO, TAED improves DINO-R18 and two-stage Deformable DETR-R18 by 2.5 and 1.7 AP, respectively. Further gains on D-FINE and ECDet demonstrate applicability to recent real-time DETRs at no additional inference cost.

---


### 427. [Draft Forcing: Target-guided Speculative Drafting and Learned Verifier for Autoregressive Video Generation](https://arxiv.org/abs/2611.30328)

**<font color=#1a73e8>作者：</font>** Chenkai Xu, Yuji Ren, Zihui Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models enable streaming synthesis chunk by chunk, yet invoking the large model for every chunk remains costly. While chunk-level speculative decoding can offload chunks to a lightweight draft model, existing approaches suffer from two limitations: (1) an off-the-shelf draft diverges from the target's trajectory, compounding errors in history; and (2) they either omit verification or rely on costly post-decode aesthetic scores rather than verifying consistency against the target. We address both with Draft Forcing, a framework coupling target-guided drafting with an on-policy trained verifier. Specifically, to align the draft for high acceptance, we opt for feature-level drafting, conditioning it on multi-layer target hidden states persisted from committed chunks, whose outputs are pushed to match target trajectories with multi-aspect losses. For verification, we propose an on-policy trained feature-space verifier predicting CDF-calibrated frame-wise relative RMSE against the target. It is trained on speculative rollouts as contexts anneal from random to inference-aligned mixtures, and gates proposals without VAE decoding. On the 14B Self-Forcing target, Draft Forcing achieves $1.63\times$ DiT and $1.57\times$ end-to-end speedups on VBench with minimal quality loss, and up to $1.93\times$ DiT ($1.82\times$ end-to-end) when combined with orthogonal KV compression. It generalizes to accelerate a streaming variant of MiniMax-H3, generating over $50\%$ draft frames with competitive quality.

---


### 428. [AirVT-15k: A Query-Diverse UAV Video-Text Dataset and Query-Adaptive Evidence Alignment Network for Retrieval](https://arxiv.org/abs/2611.30339)

**<font color=#1a73e8>作者：</font>** Xi Chen, Xu Chen, Xiangyang Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle video-text retrieval (UAV-TVR) requires matching language to both scene context and subtle object changes. A harbor-layout query relies on global scene context, whereas a departing-vessel query requires local functional cues and motion states. Existing benchmarks provide diverse aerial descriptions but give limited attention to distinct evidence needs within the same video. We introduce AirVT-15k, a benchmark of 15,504 UAV videos and 155,040 captions, with ten complementary bilingual captions per video describing scenes, object states, and temporal changes. We also propose AirFocus-CST, which selects query-relevant frames and patches, encodes temporal feature differences, and combines coarse-to-fine interaction (CFI) with optimal-transport alignment (OTA). Average mean recall reaches 63.67% on AirVT-15k and 24.41% on CapERA, improving over the strongest baselines by 2.96 and 1.91 percentage points, respectively. The dataset and code are available at this https URL.

---


### 429. [FMSNO: Scaling Surface Neural Operators by Learned Flow Matching Reparametrisation](https://arxiv.org/abs/2611.30341)

**<font color=#1a73e8>作者：</font>** Vasilii Liamin, Oleg Bakhteev, Vladimir Vanovskiy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose the Flow Matching Surface Neural Operator (FMSNO), which combines learning a shared map from irregular surface meshes to a regular two-dimensional grid on the sphere and training a neural operator on the regular grid. Constructing a separate map for each new geometry can dominate inference time on large meshes. We initially pretrain the mapping by flow matching using precomputed optimal transport maps as targets and then continue its training using combined geometry and CFD objectives. We apply it to unseen geometries in a single forward pass. The learned flow deforms the surface points, and we project its endpoints onto the sphere. We then splat geometric features onto the spherical grid, apply a neural operator (we tested both Fourier and Spherical Fourier Neural Operators), and interpolate its output back to the surface. For a mesh with $N$ points, evaluating the map costs O(N), and the full prediction costs O(NlogN) with the FNO backbone. We evaluate surface pressure prediction on ShapeNet-Car, AhmedML, and DrivAerNet++, and drag coefficient prediction on DrivAerNet++. Across the three pressure benchmarks, our accuracy is on par with that of the most accurate baseline. On a surface with one million points, our method achieves a 354x end-to-end inference speedup over that baseline while keeping the same memory usage asymptotics of O(N).

---


### 430. [Shift by Analogy for Compositional Zero-Shot Learning](https://arxiv.org/abs/2611.30342)

**<font color=#1a73e8>作者：</font>** Zanwu Liu, Bo Li, Guanglin Niu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compositional zero-shot learning recognizes attribute-object pairs absent from training. An unseen pair has a semantic description but lacks an observed visual reference. We propose Shift by Analogy (SBA) to make unseen compositions visually seen through a shift-then-match process. Its core add-subtract-add rule transfers an attribute change between two seen image-text residuals on a source object to a reference residual on the target object. This shifts the target's own text feature toward its visual center; learned refinement produces a proxy for matching query images. During training, each target is excluded from its supports, and recognition is learned using references constructed from other pairs. An analogy library and same-object attention extend this construction across candidates, while joint learning integrates proxy matching with semantic and primitive evidence. Visual-center analysis confirms substantially improved correspondence for unseen compositions. Experiments across three standard benchmarks show that SBA consistently outperforms strong CZSL baselines under both closed- and open-world evaluation.

---


### 431. [NNS-GS: Non-Local Neural Scattering for Relightable Gaussian Splatting](https://arxiv.org/abs/2611.30351)

**<font color=#1a73e8>作者：</font>** Shiyu Liang, Yang Gao, Lili Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creating relightable 3D assets of translucent objects is challenging because changing the illumination at one surface location can affect the appearance elsewhere through subsurface scattering. Existing Gaussian-based scattering models typically predict scattering from local features, making this dependence difficult to capture. We present Non-Local Neural Scattering for Gaussian Splatting (NNS-GS), which learns non-local scattering together with geometry-guided local reflection. The scattering module learns how illumination from light-visible surface regions in light space contributes to the shading point in view space, conditioned on regional diffuse responses and spatial relationships. The reflection module supplies these diffuse responses and uses additional geometric guidance to better capture specular highlights and sharp shadow boundaries. To reduce component mixing and support controllable scattering appearance, anchor-based progressive training establishes the diffuse-scattering base before introducing specular reflection and supervises the components separately. Under calibrated point lighting, NNS-GS improves mean PSNR over existing methods by 2.47 dB and 0.81 dB on the synthetic and real translucent scenes, respectively. Additional synthetic comparisons further show that NNS-GS better matches the reference when adjusting scattering attenuation.

---


### 432. [STAR: Structure-Aware Temporal Action Recovery for Point Supervised Temporal Action Localization](https://arxiv.org/abs/2611.30354)

**<font color=#1a73e8>作者：</font>** Yawar Rehman, Min Young Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point supervised temporal action localization is becoming the need of time in this era of ever growing and non-stop video data. Existing method mainly rely on snippet level action response to generate pseudo labels. However, these labels often suffer from boundary ambiguity, over extended proposals, and weak temporal structure. To address these issues, we propose STAR, a structure-aware Temporal Action Recovery framework for point supervised temporal action localization. STAR works by enhancing the base S model with temporal difference interaction with attention module to capture forward and backward snippet changes, and introduces the learning of start, core, and end roles to model the internal temporal structure of actions. In addition, STAR further improves the pseudo label generation through All point proposal ranking and Rolebank based structural re-ranking, which suppress neighbor crossing and structurally inconsistent proposals. Finally, temporal action detector to STAR feedback supervision transfers high quality detector prediction back to the STAR model through soft start, core, end, action, and background targets. This helps to further refine the pseudo labels. Extensive experiments on four standard benchmarks shows the effectiveness of STAR. By using I3D features, STAR achieves 67.2% at AVG@0.1:0.7 on THUMOS'14, 58.1% on GTEA, 74.6% on BEOID, and 31.7% at AVG@0.5:0.95 on ActivityNet-1.3, outperforming previous point supervised methods across multiple benchmarks.

---


### 433. [Boosting zero-shot learning through neuro-symbolic integration](https://arxiv.org/abs/2611.30358)

**<font color=#1a73e8>作者：</font>** Francesco Manigrasso, Fabrizio Lamberti, Lia Morra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot learning (ZSL) aims to train deep neural networks to recognize objects from unseen classes, starting from a semantic description of the concepts. Neuro-symbolic (NeSy) integration refers to a class of techniques that incorporate symbolic knowledge representation and reasoning with the learning capabilities of deep neural networks. However, to date, few studies have explored how to leverage NeSy techniques to inject prior knowledge during the training process to boost ZSL capabilities. Here, we present Fuzzy Logic Prototypical Network (FLPN) that formulates the classification task as prototype matching in a visual-semantic embedding space, which is trained by optimizing a NeSy loss. Specifically, FLPN exploits the Logic Tensor Network (LTN) framework to incorporate background knowledge in the form of logical axioms by grounding a first-order logic language as differentiable operations between real tensors. This prior knowledge includes class hierarchies (classes and macroclasses) along with robust high-level inductive biases. The latter allow, for instance, to handle exceptions in class-level attributes and to enforce similarity between images of the same class, preventing premature overfitting to seen classes and improving overall performance. % CHECK: original sentence had no verb ("Both class-level and attribute-level prototypes through an attention mechanism ...") FLPN learns both class-level and attribute-level prototypes, the latter through an attention mechanism specialized for either convolutional- or transformer-based backbones. FLPN achieves state-of-the-art performance on the GZSL benchmarks AWA2 and SUN, matching or exceeding the performance of competing algorithms with minimal computational overhead. The code is available at this https URL

---


### 434. [REACT: Response-based Expert Assembly from Contextual Trajectories](https://arxiv.org/abs/2611.30366)

**<font color=#1a73e8>作者：</font>** Hesen Yang, Yuxue Liu, Yanzhe Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense feed-forward networks are unaffected by how their neurons are grouped: every neuron is evaluated. Sparse execution makes this grouping consequential, because each input can access only a few experts. An arbitrary partition can therefore retain pretrained weights while separating computations that an input needs together. We argue that upcycling should organize neurons according to their responses to similar inputs. To establish this correspondence, we introduce a context-guided upcycling approach REACT, Response-based Expert Assembly from Contextual Trajectories, that uses frozen denoising trajectories to connect input contexts with pretrained neuron responses. We first identify contexts after timestep-wise centering to account for distribution shifts across noise levels, then use their associated responses to allocate intact neurons to routed experts. The same contexts initialize the corresponding router entries, aligning expert contents with their intended inputs, while global activation statistics select an always-active shared expert. Layer-wise reconstruction and end-to-end adaptation refine this initialization for sparse execution. On ImageNet-1K, our approach achieves better generation quality while activating only 37.5% of the original FFN parameters and reducing total per-token activated parameters by 27.6%.

---


### 435. [Mind the Gaps: State-Guided Supervision Allocation for Object Detection Dataset Distillation](https://arxiv.org/abs/2611.30369)

**<font color=#1a73e8>作者：</font>** Jiehui Xie, Zhengxun Jin, Jiahao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in dataset distillation have enabled large-scale training datasets to be compressed into compact synthetic sets. However, dataset distillation for object detection remains challenging, as it requires preserving diverse classification and localization signals under limited image budgets. Existing approaches often emphasize individual-image informativeness without explicitly accounting for supervision accumulated across the distilled dataset, potentially leading to redundant supervision and uneven class-scale coverage. To address this limitation, we propose State-Guided Supervision Allocation (SGSA), a framework that formulates object detection dataset distillation as a dataset-level progressive supervision allocation problem. SGSA establishes class-scale supervision quotas and maintains a global state that tracks detector predictions accumulated from previously selected synthetic images. The remaining gaps between the target quotas and accumulated supervision guide adaptive object sampling, detector-guided canvas refinement, and marginal-gain-based candidate selection, encouraging complementary supervision across images. On MS COCO, SGSA outperforms a matched OD3 baseline by 3.73-4.06 mAP points across three image budgets (0.25%-1.0%). On PASCAL VOC, SGSA outperforms the strongest evaluated baseline by 4.53-6.90 mAP50 points across three image budgets. These results demonstrate the effectiveness of dataset-level supervision allocation guided by accumulated detector feedback under limited image budgets.

---


### 436. [ColonoWorld: Camera-Controlled Full-Procedure Colonoscopy Video Generation](https://arxiv.org/abs/2611.30372)

**<font color=#1a73e8>作者：</font>** Jihwan Hong, Sunghwan Steve Cho, Ping Shu Ho 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Navigation systems in colonoscopy are advancing from guiding the endoscopist to steering the scope autonomously. Since an incorrect motion can injure the patient, developing and evaluating these systems calls for a world model of colonoscopy. Such a model must follow a commanded scope motion, keep the colon anatomy consistent, and show lesions and procedural events. Yet camera-controlled generators trained on general scenes lose the colon's structure under motion, and endoscopic generators offer no camera control. We present ColonoWorld, a colonoscopy world model conditioned on a camera trajectory and a coarse 3D tube of the colon, trained on in vivo videos. From a whole-colon tube, it generates a full cecum-to-rectum procedure, even for unseen colon shapes. It also places polyps, instruments, and irrigation at specified locations and times. ColonoWorld outperforms state-of-the-art video generators, reducing camera trajectory error by 32% and FVD by 29%. Our code and annotations will be released at this https URL.

---


### 437. [Low-Rank Tensor Representations for Efficient Multimarginal Optimal Transport](https://arxiv.org/abs/2611.30376)

**<font color=#1a73e8>作者：</font>** Johann Cl{é}ment-Cottuz, Gilles Gasso, Maxime Berar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimarginal Optimal Transport (MOT) suffers from exponential computational and memory costs in the number of marginals, as transport plans are represented by high-dimensional tensors. We introduce Low-Rank Multimarginal Optimal Transport (LRMOT), which restricts transport plans to tensors with bounded multilinear rank, providing a compact and structured representation of multimarginal couplings. This structure enables efficient algorithms with a low memory footprint. We establish approximation bounds for the resulting low-rank formulations and demonstrate experimentally that the proposed algorithms substantially reduce computational time while achieving solutions with low transport cost.

---


### 438. [IP-GNO: An Inductive Physics-Informed Graph Neural Operator for Automated Distribution System State Estimation](https://arxiv.org/abs/2611.30387)

**<font color=#1a73e8>作者：</font>** Sakshi Kumar, Chhavi Jhari, Ajay Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distribution System State Estimation (DSSE) is a crucial tool for real-time monitoring, operation, and control of the new-age distribution systems (DSs) due to intensified voltage fluctuations and operational uncertainties introduced by volatile power injection at the nodes. Existing GNN-based approaches generally exhibit limited generalization across networks with different sizes and topologies, making zero-shot cross-grid transfer to unseen DSs a significant challenge. To overcome the aforementioned challenges, this article proposes an Inductive Physics-Informed Graph Neural Operator (IP-GNO) for scalable and transferable DSSE. The proposed framework frames complex bus voltage estimation as an operator-learning problem inspired by the Neumann series expansion of the inverse bus admittance matrix. An admittance-parameterized kernel, incorporating a self-admittance gate in the zeroth-order term and a persistent source-injection skip connection across network layers, captures the underlying electrical dependencies. Additionally, a Physics-Embedded Tree Encoding (PETE) scheme introduces five grid-size-invariant positional features derived from path impedance and a DC-linearized phase-angle prior. A sine-cosine output formulation is further employed to address phase-angle periodicity and ensure stable training. The proposed IP-GNO module is evaluated on two small (IEEE 33- and 69-bus), two medium (IEEE 123- and 136-bus), and one large (2522-bus) sized DSs. Particularly, its zero-shot cross-grid generalization capability is investigated by training the model exclusively on the IEEE 33-bus system and directly evaluating it on four unseen distribution networks of different sizes without retraining or fine-tuning. A detailed comparative analysis with the existing state-of-the-art DSSE tools proves the superiority of IP-GNO, enabling scalable DSSE across heterogeneous DSs.

---


### 439. [BASE: A Backend-Agnostic Streaming Embodiment Layer for Full-Duplex Conversational Avatars](https://arxiv.org/abs/2611.30388)

**<font color=#1a73e8>作者：</font>** Chenye Yang, Jin Jiang, Shengcai Liao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many end-to-end spoken dialogue models can now converse in real time and full duplex, and turning them into 3D avatars requires full-body gestures, listening feedback, and turn-taking. Existing methods couple the motion generator tightly to one dialogue model by reading its internal states or training speech and motion jointly. The motion module must then be retrained whenever the dialogue model changes, cannot be attached to cloud APIs that expose only audio, and entangles role, voice, and motion style. We propose BASE, a backend-agnostic streaming embodiment layer whose only interface to the dialogue model is its emitted speech. First, a conversation state manager driven solely by audio handles speaking, listening, idling, barge-in, and proactive turns on one timeline, while role, voice, motion style, and 3D appearance are set independently. Second, to run an offline 2 s flow-matching gesture model on live audio, we reformulate inference as sliding-window continuation with overlapped look-ahead ensembling, which removes seam jitter. Third, we show that the remaining streaming gap comes from errors accumulating in the self-generated motion history rather than missing future speech; our Drift-Aware History Perturbation (DAHP) reduces this gap in about 50 min on one GPU by injecting inference-like drift into ground-truth training histories, and transfers to a second generator. On BEAT2, streaming BASE reaches an FGD of 0.342, on par with the tightly coupled MIBURI (0.333), and viewers prefer its body motion over MIBURI's in 82% of forced-choice judgments. Without retraining, the same layer drives a cascaded pipeline, three open full-duplex models, and a cloud API in real time.

---


### 440. [Trustworthy Speech-Based Autism Screening under Class Imbalance with Uncertainty-Aware HuBERT Ensembles](https://arxiv.org/abs/2611.30390)

**<font color=#1a73e8>作者：</font>** Nihel Loubna Ghennani, Mourtada Benazzouz, Julie Mauclair  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early screening of Autism Spectrum Disorder (ASD) is critical for timely clinical intervention, although establishing reliable speech based screening systems remains problematic due to limited clinical data, class imbalance, and the need for reliable uncertainty estimation. We propose an uncertainty-aware ASD screening framework based on self-supervised HuBERT representations, combining Leave-One-Subject-Out (LOSO) crossvalidation, balanced k-bagging, and Monte Carlo (MC) Dropout. Multiple HuBERT models are fine-tuned on balanced subsets, with predictions combined through probability-based ensemble averaging and aggregated at the subject level. Experiments on the Child Pathological Speech Database (CPSD) show strong performance, achieving 86.30% balanced accuracy and 93.74% ROC-AUC at the utterance level, and 95.04% and 96.30%, respectively, at the subject level. Furthermore, predictive entropy effectively reflects classification reliability: incorrectly classified segments show higher entropy than correctly classified ones (0.4605 $\pm$ 0.2314 vs. 0.1717 $\pm$ 0.1830), with a significant correlation with errors (r = 0.3981, p = 7.38 x 10 -170 ) and an error-detection ROC-AUC of 0.8359. These results demonstrate the potential of the proposed framework as a robust and uncertainty-aware computer-aided tool for ASD screening.

---


### 441. [LiquidGazeNet: Towards Event-Based Near-Eye Gaze Estimation under Low-Light Conditions](https://arxiv.org/abs/2611.30392)

**<font color=#1a73e8>作者：</font>** Himanshu Kumar, Sanjay Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Near-eye gaze estimation under low-light nighttime conditions is challenging because the quality and effective temporal resolution of conventional intensity frames can be reduced. This paper presents LiquidGazeNet, an event-only gaze-estimation framework that combines polarity-aware spike-latency encoding with a custom LTC-based recurrent module. Positive- and negative-polarity events are represented in separate channels, while exponentially decayed time surfaces retain per-pixel temporal recency across successive event windows. A shared convolutional encoder extracts spatial features from each window, and a two-layer recurrent module composed of LTC-inspired cells integrates them causally over short temporal sequences. The network is trained using a hybrid objective that combines screen-space coordinate regression with centre-referenced directional consistency. The framework is evaluated on Gaze-FELL under cross-subject and cross-scene protocols and is further assessed through event-representation, temporal-module, window-duration, and computational ablations. LiquidGazeNet achieves mean errors of 3.75 degrees and 2.41 degrees under cross-subject and cross-scene evaluation, respectively. The results indicate that polarity-aware temporal-recency encoding, together with recurrent integration, is effective for event-only gaze estimation under the evaluated low-light nighttime conditions.

---


### 442. [WEPWAWET-CORE: A Hardware-Resident ML-DSA Architecture with Fabric-Generated, Fabric-Sealed Keys for Post-Quantum Avionics](https://arxiv.org/abs/2611.30396)

**<font color=#1a73e8>作者：</font>** Mohamed El-Hadedy, Wen-Mei Hwu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Spacecraft that exchange commands over crosslinks need quantum-resistant signatures, for which the Module-Lattice-Based Digital Signature Algorithm (ML-DSA, FIPS 204) is the standard, yet a software signer runs its data-dependent rejection loop, and keeps its key, on cores and memory shared with attitude control and payload processing. This paper shows that for a hardware-assisted signer the cost that matters is not the arithmetic but the number of times the processor crosses into the fabric, and that the boundary which minimizes those crossings is also where the key can be sealed. A gem5-supported analysis of three control granularities over the same kernels shows that only one job per signature, with the whole rejection loop on chip, takes the processor off the critical path. WEPWAWET-CORE realizes that boundary on an XCZU3EG at 300 MHz: a ROM microsequencer runs Sign, Verify, and key generation as three programs over one datapath and a banked scratchpad, and keeps the key, the on-die entropy, and the mask seed off the processor bus. The processor-side cost of a signature falls from over a second under per-kernel control to 0.53 ms, fixed whatever the number of rejections, and the fabric's time per attempt varies by less than 0.1% under a saturating workload. Under NASA JPL's F Prime with attitude-control and imaging loads, two nodes with fabric-generated, ground-certified keys exchanged 3,575 signed frames, every frame was accepted, and no attitude deadline was missed. A cycle profile places the remaining distance to dedicated cores in two serial units.

---


### 443. [Event-Driven Parameter Dynamics for Spatiotemporal Parameter-Update Application in Deep Learning](https://arxiv.org/abs/2611.30397)

**<font color=#1a73e8>作者：</font>** Ruixue Li, Chaofei Hong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Standard neural network training typically applies optimizer-generated update signals to model parameters at every iteration. This work introduces a spatiotemporal view of parameter updating and proposes Event-Driven Parameter Dynamics (EPD), which separates candidate-update generation from their application through an intermediate state with accumulation, event-triggered release, and reset. In a canonical coordinate-wise instantiation, accumulation produces temporal integration, release imposes a spatial budget, and reset separates successive inter-release intervals, while conventional dense updating is recovered as a boundary case. Across four model--optimizer configurations on CIFAR-100, EPD maintains final performance close to conventional training even when only a small fraction of coordinates are released at each step, including the 1\% regime. Matched-control experiments further show that temporal accumulation, state-dependent selection, and post-release reset each contribute to the observed behavior. Together, these results identify parameter-update realization as a controllable dimension of optimization and provide a concrete basis for studying its temporal and spatial organization separately from candidate-update generation.

---


### 444. [GeLiFiSH: Recursive LiDAR Keypoint Estimation with Ground and Moving Object Segmentation](https://arxiv.org/abs/2611.30402)

**<font color=#1a73e8>作者：</font>** Nikolaos Stathoulopoulos, George Nikolakopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR registration and loop closure often rely on sparse keypoints, which must remain repeatable across sessions, viewpoints, and sensors. To handle differing scan patterns, detectors typically operate on accumulated submaps, which introduces latency and processes each submap independently, so repeated observations are never fused. Height-based detectors also reference structure to an estimated ground, so its inconsistency across sessions propagates into the keypoints. Moreover, dynamic objects leave ghost trails that can be mistaken for static structure. We present GeLiFiSH (Geometric LiDAR Filtering with Sequential Hypothesis testing), a learning-free filter that recursively estimates persistent keypoints at scan rate. A height-structure detector runs on a rolling voxel map, and detections initialize tracks with a position, covariance, and existence probability, accepted or rejected by a sequential probability ratio test. Ground segmentation provides a sensor-agnostic height reference, and moving object segmentation removes dynamic points before map insertion. On SemanticKITTI, HeLiMOS, and HeLiPR, spanning five LiDARs and multiple sessions, GeLiFiSH attains the highest average keypoint repeatability among the compared detectors and the second-highest cross-session registration recall from keypoints alone, behind ISS which extracts four times as many keypoints. With one parameter set and no sensor-height prior, both ground and moving object segmentation modules outperform their baselines on average.

---


### 445. [Does coverage explain core-set active learning? Mean, max, and the choice of distance](https://arxiv.org/abs/2611.30450)

**<font color=#1a73e8>作者：</font>** Ferdinand Equilbey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Core-set selection casts batch active learning as a covering problem, in which the points to label minimise the covering radius of the pool. Its main argument is a generalization bound in which this radius controls the gap between the loss on the pool and on the labelled sample. We examine what this bound requires and what it says in practice. We first state it with the assumption that its proof uses at the labelled points, a zero conditional risk, and show that it then holds for any dissimilarity and any selection rule that uses no label outside the sample. The proof works point by point and involves two averages, the mean distance of the pool to the labelled sample and the purity of the cells attached to the labelled points. Keeping them gives, when labels are deterministic at the labelled points, a bound on the pool loss with no zero-loss assumption and without the factor C, the number of classes, of the original constant. We then compare scales, for deterministic labels and a regression function Lipschitz on the whole pool. With the original constant, the bound can be informative only if the radius is below the smallest distance between two classes divided by C. Without C, its radius form can be informative only once the nearest-neighbour rule built on the sample is exact on the pool. Finally, a misalignment criterion measures whether a quantity ranks selections as the gap or the test error do. Experiments on a Gaussian pool and on two image pools, digits and MNIST, the latter under eight distances, and with a network retrained at each cycle, show that the radius does not rank selections consistently with the gap and, on the image pools, that the bounds that do not use the labels of the pool are never informative and that covering in mean rather than in maximum, as greedy k-medoids does, gives a higher purity and accuracy than random sampling.

---


### 446. [PLATRS: A Lattice-Based Linkable Accountable Ring Signature for Permissioned Blockchains](https://arxiv.org/abs/2611.30453)

**<font color=#1a73e8>作者：</font>** Jie Zhang, Xiaohong Li, Honglin Mao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Permissioned-ledger cross-domain data sharing needs anonymity and accountability: an endorsement hides its author, but a regulator must identify it on authorization reuse. Existing lattice-based schemes give these only separately: public traceability exposes signers to collision detectors; linkable non-tracing schemes cannot open; threshold schemes solve another problem. None gives post-quantum security, a signer-chosen ring, a publicly comparable per-event tag, and one-authority opening together.
We propose \textsf{PLATRS}, a module-lattice linkable accountable ring signature for permissioned blockchains. Consortium-CA enrollment binds the key returned by an opening to a registered identity. The signer chooses the ring; verification is index-free; each signature has a per-event tag any verifier can compare. Tag noise derives from the signer's tracing secret and event, so linking is one comparison for honest signatures while the tag remains M-LWE without the secret. Detection is two-tier: tag mismatch is immediate; different tags on two accepted signatures for one event trigger an opening; the authority publishes the recovered public opening component, and any member recomputes the verdict against the ring. We prove CPA anonymity from M-LWE, linkability, authority-only traceability, and unforgeability from M-SIS with M-LWE in the random oracle model. At \(N=1024\), our open-source implementation: sign 9.886~ms, verify 3.919~ms, link 0.7~\(\mu\)s, open 480~\(\mu\)s; signature 107.3~KiB (log in ring size); adjudication 4.867~ms. Hyperledger Fabric: 60.5 signature submissions/s at 7.87~MB/s with 16~MiB blocks, commit-bandwidth limited. Common-harness: fastest of 5 schemes to sign/verify, second in size; vs FLLL\(^+\)21, signing is 3188\(\times\) faster and signatures 133\(\times\) shorter.

---


### 447. [LiveMirror: Real-Time Diffusion Virtual Try-On on a Consumer GPU and Its Self-Supervised Adaptation to Indian Ethnic Wear](https://arxiv.org/abs/2611.30461)

**<font color=#1a73e8>作者：</font>** Jigyansha Jeevan Rout, Sukanta Kumar Sabut  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion virtual try-on (VTO) models produce convincing garment transfers from a single product photograph, but at hundreds of milliseconds to seconds per image every deployment today is offline or falls back to AR mirrors that need a rigged 3D asset per product. We present LiveMirror, a live-camera try-on mirror that renders a flat garment photograph onto a moving person with a diffusion model on one 16 GB consumer GPU. Its core is asynchronous keyframe try-on: generation never blocks the display, every displayed frame is an optical-flow warp of the latest generated keyframe, and keyframes are replaced only through a cross-fade. The display runs at camera rate (25 FPS at 720p) while a new try-on arrives every 370-490 ms; we measure the residual flicker, give a stage-by-stage latency budget, and report which accelerations (step count, consistency LoRA, tiny decoder, compilation) keep garment prints intact. We then show that the same GPU fixes the model's biggest cultural blind spot: try-on models trained on VITON-HD and DressCode render a knee-length kurta or sherwani as a torso-length top or a dress over bare legs. A thigh-covering mask, self-supervised pairs built automatically from 24.9k on-model e-commerce photographs, and 3.2 GPU-hours of attention-only fine-tuning of CatVTON halve the perceptual error on ethnic wear (LPIPS 0.137 to 0.077 on IndoFashion, 0.135 to 0.073 on Atlas; 200 held-out pairs per source) with no regression on Western tops. A two-pass hem-aware mask then removes the remaining failure, recoloured trousers below the hem, on all but 3-4% of pairs at no training cost; in the mirror the hem comes from the previous keyframe for free. The adapted model beats FASHN VTON 1.5 on every aggregate ethnic-wear metric at about $20\times$ lower inference cost, and its weights drop straight into the mirror.

---


### 448. [SGD Selects Initialization-Dependent Representation in Overparameterized ReLU Networks](https://arxiv.org/abs/2611.30467)

**<font color=#1a73e8>作者：</font>** Nikos Tsikouras, Yorgos Pantis, Ahmed Mehdi Inane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Overparameterized neural networks can represent the same function through many different hidden configurations, raising the question of which representation is favored by a given training algorithm. We study how stochastic gradient descent (SGD), jointly training both layers, resolves this ambiguity in finite-width, bias-free, two-layer ReLU networks trained to learn a linear teacher under Gaussian inputs. At width two, exact fitting leaves no choice: the neurons must align with the teacher directions. At every width $m \ge 4$, however, infinitely many non-aligned exact fits are possible. Despite this ambiguity, we prove that joint batch-size-one SGD from sufficiently small initialization drives every neuron arbitrarily close to one of the two teacher directions while reaching arbitrarily small population error in finite time. This occurs without explicit regularization, layerwise training, gradient clipping, or a learning-rate schedule. The dynamics additionally select an initialization-dependent allocation of the fitted function across neurons, providing a finer characterization of the representation selected by SGD. Numerical experiments reproduce the predicted alignment, fitting, and initialization-dependent allocation. Our results identify sufficient conditions under which standard SGD exhibits a strong implicit bias toward a highly structured internal representation, even when overparameterization creates infinitely many qualitatively different exact representations.

---


### 449. [Struct2Det: Grounding Category Structure in Visual Evidence for Few-Shot Object Detection](https://arxiv.org/abs/2611.30469)

**<font color=#1a73e8>作者：</font>** Kaixuan Chang, Huabing Zhou, Yanduo Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot detectors struggle to distinguish categories that look alike but differ in local components, because a few examples rarely reveal which differences determine category identity. Category descriptions specify components and relations but do not establish their presence in an image. We propose Struct2Det, which uses category structure to guide detection and verify candidates in three stages. Relational Structure Encoding maps category graphs to component embeddings and a global condition. Component-Grounded Detection uses component queries to retrieve multi-scale image evidence that, with the global condition, modulates category text embeddings for initial detection. Verification-Guided Refinement matches candidate regions with components expected by their top-scoring categories; when class scores are close and matches are reliable, matched pairs correct region features before the shared detector predicts again. Category structure informs both classification inputs: text embeddings integrate image-wide component evidence, while region features incorporate candidate-specific matches. We also construct InduSym, with 88,912 symbol instances across 275 categories from 674 engineering drawings and a structural graph per category. Struct2Det improves few-shot-category AP over the strongest baseline by 6.02 points on InduSym and 9.68 on Digitize-PID, with the highest base-category AP on both. InduSym ablations show few-shot gains from correct category structure, image-level retrieval, and candidate verification. Further tests show gains in few-shot natural-object detection and zero-shot Chinese character recognition.

---


### 450. [Inclusion of obstacles in ground point classification in ALS data for terrain models used for analysis of vehicle traversability](https://arxiv.org/abs/2611.30471)

**<font color=#1a73e8>作者：</font>** Mikael Lundbäck, Erik Wallin, Sima Mohtasami 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classification of ALS point clouds has been studied for decades, but it remains challenging in forest contexts due to the great variety of terrain types, sensor equipment, flight parameters, and resulting point densities. Point cloud density has increased significantly in recent years, and existing algorithms, developed for lower density point clouds, may no longer be effective. It is beyond the scope of most existing algorithms to classify obstacles, such as boulders, while also distinguishing non-obstacles, such as bushes and undergrowth. We evaluate the performance of different algorithms for ground point classification in ALS data in a context where obstacles are included in the ground class, resulting in terrain models useful for offroad machinery route planning and navigation. The evaluation is performed using metrics directly on the point clouds (Precision, Recall, $F_1$-score) and on resulting terrain models (RMSE and maps of differences). The results show that there are several algorithms that perform well, but performance is highly affected by the parameters used. The best results in terms of terrain model RMSE are obtained with the CSF-algorithm, with an average RMSE of 0.08 meters. The results indicate that existing algorithms can be adapted to include obstacles in the ground class under the tested conditions.

---


> [!TIP]
> 当前位于：**401-450**（第 9/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
