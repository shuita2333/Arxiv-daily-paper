# 📦 其他研究 | 2026年09月16日

> 本类共 **416** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-416](./part-09.md)

---

### 101. [Recoverability as a System Primitive for Long-Horizon AI Agents](https://arxiv.org/abs/2609.13672)

**<font color=#1a73e8>作者：</font>** Zhihui Zhang, Wei Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can be interrupted while editing files, calling tools, or carrying out multi-step tasks. Restarting repeats completed work, but continuing from unverified or outdated progress can carry earlier errors forward. A saved state is not necessarily a suitable place to resume. We introduce recoverability as a system primitive that makes reuse an explicit decision: select a supported starting point and a permitted recovery action, or withhold automatic continuation. Its behavioral contract binds that choice to supporting evidence, execution, and independent checks. A reference architecture connects persistence, validation, and control, with complementary runtime instances testing distinct responsibilities. Four deterministic and 20 paired file challenges demonstrate that accurate restoration and successful completion can conceal disallowed starting points. Progress controls attribute retained work to shared restoration. Event-time tests show that permission must also constrain the action, and that independently held policy evidence can expose violations even after an effect occurs. These findings establish why recovery decisions need their own evaluation, beyond restored bytes and final task success. Within supplied policies and a declared trust model, the contribution is a common, testable interface for retaining justified progress and making the conditions for its reuse explicit and enforceable.

---


### 102. [Windowed A-K-MDP](https://arxiv.org/abs/2609.13676)

**<font color=#1a73e8>作者：</font>** Xiangwen Yang, Frankie Cho, Iadine Chades  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Markov decision processes (MDPs) are used to support decision-making in conservation of biodiversity, but policies, even over small state spaces, can be difficult to interpret for conservation managers. K-MDP methods address this problem by building simpler MDPs with at most K abstract states. We show that the previously proposed A-K-MDP algorithm that relies on selecting a discretisation divisor using binary search can skip better abstract states. To fix this issue, we propose Windowed A-K-MDP, an algorithm that generates every distinct feasible partition induced within a declared divisor window and evaluates candidates until reaching the ideal value loss (J = 0) or exhausting the family of candidates. Across 33 K-MDP instances, Windowed improved 25 and tied 8.

---


### 103. [MomentBA: Second-order Spatial Moments for Anisotropic Correspondence Uncertainty in Differentiable Bundle Adjustment](https://arxiv.org/abs/2609.13691)

**<font color=#1a73e8>作者：</font>** Yuqing Wang, Xiaoji Niu, Yan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing visual odometry (VO) systems treat feature correspondences as deterministic measurements or assign uniform uncertainty, ignoring the inherent localization ambiguity of different observations. However, correspondence uncertainty is often anisotropic due to image structures such as edges, repetitive patterns, and motion blur, which can significantly affect geometric optimization. In this work, we propose MomentBA, a geometry-aware bundle adjustment framework that derives anisotropic correspondence uncertainty from second-order spatial moments of local similarity responses. Instead of introducing additional covariance prediction networks, the proposed method directly converts matching response distributions into interpretable covariance estimates and incorporates them into bundle adjustment as correspondence-specific information matrices for uncertainty-aware residual weighting. Furthermore, the proposed formulation is integrated into a differentiable optimization framework, establishing a direct connection between correspondence uncertainty and geometric estimation. Experiments on the EuRoC MAV and TartanAir v1 Hard datasets demonstrate that MomentBA improves monocular visual odometry accuracy compared with existing feature-based and learning-based approaches. The proposed anisotropic covariance model achieves lower rotational errors and more robust trajectory estimation than fixed and isotropic uncertainty models, validating the effectiveness of geometry-induced uncertainty modeling for challenging visual environments.

---


### 104. [Choosing Together: How Dyadic Negotiation Shapes Adaptive Kitchen Design Preferences for Older Adults with Cognitive Impairment and Their Care Partners](https://arxiv.org/abs/2609.13700)

**<font color=#1a73e8>作者：</font>** Ibrahim Bilau, Abdurrahman Baru, Stacie Smith 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Adaptive technology for older adults with cognitive impairment is typically designed around individual preference, yet most of this population lives and cooks with a spouse or family member. This paper examines a co-design workshop in which four dyads and two individuals (N=10) built kitchen cabinet designs from twenty-one options across five features. Thematic analysis of thirty selections identifies recurring patterns: visual access retained through enclosure rather than open shelving, physical effort treated as a household concern, and automation accepted when predictable. Structured analysis of ten interaction episodes shows how some patterns were negotiated in practice, including care partners contributing embodied constraints distinct from the primary participant, and disagreements resolving through documented deliberation. Together, the two analyses show that adaptive technology preferences are not always individual properties but can be shaped through household interaction. We offer candidate design implications for facilitation protocols and collaborative systems supporting shared decision-making in aging-in-place contexts.

---


### 105. [Leakage-Safe and Scheduler-Aware Machine Learning for Grid Job Runtime Prediction](https://arxiv.org/abs/2609.13701)

**<font color=#1a73e8>作者：</font>** Ashfaq Ali Shafin, Khandaker Mamun Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate job runtime prediction can improve scheduling-aware resource management in grid and distributed computing environments, but prediction models must be evaluated under realistic deployment constraints. This paper revisits CPU burst time prediction on the GWA-T-4 AuverGrid workload trace and reformulates it as leakage-safe pre-execution job runtime prediction. We define the target as job-level runtime, use only submission-time attributes, exclude post-execution variables, and evaluate models under temporal and cold-start settings rather than relying only on random cross-validation. We compare standard regressors, chronological historical baselines, categorical encoding strategies, and CatBoost with native categorical handling. We further add temporal hyperparameter tuning, runtime predictability analysis, feature ablation, error analysis by job length, and a minimal scheduling simulation. After temporal-validation tuning, CatBoost achieves the strongest deployment-oriented result with R^2=0.239, MAE=27,019, RMSE=46,587, and LogMAE=2.646 on the held-out temporal test set. A single-server simulation over all 69,523 held-out temporal test jobs shows that prediction-informed SJF reduces average waiting time by 50.92% relative to FCFS. The results show that random-split evaluation overestimates performance, categorical-native boosting improves temporal generalization, and long-job underestimation remains a scheduler-relevant challenge.

---


### 106. [Rank-Consistent Set Reasoning for Co-Salient Object Detection](https://arxiv.org/abs/2609.13706)

**<font color=#1a73e8>作者：</font>** Yuan Xiang, Matteo Rossi, Yingzhou Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-salient object detection (Co-SOD) requires a model to find foreground regions that are salient in individual images and supported by the image group. We present \emph{Rank-Consistent Set Reasoning} (RCSR), a supervised dense-prediction framework that models a group as an unordered set rather than as a sequence of images or a semantic label. The core idea is to rank how strongly each spatial region agrees with a small collection of learned group slots at every image scale, and to aggregate these ranks with a robust trimmed statistic. This suppresses accidental pairwise matches and prevents one atypical group member from dominating the shared representation. A set encoder builds group slots directly from multi-scale visual features, while a rank-consistency gate measures whether the ordering of candidate regions is stable across group members. The gated slots are decoded jointly with per-image features to produce co-saliency maps. The model contains no natural-language branch, no open-vocabulary detector, and no external segmentation model. We further introduce a group permutation objective and hard-distractor augmentation so that the model learns the properties of a set-level target rather than memorizing image order or isolated visual saliency. We formulate an evaluation protocol for CoCA, CoSal2015, and CoSOD3k, together with tests of group-size robustness, distractor rejection, order invariance, and cross-dataset transfer.

---


### 107. [When Edit Localization Amplifies Relative Selection Bias: Gradient Geometry, Target Mismatch, and Importance Weighting](https://arxiv.org/abs/2609.13709)

**<font color=#1a73e8>作者：</font>** Shengwei Zhang, Haoda Dai, Yifei Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human corrections identify editable spans, but the examples receiving corrections may come from a selective feedback channel. We analyze this interaction at a fixed model checkpoint by decomposing a localized gradient into edited and retained untouched components. Squared relative selection bias is a ratio of quadratics whose derivative has the sign of an explicit quadratic polynomial. Localization can increase, decrease, or nonmonotonically change this diagnostic; its direction depends on component biases and geometry. Oracle importance weighting recovers the population mean for each fixed localization objective, but these objectives have different targets. Against one common full-gradient target, we derive the finite-sample mean-squared error, an analytic optimal retention coefficient, and a fixed-clipping extension. Exact finite-population calculations and 10,000 Monte Carlo repetitions per sample size verify the identities and counterexamples. Public human-post-edit experiments use two translation directions and pretrained models, with declared synthetic selection. An English-German extension differentiates 73.89 million native parameters. In all three declared settings, hard localization has higher relative bias but lower absolute bias than full retention. Untouched-component biases are nonzero and selected component means have negative inner products, so the general criterion applies where the simple unbiased/aligned explanation fails. Output-bias diagnostics show the same endpoint ordering of relative bias across both directions, with one interior maximum. Mechanisms reuse each language's records and include a mixture; they are not independent replications. The evidence separates relative amplification from absolute gradient error and establishes estimation properties, without inferring translation-quality gains or identifying actual complaint propensities.

---


### 108. [Degraded but Not Entirely Ineffective: PE-Based Deformable Graph Neural Networks](https://arxiv.org/abs/2609.13712)

**<font color=#1a73e8>作者：</font>** Jinhua Wu, Xinliang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many real-world scenarios can be represented using graph-structured data. However, traditional GNNs that transmit messages based on first-order neighbors have long faced several fundamental contradictions: increasing depth leads to over-smoothing, long-range dependencies cause over-compression, fixed neighborhoods restrict the receptive field, and on heterophilous graphs, topological neighbors become a source of noise. Although many works have addressed these issues individually, few mechanisms can simultaneously alleviate all of these challenges. To address the aforementioned problems, we propose a Position Encoding-Based Deformable Spatial Aggregation Module (PEBDSAM) that solves them all in one step. Specifically, we utilize a deformable mechanism in the position space to identify relevant nodes to supplement the original first-order neighbor information of GNNs, allowing traditional GNNs to adapt to heterophilous scenarios. Through diagnostic experiments, we obtained several major findings: current offsets fail to have any effect; subsequently, we analyzed the causes of offset failure and why model performance still improves even after offset failure, pointing out future research directions. Based on these diagnostic experiments, we streamlined the original PEBDSAM, resulting in a simplified version, which we call the Position Encoding-Based Spatial Aggregation Module (PEBSAM). In addition, we propose a PEBSAM-Speed to adapt to large datasets. Finally, we designed the module to be plug-and-play and applied it to GCN, GAT, GIN, and GraphSAGE, achieving desirable results on three homophilous datasets and six heterophilous graph datasets.

---


### 109. [Certifying Model Upgrades with Slice-Wise Non-Regression and Incumbent Fallback](https://arxiv.org/abs/2609.13714)

**<font color=#1a73e8>作者：</font>** Shengwei Zhang, Tao Wu, Fei Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An updated model can improve an aggregate metric while degrading a slice that matters to a downstream user. We study checkpoint selection subject to non-regression tolerances relative to a retained incumbent. The central distinction is between failing to detect harm and certifying non-inferiority: the former can release harmful updates with high probability when evaluation is noisy. We give a reproducible release procedure that separates candidate search from independent, paired evaluation and returns the exact incumbent when certification fails. Applying established intersection-union and Learn-then-Test principles, we state finite-sample guarantees for one frozen candidate, a finite candidate library, and a prespecified testing order. A joint release decision does not require a slice-count Bonferroni penalty, although certification power can still decrease with the number of slices. In bounded-score simulations, a no-detected-harm gate releases a harmful candidate in 99.7% of trials in one 32-slice setting, compared with 2.6% for an exact non-inferiority gate at a 5% target. A constructed two-block family yields larger certified utility than a scalar path under matched candidate counts. Public digits experiments, including a subsequent continuation that improves average aggregate accuracy, return the incumbent in every run because certification is underpowered. These results establish an auditable protocol and its limitations; they do not establish benefits on foundation-model or multilingual translation upgrades.

---


### 110. [JaxAHT: A JAX-Based Library for Ad Hoc Teamwork](https://arxiv.org/abs/2609.13716)

**<font color=#1a73e8>作者：</font>** Caroline Wang, Rolando Fernandez, Zelal Su Mustafaoglu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ad Hoc Teamwork (AHT) addresses the challenge of designing agents capable of coordinating with novel partners without prior coordination. However, progress in the field is hindered by the prohibitive computational cost of the AHT research lifecycle, the lack of standardized benchmark implementations, and the absence of a diverse, validated evaluation teammate suite. In this work, we introduce JaxAHT, the first open-source, JAX-based library designed to accelerate and standardize the AHT research lifecycle. Leveraging JAX's hardware acceleration and massive parallelization capabilities, JaxAHT provides a unified framework for teammate generation, ego agent training, and evaluation against unseen teammates, achieving approximately 95x wall-clock speedup over PyTorch counterparts. Alongside the library, we contribute a diverse suite of evaluation teammates across the domains of Level-Based Foraging, Overcooked, and Hanabi. To illustrate the value of the framework, we use it to conduct a large-scale, compute-controlled benchmark study comparing teammate generation and AHT agent learning methods, finding that no algorithm consistently performs best, and that agent modeling primarily offers benefits in role-based scenarios with diverse teammates.

---


### 111. [PatchRisk: Forecasting Future Vulnerability Exposure in Open-Source Dependency Networks](https://arxiv.org/abs/2609.13719)

**<font color=#1a73e8>作者：</font>** Ashfaq Ali Shafin, Khandaker Mamun Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-source software ecosystems are web-scale dependency networks. A downstream package can become exposed to security risk not because its own source code changes, but because one of its transitive dependencies later receives a vulnerability advisory. Existing vulnerability-detection work often focuses on whether code is currently vulnerable or whether a known vulnerable dependency is already present. We study a different problem: future transitive vulnerability exposure. Given a package-version dependency graph observed at release time, the task is to predict whether any non-root dependency will receive a vulnerability advisory within a future horizon. This problem is important for Web intelligence and software supply-chain security because it supports proactive dependency triage before future exposure is visible. It is also easy to evaluate incorrectly: current vulnerable dependencies can leak the label, and different versions of the same root package can create package-level memorization across train and test splits. We therefore construct PatchRisk, a leakage-aware benchmark from Open Source Vulnerability advisories and this http URL dependency graphs for npm and PyPI. The benchmark uses filtration-aware labels, package-disjoint evaluation, temporal testing, and nested 1K, 3K, 5K, and 10K sampling scales. The largest cleaned setting contains 9,007 root package-version graphs spanning 4,157 root packages. We evaluate three feature families: TimeOnly, GraphStruct, and HistoryGraph. On the 10K temporal-test benchmark, HistoryGraph improves AUPRC over the strongest TimeOnly baseline from 0.351 to 0.640 for 90-day forecasting and from 0.473 to 0.813 for 365-day forecasting. The improvement remains stable across smaller scales and package-group shuffle robustness tests.

---


### 112. ["What Can I Do for You'': How Should AI Companions Provide Assistance to Players in Virtual Reality Games](https://arxiv.org/abs/2609.13727)

**<font color=#1a73e8>作者：</font>** Taiyu Zhang, Xinnian Zhao, Adalberto L. Simeone  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in artificial intelligence (AI) have expanded the capabilities of non-player characters (NPCs), enabling them to perceive game states, perform in-game actions. In immersive virtual reality (VR) games, such assistance is not limited to providing hints or interface-level support: an AI companion can appear as a co-present character, share the player's spatial environment, and visibly act on game objects. This raises a design question for VR gameplay: how can AI companions best assist players while preserving their active participation in the virtual world? To explore this question, we developed a VR puzzle game for Apple Vision Pro featuring an AI companion across four gameplay modes: no assistance, command-based assistance, discussion-based assistance, and autonomous agent play. A within-subjects study with 24 participants showed that AI assistance significantly reduced players' workload. However, autonomous agent play, despite producing the lowest workload, substantially diminished player experience by reducing challenge, autonomy, immersion, and enjoyment. Qualitative analysis further showed that players evaluated the companion not only by its usefulness, but also by whether it felt like a tool, a teammate, or an integrated character in the game world. We categorised participants into four player types and summarised their expectations of AI companions. These findings provide design implications for AI companions as embodied participants in VR games.

---


### 113. [A Variational Optimal Transport Operator on Incompressible Flow](https://arxiv.org/abs/2609.13729)

**<font color=#1a73e8>作者：</font>** Jinjin He, Shenyifan Lu, Sinan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present the Variational Incompressible Optimal Transport (VIOT) operator, a generative neural operator for amortized incompressible density transport. Given a new source-target density pair, VIOT predicts a divergence-free velocity field and generates the full transport trajectory by feed-forward inference, replacing the hour-scale per-pair optimization used by adjoint fluid solvers and differentiable simulation baselines. The system consists of three components: a stream-function or vector-potential representation that enforces incompressibility by construction, a regularized incompressible transport objective that balances endpoint accuracy and flow smoothness, and a Fourier Neural Operator backbone that amortizes the solve across new pairs and grid resolutions. Together, these components make incompressible transport a reusable neural operator that facilitates various transport processes. Further, the generative capability extends beyond the training distribution, with VIOT producing incompressible transports for user-drawn source-target pairs in a real-time interactive system. We demonstrate VIOT on 2D and 3D density-transport benchmarks. Both 2D and 3D rollouts complete in seconds per pair, while per-instance baselines in our 2D comparisons optimize each new pair from scratch and require on the order of an hour, a roughly $10^4\times$ online speedup.

---


### 114. [JumpStart Your Policy Learning with Lessons from 160,000 Training Runs](https://arxiv.org/abs/2609.13730)

**<font color=#1a73e8>作者：</font>** Nabil Omi, Eric Bae, Chung Yik Edward Yeung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable progress in offline policy learning depends on careful reporting, well-tuned baselines, and evaluation across diverse conditions. Prior work has shown that results can be sensitive to reporting choices, hyperparameter tuning, and dataset properties, but these sources of variability have not been systematically investigated together at the scale needed to understand how they shape conclusions. To address this gap, we present a large-scale empirical study of offline reinforcement and imitation learning, training over 160,000 policies across 114 datasets. At this scale, no algorithm dominates: aggregate performance among the strongest methods is often close, but the leaders differ substantially across environments. We find that proper hyperparameter tuning frequently reshuffles perceived algorithm rankings and that benchmark composition can produce conflicting conclusions. We also study hyperparameter sensitivity and transfer across environments, identifying a simple strategy for deriving strong default configurations. We use our findings to develop a dataset-conditioned recommender that provides task-specific algorithm recommendations for practitioners. Finally, we release JumpStart: a resource suite containing every trained policy, per-model scores and hyperparameters, strong baselines across all environments, training and evaluation code, and an extensible website for retrieving, analyzing, and contributing results. Together, these resources aim to make offline policy-learning research more reliable and enable future work beyond the scope of this study.

---


### 115. [FFVO: A Feedforward Pose Decoder for Long-Horizon Visual Odometry](https://arxiv.org/abs/2609.13733)

**<font color=#1a73e8>作者：</font>** Meng-Li Shih, Shih-Yang Su, Yuliang Zou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stable and reliable 4D spatial understanding is fundamental for autonomous driving systems. While feedforward reconstruction networks can estimate camera motion and 3D structure in one pass, pose estimation over long videos remains challenged by computational cost, long-context ambiguity, and temporal instability. To address these challenges, we propose Feedforward Visual Odometry (FFVO), a pose-specialized adaptation of joint reconstruction architectures for efficient and temporally stable camera-pose estimation. FFVO uses (i) a compact camera-token representation for computationally efficient temporal aggregation, (ii) a hierarchical local-to-global temporal decoder that mitigates geometric ambiguity by separating short-range motion aggregation from sequence-level integration, and (iii) intermediate trajectory supervision that promotes temporal stability. Extensive evaluation on the Waymo Open Dataset (WOD), KITTI, and a large-scale proprietary benchmark demonstrates that our method performs favorably against existing feedforward approaches, and greatly reduces jitter and drift. These results support FFVO as an effective feedforward camera-pose decoder in long-horizon visual odometry settings.

---


### 116. [Development of Low-Cost Real-Time Driver Drowsiness Detection System using Eye Centre Tracking and Dynamic Thresholding](https://arxiv.org/abs/2609.13756)

**<font color=#1a73e8>作者：</font>** Fuzail Khan, Sandeep Sharma, M. R. Arulalan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One in every five vehicle accidents on the road today is caused simply due to driver fatigue. Fatigue or otherwise drowsiness, significantly reduces the concentration and vigilance of the driver thereby increasing the risk of inherent human error leading to injuries and fatalities. Hence, our primary motive being - to reduce road accidents using a non-intrusive image processing based alert system. In this regard, we have built a system that detects driver drowsiness by real time tracking and monitoring the pattern of the driver's eyes. The stand alone system consists of 3 interconnected components - a processor, a camera and an alarm. After initial facial detection, the eyes are located, extracted and continuously monitored to check whether they are open or closed on the basis of a pixel-by-pixel method. When the eyes are seen to be closed for a certain amount of time, drowsiness is said to be detected and an alarm is issued accordingly to alert the driver and hence, prevent a casualty.

---


### 117. [HyperProve: Answer-Guided Hypergraph Expansion for Multi-Hop Question Answering](https://arxiv.org/abs/2609.13768)

**<font color=#1a73e8>作者：</font>** An Nguyen Phu, Dung Nguyen Quang, Luu Hieu An 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop question answering often fails when retrieval treats evidence as isolated matches to the original question, since the facts needed to answer a complex question are usually connected through intermediate entities, relations, and constraints. We propose HyperProve, a retrieval-augmented QA framework that addresses this challenge by coupling question decomposition with answer-conditioned expansion over a hypergraph of atomic facts. HyperProve does not use atomic facts, hypergraphs, or iterative retrieval in isolation; instead, it carries intermediate answers and supporting hyperedges as retrieval state, then uses that state to bias the next local hypergraph expansion. This design enables HyperProve to construct coherent evidence chains for final answer generation while making the retrieval process stateful and fact-centered. Across multi-hop QA benchmarks, HyperProve achieves the best overall performance in our evaluation, outperforming the strongest baselines by an average relative improvement of 6.2% in answer accuracy and 4.9% in F1.

---


### 118. [Training Specialist Models without Reasoning Trajectories for Domain Expert Distillation](https://arxiv.org/abs/2609.13770)

**<font color=#1a73e8>作者：</font>** Yilei Tu, Zihao Li, Shaoxiong Ji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Specialist distillation effectively transfers domain expertise to student models via teacher-generated reasoning trajectories. However, when these specialists are trained solely on question--answer pairs without explicit reasoning supervision, what governs the trajectories they generate? In this work, we show that specialist optimization implicitly selects from this latent trajectory space. To isolate and observe this latent distribution, we leverage student distillation not as a downstream goal, but as an agnostic probe---since students inherit no parameterization or optimization constraints from the specialist, inheriting only the sampled trajectories themselves. Through this probe, our empirical analysis unveils a tight governing relationship: across 27 specialist--student pairings, their specialization--generalization profiles correlate exceptionally strongly. Crucially, explicitly controlling the specialist's distributional drift systematically shifts both the teacher and its distilled student along a controllable trade-off between domain precision and general-capability retention. Across chemistry, physics, and multilingual settings, distilled students systematically reflect these specialist-induced profiles, even across divergent model families. Our findings establish a new view of specialist training: when gold reasoning is absent, tuning choices directly control the latent supervision passed to downstream models.

---


### 119. [Homeostatic Continual Learning](https://arxiv.org/abs/2609.13771)

**<font color=#1a73e8>作者：</font>** Yue Jin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, I formulate a Continual Learning problem and propose a method named "Homeostatic Continual Learning" that enables an AI agent to learn continuously in a changing environment without catastrophic forgetting. The core of the method is to find outliers in the environment data when the agent experiences an outlier in its output. Through this method, the agent gradually completes its model and policy and performs well in more and more contexts. I also suggest that we may use the method to build a world model where the agent factorizes the objects in the world into features, abstract objects into comparable instances of concepts and map concepts to intents through features. I discuss the works needed to render the method practical, the connections to many fields in Artificial Intelligence and the broader implications of the method.

---


### 120. [GEAR: From Dynamic Encoding to Dynamic Activation in Social Trajectory Prediction](https://arxiv.org/abs/2609.13778)

**<font color=#1a73e8>作者：</font>** Jiaheng Chen, Jiaxing Li, Leixia Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human trajectory prediction requires modeling both individual motion patterns and social interactions among agents. Existing methods have made substantial progress by using attention mechanisms, graph structures, and temporal encoders to capture dynamic social context. However, most of them primarily focus on how social information is encoded, while paying less explicit attention to how the encoded social context should take effect during future trajectory generation. In this paper, we argue that dynamic social encoding does not necessarily imply dynamic social activation. The same interaction context may require different activation strengths across future horizons and scene densities: social cues should be strengthened when interaction evidence is strong, but suppressed when they are weak or noisy. To address this issue, we propose GEAR, a generation-aware bias activation model for human trajectory prediction. Built upon a bias-decomposed trajectory generation formulation, GEAR dynamically activates the individual-motion and social-resonance bias terms at each future step before final trajectory composition. This allows the model to explicitly control when and how strongly individual and social bias components participate in generation. Experiments on ETH-UCY, SDD, and NBA show that GEAR consistently improves the resonance-based baseline and achieves competitive state-of-the-art performance. Further analyses of activation patterns and density-grouped errors validate the importance of calibrating encoded social context during trajectory generation. Our code is available at this https URL.

---


### 121. [PQLN: Post-Quantum Security for the Bitcoin Lightning Network's Off-Chain Surfaces](https://arxiv.org/abs/2609.13781)

**<font color=#1a73e8>作者：</font>** Ahmet Kurt, Abdul-Salem Beibitkhan, Yacoub Hanna 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A cryptographically relevant quantum computer will break the elliptic-curve cryptography behind Bitcoin and its Lightning Network, the most widely used payment channel network. Even a post-quantum consensus upgrade of Bitcoin would not cover Lightning's off-chain surfaces, so its gossip, peer transport, invoices, payment onions, and offers need separate protection. An adversary can already record Lightning's encrypted traffic today and decrypt it once such a computer exists. Lightning can therefore move to post-quantum cryptography now, without waiting for Bitcoin, and stop such harvest-now-decrypt-later attacks along with node impersonation, invoice forgery, and payment deanonymization. In this paper, we propose PQLN, a hybrid post-quantum extension of Lightning that protects all of these surfaces with the lattice-based standards ML-DSA and ML-KEM. PQLN distributes post-quantum node identities through Lightning's gossip, hybridizes the transport handshake, adds post-quantum signatures to invoices, commits post-quantum keys in offers, and makes payment onions hybrid. Since post-quantum material is much larger than its elliptic-curve counterpart, we introduce techniques that fit it into Lightning's existing message formats and size limits. We analyze the security of PQLN against a quantum adversary and implement it in rust-lightning, a major Lightning implementation. Our evaluation with real Lightning nodes shows that PQLN nodes interoperate with unmodified nodes. The added cryptographic operations take at most 0.33 milliseconds, and the main cost is communication, since gossip data grows about tenfold with ML-DSA and about fourfold with the smaller Falcon. To our knowledge, PQLN is the first post-quantum design, implementation, and evaluation for Lightning.

---


### 122. [Partition Scores Are Not System Scores: Deployment-Fidelity Gaps in Decomposed Algorithm Selection](https://arxiv.org/abs/2609.13785)

**<font color=#1a73e8>作者：</font>** Jiachen Zhang, Yu Tang, Li Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Oracle-style quantities, including virtual best solvers, selected-portfolio VBS, virtual-best encodings, and best-in-family summaries, are widely reported as upper bounds on what a deployable selector could achieve. In decomposed algorithm selection, an analogous partition-level score grants an oracle choice of the best algorithm within the selected family; once the family selector is fixed, the deployable system must replace that within-family oracle with a learned within-family selector.
We define the deployment-fidelity gap G(R) as the difference between partition-level and deployable end-to-end utility and derive two accounting consequences: a per-instance margin-regret stability condition that tells us when a partition-time family choice is deployment-optimal, and a sharp partition-only identification interval that, when it strictly crosses zero, prevents the partition-level report from certifying the deployable winner.
Across five public algorithm-selection benchmarks spanning tabular AutoML and combinatorial CSP/SAT, every decomposed pipeline has positive G(R), ranging from 0.012 on TabZilla to 0.13 on PROTEUS-2014. Four of ten decomposed-versus-flat decisions have sign-changing point estimates; on PROTEUS-2014, a 33-point partition advantage shrinks to a 20-point end-to-end advantage. A training-side validation gap-correction diagnostic recovers the point-estimate deployable sign on all four sign-changing cells; it is a reporting aid, not a substitute for direct end-to-end evaluation. Partition and end-to-end scores should be reported side by side.

---


### 123. [What Makes a Great Co-Worker in an AI-Native Workplace?](https://arxiv.org/abs/2609.13786)

**<font color=#1a73e8>作者：</font>** Rudrajit Choudhuri, Max Meijer, Sam Yu-Te Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As knowledge work grows interdependent between humans and AI, we ask what makes a great co-worker in an AI-native workplace. To answer this, we conducted 22 interviews and a large-scale mixed-methods survey of 1,534 knowledge workers at a multinational technology company. We contribute BACI, a framework of 75 co-worker qualities that apply to humans and AI, spanning Benevolence, Ability, Cooperativeness, and Integrity. Comparing priorities for humans and AI identified 11 co-worker archetypes and revealed disagreement over whether AI should have warmth, take initiative, or own outcomes. We also show how priorities for these archetypes varied with workers' individual characteristics. Lastly, we contribute a taxonomy of AI work etiquette capturing the obligations co-workers expect of one another when preparing, sharing, and taking responsibility for AI-supported work. Based on these findings, we derive implications to inform worker-centric AI and workplace design.

---


### 124. [PPDL: A Real-world Industrial User Retention Ratio Forecasting Framework Integrating Physical Priors with Deep Learning](https://arxiv.org/abs/2609.13789)

**<font color=#1a73e8>作者：</font>** Zibo Zhao, Zhengxiong Guan, Chaoli Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multi-channel paid user acquisition, early and accurate prediction of user retention at the channel level is crucial for optimizing budget allocation. User retention curves display a pronounced temporal pattern: an initial period of high churn transitions into long-term stability. This pattern is further characterized by regular fluctuations attributable to seasonality and exhibits high serial autocorrelation. These intrinsic properties make such curves highly suitable for analysis within a time-series forecasting framework. However, forecasting user retention ratio for large-scale short-video platform faces three major challenges: significant heterogeneity across channels, pronounced global trend of decay followed by saturation, and short look-back windows. To address these challenges, we propose PPDL, a novel forecasting framework that integrates physical priors with deep learning. We first introduce a trend-residual decomposition component. The trend is modeled using the Weibull distribution, whose parameters are learned via a Multilayer Perceptron (MLP). Secondly, for the residual component, we design an auxiliary embedding module on top of a deep learning backbone to maintain the channel identity awareness. Finally, to enhance the model's sensitivity to trends, we design a Multiscale Trend-penalized loss function. The proposed approach PPDL is validated through comprehensive experiments on industrial-scale datasets, covering three applications with an average of 30+ channels each. Experimental results show that PPDL achieves improvements across different backbones and significantly outperforms existing online solutions.

---


### 125. [Restore What Matters: Lessons from Joint Restoration and Recognition](https://arxiv.org/abs/2609.13791)

**<font color=#1a73e8>作者：</font>** Lanqing Guo, Xijun Wang, Minchul Kim 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognition pipelines typically adopt a restore-then-recognize workflow, yet decades of experience show that generating visually pleasing images seldom translates to improved recognition. We propose a Joint Restoration-for-Recognition (JR$^2$) paradigm: restore only what downstream tasks truly require, with task signals dictating where, how much, and whether restoration is necessary. JR$^2$ rests on three pillars: (i) Physics, employing optics-accurate turbulence simulation, extensible to blur and noise, to ground restoration in real image formation; (ii) Neuroscience, drawing on selective attention and neuroplasticity to direct model capacity toward identity-critical regions and frames while bypassing already-clean inputs; and (iii) Vision & Learning, coupling recognition loss end-to-end through restoration and alignment so that low-level edits maximize high-level identity stability. Evaluations on IARPA-BRIAR show consistent improvements (e.g., TAR@0.01% FAR +0.6; FNIR@1% FPIR -2.5), while a quality gate skips ~70% of clean frames, reducing cost. Ablations confirm physics priors enhance realism, joint training prevents catastrophic forgetting, and selective restoration suffices in many cases. We conclude that better-looking images are neither necessary nor sufficient; restoration modules must be task-driven, selective, and physically aware. Code, pretrained models, and recipes are provided for integration.

---


### 126. [SyRHM: Symbolic-Language-Enhanced Reasoning with Associative Retrieval for Zero-shot Harmful Meme Detection](https://arxiv.org/abs/2609.13794)

**<font color=#1a73e8>作者：</font>** Hanling Wang, Chenlong Wei, Yingjuan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting harmful memes is critical for maintaining safe online communities. However, harmful intent is often implicit, arising from visual-textual incongruity and cultural stereotypes, which challenges existing multimodal detectors. We propose SyRHM, a framework that decomposes harmful meme detection into meaning-grounded retrieval and symbolic-language-enhanced multi-stage reasoning. SyRHM retrieves semantically related memes by parsing multimodal content into textual elements and descriptions, providing grounded context beyond surface-level similarity. Building on the retrieved context, SyRHM uses a translator stage to convert multimodal inputs into symbolic intermediate representations, and then performs multi-stage reasoning via planner and solver stages, enabling expressive and interpretable analysis of harmful intent. Experiments on FHM, HarM, and MultiOff demonstrate the effectiveness of SyRHM, achieving superior performance on most evaluation settings against multimodal and reasoning-based baselines, while providing reasoning traces for harmful content. The code is available at: this https URL

---


### 127. [Do Not Restart: Residual Completion for Stateful Agent Handoffs](https://arxiv.org/abs/2609.13800)

**<font color=#1a73e8>作者：</font>** Runzhi Deng, Yiming Zhong, Fang Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Routing and cascades reduce tool-agent cost by transferring control across models, but stateful handoffs must preserve accepted choices, realized effects, and unfinished obligations. We formulate this as commitment-constrained residual completion and introduce Commitment-Frontier Residual Completion (CFRC). CFRC enforces target-before-proposal, whole-proposal-before-authority, and live-evidence-before-success: it freezes a residual contract from accepted progress, closes the successor continuation into an evidence-linked graph, and admits execution only when the remainder is covered, with live receipts discharging obligations. We establish contract-relative partial correctness, which extends to the original residual request under complete contract construction. Across five environments and two same-provider model pairs, CFRC achieves comparable macro accuracy to strong full-task agents at only 22.0%-34.6% of their inference cost, with additional cross-provider results demonstrating broader transfer.

---


### 128. [Understanding the Limits of Agentic ICD Coding](https://arxiv.org/abs/2609.13806)

**<font color=#1a73e8>作者：</font>** Chong Yock Eng, Yushi Cao, Yiming Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ICD-10-CM codes are alphanumeric codes used in the US to classify diagnoses and injuries for medical billing and epidemiological reporting. Standard ICD-10-CM benchmarks report aggregate metrics that obscure performance on complex coding scenarios. We evaluate neural, workflow, and agentic systems on a rarity-stratified set of MIMIC-IV discharge summaries and identify two orthogonal failure modes. Neural classifiers exhibit a 0.43 micro-F1 gap between rare and common codes. Workflow systems handle rare codes well but score near zero on injury and external cause codes that require multi-step guideline following. A tool-augmented agentic configuration with structured access to official ICD-10-CM reference materials recovers up to 0.34 micro-F1 on this subset. No single system dominates across all conditions.

---


### 129. [Benchmarking Optimizers to Solve Inverse Problems with Differentiable Physics Simulators](https://arxiv.org/abs/2609.13819)

**<font color=#1a73e8>作者：</font>** Xiang Chen, Huanhuan Xia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving inverse problems with differentiable physics simulators holds the potential to revolutionize scientific discovery and engineering design, as it enjoys both the strict physical correctness from rigorous numerical physics simulators, and the high efficiency and effectiveness from automatic differentiation and gradient-based optimization. However, currently, this paradigm faces performance issues in optimization. In this work, we target benchmarking the performance of different optimizers to solve various inverse problems. We construct 12 differentiable physics simulators spanning physics domains including discrete mechanics, continuous mechanics, atomistic simulations, rendering, and semi-empirical physics models. Based on these simulators, we design corresponding inverse problems that can be categorized into parameter identification, inverse design, and optimal control. Finally, we conduct extensive experiments to compare the performance of different optimizers, including regular first-order methods, approximate second-order methods, as well as global optimizers, on these inverse problems, and analyze the results to provide insights on how to choose and design optimizers for differentiable programming. We hope such benchmarks can inspire the development of more effective optimizers, and further promote the applications of differentiable programming in various scientific and engineering domains.

---


### 130. [Semantic Privacy Protection with Utility Preservation for 3D Point Clouds](https://arxiv.org/abs/2609.13823)

**<font color=#1a73e8>作者：</font>** Jinchang zhang, Jiakai Lin, David Crandall 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud data face serious semantic privacy risks during acquisition, transmission, and cross-institutional sharing. Existing methods mostly rely on geometric perturbation or destructive encryption, which can reduce the recognizability of the original class but often impair downstream usability. This paper proposes a class-transfer-based semantic encryption framework for point clouds, aiming to conceal original class information while preserving task utility and supporting authorized recovery. Specifically, we construct a unified latent space with a shared-backbone Normalizing Flow, and combine LoRA and FiLM to achieve parameter-efficient class-conditional adaptation. We further introduce diffusion-guided flow alignment to regularize the latent distribution, construct an energy-based category transition graph, and obtain an optimal class-transfer table through global matching. Then, a latent-space Neural ODE continuously evolves source-class latents into target-class latents, which are decoded into target-class point clouds through the inverse flow. We adopt attacker-oriented metrics, including New-Class Recognition Rate (NCRR), Original-Class Leakage Rate (OCLR), and Original Label Recovery Rate (OLRR), to evaluate privacy and utility. Experiments on classification and segmentation benchmarks show that the proposed method achieves controllable semantic transformation, effectively reduces original-class semantic leakage, preserves downstream learnability in the protected domain, and supports reliable authorized reconstruction.

---


### 131. [ViperQ: Order Flow Pattern Recognition via Auction Market Theory for Reinforcement Learning Trading](https://arxiv.org/abs/2609.13825)

**<font color=#1a73e8>作者：</font>** Asser Moustafa, Rares-Mihail Neagu, Jugal Kalita  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning trading systems published in the academic literature overwhelmingly rely on price-aggregate state representations (OHLCV bars) or limit-order-book depth features, leaving microstructure pattern theories from the practitioner literature, namely Auction Market Theory and Market Profile, without a peer-reviewed computational instantiation. We present ViperQ, a reinforcement learning system whose state representation is built explicitly from Auction Market Theory primitives: Volume Point of Control, Value Area position, Low Volume Node flags, Cumulative Volume Delta divergence, and tape-velocity signatures, assembled into a 20-dimensional Z-normalised vector. Two Proximal Policy Optimisation agents are trained with a prospect theory-grounded asymmetric reward function that penalises losing holds at a magnitude consistent with Kahneman and Tversky's loss-aversion coefficient. Evaluated on a held-out twelve-month partition of institutional tick data the agents have never seen, ViperQ achieves +163.6% ROI on TSLA (-27.5% max drawdown, 27,019 trades) and +116.5% ROI on NVDA (-47.8% max drawdown, 12,892 trades) under zero leverage. The results establish Auction Market Theory features as a tractable structured input modality for sequential decision-making on financial time series and motivate further work on microstructure-aware policy learning.

---


### 132. [Graph Neural Networks for Influence Maximization in Social Networks: An Unsupervised Minimum Dominating Set Approach](https://arxiv.org/abs/2609.13836)

**<font color=#1a73e8>作者：</font>** Erfan Ahmadi, Mina Shirazi, Behnam Bahrak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Minimum Dominating Set (MDS) problem is a classic NP-hard combinatorial optimization problem with critical applications in social network analysis, including viral marketing, influence maximization, public health interventions, and information dissemination. Identifying a minimal set of influential individuals whose reach covers an entire social network is central to these applications, yet remains computationally challenging at scale. Graph neural networks (GNNs) have emerged as powerful tools for learning over graphs, and recent work explores their application to hard combinatorial problems. This paper presents a novel unsupervised GNN framework for the MDS problem that eliminates the need for ground-truth solutions during training. Trained on 12,000 synthetic graphs with diverse structural properties, our method achieves up to 55x faster inference than metaheuristic baselines and up to 14x faster inference than supervised learning approaches, while finding optimal or near-optimal dominating sets on real-world social network benchmarks. Our learned heuristic generalizes effectively to unseen graph distributions, demonstrating strong practical applicability for large-scale social network analysis.

---


### 133. [TotalSynth: Robust Whole-Body Synthetic CT from MRI and CBCT](https://arxiv.org/abs/2609.13838)

**<font color=#1a73e8>作者：</font>** Valentin Boussot, Cedric Hemon, Anais Barateau 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: To develop and evaluate TotalSynth, a reusable pretrained framework for whole-body synthetic CT (sCT) generation from MRI and cone-beam CT (CBCT) images. Materials and Methods: In this retrospective technical study, the dataset was assembled between 2020 and 2026 from SynthRAD challenge data, four prostate cohorts, and BIC-MAC. After registration quality control, 1450 of 1800 public challenge pairs were retained; 350 were excluded for insufficient registration quality or major source/CT mismatch. The corpus also included 84 additional prostate MRI/CT and 60 external BIC-MAC MRI/CT cases. Three 5-fold model families were evaluated with image-domain, anatomy-aware, registration-based, and uncertainty metrics. Age and sex were not consistently available across public datasets. Results: The released MRI-to-CT model achieved an overall MAE of 67.49 HU, SSIM of 0.920, and PSNR of 29.28 dB. The CBCT-to-CT model achieved an overall MAE of 53.55 HU, SSIM of 0.939, and PSNR of 32.09 dB. The unified model maintained similar performance on MRI inputs (MAE, 67.68 HU) and CBCT inputs (MAE, 54.22 HU). On external BIC-MAC data, MRI-to-CT MAE was 100.91 HU without fine-tuning and 62.21 HU after fine-tuning. Conclusion: TotalSynth provides reusable MRI- and CBCT-based CT synthesis models with broad anatomical coverage, while external evaluation highlights the need for local validation and optional fine-tuning under domain shift.

---


### 134. [Accuracy Is Not Service: A Decision-Aware Benchmark for Intermittent-Demand Forecasting](https://arxiv.org/abs/2609.13840)

**<font color=#1a73e8>作者：</font>** Joo Ern Chin, Shih-Fen Cheng, Aldy Gunawan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A contract-logistics spare-parts operator is paid on order-level service: an order counts only if every requested line is fulfilled, yet forecasters are selected based on line-level forecast accuracy. This disconnect matters when demand is intermittent and lumpy, histories are short, and lead times span months. We benchmarked 38 forecasting methods spanning classical, intermittent-demand, machine-learning, deep-learning, and pretrained foundation models. A common decision-aware protocol evaluates them on an industrial panel drawn from a live contract and two public datasets. Forecast-accuracy rank and order-service rank are negatively correlated on the industrial panel, at -0.555, across methods evaluated on 20,330 real multi-item orders. Service is more closely associated with the direction of cumulative forecast bias, including over-prediction during zero-demand periods, than with point accuracy. Examining bias in Chronos-2's instance normalization yields a training-free correction that lifts the per-material fill proxy from 77.5% to 92.0% (14.5 percentage points) at the 90% policy target and raises the complete-order fill rate from 54% to 63%. For reproducibility, we release RUF (Regenerate-Until-Fidelity), a method for generating fidelity-certified synthetic panels on which the findings reproduce. For intermittent demand, the lowest-error forecast need not deliver the highest service. Bias direction helps explain this gap, which can be reduced without retraining.

---


### 135. [Pre-training with Graph Transformers](https://arxiv.org/abs/2609.13844)

**<font color=#1a73e8>作者：</font>** Jiaming Wang, Thomas Laurent, Xavier Bresson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article investigates pre-training strategies for graph transformers in the biochemistry domain. By conducting comprehensive experiments, the study reveals that supervised pre-training using computed properties as labels provides the highest performance gain on downstream tasks. The results also highlight the importance of constraining model capacity to mitigate overfitting in graph transformers.

---


### 136. [Event-Level Emotion Recognition in the Wild Using Deep Facial Expression Analysis](https://arxiv.org/abs/2609.13854)

**<font color=#1a73e8>作者：</font>** Aleksandr Semerikov, Pakizar Shamoi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial emotion recognition (FER) in real-world environments remains challenging due to unconstrained imaging conditions, including multiple faces, occlusions, pose variations, and complex lighting. Most existing studies focus on individual facial emotion classification and do not address the analysis of collective emotional states at the event level. This paper proposes an end-to-end pipeline for event-level emotion recognition from photographs. The approach detects faces in each image, classifies facial expressions using a deep convolutional neural network, and aggregates face-level emotion probabilities to estimate the overall emotional distribution of a public event. A comparative evaluation of several CNN architectures on the FER- 2013 and RAF-DB datasets demonstrates that transfer learning with EfficientNet-B2 trained on RAF-DB is more suitable for real-world RGB data. The proposed method is evaluated on a real-world event dataset containing 1658 images. Experimental results show stable emotion distributions across event subsets, confirming the effectiveness of event-level aggregation for emotion analysis in the wild.

---


### 137. [ReH-FUSE: Reliability-Aware Hierarchical Fusion of Experts for Multimodal Emotion Recognition in Conversation](https://arxiv.org/abs/2609.13857)

**<font color=#1a73e8>作者：</font>** Guan-Hua Wen, Hou-Chiang Tseng, Kuan-Yu Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal emotion recognition in conversation (ERC) requires adapting to the instance-dependent reliability of different evidence sources. Lexical content may be decisive, vocal expression may provide complementary cues, or accurate recognition may require cross-modal interaction; fixed fusion does not explicitly account for this variation. We propose ReH-FUSE, a reliability-aware framework with dialogue-aware text, audio, and cross-modal experts. Its decision-level router first models the relative preference between text and audio and then balances the resulting unimodal mixture against the cross-modal expert. This factorization separates unimodal competition from cross-modal selection. Across three independent runs on IEMOCAP, ReH-FUSE achieves 74.34% weighted F1 and 73.11% macro F1; on MELD, it achieves 68.03% weighted F1. Controlled ablations show that learned routing outperforms uniform expert averaging and benefits from cross-modal interaction.

---


### 138. [An Uncertainty-Aware Hybrid Mathematical-Machine-Learning Model for Smart Irrigation Decision Support](https://arxiv.org/abs/2609.13864)

**<font color=#1a73e8>作者：</font>** Andrea Scariolo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agriculture accounts for roughly 70% of global freshwater withdrawals, yet irrigation is still commonly scheduled reactively, with no forecast of where soil moisture is heading and no statement of confidence in that forecast. Data-driven models are accurate but opaque and point-valued; water-balance models are transparent but carry large structural error. Neither alone supports a defensible irrigation decision under uncertainty. This study coupled the two and carried uncertainty through to the decision: a four-parameter water-balance core, calibrated on training data only, was corrected by a Random Forest that learned nothing but the physical residual, conformal prediction attached 90%-nominal intervals, and a risk-aware rule converted the interval lower bound into an irrigation trigger. It was evaluated on three years of hourly in-situ measurements from a rainfed Mediterranean cropland station under a strict chronological split, scored against persistence, from one hour to one week. At the 24 h horizon the hybrid reached RMSE 0.00925 m^3 m^-3 and +9.4% skill, roughly double the best of nine baselines, of which only the Random Forest beat persistence. Skill did not grow with lead time: it peaked at +27.4% at three hours and fell to +1.2% at one week. Conformalised quantile regression was better calibrated and 11% sharper than constant-width conformal prediction. The risk-aware rule raised management-threshold crossings detected in advance from 0.905 to 1.000, at a precision cost of 0.975 to 0.950 and 3.7% more notional water, and beyond 72 h the point forecast fell below the no-forecast rule while the interval-based rule did not. Uncertainty quantification therefore governs the lead time over which forecast-driven irrigation advice remains trustworthy, and here transparency in the physical layer cost no measurable accuracy.

---


### 139. [Bangla Sentence Function Classification: Corpus Development, Model Benchmarking, and Interpretability](https://arxiv.org/abs/2609.13869)

**<font color=#1a73e8>作者：</font>** Swapnil Kundu Argha, Abdullah Al Shafi, Rowzatul Zannat 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic sentence function identification is important for many downstream natural language processing (NLP) applications such as dialogue systems, text-to-speech synthesis, and machine translation. However, benchmark resources for Bangla sentence function classification remain limited. To mitigate this gap, this paper introduces a corpus of 10,000 Bangla sentences, manually annotated into four functional categories, namely declarative, interrogative, imperative, and exclamatory. The corpus is nearly balanced across the four classes, with high annotation reliability reflected by a Fleiss\' Kappa of 0.82. Furthermore, we evaluate multiple feature representations, including Bag-of-Words (BoW), TF-IDF, and Word2Vec, with several classical machine learning classifiers. In addition, two heterogeneous ensemble models, namely Single-Level Ensemble (SLE) and Double-Level Ensemble (DLE), are utilized to improve classification performance. Experimental results show that TF-IDF consistently outperforms Word2Vec, likely due to its ability to emphasize discriminative lexical cues associated with sentence functions, particularly given the relatively small corpus used to train Word2Vec. The DLE model with TF-IDF features achieves the best performance with accuracy and macro-F1 of 0.95, demonstrating the effectiveness of sparse lexical representations and heterogeneous ensemble learning for this task. Further cross-validation confirms the robustness of the approach, while LIME-based interpretability provides insights into model predictions. The developed corpus and model benchmarking establish strong baselines for Bangla sentence function classification.

---


### 140. [Learning How Much to Collaborate: Difficulty-Aware Topology Selection for Multi-Agent Code Generation](https://arxiv.org/abs/2609.13890)

**<font color=#1a73e8>作者：</font>** Yunsong Hong  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems for code generation are deployed with a single communication topology, chosen once for every problem. This is the wrong granularity. Evaluating five topologies on 614 problems from APPS, HumanEval+ and LiveCodeBench, we find that the advantage of hierarchical collaboration over a single agent grows from 2.4 points of pass@1 on the easiest third of problems to 21.1 points on the hardest third, while its token cost stays about ten times higher. We propose the Difficulty-Aware Topology Selector (DATS), which predicts each topology's probability of solving a problem and selects the one maximising predicted success minus cost. Its predictor is a graph network that treats the five topologies as nodes of a connectivity order rather than independent labels, worth 1.7 points over a flat multi-label head. Because the cost penalty is a single scalar recalibrable without retraining, routers compare at equal spend: under this budget-matched protocol six cost-aware methods span 21.6 percentage points, and two baselines leading DATS fall behind once calibrated to it. Fixed at 40% of the always-hierarchical cost, DATS reaches 77.7% pass@1 against 73.6% (always-hierarchical) and 74.3% (strongest learned competitor), all eleven pairwise McNemar comparisons surviving Holm-Bonferroni correction. The 4.1-point gain holds across four backbones spanning fourteen points of capability, and replacing the 39 interpretable features with a graph network or a pretrained encoder shifts accuracy by at most 1.3 points, never significantly. A cross-domain study on 400 mathematical reasoning problems reproduces the effect, the gap widening from 2.5 to 20.9 points.

---


### 141. [SkyAnchor: Updating Metric-scale Aerial 3D Gaussian Scenes from Unposed Ground-View Sequences](https://arxiv.org/abs/2609.13903)

**<font color=#1a73e8>作者：</font>** Zhuoxiao Li, Xinyi Liu, Taoyu Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study how to update a pre-built aerial scene with a newly captured, unposed ground-view sequence. The aerial scene already contains a reliable metric Structure-from-Motion (SfM) reconstruction and a pre-trained 3D Gaussian Splatting (3DGS) model, whereas the ground-view sequence is collected later to add street-level appearance but has unknown camera poses and global scale. Registering this sequence to the aerial SfM reconstruction is challenging because single-image cross-view localization is brittle and long trajectories are prone to drift. To address these challenges, we present SkyAnchor, which treats the existing aerial scene as a fixed scaffold for ground-view registration and scene update instead of jointly reconstructing aerial and ground imagery from scratch. It first localizes short groups of consecutive ground frames against geometrically verified aerial support, producing sparse anchor poses. It then recovers the full ground trajectory with anchor-constrained submaps, fixing the front and rear anchor poses during incremental registration and bundle adjustment. Finally, it inserts filtered ground Gaussians while preserving the aerial view, followed by lightweight joint refinement. Experiments on seven real aerial--ground scenes show accurate metric ground trajectories and updated 3D Gaussian scenes with strong aerial- and ground-view rendering quality.

---


### 142. [Phorecaster365: A Human-Supervised Reference Architecture for Hybrid Pharmaceutical Sales Forecasting and Planning Decision Support](https://arxiv.org/abs/2609.13907)

**<font color=#1a73e8>作者：</font>** Houman Kazemzadeh, Kamyar Naderi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pharmaceutical sales forecasts inform planning across products, regions, and distribution channels, yet their interpretation depends on inventory availability, transaction semantics, product lifecycle, and the information available when each forecast is issued. A model prediction alone does not preserve these conditions or establish whether a forecast is suitable for operational use. We present Phorecaster365, a human-supervised reference architecture that connects enterprise resource planning data to reviewable pharmaceutical sales forecasts. The architecture separates source ingestion, product-region series construction, temporally valid feature generation, statistical and machine-learning modeling, ensemble formation, uncertainty assessment, planner review, and lifecycle governance. Its central intermediate representation is a forecast context package that preserves the source snapshot, forecast target, temporal cutoff, available covariates, data-quality state, and hierarchy version. A corresponding forecast evidence package links predictions to model and calibration versions, exceptions, human adjustments, and publication history. Development experience with a synthetic panel of 10,950 daily records across 30 product-region series informs the design. Historical experiment summaries are retained only as descriptive evidence of development because their evaluation does not establish independent predictive validity. We specify a rolling-origin evaluation protocol, baseline and ablation requirements, uncertainty and robustness assessments, and a staged pathway from synthetic testing to use in governed planning. The contribution is an implementation-neutral system design and validation framework; the report does not establish real-world forecasting accuracy, comparative superiority, or operational benefit.

---


### 143. [Machine Learning under Imperfect Data: Challenges and Methods](https://arxiv.org/abs/2609.13914)

**<font color=#1a73e8>作者：</font>** Masoumeh Zareapoor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning models are commonly developed under an assumption that training and test data are sufficiently complete, balanced, labelled, and drawn from compatible distributions. In practice, one or more of these conditions is often violated. Measurements may be missing or corrupted, rare classes may be poorly represented, supervision may be weak, and the deployment environment may differ from the training environment. These imperfections are usually treated as separate technical problems, although they alter learning through a small number of shared mechanisms: loss of information, biased empirical risk, ambiguous supervision, and unstable representations. This short survey organises representative methods around these mechanisms. It reviews reconstruction and generation, rebalancing and representation calibration, learning with limited supervision, adaptation across domains and modalities, and reliability under distribution change. The discussion highlights the limits of plausible reconstruction, benchmark-specific correction, and adaptation without trustworthy feedback. It concludes with directions for evidence-aware learning, uncertainty-preserving prediction, and evaluation that separates visual plausibility from decision utility.

---


### 144. [Learning Through Energy Refinement and Manifold Projection: A Cooperative EBM-AE Framework](https://arxiv.org/abs/2609.13917)

**<font color=#1a73e8>作者：</font>** Ryad Zemouri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy-Based Models (EBMs) provide a flexible framework for generative modeling by learning an energy landscape that assigns low energy values to realistic samples and higher energies to unlikely observations. Despite their theoretical appeal, training EBMs remains challenging due to the computational cost of Langevin sampling and the difficulty of efficiently exploring the learned data manifold. In this work, we propose a cooperative Energy-Based Model and Autoencoder (EBM-AE) framework that combines energy-based refinement with manifold projection. The proposed approach jointly trains an EBM with a denoising autoencoder and introduces an iterative EBM$\rightarrow$AE$\rightarrow$EBM sampling procedure in which Langevin dynamics and autoencoder projection alternately refine generated samples. Within this framework, the autoencoder acts as a manifold projection operator that regularizes sampling trajectories, while the EBM performs energy-based refinement toward low-energy regions of the learned distribution. Extensive experiments conducted on the MNIST dataset demonstrate that joint EBM-AE training substantially improves generation quality compared with a conventional autoencoder.
Beyond unconditional generation, we evaluate the proposed framework on image inpainting tasks involving structured and random masks. The results show that manifold projection provides the majority of the reconstruction capability, whereas the final energy-based refinement becomes increasingly beneficial as the reconstruction problem becomes more challenging.
Taken together, the results indicate that combining manifold projection and energy minimization provides an effective and interpretable framework for generation, reconstruction, and out-of-distribution detection, while offering new insights into the complementary roles of energy-based modeling and representation learning.

---


### 145. [Finite-Time Node Separation in Recurrent Graph Neural Networks with Persistent Gaussian Perturbations](https://arxiv.org/abs/2609.13920)

**<font color=#1a73e8>作者：</font>** Mostafa Haghir Chehreghani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Persistent Gaussian perturbations have been shown to prevent asymptotic oversmoothing in recurrent Graph Neural Networks (GNNs) by ensuring a positive stationary Dirichlet energy. However, this global energy bound does not guarantee that individual node representations remain distinct at finite depths. In this paper, we provide a complementary finite-time analysis of the same persistent-noise architecture. Let \(d\) denote the representation dimension and \(\sigma\) the noise standard deviation. We first prove an exact second-moment decomposition for the expected squared distance between any two node representations, yielding the universal lower bound \(2\sigma^2 d\) at every positive time step without contraction or stationarity assumptions. More precisely, conditional pairwise distances have a noncentral chi-square characterization: the noncentrality parameter is the deterministic message-passing separation normalized by \(2\sigma^2\). This yields dynamics-aware fixed-time and finite-horizon near-collision bounds that retain information discarded by the central worst-case analysis. The earlier central Gaussian bound is recovered as the worst-case zero-separation case. We additionally prove almost-sure pairwise noncollision, derive a uniform finite-horizon guarantee, and establish permutation equivariance in distribution for the stochastic dynamics and permutation-invariant graph outputs. Our results complement the asymptotic energy analysis of prior work and provide rigorous finite-time guarantees on node-level representation separation.

---


### 146. [Minibatch persistency, eight years later: what batch reuse costs in steps and joules, and what it saves in data](https://arxiv.org/abs/2609.13922)

**<font color=#1a73e8>作者：</font>** Matteo Fischetti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Minibatch persistency reuses data instead of reading it: rather than drawing a fresh minibatch at every optimizer step, it takes K consecutive steps on the same one. Absorbed into data echoing in 2019, it has carried one objection -- that reuse merely imitates a larger learning rate -- and no baseline tuned as carefully as the method itself. This paper runs the missing test. A pre-registered study trains a 49M-parameter Transformer on FineWeb-Edu at minibatch size B in {32, 128, 512}, 8 seeds per cell, tuning the learning rate separately for every batch size and every arm, against a reuse-free control that changes the sampling and nothing else. Each headline claim is a cost to reach a fixed loss, read on four axes: optimizer steps, fresh tokens, seconds, and joules at the socket. We then replicate on new seeds and a newer GPU generation, and put the three arms on one schedule in steps. The outcome of our study is that what minibatch reuse buys is neither speed nor energy but data, and only at large minibatch size: at B = 32 it reads more fresh tokens than the baseline, not fewer. On steps, seconds and joules it is at best free; and at B = 512, where it looks best, a registered control cannot separate the effect of reuse from the position on the learning-rate schedule at n = 8 seeds. The technique is therefore worth using where fresh data rather than compute is the binding cost: a corpus that runs out, a pipeline that pays per sample, a stream that cannot be rewound. Where the data can simply be read again, spaced epochs do as well or better.

---


### 147. [Exploring napping paradigm for Recurrent Spiking Neural Networks](https://arxiv.org/abs/2609.13927)

**<font color=#1a73e8>作者：</font>** Andreas Massey, Stefano Nichele, Aliaksandr Hubin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological organisms minimize free energy by balancing two competing demands on their internal world model: it must be accurate enough to predict sensory input, yet simple enough to generalize beyond it. Two mechanisms regulate this balance offline: sleep reduces complexity through gradual synaptic downscaling, while stochastic noise attenuates precision, relaxing the constraint sensory input imposes on synaptic reorganization. Engineered Spiking Neural Networks (SNNs) leave this balance unaddressed, favoring instantaneous, noiseless weight normalization instead. This paper investigates the hypothesis that a biologically inspired micro-sleep paradigm, napping -- combining proportional weight scaling with continuous stochastic membrane activity -- can replicate the stability of normalization while shedding model complexity. We evaluate this in an unsupervised recurrent SNN trained via trace-based spike-timing-dependent plasticity (STDP) on Gabor-preprocessed MNIST. We tune napping across three regularization regimes by sweeping its duration and membrane noise level, then compare the best configuration against weight normalization. Across all three regimes, well-tuned napping matches the accuracy of normalization: accuracy peaks at brief durations and low noise, then declines monotonically as either grows. Clustering diverges, with the strongest geometric separation arising at longer durations and higher noise -- the two terms of free energy pulling apart, accuracy rewarding data fit and structure rewarding the simpler representation that gradual, noisy downscaling induces. This gain carries a simulation cost normalization avoids, so napping is most compelling where representational structure, rather than raw classification efficiency, is the priority.

---


### 148. [Enforcement of In-Kernel Stateful Security Policies via eBPF](https://arxiv.org/abs/2609.13930)

**<font color=#1a73e8>作者：</font>** Letterio Galletta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many attacks against workloads running on multi-tenant systems are multi-step and history-dependent: sequences of innocuous operations whose malicious nature emerges only over an execution trace. Defending against them requires security policies that are stateful, are enforced within the kernel, and have a precise semantics. Currently deployed proposals fail on at least one count: kernel's built-in syscall filtering and classical MAC frameworks are stateless, while current eBPF-based tools express their policies through ad hoc YAML rules that cannot capture temporal relations among events, and whose semantics is defined only by the implementation.
We present BPFence, an in-kernel runtime-verification framework that satisfies the properties above. BPFence provides a policy language with a formal semantics that can express temporal relations among events. It also provides a type system that statically distinguishes events the kernel can control from those it can only observe. Every well-typed policy is compiled into a finite-state monitor proved correct with respect to its semantics, and then into eBPF programs that run inside the kernel. We evaluate BPFence on seven case studies drawn from real-world attack patterns, and on a set of micro- and macro-benchmarks to show that the enforcement overhead remains compatible with production deployment.

---


### 149. [Optimal Transport for Efficient, Unsupervised Anomaly Detection on Industrial Data](https://arxiv.org/abs/2609.13940)

**<font color=#1a73e8>作者：</font>** Abigail Langbridge, Fearghal O'Donncha, James T Rayfield 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective anomaly detection frameworks are a central pillar of the Industry 4.0 paradigm. In this paper, we introduce an Optimal Transport (OT)-based framework for anomaly detection, designed to detect deviations from normal behaviour in time-series sensor data. The OT-based method requires minimal user input and adapts to real-time data without the need for labelled training data. Our method effectively addresses existing limitations related to data labelling, generalisability, and scalability, demonstrating resilience against short-term fluctuations, noise, and data gaps - common challenges in industrial environments. Additionally, our method provides counterfactual explanations improving the auditability of the approach when deployed in industrial settings. The proposed method learns the mapping between normal and observed operating conditions through a sliding reference window that adapts to the dynamicity of the data. We evaluate our approach on three industrial datasets, from shipping, industrial HVAC systems, and publicly available benchmark data. The method was highly effective in identifying anomalies and reducing false positives, outperforming traditional methods, while maintaining computational efficiency and ease of configuration.

---


### 150. [BLInD: Learning Driver Intent as a Distribution over Future Ego Trajectories](https://arxiv.org/abs/2609.13941)

**<font color=#1a73e8>作者：</font>** Flavian Pegado, Ronit Hire, Shreyas Rajesh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present BLInD (Blind Learned Intent Distribution), a compact network that maps recent vehicle-state history (e.g. speed, curvature, indicator, and vehicle type) to a top-k distribution of future ego trajectories, with no camera, LiDAR, map, or object-track inputs. We find that vehiclestate history alone is sufficient to learn a useful multimodal distribution over near-term ego trajectories, and its low-latency nature makes it well-suited for safety-critical deployment. We investigate two distribution architectures, autoregressive (AR) and flow-matching, and train on both mixed-platform opensource and Wayve datasets. Both generalize without datasetspecific adaptation; the flow-matching model achieves best topk ADE/FDE of 0.15/0.37 m on Wayve, 0.15/0.36 m on Waymo, and 0.28/0.59 m on nuScenes, with the AR model reaching comparable coverage. Integrating the distributions into an AEB trigger task, a strict all-candidates policy reduces false positives from 1.51% to 0.11% with AR (13.7x reduction, 94.9% TP) and to 0.06% with flow-matching (25.1x reduction, 98.7% TP) compared to a 1-CTRV policy with 100% true positive score. BLInD runs in 0.87 ms with the AR head and 2.9 ms with the flow-matching head on an NVIDIA DRIVE Orin ECU making it compatible with real-time deployment on automotive ECUs. While existing learned distribution models rely on scene context and blind vehicle-state models typically collapse to a single path, BLInD is learned, blind, and cross-domain simultaneously, a combination not demonstrated by prior work. These results show that such a distribution provides a controllable and plausible intent sampling interface for downstream systems, with AEB as one instantiation.

---


> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-416](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
