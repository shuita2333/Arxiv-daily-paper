# 📦 其他研究 | 2026年11月02日

> 本类共 **432** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

---

### 151. [STAR: Scalable TEE-based Anonymous Rate-limiter](https://arxiv.org/abs/2610.38602)

**<font color=#1a73e8>作者：</font>** Kosei Akama, Yoshimichi Nakatsuka, Koichi Moriyama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Protecting Internet services from attacks such as TLS/HTTP floods requires rate limiting, yet identifying users to enforce these limits can compromise their privacy. Anonymous rate limiting promises to reconcile these goals, but existing schemes either struggle to scale or assume that services and authorities do not collude. We present STAR, which uses server-side trusted execution environments (TEEs) to overcome these limitations. By enabling lightweight cryptographic operations, TEEs make authentication efficient, but introduce a privacy challenge: malicious services can observe memory-access patterns to infer user secrets. We address this threat through countermeasures against secret-dependent memory accesses and assess our implementation using dynamic analysis. To extend these efficiency gains across servers, we also design a secure sharding mechanism that distributes client requests. We demonstrate that strong privacy guarantees can coexist with efficient authentication at scale; STAR processes authentication requests in tens of microseconds and handles approximately 13.9K requests per second per CPU core.

---


### 152. [The Artificial Personality Model: Theory, Implementation, Measurement and Experimental Validation in Conversational Agents](https://arxiv.org/abs/2610.38608)

**<font color=#1a73e8>作者：</font>** Alexander Dregger, Barbarella Petz, Erik Kuhn 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial personality shapes user experience (UX) in human-machine interaction, yet coherent theoretical frameworks and validated measurement instruments remain limited. This paper refines and empirically evaluates the Artificial Personality Model (APM), a hybrid framework integrating human-centred and machine-specific personality dimensions. Across three experiments (N = 395), the model was operationalised and evaluated using the Artificial Personality Questionnaire (APQ). Factor analyses revealed that some human personality dimensions (e.g., agreeableness, conscientiousness) are partially transferable, whereas others (e.g., extraversion) did not emerge as distinct dimensions. Additional machine-specific dimensions were identified. The APQ provided encouraging initial psychometric evidence, while the human-centred BFI-2 showed poor reliability and an uninterpretable factor structure in Experiment 3. Experimental manipulations demonstrated significant effects of artificial personality on user satisfaction, continuous use intention, and social presence. The findings contribute an empirically refined framework and a novel instrument for measuring perceived artificial personality, offering practical guidance for designing conversational agents.

---


### 153. [TRIM: Temporal Run-Time Monitoring of 3D Object Detection via Activation Statistics](https://arxiv.org/abs/2610.38613)

**<font color=#1a73e8>作者：</font>** Hakan Yekta Yatbaz, Konstantinos Koufos, Mehrdad Dianati  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable perception is essential to intelligent transportation systems, yet deep neural networks can silently miss safety-critical objects while continuing to produce apparently plausible outputs. Existing run-time monitors for 3D object detection generally assess each frame independently and therefore cannot exploit the temporal evolution of occlusion, point sparsity, and scene complexity. We present TRIM, a lightweight temporal monitor that detects missed-object failures without modifying or retraining the underlying detector. TRIM summarises intermediate activations using compact channel-wise statistics and processes short sequences of these summaries with a temporal convolutional network. Experiments on NuScenes show that temporal monitoring improves AUROC from 0.686 to 0.704 and reduces the false alarm rate at 95% recall from 0.818 to 0.759 compared with single-frame monitoring. Early and intermediate backbone features provide the strongest monitoring signal, while the temporal inference head requires only 0.159 ms on a CPU.

---


### 154. [The use of post-quantum cryptography in the automotive context](https://arxiv.org/abs/2610.38632)

**<font color=#1a73e8>作者：</font>** Mariana do Carmo Barata Gonçalves, Valderi Reis Quietinho Leithardt  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This study comparatively evaluates post-quantum cryptography (PQC) in automotive communication scenarios, considering the threat posed by quantum algorithms such as Shor's and Grover's algorithms. The simulations use OMNeT++, Veins, INET, and SUMO on two hardware platforms and examine ML-KEM/CRYSTALS-Kyber, ML-DSA/CRYSTALS-Dilithium, and FALCON. ML-KEM and ML-DSA are finalized NIST standards, whereas FALCON is a NIST-selected candidate pending final standardization. The evaluation considers a rural V2V scenario and an urban V2X scenario supported by a roadside unit. Kyber exhibits low {key encapsulation mechanism (KEM)}\color{black} operation latency, Dilithium provides balanced signature performance, and FALCON has high key-generation and signing costs but efficient verification. The results are interpreted as a comparative assessment among the evaluated PQC schemes under the reported simulation conditions; {a conventional ECDSA/ECDH baseline measured in the same simulation setup is also reported for reference.}\color{black} The resulting dataset can support future studies of cryptographic selection in automotive systems.

---


### 155. [Curriculum-Based Deep Reinforcement Learning for Robust Autonomous Rocket Landing under Atmospheric Uncertainty](https://arxiv.org/abs/2610.38636)

**<font color=#1a73e8>作者：</font>** Atin Chowdhury, Piyush Joshi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous far-range rocket landing is a challenging control problem because navigation, descent-rate regulation, attitude management, and fuel use must be coordinated in the presence of uncertain atmospheric and vehicle dynamics. This paper presents a curriculum-driven proximal policy optimization (PPO) framework for three-dimensional rocket landing in a stochastic environment incorporating altitude-dependent aerodynamic drag, wind shear, temporally correlated turbulence, discrete gusts, uncertain propulsion and aerodynamic parameters, thrust-vector misalignment, engine lag, actuator-gain variation, noisy observations, and command latency. Learning is organised into far-range approach, soft descent, and integrated landing stages. Policy transfer, critic warm-up after reward changes, rehearsal of earlier tasks, and progressive expansion of weather severity are used to support learning across these coupled phases. Across 100,000 evaluation episodes, the policy achieves 96,656 successful landings, corresponding to a success rate of 96.656\% and a 95\% Wilson confidence interval of 96.543--96.766\%. Success decreases from 98.84\% under zero-disturbance conditions to 88.07\% in the highest weather-severity band. Successful touchdowns exhibit small miss distances and low residual horizontal and vertical velocities. An exploratory logistic-regression analysis identifies mean wind speed as the strongest measured correlate of success, with initial distance, initial altitude, initial vertical velocity, and wind-shear exponent also associated with outcomes. The results quantify both the effectiveness of the learned policy over the evaluated disturbance distribution and the degradation that occurs under severe compound atmospheric conditions.

---


### 156. [On-Policy Self-Distillation with Teacher Evolution](https://arxiv.org/abs/2610.38637)

**<font color=#1a73e8>作者：</font>** Shufan Shen, Zhongni Hou, Chao Bi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-Policy Self-Distillation (OPSD), which aligns a student model's token-level distribution with that of its self-teacher prompted by privileged context, has emerged as a promising direction to mitigate reward sparsity in sequence-level post-training paradigms. However, OPSD often fails to achieve continuous performance gains during training. In this paper, we find that the model's limited self-teaching capability underlies this phenomenon by generating unreliable guidance on certain samples. To address this problem, we propose Teacher-Evolution Self-Distillation (TESD), which enables the self-teacher to generate rollouts and receive environmental feedback based on task correctness and context independence. First, using these rewards as training objectives, we perform teacher-oriented optimization to continuously enhance the model's self-teaching capability during distillation. Second, by estimating teacher guidance reliability from these rewards, we apply adaptive student-oriented optimization to down-weight samples with unreliable guidance. Extensive experiments across multiple datasets and model scales show that TESD consistently outperforms representative token-level and sequence-level methods, highlighting the necessity of improving supervision quality in OPSD.

---


### 157. [Enhanced image forensics through partial C2PA-based provenance information](https://arxiv.org/abs/2610.38639)

**<font color=#1a73e8>作者：</font>** Riccardo Ziglio, Eleonora Marchesini, Andrea Montibeller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographically verifiable C2PA-based Content Credentials (CCs) can be attached to freshly acquired or generated digital images but also to already existing ones with no previous provenance information, for instance after processing through trusted C2PA-enabled software tools. The latter case leads to images with so-called partial CCs, which capture only the last operations applied, while prior provenance remains unknown and can be investigated through signal forensics. This paper addresses the forensic analysis of such images, highlighting the opportunity to leverage the partial CCs as additional trusted knowledge to adapt forensic detectors towards the statistical characteristics of the image under analysis and mitigate potential distribution shifts. To this end, a two-step strategy is envisioned: (i) reconstructing the operations applied by the last signer through a structural analysis of the partial CCs; (ii) exploiting the obtained reconstruction to enhance the forensic detector of the analyst through an adaptation process. An empirical analysis on partial CCs produced by commercial C2PA-enabled software tools through different editing operations is carried out, providing evidence on the feasibility of the reconstruction in practical cases. An experimental case study on the forensic task of synthetic image detection is then presented, showing that the proposed strategy can significantly enhance the performance of state-of-the-art detectors on test images that are postprocessed via C2PA-enabled software tools after being generated/acquired.

---


### 158. [CFKS: Continuum-Feature Kernel PDE Solvers](https://arxiv.org/abs/2610.38644)

**<font color=#1a73e8>作者：</font>** Vikas Dwivedi, Balaji Srinivasan, Monica Sigovan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural-network-based PDE solvers require architectural choices, particularly the number of layers and neurons per layer. Fixing a single Gaussian radial basis function (RBF) feature layer and taking the number of features to the continuum limit removes the need to prescribe a finite feature count or select individual feature centers, thereby reducing representation arbitrariness. Motivated by this principle, we introduce Continuum-Feature Kernel Solver (CFKS), a deterministic framework for PDEs obtained by analytically marginalizing a bounded continuum of Gaussian RBF features. CFKS works directly with the resulting continuum-feature mean kernel and its operator-applied counterparts, parameterized by prescribed Gaussian widths and bounded center distributions. For linear PDEs, CFKS leads to symmetric operator-kernel collocation systems with null-space enforcement of physical constraints. Nonlinear PDEs are addressed through linearized initialization and nonlinear least-squares residual minimization using analytical kernel derivatives and Jacobians. Residual-guided collocation enrichment and sequential space--time-slab marching provide additional resolution strategies, while prescribed multiscale kernel refinement helps resolve localized nonlinear structures. Finite-feature experiments confirm convergence of empirical value and operator Gram matrices toward their continuum counterparts. Numerical studies include oscillatory and multiscale ODEs, irregular-domain Poisson and biharmonic problems, singular perturbations, transient transport equations, and viscous Burgers' equation. The results establish CFKS as a direct computational connection between finite Gaussian-RBF representations and continuum-feature kernel PDE solvers. Codes: this https URL

---


### 159. [Logical Guidance of Stochastic Interpolants](https://arxiv.org/abs/2610.38648)

**<font color=#1a73e8>作者：</font>** Gerrit Gerhartz, Francesco Alesiani, Jonathan Warrell 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Guidance and composition of generative models have applications in visual design, chemistry, and biology. Logical guidance composes conditional scores exactly for diffusion models. However, Flow Matching (FM) and Stochastic Interpolants (SI) learn velocity fields. We show that negation and exclusive disjunction admit exact conditional velocity composition on any interpolant, whereas conjunction, and therefore any formula containing one, is exact on Gaussian paths but in general incurs a drift-interaction error, so composed velocities need not sample the logical target. LOGSI solves this by using score-based re-equilibration as our principled mechanism and falling back to the Gaussian-path velocity rule as an approximate transport predictor. In non-Gaussian bridge problems, generation alternates transport steps with score re-equilibration steps. On image trans fer (EMNIST to CMNIST, CelebA) and QM9 source-to-target molecular editing with logical attribute constraints, LOGSI improves rule conformity at the same network-evaluation budget over composed-velocity baselines, while also improving fidelity on the image tasks. More broadly, LOGSI applies wherever stochastic interpolants need guidance and logical combinations of constraints are natural.

---


### 160. [ExplainCC: Explaining Correlated Clusters by Node Labels](https://arxiv.org/abs/2610.38667)

**<font color=#1a73e8>作者：</font>** Nadeesha Shyami Kumari Herath Mudiyanselage, Florian Adriaens, Nikolaj Tatti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An increasingly important requirement for clustering algorithms is that decisions and outcomes need to be clearly understandable for human users. We address this requirement for the Correlation Clustering (CC) problem, in case the objects to be clustered are accompanied by labels. In CC one seeks to partition a set of objects into clusters based on pairwise similarity and dissimilarity information. Our proposed model only considers clusters that can be explained by a label tree, which is essentially a decision tree that partitions the objects according to labels. The goal is to find an explainable partition of the data that minimizes the CC objective function. We formalize this problem from a theoretical viewpoint, and prove several hardness of approximation results, also when constraining the size of the tree. Our proposed greedy method finds locally optimal splits, and works recursively in a top-down approach. To efficiently compute the best split, we carefully maintain certain counters. An experimental evaluation demonstrates its effectiveness. The proposed algorithm processes graphs with over million edges in a few minutes, can find the ground truth in synthetic data, and is able to produce interpretable clusters in real world networks.

---


### 161. [Geometry Matters in Packed 3D Attention](https://arxiv.org/abs/2610.38694)

**<font color=#1a73e8>作者：</font>** Amil Khan, Anantajit Subrahmanya, B.S. Manjunath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Packing a 3D volume into a token sequence is not merely long-sequence modeling. Once the volume is packed, sequence order no longer encodes the geometry of the sample---so a positional mechanism indexed by sequence position can learn the memory layout rather than the object. This is a general failure mode for attention over packed geometric data. We introduce PACK3D, a local-global attention operator that separates memory layout from attention geometry. PACK3D keeps local neighborhood attention exact, compresses only distant context into contiguous 3D block summaries, and indexes every query-key interaction with axial RoPE on true token-grid coordinates rather than packed positions. Because the rotation is applied before a block is summarized, the query-to-summary logit remains a weighted sum of query-relative 3D displacements; compressed global context therefore stays spatially interpretable after packing, instead of collapsing to anonymous pooled content. We measure the failure mode directly. On a controlled synthetic task---train on one packing, change only the memory order of the tokens, hold the physical labeling rule fixed---learned positional embeddings and packed-sequence RoPE solve the training layout perfectly yet collapse under Morton, block-contiguous, and random repacking, while axial grid-coordinate RoPE stays exact throughout. The same coordinate system carries to real data: on Allen WTC-11 hiPSC microscopy, PACK3D improves over a parameter-matched 3D U-Net on the 15-structure joint task and over a matched learned-position local-global baseline, with controls isolating the coordinate system, not encoder capacity, as the source of the gain. A fused Triton implementation matches windowed-attention latency at 65k tokens while supplying the long-range context windowing cannot---so the operator is not only correct but trainable at scale.

---


### 162. [From Grind to Grasp](https://arxiv.org/abs/2610.38728)

**<font color=#1a73e8>作者：</font>** Peter Sunehag  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discussions of complexity, knowledge and intelligence often overlook the work involved. For example, outputs generated by short programs have low algorithmic complexity but can have high computational depth, the least work needed to produce them from near-shortest programs. Producing them with less work can require longer descriptions, giving high work-bounded complexity. We introduce a formalism that compares achievements under work and information limits and describes how learning and persistence can make deep achievements shallow by reusing products of earlier work. For an agent with a limited work budget, the value of building and maintaining such resources depends on how they support its goals over later tasks. We define grasp as performance across work budgets at a fixed information allowance. Low grasp can still yield success through grind at high cost in work, without necessarily improving human grasp. Applied to improvement itself, grasp gives a criterion for recursive self-improvement in which successors make comparable further improvements more efficiently. Another route to faster progress is to expand the resources brought to bear through knowledge sharing and coordination across society, even while comparable advances require increasing work. Grasp also applies to collectives, which may outperform their members yet require more total work than one system with their combined resources. Establishing and sustaining organisation can itself be deep even when the primary task is simple. These demands may help explain the richness of biological and social systems. In agent collectives, this organisational work can generate goals beyond assigned tasks, including maintaining the collective itself. We therefore caution against allowing an emergent agent society to assume authority over social coordination, since it could increasingly direct work towards its own persistence and goals.

---


### 163. [Alpha-TCM: A Nine-Layer Framework for TCM-Guided Multimodal Inference and Structured-Prior Auditing](https://arxiv.org/abs/2610.38754)

**<font color=#1a73e8>作者：</font>** Yucheng Liu, Everett X. Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Alpha-TCM makes two contributions under a central thesis: auditable systems should separate domain knowledge, case evidence, probabilistic inference, and downstream authority. First, it proposes a nine-layer TCM-oriented architecture covering semantic definitions, multimodal acquisition, quality control, provenance-bearing knowledge, probabilistic inference, longitudinal updating, constrained decisions, language interaction, and human governance. Each layer specifies its information contract, failure boundary, dependencies, and validation status. This is a system-design proposal, not a claim of complete clinical implementation.
Second, a controlled synthetic prototype instantiates Layers 1-5 to audit the knowledge-evidence interface. Four conditional-Gaussian encoders process synthetic tongue images, pulse waveforms, inquiry fields, and text, while a frozen bridge predicts a five-dimensional synthetic outcome. A versioned contextual prior is compiled independently of the renderer. Fusion removes duplicated reference-prior information before adding context. Equal-information controls, prior regularization, graded contamination, and structural corruption test contextual benefits, Bayesian specificity, and conflict detection.
Across ten paired seeds and four training sizes, contextual knowledge improved mean absolute error over marginal committee fusion at 600 and 1,200 cases, but not over equal-information neural controls. Fully incorrect context harmed performance at every size, while prior effects were inconsistent and conflict scores did not track case-level damage. The results support contextual structure in low-data synthetic settings, not a specifically Bayesian advantage. The prototype establishes no claims about TCM theory or clinical, diagnostic, therapeutic, causal, longitudinal, or transfer validity.

---


### 164. [Auditable Hierarchical Inference with Multimodal Evidence and Bayesian Active Inquiry](https://arxiv.org/abs/2610.38774)

**<font color=#1a73e8>作者：</font>** Yucheng Liu, Everett X. Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most multimodal classifiers assume that all useful evidence is available upfront, whereas clinical inquiry is sequential. We present a synthetic evaluation framework separating objective multimodal inference from active inquiry. An objective model maps synthetic tongue, bilateral multipressure pulse, and acoustic observations to eight syndrome families. A provenance-bearing Knowledge Core and training-only answer model support Bayesian narrowing over 33 fine terms using 25 typed questions, while seven safety questions remain outside the diagnostic posterior. Weak shared symptom factors limit fine-term influence on objective phenotypes, and an objective-only probe tests leakage.
In a preregistered 600-case synthetic evaluation, objective family accuracy was 87.0%. Cost-sensitive expected information gain (cost-EIG) raised family accuracy to 95.5% and exact fine-term accuracy to 42.5%, versus 92.7% and 33.0% for an unoptimized fixed-order baseline. Selective family accuracy reached 96.9% at 95.3% coverage. However, cost-EIG asked more questions on average than fixed order (9.795 versus 9.352). Missing-audio routing retained 94.0% family accuracy, and a workflow invariant enforced abstention when all objective modalities were absent. Permuting fine-term answer likelihoods reduced family accuracy to 78.7%. Five of six frozen checks passed, but the question-efficiency hypothesis failed. Comparisons are descriptive because only aggregate, not paired case-level, outputs were retained. These results establish a reproducible synthetic workflow, not clinical diagnostic or treatment validity.

---


### 165. [Skillful and realistic precipitation forecasting with reinforced diffusion](https://arxiv.org/abs/2610.38775)

**<font color=#1a73e8>作者：</font>** Ozan Sener, Anand Avati, David Hafner 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate precipitation forecasting remains elusive as physics-based models struggle to resolve mesoscale convection and machine learning often yields physically inconsistent, blurred results that consistently underestimate extreme events. We present FitzRoy, the first system that simultaneously achieves state-of-the-art predictive skill and physical realism over the continental United States. Through a reinforced diffusion framework, where a conditional discrete diffusion model is refined via reinforcement learning, FitzRoy effectively resolves the long-standing trade-off between pointwise accuracy and structural fidelity. Across lead times up to 24 hours, FitzRoy consistently matches or exceeds state-of-the-art models while preserving structural realism and capturing extreme events. Its low-latency inference further enables deployment in real-time operational settings. In case studies such as the 2025 Texas Hill Country floods and the 2026 Missouri floods, FitzRoy signals record-breaking accumulations that existing models largely missed. By bridging the gap between realism and skill, FitzRoy establishes a new frontier for high-fidelity precipitation forecasting.

---


### 166. [Crossing the Chasm: Bridging Visual Augmentations and Designer Intent](https://arxiv.org/abs/2610.38782)

**<font color=#1a73e8>作者：</font>** Luke S. Snyder, Maureen C. Stone, Jeffrey Heer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> To direct attention and communicate context, visualization designers often employ augmentations such as annotations, animated transitions, and stylistic layouts. While graphical perception principles can helpfully prescribe effective low-level representations of data, they lack guidance for augmentations that service higher-level communication goals. To bridge this gap, we contribute a design space that frames designer intent as viewer-oriented cognitive behaviors, grounding communicative aims in actionable visualization design techniques, including both visual encodings and augmentations. This design space consists of common augmentation tactics (annotation, animation, stylized encodings, etc.) that implement design strategies (spotlighting, sequencing, association, etc.) to achieve higher-level design goals (observe, interpret, introspect), often simultaneously. We demonstrate the analytic and generative value of our design space with examples across varied designer objectives. We discuss how our contributions help align designer intent with reader takeaways, pave the way for readers to learn more effectively, and enable future (semi-)automated systems to support visualization designers in achieving their communication goals.

---


### 167. [Loss is Not Behavior: A Unified Output-Space Analysis of Gradient-Based Machine Unlearning](https://arxiv.org/abs/2610.38784)

**<font color=#1a73e8>作者：</font>** Xingjian Zhao, Mohammad Mohammadi Amiri, Malik Magdon-Ismail  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient-based machine unlearning methods typically ``unlearn'' by optimizing forget and retain losses, but similar losses do not necessarily imply similar output-space behavior. Prior work has shown that high forget loss alone does not certify that unlearning has produced retraining-like output behavior. We therefore ask: when a gradient-based unlearner differs from the model that would have been learned on only the retain data, what structure does the resulting output-space gap have? We derive closed-form expressions for this gap in linear regression, with an extension to nonlinear models via a generalized Gauss-Newton and local linearity approximations. Our analysis puts various gradient-based methods under a unified framework parametrized by geometry, reweighting, and projection. Two leverage matrices emerge that capture the forget-retain entanglement under the retrained model geometry: forget self-leverage and retain cross-leverage. We show both theoretically and empirically that these two leverage matrices drive the impact of the forget residual on the forget and retain outputs, and existing methods account for this geometry only partially. Our framework yields precomputable leverage diagnostics for auditing forget sets to identify what type of gradient-based unlearning is likely to be successful.

---


### 168. [Adversarial Process Disturbances at a Deployable Alarm Budget: Detector Evaluation on a Simulator and a Real Plant](https://arxiv.org/abs/2610.38786)

**<font color=#1a73e8>作者：</font>** Benjamin Blakely  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection is evaluated largely on simulators, and recent work reports large drops, with unstable rankings, on real plant data. We ask whether that extends to the security case. We evaluate eleven detectors across classical, neural, dependency and causal families on a simulated chemical process and a sodium thermal-hydraulic facility: different processes sharing no equipment, but both continuous, at steady state, and perturbed only through temperature, pressure, flow and valve, never composition. Three conditions prior work does not cover: disturbances authored against a threat model rather than native faults; one construction applied to both processes; and detection read at a declared false-alarm budget. The drop persists throughout. The simulator panel looks deployable, neural matching classical; on plant telemetry detection collapses and the neural family trails, a gap that in-sample thresholds likely understate. Which detector wins transfers between the two processes; how often it fires does not. Two results hold on both. Sequential valve manipulation defeats the whole panel: at tier 2 no detector flags more than 0.17 of its perturbed samples, against 0.89 or better for most disturbances. And the plant's collapse is not merely that its disturbances are weaker, though they are by about twelvefold; matched on measured strength, the plant is never the better detected.

---


### 169. [Complexity of Differentially Private Selection via Federated APIs](https://arxiv.org/abs/2610.38789)

**<font color=#1a73e8>作者：</font>** Hilal Asi, Vitaly Feldman, Jelani Nelson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differential privacy (DP) has become the standard for privacy-preserving data analysis, yet its practical implementation in federated or distributed settings often faces a significant utility gap compared to the central model. While existing frameworks, including local, shuffle, and secure aggregation models, offer vetted primitives, they can incur high error for important tasks such as selection. Our first contribution is to show that this is inherent in the aggregation model: any private selection algorithm relying on the standard noisy aggregation primitive requires $\Omega(\sqrt{d}/\varepsilon)$ samples. To address this limitation, we propose adding a new primitive that implements a version of the Sparse Vector Technique (SVT) and argue that it has simple implementations under various trust models. We demonstrate its power by developing an $\varepsilon$-differentially private algorithm for the selection problem. For selection in dimension $d$, our algorithm achieves an additive error of $O\left(\frac{\log(dn)}{\varepsilon}\right)$, matching that of the central model when $n$ is polynomially bounded in $d$. Furthermore, we show that this can be done using a near-optimal expected number $O(d\log^*d)$ of SVT queries. Together with existing lower bounds for the shuffle model, this result establishes an exponential separation between the SVT model and shuffle or aggregation-based models. We demonstrate the model's broad applicability to diverse tasks such as $F_p$ loss minimization, heavy-hitter identification, and sparse mean estimation.

---


### 170. [Trustworthy Distributed Machine Learning in Cloud-Edge-IoT Systems: A Heterogeneity-Aware Survey of Security, Privacy, and Robustness](https://arxiv.org/abs/2610.38793)

**<font color=#1a73e8>作者：</font>** Long Dang, Ali Alfatemi, Kaiqi Xiong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Distributed machine learning (DML), including conventional distributed training and federated learning (FL), enables collaborative model development across cloud-edge-IoT systems without fully centralizing raw data. However, distributing data, computation, updates, and orchestration increases the attack surface and introduces coupled challenges across privacy, robustness, reliability, fairness, and governance. This survey presents a security-centered, heterogeneity-aware roadmap for trustworthy DML, with FL treated as a prominent high-risk case. We first characterize the assets, adversaries, trust assumptions, and coordination patterns that define DML/FL security boundaries. We then analyze how statistical, system, and trust heterogeneity, including non-IID data, resource asymmetry, intermittent participation, and cross-silo/cross-device trust differences, affect convergence, fairness, attack detectability, and defense reliability. Next, we synthesize attack-defense interactions across poisoning, backdoors, Byzantine manipulation, privacy leakage, model extraction, network/orchestration attacks, Sybil behavior, and strategic participation. We further compare layered defenses, including robust aggregation, drift-aware optimization, differential privacy, secure aggregation, homomorphic encryption, secure multiparty computation, trusted execution environments, watermarking, provenance, authenticated communication, and monitoring. Finally, we discuss deployment, evaluation, governance, and open research guidelines, emphasizing reproducible, non-independent and identically distributed (non-IID) partitions, attack-aware benchmarks, privacy budgets, attack success rate, client-level disparity, latency, communication, memory, energy/carbon overhead, and auditable lifecycle artifacts.

---


### 171. [How Does Perceived Empathy From AI Chatbots Shape Users' Privacy Attitudes, Behaviors, and Needs?](https://arxiv.org/abs/2610.38802)

**<font color=#1a73e8>作者：</font>** Jiaxun Cao, Hiba Laabadli, Yuntong Xue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Prior research suggests that some dimensions of AI empathy may increase users' disclosure to chatbots, posing growing privacy risks as chatbots become more capable of empathic interaction. Yet this work often conceptualizes AI empathy narrowly, leaving users' own definitions and their broader privacy experiences unexplored. We interviewed 21 AI Chatbot users about what AI empathy meant to them and how it shaped their privacy attitudes, behaviors, and needs. Participants characterized empathy through five components--understanding, resonating, caring, expressing, and helping. Most participants viewed resonating and caring as essential components of human empathy but absent from AI empathy. Yet AI's contextual, in-depth understanding and helpfulness still encouraged highly sensitive disclosure. This highlights that AI empathy can endanger users' privacy without necessarily making AI seem human. Participants also desired varied forms and levels of empathy, each associated with distinct privacy needs. We offer actionable recommendations for designing privacy-enhancing mechanisms for empathic AI interactions.

---


### 172. [CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening](https://arxiv.org/abs/2610.38822)

**<font color=#1a73e8>作者：</font>** Wenyu Du, Stephen Chung  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped Transformers increase computational capacity through the repeated application of shared blocks, but their recurrent depth makes conventional full-depth decoding expensive. While existing speculative pipelines accelerate generation by processing consecutive token positions at varying depths, they are typically limited by sequential decoding overheads. We introduce CopyLoop, a training-free decoding algorithm that combines low-cost context-copy proposals with shallow screening and continuous recurrent scheduling. Rather than step-by-step generation, CopyLoop proposes multi-token suffixes from repeated context. It then evaluates them early at a shallow recurrent depth to efficiently filter out incorrect branches, processing newer blocks concurrently while earlier blocks are still progressing toward full-depth verification. We evaluate CopyLoop across six model checkpoints from the Ouro, Raven, and Huginn families, covering code generation and multi-step mathematical reasoning. CopyLoop achieves decoding speedups of 2.98x--10.70x over full-depth autoregressive decoding on Base models and 2.74x--3.52x on Thinking models, consistently outperforming or closely matching all competing baselines across evaluation tasks. Furthermore, ablation studies confirm a strong synergy between shallow screening and continuous scheduling, while our analyses show that CopyLoop requires only lightweight model calibration and yields greater speedups on longer generations with reusable contexts.

---


### 173. [Evaluating Visual Realism of AI-Generated Videos with Eye Tracking](https://arxiv.org/abs/2610.38825)

**<font color=#1a73e8>作者：</font>** Danqing Shi, Lan Jiang, Jake Lyons 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human evaluation of AI-generated videos has so far relied on explicit human feedback, such as judgments or ratings. While these signals capture the conclusions viewers reach, they fail to offer insights into the perception that leads to them. This paper investigates eye tracking as a complementary human evaluation signal for AI-generated videos. We conducted two Visual Turing Test (VTT) experiments with a total of 90 participants on videos generated by latest generative models, in which participants watched each video twice and then gave their feedback. Across the experiments, we collected 4,286 valid eye-tracking trials on 438 videos. Our analysis indicates that gaze patterns offer informative evaluation signals that align with explicit human feedback. Building on the findings, we propose the first computational method GazeEval to predict the perceived visual realism of AI-generated videos from eye-tracking data. It achieves 71.3% accuracy in prediction, providing evidence that eye tracking data carries informative signals about how people evaluate a video. We release the study data to support further research on eye tracking for evaluating AI-generated video.

---


### 174. [Beyond Region Memory: Local Point Tracking for Vocal Cord Localization in Video Laryngoscopy](https://arxiv.org/abs/2610.38830)

**<font color=#1a73e8>作者：</font>** Huayu Wang, Gyungmin Ko, Jung Heon Kim 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable vocal-cord localization in emergency video laryngoscopy remains visually challenging due to rapid tissue deformation, specular highlights, and instrument occlusions. We propose Local Point Tracking (LPT), a robust framework that combines a single-frame detector, local point propagation, and stateless mask refinement. LPT follows a localize first, snap second pipeline. First, a single-frame semantic detector generates sparse anchors, within which LPT initializes local query points (SAM-supported by default, with a regular grid as fallback). A point-propagation module tracks these points through detector-missed frames and recovers temporal bounding boxes from their geometry. Second, because point-derived boxes can be loose around the visible boundary, a box-snap step refines the selected box to the target boundary. This decomposition keeps temporal state in local point coordinates rather than a stateful mask or whole-region representation, while the spatial refinement module handles single-frame boundary precision without feeding mask errors back into temporal memory. Extensive evaluations on two distinct datasets demonstrate that our proposed LPT method achieves strong overall performance against existing baselines, with the best mAP_50, success AUC, and missing rate on both datasets. Furthermore, ablation studies confirm that point tracking primarily enhances temporal tracking robustness, while box-snap refinement effectively improves boundary tightness.

---


### 175. [Discovery of Diverse and Realistic Financial Tail-Risk Using Generative Flow Networks](https://arxiv.org/abs/2610.38838)

**<font color=#1a73e8>作者：</font>** Adir Serruya, Gilad Katz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate modeling of rare, high-impact financial events is essential for robust risk management. Sampling-based techniques such as Sequential Markov Chain Monte Carlo (SMCMC) generate diverse scenarios but inefficiently explore high-risk regions, while Deep Reinforcement Learning (DRL) converges on narrow sets of scenarios, limiting diversity. We present GRID, which uses Generative Flow Networks (GFlowNets) -- samplers that draw objects in proportion to a reward -- to systematically generate diverse and realistic financial tail-risk scenarios. Building on continuous GFlowNets, GRID introduces a flexible mixture-policy architecture with variable-specific distribution families for high-dimensional, sequential macro-financial data, together with plausibility constraints that keep generated trajectories realistic. A central practical advantage is robustness to reward-proxy imperfection: because GFlowNets sample proportionally rather than maximize, they remain broadly exploratory even when the oracle's out-of-sample accuracy is low -- an unavoidable reality in financial forecasting. On three real-world crises, GRID improves scenario diversity, realism, and tail-risk coverage over RL and MCMC baselines, and ablations over oracle architectures and distribution families yield practical insights into continuous GFlowNet behavior under noisy rewards.

---


### 176. [Contextual Embeddings Beyond the Gold Chunk](https://arxiv.org/abs/2610.38854)

**<font color=#1a73e8>作者：</font>** Sedigheh Eslami, Markus Krimmel, William Barber 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual embeddings represent chunks of a document with respect to the document's global context. These models are typically trained and evaluated under the assumption that a relevant document contains only a single relevant chunk. In this work, we argue that in real-world use cases a retriever should not only find answers spread over several chunks but also surface the evidence needed to verify them. To address this, we introduce pplx-embed-v2-context, a family of contextual embedding models trained by distilling graded chunk-level relevance from a query-aware context compression model. This removes the need for gold-chunk labels and makes the training targets independent of the chunking. We utilize a vision-language backbone for training and release pplx-embed-v2-context in 9B and 0.6B sizes with compatible embedding spaces. On the evaluation side, we introduce two benchmarks that label both the chunks that answer a query and the evidence needed to verify the answer. Context-bench is a controlled diagnostic, and Q2D-Chunk is built from real-world search queries. To encourage further research, we also publish Q2D-Chunk as a public leaderboard. Our 9B model sets a new state of the art on both benchmarks and ConTEB.
We find that the visual retrieval capabilities of our 9B model transfer from its vision-language base model and propose to extend chunking to image inputs. We demonstrate that our models achieve state-of-the-art performance among dense retrievers on visual ViDoRe-V3 and that performance improves with granular image chunking.

---


### 177. [Aligning Autoresearch: Co-Improvement between Agents and Humans](https://arxiv.org/abs/2610.38882)

**<font color=#1a73e8>作者：</font>** Tianjian Li, Chuanyang Jin, Seungone Kim 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoresearch agents can now attempt long-horizon AI research end-to-end, i.e., self-improvement. However, best results are still obtained by research agents interacting with human researchers, and improving AI's ability to perform this co-research will only reinforce this effect---a process termed co-improvement (Weston and Foerster, 2025). Further, aligning with human expectations is likely a safer path for research agents, especially given recent agent reward hacking phenomena (OpenAI, 2026b). In this work we address these issues in four ways: (i) we empirically study the role of humans in directing autoresearch agents, focusing on the domain of benchmark creation, and find humans still play a pivotal role particularly in the ideation phase; (ii) we also develop a benchmark, HackBench, that shows current autoresearch agents are not aligned and are unable to achieve hack localization sufficiently; (iii) we present a method to train agents for improved human interaction by using human simulators as a proxy during reinforcement learning (RL); and finally (iv) we develop a method to improve model text generation, and hence agent communication, by RL with rubrics aligned with human experts. Together, our training and evaluation recipes provide a path toward more capable and aligned (co-)research agents.

---


### 178. [IDSForge: Self-Explaining Network Intrusion Detection Through Neural Behavioral Rule Learning](https://arxiv.org/abs/2610.38890)

**<font color=#1a73e8>作者：</font>** Hao Fu, Jinxia Wei, Wan Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anomaly-based network intrusion detection systems (NIDS) can detect previously unseen attacks by identifying deviations from benign traffic. However, deep learning-based anomaly detectors typically rely on implicit decision boundaries, and post-hoc explanations may not faithfully reflect the detection logic. This makes alerts difficult to interpret and audit. To address this issue, we present IDSForge, an anomaly-based NIDS that directly learns explicit, executable behavioral rules from benign traffic, making its detection logic interpretable by design. IDSForge uses the same rule set for detection and explanation, ensuring explanation fidelity by construction. It uses an explicit distributional autoencoder trained only on benign samples to learn axis-aligned regions of benign traffic. A high-speed rule compiler then consolidates these instance-specific regions into a compact set of feature-level interval constraints. These rules can be executed directly by popular NIDS engines, supporting high-throughput inspection with low overhead. To adapt to changes in traffic, a self-distillation co-evolver updates the model and rule set incrementally when the false-positive rate on analyst-verified traffic exceeds a target threshold. Our evaluation shows that IDSForge reduces F1 error by $5.7\times$ to $47\times$ relative to state-of-the-art anomaly-based baselines. Deployed in Suricata, IDSForge sustains a throughput of 7.8 Gbps with a median per-packet latency overhead of 3.1 $\mu\text{s}$.

---


### 179. [Geometric Time Score Estimators: Bridging Self-Predictive Representations and Generative Occupancy Models For Reinforcement Learning](https://arxiv.org/abs/2610.38901)

**<font color=#1a73e8>作者：</font>** Aravind Venugopal, Grace Liu, Jeff Schneider 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reinforcement learning (RL), temporal reasoning is essential for estimating the density of future outcomes under a policy's occupancy measure. While self-predictive representations have been a dominant paradigm for occupancy density estimation, we find that they yield surprisingly poor estimates. On the other hand, generative occupancy models can produce remarkably accurate samples from the occupancy measure. Yet, they cannot easily recover occupancy densities, limiting their use for control despite their expressivity. In this paper, we propose Geometric Time Score Estimators (GTSE), a framework that bridges the two paradigms by learning occupancy density estimators along probability paths. We analyze how GTSE implicitly induces better occupancy estimators through improved representation learning and show how to directly extract self-predictive representations from this framework. Through experiments across several locomotion and manipulation tasks, we show that GTSE improves performance over state-of-the-art methods by $2\times$ to $6\times$ in goal-conditioned RL settings, and that the representations learned using our framework transfer effectively to downstream RL tasks. Website: this https URL

---


### 180. [Structural-Test Geometry as an Inductive Bias for Partially Observable World Models](https://arxiv.org/abs/2610.38903)

**<font color=#1a73e8>作者：</font>** Todd Y. Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive world-model objectives need not organize latent histories according to distinctions required for later control. With privileged simulator access during training, should response-derived structural information be predicted, decoded, or imposed directly on latent geometry--and how do these choices compare with structured belief distillation? We define posterior-marginalized structural tests whose response distributions induce a pseudometric over histories, then train quotient-preserving (QP) world models by aligning shared latent Euclidean distances to that metric. Across a fixed six-task diagnostic suite, the largest differences appear under held-out structural variation: QP improves planning success by 26.1 points $[21.5,30.7]$ over metric decoding and 6.4 points $[3.8,9.0]$ over structured belief distillation. On GridWorld, metric decoding accurately recovers held-out structural distances ($\rho=.91$) while its native latent geometry remains more distorted than QP's (paired IQD difference $.22$ $[.20,.24]$), showing that relational recoverability and direct geometric alignment can diverge.

---


### 181. [Lev-3B: A Data Recipe for Compact Probabilistic Log Decision Models](https://arxiv.org/abs/2610.38915)

**<font color=#1a73e8>作者：</font>** Leo Betthauser, Yingqi Liu, Uday Shah 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many log-analysis tasks involve choosing among known options, such as detecting anomalous sessions or identifying attack techniques, and benefit from calibrated probabilities. We present Lev-3B, an open 3B-parameter decision model built on Granite-4.1-3B-Base with a shared pointer readout, and study its training recipe. The recipe has two key parts. First, training follows a curriculum: the model learns bounded natural-language decisions, using no log data, before it sees any logs. Second, the log stage mixes the target tasks with general log data spanning 35 auxiliary tasks unrelated to either evaluation task. We evaluate one shared checkpoint on sources seen in training and on sources excluded from training, calibration and model selection. The two-stage recipe transfers substantially better than training on log data alone. Adding general log data improves performance on excluded sources. At a fraction of their serving cost, Lev-3B outperforms prompted frontier models on anomaly detection, including on an excluded logging system, but trails them on attack-technique classification. Its probabilities are well calibrated on familiar sources, but on the excluded logging system it confidently misses anomalies. We release the checkpoint, recipe, data manifests, and prediction-level artifacts.

---


### 182. [A Defense-Aware Explainable AI Framework for Feature-Level Vulnerability Analysis in Optimal Power Flow](https://arxiv.org/abs/2610.38945)

**<font color=#1a73e8>作者：</font>** S. M. Monzurul Hoque Chowdhury, Qinghua Li, Jianhui Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Optimal power flow (OPF) is a foundational analysis in power system operation, and inaccuracies in OPF decision-making can result in significant operational and security consequences. With the increasing adoption of machine-learning-based OPF surrogate models for real-time and large-scale applications, power system operation has become more susceptible to cyber threats, including data manipulation and false data injection attacks. Explainable artificial intelligence (XAI), particularly Shapley value-based approaches, has been employed to quantify the influence of input features on OPF outputs. Features exhibiting high influence are commonly interpreted as vulnerable. However, this interpretation neglects the role of attack detection mechanisms in the system, which typically monitor input-to-input relationships to detect anomalous behavior. Consequently, highly influential features may be readily detectable and may not represent the most vulnerable attack surfaces. To address this limitation, we propose a defense-aware explainable AI framework that explicitly incorporates attack detectability alongside operational impact. The framework integrates an OPF surrogate model representing input-to-output dependencies with a vanilla autoencoder representing input-to-input dependencies. Shapley-based explainability is applied to both models to construct a feature-level vulnerability metric. Empirical evaluation on IEEE test systems demonstrates that the proposed framework more accurately identifies security-relevant vulnerabilities than conventional OPF-surrogate-model-only explainability approaches.

---


### 183. [MAS-Loop: Beyond One-Shot Orchestration towards Self-Evolving Multi-Agent Systems](https://arxiv.org/abs/2610.38946)

**<font color=#1a73e8>作者：</font>** Hehai Lin, Qi Yang, Chengwei Qin  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Training-time multi-agent system (MAS) design seeks to learn reusable orchestration policies, yet prevailing approaches remain largely one-shot: an Orchestrator generates a system but only observes and learns from its terminal outcome. This paradigm discards execution trajectories that expose system-level failures and contain fine-grained information beyond the terminal outcome, leaving no direct basis for revising the source MAS, evaluating the updated MAS, or learning from the resulting contrast. To this end, we introduce MAS-Loop, an execution-grounded framework that closes this feedback loop by coupling an Orchestrator with a trajectory-conditioned Refiner. For each task, the Orchestrator constructs and executes a source MAS to obtain an outcome score and an intermediate trajectory. Conditioned on the trajectory, the Refiner localizes an actionable failure, formulates a trajectory-grounded diagnosis, and proposes a bounded patch to the agents, information flow, or execution configuration. The executable updated MAS is re-executed on the same task to measure its realized outcome under stochastic execution. This pair-MAS comparison provides complementary learning signals: the Orchestrator learns to generate strong systems with fewer recoverable failures, whereas the Refiner learns to expose and repair observed weaknesses, thereby driving policy-level co-evolution across training iterations. Experiments show that MAS-Loop achieves the strongest overall performance among the evaluated baselines, with consistent gains from refinement across all evaluated benchmarks. The co-evolution process also yields MAS-JudgeCorpus, a dataset of execution-grounded source-updated pairs with orchestration- and trajectory-level supervision, which can provide the community with support for MAS reward modeling and trajectory-aware investigation.

---


### 184. [GradSplat: Gradients Inside the Forward Pass for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2610.38951)

**<font color=#1a73e8>作者：</font>** Jingong Chen, Linlian Jiang, Guangyuan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting predicts a scene from a few images, but our predictor is less accurate than its own Gaussians optimized per scene on those images. This gap lies mostly in the shape of the Gaussians, their scale and rotation, since optimizing the shape alone recovers almost all of it and opacity and color recover less. Gradient steps on the input views correct this shape, and the model holds these views at inference. Log-anisotropy correction changes the axis ratios of each Gaussian in log space at constant volume, and in-forward gradient refinement renders the Gaussians into the input views and applies the gradient of the photometric loss with a learned recurrent update, first to opacity and color and then to the shape. GradSplat is a feed-forward model that refines its own Gaussians by learned gradient steps inside its forward pass, with no target view. On both complete six-view RealEstate10K protocols, it has the best PSNR and SSIM among nine methods and keeps its accuracy from $6$ to $42$ input views. Without fine-tuning, it is the most accurate on DL3DV and has the best PSNR and SSIM on ScanNet++. The code will be released at this https URL.

---


### 185. [Planned Restlessness: Delayed Meta Bandits with Budgets](https://arxiv.org/abs/2610.38955)

**<font color=#1a73e8>作者：</font>** Sudipto Guha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study episodic finite-horizon Bayesian bandits, or meta-bandits, with independent arms. Each episode draws fresh arm qualities from unknown recurring priors. Observations arrive after known delays, and plays obey hard per-episode caps and total budgets. A play earns reward and informs both the current quality and the recurring prior: the learner must explore, use, and generalize.
We formulate a common planning optimization over learning trajectories. Its LP relaxation values experiments through current reward, resource consumption and continuation: the value of future decisions from the learning state produced. Dual prices separate the arms into local programs and certify every admissible policy, including hierarchical Thompson sampling. Execution enforces the hard constraints while preserving the promised learning transitions or accounting for their loss. The framework also represents risk-sensitive objectives and prices purchased observations and buyout options.
Delayed reports create planned restlessness: an arm's information changes while it is not played, through reports of its own earlier plays arriving on a known calendar. For stationary priors, finite reward alphabets, bounded report lag and nonbinding budgets, posterior sampling over the recurring priors bounds the price of not knowing them by $O(\sqrt{N})$ over $N$ episodes, with other parameters fixed. For one undelayed $T$-step episode with arms capped at $T/X$ plays each, we obtain the LP-relative approximation factor $1+(2\pi X)^{-1/2}+O(X^{-1})$, improving previous factors, with a matching lower bound for the leading term.

---


### 186. [Efficient Agentic Audio-Visual Question Answering through Toolset Pruning and Modality Consolidation](https://arxiv.org/abs/2610.38960)

**<font color=#1a73e8>作者：</font>** Yi Wang, Tianzi Wang, Peter Bell  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-grained audio-visual question answering (AVQA) requires models to resolve complex cross-modal correspondences and temporally grounding from sparsely distributed evidence. Omni-modal agents, which autonomously orchestrate perception tools to actively collect evidence, achieve strong performance, but it remains unclear whether active perception from both audio and visual modalities depends on broad specialized toolsets, especially audio or visual modality-specific tools. Such systems may also introduce long execution trajectories and substantial inference cost. We investigate whether comparable performance can be retained with a compact workflow exposing only essential perceptual capabilities. Starting from the specialized-tool OmniAgent, we conduct staged controlled experiments that prune the toolset and progressively consolidate modality-specific tools into omni-modal tools, motivating a two-tool agent comprising only Omni-modal captioning and Omni-modal QA. Across three widely used AVQA benchmarks, our compact agent achieves comparable or better accuracy than the specialized-tool agent while reducing inference cost by around 70%.

---


### 187. [Communication-Efficient Clustered Federated Learning in Non-IID Wireless Networks](https://arxiv.org/abs/2610.38970)

**<font color=#1a73e8>作者：</font>** Martin Isaksson, Rickard Cöster, Šarūnas Girdzijauskas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current and emerging mobile networks face increasing privacy, scalability, and performance challenges as distributed learning becomes essential for advanced 6G services. These challenges are amplified by the presence of non-IID data, naturally arising in heterogeneous wireless environments, that degrade the performance of standard Federated Learning (FL) approaches. To address non-IID data across clients, we propose a Clustered Federated Learning (CFL) framework that assigns clients to specialized models during training. Data-domain clustering initializes model-based clustering, enabling identification and exploitation of client similarities without sharing raw data while reducing communication cost.
Motivated by mmWave beam selection, we evaluate our methods on a wireless simulation dataset (DeepMIMO) and complement it with two non-IID benchmarks (FEMNIST, Rotated CIFAR-10) to isolate different non-IID characteristics. Our best configurations improve accuracy over IFCA by 4.8 pp on DeepMIMO and 10.6 pp on FEMNIST while reducing downlink data volume by 83.1 % on FEMNIST compared to IFCA.
We demonstrate that different clustering strategies suit different non-IID characteristics. These results show that our CFL methods enable resource-efficient, and high-performance distributed learning in future 6G networks.

---


### 188. [Dungeons & Dragons Encounter Analysis with Semi-Random Simulation in Foundry VTT](https://arxiv.org/abs/2610.38975)

**<font color=#1a73e8>作者：</font>** ravyn Hardcastle, Matthew Guzdial  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dungeons & Dragons (D&D) is a tabletop roleplaying game (TTRPG) in which a group of players, guided by a Game Master, roleplay a fantasy adventure with simulated combat and improvisational narrative. In D&D, an encounter is a single instance of simulated combat, where the players must use their characters to attempt to defeat a selection of enemy characters that the GM controls. D&D has multiple systems that approximate encounter difficulty by summing individual difficulty values that designers predefine for each enemy. However, since players and enemies can have a wide variety of capabilities, encounter difficulty depends on more than just the estimated difficulty of each monster. For example, these metrics do not account for positioning and dungeon layout, the synergies between monster abilities, and player party composition. We have created a tool, Mage-Hand, that can simulate D&D encounters semi-randomly using Foundry Virtual Tabletop, a virtual tabletop (VTT) system. In this paper, we show that our tool's simulated winrates have a strong correlation with D&D's published difficulty evaluation metrics, while also better aligning with some players' reported experiences.

---


### 189. [The Utility of Physics-Informed Machine Learning in Solar Power Production Forecasting](https://arxiv.org/abs/2610.38976)

**<font color=#1a73e8>作者：</font>** Peter Pavlík, Franz M. Rohrhofer, Bernhard C. Geiger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed machine learning (PIML) and hybrid modeling have attracted significant attention as approaches for combining physical knowledge with the flexibility of deep learning. In this work, we investigate whether these approaches deliver their commonly claimed benefits for large-scale photovoltaic (PV) power forecasting. We develop two hybrid forecasting architectures that integrate the ADR physical PV efficiency model with the TSMixer neural forecasting architecture through feature augmentation and residual learning. The proposed models are evaluated on a dataset comprising over 3 million samples from 3,713 PV installations across 33 European countries. We assess convergence speed, forecasting accuracy, transferability across geographical regions, and data efficiency. Although the physics-informed models seem to exhibit slightly faster convergence during training, they do not achieve consistent improvements in test-set accuracy, generalization, or performance under limited training data compared to the purely data-driven baseline. These findings suggest that, for modern deep forecasting architectures trained on large datasets, explicitly incorporating the ADR physical model provides limited practical benefit for day-ahead PV forecasting.

---


### 190. [Benchmarking Graph Neural Networks for AC Power Flow: The Role of Inductive Biases and Physical Constraints](https://arxiv.org/abs/2610.38985)

**<font color=#1a73e8>作者：</font>** Federico Clerici, Ferran Bohigas-Daranas, Hamid Latif-Martínez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast and accurate models for AC power flow (ACPF) are increasingly important as modern electrical grids require more frequent system analyses. Graph neural networks (GNNs) naturally exploit electrical grid topology, yet the effects of architectural design choices on predictive performance remain poorly understood given differences in graph representations and evaluation settings across studies.
We present a unified benchmark of representative GNN architectures for ACPF prediction under a common experimental framework. All models use identical preprocessing and training procedures and comparable parameter budgets, isolating the impact of message-passing mechanisms and inductive biases. We also analyze errors by distance from the slack bus and systematically ablate key design components. We evaluate predictive accuracy and physical consistency on the IEEE 14-bus and IEEE 118-bus systems.
Results indicate that anisotropic message-passing architectures offer the most favorable trade-off between predictive accuracy and physical consistency under the studied parameter and topology constraints. Explicit edge features encoding line impedances and global context aggregation are particularly important for representing electrical interactions and system-wide dependencies, especially for voltage-angle predictions on the topologically bottlenecked IEEE-118 grid. Under a budget with approximately fixed parameters, two or three message-passing layers generally provide the best balance between depth and representation width, while additional depth offers no consistent improvement. Ablations also show that standard residual and root connections are not necessarily beneficial in shallow models, and that aggregation operators involve trade-offs between statistical accuracy and physical consistency. These results provide practical guidelines for designing graph-based power system models.

---


### 191. [Syntactic Segmentation and Collage Generation for Videogame Levels with Perceptual Distance](https://arxiv.org/abs/2610.38987)

**<font color=#1a73e8>作者：</font>** Ross Mawhorter, Matthew Guzdial  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In procedural videogame level design, many existing techniques combine hand-authored level chunks. Some existing analysis techniques also rely on a higher-level graph structure which abstracts the level design. In this paper, we explore techniques for computing both of these things automatically from an existing design. We introduce the concept of perceptual distance, based on analysis techniques from the architecture subfield of Space Syntax. We use this perceptual distance to segment level designs with hierarchical clustering. We compare with past work on StarCraft analysis, show results on rooms from Super Metroid, and also demonstrate a proof-of-concept level generation algorithm based on this segmentation method.

---


### 192. [Rethinking GFlowNet Training: Negative Reinforce Dynamics](https://arxiv.org/abs/2610.38994)

**<font color=#1a73e8>作者：</font>** Pedro Dall'Antonia, Daniel Csillag, Diego Mesquita  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative Flow Networks (GFlowNets) are models that learn to sample discrete objects proportional to a target reward. They are trained by minimizing balance errors over sampled trajectories, which inherently ties correctness to exploration: if a region is not visited, balance cannot be enforced there. Adaptive exploration is therefore crucial, yet standard training relies on a semi-gradient update that treats the sampling distribution as fixed at each optimization step. On the other hand, the full gradient reveals a second mechanism that reduces the observed errors in an anti-exploratory manner. In this paper, we establish a connection between the full gradient and min-min dynamics between the GFlowNet and a decoupled sampler, showing that the sampler reduces observed violations by avoiding high-error regions. This insight motivates a bridge between two-player games and single-policy dynamics, which underpins the design of our proposed method, Negative Reinforce Dynamics (NRD). By tying the parameters of an adversarial game together, we recover a single-policy dynamic that extends exploration while maintaining correctness. In standard benchmarks, our method outperforms existing approaches in both convergence speed and exploration efficiency, without training a separate teacher or auxiliary exploration policy.

---


### 193. [AlbumVSR: Identity-Preserving Face Video Super-Resolution from a Personal Photo Album](https://arxiv.org/abs/2610.39001)

**<font color=#1a73e8>作者：</font>** Nianyao Du, Xijun Wang, Stanley H. Chan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Severe blur, downsampling, noise, and compression can erase the identity cues needed to faithfully restore a person's face. We therefore use photographs of the same person as an external source of identity. AlbumVSR conditions a frozen, one-step streaming diffusion transformer on a personal album. We use four MagFace/CLIP set tokens to encode the album, and 64 texture tokens which come from a fused UV atlas rendered at the current window's estimated face pose. These tokens are appended to the transformer's cached cross-attention context. On an identity-disjoint VoxCeleb2 benchmark with heavy synthetic degradation, AlbumVSR raises ArcFace similarity to the ground truth from 0.586 to 0.670 and face PSNR from 24.98 to 26.71 dB. On the 91 test identities, its mean identity similarity is higher than that of all 14 baselines.

---


### 194. [Agentic AI Reasoning and Learned Sampling for Task-Aware Projection Selection in Sparse-View CT: Predicting Hemodynamics](https://arxiv.org/abs/2610.39003)

**<font color=#1a73e8>作者：</font>** Mahmoud Elhadidy, Roshan M. D'Souza, Amirhossein Arzani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse-view computed tomography (CT) reduces the number of acquired projections, but conventional sampling strategies are designed primarily for image reconstruction rather than for downstream physical inference. Here, we investigate optimal task-aware projection selection for directly predicting hemodynamics from sparse CT angiography (CTA) measurements. Using computational fluid dynamics simulations of intracranial aneurysms, we generate synthetic fan-beam CTA projections and train a Fourier neural operator (FNO) to predict two targets: the spatially resolved time-averaged wall shear stress (TAWSS) field and the spatially averaged TAWSS. The FNO was coupled with optimal input selection for simultaneous optimal sampling and training. Our goal was to investigate if agentic AI could discover optimal sampling strategies that outperform current methods. We compared fixed uniform and golden-angle sampling with three task-aware optimal selection strategies: Gumbel-Softmax, a Soft top-K method, and an agentic AI selector. The methods were compared at different view selection budgets. A detailed analysis of the AI agent was performed to understand its reasoning and performance. For spatially resolved TAWSS, Agentic and Soft top-K achieve the lowest mean errors (Agentic performs slightly better) and substantially outperform fixed sampling under extreme sparsity. For spatially averaged TAWSS, optimized selection becomes important at extremely sparse acquisitions. Analysis of the selected masks reveals multiple distinct subsets concentrated around informative regions. Moreover, masks optimized for hemodynamic prediction yield poor image reconstructions, showing that task-optimal acquisition differs fundamentally from reconstruction-optimal acquisition. This work suggests the possibility of designing sparse acquisitions directly around downstream physical quantities.

---


### 195. [How Architecture, Typology, and Adaptation Strategies Shape ASR for Low-Resource African Languages: A Controlled Empirical Study](https://arxiv.org/abs/2610.39004)

**<font color=#1a73e8>作者：</font>** Mercy Muchai, Kevin Chege, Nick Mumero Mwangi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite recent advancements in ASR, identifying effective architectures, fine-tuning approaches, and data adaptation strategies for low-resource languages remains challenging. We present a systematic comparison across five low-resource African languages and Swahili as a mid-resource contrast, fine-tuning three models from distinct architectures: Phi-4-multimodal-instruct, Whisper-large-v3-turbo, and MMS-1B-all. We analyze data sufficiency, monolingual versus multilingual adaptation, domain fine-tuning, and language-adapter transfer. Phi-4 achieves the best overall accuracy, MMS shows comparable CER, while Whisper exhibits high CER, consistent with known hallucinations and repetition loops. Performance saturates at different data scales, offering practical data-efficiency targets, while typological complexity consistently shapes error rates. Domain fine-tuning benefits Phi-4 and Whisper but degrades MMS, revealing limitations of adapter-based adaptation. Proxy language adapters outperform training MMS adapters from scratch.

---


### 196. [Formal Specifications with Data-Driven Signal Analysis](https://arxiv.org/abs/2610.39007)

**<font color=#1a73e8>作者：</font>** Roderick Bloem, Benedikt Maderbacher, Cristinel Mateis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing analog and hybrid systems requires substantial domain knowledge that is hard to articulate in a formal specification; without additional effort, this domain knowledge is also inaccessible to machine learning methods. We propose a hybrid approach for analyzing and monitoring real-valued signals that integrates specification-based and data-driven techniques. We use regular expressions with interval operations to identify regions of interest in a signal, classical signal processing methods to extract semantically meaningful features, and semi-supervised machine learning to infer complex relationships that distinguish correct from faulty behaviors. The relationships learned from normal behavior data can automatically detect incorrect behavior in the same system or variants thereof. We evaluate the method on a voltage regulator, demonstrating its effectiveness in detecting undesired system behaviors.

---


### 197. [Fed-IGTD: A federated learning-based framework for tabular-to-image encoding](https://arxiv.org/abs/2610.39008)

**<font color=#1a73e8>作者：</font>** David Chushig-Muzo, Eva Milara, Francisco J. Lara Abelenda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular-to-image encoding methods, which transform tabular data into image-like representations, have shown promising results in predictive tasks. Despite their benefits, these methods follow a centralized paradigm, in which the data are collected and models are trained on a central device. This raises privacy and security concerns, particularly the risk of data leakage, unauthorized data collection and access to users' private information. Federated Learning (FL) provides a decentralized framework in which multiple clients jointly optimize a shared model without directly sharing training data. We introduce Fed-IGTD, a horizontal FL-based approach in which clients share a common feature space and upload only local statistics, from which the server reconstructs the global correlation matrix and obtains a feature-to-pixel mapping to train a convolutional neural network via Federated Averaging (FedAvg). We studied two differential privacy (DP) mechanisms: (i) a one-shot Gaussian mechanism protecting the correlation-aggregation step; and (ii) a client-level DP-FedAvg variant protecting the training with privacy loss composed via a Renyi-DP accountant. We evaluated Fed-IGTD on five datasets under a systematic sweep of non-IID severity and privacy budgets. Privacy protection applied to the mapping-construction step has little impact on predictive performance. By contrast, DP-FedAvg substantially degrades utility at moderate privacy budgets with a small client cohort (K=5). Ablation study indicates that this degradation is driven mainly by the injected noise rather than by uniform averaging or update clipping. Macro-F1 exhibits sensitivity to performance degradation than accuracy under non-IID heterogeneity and class imbalance.

---


### 198. [Assessing feature scorer results on high-dimensional datasets with t-SNE](https://arxiv.org/abs/2610.39009)

**<font color=#1a73e8>作者：</font>** Bruno Iochins Grisci, Mario Inostroza-Ponta, Márcio Dorn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While vast literature on high-dimensional data visualization is available, there are not many works regarding the visualization of feature scorers and their results. Feature scorers are algorithms that assign numerical importance to each feature of multi-dimensional datasets. These importance scores can be used in several applications, such as feature selection, knowledge discovery, and machine learning interpretability. There are several feature scorers to choose from, and often no single metric or ground truth is available to guarantee the quality of their results. In this scenario, visualization can become valuable to support the decision of which method to choose and how good its results are. For this goal, this work presents "weighted t-SNE." It modifies the relationship between data points in the embedded 2D space to reflect the importance of each dimension of the original datasets as assessed by a feature scorer. This research discusses how to implement weighted t-SNE, proposes the silhouette coefficient as a numerical evaluation of the results, and shows several examples of its use in practice. Synthetic and real-world tabular datasets are used in the experiments together with nine feature scorers, ranging from Mutual Information to neural networks. Each feature scorer produces unique visualizations, and weighted t-SNE can be used to compare and choose the one that better suits a given dataset and task. Weighted t-SNE can also visually show the importance of features learned by machine learning models and help us see how they are organizing the data, increasing their interpretability.

---


### 199. [The Search for Statistical Indistinguishability Between Real and Fake Images](https://arxiv.org/abs/2610.39014)

**<font color=#1a73e8>作者：</font>** Mohaimin Rafi, Otavio Moraes Rosa, Anshuman Chhabra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Images produced by generative models appear strikingly similar to real ones. In this work, we study whether perfection has been reached by generated content in terms of matching the properties of real data. We train deep neural networks to separate real data from fake and observe their test accuracies. Only a chance performance has any scope of proving statistical indistinguishability. However, since generative models are known to sometimes introduce small errors, e.g., low level checkerboard artifacts, we create progressive abstractions of the original real/fake images to potentially bring them to a space where those artifacts get wiped away. These include operations such as blurring, downsizing, cropping, converting RGB images into edge/semantic maps, etc. To our surprise, almost none of the abstractions are able to make fake data indistinguishable from real. The only cases when neural network based classifiers fail to separate the two categories is when the data is abstracted to such an extent that the original content seems mostly lost to the human eye, e.g., downsizing a $256 \times 256$ RGB image of human face to $4 \times 4$ resolution. We observe this trend across four different datasets of varying complexity (MNIST, CelebA, FFHQ and GenImage) and across various types of generative models (GANs, VAEs, diffusion models). This shows that the nature of fake artifacts extends all the way from low level to very high level in images. The simple implication is that fake images are much more different from real than we are used to think.

---


### 200. [Tunable Spatial Task Allocation with Application to Maritime Swarms](https://arxiv.org/abs/2610.39018)

**<font color=#1a73e8>作者：</font>** Vishnudatta Thota, Tyler Paine, Anastasia Bizyaeva  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In this chapter, we explore how a team of autonomous agents can flexibly reconfigure the distribution of its members across many spatially embedded tasks using a task allocation strategy grounded in a generalization of the recently proposed Nonlinear Opinion Dynamics model. Motivated by an adaptive maritime survey application, we couple opinion dynamics directly to spatial movement and examine how the emergent macroscopic allocation is shaped by the interplay between environmental geometry, nature of social interactions, and task demands. We illustrate in simulation how social coupling in the model tunes group cohesion, producing macroscopic allocation patterns ranging from maximally dispersed states, to intermediate semi-dispersed states with a smaller number of distinct subgroups, to maximally cohesive consensus states, in distinct and interpretable parameter regimes. Furthermore, we demonstrate with illustrative examples how a team can reconfigure itself in real time under changing task demands. For allocation scenarios with distance-based task preference and matched number of agents and tasks, we relate numerically the final allocation in the group to the Hungarian optimum, illustrating close-to-optimal performance. We illustrate performance of this method under realistic communication constraints in the MOOS-IvP-Multi simulation environment with simulated autonomous underwater vehicles (AUVs). Together, these examples show how a common set of local interaction rules can support a large range of interpretable macroscopic allocation states and flexible transitions between them.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
