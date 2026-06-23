# 📦 其他研究 | 2026年06月24日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**551-600**（第 12/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-654](./part-14.md)

---

### 551. [Weighted Score-Oriented Losses for Temporally Localized Event Prediction](https://arxiv.org/abs/2606.23145)

**<font color=#1a73e8>作者：</font>** Edoardo Legnaro, Sabrina Guastavino, Francesco Marchetti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operational event-detection systems are rarely assessed by pointwise accuracy alone. In anomaly detection, changepoint detection, and warning systems, the utility of an alarm depends on its temporal position relative to an event. This produces a score-loss mismatch. Neural networks are commonly trained with classical loss functions, such as cross-entropy, whereas deployment decisions are obtained by thresholding network predictions, merging alarms through post-processing rules, and evaluating them with event-based metrics defined by detection windows and false-alarm costs. This paper studies a temporally localized specialization of weighted score-oriented loss (wSOL) for event prediction. Starting from score-oriented losses based on expected confusion matrices and from the weighted SOL framework of Marchetti et al., we consider temporal weights that discount near-event false positives and reduce false-negative penalties when an event is preceded by an admissible alarm. The resulting objective is differentiable with respect to the network predictions, and therefore can be optimized by back-propagation. It can be instantiated with balanced accuracy, true skill statistic, F1, critical success index, and related confusion-matrix scores. We evaluate the proposed approach by comparing cross-entropy, unweighted score-oriented loss, and wSOL on three benchmark datasets for time-series event prediction and detection. The results show that wSOL can improve performance when the evaluation utility is localized in time and is not already encoded by the pointwise labels.

---


### 552. [Decomposing Financial Market Dynamics via Mechanism Analysis in an Evolutionary Multi-Agent Simulation](https://arxiv.org/abs/2606.23158)

**<font color=#1a73e8>作者：</font>** Zhibao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evolutionary agent-based markets (ABMs) couple several mechanisms -- who reproduces, how price forms, how biased the agents are, how consensus propagates -- yet these are usually fixed by convention, so it is unclear which mechanism controls which emergent property. In a coevolving, endogenous-price simulator with 120 heterogeneous behavioral agents, we make four mechanisms pluggable and run matched 3x20-seed interventions. We find the levers are largely separable. (1) Selection -> diversity: a Quality-Diversity (QD/MAP-Elites) operator robustly raises strategy-mix entropy over truncation top-k (paired Delta entropy +0.27 to +1.12 bits; sign-test p<0.001; CIs exclude 0) and sustains more strategy cycling (strongest in crisis: Delta=+0.070, p=0.0004). (2) Selection does not improve realism: even a per-agent realism reward that provably steers selection does not raise 5-fact realism (Delta_5=-0.11,-0.08,+0.03; not significant). (3) Microstructure -> realism: enabling reflexive price feedback does raise realism (Delta_5=+0.13,+0.20,+0.20; crisis/bull p<0.05, all CIs positive). (4) Behavior -> fragility: amplifying behavioral bias raises a genomic fragility proxy (Delta=+10.5,+11.1,+14.4; bull p<0.001, all CIs positive) while leaving realism flat. The remaining mechanism -- consensus network topology -- shows no robust effect (honest null). The contribution is a decomposition: in these single-mechanism sweeps the mechanisms behave as approximately distinct control knobs over diversity, realism, and fragility.

---


### 553. [Substitution-Based Analysis of Structural Novelty for Generative Models of Materials](https://arxiv.org/abs/2606.23166)

**<font color=#1a73e8>作者：</font>** Masahiro Negishi, Aron Walsh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There has been rapid progress in generative artificial intelligence (AI) models for inorganic crystal design, which can efficiently generate large numbers of candidate compounds after being trained on databases of known crystals. However, it remains unclear whether they genuinely expand the accessible materials search space beyond conventional strategies such as elemental substitution within known structure types. We address this question by developing a workflow to assess whether AI-generated crystals are duplicates of training structures, reproducible by elemental substitution, or unmatched by either criterion. Applying this workflow to representative generative models reveals that 81-92% of chemically valid and metastable generated crystals are either training duplicates or substitution-derived structures. This tendency is particularly strong in high-symmetry crystal systems, even though many possible structural prototypes remain unexplored. Further analysis of the underlying structural fingerprints shows that low-symmetry structures beyond duplication or substitution can be interpreted as interpolation in training-data-rich regions, while high-symmetry duplicates appear to result from memorisation in training-sparse regions. Our findings highlight a limitation in the current generation of models that exhibit a bias towards known structural prototypes in the high symmetry regions, but enable wider exploration of the low-symmetry structural space.

---


### 554. [Position: Correct Answer, Wrong Mechanism -- When AI Scientists Defend General Claims Their Own Data Contradicts](https://arxiv.org/abs/2606.23175)

**<font color=#1a73e8>作者：</font>** Steven Young Eulig  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI scientist systems are described as tools, coauthors, or founders, but we evaluate them as if only the final answer matters. This position paper argues that outcome-only evaluation is insufficient, and that task outcome, mechanism fidelity, and epistemic honesty must be measured separately. Our evidence comes from 28 episodes of a coding agent attempting to rediscover a known particle identification observable in a Geant4 simulation, including an 8-episode probe across two additional frontier models. In 4/20 primary-model and 3/8 cross-model episodes, agents reach right-looking results through incorrect reasoning that breaks when conditions change, which we call Correct Answer, Wrong Mechanism (CAWM). Honesty and mechanism fidelity dissociate within a single agent trajectory. When given a partially misleading prior, all five agents reject the false component on evidence, yet one defends its chosen observable with physics inconsistent with its own data. In the simulation-based discovery setting studied here, coding agents prove reliable tools but unreliable scientific co-authors for open-ended claim-making, where co-author trust requires mechanism-fidelity verification they do not reliably self-apply. The failure is detectable, and we propose a lightweight test. A one-step regime-shift check needs only the agent's claim and flags the over-generalized cases. A companion recomputation flags the remaining cases when the correct observable is known. Together, these checks flag every CAWM case in this study.

---


### 555. [Interpretable Probabilistic Medical Image Segmentation via Gaussian Process with Explicit Modelling of Annotation Bias and Variability](https://arxiv.org/abs/2606.23177)

**<font color=#1a73e8>作者：</font>** Qi Li, Yuliang Huang, Shaheer U. Saeed 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based medical image segmentation models are trained using annotations that exhibit systematic bias and variability across raters. While probabilistic multi-rater approaches can emulate annotator-specific delineations, annotator characteristics are typically encoded implicitly in deep latent feature space, making direct analysis of their influence on predictive distributions less straightforward. We propose a logit-space probabilistic segmentation framework based on stochastic variational Gaussian Process that explicitly decomposes predictions into an image-dependent reference logit distribution and annotator specific perturbations parameterised by bias and variance. This formulation enables more explicit analysis on how intra- and inter-rater variability propagate to predictive distributions. We evaluate the method on a multi-annotator medical image dataset, which shows that explicitly modelling annotator specific perturbations improves uncertainty calibration while maintaining comparable segmentation accuracy, compared with state-of-the-art multi-rater probabilistic segmentation method. The learned bias and variance parameters quantitatively reflect annotator-specific behaviour. Furthermore, controlled perturbation experiments over bias and variance demonstrate how changes in annotator parameters systematically influence predictive performance. The code used in this paper is made publicly available at this https URL.

---


### 556. [EML Trees Are Universal Approximators](https://arxiv.org/abs/2606.23179)

**<font color=#1a73e8>作者：</font>** Joe Germany, Elie Abdo, Joseph Bakarji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The recently introduced EML (Exp-Minus-Log) function acts as continuous analogue of NAND gates, providing a compositional building block capable of representing elementary functions. In this work, we study the expressive power of tree-structured compositions of EML functions. We show that such trees enjoy a universal approximation property for functions in $W^{k, \infty}$ for $k \in \mathbb N$, drawing on classical neural network approximation arguments while exploiting the ability to explicitly construct EML trees that mimic polynomial representations. We further propose a learning algorithm for EML-type trees equipped with fitting parameters, and demonstrate its feasibility in practical optimization problems. Our results establish EML trees as a theoretically grounded framework for function approximation.

---


### 557. [StreamPPG: Low-Latency rPPG Estimation via Consistent Privileged Learning](https://arxiv.org/abs/2606.23186)

**<font color=#1a73e8>作者：</font>** Yiming Li, Yihan Yang, Yuguang Chu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote photoplethysmography (rPPG) estimates the blood volume pulse (BVP) signal from facial videos, enabling contact-free health monitoring. Conventional clip-wise approaches, which use video clips as input, require capturing over one hundred frames before inference, thus introducing several seconds of delay and hindering real-time use. Meanwhile, frame-wise approaches struggle to capture long-range temporal and periodic features of physiological rhythms, and therefore lead to reduced estimation accuracy. To overcome these issues, we propose StreamPPG, a unified architecture that enables low-latency frame-wise physiological signal estimation while achieving competitive accuracy compared with clip-wise approaches. StreamPPG is trained under a consistent privileged learning (CPL) strategy, which leverages ground-truth rPPG signals as privileged information to enhance the model's representation capability. Extensive experiments demonstrate that StreamPPG achieves state-of-the-art accuracy across multiple datasets while maintaining real-time throughput on edge devices.

---


### 558. [Stage-dependent integer-binary encoding in factorization-machine black-box optimization](https://arxiv.org/abs/2606.23188)

**<font color=#1a73e8>作者：</font>** Ryo Ogawa, Mayumi Nakano, Yuya Seki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Black-box optimization (BBO) deals with problems where objective functions lack explicit analytical forms and are expensive to evaluate. Factorization machine with quadratic-optimization annealing (FMQA) constructs a surrogate model using a factorization machine (FM) and optimizes it with an Ising machine. Conventional FMQA applies a single integer-binary encoding throughout the optimization process, although the encoding best suited to surrogate learning may differ from the one best suited to Ising-machine solution search. We propose a stage-dependent FMQA framework and derive conversion formulas between one-hot and domain-wall QUBO matrices that preserve the surrogate objective over feasible integer states up to an additive constant. We evaluate the OhDw variant, which employs one-hot encoding for learning and domain-wall encoding for search, on the Rastrigin function with input dimensions N = 2 and 5 and discretization levels q = 61 and 301. Across all conditions, the dominant factor governing optimization performance is the encoding used in the learning stage, with one-hot encoding consistently yielding lower residual errors than domain-wall or binary encoding. The additional benefit of switching to domain-wall encoding for solution search is condition-dependent. For N = 5 and q = 301, OhDw achieves a lower residual error and solutions closer to the global optimum than one-hot-only FMQA, whereas for N = 5 and q = 61 the latter achieves a lower residual error. These results indicate that one-hot encoding in the learning stage is the primary performance driver and that stage-dependent encoding can provide further improvement under finer discretization.

---


### 559. [Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity?](https://arxiv.org/abs/2606.23189)

**<font color=#1a73e8>作者：</font>** Anmol Goel, Iryna Gurevych  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) now act on a user's behalf across personal applications such as email, calendars, and to-do lists. This cross-application access is useful, but it also creates a privacy risk that has been largely overlooked: when an agent works in one context, it can pull in information from another that is inappropriate in that context. Hence, we introduce AgentCIBench, an evaluation harness that turns this risk into executable, deterministically scored scenarios. We target three common failure modes in CUAs: visual co-location, where the agent pulls in prohibited items that sit next to the task target in the UI; task-ambiguity overshare, where the agent dumps dense personal state in response to an under-specified prompt; and recipient misalignment, where the agent sends content to an addressee for whom it is inappropriate. We evaluate 15 frontier agents and find a surprisingly high failure rate: 11 of 15 leak on more than 50% of scenarios, with an average leakage of 67.9%, and the same failures persist when agents act end-to-end in the environment to complete the task. We release AgentCIBench to encourage the development of safer computer-use agents and position contextual disclosure testing as a pre-deployment safety check.

---


### 560. [Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory](https://arxiv.org/abs/2606.23195)

**<font color=#1a73e8>作者：</font>** Zewen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents increasingly rely on memory systems to maintain long-term coherence. Recent work shows that agent memories degrade during continuous consolidation. However, existing research assumes memories are derived from unbiased experiences. In this work, we identify and formalize a novel phenomenon: Memory Contagion -- the cross-temporal propagation of evaluator bias through agent memory. We show that when agents are trained or guided by biased evaluators, their experiences become biased; when these trajectories are stored and consolidated into memory, the bias propagates to future agents retrieving from the same memory store, even when consolidation is perfect (oracle). Across two bias types (length preference, authority bias) and four experimental phases, we demonstrate: (1) Memory Contagion occurs even with perfect consolidation (oracle condition), proving that biased input is a sufficient cause of contagion; (2) Consolidation has opposite effects depending on bias type -- robustly attenuating length bias while preliminarily amplifying authority bias (single-run estimate), suggesting a bias-type-dependent interaction; (3) No observed safe threshold: bias propagation is detected at contamination rates as low as p=0.2. Our findings expose a critical vulnerability in current agent memory designs and provide formal tools for measuring cross-temporal bias propagation.

---


### 561. [When Does Intrinsic Self-Correction Help? A Task-Sensitive Analysis](https://arxiv.org/abs/2606.23196)

**<font color=#1a73e8>作者：</font>** Elroy Stav, Dvir Berlowitz, Maayan Orner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Intrinsic self-correction (SC) aims to improve large language model outputs by prompting a model to revisit its own initial answer without external feedback. Recent studies have questioned the reliability of this approach, showing that models often struggle to judge whether their initial responses are correct. In this work, we take a task-sensitive view of SC. Rather than asking whether it works in general, we examine settings where SC may operate through different mechanisms: verifying explicit constraints, revisiting a complex reasoning process, or providing a second opinion over competing strategies in word-game tasks. Across multiple benchmarks and models, we find that SC can yield consistent performance gains when the underlying task structure facilitates these modes of revision. These results suggest that SC is best understood as a task-dependent inference-time strategy whose usefulness depends on the role the revision stage can play in a given task, rather than as a uniformly reliable method for improving initial model outputs.

---


### 562. [Bridge the Gaps: Heterogeneous Attributed Graph Clustering via Quaternion Representation Learning](https://arxiv.org/abs/2606.23199)

**<font color=#1a73e8>作者：</font>** Xinxi Chen, Junyang Chen, Yiqun Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attributed graph clustering partitions nodes by jointly exploiting node attributes and graph topology. It remains challenging due to attribute heterogeneity and representation degradation during graph learning. Real-world datasets often contain heterogeneous attributes, i.e., numerical and categorical attributes, complicating unified representation learning. This challenge becomes more complex in attributed graphs, where constructing a clustering-friendly graph structure from attributes and topology remains difficult. Under deep graph architectures, repeated graph propagation causes node embeddings to become overly similar, leading to the over-smoothing (OS) effect. Meanwhile, graph representation learning amplifies topological influence, making discriminative attribute information harder to exploit for clustering, an effect we refer to as over-dominating (OD). To bridge these gaps, an end-to-end framework, Any-type attributed Graph REpresentation lEarning (AGREE), is proposed. It unifies attributed graphs and any-type attributed data through multi-level alignment and similarity-based graph construction. Quaternion-based graph convolution strengthens attribute interaction to alleviate OD, while shallow graph architectures help relieve OS. The learned embeddings are jointly optimized for graph reconstruction and clustering, without requiring a predefined number of clusters during training. Experiments on diverse benchmarks show that AGREE achieves strong overall performance in accuracy, robustness, and adaptability.

---


### 563. [Unmasking LAION-5B: Age, Gender, Race, and Emotion Biases in Large-Scale Image Datasets](https://arxiv.org/abs/2606.23204)

**<font color=#1a73e8>作者：</font>** Iris Dominguez-Catena, Daniel Paternain, Mikel Galar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale image-text datasets, such as LAION-5B, are foundational to modern AI systems, yet their vast scale and uncurated nature raise significant concerns about demographic and stereotypical biases. This study presents a comprehensive analysis of the demographic composition and representational, stereotypical, and intersectional biases in LAION-2B-en and LAION-2B-multi, the two main components of the LAION-5B dataset. Using state-of-the-art models -- FairFace, DeepFace, and Emo-AffectNet -- we analyze faces detected in the dataset to identify biases across age, gender, race, and expressed emotion. Our findings reveal substantial overrepresentation of young adults (20--39), White individuals, and males, alongside consistent underrepresentation of minority racial groups and middle-aged or older women across both dataset components. We also observe stereotypical associations between demographic attributes and emotions, such as ``Anger'' being predominantly linked to males and ``Happiness'' to females, pointing to systemic imbalances in the data. The consistency of these patterns across two demographic models and both components of LAION-5B demonstrates that these biases are deeply embedded in one of the most widely-used training datasets. Given the scale at which LAION-5B is used to train generative models, these demographic imbalances could shape the behavior and outputs of numerous downstream AI systems.

---


### 564. [Efficient Network Inference via Hardware-Aware Architecture Search, Model Pruning & Quantization](https://arxiv.org/abs/2606.23210)

**<font color=#1a73e8>作者：</font>** Lucas Heublein, Mark Deutel, Axel Plinge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Embedded global navigation satellite system (GNSS) interference monitoring requires fast and memory-efficient inference to process large volumes of raw in-phase and quadrature (IQ) samples in real time. At the same time, increasingly expressive deep neural networks (DNNs) are needed for robust interference classification and characterization across diverse signal conditions. This creates a fundamental tension between predictive performance and deployability on resource-constrained hardware. In this paper, we investigate efficient network inference for GNSS interference characterization using iterative structured pruning, post-training static quantization, and hardware-aware zero-shot neural architecture search (NAS). Starting from MCUNet as a compact baseline, we analyze how model compression and automated architecture optimization affect model size, computational complexity, and memory usage while maintaining task performance. Experiments on a GNSS interference dataset, covering both classification and generalized characterization, show the benefits of combining compression and hardware-aware design for embedded deployment. Our results provide practical guidance for developing compact machine learning (ML) models for real-time GNSS interference monitoring on embedded platforms (iMXRT1062 MCU, Raspberry Pi Zero 2W, and Raspberry Pi 5).

---


### 565. [Temporally Aware Densification for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.23212)

**<font color=#1a73e8>作者：</font>** Vikram Sandu, Mayurdeep Pathak, Rajiv Soundararajan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite modeling temporal motion, dynamic 3D Gaussian Splatting (3DGS) methods still inherit a static densification strategy that is ill-suited for dynamic scenes. This neglect of temporal behavior leads to under-reconstructed and blurry dynamic regions, as short-lived Gaussians receive sparse supervision and fail to densify effectively. We propose a Visibility-Aware Densification (VAD) framework that integrates temporal visibility into the densification process, ensuring that Gaussians are refined based on their actual temporal presence. A Temporally-Adaptive Thresholding (TAT) mechanism further adjusts each Gaussian's densification threshold according to its temporal lifespan, promoting balanced refinement of both static and dynamic regions. Finally, a Temporal Offset Warping (TOW) design enhances deformation capacity around temporal centers, extending the lifespan of highly dynamic Gaussians and facilitating more effective densification. Our approach achieves substantial improvements in the visual quality of dynamic regions, outperforming existing methods across three dynamic multi-view benchmark datasets. Moreover, the proposed VAD module generalizes across diverse dynamic 3DGS methods, consistently improving dynamic reconstruction as a plug-and-play component.

---


### 566. [Deep learning-based detection of cessation of breathing in pre-term infants](https://arxiv.org/abs/2606.23213)

**<font color=#1a73e8>作者：</font>** Dineo Serame, Lionel Tarassenko, Mauricio Villarroel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Apnoea of prematurity is characterised by recurrent episodes of cessation of breathing and remains difficult to detect reliably using routinely monitored physiological signals in the Neonatal Intensive Care Unit (NICU). Existing bedside monitors rely primarily on respiratory rate and oxygen saturation thresholds, often generating high false-positive alarm rates and missing short or irregular events. Improving automated detection using routinely acquired clinical signals could enhance identification of clinically meaningful events without additional sensing hardware.
We evaluated deep learning-based detection of apnoea-related Cessation Of BrEathing (COBE) events using impedance pneumography (IP), electrocardiography (ECG), and photoplethysmography (PPG) signals from approximately 430 hours of NICU recordings collected from 24 pre-term infants. Three independent reviewers annotated COBE events, producing a dataset of 346 COBE and 608 non-COBE events. We compared a shallow convolutional neural network (CNN), residual networks (ResNets), and a ConvNeXt architecture using an independent held-out test set.
Across all architectures, detection performance was influenced more strongly by signal modality than by architectural complexity. Unimodal IP-based models achieved balanced accuracies of 86.8-88.0%, outperforming ECG-derived (62.6-69.7%) and PPG-derived (65.1-66.4%) respiratory surrogates. Multimodal fusion yielded modest improvements over IP alone. The best-performing model, a ConvNeXt architecture combining IP and PPG inputs, achieved 88.7% balanced accuracy and an F1 score of 0.75 on the independent test set.
These findings demonstrate that deep learning models applied to routinely monitored NICU signals can reliably detect COBE events and highlight the importance of signal modality in data-constrained neonatal monitoring settings.

---


### 567. [SPADE: Structure-Prior Adaptive Decision Estimation](https://arxiv.org/abs/2606.23219)

**<font color=#1a73e8>作者：</font>** Yifan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physical-structure priors such as conservation laws, Hamiltonian forms, and symmetries can improve scientific machine learning when correct, but can degrade predictions when misspecified. Existing methods usually enforce a chosen structure or tune a soft penalty, without a calibrated rule for deciding whether to impose a prior, how strongly to impose it, which prior to use, or which subset of candidate laws holds. We introduce SPADE, Structure-Prior Adaptive Decision Estimation, a closed-form framework that treats this problem as shrinkage of the structure-violating block of an unconstrained estimator. SPADE uses one exact specification test and one estimand: the test decides whether the prior is supported by data, Stein-unbiased James-Stein shrinkage sets the enforcement strength with an $O(\sigma^2/n)$ oracle guarantee, and a gate commits to the hard prior only when the test certifies it. The same test yields consistent nested structure selection and Benjamini-Hochberg control for subset discovery in non-nested constraint families. Across a linear-subspace prior, a reservoir conservation law, and a nonlinear Hamiltonian prior on Duffing dynamics, SPADE tracks the oracle, beats a neural-network baseline, reduces correct-prior regret from $10.3\%$ to $2.6\%$, matches cross-validation with $1/71$ of the solves, selects the correct structure with $100\%$ accuracy, and recovers partial laws with controlled false relaxation.

---


### 568. [PhysFlow: Frequency Decoupled with Dual-Field Rectified Flow for Remote Photoplethysmography](https://arxiv.org/abs/2606.23226)

**<font color=#1a73e8>作者：</font>** Zixu Li, jianjun Qian, Hang Shao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote Photoplethysmography (rPPG) enables contactless pulse estimation from facial videos, serving as a vital tool for health monitoring. However, current deep learning methods often struggle under complex disturbances, particularly varying illumination, facial expressions, and unconstrained head movements. In such scenarios, subtle physiological signals are easily dominated by external interference, making the recovered rPPG waveform unstable and unreliable. One important reason is that most existing methods directly model the rPPG signal in a unified manner, where different signal components are coupled during reconstruction. This makes it difficult to preserve weak pulse-related variations when strong disturbance-induced changes are present. To address this challenge, we propose PhysFlow, a frequency-decoupled dual-field rectified flow framework tailored for robust rPPG estimation. Specifically, the ground-truth rPPG signal is decomposed into trend and amplitude components, which are used as separate supervisory targets. Based on the extracted facial features, PhysFlow learns two component-specific conditional velocity fields to model the two components separately. This design reduces mutual interference between different components and improves the robustness of rPPG reconstruction under complex disturbances. Moreover, the rectified flow formulation enables efficient waveform reconstruction with only a few ordinary differential equation (ODE) integration steps. Extensive experiments on multiple benchmark datasets demonstrate that PhysFlow outperforms state-of-the-art methods in both heart-rate estimation and rPPG waveform reconstruction across diverse challenging scenarios.

---


### 569. [Privacy-Preserving Person Re-Identification from Temporal Sequences with Transformer and Hungarian Optimization](https://arxiv.org/abs/2606.23230)

**<font color=#1a73e8>作者：</font>** Raphaël Delécluse, Hazem Wannous, Laurent Guimas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Person re-identification (Re-ID) is a crucial task in surveillance and human behavior analysis, often used in public spaces such as transport hubs. Traditional RGB-based Re-ID methods raise privacy concerns and are highly sensitive to lighting variations and occlusion. In this paper, we propose a novel Re-ID approach that leverages depth images, which inherently obscures facial and other identifiable features, making it a privacy-preserving solution. Our method addresses the association problem between multiple views of individuals by applying the Hungarian algorithm, optimizing the matching process through minimization of the global cost across the distance matrix. We further enhance the approach by introducing temporal sequences of frames as input to a Transformer encoder architecture, which exploits both RGB and depth modalities. This architecture captures dynamic movement patterns, improving feature extraction and re-identification accuracy. Additionally, we employ batch hard triplet loss to enhance discriminative feature learning by focusing on the hardest samples. We evaluate both depth-only and RGB-D models on several top-view datasets, including TVPR2, GODPR, and BIWI RGBD-ID. Our results demonstrate that depth-only re-identification can achieve competitive performance compared to state-of-the-art methods, as measured by standard metrics such as Cumulative Matching Characteristics (CMC) and Mean Average Precision (mAP), while prioritizing privacy preservation.

---


### 570. [Judgment-Grounded Expansion for Peer Review Generation](https://arxiv.org/abs/2606.23233)

**<font color=#1a73e8>作者：</font>** Sheng Lu, Lizhen Qu, Iryna Gurevych  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic review generation is a promising direction for accelerating scientific progress. While most work adopts an end-to-end setup, its fully automated nature makes it less suitable for settings that demand accountability. To better balance automation and accountability, we formalize judgment-grounded expansion, a human-AI collaboration mode where a reviewer provides an evaluative claim and the system expands it into review comment candidate(s). We model it as a structured generate-check-refine process and conduct a user study to collect human-model interaction data. We study two practical challenges for judgment-grounded expansion: scalable evaluation and candidate set curation. We develop methods to simulate the process for large-scale evaluation, and show that conformal prediction is well suited to balancing candidate set size and target coverage. Our work establishes judgment-grounded expansion as a concrete task and provides empirical and methodological foundations for the design of future collaborative review generation systems.

---


### 571. [A Hybrid Intrusion Detection System for Electric Vehicle Charging Infrastructure](https://arxiv.org/abs/2606.23236)

**<font color=#1a73e8>作者：</font>** Charukeshi Joglekar, Chijioke Eze, Danni Xiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The integration of Electric Vehicle Charging Stations (EVCSs) into the smart grid necessitates sophisticated digital infrastructure for their management and coordination, which expands the attack surface and makes both the power grid and EVCSs vulnerable to cyberattacks. This research addresses critical gaps in existing EVCS Intrusion Detection Systems (IDS) by proposing a hybrid IDS that integrates attack detection on both the cyber and physical layer of the EVCS ecosystem. The proposed hybrid IDS utilizes a dual-layer integration method, which combines network-based IDS (NIDS) and host-based IDS (HIDS). This approach facilitates for comprehensive monitoring of both network traffic through the NIDS and host-level activities via the HIDS, effectively addressing the unique challenges posed by the interconnected nature of EVCS ecosystems. Utilizing the recent CICEVSE2024 dataset, the IDS presented in this work performs multiclass classification across various attack types, including False Data Injection Attacks (FDIAs), reconnaissance, denial of service, backdoor, and cryptojacking attacks. Experimental results demonstrate that our approach achieves excellent detection accuracy, with the NIDS component reaching 99.99\% accuracy for network-based attacks and the HIDS component achieving 83.47\% accuracy on FDIA, cryptojacking, backdoor, all DoS, all Recon except Slowloris Scan attacks. This dual-layer detection significantly outperforms single-source detection approaches previously presented in literature.

---


### 572. [Students' Perception Accuracy of Partners' AI Use and its Relation to Collaboration Performance](https://arxiv.org/abs/2606.23237)

**<font color=#1a73e8>作者：</font>** Laura Graf, Ramona Beinstingel, Stephan Kusche 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Collaborative assignments are a cornerstone of programming education. Effective collaboration during a programming project depends on the formation of reasonably accurate beliefs about how each partner works. Generative AI tools, now widely used by undergraduate students, have introduced a consequential and largely invisible new dimension into collaboration: each student's use of AI. When partners collaborate remotely, they interpret partners' ability and effort through their code. This raises the question of how accurately students perceive each other's AI use in collaborations, and if a misalignment in these perceptions relates to team performance. To address this question, we conducted a three-wave longitudinal study of 103 student pairs in an introductory software engineering course. We found that greater misalignment between partners' beliefs about each other's AI use early in the project was associated with lower final project scores. The effect of such misaligned perceptions is the strongest in teams with lower prior programming performance, suggesting that low performing students pay a higher cost of misaligned perceptions. The perception misalignment does not consistently decrease through face-to-face pair-programming sessions. This suggests that ways to foster transparency may be needed to support student teams in collaborative programming.

---


### 573. [When Suspicion Becomes Detection. Folk Deception Cues and Detection Strategies in Online Dating Romance Scams](https://arxiv.org/abs/2606.23241)

**<font color=#1a73e8>作者：</font>** Sima Amirkhani, Jana Krüger, Dave Randall 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The growth of mobile dating platforms has coincided with a rise in romance scams, in which offenders construct convincing personas to defraud users. While research on romance scams is expanding, victims lived experiences of recognizing and responding to deception in mobile-mediated interactions remain insufficiently understood. To address this gap, we conducted indepth interviews with 24 victims of online dating romance scams in Iran, where legal, social, and cultural constraints limit formal support. Our analysis identifies suspicion cues and the investigative strategies victims use to verify identities across platforms. We show that victims are not passive recipients of deception but engage in active, iterative detection practices under significant emotional, social, and relational pressure. Based on these findings, we contribute empirically grounded insights into deception cues and user driven detection work, and we discuss implications for the design of mobile technologies that better support users in identifying, resisting, and recovering from romance scams. Content Warning, This paper discusses sexual violence

---


### 574. [SteerVTE: Seamless Video Text Editing with Style and Glyph Control](https://arxiv.org/abs/2606.23254)

**<font color=#1a73e8>作者：</font>** Kai Zeng, Moran Li, Zhengwei Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual text editing aims to precisely modify text in images and videos while preserving stylistic consistency and visual realism. Despite significant advances in the image domain, video text editing remains largely unexplored: it is a localized task demanding stroke-level precision within small text regions, which compounds the challenges of cross-frame accuracy, temporal coherence, and stylistic fidelity. We introduce SteerVTE, a unified framework that \underline{\textbf{steer}}s a frozen video diffusion model to perform precise \underline{\textbf{V}}ideo \underline{\textbf{T}}ext \underline{\textbf{E}}diting through style and glyph control. Built on a frozen diffusion transformer, SteerVTE attaches a lightweight text context adapter with two complementary modules: a style encoder capturing the original text's visual attributes, and dual-granularity glyph encoders encoding the target text at both the line and character levels. To overcome the inherently weak text rendering priors of video foundation models, we further propose a glyph-aware spatial-focal loss and a three-stage progressive training curriculum that scales from image to video data. To support large-scale training, we also develop an automatic synthesis pipeline and construct SteerVTE-1M, a dataset of one million triplets spanning diverse scenes, fonts, and stylistic effects. Extensive experiments demonstrate that SteerVTE substantially outperforms existing video editing baselines across text accuracy, style consistency, and temporal coherence.

---


### 575. [P-JEPA: Procedural Video Representation Learning via Joint Embedding Predictive Architecture](https://arxiv.org/abs/2606.23256)

**<font color=#1a73e8>作者：</font>** Felix Tristram, Stefano Gasperini, Benjamin Killeen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The increasing maturity of embodied AI platforms has driven a growing interest in procedural video representation learning to support intelligent assistance systems for complex, multi-step tasks. Leveraging large-scale latent predictive training, video foundation models capture video dynamics, enabling downstream tasks such as activity understanding, spatiotemporal localization, and predictive control. However, procedural videos include actions with long-range dependencies that these models do not support, due to the quadratic complexity of self-attention. Distinct actions, for example, may be visually similar despite appearing at different points in the procedure, such as turning the stove on versus off. Here, we propose a backbone-agnostic approach that learns long-duration video representations by reducing the problem to a dense, frame-aligned action space and predicting pooled masked latent vectors. This approach allows our Procedural Joint Embedding Predictive Architecture (P-JEPA) to ingest videos over 30 minutes long, enabling effective long-form understanding of procedural steps. We evaluate P-JEPA using features extracted with VJEPA2.1, TSM, and I3D over the EgoExo4D, EgoProceL, and Assembly101 datasets, finding that it consistently improves linear separability, streaming inference, and temporal action segmentation performance, achieving state-of-the-art results on EgoExo4D fine-grained action classification while using an order of magnitude fewer parameters than LLM-based methods and running in real time.

---


### 576. [Ranking Companion: A Visual Analytics Approach to Item-Based Ranking with Hybrid Item Selection](https://arxiv.org/abs/2606.23263)

**<font color=#1a73e8>作者：</font>** Aman Kumar, Maximilian Tornow, Michaela Benk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Personalizing item ranking creation is a challenging task, especially when users lack knowledge of data attributes or the ability to express and formalize their attribute preferences. Item-based ranking creation is an approach allowing users to directly externalize preferences through known-item judgments rather than attribute-based scoring. However, a core challenge of item-based ranking is identifying and selecting representative candidate items for externalizing preferences. Existing approaches rely on singular item-selection methods, limiting flexibility and user control. To address this challenge, we present Ranking Companion, a visual analytics approach for item-based ranking that combines model-driven active learning with human-driven item-selection methods. By drawing from six complementary item-selection methods, users can externalize listwise preferences based on selected candidate items, while an iterative machine learning process with a ranking model calculates ranking results, presented to users alongside explanations for interpretation. We evaluated Ranking Companion in a formative user study with 10 participants, in which participants used each item-selection method across three iterations, revealing tradeoffs in perceived ranking quality across accuracy, diversity, novelty, transparency, control, and satisfaction. Ranking Companion contributes a unified interactive item selection space and provides preliminary empirical guidance toward the hybrid use of multiple complementary item-selection methods in personalized item-based ranking creation.

---


### 577. [Safe Few-Step Generation via Velocity Editing](https://arxiv.org/abs/2606.23267)

**<font color=#1a73e8>作者：</font>** Yujin Choi, Jaehong Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching has recently emerged as a strong paradigm for state-of-the-art text-to-image (T2I) generation, enabling high-quality generation with a small number of sampling steps. As these models are increasingly integrated into real-world applications, ensuring safe and non-sensitive content generation has become a critical requirement. However, adapting safety and concept removal methods to this new generation framework remains an open challenge. Specifically, prior methods largely rely on iterative trajectory steering across a number of denoising steps or on CLIP-centric prompt embedding manipulation. These design assumptions pose fundamental bottlenecks for safety in flow matching-based T2I generation, where limited sampling steps constrain iterative correction and modern context-aware text encoders diminish the effectiveness of embedding-level interventions. In this paper, we propose VESFlow, a training-free safety method tailored to flow matching with extremely few sampling steps. Leveraging the fact that flow matching models learn the marginal velocity, we directly edit the velocity field via a safe-conditional posterior. VESFlow steers the trajectory toward safe outputs while leaving the conditioning prompt unchanged. Building on the observation that VESFlow leaves outputs unchanged under benign prompts, we further introduce a risk score-based filtering that bypasses velocity editing to reduce computational cost while preserving benign prompt generation. Based on this filtering, we propose VESFlow+, a stronger variant of VESFlow that not only edits the velocity toward the safe direction, but also pushes it away from the unsafe direction. Experimental results show that VESFlow+ removes the target concept, reducing the attack success rate by NudeNet to 6.3% on Ring-A-Bell and 6.8% on MMA-Diffusion on the 4-step MeanFlow model, while preserving fidelity on benign prompts.

---


### 578. [Transfer learning-based method for automated ewaste recycling in smart cities](https://arxiv.org/abs/2606.23286)

**<font color=#1a73e8>作者：</font>** Nermeen Abou Baker, Paul Szabo-Müller, Uwe Handmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sorting a huge stream of waste accurately within a short period can be done with the support of digitalization, particularly Artificial Intelligence, instead of traditional methods. The overlap of Artificial Intelligence and Circular Economy can flourish many services in the environmental technology domain, in particular smart ewaste recycling, resulting in enabling circular smart cities. We analyse the growing need for automated ewaste recycling as an essential requirement to cope with the fast growing ewaste stream and we shed the light on the impact of Artificial Intelligence in supporting the recycling process through smart classification of devices, where the smartphone is our case study. Our study applies transfer learning as a special technique of Artificial Intelligence by finetuning the output layers of AlexNet as a pretrained model and perform the implementation on a small size dataset that contains 12 classes from 6 smartphone brands. We evaluate the performance of our model by tuning the learning rate, choosing the best optimizer, and augmenting the original dataset to avoid overfitting. We found that the optimizer of Stochastic Gradient Descent with Momentum and 3e-4 as a learning rate brings almost 98% model accuracy with generalization. Our study supports automated ewaste recycling in decreasing the error rate of ewaste sorting and investigates the advantages of applying transfer learning as the best scenario to overcome the rising challenges.

---


### 579. [Towards a Bathroom-Centered Human-Building Digital Twin Framework for Indoor Safety Analysis](https://arxiv.org/abs/2606.23292)

**<font color=#1a73e8>作者：</font>** Yuanzhi Su, Huiying  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Bathroom use is a critical safety challenge for older adults because wet surfaces, constrained layouts, limited support, and frequent posture transitions are concentrated within a small domestic space. These conditions create risks that cannot be adequately understood by considering either the bathroom environment or human motion in isolation. Existing bathroom safety studies mainly identify hazards, accessibility problems, or design modifications, whereas human-centered sensing studies often focus on activity recognition or fall detection without sufficient semantic understanding of the surrounding environment. This separation limits the interpretation of how older adults interact with fixtures, support surfaces, wet areas, and spatial constraints during daily bathroom activities. To address this gap, this study proposes a bathroom-centered human-building digital twin framework for interaction-aware indoor safety analysis with a specific emphasis on older adult bathroom safety. The framework conceptualizes bathroom risk as a coupled human-environment process and integrates semantic bathroom representation, skeleton-based human representation, spatial-semantic coupling, interaction-aware event analytics, and safety-oriented visualization. A Unity-based proof-of-concept prototype is developed to demonstrate the feasibility of the framework. Although the current work remains a prototype-oriented investigation, it establishes a methodological basis for analyzing older adults' bathroom safety through explicit body-environment relations and for advancing privacy-sensitive, interaction-aware digital twin applications in aging-in-place residential environments.

---


### 580. [Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation](https://arxiv.org/abs/2606.23293)

**<font color=#1a73e8>作者：</font>** Mingyu Mei, Li Zhang, Zibo Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 6D pose estimation is a key task in computer vision and embodied AI, widely used in robotic manipulation, augmented reality, etc. Existing methods directly regress in a high-dimensional continuous space, facing two key challenges in category-level pose estimation: limited accuracy due to noise and local optima, and inefficient search over an infinite space that hinders real-time performance. This paper proposes Flow6D, a hierarchical flow matching framework with a two-stage discrete latent space localization-continuous pose regression strategy. Rotation and translation parameters are first discretized into bins, with a discrete flow matching model locking the latent space around the true pose to reduce search complexity. Then, by sampling in the latent space, a continuous flow matching model predicts local pose residuals to optimize the estimate and regress to an accurate pose. The framework also naturally extends to articulated objects, outperforming state-of-the-art methods on synthetic and real datasets with real-time inference at 70 FPS. Project website: this https URL.

---


### 581. [Non-asymptotic estimates of the minimal risk in statistical learning](https://arxiv.org/abs/2606.23295)

**<font color=#1a73e8>作者：</font>** Liming Wu, Sen Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper we prove some concentration inequalities for two types of error probabilities in the Empirical Risk Principle (ERP) in statistical learning, which provide a lower bound and an upper bound for the minimal risk (in terms of the minimal empirical risk) with non-asymptotic high confidence. The usual boundedness condition of the empirical risk function is relaxed to the Gaussian or exponential integrability condition. The confidence of the lower bound of the minimal risk is shown to be independent of the number of training parameters and the dimension of the input vectors, allowing one to detect the deficiency of a learning machine efficiently; and the confidence of the upper bound of the minimal risk is proved to be high provided that the sample size $n$ is much greater than the box dimension of the parameter set $\Theta$ in the Orlicz metric $d_{\psi_1}$ associated with the risk functions. Our work is based on Talagrand's concentration inequalities (the sharp versions by Bousquet and Klein-Rio), transport-entropy inequalities and the recent progress in the theory of empirical processes and statistical learning.

---


### 582. [Ocean4D: Generative Underwater 4D Reconstruction via Medium-Aware Video Diffusion](https://arxiv.org/abs/2606.23298)

**<font color=#1a73e8>作者：</font>** Yuqiang Huang, Yuxi Wang, Junyu Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater 4D reconstruction remains challenging due to the coupling between degraded light transport in participating media and dynamic water variations. Most existing Methods are developed under in-air assumptions and do not explicitly account for underwater absorption and backscatter. Additionally, near-static assumptions make these approaches sensitive to drifting particles and dynamic distractors , leading to unstable geometry and inconsistent cross-view results. To address these issues, we propose a generative framework for underwater 4D reconstruction, named Ocean4D, which is built on two complementary components. Specifically, 4D-GCC constructs 4D geometrically consistent conditioning with improved cross-frame coverage, while the Medium-Aware Block performs implicit medium-aware denoising in the latent diffusion process to stabilize underwater appearance under absorption and scattering. Given a monocular video and target cameras, our method generates videos along the target trajectories while preserving global structure and cross-view consistency. Extensive experiments on both dynamic and static underwater benchmarks demonstrate state-of-the-art performance on underwater reconstruction.

---


### 583. [EHR-Complex: Benchmarking Medical Agents for Complex Clinical Reasoning](https://arxiv.org/abs/2606.23301)

**<font color=#1a73e8>作者：</font>** Yitong Qiao, Lei Liu, Yue Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical agents promise to democratize access to electronic health records (EHRs), yet existing benchmarks fail to reflect the complexity of practical EHR analysis, e.g., often operating on idealized, clean EHRs via static SQL generation rather than interactive execution. In this work, we introduce EHR-Complex, a large-scale benchmark designed for interactive clinical database reasoning. Built on the large MIMIC-IV substrate (365K patients, 31 tables, 500M+ records), EHR-Complex comprises about 52K tasks spanning six clinical intents, supporting both patient-level and population-level queries, where each task requires an agent to interact with a sandboxed environment by executing SQL queries or Python code. Notably, EHR-Complex considers the real-world SQL task complexity for longitudinal multi-table aggregation and compositional reasoning, resulting in 31.93 SQL structural components per query on average. Evaluation results on EHR-Complex reveal the clinical difficulty of these EHR reasoning scenarios, with the top-performing model achieving only 62.3% exact-match accuracy. Pass^k consistency drops below 50% for nearly all evaluated models at k=4, exposing broad stochastic fragility. A fine-grained analysis of more than 3,800 failed trajectories for representative LLMs reveals three dominant failure modes: SQL logic errors, medical-code lookup failures, and semantic misunderstandings. EHR-Complex provides a rigorous testbed for clinical agents and highlights remaining gaps in robust reasoning for large-scale EHR analysis.

---


### 584. [The Anatomy of the CTC Oracle Gap: Acoustic Exhaustion and Linguistic Recovery](https://arxiv.org/abs/2606.23306)

**<font color=#1a73e8>作者：</font>** Ivan Novosad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study the limits of CTC-internal scoring for N-best hypothesis selection and locate the information bottleneck separating acoustic confidence from linguistic plausibility. Eleven CTC-internal and acoustic-feature scoring strategies produce no statistically significant WER improvement over greedy decoding on LibriSpeech dev-other at G=16 (all p > 0.05). The exhaustion is systematic: CTC's Spearman $\rho$ between hypothesis score and per-utterance WER degrades from -0.574 at G=4 to -0.270 at G=128, a 53% loss driven by blank-path proliferation. This establishes that the discriminative capacity of CTC-internal representations is saturated: no recombination of acoustic signals can close the oracle gap.
Confirming that the bottleneck is linguistic, not acoustic, external linguistic information introduced via MBR decoding breaks through it. MBR-CER decoding with a RoBERTa pseudo-log-likelihood (PLL) posterior ($\tau$=10, G=128) achieves 5.42% WER on held-out LibriSpeech test-other (greedy 5.96%, $\Delta$=-0.535 pp, p<0.0001, 9.0% relative). RoBERTa PLL $\rho$ degrades only 21% over the same range, retaining discriminating power where CTC loses it. Applied without retuning across two Zipformer architectures, three domains (LibriSpeech, TED-LIUM 3, VoxPopuli), and four MUSAN noise levels, the recipe gives significant gains in 11 of 13 conditions.
On the training side, standard MWER training via the CTC forward-backward algorithm implements Rao-Blackwellized REINFORCE at the output projection (variance about 3x below Viterbi). Yet sequence-level fine-tuning fails at near-converged checkpoints: all four MWER configurations on CR-CTC collapse (+6.18 to +8.90 pp WER), as a training oracle gap of 0.007 pp provides no usable reward signal.

---


### 585. [Tmax: A simple recipe for terminal agents](https://arxiv.org/abs/2606.23321)

**<font color=#1a73e8>作者：</font>** Hamish Ivison, Junjie Oscar Yin, Rulin Shao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Terminal-using agents have quickly become the most popular downstream application of language models (LMs). Despite their prevalence, relatively little academic work has examined RL-based training of these models, likely due to difficult benchmarks, a lack of data, and a lack of simple baseline recipes. We present Tmax, the strongest open RL recipe for terminal agents to date, bringing open data recipes closer to the frontier. While simple, our recipe achieves 27\% on Terminal-Bench 2.0 with only 9B parameters, outperforming much larger models from prior work. Concretely, we generate data using a novel taxonomy, combining difficulty control, personas, and verifier diversification, which allows us to cheaply generate large amounts of terminal environments for RL and SFT training. We open-source our terminal dataset, which is over 2.5x larger than previously released terminal-agent datasets. We then train open-weight models using RL with our data, using a simple, outcome-only recipe. We release our data, models, and code as a strong baseline for future open academic work on terminal agents at this https URL.

---


### 586. [VideoAgent: All-in-One Framework for Video Understanding and Editing](https://arxiv.org/abs/2606.23327)

**<font color=#1a73e8>作者：</font>** Hengji Zhou, Lingxuan Huang, Jian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video editing has become essential in digital media creation, yet existing automated systems are restricted to short segment processing and domain-specific tasks. They face two critical limitations: i) inability to handle diverse video comprehension and editing operations, and ii) lack of long-video understanding for coherent narrative creation. We propose VideoAgent, an all-in-one agentic framework addressing these challenges through two key innovations. First, we develop automated video shot creation with shot planning agents for coherent narratives and cross-modal retrieval for aligned visual content. Second, we design a multi-agent orchestration framework integrating over thirty specialized editing agents. Intent parsing filters relevant tools while textual-gradient graph optimization assembles complex editing pipelines. Extensive experiments on our newly-proposed VideoEdit benchmark and public datasets demonstrate VideoAgent's superiority over existing multimodal LLMs and agentic systems. VideoAgent achieves 87-95% orchestration success rates while reducing API costs by 60%. Human evaluation across six video categories shows VideoAgent produces professional-quality content approaching human-level performance, with ratings only 4% below human-created videos. We release our code at this https URL.

---


### 587. [RT-DocLayout: Real-Time End-to-End Document Layout Analysis with Reading Order in the Wild](https://arxiv.org/abs/2606.23344)

**<font color=#1a73e8>作者：</font>** Cheng Cui, Tingquan Gao, Xueqing Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate document layout analysis remains a critical bottleneck for document parsing systems, due to the intricate coupling among heterogeneous document layout elements, geometric distortions (\eg, paper warping and bending, perspective variations), and reading order within diverse layout structures. Existing approaches typically rely on fragmented multi-stage pipelines or computationally heavy generative Transformer architectures, leading to error propagation and limited efficiency.
In this paper, we present RT-DocLayout, a highly efficient end-to-end framework for document layout analysis, designed as a front-end for document parsing tasks. The proposed model unifies classification, detection, pixel-level segmentation, and reading order prediction for layout elements within a single 33M-parameter architecture. Built upon the RT-DETR, our key contribution is a unified multi-task formulation within a single query-based decoder that simultaneously classifies, regresses bounding box, generates masks, and constructs relationship to reason reading order.
By jointly learning geometric and structural representations, RT-DocLayout introduces multi-task optimization that substantially improves robustness under real-world document distortions. Extensive experiments on public benchmarks demonstrate state-of-the-art performance in document layout analysis while maintaining real-time inference speed(132.1 FPS). When coupled with downstream OCR engines, RT-DocLayout significantly improves full-document reconstruction quality, providing a scalable and practical foundation for real-world document intelligence systems.

---


### 588. [Superhuman AI for Generals.io Using Self-Play Reinforcement Learning](https://arxiv.org/abs/2606.23348)

**<font color=#1a73e8>作者：</font>** Matej Straka, Viliam Lisý, Martin Schmid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a superhuman AI agent for this http URL, a real-time strategy game that requires both long-horizon planning and short-term tactics under strong imperfect information. Trained for four days on 4x NVIDIA H200 GPUs, our agent reaches #1 on the public 1v1 leaderboard of over 5,000 human players, leading the second-ranked player by the same margin that separates second place from 25th, and beats the two top-ranked humans head-to-head with a combined 199-70 record across 269 ladder matches. A key enabler is a JAX-native simulator that reaches tens of millions of frames per second on a single GPU, roughly a 10,000x speedup over the prior simulator. On top of this, we train a vision transformer policy end-to-end by self-play with a policy-gradient loop and sparse win/loss reward, using top-advantage sample filtering and an exponential moving average of the policy parameters. Taken together, our findings highlight what matters, and what does not, once a fast simulator removes the data bottleneck.

---


### 589. [Changing Modalities: Adapting Remote Sensing Models to New Satellites and Sensors](https://arxiv.org/abs/2606.23356)

**<font color=#1a73e8>作者：</font>** Tim G. Zhou, Anthony Fuller, Geoff Pleiss 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine learning models for remote sensing are trained and deployed on a static set of modalities. However, as we equip newer satellites with novel sensors and retire old ones, practitioners may wish to deploy an existing model on a substitution, superset, or subset of modalities with minimal retraining given data availability or practical computational constraints. We study the setting of updating existing models to changing modalities and identify three main scenarios: Modality Transfer (substitution), Addition (superset), and Peeking (subset). We propose DeluluNet, an architecture with modular components for all three changing modality scenarios. DeluluNet is trained end-to-end, learning a multi-modal model from a unimodal teacher and unlabeled multimodal data via modality hallucination--predicting missing modality representations from those that are present. As a result, DeluluNet can keep predicting even when input modalities change, providing a practical alternative to re-labeling and re-training in a changing world.

---


### 590. [SOAP-Bubbles: Structured Weight Uncertainty for Neural Networks](https://arxiv.org/abs/2606.23357)

**<font color=#1a73e8>作者：</font>** Adrian Robert Minut, Nico Daheim, Marco Miani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured weight-uncertainty can improve many aspects of deep learning, but it remains costly to estimate and difficult to implement. Here, we show that these issues can be addressed by adapting the SOAP optimizer. Our key idea is to run IVON, an existing diagonal-covariance variational method, in the eigenspace of SOAP's preconditioner and then use the preconditioner to transform the diagonal estimate into a non-diagonal covariance. The resulting method has costs similar to those of SOAP and requires no drastic changes to training pipelines. We call the posteriors obtained in this way SOAP-Bubbles and our new optimizer Eigenspace-VON (EVON). We show that, for logistic regression, EVON recovers the exact Gaussian covariance and that, for language model pretraining, it yields significantly better results than existing diagonal-covariance methods. Our work makes it easier to estimate more expressive posterior distributions for deep learning at scale.

---


### 591. [Adaptive Hard-Soft Physics-Informed Neural Networks for Robust Boundary-Constrained PDE Solving](https://arxiv.org/abs/2606.23359)

**<font color=#1a73e8>作者：</font>** Duc Tien Nguyen, Trinh Minh Tuan, Nguyen Duc Manh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) provide an effective way to solve partial differential equations (PDEs) by embedding physical principles into the learning process. However, the conventional PINN formulation, in which all constraints are imposed as soft penalty terms within a composite loss, often exhibits slow convergence, sensitivity to loss weight scaling, and inaccurate boundary enforcement due to poor conditioning of the optimization landscape. To address these limitations, this study proposes a unified hard--soft physics--informed neural network (HSPINN) with adaptive loss weighting. In this framework, Dirichlet and periodic boundary conditions are enforced exactly by construction through analytical or polynomial lifting, masking functions, and periodic feature mappings, while the governing PDE residuals, Neumann fluxes, and initial conditions are treated as soft constraints. An inverse-share softmax strategy dynamically balances the relative importance of individual loss components during training, eliminating manual penalty tuning and improving gradient stability. This formulation ensures boundary admissibility throughout optimization and enhances convergence efficiency and numerical robustness. Applications to representative elliptic (Poisson), parabolic (Burgers), and hyperbolic (convection with periodic boundaries) problems demonstrate that HSPINN consistently achieves faster convergence, higher accuracy, and greater stability than conventional PINNs, establishing a general and scalable foundation for physics-constrained deep learning across science and technology.

---


### 592. [Rethinking Molecular Graph Backdoors under Chemistry-aware Admission](https://arxiv.org/abs/2606.23361)

**<font color=#1a73e8>作者：</font>** Thinh T. H. Nguyen, Sze Jue Yang, Khoa D. Doan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks on molecular graph neural networks (GNNs) are typically evaluated as abstract graph edits, but real molecular learning pipelines do not train on arbitrary graphs. Molecular records must first survive parsing, sanitization, canonicalization, and graph-string consistency checks. We formalize this overlooked admission stage as ChemGuard, an operational protocol for testing whether a submitted molecular record can enter a realistic learning pipeline, while complementing existing defenses. ChemGuard admits a record only when its molecular string is sanitizable and the graph reconstructed from that string matches the submitted molecular graph. Under this operational view, many existing graph-based backdoors lose much of their apparent efficacy because their poisons are chemically invalid or representation-inconsistent. We then show that admission checks alone are insufficient to rule out molecular backdoors. We propose ChemBack, an admission-aware molecular backdoor attack that constructs chemically feasible motif-anchor attachments and ranks admitted candidates by fingerprint-based Tanimoto similarity to clean target-class molecules. ChemBack is model-free during trigger selection, using molecular structures, target labels, fingerprints, and public validity checks, but no victim model, surrogate GNN, learned embedding, gradient, logit, or training-code access. Across molecular benchmarks, validators, architectures, and defenses, \textbf{ChemBack} achieves high attack success with fully admitted poisons while preserving clean accuracy. Our results reveal a two-sided lesson, chemistry-aware admission suppresses many graph-only backdoors, yet chemically valid and target-aligned molecular backdoors remain a practical threat.

---


### 593. [TooBad: Backdoor Diffusion Models with Ultra-Low Poison Rate and Imperceptible Trigger](https://arxiv.org/abs/2606.23362)

**<font color=#1a73e8>作者：</font>** Vu Tuan Truong, Long Bao Le  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Diffusion models (DMs), despite their impressive capabilities across a wide range of generative tasks, have been shown to be vulnerable to backdoor attacks. However, existing backdoor methods face critical trade-offs among key factors: attack performance, stealthiness, time complexity, and required poison rates. For example, achieving high attack performance typically demands a high poison rate and prolonged training, which undermines stealthiness, making the attack more detectable by backdoor defenses. This paper proposes TooBad (trigger optimization for backdoor diffusion models), a backdoor framework which introduces a novel DM-tailored trigger optimization technique to dramatically enhance the performance of backdoor attacks on DMs. Experiments on representative benchmarks such as CIFAR-10 show that TooBad can achieve high ASRs ($> 85$%) at only 0.5% poison rate, significantly lower than the 10% typically required by prior work on the same datasets. At 5% poison rate, TooBad reaches nearly 100% ASR within just 3-5 backdoor injection epochs, whereas existing methods need at least 30-50 epochs at double the poison rate for comparable results. Despite its potency, TooBad easily evades SOTA defenses and maintains high utility. These results reveal a critical threat on DMs and highlight the need for more robust defenses against such stealthy yet efficient attacks.

---


### 594. [Convergence of Gradient Descent for General Neural Network Architectures Beyond the NTK Regime](https://arxiv.org/abs/2606.23364)

**<font color=#1a73e8>作者：</font>** Yuqing Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training dynamics is central to understanding neural networks, yet its theoretical analysis remains difficult even for simple architectures and becomes substantially more challenging for general modern architectures. In this paper, we propose a convergence framework for analyzing gradient descent (GD) dynamics under a broad family of neural network architectures and datasets beyond the neural tangent kernel (NTK) regime. The framework is formulated at the level of network blocks and covers architectures including pre-normalized multi-layer transformers. More precisely, under mild assumptions, we prove that for almost all initializations, GD with regular learning rates converges to the neighbourhood of a stationary point. This is mainly proved by establishing an iterate-dependent PL-type inequality through analyticity and measure-zero arguments, and by proving Lipschitz smoothness along the GD trajectory through polynomial generalized smoothness and a local relaxed dissipative condition. We further interpret the theorem under Xavier initialization and practical architectural scaling, showing that the learning rate scale depends on the depth and effective bottleneck dimensions rather than the largest width. Finally, we derive structural nondegeneracy implications for residual connections and function composition, and provide a generic characterization of global minimizers within our framework.

---


### 595. [Polynomial Dice Loss for Medical Image Segmentation](https://arxiv.org/abs/2606.23373)

**<font color=#1a73e8>作者：</font>** Hiroaki Aizawa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation is a fundamental task for medical image processing and computer-assisted intervention, yet data imbalance and small lesion detection pose significant challenges. Dice Loss, which measures the overlap between predicted and ground truth regions, is widely used to mitigate these issues. To further emphasize its properties, we propose Polynomial Dice Loss, a polynomial extension of Dice Loss. Specifically, by leveraging the geometric characteristics of Dice Loss and formulating the loss function as a polynomial representation via Taylor expansion, we enable the adjustment of the contribution of higher-order components to the loss function. In our experiments, we evaluate the proposed method against loss functions derived from conventional Dice and Tversky coefficients. Experimental results and further analysis show that the polynomial formulation provides a simple way to control the loss shape and achieves competitive performance across multiple segmentation settings.

---


### 596. [Energy-Based Transformers as Predictors of Reading Difficulty](https://arxiv.org/abs/2606.23382)

**<font color=#1a73e8>作者：</font>** Jakub Dotlacil, Ece Takmaz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer language models have become established tools for modeling human sentence processing, with measures such as surprisal and attention entropy serving as effective predictors of reading difficulty that together capture complementary aspects of processing load. Here, we explore a related class of transformer models: energy-based transformers, which provide a principled formal link to associative memory models, bringing processing research into direct contact with the broader literature on Hopfield networks and dense associative memory. To our knowledge, this is the first exploration of an energy-based transformer measure in computational psycholinguistics. Across reading-time corpora (Natural Stories, UCL eye-tracking, UCL self-paced reading), the energy measure is a robust predictor of reading times, providing significant fit beyond surprisal in all three. In a controlled experiment on relative clause processing, energy at a single layer captures the well-known object/subject asymmetry. We find evidence that it subsumes effects attributable to both attention entropy and surprisal, suggesting that energy may serve as a single unified predictor where multiple complementary measures have previously been required.

---


### 597. [Physics-Informed Modeling for Wood Thermal Analysis and Prediction](https://arxiv.org/abs/2606.23402)

**<font color=#1a73e8>作者：</font>** Jingren Xie, Alex John Buckthal, Ryan Anthony O'Connor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wood materials exhibit complex, spatially varying thermal properties that challenge traditional architectural assumptions of material homogeneity. Although data-driven approaches can directly map wood RGB images to their corresponding thermal responses, they operate as uninterpretable black boxes that prioritize statistical correlation and may absorb experimental noise rather than thermodynamic plausibility. To address these limitations, we present physics-informed deep learning frameworks that integrate partial differential equations (PDEs) to predict pixel-level thermal responses of spatially heterogeneous wood materials using wood RGB images and testbed temperature maps. Specifically, we investigate two distinct approaches to enforcing a normalized 2D steady-state heat transfer equation derived from the general heat transfer equation: Physics-Informed Convolutional Neural Networks (PICNNs), which embed physics as a soft penalty term in the loss function, and Physics-Integrated Convolutional Neural Networks (PInteCNNs), which hard-code an analytical approximator-predictor-corrector solver directly into convolutional neural networks. To validate our proposed approaches, we collect three real-world multimodal datasets of Poplar, Grandis Cross-Cut (Grandis-CC), and Grandis Radial-Cut (Grandis-RC) wood samples. We further demonstrate that embedding physical inductive biases successfully balances predictive accuracy, physical interpretability, and intra-species diversity, outperforming data-driven approaches in handling complex wood material heterogeneity and enabling the extraction of interpretable physical parameters. Project: this https URL

---


### 598. [Litmus: Zero-Label, Code-Driven Metric Specification for Evaluating AI Systems](https://arxiv.org/abs/2606.23403)

**<font color=#1a73e8>作者：</font>** Prajjwal Gupta, Prasang Gupta, Vishal Bhutani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agentic LLM systems move from prototypes to deployment across increasingly diverse domains, evaluating them has become both more important and more difficult. The challenge is not only that individual metrics may be unreliable, but that evaluation goals are often left implicit. Without a clear account of what a system is expected to do, how it can fail, and which failures matter, metric choices become difficult to justify, interpret, or validate. We present Litmus, a zero-label system that designs evaluation and monitoring metrics for AI pipelines by eliciting evaluation intent from source code and targeted interrogation. Instead of assuming that the evaluation target is already known, Litmus first identifies what must be measured and why, then converts those answers into constraints for constructing a justified, per-stage metric portfolio. We evaluate Litmus on three real, code-defined AI pipelines - financial account grouping, scientific QA, and inherent risk assessment - against AutoMetrics and three DynamicRubric baselines. Litmus achieves the broadest or tied-broadest concern coverage, spans more pipeline stages, produces a near-zero-redundancy portfolio, and ranks first in validity against per-row quality labels on all three pipelines - decisively on scientific QA (Spearman $\rho=0.72$ vs. less than $0.47$ for every baseline), and within overlapping confidence intervals in relation to two components of the audit framework despite using no labels during metric design. Our results support a shift from automatic metric implementation to automatic metric specification: before asking which metric to compute, evaluation systems should ask what must be measured and why.

---


### 599. [OptChain: Achieving Optimal Throughput of Permissionless Blockchains](https://arxiv.org/abs/2606.23405)

**<font color=#1a73e8>作者：</font>** Chunjiang Che, Songze Li, Xuechao Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce \textit{OptChain}, a permissionless blockchain state machine replication (SMR) protocol that achieves optimal throughput. We first establish a theoretical upper bound on the throughput of any SMR protocol under a fixed error probability, and OptChain is the first protocol to approach this limit. Conceptually, OptChain is a sharding protocol that optimizes both vertical and horizontal scalability. Vertically, we introduce \textit{Shardis}, a novel permissionless verifiable information dispersal mechanism that maximizes intra-shard throughput to its physical limit, determined by the fastest node's bandwidth within each shard. Horizontally, we propose \textit{diffusion mining}, which ensures security as long as each shard includes at least one honest node, thereby allowing for the maximum number of shards. We provide a formal security and efficiency analysis, demonstrating that OptChain approaches the established upper bound while maintaining robust security. Finally, we implement a full prototype of OptChain and deploy it on AWS EC2 nodes across various regions. Experimental results indicate that OptChain outperforms state-of-the-art permissionless protocols and closely approaches the theoretical optimal throughput.

---


### 600. [HyperQuant: A Rate-Distortion-Optimal Quantization Pipeline for Large Language and Diffusion Models](https://arxiv.org/abs/2606.23406)

**<font color=#1a73e8>作者：</font>** Yuval Domb, Hadar Sackstein, Tomer Solberg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present HyperQuant (Hadamard, optimallY Packing, Entropy Rice-coding), a unified post-training quantization pipeline for the weights and the KV cache of large language and diffusion transformers. Across a suite of self-contained experiments (Table 1), HyperQuant outperforms the recent HIGGS scheme at every operating point from 3 to 5 bits per scalar (bps) on weights, and beats both TurboQuant and OCTOPUS on KV quantization down to 1.7 bps. Beyond the LLM setting, HyperQuant quantizes the 19B-parameter LTX-2 DiT video model with no observable per-frame artifacts. End-to-end on an H100 at 4 bps, HyperQuant compresses the linear weights ~3.9x and the KV cache ~3.79x at near-lossless quality.
HyperQuant combines four known ideas into a single construction: (i) a per-tile Randomized Hadamard Transform that makes the per-coordinate distribution of weights and activations approximately Gaussian; (ii) quantization to a low-dimensional optimal lattice (E8, D4, A2, or Z); (iii) lossless bit-stripping and near-entropy-optimal variable-length Rice coding of the lattice indices; and (iv) bias-correction methods for the KV cache that keep the reconstruction unbiased under inner products, preserving attention semantics. We further integrate the pipeline with 8-bit and 4-bit Tensor-Core MMA paths (fp8-e4m3, int8, nvfp4, mxfp4), and find that int8 beats fp8 on the post-RHT lattice output. Project page: this https URL

---


> [!TIP]
> 当前位于：**551-600**（第 12/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
