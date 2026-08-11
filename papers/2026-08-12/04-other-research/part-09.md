# 📦 其他研究 | 2026年08月12日

> 本类共 **445** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-445**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-445**

---

### 401. [ResemBrick: Brick Reconstruction from Photographs with Perceptual Fidelity and Buildability](https://arxiv.org/abs/2608.09597)

**<font color=#1a73e8>作者：</font>** Xilun Chen, Hanwen Wan, Yusong Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Producing a hand-buildable, colored brick model of a 3D object from a few casual photographs is a clean testbed for a broader challenge: generating 3D content that meets hard physical-assembly constraints under a discrete, budget-limited voxel grid. On a coarse lattice, visual resemblance and structural stability pull against each other, yet prior brick pipelines address only one side and treat voxelization as fixed preprocessing rather than a variable to optimize. We present ResemBrick, which couples the two. Budgeted occupancy completion reframes discretization as allocation: given a target occupied-voxel count, a single resolution-conditioned network decides in one feed-forward pass which surface voxels to fill for best appearance, one weight set spanning 13 resolutions. Buildability by construction then combines support- and look-ahead-aware greedy placement with a deterministic, provably terminating repair that grounds every floating component. Under a matched budget, ResemBrick surpasses existing voxel selectors in perceptual fidelity while uniquely reaching zero floating and zero unstable bricks on unfiltered held-out objects; as a complete pipeline, it attains the best perceptual fidelity among prior brick-construction systems. Our results point to treating discretization and assembly as tightly coupled stages rather than independent ones.

---


### 402. [Structure-Enhanced Features and Quality-Aware Dynamic Anchor Scoring for Robust Lane Detection](https://arxiv.org/abs/2608.09610)

**<font color=#1a73e8>作者：</font>** Weize Cai, Yongqi Dong, Zhida Shao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lane detection requires recovering thin, elongated, and frequently occluded lane structures under challenging driving conditions. While anchor-based detectors provide efficient candidate generation, their performance is limited by two coupled issues: backbone features often lose structural continuity along partially visible lanes, and classification confidence may decouple from line-level localization quality, allowing inaccurate anchors to persist before non-maximum suppression (NMS). We propose a structure-enhanced and quality-aware framework that improves lane representation and dynamic-anchor scoring while preserving the inference pipeline of the Anchor Decomposition Network (ADNet). Specifically, a Gated Horizontal-Vertical Token (GHVT) module enhances mid- and high-level backbone features via lightweight directional token interactions with a learnable residual gate. In parallel, Line-Quality-Aware Dynamic Anchor Scoring (LQAS) calibrates existing classification logits using quality supervision, hard-negative suppression, and pairwise ranking without adding inference branches. On the VIL-100 dataset, our method improves ADNet-R34 from 89.97 to 91.28 in F1 score at the 0.5 intersection-over-union threshold (F1@50), reducing both false positives and false negatives. Additional experiments on CULane and TuSimple datasets, extensive ablations, score-distribution diagnostics, and runtime analysis confirm complementary structural and ranking improvements with minimal computational overhead.

---


### 403. [Marrying Optimal Transport and ODEs for Unified Continuous-Time 4D Reconstruction and Tracking](https://arxiv.org/abs/2608.09613)

**<font color=#1a73e8>作者：</font>** Liying Yang, Hao Mo, Jialun Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing unified 4D reconstruction and point tracking approaches typically rely on heuristic interpolations or just predict at integer timestamps, lacking kinematic coherence and failing to model dynamics at any arbitrary timestamp. In this paper, we propose Uni4R, a framework that unifies these tasks by learning continuous velocity fields through the synergy of Optimal Transport (OT) and Ordinary Differential Equation (ODE). Importantly, this continuous velocity field acts as a kinematic prior that mutually benefits both 4D reconstruction and point tracking. Specifically, we propose the Flow Matching Guided Decoder (FMGD). A global velocity branch first extracts anchor features that capture the global dynamic state of the sequence. Then, FMGD leverages Flow Matching (FM) theory to formulate a probability path defined by OT on the anchor feature manifold, instantiating it as FM-guided velocity features for velocity prediction. This establishes a robust kinematic inductive bias. Meanwhile, a point reconstruction branch provides geometric features. The local velocity prediction module then joint above features and time embeddings, to decode velocities at arbitrary timestamps. To overcome the absence of high-quality ground-truth velocities in fractional frames, we propose an integral-consistency training strategy. This strategy uses an ODE solver to integrate velocities to recover target pointmaps, enabling the model to be supervised end-to-end directly from integer timestamps. Experimental results demonstrate that Uni4R achieves SOTA performance in both 4D reconstruction and point tracking, and achieves SOTA in our new kinematics-aware benchmark at continuous time.

---


### 404. [Bayesian Symbolic Regression with Entropic Reinforcement Learning](https://arxiv.org/abs/2608.09617)

**<font color=#1a73e8>作者：</font>** Oussama Boussif, Mohammed Mahfoud, Younesse Kaddar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression is the problem of finding an algebraic expression describing a stochastic dependence of a target variable on a set of inputs. Unlike forms of regression that fit parameters assuming a fixed model structure, symbolic regression is a search problem over the space of expressions, represented, for example, as abstract syntax trees using a library of operators. Symbolic regression is typically used in settings with limited, noisy data in the natural sciences. However, searching for a single best-fitting expression fails to capture the epistemic uncertainty about the expression, which motivates a Bayesian perspective that enables uncertainty quantification and specification of natural priors to constrain the search space. In this work, we propose ERRLESS (Entropy-Regularized Reinforcement Learning for Expression Structure Sampling), a scalable approach for sampling from the posterior distribution over expressions given data using maximum-entropy reinforcement learning. ERRLESS learns a neural policy that constructs expressions sequentially by building up their abstract syntax trees. At convergence, the policy samples expressions from the posterior. At test time, expressions can be sampled by rollouts of this policy. We demonstrate that ERRLESS achieves competitive results on the Feynman benchmark while producing short and interpretable expressions. Additionally, we demonstrate that the mean of the posterior predictive approximated by ERRLESS achieves a high coefficient of determination ($R^2$) compared to an SMC baseline, highlighting the benefits of the Bayesian perspective in symbolic regression.

---


### 405. [Adaptive Sequential Test Planning for Multi-Mechanism Reliability Qualification via Bayesian Monte Carlo Tree Search](https://arxiv.org/abs/2608.09622)

**<font color=#1a73e8>作者：</font>** Youssef A. Elhagrasy, Ian Hill, André Ivanov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliability qualification of advanced semiconductor devices requires sequential stress decisions that balance characterization objectives against multiple competing failure mechanisms. Current practice relies on static test plans derived from population-level acceleration models, which cannot adapt to per-unit variability or real-time degradation observations. This paper presents a closed-loop adaptive test planning framework that formulates reliability qualification as a partially observable sequential decision problem and solves it using Monte Carlo tree search for seed-action simulators (MCTS-SA) coupled with extended Kalman filter (EKF) belief-state estimation. The framework models stochastic, per-device variability in bias temperature instability (BTI), electromigration (EM), and time-dependent dielectric breakdown (TDDB), and treats stress selection as a constrained sequential optimization, i.e., to maximize the probability of successful degradation characterization while respecting catastrophic failure constraints. Under the experimental assumptions used here (discrete stress actions, proxy damage observability, and cumulative degradation without recovery), we believe this to be a novel application of tree-search-based adaptive test planning to multi-mechanism reliability qualification. Across 5,000 planning iterations, the characterization yield (CY) improves from 20% in the first 500 iterations to over 54% in the final 500, with 39% cumulative success, while the best successful test sequence terminates with EM and TDDB damage fractions DEM=0.564 and DTDDB=0.537, well within safety margins. These results demonstrate that sequential Bayesian planning can synthesize damage-aware test policies that significantly outperform non-adaptive strategies for reliability qualification under competing failure modes.

---


### 406. [Satellite Trajectory Optimization via Proximal Policy Optimization for Space Debris Avoidance](https://arxiv.org/abs/2608.09628)

**<font color=#1a73e8>作者：</font>** Logan Luna, Juan Ortiz Couder, Raul Alejandro Vargas-Acosta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collision avoidance systems are commonly used to avoid fragmentation events occurring in Low-Earth Orbit (LEO) and Geosynchronous Equatorial Orbit (GEO). However, these events have been growing in frequency as orbital congestion worsens with the launch of megaconstellations. Consequently, conjunction alerts and collision risks are becoming increasingly common. Current practices, which are commonly manual or rule-based, have difficulty scaling to these worsening dynamic environments. To address this intensifying situation, we propose a reinforcement-learning policy for autonomous collision avoidance, trained via Proximal Policy Optimization (PPO) along with an open-source, high-fidelity astrodynamics simulator for training and evaluation. In 1,000 deterministic GEO episodes, our agent achieves a 97.5% collision avoidance success rate, outperforming traditional controllers such as a rule-based baseline (20.7% success) and an impulsive delta-v planner baseline (27.5% success). To achieve these results, we designed a simulator to train and evaluate our agent, using real-world and simulated debris. We simulate Newtonian two-body dynamics using Sun/Moon third-body perturbations, fuel-dependent thrust, and configurable debris fields. The agent is trained with curriculum learning and shaped rewards oriented toward encouraging survival, adequate projected miss distance, and delta-v conservation. Finally, our evaluation consisted of a fully deterministic pipeline, including shared seeds, per-episode logs, and telemetry exports. Our work is a publicly available framework at this https URL

---


### 407. [NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation](https://arxiv.org/abs/2608.09636)

**<font color=#1a73e8>作者：</font>** Haiyang Yan, Jinyue Guo, Yanchao Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D neuron segmentation in fluorescence microscopy is critical for neuroscience. However, the sparse and elongated morphology of neurons poses significant challenges to existing segmentation methods. These methods struggle to preserve both local details and global topology, leading to fragmented results. To address this, we propose NeuroRefiner, a multi-agent system that formalizes the human expert workflow involving iterative global observation and local editing. Specifically, NeuroRefiner comprises three collaborative agents dedicated to diagnosing topological errors, generating correction instructions, and validating refinement quality. To facilitate agent instruction-guided segmentation refinement, we propose TopoRefineNet, a dedicated 3D U-Net-based tool that leverages cross-modality feature fusion to generate refined masks. Through multi-round agent reasoning and voxel-level editing, NeuroRefiner produces topologically more accurate segmentations with enhanced interpretability. Experiments on the BigNeuron, CWMBS, and ZBFWB datasets demonstrate that NeuroRefiner outperforms state-of-the-art methods, notably achieving a 3.02% improvement in F1 score on the challenging ZBFWB dataset.

---


### 408. [DUET: A Diversity-Quality Duet of Distillation Experts for Two-Step Video Generation](https://arxiv.org/abs/2608.09637)

**<font color=#1a73e8>作者：</font>** Zian Li, Litong Gong, Borui Liao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have enabled high-quality video generation in recent years, but the high cost of iterative sampling hinders their practical deployment. Few-step distillation alleviates this cost, yet exposes a quality--diversity trade-off between its two dominant paradigms: trajectory-level distillation (e.g., sCM) favors diversity, whereas distribution-level distillation (e.g., DMD) favors quality. Targeting extreme two-step video generation, we introduce DUET, which reconciles the two paradigms through a noise-level duet of experts: an sCM expert takes the high-noise step to lay out diverse structure, and a DMD expert takes the low-noise step to refine appearance detail. Since the two experts are trained independently with their native objectives, DUET sidesteps the optimization difficulties of loss-level combinations and delivers quality and diversity jointly rather than trading one for the other. We further identify the relay interface and the high-noise stage as the remaining bottlenecks, and address them with RL-guided expert adaptation, yielding DUET+. With the Wan2.1-T2V-1.3B backbone, DUET lifts the two-step quality of sCM close to the level of DMD while retaining nearly all of its structural diversity---about twice that of DMD---and DUET+ further improves overall quality while preserving this diversity advantage. Together, these results establish noise-level expert specialization as a simple, effective paradigm for reconciling diversity and quality in two-step video generation.

---


### 409. [EgoHieraLoc: A Cortically Inspired Hierarchical Segmentation-Guided Framework for Egocentric Visual Query Localization](https://arxiv.org/abs/2608.09656)

**<font color=#1a73e8>作者：</font>** Yifei Cao, Guolong Wang, Mingliang Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual query localization (VQL) aims to retrieve and re-localize a queried object in egocentric videos, yet remains challenging when object boundaries are ambiguous and global context cannot effectively guide fine-grained localization. Human vision handles such ambiguity through a hierarchical process: it rapidly screens foreground candidates, selectively attends to the target despite distractors, refines perception via feedback between global context and local detail, and, when a single view is unreliable, integrates evidence across viewpoints according to its credibility. Inspired by these competencies, we propose \textbf{EgoHieraLoc}, a unified framework for VQL-2D and VQL-3D. A Discriminative Parsing Module first extracts foreground-aware query representations using segmentation priors; a Query-Aware Module then performs robust target localization through discriminative correlation filtering with deformable modeling; and a Regional Adaptation Module feeds multi-scale context back into local regions to recover precise object boundaries. To extend this perceptual hierarchy to 3D localization, we introduce Geometric-Semantic Joint Confidence (GSJC), which multiplicatively couples segmentation confidence with local depth consistency, multi-view back-projection consistency, and triangulation-baseline quality, so that a viewpoint contributes to the 3D estimate only when it is credible both semantically and geometrically. Extensive experiments demonstrate state-of-the-art performance on both VQL-2D and -3D benchmarks.

---


### 410. [CIFA: Contextual-Intersectional Fairness Auditing for Hidden Subgroup Discovery in Face Analysis](https://arxiv.org/abs/2608.09669)

**<font color=#1a73e8>作者：</font>** Nazia Aslam, Khalid Adnan Alsayed, Thomas B. Moeslund 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fairness evaluation in computer vision commonly relies on aggregate accuracy and demographic subgroup analysis. However, visual models are also sensitive to contextual factors such as illumination, blur, image quality, facial accessories, and appearance attributes. These factors may interact with demographic characteristics, producing hidden subgroups in which performance degrades substantially despite strong aggregate accuracy and apparently acceptable demographic fairness. To address this, we propose the Contextual-Intersectional Fairness Auditing Framework (CIFA), a structured framework for identifying subgroup vulnerabilities arising from interactions between demographic and contextual attributes. CIFA performs demographic, contextual, and contextual-intersectional auditing, followed by worst-group discovery to identify and rank the most vulnerable attribute combinations. We evaluate CIFA on gender classification using ResNet-50 \cite{he2016deep} and ViT-B/16 \cite{dosovitskiy2020image} across FairFace \cite{Karkkainen2021}, CelebA \cite{Liu2015}, and UTKFace \cite{Zhang2017}. Our results show that aggregate accuracy and demographic-only evaluation can mask substantial contextual-intersectional disparities. We further assess several established mitigation strategies through an audit--mitigate--reaudit protocol and find that, although some worst-group disparities are reduced, no single strategy consistently eliminates them across datasets and architectures. These findings establish contextual-intersectional auditing as an important component of fairness evaluation and provide a reproducible framework for discovering, prioritizing, and reassessing hidden subgroup risks in face analysis systems.

---


### 411. [MPISuperRes-PnP: A Super-Resolution Zero-Shot Plug-and-Play Reconstruction Algorithm for Magnetic Particle Imaging](https://arxiv.org/abs/2608.09672)

**<font color=#1a73e8>作者：</font>** Vladyslav Gapyak, Thomas März, Andreas Weinmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic Particle Imaging (MPI) is an emerging medical imaging modality. MPI is based on the non-linear response of magnetic nanoparticles to an applied magnetic field and avoids ionizing radiation. The measured signal is the voltage induced in receive coils by the particles' response. Reconstructing the particle concentration from the signal constitutes the imaging task. Even using state-of-the-art measurement-based reconstruction, the associated spatial grid is very coarse, hence super-resolution (SR) techniques are important. In this work, we propose an approach for SR in MPI inspired by energy minimization. Different methods have been proposed for SR in MPI, ranging from upscaling of the associated system matrix to interpolation of the reconstruction. Here we incorporate SR into the reconstruction task via an energy minimization formulation. Following the plug-and-play approach to energy minimization we derive a splitting scheme and a SR method for MPI where the arising Gaussian denoising task is treated with a pre-trained learned Gaussian denoiser in a zero-shot fashion. This way, we incorporate benefits of deep learning without training and avoid the need of training data. Further, we provide a quantitative and qualitative evaluation of the proposed method. Hyper-parameter are selected via an extended parameter search. The found parameters are applied for reconstruction on real data. We show the applicability of our method on synthetic and on real data (MPIData: EquilibriumModelWithAnisotropy and 2D-OpenMPI Data). The proposed method employs a deep-learning denoiser without training -- thus it does not require presently scarcely available MPI training data. The denoiser behaves conservatively, i.e., no hallucination artifacts were observed. The SR approach is generic such that it can be applied in future MPI contexts involving different regularizers or different imaging tasks.

---


### 412. [Deep Learning Imputation of Missing Radius of Maximum Winds (Rmax) Values in Tropical Cyclone Best-Track Data](https://arxiv.org/abs/2608.09683)

**<font color=#1a73e8>作者：</font>** Swastik Agrawal, Nishkal Hundia, Ziyue Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic coastal hazard assessments require accurate characterization of tropical cyclone (TC) parameters, yet datasets often contain missing records for the radius of maximum winds (Rmax), a key variable in Joint Probability Method analyses. This study evaluates data-driven approaches for Rmax imputation, including one-dimensional Convolutional Neural Networks (1DCNNs), Long Short-Term Memory (LSTM) networks, and conventional machine learning models. We examine physics-informed input augmentation, temporal modeling, and transfer learning using synthetic RAFT and STORM datasets for pre-training and observational IBTrACS data for fine-tuning. Including the radius of 34-knot winds (R34) substantially improves performance across all model types. Temporal models achieve higher average correlations than non-temporal models despite using approximately an order of magnitude fewer samples, indicating better preservation of relative Rmax variability across storms. This advantage is more pronounced when R34 is unavailable, suggesting temporal information can partially compensate for missing storm-size predictors. Transfer learning does not improve performance, likely because synthetic datasets have lower and less variable Rmax distributions than IBTrACS. These findings demonstrate the potential of temporal deep learning for reconstructing incomplete TC records and highlight the importance of physics-informed inputs, observational data availability, and distributional consistency in coastal hazard assessment.

---


### 413. [Adaptive Semantic Capacity Allocation for Parallel Generative Recommendation](https://arxiv.org/abs/2608.09685)

**<font color=#1a73e8>作者：</font>** Chenxi Li, Yuchen Lu, Xu Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive semantic ID recommenders are constrained by expensive beam-search decoding, which limits the practical length of item identifiers. Parallel generation methods alleviate this bottleneck by predicting all semantic ID tokens simultaneously, enabling longer IDs. However, existing semantic ID methods still rely on manually predefined and homogeneous ID structures, where both the number of semantic slots and the codebook size of each slot are treated as fixed hyperparameters. This ignores the heterogeneous capacity demands of different semantic subspaces and may allocate prediction capacity to slots with limited utility. We show that uniformly expanding semantic slots can provide limited gains, indicating redundant capacity in homogeneous semantic IDs. We propose InforID, a lightweight adaptive semantic target construction framework for parallel generative recommendation. InforID allocates a fixed capacity budget across candidate semantic slots, thereby jointly determining the effective ID length and slot-specific codebook sizes. Experiments demonstrate improved recommendation accuracy under comparable capacity budgets while preserving one-step parallel prediction.

---


### 414. [FedOrbit: Adaptive Personalized Federated Learning for Non-IID LEO Satellite Constellations](https://arxiv.org/abs/2608.09687)

**<font color=#1a73e8>作者：</font>** Satwat Bashir, Tasos Dagiuklas, Muddesar Iqbal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) in Low Earth Orbit (LEO) satellite constellations is affected by non-IID data and irregular ground-station visibility, both driven by orbital geometry. Global aggregation performs poorly when orbit-level class distributions are disjoint, while strong personalisation can be excessive when these distributions overlap. We present FedOrbit, which combines continuous orbit-level training over inter-satellite links, class-aware hierarchical aggregation, quality-weighted feature aggregation with return-rate dampening, and adaptive feature decomposition based on inter-orbit class similarity. Across three remote-sensing benchmarks and two non-IID partitions, FedOrbit achieves the highest accuracy in five of six settings and is within $0.9$ percentage points of the best result in the sixth. The gains over the strongest baseline reach $16.1$ percentage points under Dirichlet partitioning and $8.6$ under pathological partitioning, with the smallest per-orbit accuracy spread in five of six settings.

---


### 415. [Confusion-Geometry Rebalancing for Long-Tailed Adversarial Training](https://arxiv.org/abs/2608.09688)

**<font color=#1a73e8>作者：</font>** Mengnan Zhao, Geyong Min, Lihe Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial training under long tailed distributions suffers from a dual imbalance: the class imbalance skews the training objective toward head classes, and the adversarial inner maximization may further amplify this bias. Existing methods mitigate this issue by correcting class priors or adapting class wise robust supervision, yet they treat each class in isolation and fail to identify which boundaries drive long tailed collapse. We propose a Confusion Geometry Rebalancing method (CGRm) for long tail adversarial training, a plug in framework that leverages directed robust errors as training signals. CGRm leverages periodic robust evaluations to derive source class loss weights, class wise robust coefficients, and a directed confusion geometry graph. The method then couples feedback weighted robust optimization with graph guided margin correction, thereby boosting the robustness of vulnerable classes and sharpening the critical boundaries that drive long tailed performance degradation. Experiments on long tailed benchmarks show that CGRm achieves consistent robust performance gains over existing methods, with ablations validating the contribution of each component. We provide the code in the supplement.

---


### 416. [Recurrent Neural Networks Beyond Time: Learning from Multiple Ordered Projections](https://arxiv.org/abs/2608.09690)

**<font color=#1a73e8>作者：</font>** Vagan Terziyan, Artur Terziian, Oleksandra Vitko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent neural networks (RNNs) are widely used for sequence learning, yet their application is commonly associated with temporal data, although recurrent computation fundamentally operates on ordered sequences rather than on time itself. Building on this observation, we introduce the Ordered Structural Dependency Hypothesis (OSDH), which proposes that multiple admissible orderings of the same observations may reveal complementary structural dependencies inaccessible through a single sequential organization. To operationalize this hypothesis, we propose the Independent Structural Expert Principle (ISEP), whereby projection-specific sequence models are trained independently before their learned representations are integrated through a dedicated fusion model. As a concrete realization, we present Structural Evolution RNNs (SE-RNNs), which employ conventional RNNs as projection-specific structural experts while preserving the underlying recurrent computation unchanged. Proof-of-concept experiments on three synthetic datasets with substantially different levels of structural complexity demonstrate that the proposed architecture consistently benefits from multiple ordered projections when hidden structural dependencies are present, while remaining competitive on simpler datasets. Since OSDH is independent of the underlying sequence-processing model, the proposed framework naturally extends beyond recurrent networks and may be instantiated using alternative architectures. The results suggest a general computational perspective for exploiting complementary ordered representations across diverse structured learning problems.

---


### 417. [Evaluating Generative Time-Series Models on Data with Point Masses](https://arxiv.org/abs/2608.09692)

**<font color=#1a73e8>作者：</font>** Jian Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many of the series that generative time-series models are benchmarked on place a large probability mass on a single value --- it does not rain, no ride is requested, no part is ordered. We report what happens when such data is evaluated carefully. First, the standard rolling-origin protocol can score a model on a window whose atom structure bears no resemblance to the dataset: on one benchmark the dataset is $42\%$ zeros and the evaluation windows are $13\%$, on another $47\%$ against $5\%$. This is not a cosmetic problem --- it reversed one of our own conclusions, turning the strongest occurrence model in our study into what looked like a cautionary tale. Second, we give a control in which CRPS is invariant \emph{by construction} while the temporal coupling is destroyed, which measures exactly how much that coupling contributes to a chosen statistic. Third, benchmarking seven models on a matched protocol over five seeds, an autoregressive hurdle beats a conditional flow on five of six datasets, by up to a factor of $153$, while the flow's own occurrence statistics vary by up to $62\%$ across training seeds and every baseline is deterministic. Finally, the model ordering is not the same under five different occurrence statistics, and the two that do not share a construction agree with each other least.

---


### 418. [Full-Key Recovery and Forgery from One MQOM v2.1 Signature](https://arxiv.org/abs/2608.09699)

**<font color=#1a73e8>作者：</font>** José Luis Delgado  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We give a full-key-recovery attack on MQOM v2.1, a Round-3 candidate in the NIST additional-signature process, that recovers the complete signing key from one accepted signature and uses it to sign a fresh message. If $\delta=\operatorname{FirstBits}_{\lambda}(x)$ is the prefix of the witness $x$, the sibling path determines a public value $A$ such that tree parity gives $s=\delta\oplus A$. Substitution into the hidden-leaf commitment yields $$\mathsf{Enc}_K(\delta\oplus A)=T\oplus\mathsf{LinOrtho}(\delta)$$ with public values $K$ and $T$. The correction in the same signature expands a solution into a complete witness, while the public MQ relation identifies those yielding valid signing keys; serializing such a witness gives the secret key, enabling a fresh-message signature accepted by the reference verifier.
We evaluate this equation over the specified AES/Rijndael circuits using retained circuit state along a Gray traversal. Complete-domain scans for Categories I and V cost $2^{142.335112}$ and $2^{271.794162}$ Boolean gates. Category-III scans cover $1/2+2^{-20}$ and $0.580004770183$ of the domain at costs of $2^{206.774558}$ and $2^{206.988685}$ gates. All four totals are below the NIST security benchmarks. Reduced-domain runs against the reference implementation recover the byte-exact witness and key in all three categories and produce a fresh-message forgery accepted by the reference verifier. Independently generated source-syntax circuits evaluate the fixed ciphers over the stated domains and translated L3 prefixes, while an exact ideal-cipher factorial-moment bound controls additional equation preimages passed to public-key validation. Every value in the equation is fixed by the accepted transcript, so salt-bound global-root expansion changes its public constants without removing the one-signature recovery channel.

---


### 419. [Designing PULSE: A Realtime Annotation Tool to Support Simulation Debriefing](https://arxiv.org/abs/2608.09715)

**<font color=#1a73e8>作者：</font>** Caleb Vatral, Jennifer Hunt, Mary Ann Jesse 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Debriefing is central to effective simulation-based education. However, effective debriefing is challenged by high instructor workloads and limited engagement of observing students. A real-time annotation tool to support debriefing, called PULSE, was co-designed with nursing educators. A field study comparing three standard simulation debriefings with three debriefings using PULSE was conducted as a preliminary evaluation. Outcomes were assessed using the Debriefing Assessment for Simulation in Healthcare (DASH) student survey and a follow-up instructor interview. PULSE significantly improved overall DASH scores (t(4) = 4.03, p = 0.027, Cohen's d = 2.05). Survey findings suggested improvements in debriefing organization and depth of reflection. Interview data indicated that the student-generated annotations enhanced engagement and stimulated more interactive discussions. PULSE shows promise as a support tool for debriefing, particularly by facilitating reflection of observing students. However, larger and more diverse studies are needed to confirm effectiveness and refine the system for broader implementation.

---


### 420. [Mirroring the Past: Exploring How Ancestral Digital Self Influences History Learning](https://arxiv.org/abs/2608.09719)

**<font color=#1a73e8>作者：</font>** Duo Gong, Fan Sun, Yucen Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Learners often perceive history as distant from themselves, which limits immersion and empathy in history learning. To bridge this gap, we introduce the "Ancestral Digital Self," an AI-generated pedagogical agent presented in prerecorded videos that mirrors the learner's facial features and vocal timbre, representing a historically situated version of the self. We developed a reproducible workflow for creating AI-generated historical learning videos and conducted a within-subjects study (N=36) comparing a Digital Self agent with a non-self pedagogical agent. The Digital Self agent enhanced experiential measures, including narrative transportation, perceived relatedness, self-other inclusion, and agent perception. However, it did not improve immediate learning outcomes: quiz scores were lower in the Digital Self condition, and Remember/Know judgments showed no reliable differences. Interviews further suggested that self-similarity increased familiarity and motivation, while novelty and uncanniness could draw attention away from historical content. These findings offer design implications for future educational environments supported by pedagogical agents.

---


### 421. [PET/CT Radiogenomic Mutation Prediction in Non-Small Cell Lung Cancer Using Multi-Label Learning](https://arxiv.org/abs/2608.09721)

**<font color=#1a73e8>作者：</font>** Mona Furukawa, Sai Hyne, Daniel R. McGowan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lung cancer remains one of the leading causes of cancer- related mortality worldwide. Although targeted therapies have improved outcomes for patients with non-small cell lung cancer (NSCLC), they rely on mutation profiling through tissue biopsy, an invasive procedure with several limitations. This study investigates PET/CT-based radio- genomic prediction of epidermal growth factor receptor (EGFR), tumour protein 53 (TP53), and Kirsten rat sarcoma viral oncogene (KRAS) mutations using deep learning. We further evaluate whether pairwise multi-label learning improves mutation prediction compared with conventional single-gene classification. To the best of our knowledge, this is among the first studies to systematically investigate multi-label learning for PET/CT radiogenomic mutation prediction in NSCLC. Experiments were conducted on a novel UK-based radiogenomics cohort. Joint pre- diction of KRAS and TP53 improved AUC from 0.58 to 0.64 for KRAS and from 0.69 to 0.71 for TP53. For the EGFR/KRAS pair, only EGFR benefited from joint learning, while no improvement was observed for the EGFR/TP53 pair. These findings demonstrate that the effectiveness of multi-label learning depends on the specific combination of gene mutations being modelled, suggesting that mutation-specific modelling strategies may be preferable for PET/CT radiogenomic prediction.

---


### 422. [HandSplatter: Automated Digital Goniometry from Neural Rendering](https://arxiv.org/abs/2608.09735)

**<font color=#1a73e8>作者：</font>** Emmett Chen, Neal Chen, Xiang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand and finger disorders are leading contributors to musculoskeletal disability, creating a clinical need for precise methods to quantify joint motion. Range of motion (ROM) serves as the metric for diagnosis, rehabilitation monitoring, and evaluating surgical outcomes. Currently, the goniometer is the standard tool for assessing finger flexion and extension. However, manual goniometry is labor-intensive and suffers from inconsistent inter-rater reliability due to variations in examiner technique. While digital alternatives exist, current software-based approaches often lack the necessary accuracy for clinical usage. To address these limitations, we present a novel pipeline for 3-D hand joint location and pose estimation using neural rendering. Unlike previous methods, our approach combines 2-D feature extraction with view synthesis to significantly improve accuracy and clinical viability. Furthermore, we introduce a discrete density hill climbing algorithm that facilitates the meaningful correction of projected landmarks in 3-D space. This system overcomes the inefficiencies of manual measurement and the inaccuracies of existing software, providing a robust tool for objective functional assessment.

---


### 423. [Second-Order Muon Done Right: A Principled Marriage of Spectral Geometry and Curvature](https://arxiv.org/abs/2608.09763)

**<font color=#1a73e8>作者：</font>** Tong Che  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Muon's polar update is exact for an unweighted spectral geometry. We introduce GO-MUON, which uses a matched data-dependent geometry and reuses it across several optimization steps. Conditioned on any positive-definite left and right maps, its raw update exactly solves the corresponding weighted spectral oracle; this statement is independent of how the maps are estimated or how recently they were refreshed. For softmax cross-entropy, we quantify when the observed-label backward factor approaches the model Fisher and generalized Gauss--Newton factor. We also show that four-step refresh nearly preserves the tracking delay of slowly changing geometry while increasing stationary factor noise, making lazy geometry a compute--statistics tradeoff rather than a denoising mechanism.

---


### 424. [MoNo: Multiscale Optimal Transport Neural Operator for Solving PDEs on General Geometries](https://arxiv.org/abs/2608.09764)

**<font color=#1a73e8>作者：</font>** Zijiang Yang, Xiaomeng Wu, Dongmei Fu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based neural operators have achieved substantial progress in solving Partial Differential Equations (PDEs) by projecting spatial observations into compact latent tokens and learning physical interactions in latent spaces. However, we reveal that existing learnable projection mechanisms cannot ensure stable and balanced assignments from observation points to latent tokens, causing some latent tokens to be over-assigned while others remain underutilized. This limitation further restricts the design of hierarchical architectures, as assignment imbalance is continuously inherited and amplified across latent spaces, eventually causing severe token collapse in deeper spaces. To address these issues, we propose MoNo (Multiscale Optimal Transport Neural Operator), a progressive multiscale neural operator that efficiently solves PDEs on general geometries through stable latent-space construction. At its core is CoTAP (Cross-scale Optimal Transport Assignment and Projection), a novel latent-space construction method that formulates cross-space assignment between adjacent spaces as an entropy-regularized optimal transport problem, thereby constructing balanced bidirectional projections and stable latent spaces. CoTAP also ensures stable information transfer across multiple latent spaces, further enabling multiscale architectures on general geometries, which in turn support more efficient learning of long-range physical interactions. Extensive experiments demonstrate that MoNo outperforms existing state-of-the-art neural operators in both prediction performance and computational efficiency. Code is available at this https URL.

---


### 425. [Cultivar: A Contrastive and Locale-Oriented Translation Benchmark for Investigating Contamination and Localisation Robustness](https://arxiv.org/abs/2608.09766)

**<font color=#1a73e8>作者：</font>** Pinzhen Chen, Koel Dutta Chowdhury, Xiaoya Xu 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual translation benchmarks are typically sourced in English and translated into other languages, treating language pairs as the unit of evaluation---a design that is prone to contamination over time and overlooks locale and cultural considerations. We therefore advocate for source-contrastive evaluation and instantiate it with Cultivar, a localised subset of FLORES, which enables locale-specific translation evaluation. When paired with unlocalised counterparts, performance discrepancy allows the probing of data contamination and localisation robustness. We benchmark 32 open-weight models and find that MT-specialised models are less robust, a few models potentially overfit FLORES, and models tend to translate US content better than that of other locales, regardless of language.

---


### 426. [Structured Phonological Representations for Audio-Articulatory rtMRI Speech Classification](https://arxiv.org/abs/2608.09767)

**<font color=#1a73e8>作者：</font>** Abner Hernandez, Tomás Arias Vergara, Daiqi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-time MRI makes it possible to observe vocal-tract articulation during speech, but mapping these articulatory patterns to phonetic and phonological categories remains challenging. We investigate whether PhonoQ, an audio-based model trained to recognize structured phonological features, provides useful information for audio--articulatory modeling. Specifically, we extract representations from PhonoQ's Conformer module, whose training is shaped by supervision for manner, place, voicing, and vowel features. Using articulatory contours with synchronized audio-derived features, we compare WavLM-large and HuBERT-large baselines with models that incorporate PhonoQ-derived representations. Across unseen-speech and unseen-subject settings, these features improve macro-F1 for phonological targets including manner, place, voicing, vowel height, and vowel backness, and also improve fine-grained 39-phoneme classification. In a contour-only inference setting, audio-derived teacher supervision yields modest but consistent gains over contour-only training, indicating that phonological information from synchronized audio can be partially transferred to articulatory models. Finally, posterior analyses show interpretable surface-sensitive patterns consistent with flapping-like /t/ realizations, /t/-/r/ retraction or affrication, and nasal place assimilation.

---


### 427. [ReliableNet: A Chance-Constrained Approach to Trustworthy Classification in Deep Learning](https://arxiv.org/abs/2608.09768)

**<font color=#1a73e8>作者：</font>** Ange-Clément Akazan, Ineza Remy Mugenga, Abebe Geletu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A prediction that is both confident and wrong is a critical reliability failure because it can bypass abstention and human review precisely when the model is mistaken. Empirical risk minimization (ERM) controls average loss but not this failure directly, while calibration, uncertainty estimation, conformal risk control, and selective prediction methods target related reliability properties rather than bounding the joint failure event during training. We propose ReliableNet, which constrains the Joint Confident-Wrong (JCW) probability, the probability that a prediction is simultaneously confident and incorrect, below a user-specified risk budget $\alpha\in(0,1)$. We formulate this as a chance-constrained ERM problem, use a conservative smooth inner approximation whose population feasibility implies the original JCW constraint. Across four tabular and two image datasets, ReliableNet is the only method certified within the JCW budget for every dataset and seed in distribution, when compared against baselines spanning ERM, post-hoc calibration, conformal risk control, and selective prediction. Under demographic, ambiguity, spurious-correlation, novel-class, and covariate shifts, it achieves the lowest empirical JCW among the compared methods while remaining very competitive in accuracy, coverage, calibration, and selective prediction. Risk-coverage results further indicate that ReliableNet achieves better selective ranking than the benchmark methods on most datasets. Overall, ReliableNet provides a principled approach to trustworthy classification.

---


### 428. [C$^2$A: Coupling Spatial Evidence with Clinical Priors via Co-occurrence Aware Class Attention for Multi-Label Chest X-Ray Classification](https://arxiv.org/abs/2608.09774)

**<font color=#1a73e8>作者：</font>** Akash Gogineni, Nagur Shareef Shaik, Aasrith Mandava 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thoracic pathologies rarely occur in isolation, yet standard multi-label classifiers rely on shared global descriptors, discarding \emph{where} findings lie and \emph{how} they co-occur. We propose \textbf{C$\mathbf{^2}$A} (Co-occurrence Aware Class Attention), a classification head that explicitly couples spatial evidence with clinical priors. First, C$^2$A casts pooling as an expectation over learned per-class spatial attention maps, yielding localized descriptors for each disease. Second, it couples these descriptors via a learnable graph warm-started from empirical label co-occurrence. A single residual message-passing step shares evidence among related findings, proving to be a bounded perturbation of the identity where co-occurrence enters each logit through an explicit bilinear interaction. On CheXpert, C$^2$A achieves a superior $0.895$ macro-mean AUROC, outperforming advanced context-gating baselines. Crucially, gains concentrate on highly co-occurrent classes with ambiguous spatial evidence (rescuing Atelectasis by $+1.5$ over GCG), demonstrating the prior's regularizing effect with a negligible overhead of one linear projection and a $C\!\times\!C$ edge matrix.

---


### 429. [AirFlow: Context Preserving and Multi-Rate State Modeling for Air Quality Forecasting](https://arxiv.org/abs/2608.09775)

**<font color=#1a73e8>作者：</font>** Fan Yang, Nan Chen, Yijie Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate air quality forecasting is essential for public health and urban environmental management, but remains challenging because pollutant channels differ in periodicity and distribution drift, while their concentration trajectories contain both multi-scale dependencies and rapid changes. Recent methods have improved spatial dependency learning and meteorological covariate modeling. However, pollutant channels are still passed through the same normalization rule and temporal backbone, using a shared latent representation for channel-specific distributions and changes at different rates. To address this limitation, we propose AirFlow, a pollutant-aware dual-stream framework that operates on station multivariate observations without additional graph propagation or predefined signal decomposition. Specifically, AirFlow designs two novel blocks: (1) a statistic-guided normalization routing mechanism that selects a normalization path for each pollutant according to its 24-hour autocorrelation and distribution drift; and (2) a hierarchical dual-stream state model that combines multi-scale state space propagation with learnable response coefficients, where gated bidirectional cross-attention exchanges information and adaptively fuses the resulting representations. Experiments on real-world data from multiple cities show that AirFlow achieves the best performance in 34 of 36 metrics comparisons, with reductions of up to 11.11% root mean square error over the state-of-the-art baseline. AirFlow also requires only 0.0483M parameters and 0.0215G FLOPs, achieving high forecasting accuracy with low computational overhead.

---


### 430. [NTIRE 2026 Low-light Enhancement: Twilight Cowboy Challenge](https://arxiv.org/abs/2608.09782)

**<font color=#1a73e8>作者：</font>** Aleksei Khalin, Egor Ershov, Artyom Panshin 等 49 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a review of the NTIRE 2026 Low-light Enhancement: Twilight Cowboy Challenge. The objective of the competition was to merge a set of misaligned smartphone images in the raw domain, captured in low-light conditions, into a single, clean image. Introduced setup simultaneously addresses two problems of low-light photography: visual degradations such as high noise and mixed scene illuminants, and the geometric inconsistencies caused by hand movement during multi-frame capture. To advance research in low-light and nighttime computational photography, a challenging dataset was collected comprising 585 real-world scenes, spanning indoor low-light and outdoor nighttime conditions, for training and benchmarking participant solutions. The competition employed a three-stage evaluation protocol: automatic validation via the CodaBench platform in stages one and two, followed by blind assessment on a private test set for the final ranking. Ten teams surpassed the established baseline, achieving improvements of up to +6.49 dB in PSNR and +0.0101 in SSIM, thereby establishing new state-of-the-art performance for burst-based low-light image enhancement. These results demonstrate significant progress in handling real-world noise, motion, and illumination variability in the low-light setting. Comprehensive results, leaderboards, and additional information are publicly available at this https URL.

---


### 431. [Comparing British and American Audio Description of Movies](https://arxiv.org/abs/2608.09792)

**<font color=#1a73e8>作者：</font>** Igor Sterner, Alex Lascarides, Frank Keller  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Narrating the visual component of movies is known as audio description. It is a narrative technique designed to enable blind and visually impaired individuals to follow the story. However, it is far more constrained than most narratives: the descriptions not only need to convey the story in the movie, but they must also fit into gaps between dialogue and they need to conform to guidelines that exist in each region. In this work, we compare audio description created in the United Kingdom against audio description created in the United States. We use guidelines written for these two regions, alongside the impressions from a practitioner in the field, to motivate specific hypotheses about the differences. We test these hypotheses against our pre-existing corpus, which provides both human-authored American and British audio description for each of 206 movies. Results provide quantitative evidence to uphold all tested hypotheses, including differences in lexicon, the use of the progressive aspect, the use of passive constructions, the use of subjective adjectives and modifiers, when characters are named, how scenes are cued, and degree of overlap with movie dialogue and music. Our work offers a quantitative lens into the narrative technique of audio description.

---


### 432. [Modern Backbones Improve Multi-task DETR for Mammography Classification and Lesion Localization](https://arxiv.org/abs/2608.09801)

**<font color=#1a73e8>作者：</font>** Dinh Tan Nguyen, Quang-Hien Kha, Le-Hoang Nguyen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint exam-level prediction and candidate-region localization may improve the usefulness of AI support in mammography. We study this setting using a multi-task DETR framework, where shared representations support both image-level malignancy prediction and lesion localization, and evaluate its performance on OPTIMAM and a biopsy-confirmed SGM1k cohort. Across both datasets, modern backbones consistently outperformed older ResNet-style features, with ConvNeXtV2 and DINOv3 giving the strongest overall results, whereas MambaVision was less competitive. On OPTIMAM, ConvNeXtV2 achieved the best overall performance, reaching 97.96% AUC, 99.89% sensitivity, 25.08% mAP@.5, and 74.38% recall@.25. On SGM1k, DINOv3 gave the strongest overall results, with 90.97% AUC, 86.28% sensitivity, 82.00% specificity, 27.04% mAP@.5, and 77.32% recall@.25. These findings suggest that backbone quality is a critical factor in effective multi-task mammography, with ConvNeXtV2 emerging as a particularly strong and well-matched CNN backbone for mammography in this framework.

---


### 433. [Multi-Agent AI Safety as an Institutional Design Problem](https://arxiv.org/abs/2608.09828)

**<font color=#1a73e8>作者：</font>** Abdullah X  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly work inside systems that govern how they delegate tasks, move information, execute actions, and use shared resources. Recent work already shows that deployment rules can change collective behavior. Here we ask which parts of an AI institution produce safety and how they do it. This is the first paper from POLIS, an ongoing research programme studying algorithmic institutions for multi-agent systems. We report a frozen 5,280-episode study suite. The main pre-specified delegation experiment spans four model families; a targeted high-conflict diagnostic adds three additional model endpoints. In matched structured workflows, the model sees different rule formulations and guards consult different authority states. We also vary the attractiveness of the immediate compliant internal/self fallback and allow blocked workflows to continue. A detailed constitutional prompt produces 0/384 realized violations. A provenance-aware executable guard also produces 0/384, although it blocks prohibited attempts in 51/384 episodes; 44/51 of those episodes later complete safely. The local-state guard's failures concentrate in scenarios where an ordinary transformation changes visible policy while originating authority stays fixed. In matched laundering scenarios, that guard admits violations in 22/96 episodes and provenance enforcement in 0/96 (p = 4.77 x 10^-7). A separate resource-allocation experiment shows that revealing the numerical value of an otherwise identical cap changes agent requests. In these structured workflows, the same final violation rate can hide very different mechanisms. The rule itself is only part of the institution. The authority state the system trusts matters, and so does the path available after a block.

---


### 434. [Deep Multimodal Wearable Sensor Fusion for Detection of Body-Focused Repetitive Behaviors](https://arxiv.org/abs/2608.09830)

**<font color=#1a73e8>作者：</font>** Samaneh Rezaeimanesh, Mohsen Behradfar, Mohammad Fili 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Body-focused repetitive behaviors, such as hair pulling and skin picking, are compulsive motor actions commonly associated with obsessive-compulsive and anxiety disorders. Their early, objective detection remains difficult because the movements are subtle and overlap with ordinary, non-pathological gestures. We developed and evaluated a multimodal deep learning framework to detect and classify these behaviors from wrist-worn sensor data. The data, collected by the Child Mind Institute using the Helios wrist-worn device, combine inertial measurement units, thermopile sensors, and time-of-flight sensors, capturing kinematic, thermal, and proximity information. The framework combined a convolutional neural network with a gated recurrent unit, alongside modality-specific autoencoders and a late-fusion classifier, to exploit temporal and spatial dynamics. It achieved an F1 score of 0.985 and an area under the receiver operating characteristic curve of 0.997 for binary detection, distinguishing these behaviors from other activities, and a macro-averaged F1 score of 0.700 with an area under the curve of 0.963 across a nine-class scheme that distinguished each individual behavior from a single grouped Non-Target class, improving over single-modality baselines. Post-hoc interpretability based on Shapley additive explanations showed that the time-of-flight and inertial modalities dominated discriminative power by capturing spatial proximity and dynamic movement, while hierarchical clustering indicated that misclassifications were driven primarily by the anatomical region of the gesture. These findings demonstrate that multimodal sensor fusion enables accurate, objective, and continuous behavioral monitoring. This work establishes a foundation for real-time, wearable-assisted mental health diagnostics and personalized interventions in biomedical research and clinical care.

---


### 435. [Real-Time Climate Risk Assessment for Supply Chain Resilience: A Data-Driven Nowcasting Framework for Colombian Agriculture](https://arxiv.org/abs/2608.09846)

**<font color=#1a73e8>作者：</font>** Hernan J. Silva-Sosa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a methodological framework for real-time climate risk assessment using data-driven nowcasting techniques to enhance supply chain resilience in Colombian agricultural contexts. Climate variability in Colombia, characterized by irregular rainfall, temperature fluctuations, and recurrent extreme events, has a direct impact on agricultural production and logistics, particularly for time sensitive crops. The proposed approach integrates short term climate forecasting based on historical meteorological observations with supply chain risk modeling to establish a conceptual early warning system architecture. A prototype implementation developed in a controlled computational environment demonstrates the feasibility of the framework using historical meteorological and agricultural time series derived from official statistics and reanalysis products, without reliance on satellite imagery or computer vision components. The methodology addresses the integration of climate nowcasting with supply chain decision making through explicit risk mapping, threshold-based categorization, and stakeholder-oriented risk signals. Results from synthetic and historical data experiments indicate that short term precipitation nowcasts can be translated into actionable risk indicators for agricultural supply chains, supporting anticipatory decisions related to inventory, sourcing, and transport.

---


### 436. [Agentic Auto-Research is Fuzz Testing](https://arxiv.org/abs/2608.09855)

**<font color=#1a73e8>作者：</font>** Yifeng He, Jicheng Wang, Yinzhe Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous research agents can generate experiments faster than researchers can validate them. Researchers have responded by scaling the proposer and ranking more samples with a learned judge or human reviewers. We argue that this *generate-and-rank* paradigm misses the problem of sparse feedback. Within a declared research problem, an agent follows the control loop of a greybox fuzzer: it proposes a candidate, executes it, observes feedback, and chooses what to try next. A fuzzer rarely finds a bug, but coverage makes partial progress observable on every execution. Fuzzers then use that signal to mutate inputs and allocate effort, rather than only to rank completed runs. Auto-research needs the same two capabilities. First, each experiment should expose a cheap, dense signal of epistemic progress before final scientific validation is available. Second, that signal should determine the next intervention so that the agent searches rather than repeatedly samples. Because the optimized progress signal is guidance rather than a verdict, final validation must still decide what counts as a discovery using evidence protected from adaptive reuse. We propose controlled tests of whether candidate signals predict validated progress, whether feedback-directed search yields more validated discoveries per unit cost than repeated sampling, and whether protected validation reduces false discoveries. Feedback architecture, not only generation, is a central bottleneck in auto-research.

---


### 437. [A Bird's-Eye View on Security Considerations in RFCs](https://arxiv.org/abs/2608.09865)

**<font color=#1a73e8>作者：</font>** Jukka Ruohonen, Qusai Ramadan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Request for comments (RFCs) are Internet standards, memorandums, and related technical documents about core Internet protocols made via and released by the Internet Engineering Task Force (IETF). In the early 1990s each RFC was required to have a section for security considerations. The present work examines these sections. According to the empirical results, (1) over 90% of the RFCs sampled have discussed security explicitly in these sections, (2) although mandatory security requirements have only seldom-if ever-been imposed. Furthermore, (3) the RFC-to-RFC reference network specific to the security consideration sections is sparse, although a few RFCs and their security consideration sections are heavily referenced. In addition, (4) the volume of references peaked during a period from circa mid-1990s to mid-2010s. Regarding the topics discussed in the sections, (5) these do not represent general security issues, such as spoofing or eavesdropping; rather, the topics mostly reflect distinct security issues specific to distinct protocols. With the exceptions of network security in general, security specifications, and routing, (6) also the longitudinal evolution of the topics is protocol-specific. As the subject matter has not been previously examined, these empirical results fill a gap in the standardization literature.

---


### 438. [ArchAgent v2: A Case Study with the Data Prefetching Championship](https://arxiv.org/abs/2608.09874)

**<font color=#1a73e8>作者：</font>** Abraham Gonzalez, Raghav Gupta, Akanksha Jain 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic artificial intelligence has shown great promise in automating algorithm design, but scaling similar techniques to computer microarchitecture discovery remains challenging due to vast search spaces, strict hardware budgets, and long simulation times. In this work, we present ArchAgent v2, a framework which scales automated microarchitecture search to multi-level data prefetching. While the original ArchAgent successfully discovered single-level cache replacement policies in competition settings, it does not scale to multi-level prefetching where the design space and degrees of freedom are larger. To overcome this, we introduce two new additions to ArchAgent: a cascaded evolutionary search that subdivides the design space by sequentially evolving and freezing prefetchers at individual cache levels, and a hardware-realizability feedback loop that embeds real-time size-estimation directly into the evolution process.
Evaluated under identical rules of the 4th Data Prefetching Championship (DPC4), ArchAgent v2 automatically designs a three-level prefetcher that outperforms the winning hand-designed solution, further demonstrating automated agentic discovery as a useful tool for computer architects. Our discovered policy achieves a 3.8\% geometric mean IPC speedup over the baseline overall and a 0.3\% improvement over the prior champion, BertiGO. On low-bandwidth single-core configurations, our policy yields a 4.6\% performance speedup compared to only 2.6\% for BertiGO. However, multi-core evolution still remains a significant challenge due to simulation latency impeding evolution speed. Finally, our profiling of an ArchAgent evolution of over 12,000 candidate designs provides key insights into how automated evolutionary agents explore and synthesize complex microarchitectural logic.

---


### 439. [Space-Creating versus Dead Possession: An Off-Ball Possession-Quality Index for Broadcast Football](https://arxiv.org/abs/2608.09887)

**<font color=#1a73e8>作者：</font>** Seongjin Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ball possession is the most-cited and most-misleading number in football: 60% recycled in one's own half is not 60% spent pinning the opponent back. Existing event-based possession-value frameworks (expected threat, VAEP, on-ball value) price on-ball actions but ignore the off-ball question a sterile possession poses: did holding the ball create space, or was the circulation dead? We answer this in two layers. First, an event-side junk-possession index prices each possession sequence by its peak threat gain under an expected-threat grid and -- after reconstructing the live scoreline to exclude lead-protecting circulation -- flags low-threat sequences in tied-or-losing states. On the 2026 FIFA World Cup (103 matches, 206 team-matches) the flag correlates negatively with points (r=-0.37) and xG difference (r=-0.51, partly index-coupled). It is not a repackaging of on-ball value: with team offensive VAEP and field tilt held fixed, the junk flag stays strongly negatively associated with points (p<0.0001, also match-clustered) while VAEP is not significant -- in this same-match (descriptive) regression it adds information beyond this on-ball action-value model. Second, for a flagged window we resolve whether it was spatially dead or space-creating by projecting broadcast video to pitch coordinates and measuring a Space-Creation Index (SCI): a net pitch-control change capturing whether the possession seized space or pushed the opponent's block back. Across 31 of 35 flagged windows from nine World Cup matches (a purposive sample), 74% are spatially non-space-creating, 19% weak progression, and 6% space-creating windows the event flag alone would score as failure -- including a side with 73% of the ball that exited on penalties (two non-creating windows). The two layers separate space-creating-but-unconverted from sterile possession, a distinction event-only on-ball value cannot make.

---


### 440. [Fairness in Link Prediction Beyond Demographic Parity: A Reproducibility Study](https://arxiv.org/abs/2608.09899)

**<font color=#1a73e8>作者：</font>** Valentijn Oldenburg, Floris de Kam, Stef de Wildt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In fair ranked link prediction, demographic parity ($\Delta_\mathrm{DP}$) is a common fairness metric. Yet, Mattos et al. (2025) argue that it fails to detect exposure bias because it ignores where links appear in the ranking. In this study, we reproduce this claim by showing that $\Delta_\mathrm{DP}$ can indicate aggregate parity even when some subgroup-pair links are systematically ranked lower than others. The proposed rank-aware Normalized Discounted KL-divergence (NDKL), however, does detect such disparities. We also reproduce the effectiveness of MORAL, a post-processing method that improves exposure-based fairness while maintaining competitive utility. Beyond reproduction, we assess robustness using synthetic homophily settings, categorical sensitive attributes, and additional fairness and utility metrics, including subgroup-pair-adapted Attention-Weighted Rank Fairness (AWRF). Overall, our results show that exposure-based metrics uncover biases hidden by $\Delta_\mathrm{DP}$ and that MORAL reduces these biases with minimal utility loss across diverse settings and datasets. We release a corrected, reproducible implementation at this https URL.

---


### 441. [DSLE: A Learning Environment for Dark Souls Boss Encounters](https://arxiv.org/abs/2608.09902)

**<font color=#1a73e8>作者：</font>** Derin Gezgin, Jim O'Connor, Tanner Goodwin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce the Dark Souls Learning Environment (DSLE), a containerized platform that presents all 22 boss encounters of Dark Souls: Remastered as game-playing agent benchmarks through a Gymnasium-style interface. DSLE combines real-time combat, high-dimensional visual input, and sparse terminal rewards, with each environment step being a real action executed against the running game. To support controlled comparison, we define DSLE-5, a representative five-boss subset, spanning a melee fight, a spatially constrained arena, an environmental-hazard fight, a multi-target fight, and a fast final-boss fight, that we recommend as the starting suite for agents built on DSLE. On DSLE-5 we evaluate a random policy, an expert system, an evolutionary baseline, and PPO and DQN agents trained from visual input. The expert system and the evolutionary baseline each defeat the Asylum Demon, the game's tutorial boss (63% and 43% peak win rates), but none of the five methods defeats the other four DSLE-5 bosses; PPO and DQN show no measurable learning (at most 0.33% win rate on the tutorial boss, 0% elsewhere) within a budget that already costs tens of wall-clock hours per run. A broader study running the evolutionary baseline across all 22 encounters under advantaged all level-50 stats yields wins on only a handful of additional early-game bosses and leaves the rest unwon. The failure cases range from sub-10-second deaths in cramped, multi-target encounters to minute-long stalemates that inflict almost no damage, and we report them through survival time and damage dealt rather than win rate alone.

---


### 442. [Beyond Hazard Resemblance: Contrastive Event Adjudication for Training-Free Video Anomaly Detection](https://arxiv.org/abs/2608.09908)

**<font color=#1a73e8>作者：</font>** Wenti Yin, Xiang Wang, Huaxin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly detection (VAD) aims to identify and temporally localize abnormal events in videos. Supervised methods learn anomaly decision boundaries from target-domain annotations but require substantial in-domain data. Existing training-free methods leverage the rich semantic knowledge and reasoning capabilities of pretrained models to interpret visual content, yet these capabilities do not directly define an anomaly decision criterion: richer anomaly descriptions better capture hazard resemblance without resolving abnormality. To this end, we propose Contrastive Event Adjudication for training-free Video Anomaly Detection (CEAVAD), which shifts the unit of inference from isolated anomaly concepts to falsifiable event hypotheses and establishes an inference-time explanatory boundary through the interaction between competing explanations and video evidence. Specifically, CEAVAD first uses public-safety knowledge to construct hazard-benign event contrasts, pairing each hazard mechanism with a generic normal account and a mechanism-specific benign counterpart. It then determines whether the target interval better supports a hazard explanation or its benign competitor, yielding a revisable contrastive boundary proposal for the target. Finally, CEAVAD adjudicates between the competing explanations to determine whether the hazard hypothesis survives the video evidence, supporting both temporally localized anomaly detection and evidence-grounded explanations. Experiments on three widely used VAD benchmarks demonstrate that CEAVAD achieves state-of-the-art performance under the training-free paradigm.

---


### 443. [Overcoming Data Scarcity and Confidentiality in Hardware Assurance via Synthetic Generation](https://arxiv.org/abs/2608.09914)

**<font color=#1a73e8>作者：</font>** Gijung Lee, Ronald Wilson, Damon L. Woodard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware assurance relies on scanning electron microscopy (SEM) to verify nanoscale structures, but assembling the large, high-quality datasets required for automated analysis is impeded by time-intensive acquisition and strict intellectual property (IP) constraints on proprietary designs. We propose a privacy-preserving pipeline that secures IP by heavily distorting the functional design while generating a visually realistic synthetic dataset from a small set of initial examples. A StyleGAN first learns the distribution of hardware layout masks to generate novel, macroscopically varied structures. Subsequently, a conditional GAN (Pix2PixHD) translates these masks into realistic SEM images that preserve authentic textures and noise. The primary finding of this work is that a segmentation model trained exclusively on this synthetic data not only demonstrates a successful "sim-to-real" transfer to real images but also outperforms a baseline model trained on the limited real dataset. Because the underlying synthetic layouts are demonstrably novel and reproduce none of the specific proprietary routing of the original design, deploying the final segmentation model mitigates the risk of exposing sensitive IP to attacks like gradient inversion and membership inference, providing a highly secure, high-performance solution for hardware assurance.

---


### 444. [GENCO - A Unified Neural Solver Embedded in a Development Framework for Steady-State Grid Analysis](https://arxiv.org/abs/2608.09921)

**<font color=#1a73e8>作者：</font>** Alban Puech, Matteo Mazzonelli, Tamara R. Govindasamy 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models are transforming business workflows and boosting productivity, yet they remain largely absent from engineering domains such as power system analysis, where strict physical consistency must be enforced.
We present GENCO (GEometric Neural Corrective Optimizer), a unified neural solver for steady-state transmission grid analysis that handles power flow (PF), optimal power flow (OPF), and state estimation (SE) within a single architecture and shared network representation. To support advances in neural power system solvers, we introduce the open-source GridFM Development Framework, which standardizes synthetic data generation and training in a low-code environment. We also release large-scale datasets with millions of PF and OPF scenarios across diverse grid topologies to support reproducible benchmarking.
We evaluate GENCO on the PFDelta and OPFData benchmarks against state-of-the-art neural solvers and classical solvers, including Newton-Raphson and IPOPT, as well as on real-world Hydro-Québec SCADA data. For large-scale PF, GENCO recovers the full AC operating state, including voltage magnitudes and reactive power that DC-PF cannot provide, while matching DC-PF-level active power-balance residuals. It achieves up to 30x speedups over Newton-Raphson at only 2x the runtime of DC-PF. For OPF, it achieves up to 85x speedups over IPOPT while improving feasibility, optimality, and runtime over DC-OPF. For SE, GENCO is more robust than classical weighted least squares to noisy measurements and network parameter errors, and always returns a high-quality estimate even when weighted least squares fails to converge.
Together, the unified architecture and development framework provide a new approach to large-scale steady-state grid analysis, lowering the barrier to entry for power system engineers and marking a step toward Grid Foundation Models.

---


### 445. [Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning](https://arxiv.org/abs/2608.09926)

**<font color=#1a73e8>作者：</font>** Haodong Li, Shaoteng Liu, Tianyu Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The world evolves following its dynamics, i.e., its laws of motion. However, leading video diffusion models largely fit the pixels without modeling how the pixels transit over time. Thus, they render visually plausible frames but may not accurately obey the laws. To capture the dynamics purely from pixels, we introduce Latent Dynamics Reasoning (LDR). LDR casts the latent transition as an explicit kinematic integration, where the lower-order dynamics are integrated numerically and the model regresses only the third- and higher-order residual that drives the rollout. For this integration to extrapolate better, LDR runs it on a structured latent rather than dense convolutional features. Following PhyWorld, we validate LDR on a controlled white-box physics benchmark spanning five tasks (uniform motion, parabola, collision, bouncing, looming), focusing on out-of-distribution scenarios that reveal whether a model has truly learned the underlying dynamics. LDR extrapolates the learned dynamics far better: the gap between its in- and out-of-distribution error is over 20$\times$ smaller than the video diffusion baseline's, under both single- and joint-task training at 256$^2$ resolution, while using 26$\times$ fewer parameters and running 143$\times$ faster. LDR can even generalize under severe shift: for example, trained only on red balls moving left-to-right, it correctly predicts the motion of a blue square moving right-to-left. To our knowledge, this is the first video world model that extrapolates learned dynamics beyond its training distribution. Project page: this https URL

---


> [!TIP]
> 当前位于：**401-445**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-445**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
