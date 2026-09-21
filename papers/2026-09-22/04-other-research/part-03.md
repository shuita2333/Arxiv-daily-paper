# 📦 其他研究 | 2026年09月22日

> 本类共 **179** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-179](./part-04.md)

---

### 101. [What Must Survive? Exact Task-Information--State Frontiers for Resource-Sufficient Learning](https://arxiv.org/abs/2609.21523)

**<font color=#1a73e8>作者：</font>** Ronald Katende  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A system may be compressed before its downstream task is fully known. We ask how much retained state is then necessary and how much can be saved by limited advance task information.
For a finite family of linear tasks, a task message is revealed before state formation and the exact task only afterwards. For an advice alphabet of size $K$, the exact frontier is \[ p^*(K)= \min_{\substack{\Pcal\text{ partition of }\U\\|\Pcal|\le K}} \max_{C\in\Pcal}\rank(T_C), \] with the $b$-bit frontier obtained by setting $K=\min(2^b,|\U|)$. Thus advance task information reduces state through partitions whose joint task operators have low rank.
We also give an approximate singular-value frontier, a common-core lower bound and exact direct-sum law, and strong NP-hardness of finding an optimal advice partition. The hardness persists at every fixed positive approximation tolerance.
Three examples illustrate the result. A well-conditioned softmax attention construction gives an exact $524{,}288\to1{,}024$ coordinate frontier when nine bits resolve one of $512$ continuations. A domain-decomposed digital twin yields an interface-plus-local-state law and a weighted partition problem for heterogeneous regions.
A hierarchical multi-task model gives a two-stage frontier in which three bits reduce the required state from $3136$ to $448$ coordinates, with further task information approaching the irreducible $328$-coordinate single-task floor.

---


### 102. [IncentRL: The Trade-Off Between Preference Guidance and Task Performance](https://arxiv.org/abs/2609.21525)

**<font color=#1a73e8>作者：</font>** Xuening Wu, Yanlan Kang, Shenqin Yin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference-based reward shaping can guide reinforcement learning, but adding preference signals to the reward may unintentionally change the task being optimized. We address this problem with IncentRL, a framework that introduces preference guidance while explicitly characterizing its effect on external-task performance. IncentRL adds a Kullback--Leibler (KL) penalty between a specified outcome distribution and a preferred distribution. For finite discounted Markov decision processes with bounded shaping costs, we derive an external-value perturbation bound, establish a sufficient strict-action-gap condition for preserving the original optimal policy, and characterize the large-weight regime through discounted cumulative preference cost. Exact examples clarify the limits of these guarantees, including tied optima and support mismatch. We study a practical implementation using a hand-designed, distance-based outcome proxy, a fixed preference distribution, and score-weighted coefficient search. On MiniGrid DoorKey-8x8, the reported three-seed mean success rate after two million training steps reaches 98\% with coefficient 0.01, compared with 90.5\% for the reported zero-coefficient baseline, while the search progressively shifts toward smaller coefficients. Together, these results provide a principled view of the central trade-off in preference-based RL: using additional guidance to improve learning without excessively distorting the original task objective. The current experiments remain descriptive and do not yet isolate KL shaping from simpler alternatives.

---


### 103. [Critical sets of Latin squares based on autoparatopisms](https://arxiv.org/abs/2609.21532)

**<font color=#1a73e8>作者：</font>** Manuel González-Regadera, Raúl M. Falcón, María Dolores Frau  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In cryptography, critical sets of Latin squares have particularly been implemented to design secret sharing schemes. A main problem in these cryptographic protocols arises from absent holders of pieces of information that are common to different critical sets, because they become indispensable to recover the secret. This paper solves this problem by making use of the orbits of entries described by the autoparatopism group of the Latin square under consideration. To this end, we introduce the more general problem of computing critical sets of Latin squares having a given paratopism in their autoparatopism group. These critical sets depend only on the conjugacy class of the autoparatopism and the main class of the Latin square under consideration. Based on this fact, as an illustrative example, we determine the smallest and largest sizes of critical sets associated with autoparatopisms of Latin squares of order up to six. We implement this approach in the design of a new secret sharing scheme.

---


### 104. [Purification and Regulation: Comorbidity-Aware Multi-Label Few-Shot Learning for Medical Image Classification](https://arxiv.org/abs/2609.21541)

**<font color=#1a73e8>作者：</font>** Ying-Chih Lin, Po-Chih Kuo, Yong-Sheng Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-label few-shot learning (MLFSL) remains a significant challenge in medical image analysis (MIA). Current metric-based meta-learning methods face two critical limitations in MIA. First, conventional prototype generation often entangles irrelevant disease information, leading to contaminated prototypes and degraded performance. Second, prior studies typically enforce inter-class separability in embedding space, largely neglecting the inherent correlations among diseases. To overcome these challenges, we propose Prototype Purification and Regulation (PPR), a novel MLFSL framework for MIA. PPR first performs prototype purification by leveraging sample-level comorbidity scores to emphasize disease-specific features, producing purified prototypes that better characterize each disease. Building upon these purified prototypes, PPR further addresses the underexplored problem of inter-class prototype distance in MIA by incorporating disease-level comorbidity statistics to adaptively regulate inter-class similarity, forming a comorbidity-aware embedding space. Overall, PPR sequentially enables the model to capture pure disease features and inter-class relationships for reliable MLFSL in MIA. Extensive experiments across four chest X-ray benchmark datasets, including cross-domain evaluation, show that PPR consistently outperforms state-of-the-art methods, significantly improving disease detection while demonstrating robust generalization and clinical applicability.

---


### 105. [Do We Care About Personalization and Explainability? An Interview Study with News Recommendation Engineers](https://arxiv.org/abs/2609.21547)

**<font color=#1a73e8>作者：</font>** Jasmin Kareem, Siddharth Mehrotra, Martijn C. Willemsen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Research on explainability in recommender systems largely centers on end users, overlooking the perspectives of those who build and maintain these systems and their potential use cases such as model debugging. In this study, we examine how news engineers and related technical stakeholders perceive and implement personalization and explainability in practice. We conducted 15 semi-structured interviews across nine news organizations, spanning diverse regions in both public and private sectors, to investigate the challenges and motivations shaping their approaches. Our findings reveal that personalization is not always a straightforward or desirable choice for news organizations, as concerns around user tracking, editorial control, and resource constraints often limit its adoption. Even among organizations implementing personalized news recommender systems in production, explainability is rarely prioritized, with day-to-day operational demands frequently taking precedence over longer-term transparency goals. Definitions of explainability vary widely across organizations, though some demonstrate promising internal practices and visualization tools that facilitate communication between engineering teams and newsrooms. Based on our analysis, we provide actionable and practical guidelines for news engineers and researchers on how to adopt explainability methods within a news personalization pipeline.

---


### 106. [Dual-Interest Sequential Product Recommendation With Multi-Granular SSM](https://arxiv.org/abs/2609.21548)

**<font color=#1a73e8>作者：</font>** Shuiying Liao, P. Y. Mok  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sequential recommendation aims to predict the next item a user will interact with based on their historical behavior. Advances in Transformers have significantly improved sequential recommendation but are still limited by cost efficiency. Although State Space Models (SSMs) have recently enabled efficient long-range modeling, most existing methods encode each item with a single static contextual role, overlooking the phenomenon of item polysemy. In fact, the same item often plays different semantic roles depending on user context, and existing methods are limited in capturing dynamic behavior across different temporal granularities. In this work, we propose DSRec, a novel dual-interest cross-SSM model that explicitly disentangles item roles across long-term and short-term semantic context. Sequential items are encoded into long-term interest embeddings that capture stable preferences via historical aggregation, and a short-term interest branch that emphasizes local session intent modulated by inter-click time intervals. These interest embeddings are processed through distinct SSM encoders: a full-sequence Mamba for long-term modeling, and a time-modulated SSM that dynamically adjusts state evolution based on temporal gaps. To enable effective cross-granularity alignment, we adopt a residual cross-fusion mechanism that exchanges contextual information between the two branches while preserving semantic independence. Experiments on public benchmarks demonstrate that DSRec outperforms other state-of-the-art methods.

---


### 107. [CityLearn v3: A Configurable Simulation and Evaluation Framework for Realistic Control Studies of Renewable Energy Communities](https://arxiv.org/abs/2609.21570)

**<font color=#1a73e8>作者：</font>** Tiago Fonseca, Luis Lino Ferreira, Armando Sousa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Renewable energy communities (RECs) coordinate buildings, photovoltaic generation, batteries, electric vehicles and flexible loads. Controller studies often simplify changing participation, equipment availability, service deadlines and data quality, so lower cost or peak demand can conceal missed services or infeasible power requests. This paper presents CityLearn v3, a configurable simulation and evaluation framework for REC control studies under these conditions. It represents changing members and assets, flexible-load deadlines, demand-response requests, local energy sharing, and data or equipment failures within one simulation environment. Building and phase power limits constrain controllable requests, while a declared timestep preserves consistent power-to-energy accounting. The framework records controller inputs and distinguishes requested actions from those applied to the simulated equipment. Reference controllers, service- and constraint-aware performance indicators, and trajectory exports support comparisons within and across communities. Software checks and application examples examine service delivery, electrical constraints, settlement and changing scenarios; a synthetic high-frequency trace replay illustrates how aggregation can conceal short peaks without changing annual energy. Together, these records allow aggregate performance to be interpreted alongside service failures, action reductions and participant-level outcomes.

---


### 108. [GestureFAR: Streaming Co-Speech Gesture Generation with Flow Autoregression](https://arxiv.org/abs/2609.21576)

**<font color=#1a73e8>作者：</font>** Pinxin Liu, Haiyang Liu, Jiahao Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating natural co-speech gestures from streaming speech is essential for embodied conversational agents, where motion must be produced while a user is still speaking. Recent streaming gesture systems make online generation possible by autoregressing over discrete motion tokens, but this design compresses high-dimensional continuous motion into finite codebooks and can limit the realism and diversity of generated gestures. To preserve both causality and continuous expressiveness, we propose \textbf{GestureFAR}, a flow-autoregressive framework for streaming co-speech gesture generation. First, GestureFAR autoregresses over causal continuous motion latents, using a transformer to model streaming audio-motion context and a per-token flow-matching head to sample the next latent from a continuous distribution. Second, we introduce a head-only flow distillation strategy that freezes the causal backbone and distills the multi-step per-token flow head into a single network evaluation using consistency and distribution-matching objectives. This keeps the model token-causal while removing the main latency bottleneck for live interaction. Experiments on BEAT2 show that GestureFAR significantly improves the quality--latency trade-off among streaming-capable methods, preserving strong gesture quality while enabling real-time token-causal generation. Project Page: this https URL

---


### 109. [A benchmark dataset and baseline methods for four-dimensional STEM diffraction patterns](https://arxiv.org/abs/2609.21593)

**<font color=#1a73e8>作者：</font>** Yuyan Guan, Haoran Zhang, Zian Mao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Four-dimensional scanning transmission electron microscopy (4D-STEM) records a two-dimensional diffraction pattern at each electron-probe position, yielding spatially resolved reciprocal-space information but large, heterogeneous data volumes. Here we describe 4D-ImageNet, a collection of 174,000 diffraction patterns comprising 145,000 experimental patterns selected from 29 acquisitions and 29,000 multislice simulations. The experimental data cover acquisition-level labels for Ag, Au, mixed Au-Ag, CoO, Pd and ZnO specimens across multiple fields of view, scan dimensions, camera lengths and exposure times. Each acquisition contributes 5,000 quality-ranked patterns with source scan coordinates and acquisition metadata. A set-prediction detector provides model-derived pseudo-labels for the direct-beam position and Bragg-disk centres, with a confidence score for each disk. The simulation data cover 13 crystal structures and include Euler rotations, reciprocal-space sampling and approximate low-index beam directions. A grouped mixed-domain masked-reconstruction benchmark is provided to assess leakage-resistant loading and evaluation across experimental and simulated data. The dataset is intended for representation learning, disk detection, diffraction-pattern retrieval, orientation analysis and simulation-to-experiment studies.

---


### 110. [HAT: Hypothesis-Anchored Tracking for Video Monocular Spacecraft Pose Estimation](https://arxiv.org/abs/2609.21597)

**<font color=#1a73e8>作者：</font>** André Lopo, Atabak Dehban, Rodrigo Ventura  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 6-DoF pose estimation of non-cooperative targets is important for on-orbit servicing and debris removal. A single-image estimator can confuse near-symmetric spacecraft orientations, and tracking can preserve an incorrect pose. We present Hypothesis-Anchored Tracking (HAT), a causal framework that uses inter-frame motion to select among competing CAD-based pose hypotheses before alignment and fusion. Rather than independently choosing the highest-scoring hypothesis in each image, HAT retains competing orientation histories and selects a pose to anchor the relative trajectory estimated by monocular SLAM. Sparse anchors and pose fusion provide per-frame estimates after initialization without revising past outputs. The method requires only a calibrated RGB sequence, a metric CAD model, and target image regions, which can be supplied by detection or segmentation. The pretrained pose and SLAM networks require no target-specific training or fine-tuning. We evaluate two versions, Mega-HAT and Pico-HAT, using MegaPose and PicoPose, on SPARK-2024, SwissCube and SHIRT, with YCB-Video assessing performance outside the space domain. Using one temporal configuration per method, the arithmetic means of the four dataset-wise comparisons show 9.4% lower mean pose error and 3.76 times the sustained input FPS for Mega-HAT relative to independent MegaPose, and 23.9% lower mean pose error and 2.42 times the FPS for Pico-HAT relative to independent PicoPose. Mega-HAT ablations on SPARK and an offline reference examine component contributions and the effect of revising past estimates.

---


### 111. [Beyond Accuracy: Centroid-Guided Contrastive Loss for Structured Fraudulent Job Posting Detection](https://arxiv.org/abs/2609.21599)

**<font color=#1a73e8>作者：</font>** Syed Ali Ahmed, Malaika Raza, Muhammad Shoaib Siddiqui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fraudulent job posting detection aims to identify job advertisements that are corrupted either through fake content, misleading information, or negative intent, disrupting the online eco-system of job-seekers and employers. Existing studies in this domain lack effective methods to simultaneously achieve high accuracy and meaningful structure of latent-space representations that capture subtleties among fake posts. To this end, we propose Centroid-Guided Contrastive Loss (CGCL), a loss function which unifies classification with densely formulated clustering to consistently reshape latent-space through a centroid-driven top-$k$ push-and-pull mechanism. The complementary nature of CGCL enables the model to enforce accurate decision boundaries and maintain high clustering compactness, effectively capturing both class separability and latent structure. Extensive experiments demonstrate the state-of-the-art (SOTA) performance of our method on EMSCAD, a public benchmark dataset. The code associated with this work is available at: this https URL

---


### 112. [Learned Parametric Emotion Editing: Real-Time Affective Filtering for On-Device Social Media Video](https://arxiv.org/abs/2609.21624)

**<font color=#1a73e8>作者：</font>** Musa Rochi, Marcel Schubert, Christoph Gebhardt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Problematic internet use affects a growing share of the population, yet common interventions, e.g., time limits, blocking, forced breaks, are coercive and easily circumvented. We explore a less restrictive alternative: adapting the emotional intensity of visual content. Prior work has shown that optimization can steer an image's affective content, but its per-image optimization cost makes it impractical for real-time deployment. We instead learn a model that predicts this transformation in a single forward pass: a MobileNetV4 backbone with FiLM-based emotion conditioning outputs parameters for differentiable global transformations. This replaces prior iterative optimization (80 s per image) with a single 3.7 ms forward pass. In a user study (N = 54), the model reduced viewer-reported arousal relative to unedited images, comparably to the grayscale well-being filter, while being rated higher in perceived quality. We integrate the model into an Android app that adapts Instagram video in real time, sustaining 60 fps on a Samsung Galaxy S23.

---


### 113. [Detection is solved, delineation is not: what governs tooth segmentation on panoramic radiographs](https://arxiv.org/abs/2609.21628)

**<font color=#1a73e8>作者：</font>** Muhammad Rehan, Moaz Amjad, Syed Danial Ahmed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic tooth segmentation and FDI numbering on panoramic radiographs underpins computer-assisted dental diagnosis, yet which factors govern performance remains unclear. We assemble a corpus of 1,422 panoramic radiographs containing 42,142 expert-delineated tooth polygons across the 32-class FDI taxonomy, annotated by 30 dental practitioners and independently reviewed by two others, and use it to isolate input resolution, architecture and anatomical priors under a single evaluation protocol.
First, resolution dominates: across a controlled 640/1024/1280 ablation, mask mAP50-95 rises 0.656 -> 0.710 -> 0.717 while mAP50 stays flat at ~0.982. Both gains are significant under a paired bootstrap over images (p < 0.001, p = 0.024); neither mAP50 change is distinguishable from zero. Added resolution buys boundary precision, not detection. Second, architecture is nearly irrelevant in-domain: a query-based transformer with 2.1x the parameters is statistically equivalent to a one-stage detector (95% CI [-0.0064, +0.0064]), only marginally better under domain shift, 5.5x slower on CPU and not executable under standard ONNX runtimes. Third, three targeted interventions fail: a LoRA-adapted self-supervised encoder underperforms, a promptable foundation segmenter degrades masks by 39%, and globally optimal anatomical label assignment yields +0.0007 despite correcting a constraint violated in 40% of out-of-domain predictions.
Zero-shot transfer to an independent multi-centre cohort, verified overlap-free, costs 62% of mask mAP50-95 but only 18% of mAP50, reproducing the dissociation. Decomposing masks along the tooth axis localises the residual error to the apical third. Boundary precision is therefore the binding constraint, and effort is better directed at resolution and acquisition diversity than at architectural novelty.

---


### 114. [Extending Decoupled Attention to Dense Prediction and Masked Training for Multi-Channel Images](https://arxiv.org/abs/2609.21629)

**<font color=#1a73e8>作者：</font>** Umar Marikkar, Sameed Husain, Muhammad Awais 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-Channel imaging (MCI) data differs fundamentally from natural images, as each channel records a semantically distinct signal rather than a colour band. To adapt vision encoders to MCI data, Multi-Channel Vision Transformers (MC-ViTs) tokenize each channel independently and concatenate the resulting tokens into one sequence, and the channel count is no longer fixed by the architecture. Self-attention is then computed across all channel-patch tokens with no restriction on which channels attend to which, which dilutes the features of individual channels. The Decoupled Vision Transformer (DC-ViT) regulates this by separating updates computed within a channel from updates computed across channels, and by forming a representation per channel before the channels are combined. Its formulation, however, pairs tokens by spatial position, and thus requires the same visible tokens in every channel. Correspondence under independent per-channel masking is recovered by solving a linear assignment between the retained patches of each channel, which allows decoupled attention to be combined with current masked multi-channel training in its standard configuration rather than a restricted one. Across three classification and three segmentation benchmarks spanning fluorescence microscopy, imaging mass cytometry and satellite imaging, including dense prediction at high channel counts, the resulting formulation outperforms the strongest MC-ViT baseline.

---


### 115. [Riemannian Neural Hamiltonian Flows: Geodesic Symplectic Transport and Interpretability](https://arxiv.org/abs/2609.21647)

**<font color=#1a73e8>作者：</font>** Vincent Souveton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hamiltonian normalizing flows are attractive generative models because their phase-space maps are invertible and volume preserving, but most neural constructions are formulated in Euclidean space. We introduce Riemannian Neural Hamiltonian Flows, which combine the fixed kinetic energy of a Riemannian manifold, a learned scalar potential, and an explicit geodesic leapfrog integrator. Our analysis explains how the learned Hamiltonian can be made interpretable. Every normalizable potential defines an implicit profile, and the position marginal initially accelerates along the relative score between that profile and the base. The matched potential is the interpretable specialization for which the implicit profile is the target. In the isotropic Gaussian case, the mechanism corresponds to a phase-space rotation. A local harmonic analysis extends this result around each mode of a general target on a manifold. The gap between the learned and the matched potential is the sum of a residual memory of the base and a bias of the model, and the two potentials agree when the position base has been transferred to the momentum. This can be achieved when the former is broader than the target. Numerical experiments on Euclidean, hyperbolic, and spherical spaces show competitive sample quality and numerical cost against a Riemannian continuous normalizing flow, and confirm the interpretability of the learned potential.

---


### 116. [Beyond Gaussian Worlds: Latent Geometry Matters for JEPAs](https://arxiv.org/abs/2609.21656)

**<font color=#1a73e8>作者：</font>** Léo Nicollier, Enric Meinhardt-Llopis, Marc Pic 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent Joint-Embedding Predictive Architectures (JEPAs) prevent representation collapse by constraining learned representations to follow a prescribed target distribution, such as an isotropic Gaussian or the uniform distribution on a hypersphere. Klindt et al. (2026) showed that, under their Euclidean assumptions, matching a Gaussian target can recover Gaussian latent variables up to a linear transformation, and that the Gaussian is the unique distribution with this guarantee. We extend their analysis to latent variables supported on embedded Riemannian manifolds and derive conditions on the latent geometry and positive-pair dynamics under which alignment and exact distribution matching guarantee linear recovery. In particular, when the latent variables are uniformly distributed on a sphere and the representations are matched to the same spherical distribution, every optimal representation recovers the latent state up to an orthogonal transformation. This shows that Gaussian uniqueness is not a universal property of distribution-matched JEPAs: non-Euclidean latent geometries can admit other linearly recoverable distributions. We further derive an approximate-recovery bound that is strictly tighter for the spherical world than for the Gaussian world. Experiments on Gaussian, spherical, and toroidal latent spaces show that geometrically compatible targets yield better linear recovery when optimization succeeds, whereas mismatched targets distort the latent structure. This advantage persists in high-dimensional Clifford-torus worlds.

---


### 117. [Multi-Domain Clustering via Measure Quantization](https://arxiv.org/abs/2609.21664)

**<font color=#1a73e8>作者：</font>** Rafael Pereira Eufrazio, Eduardo Fernandes Montesuma, Charles Casimiro Cavalcante  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustering is a fundamental task in data analysis, typically addressed through centroid-based methods such as K-means. In this work, we present a general framework for multi-domain clustering via measure quantization: given samples from multiple domains, we learn a shared set of cluster prototypes by minimizing a probability metric, such as the Sinkhorn divergence or the Maximum Mean Discrepancy, between each domain's probability measure and the measure of prototypes. Data points are then assigned to clusters either via nearest centroid, or via optimal transport, a collaborative strategy that couples all samples within a domain. A mini-batch optimization strategy makes both fitting and assignment scalable, reducing memory and computational cost while preserving clustering performance. Experimental results on 5 multi-domain benchmarks spanning image, audio and sensor data show that our Sinkhorn-based method consistently outperforms classical and multi-domain clustering baselines, and that this advantage persists when scaling to hundreds of thousands of samples.

---


### 118. [Listen Before You Speak: Response Planning from Listener Facial Reactions for Conversational Speech Generation](https://arxiv.org/abs/2609.21683)

**<font color=#1a73e8>作者：</font>** Yunji Chu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational speech depends on dialogue context and the listener's immediately preceding behavior. We propose ReACT-TTS, a two-stage framework that uses a one-second pre-response listener facial sequence to plan the next utterance's emotion and prosody before speech realization. On a strict dyadic MELD protocol, Temporal conditioning yields higher mean macro-F1 and VAD concordance than Text-only across ten seeds, while accuracy remains essentially unchanged. Ablations show that temporal modeling performs best among the visual variants and that an explicit early-to-late difference is unnecessary; correct listener reactions also outperform cyclic mismatches on average. In a contextual-appropriateness study with 20 speech researchers, 76% of judgments prefer Temporal, 9% Text-only, and 15% report no preference. We further connect the predicted response style to a Grad-TTS backbone for end-to-end speech realization. Overall, the results support pre-response listener dynamics as complementary cues for conversational response planning. The source code is available at this https URL.

---


### 119. [Optimization Geometry of Equivalent Brownian RKHS Representations](https://arxiv.org/abs/2609.21693)

**<font color=#1a73e8>作者：</font>** Mahdi Mohammadigohari, Gustau Camps-Valls  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivalent finite parameterizations can represent the same functions and intrinsic norm yet induce different optimization algorithms. We study this effect in a controlled finite Brownian RKHS with nodal, increment, and spectral coordinates. Classical finite-element, RKHS-interpolation, Brownian-covariance, and mixed-boundary DCT identities make the shared hypothesis class, Brownian energy, approximation operator, and coordinate maps explicit. Our main results concern the optimization geometry of this fixed model. With mapped initialization, identical scalar steps, and identical minibatches, nodal and spectral GD/SGD have exactly the same mapped trajectories. Increment GD is an explicit Euler step for the constant Brownian/Sobolev metric, with factor $1/h$. For Brownian-regularized least squares, $\kappa_2(\mathbf H_{\mathrm{inc}})\le1+A/\rho$, independently of grid resolution $G$ for fixed $A$, $\rho>0$, and the stated normalization. Under the stated standard-Adam convention, the universal orthogonal equivariance group is exactly the signed permutations; the block DCT-VIII transform is not one. Float64 tests over five grids numerically verify the finite identities, mapped one-layer and recursive trajectories, conditioning predictions, and theorem-matched Adam separation. Thus coordinate effects are isolated without changing the represented functions, intrinsic regularizer, or approximation space.

---


### 120. [Diffusion-Based Tumor Inpainting for Renal Segmentation under Clinical Data Scarcity](https://arxiv.org/abs/2609.21698)

**<font color=#1a73e8>作者：</font>** Ekaterina Sedykh, Salme Ussanov, Dmytro Fedorenko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning segmentation of renal tumors requires large annotated datasets, yet clinical deployments typically offer only a handful of tumor-positive cases from the target site. We propose a diffusion-based inpainting framework that synthesizes anatomically plausible renal tumors within healthy CT scans, requiring no additional annotation, and provide the first systematic comparison of 2D, 2.5D, and full 3D (MAISI) synthesis strategies for this task. Training the diffusion model on public data (KiTS23, KIRC) and evaluating nnU-Net segmentation on a internal cohort across three low-data regimes, we find that 2.5D and 3D augmentation substantially reduce false positives (from $\sim$18--20\% to $\sim$3--6\%) while maintaining Dice, whereas 2D provides no consistent benefit. Crucially, the proposed 2.5D method matches full 3D synthesis on every metric at substantially lower computational cost, indicating that local volumetric consistency alone is sufficient for effective augmentation in data- and resource-scarce clinical settings.

---


### 121. [ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation](https://arxiv.org/abs/2609.21712)

**<font color=#1a73e8>作者：</font>** Boni Hu, Xiong Wei, Haoming Huang 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative world models offer controllable and repeatable closed-loop simulation for end-to-end and vision-language-action driving policies, but production deployment exposes three unresolved requirements: faithfully reproducing a mixed fisheye-pinhole rig at native resolutions; reconciling causal, per-timestep interaction with long-horizon stability and low latency; and preserving scene identity when a location is revisited. We present ZYT-World, a single architecture that natively generates four fisheye views with field of view > 180° and three pinhole views. Projection-specific Plucker adapters encode camera geometry, ego-motion adaptive layer normalization provides global motion control, and a lightweight pixel-aligned layout conditions traffic participants and signals through instance-level boxes, headings and colors. Heterogeneous training combines full-rig geometric coverage with high-resolution detail. Teacher forcing, causal consistency distillation, self-rollout distribution matching distillation, and RigCritic transform a 40-step bidirectional teacher into a one-step, per-latent streaming generator, with RigCritic evaluating the seven-view rig jointly. A 19M-parameter variational autoencoder decoder (TinyVAE), W8A8 quantization, and our inference engine reduce decoding, backbone, and incremental-execution costs, respectively. Finally, cross-trajectory pairs derived from real captures train a plug-in implicit-memory module that preserves place-specific evidence. On the internal multi-view test set, the one-step model retains more than 90% of the teacher's PSNR and SSIM, while FID, FVD, and LPIPS stay within 11% of the teacher. Under the generator-only timing in Figure 2, it is 107.7 times faster than the 40-step bidirectional teacher. TinyVAE decodes 59.8 times faster than Wan. 30s rollouts and cross-trajectory revisits show the intended long-horizon and memory behavior.

---


### 122. [TERMon: Detecting Persistent Behavioral Threats in Edge AI via Hardware-Native Ternary Runtime Monitor](https://arxiv.org/abs/2609.21713)

**<font color=#1a73e8>作者：</font>** Arish Sateesan, Edlira Dushku  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Edge AI accelerators are increasingly deployed in safety-critical environments, where model outputs may control physical actuators, make access-control decisions, or trigger alarms. In these settings, runtime failures often remain undetected because model corruption, distribution shift, and adversarial inputs can still produce well-formed, confident predictions. This paper presents TERMon, a lightweight hardware runtime monitor that detects such anomalies by observing inference behavior rather than re-executing or formally verifying the model. TERMon represents class-conditional trusted behavior as hardware-efficient ternary patterns that are matched in parallel against a thermometer-encoded fingerprint. The ternary encoding reproduces the corresponding unquantized range decision exactly. TERMon detects harmful weight corruptions in proportion to their behavioral impact, while out-of-distribution and adversarial inputs are largely not separable using the monitored features at a strict false-positive operating point. We implemented TERMon on a PYNQ-Z2 FPGA, and the pipelined design requires no on-chip block RAM or DSPs and has a two-cycle decision latency.

---


### 123. [A Framework to Quantify the Probability of Future Cyber Loss Events](https://arxiv.org/abs/2609.21717)

**<font color=#1a73e8>作者：</font>** Siem Peters, Martin Eian  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity risk quantification remains challenging due to limited operational data and difficulties in quantifying Loss Event Frequency (LEF). This paper introduces the Loss Event Frequency Security Analyser (LEFSA), a probabilistic framework that reformulates LEF estimation as machine-level Cyber Loss Event (CLE) prediction combined with hierarchical infrastructure-level aggregation. LEFSA estimates calibrated machine-level CLE probabilities from operational cybersecurity telemetry and aggregates them across infrastructure layers while accounting for machine-level dependencies. This provides a foundation for scalable, explainable, and operationally applicable cyber risk estimation at the level of machines, services, business processes, and the entire organization. The framework was evaluated using proprietary Managed Detection & Response telemetry from 23 organizations using Microsoft Defender for Endpoint. XGBoost achieved the strongest predictive performance, with a mean area under the receiver operating characteristic curve of 0.90 and consistently low calibration error across evaluation periods. The results demonstrate that operational cybersecurity telemetry contains substantial predictive information for future CLE occurrence, supporting probabilistic machine-level modeling and hierarchical aggregation as a promising foundation for quantitative, data-driven cyber risk management.

---


### 124. [Verifiable Computation with Trusted Execution Environments and On-Chain Digital Rights Tokens](https://arxiv.org/abs/2609.21728)

**<font color=#1a73e8>作者：</font>** Bingle Stegmann Kruger, Co-Pierre Georg  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present an architecture that enables data owners to combine private data into data pools using Trusted Execution Environments (TEEs) and manage these pools by issuing narrowly scoped computational rights, encoded as Digital Rights Tokens (DRTs), to third-party data analysts. Each DRT binds specific open-source code to a pool and is issued and redeemed on a distributed ledger. Data analysts can obtain the right to execute open-source code on the combined sealed data inside a TEE and receive the result from this code execution, but not the underlying data. We argue for a control-centric view of privacy in which creators retain ex ante control over how their data is processed. A reference implementation runs WebAssembly (WASM)/Python jobs over sealed datasets and records redemptions on Solana, illustrating the feasibility and limitations of the platform.

---


### 125. [GEM-MPC: Balancing Exploration and Exploitation through Expert-Guided Planning](https://arxiv.org/abs/2609.21735)

**<font color=#1a73e8>作者：</font>** Alvaro Serra-Gomez, Thomas Moerland  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective exploration in high-dimensional continuous control remains a central challenge in reinforcement learning. Planning-based methods address this by combining online planning with learned policies and value functions, but their components can become misaligned during training: learned sampling policies may diverge from planner behavior, while planning distributions stored in replay become stale as the model and value function evolve. Reanalysis can refresh these targets, but at substantial computational cost. We propose GEM-MPC, an MPPI-based reinforcement learning method that improves the interaction between planning and learning. GEM-MPC uses MPPI to combine a policy trained to clone the planner with a KL-regularized policy that explores around it, providing complementary exploitation and guided exploration within planning. We further introduce Gated Prior Distillation, which selectively learns from stored planning distributions only when they provide a better target than the current prior, reducing the impact of stale planning data without requiring full reanalysis. Across continuous-control benchmarks, GEM-MPC consistently outperforms existing planning-based baselines under lower computational budgets.

---


### 126. [Balanced Prompt Adaptation against Entropy-Induced Collapse for Test-Time Binary Segmentation](https://arxiv.org/abs/2609.21743)

**<font color=#1a73e8>作者：</font>** Zhengshan Wang, Joshua Charles Webster-Ford, Yifei Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Entropy minimization is a standard objective for test-time adaptation (TTA), but it can fail in imbalanced binary segmentation. Unlike image classification, dense segmentation aggregates thousands of pixel predictions, allowing the larger predicted class to dominate the update, pull minority predictions toward itself, and produce a degenerate mask as predictions saturate and their entropy gradients vanish. We theoretically establish this collapse in a shared-shift model. This analysis motivates Balanced-Anchor Prompt Adaptation (BAPA), which combines two complementary modules. The Class-Balanced Anchors (CBA) module selects high-confidence anchors separately from each predicted class and gives foreground and background equal total loss weight, preventing the larger region from dominating the update. Dynamic Prompt Adaptation (DPA) refreshes these anchors after each prediction update and optimizes only text-side prompt residuals while keeping the vision-language encoders frozen. This prompt-only update refines the foreground-background decision boundary without altering the pretrained dense visual representation. Across experiments from four domains, BAPA achieves the highest mean Dice among the evaluated methods. Factorized ablations further validate the complementary roles of CBA and DPA, supporting balanced prompt adaptation as an effective alternative to entropy minimization for test-time binary segmentation.

---


### 127. [World Modeling in Transformers](https://arxiv.org/abs/2609.21748)

**<font color=#1a73e8>作者：</font>** Pierre Beckmann, Matthieu Queloz, Andre Freitas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavioral failures can make a transformer appear to lack a world model even when it has learned faithful representations of its environment. We demonstrate this in TaxiGPT, a transformer trained on random walks through Manhattan whose failures have been interpreted as evidence of an incoherent internal map. Through mechanistic analysis and causal interventions, we show that the model represents intersections and streets, tracks its position, and uses a goal compass to navigate. We trace its failures to interference between superposed intersection features, which disrupts localization within the internal map. Affordance packing, which groups representations of intersections with the same legal moves, helps limit the consequences of these errors. Finally, we propose mechanistic indicators that we use to compare models and show that world-modeling capacities emerge at different stages of training. Our findings motivate a shift from asking whether a model has a world model to mechanistically studying its world modeling: the interacting capacities through which it represents its environment and uses those representations to guide behavior.

---


### 128. [SFVO: Decoupled Confidence-Guided Stereo-Flow Visual Odometry with Bidirectional PnP](https://arxiv.org/abs/2609.21754)

**<font color=#1a73e8>作者：</font>** Kai Zhang, Guoyang Zhao, Jun Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based visual odometry (VO) has achieved significant progress, yet most existing methods focus on a monocular approach, which suffers from scale ambiguity. Stereo VO provides real metric by its nature, but remains less studied in deep learning VO due to its high computational cost and modeling complexity. Recent advances in stereo matching and optical flow estimation have made dense visual correspondence increasingly accurate and reliable, but their complementary geometric information has not been fully exploited for VO. In this paper, we present SFVO, a correspondence-driven stereo VO framework that directly builds upon pretrained stereo matching and optical flow models. SFVO exploits pretrained stereo matching and optical flow models to estimate stereo and temporal correspondences. Instead of learning pose directly from images, SFVO maps learned correspondences into geometric constraints and predicts which points are trustworthy. To improve the reliability of visual correspondence-based geometric constraints, we introduce decoupled confidence maps for rotation and translation. This design better aligns the characteristics of visual correspondence and 6-DoF transformations. Extensive experiments on outdoor and indoor datasets demonstrate that SFVO achieves robust and accurate pose estimation with strong generalization capability. The code will be released.

---


### 129. [Bilevel Optimization of Topology and Hyperparameters (BOTH)](https://arxiv.org/abs/2609.21758)

**<font color=#1a73e8>作者：</font>** Suryanarayanan Manoj Sanu, Miguel Anibal Bessa, Alejandro Marcos Aragón  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Topology optimization (TO) represents a significant step towards automating the design process: given a working simulation, TO can produce a viable prototype at the press of a button by differentiating the simulation and iteratively improving the design. In practice, however, TO is riddled with ``magic numbers''---hyperparameters whose tuning significantly affects the outcome. Finding the right values typically requires not only deep problem-specific knowledge but also extensive trial-and-error. While practitioners can use surrogate-assisted hyperparameter optimization as an alternative, this approach requires strictly limiting the number of hyperparameters through careful problem formulation. Here, we propose differentiating TO itself using automatic differentiation. This yields ``hypergradients'' that allow us to tune these hyperparameters in tandem with the primary optimization. We show that evaluating just one or two steps of TO is sufficiently informative and that the method scales favorably to thousands of hyperparameters at an expense comparable to only a few standard TO runs. We demonstrate this approach on stress-constrained and compliance problems, with the latter utilizing a neural parameterization of the density field.

---


### 130. [XCalib Depth-Guided Geometric Optimization for Dense Thermal-Visible Video Registration](https://arxiv.org/abs/2609.21770)

**<font color=#1a73e8>作者：</font>** Aurelien Godet, Gabriel Jobert, Mauro Dalla Mura  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image registration is a vital preprocessing step in multimodal perception tasks, including image fusion, object detection, and semantic segmentation. In Advanced Driver- Assistance Systems (ADAS), spatial misalignment between visible (RGB) and infrared (IR) cameras -caused by non-coincident optical axes and field-of-view differences- introduces non-uniform parallax and visual ghosting. Classical keypoint-based methods are restricted to global homographies that fail under dynamic depth, while unconstrained dense flow algorithms lack structural regularization and suffer from temporal instability. In this paper, we propose XCalib, an unsupervised dense thermal-visible registration framework that bridges this gap. Rather than serving as an absolute metric calibration tool, XCalib leverages virtual pinhole camera parameterization strictly as a geometric constraint space. By optimizing effective relative pose and intrinsics alongside predicted monocular metric depth, XCalib restricts the search space of spatial displacements to physically valid projection geometries. Our key contributions are: (1) a novel registration paradigm that uses camera parameterization as an implicit regularizer for dense cross-modal warping; (2) Normalized Edges Correlation (NEC), a robust structural similarity metric tailored to cross- spectral alignment; and (3) extensive quantitative and qualitative evaluations across public ADAS datasets, demonstrating superior temporal stability and alignment accuracy over unconstrained dense flow baselines.

---


### 131. [Notrix: Understanding Machine Learning Solutions Across Computational Notebooks at Scale](https://arxiv.org/abs/2609.21775)

**<font color=#1a73e8>作者：</font>** Xiaotian Su, Hongxin Fu, Xiaoyu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Computational notebooks make problem-solving visible, but typically only one notebook at a time. Meanwhile, in data science platforms like Kaggle, one competition can accumulate hundreds of notebooks. Effective collection-level analysis requires characterizing recurring solution patterns across all notebooks, as well as isolating specific notebooks for closer examination and learning. However, standard notebooks provide no common basis for this. Their workflows are nonlinear, cells declare no intent, and identical code can serve different ends, leaving hundreds of notebooks as separate documents. In this paper, we present Notrix, an interactive visual analytics tool for profiling hundreds of notebooks as one collection. Inspired by a formative study (N = 11), Notrix classifies every cell into one of thirteen machine learning (ML) stages, turning each notebook into a stage sequence, and clusters those sequences by structure rather than by code. To keep the representation constant as the scope narrows from the whole collection to a single cell, Notrix features three coordinated views---Workflow, Structural Matrix, and Detail---that appear at all four levels of granularity. In a within-subject study (N = 17) using two Kaggle collections of over 400 notebooks each, we observed participants answered questions about all notebooks more accurately with Notrix (median 88% vs. 50%) while opening 80% fewer notebooks per minute. Notably, four of the fourteen answered it without opening a single notebook (interaction logs, N = 14). Participants also reported significantly lower mental demand, temporal demand, and stress with Notrix (Holm-Bonferroni adjusted).

---


### 132. [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780)

**<font color=#1a73e8>作者：</font>** Xuanming Shang, Weijia Zhang, Chao Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D object detection from LiDAR point clouds faces a fundamental dilemma: voxel-based methods achieve efficiency at the cost of geometric quantization, while point-based methods preserve fidelity but suffer from prohibitive computational bottlenecks. Specifically, point-based architectures are crippled by slow downsampling strategies (e.g., FPS) and expensive dynamic neighbor queries (e.g., k-NN) coupled with costly continuous interactions. To tackle these systemic inefficiencies, we propose PointLAM, a highly efficient and powerful point-based architecture driven by two synergistic innovations. First, to resolve the downsampling bottleneck, we develop the Laplacian Point Sampler (LPS). LPS employs an implicit discrete Laplacian high-pass filter and Doubly Sorted Sampling to achieve fast, structure-aware foreground preservation. Second, to overcome local modeling latency, we design the Local Hadamard Aggregator (LHA). LHA decouples spatial indexing from feature representation using transient grids, and replaces complex continuous interactions with a Hadamard Gating mechanism for topology-aware, attentive modulation. By coupling this local gating with Bi-Directional Mamba (BDM) layers for global sequence modeling, we formulate the Local Attentive Mamba (LAM) block. Powered by this architecture, PointLAM achieves competitive performance on nuScenes and Waymo for point-based detectors. It rivals highly optimized voxel competitors while requiring a fraction of the computational footprint, demonstrating marked superiority in detecting small instances and handling extreme sparsity. Project page: this https URL.

---


### 133. [Per-Aetiology Contrastive Severity Embeddings with Phonological Pseudo-Labelling for Multilingual Dysarthric Speech](https://arxiv.org/abs/2609.21789)

**<font color=#1a73e8>作者：</font>** Bernard Muller, Antonio Armando Ortiz Barrañón, LaVonne Roberts  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most multilingual dysarthria-severity systems either train on a single aetiology-language pair or pool heterogeneous aetiologies into one label space. We test that pooling assumption with four matched HuBERT-base contrastive embedding models under a shared backbone, training recipe, corpus registry and held-out evaluation: one mixed-aetiology baseline and three aetiology-specific models for cerebral palsy (CP), Parkinson's disease (PD) and amyotrophic lateral sclerosis (ALS). Training combines clinically labelled speech with ordinal pseudo-labels from a training-free phonological profiling method [1], [2]. On speaker-disjoint, leakage-filtered held-out subsets, the per-aetiology models outperform the mixed baseline across all three target aetiologies: CP (macro F1 0.829 vs 0.676, +22.6 % relative), PD (0.715 vs 0.511, +40.0 %) and ALS (0.788 vs 0.596, +32.3 %). On CP, adding 144 SAP and 44 CDSD pseudo-labelled speakers lifts macro F1 from 0.786 to 0.829 over a clinical-only CP model (+4.3 percentage points). Training data span three to seven languages per aetiology. We position this as a controlled comparison of label-space design choices and discuss pseudo-label calibration, split hygiene, and confidence-thresholded deployment as important limitations for future work.

---


### 134. [RegKT: Interpretable and Robust Deep Knowledge Tracing With IRT-Regularizer](https://arxiv.org/abs/2609.21791)

**<font color=#1a73e8>作者：</font>** Samuel Girard, Juan D. Pinto, Jill-Jênn Vie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As deep learning models continue to advance, knowledge tracing models have achieved higher accuracy. However, these gains come at the cost of reduced interpretability, which is crucial for practitioners in educational settings to adopt new methodologies. Additionally, deep learning models are prone to overfitting, particularly when dealing with the small datasets that are common in educational applications. In this paper, we propose a novel regularization technique designed to enhance the robustness of deep-learning-based knowledge tracing models, while simultaneously improving their interpretability. Our method addresses both the interpretability and overfitting challenges, making it more feasible for real-world educational applications.

---


### 135. [Comparing Hand and Controller Avatars with Hand Tracking and Controller-Based Interaction](https://arxiv.org/abs/2609.21799)

**<font color=#1a73e8>作者：</font>** Natalia Ocampo, J. Felipe Gonzalez, Robert J. Teather  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Previous research suggests that the congruency between common VR input devices - such as controllers or hand tracking - and their visual representations (e.g., hand or controller avatars) influences user experience and performance. However, the specific effects of input-avatar combinations remain underexplored. We study the effects of common input devices (hand tracking and controllers) and visual representations (hand and controller avatars) on performance and perceived success in target acquisition tasks. We included both grasping and pinching gestures across 16 combinations of input, avatar, and target size. Results indicate that hand tracking benefits from any form of visual representation - even when mismatched - achieving up to 5.8% greater accuracy compared to having no avatar, likely due to its reliance on visual feedback in the absence of a physical prop. Controllers were generally preferred and offered faster task completion. However, mismatched avatars had a stronger negative effect with controllers, particularly when the virtual gesture did not align with the physical action, leading to a 5.6% drop in accuracy compared to the matched condition - suggesting that inaccurate feedback can be more disruptive than having no avatar feedback at all.

---


### 136. [A Principled Approach to Unsupervised Anomaly Detection](https://arxiv.org/abs/2609.21800)

**<font color=#1a73e8>作者：</font>** James Myles, Matthew Baugh, Johanna P. Müller 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional unsupervised anomaly detection (UAD) methods are designed to flag or localise deviations from a normative distribution, ignoring the underlying generative mechanisms of the anomalies. Yet the nature of an anomaly is often as important as its presence. We reformulate UAD as a Bayesian inverse problem, in which the objective is to infer the most probable corruption responsible for each observation. Our framework yields a probabilistic anomaly score as the energy of the inferred corruption parameters, and serves as a principled recipe for developing new UAD algorithms. We derive several existing methods as instances of the general framework, each corresponding to the same energy score under different modelling choices. Experimentally, we study the framework's components in a controlled setting, and improve object-class AUROC on the MVTec AD dataset by 2.3% by adapting the underlying corruption model. Finally, we validate the framework on a brain MRI benchmark, achieving strong detection performance while producing estimates of pathology intensity, bias, and geometry. Code is available at this https URL.

---


### 137. [VideoReloc: Long-Term Indoor Video Relocalization against a Kilobyte-Scale Semantic Scene Graph](https://arxiv.org/abs/2609.21804)

**<font color=#1a73e8>作者：</font>** Qianru Li, Xuyang Chen, Xuqin Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given a compact semantic scene graph, long-term indoor video relocalization estimates a map-frame trajectory after lighting and furniture changes. Visual methods rely on appearance and become unreliable under these changes; localizing one frame at a time from object classes and geometry instead leaves sparse, ambiguous evidence. We introduce VideoReloc, whose adaptive clips use odometry to gather spatial evidence until object and motion criteria are met, adapting query length to the observed scene. Its run-level decision rechecks conflicting placements using evidence accumulated across connected clips, stabilizing the trajectory beyond adjacent-clip tracking. Hypothesis-first registration proposes poses from object triplets and verifies each using clip-wide object centers and box surfaces. Orientation-aware refinement uses box faces, gravity and wall directions to resolve ambiguity in camera orientation and refine the full pose. This reframes sparse-map relocalization as verification of spatially extended video queries, moving discriminative support from stored appearance to temporal context and permitting a 100 kB map of class-labelled boxes. On RIO10 and ReplicaCAD, the all-frame localization success rate at 1 m/10$^\circ$ is 73.5% and 61.1% under causal evaluation, rising to 90.6% and 74.8% with clip closure. The evaluated per-frame scene coordinate regressors reach up to 47.6% and 49.8%, respectively, with maps of 12.6-42 MB. Project page: this https URL

---


### 138. [An Agentic Just-in-Time Adaptive Intervention System for Personalized Sleep Support: Proof-of-Concept Study with N of 1 Data](https://arxiv.org/abs/2609.21805)

**<font color=#1a73e8>作者：</font>** Nick Rezaee, Chelsea Boccagno  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background: Just-in-time adaptive interventions (JITAIs) can use behavioral data to adapt support to changing contexts, but many rely on predefined rules and manual configuration.
Objective: We developed a proof-of-concept sleep JITAI using an AI agent to review personal data, evaluate reminders, adapt interventions, and record decisions for human review.
Methods: Running in Home Assistant on a configurable schedule, the agent follows a reusable skill file to review 30 days of sleep and behavioral data, including physical activity, smartphone use, and bedtime routines, to identify patterns and create or update automated reminders.
Results: Initial runs demonstrated technical feasibility, successfully completing data review and intervention decisions while limiting reminders to three per day and saving decision records.
Conclusions: Agentic AI may enable flexible, adaptive sleep JITAIs. The architecture supports future comparison with fixed or rulebased interventions, requires human oversight, and could extend to other health behaviors.

---


### 139. [MIST: Multimodal Survival Prediction with Genomic-Guided Histology Attention](https://arxiv.org/abs/2609.21811)

**<font color=#1a73e8>作者：</font>** Muhammet Sami Yavuz, Sabri Mustafa Kahya, Richard R. Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal survival models can combine complementary prognostic information from whole-slide images and genomic profiles, but effective fusion remains challenging amid external cohort shift and computational complexity. To address these challenges, we propose MIST, multimodal survival prediction with genomic-guided histology attention. MIST represents genomic features as tokens and allows them to query compact foundation-model-derived histology context tokens before survival prediction. This design enriches molecular information with histology context rather than merging separately encoded modalities only at the final stage. Training combines discrete-time survival prediction with genomic feature masking, WSI dropout, and paired WSI-genomics contrastive alignment. Across four external evaluations in colon, renal, lung, and glioblastoma cohorts, MIST improves external C-index over standard fusion baselines in the primary comparisons. These results support genomic-guided histology attention as a compact and effective strategy for multimodal oncology outcome prediction. Our code is available at this https URL .

---


### 140. [Matrix AdaGrad: Row-wise and Column-wise Adaptive Subgradient Methods](https://arxiv.org/abs/2609.21815)

**<font color=#1a73e8>作者：</font>** Wenpeng Zhang, Runsheng Yu, Peilin Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive optimization methods such as AdaGrad and Adam are widely used in modern neural-network training, but their adaptive scaling is primarily designed for vector-valued parameters and does not explicitly exploit matrix structure. Recent matrix-aware optimizers demonstrate the benefits of structured optimization, yet a general theoretical framework for deriving matrix-aware adaptivity comparable to that of AdaGrad remains lacking. In this work, we develop a general Online Mirror Descent framework with adaptive proximal functions for matrix-valued parameters, providing a principled approach to deriving matrix-aware adaptive optimization through online regret minimization. By introducing row-wise and column-wise matrix proximal functions and analyzing the resulting regret trade-off, we derive Row-wise Matrix AdaGrad (Row-AdaGrad) and Column-wise Matrix AdaGrad (Column-AdaGrad), with adaptive scaling determined by the accumulated row-wise or column-wise gradient norms. We establish regret guarantees and show that these matrix-aware bounds can be strictly tighter than those of entry-wise AdaGrad under structured gradients. Experiments on matrix factorization and deep neural-network training further demonstrate the benefits of aligning adaptive scaling with matrix structure, including improved optimization stability and trainability at larger learning rates and greater network depths.

---


### 141. [Object Detection Benchmarks are Incomplete: The Role of Label Errors and Annotation Uncertainty](https://arxiv.org/abs/2609.21822)

**<font color=#1a73e8>作者：</font>** Sarina Penquitt, Jonathan Klees, Antonia van Betteray 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While object detection has advanced through improved architectures and open-vocabulary models, we provide strong evidence that benchmark quality is limited by annotation incompleteness. Across four widely used datasets (COCO, Pascal VOC, Cityscapes, KITTI), re-annotation reveals substantial increases in annotated objects (e.g., up to +60% on KITTI and +40% on COCO), driven primarily by previously unlabeled small, occluded, or densely packed instances. While some differences arise from dataset-specific annotation conventions, we consistently find that missing annotations are the main source of label errors across all datasets. To achieve high data quality, we introduce a scalable annotation pipeline that emphasizes high recall and captures ambiguity through soft labels aggregated from at least 11 annotators per object. The resulting annotations improve coverage and align well with human calibration. We show that benchmark performance is highly sensitive to annotation quality, although model rankings remain largely stable. We introduce two large-scale benchmarks: (i) an uncertainty-aware object detection benchmark, and (ii) a label error detection benchmark grounded in real label errors. We show that current detectors are strongly depended on annotation quality and are misaligned with human perception. Current label error detection methods, which have been shown to perform well on synthetic noise, struggle to achieve high recall and precision on real label errors. Our results highlight the need for future object detection benchmarks to move beyond deterministic annotations toward high-recall, uncertainty-aware evaluation that maximizes valid instances and better reflects real-world ambiguity.

---


### 142. [Federated Deep Clustering Networks for High-Dimensional and Heterogeneous Data](https://arxiv.org/abs/2609.21829)

**<font color=#1a73e8>作者：</font>** Morris Stallmann, Charalampos S. Kouzinopoulos, Marcin Pietrasik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustering high-dimensional data is a fundamental task in unsupervised machine learning with applications to a variety of domains. In the centralized data scenario, this task is commonly solved using deep clustering methods that utilize deep neural network architectures to learn clustering-friendly latent space representations. In Federated Learning, where data is distributed between clients and is private, deep clustering methods are less explored. In particular, recently introduced federated deep clustering methods, despite showing very promising performance, still fall short in reliably providing good performance if data across clients are non-identically-independently distributed. In this work, we introduce a generalization of Deep Clustering Networks to the federated scenario, named FedDCN, that simultaneously optimizes a reconstruction loss and a clustering loss. To ensure robustness and latent space alignment in non-identically-independently distributed data scenarios, FedDCN generates synthetic data augmentations, and its learning objective includes a geometric regularization for latent space alignment. Through experimental evaluation, the effectiveness of the approach under IID and non-IID assumptions is demonstrated, and future research directions are identified.

---


### 143. [Reusing Latent Speech Representations for Query-Conditioned Topic Localization in Transcripts](https://arxiv.org/abs/2609.21844)

**<font color=#1a73e8>作者：</font>** Steffen Freisinger, Philipp Seeberger, Thomas Ranzenberger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long transcripts are costly inputs for downstream NLP systems and often contain irrelevant context. We study query-conditioned topic localization: predicting the sentence span in a transcript that best addresses a topic-title query. To improve span localization, we reuse ASR encoder states as sentence-level representations and fuse them with textual embeddings. This lets lightweight span locators exploit speech information without running a separate audio encoder. Experiments on two public datasets show consistent gains over text-only baselines, especially under strict boundary-matching criteria. Cross-dataset experiments further indicate that the benefits are strongest for structured or semi-structured speech, while gains on spontaneous speech are limited and mixed.

---


### 144. [Beyond Counting Blessings: Tracing the Evolution of Gratitude Practices and Technology Needs](https://arxiv.org/abs/2609.21853)

**<font color=#1a73e8>作者：</font>** Qiuyue, Zhong, Jeongah Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Gratitude technologies support well-being by prompting reflection on what people appreciate. But gratitude does not serve the same purpose in every circumstance: as life situations change, so does what people seek from it, and whether it feels appropriate at all. To understand how technology can adapt to and support such shifts, we conducted retrospective, artifact-elicitation interviews with 17 adults who had practiced gratitude for one to fifteen years. Participants' appraisals of their situations shaped what they needed, yielding six recurring practice patterns, including a boundary where gratitude felt forced. We contribute the Adaptive Gratitude Practice Model, which explains how appraisals shifted even within the same life situation, how participants adapted activities, modalities, and rhythms, lapsed under competing demands or emotional unreadiness, and resumed when gratitude again felt useful. Additionally, we derive design implications for situated support, self-understanding through past records, and relational care with changing life situations.

---


### 145. [Morphology-Aware Ambiguity Learning for Wafer Defect Decision Support](https://arxiv.org/abs/2609.21866)

**<font color=#1a73e8>作者：</font>** Seungjun Chu, Seokhyun Chung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wafer map defect recognition is commonly formulated as a fixed-taxonomy classification problem that assigns each wafer to a single defect class. However, some wafers exhibit morphologies near class boundaries, for which forcing a single prediction may be less informative than providing plausible diagnostic alternatives. This paper proposes a morphology-aware ambiguity learning framework that supports three diagnostic actions: automatic single-class diagnosis, assisted diagnosis with two plausible defect classes, and full review. Using the radial, angular, and geometric characteristics of training wafer maps, the framework constructs a class-level ambiguity matrix representing defect-class pairs with similar morphology and plausible diagnostic alternatives. It guides the model to learn plausible alternative classes rather than treating all incorrect classes equally. During inference, the matrix determines whether an uncertain prediction can be represented by a meaningful two-class diagnostic set or should be escalated for full review. Experiments on WM-811K show that the proposed framework outperforms conventional approaches in defect recognition and diagnostic decision support, providing meaningful two-class alternatives while reserving full review for cases with unresolved ambiguity. Illustrative cost analyses further show the potential cost advantage of the proposed routing strategy. The diagnostic behavior of the framework remains consistent across different backbone architectures.

---


### 146. [Comparing Haptic Feedback Across Hand Tracking and Controllers in VR Object Interaction Tasks](https://arxiv.org/abs/2609.21869)

**<font color=#1a73e8>作者：</font>** Natalia Ocampo, J. Felipe Gonzalez, Robert J. Teather 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Hand tracking offers natural VR interaction but lacks controllers' inherent tactile feedback, while haptic feedback across input methods remains understudied. We conducted a participant study comparing vibration, impulse, and no feedback in hand- and controller-based VR interaction across grasp-, pinch-, and tap-like gestures assessing performance, workload, and preference. A custom glove and controller-mounted device provided both feedback types, aiming for consistency across input modalities. Controllers were faster for grasp and pinch, whereas hand tracking was more accurate for pinch and preferred overall. Haptics had limited performance effects, although impulse reduced grasp accuracy with controllers. Participants preferred vibration and impulse over no haptic feedback, favouring vibration overall. Our findings reveal a more nuanced relationship between haptic feedback, input device, and interaction context than suggested by previous work.

---


### 147. [Neural Cellular Automata Learn General Features in their Hidden Channels](https://arxiv.org/abs/2609.21870)

**<font color=#1a73e8>作者：</font>** Etienne Guichard, Stefano Nichele  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep learning models achieve impressive generalization through over-parameterization, but this paradigm often struggles with overfitting and memorization in few-shot regimes. Neural Cellular Automata (NCAs) offer a highly parameter-efficient alternative, yet research has focused primarily on their output, leaving the role of their internal hidden channels largely unexplored. In this paper, we investigate the internal dynamics of NCA hidden channels and introduce a novel transfer-learning mechanism that injects a pretrained teacher's hidden states into a student model to guide early optimization. Evaluated on few-shot and scale-variant MNIST benchmarks, NCAs outperform comparable recurrent and feed-forward architectures, demonstrating superior generalization with a minimal parameter budget (~9,800 parameters). Mechanistic analysis reveals that the hidden channels decouple feature extraction from uniform classification consensus by absorbing morphological complexity and converging to mutually orthogonal states. Furthermore, we demonstrate that these hidden channels capture general, scale-invariant topological primitives rather than class-specific templates. This allows a student model to achieve strong few-shot performance on unseen classes using features transferred from a teacher trained only on a subset of digits (0-5). Our results highlight the potential of utilizing hidden-state dynamics as a robust, decentralized computational substrate for parameter-efficient transfer learning

---


### 148. [Chronosphere: Space-Time Tessellation of Local Climate Experts](https://arxiv.org/abs/2609.21872)

**<font color=#1a73e8>作者：</font>** Daniel Cher, Eric Xing, Kexing Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Chronosphere, a spatio-temporal neural field that learns representations of climate. A central challenge in geographic representation learning is modeling environmental processes whose spatial and temporal complexity varies widely. Yet existing location encoders typically fix a single level of detail everywhere. Global bases such as spherical harmonics spread capacity uniformly across space and time. Localized bases resolve only predefined regions. Learned tessellations adapt, but are inefficient at representing higher frequencies. Chronosphere unifies these approaches, pairing an adaptive tessellation of learnable sites on the spacetime torus $S^2\times S^1$ with a shared bank of local basis functions. Both where capacity is placed and how much detail each region carries adapt to the data, across space and time. Trained to reconstruct climatology, Chronosphere matches or leads state-of-the-art location encoders across spatial and temporal tasks, with the largest gains under spatial and temporal transfer.

---


### 149. [SFPF: Spatio-Frequency Polarization Fingerprint for Anomalous Wireless Device Detection](https://arxiv.org/abs/2609.21873)

**<font color=#1a73e8>作者：</font>** Xiaoxuan Huang, Jinlong Xu, Daoyuan Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Periodic inspection of deployed wireless devices is necessary because unauthorized hardware replacement may preserve communication functions, credentials, and logical identity, making anomalous devices difficult to detect. Such inspections are conducted under controlled measurement conditions to verify that each device remains consistent with its enrolled hardware state. Conventional radio-frequency fingerprint (RFF) may provide insufficient separation when replacement hardware closely resembles legitimate hardware, while a polarization fingerprint (PF) constructed at one observation direction may miss spatially nonuniform polarization changes. This paper proposes the spatio-frequency polarization fingerprint (SFPF), which jointly represents complex polarization responses over multiple frequencies and observation directions; conventional PF is its fixed-direction slice. We derive SFPF formation from hardware-dependent modal excitation, directional far-field radiation, and polarization projection. A first-order sensitivity analysis shows that the response to the same hardware change varies with both frequency and direction, motivating joint spatio-frequency acquisition. Electromagnetic simulations confirm the nonuniform spatio-frequency sensitivity and show that, under the same observation budget, SFPF improves normalized distance, Fisher score, and the inter-/intra-class ratio over PF by 17.7%, 45.8%, and 11.3%, respectively. Experiments show that SFPF consistently outperforms RFF and PF over 0--20~dB. At 15--20~dB, SFPF achieves anomalous-device F1 scores of 87.3--90.4% and AUROC values of 85.4--95.5%.

---


### 150. [Geometric Mean Pooling for Equal-Weight Multiplicative Coarse-Graining](https://arxiv.org/abs/2609.21876)

**<font color=#1a73e8>作者：</font>** Ang-Kun Wu, Fangdi Wen, Jingtao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As an alternative to the additive and extremal biases of average and max pooling, we introduce Geometric Mean Pooling (GMP), a signed pooling operator that combines the product of feature signs with the geometric mean of feature magnitudes. Motivated by local-to-global composition in quantum many-body physics, GMP retains both joint sign information and a characteristic multiplicative scale without introducing learnable pooling parameters. We show that non-overlapping hierarchical GMP preserves the corresponding global multiplicative statistic and evaluate it on synthetic sequence tasks, iterative coarse-graining, image classification, and molecular lipophilicity regression. On the synthetic tasks, GMP recovers product-based signals more accurately than average and max pooling and maintains predictive performance under the tested levels of multiplicative input noise. On image and molecular data, however, its effectiveness depends on the representation, target parameterization, and placement of local and global pooling. These results position GMP as a complementary, regime-dependent inductive bias for tasks in which equal-weight multiplicative composition is plausible, rather than as a universal replacement for standard pooling operators.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-179](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
