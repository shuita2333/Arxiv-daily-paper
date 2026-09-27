# 📦 其他研究 | 2026年09月28日

> 本类共 **266** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-266](./part-06.md)

---

### 201. [AI-based detection of worsening heart failure from low-resolution telemonitoring data](https://arxiv.org/abs/2609.29742)

**<font color=#1a73e8>作者：</font>** Erik Aerts, Yinan Yu, Annika Rosengren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective: Heart failure (HF) presents a healthcare challenge due to its high comorbidity burden, aging patient population and frequent hospitalizations. Remote monitoring offers a promising approach to managing HF patients by early detection of health deterioration. Developing autonomous systems to detect signs of worsening in telemonitoring data is of interest to reduce the workload of healthcare personnel. Methods: We propose the TRACER model, a Transformer with Contrastive Event Representation, designed to predict timelines leading to rare hospitalization events in low-resolution and irregularly sampled telemonitoring data. TRACER incorporates time-aware embeddings for each biomarker, contrastive pre-training to enhance anomaly detection via representation learning, and independent binary classifiers for detection. We used measurement data containing remotely recorded biomarker sequences from 276 HF patients segmented into overlapping windows based on temporal rules, and labeled the windows based on the occurrence of HF relevant hospitalizations at the latter edge of the window. Results: TRACER was able to correctly predict 66.7% timelines leading up to HF hospitalizations in the highly imbalanced real-world dataset with an overestimation of 7.9%. Reformulating the training of TRACER as an event detection problem improved the predictive performance compared with training directly on forecasting windows, enabling more effective use of the limited hospitalization events. Conclusion: TRACER demonstrated superior performance in detecting signs of worsening status in real-world telemonitoring data compared to the other tested models. Significance: TRACER shows promise in identifying signs of clinical deterioration that allow for alerts to be generated to provide counteractive treatment in patients with HF.

---


### 202. [Improving the Reliability of Anomaly Detection for Encrypted OPC UA Traffic over Private 5G](https://arxiv.org/abs/2609.29745)

**<font color=#1a73e8>作者：</font>** Song Son Ha, Florian Foerster, Henry Beuster 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open Platform Communications Unified Architecture (OPC UA) is increasingly deployed over private 5G networks in industrial environments, where end-to-end encryption prevents payload inspection by network-based intrusion detection systems (IDSs). Although payload-agnostic statistical features extracted from encrypted traffic enable traffic-based anomaly detection, benign connectivity variations may alter observable user-plane (UP) behavior and increase the false-positive rate (FPR). This paper investigates this reliability problem and proposes a control-plane (CP)-aware decision adaptation for four frozen IDS models. CP indicators at the user equipment (UE) level are used to construct a temporal CP context in which a CP-specific threshold selected on adaptation validation data is applied, while the original threshold remains active outside the context. The traffic features, attack scores, preprocessing procedure, and trained model parameters remain unchanged.
Evaluation on a real industrial private 5G testbed shows that benign connectivity variations increase the FPR for all four evaluated models and that false positives are concentrated within periods temporally associated with CP activity. The proposed CP-aware decision adaptation reduces both global FPR and FPR within the CP context while introducing a configurable trade-off between FPR reduction and retained recall over the complete attack campaign. These findings demonstrate that CP context can improve the operational reliability of encrypted-traffic intrusion detection without retraining the underlying models.

---


### 203. [WeatherDiagFlow: Evidence-Grounded Radar Nowcasting with Diagnostic Flow Refinement](https://arxiv.org/abs/2609.29772)

**<font color=#1a73e8>作者：</font>** Chunlei Shi, Yufeng Zhu, Yixiao Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Radar nowcasting is essential for short-term warning and emergency response, yet conventional systems mainly return future radar fields and provide limited support for operational communication and post-event verification. We formulate radar nowcasting as an evidence-grounded forecast--bulletin--audit task, in which a numerical forecaster produces both future radar fields and structured diagnostic evidence. Forecast-time bulletins use only model-available evidence, whereas post-event audits incorporate future radar truth only after the forecast horizon is observed. Based on this task formulation, WeatherDiagFlow predicts motion, growth and decay, heavy-echo risk, and uncertainty to condition rolling flow refinement, while frozen-scaffold residual calibration improves long-lead strong-echo preservation. A multi-agent layer converts the structured evidence into operational bulletins and independently generates verification audits without feeding textual outputs back into the forecaster. Experiments on FJRADAR demonstrate competitive overall performance and improved strong-echo event skill. WeatherDiagFlow therefore connects numerical prediction, evidence-grounded reporting, and auditable verification under a leakage-controlled protocol.

---


### 204. [An Analytical Theory of Auxiliary Learning](https://arxiv.org/abs/2609.29774)

**<font color=#1a73e8>作者：</font>** Federico Milanesio, Alessandro Ingrosso, Matteo Osella  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auxiliary learning is an optimization paradigm in which a neural network's performance on a target task is improved by jointly training it on additional tasks. However, the mechanisms behind this improvement remain poorly understood. We study this problem using a teacher-student framework and derive a closed system of differential equations describing the dynamics of online stochastic gradient descent in the large-input limit. For linear networks, we obtain a closed-form expression for the generalization error to leading order in the learning rate, quantifying how task correlations and label noise determine the benefit of auxiliary learning. For non-linear activation functions, we develop a fluctuation-dissipation analytical theory that establishes a general relation linking the main and auxiliary errors to the corresponding single-task error. Numerical experiments support the theoretical predictions and show how auxiliary tasks improve generalization by balancing the forcing dynamics towards the optimal solution with gradient noise.

---


### 205. [Mind the Gap: Mesh-Guided Repair of Broken Vessels](https://arxiv.org/abs/2609.29779)

**<font color=#1a73e8>作者：</font>** Gniewosz Drwiega, Wojciech Szymanski, Marek Wodzinski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vessel segmentation is commonly optimized as voxel-wise classification, but small local errors can strongly disrupt vascular connectivity while having little effect on overlap scores. This is particularly problematic for downstream analyses that rely on centerlines, branches, connected components, or graph structure. We propose a mesh-guided post-processing framework for repairing broken vessel segmentations produced by nnU-Net. For each predicted binary mask, a deformable template mesh is fitted to the mask surface in physical space and used as a case-specific geometric scaffold. The fitted mesh is not voxelized as the final segmentation; instead, it guides conservative reconnection of disconnected components by proposing or validating thin bridge candidates under foreground-growth constraints. We evaluated this approach in three vascular anatomies using AortaSeg24 and SEGA for the aorta, TopCoW for the Circle of Willis, and PARSE for the pulmonary arteries. Performance is measured using Dice, connected-component Dice (ccDice), and the Betti-0 number. Across these datasets, repair substantially improved connectivity while preserving overlap: Dice remained nearly unchanged, whereas ccDice increased from 0.596 to 0.992 for aorta, from 0.722 to 0.835 for TopCoW, and from 0.028 to 0.862 for PARSE. The FOMAML meta-initialization further accelerated the fitting per-case, supporting practical mesh-based repair of the vascular topology. These results suggest that explicit mesh representations can provide a useful geometric prior for correcting topological failures in otherwise accurate voxel segmentations.

---


### 206. [Lightweight Vision Transformer-Based U-Net for Brain Tumor Segmentation from MRI](https://arxiv.org/abs/2609.29785)

**<font color=#1a73e8>作者：</font>** Sheekar Banerjee, Md. Srabon Chowdhury, Md. Mahbub Hasan Akash 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate brain tumor segmentation from Magnetic Resonance Imaging is essential for diagnosis, treatment planning, and surgical guidance. Although Convolutional Neural Networks, particularly UNet, have achieved significant success in medical image segmentation, they often struggle to capture the long-range spatial dependencies required to model tumors with irregular shapes and complex boundaries. This paper proposes a lightweight Vision Transformer UNet that combines the hierarchical feature extraction capability of UNet with the global context modeling of Vision Transformers. The proposed architecture incorporates a compact ViT bottleneck within a U-Net encoder-decoder framework, enabling effective learning of both local and global features while maintaining computational efficiency with only 2.6 million trainable parameters. The model was evaluated on the TCGA LGG MRI Segmentation dataset, achieving a mean Intersection over Union of 0.8100 and a Dice score of 0.8446, outperforming the baseline UNet by 3.75% and 3.15%, respectively. Extensive quantitative and qualitative analyses, including confusion matrix evaluation, precision recall curves, per-image performance distribution, and tumor size dependency analysis, demonstrate the effectiveness and robustness of the proposed method for brain tumor segmentation.

---


### 207. [OREO: Fidelity Alignment in 3D Generation via On-the-fly Rendering-Editing Optimization](https://arxiv.org/abs/2609.29788)

**<font color=#1a73e8>作者：</font>** Zhiyuan Ma, Wenbo Hu, Wang Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent advancements in 3D generation, models often struggle to produce assets with high visual fidelity. To bridge this gap, we propose OREO, an alignment framework that enhances the realism of 3D generators by leveraging rich 2D diffusion priors. Instead of relying on static datasets, OREO establishes a dynamic optimization loop that produces on-the-fly edited renderings as 2D pseudo-targets. At its core, we introduce Reinforced Editing, which utilizes a 2D model to refine rendered views of the 3D output, enhancing their overall visual fidelity while preserving the underlying geometry, viewpoint, and content. These refined views serve as high-quality supervision targets, enabling the 3D generator to learn from its own generated samples and progressively improve its visual quality. Experiments demonstrate that OREO effectively improves upon pre-trained baselines, producing 3D assets with enhanced visual realism.

---


### 208. [S2Planner: Multi-Scale Semantic Planner for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.29813)

**<font color=#1a73e8>作者：</font>** Zhaowei Lu, Liguo Zhou, Yujie Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present S2Planner, a trajectory planner that combines three front-facing cameras with ego-motion history and the current driving command. A fine-tuned DINOv3 backbone and a Spatial Tuning Adapter produce multi-scale image features; a coarse-to-fine decoder then uses trajectory self-attention and camera-projected cross-attention to refine candidate waypoints. The contribution is the integration of ego-conditioned trajectory initialization with iterative, geometry-guided sampling of multi-scale image features, rather than a new visual backbone or attention operator. On the NAVSIM v1 non-reactive evaluation, the previously reported navtest run obtained 88.03 PDMS. Because that run was selected using navtest performance, this number is exploratory and cannot be interpreted as an unbiased test estimate. Validation-selected evaluation on unexposed data, repeated runs, and computational measurements are needed to establish generalization and efficiency.

---


### 209. [SwitchPFN: Shared Switching Dynamics for Frozen In-Context Time Series Classification](https://arxiv.org/abs/2609.29814)

**<font color=#1a73e8>作者：</font>** Zhenyi Zhu, Jacqueline Pang, Peilin Shen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) provide a promising route to time-series classification, but their effectiveness depends on how sequential data are converted into tabular representations. Existing representations face two challenges: global aggregation can lose the order of temporal evolution, while features computed in independently fitted coordinate systems may not have consistent meanings across sequences. We therefore view representation design for TFMs as a problem in its own right: the representation should preserve local temporal transitions while maintaining a shared feature definition across samples. We propose SwitchPFN, which learns a shared projection and regime codebook from the training sequences, making local dynamic operators and transition features directly comparable across samples. Across the evaluated benchmarks, SwitchPFN achieves the highest mean accuracy among the evaluated methods, improving over the strongest baseline by 4.47% relatively. Ablation studies, parameter sensitivity analyses, and reduced-training-data experiments further examine the contributions of the representation, its main design choices, and its behavior when labeled data are limited.

---


### 210. [Decoding Imagined Speech: A Strictly Subject-Independent Approach Using EEG](https://arxiv.org/abs/2609.29820)

**<font color=#1a73e8>作者：</font>** Frederik Møllskov Trier, Xiaopeng Mao, Sadasivan Puthusserypady  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Imagined speech decoding from electroencephalography (EEG) has gained increasing attention as a potential communication pathway for individuals with severe motor impairments, yet reported performance often relies on evaluation protocols that do not clearly reflect cross-subject generalization. This study presents a transparent baseline investigation of a multi-class imagined speech EEG dataset under a strictly subject-independent evaluation framework. Two preprocessing and feature extraction pipelines were compared: a time-domain statistical feature approach and a frequency-domain spectral bandpower approach, evaluated using subject-wise cross-validation and trial-level majority voting with a random forest classifier. The spectral pipeline achieved a significantly higher mean trial-wise accuracy than the statistical pipeline (49.03 $\pm$ 4.18% vs. 37.97 $\pm$ 3.79%) for coarse-level classification across subjects. Forward feature selection further indicated that a limited subset of frequency bands captured most of the discriminative information. Overall, this work provides a strong basis for future brain-computer interface studies targeting improved cross-subject generalization in EEG-based imagined speech decoding.

---


### 211. [Anatomy-Aligned Surface Field Learning for Myocardial Reconstruction from Sparse Short-Axis Cine MRI](https://arxiv.org/abs/2609.29825)

**<font color=#1a73e8>作者：</font>** Xiaohan Yuan, Xuan Yang, Qingya Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Patient-specific 4D myocardial reconstruction from cine MRI supports quantitative functional assessment, regional motion analysis, and simulation-based modeling. However, routinely acquired short-axis (SAX) cine MRI is sparsely sampled along the through-plane direction, making dense and anatomically consistent surface reconstruction challenging. In this study, we propose an anatomy-aligned surface learning framework that parameterizes the epicardial and endocardial surfaces on a shared circumferential-longitudinal UV domain. This formulation converts irregular 3D reconstruction into structured coordinate-field completion with explicit correspondence across subjects and cardiac phases. Sparse SAX contours are encoded as UV observation fields, coverage-aware sampling improves robustness to incomplete slice coverage, and topology- and distortion-aware learning preserves circumferential continuity and local surface quality. Experiments on three public cine MRI datasets showed that the proposed method consistently outperformed representative mesh-based and implicit reconstruction approaches, achieving overall Chamfer distances of $2.887$~mm on ACDC, $2.641$~mm on M\&Ms, and $2.810$~mm on M\&Ms-2. The reconstructed sequences also preserved ventricular function, with end-diastolic volume and ejection fraction errors of $3.3$~mL and $1.1 \%$, respectively. These results demonstrate that anatomy-aligned UV learning provides an accurate, efficient, and correspondence-aware representation for sparse cine MRI reconstruction and myocardial modeling. The source code will be available at this https URL.

---


### 212. [SplatLabel: Pseudo-Labelling through 4D Gaussian Splatting](https://arxiv.org/abs/2609.29836)

**<font color=#1a73e8>作者：</font>** Nitya Nanvani, Andras Palffy, Holger Caesar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 2D Vision Foundation Models offer a pathway to automate 3D semantic pseudo-labelling, translating these priors into robust 3D representations typically requires complex heuristics or multi-model ensembles. We introduce SplatLabel, an automated pipeline that leverages a 4D Gaussian representation to extract LiDAR segmentation with predictive confidence, as well as semantic occupancy grids at arbitrary voxel resolutions. At its core, SplatLabel handles dynamic environments through an explicit temporal manifold that models the trajectories and lifespans of individual 3D primitives. This allows the system to accurately track moving actors and strictly define when objects appear and disappear, completely eliminating the need for pre-annotated 3D bounding boxes. To robustly support this dynamic tracking, the representation is grounded by structural and semantic priors: we guide scene geometry in unobserved regions by integrating 360-degree LiDAR via virtual depth maps, and rather than relying on domain-specific prompt engineering, we directly distill continuous soft probabilities from 2D models to inherently resolve semantic ambiguities over time and space. Finally, to accurately reflect the real-world trade-off between precision and recall, we reframe pseudo-label evaluation as a selective classification task using a generalized risk-recall metric. Experiments on SemanticKITTI demonstrate that SplatLabel consistently outperforms state-of-the-art baselines across multiple recall levels, establishing a highly robust framework for both 3D LiDAR segmentation and occupancy prediction.

---


### 213. [Template Ageing and Longitudinal Verification in Fixed-Text Keystroke Dynamics: A Subject-Disjoint Study Across Eight Weeks](https://arxiv.org/abs/2609.29851)

**<font color=#1a73e8>作者：</font>** Simon Parkinson, Saad Khan, Na Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Behavioural biometric templates are widely believed to degrade as the gap between enrolment and verification grows, but few studies measure this template ageing effect directly under controlled conditions. We collected a longitudinal dataset of 40 fixed passwords, each typed four times per weekly session over eight consecutive weeks. We compare a scaled-Manhattan matcher (M1), a gradient-boosted classifier (M2), a TypeNet-style recurrent embedding model (M3), and a TypeFormer-style Transformer (M4) under a 5-fold subject-disjoint protocol and a design that jointly varies mechanism and the enrolment-to-query gap, from 0 to 7 weeks. Template ageing proves large and systematic. Error increases monotonically with the gap for every mechanism, from an EER of 14.6-27.2% at a gap of zero to 25.5-37.1% at seven weeks, or 1.7% of decision error per week elapsed (p < 0.001). However, the choice of mechanism matters more than its rate of ageing. Baseline accuracy spans 12.6 percentage points across the four mechanisms, the degradation each accumulates over seven weeks spans only 2.3 points, and ageing never reorders them. A matcher can therefore be chosen on same-session accuracy, with ageing managed by re-enrolment scheduling rather than by matcher selection. The two properties are nonetheless distinct, as M3 is the least accurate mechanism yet ages significantly more slowly than M1 under every specification tested. Training randomness also matters differently by architecture, with 58% of the recurrent model's fold-to-fold variance attributable to seed noise against 19% for the Transformer. Because the smaller ageing-rate differences are sensitive to modelling choices, while the accuracy differences and the ageing effect are not, we recommend that comparative ageing-rate claims be supported by seed-level score fusion, independent replication, and an alternative outcome-model specification.

---


### 214. [Multi-Task Learning by using Contextualized Word Representations for Syntactic Parsing of a Morphologically Rich Language](https://arxiv.org/abs/2609.29855)

**<font color=#1a73e8>作者：</font>** Toqeer Ehsan, Miriam Butt, Sarmad Hussain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We address the challenge of syntactic parsing for Urdu, a morphologically rich language, and present state-of-the-art results for both constituency and dependency parsing. This paper offers four major contributions: 1) the conversion of the CLE-UTB phrase structure treebank into a dependency treebank by developing language-specific head-word and phrase-to-dependency label mapping rules; 2) a novel sequence labeling scheme that transforms the parsing task into a unified representation; 3) the training of contextualized word representations on a large 220 million tokens Urdu corpus collected from the web; and 4) development of parsing framework using two learning paradigms, single-task and multi-task learning. Several post-processing rules are applied to improve the quality of the automatically converted dependency structure treebank. The proposed sequence labeling scheme enables the use of a shared architecture that learns the syntactic structures from both grammatical structures simultaneously and hence improves generalization. Experiments show that the multi-task learning setup significantly enhances parsing performance, achieving an F1 score of 91.39 for constituency parsing (an improvement of 3.29 points) and a labeled attachment score of 85.69 for dependency parsing (an improvement of 1.49 points). These results demonstrate that learning cross-task representations provides measurable benefits and advances the state of syntactic parsing for Urdu.

---


### 215. [Modelling dynamic systems transfer functions from events in computational neuromorphic imaging](https://arxiv.org/abs/2609.29863)

**<font color=#1a73e8>作者：</font>** Nimrod Kruger, Gregory Cohen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event Vision Sensing (EVS) report threshold crossings of log-irradiance, so a static optical system imaging a static scene produces no output at all. The classical procedure for measuring a Point Spread Function (PSF), illuminating the system with a constant point source, therefore has no event-based equivalent: the probe must carry a temporal profile, and that profile becomes part of the measurement. A growing body of Computational Neuromorphic Imaging (CNI) work already exploits this, pairing engineered or modulated optics with event sensing, but each system adopts a particular excitation together with a particular reading of the event stream without the correspondence between the two being stated. We examine that correspondence directly within a analytical framework of an Linear Shift-Invariant (LSI) optical system with a specified Modulation Transfer Function (MTF), a first-order filter EVS pixel model, and three different temporal probes: a step function, a linear ramp and an exponential ramp. By analysing the inverse of the entire chain for different event-statistic, and comparing the results to the specified MTF, we identify the context where each probe is most relevant. We consider how photon-noise and cross-array threshold mismatch effects the analytical accuracy of the probe-inverse. Results show that the widely used step probe is highly susceptible to mismatch while resilient to photon shot-noise, while a linear rise probe and exponential rise probe retain their ability to infer signal levels even with high mismatch. We discuss the potential of dynamic-PSFs as components of a full forward operator from scene to events. In this, we use this analytical description to define dynamic-PSFs around EVS, and discuss the gaps toward a unified pixel model and a scene-composition framework required for CNI.

---


### 216. [Efficient Continuous DEM Reconstruction under Limited Target-Resolution Supervision](https://arxiv.org/abs/2609.29864)

**<font color=#1a73e8>作者：</font>** Zekai Shi, Meng Zhang, Haokun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution digital elevation models (DEMs) support Earth observation applications, but paired training references are often available only at coarser output resolutions. Reconstructing finer terrain grids therefore requires both effective transfer beyond the supervised scale and control of dense-query computation. To address this problem, SCOPE learns a continuous terrain representation from coarser-resolution pairs. It predicts a latent coefficient field on the low-resolution grid and reuses local Fourier residual functions through basis evaluation and geometry-guided ensemble fusion. This separates high-dimensional coefficient prediction from output-grid construction. Experiments on geographically distributed land--ocean samples assess supervised reconstruction, unseen-scale inference, cross-domain generalization, and theoretical computation. SCOPE leads the compared methods across six metrics in the main supervised-scale evaluation. At an unseen factor three times the training factor, land reconstruction reduces RMSE and MAE by approximately 12\% relative to bicubic interpolation, with errors close to target-scale fine-tuning. Ninefold output density increases counted multiply--accumulate operations by only about 2\%. Frozen-model validation on held-out external marine regions reduces RMSE relative to the DEM-specific implicit baseline EBCF-CDEM by approximately 19\% under self-downsampling and 2\% with cross-product inputs, while also yielding lower RMSE than LIIF-MS in both settings. These results demonstrate the value of reusable coefficient fields for accurate reconstruction beyond the supervised resolution with low incremental arithmetic cost.

---


### 217. [From Graphs to Feeders: Constraint-Guided Diffusion for Rule-Compliant Feeder Generation](https://arxiv.org/abs/2609.29879)

**<font color=#1a73e8>作者：</font>** Yu Qin, Andrew Glaws, Aadil Latif 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative modeling approaches often focus on recovering broad statistical characteristics from the training data. In the context of graph generation, this may refer to degree distributions, clustering coefficients, or spectral properties. However, generating usable distribution feeders when detailed feeder models are unavailable requires more than matching generic graph statistics: the sampled topology must also obey electrical compatibility and radiality rules. We therefore formulate feeder synthesis as a constraint-guided graph generation problem and propose the Power-Grid-constrained Discrete Denoising Diffusion model, PG-DiGress, which learns categorical node and edge patterns from feeder data, while respecting domain-specific rules. Specifically, it injects feeder constraints into the reverse diffusion process through soft masks that suppress incompatible edge classes during denoising, followed by a final projection step that rebuilds a connected, rule-compliant feeder graph. We evaluate PG-DiGress using graph-distribution similarity, feeder-rule satisfaction, structural validity, and downstream model construction. Compared with the unconstrained baseline, PG-DiGress increases the strict feeder pass rate from 13.7% to 96.8%. We also successfully convert the generated graphs into executable feeder models for downstream analysis.

---


### 218. [Working with Agentic `Teammates': When a New Organizational Actor Collides with the Human Ecosystem of Work](https://arxiv.org/abs/2609.29901)

**<font color=#1a73e8>作者：</font>** Rida Qadri, Remi Denton, Michael Madaio 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Enterprise AI is transitioning from single-user, reactive tools toward proactive, multi-user 'teammates,' but our empirical understanding of this transition is limited. In this paper, we present an in-situ qualitative study of a persistent, proactive AI agent 'teammate' deployed across multiple teams in a large technology company. Our findings reveal the boundaries of the human-agent workplace are actively in flux, triggering breakdowns and negotiations across: 1) tacit rules of collaborative human workflows, 2) the relational boundaries of this new non-human actor, and 3) the redistribution of trust and human agency. We use these early micro-negotiations as signals to chart a new research, design, and organizational agenda that intentionally preserves human agency in a workplace shared with non-human organizational actors.

---


### 219. [Spatio-temporally complementary feature propagation on graphs for longitudinal AADT estimation](https://arxiv.org/abs/2609.29906)

**<font color=#1a73e8>作者：</font>** Linghang Sun, Qishen Zhou, Michail A. Makridis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The estimation of Annual Average Daily Traffic (AADT) is vital for transportation planning and infrastructure maintenance, yet obtaining accurate values for an entire urban network across multiple years remains challenging due to the high cost and spatial sparsity of physical sensors. This research proposes a novel spatio-temporally complementary feature propagation framework that leverages the strengths of two distinct data sources: spatially sparse but temporally dense loop detector data, and a spatially complete but temporally sparse macroscopic transportation model. The methodology highlights a feature propagation algorithm on directed graphs, formulated as a Poisson energy minimization considering residues. The standard binary adjacency matrix is replaced with flow ratio matrices to capture real-world vehicle turn ratios at intersections. Validated in the city of Zurich, the algorithm demonstrates high computational efficiency, achieving convergence within minutes. Results indicate that the framework effectively reconciles theoretical models with empirical ground truths, yielding a normalized mean absolute error below $10\%$. This scalable approach provides a feasible solution for spatio-temporal network-wide AADT estimation through combining real-world limited sensor coverage and traffic models.

---


### 220. [EndoFSA: Endoscopic Few-Shot Image Generation via Rank-Constrained Parameter Adaptation](https://arxiv.org/abs/2609.29930)

**<font color=#1a73e8>作者：</font>** Panagiota Gatoula, Grigoris Karypidis, Dimitris K. Iakovidis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> WCE produces large-scale gastrointestinal image data yet pathological findings remain significantly underrepresented limiting the generalization performance of deep-learning based abnormality detection systems. SDG methods offer a practical solution to mitigate this imbalance. However their training directly on scarce abnormal samples often results in instability overfitting and structural distortions. Addressing these challenges requires controlled adaptation mechanisms that preserve anatomical priors while enabling realistic pathological variation. This paper presents EndoFSA a GAN-based model for Endoscopic Few-Shot image generation by Adaptation in WCE imaging. EndoFSA leverages a generator pretrained on abundant normal data and adapts it to abnormal domains using limited number of training samples through a rank-constrained parameter adaptation where only a small number of modulation parameters is updated while the pretrained weights remain frozen. By restricting parameter updates to a low dimensional subspace and incorporating perceptual boundary regularization and cluster-wise diversity control EndoFSA enables efficient model adaptation under limited data conditions and mitigates mode collapse while preserving the anatomical priors learned from normal data. Importantly EndoFSA operates without requiring pixel-level annotations, masks or bounding box supervision. Evaluation on publicly available WCE benchmark datasets spanning various abnormal categories demonstrates that EndoFSA generates abnormal images reproducing real lesions morphology. Moreover in a downstream classification task training an image classifier solely on synthetic abnormal images generated by EndoFSA yields performance comparable to that obtained with real images.

---


### 221. [Improving Calibration of Black-Box Radiology AI Using Test-Time Augmentation](https://arxiv.org/abs/2609.29931)

**<font color=#1a73e8>作者：</font>** Nathan Le, Magdalini Paschali, Arogya Koirala 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Radiology AI systems increasingly inform clinical decisions such as triage, follow-up imaging, and treatment planning. For these decisions to be made safely, model outputs must be well calibrated, meaning predicted probabilities accurately reflect true risk. Many standard techniques for improving calibration, such as MC Dropout and Deep Ensembles, require access to model parameters or retraining. However, proprietary clinical AI systems operate as black boxes, preventing access to the model's internals. To that end, we propose a model-agnostic framework for improving calibration of black-box models using clinically grounded test-time augmentation (TTA). Our framework applies geometric and physics-inspired 3D CT perturbations and learns probability-level aggregation strategies without access to model internals or the original training data. Across pulmonary embolism and intracranial hemorrhage detection tasks, DualTTA achieved the strongest overall calibration among TTA methods, reducing the Expected Calibration Error by 54% (0.239 -> 0.109) and 43% (0.051 -> 0.029), respectively, while requiring only input-output access. Additionally, DualTTA outperformed uncertainty estimation techniques that require access to model internals, such as Temperature Scaling, MC Dropout, and Deep Ensembles, in most calibration metrics. These results demonstrate that learned TTA aggregation can improve the calibration of clinical AI systems, providing a practical approach for improving the reliability of black-box medical AI.

---


### 222. [Beyond Spatial Benchmarks: From Spatial Reasoning to Navigation](https://arxiv.org/abs/2609.29934)

**<font color=#1a73e8>作者：</font>** Xun Huang, Shijia Zhao, Rongsheng Qu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Does progress on spatial reasoning benchmarks translate into better navigation? Existing benchmarks test isolated inferences from images or videos, with little connection to downstream navigation. Our analysis reveals a gap between benchmark-oriented spatial specialization and navigation performance, and shows how aligning spatial supervision with navigation goals, phases, and decision learning improves navigation. Guided by these findings, we build \textsc{Spatial-Nav-100K} and fine-tune in two stages, \textit{i.e.} first learning a shared spatial-navigation foundation, and then specializing each phase with the abilities it relies on. We further introduce Spatial-NPD, where a teacher conditioned on spatial priors produces grounded action preferences and distills them into a student policy, so no explicit spatial reasoning is needed at inference. With 45 A100 GPU-hours of policy training, our 8B model reaches SR/SPL of 77.4/35.4 on HM3D-v0.2, 60.2/30.5 on HM3D-v0.1, and 47.9/20.6 on train-unseen MP3D. It outperforms several systems that rely on closed-source models or thousands of GPU-hours of training, at 148 ms per action step. All code and datasets will be publicly available at this https URL.

---


### 223. [When Temporal Perturbations Act Like Sensor Biases: Label-Free Auditing of Wearable Activity Recognizers](https://arxiv.org/abs/2609.29937)

**<font color=#1a73e8>作者：</font>** Qingyu Wu, Yuan Wei, Renju Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable human-activity recognition (HAR) models operate across sensors, subjects, and backbones, yet a smooth waveform may appear temporal while exploiting a persistent sensor offset primarily. We introduce SpectrumAudit, a label-sealed audit that fits a phase-randomized full-window stimulus on calibration windows from subjects held out from training and testing. After selection, it replays its exact DC projection and budget-constrained zero-mean residual on the same frozen victim without refitting. Across 27 victims from three datasets and three backbones, the selected waveforms cause 2.87-40.83-point three-phase robust accuracy losses. Under this replay budget, DC is more damaging than AC on 24/27 victims and recovers at least 90% of the full drop on 22/27; all 5 failures occur on WISDM. In a held-out UTD-MHAD check, the selected waveform causes 13.49-pp accuracy and 11.68-pp macro-F1 losses, versus -0.66 pp for matched random changes. The audit diagnoses offset versus zero-mean variation under a common peak-budget cap. The code will be released upon acceptance.

---


### 224. [MF-SCBO : Multi-fidelity Scalable Constrained Bayesian Optimization](https://arxiv.org/abs/2609.29941)

**<font color=#1a73e8>作者：</font>** Lucas Palazzolo, Mickaël Binois, Laëtitia Giraldi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world optimization problems rely on expensive simulations or experiments, making the efficient use of available data essential. Multi-fidelity optimization of high-dimensional black-box functions subject to black-box constraints is increasingly relevant as the cost of objective evaluations continues to rise in applications such as machine learning, engineering, and control. To our knowledge, no existing method simultaneously addresses high-dimensionality, black-box constraints, an arbitrary number of fidelity levels, and non-nested sampling. In this work, we extend the Scalable Constrained Bayesian Optimization method to the multi-fidelity setting, resulting in the MF-SCBO method. The proposed approach is evaluated on standard benchmark functions as well as challenging problems. The experimental results demonstrate that MF-SCBO generally achieves better convergence than both the single-fidelity SCBO and the other multi-fidelity method considered in this high-dimensional and constrained settings.

---


### 225. [Error- and Prediction-Driven Motor Learning in the Cortico-Cerebellar Loop](https://arxiv.org/abs/2609.29945)

**<font color=#1a73e8>作者：</font>** Ana Carolina Filipe, Rui Ponte Costa, Cláudia Soares  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust control under delayed sensory feedback remains a key challenge in both robotics and neuroscience. Classical cerebellar models explain delay compensation through forward prediction but fail to account for fast online corrections and rapid adaptation observed in biological systems.
We propose a cerebellum-inspired control framework that combines multiplexed predictive representations with internal feedback. By jointly encoding kinematic variables and task-relevant error signals, the model enables accurate online correction despite delayed feedback. Furthermore, incorporating feedback within the cerebellar loop significantly accelerates adaptation, reducing learning time by an order of magnitude.
Our results show that single-signal predictions are insufficient under delay, while multiplexing and feedback together provide a unified mechanism for online control and rapid learning.

---


### 226. [Tracking States or Tracking Cosets? An Algebraic Account of Learned State Tracking](https://arxiv.org/abs/2609.29951)

**<font color=#1a73e8>作者：</font>** Zhiyu Zhang, Yupeng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State tracking requires composing a sequence of updates, but accuracy alone does not reveal what a model has learned. We study neural networks trained to predict the running product of group elements. We identify quotient solutions in Transformers, where models recover the quotient class while predicting nearly uniformly among its members. The reciprocal of class size predicts partial accuracy without a fitted parameter, extending parity-based accounts to non-parity quotients. Our baseline Transformers' predictions change little under prefix reordering beyond the exact-tracking frontier. We prove that, for finite groups under uniform i.i.d. full-group inputs, optimal order-blind exact accuracy converges to the reciprocal of abelianization class size as prefix length grows, consistent with the observed abelianization plateaus. Sequential updates permit more: any partition into right cosets of a subgroup, normal or not, survives sequential updates. In our census of standard Transformers, every recovered coset partition comes from a normal subgroup, whereas parameter-matched recurrent networks pass through both normal and non-normal right-coset stages during training. On $A_5$, we identify low-dimensional subspaces of the recurrent state that encode non-normal cosets. In the three-dimensional cases, coset mean vectors form approximate dodecahedra, and swapping the state components in these subspaces transfers the donor's coset state through a shared input suffix. Our results connect partial accuracy, learning stages, and internal computation through the subgroup cosets that models learn to track.

---


### 227. [Not All Confusion Is Equal: A Source-Aware Uncertainty Diagnosis for Fine-Grained Aircraft Detection](https://arxiv.org/abs/2609.29959)

**<font color=#1a73e8>作者：</font>** Hai Huang, Helmut Mayer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained object detectors are commonly evaluated with confusion matrices, which show where the model is confused but not why, nor whether the confusion can be reduced. We argue that confusion can be attributed to distinct, separable sources, each quantitatively measurable, turning a passive measurement into actionable guidance. We present $A^2E^2$, a diagnostic tool that decomposes the sources of confusion along two axes, $\{$aleatoric, epistemic$\} \times \{$within-class, between-class$\}$, giving a $2\times2$ taxonomy that enumerates the source types. Each quadrant is measured by its own quantity, computed in one of three places (input geometry, output-space disagreement, and the bias-parameter posterior), so the two epistemic sources are separated by construction rather than by an empirical correlation. On fine-grained aircraft detection, the four quadrants become four named sources with their own remedy verdict: affinity (geometric similarity, irreducible from size alone), heterogeneity (geometrically heterogeneous sub-variants, pointing to re-labeling rather than more data), contested (an insufficiently trained but learnable boundary, improvable), and collapsed (a class starved of data, reducible). After attributing the confusion to a specific reducible source, we apply a targeted intervention and verify experimentally that it reduces the diagnosed source specifically while leaving the irreducible sources unchanged. $A^2E^2$ thus turns confusion measurement into a concrete, validatable and actionable "diagnosis" in which the same off-diagonal mass can carry opposite causes and opposite remedies. We also state this framework's limits, including which sources are only partially identifiable on this specific dataset and why.

---


### 228. [A Contraction Framework for Stochastic Operators with Bootstrapping: Application to TD Learning](https://arxiv.org/abs/2609.29961)

**<font color=#1a73e8>作者：</font>** Ids van der Werf, Sergio Rozada, Antonio G. Marques  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many iterative algorithms rely on bootstrapping. A variable is updated using a second, frozen copy as a target, which is periodically replaced with the updated variable. Majorize-minimize and inexact proximal-point methods share this structure, as does temporal-difference (TD) learning. However, existing convergence guarantees for scenarios that combine sampled updates with targets refreshed only every $K$ steps rely on the specific structure of the update, such as linear approximation or gradient-based inner steps, and on uniformly bounded sampling error. We instead model the sampled update as a stochastic operator on the parameter space, which reduces the analysis to a contraction argument that needs no gradient structure and allows the sampling error to grow with the iterates. Within this framework, we derive a finite-time bound for i.i.d. samples and any target-update period $K$. We show that the iterates converge geometrically in root mean square to a ball around the fixed point, provided the sensitivity to the frozen target is smaller than the contraction slack of the inner map. Existing deterministic frozen-target contraction and stochastic-gradient-type bounds follow as special cases of our framework, and simulations of TD learning reproduce the predicted contraction rate and scaling of the error floor with the step size.

---


### 229. [ADATEX4D: adaptive texture capacity allocation for 4D gaussian splatting](https://arxiv.org/abs/2609.29963)

**<font color=#1a73e8>作者：</font>** De Jiang, Peiqiang Wang, Kehong Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Textured Gaussians improve local appearance capacity, but assigning the same texture resolution to every primitive wastes storage on low-detail or weakly visible regions. We introduce AdaTex4D, an adaptive texture-capacity module for deformation-based 4D Gaussian Splatting. Each Gaussian carries packed RGBA triplanes whose two axes grow independently according to visibility normalized screen-space gradients and deformed local scales. Experiments on N3DV and PanopticSports show that AdaTex4D reduces texture storage by more than half while preserving reconstruction quality. Under fixed memory budgets, adaptive allocation also improves quality over uniform texture assignment and reduces overall model and peak memory. These results show that dynamic, anisotropic texture allocation provides a more efficient way to distribute local appearance capacity in 4D Gaussian representations.

---


### 230. [Diverse Geometries, Frozen Weights: Robust Heterogeneous Treatment-Effect Estimation via Causal Expert Ensembles](https://arxiv.org/abs/2609.29974)

**<font color=#1a73e8>作者：</font>** Ali Haghpanah Jahromi, Mohammad Taheri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating heterogeneous treatment effects from observational data is difficult because the most appropriate inductive bias varies with overlap, treatment imbalance, prognostic structure, and sample size. We introduce the Geometry-Diverse Anchor-Correction Expert Ensemble (GeoACE), a five-expert framework that combines a common anchor-correction estimator with complementary overlap-aware and outcome-guided geometries. Its task-level ensemble weights are learned only from internal validation predictions, frozen before test evaluation, and then applied to experts refitted on the complete development sample. The fifth expert, O-Phi-ACE, constructs an outcome-free, overlap-aware statistical projection from covariates and treatment assignment and replaces the anchor input with this lower-dimensional geometry. We evaluate GeoACE against 11 comparators on eight benchmark protocols. Adding O-Phi-ACE reduced mean sqrt(PEHE) relative to the four-expert ensemble on all seven benchmarks with individual-effect truth, winning 998 of 1,225 paired tasks; the change on JOBS policy risk was negligible. The five-expert ensemble ranked first on IHDP100, IHDPA, and IHDPB and second on NEWS, differing from the NEWS leader by 0.13%. Across the seven sqrt(PEHE) benchmarks it obtained the lowest observed average rank (3.714), although the omnibus Friedman and Iman-Davenport tests were not significant (p=0.328 and p=0.330). Using the same five frozen experts, inverse-DR weighting was consistently better than winner-take-all selection, convex DR fitting, R-stacking, and causal Q-aggregation in benchmark-balanced analyses, but was statistically indistinguishable from equal weighting and DR ridge shrinkage. The evidence therefore supports geometry-diverse expert libraries and leakage-free aggregation as a robustness strategy, not universal superiority of either GeoACE or one weighting rule.

---


### 231. [Sluice: Global Invariant, Local Enforcement for Pooled Payment-Channel Liquidity](https://arxiv.org/abs/2609.29975)

**<font color=#1a73e8>作者：</font>** Yueqi Wu, Huiping Sun, Peilu Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A routing node on the Lightning Network holds its liquidity in separate channels, so a payment can fail at a channel whose outbound balance is exhausted while the node's other channels still hold balance. Pooling the channels into one reserve fixes this only if the node's draws across all channels stay within the reserve: a global invariant that each counterparty must enforce from its own channel, with no shared counter that off-chain draws can update. A node must therefore split the reserve into per-channel quotas in advance or coordinate every draw with every counterparty. On three Lightning snapshots the advance split forfeits $16$ to $67\%$ of the pooling gain over unpooled channels, and the loss grows with channel count. Sluice recovers $19$ to $65\%$ of that loss with a nested reservation: each channel keeps an exclusive base that its counterparty checks alone, and the rest is a shared overflow drawn on with certificates from a capacity-weighted quorum of the node's counterparties. Two conflicting certificates share an honest signer, so over-drawing is prevented without a slashable stake, under a stated bound on the capacity the node controls in the signing set. Sluice loses at most $1.3$ points of payment success to coordination where deployed coin movers lose up to $10.3$, and improves them in eleven of twelve cells when stacked on them. Re-creating every base output each epoch costs $2.8$ to $5.1$ times Lightning's on-chain bytes; re-creating only those that overflowed costs $0.5$ to $1.2$ times and keeps part of the gain.

---


### 232. [A Lightweight Ethereum Voting Prototype for Hospital Ethics Committees with Receipt-Based Inclusion Verification](https://arxiv.org/abs/2609.29981)

**<font color=#1a73e8>作者：</font>** Edwin Clatus, Madhusudan Singh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents a Solidity, Hardhat, React, MetaMask, and this http URL prototype for hospital ethics committee voting. Role controls, case-state checks, duplicate vote controls, and a receipt hash support public audit and transaction inclusion verification. Because vote events expose wallet addresses and vote values, the design provides pseudonymous auditability, not anonymous or secret-ballot voting; the receipt is neither receipt-free nor coercion-resistant. Evaluation reports 22 passing functional tests and local Hardhat gas use, including 284,137 gas per vote. A 12-participant simulation used assumed probabilities and is not human-subject evidence. Residual risks include multiple wallets, administrator or frontend compromise, credential reassignment, front-running, denial of service, and untested adversarial paths. Confidential deployment requires governed enrollment, encrypted ballots, independent audit, adversarial testing, reproducible benchmarks, and a real user study.

---


### 233. [OceanXL: Large-scale Underwater 3D Gaussian Splatting via Block Partitioning and Adaptive Pruning](https://arxiv.org/abs/2609.29985)

**<font color=#1a73e8>作者：</font>** Haoran Wang, Shaoyu Cai, Adrian Azzarelli 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater 3D reconstruction is critical for marine exploration, ecological monitoring, and subsea infrastructure inspection, yet remains challenging at large scale due to light attenuation, scattering, and limited capture coverage. While 3D Gaussian Splatting (3DGS) enables high-quality real-time rendering, its application to large underwater scenes is constrained by high memory consumption and inefficient optimization over extensive areas. We propose OceanXL, a fast and scalable 3DGS-based framework for large-scale underwater reconstruction. OceanXL adopts a divide-and-conquer strategy, partitioning scenes into spatially coherent blocks to enable efficient optimization while preserving global geometric consistency. We further introduce an adaptive pruning scheme tailored to underwater conditions that removes redundant primitives, producing compact representations without sacrificing visual fidelity. Together, these components improve training efficiency and rendering performance for large scenes. We also introduce a large-scale underwater dataset covering diverse marine environments. Experiments on five large-scale scenes demonstrate favorable scalability, compactness, and efficiency--quality trade-offs over large-scene baselines. Controlled comparisons on the small-scale SeaThru-NeRF dataset further show competitive reconstruction quality with substantially smaller model sizes than underwater-specific methods.

---


### 234. [Advancing Model Research in AgentX: Long-Horizon Autonomy for Industrial Recommender Systems](https://arxiv.org/abs/2609.30001)

**<font color=#1a73e8>作者：</font>** Shuang Yang, Zijie Zhuang, Changxin Lao 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sustaining industrial recommendation research requires using the results of one experiment to decide what to investigate next. We present AgentX-Model, the next generation of AgentX's model research framework, which connects proposal development and model experimentation within sandboxes defined by business inputs and prediction tasks. AgentX-Model adopts a dual-agent architecture comprising a Research Agent and a Model Agent. The Research Agent develops independently reviewed proposals from papers and experimental findings, while the Model Agent conducts multi-round investigations and returns code, measurements, and unresolved questions. Using the returned results, the Research Agent selects a starting implementation and formulates the next research question, allowing subsequent experiments to build on earlier findings. We organize this continuing research around four actions: Reproduce, Follow-up, Composition, and Diagnose. The first three actions drive routine research, while Diagnose acquires the evidence needed to choose a repair, including for issues raised by business feedback and online evaluation, such as prediction bias measured by PCOC. Across the production evaluation, 560 of 636 completed model-changing experiments recorded AUC above their business baselines. As research continued, some experiments recorded AUC above every comparable ancestor in their lineages. The five latest online A/B evaluations across different business settings reported gains including 10-15% in acquisition efficiency, 15-20% in target-segment advertising spend, and 0.3-0.8% in watch time; the watch-time model used approximately 10% fewer FLOPs and parameters. A dependency-aware historical-replay benchmark further evaluates research allocation, with initial results showing no consistent efficiency gain from more complex scheduling when agents already analyze and select concrete candidates.

---


### 235. [VietPrism: A large-scale Vietnamese speech and deepfake corpus with diverse dialects and code-switching](https://arxiv.org/abs/2609.30005)

**<font color=#1a73e8>作者：</font>** Minh Hoang, Thai Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vietnamese speech research is constrained by resources that isolate automatic speech recognition from speaker, dialect, code-switching, and deepfake analysis. We introduce VietPrism, an open, multi-domain corpus that brings these dimensions together at scale: 993.4 hours and 403,941 bona fide utterances from 1,262 verified speakers across 8,388 real-world videos. To our knowledge, it is the first large-scale Vietnamese corpus to jointly provide transcripts, consistent speaker identities, five dialect groups, and naturally occurring Vietnamese--English code-switching, which constitutes nearly half of the corpus by duration. We further create over 3.1K hours of spoof speech with four open-source and commercial synthesis systems. Every spoof is conditioned on a verified speaker reference and paired with a transcript- and speaker-matched bona fide utterance, enabling unique controlled evaluation with reduced lexical and identity confounds. Zero-shot evaluation of five pretrained multilingual detectors reveals striking brittleness: EER greatly varies across detector--generator pairings, while recent multilingual detector DFA-1B degrades from 16.3% to 33.6% as speaker similarity increases. Dialect-stratified results expose further model-dependent disparities. By unifying natural linguistic diversity with controlled spoof generation, VietPrism provides a challenging foundation for Vietnamese speech modeling and trustworthy audio-deepfake detection.

---


### 236. [Training-Free Hold-Usage Detection in Sport Climbing with Foundation Pose Models](https://arxiv.org/abs/2609.30026)

**<font color=#1a73e8>作者：</font>** Abu Bakar, Abdullah Aftab, Amir Hamza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting which holds a climber uses, and when, underpins automated scoring, movement analysis, and assistive systems for sport climbing. Existing approaches train task-specific models or repurpose 2D pose estimators whose hand keypoint sits at the wrist and foot keypoint at the ankle i.e. offset from the fingertips and toes that actually contact the holds, and whose hands are occluded in roughly half of all frames. We show that a frozen, off-the-shelf pose foundation model is sufficient: using the fingertip and toe keypoints of Sapiens, a per-frame proximity test against the annotated holds, per-limb mutual exclusion, and a short temporal-persistence rule, we detect hold usage without any climbing-specific training. On the The Way Up dataset (22 videos, 10 athletes, two routes), our method reaches an event F_1 of 90.2% on a held-out split (89.8% under leave-one-participant-out cross-validation) and 79.9% over all 22 videos at any temporal overlap, and performs best on footholds (F_1,89.8% overall, 96.6% held-out). Under an identical protocol it exceeds our reproductions of the YOLOv8-pose and ViTPose pipelines at every temporal threshold, with the margin widening under strict timing. An ablation shows that two intuitively helpful additions---dense foundation-feature change gating and body-part segmentation---both hurt, arguing that a minimal, keypoint-only design is the right one for this task. Finally, standard coaching statistics computed from our automatic predictions track ground truth closely (Pearson r=1.00 for climb time, 0.94 for pace), turning ordinary single-camera video into reliable performance metrics with no instrumentation.

---


### 237. [Trusted Model Environment for Private Semantic Computations](https://arxiv.org/abs/2609.30032)

**<font color=#1a73e8>作者：</font>** Vasisht Duddu, Xi He  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A private semantic computation primitive enables parties to privately compute over structured and unstructured data that requires understanding its semantics, context, and relationships. Standard cryptographic primitives (e.g., multiparty computation) do not readily support such computation. Generative models are well suited for such tasks but typically process data in plaintext, while cryptographic private inference remains inefficient and difficult to scale. Thus, we need a new primitive for private semantic computation. We introduce trusted model environments (TME), the first such primitive that executes generative models inside trusted execution environments (TEEs) while controlling output leakage. TME is designed to be (i) effective (correctly performs the semantic task); (ii) confidential (protects computation and sensitive inputs); (iii) utility-preserving (retains utility on other tasks); (iv) verifiable (provides tamper-resistant evidence of the computations); (v) efficient (incurs low overhead compared to baseline model computations); and (vi) scalable (supports multiple participating parties). Effectiveness follows from the generative models, while TEEs provide confidential computation. For confidentiality of sensitive inputs, we combine adversarial training to resist verbatim leakage with an information flow control module to suppress semantic leakage. For verifiability, we introduce novel attestations that let parties verify TME operations on their data and queries, along with optimizations (e.g., batching) for efficiency and scalability. We design and evaluate the proof-of-concept for TME across three applications, showing that it meets all the requirements.

---


### 238. [Aim Short to Reach Far: Your Frozen World Model Can Plan Better Than You Think](https://arxiv.org/abs/2609.30036)

**<font color=#1a73e8>作者：</font>** Xvyuan Liu, Jianjie Fang, Chen Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Planners built on visual world models commonly score each predicted outcome by its distance to the encoded goal image. We show that this target can limit control even with exact dynamics and globally optimal short-horizon search: reaching a goal may require actions that initially move away from it. With frozen LeWM models, intermediate targets substantially improve action synthesis and recorded-action ranking on Cube, PushT, Reacher, and TwoRoom. Learned targets and targets drawn from observed experience both produce these gains. We introduce Anchored Planning, which retrieves a recorded segment whose start and end resemble the current and goal observations, then aims at an observation shortly after its start. The frozen model scores actions toward this target from the current state. Without additional training, planning toward observed targets outperforms the released LeWM planner on every task in our long-range evaluation. Additional final-goal search falls short of the same gains. Lower successor-prediction error need not translate into better control. Success also depends on how far ahead the target is placed and on shrinking the retrieval span as execution advances. Changing only the target lets the same frozen model and planner reach goals that final-goal scoring misses.

---


### 239. [AERIAL: Adversarial Evaluation of Robustness in Accuracy-Preserving Low-Precision EEG Decoders](https://arxiv.org/abs/2609.30037)

**<font color=#1a73e8>作者：</font>** Saim Rehman, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deployment-oriented compression is attractive for resource-constrained brain--computer interfaces (BCIs), but whether it changes adversarial vulnerability remains unclear. On BCI Competition IV-2a, we compare 32-bit floating-point (FP32) EEGNet and ShallowConvNet models with global magnitude pruning and simulated INT8 post training quantization (PTQ) and quantization-aware training (QAT) across nine subjects and three seeds. Simulation provides differentiable quantize--dequantize models for white-box attacks and gradient analysis, while native TensorRT deployment is used for validation. Accuracy-preserving compression does not improve direct robustness: at $\epsilon=0.005$, EEGNet PGD accuracy remains 22--24\% across FP32, 50\% pruning (P50), PTQ, and QAT. However, P50 reduces bidirectional transfer efficiency to 0.963/0.928 (FP32$\rightarrow$P50/P50$\rightarrow$FP32), versus 0.994/0.997 for PTQ; the same trend holds for ShallowConvNet. Gradient alignment shows a corresponding separation, while native PTQ agrees with simulated clean/adversarial predictions in 95--98\% of cases. These results show that direct robustness, adversarial transfer, and deployment efficiency are distinct properties of compressed EEG decoders.

---


### 240. [ConPro: Contrast Projection Pretraining for Label-Efficient Vessel Segmentation in DSA Sequences](https://arxiv.org/abs/2609.30043)

**<font color=#1a73e8>作者：</font>** Xinge Guo, Yuanhao Wang, Liqi Shu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense vessel annotation in digital subtraction angiography (DSA) is labor-intensive, yet every unlabeled sequence records how contrast passes through the vessels. Semi-supervised methods take their targets from the current model, and generic self-supervised pretexts reconstruct static appearance, so this signal goes unused. We propose ConPro, a self-supervised pretraining scheme whose target is a contrast projection, the normalized drop of every pixel below its temporal median over the sequence. On DIAS and DSCA, with 10%, 20% and 50% of the training cases labeled, ConPro improves on training from scratch at every label fraction and is the best of the compared methods on DSCA at 20% and 50% labels. Controlled comparisons show that the gain comes from the target. A temporal-median target with the same input, loss and budget stays at scratch level, and using the projection directly instead of learning it, as an input channel or a pseudo-label, helps little or hurts. ConPro provides pretrained weights without changing the segmentation architecture, so it combines with semi-supervised training, and UniMatch, the strongest baseline, gains 0.5 to 2.0 Dice and 0.9 to 2.3 clDice at every label fraction when started from ConPro weights, reaching 75.4 Dice on DIAS and 81.3 on DSCA.

---


### 241. [NNV3: Expanding Neural Network Verification to New Architectures and Domains](https://arxiv.org/abs/2609.30050)

**<font color=#1a73e8>作者：</font>** Anne M. Tumlin, Samuel Sasaki, Ben Wooding 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present NNV3, the latest version of the Neural Network Verification (NNV) tool, a MATLAB framework for formal verification of deep learning models and learning-enabled cyber-physical systems. Building on the set-based reachability foundation of NNV 1.0 (FFNNs, CNNs, NNCS) and NNV 2.0 (RNNs, SSNNs, neural ODEs), NNV3 introduces new members of the Star-set family: ModelStar for verifying networks under weight perturbation, VolumeStar for video and 3D volumetric inputs, and GraphStar for graph neural networks. A conformal-inference-based probabilistic reachability mode complements sound analysis for problems where deterministic verification is intractable, while FairNNV certifies counterfactual and individual fairness properties over continuous input regions. NNV3 introduces new benchmarks for malware detection, graph-based power-system models, medical imaging, variable-length time series data, and action recognition. NNV3 also incorporates tutorials and developer guides through a unified documentation site. This paper details these major updates, demonstrating NNV's maturation into a comprehensive, robust, and accessible verification tool for a diverse range of AI systems.

---


### 242. [A Data-Driven Analysis of Infostealer Malware Victims](https://arxiv.org/abs/2609.30070)

**<font color=#1a73e8>作者：</font>** Arttu Paju, Juha Nurmi, David Arroyo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Infostealer malware infects devices worldwide and harvests their most sensitive contents: credentials, browser sessions, private keys, and access certificates. Yet its impact on victims remains difficult to study without an ethical, legal, and curated research dataset. To close this gap, we build a privacy-preserving pipeline that turns illicitly sourced infostealer logs into a reproducible research artifact, minimizing sensitive data while preserving measurement utility, and use it to construct a dataset of 170,298 victims from logs of multiple infostealer families. Analyzing these victims, we find that the most compromised services mirror the world's most popular platforms, with gaming and entertainment services strongly overrepresented. Within the sample we identify compromised credentials for high-value organizations, including law-enforcement domains, government and military services, and all eight Ivy League universities, as well as substantial exposure of security-critical infrastructure and of financial, remote-access, and development platforms. Victims also show widespread credential reuse and significant revictimization risk, overlapping with phishing and ransomware victim populations. We release the first anonymized victim-level infostealer dataset under controlled access to enable ethical, privacy-preserving, and reproducible research on information security and victim behavior.

---


### 243. [A Native-Reference Phone-Class Geometry for Second-Language Pronunciation Analysis](https://arxiv.org/abs/2609.30075)

**<font color=#1a73e8>作者：</font>** Tina Raissi, Nhan Phan, Chenxiao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speaking assessment systems can provide holistic proficiency scores, but often lack interpretable measures that characterize pronunciation quality. We propose a native-reference phone-class geometry for measuring second language (L2) pronunciation deviation without requiring pronunciation labels, read-aloud prompts, or matched recordings of the same text from native and L2 speakers. Given a native speech corpus, we average frame-level self-supervised representations for each context-dependent phone-class and use singular value decomposition (SVD) to derive a compact native-reference coordinate system. For each L2 utterance, we compute the corresponding averages and project them into the native-reference space. We then demonstrate that the distances between L2 and native-reference coordinates for matched phone-classes show consistent negative correlations with holistic speaking proficiency on the Dev subset of the Speak and Improve Corpus 2025 (Spearman's $\rho\!=\!-0.53$) and with pronunciation quality on the learner subset of the English Read by Japanese Students dataset ($\rho\!=\!-0.34$). These findings suggest that the proposed geometry captures acoustic-phonetic information relevant for proficiency rating while remaining applicable to spontaneous L2 speech without matched native recordings.

---


### 244. [Beyond Driving: Envisioning Activities in Future Autonomous Vehicles through Experience-Centered Design](https://arxiv.org/abs/2609.30076)

**<font color=#1a73e8>作者：</font>** Keqi Chen, Xiao Xue, Xinyi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles (AVs) are poised to fundamentally alter personal transportation, offering occupants the freedom to engage in various non-driving-related activities (NDRAs). However, our current understanding of how people might actually use this time in fully autonomous vehicles (FAVs) is limited. Traditional research methods often struggle to capture the influence of diverse travel circumstances and purposes when exploring future scenarios. This paper introduces experience-centered design (ECD) as an approach to investigate potential NDRAs within FAVs by examining the intricate connections between individuals' daily routines, specific travel contexts, and the activities they might undertake in transit. Through a multi-phase study employing participatory techniques that facilitated narrative construction and exploration, including diary studies, scenario scripting, and mixed reality (MR) enactments, we enabled participants to ground speculative future scenarios in their own lived experiences. This process yielded nuanced insights into preferences and behaviors concerning potential NDRAs, alongside the underlying subjective meanings and sociotechnical considerations. Our findings lead us to conceptualize NDRAs not as isolated instances of "travel time use," but as dynamic sequences of interrelated activities deeply shaped by pre- and post-journey contexts. The effectiveness of our ECD approach in bridging current lived experiences with future scenarios was crucial for uncovering these insights. Ultimately, this study reconceptualizes AVs as complex sociotechnical systems that actively mediate human activity and interaction, suggesting a fundamental shift in their role within the urban fabric.

---


### 245. [Reachability-Based Formal Verification of Graph Neural Networks with Node and Edge Features](https://arxiv.org/abs/2609.30079)

**<font color=#1a73e8>作者：</font>** Anne M. Tumlin, Ben Wooding, Zhenxuan Shao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) have become a prominent approach for developing fast, topology-aware surrogates in electric power systems, supporting tasks such as power flow (PF) analysis, optimal power flow (OPF) estimation, and cascading failure analysis (CFA). Despite this growing use, formally verifying GNN-based models remains challenging, with existing methods limited in scope. We extend the neural network verification (NNV) framework to graph-structured inputs through GraphStar sets, a generalization of Star sets that captures uncertainty over both node and edge features. This extension enables the propagation of linear message-passing operations and the sound approximation of ReLU nonlinearities for GNN architectures, including graph convolutional network (GCN) and graph isomorphism network with edge features (GINE) layers. We evaluate GNNV across three power system tasks, PF, OPF, and CFA, on the IEEE-24, IEEE-39, and IEEE-118 test cases, as well as two standard graph classification benchmarks, ENZYMES and PROTEINS. Our results show that GNNV provides tighter robustness guarantees than CORA on graph classification models with ReLU-based activations and, for the first time, delivers edge-aware robustness guarantees for GINE-based PF and OPF models under joint node and edge perturbations.

---


### 246. [Residual Correlation as a Diagnostic for Joint-Uncertainty Gains from GP Coregionalisation](https://arxiv.org/abs/2609.30085)

**<font color=#1a73e8>作者：</font>** Fangqin Zhou, Joaquin Vanschoren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multi-target regression, correlated targets are often coupled through multi-output Gaussian processes with an intrinsic model of coregionalisation (GP-ICM), assuming that sharing statistical strength improves overall performance. In practice, the benefits are inconsistent. Across the settings studied, we find that the main benefit of coregionalisation is joint uncertainty quantification rather than point prediction. Raw target correlation does not predict when coupling helps; in the separable GP-ICM settings studied here, residual correlation, the cross-target dependence left unexplained by independent per-target predictors, is the strongest predictor of joint-uncertainty gains.
We introduce a lightweight diagnostic, $D_{\rm logdet}=-\frac{1}{2}\log\det R_{\rm res}$, which represents the idealised joint negative log-likelihood (NLL) gain from modelling a full rather than diagonal residual covariance and is computable from independent GPs alone. Across a controlled synthetic study, 16 multi-target benchmarks, and frozen transformer and convolutional neural network representations for keypoint regression, point prediction remains largely unchanged ($\Delta R^2\approx 0$). In contrast, $D_{\rm logdet}$ strongly predicts observed ICM NLL improvements ($\rho_s=-0.83$, $p<0.001$), outperforming heuristics such as the feature-to-sample ratio. We also propose Residual-ICM, which preserves independent marginal variances while adding residual-correlation structure to the joint covariance. Residual-ICM achieves the best average joint NLL among the compared methods, while the diagnostic indicates when covariance coupling is likely to be useful. The diagnostic is specific to global Gaussian residual dependence, the structure captured by separable coregionalisation.

---


### 247. [AT-SKM-Net: An Accelerated Trainable Sampling Kaczmarz-Motzkin Framework for Linear Hard-Constraint Feasibility on Dynamic Graphs](https://arxiv.org/abs/2609.30088)

**<font color=#1a73e8>作者：</font>** Xiaochen Zhang, Haoyu Zhu, Yao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-structured optimization with linear constraints is fundamental to critical infrastructure but faces scalability limits due to massive strict hard constraints and high dimensionality. While recent projection-based methods such as Trainable Sampling Kaczmarz-Motzkin Net (T-SKM-Net) guarantee feasibility, they face high computational costs in dynamic environments by processing the entire constraint set and requiring expensive matrix factorizations. To bridge this gap, we propose the Accelerated Trainable-SKM (AT-SKM) Net framework. To concentrate computation on the active constraints and eliminate redundant calculations, we introduce a hybrid sampling strategy guided by a topology-aware heterogeneous GNN model. To efficiently handle topological shifts in graph-based constraints, we employ a Cholesky Update mechanism that theoretically reduces the equality projection complexity from O(N^3) to O(N^2) under low-rank perturbations. Experiments on random geometric graphs, N-1 Security-Constrained DC-OPF, and minimum-cost gas transport problem demonstrate that AT-SKM reduces iteration counts by up to 85% and achieves 2.95x-7.29x SKM layer speedups, while maintaining zero constraint violations.

---


### 248. [Accelerating Video Diffusion via Training-Free Trajectory Routing](https://arxiv.org/abs/2609.30096)

**<font color=#1a73e8>作者：</font>** Mustafa Munir, Huy Vu, Shreyas Misra 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion is computationally expensive, as it requires executing a large model across many denoising steps. Even with step-distillation, inference remains expensive because every distilled step still requires a costly model evaluation. We present TRACK: TRajectory-Aware Capacity routing via top-K selection, a heterogeneous denoising strategy that switches between compatible large and small models at selected steps, reducing the average cost per denoising evaluation. The switching steps are determined using a calibration process. TRACK first rolls out a reference trajectory with the large model. Then at each step, the small model's prediction is also collected and compared against the large model's prediction to obtain a relative disagreement score. Both models receive the same latent, timestep, conditioning, and guidance inputs. Aggregating this signal over a calibration set produces a disagreement score map across diffusion steps, which determines a switching policy for an efficient inference process: quality-sensitive steps keep using the large model, while steps with low disagreement scores are routed to the small model. Inference executes only the selected model at each step, requiring no retraining, architecture or scheduler changes, or online dual-model evaluation. Across Wan 2.1, Cosmos 3, TurboDiffusion, and FastVideo, TRACK yields $1.95\times$, $2.04\times$-$2.73\times$, $2.69\times$, and $2.17\times$ speedups, respectively, with comparable aggregate quality and high diversity retention. TRACK thereby establishes automated, training-free model switching as a practical acceleration paradigm for video diffusion.

---


### 249. [On the SoS Certifiability of Log-Concave Distributions](https://arxiv.org/abs/2609.30105)

**<font color=#1a73e8>作者：</font>** Aleksandr Storozhenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For an arbitrary isotropic log-concave distribution $P$ on $\mathbb{R}^d$, we prove that the polynomial $(Cm)^m\|v\|_2^m - \mathbb{E}_{X\sim P}\langle X,v\rangle^m$ is a sum of squares for every even $m\ge2$, where $C>0$ is a universal constant. This removes the dependence on the Poincaré constant in the theorem of Kothari and Steinhardt (arXiv:1711.07465), recovering the optimal moment bounds for log-concave distributions. As an immediate corollary, we obtain computationally efficient algorithms with dimension-free error guarantees for a wide range of high-dimensional statistical estimation problems.
Our proof uses stochastic localization to decompose $P$ as an average of random strongly log-concave measures, whose centered moments admit the subgaussian certificates of Diakonikolas, Hopkins, Pensia, and Tiegel (STOC 2025; arXiv:2410.21194). With a covariance-adapted choice of localization, we show that a fourth-moment certificate derived from Letwin's variance inequality for quadratic forms (arXiv:2607.24164) suffices to control this averaging at every even degree.

---


### 250. [Smartphone-Based Method for Automated Speed Enforcement](https://arxiv.org/abs/2609.30107)

**<font color=#1a73e8>作者：</font>** Keya Li, Jahnavi Malagavalli, Lamha Goel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Smartphone cameras and computer vision (CV) hold significant promise in assisting public agencies with enforcing traffic laws and enhancing road safety. This work designs and tests a smartphone-based method for automated speed estimation and vehicle identification (license plate, make/model, and color recognition) via an automated pipeline to assist enforcement agencies in reliably identifying speeders. The CV code accurately recognizes nearly half (46%) of the license plates' text on 1,800 images from a Brazil open-source dataset, called UFPR-ALPR. Code tests on daytime recordings from hand-held smartphone videos (n = 73) and roadside cameras (n = 42) in Austin, Texas yield 60.8% accuracy for color detection (among all possible RGB color categories), 48.6% on vehicle make/manufacturer identification, and 16.89% on vehicle make and model identification. Prediction accuracy for speed estimation (within a 20% range), vehicle make (within the top 3 predictions), and license plate recognition (within the top 10 predictions) are 16.3%, 16.9%, and 29.7%, respectively. This paper also illuminates the legal, technological, and practical aspects of using smartphones for enforcement, including the potential use of recordings for enforcement purposes, emphasizing the need to transform the potential of smartphone-based CV technologies into practical tools for vital information on traffic violations.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
