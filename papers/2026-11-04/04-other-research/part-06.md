# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

---

### 251. [CipherFlow: Compiling AI Programs for Efficient Cryptographically Secure Inference](https://arxiv.org/abs/2611.01450)

**<font color=#1a73e8>作者：</font>** Hedong Zhang, Mengxin Zheng, Qian Lou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographically secure inference faces two practical challenges: making secure programming accessible to AI developers and data scientists, and achieving efficient execution across deployment environments. Developers must compose cryptographic primitives correctly, while performance depends on hardware, networks, and evolving ciphertext states. We present CipherFlow, a compiler framework that takes a high-level AI computation graph, available cryptographic primitives, and a target hardware and network configuration to generate an executable, latency-optimized secure inference program. CipherFlow automates cryptographic execution decisions through three techniques: MicroBench profiles deployment-specific primitive costs; state-expanded planning jointly optimizes homomorphic encryption (HE) and secure multi-party computation (MPC) placement, conversions, and ciphertext maintenance under cryptographic-state constraints; and BlockFold summarizes branched regions to scale planning to Transformer graphs. Evaluation using measured HE/MPC backend costs across CPU/GPU and network settings shows up to 16.5$\times$ speedup on BERT-base and over 22$\times$ on ViT compared with static hybrid placement baselines. CipherFlow separates model programming from cryptographic execution decisions, enabling developers to express AI computations while the compiler constructs efficient secure programs.

---


### 252. [ContactCut: A Partition-Aware Contact Selection Framework for False-Merge Correction in Connectomics](https://arxiv.org/abs/2611.01457)

**<font color=#1a73e8>作者：</font>** Byunghyun Ko, Won-Ki Jeong, Chaoli Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Localized false-merge correction in connectomics requires converting an identified error into an executable native 3D partition. Still, neither intermediate correction predictions nor seeded graph solvers alone determine which native source-sink constraints should define that partition. We formulate this problem as a 3D-native partition-aware contact selection problem: selecting candidate contacts based on the complete partitions they induce. Our solution comprises two components: ContactCut (CC)-Auto, which uses learned single-contact selection, and ContactCut (CC)-Search, which enables bounded paired-contact search, generates compact alternatives, and applies learned panel ranking. On historical two-way false-merge corrections from MICrONS and FlyWire, CC-Auto improves failure-aware 3D partition (FA-3D Part.) mIoU by 5.9 and 3.4 points over the strongest graph-based controls and by 12.5 and 10.0 points over the best learned baselines. A MICrONS-trained ranker transfers to FlyWire with negligible degradation. CC-Search expands oracle reachability and prioritizes near-oracle alternatives. The code is available at this https URL.

---


### 253. [Resolve, Clear, or Defer: Training-Free Active Prototype Triage for Ecological Detection Pipelines](https://arxiv.org/abs/2611.01466)

**<font color=#1a73e8>作者：</font>** Anirudh Potlapally, Brijesh Nanda Brunda Yogananda, Jianyang Gu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ecological monitoring increasingly relies on camera traps and aerial surveys that generate large image collections. High-recall animal detectors can localize candidate animals at scale. However, they also produce many detections that still require expert review, including false positives, ambiguous cases, and animals difficult to identify at the species level. Since exhaustive review requires substantial effort, we propose training-free active prototype triage, where reviewed detections become reusable evidence to (1) Resolve supported foreground classes, (2) Clear likely background false positives, or (3) Defer insufficiently supported cases for expert review. Across camera-trap and aerial datasets, foreground recognition and false-positive rejection benefit from different pretrained representations: BioCLIP2 provides foreground evidence while DINOv3 provides background evidence, reducing erroneous foreground clearing while improving automatic foreground recovery. Deferring unsupported cases avoids the higher error rates caused by forced decisions. Compared with confidence-thresholded multiclass k-NN and uncertainty-sampling logistic regression, prototype triage improves foreground recovery while maintaining competitive or lower review burden. Acquisition goes beyond class discovery: even after classes are represented, prototype choice determines how reliably evidence propagates through the remaining detections. Our results suggest that once animal localization reaches high recall, the challenge shifts from finding animals to deciding which examples to review, how to reuse them, and when evidence does not support an automatic decision.

---


### 254. [Endless VR Walk: Dynamic Mapping of Limited Physical Spaces into Infinite Linear Paths](https://arxiv.org/abs/2611.01495)

**<font color=#1a73e8>作者：</font>** Sofia Martinez, Reagan Haddix, Miles Haase 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Natural locomotion in virtual reality (VR) can provide a more immersive and engaging experience, but the physical space required for unrestricted walking is a significant limitation. This paper presents Endless VR Walk, a system for dynamically mapping a limited physical space into an effectively infinite linear virtual path. The approach uses a recursive path-generation algorithm to construct virtual blocks in real time as the user walks, while constraining the path to the available physical area and preventing spatial overlap. We evaluate path variability under different physical-space constraints and identify the smallest space that enables diverse path configurations. The resulting framework provides a platform for applications benefiting from extended walking, including physical therapy, rehabilitation, and fitness, as well as adaptations of traditional platformer and endless-runner games in VR.

---


### 255. [FedUDG: Federated Domain Generalization with Unlabeled Clients](https://arxiv.org/abs/2611.01498)

**<font color=#1a73e8>作者：</font>** Junyu Ren, Wensheng Gan, Philip S. Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated domain generalization (FDG) aims to learn models that generalize reliably to out-of-distribution (OOD) environments without centralizing client's data. However, existing FDG methods assume that all source clients have labeled data, limiting their ability to leverage the abundant unlabeled client data available in practice. To address this limitation, we propose FedUDG. At the federation level, FedUDG utilizes a parameter-functional differentiation strategy that maintains a semantic anchor updated solely using ground-truth labels. The remaining parameters absorb knowledge from unlabeled domains under bounded aggregation, preventing domain-biased noise from eroding the class semantics. Within each unlabeled client, FedUDG utilizes a student-teacher framework with two complementary objectives: (1) semantic self-training on high-confidence samples, using the functional differentiation between the semantic anchor and classifier to constrain the model to learn semantically pure and cross-domain stable features; and (2) label-free representation distillation on all unlabeled samples to stabilize learning under appearance variations. Together, these objectives guide the model toward a transferable feature space, while mitigating overfitting to domain-specific characteristics. Furthermore, to address the lack of systematic evaluation of FDG under formal privacy constraints, we develop a sample-level differentially private extension, DP-FedUDG, to quantify the trade-off between privacy and OOD generalization. Across four evaluation protocols, FedUDG consistently outperforms state-of-the-art baselines. The code is available at this https URL

---


### 256. [Improved Sample Complexity Analysis For First Order Bilevel Reinforcement Learning](https://arxiv.org/abs/2611.01500)

**<font color=#1a73e8>作者：</font>** Mudit Gaur, Naman Saxena, Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bilevel reinforcement learning optimizes an upper-level objective through the policy response to a lower-level reinforcement learning problem. Such problems arise when learning a reward model while adapting a policy to that reward. However, a gap remains between sample-complexity guarantees and practical actor--critic training. Tabular analyses restrict applicability to finite spaces, while continuous-state analyses often impose a uniform Polyak--Łojasiewicz (PL) condition. We show that this condition need not hold even for smooth positive policies with exactly representable values. We develop a single-loop, fully first-order method for continuous states and finite actions with specified multilayer neural actors and a persistently trained nonlinear critic built from fixed features. Under explicit initialization, regularity, feature-excitation, and value-realizability conditions, fixed reference-KL regularization yields local curvature, and we prove containment of the coupled iterates. Shared trajectories control sampling noise, while paired critic analysis controls normalized critic-error differences as the response perturbation shrinks. A joint descent and tracking argument establishes an improved $\widetilde{\mathcal O}(\varepsilon^{-2})$ sample complexity for $O(\varepsilon)$ expected squared gradient norm of the upper objective induced by the selected regularized policy response, including critic training.

---


### 257. [Abstention Spends Its Budget on Local Label Variance More Than on Novelty: Auditing Conformal Calibration and Selective Prediction under Molecular Scaffold Shift](https://arxiv.org/abs/2611.01512)

**<font color=#1a73e8>作者：</font>** Arnav Srivastava, Krishna Kassetty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selective prediction with split conformal calibration promises a post-hoc fix for molecular property prediction: abstain on the least reliable compounds, ideally out-of-distribution chemistry, and the retained set becomes trustworthy without retraining. We audit this recipe for a gradient-boosted fingerprint model on lipophilicity (regression) and BBBP (classification) under a Bemis-Murcko scaffold split, holding the fitted model and evaluation molecules fixed while varying only the calibration fold (18 replicates). (i) On lipophilicity, coverage depends on calibration provenance: calibrating on held-out training-scaffold molecules falls below nominal (PICP 0.841 at a 0.90 target), while novel-scaffold calibration recovers it (0.904); on BBBP, coverage stays above nominal in every regime. (ii) For split conformalized quantile regression (CQR) the conformal correction is a constant, so conformalization does not change what is abstained on. (iii) The abstention score (CQR width; effectively ensemble variance on BBBP) tracks local label variance more than chemical novelty: controlling for local label variance largely explains away the novelty association (partial Spearman 0.067 and 0.047). (iv) At a fixed assay budget, gating on interval width or ensemble variance never improves hit precision over ranking by point prediction, at the pre-specified operating point or across 20 exploratory settings; a plain novelty gate shows small, uncorrected gains at the smallest budgets. (v) In an exploratory analysis, exact conformal selection exceeds its false discovery rate target under training-scaffold calibration (0.303 at q=0.2) and is consistent with it under novel-scaffold calibration, contributing a data-driven batch size rather than a better ranking. Conformalization earns its keep through guarantees whose validity hinges on calibration provenance, not by choosing what to abstain on.

---


### 258. [InformedXRD: Reproducible Benchmarks and Physics-Informed Evaluation for Powder Diffraction Symmetry Classification](https://arxiv.org/abs/2611.01525)

**<font color=#1a73e8>作者：</font>** Edward G Friedman, Elizabeth J. Baggett, Abhishek Shetty 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning for powder diffraction (PXRD) symmetry classification is being trained at scale, yet the field lacks a common evaluation standard: papers report results on different subsets of experimental archives, with different target taxonomies, preprocessing, and metrics, and published models are rarely released in a form that permits rescoring. We present InformedXRD, an evaluation framework with three parts: (i) a machine-readable mapping from 230 space groups to 99 extinction groups, the finest classes powder diffraction can identify from systematic absences alone; (ii) a benchmark-construction method whose inclusion rules are specified as code and reproduce from a frozen snapshot, instantiated as RRUFF-473, RRUFF-325, and, as a small example, opXRD-98; (iii) a reporting protocol with prior-only frequency baselines, a label-permutation test, a hierarchy-aware error metric on the condensed translationengleiche subgroup graph, and stratified evaluation. We build on the mapping, RRUFF benchmarks, subgroup graph, and four ViT checkpoints released in our earlier work (Baggett et al., 2026). Using these checkpoints, a 1D residual CNN, and six architectures trained under the XRDBench recipe (Cao et al., 2025), we show that evaluation design changes what conclusions are justified: paired tests point in different directions at Top-1 and Top-5; paired Top-k tests do not separate the three leading XRDBench models, while hierarchy-aware analysis describes error distance and direction across all six; an input-blind frequency predictor matches the models on aggregate Top-k, yet a label-permutation test still detects pattern-specific evidence; and stratified analysis exposes a label-entropy confound that aggregate accuracy hides. All mapping tables, benchmark code, scripts, and checkpoints are released as shared infrastructure for PXRD-ML evaluation.

---


### 259. [Learning Gradients of Homogeneous Functions](https://arxiv.org/abs/2611.01530)

**<font color=#1a73e8>作者：</font>** Mayur S. Gowda, Srinivasa Pranav, Shreyas Chaudhari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Homogeneous gradient functions have widespread significance, including applications in maximum energy subspace selection and retrieval problems. Euler's homogeneous function theorem specifies how the potential associated with a positively k-homogeneous gradient field can be recovered directly from the field itself. We use Euler's theorem to build on GradNets and propose a homogeneous gradient network architecture that is guaranteed to correspond to the gradient of a homogeneous function. Then, we describe how monotone homogeneous GradNets universally approximate the gradients of k-homogeneous convex functions. The inductive bias of homogeneous GradNets enables them to outperform baseline ICNNs by up to 7dB in our max energy subspace projection experiment and by up to 13% higher accuracy, 98% fewer parameters, and 70% fewer FLOPS in our amortized inner product search experiment.

---


### 260. [AbacusGS: Gaussian Splatting without Per-Splat Sorting](https://arxiv.org/abs/2611.01534)

**<font color=#1a73e8>作者：</font>** Jiacheng Ding, Yanliang Qi, Cong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting sorts every splat by depth in every frame. Viewers that draw splats with the hardware rasterizer and sort them on the CPU, as most web and mobile viewers do, spend most of the frame time in this sort. We present AbacusGS, which stores the blending order of a 3DGS scene in the scene layout. AbacusGS groups the splats into octree boxes of at most 128 splats and stores each box in order along an axis chosen at write time. In each frame, AbacusGS sorts only the visible boxes, and one dot product per box decides whether the box is read forward or backward. A short order-aware fine-tuning converts an existing 3DGS model, and the over operator of 3DGS stays unchanged. On 13 standard scenes, AbacusGS loses 0.13 dB PSNR on average against an equally fine-tuned 3DGS model. In an OpenGL viewer that orders splats on the CPU, AbacusGS renders frames 4.5 times faster than per-splat sorting. We also present a compact format of 17 bytes per splat and a CUDA tile renderer that use the same order. The code will be released.

---


### 261. [CUFormer: Modality-Aware CT-Ultrasound Point Cloud Registration for Orthopedic Navigation](https://arxiv.org/abs/2611.01536)

**<font color=#1a73e8>作者：</font>** Lixing Tan, Qing Xia, Yuting Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Registering intraoperative Ultrasound (US) bone-surface point clouds to preoperative Computed Tomography (CT) models can support radiation-free orthopedic navigation. Differences in imaging physics produce distinct surface sampling patterns, complicating cross-modal feature matching. Bone strongly reflects ultrasound and casts an acoustic shadow, so US captures only the probe-facing bone surface and leaves most CT points unmatched. This partial coverage makes correspondences ambiguous on near-symmetric bones. We propose CUFormer, a modality-aware registration framework. We introduce a Modality-Aware Transformer (MAT) that encodes input modality through identity embeddings and updates features through modality-specific adapters within a shared geometric matcher. We model imaging visibility and use predicted reference-side visibility to weight coarse and fine correspondences. CUFormer achieves the lowest mean registration errors among evaluated methods on two CT-US datasets, UltraBones100k and UltraBonesHip, and the CT-RGB-D dataset SpineDepth. On UltraBones100k, it reaches mean rotation error 4.53$^\circ$, translation error 3.19\,mm, and Root Mean Squared Error (RMSE) 2.54\,mm, reducing RMSE by 65.8\% relative to the best-performing baseline by this metric. These results demonstrate CUFormer's effectiveness in aligning partial bone surfaces with preoperative CT across anatomical sites.

---


### 262. [The Structure of Disagreement in Emotion Annotation](https://arxiv.org/abs/2611.01539)

**<font color=#1a73e8>作者：</font>** Emily Öhman, Anna Koufakou, Eugenia Diegoli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Calculating inter-annotator agreement is an established practice in NLP, and disagreement-aware work increasingly retains the distribution of human judgments rather than reducing annotations to a single gold label. Keeping the distribution, however, does not explain why annotators disagree. This paper examines the types of disagreement that occur in emotion annotation, starting from multilabel annotations of 1,677 sentence-level units from Ernest Hemingway's The Old Man and the Sea and testing the patterns they reveal against individual-level annotations from BRIGHTER and GoEmotions. Across the three datasets, we find three main recurring disagreement structures. Emotion categories overlap systematically; annotators differ both in how broadly they apply labels and in how they treat particular category boundaries, while sparse participation and explicit abstention can look like disagreement. Where intensity is rated, disagreement over whether an emotion is present can be separated from disagreement over its intensity once recognized. Similar aggregate disagreement can therefore arise from qualitatively different annotation processes. Hard aggregation removes most of this structure, while annotator vote-share representations keep marginal label frequencies but not the co-occurrence, annotator-specific, or procedural patterns that produced them. We argue that disagreement should be understood in terms of its underlying patterns before it is summarized, aggregated, or used as a modeling target, and propose a vocabulary for disagreement structure.

---


### 263. [GSExplorer: Interactive World Generation with a Persistent 3D Gaussian World State](https://arxiv.org/abs/2611.01543)

**<font color=#1a73e8>作者：</font>** Sicheng Yu, Liu Liu, Xinjie Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive world generation requires both accurate local control and stable scene consistency over long rollouts. Existing methods improve local generation through camera or geometry conditioning and extend historical context with memory mechanisms. However, long-horizon exploration remains challenging as target-view guidance becomes incomplete and inconsistencies accumulate across repeated scene updates. We present \textbf{GSExplorer}, a generation--reconstruction framework built around a persistent 3D Gaussian world state. At each step, the current 3DGS scene provides multimodal rendering conditions for a condition-driven video generator, while camera geometry is injected through a separate Relative Ray Encoding branch. Generated videos are then fed back to a SLAM-based reconstruction backend, where inconsistency filtering prevents conflicting content from corrupting the scene and cross-chunk bundle adjustment improves spatial alignment across generation steps. We further design a data-construction pipeline that reproduces realistic 3DGS degradation during scene extrapolation, yielding 293K training pairs of degraded multimodal renderings and real target videos. GSExplorer achieves the best overall performance among the compared methods on both single-step and three-step WorldScore evaluation, with strong camera control and consistency across both settings, including a Camera Control score of 99.07 in single-step extrapolation. On 481-frame leave-and-return rollouts, it also shows strong revisit consistency, demonstrating the value of maintaining a reliable 3D world state for continued exploration.

---


### 264. [Band2Net: Frequency-to-Network Transport Distillation for fMRI-Privileged, EEG-Only Session-Condition Decoding](https://arxiv.org/abs/2611.01548)

**<font color=#1a73e8>作者：</font>** Nishi Kanta Paul, Md Shihabul Islam Shovo, Dwarikanath Mahapatra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Functional MRI resolves large-scale brain networks but is expensive and stationary, whereas EEG is portable but poorly localised. We treat fMRI as privileged information, available during training and absent at deployment, with EEG and fMRI acquired from the same participants under matched conditions but not simultaneously. Band2Net encodes EEG into five frequency-specific connectivity graphs and fMRI into seven canonical network tokens from a frozen teacher, and solves a balanced entropic transport problem between the two token sets that gives each EEG band its own fMRI target. In subject-grouped cross-validation on the PsiConnect psilocybin data set, Band2Net reaches 0.801 ROC-AUC for EEG-only session-condition decoding, 5.0 AUC points (95% CI 1.8-8.2) above an EEG-only student. Although its margins over a single shared plan, a KL-relaxed plan and label-free network descriptors remain unresolved, secondary comparisons favour band-specific transported targets over logit, global-feature, contrastive and pooled-target distillation, though not after Holm correction.

---


### 265. [Detecting Generated-Depth Injection Attacks on RGB-D Place Authentication](https://arxiv.org/abs/2611.01550)

**<font color=#1a73e8>作者：</font>** Seigo Kawachi, Satoshi Matsuura  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advances in monocular depth estimation (MDE) now let an attacker generate depth from publicly available RGB images and submit forged RGB-D queries. Such attacks break a core assumption of RGB-D place authentication: that depth comes from a sensor. We study a presentation attack detection (PAD) classifier that uses geometric consistency between the enrollment and query views, as a software-layer defense. A three-stage evaluation shows how far this classifier detects software-injected depth, depending on how accurately the attacker knows the camera intrinsics. In the first stage, the attacker has only an estimate of the intrinsics, and the PAD classifier separates forgeries generated by all three MDE models with a validation area under the receiver operating characteristic curve (AUC) of 0.997-0.999. In the second stage, the attacker obtains the exact intrinsics, and the original PAD classifier falls to near chance (AUC 0.54-0.61); a retrained PAD classifier, however, still has the registration residual between enrollment and query as a cue. In the third stage, an oracle evaluation, in which the evaluator fits warps using the ground-truth 3D geometry, shows that detection falls to near chance only in its strongest case, where every valid query keypoint is given its ground-truth 3D coordinate. Of the detection cues, the reprojection error captures the attacker's misestimate of the intrinsics, whereas the registration residual remains even when the attacker knows the exact intrinsics.

---


### 266. [TopoDPO: Dense Preference Alignment for Structure-Sensitive Aerial Referring Segmentation](https://arxiv.org/abs/2611.01551)

**<font color=#1a73e8>作者：</font>** Huaiyuan Peng, Jisheng Dang, Wencan Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preference optimization for multimodal segmentation faces a granularity mismatch: dense masks contain spatially heterogeneous preference signals, whereas image-level objectives assign one shared nonlinear weight to all spatial margins. We introduce TopoDPO, a topology-aware dense preference alignment framework for structure-sensitive aerial referring segmentation. Topo-Prior mines informative preference pairs using connected-component discrepancy and macro-corner recall, while the dense objective applies the preference penalty to each local margin before spatial aggregation against a frozen supervised reference. On Topo-RS-Hard, a 4590-instance structural stress set, TopoDPO improves intersection over union (IoU) from 50.91% to 51.24% over image-level direct preference optimization (DPO) and reduces Betti-0 error from 1.34 to 0.90; paired image-cluster bootstrap intervals against image-level DPO exclude zero for all five reported metrics. Matched supervised controls and a complete factorial analysis separate the effects of topology-aware pair mining, localized correction, and dense reference-relative preference weighting. An unfiltered stratification over all 39,244 validation records further shows the clearest structural gains on samples with moderate or severe pre-alignment component-count errors. The code is publicly available at: this https URL.

---


### 267. [Text-Assisted Event Stream Visual Place Recognition via Multi-Scale Spatiotemporal Optimal Transport](https://arxiv.org/abs/2611.01558)

**<font color=#1a73e8>作者：</font>** Lan Chen, Xingxing Xiong, Xiao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benefiting from the high dynamic range, high temporal resolution, and low energy consumption of event cameras, low-altitude economic research leveraging event cameras has become a popular topic. Several existing attempts introduce natural-language descriptions into visual place recognition (VPR) to mitigate the sparsity of structural spatial information inherent to event cameras. Nevertheless, these methods still fail to fully address two core challenges: effectively encoding event streams and semantically aligning event streams with text. In this paper, we propose a multi-scale spatial-temporal optimal transport approach, MSTOT-EPR, to address these challenges. Specifically, given event streams and scene text information, we first adopt a visual encoder and a text encoder to extract respective feature representations. We then apply optimal-transport constraints to achieve cross-modal alignment. We then design a cross-modal bottleneck fusion module to further fuse bimodal features. Furthermore, we develop multi-scale spatial optimal transport and inter-frame temporal optimal transport modules to mine high-quality spatial-temporal event features for scene recognition. Extensive experiments on the NYC-Event-VPR and EPRBench datasets fully validate the effectiveness of our proposed framework for event-based VPR. The source code of this paper will be released upon acceptance.

---


### 268. [Generative Modeling with Continuous Flows: Sample Complexity of Flow Matching](https://arxiv.org/abs/2611.01559)

**<font color=#1a73e8>作者：</font>** Mudit Gaur, Prashant Trivedi, Shuchin Aeron 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching has emerged as a promising alternative to diffusion-based generative modeling, offering a continuous-time ordinary differential equation formulation with fast sampling and a simple regression-based training objective. Despite its empirical success, some theoretical analyses idealize the learning procedure by assuming that the velocity field is obtained by exact empirical risk minimization. This assumption does not reflect the practical finite-dataset setting, where the empirical flow-matching loss is only approximately minimized by a finite number of stochastic-gradient updates. We develop an empirical-risk-minimizer-free analysis for flow matching that explicitly accounts for both finite-sample statistical error and finite-time empirical optimization error. Our analysis considers a finite dataset of \(N\) flow-matching samples and a learned parameter \(\theta_T\) obtained after \(T\) stochastic gradient updates on the empirical objective. Under regularity assumptions on the interpolation path, sub-exponential source and target distributions, approximation by a bounded-parameter smooth neural velocity class, empirical-loss optimization, and uniform flow stability, we prove a guarantee that holds with high probability over the finite training dataset and in expectation over the stochastic-gradient randomness. The resulting bound separates approximation error, statistical error from the finite dataset, tail error from unbounded source and target distributions, and empirical optimization error from approximate minimization of the finite-sample objective.

---


### 269. [Finite-Time Online Sample Complexity for Conditional Diffusion Models](https://arxiv.org/abs/2611.01562)

**<font color=#1a73e8>作者：</font>** Mudit Gaur, Prashant Trivedi, Sasidhar Kunapuli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the finite-time training and sampling error of conditional diffusion models trained by online stochastic-gradient denoising score matching. Rather than assuming access to an exact empirical or population risk minimizer, we analyze the score network produced after a finite number of stochastic-gradient updates under an explicit localized Polyak--Łojasiewicz (PL) condition, stochastic-gradient regularity, and a trajectory-containment assumption. Our analysis separates the network approximation complexity from the online training-sample budget and propagates both errors through the reverse diffusion process. Under anisotropic smoothness, a joint intrinsic-dimensional structure for the data and conditioning variables, sub-exponential tails, and explicit approximation-class compatibility, we obtain a conditional score approximation error of order \[ \widetilde{\mathcal O}\!\left(M^{-\eta_{\mathrm{app}}}\right), \qquad \eta_{\mathrm{app}} = \frac{2\alpha_x} {2\alpha_x+d_x'+(\alpha_x/\alpha_y)d_y'}, \] where \(M\) denotes the approximation complexity, \(d_x'\) and \(d_y'\) are the intrinsic response and conditioning dimensions, and \(\alpha_x,\alpha_y\) are their corresponding smoothness exponents. For \(N=RB\) online denoising samples used by SGD, the finite-time optimization error is controlled explicitly in terms of the PL, smoothness, gradient-noise, and initialization constants. Combining these ingredients with reverse-process stability yields a total-variation bound that decomposes into terminal-initialization, time-discretization, approximation/localization, and finite-time optimization errors.

---


### 270. [Meta-memorization and memorization scaling laws in transformers](https://arxiv.org/abs/2611.01564)

**<font color=#1a73e8>作者：</font>** Alex Nguyen, Kenneth A. Norman, Gautam Reddy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Larger transformers can memorize more data, with a capacity (in bits) that scales roughly linearly with the number of parameters. Counterintuitively, larger models also memorize faster, requiring fewer repetitions of a sequence during training before it is memorized. We reproduce both memorization scaling laws in transformers trained on random binary sequences, showing that rapid memorization can arise even when data contain no semantic or compositional structure. Rapid memorization is due to a meta-memorization effect, where models trained to memorize a large set of random sequences learn to memorize novel sequences more quickly. The rate $r(t)$ at which models memorize grows with training time $t$ as a power-law $r(t) \sim t^{\beta}$ with a fixed exponent $\beta$ but an increasing upper cutoff across model scales. Meta-memorization enables even one-layer transformers to few-shot memorize a 100-bit sequence. This effect is partly explained by the formation of structured attention heads that convey position-invariant sequence information to MLPs where memorized sequences are stored. Meta-memorization is recapitulated in a simplified model of a dense associative memory where retrieval is constrained by an attentional bottleneck. Our results suggest transformers, through pre-training, acquire reusable mechanisms that enable highly efficient storage and retrieval of memories.

---


### 271. [Beyond Validation Loss: Coverage and Reliability Dynamics in Robot Policy Pretraining](https://arxiv.org/abs/2611.01565)

**<font color=#1a73e8>作者：</font>** Zhanyi Sun, Max Simchowitz, Shuran Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In modern robot learning, generative robot policies are first pretrained through supervised learning from demonstrations, then refined through reinforcement learning, supervised finetuning, or other forms of posttraining. Yet conventional pretraining metrics, such as validation loss and average task success, provide an incomplete account of which policies support both effective direct deployment and subsequent posttraining. In this work, we study closed-loop pass@k, which evaluates the probability that k rollouts from the same initial condition attain at least one success. Thus, pass@1 measures mean task success; large-k pass@k measures whether success remains reachable under repeated sampling. Across a wide range of posttraining recipes, we show that large-k pass@k reveals posttraining differences not captured by pass@1. In particular, checkpoints with similar pass@1 but different large-k pass@k have different posttraining performance. Moreover, we show pass@k peaks at different checkpoints during supervised pretraining, revealing a coverage-reliability tradeoff over the course of training. Based on these observations, we propose two practical interventions: (1) a purely offline checkpoint-selection criterion that balances coverage and reliability without closed-loop evaluation, and (2) a generative data augmentation procedure that expands supervision beyond the finite demonstration set, preserving large-k pass@k while maintaining or improving pass@1 and raising the observed coverage-reliability Pareto frontier. Together, our results motivate evaluation, checkpoint selection, and training procedures that explicitly account for posttraining. Blog post, visualizations, and code are available at this https URL.

---


### 272. [Search-Aware On-Policy Self-Distillation with Sibling Alignment for Generative Recommendation](https://arxiv.org/abs/2611.01568)

**<font color=#1a73e8>作者：</font>** Rongfeng Guo, Zhuang Zhuang, Ji Dai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative recommendation retrieves items by autoregressively generating semantic IDs, typically via beam search. On-policy self-distillation (OPSD) enhances training supervision by transferring privileged self-teacher knowledge at student-generated states. However, beam-search retention depends on competition among prefixes: visited states differ in importance, and initially reliable decisions may approach the pruning boundary as training evolves. Moreover, conventional distribution matching couples target-token confidence with preferences among competing continuations, potentially weakening relational supervision when the self-teacher strongly favors the target. To address these challenges, we propose Search-Aware On-Policy Self-Distillation (SA-OPSD), a framework that transfers privileged self-teacher knowledge to the states visited during the student's own beam search. Specifically, we introduce Evolving-Boundary Sampling, which prioritizes search-critical states by considering both current pruning-boundary proximity and initial-reference retention-margin decline under a controlled distillation budget. Furthermore, we develop Confidence-Decoupled Branch Distillation, which separates target-probability calibration from informative sibling relations to better preserve the teacher's preferences among competing branches. Experiments on Industrial, Office, and Instruments demonstrate strong performance for SA-OPSD.

---


### 273. [Spend the Bits Where the Tiny Objects Are: Rate-Utility Region Coding for Aerial Detection](https://arxiv.org/abs/2611.01573)

**<font color=#1a73e8>作者：</font>** Yanliang Qi, Jiacheng Ding, Cong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bandwidth-limited aerial cameras must compress their images before a remote detector can find the many tiny objects in them. Threshold-based region-of-interest (ROI) coding sends only confidently detected regions, and because tiny objects provide limited visual evidence and often score low, it can discard the regions that contain them. We propose rate-utility region coding (RUO), which sends a region when its expected detection utility justifies its measured byte cost, choosing to drop it or to send it at low or high quality with one multiplier shared across images. RUO trains no model, uses a standard image codec and decodes in a few milliseconds. On all 1,610 VisDrone-DET test-dev images, RUO uses 42.4% fewer bits than a tuned threshold-based ROI coder, averaged over their shared tiny-object average precision (AP) range. RUO also needs fewer bits for tiny objects than the AV1 Image File Format (AVIF), High Efficiency Video Coding (HEVC) and three published learned codecs, and its advantage over threshold-based ROI coding persists when the sender and receiver use different detectors. For AP over all object sizes RUO needs 25.4% more bits than the tuned ROI coder, because its allocation drops large regions first at low rates, so it suits tasks that target tiny objects. We plan to release the code.

---


### 274. [Recoverability-Aware Evaluation of Diffusion Video Inpainting and Object Removal](https://arxiv.org/abs/2611.01578)

**<font color=#1a73e8>作者：</font>** Yanliang Qi, Jiacheng Ding, Cong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video inpainting for object removal is scored over the whole hole, although the background behind the object is visible in other frames of the shot for some hole pixels and in no frame for others. A whole-hole score therefore mixes copying with generation and cannot show which of the two a remover does well. To separate the two, we propose recoverability-stratified evaluation, in which a point tracker run on the clean video labels each hole pixel by whether and how far away it is observed, so that fidelity and temporal stability can be reported per stratum against a copy reference. To reuse the observed content, we also propose evidence-guided sampling (EGS), which blends tracked colors into the clean-latent prediction of a video diffusion remover without training. On DAVIS, the perceptual advantage of three diffusion removers over flow propagation shrinks where the content is visible a few frames away (LPIPS difference-in-differences +0.046 to +0.056 against E2FGVI-HQ), and real paired captures show the same pattern for two of them. Their DAVIS hole warping error is two to four times that of ProPainter, and copying along clean-video tracks lowers their recoverable LPIPS by a quarter to two fifths. EGS closes 43% and 56% of the gap to this copy reference on held-out DAVIS when its colors come from clean-video tracks. With colors tracked on the masked input, a pre-registered confirmation finds no gain on MiniMax-Remover and a loss on ROSE. Diffusion removers thus leave observed content unused on DAVIS, and training-free reuse does not yet hold with tracked evidence.

---


### 275. [Attack Patterns in Cross-chain Bridges: A Trust-based Empirical Analysis](https://arxiv.org/abs/2611.01587)

**<font color=#1a73e8>作者：</font>** Ishraq Samiha, Yasir Rahman, Rahma Mukta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid growth of multiple blockchain ecosystems has made cross-chain bridges essential for transferring assets and information across independent blockchains. Their multi-component architectures, cross-chain trust assumptions, and concentration of valuable assets expose them to diverse security threats. This paper presents an empirical study of cross-chain bridge attacks based on 48 evidence-supported real-world incidents from January 2022 to August 2026. We propose a behaviour-based attack pattern architecture comprising six trust-violation attack patterns, each defined by the primary trust assumption violated by the attacker: Proof Forgery,Logic Exploitation, Event Injection, Economic-State Manipulation, Credential Seizure, and Infrastructure Hijacking. The architecture further maps these patterns to five functional domains of cross-chain bridges: Deposit, Relay, Verification, Execution, and Governance and Operations, separating how a trust assumption is violated from where the compromised trust boundary lies. The 48 incidents correspond to $2.676 billion in gross bridge-specific losses, with the ten largest incidents accounting for 92.4% of total losses. Measured on the primary loss basis, Proof Forgery and Credential Seizure make up 86.2% of all losses, and the Verification and Governance and Operations domains hold 93.9%. A handful of very large incidents drives this concentration, yet it still holds when we switch to other loss bases or reclassify the boundary cases. By tying what attackers do to the bridge functions and security assumptions they target, the architecture gives threat modelling for cross-chain bridges an empirical footing.

---


### 276. [Autoencoder Based Deep Clustering of Point Clouds](https://arxiv.org/abs/2611.01594)

**<font color=#1a73e8>作者：</font>** Nader Alfares, Guangmingmei Yang, David J. Miller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by a problem in Generative Specification-Producing AIs (SPAIs), we focus on a problem of deep clustering of three-dimensional shapes specified by point clouds. After reviewing clustering and deep clustering, we study the fully unsupervised pipeline in which a FoldingNet autoencoder is first trained for reconstruction and then K-means++ is then applied to the resulting codewords. We report clustering accuracy (ACC), normalized mutual information (NMI) and adjusted Rand index (ARI) on ModelNet10 and ModelNet40 datasets, as a function of the number of clusters K. We also provide t-SNE visualizations of the codewords, and discuss the choice of K.

---


### 277. [Accurate automated photo-identification of Near Eastern and European fire salamanders](https://arxiv.org/abs/2611.01601)

**<font color=#1a73e8>作者：</font>** Maayan Yesharim, Hava Goldstein, Gabi Kolodny 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photo-identification underpins non-invasive capture-recapture monitoring of amphibians, but manual identification becomes slow and error-prone as reference libraries grow. Focusing on the Near Eastern fire salamander (Salamandra infraimmaculata), we developed a pipeline based on zero-shot local-feature matching (SuperPoint and LightGlue) without species-specific training and evaluated it on $2{,}440$ field photographs from Haifa and Tel Dan in northern Israel. We isolated the yellow spot pattern, scored image similarity by the number of high-confidence keypoint matches, which reduced a confound whereby many-spotted individuals accumulate spurious matches, and assigned identities across the database by two-tier clustering. Pipeline-assisted expert review corrected misidentifications, reducing the number of identities by almost a quarter. On held-out individuals, the pipeline ranked the correct individual first for $95.2\%$ of queries and recovered identities with an ARI of $0.958$. Without modification, it reached $95.1\%$ and $91.7\%$ top-1 accuracy on two datasets of the European fire salamander (Salamandra salamandra) and recognised $93.7\%$ of recaptures in one of them, compared with $38$-$77\%$ for five established programs and $93.9\%$ for visual inspection. Zero-shot local-feature matching thus offers amphibian monitoring a re-identification tool that needs no training data, transfers between related species, scales to databases of over a thousand individuals, and can audit existing databases before capture-recapture analysis.

---


### 278. [DyRadio: Spatiotemporal Diffusion for Dynamic Radio Map Reconstruction](https://arxiv.org/abs/2611.01603)

**<font color=#1a73e8>作者：</font>** Zhijie Fan, Zhifeng Zhao, Rongpeng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate radio map (RM) reconstruction is essential for environment-aware wireless networks. Sampling-based methods, which infer radio conditions from sparse measurements, are widely adopted because they do not require explicit knowledge of transmitter configurations. However, in dynamic environments, time-varying propagation conditions cause RMs to evolve, complicating reconstruction from temporally distributed sparse observations. Although cross-frame observations provide complementary spatial information, their direct aggregation can introduce temporal state mismatch. Furthermore, unknown measurement noise adds to the reconstruction difficulties. To address these challenges, we propose DyRadio, a framework that integrates spatiotemporal RM reconstruction with unknown noise estimation. Specifically, a propagation-prior-guided, noise-conditioned spatiotemporal diffusion model (DM) jointly reconstructs consecutive RMs by capturing cross-frame dependencies, while adapting to measurement noise levels. To estimate the noise level, an iterative predictive likelihood method alternates between DM-based blind-area prediction and noise-level updates. The estimated noise level then conditions reconstruction of the complete RM sequence. Experimental results demonstrate superior reconstruction accuracy and robustness against measurement noise, with peak signal-to-noise ratio (PSNR) improvements of 1.18-5.75 dB over the best-performing baseline across all evaluated settings.

---


### 279. [MedNet and U$^2$-ViT: A Nested Vision Transformer Diffusion Framework for Diverse Medical Images Generation](https://arxiv.org/abs/2611.01605)

**<font color=#1a73e8>作者：</font>** Lakshmikar R. Polamreddy, Jialu Li, Youshan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The scarcity of diverse, high-quality medical images remains a significant bottleneck in advancing AI-driven medical diagnostics and treatment planning. Traditional datasets often suffer from class imbalances, limited disease coverage, and insufficient variations in imaging conditions - challenges that hinder the development of robust, generalizable models. To address this, we introduce MedNet, a large-scale, multi-modal text-to-image dataset spanning 61 disease categories with 160 classes, covering both humans and animals. We built this with images from trusted public repositories, ensuring data diversity, quality, and ethical compliance. Additionally, we propose U$^2$-ViT, a novel diffusion-based text-to-image generation architecture arranging Vision Transformers (ViTs) in a nested U-Net structure to enhance the generation of diverse, and high-fidelity medical images. Through extensive experiments, we demonstrate that our model achieves the best Fr'echet Inception Distance (FID) score compared to state-of-the-art models. The source code is available at this https URL.

---


### 280. [NatureFusion: Rethinking Infrared and Visible Image Fusion as Natural Complementary Enhancement](https://arxiv.org/abs/2611.01607)

**<font color=#1a73e8>作者：</font>** Jianfeng Ding, Linfeng Tang, Hao Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the absence of ground truth, most existing infrared and visible image fusion methods pursue fidelity to the source images and directly superimpose two physically distinct modalities. As a result, salient infrared targets appear as bright patches of thermal radiation pasted onto the scene. These patches obscure the original color and texture of the targets, so the fused images look unnatural to human observers and deviate from the data distribution learned by vision models pretrained on visible images. Therefore, we redefine infrared and visible image fusion as natural complementary enhancement rather than source fidelity, and propose NatureFusion, which exploits cross-modal complementary cues to infer a clear and natural visible-style image from low-quality visible and infrared image pairs. Specifically, to address the lack of ground truth, we employ a generative foundation model as the teacher to directly generate visually natural fused images for supervision. Furthermore, to fully distill the teacher's generative capability while reducing computational cost, we fine-tune a pretrained generative model with conditional flow matching through a light-weight fusion adapter. Last but not least, to further improve downstream performance without sacrificing natural appearance, we freeze the fusion adapter and introduce a detector-supervised task adapter that strengthens the complementary contribution of infrared. Extensive comparisons with seven multi-modal fusion and seven single-modality enhancement methods demonstrate that NatureFusion generates visually natural fused images with the best perceptual quality. Detection and segmentation models pretrained on visible images achieve substantially higher accuracy on our fused images than on those of any competing method.

---


### 281. [Halal-NeSyNet: Clause-Scoped Neuro-Symbolic Cross-Attention for Automated Food Ingredient Auditing and Risk-Aware Halal Logistics Triage](https://arxiv.org/abs/2611.01612)

**<font color=#1a73e8>作者：</font>** Mochamad Rizal Fauzan, Naila Nursyifa, Irgi Surya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verifying that a packaged food is Halal requires reading ingredient declarations and E-number additives before goods enter certified warehouses. Dual-origin additives such as E471, E422, E441 and E920 are Mushbooh (doubtful) unless a botanical, microbial or certified-Halal qualifier appears in the same ingredient clause, so a plant-based qualifier on one clause must not clear an unqualified additive in another. We call a failure to respect this scope cross-clause modifier confounding and build a benchmark of 3,199 items (277 Open Food Facts records and 2,922 template-generated clause-swap items, labelled by an explicit 50-code rule base rather than by a certification authority) with a 540-item counterfactual suite. We propose Halal-NeSyNet, which couples a DistilBERT encoder with a 16-dimensional rule-derived symbolic vector through cross-attention and gated fusion, trained with an asymmetric false-Halal risk loss. Over five seeds, text-only TF-IDF baselines reach 86.25-86.71 % accuracy with 13.42-21.73 % false-Halal leakage and 6.33-26.00 % counterfactual triad consistency, whereas Halal-NeSyNet reaches 97.04+/-0.34 % and 99.67+/-0.50 %. Gradient boosting given the same symbolic vector reaches 96.25+/-1.24 % (+0.59 points from Halal-NeSyNet, 95 % CI [-1.11, +2.28]), so most of the gain comes from clause-scoped symbolic features and not from the network, and the risk loss did not help. Holding out whole template families, text-only models fall to 61.91-78.35 %, Halal-NeSyNet to 90.87+/-11.76 % and logistic regression with the symbolic vector to 91.11+/-2.88 %, with far more spread for Halal-NeSyNet. A three-lane receiving simulation auto-clears 49.33 % of cargo at 0.76 % green-lane contamination. Because labels and features come from one rule engine and 91.3 % of the items are templated, the results measure fidelity to a rule policy, not religious certification.

---


### 282. [Sonny-ENS: demystifying machine-learning ensemble weather forecasting](https://arxiv.org/abs/2611.01614)

**<font color=#1a73e8>作者：</font>** Minjong Cheon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every weather forecast is uncertain, and decisions from flood warnings to energy trading depend on how well that uncertainty is quantified. Machine-learning (ML) ensembles now quantify it better than the best physics-based ensemble, yet two things about them remain opaque: whether their skill requires hundreds to thousands of accelerator-days of training, and how a network with a simple source of randomness produces a spread that follows the flow. Here we introduce Sonny-ENS, an ensemble of three 68.9-million-parameter networks with Monte Carlo dropout, trained on the continuous ranked probability score (CRPS) in 2.7 A40 GPU-days. On 2022, it has a lower CRPS than the European Centre for Medium-Range Weather Forecasts ensemble (ENS) on 96% of 570 targets and an 8.3% lower mean CRPS at lead times of 1-10 days. It outperforms the operational GenCast on 69% of the targets, and a 51-member, 15-day forecast takes 69 s on one GPU. Ablations identify the ingredients of this skill, and a Kolmogorov-Arnold sparse autoencoder shows that dropout injects uncertainty mainly in the tropics, whereas the spread grows where the atmosphere is baroclinically unstable (spatial correlation 0.91 with the Eady growth rate). Skillful probabilistic weather forecasts are therefore within reach of a single GPU server.

---


### 283. [FinForesight: A Diagnostic Backtesting Benchmark for Deep Research Systems in Financial Forecasting](https://arxiv.org/abs/2611.01621)

**<font color=#1a73e8>作者：</font>** Fengyuan Liu, Mukai Li, Jieshun You 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Anticipating financial outcomes requires synthesizing evolving evidence and reasoning under uncertainty, making deep research systems promising tools for forecasting. Yet evaluating forecasting ability is challenging because historical backtests may reward memorized outcomes or information retrieved after the forecast date. Live forecasting avoids direct access to realized outcomes, but feedback arrives only after events resolve. To obtain timely feedback and assess historical scores, we introduce FinForesight, a diagnostic backtesting benchmark for financial deep research systems. Across the Chinese, U.S., and Hong Kong markets, the benchmark evaluates four forecasting tasks: valuation, return ranking, event direction, and future financial fundamentals. Two capability diagnostic tasks assess counterfactual reasoning and financial calculation, scored separately from forecasting performance. Our harness-compatible framework restricts retrieved evidence to information available at the forecast date. We compare pretraining-era, resolved post-cutoff, and live evaluations to test whether controlled backtests approximate future performance. Pretraining-era scores exceed post-cutoff scores in most temporal comparisons, and stronger retrieval controls narrow the gap between post-cutoff backtests and live results. Forecasting attribution and robustness analyses reveal how scores respond to retrieval policy and how predictions respond to prompt rewrites and numerical perturbations. The code and benchmark data are publicly available.

---


### 284. [Special and General Computational Aesthetics](https://arxiv.org/abs/2611.01626)

**<font color=#1a73e8>作者：</font>** Ganqing Luo, Chuan Li, Liaoruxing Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computational aesthetics is a field at the intersection of computer science, artificial intelligence, aesthetics, and other disciplines. As AI has developed, the field has formed relations of inclusion, intersection, or support with computational art, AI art, AI aesthetics, AI-generated content (AIGC), computational creativity, affective computing, and neuroaesthetics. Without distinguishing scope, objectives, and methods, it may be narrowed to image aesthetic quality assessment or expanded into an umbrella term for AI's involvement in art.
We analyze its internal structure and its relations with neighboring concepts, and propose a two-level scope: special computational aesthetics (SCA) and general computational aesthetics (GCA). SCA centers on aesthetic measurement and aesthetic process modeling. The former primarily corresponds to "Aesthetic Perception": computationally identifying and representing aesthetic attributes and predicting human aesthetic evaluations; the latter primarily to "Aesthetic Understanding": computationally describing, testing, and explaining how human aesthetic perception and judgment are formed. GCA extends this core to include "Aesthetic Generation," namely artistic generation guided by computational aesthetic models. Some computational aesthetic tasks can also use non-AI methods. Research in this scope using AI algorithms and models we define as AI aesthetics, which may involve the special core and the general extension. "Aesthetic Generation" intersects with AIGC, AI art, and computational creativity, but belongs to the general extension defined here only when computational aesthetic models substantively constrain, guide, or optimize artwork generation. We also draw on Feng Peng's discussion of the computability of beauty, aesthetic experience, and art as a theoretical reference for clarifying boundaries between computational aesthetics and related concepts.

---


### 285. [EgoMo3R: Joint Egocentric Motion and Scene Reconstruction](https://arxiv.org/abs/2611.01627)

**<font color=#1a73e8>作者：</font>** Chaitanya Patel, Yusuke Kato, Rin Takahira 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding holistic 3D human motion and the surrounding environment from egocentric video is fundamental for applications in AR/VR and robotics. Although these tasks are inherently coupled, existing methods treat them separately. In particular, egocentric motion reconstruction methods typically assume access to metric, gravity-aligned camera trajectories from specialized inertial sensors. Recovering such trajectories from monocular egocentric video remains a significant challenge due to rapid head movements and motion blur. We present EgoMo3R, a joint optimization framework that simultaneously reconstructs 3D human motion and scene geometry from casual egocentric video. It leverages the robustness of low-level visuo-geometric primitives, including monocular depth, optical flow, and point tracks, integrated with a diffusion-based human motion prior via first-order optimization. We propose an alternating optimization scheme that establishes a synergistic feedback loop: scene reconstruction provides physical grounding and trajectory conditioning for the motion prior, while the motion prior regularizes the camera trajectory and anchors the scene in a metric, gravity-aligned world frame. We evaluate EgoMo3R on the highly dynamic sequences of the EgoExo4D and Nymeria datasets and show that it outperforms specialized baselines in both 3D scene reconstruction and egocentric motion estimation.

---


### 286. [UA-Depth: Uncertainty-Aware Depth Restoration for Material-Agnostic Object Manipulation](https://arxiv.org/abs/2611.01645)

**<font color=#1a73e8>作者：</font>** Rui Cao, Jia-Hui Pan, Yin Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic manipulation requires accurate metric depth, yet commodity RGB-D cameras often fail on non-Lambertian objects such as transparent, reflective, and translucent materials, producing holes, structured noise, and biased depth. Most restoration methods produce only a single depth map, treating noisy and reliable regions uniformly for downstream tasks while ignoring regional uncertainty. We present UA-Depth, an uncertainty-aware depth restoration framework that iteratively co-refines depth and pixel-wise uncertainty, and uses uncertainty-gated features to suppress unreliable cues for stable updates. To strengthen zero-shot behavior, UA-Depth leverages a frozen depth foundation model as a prior to initialize missing or unreliable depth, and applies two-stage MAD-weighted log-depth scale normalization to reduce outlier bias in relative-to-metric alignment. We introduce an eight-dataset zero-shot benchmark across diverse scenes, materials, and sensors. Across these benchmarks, UA-Depth achieves the best mean rank among representative baselines, with particularly strong gains on datasets dominated by transparent and reflective objects. Beyond depth metrics, we demonstrate downstream improvements in category-level 6D pose estimation and 6D grasp synthesis by exploiting the predicted uncertainty. \emph{Code, models, and data for training and evaluation will be released upon publication.}

---


### 287. [Yielding Fairness: Coupled Learning and Fairness for Value-Weighted Ranking](https://arxiv.org/abs/2611.01647)

**<font color=#1a73e8>作者：</font>** Ami Tavory, Yaniv Sheena, Shaked Bar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Risk screening and recommendation systems pass or block accounts that generate both value and loss. Under a blocked-value budget, a cap on expected value forgone through blocking, the optimal ranking orders accounts by expected value per unit expected loss, a ratio of conditional expectations. This rule can conflict with accepted harm or net-harm criteria, blocking accounts that another criterion would pass at the same budget. We call these cases account-level objections and define group complaint disparity as the difference between groups' normalized realized objections.
Weighted binary cross-entropy (W-BCE) implements the value-per-loss order with one score. Objection penalties modify the ranking, while group multipliers scale those penalties differently by group, tracing tradeoffs between loss capture and complaint disparity. This preserves the value-budgeted ranking structure and makes the cost of reducing contestable blocks explicit.
Across public recommendation, insurance, credit, and mortgage datasets, we compare undamped W-BCE with ordinary BCE using yield Gini, an area summary of loss capture versus blocked value. Logarithmic weight damping is evaluated separately. Held-out evaluations measure capture-disparity tradeoffs. Validation-selected group-aware complaint penalties improve complaint closure in some cohorts. A corrected comparison normalizes and enlarges candidate policy banks using validation-only price sweeps and retains all ten applicable sources. The source-level results do not establish a statistically significant average advantage over group-blind pricing at the fixed minimum retained loss capture. We also compare with blocked-count, blocked-value, and protected-loss parity postprocessors, which do not directly constrain realized objections, and measure objections in candidate-count and loss units.

---


### 288. [Near-Optimal $\sqrt{K}$-Regret for Online Learning in Uninformed Markov Games](https://arxiv.org/abs/2611.01649)

**<font color=#1a73e8>作者：</font>** Junyan Liu, Haipeng Luo, Lillian J. Ratliff 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online learning in two-player uninformed Markov games, where the opponent may follow an arbitrary, unknown policy in each episode and the learner does not observe the opponent's actions. [TWYS21] showed that achieving sublinear external regret requires an exponential dependence on the episode length $H$. Motivated by this limitation, they studied the weaker notion of Nash-value regret and obtained an $\widetilde{O}(K^{2/3})$ regret bound, where $K$ is the number of episodes. More recently, [LLZR26] introduced a stronger notion called empirical Nash-value regret and achieved an $\widetilde{O}(\sqrt{K})$ bound when the opponent's non-stationarity is moderate, including the case where the opponent follows a fixed policy. However, whether the $\sqrt{K}$ rate is achievable in the worst case remained open.
In this paper, we resolve this open question by developing an algorithm that achieves $\widetilde{O}(H^{3/2}S\sqrt{AK})$ empirical Nash-value regret against arbitrary opponent policies, where $S$ is the number of states and $A$ is the number of learner's actions. Specifically, our algorithm combines global and local planning by maintaining a collection of candidate predictions of future losses, each associated with a policy. Global planning learns which candidates to favor across episodes, while local planning combines their policies differently at each state to make decisions. A key ingredient is to coordinate these two components to control the discrepancy between local loss estimates and the total loss of the executed policy, using only the learner's observed trajectories.

---


### 289. [Physics-Informed One-Step Generation on Long-short flow maps](https://arxiv.org/abs/2611.01651)

**<font color=#1a73e8>作者：</font>** Zhiqi Li, Duowen Chen, Jinjin He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed generative models should produce samples that are both data-aligned and physically valid, yet existing methods are often iterative and too slow for practical use. Achieving this with a one-step flow-map model is difficult because both data-distribution and physics-constraint learning are enforced only indirectly through surrogate objectives, making their joint learning fragile for long-range flow maps. We propose \textbf{Physics-Informed Long-Short Flow Maps with Direct Guidance (LSFM-DG)}, which makes direct target computation feasible by decomposing one-step generation into a long flow map for global evolution and a near-terminal short flow map with computable closed-form solutions and physics potentials. As the short flow map shrinks to zero, it provides both direct distributional and physical targets for learning the long flow map. This yields a unified one-step flow-map model that removes Jensen's gap, improves training stability, and achieves stronger data fidelity and physical consistency without distillation.

---


### 290. [A Hybrid Anomaly Detection Method for Electric Vehicle Identification from Smart Meter Recordings](https://arxiv.org/abs/2611.01655)

**<font color=#1a73e8>作者：</font>** Ali Babalhavaeji, Hui Song, Mohammadreza Radmanesh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, electric vehicles (EVs) have attracted much attention due to their potential to decarbonize the transport system. EV charging imposes challenges on power grids, such as load imbalance and voltage instability. Therefore, electricity distributors need to identify which users have an EV. Smart meter recordings can be effectively used for this purpose. The major issue associated with such data is the imbalance problem, where the majority of the data belongs to users without EVs. The existing methods for EV identification from smart meter recordings have framed it as a classification task. In this paper, we frame the problem as an unsupervised problem and propose a hybrid anomaly detection method that combines the power of prediction-based and reconstruction-based anomaly detection methods. The proposed model considers temporal and stochastic representation information of smart meter time series via prediction-based and reconstruction-based components, respectively. The performance of the proposed model is compared with state-of-the-art supervised and unsupervised methods. Its superiority is verified on real-world data.

---


### 291. [A Hybrid Anomaly Detection Method for Multivariate Time Series](https://arxiv.org/abs/2611.01661)

**<font color=#1a73e8>作者：</font>** Ali Babalhavaeji, Hui Song, Mahdi Jalili  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series are ubiquitous in monitoring smart systems such as power plants, smart houses, and servers. These systems use multiple sensors to collect the system's status over time. Those sensors represent the status of the whole system as one entity. Anomaly detection in such smart systems is of critical importance to prevent system failure and maintain functionality. But anomaly detection in such multivariate time series data is very challenging since this type of data includes both temporal and spatial information. Capturing both of these pieces of information is important to detect anomalies. In this paper, we propose a hybrid deep learning-based anomaly detection method, which captures both temporal and spatial information. We propose to take advantage of the feature extraction capabilities of 2d convolutional network in a variational autoencoder, alongside a prediction-based deep neural network of 2d convolutional networks and a gated recurrent unit network to capture both spatial and temporal information. Experiments on public data against state-of-the-art show the potential of our method.

---


### 292. [Stand-In Effects and Pooling Amplification: Design-Based Tests of Whether Biological World Models Use Actions](https://arxiv.org/abs/2611.01666)

**<font color=#1a73e8>作者：</font>** Bowen Xu, Boyu Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Action-conditioned world models are increasingly trained on data from randomized experiments, and whether their predictions respond to actions is usually checked by replacing or removing the actions and measuring the loss in accuracy. We show that such diagnostics report action effects where there are none: under autocorrelated designs, future actions stand in for history the model does not see, and a better model learns the stand-in better. When the design law is known, a conditional randomization test written as an e-value is valid in finite samples whatever the model, provided the resampler conditions on the full state the design used; resampling from a simpler law reproduces the false effect. We identify a second failure, specific to world models: when many sites share one action sequence (cells in a microscope field, pixels in a frame), the natural pooled score turns small model errors along the action contrast into overwhelming evidence against a true effect. In a pixel world, its median log e-value fell from $-17.3$ to $-6832$ as frames grew from 64 to 4096 pixels, while the oracle's rose. Tempering the score by a design effect estimated on training data changes the bet, not the validity. Our own preregistered analysis of optogenetic ERK experiments failed in exactly this way; a tempered statistic, selected on synthetic data and registered before the data were obtained, then rejected the null on a never-opened field ($E\approx 1.1\times10^{10}$). Every analysis is preregistered, fixed in a dated protocol before it was run, or labelled exploratory, and every reported result is generated from hashed result files.

---


### 293. [Wave Physics as Representation: Tensor-Structured Neural Reconstruction for Ocean Acoustic Fields](https://arxiv.org/abs/2611.01680)

**<font color=#1a73e8>作者：</font>** Yifan Sun, Panqi Chen, Weifeng Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing three-dimensional (3D) complex ocean acoustic fields from sparse measurements is challenging due to highly oscillatory wave structures and restricted sensing patterns/routes. Learning-based approaches fall into two categories. First, purely data-driven models can learn complex field patterns, but do not explicitly exploit wave physics that may enhance interpretability and reduce training costs. Second, physics-informed methods impose a specified physical equation as a reconstruction constraint, but often require environment-dependent parameters that are difficult to acquire. As a result, practical 3D acoustic field reconstruction that is both physically grounded and robust to uncertain environmental information remains largely unexplored. This work takes an alternative route: instead of solving a fully specified wave equation, it extracts a structured representation from wave physics and learns its components from data. From the Helmholtz equation and normal mode propagation, we derive a structured spatial-angular tensor representation, termed the S/c representation. Under a low-rank specialization, it takes the form of a rank-(L,L,1) block-term tensor decomposition, which connects structured sampling patterns/routes used in ocean sensing to sufficient conditions for field recovery. Building on this tensor representation, we propose TIDAL, a neural reconstructor that uses the S/c representation as an inductive bias for structured decoding and aligns information aggregation with the sampling geometry. The neural learner removes the need for known model parameters required by conventional physics-based recovery methods. Experiments across three structured sampling geometries show that TIDAL achieves the best reconstruction performance and fastest inference among baselines, with benefits from the physics-derived representation under limited data and model capacity.

---


### 294. [Leveraging 2D Foundation Priors for Generalized Category Discovery under Test-Time Adaptation in 3D LiDAR Segmentation](https://arxiv.org/abs/2611.01682)

**<font color=#1a73e8>作者：</font>** Hanqi Chen, Chaoqi Chen, Tian Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In autonomous driving, 3D LiDAR semantic segmentation is expected to adapt to evolving environments and recognize previously unseen categories, making generalized category discovery under test-time adaptation (GCD-TTA) an important problem. However, existing works treat GCD and TTA separately, while the limited semantic information in 3D point clouds makes GCD-TTA under domain shift more prone to feature collapse when combining GCD with TTA. To address this issue, we propose a two-stage framework for GCD-TTA in 3D LiDAR semantic segmentation. Specifically, in the first stage, we adaptively aggregate local 3D features according to geometric density variations and obtain reliable pseudo labels under a global class-wise prototype consistency constraint. In the second stage, we cast category discovery as an optimal transport assignment process for globally consistent grouping of novel categories. Meanwhile, semantic features from 2D vision foundation models are fused with 3D point cloud features to enrich 3D semantic information and promote a more separable feature space. Extensive experiments on Synth4D to SemanticKITTI, SynLiDAR to SemanticKITTI, and Synth4D to nuScenes demonstrate the effectiveness of our framework. Under a unified evaluation protocol, our method achieves the best overall mIoU on 9 out of 10 benchmark splits and improves the overall mIoU by up to 12.21 points over the strongest re-implemented baseline.

---


### 295. [SEALECT: Scene-Conditioned Pose Priors for Plausible Maritime Vessel Retrieval](https://arxiv.org/abs/2611.01688)

**<font color=#1a73e8>作者：</font>** Faisal Mohammad, Mohamed Younis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address scene-conditioned object retrieval for compositional augmentation in maritime imagery, where strong geometric constraints make appearance-only retrieval produce physically implausible vessel insertions. We propose SEALECT, a retrieval framework that jointly models visual compatibility, vessel pose, scale, and scene geometry through a unified score combining neural similarity, scene-conditioned pose priors, and observed-pose consistency. We construct a maritime scene-pose library and model the pose and scale priors nonparametrically, as a kernel that conditions each prior continuously on the scene with no learned parameters. Across seven maritime benchmarks, our trained scene-conditioned retriever exceeds the strongest appearance encoder (SigLIP 2) in recall (+0.14), and the training-free prior raises geometric plausibility further at negligible recall cost, more than halving the constraint violations of appearance retrieval and outperforming learned foreground-search baselines (GALA-style, DiscoFOS). In a blind study of end-to-end composites (BootPlace placement, DiffHarmony harmonization), SEALECT ranks first among six methods, ahead of random and GALA-style selection and statistically tied with CLIP, DiscoFOS, and DINO.

---


### 296. [Direct Covariance-to-Beamformer Mapping for Low-Latency Hybrid ISAC Beamforming with Subsequent DoA Estimation](https://arxiv.org/abs/2611.01694)

**<font color=#1a73e8>作者：</font>** Anjali K.S., Manoj Kumar Panda, Chandramani Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrated sensing and communication (ISAC) systems typically employ a two-stage beamforming pipeline, in which target directions are first estimated from the received covariance matrix and then used to compute the beamforming weights by solving non-convex optimization problems. Although effective, this approach introduces processing latency that can limit beam adaptation in dynamic environments. This letter proposes a beamforming deep neural network (BFDNN) for direct covariance-to-beamformer learning in ISAC systems. BFDNN is a compact regression network that maps covariance-matrix features directly to the hybrid beamforming weights produced by a hybrid ISAC beamformer, eliminating the direction-of-arrival (DoA) estimation stage during inference. Compared with MUSIC, classification-DNN, and regression-DNN based beamforming pipelines, BFDNN generates comparable beam patterns and higher effective spectral efficiencies while reducing the beamforming prediction latency by 25-30 times on the evaluated platform, demonstrating the potential of direct covariance-to-beamformer learning for low-latency ISAC beam updates. Moreover, the target directions can be inferred indirectly from the generated radiation pattern, yielding DoA accuracy competitive with that of dedicated learning-based methods in the evaluated scenario.

---


### 297. [Restoring Semantic Fidelity for Training-Free High-Resolution Image Generation in Diffusion Transformers](https://arxiv.org/abs/2611.01696)

**<font color=#1a73e8>作者：</font>** Junjie Li, Zengbin Wang, Gaoxiang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformer (DiT)-based text-to-image models have recently achieved remarkable success in image synthesis. However, when directly applied beyond their training resolution, these models often suffer from severe semantic degradation, where meaningful semantic content disappears. Although existing training-free high-resolution generation methods can mitigate this issue, the inherent semantic degradation at high resolutions remains largely unresolved, leading to degraded fine-grained details. Furthermore, widely used structural guidance methods lack modeling of the structure and details in the intermediate trajectory, which degrades the quality of the generated results. In this paper, we propose a training-free framework for high-resolution image generation to address these challenges. First, we propose a text-visual scale-decoupled attention (TVSDA) module, which restores the model's ability to generate semantically meaningful content at high resolutions by preserving the global receptive field of text tokens while aligning the receptive field of image tokens with the training resolution. Second, we propose a structure-detail guidance (SDG) strategy that explicitly models structural information and fine details through scale-wise and temporal-wise guidance, overcoming the limitations of conventional low-resolution guidance. Extensive experiments demonstrate that our method significantly improves both structural coherence and detail fidelity over existing training-free DiT-based high-resolution generation approaches. The code is available at this https URL.

---


### 298. [SparseLift: Automatically Optimizing Opaque Sparse Paths in Industrial-Scale Recommendation Model Training](https://arxiv.org/abs/2611.01702)

**<font color=#1a73e8>作者：</font>** Changqing Shi, Anan Liu, Genbao Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The sparse path, comprising sparse operations and collective communication, is a critical component of large-scale recommendation models. However, these operations are often represented as opaque nodes in the training computation graph, hindering whole-graph optimization. We present SparseLift, a low-overhead compiler for the sparse path of large-scale recommendation training. It exposes sparse computation and communication to whole-graph analysis to expand the optimization space and improve training efficiency. By analyzing model structure and runtime information, SparseLift reconstructs opaque nodes as analyzable subgraphs, recovering the resource semantics of sparse computation and communication within the graph. Building on the recovered semantics, we design incremental cost models and a constraint-aware planner to automatically select and organize subgraph optimizations into an execution plan that is reused during subsequent steady-state training. We evaluate SparseLift on an industrial video-platform recommendation task with 100B sparse parameters and the public DLRM benchmark. SparseLift improves steady-state throughput for ordinary industrial training steps by 16.5\% over the native baseline. On DLRM, it achieves $1.60\times$ and $1.26\times$ model-execution speedups over DLRM-Baseline and TorchRec, respectively.

---


### 299. [Fréchet Oral Distance: A Coordinate-Free Metric and Benchmark for Speech-Driven Oral Animation](https://arxiv.org/abs/2611.01705)

**<font color=#1a73e8>作者：</font>** Jaehong Myung, Seungho Eum, Hyunjung Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, speech-driven facial and oral animation technologies have been used in various fields such as education, speech therapy, and healthcare. But methods to objectively evaluate the quality of generated results are still limited. Accordingly, we propose the Fréchet Oral Distance (FOD), which uses embeddings from an Oral Motion Encoder (OME) and a TIMIT-Vis reference distribution. In experiments, FOD reproduced model rankings similar to the coordinate-based metric, Lip Vertex Error (LVE), and showed trends consistent with user preference. Our framework provides objective and reproducible benchmarking without relying on expensive equipment or subjective evaluation, and it can be extended to compare a variety of 2D/3D models.

---


### 300. [Comparative Strategies for Handling Imbalanced QSAR Regression: A Case Study on hERG Activity Prediction](https://arxiv.org/abs/2611.01709)

**<font color=#1a73e8>作者：</font>** Ming-Yen Sung, Hsin Liu, Tung-Sheng Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data imbalance frequently occurs in QSAR modeling, yet most studies focus on classification tasks, and few address regression tasks, as it is challenging to determine which regions of the data are sparse or dense. Data-level and algorithm-level imbalance-handling strategies can have different effects on model performance. In this study, we systematically compare various strategies across GCN and fingerprint-based machine learning models. To evaluate model performance more meaningfully, we partitioned the target region into several subregions based on both domain knowledge and data distribution. We focused on the region of greatest practical interest. Our results demonstrate that selecting models based on this interest-region metric leads to more reliable performance than using the total region metric. We also observed that different imbalance-handling strategies can have divergent effects depending on the model type. These findings highlight the importance of region-aware evaluation in regression QSAR modeling and provide practical guidance for selecting appropriate strategies for imbalanced datasets.

---


> [!TIP]
> 当前位于：**251-300**（第 6/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
