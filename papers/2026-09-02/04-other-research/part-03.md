# 📦 其他研究 | 2026年09月02日

> 本类共 **485** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

---

### 101. [AdapToPASS: Ambiguity-aware Adaptive Spherical Transformer for Panoramic Semantic Segmentation](https://arxiv.org/abs/2608.29081)

**<font color=#1a73e8>作者：</font>** Soumyaratna Debnath, Weiming Zhang, Shriram Damodaran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spherical Transformers have emerged as a promising framework for panoramic semantic segmentation (PASS) by operating directly on spherical geometry and alleviating projection-induced distortions. However, existing architectures often assume canonical spherical structure and stable viewpoints, which are frequently violated in real-world imagery due to unconstrained camera motion, introducing contextual and geometric ambiguity. Consequently, they lack adaptive mechanisms to handle such ambiguity, limiting robustness to unseen spherical transformations. In contrast, biological perception is inherently ambiguity-aware, adapting to fluctuations in cue reliability caused by geometric and contextual variations to maintain stable interpretation under complex transformations. Motivated by this, we first systematically analyze existing PASS architectures under various unseen spherical transformations. We then introduce AdapToPASS, a novel bio-inspired Spherical Transformer that adaptively models contextual and geometric ambiguities for robust PASS. At its core, Adaptive Spherical Attention (AdaSpA) blocks dynamically modulate attention according to local contextual ambiguity, mimicking adaptive, context-driven biological perception. To address geometric ambiguity, AdapToPASS employs Bifocal Spherical Representation to balance field of view and spatial resolution, together with boundary supervision inspired by the boundary-sensitive nature of biological vision. Across indoor and outdoor semantic segmentation, AdapToPASS consistently outperforms prior state-of-the-art methods. Under unseen spherical transformations, it surpasses the next-best method by +13.38% relative mIoU on Stanford2D3D and +18.77% on WildPASS. We further introduce AdapToPASS-Swift, a lightweight variant with fewer than 2M parameters, which surpasses compact baselines while retaining robustness to spherical transformations.

---


### 102. [UiAs: User-Independent 3D Facial Anti-Spoofing via Multi-modal Wireless Signals](https://arxiv.org/abs/2608.29084)

**<font color=#1a73e8>作者：</font>** Zhiwei chen, Lebin Lyu, Yimo Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Face authentication is widely deployed in security-sensitive applications, while increasingly realistic 3D spoofing attacks pose growing threats. High-fidelity 3D masks can reproduce facial appearance and geometry but cannot replicate the intrinsic physical responses of living tissue, which can be actively probed by wireless signals. However, the resulting liveness cues captured by wireless signals are entangled with user-dependent facial geometry, limiting cross-user generalization. We present UiAs, a multimodal user-independent 3D facial anti-spoofing system using electromagnetic (mmWave) and mechanical (acoustic) waves. The two modalities share similar user-dependent geometric variations, allowing UiAs to suppress them through cross-modal subtraction while preserving modality-specific liveness cues. Their complementary physical responses further improve live/spoof discrimination. In practical deployments, multiple materials (e.g., skin, hair, eyeglasses, or face coverings) may also bias liveness representations, while spoofing materials are diverse and open-ended. UiAs addresses both through skin-anchored contrastive learning. We evaluate UiAs with real 3D spoofing attacks, which achieves 93.25\% accuracy for unseen users without user-specific physical-signal enrollment.

---


### 103. [Titans-QFWP: A Regime-Aware Hybrid Quantum Fast Weight Programmer for Portfolio Optimization](https://arxiv.org/abs/2608.29093)

**<font color=#1a73e8>作者：</font>** Ming-Kai Hung, Jun-Hao Chen, Yun-Cheng Tsai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Titans-QFWP, a hybrid reinforcement learning architecture integrating a Quantum Fast Weight Programmer with Titans-style memory (Persistence, Surprise, and Forgetting) for adaptive portfolio optimization. To address high-dimensional market features, we introduce an enhanced A3C^2 framework with Hungarian-aligned K-means clustering and scaled log-return rewards. Evaluated on 468 S&P 500 stocks under an Equal-Parameter-Count (EPC) benchmark with approximately 3,000 trainable parameters, Titans-QFWP achieves strong performance (median ARR 0.4260, Calmar 8.5504, IR 0.8427). Ablation results reveal that quantum gating fundamentally reshapes memory component roles, with Persistence supporting drawdown control, Surprise contributing to return generation, and Forgetting providing additional stabilization. By stabilizing these quantum representations, the model enables defensive allocation during market drawdowns while preserving upside potential.

---


### 104. [SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and Guard Models](https://arxiv.org/abs/2608.29098)

**<font color=#1a73e8>作者：</font>** Zongrui Wang, Xiangyang Zhu, Sicheng Wang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal safety moderation requires distinguishing risks arising from visual content, user intent, and assistant behavior. Existing safeguards, however, are typically trained for a single judgment target and reduce safety assessment to a binary decision. Consequently, risk becomes difficult to compare across a multimodal interaction, and ambiguous cases are obscured. We introduce SafeAtlas-VL, a dataset of 1.5M training instances that places image-, request-, and response-level judgments on a five-level ordered scale. We curate a broad collection of safety-relevant data from both real-world and synthetic sources and apply a disagreement-aware annotation procedure. The resulting dataset spans 15 harm categories and 55 fine-grained subcategories, covering a broad range of multimodal safety scenarios. We also construct SafeAtlas-Bench, a held-out set of 5,000 instances for evaluating five-level predictions and continuous risk scores. Upon this dataset, we train the SafeAtlas Guard series of models via target-conditioned tuning for multimodal safety detection. Our models not only perform five-way classification of safety levels but also map safety to continuous scores through a soft cumulative ordinal head. Experimental results demonstrate that guard models trained on our dataset exhibit strong generalization: even without using the training sets of other benchmarks, they achieve competitive performance on the corresponding test sets. Notably, our 8B model attains the overall best performance, outperforming the previous SOTA by approximately 4% in F1 score. Code, data, and models are released to support further research. Warning: this paper contains example data that may be offensive, harmful, graphic, or disturbing.

---


### 105. [Temperature-Adaptive Transformed Teacher Matching](https://arxiv.org/abs/2608.29099)

**<font color=#1a73e8>作者：</font>** Hiroaki Aizawa, Yoshikazu Hayashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temperature scaling is a core component of knowledge distillation, yet its role and effect are still not fully understood. Transformed Teacher Matching (TTM) clarifies the role of temperature scaling by applying it only to the teacher distribution and interpreting the resulting objective as standard distillation with an implicit Rényi entropy regularization on the student. However, TTM still relies on a fixed temperature and does not specify how the teacher-side temperature should be adapted for individual samples. In this paper, we introduce a sample-wise inverse-temperature update for TTM by locally minimizing the Kullback-Leibler divergence between the temperature-scaled teacher distribution and the student's prediction. We derive closed-form first and second derivatives with respect to the inverse temperature, and show that they can be expressed using variance and covariance statistics of centered teacher and student logits under the transformed teacher weighting. This yields an efficient curvature-aware update that requires one softmax evaluation and a constant number of class-wise weighted sums. Experiments on standard image classification distillation benchmarks show that our temperature adaptation generally improves TTM and WTTM, while remaining competitive with or outperforming prior temperature-adaptive distillation baselines.

---


### 106. [Clustering as Approximation by Constrained Projectors: Theory and Guarantees](https://arxiv.org/abs/2608.29102)

**<font color=#1a73e8>作者：</font>** Angshul Majumdar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper develops a unified theoretical framework showing that a broad family of clustering methods, including k-means, fuzzy c-means, kernel k-means, kernel FCM, and spectral clustering, can all be expressed as structured low-rank projectors acting on a signal-derived matrix. By formulating each method as an instance of min over B in C of ||M - M P_B||_F^2, with different constraint sets C, we establish a common optimization template that clarifies the algebraic links among hard, fuzzy, kernel-induced, and orthonormal projections. Within this framework, we derive non-trivial theoretical results, including geodesic convexity properties on the projection manifold, perturbation bounds quantifying stability to matrix noise, and exact recovery guarantees under ideal block-model conditions. The analysis further explains when different clustering families collapse to the same optimal subspace and how deviations arise under small inter-cluster leakage. Overall, the work provides a coherent, theory-first foundation for understanding clustering through structured projectors.

---


### 107. [Elastic Triangle Splatting](https://arxiv.org/abs/2608.29106)

**<font color=#1a73e8>作者：</font>** Tian Shi, Shenhan Qian, Daniel Cremers  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While neural rendering methods such as 3D Gaussian Splatting achieve remarkable visual fidelity, traditional polygonal meshes remain the backbone of established graphics pipelines. Triangle splatting bridges this gap by optimizing triangle primitives as differentiable splats, producing representations that are closer to mesh-based workflows. Central to these methods is the kernel function that softens triangle boundaries to propagate gradients to vertex positions. Existing triangle splatting methods make inconsistent choices of kernel functions, and analysis of these kernels' optimization behavior has been limited to unstructured triangle soups for novel-view synthesis. In this work, we consider triangle splatting as a generic tool for photometric optimization, comparing kernel properties through two complementary tasks: mesh optimization for shape reconstruction and triangle soup optimization for novel-view synthesis. Along with the analysis, we introduce an elastic kernel function that features bilateral gradient support across the boundary and an adaptive boundary value, which are shown to be essential for robust optimization. Under isolated comparison, our elastic kernel outperforms existing kernels on shape reconstruction and in the majority of novel-view synthesis benchmarks, demonstrating the importance of kernel design in the effectiveness and versatility of triangle splatting.

---


### 108. [PathGuide: Dynamic Classifier-Free Guidance via On-Policy Transport Alignment](https://arxiv.org/abs/2608.29107)

**<font color=#1a73e8>作者：</font>** Avishag Nevo, Tamir Hazan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While modern generative models excel at modeling complex data, precise inference-time control in conditional generation remains a critical challenge. Classifier-free guidance (CFG) is a primary mechanism for such control, yet it is typically treated as a static tuning parameter. In flow-based models, however, the guidance scale fundamentally dictates the velocity field and the resulting probability path, making guidance selection a dynamic path-optimization problem. We introduce PathGuide, a framework that reformulates scalar CFG selection as an on-policy transport problem. Leveraging the weak form of the continuity equation, we derive a selection criterion with a direct path-correctness interpretation: we prove that if the guided field is weakly equivalent to the exact conditional field along the generated rollout, the sampler's path coincides with the target conditional law. For scalar CFG, this criterion yields a strictly quadratic local objective with an efficient, closed-form selector for each solver interval. PathGuide enables optimal guidance scales to be computed and used online during generation or fitted offline as a reusable piecewise-constant schedule. We validate our method on low-resolution image manifolds and controlled settings across various continuous-time flow constructions, demonstrating that this transport-based selector improves path alignment and sample fidelity over both fixed and state-of-the-art adaptive guidance baselines.

---


### 109. [Explainable Machine Learning for Broadband Adoption Disparities: Tract-Level Prediction and SHAP-Based Factor Profiling](https://arxiv.org/abs/2608.29110)

**<font color=#1a73e8>作者：</font>** Xiao Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The United States has allocated approximately $65 billion through the Infrastructure Investment and Jobs Act for broadband expansion, yet evidence-based methods for targeting these investments remain underdeveloped. This paper presents an explainable machine learning framework for profiling broadband adoption disparities at census-tract granularity across 83,359 tracts nationwide. Using 65 socioeconomic, demographic, and infrastructure features derived from the American Community Survey 2022, we train a LightGBM model under spatial five-fold cross-validation, achieving R^2 = 0.533 and Spearman rho = 0.763; state-held-out cross-validation (51 folds) confirms generalization (R^2 = 0.525). TreeSHAP analysis identifies income and education as the dominant factor group (with the engineered interaction term absorbing attribution from its constituent features), and SHAP-based clustering reveals three exploratory factor profiles: Well-Connected Moderate (~49K tracts), Affordability-Limited Severe (~21K tracts), and Rural-Elderly (~13K tracts). As a screening tool, ML-based tract selection captures 38.0% of the total adoption gap within the top 10% of tracts versus 35.2% for income-only heuristics (+2.8 pp, p < 0.002, county-block bootstrap); in regret-reduction terms, the model closes 19% of the remaining gap between income-only and oracle selection. The primary contribution is the per-tract factor decomposition: SHAP identifies which feature groups (income/education, rurality, age) are most strongly associated with each tract's predicted gap, and informs differentiated investigation. A temporal stability check, training on ACS 2017 and predicting ACS 2022 with zero survey-year overlap, confirms ranking stability (rho = 0.784, noting hyperparameters tuned on 2022 data).

---


### 110. [NFAD: Nuisance-Filtered Anomaly Detection Under Distribution Shift](https://arxiv.org/abs/2608.29112)

**<font color=#1a73e8>作者：</font>** Dat Cao, Son Nghiem, Phan Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in anomaly detection (AD) for industrial inspection have pushed performance on standard benchmarks toward saturation. However, strong benchmark performance does not necessarily translate to real-world deployment, as these benchmarks are primarily collected under controlled acquisition conditions. Changes in illumination, background, viewpoint, and other environmental factors can shift normal samples away from the learned normal distribution and cause false anomaly responses. We address AD under such distribution shifts by explicitly modeling nuisance variation from changing imaging conditions in feature space. Without anomaly labels or target-domain data, our Nuisance-Filtered Anomaly Detection (NFAD) framework estimates a nuisance subspace from matched feature displacements induced by content-preserving perturbations and suppresses its contribution to anomaly residuals at inference. The same subspace supports two complementary branches: full projection for image-level detection and selective suppression for pixel-level localization, preserving evidence of localized defects. On AeBAD-S, a benchmark specifically designed for AD under acquisition shifts, NFAD achieves 91.0\% image-level AUROC, establishing a new state of the art. Notably, this robustness does not come at the expense of conventional AD performance: NFAD remains competitive on standard benchmarks that do not explicitly evaluate distribution shift, including VisA, Real-IAD, and MVTec AD. These results show that explicitly suppressing such nuisance variation improves AD under distribution shift while preserving strong performance in standard settings.

---


### 111. [GramLoop: Training-Free Gram-Gated Replay for Robust Dense Prediction](https://arxiv.org/abs/2608.29113)

**<font color=#1a73e8>作者：</font>** Yang Chen, Canyu Shen, Xinzhe Rao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We aim to improve frozen DINOv3 dense-prediction models under distribution shift by adding inference computation inside the visual backbone, without changing model weights, task adapters, or prediction heads. The challenge is that repeated transformer-block computation must refine dense features without disrupting the pairwise patch relations that DINOv3 uses to preserve spatial structure. We introduce GramLoop, a training-free framework that replays a short transformer window and controls each replay through final-layer cosine-Gram consistency. Each proposal is propagated through the frozen suffix, measured against the standard DINOv3 trajectory, and accepted through a patchwise gate at the replay-window endpoint. Across object detection and semantic segmentation under corruptions, perturbations, and natural shifts, GramLoop improves all five shifted benchmarks over the paired DINOv3 baseline. On COCO-O, it improves mAP by +0.252 and Effective Robustness by +0.250, while preserving clean ADE20K performance. Code will be released.

---


### 112. [Acoustically Grounded Cost Learning for Open-Vocabulary Audio-Visual Semantic Segmentation](https://arxiv.org/abs/2608.29121)

**<font color=#1a73e8>作者：</font>** Tianrui Hui, Shaofei Huang, Qisong Han 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-Vocabulary Audio-Visual Semantic Segmentation (OV-AVSS) aims to perform pixel-level segmentation of sound-emitting objects from an open set of categories. The previous method relies on a class-agnostic foreground definition, which groups semantically diverse objects into a heterogeneous positive set, causing the model to learn unstable sounding patterns and produce unreliable proposals. To address this, we reformulate the objective to be category-specific and propose a novel Acoustically Grounded Cost Learning (AGCL) framework to transform the static, audio-agnostic visual-text priors into dynamic, audio-grounded cost representations. For intra-category soundingness discovery, we devise Audio-Modulated Cost Generation (AMCG) and Audio-Guided Temporal Aggregation (AGTA) modules to enable both frame-level sounding region highlighting and video-level temporal refinement with a low-intrusive audio injection mechanism. For inter-category distractor discrimination, we introduce a Synergistic Distractor Mining (SDM) strategy, which selectively penalizes acoustically and semantically confusing negative categories to learn more discriminative decision boundaries. Extensive experiments on the AVSBench-OV dataset demonstrate that our method significantly outperforms previous state-of-the-art approaches, particularly on unseen categories. Code is available at this https URL.

---


### 113. [Dancing Stick Figures: An Introductory Dataset for Training Video Generation Models](https://arxiv.org/abs/2608.29123)

**<font color=#1a73e8>作者：</font>** Jin Hyuk Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training a video-generation model from scratch is hard for reasons that precede model design. The feedback loop is long: a failure that appears only after a training run can make each attempted fix another run. The data are hard to reach: the corpora and recipes behind strong models are large, heterogeneous, and often unreleased. And scoring is blunt: open-ended generation has no single correct output, and an aggregate score does not by itself establish whether a sample succeeds or which property failed. Dancing Stick Figures is a synthetic video dataset built against these three obstacles. For iteration speed, its 64x64, 64-frame reference task is sized for practical repeated training on a single workstation GPU. For accessibility, the release is a 0.79-GB training tier of 4,020 video clips--1,340 six-second source motions, each rendered from three cameras by a deterministic dataset-generation harness--with checkpoints and a Colab workflow that reruns the reference training pipeline at reduced budget on a 16 GB Tesla T4. For scoring, every frame retains its generating state (ARDY cskel27 joint positions, camera, body parameters, and source motion) and per-pixel depth, surface normals, and part labels. These annotations support dataset-specific metrics for visible topology and part-wise motion; corruptions expose their sensitivities and blind spots.

---


### 114. [Efficient Language-to-Vision Feature Injection for Referring Single-Object Tracking](https://arxiv.org/abs/2608.29126)

**<font color=#1a73e8>作者：</font>** Han Wang, Yuxuan Liu, Yuhan Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring single-object tracking enables language-grounded target initialization and subsequent tracking by jointly leveraging semantic cues and visual templates. The core difficulty is to use language differently across stages: it is indispensable for grounding but can induce semantic drift during tracking when overemphasized. Meanwhile, current methods often require costly vision-language alignment training. We present LVTrack, a pure transformer framework that introduces a mode-conditioned Gated Feature Injector to adaptively regulate textual guidance and alleviate semantic drift. Together with targeted adaptations, it directly harnesses a frozen vision-language pretrained model, greatly reducing training cost and preserving strong language understanding. To further improve temporal localization, LVTrack integrates hybrid relative-absolute positional encodings with a lightweight memory mechanism and optimizes autoregressive box prediction using a Gaussian-smoothed KL loss. Extensive experiments on standard benchmarks demonstrate that LVTrack achieves strong performance.

---


### 115. [Mechanizing Typed Regulatory Actions for Security Tokens: Semantics, Falsification, and Bounded EVM Evidence](https://arxiv.org/abs/2608.29134)

**<font color=#1a73e8>作者：</font>** Jinwook Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security-token standards expose privileged transfer, freezing, recovery, and compliance mechanisms, but a mechanism does not by itself identify the legal effect being executed or the evidence and reversal obligations attached to it. We formalize in Isabelle/HOL a reference execution semantics for the six regulatory-action meanings proposed in ERC-8319: FREEZE, SEIZE, CONFISCATE, LIQUIDATE, RESTRICT, and RECOVER. The model distinguishes applied, rejected, and operational-failure outcomes and mechanizes reversal, replay, epoch, frame, case-local terminality, and receipt properties; the build has no unproved placeholders or added axioms. It proves an external-truth boundary: two concrete worlds that disagree about title, settlement, and entitlement induce the same kernel observation, so those external facts cannot be established from bound inputs. Constructive witnesses and direct mutations show reachability and falsification for the declared fault set. For one ERC-TRUST Solidity/EVM candidate, we report separately scoped Foundry, Certora, Kontrol/KEVM, mutation, deterministic-build, and runtime-identity evidence. The current publication profile qualifies all seven evidence packages and all 49 Core and 24 mandatory Supporting obligations with no partial credit; six optional obligations remain unclaimed. A mechanized abstraction relation is proved unique and functional under pinned-runtime premises, and package and row corollaries yield conditional, profile-scoped refinement theorems from hash-bound certificates. These results do not constitute a complete Isabelle-to-Solidity-to-EVM refinement theorem, compiler correctness, an audit, production readiness, or deployment verification. The contribution is a machine-checked domain semantics and a falsifiable map of what is proved, what is bounded evidence, what is assumed, and what remains open for a regulated-token execution standard.

---


### 116. [More Perspectives, Stronger Signals: Multi-Perspective Enhancement and Progressive Fusion for Multimodal Entity Representation Learning](https://arxiv.org/abs/2608.29139)

**<font color=#1a73e8>作者：</font>** Chenyi Xiong, Yan Zhang, Jing Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning effective multimodal entity representations is fundamental for reasoning tasks such as multimodal knowledge graph completion (MMKGC). However, existing methods often suffer from semantic over-smoothing within modalities and ineffective noise filtration across modalities, particularly under sparse or ambiguous conditions. To overcome these limitations, we propose PrismF, a unified framework that synergizes multi-perspective enhancement with progressive fusion to extract stronger signals from diverse inputs. PrismF enhances fine-grained intra-modal semantics through a multi-perspective mechanism that decomposes each modality into complementary views and constrains them with a decoupling loss to reduce representation collapse. Furthermore, it improves cross-modal integration through a progressive fusion strategy that dynamically calibrates inter-modal interactions, enabling the model to emphasize informative signals while suppressing noisy or unreliable ones. Extensive experiments on three public benchmarks show that PrismF achieves the strongest overall performance, including relative improvements of 4.04% in MRR and 11.17% in Hits@1 on KVC16K. Our code can be found at this https URL.

---


### 117. [STARLINC: Satellite Trail Artifact Removal using Inter-Frame Correlation](https://arxiv.org/abs/2608.29145)

**<font color=#1a73e8>作者：</font>** Shingeon Kim, Hyeyoon Lee, Dain Kwon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of low Earth orbit satellites such as Starlink is increasingly contaminating astronomical surveys. In practice, contaminated images are often identified through inspection. However, modern surveys generate terabytes of data each night, making manual screening infeasible and necessitating reliable automated methods for satellite trail removal. Unfortunately, existing general-domain line detection methods fail to generalize to astronomical images due to domain mismatch, which are mostly grayscale with sparse bright stars and have a low signal-to-noise ratio. Moreover, training new models from scratch is impractical due to the lack of large-scale annotated astronomical datasets. To address these challenges, we introduce STARLINC, the first ML-based framework for satellite trail removal without requiring tedious pixel-level annotation of astronomical images. STARLINC combines synthetic satellite trail generation for training, inter-frame differential maps from temporally adjacent exposures to highlight transient trails, and heatmaps to provide additional localization cues for pixel-level segmentation. Extensive experiments on real-world data demonstrate substantial improvements over baselines, establishing STARLINC as a scalable solution for next-generation astronomical surveys. Code is available at this https URL.

---


### 118. [SGRNet: Spatially Guided Radiology Network for Structured Radiological Reporting of Head and Neck Cancer](https://arxiv.org/abs/2608.29153)

**<font color=#1a73e8>作者：</font>** Ayush Gupta, Vinkle Srivastav, Prateek Upadhya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated radiological report generation can alleviate clinical workloads and eliminate observer variability. However, standard free-text generation models pose hallucination risks in dense regions and fail under data scarcity. We address these challenges in Head and Neck Cancer (HNC) from contrast-enhanced CT (CECT) imaging. To enforce factual safety, we reformulate report generation as an anatomically grounded, multi-label, structured reporting task, predicting localized tumor involvement across a hierarchical clinical schema. To bridge the visual gap from missing metabolic imaging (e.g., PET), we introduce SGRNet (Spatially Guided Radiology Network), incorporating two low-cost spatial priors: automated organ segmentations and weakly supervised tumor localization maps modeled via 3D Gaussian heatmaps. These priors are dynamically integrated via spatial feature modulation to guide the network toward subtle tumor-induced structural alterations. Evaluated on a multi-centric dataset of 184 paired HNC CECT volumes and reports, on five clinically salient, densely packed anatomical subsites, SGRNet achieves a mean Average Precision (mAP) of 0.60, an 8.8 percentage-point absolute improvement over strong volume-only 3D baselines.

---


### 119. [Training-Free Hidden-State Refinement for Flow-Matching Image Generators](https://arxiv.org/abs/2608.29160)

**<font color=#1a73e8>作者：</font>** Yuanyi Yan, Xinzhe Rao, Canyu Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We aim to improve frozen flow-matching image generators by adding inference computation inside the denoiser, without changing model weights or the outer sampler. Existing generators usually spend extra test-time computation by increasing the number of sampling steps, which repeatedly evaluates the entire denoiser and couples quality gains to sampler cost. A key challenge is how to use extra computation inside a frozen transformer denoiser: the method must decide which tokens, layers, and sampling times receive repeated updates while preserving the original generation pipeline. We introduce a training-free looping framework that repeatedly applies selected transformer layers inside each denoising call. Dense and Sparse Token Loop vary the token scope; Sampling-Progress Gating and the loop layer range specify when and where looping is active; loop count and strength control the repeated updates; and Loop Guidance combines ordinary and looped vector-field predictions. Across two Scale-RAE model scales, loop variants improve primary and auxiliary quality metrics with competitive quality--efficiency trade-offs. Loop Guidance further improves both primary metrics across all three tested models; on Scale-RAE DiT2.4B, it raises GenEval from 0.4471 to 0.5691 and DPG-Bench from 0.7656 to 0.8053. Code will be released.

---


### 120. [Subtraction-Based Tumor Segmentation and Lesion-Centered pCR Prediction for the MAMA-MIA Challenge](https://arxiv.org/abs/2608.29162)

**<font color=#1a73e8>作者：</font>** Kai Geissler, Raphael Schäfer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe the submission of team FME to the MAMA-MIA Challenge, which evaluated primary tumor segmentation and prediction of pathological complete response (pCR) from pretreatment dynamic contrast-enhanced breast MRI on an external multi-country cohort. For segmentation, we trained a five-fold residual-encoder nnU-Net ensemble using only the first post-contrast minus pre-contrast image, combined with mirroring test-time augmentation and largest-connected-component filtering. For pCR prediction, we ensembled 25 pretrained 3D video classifiers trained on lesion-centred crops from the pre-contrast and first two post-contrast volumes. FME ranked second in both tasks. The segmentation method achieved a combined performance-fairness score of 0.882, with Dice 0.713 and normalized Hausdorff distance 0.099. The pCR method achieved a combined score of 0.664, balanced accuracy of 0.541, and equalized-odds disparity of 0.212. The results indicate that subtraction-based input and ensembling support robust tumor segmentation under cross-site domain shift, whereas pCR prediction from baseline DCE-MRI alone remains limited.
For the submission repository, see this https URL

---


### 121. [Mapping-Based Image Diffusion](https://arxiv.org/abs/2608.29164)

**<font color=#1a73e8>作者：</font>** Freddie Åström, Michael Felsberg, George Baravdish  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce a novel tensor-based functional for targeted image enhancement and denoising. Via explicit regularization, our formulation incorporates application dependent and contextual information using first principles. Few works in literature treat variational models that describe both application dependent information and contextual knowledge of the denoising problem. We prove the existence of a minimizer and present results on tensor symmetry constraints, convexity, and geometric interpretation of the proposed functional. We show that our framework excels in applications where nonlinear functions are present such as in gamma correction and targeted value range filtering. We also study general denoising performance where we show comparable results to dedicated PDE-based state of the art methods.

---


### 122. [Feature-Spectral Fragility in Segmentation: Dataset Dependence, Architecture-Specific Localization, and Spectral Correlates](https://arxiv.org/abs/2608.29167)

**<font color=#1a73e8>作者：</font>** Subhash Kashyap  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robustness of segmentation models is commonly assessed through input-domain perturbations, while dependence on frequency content within learned feature representations remains less understood. We probe this dependence using targeted post-training low-pass interventions on internal representations of three segmentation architectures, ResNet50-UNet (CNN), VM-UNet (SSM), and Swin-UNETR (Transformer), across CVC-ClinicDB and ISIC2018, with headline evaluations performed on untouched held-out test sets. At cutoff rho=0.25, feature-domain low-pass filtering causes severe degradation on CVC: Dice drops by 100%, 73.2%, and 30.9% for CNN, SSM, and Transformer, respectively, compared with 9.4%, 10.3%, and 0.6% on ISIC. The cross-dataset difference is statistically significant for every architecture. Single-stage interventions further show that sensitivity is localized at architecture-specific depths: the CNN peaks at a mid/late encoder block, whereas the SSM peaks in an early encoder stage on both datasets. Native feature-domain spectral measurements show an inverse association between high-frequency energy and fragility on CVC; the relationship is only partial on ISIC and is therefore treated as a candidate correlate rather than a proven mechanism. Finally, Fourier augmentation improves robustness to input-space low-pass filtering but leaves feature-domain degradation essentially unchanged. These results show that feature-spectral robustness is strongly dataset-dependent, architecture-specific, and distinct from input-domain spectral robustness.

---


### 123. [Toward a Cross-Lingual Romanization Ecosystem for Sinitic Languages: A Paired Mandarin-Cantonese Case Study](https://arxiv.org/abs/2608.29170)

**<font color=#1a73e8>作者：</font>** Zijie Zhang, Tan Lee, Yong Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper proposes the Sinitic Romanization Ecosystem, a cross-lingual Sinitic romanization design framework with supporting digital infrastructure and a community-driven open-source workflow. The design framework addresses the lack of systematic cross-lingual romanization alignment among Sinitic languages through four design principles: phonetic correspondence for representing similar sounds with similar romanized symbols, historical-phonological correspondence for aligning cognate romanization strings, one-phoneme-one-symbol, and basic Latin-letter use, with a balancing consideration recognizing trade-offs among these principles. For the main paired case study, we devel-op CantRomZJ1 and MandRomZJ1, Cantonese and Manda-rin romanization schemes following the design framework, respectively. We also develop schemes for several other Sinitic languages, including Meixian Hakka, Shanghai Wu, and Nanjing Jianghuai Mandarin, following the same de-sign framework. To bring the romanization schemes into practical use, we develop open-source infrastructure for structured romanization storage, conversion, parsing, dic-tionary construction, and input-method generation. Finally, we evaluate the design framework through speech-to-romanization experiments based on Meta's Massively Mul-tilingual Speech (MMS) fine-tuning. Compared with the Pinyin+Jyutping baseline, our Man-dRomZJ1+CantRomZJ1 condition reduces Cantonese WER and CER by 7.80% and 10.61%, respectively. These results suggest that cross-lingual romanization alignment can improve transfer in low-resource Sinitic speech technology.

---


### 124. [A Tensor Variational Formulation of Gradient Energy Total Variation](https://arxiv.org/abs/2608.29172)

**<font color=#1a73e8>作者：</font>** Freddie Åström, George Baravdish, Michael Felsberg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a novel variational approach to a tensor-based total variation formulation which is called gradient energy total variation, GETV. We introduce the gradient energy tensor [6] into the GETV and show that the corresponding Euler-Lagrange (E-L) equation is a tensor-based partial differential equation of total variation type. Furthermore, we give a proof which shows that GETV is a convex functional. This approach, in contrast to the commonly used structure tensor, enables a formal derivation of the corresponding E-L equation. Experimental results suggest that GETV compares favourably to other state of the art variational denoising methods such as extended anisotropic diffusion (EAD)[1] and total variation (TV) [18] for gray-scale and colour images.

---


### 125. [An Explainable Coherence Score for Detecting Temporal Inconsistencies in Political News](https://arxiv.org/abs/2608.29175)

**<font color=#1a73e8>作者：</font>** Marius Nicusor Pantea, Adrian Groza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Temporal inconsistencies, such as mandates attributed outside their real interval, events presented as past before they occurred, or inverted causal sequences, are a form of political disinformation that evades style-based fake news detectors: a well-written article with a single wrong date carries no lexical signal of falsehood. This paper introduces the Temporal Coherence Score (TCS), a continuous, intrinsically interpretable metric that quantifies the temporal coherence of a news article, computed by a four-stage pipeline: extraction of temporal facts, construction of a temporal knowledge graph, hierarchical verification against internal consistency rules and external reference sources, and score aggregation with automatically generated explanations. Verification combines eight internal checkers derived from Allen's interval algebra with a five-level external hierarchy ranging from a locally stored reference knowledge base of 1{,}256 curated political facts to live Wikidata SPARQL queries. On a benchmark of 100 political news articles with injected temporal errors, the system reaches a precision of 0.909 at the selected operating threshold, with a single residual false positive, a profile deliberately tuned for human-in-the-loop fact-checking assistance, where false alarms are costlier than missed detections. Unlike lexical baselines that output only a binary label, every flagged article is accompanied by the inconsistency type, the entities involved, and the reference source that contradicts the claim.

---


### 126. [Dynamic-Robust Photometric-Semantic Reconstruction for Open-Vocabulary 3D Scene Understanding](https://arxiv.org/abs/2608.29177)

**<font color=#1a73e8>作者：</font>** Boyu Cai, Li Yang, Yan Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The integration of novel view synthesis (NVS) and open-vocabulary segmentation (OVS) has recently yielded powerful feed-forward 3D foundation models. However, their inherent reliance on static-scene assumptions leads to severe misalignment of spatial features in unconstrained dynamic environments. To bridge this critical gap, we propose SPAR, a novel joint semantic-geometric encoding architecture that explicitly isolates transient dynamic noise prior to latent space aggregation. Furthermore, we introduce a dynamic-region-aware end-to-end training paradigm that structurally couples motion estimation with multi-view visual and semantic learning. This unified approach enables the network to inherently resolve motion conflicts and distill multi-view consistent, temporally stable scene representations from dynamic inputs. Extensive experiments on the challenging D-RE10K benchmark demonstrate that SPAR achieves state-of-the-art performance. Our end-to-end approach achieves exceptional novel view synthesis quality, yielding a PSNR of 22.15 dB and 23.33 dB given only 3 and 4 input views respectively. Despite being trained in a self-supervised manner, our model achieves an mIoU of 88.5% for motion mask prediction. Furthermore, our analysis reveals a strong inter-task synergy between photometric scene reconstruction and semantic understanding, where semantic synthesis learning consistently enhances photometric fidelity in novel view rendering. Code will be available at this https URL.

---


### 127. [Foundational feature fusion for conditional flow matching in 6D pose estimation](https://arxiv.org/abs/2608.29183)

**<font color=#1a73e8>作者：</font>** Amir Hamza, Davide Boscaini, Fabio Poiesi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conditional flow matching has enabled a step forward in object 6D pose estimation, achieving state-of-the-art performance by progressively denoising and registering object representations to observed scenes. Existing methods require training task-specific encoders supervised on object-scene overlap and rely on trivial feature fusion strategies to resolve pose ambiguities. We present FunFlow6D, a novel flow matching-based formulation that leverages features from geometric and appearance foundation models for pose estimation, eliminating the need for task-specific encoder training. We also introduce a cross attention-based fusion mechanism that dynamically combines geometric and appearance features to provide richer conditioning for the flow matching module. Experiments on four datasets from the BOP benchmark show that FunFlow6D outperforms the previous state of the art while reducing supervision requirements and memory overhead. Extensive ablations validate the contribution of each proposed component. Project website: this https URL.

---


### 128. [GhostSplat: Input-Triggered Backdoors for Multi-View-Consistent 3D Content Manipulation in Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2608.29184)

**<font color=#1a73e8>作者：</font>** Yudong Gao, Zongjian Ding, Linghan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) reconstructs a 3D scene from sparse images in one forward pass. Its shared pretrained weights also expose a supply-chain attack surface. Existing Neural Radiance Field and 3DGS backdoors modify individual scenes and activate at selected viewpoints; they do not install persistent behavior in shared generator weights. We introduce GhostSplat, an input-triggered backdoor that installs such behavior in feed-forward 3DGS. A low-amplitude pattern added to the input images causes the poisoned generator to render an attacker-chosen payload on unseen victim scenes. Anchoring the payload to a 3D point and reprojecting it into each target view makes the payload multi-view consistent. Exact projection onto the generator's representation-specific consistency set leaves a realized payload unchanged because the output already belongs to that set. The GhostSplat training framework succeeds across three architectures (MVSplat, pixelSplat, DepthSplat) and two datasets (RealEstate10K, ACID). Its strongest evaluated injection and deletion settings reach 96% and 100% ASR, respectively, with zero observed false positives while surviving JPEG, blur, and resampling. Defenses that use only that exact projection are therefore insufficient; effective mitigation requires information or intervention beyond same-set consistency projection.

---


### 129. [Multi-Scale Temporal Domain Alignment for Federated Video Domain Adaptation](https://arxiv.org/abs/2608.29186)

**<font color=#1a73e8>作者：</font>** Lee En-Yi Hannah, Haozhi Cao, Yuecong Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated Video Domain Adaptation (FVDA) enables collaborative learning across distributed and non-IID video datasets while preserving privacy, but is under-explored due to challenges in aligning temporal information. We propose Multi-scalE Temporal domAin aLignment (METAL), a novel framework that leverages temporal information at multiple resolutions to improve cross-domain video action recognition with only model parameter transfers. METAL trains per-scale transformer encoders on source-clients, then performs independent knowledge voting at each temporal scale to generate robust pseudo-labels on the target-server. A novel $L_2$ variance penalty enforces cross-scale consistency during scale-based knowledge distillation, preventing a singular dominant scale. The late fusion aggregates features across different scales, where the fusion head is trained via knowledge distillation using confidence-weighted aggregation of scale-wise predictions, enabling the model to effectively exploit complementary temporal information for final predictions. Experiments on Epic-Kitchens-55 and Daily-DA demonstrate state-of-the-art performances, with gains up to 28.47% over current FDA methods. Ablation studies prove that multi-scale distillation and scale coordination are critical for effective temporal knowledge transfer.

---


### 130. [OPUS-V2: Bridging the Gap between Sparse Points and Dense Voxels](https://arxiv.org/abs/2608.29187)

**<font color=#1a73e8>作者：</font>** Jiabao Wang, Qiang Meng, Liujiang Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The point-based occupancy prediction paradigm has achieved an attractive trade-off between accuracy and efficiency by modeling 3D space sparsely. However, its predictions inherently mismatch the dense voxel-based occupancy required by self-driving systems, necessitating hand-crafted heuristics during training and inference that limit final performance. To overcome these limitations, we propose OPUS-V2, a novel framework built upon the pioneering OPUS (occupancy prediction using a sparse set) point-based approach. OPUS-V2 incorporates a lightweight point-voxel transformation (PVT) module behind the decoder to adaptively map sparse predictions into the dense voxel space, eliminating the need for suboptimal operations and improving model accuracy. Furthermore, our architecture decouples feature and occupancy generation processes, allowing OPUS-V2 to adapt to arbitrary occupancy resolutions. OPUS-V2 achieves a state-of-the-art rayIoU of 44.0 on the Occ3D dataset. On the more challenging OpenOccupancy dataset, it attains a competitive 16.4 mIoU while running in real time at 20.6 FPS.

---


### 131. [A Broadcast Authenticated Encryption with Keyword Search in the Standard Model: Tightly Secure in Multi-User, Multi-Challenge Settings](https://arxiv.org/abs/2608.29191)

**<font color=#1a73e8>作者：</font>** Sayantan Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> However, no known work considered the functionality requirement in its most realistic setting. We propose a new security definition of BAEKS in the multi-user (with adaptive corruptions) and multi-challenge (both in terms of ciphertext and trapdoor in an interleaved manner) settings. We also study the question of the unforgeability of BAEKS. In fact, our strong hiding requirement already implies a significant amount of unforgeability. We then propose a new BAEKS construction in the bilinear pairing groups. We prove this scheme achieves adaptive tight full-hiding security under (almost) standard MDDH assumptions. Restricting our BAEKS construction for a single receiver also gives an efficient and tightly secure PAEKS construction. We further run experiments to implement and evaluate our scheme.

---


### 132. [An Eye-Tracking Dataset for Viewing Distance Categories in Real-World Scenarios](https://arxiv.org/abs/2608.29192)

**<font color=#1a73e8>作者：</font>** Dohwa Kim, Yejin Choi, Seungbok Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Estimating viewing distance from gaze behavior is essential for understanding user intent and enabling distance-aware interactive systems. However, most existing eye-tracking datasets have been collected in constrained settings, such as laboratory environments or static tasks. Consequently, they only partially capture viewing behaviors in real-world situations where viewing distance changes with natural head and body movements. We introduce GazeDepth, an eye-tracking dataset collected from 19 participants using a wearable tracker during tasks reflecting real-world scenarios. GazeDepth includes fixed-distance viewing scenarios with constant observer-target distances at near (33 cm), middle (50 cm), and far (300 cm), as well as variable-distance viewing scenarios in which participants shift gaze among targets at different depths in indoor and outdoor environments. The dataset provides synchronized gaze data, pupil size, 3D eye-vectors, and head-motion signals, along with distance labels. Statistical analyses showed that distance-related gaze features, such as vergence angle and estimated viewing distance, differed consistently across viewing-distance categories. In addition, classification models trained on GazeDepth further demonstrated that the dataset captures gaze characteristics that distinguish the three viewing-distance categories, supporting gaze-based distance inference and distance-aware interaction in realistic scenarios.

---


### 133. [RLG-TPV: Radar- and LiDAR-Guided Tri-Perspective View Fusion for Camera-Radar 3D Object Detection](https://arxiv.org/abs/2608.29194)

**<font color=#1a73e8>作者：</font>** Ahmet Mete Dokgoz, A. Enes Doruk, Hasan F. Ates  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tri-Perspective View (TPV) representations describe 3D scene structure through top, side, and front feature planes, but existing TPV lifting is primarily camera-based, leaving the depth of sampled image evidence ambiguous along projected camera rays. We propose RLG-TPV, a multimodal TPV framework for camera-radar 3D object detection in which radar and training-time LiDAR provide complementary geometric guidance during representation construction. A ray-guided deformable-attention lift weights sampled image features using LiDAR-supervised camera depth probabilities and radar frustum occupancy, while radar additionally refines the depth distribution before lifting. Because conventional radar provides limited elevation information, LiDAR-derived class-occupancy targets supervise the side and front planes during training; the corresponding heads are removed at inference, so deployment requires only cameras and radar. For temporal aggregation, Doppler-guided temporal fusion aligns past features using a motion field anchored by measured radar radial velocity, with gating that limits warping in regions without supported motion. An RCS-aware radar scatter further allows radar evidence to spread over spatial neighborhoods conditioned on radar cross section. On the nuScenes validation set, RLG-TPV achieves 0.4981 mAP and 0.5959 NDS, reducing orientation and velocity error by 31.9\% and 30.7\% relative to the published CRN baseline. Ablation studies show that ray-level geometric guidance is a major contributor to the final performance.

---


### 134. [Bayesian-Optimized Superpixel-GrabCut for Traceable Optic Disc Segmentation](https://arxiv.org/abs/2608.29196)

**<font color=#1a73e8>作者：</font>** Shraddha Changune, Vivek Noel Soren, Gautam Das 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optic disc (OD) segmentation is essential for diagnosing ophthalmic pathologies from retinal fundus images. However, prevailing deep learning approaches operate as opaque black boxes, lacking the inference-stage mathematical traceability--a critical requirement for algorithmic auditing and failure analysis in clinical workflows. This paper presents a fully algorithmically traceable and trainable segmentation pipeline that jointly combines superpixel decomposition, hybrid brightness-proximity superpixel scoring, morphological regularization, iterative GrabCut refinement, and elliptical shape fitting. The hyperparameter optimization is formulated as an objective function and solved via Bayesian optimization to eliminate manual parameter tuning. A quantitative evaluation on the Drishti-GS dataset demonstrates that our method achieves a Dice coefficient of 0.9536, matching state-of-the-art performance. By maintaining explicit mathematical transparency across all processing stages, our framework offers a deterministic, traceable alternative to black-box architectures for medical review and debugging.

---


### 135. [PokaiTrainer: Scaling Belief-State Search to Competitive Pokémon VGC](https://arxiv.org/abs/2608.29197)

**<font color=#1a73e8>作者：</font>** Max Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-time equilibrium search carried poker to superhuman play, but it has so far relied on tractable subgames: a handful of actions per decision, chance confined to card deals, one player moving at a time. Competitive Pokémon in its official doubles format (VGC) breaks all three assumptions at once. Both players act simultaneously from joint menus in the hundreds, each joint action resolves to hundreds of stochastic outcomes, and the opponent's reserves and stat allocations are hidden. We set out to build a strong VGC agent and report what that took. PokaiEngine, our Rust battle engine, enumerates a joint action's full weighted outcome distribution in one pass, at ${\sim}99\%$ parity with Pokémon Showdown and a fraction of the cost of sampling it. On top of the engine, PokaiTrainer adapts Student of Games to this scale, solving every decision as a Bayesian matrix game over public belief states and growing subgames under an explicit compute budget. On the live Showdown best-of-three ladder, the agent wins 59% of 150 sets against a human field averaging ${\sim}1320$ Elo. It settles into a 1350-1400 Elo band, and at its peak briefly entered the format's top 500.

---


### 136. [Imag-Eval: a language-grounded framework for interpretable Text-to-Image instruction following evaluation](https://arxiv.org/abs/2608.29210)

**<font color=#1a73e8>作者：</font>** Ibrahim Mohamed Serouis, David Jaramillo Duque  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-Image (T2I) models have recently achieved impressive visual fidelity, yet their evaluation remains constrained by benchmarks that are often difficult to interpret and insufficiently diagnostic. Existing skill-based evaluations tend to overlook critical failure modes that strongly impact usability but fall outside standard taxonomies, such as global incoherence arising from missing parts or physically implausible configurations (e.g., floating objects). In addition, prompt difficulty is typically controlled along a single dimension; either prompt length or the number of elements to generate. To address these limitations, we introduce Imag-Eval, a controlled benchmark designed to assess how T2I models ground compositional natural-language instructions into visual outputs. Unlike prior work that conflates surface linguistic complexity with compositional difficulty, Imag-Eval explicitly seeks to disentangles these factors by independently varying both the number of instances and the combination of constraints (rules), while avoiding error propagation. This design enables fine-grained and interpretable analysis of where cross-modal instruction following fails. Our benchmark comprises 1,140 prompts and 8,842 combined rules, and we evaluate it on several state-of-the-art models. Complementing this analysis with an additional study of over 2,000 prompts from a concurrent benchmark, our results suggest that, for structured skills, compositional difficulty is primarily governed by the number of grounded rules and their binding to instances,, rather than by prompt length alone.

---


### 137. [Ground-to-Satellite Localization in Unconstrained Image Collections for 3D Scene Reconstruction](https://arxiv.org/abs/2608.29211)

**<font color=#1a73e8>作者：</font>** Angel Daruna, Ben Southall, Niluthpol Chowdhury Mithun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ground image localization with respect to satellite imagery is a key enabler for metrically-accurate, geo-localized 3D scene reconstruction from unconstrained image collections. Existing cross-view localization methods have strict requirements such as panoramic imagery or known initial locations, limiting their applicability for in-the-wild reconstruction settings. We propose a robust hierarchical cross-view localization framework that leverages geometric constraints from Structure-from-Motion (SfM) models derived from unconstrained ground image collections. Our method generates coarse-to-fine pose hypotheses through a cross-view matching approach and aggregates noisy predictions across SfM model(s) using Kernel Density Estimation to recover consensus alignments while filtering outliers. Experiments demonstrate reliable localization performance from challenging image collections. Empirically we found satellite-referenced alignment enables accurate metric scale estimation, doppelgänger detection, and merging of disjoint SfM reconstructions, resulting in more complete, geo-localized site models than are possible with SfM alone.

---


### 138. [Asymmetric Phase Coding Video Watermarking](https://arxiv.org/abs/2608.29212)

**<font color=#1a73e8>作者：</font>** Guang Yang, Fengchen Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing video watermarking systems are symmetric: the party that can verify a mark holds the extractor weights or generator secret and can therefore also embed one. Benchmarks confirm the consequence, reporting that white-box forgery defeats all evaluated methods. We present a training-free video watermark that removes the shared secret. The signer embeds a complete Ed25519 signature into the phase spectrum of the chroma plane; any party holding the 32-byte public key and public per-video metadata verifies offline, with no model, no registry, and no network. The payload, 1024 bits of signed message with error correction, is an order of magnitude above common learned payloads and is carried by three design elements: a run-length temporal layout whose decoder identifies payload groups by correlation and never reads a frame index, a payload-free search that recovers scale, rotation, and translation from the carrier itself, and a closed-loop signing procedure that selects each video's embedding strength by self-verification through the unchanged public verifier. On 1000 uncurated real-world clips the system ships a verifying signature for 99.3% of the corpus and accepts a wrong public key zero times in 1000 attempts. An attack-aware acceptance gate yields embeddings that survive H.264 re-encoding at 100% and 50% rescaling at 97.4% on gated clips. The signature also verifies through a real display and capture loop, an axis absent from published evaluations.

---


### 139. [SGPDFuse: Semantically-Guided Physics-Disentanglement General Multi-Modal Image Fusion](https://arxiv.org/abs/2608.29220)

**<font color=#1a73e8>作者：</font>** Haozhen Wei, Chengjun Jiang, Yutong Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal image fusion (MMIF) aims to integrate complementary sensor data into a single representation that preserves intrinsic scene reality while eliminating environmental interferences. Most existing approaches rely on blind feature aggregation, which excels at signal accumulation but fails to distinguish essential content from physical degradations. We propose SGPDFuse, which bridges this gap by mapping inputs into a physics-disentangled structural representation via a Semantic-Physical Parametric Bridge (SPPB) built on pretrained vision foundation models, utilizing the Intrinsic-Variation principle to decouple invariant scene attributes from transient environmental factors. To guide this decomposition, we introduce a Semantic Alignment mechanism: we explicitly anchor the fused representation to salient semantic features in the same foundation model feature space via cosine similarity to preserve critical targets, while enforcing physical texture fidelity through Gram-matrix regularization to strictly eliminate unnatural artifacts. Extensive experiments demonstrate that SGPDFuse achieves state-of-the-art performance across infrared-visible, multi-focus, and multi-exposure benchmarks using a single architecture.

---


### 140. [Computational Depth Measurement in Thermographic Video: Overcoming Spatial Overfitting via Spatio-Temporal Decoupling](https://arxiv.org/abs/2608.29223)

**<font color=#1a73e8>作者：</font>** Zain Ul Abidin, Habeeban Memon, Junaid Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate through-thickness measurement of subsurface delamination depth in Carbon Fiber Reinforced Polymer (CFRP) is important for structural assessment because defect location determines affected load-bearing layers. Optical pulsed thermography (OPT) provides a two-dimensional thermal video rather than volumetric measurements, so depth must be inferred from temporal heat-diffusion responses. A challenge is spatial dataset bias: when calibration defects follow regular grids, regression models may memorize their geometry instead of learning physical relationship between thermal decay and depth. This work introduces a spatio-temporal decoupling architecture that separates spatial defect localization from temporal depth measurement. Defect regions are first localized using segmentation methods, after which thermal responses are spatially averaged and converted into sixteen physics-informed temporal, energy, statistical, and geometric features. These features expose the one-dimensional heat-conduction relationship while withholding pixel coordinates from the depth model. Four regression models are evaluated using specimen-level cross-validation: Random Forest (RF), Gradient Boosting Machine (GBM), Advanced Multi-Layer Perceptron (Adv-MLP), and XGBoost. Unregularized trees and over-parameterized Adv-MLP exhibit calibration collapse under geometric shifts, with errors exceeding 0.5 mm. In contrast, regularized XGBoost with L1/L2 penalties and column sampling maintains cross-specimen calibration, achieving a mean absolute error (MAE) of 0.056 mm and root mean square error (RMSE) of 0.085 mm. Predicted depths are merged with masks to generate Delaunay-triangulated three-dimensional defect models in three to five seconds per specimen. Results show that mathematical regularization and spatio-temporal decoupling reduce spatial memorization in thermal-video depth regression.

---


### 141. [Using Channel Representations in Regularization Terms: A Case Study on Image Diffusion](https://arxiv.org/abs/2608.29227)

**<font color=#1a73e8>作者：</font>** Christian Heinemann, Freddie Åström, George Baravdish 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work we propose a novel non-linear diffusion filtering approach for images based on their channel representation. To derive the diffusion update scheme we formulate a novel energy functional using a soft-histogram representation of image pixel neighborhoods obtained from the channel encoding. The resulting Euler-Lagrange equation yields a non-linear robust diffusion scheme with additional weighting terms stemming from the channel representation which steer the diffusion process. We apply this novel energy formulation to image reconstruction problems, showing good performance in the presence of mixtures of Gaussian and impulse-like noise, e.g. missing data. In denoising experiments of common scalar-valued images our approach performs competitive compared to other diffusion schemes as well as state-of-the-art denoising methods for the considered noise types.

---


### 142. [Compact Snapshot Spectral Imaging with Calibration-Free Aperture Diffraction](https://arxiv.org/abs/2608.29230)

**<font color=#1a73e8>作者：</font>** Tao Lv, Quan Yuan, Shiqiao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Snapshot Spectral Imaging (SSI) provides high-dimensional temporal-spatial-spectral observation to uncover intrinsic physical characteristics. However, its complex system and repetitive calibration requirements hinder edge applications. Here, we propose a compact, cost-effective, calibration-free SSI method, Aperture Diffraction Imaging Spectrometer (ADIS), which consists only of a diffractive lens with a binary mask and a Bayer-filtered sensor, requiring no additional physical footprint compared to standard RGB cameras. ADIS disperses and multiplexes wavelengths, mapping energy to distinct sensor locations, enabling full-resolution recovery from superpixel-level encodings. ADIS directly leverages theoretically computed PSFs to enable calibration-free spectral reconstruction, while tolerating lens-dependent variations across different optical configurations and bridging the gap between simulation and reality. To achieve SSI by solving a sparsely-constrained inverse problem, we introduce the Orthogonal Diffraction-Aware Unfolding Framework (ODAUF) with Voxel Shift Transformer (VST) for improved orthogonal diffraction perception. Integrating VST into ODAUF forms the efficient Orthogonal Diffraction-Aware Unfolding Voxel Shift Transformer (ODAUVST), delivering excellent recovery and reduced parameters. By elaborating on theory, systematic and comprehensive comparing, and demonstrating real SSI results, we validate the superiority of ADIS, achieving calibration-free full-resolution SSI within a commercial camera footprint.

---


### 143. [Background-Free Objectness Learning for Class-Agnostic Detection](https://arxiv.org/abs/2608.29232)

**<font color=#1a73e8>作者：</font>** Dania Batool, Liliana Lo Presti, Marco La Cascia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detectors are typically trained under closed-set supervision, where unlabeled regions are implicitly treated as background. Under incomplete annotations, this assumption introduces objectness bias: visually valid but unlabeled objects are used as negatives, tying objectness to the annotated taxonomy rather than generic object structure. This limitation is particularly problematic for class-agnostic and open-world detection. This paper proposes Background-Free Objectness Learning (B-FOR), a dense class-agnostic detection framework that learns objectness without explicit background supervision on unlabeled regions. B-FOR formulates detection as the prediction of dense multi-scale object-center and scale fields, from which object hypotheses emerge as local spatial structures. Supervision is confined to reliable annotated regions through spatially structured soft targets, avoiding foreground-background discrimination. To support decoding from emergent local maxima, the paper further introduces displacement-aware scale fields that model object extent as a spatially varying property of the learned objectness field. Experiments on PASCAL VOC, MS-COCO, and Open Images demonstrate strong generalization to unseen categories and cross-dataset object distributions. B-FOR improves recall by more than +10 AR points over prior class-agnostic baselines. Ablation studies show that both localized objectness supervision and displacement-aware scale fields are critical for class-agnostic localization under incomplete annotations. Code available at: this https URL.

---


### 144. [Generalization over Memorization: Generalization-Aware Diffusion Adaptation for Single-Image Multi-View Synthesis](https://arxiv.org/abs/2608.29233)

**<font color=#1a73e8>作者：</font>** Jie Li, Xingchen Zou, Yuxuan Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present the winning solution to the ACM Multimedia 2026 Grand Challenge on Single-Image Guided Multi-Angle Image Synthesis. It ranks first among 293 registered teams; 56 teams obtained at least one scored submission on the public Phase-A leaderboard. With only 40 training scenes, the challenge requires 26 target views from one RGB model and one forward pass per view; it prohibits explicit geometry, external rendering, chained generation, candidate selection, and post-processing. We identify a critical model-selection failure: shared training and validation scenes make memorization appear as transferable view control. We therefore introduce GoM. Short for Generalization over Memorization, the framework combines scene-disjoint validation, exposure-matched selection, and targeted diffusion adaptation. Its synthesis model adapts a 4B rectified-flow DiT using rank-32 LoRA, optimizer restarts, late-checkpoint averaging, and VAE decoder tuning. More than 300 offline experiments and 24 online submissions show that validation design and training-trajectory control can matter as much as architecture scale in small-data generative modeling.

---


### 145. [Uncertainty-Aware Multimodal Anti-UAV Detection via Evidential Fusion and Conflict-Discounted Belief Aggregation](https://arxiv.org/abs/2608.29235)

**<font color=#1a73e8>作者：</font>** Sharanda Suttorp, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansour Alsahag  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anti-UAV perception systems must remain reliable when sensor streams degrade under occlusion, fast motion, or modality-specific failure. Existing multimodal anti-UAV systems fuse RGB and thermal streams deterministically, without modeling predictive uncertainty, and cannot express doubt when streams disagree. Evidential Deep Learning (EDL) produces calibrated per-class uncertainty in a single forward pass. EDTC already exploits this for thermal-only perception, yet cross-modal evidential fusion remains unaddressed.
This paper extends EDTC to multimodal RGB-Thermal perception via Discounted Belief Fusion (DBF), which converts inter-modal conflict into uncertainty mass before aggregating stream opinions. Bounding boxes are resolved by selecting the lower-uncertainty modality. On the Anti-UAV benchmark, multimodal fusion consistently outperforms either single stream (test Acc 0.670 vs. 0.604 IR, 0.598 RGB) at real-time speed (at least 38 FPS). However, DBF is empirically indistinguishable from undiscounted averaging: near-zero inter-modal conflict on this presence-dominated benchmark leaves the discounting step inert. The fused uncertainty is well-calibrated (ECE 0.057) yet expectedly a weaker localization failure detector than spatial variance (AUROC 0.626 vs. 0.739). The null result is structural: the benchmark's near-universal presence and vacuous miss-encoding jointly suppress inter-modal conflict, a diagnosis that delimits where conflict-aware fusion provides measurable benefit.

---


### 146. [AGRICAM: A Track-Mounted Crop Pollination Monitoring Robot](https://arxiv.org/abs/2608.29237)

**<font color=#1a73e8>作者：</font>** Malika Nisal Ratnayake, Adel N. Toosi, James Cook 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Insect pollination is critical for global food production, yet monitoring pollinators at commercial farm scale remains a challenge. Recent advances in computer vision and deep learning have enabled detailed analysis of pollinator behaviour, but monitoring must trade-off detail against spatial coverage and human or technological resources. This paper presents the Automated Guided Robot for Insect and Crop Activity Monitoring (AGRICAM), a purpose-built robotic system designed to meet the requirements of large-scale pollination monitoring in protected cropping systems. AGRICAM operates autonomously on low-cost, easily installed track for movement along crop rows, without disrupting farm operations or insect behaviour. The platform integrates two RGB cameras, microclimate sensors, GPS and RFID modules, motion sensors, and 4G cellular network connectivity for data transmission. A web interface enables remote device configuration and scheduling. The system autonomously captures video and image data of insects' locations and local environmental conditions. These are transferred to the cloud and analysed using computer vision models to quantify pollinator visitation and spatio-temporal activity variation. We deployed the system on a commercial blueberry farm to demonstrate and test its capability. It successfully mapped insect pollination patterns across 80 m long industrial polytunnels over 30 hours. This data enabled spatial analyses of insect activity we used to confirm a uniform pollinator distribution within polytunnels, as desired by the farm management team. The data also highlighted variation of insect activity associated with time of day and microclimate. AGRICAM therefore has been shown to be a scalable, automated crop pollination monitor that can support data-driven decisions to enhance pollination management, thereby improving crop productivity and food security.

---


### 147. [Anchoring Speech with Semantics: A Multimodal Adapter Mechanism for Automatic Speech Recognition in Low-Resource Languages](https://arxiv.org/abs/2608.29239)

**<font color=#1a73e8>作者：</font>** Kuan-Tang Huang, Cheng-Yeh Yang, Chien-Chun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource ASR remains difficult because scarce transcripts provide limited supervised evidence for target-side generation. To address this gap, we propose SAMA-ASR, a lightweight adapter mechanism that augments the decoder with semantic anchors from auxiliary translations and an acoustic anchor from speech; in principle, the mechanism can be applied to similar encoder--decoder multitask speech models. Through cross-modal adaptation, SAMA-ASR conditions decoder states on translation-derived semantic embeddings and a speech embedding, combining utterance-level meaning with speech-grounded evidence before token prediction. At evaluation time, these semantic anchors can be generated automatically by an upstream speech-to-text translator rather than supplied as oracle translations. Experiments on two 30-hour datasets covering the low-resource Sinitic varieties Taiwanese Hokkien and Hakka show that SAMA-ASR improves over acoustic, prior prompt-based, and semantic-only translation-guided baselines and remains effective in practical automatic semantic-anchor settings; translator-capacity analyses show that useful semantic anchors can be produced by a compact ST model.

---


### 148. [DARD: Zero-Shot Degradation-Aware Retinex-Guided Diffusion for Low-Light Image Enhancement](https://arxiv.org/abs/2608.29243)

**<font color=#1a73e8>作者：</font>** Wenjie Cai, Yuezhe Yang, Jianyang Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing diffusion-based enhancement methods provide strong generative capability for low-light image enhancement (LLIE), yet they either rely on paired supervision or lack reliable scene constraints in zero-shot settings, often leading to structural inconsistency and color drift. Motivated by conventional Retinex models, which offer physically interpretable priors that can serve as reliable scene constraints yet struggle with mixed degradations in real-world scenarios, we propose DARD, a zero-shot Degradation-Aware Retinex-guided Diffusion framework for LLIE. DARD first extracts image-specific physical priors from the degraded input through a test-time degradation-aware Retinex decomposition, thereby providing reliable structural guidance for zero-shot restoration. It then injects these priors into reverse diffusion through a timestep-adaptive frequency fusion strategy to balance structural anchoring and detail generation. Finally, a guided reverse refinement process with physical consistency and Contrastive Language-Image Pre-training (CLIP)-based semantic guidance is introduced to suppress structural artifacts and semantic drift during sampling. Extensive experiments show that DARD achieves strong distortion and perceptual performance and consistently outperforms existing zero-shot baselines across multiple real-world low-light benchmarks. To further validate the practical utility of our method for downstream applications, we evaluated its impact on semantic segmentation. Experiments demonstrate that images enhanced by DARD achieve a 28.10% relative improvement in mIoU over AGLLDiff.

---


### 149. [RL-FAT: Reinforcement Learning for Fair Adversarial Training](https://arxiv.org/abs/2608.29247)

**<font color=#1a73e8>作者：</font>** Tejaswini Medi, Levan Mikeladze, Margret Keuper  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks remain highly vulnerable to adversarial perturbations, and adversarial training (AT) has become a widely used approach for improving robustness. However, improvements in average robust accuracy often mask substantial class-wise disparities: while some classes become more robust, others may remain disproportionately vulnerable under attack. This imbalance raises an important adversarial fairness concern, particularly in vision tasks where reliable robustness is expected across all categories. To address this challenge, we propose \textbf{RL-FAT}, a reinforcement-learning-inspired fair adversarial training framework that uses policy-gradient based feedback from adversarial predictions. RL-FAT interprets the prediction distribution as a policy and combines correctness-based prediction rewards with class-wise value estimates to compute class-specific advantages for policy-gradient optimization. This enables the model to adaptively focus on class-wise misclassification. Furthermore, we introduce a fairness-emphasis adversarial loss that assigns stronger training pressure to classes with high adversarial loss, thereby mitigating class-wise robustness disparity. By combining reinforcement-driven adaptation with fairness-emphasis regularization, RL-FAT improves adversarial robustness while promoting a more balanced robustness distribution across classes. Extensive experiments demonstrate that our method achieves competitive robust accuracy and substantially reduces class-wise robustness imbalance compared with standard adversarial training baselines.

---


### 150. [Dynamic Important Example Mining for Reinforcement Finetuning](https://arxiv.org/abs/2608.29252)

**<font color=#1a73e8>作者：</font>** Haoru Tan, Sitong Wu, Yanfeng Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement fine-tuning (RFT) is increasingly used to strengthen the reasoning abilities of large models, yet its effectiveness is bound by how training data are selected and used. Most data-centric RFT methods rely on static or heuristic sample selection, implicitly assuming a sample's value is fixed over training. This overlooks the non-stationary dynamics of policy learning and can lead to suboptimal updates. We propose Dynamic Important Example Mining (DIEM), a principled and fully automated framework that makes data utilization adaptive throughout RFT. DIEM integrates two components into each optimization step: (i) a gradient-alignment importance estimator that efficiently approximates each sample's marginal contribution to policy improvement; and (ii) a constrained batch reweighting scheme that maximizes aggregate utility while preserving the update's gradient magnitude to stabilize optimization. Across several reasoning benchmarks, DIEM consistently outperforms strong static and dynamic baselines. The code will be released via this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
