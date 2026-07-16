# 📦 其他研究 | 2026年07月17日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-202](./part-05.md)

---

### 101. [CDS: Counterfactual Directionality Score for Structured Interventions in Spatial Graphs](https://arxiv.org/abs/2607.13508)

**<font color=#1a73e8>作者：</font>** Humaira Anzum, Md Ishtyaq Mahmud, Jagan Mohan Reddy Dwarampudi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantifying directional influence between node populations is a fundamental problem in graph-based modeling, particularly in spatial biological systems where cell-cell interactions shape functional outcomes. Existing approaches based on attention, attribution, or correlation capture associations but do not provide a principled framework for evaluating directional effects under controlled perturbations. We introduce a framework for structured counterfactual interventions in graph-based models to estimate directional influence between node types. Our approach trains a Neighbor Influence Model (NIM) to predict node states from local neighborhoods and applies constrained interventions that modify neighborhood composition while preserving key spatial and structural properties. We define the Counterfactual Directionality Score (CDS), which measures the change in predicted node state induced by targeted perturbations, and provide a theoretical interpretation of CDS as a finite-difference measure of local intervention sensitivity. To obtain valid uncertainty estimates, we introduce a core-level bootstrap procedure that accounts for dependencies within spatial samples. Experiments on synthetic spatial graphs with known directional structure show that CDS recovers directional influence, remains well calibrated under null conditions, and is robust to confounding signals, while preliminary results on spatial transcriptomics data reveal biologically plausible and consistent interactions across tissue cores.

---


### 102. [DriveFace: A Cross-Spectral Through-Glass Face Dataset for On-the-Move Vehicular Border Control](https://arxiv.org/abs/2607.13515)

**<font color=#1a73e8>作者：</font>** Anjith George, Luis Luevano, Alain Komaty 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The continuous growth in cross-border mobility places increasing pressure on existing border control infrastructures, motivating on-the-move biometric authentication, in which travellers are identified directly inside their vehicles at checkpoints. Face recognition is well-suited to this setting, as it can be acquired passively and at a distance. Its development, however, is hindered by the lack of representative datasets: existing benchmarks are collected in controlled environments and do not capture the challenges inherent to vehicular acquisition, including motion blur, variable illumination, occlusions, and cross-spectral enrollment. To address this gap, we introduce a dataset for on-the-move face recognition in border-control scenarios, comprising NIR vehicle-crossing videos paired with smartphone-based pre-enrollment data. Baseline evaluations with state-of-the-art models show clear performance limitations under these realistic conditions, highlighting the need for dedicated methods to advance the field.

---


### 103. [VGIF-Score: Interpretable and Diagnostic Evaluation of Spatio-Temporal Instruction Following in Video Generation](https://arxiv.org/abs/2607.13527)

**<font color=#1a73e8>作者：</font>** Songyu Xu, Xin Wang, Qiang Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video generation models (VGMs) have made substantial progress in visual fidelity, yet their ability to follow long, compositional instructions remains insufficiently evaluated. Existing evaluation protocols often rely on prompts that are short and semantically shallow, with limited atomic constraints and weak spatio-temporal dependencies. They also frequently depend on costly human evaluation or handcrafted vision pipelines, while providing little diagnostic insight into which instruction constraints succeed or fail. To address this gap, we propose VGIF-Score, a highly automated and interpretable framework for evaluating instruction following in video generation. VGIF-Score consists of two complementary components: an objective completion branch that parses prompts into a Spatio-Temporal Directed Acyclic Graph (ST-DAG) and performs dependency-aware QA with short-circuit diagnostics, and a subjective satisfaction branch that uses instruction-conditioned AutoRubric to assess cinematography, visual purity, motion smoothness, and physics adherence. Together, these components produce a unified score that captures both objective completion and perceptual satisfaction. We instantiate this framework on VGIF-Bench, a benchmark of 223 long, structurally entangled prompts paired with approximately 4.3K fine-grained evaluation items. Experiments on 14 proprietary and open-source VGMs across more than 3K generated videos show that VGIF-Score provides reliable, interpretable, and diagnostically useful evaluation of video generation instruction following. The code will be available at this https URL.

---


### 104. [When T2I Synthetic Data Backfires: Amplified Privacy Risks in Real-Synthetic Mix Training](https://arxiv.org/abs/2607.13541)

**<font color=#1a73e8>作者：</font>** Na Li, Boyu Kuang, Hongsheng Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> To overcome data scarcity and privacy constraints in data collection, it has become standard practice across academia and industry to augment real training data with text-to-image (T2I)-generated synthetic data, a paradigm we term Real-Synthetic Mix-Training (RSMT). While substituting synthetic data for sensitive real samples is widely regarded as a means to mitigate privacy exposure of the substituted data, the risk to the remaining real samples that actively participate in training has remained largely unexamined.
This work reveals, for the first time, that RSMT can substantially amplify privacy leakage of these real training samples. We establish a theoretical framework, RSMT Memorization Amplification, proving that incorporating synthetic data displaces real samples toward peripheral regions of the mixed feature space, in turn forcing the model to memorize them more aggressively. Guided by this foundation, we propose RSMixLeak to systematically assess this risk through membership inference attacks (MIAs). RSMixLeak comprises two variants depending on the adversary's capability. The non-adversarial variant audits a benign RSMT pipeline with an honest T2I provider, establishing a lower bound on the leakage induced by the intrinsic gap between real and T2I-generated data. The adversarial variant considers an adversary who controls the T2I model or contributes crafted data to the T2I provider, and deliberately enlarges this distributional gap on a target class via either high-level semantic attribute binding or imperceptible pixel-level coating, further amplifying leakage on real training data while improving downstream model utility. Motivated by these findings, we further propose a lightweight leakage propensity indicator computable from real data alone that reliably identifies high-risk datasets unsuitable for entering RSMT, as a self-assessable mitigation.

---


### 105. [Clustering algorithms for multivariate wind farm SCADA data filtering](https://arxiv.org/abs/2607.13544)

**<font color=#1a73e8>作者：</font>** Nicolò Italiano, Vasilis Pettas, Tuhfe Göçmen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> During wind farm operation, Supervisory Control and Data Acquisition (SCADA) systems record numerous anomalies, transients, and specific operational modes, leading to large datasets. However, for a wide range of applications, only measurements corresponding to normal operation are required and, therefore, the SCADA data must be filtered. For this purpose, several methods have been proposed to automate and replace manual filtering conducted by experts via visual inspection of the data. In this paper, we compare the filtering accuracy of multiple clustering algorithms against manual filtering, introducing evaluation metrics that are suitable for unlabeled data and robust across potential applications. Based on the results, we provide recommendations for generalizing model calibration to different datasets and discuss potential use cases for each model. The models are applied to the SCADA data of three turbines of an existing offshore wind farm, using 10-minute statistics across multiple data channels. In addition to the anomalies and operational modes typically recorded, the dataset presents a large number of non-evident outliers due to several field tests. Overall, the results highlight the importance of extending the analysis beyond the power curve, both in feature selection and in the design of evaluation metrics. In most cases, cluster-based methods are able to detect both evident and subtle outliers, achieving higher accuracy than manual filtering. However, the accuracy and the amount of data retained vary considerably depending on the model, and expert involvement remains necessary, though to a reduced extent compared to manual filtering.

---


### 106. [From Novice to Expert: Cost-Aware Bandits for Evolving Worker Performance in Crowdsensing](https://arxiv.org/abs/2607.13546)

**<font color=#1a73e8>作者：</font>** Yin Huang, Qingsong Liu, Jie Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile crowdsensing (MC) recruits mobile users to perform sensing tasks using their smartphones, enabling large-scale applications such as traffic monitoring and environmental sensing. A fundamental challenge is online worker recruitment under uncertainty, where the platform must learn workers' sensing performance while operating with a limited budget. Existing learning-based MC recruitment methods typically assume that each worker's sensing quality is stationary with a fixed mean over time. In practice, however, worker performance often improves with experience and eventually stabilizes, while the incurred sensing cost can be unknown in advance due to time-varying device and context states. In this paper, we study a budget-constrained online recruitment problem in which the platform selects one worker in each round, observes the sensing quality and incurred cost, where the expected sensing quality of each worker increases with experience and eventually converges to a plateau, and repeats until the budget is exhausted. We formulate this problem as a structured bandit model where each worker's expected reward evolves according to an unknown increasing-then-converging function of its participation count, and each worker has an unknown expected cost. We develop a cost-aware online learning framework that jointly learns evolving reward trajectories and heterogeneous costs, detects performance saturation, and allocates the limited budget to maximize long-term sensing utility. We provide theoretical performance guarantees and validate the proposed approach through extensive experiments, demonstrating consistent improvements over baselines that ignore experience-driven dynamics or assume known costs.

---


### 107. [How Far Can Root Cause Analysis Go on Real-World Telemetry Data?](https://arxiv.org/abs/2607.13548)

**<font color=#1a73e8>作者：</font>** Athira Gopal, Ashwanth Krishnan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying root causes in production microservice failures requires reasoning over large-scale, multimodal telemetry spanning metrics, logs, and traces, a problem that has proved resistant to both classical and LLM-based approaches. The OpenRCA dataset exemplifies these challenges: it is large-scale, multimodal, and lacks detailed domain knowledge, and yields consistently low accuracy across all existing methods. We show that classical causal discovery methods and existing LLM-based multi-agent systems fail to reliably identify root causes on this benchmark, and present a Structured Multi-Agent RCA pipeline that substantially outperforms existing LLM-based and classical baselines, supporting both domain-knowledge and knowledge-free operating modes. To diagnose where failures originate, we introduce a reverse reasoning agent that, given the correct answer, identifies which signals in the extracted anomalies support it and determines whether Stage~1 had access to those signals, classifying each failure as Reasoning Gap (evidence present but unused) or Data Ambiguity (evidence genuinely absent). This analysis reveals that the required evidence is present in the vast majority of failures: the bottleneck is not data access but the agent's ability to reason over it correctly. We further introduce an automated rule mining pipeline that systematically extracts discrimination rules from reverse reasoning reports, reducing reliance on manual knowledge curation. Across all configurations, model reasoning capability and domain knowledge are the primary constraints: stronger models embed more domain expertise, and explicit knowledge injection partially compensates for this gap. Reasoning performance remains practically bounded even when evidence extraction is perfect: scaffold engineering and better data pipelines alone cannot close this gap; progress requires improvements at the model level.

---


### 108. [Multivariate Cryptography-Based Anonymous Certificate Scheme](https://arxiv.org/abs/2607.13554)

**<font color=#1a73e8>作者：</font>** Abel C. H. Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As quantum computing technology continues to mature, the US National Institute of Standards and Technology (NIST) has outlined a migration timeline for Post-Quantum Cryptography (PQC), recommending the deprecation of certain elliptic curve cryptography (ECC) by 2030. Furthermore, privacy-sensitive application scenarios, such as vehicular communications, require the use of anonymous certificates. However, existing anonymous certificate schemes are still largely based on ECC. Therefore, this study proposes a multivariate cryptography-based anonymous certificate scheme, aiming to design quantum-safe anonymous certificates suitable for privacy-sensitive application services. The proposed multivariate cryptography-based anonymous certificate scheme is supported by rigorous mathematical proofs and illustrated with computational cases.

---


### 109. [Multi-Agent Collaborative Reasoning with Tool-Augmented Evidence for Urban Region Profiling](https://arxiv.org/abs/2607.13558)

**<font color=#1a73e8>作者：</font>** Xixuan Hao, Yutian Jiang, Jiabo Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban region profiling constitutes a core problem in urban computing, supporting applications such as population estimation, economic assessment, and environmental monitoring. Existing methods typically formulate this task as multimodal representation learning, fusing heterogeneous urban data, e.g., satellite imagery, points of interest, textual descriptions, and 3D building information, into latent embeddings for prediction. However, these approaches are largely correlation-driven, assume cross-modal consistency, and rely on static pipelines, which limit their robustness in heterogeneous or unseen urban regions. We propose UrbanAgent, an agentic framework that reframes urban region profiling as a reasoning-driven inference problem. UrbanAgent instantiates an independent agent for each data modality and performs structured multi-agent collaborative reasoning to explicitly address cross-modal inconsistencies rather than absorbing them into a single representation. In addition, UrbanAgent extends indicator prediction as a closed-loop process of active evidence acquisition and iterative reasoning, enabling agents to verify uncertain inferences through tool-augmented retrieval of external knowledge optimized via reinforcement learning. Extensive experiments on global urban datasets for Carbon emissions, GDP, and Population estimation show that UrbanAgent consistently outperforms existing baselines, achieving an average improvement of 8.1% in R2, and exhibiting strong generalization performance in unseen-city settings.

---


### 110. [AI advice suppresses people's willingness to say "I don't know", even when the advice is wrong and accuracy is incentivized](https://arxiv.org/abs/2607.13562)

**<font color=#1a73e8>作者：</font>** Chiara Marcoccia, Walter Quattrociocchi, Valerio Capraro  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowing when to say "I don't know" is fundamental to human judgment, yet AI assistants offer a fluent answer to almost any question. In five experiments (N = 3,132; four preregistered, one direct replication), participants answered difficult questions and could always decline to respond. We engineered the questions so that AI advice was wrong, separating AI use from its accuracy. Merely having access to AI nearly eliminated participants' willingness to suspend judgment, and this held whether the advice was actively requested or simply displayed. Consequently, participants answered more questions but were correct about a third as often as when AI was unavailable-yet their confidence nearly doubled. Incentivizing accuracy and penalizing inaccuracy led participants to seek and follow AI advice less, answer more accurately, and suspend judgment more often, though still far less than when AI was unavailable. As AI suggestions grow ubiquitous and unsolicited, they may not simply affect answer accuracy; they may even alter the metacognitive threshold at which people decide whether they know enough to answer.

---


### 111. [Nexus: Native Mesh Generation with Diffusion](https://arxiv.org/abs/2607.13563)

**<font color=#1a73e8>作者：</font>** Hanxiao Wang, Ying-Tian Liu, Yuan-Chen Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating high-quality triangle meshes is essential for film, gaming, and interactive 3D applications. Mainstream methods rely on mesh serialization and autoregressive processes, which stuggles in effective inference and is sensitive to error accumulation. In this paper, we present Nexus, a diffusion method that achieves holistic mesh generation via decoupled vertex and topology generation. First, we view mesh vertices as sparse voxels organized as an octree and adopt a diffusion model to generate the vertices in a coarse-to-fine manner. Second, for topology modeling, we propose Spacetime Interval, as an extension of Spacetime Distance to encode arbitrary edge and face topology into continuous per-vertex embeddings. It allows for a global and efficient recovery of complex topology. We then employ a diffusion model to generate the continuous embeddings on the generated vertices. Extensive experiments on the Objaverse and Toys4K datasets and in-the-wild images demonstrate that our method outperforms state-of-the-art autoregressive and two-stage baselines, effectively circumventing the inherent limitations of sequential mesh modeling. A blind user study from 3D practitioners confirms strong perceptual preference for our results.

---


### 112. [UTS at ELOQUENT 2026 Voight-Kampff: structural shifts in AI writing bypass state-of-the-art detectors](https://arxiv.org/abs/2607.13565)

**<font color=#1a73e8>作者：</font>** Dima Galat, Marian-Andrei Rizoiu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We investigate which language model evasion attacks survive state-of-the-art adversarial fine-tuning, developing strategies that sweep the top 5 positions on the ELOQUENT 2026 Voight-Kampff leaderboard. While adversarial fine-tuning trivially closes the 2025 winning evasion recipes, we uncover a fundamental asymmetry in detector vulnerability: pushing generated text out of the detector's training distribution reliably defeats adversarial detection, whereas pulling it into the distribution (e.g., mimicking human training data) fails completely. Exploiting this, we introduce two novel out-of-distribution attack families - cross-decade register attacks and modernist stream-of-consciousness form. Both strategies easily bypass adversarial closure, achieving up to approximately 50x higher fool rates than previous methods while preserving naturalness. Furthermore, experiments show that the obvious deployer countermeasure (augmenting training data with period prose) fails to close the vulnerability. Our findings show that the tested detector families, including adversarially fine-tuned ones, exhibit persistent vulnerabilities under structural out-of-distribution shifts, a mechanism that directly powers our leading competition performance.

---


### 113. [GHR-VLM: Making Zero-Shot Transit Video Analytics Realizable with Grounded Hybrid Reasoning](https://arxiv.org/abs/2607.13569)

**<font color=#1a73e8>作者：</font>** Kaicong Huang, Weiheng Oh, Ruimin Ke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transit video understanding can provide valuable fine-grained data that conventional passenger counters and fare systems cannot capture. However, supervised video models require task-specific annotations, while applying vision-language models (VLMs) directly to long onboard videos is unreliable and costly. To leverage the complementary strengths of both approaches, we propose GHR-VLM, a visual grounded hybrid reasoning framework for zero-shot transit-bus video analytics. It is motivated by the observation that explicit visual grounding can improve VLM reasoning by converting long surveillance streams into compact, passenger-centered spatiotemporal evidence. Specifically, we propose an edge-cloud design in which a lightweight edge-based monitor continuously tracks door status and segments passenger clips. A backend VLM then identifies boarding passengers and classifies payment behavior through a two-stage coarse-to-fine refinement of spatiotemporal evidence. By invoking the VLM only on grounded passenger clips and contact sheets, GHR-VLM reduces cloud inference, avoids payment-specific training data, and supplies the localized evidence that VLMs otherwise struggle to identify. Evaluation on 486 minutes of real-world bus surveillance video demonstrates the potential of grounded edge-cloud reasoning for passenger-level payment analytics while highlighting the challenges posed by degraded video conditions.

---


### 114. [Structured Reinforcement Learning for Bayesian Persuasion : Application to Intelligent Interactive Driving](https://arxiv.org/abs/2607.13576)

**<font color=#1a73e8>作者：</font>** Merlin Paul, Anup Aprem  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interactive driving, wherein an intelligent lead vehicle equipped with real-time traffic data coordinates route choices of connected vehicles, offers a promising approach to dynamic traffic management. To address the challenge of harmonising decisions, this paper considers the strategic information revealing framework of Bayesian persuasion. Here, the principal (lead vehicle) aims to guide the agent's (connected vehicle) partially observable sequential decision making towards its own objectives by selectively revealing information, such as real-time traffic ahead, using signals. However, the agent's farsighted response to maximize its long-term reward, renders the principal's signaling strategy design computationally challenging. We propose an online structured reinforcement learning framework to synthesize computationally efficient signaling strategy which is persuasive for a far-sighted agent. The main contributions of the paper are as follows: (i) For a monotonic agent with approximate best response, we propose MAPL, a structured policy learning algorithm for faster online learning, (ii) Identification of sufficient conditions for the supermodular structure of the Q function of the principal for a monotonic agent, (iii) Identification of sufficient conditions to ensure the persuasiveness of the principal's signaling strategy, (iv) Supermodular Q learning for Principal (SQP), which leverages the supermodular structure of principal's action value to synthesize computationally efficient signaling strategy that is persuasive for a monotonic learning agent, (v) Numerical analysis considering a real-time application of Bayesian persuasive driving for lane selection demonstrates that the proposed method is 30% cost efficient for optimising travelling rewards of both the lead and connected vehicle compared to the existing methodologies for signaling strategy design.

---


### 115. [UniPhysGen: Unified Physical Grounding for Simulation-Ready 3D Assets](https://arxiv.org/abs/2607.13586)

**<font color=#1a73e8>作者：</font>** Xian Li, Rong Wei, Lujie Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physically grounded 3D assets are increasingly important for embodied AI and robotic simulation. However, most existing 3D assets lack unified physical semantics, including articulation semantics and intrinsic physical properties, required for realistic interaction. Current approaches either treat these semantics independently or rely on canonicalized object structures, limiting robustness across heterogeneous 3D assets. We present UniPhys, a scalable framework for automatically transforming raw 3D assets into simulation-ready assets with unified physical semantics. Based on UniPhys, we construct UniPhys-40K, a large-scale physically grounded dataset, together with UniPhys-Bench, a carefully verified benchmark for unified physical grounding evaluation. We further introduce UniPhysGen, a unified physical grounding model that jointly reasons over articulation semantics and intrinsic physical properties. UniPhysGen incorporates geometry-robust articulation grounding to mitigate geometric shortcut bias under heterogeneous part decompositions. Extensive experiments demonstrate state-of-the-art performance across articulation grounding and intrinsic physical property estimation tasks, while the resulting assets can be directly deployed in robotic simulation environments for realistic physical interaction. Our code and dataset will be available at this https URL.

---


### 116. [SAFETY SENTRY: Context-Aware Human Intervention via EXECUTE-ASK-REFUSE Routing](https://arxiv.org/abs/2607.13594)

**<font color=#1a73e8>作者：</font>** Tianyu Chen, Chujia Hu, Wenjie Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents act on real-world environments through tool calls, and a single misjudged action can cause irreversible harm. The standard safeguard is a guard model that labels each proposed action as safe or unsafe, but this binary view conflates two distinct decisions: whether the action is harmful in itself, and whether it is appropriate given the user's context. It also operates at the granularity of action categories rather than individual instances, producing routine interruptions that erode autonomy and train users to wave through the most consequential alerts. We reframe the problem as a per-instance three-way routing decision over {EXECUTE, ASK, REFUSE} and instantiate it with Safety Sentry, a lightweight guard model whose inference reduces to a single decoding call. A single decoding-time threshold lets one fixed checkpoint be re-positioned across deployments of differing risk tolerance without retraining. Safety Sentry outperforms a broad set of open-weight and frontier closed-source baselines on overall accuracy and safety-related recall, while controlling both directional error rates simultaneously.

---


### 117. [Equilibrium stability as a driver of cooperation among Q-learners](https://arxiv.org/abs/2607.13607)

**<font color=#1a73e8>作者：</font>** Janusz M. Meylahn, Maximilian Schäfer  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Algorithmic collusion among pricing algorithms has raised concerns about sustained supra-competitive prices and their implications for social welfare. Existing work has largely focused on the probability that reinforcement-learning algorithms converge to cooperative strategies, typically under the assumption that exploration vanishes over time. Motivated by the observation that algorithms deployed in practice are likely to continue exploring in order to remain adaptive to changing environments, we study learning dynamics under constant exploration. In this setting, the relevant question is no longer whether an algorithm converges to a particular strategy profile, but rather what fraction of time the algorithms spend playing cooperative strategies. Even in the benchmark case of the repeated Prisoner's Dilemma with one-period memory, this yields high-dimensional stochastic learning dynamics, for which a complete analytic treatment is intractable. We show that cooperative strategies can be dominant in this time-averaged sense and derive a boundary predicting when such dominance arises, based on the expected dynamics of the Q-learning process. Extensive simulations show that this boundary is a strong predictor for non-defection-dominated behaviour under epsilon-greedy Q-learning.

---


### 118. [Gauge-Invariant, Parameter-Insensitive Regularization for Potential Recovery from Flow on Directed Graphs](https://arxiv.org/abs/2607.13609)

**<font color=#1a73e8>作者：</font>** Mohammad Forouhesh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering a latent potential from observed flow on a directed graph (a discrete Poisson problem with Dirichlet boundaries) is ill-posed, and the standard fix backfires: ridge regularization shrinks toward a gauge-meaningless origin, collapsing and reversing the recovered ordering ($+0.81\to-0.42$ rank correlation against a planted ground truth). The gauge-invariant graph Dirichlet energy removes the hazard and delivers parameter-insensitivity: the estimate is stable across four orders of magnitude in $\lambda$, whereas ridge inverts the ordering for every $\lambda>0$. We prove the reduced solve is SPD and preserves dynamic range exactly where ridge collapses it, and localize absorbing boundaries from flow alone via a Poisson residual. The $H^1$ seminorm is classical; what is new is the gauge diagnosis, the parameter-insensitivity it buys, and an ablation showing the result is robust to the extraction method. On three public clickstream corpora the gauge-invariant estimate retains $28$--$41\%$ of the interior dynamic range while ridge collapses to as little as $0.2\%$. The same gauge invariance carries into graph neural networks -- neutralizing the constant mode per layer prevents the oversmoothing that collapses a deep directed GCN -- linking this classical inverse problem to a central question in graph learning.

---


### 119. [FastCentNN: Accelerating Centroid Neural Network with Entropy Proxy](https://arxiv.org/abs/2607.13613)

**<font color=#1a73e8>作者：</font>** Le-Anh Tran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Centroid neural network (CentNN) is an unsupervised competitive learning algorithm in which centroid splitting is triggered only after strict local stabilization, often leading to prolonged low-movement training phases before model expansion. This report proposes FastCentNN, an accelerated variant that addresses this inefficiency by introducing an early splitting strategy based on the total centroid movement per epoch, which serves as a training entropy proxy. As a result, FastCentNN reduces unnecessary reassignment epochs while preserving the original winner-loser learning dynamics. FastCentNN supports both absolute and stage-relative movement thresholds, allowing the splitting criterion to remain either fixed or adaptive throughout training. Experiments on some benchmark datasets show that FastCentNN consistently achieves clustering quality comparable to CentNN while reducing runtime by up to 16% on synthetic 2D datasets and about 5% on high-dimensional datasets. FastCentNN therefore provides a practical and efficient drop-in replacement for CentNN, retaining its online adaptive learning behavior while offering a simple and interpretable speed-stability trade-off through configurable splitting thresholds.

---


### 120. [Extending Liquid Rank Toward Multi-Source Reputation Aggregation](https://arxiv.org/abs/2607.13615)

**<font color=#1a73e8>作者：</font>** Nejc Znidar, Anton Kolonin  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In this paper, we present an extension of liquid rank reputation systems that enables the aggregation and blending of multiple heterogeneous reputation sources into a unified reputation score. The proposed framework supports the incorporation of external reputational signals alongside internally generated reputation, allowing influence to reflect participation and contribution across multiple contexts and subsystems. By introducing explicit weighting and blending mechanisms, the model provides fine-grained control over the relative impact of individual reputation sources, making it adaptable to diverse governance and coordination scenarios involving both human and machine agents. The resulting approach extends existing liquid rank systems and offers a flexible foundation for designing reputation-based governance mechanisms in complex socio-technical environments.

---


### 121. [UESF-Bench: Benchmarking and Probing for Unified Embodied Seeking and Following](https://arxiv.org/abs/2607.13621)

**<font color=#1a73e8>作者：</font>** Kun Yu, Jianhua Yang, Yixiang Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-guided human following is an important capability for embodied agents, but existing benchmarks typically assume that the target person is visible at the start of an episode. This setting simplifies the problem and overlooks a more realistic requirement: an agent often needs to first find a language-described target and then persistently follow that target in a dynamic environment. While recent work has started to study human search, existing settings are typically evaluated in task-specific scenarios and often rely on stronger prior knowledge of the environment. Moreover, they usually treat searching and following as separate tasks and still lack a unified benchmark for systematic evaluation. To address these limitations, we introduce the Unified Embodied Seeking and Following Benchmark (UESF-Bench), a large-scale and diverse benchmark for embodied human seeking and following. The benchmark requires agents to handle semantic-guided exploration, reliable behavior switching and recovery, and delayed identity grounding. To this end, we propose SeekFollow-VLA, a vision-language-action framework with a task-driven routing mechanism for latent phase inference and transition modeling between seeking and following. Experimental results show that SeekFollow-VLA achieves clear improvements over both single-head and dual-head baselines across single-person and multi-person environments, establishing a baseline for unified embodied seek-and-follow.

---


### 122. [How the Hessian-Spectrum of Neural Networks Depends on Data](https://arxiv.org/abs/2607.13631)

**<font color=#1a73e8>作者：</font>** Jasraj Singh, Enea Monzio Compagnoni, Antonio Orvieto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Hessian matrix is an important quantity of interest when it comes to studying the loss landscape and optimization dynamics in deep learning, as well as designing measures of generalization, second-order learning algorithms, etc. Prior works have focused on empirical results or pursued a theoretical treatment under overly simplified settings. In this work, we derive the eigenvalues of the Hessian of linear networks with arbitrary widths and depths, and datasets with an arbitrary number of samples, features, and labels. Importantly, for classification tasks with MSE loss, we identify that the sharpness of the solution is directly related to the maximum proportion of samples belonging to any class. We empirically validate our predictions and systematically analyze the effects of shedding the impractical assumptions one at a time, as well as incorporating nonlinearities. We observe that our predictions are considerably robust in most cases, allowing us to extend our conclusions to more practical learning setups.

---


### 123. [OvisOCR2 Technical Report](https://arxiv.org/abs/2607.13639)

**<font color=#1a73e8>作者：</font>** Shiyin Lu, Yinglun Li, Yu Xia 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce OvisOCR2, a 0.8B document parsing model. OvisOCR2 is designed as an end-to-end parser: given a document page image, it generates a Markdown representation in natural reading order, covering text, formulas, tables, and visual regions. We build a data engine that combines filtered real-document annotations with synthetic pages whose rendered images and Markdown targets are derived from the same HTML source. The training recipe includes supervised fine-tuning, reinforcement learning on a 4B branch with a multi-component reward design, on-policy distillation into the 0.8B model, and model fusion. On OmniDocBench v1.6, OvisOCR2 achieves a state-of-the-art overall score of 96.58, placing an end-to-end model at the top of this leaderboard previously dominated by pipeline methods and highlighting the potential of end-to-end document parsing. On PureDocBench, OvisOCR2 also achieves the highest Avg3 score of 75.06. Beyond these two public benchmarks, we evaluate OvisOCR2 on an in-house benchmark designed to cover a broader set of long-tail and challenging scenarios. OvisOCR2 obtains the best overall performance among the compared methods, providing further evidence of its generalization and robustness. OvisOCR2 is available at this https URL.

---


### 124. [WarpGuard: Towards Control-Flow Attestation for Heterogeneous CPU-GPU Execution](https://arxiv.org/abs/2607.13640)

**<font color=#1a73e8>作者：</font>** Christian Lindenmeier, Meni Orenbach, Amro Awad 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Heterogeneous CPU-GPU workloads are increasingly used in safety-critical embedded systems, yet no existing approach provides joint attestation of their execution. Prior Control-Flow Attestation (CFA) techniques focus on CPU-side CFA, while GPU attestation is limited to static, load-time verification and does not provide runtime guarantees. As a result, runtime attacks on GPU kernels and violations of the CPU-GPU interaction contract remain unaddressed. We present WarpGuard, the first composite CFA framework for heterogeneous CPU-GPU workloads. WarpGuard verifies execution against a unified control-flow graph (CFG) that captures both CPU and GPU components. It extends prior CFA techniques in two ways: it enables runtime CFA of GPU kernels by tracing their execution against kernel-specific CFGs, and it monitors kernel launch events and enforces per-call site policies to detect violations at the CPU-GPU boundary. These extensions address challenges arising from GPU parallelism and cross-device interactions. We implement WarpGuard using software-based instrumentation, requiring no specialized hardware or binary modifications. Our evaluation on an NVIDIA Jetson Orin Nano shows that WarpGuard detects GPU-side control-flow and cross-boundary attacks. Across microbenchmarks, SPECAccel, and eight TensorRT inference workloads, WarpGuard incurs moderate overheads, suggesting practicality for embedded safety-critical settings.

---


### 125. [Consensus as Privileged Context for Label-Free Self-Distillation](https://arxiv.org/abs/2607.13643)

**<font color=#1a73e8>作者：</font>** John Gkountouras, Josip Jukić, Ivan Titov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling multiple solutions and returning the majority answer is among the most reliable ways to improve the reasoning accuracy of large language models without labels, and a growing family of methods converts this consensus signal into training supervision. However, existing approaches use consensus only in restricted forms: as a filter that selects solutions for fine-tuning, as a preference between answers, or as a scalar reward for reinforcement learning, discarding most of the information that the agreeing solutions contain. We present CANON (Consensus-ANchored self-distillatiON), a label-free training method that turns consensus into dense, token-level supervision. For each unlabeled prompt, CANON samples multiple solutions, extracts the majority answer, and conditions a frozen snapshot of the model on a solution that reaches it; this consensus-anchored teacher then supervises the model on its own rollouts at every token. Experiments on mathematical and scientific reasoning benchmarks show that CANON improves pass@1 by up to 12 points, outperforming label-free reinforcement learning by 6 points at a seventh of its compute and approaching a teacher conditioned on gold solutions; trained on pooled unlabeled data, it transfers to held-out benchmarks, matching training methods that use gold labels. Analysis suggests that the improvements are not pure distribution sharpening: after training, the model solves problems it previously never solved in 32 attempts, and its majority vote itself becomes more accurate.

---


### 126. [Human4K: A Large-Scale 4K Multi-View Mocap Dataset for Whole-Body 3D Human Reconstruction](https://arxiv.org/abs/2607.13646)

**<font color=#1a73e8>作者：</font>** Tianshun Han, Ziyu Shi, Lijian Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D human reconstruction have improved overall performance, yet current models still fail in the most challenging real-world scenarios. They often produce unstable geometry, inaccurate limb articulation and unreliable predictions under depth ambiguity or self-occlusion. A key reason is that existing datasets still lack the combination of high-resolution images, high-precision annotations and diverse whole-body motions required to support robust reconstruction. To address this gap, we present Human4K, a large-scale 4K multi-view whole-body human reconstruction dataset with mocap-accurate SMPL-X annotations. Human4K contains over six million 4K images captured by an eight-view high-resolution camera system synchronized with a professional Vicon motion capture setup, covering 11 subjects performing complex, highly articulated and strongly self-occluded full-body motions. All sequences are processed by a Motion-Retargeting and Refinement Module (MRRM) to ensure precise alignment for the full body and extremities. Experimental results show that training with Human4K consistently improves whole-body reconstruction on standard benchmarks, with particularly large gains for hands, feet and depth-ambiguous limb configurations.

---


### 127. [Beyond Color Geometry: Evaluating Human-Like Color Representations in Vision Models](https://arxiv.org/abs/2607.13647)

**<font color=#1a73e8>作者：</font>** Ayan Igali, Pakizar Shamoi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Do vision models see colors the way humans do? Existing evaluations of color representations usually compare them with geometric spaces such as CIELAB or with discrete color labels. These references capture perceptual distance or category membership, but not the graded way in which people organize colors. We evaluate color grounding against a fuzzy perceptual model with 86 graded categories fitted to human survey data. The framework can be applied to any image encoder and measures three complementary properties: category boundaries, category compactness, and graded alignment beyond what color geometry alone can explain. Across eleven Vision Transformer encoders, the category-level results are broadly similar, whereas graded alignment differs substantially. Masked Autoencoders achieve the strongest beyond-geometry alignment, with confidence intervals that do not overlap those of the other encoders. A layer-wise analysis further shows that masked reconstruction preserves this structure toward the output. On natural images, MAE represents surface color globally, while language-supervised models encode color more strongly in relation to the foreground object. These results show that human-like color grounding has several distinct aspects that should not be reduced to a single score.

---


### 128. [Maximally Robust Satisficing Bayesian Optimization](https://arxiv.org/abs/2607.13652)

**<font color=#1a73e8>作者：</font>** Samuli Kinnunen, Petrus Mikkola, Antti Niskanen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many design tasks can be cast as black-box function optimization, enabling use of Bayesian optimization to find an ideal design with minimal number of trials. However, often we do not actually need the optimum but instead a sufficiently good solution is enough, for instance a material that is durable enough for its intended use. In most cases there are multiple satisfactory solutions, forming a superlevel set of the function, raising a key question of which one to prefer. We answer this by explaining why robustness to input perturbations that may occur when the solution is deployed is a good criterion and by introduce a Bayesian optimization method that efficiently finds satisficing solutions that are robust to maximally large perturbations. In contrast to previous works, we assume the inputs can be accurately controlled during optimization, but will be perturbed after the deployment.

---


### 129. [Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation](https://arxiv.org/abs/2607.13653)

**<font color=#1a73e8>作者：</font>** Boyu Mi, Mengchen Ma, Yifei Yao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world deployment of embodied agents requires active exploration, visual grounding, and interactive intent disambiguation. However, existing frameworks often rely on privileged simulator states or assume complete instructions, bypassing realistic deployment challenges. To bridge this gap, we present REAL, an agentic framework for open-world mobile manipulation. REAL establishes sim-to-real-consistent environment APIs without oracle perception and integrates a simulated user to enable human-in-the-loop interaction. Within this environment, we design diverse task compositions to drive data collection, supervised fine-tuning, and online reinforcement learning, systematically optimizing agent performance. To comprehensively evaluate this approach, we introduce REAL-Bench, a benchmark spanning 241 tasks across active exploration, visual distraction, articulated manipulation, and interactive disambiguation.
Experimental results demonstrate that our trained agent outperforms leading commercial closed-source VLMs on interactive tasks with a 56.9% success rate. Further empirical analysis reveals that our hierarchical training pipeline successfully aligns the model's tool-use capabilities while maintaining robust open-vocabulary reasoning under extended exploration horizons. Finally, we deploy and evaluate our framework on a physical dual-arm mobile robot, where it achieves a 78.3% end-to-end success rate over 60 real-world episodes. These physical trials demonstrate robust zero-shot transferability to unseen household scenarios, validating that our sim-to-real-consistent design successfully bridges the reality gap for long-horizon mobile manipulation. Code is available at this https URL.

---


### 130. [T3HG-Editor: Text-driven 3D Human Garment Editing with Body Priors Embedded in SMPL-X](https://arxiv.org/abs/2607.13654)

**<font color=#1a73e8>作者：</font>** Shaoru Sun, Xingtao Wang, Zihan Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Gaussian Editing (3DGE) has seen substantial progress, text-driven 3D human garment editing remains largely underexplored. Existing 3DGE works typically follow a paradigm that applies 2D editing techniques to multi-view rendered images and updates 3D Gaussians based on the modified images. Extending such methods to 3D human garment editing suffers from low-fidelity outcomes, caused by introduced distortions and garment inconsistencies. A promising breakthrough opportunity arises from the SMPL eXpressive (SMPL-X) model that embodies rich prior information for virtual humans. Motivated by this insight, we propose a text-driven 3D human garment editor termed T3HG-Editor, which delivers high-fidelity and garment consistent results by leveraging geometry and joint priors embedded in SMPL-X. Specifically, T3HG-Editor contains three stages, namely obtainment of editable Gaussians, garment consistent editing, and Gaussian updating with overflow pruning. The obtainment of editable Gaussians begins with seeding Gaussians along SMPL-X normals to generate sufficient near surface Gaussians, followed by a 2D mask constraint that precisely localizes the target Gaussians to be edited. The garment consistent editing aggregates tokens corresponding to the same SMPL-X vertex across multiple views and propagates them to their original views, enforcing garment consistency without requiring additional training. Gaussian updating with overflow pruning employs a Signed Distance Function (SDF) defined on SMPL-X to construct a human distance field, which is then integrated with a 2D semantic mask to prune overflowing Gaussians, thus preventing contamination of non-target regions. Experiments on multiple subjects and diverse garment types demonstrate that T3HG-Editor outperforms state-of-the-art methods in both editing quality and garment consistency.

---


### 131. [Explaining Reinforcement Learning Agents via Inductive Logic Programming](https://arxiv.org/abs/2607.13655)

**<font color=#1a73e8>作者：</font>** Celeste Veronese, Edoardo Zorzi, Daniele Meli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explainable Reinforcement Learning (XRL) seeks to make Reinforcement Learning (RL) policies more transparent and interpretable, a key requirement in safety-critical and human-centric scenarios. However, it is mostly based on user studies, thus targeting the needs of a specific audience and lacking shared evaluation metrics. On the other hand, logic-based approaches within eXplainable Artificial Intelligence (XAI) provide compact, human-readable abstractions of decision-making. However, the systematic quantification of the explainability degree of logical representations remains an open problem. This work aims to advance the state of the art in XRL by introducing objective and planning-oriented metrics for policy explainability in RL settings. At the same time, it contributes to the field of logic for XAI by providing a principled way to quantify the explainability of logical rules, moving beyond common-sense assessments and simple propositional fragments. We employ Inductive Logic Programming (ILP) to extract symbolic representations of RL policies and define a novel set of explainability metrics, including activation rate, feature coverage, syntactic distance and semantic distance. These metrics quantify alignment between symbolic rules and agent behavior, the role of features in decision-making, and the evolution of policies during training and across agents in single and multi-agent RL. Experiments across different RL domains show that the proposed metrics highlight action-specific learning dynamics beyond global return, provide fine-grained insights into domain features beyond classical approaches for global feature importance estimation, and uncover coordination, specialization, and adaptation patterns in MARL. Moreover, they provide crucial insights for the transfer and generalization of action-specific policies.

---


### 132. [FreeLit: Paired-Free Indoor Relighting via Physics-Guided Diffusion](https://arxiv.org/abs/2607.13656)

**<font color=#1a73e8>作者：</font>** Chi-En Yen, Duy-Khanh Ngo, Wen-Wei Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-based indoor scene relighting remains challenging due to the complex interplay between cluttered geometry and local illumination, requiring precise modeling of light position, color, and intensity. Existing data-driven methods implicitly learn this relationship via paired multi-illumination datasets. Nevertheless, this data is costly and fails to scale, which is essential for accurate light-source-level control. Conversely, inverse-rendering methods reduce the data dependency by incorporating physical priors; however, they lack the robustness of intrinsic estimation in challenging conditions.
In this paper, we present FreeLit, a paired-free framework for controllable indoor relighting that explicitly manipulates light-source location, color, and intensity. Instead of relying on paired supervision, we construct a physics-guided illumination prior from intrinsic scene properties, generating a structured lightmap along with a pseudo-relit image to guide diffusion-based synthesis. To address instability in intrinsic estimation, especially in low-light scenes, we introduce a relighting-guided intrinsic stabilization strategy that enforces illumination-invariant reflectance through structure-aware distillation and consistency constraints. Furthermore, we propose controllability-oriented evaluation metrics to quantify alignment with user-specified illumination color and intensity. Experimental results demonstrate that FreeLit achieves stable, physically consistent, and controllable relighting, with improved robustness in low-light indoor scenes, without requiring paired supervision.

---


### 133. [The Hyperspherical Geometry of CLIP Latent Space: A Semantic Mixture Model](https://arxiv.org/abs/2607.13660)

**<font color=#1a73e8>作者：</font>** Zijie Yu, Gaowen Liu, Ramana Rao Kompella 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive Language-Image Pretraining (CLIP) representations form a semantic embedding space governed by cosine similarity, reflecting an intrinsic hyperspherical geometry. However, existing probabilistic interpretations typically rely on Gaussian assumptions, which fail to capture this directional and multimodal structure. We propose a principled density model for the CLIP latent space based on Mixtures of von Mises-Fisher (MovMF) distributions defined on the unit hypersphere. Using the Expectation-Maximization (EM) algorithm, we efficiently learn a probabilistic model in which each mixture component corresponds to a coherent semantic concept. This formulation yields a closed-form likelihood naturally aligned with hyperspherical geometry, enabling accurate and interpretable density estimation. Empirically, our model significantly improves long-tailed and out-of-distribution detection and provides a natural semantic decomposition, representing each embedding as a sparse probabilistic combination of interpretable concepts. These results suggest that CLIP latent space is more faithfully characterized as a hyperspherical semantic mixture rather than an isotropic Gaussian, establishing a simple and geometrically consistent probabilistic framework for modeling and understanding multimodal representations. Project page is available at this https URL.

---


### 134. [Learning Speaker Identity Beyond Language and Modality Constraints: Insights from the POLY-SIM 2026 Challenge](https://arxiv.org/abs/2607.13669)

**<font color=#1a73e8>作者：</font>** Marta Moscati, Muhammad Saad Saeed, Marina Zanoni 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal speaker identification systems typically assume the availability of complete and homogeneous audio-visual modalities during both training and testing, and assume each speaker only speaks a single language. However, in real-world applications, such assumptions often do not hold. Visual or audio information may be missing due to occlusions, camera or microphone failures, or privacy constraints. Multilingual speakers introduce additional complexity due to linguistic variability across languages. These situations constitute substantial challenges for the robustness and generalization capabilities of multimodal speaker identification systems. Aim of the POLY-SIM 2026 challenge is to address these aspects of speaker identification and to provide a standardized setup for the comparison of the proposed solutions.

---


### 135. [WAVE-Stereo: Warp-Aligned Volume Encoding for Stereo Matching](https://arxiv.org/abs/2607.13674)

**<font color=#1a73e8>作者：</font>** Zehan Liu, Yage He, Xianwu Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing iterative stereo matching methods primarily adopt two types of correspondence representation: explicit matching search via correlation volumes and local residual refinement via warped features, yet the two remain separately modeled. We propose WAVE-Stereo, built on a core insight: correlation volumes and feature warping provide complementary matching cues. \textbf{GeoWarp Correspondence Encoder (GWCE)} encodes matching search, residual alignment, and disparity prior in parallel at the ConvGRU input. To mitigate matching degradation in textureless regions, we propose \textbf{Periodic Global Context Propagation (PGCP)}, which propagates global spatial information in a periodic manner. On five real-world benchmarks -- Middlebury, ETH3D, KITTI 2012, KITTI 2015, and Booster -- WAVE-Stereo achieves competitive zero-shot generalization accuracy without any external foundation model prior, achieving 3.18\% D1-all on KITTI 2015, 4.42\% Bad-2.0 on Booster, and 66ms real-time inference, striking a favorable balance between accuracy and efficiency. Our code is available at this https URL.

---


### 136. [When Bots Join the Team: Bot Adoption and the Institutional Fabric of Open-Source Software Projects](https://arxiv.org/abs/2607.13679)

**<font color=#1a73e8>作者：</font>** Yongren Shi, Wenyi Gong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are joining human teams, raising a basic question: when an automated agent becomes a regular participant, does group organization strengthen or weaken? We study this question in open-source software, where bots open pull requests, review code, and merge changes alongside people, leaving a public record of every interaction. Treating bots as participants rather than tools, we examine 2,991 GitHub projects for two years before and after each adopted its first bot. We measure three capabilities that institutional theory links to durable coordination - repeated engagement, social memory, and role differentiation - and two outcomes: conflict cascades and output distinctiveness. Bot adoption is followed by more repeated collaboration, greater recognition of specific bots in discussion, fewer conflict cascades, and more distinctive outputs. These changes cluster around adoption rather than accumulating gradually. Because we lack an untreated comparison group, we interpret the results as precisely timed associations, not causal effects. Two patterns are difficult for alternative explanations to account for: capabilities predict outcomes according to their function - coordination versus differentiation - rather than whether humans or bots provide them, and human-side capabilities account for the bot-conflict association but not the bot-distinctiveness association. The findings are consistent with a specific interpretation: predictable, rule-based agents can become part of a community's social infrastructure. The bot is the occasion; social organization is the mechanism.

---


### 137. [Towards Spatial Supersensing in the Wild](https://arxiv.org/abs/2607.13681)

**<font color=#1a73e8>作者：</font>** Tianjun Gu, Tianyu Xin, Kuan Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans can efficiently parse continuous sensory streams, from hours to years, scaffolding an internal world model that grounds spatial reasoning and prediction. To mimic this capacity, spatial supersensing challenges multimodal models to move beyond linguistic understanding toward true world modeling. However, their benchmark relies on synthetic long videos, formed by concatenating random short clips, and is mostly limited to household scenes, leaving real-world continuity and diversity underexplored. To address the gap, we introduce $\textbf{VSI-Super-Wild}$, a large-scale benchmark for evaluating spatial supersensing over long temporal horizons in diverse in-the-wild scenes. Notably, inspired by cognitive studies on how humans structure experience, we systematically probe the full triad of world state: the agent (observer), objects (scene items), and the environment (places and global layout). In total, VSI-Super-Wild contains $\textbf{6,980}$ human-verified question-answer pairs derived from $\textbf{442}$ real-world videos spanning 8 scene categories, including long-form recordings exceeding 4 hours. Results on VSI-Super-Wild expose a fundamental disconnect: despite advances in static image understanding, models consistently fail at tasks that require coherent world-state tracking over time. We characterize how performance degrades with world-state complexity and temporal horizon, and diagnose four failure modes: spatial collapse, semantic shortcuts, insufficient update, and instance confusion. This taxonomy reveals that models lack mechanisms to bind objects, agents, and environments into a unified spatial world model, a fundamental gap that defines the path forward for spatial supersensing.

---


### 138. [Calibrated Closed-Form Uncertainty for Radiative Gaussian Splatting in Sparse-View CT](https://arxiv.org/abs/2607.13682)

**<font color=#1a73e8>作者：</font>** Chulin Zhao, Yiran Xu, Shu Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiative Gaussian splatting has made sparse-view CT reconstruction fast, but existing methods output point estimates with no notion of where the reconstruction can be trusted. We exploit a property of transmissive X-ray imaging that RGB splatting cannot claim -- projection and voxelization are strictly linear in the per-Gaussian densities -- to equip radiative Gaussians with a variational density posterior whose predictive variance propagates in closed form, exactly, in a single forward pass, in both volume space ($\sigma^2(x)=\sum_i g_i(x)^2 s_i^2$) and projection space ($\mathrm{Var}[I_p]=\sum_i w_{i,p}^2 s_i^2$). We present the first systematic calibration study for Gaussian-splatting CT (Spearman / AUSE / ECE with temperature scaling), showing that the resulting per-voxel uncertainty ranks true reconstruction error on 14 of 15 scenes of the official benchmark across three view budgets -- 9 of 15 additionally meeting our magnitude-calibration target after a single temperature -- while the perturbation-ensemble heuristic of concurrent work, transplanted to voxel space under the same protocol on our development scenes, does not (rank correlation as low as $-0.08$). We then dissect why uncalibrated acquisition scores can nevertheless select acceptable views, identifying three regimes -- flat (isotropic, balanced), pathological (degenerate coverage), and anisotropic -- and showing, in controlled single-scene testbeds, that principled uncertainty earns a measurable premium only in the last, motivating a coverage-gated, maturity-scheduled acquisition policy; the same calibrated posterior further points toward a dose-adaptive stopping rule, whose experimental validation we leave to future work.

---


### 139. [Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity](https://arxiv.org/abs/2607.13683)

**<font color=#1a73e8>作者：</font>** Xiaotian Luo, Fengxingyu Wang, Chuanrui Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An LLM agent's real-task performance is shaped as much by the harness around its model as by the frozen model itself: its prompts, injected knowledge, runtime control, and configuration. In deployment the harness is often the only lever available, so improving it automatically is the natural way to raise performance without touching the weights. The hard part is not generating changes but knowing which one truly helped. Self-generated feedback is noisy, and an apparent gain can be a measurement artifact or an edit that merely overfits the tasks it was tuned on. We present a self-evolving agent-harness framework that separates proposing changes from crediting them: a language model diagnoses failures and proposes patches, while all sampling, measurement, and significance testing are owned by deterministic code, so every credited improvement is trustworthy by construction. Patches populate a gated, categorical quality-diversity archive (GSME) keyed on the (WHERE x WHY) pathology an edit addresses rather than the tasks it fixes, an anti-overfitting inductive bias; generalization is measured on a sealed test scored only after evolution. Across seven domains with a frozen open-weight model, the harness is train-selected and scored once on a sealed test; its credited gains there are +9 to +15.5pp and retain 86-147% of the training gain, evidence they generalize rather than overfit. The winning patch tracks the model's dominant pathology, not its size or family: changing the model can change the pathology and the patch, while the same pathology-to-patch match recurs across two model families. What transfers is the diagnose-and-credit loop, not any specific harness.

---


### 140. [DNA: Dual-stage Native Attribution for Generated Image Source Tracing](https://arxiv.org/abs/2607.13685)

**<font color=#1a73e8>作者：</font>** Chao Wang, Kejiang Chen, Zijin Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of image generation has produced numerous within-family variants, making source-model attribution of suspect images increasingly important for digital forensics. Existing proactive methods rely on watermark embedding or model modification, which may degrade visual quality and limit deployment flexibility. Passive methods often rely on large-scale supervised training or a single reconstruction signal, limiting their ability to handle unknown sources and distinguish highly similar within-family variants. We observe that attribution signals in latent generative models are naturally stratified across architectural levels: VAE-level cues reflect family-shared information, whereas backbone-level cues capture variant-specific behaviors. Motivated by this insight, we propose Dual-stage Native Attribution (DNA), a coarse-to-fine framework that follows this hierarchy without additional neural-network training. The coarse-grained stage uses Autoencoder Double-Reconstruction (AEDR) for efficient open-set family-level screening. The fine-grained stage performs closed-set model-level attribution with Native Prediction Consistency (NPC), which compares native prediction errors of within-family variants across multiple noise levels under semantic conditioning and attributes the source via normalized calibrated scores. To enable systematic evaluation, we construct DNA-30K, a benchmark for within-family variant attribution under open-set family-level evaluation. It comprises 30,000 images generated by 24 candidate models across six families spanning both denoising diffusion and flow matching, plus non-candidate generated and natural images as unknown sources. Experiments show that DNA achieves 89.11% end-to-end attribution accuracy on a task where random guessing accuracy is below 1% and outperforms the strongest baseline by 33.81% even when AEDR is used as the coarse-grained stage.

---


### 141. [Optimal and Efficient Contextual Combinatorial Semi-bandits with General Function Approximation](https://arxiv.org/abs/2607.13686)

**<font color=#1a73e8>作者：</font>** Hao Qin, Chicheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the contextual combinatorial semi-bandit (CCSB) problem with general reward function approximation. At each round, the learner observes a context, selects a combinatorial action consisting of a subset of basic arms, and receives the reward of each selected arm; the goal is to maximize the cumulative reward over time. We propose this http URL, a computationally efficient algorithm that, at each round, solves a convex optimization problem to sample a combinatorial action that balances exploration and exploitation. this http URL scales to large arm sets and imposes no structural assumptions on the action set beyond a cardinality bound of $m$ on each combinatorial action. We prove that this http URL achieves a minimax optimal regret bound of $O(\sqrt{m A T \log |\mathcal{F}|})$, where $A$ is the number of arms, $m$ is the maximum number of arms in a combinatorial action, $T$ is the time horizon, and $\mathcal{F}$ is the reward function class. In the realizable setting, this bound matches the state-of-the-art regret guarantees achieved by policy search-based algorithms in the more restricted slate recommendation settings, while simultaneously generalizing to arbitrary combinatorial action structures and general reward function approximation.

---


### 142. [Microstructure-Conditioned Surrogate Models for Graded Multiscale Optimization of Mycelium Composites](https://arxiv.org/abs/2607.13688)

**<font color=#1a73e8>作者：</font>** J. Storm, I.B.C.M. Rocha, S. Schyck 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emerging sustainable materials increasingly rely on engineered hierarchy and microstructure to achieve control of their properties and mechanical behavior. Optimizing these materials with controllable microstructures requires efficient multiscale simulations. Data-driven surrogate models for the microscale can accelerate multiscale simulations, but require large amounts of data even for a fixed microstructure. When a range of microstructures is considered, as is the case in multiscale optimization, even more data is needed to train a surrogate. To overcome this challenge, we condition a hybrid physics-data surrogate on microstructural variables using a hypernetwork. This approach enables accurate predictions of multiscale mechanical behavior for a mycelium-woodchip composite material, even when trained on small datasets. The conditioned surrogate makes multiscale simulations of functionally graded structures tractable, and we validate it against a full FE^2 simulation. We optimize a graded multiscale disk, and reduce the peak stress by 42% compared to one with a random microstructure. Then, we go one step further, conditioning the network directly on manufacturing variables that can have a complex influence on the microstructure. This is a practical route to engineer the microscale for desired macroscale behavior. This contribution highlights the benefits of microarchitectured structures and demonstrates how conditioned surrogate models enable their multiscale optimization, which will accelerate the development and design of future sustainable materials and structures.

---


### 143. [Barnamala: Parameter-Efficient Handwritten Devanagari Recognition at Benchmark Saturation](https://arxiv.org/abs/2607.13689)

**<font color=#1a73e8>作者：</font>** Ashish Thapa, Samrat Karki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We built a compact convolutional network (1.11 M parameters) for 46-class DHCD Devanagari recognition and reached 99.73%, the highest reported at 15.6x smaller than prior state-of-the-art. We have effectively reached the saturation point: every model tested, large teacher ensembles included, hits the same 11-error intrinsic floor. No configuration achieves a statistically clear win under exact McNemar tests with Wilson confidence intervals. Even without knowledge distillation, our student matches the nearest large-model baseline (17.32 M parameters; McNemar $p = 0.345$). Outside of DHCD, zero-shot on CMATERdb digits gives 76.6% and fine-tuning reaches 97.8%; corruption robustness is also far better than large baselines (mean corruption accuracy 75.7% vs. 38.7%). All artifacts are at this https URL.

---


### 144. [Social Simulations: from Agent-Based Modeling to Digital Twins](https://arxiv.org/abs/2607.13693)

**<font color=#1a73e8>作者：</font>** Erica Cau, Andrea Failla, Valentina Pansanella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This book chapter covers the evolution of social simulation from classical agent-based models, in which agents interact according to explicitly defined behavioral rules, to AI-enhanced simulations based on Large Language Models and, ultimately, Social Digital Twins: high-fidelity, data-driven representations of real-world socio-technical systems. Along this trajectory, we discuss the main methodological foundations, applications, advantages, and limitations of each paradigm, highlighting the progressive shift from abstract models designed to investigate general social mechanisms toward increasingly realistic computational representations of specific social systems.

---


### 145. [Conditional Invertible Neural Networks for Data-Driven UAV Control: A 2-D Proof of Concept](https://arxiv.org/abs/2607.13703)

**<font color=#1a73e8>作者：</font>** Christian Wittke, Stephan Myschik, Oliver Niggemann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate conditional invertible neural networks (cINNs) as probabilistic inverse-dynamics models for multirotor control. For a planar X8 coaxial multicopter, we learn $p(u \mid s_t, c_t)$ from an incremental nonlinear dynamic inversion (INDI) teacher using rational-quadratic spline coupling and invertible linear mixing. Open-loop reproduction reaches $R^2 = 0.944$, mean CRPS 0.0915, and log-probability-error correlation $\rho = -0.60$. Over 15 closed-loop scenarios, position RMSE matches INDI (9.7 vs. 9.5 m), with 47 percent tracking acceptably; failures separate into attitude divergence under aggressive steps and phase lag under high-frequency references, isolating command bandwidth and data coverage as dominant failure mechanisms.

---


### 146. [How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement](https://arxiv.org/abs/2607.13718)

**<font color=#1a73e8>作者：</font>** Alexandra E. Michael, Franziska Roesner  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As AI agents gain prevalance, users are increasingly exposed to the risks such systems entail. Prompt injection attacks, as well as hallucination, can cause agents to leak private information to third parties. As autonomous systems, agents also present the more active danger of performing sensitive tasks, such as bank transactions, without the user's intent or authorization.
Recognizing this challenge, the agentic security community has developed numerous proposals for secure agentic systems. Much of this work has focused on product-level approaches, where agentic system developers determine and apply the same security policies and permissions to all users. Yet different users have different needs and preferences, necessitating support for user-level permissions policies in agentic AI systems.
To understand how user-level permissions are handled in AI agent systems, we survey 21 proposals for agent permissions systems. From this review, we construct a taxonomy of how different systems specify user-level permissions policies, both at the user interface and internally; derive internal policies from user input; and enforce those policies at run-time. We then analyze five prominent commercial agents and compare their permissions handling to agentic permissions systems in the literature. We identify several high-level themes across the literature and commerical agents, as well as multiple gaps where future work is needed.

---


### 147. [Self-supervised Speech Comparison for L2 Phone, Rhythm, and Intonation Scoring](https://arxiv.org/abs/2607.13721)

**<font color=#1a73e8>作者：</font>** Stephen McIntosh, Reuben Smit, Daisuke Saito 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> L2 speech assessment has traditionally focused on phonetic assessment, leaving the scoring of suprasegmental features such as rhythm and intonation underexplored. Moreover, assessment methods often require training with labeled L2 speech data, making them difficult to apply in low-resource settings. We investigate whether DTW over self-supervised WavLM representations can provide a text-free framework for assessing phonetic accuracy, rhythm, and intonation in English and Japanese L2 speech. Results show that a basic DTW-based approach that compares learner speech to native templates exceeds human agreement on holistic and sentence-level phonetic scoring. For rhythm, we introduce methods that measure the degree of warping in the DTW alignment path; our best method approaches human-level performance. For intonation, we combine DTW distance over prosodic residuals with pitch and intensity features, but performance remains more modest on some tasks. Our results point to self-supervised representations as a promising, text-free basis for multi-aspect pronunciation assessment.

---


### 148. [Interaction Density as a Behavioural Signature of Exhibit Type: A Minimal-Log Study from a Two-Venue Science Experience Centre](https://arxiv.org/abs/2607.13724)

**<font color=#1a73e8>作者：</font>** R A Udaya Rakshith, Inavamsi Enaganti, Umang J Gala  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding how visitors engage with interactive exhibits usually calls for either labour-intensive manual observation or invasive multimodal sensing -- eye-tracking, cameras, wearables -- that few science centres can deploy at scale. We ask how much can be learned instead from the handful of fields that most touch-enabled exhibits already log by default: a session's start time, end time, and press count. Analysing 2,816 visitor sessions across eight exhibits at two venues of a science experience centre in Bengaluru, India, we derive interaction density -- presses per second -- as a simple behavioural signature, and use it to distinguish fast-paced games from slower, deliberate quizzes. Density does so cleanly (Mann-Whitney r=0.556) and predicts exhibit type on its own with a cross-validated AUC=0.778. But the data complicates the obvious story: games are not just more intense, visitors also dwell on them longer (r=0.172), reversing the intuitive trade-off between intensity and duration -- traced to exhibits whose escalating difficulty creates open-ended re-engagement loops rather than fixed endpoints. Density is not a universal replacement for existing metrics either: raw press count alone explains far more variance in dwell time (R^2=0.527) than density does (R^2=0.081), though combining both improves on either alone (R^2=0.667). Exhibit-level anomalies, a cross-venue replication check, and a session-length censoring artefact further stress-test rather than simply confirm these results. The broader case we make is methodological: minimal, privacy-preserving interaction logs -- not additional sensors -- can already support rigorous, falsifiable behavioural research at any science centre with touch-enabled exhibits.

---


### 149. [DAGR: State-Conditioned Goal Representations via Difference-Aware Goal Cross-Attention](https://arxiv.org/abs/2607.13731)

**<font color=#1a73e8>作者：</font>** Xing Lei, Wenyan Yang, Xuetao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Goal-conditioned reinforcement learning hinges on how the goal is encoded. Contrastive, metric, temporal-distance, and information-theoretic encoders differ in objective. They still share one trait. None of them sees the current state. Such a state-independent embedding cannot mark which part of the goal still needs action. The policy must then recover that cue by inverting both encoders. We propose DAGR. It refines the static embedding of any late-fusion encoder into a state-conditioned one through multi-scale gated cross-attention. A near-identity gated residual preserves the base representation. Difference-aware Goal Cross-Attention then biases the attention scores using a per-token state-goal discrepancy map. On OGBench, DAGR improves navigation. Our ablations trace the gain to the gated residual, not to the difference bias that names the method. On manipulation and puzzle tasks it matches or falls below the base. DAGR is a structured refinement, not a universal improvement.

---


### 150. [Constraint-Driven Model Optimization: An Industry Framework for Selecting Compression and Acceleration Techniques in Modern Machine Learning Systems](https://arxiv.org/abs/2607.13735)

**<font color=#1a73e8>作者：</font>** Dhruv Shivkant, Saket Mohanty, Utkarsh Wadhwa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid deployment of machine learning systems across cloud, edge, and enterprise environments has brought model optimization to the forefront of systems-engineering. Despite a rich literature spanning quantization, pruning, knowledge distillation, parameter-efficient fine-tuning (PEFT), and inference-time optimization, practitioners are often left navigating these techniques through heuristics rather than principled methodology. We argue that optimization should be formulated as a constraint-driven, multi-objective engineering decision and introduce a unified framework that characterizes any production deployment along five interacting constraint dimensions: data availability, latency budget, memory budget, accuracy tolerance, and retraining budget. Building on this taxonomy, we synthesize empirical gains reported across the research literature and map them to operational constraints rather than algorithmic categories. To ensure practical relevance, we selected these techniques by reviewing recent literature for methods that report measurable improvements against critical deployment bottlenecks. We propose a prescriptive decision framework and provide optimization pipelines for four representative industrial scenarios to illustrate it in practice. To the best of our knowledge, this work provides one of the first structured attempts to formalize model optimization as a constraint-aware, multi-objective engineering process, synthesizing quantitative evidence from the research literature.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-202](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
