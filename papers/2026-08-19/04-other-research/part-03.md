# 📦 其他研究 | 2026年08月19日

> 本类共 **435** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

---

### 101. [Do Geometry-Aware Positional Encodings Help Transformers in Spatial Imperfect-Information Games?](https://arxiv.org/abs/2608.14982)

**<font color=#1a73e8>作者：</font>** Wenji Fu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers applied to spatial imperfect-information games must represent map geometry while tracking hidden entities through time. We ask whether geometry-aware positional encodings improve these capabilities, without claiming a new positional encoding. We construct a four-level benchmark on a hexagonal naval pursuit game: controlled geometry and topology probes, an exact-Bayes hidden-target tracking task, offline policy imitation at 1k and 10k games, and 7,200 fixed-seed games against three legacy opponents. Across matched Transformer backbones, HexRoPE reduces exact-belief posterior cross-entropy relative to no positional encoding by 0.278 on D6-transformed test orbits and 0.329 on a larger map; both hierarchical-bootstrap confidence intervals exclude zero, and both Holm-adjusted p-values are below 0.001. At 1k games, HexRoPE improves policy action accuracy by 4.63 percentage points over no encoding and 2.05 points over rectangular relative bias; the gains shrink to 1.55 and 0.41 points at 10k games. However, HexRoPE does not improve aggregate gameplay win rate: its paired effect over no encoding is -1.56 percentage points (95% CI [-4.50, 1.17]). Rectangular relative bias is strongest on D6 belief consistency but fails sharply when extrapolating from radius 3 to radius 4, while graph bias provides only a small blocked-edge gain. The results show that geometric inductive bias improves belief estimation and data-efficient imitation, but those representation gains do not automatically produce stronger closed-loop play.

---


### 102. [Registration-Free Hyperspectral Reconstruction from RGB via a Permutation-Invariant Gram-Matrix Principle](https://arxiv.org/abs/2608.14994)

**<font color=#1a73e8>作者：</font>** Jiangsan Zhao, Masayuki Hirafuji, Seishi Ninomiya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing a spatially and spectrally high-resolution hyperspectral image (HR-HSI) from a low-resolution HSI (LR-HSI) and a high-resolution RGB image (HR-RGB) usually assumes precise registration and a known camera response function (CRF). Both assumptions are difficult to satisfy with different sensors. We remove both through a permutation-invariant supervision principle: the Gram matrix of an unmixed abundance map depends on shared material composition but not on pixel ordering. Matching abundance Gram matrices therefore allows RGB-to-HSI mapping to be learned without spatial correspondence and without a predefined CRF. Under a full random permutation of HR-RGB pixels, a state-of-the-art fusion method collapses, whereas our reconstruction is unchanged after inverse reindexing for evaluation. Building on this principle, a residual spectral super-resolution function maps HR-RGB directly to HR-HSI without registration, known CRF, or paired supervision. Across indoor, natural-scene, and remote-sensing benchmarks, the method achieves accuracy comparable to approaches that require these assumptions while remaining robust when they are violated. Loss ablations further show that reconstruction accuracy is largely insensitive to the specific discrepancy used to match the Gram matrices, indicating that performance arises primarily from the permutation-invariant principle rather than loss tuning.

---


### 103. [DualMiT-Net: Local-Global Transformer-Convolutional Fusion for Breast Mass Segmentation in Mammographic Regions of Interest](https://arxiv.org/abs/2608.15019)

**<font color=#1a73e8>作者：</font>** Alibek Kamiluly, Milana Muratova, Yash Patel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast mass segmentation is an important step in computer-aided mammography, but it remains difficult because masses can have low contrast, irregular shapes, and boundaries that blend with surrounding breast tissue. To address this problem, we present DualMiT-Net, a dual-branch network that uses both a focused view of the mass and a wider view of the surrounding tissue. The local branch uses a Mix Transformer (MiT-B5) encoder to learn mass shape, texture, and boundary information, while the global branch uses an EfficientNet-B5 encoder to learn surrounding breast context. Features from the two branches are shared at the deeper encoder levels and are then progressively fused in a single decoder. A spatial gate controls how much global information is added during decoding. We also evaluated four input representations and selected a percentile-windowed mammogram combined with a Gabor texture response. The model was trained and evaluated on the mass subset of the Curated Breast Imaging Subset of the Digital Database for Screening Mammography (CBIS-DDSM) using a patient-level split. Across three training runs, DualMiT-Net with exponential moving average weights achieved a mean Dice coefficient of 0.9375 and a mean Intersection over Union of 0.8834. It also achieved better Dice and IoU scores than six standard encoder-decoder baselines trained using the same data and training settings. These results show that combining local mass information with wider breast context can provide accurate and consistent breast mass segmentation.

---


### 104. [Geometry-Calibrated Closed-Form Shrinkage for SAR Despeckling](https://arxiv.org/abs/2608.15028)

**<font color=#1a73e8>作者：</font>** Xuran Hu, Mingzhe Zhu, Djordje Stanković 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic aperture radar (SAR) despeckling is an inverse-recovery problem in which multiplicative non-Gaussian noise must be suppressed without erasing scattering structures. We revisit a nonlocal sparse estimator that applies a log--Yeo--Johnson transformation, stacks similar patches into groups, codes each group on its own left singular basis, and shrinks the resulting coefficients. Three quantities usually treated as tunable are shown to be fixed by this construction. First, the group dictionary is orthonormal, so the weighted Lasso admits an exact coefficient-wise soft-threshold solution: the iterative inner solver is unnecessary, and the two apparent weighting matrices are the numerator and denominator of a single threshold field rather than independent modules. Second, because the dictionary is estimated from the noisy group itself, its retained subspace absorbs speckle in proportion to the group aspect ratio $\gamma=p^2/K$; a random-matrix argument converts the corresponding regularization constant into a geometry-calibrated correction and collapses patch size, group size, and shrinkage scale into one analytically determined degree of freedom. Third, singular projection makes the coefficient noise nearly Gaussian at every tested look number, which locates the point at which an exact speckle likelihood ceases to be informative. The resulting estimator is deterministic, training-free, and applies one set of analytically determined settings to every image and sensor. It ranks first in 18 of 24 PSNR/SSIM comparisons against twelve published methods on three synthetic benchmarks, and attains the lowest mean deviation of the ratio image from the theoretical speckle model over six real-SAR configurations from five sensors. Code is available \href{this https URL}{here}.

---


### 105. [Generation of Synthetic Fingerphotos with GANs](https://arxiv.org/abs/2608.15029)

**<font color=#1a73e8>作者：</font>** Conor Miller-Lynch, Sandip Purnapatra, Syed Konain Abbas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contactless fingerprinting is an emerging approach to biometric authentication that allows users to scan their fingerprints without touching a scanner. Due to the limited amount of contactless fingerprint data available and the security risks associated with sharing real individuals' fingerprints, it is valuable to explore methods of generating synthetic data that can be used in place of - or in conjunction with - real data to develop and evaluate contactless fingerprinting systems. In this paper, we present and evaluate synthetic fingerphotos generated using StyleGAN2-ADA and StyleGAN3, existing image generation architectures. We evaluate the realism, privacy preservation, and variety of the synthetic fingerphotos by comparing their biometric feature statistics to those of real fingerphotos, computing match scores between real and synthetic fingerphotos, and computing match scores between different synthetic fingerphotos. This paper provides a quantitative comparison point for future evaluations of synthetic fingerphotos. The evaluation code is made available at this https URL.

---


### 106. [Tensor--Action Ko--Lee Cryptography: A Framework and Structural Cryptanalysis of Commuting Subgroup Constructions](https://arxiv.org/abs/2608.15030)

**<font color=#1a73e8>作者：</font>** Ziyan Chen, Yuqiao Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tensor isomorphism has been studied as an algebraic problem relevant to post-quantum cryptography, while its use in public-key encryption remains open. In this paper, we formulate a Ko--Lee-style framework for public-key encryption from cubic tensor actions and prove its formal correctness. We then show that the framework is generically insecure when the commuting matrix subgroups are given by public finite generating sets. Viewing a cubic tensor as a vector in a $d^3$-dimensional space, a linear decomposition attack recovers the shared tensor from the public transcript in polynomial time without recovering either secret action. We also cryptanalyze three natural commuting-subgroup constructions---field-extension, block-diagonal, and tensor-product constructions---and give toy-scale experiments illustrating their specific structural leakage. Finally, we examine the lower-dimensional leakage caused by scaled-block structure. The contribution is therefore a framework proposal together with its cryptanalysis; it does not provide a secure public-key encryption scheme.

---


### 107. [Lipschitz Bandits with Arbitrary Feedback Delays](https://arxiv.org/abs/2608.15036)

**<font color=#1a73e8>作者：</font>** Yuhao Liu, Yu Chen, Longbo Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Lipschitz bandit problem extends the traditional multi-armed bandit framework to continuous action spaces by assuming that the reward functions satisfy a Lipschitz condition. This work investigates Lipschitz bandits under arbitrary feedback delays, where reward signals are not received immediately upon taking an action but after an arbitrarily chosen delay. We consider both stochastic and adversarial reward settings, proposing an elimination-based algorithm and an EXP3-based algorithm, respectively. For both settings, our algorithms achieve a regret bound of $\tilde{O}\left(T^{\frac{d_z+1}{d_z+2}}+\sqrt{D}\right)$ over a time horizon $T$ with total delay $D$, where the main difference between settings lies in the definition of the zooming dimension $d_z$. Our bounds match existing delay-free regret guarantees for Lipschitz bandits and characterize the additional $\tilde{O}(\sqrt{D})$ impact introduced by feedback delays.

---


### 108. [SCOPE: Score-Isolated Agentic Optimization for Video World Models](https://arxiv.org/abs/2608.15043)

**<font color=#1a73e8>作者：</font>** Yuhua Jiang, Jiaming Wang, Qingbin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video world models are increasingly used as simulators for planning and embodied decision making, yet improving them at inference time introduces a subtle evaluation problem: prompts, samplers, verifiers, and selectors may evolve together, making it difficult to attribute gains or prevent held-out feedback from shaping the final policy. We introduce \scope (\emph{\scopefullname}), a framework for auditable inference-time adaptation of frozen video world models. \scope represents external controls as a typed state, updates this state only through bounded changes supported by development evidence, and freezes the resulting policy before held-out evaluation. On Physics-IQ benchmark, \scope improves over the exact frozen base by $+14.24$ (95\% CI $[+8.10,+21.23]$). Controlled ablations further identify gains from scene specification, sampling, and learned selection, while the margin over the strongest matched agentic baseline remains unresolved. Cross-backbone and prospective evaluations reveal a complementary result: useful inference-time updates exist, but their benefits do not transfer uniformly across models and settings. Together, these findings suggest that reliable inference-time adaptation requires not only better proposals, but also a principled mechanism for deciding which updates should become part of the deployed system. Code is available at this https URL.

---


### 109. [Beyond Overt Reactions: Analyzing Subtle User Emotional Response to Unexpected In-Vehicle System Behavior](https://arxiv.org/abs/2608.15048)

**<font color=#1a73e8>作者：</font>** Huy Quyen Ngo, Suresh Kumaar Jayaraman, Brian Mok 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Modern vehicles, with advanced AI voice and autonomous navigation features, extend beyond traditional driving but, like any autonomous system, can potentially make mistakes or behave in ways unexpected by users. Although providing real-time explanations can alleviate some confusion, constant information can overwhelm users and potentially cause unnecessary distractions. Some situations may require explanations or corrective vehicle behavior, and thus, recognizing user response to unexpected vehicle behavior is critical. To investigate such user responses, our study focused on collecting and analyzing user behavioral responses to unexpected events while interacting with a fully autonomous vehicle in a driving simulator. We also aimed to address the lack of datasets capturing subtle user responses (facial, spoken language, physiological signals) to in-vehicle events, as existing datasets primarily focus on strong emotional signals in conventional human-driven cars and user response to external road and traffic conditions. Users were exposed to stimuli designed to induce surprise, confusion, and frustration while performing a secondary task on a tablet and interacting with the vehicle through voice commands and in-vehicle displays. We collected a multi-modal dataset with video, audio, and heart rate data and gained insights into subtle user responses that underscored the need for further investigation of nuanced user behaviors. These observations highlight the importance of designing vehicles that recognize and adapt to occupants' behavior, potentially improving their experience.

---


### 110. [Online Convex Optimization with Dueling Feedback](https://arxiv.org/abs/2608.15050)

**<font color=#1a73e8>作者：</font>** Yiyang Lu, Hareshkumar Jadav, Mohammad Pedramfar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online convex optimization with dueling (pairwise comparison) feedback, where the learner observes only a binary preference between two queried points. While dueling feedback is well understood in discrete or stochastic settings, the adversarial convex setting has remained unexplored. We propose a simple reduction that converts dueling feedback into approximate gradients, enabling the use of standard first-order methods. We show that regret guarantees transfer under this reduction, yielding the first results for this setting, including $\mathcal{O}(T^{3/4})$ static, adaptive, and dynamic regret. Under additional structure, we obtain improved rates of $\mathcal{O}(T^{2/3})$ for smooth objectives and $\mathcal{O}(\sqrt{T \log T})$ for strongly convex functions.

---


### 111. [Andy: A Mathematical Agent for Rigorous Proof and Autonomous Research](https://arxiv.org/abs/2608.15052)

**<font color=#1a73e8>作者：</font>** Zi'an Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Andy is an autonomous mathematical research agent that solves and verifies submitted problems, formulates new research problems, and constructs rigorous proofs. It separates proof generation from correctness evaluation and supports knowledge acquisition, targeted revision, and multistage verification. This paper illustrates the workflow using a published result on self-triggered impulsive consensus as a starting point. Andy formulates a global exponential leader-follower synchronization problem for delayed heterogeneous networks with switching communication topologies. The proposed hybrid control combines self-triggered impulses with execution delay and recovery-phase continuous feedback. After each delayed impulse, this feedback cancels the delayed error channel during a recovery window. Sufficient conditions for global exponential synchronization are established, and Zeno behavior is excluded for both the sampling and impulse sequences. A numerical example confirms the result. This case demonstrates Andy's ability to learn from existing results, formulate meaningful research problems, and develop and verify rigorous proofs.

---


### 112. [Frequency and Edge-Guided Segment Anything Model for Remote Sensing Image Semantic Segmentation](https://arxiv.org/abs/2608.15054)

**<font color=#1a73e8>作者：</font>** Feng Gao, Zizhe Pan, Haoting Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing image semantic segmentation (RSISS) has attracted significant attention due to the growing demand for fine-grained land cover information. The Segment Anything Model (SAM), proposed as a foundation vision model, offers strong segmentation performance and generalization capabilities for RSISS tasks. However, existing SAM-based approaches face two limitations: (1) Insufficient adaptation of SAM's features to the diverse characteristics of land cover types. (2) Semantic ambiguity at object boundaries, which hinders accurate delineation. To address these limitations, we propose Frequency and Edge-guided SAM (FE-SAM), a scalable and efficient framework for RSISS. Specifically, we introduce a Frequency-Modulated Adapter (FMA) that adaptively decomposes and modulates frequency-domain features based on the input data. It selectively enhances informative high- and low-frequency components corresponding to different land cover types. Furthermore, to improve SAM's ability to capture fine-grained details, we design EGRefiner, which integrates multi-scale edge-enhanced information extracted from the input image. Extensive experiments on three benchmark datasets demonstrate that FE-SAM outperforms state-of-the-art methods. The source codes are available at: this https URL.

---


### 113. [EgoTac: In-the-wild Tactile Prediction from Egocentric Vision](https://arxiv.org/abs/2608.15060)

**<font color=#1a73e8>作者：</font>** Wenkang Zhang, Chengbo Yuan, Zicheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Touch is fundamental to dexterous manipulation, yet most egocentric human data increasingly used for robot learning lacks tactile information. Directly collecting large-scale tactile data is challenging due to sensor limitations, while human video data is abundant, contact-rich, and easily scalable. This motivates a natural question: can tactile signals be inferred purely from vision? To address this, we introduce EgoTac, a generalizable model that predicts rich tactile information directly from egocentric human videos. EgoTac is trained on a unified corpus of over 5.7M image-tactile pairs, covering both continuous force measurements and binary contacts. By learning from this diverse dataset, EgoTac captures nuanced touch dynamics across varied interactions. Experiments demonstrate strong performance: in-domain prediction achieves an average force error below 0.06N. On out-of-domain contact prediction benchmarks, EgoTac consistently outperforms the state-of-the-art contact estimator. It also captures the rise and fall patterns of real tactile data and enables zero-shot predictions on unconstrained real-world videos. Scaling analyses further reveal that both data diversity and volume improve performance steadily. Overall, EgoTac provides a scalable pathway to extract tactile priors from egocentric human videos, enabling broadly applicable tactile-aware robot learning.

---


### 114. [LongDocBench: Benchmarking TOC Hierarchy and Contextual Relationship Recovery in Long Documents](https://arxiv.org/abs/2608.15064)

**<font color=#1a73e8>作者：</font>** Yuefeng Zou, Yichen Lu, Jingxiao Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parsing visual documents into machine-readable representations is fundamental to document intelligence. Existing benchmarks focus on page-level element recognition, reading order, formula recognition, and table structure. Long documents, however, also require document-level structure recovery. This includes reconstructing cross-page table-of-contents (TOC) hierarchies and identifying typed links from tables and figures to their captions, notes, and sources, often in one-to-many form. Because these structures are covered only partially or subsumed within broader parsing protocols, existing benchmarks cannot directly evaluate two key document-level tasks: \emph{Table-of-Contents Hierarchy Recovery} and \emph{Contextual Relationship Recovery}. To benchmark these two tasks, we introduce \textsc{LongDocBench}, comprising 85 real-world financial reports, textbooks, and academic papers spanning 2,582 pages, with up to 105 pages per document. It provides human-verified annotations for 3,937 heading nodes (mean node depth 3.55; maximum depth 9) and 3,258 contextual relationships annotated across 2,680 table and figure objects. We further evaluate both the downstream utility and recoverability of these structures. Long-document question-answering experiments show that human-verified TOC hierarchies and contextual relationships improve reasoning, with their combination providing complementary benefits. Meanwhile, representative document parsers remain limited on both recovery tasks despite strong page-level performance. To support further progress, we publicly release \textsc{LongDocBench} and its evaluation protocol and reproducible testbed for advancing document-level structure recovery in long documents.

---


### 115. [GATTA: Graph Active Learning with Test-Time Augmentation](https://arxiv.org/abs/2608.15084)

**<font color=#1a73e8>作者：</font>** Zsombor Bánfi, András Gézsi, András Formanek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time augmentation (TTA) has proven effective for improving model robustness and uncertainty estimation in computer vision, yet its application to graph-structured data remains largely unexplored. We introduce GATTA (Graph Active Learning with Test-Time Augmentation), a framework for enhancing active learning by aggregating predictions across multiple augmented views to produce more reliable uncertainty estimates. To address the challenge of label-preserving graph augmentations, GATTA incorporates a consistency-based filtering mechanism that discards augmented views yielding unreliable predictions. We systematically evaluate GATTA across multiple graph datasets, GNN architectures, and acquisition strategies. Our results show that simple uncertainty-based methods, such as Entropy and Least Confidence, benefit most from TTA, achieving performance competitive with more sophisticated and computationally expensive approaches. GATTA generalizes across architectures, outperforms model-side ensemble methods such as MC Dropout. We further show that GATTA scales efficiently with both ensemble size and graph size. Extensive analysis of augmentation types, strengths, and filtering strategies provides practical guidelines for effective deployment. Our findings demonstrate that augmenting simple methods with TTA offers a more efficient path to strong active learning performance than engineering complex acquisition functions, enabling practitioners to achieve competitive results with lower computational overhead and reduced implementation complexity.

---


### 116. [Distribution-free false-alarm calibration and chance-corrected spatial evaluation for industrial anomaly detection](https://arxiv.org/abs/2608.15090)

**<font color=#1a73e8>作者：</font>** Jie Deng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Studies of industrial visual inspection commonly report the area under the receiver operating characteristic curve (AUROC) and the overlap between anomaly maps and defect masks. Neither measure specifies the false-alarm rate at a selected threshold, while recurrent defect locations and mask geometry can inflate overlap. We combine a distribution-free upper tolerance threshold with a paired-minus-crossed spatial test. This test compares each detector's score-contributing locations with the matched defect mask and with masks from other images; the difference in rates defines spatial-evidence lift relative to the empirical chance-overlap rate. We evaluate three detectors on 120 point-defect images from three ISP-AD modalities and three fixed data splits. Of 378 alarms, 230 overlap the matched mask. Paired and crossed rates are nevertheless similar in eight of nine detector--modality cells; only DINOv2--ASM has a positive 95\% bootstrap lower bound (lift 0.259, 95\% interval 0.159--0.347). On the independent Magnetic Tile Defect dataset, the same analysis gives lifts of 0.203 (0.169--0.236) for Wide ResNet-50 (WRN50) patch memory and 0.231 (0.202--0.262) for Vision Transformer B/16 (ViT-B/16) patch memory, with one-sided permutation $p=10^{-5}$ for both. When crossed masks are restricted to the same defect class, the lifts remain 0.185 and 0.210. Exact sample planning shows that, with 150 calibration normals, a 95\%-confidence distribution-free claim is supported only for target false-positive rates of 1.98\% or higher; a 1\% target requires at least 299 normals. The results support reporting operating-point performance and chance-corrected spatial evidence alongside AUROC and raw mask overlap.

---


### 117. [Validation-Frontier Representation Selection under Constrained Observation](https://arxiv.org/abs/2608.15095)

**<font color=#1a73e8>作者：</font>** Wesley Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems deployed outside clean benchmark settings often rely on observations that are incomplete, unstable, costly, or degraded by monitoring failures. This paper studies representation selection under constrained observation: choosing a state representation when raw accuracy is not the only operational criterion. We propose a validation-frontier selector that combines balanced accuracy with penalties for feature cost, overfit gap, and validation-test instability. In a focused public-tabular benchmark using three scikit-learn datasets, five observation regimes, 45 matched task cells, 720 candidate actions, and 405 representation rows, the adaptive selector improves frontier score over full trace features by 0.025801 while reducing mean feature count by 22.733. Balanced-accuracy difference is small and not statistically significant. A broader offline stress test gives mixed results. The supported claim is therefore bounded: adaptive representation selection can improve a constrained-observation robustness-efficiency frontier in matched benchmark settings, but does not universally dominate trace baselines.

---


### 118. [MODAL: Multi-Modal Object Re-ID via Model-Driven Sparse Decoupling and Text-Image Differential Filtering](https://arxiv.org/abs/2608.15096)

**<font color=#1a73e8>作者：</font>** Chengbo Huang, Jun-Jie Huang, Long Lan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal object re-identification (Re-ID) aims to facilitate cross-camera object retrieval in complex environments by leveraging complementary information from visual (e.g., RGB, NIR, TIR) and textual modalities. However, existing approaches often lack principled feature disentanglement and coherent multi-modal integration, leading to entangled representations that introduce cross-modal conflicts, obscure discriminative cues, and suffer distribution shift under modality-missing conditions. To tackle these challenges, we propose MODAL, a novel multi-modal object re-identification framework, grounded in coupled sparse coding theory and differential suppression principles. A core component of MODAL is a Multi-modal Feature Sparse Decoupling module, developed in a model-driven deep unrolling manner based on multi-modal coupled sparse coding. It explicitly decomposes multi-modal features into uni-modal specific, bi-modal and tri-modal shared representations, thereby achieving more transparent and effective feature disentanglement. Benefiting from the principled feature disentanglement, MODAL naturally mitigates performance degradation in incomplete-modality scenarios via a Modality-Aware Subspace Activation that selectively activates only the consistently shared subspaces. Moreover, we propose a Text-Image Differential Filtering module that leverages coarse-grained textual semantics to adaptively suppress task-irrelevant responses in the decoupled visual representations, thereby enhancing discriminative information. Extensive experiments on four datasets demonstrate that MODAL achieves state-of-the-art performance with superior transparency.

---


### 119. [Second-Order Policy Effects as State Transitions: A Source-Linked Benchmark for Policy Simulation](https://arxiv.org/abs/2608.15101)

**<font color=#1a73e8>作者：</font>** Wesley Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Policy evaluation often estimates direct benefits and costs while treating the institutional environment as fixed. In practice, a policy changes the system it enters: actors adapt, enforcement capacity shifts, burdens move, and new equilibria form around capture, gaming, compliance theater, irreversibility, and repair costs. We formalize this as second-order policy-effect prediction and present a source-linked benchmark for policy simulation. The benchmark contains 96 named public-policy cases across eight domains and four balanced action classes: implement, modify, pilot, and block. Each case includes source locators and state variables for benefit, capture, gaming, burden shift, instability, uncertainty, irreversibility, distributional risk, and implementation capacity. The runner regenerates method outputs and aggregate results from the case table, and the simulator never reads the expert action target. We report a protocol-based transition-channel audit with recall, precision, F1-style efficiency, and selective top-channel stress diagnostics, so universal channel coverage is not mistaken for field validation. The side-effect simulator achieves mean policy-effect quality of 0.945, compared with 0.838 for the risk-register baseline and 0.879 for the causal-loop baseline. Its advantage is concentrated in side-effect recall and aggregate transition scoring; it does not dominate the best structured baselines on exact policy-action choice. The evidence remains benchmark-based, but supports a bounded claim: transition-state variables make policy simulators more sensitive to downstream institutional effects.

---


### 120. [ProjFormer: Point Cloud Completion via Geometric-Projective Transformer and Cross-Modal Semantic Constraints](https://arxiv.org/abs/2608.15104)

**<font color=#1a73e8>作者：</font>** Sheng Liu, Meng Wang, Ruihui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud completion is inherently ill-posed due to severe sparsity and ambiguity in partial observations. Existing multi-view methods alleviate this by incorporating 2D semantics, but often rely on learned attention and fixed fusion, which lack geometric consistency and adaptability. We propose ProjFormer, a cross-modal framework that enforces geometry-consistent 2D-3D interaction through explicit projection and adaptive feature routing. A Projective Guided View Attention module aligns 3D points with multi-view features via deterministic projection, enabling efficient and geometrically consistent aggregation. Building on this, a geometry-aware routing network performs point-wise adaptive fusion of structural and observation-driven features for progressive refinement. Experiments show that, under a lightweight design, ProjFormer delivers competitive performance with improved structural completeness.

---


### 121. [EMASAM: a Computationally Efficient Sharpness-Aware Minimization via EMA-Guided Perturbations](https://arxiv.org/abs/2608.15105)

**<font color=#1a73e8>作者：</font>** Tanapat Ratchatorn, Masayuki Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in optimization research has highlighted the sharpness of the loss landscape as a key factor in narrowing the generalization gap. Motivated by this insight, Sharpness-Aware Minimization (SAM) was proposed as a training strategy that enhances generalization. Despite the promising performance, SAM suffers from its twice computational cost due to its core algorithm requiring an extra gradient computation during the perturbation step. To overcome this limitation, we introduce Exponential Moving Average Sharpness-Aware Minimization (EMASAM), a computationally efficient variant of SAM. EMASAM does not require the loss gradient in the perturbation step. Instead, EMASAM defines the perturbation direction based on the discrepancy between the main model and the EMA shadow model. This perturbation travels away from the stable average position toward the less stable area, acting as a softer yet cheaper alternative to SAM's worst-case scenario perturbation. Moreover, since EMASAM's perturbation does not rely on noisy mini-batch gradients, it mitigates the gradient-induced instability inherent in SAM. Hence, EMASAM eliminates the need for an extra backpropagation while also preserving the generalization ability of the SAM-style training. Several experiments have been performed and confirm the efficiency and robustness of our method.

---


### 122. [Global Federated Learning Strategies for Building Efficient Personalized Models](https://arxiv.org/abs/2608.15107)

**<font color=#1a73e8>作者：</font>** Seongyoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a practical framework that can train models on distributed user data while guaranteeing data privacy; however, due to heterogeneity in which each user has a different data distribution, problems frequently arise where both global and personalization performance deteriorate simultaneously. This dissertation presents methodologies for building efficient personalized models by identifying which strategies are effective in the global training stage and by showing how to preserve global knowledge while securing user-specific performance during local adaptation. First, we show that as data heterogeneity increases, the collapse of feature vectors is a more fundamental bottleneck than classifier weights, and propose a method that directly mitigates the discrepancy in representation magnitude between local and global models. Second, we analyze that a training approach that strengthens local alignment can induce forgetting of global knowledge (e.g., categories not observed locally), and propose a method that achieves both local alignment and global knowledge preservation by combining feature distillation based on the global model's feature vectors. Third, in federated personalized reward model learning with preference heterogeneity, we empirically verify the conventional belief that "increasing the number of global models yields better initialization," and we show that when sufficient local fine-tuning is allowed, a single global initialization can instead provide stronger personalization performance. This study redefines the role of global initialization under data and preference heterogeneity and provides practical training strategies that simultaneously satisfy global knowledge preservation and personalization.

---


### 123. [CETalk: Continuous Valence-Arousal Control for Audio-Driven 3D Talking Head Generation](https://arxiv.org/abs/2608.15110)

**<font color=#1a73e8>作者：</font>** Peng Jia, Li Dai, Zhen Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotional 3D talking head generation aims to synthesize expressive facial animations with accurate lip synchronization. However, existing methods often rely on discrete emotion categories, which fail to capture the continuous evolution of affect. They also overlook the temporal frequency mismatch between audio articulation and emotional expression. In this paper, we propose CETalk, an audio-driven 3D facial animation framework conditioned on continuous Valence--Arousal (VA) representations for fine-grained emotion control. CETalk predicts a sequence of FLAME parameters through three key components: a Dynamic Emotion Modulation Module that adaptively scales emotional intensity using audio-derived cues; a Multi-Scale Temporal Modeling mechanism that employs parallel branches to decouple high-frequency articulatory movements from low-frequency emotional dynamics; and a Dynamic Fusion Mechanism that integrates these multi-scale features via an adaptive gating network. To support training and evaluation, we construct 3D-VA-MEAD, a large-scale dataset with automatically estimated VA annotations and reconstructed 3D facial motions. Extensive experiments demonstrate that CETalk outperforms state-of-the-art methods in both lip-sync accuracy and emotional expressiveness, while enabling smooth and controllable emotion transitions.

---


### 124. [Probability-Preserving Transformer for the Time-Dependent Schrödinger Equation](https://arxiv.org/abs/2608.15112)

**<font color=#1a73e8>作者：</font>** Mushtaq Ali, Muzamil Tariq, Niaz Ali Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving the time-dependent Schrödinger equation (TDSE) via traditional numerical methods is computationally intensive. Transformer models offer a compelling alternative, but standard implementations rely on soft constraints that cannot rigorously guarantee probability conservation. Here, we introduce a Transformer architecture that enforces TDSE probability conservation as a hard constraint. The design intrinsically ensures unitarity across temporal evolution without requiring repeated retraining. Our empirical findings show that this hard-constraint approach is not only physically exact but also computationally superior to conventional soft-constraint methods.

---


### 125. [Fast Test-Time Refinement for Robust Learned Image Compression](https://arxiv.org/abs/2608.15113)

**<font color=#1a73e8>作者：</font>** Jiaming Liang, Chi-Man Pun, Weisi Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned image compression (LIC) has demonstrated remarkable rate-distortion (RD) performance in benign settings. However, the high representational capacity endowed by deep neural networks (DNNs) comes at the expense of increased adversarial vulnerability. This hinders their adoption as trusted standardized codecs. Recent work has sketched test-time refinement (TTR) as a defense in gray-box scenarios, despite its original purpose of improving benign RD performance. Unfortunately, extensive iterations of TTR incur prohibitive overhead, while the robustness mechanism lacks theoretical understanding. Moreover, TTR has not been evaluated in white-box settings or against attacks beyond $\ell_2$-bounded rate and untargeted distortion objectives. To bridge these gaps, we present a systematic study. Our study reveals an Asymmetric Adversarial Trajectory (AAT) property in LIC systems: transitioning from adversarial to benign regions is significantly easier than the reverse process, where adversarial examples can often be roughly recovered within only 1-2 steps. We provide a two-dimensional Tube Model to explain this phenomenon. Based on AAT, we propose a Fast Test-Time Refinement (FTTR) framework for practical and robust LIC systems. We establish that the robustness arises from the contraction of adversarial regions induced by the Input-as-Label property of LIC systems, rather than from obfuscated gradients. Extensive evaluations with diverse strong adaptive attacks across multiple LIC systems demonstrate the promise of the proposed FTTR framework. The code is available at this https URL.

---


### 126. [Decision-Driven Regularization: A Blended Model for Learning and Optimization](https://arxiv.org/abs/2608.15124)

**<font color=#1a73e8>作者：</font>** Gar Goei Loke, Qinshen Tang, Yangge Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In contextual optimization, the decision-maker seeks optimal decisions to minimize a cost function, that varies based on observed features. This context is common in many business applications ranging from on-demand delivery and retail operations to portfolio optimization and inventory management. In this paper, we study the learning and optimization approach, which first learns how outcomes result from the features, and then selects optimal decisions based on these outcomes. We focus on the integrated learning and optimization literature, and identify that a lack of control for prediction accuracy can lead to overfitting and a loss of decision effectiveness against simple separate learning and optimization models. Instead, we propose a bi-objective formulation that balances prediction accuracy and cost minimization, termed decision-driven regularization. It also addresses ambiguity in the definition of the cost function via a surrogate that depends on a new hyperparameter. We additionally show that alternative perspectives for formulating the problem, namely robust optimization and regret minimization, lead to models that are closely related to our proposed model. As a consequence, our framework generalizes models such as SPO+. Our model is shown to be numerically superior to other benchmarks, such as OLS, Random Forest, XGBoost, SPO+, Perturbation Gradient, and Learning and Rank, in our synthetic studies.

---


### 127. [Platform Adaptation Under Governance Interventions: Actor Best-Response Modeling and an External Public-Case Benchmark](https://arxiv.org/abs/2608.15131)

**<font color=#1a73e8>作者：</font>** Wesley Shu, Peng Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital platforms govern by changing rules: rankings, monetization thresholds, moderation standards, verification systems, disclosure requirements, appeal processes, and access policies. These interventions are rarely absorbed passively. Creators, sellers, advertisers, moderators, users, developers, and strategic operators adapt to the new reward surface. This paper develops a platform-adaptation model for evaluating governance interventions as transitions in adaptive multi-actor information systems. The model represents actor best response, strategic gaming opportunity, moderation burden, user-incentive movement, enforcement response, externality formation, and downstream platform stability. We evaluate the model on 72 external public platform-governance cases covering media monetization, ranking systems, verification, delivery platforms, marketplaces, app stores, community platforms, and creator ecosystems. Across 9 methods and 648 method-case evaluations, the full platform-adaptation simulator achieves mean adaptation quality of 0.836338, compared with 0.669731 for a risk-register baseline, 0.589457 for causal-loop analysis, 0.492750 for generic governance critique, 0.369492 for engagement-only optimization, and 0.331965 for baseline policy review. Paired comparisons show a win rate of 1.00 against all tested baselines and channel ablations. The contribution is an information-systems theory and measurement framework showing why platform governance evaluation fails when it treats policy rules as static controls rather than interventions into adaptive actor-response fields.

---


### 128. [HOIMask: Towards Generative Masked Modeling for Human Object Interaction Generation](https://arxiv.org/abs/2608.15141)

**<font color=#1a73e8>作者：</font>** Yihong Ji, Jinsong Zhang, He Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based methods have dominated the HOI generation, as they enable critical contact fusions or signals to guide the diffusion process. However, they often result in high artifacts and unstable interaction quality due to error accumulation during iterative denoising. In this work, we propose HOIMask, the first generative masked framework for modeling HOI motion in discrete space. HOIMask first encodes both motion sequences and contact-aware signals into discrete 2D human and object token maps via HOI Vector Quantization (VQ), preserving fine-grained spatial-temporal structure beyond conventional 1D representations. On this basis, a generative masked modeling framework is employed to jointly capture human-object interaction dynamics, leveraging a transformer architecture designed to model complex spatial-temporal and interaction dependencies. To generate more coherent and physically plausible motions, we further introduce a novel contact-aware reconstruction guidance in discrete space during inference, which fuses contact signals to optimize HOI tokens that forces the generated motion with higher spatio-temporal consistency. With craftily designed motion interaction tokens, dedicated architecture and guidance strategy, HOIMask outperforms state-of-the-art diffusion-based methods, generating more realistic and semantically aligned HOI motions. Please refer to this https URL for more results.

---


### 129. [Translating finite-domain integer constraint models to CP/SMT/ILP/PB/SAT solvers with CPMpy](https://arxiv.org/abs/2608.15143)

**<font color=#1a73e8>作者：</font>** Tias Guns, Ignace Bleukx, Hendrik Bierlee 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constraint solving is a declarative approach for solving combinatorial satisfaction and optimization problems. The user specifies their problem through constraints and decision variables, and a generic solver is used to find a solution. Several constraint-solving technologies exist, and certain solvers perform well on certain problems. Therefore, it is useful to try different solvers given a particular application. However, each solving paradigm supports different types of constraints and decision variables.
Our goal is to translate high-level constraint satisfaction and optimization problems into any lower-level formalism, including CP, SMT QF-LIA, ILP, PB and (Max)SAT. This allows for comparing different solving technologies for a particular problem, without requiring a user to manually remodel it for each solving paradigm.
We define a high-level language of logical and arithmetic operations, and useful additional functions and constraints, which are known as global constraints in the CP community. We then present a modular framework for transforming our high-level modeling language to CP/SMT/ILP/PB and (Max)SAT solvers. While many transformations are partly described in the literature, we observe that they can be implemented through a modular waterfall of smaller components, where lower-level paradigms reuse the transformations of higher-level paradigms. Two recurring challenges are handling the negation of arbitrary subexpressions and avoiding the introduction of auxiliary variables. Additionally, we take special care linearizing non-linear operators for ILP, PB and SAT-solvers.
The transformation waterfall is implemented and evaluated in the open-source CPMpy library. Our results show that constraint models significantly change throughout the transformations, and that optimizations to the linearization of constraints are essential for ILP and PB solvers.

---


### 130. [PureTD: Reinforcement Learning for Backgammon Money Games with No Evaluation-time Search](https://arxiv.org/abs/2608.15146)

**<font color=#1a73e8>作者：</font>** Alexander L. Strehl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We revisit Tesauro's TD-Gammon for backgammon money games in the setting of no evaluation-time search. Both checker play and cube action (use of the doubling cube) are learned from scratch via self-play reinforcement learning (RL), with minimal hand-coded logic and no expert features. In this setting, we demonstrate that pure self-play RL suffices to train models that reach near-state-of-the-art playing strength. Specifically, for cubeful money games, our search-free model evaluates faster and is substantially stronger than the open-source engines GNU Backgammon and Open Sage running a one-move (1-ply) look-ahead search.

---


### 131. [SAEFUZZ: Smart Contract Vulnerability Detection through Statically Guided Evolutionary Fuzzing](https://arxiv.org/abs/2608.15151)

**<font color=#1a73e8>作者：</font>** Shiting Yu, Rundong Wei, Xiaoqi Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The effectiveness of smart contract fuzzing depends strongly on whether generated transactions reach deep, state-dependent execution paths. Existing fuzzers often generate highly random call sequences, wasting executions on semantically invalid or low-value states and leaving vulnerabilities that require specific invocation orders unexplored. We present a lightweight method for generating fuzz test cases under bytecode-level static guidance. We construct an Ethereum virtual machine control-flow graph, extract paths containing vulnerability-relevant instructions, recover function selectors, and order externally callable functions according to storage read-write dependencies. A coverage-guided evolutionary strategy then generates, evaluates, recombines, and mutates executable seeds. Five dedicated runtime oracles target reentrancy, integer overflow or underflow, block-state dependence, unsafe delegate calls, and frozen Ether. The evaluation uses deployed Ethereum contracts, including labelled vulnerable contracts. SAEFUZZ detects most labelled vulnerable contracts, yielding 98.50% accuracy, 90.00% precision, and 81.82% recall. It also achieves 84.07% mean instruction coverage, with valid test cases accounting for 93.48% of generated cases. Ablation results indicate that static guidance, directed seed generation, and vulnerability-specific oracles each contribute to the final performance.

---


### 132. [An Adaptive Gradient Clipping and Noise Injection Mechanism for Differentially Private Federated Learning](https://arxiv.org/abs/2608.15153)

**<font color=#1a73e8>作者：</font>** Wenjing Wei, Alla Jammine, Farid Nait-Abdesselam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differentially private federated learning must balance privacy protection against model accuracy and training efficiency. Static gradient clipping applies a fixed threshold throughout training and across model layers, which can cause excessive clipping when the threshold is too small or unnecessarily large noise when it is too large. This paper presents DDP-SA-adaptive, an adaptive gradient clipping and noise adding mechanism for differentially private federated learning with secure aggregation. At each communication round, every client determines a separate clipping threshold for each model layer from the median of its per-sample gradient norms. The resulting layer-wise thresholds adapt to the evolving gradient distributions and calibrate the Laplace noise added before the updates are encoded and secret-shared among intermediate aggregation servers. We evaluate the proposed mechanism on a federated regression task in terms of efficiency, accuracy, privacy, convergence, clipping norm, and noise magnitude. Compared with the static DDP-SA baseline, DDP-SA-adaptive reduces the number of communication rounds by 6.81%, total training time by 19.21%, and average per-round training time by 13.33%, leading to improved training efficiency. It also reduces test loss by 98.74% and increases test R2 by 3.41%, leading to improved model accuracy. To attain R2 = 0.99, the adaptive mechanism operates with a privacy budget of approximately epsilon = 0.1, compared with epsilon = 0.4 for static DDP-SA, thus providing stronger privacy protection and achieving stronger privacy guarantees. These results demonstrate that round-wise, layer-wise adaptation can improve the privacy-accuracy-efficiency trade-off of differentially private federated learning.

---


### 133. [A Unified Backbone--Expert Framework with Relation-Token and Residual--Classifier Interfaces for Automatic Modulation Recognition](https://arxiv.org/abs/2608.15160)

**<font color=#1a73e8>作者：</font>** Zhixiang Deng, Houbiao Li, Zongyong Cui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic modulation recognition (AMR) faces distinct representation bottlenecks under varying observation lengths, where a single model architecture often fails to excel. To address this, we propose a unified backbone-expert framework with a common convolutional state-space backbone and two specialized interfaces. For short sequences, we inject explicit lag-aware complex-plane descriptors as relation tokens before encoding to compensate for information loss. For long sequences, we design a gated multi-scale residual refinement module to correct the feature map, combined with a fixed-averaging classifier collaboration to harness complementary evidence. Our framework achieves overall average accuracies of 67.28 \pm 0.14% on RML2016.10b and 87.19 \pm 0.77% on HisarMod2019 (mean \pm sample standard deviation over three runs), respectively. The framework's efficacy is further validated through three-seed ablations, native-length cross-configuration tests, and controlled window studies, confirming the benefit of expert-interface decoupling over one-size-fits-all architectures.

---


### 134. [FinFraudBench: A Heterogeneous Graph Benchmark for Financial Fraud Detection](https://arxiv.org/abs/2608.15177)

**<font color=#1a73e8>作者：</font>** Yixuan Chen, Hongyu Zhan, Jie Sheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing complexity of digital financial systems has reshaped financial fraud detection from isolated transaction classification into relational risk reasoning over interconnected financial entities. This shift has motivated graph-based fraud detection, where models identify fraudulent nodes by exploiting dependencies among customers, cards, merchants, categories, and locations. However, despite rapid progress in graph-based methods, existing public benchmarks remain misaligned with real-world financial systems in two important aspects. First, they often simplify financial ecosystems into homogeneous or single-node-type multi-relational graphs, failing to preserve the multi-entity and multi-relational nature of financial data. Second, they rarely provide large-scale heterogeneous financial graph datasets with realistic operating conditions such as extreme class imbalance and limited label availability, making it difficult to assess the practical effectiveness of current methods. To address these gaps, we present FinFraudBench, a heterogeneous graph benchmark for financial fraud detection. FinFraudBench contains two heterogeneous graph datasets (CreditCard-Fraud and BankTrans-Fraud) with up to 8.99M nodes and 89.23M directed typed edges. Each dataset preserves six financial entity types, fourteen directed edge types, and natural fraud rates that mirror deployment constraints. With these datasets, we establish a standardized evaluation protocol covering both ranking and imbalance-sensitive classification metrics, and evaluate representative baselines. Extensive experiments yield empirical insights into current methods' limitations and suggest promising avenues for future research. FinFraudBench is available at this https URL.

---


### 135. [Pre-Model Representation Failures in GNN-Based Smart Contract Vulnerability Detection](https://arxiv.org/abs/2608.15184)

**<font color=#1a73e8>作者：</font>** Birindwa Prisca Hondi, Chinoso Philip Nwishienyi, Charity Wanja Mwaura 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper is a failure analysis of the representation layer underlying GNN-based smart contract vulnerability detectors. These systems convert source code into graphs before any learning takes place; if the graph fails to capture the code's semantics, no model improvement can compensate.
We investigate GNNSCVulDetector and identify four failures. First, structurally different contracts produce byte-for-byte identical graphs, constituting a concrete evasion attack. Second, graph construction is governed by a hardcoded 47-entry variable whitelist (including one duplicate entry), which constrains what the extractor can recognise. As a consequence, identical vulnerabilities with different variable names produce inconsistent graphs, graph quality degrades as naming diverges from the whitelist, and when no entry matches the pipeline produces structural output not grounded in source variables. Third, the C node (the graph element representing the external caller that triggers a reentrancy attack) is absent from even the most canonical vulnerable contract in the literature. Fourth, a controlled experiment confirms this as a direct misclassification: a fully exploitable contract is labelled safe because the C -> W edge is never constructed.
All four failures are demonstrated experimentally. Current accuracy figures in the literature are measured under conditions that do not expose these failures. We demonstrate one confirmed case of misclassification caused directly by a representation-layer failure; the prevalence of such failures in real-world contract populations remains an open empirical question.

---


### 136. [MiNO: Cotangent-bundle propagator learning for PDEs](https://arxiv.org/abs/2608.15187)

**<font color=#1a73e8>作者：</font>** Gnankan Landry Regis N'guessan, Bum Jun Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific machine learning for partial differential equations commonly targets solution fields, as in physics-informed neural networks, or solution maps, as in neural operators. We study a third target: the propagator itself, a phase and amplitude in phase space. The motivation is a gap in regularity. A transported discontinuity is nonsmooth in space and time, yet the rule that moves it can be a polynomial phase carrying unit amplitude, so the object that generates an evolution can be far smoother than the field it generates. The microlocal neural operator (MiNO) learns that object, using the eikonal equation for the phase and the transport equation for the amplitude, and recovers the solution by an oscillatory integral. Sharp fronts and caustics then belong to propagation geometry rather than to a field fitted pointwise. Small residuals certify more than the reconstructed field. They place the learned canonical relation, the geometry that carries singularities, close to the exact one, and they separate trainable error from the frequency-truncation tail. On a matched-budget discontinuous-advection benchmark, MiNO stops improving within 10,000 steps at the accuracy limit of its finite reconstruction window, a limit predicted in closed form, whereas a physics-informed neural network with neural-tangent-kernel loss balancing stays near its initial error. On smooth advection, the mean error is $3.84\times10^{-3}$ for MiNO and $3.12\times10^{-2}$ for a supervised Fourier neural operator. Single-branch MiNO is the smallest model compared, and one trained generator serves five unseen initial conditions without retraining.

---


### 137. [Anchor-Regularized Adaptation for Generalizable AI-Generated Image Detection with DINOv3](https://arxiv.org/abs/2608.15196)

**<font color=#1a73e8>作者：</font>** Hyeongjun Choi, Juhun Lee, Davide Cozzolino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent works in AI-generated image detection have shown that careful training data alignment can improve generalization by removing spurious correlations. However, linear probes on frozen DINOv3 representations achieve remarkably strong performance even when trained on misaligned datasets. Motivated by this result, we analyze the underlying rationale and the limits of this generalization. We find that frozen DINOv3 performs well because its decisions rely on features that faithfully represent the space of authentic images. At the same time, its final layer is less effective at capturing the subtle pixel-artifact cues that can be emphasized by aligned training data. We further observe that naively mixing aligned and misaligned data during adaptation improves sensitivity to such cues but at the cost of distorting the pre-trained representation, limiting generalization. To address this issue, we propose Anchor-Regularized Adaptation (ARA). We apply Low-Rank Adaptation to capture pixel-level artifacts while leveraging a frozen anchor classifier to avoid deviations from the original representation structure. This allows the model to exploit pixel-artifact cues without sacrificing generalization. Our method achieves state-of-the-art performance on nine diverse and challenging benchmarks, indicating that ARA enables complementary supervision from misaligned and aligned data for more effective detection.

---


### 138. [TERRA: A Hierarchical Parallel Training and Memory Orchestration Framework for High-Resolution AI-based Earth Modeling](https://arxiv.org/abs/2608.15211)

**<font color=#1a73e8>作者：</font>** Ruohan Wu, Ziqi Zhu, Yang Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training high-resolution AI-based Earth forecasting models is memory-intensive. Window-based Swin Transformers reduce the quadratic cost of global attention, but existing distributed systems such as AERIS primarily target pixel-level models and do not jointly support convolutional sampling modules and shifted-window execution. Long-lead rollout finetuning further increases activation memory. To address these challenges, we present TERRA, a hierarchical parallel training framework for high-resolution Earth forecasting. TERRA introduces Sampling-Aware Window, Sequence, and Tensor Parallelism (SAWSTP), which preserves spatially contiguous layouts for sampling modules and routes tokens into topology-aware ragged window layouts for Transformer execution. For long-lead finetuning, Memory Orchestration (MO) provides rollout-aware checkpoint planning and combines input buffering with budget-constrained activation offloading. Experiments on the $1/12^\circ$ GLORYS-based Wenhai workload show that TERRA supports models with up to 11.4B parameters on 96 H200 GPUs and sustains up to $39.76$ PFLOPS, achieving $65.0\%$ strong-scaling and $94.1\%$ weak-scaling efficiency. Compared with checkpoint-only policies, MO further reduces peak allocated GPU memory by $32.2\%$--$51.8\%$ with at most $20.0\%$ step-time overhead, which makes finetuning with smaller patch sizes and longer rollouts feasible for improved forecasting accuracy.

---


### 139. [Self-Supervised Topologically Invariant Manifold Learning for Railway Image Quality Assessment](https://arxiv.org/abs/2608.15217)

**<font color=#1a73e8>作者：</font>** Tingqiong Cui, Yibu Yang, Yang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing blind image quality assessment (BIQA) methods typically rely on synthetic distortions and subjective annotations, limiting generalization in real-world domains. To address this, we propose a fully self-supervised BIQA framework based on topologically invariant manifold learning under boundary constraints, which constructs a stable quality reference without manual labels. The framework generates progressive background dilution scales via repeated random cropping around each target; exploiting the monotonic degradation of target information density across these scales, it establishes a self-constrained quality manifold. A linearized spatial moment projection eliminates geometric distortions from random cropping; then a monotonicity divergence filter prunes background-sensitive evaluators, isolating an elite pool \(\mathcal{M}_{\text{elite}}\). A robust M-estimator with a principal component stabilizer fuses the metrics into an asymptotically efficient pseudo-ground truth \(q_{\text{PGT}}\), contracting variance toward the Cramér-Rao lower bound. Extensive evaluations demonstrate that the elite evaluator pool, distilled from 11 baseline metrics, secures superior zero-shot transferability across standard synthetic and wild benchmarks (CSIQ, LIVEC, LIVE-2). Concurrently, deployments on the CQU Railway Rolling Stock Surveillance Dataset (2,797 images) yield a manifold cosine similarity \(>0.999\) and a 100.0\% survival rate under industrial extreme stresses, robustly validating its cross-paradigm decoupling and topological resilience.

---


### 140. [Inferring 1-Minimal Trigger Configurations for Assessing Linux Kernel CVE Triggerability](https://arxiv.org/abs/2608.15225)

**<font color=#1a73e8>作者：</font>** Tongjie Wei, Peng Zhang, Zhiwen Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vendors assessing Linux kernel CVEs need to know whether a bug is triggerable under production-tailored configurations, not merely whether a version is affected, yet upstream reproducers and vulnerability databases rarely provide configuration-level context. We study minimal trigger-configuration inference: given a CVE entry and a target kernel version (optionally a baseline .config), we synthesize a Kconfig-satisfiable option set that remains effective after make olddefconfig and, when a reproducer is available, still triggers under a specified evaluation protocol; we then prune it to a 1-minimal (subset-minimal) boundary for evaluation. Our framework FCC links vulnerability cues to build-system symbols, completes implicit prerequisites under olddefconfig feedback to avoid silent rollback, and performs runtime-validated minimization guided by dependency topology. We evaluate on KernJC and KernelCTF, totaling 88 CVEs across multiple kernel versions. On the 88-CVE set, FCC improves the post-make olddefconfig configuration success rate from 62.5% (55/88) to 96.6% (85/88) over an olddef-only injection baseline; on the KernJC set, FCC reduces the average candidate set size by 78.7% compared to KernJC (Avg. 14.72 vs. 69.00 options per CVE). A stage-wise analysis of time and token costs shows that Stage I dominates overhead, while CVE-focused evidence selection substantially reduces this cost. By returning an effective and auditable 1-minimal configuration boundary, FCC helps vendors scope triggerability against their deployment configurations with a clear, tool-supported decision line.

---


### 141. [PersonaDrive: Controllable Trajectory Prediction with Multi-Dimensional Driving Personas](https://arxiv.org/abs/2608.15230)

**<font color=#1a73e8>作者：</font>** Chan Lee, Kimin Yun, Yuseok Bae 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although recent trajectory prediction and end-to-end autonomous driving methods improve robustness in urban environments, they still lack meaningful controllability. Existing benchmarks either provide no persona-conditioned annotations or support only a single urgency spectrum (i.e., emergency, normal, relaxed), which cannot distinguish personas that share the same urgency level but require different driving dynamics. To address this, we propose (i) the Persona-Conditioned Trajectory (PCT) dataset, which decomposes driving personas along two axes, Temporal Urgency and Ride Comfort, and combines three levels of each to form a grid of nine personas, each paired with natural-language descriptions and trajectories, and (ii) PersonaDrive, a framework that can learn driving personas from language and can generate persona-specific trajectories. PersonaDrive incorporates Persona-Conditioned Anchor Transform (PCAT), which hierarchically reshapes anchors along both axes, and Persona-Conditioned Multi-Modal Fusion (PCMF) for BEV-level persona fusion. Training is supervised by a Hierarchical Guide Loss enforcing axis-aligned physical orderings and an Axis-Decomposed Diversity Loss preventing diagonal mode collapse. Experimental results show that PersonaDrive consistently improves over the compared baselines across multi-dimensional scenarios. The code and PCT dataset are available at this https URL

---


### 142. [LongRCA Bench: Diagnosing Responsible Roles and Root Causes in Long-Horizon Agent Failures](https://arxiv.org/abs/2608.15242)

**<font color=#1a73e8>作者：</font>** Yunfei Zhang, Boyu Feng, Changhua Pei 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a long-horizon agent execution fails, outcome-level evaluation reveals the unsuccessful result but not where the decisive error entered the trajectory. Developers must then inspect the full execution to identify the responsible role and localize the earliest decisive root-cause step. Existing failure-attribution benchmarks largely focus on shorter traces, leaving diagnosis across hundreds of recorded steps underexplored. We introduce LongRCA Bench, comprising 1,140 failed trajectories across five domains without injected errors. It provides independently scored human labels for the responsible role and earliest decisive root-cause step. The median trajectory contains 145 steps, and the strongest baseline reaches only 13.2% exact root-step accuracy. We further present Root-Cause Trajectory Attribution (RCTA), a training-free method that retrieves candidate error steps from segment summaries and traces them to available earlier handoff instructions. Using the same backbone, benchmark instances, and scoring protocol, RCTA reaches 51.1% responsible-role accuracy and 24.1% exact root-step accuracy. These results highlight the need to evaluate responsible-role attribution and exact root-step localization as separate targets in long-trajectory failure diagnosis.

---


### 143. [CG-GLORE: A Conjugate Gradient-Based Global-Local Regularization Network for Sparse-View CT Reconstruction](https://arxiv.org/abs/2608.15246)

**<font color=#1a73e8>作者：</font>** Tran Xuan Hieu Le, Doanh C. Bui, Vu Trung Duong Le 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view computed tomography (CT) reduces radiation dose by acquiring fewer projection views, but the resulting inverse problem is highly ill-posed and often produces severe streak artifacts. Existing deep reconstruction methods have achieved promising performance, yet many rely on first-order updates or large regularization networks, which can be less effective in ill-conditioned settings. We propose \textbf{CG-GLORE}, a compact deep unrolling framework inspired by second-order optimization for sparse-view CT reconstruction. Each unrolled stage uses a CG-solved linear system based on a structured Hessian surrogate: it retains the physics-induced curvature of the data-fidelity term while using an identity approximation for the learned regularization term. Thus, the method is second-order-inspired rather than an exact Newton method for the full learned objective. To model image priors, we design a Global-Local Regularization Network (GLORE), which combines convolutional local feature extraction with a Long-Range Dependency Representation module based on sparse patchification and Nyström attention. This design captures anatomical details and non-local dependencies while maintaining practical complexity. Experiments on AAPM and DeepLesion under multiple sparse-view and noise settings show that CG-GLORE achieves strong quantitative performance, stable convergence, lower noise power, and improved visual fidelity compared with representative reconstruction methods.

---


### 144. [Robust structure from motion for aerial-ground images via detector-free feature matching and multi-view track refinement](https://arxiv.org/abs/2608.15251)

**<font color=#1a73e8>作者：</font>** San Jiang, Hui Wang, Xing Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Integrated 3D reconstruction from aerial-ground images is essential for generating high-precision urban 3D models, yet severe variations in viewpoint, scale, and rotation make robust feature matching highly challenging. To address these limitations, this study introduces a rotation-robust detector-free matching network coupled with multi-view track refinement for incremental Structure from Motion (ISfM). The proposed workflow features four key modules. First, rotation-aware feature extraction replaces traditional convolutions with an Omnidirectional State Space Block (OSS Block) that selectively scans across eight symmetrical directions to model long-range spatial dependencies and synthesize rotation-invariant feature maps. Second, multi-scale attention transformation utilizes quadtree attention to build a hierarchical token pyramid that isolates high-association token regions and discards irrelevant areas, capturing long-range context with linear computational complexity. Third, bi-directional feature matching executes a symmetric coarse-to-fine matching scheme where coarse alignment computes dual-direction Softmax confidence matrices under mutual nearest neighbor constraints, and fine alignment uses a multi-layer perceptron to regress sub-pixel coordinate offsets. Finally, multi-view track refinement employs an integrated indexing structure to evaluate localized spatial proximity and link disjoint sub-tracks to the highest-confidence anchor point, ensuring stable feature repeatability across the ISfM pipeline. By using real aerial-ground datasets, experimental results demonstrate that the proposed method improves AUC at 5° pose error by 93.9% compared with LoFTR and achieves the highest precision in ISfM reconstruction, with the improved accuracy ranging from 27.6% to 32.7%. The proposed method provides a reliable solution for integrated 3D reconstruction of aerial-ground images.

---


### 145. [Decentralized Federated Learning for Heterogeneous Multi-Task Semantic Communication](https://arxiv.org/abs/2608.15256)

**<font color=#1a73e8>作者：</font>** Lin Yin, Tiejun Lv, Weicai Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collaborative training in distributed semantic communication (DSC) networks typically relies on decentralized federated learning (DFL). However, pushing topology-agnostic aggregation into heterogeneous, multi-task environments creates a fundamental bottleneck: it drives negative transfer and overconsensus bias (OCB). This paper introduces a personalized DSC framework that cuts off this cross-task interference. At the node level, a policy-driven multi-path routing mechanism separates task-specific features from shared representations to preserve local fidelity. Across the network, we deploy a "communicationwhile- aggregation" protocol. It calibrates a column-stochastic consensus matrix using task affinities. This limits the system to absorbing complementary knowledge while actively blocking mismatched parameter updates. To bound the convergence, we derive a unified Lyapunov drift analysis. We reveal a strict Ushaped trade-off: deeper topological mixing reduces variance but amplifies structural OCB. Resolving this tension yields a closed-form expression for the optimal aggregation depth. We evaluate the proposed framework on NYU-v2, where the results reveal a clear trade-off between insufficient aggregation and excessive topological mixing. At the analytically derived optimal aggregation depth, our method achieves a 4.77% global relative improvement over the no-aggregation baseline and outperforms decentralized FedAvg, FedAMP, and heuristic max aggregation. We further evaluate the framework on Taskonomy and imperfect wireless links to examine the effects of network-size variation and wireless-link reliability.

---


### 146. [UAV Video Deblurring via Motion-Aware Diffusion: A Path to Robust Target Detection](https://arxiv.org/abs/2608.15259)

**<font color=#1a73e8>作者：</font>** Zhiqiang Hu, Shouren Huang, Masatoshi Ishikawa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned Aerial Vehicles (UAVs) play a crucial role in various scenarios ranging from disaster response to traffic surveillance. However, aerial video footage often suffers from severe motion blur due to rapid flight maneuvers, vibrations, and camera panning, which can significantly degrade downstream tasks such as target detection. Our goal is to explore a computationally-efficient and effective video deblurring approach to enhance UAV target detection performance. To reduce computational cost, we first propose an Adaptive Latent Scale Selector that dynamically adjusts the latent space resolution according to the intensity of UAV motion, thus balancing detail preservation with inference efficiency. To ensure temporal consistency, we introduce a Multi-Frame Alignment and Learnable Gating module to warp and gate the preceding frames, allowing the model to fuse only relevant temporal information and suppress misaligned or uninformative features. Our method can effectively recover sharp details from the UAV video stream. Extensive experiments on real UAV benchmarks demonstrate that our method not only yields superior deblurring performance but also significantly boosts target detection accuracy, making it highly applicable to robust aerial vision tasks.

---


### 147. [VGGT-Align: Bridging Local Reconstruction and Global Consistency for Long-Sequence 3D Reconstruction](https://arxiv.org/abs/2608.15260)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Yihang Wu, Songhua Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maintaining global geometric consistency is a central challenge in long-sequence 3D reconstruction, with scale drift being the most critical failure mode. In chunk-based inference pipelines, the scale degree of freedom in sequential Sim(3) alignment is left unconstrained, causing estimation errors to compound multiplicatively and distort global trajectories and point cloud geometry. We present a scale-consistency enhancement framework built on a key insight: in structured environments such as driving scenes, geometric quantities arising from environmental regularity remain inherently invariant across temporal segments, and discrepancies in their per-chunk measurements directly expose inter-chunk scale drift. We propose Scene Geometric Invariant Anchoring (SGIA), which extracts dominant geometric invariants from each chunk's predicted point cloud via coarse-to-fine robust estimation and exploits their cross-chunk consistency to establish scale constraints independent of point cloud registration, explicitly degenerating 7-DoF Sim(3) alignment into 6-DoF rigid-body transformation and severing chain-wise scale error propagation at its source. We further introduce a lightweight test-time adaptation strategy that fine-tunes only normalization-layer parameters via multi-objective self-supervision, progressively improving intra-chunk predictions along the sequence. Both modules are plug-and-play and require no offline retraining. Experiments on multiple long-sequence benchmarks demonstrate state-of-the-art performance, reducing absolute trajectory error by up to 32% with significant gains in trajectory stability and reconstruction quality. Code: this https URL

---


### 148. [Boundary-Aligned Contribution Routing for Robust Optical--SAR Object Detection](https://arxiv.org/abs/2608.15261)

**<font color=#1a73e8>作者：</font>** Haifa Zhang, Yijing Wang, Haoyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical imagery provides rich appearance cues, whereas synthetic aperture radar (SAR) offers observations that are less sensitive to illumination and weather, making optical--SAR fusion attractive for remote-sensing object detection. However, the presence of multiple modalities does not guarantee beneficial fusion: imperfect spatial, temporal, and semantic correspondence can make an otherwise intact stream conditionally harmful and induce negative cross-modal transfer. We handle this issue through a model-specific task-utility perspective and learn task-conditioned contribution routing using detection supervision alone. The proposed fusion-boundary-aligned routing regulates each modality's contribution before the first learned cross-modal feature-value mixing operation. For architectures with frequent shallow interaction, a Feature Router performs cross-conditioned, group-addressable modulation near the input; for dual-backbone architectures, a Dual-Statistic Semantic Router predicts stream-level contribution weights from modality-specific average and maximum statistics before late semantic fusion. The routers require no explicit utility supervision, quality labels, reconstruction, or distillation. Experiments on M4-SAR and SpaceNet6-OTD cover nominal full inputs, controlled correspondence shifts, missing modalities, and four nonzero modality-corruption scenarios. Across the reported clean-training controls, routing improves full-input $\text{mAP}_{50}$ by 0.5--5.9 points. Relative to the corresponding modality-dropout baselines, it raises missing-modality $\text{mAP}_{50}$ by 7.6--41.6 points and reduces the negative-transfer rate by up to 12.7 percentage points. Spearman correlations between the learned routing weights and model-specific leave-one-modality-out utility range from 0.45 to 0.66, supporting the task-utility interpretation of the routing coefficients.

---


### 149. [On the Adversarial Robustness of Remote Sensing Semantic Change Detection](https://arxiv.org/abs/2608.15267)

**<font color=#1a73e8>作者：</font>** Weikang Yu, Yonghao Xu, Pedram Ghamisi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic change detection (SCD) is a bitemporal dense-prediction task that jointly identifies changed regions and their semantic states before and after change. Unlike single-image segmentation or binary change detection, SCD couples two temporal inputs with timestamp-wise semantic prediction, change localization, and final semantic-change decoding, creating adversarial dependencies that are not captured by conventional robustness protocols. We present a task-specific evaluation framework that separates output-side attack objectives from input-side temporal perturbation access, enabling systematic analysis of component vulnerability and cross-temporal propagation. Experiments on four datasets and six representative CNN-, Transformer-, and state-space-based models evaluate component-level and temporal objectives, single- and dual-timestamp perturbations, multiple attack methods, and cross-architecture transferability. The results show that final semantic-change predictions can be severely corrupted even when binary change localization remains comparatively stable, and that perturbations or attack objectives associated with one timestamp can propagate to the prediction of the other. These behaviors occur across different architecture families, while direct cross-model transfer remains considerably weaker than white-box attacks. The study demonstrates that adversarial robustness in SCD depends on the complete bitemporal prediction pathway rather than on an individual branch or backbone family, and provides a structured protocol for evaluating robustness in coupled bitemporal image analysis. Code is available at this https URL.

---


### 150. [RemiVoice: Supporting Reminiscence Therapy for Older Adults with Mild Dementia Through Voice-First Conversational AI](https://arxiv.org/abs/2608.15273)

**<font color=#1a73e8>作者：</font>** Aaryan Gajula, Soumay Agarwal, Shaoze Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the global population aging and increasing prevalence of dementia, there is an urgent need for effective solutions to support patients across various stages of Alzheimer's Disease and Related Dementias (ADRD). Reminiscence Therapy (RT) is a validated intervention designed to trigger memories and is widely used for various stages of dementia. We present our preliminary prototype and exploration of RemiVoice, a browser-based voice-first conversational AI assistant that supports older adults with mild dementia in RT through conversationally grounded images and videos.

---


> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
