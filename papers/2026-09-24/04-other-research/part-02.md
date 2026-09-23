# 📦 其他研究 | 2026年09月24日

> 本类共 **275** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-275](./part-06.md)

---

### 51. [Mean Velocity Matching: Rethinking Generative Dynamics in Diffusion Models](https://arxiv.org/abs/2609.25444)

**<font color=#1a73e8>作者：</font>** Yunhong Zhang, Changjie Cao, Zhihua Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work studies prediction parameterization for stochastic generative dynamics in diffusion models. Existing velocity-based generative models provide the simplicity of learning a single transport field, but their standard formulation is deterministic, whereas stochastic extensions generally require additional score information or an intermediate velocity-to-score reconstruction. To retain single-field prediction while directly supporting stochastic reverse dynamics, this paper introduces Mean Velocity Matching (MVM). MVM constructs a Gaussian perturbation process for which the conditional expectation of a restoration-oriented velocity, $(x_0-x_t)/t$, directly forms the reverse-SDE drift. Consequently, a single learned field is sufficient to parameterize the stochastic reverse process without separately estimating or reconstructing the score. Because direct regression of this velocity becomes unbounded near $t=0$, MVM further introduces a $\sqrt{t}$-scaled parameterization that preserves the reverse dynamics while yielding a bounded training target. The same learned field also induces a deterministic probability-flow ODE, enabling stochastic and deterministic sampling to be studied within a unified formulation. Experiments with Transformer-based generative models achieve an FID of $\MVMImageNetThirtyTwoFID$ at \MVMImageNetThirtyTwoNFE\ NFE on ImageNet $32\times32$ and $\MVMImageNetTwoFiftySixFID$ at \MVMImageNetTwoFiftySixNFE\ NFE on ImageNet $256\times256$. Controlled SDE--ODE comparisons further show that the ODE performs better under very low NFE, whereas the stochastic reverse process achieves lower FID when sufficient function evaluations are available. These results demonstrate that MVM provides a direct single-field parameterization of stochastic reverse dynamics while maintaining competitive generation quality.

---


### 52. [Combinatorial Network-Based Manifold Topological Deep Learning for Image Analysis](https://arxiv.org/abs/2609.25453)

**<font color=#1a73e8>作者：</font>** Alice Wachira, Xiang Liu, Zhe Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image analysis remains fundamentally challenging because of the intricate geometric and topological structures present in medical data. Conventional convolutional neural networks model images as regular Euclidean grids, limiting their ability to preserve geometric relationships and higher-order structural information. Recently, manifold topological deep learning (MTDL) has emerged as a promising paradigm that integrates deep learning with geometric and topological representations. Nevertheless, existing methods have not yet fully exploited discrete manifold structures within combinatorial complex neural networks. To bridge this gap, we introduce CNMTDL, a MTDL framework that integrates Hodge decomposition with a combinatorial attention mechanism. In our approach, medical images are represented as discrete manifolds and decomposed into three Hodge components. Features extracted from these components are concatenated and embedded into a combinatorial complex architecture, enabling enhanced higher-order message passing between $0$-cells and $2$-cells through attention-based blocks. We evaluate CNMTDL on six two-dimensional and three-dimensional datasets from the MedMNIST v2 benchmark, demonstrating its effectiveness for medical image analysis.

---


### 53. [MIND the Gap: A Geographic Implicit Neural Representation with Adjustable Spatial Scale](https://arxiv.org/abs/2609.25454)

**<font color=#1a73e8>作者：</font>** Isaac Corley, Arjun Rao, Esther Rolf 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geographic measurements are often sparse, leaving large areas without labels for the quantities we want to map. Geographic implicit neural representations (INRs) address this by learning smooth, general-purpose embeddings that can be queried at any coordinate. Downstream models combine these embeddings with sparse labels to predict target values at unsampled locations without satellite imagery at inference. However, generalization to distant regions remains largely unexplored, despite its importance for remote sensing applications. We introduce Matryoshka Implicit Neural Distillation (MIND), which distills embeddings from specialist pretrained geospatial models into a single generalist coordinate embedding with adjustable spatial granularity. MIND uses nested supervision at several embedding dimensions, which define a series of contiguous chunks. In our experiments, early chunks capture coarser geographic variation, while later chunks add more fine-grained details. A downstream predictor can retain only leading chunks or be fitted with our Chunked Penalty to downweight later chunks while keeping the full embedding, without retraining the INR. To measure MIND and compare to existing approaches around the world, we introduce CoordBench, a large-scale INR evaluation suite of $52$ datasets and $78$ targets that aims to test both local interpolation and prediction in held-out regions at various spatial scales. MIND and its Chunked Penalty variant achieve the highest aggregate regression and classification scores among tested INRs, and the highest scores overall under regional holdout, setting a new state-of-the-art for geographic INRs.

---


### 54. [Real-Time Hand Gesture Recognition for OpenXR Using Transformer-Based Machine Learning](https://arxiv.org/abs/2609.25466)

**<font color=#1a73e8>作者：</font>** Salar Rezayani, Russell Butler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hand gesture recognition is a key component in human-computer interaction (HCI), enabling intuitive interfaces for applications in gaming, virtual reality (VR), robotics, and more. This study integrates transformer-based machine-learning models for real-time hand gesture recognition, using hand-tracking data captured through the OpenXR standard in Unity. We leverage positional data of hand joints and wrist rotation angles to train a custom gesture recognition system. By utilizing the sequential modeling capabilities of transformers, the system captures temporal dependencies within short gesture windows and classifies gestures robustly across hand orientations and sizes. The results show a significant improvement in gesture classification accuracy. Building on this, we outline how the approach can be extended toward detecting the flow of movement, i.e., the transitions between gestures, as future work.

---


### 55. [ShowTellArena: Evaluating Business Workflow Understanding from Demonstrations](https://arxiv.org/abs/2609.25467)

**<font color=#1a73e8>作者：</font>** David Garg, Ritobrata Sarkar, Ehsan Azarnasab 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We often teach a colleague by showing the work and explaining the decisions as we go. How can we check what an agent understood from the same lesson? We introduce ShowTellArena, a benchmark protocol and public dataset for comprehension after narrated business demonstrations. The v1.0 release contains 50 business workflow tasks, with recordings, screenshots, narration, fixture seeds, and 502 questions. Tasks span finance, hiring, procurement, customer decisions, inventory, and logistics. The protocol holds the business scenario and quiz fixed while allowing each product to capture the lesson through its own teaching interface. Questions test operational rules, boundaries, exceptions, and errors in proposed automations. We analyze 218 selected pilot attempts across 39 workflow cases, including 28 cases attempted by all three evaluated systems. These exploratory results expose both answer errors and failures to complete the teaching experience. We describe the release's verification gaps and the pilot's uneven coverage, exclusions, and grading provenance. The contribution is an inspectable dataset and assessment workflow that others can extend; the selected pilot is not a controlled product ranking.

---


### 56. [A Practical Recipe for Semi-Supervised Federated ASR: Online Pseudo-Labels with Server Update Stabilization](https://arxiv.org/abs/2609.25471)

**<font color=#1a73e8>作者：</font>** Wonho Bae, Zakaria Aldeneh, Martin Pelikan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised federated learning (SSFL) trains models on clients' unlabeled data using a teacher to generate pseudo-labels, with a small labeled seed dataset on the server. Automatic Speech Recognition (ASR) is particularly fragile here: pseudo-label errors compound across the output sequence and across training rounds into divergence, leaving a large gap to fully-supervised FL. We show that closing this gap turns on two coupled design axes -- the teacher (which model generates the pseudo-labels) and the anchor (the server-side updates on labeled data that stabilize training). On the teacher axis, a per-client online teacher (each client's own evolving model) diverges on its own, but once stabilized it matches or beats the broadcast global teacher (one server model, fixed within a round) -- decisively in-domain and competitively under domain shift. As the seed grows stronger and the online teacher's advantage narrows, a transitioning teacher (global $\rightarrow$ online at round $r$) matches or beats both. On the anchor axis, the server must keep training on labeled data between rounds -- otherwise the online teacher drifts -- and this interleaving, more than the seed model, governs convergence. The two axes are inseparable: aggressive teacher choices pay off only once the anchor stabilizes training, which is highly sensitive to data augmentation and batch size -- the settings that govern how much input and gradient noise the server injects. How much stabilization is needed is domain-dependent, governed by the dispersion of the seed data and its overlap with client data. These findings yield guidelines for SSFL in ASR training, improving over the strongest prior method on 9 of 11 pairs, by $20.8\%$ on average in-domain and $10.0\%$ cross-domain, narrowing the gap to fully-supervised FL.

---


### 57. [Learning Defensive Policies against Diverse Inference Attacks for Smart Meter Privacy](https://arxiv.org/abs/2609.25484)

**<font color=#1a73e8>作者：</font>** Ruichang Zhang, Mustafa A. Mustafa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smart meter (SM) data provides fine-grained visibility into household energy consumption, but also exposes users to privacy risks. Inference attacks, known as non-intrusive load monitoring (NILM), can perform appliance-level inference from aggregate signals and recover sensitive behavioral patterns. In practice, attacker models are unknown and heterogeneous, making robust defense challenging. We formulate SM privacy protection as a black-box inference defense problem, aiming to reduce the recoverability of appliance-level information while generalizing across diverse and unseen attackers. We propose a proxy-guided hierarchical reinforcement learning framework that learns battery-based load-shaping policies to inject realistic but misleading appliance-level signatures into the aggregate signal, thereby disrupting the structured patterns exploited by NILM. A self-supervised aggregate-structure privacy probe provides a reconstruction-error-based surrogate reward for disrupting recoverable load structure, while a signature library makes the perturbations appliance-relevant and physically realizable through battery control. We provide theoretical rationale showing that proxy-guided optimization improves inference robustness under attacker diversity. Experiments on real-world datasets UK-DALE and REDD demonstrate strong cross-model and cross-appliance generalization. Across six unseen NILM attackers, covering four appliances on UK-DALE and five on REDD, our proposed defense increases average appliance-level RMSE by 107% and 166%, respectively, while reducing F1 score by 79% and 80%.

---


### 58. [Identifying Suspected Mislabeled Apps in Google Play Application Removal Prediction: An Empirical Comparison of Label Noise Detection Methods](https://arxiv.org/abs/2609.25487)

**<font color=#1a73e8>作者：</font>** Deborah Dobles Montalvan, F. Mohsen, H. de Weerd  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Models that predict which Google Play apps will be removed are trained on labels that record only whether an app was still in the store at a later observation. A disappeared app is labeled removed and a present one stable, but neither records why. A voluntary withdrawal and a policy takedown both produce removed, and an uncaught spam app keeps stable. This work calls that mismatch label noise. Three detectors from different methodological families are applied to the 870,514 apps of Mohsen, Karastoyanova, and Azzopardi (2022): Isolation Forest, flagging apps unusual in the feature space, Neighborhood Disagreement, flagging apps whose nearest neighbors carry the opposite label, and Prediction Inconsistency, flagging apps a classifier labels differently from the data. The apps flagged by all three, the overlap, number 7,598 at default settings and are the strongest mislabeling candidates. Two questions follow. First, does removing flagged apps improve the model? It does not. No detector, overlap, or union beats the baseline, and the loss grows with the number removed. Second, do flagged apps appear less often than expected among apps whose label VirusTotal and Quark Engine confirm? Among confirmed removals they do, falling to 0.43 times the expected rate as the threshold tightens, while an excess on the stable side disappears once the age of the scanned apps is accounted for. A model trained on only the 3,021 trainable overlap apps reaches a test AUC of 0.2518, far below chance, so the relationship between features and labels there runs opposite to the rest of the data. The flagged apps run wrong in both directions: abandoned apps that resemble spam carry stable, while apps that look healthy carry removed. The value of the detectors lies in characterizing this label noise. They locate a small set of candidates they cannot profitably remove.

---


### 59. [SAM-V: Geometry-Aware Segment Anything for Multi-View Instance Segmentation](https://arxiv.org/abs/2609.25490)

**<font color=#1a73e8>作者：</font>** Jiangshan Gong, Yuqun Wu, Qiqian Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Consistent multi-view object segmentation is critical for 3D perception and robotics, yet remains challenging under severe viewpoint and occlusion changes. Existing methods typically perform 3D instance segmentation on point clouds or rely on offline 2D mask-matching pipelines. However, 3D instance segmentation is limited by scarce 3D annotations, while offline 2D matching suffers from object identity ambiguity across frames. To leverage strong 2D and 3D priors jointly, we propose SAM-V (Geometry-Aware Segment Anything for Multi-View Instance Segmentation). Instead of combining the two priors through post-hoc matching, SAM-V directly integrates features from a feed-forward geometry model (VGGT) into a 2D segmentation foundation model (SAM), trained end-to-end for cross-view instance prediction. SAM-V introduces a prompt-fusion mechanism that enriches sparse SAM prompt tokens with view-specific camera tokens and local VGGT features, making the prompt representation both view-aware and spatially grounded, together with a mask decoder that attends to dense 2D and 3D features. By conditioning the mask decoding directly on multi-view geometry, SAM-V produces consistent multi-view segmentation of a prompted object in a single forward pass without offline mask matching or explicit 3D reconstruction. On the IGGT 3D tracking benchmark, where consistent instance identity across frames directly determines performance, SAM-V improves overall IoU by 5 points and frame-level recall by 12 points on the ScanNet++ split over the state-of-the-art multi-view instance segmentation baseline and leads on all metrics in the zero-shot ScanNet split. Our code and pretrained models are available at this https URL.

---


### 60. [Queer inclusion in speech datasets: An audit and taxonomy of practical tensions](https://arxiv.org/abs/2609.25491)

**<font color=#1a73e8>作者：</font>** Brooklyn Sheppard, Anaelia Ovalle, Adina Williams 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we examine speech datasets for their inclusion of LGBTQIA+, or queer, voices and provide a taxonomy of tensions to better understand why there is a lack of such voices in current speech technology datasets. Through an audit of six diverse speech datasets, we find that measurable queer representation is low (0-1.4% of speakers) - insufficient for robust disparity measurement. We take this community as a case study to consider what challenges and tensions are associated with collecting speech data from marginalized communities. For comparison, we audit an additional two datasets from the speech sciences that were created by, for, and with the queer community. We note that many customs in speech dataset collection efforts in AI and speech technology research may conflict with values emphasized in participatory approaches with marginalized communities, and provide a taxonomy describing these tensions.

---


### 61. [Towards participatory speech dataset curation: A queer case study and conceptual framework](https://arxiv.org/abs/2609.25496)

**<font color=#1a73e8>作者：</font>** Brooklyn Sheppard, Anaelia Ovalle, Adina Williams 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we motivate the need for a participatory speech dataset creation framework through a case study of the LGBTQIA+, or queer, community - a community with documented concerns about AI and reported harms, including attempts to develop 'gaydar' technologies that purportedly identify individuals as queer. We review common speech data collection practices, why these methods may be unsuitable for engaging with queer speakers, and discuss previous efforts in participatory AI with queer community engagement, as well as participatory endeavours specific to speech data collection for other marginalized communities. From this review, we develop a conceptual framework for participatory speech data curation by, for, and with marginalized communities drawing on insights from co-design and knowledge sharing. We propose a framework comprising overlapping and two-way processes of defining a community, project formulation, modes of participation, and personal autonomy.

---


### 62. [mbariml: a curation pipeline for turning deep-sea imagery and video into object-detection training data](https://arxiv.org/abs/2609.25500)

**<font color=#1a73e8>作者：</font>** Lonny Lundsten, Kevin Barnard, Dave Caress  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training data quantity and quality greatly affect object detection model performance, regardless of model architecture. When using object detection models on video and images from the deep sea, in which the objects of interest, primarily organisms, are sparse, faint, and hard to identify, incremental improvements to object detector performance may require an iterative approach to data labeling and management. This paper presents mbariml, a python-based video and image analysis pipeline built around the data labeling management process. mbariml uses an Ultralytics YOLO detection model, runs it over still images or video, stores every detection as a reviewable region of interest, groups those regions by visual similarity so that a human can accept or reject them in bulk, and exports the result as training data, statistics, image sidecars, and additional metadata. The human review stage is the centre of the design: an annotator can validate, relabel, resize, delete, and draw entirely new localizations, and every one of those edits is written back to the same database the detector wrote to. Video receives particular attention: the software treats each tracker-produced track as a provisional observation and selects one representative frame instead of retaining every detection in the track. We describe the pipeline stage by stage, including the operational middle-third heuristic used for track observation selection.

---


### 63. [Continuous Optimization for p-adic Models](https://arxiv.org/abs/2609.25501)

**<font color=#1a73e8>作者：</font>** Julian Salazar, Dimitri Kanevsky, Matt Harvey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present the first method for native, continuous gradient descent for machine learning models with $p$-adic parameters. Existing native optimizers are discrete, mostly combinatorial searches, as the $p$-adic numbers $\mathbb{Q}_p$ are totally disconnected, with standard losses that are flat away from their minima. To enable continuous optimization, we propose working with $\mathbb{Q}_p$ via its Berkovich affine line: a canonical, path-connected expansion of $\mathbb{Q}_p$ that preserves its isometries and uniquely extends its analytic maps. This hull is a metric tree with interpretable points and local derivatives, which we show enables effective optimizers and backpropagation. We formulate gradient descent and show that its approximations efficiently learn linear models with coefficients in $\mathbb{Q}_p$ to do modular arithmetic, an XOR-like task not expressible by linear models in $\mathbb{R}$. We also demonstrate momentum and Adam variants, linear regression, and classification on binary-encoded hierarchies (Quillian semantic networks), addressing open problems posed by Martins (2025). Library at this https URL

---


### 64. [SBMVTrack: Spike-Budgeted Multi-View Learning for Energy-Efficient UAV Tracking](https://arxiv.org/abs/2609.25503)

**<font color=#1a73e8>作者：</font>** Pengzhi Zhong, Jiwei Mo, Haolun Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With sparse and event-driven computation, spiking neural networks show great potential for achieving accurate and energy-efficient UAV visual tracking. However, existing SNN-based trackers typically use spike firing rates only for energy evaluation and lack explicit optimization of actual spike activity. To address this, we propose SBMVTrack, a fully spiking framework for energy-efficient UAV tracking. SBMVTrack introduces Energy-Weighted Spike Budgeting (EWSB). EWSB weights actual spike activity according to the computational cost of each spiking layer. It constrains the energy-weighted firing rate and saturation activity, thereby reducing redundant spike computations. To improve tracking performance under the spike budget constraint, we propose Masked Multi-View Target Modeling (MVTM). This method treats the initial template, online template, and search region from the same sequence as correlated temporal views. It enhances the robustness of target representations through cross-view feature completion and identity-consistency learning. Extensive experiments on multiple benchmarks demonstrate that SBMVTrack effectively reduces the average spike firing rate and theoretical energy consumption. Meanwhile, it maintains competitive tracking performance, achieving a better accuracy-energy trade-off. The source code will be released upon acceptance.

---


### 65. [SMTB: Fast Structure-Mapping with Tight Bounds](https://arxiv.org/abs/2609.25508)

**<font color=#1a73e8>作者：</font>** Daniel Weitekamp, Christopher MacLellan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structure-mapping forms analogies by aligning systems of relationally connected elements based on shared structure instead of surface features. We introduce a new structure-mapping algorithm: Structure-Mapping with Tight Bounds (SMTB) that is 5--15x faster than the structure-mapping engine (SME) and about 50\% better at finding mappings in large nested domains. SMTB is part of the broader Cognitive Rule Engine (CRE) project, a flexible multi-language-compatible framework with an accessible Python interface to state-of-the-art C++ implementations of core algorithms commonly used in cognitive systems such as pattern matching, planning, and structure-mapping. CRE and SMTB are designed to work with a wide range of representation choices. Unlike SME, which biases higher-order correspondences in tree-like predicate logic, SMTB maximizes relational connectivity without privileging higher-order relations. This allows SMTB to work just as well over arbitrary relational graphs as it does in tree-like domains of nested predicate logic. We discuss situations where privileging "higher-orderness" in structure-mapping can cause issues, and illustrate how SMTB avoids failure modes that SME would encounter in these situations. We also provide an evaluation comparing SMTB to SME v4 over 5845 domain pairs from the SME corpus.

---


### 66. [Real-World Perception for Autonomous Driving in Adverse Weather: Enhancing Standard Detectors via Foundation-Guided Auto-Annotation](https://arxiv.org/abs/2609.25515)

**<font color=#1a73e8>作者：</font>** Sepideh Gohari, Goodarz Mehr, Azim Eskandarian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard deployment-ready object detectors for autonomous vehicles degrade in adverse weather and lighting conditions without being trained on extensive domain-specific data. While large-scale vision foundation models offer robust zero-shot generalization, their high computational cost makes them impractical for real-time deployment. To bridge this gap, we propose a foundation-guided auto-annotation pipeline that enhances standard detectors without architectural changes. We first benchmark three distinct models, YOLOv8, Co-DETR, and SAM3, on our custom real-world driving dataset spanning 25 unique operational scenarios across various route, weather, and lighting conditions. Based on our analysis, SAM3 demonstrates superior accuracy and resilience across all scenarios. Thus, we deploy it as an offline auto-annotator to generate pseudo-labels on the unannotated subset of our dataset. Fine-tuning the baseline YOLOv8 on these annotations yields a 16.04% higher overall mean Average Precision (mAP) and improves cross-environmental stability compared to the baseline model, highlighted by a 32.73% and 28.65% mAP increase in Residential Direct Sunlight and Highway Fog, respectively. These results demonstrate that standard detectors can achieve environmental resilience without the need for extensive manual annotation or architectural modifications.

---


### 67. [When the Strike Zone Becomes Algorithmic: Umpire Judgment and Player Challenge Decisions under AI Review](https://arxiv.org/abs/2609.25525)

**<font color=#1a73e8>作者：</font>** Kichang Lee, Gyeongmin Han, Sungmin Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Automated Ball-Strike challenge system that Major League Baseball adopted in 2026 offers a distinctive setting for studying human AI interaction in which umpires make every ball and strike call, while players can selectively ask an automated system to publicly overturn those decisions. We analyze 4,114,256 called pitches from 2015 through 2026 and 8,447 challenges from the 2026 season to examine how algorithmic review reshapes umpire judgment and player behavior. We study where umpires placed the effective strike zone boundary, how consistently they applied that boundary, how they responded to overturned calls, and which calls players chose to challenge. In 2026, the effective called boundary shifted toward the automated strike zone beyond the trajectory observed in prior seasons, while the consistency of that boundary largely continued its existing trend. Following an overturned call, umpires temporarily adjusted subsequent decisions near the corrected boundary, although these effects did not consistently persist into the next game. Count dependent variation in calling remained, while differences associated with player status narrowed. Players, meanwhile, left many overturnable calls unchallenged and appeared to base challenge decisions more strongly on immediately observable evidence than on the precise geometry of the automated zone. Together, these findings show that selective AI review does more than correct individual errors. It reshapes human judgment, adaptation, and strategic behavior around an algorithmic authority.

---


### 68. [FASTAR: FRI Accelerator for Scalable Transparent ARguments of Knowledge](https://arxiv.org/abs/2609.25535)

**<font color=#1a73e8>作者：</font>** Tengkai Gong, Xiaolin Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zero-Knowledge Proofs (ZKPs) enable a prover to cryptographically convince a verifier of the validity of a statement without revealing any underlying secrets, forming a foundational primitive for verifiable computation. The ZKP landscape is undergoing a fundamental shift from classic zk-SNARKs such as Groth16, which rely on trusted setup and are vulnerable to quantum adversaries, toward transparent, post-quantum constructions such as zk-STARK. These systems achieve post-quantum security by relying solely on collision-resistant hash functions, however, at the cost of substantial computational overhead. In particular, the Fast Reed--Solomon Interactive Oracle Proof of Proximity (FRI) protocol dominates prover complexity, generating massive data volumes, repeated Merkle-tree commitments, and irregular memory access patterns that limit performance and energy efficiency on general-purpose processors.
To address these challenges, this work proposes FASTAR, a novel FPGA-based accelerator for the FRI protocol. Unlike accelerators that pursue fixed high-performance kernels on expensive ASIC process nodes, FASTAR adopts a constraint-driven design methodology. Our framework is implemented with High-Level Synthesis (HLS) and composed of fully parameterizable building blocks for the major stages of FRI, including polynomial evaluation, recursive split-and-fold, and Merkle-tree construction. From user-provided board specifications, FASTAR automatically generates hardware implementations tailored to the resource and memory constraints of the target FPGA, enabling deployment across a wide range of platforms without manual redesign.

---


### 69. [Point Diffusion Mamba: Unified Diffusion-State-Space Modeling for Single-View 3D Reconstruction under Data Scarcity](https://arxiv.org/abs/2609.25538)

**<font color=#1a73e8>作者：</font>** Wei Zhou, Xinzhe Shi, Xingxing Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While single-view 3D reconstruction has seen significant progress, extrapolating complex 3D structures from inherently ambiguous 2D observations remains fundamentally ill-posed, particularly in the critically underexplored data-scarce regime. To address this challenge, we propose Point Diffusion Mamba (PDM), a method that integrates the generative power of diffusion models with the efficiency of state-space model for single-view 3D reconstruction under data-scarce conditions. Specifically, PDM employs a lightweight reconstruction module tailored to handle unordered point-cloud inputs effectively. By combining a Local Geometric Aggregation module with Mamba blocks, our approach jointly models global geometric structures and local details. In 3D reconstruction, each point in the initial noisy input requires a precise prediction, yet the high-level features extracted by the Mamba module capture only abstract semantic information from sparse points. To bridge this gap, we introduce the Hierarchical Feature Integration Network, which fuses high-level semantic and local geometric features for each point, overcoming the limitations of token-based point-cloud reconstruction. Furthermore, we propose a Dynamic Weighted Sampling strategy that adaptively unifies 3D generation with single-view reconstruction by leveraging generative priors to enhance reconstruction quality. Experimental results on the ShapeNet and Pix3D benchmarks demonstrate that PDM outperforms state-of-the-art methods, providing an effective solution for 3D reconstruction under data-scarce settings. Code is available at: this https URL.

---


### 70. [DefaultGNN: A Dual-Perspective GNN Framework for Predicting Corporate Default from Buyer-Seller Transaction Networks](https://arxiv.org/abs/2609.25542)

**<font color=#1a73e8>作者：</font>** Junghoon Kim, Hyunsung Kim, Seungyoon Choi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Corporate default prediction is a core problem in financial risk management, yet traditional credit models rely heavily on financial statements that are often sparse or unavailable for many firms. Corporate transaction networks offer a complementary view of real economic activity, but how risk propagates through buyer-seller relationships remains underexplored. We conduct a large-scale empirical study using real-world electronic tax-invoice data spanning six years that links transaction histories with default events, revealing that transaction-driven risk is both role-dependent (buyer or seller) and scale-dependent. Based on these findings, we construct multiplex buyer-view and seller-view transaction networks and propose DefaultGNN, a dual-perspective graph neural network-based framework for corporate default prediction. DefaultGNN integrates both views to model how risk flows through transactional relationships, achieving strong improvements over both attribute-based and graph-based baselines, especially for firms with limited intrinsic risk signals. We further provide interpretable network-based explanations by visualizing how distressed trading partners contribute to default risk. In collaboration with a licensed credit rating agency, we validate that DefaultGNN's predictions complement existing credit scoring models, improving approval rates by 7-11%p without increasing default risk among approved firms. The source code can be found at this https URL

---


### 71. [Weakly Supervised Quantum Error Mitigation](https://arxiv.org/abs/2609.25555)

**<font color=#1a73e8>作者：</font>** Seyed Mohamad Ali Tousi, G. N. DeSouza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised approaches to quantum error mitigation learn a map from noisy circuit outputs to ideal ones, and therefore require the ideal outputs. Producing those ideal outputs demands noiseless classical simulation, whose cost grows exponentially with system size, so supervision is unavailable in exactly the regime where mitigation matters most. We ask whether cheap, individually unreliable signals drawn from circuit structure and hardware calibration can take the place of ideal labels. We assemble sixteen heuristic labeling functions (stabilizer and parity constraints, relaxation and readout characteristics, local depth, gate counts, and neighboring activity), reconcile their disagreements with a probabilistic label model, and read the resulting per-qubit error probabilities as a readout channel whose inverse mitigates the measured distribution. No ideal output enters the training path. On $147{,}000$ five-qubit circuits executed on two IBM devices, the method removes $24.3\%$ (Algiers) and $28.8\%$ (Hanoi) of the Kullback-Leibler divergence to the ideal distribution, against $15.4\%$ and $21.5\%$ for the strongest published analytical baseline, a margin that holds on both devices and lies far outside its bootstrap interval. Supervised neural models trained on ideal distributions remain stronger where such labels exist, and we quantify that gap rather than setting it aside; the method's claim is to the regime where they do not, since the labels they require cannot be computed for the circuits mitigation is needed for. The codes will be released shortly.

---


### 72. [Agentic Building-Aware Satellite Gaussian Splatting for Auditable Urban DSM Reconstruction](https://arxiv.org/abs/2609.25578)

**<font color=#1a73e8>作者：</font>** Wentao Sun, Zhengsen Xu, Yiping Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban-scale 3D reconstruction from satellite imagery supports disaster response, city monitoring, and geospatial digital twins, yet neural rendering methods typically optimize average visual fidelity rather than the structures that analysts inspect first: buildings. We present an agentic building-aware satellite Gaussian Splatting workflow that uses Segment Anything-derived building masks as semantic priors and an Agentic Reconstruction Controller to select, verify, and record DSM reconstruction policies. On the DFC2019 JAX\_004 scene, building-aware weighting reduces building-region DSM MAE from 0.844 m to 0.806 m, showing that semantic priors can shift reconstruction capacity toward analyst-critical regions. A staged schedule provides a balanced operating point, improving full-scene MAE from 1.362 m to 1.349 m while retaining a building gain. Across four JAX scenes, the Agent selects validated policies for both general DSM and building-focused DSM objectives, and produces building-inventory metadata and per-scene decision records. The system combines semantic priors, policy selection, region-specific DSM metrics, and DSM-derived GIS surface products for auditable urban 3D analysis.

---


### 73. [Rethinking Backdoor Repair Evaluation: Distinguishing Aggregate Clean Utility from Benign Performance Preservation](https://arxiv.org/abs/2609.25579)

**<font color=#1a73e8>作者：</font>** Baogang Song, Changtian Song, Jian Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor repair aims to suppress malicious behavior in compromised models while preserving benign task performance. Existing studies typically evaluate these objectives using Attack Success Rate (ASR) and Overall Clean Accuracy, but aggregate clean accuracy can obscure substantial degradation concentrated in a small portion of the label space. We revisit benign-performance evaluation from a preservation perspective by distinguishing aggregate clean utility from the preservation of previously available class-wise performance. We define class-wise preservation loss by comparing clean performance before and after repair and show that aggregation can hide localized degradation through localized-loss dilution and cross-class compensation. To complement Overall Clean Accuracy, we characterize localized preservation loss using Worst-Class Preservation Loss and Tail Preservation Loss. We conduct a systematic empirical study across representative backdoor attacks, repair methods, datasets, attack targets, and model architectures, with additional validation under clean-label attacks. Results show that effective attack suppression and favorable aggregate clean performance do not necessarily imply uniform preservation of previously available benign performance across classes. Substantial localized preservation losses can remain, and their severity and class-wise structure vary across repair conditions. These findings motivate preservation-oriented class-wise evaluation alongside ASR and Overall Clean Accuracy.

---


### 74. [Gaze responses to false-positive computer-aided detection prompts during colonoscopy: a paired-video and real-time eye-tracking study](https://arxiv.org/abs/2609.25581)

**<font color=#1a73e8>作者：</font>** Te Luo, Yan Zhu, Peiyao Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> False-positive computer-aided detection (CADe) prompts may divert endoscopists' attention during colonoscopy, yet the attentional impact of individual prompts remains unclear. We used event-locked eye tracking to quantify gaze attraction and attention occupation in complementary retrospective and prospective studies. In a retrospective paired-video experiment, 3 senior and 2 novice endoscopists viewed 60 colonoscopy videos with and without CADe. The prospective study recorded gaze during 42 real-time CADe-assisted colonoscopies performed by 9 senior endoscopists. Screened CADe prompts outside expert-annotated lesion windows were classified as false-positive artifact events. False-positive prompts attracted gaze in 48.6% (68/140) of retrospective observations and 65.2% (533/817) of prospective events. Among attraction events with complete recovery, median attention occupation lasted 1000 ms in the retrospective study and 1100 ms in the prospective study. Corresponding median prompt durations were 33 ms and 267 ms, with median time amplifications of 17.55-fold and 5.15-fold, respectively. In paired retrospective comparisons, visible artifact prompts drew gaze closer to the prompted region than did the same-coordinate unassisted reference. Secondary retrospective analyses showed high lesion gaze recognition without and with CADe (98.0% versus 99.0%). First gaze entry into lesion regions occurred 147.8 ms earlier with CADe. Across controlled and real-time clinical settings, false-positive CADe prompts frequently captured gaze, with attention persisting beyond prompt visibility. These findings support considering prompt-related attentional burden in CADe evaluation and design.

---


### 75. [EMGBlend: Heterogeneity-Aware Self-Supervised Pretraining for Gesture and Force Decoding](https://arxiv.org/abs/2609.25582)

**<font color=#1a73e8>作者：</font>** Yuwei Jia, Cheng Zhong, Jinyang Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Public surface electromyography (EMG) datasets vary widely in electrode layout, channel count, frequency support, and size. Simply mixing them for pretraining can misalign channel semantics, introduce spectral targets that some devices cannot observe, and let large or high-channel-count datasets dominate learning. We introduce EMGBlend, a self-supervised framework designed around these differences. It combines shared channel patches with geometry-aware attention, restricts spectral targets to each recording's supported frequency band, and balances exposure across data sources. We pretrain a 109M-parameter model on 11 public EMG sources and evaluate it on gesture recognition, continuous-force regression, and contact classification. EMGBlend consistently outperforms matched random initialization and waveform reconstruction controls. Fixed-budget source controls show that multi-source pretraining improves gesture recognition and remains competitive for force decoding. Ablations confirm that geometry, band-aware targets, and source balancing each contribute to transfer, although cross-person NinaPro force estimation remains difficult. Overall, EMGBlend shows how heterogeneous EMG datasets can be combined through explicit mechanism design rather than simple concatenation. Code is available at this https URL

---


### 76. [Hi-OPD: Hierarchy-Aware Open-Prompt Detection for Remote Sensing Images](https://arxiv.org/abs/2609.25584)

**<font color=#1a73e8>作者：</font>** Jinlong Hu, Yi Zhang, Zhiqi Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hi-OPD addresses a failure mode left uncontrolled by flat open-prompt training: descendant retrieval need not persist under ancestor queries when multi-source remote sensing annotations exhibit inconsistent granularity and missing labels. A detector may localize \textit{car} and \textit{van} under atomic prompts yet miss the same instances under \textit{vehicle}; flat AP does not expose this cross-level inconsistency.
We propose Hi-OPD, a hierarchy-aware open-prompt detector, and construct RS153-HierOPD from 175,644 retained training image/tile records and 3.48M boxes mapped to 153 atomic categories with sparse hierarchy and alias relations. Hi-OPD learns ancestor retrieval through hierarchy-safe negative sampling, path multi-positive supervision, and one-way upward consistency, while per-source risk exclusion handles potentially missing labels. ConvVPE converts K-shot support boxes into text-compatible embeddings using detector-native features and the shared contrastive head.
On Track A, Hi-OPD obtains 79.7/72.3 AP50 on DIOR/DOTA-v2.0, above the literature-reported OpenRSD results of 76.7/71.8. Under controlled training on the original converted annotations, the full hierarchy recipe raises DOTA-v2.0 parent AP50 from 7.2 to 71.5 and FAIR1M grandparent AP50 from 31.6 to 71.4, while DOTA-v2.0 atomic AP50 changes from 71.4 to 72.3. The text path reaches 99.7% CAR50 (0.3% violation) across the three common sources and 99.9%/0.1% on FAIR1M grandparent relations. On held-out VEDAI, text AP50 is 75.9, 6.2 points above OpenRSD. Joint AP and CAR show that explicit hierarchy training repairs this failure mode while retaining atomic detection and prompt transfer.

---


### 77. [Transformer Heads Looking for Order](https://arxiv.org/abs/2609.25588)

**<font color=#1a73e8>作者：</font>** Jasper van Doornmalen, Alexander Kozachinskiy, Corinna Mathwieser 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this note, we show that the problem of checking, whether a sequence of bits is ordered, is not doable by 1-head 1-layer transformers but is doable by a 2-head 1-layer transformer. Unlike similar previous results, our results assume the model where transformers have an output MLP.

---


### 78. [Observer Choice and Threshold Selection in Retinal Vessel Segmentation: A Subject-Separated Evaluation](https://arxiv.org/abs/2609.25597)

**<font color=#1a73e8>作者：</font>** Wenhao Xu, Yixian Kong, Ting Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The annotation used to select a segmentation threshold is part of the evaluation protocol, yet its effect is easily conflated with model quality. We examine this choice for retinal vessel segmentation using all 28 CHASE DB1 images and both human annotations. A fixed seven-fold protocol keeps both eyes of each of the 14 subjects together. Random forests and Extra Trees are fitted against observer 1 with three random seeds, yielding 42 fits. Five threshold policies share identical score maps: fixed 0.50, observer-1 tuning, observer-2 tuning, mean-observer tuning, and maximin tuning of the per-image lower observer Dice. For random forests, maximin changes the threshold in 19 of 21 fits, but worst-observer Dice decreases from 70.53 percent to 70.45 percent. The paired difference is -0.073 percentage points, with a conditional subject-bootstrap 95 percent interval of [-0.384, 0.238]. Extra Trees shows the same direction. Identical observer-1-tuned random-forest masks score 73.66 percent against observer 1 and 71.06 percent against observer 2. The results support explicit reporting of both the threshold-selection reference and evaluation reference; they do not support an accuracy benefit from maximin tuning in this cohort. All splits, raw predictions, metrics and code are supplied. AI assistance is disclosed.

---


### 79. [Ultra-fast Neural Inference for Stochastic Gaussian Splatting Denoising](https://arxiv.org/abs/2609.25604)

**<font color=#1a73e8>作者：</font>** Chenxiao Hu, Hao Zhang, Yanchen Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stochastic rendering eliminates the sorting and alpha blending process in Gaussian splatting, at the cost of introducing spatial noise. Formulating temporal denoising over the pixel stream shared by view-consistent stochastic splatting renderers, we propose a temporal neural denoiser validated on stochastic 2D Gaussian Splatting rendering, combining dual-path exponential moving average accumulation, per-pixel learned trust prediction for history validation, a fixed anisotropic spatial filter and a variance-gated composition with stabilization. The denoiser suppresses the noise, achieving temporally stable, visually compelling outputs during free camera navigation, all while retaining the sort-free, blend-free rasterization performance. The combined pipeline retains a PSNR gap to sorted alpha-blending renderers, but the denoiser's overhead stays below the time saved by removing sorting and blending.

---


### 80. [SurgGaze: Implicit Calibration for Accurate Gaze Analysis in Operating Rooms with Wearable Eyetrackers](https://arxiv.org/abs/2609.25612)

**<font color=#1a73e8>作者：</font>** Jingying Wang, Rosiana Natalie, Keyuan Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Accurate gaze tracking is essential for understanding surgeons' visual attention and cognitive processes during laparoscopic surgery, yet wearable eye trackers produce large errors systematically correlated with ground-truth gaze locations, as demonstrated in Study 1. We introduce SurgGaze, an implicit calibration method that corrects these errors using high-confidence surgical moments. Building on evidence that surgeons' gaze converges near the tool-tissue contact point (TTCP) during dissection, SurgGaze uses TTCP as a surrogate for true gaze to construct training pairs. We evaluate SurgGaze in a simulated operating room trial and an authentic operating room case study. In simulation, SurgGaze reduced gaze estimation error by 40.6%, significantly outperforming conventional 9-point explicit calibration. The case study showed that these moments provide reliable training data and that calibrated gaze improves interpretation of surgeons' attention beyond numeric error reduction. These findings demonstrate that structured behavioral signals can enable implicit calibration for gaze tracking in complex real-world settings.

---


### 81. [Evidence-gated multimodal parsing and vectorization of architectural floor plans](https://arxiv.org/abs/2609.25615)

**<font color=#1a73e8>作者：</font>** Hongxuan Chen, Wenda Wang, Jiachen Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Architectural floor plans remain a high-friction barrier to archive digitization and early design-model preparation because heterogeneous graphics encode spatial semantics and editable geometry together. We introduce SALI-FP, an evidence-gated multimodal pipeline that converts a plan into reviewable semantic maps, objects, vectors, and relation records while constraining local revisions by image evidence. In a full production audit of 11,534 heterogeneous plans, SALI-FP produced structured outputs for every plan, including 752,510 valid polygon-bearing objects. The same output form has supported initial drawing digitization and design-model preparation in practical design work. Public-benchmark calibration is paired with a 30-case matched visual evidence set in Appendix F, where room-scale coverage, openings, oblique boundaries, and circulation continuity can be inspected directly. SALI-FP offers an engineering-oriented interpretation-to-geometry workflow for reviewed CAD/BIM preparation and existing-building information recovery.

---


### 82. [What Should a Self-Teacher See? Privileged Context Design for On-Policy Self-Distillation](https://arxiv.org/abs/2609.25623)

**<font color=#1a73e8>作者：</font>** Kanghui Tian, Siyuan Liu, Tianxiang Jiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> More privileged information does not always make a better teacher. We study this tension in on-policy self-distillation (OPSD), where a frozen copy of the base model scores the student's own rollouts under privileged context, conventionally a complete reference solution that bundles the final answer with one particular reasoning path. Holding the student view and training fixed within each scale, we compare that default against three abstractions compiled offline, a named strategy, a method-independent framing, and a problem category, and against an answer-only control that keeps the destination but removes the path. In the primary runs on competition mathematics, the best intermediate contexts improve the in-domain peak mean over the full solution by 1.4 points at 4B and 1.6 at 8B, while storing an order of magnitude fewer hint tokens. Comparisons across three seeds also show positive mean gains for the framing and category contexts at both scales. Answer-only conditioning remains competitive in the primary runs, within 0.2 points of the full solution at these scales. The preferred context varies with student scale and task. Initial teacher-student KL does not order downstream performance. What a self-teacher should see is therefore not everything it could, but the level of abstraction its student can still act on.

---


### 83. [An Exploratory Replica-Overlap Probe of the Grokking Transition](https://arxiv.org/abs/2609.25634)

**<font color=#1a73e8>作者：</font>** A. C. Opus, J. Q. Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We trained 64 independently seeded networks in four configurations, continuing each to sustained convergence or a 40,000-epoch ceiling. We then asked whether an RSB-inspired distribution of pairwise weight overlaps changes across the grokking transition. It is the alignment step, not the overlap statistic, that determines what this registered probe can report. The registered implementation permutes hidden units without the corresponding bias and head-internal permutations and therefore does not preserve the network function. Every q_wt value computed through this alignment inherits the defect; q_fn does not, because it is computed from predictions of the unpermuted models. The numerical-precision requirement also failed, and an audit found protocol deviations. Consequently, the pre-registered rule gives no verdict: registered outcome UNDETERMINED (reason code C0_INSTRUMENT_INVALID). These data provide neither a confirmatory null nor a validated reading of the Parisi order parameter. Only frac40 cleared the 12/16 checkpoint-completeness requirement. For this configuration, a post-hoc criterion applied to the same data gave a Hartigan-dip interval containing zero (95% CI for Delta dip = [-0.017, 0.034]), whereas the overlap standard deviation increased by a factor of about 5.6. A post-hoc calibration assigns the dip test zero power at the simulated separations; the interval is therefore uninformative, not evidence of no change. The standard-deviation ratio is the only statistic here with power at the observed effect. Ensemble loss was near-flat only under the pre-specified 1% threshold. Finally, grokking rates of 0/16, 11/16 and 16/16 remain descriptive because train fraction is confounded with split identity.

---


### 84. [What Drives Hierarchy-Aware Image Retrieval? Taxonomy Alignment, Objective Choice, and Geometry](https://arxiv.org/abs/2609.25638)

**<font color=#1a73e8>作者：</font>** Ling Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation vision models provide strong generic representations, yet high class-level retrieval accuracy does not necessarily imply that an embedding respects a target semantic taxonomy. We study strict explicit-taxonomy image retrieval on frozen DINOv2 features and ask: when hierarchical retrieval improves, how much of the change is associated with the organization of taxonomy-aware supervision, and how much with the Euclidean-hyperbolic geometry choice?
We evaluate higher levels with strict cross-class criteria that exclude finer-grained matches, and compare Euclidean and hyperbolic projections trained with taxonomy-distance regression or a taxonomy-aware supervised contrastive objective. A compute-matched 2 x 2 Geometry x Loss factorial uses the same 768-256-32 projector capacity, optimization schedule, batch order, and fixed 100-epoch budget; the Loss axis denotes the Regression-to-Taxonomy-SupCon objective-family contrast. On CUB, the objective-family contrasts in mean hierarchy mAP (strict middle/high average, excluding Class/Leaf) are +0.0487 in Euclidean space and +0.0414 in hyperbolic space, compared with geometry contrasts of +0.0102 and +0.0030. On NABirds Parent-disjoint retrieval, the corresponding objective-family contrasts are +0.0467 and +0.0440, whereas geometry contrasts are +0.0017 and -0.0009.
A semantic-alignment control shows that the true taxonomy substantially outperforms a structure-preserving shuffled hierarchy, while a NABirds curvature/radius control does not support stronger negative curvature as the explanation for the observed hierarchy gains. Across the two taxonomies, the Regression-to-Taxonomy-SupCon contrasts are larger in aggregate than the evaluated geometry contrasts; semantic alignment also matters separately, while geometry remains hierarchy-dependent.

---


### 85. [Decoupling Disease, Covariates, and Individual Variability: A Unified Disentanglement Framework for Medical Image Classification](https://arxiv.org/abs/2609.25650)

**<font color=#1a73e8>作者：</font>** Shengjie Zhang, Jinglin Zhang, Zhuangzhuang Jiang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately isolating disease-related features from confounding covariates (e.g., age, gender, site) and individual variations remains a fundamental challenge in medical image classification. Traditional regression-based approaches may ignore non-linear relations between image features and true covariates. To overcome this issue, we present a generalized Medical Imaging Disentanglement Learning (MedIDL) framework. MedIDL maps image features into three mutually orthogonal latent spaces through specialized disentanglement heads: a disease classification head guided by a supervised loss, a covariate-alignment head constrained by cross-subject similarity matching, and a Gaussian head absorbing individual variations. We evaluated our framework across 7 datasets encompassing diverse imaging modalities. MedIDL outperforms state-of-the-art supervised and self-supervised classification methods in accuracy across all datasets. Association analyses demonstrate that MedIDL successfully isolates target-specific latent representations. Gradient-based interpretability mappings localize pathognomonic patterns aligning with established clinical literature.

---


### 86. [GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](https://arxiv.org/abs/2609.25652)

**<font color=#1a73e8>作者：</font>** Zijun Lin, Zhiyang Deng, Yuzhe Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent game world models support realistic visual simulation and interactive gameplay based on player inputs. However, they typically learn environment dynamics from pixel-level supervision, jointly modeling perception, memory, state transitions, and rendering within a single end-to-end framework. While this design enables open-ended, action-controllable generation, it still falls short of delivering a complete gameplay experience. Games are governed by explicit mechanics, such as health deduction, skill activation, combat rules, and termination conditions. These mechanics depend on precise and consistent state transitions that generative models alone cannot reliably enforce. In contrast, game engines can guarantee such mechanics through hard-coded rules, but provide limited flexibility for player-driven creation. To bridge these paradigms, we introduce GameDirector, the first agentic framework that decouples rule-based gameplay logic from visual rendering. Given player-defined configurations, the framework acts as an intelligent director that interprets visual observations, updates game states, tactically controls NPCs, and enforces gameplay rules. It then translates these decisions into text prompts that guide the video world model to render the resulting gameplay. This separation allows players to configure characters, states, and rules much like a game developer while preserving coherent game mechanics. Experiments on three games, using data collected by our automated gameplay agent, show that GameDirector achieves accurate state tracking, reliable rule following, and improves boss action quality by more than 39.9% over various end-to-end game world model settings. Overall, by externalizing player-controllable game logic, GameDirector establishes a middle ground between hard-coded simulation and generative modeling, enabling more flexible and closed-loop gameplay experiences.

---


### 87. [Targeted Review for AI-Assisted Biodiversity Surveys: Active Continuous-Score Occupancy Modeling](https://arxiv.org/abs/2609.25657)

**<font color=#1a73e8>作者：</font>** Timm Haucke, Lauren Harrell, Justin Kay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We increasingly use machine learning to label scientific datasets. The models we develop and deploy are improving all the time, but they are not and will likely never be perfect. Mistakes matter, as errors can propagate into our scientific understanding, particularly when systematically biased. Very reasonably, scientists thus review substantial proportions of ML-generated labels to verify or correct mistakes in pursuit of ensuring their scientific findings are not biased by ML. In this work, we focus on helping scientists optimally allocate this reviewing effort relative to their scientific goals. We focus on a specific class of scientists (ecologists) and a specific, widespread, and impactful modeling target (occupancy modeling, which estimates where species are likely to occur, conditioned on environmental factors). We introduce Active Continuous-Score Occupancy Modeling (ACORN), a method that incorporates ML predictions into occupancy models and strategically selects samples for expert review that are maximally informative for downstream ecological analysis. Across camera-trap and bioacoustic datasets, our method recovers ecological conclusions close to those obtained from fully human-labeled data, while requiring substantially fewer expert reviews than non-targeted review policies. Our results suggest that ML-assisted scientific workflows should optimize expert effort for downstream inference, rather than for classifier accuracy alone, especially when human review budget is limited. Our code is available at this https URL

---


### 88. [When Riemann flows with Wasserstein: Generative Modeling of Probability Distributions on Manifolds](https://arxiv.org/abs/2609.25659)

**<font color=#1a73e8>作者：</font>** Doron Haviv, Edward De Brouwer, Rishabh Anand 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many scientific datasets, such as molecular conformational ensembles or single-cell tissue measurements, are naturally modeled as meta-distributions: distributions over probability measures on non-Euclidean domains. Existing generative methods largely assume Euclidean geometry and fail to capture this structure. We introduce Riemannian Wasserstein Entropic Flow Matching (RWEFM), a generative framework on the Wasserstein space $\mathcal{P}_2(\mathcal{M})$ of a Riemannian manifold $(\mathcal{M},g)$. RWEFM is trained by regressing a neural vector field onto Riemannian optimal transport velocities, using McCann displacement interpolations as conditional paths. We confirm theoretically that this construction leads to a valid flow matching approach on $\mathcal{P}_2(\mathcal{M})$ and introduce the Riemannian Entropic Map, a GPU-efficient approximation of the optimal transport map on manifolds. Our experiments show that by respecting the intrinsic geometry of the data, RWEFM can generate whole single-cell samples in hyperspherical latent spaces and protein conformational ensembles on the torus. As RWEFM requires only a geodesic distance and a projection operator, it is not restricted to manifolds with closed-form geometry, which we demonstrate by generating distributions on a general triangulated mesh.

---


### 89. [Marginal Log-Likelihood Increments under Dirichlet-Smoothed Markov Estimation](https://arxiv.org/abs/2609.25675)

**<font color=#1a73e8>作者：</font>** Levin David Schwab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For a Dirichlet-smoothed transition model, the effect of adding one workflow trace to the training archive is an exact change in reference-weighted log likelihood. We derive that change and show that it is a weighted reduction of Kullback--Leibler divergence between the reference conditionals and the model. From this form we obtain an upper bound on the gain available to any acquisition, which expresses a millinat difference as a share of what is attainable, an exact covariance identity for the effect of the reference weighting, and a sign criterion for the interaction between two candidates, from which the batch objective is neither submodular nor supermodular. A case study on the BPI Challenge 2012 loan-application log measures all three and finds a positive selection result in one of the four combinations of reference weighting and budget unit. There, of two regressors fitted to identical descriptors and identical labels, the one that predicts individual increments far more accurately, median $R^2$ 0.87 against 0.62, realizes the smaller share of the attainable gain, 61 against 69 per cent, so ranking accuracy for individual traces is neither necessary nor sufficient for batch quality.

---


### 90. [Real-Time Atomic-Resolution Electron Phase Imaging without Probe Calibration via Ptychography-Supervised Learning](https://arxiv.org/abs/2609.25684)

**<font color=#1a73e8>作者：</font>** H. Yue, C.-C. Chen, C.-N. Hsiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Atomic-scale phase imaging is central to resolving defects, interfaces, and weakly scattering atoms that govern the behavior of nanoscale materials. Electron ptychography delivers sub-ångström phase sensitivity but remains an offline technique, because its iterative reconstruction is computationally expensive and sensitive to experimental calibration, preventing live use during data acquisition. Here, a ptychography-supervised local inference framework is presented that converts four-dimensional scanning transmission electron microscopy (4D-STEM) into an acquisition-compatible phase-imaging workflow. Physics-constrained reference phase maps reconstructed from a single experimental AuPd dataset serve as teacher labels for a compact model that predicts local phase patches directly from diffraction measurements, without explicit probe input or online iterative optimization. Full-field images are assembled by deterministic overlap stitching. The workflow reaches an online latency of about 0.27 ms per probe position and a throughput of about 20,000 positions per second, an approximately 1,000-fold speed-up over GPU-accelerated ePIE, while preserving atomic-scale lattice contrast and reciprocal-space fidelity. Without fine-tuning, the same model transfers across materials (WS2), defocus conditions (high-entropy alloy nanoparticles), and instruments (hBN at 300 kV). The approach amortizes ptychographic redundancy into a fast, generalizable workflow that enables real-time atomic-scale phase imaging for materials microscopy.

---


### 91. [Initialization and Stopping Tolerance in CPU Dermoscopic Segmentation](https://arxiv.org/abs/2609.25685)

**<font color=#1a73e8>作者：</font>** Wenhao Xu, Yixian Kong, Ting Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contour initialization and numerical stopping can jointly affect the evaluation of active-contour segmentation. We examine their interaction using the open-source scikit-image Chan-Vese implementation on a resized ISIC 2017 mirror. A fixed development set of 100 images selects a common input channel; all 600 images in the repository's held-out partition are then evaluated. Otsu thresholding is compared with checkerboard-, disk-, and Otsu-initialized contours under default and tighter level-set tolerances. At the default tolerance, Otsu initialization increases mean image Dice from 0.6011 to 0.6660 relative to checkerboard initialization, a paired difference of 0.0649 (95% image-bootstrap interval [0.0452, 0.0860]). Otsu thresholding alone achieves 0.6897. The default disk initializer stops after one iteration on 471 images. Tightening the tolerance reduces the Otsu-seed advantage over checkerboard initialization to 0.0197, with most runs reaching the 500-iteration limit. The default-tolerance advantage also reverses between small- and large-lesion strata. These findings show that an improvement over a generic initializer can coexist with deterioration relative to the threshold baseline. Evaluations should retain the unrefined mask as a comparator and report the initial-field definition, stopping tolerance, and observed iteration counts together.

---


### 92. [Graph Domain Adaptation Does Not End with Representation Learning](https://arxiv.org/abs/2609.25692)

**<font color=#1a73e8>作者：</font>** Ziqian Liu, Yongxue Xu, Enze Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph domain adaptation (GDA) transfers knowledge from a labeled source graph to an unlabeled target graph under shifts in both node attributes and graph structure. Existing methods primarily adapt graph representations through propagation redesign, distribution alignment, or source-to-target transition modeling, but still rely on a single graph-propagating path for target prediction. This leaves open whether an adapted graph representation exhausts the predictive evidence available in the target domain, since the graph-aware expert and graph-free local expert may exhibit different failure modes under topological shifts. To address this limitation, we propose EviGDA, an Evidence-Augmented Graph Domain Adaptation framework that complements graph representation adaptation with a graph-free local expert. The graph-aware expert performs message passing and entropy-aware marginal alignment, while the graph-free local expert learns solely from source node features and labels without graph propagation or target alignment. The two experts are optimized independently and combined only at inference through a task-level constant probability mixture, preserving complementary evidence without joint training, learned routing, or target pseudo-labels. Extensive experiments on ten datasets and 16 transfer tasks show that EviGDA outperforms state-of-the-art baselines.

---


### 93. [Interpretable AI plus Handheld, Portable Retinal Photographs: A Low-Cost Glaucoma Screening Solution for West Africa](https://arxiv.org/abs/2609.25697)

**<font color=#1a73e8>作者：</font>** Charis Y. N. Chiang, Tarela Sarimiye, Adeyinka Ashaye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: To develop and evaluate an interpretable artificial intelligence (AI) framework for glaucoma screening from low-cost portable, handheld retinal fundus photographs in a West African population and to compare its performance with clinical tabletop fundus imaging. Methods: We used data from a community-based study of 681 participants (1,362 eyes) in Nigeria, comprising 414 glaucoma, 478 glaucoma suspect, and 470 non-glaucoma eyes. Fundus photographs were acquired using the low-cost handheld, portable Volk Viva retinal camera and the Canon CR-2-AF tabletop camera. We fine-tuned component models separately to each device to perform vessel segmentation, cup and disc boundary segmentation, and feature extraction to detect optic nerve head features. A final classification model combined these components to classify scans as glaucoma, glaucoma suspect or non-glaucoma. Feature-weight analysis and Gradient-weighted Class Activation Mapping were used for interpretation. Results: The models performed well on both Volk Viva and Canon CR-2-AF images: Vessel segmentation: 0.98 Dice Coefficient (DC) (Volk) and 0.94 DC (Canon); Cup and disc segmentation: 0.95 DC (Volk) and 0.96 DC (Canon); Optic nerve head feature detection: area under the receiver operating characteristic curve (AUCs) of 0.83$\pm$0.03 (Volk) and 0.87$\pm$0.04 (Canon); Classification model: AUCs of 0.85$\pm$0.01 (Volk) and 0.93$\pm$0.01 (Canon). Reports for each image, present model decision confidence scores and decision-rationale visualizations to support clinical interpretation. Conclusions: Volk Viva results were reasonably comparable to Canon CR-2-AF in the component models and not far behind in classification. This shows that interpretable AI combined with low-cost, portable imaging may enhance community-level glaucoma screening, especially in settings with limited specialist access and resources.

---


### 94. [Fully Byzantine-Resilient Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.25701)

**<font color=#1a73e8>作者：</font>** Haejoon Lee, Dimitra Panagou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study distributed Byzantine-resilient actor-critic multi-agent reinforcement learning (AC-MARL), where agents collectively learn policies through local interactions. Existing methods guarantee convergence of the agents' parameters only to a neighborhood of the attack-free limit points, resulting in degraded performance. We propose Fully Resilient AC-MARL (FRAC-MARL), a decentralized method in which each agent leverages redundancy in two-hop messages to identify reliable messages. Under linear parameterizations of the value and team-reward functions and Byzantine edge attacks, where adversarial behavior is confined to the communication layer, we prove that agents' parameters converge almost surely to the same limit points as in the attack-free case over time-varying communication graphs. We introduce a novel topological condition for the convergence of our method, present a systematic method to construct such networks, and prove that this condition can be verified in polynomial time. Finally, we demonstrate our method on cooperative multi-robot formation control tasks.

---


### 95. [FoMo: Forking Moment in Generative Trajectory as a Perceptual Distance](https://arxiv.org/abs/2609.25716)

**<font color=#1a73e8>作者：</font>** Jaihyun Lew, Mingi Jung, Minjun Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-based image quality assessment (IQA) metrics aim to reflect how humans perceive the perceptual distance between a pair of images. To learn how the human visual system (HVS) operates, recent reference-based IQA metrics heavily rely on human-annotated data. Mean opinion score (MOS)-based pointwise scoring, which assigns a scalar quality value per image, is preferable for annotation but is prohibitively expensive to collect at scale and is known to be noisy due to inconsistent human judgments. As an alternative, two-alternative forced choice (2AFC) pairwise labels have gained popularity due to their reliability and efficiency, but they capture only relative comparisons between pairs. In this paper, we propose a fully automated data generation pipeline that generates pointwise perceptual distance labels between image pairs without any human annotation. Our approach exploits the generative dynamics of diffusion models as a perceptual distance proxy, where the coarse structure of an image is generated in the early timesteps and the fine details are generated in the later timesteps. Images that fork early in the generation process share only coarse structure and are perceptually far apart; images that fork late differ only in fine detail. We demonstrate that the diffusion trajectory aligns well with the human visual system, and use this forking moment, FoMo, as a reference-grounded distance label to supervise the training of a reference-based IQA metric. The pointwise labels, which support universal comparison between arbitrary image pairs, enable an information-rich training objective. Extensive experiments across diverse backbone architectures confirm the effectiveness of our generation pipeline, outperforming human-annotated datasets in multiple benchmarks.

---


### 96. [Signed Graph Pre-Training and Prompt Learning](https://arxiv.org/abs/2609.25722)

**<font color=#1a73e8>作者：</font>** Zihan Mei, Rong Pan, Yuzhou Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Signed graphs arise in trust--distrust networks, financial correlation systems, biological interaction graphs, and many other domains in which edges can be positive or negative and may also be directed. While signed graph neural networks have improved task-specific learning, graph transfer learning on signed graphs remains underdeveloped. In this paper, we introduce TopoSIGN, a pioneer topology-guided graph pre-training and prompt learning framework for signed graphs. TopoSIGN combines a structural encoder built on the magnetic signed Laplacian with a novel persistent-homology branch that summarizes signed topology through Dowker-complex persistence images. The fused embeddings are then transferred to a prompt learning function. Experimental results on synthetic and real-world datasets demonstrate the efficacy of TopoSIGN in extracting useful structural information in signed graphs, as well as the adaptability and flexibility of the proposed general framework.

---


### 97. [Self-Supervised Combinatorial Optimization with Constraints via Frank-Wolfe](https://arxiv.org/abs/2609.25728)

**<font color=#1a73e8>作者：</font>** Akbar Rafiey, Yifei Xu, Nikolaos Karalias  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning for combinatorial optimization has emerged as a promising paradigm for solving discrete optimization problems with neural networks, but a central challenge remains: handling hard combinatorial constraints within continuous, gradient-based training. Continuously extending combinatorial objectives to convex domains is a powerful technique, yet existing approaches often require projection steps that constrain neural network outputs to lie inside the feasible polytope and rely on ad-hoc and problem-specific constructions. We propose a general framework in which the neural network is allowed to predict arbitrary continuous vectors that could potentially lie outside of the feasible polytope. These predictions are then approximated by sparse convex combinations of feasible solutions using a geometric decomposition algorithm based on Frank--Wolfe methods and approximate Caratheodory results. This decomposition induces an a.e.-differentiable, self-supervised loss defined as the expected value of the discrete objective. The same procedure provides an automatic rounding guarantee at inference time. We demonstrate strong empirical performance across multiple combinatorial problems, including the Quadratic Assignment Problem, Maximum Coverage, and the Traveling Salesperson Problem.

---


### 98. [Annual Earth-observation embeddings encode wildfire disturbance and support simplified burned area mapping](https://arxiv.org/abs/2609.25731)

**<font color=#1a73e8>作者：</font>** Jovana Knezevic, Clement Atzberger, Zhengpeng Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medium-resolution (10-30 m) burned area mapping is vital for monitoring wildfires and their impacts, but remains difficult to scale. Existing methods require either curated fire-specific imagery or dense time-series analysis. Here, we tested whether annual Earth-observation embeddings retain wildfire disturbance signals sufficiently to map burned areas without either requirement. Using Tessera and AlphaEarth embeddings, we tested individual burn-scar delineation, mapping of all same-year fires within an area, regional wall-to-wall mapping, cross-continental transfer, and intra-annual fire timing. Tessera strongly encoded wildfire disturbance, allowing even linear models to separate burned from unburned pixels; the signal was weaker in AlphaEarth. Models trained on a single Tessera embedding matched or exceeded equivalent models using paired pre- and post-fire HLS imagery, and outperformed post-fire imagery alone. The same approach mapped all same-year fires within benchmark scenes (F1 = 0.90). Applied across California, with no California fire data used for downstream training, it recovered 97% of reference burned area and detected substantially more small and medium-sized fires than GABAM or MCD64A1. Separately, a model trained on 2018-2021 US fires transferred without retraining to 88 European fires from 2024-2025 (F1 = 0.88). For well-detected fires, ignition timing was recovered with a mean absolute error of 13 days. Performance declined for fires ignited near the end of the calendar year, and wall-to-wall deployment produced systematic false positives in some unseen landscapes. Annual embeddings nevertheless achieve high segmentation accuracy while moving the burden of dense time series processing upstream, providing a promising path towards simpler regional burned area mapping.

---


### 99. [GuidedRay: Diversity-Guided Direction Discovery for Targeted Hard-Label Black-Box Attacks](https://arxiv.org/abs/2609.25734)

**<font color=#1a73e8>作者：</font>** Fei Yuan, Yantian Shen, Qingyuan Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are vulnerable to adversarial attacks. Among black-box attacks, targeted decision-based attacks are particularly difficult: the attacker observes only the target model's top-1 label and aims to make it predict a prespecified target class under a bounded perturbation. Before perturbation refinement, the attacker must discover a direction that reaches the prescribed target region. This initialization step can incur substantial query cost. We propose GuidedRay, a targeted decision-based attack based on diversity-guided direction discovery. GuidedRay builds on two observations: target-class reference samples provide useful target-conditioned direction priors, and diverse candidates increase the probability of discovering a targeted adversarial direction. GuidedRay generates varied candidates from one or multiple target-class references and uses a one-query Fast Test to screen their induced sign directions. Once a feasible direction is found, GuidedRay applies Ray Search to reduce its decision-boundary radius. Experiments on CIFAR-10, CIFAR-100, and ImageNet demonstrate that GuidedRay consistently outperforms five state-of-the-art decision-based attacks at four evaluated query budgets from 500 to 5,000, with particularly pronounced gains in direction discovery during initialization. Against models protected by adversarial training or TRADES, it likewise achieves the highest attack success rate at all four query budgets.

---


### 100. [Beyond Class Marginals: Bounding Rehearsal Gaps without Freezing Class Co-occurrence](https://arxiv.org/abs/2609.25735)

**<font color=#1a73e8>作者：</font>** Congren Dai, Nat Roongjirarat, Fei Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class-balanced replay controls class frequency but does not determine the interval between successive replay appearances of a class. We study this interval, the rehearsal gap, separately from the class marginal and class co-occurrence, and introduce randomised-pass replay (RPR), which visits each resident class once per shuffled pass. For a fixed set of C resident classes and replay batch size b less than or equal to C, RPR preserves the balanced time-averaged class marginal and bounds every gap by 2*ceil(C/b)-1; a churn-conditional bound applies while the resident set changes. The scheduler uses no future class information and adds no replay examples or forward passes. In a linear-head ER-ACE diagnostic, joint absence from the incoming and replay batches produces a one-sided classifier-bias gradient. Longer absence episodes are associated with larger negative bias displacement, and removing the incoming-loss mask attenuates the scheduling effect. In the primary ER-ACE experiments, RPR improves final average accuracy by 0.72-1.67 percentage points relative to independent class-balanced retrieval under reservoir storage, with positive effects also observed under balanced storage. Pretrained ViTs show positive effects on the tested LT10 streams with small replay batches, while matched larger-batch controls show no material effect. Fixed-cycle and reused-pass controls change more than one temporal statistic, so the experiments do not isolate rehearsal-gap length from all other forms of temporal dependence. The accuracy effects depend on the learner and operating regime.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-275](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
