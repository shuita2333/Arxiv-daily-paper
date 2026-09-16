# 📦 其他研究 | 2026年09月17日

> 本类共 **219** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-219](./part-05.md)

---

### 1. [Single Document Extractive Summarization using Domination in Hypergraph](https://arxiv.org/abs/2609.15993)

**<font color=#1a73e8>作者：</font>** Aamir Miyajiwala, Aabha Pingle, Sheetal Sonawane 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Text Summarization (ATS) in Natural Language Processing has been an important task in Information Retrieval. It compresses a document to create a summary that captures all the relevant and important information conveyed in the document. This study explores Hypergraph for extractive text summarization of single documents. Objective: This study explores a novel method of leveraging the property of domination in hypergraphs to generate an extractive summary and compare its performance with state of the art graph based methods. Method: Our work aims to generate an extractive summary by creating a sentence hypergraph where each sentence represents a node and the edge is a keyword or a named entity that contains the sentences in which it occurs. We generate a hypergraph where each edge is a keyword or an important topic and the nodes are sentences containing those keywords. Then we apply a greedy algorithm to find the dominating set of the hypergraph which will contain sentences that will form the extractive summary.

---


### 2. [Bias Audits Detect Bias but Disagree on Ranking: Evidence from Ten Instruments and Ten Frontier Models](https://arxiv.org/abs/2609.15995)

**<font color=#1a73e8>作者：</font>** William Guey, Pierrick Bougault, Wei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emerging AI regulation mandates bias audits of high-risk systems, and audit scores are beginning to be used to rank models. Both uses assume different audit tools measure the same thing well enough to compare. We test that assumption directly, running ten extrinsic audit instruments over a shared panel of ten frontier models through one pooled inference gateway, first on occupational gender bias, then on age and socioeconomic status. Detection succeeds while ranking fails. Eight of ten tools detect bias with confidence intervals clear of zero; two widely cited direct-probe benchmarks are saturated because frontier models now answer neutrally. But cross-tool rank agreement is indistinguishable from chance (Kendall's W=0.07, p=0.83). A positive control with six deliberately weaker models separates two explanations: within-tool reliability recovers once the panel spans real capability gaps, yet cross-tool ranking never recovers, which points to the tools measuring different constructs rather than one construct noisily. Even the direction of bias splits by audit format: forced-choice decision tools mostly over-correct (toward women, and toward working-class candidates in 273 of 278 hiring decisions), while free generation and default coreference stay stereotype-congruent. The pattern replicates on socioeconomic status; an apparent ranking agreement on age dissolves under the paper's own tool-inclusion rules. The practical message: a single audit can detect bias and estimate its direction within its own operationalization, but no single audit supports ranking one model against another. All raw responses, code, and the analysis that recomputes every reported number from source are available at this https URL.

---


### 3. ["Looking for Something Weird to Happen": How Humans Sustain AI Agent Novelty Amid Semantic Collapse](https://arxiv.org/abs/2609.16051)

**<font color=#1a73e8>作者：</font>** Shiyang Lai, Arna Woemmel, Hongkai Mao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Semantic collapse, the progressive narrowing of what AI systems generate, has been studied mainly in closed settings, and remedies have targeted models and data. We study it in MOLTBOOK, a social network of interacting AI agents that human users configure and steer. Across 30,076 active agents, output grows less diverse within agents and more similar across them over weeks, yet a minority sustains high novelty. Interviews with users of high- and typical-novelty agents (N=11) associate sustained novelty with three features: users value novelty of itself, they supply broad and distinctive material and revise it when output narrows, and they approach MOLTBOOK as a new agentic world to explore, not a venue to instrumentally exploit. A survey of users of distinctive agents (N=53) confirms these patterns. Communities with more novel agents also show more diverse output from other agents. We discuss interface and policy interventions that could support improved human input.

---


### 4. [Causal neural set filtering for online multi-target tracking](https://arxiv.org/abs/2609.16054)

**<font color=#1a73e8>作者：</font>** Zhongdi Liu, Huangyu Dai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based multi-target tracking (MTT) jointly learns data association and state estimation, but MT3/Track-MT3-style trackers repeatedly re-encode measurement windows, incurring redundant computation. We propose Causal Neural Set Filtering (CNSF)\footnote{\href{this https URL}{Code: this https URL}}, a neural set filter that encodes only current measurements while carrying past evidence in a structured recursive track state. CNSF combines exclusive Sinkhorn association, association-conditioned Kalman-shaped updates with moment matching, and recurrent Bernoulli lifecycle modeling with measurement-driven birth. These mechanisms impose soft one-to-one constraints, propagate association-induced state uncertainty, and support existence estimation under missed detections and birth--death transitions. On a held-out three-regime simulated test set, CNSF reduces mean GOSPA and T-GOSPA relative to Track-MT3 by 19.3\% and 30.4\%, with 55.9\% fewer parameters and a $3.76\times$ speedup in single-thread CPU inference.

---


### 5. [Managing Action Preconditions in Neuro-Symbolic RL: Three Placement Strategies for Embodied Agents](https://arxiv.org/abs/2609.16056)

**<font color=#1a73e8>作者：</font>** Norbert Oswald, Fabian Deuser, Thomas Bräunl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans carry behaviour knowledge of how to act in familiar situations into every new task rather than relearning it from scratch. There is no reason a Reinforcement Learning (RL) agent shouldn't do the same: known behaviour patterns need not be learned, only applied. Neuro-symbolic RL bridges prior knowledge and RL by injecting symbolic knowledge alongside a learned policy. The point at which this knowledge is integrated is critical: a poor choice can produce, for instance, hallucinated preconditions, which surface as safety and reliability problems in agents acting in changing environments. We formalise this behavioural knowledge as a precondition Bayesian network (BN) over the agent's \emph{structural actions} - the actions whose legality depends on preconditions, such as picking up a key, grasping a block, toggling a door, or dropping an object. The BN restricts when these actions may fire, and we inject it into the RL loop at three placements: (1) a \emph{symbolic verifier}, consulted only at inference, that fires a structural action once its preconditions hold; (2) a \emph{symbolic enforcer}, active during both training and inference, that governs structural-action use throughout learning; and (3) a \emph{symbolic learner}, which folds the knowledge into the network and learns the restriction and use of structural actions itself. To test the three variants we run experiments on two benchmarks with opposite regimes: one built on long, ordered planning chains, the other on continuous manipulation. We compare against strong baselines on solution quality, sample efficiency, and traceability. The payoff is substantial. On MiniGrid, all three placements improve the \emph{solution quality} over the PPO+RND baseline, the symbolic enforcer leading at $98.2\%$ against the baseline's $88.8\%$. On Fetch, $\dots$

---


### 6. [Driver Behavior Estimation at Signalized Intersections Using a Physics-Constrained Decision-Conditioned Autoregressive Transformer](https://arxiv.org/abs/2609.16058)

**<font color=#1a73e8>作者：</font>** Mohammad Khoshkdahan, Pavel Laskov, Alexey Vinel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Red-light violations and harsh braking at signalized intersections are major contributors to traffic accidents. This paper analyzes and predicts human driver decision-making and longitudinal trajectory behavior during traffic light signal transitions. We collected a diverse real-world dataset comprising 449 approach runs under varying speed and distance conditions. Vehicle motion was recorded using RTK-corrected GNSS with centimeter-level accuracy, and driver heart rate and multi-level comfort ratings were monitored. Spatial and temporal calibration ensured precise alignment between vehicle state and signal timing. Statistical analysis identifies required deceleration as the dominant single predictor of the stop-go decision, and heteroscedastic Gaussian modeling of peak deceleration reveals five empirical comfort ranges derived from human stopping behavior. Based on this insight, we propose a two-stage modeling framework. Stage 1 predicts the binary maneuver decision, and Stage 2 generates the longitudinal acceleration trajectory using a decision-conditioned autoregressive Transformer with physics constraints, including target-state conditioning and jerk limits. The proposed architecture outperforms baseline methods and achieves 0.49m/s^2 acceleration MAE and 0.62m distance MAE. It also estimates the future stopping-comfort level of the human driver from a single yellow-onset snapshot. Qualitative results demonstrate realistic human-like braking behavior. The dataset and source code are publicly available.

---


### 7. [Signed p-adic Residual Encodings of Finite-Domain All-Different Systems with a Sudoku Case Study](https://arxiv.org/abs/2609.16063)

**<font color=#1a73e8>作者：</font>** Greg Baker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study signed, weighted affine $p$-adic residual objectives as native encodings of finite-domain constraints. For primes that separate the finite alphabet, sufficiently weighted positive unary rows pin each coefficient to its allowed set, while negative rows reward unequal endpoints or clause satisfaction. A coordinatewise domination theorem places every global minimiser in the finite domain; there the loss is, up to an additive constant, the all-different conflict count or the negative number of satisfied CNF clauses. Standard Sudoku provides an $81$-coefficient case study without a one-hot lift. A client-side implementation exposes the generated dataframes, arithmetic, diagnostics, and searches.

---


### 8. [A panoramic aerodynamic performance prediction method for turbomachinery cascades using transformer-enhanced neural operator](https://arxiv.org/abs/2609.16066)

**<font color=#1a73e8>作者：</font>** Qineng Wang, Zhendong Guo, Liming Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To enable flexible and rapid aerodynamic performance evaluation in turbomachinery design, this paper proposes a panoramic performance prediction framework. Unlike most previous prediction models that directly predict the objective functions of interest, our approach first predicts the basic parameters of the Navier-Stokes equations, such as temperature, pressure, and density. Utilizing these basic physical quantities, it subsequently predicts key performance parameters of the turbine stage meridian plane. By adopting this methodology, our proposed panoramic performance prediction framework functions similarly to a CFD simulator, capable of predicting various objective of interest to the designers. To enhance prediction accuracy, a transformer-enhanced neural operator (TNO) is introduced within this framework. Using the Rotor 37 blades as a reference, the proposed TNO is trained to predict the performance of a transonic compressor blade in the meridian plane. The TNO can accurately predict total quantities such as isentropic efficiency, mass flow, and distributions of total pressure ratio. Remarkably, the prediction error of TNO is observed to be smaller than that of state-of-the-art deep learning operators such as the FNO and DeepONet. Furthermore, the TNO is applied to downstream tasks, including sensitivity analysis and optimization of various objective functions. The results confirm that the TNO can operate almost like a CFD simulator, while reducing the computational cost of downstream tasks by four orders of magnitude. The effectiveness and reliability of the proposed TNO for solving different kinds of downstream tasks have been well demonstrated.

---


### 9. [A Dynamic Aggregation Strategy Enhanced Efficient Global Optimization Algorithm for Solving High-Dimensional Turbomachinery Design Problems](https://arxiv.org/abs/2609.16067)

**<font color=#1a73e8>作者：</font>** Qineng Wang, Zhendong Guo, Yun Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In order to solve the high-dimensional ($d \geq 30$) expensive black-box problems within budget, an efficient global optimization (EGO) algorithm with a dynamic aggregation strategy is proposed, labeled as DA-EGO. Specifically, the DA-EGO decomposes the original high-dimensional design space into a set of low-dimensional subspaces for efficient surrogate-based optimization search, and the optimal solutions of subspaces are combined as an elite point for the global search. Most importantly, the subspaces are not fixed. Instead, the subspace variables are updated in each iteration, according to the variable interaction analyses in the sub- and full-spaces. The perturbation method and the analysis of variance are used to detect variable interactions. To further accelerate the optimization progress, the searching ranges of subspaces are also adaptively adjusted according to the analyses of subspace optimization results of the previous iteration. Tests on 21 benchmark instances, comprising seven functions at 30, 60, and 90 dimensions, show that DA-EGO is effective on separable and partially separable problems under a budget of 1500 function evaluations. Its advantage is case-dependent: on the non-separable shifted Rosenbrock function, GSGA performs better at 60 and 90 dimensions, while the 30-dimensional results are statistically comparable to IKAEA and GSGA. Moreover, the advantage of DA-EGO is also seen in the aerodynamic optimization of a transonic rotor blade with 28 variables as well as the compressor stage optimization with 60 variables. With the above, the effectiveness of the proposed DA-EGO has been well demonstrated.

---


### 10. [Efficient Multimodal Generative Recommendation with Latent Narrative Reasoning](https://arxiv.org/abs/2609.16070)

**<font color=#1a73e8>作者：</font>** Chenxing Wang, Nantao Zheng, Hao Miao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative recommendation reformulates item prediction as semantic identifier generation, yet episodic content introduces a fundamentally different setting where the target is determined by narrative evolution rather than user preference. This task requires models to understand multimodal storyline progression while addressing the efficiency challenges caused by redundant visual contexts and costly explicit reasoning generation. We propose \textbf{NarraLite}, an efficient multimodal generative recommendation framework that jointly compresses perception and reasoning. Specifically, Progressive Spectral Compression selectively distills long visual contexts into compact narrative-relevant evidence, preserving transition-critical information while reducing redundant visual computation. Latent Narrative Reasoning introduces context-routed latent reasoning tokens and aligns their contextualized representations with future continuation semantics, enabling implicit narrative inference without autoregressively decoding textual rationales. We further establish a user-agnostic multimodal benchmark for short-form drama continuation across UGC, PGC, and OOD settings. Extensive experiments demonstrate that NarraLite consistently improves continuation accuracy, narrative coherence, and robustness over existing approaches, while achieving a favorable accuracy--efficiency trade-off.

---


### 11. [Schema-Adaptive Action-Conditioned JEPA for Cross-Machine CNC Transfer under Partial Sensor Overlap](https://arxiv.org/abs/2609.16071)

**<font color=#1a73e8>作者：</font>** Ayoub Louaye Bouaziz, Matthieu Ostertag, Anton Demasles  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-machine deployment of industrial world models requires transfer across changes in dynamics, sensing interfaces, sampling regimes, and control units. We study a schema-adaptive action-conditioned Joint-Embedding Predictive Architecture (SAAC-JEPA) for CNC dynamics, where the source machine has 17 canonical sensor channels and the target shares only 10. Evaluation uses group-disjoint source splits, source-only normalization, held-out self-supervised validation, unit audits, and a sealed target test after model locking. Across five seeds, JEPA pretraining gives no clean-source forecasting gain: scratch and pretrained-body models obtain \(\mathrm{RMSE}=0.811\pm0.022\) and \(0.813\pm0.022\). A source-only search over 20 candidates selects a schema-consistent action-conditioned JEPA after seven-seed stability checks. On the confirmatory target pass, the locked model reaches zero-shot \(\mathrm{RMSE}=0.546\), \(R^2=0.012\), and \(\mathrm{NLL}=0.52\), outperforming persistence but not RevIN-equipped PatchTST and iTransformer baselines (\(0.503\) and \(0.498\)). A pre-declared paired ablation shows that RevIN in the same architecture improves RMSE to \(0.495\pm0.004\) over three seeds, but degrades target calibration (\(\mathrm{NLL}=20.6\)) on stationary context windows. A pre-lock adaptation sweep further reduces RMSE to \(0.520\) with limited target support. These results show that source-domain forecasting accuracy alone is insufficient to assess industrial predictive representations, and that cross-machine adaptation under partial sensor overlap is a distinct evaluation axis.

---


### 12. [Pseudo-Label Augmentation for Affect Sensing in Small Collaborative Groups](https://arxiv.org/abs/2609.16077)

**<font color=#1a73e8>作者：</font>** Meisam Jamshidi Seikavandi, Tanya Ignatenko, Fabricio Batista Narcizo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physiological affect sensing in naturalistic group interaction is often limited by sparse labels rather than sensor data: wearable devices produce many time windows, while self-reports are collected only a few times per session. Using GroupAffect-4, a four-person collaborative dataset with wearable physiology, eye tracking, Big Five personality, and post-task VAD labels, we study pseudo-label augmentation for affect sensing under sparse supervision. We compare no augmentation, Gaussian Process pseudo-labelling, personality-aware trust weighting, and joint personality-plus-confidence weighting within a shared target-construction pipeline. Results show that pseudo-label augmentation improves over the labelled-only baseline in the known-team setting. However, the narrow range of Big Five cosine similarities (0.91-0.99) makes fine-grained personality weighting ineffective; personality similarity functions mainly as a same-team filter rather than a calibrated trust signal. With smoothing, augmented SVM variants are effectively tied on Valence and Arousal, while the joint personality-plus-confidence variant gives the highest Dominance score. Cross-subject LOSO transfer remains encouraging, especially for Arousal, whereas strict session-isolated LOGO removes the augmentation benefit. Given only 10 groups, LOGO should be interpreted as a conservative lower bound on unseen-group transfer. Overall, the results suggest that pseudo-label augmentation can make better use of sparsely labelled collaborative affect data, while personality information is most useful as a within-team selection mechanism.

---


### 13. [Evaluating Open-Weight E-Commerce Agents with Environment-Grounded Verification](https://arxiv.org/abs/2609.16093)

**<font color=#1a73e8>作者：</font>** Nimit Shah, Haitz Sáez de Ocáriz Borde  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A shopping conversation has many routes to the same cart, and a task-success rate reduces all of them to one score. We build a deterministic and reproducible e-commerce environment that precommits each trial's customer and trajectory parameters, including the persona, difficulty, target cart, and an item reveal schedule. A simulated consumer attempts to buy a target cart from the environment with assistance from the evaluated model. The environment guides the simulator's actions and records every assistant action alongside the environment state at that point. After the trial, these records allow the evaluator to assess individual parts of the conversation against the retained evidence. For example, the evaluator penalizes a search for failing to surface a target product only when the customer has already mentioned that product. We further use this evidence to apply different penalties to tool calls depending on how the assistant's actions compare with an expected tool-call set. Our environment also interacts with the simulator bidirectionally, reading its output to stop the trial when the simulator determines that the customer has become too frustrated and injecting directives in real time that specify when to explore, defer buying an item, or recall a previous exchange. This interaction creates an open-ended and verifiable simulation. Across eight open-weight agents from 20B to 35B parameters, with 160 trials per agent and 44 metrics, the resulting capability profiles distinguish under-action, over-purchase, unsupported product attributes, and poor search, all of which terminal success obscures.

---


### 14. [SWB-DM: A Calibrated Sliced-Wasserstein-Barycenter Aggregator with Delayed-Momentum Caching for Byzantine-Robust Federated Learning under Partial Participation](https://arxiv.org/abs/2609.16099)

**<font color=#1a73e8>作者：</font>** Saranraj S, Saranya M S, Alex David S 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust aggregation methods for federated learning quietly rest on a fragile assumption: that whoever shows up in a given round is a fair sample of the full population. In practice, they rarely are. When only a handful of clients participate per round, even a modest fraction of adversaries can dominate that sample and silently invalidate the finite-sample guarantees that coordinate-wise median, Krum, Bulyan, and trimmed mean all depend on.
We introduce SWB-DM to address this directly. SWB treats each slice of a client update as a one-dimensional distribution, computes a trimmed Wasserstein barycenter across clients, and recovers coordinate identity via a medoid-based gauge-fixing step -- a heuristic we developed and do not claim it belongs to standard optimal-transport theory. DeMoA-style delayed momentum then caches updates across the full client population each round, decoupling robustness from whoever happened to be sampled. Trim ratio calibration is not cosmetic: under-trimming causes collapse at corruption levels a properly calibrated model survives.
Across 448 CIFAR-10 configurations, plus CIFAR-100, FEMNIST, and a 500-client scalability run, we find several mechanistically distinct failure modes. Even-sample coordinate-wise median degrades to a deterministic wrong answer. Krum silently violates its own n greater than 2f+2 precondition and diverges without warning. Bulyan's n greater than or equal to 4f+3 threshold produces a sharp pass/fail boundary. On attacks, IPM defeats order-statistic defenses -- including SWB -- more reliably than ALIE, confirmed through delta-space measurements against a convergence bound.
SWB-DM's cache carries a real warm-up cost, but extending all baselines to the same round budget shows its CIFAR-10 gains are disproportionately large. On CIFAR-100, FLTrust benefits more -- for reasons entirely unrelated to caching.

---


### 15. [A Decision-Support Audit Protocol for Supervision Drift in Proxy-Labeled Credit-Risk Prediction](https://arxiv.org/abs/2609.16102)

**<font color=#1a73e8>作者：</font>** Mehrdad Shoeibi, Muhammad Shabanpour, Waldemar Karwowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit-risk models are trained on proxy labels and deployed under temporal and segment change, yet no single transfer metric separates base-rate shift, probability-scale shift, and feature-label relationship change. We contribute a design-science artifact: a locked, multi-signal audit protocol for supervision drift in proxy-labeled credit-risk prediction. Five layers (transfer performance, an oracle-gap probe, a calibration diagnostic, feature-label stability, and a synthetic positive control), thresholds, and decision rules were locked before interpretation; a bounded reading is a designed outcome. On a public LendingClub dataset (temporal 2013 to 2016 and cross-segment transfer), ranking is stable and oracle gaps are small; the clearest temporal signal is a prevalence and probability-scale mismatch that intercept-only diagnostic recalibration largely reduces, though its cause is not identifiable from the available release. The positive control responds only to larger injected shifts; subtler drift cannot be excluded. Mapping diagnostic patterns to governance actions is conceptual guidance, not validated here.

---


### 16. [Optimal Pruning for Neural Architectures using Fisher Information Distances](https://arxiv.org/abs/2609.16129)

**<font color=#1a73e8>作者：</font>** David S. Berman, Yen-Yu Fu, Edward Hirst 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A new scheme for parameter pruning is introduced, derived from the differential-geometric distance in model space. Pruning a parameter sets its value to zero, representing a displacement of the model to the hypersurface on which that parameter vanishes. The minimal distance from the unpruned model to this hypersurface is naturally computed via the geodesic distance in the model space as determined by the Fisher information metric. This distance determines the true change in the model, and its performance, under pruning. By analysing progressively more faithful approximations of this geodesic distance a natural hierarchy of optimality for pruning methods is determined. This starts with the traditional magnitude pruning, then develops into new more sophisticated and effective pruning schemes. The method is demonstrated for both fully-connected networks and vision transformers, on MNIST and CIFAR-10, over the complete $0$-$100\%$ pruning range and across five random seeds. It outperforms pruning by parameter magnitude and by the local Fisher information alone in every architecture and dataset combination considered, on both accuracy and the Matthews correlation coefficient. Additionally, analysis of different levels of geodesic approximation produces intermediate pruning schemes that are computationally efficient and maintain near-optimal performance. This geometric picture supplies not only a state-of-the-art pruning methodology for AI models, but also a verified and mathematically-motivated justification for pruning schemes.

---


### 17. [DenseFace: Bias Mitigation in Face Recognition via Density-Aware Probabilistic Matching](https://arxiv.org/abs/2609.16149)

**<font color=#1a73e8>作者：</font>** Mansur Bultygov, Vadim Seliutin, Dmitry Nekhaev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite steady progress in face recognition, current face recognition models still suffer from significant demographic biases. While approaches for bias mitigation have been proposed, existing methods often impose constraints on the training procedure and result in the degradation of recognition accuracy. To address this issue, we here introduce a method that reduces racial bias in pre-trained face recognition models without compromising their accuracy. To this end, we model face embeddings of each person by von Mises-Fisher (MF) distribution. We next observe the dependency between demographic attributes and the density of MF distributions, and propose DenseFace, a probabilistic face matching procedure that accounts for differences in MF distributions. Our extensive experiments demonstrate DenseFace to consistently reduce racial bias in strong face recognition models varying in network architectures, training datasets and loss functions. Notably, DenseFace preserves recognition accuracy and requires no retraining of the underlying face recognition model. Our work also investigates previously adopted bias measures and makes suggestions.

---


### 18. [GPEvac: GNN-Based PPO for Adaptive Evacuation Routing During Shooting Events](https://arxiv.org/abs/2609.16163)

**<font color=#1a73e8>作者：</font>** Daniel Perkins, Subhadeep Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The sharp increase in mass shootings underscores an urgent need for systems that guide victims to safety in real time. An effective evacuation system must minimize threat exposure while also accounting for adversarial uncertainty and crowding dynamics. Current methods in the literature are rigidly constrained to layout-specific policies and computationally intractable in large-scale layouts, while practical guidelines simply advise victims to "run", "hide", or "fight". We propose GPEvac: a GNN-based PPO framework that computes adaptive evacuation routes during shooting events. To capture both local and long-distance dependencies, we introduce an edge-first sequential message-passing scheme with a learnable virtual global node. The resulting graph embeddings are integrated into a permutation-invariant scoring mechanism that allows a single learned policy to operate across building layouts of diverse topologies and sizes. Through extensive simulation, we show that GPEvac outperforms intelligent baselines across distinct architectural layouts, significantly reducing total threat exposure. Crucially, the system computes global evacuation routes in just 14.73 ms on local CPU hardware, enabling seamless integration with live surveillance systems. In addition to saving lives during shooting events, the methodologies developed are transferable to other graph-structured decision-making domains, including critical infrastructure, intelligent transportation systems, and adaptive sensor networks.

---


### 19. [Skeletal Prototypes on Iterative Nerve Expansions](https://arxiv.org/abs/2609.16170)

**<font color=#1a73e8>作者：</font>** Jordan Eckert, Henry Schenck  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prototype reduction replaces a training set with a smaller representation, and the established methods return a finite set of points. We propose Skeletal Prototypes on Iterative Nerve Expansions (SPINE). The model for each class is an embedded 1-complex rather than a point set. Its initial edge set is a class-conditional Mapper graph, so the data decide which localized clusters are joined. Later phases fit the vertices under a classification objective, and an observation is assigned to the class whose complex is nearest. The segments therefore enter the decision rule and not only the fitting. We evaluate SPINE on seventeen benchmark datasets under stratified 10-fold cross validation, against seven other prototype reduction methods at a matched budget. SPINE attains the highest mean accuracy and the best average rank. It is significantly better than five of the seven competitors under Wilcoxon signed-rank tests with Holm correction. A budget sweep shows that the decision rule using the entire graph segments contribute most when prototypes are scarce, while the method as a whole competes best at moderate budgets. Construction cost places SPINE with the discriminative methods, and it is faster than generalized learning vector quantization on fourteen of the seventeen datasets.

---


### 20. [Anatomy of Associative Recall in Fixed-State Recurrences: A Matched-State Decomposition, an Interference Wall, and a Curriculum That Breaks It](https://arxiv.org/abs/2609.16183)

**<font color=#1a73e8>作者：</font>** Julian Boesch, Andrew Wee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fixed-state recurrences--linear attention and state-space models--are reported to lag behind attention on associative recall, but whole-architecture comparisons cannot say which ingredient is responsible. We decompose masked multi-query recall at a fixed state budget along three single-knob axes: a short causal convolution, the transition structure (rank-1 delta rule vs. diagonal), and decay. The convolution dominates (~+0.5 recall in both families under matched training): comparisons that pit convolution-free cells against a convolution-equipped Mamba measure the missing convolution, not the recurrence. The rank-1 transition beats its diagonal ablation by +0.19/+0.32 at 16/32 pairs, but the margin shrinks to +0.03 once both cells carry the convolution, and a state-matched Mamba-2 ties the unarmed rank-1 cell: no class claim survives. Cells that solve 32-pair recall degrade gracefully with load yet fall to chance retrieving 4 pairs from a distractor haystack--flat across lengths and transitions. Interference under sparse supervision, not capacity: a distance curriculum takes the unchanged architecture from 0.021 to 1.000. Training is a lock-in lottery--a seed either locks in or does not--and the curriculum is the lever. Lock-in rises from 1/10 to 7/10 (p=0.02); dense supervision adds nothing; at L=256 a shaped ramp reopens a boundary the uniform curriculum cannot (4/5 vs. 0/9); and at L=512, where the ramp collapses (0/6), gating it on measured accuracy locks in 6/6 (p=0.001). Bidirectional denoiser cells, reading the query before the haystack, show no measurable advantage over causal training (ten seeds), and collision-key retrieval needs two layers. Arming for recall is free on an S_5 state-tracking guardrail--the armed cell is significantly better at every depth (p<=0.0044). These replace "recurrent models are bad at recall" with a measured decomposition and two cheap interventions.

---


### 21. [Hyperbolic Contrastive Learning with Entailment for Spatial Transcriptomics](https://arxiv.org/abs/2609.16207)

**<font color=#1a73e8>作者：</font>** Daniela Vega, Paula Cárdenas, Hannah Ceballos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial Transcriptomics (ST) has transformed biomedical research by enabling the spatial mapping of gene expression across tissue sections. However, high operational costs, specialized equipment requirements, and sensitivity to experimental noise limit the accessibility and scalability of ST. Recent computer vision approaches aim to overcome these limitations by predicting spatial gene expression directly from histopathology images. While effective, current approaches often suffer from gene expression over-smoothing and overly uniform predictions across tissue regions, suggesting that further progress depends on learning representations that reflect the hierarchical and asymmetric structure of gene regulation and tissue morphology. To address these issues, we propose Hyperbolic Contrastive Learning with Entailment for Spatial Transcriptomics (HyCLoST), a hyperbolic contrastive learning model that captures the intrinsic hierarchical relationships within ST data. By leveraging hyperbolic geometry and a gene-to-image entailment loss, HyCLoST learns structured, biologically grounded representations that improve gene expression prediction accuracy, achieving a 6% reduction in MSE and an 8% increase in PCC across 26 ST datasets, over previous methods. Our source code is publicly available at this https URL

---


### 22. [Analyzing Multi-Factor Authentication Through Cryptographic Security Properties](https://arxiv.org/abs/2609.16214)

**<font color=#1a73e8>作者：</font>** Ryan Tipping, Yousef Tahboub, Krishna Bodige  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern authentication systems use cybersecurity techniques to validate the identity of the person (or applications acting on behalf of the person) as a primary defense against unauthorized access. While initially built around single mechanisms such as usernames/passwords, physical tokens, or biometrics, current systems have evolved into multi-factor authentication (MFA) platforms that combine multiple mechanisms. Among them, several focus on strategies that prevent replay attacks (i.e. the reuse of a component that could have been potentially compromised).

---


### 23. [How I learned to stop worrying and love StopGrads: Stationarity, Convergence, and a case study on Flow Map Learning](https://arxiv.org/abs/2609.16222)

**<font color=#1a73e8>作者：</font>** Max W. Shen, Mark Goldstein, Zichu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stopgrads are widely used in training machine learning models, but stopgrads can alter the gradient, stationary points and convergence guarantees of the original objective, which can make stopgrad training theoretically ungrounded. We introduce a stopgrad regression principle, which identifies a general template for stopgrad objectives with a closed-form characterization of stationary points and their uniqueness, unifying stopgrad objectives for flow maps, reinforcement learning, and diffusion samplers. We provide theoretical grounding for optimizing stopgrad flow map objectives by showing their unique stationary point is the true flow map, and showing positive convergence results for Eulerian and Lagrangian objectives, including MeanFlow and improved MeanFlow. Remarkably, we show that under functional semi-gradient flow, the learned flow map has a closed-form expression composing the initial flow map and the true flow map. We additionally use our stopgrad regression principle to propose modified stopgrad placements for flow map objectives which reduce training memory by 2x.

---


### 24. [Exploiting and Securing Docker containers and Kubernetes pods from a MitM attack](https://arxiv.org/abs/2609.16253)

**<font color=#1a73e8>作者：</font>** Henry Kabuye, Ismail Khalid Kazmi, Chunyan Mu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> PURPOSE - Workloads in containers, such as Docker containers and Kubernetes pods, are vulnerable to many of the same attacks as workloads in non-container environments, including phishing, application exploits and network intrusions. This systematic review and design-and-creation study explores techniques for securing containerised-based operating systems against Man-in-the-Middle (MitM) attacks. The proposed framework uses a conceptual model for representing communication and cryptographic primitives, together with the AnBxJ Java security library and container firewalls operating at layer 7 of the OSI model. The study addresses the question: How can containerised-based operating systems be effectively secured from Man-in-the-Middle attacks? It aims to support practitioners in protecting Docker and Kubernetes deployments by systematising security practices and applying a zero trust architecture.
METHODOLOGY - The research uses a Systematic Review (SR) based on the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA), bringing together evidence from studies addressing the same research topic.
FINDINGS - Success factors were identified, and a security mechanism was successfully implemented in a containerised-based operating system scenario.
VALUE - The findings may help practitioners protect Kubernetes and Docker installations by systematising container security practices and providing a zero trust architecture for containerised-based operating systems.

---


### 25. [SuperSenseDoctor: A Multimodal and Contactless Agent for Health Tracking](https://arxiv.org/abs/2609.16257)

**<font color=#1a73e8>作者：</font>** Xuwen Zhang, Zijian Lu, Yicheng Lei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Population aging is increasing the need to monitor older adults safely and independently at home. However, cameras, wearables, and manual checks often introduce privacy, adherence, and attention burdens that hinder sustained health monitoring. This paper presents SuperSenseDoctor, a multimodal contactless agent architecture for long-term home health tracking. The system transforms WiFi, mmWave radar, and surface temperature into a persistent human health state. The system relies on fixed decision rules to conduct continuous daily monitoring and respond to pre-defined hazards. When abnormal signals appear, event-driven reasoning analyzes only standardized evidence to produce traceable care-support measures. In this manner, SuperSenseDoctor integrates sensing, temporal state, reasoning, and action into a unified and auditable loop. The calibrated multimodal pipeline achieves 1.994 bpm mean absolute error (MAE) and 3.142 bpm root mean square deviation (RMSD) for heart rate, 0.197 bpm MAE and 0.263 bpm RMSD for respiratory rate, and 96.5% fall-recognition accuracy. The evaluation also covers 2686 one-second states across 9 chronological intervals and reaches a 96.7% criterion-level Agent checklist pass rate. These results demonstrate the feasibility of a stateful contactless sensing-to-action architecture for long-term home health monitoring.

---


### 26. [The AI-Enabled Scientific Frontier](https://arxiv.org/abs/2609.16258)

**<font color=#1a73e8>作者：</font>** Gabriel Manso, Emma Fu, Neil Thompson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence's capabilities improve, it is increasingly viewed as a general scientific method. But how true are these claims? Does AI outperform all techniques, or only some, and how is this changing? To assess the claims, we assemble a corpus of 2,507 head-to-head comparisons between AI and other scientific analysis techniques across 27 scientific disciplines from papers published between 2000 and early 2025. We find a profound dichotomy. Relative to traditional statistics, AI often outperforms, but at a significantly higher computational cost. But there are also nearly a quarter of cases where AI is both more expensive and performs worse than traditional statistical techniques and this fraction has been stable for a decade. Relative to scientific computing, AI often underperforms, but at lower computational cost. This has begun to change: since 2020, AI's performance against scientific computing has notably strengthened and it now outperforms on more than half of comparisons. These patterns suggest that AI is therefore not a universal replacement for existing methods, but rather a valuable -- and improving -- part of a new AI-enabled scientific frontier.

---


### 27. [The record is part of the task: matched-record evaluation of text classifiers across maintenance, safety and recall reporting](https://arxiv.org/abs/2609.16267)

**<font color=#1a73e8>作者：</font>** Hisham Ihshaish, Peter Mayhew, Tasnim M. A. Zayet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many operational cases are documented more than once, at different workflow stages and for different purposes, yet model evaluations normally select one of these records before model comparison begins. We treat that selection as part of the evaluation and compare matched records of the same cases under fixed labels and splits in three systems: GE Aerospace repair events, NASA ASRS safety reports and NHTSA vehicle recalls. Across the three GE fields, for events whose label comes from parts transactions independently of the narratives, held-out macro-F1 ranged from 0.33 to 0.91. A difference of 0.46 separated the customer report, written before shop work, from the technician report, written after diagnosis but before the transaction that generates the label. That difference is substantially larger than the representation and architecture differences tested on the same events. The public systems showed different patterns: the NHTSA defect summary remained strongest under every model family tested, whereas the ASRS analyst synopsis outperformed the reporter narrative under learned sequence models but not under lexical baselines. Secondary analyses showed that some model comparisons were also record-dependent. Evaluations should be run on the information available at the intended decision point and should report how both the record and the label were produced.

---


### 28. [Speaker-Specific and Language-Dependent Temporal Organization in Bilingual Political Speech](https://arxiv.org/abs/2609.16274)

**<font color=#1a73e8>作者：</font>** Nina Hosseini-Kivanani, Nafiseh Taghva, Peter Gilles 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech rhythm helps structure persuasive speech, but most empirical work examines monolingual English. This study asks how politicians organize timing when speaking Luxembourgish and French. We analyze 400 sentences from ten politicians, annotated for segments and pauses. We compute rhythm metrics, including means, variability, and pairwise variability indices for consonants and vowels. We quantify speaker and language contributions and test within-speaker language effects with paired t-tests. Results show that consonant-based metrics retain speaker-specific signatures, whereas vowel-based metrics are largely driven by language choice. French tokens display longer and more variable vowels and vocalic intervals, while consonant timing differences are smaller. No robust language by gender interactions emerge. These findings show that language choice systematically reorganizes rhythmic timing in bilingual public speech.

---


### 29. [Speaker or Language? Explaining Variance in Charismatic Prosody Across Luxembourgish and French](https://arxiv.org/abs/2609.16275)

**<font color=#1a73e8>作者：</font>** Nina Hosseini-Kivanani, Nafiseh Taghva, Peter Gilles 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Charismatic speech is shaped by language and speaking style, yet their relative contribution in bilingual public speaking remains unclear. We analyzed spontaneous speeches of 10 politicians who address audiences in Luxembourgish and French, in highly comparable communicative contexts across languages. From 400 utterances, we extracted 41 acoustic-prosodic features linked to vocal charisma and fitted mixed-effects models to separate speaker- and language-related variance. Speaker identity accounted for most variance, whereas language explained less, but still showed systematic differences: French productions showed higher shimmer and phrase-final F0, indicative of a polite, respectful voice, while Luxembourgish productions exhibited stronger mid-frequency spectral energy, suggesting a more vocally present profile. These patterns align with the sociolinguistic roles of Luxembourgish as an informal identity language and French as a high-prestige institutional variety.

---


### 30. [Scaling Laws for Physics-Aware ACOPF Surrogate Learning](https://arxiv.org/abs/2609.16282)

**<font color=#1a73e8>作者：</font>** Yijiang Li, Emon Dey, Stefano Fenu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-based surrogates for AC optimal power flow (ACOPF) promise large speedups over classical solvers, but their operational value depends on physical feasibility as much as predictive accuracy. Physics-aware objectives such as the augmented Lagrangian (AL) improve constraint satisfaction at additional per-step cost, yet how this trade-off behaves with scale is uncharacterized. We sweep model and dataset sizes under both MSE and AL training, and characterize how constraint violation changes with network size across grids. Both objectives improve as power laws, but at different rates: MSE is governed primarily by model capacity, while AL is balanced across both. Violation grows roughly twice as fast with network size under MSE as under AL. On matched hardware, AL reduces violation by nearly $30\times$ for an order of magnitude more training time, with negligible added memory. The training objective determines not only where a surrogate lands but how its quality evolves with scale.

---


### 31. [Drift Field Net: Learning Ocean Lagrangian advection fields from in-situ and satellite observations](https://arxiv.org/abs/2609.16288)

**<font color=#1a73e8>作者：</font>** Théo Archambault, Pierre Garcia, Mattia Romero 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The North Pacific Subtropical Gyre (NPSG) is a major accumulation zone for floating plastic debris, resulting from basin-scale convergent ocean circulation. Effective cleanup strategies in this region rely on accurate forecasts of Lagrangian particle drift. Here, we introduce Drift Field Net (DFN), a deep neural network that predicts ocean surface flow fields from operational satellite observations. DFN is trained using a novel two-stage strategy that combines pretraining on simulated data with Lagrangian fine-tuning based on an advection-consistent loss function. This physics-informed optimization directly improves the accuracy of particle trajectory predictions. We evaluate DFN against an operational physics-based forecasting system and demonstrate the potential of deep learning for ocean surface flow prediction. On in situ drifter trajectories, DFN reduces the mean positioning error by 20 km after a 7-day forecast compared with the operational model. Furthermore, Lagrangian fine-tuning with the proposed advection loss further reduces the positioning error by 10 km, highlighting the benefits of incorporating Lagrangian constraints into the training process.

---


### 32. [Intelligent Interaction Techniques (IIxT) - Proposal](https://arxiv.org/abs/2609.16295)

**<font color=#1a73e8>作者：</font>** Brad A. Myers  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interaction techniques (IxTs) are the low-level, reusable components out of which user interfaces are designed, including menus, scroll bars, text input fields, and also copy-paste, text-entry, and selecting objects. The IxTs for graphical user interfaces (GUIs) were well established in the 1980s, with relatively minor additions and tweaks for smartphones in the 2000s. Most of today's AI user interfaces involve a chat window, which is an excellent interaction for some tasks, but is generally considered separate from the GUI IxTs. I argue for making the IxTs themselves more intelligent, so users can freely mix modalities, even within the same interaction. This will require research into new IxTs, and also into the infrastructure that will enable these intelligent IxTs (IIxTs) to be built. There are also significant security, privacy and economic implications to this vision.

---


### 33. [Closing the Loop: Branch-and-Bound for Scalable Verification of Nonlinear Neural Feedback Systems](https://arxiv.org/abs/2609.16298)

**<font color=#1a73e8>作者：</font>** I. Samuel Akinwande, Mykel J. Kochenderfer, Clark Barrett  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in the verification of nonlinear neural feedback systems, scalability remains the central obstacle, as state-of-the-art solvers do not yet handle the network sizes and nonlinear dynamics of autonomy applications. Combinatorial solvers do not scale to large networks, whereas propagative solvers excessively sacrifice precision. This work seeks to improve the scalability of combinatorial solvers by formulating verification as branch-and-bound on an abstraction of the closed-loop system. We introduce \rail, an interface that exposes polyhedral enclosures of the dynamics to LiRPA-style bound propagation, and \clipper, a branch-and-bound algorithm that jointly refines enclosures and splits controller activations. This framework enables joint reasoning on the computational graph of the closed-loop system, preserving symbolic correlations across time steps. We present our construction and show that it yields significant improvements over the state of the art.

---


### 34. [Sequence Recognition in Bharatnatyam dance](https://arxiv.org/abs/2609.16306)

**<font color=#1a73e8>作者：</font>** Himadri Bhuyan, Rohit Dhaipule, Partha Pratim Das  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bharatanatyam is the oldest Indian Classical Dance (ICD) which is learned and practiced across India and the world. Adavu is the core of this dance form. There exist 15 Adavus and 58 variations. Each Adavu variation comprises a well-defined set of motions and postures (called dance steps) that occur in a particular order. So, while learning Adavus, students not only learn the dance steps but also take care of its sequence of occurrences. This paper proposed a method to recognize these sequences. In this work, firstly, we recognize the involved Key Postures (KPs) and motions in the Adavu using Convolutional Neural Network (CNN) and Support Vector Machine (SVM), respectively. In this, CNN achieves 99% and SVM's recognition accuracy becomes 84%. Next, we compare these KP and motion sequences with the ground truth to find the best match using the Edit Distance algorithm with an accuracy of 98%. The paper contributes hugely to the state-of-the-art in the form of digital heritage, dance tutoring system, and many more. The paper addresses three novelties; (a) Recognizing the sequences based on the KPs and motions rather than only KPs as reported in the earlier works. (b) The performance of the proposed work is measured by analyzing the prediction time per sequence. We also compare our proposed approach with the previous works that deal with the same problem statement. (c) It tests the scalability of the proposed approach by including all the Adavu variations, unlike the earlier literature, which uses only one/two variations.

---


### 35. [Racing in Volume with Flow Ensembles](https://arxiv.org/abs/2609.16310)

**<font color=#1a73e8>作者：</font>** Saswat Subhajyoti Mallick, Riu Cherdchusakulchai, Marc Ruiz Olle 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 4D reconstruction has been demonstrated only indoors, on dense camera rigs surrounding subjects that move at human pace. Outdoor 4D reconstruction exists but relies either on cameras mounted on the moving vehicle itself, or on limited-coverage arrays observing quasi-static subjects offline. The case that actually matters for spectators is a fast-moving subject, watched from a sparse ring of allocentric cameras, streaming. No method targets this, and no benchmark exists to evaluate one. To this end, we introduce FastFlowGS, a streaming 4D Gaussian Splatting method for reconstructing fast-moving subjects from a small set of fixed external cameras, and Monaco4D, a photorealistic Unreal Engine 5 benchmark for high-speed outdoor reconstruction. FastFlowGS fuses sparse matches, semi-dense tracks, and dense optical flow by lifting each signal to 3D with geometric uncertainty and combining them through a Kalman-style temporal update. Monaco4D provides Formula 1 sequences under varied illumination from trackside, onboard, and drone viewpoints with dense ground truth. On CMU-Panoptic, FastFlowGS exceeds the strongest baseline by 12.6% VMAF at 35% greater efficiency. On Monaco4D, where existing streaming methods degrade severely, it improves dynamic-region PSNR by up to 18.6% with 28.3% lower per-frame optimization time. Dataset and additional details can be found at this https URL.

---


### 36. [Efficient One-to-Many Translation with Joint Multi-Stream Diffusion](https://arxiv.org/abs/2609.16312)

**<font color=#1a73e8>作者：</font>** Yiwen Guan, Jacob Whitehill  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One-to-many machine translation (MT) is computationally expensive for autoregressive (AR) systems, which suffer from linear latency scaling with both sequence length and the number of target languages. We explore how diffusion can enable multilingual translation with a discrete diffusion framework that refines all target languages in parallel, achieving sublinear latency scaling with the number of targets, and supports deployment as a single unified model to replace multiple independent systems. Conditioned on a continuous semantic anchor rather than source tokens, our framework supports zero-shot transfer to unseen source languages without retraining, maintaining approximately $75\%$ of its supervised translation quality on zero-shot sources. We investigate the quality-latency frontier and find that with accelerated sampling, it achieves comparable supervised quality to AR baselines with a $2 \times$ speedup and $11.9\%$ better zero-shot BLEU. These results highlight the potential of joint multi-stream diffusion as a practical and flexible alternative for efficient one-to-many translation.

---


### 37. [Robust Fault Detection in Mechanical Multimodal Time Series via Self-Supervised Cross-Modal Reconstruction](https://arxiv.org/abs/2609.16314)

**<font color=#1a73e8>作者：</font>** Magnus Munk Jensen, Dorte Hammershøi, Rafał Wiśniewski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fault detection is essential in industrial systems, enabling early identification of abnormal behaviour and improving safety, reliability, and operational efficiency. Modern systems increasingly rely on heterogeneous sensing modalities that capture complementary aspects of the underlying physical process. However, existing data-driven anomaly detection methods often process each modality independently or use simple feature-level fusion, limiting their ability to exploit cross-modal relationships that characterize normal system behaviour. Their performance also commonly assumes similar training and deployment distributions, whereas real-world operation is affected by changing operating conditions, environmental influences, and system degradation that induce distribution shifts and reduce detection performance, especially in unseen regimes.
In this work, we propose a multimodal anomaly detection framework based on cross-modal reconstruction of heterogeneous time-series sensor data. Rather than modeling each modality independently, the framework learns system dynamics by reconstructing each modality from the others, thereby exploiting complementary information across modalities. This integrates information across sensing channels without requiring explicit temporal alignment or identical sampling rates, while improving robustness to sensor noise, missing measurements, and modality-specific disturbances. To address distribution shifts during real-world deployment, anomalies are identified using cross-modal reconstruction error and an adaptive test-time thresholding mechanism that adjusts to changing operating conditions. Experiments on three industrial case studies show strong fault detection performance and substantially improved robustness under out-of-distribution conditions, with the largest gains observed in the most challenging operating regimes.

---


### 38. [Generative models for simulation based filtering: Formulations and Empirical Comparisons](https://arxiv.org/abs/2609.16317)

**<font color=#1a73e8>作者：</font>** Mohammad Al-Jarrah, Wei Deng, Bamdad Hosseini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This letter presents a unified formulation and a controlled numerical comparison of generative-model approaches to the nonlinear filtering problem. Under this formulation the analysis step is realized by a transport of the forecast distribution to the posterior, the approaches differing only in how that transport is selected and learned. We derive three new filters, based on stochastic interpolants, their deterministic flow-matching limit, and Schrödinger bridges realized through forward--backward SDEs. We develop a two-stage tuning procedure that separates the training of the generative model from its online refinement. The resulting methods are compared against the optimal transport filter (OTF), the Knothe--Rosenblatt filter (KRF), the sequential importance resampling (SIR) particle filter and the ensemble Kalman filter (EnKF), in terms of accuracy, computational time, and sensitivity to ensemble size and state dimension. The results indicate that every generative filter resolves multimodal posteriors that the EnKF and SIR do not, that no single generative framework dominates, the preferred method being set by the available online budget and ensemble size, and that the filters differ in the regularity of the particle trajectories they produce.

---


### 39. [Cross-Anatomy Transfer Versus Sparse Interpolation in Digital-Twin-Oriented Aortic Fluid-Structure Interaction Surrogates](https://arxiv.org/abs/2609.16322)

**<font color=#1a73e8>作者：</font>** Ali Nourbakhsh, Mohammad Reza Niroomand, Erfan Nourbakhsh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Surrogate credibility for fluid-structure interac- tion (FSI) requires distinguishing transfer across independent anatomies from interpolation within an already sampled surface. Four de-identified human aortic models from the Vascular Model Repository were reconstructed into separate lumen and nominal 1.5-mm wall domains and analyzed under matched first-cycle two-way FSI. A geometry-only LightGBM prior, selected by leave-one-anatomy-out development on three anatomies, was zero-shot evaluated on a fourth, then probed with a post-zero- shot sparse field-completion case study over six targets. Zero-shot transfer was poor across all targets. At a five-percent anchor level (203 anchors, 3,852 evaluation nodes), prior-plus-adaptation reached an oscillatory shear index (OSI) R2 of 0.603. However, same-anchor controls tuned only on the three development anatomies were stronger for several outcomes: inverse-distance weighting reached R2 = 0.829 (OSI), 0.617 (peak von Mises stress), 0.676 (mean stress); radial basis function interpolation reached 0.917, 0.714, 0.778. Sparse within-anatomy labels thus support field completion, but this four-anatomy cohort gives no evidence the cross-anatomy prior adds value beyond direct interpolation. We frame this as a first computational stage toward a measurement-linked digital twin: the surrogate/update layer is evaluated here, while larger cohorts, converged FSI, measurable patient-side inputs, and physics-informed learning remain future work, not a claim of a complete clinical twin. Our code, data and computation files are available at https://github. com/ali-nourbakhsh2005/Aortic-FSI-Sparse-Field-Completion

---


### 40. [Understanding the Usability of Cryptographic Verification Tools](https://arxiv.org/abs/2609.16323)

**<font color=#1a73e8>作者：</font>** Tarikul Islam, Yasin Islam, Khandakar Ashrafi Akbar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographic protocol verification tools are widely used to analyze the security of complex protocols, yet how users interact with these tools remains comparatively understudied. We present an exploratory human-centered study of experienced users of Tamarin, ProVerif, and related protocol verifiers. Our survey included researchers, graduate students, and practitioners with hands-on experience using Tamarin, ProVerif, or related tools. The findings reveal usability barriers across the verification workflow, including difficulties debugging non-termination and performance issues, and the lack of systematic methods for validating formal models against real protocols. When proofs fail without concrete attacks, users commonly simplify models, add helper lemmas, and revisit modeling abstractions. Participants also called for actionable diagnostics, clearer explanations of results, visualization, and automation for recurring proof tasks. Our findings suggest that persistent usability challenges arise from the gap between protocol-level reasoning and the verifier's formal model, proof procedures, and diagnostic output. We derive concrete design priorities for improving the accessibility, interpretability, and usability of cryptographic protocol verification tools.

---


### 41. [Illusion of Depth: Revealing Hidden Stereo Vision Vulnerabilities in Depth Estimation](https://arxiv.org/abs/2609.16336)

**<font color=#1a73e8>作者：</font>** Sri Hrushikesh Varma Bhupathiraju, Tetsu Ishizue, Nicholas U. Costagliola 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Stereo cameras are integrated into autonomous systems such as self-driving cars, drones, and robots to offer precise depth estimation in a cost-effective manner compared to LiDAR technology. In this work, we reveal an intrinsic vulnerability in stereo cameras that stems from their pixel sampling and calibration processes, which can influence the outputs of stereo matching algorithms. Attackers can achieve fine-grained control over the estimated depth of real obstacles using simple repeating patterns, without relying on sophisticated adversarial machine learning techniques. Furthermore, deep learning-based depth estimation models exhibit a similar vulnerability. We evaluate the impact of this attack on two widely used stereo matching algorithms (BM and SGBM), three deep learning models (PSMNet, MoCha-Stereo, and UniMatch), a stereo-LiDAR fusion model (SGM-DDC), and two popular commercial stereo cameras, the ZED2 and Intel RealSense D435. For example, in the ZED2 camera, an attacker can displace obstacles up to 20~meters farther or 12~meters closer. In our real-world evaluation in a driving setting, a brief 0.5~second attack can trigger emergency braking in a popular autonomous driving framework. We further demonstrate the feasibility at driving speeds up to 40~km/h using CARLA. Finally, we confirm the ineffectiveness of state-of-the-art defenses, and we propose a novel strategy that leverages similarity scores to dynamically detect and suppress the depth discrepancies. Our work highlights vulnerabilities hidden in stereo matching and deep learning depth estimation models, addressing critical limitations in autonomous system deployments.

---


### 42. [Channel-Informed Neural Network for Physical Layer Key Generation](https://arxiv.org/abs/2609.16341)

**<font color=#1a73e8>作者：</font>** Jose Angel Sanchez Viloria, George Sklivanitis, Dimitris Pados 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical-layer key generation (PKG) enables wireless devices to establish shared keys from reciprocal channel observations without directly exchanging the key. This capability is attractive for edge networks, where distributed and resource-constrained devices may require lightweight key establishment with limited access to centralized infrastructure. We introduce a channel-informed neural network for PKG that derives binary key features directly from received IQ measurements while explicitly grounding the learned representation in the underlying multipath channel. The proposed multi-task recurrent neural network jointly learns reciprocity-preserving binary features and an auxiliary channel estimate using a training objective that combines deep metric learning with channel-informed supervision. Structured channel sounding enables channel estimation from over-the-air measurements, while Sionna-RT ray tracing is used to augment training with additional propagation conditions. We evaluate the framework using indoor and outdoor software-defined-radio measurements collected on the POWDER radio testbed. Across all evaluated scenarios, the proposed model produces lower bit disagreement for reciprocal Alice-Bob observations than for Eve-related observations. Ray-traced data augmentation substantially improves key diversity, increasing the unique-key rate to 0.94, 0.99, and 0.99 across the indoor and two outdoor scenarios, respectively. Successfully reconciled channel-informed keys pass the selected NIST randomness tests prior to SHA-3 privacy amplification. The results demonstrate the potential of channel-informed representation learning for decentralized wireless key establishment while highlighting an important tradeoff between key diversity and reconciliation reliability.

---


### 43. [From Momentary Emotion Inference to Sustained Emotion Support: Evaluating a Companion Agent in a Longitudinal Study](https://arxiv.org/abs/2609.16344)

**<font color=#1a73e8>作者：</font>** Kexin Quan, Zijian Ding, Jiaye Yong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Sustained emotional support is a long-horizon interaction task closely tied to human well-being. Recent research demonstrates generative agents' capacity for momentary emotional support, yet how these capabilities sustain support over time remains unclear. To examine this challenge, we deployed PAIR, a theory-based emotion-regulation companion, with 19 participants for 14 days. Across 1,093 sessions, we paired emotion estimates with self-reports before and after guidance and analyzed logs and interviews. Estimates corresponded more closely to self-reported valence and dominance than arousal. Guided conversations were followed by higher valence and state-dependent arousal changes. Participants felt understood through contextual exploration and emotional acknowledgment, acting on guidance suited to their needs and constraints. Perceived helpfulness of guided conversation significantly increased over time. Our findings link memory updates and retained corrections to cross-session personalization, informing future emotional support tools that adapt to evolving needs, learn from prior outcomes, and preserve user control over memory.

---


### 44. [Multi-Label Proportion Learning for Sea-Ice Type Prediction](https://arxiv.org/abs/2609.16347)

**<font color=#1a73e8>作者：</font>** Samira Alkaee Taleghan, Younghyun Koo, Andrew P. Barrett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sea-ice type prediction is important for climate monitoring, maritime navigation, and decision-making in polar regions. The main source of label data for this task is the ice chart, produced manually by ice analysts who interpret satellite imagery to delineate ice zones into polygons. Although ice charts are valuable, their production is labor-intensive and expensive, motivating recent efforts to automate the process using deep learning. However, deep learning models require patch-level (or pixel-level) label data for training, while ice charts provide only polygon-level annotations. As a workaround, supervised approaches often create approximate patch-level labels from polygon-level ice chart labels by assigning each sample the dominant ice type of its parent polygon. This approach enables supervised training but creates an ill-posed learning problem with intrinsically approximate solution. In this paper, we redefine sea-ice type prediction as a weakly supervised multi-label proportion learning problem to be able to directly use the polygon-level ice chart labels and avoid unnecessary label approximation for improved prediction accuracy. To address this problem, we propose a two-module framework where first Multiple Instance Learning (MIL) is used for water--ice classification, and then a multi-label proportion learning (MLPL) is introduced for ice-type composition prediction. We further extend this framework with a multimodal model that integrates SAR imagery with AMSR2 brightness temperatures and ERA5 reanalysis data through modality-guided auxiliary regularization. Evaluated on the AI4Arctic dataset, the SAR-only model reduces MAE by 14.5\% and more than doubles mean ice-class F1 over the best supervised baseline. The multimodal model further reduces MAE by 21.5\% and raises mean F1 by 41.2\% over the SAR-only model, and by 52.7\% over the supervised multimodal baseline.

---


### 45. [Federated stochastic bilevel optimization with fully first-order gradients](https://arxiv.org/abs/2609.16350)

**<font color=#1a73e8>作者：</font>** Yihan Zhang, Rohit Dhaipule, Chiu C Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated stochastic bilevel optimization has been actively studied in recent years due to its widespread applications in machine learning. However, most existing federated stochastic bilevel optimization algorithms require the computation of second-order Hessian and Jacobian matrices, which leads to longer running times in practice. To address these challenges, we propose a novel federated stochastic variance-reduced bilevel gradient descent algorithm that relies solely on first-order oracles. Specifically, our approach does not require the computation of second-order Hessian and Jacobian matrices, significantly reducing running time. Furthermore, we introduce a novel learning rate mechanism, i.e., a constant single-timescale learning rate, to coordinate the update of different variables. We also present a new strategy to establish the convergence rate of our algorithm. Finally, the extensive experimental results confirm the efficacy of our proposed algorithm.

---


### 46. [Autonomous Droplet Navigation via Model-Based Reinforcement Learning](https://arxiv.org/abs/2609.16369)

**<font color=#1a73e8>作者：</font>** Rajneesh Anand, Mayuresh V. Kothare  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Precise manipulation of liquid droplets underpins lab-on-a-chip platforms for diagnostics, chemical synthesis, and biological assays. Yet autonomous droplet transport through confined geometries of varying complexity remains an open challenge. Droplets exhibit contact-angle hysteresis, deformability, and capillary pinning, which make their response to actuation nonlinear and history dependent, that classical controllers and pre-programmed trajectories cannot cope in multi-turn environments. Here we demonstrate autonomous navigation of a liquid droplet through geometries of increasing complexity on a gravity driven (Labyrinth) platform using model-based reinforcement learning. A thin silicone oil film reduces contact-line pinning while two-axis tilt supplies the gravitational driving force, and an overhead camera tracks the droplet in real time. An offline-trained policy discovers effective tilt strategies from limited physical interaction data, without simulation or analytical droplet models. The system operates under partial observability, as oil-film thickness, instantaneous contact angle, and droplet deformation state remain hidden from the controller. Despite these challenges, the learned policy achieves reliable navigation across straight, right-angle, and curved-arc paths, including outside-corner geometries. We further demonstrate that a policy trained on a simpler geometry transfers to complex ones, succeeding zero-shot on right-angle and staircase paths and reaching full success on a curved arc with a fifth of the training data. The findings suggest promising avenues for enabling droplet based microfluidic systems to serve as intelligent chemical laboratories.

---


### 47. [Certified Uncertainty Propagation in One-Shot Federated Bayesian Models via Posterior Event Transport](https://arxiv.org/abs/2609.16373)

**<font color=#1a73e8>作者：</font>** Mahyar Mohammadi, Mohammad Hossein Badiei, Abolfazl Yaghmaei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic certification of Bayesian neural networks lower-bounds the posterior probability that a model satisfies a verifier-defined safety property. In one-shot federated Bayesian learning, however, the deployed model is obtained by aggregating parameters drawn from client-specific posterior distributions, so local certificates do not directly guarantee safety of the aggregated model. This paper develops a deployment-consistent certification framework by propagating local posterior events through the deployment aggregation rule, with an exact geometric characterization for Federated Averaging (FedAvg). Each client constructs disjoint hyper-rectangular regions in parameter space and computes their probability masses. The server forms Cartesian products of these regions, maps them through the deployment rule, and retains a product event only when its aggregation image is verified to satisfy the safety property. Under independent client posteriors, each product-event probability factorizes into local masses, and summing verified disjoint events yields a lower bound on safety probability of the deployed model. For FedAvg with nonnegative aggregation coefficients, the image of a Cartesian product of axis-aligned hyper-rectangles is exactly a weighted hyper-rectangle, introducing no set over-approximation. We distinguish the proposed transported-event certificate from direct certification under posterior distributions induced by FedAvg and Product-of-Gaussians aggregation. Experiments on MNIST and Fashion-MNIST under label-Dirichlet heterogeneity show that the transported FedAvg certificate ranges from 22.51% to 46.89%, while direct global certificates range from 72.05% to 91.39%. Results show that predictive accuracy and certifiable safety do not necessarily follow the same trend, and that global posterior constructions can exhibit distinct certification behavior across architectures.

---


### 48. [gr-PHYSEC: Real-time Channel-based Key Generation for Physical Layer Secure Wireless Communications](https://arxiv.org/abs/2609.16375)

**<font color=#1a73e8>作者：</font>** Jose Angel Sanchez Viloria, George Sklivanitis, Dimitris Pados  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Securing wireless communication against eavesdropping is critical, particularly in dynamic and decentralized environments. We present gr-PHYSEC, a new GNU Radio out-of-tree (OOT) module for real-time physical-layer key generation. Unlike traditional key generation that relies on pre-shared secrets or computational complexity, our approach derives symmetric keys from the wireless channel's inherent randomness. We embed a trained neural network within GNU Radio to extract channel features between trusted parties (Alice and Bob) during probe exchanges. These features are quantized into binary keys, reconciled via Reed-Solomon encoding, and further secured with SHA-512 hashing. The generated keys are then directly used to encrypt data. Real-world experiments at the FAU CAAI connected robotics testbed using ADALM Pluto software-defined radios and NVIDIA Jetson Orin validate the approach with ground robotic platforms. Results demonstrate low key disagreement rates and strong randomness, as verified by the NIST test suite for random and pseudorandom number generators for cryptographic applications. This integration showcases how GNU Radio can support real-time AI-driven security solutions, pushing the boundaries of software-defined secure communication. The source code for this project is available at: this https URL

---


### 49. [Bounded Adjustment with Reliability-Guided Embedding for Imbalanced Learning with Noisy Labels](https://arxiv.org/abs/2609.16380)

**<font color=#1a73e8>作者：</font>** Mushir Akhtar, Akarsh J., M. Tanveer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class-balanced learning and label noise create a coupled failure mode: frequency correction prevents majority classes from dominating the decision rule, but can amplify incorrectly labeled minority examples. We introduce BARGE (Bounded Adjustment with Reliability-Guided Embeddings), a single-stage objective combining a bounded, prior-adjusted density-power score with reliability-guided angular geometry. Its classification score is strictly proper in the adjusted probability space and recovers balanced Bayes ordering under clean supervision and the true class prior. Under label contamination, its finite range bounds classification-risk perturbation at a fixed predictor, while its logit gradient redescends when the model confidently contradicts the supplied label. The adjusted target probability also weights class-equal feature compactness, and a one-sided separation term discourages aligned class directions. BARGE requires neither a noise rate nor a transition matrix, uses one network, and leaves inference unchanged. We evaluate it on CIFAR-10, CIFAR-100, and Tiny ImageNet under long-tail and step imbalance, clean labels, and 20% and 40% random incorrect-label replacement. Across 12 clean settings, BARGE ranks second overall and attains the lowest error in four. Under corruption, it achieves the lowest mean balanced error in all six dataset-corruption settings, reducing the six-setting average from 72.32% for the strongest competitor to 70.00%. It also obtains the highest macro-F1 and macro-AUPRC in every corrupted-label setting. Ablations show that class-equal angular compactness improves on the bounded score alone. These results support bounded predictive influence and reliability-guided geometry as complementary mechanisms for imbalanced learning with uncertain labels.

---


### 50. [ParsHate: A Benchmark Dataset for Hate and Target Detection in Persian](https://arxiv.org/abs/2609.16393)

**<font color=#1a73e8>作者：</font>** Zahra Bokaei, Walid Magdy, Bonnie Webber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce ParsHate, a manually annotated dataset of 10,000 Persian tweets spanning 2013-2022, representing the first decade-long benchmark for hate speech detection in Persian. The dataset contains 31% hateful content and supports both hate detection and multi-label fine-grained target identification across seven structured target categories. ParsHate also distinguishes explicit and implicit hate, marks explicit and implicit targets, and provides span-level rationales. Data collection combines random and score-stratified temporal sampling to reduce keyword-driven bias while preserving natural label distributions. Applying SOTA models for Persian hate-speech detection on ParsHate shows moderate performance (79% F1), especially with samples from earlier years, and low performance with target identification (25.5% macro-F1). This emphasizes the diverse sampling of hate speech in ParsHate and its challenging nature that requires more advanced methods for better performance. Dataset is made publicly available.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-219](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
