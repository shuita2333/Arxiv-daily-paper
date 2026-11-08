# 📦 其他研究 | 2026年11月09日

> 本类共 **237** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-237](./part-05.md)

---

### 101. [Neural Image Compression with Internal-External Prior Fusion and Alignment](https://arxiv.org/abs/2611.07644)

**<font color=#1a73e8>作者：</font>** Tiancheng Si, Wenlong Xu, Dahua Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing context models for learned image com- pression rely primarily on internal priors from the current image, overlooking common patterns and typical textures shared across natural images. To address this limitation, we propose an Internal-External Prior Fusion-Alignment (IE-PFA) context model built upon quadtree spatial-channel joint modeling, where a learnable dictionary shared by the encoder and decoder serves as an external prior. Specifically, an RWKV-based Spatial- Channel Prior Fusion (RSCPF) module efficiently fuses inter- nal and external priors along spatial and channel dimensions with linear complexity, while a training-only Self-Distilled Prior Alignment (SDPA) mechanism aligns them without inference overhead. Moreover, our model supports variable-rate coding over 64 quality levels within a single network and is accelerated by custom CUDA operators. Experiments on seven benchmarks demonstrate state-of-the-art rate-distortion performance, achiev- ing an average BD-Rate saving of 21.65% over VTM-22.0-Intra, with only 29.9M parameters and the fastest coding speed among advanced neural codecs (61 ms encoding and 52 ms decoding). Code is available at this https URL.

---


### 102. [WaSP: Wasserstein Data Synthesis Pipeline for Solver-Free Operator Learning](https://arxiv.org/abs/2611.07646)

**<font color=#1a73e8>作者：</font>** Ryan Liu, Chuwei Wang, Ricardo Baptista 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators offer fast surrogates for solving PDEs, but training them typically requires expensive input-solution pairs. Two solver-free alternatives include physics-informed learning and training on manufactured data. Physics-informed learning approximates solutions by minimizing PDE residuals. While the residual norm must be strong enough to control solution error, stronger norms increase mini-batch variance and hinder optimization. Manufactured data constructs input-solution pairs for learning by applying the PDE operator to artificial solutions. However, the resulting training distribution can be mutually singular with the target distribution, yielding poor accuracy on the target distribution. We introduce the Wasserstein Data Synthesis Pipeline (WaSP), which trains on manufactured input-solution pairs while gradually mitigating the distribution shift. WaSP synthesizes new pairs by applying the learned operator to a path of intermediate distributions converging to the target input distribution. Training proceeds in stages along this path. At each stage, the previous surrogate generates solutions, and the exact PDE operator derives corresponding inputs, yielding training pairs for the next surrogate. Theoretically, we prove a stepwise error-propagation bound for the distribution shift introduced during synthesis. Empirically, WaSP reduces solution error by $3.9\times$ to $9.5\times$ compared to existing solver-free methods on PDEs such as Allen-Cahn, Kuramoto-Sivashinsky, and Ginzburg-Landau, and better reproduces the two chaotic systems' statistical observables.

---


### 103. [UniGADD: Universal Generator-Agnostic Deepfake Detector](https://arxiv.org/abs/2611.07647)

**<font color=#1a73e8>作者：</font>** Bernard Tomczyk, Agil Aghasanli, Plamen Angelov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce Universal Generator-Agnostic Deepfake Detector (UniGADD), a novel method that employs supervised learning to achieve high accuracy on known deepfake generators, while maintaining robust performance on previously unseen ones. The proposed approach follows a two-stage optimisation process. In the first stage, a contrastive loss encourages the model to learn discriminative feature embeddings from real and known fake images, resulting in strong performance within the training domain. In the second stage, the embedding space is refined by promoting inter-cluster separation and intra-cluster compactness, applied exclusively to real samples. This refinement enhances generalisability, enabling the method to exhibit improved robustness against unseen deepfake generation techniques. UniGADD achieves accuracy on par with state-of-the-art methods for known generators, while significantly outperforming them on unseen cases, demonstrating its scalability and practical applicability for adversarial content detection.

---


### 104. [PharmAgents2: Towards Autonomous End-to-End Drug Discovery](https://arxiv.org/abs/2611.07653)

**<font color=#1a73e8>作者：</font>** Haichuan Tan, Bowen Gao, Tao Huang 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Drug discovery requires continuous scientific decision-making across a vast research space. We introduce PharmAgents2, an autonomous system for end-to-end drug discovery that combines knowledge-enhanced decision-making with organized large-scale exploration. Paper2Skill extracts transferable scientific decision knowledge from public sources and, together with expert-developed skills, supports research decisions. Self-Scaling Discovery expands exploration through parallel agents inheriting research context and decision-making capabilities across targets, scientific hypotheses, and discovery strategies. We introduce PharmAgents-Bench v0.1, comprising 121 questions across nine decision scenarios and three end-to-end tasks assessed with expert-defined process rubrics. PharmAgents2 outperforms evaluated baselines in most decision categories and achieves the highest process scores on all three end-to-end tasks. In three real-world studies, autonomous investigations generated findings subsequently supported by human-executed experiments. For LpxH, PharmAgents2 hypothesized a previously unreported allosteric site and screened compounds against it, identifying a novel inhibitor scaffold with experimentally confirmed inhibitory activity and binding. For JAK1, it prioritized a covalent inhibition strategy and nominated compounds with experimentally demonstrated activity. Starting from a known bioactive molecule, Self-Scaling Discovery explored candidate targets across the proteome and identified a new binding target, with the interaction subsequently confirmed experimentally. PharmAgents2 represents a prototype of a virtual pharmaceutical company, marking a step toward autonomous end-to-end drug discovery.

---


### 105. [ArtCrafter: Feed-Forward Generation of Articulated 3D Object with Analytic Joint Derivation](https://arxiv.org/abs/2611.07658)

**<font color=#1a73e8>作者：</font>** Minh Canh Tu, Quang-Binh Nguyen, Khoi Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Articulated 3D assets are essential for robotic simulation and training, yet their generation from casual images poses a key challenge: recovering part geometry and kinematics that remain mutually consistent. We present ArtCrafter, a novel feed-forward generative model for controllable generation of articulated 3D objects from a pair of images, one depicting the object in the rest state and the other in the open state. At the core of ArtCrafter is a DiT-based generative model that jointly produces part-level meshes for both articulation states in a single forward pass. Inspired by Slot Attention, its denoising process operates on a $1+2N$ slot layout comprising one shared base slot and $N$ paired rest/open slots, encouraging each pair to bind to the same kinematic part. To ensure geometrically consistent and disjoint part generation, we introduce Triplet Attention to enforce cross-state geometric consistency between paired rest/open slots anchored through the shared base slot, and a repulsion loss $\mathcal{L}_{\mathrm{rep}}$ on decoded part point clouds to prevent inter-part penetration throughout denoising. Given the resulting paired meshes, URDF joint parameters---type, axis, origin, and range---are derived analytically from the rigid transformation between each rest/open pair, providing an interpretable alternative to learned joint-parameter regression. Extensive experiments on both in-distribution and out-of-distribution datasets demonstrate that ArtCrafter outperforms existing method under the same dual-state setting in geometry quality and articulation precision, while remaining competitive with methods operating under different input settings and paradigms.

---


### 106. [Simple Meta-Learning for HPO and CASH Using Performance Representations](https://arxiv.org/abs/2611.07659)

**<font color=#1a73e8>作者：</font>** Emiel Witting, Cheng Yan, Tom Julian Viering  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization for Hyperparameter Optimization (HPO) and Combined Algorithm Selection and Hyperparameter Optimization (CASH) often relies on explicit hyperparameter encodings as surrogate inputs. In high-dimensional search spaces, however, such representations can make it difficult for standard surrogates to learn useful performance models. We instead study an alternative meta-learning representation that describes each configuration directly as its historical performance across prior tasks. This representation can be paired directly with standard surrogate models. Our scope is the iterative selection component of AutoML, deciding which configuration to evaluate next from a fixed candidate set, rather than a complete framework with features such as runtime estimation, cost-aware budgeting and ensembling. We further apply this representation to maximal marginal relevance (MMR), a diversity-based re-ranking criterion from recommender systems, as a posterior-free acquisition rule. When selecting and optimising across multiple models on the TabArena benchmark, the performance-based representation paired with a linear Bayesian ridge regression model outperforms dedicated meta-learning baselines, achieving the same tuned performance in roughly half the number of trials. For single-model HPO, it remains a competitive second. Across both benchmarks this method closely matches or improves on regret at a fraction of the complexity and cost, requiring no pre-training or tuning and scaling independently of search space dimensionality. Code for reproducing our results is available at this https URL.

---


### 107. [Which Objects Stay? Learning Hierarchical Persistence Beliefs for Lifelong Open-Vocabulary Object Maps](https://arxiv.org/abs/2611.07662)

**<font color=#1a73e8>作者：</font>** Thanh Nguyen Canh, Haolan Zhang, Nak Young Chong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lifelong object maps must estimate whether an object remains at its previously observed location after it leaves view. Existing persistence filters rely on class-based survival priors, making them difficult to apply reliably in open-vocabulary settings. We introduce HiPer, a hierarchical persistence filter that derives persistence beliefs directly from data rather than semantic categories. For a new object, HiPer retrieves visually and geometrically similar training instances and estimates an initial survival rate from their observed histories, without requiring class labels. This estimate initializes a conjugate Beta belief over the object's survival probability, which is updated in closed form using detections and missed observations under Rosen's persistence-filter framework. When an object is re-identified at a new location, its persistence belief is transferred with the object, enabling the map to learn object-specific mobility over time. Experiments on 120 held-out simulated sequences show that HiPer consistently achieves the best performance among competing methods. Retrieval-based priors outperform CLIP-derived label priors, and object-specific online learning provides further gains. Results on 47 held-out 3RScan environments demonstrate that the proposed retrieval-based prior also outperforms state-of-the-art baselines in real-world settings.

---


### 108. [CoGenRec: A Unified Generative Framework for Complementary Vision Reconstruction](https://arxiv.org/abs/2611.07665)

**<font color=#1a73e8>作者：</font>** Yapeng Meng, Yuguo Chen, Xiangru Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Capturing scenes with extreme motion and high dynamic range is fundamentally constrained by trade-offs among temporal resolution, spatial detail, signal-to-noise ratio, and dynamic range under practical bandwidth, power, and quantum-efficiency limits. Conventional frame-based cameras therefore suffer from temporal undersampling, exposure-induced motion blur, and sensor saturation. The Complementary Vision Sensor (CVS) addresses these limitations by decomposing visual information across two complementary pathways, a spatially dense, temporally sparse, long-exposure RGB pathway and a temporally dense, spatially sparse, short-exposure patiotemporal difference pathway. Their complementary measurements provide appearance, structural, and motion cues across a wide dynamic range that enable reconstruction beyond conventional imaging. We present CoGenRec, a complementarity-driven generative reconstruction framework that unifies video deblurring, high-temporal-resolution frame interpolation, and HDR fusion. CoGenRec encodes complementary measurements into multi-scale spatiotemporal features using exposure-aware appearance modeling and bidirectional temporal propagation. These features constrain a video diffusion model and are injected into the VAE decoder to recover fine structures lost during latent-space compression, combining the scene fidelity of physical measurements with the appearance recovery capabilities of learned video priors. On SportsSloMo-CVS, CoGenRec improves PSNR over the strongest general-purpose baseline by 4.40 dB for deblurring, 3.89 dB for frame interpolation, and 5.04 dB for HDR fusion, respectively. It also achieves strong perceptual quality on 129 unseen scenes captured with real CVS. These results establish a unified approach to advance high-quality reconstruction under challenging motion and illumination conditions. Project page: this https URL.

---


### 109. [Calibrated Target Noise Recovers Curvature from the Gradients](https://arxiv.org/abs/2611.07671)

**<font color=#1a73e8>作者：</font>** Arash Jamshidi, Katsiaryna Haitsiukevich, Aristides Gionis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating curvature information from gradients alone is a fundamental problem in machine learning. The challenge becomes particularly acute in settings where only aggregate mini-batch gradients are available, yet curvature information is still required for applications such as preconditioning in optimisation, sampling, and early stopping. Perhaps surprisingly, we show that a simple target-perturbation scheme suffices to recover such curvature information from gradients alone. Our method injects zero-mean noise into the targets, with variance calibrated to the local output curvature. The covariance of the resulting noisy batch gradients then recovers practical curvature matrices, without requiring per-sample gradients, second-order derivatives, or other internal network quantities. For a broad class of non-linear models, our scheme recovers the Generalised Gauss--Newton (GGN) matrix; for feed-forward ReLU networks, it additionally recovers the diagonal blocks of the population Hessian. We demonstrate that the resulting estimator is simple, lightweight, provably optimal, and easy to integrate into existing training pipelines. Experiments demonstrate accurate curvature recovery, faster optimisation when the estimator is used for preconditioning, and the utility of the estimated GGN for early stopping.

---


### 110. [Instrumental Variables in Continuous-Time Stochastic Processes](https://arxiv.org/abs/2611.07674)

**<font color=#1a73e8>作者：</font>** Lars Pennig, Søren Wengel Mogensen, Niki Kilbertus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal questions often arise in systems that evolve in continuous time. While instrumental variable (IV) methods provide a principled approach to identify causal effects in static or discrete-time settings, even in the presence of unobserved confounding, they do not yet extend to continuous-time dynamics. In this work, we develop an IV framework for stationary continuous-time stochastic processes parameterized by stochastic differential equations (SDE), where the instrument itself takes the form of a stochastic process. We encode the structural sparsity and causal effects directly at the infinitesimal level of the drift, and contrast these assumptions with the IV assumptions on the discretized version of the same process. Based on these structural assumptions, we derive moment restrictions using path-valued instruments. We show how these restrictions simplify for Ornstein-Uhlenbeck processes and present an identification condition together with a corresponding consistent estimation method. Finally, we extend our estimation framework to nonlinear causal effects by expressing the path-based moment restrictions leveraging the signature kernel. Empirically, our method recovers causal effects in confounded continuous-time systems where maximum-likelihood-based estimation and discrete-time IV methods are systematically biased.

---


### 111. [$O(1/n)$ Convergence Rate for RVI $Q$-Learning](https://arxiv.org/abs/2611.07676)

**<font color=#1a73e8>作者：</font>** Avik Kar, Siddharth Chandak, Rahul Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish finite-time convergence guarantee for synchronous relative value iteration (RVI) $Q$-learning for finite weakly communicating Markov decision processes (MDPs). For stochastic Krasnosel'ski\uı--Mann iterations driven by a non-expansive, linearly regular map on a finite-dimensional normed space, we establish last-iterate mean-squared residual bounds under martingale-difference noise whose conditional second moment grows at most linearly with the squared residual. Suitable polynomial stepsizes of order $n^{-a}$ yield an $O(n^{-a})$ rate for $0<a\leq1$. We verify linear regularity and the noise condition for the centered Bellman operator for finite weakly communicating MDPs. Applying the general result gives an $O(n^{-1})$ bound on the mean-squared Bellman span residual of RVI $Q$-learning iterates when a suitable stepsize sequence is used. The positive gap between optimal and suboptimal stationary deterministic policies then yields an $O(n^{-1})$ bound on the expected suboptimality of the greedy policy. Consequently, $O(\epsilon^{-1})$ synchronous iterations suffice for an $\epsilon$-optimal policy in expectation. These guarantees are instance-dependent, with constants that depend on the hitting-time parameters and the suboptimality gap of the second-best policy.

---


### 112. [GEKey: Learning Geodesic Eccentric 3D Keypoints via Self-Supervision](https://arxiv.org/abs/2611.07677)

**<font color=#1a73e8>作者：</font>** Pierre Onghena, Santiago Velasco-Forero, Beatriz Marcotegui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point clouds represent 3D object geometry as sets of spatial coordinates. A fundamental task in their analysis is keypoint detection, i.e., identifying a sparse subset of points that captures the most salient features. While supervised methods rely on manual annotations, unsupervised approaches leverage intrinsic geometric properties to localize keypoints without human input. We introduce GEKey, a self-supervised framework that uses the geodesic eccentricity transform, an SE(3)-invariant geometric measure, to identify instance-specific salient points. These points serve as pseudo-labels to train a model that aligns its predictions with the object's intrinsic structure. GEKey is simple, efficient, and robust, preserving intra-class variation by balancing instance-specific and category-level structure. Extensive experiments on ShapeNetCoreV2, KeypointNet, CAPE, ITOP, and DeformingThings4D show state-of-the-art performance in both keypoint detection and alignment, with strong resilience to noise, downsampling, deformations, and real-world conditions. The code and pretrained models are available at this https URL.

---


### 113. [DEQ-Det: Dual Evidence Queries for Few-Shot Analog IC Device Detection](https://arxiv.org/abs/2611.07682)

**<font color=#1a73e8>作者：</font>** Zidong Zhao, Rong Huang, Chengxing Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting analog integrated circuit (IC) devices in layout images supports circuit analysis and inspection. With only a few annotated examples, variation in device geometry and visual similarity to dummy or routing structures make reliable detection difficult. Foreground similarity alone can highlight plausible targets without distinguishing them from competing layout patterns. We propose Dual Evidence Queries for Detection (DEQ-Det), which constructs complementary foreground and background references from the same support images without additional annotations. Foreground references capture target morphology, while selected background references characterize surrounding layout patterns. Both sources guide query selection and region verification, combining target appearance with layout context. Across five held-out device categories and three random seeds, DEQ-Det achieves macro AP50 of 39.41 and 53.03 at 10 and 30 shots, exceeding the strongest listed baselines by 3.97 and 9.71 points, respectively. A matched 30-shot ablation further shows that RoI background evidence reduces pooled false positives at comparable recall, supporting its role in interference suppression.

---


### 114. [ReferClaw: Disambiguating User Intent for Egocentric Assistance](https://arxiv.org/abs/2611.07683)

**<font color=#1a73e8>作者：</font>** Hangyu Qin, Junbin Xiao, Angela Yao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Users of egocentric AI assistants often ask short, ambiguous questions whose intended referents cannot be uniquely resolved from video and dialogue history. For example, "Where did I leave it?" may refer to several previously handled objects. Existing VideoQA systems typically commit to a single interpretation, risking plausible but intention-misaligned answers. We introduce ReferClaw, an agentic framework that formulates egocentric streaming QA as an interactive process: the assistant asks clarifying questions to resolve user intent before answering. Three cooperating agents identify candidate interpretations, request clarification, and generate answers grounded in the resolved intent and visual evidence. A bounded, cost-aware policy balances expected information gain against user effort while limiting clarification turns and question complexity. Referclaw learns from interaction through intent-specific skill updates and process-reward-guided policy optimization with agent-level credit assignment. Evaluations on augmented egocentric QA benchmarks demonstrate improved answer accuracy and joint answer-and-grounding performance over existing baselines, alongside zero-shot transfer across datasets. These findings support interactive clarification as a practical approach to resolving online user intent in egocentric streaming assistance.

---


### 115. [Non-Parametric Mutual Information Estimation with Vine Copulas](https://arxiv.org/abs/2611.07693)

**<font color=#1a73e8>作者：</font>** Sigurd Holmsen, Berit Omli Øksnes, Ingrid Hobæk Haff 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce VINE: a non-parametric mutual information (MI) estimator based on simplified D-vine copulas. Approximating the joint density with a simplified D-vine allows the density ratio to simplify to a product of pair copulas, which we can estimate non-parametrically. This structural simplification yields VINE, a flexible and computationally efficient MI estimator. We compare VINE against SotA neural MI estimators on a range of datasets, both under settings where the simplified D-vine assumption holds and where it is violated, demonstrating competitive accuracy at a lower computational cost for low- to medium-dimensional datasets.

---


### 116. [Equivariant Deep Learning in Direct-Product Space for Electronic-Structure Hamiltonian Prediction](https://arxiv.org/abs/2611.07695)

**<font color=#1a73e8>作者：</font>** Shi Yin, Zujian Dai, Xinyang Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most existing equivariant architectures for Hamiltonian prediction propagate features in direct-sum spaces of irreducible spherical tensors, whereas the target Hamiltonian is naturally an operator block in a direct-product representation over local orbital and spin bases. This representation mismatch fragments contiguous Hamiltonian blocks, obscures direct manipulation of orbital couplings, and organizes features into irregular angular-momentum components that require numerous transformations and are poorly aligned with efficient hardware execution and memory management. To address both the representation mismatch and computational bottleneck, we propose DP-Learner, an equivariant learning framework that performs message passing directly on Hamiltonian-like operator blocks in the direct-product space. Theoretically, we propose Lie-generator-based directional embedding and invariantly weighted left--right products and contractions that preserve equivariance to SO(3), SU(2), and spatial inversions, without explicit Clebsch--Gordan decomposition or inverse reconstruction. Methodologically, we instantiate this principle as a Transformer architecture, in which Hamiltonian-like feature matrices or tensors evolve through equivariant operators in the direct-product space, while non-linear invariant scalar routing controls structured gating over matrix units, directional propagation, attention, and environment-embedded context interactions. We further construct MP-HAM-110K, a large-scale Hamiltonian dataset comprising more than 110,000 material structures covering 68 elements with both Hamiltonian and wavefunction data. Experiments on MP-HAM-110K and Materials-HAM-SOC demonstrate that DP-Learner dramatically improves Hamiltonian prediction accuracy and inference efficiency over the state-of-the-art method.

---


### 117. [InfMasking: A Unified Variational Framework for Synergistic Multimodal Learning](https://arxiv.org/abs/2611.07702)

**<font color=#1a73e8>作者：</font>** Liangjian Wen, Qun Dai, Jiang Duan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal models are expected to exploit synergistic information, that is, information available only when multiple modalities are observed together. In practice, however, a fusion module can fit the training objective by relying on a dominant modality or on information that modalities share, and the synergy between modalities is often left unused. We propose InfMasking, a unified multimodal learning framework based on Infinite Masking. Before fusion, InfMasking randomly masks the features of each modality; each sampled mask produces a different partial combination of cross-modal evidence and a fused representation of the corresponding modality interactions. All masked fused representations are required to remain consistent with a reference target: the unmasked fused view when training is unsupervised, and the class proxy of the task label when labels are available. Maintaining this consistency across diverse partial combinations discourages reliance on a dominant modality or on shared information alone, and drives the fusion module to learn cross-modal interaction patterns that remain meaningful under partial observations. Since the objective is an expectation over infinitely many masks, we model the masked fused representations as Gaussian and optimize closed-form variational bounds, whose population-moment gaps are controlled by the masking-induced covariance under this model. On the evaluated benchmarks, InfMasking improves predictive performance and yields higher mean PID estimates of task-label synergy in learned modality-specific representations, alongside higher InterSHAP interaction attribution in the trained predictors. Code is available at this https URL.

---


### 118. [FlyingDrones: A Dataset and Benchmark for Optical Flow Estimation from UAV motion](https://arxiv.org/abs/2611.07705)

**<font color=#1a73e8>作者：</font>** Laurenz Ruzicka, Roman Pflugfelder, Daniel Cremers  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical flow is an important cue for drone analysis in aerial surveillance, airspace monitoring, and long-range target tracking, where motion remains informative when appearance is weak. Estimating the motion of small Unmanned Aerial Vehicles, however, is difficult because distant targets occupy few pixels, have low contrast, and move against complex dynamic backgrounds. Standard optical-flow benchmarks emphasize large, object-centric motions and therefore do not characterize distant aerial targets well. We introduce FlyingDrones, a generated benchmark with dense ground-truth optical flow and segmentation masks derived from physically based rendering, and define resolution-normalized metrics (EPE Norm) that normalize flow by image dimensions. We evaluate 16 state-of-the-art model families on a motion- and size-stratified subset of 999 flow pairs at three resolutions. Every family recovers drone motion better than the zero-flow reference, but the gap between families widens with resolution: at 1920x1080, global-matching, recurrent, transformer, and short-window temporal models separate clearly from pyramid, classical, self-supervised, lightweight, and diffusion models. Within-family checkpoint spread is comparable to or larger than between-family spread, so the training curriculum is as important as the architecture. Two complementary studies test the benchmark beyond synthetic accuracy: a ground-truth-free motion-alignment evaluation on 21 cameras of real UAV footage shows that the synthetic ranking carries a moderate, significant signal about real-world performance (Spearman \r{ho} = 0.63 over 41 checkpoints) while the exact top ranks differ, and a fine-tuning study shows that 800 FlyingDrones pairs reduce held-out drone-region error by up to 37% and improve drone localization on the real footage for all four architectures tested.

---


### 119. [Towards Generalist Graph-Level Anomaly Detection](https://arxiv.org/abs/2611.07706)

**<font color=#1a73e8>作者：</font>** Junjun Pan, Yixin Liu, Yu Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-level anomaly detection (GLAD) aims to identify graphs that deviate significantly from the majority. While recent advances have achieved competitive performance, existing approaches mainly follow a dataset-specific paradigm, requiring substantial in-domain data and training cost when applied to new application scenarios. This limits their scalability and practicality in real-world applications where labeled data is scarce and diverse domains are continuously emerging. In this paper, we investigate the problem of generalist GLAD, which seeks to learn a single unified model capable of detecting anomalous graphs across multiple domains with minimal supervision on the target data. This problem introduces key challenges, including learning transferable patterns from heterogeneous graph datasets and effective adaptation under limited supervision. To address these challenges, we propose GenGLAD, a generalist GLAD approach that leverages discriminative subgraph extraction as the core mechanism to learn transferable anomaly knowledge and enable efficient adaptation to new domains. Specifically, GenGLAD employs a graph neural network-based discriminative subgraph extraction model to learn the anomaly-discriminative substructures that distinguish anomalous and normal graphs across diverse domains. During the test-time adaptation phase, multi-dimensional discrepancies between the extracted subgraph and multi-level contextual information are calculated to characterize anomalies from multiple perspectives. For efficient adaptation, a lightweight scoring module is introduced to automatically decide the most informative signals, improving robustness against misleading patterns. Extensive experiments on diverse benchmark datasets demonstrate that the proposed approach achieves strong performance, superior generalization ability, and improved data efficiency compared to existing methods.

---


### 120. [AffineGS: Unlocking Accurate Geometry in 3DGS via Spatially Varying Affine Rectification](https://arxiv.org/abs/2611.07709)

**<font color=#1a73e8>作者：</font>** Tze Ho Elden Tse, Jizong Peng, Richard Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has become the leading approach for photorealistic novel view synthesis, yet its geometric accuracy lags behind its visual quality. Existing depth-guided methods attempt to resolve this by regularizing the optimization with monocular depth priors, typically using a single global scale-and-shift alignment. Crucially, we discover a fundamental flaw in this assumption: modern monocular depth networks systematically exhibit region-dependent, piecewise-linear distortions. This discovery invalidates standard global alignment strategies, which warp scene geometry by enforcing a single transform. To address this, we introduce a spatially varying affine rectification model that corrects monocular disparity into consistent metric depth using regionally smooth, edge-aware fields. We further derive a normal-aware regularizer that uses spatial gradients to couple the rectified disparity with 3DGS depth and normals. Across diverse experimental settings, our sensor-free method shows strong photometric quality of Gaussian Splatting while substantially improving geometric accuracy and outperforming state-of-the art geometry-focused methods.

---


### 121. [Fast and Accurate Hand Estimation in Pixels, Interaction and World Space](https://arxiv.org/abs/2611.07711)

**<font color=#1a73e8>作者：</font>** Jinkun Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular hand mesh estimators commonly predict rig parameters and project the mesh to obtain 2D keypoints. We find that directly predicted 3D joints agree better with 2D predictions, and fitting a mesh to predicted points reduces mesh error. We present FAH (Fast and Accurate Hand Estimation), a family of models built on SAM 3D Body's hand branch through fine-tuning and feature distillation. The models predict corresponding 2D and 3D joints and surface points, fit MANO or MHR-Hand, and optionally estimate anatomical parts and contact without object geometry at inference. Causal refinement reduces acceleration error, and camera estimation places the hands in world space. Experiments show improvements in image-space alignment, hand geometry, contact estimation and world-space tracking over the evaluated baselines. The default ViT-L model runs at 65 fps with mesh fitting on an RTX 4070 Ti SUPER, or 49 fps with parts and contact enabled. The smallest ViT-S model reaches 125 fps without mesh fitting, parts or contact. Code: this https URL.

---


### 122. [Selective Event Evidence and Persistent Temporal Priors for Event-Based Point Tracking](https://arxiv.org/abs/2611.07713)

**<font color=#1a73e8>作者：</font>** Xiaokai Song, Zhang Li, Leqi Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras enable tracking under fast motion and challenging illumination. However, stable long-term point tracking remains challenging: event activity is sparse and varies with scene content and motion, complicating correspondence, while trajectory estimates can drift over long sequences. Together, these challenges motivate a tracker that selectively uses informative event evidence and retains trajectory constraints across temporal windows. We propose Selective Event Evidence and Persistent Temporal Priors (SEPT), an event-only framework for tracking any point (TAP) over long sequences. SEPT introduces two complementary modules: Task-Adaptive Event Evidence Modulation (TEEM) and Persistent Trajectory Prior (PTP). Using only tracking supervision, TEEM learns a bounded reliability field that weights the event tensor across space, time, and channels before feature extraction. PTP carries geometric information across overlapping windows by marginalizing a fixed local quadratic trajectory model with a Schur complement. Its visibility-aware correction refines overlap coordinates, while a clipped terminal velocity initializes coordinates at newly exposed timestamps. SEPT builds on the ETAP architecture. SEPT is trained exclusively on synthetic EventKubric data and evaluated on five datasets across TAP and feature tracking. Results show that SEPT outperforms the retrained ETAP baseline in average Jaccard for TAP and in feature age and expected feature age for feature tracking; it also surpasses several methods combining event and frame inputs on EC and EDS. The source code is publicly available at this https URL.

---


### 123. [Multimodal Information Interactions Bottleneck for Multimodal Self-Supervised Learning](https://arxiv.org/abs/2611.07718)

**<font color=#1a73e8>作者：</font>** Liangjian Wen, Jiangtao Zheng, Jiang Duan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal self-supervised learning is challenged by heterogeneity, unequal informativeness, and complex information interactions across multimodal data sources such as images, text, audio, and tabular data. While contrastive methods effectively align shared semantics, they typically rely on strong multi-view redundancy assumptions, overlooking modality-specific and synergistic information, thus leading to suboptimal representations. We propose the Multimodal Information Interactions Bottleneck (MIIB), a principled framework grounded in Partial Information Decomposition that explicitly encodes redundant, unique, and synergistic information within multimodal interactions. MIIB employs a dual-path model architecture for modality-specific encoding and multimodal fusion, optimized using surrogate tractable entropy-based objectives that enforce minimal sufficient representations without requiring explicit mutual information estimation. By leveraging variational bounds and score-based entropy estimation, MIIB efficiently captures complex cross-modal interactions while suppressing superfluous information. Experiments across diverse benchmarks demonstrate consistent improvements over state-of-the-art multimodal self-supervised methods. Code is available at this https URL.

---


### 124. [Continued Training of Continuous Language Flows with Token Identity Squared Supervision](https://arxiv.org/abs/2611.07721)

**<font color=#1a73e8>作者：</font>** Jiawei Jiang, Zhaoxiang Zang, Zhengtao Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow models have recently been extended to language modeling, generating text through continuous denoising in token embedding spaces. Pretrained models provide token representations and contextual prediction capabilities, but improving generation with limited additional training requires an appropriate connection between supervision and continuous generation. Continuous MSE evaluates a predicted vector obtained by weighting token embeddings with predicted probabilities; different probability distributions can yield the same vector and are therefore indistinguishable under this objective. We propose Token Identity Brier Flow (TIBF), which applies squared supervision directly to token identities when continuing pretrained language flows. TIBF combines network scores with token-matching scores under a Gaussian observation model, supervises token probabilities using the Brier loss, and uses probability-weighted embeddings for continuous generation. With fixed token embeddings, we show that the squared error between predicted token probabilities and the true posterior bounds the squared errors of continuous denoising predictions and flow velocities. A risk decomposition separates uncertainty inherent in the observation from posterior fitting error, motivating continued training that preserves pretrained embeddings and focuses on probability prediction. We also establish convergence to token embeddings under ideal predictions and sufficient conditions for local convergence with prediction error. From common pretrained initializations and under matched continuation budgets, frozen-embedding TIBF achieves this http URL values of 33.96 on OWT and 81.17 on LM1B, outperforming continuous-MSE and CE continuation controls. It attains the lowest this http URL at every tested sampling budget on both datasets, together with the lowest repetition rate on LM1B.

---


### 125. [Static Recovery Is Not Dynamic Stability: Dynamics-Aware Benchmarking of Protein Motif Scaffolding](https://arxiv.org/abs/2611.07723)

**<font color=#1a73e8>作者：</font>** Emile de Bruyn, Moritz Schäffler, Jannik Schneider 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein motif scaffolding benchmarks assess whether generative models can build scaffolds around functionally important residues. Their conclusions depend on which motifs are tested and which criteria define success. Existing benchmarks typically use small hand-curated motif sets and static refolding criteria, but protein function often depends on conformational ensembles and transitions. Here, we address both benchmark scope and success criteria. We introduce BILBY-PRO, a systematically derived benchmark of structurally conserved functional motifs from PROSITE-linked experimental structures, comprising 220 cases from 174 PROSITE motif-pattern entries. Evaluating six recent scaffold-generation models reveals distinct patterns in target coverage and unique-solution yield: RFDiffusion and Proteina solve more targets, whereas ESM3 produces more unique successful scaffolds on the targets it solves. We further introduce BILBY-MD, a reference-based all-atom molecular dynamics evaluation framework. Applied to statically solved designs from the original MotifBench benchmark, it compares motif drift, scaffold drift, motif-contact preservation, and motif-dihedral free-energy landscapes against reference simulations. Of 55 statically solved model-problem pairs, 31 satisfy our MD-supported criterion and only 8 pass all checks. Compact, self-contained motifs are often MD-supported, whereas interface-like or context-dependent motifs fail more frequently. Static refolding success therefore provides useful evidence of local motif recovery but does not establish dynamical fidelity of the full scaffold. BILBY highlights three complementary axes of motif-scaffolding evaluation: target coverage, unique-solution yield, and MD-supported dynamical fidelity.

---


### 126. [Comparing Classification and Feature Learning by Analyzing Their Loss Functions in Normalized Spaces with Different Scale Factors](https://arxiv.org/abs/2611.07741)

**<font color=#1a73e8>作者：</font>** Qiufu Li, Huibin Xiao, Linlin Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classification and feature learning are two closely interrelated fundamental tasks. Feature learning in supervised settings is typically achieved by training classification models, under the common assumption that higher classification accuracy implies better feature quality. In this paper, we first point out that classification accuracy reflects the sample-wise local properties of a model on a dataset, whereas feature learning aims to learn features with good dataset-level global properties, such as intra-class compactness and inter-class separability. From the first principle of feature learning, we redesign the binary cross-entropy (BCE) loss, a counterpart of the cross-entropy (CE) loss used in classification. Then, in normalized feature space, we analyze the minima of the BCE and CE losses and show that both can lead to neural collapse, where sample features from different classes become maximally compact and maximally separated. More importantly, by investigating the convergence behaviors of the two losses as the scale factor $\gamma$ varies in the normalized space, we reveal how classification accuracy and feature quality change differently across spaces of different sizes. Under a fixed training strategy, a very large $\gamma$ achieves perfect classification accuracy but slows convergence toward the ideal feature geometry, whereas a very small $\gamma$ makes classification highly sensitive to small perturbations. A moderate $\gamma$ is therefore necessary for simultaneously achieving reliable classification and well-structured features. Extensive experiments validate these findings and demonstrate that BCE loss exhibits advantages in long-tail and open-set recognitions, as it better aligns with the global requirements of feature learning.

---


### 127. [Ordering Multivariate Time Series by Volatility Memory: A Temporal Convolutional Approach to Volatility Heredity](https://arxiv.org/abs/2611.07746)

**<font color=#1a73e8>作者：</font>** Kaoutar El Azaar, Mohamed Hamlich, Moncef Garouani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Volatility dynamics can carry information about temporal relationships that is not apparent in the conditional mean. Extracting this information is difficult because the persistence of each variable can obscure its dependence on other variables. This paper presents QS-TCN, a method for ordering multivariate time series that combines statistical estimates of volatility memory with temporal convolutional learning. Persistence estimates obtained by quasi-maximum likelihood and temporal modes extracted by the Matrix Pencil method define structured filters within the network. Together with learned filters, they represent the history of the target and support comparisons of directional evidence between variables. These comparisons are combined into a global order of precedence, which does not identify a causal graph. The method is evaluated on synthetic systems with linear and nonlinear volatility interactions and on the Finance and fMRI benchmarks, whose reference relations are known. Across the four synthetic volatility regimes studied, QS-TCN reaches a higher mean ordering quality than an external lead--lag ordering and its squared-input adaptation, although the gain over the adaptation is uncertain in two regimes. Applications to currency, gold and cryptocurrency markets are reported descriptively.

---


### 128. [ConvPE: Convolutional Position Embedding Improves Transformers](https://arxiv.org/abs/2611.07749)

**<font color=#1a73e8>作者：</font>** Zehao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ConvPE (Convolutional Position Embedding) improves both the performance and efficiency of Transformer models in language modeling, long-context extension, and vision. It injects a windowed, content-dependent bias into attention scores through a lightweight causal convolution over a low-dimensional projection of the hidden states. As a lightweight plug-in, ConvPE is compatible with RoPE, attention masks, and KV concatenation. It also supports high-dimensional position embeddings via high-dimensional convolutions. In a reproduction, ConvPE outperforms five 1D baselines and eight 2D baselines. The code is publicly available at this https URL.

---


### 129. [Foresee to Trade: Forecast-Augmented Policy Optimization for Portfolio Management](https://arxiv.org/abs/2611.07750)

**<font color=#1a73e8>作者：</font>** Zeyu Liu, Xuanzhi Feng, Haoran Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online investment services must translate asset opportunities into investment outcomes for users' accounts, yet the same market opportunity can warrant different account actions. We study how supervision from future asset opportunities can strengthen account-level trading decisions and propose Forecast-Augmented Relative Policy Optimization (FRPO). FRPO separately supervises asset opportunities and account decisions through a jointly learned representation: a Financial State Head (FSH) learns future relative-return targets to provide asset-level opportunity supervision, while Same-Path Group-Relative Optimization compares trading trajectories under the same market path and initial account to provide account-level relative-outcome supervision. An Adaptive Gate coordinates auxiliary supervision using predictive variance and gradient alignment. FSH is used only during training; inference uses the encoder and policy for trading. Across DJIA30, TOPIX Core30, and three investment-style portfolios, ten-seed evaluations show that FRPO achieves the highest mean cumulative and annualized returns among the compared methods in all five settings. These results support strengthening investment agents' trading decisions through joint supervision from asset opportunities and trading outcomes.

---


### 130. [Neural Collapse on Imbalanced Datasets and Open-Set Scenario](https://arxiv.org/abs/2611.07753)

**<font color=#1a73e8>作者：</font>** Qiufu Li, Huibing Xiao, Linlin Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural collapse (NC) describes the elegant geometric structure that sample features and classifier vectors exhibit when a classification model's loss reaches its minimum. Class imbalance, however, generally distorts standard NC. In this paper, we theoretically reformulate NC on imbalanced datasets and in open-set settings. Our analysis is based on an optimization problem over class-wise averaged losses, rather than the global averaged losses used in prior NC studies. We prove that when class-wise averaged losses attain their minima, standard NC is achieved on balanced or imbalanced datasets, for both cross-entropy (CE) and binary cross-entropy (BCE) losses. We further extend the analysis to an open-set-inspired scenario, where some classes contain no training samples yet are still assigned classifier vectors in the losses. We find that in this scenario, when class-wise averaged losses reach their minima, standard NC still emerges on the known classes with training samples, while the classifier vectors of unknown classes without training samples overlap with each other and become orthogonal to those of the known classes. Finally, we analyze Softmax- and Sigmoid-based contrastive losses re-balanced by inverse sample frequency, proving that at their minima on balanced or imbalanced datasets, sample features of different classes likewise form standard NC.

---


### 131. [BiGrounder: Bidirectional Training Unlocks the Potential of GUI Grounding](https://arxiv.org/abs/2611.07765)

**<font color=#1a73e8>作者：</font>** Dengyao Shi, Tianyu Fu, Fei Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) grounding aims to map natural language instructions to precise operational coordinates, serving as a critical task for autonomous agent interaction. Current approaches formalize GUI grounding as predicting action-coordinate pairs from instructions, with end-to-end training supervised solely by final coordinates. Training datasets typically provide only a small number of descriptions per target coordinate, whereas real-world scenarios involve a much larger set of varied descriptions for the same target, which limits robustness to linguistic variation. While recent GUI grounding paradigms have begun employing reinforcement learning to enhance localization accuracy, models with limited exploratory capability before reinforcement yield constrained improvements even with identical training data during the reinforcement phase. To overcome these limitations, we propose a bidirectional reward paradigm that enables model self-reinforcement. During SFT, bidirectional training equips the model to generate action descriptions from target coordinates. During RL, the model samples semantically consistent instruction variations on-policy and grounds each variation back to its target. A cycle-consistency gate couples semantic quality to grounding success, turning the model's own instruction policy into a source of continually refreshed reinforcement trajectories. Our 4B-parameter model achieves competitive accuracy across five grounding benchmarks in our evaluation, indicating the effectiveness of the proposed training paradigm. this https URL

---


### 132. [Optimal Learning in Games with Arbitrary Delays: Best-of-Both-Worlds for Self-Play and Adversarial Opponents](https://arxiv.org/abs/2611.07773)

**<font color=#1a73e8>作者：</font>** Emmanuel Esposito, Andrew Jacobsen, Hao Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study learning in zero-sum games with delayed feedback. We introduce Multi-Anchor Optimistic Online Mirror Descent (MAO-OMD), a single algorithm which obtains optimal fast rates in self-play on smooth games, while simultaneously maintaining minimax optimal guarantees against arbitrary opponents. In particular, in smooth zero-sum games with arbitrary and unknown feedback delays, MAO-OMD obtains $O(\sigma_{\max}+1)$ social and individual regrets when used by both players, where $\sigma_{\max}$ denotes the maximum number of outstanding gradients, while also guaranteeing minimax optimal $O(\sqrt{T+d_{\mathrm{tot}}})$ individual regret against arbitrary opponents, where $d_{\mathrm{tot}}$ is the total delay. Moreover, we show that these optimal rates cannot be obtained simultaneously using the standard black-box reduction to the undelayed setting. We also extend our results to multi-player games, and to games with player-dependent delay sequences.

---


### 133. [Adapters as Data: The Latent Space of LoRAs](https://arxiv.org/abs/2611.07775)

**<font color=#1a73e8>作者：</font>** Moritz Grävinghoff, Konstantin Wehmeyer, Aron Asefaw 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LoRA adapters are usually treated as finished artifacts rather than as a data modality. Prior work has shown that LoRA adapters populate a low-dimensional manifold that a linear PCA basis already organizes well enough to support different operations such as sampling, editing, and inversion. We ask what a learned, nonlinear latent adds beyond this. We train a transformer autoencoder on the same population of LoRA identity adapters, mapping each into a latent space and compare every operation against the identical operation applied directly to the raw adapter weights. The latent preserves the capabilities already available in weight space, sampling diverse identities and editing individual attributes. Beyond preservation, we show that the latent is far more robust to displacement than weight space, degrading into distorted but still valid faces rather than texture. Fixed-dimensional weight-space representations cannot natively host adapters of more than one rank, so we extend our sequential autoencoder to hold mixed-rank adapters within one shared latent. This gives a path toward treating adapter weights of varying architecture as a single, general modality rather than one tied to a fixed rank, and points to a learned, nonlinear latent as the mechanism that could carry this generalization further, toward heterogeneous populations of adapters.

---


### 134. [EnergyBench: a live, gate-aligned benchmark of day-ahead forecasts for European power markets](https://arxiv.org/abs/2611.07784)

**<font color=#1a73e8>作者：</font>** Evgenii Genov, Ander Martinez Alonso, Christoph Bergmeir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy forecasting models are usually compared on backtests and fixed public datasets. Backtests can use data that did not yet exist when the forecast would have been made, and a fixed test set, reused across studies and possibly contained in the pretraining data of foundation models, invites overfitting to the benchmark. EnergyBench evaluates every entry live instead. Each day at 11:30 CET/CEST, thirty minutes before the day-ahead (SDAC) gate closes, every model forecasts the next day's price, wind and solar generation and load on the 15-minute grid for six bidding zones (BE, NL, FR, DE-LU, DK1, DK2). Unlike existing live benchmarks, EnergyBench runs the models itself, on one information set that it freezes at the cut-off and publishes, including three numerical weather prediction models, so that foundation models can be compared with and without the same weather covariates under the actual market deadline. Errors are pooled per series against a seasonal-naive baseline, and models are ranked by a Bradley-Terry rating on the Elo scale with a day-bootstrap interval. The field spans baselines, linear and gradient-boosted models on the frozen weather, eighteen time-series foundation models from eleven families, ensembles, and the grid operators' own forecasts. Over the first thirty-two live days, the covariates reduced the error of each of the ten foundation models run with and without them by 37-51% on matched races (64-73% on wind, 48-61% on solar). Used zero-shot, these models match or outperform a LightGBM model trained on the same covariates. Model size, from 3M to 331M parameters, has a much smaller effect, and median ensembles of the covariate models rank highest. The grid operators' pre-gate forecasts remain ahead on wind and solar, where the best single foundation models have 16-22% more error; on load the gap is 4-6%, within the intervals.

---


### 135. [Rain Beyond Streaks: Cascaded Realistic Rain and Wet Surface Synthesis via Scene Priors](https://arxiv.org/abs/2611.07793)

**<font color=#1a73e8>作者：</font>** Melissa Tijink, Kirill Tolstobrov, Shunxin Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Realistic rain synthesis is a persistent challenge for vision systems operating in adverse weather. Existing methods primarily focus on generating rain streaks, often neglecting consequent surface effects such as reflections and puddles, which are critical for perceptual realism and robustness of downstream vision tasks. We introduce CascadeRS, a rain synthesis framework that leverages depth and segmentation priors to render scene-consistent rain and surface effects. In addition to rain streaks, CascadeRS produces reflections and puddles aligned with scene semantics through a physics-inspired zero-shot, controllable generative pipeline. It produces photorealistic rainy urban scenes, with high perceptual realism, which we validate qualitatively with an extensive user study and quantitatively. We produce the Cityscapes-CascadeRS dataset, to study downstream task performance under real rainy conditions. Our results establish CascadeRS as a scalable and realistic rain-generation framework for evaluating and enhancing the robustness of vision in adverse rainy weather. Code and dataset are available via this https URL

---


### 136. [Dataset Collection and Fine-Tuning of NLLB for German--English Translation](https://arxiv.org/abs/2611.07797)

**<font color=#1a73e8>作者：</font>** SK Deeraj, Yash Ingle, Pruthwik Mishra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the curation of a high-quality parallel corpus from OPUS Books and the fine-tuning of Meta's NLLB-200 models for German--English translation. We detail a dataset extraction pipeline that filters 45k raw OPUS sentence pairs to 25k high-quality examples through encoding validation, length filtering, language identification, deduplication, and quality scoring. We present a reproducible fine-tuning methodology optimized for consumer GPUs using mixed precision, gradient accumulation, and gradient checkpointing. Our fine-tuned NLLB-600M model achieves statistically significant improvements (+3.4 BLEU, +2.6 chrF++, -3.2 TER) over the base model on literary and technical German-English translation. We demonstrate practical deployment by integrating the fine-tuned model into LinguaHaru, an existing open-source document translation system, achieving format-preserving translation across PDF and Office documents. All dataset preparation scripts, training code, and evaluation tools are provided for reproducibility. The fine-tuned model is available at HuggingFace.

---


### 137. [Self-Supervised Diffusion Models for Handwritten Signature Verification via Ruin Reconstruction](https://arxiv.org/abs/2611.07810)

**<font color=#1a73e8>作者：</font>** Peirong Zhang, Zhenhua Yang, Jiaxin Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handwritten signature verification (HSV) is a critical biometric technique in legal and forensic authentication, whose efficacy hinges on the discriminability of signature representations. Current HSV methods predominantly adopt supervised learning to enhance representation quality, leaving self-supervised learning largely unexplored. We propose \emph{SigDiffuser}, a diffusion-based self-supervised framework for signature representation and verification. At its core, \emph{SigDiffuser} introduces a novel pretext task termed \emph{Reconstruction from Ruins (RFR)}, which deliberately ``ruins'' signatures through severe crumpling, obliterating their structural integrity and writing styles. A visual encoder is employed to capture crucial handwriting patterns from intact signature regions, guiding the denoiser to reconstruct the ``ruined'' portions and learning meaningful representations. Additionally, we introduce a \emph{pyramidal feature aggregation module (PFAM)} to bridge the visual encoder and denoiser, enhancing representation quality via hierarchical aggregation and modulation. Extensive experiments on multilingual signature datasets demonstrate that \emph{SigDiffuser} significantly outperforms both state-of-the-art SSL methods and HSV models. We further show that increasing the crumpling severity on signatures effectively improves representation quality. Notably, our work demonstrates that extreme destruction, coupled with self-supervised diffusion models, can yield superior signature representation compared to traditional mild deformations, paving new avenues for HSV and other biometric domains. Code will be publicly available.

---


### 138. [MV-Sign: Multi-View 3D Motion Integration and Enhanced Text-to-Motion Conditioning for Sign Language Production](https://arxiv.org/abs/2611.07811)

**<font color=#1a73e8>作者：</font>** Singyu Muk, Kaustubh Kundu, Kunyuan Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language production (SLP) aims to generate appropriate sign language motion from spoken language text. However, current 3D SLP methods suffer from noisy supervision and weak text conditioning. Specifically, these methods typically rely on pseudo-3D motion data fitted from single-view frontal videos, which introduces severe self-occlusion and loses fine-grained hand details, ultimately degrading downstream production. To overcome these limitations, we propose a comprehensive framework that jointly integrates multi-view 3D motion data and optimizes the text-conditioning pathway. First, we introduce How2Sign-MV3D, a high-fidelity dataset constructed via a novel cross-view curation pipeline that fuses multi-view estimates to resolve occlusions and filter non-signing segments. Second, we design a robust SLP model incorporating a sign-aware spatio-temporal VQ-VAE (ST-VQVAE) for joint body-hand tokenization, a pseudo-gloss adapter, and keyframe-aware retrieval to enhance text-to-motion alignment. Evaluated on the How2Sign benchmark, our framework reduces body and hand DTW-PA-JPE by 32.8% and 20.9% respectively compared to the state-of-the-art. Finally, we release two new high-quality 3D datasets, ASLCitizen-3D and MM-WAuslan-MV3D, alongside SGNify-MV as a multi-view video benchmark to support broader community research.

---


### 139. [CMDiff: Left Atrial Scar Segmentation from 3D LGE MRI Using Conditional Mask Diffusion Model: A Feasibility Study](https://arxiv.org/abs/2611.07814)

**<font color=#1a73e8>作者：</font>** Jing Zhang, Bastien Bergere, Jonas Leite 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Late gadolinium enhancement (LGE) cardiac MRI enables non-invasive assessment of left atrial (LA) scar, an imaging marker associated with atrial fibrillation ablation outcome. However, automatic scar segmentation is hindered by low contrast, the thin atrial wall, scarce labels, and extreme class imbalance. Conditional diffusion offers iterative mask generation, but its suitability for sparse 3D LA scar segmentation remains unclear. To address this gap, we propose Conditional Mask Diffusion (CMDiff), which predicts clean masks using a dynamic-encoder-conditioned 3D sinusoidal UNet. We compared CMDiff with a deterministic baseline on identical cases in five-fold cross-validation of 60 scar-labelled public LASCARQS subjects, with 48 training and 12 held-out cases per fold. CMDiff achieved a scar DSC of 0.47 $\pm$ 0.08, HD95 of 12.89 $\pm$ 6.39 mm, and ASD of 1.91 $\pm$ 0.96 mm, compared with deterministic baseline values of 0.51 $\pm$ 0.08, 10.86 $\pm$ 5.39 mm, and 1.58 $\pm$ 1.03 mm, respectively. Under the same implementation, clean-mask prediction performed substantially better than the noise-prediction configuration evaluated in this study. Thus, CMDiff was technically feasible but did not improve segmentation performance: DSC was lower, and both HD95 and ASD were higher. Direct mask diffusion therefore provides an analytical alternative, but not a competitive performance advance for this task. The source code is publicly available at this https URL.

---


### 140. [STAG-Net: Structure-Aware Attention over Landmark Groups for Lightweight Head Pose Estimation](https://arxiv.org/abs/2611.07828)

**<font color=#1a73e8>作者：</font>** Asiri Gawesha Lindamulage, Sanka Mohottala, Dharshana Kasthurirathna 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Head pose estimation is important for human computer interaction and driver monitoring, but many image based methods remain too costly for resource constrained deployment. We propose STAG-Net, a structure-aware attention over landmark groups for lightweight head Pose estimation that estimates head pose from facial landmarks using movement aware selection, spatial clustering, compact DeepSet encoders, self attention, and a global geometry descriptor. We develop variants using FaceMesh and Face Alignment Network landmarks and evaluate them under cross dataset and subject independent protocols on 300W-LP, AFLW2000, and BIWI. STAG-Net achieves the lowest mean absolute error among all compared landmark based methods in every evaluated setting. On BIWI frames with valid detections, the FAN variant also records the lowest overall error among all compared methods, reaching $3.51^\circ$ under cross dataset evaluation and $2.39^\circ$ under subject independent evaluation. The regressors use only 0.012 to 0.043 million parameters and 24.1 to 83.6 thousand FLOPs, about three orders of magnitude fewer FLOPs than FSA-Net. Despite including landmark extraction and regression, the FaceMesh pipeline reaches 322.9 frames per second on a Tesla T4 GPU, nearly twice the 164.5 frames per second of the fastest measured image based baseline, and 111.0 frames per second on CPU. After normalization by dataset size, STAG-Net processes training samples seven to eight times faster than FSA-Net and more than one hundred times faster than HopeNet and TokenHPE, while complete training finishes within 28 minutes. These results show that STAG-Net combines leading landmark based accuracy with substantially lower training and inference cost.

---


### 141. [Enhanced MRI brain tumor detection using deep learning in conjunction with explainable AI SHAP based diverse and multi feature analysis](https://arxiv.org/abs/2611.07843)

**<font color=#1a73e8>作者：</font>** Asif Rahman, Maqsood Hayat, Nadeem Iqbal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent innovations in medical imaging have markedly improved brain tumor identification, surpassing conventional diagnostic approaches that suffer from low resolution, radiation exposure, and limited contrast. Magnetic Resonance Imaging (MRI) is pivotal in precise and accurate tumor characterization owing to its high-resolution, non-invasive nature. This study investigates the synergy among multiple feature representation schemes such as local Binary Patterns (LBP), Gabor filters, Discrete Wavelet Transform, Fast Fourier Transform, Convolutional Neural Networks (CNN), and Gray-Level Run Length Matrix alongside five learning algorithms namely: k-nearest Neighbor, Random Forest, Support Vector Classifier (SVC), and probabilistic neural network (PNN), and CNN. Empirical findings indicate that LBP in conjunction with SVC and CNN obtained high specificity and accuracy, rendering it a promising method for MRI-based tumor diagnosis. Further to investigate the contribution of LBP, Statistical analysis chi-square and p-value tests are used to confirm the significant impact of LBP feature space for identification of brain Tumor. In addition, The SHAP analysis was used to identify the most important features in classification. In a small dataset, CNN obtained 97.8% accuracy while SVC yielded 98.06% accuracy. In subsequent analysis, a large benchmark dataset is also utilized to evaluate the performance of learning algorithms in order to investigate the generalization power of the proposed model. CNN achieves the highest accuracy of 98.9%, followed by SVC at 96.7%. These results highlight CNN's effectiveness in automated, high-precision tumor diagnosis. Code: this https URL

---


### 142. [Tasteply: Externalizing Stable and Situational Preference as Manipulable Spatial Objects](https://arxiv.org/abs/2611.07851)

**<font color=#1a73e8>作者：</font>** DaEun Choi, Daniel Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Most recommender systems treat user preferences as a single signal to infer and optimize, yet human preferences are a mix of a stable preference and situational preferences that turn on and off depending on context. Through Tasteply, we externalize this preference structure as manipulable spatial objects. Tasteply represents each situational preference as an attractor and the stable preference as an underlying global field. Users can adjust their feed by moving around the space and adjusting the strength of the global field, turning the preference structure that remains latent within the model into something they can see and act on directly to steer the recommendation algorithm. Through an exploratory study (N=5), we found that this spatial control was effective, along with its limits and future direction as a means of manipulating preference-based recommendations.

---


### 143. [CORE: Coarse-to-Fine Search with Context Management for Deep Research](https://arxiv.org/abs/2611.07859)

**<font color=#1a73e8>作者：</font>** Hoang Tran Vuong, Ngoc Quan Pham, Hung Bui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research agents answer complex questions through repeated search. They rely on a harness that runs their tool calls and returns evidence to their context. This creates a trade-off: Search works best over long passages, which give enough context for reliable semantic matching. But the returned evidence should be short, because every observation stays in the agent's context for the rest of the trajectory. We introduce CORE, a training-free harness that combines coarse-to-fine search with context management. CORE retrieves passages with a dense retriever. It then reuses the token-level similarities from a late-interaction reranker to return only the most relevant snippet from each passage. Context management lets the agent expand the context around sources it has already retrieved and suppresses repeated snippets. In controlled closed-search comparisons with the Tongyi DeepResearch and OpenResearcher harnesses, CORE achieves state-of-the-art answer accuracy and evidence recall across three agent models and three benchmarks (BrowseComp-Plus, BrowseComp-Wikipedia and BrowseComp-Plus-CM), on corpora containing up to 553M documents.

---


### 144. [OcTreeMamba: Topology-Aware Mamba for 3D Medical Segmentation via Octree Sparsification](https://arxiv.org/abs/2611.07865)

**<font color=#1a73e8>作者：</font>** Kaixiang Mai, Jiaqi Yu, Yuzhu Ji 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of 3D anatomical structures is crucial to medical image analysis. Recently, Mamba-based approaches have achieved promising segmentation performance in capturing long-range dependencies with linear-time computational complexity. However, heuristic selective scanning strategies inherently disrupt the intrinsic spatial hierarchy and increase computational redundancy, ignoring the inherent sparsity of 3D anatomical structures. To this end, we propose OcTreeMamba, a hierarchical framework that incorporates Octree structures into SSM, achieving 3D topology-aware long-range context feature propagation and integration. Specifically, a Structure Learner performs anatomy-adaptive structured sparsification through hierarchical gating and Gumbel-Softmax sampling, enabling differentiable selection of anatomical regions. The selected regions are subsequently organized by a Dynamic Octree Builder into a multi-level topology that preserves their hierarchical connectivity. Based on the constructed Octree, a bidirectional Tree-SSM propagates and integrates contextual features along connectivity-aware leaf--parent--root and root--parent--leaf trajectories. Extensive experiments on four benchmark datasets show that our proposed OcTreeMamba achieves competitive performance \wrt topological continuity and computational efficiency, particularly for recovering the complex structure on vascular datasets. The code is available at this https URL.

---


### 145. [PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State](https://arxiv.org/abs/2611.07867)

**<font color=#1a73e8>作者：</font>** Jihai Zhang, Yuhan Zhou, Junyou Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building a playable world requires more than generating plausible video: it demands responsive control, persistent spatial structure, and coherent interactions with dynamic entities. Using generated frames as the sole recurrent world representation ties these requirements to view-dependent appearance synthesis, making it difficult to maintain long-term spatial and temporal consistency in generation and interaction. We present PlayGen2, a real-time interactive world model that separates learned 3D state evolution from neural rendering. PlayGen2 maintains a persistent world memory comprising static geometry represented by a volumetric occupancy grid and identity-indexed 3D states for the player and other entities. Within a fixed-size local region, its world-state model jointly learns action-conditioned entity dynamics, geometry completion, and entity discovery, committing updates to a persistent world memory. A separate neural renderer synthesizes first-person observations from depth and semantic projections of the world state, without feeding generated images back into state prediction. Using Doom as a testbed, we demonstrate that the model successfully learns world dynamics including geometry-aware player motion and player--NPC interactions. The framework is computationally efficient, enabling the complete simulation and rendering pipeline to achieve approximately 160ms backend latency on a MacBook Pro with an M4 Pro chip. Beyond single-player interaction, we demonstrate zero-shot deployment on unseen Doom maps, multiplayer interaction through the composition of single-player models, and programmable gameplay through rule-based state interventions. These capabilities demonstrate the transferability and extensibility of the learned game-world model. Code and pretrained model weights are publicly available.

---


### 146. [PVDepth: Panoramic Video Depth Estimation via Geometry-Aware Spatiotemporal Adaptation](https://arxiv.org/abs/2611.07873)

**<font color=#1a73e8>作者：</font>** Chuanxin Song, Peixi Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramic video depth estimation is pivotal for applications such as Virtual Reality and World Models. However, advancements in this field are impeded by two primary obstacles: the scarcity of large-scale training data and the unique spatiotemporal challenges of Equirectangular Projection (ERP), which hinder the direct transfer of perspective models. In this paper, we first present PanoCARLA, a large-scale synthetic RGB-D panoramic video dataset, featuring natural motion trajectories and drone-like roaming perspectives. Building on this foundation, we propose PVDepth, an end-to-end framework adapted from perspective video depth models. To tackle ERP-specific geometric distortions and consequent non-linear temporal dynamics, we introduce two core mechanisms: (1) A Progressive Sphere-aware Noise Initialization strategy that anneals the noise distribution from planar to spherical, guiding the model to adapt to non-uniform information density; and (2) A Cube-rectified Temporal Modeling module that incorporates an auxiliary cubemap temporal branch to rectify non-linear temporal dynamics in the ERP domain. Extensive experiments demonstrate that PVDepth achieves superior performance, generating geometrically accurate and temporally consistent depth sequences. Code and data will be released at https:// this http URL.

---


### 147. [DISCERN: Distributional Synthetic Replay for Retain-Free Incremental Machine Unlearning](https://arxiv.org/abs/2611.07892)

**<font color=#1a73e8>作者：</font>** Nicolás Segura-Kunsagi, Juan Luis Suárez-Díaz, Iván Sevillano-García 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove the influence of specific training data from a trained model without retraining from scratch. In real deployments, however, deletion requests arrive over time, calling for incremental class unlearning (ICU): classes are removed sequentially, previously forgotten knowledge must remain forgotten, and the remaining classes must be preserved. We present DIstributional SynthetiC rEplay for Retain-free iNcremental unlearning (DISCERN), an intervention-based class unlearning method that replaces access to the retain set with synthetic embeddings sampled from per-class parametric distributions. Unlike prototype-based replay, which assumes an isotropic Gaussian around each class centroid, DISCERN fits Euclidean (Gaussian, Laplace, Student's $t$) and directional (von Mises--Fisher, Fisher--Bingham) families to each class and selects among them through statistical tests and, when none of them accepts, cross-validated log-likelihood. This design is motivated by the architecture-dependent latent geometry: transformer embeddings lie approximately on a hypersphere and concentrate around class directions, unlike those of convolutional networks. We evaluate DISCERN against seven retain-free baselines on MNIST, CIFAR-10, and CIFAR-100 with two convolutional and two transformer backbones, under single-class, multi-class, and incremental unlearning. DISCERN is competitive when classes are removed at once and is the most stable method in ICU on transformers: on ViT-B/16, after 20 sequential deletions it retains a harmonic mean of $0.797$, whereas the strongest method in the simultaneous setting drops from $0.918$ to $0.048$. A paired ablation shows that per-class distribution selection substantially reduces the resurfacing of previously forgotten classes, acting as a stabilizer of accumulated forgetting rather than a uniform improvement.

---


### 148. [Persistent Retrieval for Conversational Agents: A Study of Retrieval Efficiency](https://arxiv.org/abs/2611.07899)

**<font color=#1a73e8>作者：</font>** Karthik Ravula, Sathwik Kowtha, Rishabh Verma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational agents can retrieve information directly or delegate retrieval to a subagent. This design choice affects how retrieval history is maintained, what context each model call receives, and what information must be re-retrieved in follow-up questions. We compare three designs: skill-based retrieval in the main agent, a non-persistent retrieval subagent that generates a findings response, and our persistent retrieval subagent, which maintains retrieval history across turns and returns retrieved evidence directly to the main agent. Our approach also allows the main agent to request corrections from the same subagent.
We evaluate the three designs on enterprise questions posed independently, within shared conversations, and as dependent follow-ups. Across five multi-turn settings, our approach uses 43.3% fewer recorded agent-model tokens and incurs 45.0% lower estimated API cost than skill-based retrieval, while reducing average response time by 9.1%. Compared with non-persistent retrieval, it reduces response time by 15.6 seconds per question, while using 65.1% more tokens and incurring 29.1% higher estimated API cost.
Our approach shifts the retrieval subagent from producing synthesized responses to maintaining retrieval state and supplying evidence that the main agent can directly evaluate and use for answer generation.

---


### 149. [Structure from Collision via Hypothesis-Space Reasoning](https://arxiv.org/abs/2611.07900)

**<font color=#1a73e8>作者：</font>** Takuhiro Kaneko  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge of the hidden interior structure of an object, including the presence and location of cavities, is essential for predictive simulation, robotic manipulation, and nondestructive inspection. However, such cavities leave no direct signature on the static visible surface, making collision-induced deformation one of the few cues used to infer their presence. Structure from Collision (SfC) addresses this problem by recovering the hidden interior structure of an object from multiview observations of a collision event. SfC is challenging for two reasons: hidden cavities are only indirectly observable through surface motion, and voids correspond to the absence of material, making direct optimization using standard density representations difficult. The density-based SfC baseline inherits both difficulties. Surface-matching gradients do not directly indicate the cavity location, while density gradients can be weak or uninformative inside or near void regions. Therefore, we reformulate SfC as hypothesis-space reasoning, representing hidden cavities as explicit structural hypotheses whose variables encode available structural assumptions rather than relying on implicit density updates. A global stage performs gradient-free optimization over this hypothesis space using forward-only material point method (MPM) simulation. A local stage then refines the selected hypothesis as a Lagrangian particle system through gradient-based optimization using differentiable MPM simulation. On the SfC benchmark, our method improves hidden-structure reconstruction and future prediction over the density-based SfC baseline. Interior-topology stress tests and robustness analyses characterize its scope and limitations. The project page is available at this https URL.

---


### 150. [XM4D: 4D Reconstruction through Certifiable Geometric Optimization](https://arxiv.org/abs/2611.07902)

**<font color=#1a73e8>作者：</font>** Haoyu Han, Jack Benarroch Jedlicki, Jiahui Lei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 4D reconstruction remains challenging: jointly estimating camera motion, scene geometry, and non-rigid deformation entails highly nonconvex optimization, making global optimality difficult to guarantee. We present XM4D, a framework for accurate and efficient 4D reconstruction built upon certifiably globally optimal geometric optimization. By separating the estimation of camera motion from non-rigid deformation, we formulate both stages as structured quadratically constrained quadratic programs (QCQP) that admit semidefinite programming (SDP) relaxations and verifiable global optimality certificates. For camera motion estimation, we lift static point tracks into 3D using foundational depth prediction models and formulate a scaled bundle adjustment problem that jointly estimates camera poses, depth scales, and static landmarks. By analytically eliminating translations and landmarks, we reduce the problem to a QCQP over scaled rotations. For non-rigid reconstruction, we represent dynamic motion using an embedded deformation graph (EDG) and show that its tracking, rigidity, and temporal regularization objectives similarly reduce to a rotation-only QCQP. Both problems admit SDP relaxations that we solve efficiently with a GPU-accelerated Burer-Monteiro solver based on Riemannian optimization. The recovered geometry further initializes dynamic Gaussian splatting for photometric refinement. Extensive experiments across seven benchmarks demonstrate accurate camera motion estimation on both static and dynamic scenes, efficient optimization that scales to thousands of frames, and state-of-the-art novel-view rendering quality.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-237](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
