# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**751-800**（第 16/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | **751-800** | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 751. [Automated feature engineering, AutoML, and decision-focused learning for improved energy consumption forecasting](https://arxiv.org/abs/2609.35013)

**<font color=#1a73e8>作者：</font>** Nasser Alkhulaifi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rising cost and demand for energy, together with environmental sustainability goals, create major challenges for energy management. Energy Consumption Forecasting (ECF) supports planning by predicting future consumption, but Machine Learning (ML) models for ECF often depend on expert-driven Feature Engineering (FE). This thesis addresses that dependence through three contributions. First, it establishes and evaluates a comprehensive FE pipeline for ECF and investigates domain-specific features. Second, it introduces AutoEnergy, a domain-tailored automated FE algorithm that generates interpretable features from timestamps and lagged consumption and integrates with AutoML for end-to-end ECF modelling. Across eighteen real-world energy datasets spanning residential, commercial, industrial, renewable, and grid domains, AutoEnergy reduces forecasting error by 19.52%-84.72% relative to baseline AutoML and established automated FE methods, while running 1.31-4.41 times faster, with gains varying by dataset. Third, AutoEnergy is integrated with Decision-Focused Learning (DFL) for a Battery Energy Storage System problem, jointly forecasting electricity prices and demand while optimising charging and discharging decisions. On a real-world UK property dataset, this approach reduces operating costs by 22.9%-56.5% compared with the same DFL models without automated FE. Overall, the results show that domain-specific automated FE can reduce reliance on manual feature design, improve forecasting accuracy, and translate predictive gains into measurable operational benefits in energy management.

---


### 752. [Environmental requirements for the use of social information by artificial life agents using evolved plastic artificial neural networks](https://arxiv.org/abs/2609.35018)

**<font color=#1a73e8>作者：</font>** Hugh Charterton, James M. Borg, Aniko Ekart  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evolved Plastic Artificial Neural Networks (EPANNs) consist of two principal processes, the first, evolution, and the second, development and in-life learning. In the context of the origins of social = learning, very few studies have been carried out using ALIFE models based on EPANN requirements. Studies in this field have usually involved an imitative teacher/pupil relationship. This, however, ignores the possibility that the observed behaviour is a consequence of social information cues rather than direct imitation or teaching. Starting with the first of the EPANN processes (evolution), a series of experiments was undertaken using artificial neural network (ANN) based agents in a variety of foraging environments to examine under what minimal environmental conditions the use of social information might have evolved, as measured by the number of generations taken to meet a specified fitness criterion. NEAT (Neuroevolution of Augmenting Topologies) was the ANN used as its evolutionary algorithm would evolve a network's topology as well its weights. Unintentionally, in the experiment there was a simple network topology based on the location of the nearest food item which enabled agents to swiftly meet the fitness criterion. With this topology, additional information, social or otherwise, was not required and could have proved to be a hindrance. However, this does indicate that for the use of social information to have evolved, it would require a greater degree of complexity in the environment to do so.

---


### 753. [Verifying the Linear Representation Hypothesis: How Interpretable Are Vision SAEs?](https://arxiv.org/abs/2609.35020)

**<font color=#1a73e8>作者：</font>** Teodor Chiaburu, Franz Motzkus, Frank Haußer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Sparse Autoencoders (SAEs) have become a popular tool in Mechanistic Interpretability due to their presumed ability to disentangle complex features learned by a model into monosemantic concepts. Despite their growing popularity, evaluating their interpretability remains an active topic of research. The bedrock motivating the adoption of SAEs is the Linear Representation Hypothesis (LRH), which claims that polysemantic features can be projected onto a (near) orthogonal basis of sparse, human-understandable representations. Yet, most current frameworks evaluate proxies such as the sparsity of SAE features or the coherence of the inferred dictionary, implicitly assuming that these reflect alignment with human perception. In this paper, we provide empirical evidence that measuring the interpretability of SAE concepts is more difficult than these proxies suggest. To this end, we adapt the Autointerpretability Score (AIS) - previously shown to align with human judgments in Natural Language Processing - to vision tasks and validate our approach in a dedicated user study. We evaluate SAE concept quality using both standard metrics and our adapted AIS. We find that established interpretability metrics for SAEs correlate neither with one another nor with AIS, indicating that no single reference-free metric, whether grounded in the LRH or not, is sufficient for verifying the interpretability of vision SAEs. We argue these findings support recent calls for more verifiable, ground-truth-anchored design and evaluation of explanation methods.

---


### 754. [Addressing Spatial Indistinguishability in Spatiotemporal Prediction via Optimal Transport-Guided Masking](https://arxiv.org/abs/2609.35021)

**<font color=#1a73e8>作者：</font>** Guangyu Wang, Jiawei Tong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal prediction aims to learn discriminative representations from correlated temporal signals over spatial structures for accurate future inference. A central challenge is \emph{spatial indistinguishability}: different nodes may share similar historical patterns yet evolve toward divergent futures, severely degrading forecasting performance in real-world sensor networks. Existing embedding-based and graph neural network (GNN)-based approaches can partially detect such ambiguous nodes but rely on historical similarity, struggling to capture \emph{future behavioral divergence}. We propose \textbf{STOT} (\textbf{S}patio\textbf{T}emporal \textbf{O}ptimal \textbf{T}ransport), a self-supervised framework that resolves spatiotemporal ambiguity via structured masking guided by optimal transport. Our key idea treats indistinguishability as a \emph{disambiguation} problem: future states are inferred by exploiting concurrent spatial correlations and their time-varying similarity. We design a similarity-aware metric for dynamic inter-node relationships and an optimal transport-based masking strategy to emphasize ambiguous positions during pre-training. A batch consistency constraint preserves semantic coherence, while a random-walk masking mechanism promotes structured context exploration. Experiments on six real-world datasets show that STOT performs competitively with state-of-the-art baselines on the evaluated benchmarks and improved interpretability through transport-plan visualizations.

---


### 755. [Detection of Adversarial Attacks on Super-Resolvers Using Spectral Features](https://arxiv.org/abs/2609.35022)

**<font color=#1a73e8>作者：</font>** Emma J. Reid, Haley Duba-Sullivan, Tony G. Allen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The integration of deep learning models into image preprocessing pipelines such as super-resolution introduces a largely unexplored attack vector for adversaries targeting downstream tasks. To ensure trustworthiness of critical imaging pipelines, we must be able to detect adversarial behavior within preprocessing models. In this paper, we propose a spectral-based detection method for identifying adversarial attacks embedded in super-resolution model weights. More specifically, we use the radially-averaged power spectral density as a discriminative feature to train an extreme gradient boosting (XGBoost) detector, demonstrating detectability of model-level threats in super-resolution networks. We further benchmark our detector against magnitude- and phase-based Fourier spectrum detectors, evaluating each method across a range of training and cross-architecture scenarios. Our proposed detector out-performs the comparison detectors in most of these scenarios and indicates that high-frequency features are most informative for detecting AdvSR attacks across SR architectures.

---


### 756. [WebPageBench: Event-Level Verification and Controlled UI-Variant Generation for Web Agents](https://arxiv.org/abs/2609.35026)

**<font color=#1a73e8>作者：</font>** Anton Emelyanov, Maria Tikhonova, Zaven Martirosian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present WebPageBench, an open framework for evaluating web agents in which every task is verified from the interface's own event log. Six instrumented mock sites with brand identifiers removed (a marketplace, a bookstore, a grocery service, rail ticketing, hotel search and a document cabinet) emit typed events with parameters as a user or an agent acts. A task declares the events it requires, and success is decided by matching them, with no judge model and no scraping of rendered pages. The same instrumentation supports controlled UI variation: one configuration switch re-renders a task through a different implementation of a single control while the prompt and the success conditions stay completely identical, so sensitivity to interface form can be measured under a fixed task specification. The WebPageBench release consists of three components: 152 tasks, divided into 65 canonical scenarios and 87 control variants across light/dark UI-modes; a common runner evaluated with six browser/DOM harness configurations and five screenshot-only GUI-agent families; and a public leaderboard of 24 model-harness pairs. On the public 152-task leaderboard the gap between what agents declare finished and what the log confirms reaches 41 points (one configuration declares every task finished and satisfies the conditions on 59%).

---


### 757. [Fast Learning Rate Transfer in Shallow Linear Networks at Growing Training Horizons](https://arxiv.org/abs/2609.35029)

**<font color=#1a73e8>作者：</font>** Mana Sakai, Masaaki Imaizumi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperparameter transfer across model width can substantially reduce the cost of tuning large neural networks, but its behavior when the training horizon grows with width is not fully understood. Building on the framework of fast hyperparameter transfer (Ghosh et al., 2026), which formalizes when transfer is effective, we investigate conditions that ensure fast transfer in the growing-horizon regime. Specifically, we study learning-rate transfer in a shallow linear network with a single trainable hidden matrix, trained by full-batch gradient descent. Under additional spectral assumptions, our main results are threefold. (i) We prove fast learning-rate transfer as $n,T\to\infty$ whenever $T=o(\sqrt{n})$. (ii) We characterize the transfer rates through the finite-width perturbation scale, the first-order sensitivities of the loss and its learning-rate derivative to finite-width perturbations, and the local loss curvature. (iii) We derive limiting distributions for the optimal learning rate and optimized loss, governed by fluctuations associated with the extreme eigenvalues of the data Gram matrix. These results clarify how spectral structure and local loss sensitivities govern learning-rate transfer at growing horizons.

---


### 758. [GAZEleak: Passcode Inference Against Eye-tracking XR Devices Through External Observation](https://arxiv.org/abs/2609.35040)

**<font color=#1a73e8>作者：</font>** Hwanjo Heo, Junhee Lee, Jinwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mixed-reality headsets such as Apple Vision Pro replace the touch screen with gaze-as-pointer interaction: the wearer looks at a target and confirms with an air pinch. Because the display is inside the headset and the eye tracker is walled off from third-party software, such input is widely assumed to be unobservable to bystanders---a built-in defense against the shoulder-surfing that plagues phones and laptops. We present GAZEleak, a side-channel attack that recovers gaze-driven input from external video of head motion alone, under a strictly local, physical-observer threat model: the adversary only films the wearer from across the room and installs no software on the device. The attack exploits the centrally coupled eye-head motor program: gaze shifts recruit small, target-dependent head reorientations that project into sub-degree pose changes recoverable from commodity video. GAZEleak implements a measurement-based, sparse-optical-flow inference pipeline for users' 6-digit device passcodes. On a preliminary front-view dataset from three author-subjects who were aware of the attack hypothesis, GAZEleak places the true code within the top ten guesses for 56% (10 of 18) of test codes under a cross-person protocol with no labeled victim data, and for every code of the most exposed subject. The performance is subject-dependent: no passcode from the least exposed subject reaches the top ten, although its median guessed passcode rank is 12,786 rather than 500,000 expected from an uninformative ordering. These results provide preliminary evidence that gaze-coupled head motion can expose passcode information under controlled conditions, while motivating broader evaluation across users, behaviors, and capture settings.

---


### 759. [Mixed-Prior Decision Risk for Open-Set Recognition](https://arxiv.org/abs/2609.35043)

**<font color=#1a73e8>作者：</font>** L. A. Erlygin, P. D. Proskura, A. A. Zaytsev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In open-set recognition (OSR), a probe must either be identified as one of the known gallery classes or rejected as unknown, so three error types coexist: false acceptance, false rejection, and misidentification. An uncertainty score for selective recognition should rank probes by the risk of the decision the system has made. Bayesian gallery-aware models such as Holistic Uncertainty Estimation (HolUE) summarize the posterior over known and unknown classes by Kullback--Leibler (KL) divergence components and map them to an uncertainty score with a supervised nonlinear calibrator. We show that the KL summary is not generally monotone in decision risk: linear fusion of the KL components tuned on validation data yields negative filtering quality on several benchmarks. We propose MPRisk, a mixed-prior posterior decision-risk score that keeps the same Bayesian posterior but directly scores the error events associated with the selected decision: false-acceptance, misidentification, and false-rejection risks, plus a non-specificity penalty for rejections, enabled by modeling unknown identities as a continuous component. Four nonnegative weights tuned on a validation set suffice for ranking; no nonlinear supervised model is required. Across nine image, audio, and text benchmarks, MPRisk achieves the best or tied-best Prediction Rejection Ratio at every operating point on the image and audio benchmarks and on most text operating points, with bootstrap-confirmed gains over HolUE on five benchmarks (up to $+0.19$ PRR) at comparable or lower runtime.

---


### 760. [LEGAU: Learning Semantic Gaussian Priors for Scalable Category-level Pose Estimation](https://arxiv.org/abs/2609.35046)

**<font color=#1a73e8>作者：</font>** Hongli Xu, Zhaowei Lu, Junwen Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Category-level 6D pose estimation from a single RGB-D observation is inherently under-constrained, since partial visible geometry must be interpreted together with a canonical object structure before a stable pose can be determined. We present LEGAU, a unified framework that jointly predicts NOCS correspondence, object pose and size, and a canonical Semantic Gaussian Field. Rather than treating reconstruction as a detached auxiliary task, LEGAU uses the Gaussian field as a category-conditioned structural prior that participates in multimodal feature fusion and provides global guidance for local pose reasoning. Conditioned on a categorical text embedding, LEGAU processes RGB-D observations through a transformer-based fusion module that integrates visual, geometric, and category-level cues, decoding the NOCS map, pose and size information and the Gaussian-based object representation. Extensive experiments on synthetic and real-world benchmarks show that this coupled pose-shape formulation achieves strong performance in a single-model multi-category setting, with up to 22\% on SOPE and competitive transfer to real-world data. These results highlight the benefit of jointly learning canonical correspondence, object shape, and pose alignment within a unified representation.

---


### 761. [OPIS: An Input-Grounded Benchmark for Multi-Object Memory in Video World Models](https://arxiv.org/abs/2609.35052)

**<font color=#1a73e8>作者：</font>** Hao Wang, Tao Yu, Liuzhou Zhang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models must preserve the visual state of the world over time, but existing evaluation protocols often rely on generated histories, video reference, or selected revisit viewpoints that can confound the assessment of a model's true memory capability. To address this, we introduce OPIS, an input-grounded benchmark that strictly anchors the assessment to a fixed set of object instances from the initial observation for evaluating multi-object memory in video world models. The OPIS dataset comprises 500 cases across real-world, embodied-robotic, and game-world domains, providing dense object-level annotations for 12,672 rigid, articulated, and deformable instances. Our object-centric evaluator combines association and explicit visibility reasoning to hierarchically measure Object (O) Presence (P), Identity (I), and Structure (S), utilizing static or dynamic evaluation tracks based on object kinematics. Across eight image-to-video or camera-conditioned world models, our proposed OPIS scores range from 48.65 to 56.01. As the reference inventory grows from less than 20 to more than 40 objects, the Presence, Identity, and Structure scores show an overall decline, with the average Identity score falling from 40.22 to 23.11. The results demonstrate that preserving the particular object instances in the input is considerably harder than generating plausible visual elements.

---


### 762. [Efficient TCitH-Based Alternatives to SLH-DSA: Cross-Layer ASIC Design of Mirath](https://arxiv.org/abs/2609.35053)

**<font color=#1a73e8>作者：</font>** Hiandra Tomasi, Maximilian Schöffel, Johannes Feldmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> To address the security risks posed by quantum computers, the U.S. National Institute of Standards and Technology (NIST) has standardized the post-quantum signature schemes ML-DSA, FN-DSA, and SLH-DSA. While ML-DSA and FN-DSA are lattice-based, SLH-DSA relies on hash-based assumptions. To support cryptographic agility against future vulnerabilities, NIST is evaluating non-lattice candidates as alternatives to SLH-DSA. Among these, TCitH-based schemes are particularly promising due to their compact keys and small signatures.
However, their high computational complexity and memory footprint pose significant challenges for efficient implementations on resource-constrained embedded platforms. They remain largely unexplored in this context, particularly in ASIC implementations. To address this gap, we use a cross-layer methodology combining algorithmic and hardware layers to present, to the best of our knowledge, the first ASIC implementation of Mirath, a TCitH-based signature scheme, in a RISC-V-based system. The design is implemented in a 22nm FD-SOI technology node. Compared with an SLH-DSA ASIC implemented in the same technology node, the proposed architecture achieves 17.8x lower signing latency while requiring 58% less total cell area, showing the potential of TCitH-based signatures as efficient non-lattice alternatives from an implementation perspective.

---


### 763. [Universality and Generalization of Causal Transformers Across Context Lengths](https://arxiv.org/abs/2609.35055)

**<font color=#1a73e8>作者：</font>** Takashi Furuya, Maarten V. de Hoop, Gabriel Peyré  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long contexts are central to modern transformer systems, but most expressivity results choose a different network for each fixed sequence length. We study whether one masked transformer can approximate causal token-to-token maps uniformly over sequences of arbitrary length sampling a fixed normalized horizon. To relate sampling resolutions, we model tokens by $\alpha$-Hölder sequences or, more generally, a common modulus of continuity. Our notion of continuity across resolutions characterizes the causal families admitting uniform approximation on these compact input classes by a single transformer with length-independent parameters. The result extends to the infinite-length mean-field limit, where tokens form continuous curves and masked attention becomes a causal time integral. For bounded regression with target maps satisfying a $\beta$-smooth stability condition defined using regular test functions, quantitative approximation yields a generalization bound: exact empirical risk minimization over suitably sized bounded-weight transformers gives root mean-square prediction error $O((\log\log N/\log N)^{\beta/(d+2)})$ from $N$ iid labeled sequences. The bound holds at fixed confidence on the same sampling distribution, with $d$ the token dimension and no maximum-length factor. Finally, experiments on physical time series support the Hölder-regular token model at observed scales, with dataset-dependent fitted exponents, whereas text input embeddings provide a contrasting case. Native and dense sampling, shuffled controls, and refinement checks delimit this empirical regularity regime.

---


### 764. [Towards Generalizable 3D Anomaly Detection via Relational Inconsistency Modeling](https://arxiv.org/abs/2609.35059)

**<font color=#1a73e8>作者：</font>** KunHo Heo, SuYeon Kim, Hayoung Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D anomaly detection (3DAD) aims to identify defective regions in point cloud data, serving as a critical component in industrial inspection systems. Existing methods are normality-centered -- learning the distribution of normal samples and treating deviations as anomalies -- without explicitly modeling what constitutes a defect. This leads to ambiguous decision boundaries with increased false positives and negatives, particularly in unified and cross-domain settings where diverse normal distributions further blur the boundaries. We propose a relational inconsistency modeling framework that characterizes defects as violations of geometric consistency among neighboring structures. Our approach learns category-agnostic defect cues through pseudo-anomalies designed as controlled relational violations, instantiated by two key modules: Edge-aware Graph Refinement (EGR) for encoding geometric relationships among local regions, and Cluster-Deviation Modeling (CDM) for identifying regions that are relationally incompatible within their structural peer group. Extensive experiments on Anomaly-ShapeNet and Real3D-AD demonstrate consistent improvements over prior state-of-the-art methods in both in-domain and cross-domain settings, validating the effectiveness of learning an explicit, relation-based defect criterion for 3D anomaly detection. Project page: this https URL.

---


### 765. [Beyond Gradient Flow: Identifiability and Recovery from Distribution Snapshots](https://arxiv.org/abs/2609.35060)

**<font color=#1a73e8>作者：</font>** Nam D. Nguyen, Valeriya Malysheva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring dynamics from snapshots of evolving distributions is fundamentally underdetermined: the Fokker-Planck equation constrains the drift $F$ only through its score-weighted divergence $\nabla\cdot F+F\cdot\nabla\log\rho$, leaving a $\rho$-solenoidal gauge invisible to any single-time constraint. Time-indexed transport formulations cannot resolve this ambiguity: every admissible marginal path admits a curl-free explanation, minimum-action reconstruction selects it, and marginal fit alone cannot distinguish dynamically inequivalent explanations. Requiring one autonomous field to explain several marginals instead makes part of the hidden circulation visible as $\nabla\log\rho$ changes across marginals. Separating instantaneous Fokker-Planck source constraints from the snapshot experiment, we show that the source constraints identify the field modulo the kernel of a stacked score-weighted divergence operator. For generic Gaussian shape variation, source constraints at $K\ge m$ time points in intrinsic dimension $m$ eliminate every polynomial gauge direction, whereas finitely many density snapshots alone admit aliasing; we give the obstruction explicitly. At a Gaussian anchor, for Sobolev smoothness $s$ and $n$ samples per time point, we derive a conditional lower rate $(nK)^{-2s/(2s+m+1)}$ for the tangent snapshot experiment, with a matching upper rate in a degreewise benchmark. Strong-form fitting is non-orthogonal to score error and cannot be repaired by spectral filtering. Instead, we estimate using smooth test functions while retaining the known diffusion term, and derive a finite-sample bound that separates sampling error from fixed-grid quadrature bias. Planted-circulation experiments confirm the predicted gauge contraction and expose a design tension between cross-slice information and covariance-aware whitening.

---


### 766. [Depot-Closed Multi-Component Construction for Neural Vehicle Routing](https://arxiv.org/abs/2609.35066)

**<font color=#1a73e8>作者：</font>** Shinichiro Hamada, Hisashi Kashima  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most neural constructive solvers for the vehicle routing problem (VRP) use route-by-route construction, extending one route until completion before starting the next. This commits route membership early and hinders global coordination across routes. We propose multi-component construction, which maintains many route components simultaneously and merges them in an arbitrary order. This removes the depot-return cue that route-by-route construction obtains from the remaining capacity; to compensate, we introduce an interpretation in which every component is treated as an implicitly depot-closed route. Under this depot-closed interpretation, every intermediate state of standard CVRP construction is a complete feasible solution, and the exact cost reduction of a merge is the Clarke-Wright saving. The neural policy combines this CW-saving signal with the evolving component state to learn what to connect and when to connect. A policy trained only on CVRP100 outperforms the reported results of representative neural solvers on CVRP100-500 with greedy inference and, reused for ruin-and-reconstruct, performs strongly at all evaluated sizes up to CVRP1000. In a zero-shot Constraint Tightness evaluation with capacities from $C=10$ to $500$, it outperforms the reported neural solvers at every capacity. Controlled analyses show that robustness persists without CW grounding and point to learned route-closing behavior as a plausible contributor to the tight-regime degradation of learned route-by-route solvers.

---


### 767. [Interrelating Fruchterman-Reingold Graph Visualization and Agglomerative Clustering](https://arxiv.org/abs/2609.35073)

**<font color=#1a73e8>作者：</font>** Alexandre Benatti, Luciano da F. Costa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph visualization methods and agglomerative clustering have been frequently considered in data analysis and pattern recognition. Because these approaches are interrelated and complementary, it is of particular interest to investigate their associations. In this work, we study the possible relationship between the Fruchterman-Reingold graph visualization method and four types of agglomerative clustering adopting single- and complete-linkage, average, and Ward's linkage criteria. Three types of datasets have been considered in 2 and 10 dimensions, as well as the PCA projection of the latter to two dimensions. The results obtained suggest that the relationship between the methods considered did not vary much for the three types of data mentioned above. At the same time, the agglomerative methods tended to yield results that are mostly similar to each other, while presenting moderate similarity with the original data. The Fruchterman-Reingold visualization resulted similar to the original data, but exhibited relatively smaller similarity to the agglomerative methods.

---


### 768. [ReCo: When to Relocate Sensor Kits under Deployment Constraints -- A NILM Case Study](https://arxiv.org/abs/2609.35075)

**<font color=#1a73e8>作者：</font>** Haokun Chen, Yu Tong, Yehai Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many sensing tasks obtain training labels only by deploying instruments in the field. With a limited number of sensor kits, a collection deadline, and measurement downtime at every move, the collector must repeatedly decide whether to stay at the current site or relocate. We study this decision in non-intrusive load monitoring (NILM), which estimates the power drawn by individual appliances from a home's main meter and is trained on data from homes temporarily fitted with appliance-level sub-meters. In NILM, appliance usage varies with the appliance, season and climate, and the value of new data depends on how diverse the combinations of target operation and background load are. To address this, we propose a constraint-based relocation framework and instantiate it for NILM as ReCo (Relocation by Coverage gain). ReCo counts new operating regimes in a joint target-background feature space, forecasts each home's future gain from the data collected so far, and each night weighs the gain of staying against the gain of moving elsewhere after the downtime. In replayed deployments on the Plegma dataset under two kit counts and two downtime costs, ReCo outperforms fixed-dwell and count-based schedules and a threshold rule using the same metric in every setting. Its advantage is not explained by collecting more days alone and reflects allocating the days to more valuable homes and periods.

---


### 769. [Propagate, Then Sharpen: Post-Hoc Refinement of Frozen Node Classifiers](https://arxiv.org/abs/2609.35080)

**<font color=#1a73e8>作者：</font>** Preben Johnsen Bentdal, Nello Blaser, Xue-Cheng Tai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study post-hoc refinement of frozen node classifiers: given only the graph $G$ and class distributions $Q$ predicted by a frozen model, can we improve accuracy without access to node features, model parameters, or gradients? APPNP answers this by propagating logits with a restart towards the initial predictions, minimizing the anchored Dirichlet energy. Instead, we consider the Potts energy, and decompose it into a Dirichlet term, which penalizes disagreement between neighbouring nodes, and a Gini term, which penalizes indecision within each node. This decomposition motivates Propagate, Then Sharpen (PtS), which alternates between propagation of class probabilities and node-wise, mass-preserving sharpening, with only one additional hyperparameter selected using labelled validation nodes. Across nine homophilic graphs, with a frozen MLP backbone, PtS improves mean test accuracy over independently tuned APPNP by $1.71$ percentage points on clean inputs and $3.90$ under severe Gaussian feature corruption. Gains over APPNP become smaller, but remain positive with frozen GCN and GraphSAGE backbones. Sharpening also removes most of the accuracy loss of deep propagation: on clean inputs without restart, accuracy falls by $2.2$ points between $2$ and $100$ propagation steps under PtS, compared with $33.8$ for APPNP.

---


### 770. [Retrieval-Augmented Diffusion Modeling for Stochastic Discount Factor Portfolios](https://arxiv.org/abs/2609.35086)

**<font color=#1a73e8>作者：</font>** Kelvin J.L. Koa, Xinyang Li, Ke-Wei Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we study portfolio optimization under the stochastic discount factor (SDF) framework by learning market state representations that capture the underlying risk structures of financial data. This is challenging due to several factors: financial markets exhibit non-stationary dynamics with shifting regimes, multimodal inputs such as price and news data often contain stochastic noise, and existing diffusion-based approaches, while effective for modeling stochastic dynamics, rely on assumptions such as isotropic Gaussian noise that fail to capture the state-dependent nature of financial uncertainty. To address these challenges, we introduce RADAR, a retrieval-augmented diffusion framework that learns market representations by conditioning on similar historical regimes. RADAR leverages retrieval to construct context-dependent noise distributions, applies conditional diffusion to denoise multimodal representations, and initializes the diffusion process using empirical statistics to reflect state-dependent uncertainty. Experiments show that RADAR achieves state-of-the-art performance on key risk-adjusted metrics while producing economically meaningful signals on asset returns and correlations.

---


### 771. [DF-CBM: Region-Aware Concept Bottleneck Models for Deepfake Detection](https://arxiv.org/abs/2609.35096)

**<font color=#1a73e8>作者：</font>** Georgios Tsoumplekas, Vazgken Vanian, Alexandros Doumanoglou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detection methods have become increasingly effective yet most provide limited insight into the evidence behind their predictions. However, in forensic settings users also need to know which manipulation cues support the decision and where they appear. Existing explainability methods only partially address this need since localization-based approaches lack semantic descriptions while language-based explanation methods are only weakly grounded in visual evidence. In this work, we propose DF-CBM, a region-aware concept bottleneck model for explainable deepfake detection. DF-CBM builds a compact vocabulary of manipulation-related concepts from textual artifact annotations and links each concept to plausible facial and boundary regions. It then predicts these concepts from visual features using a concept-specific masked attention mechanism guided by parsed facial masks and the final real/fake decision is made from the predicted concept bottleneck. Our experiments show that DF-CBM outperforms concept-based baselines in concept prediction and deepfake classification while remaining competitive with state-of-the-art black-box detectors. Finally, qualitative results and intervention analyses demonstrate that DF-CBM provides spatially grounded concept evidence and enables counterfactual explanations of how individual manipulation concepts influence the final prediction. Our code is available at: this https URL.

---


### 772. [SpikeLite: Lightweight Spiking Neural Networks for Time-Series Forecasting](https://arxiv.org/abs/2609.35097)

**<font color=#1a73e8>作者：</font>** Bang Hu, Changze Lv, Mingjie Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs) offer an energy-efficient paradigm for time-series forecasting through spike-driven computation. However, recent SNN forecasters often pursue higher accuracy through increasingly complex attention mechanisms, or specialized neuronal dynamics, weakening the lightweight motivation of SNNs. We introduce SpikeLite, a spiking forecasting framework built around two modules: a Frequency-Selective Spiking Encoder (FSSE) for frequency-sensitive temporal encoding and a Sparse Spiking Channel Attention (SSCA) module for selective cross-channel interaction. FSSE exploits the low-pass filtering behavior of LIF dynamics to reorganize each input sequence into frequency-sensitive components while collectively preserving the input at the decomposition stage. SSCA then learns a binary mask from encoded channel representations and uses it to selectively exchange information within spike-driven self-attention, retaining informative cross-channel interactions while suppressing redundant ones. When explicit channel interaction is unnecessary, SpikeLite uses the lighter FSSE-only channel-independent path. Experiments under the SeqSNN and SpikF protocols cover four standard multivariate and eight long-term forecasting benchmarks. SpikeLite achieves the best aggregate performance under both protocols, with an average $R^2$ of 0.790 and RSE of 0.440, and lowest average MSE/MAE of 0.343/0.345 in long-term forecasting. Moreover, evaluation on the ECL dataset shows that SpikeLite achieves the lowest reported energy consumption, further demonstrating its potential for energy-efficient time-series forecasting.

---


### 773. [E3J: An Efficient and Open-Source Backend for Euclidean Equivariant Operations on GPU and TPU](https://arxiv.org/abs/2609.35099)

**<font color=#1a73e8>作者：</font>** Olivier Peltre, Armand Picard, Adrien Pichard 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present e3j, a fast Euclid-equivariance backend for geometric deep learning applications with JAX bindings for GPU and TPU. Leveraging both optimized CUDA and Pallas kernels and algorithmic improvements, the library achieves state-of-the-art throughput and runtime on both forward and backward paths. On a machine learning interatomic potential (MLIP) use case, it outperforms established backends, measuring up to 34% speed-up over cuEquivariance on water box NPT simulation using MACE, while remaining fully open source. E3j achieves over 80% efficiency over the H100 maximum memory bandwidth on tensor product operations, and in many cases more than doubles throughput of message passing convolutions forward compared to previously available backends. In addition, with the release of dedicated Pallas TPU kernel, e3j opens the possibility of large scale equivariant deep learning workloads on TPU architectures, which has so far been difficult to achieve. Our benchmarks show that e3j also achieves over 80% of a TPUv6e memory bandwidth, up to one order of magnitude more than e3nn-jax. The library is available on GitHub, PyPI and is released under an open source Apache 2.0 license.

---


### 774. [DRIFT: Disentangled Responsive-Invariant Flow Transport for Single-Cell Perturbation Prediction](https://arxiv.org/abs/2609.35106)

**<font color=#1a73e8>作者：</font>** Mustapha Bounoua, Giulio Franzese, Pietro Michiardi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting cellular responses to perturbations is a central problem in cellular biology, with broad applications in systems biology and drug discovery. This task is challenging because cellular responses can be complex and cell-state dependent, intrinsic cell-to-cell variability can be confounded with perturbation effects, and destructive single-cell RNA sequencing precludes paired measurements of the same cell before and after treatment. Flow matching transports control cells to perturbed states flexibly, but acting on the full cell state can confound perturbation effects with pre-existing cell-to-cell variability. Disentangled approaches separate responsive from invariant components, but model perturbations through prescribed mechanisms, such as latent shifts or graph edits, limiting their flexibility. We address both limitations in a unified framework. A variational encoder disentangles each cell into an invariant block, capturing state unaffected by the perturbation, and a responsive block, capturing state it changes, through conditional priors and an information-theoretic invariance constraint. Conditional flow matching transports only the responsive block, conditioned on the perturbation and invariant state, yielding a flexible, data-driven model of perturbation effects without confounding pre-existing variability. Across several benchmarks, our method outperforms the strongest published method in settings involving combinatorial and unseen perturbation prediction.

---


### 775. [DoAtlas-2: A Foundation for Self-Evolving Causal Biomedical Discovery](https://arxiv.org/abs/2609.35107)

**<font color=#1a73e8>作者：</font>** Yulong Li, Rong Xia, Yuxuan Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce DoAtlas-2, a foundation for self-evolving causal biomedical discovery that organizes knowledge around causal mechanisms and advances through external evidence from human populations. DoAtlas-2 integrates 771 research resources covering more than 720,000 participants in 48 countries, from longitudinal clinical phenotypes, medical imaging, and continuous physiological signals to eight molecular layers, together with an evidence network of approximately 4.7 million literature-derived records over 93,566 concepts and 149,383 candidate causal relations. DoAtlas-2 autonomously formulates research questions from evidence gaps and unresolved mechanisms, prespecifies their causal designs, and generates validated analyses. Supporting, challenging, and unresolved results continuously revise mechanistic interpretations, the causal evidence state, and the discovery frontier, so that DoAtlas-2 self-evolves within a closed loop of hypothesis generation, empirical testing, and renewed discovery. DoAtlas-2 has systematically evaluated 2,031 research questions. In the Human Phenotype Project (HPP), it formulated 4,014 candidate pathway questions across vascular, early-glycemic, and hepatic-metabolic systems, and screening of the first 1,079 yielded statistical support for 756. Representative studies identify blood pressure as a convergence node linking adiposity, hepatic, and lipid phenotypes to vascular outcomes, and show that an adiposity-inflammation-blood-pressure pathway is largely attenuated by joint adjustment for body mass index (BMI) and smoking. The discovered vascular network constitutes a completely interpretable predictive foundation, admitting exact attribution of every prediction and closed-form mediation effects. DoAtlas-2 thereby unifies causal mechanism discovery, population-evidence testing, and interpretable prediction within one continuously evolving foundation.

---


### 776. [Sol-H3: Recursive Self-Improvement for MiniMax-H3 Inference Acceleration on Sol-Engine across Cloud and Edge](https://arxiv.org/abs/2609.35110)

**<font color=#1a73e8>作者：</font>** Yitong Li, Jincheng Yu, Junsong Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video diffusion models are rapidly scaling and exhibiting enhanced generation capabilities. Among these recent advancements, MiniMax-H3 stands out as a highly capable, production-level open-source model. However, its 33-billion parameters and multi-step iterative denoising process introduce substantial computational overhead. Consequently, their practical production is hindered by generation latency in the cloud deployment like NVIDIA-GB200, alongside strict memory limits that pose further challenges at the edge device like DGX-Spark. To address these diverse hardware bottlenecks from cloud to edge device, we present a full-stack inference pipeline that integrates efficient algorithmic design with optimized operator implementations. Algorithmically, we introduce a cross-resolution two-stage generation scheduler that exploits the step-wise nature of diffusion: early low-resolution steps rapidly establish the global layout, while later high-resolution steps focus refinements of local and perceptual details. These stages are connected by a learned latent-to-latent mapping module, completely eliminating the computationally expensive VAE decode-reencode cycle for resolution transferring cross different resolutions. For operator implementation, we deploy a Recursive Self-Improvement (RSI) loop that searches kernel fusions and memory layouts, evaluating latency together with numerical agreement. Together, these optimizations deliver up to 30x end-to-end speedup and 20% lower memory: a 5-second 1344x768 video with audio is generated 3.5x faster than real time on an 8xGB200 node, and in under a minute fully memory-resident on a single DGX Spark.

---


### 777. [SymbolicArena: A Unified Infrastructure for Benchmark Distillation and Dynamic Evaluation in Symbolic Regression](https://arxiv.org/abs/2609.35113)

**<font color=#1a73e8>作者：</font>** Ziwen Zhang, Xiju Wu, Yuheng Jing 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) seeks concise and interpretable mathematical expressions from data for scientific equation discovery. Existing SR benchmarks face a tradeoff between evaluation cost and benchmark validity. Repeated evaluation of large task pools is expensive, and compact benchmarks lack systematic evidence of preserved task diversity and algorithm discriminability. SymbolicArena provides a unified infrastructure for benchmark distillation and dynamic evaluation. The framework standardizes 664 heterogeneous tasks with executable ground truth expressions and distills the Full Task Set into Core50, a validated benchmark of 50 tasks. The distillation process preserves task coverage and algorithm discrimination under explicit balance constraints. SymbolicArena applies a unified execution protocol to heterogeneous SR algorithms and produces comparable outputs and search trajectories. Multi Axis Evaluation characterizes numerical quality, symbolic quality, and search behavior. Core50 reduces evaluation workload by 92.5% and maintains agreement with Full Task Set evaluations. Experiments show that SymbolicArena achieves 72.6% to 86.7% lower approximation error than alternative selectors, further supporting its fidelity to the Full Task Set. Evaluation reveals a substantial gap between numerical fitting and symbolic recovery across current SR methods, suggesting that reliable equation recovery remains an open challenge.

---


### 778. [DuplexCadence: Exact State and Execution from a Speech Model's Declared Timelines](https://arxiv.org/abs/2609.35115)

**<font color=#1a73e8>作者：</font>** Haixiao Gao, Yimin Zheng, Linyou Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech models support streaming interaction that listens and speaks at the same time. Serving them is governed by a strict, repeating deadline: conversation advances on a one-second cadence, and every second of input must be turned into a second of speech before the next second arrives. Because stages within a session run in strict sequence, per-invocation overhead cannot be batched away. Profiling reveals that the autoregressive stages of a duplex second already fit within the period, whereas the token-to-audio synthesis tail is what causes overruns. This tail stage suffers from orchestration slack where the GPU is left waiting as thousands of tiny, regular operations are issued one by one, while also wasting substantial memory by over-provisioning state at static implementation constants. Existing remedies, such as graph recording and demand-sized allocation, fail because streaming state dynamics violate their prerequisites. The root cause is that the runtime lacks the model's native clocks: the per-region counters that govern advancement rates and retention policies. We propose DuplexCadence, which explicitly declares native clocks to the runtime and derives two mutually enabling rules: demand-sized state allocation at a stable address, and exact-shape graph replay without padding. The former eliminates idle memory and stabilizes tensor pointers, while the latter removes orchestration slack without padding overhead. Evaluated on four released models across three decoder architectures with bit-for-bit identical output, DuplexCadence reaches $2.85\times$ the stock runtime's speed at $38.8\%$ lower peak memory. On the live duplex path, mean SPEAK time falls from $14\%$ over the one-second cadence to $2\%$ under it, enabling models to reliably keep up with interactive speech while markedly expanding multi-

---


### 779. [Style-Driven Data Synthesis and Degradation-Aware Enhancement for Ultrasound Image Restoration](https://arxiv.org/abs/2609.35120)

**<font color=#1a73e8>作者：</font>** Yu-Kai Wang, Chun-Xin Tan, Manh-Hung Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-cost handheld ultrasound devices can be widely deployed compared to professional hospital ultrasound machines. However, their images suffer from compound degradation that can mislead clinical judgment. Motivated by this observation, mapping handheld low-quality (LQ) to hospital high-quality (HQ) images has been considered a valuable research question. Conventionally, the mapping requires pixel-aligned LQ-HQ pairs. This requirement is unsatisfactory in practical scenarios because real scans at different times are never pixel-aligned. This paper addresses the challenge with a two-stage framework. The first stage generates pixel-aligned LQ-HQ datasets, and the second stage trains an enhancement model that improves LQ images. The first stage trains a cycle-consistent style-transfer model on unaligned real LQ-HQ pairs to learn a HQ-to-LQ model. Then, the model transforms real HQ images into pixel-aligned LQ images. Based on the dataset generated by the first stage, the second stage uses the Dual Degradation-Guided (DDG) Low-Rank Adaptation (LoRA) method to fine-tune an LQ-to-HQ model based on aligned pairs. In this stage, the model is based on the well known PiSA-SR framework but inserts a degradation-conditioned correction matrix. Experimental results on the USenhance2023 dataset show that the FID metric is improved by 16.7% over the strongest baseline while other metrics indicate that our enhanced outputs are well aligned with the real HQ distribution. The source code of our method is available at this https URL.

---


### 780. [A Multimodal Autonomic Sensing Framework for Objective Assessment of Patient Responses to Dental Pulp Stimulation](https://arxiv.org/abs/2609.35121)

**<font color=#1a73e8>作者：</font>** Youngsun Kong, Yubin Choi, Dongjin Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Patient responses to dental pulp testing, ranging from no sensation to intense pain, provide important information for assessing pulp status in endodontic diagnosis. However, pain is a subjective sensory and emotional experience that varies considerably across individuals and can be difficult to communicate. We investigated whether complementary autonomic signals could support objective assessment of responses during dental examination. Forty-nine patients underwent cold pulp testing, yielding no-response, mild-response, and intense-response conditions. The framework integrated ECG-derived skin nerve activity (SKNA) and R-R intervals (RRI), together with electrodermal activity (EDA), using temporal convolutional network encoders with attention-based mid-level fusion. Individual baseline signals and subject-level covariates, including anxiety scores and biological sex, were also incorporated. The framework achieved 80.2% balanced accuracy, 75.2% sensitivity, and 85.2% specificity for binary classification of no response versus mild or intense response. For three-class classification, it achieved 60.0% balanced accuracy and a 58.8% macro-averaged F1 score. Ablation and attention-weight analyses indicated that EDA contributed most strongly to model performance, followed by RRI, while SKNA improved balanced accuracy by approximately five percentage points. Age was significantly associated with model performance. These findings support the feasibility of multimodal autonomic sensing for objective, non-invasive assessment of responses to dental pulp stimulation.

---


### 781. [Explaining Hyperbolic Neural Networks via Geometry-Aware Relevance Propagation](https://arxiv.org/abs/2609.35128)

**<font color=#1a73e8>作者：</font>** Ping Xiong, Shanglin Li, Yi Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic neural networks introduce geometric operations that require explicit treatment in relevance propagation. Equivalent geometric realizations can produce different feature attributions, even when local relevance is conserved. We study this problem through Geometric Representation Invariance (GRI), a specialization of Implementation Invariance, and zero-curvature consistency, which requires identity relevance propagation when a geometric module approaches the identity. We propose LRP-radial-all for origin-centered radial modules, treating geometric scaling as modulation and assigning relevance entirely to the signal branch. The rule conserves relevance, is invariant to equivalent radial factorizations, and satisfies zero-curvature consistency, yielding GRI for a specified Poincaré-Lorentz logarithmic-map construction. In contrast, a conservative LRP-half baseline can violate both consistency criteria. Experiments on hyperbolic MNIST, sEEG, and CIFAR-10 classifiers assess attribution fidelity, qualitative explanations, and runtime. LRP-radial-all achieves competitive attribution fidelity across datasets with runtime comparable to Gradient$\times$Input and substantially lower than Integrated Gradients. These findings motivate geometry-aware propagation rules that distinguish relevance conservation from consistency across equivalent computations.

---


### 782. [CTP-FL: Common-Trajectory Gradient Prediction for Federated Learning](https://arxiv.org/abs/2609.35130)

**<font color=#1a73e8>作者：</font>** Junkang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Communication-efficient federated optimization commonly spends several
gradient evaluations between server updates. Existing local-update
methods use this computation to advance an independent model on each
client. Under heterogeneous data, however, these models evaluate
gradients at different locations, making the aggregated update
difficult to interpret as a gradient of the global objective.
We study an alternative use of the same computation budget:
\emph{evaluate the global objective along a shared, predicted path}.
We propose Common-Trajectory Predictive Federated Learning
(\texttt{CTP-FL}). At each round, all clients construct the same
sequence of query points from the current global model and the
previous aggregated direction, evaluate $K$ stochastic gradients
along this sequence, and upload their average. The server then
performs a single global update. Thus, \texttt{CTP-FL} uses $K$
mini-batch gradients per client and one model-sized vector in each
communication direction, matching the per-round computation and
communication of full-participation FedAvg-M.
Shared query points make the aggregated direction an unbiased
estimator of the average \emph{global} gradient along the predicted
path. The remaining discrepancy from the gradient at the current
model is controlled by the path length, without assuming bounded
client-gradient dissimilarity or bounded gradients. For smooth
non-convex objectives, we establish an
$\mathcal{O}\!\left(
\sqrt{L\Delta\sigma^2/(NKR)}+L\Delta/R
\right)$
average-stationarity bound under full participation. The analysis
isolates a testable trade-off: extending the prediction path provides
more forward-looking gradient information but increases its
displacement bias.

---


### 783. [VideoPhysEdit: Physical Counterfactual Video Editing via Rigid-Body Physical Scene Reconstruction](https://arxiv.org/abs/2609.35134)

**<font color=#1a73e8>作者：</font>** Conghan Yue, Yuanjie Chen, Yue Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video editing has advanced substantially in recent years, with methods increasingly accounting for the visual consequences of edits, such as changes to shadows and occlusions. However, the physical consequences of edits, including changes to subsequent motion and interactions, remain less explored. We formulate this problem as physical counterfactual video editing (PCVE), which aims to generate a counterfactual video depicting the resulting motion and interactions given a source video, a physical edit, and its execution frame. PCVE is challenging because it requires understanding scene physics and inferring the downstream motion and interactions induced by a physical intervention, while paired factual and counterfactual data and dedicated evaluation metrics are lacking. We introduce VideoPhysEdit, a new training-free pipeline for PCVE in rigid-body scenes. It makes physical reasoning explicit through a novel physical scene reconstruction method that recovers a scene reproducing the observed motion and interactions under simulation, enabling the pipeline to apply physical edits as interventions and use the resulting trajectories to guide counterfactual video generation. We further construct PCVE-RigidBench, a synthetic benchmark with paired source and counterfactual target videos and physical ground truth, and introduce the Physical Edit Score. VideoPhysEdit achieves substantially higher physical edit accuracy than open-source methods and commercial models while maintaining competitive visual fidelity. Its Physical Edit Score is 0.376, the only positive score among the compared methods. Qualitative comparisons on real videos further show that VideoPhysEdit applies to real-world scenes and better depicts the downstream motion and interactions induced by the edits than the compared methods. Code: this https URL

---


### 784. [FlexiWorld: Learning and Planning via Flexible Action Chunks Across Multiple Time Scales](https://arxiv.org/abs/2609.35138)

**<font color=#1a73e8>作者：</font>** Shidu Ren, Qilin Gu, Zhenghao Ni 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models predict future states for goal-directed planning using action chunks spanning multiple primitive steps. Existing methods typically use fixed-length chunks and either omit goal-conditioned action generation or limit their supervision to short goal spans. We introduce FlexiWorld, a JEPA-based world model that combines mixed-span goal supervision with variable-length action chunks to improve long-horizon control. During training, we sample varying goal spans and randomly partition the actions into variable-length chunks. We jointly train the world model with a causal action encoder that embeds variable-length chunks and an autoregressive actor that generates primitive actions sequentially. Student Forcing reduces exposure bias by training on generated action prefixes. For planning, Actor-Residual Cross-Entropy Method (ARCEM) combines action-residual search with within-chunk autoregressive feedback and chunk-boundary latent prediction. Across four benchmarks and goal distances, FlexiWorld with ARCEM achieves 89.29% mean success, compared with 83.98% for the strongest baseline. PushT ablations show improved direct control from mixed-span supervision, variable-length chunks, and Student Forcing. Without retraining, FlexiWorld supports different planning chunk lengths: longer chunks accelerate ARCEM by approximately $1.3\times$ on average while maintaining comparable average success.

---


### 785. [FONDANT: Strong and Best-Effort Planning via Antichains](https://arxiv.org/abs/2609.35160)

**<font color=#1a73e8>作者：</font>** Benjamin Aminof, Tuan Khai Nguyen, Sasha Rubin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A classical solution concept in fully observable nondeterministic (FOND) planning, is the strong policy (aka winning strategy in the closely related area of reactive synthesis), i.e., such a policy ensures that the goal is reached in an adversarial environment. When strong policies are not available or there is no evidence that the environment is adversarial, one can resort to best-effort policies, which always exist, and which follow the classic decision-theoretic principle that an agent should not use a dominated strategy. A typical positional best-effort policy works as follows: from every state, it follows a strong policy if one exists from that state (such states are called ``strong-winning''), else a weak policy if one exists from that state (``weak-winning''), and else is unconstrained (``losing''). In this work, we introduce a sound and complete planner for both best-effort planning and strong planning. The algorithm that underpins the planner is quite simple: it represents certain sets of states, such as the winning regions, by their $\subseteq$-minimal elements. The algorithm returns uniform policies, i.e., it returns a policy $\pi_t$ that is a strong solution starting in every strong-winning state, and it returns a policy $\pi_w$ that is a weak solution starting in every weak-winning state, and it provides a certificate for the set of losing states. We implemented the algorithm with some simple optimizations (calling it FONDANT), and evaluated it on a benchmark set consisting of the instances that were used in the evaluation of leading strong planners PR2 and FOND-SAT, and the best-effort planner BeSyftP. On coverage, our implementation is at least as good on all domains, and outperforms on some domains; and on wall time, it is slower on small and medium-sized instances, and outperforms on larger instances.

---


### 786. [Small transformers track Bayesian evidence for latent common causes via a context-invariant mechanism](https://arxiv.org/abs/2609.35161)

**<font color=#1a73e8>作者：</font>** Amir Mohammadpour, Michael Franke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an in-depth investigation of how a form of Bayesian reasoning about common causes can emerge as a cross-contextual generalization in small, tractable transformers. Incrementing on recent work, our set-up (i) disentangles causal mechanisms in the model from the causal structure of the true data-generating process, (ii) orients more towards natural language prediction by considering inference of latent common causes, and (iii) considers whether and how Bayesian evidence accumulation for latent common causes can be implemented in representations and mechanisms that allow for cross-context generalization to novel test cases.

---


### 787. [Learning to Re-Draft: A Variational Stackelberg Game for Discrete Diffusion](https://arxiv.org/abs/2609.35166)

**<font color=#1a73e8>作者：</font>** Dmitrii Moor, Federico Tomasi, Paul N. Bennett 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models offer the ability to re-draft, revisiting and correcting earlier tokens throughout generation. This capability depends on the forward corruption process that defines what the denoiser learns to correct. Masked diffusion models fix tokens once they are unmasked, while uniform diffusion permits revisions but relies on uniformly random token substitutions. We instead learn which substitutions are most useful for training the denoiser to re-draft. We introduce Variational Stackelberg Discrete Diffusion (VSDD), a framework for learning a semantically aware corruption process. VSDD formulates training as a leader-follower game: the leader defines a Markovian corruption process parameterized by the denoiser's token embeddings, while the follower optimizes a variational denoising objective with the corruption process held fixed. The leader rewards corruptions based on how much the denoiser improves after learning from them, rather than on how easily the current denoiser can reconstruct them. We measure this improvement under a fixed reference corruption process, approximate the follower's response with a one-step gradient update, and optimize the leader using a score-function estimator. We evaluate VSDD across molecular, text, and playlist generation. VSDD substantially improves molecular validity over uniform and masked diffusion, reduces text perplexity relative to uniform diffusion while remaining competitive with masked diffusion, and achieves sizable improvements in offline playlist recommendation metrics.

---


### 788. [QAM: Quadratic-Accurate Checkpoint Merging via Sequential Consistency](https://arxiv.org/abs/2609.35168)

**<font color=#1a73e8>作者：</font>** Shihao Wang, Rui Kong, Xinran Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Saved checkpoints record states along a training trajectory, but generally do not determine the updates at states that would be visited under a different schedule. We study how accurately these checkpoints can reconstruct the endpoint of a sequential reference with prescribed update strengths. Under a common local transition model, two checkpoint-index moment conditions characterize all convex merges that agree with this reference through second order. We then prove an information limit that for nondegenerate profiles, no algorithm using only a fixed-length gradient-descent (GD) history with step size $h$ can achieve $o(h^3)$ endpoint error uniformly over a fixed class of smooth, strongly convex losses. The lower bound follows from two losses with identical GD checkpoint histories but sequential reference endpoints separated by $\Omega(h^3)$. \textbf{Quadratic-Accurate Merging} (QAM) achieves a matching uniform $O(h^3)$ endpoint error bound. Its explicit coefficients also define the unique profile-dependent merge that exactly matches the sequential GD reference across all fixed quadratic objectives. Across two public Adam checkpoint trajectories (SmolLM3-3B and OpenEuroLLM-Prelude-9B), three windows and three profiles per model, and 15 tasks, QAM shows mixed results for short windows and broader advantages over \textbf{Warmup-Stable and Merge} (WSM) for longer windows. Matched-moment GSM8K diagnostics further show that local consistency alone does not fully determine downstream scores. These results characterize the reconstruction limits of saved histories, provide a coefficient rule that attains the optimal rate, and assess its practical utility.

---


### 789. [ProtoSeam: Lifting Classifier Training with Latent Gaussian Mixture Models](https://arxiv.org/abs/2609.35174)

**<font color=#1a73e8>作者：</font>** Robert Lampel, Timon Klein, Sebastian Sager  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a lifted reformulation of supervised classification that improves the final accuracy of standard classifiers without changing the architecture at inference time. A network $N=N_2\circ N_1$ is split at a single semantic interface and one learnable prototype per class is inserted there. Training combines a quadratic consensus penalty that pulls $N_1(x)$ toward the prototype of its class with a classification loss of $N_2$ evaluated on samples drawn around the prototypes, whereat no gradient crosses the interface. At inference the prototypes are discarded and the unmodified network $N_2\circ N_1$ is used. Across CIFAR-10, CIFAR-100, and TinyImageNet with ResNet and vision transformer backbones, lifted training improves test accuracy by up to five percentage points over variants without lifting under a shared tuning protocol. Moreover, we provide theoretical justification of those results.

---


### 790. [Subgroup Rank-1 Lattice for Practical High-dimensional Black-box Integral Approximation](https://arxiv.org/abs/2609.35177)

**<font color=#1a73e8>作者：</font>** Yueming Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating integrals of black-box, high-dimensional functions, from expectations and kernel mean embeddings to the softmax kernel in self-attention, is a basic subroutine in machine learning. Rank-1 lattice rules suit this setting: they query the integrand only at a fixed point set and need no gradients. When the $n$ points serve as a design matrix $X\in\mathbb{R}^{n\times d}$ for a feature map, however, computing $\Psi(X)^\top v$ or $\Psi(X)w$ for an elementwise nonlinearity $\Psi$ costs $O(nd)$ time and memory for any standard quasi-Monte Carlo point set. We study subgroup rank-1 lattices, whose Korobov generator $(1,t,\dots,t^{d-1})$ uses a scalar $t$ of fixed multiplicative order $m$. Splitting $\mathbb{F}_n^\times$ into cosets of $\langle t\rangle$ reduces both maps to short cyclic correlations evaluated by FFT, giving exact results for arbitrary $\Psi$ in $O(n\log m)$ time and $O(n)$ memory, without forming $X$. Since fixing $m$ falls outside classical component-by-component theory, we prove convergence directly: via resultants with the cyclotomic polynomial $\Phi_m$, the squared worst-case error in the Korobov space decays as $O(n^{-(\alpha-1)/(m-1)})$ for prime $m\ge d+1$, and this threshold is exact. Using the splitting of $n$ in $\mathbb{Q}(\zeta_m)$, averaging over the $m-1$ admissible generators improves the constant by a factor $\Theta(m-1)$. Empirically, the subgroup lattice beats Gaussian and orthogonal random features and scrambled Sobol' and Halton points in 49 of 54 synthetic kernel-estimation settings and all 45 softmax-attention settings on nine real datasets, and builds a sample set with $d=2048$, $n\approx4.1\times10^7$ in 2.3 ms.

---


### 791. [5W1H+Which: Context-Valid Semantic Indexing with Progressive Ontology Binding](https://arxiv.org/abs/2609.35184)

**<font color=#1a73e8>作者：</font>** Yaxiao Liu, Pengbo Liu, Yiwen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transforming raw data into queryable knowledge requires both early extraction of reusable information and explicit types, relations, and applicability conditions for particular tasks. If indexing selects content too early around a single business schema, later tasks may be unable to use information that was omitted. If the index retains only open-ended text, however, rule-based reasoning lacks checkable premises. We propose 5W1H+Which, a semantic indexing design that separates content extraction from ontology binding. The 5W1H questions organize source-grounded content units; Which points to versioned ontology elements and records mapping relations, scope, and validation status. Time, location, system environment, and participant roles are not merely retrieval labels: together, they constrain the contexts in which facts, bindings, and rules apply. Unbound content remains searchable, while bound content enters a formal reasoning path only after premise checks. The method further distinguishes business valid time, system knowledge time, and operational traces, and uses dependency records to support binding revalidation and the maintenance of derived conclusions. A worked example of migration from an on-premises server to a cloud environment illustrates the different treatment of world-state changes, ontology-version changes, and changes in rule applicability. We formulate three groups of falsifiable hypotheses concerning cross-task evidence coverage, control of contextual misuse, and incremental update cost. The planned evaluation includes a strong typed fact-graph baseline with the same evidence, temporal information, and budget, to test whether benefits arise from 5W1H organization, deferred binding, or additional information and engineering effort. The contribution is a testable indexing mechanism, not a claim to a new universal ontology or a demonstrated performance advantage.

---


### 792. [CarveMix-RC: Addressing Rare-Class Imbalance Through Lesion-Aware Synthetic Augmentation for Brain Metastasis Segmentation](https://arxiv.org/abs/2609.35195)

**<font color=#1a73e8>作者：</font>** Md Shibly Sadique, Md Fayaz Bin Hossen, Michael L. Evans 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of post-treatment brain metastases is essential for treatment planning, longitudinal disease monitoring, and quantitative assessment of therapeutic response. The BraTS-MET 2026 Task 1 challenge introduces a clinically relevant segmentation problem involving four anatomically distinct tumor subregions: non-enhancing tumor core (NETC), surrounding non-enhancing FLAIR hyperintensity (SNFH), enhancing tumor (ET), and the resection cavity (RC). Among these, RC segmentation is particularly challenging because of its low prevalence, heterogeneous postoperative appearance, and lesion-wise evaluation protocol, leading conventional segmentation networks to prioritize dominant tumor classes during optimization. The proposed nnU-Net-based framework explicitly addresses RC segmentation through four complementary components: (i) RC-weighted Dice and Cross-Entropy optimization to alleviate class imbalance, (ii) anatomically consistent cavity augmentation to increase the diversity of postoperative cavity appearances, (iii) a residual encoder architecture for enhanced multi-scale feature learning, and (iv) lesion-aware morphological post-processing to suppress false-positive cavity predictions while preserving anatomically plausible structures. The framework is evaluated on the BraTS-MET 2026 Task 1 online validation benchmark. Among the evaluated configurations, the ensemble model (Residual Encoder nnU-Net + nnU-Net + RC-aware CarveMix) achieves the best performance, with lesion-wise Dice scores of 0.732, 0.752, 0.708, and 0.575 and corresponding NSD scores of 0.794, 0.798, 0.727, and 0.474 for ET, TC, WT, and RC, respectively. These experimental results show that integrating RC-aware optimization, anatomically consistent augmentation, and lesion-aware post-processing provides an effective strategy for improving rare resection cavity segmentation in post-treatment brain metastases.

---


### 793. [Alignment Games: A Framework for Conceptual Repair in Human-AI Collaboration](https://arxiv.org/abs/2609.35197)

**<font color=#1a73e8>作者：</font>** Hari Subramonyam, Maneesh Agrawala, Sean Follmer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The meaning of a concept in use is shaped by the situation, task, goals, and prior knowledge. For example, a request to make a poster "visually appealing for a five-year-old" might evoke bright colors and cartoon imagery for one collaborator, but less text, bold shapes, and visual simplicity for another. We call such task-relevant differences conceptual misalignment. We introduce Alignment Games, a framework for making these differences visible and repairable during human-AI interaction. Drawing on theories of situated conceptualization, we characterize task-specific conceptual frames in terms of relevant attributes, values, relations, constraints, and priorities. We then define alignment moves that intervene on the situation, the reasoning used to interpret it, or the resulting frame. Through examples from educational content generation, creative coding, and argumentative writing, we show how these moves can be composed into repair sequences and derive design principles for supporting task-sufficient conceptual alignment at runtime.

---


### 794. [From UNI2-h to ConvNeXt-T: Lightweight Nuclei Instance Segmentation via Knowledge Distillation](https://arxiv.org/abs/2609.35203)

**<font color=#1a73e8>作者：</font>** Wenyan Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nuclei instance segmentation is a core task in digital pathology, yet high-accuracy models rely on large vision transformer (ViT) encoders whose inference speed cannot meet real-time clinical demands. We propose a lightweight scheme that distills the UNI2-h pathology foundation model into a ConvNeXt-Tiny student (Ours-T, 34.7M parameters, 1/20 of the teacher) via output-level knowledge distillation. Ours-T achieves an mPQ of 0.519 on PanNuke (98.8% of the teacher), a zero-shot bPQ of 0.668 on MoNuSeg, and an inference speed of 634.3 img/s, requiring only 0.045 s for full-resolution 1024^2 analysis (21.8x speedup). Experiments further show that multi-scale gated convolution (MALA) yields no gain under ViT encoders, and output-level distillation alone suffices for efficient knowledge transfer.

---


### 795. [OT-PCA: New Key-Recovery Plaintext-Checking Oracle Based Side-Channel Attacks on HQC with Offline Templates](https://arxiv.org/abs/2609.35205)

**<font color=#1a73e8>作者：</font>** Haiyue Dong, Qian Guo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce OT-PCA, a novel approach for conducting Plaintext-Checking (PC) oracle based side-channel attacks, specifically designed for Hamming Quasi-Cyclic (HQC). By calling the publicly accessible HQC decoder, we build offline templates that enable efficient extraction of soft information for hundreds of secret positions with just a single PC oracle call. Our method addresses critical challenges in optimizing key-related information extraction, including maximizing decryption output entropy and ensuring error pattern independence, through the use of genetic-style algorithms.
Extensive simulations demonstrate that our new attack method significantly reduces the required number of oracle calls, achieving a 2.4-fold decrease for hqc-128 and even greater reductions for hqc-192 and hqc-256 compared to current state-of-the-art methods. Notably, the attack shows strong resilience against inaccuracy in the PC oracle-when the oracle accuracy decreases to 95%, the reduction factor in oracle call requirements increases to 7.6 for hqc-128.
Lastly, a real-world evaluation conducted using power analysis on a platform with an ARM Cortex-M4 microcontroller validates the practical applicability and effectiveness of our approach.

---


### 796. [Adversarial Consistency-Guided Representation Learning for Multi-view Clustering](https://arxiv.org/abs/2609.35212)

**<font color=#1a73e8>作者：</font>** Yuchen Lin, Kunpeng Xu, Ying Fang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-view clustering aims to capture cross-view consistency while exploiting view-specific information. However, shared representations learned to capture cross-view consistency may still retain view-identifying information, potentially compromising the consistency of cross-view clustering structures. To address this issue, we propose ACGRL, an adversarial consistency-guided representation learning framework for multi-view clustering. ACGRL employs a gradient-reversal view discriminator to reduce view identifiability and obtain invariant reference representations. These representations are then frozen to provide fixed references for disentangling view-specific information from cross-view common information in the subsequent learning stage. The fixed reference representations are concatenated with the learned view-specific representations for reconstruction and clustering, with cross-view cluster alignment encouraging consistent clustering assignments. Experiments on four benchmark datasets demonstrate the superior clustering performance of ACGRL compared with representative multi-view clustering methods.

---


### 797. [Temporal Heterogeneous Graph Pretraining for Relational Deep Learning](https://arxiv.org/abs/2609.35219)

**<font color=#1a73e8>作者：</font>** Yixin Peng, Er Jin, Diego Collarana 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational deep learning models database rows and foreign-key links as a heterogeneous graph for prediction from record attributes and relational context. These graphs contain two distinct temporal signals: record age changes with the prediction cutoff, while intervals between observed records remain fixed. Prior work often treats time as a single signal or studies temporal representation and pretraining separately. We investigate how explicitly encoding both signals affects temporal pretraining for downstream tasks. Our framework combines Multi-scale Time Encoding, which captures record age using learnable time scales and type-specific projections, with Rotary Time Encoding, which represents signed inter-record intervals through rotary transformations during graph propagation. We pair these encodings with three self-supervised objectives: historical relation recovery, horizon-aware future relation activity prediction, and temporal subgraph contrast. All inputs respect their observation cutoffs. Pretraining proceeds in two stages: subgraph contrast first learns neighborhood representations, followed by refinement through either relation recovery or future activity prediction. We evaluate on five RelBench datasets across 11 classification and regression tasks using heterogeneous GNN and graph Transformer backbones. With both encodings, the best evaluated staged schedules improve over supervised training with the same encodings by 3.02% and 1.06% on the two backbones, respectively, and over controls without pretraining or either encoding by 3.24% and 2.37%.

---


### 798. [Poster: Towards ProofWeave: A Privacy-Minimised, Integrity-Anchored Evidence Plane for Continuous Agentic Assurance](https://arxiv.org/abs/2609.35234)

**<font color=#1a73e8>作者：</font>** Guy Lupo, Nguyen Hung Nguyen, Viet Vo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems increasingly act via tools, memory, delegation, and external services. Existing observability and provenance mechanisms can reconstruct events post hoc, but they rarely show, at the time of the record, whether each policy-relevant action was checked by the intended control before execution. This leaves a trust-observability gap for continuous monitoring, detection, and response: later assurance may rest on evidence that is incomplete, privacy-leaking, mutable, or detached from the policy context that governed the event. What's missing in the literature is contemporaneous, policy-bound evidence that the intended control was evaluated under the policy in force at the time.
We introduce ProofWeave, a record-time chain-of-evidence concept for agentic AI assurance. At each policy-relevant action boundary, ProofWeave generates a privacy-minimised and integrity-anchored evidence transaction that binds (i) agent intent or action, (ii) control response, and (iii) a policy-at-time snapshot. Each transaction is committed to an append-only ledger and materialised into a derived proof graph. A bounded Weaver Agent translates policy intent into proof obligations, while deterministic validators check evidence completeness, privacy minimisation, policy binding, and integrity.
In the minimal scenario, an agent attempts to transmit a secret to an unapproved external sink. The audit compares a logs-only correlation baseline with ProofWeave across verdict latency, join ambiguity, privacy exposure, tamper detection, and resistance to graph-only proof injection. ProofWeave reduces candidate bindings per verdict from up to `10,201` to one, validation operations from up to `10,201` to approximately `26`, and assurance evidence storage from `0.79`MiB to `0.15`MiB per project.

---


### 799. [Long-Horizon Scaling: How Model Capabilities Shape the Returns to Computation](https://arxiv.org/abs/2609.35236)

**<font color=#1a73e8>作者：</font>** Haoyu Zheng, Zhengyu Chen, Huaisheng Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents improve solutions through sustained interaction, execution, and task feedback. Scaling studies relate performance to resources and capabilities, yet how existing capabilities shape returns to extended interaction remains less understood. To address this gap, we analyze AutoLab and EdgeBench, two long-horizon benchmarks. We find that starting performance and subsequent growth are associated with different capabilities: within a task category, similar early scores can precede different later gains. To formalize this finding, we model capability-time scaling with category-specific logistic power laws shared across models. Fitted to early trajectories, these curves extrapolate the observed models' category-average scores to later computation. However, rising average scores mask narrowing improvement opportunities: later gains concentrate among fewer improving models. High final scores and continued improvement also have distinct capability profiles. Predicted mean gains estimate each model's fraction of improving tasks; averaging these estimates forecasts the average share of improving models. These uneven returns motivate deciding whether a specific run should continue. We therefore derive a continuation policy to save time and compute with limited score loss. The policy conditions growth predictions on the run's observed progress and weighs immediate and delayed gains against computation costs. In replay with training and price calibration based on other models' histories, the policy saves roughly one-third of full-run time, with relative score losses of 2.4% on AutoLab individual runs and 3.3% on EdgeBench published mean curves. Our repository is available at this https URL.

---


### 800. [Disentangling Lung-Cancer CT/LDCT AI: A Systematic Evidence Map of Clinical Tasks, Evidence Chains, and Translational Gaps](https://arxiv.org/abs/2609.35240)

**<font color=#1a73e8>作者：</font>** Surajit Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial-intelligence studies using computed tomography (CT) for lung cancer are often broadly labelled "prediction" despite addressing clinically distinct tasks. We systematically mapped CT/low-dose CT (LDCT)-centered lung-cancer AI using five-database retrieval, full-text eligibility assessment, role-aware modality/omics extraction, clinical-task classification, and a Multi-Tier Evidence Graph (MTEG). The final corpus comprised 293 studies (2016-2026): 230 Detection, 8 future Risk-prediction, and 55 Other studies. Clinical variables (96.2%), 3D CT/LDCT (73.0%), and radiomics (63.5%) predominated, whereas external validation (29.0%), calibration (20.5%), decision-curve analysis (13.0%), longitudinal CT (17.7%), and saliency/attribution XAI (21.5%) were less frequent. The MTEG comprised 377 nodes and 3,444 edges; only 31 studies (10.6%) completed the six-tier substantive evidence chain, with greatest attrition at reasoning/explanation. Overall, the literature is detection-dominated, genuine future risk prediction remains uncommon, and complete translational evidence chains are rare.

---


> [!TIP]
> 当前位于：**751-800**（第 16/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | **751-800** | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
