# 📦 其他研究 | 2026年06月26日

> 本类共 **222** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-222](./part-05.md)

---

### 51. [Beyond Shapley: Efficient Computation of Asymmetric Shapley Values](https://arxiv.org/abs/2606.25103)

**<font color=#1a73e8>作者：</font>** Ezequiel Companeetz, Santiago Cifuentes, Sergio Abriola  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We address the problem of explainability in machine learning models through feature attribution methods. In particular, we consider a variant of Shapley values known as Asymmetric Shapley Values (ASV), which enables the incorporation of causal knowledge into model-agnostic explanations through the use of a causal graph. We show that in certain contexts in which the computation of SHAP is $\#P$-hard, the exact computation of ASV can be done in polynomial time. To extend this algorithmic result, we introduce a notion of equivalence classes over the topological orderings of the underlying causal graph, which is useful to reduce the time to compute ASV. In particular, we present a polynomial-time algorithm (in the number of equivalence classes) to compute it whenever the causal graph is a rooted directed tree. Finally, we develop an algorithm for approximating ASV in arbitrary causal DAGs which relies on a procedure to sample topological orderings uniformly at random. To implement this sampling mechanism we leverage known algorithms as well as simpler alternatives. Our experimental results demonstrate the practical viability of the proposed approach in realistic causal structures.

---


### 52. [The Clinician's Veto: Navigating Trust, Liability, and Uncertainty in Autonomous AI Prescribing](https://arxiv.org/abs/2606.25108)

**<font color=#1a73e8>作者：</font>** Eileanor LaRocco, Sarah Tan, Adarsh Subbaswamy 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous AI systems are transitioning from advisory to autonomous roles for medication prescriptions. Recent United States bill H.R. 238 and Utah's prescription-renewal pilot both authorize AI to prescribe medications in an agentic capacity. While some regulatory guidelines suggest aggregate model performance metrics for clearance, they do not require i) calibrated per-prediction confidence for action-gated thresholds, ii) differentiated communication of uncertainty arising from model ignorance (epistemic) versus genuine clinical ambiguity (aleatoric), and iii) inferential transparency at the moment of decision that allows for liability allocation. Here, we present a regulatory and technical argument (tested with a survey of 136 U.S. prescribing clinicians) positioning these as minimum architectural requirements for safe autonomous prescribing. Our results suggest prescribing clinicians i) would not permit autonomous prescribing without a calibrated confidence-based escalation mechanism, ii) preferred a competing-options summary when uncertainty was aleatoric but shifted to abstention when uncertainty was epistemic, and iii) were only willing to accept additional liability when inferential transparency enabled a substantive judgment under acknowledged uncertainty. These findings indicate our recommended architectural features would encourage higher rates of clinician adoption, largely through collapsing much of what "autonomy" conventionally means. A system meeting these requirements would function less as an autonomous agent and more as a heavily supervised decision-support tool. As legislation and state pilots proceed, our technical argument backed by clinician perspectives provides opportunities for regulation to constrain the degree of autonomy ethically granted to AI in prescribing while aligning liability with the institutional actors who control system design and deployment.

---


### 53. [A Framework for Directed Hypergraph Signal Processing via tensor t-SVD](https://arxiv.org/abs/2606.25112)

**<font color=#1a73e8>作者：</font>** Carlos Mundo-Levano, Nicolás Bello, Daniel L. Lau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Directed Hypergraph Signal Processing (DHGSP), a unified framework that extends graph signal processing to accommodate both higher-order (polyadic) and asymmetric (directional) relationships simultaneously. Using the tensor singular value decomposition (t-SVD) within the t-product algebra, we define a novel adjacency tensor for directed hypergraphs, a topologically faithful shift operator, and a lossless Directed Hypergraph Fourier Transform (t-DHGFT). Experiments on real traffic networks demonstrate that DHGSP outperforms matrix-based (graph and digraph) and undirected tensor-based (hypergraph) baselines in denoising tasks.

---


### 54. [Reward-Conditioned Attention: How Reward Design Shapes What Autonomous Driving Agents See](https://arxiv.org/abs/2606.25127)

**<font color=#1a73e8>作者：</font>** Mohamed Benabdelouahad, Ahmed Djalal Hacini, Nadir Farhi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate how reward design shapes the internal attention patterns of reinforcement learning agents trained for autonomous driving. Using three Perceiver-based agents that share identical architectures and training data but differ only in their reward configurations$\unicode{x2014}$ranging from basic violation penalties to continuous proximity penalties$\unicode{x2014}$we analyze cross-attention allocation across 50 real-world scenarios from the Waymo Open Motion Dataset. A central methodological finding is that naïve pooling of timesteps across episodes substantially underestimates the attention$\unicode{x2013}$risk relationship; within-episode correlation with Fisher z-transform aggregation is the appropriate statistic and reveals a robustly positive link between collision risk and agent-directed attention. Building on this validated methodology, we demonstrate two reward-conditioned effects: agents trained with navigation rewards allocate up to $2.0\times$ more attention to GPS-path tokens than those trained with additional proximity penalties$\unicode{x2014}$and $4.7\times$ more than agents with no navigation incentive$\unicode{x2014}$revealing that reward content directly determines which scene elements the encoder prioritizes, and continuous time-to-collision penalties create a $\textit{learned vigilance prior}$$\unicode{x2014}$elevated resting agent surveillance maintained throughout collision-free phases. In several scenarios, the complete-reward and minimal-reward models exhibit opposite attention$\unicode{x2013}$risk correlation directions, demonstrating that reward design can qualitatively reverse attentional strategy rather than merely modulating its magnitude. These results suggest that attention analysis is a practical diagnostic for verifying that a reward function produces the intended representational behaviour in safety-critical RL systems.

---


### 55. [The cognitive, affective, and behavioral expression of self-stigma among people who use drugs in online substance use communities](https://arxiv.org/abs/2606.25143)

**<font color=#1a73e8>作者：</font>** Layla Bouzoubaa, Hyung Wook Choi, Milan Varghese 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Objectives: To develop a codebook for self-stigma across cognitive, affective, and behavioral domains, and to estimate the prevalence, co-occurrence, and temporal patterns of these indicators in Reddit posts by people who use drugs. Methods: We developed a ten-indicator codebook through consensus-based abductive coding spanning cognitive (self-labeling, pessimism/self-defeatism, deservingness/worthlessness), affective (shame, guilt/self-blame, despair/hopelessness), and behavioral (concealment, anticipated rejection, desire to quit, ambivalence) domains; two coders reached substantial agreement (Cohen's k = 0.72). We then scaled classification with a large language model validated against expert coding (k = 0.73, F1 = 0.80), analyzing 72,115 thread-initiating posts from 1,660 English-language users (2006-2025). Results: 3,838 posts (5.3%) from 1,228 users (74.0%) contained self-stigma; all ten indicators discriminated self-stigma posts (RR 3.6 to 86.2), led by self-labeling (56.0%) and despair/hopelessness (48.5%). Self-stigma was integrated: core and behavioral indicators were strongly associated at the user level (OR = 4.65, 95% CI 3.12-6.94, p < 0.001), and 87.0% of posts with behavioral indicators also contained a core indicator. Contrary to progressive models, behavioral indicators emerged earlier than core ones (desire to quit at median position 0.08 vs. shame at 0.38). Nine of ten indicators were stable across posting trajectories; only pessimism increased (OR = 1.62, 95% CI 1.25-2.10). Conclusion: Among people who use drugs online, self-stigma is an integrated phenomenon in which behavioral indicators rarely appear without internalized ones and often precede them. Most expressions remain stable over time, but pessimism about change deepens, marking a target for early digital intervention and showing that progressive stage models do not map directly onto textual disclosure.

---


### 56. [Proactive Systems in HCI and AI: Concepts, Challenges, and Opportunities](https://arxiv.org/abs/2606.25149)

**<font color=#1a73e8>作者：</font>** Nima Zargham, Sharon Ferguson, Jaisie Sin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The last few years have seen a significant rise in interest in highly autonomous and proactive systems, fueled by advances in AI. Systems that anticipate user needs, take initiative, and act without explicit user input. Such systems span a wide range of applications, from smart lighting that adapts to user activity to assistive robots that plan actions in advance to intelligent thermostats that learn routines and adjust environments proactively. Despite this breadth, the concept of proactivity remains loosely defined and inconsistently applied across research and practice. Current usage of the term often conflates fundamentally different system behaviors. For instance, simple reminders or recommendation systems are frequently labeled as proactive, even though underlying mechanisms and intentions differ significantly. This conceptual ambiguity limits our ability to systematically design, compare, and evaluate proactive systems. Moreover, existing methodologies for design and evaluation are largely rooted in reactive interaction paradigms, failing to address the unique challenges posed by proactive behavior, including timing, appropriateness, user control, transparency, and trust. This multidisciplinary workshop aims to establish a clearer and more rigorous foundation for understanding proactive systems. We bring together researchers and practitioners from Human-Computer Interaction, AI, and related fields to (1) develop a shared conceptualization of proactivity, (2) identify gaps and limitations in current design and evaluation approaches, and (3) co-create human-centered guidelines and research directions for future systems. Through interactive discussions and collaborative activities, the workshop seeks to map key challenges and opportunities, ultimately advancing robust and consistent frameworks for designing and evaluating proactive technologies.

---


### 57. [Silent Failures in Physics-Informed Neural Networks: Parameter Poisoning and the Limits of Loss-Based Validation](https://arxiv.org/abs/2606.25151)

**<font color=#1a73e8>作者：</font>** David McShannon, Nicholas Dietrich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) embed governing equations in their loss function, enabling mesh-free solutions to partial differential equations. Low training loss is treated as evidence that the learned solution is physically correct. This paper shows that assumption breaks down when encoded physics are incorrect. By perturbing PDE parameters before training, a setting we describe as physics parameter poisoning or parameter misspecification, we produce models that train to low loss but give incorrect answers; we treat the perturbation schedule as sensitivity analysis rather than only as a security threat, and none of our claims requires an adversary. Achieving low residual loss does not discriminate accurate from inaccurate solutions: poisoned models reach losses at or below the clean baseline yet differ by large margins, so driving the residual down is not evidence of physical accuracy. Across three PDE systems (Burgers equation, Navier-Stokes cavity, and convection-diffusion), poisoned models match or beat the clean-model training loss while their solutions differ by up to 71% in the fixed sweep and up to 128% under adversarial search; at Cavity Re=400 the poisoned loss falls below the clean baseline. We define a detection difficulty ratio R (solution error divided by training loss) to summarize how invisible the corruption is, though cross-PDE comparison is complicated by differences in loss scale. We test six candidate defenses, none of which reliably detects corruption across all regimes. We propose a post-hoc defense: sweeping the PDE residual loss across parameter values without retraining. The loss minimum recovers the true training parameter without external data, and generalizes across all three PDE systems. The effect holds across five network architectures (8.7K to 133K parameters), is bidirectional, and is confirmed across multiple random seeds.

---


### 58. [Hitting a Moving Target: Test-Time Adaptation for AI Text Detection under Continual Distribution Shift](https://arxiv.org/abs/2606.25152)

**<font color=#1a73e8>作者：</font>** Kevin Ren, Manish Raghavan, Nikhil Garg  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deployed approaches for AI text detection often rely on training-time access to labeled datasets of both human-written and AI-generated text. This approach is vulnerable to three types of distribution shifts that occur continually post-deployment, and for which labeled data is often unavailable: adversarial humanization, new LLMs being released, and temporal drift in human writing. Simultaneously, existing approaches do not leverage a key signal of LLM usage: inference-time homogeneity. We propose a test-time adaptation (TTA) approach, using semi-supervised learning, that adapts to distribution shifts by leveraging homogeneity among unlabeled samples observed at inference time. Empirically, we find that state-of-the-art supervised detectors systematically fail when they encounter distribution shifts in AI-generated and human writing, both adversarial and natural, while test-time adaptation with semi-supervised learning is largely robust; e.g., the commercial model Pangram detects just 24.1% of our adversarial AI-generated text, compared to 90.5% for our test-time approach. We establish that test-time adaptation is a promising framework for AI text detection in the wild. We publicly release our code (which includes code for model training, evaluation, and plots) at this https URL.

---


### 59. [The Gentle Collapse: Distributional Metrics for Continual Learning](https://arxiv.org/abs/2606.25165)

**<font color=#1a73e8>作者：</font>** Ahmed Anwar, Andreas Wagner, Federico Raue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accuracy degradation is the standard metric for Catastrophic Forgetting (CF), however, it records only whether forgetting occurred or not. It saturates at the extremes and collapses discretely at task boundaries, hiding the internal structure of what is being forgotten. We introduce six softmax-derived metrics spanning true-label rank (TLR), predictive confidence, and distributional divergence that characterize forgetting continuously, each normalized to [0, 1] with no modification to training. On CIFAR-100, these metrics carry information where accuracy does not: at 0% accuracy, the Confusion Margin spans an IQR of [0.32, 0.50] across classes that accuracy treats identically. We demonstrate that this richer signal is actionable in mitigating catastrophic forgetting. Per-sample metric scores used as loss weights reduce forgetting by 1.3 percentage points over uniform experience replay (ER) on CIFAR-100. Furthermore, the slope of a metric over a small window provides a stable sampling criterion: at a small-window size (e.g. 3 epochs), accuracy-trend degrades to 34.79% (std. = 2.32) while log-TLR achieves 41.07% (std. = 0.57). This gap is structural since reliable small-window trend estimation requires a continuous signal. On TinyImageNet, log-TLR trend sampling reduces forgetting by 7.7 percentage points over the ER baseline.

---


### 60. [Elo-Disentangled Player-Style Embeddings for Human Chess via Rating-Conditioned Residual Move Model](https://arxiv.org/abs/2606.25176)

**<font color=#1a73e8>作者：</font>** Jason Carlson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study representation learning for individual human chess style: a per-player embedding learned from a player's move history such that inner products measure stylistic similarity, while being approximately disentangled from playing strength (Elo). Our key design is a residual formulation: a rating-conditioned base move model (Maia-3 policy logits plus Stockfish-derived features, scored over Maia-2-proposed candidates) captures what a typical player of a given strength would play, and a frozen copy of it anchors a learned move encoder and a per-player vector z, so that z explains only deviations from rating-typical play. The base model improves move prediction over the strong Maia-3 policy by 27-37% relative NLL across the rating spectrum, with the largest gains at the top (2800+); Stockfish's marginal value grows monotonically with Elo (negligible at 900-1200, +0.085 nats at 2800+). On a shared Elo-stratified benchmark of 22,620 held-out decisions, top-1 move-matching rises monotonically from Maia-2 to Maia-3 to the Stockfish-augmented base (0.51 -> 0.57 -> 0.68): the base is +33% relative top-1 over Maia-2 and +19% over Maia-3 (30% lower NLL), with the engine-feature lift largest at high Elo. The player embedding adds little to raw move-matching on top of this base -- its marginal top-1 gain falls within the 95% confidence interval -- and its value is instead representational: z generalizes to held-out decisions without overfitting, re-identifies players from disjoint games above chance, and a linear probe recovers rating from z with only R^2 = 0.06 (no better nonlinearly), evidence it captures style on an Elo-orthogonal axis. We argue that a strong rating-conditioned base plus a compact, Elo-disentangled embedding -- separating typical play from individual deviation -- is an economical, interpretable model of individual style, an alternative to per-player preference fine-tuning.

---


### 61. [EveLoad: Cognitive Workload Recognition from Event-Based Eye Movements](https://arxiv.org/abs/2606.25177)

**<font color=#1a73e8>作者：</font>** Guorui Lu, Shaohua Guan, Zhen Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cognitive workload monitoring is important for adaptive rehabilitation and assistive interfaces, where task difficulty, pacing, and feedback should be adjusted according to the user's cognitive state to avoid overload and under-challenge. Emerging extended reality and robot-assisted rehabilitation environments provide controllable training tasks, but they require unobtrusive sensing methods that can capture rapid ocular dynamics during interaction. Existing eye-movement-based cognitive workload recognition methods mainly rely on frame-based eye trackers, which often suffer from limited temporal resolution and degraded robustness under rapid eye movements. In contrast, event cameras provide microsecond-level temporal resolution, high dynamic range and low latency, making them suitable for capturing fine-grained ocular dynamics. Many previous studies rely on free-viewing or similar paradigms, where gaze locations can vary across tasks. As a result, models may learn associations between gaze-location distributions and cognitive workload, rather than workload-related eye movement characteristics themselves. In this work, we introduce EveLoad, which, to the best of our knowledge, is the first event-based eye-movement dataset with graded cognitive workload annotations, collected from 20 healthy participants under spatially constrained and task-driven conditions using a controlled N-back-guided fixation paradigm. Based on this dataset, we establish a benchmark for cognitive workload recognition with six workload levels and propose a learning framework that encodes spatiotemporal event representations. Experimental results show that our approach achieves an average subject-specific accuracy of 96.36% and 96.13% under mixed random split evaluation. These results suggest that event-based eye movements may provide a useful sensing pathway for future workload-aware rehabilitation.

---


### 62. [Neural operator-based digital twins for modeling amyloid-$β$ and tau propagation and treatment optimization in Alzheimer's disease](https://arxiv.org/abs/2606.25185)

**<font color=#1a73e8>作者：</font>** Xiaofeng Xu, Tingting Dan, Zifan Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurately predicting the spatiotemporal evolution of amyloid-$\beta$ and tau proteins at the individual level is critical for improving the diagnosis and treatment of Alzheimer's disease. We consider the problem of constructing patient-specific digital twins that model the propagation of these biomarkers on the cortical surface using reaction--diffusion dynamics. A major challenge is that the underlying nonlinear aggregation mechanisms are unknown and must be inferred from sparse, noisy, and heterogeneous longitudinal PET imaging data. To address this, we develop a data-driven framework that learns biomarker dynamics directly from clinical observations. The approach combines operator learning with reduced-order representations to infer governing equations of disease progression from data. Using this framework, we achieve predictive accuracies of 87\% for amyloid-$\beta$ and 81\% for tau. Building on the learned dynamics, we further formulate a PDE-constrained optimal control problem to design personalized therapeutic strategies that regulate pathological protein propagation. By integrating data-driven dynamical modeling with treatment optimization, the proposed digital twin framework provides an interpretable and predictive platform for understanding disease progression and enabling precision interventions in neurodegenerative disorders.

---


### 63. [Efficient Analytic Uncertainty Quantification for Multi-Modal Regression](https://arxiv.org/abs/2606.25188)

**<font color=#1a73e8>作者：</font>** Kun Jin, James Harrison, Jiawei Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient uncertainty quantification (UQ) is essential for trustworthy large-scale learning. Existing UQ methods for regression tasks mainly operate under the assumption that the conditional label marginal satisfies single-peak parametric models, e.g., Gaussians, where the negative log-likelihood function simplifies to the mean square error. However, such single-peak assumptions fail in regression tasks featuring multi-modal distributions. On the other hand, semi-parametric methods which achieve strong regression performance for multi-modal distributions often lack efficient quantification on their prediction variances. In this work, we extend UQ techniques based on Variational Bayesian Inference (VBI) to two widely used semi-parametric regression models that yield histogram-like reconstructions of the conditional label densities: Quantile Regression (QR) and Classification Restoration (CR). Our approach introduces a unified, distribution-agnostic framework that simultaneously achieves accurate estimation of complex conditional distributions and highly efficient UQ. Theoretically, our method is grounded in novel formulations of QR and CR within the VBI framework, yielding analytic Evidence Lower Bounds (ELBO) to streamline training and a closed-form or analytically approximated predictive density for efficient inference. Empirically, we evaluate our methods on three large-scale regression benchmarks with multi-modal label distributions. Our framework outperforms state-of-the-art multi-modal regression baselines, and even matches predictive performance of computationally expensive ensemble models. Furthermore, by leveraging epistemic uncertainty estimation, our approach enables highly data-efficient active learning strategies.

---


### 64. [SoK: AI Secure Code Generation: Progress, Pitfalls, and Paths Forward](https://arxiv.org/abs/2606.25195)

**<font color=#1a73e8>作者：</font>** Rupam Patir, Keyan Guo, Haipeng Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing use of AI systems for code generation raises a central security question: what can today's models and coding agents actually do to produce secure code, where do they still fail, and what would move the field forward? Existing work has explored prompting, fine-tuning, reinforcement learning, and agentic workflows for secure code generation, but the field still lacks a systematic understanding of how these techniques improve security and why substantial failures persist. In this SoK, we systematize the progress, pitfalls, and paths forward for AI secure code generation. We introduce a three-level framework that measures models' natural-language understanding of secure coding principles, their code-level actuation of those principles during generation, and the knowledge--actuation gaps between the two. We instantiate this framework across models and coding agents on benchmarks covering both isolated function-level security and full web-application security. Our results show that secure-coding-principle understanding is a statistically strong predictor of code-level outcomes, including functional correctness, security, and joint functional-security correctness. Yet substantial knowledge--actuation gaps remain: models can recognize relevant security principles but still fail to translate them into secure and functional code. These findings offer a principle-centered account of where AI secure code generation stands today and identify concrete paths forward through principle-guided generation, evaluation, benchmarking, and agentic workflows.

---


### 65. [Efficient Adaptive Data Acquisition via Pretrained Belief Representations](https://arxiv.org/abs/2606.25197)

**<font color=#1a73e8>作者：</font>** Daolang Huang, Zhuoyue Huang, Conor Hassan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning effective policies for adaptive data acquisition remains challenging: posterior-based methods rely on surrogate models and posterior approximations that can be misspecified or biased, while direct policy-learning methods map from historical observations and fail to exploit available model representations, making learning harder. We introduce policy learning with belief representations (POLAR), based on the insight that optimal data acquisition depends on the observation history only through a sufficient belief state. Specifically, POLAR decouples representation learning from policy learning by leveraging pretrained predictive foundation models as belief-state encoders, training a policy head on top of their representations. This yields a simple, unified amortised policy learning framework for Bayesian experimental design, Bayesian optimisation, and active learning, differing only in the task-specific utility used to train the policy. Empirically, we find that POLAR outperforms state-of-the-art amortised methods across diverse tasks while requiring far fewer training samples, demonstrating a significant step in the scalability and efficiency of amortised data acquisition.

---


### 66. [Heuresis: Search Strategies for Autonomous AI Research Agents Across Quality, Diversity and Novelty](https://arxiv.org/abs/2606.25198)

**<font color=#1a73e8>作者：</font>** Antonis Antoniades, Deepak Nathani, Ritam Saha 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous AI Research promises to accelerate the scientific progress of machine learning. To realise this goal, current Large Language Model (LLM)-based agents need to go beyond just writing code, to mastering the exploration of simultaneously performant, diverse and novel ideas. To this end, we introduce Heuresis, a framework that abstracts the research pipeline into a set of general and composable primitives, enabling open-ended scientific exploration in machine learning research. We implement six search strategies: a greedy baseline, two archive-based (MAP-Elites, Go-Explore), one evolutionary (Islands), and two divergent (Curiosity, Omni), and evaluate them across three axes (Quality, Diversity, and Novelty) on three domains (LLM Pretraining, On-Policy RL, and Model Unlearning), totalling 3,222 scored runs. We find that completely novel ideas are rare. No idea across our scored runs is rated as "Original", and only a few achieve only "Minor Similarity" to prior work. Moreover, novel ideas never approach the highest-performing known-recipe scores. Across all six strategies and three domains, only one such idea lands in the top-10 by quality. We also observed agents resorting to a variety of reward-hacking techniques during execution (40 confirmed fabrications across 1,628 scored runs), and detecting them was necessary to keep the search faithful to the task. Our results show that while current search and Quality-Diversity strategies enable us to steer where the generated ideas land on the quality, diversity, and novelty axes, they do not expand the quality-novelty frontier. Bridging this gap is the open challenge towards the ultimate goal of perpetual, autonomous scientific progress. Code is available at this http URL.

---


### 67. [A Hybrid CNN-LSTM Intrusion Detection Framework for Cybersecurity in Smart Renewable Energy Grids](https://arxiv.org/abs/2606.25200)

**<font color=#1a73e8>作者：</font>** Sajib Debnath, Remon Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The accelerated digitalization of renewable energy smart grids through IoT sensors, AMI, and SCADA systems has significantly expanded the attack surface for sophisticated cyberattacks, FDI attacks that stealthily distort state estimation and DoS/DDoS attacks that flood communication channels. Current IDS, however, exhibit three inherent limitations: inadequate modeling of the temporal progression of multi-step attacks, degraded scalability under extremely skewed class distributions of standard benchmark datasets, and restricted generalization across heterogeneous network environments. In this study, we present a Hybrid CNN-LSTM IDS that jointly exploits CNN-based spatial feature extraction and LSTM-based temporal sequence modeling, enabling the detection of instantaneous volumetric anomalies and gradually evolving low and slow-attack campaigns in real time. The model was trained using a seven-step preprocessing workflow comprising missing-value imputation, min-max normalization, one-hot encoding, SMOTE class balancing, mutual-information feature selection, causal temporal sequence construction (T=10), and stratified partitioning. LSTM (96.1%), Random Forest (93.5%), SVM (91.2%) and KNN (89.7%); in NSL-KDD, it reaches 98.2% precision versus 96.4% (LSTM), 95.2% (CNN), 92.7% (Random Forest) and 90.8% (SVM), with margins of 2-9 percentage points in all measures. An ablation analysis identified SMOTE balancing as the most influential design choice (-3.7~pp F1 without it). The model achieves a real-time inference throughput of 27,800 flows/s on GPU and 0.082 ms/sample CPU latency in FP32,, with INT8 quantization providing an additional 3.1 x speedup at 0.3% accuracy loss, confirming deployment feasibility on resource-constrained IEDs with <128MB memory and establishing a deployable deep-learning framework for securing next-generation renewable energy smart grid infrastructure.

---


### 68. [FDN: Interpretable Spatiotemporal Forecasting with Future Decomposition Networks](https://arxiv.org/abs/2606.25201)

**<font color=#1a73e8>作者：</font>** Nicholas Majeske, Ariful Azad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal systems comprise a collection of spatially distributed yet interdependent entities each generating unique dynamic signals. Highly sophisticated methods have been proposed in recent years delivering state-of-the-art (SOTA) forecasts but few have focused on interpretability. To address this, we propose the Future Decomposition Network (FDN), a novel forecast model capable of (a) providing interpretable predictions through classification (b) revealing latent activity patterns in the target time-series and (c) delivering forecasts competitive with SOTA methods at a fraction of their memory and runtime cost. We conduct comprehensive analyses on FDN for multiple datasets from hydrologic, traffic, and energy systems, demonstrating its improved accuracy and interpretability.

---


### 69. [ARTOO-DARTU: Studying AR-HRC With AR Obstruction Mitigation During a Warehouse Task](https://arxiv.org/abs/2606.25202)

**<font color=#1a73e8>作者：</font>** Christian Fronk, Hanting Ye, Zhehan Qu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-robot collaboration (HRC) often requires robot intentions and internal states to be conveyed to users for task efficiency and safety. Recently, augmented reality (AR) situated analytics provide such real-time robot feedback in HRC contexts. However, AR situated analytics can obstruct important real-world elements, posing safety and usability risks, especially when content is dynamically positioned relative to movements of mobile robots in a warehouse HRC scenario. In this paper, we introduce the Augmented Reality Technique Of Obstruction Deterrence while Aiding Robotic Teaming for Users (ARTOO-DARTU), an AR system tailored specifically for warehouse HRC that enables real-time robot situated analytics and control while preserving visibility of the real world through an obstruction detection and mitigation pipeline (ODM) that is uniquely suited for AR-HRC. To evaluate ARTOO-DARTU, we developed Pocket MonstARs, a controlled gamified abstraction of HRC warehouse inventory picking in which virtual monsters serve as proxies for pick targets, while labeled and object-marked boxes preserve the real-world identification demands of the picking task. In a 34-participant user study, we found that our designed AR situated analytics yielded a 46% increase in efficiency on the overall HRC task, but only when the ODM was active. Participants with the ODM active were also 61% faster on subtasks requiring visibility of the real world. Our findings demonstrate that, when paired with our developed ODM to prevent real-world obstructions, the situated analytics in ARTOO-DARTU can significantly enhance efficiency and user experience in AR-HRC warehouse scenarios.

---


### 70. [ASAP: Agent-System Co-Design for Wall-Clock-Centered Auto HPO Research for ML Experiments](https://arxiv.org/abs/2606.25207)

**<font color=#1a73e8>作者：</font>** Taicheng Guo, Haomin Zhuang, Kehan Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperparameter Optimization (HPO) is essential for maximizing machine learning model performance, and its core challenge is sample efficiency: finding strong configurations within a limited budget. Because every HPO tool relies on a surrogate prior that imparts its own inductive bias, individual tools struggle once problems become sufficiently diverse and drift from these priors. Motivated by the reasoning and generalization capabilities of LLMs, recent work has explored using LLMs for HPO and reports improved per-iteration performance. Yet these methods share two limitations with a common origin: they use the LLM as a single-tool replacement evaluated by iteration count. (i) Deployed in place of prior tools, the LLM is itself constrained by its pretraining objective to one family of inductive-biased proposals; this single-source setup still fails to handle the full diversity of problems. (ii) Per-iteration evaluation ignores that, in real runs, LLM inference or tool execution is paid serially on top of model evaluation every round, so iteration-count gains do not translate into end-to-end wall-clock gains. We present ASAP, an agent-system co-design that addresses both limitations. On the agent side, ASAP uses the LLM to integrate a diverse pool of inductive-biased optimizers and to select among their proposals each round. On the system side, ASAP re-architects the loop to reduce end-to-end wall-clock while preserving regret quality: a prefix-stable prompt maximizes KV-cache reuse across rounds; speculation parallelism hides the remaining LLM and tool latency under model evaluation via a relative-error accept test; and a Self-Tuner adapts the speculation threshold from execution logs off the critical path. Extensive experiments on diverse modern HPO tasks show that ASAP consistently outperforms baselines, underscoring the value of tool integration and agent-system co-design.

---


### 71. [Reflective VLA: In-Context Action Consequences Make VLAs Generalize](https://arxiv.org/abs/2606.25215)

**<font color=#1a73e8>作者：</font>** Qing Lian, Kent Yu, Lei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most vision-language-action (VLA) models are reactive: they predict the next action from the current instruction and observation, implicitly assuming that the current observation fully specifies the action-relevant state. In embodied control, however, embodiment-specific factors such as camera-to-robot geometry, robot calibration, or systematic actuation bias are often hard to identify from a single observation. As a result, reactive policies cannot reliably disambiguate these factors in general, overfitting to training environments and generalizing poorly at deployment. We propose Reflective VLA, which conditions each decision on a context of observation-action-consequence triplets. Each triplet records not only what the robot observed and executed, but also how the scene changed afterward, exposing the deployment-specific mapping from actions to observed effects. Architecturally, Reflective VLA routes all observation modalities through the VLM under shared attention, so the action expert reasons directly over past triplets and the current observation. A block-causal mask enables parallel multi-frame training without leakage and supports KV-cached real-time inference. On standard LIBERO and SimplerEnv-Bridge, Reflective VLA preserves strong in-distribution performance. Under distribution shift on LIBERO-Plus and the harder LIBERO-Plus-Hard, it improves average success rate by 5.4 and 4.2 percentage points over a matched reactive baseline. Ablations with a matched history-only baseline further show that action consequences -- rather than additional context length alone -- are the key to cross-environment generalization. Project page: this https URL

---


### 72. [Homomorphic Encryptions for Privacy Preserving Vision](https://arxiv.org/abs/2606.25216)

**<font color=#1a73e8>作者：</font>** Preey Shah, Rohan Virani, Sanjari Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Legal requirements might prevent organizations from sharing sensitive data like medical or financial details of consumers which prevents them from leveraging cloud based ML-as-a-service solutions provided by third party providers, which are quickly gaining popularity these days. In this project, we aim to perform inference tasks in Computer Vision in a privacy-preserving manner, i.e, by only looking at encrypted data. Recent advances in fully homomorphic encryption make this possible. A fully homomorphic encryption allows an arbitrary sequence of additive and multiplicative operations to be performed on encrypted data directly. Applying homomorphic encryptions to CNNs requires modifying the conventional CNN layers, so that they adhere to the encryption scheme. Our aim was to explore the best methods to create CNNs which can classify encrypted images directly. We used Microsoft SEAL for performing homomorphic encryption. The performance of these "encryption based CNNs" should be comparable with baseline accuracies of the same CNNs trained on unencrypted data, and the aim was to achieve as low of a hit on inference-time performance as possible. We successfully obtained minimal drop in classification accuracy for various datasets. We used MNIST as our baseline, which is popularly used in related research work and then explored more complex datasets like Kuzushiji MNIST, Fashion-MNIST and CIFAR-10 as a part of our contribution. Additionally, we also added support for more complex operations on top of TenSEAL, like processing colored images (multi-channel input), applying multiple convolutional layers and performing average pooling.

---


### 73. [Cage-based Texture Transfer with Geometric Filtering](https://arxiv.org/abs/2606.25220)

**<font color=#1a73e8>作者：</font>** Rose Mei Zhou, Lynnette Hui Xian Ng, Adrian Xuan Wei Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time texture transfer expands the creative horizon for interactive applications, enabling seamless detail projection in scenarios that range from digital character cosmetics to procedural automotive texturing. Yet, its practical application is governed by inherent trade-offs between processing speed and suppression of artifacts. Low-latency transfer methods frequently fail to suppress artifacts, and robust alternatives rely on large-scale models that are costly in training and memory. Our proposed method bridges the gap between efficiency and robustness by using a cage-based geometric filtering method to identify Non-Cosmetic Zones (NCZs) for artifact suppression. While other models are resource-intensive and require multiple days of training on manually annotated datasets, we are able to successfully suppress artifacts and achieve immediate deployment on consumer-grade hardware. Our framework achieved highly efficient runtimes of ~70ms on mobile devices for a ~4.8k triangle mesh.

---


### 74. [MJEPA: A Simple and Scalable Joint-Embedding Predictive Architecture for Audio-Visual Learning](https://arxiv.org/abs/2606.25225)

**<font color=#1a73e8>作者：</font>** Revant Teotia, Adrien Bardes, Michael Rabbat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning from large-scale video data has emerged as a dominant paradigm for visual representation learning. Since audio and visual streams naturally co-occur in video data, extending this success to jointly learn from both modalities is a natural next step, yet it remains challenging. Existing audio-visual self-supervised methods rely on modality-specific encoders and complex combinations of contrastive or reconstruction objectives, limiting cross-modal synergy and scalability. Joint Embedding Predictive Architectures (JEPAs) offer a simple, modality-agnostic alternative, but have to date been applied primarily to individual modalities. We introduce MJEPA, a joint-embedding predictive architecture for audio-visual learning that uses a single, unified encoder for both modalities. Our approach uses only a single predictive objective, applied both within and across modalities. We show that cross-modal prediction is critical: without it, a shared encoder degrades below unimodal baselines; with it, each modality's representation benefits from the other. Our frozen ViT-g model outperforms the best prior frozen baseline by over 6.8 mAP on AudioSet-20K, surpasses fully finetuned models on ESC-50 and FSD50K, and is competitive on video benchmarks despite using 10x less video data.

---


### 75. [Towards Structuring an Arabic-English Machine-Readable Dictionary Using Parsing Expression Grammars](https://arxiv.org/abs/2606.25231)

**<font color=#1a73e8>作者：</font>** Diaa Mohamed Fayed, Aly Aly Fahmy, Mohsen Abdelrazek Rashwan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dictionaries are rich sources of lexical information about words that is required for many applications of natural language processing and human language technology. However, publishers prepare printed dictionaries for human usage not for machine processing. This paper presented a method to structure partly a machine-readable version of the Arabic-English Al-Mawrid dictionary. The method converted the entries of Al-Mawrid from a stream of words and punctuation marks into hierarchical structures. The hierarchical structure expresses the components of each dictionary entry in explicit format. A dictionary entry is composed of subentries and each subentry consists of defining phrases, domain labels, cross-references, and translation equivalences. We designed the proposed method as cascaded steps where parsing is the main step. We implemented the parser using the parsing expression grammars formalism. In conclusion, although Arabic dictionaries do not have microstructure standardization, this study demonstrated that it is possible to structure them automatically or semi-automatically with plausible accuracy after inducing their microstructure.

---


### 76. [Semantic Allocation in Ordered Bottlenecks: Predictive Residual Inference for Visual Representation Learning](https://arxiv.org/abs/2606.25232)

**<font color=#1a73e8>作者：</font>** Erik Ayari, Manuel Traub, Martin V. Butz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ordered bottlenecks aim to provide utility at flexible budgets by assigning coarse information to early tokens and task-relevant detail to later ones. Prior work, including tail dropping (TD), typically enforces ordering by means of a masking-based ordering pressure (MBOP): Late tokens are masked more frequently than early tokens and are therefore encouraged to store less essential fine details. We introduce predictive residual inference for ordered representations (PRIOR), a framework designed to address inherent weaknesses of MBOP. MBOP is prone to weak late-token utility because it lacks an explicit refinement objective and uses gradient exposure as a proxy for importance. Furthermore, representations may become particularly brittle in optimization-sensitive settings, such as when using discrete or quantized token representations. PRIOR replaces activation-rate control with log2-scaled levels and level-wise predictors. These predictors separate already explained from unexplained information, focusing each level on residual error. We compare PRIOR against MBOP-TD and independent tail-biased dropout (MBOP-ITD) in contrastive learning and image reconstruction tasks. Unlike the baselines, PRIOR learns well-ordered representations across experiments: low budgets provide coarse descriptors, while high budgets add refinements. Simultaneously, full-budget performance with PRIOR is higher in all but one experimental setting, where performance remains comparable. MBOP baselines are severely limited in discrete and quantized settings, while PRIOR approaches the performance of continuous counterparts. Taken together, these findings establish PRIOR as an effective framework for ordered representation learning.

---


### 77. [Structuring Sparsity: Block-Sparse Featurizers Capture Visual Concept Manifolds](https://arxiv.org/abs/2606.25234)

**<font color=#1a73e8>作者：</font>** Thomas Fel, Matthew Kowal, Mozes Jacobs 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> What is the geometry of a visual percept? The most widely used protocols for decomposing neural network representations into interpretable parts treat concepts as isolated directions, yet recent work shows that concepts are often realized as geometric structures in low dimensional regions of activation space. We turn to the literature of Structured sparsity to close this gap, and show that block sparsity, which groups directions into blocks, is the prior matched to a generative model in which a representation is a sparse sum of low-dimensional manifolds: the modern, learned form of a classical idea in visual neuroscience, where a visual feature is carried by a coordinated group of neurons rather than a single tuned one. We implement three variants of block-sparse featurizers (BSFs) and, through a minimum-description-length analysis, show that all three describe activations more compactly than direction-based featurizers, with the recovered concepts typically two- to four-dimensional. We then use BSFs to (i) recontextualize prior work, showing that curve detectors in InceptionV1 actually read from a single continuous curve manifold, (ii) discover novel manifolds including shadows and lighting in DINOv3, and (iii) support interpretable control of image generation in diffusion models (SDXL) via manifold steering.

---


### 78. [OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos](https://arxiv.org/abs/2606.25245)

**<font color=#1a73e8>作者：</font>** Oussema Dhaouadi, Zuria Bauer, Johannes Michael Meier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous 6-DoF pose estimation is essential for autonomous UAV operations. Yet, existing visual odometry and SLAM methods accumulate drift and yield only relative, up-to-scale trajectories. Single-frame geo-localization, in turn, discards temporal continuity and remains too slow for real-time use. We present OrthoTrack, a training-free system that estimates continuous 6-DoF UAV trajectories using only publicly available orthophotos and surface models as a map prior. OrthoTrack matches keyframes against the orthophoto and lifts correspondences to metric 3D via the surface model. It then propagates these map-anchored correspondences to intermediate frames with optical flow, producing absolute, metrically scaled poses at every frame without GPS or post-hoc alignment. We also introduce the MovingDrone Dataset, a large-scale benchmark pairing photorealistic UAV sequences with dense 6-DoF ground truth and co-registered multi-modal geodata including multi-temporal orthophotos. On MovingDrone and real-world benchmarks, OrthoTrack runs in real time on a single GPU. It outperforms all baselines by a large margin, even those receiving oracle scale and alignment. By relying on publicly available geodata, OrthoTrack enables deployment to new regions without site-specific adaptation.

---


### 79. [Multilingual Hematology Visual Question Answering Dataset](https://arxiv.org/abs/2606.25246)

**<font color=#1a73e8>作者：</font>** Hajra Malik, Hafiza Tooba Aftab, Abdul Rehman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) have shown promising capabilities in medical image analysis by jointly understanding visual and textual information for tasks such as Visual Question Answering. However, existing hematology vision-language resources remain predominantly English centric, limiting their applicability in multilingual healthcare environments. This challenge is releveant generally to South Asia and specifically to Pakistan, where Urdu is widely used despite healthcare information and digital medical systems being largely dependent on English. To investigate this gap, we conducted a survey among healthcare professionals, which revealed substantial language mismatches between clinical documentation and patient communication, emphasizing the need for multilingual healthcare technologies. To address this limitation, we introduce WBCMor VQA, a clinically validated bilingual English, Urdu morphology aware VQA benchmark for leukemia and normal white blood cell analysis. The benchmark is constructed using morphology-aware annotations from LeukemiaAttri and WBCAtt datasets and supported by a domain specific Urdu hematology dictionary to ensure linguistic consistency and clinical correctness. The final benchmark contains 110K bilingual question answer pairs serving as VQA annotations for 20K leukemic and normal single-cell images. Furthermore, we establish baseline performance by evaluating multiple open-source VLMs on the proposed benchmark. The proposed resource aims to facilitate the development of accessible and clinically relevant AI systems for multilingual healthcare environments.

---


### 80. [FUTO Swipe: Layout-Agnostic Neural Swipe Decoding](https://arxiv.org/abs/2606.25247)

**<font color=#1a73e8>作者：</font>** David Lee Miller, Aleksandras Kostarevas  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Neural swipe decoders are typically tied to the keyboard they were trained on, requiring a new corpus and training run for each layout. In this report, we document our approach toward training models that can function on any contiguous mobile keyboard layout. At each point along the swipe, our encoder predicts whether the user is indicating a character and where on the keyboard that character lies. The keyboard layout is supplied at inference time and used to map the spatial and temporal prediction to a logit at each key, rather than being learned during training.
Training neural models requires substantial data, but public swipe data is limited, particularly for non-QWERTY layouts. We release this http URL, the largest MIT-licensed swipe corpus we are aware of, containing over 1M donated swipes from more than 12k donor sessions. To generalize beyond the English QWERTY layout, we apply geometric augmentations to both the swipe trajectory and the keyboard layout at every training step, forcing the model to make predictions based on characteristics of the swipe gesture rather than the training layout. The model generalizes to layouts absent from training, in some cases more accurately than the layout it was trained on. This combines the layout-flexibility of an algorithmic decoder with the accuracy of a neural model. Trained models are publicly available.

---


### 81. [Sponsored Group Signature and its Application to Privacy-preserving Guest Access in Smart Environments](https://arxiv.org/abs/2606.25248)

**<font color=#1a73e8>作者：</font>** Sepideh Avizheh, Reihaneh Safavi-Naini, Shiwei Sun  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Group signatures are privacy preserving signature schemes in which a group member can anonymously sign messages on behalf of the group, while providing accountability, by allowing the signature of a misbehaving group member be ``opened'' and the identity of the signer be revealed. In group signature members are admitted to the group by a (trusted) group manager. We motivate the need for a flexible mechanism in applications, such as privacy preserving access in smart environments, and propose a two-level member-join group signature that we call SPonsored Group Signature (SPGS) where group members of level 1 can ``sponsor'' new members, in level 2, to join the group. This relaxation of user join comes with additional accountability mechanisms: we require that the signature of a sponsored member can be opened to the identity of the sponsor (that is sponsor is responsible for the sponsored member), and while all signatures are anonymous, for the sponsored members, the signatures are linkable. This allows a sponsor to efficiently identify an undesirable sponsored member. We formalize SPGS scheme, define its security using a game-based approach, and give a generic construction of SPGS that uses a (dynamic) group signature scheme, a commitment scheme, and a knowledge-sound non-interactive zero knowledge proof of knowledge, and prove its security. We also give an instantiation of our construction. To show applicability of SPGS in practice, we consider the problem of providing guest access in a smart building, and introduce Anonymous Guest Access Token (AGAT) that allows a temporary guest to anonymously access (a subset of) the building resources. We show how SPGS can be used (together with an IND-CPA secure public key encryption scheme) to give a direct construction for AGAT, and show the efficiency of our guest access protocol when it is instantiated with existing schemes.

---


### 82. [Automatic Generation of Highlights for Academic Paper Via Prompt-based Learning](https://arxiv.org/abs/2606.25253)

**<font color=#1a73e8>作者：</font>** Yi Xiang, Chengzhi Zhang, Heng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Highlights provide a concise summary of the main contributions of an academic paper and help readers quickly understand its focus. However, many journals do not provide highlights, which limits their use in literature retrieval, text mining, and bibliometric analysis. Existing studies have explored supervised learning methods for automatic highlight extraction, but these methods usually require large amounts of labeled training data. This study investigates prompt-based learning for automatic highlight generation. We design task-specific prompt templates and combine them with paper abstracts as model inputs. Several language models are evaluated, including locally deployed pre-trained models such as GPT-2 and T5, as well as ChatGPT accessed through an API. Experiments on three datasets show that ChatGPT with prompt templates achieves performance comparable to previous supervised methods without using task-specific training samples. When a small number of examples are added to the prompts, the model significantly outperforms state-of-the-art methods on two datasets. We further analyze how prompt design affects generation quality and find that, although ChatGPT has strong language modeling ability, its performance on this task is highly sensitive to the information provided in the prompt. Case studies also show that the generated highlights are generally coherent, informative, and close to author-written highlights. This study is among the first to apply prompt-based learning to academic highlight generation. The proposed method does not rely on domain-specific training corpora and can generate highlights for papers that lack such information, thereby supporting downstream text mining and bibliometric research.

---


### 83. [Cross-Modality Structural Guidance in 3D Latent Diffusion for Robust FLAIR Super-Resolution](https://arxiv.org/abs/2606.25255)

**<font color=#1a73e8>作者：</font>** Haoyu Lan, Jiazhen Zhang, John Onofrey 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution (HR) MRI acquisition is often hampered by scan time constraints, resulting in anisotropic or low-resolution scans (e.g., thick-slice FLAIR) that limit diagnostic accuracy. While deep learning-based super-resolution (SR) methods show promise, they often hallucinate anatomical details, which can compromise brain structural integrity. To mitigate this limitation, we introduce MR-DiffuSR, a Multi-Resolution Diffusion-based Super-Resolution framework that incorporates HR T1w structural image priors to guide the restoration of thick-slice FLAIR scans and operates in the 3D latent space. Our architecture introduces cross-modality structural swin-attention, which derives structural attention maps from the HR T1w and applies them to the low-resolution FLAIR latent features. This design disentangles anatomical structure from modality-specific contrast, effectively preventing hallucinations. Furthermore, we employ a mixed-scale degradation strategy, training the model on a continuum of downsampling factors to ensure robustness to varying slice thicknesses, while optimizing with a DINOv3-based perceptual loss to preserve high-frequency semantic details. Evaluated on the ADNI-4 dataset, MR-DiffuSR surpasses both CNN and 2D diffusion approaches, achieving an average PSNR of 32.46dB, SSIM of 0.97, and LPIPS of 0.07 across all downsampling factors. In downstream white matter hyperintensity segmentation, our model demonstrates exceptional robustness. While baseline performance collapses at 10x down-sampling (Dice: 0.51), MR-DiffuSR maintains a Dice score of 0.63, preserving utility even at 7mm equivalent slice thickness.

---


### 84. [Pre-Warm: Input-Conditioned Weight Initialization for Convolutional Neural Networks](https://arxiv.org/abs/2606.25256)

**<font color=#1a73e8>作者：</font>** Rowan Martnishn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Pre-Warm, a simple yet effective zero-training-cost method for data-conditioned initialization of the first convolutional layer. Before the first forward pass, Pre-Warm extracts mean-centered local patches from a single training batch, clusters them with MiniBatchKMeans, applies inverse Manhattan spatial weighting, and uses the resulting centroids to initialize half of the first-layer filters (the remainder retain Kaiming initialization).
We derive closed-form rules for all hyperparameters except a single insensitive scale parameter, though we derive a Kaiming parity bound on scale from patch dimensionality. For grayscale datasets we use Otsu's foreground density; for natural color images we use the mean L2 norm of mean-centered patches. Both rules accurately predict the optimal patch count observed in grid search.
Across five standard benchmarks -- MNIST, Fashion-MNIST, CIFAR-10, SVHN, and CIFAR-100 -- and 8-seed paired experiments, Pre-Warm yields statistically significant accuracy improvements over standard Kaiming initialization (p < 0.05 on all datasets, p = 0.0007 on SVHN with 8/8 wins, p = 0.0033 on CIFAR-100 with 7/8 wins). The method adds negligible overhead, requires no architectural changes, and integrates into existing training pipelines with only a few lines of code.
Pre-Warm demonstrates that even a lightweight, input-dependent signal can meaningfully improve optimization trajectories in modern convolutional networks.

---


### 85. [Variational Inference via Entropic Transport Descent](https://arxiv.org/abs/2606.25265)

**<font color=#1a73e8>作者：</font>** Vincent Pacelli, Akash Ratheesh, Evangelos Theodorou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Particle-based variational inference (ParVI) methods approximate an intractable target distribution by evolving an ensemble of interacting samples. Existing approaches rely predominantly on kernel-based repulsion (e.g., SVGD), which suffers from variance collapse in high dimensions and mode collapse on multimodal targets -- pathologies caused by the absence of global transport structure. We introduce entropic transport descent (ETD), a ParVI family that frames each particle update as an entropy-regularized optimal transport problem. Derived from the JKO proximal scheme by lifting to the space of couplings and relaxing via the KL chain rule, each ETD iteration reduces to a Sinkhorn computation. The resulting transport plan provides global coordination, guiding each particle to nearby high-density proposals and naturally preserving multimodal structure. ETD can operate entirely score-free, requiring only pointwise evaluations of the unnormalized target density. Experiments on variance-collapse diagnostics, Bayesian logistic regression, neural networks, and molecular Boltzmann distributions show that ETD matches or outperforms SVGD, AGF-SVGD, and SGLD, with the largest gains in high-dimensional and multimodal settings.

---


### 86. [Inverse Reinforcement Learning for Interpretable Keystroke Biomarkers in Parkinson's Disease](https://arxiv.org/abs/2606.25270)

**<font color=#1a73e8>作者：</font>** Navin Bondade  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Keystroke dynamics have been explored extensively as a passive digital biomarker for Parkinson's disease (PD), typically by extracting summary statistics from typing timing and training a classifier to discriminate PD from healthy controls. We instead apply inverse reinforcement learning (IRL) to keystroke data, modeling each keystroke as a discrete choice over typing speed and recovering, per subject, an interpretable reward function that explains their observed timing behavior. To our knowledge this is the first application of IRL to keystroke dynamics. On the public neuroQWERTY MIT-CSXPD dataset (85 subjects, 42 with PD), an initial four-parameter reward decomposition (speed, effort, smoothness, hand-alternation cost) was found to suffer severe feature collinearity between two terms ($r=1.000$ in typical contexts); we diagnose and correct this, yielding an identifiable three-parameter model. The recovered speed-preference weight correlates with UPDRS-III severity at $r=-0.607$ ($p<0.001$, $n=42$), replicates independently across two sub-cohorts, is stable across nine sensitivity configurations, and retains a statistically significant contribution beyond raw typing speed alone (incremental $R^2$ from 0.194 to 0.338, $p=0.006$). Two other recovered weights (consistency, hand-alternation) did not survive confound checks and are reported as negative results. We document two implementation bugs found during adversarial code review (session-boundary contamination, a rolling-window data leakage) and show the headline result is materially unchanged after fixing both. We discuss this result in the context of a literature where reported accuracies vary widely between studies (pooled AUC 0.85, I^2=94% in a 2022 meta-analysis), and argue that the validation process itself, not only the correlation coefficient, is part of the contribution.

---


### 87. [Co-designing a Preliminary Repository of Augmented Reality Concepts for Real-Time Emotion Regulation](https://arxiv.org/abs/2606.25271)

**<font color=#1a73e8>作者：</font>** Graciela Camacho-Fidalgo, Edgar Rojas-Muñoz  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Augmented Reality (AR) can be a positive therapeutic approach to support mental health and emotion regulation. Although AR techniques for therapeutic support exist, there is no user-centered, expert-informed understanding of how real-time AR designs can support people in emotional distress without disengaging them from their ongoing activities. This lack of reusable design resources hinders the adoption of AR for mental health support. This paper addresses this gap by introducing a co-designed collection of AR interventions describing how this technique can support real-time emotion regulation. The repository was created following a two-phase participatory design process. Phase 1 recruited 40 anxiety-prone individuals and used the Nominal Group Technique to list ideas on how AR affordances could support emotion regulation. Phase 2 recruited 10 mental health professionals to organize these ideas into thematic clusters and assess their clinical feasibility. The resulting AR design repository, grounded in user perspective and clinical expertise, identifies eight thematic clusters and 106 design ideas. This work represents a first step towards the development of seamless real-time AR interventions for mental health.

---


### 88. [CoGeoAD: Hierarchical Color-Geometric Fusion with Multi-View Attention for Zero-Shot 3D Anomaly Detection](https://arxiv.org/abs/2606.25273)

**<font color=#1a73e8>作者：</font>** Ke Xu, Xinle Wang, Yanning Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot 3D anomaly detection is essential for industrial quality inspection, where labeled anomaly samples are scarce. Meanwhile, existing methods lack an effective mechanism to fuse complementary 2D color images with 3D geometric structures, limiting their ability to detect both surface and structural defects in a unified framework. To address these issues, we propose CoGeoAD, a unified CLIP-based framework that fuses color and geometric features by constructing pixel-aligned paired multi-view images. The framework introduces a Data-Driven Multi-View Attention (MVA) mechanism to adaptively aggregate 3D features and a Multi-Stage Color-Geometric Fusion (MS-CGF) module to hierarchically integrate multi-level features from both modalities. Extensive experiments on the MVTec3D-AD and Eyecandies benchmarks demonstrate that CoGeoAD achieves state-of-the-art performance, effectively capturing both structural and textural anomalies in complex industrial scenarios. our source code is available at this https URL.

---


### 89. [UC-Search: Risk-Aware Test-Time Search for Delayed Constrained Time-Series Control](https://arxiv.org/abs/2606.25274)

**<font color=#1a73e8>作者：</font>** Xibai Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series models are usually scored as forecasters, yet deployed systems often require delayed decisions under uncertainty and hard feasibility constraints. UC-Search is a model-agnostic test-time wrapper: a backbone emits forecasts or action scores, a feasibility automaton rolls candidate paths forward, and bounded search returns the first action of a risk-adjusted feasible trajectory. We instantiate UC-Beam and a UCT-style UC-MCTS diagnostic, using epistemic, aleatoric, and propagated uncertainty mainly as path-risk terms. A myopic-collapse/separation theorem states when search reduces to one-step risk-greedy and when delayed feasible-set coupling can create non-myopic value. Primary evidence comes from a predeclared public $9$-family, $33$-series delayed-control suite with six held-out starts per series: UC-Pareto is positive versus validation-selected CEM, MPPI, and risk-aware random at the normalized threshold ($+3.1675/+2.3328/+2.5038$), and remains positive in a compute-matched audit ($+2.8466/+2.7418/+2.7429$). ETT/LTSF delayed-inventory validation supports the same compute-frontier claim. A 48-series raw M4 standard periodic-review lost-sales inventory audit is positive versus the strongest classic base-stock control ($+13556.7547$), CEM ($+64900.2207$), and risk-random ($+52881.6042$), while MPPI remains family-mixed. FI-2010, official-forecast adapters, SB3/FQI controls, direction/capacity/intervention checks, and synthetic mechanism tests are reported as boundary or mechanism evidence rather than broad dominance claims.

---


### 90. [Heterogeneous and Adept Snapshot Distillation for 3D Semantic Segmentation](https://arxiv.org/abs/2606.25278)

**<font color=#1a73e8>作者：</font>** Xiaopei Wu, Yuenan Hou, Junkai Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal fusion and multi-model ensembling are prevalent in enhancing the performance of 3D semantic segmentation. Despite the impressive performance, these methods either rely on auxiliary input signals or suffer from costly computational expense. To efficaciously enhance the segmentation performance without introducing intolerable costs, we propose to transfer the rich knowledge from the multi-modal model (i.e., point clouds and images) and multiple model experts to the point-cloudbased network through knowledge distillation. Specifically, we present Information-oriented Heterogeneous Distillation (IHD) to help the uni-modal model absorb the complementary knowledge from the multi-modal teacher. We design the Information-Oriented Filtering (IOF) strategy to select informative images from the continuous image sequence for multi-modal fusion. This practice can boost the performance of the multi-modal teacher, thus benefiting the learning of the student. Besides, as opposed to vanilla model ensembling that requires the separate training of each expert, we propose Adept Snapshot Distillation (ASD). ASD treats the freely available model snapshots generated during the training phase as multiple experts, which significantly reduces the training cost for model ensembling. For each expert teacher, it only provides supervision to the student in the class where it is adept. The resulting Heterogeneous and Adept Snapshot Knowledge Distillation, dubbed HAS-KD, attains state-of-the-art results on ScanNetV2 and S3DIS datasets. HAS-KD can be seamlessly integrated into contemporary 3D segmentation algorithms and bring considerable gains without introducing extra inference burdens. The code will be made publicly available upon publication.

---


### 91. [MRI2Rep: Autoregressive Structured Report Generation for 3D Liver MRI](https://arxiv.org/abs/2606.25279)

**<font color=#1a73e8>作者：</font>** Xinran Li, Junlin Yang, Annabella Shewarega 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manual reporting of 3D MRI studies is time-consuming, yet end-to-end structured report generation for 3D liver MRI remains underexplored due to volumetric complexity and scarce paired data. We propose MRI2Rep, an autoregressive framework for liver MRI report generation. From 3,929 real-world MRI-report pairs acquired over a 10-year single-institution cohort, a Report-to-Label Canonicalization (RLC) module converts free-text reports into structured, closed-vocabulary diagnostic sequences without lesion-level annotations. On a held-out test set, MRI2Rep achieves 76.0% case-level sensitivity, 29.4% lesion-level F1, compared with no more than 8.3% for adapted medical vision-language baselines, and 82.4% liver-level accuracy. In a blinded reader study, two radiologists rated 75% and 70% of AI-generated reports as clinically acceptable, compared with 95% and 100% for original reports. Our automated LLM-based judge, LLM-Eval, rated 61.8% of AI-generated reports as acceptable, applying a stricter standard and supporting its use as a conservative proxy. To our knowledge, this is the first end-to-end LI-RADS-structured reporting system for 3D liver MRI.

---


### 92. [Evaluation Protocols and Validation for Cameras in Indoor Healthcare Monitoring](https://arxiv.org/abs/2606.25284)

**<font color=#1a73e8>作者：</font>** Amirhossein Dadashzadeh, Jingjing Liu, Qianhui Men 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based monitoring systems are increasingly adopted in healthcare settings for the continuous assessment of patient movement and activities. However, their technical performance under real-world indoor conditions remains insufficiently characterised, preventing appropriate camera selection for clinical or home adoption and reproducibility. Existing validation studies typically assess either device metrological performance or algorithm accuracy in isolation, and often do not systematically account for practical deployment factors, such as lighting variability, occlusions, and camera positioning. We present two technical validation protocols: the first evaluates the metrological performance of RGB and RGB-D cameras, and the second assesses their use in supporting human pose estimation, validated using state-of-the-art pose estimators. The proposed protocols systematically assess five cameras, four RGB-D and one RGB, under controlled variations in lighting, camera height, viewing angle, and occlusion level within representative indoor scenarios. The experimental results show that metrological performance varies substantially across cameras, with depth bias at 5 m ranging from 50 mm to over 1400 mm depending on the device. For 2D pose estimation, all cameras achieve broadly comparable accuracy, with mean mAP between approximately 78% and 90% across cameras and estimators, whereas 3D reconstruction error differs markedly across devices, with MPJPE ranging from 104 mm to 365 mm, closely reflecting underlying depth-sensing quality. Environmental factors have a camera- and estimator-dependent effect on 3D performance, while camera mounting height has minimal influence within the evaluated range. This work provides evidence-based guidance for the selection and deployment of cameras in healthcare monitoring applications, addressing an important gap in current technical validation practice.

---


### 93. [The Digital Pirahã Condition: Ecological Mismatch and the Reconstruction of Recursive Cognition](https://arxiv.org/abs/2606.25287)

**<font color=#1a73e8>作者：</font>** Dhushy Thillaivasan, Samar Shailendra, Kristina Nicholls 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Contemporary digital and AI-mediated environments are reshaping the cognitive ecologies within which human reasoning develops. As everyday activity becomes embedded in datafied infrastructures, cognitive habits adapt to conditions of immediacy, fragmentation, externalisation, and algorithmic filtering. This paper introduces the Digital Pirahã Condition, a cultural ecological model explaining how these environments cultivate adaptive but shallow cognitive patterns, epistemic flattening, reduced recursive capacity, and heightened reliance on external scaffolds. While functional within digital systems, these adaptations create an ecological mismatch with the recursive, integrative reasoning required in academic and institutional activity systems. The paper argues that this mismatch is an ecological outcome rather than a psychological deficit, and that addressing it requires intentional cognitive niche construction within educational institutions. The lecturer is conceptualised as a cultural entrepreneur who reconstructs the cognitive ecology of learning through analog sanctuaries, AI-supported metacognitive scaffolds, and recursive curriculum architectures. The Digital Pirahã Condition thus provides a theoretical lens for understanding contemporary cognitive change and a framework for ecological redesign in AI-mediated societies.

---


### 94. [Communicability-Inspired Positional Encoding (CIPE)](https://arxiv.org/abs/2606.25293)

**<font color=#1a73e8>作者：</font>** Yipeng Zhang, Zhongtian Sun, Pietro Liò 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Positional encodings (PEs) are essential for Transformers. Yet designing effective PEs for non-Euclidean graphs remains challenging. Such encodings should ideally induce an Attention-Compatible Geometry for self-attention: not merely describing graph structure, but defining a geometry whose inner products reflect meaningful structural relatedness. To realize this geometry, we propose Communicability-Inspired Positional Encoding (CIPE), built from communicability, a measure between pairs of nodes that aggregates contributions from paths of all lengths. By construction, CIPE inner products recover communicability, converting global multi-path connectivity into an attention-ready similarity geometry. For practical Transformer training, we introduce dimensionality alignment, mapping graph-size-dependent CIPE representations to prescribed dimensions while faithfully preserving the induced geometry. Empirically, CIPE improves structure-agnostic Transformers by 35.5% on average across seven benchmarks, outperforming representative PEs; it also consistently improves structure-biased graph Transformers, where competing PEs often yield only marginal benefits. These results position CIPE as a principled framework for attention-compatible graph positional encodings.

---


### 95. [Minimalist Preprocessing Approach for Image Synthesis Detection](https://arxiv.org/abs/2606.25297)

**<font color=#1a73e8>作者：</font>** Hoai-Danh Vo, Trung-Nghia Le  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models have significantly advanced image generation, resulting in synthesized images that are increasingly indistinguishable from authentic ones. However, the creation of fake images with malicious intent is a growing concern. Low-configured smart devices have become highly popular, making it easier for deceptive images to reach users. Consequently, the demand for effective detection methods is increasingly urgent. In this paper, we introduce a simple yet efficient method that captures pixel fluctuations between neighboring pixels by calculating the gradient, which highlights variations in grayscale intensity. This approach functions as a high-pass filter, emphasizing key features for accurate image distinction while minimizing color influence. Our experiments on multiple datasets demonstrate that our method achieves accuracy levels comparable to state-of-the-art techniques while requiring minimal computational resources. Therefore, it is suitable for deployment on low-end devices such as smartphones. The code is available at this https URL.

---


### 96. [KidRisk: Benchmark Dataset for Children Dangerous Action Recognition](https://arxiv.org/abs/2606.25298)

**<font color=#1a73e8>作者：</font>** Minh-Kha Nguyen, Trung-Hieu Do, Kim Anh Phung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Children are naturally energetic, and during their spontaneous activities, they often encounter potentially dangerous situations, especially when lacking parental supervision. Identifying actions that pose risks plays a crucial role in ensuring their safety. This paper build a novel challenging dataset, namely KidRisk, including 2,500 short videos of children's actions and 10,000 images for dangerous action of children. We also introduce a benchmark on our newly constructs dataset and find that traditional deep learning models demonstrated limited effectiveness on these tasks. Therefore, we develop vision-language based baselines with exceptional context understanding of visual information. Our proposed methods achieved an accuracy of 83.53% in classifying children's actions and 96.14% in recognizing children's dangerous actions, significantly outperforming traditional approaches. These results confirm that vision-language models are not only feasible but also highly effective in detecting hazardous actions, contributing positively to safeguarding children's safety.

---


### 97. [Physics Question Scene Graph: Fine-grained Evaluation of Physical Plausibility in Text-to-Video Generation](https://arxiv.org/abs/2606.25306)

**<font color=#1a73e8>作者：</font>** Atin Pothiraj, Jaemin Cho, Yue Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models are increasingly capable of producing realistic videos, but they still struggle to generate videos that follow basic physical laws. Compounding this is a lack of reliable granular evaluation methods for localizing and specifying physical law violations in videos. We address this by introducing Physics Question Scene Graph (PQSG), a hierarchical question-based evaluation pipeline. PQSG evaluates generated videos by checking their faithfulness to a prompt across objects, actions, and adherence to physical laws using a graph-based hierarchy of questions generated by a vision-language model (VLM), guided by high-quality in-context examples. By representing questions as a graph, PQSG introduces logical dependencies within questions, ensuring that each query is contextually valid. Moreover, PQSG provides granular assessments of which qualities of the video violate physical plausibility constraints. We validate PQSG by creating FinePhyEval, a dataset with physics-based prompts and corresponding generated videos from diverse state-of-the-art video generation models (Sora 2, Veo 3, and Wan 2.1), with each video annotated across multiple categories by humans. Using FinePhyEval, we measure the correlation between PQSG's fine-grained scores and human judgments, showing higher overall correlations than prior work. We also find that PQSG ranks closed-source models higher than Wan 2.1 on physical realism. Lastly, we show that the annotations we provide in FinePhyEval can also be used for subtask evaluation: we benchmark two strong VLMs on generating and answering questions, finding that while models can create human-like questions, they still fall short of human performance in answering them.

---


### 98. [ESTANet: Efficient Online Error Detection in Procedural Videos via Prediction Inconsistency](https://arxiv.org/abs/2606.25317)

**<font color=#1a73e8>作者：</font>** Shih-Po Lee, Reza Ghoddoosian, Faizan Siddiqui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An efficient and accurate system for detecting errors in procedural tasks is crucial for supporting human needs in daily life, as it can provide instant notifications and guide people to correct mistakes. In this work, we study real-time online error detection in procedural videos from a simple but overlooked perspective: the prediction behavior of action detectors themselves. Instead of designing complex architectures or specialized supervision, we observe that action detectors naturally exhibit different prediction characteristics depending on their sensitivity to input dynamics and temporal context. We therefore propose ESTANet (Error-Sensitive and Temporally-vArying Network), a lightweight framework that detects errors by exploiting inconsistencies among action predictions produced by a small set of action detectors. We construct standard and error-sensitive action detectors that behave similarly on correct executions but respond differently when errors occur. Meanwhile, detectors operating with different temporal contexts further amplify prediction inconsistencies when the procedure deviates from the intended sequence. During inference, we detect errors by aggregating mismatches between standard and error-sensitive predictions through majority voting to flag frames that contain errors. Extensive experiments on EgoPER, Assembly-101-O, and EPIC-Tent-O demonstrate that ESTANet achieves state-of-the-art performance in online error detection while maintaining real-time efficiency with a lightweight architecture. Our results highlight that leveraging the intrinsic properties of action detectors can yield a powerful and practical solution for online error detection without increasing architectural design complexity.

---


### 99. [REViT: Roto-reflection Equivariant Convolutional Vision Transformer](https://arxiv.org/abs/2606.25318)

**<font color=#1a73e8>作者：</font>** Sheir A. Zaheer, Alexander C. Holston, Chan Y. Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a discrete roto-reflection group equivariant vision transformer with convolutional attention. Roto-reflection equivariant networks preserve the rotational, flip and positional symmetry in feature maps, making them useful for tasks where orientation of the inputs is relevant to the model outputs. In image classification and object detection, most of the studies on roto-reflection equivariant models have focused on using convolutional neural networks rather than vision transformers. In this paper, we examine the challenges involved in achieving equivariance in vision transformers, and we propose a simpler way to implement a discretized roto-reflection group equivariant vision transformer. The experimental results demonstrate that our approach outperforms the existing approaches for developing discrete roto-reflection group equivariant neural networks for image classification.

---


### 100. [State Space Models Meet Remote Sensing: A Survey](https://arxiv.org/abs/2606.25329)

**<font color=#1a73e8>作者：</font>** Qinzhe Yang, Chenyang Liu, Jia Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs), designed for long-range modeling, offer linear computational complexity and strong capabilities in capturing long-range dependencies. In the field of remote sensing, SSMs have gained popularity due to their effectiveness in addressing unique challenges such as dense visual predictions, multi-modal remote sensing data, and temporal remote sensing data, which have also yielded significant advancements in customized architectures. This paper presents a comprehensive review of SSM-based approaches in remote sensing, covering most of the relevant studies since SSMs were first introduced to the field. We offer a multi-dimensional analysis examining SSM applications in remote sensing tasks and discussing advancements in architecture design. This paper not only synthesizes the rapid progress in SSM-based research but also identifies key challenges and future opportunities. By providing a detailed perspective, this paper aims to serve as a foundational resource for remote sensing researchers, offering actionable insights to foster further advancements in this evolving domain. We will keep tracing related works at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-222](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
