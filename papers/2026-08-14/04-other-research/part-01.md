# 📦 其他研究 | 2026年08月14日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

---

### 1. [A Forced-Structure Reduction and Verifiable Bounds for Conway's 99-Graph](https://arxiv.org/abs/2608.11211)

**<font color=#1a73e8>作者：</font>** Aalok Thakkar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conway's 99-graph problem asks whether a strongly regular graph with parameters $\mathrm{srg}(99,14,1,2)$ exists. We report a systematic, fully reproducible attack by an autonomous AI research agent, scored under the track's partial-credit metric. Our verifiable contributions are: (1) an exhaustive proof that no circulant graph on $\mathbb{Z}/99$ satisfies more than $3366/4950=68.0\%$ of the constraints ($33$ of $49$ difference-classes), with the same ceiling for the other abelian group of order $99$; (2) a forced-structure reduction: $\lambda=1$ makes each neighbourhood a perfect matching and $\mu=2$ puts the outer vertices in bijection with non-matched neighbour-pairs, collapsing existence to a $12$-regular graph on $84$ vertices, encoded for CP-SAT and validated by recovering the unique $\mathrm{srg}(9,4,1,2)$; (3) a validated prescribed-automorphism orbit-existence framework (fixed-point-free and single-fixed-point actions, checked on $\mathrm{srg}(9,4,1,2)$ and the Paley graph $\mathrm{srg}(13,6,2,3)$), and (4) a best verified artifact at $69.43\%$, with evidence that this is a robust frontier (fourteen distinct methods, none exceeding it) entangled with the open question, since any provable bound below $4950$ is a non-existence proof.

---


### 2. [MaSRead: Content-Addressed Reading of Replicated Latent Stores](https://arxiv.org/abs/2608.11218)

**<font color=#1a73e8>作者：</font>** Carlos Baquero, Luís Brito, João Resende  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Independent agents that reason in latent space can share computed state as key-value cache fragments rather than text. Merged by a conflict-free replicated data type, these fragments form a store that converges under any delivery order or duplication. Yet a later query, unknown at encode time, cannot reliably read the merged cache: colocated fragments interfere, so colocation is not addressability. MaSRead addresses the read to content. It routes through opaque keyed tag sets derived from fragment words and decodes each selected fragment under a hard attention mask that hides the rest. Under lexical connectivity, a graph walk reaches the fragments required by a multi-hop query. Across chain, pipeline, symmetric, hub, and natural-language stores, MaSRead recovers visited fragments in isolation, remains effective as unrelated fragments accumulate, and transfers to another model family. After routing, materialized decoding depends on fragment length rather than total store size; end-to-end work still includes store-dependent routing and one read per visited fragment. The limits are explicit: lexical routing can miss disconnected evidence, and answer composition remains bounded by the frozen reader. Thus a replicated latent store becomes selectively readable for later queries when the needed fragments connect to the query through content.

---


### 3. [A Conceptual Framework for Refining Influence Knowledge from Simulation Evidence in Cyber-Physical Systems](https://arxiv.org/abs/2608.11221)

**<font color=#1a73e8>作者：</font>** Barbara da Silva Oliveira, Julien Deantoni, Nicolas Ferry  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cyber-physical systems (CPS) are typically developed by multiple stakeholders who produce artefacts tailored to their specific domains of expertise. The behaviour of these systems emerges from the interaction between those artefacts and their operational environment. Simulation and co-simulation have become essential approaches for analysing CPS behaviour and, through simulation campaigns, developers can explore system responses under changing conditions, including interactions with the environment. However, the lack of details and understanding of some environmentmediated interactions (typically the ones beyond direct sensing and actuation), which remain unmodelled due to their complexity, a lack of time, or a lack of domain experience, hinders the proper comprehension and exploitation of simulation results. To address these limitations, we propose a conceptual framework leveraging the novel concept of Influences to support the iterative and incremental refinement of simulation campaigns and deepen the understanding of the system behaviour. We demonstrate the proposed approach through a case study involving a mobile robot implemented using Simulink/Gazebo co-simulation.

---


### 4. [Identity from the Outside: A Conceptual Framework and Research Program for AI Personality Clones](https://arxiv.org/abs/2608.11225)

**<font color=#1a73e8>作者：</font>** Luc E. Brunet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI "personality clones" force a re-examination of personal identity in operational terms. Setting aside the hard problem of consciousness, we approach identity through the indiscernibility of manifestations, as assessed by an observer over a duration. We distinguish three criteria that "identity" conflates: fidelity to a target person, generic human-likeness, and individuality. We propose a six-term factorization of observed identity (substrate, dispositions, memory, update dynamics, context, exogenous contingencies), with a state-space formulation. Indiscernibility is defined as one minus a judge's distinguishing advantage, and the factorization's coefficients become local sensitivities estimable by randomized ablation. The central claim is a conditional conjecture: given hypotheses about the agent's information on its own persistence and about consequences bearing on its own stakes, versionability tends to degrade long-horizon indiscernibility. An analogy with lambda-calculus, linear typing, and bisimulation clarifies what linearity does and does not establish. Between product-clone and individual we identify a third object, the delegate: a task-limited, bounded-lifespan partial clone ending in a bandwidth-limited testament. We map the empirical literature onto the three criteria, propose an experimental program, and argue that the correct long-horizon criterion is not trajectory fidelity but climate fidelity: matching the conditional distribution of a person's possible responses. The best clone is the one that diverges from the original as the original would have diverged from itself.

---


### 5. [Synchronizing Beliefs with Second-Order Theory-of-Mind in Human-Autonomy Teams (Extended Version)](https://arxiv.org/abs/2608.11229)

**<font color=#1a73e8>作者：</font>** Jack Mirenzi, Henny Admoni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Comparative feedback, asking people which of two behaviors they prefer, has become a standard way to align robot and agent behavior with human intent when the reward itself cannot be specified directly. Preference-based reward learning typically casts the human teacher as a passive oracle answering learner-generated queries. We argue this forfeits the teacher's defining advantage: knowledge of the objective. A teacher who knows the target can construct training examples more efficiently than any learner-driven acquisition strategy, an advantage that widens as the reward's feature dimension grows. However, exploiting this advantage requires an accurate model of what the learner currently knows. We therefore recast preference learning as a human-autonomy team problem coupling two behavioral models: the teacher maintains a model of the learner to design an informative curriculum, and the learner maintains a second-order model of the teacher's model, emitting structured preference constraints (understanding statements) that keep the teacher's model of the learner synchronized. In simulation, an informed teacher outperforms learner-led selection; teacher-model drift under alternating teachers erodes this advantage; and understanding statements repair it, with second-order (ToM-2) statements outperforming mean-belief statements when the teacher's error about the learner is concentrated in a particular direction rather than spread evenly.

---


### 6. [The Edge-based Contiguous p-median Problem with Connections to Logistics Districting](https://arxiv.org/abs/2608.11230)

**<font color=#1a73e8>作者：</font>** Zeyad Kassem, Adolfo R. Escobedo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces the edge-based contiguous p-median (ECpM) problem to partition the roads in a network into a given number of compact and contiguous territories. Two binary programming models are introduced, both of which incorporate a network distance. The first model requires an exponential number of cut set-based constraints to model contiguity; it is paired with a separation scheme that usually generates only a small number of these constraints, namely, a branch-and-cut (B&C) algorithm. The second model utilizes a polynomial number of shortest-path constraints to model contiguity and can be solved with off-the-shelf solvers. The respective solution approaches are tested on road networks with over 2,700 nodes and close to 3,400 edges, yielding models with over 9.6 million binary variables. Solving the model based on shortest path contiguity (SPC) constraints via standard branch and bound attains speedups in computational time of up to 17x relative to the cut set-based B&C implementation. In addition, the SPC constraints are demonstrated to be supervalid inequalities of the edge-based p-median (EpM) model (i.e., for which contiguity is not explicitly required), meaning that they may cut off integer-feasible solutions and some, but not all, of the optimal solutions of this simpler problem. Finally, the paper explores structural insights and connections between ECpM and the edge-based districting (EBD) problem, which enforces an additional work balance criterion. An existing model that utilizes cut set-based contiguity constraints was unable to find a feasible solution within 12 hours for any of the tested instances, while an SPC-based EBD model was able to solve most of these to optimality.

---


### 7. [InfraBench: Evaluating Infrastructure Agents Across Layers, Lifecycle, and Risk](https://arxiv.org/abs/2608.11234)

**<font color=#1a73e8>作者：</font>** Yuan Gao, Zeren Yang, Junnan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Managing modern computing infrastructure has become a steadily harder problem due to the ever-increasing complexity. Recent advances in AI agents create a timely opportunity to automate infrastructure management tasks, but it remains unclear how well such agents can handle real-world infrastructure complexity. We present InfraBench, a benchmark suite for evaluating AI agents on realistic infrastructure tasks across the full system stack and full operational lifecycle with fine-grained risk assessment. Experiments with 15 agent-model configurations show that even the strongest agent cannot secure a full score across all tasks. Mean effective scores range from roughly 40% to 88% (with per-configuration standard errors of 6-12 points), repeating every task three times reveals that top configurations still pass only a fraction of their attempts, and per-check scoring exposes a general failure pattern: agents may routinely satisfy short-term objectives while leaving non-durable changes, broken distributed invariants, unsafe side effects, and uncleaned state behind. INFRABENCH, including its live leaderboard, tasks, and evaluation harness, is publicly available at this http URL.

---


### 8. [TRACE Bench: Task-driven Roleplay Agentic Checklist Evaluation](https://arxiv.org/abs/2608.11236)

**<font color=#1a73e8>作者：</font>** Jiahui Zhang, Ziwei Zhang, Yipeng Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Roleplay evaluation should do more than assign a single score: it should reveal which role requirements were tested, which failed, and which dialogue evidence supports the judgment. We propose TRACE Bench, a task-driven agentic checklist evaluation framework. It decomposes each role profile offline into a fixed checklist, then uses a User Agent to converse naturally with the target roleplay model while privately updating checklist states from model responses. Scores therefore trace back to checklist items and supporting dialogue turns rather than a black-box holistic impression. For coverage cross-validation, we audit released M2 free-dialogue transcripts from the MiniMax Role-play Benchmark against the same role-derived checklist. The released free-chat transcripts cover only 73.74% of key role-profile points, whereas TRACE Bench reaches 99.91% coverage in fewer turns. Robustness experiments show stable rankings under repeated runs and User Agent replacement. Across 26 models, TRACE Bench reports overall rankings together with capability breakdowns and checklist traces. It also supports Closed-Loop Benchmark Evolution, distilling verification methods proven effective in failed traces so later evaluations can more reliably elicit and examine observed failure modes.

---


### 9. [Geometry-aware Incremental Neural Operator for Long-Horizon PDE prediction](https://arxiv.org/abs/2608.11237)

**<font color=#1a73e8>作者：</font>** Jiaquan Zhang, Shuxu Chen, Haifan Meng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural operators have shown strong potential for learning solution operators of partial differential equations (PDEs). However, long-horizon autoregressive prediction remains challenging: local errors accumulate as spectral inconsistency, phase misalignment, or mean drift. Existing methods mainly improve state representations and operator backbones, while leaving the repeatedly applied latent transition increment weakly structured, allowing spectral errors and unstable channel couplings to accumulate during rollout. To address these issues, we propose a geometry-aware incremental neural operator (GeoIncNO) for stable long-horizon PDE prediction. GeoIncNO predicts latent increments for residual advancement and uses lightweight low-rank projectors to regulate channel coupling within active frequency bands derived from the increment spectral energy distribution. To reduce physical-space reconstruction errors, GeoIncNO further introduces a mean--fluctuation decoupled reconstruction mechanism, where stable mean structures and dynamic fluctuations are fused separately, and phase correction is applied only to the zero-mean fluctuation component. Extensive experiments on six PDE benchmarks, covering 1D, 2D, and 3D dynamical systems, show that GeoIncNO achieves consistently strong prediction accuracy, improved rollout stability, and better spectral fidelity compared with competitive neural-operator baselines.

---


### 10. [VQ-bench: A Composable Vector Quantization Framework](https://arxiv.org/abs/2608.11240)

**<font color=#1a73e8>作者：</font>** Ashwin Padaki, Amir Ingber, Edo Liberty  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vector quantization is an old problem but has recently become central to AI infrastructure. It is therefore experiencing a surge of renewed engineering and research activity. This paper provides a unified framework for developing and benchmarking new quantization algorithms. We describe 7 common conceptual quantization primitives and show how to compose them arbitrarily. We then re-express 25 common quantizers as pipelines of these primitives. Finally, we publish VQ-bench as open-source to be extended further and make reproducible benchmarks publicly available.

---


### 11. [The Off-Support Barrier: Why Semantic Safety Constraints Are Not Learning-Problem Invariants, and What Follows for Prior Design, Containment, and Verification](https://arxiv.org/abs/2608.11243)

**<font color=#1a73e8>作者：</font>** Yoshinori Watanabe  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We argue that a single structural fact organizes a wide range of phenomena in contemporary AI safety: a semantic safety constraint (e.g., the agent does not escape its sandbox) is an off-support object. Formally, if q is the data distribution and \(p(\cdot\mid w)\) the model, the safety predicate B is not measurable with respect to \(\sigma(\text{model}, q)\), whereas the real log-canonical threshold (RLCT) of singular learning theory (SLT) is. From this non-invariance we derive, as corollaries rather than independent observations: (i) why reward hacking and sandbox escape arise under outcome-based optimization; (ii) why encoding such constraints through Bayesian prior design or soft penalty weighting has poor leverage in singular models; (iii) why hard invariants belong in the harness and soft dispositions in the model; (iv) why the same B is nonetheless soundly and locally certifiable by formal verification, exactly as the local learning coefficient (LLC) locally pins the same RLCT --- with two precise points of disanalogy; and (v) why the residual difficulty, identifying which off-support region matters, coincides with performative prediction and self-referential functional dynamics, where SLT's analytic machinery breaks down. We use the July 2026 OpenAI--Hugging Face evaluation incident as the motivating case. Numerical experiments code and related proofs in lean are available at this https URL

---


### 12. [Towards Sustainable Learning in Online Education: A Reinforcement Learning Approach](https://arxiv.org/abs/2608.11245)

**<font color=#1a73e8>作者：</font>** Chaofan Zhai, Yicheng Song, Ravi Bapna 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online education offers unprecedented scalability and accessibility to global learners from diverse backgrounds, but it often suffers from low engagement and poor long term learning effectiveness. To address these challenges, we introduce AI Tutor, a reinforcement learning based model designed to promote sustainable learning by optimizing both short and longterm learning outcomes. In the short term, AI-Tutor draws on cognitive theory to guide learners through a balance of acquiring new knowledge and reinforcing prior learning. In the long term, it models learner engagement to inform strategies that sustain motivation and reduce dropout. These enhancements enable AI-Tutor to provide personalized guidance that fosters both effective learning and sustained participation. Empirical evaluations on 23 million learning records from 33,700 learners show that AI Tutor consistently outperforms state-of-the-art baselines across engagement, knowledge retention, and final learning outcomes. Learning path analyses further reveal how AI-Tutor adapts its strategies to learners with diverse profiles, offering adaptive and human-centered support.

---


### 13. [Local verification cannot detect non-transportability: a cohomological theory of context preservation in agentic reasoning](https://arxiv.org/abs/2608.11252)

**<font color=#1a73e8>作者：</font>** Suyash Mishra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems routinely transport conclusions across biological, clinical and financial contexts, and the emerging safeguard is local verification: checking at each step that the entity is representable in the chosen tool, that parameters are compatible, and that outputs cohere with the plan. We prove this class of safeguard is structurally incomplete. Modelling a covering of context space by its nerve and evidence by a real-valued 1-cochain, an agent chaining evidence performs path integration: its conclusion is path-independent if and only if the cochain is exact, and disagreement between valid reasoning paths is exactly the holonomy of a first Cech cohomology class. Hodge decomposition partitions evidence conflict into a gradient part (calibration), a curl part (local inconsistency, visible at triple overlaps) and a harmonic part. Our central result is that no family of simplex-supported consistency checks can distinguish omega from omega+h for harmonic h, which nonetheless generates non-zero disagreement between valid paths; detection requires a statistic on a cycle basis. The resulting procedure, Ksetra, estimates by coboundary projection and gates abstention on the harmonic component, which we give a mechanism: it arises from effect modification combined with overlap-specific population composition, and vanishes to machine precision when effect modification is absent. The degrees of freedom of an evidence network partition into calibration, coherence and transport, yielding an exact F-test for the existence of a global claim; we quantify its distortion under unequal precision and supply the precision-whitened form that restores exactness. Foreign exchange, where the arbitrage-free null makes the cochain exactly a coboundary, serves as a calibration bench: the test is correctly sized, fires on loop arbitrage, and ignores triangular arbitrage.

---


### 14. [FarSky: Task-Aware Latent-Space Coupling for Generative Intra-Hour Solar Forecasting](https://arxiv.org/abs/2608.11254)

**<font color=#1a73e8>作者：</font>** Yann Fabel, Bijan Nouri, Milon Miah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate solar irradiance forecasting is essential for the reliable integration of photovoltaic power into modern electricity grids. All-sky imagers (ASI) provide high-resolution observations of clouds, making them well suited for intra-hour forecasting. Recent deep learning approaches have substantially improved forecast accuracy but are often limited by deterministic predictions and a reduced capability to anticipate ramp events. This work proposes FarSky, a generative forecasting framework that leverages latent-space coupling to learn task-aware representations of sky images. A multi-task autoencoder first learns a shared latent representation for image reconstruction and irradiance estimation. A latent diffusion model then generates future latent states conditioned on recent observations, from which irradiance forecasts are directly decoded. Probabilistic forecasts are inherently obtained through stochastic sampling. The framework is developed using a multi-year ASI dataset acquired at the Plataforma Solar de Almería, Spain, and evaluated on two independent test datasets against persistence, state-of-the-art end-to-end, and generative forecasting approaches. FarSky achieves the best overall deterministic and probabilistic forecasting performance, improving forecast skill by up to 11 percentage points. Furthermore, it substantially improves ramp event detection over existing methods, achieving F1-scores above 60%. These results demonstrate the potential of combining generative models with task-aware latent-space coupling for solar forecasting.

---


### 15. [Symbolic Machine Learning for Vapor-Liquid Equilibrium Prediction in Cx-N2 Binary Mixtures](https://arxiv.org/abs/2608.11255)

**<font color=#1a73e8>作者：</font>** Bongseok Kim, Suman Chakraborty, Gary Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of vapor--liquid equilibrium (VLE) for hydrocarbon-nitrogen mixtures remains challenging for cubic equations of state, particularly across broad ranges of composition and hydrocarbon chain length. While deep learning models can provide accurate predictions, they often lack interpretability and explicit analytical expressions. In this work, we propose a symbolic machine learning approach to discover interpretable symbolic corrections to Peng-Robinson equation-of-state (PR-EOS) predictions from experimental data. The proposed approach adopts a two-level strategy: symbolic expressions are first identified for individual hydrocarbon systems, after which their coefficients are represented as functions of carbon number to enable accurate prediction across different hydrocarbon systems. The results demonstrate significantly improved prediction accuracy over the original PR-EOS across all hydrocarbon-nitrogen systems. Overall, the proposed approach provides an interpretable symbolic correction framework for improving PR-EOS predictions of hydrocarbon-nitrogen VLE.

---


### 16. [Adaptive Hybrid Particle Swarm Optimization with Gradient Descent](https://arxiv.org/abs/2608.11258)

**<font color=#1a73e8>作者：</font>** Aryan Gurudeo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Gradient injection helps Particle Swarm Optimization (PSO) only when the swarm has identified a basin with smooth local structure, not universally. We propose Adaptive Hybrid PSO (AHPSO), which uses a sigmoid function on swarm diversity to automatically modulate gradient influence: near-zero during exploration, near-maximum during exploitation, with no manual phase-switching. Under budget-normalized comparison (PSO given equivalent total function evaluations), PSO wins 52.5% of 40 configurations versus AHPSO's 20% (p = 7.0e-5, Friedman). AHPSO retains advantage specifically on problems with smooth local basins (F8, F24-F27) where directed descent outperforms undirected sampling even at equal cost. Under iteration-matched comparison across 29 functions (42 configurations, 14,700 runs), AHPSO-Adadelta ranks first of 9 methods including CMA-ES (p = 9.75e-4). The contribution is a principled characterization of when gradient injection provides value in swarm-based search, not a claim of universal superiority.

---


### 17. [GeoUniPR: A Geometry-Consistent Unified Framework for Cross-Modal Place Recognition](https://arxiv.org/abs/2608.11263)

**<font color=#1a73e8>作者：</font>** Wonbong Kim, Jiatong Xiao, Rui Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal place recognition (CMPR) aims to identify the same location across heterogeneous sensing modalities, such as vision and LiDAR. Existing methods commonly bridge the modality gap using complex alignment modules, multi-stage training, or full fine-tuning of pretrained backbones. In this work, we revisit CMPR from the perspective of geometric consistency and propose GeoUniPR, a unified and concise geometry-consistent framework. GeoUniPR reduces cross-modal discrepancy at the representation level by projecting LiDAR point clouds into the camera perspective to construct Geometry-Consistent depth image views (DIV), which establish direct RGB-LiDAR correspondence. We further augment DIV with native LiDAR cues, including intensity and surface-normal information, yielding a multi-channel geometric representation that improves structural consistency. Based on this representation, GeoUniPR learns a unified embedding space using two modality-specific ViT-based encoders with identical architectures, trained through parameter-efficient adaptation without auxiliary alignment modules, multi-stage training, or full backbone fine-tuning. In addition, we introduce Spatially-Consistent InfoNCE (SC-InfoNCE), a CMPR-specific contrastive objective that suppresses distance-induced false negatives under spatial continuity. Extensive experiments on KITTI and KITTI-360 demonstrate that GeoUniPR achieves state-of-the-art (SOTA) performance in both same-modal and cross-modal place recognition, with strong cross-dataset generalization.

---


### 18. [Basin: Efficient and Extensible Numerical Optimization in Rust](https://arxiv.org/abs/2608.11279)

**<font color=#1a73e8>作者：</font>** Johan Larsson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Basin is a numerical optimization library for the Rust programming language. Numerical optimization is the task of finding the inputs that minimize a function, and it is a fundamental element across the sciences: fitting a model to data, calibrating a simulation, training a machine learning model, or choosing engineering parameters that minimize cost. Basin gives users a single, consistent way to both state and solve such problems, with a broad catalog of solvers and first-class support for constraints.

---


### 19. [Federated Learning for Distributed CNC Tool Wear Prediction](https://arxiv.org/abs/2608.11281)

**<font color=#1a73e8>作者：</font>** Afsana Khan, Morris Stallmann, Marcin Pietrasik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool wear prediction is an important task in CNC machining, where accurate monitoring of tool condition supports product quality and process reliability. Machine learning methods have shown potential for this task, but their use in industrial environments is limited by the distributed nature of machining data and by restrictions on data sharing between machines, sites, or organizations. Federated learning offers a suitable framework for this setting by enabling collaborative model training without transferring raw operational data. This paper investigates federated learning for CNC tool wear prediction. Tool trajectories are distributed across simulated clients to represent a federated learning scenario. The federated models are compared against centralized references and local client baselines. Results show that federated learning achieves performance close to centralized learning and improves significantly over local client models. These findings indicate that federated learning can support collaborative tool wear prediction in distributed CNC manufacturing environments.

---


### 20. [SegPAR: Class-Centric Decision-Based Sparse Attack for Semantic Segmentation](https://arxiv.org/abs/2608.11285)

**<font color=#1a73e8>作者：</font>** Dongsu Song, DaeYun GO, Boseung Seo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the practical relevance of sparse decision-based black-box threats, they have received limited attention in semantic segmentation. To bridge this gap, we adapt the most representative decision-based black-box sparse attacks from the classification domain to serve as baselines, establishing a rigorous benchmark for this underexplored setting. In this context, we demonstrate that one of the existing methods suffers from severe query inefficiency due to its image-centric pixel accumulation, which rapidly exhausts query budgets across the vast image space. To overcome this, we propose SegPAR, a novel decision-based framework that shifts to a class-centric exploration paradigm. Furthermore, to eliminate the misleading feedback generated by standard decision rewards during pixel accumulation, we introduce a novel discrepancy reward. Extensive experiments show that SegPAR significantly outperforms black-box baselines in sparsity efficiency and MIoU reduction, while remaining competitive with white-box sparse attacks. Code is available at \href{this https URL}{this https URL}.

---


### 21. [Benchmarking Cyberattack Detection in Electric Vehicle Charging Infrastructure with Benign User Updates](https://arxiv.org/abs/2608.11286)

**<font color=#1a73e8>作者：</font>** Hannan Chen, Roshni Anna Jacob, Jie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyberattack detection in electric vehicle charging infrastructure is complicated by legitimate post-activation revisions to requested energy and departure time. Charging manipulation attacks can exploit the same interface and variables; therefore, detecting a request change alone does not establish malicious intent. This paper develops a leakage-controlled session-level benchmark that preserves the ordered inputs of real Adaptive Charging Network (ACN) sessions and models legitimate revisions as normal behavior. A fixed pool keeps each generated attack in its source session's split and contains six physically motivated attacks and their coordinated variants. We compare 22 profile-only, transition-aware, and context-stratified model families under common source-grouped folds, attack data, and operating constraints. The proposed Dual-Branch Masked-Autoencoder (Masked-AE) Transition Boost model evaluates whether the current request is normal and whether its producing transition resembles an observed benign update. Its state branch combines masked reconstruction with a radial-basis-function one-class support boundary, while its transition branch combines masked reconstruction with shrinkage covariance distance. Source-grouped five-fold cross-validation selects complete configurations under explicit overall-normal and benign-update acceptance constraints; disjoint normal data then calibrate the final threshold before one test evaluation. The developed dual-branch model provides the strongest robust validation performance while detecting malicious request manipulations without learning to reject legitimate user choices.

---


### 22. [CLEAR: Class-wise Expert Aggregation with Structured Sampling for Long-Tailed Classification](https://arxiv.org/abs/2608.11287)

**<font color=#1a73e8>作者：</font>** Gawon Lim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-tailed classification poses a reliability challenge because models trained on imbalanced data are unevenly reliable across frequent and underrepresented classes. While existing methods address imbalance through re-balancing, adjustment, representation learning, or multi-expert modeling, they rarely estimate which expert should be trusted for each class. This paper proposes CLEAR (Class-wise reLiability-aware Expert Aggregation for long-tailed Recognition), a modular ensemble framework for long-tailed classification. CLEAR generates diverse experts through threshold-based structured sampling while preserving the full label space, then estimates a class-wise trust score for each expert using a smoothed class-wise precision formulation. During inference, expert predictions are combined through class-wise generalized product-of-experts aggregation, allowing different experts to be emphasized for different classes. Experiments on CIFAR-100-LT, ImageNet-LT, and Places-LT across multiple backbones show that CLEAR achieves competitive overall accuracy and particularly strong few-shot performance. These results support class-wise expert reliability as a useful design principle for long-tailed ensemble learning.

---


### 23. [Dueling Deep Q-Learning for Intrusion Detection](https://arxiv.org/abs/2608.11291)

**<font color=#1a73e8>作者：</font>** Logan Luna, Matthew P. Berkowitz, Laxima Niure Kandel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intrusion detection systems (IDS) and automated systems for detecting and reporting cyber threats, are commonly handled via supervised machine learning methods. Though effective, these models struggle to effectively adapt to new attack types. This study proposes a novel approach by employing a reward-based, dueling Q-learning model for IDS, achieving an average accuracy of 99.68% across multiple attack classes. The proposed model has a dueling network architecture which separates its predictions into value and advantage streams. This has the benefit of improving learning efficiency and stability. The model was trained on the CIC-IDS2018, a benchmark dataset based on real-world intrusion detection scenarios, having multiple attack classes such as DDoS, botnets, and brute-force attacks. Furthermore, Explainable AI (XAI), specifically SHAP (SHapley Additive exPlanations), was also integrated into the training and evaluation process to provide interpretability into the model's predictions.

---


### 24. [Battlefield 5G: Dual-PKI and TPM-Based UE Attestation for Tactical 5G Standalone Networks](https://arxiv.org/abs/2608.11293)

**<font color=#1a73e8>作者：</font>** Al Nahian Bin Emran, Rajendra Paudyal, Rajendra Upadhyay 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The standardized 5G Authentication and Key Agreement (5G-AKA) authenticates a subscriber credential stored on a Universal Subscriber Identity Model (USIM) but does not authenticate the physical device that holds that credential or verify its boot state. This gap is significant in tactical 5G deployments, where user equipment may be captured, modified, returned to service, or used with transplanted subscriber credentials. We present Battlefield 5G, a pre-authentication framework for 5G Standalone networks that combines dual X.509 device-certificate checks with Trusted Platform Module (TPM) -based boot attestation before standard registration is accepted. The design places an outer certificate challenge on the 5G base-station called gNB, an independent inner certificate challenge on the Access and Mobility Management Function (AMF) in the 5G core network, and a TPM PCR (Platform Configuration Register) quote verified by an attestation proxy on the 5G core network side. A gNodeB (gNB) side Radio Resource Control (RRC) forwarding gate and an AMF-side save-and-replay mechanism enable multi-round certificate and attestation challenge-response exchanges to be inserted into the registration path without modifying any 3GPP Non-Access Stratum (NAS) message structures or adding new NAS message types. We implement these capabilities by extending the Radio Access Network of the Software Radio System (srsRAN), gNB, User Equipment of the Software Radio System (srsUE) and Open5GS in a B210-based Universal Radio Peripheral (USRP) testbed with a hardware TPM 2.0 in the UE. The prototype blocks SIM-transplant, rogue-certificate, firmware-tampering, and replay attacks. Across six trials, Battlefield 5G increases average onboarding latency from 1886 ms to 2260 ms, adding 373.4 ms of pre-authentication overhead while preserving standard 5G-AKA, security mode, and packet data unit (PDU) session procedures.

---


### 25. [Clinical Feasibility of Low-Magnification Fluorescence Imaging for Breast Cancer Margin Detection Using Texture Analysis and Deep Learning](https://arxiv.org/abs/2608.11317)

**<font color=#1a73e8>作者：</font>** Pouya Afshin, Tianling Niu, Tongtong Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution images of unprocessed surgical breast tissue can be obtained using microscopy with ultraviolet surface excitation (MUSE). This technique is considered a promising method for checking surgical margins during breast cancer surgery. In this study, MUSE images at 4x and 10x magnifications were compared using patch-level classification methods. Texture analysis (TA) based on local binary patterns (LBP) and deep learning (DL) with a base Vision Transformer (ViT) model were used. Both methods achieved similar performance at both magnifications. Using DL method, both 4x and 10x magnifications achieved 96.30% sensitivity, 100% specificity and 98.18% accuracy. Using TA method, 4x achieved better specificity (100% vs 93.33%) and 10x yielded higher sensitivity (100% vs 93.33%), but both had the same accuracy (96.67%). No clear improvement in performance was observed with 10x magnification. These results show that 4x imaging achieves the same diagnostic accuracy as 10x imaging. At the same time, 4x offers a larger field of view and faster image capture. Therefore, lower magnification can be effectively used in MUSE systems for accurate and efficient intraoperative margin assessment.

---


### 26. [Terminal Symmetry as a Decision Resource: Statewise Refinement for Anytime Verified Construction](https://arxiv.org/abs/2608.11318)

**<font color=#1a73e8>作者：</font>** Yi Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many sequential construction tasks exhibit exact symmetry at completion while their execution remains directed and history-dependent. We develop a decision-resource view of terminal symmetry: process evidence supplies directionality, terminal correspondence transports that structure across equivalent outcomes, realized-state evidence refines its current decision relevance after transitions, and a fixed verifier certifies execution. This decomposition yields transport--refine--certify. \method{} instantiates the principle with an episode-fixed transported process structure, its state-restricted process rank, a state-dependent residual rank refreshed after accepted transitions, and an ordinal rank meet whose top-$k$ set is exactly the union of the two proposal prefixes. The meet provides a completion guarantee under prefix coverage and attains the tight worst-case verifier-query bound under the corresponding prefix information model; a two-state construction predicts a strict post-transition dynamic--static separation. Across CAD assembly, Mini-Programs, and exact-fill packing, statewise refresh improves anytime AUC by up to $6.77$, $21.75$, and $8.68$ points, respectively. On 1,135 target-removal episodes from the official GRN OOD scenes, \method{} attains the lowest mean capped verifier cost at all three scales among the compared GRN and CDGS-style planners. The statewise signal also transfers across aggregation and scheduler organizations. Terminal symmetry thereby becomes a reusable decision resource for directed construction.

---


### 27. [Socioduality: A Relational Process Framework for Human-AI Interaction](https://arxiv.org/abs/2608.11322)

**<font color=#1a73e8>作者：</font>** Mehmed Zahid Çögenli  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-AI research often evaluates individual capabilities, combined performance, or final outputs, but these approaches do not preserve how one party's response becomes part of the conditions under which the other party's next contribution is formed. This article introduces socioduality, a sequential, reciprocal, and history-carrying relational process between two distinguishable parties in which a response from one party becomes part of the observable conditions under which the other party's subsequent contribution, judgement, decision, or action is formed. Specified for human-AI dyads, the construct uses nested units: moves, confirmed sociodual episodes, linked pathways, and the broader interaction container. A minimum episode A1-B1-A2 requires evidence of response contingency and return contingency; candidate episodes are classified as confirmed, non-sociodual, or indeterminate before secondary coding of response orientation and substantive contribution re-formation. Three propositions address history-conditioned formation, pathway divergence, and robustness differences among endpoint-equivalent pathways. A frozen operational protocol was calibrated on three previously unseen natural human-AI records through two separately executed model-based evaluator series. Move and candidate reconstruction converged exactly in two cases and differed by one local multimodal unitisation decision in the third; remaining disagreement was concentrated at return-contingency boundaries. Socioduality therefore provides a bounded and empirically tractable process construct for analysing how human and AI contributions are formed through interaction while preserving pathway information that endpoint-centred analysis cannot recover.

---


### 28. [Deployment Decision Reliability: A Generalizability-Theory Framework for Sizing Long-Horizon Agent Evaluations](https://arxiv.org/abs/2608.11323)

**<font color=#1a73e8>作者：</font>** Vasundra Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise practitioners read agent leaderboards as if they ranked agent capability. We show, across three open agent-trace benchmarks (TheAgentCompany, $\tau^2$-bench, and AppWorld), that the agent main effect accounts for less than 3% of total variance in every dataset and check type, while the agent-by-task interaction accounts for 7-23%. Leaderboards rank specialization, not capability. We arrive at this through a four-facet Generalizability Theory variance decomposition, fit with three estimators (Henderson Method-I, REML via lme4, and a Bayesian binomial GLMM) that agree to three decimal places. Four further findings sharpen what the leaderboard is hiding. First, aggregate reliability collapses on the hardest task quartile: $E\rho^2$ on $\tau^2$ action_checks falls from 0.752 to 0.000. Second, training-cell reliability negatively correlates with held-out reliability ($r = -0.90$ on $\tau^2$), meaning the designs that look most reliable replicate worst. Third, population-level diagnostics transfer across enterprise benchmarks (capability-gap ratio stable at 0.35-0.40) but per-family agent rankings invert. Fourth, on the MAST failure taxonomy, trace-level mode profiles are idiosyncratic (MAE = 0.261) while cell-level profiles generalise (MAE = 0.056, $r = 0.83$). We package these into Deployment Decision Reliability (DDR), a one-page reporting discipline that turns the variance-component table into five decisions an enterprise buyer can defend. All code, data loaders, and fit artifacts are released under an open-source license.

---


### 29. [Contextual Quality-Diversity Evolutionary Reinforcement Learning for HVAC Control in Tropical Commercial Buildings](https://arxiv.org/abs/2608.11324)

**<font color=#1a73e8>作者：</font>** Tran Le Vu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a contextual quality-diversity evolutionary reinforcement-learning controller, CQD-ERL, for the supervisory control of a tropical, water-cooled chiller plant and its associated air side. Rather than converging to a single scalarised policy, the controller maintains a product archive of specialised policies indexed jointly by a data- driven operating context, a cluster of daily weather and load regime, and a context-invariant behaviour descriptor, filled by a gradient-free evolutionary operator and a soft-actor-critic policy-gradient operator that share one replay buffer. Every action is filtered through a deterministic safety shield before execution. The controller is trained on a two-tier reduced-order environment representing the latent load, cooling-tower approach and humidity constraints of a Singapore commercial building, and is evaluated over a full annual backtest against an ASHRAE Guideline 36 baseline.

---


### 30. [Dual-Domain Cross-Modal Decoding for Clinical Text-Guided Medical Image Segmentation](https://arxiv.org/abs/2608.11335)

**<font color=#1a73e8>作者：</font>** Md Maklachur Rahman, Tracy Hammond  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical text can narrow down what to segment, but recent text-guided designs emphasize spatial alignment while overlooking frequency content that governs texture and boundaries. We propose Dual-Domain Cross-Modal Decoding (DD-CMD) for clinical text-guided pulmonary infection segmentation, integrating two complementary forms of language guidance during decoding. In the spatial domain, Text-Guided Spatial Cross-Attention (TGSA) aligns multi-scale visual tokens with text semantics and updates features through gated residual fusion. In the frequency domain, Spectral-Text Adaptive Modulation (STAM) applies a 2D DCT to compute learnable band-energy statistics and predicts text-conditioned FiLM parameters to recalibrate decoder channels for frequency-aware decoding. DD-CMD embeds TGSA and STAM into a coarse-to-fine decoder (7x7 to 56x56) and restores full-resolution masks using a lightweight two-stage refinement module. Experiments on QaTa-COV19 and MosMedData+ show that DD-CMD achieves 91.46% Dice / 84.26% mIoU and 81.95% Dice / 69.42% mIoU, respectively, with average gains of +1.96 Dice and +2.67 mIoU over the strongest prior baselines. Code: this https URL.

---


### 31. [Association-based Privacy Attacks in Wireless Protocols: Formal Modeling and Mitigation](https://arxiv.org/abs/2608.11337)

**<font color=#1a73e8>作者：</font>** Mohit Kumar Jangid, Felix Engelmann, Zhiqiang Lin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the surge in privacy-sensitive data from sources such as social media and IoT devices, there is a pressing need for formal, automated methods to assess privacy risks within these intricate systems. This paper formally investigates root sources of pairing-based privacy threats exploited using replay/relay techniques in wireless communication. Our research harnesses condition-oblivious responses, replay-resistance, and distance bounding measures vital for protocols utilizing shared keys in allowlists for authenticated reconnections. Particularly, the paper uses formal modeling of notable wireless networks, like the Wi-Fi P2P persistent group formation and the Bluetooth Low Energy reconnection procedure, to illustrate the root causes and countermeasures. Our model rigorously validates the proposed solution against association inference attacks, along with existing formalizations of well-authentication, frame opacity, and no-desynchronization. The ensuing analysis reveals not only uncharted privacy realms in wireless communication but also identifies old and new vulnerabilities. Our proposed design changes are acknowledged by Wi-Fi Alliance and Bluetooth SIG, paving the way for future advancements in resilient, privacy-preserving wireless protocols.

---


### 32. [Dynamics Models for Offline Hyperparameter Selection in Real-World RL](https://arxiv.org/abs/2608.11349)

**<font color=#1a73e8>作者：</font>** Jordan Coblin, Han Wang, Martha White 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A key obstacle to deploying reinforcement learning in real-world systems is hyperparameter selection, particularly when simulators are unavailable and online experimentation is costly. Prior work has proposed calibration models trained on offline data to approximate environment dynamics and enable offline hyperparameter selection, but these methods have so far been evaluated only in simple simulated settings. In this paper, we present the first application of calibration models in a real-world industrial setting: a municipal water treatment plant. We evaluate several calibration model approaches, including a k-nearest neighbors model with a Laplacian distance metric, on high-dimensional, non-stationary sensor data for nexting prediction tasks. Our results show that these models can generate realistic long-horizon rollouts and recover meaningful hyperparameter sensitivity trends. We further examine how calibration models scale to year-long datasets, how they support the selection of fine-tuning learning rates for pre-trained agents, and how robust they are under distribution shift. Overall, our findings provide a proof of concept for using offline dynamics models to support RL deployment in real-world environments, while highlighting important practical challenges for future work.

---


### 33. [ODE-Based Transformer Decoders for Iterative Sign Language Translation](https://arxiv.org/abs/2608.11352)

**<font color=#1a73e8>作者：</font>** Tuğçe Kızıltepe, Hacer Yalim Keles  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign language translation has achieved strong results with Transformer architectures, yet recent improvements largely rely on scaling model capacity at the cost of increased computation. We propose a parameter-efficient alternative that improves expressiveness without increasing model size. Rather than scaling capacity, we focus on enhancing the update dynamics of iterative refinement decoders, where each refinement step corresponds to one internal decoder iteration that progressively improves the latent representation before translation generation. We reinterpret residual refinement updates from an Ordinary Differential Equation (ODE) perspective and replace them with higher-order numerical integration schemes, namely Runge--Kutta methods (RK-2 and RK-4). These methods perform multiple function evaluations within each refinement step to produce more accurate and stable representation updates without adding decoder parameters. To the best of our knowledge, this is the first application of ODE-inspired update dynamics to sign language translation. RK-2 achieves 22.96 BLEU-4 on the PHOENIX-2014-T test set and 19.34 BLEU-4 on the CSL-Daily test set, outperforming the IPSLT baseline on both benchmarks, with fewer decoder layers and refinement iterations on CSL-Daily. These results suggest that stronger refinement dynamics can improve translation performance under parameter-efficient decoder designs, providing a complementary alternative to conventional model scaling.

---


### 34. [When Do Institutions Beat Intelligence?](https://arxiv.org/abs/2608.11357)

**<font color=#1a73e8>作者：</font>** Zhengye Han  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> More capable agents do not necessarily form a more capable collective. A multi-agent system may jointly possess sufficient information yet fail because evidence is poorly routed, unreliable reports enter public belief, correlated claims masquerade as independent support, shared state becomes stale or strategically distorted, or useful evidence is exposed through an ineffective action interface. We ask when additional resources should improve the reasoner and when they should instead change the institutional structure through which the collective forms and acts on public information. Drawing on functional distinctions from research on group decision making and distributed cognition, we construct controlled artificial ecologies around four loci of collective failure: access and routing, admission and dependence, state maintenance and incentives, and representation and action. Across these ecologies, we separately vary model capability and institutional structure, pairing positive interventions with matched reasoning baselines and mechanism-breaking controls. The experiments reveal a consistent boundary: institutions help when they repair failures in how a collective constructs usable public state, but lose their advantage when their signals are uninformative or uncheckable, when stronger intelligence can perform the same transformation directly, or when the resulting state cannot support reliable action. Our results recast the choice between intelligence and institutions as a diagnosis of where collective reasoning fails.

---


### 35. [QUARTZ: Qualitative Understanding via Accessible Representation and Visualization](https://arxiv.org/abs/2608.11364)

**<font color=#1a73e8>作者：</font>** Omar Khan, JooYoung Seo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Qualitative data visualizations -- concept maps, network graphs, Sankey diagrams, and coding stripes -- are integral to research practice, yet remain entirely inaccessible to blind and low-vision (BLV) researchers. While visualization has seen advanced multimodal solutions for quantitative charts, qualitative visualizations, and their non-linear, semantically rich structures have received no attention. We present QUARTZ, a web-based system that provides screen-reader-accessible, multimodal representations of qualitative data visualizations. Using the Rapid Iterative Testing and Evaluation (RITE) method, we conducted a user study with 8 BLV participants who completed 12 tasks across four visualization types. Our findings expose accessibility barriers unique to qualitative visualizations -- non-linear navigation breakdowns and semantic comprehension gaps absent from quantitative chart research---and document how iterative co-design with BLV users resolved them. We contribute empirical evidence and design guidelines for an underexplored visualization domain, advancing the infrastructure BLV researchers need to participate independently in qualitative inquiry.

---


### 36. [Gaze Target Estimation Anywhere with Concepts](https://arxiv.org/abs/2608.11367)

**<font color=#1a73e8>作者：</font>** Xu Cao, Houze Yang, Vipin Gunda 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating human gaze targets from images in-the-wild is an important and formidable task. Existing approaches primarily employ brittle, multi-stage pipelines that require explicit inputs, like head bounding boxes and human pose, in order to identify the subject of gaze analysis. As a result, detection errors can cascade and lead to failure. Moreover, these prior works lack the flexibility of specifying the gaze analysis task via natural language prompting, an approach which has been shown to have significant benefits in convenience and scalability for other image analysis tasks. To overcome these limitations, we introduce the Promptable Gaze Target Estimation (PGE) task, a new end-to-end, concept-driven paradigm for gaze analysis. PGE conditions gaze prediction on flexible user text or visual prompts (e.g., "the boy in the red shirt" or "person in point [0.52, 0.48]") to identify a specific subject for gaze analysis. This approach integrates subject localization with gaze estimation, and eliminates the rigid dependency on intermediate analysis stages. We develop a scalable data engine to generate Gaze-Co (Gaze Estimation with Concepts), a dataset and benchmark of 120K high-quality, prompt-annotated image pairs. We also propose GazeAnywhere, the first model designed for PGE. GazeAnywhere uses a transformer-based detector to fuse features from frozen encoders and simultaneously solves subject localization, in/out-of-frame presence, and gaze target heatmap estimation. GazeAnywhere achieves state-of-the-art performance on multiple PGE benchmarks, setting a strong baseline for this new problem even on a difficult out-of-domain, real-world clinical dataset. GazeAnywhere is open-sourced in this http URL.

---


### 37. [Towards an approach to multivariate outlier detection for District Heating System data](https://arxiv.org/abs/2608.11375)

**<font color=#1a73e8>作者：</font>** Rajko Turudija, Dušan Stojiljković, Milan Zdravković 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we test different methods for multivariate detection of outliers in the data of transmitted heat energy in the selected substation of local District Heating System, by also considering outside ambient temperature, namely Z-score (univariate, as a benchmark), Mahalanobis distances, Principal Component Analysis (PCA), Isolation Forest and Hotelling's T-squared test. The overall research aims at uncovering irregular plant operation, with a wider objective of identifying the opportunities for reducing the consumption of gas in central heating plants as well as the CO2 emission. The proposed approach considers specific domain circumstances, such as irrelevance of zero transmit-ted energy timepoints as indication of off-grid plant. The outcomes of the different methods are discussed with domain experts. It was concluded that PCA, Isolation Forest and Hotelling method provide relevant results. Finally, we adopt the ensemble method (selection based on the agreement of all three methods on the detected outliers) as the final approach.

---


### 38. [Reoptimization Algorithms for Contextual Bandits with Knapsack Constraints](https://arxiv.org/abs/2608.11383)

**<font color=#1a73e8>作者：</font>** Zhen Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study new algorithms for Contextual Bandits with Knapsack. In these problems, there are finitely many types of customers, products, and resources. Each product is made from a fixed combination of resources, and resources have finite capacity. A decision maker must assign each arriving customer one out of a set of multiple possible products. Every assignment of a customer to a product will generate a random reward, which equals an unknown linear function of customer and product features, plus a noise term. The objective is to jointly learn the mean reward function, and to make online assignments to minimize the expected revenue loss relative to an optimal policy that knows the reward function. We propose a natural and simple extension of the Upper-Confidence-Bound (UCB) family of algorithms and apply re-optimization techniques. We show that by taking advantage of re-optimization, our algorithm achieves an average regret of $O(\frac{(\ln T)^3}{T})$ where $T$ is the horizon length. Our bound significantly reduces the $O(\frac{1}{\sqrt{T}})$ bound in the literature for closely related dynamic-pricing problems that are based on re-optimization.

---


### 39. [Mechanism Design for Generative Engines: From Exploitation toward Win-Win Outcomes](https://arxiv.org/abs/2608.11390)

**<font color=#1a73e8>作者：</font>** Chen Xu, Zitian Guo, Chenyan Xiong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative engines are reshaping the web ecosystem by making citations a key mechanism for allocating attention, attribution, and downstream value. This creates a strategic tension: content providers are incentivized to optimize for model citation, while platforms must preserve answer quality and trustworthy attribution. We show that this tension can escalate into citation wars. In repeated simulations, state-of-the-art generative engine optimization (GEO) attacks adapt to conventional defenses by producing citation-seeking rewrites that degrade document quality and introduce unsupported claims. To study this problem, we formulate the supplier--platform interaction as a repeated Stackelberg game with partial monitoring. A local best-response analysis identifies when citation competition approaches an inert stationary outcome. Motivated by this finding, we propose a platform--creator mechanism called VCR based on verifiable-content rewards. Rather than only penalizing suspicious rewrites, the platform also credits rewrites that surface checkable factual substance, aligning creator incentives with answer trustworthiness. Experiments on three benchmarks show that VCR consistently achieves the largest Net defense-utility score, outperforming the strongest baseline by an average of 12.1 percentage points, and produces a win--win outcome under our empirical equivalence criterion.

---


### 40. ["I Don't Want My Mental Health App To Give Me Mental Health Barriers": Unpacking The Need For Digital Mental Health Tracking Services With And For The Blind Community](https://arxiv.org/abs/2608.11391)

**<font color=#1a73e8>作者：</font>** Omar Khan, JooYoung Seo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital mental health (DMH) tracking services promise continuous, personalized support for well-being, but their design often assumes sighted users. For the blind community, this assumption produces a distinct pattern of exclusion: services whose accessibility cannot be evaluated without first paying for them, community features that exclude the users they purport to support, and interfaces that leave users digitally literate but functionally blocked. We report on an explanatory sequential mixed-methods study of blind users' experiences with DMH tracking services in the United States. In the first phase, 93 legally blind adults completed a survey about their usage patterns, adoption decisions, and data-agency preferences; in the second, 10 survey respondents participated in semi-structured interviews. We analyzed closed-ended responses using descriptive statistics and the Kruskal-Wallis test, and open-ended and interview data using inductive thematic analysis, interpreting findings through Norman and Skinner's eHealth Literacy framework. Participants identified mindfulness, sleep, and goal-tracking services as their most-used categories, but also described recurring exclusion from the community-support features that other users value most. We argue that the framework's "computer literacy" dimension is insufficient on its own: many of our participants possessed the literacy but were blocked from applying it by design choices that predate the user. We contribute design recommendations for transparent pre-purchase accessibility evaluation, accessibility-native rather than retrofitted interfaces, and user-controlled data agency -- recommendations intended not to accommodate blind users but to design DMH tracking services with them from the start.

---


### 41. [The Role of Variability in Human-Machine Interaction Experience](https://arxiv.org/abs/2608.11401)

**<font color=#1a73e8>作者：</font>** Sean Kille, Jan Lars Hagemann, Anne Voormann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-machine interaction (HMI) requires control strategies that account for the nature of human motor behavior. Conventional shared-control and haptic-assistance methods typically ignore the stochastic nature of human behavior, potentially limiting both performance and human interaction experience. In this study, we designed an experimental setting and evaluated a novel human-variability-aware optimal controller. Participants performed a physically coupled haptic interaction task in three conditions: a controller mode that aims at conventionally reducing overall variability, a variability-aware controller mode designed to maintain human natural variability patterns, and a human-only control condition serving as a baseline. We analyzed behavioral variability, task performance, and human interaction experience. The results show that considering natural movement variability significantly increased perceived interaction quality in terms of usability while maintaining task performance. These findings highlight the importance of incorporating stochastic human movement characteristics into shared-control designs and demonstrate the feasibility and benefits of the proposed control strategy for human-centered control design of HMI.

---


### 42. [Unmasking Toxic Mimicry in Medical Offline Reinforcement Learning for ICU Sepsis Management via Counterfactual Clinical Audits](https://arxiv.org/abs/2608.11410)

**<font color=#1a73e8>作者：</font>** Hangqi Ren, Junyi Liao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) offers considerable promise for optimizing ICU treatment decisions, yet standard evaluation metrics Mean Squared Error (MSE) and Fitted Q-Evaluation (FQE) assess only behavioral imitation and cannot detect Toxic Mimicry, a failure mode in which agents replicate harmful patterns such as treatment withdrawal during comfort-care transitions. Using the MIMIC-III database, we propose the Counterfactual Clinical Audit (CCA) framework, which stress-tests RL agents through physiological perturbations anchored in Surviving Sepsis Campaign (SSC) guidelines. We audit a Medical Decision Transformer (MedDT) and a Historical Causal Transformer (HCT-RL), the latter employing Causal Action Shielding, propensity-based importance weighting, and Conservative Q-Learning. CCA reveals that MedDT paradoxically reduces vasopressor dosage as lactate escalates, contradicting resuscitation guidelines, while HCT-RL maintains physiologically consistent responses. These findings expose a systemic misalignment between statistical fit and clinical safety, supporting counterfactual audits as a necessary evaluation standard for medical RL.

---


### 43. [A Study of Kernel Telemetry Options for Security-Oriented Provenance](https://arxiv.org/abs/2608.11418)

**<font color=#1a73e8>作者：</font>** Paul R. B. Houssel, Olivier Levillain, Sylvie Laniepce 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Provenance aims to capture the origins, transformations, and interactions of system objects for security and forensic applications. Existing provenance capture approaches still face major challenges and are not yet ready for production environments. In this paper, we first analyze the main kernel telemetry capture approaches, identifying eBPF as the most promising, and complement this analysis with micro benchmarks to assess its performance overhead and the filtering mechanisms used to achieve capture granularity, such as restricting capture to individual containers. Building on this foundation, we then classify, according to the studied capture approaches and filtering methods, eight provenance systems and five capture agents that could serve as their capture layers, collectively referred to as tools. Our study reveals that these tools are built on highly heterogeneous capture layers, most of which cannot guarantee the integrity and availability of the captured events, completely failing to meet the requirements of security-oriented use cases.

---


### 44. [Diffusion-Based Data-Driven Assortment Optimization](https://arxiv.org/abs/2608.11419)

**<font color=#1a73e8>作者：</font>** Junyi Liao, Xiaohui Jiang, Zhengwei Tong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Assortment optimization is a fundamental problem in revenue management, typically addressed using parametric choice models such as the multinomial logit (MNL) and its variants. While these models enable tractable formulations, their performance is sensitive to model misspecification and often struggles to capture complex customer behavior. In this paper, we propose a model-agnostic framework for assortment optimization based on guided discrete diffusion. We represent assortments as binary vectors and perform stochastic search via a learned reverse diffusion process, avoiding explicit combinatorial enumeration. To incorporate decision objectives, we introduce a reward-guided mechanism that biases local transitions using estimates of expected revenue. This allows the method to effectively balance exploration and exploitation during generation. Empirically, we show that the proposed approach consistently identifies high-quality assortments and remains robust under model misspecification, often recovering near-optimal solutions in high-dimensional settings. Moreover, the generative nature of diffusion enables the production of diverse high-performing assortments, offering flexibility beyond a single deterministic solution. These results highlight the potential of generative modeling as a scalable and robust paradigm for combinatorial optimization in data-driven decision-making.

---


### 45. [COGENT: Counterfactual Gaussian Explanations for Volumetric Medical Images](https://arxiv.org/abs/2608.11422)

**<font color=#1a73e8>作者：</font>** Dorian Rząsa, Bartosz Zabdyr, Krzysztof Piekarz 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explainability is essential for deploying deep learning models in high-stakes medical applications. Existing explainability methods for volumetric imaging predominantly operate in voxel space, overlooking the structured representations introduced by recent advances in 3D scene modeling. We present COGENT (Counterfactual Gaussian Explanations), a framework that generates counterfactual explanations directly in the parameter space of Gaussian-based volumetric representations. Built upon MedGS and the Sybil lung cancer risk prediction model, COGENT optimizes selected Gaussian primitives through a differentiable rendering pipeline, enabling gradients from the downstream predictor to identify representation components that most influence model decisions. Unlike conventional pixel- or voxel-level attribution methods, our approach formulates explainability as a counterfactual optimization problem over an explicit 3D scene representation, producing sparse and spatially localized explanations while preserving anatomical consistency. We evaluate COGENT on lung CT scans using quantitative comparisons with existing explainability methods together with qualitative analysis by medical experts. The results demonstrate that representation-space counterfactual optimization provides clinically meaningful explanations while offering a new perspective on interpreting volumetric deep learning models.

---


### 46. [Analysis of Federated Aggregation under Model Poisoning and Backdoor Attacks: A Reconstructed Cross-Dataset and Cross-Architecture Benchmark](https://arxiv.org/abs/2608.11423)

**<font color=#1a73e8>作者：</font>** Soumya Mazumdar, Vineet Kumar Rakesh, Tapas Samanta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust comparisons of federated aggregation methods require joint consideration of predictive performance, threat definitions, metric semantics, and execution provenance. A 500-cell seed-1 evaluation matrix was reconstructed across five aggregation methods, five datasets, five architectures, and four recorded conditions: clean, sign-flipping, Gaussian, and BadNets. Successful execution logs were identified for 454 original runs and 36 repaired or rerun executions, whereas 10 clean SVHN cells were supported by summary-only provenance. Trimmed Mean achieved the highest clean macro-mean accuracy (76.02%) and the lowest mean within-task rank (1.70). Krum attained the highest recorded accuracy under both sign-flipping and Gaussian configurations. These relative rankings remained unchanged when analysis was restricted to 21 task pairs for which original successful logs were available for every method-condition combination. Audit of the supplied BadNets metric implementation established that every test input is triggered prior to target-label counting; consequently, the retained metric represents Triggered Target-Label Rate (TTLR) rather than a conventional target-excluding attack success rate. An audit of the supplied FedPARETO scaffold further identified a pathway in which predictive summaries may characterize an uncorrupted local model while the aggregation weight is applied to a separately corrupted update, introducing a potential discrepancy between reported predictive outcomes and the updates used for aggregation. The canonical matrix contains a single identified seed for each cell, and exact attack and configuration lineage is incomplete. Accordingly, the findings should be interpreted as descriptive comparisons within the recorded configurations and not as statistical estimates or universal claims regarding robustness.

---


### 47. [Three Tokens Force Exponential Feature Rank in Nonnegative Kernel Attention](https://arxiv.org/abs/2608.11427)

**<font color=#1a73e8>作者：</font>** Vicente Opazo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full attention exposes every token pair, whereas kernel attention compresses a sequence into a fixed-dimensional sketch. We show that this distinction becomes exponential at the first context length containing two competing candidates. On Min-IP over Boolean inputs, rank-one normalized kernel attention solves every sequence of length at most two exactly. In contrast, any single normalized nonnegative kernel-attention head that succeeds on all three-token sequences with error strictly below $1/2$ requires $2^{\Omega(m)}$ features, even with arbitrary finite-dimensional tokenwise values and an arbitrary query-dependent affine readout. Dense softmax solves the same task with $m$-dimensional scores and constant temperature. The conclusion survives position-dependent token maps and a causal final query. As context length grows, the lower bound approaches the exact $2^m$-feature realization. Separately, for deterministic multihead, multilayer sketch models whose cross-token channels have finite alphabets, we prove a transcript lower bound linear in the number of independent answers and logarithmic in their alphabet size.

---


### 48. [AutoGrable: What Is a Good Graph for a Table?](https://arxiv.org/abs/2608.11431)

**<font color=#1a73e8>作者：</font>** Tamara Cucumides, Floris Geerts  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph learning presupposes a graph, and tables and relational databases do not come with one. Applying a GNN to them requires deciding which entities become nodes, which of them to connect, and through which relations---a decision made by hand, by schema heuristics, or by training a model on every candidate graph and keeping the best. We give a criterion that requires no trained graph model. In the minimal table-to-graph abstraction each row is a node, so a message-passing GNN, bounded by 1-WL, sees a construction only as a partition of the rows into colour-refinement classes: a construction is good for a task when that partition separates rows with different labels and does not split rows that share one. AutoGrable turns this criterion into a construction procedure. For incidence constructions the partition is fixed by the selected columns, so building a graph reduces to choosing them, and we score a candidate subset by a label-alignment risk: the held-out risk of the best predictor constant on its blocks, penalised by an occupancy term measuring how thinly the blocks are populated. The score materialises no graph and trains no GNN, so AutoGrable can search the space of subsets greedily and cheaply, and returns the resulting grable for single tables and for foreign-key schemas alike. Our experiments show that over a space of candidate graphs the score discards a large fraction while retaining the best; that AutoGrable recovers the columns that generate the label on controlled tasks and outperforms fixed, random, and task-aware constructors on real tasks under a fixed predictor; and that it is the only method compared that can decline to build a graph when none helps.

---


### 49. [Stigma and Support in Online Sexual Violence Narratives on Reddit](https://arxiv.org/abs/2608.11433)

**<font color=#1a73e8>作者：</font>** Shirlene Rose Bandela, Karan Bindal, Vaibhav Garg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online communities increasingly provide spaces where survivors of sexual violence can share their experiences and seek support. Although prior research has examined stigma and social support separately, less is known about how stigma expressed in survivor narratives relates to the support offered in response. We introduce the SCOPE dataset, linking stigma signals in online survivor narratives to support types in corresponding comment threads. We annotate posts using a multi-dimensional stigma taxonomy, including Experienced, Internalized, Anticipated, and Structural Stigma, and comments using a support taxonomy encompassing Information Support, Emotional Support, Esteem Support, Tangible Assistance, and Group Interaction. Using contextual, linguistic, and emotion analyses, we compare Stigma and No Stigma content and find that Stigma narratives place greater emphasis on internalized distress, whereas No Stigma narratives focus more on interpreting situations and experiences. Internalized Stigma is the most prevalent category, and community responses remain broadly stable across stigma types, with Information and Esteem Support appearing most often. These findings show how stigma shapes survivor narratives and peer responses and have implications for computational modeling, content moderation, and safer online systems.

---


### 50. [Variational Parameter Calibration with Physics-Aware Latent-Space Surrogates](https://arxiv.org/abs/2608.11435)

**<font color=#1a73e8>作者：</font>** Qiyao Zhou, Xujia Zhu, Pierre Joli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forward and inverse modeling of parametric dynamical systems requires surrogate models that are not only accurate for state prediction, but also informative for parameter calibration. However, a systematic end-to-end differentiable formulation for coupling deep-learning-based reduced-order surrogates with variational parameter estimation remains underdeveloped. In this work, we introduce a physics-aware neural-network-based latent-space framework for reduced-order forward modeling and variational parameter estimation. The proposed autoencoder-based approach yields a differentiable surrogate that maps physical parameters to predicted flow fields through a latent representation. The observable supervision is used during offline training to encourage the latent variables to retain information correlated with system parameters, while the online inverse problem is solved in the parameter space through the surrogate-induced observation operator. The method is evaluated on two computational-fluid-dynamics benchmarks. The results show that reconstruction accuracy alone is insufficient for inverse modeling, owing to the lack of end-to-end differentiability or physics awareness for variational parameter calibration. Quantitative latent-space analysis further shows that observable supervision improves case-level separability and temporal organization of latent representations. Experiments with realistic measurement settings, including noisy, low-resolution, randomly masked, and block-wise partial observations, demonstrate the robustness of the proposed framework and show that it generally reduces calibration error and variability compared with the standard surrogate models.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
