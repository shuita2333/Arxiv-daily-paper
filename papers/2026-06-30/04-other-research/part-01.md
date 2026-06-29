# 📦 其他研究 | 2026年06月30日

> 本类共 **160** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-160](./part-04.md)

---

### 1. [A Survey of Automated Presentation Coaching: Systems, Methods, and Open Challenges](https://arxiv.org/abs/2606.27380)

**<font color=#1a73e8>作者：</font>** Wen Liang, Li Siyan, Zackary Rackauckas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated coaching for oral presentations sits at the intersection of computer-assisted pronunciation training (CAPT), prosody modeling, and speech synthesis, yet no prior work has systematically surveyed and compared existing systems along these dimensions. This survey reviews and categorizes automated presentation coaching systems, spanning pronunciation tutors, fluency and prosody coaches, multimodal trainers, and conference Q&A practice tools. We introduce a five-dimensional task taxonomy - covering segmental pronunciation, lexical stress, suprasegmental prosody, pacing, and content faithfulness - and explicitly map surveyed systems onto it to reveal coverage gaps. We further review the core technical methods these systems employ: TTS-based exemplar generation and diagnostic methods for pronunciation, prosody, and fluency assessment. Key open challenges include the scarcity of annotated presentation corpora, achieving accent-fair feedback across diverse L1 backgrounds, and delivering low-latency diagnostics for real-time rehearsal.

---


### 2. [OverFlowLight: Real-Time Gridlock Prevention and Traffic Signal Optimization for Urban Intersections](https://arxiv.org/abs/2606.27381)

**<font color=#1a73e8>作者：</font>** Mingyuan Li, Boyang Huang, Tianqi Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Queue overflow, a severe consequence of urban traffic congestion, occurs when vehicle queues exceed intersection capacity, obstructing upstream traffic and triggering cascading gridlocks. Prevailing traffic signal control (TSC) algorithms, primarily optimized for throughput, often fail to address overflow during peak hours, exacerbating congestion and creating safety hazards. We propose OverFlowLight, a real-time framework designed to preemptively resolve overflow and enhance overall TSC performance. It first introduces a mechanism to accurately detect overflow in real-time by leveraging multi-modal sensing from cameras and radars. Upon detection, it dynamically generates and inserts dedicated overflow phases into the signal cycle to clear the blocking queues. This is orchestrated by a hybrid control design that combines rapid rule-based overflow intervention with controller back ends such as reinforcement learning (RL) for longer-horizon efficiency. We conducted extensive real-world deployments of OverFlowLight across 43 intersections in three major cities. The framework demonstrates seamless integration with existing RL-based TSC agents, highlighting its modularity and practical applicability. Empirical results show that OverFlowLight reduces overflow incidents by 60.4% and increases network throughput by 18.2% compared to deployed baselines. Furthermore, it substantially diminishes the need for manual intervention common with expert-tuned signal plans. This work presents the first practical, scalable, and data-driven framework for actively preventing traffic gridlock, offering a crucial component for building resilient and efficient urban transportation systems. Our demonstration videos, codes and datasets are available at the anonymous URL, this https URL.

---


### 3. [AI-Model Network: Concept, Current State and Future](https://arxiv.org/abs/2606.27382)

**<font color=#1a73e8>作者：</font>** Li Zhetao, Zeng Xiyu, Wang Jianhui 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While the primary function of computers lies in computation and processing, the core value of the Internet is rooted in sharing and collaboration. Computers create the Internet, and the Internet empowers the value of computers. The rapid development of the Internet, cloud computing, and big data is pushing artificial intelligence into the era of large models (LMs). However, the practical application of LMs is currently hindered by high training costs and deployment complexities, driving a shift toward lightweight, private, and domain-specific models. With the rapid proliferation and wide distribution of heterogeneous models, enabling effective interaction and collaboration among them has emerged as a critical bottleneck that urgently needs to be addressed in LM development. Drawing inspiration from the development of the Internet, this paper proposes the concept, vision, and system architecture of world wide AI-model network (AI-ModelNet). It is a novel paradigm that achieves interconnection, capability sharing, and collaborative reasoning by establishing pathways between models. We first briefly review the current state of single-model and multi-model research. Subsequently, the systemic vision and hierarchical architecture of AI-ModelNet are articulated, followed by validation of the framework's feasibility through a prototype system and diverse application cases. Finally, key directions for future research are discussed preliminarily.

---


### 4. [RANSAC Scoring Done Right](https://arxiv.org/abs/2606.27385)

**<font color=#1a73e8>作者：</font>** James Pritts, Felix Seegräber, Kevin Köser  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The most widely used RANSAC variants score candidate models by counting inliers or summing per-point scores that saturate beyond a residual threshold. Every such score requires a user-supplied parameter that is a function of the inlier scale, which must itself be estimated from contaminated data. We remove this dependence by reversing the usual order of inference: rather than estimating the scale and then scoring against it, we marginalize the inlier scale analytically in closed form under a conjugate Inverse-Gamma prior for a fixed inlier partition, then optimize over partitions. A single closed-form expression spans the non-informative Jeffreys limit and informative empirical-Bayes priors, so the same score adapts across data-rich and data-scarce regimes without any change to the algorithm. The proposed RANSAC score is the first in which the inlier scale is genuinely absent from the formula. The score admits O(N log N ) computation via sort-and-sweep. On a benchmark of nearly 70 000 image pairs spanning different two-view estimation problems and both engineered and learned feature pipelines, the proposed score exceeds the state of the art (RANSAC, MSAC, GaU, MAGSAC): it stays nearly flat under threshold miscalibration where baselines degrade, reaches near-optimal accuracy from as few as two validation pairs where baselines need ont he order of 100 times more,. and tightens its prior regularization as validation data grows scarce.

---


### 5. [SidConArena: An Environment Evaluating Agents in Open-Ended,Positive-Sum Bargaining Game](https://arxiv.org/abs/2606.27397)

**<font color=#1a73e8>作者：</font>** Yeqi Feng, Yuxin Chen, Tianxing He  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Evaluating LLM agents requires dynamic environments that go beyond static reasoning and zero-sum games. Real-world economic interaction is often open-ended and mixed-motive: agents must negotiate, create positive-sum surplus, compete for scarce assets, and plan under delayed returns. We introduce SidConArena, a new benchmark framework for evaluating LLM agents in open-ended, positive-sum bargaining. SidConArena formalizes a multi-player economy as a finite-horizon partially observable stochastic game with three coupled phases: natural-language negotiation with binding trades, deterministic converter-based production, and sealed-bid auctions for long-term assets. The framework combines structured observations, phase-aware agent dispatching, a neural-symbolic action interface, and asynchronous execution, enabling free-form interaction while preserving rule-grounded evaluation. Across homogeneous and heterogeneous tournaments, stronger frontier models achieve higher economic outcomes, yet agents still misvalue resources, bargain passively, and remain limited in long-horizon investment planning.

---


### 6. [Not All Relations Rotate Alike: Transformation-Aware Decoupling for Viewpoint-Robust 3D Scene Graph Generation](https://arxiv.org/abs/2606.27412)

**<font color=#1a73e8>作者：</font>** Jingjun Sun, Chaowei Wang, Zhirui Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Scene Graph Generation (3DSGG) represents 3D scenes as structured object-relation-object graphs, providing a compact relational abstraction for spatial understanding. In embodied intelligence settings, the same 3D scene may be observed by agents from viewpoints that differ by yaw rotations. However, current 3DSGG models often fail to produce relation predictions that follow the expected transformation behavior under such viewpoint shifts. This behavior reveals an empirical mismatch related to predicate-level transformation heterogeneity: directional predicates such as left, front, right, and behind should transform with the observation frame, whereas most contact, support, and semantic predicates such as standing on and attached to should remain stable. To reduce this mismatch, we propose Transformation-Aware Decoupling (TAD), a viewpoint-robust 3DSGG framework that decouples relation reasoning according to predicate transformation behavior and is supported by viewpoint-stable object representations. TAD decomposes relation reasoning into two parts: one learns cues that should stay stable across viewpoints, while the other learns directional cues that should change with the observation frame. The two parts are merged for standard multi-label predicate prediction. Transformation-specific descriptors and group-aware auxiliary supervision encourage the two branches to capture complementary relation cues. Extensive experiments on 3DSSG show that TAD achieves state-of-the-art robustness under yaw viewpoint changes without training-time rotation augmentation, while maintaining competitive performance under the standard benchmark. The project page is available at this https URL.

---


### 7. [Unified Zero-Shot Time Series Forecasting: A Darts Foundation](https://arxiv.org/abs/2606.27438)

**<font color=#1a73e8>作者：</font>** Zhihao Dai, Dennis Bader, Alain Gysi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Since its initial release in 2020, Darts has become a widely used open-source Python library for time series analysis. A series of foundation models have recently claimed accuracy improvements in zero-shot forecasting, promising a paradigm shift from training custom models to harnessing pre-trained general-purpose forecasters. Foundation models, however, are often released as isolated packages with fragmented interfaces and limited interoperability with common tooling, making joint evaluation and integration within complete pipelines difficult. In Darts, we developed a unified $\texttt{FoundationModel}$ class collection (Chronos-2, TimesFM 2.5, TiRex, PatchTST-FM) that provides standardized, full-cycle forecasting interfaces with minimal external dependencies for integrating foundation models into the ecosystem. Existing Darts pipelines can now use foundation models with only a name change; new pipelines can use them for zero-shot or fine-tuned forecasting, uncertainty estimation, and backtesting, combined with data processing and evaluation tooling, all within a unified framework.

---


### 8. [PairSAE: Mechanistic Interpretability from Pair Representations in Protein Co-Folding](https://arxiv.org/abs/2606.27440)

**<font color=#1a73e8>作者：</font>** Giosue Migliorini, Aristofanis Rontogiannis, Grigori Guitchounts 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models for structural biology have achieved remarkable performance in predicting biomolecular structure and show promise for the design of proteins and small molecules. Yet understanding which internal features drive their outputs remains challenging. Standard sparse autoencoders (SAEs), effective on transformer-style sequence embeddings, do not transfer cleanly to pairformer-like architectures: naively operating on pairwise representations yields a quadratic blow-up of features and obscures concepts distributed jointly across sequence and pair representations.
We introduce PairSAE, which summarizes pairwise tensors via an N-mode SVD into token-wise interaction roles, then uses a sparse autoencoder to learn a shared set of token-level features that decode into both sequence and pair representations. Evaluated on Boltz-2 activations for PLINDER protein-ligand complexes, PairSAE yields interpretable features that align with UniProt annotations and predict Boltz-2 affinity values. These results indicate that PairSAE links the latent space of foundation models for structural biology to interpretable structural concepts, clarifying what the model "knows" while avoiding pairformer-induced pitfalls that limit conventional SAEs.

---


### 9. [SemCityLoc: Aerial 6DoF Localization Using Semantic 3D City Models](https://arxiv.org/abs/2606.27444)

**<font color=#1a73e8>作者：</font>** Jingfeng Mao, Xuyang Chen, Qilin Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial 6DoF localization typically relies on precise GNSS signals or radiometrically rich 3D reconstructions, limiting scalability and on-board deployment. We propose SemCityLoc, a semantic-geometric alignment system that reframes aerial pose estimation as structured surface registration between foundation-model-derived visual priors and standardized LoD-compliant 3D city models. Instead of matching sparse contours or dense texture, our method aligns semantic surfaces and monocular depth with lightweight semantic 3D building models, increasing pose discriminability in repetitive and occluded urban environments. To enable accurate evaluation, we introduce SemCityLockeD, the first real-world benchmark combining centimeter-accurate UAV poses with standardized LoD1--LoD3 semantic city models and challenging low-altitude imagery. Experiments demonstrate substantial improvements over existing map-based approaches, improving recall by up to 36% and reducing mean positional error from 9.89m to 2.62m in challenging urban canyons. Our results indicate that semantically structured geometry provides sufficient and scalable constraints for high-precision aerial localization without radiometric scene reconstructions. The code and data are available at this https URL.

---


### 10. [Learning in Markovian bandits with non-observable states and constrained decision epochs](https://arxiv.org/abs/2606.27448)

**<font color=#1a73e8>作者：</font>** Thomas Hira, Victor Boone, Urtzi Ayesta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies the problem of regret minimization in Markovian bandits with \emph{non-observable states} and possibly \emph{constrained} decision epochs. The focus is restricted to a ``pure'' regret benchmark, that compares the performance of the learning algorithm to the best \emph{pure policy} which -- akin to optimal policies of stochastic bandits -- picks the optimal arm from start to finish without ever switching. We introduce a generalization of rested Markovian bandits, \emph{self-degrading Markovian bandits}, for which pure policies are always asymptotically this http URL show that without prior knowledge on the underlying bandit, the regret of algorithms that switch arms rarely necessarily scales super-logarithmically for every bandit, i.e., as $\omega(\log(T))$, where $T$ is the learning horizon. Despite the unreachability of the logarithmic regime, we design UCB-NOM, an optimistic algorithm inspired by UCB, of which the regret is nearly logarithmic. Lastly, we show that given prior knowledge on the Markovian bandit in the form of a bound on the bias functions of its arm, a proper instantiation of UCB-NOM achieves $O(\log(T))$ regret. We further show that this prior knowledge allows for a $O(\sqrt{T \log(T)})$ worst-case regret bound for UCB-NOM. Notably, our regret bounds do not depend on the number of states of the underlying Markov chains. Our findings suggest that the non-observability of states is a mild inconvenience in self-degrading Markovian bandits.

---


### 11. [Prism Transformer: Progressive Head Schedules for Hierarchical Attention Processing](https://arxiv.org/abs/2606.27449)

**<font color=#1a73e8>作者：</font>** Shubham Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-head attention conventionally partitions the hidden dimension equally across all heads at every layer, enforcing an identical representational subspace dimension (dh = dmodel/h) throughout the models depth. In this work, we identify this uniform allocation as a fundamental structural bottleneck: due to their restricted dimensional space, early-layer heads are unable to faithfully capture complex, high-dimensional contextual patterns. To resolve this, we introduce the Prism Transformer, a novel architectural paradigm that replaces the static, uniform head configuration with a progressive head schedule. By monotonically increasing the head count across layers, the Prism Transformer naturally establishes a local-to-global representational hierarchy: early layers leverage fewer, exceptionally wide heads to capture complex, local compositional patterns, while deep layers deploy many, narrow heads to decompose these patterns into specialized linguistic features. Crucially, this structural shift is parameter-neutral, compute-neutral, and introduces zero training or inference overhead, preserving identical weight matrices and FLOP budgets as the standard Transformer. Across three model scales (124M, 354M, and 757M), the Prism Transformer consistently outperforms uniform baselines, achieving consistent reductions in validation loss alongside consistent gains on downstream zero-shot benchmarks (including PIQA, HellaSwag, ARC-Easy, and WinoGrande). Our findings demonstrate that non-uniform subspace allocation unlocks latent capacity within the standard Transformer budget, enabling more effective use of model capacity.

---


### 12. [Operator Learning for Cubic Nonlinear Schrödinger Equation on Periodic Domains](https://arxiv.org/abs/2606.27459)

**<font color=#1a73e8>作者：</font>** Emmanuel E. Oguadimma, Victory C. Obieke, Xueying Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the cubic nonlinear Schrödinger (NLS) equation on two-dimensional flat tori with varying aspect ratios. In this formulation, the choice of aspect ratio governs the Fourier resonance structure, so rational and irrational geometries can exhibit different high-frequency cascade behaviors. We present a geometry-conditioned Fourier neural operator (FNO) for the cubic defocusing NLS equation, where the input consists of the real and imaginary parts of the solution together with the aspect-ratio parameter \(\omega^2\). The model is trained to approximate the one-step solution operator and is evaluated on unseen trajectories generated from random-phase initial data using Fourier pseudospectral method. Our numerical experiments show that the learned operator captures the main solution dynamics on both tori and reproduces the distinct Sobolev norm behavior of the two geometries, with stronger \(H^2\)-growth on the rational torus and more constrained behavior on the irrational torus, consistent with the findings of \cite{hrabski2021energy}. We perform ablation studies to examine the roles of retained Fourier modes, activation functions, Fourier-layer depth, and explicit geometry conditioning. The results indicate that including $\omega^2$ improves long-time predictive accuracy, especially for the rational geometry, and supports the use of geometry-aware neural operators for learning spectral-transfer phenomena in nonlinear dispersive partial differential equations.

---


### 13. [SelectAnyTree: A Promptable Instance Segmentation Model for 3D Forest LiDAR Point Clouds](https://arxiv.org/abs/2606.27491)

**<font color=#1a73e8>作者：</font>** Trung Thanh Nguyen, Daniel Lusk, Kilian Gerberding 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated instance segmentation of forest LiDAR point clouds is increasingly critical as forest monitoring moves toward scalable, detailed, 3D measurement. Yet, progress is constrained by label scarcity for tree instances; a single hectare can hold millions of points and hundreds of overlapping, complex crowns, making manual annotation from scratch with raw data laborious and error-prone. Annotations are often corrected from automatic pre-segmentations, but remain costly as these provide no interactive or AI-assisted refinement. Inspired by the promptable paradigm of foundation segmentation models, we propose SelectAnyTree, a promptable instance segmentation model that delineates any individual tree in a 3D forest point cloud from a few clicks. It introduces two key components: Click-to-query prompt encoder and Canopy Height Model (CHM)-guided first prompt. The former turns each click into a single content query, encoding its 3D position and positive/negative polarity together with a pooled local backbone feature. The latter provides treetops as a geometry- and ecologically guided first prompt without any user input. The resulting prompt query is then decoded into one tree mask by a state-space query decoder to efficiently capture long-range context in large-scale forest scenes with linear-time complexity. We evaluate SelectAnyTree in interactive and instance-level settings across seven diverse forest regions and an independent held-out test dataset, demonstrating strong generalization beyond the training domains. It segments a target tree to 78.2 Intersection over Union (IoU) from a single click, 24.8 points above the strongest promptable baseline, and reaches every accuracy target with the fewest clicks, while using far fewer parameters and less inference time than prior promptable models. The source code is available at this https URL.

---


### 14. [ReWorld: Learning Better Representations for World Action Models](https://arxiv.org/abs/2606.27504)

**<font color=#1a73e8>作者：</font>** Tianze Xia, Lijun Zhou, Kaixin Xiong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) model future environment evolution under action conditioning, offering a scalable paradigm for autonomous driving. However, existing approaches focus largely on model architecture design, and how a WAM can efficiently learn better world representations for planning remains underexplored. To address this gap, we propose ReWorld, the first representation learning framework specifically designed for autonomous-driving world action models. In WAMs, standard training supervises only the output ends of the generation and planning modules, leaving the intermediate representations that carry world knowledge to be shaped only indirectly, as byproducts of fitting these outputs. The core idea of ReWorld is to treat intermediate representations as direct targets of optimization, shaping them along three complementary dimensions. On the Video DiT responsible for generation, we impose future-predictive supervision on its intermediate representations. On the Action DiT responsible for planning, we first align its intermediate representations cross-modally with the video world representation, then further shape them to be discriminative around safety-critical boundaries via hard-negative supervision. In addition, we systematically analyze the effectiveness of existing representation learning methods in video generation world models, and discuss why their performance is limited on this task. Experiments on nuScenes and NAVSIM show that ReWorld improves fine-tuned video generation by 23.9% in FVD (81.3 to 61.9), raises closed-loop PDMS from 89.1 to 90.4 without any post-training such as RL or post-processing, and accelerates from-scratch convergence by approximately 2x.

---


### 15. [TruEye: Fine-Grained Detection of AI-Generated Human Subjects in Images](https://arxiv.org/abs/2606.27505)

**<font color=#1a73e8>作者：</font>** Jay Barot, Dan Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI generated images are proliferating across the Internet. While some are used for entertainment, others are weaponized for fraud and social engineering attacks on social media users. Existing detectors overfit to generators seen during training, treat detection as opaque binary classification, or rely on costly Large Language Models (LLMs) to explain their outputs. In this paper, we present TruEye, a novel model for fine grained detection and localization of AI manipulated or AI generated humans and scenes. Unlike conventional detectors that assign a single authenticity label, TruEye is the first to distinguish among five compositional categories of synthetic content, including the most challenging case in which a real human is composited into a real scene where they were never physically present. At its core is a mask conditioned dual stream transformer that separates human and scene tokens while preserving patch level spatial correspondence. Specialized reasoning within each stream and region gated cross attention enforce semantic coherence between subject and background, while token level supervision and global compositional classification yield robust, interpretable predictions without invoking an LLM. By restricting intra stream attention to semantically coherent tokens, TruEye also runs over $100\times$ faster than LLM based competitors. Experiments on 6 datasets and our newly curated FineSyn dataset, show that TruEye surpasses state of the art detectors with higher accuracy, faster inference, and stronger generalization to unseen AI generated or manipulated images.

---


### 16. [Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints](https://arxiv.org/abs/2606.27509)

**<font color=#1a73e8>作者：</font>** Huaiyuan Weng, Huibin Li, Chul Min Yeum  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this study, we develop a Structured framework for Gaussian Splatting (3DGS) with LiDAR integration (Structured-Li-GS). It is a lightweight Gaussian Splatting pipeline that leverages LiDAR-inertial-visual SLAM. Structured-Li-GS achieves high-quality 3D reconstructions with fewer Gaussians by training on accurate, dense, colorized point clouds. Gaussian primitives are anchored using sub-sampled point clouds, and their ellipsoidal parameters are initialized from local surface geometry. Our training strategy integrates a comprehensive set of loss terms, including photometric, flattening, offset, depth, and normal losses, guided by the dense point cloud, enabling accurate reconstruction without Gaussian densification. This approach produces up-to-scale, high-fidelity results with a moderate model size. For experimental validation, we develop a custom hardware-synchronized LiDAR-camera handheld scanner. Experiments on both benchmark datasets and our real-world in-house dataset demonstrate that Structured-Li-GS surpasses state-of-the-art methods while using fewer Gaussians.

---


### 17. [The Curse of Multiple Mediators: Hidden Interaction Effects in Activation Patching](https://arxiv.org/abs/2606.27510)

**<font color=#1a73e8>作者：</font>** Sankaran Vaidyanathan, David Arbour, Aaron Mueller 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation patching is the primary tool in mechanistic interpretability. It attributes causal responsibility for a model behavior to each of its individual components by estimating its natural indirect effect (NIE). Re-deriving the activation patching estimand from causal mediation analysis, we find that the NIE does not solely capture the causal effect through the specific component. It also contains interaction effects (INT) that measure how much the component's causal effect itself depends on the state of other components in the model. A natural response may be to try to eliminate INT by adjusting the estimator or unit of analysis, but each of these potential remedies has predictable failure modes. We demonstrate these failure modes in the GPT-2 IOI circuit; components whose causal importance is conditional on the state of other components are either invisible or artificially inflated, and INT variance explains the previously documented instability of faithfulness scores. We prove that INT scales with the distance between clean and patched component activations, is negligible when the model is locally affine, and decomposes combinatorially into pairwise and higher-order group interactions. Despite its inevitability, INT is not a nuisance to be eliminated, but rather a diagnostic for interpretability studies. Its individual and group-level magnitude and sign signal when causal conclusions are prompt-dependent, and when greedy NIE-based component ranking will miss mechanisms only discoverable through combinatorial search.

---


### 18. [Tessellating The Earth](https://arxiv.org/abs/2606.27514)

**<font color=#1a73e8>作者：</font>** Daniel Cher, Hamza Iqbal, Eric Xing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geolocation encoders, which map geographic coordinates to learned representations, are emerging as an effective means of capturing visual and non-visual characteristics from a latitude-longitude pair alone. However, existing approaches project coordinates onto fixed bases (e.g., spherical harmonics), allocating representational capacity uniformly and devoting equal resources to the open ocean and to a developing city. We introduce Tessellating the Earth (TTE), a location encoder built from learnable Spherical Voronoi partitions that concentrates representational capacity where it is needed in a fully differentiable, end-to-end manner. Each Voronoi site carries its own embedding and migrates during training toward discriminative areas. To bridge the gap between local spatial structure and global semantic understanding, we introduce \emph{global semantic tokens}: a set of shared learnable concept tokens that distill semantic knowledge from the satellite imagery into a compact vocabulary the location encoder can reference at inference, enabling geographically distant sites covering similar environments to share semantics. TTE sets a new state of the art for location encoders across a suite of geospatial classification and regression tasks, and achieves the strongest results when used as a geographic prior for fine-grained species classification on iNaturalist-2018. Code, and weights are available at this https URL.

---


### 19. [The Context-Ready Transformer](https://arxiv.org/abs/2606.27538)

**<font color=#1a73e8>作者：</font>** Mahesh Godavarti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce the context-ready transformer, a new recurrent neural network architecture built from a D-layer transformer block that pre-contextualizes each token before it enters the block. During left-to-right generation, a correction network combines the previous position's block output -- a cached summary of past context -- with the current token embedding, so the tokenenters the block already contextualized rather than as a raw embedding. At sequential inference, the correction chain makes the architecture a recurrent neural network. For training, we unroll the correction process K times over the full sequence, processing all positions in parallel at each step. A pretrained transformer can also be converted to a context-ready model by adding a zero-initialized correction FFN and fine-tuning. We evaluate across widths, depths, block sizes, and two datasets, with all comparisons against standard transformers, variants, and ablations. A D=5 model beats a 12-layer transformer while generating 1.7x faster on an A100. With K=10, a single-layermodel (D=1) beats a 6-layer transformer with a 2.6x inference speedup, and sequential inference matches parallel K=10 to within 0.01 PPL. The architecture benefits most from wide representations and long contexts. On a pointer-chasing task, D=1 trained with BPTT solves all 10 composition levels, while standard transformers exhibit staircase-like depth dependence.

---


### 20. [Beyond MoCap: Scaling Motion Tokenizers with Synthetic Human Motion for Generative Modeling](https://arxiv.org/abs/2606.27547)

**<font color=#1a73e8>作者：</font>** Yiwen Yan, Wanning He, Yu-Wing Tai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion generation models are fundamentally constrained by the limited diversity of motion capture datasets, which predominantly contain common, repetitive actions and fail to cover the long tail of complex human movements, resulting in a restricted motion vocabulary in learned latent representations and poor generalization to rare, compositional, and highly dynamic motions. In this work, we propose a framework for expanding the motion representation space by leveraging large-scale synthetic human motion, introducing a data generation pipeline that produces diverse, physically plausible motion sequences beyond the distribution of existing datasets and integrating it with a redesigned VQ-VAE tokenizer that adapts to this expanded motion space. Unlike conventional tokenizers trained on narrow data distributions, our approach jointly scales both the training distribution and the discrete codebook, enabling the model to capture a significantly richer set of motion primitives. We demonstrate that training with synthetic motion substantially improves the coverage and compositionality of the learned motion vocabulary, leading to consistent gains across motion generation tasks such as text-to-motion and motion continuation, while remaining fully compatible with existing frameworks including MotionGPT. Our results suggest that the primary bottleneck lies in the limited support of the learned motion representation, rather than model architecture alone. Scaling synthetic motion in tandem with representation learning offers a principled path toward more expressive, controllable, and generalizable human motion synthesis.

---


### 21. [Understanding Cross-Rig Generalization in Automotive Perception: a Multi-Rig Benchmark and Rig Variation Metrics](https://arxiv.org/abs/2606.27554)

**<font color=#1a73e8>作者：</font>** Tim Alexander Bader, Tim Dieter Eberhardt, Maximilian Dillitzer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based perception systems for autonomous driving are typically developed and evaluated using fixed sensor rigs, while real-world vehicle fleets exhibit substantial variation in camera placement, orientation, field of view, and camera count. This mismatch introduces a cross-rig domain gap in which only the geometric observation process changes. To study this effect under controlled conditions, we introduce Plentiful CARLA Camera Rigs, a benchmark that renders identical driving scenes under 14 systematically designed camera rigs. This setup enables direct analysis of cross-rig generalization without confounding changes in scene content or appearance. Using the benchmark, we analyze cross-rig transfer behavior of representative multi-view perception architectures and observe substantial performance shifts induced by geometric rig variation. To facilitate structured analysis, we further introduce two calibration-based descriptors derived from rig metadata: Rig Variance, capturing internal rig diversity, and Rig Contrastive Distance, measuring geometric discrepancy between rigs. Our experiments show that geometric rig differences strongly correlate with relative cross-rig performance shifts and that Rig Contrastive Distance provides a reliable proxy for ranking transfer difficulty between sensor rigs.

---


### 22. [Radar Guided Camera Verification for Automatic Emergency Braking Rethinking Object Detection in Radar Camera Fusion](https://arxiv.org/abs/2606.27556)

**<font color=#1a73e8>作者：</font>** Ram Charan Akula, Sivanathan Kandhasamy, Manikandan Ganesan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radar camera fusion is widely used in Automatic Emergency Braking AEB systems because radar provides reliable range and velocity measurements while cameras provide a proper visual confirmation of the objects . Most of the deployed systems perform this confirmation using computationally intensive object detectors. However, if the radar has already localized a target, the camera may only need to verify the obstacles presence rather than solving a full problem by identifying the object. Our work proposes a radar scoped edge density gate that performs obstacle verification within radar guided image regions of interest. This method requires no training data, model weights, or GPU acceleration and was integrated into a complete radar camera fusion AEB system with brake by wire actuation. Evaluated on a real instrumented vehicle across 72 driving sessions and 131,603 camera frames, the proposed approach reduced the camera search space by up to 98.7 percentage, achieved a mean processing latency of 0.121 ms per ROI, an AUC of 0.898, and a recall of 0.994. Across 33 staged threat scenarios, the complete AEB system recorded zero missed brake events.

---


### 23. [Productionized Fairness Measurement Under Privacy Constraints](https://arxiv.org/abs/2606.27558)

**<font color=#1a73e8>作者：</font>** Osonde A. Osoba, Yuzi He, Saikrishna Badrinarayanan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness measurements in the form of disaggregated evaluations often rely on demographic signals that are legally constrained or culturally sensitive. Race and ethnicity signals are among the more difficult signals to curate and use for this task. This paper presents Privacy-Preserving Probabilistic Race/Ethnicity Estimation (PPRE) as a method for enabling fairness measurements with respect to race/ethnicity for U.S.\ LinkedIn members in a privacy-preserving manner. PPRE applies privacy technologies (specifically: secure two-party computation, differential privacy, and additive homomorphic encryption) on top of two race/ethnicity demographic signal sources (the Bayesian Improved Surname Geocoding estimator and a sparse golden survey set of self-reported demographics) to power a fairness measurement solution with respect to US-based race/ethnicity demographics. We detail its privacy guarantees and demonstrate its application on candidate- and viewer-side fairness measurements. We close with a transferable framework for institutions seeking to implement similar privacy-preserving measurement infrastructure.

---


### 24. [Quantum Generative Diffusion Model for Real-World Time Series](https://arxiv.org/abs/2606.27561)

**<font color=#1a73e8>作者：</font>** Jack Waller, Filippo Caruso, Dimitrios Makris 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models have achieved remarkable success in data synthesis, though recent advances driven by increasing model scale have introduced challenges in computational cost and efficiency. Quantum machine learning offers a promising alternative, representing complex data distributions using compact, highly expressive models. Here, we propose QDiffusion-TS, the first quantum generative diffusion model for time series synthesis, and validate it on the IQM quantum processor. The framework extends a classical diffusion architecture by replacing feed-forward components within the denoising transformer with quantum neural networks, yielding a hybrid quantum transformer that reduces the number of trainable parameters in each replaced component by nearly three orders of magnitude. Evaluated on financial time series from Apple and Amazon, the model generates synthetic data that more accurately reproduces the real distributions, reducing Wasserstein distance by approximately 44% relative to its classical counterpart across both datasets. In a downstream forecasting task, augmentation with the generated data improves predictive performance by up to 71% in RMSE over a baseline trained solely on real data. These results show that quantum enhanced architectures can consistently match and frequently surpass classical performance with substantially fewer parameters, establishing a practical framework towards more efficient and scalable data-driven generative modelling.

---


### 25. [On the Inseparability of Instructions and Data in Shared-Embedding Sequence Models](https://arxiv.org/abs/2606.27567)

**<font color=#1a73e8>作者：</font>** Dewank Pant, Shruti Lohani, Avijit Kumar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection is the top security risk for LLM-integrated applications, yet every defense proposed so far has been broken. We prove this is not a coincidence: in shared-embedding architectures that lack enforced control-data separation, perfect prompt-injection prevention is mathematically impossible. We formalize prompted systems as Prompted Action Models whose outputs include control-authoritative actions: refusal decisions, tool authorization, policy routing, and memory writes. We define Semantic-Faithful Control (SFC), the property that such behavior depends only on the meaning of untrusted input, not on how it is encoded. We then prove SFC is unachievable within the shared pipeline, via three results: a provenance-recovery impossibility (shared representations make trusted and untrusted content statistically inseparable, bounded by total variation distance); control-path exposure (untrusted tokens enter control-relevant computation through the same attention value-aggregation that determines outputs); and a finite-coverage invariance gap (finite training cannot certify invariance over infinite semantic-equivalence classes). We ground each quantity in measurements on production tokenizers and models.
The result is structural, not a gap in current defenses. It mirrors the code-data confusion in Von Neumann machines that gives rise to buffer overflows, a vulnerability class that took decades of layered defenses (DEP, Write-XOR-Execute, ASLR, stack canaries, and ultimately memory-safe languages) to contain, because no single mechanism sufficed. The implication is the same: prompt injection cannot be eliminated by better in-pipeline classification or alignment alone. It requires architectural separation of instruction and data channels. We identify the root cause and the class of solution it demands.

---


### 26. [DeLux: Cross-Modal Local Artifact Restoration in Video Using Neuromorphic Data](https://arxiv.org/abs/2606.27576)

**<font color=#1a73e8>作者：</font>** Bartosz Stachowiak, Dariusz Brzezinski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional RGB cameras suffer from lighting artifacts such as flare, glare, flicker, and overexposure, leading to irrecoverable information loss that necessitates computational restoration. However, existing approaches treat these problems in isolation, failing to recover structural details completely obscured by complex spatially discrete image degradations. In this paper, we propose a novel cross-modal restoration paradigm and present DeLux, a modular proof-of-concept pipeline that leverages neuromorphic event streams as a structural prior to guide the targeted detection and inpainting of lighting artifacts in RGB video. Validation on synthetic benchmarks and real-world automotive footage demonstrates that DeLux effectively suppresses local artifacts and restores affected regions. The proposed approach outperforms existing RGB-only baselines and event-guided HDR models, achieving an average MS-SSIM of over 0.99 across all artifact types and demonstrating up to an 88% reduction in artifact severity in real-world automotive footage. The synthetic artifact generation tools and curated real-world evaluation datasets are made publicly available to foster future research on cross-modal restoration.

---


### 27. [hia-gat: A Heterogeneous Interaction-Aware Graph Attention Network For Frame-Level Traffic Conflict Risk Prediction On Freeways](https://arxiv.org/abs/2606.27577)

**<font color=#1a73e8>作者：</font>** Mahshid Malazizi, Seyedmehdi Khaleghian, Mina Sartipi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper formulates frame-level freeway risk assessment as a multi-agent scene graph-level binary classification problem, where each video or trajectory frame is labeled risky if any TTC- or PET-based conflict violates a specified severity threshold. We construct a relation-aware graph per frame with vehicles as nodes and two interaction types as edges: same-lane (longitudinal) and adjacent-lane (lateral), augmented with physics-informed edge features aligned to rear-end and lane-change conflict mechanisms. Building on a structured benchmarking suite of non-graph models and graph baselines, we propose HIA-GAT, a dual-stream heterogeneous graph attention network that processes longitudinal and lateral interactions through dedicated attention pathways and fuses them via a conflict-type-aware gating mechanism with event-level gate supervision derived from SSM conflict attribution. Experiments on the NGSIM I-80 and US-101 freeway datasets across nine TTC and PET threshold configurations show that HIA-GAT achieves the best average risk-ranking performance (AUC 0.835 on I-80 and 0.867 on US-101), with the largest gains on PET-only (lane-change) settings where relational structure is essential. Beyond accuracy, the learned gate provides interpretable per-vehicle attribution of dominant conflict type, supporting actionable, real-time freeway safety monitoring. We show that graph structure is critical for modeling lateral conflict risk, while longitudinal risk can often be captured by non-relational aggregation.

---


### 28. [Distribution-based deep multiple instance learning for tumor proportion scoring in NSCLC](https://arxiv.org/abs/2606.27579)

**<font color=#1a73e8>作者：</font>** Krzysztof Pysz, Artur Bartczak, Jarosław Kwiecień 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate assessment of tumor proportion score (TPS) in non-small cell lung cancer (NSCLC) is critical for treatment planning and prognosis. Key challenges include the tedious manual work required to annotate each slide, combined with the limited number of experts certified for this task. Multiple instance learning (MIL) has proven to be an effective approach for predicting TPS scores at the slide level; however, existing methods struggle with non-expressive (zero class) images. Our approach involves two models: (1) an embedding-extraction and multiclass-classification network that captures the histopathological features of individual patches, and (2) a MIL model that aggregates these embeddings to predict zero-inflated beta (ZIBeta) parameters representing the overall TPS probability distribution for the entire slide. Using only slide-level TPS scores as labels, we demonstrate how this end-to-end framework can leverage a novel distribution-based architecture to improve prediction accuracy and explainability. ZIBeta modeling significantly outperforms baseline linear and ridge regression while capturing expected accuracy through distribution concentration.

---


### 29. [Beyond Points: Spherical Distributional Part Prototypes for Interpretable Classification](https://arxiv.org/abs/2606.27582)

**<font color=#1a73e8>作者：</font>** Duarte Leão, Diogo Pereira Araújo, Catarina Barata 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prototype-based neural networks aim to provide intrinsic interpretability by grounding predictions in a small set of part prototypes. However, modern vision backbones typically operate in normalized, directional embedding spaces where each semantic part exhibits substantial intra-class variability. As a result, point prototypes often become redundant or unstable, hurting both explanation quality and robustness. We propose vMFProto, a distributional part-prototype framework that models each class as a mixture of von Mises-Fisher components on the hypersphere. Each prototype learns its own concentration, capturing part-specific variability, and we use entropic optimal transport (OT) to obtain structured patch-to-prototype assignments. A two-stage training schedule performs OT-driven prototype discovery followed by end-to-end refinement with patch-level distillation and distribution-aware diversity regularization. Experiments on CUB-200-2011, Stanford Dogs, and Stanford Cars with frozen DINO backbones show that vMFProto achieves state-of-the-art explanation quality (consistency, stability, and distinctiveness) with competitive accuracy. Qualitative results confirm that vMFProto yields localized, non-redundant part evidence.

---


### 30. [CoIn: Comprehensive 2D-3D Inpainting with Gaussian Splatting Guidance](https://arxiv.org/abs/2606.27584)

**<font color=#1a73e8>作者：</font>** Hana Kim, Minje Kim, Tae-Kyun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene inpainting is essential for reconstructing areas corrupted by occlusions or limited viewpoints. While recent methods leverage Gaussian Splatting (GS) for efficient 3D editing, they often depend on precise multi-view segmentation masks and are inherently constrained to object removal tasks. We propose CoIn, a novel framework that bridges 2D inpainting models and 3DGS through a multi-stage consistency pipeline. Our approach first generates initial inpainted images using a diffusion model, enabling the use of arbitrary-shaped masks and diverse tasks like object insertion. We then introduce Reference Adaptive GS with Feature Attention to reconstruct a coarse 3D scene by adaptively weighing towards a reference view (2D -> 3D). This 3D representation provides geometric guidance to the diffusion process via GS-based Reference Feature Warping, ensuring multi-view consistency (3D -> 2D). Finally, a Texture-Enhancing Discriminator refines the 3D scene to achieve high photometric realism (2D -> 3D). Experiments show that CoIn, effectively leveraging bidirectional information flow, achieves state-of-the-art performance and effectively handles both object removal and object insertion with flexible mask input.

---


### 31. [Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents](https://arxiv.org/abs/2606.27595)

**<font color=#1a73e8>作者：</font>** Minbyul Jeong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web-agent benchmarks overwhelmingly measure depth -- pinning one obscure answer behind a chain of constraints -- while breadth, exhaustively enumerating a closed set and filling each item's attributes, is barely evaluated, especially outside English. Breadth is also hard to build: certifying that a gold set is complete and every cell correct is far costlier than checking a single answer. I introduce \textsc{Ko-WideSearch}, a Korean breadth-search benchmark built by an automated synthesize-and-verify pipeline. Each task names a set-parent entity -- a TV season, a dynasty, a league, an administrative region, an election -- and asks for its full membership plus a per-item attribute table, graded by Item-, Column-, and Row-F1. It spans 228 tables over 190 entities and sixteen categories across three difficulty tiers, set by two structural knobs I dial independently -- table width and a 2-D composite key -- so cross-product membership climbs from 0\% to 100\% across the tiers. A single normalization-aware comparator is shared between gold construction and grading, so stable date and count columns are not over-dropped on formatting alone. Across twenty web agents, the failure is consistent: agents recover the set but not the rows (e.g.\ Item-F1 92.8 against Row-F1 53.7), accuracy falls steadily as the knobs harden, and neither more search nor more spend closes the gap. Broken down by cell, the hard part is finding the right value, not formatting it: open-ended free-text cells fail most, while cells with a standard answer such as a date or a name usually come out right.

---


### 32. [Narrative-UFET: Narrative Generation for Ultra-Fine Entity Typing](https://arxiv.org/abs/2606.27598)

**<font color=#1a73e8>作者：</font>** Mreedul Gupta, Advait Deshmukh, Ashwin Umadi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ultra-fine entity typing (UFET) assigns highly specific types to entity mentions, but current approaches struggle with types in the long tail. We hypothesize that a key limitation is the reliance on sentence-level context, since disambiguating evidence is often spread across multiple sentences. Testing this has been difficult because all existing UFET resources are sentence-level. We present Narrative-UFET, a controlled extension of UFET in which each entity mention is paired with an automatically generated short, coherent narrative. Synthesizing narratives lets us isolate the effect of specific discourse properties. We experiment with two paired variants: one in which the entity's type is held constant across the narrative (Maintain) and one in which it shifts (Change). We show that narrative context yields consistent improvements on long-tail types over sentence-level baselines, with the Change variant providing the stronger signal. A comparison against naturally occurring contexts shows that synthetic narratives yield stronger gains, indicating that controlled discourse construction can surface signals that real text leaves implicit. Substantial room for improvement remains, suggesting open directions in both discourse modeling and narrative construction.

---


### 33. [Global Explanations for Multivariate Time Series Forecasting Models via $K$-Order Markov Approximations](https://arxiv.org/abs/2606.27599)

**<font color=#1a73e8>作者：</font>** Amadeo Tunyi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While many explainable AI (XAI) methods have been proposed, most are not designed for time-series forecasting models and often rely on the implicit assumption that timestamp features are independent. This assumption ignores the fundamental property of temporal dependence and can lead to explanations that violate the sequential and causal structure of the data. We introduce \textsc{KARMA}, a method for explaining time-series predictors by constructing a Markov surrogate model that captures the temporal dependencies learned by the predictor. Our approach revolves around three main aspects: identifying the minimal history length $K$ that is predictively sufficient for the model, estimating the best-fitting $K$-order Markov transition kernel from the discretized history space, and a five-level global explanation hierarchy that can be derived from the Markov transition kernel, which we illustrate using real-world weather data (Beijing PM 2.5). We also certify using complex synthetic data with known true causal edges that KARMA (i) recovers the data causal structure as learned by the model via a controlled experiment and (ii) identifies temporal dependencies better than established attribution methods such as TimeSHAP.

---


### 34. [Training Observable Control Policies to Expose Agent State Through Actions](https://arxiv.org/abs/2606.27609)

**<font color=#1a73e8>作者：</font>** Andres Enriquez Fernandez, John J. Bird  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical or operational constraints often impose communications limitations on autonomous agents. Such limitations complicate monitoring or multiagent coordination. Even when strong communications are absent, some information may still be available. The remainder of the relevant agent state may be reconstructed via estimation. The actions taken by an agent are a potential source of information -- as the agent interacts with the environment, these actions may be observed even in the absence of explicit communication. We investigate using actions to estimate the state of an agent, using reinforcement learning to develop policies which make the estimation problem more tractable. Policy observability is encouraged through the training reward and is analyzed using simulation of the trained agent. In an aircraft tracking problem a policy with enhanced observability is found that has minimal impact on nominal task performance.

---


### 35. [Masked Language Flow Models](https://arxiv.org/abs/2606.27617)

**<font color=#1a73e8>作者：</font>** Iskander Azangulov, Kianoosh Ashouritaklimi, Leo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked Diffusion Models (MDMs) promise fast, parallel language generation, but their reverse transition factorises across token positions -- an approximation that breaks down in the few-step sampling regime where parallel generation ought to provide the greatest efficiency gains. Flow Language Models (FLMs) sidestep this limitation by learning a continuous flow that transports noise toward clean sequences represented in Euclidean space, inducing a flow map that can be distilled for single-step generation. However, this makes complex tasks requiring multi-step reasoning problematic for FLMs, as FLMs are forced to decode every token during generation. To address this, we introduce Masked Language Flow Models (MLFMs), which incorporate masking into FLMs using a continuous stochastic interpolant to bridge partially masked and clean sequences. This design enables conditional generation via continuous flows and allows pretrained MDMs to be converted into MLFMs through a simple, lightweight adaptation. Leveraging this flexibility, we propose a novel sampler that alternates continuous denoising with the discrete unmasking of confident tokens to better support multi-step reasoning. We evaluate our approach on GSM8K and MT-Bench and find, for the first time, that flow-based language models can be scaled to solve downstream reasoning and instruction-following tasks.

---


### 36. [FoggyTrust: Robust Federated Learning with Hierarchical Trust Networks](https://arxiv.org/abs/2606.27622)

**<font color=#1a73e8>作者：</font>** Emmanuel Rassou, Tomas Gonzalez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Byzantine-robust federated learning seeks to protect distributed model training from malicious or corrupted clients without requiring access to their private data. FLTrust addresses this challenge by introducing a trusted server-side root dataset that assigns trust scores to client updates for more robust aggregation. In this work, we propose FOGGYTRUST, a hierarchical extension of FLTrust that localizes trust computation to fog nodes, allowing the framework to better handle globally heterogeneous data while preserving robustness within locally homogeneous client groups. We further show that this two-level architecture can simultaneously address distribution mismatch in trust estimation and client drift across groups by combining local trust-based aggregation with heterogeneity-aware global optimizers such as FedAdam and SCAFFOLD. Across benchmark datasets, FOGGYTRUST achieves its strongest gains on more challenging heterogeneous settings, particularly on CIFAR-10 under Krum and Trim attacks, where it achieves an over 50% improvement over FLTrust. We also test FOGGYTRUST in a real-world safari dataset to show the promise of hierarchical trust networks for robust federated learning in socially impactful, safety-critical settings such as distributed wildlife monitoring.

---


### 37. [Cross-Platform Chinese Offensive Comment Detection via Dual-Threshold Hard Example Mining](https://arxiv.org/abs/2606.27629)

**<font color=#1a73e8>作者：</font>** Ruixing Ren, Junhui Zhao, Fangfang Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-platform deployment of offensive comment detection for Chinese social media suffers performance degradation. The paper proposes a dual-threshold hard mining method to address this. First, the clean-Chinese-base RoBERTa is finetuned on COLD to establish a binary baseline for fair comparison. Second, a three-class fine-labeled test set covering Weibo, Xiaohongshu, Tieba, and Zhihu is constructed, domain distances from the source are quantified using Jaccard and Proxy-A Distance, as well as the degradation bottleneck of the baseline under domain shift is systematically revealed. Herein, a dual threshold hard example mining strategy is proposed. High- and low-confidence error-prone samples are filtered from unlabeled corpora by prediction confidence. The model is secondarily finetuned under implicit contexts with merely a small set of manually labeled hard examples, realizing low-cost cross-platform domain adaptation. Experiments reveal significant performance gains of the optimized model across four platforms.

---


### 38. [Denoising ICF Images with Multiplicative Uniform Noise: A Self-Supervised Study Based on the Log-Domain Noisier2Inverse Framework](https://arxiv.org/abs/2606.27635)

**<font color=#1a73e8>作者：</font>** Gyeongha Hwang, Bradley Thomas Wolfe, Naima Naheed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper documents the implementation and evaluation of a self-supervised denoising framework on Inertial Confinement Fusion (ICF) images corrupted by Multiplicative Uniform noise: the \emph{Log-Domain Noisier2Inverse} framework. This framework is developed and analysed in this work; the key theoretical result -- that minimising the log-domain self-supervised loss is equivalent to supervised learning in the transformed domain -- is presented with full proof. We document significant implementation challenges arising from the unique characteristics of ICF imagery, describe the fixes applied at each stage, and report final quantitative results. The log-domain approach with per-image JSON Uniform noise loading (Variant~B) achieves the best result: a mean PSNR of $21.41\db$ and SSIM of $0.8358$, a $+19.46\db$ improvement over the noisy input baseline of $1.95\db$, substantially outperforming BM3D log-domain ($4.47\db$, SSIM $0.5181$) and Noise2Self ($4.75\db$, SSIM $0.0177$). Variant~A, using fixed Gaussian noise loading, achieves $21.39\db$ PSNR and SSIM $0.8436$. Of the three evaluated methods, Log-Domain Noisier2Inverse and Noise2Self are entirely self-supervised during training, requiring no clean ground truth data; BM3D is a classical filter-based method requiring no training at all. The clean reference images are used solely for quantitative evaluation of all three methods.

---


### 39. [AI-Generated Image Recognition via Fusion of CNNs and Vision Transformers](https://arxiv.org/abs/2606.27637)

**<font color=#1a73e8>作者：</font>** Xuan-Bach Mai, Hoang-Minh Nguyen-Huu, Quoc-Nghia Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in synthetic data technology have opened a new era where images of remarkable quality are generated, blurring the lines between real-life images and those produced by Artificial Intelligence (AI). This evolution poses a significant challenge to ensuring the reliability and authenticity of data, underscoring the need for robust detection methods. In this paper, we present a robust approach aimed at addressing these pressing concerns. Our methodology revolves around leveraging fusion strategies, combining the strengths of multiple detection methods for identifying AI-generated images. Through extensive experimentation on the CIFAKE dataset, our model showcases remarkable performance, achieving an impressive accuracy rate of 97.32%. This accomplishment underscores the efficacy of our approach in accurately distinguishing between AI-generated images and real-life images, thus contributing to the advancement of data authentication techniques amidst the proliferation of synthetic data.

---


### 40. [TeRoR: Decoupled Temporal Rotation with Relational Circular Region for Temporal Knowledge Graph Embedding](https://arxiv.org/abs/2606.27651)

**<font color=#1a73e8>作者：</font>** Peijia Xie, Yike Liu, Chao He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, with the emergence of Temporal Knowledge Graphs (TKGs), research on learning entity and relation representations in TKGs has attracted increasing attention, giving rise to a large number of TKG embedding methods. TeRo is a simple and efficient temporal knowledge graph embedding approach. However, TeRo does not do well in modeling the mapping properties of various relations, such as one-to-many, many-to-one, and many-to-many. Meanwhile, it also has limitations in the expression of temporal information. To address these issues, we propose a novel TKG embedding method named TeRoR. This method divides the temporal evolution of entity embeddings, and conducts independent rotation transformations on head and tail entities in the complex vector space to strengthen temporal information modeling capacity. In terms of relational characteristics, we train a radius to constrain the rotated and translated head entities within a circular region centered on the tail entity, which effectively captures the diverse mapping properties of relations. Experimental results demonstrate that TeRoR achieves competitive performance against state-of-the-art models on four distinct TKG datasets.

---


### 41. [Temporal-Emerged Prompting for Segment Anything in Multiframe Infrared Small Target Detection](https://arxiv.org/abs/2606.27655)

**<font color=#1a73e8>作者：</font>** Yinghui Xing, Donghao Chu, Shizhou Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately localizing and segmenting small targets in low signal-to-noise ratio (SNR) infrared sequences remains a challenging task. Since targets are often indistinguishable from the background in individual frames, existing methods, even when equipped with advanced foundation model and powerful inter-frame association mechanisms, still fail to detect them. Motivated by the observation that targets tend to emerge gradually from the background over time and become distinguishable, we propose Temporal-Emerged Prompting for Segment Anything Model (TEP-SAM), a principled framework designed to explicitly exploit such temporal-emerged cues to modulate and prompt SAM. TEP-SAM operates by jointly modeling global motion patterns and local motion deviations to locate potential targets. It further enhances target region features by leveraging motion discrepancy, thereby generating temporal-emerged cues for SAM and enabling non-interactive segmentation. By bridging large-scale semantic pretraining with task-specific temporal modeling, TEP-SAM effectively adapts SAM to the challenging multiframe infrared small target detection task. Extensive experiments demonstrate the effectiveness of our approach, particularly under severely low-SNR conditions and in complex dynamic background.

---


### 42. [GeoFace: Consistent Multi-View Face Generation with Geometry-Constrained Diffusion](https://arxiv.org/abs/2606.27659)

**<font color=#1a73e8>作者：</font>** Yeji Choi, Jinhyeok Choi, Jaewon Min 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present GeoFace, a geometry-constrained multi-view diffusion framework for consistent face generation from a single input. % While recent multi-view diffusion models achieve photorealistic synthesis at the per-view level, they lack an explicit mechanism to enforce a shared 3D structure across views, often leading to inconsistent geometry across viewpoints. To address this, GeoFace proposes a unified dual-stream framework for joint generation of multi-view RGB images and 3D face geometry, where the appearance and geometry streams interact through shared attention layers. To encourage the two streams to mutually constrain each other, we introduce a geometry-guided attention alignment loss that supervises the cross-attention between appearance and geometry tokens with 3D-consistent correspondences, enabling the appearance stream to correctly reference pose-invariant geometric cues for robust alignment across viewpoints. Geometry is represented as a canonical UV position map, derived from a FLAME mesh fitted to multi-view observations, serving as a view-invariant shared constraint across all generated views. Experiments on RenderMe-360 and NeRSemble demonstrate that GeoFace consistently outperforms existing methods in both visual quality and cross-view geometric consistency, facilitating more efficient 3D reconstruction.

---


### 43. [Explainable AI for Biodiversity Monitoring and Ecological Image Analysis](https://arxiv.org/abs/2606.27667)

**<font color=#1a73e8>作者：</font>** Brinnae Bent, Holly R. Houliston, Jiayi Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is transforming biodiversity monitoring by enabling automated analysis of ecological imagery collected from camera traps, drones, satellites, underwater platforms, and other sensing systems. These tools can expand the scale and speed of conservation assessments, yet many computer vision models remain difficult to inspect, making it challenging to determine whether predictions are based on ecologically meaningful signals or on spurious correlations, sampling biases, and other artifacts that may undermine conservation decisions. We argue that explainable artificial intelligence (XAI) should become a standard component of ecological model validation because conservation practitioners increasingly depend on understanding not only whether a model is accurate, but why it is accurate. We provide practical guidance for applying XAI to three common ecological computer vision tasks: image classification, object detection, and image segmentation. To illustrate how XAI can support ecological model auditing, refinement, and deployment, we present two case studies using aerial imagery: harbor seal detection and cetacean anatomical segmentation. These examples demonstrate how explanation methods can identify biologically meaningful cues, reveal false positives driven by background and shape confounds, uncover edge and occlusion effects, and guide data collection, augmentation, and retraining strategies. More broadly, they show how explainability can help assess whether model reasoning aligns with ecological understanding. We conclude by identifying key challenges and opportunities. By making model behavior more transparent and scientifically interrogable, XAI can help ensure that AI-supported ecological evidence is more reliable, understandable, and actionable for biodiversity conservation.

---


### 44. [When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search](https://arxiv.org/abs/2606.27669)

**<font color=#1a73e8>作者：</font>** Yiling Tao, Shihan Deng, Meiling Tao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search agents powered by large language models (LLMs) are increasingly used to solve complex information-seeking tasks, requiring multi-step retrieval and reasoning to fulfill user goals. However, existing benchmarks often assume that user queries are complete and explicit, overlooking the fact that real-world search requests are frequently vague, underspecified, or even factually incorrect. In deep search scenarios, such ambiguity can propagate along multi-step reasoning chains and lead agents toward incorrect search trajectories. To address this gap, we introduce DiscoBench, a benchmark for clarification-aware deep search, designed to evaluate whether search agents can proactively identify ambiguity, ask effective clarification questions, and recover correct reasoning paths through user interaction. DiscoBench contains 211 samples and 463 ambiguity instances across 11 real-world domains, covering four ambiguity types. We further design a user simulator for multi-turn interaction and evaluate model performance from four perspectives: task utility, ambiguity detection, interaction strategy, and cost efficiency. Experiments on representative LLMs show that ambiguity detection and effective clarification are distinct capabilities, and that repeatedly searching instead of asking for clarification often performs worse than direct guessing, highlighting a critical gap between retrieval ability and interactive problem-solving in current search agents.

---


### 45. [Multi-Modal Conditioned High-Resolution Transformer for Urban Electromagnetic Field Map Prediction Download PDF](https://arxiv.org/abs/2606.27671)

**<font color=#1a73e8>作者：</font>** Do-Eon Kim, Dongryul Park, Seungyoung Ahn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting electromagnetic field (EMF) strength in urban environments is essential for cellular network planning but computationally expensive with physics-based simulators. We propose a multi-conditioned dense prediction framework that generates 500 500 EMF maps from building layout images and antenna configurations. Our architecture uses a High-Resolution Transformer (HRFormer) backbone with two complementary conditioning mechanisms: Feature-wise Linear Modulation (FiLM) injects scalar antenna parameters into all backbone stages, while cross-attention fuses 1-D radiation pattern tokens with spatial features at the deepest stage. We further introduce transmitter-relative spatial channels encoding distance, proximity, and bearing from the antenna, enabling coordinate-consistent test-time augmentation (TTA) that reduces test MAE by 6.3%. To address the prediction difficulty imbalance across EMF maps, we design a composite loss combining masked L1, multi-scale structural similarity (MS-SSIM), and a focal L1 term that upweights high-signal pixels, outperforming individual loss components in all metrics. Our best model achieves a test MAE of 0.0461, a 25.2% improvement over a plain UNet baseline and 31.8% over an HRFormer-only this http URL-

---


### 46. [Two-Stage Cross-Domain Cervical Abnormality Screening with Cytopathological Image Synthesis and Knowledge Distillation](https://arxiv.org/abs/2606.27678)

**<font color=#1a73e8>作者：</font>** Jincheng Li, Yuzhi He, Yihui Zhan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-domain diagnosis remains a major challenge in cervical cell pathology due to pronounced domain shifts across institutions and the subtle visual differences among disease stages, which jointly impair model generalization. To address these issues, this paper proposes a two-stage framework for cross-domain cervical cell detection. In the first stage, we propose the Spatially-Continuous Unpaired Neural Schrödinger Bridge (SC-UNSB), which constructs a synthetic intermediate domain to mitigate cross-domain distribution shifts by modeling image translation as an entropy-regularized optimal transport process. In the second stage, we propose a dual-level feature alignment strategy within a knowledge distillation, which progressively aligns shallow structural features and deep semantic representations to facilitate the transfer of domain-invariant knowledge from the source to the target model. Experimental results demonstrate that the proposed method effectively mitigates domain shift and category ambiguity, improving the cross-domain detection performance.

---


### 47. [Deployment-Side Adaptiveness in Multi-Horizon Volatility Forecasting](https://arxiv.org/abs/2606.27688)

**<font color=#1a73e8>作者：</font>** Riku Green, Zahraa S. Abdallah, Telmo M Silva Filho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In financial forecasting, predictive performance depends not only on which model is trained, but also on how the trained model is deployed. We study this issue in multi-horizon volatility forecasting. Our starting point is that a trained multi-output (MIMO) forecaster does not define a single deployable predictor: by changing the inference-time rollout rule, the same trained model induces a family of forecasts with different accuracy and cost profiles. Across 20 stock-volatility series, three forecast horizons, and architectures ranging from linear models to PatchTST, we find that non-default rollout rules often improve over standard MIMO deployment. However, the best fixed rule varies substantially across architectures and horizons, making any single static replacement unreliable. We therefore evaluate validation-based deployment policies over the induced rule family. Under the primary MSE objective, validation-selected singletons provide a low-cost improvement over default MIMO, while small rule subsets recover much of the benefit of larger ensembles at substantially lower inference cost. We also find that policy rankings are metric-sensitive: MSE-selected policies do not transfer uniformly to QLIKE, a finance-standard volatility loss. These results show that inference-time deployment is a meaningful source of adaptiveness in financial forecasting, and that trained volatility forecasters should be evaluated not only by their architecture, but also by their deployment policy.

---


### 48. [Halt Fast! Early Stopping for Certified Robustness](https://arxiv.org/abs/2606.27694)

**<font color=#1a73e8>作者：</font>** Andrew C. Cullen, Paul Montague, Benjamin I.P. Rubinstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized Smoothing (RS) provides rigorous robustness guarantees for neural networks without architectural constraints, yet its adoption is limited by extreme computational costs. Standard RS requires tens of thousands of model evaluations per input and forces practitioners to commit to fixed sample sizes a priori. In this work, we present a novel meta-learning framework for anytime-valid certified robustness that adaptively deploys computational resources. By using a lightweight meta-learner to predict image-specific priors for a sequential E-process, we achieve a 20-fold reduction in sample complexity compared to traditional methods while maintaining rigorous statistical guarantees. Beyond raw efficiency, we demonstrate how anytime-validity enables adaptively allocating compute based upon application-specific risk thresholds, a form of resource triage impossible under classic certification frameworks. That this is achievable while also providing similar certification performance demonstrates that our approach provides a pathway for real-time, safety-critical certification deployments.

---


### 49. [Class-frequency Guided Noise Schedule for Diffusion Models](https://arxiv.org/abs/2606.27696)

**<font color=#1a73e8>作者：</font>** Jiequan Cui, Beier Zhu, Qingshan Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we are the first to examine the correlations between class frequency and the multi-scale noise schedule within diffusion models. For score-based generative models, low-density regions often lead to inaccurately estimated scores, thereby compromising the generation quality. Although the multi-scale noise schedule can alleviate this issue during the diffusion process, low-frequency classes still face the challenge of large low-density regions, resulting in more inaccurate estimated scores than high-frequency classes. Furthermore, high-frequency classes tend to dominate the score space, causing a convergence of most data points towards generating samples from these classes. Consequently, samples generated within low-frequency classes exhibit suboptimal quality and limited diversity. To address this challenge, we propose the \textit{Class-frequency Guided (CFRG)} noise schedule, leveraging the insight that low-frequency classes should be endowed with larger-scale noises. To illustrate the effectiveness of our method, we conduct experiments on various tasks, including image generation, image classification, and text-to-image generation, using imbalanced datasets, \textit{i.e.}, CIFAR-100-LT, and ImageNet-LT. By employing the CFRG noise schedule, we achieve substantial improvements over baselines, manifesting the crucial role of frequency statistics in noise schedule design.

---


### 50. [What Was That Again? Certified Robustness for Automatic Speech Recognition](https://arxiv.org/abs/2606.27698)

**<font color=#1a73e8>作者：</font>** Andrew C. Cullen, Neil Marchant, Jiani Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition systems are notoriously both sensitive to adversarial and benign perturbations. While this has been repeatedly demonstrated using reference datasets, detecting such behaviors in deployed systems is incredibly challenging, due to the absence of oracle knowledge of the true transcription. We demonstrate that employing a certification-inspired mechanism can significantly decrease WER, increase recall, and decrease the Spearman correlation between confidence and WER. We achieve this through a dual-gate diagnostic pipeline: a Two-Sided Atomic Audit that accumulates statistical wealth to certify both token existence and adversarial exclusion, and a Rank-Based Tournament that selects the winning sequence. Our evaluations across four diverse architectures demonstrate up to a 55% relative reduction in Word Error Rate, while also providing granular word- and sentence-level certifications to enhance acoustic security.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-160](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
