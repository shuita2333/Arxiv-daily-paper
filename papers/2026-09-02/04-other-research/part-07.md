# 📦 其他研究 | 2026年09月02日

> 本类共 **485** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

---

### 301. [VERA: Authority-Preserving Edge Revocation for Federated AI-Agent Workflows](https://arxiv.org/abs/2608.30091)

**<font color=#1a73e8>作者：</font>** Lifei Liu, Haoran Yu, Xiaochong Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern agent frameworks compose planners, tool agents, remote services, and shared specialists into runtime delegation graphs, but their revocation APIs still resemble token or subtree invalidation. When one delegation is withdrawn, the runtime must know which agents lose authority while independently authorized agents keep working. We study this authority consistency problem and introduce VERA (Verifiable Edge Revocation for Agents), a verifier-checkable revocation contract and API emitted by agent-runtime adapters as signed evidence. Under disjunctive authority, revoking edge e invalidates exactly T_intent(e,G) = reach(G) \ reach(G \ {e}), the agents whose every authorizing root path used e. Used as a contract, this target exposes two runtime failures: tree cascades over-revoke shared agents, while deployer-scoped cascades under-revoke cross-domain descendants. In a LangGraph framework-replt cells repeated 20 times yield 500compiled-framework traces and 2,000 valid signed delegation decisions; 13/25 cells contain runtime multi-parsharing and 8/25 contain cross-deployer shies 500/500 target proofs, preserves all320 alternate-parent shared-agent cases that tree cascade revokes, and rejects unauthorized signers and omission attacks. Baseline replay over 1,9that holder/node and tree-style targetscannot express this behavior. We further validate schema portability on A2A, AutoGen, and CrewAI artifacts: nine traces, including five executable Cregned delegation events that pass schema and signature checks.

---


### 302. [SMOTE-VAR: An Uncertainty-Aware Oversampling Method for Predicting Depression Remission in University Students](https://arxiv.org/abs/2608.30102)

**<font color=#1a73e8>作者：</font>** Dang Nguyen, Arun Kumar A V, Taylor A. Braund 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> University students experience disproportionately high rates of common mental health conditions, such as depression, which can impair learning, social functioning, and overall well-being. Although lifestyle interventions such as mindfulness and physical activity can reduce the symptoms, many do not achieve symptomatic remission. Developing new approaches to identify students with poor outcomes could enable earlier and more targeted intervention. Machine learning (ML) methods have increasingly been used to predict remission in depressive patients. However, these ML models often suffer from class imbalance, where there may be an unequal proportion of people in the remitted group relative to the non-remitted group. This imbalance can reduce model accuracy and bias predictions. To address this, studies commonly employ the popular oversampling strategy SMOTE. However, SMOTE has a notable limitation: it may generate invalid synthetic minority samples. In a clinical context, these false positives can lead to incorrect risk stratification, potentially delaying necessary escalated care for patients unlikely to remit. In this paper, we introduce a novel and effective oversampling method that addresses this shortcoming. Our approach leverages the variance function of a Gaussian process to estimate the uncertainty of generated minority samples to reduce false positives. We validate our method on a depression dataset collected from university students and demonstrate that it is better than existing oversampling approaches in predicting remission (i.e., treatment outcome). By improving the reliable identification of non-responders, our method provides a robust computational tool to help clinicians rapidly pivot to adjunctive therapies, thereby personalizing and optimizing mental health care pathways.

---


### 303. [Graph4BiLO: Graph Neural Network Approximation for Bilevel Mixed-Integer Linear Optimization](https://arxiv.org/abs/2608.30103)

**<font color=#1a73e8>作者：</font>** Jessica D. Elrefaei, Kaixun Hua, Seungbae Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bilevel mixed-integer linear optimization problems model hierarchical decision processes in which a leader anticipates the optimal response of a follower. Although expressive, these problems are computationally challenging because lower-level optimality is embedded in the leader's feasible region. Value-function reformulations replace the nested follower optimization with a constraint involving the follower's optimal value, but evaluating this value function exactly can itself be expensive. This paper introduces Graph4BiLO, a graph neural network (GNN) approach for learning bilevel value functions from variable--constraint graph representations. In contrast to fixed-length multilayer perceptron (MLP) representations, the GNN uses shared message-passing parameters and can therefore be applied across multiple problem sizes with a single trained model. The learned ReLU network is encoded exactly as mixed-integer linear constraints and embedded in an approximate single-level formulation. A repair step subsequently re-solves the follower problem for the selected leader decision to recover a bilevel-feasible follower response. We evaluate Graph4BiLO on knapsack interdiction instances with 20--100 items against the exact MibS solver and the learning-based Neur2BiLO method. Graph4BiLO obtains objective values comparable to Neur2BiLO across all tested sizes while avoiding size-specific neural networks. An additional out-of-distribution experiment demonstrates zero-shot transfer from 20-item training instances to previously unseen 40- and 60-item instances. However, embedding message passing at every graph node substantially increases the resulting mixed-integer formulation size and solve time. These results identify a central tradeoff between size-generalizable graph representations and the computational cost of embedding GNNs within optimization models.

---


### 304. [A Simple Transformer Pipeline for Full-Key Side-Channel Attacks on Uncropped Datasets](https://arxiv.org/abs/2608.30105)

**<font color=#1a73e8>作者：</font>** Jimmy Gammell, Kaushik Roy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep learning-based side-channel analysis has historically focused on single-byte targets and manually cropped traces, which risks discarding exploitable leakage. While recent work has proposed specialized architectures and resampling techniques to address this gap, the literature lacks a simple transformer baseline for simultaneous full-key attacks on uncropped traces. We present an open-source transformer implementation for uncropped full-key attacks which uses the standard transformer encoder backbone, adapting only the input and output layers to the side-channel setting. We release our implementation, training recipes, and pretrained weights for uncropped ASCADv1f, ASCADv1r, and CHES-CTF-2018 which achieve performance competitive with previously-reported results, while using less than 10GB of VRAM and requiring at most 3.34 hours of training on a single NVIDIA A6000.

---


### 305. [AtlasNLP: A Country-Aware Atlas of Dataset Representation in NLP](https://arxiv.org/abs/2608.30107)

**<font color=#1a73e8>作者：</font>** Joan Nwatu, Tsedeniya Solomon Amare, Longju Bai 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding which countries are represented in NLP datasets is essential for identifying gaps, targeting data collection, measuring progress, and informing AI policy. However, geographic metadata is very rarely available, and country-level representation is often hidden behind broad language-level claims. We introduce AtlasNLP, a country-aware atlas of over 13,000 NLP dataset records across normalized NLP task categories, tracking both the populations represented and where datasets are produced. AtlasNLP includes AtlasNLP-Gold, a human-curated reference set, and AtlasNLP-Core, an ACL-derived large-scale collection. Using this resource, we show that (1) dataset coverage is highly uneven across countries and tasks; (2) dataset production and representation are geographically asymmetric; and (3) language coverage does not imply geographic representation. These findings reveal blind spots in current dataset documentation practices and motivate more explicit geographic metadata for country-aware NLP evaluation.

---


### 306. [FocusAdapt: Context-aware Adaptive Focus Assistance in Diminished Reality](https://arxiv.org/abs/2608.30108)

**<font color=#1a73e8>作者：</font>** Tianyu Zhang, Shutong Wu, Jiankun Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Diminished Reality (DR) can reduce visual clutter by removing irrelevant objects. However, removing all task-irrelevant objects may eliminate useful contextual information and reduce situational awareness. We present FocusAdapt, a context-aware DR system that predicts object-level distraction by integrating visual saliency, semantic relevance, and gaze behavior. Based on findings from a formative study, FocusAdapt selectively diminishes highly distracting objects while preserving useful context, enabling adaptive focus assistance during procedural tasks.

---


### 307. [Drishti: AI-Led Human-Directed Vulnerability Auditing for 5G Cores](https://arxiv.org/abs/2608.30112)

**<font color=#1a73e8>作者：</font>** Sriram Ramachandran, Levente Csikor, Dinil Mon Divakaran  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Candidate generation for open-source vulnerabilities is no longer scarce. AI-assisted code review now produces defect candidates cheaply, and industry programs pair them with expert human triage. The remaining scarcity is validation and impact assessment, and the gap is largest in critical-infrastructure software like 5G cores. Here, validation has four costs: verification, reachability, impact, and fix-completeness. We present Drishti, an AI-led human-directed vulnerability audit framework with four components, one per cost: (i) an anti-pattern catalog for verification, (ii) critical-path triage for reachability, (iii) concentric validation for impact, and (iv) patch-review for fix-completeness. Across audits of Open5GS and free5GC, Drishti produced three findings. The first is a pre-authentication NULL-dereference in the Open5GS NRF multipart parser, fixed upstream with a CVE requested. The second is an ASN.1-PER memory amplification in the free5GC NGAP decoder. A 2-byte input from a rogue gNodeB OOM-kills the AMF in 6.2 seconds. The third is a defective patch on CVE-2025-69248 whose defense-in-depth check is dead code before authentication.

---


### 308. [Supraglacial Lake Fate Is Knowable Long Before the Season Ends](https://arxiv.org/abs/2608.30113)

**<font color=#1a73e8>作者：</font>** Emam Hossain, Md Osman Gani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A supraglacial lake on the Greenland Ice Sheet ends its melt season in one of four ways: it drains rapidly through a hydrofracture, drains slowly across the surface, refreezes in place, or is buried by late-season snowfall. Which one occurs decides whether the meltwater reaches the ice bed. Satellite classifiers recover the outcome accurately but only after the season closes, and how much of a season each outcome actually requires has never been measured. We measure it directly: holding the representation and the classifier fixed, we truncate the input at $14$ cutoffs from 1 May to 31 December, retrain at each, and record the earliest cutoff at which each outcome's per-class $F_1$ reaches a fixed target. The outcomes resolve in a consistent order, two of them months early: rapid drainage by 15 July and slow drainage by 1 August, $92$ and $75$ days ahead of the earliest date a full-season pipeline can be computed at all, with buried and refreeze following at $44$ and $30$ days. Five further learners, from a majority-class floor and $54$ summary statistics to a trigger-based early classifier, leave the ordering intact: every learner that produces a per-class trajectory reproduces it despite end-of-season accuracies differing by up to $18$ percentage points, and it survives leave-one-basin-out evaluation, though not the substitution of machine labels for expert ones in an unseen season. Every feature we compute at day $t$ reads only days up to $t$, at a cost of at most $1.3$ percentage points. A monitoring system should therefore not have one release date: rapid drainage can be flagged on 15 July, three months before a full-season pipeline can be computed at all.

---


### 309. [TPR-Attention for Combinatorial Generalization](https://arxiv.org/abs/2608.30124)

**<font color=#1a73e8>作者：</font>** Melisa Civelekoğlu, Isabeau Prémont-Schwarz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Systematic generalization remains a significant challenge in deep learning. In particular, combinatorial generalization - generalizing to new configurations of known factors of variation - is effortless for humans but difficult for standard neural architectures that rely on statistical correlations rather than explicit structural representations. We introduce a new architectural component that embeds structured inductive bias into deep learning: an attention mechanism operating over tensor-product representations (TPRs). Through controlled experiments on compositional tasks, we show that this TPR-attention mechanism outperforms existing architectural components in combinatorial generalization. These results highlight the value of integrating explicit compositional structure into neural attention and point toward a promising path for models capable of systematic generalization.

---


### 310. [Efficient and High-Quality Depth Estimation via Pixel-Space Diffusion with Linear Attention](https://arxiv.org/abs/2608.30129)

**<font color=#1a73e8>作者：</font>** Bingde Liu, Wu Ran, Jinglei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents $\textbf{Lapis}$, a $\textbf{l}$inear-$\textbf{a}$ttention-based $\textbf{pi}$xel-$\textbf{s}$pace generative framework that achieves efficient and high-fidelity depth estimation with one-step diffusion. While generative frameworks have significantly advanced monocular depth estimation with superior detail fidelity, the $\mathcal{O}(N^2)$ complexity of standard attention and the multi-step denoising process introduce prohibitive computational costs when scaling them to high-resolution image applications. Although linear attention and one-step prediction are intuitively viable, directly applying them leads to poor structural consistency, detail loss, and noise. Lapis rectifies these limitations through a coarse-to-fine hierarchy. Specifically, a Patch-level Consistency Module restores structural coherence by integrating semantic and spatial priors. Subsequently, a Pixel-level Refinement Module recovers sharp geometric boundaries via skip-connection-based pixel correspondence. Furthermore, to mitigate sampling noise inherent in one-step diffusion, we leverage the manifold assumption and adopt a direct $\mathbf{x}$-prediction strategy to target the clean data manifold. Extensive evaluations on multiple benchmarks demonstrate that Lapis consistently achieves state-of-the-art (SOTA) accuracy and boundary sharpness across various resolutions, reducing inference latency by up to 7.6$\times$ at 1080P and 10.9$\times$ at 1440P resolution compared to previous SOTA generative models.

---


### 311. [Repeatability Characterisation and Error Budget of a Consumer Structured-Light Scanner for 3-D Wound Geometry:A Rigid-Phantom Study](https://arxiv.org/abs/2608.30143)

**<font color=#1a73e8>作者：</font>** Pushkal Kumar, Aadit Aggarwal, Karlen Aleksanyan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We characterise the measurement error of a free- hand consumer structured-light scanner used to derive three- dimensional geometric wound descriptors. Rigid wound-care phantoms cannot change, so every difference between repeat scans of one site is measurement error; all repeats come from a single scanner unit, nine sites and 23 scans, so this charac- terises one instrument. The 95 percent repeatability limit for reconstructed surface area is a factor of 4.8, with a confidence interval from 3.0 to 7.0, so rescanning an unchanged site can shift the reading from a 79 percent decrease to a 377 percent increase. Forty-four of 45 descriptors fall below an intraclass correlation of 0.50, and none of 248 descriptor and pipeline combinations reaches 0.75. An error budget formed by holding the analy- sis region fixed, leaving sensor and reconstruction untouched, bounds the share of variance attributable to how much surface the operator captured at 75 percent for surface area, 91 percent for hull area and 95 percent for bounding-box diagonal; only hull volume is majority instrumental, at 48 percent, so a better sensor would buy little. No wound is delineated anywhere in the chain, so the comparison against the four-week area reduction used clinically to predict healing, a ratio near 2.1, is a lower bound on the noise an unsegmented pipeline must overcome, not a measurement of wound-area reproducibility. Standardising the analysis region cuts the limit to 2.13, meeting that ratio rather than clearing it. Statistical outlier removal imposes a measured systematic area deficit near 11 percent.

---


### 312. [CedarCypress3D: an annotated UAV-LiDAR dataset of individual trees in planted cedar and cypress forests](https://arxiv.org/abs/2608.30149)

**<font color=#1a73e8>作者：</font>** Katsuto Shimizu, Fumiaki Kitahara, Tomohiro Nishizono 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Individual tree measurements derived from Light Detection and Ranging (LiDAR) mounted on Unmanned Aerial Vehicles (UAV) provide valuable information for forest inventory, ecosystem monitoring, and sustainable forest management. Recent advancements in machine learning have increased the demand for annotated datasets to develop and evaluate point cloud-based approaches, especially for individual tree segmentation. However, publicly available annotated UAV-LiDAR datasets in temperate forests are limited. In this article, we present CedarCypress3D, a manually annotated UAV-LiDAR dataset collected in Japanese cedar (Cryptomeria japonica) and Japanese cypress (Chamaecyparis obtusa) plantations in Japan. The dataset consists of UAV-LiDAR point clouds and field survey measurements from 34 circular plots across two sites with different topographic characteristics, along with terrestrial LiDAR point clouds available for a subset of 22 plots. A total of 1,627 trees were measured in the census field survey and manually annotated to match the corresponding trees in the UAV-LiDAR point clouds. For the subset of plots with terrestrial LiDAR data, semantic labels (i.e., stem and non-stem) were additionally assigned to tree points in the UAV-LiDAR data. CedarCypress3D provides high-quality annotated UAV-LiDAR data for developing and evaluating individual tree instance segmentation and semantic segmentation methods in temperate planted forests. The dataset can also support research on tree attribute prediction and multi-platform LiDAR analysis. The dataset is publicly available at this https URL.

---


### 313. [Converse and Collision-Based Achievability for Node Localization with Hybrid Distance-Spectral Graph Positional Encodings](https://arxiv.org/abs/2608.30152)

**<font color=#1a73e8>作者：</font>** Zimo Yan, Yifan Li, Hao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph positional encodings are widely used in graph neural networks and graph Transformers, yet it remains unclear when the code itself can identify nodes. We study a hybrid distance-spectral encoding that combines anchor-distance profiles with quantized low-frequency Laplacian-energy coordinates. Treating the encoding as an observation map yields a simplex-refined converse, an exact collision factorization \(\kappa_H=\kappa_D\kappa_{S|D}\), and the collision information \(I_H=-\log\kappa_D-\log\kappa_{S|D}\). On random regular graphs, the criterion is made explicit through a bounded-correlation Gaussian-wave surrogate; for actual Laplacian-energy coordinates, we give the distance-conditioned spectral collision condition sufficient for conditional actual-coordinate achievability. Experiments show that \(I_H/\log n\) calibrates localization success, and PE-only structural task probes on Universal Dependencies trees show that hybrid encodings better recover syntactic-tree geometry than distance-only or spectral-only baselines.

---


### 314. [AI-enabled Low-Cost 3D Maize Ear Morphometry Platform at Breeding Scale](https://arxiv.org/abs/2608.30161)

**<font color=#1a73e8>作者：</font>** Therin Young, Elijah Rodriguez, Lisa Coffey 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maize ear geometry (length, width, curvature, and volume) is closely tied to yield and grain-filling outcomes, but existing high-throughput phenotyping pipelines remain constrained by the cost, labor, and specialized hardware they require. We developed and validated a low-cost pipeline that reconstructs a watertight 3-D mesh of a maize ear from a single 20-second video captured with a consumer-grade DSLR on a motorized turntable under uniform LED illumination. Camera poses from a multi-seed COLMAP procedure initialize a Neural Radiance Field (NeRF), and a cylindrical holder of known diameter, visible in every frame, provides automatic metric scaling with downstream geometric quality control. Applied to 300 ears spanning a diverse maize inbred panel, 250 (83.3%) passed automated processing and quality control. Skeleton length agreed with manual caliper measurements across all 250 ears (R^2 = 0.964, RMSE = 4.68 mm), and convex-hull volume agreed with water-displacement volume on a 15-ear subset spanning the full size range (R^2 = 0.982, RMSE = 5.26 mL). Residual length error grew with ear curvature, whereas bounding-box height, which records the same straight-line chord as calipers, showed no such trend; the discrepancy therefore originates in the measurement definition, since calipers record the chord while skeleton length traces the geodesic arc. The capture hardware costs approximately 607 USD, and operator involvement fell from roughly five minutes to one minute per ear, with all downstream processing running unattended. The platform provides a foundation for breeding-scale 3-D ear phenotyping.

---


### 315. [Reinforcement Learning for Symbolic Equation Solving](https://arxiv.org/abs/2608.30162)

**<font color=#1a73e8>作者：</font>** Kevin P O Keeffe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a reinforcement-learning agent that solves symbolic equations step by step, covering both nonlinear closed equations (radicals, exponentials, trigonometric) and a controlled class of restricted-open families requiring a change of variables (CoV) such as completing the square. We cast algebra as an MDP with a dynamic action space and a tree-structured policy (TreeMLP). The main policy learns from reward alone with no supervised solution traces; the CoV substitution comes from a supervised generator interchangeable with a CAS call. On closed equations the agent matches the prior best on CommonCore (0.93 greedy vs. ConPoLe's 0.925) under a single policy. On four hand-designed restricted-open families (quadratic, cubic, quartic, exponential) it reaches 0.79 beam / 0.67 greedy, exceeding the strongest non-learned search (A-star, 0.64). Learned CoV timing has content only on the exponential family, the one requiring a nested CoV, where a natural rule solves none of the held-out equations while the policy solves 75% from reward alone. At 10x scale a sharp seed-level bimodality emerges; a UCB learning-progress curriculum shows a non-significant positive trend toward mitigating it. We do not claim general open-equation solving: every open-equation result is confined to these four controlled families.

---


### 316. [Reducio: Optimized Confidential Serverless Cloud Deployments for Enterprise Customers](https://arxiv.org/abs/2608.30171)

**<font color=#1a73e8>作者：</font>** Vikram Ramaswamy, Chuqi Zhang, Adil Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Serverless platforms based on Confidential Virtual Machines (CVMs) have been recently proposed to address the privacy problems with serverless functions, while achieving low latency. Unfortunately, our study indicates that to achieve these properties, existing proposals impose non-trivial requirements in terms of infrastructure changes and platform memory. Reducio is an alternate serverless platform design that does not require infrastructure changes and significantly reduces platform memory requirements. The platform is designed using two key components: (1) a function isolation framework inside a CVM based on kernel deprivileging features that minimize infrastructure requirements, and (2) a layer-wise caching methodology and algorithm that effectively uses a small in-memory function cache. Our evaluation indicates that Reducio can significantly reduce both platform requirements for deployment and function memory consumption.

---


### 317. [Benchmarking Peptide-Protein Affinity Prediction Across Peptide and Target Shifts](https://arxiv.org/abs/2608.30175)

**<font color=#1a73e8>作者：</font>** Jiaxin Tian, Darren An, Jun Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Peptide-protein affinity models are often evaluated with a single data split, obscuring whether they interpolate among measurements for observed targets or generalize across peptide or target shifts. We integrated three sources of quantitative peptide-protein binding data to obtain 11,349 deduplicated pairs and benchmarked ten peptide representations, ESM-2 protein embeddings, and six regressors under peptide-similarity, within-target, and leave-target-out partitions. Across 60 matched representation-regressor configurations, mean test Spearman correlations were 0.462, 0.669, and 0.530, respectively. The top configuration shifted from ECFP-16 count fingerprints with random forest in the first two settings to HELM-BERT with Extra Trees when exact target sequences were excluded. Representation-rank correlations ranged from -0.042 to 0.624 across partitions, whereas regressor-rank correlations ranged from 0.771 to 0.943. Learning curves showed that representation differences were largest with limited supervision and narrowed as training data increased. PeptideCLM-2 adaptation and simple element-wise interaction features provided no consistent gain over a frozen encoder and direct concatenation under the tested protocols. These conclusions are specific to a dataset that pools transformed Kd, Ki, and IC50 measurements and to target exclusion at the exact-sequence level. Peptide-protein affinity benchmarks should therefore align data partitions with the intended use and jointly assess the effects of data scale, molecular representation, and downstream learner.

---


### 318. [ATGS: Anchored Temporal Gaussian Splatting for Long Volumetric Video Representation](https://arxiv.org/abs/2608.30184)

**<font color=#1a73e8>作者：</font>** Jiahao Wu, Jie Liang, Die Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Volumetric video enables immersive free viewpoint rendering of dynamic real world scenes, yet existing methods struggle with long sequences and complex motions, often leading to temporal instability and visual artifacts. To address these challenges, we propose \ourname, a Gaussian splatting based framework for volumetric video reconstruction. Our key insight is that explicitly tracking long term complex motion with individual Gaussian primitives is inherently unstable. Instead, we organize Gaussians around time conditioned anchors that localize their spatial and temporal support, thereby reducing long range motion complexity. We further introduce a temporal windowing strategy to activate only anchors relevant to the queried time, which improves scalability and temporal coherence. In addition, to ensure spatial and temporal stability, we design a compact set of multi level anchor features that encode global features, local spatial features, and local temporal features, jointly constraining Gaussian generation. Extensive experiments demonstrate that \ourname \ consistently outperforms prior methods on long sequence volumetric videos with complex motions. Project page: this https URL.

---


### 319. [Certified Safety Radii in Forecast-Error Space for Wasserstein Distributionally Robust Small Signal Stability-Constrained AC Optimal Power Flow via Lifted Spectrahedral Containment](https://arxiv.org/abs/2608.30201)

**<font color=#1a73e8>作者：</font>** Ziqi Zhang, Xi Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Directly robustifying small-signal stability in AC optimal power flow is challenging since the stability boundary in the original uncertainty space is implicit, highly nonconvex, and changes with the operating decision. This paper exploits an alternative geometry. For a fixed model-specific stability certificate admitting suitable physical lifts, the small-signal stability requirement becomes an affine positive semidefinite constraint in the lifted variables, thereby defining a convex certified safe region. Instead of approximating the nonlinear instability boundary itself, we optimize a sample-wise safe radius in the original uncertainty space and certify, in the lifted space, that the entire power-flow image of the corresponding uncertainty ball is contained in the convex stability region. To this end, a componentwise Perron certificate guarantees existence, uniqueness, and Jacobian regularity of the target AC power-flow branch throughout each ball. An adjoint elimination then provides an exact affine-quadratic representation of the stability-relevant quantities, while rigorous matrix remainder bounds convert their nonlinear variation into finite robust PSD constraints. The resulting radii are certified lower bounds on the distances from empirical samples to failure and can therefore be coupled directly to the distance-based reformulation of a Wasserstein distributionally robust chance constraint, without directly approximating the instability boundary. Numerical studies demonstrate the effectiveness of the proposed framework.

---


### 320. [Diffusion-Based Refinement for Kilometer-Scale Probabilistic Precipitation Nowcasting](https://arxiv.org/abs/2608.30205)

**<font color=#1a73e8>作者：</font>** Dohyun Park, Changhoon Song, Tengyuan Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Localized extreme precipitation is a major trigger of urban flash floods and landslides, yet producing nowcasts that combine fine spatial detail with probabilistic uncertainty remains challenging. Here we introduce exPreCast-ENS, a conditional residual diffusion framework that transforms the deterministic 4 km radar nowcaster exPreCast into a 1 km probabilistic ensemble while correcting systematic forecast errors. Conditioning on both the forecast and preceding radar observations lets the ensemble-mean correct the baseline rather than perturb it, while members represent unresolved fine-scale variability. Over the Korean Peninsula, skill improves with ensemble size. In two high-impact events in 2023, a 30-member ensemble recovers 38-47% of heavy-rain pixels missed by exPreCast while retaining approximately 95% of its correct detections and alarming on under 1% of the pixels it correctly left clear. The method generates a 1-h forecast in 3.4 s on a single GPU and yields consistent improvements on the French regional MeteoNet radar dataset.

---


### 321. [SPARK: Skeleton-Guided Reasoning Synthesis from Large-Scale Scientific Literature](https://arxiv.org/abs/2608.30214)

**<font color=#1a73e8>作者：</font>** Yu Li, Wei Li, Xin Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific reasoning remains challenging for open-source models, largely due to the lack of high-quality scientific reasoning data. Existing datasets are often dominated by factual recall or formulaic problem solving, with limited emphasis on mechanism understanding, evidence-grounded reasoning, and hypothesis evaluation. To address this, we introduce SPARK (Scientific Paper Abstracted Reasoning sKeleton), a paper-oriented synthesis framework built on Sci-Base, a large-scale corpus of research papers spanning 10 scientific disciplines. Instead of directly converting papers into question-answer pairs, SPARK treats the claim-evidence-derivation structure of a paper as the fundamental unit of reasoning synthesis. Specifically, SPARK (1) distills each paper into a compact reasoning skeleton capturing its central claims and supporting evidence, enabling self-contained question generation, and (2) synthesizes reasoning tasks from four scientific perspectives: mechanistic reasoning, hypothesis falsification, quantitative derivation, and boundary calibration. A final consistency verification stage further removes unsupported or contradictory outputs. Using this framework, we construct Spark-234K, a scientific reasoning dataset with substantially higher difficulty and diversity than existing resources. Experiments show that Spark-234K consistently outperforms existing scientific reasoning datasets while achieving stronger performance with significantly fewer training samples.

---


### 322. [Label Semantic Expansion via Label Guided Neural Topic Modeling](https://arxiv.org/abs/2608.30216)

**<font color=#1a73e8>作者：</font>** Haojia Zheng, Yuyin Lu, Juntian Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Topic models are widely used for content analysis, where users often analyze corpora around predefined labels rather than unordered latent topics. Existing label-aware topic models mainly follow a labels-for-topics perspective, using labels to guide topic learning, while the learned topics are not directly usable for label-centered analysis. We explore the reverse topics-for-labels perspective and instantiate it as Label Semantic Expansion (LSE), which enriches sparse label representations with corpus-grounded descriptive topic words. To exploit topics in LSE effectively, we propose a Label-Guided Neural Topic Model (LGNTM), which learns dedicated label-aligned topics, grounds them in lexical and document semantic spaces, and preserves consistency between topic structures and label structures. Experiments on label-topic alignment, label expansion, topic quality, and downstream classification demonstrate strong overall performance across complementary evaluation dimensions.

---


### 323. [Amortized Anchor Refinement for Deployable Continuous-Time 4D Gaussian Reconstruction](https://arxiv.org/abs/2608.30218)

**<font color=#1a73e8>作者：</font>** Jingong Chen, Qingwen Zhang, Sanghyeon Jun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous-time 4D reconstruction remains impractical on standalone XR headsets. Per-scene optimization demands deployment-infeasible compute, and lower budgets cause collapse rather than degrade gradually. Feed-forward prediction is fast, but struggle to recover scene-specific detail. We present Amortized Anchor Refinement, which uses a frozen backbone to predict an initial Gaussian representation and a short optimization to specialize it under a fixed compute budget, with a capacity floor preserving representational density. A training-free stage then applies a persistent-homology constraint to prune unstable Gaussians while preserving topologically persistent structures, and streams the resulting trajectories directly as scene flow. On the Stage-Capture benchmark, Amortized Anchor Refinement achieves 24.31$\pm$2.22dB, while our deployment experiments demonstrate reconstruction within the target budget on a single consumer GPU and playback on a standalone XR headset.

---


### 324. [Rethinking the Test-Time Prompt Tuning Objective from the Perspective of Calibration](https://arxiv.org/abs/2608.30230)

**<font color=#1a73e8>作者：</font>** Jungwon Choi, Hyeonseo Jang, Kibok Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time prompt tuning (TPT) has emerged as a powerful paradigm, refining prompts for each test sample via entropy minimization (EM) over multiple augmented views. However, we identify a limitation in the standard EM-based adaptation: it inherently drives the model toward overconfident predictions disregarding sample-specific uncertainty, leading to significant calibration degradation. To address these limitations, we propose a new objective that replaces the conventional EM loss by aligning the original-view prediction with a target distribution derived from augmented views via cross-entropy, while adversarially incorporating the entropy of the target distribution to capture sample-specific uncertainty. Furthermore, to better construct this target distribution, we apply confidence-aware temperature scaling to each augmented-view prediction according to its confidence, sharpening confident predictions while softening uncertain ones. This formulation allows the model to increase confidence only when the target distribution is reliable, while preserving uncertainty when it reflects ambiguous or conflicting augmented-view predictions. Extensive experiments across diverse benchmarks demonstrate that our approach not only achieves state-of-the-art accuracy but also significantly improves model calibration.

---


### 325. [Semantic-Spatial Discriminability Enhancement for Generalized Visual Grounding](https://arxiv.org/abs/2608.30233)

**<font color=#1a73e8>作者：</font>** Kaiyan Lei, Xu-Yao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized Visual Grounding (GVG) task aims to localize targets in an image based on referring expressions, extends the classical visual grounding paradigm by integrating multi-target and non-target scenarios. Previous methods typically rely on global semantic matching or coarse-grained region interactions for localization, where the discriminative cues are primarily derived from sentence-level semantics or regional context. In complex multi-target scenarios, such approaches tend to confuse visually similar targets, making it difficult to establish stable instance-level decision boundaries. To address these limitations, this paper proposes a novel Semantic-Spatial Discriminability Enhancement (SSDE) framework for generalized visual grounding, which aims to enhance the discriminative ability on fine-grained semantics and spatial localization, improving both cross-modal understanding and instance-level grounding. Specifically, to enhance the semantic discriminability of query representations at the fine-grained level, we propose a Semantic Discriminability Enhancement (SeDE) module, which leverages spatially guided cross-attention to disentangle fine-grained target-relevant visual attributes and integrates them with the textual subject semantics. Furthermore, to strengthen the spatial discriminability of the referred targets, we introduce a Spatial Discriminability Enhancement (SpDE) module, which models an instance center density map to characterize the spatial distribution of targets, and explicitly constructs instance separation structures in the spatial domain by employing them as an auxiliary supervision signal. Extensive experiments show that SSDE achieves superior performance on ten datasets across both classic and generalized visual grounding tasks.

---


### 326. [CoLa-ICD: A Knowledge-Enhanced Framework for Long-Tail Automated Medical Coding](https://arxiv.org/abs/2608.30234)

**<font color=#1a73e8>作者：</font>** Yihang Cheng, Veronica Liesaputra, Andrew Trotman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic medical coding assigns ICD codes to clinical notes, but it remains challenging due to long documents, imbalanced label distributions, and diverse terms. These challenges are especially severe for rare codes, which have limited training instances and are easily confused with semantically similar labels. We introduce CoLa-ICD, a knowledge-enhanced framework for long-tail prediction. CoLa-ICD enriches ICD labels with external terms, models dependencies among related codes, and learns stronger alignment between label semantics and clinical evidence for long-tail prediction. Experiments show that CoLa-ICD improves long-tail prediction with larger gains in larger and sparser label spaces and achieves state-of-the-art performance in AUC, F1, and P@k. Our code is available at this https URL.

---


### 327. [PaperBanana-Interact: Scientific Diagram Refinement with Multi-Turn Human Feedback](https://arxiv.org/abs/2608.30241)

**<font color=#1a73e8>作者：</font>** Xueqing Wu, Ashwin Balasubramanian, Bingxuan Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent efforts have aimed to automate scientific diagram generation from paper content (Lin et al., 2026; Zhu et al., 2026a). However, fully satisfying an author's visual and communicative preferences in a single turn is challenging: in our formative user study (N = 14), all participants requested further revisions after viewing an initial draft, and 86% of them rated the refined diagrams as more satisfactory. Despite the clear demand, the multi-turn workflow remains largely underexplored. To bridge this gap, we present MTPaperBananaBench, a benchmark for multi-turn diagram generation containing 292 images annotated with 3,518 user requirements. To reduce expensive human studies and enable scalable benchmarking, we construct a user simulator that, at each turn, identifies unsatisfied requirements and converts k of them into natural language feedback. Evaluating both requirement satisfaction and overall diagram quality reveals two key failure modes shared across baseline multiturn systems: (1) quality drift, where diagram quality progressively declines over turns, and (2) forgetting, where previously implemented features are lost in subsequent turns. To address these issues, we introduce PaperBanana-Interact, a multi-agent system that refines diagrams via an internal critique-and-refine loop. PaperBanana-Interact consistently improves rather than degrades diagram quality across turns, outperforming baselines by 11.9-18.6 points in quality score and reducing forgetting by 3.7-6.2 points.

---


### 328. [OPUS: A Simple yet Effective Unified Framework for Open-Vocabulary Detection](https://arxiv.org/abs/2608.30247)

**<font color=#1a73e8>作者：</font>** Xiaoyan Wei, Zhimin Yao, Ruilin Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent unified open-vocabulary detection (OVD) supports heterogeneous prompts, including text queries, visual exemplars, and their combinations, but often rely on increasingly complex designs such as heavy cross-modal fusion, staged training, and iterative annotation pipelines. We revisit whether such complexity is necessary in the era of stronger foundation models. Our finding is that unified OVD can be made substantially simpler with semantic-rich visual representations and scalable grounding supervision. We present OPUS (\textbf{O}pen-vocabulary, \textbf{P}rompt-\textbf{U}nified, \textbf{S}imple), a unified detector supporting text, interactive visual, generic visual, and mixed prompting within one framework. OPUS adopts a simple three-part design. Its model architecture combines a semantic-rich visual encoder, built on a DINOv3-ConvNeXt-B backbone with efficient hybrid encoding, with a prompt-aware decoder that avoids prompt-specific branches for unified prompt reasoning. OPUS is trained with a one-stage text-visual training strategy with Instance-level Contrastive Alignment (ICA), and is supported by a SAM3-based single-pass data engine for heterogeneous grounding supervision. Experiments on COCO, LVIS-minival, and ODinW35 show that OPUS achieves state-of-the-art Visual-I performance, reaching 68.1/69.2/54.7 AP, while maintaining balanced Text and Visual-G accuracy. OPUS also turns mixed prompting from interference into complementarity, improving over text or visual prompt alone. These results show that simplicity and strong unified prompting capability can be achieved together.

---


### 329. [Exact Recovery Thresholds for Weighted Data Selection in Vector-Valued Linear Regression](https://arxiv.org/abs/2608.30254)

**<font color=#1a73e8>作者：</font>** Guangjian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We resolve the threshold part of Question 4 of the COLT 2025 open problem "Data Selection for Regression Tasks" of Hanneke, Moran, Shlimovich and Yehudayoff. In vector-valued linear regression with square loss $\ell_{(x,y)}(W)=|Wx-y|_2^2$, where $x\in\mathbb{R}^d$, $y\in\mathbb{R}^m$ and the learner is the empirical risk minimizer of minimal Frobenius norm, we prove that the minimal budget of weighted examples that recovers the full-data loss on every finite dataset is exactly $n^*(d,m)=(m+1)d$. We further determine two more values of the weighted selection profile $F_w(d,m,n)$: at the near-threshold budget, $F_w(d,m,(m+1)d-1)=1+\frac{1}{dm^2}$, and at the spanning budget, $F_w(d,m,d)=d+1$ for every $m$, while $F_w(d,m,n)=\infty$ for $n<d$. For the smallest open intermediate cell $(d,m)=(2,2)$ we prove $F_w(2,2,3)\in[13/8,15/8]$ and $F_w(2,2,4)\in[5/4,3/2]$, reduce the conjectured exact values $13/8$ and $5/4$ to a finite moment problem on the circle with at most seven atoms, and establish strong structural evidence for the conjecture. The upper-bound techniques (a fixed-basis conic compression lemma, a determinant-facet rigidity theorem for maximal certificates, and sharp sparsification lemmas for zero-mean weighted point systems) are of independent interest. As a byproduct we correct an erroneous claim circulating in a recent unrefereed preprint, exhibiting an explicit dataset with $m=2$ on which no weighted selection of $2d$ points recovers the optimal loss. All results are new only for $m\ge 2$; the scalar case $m=1$ is due to Hanneke et al.

---


### 330. [Multivariate Scientific Data Compression with Learned Cross-Variable Latent Decorrelation and Autoregressive Entropy Modeling](https://arxiv.org/abs/2608.30262)

**<font color=#1a73e8>作者：</font>** Liangji Zhu, Anand Rangarajan, Sanjay Ranka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific simulations generate collections of physical fields with heterogeneous statistics and dependencies, yet learned compressors often encode those fields independently or rely on a shared encoder without explicitly modeling the structure that remains in latent space. We present CAESAR-LDAR, an error-controlled multivariate learned compressor that augments a shared CAESAR-V backbone with two complementary mechanisms: a trainable orthogonal transform that reorganizes dependence across aligned latent channels, and a causal autoregressive hierarchical prior that captures local spatial structure left after transformation. Orthogonality is maintained through a matrix-exponential parameterization, making the transform exactly invertible without an additional penalty. A common residual-correction stage is applied uniformly to all variants to enforce the requested reconstruction tolerance.
Experiments across combustion, climate, and turbulence data show that the two mechanisms are useful in different regimes. Latent decorrelation helps most when substantial linear cross-channel dependence survives the nonlinear encoder, whereas autoregressive modeling remains effective when the remaining structure is primarily local or spatial. Their combination provides the strongest or near-strongest rate-distortion performance across the evaluated datasets. The global transform adds little computational overhead, while autoregressive coding introduces a larger throughput tradeoff. More broadly, the results suggest a practical design principle for multivariate scientific compression: exploit global cross-channel dependence when it is measurably present in latent space, and use local probabilistic context as a complementary mechanism across a wider range of data regimes.

---


### 331. [Read the Room, Read the Image: Understanding Indirect Speech Acts in Multimodal Visual Contexts](https://arxiv.org/abs/2608.30270)

**<font color=#1a73e8>作者：</font>** Jaehee Kim, Ji Hoon Chung, Seoyoon Park 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Indirect speech acts (ISAs) require pragmatic reasoning over context, as directive intent can- not be inferred from surface form alone. Prior text-based studies and existing multimodal benchmarks largely overlook this requirement, focusing instead on explicitly encoded context or perceptual recognition, and thus underex- plore context-dependent pragmatic understand- ing, particularly in high-context languages such as Korean. We introduce READI, a multimodal benchmark for evaluating ISA understanding through integrated reasoning over visual con- text and dialogue. READI models graded in- directness grounded in pragmatic theory and formulates the task as vision-based pragmatic question answering (V-PQA), supporting cross- lingual evaluation in English and Korean. Ex- periments show that even state-of-the-art multi- modal models struggle with visually grounded indirect speech acts, with performance declin- ing as indirectness increases, underscoring the need for benchmarks that explicitly target con- textual pragmatic reasoning.

---


### 332. [Motion-Saliency Complementary Masked Modeling for Point Cloud Video Understanding](https://arxiv.org/abs/2608.30279)

**<font color=#1a73e8>作者：</font>** Wei Wang, Yiding Sun, Yuyan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud video representation learning is crucial for 3D dynamic scene understanding. In this paper, we propose MoSaiC, a novel Motion-Saliency Complementary masked modeling framework for self-supervised point cloud video representation learning. MoSaiC couples three components: Curriculum Motion-Saliency Masking (CMSM), which guides the masking process toward motion-salient tokens under a curriculum schedule; Normal-Flow Motion (NFM) modeling, which supervises the local rigid rotation of each token in the Lie algebra so(3) as an explicit geometric motion target; and Cross-view Token Consistency Prediction (CTCP), which enforces consistency between two complementary masked views at the token level. Together, these components allow MoSaiC to effectively capture both appearance and motion dynamics. Extensive experiments on multiple downstream tasks, including action recognition, temporal action segmentation, and point-level semantic segmentation, demonstrate the effectiveness of our approach.

---


### 333. [SELECT: SELEctive Context Transfer for Class-Incremental Semantic Segmentation](https://arxiv.org/abs/2608.30281)

**<font color=#1a73e8>作者：</font>** Avi Gupta, Saurabh Yadav, Koteswar Rao Jerripothula 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-Incremental Semantic Segmentation (CISS) is fundamentally challenged by catastrophic forgetting and background shift, where learning new concepts degrades performance on previously seen classes. While existing methods attempt to balance stability (retaining old knowledge) and plasticity (learning new knowledge), they often fail to leverage prior knowledge effectively. These approaches typically rely on indiscriminate knowledge transfer or ambiguous initializations, which can dilute crucial semantic information. To overcome this limitation, we propose SELECT, a novel approach for Selective Context Transfer, which instead grounds each new class in a small set of semantically similar past classes. Its core is a Context Transfer Attention mechanism that aggregates the learned tokens from similar classes into a structured initialization for the new class. To ensure this transfer does not corrupt the borrowed representations, we add a controlled noise perturbation and a margin-based context-transfer loss that enforces separation between the new class token and its source tokens. Extensive experiments on Pascal VOC and ADE20K show that SELECT consistently outperforms prior work, achieving mIoU of 2.2% on VOC and 2.8% on ADE, providing an effective handle on the stability-plasticity dilemma. Code is available at this https URL.

---


### 334. [BCPPO: Bachelier-Inspired Constrained Proximal Policy Optimization for Tail-Risk-Aware Safe Reinforcement Learning](https://arxiv.org/abs/2608.30283)

**<font color=#1a73e8>作者：</font>** Dongsheng Hou, Yanqiao Chen, Yuhan Rui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Expected-cost constraints can still permit rare, high-cost events. Monte Carlo conditional value at risk (CVaR) gradients can be noisy at high confidence, whereas critics that model an outcome distribution add complexity. We propose BCPPO (Bachelier-Inspired Constrained Proximal Policy Optimization), a proximal policy optimization (PPO) method. Separately initialized cost-prediction networks (critics), trained with random sample masks, produce disagreement that marks predictions sensitive to which state-action regions occur in the training data and to critic training. A Bachelier formula for the expected amount above a reference level converts this disagreement into a smooth policy-update penalty. Gradients from this penalty do not alter the critics, so temporal-difference (TD) critic learning is unchanged. A saturation-aware controller adjusts the mean-cost penalty and stops accumulated error from growing while that penalty is clipped. Deployment retains only the policy network. The disagreement penalty is neither a tail-event probability nor a guaranteed error bound, and it provides no safety guarantee. Across 175 runs with shared tasks, costs, budgets, training steps, and evaluation seeds, no comparator attains both higher mean return and lower mean CVaR than BCPPO in any task. On Push1, BCPPO has no lower return and no higher CVaR than every comparator, with at least one strict gain. These results support a practical balance among reward, caution around cost predictions that vary across trained critics, and policy-only deployment.

---


### 335. [Lazy Grounding: Attacking Search Agents with Factual Evidence](https://arxiv.org/abs/2608.30303)

**<font color=#1a73e8>作者：</font>** Yulin Zhang, Yukun Huang, Sanxing Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search agents reduce hallucination by grounding answers in retrieved web evidence. Yet reliance on retrieval also creates an attack surface: poisoned corpora with false or malicious documents can cause agents to reproduce misinformation. We show that falsehood is not necessary -- a search agent can be misled by factual evidence for a nearby question, adopting that nearby answer even when it does not answer the current question. We call this failure lazy grounding. We expose lazy grounding using nearby evidence from answer-changing rewrites of benchmark questions. Each document truthfully supports a neighboring rewritten question, but is surfaced for the original question. Across 12 model-benchmark pairs, nearby evidence reduces accuracy by 5.9 points on average and by up to 17.3 points, while inducing nearby-answer adoption in every setting. The effect is stronger when nearby evidence appears later or is more answer-shaped. Our results show that robust search agents must defend against not only misinformation but also the misapplication of factual evidence. The code is publicly available at this https URL.

---


### 336. [Learning to Restore More: Continual Capability Expansion for Pretrained Image Restoration Models](https://arxiv.org/abs/2608.30305)

**<font color=#1a73e8>作者：</font>** Hu Gao, Yulong Chen, Lizhuang Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration models are typically trained with a fixed set of capabilities. When new restoration requirements emerge, existing solutions usually train additional models or jointly retrain the original model with both new and historical data. Instead of designing another restoration backbone, we investigate how a trained restorer can continually acquire new capabilities without forgetting those learned previously. We propose RestoreMore, a continual capability-expansion framework that preserves the pretrained restoration model as a frozen capability anchor and learns residual expansion modules for newly arriving degradations. RestoreMore introduces a capability-oriented bi-level routing mechanism at multiple feature stages. The first routing level identifies restoration capabilities relevant to the current input, while the second selects and combines a sparse set of complementary degradation experts. This design enables newly introduced tasks to selectively reuse historical restoration knowledge and progressively enriches the expert bank available for subsequent restoration tasks. Extensive experiments on a wide range of restoration benchmarks demonstrate that RestoreMore consistently acquires new restoration abilities while preserving and improving previously learned capabilities.

---


### 337. [One AI Signal, Many Human Judgments: A Bayesian Cascade Analysis of AI-based Credibility Indicators in Online Information Spread](https://arxiv.org/abs/2608.30311)

**<font color=#1a73e8>作者：</font>** Zhuoran Lu, Weilong Wang, Yangyang Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social media platforms increasingly use AI-based credibility indicators to help users judge misinformation. Unlike individual human-AI decision-making, these indicators are embedded in information spread: users see both an AI prediction and earlier judgments shaped by the same AI, and their own judgments may then enter the public history. Yet how to analytically characterize this process remains under-explored. We therefore introduce a social-learning lens for this setting by extending the classical Bayesian cascade model with the AI indicator as a shared public signal. The resulting Gateway condition compares the evidence from the AI prediction with users' private impressions. Through this view, we show that AI changes what public history means. Crowd agreement may reflect accumulated independent human evidence, or repeated dependence on the same AI prediction. This creates a preservation-correction trade-off: stronger reliance on AI can preserve correct predictions, but can also lock in incorrect ones by blocking corrective private impressions. We calibrate the model using human-subject data on news veracity judgments. Although the AI outperforms human users, the average user weights it below her own impression but above several peer judgments, while individual users vary from discounting the AI to relying on it enough to cascade. Simulations show that over-reliance on a weak AI is especially harmful, and that diversifying AI signals across users can better keep the crowd informative. We conclude with implications for understanding human-AI interaction in information spread and designing misinformation interventions.

---


### 338. [Knowing Beyond the Known: Reinforced Knowledge Specification for Multi-Label Class-Incremental Learning](https://arxiv.org/abs/2608.30316)

**<font color=#1a73e8>作者：</font>** Aoting Zhang, Dongbao Yang, Chang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing class-incremental learning methods struggle in multi-label scenarios (MLCIL) due to the inherent contradiction of learning objectives arising from co-occurring and incomplete labels. We argue that the core obstacle is the model's ambiguous boundary between known and unknown knowledge, which undermines historical knowledge retention, complicates current task learning, and limits adaptability to future concepts. To address this, we propose KBK (Knowing Beyond the Known), a reinforced knowledge specification framework that explicitly models what is known or not to unify historical, current, and prospective learning. Specifically, to clarify known knowledge, we develop a hierarchical feature purification module that disentangles fine-grained class-specific features from global features, where high-level semantic abstraction is reinforced with low-level visual features. Additionally, an uncertainty-aware recall enhancement strategy suppresses unreliable predictions based on distribution priors, improving the quality of historical recall. For probing the unknown, KBK leverages semantic correlations to synthesize informative unknown features under co-occurring, preserving embedding space for future learning. Furthermore, to mitigate heterogeneous forgetting, we design a category-balanced gradient compensation loss that dynamically reweights gradient backpropagation according to forgetting speeds. Experiments on multiple benchmarks validate the effectiveness and robustness of KBK, which surpasses prior best methods by 2.7% in Avg. Acc on MS-COCO B0-C10 setting even without any replay buffers.

---


### 339. [Online Estimation of Dynamic Origin-Destination Matrices Using Reinforcement Learning with Link-Flow Propagation Guidance](https://arxiv.org/abs/2608.30317)

**<font color=#1a73e8>作者：</font>** Donggyu Min, Dong-Kyu Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online dynamic origin-destination (OD) matrix estimation (DODE) calibrates time-dependent OD demand to reproduce observed link-flow trajectories. In online, OD demand should be estimated from current observations and propagated network states while subsequent observations and stochastic dynamic network loading (DNL) outcomes remain uncertain. Recently, reinforcement learning (RL) has emerged as a promising alternative, reducing computational burden by replacing iterative algorithms while being applicable to stochastic environments. However, because the policy is trained offline and deployed online, it must handle varying target link-flow trajectories; since each target trajectory defines the link-flow error used in the reward, the same OD demand vector can require different adjustments, making conventional scalar feedback ambiguous. To address this gap, this study proposes LFPG-RL, which integrates link-flow propagation guidance (LFPG) into proximal policy optimization (PPO). LFPG combines link-flow error sensitivities with the contribution of each OD-time demand component to simulated link flows, transforming aggregate mismatch into OD-specific advantage shaping for PPO actor updates. At deployment, the policy requires only a single forward pass. LFPG-RL is developed and evaluated on 250 weekday trajectories of 15-min link-flow data from a Melbourne arterial network modeled by a link transmission model with stochastic route choice. On held-out trajectories, LFPG-RL achieved an RMSE of 4.69, MAPE of 20.15%, and Pearson correlation of 0.995. These results support the contention that our method is a more efficient and accurate online OD demand calibration method compared to existing ones.

---


### 340. [Generative multi-domain transfer learning for fault detection in data-scarce wind turbines](https://arxiv.org/abs/2608.30323)

**<font color=#1a73e8>作者：</font>** Stefan Jonas, Angela Meyer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Normal behavior models have shown promise for reliable fault detection in wind turbines. However, these unsupervised anomaly detection models require sufficient fault-free training data to learn the normal operation behavior of turbines. Under data scarcity, for example in newly deployed wind turbines, these models may result in poor fault detection performance. In this work, we propose a multi-domain generative domain mapping approach based on Star Generative Adversarial Networks (StarGAN) to improve fault detection on data-scarce wind turbines. Our model maps SCADA measurements from a data-scarce turbine to resemble those of several data-rich turbines. By preserving the operational state during translation, faults occurring in a data-scarce domain can be mapped and detected by reliable pre-trained normal behavior models of data-rich domains. Highlighting the benefits of an ensemble fusion strategy, we show that under severe data scarcity our method can produce anomaly scores comparable to models trained on large representative datasets. Our approach can consistently outperform models trained on scarce data when less than 2 weeks of training data are available. With just 2 weeks of accumulated training data, we achieve an anomaly score similarity that is, on average, +16% higher than conventional fine-tuning, and +10% higher than single-source domain mapping. As a step towards unsupervised model selection, we propose a proxy metric that detects poor performance at training time, despite an absence of anomalies. Our study presents the potential and challenges of multi-domain mapping for wind turbine fault detection under unrepresentative training data.

---


### 341. [Learning PDE Time-Stepping with Neural Cellular Automata](https://arxiv.org/abs/2608.30328)

**<font color=#1a73e8>作者：</font>** Esha Saha, Hao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical numerical solvers for partial differential equations (PDEs) are computationally expensive to solve repeatedly across varying initial conditions, motivating the need for learned surrogates. In this paper, we propose a trainable Neural Cellular Automata (NCA) based surrogate model for learning long time PDE dynamics. Rather than mapping an entire initial field to a full trajectory in one shot, our proposed model learns a small, local, homogeneous update rule that is applied identically and repeatedly at every grid cell, mirroring the locality of differential operators. We benchmark this framework against three baselines: PDE - Net, a modified physics-informed neural network (PINN), and a Fourier Neural Operator (FNO), on five canonical PDEs (heat, advection, Burgers, Allen - Cahn, and Fisher - KPP), evaluated at temporal domain two times beyond the training temporal domain. The proposed model achieves the lowest long-horizon relative errors on the majority of the experiments.

---


### 342. [A Roadmap to Available ICS Datasets and Testbeds for Cybersecurity Research](https://arxiv.org/abs/2608.30332)

**<font color=#1a73e8>作者：</font>** Ebtesam J. Alqahtani, Mohammad Hammoudeh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Industrial Control Systems (ICS) are the backbone of many critical infrastructure sectors; however, their growing level of connectivity, long lifespan and integration with the Information Technology (IT) environment introduces numerous cybersecurity challenges. The merging of Operational Technology (OT) and IT along with the deployment of Industry 4.0 technologies increases the attack surface of ICS environments, which in turn makes them more vulnerable to advanced cyber threats. Therefore, many researchers have shown interest in the field of cybersecurity of ICS. The topics of intrusion detection, anomaly detection, threat intelligence, attack simulation and resilience assessment of ICS have received much attention. Nevertheless, the development and testing of cybersecurity solutions for ICS remains to be challenging due to the lack of appropriate datasets and experimental environment. The main objective of this paper is to provide the roadmap of existing ICS cybersecurity datasets, testbeds and digital twins. This paper presents various taxonomies along with systematic analysis of architecture, characteristics, capabilities, pros and cons of these tools. The results of the analysis demonstrate the presence of persistent problems such as lack of standardized benchmarking datasets, lack of modern attack scenarios, insufficient number of datasets based on real operational traffic and difficulty in validating artificial intelligence-driven cybersecurity solutions. In addition to summarizing current research on ICS cybersecurity datasets and testbeds, this roadmap provides the identification of research gaps and recommendations on creation of new tools.

---


### 343. [DOBI: Dynamic Opportunistic Body Input via Spare Joint Recruitment for Hands-Free XR](https://arxiv.org/abs/2608.30341)

**<font color=#1a73e8>作者：</font>** Rachel Kim, Xun Qian, Sang Ho Yoon  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extended Reality (XR) systems are often most useful when users are engaged in ongoing physical tasks, yet current interaction techniques still largely assume the hands are available. We present opportunistic body input, an interaction paradigm that redirects continuous XR control to whichever available body region remains free in the moment. To investigate how users naturally coordinate these spare-body movements, we conducted an elicitation study across six hand-busy scenarios. We found that while users' preferred spare body regions shift dynamically based on physical constraints, the resulting spontaneous movements share a consistent, low-dimensional kinematic structure organized around a dominant principal axis. Building on these findings, we present DOBI (Dynamic Opportunistic Body Input), a real-time XR technique that uses gaze to target a UI element, a brief trigger gesture to identify the recruited spare body region, and the region's subsequent motion to drive continuous 1D control. A 1D Fitts' law study establishes the baseline motor performance of this paradigm across four distinct body regions, achieving throughputs up to 2.62 bits/s with an overall 5.0% error rate, and a dual-task usability study shows that DOBI supports reliable, low-effort control (SUS = 84.2) while users remain engaged in realistic hand-busy activities.

---


### 344. [Proximity3D: Shape from Capacitive Proximity on Sensing Manifold](https://arxiv.org/abs/2608.30344)

**<font color=#1a73e8>作者：</font>** Hao Chen, Chenming Wu, Chun Ping Lam 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most shape reconstruction methods assume measurements defined over planar sensing domains, such as RGB images or depth maps. In this paper, we use a curved capacitive textile as a shape sensor, treating its surface as a non-planar sensing manifold. Each scan is represented as a capacitive proximity field on this manifold, induced by the interaction between the curved electrode layout and nearby object geometry. We introduce a multi-view feedforward reconstruction model that aggregates these fields across known sensor views and recovers the observed object shape. Simulated and physical experiments demonstrate robust reconstruction from capacitive proximity signals acquired on curved sensing surfaces, pointing toward a new route to robotic near-field geometric awareness via embodied sensing.

---


### 345. [Seeing the Unseen: Camouflaged Object Detection Beyond the Visible Spectrum](https://arxiv.org/abs/2608.30355)

**<font color=#1a73e8>作者：</font>** Avi Gupta, Trasha Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in camouflaged object detection (COD) have led to substantial progress in challenging low-visibility scenarios, with pioneering studies demonstrating notable success in localizing objects in camouflaged scenes. Despite these achievements, existing approaches predominantly rely on conventional three-channel RGB imagery, thereby constraining the available visual information to a limited spectral range. Multispectral images offer a wide range of information about a scene by capturing fine-grained spectral signatures. Hence, by leveraging multispectral images for COD, we introduce a novel approach to detect camouflaged objects from the corresponding multispectral inputs. In particular, we propose an end-to-end framework, \textbf{\textit{MSFormer}}, that takes a multispectral camouflaged image as input and predicts a binary mask for it. Additionally, we also provide empirical justification for integrating multispectral bands for this complex low-vision task. Our extensive experiments demonstrate the effectiveness of our method, which outperforms existing methods.

---


### 346. [Beyond Churn: Predicting Financial Fragmentation in Retail Banking with Temporal Machine Learning](https://arxiv.org/abs/2608.30364)

**<font color=#1a73e8>作者：</font>** Ananyaa Chopra, Brandon Xu, Brendan Yuen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retail banking attrition is usually represented as a terminal binary event, even though client relationships often weaken earlier through partial movements of deposits, investments, and recurring activity to external financial institutions. This paper defines that preceding state as financial fragmentation and presents an end-to-end temporal machine-learning system for predicting it before complete disengagement. Using anonymized multi-source data from a large retail bank, the framework predicts whether a valid external transfer or investment event will occur within 90 days. The study uses 595,220 client-month observations, with 346 engineered features combining monthly client profiles, balances, product relationships, prior flow-of-funds behavior, macroeconomic conditions, and competitor activity. A four-stage XGBoost cascade estimates (1) whether an external outflow will occur within 90 days, (2) the expected amount, (3) the originating product, and (4) the destination financial institution. The primary classifier achieved a test precision-recall area under the curve of 0.823. At the validation-selected threshold, it produced 86.4% precision, 75.1% recall, and an F1 score of 0.803. Ranking test observations in descending Stage 1 fragmentation score, the top 1% of clients yielded 95.3% precision, while the top 5% captured 78.7% of observed outflow cases. The amount model placed 94.9% of predictions within an adjacent amount bucket. Destination prediction reached a macro-F1 of 0.81 across 27 classes; source-product prediction achieved a weighted F1 of 0.92. By moving the analytical focus from terminal churn to earlier fund migration, the proposed approach provides a practical foundation for proactive, explainable, and economically informed client-retention decision support.

---


### 347. [Mode Connectivity Beyond Classifiers: Evidence from Generative and Contrastive Models](https://arxiv.org/abs/2608.30366)

**<font color=#1a73e8>作者：</font>** Chengzheyi Yao, Yongzhao Zhang, Yongding Tian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The loss landscape of Deep Neural Networks (DNNs) exhibits highly complex and non-convex properties. Recent studies have revealed the phenomenon of mode connectivity, demonstrating that independently trained network modes can be connected via a continuous low-loss path. However, existing mode connectivity research is predominantly confined to classifier-based models, leaving it an open question whether similar geometric properties exist in modern complex models. In this paper, we extend the boundaries of mode connectivity to generative and contrastive domains (specifically DDPM and NanoCLIP). Addressing the unique architecture of DDPM and CLIP, we propose an architecture-aware connection building algorithm. Extensive empirical results demonstrate for the first time that we successfully discover mode connectivity between independently trained DDPM and NanoCLIP modes. Our work provides a novel perspective for understanding the geometric properties of the loss landscapes in modern generative and contrastive models.

---


### 348. [Beat-Synchronous Tokenization for ECG Transformers](https://arxiv.org/abs/2608.30367)

**<font color=#1a73e8>作者：</font>** Ahmed Sameh, Nolan Wilson, Max Enderlein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based electrocardiogram (ECG) models commonly tokenize waveforms into fixed temporal patches. Though convenient, fixed patching can split heartbeat structures across token boundaries. We study beat-synchronous tokenization as a physiologically grounded alternative, comparing fixed patches with three beat-aligned strategies: resampled beats, adaptive pooled beats, and resampled beats augmented with R--R interval information. Experiments span two settings: 10-second 12-lead diagnostic classification on PTB-XL after MIMIC-IV-ECG masked pretraining, and 60-second single-lead rhythm classification on Icentia11k after patient-level contrastive pretraining. On PTB-XL, resampled beat tokens achieve the highest mean macro Area Under the ROC Curve (AUROC; 0.8945) and nearly match the best fixed-patch macro Area Under the Precision-Recall Curve (AUPRC; 0.7414), reducing average sequence length from 100 to 11.2 tokens. On Icentia11k, beat-synchronous tokenizers obtain comparable AUPRC to fixed patching with better stability across runs. These results suggest morphology-preserving beat tokenization is a compact, competitive alternative to fixed temporal patching.

---


### 349. [MCSeg: Pre-training and Fine-tuning Volumetric Pyramid Transformer for Multi-modal Cardiac Image Segmentation](https://arxiv.org/abs/2608.30371)

**<font color=#1a73e8>作者：</font>** Zhiyu Ye, Hairong Zheng, Tong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic cardiac image segmentation is pivotal for diagnosing and treating cardiac diseases. In this work, we introduce MCSeg, a volumetric transformer-based network tailored for multi-modal cardiac segmentation. To overcome the architectural mismatch inherent in existing hybrid networks, we propose a novel Scaling Feature Pyramid (SFP). Unlike conventional skip connections, the SFP effectively bridges the single-scale 3D Vision Transformer (ViT) encoder and the multi-scale CNN decoder by transforming the ViT's output into a hierarchical feature pyramid, ensuring that global contextual information is effectively leveraged. For the training paradigm, the ViT encoder first undergoes self-supervised pre-training via masked image modeling. Subsequently, the network is fine-tuned on downstream tasks, during which a regional mutual information (RMI) loss is integrated to improve boundary segmentation accuracy. In experiments, MCSeg consistently outperforms eleven SOTA methods on CT dataset ImageCHD, multi-modal dataset MM-WHS, MRI dataset HVSMR-2.0 and MSD Heart, highlighting the effectiveness of our MCSeg for multi-modal cardiac segmentation tasks. Furthermore, MCSeg's superior performance in few-shot experiment showcases its significant potential in adapting to limited data scenarios. Codes and pre-trained ViT-B weights are open-sourced at this https URL

---


### 350. [Kathleen Remembers: Length-Invariant One-Shot Recall Without Attention](https://arxiv.org/abs/2608.30376)

**<font color=#1a73e8>作者：</font>** George Fountzoulas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recurrent, attention-free sequence models share a structural weakness: a fading state cannot perform exact recall of something seen once, far in the past. We add to the Kathleen trunk a second memory layer -- a "notebook": a fixed-key holographic (HRR) associative store with a learned local write gate, a self-gating raw read, and write-triggered forgetting -- 25K parameters that attach to the logits of any trunk. (1) Mechanism: on a controlled needle-in-haystack task the notebook reaches 80-82% one-shot recall at 4x the training length, where the bare trunk scores ~4% and a parameter-matched attention head scores 100% inside its training length and 0% beyond it. Addressing is length-invariant by construction; the untrained memory alone recalls at 90% accuracy identically at 512, 2048 and 4096 bytes. Because the store is a linear superposition, two capabilities follow from arithmetic alone: selective unlearning (one subtraction erases one fact to chance, retained facts unharmed) and per-token attribution (counterfactual erasure names the source fact of every correct byte, 100% provenance). (2) Real text: on WikiText-2 bytes the notebook improves prediction of repeated rare words by +0.15-0.27 bits/byte, the gain growing with the distance between mentions and holding zero-shot at 4x training length; write-triggered forgetting eliminates memory pollution at 8x length (first-mention cost +0.33 -> -0.004). (3) Scope and scale: a parameter-matched attention head does generalize on natural-text repetition, so the notebook's claim is exact recall at O(L); on a WikiText-103 ladder (8 to 512 MB) the zero-shot repeat gain rises monotonically. All experiments are pre-registered, seeds reported, and reproducible on a single free-tier GPU.

---


> [!TIP]
> 当前位于：**301-350**（第 7/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
