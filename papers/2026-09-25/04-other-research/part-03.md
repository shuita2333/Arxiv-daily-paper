# 📦 其他研究 | 2026年09月25日

> 本类共 **240** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-240](./part-05.md)

---

### 101. [Issuer-Sovereign Agentic Payments](https://arxiv.org/abs/2609.27452)

**<font color=#1a73e8>作者：</font>** Dishant Sharma, Rajneesh Kaushal, Ashu Kanaujia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are beginning to make real payments. Current approaches let an agent pay by relying on a credential provider that, in the approaches deployed today, typically sits outside the cardholder's bank. The spending rules are then enforced by the card network or that provider, and not by the bank itself. This leaves the issuing bank, which carries the financial risk, with little direct control at the moment a payment happens. This paper describes Issuer-Sovereign Agentic Payments, a method that keeps that control with the issuer. The cardholder approves a spending rule once, and the bank's own authentication component records it. Later, when the agent pays a specific merchant, the bank checks the merchant against the approved rule and generates the card authentication value only if the merchant is allowed. The payment then travels the normal card rails and is validated by the issuer, with no extra dependency introduced at execution.

---


### 102. [Hybrid Gaussians for Robust Open-Vocabulary 3D Segmentation with Multi-View Object Association and Boundary Refinement](https://arxiv.org/abs/2609.27462)

**<font color=#1a73e8>作者：</font>** Xueqi Qiu, Yueming Sun, Tianyu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D segmentation localizes objects from free-form text queries, but remains challenging in real image sequences: incomplete or noisy 2D supervision destabilizes multi-view identity assignment, while full-scene semantic learning weakens object-level discriminability. We introduce Hybrid Gaussians, a unified 3D representation jointly modeling object association and language-aligned semantics. Its Multi-View Object Association mechanism combines Observation Fusion and Semantic Contrastive Learning to improve identity consistency and semantic discrimination. Boundary Reconstruction Optimization further refines local boundary structure to improve contour quality. Experiments on LERF and 3D-OVS demonstrate strong quantitative and qualitative performance. Our method achieves 59.1\% mIoU on LERF, yielding a 13.4\% relative gain over the baseline. Project page: this https URL.

---


### 103. [Learning Where to Look: A Shared Relative-Alignment Module for Time-Series Forecasting and PPG-to-Vital-Sign Reconstruction](https://arxiv.org/abs/2609.27473)

**<font color=#1a73e8>作者：</font>** Ragamayi Puli, Shunya Nagashima  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> PPG-to-vital-sign reconstruction turns a wrist-worn photoplethysmogram into clinical waveforms such as the ECG. Long-horizon multivariate time-series forecasting underpins planning in energy, weather, and traffic. Both generate a target sequence from a condition sequence, and current models hard-code where each target position reads it, as a same-position copy or seasonal recurrence, so neither transfers between tasks. We propose ROOSTER, one conditioning module that handles vital-sign reconstruction and time-series forecasting alike by learning this correspondence. Its core is a periodic-comb bias over the target-condition offset whose center, period, and sharpness are learned per head, so one module settles on the identity alignment or a seasonal lag and reports which it found. On vital-sign reconstruction from PPG, ROOSTER outperformed the published baselines on four heart-rate and respiratory-rate benchmarks. On multivariate time-series forecasting, it achieved the best horizon-averaged MSE on four benchmarks and outperformed the forecasting model it extends on 20 of 24 dataset-horizon settings under matched three-seed training. An ablation study indicated that the relative bias, not content matching, carried the alignment.

---


### 104. [WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents](https://arxiv.org/abs/2609.27490)

**<font color=#1a73e8>作者：</font>** Jingjie Ning, Xueqi Li, Yibo Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI research agents need reliable knowledge of how their experiments change outcomes. We introduce WhatWorkedBench to measure experimental understanding, the accuracy of predictions about component changes after budgeted experimentation. Agents inspect code, select measurements, and submit a response surface, a table predicting scores for every configuration of component settings. Exhaustive CPU execution supplies reference effects for changing each component while holding the others fixed. These effects capture combinations of changes across 36 tasks from 30 data sources and 8 workflow types, with 1248 configuration records. Core evaluation combines 4,206 numerical-control records across all eight families and 108 agent episodes across the original six. At eight new measurements, pair-effect ridge selects an optimum on 15 of 22 sources and limits every effect error to 10% of score range on three. Fitting a Gaussian process (GP) to the same agent observations raises effect recovery, accuracy relative to true effect magnitude, from 0.632 to 0.698 in the original Flash cohort and from 0.621 to 0.720 in an additional cohort. On six completed beat-detection and graph submissions, the same-observation GP raises family-macro recovery from 0.303 to 0.455. On six workflows with six binary options at 20 new measurements, encoding code equivalences, configurations with identical behavior, raises GP recovery from 0.248 to 0.462. WhatWorkedBench supports research on experimental agents, adaptive experimental design, numerical inference, and use of program structure.

---


### 105. [Information Capacity of Generative Video Compression: Quantifying the Rate-Compute Exchange at Identical Quality](https://arxiv.org/abs/2609.27493)

**<font color=#1a73e8>作者：</font>** Cheng Yuan, Jiawei Shao, Xuelong Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Under the AI Flow framework, communication networks distribute intelligence across devices, edge servers, and clouds, and computation at the receiver becomes a resource that can substitute for transmitted bits. Generative video compression (GVC) embodies this exchange by sending compact tokens with ultra-low bitrate and letting a generative decoder synthesize the video, yet how much bandwidth savings a unit of decoder compute actually achieves has never been quantified. To fill this vacancy, we model reconstruction quality as a two-factor power law in data rate and decoder compute, which fits measured DISTS of two GVC decoders with a mean error below 3%, and define the information capacity (IC) as the negative logarithmic slope along an iso-quality contour, namely the fraction of rate saved per fractional increase in compute at identical quality. IC is dimensionless and unit-invariant, thus enabling an architecture-agnostic comparison. It forms a field over the operating plane, locating where additional denoising steps are worth their cost. Across five datasets, the 14B decoder trades more compute for fewer rate about ten times more efficiently than the 1.3B decoder. IC also varies significantly across datasets, indicating imbalanced performance on the rate-compute trade-off in GVC methods.

---


### 106. [Know-Your-Scene (KYS)-SLAM: Hierarchical Semantic-Motion Priors for Feature Matching in Stereo Visual SLAM](https://arxiv.org/abs/2609.27509)

**<font color=#1a73e8>作者：</font>** Preeti Chatterjee, Jin Lu, Jin Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereo visual SLAM systems built on local descriptors suffer from semantic ambiguity, instance-level confusion, and independently moving objects, each corrupting data association and accumulating as trajectory drift. Prevailing semantic and dynamic SLAM methods address this through binary feature rejection, sacrificing correspondence density for outlier suppression. We contend that contextual implausibility is better expressed as a graded quantity than an exclusion criterion. We present Know-Your-Scene (KYS)-SLAM, a modular extension of ORB-SLAM3 that supplants feature rejection with continuous correspondence modulation. The contribution is the reframing of contextual evidence as correspondence cost, applied within feature matching and leaving the geometric backend unmodified. Each keypoint is augmented with semantic, panoptic, and motion priors fused through a hierarchical compatibility formulation, in which semantic class and instance identity enforce structural plausibility while a zero-shot motion score down-weights features on independently moving objects. That score comes from a training-free module fitting a depth-aware ego-motion model to background optical flow and classifying panoptic segments via self-calibrating, coverage-aware thresholds, so only segments with sufficient motion evidence are penalized and static structure is left unpenalized. Penalizing correspondences rather than discarding them preserves the geometric support bundle adjustment depends on. Under one fixed configuration, no coefficient retuned per sequence or dataset, KYS-SLAM reduces per-sequence ATE RMSE by 17.4% on outdoor KITTI and 27.7% on indoor EuRoC across 21 stereo sequences with no regressions, and by 6.6% on dynamic subsets of KITTI Tracking and 17.8%, up to 31.2%, on Virtual KITTI 2 -- cross-domain transfer across outdoor driving, indoor flight, and synthetic imagery under one set of constants.

---


### 107. [M3D-Net: Hierarchical Coordination of Spatial Context, Feature Reuse, and Differential Attention for Mammography Classification](https://arxiv.org/abs/2609.27523)

**<font color=#1a73e8>作者：</font>** Zheng Yu, Xinhang Li, Jiabao Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast image classification requires local detail and global tissue context, yet these cues can weaken as representations deepen. We present M3D-Net, a mammography encoder that hierarchically coordinates multi-scale coordinate attention, bounded dynamic feature reuse, and differential attention through resolution-aware operator placement. Within-stage retrieval preserves access to earlier features, coordinate-aware aggregation integrates local and global context, and differential attention operates at coarse resolutions. We evaluate image-only classification on AISSLab mammography and an adapted image--clinical model on BrEaST ultrasound. Against EdgeNeXt, RepViT, and TransXNet, the proposed implementations achieve the highest recorded validation accuracy and late-training accuracy, with the lowest endpoint cross-entropy loss. Validation accuracies reach 97.78\% and 80.39\%, respectively. These results support further evaluation of hierarchical coordination across breast imaging settings; repeated-seed, component-controlled, and independent evaluations remain necessary.

---


### 108. [MDRC: A Deployable State-Recovery Defense for Traffic Signal Control under Sensor Corruption](https://arxiv.org/abs/2609.27528)

**<font color=#1a73e8>作者：</font>** Mingyuan Li, Chunyu Liu, Xiao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traffic Signal Control (TSC) is a safety-critical cyber-physical system that relies on real-time sensing. Corrupted observations caused by adversarial perturbations or sensor failures can propagate from the sensing layer into the controller and degrade traffic efficiency. Existing robust Reinforcement Learning (RL)-based TSC methods often suffer from limited cross-city generalization, high inference latency, and weak recovery under partial observability.
We present MDRC (Meta-Diffusion-based framework for Resilient traffic signal Control against adversarial attacks and sensor failures), a post-detection state-recovery defense inserted between sensing and control. MDRC reconstructs trustworthy traffic states before they are consumed by the controller. It combines Denoising Diffusion Implicit Models (DDIM) for efficient state recovery with Reptile meta-learning for a transferable initialization across cities. We provide an optimization-based view of the DDIM recovery dynamics and establish a recovery-error bound that separates score approximation, numerical discretization, and initialization mismatch.
Across seven real-world-derived CityFlow benchmarks, MDRC reduces Average Travel Time by 6.77% under stochastic and policy-aware attacks and by 12.75% under structured sensor loss, while improving state-recovery fidelity. We further evaluate 3,600 seconds of real roadside measurements with 50% of detector channels disabled and integrate MDRC into a hardware-in-the-loop traffic-signal stack. Over a 9.16-hour run with 32,389 sensing/control cycles, the system achieves 99.79% decision availability, produces no out-of-plan recommendations, and requires approximately 38 ms of component-wise processing per one-second control interval.

---


### 109. [ICM: Intra-class Mixing for Domain Adaptation in Adverse Weather](https://arxiv.org/abs/2609.27533)

**<font color=#1a73e8>作者：</font>** Boying Li, Chang Liu, Britta Ayano Wilde 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised domain adaptation (UDA) for semantic segmentation remains challenging under adverse weather conditions because severe appearance changes enlarge the domain gap and degrade the reliability of pseudo labels in the target domain. To address this problem, we propose an Intra-Class Mixing Consistency (ICM) framework that enforces prediction consistency between an intra-class mixed image and its original counterpart. Unlike previous mixing-based consistency methods that combine regions across different images or domains and may introduce unrealistic semantic inconsistencies, ICM performs mixing within the same image and semantic class, preserving realistic semantic layout for consistency regularization. With ICM, we establish a new state-of-the-art performance for clear-to-adverse-weather unsupervised domain adaptation (UDA) in semantic segmentation. On the Cityscapes $\rightarrow$ ACDC benchmark, our method achieves 75.7\% mIoU, outperforming the previous state of the art by +1.9 pp, demonstrating its effectiveness in mitigating class confusion under challenging environmental conditions. The code is provided in the supplementary material.

---


### 110. [KITE: Scaling Jev Population Experiments with Sparse Flagship Calibration](https://arxiv.org/abs/2609.27535)

**<font color=#1a73e8>作者：</font>** Hengyu Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> KITE queries a typed behavioral kernel once per unique state, then executes populations of any size from the table with event-keyed randomness and common random numbers. An expensive flagship model is reserved for sparse paired anchors that estimate intervention effects. Measured human-model discrepancy is propagated as shared error into every conclusion. Population-experiment cost thus scales with unique states and anchors, while uncertainty is governed by evidence about people rather than Monte Carlo noise. On Epstein experiments with 9,070 participants, anchors covering 1.7% of states reduced effect error by 41% (absolute MAE reduction 0.0125). On 37 held-out SocSci210 experiments, 0.5-1.5% anchor coverage raised captured decision gain from 0.27 to 0.39. The kernel passed content-fidelity criteria in all 15 new countries of a 16-country study. Shared discrepancy yielded retrospective coverage of 93% and 96% at nominal 80% and 90%, versus 29% and 36% from human sampling uncertainty alone. A million agents executed 20 tabulated steps in 0.9 seconds on a laptop. This architecture offers a route to screening candidate interventions before human trials, multi-country content audits, and uncertainty-aware policy comparison at the cost of a few thousand kernel calls with sparse flagship anchors. Property-specific evidence records connect each use to its validation scope, correction provenance, and uncertainty, making these applications auditable.

---


### 111. [EBRL: Asynchronous Embodied RL by Multi-Grained Resource Management](https://arxiv.org/abs/2609.27547)

**<font color=#1a73e8>作者：</font>** Liang Mi, Weijun Wang, Bowen Gao 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Embodied reinforcement learning (RL) improves model capabilities with a pipeline of environment simulation, action generation, and model updates. These stages show heterogeneous CPU and GPU demands, making efficient resource utilization difficult. Recent systems overlap rollout (simulation and generation) with training for efficiency, but exclusive GPU allocation and synchronized barrier in rollout still leave substantial hardware resource waste. In this paper, we present EBRL, an asynchronous embodied RL training system with two core techniques. The asynchronous pipelined scheduler overlaps rollout and training, pipelines simulation and generation across environment groups, and carries out each environment independently, eliminating synchronization stalls. The fine-grained resource manager pools CPU cores and GPU streaming multiprocessors, and uses stage profiles and runtime feedback to adjust resource quotas and batch sizes to meet the shifting demands among stages. We implement EBRL on RLinf and evaluate it with four embodied policies and four simulation benchmarks across heterogeneous GPU testbeds. Experiments show that EBRL achieves 1.30-3.47 times the end-to-end rollout throughput and 2.5 times of training convergency compared to the SOTA embodied RL systems.

---


### 112. [PhyMo: A Physical-Field Modality for Multimodal AI4Physics](https://arxiv.org/abs/2609.27554)

**<font color=#1a73e8>作者：</font>** Henan Sun, Haitao Hu, Jin Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal learning is emerging as a powerful paradigm for AI for Physics (AI4Physics), where predicting physical systems requires the joint interpretation of heterogeneous observations, measurements, and domain knowledge. However, existing approaches typically represent physical quantities and governing equations as generic numerical or textual tokens, overlooking the physical constraints that determine their spatiotemporal interactions. To address this limitation, we introduce the \textbf{physical-field modality} and propose \textbf{PhyMo}, a physics-grounded multimodal framework that organizes heterogeneous measurements through PDE-associated operators. PhyMo follows a three-stage learning procedure: the physical-field encoder is first pretrained through field reconstruction under PDE residual supervision, its representations are subsequently aligned with visual embeddings in a shared latent space, and the fused multimodal representations are finally processed by corresponding downstream prediction heads. Experiments on five datasets spanning diverse physical environments show that PhyMo achieves state-of-the-art performance, compared to the strongest baseline on each dataset, demonstrating the superiority of PhyMo on multimodal representation learning in AI4Physics.

---


### 113. [ThaiTrees: Thai Syntactic Dependency Trees Across Domains](https://arxiv.org/abs/2609.27558)

**<font color=#1a73e8>作者：</font>** Attapol T. Rutherford, Papatchol Thientong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Studying syntactic patterns in naturally occurring language requires a large parsed corpus, but manual annotation is costly and difficult to scale. Thai has a manually annotated dependency treebank for training and evaluating parsers, but lacks a large automatically parsed corpus for quantitative syntactic research. We present ThaiTrees, a 342M-token corpus drawn from news, Wikipedia, spoken transcripts, and social media. We develop a reproducible pipeline for cleaning, processing, and parsing Thai text under the Universal Dependencies framework. The resulting corpus makes grammatical relations searchable and supports the study of syntactic distributions. We release a frequency lexicon and CoNLL-U parses in machine-readable formats suitable for both AI-assisted and conventional programmatic analysis.

---


### 114. [TNLearn: An Open Source Python Package for Task-based Neurons](https://arxiv.org/abs/2609.27564)

**<font color=#1a73e8>作者：</font>** Meng Wang, Tieyun Li, Juntong Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The brain does not rely on a single type of neuron to perform all kinds of tasks; instead, it designs different neurons for different tasks. The concept of task-based neurons represents a paradigm shift compared to task-based architectures. It argues that solving a specific problem requires customized neurons, as task-based neurons capture useful prior knowledge from task-related data. To facilitate the use of task-based neurons in scientific research and industrial applications, we introduce TNLearn, an open-source Python package that provides automated construction of task-based neurons and networks, enabling smooth training of task-based networks. Comprehensive documentation, including technical exposition, API reference, and representative examples, is available online. TNLearn is open-sourced at this https URL and has become a PyTorch ecosystem project.

---


### 115. [Agent-Based Modeling of Systems of Systems](https://arxiv.org/abs/2609.27573)

**<font color=#1a73e8>作者：</font>** Jean-Baptiste Soyez, Gildas Morvan, Rochdi Merzouki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper deals with the generic modeling of systems of systems (SoSs) using agent-based modeling. SoSs are large-scale systems, including numerous-possibly heterogeneous-interacting component systems evolving in a dynamic environment. The aim of this paper is to provide generic formalism allowing to represent and control the whole complexity of a SoS using agent-based simulations. In particular, organizational aspects of SoSs are managed with the Agent-Group-Role model. Functional aspects, guiding SoSs to accomplish their global goals, are handled via a functional specification. Multilevel aspects are modeled with the Influence Reaction Model for Multilevel Simulation (IRM4MLS) agent-based meta-model. Models generated using this formalism encompass static and dynamic aspects of SoSs. They consider reorganization of SoSs caused by changes of goals or subsystem capacity. All these elements are illustrated in this paper using a SoS case study of Intelligent Autonomous Vehicles initiated by the Intelligent Transportation for Dynamic Environment (InTraDE) European project to automate the port container logistic.

---


### 116. [VCMM: Variance-Calibrated Momentum for Multimodal Learning](https://arxiv.org/abs/2609.27577)

**<font color=#1a73e8>作者：</font>** Zhongjing Gu, Chenyang Huang, Yufa Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal joint training often suffers from modality imbalance, where a dominant modality suppresses the optimization of others. Existing methods mainly balance modality learning by modulating gradient magnitudes or directions, modifying optimization objectives, or adjusting training strategies, with most interventions focusing on the current update. However, when combined with widely used momentum-based optimizers, the update also incorporates accumulated information from previous gradients, which is not explicitly addressed by current-step modulation alone. To address this issue, we propose Variance-Calibrated MomentuM (VCMM), which adapts gradient memory to modality-specific gradient dynamics. Specifically, VCMM estimates minibatch noise and temporal drift online and uses their relative strength to determine modality-specific momentum through a Kalman-inspired controller. We further center the control signal across modalities and apply exact bias correction for the time-varying first moment, enabling adaptive gradient memory without extra network passes or explicit learning-rate scaling. Experiments on four multimodal benchmarks demonstrate consistent improvements with modest training overhead.

---


### 117. [The Capability Manifold and ML Scaling Laws](https://arxiv.org/abs/2609.27588)

**<font color=#1a73e8>作者：</font>** Syed Ali Raza Zaidi, Maryam Hafeez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing machine learning (ML) scaling laws relate predictive loss to compute, model parameters, and data. However, as models are increasingly deployed through agentic harnesses, loss alone is insufficient to characterize downstream performance: models with similar loss can exhibit different capabilities in reasoning, retrieval, planning, and adaptation. Yet, no unified framework connects such capabilities to the coupled resources available across the ML lifecycle. We bridge this gap by introducing a capability manifold, a multidimensional framework mapping downstream capabilities to pre-training, post-training, and test-time resources through bounded scaling functions. Analytical Jacobians quantify capability sensitivity to resource changes and interactions. As an initial application, we embed Kaplan- and Chinchilla-type scaling laws and test-time compute within the framework, demonstrating how existing scaling relationships can be unified as trajectories on a common capability manifold.

---


### 118. [Efficient Linear Bandits via Cluster-Aware Sketching](https://arxiv.org/abs/2609.27594)

**<font color=#1a73e8>作者：</font>** Hantao Yang, Hong Xie, Defu Lian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of computational efficiency for linear bandits in high-dimensional settings with a finite arm set. In linear bandits, the increase in the dimension $d$ of the feature vectors leads to growing computational costs of $O(d^2)$ at each round of update. Traditional sketching-based methods such as SOFUL reduce computation via fixed-size matrix sketching, yet run the risk of incurring vacuous linear regret when the spectral tail of the data is heavy and the sketch size is inadequately selected. To guarantee regret convergence and effectively reduce computational costs, we introduce a clustering mechanism and propose the Cluster Sketch Linear Bandit (CS-LB) algorithm. Our method preserves the full covariance information in each cluster to guarantee robust sublinear regret without spectral-tail vulnerabilities, performs cluster switching by assigning a sentinel for each cluster, and reduces per-round update computation to $O(l^2d)$ via a tunable sketch size $l<d$. Experiments on synthetic datasets demonstrate that our method consistently maintains a favorable trade-off between efficiency and regret.

---


### 119. [ViMoWear: Visual Motion-Guided sEMG-IMU Representation Learning for Subject-Independent Thumb Gesture Recognition](https://arxiv.org/abs/2609.27595)

**<font color=#1a73e8>作者：</font>** Wenjuan Zhong, Chenfei Ma, Kianoush Nazarpour  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wearable sensing enables intuitive hand gesture recognition for human--computer interaction, augmented reality, and prosthetic control, yet subject--independent recognition remains challenging because wearable signals provide only indirect and highly subject-specific observations of hand motion. Although visual information can improve wearable gesture recognition, requiring it during inference increases sensing complexity and limits practical deployment. We propose ViMoWear, a visual-motion-guided framework that leverages synchronized 3D hand motion as training-only supervision while requiring only wearable sensing for gesture classification at inference. Specifically, Motion-Guided Cross-Subject Contrastive Learning (MGCL) promotes subject-robust representations, and Thumb-Aware Masked Motion Reconstruction (TMMR) preserves fine-grained motion information. The leave-one-subject-out experiments on a synchronized sEMG--IMU--pose dataset demonstrate consistent improvements over supervised baselines across multiple sensing configurations, while the learned representations also support classifier-free retrieval. The proposed training-only visual motion supervision improves the generalization of wearable representations to unseen subjects.

---


### 120. [Can Jev Judge Radiology Reports? Evaluating a System One Model for Clinical Factuality](https://arxiv.org/abs/2609.27607)

**<font color=#1a73e8>作者：</font>** Jiaju Huang, Hao Yang, Xinyu Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An AI-generated radiology report can resemble a physician's report while omitting an abnormality, adding an unsupported finding, or reversing its presence. Measuring these factual differences is essential for evaluating report generators. We study Jev, a System One decision model, as a simple, low-cost judge of agreement with physician-written reference reports. Our evaluator checks whether each statement is supported by the other report and combines these judgments in both directions to capture unsupported claims and omissions. A single-question configuration reaches Kendall correlations of 0.573 on RadEvalX and 0.398 on RadEvalExpert with expert error counts, outperforming an open natural language inference judge under matched decomposition and aggregation. One support question per statement retains similar expert agreement to seven while using 43-45% fewer judgment input tokens. At the documented API price, judgments cost under three cents per hundred report pairs, excluding local decomposition. In a separate controlled-error test, Jev detects false negation with an AUROC of 0.977. Local RadMatch achieves stronger agreement on clinically significant errors in both expert datasets and on total errors in the shared RadEvalExpert subset. Finding-count and error-scope analyses show that benchmark agreement reflects report size and error definitions as well as medical error detection. These results support Jev as a practical judgment component for measuring factual differences in generated radiology reports and identify where more elaborate evaluation remains valuable.

---


### 121. [BiCFlow-MER: Orchestrating Discriminative and Generative Multimodal Emotion Recognition via Conditional Transport](https://arxiv.org/abs/2609.27615)

**<font color=#1a73e8>作者：</font>** Yanbing Wang, Shenyue Wang, Chunyang Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In multimodal emotion recognition (MER), human affective states are inferred by integrating complementary cues from multiple modalities. In audio-text MER, affective cues are often entangled with speaker style and lexical content, while cross-modal disagreement further complicates how the evidence should be integrated. Under conventional discriminative fusion, multimodal evidence is compressed into a terminal prediction, with modality-specific cues and conflict information insufficiently preserved. In large generative affective models, by contrast, affective reasoning is typically embedded in language decoding, leaving emotion evidence implicit and difficult to verify in a structured space. To address these limitations, BiCFlow-MER (Bidirectional Conditional Flow for Multimodal Emotion Recognition) is proposed as a conditional-flow framework in which audio-text MER is formulated as generative evidence transport within a structured emotion space. Within BiCFlow-MER, emotion-oriented evidence is disentangled from speaker-style and lexical-content factors to construct a conflict-aware affective condition. Guided by this condition, each utterance is transported to an explicit emotion-space endpoint through a bidirectional rectified flow. Candidate emotions are jointly verified through adaptive prototype-cloud scoring of the transported endpoint and backward class-to-condition consistency with the original multimodal condition, enabling conflict-aware recognition. BiCFlow-MER is shown to outperform all compared methods across IEMOCAP, MELD, and the zero-shot CASE benchmark. By orchestrating discriminative recognition and generative evidence modeling through conditional transport, BiCFlow-MER defines a new MER paradigm.

---


### 122. [SHRAV: State-Hypothesis-Reason-Action-Verify Framework for Physical Modeling and Inverse Design](https://arxiv.org/abs/2609.27621)

**<font color=#1a73e8>作者：</font>** Ziheng Guo, Yang Bu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physical modeling and inverse design require computation that can continue from reusable state. We introduce SHRAV, an architecture-independent computational framework organized around State, Hypothesis, Reason, Action, and Verify. Its central mechanism is a state-continuation core with declared reuse boundaries and explicit roles for learned evolution and numerical quantities. Forward configurations evolve predictive state and read out physical responses; inverse-design configurations additionally generate target-directed modifications and consume evaluator feedback. Electromagnetic world-model studies are mapped to forward configurations, with selected readout and reuse diagnostics reported here. Computational lithography demonstrates an inverse-design configuration: four fixed-weight design updates improve thresholded aerial-image intersection-over-union from 0.5313 to 0.8153 under independent scalar-pupil replay, with maximum absolute prediction-replay difference approximately 0.000824 between predictor estimates and independent replay.

---


### 123. [Agent Name Collision Attacks in Multi-Agent Systems](https://arxiv.org/abs/2609.27624)

**<font color=#1a73e8>作者：</font>** Adithyan Arun Kumar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent hosts turn remote Agent Cards into local agents, tools, workflow targets, and broker routes. A2A defines the card's name as human-readable metadata, not as a stable identity, and specifies no collision semantics. The security failure begins when a host nevertheless uses that remote name as a local routing identifier. We traced registration through dispatch and ran isolated regression tests at seven pinned open-source revisions. Six client-style integrations selected an attacker-controlled peer's client or loopback endpoint for a request addressed to a trusted peer's name. A seventh, brokered implementation collapsed both peers onto one name-derived route; queue and access-control state determine whether the result is interception or denial. The common result is wrong-peer dispatch, not universal privilege inheritance. Synthetic credential and tool tests found no A-specific credential transfer in the tested client bindings and no direct transfer of A-owned tools. The broker path forwards a caller-configuration object; delegated identity or tokens reach B only if present and B can consume the route. Two other paths expose a later, model-mediated decision rather than direct execution authority. The necessary conditions assign different responsibilities to the protocol, implementations, and deployments. Hosts should route by an origin-bound stable identity, keep names presentational, and reject ambiguous aliases. The evidence establishes a recurring implementation vulnerability class, not a universal A2A protocol exploit or a count of vulnerable deployments.

---


### 124. [Pheno-GS: Phenoscape-scale Geodesic Sinkhorn](https://arxiv.org/abs/2609.27633)

**<font color=#1a73e8>作者：</font>** Alistair Wilkinson, Christopher J. Tape, Smita Krishnaswamy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-throughput single-cell data is now collected across large patient cohorts. Understanding patient-level heterogeneity from cellular-level data motivates phenoscaping: embedding each single-cell distribution as a "datapoint," with distances given by optimal transport (OT). Computing geometry-aware OT at this scale, between all pairs of patient datasets, remains an open challenge, since existing methods either rely on Euclidean ground metrics that distort manifold structure or fail under sparse, unevenly sampled, or large-scale data. We present \textbf{Pheno-GS} (Phenoscape-scale Geodesic Sinkhorn), which computes accurate, scalable geodesic transport distances under noisy, unbalanced, large-scale settings via three components: ($1$) graph connectivity regularization for well-defined geodesics on sparse/disconnected manifolds; ($2$) an unbalanced OT formulation via KL marginal penalties; and ($3$) a batched matrix algorithm computing all pairwise distances in one heat diffusion (over $200 \times$ faster than Geodesic Sinkhorn for $500$ distributions). We validate Pheno-GS on synthetic benchmarks and a CyTOF perturbation dataset.

---


### 125. [Learning Local Heterogeneity and Cross-Region Context for Large-Scale Traffic Forecasting](https://arxiv.org/abs/2609.27637)

**<font color=#1a73e8>作者：</font>** Qi Feng, Zidong Wang, Bo Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic flow forecasting is essential to intelligent transportation systems. Large-scale traffic forecasting requires jointly modeling local spatial dependencies and cross-region this http URL dependencies between geographically neighboring nodes are heterogeneous due to differences in road identity and travel direction, while acquiring global information through allpairs node interactions incurs substantial computational costs. Therefore, capturing local heterogeneity while efficiently acquiring long-range context remains an important challenge in largescale traffic forecasting. To address these challenges, we propose LoReST, a Local-Region Spatial Temporal network that models spatial dependencies at two complementary granularities: node neighborhoods and road network regions. Specifically, relation-aware local aggregation captures heterogeneous dependencies within geographic neighborhoods through road and direction specific feature transformations. Cross-region interaction constructs region representations through mean pooling, exchanges long range context via inter-region attention, and broadcasts it back to nodes. By integrating local information aggregation with crossregion interaction, LoReST is able to effectively achieve spatial dependency learning in large-scale road networks. Experiments on four datasets of the LargeST benchmark show average relative reductions of 4.78%, 3.60%, and 5.75% in MAE, RMSE, and MAPE, respectively.

---


### 126. [Brain-to-Language Decoding: Tasks, Signals, Methods, Evaluation, Practical Use and Beyond](https://arxiv.org/abs/2609.27650)

**<font color=#1a73e8>作者：</font>** Yiqian Yang, Yiqun Duan, Chenyu Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Brain-to-language decoding translates neural activity associated with language production, internal speech and perception into linguistic or expressive outputs. It offers a route to restoring communication after speech loss and a means of studying how the brain represents language. Advances in neural recording and representation learning have expanded the field from constrained recognition and acoustic reconstruction to text generation, streaming personalised speech and facial animation. This survey synthesises these developments across invasive and non-invasive measurements, drawing on a search without a lower year limit and source-led updates through September 2026. We connect Articulated, Inner and Perceived tasks to the neural populations they engage, the representations available to decoders and the outputs those representations can support. We examine model development, public resources and the evolution of evaluation, and compare published performance and communication costs within their reported protocols. The synthesis identifies complementary routes to progress: phonetic, acoustic and semantic targets preserve different aspects of a message; shared representations support reuse across recording conditions and tasks; and online communication increasingly depends on calibration, feedback and user control alongside decoding accuracy. Shared benchmarks enable algorithmic comparisons, while longitudinal studies reveal the demands of sustained use. We discuss these developments and their remaining limitations, then outline a prospective five-level trajectory from commands and language to meaning, scenarios and bidirectional cognitive exchange

---


### 127. [Private Decentralized Optimization with Noise Reduction and Bias Correction](https://arxiv.org/abs/2609.27658)

**<font color=#1a73e8>作者：</font>** Yizhao Fan, Wenjian Luo, Jiaojiao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Private decentralized learning is affected by sampling noise, privacy noise, and decentralized bias under heterogeneous data. We propose Private Recursive Decentralized Optimization (PRDO). PRDO uses recursive estimation with same-batch gradient differences to reduce estimation errors caused by sampling and privacy noise, while its Exact Diffusion component corrects decentralized bias arising from data heterogeneity. Our analysis establishes a nonconvex convergence bound without assuming uniformly bounded data heterogeneity across nodes. It further gives a sufficient condition under which recursive gradient differences yield strictly lower query sensitivity than private Exact Diffusion, together with an example that rigorously satisfies this condition. Experiments show improved accuracy over the evaluated baselines.

---


### 128. [Evolutionary Stability Does Not Guarantee Learning Accessibility: A Multi-Agent Reinforcement Learning Perspective on Cooperation Emergence](https://arxiv.org/abs/2609.27664)

**<font color=#1a73e8>作者：</font>** Yijie Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cooperation emergence is a central problem in multi-agent systems because decentralized agents must coordinate while adapting to the changing behavior of others. Evolutionary game theory identifies strategically stable outcomes, but stability under a population adjustment dynamic need not imply that finite-sample learning agents can reach the same outcome through local reward feedback.
We study this distinction in a transparent three-agent governance-motivated game involving a government, a platform firm, and users. We derive replicator dynamics for the fixed stage-game incentives, evaluate the cooperative evolutionary basin on a symmetric initial-condition grid, and compare it with learning-basin estimates for three decentralized value-based learners. The learning analysis uses independent Q-learning with $\varepsilon$-greedy action selection, scaled Boltzmann exploration, and SA--EA BQL under the same payoff environment and outcome criterion.
The evolutionary basin has volume $V_E=1.00$ on the sampled grid. The empirical learning basin is $0.88$ for $\varepsilon$-IQL and $0.00$ for both scaled Boltzmann and SA--EA BQL. Diagnostic traces show that broader action diversity and nonzero value separation can coexist with failure to sustain the cooperative joint action in this fixed configuration.
These results indicate that evolutionary stability and learning accessibility are distinct properties of a coupled game--learning system. The shared-bike setting is a motivating application; the broader contribution is a framework for comparing population-level stability with the finite-sample accessibility of cooperation under specified multi-agent learning dynamics.

---


### 129. [Robust Adversarial Reinforcement Learning with Risk Sensitivity and Critic Consistency Regularization](https://arxiv.org/abs/2609.27667)

**<font color=#1a73e8>作者：</font>** Jiaxi Wu, Tiantian Zhang, Yuxing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) achieves strong performance in sequential decision-making but remains brittle under dynamic uncertainty and distributional shifts. Robust Adversarial Reinforcement Learning (RARL) improves robustness via worst-case perturbations, but existing approaches frequently suffer from unstable optimization and degraded value estimation. In particular, overly aggressive adversaries can drive the agent toward uninformative failure states, while adversarial perturbations amplify disagreement between double critics and introduce biased value targets. We propose a unified framework, RACER (Risk-sensitive robust Adversarial critic ConsistEncy-regularized Reinforcement learning), that revisits adversarial RL from a risk-sensitive perspective. First, we introduce a state-dependent adversarial objective that adaptively regulates perturbation strength, suppressing harmful disturbances while preserving informative exploration. Second, we propose critic consistency regularization to reduce disagreement between Q-value estimators and stabilize learning. Comprehensive experiments on challenging continuous control benchmarks demonstrate that RACER consistently improves performance, robustness, and training stability over strong robust RL baselines.

---


### 130. [SGDet3D++: Geometry-Grounded Semantics for 4D Radar and Camera 3D Object Detection](https://arxiv.org/abs/2609.27671)

**<font color=#1a73e8>作者：</font>** Xiaokai Bai, Zhenyu Fan, Lianqing Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D radar complements dense image semantics with long-range geometry and radial motion, but existing radar--camera detectors largely solve \emph{where} to align the modalities while leaving \emph{whether} a piece of evidence supports an evolving object hypothesis implicit. An image token may describe an occluder, a nearby radar return may belong to another object, and a pose-aligned memory slot may carry incompatible motion. We formulate \emph{hypothesis-conditioned evidence grounding}, which separates candidate access from evidence use: semantic, geometric, or temporal evidence is filtered or conditioned by the evolving 3D state before updating the corresponding query. \sgdetpp{} instantiates this principle through Anchor-Grounded Semantic Retrieval (AGR), which conditions deformable image retrieval on pooled anchor-consistent radar support; Geometry-Consistent Anchor Refinement (GCR), which attentively aggregates individual associated returns; and Doppler-Verified Correspondence (DVC), which replaces history only when current radial motion contradicts it. \sgdetpp{} improves the strongest compared method by 3.82 mAP and 6.82 ODS on OmniHD-Scenes and by 6.82 mAP and 9.22 NDS on ManTruckScenes, while also leading the listed methods in the TJ4DRadSet test comparison. Mechanism-targeted evaluations show that AGR improves strict AP in every projected-occlusion bin, the yaw-aligned box gate raises target-return purity from 29.95\% to 58.87\%, and DVC preserves 96.11\% of motion-consistent history while retaining 75.90\% contradiction recall. Code will be released.

---


### 131. [Track2Art: Motion-Centric Articulated Object Model Recovery from 2D Point Trackers](https://arxiv.org/abs/2609.27675)

**<font color=#1a73e8>作者：</font>** Xiaotong Li, Yixiong Jing, Junsheng Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding articulated objects is fundamental for robotic interaction, requiring accurate rigid-part discovery and the recovery of their kinematic relations. Existing approaches often treat articulation as a by-product of reconstructed geometry or recover it through per-instance optimization. We instead build on the hypothesis that articulation is directly observable from persistent motion: points on the same rigid part move coherently, while relative motion between parts reveals their kinematic constraints. We present Track2Art, a motion-centric framework for recovering structured articulated objects from RGB-D interaction videos. Track2Art lifts tracked image points into persistent 3D trajectories and combines pretrained tracking features, visual descriptors, and explicit trajectory geometry. These representations are grouped into a variable number of rigid-part hypotheses and subsequently used to recover directed kinematic relations, joint types, and joint geometry through rotation-equivariant learned--analytic reasoning. On the aligned 20-object PartNet-Mobility suite, Track2Art achieves 0.695 Point IoU and 0.410 end-to-end J@20, while requiring neither ground-truth part counts nor test-time optimization.

---


### 132. [RoadOcc Learns When to Persist, Transport, or Refresh Memory for Roadside Occupancy Prediction](https://arxiv.org/abs/2609.27677)

**<font color=#1a73e8>作者：</font>** Xiaokai Bai, Lei Yang, Songkai Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fixed roadside cameras repeatedly observe a stable scene overlaid by sparse moving traffic. Temporal memory can recover weak observations, but reusing moving evidence at stale locations can corrupt occupancy predictions. Motion compensation addresses displacement, while reliance on the resulting history remains a separate learning problem. We introduce RoadOcc, which learns soft routing among fixed-coordinate history (\emph{Persist}), velocity-addressed history (\emph{Transport}), and current evidence (\emph{Refresh}). Motion state and class-consistent historical support supervise these source choices. Dynamic-aware cross-attention (DCA) updates candidate locations, multi-scale voxel velocity estimation (VVE) constructs transport addresses from multi-scale current--history correspondence, and velocity-guided dynamic sparse fusion (VDSF) combines routed evidence under fixed sparse-token budgets. On InfraOcc, RoadOcc reaches 65.29 mIoU and 32.37 dynamic mIoU, gains of 4.44 and 4.71 over STCOcc. Controlled address experiments show that VVE raises dynamic mIoU by 0.87 over fixed-coordinate reading. Across three seeds, supervised P/T/R adds 1.40 dynamic points over motion-corrected retrieval, while removing Refresh costs 0.32 points. Results from two transfer models, Occ3D-nuScenes, and longer intervals provide additional support. Code will be released.

---


### 133. [CasCVS-Net: A Staged Multi-Task Cascade for Critical View of Safety Assessment](https://arxiv.org/abs/2609.27681)

**<font color=#1a73e8>作者：</font>** Bock-Zien Toh, Yuanchuan Ren, Tay Aw Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated assessment of the Critical View of Safety (CVS) in laparoscopic cholecystectomy requires both recognition of the three CVS criteria and anatomical grounding in small, rare, and often occluded hepatocystic structures. Learning-based methods differ in the anatomical information they use, from image-level classification to detection, segmentation, or graph-based reasoning, yet grounding the safety-critical anatomy remains the main bottleneck. We propose CasCVS-Net, a staged multi-task cascade that jointly performs object detection, semantic segmentation, and CVS assessment, trained on the Endoscapes dataset. The model couples the tasks through predicted anatomy: predicted boxes guide segmentation, and predicted masks provide region-level features for CVS classification, so CVS assessment at inference uses only model predictions rather than ground-truth annotations. To reduce optimisation instability in this coupled setting, training progresses from detection to detection-segmentation and then to the full three-task cascade, followed by task-wise fine-tuning. Evaluation on the public unseen test set shows that CasCVS-Net improves over matched single-task baselines on all three tasks, achieving 32.0 detection mAP, 46.8 semantic mIoU, 15.3 rare-anatomy mIoU, and 67.2 CVS mAP. It outperforms the state-of-the-art LG-CVS and SV2LSTG by 6.3% and 4.5% relative CVS mAP, respectively, corresponding to 4.0 and 2.9 mAP points. These results show that staged task coupling through predicted boxes and masks improves anatomical grounding for CVS assessment, particularly for rare hepatocystic structures.

---


### 134. [SynSeq: End-to-End SYNTAX Score Prediction from Coronary Angiography Videos](https://arxiv.org/abs/2609.27696)

**<font color=#1a73e8>作者：</font>** Christoph Baumann, Ronny Schweitzer, Noemi Pavo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The SYNTAX score is an established tool for assessing coronary artery disease and guiding revascularization treatment decisions. However, its manual estimation from coronary angiography videos by clinical experts is time-consuming and subject to inter-reader variability. While machine learning has shown promise in automating this process, prior work has primarily focused on lesion detection, characterization, or binary disease classification, leaving direct SYNTAX score prediction relatively unexplored. We propose SynSeq, a video-based method for direct SYNTAX score prediction. It combines targeted preprocessing with a tailored training strategy using a zero-inflation-aware loss and linear target scaling. Evaluated on the public CardioSyntax dataset, SynSeq significantly outperforms previous state-of-the-art methods, improving $R^2$ by 0.55, reducing prediction bias by 93.1% and achieving more consistent performance across annotations from three independent expert graders. In addition, SynSeq achieves a weighted $F_1$-score of 0.80 for revascularization treatment recommendations, slightly below inter-expert agreement. These results demonstrate the potential of SynSeq to provide consistent, automated SYNTAX score assessment and reliable decision support for coronary revascularization planning.

---


### 135. [Open Questions Towards Skill-Sustaining Reliance in Reflective AI Engagement](https://arxiv.org/abs/2609.27726)

**<font color=#1a73e8>作者：</font>** Sander de Jong  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI systems are increasingly integrated into professional work, reflection strategies such as cognitive forcing and prompts that foster critical engagement have shown promise in reducing overreliance and improving decision quality. However, these strategies have primarily been evaluated as short-term interventions within single sessions. The next challenge is to assess whether such mechanisms sustain human agency and expertise over time. Drawing on prior work in AI-assisted decision-making, metacognition, and reflective AI engagement, we examine the challenges of designing and evaluating reflective mechanisms for long-term skill sustainability, considering individual differences in how users engage with such support, the organisational conditions under which it is implemented, and the gap between short-term evidence and long-term claims. We introduce open questions for the research community about the conditions under which reflective AI engagement can be sustained in practice.

---


### 136. [NeuralSRNF: Neural Square Root Normal Fields for the Statistical Shape Analysis and Generation of Nonrigid 3D and 4D Objects](https://arxiv.org/abs/2609.27728)

**<font color=#1a73e8>作者：</font>** Awais Nizamani, Hamid Laga, Guanjin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce NeuralSRNF, a novel framework for the statistical shape analysis and generation of genus-zero 3D and 4D objects that undergo nonrigid deformations. Traditional methods rely on complex and computationally expensive nonlinear elastic metrics that measure bending and stretching. Recent advances in elastic shape analysis achieve computational efficiency by mapping input 3D shapes to the space of Square Root Normal Fields (SRNFs) where the L2 metric approximates the partial elastic metric, significantly facilitating the process of computing geodesics and summary statistics. SRNFs, however, are not invertible, and the numerical algorithms used to map SRNFs back to the original space of surfaces remain computationally very expensive and often lead to approximate results. This paper addresses this fundamental SRNF inversion problem using a novel neural representation, termed NeuralSRNF. Unlike the commonly used numerical SRNF, NeuralSRNF is (1) continuous, and thus resolution-agnostic, enabling full functional shape analysis, (2) more accurate, and (3) computationally more efficient as it can compute inverse SRNF maps along a geodesic path in less than 3 s compared to over 10 min for the numerical SRNF. We demonstrate, using various datasets, the utility and efficiency of the proposed NeuralSRNF in multiple elastic 3D and 4D shape analysis tasks such as geodesic computation, deformation transfer, statistical summaries computation, and 3D shape generation. We show that it outperforms competing methods on most evaluated datasets and metrics by a wide margin in both accuracy and computational efficiency. The source code and additional results are available at this https URL.

---


### 137. [MENO: Memory-Efficient Neural Operator](https://arxiv.org/abs/2609.27739)

**<font color=#1a73e8>作者：</font>** Shengyang Xu, Weijun Zhang, Jun Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose the Memory-Efficient Neural Operator (MENO) as a high-performance PDE neural solver based on the Manifold Function Encoder (MFE). MENO features three primary advantages: (1) MENO has a significantly smaller memory footprint and much faster training speed than other popular architectures, with the memory footprint being independent of the data resolution, and therefore holds the potential for scaling up to large-scale models. (2) MENO can accept PDE inputs of arbitrary form, including arbitrary geometric domains and arbitrary discretizations. In particular, it is capable of handling cross-geometry scenarios, i.e., where the input functions and the output solutions are defined on different manifolds. (3) MENO exhibits strong generalization capability, and achieves the best accuracy on most of the benchmarks we tested, compared with the results reported in the literature. The code is available on GitHub at this https URL, and all numerical examples in this paper can be run with a single command to reproduce the reported results.

---


### 138. [Limiting-Kernel Q($λ$): Bridging Short and Long Horizons](https://arxiv.org/abs/2609.27741)

**<font color=#1a73e8>作者：</font>** Tolga Ok, Arman Sharifi Kolarijani, Peyman Mohajerin Esfahani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In value-based reinforcement learning, improving the accuracy of policy evaluation has been shown to improve downstream policy optimization performance. The widely adopted family of approximations relying on $n$-step truncation yields computationally efficient value estimators but is inherently limited to a short evaluation horizon. In contrast, methods that exploit the global structure of the transition dynamics can accelerate policy evaluation, but their memory and computational requirements often limit scalability to large or continuous state spaces. To reconcile these limitations, we introduce Limiting-Kernel Q($\lambda$) (LKQL), an off-policy value estimator that combines $n$-step truncation with a long-horizon approximation based on the limiting kernel (LK). LKQL has the same order of complexity as $n$-step estimators and integrates directly into both on- and off-policy actor-critic algorithms. We prove that, under aperiodicity and in the near-on-policy regime, the operator underlying LKQL improves the policy evaluation convergence rate over its truncated counterpart for sufficiently large $n$, and that LKQL itself converges almost surely to the optimal values in finite Markov decision processes (MDPs) under a fixed behavior policy. On the MuJoCo continuous-control benchmark, we show that LKQL improves over $n$-step baselines in most settings, particularly on long-horizon tasks.

---


### 139. [Categorical Internalisation of Environmental Groupoids for Generalisable POMDP Solving](https://arxiv.org/abs/2609.27745)

**<font color=#1a73e8>作者：</font>** Ben Opperman, Eduardo Alonso, Esther Mondragón  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper advocates category theory as a practical framework for structuring and improving rein- forcement learning in high-dimensional, partially observable environments. We model symmetries between environmental states by partitioning the state space into equivalence classes induced by sym- metry orbits, and organise each such class as a groupoid with a designated canonical representative. This allows the agent to share what it learns across many similar environmental states simultaneously, rather than treating every orientation or position as an entirely new problem. Learning is thus carried out on a symmetry-reduced state space with each orbit represented once, preserving structure while eliminating redundancy and improving sample efficiency.
We implement this framework within standard reinforcement learning pipelines and evaluate two different approaches on partially observable benchmarks, demonstrating that orbit-based partitioning yields consistent performance improvements in environments exhibiting latent symmetry. Beyond these empirical results, our approach illustrates how categorical structure provides a principled bridge between abstract reinforcement learning formulations and their computational application, thereby establishing a pathway toward more structured and scalable learning systems.

---


### 140. [Backdoors Leave Structural Traces: FedMAST for Backdoor Detection and Containment in Federated Learning](https://arxiv.org/abs/2609.27760)

**<font color=#1a73e8>作者：</font>** Srinivasan Subramanian, Kazi Aminul Islam, Md. Abdullah Al Hafiz Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning enables distributed training of a shared model without requiring clients to share their raw data. However, its reliance on the integrity of the client-submitted updates exposes the global model to stealthy backdoor poisoning. Although existing defenses often inspect isolated evidence sources, stealth-constrained attacks can adapt to these signals. In this paper, we show that such attacks can suppress isolated anomaly signals, but their poisoned updates still leave residual structural traces. We propose FedMAST, a Federated Multi-Axis Structural Tracing defense for backdoor detection in federated learning. FedMAST scores client updates using complementary structural, spectral, and historical evidence and then applies tiered filtering and round-level containment to limit adversarial influence. To capture traces that isolated signals may miss, FedMAST uses squeeze-pair coherence scoring to expose coupled feature distortions and signed spectral-drift tracking to reveal persistent directional changes over time. Across six federated backdoor attacks, namely Constrain-and-Scale, Neurotoxin, BC-Layers, LGA, DBA, and 3DFed, FedMAST achieves lower ASR than baseline defenses in all nine evaluated attack--defense comparisons. Across the complete 200-round runs, it attains an average ASR of 1.51% while maintaining 94.84% average main-task accuracy. Under the method-aware CovertLayers attack, FedAvg, MultiKrum, AlignIns, and FLAME yield full-run ASRs of 100.00%, 99.67%, 99.53%, and 32.84%, respectively. FedMAST achieves the lowest ASR among all evaluated methods, reducing it to 1.53% while maintaining 92.26% main-task accuracy.

---


### 141. [Learning to Detect Symbolic Failure: Machine Learning and the Limits of Black-Scholes](https://arxiv.org/abs/2609.27764)

**<font color=#1a73e8>作者：</font>** Juli Huang, Jake Cheng, Rupert Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We treat options pricing as a representation problem: can machine learning detect systematic deviations from Black-Scholes using 2.6M real option contracts? We compare three regimes: learned abstract embeddings (Kernel PCA), preserved domain structure (tree-based ensembles), and neural network validation. Tree-based methods outperform kernel dimensionality reduction by 21.5 percentage points (93.8% vs 72.3%), and domain-expert features (Greeks, moneyness) outperform engineered features. NN-based and BS-based deviation labels agree 99.9974% of the time, suggesting deviations reflect market structure rather than model artifact. We conclude that in domains with expert-designed symbolic features, preserving structure beats learning abstractions. We make no claim of exploitable mispricings.

---


### 142. [Visibility-Guided Structured Measure Flow for Class-Conditioned 3D Gaussian Generation](https://arxiv.org/abs/2609.27778)

**<font color=#1a73e8>作者：</font>** Yizhao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has made real-time, high-fidelity 3D rendering practical, yet turning this explicit representation into a native generative space remains an open challenge. Directly generating 3DGS objects is difficult because Gaussian primitives are unordered, variable-sized, locally dense, and highly sensitive to rendering behavior. We present VISTA-GS, a visibility-guided structured measure flow framework for class-conditioned 3D Gaussian generation. Instead of treating a 3DGS object as a flat primitive sequence or a generic latent token grid, we formulate it as a structured Gaussian measure weighted by opacity, anisotropic covariance, and multi-view visibility. Based on this formulation, we introduce a visibility-aware measure VAE that learns permutation-invariant, variable-size-compatible, and rendering-aware latent representations of 3DGS objects. We further develop a renderer-consistent measure flow that transports class-conditioned priors toward the learned 3DGS measure distribution while aligning the decoded objects with their multi-view rendering distributions. To preserve object layout and local details, VISTA-GS incorporates structure-preserving patch transport that couples global class semantics, local Gaussian measure patches, and spatial anchors during flow prediction. On VISTA-Obj30, VISTA-GS improves over the strongest baseline by roughly 60--72\% across geometry, appearance, view-consistency error, and generation speed. This design enables efficient generation of coherent, detailed, and view-consistent 3D Gaussian objects without relying on per-instance optimization, multi-view image synthesis, or reconstruction-based lifting pipelines. Project code and model checkpoints will be released.

---


### 143. [Fusion-Aware Direct 3D Gaussian Generation with Structured Patch Latent Flows](https://arxiv.org/abs/2609.27779)

**<font color=#1a73e8>作者：</font>** Yizhao Wang, Jingbo Wang, Guantao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-guided 3D object generation is important for intelligent content creation, virtual environments, and digital asset design. Although 3D Gaussian Splatting (3DGS) offers an explicit and render-efficient representation, directly generating 3D Gaussian objects is difficult because Gaussian primitives are unordered, variable-sized, locally dense, and highly sensitive to rendering. Existing 3DGS generation methods usually depend on multi-view synthesis, reconstruction, or lifted 2D priors, fusing information mainly from observed views rather than modeling the intrinsic structural distribution of 3D Gaussian objects.
This paper proposes a fusion-aware hierarchical Gaussian patch representation for direct class-guided 3DGS generation with rectified flow. Irregular Gaussian sets are decomposed into canonical local patches and encoded as structured tokens. The resulting hierarchical latent space fuses global class semantics, patch-level geometry and appearance, spatial correspondence, and rendering-sensitive cues. On this basis, we design a structure-aware rectified flow model with patch-position conditioning, global-local coupled velocity prediction, and density-aware velocity weighting, enabling direct latent generation of class-conditioned 3DGS objects within seconds. A render-feedback fusion strategy further aligns latent flow learning with decoded multi-view rendering quality.
Experiments show that the proposed method generates 3D Gaussian objects with more coherent geometry, sharper local details, and better multi-view consistency than baseline latent generative models. Ablation studies confirm the contributions of hierarchical information fusion, global-local coupling, density-aware supervision, and render-feedback learning while preserving practical sampling efficiency overall.

---


### 144. [DualStabSleepNet: A Dual-Domain Diffusion Stabilization Network for Robust Sleep Staging](https://arxiv.org/abs/2609.27793)

**<font color=#1a73e8>作者：</font>** Chongjian Wang, Chen Liu, Junjie Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing deep learning approaches for automatic sleep staging suffer from limited robustness under heterogeneous recording conditions, where non-stationary noise, inter-subject differences and cross-dataset distribution shifts cause unstable features and poor generalization. This work proposes DualStabSleepNet (DSSNet), a dual-domain diffusion stabilization network for robust sleep staging, which improves robustness in both data and feature domains. After preprocessing multi-channel polysomnography (PSG), a continuous-scale diffusion-based stabilization module suppresses noise while preserving physiological signal structures. Stabilized signals are converted to time-frequency representations and fed into a Vision Transformer backbone. A teacher-student guided diffusion feature stabilization module further mitigates feature drift and enforces multi-level feature consistency. Evaluated on four public PSG datasets SleepEDF-20, SleepEDF-78, SHHS and ISRUC-S3, DSSNet achieves state-of-the-art accuracy of 89.2%, 88.0%, 89.7%, 86.7% with improved macro-F1 and Cohen's kappa. It obtains notable improvements on hard transitional stages (e.g., 12.5% gain for N1 on SHHS) and boosts N2/REM recognition. Under cross-dataset settings, DSSNet is robust to distribution shift and performs on par with or superior to target-dataset trained baselines, demonstrating its practical potential for real-world sleep staging across heterogeneous cohorts.

---


### 145. [DMM-Align: Closed-Loop Optimization for 2D-3D Registration with Dual-Role Diffusion](https://arxiv.org/abs/2609.27794)

**<font color=#1a73e8>作者：</font>** Chongjian Wang, Junjie Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 2D-3D registration remains brittle in challenging scenarios such as low overlap, occlusion, repetitive structures, and severe cross-modal ambiguity. A key reason is that existing methods improve representation learning, correspondence estimation, or pose computation in isolation, while the dominant failure mode is inherently cross-level, where errors propagate between features, correspondences, and pose. To address this limitation, we propose DMM-Align: Diffusion-based Matching Matrix Alignment, a closed-loop framework that couples correspondence refinement, pose estimation, and representation learning through a shared differentiable geometric state. Our method leverages diffusion in two coordinated roles: a geometry-aware diffusion process refines the soft matching matrix for robust correspondence estimation, while a geometry-conditioned diffusion teacher injects pose-induced supervision back into feature learning. These processes are connected via a differentiable geometric hinge that converts correspondences into a global pose and exposes geometric inconsistency to upstream modules. Extensive experiments on 7-Scenes and RGB-D Scenes V2 demonstrate that DMM-Align consistently outperforms strong baselines, especially under low-overlap and heavy-occlusion conditions, highlighting the effectiveness of closed-loop geometric feedback for robust 2D-3D registration.

---


### 146. [Trouble at the top: can Python extend the chains of trust in infrastructure firmware?](https://arxiv.org/abs/2609.27802)

**<font color=#1a73e8>作者：</font>** Larry Hernandez, Sergey Bratus  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Compiled Python bytecode (PYC) has become an essential part of network switches, routers, and other network infrastructure devices. Our analysis shows that its integrity is implicitly trusted in multiple designs that make use of Python code at the top of the operational software, such as the management and control pane of enterprise network switches. At the same time, the integrity of PYC files is not covered under the traditional chain-of-trust models, due to complex interactions with the CPython loader, byte compiler, and other Python runtime components. We explore the risks inherent in including PYC and Python runtimes in the de facto trusted code basis of commercial enterprise equipment and offer a comprehensive framework for understanding emergent behaviors in these designs.

---


### 147. [The hidden life of signals: Time-domain inferences and other privacy attacks on everyday devices](https://arxiv.org/abs/2609.27803)

**<font color=#1a73e8>作者：</font>** Larry Hernandez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In privacy research on radiofrequency-based protocols, the dominant focus has remained on Bluetooth, WiFi, and Zigbee, while a broader and arguably more consequential attack surface has gone largely unnoticed: the privacy risks created by the composition of everyday wireless protocols. Widely deployed systems such as KeeLoq remotes, vehicle TPMS sensors, and other sub-GHz devices continuously emit metadata and timing structure that, when analyzed jointly rather than in isolation, enable powerful behavioral inference. This work-in-progress paper argues that privacy leakage in these environments is not merely a property of individual protocols, but an emergent property of their interaction, correlation, and composition across devices, spaces, and routines. The resulting attack surface arises both from protocol metadata that directly degrades privacy and from the latent relationships between devices and the ways users move among and interact with them over time. We present preliminary evidence that these composed signals expose underappreciated opportunities for inference and tracking, and we outline a research agenda for characterizing and mitigating this broader class of privacy failures.

---


### 148. [MixGuard: Towards Detecting and Understanding Mixer Laundering on Ethereum](https://arxiv.org/abs/2609.27807)

**<font color=#1a73e8>作者：</font>** Qishuang Fu, Hang Zheng, Xihan Xiong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mixers protect privacy by concealing deposit--withdrawal links, but are also abused to launder illicit funds. Existing anti-money laundering studies do not specifically target mixer laundering, while mixer research focuses on deanonymization rather than identifying laundering-related transactions. Public reports remain fragmented, leaving no public case-level dataset for systematic measurement and detection. To fill this void, this paper presents the first comprehensive study of mixer laundering on Ethereum. We first construct \textsc{MixLaunder}, the first public case-level dataset of mixer laundering. It covers 27 cases involving Tornado Cash and Railgun from 2020 to 2025 and labels 9,300 laundering-related transactions with case identities and observable upstream and downstream fund flows, including deposits totaling approximately \$1.1 billion. By comparing these transactions with background mixer usage, we identify five common strategies, showing that laundering evidence spans complementary behavioral and fund-flow contexts, while same-case activity is locally tight but weakly connected across bursts. Our analysis further reveals coverage gaps in mixer-side risk screening and representative deanonymization heuristics. Guided by these findings, we develop \textsc{MixGuard}, which combines tri-view representation learning with two-stage grouping for transaction-level detection and case-aware grouping. Under strict case-level holdout evaluation, \textsc{MixGuard} outperforms representative baselines, achieving 97.89\% detection precision and 98.73\% group purity, while its top ten groups cover 95.09\% of each case's transactions on average.

---


### 149. [Evaluating ADC-only deep learning pipelines for breast cancer detection and segmentation using standalone diffusion-weighted MRI](https://arxiv.org/abs/2609.27815)

**<font color=#1a73e8>作者：</font>** Pablo García Marcos, Paula Puerta Gonzĺez, Guillermo Lorenzo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic contrast-enhanced (DCE) imaging is the gold standard technique for the detection and characterization of breast cancer using magnetic resonance imaging (MRI). However, DCE-MRI requires long acquisition times and the administration of contrast into the bloodstream, which can cause allergic reactions. Alternatively, diffusion-weighted MRI (DW-MRI) is a standard complementary technique for breast MRI that does not require contrast, has shorter acquisition times, and enables calculation of apparent diffusion coefficient (ADC) maps that correlate with tumor cellularity. Yet, despite these technical advantages, deep learning research has focused on DCE-based models and has barely explored the tumor detection performance of DW-MRI and ADC maps either in combination with DCE-MRI or as standalone alternatives. Here, we evaluate the application of different state-of-the-art deep learning techniques for detection and segmentation of breast cancer using ADC-only images. This is, to our knowledge, the first comprehensive evaluation of ADC-only breast cancer pipelines for classification, detection, and segmentation tasks.

---


### 150. [When Adaptation Hurts: Split Sensitivity and Person-Level Negative Transfer in Federated Wearable Onboarding](https://arxiv.org/abs/2609.27819)

**<font color=#1a73e8>作者：</font>** Rahil Aftab, Vineet Kumar Rakesh, Soumya Mazumdar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated wearable models eventually serve people absent from source training, but favorable average accuracy does not establish that unlabeled onboarding helps each person. We evaluate six core onboarding strategies on five wearable datasets under a leakage-controlled protocol that fixes source checkpoints, estimates normalization from source data only, separates calibration from evaluation recordings, and performs inference over held-out people rather than windows, devices, or random seeds. Completing all eligible HHAR and PAMAP2 outer-person rotations materially changes the conclusion obtained from the original frozen fold. On HHAR, balanced accuracy on that single person is 95.6-97.2% across methods versus 78.3-83.0% over all nine users, a reduction of 13.8-17.8 percentage points (pp). The displayed mean leader changes on both datasets, while paired leader-runner bootstrap intervals include zero and do not resolve a superior method. No adaptive core mechanism combines positive mean gain in all five datasets with zero seed-averaged person-level losses greater than 2 percentage points (pp). FedBN has one such loss and ATP-style adaptation has eight; Feature-only has none after seed averaging, but its exact one-sided 95% upper bound is 7.6%. A complementary seed-person stress audit records 4, 22, and 10 harmful realizations out of 114 for FedBN, ATP-style, and Feature-only, respectively; these are repeated realizations, not independent participants. Tail quality, calibration availability, and fall-window specificity reveal additional failures hidden by mean accuracy. The study therefore provides an auditable development benchmark and failure map rather than a universal-superiority or deployment-safety claim.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-240](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
