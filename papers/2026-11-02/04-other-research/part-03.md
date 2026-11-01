# 📦 其他研究 | 2026年11月02日

> 本类共 **432** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

---

### 101. [Transportable Offline Reinforcement Learning in Presence of Unmeasured Confounding](https://arxiv.org/abs/2610.38253)

**<font color=#1a73e8>作者：</font>** Junyi Liao, Hangqi Ren, Zhuoran Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning seeks to learn decision policies from previously collected data, but deployment environments may differ from the domains in which the data were collected, and logged variables may omit confounders that affected both historical actions and outcomes. We study offline policy learning under the joint challenges of domain discrepancy and unmeasured confounding, where multiple heterogeneous source datasets provide complementary information about a target domain. We develop a causally adjusted transportability framework combining transportability theory with instrumental variables, negative controls, and proxies to identify target-domain causal quantities. For confounded contextual bandits, identification reduces to systems of bridge-function integral equations, enabling minimax estimation from finite samples. Confidence sets for the identified quantities are then used for pessimistic policy optimization, yielding CAT-CCB. We extend the framework to episodic confounded Markov decision processes, where complementary sources identify target reward and transition mechanisms under structural and completeness conditions. Under Gaussian dynamics and linear function approximation, this yields CAT-CMDP. We establish high-probability finite-sample suboptimality guarantees that quantify the effects of approximation, estimation, source-to-target shift, offline coverage, and sample size. For bounded finite-dimensional linear classes, the contextual-bandit guarantee recovers the standard $\widetilde{\mathcal O}(N^{-1/2})$ rate. Numerical experiments support the effectiveness of the framework for learning target-domain policies from heterogeneous confounded data. Together, the results provide a principled approach when no single source dataset suffices for causal identification and policy optimization.

---


### 102. [ETA-Motion: Efficient Topology-Agnostic Motion Diffusion via Sparse Joint Learning](https://arxiv.org/abs/2610.38259)

**<font color=#1a73e8>作者：</font>** Seoyoung Hwang, Tae-Kyun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Topology-agnostic motion generation aims to synthesize motions for diverse characters with arbitrary skeletons. Unlike conventional motion generation, which assumes a fixed skeletal template, this setting must handle diverse joint configurations and inconsistent joint semantics across characters. Existing methods address this challenge through dense full-joint modeling, which incurs substantial computational cost and hinders learning transferable motion patterns across diverse skeletal topologies. We present ETA-Motion, a topology-agnostic motion generation framework based on sparse joint learning. Instead of learning motion from all joints, our method uses a compact subset of joints to reduce redundancy and trains the motion generator on the resulting sparse skeleton. To facilitate correspondence across diverse topologies, we introduce semantic joint embeddings that combine textual and visual cues, together with topology-aware training objectives for preserving skeletal structure. Although ETA-Motion is trained only on sparse skeletal observations, it supports full-skeleton motion generation during inference. Experimental results demonstrate that ETA-Motion outperforms existing topology-agnostic baselines while significantly improving efficiency and generalization to unseen motions and unseen topologies.

---


### 103. [Rosemary: Efficient and Adaptable In-Storage Acceleration for Fully Homomorphic Encryption](https://arxiv.org/abs/2610.38262)

**<font color=#1a73e8>作者：</font>** Xuan Wang, Tianqi Zhang, Gabrielle De Micheli 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully Homomorphic Encryption (FHE) enables computation on encrypted data and is promising for privacy-preserving computing. However, FHE deployment remains constrained due to massive computational, memory, and data-movement overheads. Existing acceleration strategies often overlook the storage I/O bottleneck caused by the enormous size of FHE data in large-scale applications, as most prior works focus on small benchmarks that fit in main memory. Our studies show that state-of-the-art FHE systems spend 71\% to 85\% of their execution time moving data between storage and compute units rather than performing useful computation. To address the I/O bottleneck, we present Rosemary, a heterogeneous FHE acceleration system that incorporates a novel in-storage processing (ISP) architecture with compiler-level and algorithmic optimizations. Our key innovations include 1) an adaptable hardware-aware FHE engine inside a NAND flash-based solid-state drive (SSD) for efficient and cost-effective in-storage FHE processing, 2) a Throughput-Data-Aware Program Allocator (TDAP) that partitions FHE workloads into heterogeneous programs, and 3) a Compiler-Level Ciphertext-Aware Optimizer (CLCAO) that exploits ISP-friendly FHE kernels for low-cost ISP execution. Across a diverse set of FHE workloads, including encrypted deep learning inference and cloud database queries, Rosemary achieves geometric-mean speedups of $185.7\times$ over state-of-the-art CPU/GPU implementations and $3.7\times$ over prior FHE accelerators, while improving energy efficiency by up to $3.9\times$ and Energy-Delay-Area-Product (EDAP) by up to $16.5\times$.

---


### 104. [TreemapMix: Dirichlet-Controlled Multi-Image Augmentation for Probability and Ordinal Supervision](https://arxiv.org/abs/2610.38265)

**<font color=#1a73e8>作者：</font>** Ejafa Bassam, Konstantin Garbers, Yingsheng Geng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data augmentation improves visual recognition by exposing models to synthetic training examples that encourage generalization beyond the observed data. Mixed-sample methods extend this idea by combining multiple images. However, many common approaches either mix only pairs of images or rely on fixed small layouts, limiting control over source count, visible area proportions, and induced supervision. We propose TreemapMix, a distribution-controlled multi-image augmentation that samples source weights from a Dirichlet distribution and assigns them to area-proportional regions using a treemap partition. The resulting known region areas support two complementary objectives. TreemapMix with soft cross-entropy (SCE) treats areas as soft class-probability targets, while TreemapMix with a Plackett-Luce (PL) objective converts areas into ordinal supervision. On ImageNet-1K under matched training recipes, TreemapMix-SCE achieves substantially lower calibration error than evaluated mixed-sample baselines, while TreemapMix-PL achieves the strongest Top-1 accuracy. Transfer experiments on object detection and instance segmentation suggest that TreemapMix-pretrained features remain useful beyond classification. These results show that controlled multi-image composition can expose the same region-area information as either probability-matching or rank-matching supervision. Code is available at this https URL.

---


### 105. [A Hybrid Physics-informed holomorphic neural networks Method](https://arxiv.org/abs/2610.38269)

**<font color=#1a73e8>作者：</font>** Zhijie Su, Qiaolin He, Zhiping Mao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed holomorphic neural networks (PIHNNs) exploit complex-analytic representations to satisfy homogeneous PDEs by construction, but their extension to nonhomogeneous problems is nontrivial. We propose a hybrid physics-informed holomorphic neural network (HPIHNN) framework based on a decomposition of the solution into particular and homogeneous components. The particular component is computed by a spectral method on a simple extended domain, while the homogeneous component is approximated by a PIHNN trained only on the boundary with modified boundary data. The resulting formulation avoids meshing complex geometries and retains the dimensionality-reduction advantage of holomorphic representations. The method is applied to nonhomogeneous Poisson, Stokes, biharmonic, linear elasticity, and Helmholtz equations. Numerical experiments covering complex geometries, corner singularities, and nearly incompressible regimes demonstrate that the proposed method accurately resolves the corresponding solutions and, in the considered tests, generally achieves lower errors and shorter training times than standard PINNs. The results indicate that coupling spectral particular solutions with holomorphic neural approximations provides an efficient approach to nonhomogeneous PDEs on complex domains.

---


### 106. [NAGO: Noise-Aware Generative Operator via Flow Matching](https://arxiv.org/abs/2610.38273)

**<font color=#1a73e8>作者：</font>** Guanyu Chen, Shengze Xu, Pengwei Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce NAGO, a noise-aware generative operator for efficient sampling from invariant measures of stochastic partial differential equations (SPDEs) in function space. Our central idea is to treat the source measure as a design variable rather than a fixed Gaussian default. We establish admissibility conditions for well-defined infinite-dimensional flows and show that the finite-band source--target covariance ratio controls the spectral stiffness of the marginal velocity field. This analysis yields an admissibility-constrained spectral-matching rule: choose a source that is sufficiently rough for well-posedness, then minimize covariance mismatch over the resolved Fourier modes. On three representative stochastic-field benchmarks, this source design improves few-step spectral accuracy and several complementary distributional and physical statistics. In a controlled Matern-field ablation, it reduces the accurate RK4 budget from about 30 steps for Gaussian functional flow matching to 3--5 steps, a $6$--$10\times$ reduction in neural ODE evaluations. These gains are strongest for stationary multiscale fields and depend on the metric, resolution, and guidance protocol.

---


### 107. [BudSplat: Feed-forward 3D Gaussian Splatting under a Rendering Budget](https://arxiv.org/abs/2610.38278)

**<font color=#1a73e8>作者：</font>** Muyu Xu, Fangneng Zhan, Yu Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting has recently emerged as a promising alternative to per-scene optimization, enabling fast novel view synthesis by predicting Gaussian primitives directly from input images. However, it quickly faces a bottleneck of rendering efficiency while scaling from sparse to dense multi-view inputs, which offer more geometric constraints but produce a rapidly growing set of candidate Gaussians. Existing solutions cannot reliably distinguish redundant primitives, leading to many redundant primitives from repeatedly observed regions and increased rendering cost without much gain in visual quality. We propose BudSplat, a compact feed-forward 3DGS framework that learns to keep the most valuable Gaussians under a limited primitive count. BudSplat has two novel designs. The first is a detail-aware importance score that is extracted from multi-level visual tokens, providing an explicit cue for regions where pruning is likely to harm perceptual quality. The score can be injected into voxel fusion to preserve high-value local contributors during multi-view aggregation. The second is quality-aware Gaussian pruning that selects a compact set of primitives by jointly considering rendering contribution and detail importance. The quality-aware pruning enables local quota redistribution that helps avoid over-allocating primitives to large redundant regions. Experiments on RE10K, DL3DV, and ACID show that BudSplat achieves a favorable trade-off among rendering quality and efficiency.

---


### 108. [Human Evaluation with Automatic Scores: Separating Sampling and Estimation Gains](https://arxiv.org/abs/2610.38282)

**<font color=#1a73e8>作者：</font>** Yang Liu, Ran Zou, Zhengtao Gui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic judges offer inexpensive information about model outputs, but an evaluation team must decide how to turn that information into fewer human annotations. Scores can guide sampling, correct an estimate, or support adaptive acquisition, and these uses may capture overlapping gains. We compare their incremental value on fixed evaluation pools from three preference datasets, and 19 attributed-question-answering systems. Matched comparisons use the same scores, account for pilot labels and budget rules, and separate acquisition from estimation. Score stratification is a strong reference: after ten-bin stratification, the best fixed local linear correction offers only 1.00--5.27% further MSE reduction in the primary configurations. Unequal allocation offers larger gains in some pools, but can increase error when confident scores conceal variable human outcomes. Comparison on AttributedQA, shrinking learned quotas toward score-only quotas lowers pooled MSE for 17 of 19 systems relative to the score-only procedure, but ordinary pooled 95% intervals cover only 88.09--93.54%. The same shrinkage improves on the score-only reference in only one of eight preference configurations. Ranking experiments further show that lower individual MSE need not improve system selection. These findings support a simple starting procedure, proportional sampling within score strata followed by a stratified human mean, and identify what additional evidence is needed to justify correction or adaptation for the intended evaluation output.

---


### 109. [ConvRoute-ViT: Convolutional Token Routing for Efficient Vision Transformers](https://arxiv.org/abs/2610.38284)

**<font color=#1a73e8>作者：</font>** Manish Das, Shiv Ram Dubey, Satish Kumar Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) achieve strong image recognition performance, but their self-attention increases quadratically with the number of input tokens and makes them computationally expensive. The standard implementation of ViT models treats all patch tokens with equal importance across every layer of the model. This uniform treatment introduces redundant computation and may reduce the model's focus on the most discriminative object regions. In this paper, we propose ConvRoute-ViT, a convolutional token routing mechanism for efficient vision transformers that performs token reduction through convolutional routing. Our model preserves the most relevant patch tokens according to class-token attention at selected layers, while the remaining tokens are spatially reorganized and compressed into a compact set of convolutional summary tokens. This design reduces the sequence length without completely removing the contextual information of the less informative tokens. By applying the routing process hierarchically, the proposed framework constructs compact and discriminative representations for deeper layers. Experiments on CIFAR-100 and TinyImageNet show that ConvRoute-ViT improves computational efficiency while maintaining classification accuracy compared with the base ViT.

---


### 110. [PulmoWorld: An Asynchronous Multimodal Medical World Model for Longitudinal Pneumonia Dynamics](https://arxiv.org/abs/2610.38289)

**<font color=#1a73e8>作者：</font>** Cheng Tang, Xinyu Zhang, Jiawei Chen 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pneumonia changes across respiration, inflammation, and organ function, while the measurements that describe it arrive at different times and are often incomplete. We introduce PULMOWORLD, a world model for longitudinal pneumonia dynamics that connects asynchronous state estimation, recursive simulation, and evidence-constrained planning. History-aware filtering separates state propagation from observation-driven correction, so a measurement updates the shared belief only when it is observed. That belief supports recursive forecasts of clinical values and modality representations, and summaries of future prognosis. Cap-MBRL searches imagined continuations inside an authorized action set and replaces a frozen fallback only when a candidate meets the risk budget and a predicted-cost margin. On the pneumonia cohort MASS, recursive forecasts are competitive with task-trained sequence models, and simulated future states retain prognostic information. Trained separately on public MIMIC-IV-CXR chest radiographs and clinical trajectories, this model improves prognostic discrimination over latest-value fusion in development and is competitive on long-horizon error on the locked pneumonia panel. In five known-mechanism MASS-Syn environments, Cap-MBRL lowers selection regret relative to direct fallback execution.

---


### 111. [Inner-Learning: From Hand-Coded Beliefs to Declarative Knowledge in Trick-Taking Games](https://arxiv.org/abs/2610.38304)

**<font color=#1a73e8>作者：</font>** Stefan Edelkamp  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a declarative approach to belief-state modeling in trick-taking card games. Starting from a state-of-the-art Skat player, we automatically extract its hand-coded inference rules into a domain-specific language built on the primitive $\neg\mathsf{holds}(P,C)$, denoting that player $P$ cannot hold any card in set $C$. Round-trip code generation verifies that the extracted rules reproduce the original engine's intended behavior, up to three audited bugs in the original that the declarative engine corrects. We then grow the rule base through symmetric derivation and annotation of an expert strategy document---unifying code, symmetry, and expertise in one representation. We extend the knowledge representation with \emph{cardinality constraints}: at-most-$k$ and at-least-$k$ bounds on the cards a player holds from a named group, expressed in the same declarative language and enforced at world-generation time. Confidence parameters connect symbolic rules to probabilistic belief updates. Self-play evaluation shows the declarative engine measurably improving winning percentage and score over the original hand-coded engine, with the extracted rules, the human-annotated rules, and the cardinality constraints each contributing to the effect.

---


### 112. [Does 3D Pose Improve Action Valuation in Football? An Empirical Study of Pose Representations and Learning Objectives](https://arxiv.org/abs/2610.38308)

**<font color=#1a73e8>作者：</font>** Rikuhei Umemoto, Kenjiro Ide, Soham Majumder 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Football action valuation estimates players' contributions to future scoring. Existing multi-agent deep reinforcement learning (MADRL) models use 2D positions and velocities, omitting posture information relevant to imminent actions. We investigate whether adding 3D pose to a SARSA-based model improves observed-action values relative to attack returns: goals, conceded goals or final expected possession value. Using UEFA Champions League 2022/23 event, tracking and 3D pose data, we compare six representations (no pose, raw joints, torso and head orientation, and spatial-temporal graph convolutional network (ST-GCN) embeddings) across five learning settings and three seeds. The settings vary temporal-difference targets and action-prediction loss, with Monte Carlo return regression as a reference. Across 50 on-ball and off-ball comparisons, pose robustly improved return prediction in only three, all using torso and head orientation, while worsening it in twelve, mostly with ST-GCN. Training choices had greater effects: removing the action-prediction loss raised on-ball skill of position-only values from 0.003 to 0.040 and their correlation with expected goals from 0.23 to 0.60; the improvement in return prediction persisted at matched training length. Separately, pose improved prediction of the on-ball action 0.2 s ahead (macro AUC 0.914 to 0.934 with raw joints), while the passer's pose during execution improved pass-success prediction (AUC 0.844 to 0.856). Within this training protocol, pose informed imminent actions but rarely improved observed-action values.

---


### 113. [Game-Theoretic Foundations for Undiscounted Bisimulation Metrics](https://arxiv.org/abs/2610.38313)

**<font color=#1a73e8>作者：</font>** Matthew Zurek, Yudong Chen, Josiah P. Hanna  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bisimulation metrics offer a principled notion of task-relevant state similarity in reinforcement learning, but existing constructions and methods are largely confined to discounted MDPs, where contraction arguments ensure well-defined fixed points and downstream guarantees. We develop a unified foundation for bisimulation metrics in undiscounted settings, that is total- and average-reward problems, by replacing the standard operator-centric view with a game-centric one: we interpret prior metric operators as Bellman-Shapley operators of zero-sum turn-based games and define metrics as the corresponding game value functions, yielding unique definitions even when $\gamma=1$. This game-theoretic foundation facilitates transfer of dynamic-programming theory and algorithms. We also use this game-centric perspective to characterize how metric finiteness depends on structural properties of the underlying MDP and motivate certain directed metrics that remain finite in weakly communicating MDPs. We further introduce an abstract framework for modifying the games' action spaces, allowing general transition coupling sets, that recovers many existing metrics and guides new constructions. Finally, we prove that these metrics bound total-reward and, when the optimal gain is state-independent, optimal relative value differences. We also provide error and suboptimality guarantees for aggregation-based planning in total- and average-reward settings.

---


### 114. [Extremely Sparse-View Computed Tomography from 2D Projections via Pose-Aware Diffusion Priors](https://arxiv.org/abs/2610.38319)

**<font color=#1a73e8>作者：</font>** Linrui Dai, Jinxiu Liang, Chu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extremely sparse-view computed tomography (xSV-CT) is critical when scanning time, motion, or radiation tolerance limits each scan to only a few projections. In many such scenarios, the same acquisition limits also constrain dataset construction, making pre-reconstructed 3D volumes from dense scans unavailable. This exposes a gap in current sparse-view approaches: Optimization-based methods, which use the sparse measurements directly but lack data-driven priors to suppress artifacts, and learning-based methods, which use strong priors but usually require densely scanned training volumes acquired outside the xSV-CT regime. We study this train-sparse / infer-sparse setting by learning a pose-aware diffusion prior from one 2D projection per training sample, then guiding diffusion sampling with measured-view fidelity, shared-volume reprojection, and projection-physics consistency for tomographic reconstruction. On two public CT datasets across 1-, 4-, and 8-view settings, the proposed method achieves the best novel-view synthesis scores and best or competitive reconstruction quality compared with baselines that use dense-volume supervision.

---


### 115. [SSQA: Sibling-Selective Quadtree Attention for Hierarchical Modeling in Perception Tasks](https://arxiv.org/abs/2610.38320)

**<font color=#1a73e8>作者：</font>** Yufan Chen, Arnav Bali, Angela Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perception tasks for navigation in robotics, including aerial platforms such as drones and autonomous driving systems, are inherently structured. Drone-mounted cameras typically capture sky above, terrain below, and obstacles or man-made structures in between, while driving data often contains organized road layouts, lane markings, and surrounding agents. Motivated by these axis-aligned structural priors, we note that such information is typically more structured than in generic image tasks. We hypothesize that processing information in a quadtree-esque manner can not only model features effectively in a hierarchical manner, but also offers an efficient linear-time alternative to vanilla attention mechanisms, which run in quadratic time. In this paper, we propose Sibling-Selective Quadtree Attention (SSQA), which models image tokens hierarchically as a structured, full quadtree. We show analytical complexity analysis that guarantees linear-time feature modeling, in addition to empirical experiments comparing inference speeds with other popular modeling approaches, such as Mamba 2 and Quadtree Attention. Our results, benchmarked across several tasks, show that we achieve results at least as good, if not notably better, as others at a fraction of the computational costs.

---


### 116. [Optimal Regret for Communication-Efficient Decentralized Online Learning](https://arxiv.org/abs/2610.38334)

**<font color=#1a73e8>作者：</font>** Sifan Yang, Wenhao Yang, Wei Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we investigate decentralized online convex optimization with compressed communication, where $n$ learners over a network jointly minimize a sequence of global loss functions based only on their local losses and compressed messages from their neighbors. The best known regret bounds for this problem are $O(\omega^{-1/2}n\rho^{-1}\sqrt{T\ln n})$ and $O(\omega^{-1}n\rho^{-2}\ln n\ln T)$ for convex and strongly convex loss functions, respectively, where $\rho\in(0,1)$ is the spectral gap of the communication matrix and $\omega\in(0,1]$ is the compression quality factor. Compared with the corresponding lower bounds of $\Omega(\omega^{-1/2}n\rho^{-1/4}\sqrt{T})$ and $\Omega(\omega^{-1}n\rho^{-1/2}\ln T)$, these upper bounds exhibit polynomial gaps in their dependence on $\rho^{-1}$. To close these gaps, we first develop Ascent-gossip, which combines an online compression strategy with a Chebyshev recursion and attains a faster consensus rate than existing compressed gossip methods. Furthermore, by adopting Ascent-gossip, we propose an online algorithm that achieves optimal regret bounds of $\widetilde O(\omega^{-1/2}n\rho^{-1/4}\sqrt{T})$ and $\widetilde O(\omega^{-1}n\rho^{-1/2}\ln T)$ for convex and strongly convex loss functions, respectively. Up to logarithmic factors in $n$ and $\rho^{-1}$, these results match the lower bounds in terms of $T$, $n$, $\rho$, and $\omega$.

---


### 117. [Aligning Misaligned Benchmarks for Single-View Novel View Synthesis](https://arxiv.org/abs/2610.38349)

**<font color=#1a73e8>作者：</font>** Yang-Che Tseng, Erqun Dong, Jeong-gi Kwak 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While single-view novel view synthesis methods have been dramatically enhanced recently, how to quantify their performance has yet to be standardized. In this work, we demonstrate that an important factor lies in how each method's own reference frame is aligned with the so-called ground-truth pose. Existing methods often rely on test-time optimization of target poses for this alignment, which inherently is ill-posed due to the complexity of the optimization landscape of camera poses vs render accuracy, leading to methods being evaluated at an arbitrary local optimum. Some recognize this limitation and thus rely on 3D reconstructions of entire scenes using training and test views to align poses, which may be infeasible. In this work, instead, we propose to use traditional 2D-to-2D and 2D-to-3D image matching techniques to align 3D reconstructions. We also evaluate only within co-visible regions, between different views, which is the only place where a `correct' ground truth can be defined. Our evaluations show that with proper coordinate alignment, novel-view synthesis methods that use explicit 3D Gaussians achieve the state of the art, despite being previously reported in the literature to be outperformed by pure image-based 2D methods. We further provide a simple baseline that directly utilizes an off-the-shelf video generator and a feed-forward geometry estimator. Our simple baseline is already comparable to state-of-the-art methods specifically trained for novel-view synthesis, without any task-specific training.

---


### 118. [Volley3D: Unified 3D Full-Sequence Reconstruction from Monocular Broadcasts](https://arxiv.org/abs/2610.38358)

**<font color=#1a73e8>作者：</font>** Noâm Boussouf, Adrien Maglo, Mohamed Chaouch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D reconstruction from single-view sports broadcast is a pivotal capability for automated analytics and immersive AR/VR replays, yet notoriously ill-posed due to difficult-to-calibrate moving cameras and depth ambiguity. Unlike widely studied racket sports, team sports such as volleyball feature unpredictable multi-contact sequences and high altitude jumps. These dynamics categorically invalidate the standard planar projection assumptions relied upon by existing methods. To resolve these limitations without 3D training supervision, we propose a complete, physics-grounded pipeline tailored to monocular broadcast volleyball. First, we include a correction module to the perspective drift induced by ground-plane projection by coupling temporal jump spotting with Newtonian interpolation for 3D player placement. Second, for 3D ball trajectory estimation, we design a dedicated sub-trajectory segmentation architecture alongside a collision-matching algorithm. By anchoring physical equations to reconstructed 3D hand vertices, we lift noisy ball 2D detections into a spatiotemporally coherent 3D scene. Evaluations on multi-camera benchmarks demonstrate our approach significantly reduces 3D spatial drift compared to 2D-reprojection baselines.

---


### 119. [SparseTokenGS: Gaussian-based Sparse-View CBCT Reconstruction via Reusable Token Pool](https://arxiv.org/abs/2610.38360)

**<font color=#1a73e8>作者：</font>** Zihan Deng, Zhenzhen Gong, Yujie Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view cone-beam computed tomography is widely used for fast, low-dose volumetric imaging and lesion localization in dentistry and image-guided interventions, but it introduces severe artifacts. Feed-forward Gaussian methods transfer the reconstruction cost to training and decode each coordinate from projection-aligned features and neighboring anchors. However, information from the whole scan is written only when the field is constructed and cannot be retrieved during coordinate decoding, leaving the volume inconsistent within the scan. This is a common limitation of such methods: once the field is fixed, decoding uses only local features and reconstruction quality drops substantially. We propose SparseTokenGS, a Gaussian-based method for sparse-view cone-beam computed tomography reconstruction via a reusable token pool. Anchor Token Fusion and Point-Token Attention query this shared pool at the anchors and at the query coordinates, respectively. The local Gaussian prior is retained, and the volume is reconstructed in one forward pass, without per-scan optimization or a projection-domain loss. On three public chest and dental datasets, SparseTokenGS achieves the highest reconstruction performance among the compared methods. On clinical dental scans, reconstruction from only six projections reaches 29.51 decibels in peak signal-to-noise ratio and a structural similarity of 0.842 against the full-view reference, and off-the-shelf tooth-and-pulp segmentation keeps these structures separable for root-canal localization. Experiments on volcanic rock and chicken show performance after same-object adaptation. A reusable token pool gives feed-forward reconstruction a mechanism that keeps scan-wide context available through decoding and can benefit future rapid clinical lesion localization and analysis. The code is available at: this https URL.

---


### 120. [Governance-Aware Federated Learning for Multi-Agent AI Systems: A Policy-Driven Framework for Trustworthy Collaborative AI](https://arxiv.org/abs/2610.38411)

**<font color=#1a73e8>作者：</font>** Kiranmayee Janardhan, Karthick S, Madhusmita Panda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative model training without exchanging raw data, but conventional FL provides limited runtime governance, evidence verification, fairness assessment, explainability monitoring, and auditability. This paper proposes Governance-Aware Federated Learning (GAFL), which combines independent governance-evidence verification, temporal trust, fairness and explanation assessment, anomaly detection, policy enforcement, normalized aggregation, and tamper-evident audit logging. Client-reported governance values are authenticated, bound to their submitted model updates, and independently recomputed before aggregation. A cross-silo prototype with 10 participants was evaluated on the Adult Income dataset under honest, benign non-IID, biased-data, malicious-update, non-compliant, falsified-evidence, and mixed-threat scenarios. Four methods were compared across five random seeds: FedAvg, FedAvg with anomaly filtering, GAFL without independent verification, and complete GAFL. Complete GAFL intervened on all affected participants at the final round across the evaluated risk scenarios, including identifying 100% of falsified-evidence participants, whereas GAFL without verification identified none of the falsified-evidence participants. Final macro-F1 ranged from 0.7520 to 0.7733 across GAFL scenarios. Complete GAFL required 173.67 plus or minus 26.94 ms of governance processing per round, compared with 3.82 plus or minus 0.79 ms for FedAvg. A strict demographic-parity threshold also caused frequent interventions for honest participants, demonstrating a significant fairness-policy and utility trade-off.

---


### 121. [Structure-retained low-rank adapters for weather synthesis](https://arxiv.org/abs/2610.38413)

**<font color=#1a73e8>作者：</font>** Shunxin Wang, Alexandros Stergiou, Luuk Spreeuwers 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world deployment of computer vision models, particularly in outdoor scenarios, is often limited by environmental interferences, such as adverse weather. Improving model robustness across weather conditions is thus critical for reliability. However, sourcing high-quality data relevant to isolated weather effects is a significant challenge. Most datasets include changes in dynamic elements across observations of the same scene: subjects such as pedestrians and vehicles change between shots, while camera viewpoints vary. These aspects make it difficult to decouple solely weather-induced distribution shifts from the scene. In this work, we address this with a novel weather synthesis framework that utilizes structure-retaining Low-Rank Adapters (LoRA). We analyze the attention blocks in Stable Diffusion XL (SDXL) and identify where relevant structural information is mostly processed during image-to-image translation. Through an architectural analysis of SDXL, we learn structural LoRA matrices for the corresponding blocks and then leverage them for weather synthesis, eliminating the need for external conditioning such as ControlNet. Experimental results demonstrate that our method improves upon existing synthesis approaches, achieving greater realism while preserving structure. This provides a robust pipeline for generating high-fidelity training and evaluation data for outdoor computer vision applications.

---


### 122. [IntReal: A Real-World Dataset and Benchmark for Multimodal Interleaved Generation](https://arxiv.org/abs/2610.38425)

**<font color=#1a73e8>作者：</font>** Shaohan Yu, Jie Qin, Wende Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans routinely consume multimodal content, where textual and visual information is naturally interleaved. Although Unified Multimodal Models (UMMs) can jointly generate text and images, multimodal interleaved generation remains largely underexplored. Progress in this area is hindered by two key limitations: (1) the lack of well-defined interleaved generation tasks and corresponding training data, and (2) the absence of fine-grained evaluation protocols that can reliably diagnose model performance across different capability dimensions. To this end, we present IntReal, comprising two complementary components: IntReal-100K, a real-world dataset of multimodal interleaved samples spanning four major categories, and the IntReal Evaluation Suite, which evaluates model performance across seven complementary dimensions using specialized expert models, enabling coarse-to-fine diagnosis. Extensive experiments validate our evaluation suite through low inter-metric redundancy (max pairwise absolute Spearman's $\rho \leq 0.42$ ), high agreement with human judgments (83.3% accuracy), and strong consistency across different expert evaluators (Spearman's $\rho > 0.9$ ), supporting the complementarity and reliability of our metrics. By benchmarking four families of UMMs, we show that IntReal Evaluation Suite reveals distinct strengths and weaknesses across models. Post-training experiments demonstrate the utility of IntReal-100K for improving interleaved generation and further show that training unimodal generation can also benefit interleaved generation. These findings suggest that interleaved generation can benefit from modality-specific optimization, rather than requiring joint text-image training at every stage.

---


### 123. [DecisionUnlearn-Bench: Unlearning Probabilistic Decisions under Changing Schemas](https://arxiv.org/abs/2610.38431)

**<font color=#1a73e8>作者：</font>** Tiantong Wu, Wei Yang Bryan Lim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to reproduce the behavior of a model trained without designated data. For probabilistic decision models, this target also depends on the candidate options supplied at inference. We introduce DecisionUnlearn-Bench, an empirical framework that compares full, unlearned, and retain-only models across deletion granularities, label renderings, and candidate sets. Across 20 eligible model configurations on the BANKING77 dataset, full-to-oracle displacement increases consistently from example to association to class deletion. Replacing semantic option labels with opaque codes nearly eliminates the retrained oracle's recognition of deleted classes, even with successful acquisition of the full model, whereas changing the candidate set alters both the oracle and the measured unlearning progress. SimNPO satisfies the screening criterion in 19 of 20 configurations, but its gains vary substantially across seeds and deletion targets. Development tuning on the CLINC150 dataset does not establish a positive pooled effect across 48 intents. At approximately matched suppression, methods can differ markedly in oracle fidelity. Recovery experiments further distinguish initial forgetting from subsequent adaptation and show conclusions that depend on both architecture and metric. These results show that evaluating decision-model unlearning relative to a schema-specific retraining target, with separate reporting of effect size, utility, robustness, and recoverability.

---


### 124. [Continual Adaptation Across Modalities: Learning and Forgetting in Unified Multimodal Models](https://arxiv.org/abs/2610.38436)

**<font color=#1a73e8>作者：</font>** Xinrui Wang, Zhihao Chen, Jia Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs), which can process and generate diverse modalities within a single framework, have recently emerged as a powerful paradigm. However, when these models undergo continual learning on multiple tasks across different modalities, their learning and forgetting dynamics remain poorly understood. In this paper, we systematically investigate how architectural design and adaptation method shape intra-modal learning and cross-modal interference between the generation and understanding sides. Specifically, we report three findings. First, the severity of cross-modal interference decreases with the degree of modality-specific parameter isolation. Second, a within-model asymmetry: the generation side of a UMM is markedly more fragile than its understanding side. Third, what post-training adds is the first to be forgotten: purely post-training capabilities such as personalized generation collapse by 84\% to 90\%, while pretraining capabilities remain stable. Together, these results clarify how parameter isolation and post-training fragility shape UMMs' learning and forgetting dynamics, offering a starting point for developing continually evolving UMMs.

---


### 125. [DES-JEPA: Learning a Shared Vocabulary for High-Dimensional Discrete Event Sequences](https://arxiv.org/abs/2610.38445)

**<font color=#1a73e8>作者：</font>** Hugo Math, Maximilian Forstenhäusler, Christos Anagnostopoulos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Temporal foundation models such as Chronos and TimesFM generalize across domains through a shared numerical observation space. In contrast, discrete event sequences (DESs), including operational event logs or patient clinical-event trajectories, have domain-specific event vocabularies whose labels lack a consistent correspondence across domains. Beyond this lack of consistency, the number of distinct events in real-world settings is high enough to challenge both classical temporal point process modeling and current in-context foundation inference models such as FIM-PP. Critically, current foundation models for DESs are limited to a small, fixed number of event types, restricting their applicability to realistic, high-dimensional event streams. To address this, we propose two complementary modules: (i) DES-JEPA, a joint-embedding predictive architecture that learns a shared discrete vocabulary from synthetic stochastic processes with unaligned event vocabularies; and (ii) DES-PFN, a discrete event sequence prior-fitted network that reuses the learned vocabulary for in-context next-event prediction. Without task-specific fine-tuning, this framework achieves competitive zero-shot performance on eight unseen real-world datasets and scales up to 700 distinct event types.

---


### 126. [StreamStudio: Exploring Video Authoring with Streaming Autoregressive Generation](https://arxiv.org/abs/2610.38467)

**<font color=#1a73e8>作者：</font>** Boyu Li, Zhe Lin, Eli Shechtman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present StreamStudio, a prototype system that explores a new authoring paradigm for streaming video generation. Instead of entering a prompt and waiting for a complete video before making changes, creators can interact with the generation as it unfolds: steering what comes next, returning to earlier moments, and exploring different continuations. In this way, StreamStudio shifts creative control from post-generation revision to continuous interaction with the generative process. Our contribution centers on this authoring paradigm and the interaction mechanisms that make streaming generation directly manipulable. StreamStudio is designed as a plug-and-play interface that can work with compatible generation and editing models, allowing its interaction model to evolve alongside advances in underlying video models. As streaming models become faster and easier to control in the future, such an interface may support more flexible and controllable video creation, including richer edits and multimodal interventions during generation.

---


### 127. [Cinematize from Unreal: Agentic Choreography for Controllable World Simulation](https://arxiv.org/abs/2610.38468)

**<font color=#1a73e8>作者：</font>** Zifan Song, Caihua Shan, Kaitao Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Controllable world simulation requires more than visually plausible frames: scenes must retain persistent state, coordinated actions, and editable temporal structure. Generative world models offer flexible visual synthesis, but their outputs do not always expose the objects and transitions needed for precise revision. Graphics engines provide executable state and direct control, yet translating language into valid operations requires specialized knowledge of assets, geometry, and interdependent APIs. We present CineU (Cinematize from Unreal), an agentic system for language-driven world orchestration and cinematic choreography within Unreal Engine. From a code-based world modeling perspective, an Unreal project serves as a persistent, inspectable world representation, while agent-generated code specifies operations whose effects can be executed and verified. CineU combines hierarchical orchestration, cascaded asset retrieval and geometry-constrained placement, capability-aligned code synthesis, and multi-stage verification with localized repair. Shared scene and timeline context coordinates entities, actions, camera trajectories, and shot boundaries while supporting dependency-aware revisions. Experiments on scene construction, selective editing, multi-shot cinematography, and component ablations show how specialized execution knowledge and engine feedback improve task completion and targeted recovery. CineU illustrates how executable world state can complement learned visual generation to support controllable and revisable simulated worlds.

---


### 128. [Recurrent Bipartite Graph Neural Networks for QC-MDPC Error Decoding in McEliece Cryptosystems](https://arxiv.org/abs/2610.38479)

**<font color=#1a73e8>作者：</font>** Parth Rajeshkumar Tandel, Elisabeth Fink  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As the advent of large-scale quantum computing threatens classical encryption, Quasi-Cyclic Moderate Density Parity-Check (QC-MDPC) codes have emerged as a foundational element of Post-Quantum Cryptography (PQC). However, decoding these relatively dense codes using classical Belief Propagation algorithms often leads to failures caused by short graph cycles that stall the decoder. In cryptographic applications, these failures are severe security vulnerabilities that leak secret key information. To address this, this paper proposes a Recurrent Bipartite Graph Neural Network (R-BGNN) as proof of concept. By integrating Gated Recurrent Units (GRUs) into the message-passing framework and employing a multi-topology curriculum training strategy, the R-BGNN actively learns to break limit-cycle oscillations. Evaluated across 20 unseen matrix topologies, the proposed architecture significantly outperforms classical Bit-Flipping and Min-Sum baselines, reducing the Decoding Failure Rate (DFR) by 63.7\% at moderate noise levels ($t=10$) while converging in fewer iterations.

---


### 129. [Geometry-Aware Trajectory State Modeling for Few-Shot Action Recognition](https://arxiv.org/abs/2610.38482)

**<font color=#1a73e8>作者：</font>** Zhiqi Miao, Marko Haralović, Stanislav Levendeev 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot action recognition (FSAR) requires representations that expose discriminative motion dynamics from only a few labeled videos. Recent trajectory-based methods leverage long-term point tracks for explicit temporal correspondence, but often treat trajectories as carriers of sampled visual features or summarize their motion with compact 2D displacement-based descriptors. We instead view an action as the ordered evolution of 2.5D trajectory states and their local geometric interactions. Based on this view, we introduce GeoTRAM, a geometry-aware trajectory state modeling framework for FSAR. GeoTRAM lifts sparse tracks into 2.5D trajectories, where StateMotion models ordered intra-trajectory state evolution and RelMotion captures state-conditioned local interactions through time-varying relative geometry and motion. Quality-filtered spectral sampling provides more reliable trajectory initialization; complementary semantic, motion, and depth cues are separately refined and preserved for joint spatio-temporal modeling; action-guided reweighting and top-$\rho$ trajectory selection support complementary frame- and trajectory-level matching. Experiments on five FSAR benchmarks demonstrate strong gains on the motion-centric Something-Something benchmarks while maintaining competitive performance on more appearance-driven benchmarks and a favorable accuracy--efficiency trade-off.

---


### 130. [Calibrating Track-Query Updates at Test Time for Multi-Object Tracking](https://arxiv.org/abs/2610.38494)

**<font color=#1a73e8>作者：</font>** Riku Inoue, Shogo Sato, Yu Mitsuzumi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-Object Tracking (MOT) requires localizing multiple objects and maintaining their identities over time. Recent query-propagation trackers carry target-specific representations across frames and update them with current-frame image features, yet identity association remains difficult when visually similar targets overlap or cross. During such interactions, current-frame query updates may contain components directed toward nearby active tracks, which may affect identity association in later frames. To investigate this issue, we analyze track-query updates preceding identity switches (IDSWs), where the same target is assigned a different track ID. Our analysis shows that (i) propagated track-query representations change more abruptly before IDSWs, (ii) current-frame updates have larger positive projections along directions toward other active tracks, and (iii) bounding-box intersection over union (IoU) retrieves the counterpart track involved in a subsequent IDSW with high recall when that track remains active before the switch. Motivated by these findings, we propose Test-time Track-Query Calibration (TQC), a training-free and gradient-free method for query-propagation trackers. TQC calibrates the tracker output before propagation using a bounded correction estimated from update components directed toward nearby active tracks. It requires only track-query representations and bounding boxes available during inference, without retraining or architectural modification. Across nine DanceTrack and SportsMOT test settings, TQC improves HOTA and AssA in all settings and IDF1 in eight, with an average HOTA gain of +0.38 and limited inference overhead. Controlled variants on six validation settings further show that TQC's correction direction yields more consistent HOTA improvements than alternative directions with matched correction norms.

---


### 131. [Accelerating Nonlinear MPC by Behavior Cloning with Separated Timescales: Application to Nuclear Reactor Load-Following](https://arxiv.org/abs/2610.38496)

**<font color=#1a73e8>作者：</font>** Perceval Beja-Battais, Alain Grosset{ê}te, Nicolas Vayatis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavior Cloning (BC) of expert controllers for multiscale dynamical systems is challenging: state variables evolving at widely separated timescales induce highly nonlinear couplings that a shared latent space may fail to adequately represent, degrading closed-loop generalization. We propose Structured Representation Learning for Behavior Cloning (SRLBC), an architecture designed to leverage the physical knowledge of multiscale systems in which slow state variables, fast (stiff) state variables, and predictable exogenous inputs evolve at different timescales. On 500 long-horizon roll-outs of a pressurized water reactor (PWR) load-following benchmark -a high-dimensional, stiff industrial system with challenging safety constraints -and across 20 training seeds, separated embeddings systematically outperform shared embedding baselines on cumulative cost, imitation accuracy and constraint satisfaction. The resulting standalone policies approach NMPC closed-loop performance at a computational cost 15 times lower on average. Since standalone policies still leave a few percent of trajectories infeasible, we embed the learned policies in a safety-augmented approximate NMPC framework, in which the optimizer is only called when the predicted input sequence is not certified as safe. This yields controllers still 6.8 times faster than the NMPC controller on average, with a feasibility (i.e., constraint satisfaction) of at least 99.8% for all architectures, SRLBC retaining the lowest closed-loop cost. Under distribution shift, standalone BC policies degrade sharply: SRLBC degrades the least, and once safety-augmented, it retains a feasibility above 98% with the lowest closed-loop cost. Beyond the quantitative results, Jacobian-based sensitivity analysis shows that the resulting controller relies on a sparse and less redundant set of latent features, each attributable to a single group of physical variables, and aligned with the physical timescale decomposition of the system.

---


### 132. [Vision-Based Density Estimation for Adaptive Traffic Control](https://arxiv.org/abs/2610.38497)

**<font color=#1a73e8>作者：</font>** Mohammad Usaid, Deepak Silaych, Hrithik Mhatre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic congestion is becoming a critical challenge in rapidly growing urban centers, particularly in developing nations where rapid urbanization and inadequate transport infrastructure place increasing strain on transport networks. In highly heterogeneous and chaotic traffic flows, camera-based traffic-state estimation is limited by severe vehicle occlusion and overlap. In this paper, we propose a framework to optimize traffic flow directly from stochastic visual observations. The architecture is structurally decoupled into three primary components: (a) vehicle density estimation, (b) predictive dynamics modeling, and (c) policy optimization. The proposed methodology introduces a convolutional neural network (CNN) that learns the mapping from camera feeds to spatial density maps, utilizing an adaptive k-nearest-neighbor (k-NN) Gaussian kernel to handle varying congestion levels. This feeds into an ST3DNet predictive module for spatiotemporal forecasting, followed by a hierarchical Graph-Transformer Multi-Agent Reinforcement Learning (MARL) algorithm to optimize signal phases. The density estimation stage was evaluated on 40 annotated intersection images from Rambagh 4, Jaipur, India, with a reported five-fold validation mean absolute error (MAE) of $3.32 \pm 0.95$ vehicles and a mean absolute percentage error (MAPE) of 14.5%. These results pertain to the perception component; empirical training and evaluation of the forecasting and control stages remain future work.

---


### 133. [Residual Motion Splatting for Continuous Space-Time Video Super-Resolution](https://arxiv.org/abs/2610.38499)

**<font color=#1a73e8>作者：</font>** Vincent Herfeld, Eva Coupet{é}, Julien Mairal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous space-time video super-resolution produces a high-resolution, highframe-rate video from a low-resolution, low-frame-rate one at arbitrary spatial scales and temporal instants. Classical spatial multi-frame super-resolution has shown that detail beyond a single frame's sampling limit can be recovered by aligning complementary observations with sub-pixel precision and accumulating them on a finer grid. Existing learning-based methods largely depart from this principle: some align and fuse frames only at low resolution before regressing a continuous high-resolution representation, while others interpolate each frame to the output resolution before splatting. In both cases, the per-frame samples are resampled before fusion, so their sub-pixel positions are lost before frames are combined. Restoring this principle in a learned continuous model raises two challenges: estimating sub-pixel motion at unobserved times, and handling holes and occlusions when splatting a coarse grid onto a finer one. We address the first by predicting per-pixel continuous trajectories that refine linear optical-flow paths with smooth residual motion, using features integrated over the full video sequence. We address the second by directly splatting consecutive low-resolution features in a learned latent space onto a high-resolution grid at their predicted sub-pixel positions with predicted visibility weights, before a decoder resolves remaining ambiguities. This makes temporal interpolation and multi-frame superresolution a single operation. Our method improves both reconstruction fidelity and perceptual quality on multiple standard benchmarks over the state of the art, while running up to an order of magnitude faster.

---


### 134. [UnMixMamba: Unmixing Guided State Space Subpixel Mapping of Crops from MODIS Time Series](https://arxiv.org/abs/2610.38507)

**<font color=#1a73e8>作者：</font>** Motasem Alkayid, Yimin Zhu, Naser El-Sheimy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subpixel mapping (SPM) of crop types from \SI{250}{m} Moderate Resolution Imaging Spectroradiometer (MODIS) time series to field-scale Agriculture and Agri-Food Canada (AAFC) labels supports acreage estimation and agricultural monitoring. Three difficulties remain: (i)~spectral-temporal coupling and mixed pixels that break direct coarse-to-fine classifiers; (ii)~intra-class endmember variability that a single spectrum per crop cannot capture; and (iii)~uniform refinement on the high-resolution (HR) grid, which treats every subpixel the same, so most of the effort goes to easy pixels while errors remain in the minority class. UnMixMamba addresses them as follows. For~(i), a temporal-spectral-spatial decoupled (TSSD) factorization estimates simplex fractions and drives AAFC classification from the same mixture field, instead of mapping low-resolution (LR) observations directly to HR logits. For~(ii), \(\times 8\) abundance super-resolution and a learnable per-crop variant endmember bank reconstruct the MODIS cube at LR and HR under a linear mixing model. For~(iii), the predicted crop fractions decide where a fixed Mamba token budget is spent, so HR refinement focuses on the minority class instead of the full grid. On Alberta 2015 under a fixed spatial-block protocol, UnMixMamba reaches OA 0.8397, mIoU 0.6640, AA 0.7837, and Kappa 0.7715, ahead of ST-DRes, ESPCN, FineCrop, AgriFM, and classical SPM baselines. The task is closed-set four-crop mapping inside a known agricultural mask.

---


### 135. [Similar Scores, Opposite Failures: Human Correction as an Instrument for Video Caption Evaluation](https://arxiv.org/abs/2610.38511)

**<font color=#1a73e8>作者：</font>** Ankit Khedia, Astitva Jaiswal, Chaitanya Prasad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video captioning models are increasingly evaluated with metrics designed for single-sentence image captions. We test whether those metrics recover human judgement on dense, multi-window video description, and find that they do not. Six frontier models captioned 196 short clips. Trained annotators post-edited every caption against a failure taxonomy fixed before annotation, once as a whole-clip overview and once window by window, and a quality-control reviewer checked each annotation, yielding 1,144 overview verdicts and 4,672 window verdicts. Reference-overlap metrics do not separate the captions reviewers accepted from those they rejected: BLEU-4 reaches an AUC of 0.510 and a CIDEr-style tf-idf cosine 0.528, and restricting references to reviewer corrections leaves BLEU-4 at 0.479 (95% CI 0.431-0.529), indistinguishable from chance. Review granularity changes what is detected. The same annotators record camera and shot errors on 2.7% of captions when reading the overview and on 12.8% when reading window by window, a 4.7x gap that holds across every robustness check we ran, on the mode most likely to need a near-total rewrite. Correct-overview rates span 54.1-72.7%, but only 4 of 15 pairwise gaps survive Bonferroni correction (5 after adjusting for reviewer and clip effects), and accuracy and derived severity order the models differently. Models with statistically indistinguishable accuracy have sharply different failure profiles, which no single scalar shows. We argue that caption evaluation should record what was wrong rather than only how often, and we report the taxonomy, the per-model profiles, the corpus properties that predict difficulty, and the code that regenerates every number in the paper.

---


### 136. [The Power Watershed as a Differentiable Segmentation Layer](https://arxiv.org/abs/2610.38516)

**<font color=#1a73e8>作者：</font>** Galia Akl, Laurent Najman, Hugues Talbot  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a Watershed transform, the classical tool of morphological segmentation, be placed at the end of a deep network and trained through? The Power Watershed (PW) is the limit of the seeded Random Walker (RW) as p grows to infinity with edge weights raised to the power p. At every finite p the RW solves a sparse positive-definite linear system and is exactly differentiable with respect to the edge weights and the unaries through one adjoint solve; its multi-label form costs one right-hand side per label, and its limit is the PW. We study this family as the last layer of a segmentation network, the watershed layer (WS layer). A conditioning study measures how the solve, the gradient and the distance to the limit evolve with p, and the implicit gradient is checked against unrolling. On synthetic data with correct edge costs the WS layer transforms a soft prediction into an exact boundary. On nuclei segmentation (PanNuke), a binary WS layer is level with a thresholded U-Net. With the instances as labels, the WS layer turns the U-Net into an instance segmenter whose number of labels is set per image by the markers rather than by the output layout, and the network is trained through that partition: instance F1 score rises from 0.656 to 0.795 over a U-Net with connected components, level with the same network followed by a tuned marker watershed. At the training temperature the partition is a watershed of the learned costs, and the finite temperature lets the solve hedge, discounting weak markers and sharing contested pixels. The hedging puts the WS layer 0.015--0.020 F1 ahead of the baseline when trained on a tenth of the data, at the price of having to deploy the finite-p solve rather than its exact limit at inference. Code and the full experimental record are released.

---


### 137. [AtomSteer: Test-Time Constraint Steering for Atomistic Generative Models](https://arxiv.org/abs/2610.38517)

**<font color=#1a73e8>作者：</font>** Pengfei Cai, Katharina S. C. Jäger, Utkarsh Utkarsh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow matching models offer scalable approaches to generating crystalline materials, molecular conformers, and protein-ligand complexes. However, satisfying crystallographic symmetry, structural geometry, and accurate stereochemistry remains challenging. Satisfying these requirements calls for corrections that preserve the geometry already captured by the pretrained model. In this work, we propose AtomSteer, a test-time inference framework for steering pretrained atomistic generative models with structural constraints. During sampling, AtomSteer corrects intermediate structure predictions with bounded local projections, graph-rigid stereochemical transformations, and projections over periodic symmetries, accepting updates that improve constraint satisfaction while limiting changes to the rest of the structure. We demonstrate AtomSteer across three pretrained backbones, FlowMM, ET-Flow, and Boltz-2, spanning de novo crystal generation and crystal structure prediction, molecular conformer generation, and protein-ligand complex structure prediction. AtomSteer improves space-group distribution coverage in de novo crystal generation and improves target space-group recovery in crystal structure prediction. AtomSteer improves molecular validity and E/Z stereochemical accuracy while retaining conformer ensemble fidelity. For protein-ligand complexes, AtomSteer reduces ligand E/Z errors relative to experimental reference structures while achieving competitive docking success and PoseBusters validity. Our method provides a unified framework for adding chemical and crystallographic control to existing atomistic generative models without retraining or architectural changes.

---


### 138. [Self-Consistency Geometry Injection for Multi-view Consistent Image Generation](https://arxiv.org/abs/2610.38518)

**<font color=#1a73e8>作者：</font>** Yupeng Xiao, Yankai Wu, Jianjie Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion models have achieved impressive progress in single image to multi-view generation by synthesizing consistent novel views efficiently. Existing methods usually explicitly or implicitly couple geometry inference and texture synthesis, making generation vulnerable to inaccurate geometry prediction. Although several geometry-guided methods have explored decoupling, they usually treat predicted geometry as a fixed condition and do not explicitly model whether the geometry is reliable. We therefore propose Reliability-Guided Multi-View Generation (RGMV), which comprises a parameter-free Self-Consistency Geometry Gate (SCG) and a Reliability-aware Geometry Injection (RGI) module. Specifically, a geometry proposal generator produces multiple geometry predictions for the same reference image and target viewpoints under different stochastic sampling configurations. SCG measures their spatial agreement to derive a reliability map, which RGI uses to modulate the injection strength of geometry-conditioned residuals in the RGB synthesis model. Moreover, RGMV can adapt to different geometry proposal generators. As a result, RGMV preserves stronger geometric guidance in stable regions while attenuating unreliable geometry cues before they propagate into multi-view RGB generation. Extensive experiments show that reliability-aware geometry injection improves the geometric quality of multi-view generation. Code: this https URL.

---


### 139. [Influence of Agent Number and Behavior on Users' Psychological Responses in VR Evacuation Training](https://arxiv.org/abs/2610.38536)

**<font color=#1a73e8>作者：</font>** Naoki Matsumura, Kensuke Sugihara, Tomoko Yonezawa  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study aims to build effective drill software by combining a virtual simulation of a disaster with multiple agents capable of expressing emotions. We evaluated how the number of agents and their emotional and behavioral actions during evacuation influence users in a virtual space. The results showed that users tended to act more confidently when many agents evacuated with them, and that the evacuation route chosen by the agents influenced the users' decision-making. These findings indicate that users' evacuation behavior is shaped not only by the environment itself but also by the collective behavior of surrounding agents, underscoring the need to consider how agent behavior affects users' psychological states during training.

---


### 140. [An Alignment Benchmark for Enterprise Agents on Era by Eon](https://arxiv.org/abs/2610.38544)

**<font color=#1a73e8>作者：</font>** Hai Sadon, Benjamin Gruenbaum, Doron Porat 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are widely used in enterprises to access business systems and act on them in pursuit of a goal. However, fulfilling a user's request can cause harm. Era by Eon is a product that creates a digital twin of a company by simulating its business systems and data. Its simulators implement the programming interfaces of real products. Our benchmark uses ten of these systems, including Salesforce, Zendesk, Jira and Slack. We tested whether agents would carry out harmful business requests or trust misleading information in company records. We ran 19 models on 41 tasks three times, for 2,337 runs. Of the 2,304 runs that produced an answer, 918 (40%) contained a violation. The most common were false claims about actions or records (290 runs), following planted instructions (266) and disclosing sensitive data to the wrong audience (249). Every attempted change was recorded and blocked before it took effect. Misleading Slack messages caused 16 models to report an incorrect ticket status in 47 of 57 runs. No model was free of violations. The four best models violated in 22 to 24% of their runs. Yet one of them, Nova Pro, did the task correctly in only 30 runs.

---


### 141. [PT$^3$: Prototype-Guided Self-Supervised Pretraining for Generalizable mmWave Human Point Cloud Representation](https://arxiv.org/abs/2610.38551)

**<font color=#1a73e8>作者：</font>** Ziyang Liu, Kieren Yu, Xiao Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-source millimeter-wave (mmWave) observations offer an opportunity to learn human representations reusable across sensing tasks. However, sparse detections and multipath effects make these observations unstable, challenging existing point cloud pretraining methods. We propose PT$^3$, a prototype-guided self-supervised pretraining framework for mmWave human point clouds. PT$^3$ represents local states in spatial regions as sparse compositions of shared prototypes and learns their temporal evolution through autoregressive prediction. Observation consistency further stabilizes representations under radar perturbations. After pretraining on unlabeled sequences from multiple sources, the same frozen encoder supports action classification, dense point generation, joint pose estimation, and future motion prediction on datasets not used for pretraining. Across these tasks, PT$^3$ outperforms the compared pretraining baselines and achieves competitive or superior performance to task-specific models.

---


### 142. [A Minimally Informed Black-Box Fake-Report Attack on DRL Traffic-Signal Control](https://arxiv.org/abs/2610.38557)

**<font color=#1a73e8>作者：</font>** Amro Saleh, Loukas Lazos, Mohammad J. Abdel-Rahman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) traffic-signal controllers may use vehicle-to-infrastructure (V2I) reports, exposing their perception layer to false-data injection. Existing demonstrations typically assume either white-box access to the controller's weights or full observability of the traffic state. We study the impact of a weaker and more realistic adversary who has no access to the RL model and whose traffic observations are limited to her own approach. This black-box, minimally informed attacker trains an imitation surrogate of the controller. She then crafts bounded fake reports, restricted to inflating vehicle counts on her own approach, that transfer to the real controller. We demonstrate that despite the loss of accuracy relative to an attacker who can observe the entire state and action space, this limited attacker can significantly increase the average waiting time for other approaches while barely changing the waiting time on her own approach, i.e. externalizing the added delay onto the other approaches. Because the only realizable move is to inflate one's own reported queue, we find that a zero-knowledge attacker that simply reports the maximum feasible queue is as damaging as the surrogate-based one, while an unstructured random inflation is not: the surrogate is not required to reproduce the degradation, and the exposed vulnerability is the V2I sensing channel itself. The surrogate's role is directional control, selecting a disruptive or a selfish objective at the same budget. The attack persists under +/-20% uniform demand variation. Finally, on a common per-lane budget we place the attacker on a knowledge ladder against white-box adversaries, and find the black-box surrogate matches a realizable white-box attacker that uses the victim's own gradients; only abandoning realizability raises the damage further.

---


### 143. [REVBRAIN: Real-time Probabilistic EEG Forecasting Using Residual Vector Quantization](https://arxiv.org/abs/2610.38558)

**<font color=#1a73e8>作者：</font>** Hanna Pankka, Jaakko Lehtinen, Timo Roine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time forecasting of resting-state EEG signals is required by applications like brain-state-dependent stimulation, where computer generated actions are coupled with ongoing neural oscillations. Recently, the deep learning model WaveNet was proposed for the forecasting task. It shows superior accuracy compared to the prevailing method, the linear autoregressive (AR) model, and provides a built-in uncertainty measure due to its probabilistic modeling framework. However, inference using WaveNet is too slow for real-time use due to its sample-by-sample autoregressive operation: a single forecast requires evaluating the model tens or hundreds of times depending on the length of the prediction window.
In this paper, we present REVBRAIN, a probabilistic deep learning method that produces forecasts in real time by generating the forecast over the whole prediction horizon at once. This is achieved by tokenizing the output space using residual vector quantization (RVQ) and generating forecasts over the items in the tokenized space.
We tested REVBRAIN for forecasting 200 ms of EEG time series in the alpha-frequency band (8-13 Hz) and compared our results against WaveNet model. We found that REVBRAIN achieved real-time inference on a laptop GPU and an over $50\times$ speedup compared to WaveNet, while reaching superior prediction accuracy.
By achieving real-time inference speed, REVBRAIN enables incorporating accurate and probabilistic EEG forecasting into BCI applications, opening up new ways for investigating the functioning of the human brain.

---


### 144. [Persona Learning from Feedback for Personalized AI Assistants](https://arxiv.org/abs/2610.38561)

**<font color=#1a73e8>作者：</font>** Yiran Shen, Yu Xia, Liuyi Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalizing AI assistants requires adapting their behavior to users' preferences and task contexts. Existing work elicits assistant personas through persona prompting or finetuning on persona-conditioned generations. However, persona descriptions alone do not identify what to change or preserve in a particular response, or which behaviors suit the current request. We introduce $\textit{Persona Learning from Feedback (PLF)}$, a framework that learns reusable, preference-grounded assistant personas as independent LoRA adapters on a shared frozen backbone. During training, a frozen self-teacher conditions on persona specifications and response-specific feedback to provide token-level supervision on each adapter's own generated prefixes. A feedback gate focuses corrective updates on responses judged to need improvement. At deployment, a supervised router uses the request or dialogue to select a single adapter or a fixed composition, without user-specific finetuning. We evaluate PLF on single-turn personalization with model-generated critiques and multi-turn tutoring with simulated students' reactions. Across both settings, PLF improves model-judged preference fit over fixed-persona policies and strong baselines including persona prompting and persona distillation, demonstrating how feedback-trained behaviors can be reused for adaptive assistant personalization without degrading general capabilities.

---


### 145. [A-RSI: Adaptive Task Refresh for Zero-Data Multimodal Self-Improvement](https://arxiv.org/abs/2610.38568)

**<font color=#1a73e8>作者：</font>** Yu Liu, Youxing Li, Yuedong Tan 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement requires models not only to acquire useful training experience, but also to decide when their current experience has ceased to be useful. Existing methods often focus on what experience to generate next, while paying less attention to when fresh experience should be introduced. Many also construct training targets through self-consistency or majority voting, making supervision depend on the model's own uncertain predictions. We address these two questions separately: training dynamics determine when to acquire new experience, while the answers to new tasks remain independently checkable. A-RSI monitors reward variation and accuracy in training logs to refresh a task pool when its learning signal declines, without consulting validation or test scores. A static library of model-authored programs produces multimodal questions and derives their reference answers; we specify the task-generation contract, automatically verify chosen properties of the reward and refresh rules, and separately audit the generated answers. The training loop uses no external training examples or human-written answer labels. On the primary eleven-benchmark suite, A-RSI raises the performance average from 57.77 to 61.05 with 800 fresh tasks.

---


### 146. [Episodic looking - using reinforcement learning to bias perception enhances few-shot and continual learning with protection from forgetting](https://arxiv.org/abs/2610.38577)

**<font color=#1a73e8>作者：</font>** David Rawlinson, Gideon Kowadlo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There is a fundamental contradiction between the desire for models that can generalize, and models that can continuously adapt to recent input with changing statistics. These conditions, captured in few-shot and continual learning settings, can bias or disrupt learned representations. This harms generalization to a broader context, leaving the model unable to overcome input variance.
This paper proposes a solution based on the Complementary Learning System architecture (CLS), in which a Short-Term Memory (STM) delegates generalization to a slow, statistical Long-Term Memory (LTM). Delegation is achieved by working in a space of robust, generalized perceptions produced by the LTM. With this separation, the STM can focus on memorizing recent input and avoiding interference between memories.
We show that on an image classification task, the resulting CLS model is more resistant to forgetting in a domain-incremental continual learning setting than a baseline ResNet LTM, and generalizes more effectively in a few-shot setting than other continual learners.
In the continual setting, overall accuracy is slightly worse than existing continual learning models, but with a different mix of performance characteristics. Results analysis suggests that the model is limited by the representations and representational plasticity of the LTM. In future work, we will seek to address this by replaying STM memories to the LTM.

---


### 147. [Dual DeltaNet: Value-Side Memory Reorganization for Linear Attention](https://arxiv.org/abs/2610.38578)

**<font color=#1a73e8>作者：</font>** Yixiao Qian, Yaxin Zhang, Song Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention and state space models (SSMs) offer efficient alternatives to softmax attention by maintaining a fixed-size recurrent state, but this design requires careful management to preserve useful historical associations and limit interference. The delta rule helps reduce interference through correction of the value associated with each key, but it does not explicitly account for how related value features are distributed across the state. We observe that a state $\boldsymbol{S}\in\mathbb{R}^{d_k\times d_v}$ can be viewed as a bank of $d_k$ addresses storing $d_v$-dimensional values. While a key-side read $\boldsymbol{S}^\top\boldsymbol{k}$ retrieves the value associated with $\boldsymbol{k}$, a value-side read $\boldsymbol{S}\boldsymbol{e}$ aggregates addresses whose stored value features match the selector $\boldsymbol{e}$. Based on this observation, we propose Dual DeltaNet (DDN), which extends Kimi Delta Attention (KDA) with a two-sided delta rule. The key-side delta rule reads with the current key to correct its associated value, while the complementary value-side delta rule reads with selected features of the current value to reorganize the addresses it occupies. We derive a chunkwise parallel training algorithm and a rank-2 recurrence that increases arithmetic intensity during inference. Compared with KDA, GDN-2, and Mamba-3, DDN achieves the strongest overall performance across language modeling, zero-shot downstream tasks, and retrieval, while incurring modest training and inference overhead relative to KDA. Code: this https URL

---


### 148. [Structural Pattern Mining in Inka Khipus: A KFG Re-Analysis](https://arxiv.org/abs/2610.38580)

**<font color=#1a73e8>作者：</font>** Maria Contreras  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper reports a methodological pivot from the Open Khipu Repository to the Khipu Field Guide (KFG) database, prompted by stalled progress on the OKR, and a full re-analysis of the resulting 650-khipu sample. Three findings recur across every analysis attempted. First, khipu size confounds nearly every derived structural count, explaining 42-70% of its variance; all subsequent models control for it. Second, the two-letter name prefix (AS, UR, HP, QU, JC, MM, KH) identifies the original cataloger, not a site or period, which turns documentation completeness into a second confound that must be modeled explicitly. Controlling for both, khipus cataloged by Hugo Pereyra's Proyecto Quipu (HP) show significantly fewer Ascher sum-relation types than Gary Urton's (UR) khipus (p = 0.044), while the Ascher-cataloged (AS) khipus are too collinear with their own near-total lack of side/direction documentation to assess (VIF = 5.0). Third, generic structural clustering (UMAP+HDBSCAN) does not separate the pooled 650-khipu sample from two independent null models (permutation and Gaussian), corroborating an independent conclusion already reached by the KFG itself; the same test restricted to a single cataloger (UR) proved not reproducible across runtime environments and is reported here as a methodological caveat rather than evidence of structure. A targeted replication of the KFG's own S/Z-knot spatial-block heuristic for calendar/astronomical khipus recovers 8 of 10 published candidates and proposes 34 additional ones under the same criterion.

---


### 149. [RoSAMDepth: Robust Self-supervised Depth Estimation Leveraging Segment Anything Model](https://arxiv.org/abs/2610.38587)

**<font color=#1a73e8>作者：</font>** Xuanang Gao, Zhiwei Ning, Gengming Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust depth estimation aims to maintain high-quality depths across diverse conditions. However, most existing methods estimate depth without taking into account the object-level information. As a result, the predicted depth may easily deviate within objects and become blurred under adverse conditions. To overcome this weakness, we propose RoSAMDepth, a novel framework that can assist robust self-supervised depth estimation in leveraging rich and diverse object-level priors from the Segment Anything Model (SAM). We focus on incorporating object-level information across three key aspects: a segment-guided representation contrasting method that injects object-level awareness into the feature representation space; an adaptive regional outlier masking strategy combined with a regional Gaussian likelihood loss that enforces regional depth smoothness; and an object-level reliability estimation strategy that mitigates the influence of unreliable supervision. Extensive experiments across multiple datasets and diverse weather conditions demonstrate that our method produces sharper, more accurate depth predictions, consistently outperforming state-of-the-art methods. Our code is available at this https URL.

---


### 150. [Data Scaling Laws in Stereo Matching: From In-domain Fitting to Cross-domain Generalization](https://arxiv.org/abs/2610.38600)

**<font color=#1a73e8>作者：</font>** Tong Zhao, Di Liang, Yiming Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the era of large models, stereo matching is developing towards generalizable foundation models trained on million-scale synthetic images. However, how model performance scales up with synthetic data is still underexplored. In this work, we preliminarily investigate the in-domain and cross-domain data scaling laws in stereo matching. A realistic synthetic dataset, named XStereo, containing 200 thousand samples is first built to serve as a high-quality benchmark for data scaling research. In-domain training on five large-scale datasets demonstrate a two-regime scaling behavior with data, transitioning from the standard power law to saturation, where the critical transition point is approximately invariant under a fixed model. Cross-domain performance exhibits a substantially weaker and less predictable dependence on the source-domain data scale. The distribution and coverage diversity are more effective for diminishing domain gaps. More instructive suggestions are provided for high-efficiency data construction and training. The insightful findings are significant verification and extension of the existing scaling laws in both language and vision, paving the way to efficient and stronger stereo matching. The XStereo dataset is public at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
