# 📦 其他研究 | 2026年11月25日

> 本类共 **569** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-550**（第 11/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-569](./part-12.md)

---

### 501. [EgoDepth-Bench: Benchmarking Metric Depth for Egocentric Manipulation](https://arxiv.org/abs/2611.30734)

**<font color=#1a73e8>作者：</font>** Yuan Gao, Dongchen Wei, Xinyang Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce EgoDepth-Bench, comprising 941,233 synchronized samples collected across 37 distinct physical environments. Each sample combines six calibrated RGB views with metric depth in the native fisheye view, reconstructed from five active-infrared stereo modules. A calibrated ball-bar confirms millimeter-level geometric accuracy, with a median error of 1.27 mm on a known sphere spacing. Environment-held-out splits enable evaluation of generalization to unseen environments. Across monocular, stereo, and multi-view models, the benchmark measures both depth accuracy and prediction coverage, including on hands and objects. Fine-tuning MapAnything on EgoDepth-Bench reduces metric AbsRel from 0.708 to 0.091 and scale-aligned AbsRel from 0.327 to 0.072 on unseen environments. These results demonstrate that EgoDepth-Bench provides effective supervision and enables rigorous evaluation of metric and relative depth estimation in egocentric manipulation. The project page provides the evaluation code and interactive RGB-depth sequences.

---


### 502. [Object-Centric Differentiable Logic Networks for Abstract Visual Reasoning](https://arxiv.org/abs/2611.30736)

**<font color=#1a73e8>作者：</font>** Hanne Say Eren, Ana Ezquerro, Ozan Özdenizci  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human visual intelligence enables efficient reasoning capabilities on abstract visual problems with bounded cognitive resources and minimal experience, and yields remarkable generalization to novel problems with its ability to draw relational analogies and modular abstractions. In contrast, deep learning models require exhaustive task-specific training on large datasets, making them prone to exploiting visual shortcuts and resulting in poor generalization. While neuro-symbolic approaches attempt to bridge this gap by decoupling perception from reasoning with dedicated computation units, existing solutions rely either on explicit rule supervision or parameter-heavy transformer architectures that reintroduce the computational inefficiencies they aim to solve. We introduce Slot-Dwn to address these limitations, a novel neuro-symbolic architecture that unifies unsupervised object-centric perception with logic-based symbolic reasoning. Our model utilizes a Multi-Head Differentiable Weightless Network (MH-DWN) that performs efficient reasoning entirely in Boolean space using look-up tables (LUTs). Our framework reduces visual perception complexity and introduces a LUT-based relational bottleneck with sparse input routing to minimize computational overhead. We evaluate Slot-Dwn across various abstract visual reasoning benchmark tasks targeting systematic rule generalization, sample-efficient anomaly detection, and multi-relational reasoning. We demonstrate that Slot-Dwn yields competitive performance with respect to the state-of-the-art, under extreme out-of-distribution regimes, while requiring up to 52% fewer trainable parameters, with significantly faster convergence.

---


### 503. [SchemaCaps: When a Compatible Tool Update Silently Widens an AI Agent's Authority](https://arxiv.org/abs/2611.30750)

**<font color=#1a73e8>作者：</font>** Yulliwas Ameur, Samia Bouzefrane, Soumya Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The tools users approve for their AI agents keep changing their JSON input schemas. Of 8 surveyed MCP clients and scanners, none is observed or documented to re-approve a tool whose input schema widens (two not determinable). We define non-amplification over the coordinates visible in the schema (declared arguments and undeclared fields, on effective values) and a re-binding rule decided by subschema inclusion, trusting no field labels by default and conservative up to its checker and tested case analysis. Evidence: a Coq proof of composition; 48 regression tests; an exact-reference benchmark, where the reviewed version of the rule silently re-bound 27 amplifying changes, now fixed; and a pilot on 604 releases of 39 public MCP servers. There, 412 of 580 compatible schema changes widen some coordinate, yet compatibility re-binds them silently. The authors' adjudicated double annotation finds at least 76 that add or widen an authority-bearing argument (66 of the 84 a name-based labeller flags, plus 10 it misses). On existing tools, the rule asks 645 re-approvals, against 1,197 for pinning the input schema (2,004 with descriptions) and 617 for compatibility. Behaviour change behind an identical schema remains out of reach.

---


### 504. [Learning Dense Head-Object Contact Estimation with Synthetic Data](https://arxiv.org/abs/2611.30751)

**<font color=#1a73e8>作者：</font>** Daniel Sungho Jung, Kyoung Mu Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Head serves a critical role in human cognitive and perceptual functions while remaining vulnerable to external impacts, making the understanding of head contact essential for human safety. Despite its importance, dense head-object contact estimation remains largely unexplored, primarily due to the absence of head-object contact data. Recently, it has been shown that synthetic data can serve as powerful training data in limited data scenario, implying the potential of synthetic data in head-object contact estimation. There are two core challenges for dense head-object contact estimation. First, head-object interactions are highly diverse, resulting in substantial variations in contact regions and patterns across different objects and interaction types. Second, head contact regions are often heavily occluded by hair, making direct visual observation of the actual contact regions difficult. To address these issues, we introduce HEad COntact estimation (HECO) with synthetic data. To handle diverse head-object interactions, we leverage semantic context from text features that encode semantic relationships between head regions and interacting objects. To resolve hair occlusion issue of actual head contact regions, we introduce occlusion-aware contact learning that learns to infer head contact beyond visible information from images via amodal inpainting. As a result, we enable head-object contact estimation with HECO trained with our synthetic dataset, overcoming the issue of absence of contact data. The codes will be released.

---


### 505. [Screening for nonrigidity in structure from motion using projected reprojection residuals](https://arxiv.org/abs/2611.30769)

**<font color=#1a73e8>作者：</font>** Íñigo Cirauqui-Viloria  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse structure from motion (SfM) assumes a static scene, yet deformation may still yield plausible reconstructions. Reprojection-error summaries discard how errors are arranged across points and views. We propose a diagnostic that first removes residual components explainable by small point and camera adjustments and simple spatial trends that change over time. It then measures alignment with fixed spatial and temporal patterns. The diagnostic uses one estimated SfM reconstruction and provides screening evidence rather than a physical deformation estimate. Across four synthetic tubular families, the diagnostic detected all eight acquisitions with prescribed motion, compared with five or six for summaries of reprojection-error magnitude. Each family's cutoff was the highest static score among the other three families, so the static acquisition with the highest score also screened positive. With the same cutoffs, the diagnostic retained positive detections in 19 of 20 reconstruction variants spanning changes in appearance and reconstruction pipeline, with one numerical abstention. These findings show that the arrangement of reprojection errors across points and views can reveal inconsistencies that their magnitudes alone miss. The four families were known during development, and the transfer variants reused two of them. Within this setting, the diagnostic offers a practical way to flag a plausible reconstruction for closer inspection using only its estimated cameras, 3D points and image observations.

---


### 506. [GRAIN: Shared-Budget Complementary Re-observation for Object Detection](https://arxiv.org/abs/2611.30770)

**<font color=#1a73e8>作者：</font>** Chengxuan Zhou, Shaoyang Zhang, Rui Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Re-running a frozen detector on enlarged image crops recovers small and crowded objects without retraining, yet every crop costs an extra detector call. Existing slicing and adaptive-cropping pipelines plan crops per image in isolation, even though inspection demand varies widely across an image collection. We present GRAIN, which unifies cross-image call allocation and bounded-output admission around cross-image comparable resolution-closure gains over boundary-safe crop interiors. Coarse hypotheses carry resolution deficits, crops close a geometric share of those deficits for hypotheses enclosed in their interior positive region, and multiplicative residuals discount covered evidence within a monotone submodular surrogate. Prefix sums and a global max-heap execute this collection-wide plan on CPU before crop inference, and Positive-Region Fusion aligns post-inference spatial admission with the planned interior support before class-balanced top-
selection. Across 17 frozen detectors from five families on COCO, CrowdHuman, and VisDrone-DET, GRAIN beats call-matched tiling in 100 of 102 AP@100 settings and transfers to AI-TOD-v2. With RF-DETR-S on CrowdHuman, it nearly matches two-crop tiling using one eighth of the crop calls. At fixed budgets, the surrogate orders candidate plans with Spearman correlations of 0.95 to 0.99 while the sweep attains at least 98% of the exact surrogate optimum. Code will be publicly released.

---


### 507. [Reconstructing 3D+t Cardiovascular Flow From Sparse Planar Velocity Fields With Neural Fields](https://arxiv.org/abs/2611.30775)

**<font color=#1a73e8>作者：</font>** Viraj Patel, Deblina Bhattacharjee, Katharine Fraser  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing time-resolved three-dimensional (3D+t) cardiovascular flow from sparse planar measurements is challenging because each plane observes only the two in-plane velocity components, on a small part of the volume. We propose a plane-aware neural-field framework that learns a continuous 3D velocity field from space and time coordinates through a per-plane projection, and then investigate the potential benefits of physics constraints. We evaluate the framework on computational aortic and aneurysm datasets, and on planes resampled from a real cardiac 4D Flow MRI scan. A plain multi-layer perceptron (MLP) was more accurate than classical radial basis function (RBF) interpolation on both computational datasets. For the aorta, a physics-constrained SIREN (PC-SIREN) reduced the rRMSE further to $0.3756$, compared with $0.4273$ for the plain MLP and $0.7256$ for RBF, and it was the most accurate model in every anatomical segment of the MRI data. For the aneurysms the plain MLP remained the most accurate model, with an rRMSE of $0.07$ to $0.16$ against $0.55$ to $0.71$ for PC-SIREN. Further experiments investigated scanning configuration, number of scans, and spatial resolution. These findings show that continuous neural fields can reconstruct volumetric cardiovascular flow from sparse planar measurements, and that physics constraints have to be matched to the flow.

---


### 508. [AvatarAnyone: Agentic Reconstruction of Mesh-Based Layered Avatars from YouTube Video](https://arxiv.org/abs/2611.30777)

**<font color=#1a73e8>作者：</font>** Aymen Mir, Peter Wonka, Stefanos Zafeiriou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce AvatarAnyone, a method for reconstructing avatars from casual YouTube videos as layered meshes, with each garment and footwear as a separate mesh layered on top of the body mesh. In such videos, people differ in garment classes, clothing types, and layers, and each combination needs a different reconstruction. A single fixed layered reconstruction pipeline therefore fails. AvatarAnyone solves this problem with AI agents that plan a custom optimization for each person's reconstruction. The agents predict the garment classes, the clothing type, and the layering. They use these predictions to choose an initialization and stage the optimization. Because the avatars are layered meshes, they support applications such as virtual try-on and cloth simulation. We change the clothing layers of an avatar and render it in different garments and poses. We can also simulate a clothing layer as cloth over the animated body with a standard cloth simulator. Most existing avatars are one fused surface or a set of Gaussians and cannot do this. We load the avatars directly into Blender, Unreal Engine, and robotics simulators such as MuJoCo. As the avatars are meshes, they support contact modeling with other objects. We show results from around 150 YouTube videos. On four datasets, AvatarAnyone outperforms existing mesh-based methods for animatable monocular reconstruction. Our project page is available at this https URL.

---


### 509. [PVFormer: Proper Velocity Transformer for Stable and Scalable Hyperbolic Representation Learning](https://arxiv.org/abs/2611.30785)

**<font color=#1a73e8>作者：</font>** Xianglong Shi, Nicu Sebe, Bernhard Schölkopf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic representations have shown remarkable success on hierarchical and tree-like data, and Transformers have become a central architecture for representation learning. However, a principled construction of hyperbolic Transformers remains challenging because the self-attention layer decomposes into three coupled primitives, transformation, similarity, and aggregation, that should all respect the underlying geometry. Existing hyperbolic Transformer designs are typically built in the Poincaré or Lorentz models, where bounded domains, time-like constraints, tangent-space detours, or projection steps make it difficult to keep the full block intrinsic and scalable. To address this gap, we propose PVFormer, to the best of our knowledge, the first Transformer architecture that operates natively in proper velocity (PV) space. The proper velocity model provides an unconstrained representation of hyperbolic geometry, and PVFormer exploits this structure to redesign the Transformer block in PV space. On the transformation side, we use PV homomorphism transformations to update query and value representations. On the similarity side, we generalize Euclidean inner-product attention with a PV Busemann score inspired by Busemann-based hyperbolic learning and a PV point-to-hyperplane key transformation. On the aggregation side, we replace Euclidean averaging with PV midpoint aggregation and further derive a scalable PV linear attention variant for large graphs. Extensive experiments support the effectiveness of PVFormer across graph, text, and vision benchmarks.

---


### 510. [BridgeMVS: Bridging Multi-View Stereo and Monodepth via Bidirectional Dynamic Fusion](https://arxiv.org/abs/2611.30787)

**<font color=#1a73e8>作者：</font>** Jianfei Jiang, Haochen Yu, Qiankun Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-View Stereo (MVS) and Monocular Depth Estimation (MDE) provide complementary cues for dense 3D reconstruction. While MVS leverages explicit geometry for metric depth, it struggles in challenging regions where feature matching is unreliable. Conversely, MDE provides robust structural priors but typically yields scale-ambiguous results. Existing hybrid methods mainly exploit monocular cues in a unidirectional manner, leaving the mutual enhancement between MDE and MVS insufficiently explored. To address this limitation, we propose BridgeMVS, a unified cascaded multi-stage MVS framework that bridges monocular depth features and multi-view cost volume representations through Bidirectional Dynamic Fusion (BDF). At each stage, BDF performs dynamic mono-to-cost and cost-to-mono updates, where monocular structural features guide cost volume refinement for more robust MVS depth estimation, while multi-view geometric evidence recalibrates monocular representations to improve their metric-scale consistency. Furthermore, the fused monocular and multi-view representations are progressively propagated from coarse to fine stages and constrained by stage-wise relative-scale MDE supervision and metric-scale MVS supervision, enabling cross-branch interactions to benefit subsequent high-resolution depth estimation. In addition, BDF is designed as a plug-and-play module that can be conveniently integrated into existing cascaded MVS frameworks. Extensive experiments demonstrate that BridgeMVS achieves state-of-the-art performance on the DTU, Tanks-and-Temples, and ETH3D benchmarks, while simultaneously boosting the accuracy of monocular depth estimation. Notably, BridgeMVS ranks first on both the Tanks-and-Temples Intermediate and Advanced benchmarks. The source code is available at \href{this https URL}{this https URL}.

---


### 511. [From joint attention to shared symbols: A free-energy principle account](https://arxiv.org/abs/2611.30788)

**<font color=#1a73e8>作者：</font>** Tadahiro Taniguchi, Koji Hashimoto, Ryuichiro Ishikawa  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Joint attention precedes vocabulary acquisition. How can attending to the same object help two people with different sensory experiences come to use a shared word? In a free-energy principle account, marginalizing the common object induces a statistical dependence between private perceptual states. In a categorical world, the joint prior inherits a mixture structure whose component index provides a candidate for shared reference. The collective predictive coding model approximates this prior by representing the dependence through that shared index. An established Metropolis-Hastings naming game lets agents infer and exchange words using private evidence. Toy and multiview image experiments illustrate how word exchange can coordinate private categories and improve the fit of collective models. The account connects joint attention to shared symbols through the coupling of private inference.

---


### 512. [How Systems Treat Intent: A Faceted Taxonomy of Intent for Human-AI Co-Creation](https://arxiv.org/abs/2611.30793)

**<font color=#1a73e8>作者：</font>** Ashwin Ram, Radha Kumaran, Alexander Koller 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-AI interaction depends on systems acting on user intent rather than explicit procedures, even when that intent is incomplete, evolving, or partially communicable. Literature organizing systems by interaction technique, workflow stage, or division of labor, offer limited insight into which facet of intent an interaction mechanism addresses. We introduce a six-facet taxonomy of intent, grounded in philosophical accounts of mind, action, and meaning, and apply it to systems presented in 198 papers from eleven SIGCHI venues. Our analysis reveals that different forms of incomplete intent are associated with distinct interaction and authorship strategies, showing that mechanisms that appear similar often address fundamentally different intent-related problems. This exposes blind spots, as intent is rarely represented as an interaction object, authorship provenance is rarely tracked, and tentative preferences are rarely distinguished from firm commitments. The taxonomy offers a lens for analyzing and designing AI systems around the facets of intent they address.

---


### 513. [PestWeave: Linking Semantic Modeling and Evidence-Guided Text Modulation through Visual Prototypes for Fine-Grained Pest Learning](https://arxiv.org/abs/2611.30796)

**<font color=#1a73e8>作者：</font>** Xueheng Li, Yu Wang, Yuxiang Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agricultural pests threaten crop yield and quality, making accurate pest recognition essential for targeted management and sustainable agriculture. Their diverse appearances complicate recognition and motivate multimodal approaches incorporating complementary species knowledge from text. However, complex backgrounds can obscure discriminative visual cues, while textual descriptions may contain information unsupported by the current image, limiting effective cross-modal fusion. To address these challenges, we propose PestWeave, a multimodal framework connecting content-adaptive visual organization with text fusion through visual prototypes. Its visual pathway augments a Receptance Weighted Key Value (RWKV) architecture with semantic token grouping and three types of auxiliary tokens, enabling content-adaptive scanning and contextual modeling while preserving spatial structure. Feature-similar tokens are reordered into adjacent scanning positions, while cluster prototype, global, and register tokens provide group-level summaries, global context, and additional interaction capacity, respectively. These prototypes also guide text modulation by assessing visual support for semantic components and regulating their relative contributions and overall fusion strength, reducing interference from unsupported descriptions. Extensive experiments on multiple pest recognition datasets demonstrate the effectiveness of PestWeave and its potential for practical pest management.

---


### 514. [Go Far, Look Less: Active Multi-Room Reconstruction with Persistent Goals and Selective Views](https://arxiv.org/abs/2611.30802)

**<font color=#1a73e8>作者：</font>** Jiawei Jiang, Haonan Zhou, Wendi Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active 3D reconstruction aims to allocate a sparse view budget to recover complete geometry and high-fidelity renderings. However, existing methods degrade sharply in multi-room homes: myopic next-best-view scoring gives transit no credit for distant rooms and over-polishes irreducible nearby residuals, whereas dense mappers reach far rooms only by streaming thousands of frames. We propose ROAM-GS, a training-free active multi-room reconstruction framework that couples persistent goals with selective views: each decision selects a goal and a variable-horizon prefix toward it, capturing only at its endpoint. A Surface Reconstruction Memory scores poses by projecting post-update defects and viewing directions. Persistent goals credit transit with their remaining value and are released once arrivals stop measurably improving them. Without per-scene tuning, ROAM-GS achieves state-of-the-art multi-room reconstruction while preserving single-room Replica fidelity, raising mean coverage from 74% to 93% on HSSD and from 47% to 96% (+11.7 dB PSNR) on HM3D, and matching 90-minute dense mapping using $173\times$ fewer views.

---


### 515. [Unpacking the Evaluators: How Configuration Shapes the Evaluation of Alignment in Explainable AI](https://arxiv.org/abs/2611.30816)

**<font color=#1a73e8>作者：</font>** Gizem Karagoz, Tanir Ozcelebi, Nirvana Meratnia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) evaluation fundamentally requires human-centered evaluation, assessing whether explanations align with human reasoning and expert knowledge. However, such evaluations often require expert-driven manual validation and are difficult to scale, leading to the widespread use of alignment-based metrics, where attribution maps are compared against predefined ground-truth (GT) representations. Despite their popularity, alignment evaluations are implicitly bias towards multiple design choices made during the evaluation process, for example GT representations, metric families, metric formulations (soft vs. hard), and thresholding strategies. In this paper, we formalize alignment evaluation as a structured evaluation configuration space through which the influence of these design choices can be systematically analyzed. We further introduce a structured alignment evaluation framework that models interactions between XAI methods, GT representations, metric families, metric formulations, and thresholding strategies across 2D and 3D synthetic and real-world datasets. In addition, we propose a novel taxonomy of XAI output behavior based on local entropy and boundary mass ratio, enabling structured characterization of attribution patterns for alignment evaluation. Our experiments reveal systematic flows (triples of XAI-GT-metric configurations), showing that alignment outcomes provide distinct behavior patterns under certain configurations, such as soft/hard metric implementations. We further observe varying levels of threshold sensitivity across metric families and attribution structures. These findings demonstrate that alignment evaluation cannot be treated as a fixed or invariant measure of explanation quality, and provide practical guidance for designing more reliable and behavior-aware XAI evaluation protocols.

---


### 516. [NeuroMotion: Aligning EEG to Discrete Motion Primitives for Continuous Motion Decoding](https://arxiv.org/abs/2611.30817)

**<font color=#1a73e8>作者：</font>** Yi Liu, Qi Zhang, HaoLin Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG-to-motion decoding remains challenging because noisy scalp EEG is difficult to map directly to continuous kinematics. We present NeuroMotion, a framework that aligns EEG representations to discrete motion primitives for continuous motion decoding across heterogeneous paradigms, including full-body free movement, lower-limb treadmill locomotion, and upper-limb freewill reaching and grasping. A VQ-based motion prior discretizes continuous motion into reusable primitives that serve as both alignment prototypes and intermediate prediction targets. Prototypical and supervised contrastive objectives align EEG embeddings to motion-derived prototypes and organize them according to primitive assignments. An E2M Transformer predicts motion-code sequences from the learned EEG representations, while a final geometric refinement stage improves continuous trajectory reconstruction through motion-level training. Under a last-session test protocol, NeuroMotion achieves the best mean reconstruction performance among the compared EEG decoding baselines across all three datasets, with the clearest gains on full-body motion in both reconstruction accuracy and distribution-level quality. Multi-subject ablations further support the contributions of EEG-to-primitive alignment, token prediction, and refinement. Code is available at this https URL.

---


### 517. [Task-Dependent Linguistic Measures in Aphasia Discourse: A Comparative Analysis of Narrative, Descriptive, and Procedural Speech](https://arxiv.org/abs/2611.30826)

**<font color=#1a73e8>作者：</font>** Emma Al Kubaisi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Transcript-based measures such as word counts, lexical diversity and disfluency rates are widely used to describe language ability in aphasia. Each measure comes from a specific elicitation task, and studies use different tasks, so values from different tasks may not be comparable. Aims: To test whether discourse tasks change these measures within the same speakers, and whether the measures follow a gradient from Procedural to Descriptive to Narrative discourse. Methods & Procedures: Baseline transcripts from 61 adults with chronic post-stroke aphasia were taken from the Fridriksson-2 corpus in AphasiaBank (POLAR trial, this http URL NCT03416738). Each speaker produced a Procedural (Sandwich), a Descriptive (Broken Window) and a Narrative (Cinderella) sample in one session. A rule-based pipeline extracted 13 measures, 10 of which were common enough to test. Friedman, Page and Wilcoxon tests with false discovery rate correction were used, with a speaker-grouped Random Forest classifier as a supporting check. Outcomes & Results: Total words and number of different words followed the full gradient, but the step from Procedural to Descriptive was small. For most other measures, Narrative stood apart, while Descriptive and Procedural did not differ. Among the 31 speakers with at least 25 words in every task, filler rate, repetition rate and total disfluency density were higher in Narrative than in both other tasks. The classifier reached an accuracy of 0.61 (always guessing the most common task would give 0.41), mainly by recognizing Narrative samples. Conclusions: Discourse tasks are not interchangeable, and expressing disfluencies per word does not remove the task effect. The task should be reported with every measure, and values should be compared only within the same task.

---


### 518. [Potential Games for Self-Neighborhood Channel Mixing in Graph Neural Networks](https://arxiv.org/abs/2611.30829)

**<font color=#1a73e8>作者：</font>** Marco Lavorini, Davide Bacciu, Giancarlo Bigi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph message passing must balance two competing objectives: incorporating neighborhood signals while preserving node-specific information. We model this trade-off as a game in which nodes choose how to mix their own representations with strict-neighborhood aggregates. For fixed channel representations, task supervision defines a common-payoff game, while local distinctness payoffs induce an exact potential game whose potential is the degree-normalized strict Dirichlet energy. We introduce CG2, which amortizes these choices through a shared six-parameter policy per layer based on local channel statistics and can be trained using either objective. Controlled comparisons show that the shared task-trained policy improves mean performance over fixed mixing on three of five heterophily benchmarks, with significant gains on two, while free per-node actions trained with either objective rarely improve on the same baseline. On the ECHO long-range benchmark, the clearest contribution of the gate appears on eccentricity, where the task-trained policy substantially reduces prediction error.

---


### 519. [Can Multimodal Fusion MakeSense for Embodied Vision in Degraded Sensing?](https://arxiv.org/abs/2611.30836)

**<font color=#1a73e8>作者：</font>** Cheng-Ru Chou, Shih-Yu Lai, Pei-Lin Chiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied vision systems rely on complementary sensors to perceive and act as conditions change. Even models that accept arbitrary sensor subsets can exhibit negative fusion: adding a sensor increases prediction error. We propose MakeSense, a multimodal fusion framework that preserves sensor-specific evidence in private streams and combines information through shared bottleneck tokens. Training pairs full and subset views of the same degraded observations, penalizing higher error with more sensors. Where geometry permits, the distance readout uses range measurements alone, while the rest of the prediction draws on all available inputs. Paired tests across five datasets reveal helpful and harmful sensor additions. MakeSense reduces negative fusion on MM-Fi. With lightweight adapters and per-dataset training, the same design improves UAV localization on MMAUD, cooperative 3D detection on V2X-Real, few-shot pose transfer to RELI11D, and command prediction on Humanoid-Everyday, where a world model trained on the frozen core's outputs forecasts future fused states more accurately than a linear baseline at longer tested horizons. MakeSense supports embodied sensing across human activity, aerial systems, robotics, and autonomous driving.

---


### 520. [Certified Defense against Adversarial Patches on Traffic Signs via Mask-Aware Training](https://arxiv.org/abs/2611.30840)

**<font color=#1a73e8>作者：</font>** Rudra Saxena, Vishal Dev Verma, Rohan Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial patches are a practical threat to traffic-sign recognition: a small sticker on a sign can change a classifier's decision. PatchCleanser is a certified defense that applies two rounds of masking and, for every image it certifies, provably returns the correct label for any patch that fits inside one mask. We show that on traffic signs the defense certifies almost nothing when paired with a normally trained classifier (1.7% to 4.8% certified accuracy on GTSRB), because a single mask can hide the small central symbol that distinguishes sign classes. We propose mask-aware training, which trains the classifier on images occluded by random pairs drawn from the defense's own mask set, with a sampling bias toward masks over the sign's centre. The defense, mask set and certification procedure are unchanged, so the guarantee is preserved. For an ImageNet-pretrained ResNet-50, mask-aware training raises certified accuracy from 4.8% to 60.0%. Under real per-image adversarial patches, the defended ResNet-50 reaches 85.7% accuracy, versus 74.6% for the original PatchCleanser with a normally trained ResNet-50.

---


### 521. [Age and Gender Estimation from Face and Ocular Smartphone Images via Identity Transfer and Ordinal Learning](https://arxiv.org/abs/2611.30850)

**<font color=#1a73e8>作者：</font>** Fernando Alonso-Fernandez, Kevin Hernandez-Diaz, Jose Maria Buades 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate the transferability of identity-recognition representations to gender and age estimation from face and ocular images. Three CNNs of varying complexity, pre-trained for face or ocular identity recognition, are evaluated using fixed features with SVMs and end-to-end adaptation. Experiments use 11,299 frontal smartphone images from Adience, following its predefined five-fold protocol and subject-disjoint validation. Results show that domain-matched identity pre-training outperforms direct ImageNet and scratch initialisation in end-to-end training, while combining both ocular regions narrows the gap with full-face estimation, especially for age. We additionally introduce an ordinal loss that exploits the ordering of age groups and consistently improves 1-off accuracy across architectures and input regions. Across the evaluated configurations, best gender accuracies reach 88.1% for the face and 82.9% for combined ocular regions, while age estimation reaches 59.0% exact and 93.1% 1-off accuracy for ocular images, versus 57.6% and 95.2% for the full face. To our knowledge, these are the highest ocular age accuracies reported on Adience.

---


### 522. [CableMoE: Harm-Regularized Mean-Residual Expert Fusion for Transmission-Corridor Segmentation](https://arxiv.org/abs/2611.30859)

**<font color=#1a73e8>作者：</font>** Shima Salehi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic mapping of transmission corridors benefits from heterogeneous LiDAR and image-guided predictors, but replacing a strong ensemble with a learned router can damage rare electrical assets. We introduce CableMoE, a post-hoc mixture of four frozen segmentation experts. Its deployable prediction is a calibrated residual around availability-aware probability averaging, while a harm penalty discourages extra loss on points that the mean already classifies correctly. A matched component study shows why each design choice is needed: an unconstrained learned mixture loses 1.032 mIoU points relative to probability mean, harm regularization restores 0.359 points at fixed capacity, and removing an unnecessary point-wise gate slightly improves accuracy and stability. With three zones for fitting, two disjoint zones for residual-strength selection, and router-untouched t5b5 for final reporting, CableMoE obtains 84.906% mIoU and 98.140 % overall accuracy. This is +10.000 points over SPT and +0.263 over probability mean; all three seeds improve the latter. Across pylon, conductor, structural-cable, and insulator classes, macro-IoU rises from 84.517% for SPT and 97.153% for probability mean to 98.144 %. The results support conservative residual composition, not a claim of a new segmentation backbone or universal state of the art

---


### 523. [MUNDO: a multiresolution generative framework for temporal downscaling](https://arxiv.org/abs/2611.30868)

**<font color=#1a73e8>作者：</font>** Aymeric Delefosse, Manon Tavernier, Julie Keisler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamical systems are often observed at coarse temporal resolution through sparse states or temporal aggregates, leaving the underlying fine-scale trajectories unresolved. Recovering these trajectories requires probabilistic models that capture the unresolved variability while remaining consistent with the observations. We present MUNDO (Multiresolution UNified DOwnscaling), a generative framework for temporal downscaling under general linear observation operators. MUNDO introduces a null-space parameterization that enforces exact observation consistency in a single network evaluation, unifying temporal interpolation and disaggregation. To capture complex multiscale dynamics, we leverage reverse Markov learning to factorize the observation operator into a hierarchy of successive coarsenings. Each level models only the degrees of freedom lost between adjacent resolutions. We evaluate MUNDO on two-scale Lorenz-96, four two-dimensional physical systems, and multivariate ERA5 reanalysis over Europe, for both temporal interpolation and disaggregation. Across datasets and tasks, MUNDO generally outperforms flow-based baselines. Single-step MUNDO achieves strong predictive skill, while recursive MUNDO generally improves temporal realism and ensemble calibration, with better spread-skill agreement and predictive coverage.

---


### 524. [XFreq: Geometry-Aligned Cross-View Residual Learning for Sparse 3D Ultrasound Reconstruction](https://arxiv.org/abs/2611.30869)

**<font color=#1a73e8>作者：</font>** Yuhuan Lu, P. Ellen Grant, Davood Karimi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional (3D) ultrasound provides valuable volumetric context for anatomical assessment, motivating reconstruction from widely available two-dimensional (2D) slices. Sparse slices leave much of the volume unobserved, even when their acquisition poses are known. Existing methods interpolate observed intensities or incorporate learned 2D image features into 3D reconstruction, but their complementary roles in predicting smooth structure and residual details remain less explored. We introduce XFreq, a geometry-aligned framework for sparse 3D ultrasound reconstruction. It uses known slice poses and finite footprints to query 2D image features at 3D locations, complementing splatted intensities and sampling geometry. A low-frequency decoder predicts a smooth 3D field from the splat representation, while a high-frequency decoder additionally incorporates the queried 2D features to predict residual details. A learned gating module regulates the residual contribution based on geometry and cross-slice feature variation. We evaluate XFreq on an in-house fetal brain dataset and the public CETUS cardiac dataset, using slices resampled from 3D ultrasound volumes and fivefold cross-validation. Among the compared methods, XFreq achieves the highest PSNR and SSIM in most settings across both datasets, reaching 26.82 dB PSNR on CETUS with 32 input slices. Ablation studies further show the contributions of local feature querying, geometric cues, and residual prediction, with gains generally increasing as more input slices are used. Our findings highlight the value of geometry-aligned cross-view feature integration for reconstructing 3D ultrasound volumes from sparse 2D slices.

---


### 525. [A High-Resolution UAV Benchmark Dataset and Baseline Evaluation for Teak Crown Segmentation in Western Ghats Tropical Forests](https://arxiv.org/abs/2611.30888)

**<font color=#1a73e8>作者：</font>** Anand S Sahadevan, Sunita Arya, Anup Kumar Das 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate teak-tree segmentation from high-resolution drone imagery is critical for sustainable plantation management, yet lacks dedicated benchmarks. We introduce TeakTreeNet, a comprehensive dataset and evaluation protocol for binary teak-tree segmentation at native 2cm resolution. Four state-of-the-art architectures: U-Net, PSPNet, DeepLabV3, and SegFormer were rigorously benchmarked across scratch and ImageNet-pretrained settings with three-seed reproducibility. SegFormer establishes new SOTA performance with F1 0.938 +/- 0.002 (Teak), IoU 0.968 +/- 0.001 (Teak), and Accuracy 0.986 +/- 0.001, outperforming all pretrained CNNs. Domain-adaptive training suffices, as the scratch SegFormer outperforms ImageNet pretrained baselines, avoiding large-scale pretraining overhead. Comprehensive analysis reveals Transformer's superior boundary delineation for dense plantation scenarios. TeakTreeNet provides researchers with 6391 expertly annotated drone patches (224x224) and establishes reproducible evaluation protocols, enabling direct comparison of future methods. Our benchmark demonstrates SegFormer's optimal balance of accuracy, efficiency, and deployability for operational forestry monitoring of teak plantations for India's western tropical forests.

---


### 526. [AeroJEPA: A Two-Stage Framework for Aerosol Forecasting with Joint-Embedding Predictive Learning](https://arxiv.org/abs/2611.30891)

**<font color=#1a73e8>作者：</font>** Zitong Shuai, Zengliang Zang, Chunlei Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aerosol forecasting requires integrating sparse ground observations and modeling meteorologically driven concentration evolution and spatial structure. However, analysis-initialized forecasts make limited explicit use of historical observations, while pointwise regression tends to smooth local variations and provides limited constraints on fine spatial structures. In this work, we propose AeroJEPA, a two-stage joint-embedding predictive framework for regional surface PM$_{2.5}$ forecasting. Specifically, Stage I fuses historical observations, model backgrounds, and meteorological information to predict an initial future state, meteorological conditions, and multi-scale structures. Morphology-guided encoding and joint-embedding predictive supervision support learning future spatial representations, supplementing concentration regression with structural constraints. Stage II uses predicted meteorology to guide state refinement and incorporates coarse- and fine-scale structures into state updates and decoding to generate the concentration field at a single future time step. Experiments show that AeroJEPA reduces gridded and independent-station RMSE by 17.23\% and 7.90\%, respectively, relative to PFGNet, while improving spatial consistency with analysis fields. In a 48 h recursive forecasting case study, AeroJEPA generally achieves lower RMSE and MAE than the numerical forecasts across the forecast period, indicating promising short- to medium-range forecasting performance.

---


### 527. [Speak When You See It: Proactive Task Assistants Should Wait for Evidence, Not the Clock](https://arxiv.org/abs/2611.30895)

**<font color=#1a73e8>作者：</font>** Bohe Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Proactive assistants that guide people through physical tasks must decide, every few seconds, whether a step is complete and whether a mistake has occurred. We find that two benchmarks for this task largely reward knowing when rather than seeing what: a timer that never looks at the video, raising an alarm at 25 s and confirming each step at 30 s, reaches a mistake F1 of 0.373 on Ego-MC-Bench, above every published result (at most 0.27). We formalize this as the video-blind frontier, the best trade-off between completion accuracy and mistake F1 that policies reach from the elapsed time, the instruction and training statistics alone: every published per-step result on Ego-MC-Bench lies inside it, and so do all twelve zero-shot models we run on QICD. To move beyond it, we introduce Evidence-Contrastive Training (ECT): fine-tune on the benchmark's own questions, and pair its positives with negatives from the same recording at the same elapsed time, so that elapsed time cannot separate the two sides of a pair. Trained on 209 QICD videos in about 15 GPU-hours, a 2B model with ECT crosses the frontier on both benchmarks in all four seeds; transferred to Ego-MC-Bench without adaptation, it confirms 59% of mistake-free steps in time, against 30% for a published model with the same backbone trained on about 25k synthetic counterfactuals and real recordings. Its decisions follow the video beyond what timing explains: at equal elapsed time it tells a finished step from an unfinished one in 90-92% of test pairs, where the instruction's typical duration reaches 65%, rescaling the time stamps between the frames leaves it essentially unchanged, and swapping in another recording, of the same recipe where one exists, cuts its completion accuracy by two thirds. The code and model weights will be publicly released.

---


### 528. [Predicting Rare-Mode Collapse in Recursive Generative Training from Single-Generation Calibration](https://arxiv.org/abs/2611.30897)

**<font color=#1a73e8>作者：</font>** Jingyao Zhang, Mingyu Du, Lu Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive generative training can preserve sample counts in a rare region while silently eroding its characteristic core. Mapping this finite-horizon collapse across real-data quotas, rare prevalences, and feedback perturbations via exhaustive multi-generation chains is computationally prohibitive. We develop a decoupled framework that forecasts multi-generation collapse probabilities and locates operating risk boundaries from independent single-generation conditional fits alone. Pairing an exact three-source multinomial count law with single-generation response banks propagates count marginals in closed form, backed by explicit calibration-error and boundary-resolution bounds. For additive Gaussian perturbations, we further prove that equal-variance all-row and sparse policies reverse their boundary-crossing order at a unique hyperplane distance. Across a 2,178-setting count benchmark, exact propagation cuts risk mean absolute error (MAE) from 1.85 to 0.49 percentage points (pp). Across ten two-dimensional learners, calibration achieves 2.60--5.69~pp six-round core MAE on nine stationary learners (65--81\% below an unperturbed baseline), diagnoses non-stationary outlier drift in standard DDIM (16.38~pp) via a stability probe, and resolves the predicted six-round geometric reversal. On Fashion-MNIST latent flow-matching chains, calibration outperforms direct-chain Gaussian-process interpolation at lower fit budgets and tracks the 20\% latent-perturbation boundary shift (3.14 versus 10.78~pp MAE for proportion copying) driven by opposing inflow to the rare region and outflow from its core.

---


### 529. [Do Waste Classifiers Recognise Items They Have Never Seen? Object-Disjoint Evaluation on Household and Medical Waste](https://arxiv.org/abs/2611.30911)

**<font color=#1a73e8>作者：</font>** Nusrat Jahan, Mst. Eshrat Jahan Esha, Masuma Sadia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic waste classification supports source separation, which enables recycling and keeps hazardous medical items out of household waste. Waste classification studies often report near-perfect accuracy on random image splits, which put photographs of one item in both training and test sets. To measure how well classifiers recognise items they have never seen, we built BanglaWaste-23, with 4,160 images of 172 objects in 23 household and medical waste classes from Bangladesh. Every image also records which physical item it shows. We evaluated 11 ImageNet-pretrained models and two models trained from scratch (a compact custom network and MobileNetV3-L) using object-disjoint five-fold cross-validation and a random split. On unseen objects, the best pretrained model reached a macro-averaged F1 score of 98.8%, and six models were statistically tied. The random split overstated from-scratch accuracy by 15 to 19 percentage points. The from-scratch models also missed 11 to 13% of medical items, against under 1% for pretrained models. On a second dataset from Dhaka, pretrained accuracy fell by 15 to 22 points. Classifiers should therefore be evaluated on unseen objects, with random-split results read as an upper bound. The data are on Zenodo and the code at this https URL.

---


### 530. [TrialAgentBench: Evaluating AI Agents for Clinical-Trial Analysis and Long-Horizon Drug-Development Decisions](https://arxiv.org/abs/2611.30916)

**<font color=#1a73e8>作者：</font>** Bradley Segal, William Bolton, Philip Torr 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical drug development is a long-horizon, high-stakes process requiring sequential decisions based on information that costs money and time to acquire. AI agents have demonstrated capabilities for scientific analysis, but there is no established way to evaluate them on these decisions, as real trials are expensive, involve people, and never reveal the counterfactual. We introduce TrialAgentBench, a benchmark for evaluating AI agents on clinical trial analysis and drug development decision-making using simulated trials where the truth is known, embedded within the data records of a fictional drug sponsor. We publicly release nearly 3,500 tasks, varying from analysing a single trial to managing multi-phase programmes with budget and time constraints. We score each analysis by rerunning its code on new trials, and each programme by the value its decisions achieve. Across 24 closed- and open-weight models, the strongest agents can analyse raw, messy trial records to within 6% of a process-aware analysis, even when an assumption is violated, with 95% confidence intervals containing the true effect 94--95% of the time. Over the prior year, the best model improved from 19% above this analysis, with serious misses on 15% of tasks, to 3.5% and 1%. What limits them is decision-making from evidence under uncertainty: when to correct, what evidence to buy, when to stop. The strongest agents are overly careful, correcting on 83% of tasks with equal recording errors, where it is unnecessary. On drug programmes, the best agent has substantial headroom, reaching 48% of the value an oracle achieves against 58% for a rule-based developer, with others falling 24 to 66% short. Model generations show ongoing improvements in handling data and evidence, with substantial variation. The strongest models can act as competent analysts, but do not yet make reliable long-horizon decisions.

---


### 531. [LimeTree: Linear-Memory Graph Neural Networks over Tree-Graphs for Resource-Efficient Language Modeling and Context Extrapolation](https://arxiv.org/abs/2611.30934)

**<font color=#1a73e8>作者：</font>** Elisabeth Fink  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The search for computationally efficient alternatives to the Transformer has yielded numerous architectures in recent years; however, most exhibit severe weaknesses in associative recall-such as key-value (KV) retrieval-and length extrapolation, where even standard Transformers struggle. This paper introduces LimeTree, a linear-complexity architecture in both memory and compute for sequence modeling. By integrating synthetic KV retrieval tasks directly into standard language modeling training, LimeTree achieves strong perplexity alongside reliable recall. Two variants were evaluated on WikiText-103 and PG-19 under strict compute constraints. On WikiText-103, LimeTree reaches a token-level perplexity of 19 in just 6 hours on four Quadro RTX 8000 GPUs, while maintaining 100\% KV retrieval accuracy even when extrapolating from a training context length of 512 to an evaluation length of 16,384. On PG-19, the model achieves a token-level perplexity of 13 in 35 hours on a single RTX PRO 6000 Blackwell GPU with minimal hyperparameter tuning. These results position LimeTree as a competitive linear-complexity alternative to Transformers, combining superior perplexity and training throughput with robust in-context retrieval and length extrapolation.

---


### 532. [FGSCalib: Targetless Camera-LiDAR Extrinsic Calibration from Foreground Segmentation](https://arxiv.org/abs/2611.30935)

**<font color=#1a73e8>作者：</font>** Marcell Kégl, Csaba Benedek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-LiDAR pairs installed as fixed infrastructure need periodic recalibration, but a calibration target takes the installation out of service. We present FGSCalib, a targetless method that calibrates a stationary camera-LiDAR pair from the objects moving in its view. We only assume that arbitrary moving objects are present in the scene: each sensor separates the moving foreground from the static background, without relying on object classes. With the correct extrinsic, the LiDAR foreground points project onto the camera foreground. FGSCalib turns the camera mask into a boundary-proximity field and finds the extrinsic by two-stage simulated annealing over selected frame pairs. It needs no measured initial extrinsic (random starts give similar results) and works with both rotating and non-repetitive LiDARs. We evaluate it on 21 simulated scenarios with exact ground truth and on 72 real ones (nine camera-LiDAR pairs in eight scenes), with a reference averaged from 43 manual calibrations. In simulation the median error is 5.3 cm and 0.19°. On real data we use a tolerance of 18 cm and 1.8°, met by 93% of single manual calibrations. Keeping the lowest-cost of five runs, FGSCalib meets it in 51 of the 72 scenarios: in 20 of 24 with the Livox, where the strongest of five baselines reaches 11, and in 31 of 48 with the two rotating LiDARs, where only one baseline estimate does. Its median error is 9.5 cm and 0.9°, against 7.3 cm and 0.7° for a single manual calibration. The code and the dataset are available online.

---


### 533. [SIAMBA: A Pseudo-Siamese Mamba-based Deep Learning Network for Multimodal Flood Change Detection](https://arxiv.org/abs/2611.30938)

**<font color=#1a73e8>作者：</font>** Muhammad Fasih Ishfaq, Giulio Weikmann, Lorenzo Bruzzone  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flood change detection from bi-temporal multispectral and synthetic aperture radar (SAR) images is essential for rapid disaster response. In this context, Sentinel-2 multispectral imagery provides discriminative spectral observations, whereas Sentinel-1 SAR provides weather-independent structural information. Using these modalities jointly requires modelling temporal evidence while accounting for cross-modal heterogeneity. In particular, change detection is complicated by cloud contamination, illumination variability, acquisition geometry and speckle, and heterogeneous land-cover responses. To address these challenges, we propose SIAMBA, a pseudo-siamese Mamba-based network for bi-temporal flood change detection from paired Sentinel-1 and Sentinel-2 observations. SIAMBA uses dedicated modality-specific encoders with dual-pooling squeeze-and-excitation recalibration and selective state-space processing for long-range spatial context. A gated cross-modal change module derives absolute, signed, and relative log-ratio differences at multiple semantic levels, and attention-refined skip connections support progressive multi-scale decoding. Experiments are carried out on OMBRIA benchmark, which includes an independent test set and geographically diverse subsets in France, Albania, Guyana, and Timor. SIAMBA achieves 81.98% IoU, and 93.57% OA on the independent test set, reaching the highest values in the considered comparison. It also provides the highest unweighted average IoU and OA across four regional subsets spatially disjuncted. These results indicate that combining selective state-space contextual modelling with gated multiscale discrepancy learning effectively improves flood change mapping across the evaluated geographic settings.

---


### 534. [Aggregation Rules Induced by KL-Regularised Preference Dynamics on Networks](https://arxiv.org/abs/2611.30941)

**<font color=#1a73e8>作者：</font>** Milan Vojnovic  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study agents that each align a model to their own preference data while observing one another, and ask which aggregation rule the resulting policies implement. Each round, an agent takes one KL-regularised step. The step involves a reference that the agent is penalised for leaving and a challenger against which its responses are compared, and each of the two may be the agent's own or an average over the agents it observes; attention need not be reciprocal. Aggregating the reference makes the rule collective. Agent $v$ then has the weight $\pi_v/\beta_v$, its share of the network's long-run attention divided by its temperature. If, in addition, the challenger is fixed, the agents concentrate on the response maximising $\sum_v(\pi_v/\beta_v)r_v(y)$, where $r_v$ is agent $v$'s reward, and the rule is cardinal. If the reference is fixed and the challenger aggregated, the agents' policies at a fixed point generally differ, and any weighted mean of them is an approximate maximal lottery whatever the weights, so the dynamics select no weighting. If both are aggregated, the rule is ordinal: averaged over rounds, the collective policy is a maximal lottery of the influence-weighted preference kernel, up to a slack that we bound. Where a collective rule exists, its weights depend only on the attention weights and the temperatures.

---


### 535. [Diffutoon-2: Toon Shading with Video Diffusion Models](https://arxiv.org/abs/2611.30945)

**<font color=#1a73e8>作者：</font>** Yuze Sun, Zhongjie Duan, Yingda Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Toon shading renders objects with a flat, stylized appearance. Diffusion models open a new route to this task by transforming photorealistic videos into an anime style. However, existing approaches often rely on curated source and style training pairs or additional visual references. Diffutoon avoids these requirements through structure guidance and colorization, but builds on an image diffusion backbone with short-window motion modules and repeated overlapping-window denoising. We present Diffutoon-2, a video diffusion framework that learns toon shading through animation reconstruction. Two complementary modules independently reconstruct animation clips from outlines and blurred colors, with the video backbone frozen. At inference, the modules jointly guide generation using the same types of conditions extracted from photorealistic footage, requiring neither cross-domain training pairs nor external style references. Extensive experiments demonstrate that Diffutoon-2 outperforms both general-purpose and domain-specific baselines, across quantitative metrics and human evaluation.

---


### 536. [Graph2Scene: Relation-Aware Text-to-Image Generation with Graph-Guided Diffusion Model](https://arxiv.org/abs/2611.30964)

**<font color=#1a73e8>作者：</font>** Peizheng Li, Xin Ai, Guanghui Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models still struggle with complex prompts containing many elements and interactions. Existing attention-control methods mainly focus on controlling where elements appear, but often ignore how objects interact with each other. As a result, relation tokens describing interactions between elements may assign high attention to irrelevant regions, leading to missing or incorrect interactions. In this paper, we propose Graph2Scene, a training-free framework that treats scene graphs as a core control signal for diffusion generation. It represents elements as nodes and their relations as edges, and translates these element-relation dependencies into selective attention guidance. It grounds each element to its corresponding region and guides relational interactions among the involved elements. To achieve appropriate relation control without over-constraining the generation process, Graph2Scene further adapts the control duration to scene complexity and progressively relaxes graph guidance during denoising. Experiments on T2I-CompBench and ConceptMix show clear improvements in compositional generation, especially for object relations. On ConceptMix, Graph2Scene improves relationship accuracy from 0.59 to 0.84 over the strongest FLUX.1-based regional-control baseline. Results on LongBench-T2I further show its advantage on long and complex prompts.

---


### 537. [Explanation Selection in Abductive Learning](https://arxiv.org/abs/2611.30970)

**<font color=#1a73e8>作者：</font>** En-Hao Gao, Yuan Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Abductive learning (ABL) offers a promising framework that connects machine learning and logical reasoning in a mutually beneficial loop. However, this bidirectional feedback can also reinforce incorrect concept semantics, since different interpretations of intermediate concepts may explain the same observed reasoning outcomes. Static analyses characterize this ambiguity but leave open which explanation training selects and whether its labels can still be corrected. We develop a dynamical analysis of a fixed-feature binary ABL model that links the local stability of competing explanations to differences in their concept labels. We prove that Gram matrices with identical spectra can select different explanations even under the same supervision, objective, and initialization. When any two compatible explanations differ in at least two labels, legal evidence above one half guarantees during training that admissible changes in optimization geometry preserve the selected explanation. Even when only the true explanation satisfies all constraints under a shared predictor, training can still converge to a finite attracting state whose hard predictions violate some constraints and mislabel concepts. Experiments on visual ABL tasks verify these predictions, including wrong attraction from random initializations under identifiable supervision, and show that in ordinary end-to-end training SGD and Adam select different explanations of the same supervision, while unseen concept accuracy drops relative to true-concept references as training concept errors grow.

---


### 538. [Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching](https://arxiv.org/abs/2611.30986)

**<font color=#1a73e8>作者：</font>** Yihong Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forward diffusion reinforcement learning (RL)---enabling deterministic ODE sampling without trajectory backpropagation---has grown increasingly popular for efficiently aligning diffusion models. However, we reveal that existing methods essentially rely on signed reward-weighted regression (RWR), regressing the \emph{trainable policy} velocity onto rollouts from a \emph{behavior distribution}. Unbiased baseline subtraction implicitly assumes that the policy velocity equals the behavior marginal velocity---an idealized assumption violated under classifier-free guidance (CFG) rollouts, offline/off-policy updates, and imperfect online self-consistency. This \emph{behavior--policy mismatch} breaks baseline invariance and injects \emph{baseline-induced gradient drift}, destabilizing training. To resolve this issue, we propose \textbf{I}nstantaneous \textbf{T}rajectory \textbf{D}istribution \textbf{M}atching (\textbf{iTDM}), taking the infinitesimal limit of Trajectory Distribution Matching toward a time-local reward-guided target via the posterior-score identity to yield a sample-level gradient anchored at the behavior velocity without learning an additional reward-tilted target score. Tracking this velocity with an online auxiliary denoiser guarantees exact baseline invariance at the auxiliary optimum, effectively suppressing baseline drift across both online and offline RL. Extensive experiments across compositional generation, text rendering, and preference alignment show that iTDM achieves state-of-the-art in-domain and out-of-domain performance. Notably, on the challenging GenEval2 benchmark, iTDM converges nearly $3\times$ faster than competing methods while scaling smoothly to $0.87$ without collapse. Code is available at this https URL

---


### 539. [CenShaper: Shaping Proxy Traffic for Censorship Circumvention](https://arxiv.org/abs/2611.31016)

**<font color=#1a73e8>作者：</font>** Shabbir Hussain, Aaron Ortwein, Roya Ensafi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern commodity DPI systems are capable of analyzing packet sizes, directions, and timings to detect circumvention tools even when those tools use sophisticated obfuscation. The anti-censorship community has called for innovation in traffic shaping and built an ecosystem that facilitates the adoption of new shaping techniques. However, a fundamental gap is halting progress: \textit{what} should circumvention traffic look like? Past experience with traffic shaping has underscored that effective shaping must produce traffic that looks like legitimate Internet traffic while limiting the ability of censors to identify multiple proxies through shared fingerprints.
In this paper, we use our access to large-scale real-world TLS traffic at a regional ISP to analyze approximately 12 million connections, finding that individual servers differ substantially from the broader TLS population and that traffic patterns vary across services. Combining these empirical observations with past experience with traffic shaping, we build CenShaper, which shapes each proxy's traffic to look like a selected TLS server. To reproduce these server-specific patterns, CenShaper trains a shared generative model using traffic from TLS connections to many servers and adapts it for each proxy using a small sample of recorded connections to its selected server. Our model evaluation shows that fingerprints learned from known proxies transfer poorly to proxies imitating previously unseen TLS services. In end-to-end testing, CenShaper reduces the detection rate of TLS-over-TLS fingerprinting from over 85\% to approximately 3\% at a 1\% false positive rate. Finally, we show how running CenShaper as a sidecar process simplifies integration with existing circumvention tools, making it a practical defense against increasingly powerful traffic analysis attacks.

---


### 540. [WildAnySplat: Feed-Forward 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2611.31023)

**<font color=#1a73e8>作者：</font>** Richard Shaw, Arthur Moreau, Athanasios Papaioannou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present WildAnySplat, a feed-forward 3D Gaussian Splatting framework that enables robust novel-view synthesis from in-the-wild multi-view images. Unlike controlled captures, real-world images often contain multi-view inconsistencies caused by transient occluders, illumination changes, and camera ISP, which degrade the quality of existing feed-forward reconstruction methods.
To address this challenge, we introduce a student-teacher framework that learns transient-robust and appearance-consistent 3D representations. A teacher network operates on clean images, while a student processes the corresponding in-the-wild inputs. The teacher provides clean supervision to guide the student toward a consistent canonical representation. Since paired clean and in-the-wild data are scarce, we use a hybrid data strategy, combining real paired captures, synthetic augmentations, and pseudo-clean labels generated from optimization-based reconstructions, bridging the domain gap between synthetic and real-world data.
We adopt a transformer architecture with dedicated DPT heads for camera pose, depth, and Gaussian prediction. We additionally predict per-view transient masks to reweight photometric supervision and suppress unreliable Gaussians. To account for cross-view appearance variation, we incorporate a bilateral grid module that models per-image color transformations and enables recovery of a canonical radiance representation.
Experiments on challenging in-the-wild benchmarks show that WildAnySplat improves robustness to transient occlusions and appearance variation while retaining the fast inference of feed-forward Gaussian Splatting.

---


### 541. [Token Pruning Needs a Protected Sink Token: Coherent Spatial Aggregation in Vision Transformers](https://arxiv.org/abs/2611.31025)

**<font color=#1a73e8>作者：</font>** Julian Wyatt, James Willoughby, Allison Clement 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) are a predominant architecture for computer vision, with token reduction emerging as a popular paradigm to improve their efficiency. Prior work compares reduction algorithms, but not how models respond to them, nor how their response changes with model depth. We propose Monte Carlo Token Pruning (MCTP), which estimates each token's impact on the prediction when tokens are explicitly removed during the forward pass. Applying MCTP to recent pretrained models, we observe that most, such as DINOv3, maintain a similar ranking of token importance at every depth (high Coherent Aggregation), while SigLIP 2 does not. This coherence requires predictions to survive pruning, which depends on keeping high-norm "sink" tokens: prefix tokens are kept by design, while prefix-free SigLIP 2 forms them on patch tokens, which pruning may remove. We show that in removing DINOv3's prefix tokens, its predictions and coherence collapse, while protecting only 5 tokens for SigLIP 2 cuts the token impact outside the object's bounding box by up to 62%. Beyond this, MCTP offers a post-hoc method to evaluate how a pretrained ViT responds to pruning, and suggests that token reduction methods should keep "sinks".

---


### 542. [ComputeWise: Measuring and Fixing GPU Waste by AI Research Agents](https://arxiv.org/abs/2611.31027)

**<font color=#1a73e8>作者：</font>** Egor Pakhomov, Nina Pakhomova, Anurag Koul 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are given GPUs to do AI research on their own. Do they use those GPUs well? A busy GPU does not tell us, because it can be busy with work the answer did not need. This matters, because the tokens the agent spends cost almost nothing next to the GPUs its experiments run on, so using those GPUs better has a huge impact. So we built ComputeWise, an open benchmark of research tasks on which this waste can be measured and reduced. For it we developed our own simulated GPU, which replays recorded runs to the agent's code. With no real GPU needed, we ran hundreds of experiments, far more than would be reasonable on real GPUs. With no help, the agents put only 52% of their GPU time into work the answer needed. Another 22% went to work it did not need, and 26% sat idle. Asking the agent to finish the work faster, telling it to keep every GPU busy, or giving it a job scheduler does not fix this. So we built an open-source harness, part prompting and part deterministic code. Across five models, it removed over 80% of the extra time to the answer.

---


### 543. [Black-Box Comparator-Adaptive Network Regret](https://arxiv.org/abs/2611.31032)

**<font color=#1a73e8>作者：</font>** Tomas Ortega, Hamid Jafarkhani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study comparator-adaptive decentralized online learning with network regret, which evaluates each node's prediction on the loss of every node in the network. We show that existing gossip-based algorithms are fundamentally limited for this task, and cannot achieve sublinear network regret with only one gossip step per decision round. To prove this, we construct a two-node counterexample, which shows that gossip-based algorithms can produce exponential regret despite bounded disagreement, resolving a previously open question in the literature. We then introduce a black-box reduction, which uses local learners with sublinear comparator-adaptive regret to obtain sublinear comparator-adaptive network regret. Each node exchanges predictions with its neighbors once per decision round, and a universal choice of edge weights works on every connected undirected graph without graph preprocessing. We also characterize admissible edge weights and show how weights adapted to the graph improve the regret bound. For example, for the complete graph, this improvement is quadratic in the number of nodes. Experiments on synthetic and real-world data illustrate the counterexamples we propose and compare the reduction with decentralized baselines.

---


### 544. [Déjà VAE: When Do Autoencoder Traces Reveal Generated Images?](https://arxiv.org/abs/2611.31036)

**<font color=#1a73e8>作者：</font>** Saugat Pandey  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A latent diffusion model's output has already passed through its autoencoder, so a second round trip changes it very little. This "déjà vu" underlies reconstruction-based detectors of generated images; we analyse when it reveals a generated image and when it does not. Read by a frozen vision foundation model without training, the trace is strongest in intermediate layers, and, unlike pixel-level reconstruction error, it treats blur as a sign of a real image. It belongs to the generator's exact decoder: on Synthbuster, the exact decoders of Stable Diffusion 1.3, 1.4, 2 and XL are the strongest of eight autoencoders and catch 94-100% of their generators' images at a 5% false-alarm rate (SDXL's version identified post hoc), while near-identical versions catch 7-42%. A detector trained only on real photographs and their autoencoder copies matches one trained on 162k generated images on GenImage (+2.3 points, 95% CI [0.9, 3.7]) and complements it in fusion, but one resize with JPEG re-save, or a mild blur, costs it 19-27 points. Two lessons concern benchmarks. The in-the-wild benchmark Chameleon can be solved from image width alone. And on Synthbuster, how the real photographs are matched to the generated images' size decides whether our detector leads or trails (+4.4 or -9.7 points): the matching protocol alone can reverse a detector comparison. Code and per-image scores: this https URL

---


### 545. [UMAMI: A Multimodal Benchmark Dataset for Evidence-Grounded Dietary Decisions](https://arxiv.org/abs/2611.31068)

**<font color=#1a73e8>作者：</font>** Safal Thapaliya, Jiatan Huang, Debapriya Chatterjee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dietary decisions require identifying a food's nutrient content and considering individual dietary needs, but recognizing food from an image alone does not provide this information. Visually similar foods can have different nutrient profiles, so selecting the wrong food record can lead to incorrect decisions even when nutrient rules are applied correctly. Furthermore, satisfying nutrient constraints does not necessarily establish a food's relevance to a person's intake. Evaluating these challenges together requires connecting food images, nutrient records, and individual intake histories. To support this evaluation, we introduce UMAMI (Unified Multimodal Assessment of Meals and Intake), a multimodal dataset and benchmark linking independently collected food images with nutrient profiles and respondent health and intake records. Using this dataset, we construct three diagnostic tasks covering visual nutrient question answering, personalized food recommendation, and condition-aware food substitution. Paired instances and input controls examine how visual identity and respondent context affect decisions. Our experiments identify errors in both food-record selection and nutrient-rule application, while showing that higher rule compliance does not necessarily improve alignment with subsequent recorded intake. These findings highlight the need to evaluate how multimodal systems select and use structured evidence for dietary decisions. The dataset, code, and dashboard are available at this https URL.

---


### 546. [AlphaDefect: Expert-Level AI for Slay the Spire 2](https://arxiv.org/abs/2611.31076)

**<font color=#1a73e8>作者：</font>** Qiyue Chen, Taian Yu, Junpei Komiyama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Slay the Spire 2 (STS2) is a single-player deck-building game that requires long-term planning under heavy randomness. We present AlphaDefect, an expert-level AI system for STS2: for each character, one network trained with proximal policy optimization (PPO) makes every decision of a run, in combat and outside it. At the highest difficulty, Ascension 10, on two versions of the game current in November 2026 and on test seeds not played in training, AlphaDefect wins 62-77% of runs across six characters with greedy play and 68-80% with test-time search, after 1.3 to 6.7 billion decisions of training per character; runs uploaded by human players of all levels are won 11-20% of the time at the same difficulty. The networks read the game as entity records that identify each card, relic and enemy through a learned embedding and attributes from the game data, together with consequences of public information computed by the engine. Ablations show how much the agent depends on this encoding: without these identities, the network did not win a single run, and without the computed consequences it won 8.3 points fewer. To our knowledge, AlphaDefect is the strongest publicly reported STS2 agent as of November 2026.

---


### 547. [Leakage-Safe Auditing of Attribution-Driven Data Curation in Medical Imaging](https://arxiv.org/abs/2611.31096)

**<font color=#1a73e8>作者：</font>** Malay Phadke, Akshay Gokhale  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When can an attribution-derived anomaly justify changing a medical-imaging training set? We formulate attribution-driven curation as three separately testable claims: anomaly detection, harmfulness estimation, and intervention utility. We test the first and third using a patient-disjoint, identifier-preserving audit of a 3D convolutional classifier for computed tomography angiography aneurysm candidates. We identify 232 exactly zero-valued arrays among 1,201 positive patches, including 170 training positives, and invalidate a historical 321-patch attention-failure subgroup whose identifier-free records were joined to files by position. On the held-out test set, GradCAM++ spatial concentration is central for every candidate class, reversing the historical pattern. GradCAM++ and Integrated Gradients show negative rank-order agreement for positives, limiting method-independent anatomical interpretation. Across five paired training seeds, removing the 170 corrupted training positives yields AUC 0.9617 +/- 0.0044 versus 0.9652 +/- 0.0039 for full-data training (difference -0.0035; 95% CI -0.0082 to 0.0007). Excluding 34 raw-zero test positives widens rather than closes the gap, countering a blank-memorization explanation. Budget-matched random-removal controls suggest the result is not simply an effect of reducing training size. Input corruption does not necessarily imply that deletion improves generalization. Our framework makes leakage control, sample identity, and intervention testing explicit in attribution-driven medical-imaging data curation.

---


### 548. [SayWhen: Set-Valued Semantic Commitment for Low-Regret Early Speech](https://arxiv.org/abs/2611.31101)

**<font color=#1a73e8>作者：</font>** Tianyi Huang, Lucas Su, Fred Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speaking early turns a prediction into an irreversible public commitment. We introduce SayWhen, a test-time controller that selects a task-directed act shared across typed continuation plans and controls its release as speech. A persistent veto blocks playback when intervening transcripts invalidate the candidate. We define regret-free early speech (RFES) to measure supported pre-endpoint releases without scored incompatibility. On a 72-prefix branching diagnostic, the generated-plan frontier attains 6.0% RFES with zero observed mean regret, versus 8.2% RFES and 0.068 regret for Matched Top-One. Measured planner latency constrains this path; a deterministic retail schema attains 31.7% RFES, compared with 32.0% for the complete policy. In a separate 30-task $\tau$-Voice simulation, schema-derived candidates with cached text-to-speech (TTS) audio attain 21/30 task-level RFES. Eligible audio begins 1.51 seconds before the user-audio endpoint among the 22 tasks with early speech, or 1.11 seconds over all 30 tasks with zero for tasks without eligible early speech. Semantic veto and endpoint waiting each pass 16/30 tasks. Together, the studies demonstrate a controlled coverage-compatibility trade-off and schema-based pre-endpoint operation, making the supported public commitment an explicit unit of voice-agent control.

---


### 549. [Preflight: Agentic Last-Mile Verification for AI Software Supply Chains](https://arxiv.org/abs/2611.31110)

**<font color=#1a73e8>作者：</font>** Yaman Jandali, Nojan Sheybani, Farinaz Koushanfar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Software dependencies execute within the trust boundary of downstream applications, yet provenance, static analysis, and package-level behavioral approaches do not directly determine how a released artifact behaves for a specific program. We present Preflight, a program-scoped pre-execution verifier for Python dependencies that extracts application-referenced symbols, iteratively synthesizes and validates function-level harnesses, executes resolved artifacts in a restricted environment, records behavioral fingerprints, and compares target behavior against prior versions when suitable baselines exist. We evaluate Preflight on four real software-supply-chain incidents under five application contexts, a 100-package benign corpus, and a controlled function-level versus import-only ablation. Preflight returns malicious verdicts in four incident contexts and a clean verdict in the LiteLLM client context, where the affected proxy-server path is not exercised. All 100 evaluated benign packages receive clean verdicts, with zero observed false positives. In a controlled ablation on Ultralytics and ctx, function-level harnesses expose malicious behavior in both incidents, whereas import-only probing exposes neither. Together, these results show that conditioning behavioral verification on the downstream program can expose security-relevant dependency behavior while remaining selective on benign workloads.

---


### 550. [Attention Temperature Confounds Zero-Shot Context Extension](https://arxiv.org/abs/2611.31113)

**<font color=#1a73e8>作者：</font>** Ruben Navasardyan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A training-time attention change is usually judged for zero-shot context extension against a dense baseline beyond the training length at the default temperature, $\tau = 1$. The outcome depends on how miscalibrated the baseline is there: the share of perplexity it recovers when its logits are sharpened by one scalar. Under the standard recipe (fp32 master weights), an 8k-trained baseline is 8-15% miscalibrated at 30k in three seed-paired 365M twins; in one of them this makes the block-sparse-trained twin look 7% better, which calibration removes. In pure-bf16 training without master weights the miscalibration is several times larger: an AdamW step ($\beta_2 = 0.95$) on a gain initialised at 1.0 is below half the bf16 spacing at peak learning rates under $1.7\times10^{-3}$, so gains never move (22 checkpoints), the baseline is 37-58% miscalibrated, and block-sparse pretraining, attention dropout and ALiBi look 6-35% better. Calibrating one temperature per model and length removes all three advantages, leaves ALiBi 5% behind RoPE and keeps part of the gain of a positive control, NTK-aware scaling. Unfreezing the gains reverses the block-sparse advantage at 365M and removes 71-89% of it at 1.2B. We recommend reporting extension results at calibrated temperatures and checking that normalisation gains moved.

---


> [!TIP]
> 当前位于：**501-550**（第 11/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-569](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
