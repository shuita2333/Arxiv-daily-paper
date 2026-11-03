# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**551-600**（第 12/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-633](./part-13.md)

---

### 551. [ComplianceAtlas: A Taxonomy-Driven Agentic AI Framework for Automated AI Act Gap Analysis and Remediation](https://arxiv.org/abs/2611.03121)

**<font color=#1a73e8>作者：</font>** Ilias Driouich, Hongliu Cao, Eoin Thomas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assessing regulatory compliance for high-risk AI systems requires systematic identification of technical gaps such as missing controls, in- adequate processes, or shallow evaluation of practices. Compliance officers typically admin- ister structured questionnaires collecting evi- dence of current practices, where organizations respond with descriptions of their existing pro- cesses, technical capabilities, and architectural choices. However, translating these compli- ance questionnaire responses into typed, ac- tionable gap diagnoses remains unsystematic. In this paper, we present a literature-grounded taxonomy of technical compliance gaps cover- ing areas such as accuracy, robustness, logging, and human oversight, and embed it in GapTo- Compliance, a two-stage agentic framework coordinating two specialized agents: a Gap Extraction Agent that performs hierarchical rea- soning from compliance areas to specific gap types, and a Remediation Planning Agent that ranks remediation actions from a remediation catalog via multi-signal scoring combining se- mantic similarity, regulatory alignment, and effort estimation. We evaluate this framework against four automatic compliance gap detec- tion baselines across 9 AI systems and 6 AI families. Our approach achieves a gap-type F1 of 0.831 (vs. 0.533 for the strongest baseline) and remediation P@5 of 0.872 (vs. 0.635 for retrieval methods), demonstrating promising potential for automated compliance workflows. The structured agent coordination reveals a path toward human-in-the-loop compliance systems where automated gap extraction reduces expert burden while maintaining auditability, and the taxonomy-driven design enables extension to emerging regulatory frameworks beyond

---


### 552. [An Information Hierarchy of Privacy Filters and Odometers](https://arxiv.org/abs/2611.03130)

**<font color=#1a73e8>作者：</font>** Sophie Taylor, Praneeth Vippathalla, Justin P. Coon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In sequential data analysis, privacy loss accumulates over time, and privacy filters and odometers are used to control and track this cumulative cost. We study how the information used by differential privacy filters and odometers fundamentally limits what they can achieve. We formalise three levels of information: spec-level information, fixed prior to the interaction; mechanism-level information, which includes the mechanisms instantiated during the interaction; and realisation-level information, which further includes the realised interaction. We classify privacy filters and odometers by the least informative level sufficient to determine their behaviour.
Our main results establish strict and arbitrarily large separations in achievable performance across this information hierarchy. For privacy filters, moving up the hierarchy can yield an unbounded utility advantage, quantified by a clipped measure of the number of allowed releases. For privacy odometers, it can yield an arbitrarily large improvement in precision, quantified by the expected peak excess of the reported bound over the realised privacy loss. Further, although the information classes are distinct, we show that moving to a richer class need incur essentially no loss in performance.
Finally, we show that randomisation provides a resource orthogonal to information: at every information level, it can yield an arbitrarily large utility improvement over deterministic filters. Thus, information access and randomisation can be viewed as fundamental resources governing privacy procedures in adaptive interactions.

---


### 553. [Znaki: A Russian Fingerspelling Recognition Dataset](https://arxiv.org/abs/2611.03136)

**<font color=#1a73e8>作者：</font>** Petr Surovtsev, Pavel Korotaev, Alexander Nagaev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fingerspelling - the sequential signing of letters that compose proper names, technical terms, and out-of-vocabulary words - is an integral component of any sign language. Despite Russian Sign Language (RSL) being used by more than 150,000 native signers, no public fingerspelling dataset for RSL exists, in contrast to American, British, German, and several other sign languages. We introduce Znaki the first open RSL fingerspelling dataset: 37,252 video recordings (35.4 hours) of 1,593 unique sequences - proper names sampled from 16 domain categories - recorded by 68 native RSL signers (37 Deaf, 29 hard-of-hearing, and 2 certified interpreters) through a crowdsourcing pipeline with a two-stage signer qualification procedure and expert validation. The dataset covers all 33 Cyrillic handshapes, and its letter-frequency distribution matches the Russian National Corpus. As reference points for future research, we establish two baselines adapted from American Sign Language fingerspelling recognition: a Squeezeformer-based encoder-decoder, reaching a character-level accuracy ($1-\mathrm{CER}$) of 0.932 and a sequence accuracy of 0.596, and Fingerspelling-PoseNet, reaching 0.886 and 0.545, respectively.

---


### 554. [When Optimization Meets Human Intent: Human-Centered Diffusion Model Optimization](https://arxiv.org/abs/2611.03140)

**<font color=#1a73e8>作者：</font>** Renye Yan, Jikang Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models are evolving from general tools into personalized systems that adapt to user needs through fine-tuning and guidance. However, diffusion optimization mainly targets measurable objectives such as aesthetics, rarely examining whether they align with human intent. Human needs are multidimensional, contextual, and dynamic, whereas existing methods approximate them with fixed metrics. Because these metrics capture human needs only partially and may amplify deviations from true intent during optimization, higher scores need not yield results better matching human expectations. To understand how human needs enter and influence optimization, we systematically analyze how human intent is expressed, translated into optimizable objectives, applied to model behavior or generation, and evaluated through outputs. We further discuss trade-offs affecting human-intent alignment in personalized image generation and gaps between automated metrics and real user judgments. This human-centered synthesis reorganizes diffusion optimization and provides a systematic reference for personalized generation systems designed for human preferences.

---


### 555. [Visual-to-Executable Procedural Reconstruction of Buildings](https://arxiv.org/abs/2611.03143)

**<font color=#1a73e8>作者：</font>** Zichong Zhu, Zhihao Liu, Andrei Sharf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Procedural modeling offers compact, editable, and reusable representations for architectural content, but building such models still depends heavily on manually authored grammars. We study image-based procedural building reconstruction from in-the-wild images, with the goal of recovering an executable procedural description that can be instantiated as an editable 3D building asset. Because a single image provides only partial and view-dependent evidence, we focus on recovering the dominant visible facade(s) and attach the recovered facade program to a simple mass model for building-level instantiation. Our method decomposes this task into two structured prediction stages. First, a Global Structure Layout Tree recovers facade-scale split-and-repeat organization through a fine-tuned layout model with render-guided visual-symbolic reflection. Second, a Component Parameterization schema maps representative facade tiles to structured procedural attributes for local architectural component synthesis. These two representations are then deterministically compiled into executable Computer Generated Architecture (CGA) programs, avoiding the brittleness of direct low-level program generation. Experiments show that the proposed framework handles both regular facades and challenging in-the-wild images, while maintaining high structural consistency, procedural executability, and fine-grained architectural detail. The recovered programs further enable controllable and reusable 3D building asset generation.

---


### 556. [FlowBatt: Flow Matching for Probabilistic Battery Degradation Prediction](https://arxiv.org/abs/2611.03150)

**<font color=#1a73e8>作者：</font>** Hamidreza Eivazi, Eslam Sharaawy, Stefan Wittek 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Battery degradation remains a central challenge in the development and broad application of sustainable energy technologies. Accurate degradation prediction is challenging, as battery aging emerges from complex and heterogeneous interactions among cycling behavior, operating conditions, and cell chemistry. Existing machine-learning approaches typically focus on deterministic end-of-life predictions or modeling degradation curves within fixed chemistry settings, leaving probabilistic state of health (SOH) trajectory modeling across heterogeneous chemistries underexplored. We introduce FlowBatt, a use-inspired conditional generative framework that adapts flow matching with a diffusion transformer (DiT) backbone to battery degradation trajectory modeling. FlowBatt models full SOH trajectories as probabilistic degradation processes conditioned on early-cycle capacity data. To strengthen this conditioning pathway, we use explainable AI analysis to diagnose and improve the encoder that maps early-cycle capacity matrices into conditioning vectors. We evaluate FlowBatt on five public benchmark settings spanning diverse chemistries and aging conditions, comparing it with supervised and diffusion-based trajectory models as well as established baselines for remaining useful life (RUL) prediction under shared data splits. FlowBatt achieves the best trajectory-wise SOH prediction performance on all five datasets, with errors below 2.5%, and delivers competitive RUL prediction performance. By generating multiple plausible trajectories, FlowBatt provides empirical prediction intervals for battery degradation modeling. These results indicate that flow-matching-based trajectory modeling is a promising framework for probabilistic battery health prediction.

---


### 557. [From PID to Reinforcement Learning in Building HVAC Control: A Control-Architecture Review of Tuning Strategies, Formulations, and Deployment Trade-offs](https://arxiv.org/abs/2611.03152)

**<font color=#1a73e8>作者：</font>** Erfan Haghighat Damavandi, Davide Papurello, Mahdi Alibeigi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper reviews control architectures for building heating, ventilation and air-conditioning (HVAC) systems, addressing the tension among energy demand, occupant comfort and equipment operability, and situating proportional-integral-derivative (PID) regulation within a layered control stack that also includes rule-based and model-based supervisory control and data-driven reinforcement learning (RL). It examines the thermostat-PID layer from two-position and scheduled setpoint control through proportional, PI and PID regulation and their tuning, then formulates RL for building control as a Markov decision process. Its central contribution is a taxonomy of where RL meets PID: RL as a gain tuner for an existing loop, as a direct replacement for the regulatory controller, as a hybrid with model predictive control, and as supervisory setpoint and schedule generation. Across these classes, the review establishes that the physical loop remains invariant while the intervention point changes, and that the classes differ in their requirements for actuation authority, state information, modelling, commissioning and constraint handling. It further establishes that PID is inexpensive and well codified but limited by nonlinearity, time variation, discrete mode switching, loop interaction and slow plant dynamics, while RL's admissible position must be argued rather than assumed. The paper concludes that these architectures are not competing philosophies of control but nested points of attachment on one HVAC plant, with hybrid implementations possible, and that deployment trade-offs must be assessed according to the specific control interface and scaffolding required.

---


### 558. [PaddleMaterials: An End-to-End Deep Learning Toolkit for Materials Science](https://arxiv.org/abs/2611.03154)

**<font color=#1a73e8>作者：</font>** Xuwei Liu, Zhimin Zhang, Xiaoguang Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning supports materials design, atomistic simulation and experimental characterization, yet models and workflows remain fragmented. We present PaddleMaterials, an open-source framework integrating heterogeneous materials-learning tasks while preserving task-specific representations and scientific semantics. It unifies data processing, training, evaluation, pretrained-model management and workflows across six task classes: property prediction, structure generation, machine-learning interatomic potentials, electronic-structure fields, spectrum elucidation and microscopy image processing. Task interfaces record physical quantities, units, aggregation conventions and references, making cross-task composition verifiable. A shared compiler backend enables switching from dynamic-graph to compiled execution through one setting, using graph optimization, operator fusion and hardware-targeted code generation without changing model definitions. Across 65 model instances in 11 groups, compiled execution accelerated every instance in eight groups, with group median speedups of 11%-224% and group maximum speedups of 11%-336%. Case studies on LiMnO2 and toluene link structure generation or spectrum elucidation, interatomic-potential relaxation, property prediction and electron-density prediction, using same-geometry density functional theory (DFT) calculations as references. For LiMnO2, predicted formation energies for generated and relaxed structures differed from same-geometry PBE+U references by at most 7 meV per atom, while the computational cost of model steps was less than one-twentieth of a DFT single-point calculation. PaddleMaterials extends unified materials workflows beyond conventional property, potential and structure-generation tasks while supporting verifiable cross-task operations and compiled execution.

---


### 559. [Dissecting Geometric Constraints in Grokking: Interaction-Dependent Acceleration in Modular Arithmetic](https://arxiv.org/abs/2611.03156)

**<font color=#1a73e8>作者：</font>** Zachary A. Hampton, Wasiq Khan, Bilal Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spherical transformer configurations can accelerate grokking through simultaneous modifications of several model properties. The present study investigated the contributions of these modifications in the published Sphere+Fourier configuration using 960 controlled modular-arithmetic runs. A complete factorial analysis varied residual projection, readout weight normalization, logit scale, and weight decay. Across four matched settings with weight decay, the successful-run mean crossing times without projection were 8-37 times those observed with projection. However, residual projection was insufficient to induce grokking without additional interventions. Various other unprojected configurations also generalized. Since projection altered the magnitude entering the readout, these comparisons could not separate geometry from output scale. A separate 100-run fixed-horizon study demonstrated faster first crossing for the complete configuration across five train/test partitions. Faster crossing did not necessarily correspond to greater persistence over extended training. Control experiments demonstrated rapid grokking without Fourier initialization. Task and depth sweeps also identified conditions in which the configuration failed to reach the criterion by 50K epochs. Accordingly, the observed acceleration depended on interactions among the components and did not extend uniformly across the tested tasks or depths.

---


### 560. [ViAdminShift: A Vietnamese Benchmark for Event-Level Knowledge Updates Built from the 2025 Administrative Reform](https://arxiv.org/abs/2611.03171)

**<font color=#1a73e8>作者：</font>** Phan Binh Nguyen Lam, Nguyen Thai Anh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On July 1, 2025, Vietnam reduced its 63 provinces to 34, abolished its 696 districts, and replaced its 10,035 commune-level units (wards) with 3,321. ViAdminShift, a Vietnamese language resource about this event, consists of 7,995 benchmark items, 2,281 retrieval passages from pre- and post-reform Wikipedia revisions and dated templates, and old-to-new tables that a released script rebuilds from the official conversion table (not redistributed). Changed items store the pre-reform answer (except 121 address items), a $2\times2$ design uses untouched units as controls, and 400 addresses appear without diacritics. The tables agree with an independent lineage on 10,564 of 10,565 official pairs, disagreements were settled against the resolutions, and the probing-track scorer agrees with both authors' blind labels (Cohen's $\kappa=0.91$ and $0.89$). Data, outputs, code, and a datasheet are released. In the probing track, at least 20 of 67 models know the reform. Fourteen of them give the new province alone for at most 11% of plain questions about old addresses (old province only: 14-100%); a bare date recovers up to 100%. Post hoc (80 province-free addresses, single runs), with reasoning off, today's date in the system prompt leaves 68-100% old-province-only answers for 10 of 12 models; with reasoning, an "as of" prefix in the question leaves none for seven of eight. On the 1,262-item benchmark subset, with same-source old and new passages, small models unaware of the reform give 14-30% outdated answers and the five benchmark-track knowers (also differing in size or provider) 0-5%.

---


### 561. [Auto-Research Agent on MSA Organization to Improve Protein-Protein Complex Structure Prediction](https://arxiv.org/abs/2611.03183)

**<font color=#1a73e8>作者：</font>** Zilu Zhang, Jing Bao, Lifeng Qiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Protein-complex structure prediction with AlphaFold 3 depends on MSA content, depth, and cross-chain pairing. Current pipelines apply uniform recipes, typically maximizing depth and pairing by species, yet even whether cross-chain pairing helps AF3 remains contested. We show that the value of both depth and pairing is strongly target-dependent, so no single recipe is optimal across interfaces. We introduce an autonomous agent that treats a frozen AF3 as a black-box experimental instrument. For each target, the agent formulates biological hypotheses, analyzes and reorganizes the MSA, and iteratively refines sequence selection and pairing using predictor label-free signals alone. On 1{,}015 protein--protein interfaces from three benchmarks released after AF3's training cutoff, the agent improves overall interface DockQ over AF3's default pipeline and fixed MSA recipes on every benchmark, while using on average 60\% fewer MSA sequences than the default. Gains are largest for inter-species heteromers, where species-based pairing is unreliable: mean DockQ increases from 0.465 to 0.612 on FoldBench and from 0.482 to 0.562 on HD439. The improvements arise from both sequence construction and pairing policy, including deliberate this http URL results recast MSA design as a target-specific problem and show that an autonomous agent can adapt it at test time through biological reasoning and self-directed, confidence-guided experimentation.

---


### 562. [MoSoLoco: Monocular 3D Human Localization through Visual Latent Features and Social Context](https://arxiv.org/abs/2611.03189)

**<font color=#1a73e8>作者：</font>** Yasamin Borhani, Javad Khoramdel, Yang Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating the metric 3D position of people from a monocular camera is important for robot navigation and motion prediction. Lightweight pose-based localizers are attractive for robotic hardware with limited computational resources because they operate on compact 2D keypoints. However, they typically discard the richer visual representations computed by the pose estimator. We introduce MoSoLoco, a per-frame monocular 3D human localizer that combines the pose detector's internal visual features with the detected 2D skeleton, without requiring an additional RGB or depth encoder. MoSoLoco can further incorporate sparse same-frame multi-person context to refine individual position estimates. Experiments on JRDB and NuScenes show that reusing pose-detector representations improves localization, reducing the best JRDB error by approximately 23 percent relative to the strongest evaluated keypoint-based baseline. A sparse social-interaction module incorporates nearby detections from the same image for further refinement. Controlled trajectory-forecasting experiments show downstream benefits, while the complete pipeline remains suitable for efficient Jetson AGX Xavier inference.

---


### 563. [Toward Deployable Hardware Roots of Trust for Edge AI: Software PUFs and Their Trade-offs](https://arxiv.org/abs/2611.03194)

**<font color=#1a73e8>作者：</font>** Yilin Li, Farhad Merchant  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deploying AI at the edge increases the need for security features on existing devices. When physical access to the device is available, storing secret keys in non-volatile memory is vulnerable. Physical unclonable functions (PUFs) address this by exploiting the unique yet repeatable characteristics of each device, but conventional implementations require design-stage modifications, making them inapplicable to a vast number of existing devices already manufactured. Recently, software PUFs have emerged as an alternative approach, leveraging analog characteristics exposed through software-only interfaces to derive unique responses, without post-fabrication changes. Since edge AI hardware is bound to long operational lifespans, this offers clear economic and engineering value. Existing research on software PUFs remains fragmented. It lacks a holistic review of the trade-offs among choices of components used as entropy sources and software methods to expose analog characteristics. This gap hinders assessing feasibility, comparing approaches, and identifying open challenges towards a hardware root of trust in existing devices. This paper surveys 37 existing software PUF works and compares them against the requirements of on-device model protection: boot-time versus runtime key derivation, and response latency. It analyzes trade-offs, outlines four key challenges that current software PUFs face for edge AI deployment, and highlights promising directions for overcoming barriers to real-world adoption.

---


### 564. [On the Convergence of Vanilla Adam under Heavy-Tailed Noise and Index Sampling](https://arxiv.org/abs/2611.03201)

**<font color=#1a73e8>作者：</font>** Kanata Oowada, Hideaki Iiduka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how stochastic gradient noise affects the convergence of Adam is an important problem in stochastic optimization, particularly when the noise exhibits heavy-tailed behavior. In this paper, we investigate the convergence of vanilla Adam in both the expected risk and the empirical risk minimization, focusing on the effects of heavy-tailed noise and its relationship to index sampling. For the expected risk minimization, we establish convergence guarantees under Hölder smoothness and bounded $\mathfrak{p}$-th moment assumptions, allowing stochastic gradient noise with infinite variance. Our analysis provides explicit upper bounds on the expected squared gradient norm and shows that the iteration-dependent convergence term decays more slowly as $\mathfrak{p}$ decreases. For the empirical risk minimization, we establish asymptotic and non-asymptotic convergence guarantees and demonstrate that heavy-tailed population noise can deteriorate convergence bounds through dataset-dependent constants as the dataset size increases. Furthermore, under Lipschitz smoothness, we formulate multistage Adam with practical learning rate schedules and demonstrate that increasing batch sizes can reduce index-sampling noise and improve convergence guarantees and SFO complexity. Numerical experiments support our theoretical findings on the effects of heavy-tailed noise and the computational benefits of increasing batch sizes.

---


### 565. [CERBO: Certified Recourse at a Requested Rate for Gradient-Boosted Trees](https://arxiv.org/abs/2611.03222)

**<font color=#1a73e8>作者：</font>** Farhan Shahriyar Hossain, Taufikur Rahman Fuad, Md. Zarif Bin Hasnat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recourse-aware learning trains models so that people who receive an adverse decision can reverse it with an affordable change. For gradient-boosted decision trees (GBDTs), the existing method, RABIT, exposes a single recourse weight whose effect on the recourse rate is abrupt and data-dependent, and its training bound cannot certify recourse for any rejected individual. We present Certified Recourse Boosting (CERBO), which takes a requested recourse rate and returns a GBDT with certified actions: it tracks exact additive effort along tree paths, trains against committed boxes (a family of bounds that contains RABIT's and certifies a within-budget action for each training sample) and adjusts the weight after every tree until the certified rate meets the request. A calibration step guarantees the rate on new individuals, and the certifier runs on any tree ensemble, including XGBoost and LightGBM, in milliseconds per person without a solver. In RABIT's own experimental protocol, at equal accuracy, CERBO raises the recourse ratio from 0.90 to 0.99 on FICO and from 0.64 to 0.77 on Bail. Under additive costs on six data sets, it raises the area under the accuracy-recourse frontier in all 12 settings, and in simulated deployments it guarantees recourse to 70% of rejected individuals in 11 of 12 settings, against 2 for RABIT.

---


### 566. [What Structurally Breaks an Agent? Auditing Difficulty in Stateful Tool-Use Workflows](https://arxiv.org/abs/2611.03227)

**<font color=#1a73e8>作者：</font>** Shereen Anand, Ju Wang, Yali Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An aggregate task score does not distinguish failures of scheduling, state retention, and candidate selection. We develop a small executable instrument that varies dependency depth, candidate count, active state width, and access to current-state snapshots while holding the number of required operations fixed. Two dependency-graph families show that increasing depth at fixed work changes both scheduling freedom and the number of reachable completion states, so these controls are coupled, and we quantify the coupling. The primary study contains 49,152 generated tasks and 393,216 reference-controller rollouts. A separately frozen follow-on design adds 295,936 rollouts covering retention strategy, snapshot cadence, hidden state resampling, recovery, query locality, candidate indexing, and relabeling. Residue caches and precomputed plans solve tasks that defeat limited raw-value caches, and indexed selection removes the serial-scan branching deficit. Hidden resampling imposes an exact success ceiling that additional state tracking cannot overcome. The contribution is an executable diagnostic instrument, analytic calibration, and an audit of its assumptions. A small local CPU study with a 0.5B model completed no workflows, and a 16-episode Copilot-routed fractional factorial is descriptive only. Neither supports general capability claims.

---


### 567. [AnchorComplete: Recovering Complete Scene Meshes from Partial Point Clouds](https://arxiv.org/abs/2611.03228)

**<font color=#1a73e8>作者：</font>** Weirong Chen, Ismail El-Yamany, Ganlin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most image-based 3D reconstructors primarily recover visible surfaces, producing partial point clouds with large holes and leaving unobserved geometry unresolved. To address this limitation, we introduce AnchorComplete, a framework that reconstructs complete scene meshes from partial point clouds while preserving observed geometry and supporting scenes of varying scales. Building on TRELLIS.2, our method combines partial-point conditioning, which integrates global scene tokens with local spatial evidence to anchor generation to the input, and metric-scale coarse-to-fine generation, which progressively refines scene geometry within fixed-size windows while maintaining global structural consistency. Experiments on Replica and SCRREAM demonstrate that AnchorComplete consistently outperforms strong baselines in complete-scene reconstruction, particularly under sparse-view settings.

---


### 568. [CL3DOD: Understanding the Stability-Plasticity Dilemma in Outdoor Class-Incremental 3D Object Detection](https://arxiv.org/abs/2611.03229)

**<font color=#1a73e8>作者：</font>** Muhammad Ahmed Ullah Khan, Khalil Ahmed, Didier Stricker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-incremental learning (CIL) for outdoor 3D object detection remains largely underexplored. Existing outdoor studies are limited to single-benchmark evaluations, with SDCoT++ considering KITTI and CL2OD considering nuScenes under different incremental settings. This makes it difficult to assess whether observed continual-learning behavior generalizes across autonomous-driving benchmarks. To the best of our knowledge, we provide the first unified cross-benchmark analysis of outdoor class-incremental 3D object detection across multiple autonomous-driving benchmarks, covering both two-task and multi-stage settings. We investigate: (1) how severely existing 3D detectors forget previously learned classes, (2) how incremental training exposes the stability-plasticity dilemma between knowledge retention and new-class acquisition, and (3) which forms of supervision are most effective for balancing these objectives. We introduce CL3DOD, a class-incremental 3D detection framework that restores missing supervision for previous classes using predictions from the previous-stage detector, preserves old-class responses through query-wise knowledge distillation, and employs EMA-based temporal consistency regularization. Experiments on KITTI and nuScenes reveal a consistent stability-plasticity dilemma across both benchmarks. CL3DOD generally achieves a more favorable stability-plasticity balance than controlled incremental baselines and improves upon published prior methods in the reported benchmark comparisons. This advantage persists across multiple incremental stages, demonstrating strong retention of previously learned knowledge while maintaining effective new-class acquisition. Our code, evaluation setup, and incremental task splits will be publicly released.

---


### 569. [Calibrating Multimodal Test-Time Adaptation under Reliability and Availability Modality Shifts](https://arxiv.org/abs/2611.03232)

**<font color=#1a73e8>作者：</font>** Jiangmeng Li, Jinglin Xu, Yi Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal test-time adaptation (TTA) enables pretrained multimodal models to accommodate distribution shifts during inference using only unlabeled test data, without recourse to the original training data. Compared with unimodal adaptation, multimodal adaptation is further complicated by the coexistence and interaction of multiple representation perspectives. This complexity is particularly pronounced under modality reliability shifts, which preserve modality availability but degrade information quality, and modality availability shifts, which render the corresponding modality entirely inaccessible. Category-conditional Gaussian modeling offers a natural starting point for handling such distributional variations, having proven effective in unimodal test-time adaptation for characterizing representation distributions, yet its extension to multimodal settings requires a more elaborate formulation. To this end, we propose Adaptive Probabilistic Gaussian Calibration (AdaPGC), which extends category-conditional Gaussian modeling across modality-specific and multimodal fusion representations for probabilistic calibration under multimodal distribution shifts. AdaPGC continuously updates category-conditional Gaussian models over modality-specific and fusion representations, using the resulting probabilistic predictions to calibrate source model predictions and guide reliability based rectification, while exploiting their joint distributions to recover unavailable fusion representations. Extensive experiments under diverse modality corruption and missingness conditions demonstrate that AdaPGC effectively improves robustness under both modality reliability and availability shifts. Our source code will be released at this https URL.

---


### 570. [HyperFlow: Class-Incremental Semantic Change Detection via Hyperbolic Flow](https://arxiv.org/abs/2611.03245)

**<font color=#1a73e8>作者：</font>** Manon Béchaz, Léo Buecher, Emanuele Dalsasso 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic change detection in remote sensing aims to identify and characterize land-cover transitions observed in pairs of satellite or aerial images. Existing methods assume a fixed set of change categories, limiting their applicability in real-world scenarios where changes of interest may vary, for example across geographies or over time. In this work, we tackle the problem of class-incremental semantic change detection, where a model progressively learns to detect new types of semantic change. To do so, we exploit the hierarchical structure of land-cover semantics, where newly introduced categories correspond to fine-grained refinements of existing ones, and represent said semantic categories in hyperbolic space, which is particularly well suited to represent such hierarchical relationships. To capture semantic changes, we introduce HyperFlow, a method relying on Busemann prototypes, modeling change as an anomaly in a learned semantic flow within the hyperbolic embedding space induced by segmentation. HyperFlow couples change detection to class-incremental semantic segmentation, enabling class-incremental semantic change detection. We also present HiChange, a new large-scale, high resolution remote sensing dataset with detailed, fine-grained hierarchical labels. Experimental results demonstrate that HyperFlow achieves both strong change detection and semantic segmentation performance across incremental steps. In particular, we show that progressively refining semantic categories, rather than considering them all directly, yields improved change detection, highlighting the benefits of incremental learning for semantic change detection.

---


### 571. [Rethinking Fairness Metrics for Multi-Class and Multi-Group Assessment: Not Everything is Binary](https://arxiv.org/abs/2611.03257)

**<font color=#1a73e8>作者：</font>** Matteo Grazioso, Fabio Naccarella, Chiara Gallese 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence, and Machine Learning in general, is becoming pervasive across all domains and disciplines. By means of this data-driven approach, algorithms can learns complex task just by learning from samples. However, if the data-set is biased, they might lead to the development of unfair computer systems, that is, characterised by a prejudice towards specific individuals or groups, which might get an unmotivated output from the system. This circumstance lead to the development of multiple metrics designed to quantify the level of unfairness of an algorithm. However, a generalised assumption in the literature is that the sensitive features and the output labels are binary. When the data is not binary, it is forcefully binarized using a one-versus-the-rest simplification. In this work, we discuss the limitations of existing metrics and propose novel, mathematically sound, and generalized multi-group and multi-class formulations of the metrics. Ultimately, our results highlight the empirical assessment distortion caused by binarization strategies, which reveals the limitations of binary fairness metrics in the multi class setting.

---


### 572. [DeepWaveRL: Self-Supervised Full Waveform Inversion via Reinforcement Learning](https://arxiv.org/abs/2611.03264)

**<font color=#1a73e8>作者：</font>** Peng Jin, Yinan Feng, Yinpeng Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full Waveform Inversion (FWI) is a fundamental inverse problem in geophysics to estimate subsurface properties, such as velocity, from seismic measurements. Recently, self-supervised learning methods remove the need for ground-truth velocity maps during training by leveraging a forward operator to simulate seismic data from predictions and backpropagate the gradients of reconstruction loss through it. In this work, we consider a more challenging setting without accessing such gradients. To this end, we incorporate reinforcement learning into self-supervised FWI and propose a framework named DeepWaveRL. Specifically, we reformulate FWI as a policy learning problem, where the policy network predicts velocity maps as actions, and a forward operator is used solely for simulation. A global scalar reward is computed based on data misfit for each prediction and used to weight policy gradients. Thus, learning proceeds without accessing the gradients from the forward operator. Given the indirect and coarse supervision signals, we further identify key strategies to stabilize learning and mitigate the spatial credit assignment bottleneck. Experimental results show that, despite relying entirely on a single scalar reward, DeepWaveRL achieves competitive performance compared to supervised and self-supervised baselines. These findings suggest that our framework offers a flexible and complementary learning paradigm for the FWI research community.

---


### 573. [A Human-Verified AI Workflow for Annotating Environmental Sound Data](https://arxiv.org/abs/2611.03271)

**<font color=#1a73e8>作者：</font>** Michael Barasa Murunga, Allan Vikiru  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale annotation of environmental sound recordings presents significant challenges under time and resource constraints, particularly when sound categories are imbalanced and only part of a dataset has been labeled. This paper describes the development and evaluation of a human-AI workflow used during annotation of the Kenya Forest Sounds Dataset (KFSD), using a project-stage working collection of 7,531 audio recordings across 21 categories. We investigated zero-shot classification, a feature-based ensemble, and a fine-tuned Audio Spectrogram Transformer (AST). The fine-tuned AST achieved 89.36% accuracy, 85.98% precision, 89.24% recall, and 87.58% F1 on held-out test data for binary classification of Person talking. Because this result remained below the predefined 95% threshold for autonomous annotation, model predictions were used as suggestions and subjected to human verification. Of the 5,026 initially unlabeled recordings, 2,337 were routed to a speech-verification queue and 2,689 remained for ordinary manual annotation. The verifier reviewed all 2,337 machine-labeled files and detected zero false positives, yielding 100% verification accuracy. The observed average verification time was approximately 4.2 seconds per file. At an average rate of 35 seconds per file for manual annotation, the hybrid workflow reduced work on the remaining queue from approximately 48.9 to 28.9 person-hours, saving about 20.0 hours (41%). The study documents the model-selection process, provenance-aware file organization, verification procedure, observed errors, practical limitations, and opportunities for extending AI assistance beyond one category.

---


### 574. [Strictly proper scoring rules for node selection tasks on graphs](https://arxiv.org/abs/2611.03274)

**<font color=#1a73e8>作者：</font>** Lorenz Hilfiker, Nathan Cincera Brack, Martin Sterchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In node selection tasks, the goal is to identify a single unknown target node in a graph. We consider probabilistic supervised node selection, where the estimator outputs a probability distribution over the nodes of the graph and the ground-truth node is available for evaluation. Classical evaluation metrics for such tasks are either statistically ill-conceived or blind to the graph structure. To fill this gap, we introduce two strictly proper scoring rules that are explicitly graph-aware: the Resistance score, which is parameter-free, and the Diffusion score, which operates at an adjustable coarse-graining resolution. We show that the Diffusion score interpolates between the multi-category Brier score and a cluster-level weighted Brier score. The Resistance score generalises two classical scoring rules: the multi-category Brier score and the Ranked probability score. Applied to rooted trees, it also serves as the strictly proper version of the improper Hierarchical error distance used in hierarchical classification. In the same setting, we furthermore establish strict propriety of the Hierarchical cross-entropy family, a recently introduced separate class of hierarchy-aware scoring rules. Experiments on epidemic source detection and on ImageNet classification confirm that the proposed scores detect meaningful differences in estimation quality that classical metrics miss.

---


### 575. [ReVA-HPE: Relative 6DoF Head Pose Estimation with Synthetic Pose Supervision and Personalized Virtual Anchors](https://arxiv.org/abs/2611.03283)

**<font color=#1a73e8>作者：</font>** Vasiliki Vasileiou, Panagiotis P. Filntisis, Petros Maragos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular head pose estimation is usually formulated as absolute regression from a single face crop, yet many applications observe the same person over time and can supply an explicit anchor image. Recently, relative head pose estimation was proposed, which casts the problem as estimation of the relative geometric change between an anchor and a query image. However, existing methods still require the anchor image pose to be known at inference, significantly limiting their practical use. We first extend relative head pose estimation to full 6DoF by additionally predicting a depth-normalized relative translation, which composes with the anchor to recover metric query pose in the camera frame. To eliminate the need for a ground-truth anchor pose, we reconstruct a personalized avatar from a single unlabeled enrollment image and render a bank of virtual anchors with known poses. The bank provides robust rotation hypotheses through multi-anchor consensus, while the real enrollment image serves as the real anchor in the translation branch via landmark PnP. We also introduce an efficient variant that amortizes the bank cost once at enrollment, after which each query requires a single real-to-real relative prediction, with limited accuracy sacrifice. The relative pose estimator is trained exclusively on synthetic face renderings, without real pose supervision, pseudo-labels, domain adaptation, or fine-tuning on the evaluation sets. On real 6DoF benchmarks, ReVA-HPE achieves state-of-the-art rotation accuracy on BIWI and, given a near-frontal enrollment image, on FaMoS, while remaining competitive in metric translation despite relying solely on synthetic pose supervision. Project page and code: this https URL

---


### 576. [Mesh-Agnostic Refinement Models for Latent Space Encoding of 3D Human Body Shapes](https://arxiv.org/abs/2611.03285)

**<font color=#1a73e8>作者：</font>** Chaima Zouaouid, Jonathan Cerqueirab, Sylvain Arguillere 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parametric human body models such as the Skinned Multi-Person Linear (SMPL) model provide compact representations of human shape and pose, but their reconstructions remain affected by both errors in estimated latent parameters and limitations in the decoder's expressive capacity. We propose a framework for refining these reconstructions by exploiting the geometric discrepancy between an initial decoded surface and a target mesh, without requiring vertex correspondences between them. The framework comprises three complementary approaches. Latent-VaRefine uses varifold-distance gradients to correct the estimated latent code while preserving the original parametric representation. Vertex-VaRefine processes multiscale varifold-gradient features with a DiffusionNet backbone to predict vertex displacements in a canonical pose, yielding an approximately pose-equivariant refinement pipeline. ElaOpt directly optimizes surface deformations under elastic regularization and normal-direction constraints.

---


### 577. [Top-$k$ Retrieval Leaves Memory Value Undetermined](https://arxiv.org/abs/2611.03289)

**<font color=#1a73e8>作者：</font>** Arman Behnam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A memory-augmented agent must decide which memories to keep, merge and retrieve, and its only evidence of their value is its retrieval log: the memories it retrieved in each episode and whether it succeeded. Existing methods assign every memory a value from this log, even when the log cannot separate one memory's contribution from another's. We treat the log as an experiment that nobody designed and ask which memory values it determines. Two counts answer this before any outcome is observed: how often each memory was retrieved, and how often each pair was retrieved together. From these counts, we prove that top-$k$ retrieval leaves every memory value undetermined, however many episodes are logged, and that a question with its own memories, asked once, determines at most one of their values. On fourteen standard memory benchmarks, no memory value is determined in any of 55 configurations. Both causes are choices about retrieval. We introduce LEDGER, which estimates each determined Shapley value in closed form with a confidence interval and reports every other value as undetermined. It merges memories with identical histories without losing a determined value, and it retrieves so that the next log determines more. On pooled HotpotQA, LEDGER raises the fraction of memories determined from 0.001 to 0.797, at a cost of 2.6 accuracy points on HotpotQA and with a gain of 2.7 on LoCoMo.

---


### 578. [Inferring Transferable Rewards via Active Inverse Reinforcement Learning](https://arxiv.org/abs/2611.03296)

**<font color=#1a73e8>作者：</font>** Victor Villin, Till Freihaut, Andreas Schlaginhaufen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse Reinforcement Learning (IRL) aims to recover expert rewards that transfer across environments with differing dynamics. Prior work has shown that such transfer is possible when gathering expert demonstrations across sufficiently different dynamics. In practice, however, expert demonstrations are costly, making it critical to select the right dynamics to reduce the quantity of expert data required for learning transferable rewards. We propose a two-phase approach: we first cycle through the available dynamics to obtain a reliable reward estimate, then actively select dynamics to reduce our uncertainty about the expert reward. Crucially, this yields novel sample complexity guarantees on transfer that hold for any dynamics, with a rate independent of the number of available dynamics. Empirically, our method significantly reduces the number of expert demonstrations needed to learn a transferable reward.

---


### 579. [An Axiomatic Framework for Reinforcement Learning in Open Multi-Agent Systems](https://arxiv.org/abs/2611.03301)

**<font color=#1a73e8>作者：</font>** Jianhong Wang, Yang Li, Samuel Kaski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open multi-agent systems, where only a subset of agents are controllable, are central to real-world domains such as smart grids, yet lack a principled foundation for reinforcement learning algorithm design. We study this setting through n-agent ad hoc teamwork (NAHT), a recent framework for learning in open multi-agent environments. We propose an axiomatic framework that derives value function learning from the Shapley axioms (Efficiency, Symmetry and Linearity), treating them as structural constraints rather than heuristic design choices. This formulation builds on a novel NAHT decomposition, which characterises the fundamental difference between open and fully controllable multi-agent systems, and establishes a cooperative game-theoretic foundation for learning. We further show that enforcing these axioms on learning individual value functions recovers the Shapley value for Dec-POMDPs, providing a principled bridge between reinforcement learning and classical cooperative game theory. Building on this framework, we introduce Shapley Machines and Banzhaf Machines, two generic algorithmic templates that can be instantiated with standard reinforcement learning methods. When applied to strong base algorithms such as IPPO and POAM, our methods consistently improve learning efficiency and generalisation to unseen agent types and conventions across NAHT benchmark tasks. The code of experiments is published on this https URL.

---


### 580. [Calibrated Multiaccuracy: Deterministic and Randomized Sample Complexity](https://arxiv.org/abs/2611.03305)

**<font color=#1a73e8>作者：</font>** Jiuyao Lu, Georgy Noarov, Aaron Roth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Calibrated multiaccuracy asks that a predictor be globally calibrated and multiaccurate with respect to a bounded test family $G$; that is, its residuals should be uncorrelated with every test $g(x)\in G$. This weakening of multicalibration suffices for many applications. Its sample complexity was not known to improve on that of full multicalibration, which is $\widetilde\Theta\left(\frac{\log|G|}{\varepsilon^2} + \frac{1}{\varepsilon^{3}}\right)$ when $|G|$ is at least a sufficiently large power of $\log(1/\varepsilon)$. We resolve the sample complexity of $\varepsilon$-calibrated multiaccuracy, showing that it scales as $$ \widetilde\Theta\left(\frac{\log|G|}{\varepsilon^2} + \frac{1}{\varepsilon^{5/2}}\right), $$ separating it from the complexity of multicalibration. The upper bound is obtained by an algorithm that outputs a randomized predictor.
For deterministic predictors, we establish the tight rate $$
\widetilde\Theta\left(
\frac{\log|G|}{\varepsilon^2}
+
\frac{(\log|G|)^{1/3}}{\varepsilon^{8/3}}
\right) $$ whenever $\log|G|=\Omega(\log(1/\varepsilon))$. When $\log|G|\le\varepsilon^{-1+\kappa}$ for any fixed $\kappa\in(0,1)$, this rate is polynomially larger than the rate for randomized predictors. Thus, unlike for multicalibration, calibrated multiaccuracy exhibits a genuine sample-complexity separation between deterministic and randomized predictors. The matching upper and lower bounds show that the unusual cube-root dependence on $\log|G|$ is intrinsic. At $\log|G|\asymp\varepsilon^{-1}$, the minimax rates for randomized and deterministic calibrated multiaccuracy both coincide with the minimax rate for multicalibration.

---


### 581. [Steering with Multilingual Lexicons for Sentiment Control in Low-Resource Languages](https://arxiv.org/abs/2611.03317)

**<font color=#1a73e8>作者：</font>** Lucinda Laurent, Muhammad Dehan Al Kautsar, Alfan Farizki Wicaksono 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering offers a lightweight mechanism for controlling model behavior, but existing methods depend on sentence-level contrastive data that is unavailable for most of the world's languages. We show that multilingual sentiment lexicons are a viable substitute across three model families: aggregated multilingual lexicons outperform English-derived steering vectors for mid- and low-resource languages, while monolingual lexicons remain stronger for languages a model has specialized in during pre-training. The steering efficacy is mechanistically dictated by both representational density and pre-training priors. Large-magnitude English vectors overwhelm the compact representations of low-resource languages, causing "linguistic collapse." This fragility is mitigated by the norm-dampening of multilingual aggregation. Architectural biases, including bilingual specialization penalty and latent numerical rigidity, also heavily constrain cross-lingual steering responsiveness. Ultimately, our work establishes lexicons as a practical steering signal and offers a comprehensive mechanistic account of cross-lingual steering dynamics.

---


### 582. [End-to-End NTT on FPGA for FHE Acceleration](https://arxiv.org/abs/2611.03325)

**<font color=#1a73e8>作者：</font>** Mohamed Allam, Thomas Spendlhofer, Hugo Sanz-González 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) enables privacy-preserving computation on encrypted data without decryption. Despite its strong security guarantees, FHE incurs substantial computational and memory overhead. In FHE-based deep learning inference, on average 63% of the CPU time is spent on the number theoretic transform (NTT) and its inverse (INTT), which reduce the complexity of polynomial multiplication from $O(N^2)$ to $O(N \log N)$. Prior FPGA works follow two approaches: accelerating entire FHE schemes, which yields significant speedups but ties them to specific parameters and algorithms, or accelerating only the NTT, which applies across schemes, algorithms, and libraries. Most FPGA NTT designs require interconnects that grow with parallelism and utilize significant resources, which complicates routing on multi-die FPGAs. Additionally, to the best of our knowledge, end-to-end NTT acceleration within an FHE context has so far been left unexplored. We design a fully unrolled, delay-commutator streaming NTT/INTT kernel, and floorplan it across the three dies of an AMD Alveo V80. At 400 MHz, the kernel transforms a polynomial of $2^{16}$ coefficients every 5.12 $\mu$s, the highest throughput among FPGA designs at this size. Offloaded end to end, it is up to 22x faster than the CPU per transform. We integrate the kernel into the Lattigo FHE library and evaluate it end to end. With 128-bit secure parameters, it accelerates core FHE operations, such as key switching and bootstrapping, by 1.8-2.2x, and neural network inference by 1.8-2.1x.

---


### 583. [From FAIR to AI-FAIR Metadata-First Infrastructure for AI-Enabled Science](https://arxiv.org/abs/2611.03327)

**<font color=#1a73e8>作者：</font>** Elizabeth G. Campolongo, Eric R. Sokol, Marty Downs 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) technologies and their capabilities have advanced rapidly over the past few years, leading to widespread interest and adoption in the biological and ecological sciences. However, the data infrastructure and computational resources that provide the foundation for AI workflows in ecology and biodiversity science remain fragmented. Moreover, the flow of value remains largely unidirectional: data move from collectors, through repositories and aggregators into models, and finally to research products or management actions. The derived value, such as corrected taxonomies, annotations, quality flags, and insights, rarely returns to source communities. We propose an extension of the original FAIR principles to address the needs of AI-ready infrastructure: the AI-FAIR metadata criteria, which place AI-enabled science in the context of a bidirectional Question-Data-Model triangle. This framework is designed to facilitate large-scale content-based analysis across diverse collections and ensure that the scientists generating the data benefit from the AI-enabled advances built on their data. Alongside these criteria, we introduce an agentic evaluation workflow that both rates existing datasets on the AI-FAIR and traditional FAIR criteria and provides actionable feedback where critical metadata is missing or incomplete. This modular dataset evaluation tool, paired with a domain-appropriate checklist, translates these principles into a reusable assessment of machine-learning readiness, AI-readiness for specified tasks, traceability, and ethical and CARE-aligned stewardship. Through this approach we aim to create a community-informed system to close the model data loop, so that AI also enriches data to further enable scientific discovery.

---


### 584. [Certifying Graph Neural Networks Against Label and Structure Poisoning](https://arxiv.org/abs/2611.03350)

**<font color=#1a73e8>作者：</font>** Lukas Gosch, Xichuan Chen, Yan Scholten 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust machine learning for graph-structured data has made significant progress against test-time attacks, yet certified robustness to poisoning - where adversaries manipulate the training data - remains largely underexplored. For image data, state-of-the-art poisoning certificates rely on partitioning-and-aggregation schemes. However, we show that these methods fail when applied in the graph domain due to the inherent label and structure sparsity found in common graph datasets, making effective graph-partitioning difficult. To address this challenge, we propose a novel semi-supervised learning framework called deep Self-Training Graph Partition Aggregation (ST-GPA), which enriches each graph partition with informative pseudo-labels and synthetic edges, enabling effective certification against node-label and graph-structure poisoning under sparse conditions. Our method is architecture-agnostic, scales to large numbers of partitions, and consistently and significantly improves robustness guarantees against both label and structure poisoning across multiple benchmarks, while maintaining strong clean accuracy. Overall, our results establish a promising direction for certifiably robust learning on graph-structured data against poisoning under sparse conditions.

---


### 585. [Multidimensional Suicide Risk Assessment with Machine Learning using Electronic Health Records](https://arxiv.org/abs/2611.03357)

**<font color=#1a73e8>作者：</font>** Nathan Scollar, Kemal Davaslioglu, Nathan Conger 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Suicide prevention remains a critical public health challenge, and electronic health records (EHRs) provide an opportunity to characterize suicide-related risk indicators using documented clinical, behavioral, medical, and social-contextual information. This paper presents a multidimensional machine learning framework to model and estimate suicide-related outcomes using MIMIC-IV EHR data. We construct clinically motivated diagnosis categories and define a composite outcome from documented codes corresponding to suicidal ideation, suicide attempt, prior suicidal behavior, and intentional self-harm. To address severe class imbalance and reduce age-related confounding, we apply age-matched resampling that retains all positive patients and samples comparison-cohort patients from the same age group. Logistic regression, random forest, and XGBoost classifiers are evaluated before and after resampling with isotonic calibration. The calibrated XGBoost model achieves the strongest matched-cohort performance, outperforming the other evaluated classifiers. SHAP-based interpretation shows that diagnostic burden, depression-related features, age, personality-disorder history, social determinants related to violence, and medical comorbidity contribute to elevated predicted probabilities. Our results demonstrate that combining broad EHR-derived features, age-matched cohort construction, calibration, and feature-level interpretation provides a practical framework for retrospective suicide-related risk modeling.

---


### 586. [Fuse To Align: Multimodal Representation Learning for Retrieval via Hypergraph Regularization](https://arxiv.org/abs/2611.03370)

**<font color=#1a73e8>作者：</font>** Anindya Nag, Ambuj Mehrish, Sebastiano Vascon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal retrieval must integrate complementary evidence from views that may be missing, noisy, or unequally informative. When a sample provides limited reliable evidence, learning from its views alone can hinder the acquisition of useful retrieval representations. Semantically related training samples may provide complementary observations, yet existing volume-based objectives jointly align modalities within each sample without explicitly enabling information exchange across samples. We therefore propose a training-time hypergraph fusion framework that connects observed modalities both within samples and across semantically related samples, allowing representation learning to draw on evidence beyond an individual sample while leaving the retrieval pipeline unchanged at inference. The framework includes HyVol as a special case and introduces two configurations: wHyVol learns view contribution weights and symmetric semantic affinities, whereas wRHG additionally models typed interactions and participant roles through relational propagation. Missing modalities are omitted rather than imputed, and the hypergraph is discarded after training, incurring no additional inference cost. Experiments on eleven zero-shot video-text and audio-text retrieval benchmarks demonstrate broad improvements with both GRAM and HyperGRAM. Across 17 video benchmark-modality settings evaluated in both retrieval directions, wRHG outperforms GRAM in all 34 comparisons and HyperGRAM in 33 of 34. Mean text-to-video R@1 increases from 63.4 to 68.2 with GRAM and from 64.8 to 68.4 with HyperGRAM, while the largest video-to-text gain reaches 13.3 percentage points on ActivityNet. Under missing-modality evaluation, both weighted configurations retain positive text-to-video gains over GRAM across seven benchmarks at every evaluated missingness rate, even when 90% of clips lack one modality.

---


### 587. [Mixed-Methods Exploration of Sociotechnical Factors to Improve Adoption of Crime-Reporting Apps in Urban Communities](https://arxiv.org/abs/2611.03376)

**<font color=#1a73e8>作者：</font>** Olalekan David-Banjo, Chinazunwa Uwaoma, Paul Witman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Crime-reporting mobile applications can enhance community safety and engagement in urban areas, yet their adoption remains low, partly because developers prioritize technological features over residents' social realities. This study used an exploratory sequential mixed-methods design to identify and validate the sociotechnical factors that drive adoption. Two focus groups and an analysis of 660 app reviews revealed that users' initial sense of usefulness fades, whereas sustained engagement depends on perceived value (PV), comprising six dimensions: safety, anonymity, recency, autonomy, camaraderie, and accessibility. A survey of 505 urban residents, analyzed with PLS-SEM, validated PV as a formative higher-order construct formed by four of these dimensions (safety, anonymity, autonomy, and camaraderie). PV was the strongest predictor of behavioral intention, ahead of effort expectancy, facilitating conditions, and performance expectancy, and behavioral intention strongly predicted actual use. The model explained 75% of the variance in behavioral intention and 51% in actual use. The findings offer design principles for community-centered crime-reporting technologies.

---


### 588. [RangeFinder: Predicting Ligand Property Ranges from Protein Pockets](https://arxiv.org/abs/2611.03379)

**<font color=#1a73e8>作者：</font>** Alan Nadelsticher Ruvalcaba, Chris Alvin, Supratik Mukhopadhyay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying ligands for a protein target requires searching a vast chemical space for a comparatively small set of compatible molecules. Existing machine learning approaches primarily address this problem by generating candidate ligands or scoring individual protein-ligand pairs, but provide limited information about the broader chemical space compatible with a binding pocket. We introduce RangeFinder, an SE(3)-equivariant transformer pocket-level model, trained and evaluated on BioLiP2 data, that predicts ranges over nine physicochemical ligand properties directly from pocket structure, chemistry, and evolutionary context. Using an intersection-over-union objective and evaluation metric (range-IoU), RangeFinder achieves a range-IoU of $0.464 \pm 0.002$, outperforming all deployable baselines while requiring only $12.2$ ms per pocket. We also quantify our method's ability to reduce the ligand search space while retaining compatible binders; in this regard, RangeFinder achieves a Reduction-Recall F-Score of $0.543 \pm 0.011$ --- once again outperforming all deployable baselines. Ablation experiments indicate that RangeFinder's performance depends more strongly on the density and quality of ligand supervision than on any individual input modality or specialized training strategy. Together, these results position RangeFinder as an inexpensive and effective molecular filtering prior, with demonstrated potential in narrowing the ligand search space of target pockets before docking, generation, or synthesis. The code for this project can be found at: this https URL.

---


### 589. [A Geometry-Informed Neural Operator surrogate of LISFLOOD-FP for rapid pluvial-fluvial flood forecasting: the case of Forlì, Italy](https://arxiv.org/abs/2611.03381)

**<font color=#1a73e8>作者：</font>** Samuele Maria Garofalo, Fabio Limardo, Simonetta Bodojra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physically based two-dimensional hydraulic models are too slow for real-time inundation forecasting and large ensembles. We present a time-dependent geometry-informed neural operator (GINO) surrogate of LISFLOOD-FP for the municipality of Forlì (Italy), severely affected by the May 2023 Emilia-Romagna floods. The surrogate is designed for an operational setting in which only river stage gauges and rain gauges are available. A reproducible pipeline turns public regional observations into a physically based training set: each river inflow is driven by the first stage gauge downstream of it through a calibrated water-surface boundary condition, and rain enters as SCS-CN effective rainfall. The surrogate is an autoregressive GINO trained on 216 simulations of 24 observed events with scaled forcing. It predicts volume-conserving polygon-mean depths on an exposure-based Voronoi mesh of 659 nodes, with a 20 min step over 72 h. The surrogate is tested on 38 independent observed events that it never saw during training. On these events it reaches a critical success index (CSI) of 0.934 at 0.05m and 0.844 at 0.3 m, a depth RMSE of 0.008m and an $R^2$ of 0.984 for maximum-depth maps. On one NVIDIA A10G GPU a 72-h forecast takes 1.7 s instead of 55 s with LISFLOOD-FP, and a 50-member ensemble, computed in a single batched rollout, takes 6.2 s instead of about 46 min, which makes probabilistic flood forecasting practical. These results show that neural-operator surrogates can deliver accurate pluvial-fluvial flood forecasts driven by river stage for operational early warning.

---


### 590. [ASCoR: Asymmetric Semantic-Spatial Learning for Remote Sensing Domain Generalization](https://arxiv.org/abs/2611.03382)

**<font color=#1a73e8>作者：</font>** Zitong Wang, Shuchang Lyu, Meng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Source-only domain generalization (DG) for remote sensing semantic segmentation seeks reliable predictions in unseen domains without target-domain data during training. Although vision foundation models offer transferable knowledge, category recognition remains sensitive to source-specific visual cues, while task-specific adaptation may weaken pretrained transferability. We propose ASCoR, an asymmetric semantic-spatial framework built on SAM3. Its text-conditioned semantic branch uses class-name prompts to provide explicit category guidance. Probe-Once Dynamic Adaptive LoRA distributes a fixed adaptation budget across encoder blocks to limit source-specific specialization. A complementary task-specific dense branch learns multi-scale spatial representations using a separate frozen SAM3 image encoder. A lightweight reliability router integrates the two branches through bounded spatial correction based on local prediction reliability. All components are trained using source-domain supervision only. Experiments on the ISPRS, LoveDA, and OpenEarthMap benchmarks cover nine cross-domain transfers. ASCoR achieves a state-of-the-art mean IoU of 68.61% across six ISPRS transfers, outperforming the previous best method by 2.69 percentage points. It also achieves the best results on all three LoveDA/OpenEarthMap transfers, with 59.07%, 47.95%, and 49.38% mIoU on Rural-to-Urban, Urban-to-Rural, and Urban-to-OpenEarthMap, respectively. Ablation studies, feature visualizations, and spatial reliability analyses support the effectiveness and complementarity of the proposed components. Code: this https URL.

---


### 591. [LAND: Learning an Adaptive Number of Draws for Bayesian Best-of-N Selection](https://arxiv.org/abs/2611.03388)

**<font color=#1a73e8>作者：</font>** Koen Oostermeijer, Teryn Jones  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Best-of-N decoding improves generation quality by sampling multiple candidates and selecting the best, but it allocates equal compute to sources regardless of how much they benefit from additional sampling: the expected benefit is small for sources with low-variance score distributions and potentially much larger for those with high-variance distributions. To address this shortcoming, we propose LAND (Learning an Adaptive Number of Draws), which dynamically allocates samples according to their posterior-predictive marginal value. LAND learns a discrete empirical mixture of source-conditioned score distributions from calibration data, updates its belief about a source as completion scores are observed, and stops sampling when the expected improvement of another draw falls below a shared compute price. Across machine-translation experiments with multiple models and language pairs, LAND achieves better MetricX scores than fixed best-of-N at matched average compute. Conversely, at matched translation quality, LAND requires approximately 20-40% fewer candidate generations. Adaptive allocation therefore provides a simple way to retain the benefits of best-of-N while substantially improving its compute efficiency.

---


### 592. [CrowdForge: Effects of Audio and Visual Audience Participation Modalities on Agency, Collaboration, and Engagement in AI-Mediated MR Performances](https://arxiv.org/abs/2611.03389)

**<font color=#1a73e8>作者：</font>** Torin Hopkins, Shih-Yu Ma, Zander Trafton-Hancock 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Technology-mediated audience participation (TMAP) enables audiences to influence live performances, yet balancing interaction with meaningful agency remains challenging. While AI-generated music and MR enable new forms of audio and visual audience participation, little is known about how these participation modalities influence audience experiences during live musical performance. In particular, it remains unclear how they shape perceived agency, collaboration, and engagement, and how they complement one another within TMAP systems. We present CrowdForge, an AI- and MR-mediated paradigm where audiences collectively control generative music and virtual environments during a live performance featuring a guitarist and DJ. Through a mixedmethods concert study evaluating three interaction conditions (audio, visual, and combined audio-visual), we demonstrate that observability is the primary driver of audience agency. While visual interaction provided easily observable feedback, audio parameters offered macro-structural control over the music. Audiences tended to use the control enabled by AI audio generation to test musical boundaries, introducing a productive adversarial tension between the crowd and the musicians. This dynamic pushed creative limits, deepened engagement, and generated moments of musical coherence when performers successfully resolved audience-induced challenges. We argue future TMAP systems should prioritize human-centered, highly observable interactions to build agency, while combining the expressiveness of music with the clarity of visual feedback.

---


### 593. [Progressive Multi-Scale Super-Resolution via Cascaded Bicubic Anchors and Inter-Scale Mutual Refinement](https://arxiv.org/abs/2611.03390)

**<font color=#1a73e8>作者：</font>** Chun-An Lin, Yu-Chia Chang, Chi-Mao Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Super-resolution networks are trained for one magnification factor, so several output resolutions require several models. We propose PMS-SR, a progressive single-input multiple-output network that produces x2, x4, and x8 results in one forward pass, with a Transformer backbone on the low-resolution grid. In Stage 1, each scale is predicted as a residual over the detached bicubic upsampling of the previous scale's prediction. With Dirac and zero initialization, training starts exactly from the bicubic cascade, and each head adds only the band the previous scale lacks. In Stage 2, inter-scale mutual refinement couples the scales in both directions through space-to-depth feedback, deformable alignment, and per-pixel fusion, so x8 features refine the x2 output. Trained on DF2K, the 7.95M-parameter model achieves a higher PSNR than every compared multi-scale method at x4 and x8 on all five standard benchmarks. At x8, it outperforms the x8-specific DRN-L on all of them, leads all compared methods on Urban100, and is within 0.13 dB of the best result elsewhere. Against three single-scale SwinIR-M models, PMS-SR uses 22% of the parameters, runs 2.9x faster on BSD100 inputs, and its outputs agree 6.7-12.4 dB more closely. Code and pretrained models will be released at this https URL upon acceptance.

---


### 594. [TaoMate-FVSR:Audio-Guided Facial Video Restoration](https://arxiv.org/abs/2611.03393)

**<font color=#1a73e8>作者：</font>** Xinyang Li, Zeran Xu, Qijun Gan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated videos often depict people within detailed scenes while leaving their small facial regions poorly resolved. Visual super-resolution can sharpen these regions without resolving whether the recovered lips and teeth agree with the spoken audio. We present an audio-guided facial video restoration framework that addresses this ambiguity within a reference-guided video flow model. Source--noise mixing initializes reconstruction from a partially preserved observation, and structured reference injection separates appearance anchors from continuous motion context. Training combines restoration of degraded images and videos with correction of degraded dubbed sources under target audio. Appearance and synchronization supervision allow the model to recover facial detail and support visual dubbing when the audio is replaced. On talking-head restoration benchmarks, our method achieves the best paired perceptual similarity and synchronization scores among the compared restoration methods. Component comparisons examine audio conditioning, the reconstruction formulation, and reference injection. Native AIGC examples further illustrate the recovery of lip contours, dental structure, and surrounding facial texture in scene-level footage. injection. Native AIGC examples further illustrate the recovery of lip contours, dental structure, and surrounding facial texture in scene-level footage.

---


### 595. [TaoMate-HD: Progressive-Resolution Autoregressive Audio-Video Generation](https://arxiv.org/abs/2611.03394)

**<font color=#1a73e8>作者：</font>** Qijun Gan, Chenwei Zhang, Xinyang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming digital humans produce detailed video while continuing speech as new text arrives. High-resolution denoising is costly, and text updates can cause repeated or interrupted speech. We present TaoMate-HD, an autoregressive model for high-resolution audio-video streaming. For each short segment, or chunk, two denoising steps establish coarse video structure at low resolution. A final step refines the video to high resolution, with audio generated throughout the same trajectory. Each stage passes its audiovisual predictions to the same stage of the next chunk as history. Across text updates, the model retains this history to infer what has already been spoken. Continuation training utilizes asymmetric text conditioning, with separate text windows for generation and distillation. Experiments show a 1.6x speedup over direct high-resolution generation with the same model and hardware. Optimized stage-parallel deployment provides a further 1.9x overall speedup over serial progressive generation. Our continuation training reduces character error rate by 11.18 percentage points relative to the baseline. The model also supports hour-long audiovisual generation. Our project page is this https URL.

---


### 596. [Image Guided Depth Upsampling using Anisotropic Total Generalized Variation](https://arxiv.org/abs/2611.03399)

**<font color=#1a73e8>作者：</font>** David Ferstl, Christian Reinbacher, Rene Ranftl 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work we present a novel method for the challenging problem of depth image upsampling. Modern depth cameras such as Kinect or Time of Flight cameras deliver dense, high quality depth measurements but are limited in their lateral resolution. To overcome this limitation we formulate a convex optimization problem using higher order regularization for depth image upsampling. In this optimization an anisotropic diffusion tensor, calculated from a high resolution intensity image, is used to guide the upsampling. We derive a numerical algorithm based on a primaldual formulation that is efficiently parallelized and runs at multiple frames per second. We show that this novel upsampling clearly outperforms state of the art approaches in terms of speed and accuracy on the widely used Middlebury 2007 datasets. Furthermore, we introduce novel datasets with highly accurate groundtruth, which, for the first time, enable to benchmark depth upsampling methods using real sensor data.

---


### 597. [VidDub: Replacement-Aware Distillation for Two-Step Video Dubbing](https://arxiv.org/abs/2611.03404)

**<font color=#1a73e8>作者：</font>** Yexin Liu, Yunlong Lin, Zehan Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video dubbing aims to synthesize lip movements that match target speech while preserving the speaker identity, head pose, and background of a source video. Existing editors are predominantly trained via self-reconstruction under original paired audio, even though the source mouth becomes a conflicting target when driving speech is replaced. We introduce replacement-aware cross-audio supervision: paired-audio samples use full-frame reconstruction, whereas unpaired replacement-audio samples mask out source-mouth reconstruction losses and supervise the mouth solely through audio-visual synchronization while preserving unmasked facial regions and background. Because offline dubbing provides the complete source video and target speech beforehand, we present VidDub, a full-context diffusion editor distilled into two denoising steps (2 NFE). Our replacement-aware teacher first learns accurate lip synchronization without regressing toward conflicting source mouth movements. Matched trajectory regression then transfers the teacher's CFG-guided trajectories to a two-step student, and distribution matching distillation recovers visual quality after step compression. We will release the curated training dataset, VidDub-Bench, fixed paired- and cross-audio evaluation manifests, preprocessing outputs, and unified evaluation code. Across three training seeds, masking out conflicting source-mouth reconstruction improves cross-audio Sync-C by 0.833; the final two-step model combines strong lip synchronization with superior visual quality, identity preservation, and visual speech recognition across four benchmarks.

---


### 598. [Low-Rank Clebsch--Gordan Coupling for Equivariant Spherical Forecasting](https://arxiv.org/abs/2611.03411)

**<font color=#1a73e8>作者：</font>** Yaojun Li, Zhixuan Zhao, Dongzhe Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spherical-harmonic neural operators provide an efficient representation for global forecasting, but their discretized pointwise nonlinearities can break rotational equivariance through aliasing. Clebsch-Gordan (CG) tensor products provide exactly equivariant interactions between spherical-harmonic representations, but their computational cost grows rapidly with spectral bandwidth and has limited their use at forecasting scale. We introduce LCG-SFNO, which combines low-rank CG interactions within a controlled low-degree band with coefficient-space residual propagation and an exactly projected quadratic nonlinearity, preserving SO(3) equivariance throughout the learned operator. To make the CG interaction practical, we further develop SSHCG, a sparse GPU implementation with a factorized alternative for wider coupled bands. On spherical shallow-water dynamics and the ERA5-based WeatherBench benchmark, LCG-SFNO reduces rotational error to numerical precision (more than three orders of magnitude below SFNO on shallow water and five orders of magnitude below it on WeatherBench), while matching SFNO on shallow-water forecasting and substantially improving forecast skill relative to SFNO on WeatherBench. Matched ablations show that CG coupling accelerates convergence, while SSHCG keeps the coupling to about 10 percent of a training step at the operating bandwidth, making exact equivariant coupling practical at forecasting scale.

---


### 599. [Finite-Memory Control of POMDPs: Fundamental Limits and Efficient Design](https://arxiv.org/abs/2611.03414)

**<font color=#1a73e8>作者：</font>** Emrecan Kutay, Atilla Eryilmaz, Ness Shroff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimal control of partially observable Markov decision processes (POMDPs), in general, requires a complete history. The belief state, a distribution over hidden states, summarizes this history and provides the classical sufficient statistic to control POMDPs. However, the continuous nature of the belief space generally prevents a finite-memory controller from maintaining it exactly. This raises the question we address in this work: what must the available finite memory preserve to achieve near-optimal control performance? We study this question through an information-theoretic converse that gives a fundamental lower bound on the loss of any finite-memory controller. The analysis introduces the concept of a decision witness that characterizes belief states whose confusion would lead to unavoidable loss. Motivated by this bound, we propose RECAP, a constructive quantization method for designing representative memory states. We prove an upper bound on the optimality gap of any RECAP codebook and use the components of this bound together with the converse analysis to define the codebook objective. Experiments on 11 POMDP benchmarks demonstrate that RECAP improves over finite-memory representation baselines under the same memory budget.

---


### 600. [O2N2: Efficient Doubly Oblivious Approximate Nearest Neighbor Search](https://arxiv.org/abs/2611.03415)

**<font color=#1a73e8>作者：</font>** Zhechen Li, Zimai Guo, Mingxun Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving approximate nearest neighbor (ANN) search allows clients to search from an untrusted server without revealing sensitive queries, and is useful in scenarios like medical diagnostics and credit scoring. Among the various privacy-preserving primitives, trusted execution environments (TEEs) have much lower overhead than heavy cryptographic ones, yet they leak memory access patterns, enabling adversaries to infer query contents.
Oblivious RAM (ORAM) can be used to hide those access patterns at $\mathrm{O}(\log N)$ asymptotic cost, but existing high-performance ANN search algorithms (e.g., IVF or HNSW) exhibit complex, data-dependent access patterns that are unfriendly for ORAM. Furthermore, standard ORAM constructions typically assume there exists a small amount of trusted storage, which weakens the security guarantees and is not always feasible. Solutions that eliminate such trusted storage (known as {\em double obliviousness}) typically degrade performance further to $\mathrm{O}(\log^2 N)$.
We introduce O2N2, a doubly oblivious ANN framework built around single-path search in randomly rotated $k$-d tree forests. A pointer-based Circuit ORAM stores the search structure, with separate storage for compact internal nodes and vector-bearing leaves. Each visited leaf is processed by an oblivious selection network, and fixed-schedule duplicate removal and selection combine the local results into the final top-$k$.
We evaluate O2N2 on real-world datasets and further test its scalability on 100 million vectors. For 10-NN and 100-NN search at the specified high-recall targets, it achieves a $9.8$--$125.9\times$ speedup over the fastest doubly oblivious baselines.

---


> [!TIP]
> 当前位于：**551-600**（第 12/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
