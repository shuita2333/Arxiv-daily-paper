# 📦 其他研究 | 2026年10月12日

> 本类共 **329** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-329](./part-07.md)

---

### 51. [Adaptive Multi-Discriminator WGAN Framework for Resource-Constrained Internet of Vehicles Using Reinforcement Learning and Game Theory](https://arxiv.org/abs/2610.10926)

**<font color=#1a73e8>作者：</font>** Farhoud Jafari Kaleibar, Amr M. Zaki, Marin Litoiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Managing machine learning workloads as a network service introduces a resource-orchestration problem distinct from conventional model training; which nodes should be allocated to a task, how communication and computation budgets should be divided among them, and how service quality should be sustained as connectivity and node availability change with mobility. Deploying Generative Adversarial Networks (GANs) in Internet of Vehicles (IoV) environments is a demanding instance of this problem; resource constraints, dynamic network topologies, and competing optimization objectives mean that traditional GAN architectures cannot simultaneously achieve high accuracy, efficient resource use, low delay, and low communication overhead. This paper introduces an adaptive multi-discriminator Wasserstein GAN (MD-WGAN) framework that integrates reinforcement learning with game-theoretic coordination to address these challenges jointly. In our framework, roadside units host generators paired with Deep Q-Network (DQN) agents that select discriminator subsets and manage distributed training across mobile vehicular nodes, while a game-theoretic coordination step allocates training epochs between generators and discriminators. A unified optimization objective ties adversarial learning quality to resource efficiency, communication overhead, and latency under vehicular constraints, allowing the framework to continuously adapt its training behavior as network conditions change. Evaluation on real-world NGSIM trajectory data shows that the framework attains prediction accuracy comparable to state-of-the-art GAN baselines - the lowest RMSE (1.029) and MAE (0.894) among all evaluated methods - while markedly improving resource efficiency: average CPU utilization is reduced by roughly 28% and mean memory usage by roughly 6%, at competitive communication overhead and latency.

---


### 52. [Coefficient Calibration as Selection Pressure in Symbolic Regression](https://arxiv.org/abs/2610.10931)

**<font color=#1a73e8>作者：</font>** Mattia Billa, Veronica Guidetti, Federica Mandreoli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In memetic symbolic regression, candidate structures are compared after coefficient calibration, so the calibration protocol itself contributes to evolutionary selection. Standard centralized calibration evaluates each structure at its pooled-sample optimum, ignoring how stable this calibration is under covariate shifts, and can thus favor structures whose fit relies on sample-specific coefficients.
We propose Dirichlet-Sinkhorn Constant Averaging (DSCA), a calibration strategy that partitions the optimization data into equally sized subsets with different covariate distributions, calibrates each candidate independently on every partition, and evaluates it at the mean of the resulting parameters. We show that the excess loss of DSCA relative to centralized calibration vanishes at the population level for correctly specified, identifiable expressions, whereas under misspecification it persists when partition-specific calibrations do not aggregate to the pooled optimum.
On synthetic benchmarks and ten real-world datasets, DSCA improves functional recovery and the accuracy-complexity trade-off over centralized Broyden-Fletcher-Goldfarb-Shanno and Levenberg-Marquardt calibration, under selection by negative log-likelihood and by the Akaike and Bayesian information criteria. Mechanism analyses associate the DSCA excess loss with the generalization gap and show that the effect is not reproduced by repeated centralized fitting. These results indicate that controlled heterogeneous calibration provides a complementary source of selection pressure in symbolic-regression search.

---


### 53. [World-Model Policy Arbiter for Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2610.10932)

**<font color=#1a73e8>作者：</font>** Junwei Quan, Evgenii Opryshko, Nicholas Rhinehart 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline goal-conditioned reinforcement learning (GCRL) has produced a diverse set of goal-reaching algorithms, yet no single algorithm performs best across environments, goals, and even different phases of the same task. Rather than deploying only the best-performing policy, we ask whether a set of frozen goal-conditioned policies can be used collectively as a portfolio, deciding at every state which policy should act. Choosing a policy at each state is not straightforward. The policies' own value functions cannot be compared directly: they may use different scales, and some policies have no value function. We need to judge each policy by the states it is likely to reach, even though we can execute only one policy at a time. We also need to avoid switching so often that control becomes unstable. To address these challenges, we introduce World-Model Policy Arbiter (WMPA), a test-time framework that, given a set of frozen policies as input, rolls out each frozen policy in a learned state-space world model, evaluates the imagined futures with a shared goal-conditioned value function, and executes the highest-scoring policy for a short commitment interval before the next round of arbitration (policy selection). WMPA assumes access to a bank of frozen goal-conditioned policies and requires neither policy retraining nor privileged task-specific knowledge. Under the official OGBench evaluation protocol on 18 state-based datasets spanning maze navigation as well as cube, scene, and puzzle manipulation, WMPA improves the macro-average success rate from the 44% achieved by the best policy selected per dataset to 58%, with statistically significant gains on 12 datasets. These gains include +33 percentage points on cube-double-play and +36 percentage points on scene-play.

---


### 54. [GHARP: Real-time Gaussian Head Animation from Large-scale Reconstruction Prior](https://arxiv.org/abs/2610.10945)

**<font color=#1a73e8>作者：</font>** Ali Benlalah, Sepehr Johari, Patricia Vitoria 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present GHARP (Real-time Gaussian Head Animation from Large-scale Reconstruction Prior), a method that animates 3D human heads in real time from a few input images of a subject and a driving expression signal. We decouple the problem into an identity stage that builds a representation of the subject's geometry and appearance offline, and an animation stage that predicts expression-dependent residuals on top of it at runtime. This separation offers a favorable trade-off with respect to fidelity, quality and runtime: the identity stage can be expensive while the animation stage runs a lightweight network, optimized for mobile devices. Our method performs animation in a semantically structured latent space of a pretrained reconstruction model, where expression changes remain spatially contained, making residual prediction efficient. This reconstruction prior provides a consistent spatial layout, allowing fusion of multiple input views into a compact, fixed-size canonical Gaussian representation. While this two-stage design improves the runtime-quality trade-off, it still inherits a problem common to all expression-driven avatar methods: expression codes describe only the face and thus omit body pose and clothing position, making these regions underspecified in the input. The animation network faces an ill-posed mapping and resorts to averaging over conflicting body appearances, producing blur and temporal flicker. We address this with a body alignment network that learns to align the person's body in the target image with the input reference images, removing the ambiguity from the training signal. Our method achieves state-of-the-art quality on the Ava-256 benchmark while running up to 13x faster on an A100 GPU with 8x fewer Gaussians.

---


### 55. [SPD-MetaFormer is what you need for small-data brain decoding](https://arxiv.org/abs/2610.10952)

**<font color=#1a73e8>作者：</font>** Zhida Wang, Wei Lyu, Guo Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain signal decoding is challenging because neural recordings are noisy and vary across individuals, while labeled data are often limited. Recent attention-based models on the symmetric positive definite (SPD) manifold have nevertheless achieved strong performance using covariance and connectivity representations, yet the contribution of learned token weighting remains unclear. We examine two representative architectures, MAtt (based on log-Euclidean geometry) and GBWAtt (based on generalized Bures--Wasserstein geometry), and find that their learned attention weights remain close to uniform after training. We relate this behavior to bounded similarity parameterizations that, under the original softmax scaling, limit attention-weight contrast. Moreover, replacing learned weights with uniform weights, throughout training and evaluation, has little effect on mean predictive performance while preserving each model's original aggregation geometry. Motivated by these findings, we introduce SPD-MetaFormer, an attention-free architecture built on uniformly weighted Fréchet aggregation under log-Euclidean geometry. Its backbone uses a geodesic residual to update a summary token and a shared spectral feedforward map to transform all tokens, followed by a learned weighted readout. Token states remain SPD-valued until tangent-space classification. Across three EEG benchmarks, SPD-MetaFormer achieves competitive results relative to published Euclidean and manifold baselines. Separate matched reproductions test learned versus uniform weighting within MAtt and GBWAtt. These results suggest that, in the short-sequence and limited-data regimes studied, carefully designed SPD architectures can provide a simpler and effective alternative to adaptive manifold attention.

---


### 56. [TRACE: A Governance Framework for Measuring Explainability Debt in Production AI Systems](https://arxiv.org/abs/2610.10957)

**<font color=#1a73e8>作者：</font>** Harish Kant Pathak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production AI systems deployed in high-stakes domains accumulate a governance liability that existing monitoring frameworks fail to detect: the progressive inability to explain individual decisions when regulators, auditors, or affected individuals demand accountability. We introduce TRACE (Transparency, Risk, Accountability, Compliance, and Explainability), a seven-instrument governance framework for measuring, tracking, and remediating Explainability Debt in production AI systems. The foundational instrument, the Explainability Debt Score (EDS), quantifies the proportion of production decisions falling below a governance-defined explainability confidence threshold at any point in time. Complementary instruments include DART (Debt Accumulation Rate Tracker for breach forecasting), SHIV (Scenario Health and Integrity Validator for daily governance), FDE (Feature Drift Evaluator for causal attribution), HVE (Human Validation Engine), AIDE (Audit Intervention Decision Engine), and ZERO (Zero Explainability Risk Optimiser for remediation). Through a twelve-month longitudinal case study of a production fraud detection system processing 50,000 daily financial transactions, achieving 98.46% accuracy and ROC-AUC of 0.9990, we demonstrate that an EDS of 0.23 on audit day was statistically predictable six months in advance using DART trajectory analysis (beta = 0.008/week, R-squared = 0.94, 95% CI: [0.006, 0.010]), and that 78% of Explainability Debt was concentrated in the highest-regulatory-risk decision category (transactions above $10,000), a risk asymmetry completely invisible to system-level metrics. TRACE provides the first quantitative operational architecture for EU AI Act Article 13 compliance in production AI deployment, establishing a new subdiscipline of explanation governance distinct from explanation generation.

---


### 57. [GPU-Accelerated Computation of Persistent Homology for Topological Analysis of Image Data](https://arxiv.org/abs/2610.10959)

**<font color=#1a73e8>作者：</font>** Fan Wang, Hubert Wagner, Rezaul Chowdhury 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, persistent homology has seen rapid adoption in deep learning, yet its computation remains a major bottleneck in network training. This paper introduces TopoGPU, a GPU streaming pipeline that computes persistence diagrams of cubical complexes induced by 2D and 3D images. TopoGPU streams the input image chunk by chunk, processing each chunk with massively parallel GPU kernels on a grid of GPU blocks; the resulting boundary relations are accumulated in host memory, where the CPU performs the boundary matrix reduction. TopoGPU introduces a stratification-aware discrete Morse matching that provably preserves persistent homology under streaming, together with a parallel topological sorting algorithm and a parallel V-path parity algorithm for deriving Morse boundaries on the GPU. TopoGPU outperforms Cubical Ripser, a state-of-the-art method for persistent homology computation, on every benchmark evaluated, achieving an average end-to-end speedup of 53.24x and a maximum of 198.01x. We further integrate TopoGPU into a topology-preserving deep network, demonstrating that it substantially reduces the cost of persistent homology computation during network training. TopoGPU is open source, with pre-built binaries, Google Colab notebooks, and Docker images available at the project's GitHub page: this https URL.

---


### 58. [LVSPM: Long Sequence View Synthesis and Pose Estimation Model](https://arxiv.org/abs/2610.10960)

**<font color=#1a73e8>作者：</font>** Xi Chen, Yachi Zhang, Linghao Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LVSPM, a generalizable model that jointly estimates camera poses and synthesizes novel views from uncalibrated image collections. Trained with only RGB images and pose supervision, LVSPM avoids dense 3D ground truth and employs test-time training (TTT) layers to scale seamlessly to hundreds of input views. On RealEstate10k, Co3Dv2, and DL3DV, LVSPM surpasses VGGT in pose estimation across 16-256 views, with especially large margins at strict thresholds. For novel view synthesis under a practical protocol where more views cover larger scenes, LVSPM achieves state-of-the-art pose-free quality---surpassing even pose-dependent models in PSNR---and still maintains high quality as scene scale grows, while baselines collapse. The code is available at this https URL .

---


### 59. [ASPIRE: Saddle-Point Discovery through Set Prediction and Physical Refinement](https://arxiv.org/abs/2610.10969)

**<font color=#1a73e8>作者：</font>** Yucheng Zhao, Quanyou Zhang, Shaoxiang Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting thermally activated diffusion and defect evolution with event-driven models requires identifying atomic rearrangement mechanisms and their activation barriers. Discovering the associated saddle points is a major computational bottleneck: multiple rearrangements may originate from one metastable state, while costly local searches can fail or repeatedly converge to the same saddle. To address this challenge, we introduce ASPIRE (Atomistic Saddle-Point Inference with Refinement for Events), a framework that predicts a set of saddle candidates from a single initial atomic environment and refines them through Dimer searches on the original interatomic potential. The framework's equivariant set predictor, Ev-Quiformer, integrates (i) geometry-conditioned scalar-vector event slots for generating multiple saddle-point proposals and (ii) a decoder that maps each slot to a full atomic displacement field by combining atom, slot, and anchor-relative vectors with invariant coefficients. We also contribute two datasets: (i) BCCFE4VACAV-4000, comprising 4,000 four-vacancy body-centered cubic iron configurations and 65,450 reference events grouped by initial state for set supervision and post-refinement evaluation; and (ii) BCCFE-1TO4VAC, comprising 5,372 configurations with one to four vacancies each. Theoretically, we establish conditions for proposal equivariance. Experimentally, ASPIRE achieves 77.20% reference-event coverage on this benchmark, compared with 75.73% for a conventional Dimer baseline, while requiring approximately half as many Dimer force evaluations. In a timing evaluation on 50 configurations, ASPIRE reduces wall time per configuration from 478.8 s to 176.3 s under the stated hardware settings.

---


### 60. [Transferability of Learned States in Neural PDE Solvers](https://arxiv.org/abs/2610.10972)

**<font color=#1a73e8>作者：</font>** Shunye Wang, Haochen Wen, Shuo Li Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Assessing useful reuse in neural PDE solvers is challenging: final accuracy can reflect source learning and target-time computation. Our reuse contract separates solution accuracy, learning contribution, and numerical utility through paired state comparisons, matched target information and budgets, and cost accounting. A literature audit extracts 18 version-specific protocol records from 12 papers, documenting retained states, target-time resources, and reported controls. For a fixed linear system and residual tolerance, we construct two initial guesses with identical solution-error, energy-error, and residual norms, reaching the same solution with different conjugate-gradient (CG) iteration counts. Across 240 source-training trajectories, two linear PDE families, Fourier neural operators and convolutional networks, a fixed predictor's benefit reverses across correction algorithms. Among pairs with both relative prediction errors less than or equal to 5 percent on 64 in-distribution tasks (63 by 63 interior grids), reductions in all three norms accompany more CG iterations, at mean taskwise rates of 23.5 percent and 23.9 percent in two libraries. Work-based selection saves 2.50-3.33 CG iterations on held-out in-distribution tasks; matched adaptation demonstrates finite-budget pretraining value. Independent batches confirm a 0.73 percent complete online saving for one physics-trained Fourier neural operator against zero-initialized Poisson-preconditioned CG. Reuse requires matched state comparisons and downstream computational evidence.

---


### 61. [Multi-Bandwidth Distribution Matching Distillation: On the Equivalence of Distribution Matching Distillation and Drifting Models](https://arxiv.org/abs/2610.10989)

**<font color=#1a73e8>作者：</font>** Jialin Zhu, Xing Liu, Feixiang He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Researchers are exploring effective one-step generative model continuously, and, Drifting Models (Deng et al., 2026), demonstrate great potential in one-step generation recently. There are works that reveal the connection between Diffusion & Flow Style Generative Models (DFSGMs) (Ho et al., 2020; Song et al., 2020a;b; Lipman et al., 2022; Liu et al., 2022) and Drifting Models (Li & Zhu, 2026; Lai et al., 2026; Turan et al., 2026). But no one has yet established a precise correspondence between the Drifting Model and the widely used distillation method- Distribution Matching Distillation (DMD/DMD2) (Yin et al., 2024b;a) to the best of our knowledge, even though their optimization objective formulas are virtually identical. In this paper, we prove that by converting the velocity-field / noise-field from the pre-trained DFSGMs into the attraction force field in Drifting Models and estimating the repulsion force field from the generative distribution, training the Drifting Model is naturally equivalent to the Distribution Matching Distillation. With this equivalent concept, we propose an improved method based on DMD from the Drifting Model's perspective- Multi-Bandwidth Distribution Matching Distillation (MBDMD).

---


### 62. [Region-Aware CLS Token Augmentation for Fine-Grained Image Retrieval](https://arxiv.org/abs/2610.10991)

**<font color=#1a73e8>作者：</font>** Ian de Holanda Cavalcanti Bezerra, Vivek Trivedy, Lucas Pascotti Valem 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image retrieval methods often rely on a single global semantic descriptor extracted from an image, e.g., the [CLS] token in vision transformers. However, trying to squeeze all the semantic information of an image into a single descriptor can hurt downstream retrieval performance, especially for fine-grained retrieval tasks. In this work, we augment the semantic tokens in the newer visual transformers, the global [CLS] token and the four register tokens, with a carefully selected collection of spatial tokens, aiming to capture the spatial region representation that characterizes the contents captured in each of the semantic tokens. We leverage the DINOv2-reg model, which includes register tokens that emergently learn object and part-based representations. For each "cue" token ([CLS] and each register token), we find a "buddy" image patch token and extract an N x N patch region to produce a set of localized ROI tokens. Our approach automatically captures important regions of interest without any external bounding boxes or saliency modules, purely by matching semantic tokens with their spatial representation regions. Furthermore, we incorporate these tokens into a multi-vector retrieval framework inspired by ColBERT, enabling fine-grained matching via a per-token alignment mechanism while avoiding the large storage cost of keeping all patch embeddings. Through extensive experiments, we find that (1) register tokens encode useful fine-grained details that can complement the [CLS] token; (2) automatically pooled ROI tokens further improve fine-grained discrimination; and (3) multi-vector retrieval with a small set of tokens improves over a DINOv2-reg single-vector baseline while remaining tractable for large-scale search. The code is available at this https URL.

---


### 63. [The Hint Weight of ML-DSA Signatures Is Key-Dependent: An Empirical Study across the Three FIPS 204 Parameter Sets](https://arxiv.org/abs/2610.10992)

**<font color=#1a73e8>作者：</font>** Dominik Blain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Every ML-DSA (FIPS 204) signature carries a public hint vector h. We find that the Hamming weight of each hint polynomial h_k depends on the signing key: to first order it measures the Euclidean norm of (t0)_k, the low-order part of t that key generation leaves out of the public key. A closed-form model predicts the per-key mean weight with Pearson r between 0.95 and 0.98; once the norm is accounted for, we detect no key-dependent signal above sampling noise. We measure the effect on the reference C implementation, with 200 keys and 2,000 signatures per key for each parameter set. A one-way ANOVA rejects key-independence of the total hint weight for ML-DSA-44, ML-DSA-65 and ML-DSA-87 (F = 30.1, 10.3, 11.1). The effect is weak: the key explains 0.5% to 1.5% of the variance of the total weight. A single signature identifies its key among 200 with 1.1 to 1.3 times chance accuracy from the total weight, and 1.5 to 1.8 times from the per-polynomial weight vector. A one-sided test at significance 0.001 separates two typical keys with probability one half after about 1,300 to 3,700 signatures per key. The hint weight does not endanger the signing key. The Dilithium designers do not treat t0 as secret, and t0 is known to be recoverable from signatures. The hint weight is, however, a weak statistical fingerprint: with enough signatures, it can be used to test whether they come from a common key, without the public key. Bounded-weight signing, a backward-compatible filter whose effect on the security argument we did not analyze, removes 86-91% of the between-key spread of the total weight but leaves the per-polynomial channel largely intact.

---


### 64. [F$^3$NO: Frequency-Decomposed Finite-Time Flow-map Neural Operators with Cross-Scale Conditioning](https://arxiv.org/abs/2610.10998)

**<font color=#1a73e8>作者：</font>** Fan Wu, Cheng Jing, Kookjin Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators enable fast PDE forecasting, but repeated predictions accumulate errors and fine-scale structures remain difficult to resolve. We introduce a frequency-decomposed finite-time flow-map neural operator (F$^3$NO) that leverages updated low-frequency features to guide nonlinear refinement of high-frequency information. Within each layer, this cross-scale conditioning connects global spectral processing with local detail refinement. The model directly predicts states at specified future times and adjusts the contributions of the two branches according to the prediction interval. For longer trajectories, it combines parallel predictions within short temporal segments with recursive propagation between segments. Experiments on five PDE benchmarks demonstrate improved forecasting accuracy over autoregressive and direct-prediction baselines. Ablations show that frequency-decomposed refinement can improve accuracy with fewer parameters, while the benefits of segmentation depend on spatial resolution and dynamical regime.

---


### 65. [Low-rank tensor structure of precipitation and its application to satellite-reference merging](https://arxiv.org/abs/2610.11000)

**<font color=#1a73e8>作者：</font>** Ryan Solgi, Rohan Shankar, Hugo A. Loaiciga  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The intermittent and variable nature of precipitation makes its accurate estimation over extended domains difficult, yet its spatiotemporal structure suggests that a low-rank representation may be possible. This work represents daily precipitation over the contiguous United States (CONUS) as spatiotemporal tensors and applies CANDECOMP/PARAFAC factorization, showing that preserving the native spatial and temporal modes yields more accurate reconstruction than factorizing independent daily fields or unfolded space--time matrices. Building on this finding, this work presents TMerge, a tensor-based framework that integrates satellite precipitation with sparse reference observations through shared low-rank spatial and temporal factors. TMerge was applied to correct the IMERG Final Run product with climate prediction center reference observations over CONUS. During 2019-2022, TMerge increased correlation from 0.53 to 0.85 and reduced root-mean-square error and mean absolute error by 48.2% and 29.3%, respectively. TMerge consistently outperformed linear bias correction, quantile mapping, and neural networks across seasons, precipitation-intensity regimes, and regions. Improvements were spatially coherent and largest in coastal regions where IMERG errors were greatest. These results demonstrate that low-rank tensor structure parsimoniously approximates the dominant spatiotemporal variability of precipitation and provides a practical mechanism for improving satellite estimates under limited reference observations over extended domains.

---


### 66. [PCAsplat: Gaussian Splatting with Local PCA Regularization](https://arxiv.org/abs/2610.11011)

**<font color=#1a73e8>作者：</font>** Vitor Matias, Filipe Nascimento, Kiyohiro Nakayama 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian splatting has emerged as a flexible representation for 3D reconstruction from posed images. However, existing methods are optimized primarily using rasterization-based losses, which supervise a splat only when it contributes to sampled camera rays. Gaussians that are occluded or contribute little to the sampled view therefore receive weak or no geometric gradients and may drift away from the underlying surface, producing undesired floaters. We introduce PCAsplat, a geometry-aware regularization framework for Gaussian splatting based on differentiable local principal component analysis (PCA). Our PCA regularizer acts directly on neighborhoods of Gaussian centers and can therefore update Gaussians that do not contribute to the current training view. We regularize the PCA eigenvalues to encourage Gaussians to move to the underlying surface with isotropic tangent-plane coverage. We also align each Gaussian normal with the PCA-estimated neighborhood normal to enforce consistent orientation. Experiments on DTU, Tanks and Temples, and NeRF Synthetic show that the splats produced by PCAsplat better approximate samples of the reference surface while substantially reducing undesired floaters. These surface-aligned splats enable downstream geometry-processing tasks, including point cloud segmentation, and direct Poisson reconstruction. Additionally, PCAsplat remains competitive under conventional novel view synthesis and mesh extraction tasks. Code will be released.

---


### 67. [Distillation for Incrimination and Distillation for Capabilities](https://arxiv.org/abs/2610.11012)

**<font color=#1a73e8>作者：</font>** Sebastian Prasanna, Jacqueline Tay, Alek Westover  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Powerful misaligned AI models might recognize alignment evaluations and strategically behave well on them, rendering direct audits uninformative. However, distilling such a model into a weaker benign student places the teacher in a Distillation Double Bind: if misalignment transfers, the student may conceal it less effectively, revealing evidence about the teacher; if it does not, the student may learn useful capabilities while remaining benign. We introduce two distinct distillation approaches, one targeting each outcome. Distillation for Incrimination (DFI) aims to transfer misalignment but not the ability to conceal it. Distilling AuditBench's secret-keeping models into their underlying instruction-tuned model produces students that are significantly more likely than their teachers to admit their hidden behavior when asked, suggesting that knowledge of the behavior transferred more readily than the propensity to conceal it. Confession gains largely disappear when the student does not share the teacher's pretrained base, so DFI should target the teacher's own pre-RL checkpoint, which is weaker than the teacher but shares its base model. Distillation for Capabilities (DFC) aims to transfer capabilities but not misalignment. Among several techniques we evaluate, two are effective: inoculation prompting and training for more epochs on fewer unique examples. Both preserve the capability gains of standard distillation while substantially reducing the subliminal transfer of an animal preference, our proxy for misalignment. Together, these findings demonstrate two ways distillation can be used for AI safety: incriminating misaligned models, and extracting their capabilities without their misalignment.

---


### 68. [Expression-Diverse References for Identity-Preserving Video Generation](https://arxiv.org/abs/2610.11023)

**<font color=#1a73e8>作者：</font>** Tianwen Fu, Wenbin Teng, Gonglin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity-preserving video generation aims to maintain a subject's identity while synthesizing realistic videos. Yet a single reference portrait captures the subject's appearance under only one facial configuration. As expressions change, facial appearance can vary in highly identity-specific ways, leaving the subject's appearance under unseen expressions underdetermined by the reference alone. This expression-dependent variation also complicates evaluation: similarity to a neutral reference may decrease under strong expressions even for real images of the same person. We investigate this limitation from both generation and evaluation perspectives. First, we quantify how face-recognition similarity varies with expression intensity using controlled photographs and MEAD videos. We then construct a compact yet expressive reference gallery that captures diverse expression-dependent facial configurations. Matching against this gallery provides a more robust measure of identity similarity under expressive motion. To further expose performance degradation with expression intensity, we report identity similarity separately for mild, intense, and extreme expressions. For generation, we extend Stand-In to condition on our expression-diverse reference sets and develop a data-curation pipeline that extracts consistent yet diverse face crops from training videos. In practical settings where only a single portrait is available, we construct the reference set by synthesizing additional expressions with a pretrained facial reenactment model. On our controlled benchmark, both real and synthesized reference sets outperform the evaluated baselines in identity similarity across all three expression-intensity regimes, with the largest improvements for extreme expressions.

---


### 69. [Transforming Image Editors into Video Editors](https://arxiv.org/abs/2610.11037)

**<font color=#1a73e8>作者：</font>** Feng Wang, Zijie Li, Ceyuan Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image editing systems have achieved impressive semantic understanding, visual fidelity, and instruction-following ability, while video editing remains substantially more difficult and costly. In this paper, we present a simple alternative to end-to-end video editing: instead of training a monolithic video editor, we transform a strong image editor into a video editor through anchor-based generation. Our key insight is that video editing can be decomposed into two subproblems: editing a sparse set of keyframes and propagating those edits across time. Based on this observation, we propose Anchor-based Video Editing (AVE), a two-stage framework in which a powerful image editor first performs composed editing on selected keyframes, and a motion-guided image-to-video diffusion model then generates the final video by treating the edited keyframes as fixed anchors. This design directly inherits the strengths of modern image editors while avoiding expensive end-to-end video editing training. Experiments on IVEBench and VIE-Bench show that AVE achieves strong performance in instruction following, temporal consistency, and content fidelity. Further ablations reveal that final video editing quality is strongly correlated with the quality of the image editor, suggesting that future progress in video editing may come from stronger image editing foundations and lightweight transfer to video. Code is available at this https URL.

---


### 70. [SatFix: Absolute Visual Localization of UAVs in Satellite Maps from a Single Oblique Image](https://arxiv.org/abs/2610.11049)

**<font color=#1a73e8>作者：</font>** Jiarui Zeng, Kun Shi, Chiman Vong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study absolute metric UAV localization within a provided geo-referenced satellite region, recovering continuous map position and viewing heading from a single oblique image or a short multi-view clip. Existing cross-view geo-localization methods retrieve the most similar satellite tile from a gallery and report Recall@K, but retrieval depends on gallery sampling, provides no heading estimate, and returns a tile index rather than a continuous coordinate. We propose SatFix, a feed-forward UAV--satellite localization framework built on VGGT-$\Omega$. Satellite-grid features act as queries that aggregate UAV visual evidence, and two lightweight heads regress a 3-DoF pose in the satellite-map frame: continuous 2D position and heading. SatFix requires no explicit 3D map, rendered bird's-eye image, auxiliary sensor, or test-time pose alignment. A single model supports both single- and multi-view inputs, with trajectory constraints used during multi-view training. For metric evaluation, we introduce University-Metric, where satellite imagery is re-collected over a region up to 10.7$\times$ longer on a side (about 114$\times$ the ground area) than the original University-1652 tiles, with continuous position and heading labels for the original UAV tours. With one UAV view, SatFix localizes 52.08% of test frames within 50 m and 17.34% within 10 m, with median position and heading errors of 45.66 m and $20.81^\circ$, respectively. Inference takes under 0.1 s per single-view query on an NVIDIA RTX 4090. With nine UAV views, the median position error falls to 21.96 m and the median heading error to $8.73^\circ$. Compared with a fine-tuned VGGT-$\Omega$ baseline, SatFix reduces median position error by 34.0% and nine-view median heading error from $25.43^\circ$ to $8.73^\circ$.

---


### 71. [Learning What to Trust in Multimodal Learning under Noisy Supervision](https://arxiv.org/abs/2610.11057)

**<font color=#1a73e8>作者：</font>** Jiashuo Zou, Xiaobo Xia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal classification processes and relates information from multiple modalities to achieve more accurate predictions. However, existing methods typically rely on high-quality ground-truth labels, which are difficult to obtain in real-world scenarios. While sample-selection methods for learning with noisy labels aim to identify correctly labeled examples from noisy data, traditional methods primarily focus on unimodal settings and fail to exploit multimodal information fully. This motivates us to build a more reliable noise detector in multimodal learning. To this end, we theoretically analyze the relationship between representation structure and noise detection capability. Based on this analysis, we propose REFINE, which is a multimodal label-noise detection framework that jointly uses fused and unimodal representations for label-noise detection. Specifically, REFINE constructs discriminative eigenvectors through discriminative analysis of the target and background classes and selects trusted representation spaces with better noise detection capability for each class. Within each trusted space, REFINE measures the alignment between each instance representation and the discriminative eigenvectors. It then combines the subsets selected from these spaces. The combined set provides cleaner supervision for updating the multimodal classifier, thereby reducing the influence of mislabeled examples during training and improving model generalization. Extensive experiments across diverse tasks demonstrate REFINE's superiority compared to baseline methods. The source code will be publicly available.

---


### 72. [Refine Connections, Close the Gap: A Reliable Enhancement Framework for Driving Scene Topology](https://arxiv.org/abs/2610.11058)

**<font color=#1a73e8>作者：</font>** Xiaoqi Wang, Dingyi Zhaung, David Paz 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In autonomous driving, understanding scene topology - the connectivity between lanes and traffic elements - is critical for safe path planning and motion control. While current methods excel at detecting individual map elements, their connectivity reasoning often falls short of its theoretical potential, leaving a significant performance gap relative to the theoretical upper-bound achievable given the underlying detections. Furthermore, the decision-ready topology graphs passed to downstream tasks often remain unreliable. Current approaches typically derive connectivity by thresholding continuous topology scores; however, these scores often fail to reflect the true logical likelihood of connectivity, resulting in false positives or missing connections. Existing benchmarks further overlook this issue by primarily evaluating continuous metrics, rather than assessing the discrete connectivity required for decision-making. To bridge these gaps, we propose TopoEnhance, a novel topology enhancement framework designed to unlock the latent potential of existing methods and improve the reliability of decision-ready topology. We formulate topology enhancement as a denoising-based reconstruction process, where the model learns to recover structural consistency from stochastically corrupted ground-truth graphs. This formulation enables the model to resolve logical inconsistencies and rectify unreliable connections, producing robust discrete topology graphs that closely approach theoretical maximum performance. Extensive experiments across different baselines show that TopoEnhance consistently improves both continuous topology metrics (TOP score), and discrete connectivity measured by our adapted Topology Jaccard Similarity (TJS) metric. As a flexible, source-agnostic framework, TopoEnhance delivers substantial gains across diverse state-of-the-art baselines without requiring retraining.

---


### 73. [CityDeploy-Bench: Benchmarking Physics-Grounded Spatial Set Planning for Multi-Transmitter Network Deployment](https://arxiv.org/abs/2610.11065)

**<font color=#1a73e8>作者：</font>** Chenyang Yuan, Xiaoyuan Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automating city-scale wireless deployment remains challenging under complex urban propagation and network-wide interference. We introduce \textbf{CityDeploy-Bench}, a benchmark that reframes multi-transmitter deployment as \emph{physics-grounded spatial set planning} under a unified ray-tracing verifier. The benchmark separates utility representation from planning dynamics, enabling controlled comparison between direct scalar rewards, relational models, and higher-order interaction structures across diverse planners. Our experiments reveal a clear transition in planning behavior as physical coupling grows. Deployment quality becomes increasingly dependent on whether the learned utility captures collective transmitter interactions, whereas stronger search alone cannot compensate for missing relational structure. This establishes multi-transmitter deployment as a coordination problem over physically interacting sets rather than a collection of independent spatial decisions. We release CityDeploy-Data and the benchmark framework as a reproducible testbed for research linking decision learning with physically grounded wireless network design.

---


### 74. [No Distillation Needed: Single-Pass Real-Time Talking Heads via Acausal Noise Shaping](https://arxiv.org/abs/2610.11070)

**<font color=#1a73e8>作者：</font>** Yu Han, Dejan Markovic, Alexander Richard 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-driven facial animation underpins real-time avatars, telepresence, and embodied virtual agents. And it must run online: each frame emitted from audio observed up to the current time, at interactive rates. Recent progress is dominated by diffusion models, which need many network evaluations per sample and are therefore a poor fit for streaming. We argue the cost is unnecessary in this domain. Audio-conditioned facial motion occupies a comparatively low-dimensional manifold, a regime where a single-pass GAN suffices. The obstacle is not capacity but stochastic structure. We show that a causal, time-invariant generator driven by i.i.d. noise cannot suppress its output spectrum over a band without collapsing its per-step innovation. We proposed FaceGAN, which dissolved the limitation by shaping the noise pathway acausally. Because the driving noise is synthetic, its future can be sampled now, so the audio-to-expression path stays causal, and the model supports fully causal operation. FaceGAN emits expression and head pose in a single forward pass per frame and matches or outperforms state-of-art approaches in generation quality. Being feed-forward with bounded attention windows, it generates indefinitely without drift.

---


### 75. [Optimally Pacing Budget Spending and Learning](https://arxiv.org/abs/2610.11074)

**<font color=#1a73e8>作者：</font>** Mark Braverman, Jingyi Liu, Jieming Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish near-optimal regret bounds for budget-constrained online learning against arbitrary classes of budget-pacing experts in the adversarial setting. In particular, given any class of $F$ experts and a candidate budget pacing schedule, we provide a full-information algorithm which obtains regret $O(D \sqrt{\log F}+ \sqrt{T\log F})$ against all experts whose cumulative spending stays within distance $D$ of this schedule, matching lower bounds established by Braverman et al. (2025).
We additionally show that our technique extends to various problems in online resource allocation, where the learner gets to see the rewards and costs of the current options available to them, and establish $O(D\sqrt{\log F})$ regret bounds when fractional allocation is allowed. This is the first algorithm we are aware of which can achieve $o(\sqrt{T})$ guarantees for such tasks.

---


### 76. [DaCe-DT: Data-Centric Offline Multi-Task Reinforcement Learning via Adaptive Prompts and Trajectory Correction for Heterogeneous Tasks](https://arxiv.org/abs/2610.11085)

**<font color=#1a73e8>作者：</font>** Xinfei Wang, Shanchen Pang, Chenhao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline multi-task reinforcement learning (Offline MTRL) heavily depends on the quality and distribution of pre-collected data. However, existing methods mainly focus on algorithmic optimization, with less emphasis on data-level improvements to enhance learning ability and generalization performance. This paper, from a data perspective, reveals three key bottlenecks that limit Offline MTRL performance:(i) ineffective utilization of prompts length under diverse task complexities, and (ii) semantic irrelevance of randomly sampled prompt segments, (iii) misleading supervision induced by fragmented and discontinuous trajectories. To address these challenges, we propose DaCe-DT, a robust offline MTRL framework designed to be insensitive to heterogeneous task complexities and data quality, featuring length-gated prompt masking (LGPM), retrieval-augmented prompt construction (RAPC), and value-adaptive return calibration (VARC). Together, these mechanisms enable DaCe-DT to deliver data-centric prompt adaptation and trajectory refinement, resulting in robust multi-task generalization and stable policy learning amid heterogeneous offline data and tasks. Experimental results on Meta-World show that DaCe-DT consistently outperforms state-of-the-art methods, achieving an average improvement of 11.73% on optimal datasets and an improvement of 13.34% on suboptimal datasets, demonstrating its effectiveness in learning stably from imperfect data and improving overall multi-task performance.

---


### 77. [Contrast Enhancement or Noise Reduction? On Improving Cervical Cancer Classification](https://arxiv.org/abs/2610.11086)

**<font color=#1a73e8>作者：</font>** Ach Khozaimi, Ulfatun Nahdhiyah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Cervical cancer is one of the leading causes of mortality worldwide. Deep learning has shown promising performance in medical image classification. The influence of image preprocessing algorithms on classification performance remains insufficiently investigated in the literature. This research aims to evaluate the impact of image preprocessing algorithms on the performance of CNNs for Pap smear image classification.
Methods: Three CNN architectures (ResNet-34, MobileNet-V2, and DenseNet-121) were trained and evaluated using the SIPaKMeD dataset. Two preprocessing algorithms were applied: the PMD filter for noise reduction and CLAHE for contrast enhancement. The model performance was assessed using a confusion matrix.
Results: Preprocessing improved the classification performance of all models. CLAHE significantly increased the accuracy of ResNet-34 from 76.73% to 84.16% and DenseNet-121 from 76.73% to 84.16%. The PMD filter yielded limited improvement and slightly reduced the MobileNet-V2 performance.
Novelty: This research provides a systematic comparison of contrast enhancement and noise reduction techniques across CNN architectures. This research demonstrates that contrast enhancement is more effective than noise reduction in improving CNN performance. The research provides new pipelines for improving cervical cancer classification.

---


### 78. [Continuous Ground-Truth Construction and a Recovery Policy for Air--Water Robotic Tracking](https://arxiv.org/abs/2610.11096)

**<font color=#1a73e8>作者：</font>** Jiangong Xiao, Zhe Sun, Kanzhong Yao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual tracking across the air-water interface is challenged by splashes, bubbles, refraction, reflections, and abrupt appearance changes that can temporarily invalidate observations. This setting poses two coupled difficulties: first, for evaluation, image-only annotation cannot reliably describe the target's physical location during visual blindness; second, for online tracking, corrupted observations can contaminate motion estimates and appearance templates. We address the first difficulty with a construction pipeline that synchronizes camera frames with motion-capture poses, projects known target geometry, corrects underwater projection with a medium-gated residual, and subjects the annotations to manual review. This yields an evaluation-only cross-medium test set of 22,346 frames. We further introduce a Cross-Medium Recovery Policy (CMRP) centered on confidence-triggered template selection. It supplies MixFormerV2 with the fixed initial template, a window-best pre-trigger template, and a trigger-frame Kalman-guided image crop, together with their associated weights, without retraining the visual backbone. In the accuracy evaluation, CMRP achieves 49.90 Macro Success AUC, 2.95 points above MixFormerV2 Official. On selected cross-medium transition and occlusion-recovery intervals, CMRP increases MixFormerV2 tracking coverage from 47.91\% to 50.43\% relative to Official updating, while mean loss-to-recovery latency over successfully recovered videos decreases from 55.3 to 49.3 frames.

---


### 79. [Skeleton-Guided Progressive Test-Time Adaptation for Thin Curvilinear Structures](https://arxiv.org/abs/2610.11104)

**<font color=#1a73e8>作者：</font>** Boa Jang, JunGyu Lee, Gwanho Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of thin curvilinear structures is vital for various real-world applications, from vessel analysis to road extraction. Yet their intricate geometry makes even minor pixel-wise errors enough to break the global topology, and this structural fragility turns severe domain shifts into catastrophic failures. The difficulty is most acute under cross-modality gaps, where the imaging process itself differs fundamentally between source and target. While test-time adaptation (TTA) offers a practical source-free remedy, existing methods adapt feature statistics and confidence, neither of which constrains connectivity, and thus degrade under such extreme gaps. To address this, we propose Skeleton-Guided Progressive Test-Time Adaptation (SGP-TTA). Progressive Batch Normalization (ProgBN) shifts normalization from frozen source statistics toward current target estimates under a sample-count schedule, so that the source-target balance follows the stage of adaptation rather than a fixed coefficient. Consensus Skeleton Recall (CSR) then derives a structural target from geometrically aligned multi-view predictions and updates only the BN affine parameters to preserve connected structures. Extensive experiments show that SGP-TTA consistently outperforms existing TTA methods in topological connectivity, with the largest margins under cross-modality shift. The project page is available at this https URL.

---


### 80. [TKCAM: Text and Keyframe to Camera Trajectory Generation](https://arxiv.org/abs/2610.11105)

**<font color=#1a73e8>作者：</font>** Haozhe Yang, Zhiyang Dou, Zekai Gu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating high-quality and controllable camera motion is essential for AI-assisted cinematography, video synthesis, and 3D scene understanding. We introduce TKCAM, a Text- and Keyframe-conditioned CAMera-motion synthesis framework based on generative masked modeling. We represent camera dynamics using a 12-dimensional kinematic feature comprising position, velocity, and a continuous rotation representation and discretize them into hierarchical motion tokens via a Residual Vector Quantizer (RVQ). A two-stage masked transformer architecture then learns to reconstruct and refine these tokens, utilizing explicit self- and cross-attention modules for multimodal conditioning. A central feature of our framework is sparse visual keyframe conditioning: users can provide free-form text prompts together with RGB observations at selected timestamps, which provide temporally localized visual guidance for generating coherent in-between trajectories. Furthermore, to advance evaluation standards, we curate RealEstate10K-Cap, a large-scale text-camera dataset, and establish a cross-domain benchmark with a Universal CLaTr Evaluator. Extensive experiments demonstrate that TKCAM surpasses recent state-of-the-art baselines on Fréchet distance (FID), text-motion matching scores, and retrieval metrics (R@K), while additional analyses evaluate temporal smoothness and cross-domain generalization. Code is available at this https URL.

---


### 81. [Accelerating HQC for Post-Quantum TLS 1.3 on x86 IoT Gateways](https://arxiv.org/abs/2610.11107)

**<font color=#1a73e8>作者：</font>** Jihoon Jang, Hyunju Park, Jebin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-quantum TLS at an IoT gateway must protect many device connections without large increases in handshake delay, CPU cost, or network traffic. HQC provides code-based diversity beyond ML-KEM, but its computation and ciphertext sizes can increase these costs. We optimize HQC for x86 processors with AVX2, AVX-512, and the Galois Field New Instructions (GFNI), and integrate the resulting implementations into TLS 1.3. We extend branch-free Toom-Cook/Karatsuba multiplication to AVX-512, accelerate Reed-Solomon decoding with GFNI, improve Reed-Muller decoding, accelerate SHA3-512 and fixed-weight sampling, and port Frobenius additive FFT (FAFFT) multiplication to AVX-512 + GFNI for HQC-5. On an Intel Core i5-1135G7 processor, our AVX2 implementation reduces decapsulation by 11.1-21.5% over the fastest prior AVX2 results. Our AVX-512 implementation reduces key generation by 24.9-29.5%, encapsulation by 10.4-11.1%, and decapsulation by 20.6-26.1% relative to Cabral et al. across the three HQC parameter sets. We evaluate the effects of these implementations on TLS 1.3 handshake latency and server and client CPU costs, as well as the effects of round-trip time (RTT) and bandwidth. In local loopback TLS measurements, our AVX-512 HQC-5 implementation reduces handshake latency from 3.22 ms to 2.92 ms compared with Cabral et al. On a constrained path with 1 Mbit/s bandwidth and an added RTT of 50 ms, the HQC-5 handshake takes 243 ms, compared with 87 ms for ML-KEM-1024. This indicates that HQC public-key and ciphertext sizes, rather than implementation speed, determine the remaining handshake cost on constrained links.

---


### 82. [Cova-PINN: Cross-Domain Conservation Physics-Informed Neural Network for Fluid-Solid Conjugate Heat Transfer in Complex Geometries](https://arxiv.org/abs/2610.11108)

**<font color=#1a73e8>作者：</font>** Weizheng Zhang, Xunjie Xie, Hao Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-domain physics-informed neural networks (PINNs) flexibly model medium-specific representations to solve fluid--solid conjugate heat transfer (CHT). However, standard multi-domain PINNs enforce governing equations and interface conditions on separately sampled domain supports, which can yield plausible temperature fields but inaccurate end-to-end energy transfer and outlet temperatures. We propose Cova-PINN, a multi-domain PINN framework that aligns conservation support with thermal interaction paths in complex geometries. Cova-PINN jointly optimizes cross-domain composite control-volume balances at the local scale and paired-wall closure at the global exchanger scale. We evaluate Cova-PINN on four triply periodic minimal surface (TPMS) heat exchangers and a geometrically distinct DualMS design against CHT-specific, optimization-oriented, and complex-geometry PINN baselines under a common protocol. Relative to the closest baseline, MUSA-PINN-CHT, Cova-PINN reduces average outlet-temperature and device-level closure errors across the four TPMS topologies by $37.7\%$ and $60.2\%$, respectively, while also improving full-field and heat-duty accuracy, with consistent gains on DualMS.

---


### 83. [MCL: Meta Convolution Layer](https://arxiv.org/abs/2610.11117)

**<font color=#1a73e8>作者：</font>** Naim Reza, Md Al Amin, Ho Yub Jung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic convolution enhances convolutional neural networks (CNNs) by adapting kernels to input content, but it expresses the effective kernel as a linear mixture of a small number of basis kernels, which limits expressivity and complicates optimization as the mixture size grows. In this work, we revisit dynamic convolution from a functional perspective and propose the Meta Convolution Layer (MCL), which directly models the convolutional kernel as an input-conditioned function W(x) realized via a high-order polynomial expansion. Leveraging nested residual blocks inspired by deep polynomial networks, MCL implements a structured polynomial meta-network that generates a single input-adaptive kernel, thereby decoupling representational power from the explicit number of mixture kernels and alleviating training instability. MCL is a plug-in addition with standard convolutions and can be seamlessly integrated into both CNN and transformer backbones. Experimental evaluation shows that adding MCL improves the Top-1 accuracy of Resnet- 18, Resnet-50 and ResNet-101 by 6.61%, 3.42% and 3.05% on the ImageNet dataset. Moreover, the proposed method significantly boosts the accuracy of Resnet and Wide-Resnet variants on CIFAR-10 and CIFAR-100 datasets. Additionally, the proposed method outperforms previous methods on fine-grained visual classification tasks using Swin and ViT backbones. These results demonstrate that high-order polynomial kernel generation is a powerful and scalable alternative to linear mixture based dynamic convolution.

---


### 84. [GameCommBench: A Unified Benchmark and Type-Aware Evaluation for AI-Generated Game Commentary](https://arxiv.org/abs/2610.11129)

**<font color=#1a73e8>作者：</font>** Qirui Zheng, Zhengteng Lin, Yunyi Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Game commentary is an open-ended generation task requiring multimodal perception, strategic reasoning, and contextual knowledge. Existing AI-Generated Game Commentary (AI-GGC) studies remain fragmented across games, modalities, and evaluation protocols, while overlap-based or holistic evaluators fail to capture the functional heterogeneity of commentary. We introduce \textsc{GameCommBench}, a unified benchmark spanning board games, sports, and esports, with commentary aligned to heterogeneous game contexts and annotated by commentary type. We further propose Type-Aware Commentary Evaluation (TACE), a structured framework for evaluating different types of commentary. We then validate TACE for reliability and human agreement, and use it to benchmark representative AI commentators. Results reveal non-uniform capability profiles, with live observation and strategic analysis emerging as major bottlenecks. Together, \textsc{GameCommBench} and TACE provide a diagnostic foundation for comparable and interpretable AI-GGC evaluation.

---


### 85. [Machine Learning Optimization for Enhanced OS Fingerprinting](https://arxiv.org/abs/2610.11133)

**<font color=#1a73e8>作者：</font>** Jae Sung Kim, Spencer Ekeroth, Jeremy Neale  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operating System (OS) Fingerprinting is a technique that can be used to identify a network's operating systems by evaluating network traffic in the form of TCP/IP packets. This research will explore the effectiveness of passively identifying operating systems on the CIC-IDS2017 dataset, a collection of over 47 gigabytes of pcap files with their corresponding operating systems. This research also proposes a new command line interface, OsirisML, which uses nPrint to preprocess the data into tabular data and XGBoost to apply ML to the data to generate, retrain, and test ML models. When packets are split randomly between training and testing, OsirisML models reach an accuracy of 97.66% on a down-sampled subset of the Friday capture and 84.69% on the entire capture. On the entire Monday capture, which contains no attacks, OsirisML reaches an accuracy of 73.83% and an F-1 score of 79.38%.

---


### 86. [IntrinSync: Joint Intrinsic Decomposition and Reciprocal Rendering](https://arxiv.org/abs/2610.11138)

**<font color=#1a73e8>作者：</font>** Zheng Gu, Rui Huang, Xilu Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inverse rendering decomposes an image into intrinsic properties such as appearance, illumination, geometry, and material, yet these properties are inherently interdependent. A reliable decomposition should produce intrinsic maps that are not only individually plausible, but also mutually compatible in explaining the image. However, existing methods either model intrinsic channels in isolation or treat inverse and forward rendering as separate processes, leaving the interdependence underexploited. In this paper, we introduce IntrinSync, a unified framework that captures this interdependence through joint-channel modeling and reciprocal inverse-forward rendering. At the channel level, we jointly decompose an input RGB into albedo, shading, surface normal, roughness, and metallic maps through a 1-to-N mapping, enabling information exchange across channels throughout generation. At the process level, we establish inverse-forward reciprocity through a dual cycle-consistent objective that aligns corresponding predictions across a closed loop. Experiments on three datasets demonstrate that our method achieves competitive intrinsic estimation and forward rendering performance, improving coherence and physical consistency. Beyond decomposition, IntrinSync provides a physically grounded interface for image editing, allowing intrinsic properties to be explicitly manipulated and rendered back into RGB images.

---


### 87. [A Unified Score Matching Paradigm for Video Anomaly Detection and Anticipation](https://arxiv.org/abs/2610.11149)

**<font color=#1a73e8>作者：</font>** Congqi Cao, Zhenhe Liang, Hanwen Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly detection (VAD) is a fundamental and safety-critical task in computer vision. Recent generative approaches detect anomalies from a distributional perspective, but remain limited by local anomaly modes. Meanwhile, video anomaly anticipation (VAA), as a proactive extension beyond post-hoc detection, introduces additional challenges. In particular, the contrastive inference paradigm in VAD, which relies on ground-truth frames, is not applicable to VAA, hindering its development. To address these challenges, we propose a unified score-driven framework, termed Uni-DSM, based on denoising score matching (DSM), which models anomaly patterns through likelihood estimation and score functions over the learned data distribution. Within this unified framework, we adopt a shared noise-conditioned score transformer backbone with scene-dependent embeddings and motion-aware weighting for distribution-level modeling. Instead of introducing separate architectures, Uni-DSM unifies VAD and VAA through different inference and supervision paradigms built upon the same score-based formulation. For VAD, we instantiate an autoregressive denoising score matching (ADSM) mechanism, which progressively accumulates anomalous evidence via autoregressive denoising, enabling enhanced perception of local modes beyond visual cues. For VAA, we extend the same architecture by incorporating a lightweight auxiliary decoder and a novel self-distilled denoising score matching (SDSM) mechanism. By constructing supervision from output discrepancies instead of relying on unavailable future ground truth, our method achieves efficient training suitable or early anomaly anticipation. Extensive experiments on multiple benchmark datasets demonstrate state-of-the-art performance in both VAD and VAA while maintaining high efficiency, establishing a unified and scalable pipeline from anomaly detection to anticipation.

---


### 88. [CARE: Constrained Attention Refinement for Fine-Grained Visual Classification via Teacher-Student Distillation](https://arxiv.org/abs/2610.11153)

**<font color=#1a73e8>作者：</font>** Ruibo Wen, Hang Shao, Yiming Lei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained visual classification requires models to recognize subtle local traits while exposing the visual evidence behind their predictions. Class-specific attention pathways provide a natural basis for interpretable recognition, but their constrained prediction structure limits discriminative capacity and underuses intermediate representations from strong pretrained backbones. To address this problem, we propose CARE, a constrained attention refinement framework for interpretable fine-grained recognition via teacher-student distillation. CARE keeps the final prediction and explanation within a class-specific attention student, while introducing a training-only auxiliary query teacher that reads selected intermediate DINOv2 layers with learnable queries. The teacher fuses multi-level representations and transfers logit-standardized class-discriminative knowledge to the student. To further refine the explanation pathway, we design diversity and sparsity terms to regularize student attention heads, reducing redundancy and encouraging compact trait localization. Experiments on CUB, Oxford-IIIT Pet, Stanford Dogs, and Stanford Cars show that CARE achieves strong classification performance under an interpretable frozen-backbone setting, reaching 78.5% Top-1 accuracy on CUB. Faithfulness analysis with insertion and deletion metrics further indicates that the top-ranked attention regions retain class-relevant evidence for explanation.

---


### 89. [Social Pain Disrupts Emotion-Action Brain-State Dynamics in Adolescents with Non-Suicidal Self-Injury](https://arxiv.org/abs/2610.11155)

**<font color=#1a73e8>作者：</font>** Ying Xu, Xiaojun Liang, Li Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Non-suicidal self-injury (NSSI) is prevalent among adolescents with depression, but the rapid brain-state dynamics linking social distress to maladaptive behavior remain unclear. We combine an experimental pain paradigm, electroencephalography (EEG) microstate analysis, and interpretable deep sequence modeling to investigate NSSI-related neurodynamics in 106 adolescents with depression, including 67 with NSSI (DN+) and 39 without NSSI (DN-), during social pain, physical pain, and resting-state conditions. A model integrating disease-specific, domain-adversarial, consistency, and contrastive learning captures higher-order dependencies in microstate sequences. Social pain yields the strongest NSSI discrimination, with 68.55% accuracy, outperforming the best baseline by 8.94% points. Model interpretation and conventional microstate analyses reveal weakened bidirectional transitions between MS3 and MS5 in DN+ adolescents during social pain. Source reconstruction associates MS3 with emotional/interoceptive processing and MS5 with action preparation, suggesting disrupted emotion-action coupling. Time-resolved analyses show greater early-to-middle action-state recruitment and later emotion-state recruitment in DN+ adolescents. In DN- adolescents, MS5-to-MS3 dynamics mediate associations between social-evaluation sensitivity and affective outcomes, whereas this mediation is absent in DN+; conversely, MS3-to-MS5 transitions are associated with greater negative affect in DN+. Together, these findings identify disrupted emotion-action coupling as a key neurodynamic mechanism underlying altered social pain processing in adolescents with NSSI, providing a mechanistically interpretable neural signature for objective identification of NSSI.

---


### 90. [AutoAdapt: Reliable Few-Shot Adaptation under Clinical Distribution Shifts](https://arxiv.org/abs/2610.11162)

**<font color=#1a73e8>作者：</font>** Song Wang, Jie Peng, Davis Hobley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large pretrained clinical models provide a practical way to reuse learned prior knowledge across hospitals by adapting models to them. In practice, a target hospital may only have a small labeled patient cohort, a setting commonly referred to as few-shot adaptation. This requires making multiple decisions, such as which pretrained model to adapt, how much of the model to update, and which patients to use. Nevertheless, this process faces two primary challenges. First, the best adaptation strategy varies across clinical tasks. Second, evaluating and comparing candidate strategies becomes unreliable due to the small patient cohort. In this work, we introduce AutoAdapt with two core designs to deal with these challenges. The Adapter defines an extensible space of adaptation recipes, and the Automator forms a weighted recipe combination from evidence within the adaptation patients. We propose a reliability rule to ensure that only the most effective strategy on most available patients will be selected. These selected strategies then form a combination for effective few-shot adaptation. We conduct extensive experiments across critical care, emergency care, and diagnostic datasets, and the results show that AutoAdapt consistently achieves state-of-the-art performance using only a few patients for adaptation.

---


### 91. [RideBench: A Large-Scale Exogenous-Aware Benchmark for Ride-Hailing Time Series Forecasting](https://arxiv.org/abs/2610.11164)

**<font color=#1a73e8>作者：</font>** Shengsheng Lin, Jing Hu, Zhengyang Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We release Ride-Hailing, a large-scale ride-hailing time series dataset synthesized from DiDi's marketplace data across 200 spatial areas. Ride-Hailing spans four consecutive years at half-hourly granularity and covers three representative exogenous scenarios: Weather Disturbance, Holiday Effect, and Large-scale Event Impact. Built upon Ride-Hailing, we introduce RideBench, a comprehensive benchmark for exogenous-aware ride-hailing forecasting, covering both regular week-ahead forecasting and long-horizon 8-week-ahead forecasting with up to 2,688 prediction steps. RideBench evaluates over 30 representative forecasting methods, including endogenous-only models, exogenous-aware models, and time series foundation models. Our results show that future-known exogenous variables provide clear benefits in regular week-ahead forecasting, especially under weather, holiday, and large-scale event (e.g., major sporting events and concerts) scenarios. However, current exogenous-aware models still struggle to fully capture disturbance-induced pattern changes under complex external contexts. For long-horizon forecasting, existing models cannot simultaneously achieve low pointwise errors, accurate broad trends, and reliable near-term forecasts. These findings reveal a clear mismatch between existing forecasting models and real-world ride-hailing requirements, highlighting the need for models that can better exploit future-known exogenous information, scale across heterogeneous areas, and support long-horizon planning. By introducing Ride-Hailing and RideBench, we aim to encourage the community to study these practical challenges in real-world ride-hailing forecasting.

---


### 92. [CARE: A Lightweight Plug-in Gated Correction and Uncertainty-aware Module for Long-term Time Series Forecasting](https://arxiv.org/abs/2610.11165)

**<font color=#1a73e8>作者：</font>** Guo Cheng, Changlong Lv, Jingyi Hou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate long-horizon forecasting is critical to electricity load scheduling and traffic flow management, and to financial risk control. Existing deterministic backbones output a single trajectory, masking heterogeneous prediction difficulty across horizons and channels and providing no localized reliability signal. We present CARE (Corrective branch with Aligned context and Relative-error Estimation), a lightweight plug-in that enhances any deterministic forecaster without architectural redesign. Operating in parallel with the base model, CARE resamples historical context to match the forecast horizon, learns residual correction patterns from this aligned history, and applies scale-aware bounded updates modulated by per-coordinate sigmoid risk gates. A multi-objective loss jointly optimizes forecast accuracy, residual tracking, risk alignment, and base-model anchoring. Across eight benchmarks with three representative backbones, CARE improves accuracy with marginal parameter and latency overhead. Its risk gates reliably identify high-error regions: on Weather, the highest-gate tertile exhibits nearly four times the error of the lowest-gate tertile, offering planners an interpretable per-step trust signal. Code is available at this https URL.

---


### 93. [SACQ: Structured Decoding with Memory-Conditioned Refinement for Long-Horizon Forecasting](https://arxiv.org/abs/2610.11170)

**<font color=#1a73e8>作者：</font>** Guo Cheng, Zhengzhuo Xu, Chenchen Jing 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term time series forecasting (LTSF) models predominantly employ patch-based encoders terminated by a flatten readout head that maps the entire encoded historical memory to all future steps through a single shared projection. This implicit coupling of future positions obscures position-specific historical-to-future alignment and amplifies sensitivity to corrupted inputs and extreme supervision noise. We present SACQ, a plug-in structured prediction head that replaces flatten readout while keeping the encoder unchanged. SACQ adopts a two-stage decoding pipeline: it first establishes a coarse patch-grid forecast scaffold, then refines each future position through cross-attention over historical memory and merges the attention-derived correction with the coarse scaffold via a learned per-patch gate. To stabilize optimization under long horizons and noisy labels, we further propose a batch-adaptive scaled log-cosh loss that automatically calibrates robustness to the current residual scale, suppressing outlier gradients while preserving MSE-like sensitivity for typical errors. SACQ attains top-tier test MSE/MAE across PatchTST, DLinear, and patch-Mamba backbones with only modest incremental overhead in parameters and latency. Under inference-time input corruption and training-set label-noise stress tests, SACQ substantially outperforms flatten readouts, with ablation studies validating each architectural component.

---


### 94. [VAMR: Multi-Question Agentic Reasoning for Efficient Long-Form Video Understanding](https://arxiv.org/abs/2610.11171)

**<font color=#1a73e8>作者：</font>** Runquan Gui, Hanzhu Chen, Zehao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-form video understanding often involves multiple questions about different aspects of the same recording. Yet existing video agents typically process each question through an isolated tool-use trajectory. This repeatedly restarts video exploration and memory construction, missing opportunities to acquire evidence jointly and progressively build a shared understanding that supports the complete question set. We introduce \textbf{VAMR} (\textbf{V}ideo \textbf{A}gent for \textbf{M}ulti-Question \textbf{R}easoning), which coordinates all questions about a video through one shared tool-use trajectory. At each round, a persistent policy model can invoke tools for one or more unresolved questions and submit answers for questions with sufficient evidence. Question-conditioned visual perception retrieves fine-grained clues for several questions in one call, while layered multi-question memory integrates reusable context into a shared video story and preserves separate evidence for individual questions. After supervised fine-tuning initializes this interaction protocol, we propose question-horizon policy optimization (\qhpo) to optimize shared trajectories in which questions progress and finish at different rounds. Specifically, a question-level critic estimates the value of each active question, while round alignment maps each question advantage to the rounds that directly serve it before the aligned advantages are aggregated to optimize the shared actor. Across LVBench, Video-Holmes, and LongVideoBench, VAMR achieves the highest accuracy overall and the fewest reasoning rounds among iterative methods. On LVBench, it reaches 62.1\% accuracy, exceeding VideoARM by \textbf{4.3} points while reducing reasoning rounds and processed frames by \textbf{85.9\%} and \textbf{61.4\%}.

---


### 95. [IntactWorld: Joint World Modeling with Intact Features](https://arxiv.org/abs/2610.11174)

**<font color=#1a73e8>作者：</font>** Boming Tan, Xiangdong Zhang, Yan Xia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent video generation models synthesize highly realistic visuals, they lack a genuine understanding of intrinsic real-world logic. Existing methods attempt to understand the world by internalizing diverse world knowledge, yet constrained by computational overhead or dimensionality alignment, their learning processes inevitably compress features, causing a severe loss of structural information. To address this, we propose \textbf{IntactWorld}, a \textbf{Joint World Modeling Architecture} utilizing uncompressed \textbf{Intact Features}. Since data naturally reside on a low-dimensional manifold within a high-dimensional space, predicting the flow velocity $v$ within this uncompressed high-dimensional space induces a severe manifold gap. To successfully eliminate this optimization bottleneck, our framework instead predicts the clean feature $x_0$ at intermediate layers. Furthermore, to mitigate the computational overhead of incorporating complete world knowledge, we introduce a \textit{Full-to-Compact Training Paradigm}. By replacing raw full features with highly refined CLS tokens, this paradigm enables efficient single-branch guidance, reducing spatial memory consumption by 11.4\% and cutting inference latency by 43.8\%. Extensive evaluations demonstrate the effectiveness of IntactWorld, outperforming established baselines by 2.46 points on the VBench 2.0 benchmark.

---


### 96. [Multimodal Remote Sensing Image Registration: A Comprehensive Review, Challenges and Prospects](https://arxiv.org/abs/2610.11176)

**<font color=#1a73e8>作者：</font>** Zhiqiang Han, Yuanxin Ye, Qiuyun Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal remote sensing image registration is a crucial prerequisite for the collaborative processing and downstream application of remote sensing data, such as image fusion, change detection, and target recognition. However, significant variations in radiometry, geometry, scale, viewpoint, and time often exist between multimodal images. These differences, driven by varying sensor geometries, physical radiation mechanisms, imaging platforms, and environmental disturbances, pose severe challenges to achieving high-precision, robust registration. This paper systematically reviews the progress of mainstream multimodal remote sensing image registration methods. Based on their registration pipelines, existing approaches are categorized into three main types: region-based, feature-based, and deep learning-based methods. We detail the core principles, representative algorithms, advantages, and limitations of each category. Additionally, we summarize publicly available multimodal image datasets in the remote sensing domain, analyzing their specific characteristics and applicable scenarios. Finally, we highlight current bottlenecks in high-precision registration research and outline future development trends. This review aims to provide a comprehensive reference and valuable insights for researchers in related fields.

---


### 97. [MATE4D: Matrix-Guided Editable 4D Generation from a Single Image](https://arxiv.org/abs/2610.11181)

**<font color=#1a73e8>作者：</font>** Xiaotian Chen, Dongfu Yin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models have rapidly pushed content creation be-yond 2D imagery toward dynamic 3D and 4D scene synthesis. Yet pro-ducing realistic and temporally stable 4D content from a single image is still difficult because one view provides limited structural cues and weak motion evidence. We introduce MATE4D, a framework that converts one input image into editable dynamic 4D content. Our method constructs a spatio-temporal multi-view image matrix with text-guided background manipulation, delivering coherent supervision over viewpoint, appear-ance, and motion. These synthesized observations are used to optimize 3D Gaussian primitives, which are then animated through a lightweight deformation module to form a 4D representation. The resulting scenes preserve geometry more faithfully, maintain smoother temporal behavior, and keep background edits more consistent, reducing context ambiguity and motion artifacts. Experiments on Objaverse-XL and Diffusion4D show that MATE4D outperforms strong baselines in visual quality, effi-ciency, and controllability, supporting practical AR/VR content creation.

---


### 98. [WorldFact-Bench: Beyond Image-Internal Plausibility to Image-World Consistency](https://arxiv.org/abs/2610.11184)

**<font color=#1a73e8>作者：</font>** Zhuohong Chen, Zhengxian Wu, Yunyao Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in image generation have made visual authenticity increasingly difficult to assess. Although image forensics now examines both generation artifacts and higher-level visual inconsistencies, a plausible image can still contradict real-world facts or rules. We introduce WorldFact-Bench to evaluate image-world consistency from a single image, without a predefined claim or verification target. The benchmark contains 1,274 source-aligned real-fake pairs across four verification regimes and ten semantic domains. Each pair introduces a specific, evidence-supported factual conflict while seeking to preserve non-target content and visual plausibility. Images are evaluated independently, and pair accuracy requires both members of a pair to be classified correctly. We further propose PERSIST-Agent, which organizes iterative verification around a persistent state linking candidate facts, visual observations, evidence, and verification statuses. This state guides subsequent inspection and retrieval while retaining unresolved candidates. With backbone weights fixed, harness self-optimization refines the agent's prompts and execution rules through validation feedback. Experiments reveal strong label biases in several detectors and uneven gains from retrieval. On the evaluated 8B backbones, PERSIST-Agent improves pair accuracy over both direct judgment and retrieval-augmented baselines, while ablations support the role of persistent verification state. These findings highlight the value of state-guided verification and the remaining gap between visual plausibility and factual correctness.

---


### 99. [Predictive Multiplicity in Cell-Fate Assignment: Label-Free Rashomon Sets and the Limits of Per-Cell Certification](https://arxiv.org/abs/2610.11185)

**<font color=#1a73e8>作者：</font>** Arjun Bhupatiraju, Abhiram Bhupatiraju  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell trajectory inference maps transcriptomic measurements onto developmental continua, yet configurations that fit the data equally well can assign conflicting cell fates. FateMultiplicity is a label-free framework that constructs a statistically admissible model set, or Rashomon set, without lineage labels, by evaluating model discrepancy on cross-fitted held-out genes under non-inferiority testing calibrated against random-seed variation. Multiplicity is large and depends more on the diversity of the model space than its size: twelve configurations of a second algorithm expose 20.0% of cells where twenty-four of the first expose 3.8%. Whether the per-cell certified fate margin FM yields more reliable assignments than the fitted model already provides is then tested, and it does not. On simulation ground truth, on the same cells, FM discriminates misassignment at AUC 0.682, against 0.965 for the baseline configuration's own decision margin (p = 0.003) and 0.854 for a seed-dispersion baseline. Informativeness is governed by the breadth of the admitted set, not its cardinality: at cardinality four, seed refits give 0.933 and hyperparameter-perturbed sets 0.701. Relaxing the infimum to a q-quantile recovers discrimination but converges toward the single model's own confidence; the supremum reaches 0.973 because theta*'s membership bounds it from below, while the infimum is unanchored. Multiplicity in trajectory inference is worth measuring and reporting, but per-cell certification over a label-free Rashomon set is not a route to more reliable fate calls. Two constructions survive: a margin-erosion ratio separates real from spurious branch points in simulation (AUC 0.890, untested on real data), and against clonally observed fate, uncertified cells disagree with their clone's outcome 16.4 percentage points more often than certified cells (p < 0.001).

---


### 100. [RGBD-to-3D Object Mesh Refinement via Depth Matching and Symmetry Propagation](https://arxiv.org/abs/2610.11187)

**<font color=#1a73e8>作者：</font>** Ahyun Seo, Minsu Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-view 3D reconstructors often produce plausible meshes that disagree with the input view, especially near depth discontinuities and self-occlusions. We present a lightweight, plug-and-play RGBD-to-3D refinement that improves any RGB-to-3D reconstructor without retraining. Given a depth map, we correct the visible surface by bipartite matching to back-projected depth points, mirror these corrections onto the occluded side across a detected symmetry plane, and propagate them with a smoothness solver. Every stage is closed-form, making the method orders of magnitude faster than optimization-heavy test-time refinement. On GSO and OmniObject3D with five backbones, it yields consistent gains, also with monocular pseudo-depth, benefits more from symmetry on symmetric objects, and compares favorably with prior refinement in accuracy and runtime. It further improves an RGB-D-to-mesh reconstructor and transfers to real captures with noisy sensor depth.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-329](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
