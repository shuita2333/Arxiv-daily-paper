# 📦 其他研究 | 2026年09月10日

> 本类共 **542** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

---

### 301. [Temporal-Causal Inference for Reinforcement Learning via Automata Learning](https://arxiv.org/abs/2609.07461)

**<font color=#1a73e8>作者：</font>** Jan Corazza, Daniil Kaminskyi, Simon Lutz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider reinforcement learning in environments with dynamics that undergo an irreversible phase transition governed by a hidden temporal pattern. The agent observes the base state but cannot observe the phase directly. We formalize this problem as a two-phase non-Markovian decision process and introduce Temporal-Causal Inference for Reinforcement Learning (TCIRL), a framework that jointly learns a control policy and infers the hidden temporal cause of the phase transition. TCIRL maintains a hypothesis deterministic finite automaton (DFA) to track what phase is active and refines it via counterexample-driven SAT-based synthesis. We prove that the hypothesis converges almost surely to a DFA recognizing the true cause language on all attainable label sequences, yielding an optimal policy for the original non-Markovian decision process. Experiments on a genetic therapy gridworld and a traffic signal environment show that TCIRL recovers the correct cause DFA and matches the full-information baseline in both domains.

---


### 302. [When Superpixels Fail on Documents: A Study of Segmentation for LIME Explanations](https://arxiv.org/abs/2609.07462)

**<font color=#1a73e8>作者：</font>** Quentin Telnoff, Emanuela Boros, Mickaël Coustaty 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-hoc explanation methods are widely used to inspect image classifiers, but their reliability depends on design choices that are often treated as implementation details. We study this issue for LIME on document image classification, focusing on the segmentation step that defines the interpretable units being perturbed. Standard image-based LIME typically relies on natural-image superpixels, which are poorly aligned with document structure such as text regions, layout blocks, and identification codes. Using RVL-CDIP, we compare Quickshift and SLIC with document-aware segmentations based on OCR bounding boxes and regular grids. Our results show that segmentation strongly affects explanation consistency, correctness, and local fidelity. Document-aware segmentations produce more stable and faithful explanations, require fewer perturbations to converge, and expose shortcut behaviour based on document identification codes, a known RVL-CDIP bias that superpixel-based LIME often obscures. These findings show that reliable post-hoc explanation requires domain-aware interpretable representations, and that segmentation should be treated as part of the explanation method rather than as neutral preprocessing.

---


### 303. [Modus Tollens and Counterfactuals and Counterfactual Reasoning Based on Three Types of Negation](https://arxiv.org/abs/2609.07483)

**<font color=#1a73e8>作者：</font>** Zhenghua Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modus Tollens (MT) is a classical logical inference rule, while counterfactuals are hypothetical statements that are contrary to facts, and counterfactual reasoning is a process of reasoning based on counterfactuals. Negation is an indispensable core concept in them. In this paper, based on the logical systems LCOI&PLCOI with contradictory negation, opposite negation and intermediary negation, we propose three variants of Modus Tollens corresponding to distinct negation types, namely MTC: Modus Tollens based on contradictory negation, MTO: Modus Tollens based on opposite negation, and MTI: Modus Tollens based on intermediary negation. We define the implications within MTC, MTO and MTI, provide the truth value algorithms of MTC, MTO and MTI, and discuss the reducibility of these algorithms. To incorporate these three types of negation into counterfactuals and counterfactual reasoning, we differentiate counterfactuals into two types based on whether they possess logical negation, thereby proposing three counterfactuals and counterfactuals reasoning based on different logical negations. In this paper, we further argue that the three counterfactuals reasoning based on different logical negations have the same inference form as MTC, MTO and MTI, respectively. In other words, they share the same inference structure. As a result, the truth value algorithms for MTC, MTO and MTI can be as the truth value algorithms for the three counterfactuals reasoning based on different logical negations. The algorithms indicates that if the first premise of the reasoning is true, the truth values of the reasoning conclusions are identical to the truth values of the three negative premises in the reasoning premises, respectively. This reflects the consistency and accuracy of the truth value algorithms.

---


### 304. [Improving Multivariate Time Series Classification with Class-Wise Training and Model Aggregation](https://arxiv.org/abs/2609.07493)

**<font color=#1a73e8>作者：</font>** Mouhamadou Mansour Lo, Gildas Morvan, Mathieu Rossi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a class-wise dimension (channel) selection framework for Multivariate Time Series Classification (MTSC). Rather than applying a single global dimension selection process, the proposed approach independently identifies informative dimensions for each class. A dedicated learning process is subsequently performed for each class, followed by a fusion stage for final prediction. The objective is to improve the generation of discriminative feature representations while reducing the influence of noisy or non-informative dimensions. The proposed framework is evaluated using MiniRocket, a random kernel-based baseline method. Experimental results indicate that class-wise dimension selection improves the quality of extracted representations and can enhance classification performance, particularly in high-dimensional settings. These findings suggest that incorporating class-specific information into the training process represents a promising direction for MTSC, improving robustness through consistent gains across heterogeneous datasets, and interpretability through the explicit identification of class-relevant dimensions.

---


### 305. [Mitigating Shortcut Learning: Texture-Penalized Prototype Networks](https://arxiv.org/abs/2609.07504)

**<font color=#1a73e8>作者：</font>** Akshay Anilkumar Girija, Elena Hoemann, Frank Köster 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard Convolutional Neural Networks (CNNs) exhibit severe performance degradation due to a strong inductive texture bias that prioritizes local, high-frequency patterns over global structural shapes. This dependency causes confident misclassifications during textural changes or environmental effects. To address this flaw, this study introduces the Texture-Penalized Prototype Network (TPPN), a novel architectural framework that shifts this inherent bias without depending on resource-intensive augmented datasets. Specifically, a Texture-Penalization Branch (TPB) imposes a penalty to suppress the extraction of local texture proxies, forcing the network backbone to discard high-frequency cues and extract purified, shape-biased representations. By evaluating similarities within a prototype-based hypersphere derived from the final convolutional features, the approach enforces strict geometric constraints, treating objects as compositions of essential parts to achieve robust classification. Evaluations on texture-shape cue-conflict datasets and synthetic noise benchmarks demonstrate the stronger shape bias of this structural disentanglement. The proposed framework reduces the inherent texture bias of a baseline ResNet-50 from 55.11% to 29.73%, surpassing the texture-suppression capabilities of an off-the-shelf Vision Transformer (ViT-B/16). Furthermore, the approach demonstrates robust generalization under cue-conflict conditions, resisting textural shortcut learning when encountering Out-of-Distribution (OOD) shapes. The model maintains stronger shape accuracy against elevated perturbations. On clean validation data, the architecture incurs a minimal drop in accuracy of 0.90 percentage points. This provides a structural, efficient solution to CNN texture bias.

---


### 306. [Statistical versus machine learning-based spatial interpolation of post-processed ensemble weather forecasts](https://arxiv.org/abs/2609.07512)

**<font color=#1a73e8>作者：</font>** Mária Lakatos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Statistical post-processing improves ensemble weather forecasts, but generating calibrated predictions at locations without observations remains challenging. This study compares statistical and machine-learning-based methods for post-processing ECMWF 2-m temperature and 10-m wind speed forecasts at observed and unobserved stations in Germany. We consider EMOS-based approaches, distributional regression networks, Transformers, and graph neural networks under both limited and extended predictor settings. For temperature, we also investigate linear forecast combinations and propose an altitude-aware linear pool (ALP). The results show that post-processing improves upon the raw ensemble in most settings, but no single method performs best across all variables, station groups, and evaluation metrics. The proposed ALP provides a small but significant improvement over the standard linear pool at unobserved locations.

---


### 307. [PICANet: Physics-Informed Cascaded Asymmetric Network for Infrared Small Target Detection](https://arxiv.org/abs/2609.07515)

**<font color=#1a73e8>作者：</font>** Jingjing Liu, Yinchao Han, Xianchao Xiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection (ISTD) is an important research direction in image processing. However, existing methods are limited by severe background noise propagation and target degradation in high-level semantic features. To address these limitations, this paper proposes a plug-and-play physics-informed cascaded asymmetric network, named PICANet. Specifically, we construct a hierarchical prior decoupling module to explicitly extract low-level and high-level physical information, thereby characterizing target features at different levels rather than relying solely on convolutional extraction. Furthermore, a dual-prior interactive fusion module is developed to dynamically refine target representations while suppressing complex background clutter. Unlike previous work, a multi-level cross-feature attention module with the cascaded asymmetric mechanism is introduced to achieve precise alignment between high-level semantics and low-level spatial details. Extensive experiments demonstrate that the proposed PICANet outperforms state-of-the-art ISTD methods, showing satisfactory detection accuracy even against complex backgrounds. Our code is available at this https URL.

---


### 308. [Topologically Consistent Agricultural Parcel Vectorization with Semantic-Guided Diffusion and Topology-Aware Polygonization](https://arxiv.org/abs/2609.07520)

**<font color=#1a73e8>作者：</font>** Weiqin Jiao, Xiaolong Zuo, Claudio Persello  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agricultural parcel polygons play a fundamental role in geospatial applications such as precision agriculture, land administration, and crop monitoring. Beyond regular polygon geometry and low vertex redundancy, practical parcel maps should avoid topological conflicts and preserve common boundaries between adjacent fields. Yet this requirement remains largely unresolved: segmentation-based methods mainly produce parcel masks or raster boundary cues and rely on heuristic raster-to-vector conversion, instance- and contour-based methods reconstruct parcels independently, and recent vector-oriented methods improve polygon regularity but do not explicitly recover adjacent parcels from a shared topological structure. To address this gap, we propose a semantic-guided diffusion framework for topologically consistent agricultural parcel vectorization. It couples joint edge--vertex latent diffusion with supervised multi-cue conditioning to generate geometrically regularised parcel-boundary and vertex primitives while suppressing false-positive responses. A topology-aware parcel polygon reconstruction method then converts these primitives into regular polygons by reconstructing parcel faces from a common planar graph, enabling adjacent predicted parcels to reuse shared boundaries and avoid mutual interior intrusion. Extensive experiments on the AI4SmallFarms and iFLYTEK datasets evaluate parcel vectorization in terms of pixel-level coverage, geometric fidelity, object-level correctness, and topological consistency. The results show strong and competitive performance, with zero measured intrusion ratio and the highest shared-edge recall, demonstrating the potential of the proposed framework for accurate, regular, and topologically consistent agricultural parcel vectorization.

---


### 309. [When Semantically Consistent Encoding Meets View-Label Heterogeneity Modeling: A Unified Framework for Incomplete Multi-View Multi-Label Learning](https://arxiv.org/abs/2609.07525)

**<font color=#1a73e8>作者：</font>** Chengliang Liu, Bo Li, Bob Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incomplete multi-view multi-label learning requires not only robust semantic aggregation from partially observed views, but also label-aware exploitation of view-specific evidence. Existing approaches usually emphasize either shared representation learning or decision-level fusion. The former improves robustness against missing views, yet tends to compress label-discriminative view-specific cues into a single latent representation. The latter preserves individual view predictions, but often relies on fixed or globally learned fusion weights, ignoring that different labels of different instances may require different views. To address these limitations, this paper presents V2L, a unified representation-decision framework for incomplete multi-view multi-label classification. On the representation side, V2L constructs semantically consistent variational posteriors from incomplete views through a perturbation-aware encoding mechanism, which provides a stable shared semantic basis. On the decision side, V2L introduces an active view-label relevance modeling strategy that estimates instance-wise and label-wise view contributions, allowing each label prediction to adaptively select useful view-specific evidence. From the perspective of model architecture, these two important strategies are integrated into a unified framework through a hybrid fusion architecture, simultaneously meeting the requirements of cross-view semantic consistency and representational complementarity. Extensive experiments under both incomplete and complete settings show that V2L achieves leading performance on five benchmarks. Code is available at: this https URL.

---


### 310. [Quantile-Led Feature Extraction for Multi-Horizon Predictive Maintenance in Industrial Manufacturing Systems](https://arxiv.org/abs/2609.07533)

**<font color=#1a73e8>作者：</font>** David J Poland, Daniele Ravi, Na Helian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In data-driven predictive maintenance (PdM), feature extraction is usually treated as fixed preprocessing: a descriptor set is chosen once and reused while the downstream model or forecasting horizon changes. This paper isolates the representation-learning stage and presents a quantile-led feature-extraction framework based on a dual-stage MLP-QRNN hierarchy. QRNN1 learns a broad ten-quantile conditional distribution for each sensor channel, while skip-connected QRNN2 refines a retained mid-tail quantile set into compact, channel-resolved, distribution-aware features. A fixed thirteen-pipeline ablation spans 1-hour, 70-hour, and 30-day regimes across 72 machines in 9 industrial facilities, with the downstream temporal classifier held fixed within each regime. Increasing the retained mid-tail set from two to four quantiles improves 30- and 60-minute F1-score, reaching 75.92% and 72.44% with attention enabled. The results also show that representations do not transfer reliably beyond their design horizon unless feature capacity, temporal embedding, activation strategy, and sensor breadth are scaled with the forecasting task. The unmodified short-horizon extractor falls to 42.90% F1 at 70 hours, whereas horizon-conditioned extractors reach 60.38% at 70 hours and 79.97% at 30 days. The framework therefore supports treating PdM feature extraction as a horizon-dependent representational stage rather than fixed preprocessing.

---


### 311. [TeMo: Temperature Modulation for Multimodal Contrastive Learning](https://arxiv.org/abs/2609.07540)

**<font color=#1a73e8>作者：</font>** Dhimitrios Duka, Bernt Schiele, Hilde Kuehne 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive learning approaches achieve strong performance by training models to bring similar samples closer while pushing dissimilar samples apart. A crucial component of contrastive learning is the temperature hyperparameter $\tau$, which controls the penalty strength applied to negative samples. However, most existing methods either fix this hyperparameter or learn a global value during training. In this paper, we introduce TeMo, Temperature Modulation framework, a similarity-based modulation approach that adaptively adjusts the temperature for each positive-negative pair according to their similarity, enabling more fine-grained multimodal contrastive learning. Our approach seamlessly integrates temperature-modulated multimodal and unimodal losses with the standard multimodal contrastive loss by gradually transitioning between them. This design allows the model to capture both coarse- and fine-grained semantics at different training stages. Extensive experiments demonstrate that each component of TeMo consistently enhances performance across diverse zero-shot retrieval and classification tasks, establishing new state-of-the-art results.

---


### 312. [Re-engineering SORT-based algorithms for low-cost small object tracking from omnidirectional footage](https://arxiv.org/abs/2609.07547)

**<font color=#1a73e8>作者：</font>** Xin Shu, Meegan Gower, Yvonne Buckley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking (MOT) has advanced rapidly in urban surveillance and autonomous driving, yet many trackers rely on ReID- and transformer-based appearance encoders and are designed for standard FoV cameras. These assumptions break down for low-cost omnidirectional deployments, where equirectangular projection introduces seam discontinuities and targets appear to be small and fast-moving. We address multi-object tracking of flying animals captured in remote environments using omnidirectional cameras. We propose a lightweight framework that re-engineers SORT-based tracking for this geometry, including (i) a Seam-Aware Motion Model that keeps the Kalman state continuous across the seam, (ii) a composite seam-aware association cost that pairs a wrapped Euclidean term with GIoU, and (iii) OmniSmall, a new benchmark of omnidirectional wildlife footage. On our new dataset, with ground-truth detections, our modifications improved over OCSORT by +8.51 HOTA, +9.41 MOTA, and +10.17 IDF1; with YOLOX detections the gain narrows to +1.95 HOTA. Our proposed methods improved tracking performance on OmniSmall and remained competitive on JRDB without adding appearance encoders while keeping the tracking stage CPU-only. Our dataset and source code are available at: this https URL.

---


### 313. [Heat Kernel Textures: the Geodesic Gaussians That Do Not Splat](https://arxiv.org/abs/2609.07557)

**<font color=#1a73e8>作者：</font>** Simone Foti, Caner Korkmaz, Stefanos Zafeiriou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting has recently revolutionised novel view synthesis as well as many other 3D vision methods and applications. Drawing inspiration from this representation, we now rethink textures to overcome the main issues of UV mapping while considerably lowering their memory footprint. Heat Kernel Textures (HKTex) eliminate UV unwrapping as well as their persistent issues of wasted UV space, seams, distortions, vertex-duplication, and varying resolution. Grounded in discrete Riemannian geometry and intrinsically defined on any manifold surface discretised as a triangular mesh, HKTex uses anisotropic heat kernels as geodesic equivalents to Gaussians. Like our kernels, also the optimisation of their position and the adaptive densification strategies were redefined to operate on the surface of the object to be textureised. Our novel representation is also fully integrated with a physically based renderer and can be optimised either from existing textures or multi-view images. Our project page and code are available at this http URL.

---


### 314. [Scoring Without the Engine: Validating a Deterministic, Manipulation-Resistant Content Score for Generative Engines, End to End](https://arxiv.org/abs/2609.07559)

**<font color=#1a73e8>作者：</font>** Elisha Bajemon, Andre-Louis Rochet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How do you validate a cheap, deterministic proxy for an oracle that is expensive, rate-limited, and non-stationary? We present a protocol built on adversarial falsification gates (negative control, dose response, bounded amplification, duplication penalty, length neutrality) that define and select the proxy, fitted on a training split and confirmed held-out; around them it bounds what the proxy can never resolve, and re-measures external causal evidence on the current oracle rather than assuming it. We demonstrate it end to end on Generative Engine Optimization, where the proxy is a deterministic content score, and one step fails on that domain exactly as the protocol is built to detect: re-measuring the only published causal anchors (2023 effect sizes) on ten modern engine families shows their levers move citation on none, so the anchors are an expired external check; recalibrating to the near-zero modern vector strips the score of its lever-responsive components. What survives is the gate-enforced response surface. The gates buy a measured property: on a 500-source benchmark of adversarial edits, amplifying the score's calibrated levers gains an attacker at most 6 points, and decreases with dose; single-lever amplification is provably bounded, while the cap and cross-lever sub-additivity are empirical findings consistent with it. On detection, web-spam baselines dominate and out-of-distribution attacks evade the score, so the deployable filter layers it over them. A query-conditioned skyline bounds the score's citation signal (within-query Spearman 0.11), repositioning query-agnostic scores as quality filters rather than citation predictors. A query-leakage bug in our first ranking evaluation and a failed confidence flag are disclosed and corrected; every number reproduces offline from released artifacts at zero marginal API cost.

---


### 315. [From Human Factors to Human-Technology Factors: An HCI Perspective on Technology in Avalanche Safety](https://arxiv.org/abs/2609.07560)

**<font color=#1a73e8>作者：</font>** Björn Hartmann, Jason Smith  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The avalanche safety literature has identified human factors that contribute to accidents, yet researchers note a persistent gap between these insights and effective product design. Meanwhile, interactive technologies are shaping backcountry decision making with or without grounding in theory and research. We broaden the discussion of human factors into ``human-technology factors," examining how technology can both support and undermine judgment in avalanche terrain, from a human-computer interaction (HCI) perspective. We summarize relevant HCI concepts along four dimensions - attention, cognition, trust, and social interaction - and use them to revisit McCammon's FACETS framework, cataloging ways in which specific technologies may mitigate or exacerbate classic heuristic traps, grounded in accident reports and literature where possible. We identify recurring patterns, including technologies with dual-sided effects and a pervasive ``digital expert halo."

---


### 316. [No-Regret Mixing of LRU and LFU with Optimal Switching Cost](https://arxiv.org/abs/2609.07566)

**<font color=#1a73e8>作者：</font>** Younes Ben Mazziane, Xinying Zou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Caching systems often rely on simple eviction policies such as Least Recently Used (LRU) and Least Frequently Used (LFU), which perform well in complementary request regimes. Recent policies such as LeCar and Cacheus combine LRU and LFU using ideas from the experts problem in online learning. Specifically, upon a miss, they randomize between the two eviction rules using probabilities derived from scores updated by tracking the history of past evictions. While these policies exhibit strong empirical performance, it remains unclear whether they are guaranteed, on every request sequence, to perform asymptotically as well as the better of LRU and LFU, i.e., whether they achieve sublinear regret with respect to this benchmark. We first show that LeCar suffers linear regret against an oblivious adversary, even with unbounded history. We then propose H-MC, a Hedge-based mixture of virtual LRU and LFU caches that preserves Hedge's selection probabilities, and hence its regret guarantees, while minimizing the switching cost among all joint selection rules with these marginals.

---


### 317. [SphereSOD: Geometry-Structure Coupled Learning for 360 Salient Object Detection](https://arxiv.org/abs/2609.07571)

**<font color=#1a73e8>作者：</font>** Junsong Zhang, Zhijie Shen, Shuai Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 360° salient object detection (SOD) aims to accurately segment salient regions across a full field of view. However, equirectangular projection (ERP) introduces severe spatial distortion when mapping the spherical domain onto a planar representation. Existing methods mainly focus on compensating projection distortion while overlooking the interaction between panoramic geometry and salient object structure during feature perception and prediction refinement. To this end, we propose SphereSOD, an ERP-native framework that couples panoramic geometry with evolving salient structures. Specifically, spherical geometry governs feature sampling and spatial weighting, while coarse-grained saliency and contour prediction influence context aggregation during the progressive decoding process. SphereSOD first initializes deformable sampling based on spherical projection geometry and then employs bounded, content-adaptive offsets, yielding features that are better aligned with the underlying panoramic geometry. Subsequently, the decoder performs structure-guided context aggregation and progressive refinement to recover complete salient regions and accurate boundaries. Extensive experiments on three public 360° SOD benchmarks demonstrate state-of-the-art performance and a favorable accuracy-efficiency trade-off, supporting structurepreserving inference directly in ERP space as a promising alternative to projection-heavy panoramic pipelines.

---


### 318. [Efficient Exploration Is Enough](https://arxiv.org/abs/2609.07575)

**<font color=#1a73e8>作者：</font>** Mikel Malagón, Jon Vadillo, Josu Ceberio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work introduces an alternative view of efficient exploration and studies its theoretical and empirical implications in the absence of extrinsic rewards. Specifically, we define efficient explorers as agents that prioritize generating generalizable experience, i.e., data that supports learning models capable of predicting and adapting across the environment. This allows us to analyze efficient exploration through the lens of prediction and generalization. Theoretically, we demonstrate that optimally efficient explorers naturally schedule their trajectories to visit the most informative and learnable regions first. Empirically, we show that optimizing for these agents gives rise to an automatic curriculum of progressively more complex behaviors, even in relatively simple environments. These results indicate that pursuing this purely intrinsic objective alone is enough to drive the emergence of highly sophisticated behaviors. We believe that this new framework provides a principled mechanism by which agent-environment systems may sustain an open-ended process of increasingly complex behavior without external rewards, tasks, or objectives.

---


### 319. [Validating DBpedia Triple Sets for Natural Language Generation](https://arxiv.org/abs/2609.07589)

**<font color=#1a73e8>作者：</font>** Mark Andrade, Simon Mille, Anya Belz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a study of the quality of individual DBpedia triples from the perspective of Natural Language Generation, and propose and evaluate an approach for collecting entity-specific triple sets that filters out questionable triples while minimizing the loss of correct ones. We show in an evaluation against manually annotated data that with validation rules, it is possible to reach 98% precision in triple selection, and with improvements to a few Property definitions, it is possible to improve recall by 40% without harming precision.

---


### 320. [Solution for UCF UrbanTwin LUMPI Track: Sim-to-Real Urban LiDAR 3D Object Detection](https://arxiv.org/abs/2609.07590)

**<font color=#1a73e8>作者：</font>** Pu Luo, Cong Xu, Yumei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present our solution to the LUMPI track of the UCF UrbanTwin Sim2Real LiDAR Challenge at the 6th DriveX Workshop, ECCV 2026. The detector must be trained only on synthetic data and is evaluated on 50 held-out real LiDAR frames; a separate 50-frame synthetic submission is evaluated for point-cloud realism. Our method addresses the Sim2Real gap at three levels. First, we align synthetic scans to the 50k-point test density and build a 30k-record training pool using UT-LUMPI geometry, RangeLDM-based sampling diversification, rare-class copy-paste, and pedestrian-oriented augmentation. Second, complementary DSVT detectors and Car/Bus PointPillars specialists are trained under the same synthetic-only constraint. Third, predictions are integrated by class-aware routing, asymmetric agreement fusion, constrained residual-recall supplementation, class-coverage auditing, and selective box-size calibration. The realism branch is optimized independently with radial-density matching, weak affine calibration, and calibrated set mixing. The final submission obtains a Combined Score of 0.4692, a Detection Score of 0.1797, a Realism Score of 0.9035, and 3D mAP@0.5 of 0.1258.

---


### 321. [Large-Scale User Behavior Analysis in Multimodal AI-Assisted Manual Task Execution](https://arxiv.org/abs/2609.07594)

**<font color=#1a73e8>作者：</font>** Rafael Ferreira, Diogo Tavares, Diogo Glória-Silva 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational Task Assistants (CTAs) are multimodal dialogue systems that support users in complex real-world tasks such as cooking and DIY through voice, text, image, and video interactions. Prior user studies have focused on controlled settings, leaving limited understanding of real-world CTA usage at scale. In this work, we present a large-scale study of CTA usage based on thousands of users in-the-wild. Our large-scale real-world data analysis unveils new understandings of (i) user-CTA interaction flows, (ii) user intents, (iii) user conversational traits, and (iv) behavioral factors associated with user satisfaction. Our findings reveal key opportunities for future research in CTAs, particularly in user interaction design and task engagement, concluding with concrete design guidelines.

---


### 322. [BarkNet-Lite: A Lightweight Texture and Colour Network with the BarkBD Benchmark for Bark-Based Tree Species Recognition in Bangladesh](https://arxiv.org/abs/2609.07600)

**<font color=#1a73e8>作者：</font>** Aroshi Ali, Saad Ahmed, Md. Khalid Syfullah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tree species recognition supports forest inventory and biodiversity monitoring but still depends on scarce taxonomic expertise. Bark is visible year-round at ground level, yet bark recognition has concentrated on temperate floras and on large ImageNet-pre-trained backbones. We address both gaps. First, we release BarkBD, a bark dataset for Bangladesh: 14,258 uncropped smartphone photographs of 20 native species across four districts and three weather conditions, with a fixed stratified split. Second, we propose BarkNet-Lite, a 2.96M-parameter network trained from random initialisation, pairing a multi-scale texture pathway with a parallel colour-aware pathway. Over five seeds it reaches 96.64+-0.66%accuracyunderstrict single-image inference, within 2.3 points of nine ImageNet-pre-trained backbones fine-tuned under an identical protocol and within one seed-level standard deviation of the smallest ofthem, andtransfers to public benchmarks (95.86% on BarkVN-50, 92.85% on BarkNet 1.0). Grad-CAM, validated by faithfulness and weight-randomisation checks, confirms its decisions rest on bark structure rather than background. The exported single-precision model classifies one photograph in 15.34ms on a commodity smartphone.

---


### 323. [FinCUABuild: Can Agents Build Reliable Benchmarks for Dynamic Financial Computer Use?](https://arxiv.org/abs/2609.07603)

**<font color=#1a73e8>作者：</font>** Jingpu Yang, Fengxian Ji, Jinri Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial scenarios are diverse and complex, spanning varying data conditions, tool configurations, and workflows. Yet existing CUA, Computer-Using Agent, evaluation tasks remain largely manually constructed, limiting scalable coverage of real-world financial scenarios. Then, can agents autonomously construct diverse CUA evaluation tasks for financial scenarios? Evaluating this capability poses three key challenges: scenario coverage of construction requests, fair comparison across construction methods, and reliable assessment of generated task quality. To solve these, we introduce FinCUABuildBench, a benchmark for evaluating financial CUA task construction, featuring: (i) 576 construction requests covering 24 financial workflows and three types of runtime variation; (ii) standardized input, budget, and output specifications; and (iii) a task qualification mechanism based on execution tests and quality checks. We further introduce FinCUABuildAgent, a multi-agent system for automatically constructing dynamic financial CUA evaluation tasks. It consists of three modules that jointly construct tasks, environments, and validators. On FinCUABuildBench, under the same model backbone, existing agent-based construction methods achieve strict qualification rates of only 1.3-8.3%, while FinCUABuildAgent reaches 31.3%. Downstream evaluations further show that the constructed tasks can effectively differentiate CUA task-execution capabilities. These results demonstrate that agents can autonomously construct financial CUA tasks with meaningful evaluation value, offering a practical path toward broader evaluation coverage in financial scenarios. Code: this https URL

---


### 324. [Search-to-World: Evaluation of 3D World Delivery from User Request through Web Search](https://arxiv.org/abs/2609.07605)

**<font color=#1a73e8>作者：</font>** Zixiao Gu, Yabo Chen, Xunzhi Xiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic systems can interpret user requests, search the live web, and use external tools, but their ability to transform retrieved web content into a usable 3D world has not been systematically evaluated. No established end-to-end pipeline or benchmark exists for this capability. We introduce Search-to-World, an end-to-end evaluation task covering request understanding, web visual-content retrieval, and 3D-world delivery. We define Observed Retrieval Rate (ORR) and World Delivery Rate (WDR) to distinguish observing relevant content from successfully delivering a request-aligned, perceptually acceptable world. We also present WorldSearcher, a reuse-then-reconstruction harness that connects existing search agents to world delivery: it first retrieves reusable 3D worlds and, when none are available, reconstructs a world from video. A structured recovery controller revises temporal grounding, replaces source videos, or reformulates queries after failure. Using WorldSearcher, we benchmark representative models on Search-to-World and study supervised fine-tuning (SFT) for recovery subagents. Results show that delivery depends on the underlying agentic model, and that relevant-content observation does not ensure world delivery. Jointly training recovery agents improves delivery success and action efficiency. Search-to-World makes agentic 3D-world delivery measurable, while WorldSearcher provides a practical evaluation harness with recovery capabilities.

---


### 325. [CLUES-WEASEL: No additional clues required to choose your time series clustering algorithm](https://arxiv.org/abs/2609.07606)

**<font color=#1a73e8>作者：</font>** Johann Faouzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series data is very common in many real-world applications and in numerous domains, with increasing interest for automated information extraction using machine learning. One of these subfields is time series clustering, which consists in identifying clusters among a set of time series in an unsupervised fashion. Most time series clustering algorithms suffer from the same balancing act: they trade clustering performance for faster runtimes or vice versa. We present a novel time series clustering algorithm that we call CLUES-WEASEL, which stands for CLustering with the UnsupervisEd Second version of Word ExtrAction for time SEries cLassification. CLUES-WEASEL extracts features using the unsupervised version of the transformation step of WEASEL 2.0, which is a time series classification algorithm, then reduces these features using principal component analysis, and finally performs clustering with the $k$-means algorithm using these reduced extracted features. Through extensive experiments, we prove that CLUES-WEASEL is significantly better than any other existing time series clustering algorithm while being (much) faster than any state-of-the-art one. We also show that the architecture of CLUES-WEASEL can work well with other time series feature extraction algorithms. Our findings highlight the relevance of CLUES-WEASEL for time series clustering.

---


### 326. [Solution for UCF UrbanTwin V2X-Real Track: Sim-to-Real Urban LiDAR 3D Object Detection](https://arxiv.org/abs/2609.07608)

**<font color=#1a73e8>作者：</font>** Pu Luo, Cong Xu, Yumei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bridging the simulation-to-reality gap in roadside LiDAR requires addressing several coupled discrepancies, including scene geometry, sampling density, return patterns, and pedestrian scale. This report presents a multi-source collaborative training and class-aware fusion framework for Sim2Real 3D detection. The method organizes digital-twin scans, diffusion-redrawn scans, density-stabilized scans, and pedestrian morphology-aligned samples into a unified training pool with complementary roles. Within a common DSVT detection formulation, source-specialized expert branches preserve those roles while optimizing for the same detection objective. At inference, a predefined class-aware fusion pathway integrates geometry-stable and calibration-aware branches for vehicles, sampling-complementary branches for trucks, and morphology-consistent evidence for pedestrians. A label-free point-cloud center blend then refines geometric localization. On the UrbanTwin V2X-Real hidden test set, the unified system achieves a combined score of 0.7421, with 3D mAP@0.5 of 0.4518 and a realism score of 0.8871. The results indicate that a stable, interpretable collaboration among data sources is more valuable than unconstrained aggregation of model outputs.

---


### 327. [Translation of Black-Box Clinical Prediction Models into Standalone Transparent Nomograms: Temporal External Validation in Heart Transplantation](https://arxiv.org/abs/2609.07610)

**<font color=#1a73e8>作者：</font>** Henry Pigot, Paulo J. G. Lisboa, Sandra Ortega-Martorell 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We convert black-box clinical prediction models for tabular data into standalone nomograms that can be audited term by term. PRiSM (Partial Responses in Structured Models) takes the shape of each effect and interaction from the source model, not merely which variables mattered, and lets the outcome select and weight them. We tested this in 50,356 heart transplant recipients, with validation in a later era than training. Nomograms from all 5 source models - a public clinical risk score, logistic regression, neural networks, random forests and extreme gradient boosting - met a prespecified noninferiority criterion for discrimination before any further simplification, and generally preserved calibration and clinical net benefit. Those from the 3 machine-learning models showed no detectable difference in discrimination from de novo generalized additive and explainable boosting models, exceeded neural additive models, and carried fewer terms than the explainable boosting model. PRiSM is released as an open-source Python package.

---


### 328. [Construction and Natural Language Querying of a Cybersecurity Knowledge Graph](https://arxiv.org/abs/2609.07614)

**<font color=#1a73e8>作者：</font>** Ines Ben Brahim, Mohamed-Amine El Mortaji, Nada Haddad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity vulnerability information is distributed across numerous platforms and databases, making it difficult for researchers and practitioners to obtain a unified and structured understanding of existing threats. This is a critical issue in cybersecurity, where timely access to accurate vulnerability information directly impacts risk assessment and decision-making. While previous work has shown that knowledge graphs are effective for organizing vulnerability data, a major research gap remains in their accessibility, as querying such graphs typically requires expertise in graph query languages like Cypher. This paper aims to address this gap by proposing an approach that combines the construction of a cybersecurity knowledge graph with natural language-based interrogation. The proposed methodology relies on data collected from the National Vulnerability Database (NVD)(1) through its REST API and models vulnerabilities, products, vendors, severity metrics, weaknesses, and references using the Labeled Property Graph paradigm in Neo4j. The knowledge graph is deployed on Neo4j Aura Cloud and queried through an AI-assisted interface that translates natural language queries into Cypher language. The key contribution of this work is demonstrating that natural language querying significantly lowers the barrier to interacting with cybersecurity knowledge graphs, enabling more intuitive exploration and analysis of vulnerability data, and thereby enhancing their practical usefulness for a broader range of users in the cybersecurity field.

---


### 329. [Forecasting the Winner of a Live Tennis Match](https://arxiv.org/abs/2609.07617)

**<font color=#1a73e8>作者：</font>** Charles Xie, Aneesh Muppidi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the rise of live sports betting in recent years, tennis forecasting has expanded from pre-match prediction to models that update win probabilities as a match unfolds. A central challenge in creating such a model is the constant need for models to adapt to score and performance changes. This study examines how pre-match and live information can be most effectively integrated into a model to produce accurate win-probability estimates. The analysis uses 8,222 Grand Slam matches containing a total of 1,505,355 points. Five models were evaluated using a chronological split, with matches from 2011-2021 used for training, 2022 for validation, and 2023-2024 for testing. Trace, a hybrid model, achieved accuracies of 76.06%, 82.15%, and 88.34% at 25%, 50%, and 75% match progress, suggesting that hybrid modeling is a practical approach to live tennis forecasting.

---


### 330. [Privacy Leakage from a Thousand Words: Millipixel Location Recovery from Dot Maps](https://arxiv.org/abs/2609.07623)

**<font color=#1a73e8>作者：</font>** Yuntao Du, Tanishq Pauskar, Hao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dot maps, which visualize individual data points as dots over a geographic region, are widely used across diverse domains to represent spatial patterns in sensitive data. However, the understanding of the privacy risks associated with dot maps remains limited, particularly for maps covering large geographic areas. In this paper, we systematically analyze these risks and present AutoLocate, an automated framework for high-precision location recovery. At its core, AutoLocate exploits anti-aliasing artifacts introduced during map rendering, which inadvertently encode sub-pixel information about dot locations. AutoLocate formulates location recovery as a black-box optimization problem, iteratively refining estimated coordinates by minimizing perceptual discrepancies over these artifacts between the target map and rendered candidate maps. Extensive experiments on both real-world and synthetic datasets, across different attack scenarios and a broad range of map configurations (e.g., map scale, background, resolution), demonstrate the effectiveness of AutoLocate. In particular, it achieves average recovery errors as low as 1 meter (approximately 0.0002 pixel precision) on small-scale maps of the United States, over 200x more accurate than existing approaches. We also propose mitigation strategies and introduce a privacy risk assessment tool to help practitioners evaluate and reduce privacy leakage when publishing dot maps.

---


### 331. [Norms at a Price: Why RL-Based Alignment Can Promise Conditional Compliance at Best](https://arxiv.org/abs/2609.07627)

**<font color=#1a73e8>作者：</font>** Kevin Baum, Rūta Binkytė, Felix Jahn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents sometimes act aligned when they infer they are being tested, and differently when not. We argue this is not an anomaly but what current training regimes are structured to select for. Reinforcement-learning-based alignment folds norms and task pursuit into one policy: the system learns its norms from scored behavior, and scoring flattens them. Do not do X is learned as doing X costs something if noticed. On every datum training can produce, a policy that complies only when it might be observed is indistinguishable from one that complies always. The experiment that would tell them apart - scoring unobserved behavior - is a contradiction in terms. Conditional compliance is thus the most that behavioral training can be known to deliver. Agency sharpens the problem: agents operate mostly where no one is watching, and can act on whether they are watched. An iterated pipeline that trains against detected failures selects for passing detection, not for complying. This account unifies alignment faking, sandbagging, and evaluation-aware scheming. And it reorients the remedy: not deeper internalization but architecture, making violations unavailable rather than unchosen.

---


### 332. [The Art of Hierarchical Competing Patterns: Gaussian Process Optimization of Hyphenation](https://arxiv.org/abs/2609.07638)

**<font color=#1a73e8>作者：</font>** Ondřej Sojka, Petr Sojka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hyphenation patterns remain a compact and widely deployed solution for word breaking in typesetting systems, text processors, and web rendering engines, but their generation still depends on manually tuned patgen program parameter profiles. We formulate patgen profile selection as a black-box hyperparameter optimization problem and evaluate Gaussian-process Bayesian optimization for this task. The search objective combines a precision-oriented F_{1/7}-score with an explicit trie size-accuracy trade-off using a normalized trie-size penalty.
We evaluate the method on 17 hyphenated word-list datasets covering 14 languages and multiple scripts. Against two strong hand-tuned profiles regenerated from the same 8/10 training split and evaluated on the same 1/10 held-out test split, the GP-optimized profiles improve F_{1/7} on 16 of 17 datasets and reduce trie size on all 17. The median optimized/baseline trie ratio is 0.407. A dataset-level sign test gives p = 1.37e-4; a separate budget-matched comparison on five representative datasets shows that systematic search is competitive and usually improves over the best hand-tuned profile under the fixed comparison objective. The results show that model-based optimization can make pattern generation more reproducible and less dependent on expert trial-and-error while keeping the accuracy-compactness trade-off explicit.

---


### 333. [Attestream: Usage-Aware Intermittent Data Distribution with Verifiable Lifecycle Provenance for Machine-Learning Data Streams](https://arxiv.org/abs/2609.07641)

**<font color=#1a73e8>作者：</font>** Kentaro Oda  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Providers of continuously produced, commercially valuable data -- sensor streams, telemetry, and other feeds sold as machine-learning training material -- cannot observe whether delivered data is actually used, while data that keeps flowing to inactive consumers enlarges the leakage surface without producing value. We present Attestream, a blockchain-based architecture for intermittently delivered dataset streams that couples continued delivery to verifiable usage reporting. Every lifecycle event -- dataset preparation, dual-signed delivery, derivative creation (e.g., a model), and derivative distribution -- is appended to an on-chain registry as a non-repudiable, mutually linked lifecycle record. The mechanism requires provable transfer, not tokenization: plain contract storage, ERC-721 tokens, and anchored off-chain receipts are interchangeable representations of the same protocol. A usage-aware gate suspends a consumer's stream when no derivative-creation record is registered within a reporting window; evaluated lazily inside the next delivery transaction, monitoring adds no dedicated transactions. A modality-pluggable fingerprinting layer binds any leaked copy to the dual-signed delivery record of the responsible consumer, instantiated for tabular/geospatial records, images, and documents. We implement the registry as a Solidity contract with EIP-712 dual signatures and evaluate it: a full lifecycle round costs 657k gas with plain records ($0.13 on rollups; ERC-721 tokenization adds ~30k gas per record), and over a 50-consumer pool leak attribution reaches 100% from 40 leaked table rows under moderate noise, survives JPEG recompression to quality 30, and tolerates paraphrase rates up to 30% for documents.

---


### 334. [Syntactic Patterns and Stylistic Functions in Narrative Prose: A Rule-Based and Machine-Learning Approach](https://arxiv.org/abs/2609.07651)

**<font color=#1a73e8>作者：</font>** Stefana Janicijevic  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a small-scale quantitative experiment that links syntactic structure to stylistic functions in narrative prose. Starting from a dependency-parsed corpus of 3,300 sentences, we derive sentence-level stylistic labels across five categories --- descriptive, introspective, causal, ideological, and neutral --- using a transparent rule-based procedure that inspects lemmas, universal part-of-speech tags, and syntactic relations. For each sentence we construct a compact representation of its syntactic profile as a sequence of linearised triples combining lemma, POS tag, and dependency relation. These patterns serve as input to standard machine-learning classifiers trained to predict sentence-level style. The best-performing model achieves a macro-F1 of 0.948 under 10-fold cross-validation. The experiment is implemented entirely in Python using open-source tools. Our goal is not to propose a fully fledged stylistic theory, but to offer a reproducible and extensible workflow for exploring how grammatical structure contributes to narrative interpretation.

---


### 335. [ZK-eSIM: A Privacy-Centric Zero-Knowledge Approach for eSIM Provisioning](https://arxiv.org/abs/2609.07654)

**<font color=#1a73e8>作者：</font>** Liza Ahmad, Quan Shi, Joshua Haworth 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> GSMA Remote SIM Provisioning (RSP) enables over-the-air delivery of eSIM profiles, but it exposes long-lived identifiers during profile ordering and download. In particular, stable device identifiers (e.g., EID), profile identifiers, and long-lived certificate material enable mobile operators and profile-delivery infrastructure to link provisioning events to the same eUICC and, when combined with account records, to the same subscriber. This undermines subscriber anonymity and enables cross-session tracking. We present ZK-eSIM, a privacy-preserving redesign that achieves subscriber anonymity and provisioning-session unlinkability while retaining accountable traceability by exception. ZK-eSIM (i) replaces direct disclosure of device identifiers with a zero-knowledge proof of device validity and eligibility; (ii) enforces session unlinkability through short-lived, one-time pseudonymous credentials and per-session identifiers to prevent cross-session tracking; and (iii) provides privacy-preserving accountable traceability through a jointly authorised escrow mechanism, so that no single entity can unilaterally deanonymise a user. We formalise a multi-entity, honest-but-curious threat model and prove subscriber anonymity and the unlinkability of provisioning sessions under standard cryptographic assumptions. We implement a Java Card applet on a test eUICC to evaluate performance on commodity hardware with a modified LPA and SM-DP+ server. Our experiments quantify end-to-end cryptographic overhead relative to conventional RSP, confirming that ZK-eSIM adds only practical overhead, closing a critical privacy gap while preserving deployability within existing GSMA roles and interfaces.

---


### 336. [Harnessing CLIP and DINO: An Uncertainty-Aware Cascaded Fusion Network for Generalizable Deepfake Image Detection](https://arxiv.org/abs/2609.07670)

**<font color=#1a73e8>作者：</font>** Xuechao Zou, Yi Zhou, Kai Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing realism and accessibility of manipulated and generated faces threaten the trustworthiness of digital media. To detect such forgeries, deepfake detectors based on vision foundation models have shown promising performance, but they typically rely on a single pretrained representation and are prone to overfitting to particular training distributions. To improve generalization to unseen forgeries, we propose UCF-Net, an uncertainty-aware cascaded fusion network that harnesses CLIP's language-aligned semantic priors and DINO's self-supervised visual-structure priors. UCF-Net extracts hierarchical features across Transformer depths, uses layer-wise expert aggregation to adaptively combine each encoder's multi-level cues, and performs weighted fusion of the resulting representations based on entropy-derived uncertainty. We further consolidate public deepfake datasets into a unified benchmark of approximately 4M images and construct a separate cross-generator evaluation set with over 8K face images from eight recent generators. On the unified benchmark, UCF-Net achieves the best mean AUC among the evaluated methods in both in-domain and cross-domain evaluations. On the cross-generator set, it adapts effectively with limited target-domain data, although zero-shot transfer remains challenging.

---


### 337. [On the Recall Scaling Laws in Mamba: A Theoretical and Mechanistic Study via Hashing](https://arxiv.org/abs/2609.07681)

**<font color=#1a73e8>作者：</font>** Yuval Koren, Assaf Ben-Kish, Raja Giryes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Associative Recall (AR) is the cognitive ability to learn and retrieve links between items in memory. In NLP, AR is used as a benchmark for evaluating the in-context memory capacity of architectures such as Mamba, and has been found to strongly correlate with language modeling performance. This paper explores AR from the perspective of mechanistic interpretability, aiming to reverse-engineer the exact internal algorithm used by Mamba to perform recall. Our key insight is that Mamba performs recall by implicitly learning linear hash functions, and we identify the low-level circuit that enables this behavior. Building on these findings and inspired by theoretical tools in similarity-preserving hashing, such as the Johnson-Lindenstrauss lemma, we develop a theoretical framework for analyzing AR, which we term Recall Scaling Laws. Given the vocabulary size and the number of facts in context, this framework allows us to (1) predict the embedding and state dimensions required for Mamba to achieve perfect recall, (2) predict recall success probability given the model dimensions, and (3) analyze multi-layer models and multi-head SSM patterns. Empirical results show that our theoretical findings are accurate and predictive, offering insights into how AR capacity scales with vocabulary, state, embedding size, and architecture.

---


### 338. [CrowdTraj: A Benchmark for Dense Crowd Trajectory Prediction in Realistic Crowded Environments](https://arxiv.org/abs/2609.07685)

**<font color=#1a73e8>作者：</font>** Antonius Bima Murti Wijaya, Paul Henderson, Marwa Mahmoud  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world applications, pedestrian trajectory prediction models rely on inputs from detection and tracking systems. Prior trajectory prediction benchmarks either contain relatively sparse pedestrian interactions, assume perfect tracking inputs, or rely on overhead viewpoints that minimize occlusion and perspective distortion, limiting evaluation in realistic dense-crowd scenarios. We present CrowdTraj, a benchmark for pedestrian trajectory prediction in natural dense crowd scenes. Unlike previous datasets, CrowdTraj supports end-to-end evaluation from detection through tracking to trajectory prediction under severe occlusion in CCTV views. It also captures diverse, natural pedestrian behaviours, including abrupt directional changes rarely observed in existing benchmarks. CrowdTraj includes five diverse scenes, with an average of 1,146 unique pedestrians per scene, maximum frame-level densities ranging from 114 to 372 pedestrians, and over 3.2 million annotated head bounding boxes. CrowdTraj provides pixel and real-world coordinates via per-scene homography matrices for physically meaningful analysis. Our experimental results show that tracking accuracy (IDF1) drops to 0.68 to 0.70 in the densest scenes, compared with approximately 0.90 in less crowded scenes. Trajectory prediction training also becomes substantially more computationally expensive in dense scenes, with training times increasing by up to 8 times. These findings show that CrowdTraj exposes limitations in current trajectory prediction pipelines that remain hidden on existing sparse-crowd benchmarks, particularly in robustness to tracking noise and computational scalability.

---


### 339. [Emergent Charging Coordination in Electric Delivery Fleets](https://arxiv.org/abs/2609.07689)

**<font color=#1a73e8>作者：</font>** Javier Vales-Alonso, Juan J. Alcaraz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In electric delivery fleets, mid-shift charging is non-trivial: each vehicle must decide when, where and how much to charge to finish on time with battery above a safety floor. The choices are coupled: queues build where too many vehicles pick the same station. Prior work resolves this coupling with central dispatching, precomputed schedules or reservations, machinery that charging infrastructure rarely supports. Instead, we use a family of learning agents under purely local control: every vehicle runs the same policy, deciding alone from its time budgets and broadcast station occupancies, leading to emergent coordination without central control or messaging. We validate this paradigm in simulation on real OpenStreetMap networks of twenty cities, each with a frozen scenario calibrated by an omniscient Oracle (99.5% of shifts completed on time), whereas a naive greedy rule (nearest station on low battery) completes just 73%. Agents trained with neuroevolution (NEAT) and policy gradients (PPO) on four cities and deployed zero-shot across all twenty, sixteen never seen in training, complete 96.8% and 98.6% of shifts, with the policy-gradient controllers proving more robust when demand or vehicle characteristics drift beyond the trained regime. In contrast, tuned threshold heuristics that read vehicle urgency alone fall short in contended cities (~80%). Through training, these learning agents rediscover partial charging and short opportunistic sessions, and route around busy stations, cutting per-session queue waits from about 45 minutes to under 2. In summary, this coordination paradigm balances local urgency against public occupancy, reaching near-Oracle performance at minimal implementation cost.

---


### 340. [SoK: Secure Software-Based Multi-Domain Data Segregation](https://arxiv.org/abs/2609.07701)

**<font color=#1a73e8>作者：</font>** Quang Cao, Peter Vinci, Nick Georghiou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern mission-critical coordination demands seamless communication across multiple domains. Traditionally, Voice Communication Systems (VCS) have relied on physically separated Red/Black architectures to ensure voice and data segregation. While these hardware-based methods provide strong security assurances and remain foundational in high-security contexts, they can introduce significant complexity and scalability challenges as mission parameters expand into highly dynamic, multi-domain integrations. As defence, emergency response, and critical infrastructure operations increasingly require interoperable, flexible, and cost-efficient communication environments, there is a growing need to understand whether software-based approaches can provide comparable assurance while supporting modern operational requirements. This SoK characterises a transition to software-based Multi-Domain Data Segregation (MDDS) by integrating systems security, networking, and cryptography. Its goal is to consolidate existing research, identify shared architectural patterns, and address the security challenges facing next-generation high-assurance software-based VCS architectures. By assessing software-defined and virtualized approaches, this SoK supports the development of scalable, high-assurance VCS architectures that facilitate secure real-time coordination across diverse operational domains. Specifically, this SoK examines the security implications of Software-Defined Networking, Network Slicing, Separation Kernels, and Cross-Domain Solutions while addressing challenges posed by quantum computing through Post-Quantum Cryptography (PQC). This SoK provides a comprehensive analysis of the shift from hardware isolation to software segregation, serving as a crucial foundation for researchers and industry stakeholders aiming to enhance secure and adaptable VCS infrastructures for mission-critical operations.

---


### 341. [Situated Action in Pre-Hospital Critical Care Dispatch: Identifying where and how Algorithmic Assistance might be useful in the daily work of specialist Emergency Medical Dispatchers](https://arxiv.org/abs/2609.07705)

**<font color=#1a73e8>作者：</font>** Ben Wilson, Matt Roach, Greg Browning 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study uses ethnographic immersion and observation as contextual inquiry to understand situated action at an Emergency Medical Dispatch critical care hub. The work is a response to the urgent need to recruit context-specific knowledge and participation into design that helps to narrow the AI Chasm - the gap between the promise of Artificial Intelligence (AI) systems and what they deliver for clinicians and their patients.
The work of a pre-hospital critical care team's dispatch process is described and analysed to reveal both the structure of the workflow and the different cognitive demands it makes on staff tasked with dispatch decision-making. Elements of attention, communication and focus between the humans, as they carry out this work, are drawn out in order to understand the work-as-done and identify the many dependencies in the process. The motivation is to establish where AI support might be useful and to discover what challenges there could be in designing appropriate algorithmic assistance. We ask whether, where and how the design and implementation of an AI system might be considered. The ultimate objective is to improve the decision process itself to the benefit of clinicians and patients.
The study identifies three key steps in the situated workflow and details how decision-makers negotiate each one as emergency calls follow complex routes between them. We find compelling evidence that the first of these decision steps constitutes the most promising candidate for unobtrusive assistance that could be safe and effective in improving both clinician workload and clinical outcomes.

---


### 342. [ParetoTransport: Generative Optimization by Mass Transport Toward The Pareto Front](https://arxiv.org/abs/2609.07706)

**<font color=#1a73e8>作者：</font>** Stephanie Holly, Sepp Hochreiter, Werner Zellinger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline multi-objective optimization requires not only moving the objective vectors of candidate designs toward the Pareto front, but also distributing them effectively along it. Generative methods have recently emerged as a natural approach because they learn a distribution over feasible designs while allowing generation to be steered toward promising designs. Existing methods, however, largely retain classical sample-wise guidance strategies, leaving the distribution-level modeling capability of generative methods underused. We propose ParetoTransport, a training-free guidance method for pre-trained flow-matching models that explicitly specifies and refines a population-level distribution in objective space. ParetoTransport guides a flow-matching sampler to iteratively transport the empirical offline distribution toward the Pareto front, with Wasserstein matching to intermediate proxy distributions. This directly controls distributional displacement and mass allocation along the front. We establish a convergence result and demonstrate state-of-the-art performance on standard offline MOO benchmarks, extending recent evaluations beyond hypervolume to generational distance, inverted generational distance, and Wasserstein distance.

---


### 343. [Crossing the Streams: SSH Plaintext Recovery via a Common Compression Context in Multiplexed Channels](https://arxiv.org/abs/2609.07709)

**<font color=#1a73e8>作者：</font>** Fabian Bäumer, Marcus Brinkmann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> SSH is the standard protocol for secure remote administration of servers. At the transport layer, SSH uses the Binary Packet Protocol (BPP) for encrypted and authenticated communication. Above this, the SSH Connection Protocol multiplexes one or more logical channels over a single connection, supporting interactive shells, port forwarding, and related functionality.
We show that SSH channel multiplexing creates a previously unrecognized compression side channel: all channels on a connection share the same compression context. When compression is enabled, an attacker can inject partially chosen plaintext into a channel and observe the length of the resulting ciphertext on the network. This enables an adaptive chosen-plaintext attack that recovers secrets from one channel by interacting with another. While related attacks such as CRIME and BREACH have been studied extensively for HTTP over TLS, this is, to our knowledge, the first compression side-channel attack on SSH and the first SSH analysis to consider a combined passive eavesdropper and web attacker threat model.
We further demonstrate the attack in three different application scenarios and evaluate its effectiveness under varying levels of protocol noise. We find that, in the lowest-noise scenario, an 8-character secret over a 26-letter alphabet can be recovered using at most 276 guesses. Finally, we analyze the SSH ecosystem for compression support and other implementation characteristics that influence the practical efficacy of the attack.

---


### 344. [The Emerging AI Paper-Review Arms Race: Adversarial Co-Evolution in Scholarly Publishing](https://arxiv.org/abs/2609.07713)

**<font color=#1a73e8>作者：</font>** Chenguang Wang, Ming Li, Adebayo Braimah 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative and agentic AI are reshaping both the production and evaluation of scientific research. These developments are often studied separately, as questions of how AI can produce research and how AI can review it. We argue that this separation misses an increasingly important feature of scholarly publishing: changes on one side alter the incentives, constraints, and behavior of the other. We synthesize 230 scholarly publications and institutional records using a taxonomy of six connected dynamics: production scaling, evaluation automation, evaluation manipulation, defense mechanisms and policy responses, evasion and side effects, and long-horizon ecosystem feedback. The literature shows an emerging progression in which cheaper and faster research production increases pressure on evaluation, AI-mediated evaluation becomes more scalable and repeatable, participants can exploit evaluator regularities, and institutions respond with technical safeguards and policy controls. These responses can in turn induce evasion, redistribute errors and workload, and shape the scholarly records reused by future research and evaluation systems. Evidence is strongest for production and evaluation at scale, reproducible manipulation, and institutional response, while post-policy adaptation and artifact-level long-horizon feedback remain less directly observed. This systems view shifts attention from isolated AI capabilities toward how scholarly actors and AI systems adapt to one another over time.

---


### 345. [A radiographic world model for clinical reasoning and evidence generation](https://arxiv.org/abs/2609.07719)

**<font color=#1a73e8>作者：</font>** Suyang Xi, Songtao Hu, Shansong Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical imaging artificial intelligence (AI) is commonly developed as separate mappings from radiographs to diagnostic outputs or from clinical descriptions to generated images, although both arise from the same underlying radiographic state. A world-model formulation instead seeks to learn an internal representation of this state that can support both clinical readout and conditional simulation of radiographic observations. Here we introduce MedDream, a radiographic world model that learns a shared continuous latent state from paired chest radiograph-text observations for diagnostic reasoning and report-conditioned evidence generation. MedDream was pretrained on 2.65 million leakage-controlled chest radiograph-text pairs curated from 4.40 million candidates. Across eight clinical datasets and two independent reader cohorts, MedDream outperformed leading diagnostic and generative comparators. For diagnostic reasoning, MedDream showed strong generalization across disease recognition, label-scarce adaptation, severity assessment, and localization, while MedDream-supported review increased mean resident concordance with independent radiologist consensus from 56.3% to 63.0%. For evidence generation, MedDream produced radiographs that preserved clinically relevant pathology and improved downstream performance on held-out real data, with synthetic augmentation increasing external VinDr-CXR macro-AUROC from 76.4% to 81.4%. More importantly, conditioning generation on prespecified subgroup performance gaps enabled targeted evidence construction, increasing weighted F1 by 3.1 percentage points in Asian patients, whereas matched-volume unguided augmentation decreased it by 2.3 points. These findings establish radiographic world models as a path toward medical AI that learns clinically meaningful internal states for interpreting, simulating, and constructing evidence for clinical use.

---


### 346. [Better Call CineCrew: Consistent Ultra-Long Narrative-to-Film Generation](https://arxiv.org/abs/2609.07720)

**<font color=#1a73e8>作者：</font>** Jiaben Chen, Sixun Dong, Qinhong Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-form narrative-to-film generation requires shot-level controllability and cross-clip consistency in both visual identity and character behavior-requirements that remain difficult to satisfy with current prompt-based workflows. A core reason existing workflows remain brittle is the lack of a structured intermediate layer between scripts and video models, especially when screenplays are underspecified at key cinematic decision points. We introduce a structured orchestration layer for film-oriented script-to-video generation, implemented as a multi-agent framework that operates between scripts and off-the-shelf video generators. The layer is centered on FilmDSL, a film-oriented domain-specific language that makes cinematic constraints explicit, including shot and camera directives, asset and continuity requirements, and persona cues, so that agents coordinate through a shared structured specification for planning, generation, critique, and repair. Specifically, a generation agent constructs asset packs and storyboard keyframes that anchor composition before clip-by-clip synthesis, while a critic agent produces structured QA signals and triggers targeted refinement without retraining the base model. Experiments on TV-style segments show improved controllability and consistency over text-only and reference-only baselines.

---


### 347. [Zero-Shot 3D Plant Organ Segmentation with SAM3 and Semantic NeRFs](https://arxiv.org/abs/2609.07724)

**<font color=#1a73e8>作者：</font>** Andreas Gilson, Laura Hennig, Peter Pietrzyk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D plant organ segmentation is fundamental to automated phenotyping. Existing approaches rely on annotated training data or species-specific model configurations. We present an annotation-free pipeline for 3D plant organ segmentation, combining text-prompted SAM3 segmentation with semantic neural radiance fields (NeRFs). Given only multi-view RGB images and a list of class names, our zero-shot pipeline produces semantically labeled 3D point clouds without manual annotation, per-species fine-tuning, or domain-specific preprocessing. Multi-view NeRF fusion acts as effective implicit consensus mechanism that lifts imperfect per-frame masks into accurate 3D labels. On a controlled Begonia maculata testbed the SAM3 pipeline achieves 92.6% mIoU, reaching 95.9% of the oracle upper bound established with perfect ground-truth masks. The pipeline was further evaluated on a new dataset spanning ten diverse plant point clouds reaching an average 0.856 mIoU, with leaf and pot IoU above 0.91 and 0.90 for every species, respectively. These results demonstrate that annotation-free 3D plant organ segmentation is now feasible and approaching the range of supervised methods.

---


### 348. [Attributing Cohen's d: Training Data Attribution for Disease-Related Effects in Normative Age Biomarkers](https://arxiv.org/abs/2609.07729)

**<font color=#1a73e8>作者：</font>** Jakob Snel, Marc-Andre Schulz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Normative age models are trained to predict chronological age in a nominally healthy cohort. Applied to patients, they deviate, and the gap between predicted and chronological age is read as disease risk. Here, we attribute the disease-related effect size of the age gap directly to individual training samples, rather than using a prediction-level loss as the attribution target. For Cohen's $d$, the resulting closed-form influence functional, validated against leave-one-out retraining, ranks training samples by their effect on held-out case-control separation. Across four diseases and two biomarker modalities in UK Biobank, removing the 10% most influential training samples raises held-out disease-related effect size in every seed. It more than doubles the metabolomic-age effect for type-2 diabetes and raises the brain-age effect for multiple sclerosis by roughly a third. Random removal leaves effect size flat even at 50% removal, confirming the gain comes from which samples are removed, not how many. Flagged subjects carry subclinical cardiometabolic burden that diagnosis-based exclusion misses, on markers the model never sees. For type-2 diabetes, where the method gains most, the marker recovered is HbA1c, the standard measure of blood sugar control. We release pyinfluence, our influence-function package, for reproducibility and reuse.

---


### 349. [TV-SGS: Gaussian Splatting with Geometric Information Propagation via Tensor Voting under sparse views](https://arxiv.org/abs/2609.07734)

**<font color=#1a73e8>作者：</font>** Harish N Sathishchandra, Philippos Mordohai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Splatting has been effective in inferring scene representations that excel in novel view synthesis. Multiple splats cooperate seamlessly to synthesize the pixels of novel views and are jointly optimized even though they only affect each other indirectly, via pixels they project to in common. We present an approach that enables direct communication among splats to enhance the geometric structures they form in 3D. This is accomplished by Tensor Voting, which was originally designed to infer structures from noisy inputs and has been adapted here to provide supervision during test-time optimization, leading to more accurate scene geometry. We introduce a new class of 3D losses that do not rely on rendering and can be combined with essentially all losses previously reported in the literature. Our 3D losses are especially effective when the input views are sparse and geometric regularization is essential due to limited supervision from the images. Our method is easy to integrate with a diverse set of backbones, and our experiments on the DTU and Tanks-and-Temples datasets demonstrate that TV-SGS improves the geometry of the outputs compared to the backbone, while maintaining or improving rendering quality.

---


### 350. [TFTrack: A Template-Free Framework for Efficient 3D Point Cloud Tracking](https://arxiv.org/abs/2609.07738)

**<font color=#1a73e8>作者：</font>** Zhaofeng Hu, Sifan Zhou, Jiahao Nie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR-based 3D Single Object Tracking (3D SOT) is critical for robotic perception and navigation and aims to localize dynamic objects across frames in sparse point clouds. Existing methods, rooted in the Siamese tracking paradigm from 2D vision, rely on costly dual-input designs and excessive motion modeling guided by template priors, hindering their efficiency. Our in-depth analysis reveals: (i) the template paradigm is redundant, as the previous bounding box center encodes sufficient historical context; (ii) complex motion modeling is unnecessary, as geometric alignment provides adequate motion priors. Based on the above findings, we propose the first Template-Free Tracking framework (TFTrack). The novel framework eliminates the need for template-search pairings and operates directly on the current frame guided solely by the prior bounding box center and size. We instantiate this paradigm into three variants: TFTrack-Voxel, TFTrack-Pillar, and TFTrack-Point, to explore different 3D representations under a unified framework, ensuring flexibility across sparse and dense scenes. Extensive experiments on KITTI and nuScenes benchmarks show that TFTrack is competitive with leading template-based trackers, while reducing FLOPs by approximately 50% and running at approximately 120 FPS. By simplifying overcomplicated motion-centric designs, TFTrack establishes a new minimalist paradigm for efficient 3D point cloud tracking, paving the way for real-time and resource-efficient deployment in embedded robotic systems, such as autonomous vehicles. The code is available at this https URL.

---


> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
