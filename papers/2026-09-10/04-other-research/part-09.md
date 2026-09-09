# 📦 其他研究 | 2026年09月10日

> 本类共 **542** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-542](./part-11.md)

---

### 401. [Learning Metamaterial Eigenmodes with Wavelet-Encoded Fourier Neural Operators](https://arxiv.org/abs/2609.08102)

**<font color=#1a73e8>作者：</font>** Han Zhang, Alexander Ogren, Cynthia Rudin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning surrogates based on neural operators have shown broad applicability in solving forward PDE problems. However, eigenvalue problems, in which an eigenparameter and one of several valid eigenmodes must be simultaneously solved, remain difficult because standard operator learning formulations assume a unique input-output map. This work demonstrates that Fourier Neural Operators (FNOs), combined with wavelet-based encodings of PDE inputs, can learn and predict multiple eigenmodes of the elastic wave equation, corresponding to deformation modes of acoustic waves propagating through arbitrary metamaterial geometries. We provide a mechanistic explanation and experimental evidence for why wavelet encodings are well matched to the dual spatial-spectral structure of the FNO, enabling deterministic mode selection on both continuous-valued and binary-valued geometries within a single model, and for why prediction accuracy varies with geometric discontinuities. For metamaterial design, the resulting surrogate accelerates the simulation stage of the design cycle by three orders of magnitude relative to finite element analysis on a consumer-grade CPU, while preserving high fidelity. These results also carry broader implications for designing input encodings in other multi-mode PDE solvers based on spectral neural operators.

---


### 402. [AVP-Inspect: Coordinated Cyber-Physical Testing for Privacy Analysis of COTS Apple Vision Pro Applications](https://arxiv.org/abs/2609.08103)

**<font color=#1a73e8>作者：</font>** Yichang Xiong, Vamsi Shankar Simhadri, Yue Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> XR devices introduce substantial privacy concerns due to their comprehensive data collection capabilities that surpass traditional computing platforms. While existing works have demonstrated privacy concerns on Android-based XR devices such as Meta Quest series by performing network traffic analysis, little attention has been paid to the Apple Vision Pro (AVP) devices, mainly due to the closed nature and the technical challenges associated with AVP devices. In this work, we make a bold attempt to detect privacy violations of AVP applications from network traffic through automatic testing on AVP devices. Our key insight is that effective AVP application testing requires coordinated control of both cyber (software) and physical (hardware) components, which we term Coordinated Cyber-Physical Testing. Building on this insight, we design and implement AVP-Inspect, an automatic dynamic analysis framework for AVP applications, overcoming significant challenges enforced by the closed-source nature of AVP ecosystem. AVP-Inspect consists of three components: an automatic device controller by building customized hardware devices, a 3D UI explorer by designing a new exploration engine, and a privacy violation detector by constructing a unified privacy taxonomy for AVP. We first evaluated AVP-Inspect on a manually constructed ground truth dataset, then performed a large-scale analysis on 324 AVP applications downloaded from the App Store, with each app tested for 20 minutes. We found that 188 (58.0%) of apps exhibit at least one violation, and more than 60% of the network traffic flows are not properly disclosed.

---


### 403. [Artificial Intelligence-Assisted Digital Inventory of Cultural Heritage & Traditional Knowledge: Case for Indonesian Open Digital Library of Culture](https://arxiv.org/abs/2609.08105)

**<font color=#1a73e8>作者：</font>** Hokky Situngkir  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Indonesian Digital Library of Culture (Perpustakaan Digital Budaya Indonesia, PDBI; this http URL) is a participatory platform that has collected tens of thousands of entries on Nusantara cultural heritage through public contribution since 2007. Manual contribution faces three structural barriers: coverage (knowledge is scattered across languages and sites), integrity (open sources mix authentic documentation with noise), and completeness (subjects are recorded but their data remain shallow). This paper presents a methodological framework for autonomous, AI-based harvesting of cultural knowledge from the open web, designed to expand corpus coverage while intensifying per-entry data depth. The methodology is organised as a five-stage economic funnel: focused crawling, multilingual extraction and canonicalisation, vector encoding with blocking, agentic decision-making, and idempotent publication, under the principle of deterministic orchestration, agentic decisions. Each stage is formalised: funnel economics and optimal filter ordering; crawl-frontier dynamics as a subcritical branching process that explains the necessity of recurrent re-seeding; fact-level novelty via a containment measure; Bayesian multi-source evidence fusion with elevated publication thresholds for sacred categories; exactly-once effects via idempotent upserts and the transactional outbox; sliding-window inference budgeting with a reservation protocol; statistical quality auditing; and seed selection as submodular coverage maximisation. The framework retains four high-value human roles: curator of direction, escalation approver, quality auditor, and guardian of meaning, while machine autonomy is raised in stages. Ethical, legal, and cultural-sensitivity implications are discussed, including the architectural guarantee that the machine never overwrites human contributions.

---


### 404. [Nyström Attention Matches Full Attention for Cross-Sectional Stock Prediction](https://arxiv.org/abs/2609.08106)

**<font color=#1a73e8>作者：</font>** Kunhan Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MASTER's inter-stock multi-head attention -- the module responsible for modeling cross-sectional stock relationships -- accounts for 42.5% of model parameters and 25% of predictive value. We systematically decompose this module and uncover a surprising structure: the learned attention is near-uniform (perplexity 278/300), yet forcing exact uniformity eliminates all cross-sectional discrimination. Spectral analysis resolves this paradox: the deviation from uniformity is low-rank (effective rank ~65, top-10 modes capture 96.5% of energy), explaining why sparse approximations consistently fail while Nystrom low-rank attention (m=32 landmarks) matches full O(N^2) attention at O(mN) cost -- certified equivalent via TOST at both N=300 (5 seeds, Rank IC p=0.003) and N=800 (10 seeds, Rank IC p=0.034). Additional findings include: (i) attention anti-correlates with return similarity (Spearman rho = -0.614; on the industry-labeled subset, -0.645 unconditionally and -0.627 after controlling for industry, beta, and volatility), suggesting complementarity-seeking rather than correlation mining; (ii) all graph-based alternatives degrade performance, with hard masking worse than complete module removal; and (iii) at N ~ 3,500 with adapted architectures, no cross-stock module (GCN, Nystrom, or MASTER-style pipeline) significantly outperforms a per-stock LSTM baseline (n=4 seeds), indicating that the benefits observed at smaller scales do not trivially transfer. These results establish that the inter-stock attention's value resides in a compressible, dynamic, near-global redistribution that rewards low-rank approximation but resists sparsification.

---


### 405. [SynthGait-19K: A Physically Grounded Synthetic Video Dataset for Gait Parameter Estimation](https://arxiv.org/abs/2609.08108)

**<font color=#1a73e8>作者：</font>** Soroush Mehraban, Xin Lei Lin, Vida Adeli 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of clinically meaningful gait parameters from monocular video is important for scalable mobility assessment, yet progress is limited by the small scale, restricted viewpoints, and limited visual diversity of existing datasets. We introduce SynthGait-19k, a physically grounded synthetic video dataset containing 19,272 walking videos derived from 6,427 MoCap sequences across 437 subjects, with paired SMPL motion and annotations for six gait parameters. To construct the dataset, we develop Gait2Vid, which unifies heterogeneous MoCap recordings through SMPL and synthesizes diverse RGB walking videos under controllable viewpoints and scene appearances. We assess the generated videos for consistency with their conditioning gait kinematics and validate extracted gait events against force-platform measurements. Using SynthGait-19K, we benchmark direct RGB, pose-based, biomechanical, and human-mesh-recovery approaches and analyze viewpoint, training-data scale, and synthetic-to-real domain shift. We also introduce GaitXFormer as a direct RGB reference model for estimating gait parameters. Synthetic supervision transfers effectively to real videos across both GaitXFormer and a pose-based architecture, demonstrating utility across different representations. We further find that spatial gait parameters are more sensitive to visual domain shift and that improved HMR reconstruction alone does not necessarily translate to improved downstream gait estimation.

---


### 406. [DriveMotion: A Large-Scale Multi-Source Benchmark for Driver Motion Sequence Modeling and Forecasting](https://arxiv.org/abs/2609.08117)

**<font color=#1a73e8>作者：</font>** Yuhang Wang, Chuheng Wei, Jingxin Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driver motion can provide cues to ongoing behavior, attention, and near-term driving intent. However, most existing driver-centric datasets focus on recognizing predefined driver behaviors from short video clips, while human motion forecasting benchmarks largely target motion outside the vehicle. We introduce DriveMotion, a multi-source benchmark for continuous driver motion forecasting. DriveMotion contains 393 hours of 133-keypoint motion sequences at 10 Hz from 360 drivers, integrating naturalistic driving data, curated public in-cabin videos, and the AIDE dataset into a unified representation with per-joint validity masks and synchronized driving context. Naturalistic driving contains long periods of limited body movement, making uniformly sampled evaluation dominated by persistence and less sensitive to brief but behaviorally meaningful motion. To address this, we use dynamics-anchored evaluation, placing forecasting windows around vehicle maneuvers identified offline from CAN signals without providing CAN to the model at inference. Arm motion in pre-maneuver windows is 3.4x greater than in route-matched stable-driving controls. On these anchored windows, learned models reduce forecasting error over persistence by up to 15%, while maneuver-enriched training improves forecast-derived Part-State F1 by 44% over the zero-motion reference. Training on the full multi-source corpus further reduces forecasting error on held-out web drivers by 38% compared with BATON-only training. DriveMotion provides identity-disjoint splits, fixed evaluation subsets, and reference implementations for reproducible evaluation of continuous driver motion forecasting. The dataset and benchmark are available at this https URL

---


### 407. [Hyperspectral Anomaly Detection via Group Sparse Low-Rank Tensor Factorization With Automatic Anomaly Grouping](https://arxiv.org/abs/2609.08121)

**<font color=#1a73e8>作者：</font>** Quan Yu, Yu-Hong Dai, Xiongjun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-rank tensor modeling has become an effective tool for hyperspectral anomaly detection. However, existing methods still suffer from high computational cost and limited flexibility in characterizing spatially structured anomalies. To address these issues, this paper proposes a hyperspectral anomaly detection method based on group sparse low-rank tensor factorization with automatic anomaly grouping (GSAA). Specifically, the low tubal rank background is characterized by imposing group sparsity on tensor factors, which provides an efficient alternative to direct tensor rank regularization. For anomaly modeling, a latent grouping map is introduced to build an automatic anomaly grouping penalty, allowing anomaly groups to be adaptively inferred from the data rather than predefined at the pixel level. To further exploit complementary spectral and spatial information, GSAA is applied in both domains, and the resulting detection maps are fused to form a spectral--spatial version of GSAA, termed GSAA-SS. An efficient linearized alternating direction method of multipliers algorithm with convergence guarantee is developed to solve the resulting model. Experimental results on five real hyperspectral datasets demonstrate that the proposed method achieves superior detection performance and competitive computational efficiency compared with several state-of-the-art methods.

---


### 408. [Sparse Data Augmentation for Optimization with Provable Guarantees](https://arxiv.org/abs/2609.08133)

**<font color=#1a73e8>作者：</font>** Behrooz Tahmasebi, Melanie Weber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In nonconvex optimization problems arising in geometric machine learning, data augmentation is commonly used to promote invariance by averaging empirical losses over transformations of the data. Computing the fully augmented objective, however, requires access to every element of the transformation group $G$, which may be prohibitively expensive when $G$ is large or accessible only through sampling. We study whether full augmentation can instead be approximated using a small, fixed sample of transformations acquired before optimization and reused thereafter. Under suitable regularity conditions, we show that, with probability at least $1-\delta$, gradient descent (GD) on the resulting sparsely augmented objective returns an $\varepsilon$-stationary point of the fully augmented objective using $\mathcal{O}\bigl((\log |G|+\log(1/\delta))/\varepsilon^2\bigr)$ group-transformation-oracle queries. By comparison, standard group stochastic gradient descent (group-SGD), which samples a fresh transformation at every iteration, uses $\mathcal{O}(1/\varepsilon^4)$ transformation queries. Therefore, gradient descent with fixed sparse augmentation requires fewer transformation queries than both GD applied to the fully augmented objective and group-SGD. Our proof techniques, which may be of independent interest, establish a uniform approximation of the full group-averaged gradient field by a random group average using spectral properties of group-induced operators and tools from representation theory.

---


### 409. [KBBQ: A Predictive Noise Law and the Limits of Spectrum Flattening in FP4 Quantization](https://arxiv.org/abs/2609.08135)

**<font color=#1a73e8>作者：</font>** Lexington Whalen, Yuki Ito, Ryo Sakamoto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a second-order theory of quantization noise in matrix multiplication in which the quantization format is characterized by the variance it assigns to each element. The constant variance profile of integer quantization recovers existing integer-noise theory, while the multiplicative profile of floating-point rounding reduces the data dependence to a scalar, the participation factor $\kappa$, yielding a closed-form signal-to-noise-ratio law. The resulting functional also admits a closed-form upper bound $\kappa^{*}$ that no function-preserving linear transform can exceed and that is attained by a recent state-of-the-art method. Building on this analysis, we introduce KBBQ (\textbf{K}appa-\textbf{B}raked \textbf{B}lockwise \textbf{Q}uantization), which parameterizes the extent to which a transform approaches this ceiling. At W4A4, across four base models and two FP4 formats, KBBQ outperforms the prior state of the art without additional deployment-time computation.

---


### 410. [GPU-Enabled Large-Scale Optimization Using Randomized Linear Algebra](https://arxiv.org/abs/2609.08136)

**<font color=#1a73e8>作者：</font>** Pratik Rathore, Zachary Frangella, Parth Nobel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces rlaopt, a PyTorch-based package for large-scale optimization and scientific computing using randomized numerical linear algebra (RandNLA). Despite substantial progress in RandNLA-based algorithms, few implementations combine GPU acceleration with a simple interface for specifying optimization problems. rlaopt addresses this gap by providing GPU-enabled solvers for positive-definite linear systems and convex empirical risk minimization with constraints and regularizers. These solvers use RandNLA to accelerate conjugate gradient (NystromPCG), operator splitting (NysADMM), and stochastic gradient methods (SAPPHIRE). Moreover, rlaopt includes a modeling language that lets users specify problems using natural mathematical syntax. rlaopt automatically checks compatibility with the selected solver and performs the required problem decomposition. The solvers also support differentiation through their iterations, enabling applications such as hyperparameter tuning. Experiments on ridge regression, bounded multinomial logistic regression, and bounded elastic net identify when randomized preconditioning improves performance and demonstrate substantial speedups from GPU execution. The package is open-source under an Apache license, with source code at this https URL and version 0.1.0 available on PyPI.

---


### 411. [MRI-Guided Reslice-Refined Cross-Slice SDF Reconstruction of the Left Ventricle from Cardiac MRI with Sparse Axial Supervision](https://arxiv.org/abs/2609.08148)

**<font color=#1a73e8>作者：</font>** Quanxin Zheng, Shuai Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing a three-dimensional left-ventricular (LV) endocardial surface from cardiac magnetic resonance (CMR) data is challenging when supervision is available on only a small number of axial slices. Through-plane geometry is weakly constrained, and automatically generated two-dimensional masks can propagate segmentation errors into the recovered shape. We present MR-RS-SDFR, a per-case implicit signed distance field (SDF) framework that reconstructs a continuous LV surface from a CMR volume and sparse axial weak masks. The method first builds a cross-slice SDF initialization from axial and longitudinal geometric cues and then refines the field using two complementary signals: MRI edge-field normal alignment, which provides an image-derived boundary cue independent of the weak masks, and differentiable reslice Dice and contour consistency, which preserve agreement with the observed planes. We evaluate three weak-mask generators -- LOO TransUNet, LOO nnU-Net, and an off-the-shelf Medical SAM3 model used without MM-WHS-specific training or fine-tuning -- and five sparsity levels from 4 to 64 axial planes. In the sparse-16 setting, final MR-RS-SDFR reconstruction reaches 0.928 Dice and 3.80mm HD95 with Medical SAM3 masks. The upstream generators do not exhibit a single common ranking across 2D and dense 3D segmentation, and nnU-Net- and Medical-SAM3-driven sparse reconstruction achieve the same mean final Dice despite different upstream error profiles. Across all three sparse-16 mask sources, MR-RS-SDFR is numerically better than protocol-matched full GHD+DVS in both Dice and HD95. Final Dice improves markedly from sparse-4 to sparse-16 and then saturates at the reported precision through sparse-64. These results support MRI-guided per-case SDF refinement as a reconstruction strategy that remains effective across weak-mask generators and supervision densities.

---


### 412. [SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents](https://arxiv.org/abs/2609.08149)

**<font color=#1a73e8>作者：</font>** Pujun Zheng, Zixin Shang, Shufan Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> SWE-Bench Pro has emerged as a standard benchmark for evaluating software engineering agents on challenging repository-level tasks. However, our analysis work show that its evaluation is undermined by two sources of unreliability: \textbf{reward hacking}, enabled by leakage of gold solutions or hidden evaluation information, and \textbf{task quality issues}, including misleading problem statements and improperly scoped tests. These issues can inflate benchmark performance and obscure agents' true coding ability. We present \textbf{SWE-Bench Pro Verified}, a verified version of SWE-Bench Pro that addresses both problems. Our approach combines \textbf{anti-hacking} safeguards that eliminate major leakage channels without disrupting normal agent functionality, with \textbf{task refinement} that minimally corrects inconsistencies within flawed instances. Evaluations on SWE-Bench Pro Verified reveal that some models perform substantially worse than previously reported, suggesting that existing results on SWE-Bench Pro may overestimate real software engineering capability. SWE-Bench Pro Verified offers a more trustworthy benchmark for assessing software engineering agents.

---


### 413. [Topology-induced Operators Reveal Complementary Graph Representations without Training](https://arxiv.org/abs/2609.08152)

**<font color=#1a73e8>作者：</font>** Meng Qin, Jinqiang Cui, Hongwei Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph representation learning has largely focused on designing increasingly sophisticated models to transform graph topology into vector representations, or embeddings. However, the extent to which embedding quality depends on model learning, rather than on the underlying topological transformations, remains unclear. Here, we show that informative embeddings can be derived without complicated model design and gradient-based training. Propagating random features through implicit hierarchical structures induced by random walks and anonymous walks yields embeddings that capture node proximity and structural role, respectively. These two training-free embeddings preserve complementary aspects of graph organization and perform competitively with classic and recent methods across various node-, edge-, and graph-level tasks. They often require substantially less computation, resulting in a favorable quality-efficiency trade-off. Combining the two types of embeddings further improves inference quality of some tasks compared with using either embedding type alone. Our results suggest that informative graph embeddings can arise from carefully chosen topological transformations before any learning operation is applied.

---


### 414. [Geodesic-informed Generative Diffusion Model For Topology-preserved Image Video Generation](https://arxiv.org/abs/2609.08153)

**<font color=#1a73e8>作者：</font>** Nian Wu, Nivetha Jayakumar, Jiarui Xing 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative diffusion models have emerged as a class of powerful techniques for various imaging applications, including but not limited to synthesis, reconstruction, and segmentation. Despite their success, current generative models pose two key limitations. First, they primarily rely on image intensity and texture information, with limited attention to underlying object geometry. As a result, they do not guarantee geometric or topological consistency during the generation process, which is a crucial requirement for high-stakes domains such as computational anatomy, biology, and robotics, where preserving object structure is critical. Second, existing models fail to explicitly learn or represent shape changes in the generative process. Such deformation dynamics remain occluded within network parameters; hence leaving the transformation process uninterpretable and physically uninformed. To address these challenges, we introduce IGG (Image Generation informed by Geodesic dynamics), a novel framework that integrates topology-preserving geodesic principles into the diffusion-based generative process. In contrast to conventional methods that operate in image intensity space, IGG learns and synthesizes diverse samples within geodesic deformation spaces, where geometric object changes are learned as smooth and invertible smooth mappings from a given template/source image. Our code is publicly available at this https URL.

---


### 415. [Boundary Voting Network for Ambiguity-Aware Timestamp-Supervised Action Segmentation](https://arxiv.org/abs/2609.08167)

**<font color=#1a73e8>作者：</font>** Runzhong Zhang, Yueqi Duan, Yang Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Timestamp-supervised action segmentation aims to segment and classify actions in untrimmed videos with a random frame annotated per action. Precisely localizing action boundaries from timestamp annotations is crucial for this setting, as it enables generating framewise pseudo-labels and applying the well-explored fully-supervised training. However, prevailing methods struggle with intrinsic uncertainty in boundary localization due to less discriminative features in action-transiting regions. This imprecise boundary estimation significantly reduces the stability and reliability of the generated pseudo-labels in ambiguous action-transiting regions, consequently resulting in performance deterioration of the trained segmentation models. In our paper, we introduce the boundary voting network that mitigates feature ambiguity by hierarchically propagating video-level global prior knowledge into local action-transiting regions. By generating key action representations as votes throughout the video and targeting action-transiting regions, all votes collaboratively contribute to action-transiting feature enhancement and boundary localization refinement. Extensive experiments demonstrate the effectiveness of our method on GTEA, 50Salads, and Breakfast datasets.

---


### 416. [WSPolypNet: Weakly Supervised Polyp Localization in Colonoscopy Videos](https://arxiv.org/abs/2609.08182)

**<font color=#1a73e8>作者：</font>** Giseong Hwang, Minjae Jo, Yeonghyeon Park 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Because dense frame-level annotation of colonoscopy videos is costly, we propose WSPolypNet, a weakly supervised framework for polyp localization using only video-level labels. WSPolypNet employs a 3D convolutional neural network trained with video-level supervision to generate class activation maps (CAMs), which identify candidate polyp regions without requiring frame-level spatial annotations. The CAM-derived localization cues are further enhanced using a multi-view strategy and provided to MedSAM2 as point prompts. MedSAM2 then propagates segmentation masks across the video, refining the coarse localization cues according to polyp boundaries. WSPolypNet achieved CorLoc scores of 47.80%, 43.68%, and 35.01% at IoU thresholds of 0.3, 0.5, and 0.7, respectively, compared with 36.87%, 33.72%, and 27.94% in the single-view setting. For small polyps, the multi-view strategy improved CorLoc@0.5 from 16.01% to 30.97%. The framework also achieved a recall of 94.51%. These results demonstrate the potential of weakly supervised spatiotemporal learning to substantially reduce spatial annotation requirements for polyp localization in colonoscopy videos.

---


### 417. [A Better Spur Should Start From Each Objective](https://arxiv.org/abs/2609.08211)

**<font color=#1a73e8>作者：</font>** Shanwen Mao, Hao Zhang, Guangtao nie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world Multi-Objective Reinforcement Learning (MORL) often suffers from sparse rewards, reward conflicts, and late-stage reward tug-of-war, causing traditional linear scalarization to experience severe metric oscillations. To address optimization conflicts among multiple objectives in real-world deployment scenarios, we propose Multi-Marginal Preference Optimization (MMPO), a fine-grained framework that intervenes at the data, gradient, and constraint levels rather than relying on coarse-grained global scalarization. Specifically, MMPO performs exposure debiasing to mitigate sparse and biased rewards, applies priority-aware orthogonal projection to decouple conflicting gradients, and introduces self-prompted gradient constraints to prevent dominant objectives from overwhelming weaker ones. Experiments on real-world e-commerce datasets show that MMPO improves training stability and consistently achieves better performance across conflicting metrics. Moreover, it generalizes robustly to broader tasks such as ToolRL and code generation, demonstrating its effectiveness as a practical paradigm for multi-objective alignment.

---


### 418. [DRIFT: Removing Diffusion Watermarks by Deflecting the Generative Trajectory](https://arxiv.org/abs/2609.08213)

**<font color=#1a73e8>作者：</font>** Rui Bao, Zheng Gao, Xiaoyu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Diffusion watermarking embeds verifiable signals into the generative process and commonly verifies them by recovering trajectory-dependent evidence, making the marks robust to conventional pixel-space distortions. Existing removal attacks either regenerate along deterministic trajectories, which often preserve the watermark-bearing latent structure, or optimize every image separately. We identify the reliance on a recoverable generative trajectory as a common attack surface among the schemes we study. Based on this observation, we propose DRIFT, a black-box attack that combines partial forward diffusion with stochastic reverse resampling. Forward re-noising limits source information available to a fixed-depth recovery pipeline, while stochastic reversal supplies alternative noise-driven paths whose removal benefit we isolate through matched sampler comparisons. Adaptive DRIFT searches a selected ladder for each image's first verifier-rejected rung and refines fidelity while retaining only updates rejected by the same verifier. At fixed depth, we derive information-theoretic and Wasserstein source-dependence bounds; under realized-ladder monotonicity, the first rejected rung is least distorted among rejected rungs on that ladder, and verifier-gated refinement preserves rejection. Across nine watermarks spanning three paradigms, DRIFT achieves 98-100% attack success and the best image quality among the compared attacks, without secret keys, verifier internals, or per-image gradient optimization.

---


### 419. [PhysFlow: Physics-Aware Optical Flow for Motion Controllable Video Generation](https://arxiv.org/abs/2609.08215)

**<font color=#1a73e8>作者：</font>** Cong Wang, Hanxin Zhu, Yonglin Tian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models have recently attracted substantial attention for their ability to generate visually compelling videos, yet ensuring physically consistent and plausible dynamics still remains a fundamental challenge, driving a growing line of research on physical realism in video generation. To address this challenge, motivated by the fact that physical regularities are primarily encoded in motion patterns, we propose PhysFlow, a novel two-stage framework for improving the physical plausibility of generated videos by decomposing video generation into motion-aware optical flow generation followed by motion-conditioned appearance synthesis. Specifically, PhysFlow consists of a physics-aware optical-flow video generator called PA-Flow and a flow-guided video generator called FlowRender. During the first stage, PA-Flow employs a physics-aware attention module to model how motion attributes and material properties influence global motion and local deformation, respectively, and generates an optical flow video as an explicit representation of motion. In the second stage, FlowRender leverages the decoupled motion representation as guidance to synthesize realistic textures and appearances, ultimately producing the final physically plausible video. To further support model training with explicit physical supervision, we construct PhysVideo, a physics-based video dataset generated with a physics engine and 3D-GS rendering, containing 10K foreground objects and 50K realistic video sequences with annotations of motion and material properties. Extensive experiments demonstrate that our proposed PhysFlow generates videos with superior physical plausibility while maintaining high visual fidelity compared with existing methods.

---


### 420. [SoftRerank: Hierarchical Soft Fusion with Candidate-Label Reranking for Long-Tailed Micro-Action Recognition](https://arxiv.org/abs/2609.08221)

**<font color=#1a73e8>作者：</font>** Yichi Zhang, Zhichao Xia, Yanjun Chi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-actions are subtle, low-intensity non-verbal behaviors that provide cues to fine-grained human states, including emotions and intentions. Recognizing them remains difficult because they are brief, contain weak visual changes, and often exhibit similar motion patterns across categories. This paper addresses these challenges with a fine-grained micro-action recognition method that combines full fine-tuning of InternVideo2.5, hierarchical soft fusion, and a lightweight candidate-label reranker. For the long-tailed label distribution in MA-52, we use class-balanced sampling and inverse-frequency reweighting to reduce the effect of frequent classes during training. We fine-tune InternVideo2.5 end to end and attach coarse and group-conditional fine-grained classification heads to the shared video representation, improving the consistency between coarse and fine predictions. For ambiguous samples, the candidate-label reranker uses hard samples and video-label matching to focus on easily confused fine-grained actions. Experiments validate the proposed method, which achieves a 79.99% F1-mean on MA-52 and ranks first in the 3rd Micro-Action Analysis Grand Challenge at ACM Multimedia 2026.

---


### 421. [ActionSplice: In-Flight Action Editing for Interactive World Models](https://arxiv.org/abs/2609.08230)

**<font color=#1a73e8>作者：</font>** Pardis Taghavi, Tingyu Guo, Jonas Lossner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chunk-autoregressive video world models typically condition each generated chunk on one action. An action received during sampling must therefore wait for the next chunk, condition future solver evaluations on a state produced under the previous action, or trigger rollback that repeats completed evaluations. We introduce ActionSplice, an inference framework that formulates this problem as Counterfactual State Transport (CST). A lightweight corrector transports the interrupted backbone-native representation toward the matched state induced by the revised action at the same solver step. The world model and sampler remain frozen, and sampling resumes without replaying completed evaluations. The retargeting variant $\mathrm{CST}*{R}$ updates the entire active chunk, while the temporal-splicing variant $\mathrm{CST}*{T}$ preserves a temporal prefix and updates only the suffix. Across minWM-Wan Action2V and HY-WM1.5, $\mathrm{CST}*{R}$ reduces rollback-relative LPIPS by 61.5% and 75.9% relative to direct condition swapping. $\mathrm{CST}*{T}$ reduces suffix LPIPS by 56.1% and 77.5%, respectively, while providing $2.73\times$ and $1.69\times$ pixel-ready speedups over waiting. Under the HY-WorldPlay protocol, $\mathrm{CST}_{R}$ obtains a PSNR of 25.66 dB, an SSIM of 0.6902, and an LPIPS of 0.1337 against the original rollout.

---


### 422. [CUNO: Curriculum and Preference Optimization for Stable Graph Unlearning under Mass Deletion](https://arxiv.org/abs/2609.08244)

**<font color=#1a73e8>作者：</font>** Chenhan Zhang, Ali Braytee, Madhushi Bandara 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph unlearning removes the influence of designated training data from a trained graph model without retraining from scratch. However, existing methods suffer a sharp drop in model utility under large deletion ratios (mass deletion), a phenomenon we refer to as catastrophic unlearning. We find that a key cause is the uniform treatment of all deleted samples, which is particularly damaging in graph learning: structural dependencies cause different nodes to play vastly different roles in the learned model, yet existing methods apply the same forgetting operation to the entire forget set. Based on this insight, we propose CUNO, a curriculum-based graph unlearning framework that removes the forget set progressively, ordering samples by their estimated unlearning difficulty across multiple stages. CUNO further employs a distribution-level negative preference optimization (NPO) objective at each curriculum stage that steers the model away from its original behavior on the current forget subset while preserving retained performance. Our theoretical analysis shows that the curriculum design is most beneficial when the forget set spans a wide range of unlearning difficulty, a condition naturally satisfied under mass deletion. Comprehensive experiments confirm that CUNO consistently mitigates catastrophic unlearning: at 20% deletion, it retains 74% of the original utility compared to 26-53% for existing methods, and maintains more than half the original utility even at 50% deletion. Our code is publicly available at this https URL.

---


### 423. [zScore-N: A Neural Network for On-Chain Wallet Reputation Scoring](https://arxiv.org/abs/2609.08247)

**<font color=#1a73e8>作者：</font>** Girish G N, Ashutosh Sahoo, Akshay SP 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wallet reputation scores decide who receives an airdrop, who can borrow, and who enters an allowlist across decentralised finance. They almost always begin as hand-written formulas: compositions of clamped logarithmic, linear and square-root transforms over behavioural features, with every threshold and point award set by hand. Such a formula is readable and deterministic, but it is piecewise and non-differentiable, it cannot improve as data accumulates, and it cannot distinguish a feature that is genuinely zero from one its pipeline failed to capture. We present zScore-N, the neural network that replaced ours in production. The formula served as its teacher: calibrated against 5,208,952 wallets sampled across 2019-2024 and verified to reproduce production output to within 2.3e-13, it supplies unlimited labelled training data at zero label noise. The trained network reproduces it to 0.58 points RMSE on the 1000-point scale (R^2 = 0.99997), against 2.25 for gradient-boosted trees and 28.04 for linear regression on identical features and splits. Trained with missing-value masks against uncorrupted targets, it halves the error that incomplete data introduces: at 10% feature-level missingness the formula drifts 51.4 points from its own complete-data output with a systematic -12.5 point bias, while the network drifts 17.9. The network carries the score at production scale, across a population of millions of wallets spanning six orders of magnitude in size and activity.

---


### 424. [Revisiting Spectral Representations in Generative Diffusion Models](https://arxiv.org/abs/2609.08253)

**<font color=#1a73e8>作者：</font>** Yuehao Wang, Peihao Wang, Hanwen Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have shown remarkable performance on diverse generation tasks. Recent work finds that imposing representation alignment on the hidden states of diffusion networks can both facilitate training convergence and enhance sampling quality, yet the mechanism driving this synergy remains insufficiently understood. In this paper, we investigate the connection between self-supervised spectral representation learning and diffusion generative models through a shared perspective on perturbation kernels. On the diffusion side, samples (e.g., images, videos) are produced by reversing a stochastic noise-injection process specified by Gaussian kernels; on the spectral representation side, spectral embeddings emerge from contrasting positive and negative relations induced by random perturbation kernels. Motivated by this, we propose a self-supervised spectral representation alignment method to facilitate diffusion model training. In addition, we clarify how joint spectral learning can benefit diffusion training from a geometric perspective. Furthermore, we find that the optimization of the spectral alignment objective is in an equivalent form of diffusion score distillation in the representation space. Building on these findings, we integrate a spectral regularizer into diffusion training objectives to improve the performance of diffusion models on multiple datasets. Experiments across images and 3D point clouds show consistent gains in generation quality. Code is released at this https URL.

---


### 425. [CircuTutor: Transforming Static Circuit Problems into Intelligent and Dynamic Tutoring](https://arxiv.org/abs/2609.08254)

**<font color=#1a73e8>作者：</font>** Ziyu Luo, Xiaorui Ma, Lin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning direct current circuit concepts requires learners to connect invisible physical quantities, such as current, voltage, resistance, and power, with observable outcomes such as bulb brightness. Conventional textbook materials and general-purpose circuit simulators provide opportunities for problem solving and exploration but offer limited support for explaining why circuit behavior changes or diagnosing the reasoning behind incorrect answers. We present CircuTutor, a circuit-state-driven intelligent tutoring system that transforms static textbook circuit problems into an interactive tutoring workflow. CircuTutor first uses multimodal problem parsing to extract the textbook question, circuit topology, component parameters, switch states, and answer options, which are converted into a structured task and validated through circuit simulation. Learners can then interactively explore the circuit (by changing parameters) and submit an answer while a SPICE-compatible solver computes physically consistent circuit states. After the learner submits an answer, CircuTutor presents a before-and-after circuit state animation corresponding to the selected operation, organizes the simulated state changes into a causal reasoning chain that explains the underlying circuit behavior, maps answer discrepancies to likely misconceptions, and generates adaptive follow-up exercises targeted at the diagnosed misconception. Our experimental results demonstrate that CircuTutor effectively improves conceptual learning and the overall learning experience. The proposed framework demonstrates how simulated circuit states can be transformed into intelligent and interactive tutoring for circuit education, with the potential to generalize to other STEM domains.

---


### 426. [Tracking-by-detection in Multi-object Tracking: Survey and Experiments](https://arxiv.org/abs/2609.08265)

**<font color=#1a73e8>作者：</font>** Yujin Yang, Kyujin Shim, Kangwook Ko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking (MOT) is an essential computer vision task that simultaneously tracks multiple objects in video sequences, with various applications in surveillance, autonomous navigation, and human-computer interaction. The tracking-by-detection (TBD) paradigm, which combines object detection with temporal association, has emerged as a leading approach, driven by innovative algorithms. Despite recent progress, fair evaluation of TBD-based methods remains a challenge. Many studies introduce modules such as similarity metrics, data association strategies, or motion models, but they are often evaluated under inconsistent protocols, with different baseline trackers, hyperparameters, and datasets. Such inconsistencies obscure the genuine contribution of each module and hinder objective comparison. This survey systematically reviews TBD-based MOT techniques, including similarity measurements, data association, camera motion compensation, and interpolation strategies. Starting from a minimal baseline tracker, we fairly evaluate the contributions of each method across diverse datasets and accumulate well-balanced methods. Our findings establish a strong baseline tracker and provide a foundation for the principled design of robust and versatile MOT systems suitable for real-world deployment.

---


### 427. [Synergistic Fusion of Topological Structure and Temporal Semantics of Mobility for Urban Region Embedding](https://arxiv.org/abs/2609.08268)

**<font color=#1a73e8>作者：</font>** Namwoo Kim, Jeeyun Chang, Kanghoon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban region embeddings have shown promising results in diverse urban sensing tasks such as crime, income, and service-call prediction. Recent methods improve representation quality by integrating mobility data with auxiliary modalities, using cross-view attention or contrastive objectives to align heterogeneous features into a unified region representation. However, leveraging the temporal dynamics of human mobility remains under-explored. Regional inflow and outflow fluctuate throughout the day, and inter-region connections emerge, persist, and dissolve over time. Moreover, prevailing fusion strategies combine views additively and miss the joint signal that emerges only when views co-occur. To address these gaps, we propose Mobility Stream-Structure Synergy (MoSS), which derives complementary views from mobility data: a Sequence view that preserves each region's hourly inflow/outflow profile, and a Structure view based on zigzag persistence diagrams that capture how regional connectivity emerges, persists, and dissolves over time. A synergy module then extracts emergent representations from the co-occurrence of these views through multi-degree interactions, explicitly capturing higher-order signal across views. Extensive experiments on New York City and Chicago show that MoSS achieves state-of-the-art performance across three downstream tasks using mobility data alone, outperforming baselines that rely on auxiliary modalities.

---


### 428. [Three Types of Negation of Triple and its Elements and an Extension of Triple](https://arxiv.org/abs/2609.08271)

**<font color=#1a73e8>作者：</font>** Zhenghua Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In various data models, the classical triple is a typical semantic data model. However, due to the design of the triple as a simple structure for representing positive assertions, it cannot sufficiently express different forms of negation present in the triple and its elements. This paper conceptually proposes that there are three distinct forms of negation within triples and their elements: contradictory negation, opposite negation and intermediary negation. Based on the the set SCOI and the logic LCOI+PLCOI with three kinds of negation, we propose an extension of triple that can distinguish and express these three different negations in the triple and its elements, called the TCOI triple with contradictory negation, opposite negation and intermediary negation. The TCOI triple is a semantic and structural extension of the classical triple. While retaining the ability to express positive assertions, it systematically introduces the three semantic dimensions of three negations, allowing these negations to independently act on the elements of the triple and on the whole triple. This significantly enhances the triple model capability to represent and reasoning about complex negative information. This paper also explores the expressive power and reasoning of the TCOI triple, as well as the application of TCOI triple implication reasoning in counterfactuals and counterfactual reasoning. We propose a truth-value (continuous value) algorithm for TCOI triple implication reasoning and perform its calculation through an example of the counterfactuals and counterfactual reasoning.

---


### 429. [Beyond Coherence: Benchmarking Professional Editing-Technique Execution in Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2609.08275)

**<font color=#1a73e8>作者：</font>** Tianyi Zeng, Junchao Liao, Yujie Wei 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent multi-shot audio-video generators can produce increasingly coherent and cinematic outputs, but coherence does not imply the ability to execute editing techniques. Professional editing depends on shot structure, transition grammar, audio-video cut relations, and montage, yet existing benchmarks largely rely on proxies such as content quality, synchronization, or physical plausibility, systematically missing whether such editing instructions are actually executed. We introduce CutCraft, the first benchmark for editing-technique execution in multi-shot audio-video generation. CutCraft extends structured multi-shot prompts with explicit editing specifications and is paired with a hierarchical hybrid evaluation framework that combines shot-structure alignment, expert-model metrics, tool-grounded multimodal judgment, and rubric-based question answering. Beyond evaluation, we design an agentic editing baseline that decomposes generation into planning, shot-level synthesis, and post-hoc composition, explicitly realizing editing semantics such as J-cuts, L-cuts, and transition timing. Across 13 state-of-the-art closed- and open-source models, CutCraft reveals a consistent gap between coherence and editing-technique execution: current systems often produce plausible multi-shot videos yet fail to execute editorial instructions reliably. We find unstable shot structures, weak control of transition execution, and sharp degradation on higher-order montage, while aesthetic quality is only weakly correlated with editing-technique compliance. The benchmark and metrics, and the editing agent baseline are available at this https URL.

---


### 430. [Online Signature Verification Using Augmented Path Signature and T-Mamba](https://arxiv.org/abs/2609.08276)

**<font color=#1a73e8>作者：</font>** Ruiling Li, Danyu Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Handwritten signature verification is vital for personal authentication across commercial and financial applications. Although deep learning methods are widely adopted for online signature verification (OSV), they often struggle with capturing highly discriminative features and modelling long-range dependencies. To address these issues, we propose a novel framework that integrates the augmented path signature (APS) descriptor with the T-Mamba model. The APS descriptor first applies time and basepoint augmentations, then computes sliding-window path signatures. The path signature is a non-parametric feature map from rough path theory that effectively captures geometric structures and nonlinear inter-channel interactions. Inspired by the efficacy of state space models (SSMs) in sequence modelling, our T-Mamba model employs a hybrid design combining two temporal convolutional network (TCN) blocks with a time-scanning Mamba. This design enables the model to learn both local temporal patterns and global long-range dependencies, substantially improving verification accuracy. Our framework achieves state-of-the-art EERs on three public benchmark datasets (MCYT-100, SVC-2004 Task 2, DeepSignDB), validating its effectiveness and robustness, especially when the training data is limited. Our code is publicly available at this https URL.

---


### 431. [Adaptively Incorporating Directional Hints into Zeroth-Order Optimization](https://arxiv.org/abs/2609.08277)

**<font color=#1a73e8>作者：</font>** Alexander Ryabchenko, Jian Qian, Wenlong Mou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study zeroth-order optimization of non-convex functions with the aid of directional hints, which are cheap but potentially inaccurate approximations of the true gradient direction, given by linear subspaces at each iteration. To leverage these hints adaptively while maintaining robustness to their quality, we introduce Control-Variate Zeroth-Order Descent (CV-ZOD), a new framework that refines the classical zeroth-order gradient estimator with a control variate that can be set based on the directional hints. We first show that the oracle algorithm that optimally sets the reference vector and step size at each iteration achieves a convergence rate that interpolates between the first-order $O(1/T)$ rate and the zeroth-order $O(d/T)$ rate, depending on the quality of the hints along the trajectory. We then develop a practical variant of CV-ZOD that achieves the same oracle guarantee up to logarithmic factors, without any prior knowledge of the hint quality. We validate the method empirically on simulation-based scientific optimization tasks, demonstrating sustained progress on non-convex landscapes where zeroth-order descent is slower and existing guided methods stall as guidance deteriorates.

---


### 432. [SAM3-O2D2: Zero-Shot Object Out-of-Distribution Detection by Object Class Prompting of the SAM3-Image Model](https://arxiv.org/abs/2609.08281)

**<font color=#1a73e8>作者：</font>** Lucas Görnhardt, Timo Bartels, Tim Fingscheidt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detectors have shown remarkable performance in various fields, among these medical imaging, surveillance, and autonomous driving. However, they are prone to overconfidence when encountering unseen objects in real-world deployments, causing potential safety issues. To address this, detecting out-of-distribution (OOD) objects is essential for reliable object detection. Modern approaches leverage the broad semantic knowledge of foundation models such as CLIP for post-hoc few- and zero-shot OOD detection. However, these methods typically perform OOD assessment in feature space, which can be sensitive to object detector localization errors and variations in object appearance. Moreover, the current state-of-the-art (SOTA) zero-shot method performs computationally costly diffusion in inference. In this work, for our proposed zero-shot object OOD detection method SAM3-O2D2, we employ the SAM3-image foundation model in an efficient manner. Specifically, we prompt SAM3 only with the object detector's predicted classes and compare the predictions of the object detector and SAM3. An object is in-distribution (ID), if SAM3 also detects an object at the corresponding location. If SAM3 does not detect the prompted object, this indicates a mismatch between the detector's prediction and the image content, suggesting that the object is OOD. Experimental results show that our method significantly surpasses the so-far zero-shot SOTA method. Specifically, we achieve new SOTA AuROC and FPR95 metrics over both ID datasets Pascal-VOC and BDD100K and both OOD datasets MS-COCO and OpenImages.

---


### 433. [Dreaming in Flow: Generative Grounding Feedback for Self-Evolving Unified Multimodal Models](https://arxiv.org/abs/2609.08282)

**<font color=#1a73e8>作者：</font>** Ke Hao, Yuanzhi Liang, Tingxi Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models integrate visual understanding and generation within a single network, yet the two capabilities are commonly optimized as separate tasks. We introduce Generative Grounding Feedback(GGF), a self-evolving post-training framework that uses only text prompts and the model's own visual experience. Given a prompt, the model first generates a visual ``dream.'' Flow-level feedback compares text-, image-, and repair-conditioned predictions at the same noisy latent state, transferring image-grounded generation directions to the prompt condition. Dream replay grounding replays this dream through captioning and re-imagination, training claim-level evidence to remain consistent across the replay while separating unrelated visual experiences. Jointly optimized, these two directions let generation provide visual grounding for understanding and understanding refine subsequent generation without paired image--text supervision. Experiments across unified models with different understanding--generation integration designs show consistent improvements in text-to-image generation together with modest gains in visual understanding.

---


### 434. [MARS-CLIP: Multi-Resolution and Attention Refined Zero-Shot Image Segmentation](https://arxiv.org/abs/2609.08283)

**<font color=#1a73e8>作者：</font>** Nagito Saito, Shintaro Ito, Koichi Ito 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive Language-Image Pre-training (CLIP) has demonstrated impressive capabilities in zero-shot transfer but often struggles with dense prediction tasks due to low spatial resolution and the loss of structural information. To address these limitations, we propose MARS-CLIP (Multi-resolution and Attention Refined Segmentation for CLIP), a novel framework for zero-shot semantic segmentation. Our approach introduces two key strategies: (i) a multi-resolution feature extraction module that fuses local fine-grained features with global context to overcome input resolution constraints, and (ii) an attention refinement mechanism that injects spatial and color biases from intermediate layers into the final self-attention block to accurately restore object boundaries. A set of experiments on six public datasets demonstrates that MARS-CLIP significantly outperforms state-of-the-art methods.

---


### 435. [HypLTSF: A Hyperbolic Geometric View of Multi-Scale Hierarchies for Long-Term Time Series Forecasting](https://arxiv.org/abs/2609.08286)

**<font color=#1a73e8>作者：</font>** Namwoo Kim, Hyungryul Baik, Yoonjin Yoon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-scale modeling has become an effective approach for long-term time series forecasting, capturing temporal patterns that range from fine-grained local dynamics to coarse global trends. Representations across these temporal scales are inherently hierarchical, with coarser scales abstracting and aggregating information from finer ones. While existing approaches readily exchange information across these scales, the hierarchy itself is typically left as an emergent byproduct of such interactions rather than captured as a geometric structure in its own right. In this paper, we introduce HypLTSF, a framework that endows the multi-scale hierarchy with a concrete geometric form by embedding scale-wise representations into the Poincaré ball, whose exponentially expanding volume naturally accommodates hierarchical structures. To align this geometry with the temporal hierarchy, HypLTSF imposes two constraints: (1) a radial constraint that orders embeddings by their level of abstraction, and (2) an angular constraint that groups fine-scale patterns sharing a common coarser-scale ancestor. Extensive experiments on long-term time series forecasting benchmarks show that HypLTSF achieves state-of-the-art performance, suggesting that explicitly modeling the multi-scale hierarchy as a geometric structure is effective for forecasting.

---


### 436. [TRIUNE-Net: Harmonizing Scale, Shape, and Efficiency in Pancreatic Tumor Segmentation](https://arxiv.org/abs/2609.08303)

**<font color=#1a73e8>作者：</font>** Amir Hossein Saleknia, Alireza Kheyrkhah, Sanaz Karimijafarbigloo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pancreatic tumor segmentation in 3D CT volumes is challenged by extreme scale variability across both the pancreas and tumor, and highly irregular tumor morphology. While recent advances have pushed segmentation performance, existing methods do not explicitly address these challenges and come at the cost of excessive computational complexity, limiting their practicality in resource-constrained clinical environments. We propose TRIUNE-Net, a lightweight unified architecture that harmonizes scale, shape, and efficiency through three synergistic innovations. A multi-scale context aggregation module with stage-adaptive dilated convolutions enables the model to reason across the broad range of anatomical scales present in both organs. A serial linear-deformable attention mechanism combines large effective receptive fields with shapeadaptive deformable convolutions to capture irregular, non-convex tumor morphologies. Finally, an information-preserving downsampling module replaces conventional max pooling entirely, retaining all spatial information while adding negligible parameters, preventing small tumors from being discarded before they can be recognized. On both the MSD Pancreas and NVD Pancreas datasets, TRIUNE-Net achieves state-of-theart results with only 5.86 M parameters and no external pre-training, outperforming all baselines across all key tumor metrics. Specifically, it surpasses the next-best model by 0.45% in tumor Dice, 6.0 points in F1 score, 6.6 points in sensitivity, and 3.4 points in precision, simultaneously reflecting its ability to suppress both missed tumors and false alarms in clinically realistic conditions. Our code is available at: this https URL

---


### 437. [FPicker: Topology-Guided Evolution for Filament Tracing in Low-SNR Microscopy](https://arxiv.org/abs/2609.08305)

**<font color=#1a73e8>作者：</font>** Tingyin Zhao, Mingtao Huang, Yuan Shen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automating filament tracing in Cryo-Electron Microscopy (Cryo-EM) is essential for 3D helical reconstruction but challenged by intersecting topologies and extremely low Signal-to-Noise Ratios ($\text{SNR} = \sigma_s^2/\sigma_n^2$ < 0.1 or -10 dB). Existing paradigms fail: pixel-wise segmenters suffer from severe topological fracturing, box-based detectors face ghost center drift, sequential trackers derail due to error accumulation, and traditional active contours collapse under artificial closed-curve constraints. To resolve these bottlenecks, we present FPicker, the first topology-guided framework reconciling these incompatibilities. It unifies perception via a center-endpoint representation and an open-curve evolution module to explicitly model non-cyclic connectivity. On simulated benchmarks, FPicker outperforms top baselines by over $40\%$ relative gain in mean spatio-angular precision (mSAP) and reduces topological gap rates by over $60\%$ under extreme noise ($-20\text{ dB}$). By learning intrinsic physical geometry rather than local texture, FPicker demonstrates strong potential as a resilient geometric backbone. Its zero-shot performance on the real-world EMPIAR dataset exhibits robust topological resistance, achieving a state-of-the-art 82.9\% mSAP upon fine-tuning. Our results also suggest modeling physical priors is a highly robust path toward bridging the sim-to-real gap in signal-starved scientific imaging. The code is publicly available at: this https URL.

---


### 438. [StitchOver: Technical Embroidery on Seamed Fabrics](https://arxiv.org/abs/2609.08311)

**<font color=#1a73e8>作者：</font>** Zekun Chang, Tianhong Catherine Yu, Yixuan Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Smart textiles embed interactivity into everyday garments, supporting use cases like always-available sensing for medical applications or sports. Machine embroidery allows integrating functionalities into existing textiles. However, embroidering onto real-world textile goods remains challenging. Textile goods are rarely made of a single homogeneous substrate of fabric, and embroidery with functional materials such as conductive threads requires machines to be more tightly calibrated than for decorative embroidery. In particular, seams, which bring together different substrates, along with machine variability, cause shifts in tension and friction between the functional thread and the textile substrate that frequently lead to defects (70% of samples in our evaluation).
We present a technique to reliably embroider on seamed fabric even when using functional threads. Our software tool automatically digitizes user-defined stitch patterns by introducing what we call "JumpStitches" to bypass seam interference.
We evaluated our approach under varying machine states (under-tensioned, well-calibrated, and over-tensioned), and across multiple seam and pattern configurations. Our results show that the JumpStitch mechanism eliminates defects, while maintaining conductivity compared to 70% defects without JumpStitches, and even in poorly calibrated machine states continues to work well.

---


### 439. [Supervised Cross-Modal Feature Alignment for Zero-Wearable Freezing of Gait Detection in Parkinsonism](https://arxiv.org/abs/2609.08317)

**<font color=#1a73e8>作者：</font>** Aryan Singh, Chandan Biswas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective assessment of Freezing of Gait (FoG) in Parkinson's disease (PD) relies predominantly on wearable Inertial Measurement Units (IMUs). While IMUs provide optimal kinematic precision, mandatory sensor attachment restricts continuous clinical deployment. Conversely, unobtrusive vision-based alternatives suffer substantial classification errors during turning-in-place tasks, where geometric self-occlusion degrades deterministic skeletal coordinates and obscures the high-frequency precursors required for FoG detection. To resolve these physical observation limits, we propose a supervised cross-modal subspace distillation framework. During optimisation, pre-trained kinematic data from IMU sensors and contextual clinical metadata act as oracles to guide a deployable visual architecture. By incorporating joint velocity and acceleration derivatives, utilising a confidence-based gating mechanism, the visual model mitigates some of the tracking errors during occlusion events. Empirical evaluations confirm this latent alignment transfers the predictive fidelity of hardware sensors directly into the visual representation, yielding $85.5\%$ accuracy, and $82.4\%$ balanced accuracy. All the while maintaining a vision only model at inference.

---


### 440. [EMBLEM: Enhancing Multi-script Table Detection through Masking](https://arxiv.org/abs/2609.08330)

**<font color=#1a73e8>作者：</font>** Dhruv Kudale, Udhay Brahmi, Ganesh Ramakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Table detection is a core task in document analysis, supporting downstream applications such as information retrieval, document reconstruction, and visual question answering. While existing deep learning models perform well on English and Chinese documents, they struggle with multilingual, multi-script documents due to script diversity and the limited availability of labeled data. To address this challenge, we introduce MANDALA (Multi-script Annotated Documents for Table Detection), a manually curated dataset of 2,323 table-containing pages spanning 18 languages and 15 scripts across diverse domains. We also propose EMBLEM, a masking-based paradigm for Multi-script Table Detection (MTD). EMBLEM generates masked images that conceal script- and font-specific details, enabling models pre-trained on abundant English documents to focus on script-agnostic page layout. Experiments across three table detection architectures show that EMBLEM consistently outperforms strong baselines on MANDALA while remaining competitive on five standard English-dominant benchmarks. Using only English masked images for fine-tuning, with no multi-script training data, EMBLEM achieves an absolute F1-score gain of 20.8% on MANDALA. We release MANDALA along with the accompanying code and models at this https URL.

---


### 441. [EdMCGS: Event-Driven Markov Chain Gaussian Splatting for Extreme-Low-Frame-Rate Dynamic Scene Reconstruction](https://arxiv.org/abs/2609.08332)

**<font color=#1a73e8>作者：</font>** Yuzhong Wang, Wenmin Wang, Xinxing Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present EdMCGS (Event-driven Markov chain Gaussian Splatting), an end-to-end method for reconstructing dynamic 3D scenes from extreme-low-frame-rate RGB together with an event stream, which can then be rendered at any intermediate timestamp. Methods relying solely on RGB images generate numerous artifacts due to the lack of evidence from between consecutive frames. To supply this missing evidence, we model the scene motion as an event-driven Markov chain, in which the sparse RGB frames anchor the state at their own timestamps while the events recorded within an interval drive the transition across it. Since the transition reads the events of the current interval, it remains active at inference and produces the in-between motion of the 3D Gaussians directly from the events rather than by interpolation, which sets our method apart from prior work that uses events only as training-time supervision. The state is carried by a compact set of control points, each driven by the events sampled in the neighborhood of its own image projection, and a temporal local isometry term keeps the propagated motion locally rigid. Experiments on synthetic and real-world scenes show that EdMCGS outperforms both RGB-based and event-based baselines, while rendering in real time with far fewer Gaussians than the strongest event-based baseline. We release our source code and a new dataset at this https URL.

---


### 442. [Segment Any Motion with Radar: Robust Multimodal Moving-Object Segmentation and Tracking](https://arxiv.org/abs/2609.08346)

**<font color=#1a73e8>作者：</font>** Jue Wang, Xuan Wang, Hao Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Moving-object perception must decide which image regions correspond to real motion and keep every instance identified over time. Methods that read motion from appearance, optical flow, or estimated trajectories lose that evidence under poor illumination, adverse weather, reflections, and occlusion. Radar is a natural remedy because it measures radial velocity directly instead of inferring it from photometric correspondence. However, existing benchmarks do not jointly provide radar measurements, dense moving-instance masks, and temporally consistent identities for surveillance. We therefore introduce RGBTR-Motion, a synchronized and calibrated fixed-camera benchmark that pairs RGB, thermal, and radar streams with dense instance masks and temporally consistent identities across diverse surveillance scenes. We also develop SAM-Radar, an RGB, thermal, and radar-based segmentation and tracking framework built on SAM 3. SAM-Radar's radar-aware detector fuses calibrated RGBT features with radar returns that are grounded at their projected image locations, and motion supervision, implemented as foreground classification of those projected returns, teaches the detector to reject clutter without any text prompt. The tracker associates accepted radar returns with individual trajectories and uses them as physical evidence that a visually degraded target remains present. This allows it to bridge short periods of low visibility or occlusion and reconnect a reappearing target to its existing identity instead of starting a new track. SAM-Radar attains 0.7027 IoU and 0.8090 F1-50, and raises MOTA, HOTA, and IDF1 by 0.2977, 0.1603, and 0.2857 over the strongest competing values.

---


### 443. [Geometry-Aware Bayesian Parameter-Efficient Fine-Tuning on the Stiefel Manifold via Stein Variational Gradient Descent](https://arxiv.org/abs/2609.08354)

**<font color=#1a73e8>作者：</font>** Quang-Duy Tran, Trung Le, Bao Duong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Several geometry-aware approaches to low-rank adaptation have emerged for parameter-efficient fine-tuning of large pre-trained models. These methods aim to take full advantage of the geometric structure of low-rank manifolds for improving the efficiency in subspace utilization and reducing redundancy by enforcing orthogonality constraints during optimization. The strong empirical results of these techniques have motivated further study into whether predictions from such geometry-based adaptation methods could be overconfident. In this paper, we build on the singular value decomposition factorization of adapters to develop a framework based on Stein variational gradient descent (SVGD). In this formulation, the low-rank matrices are transported along the Stiefel manifold to match the targeted distributions while retaining their crucial geometric structure. Since this geometry-aware SVGD approach provides multiple solutions during inference, it supports uncertainty quantification and produces better-calibrated adapters on the Stiefel manifold. Extensive experiments show that our method delivers strong model calibration and attains higher prediction accuracy than SVGD and related uncertainty estimation methods that are formulated in Euclidean space.

---


### 444. [Rank Without an Oracle: Deviation-Aware Interaction-Rank Selection from Offline Multi-Agent Logs](https://arxiv.org/abs/2609.08358)

**<font color=#1a73e8>作者：</font>** Xiangwu Wang, Chengwei Cao, Hongyuan Tang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Offline multi-agent payoff models are estimated under a logging distribution but used on distributions induced by learned solutions and unilateral deviations. Standard held-out loss can therefore favor an interaction class that predicts logged play well while distorting strategic incentives. We introduce Selective Interaction-Rank Validation (SIRV) for finite games with known logging distributions. A training split fits nested payoff models and constructs a common union of all candidate deployment and unilateral-replacement distributions; an independent calibration split evaluates every candidate on this same union. SIRV returns the smallest rank whose simultaneous upper worst-target risk is within tolerance of the best upper score, and abstains when a declared target is unsupported or too imprecisely estimated. A common coverage event yields a finite-candidate target-risk bound and a candidate-specific coarse correlated equilibrium (CCE) gap certificate. We also isolate an exact two-point off-support non-identifiability result. In a controlled factorial study with 2,048 independent games per family, empirical-Bernstein bounds reduce the median CCE-gap certificate by 42.5% relative to Hoeffding bounds on common returns, with a 1.36-point reduction in supported return. Under paired rank misspecification and in a separately generated congestion family, the SIRV-EB fallback rule lowers mean true candidate-selection CCE regret relative to ID-Mean, while retaining game-level losses. Across 384 games at $N=3,5,8$, ID-Mean-relative mean CCE-regret effects stay positive while certified return falls sharply under weak coverage. These results separate certifiable model selection from universal strategic improvement.

---


### 445. [Reachability-Certified Subteam Decomposition for Locally Interacting Multi-Agent MDPs](https://arxiv.org/abs/2609.08366)

**<font color=#1a73e8>作者：</font>** Xiangwu Wang, Chengwei Cao, Hongyuan Tang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Persistent communication limits force a multi-agent system to decide which agents may coordinate throughout a rollout. Current proximity alone is insufficient: separated agents may interact later, whereas a large pair reward may remain unreachable until it is heavily discounted. We introduce Reachability-Certified Subteam Decomposition (RCSD) for finite multi-agent Markov decision processes with factorized physical dynamics, finite-range ordered pair rewards, and almost-sure motion bounds. RCSD combines a speed-limit lower bound on pairwise contact time with a reward envelope to form a current-state affinity. For any capacity-valid persistent partition, the sum of cut affinities bounds the reward-deletion error of every unchanged stationary Markov state-feedback policy. A product of team-optimal policies for the resulting cut MDP incurs at most twice this certificate in regret against the centralized optimum. Both bounds are worst-case tight. On a controlled five-agent family, RCSD-Exact reduces aggregate normalized execution regret by 56.0%, 28.8%, and 25.3% relative to uniform, distance-only, and envelope-only partitions. A separate stochastic two-dimensional study finds no bound violation over 384 exact-partition and 1,440 restricted-controller evaluations. Exact four-agent evidence favors RCSD over uniform and distance-only grouping; raw evidence for current contact is borderline and envelope-only is unresolved. Across balanced 8-20-agent strata, controller-library utility is mixed: pointwise paired intervals favor RCSD over distance and current contact, include zero for uniform, and favor envelope-only and Value-MIP over RCSD. Partition construction remains subsecond in median up to 100 agents; this last result does not include affinity formation or MDP planning.

---


### 446. [Geographically Regularized AUC-Maximizing Personalized Federated Learning](https://arxiv.org/abs/2609.08379)

**<font color=#1a73e8>作者：</font>** Mayu Hiraishi, Kensuke Tanioka, Toshio Shimokawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate diagnostic and risk-prediction models are important for supporting clinical decision-making during infectious disease outbreaks. However, privacy and governance requirements may restrict patient-level data sharing across healthcare institutions, and data distributions often vary. Moreover, AUC is widely used to evaluate discriminative performance, motivating its direct optimization in model development. We propose geographically regularized AUC-maximizing personalized federated learning (GrAUC-PFL), which directly optimizes a smooth pairwise AUC surrogate to learn personalized models while keeping patient-level data local and accounting for institutional heterogeneity. Graph-based regularization encourages geographically neighboring institutions to have similar coefficient vectors while retaining a personalized models. Simulations and a real-data application suggest improved discriminative performance, particularly when geographically neighboring institutions have similar data-generating characteristics.

---


### 447. [Equivariance Breaks the Learning Rate](https://arxiv.org/abs/2609.08381)

**<font color=#1a73e8>作者：</font>** Andrei Manolache, Mathias Niepert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant networks are commonly trained with Adam, yet recent work reports that matrix-structured optimizers such as Muon can perform better on these architectures without explaining why. We identify one source of this difference inside equivariant linear layers. Each irrep block learns a channel-mixing matrix $W_l$ shared across its $2l+1$ components, giving the expanded map $W_l \otimes I_{2l+1}$. For a single application of the layer, the gradient of $W_l$ sums $2l+1$ outer product contributions and has rank at most $2l+1$. Adam rescales stored weights individually without using the irrep boundaries, so one learning rate can produce different spectral step sizes across blocks within a layer. We address this mismatch by normalizing each block update separately, without introducing a new hyperparameter. This changes only the scale of the update, leaving Adam's moment estimates and its direction within each block unchanged. We evaluate the mechanism in a controlled $\mathrm{SO}(3)$-equivariant model with a matched dense control and in an e3nn interatomic potential model trained on rMD17 and MD22. The toy setup isolates a mismatch that grows with width while the dense control shows no corresponding growth. In the interatomic potential model, block normalization and tuning Adam's momentum coefficients independently improve performance, but neither alone matches Muon. Combined, they make Adam competitive with Muon on all datasets, indicating that blockwise step control and momentum accumulation account for much of Muon's advantage.

---


### 448. [GALoc: Gravity Aligned Wireframes for Depth-Free Monocular Floorplan Localization](https://arxiv.org/abs/2609.08385)

**<font color=#1a73e8>作者：</font>** Jeahn Han, Minji Kim, Jeongbin Sohn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Floorplans are compact, appearance-invariant maps ideal for indoor localization, yet existing methods rely on depth networks that are brittle in cluttered scenes. We propose GALoc, a geometry-first framework that replaces depth prediction with gravity-aligned wireframes that satisfy verticality and coplanarity by construction. Given monocular RGB, camera intrinsics, relative poses, and IMU orientation, GALoc constructs a linear constraint matrix encoding verticality and coplanarity, and finds the camera gauge minimizing its smallest singular value via global search. The rectified wireframes are projected into bird's-eye-view layouts through a closed-form, FOV-consistent transformation and matched against the floorplan via metric-free SE(2) search. We evaluate end-to-end on Structured3D, with calibrated noise on Gibson, and on real-world author-collected sequences. When sufficient wall geometry is visible, GALoc matches or outperforms depth-based baselines -- achieving 88% sequential localization success at 0.1m over 100-step sequences on Gibson vs the baseline's 68% -- while abstaining in structure-blind scenes.

---


### 449. ["Here Be Sharks!": Enhancing Scientific Communication and Analysis through Authoring Interactivity](https://arxiv.org/abs/2609.08386)

**<font color=#1a73e8>作者：</font>** Caroline Berger, Josh Pollock, Dylan Wooton 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We report on a case study for designing authoring environments for interactive visualizations to enhance scientific work. We conducted a workshop and prototype review with a group of marine biologists. When it came to visualizing their data, participants identified challenges in conveying their research accurately and completely as well as and analyzing it with ease. Based on our findings, authoring environments should consider the context of scientific work aspects such as domain expertise, collaboration culture, and publication traditions. We propose consideration of non-traditional programming languages and environments for scientific work, discuss ways of facilitating interactive visualizations for scientists, and examine ways of meaningfully integrating AI. The critiques, artifacts, and reactions from the scientists along with our analysis and discussion inform how computational tools should be designed for scientific work.

---


### 450. [Windows Malware Detector as a Compound AI System: Trade-Offs in Accuracy, Efficiency, and Adversarial Robustness](https://arxiv.org/abs/2609.08394)

**<font color=#1a73e8>作者：</font>** Andrea Ponte, Luca Demetrio, Luca Oneto 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Industrial Windows malware detectors are commonly described as Compound AI Systems composed of multiple heterogeneous components, including rule-based mechanisms as well as machine-learning-based static and dynamic analyses. However, due to industrial secrecy and limited public disclosure, the internal architectures of these systems can only be inferred, rendering systematic evaluations of detection accuracy, computational costs, and adversarial robustness largely infeasible. In contrast, academic research provides reproducible and transparent evaluation methodologies, but typically investigates individual detection components in isolation. To bridge the gap between academic research and industrial practice, and inspired by state-of-the-art industrial architectures for Windows malware detection, we propose a novel methodology that (i) explicitly balances the trade-off among detection performance, computational requirements, and robustness, and introduces (ii) system-level threat models that capture how attackers exploit different degrees of knowledge to evade the entire Compound AI System rather than isolated detectors. Experiments conducted on real-world data demonstrate that the Compound AI System training time can be reduced and responsiveness improved while incurring only a marginal loss in detection performance. Leveraging our threat modeling, we show that increasingly knowledgeable attackers craft more effective adversarial examples, revealing the system's strengths and weaknesses, degrading its responsiveness, and exposing a direct trade-off between efficiency and robustness. Finally, we translate these trade-offs into take-home messages and deployment guidelines, helping practitioners to select the system that best matches their operational constraints.

---


> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-542](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
