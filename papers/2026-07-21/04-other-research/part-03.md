# 📦 其他研究 | 2026年07月21日

> 本类共 **152** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-152](./part-04.md)

---

### 101. [How Much Human Label Variation Does Formal Semantic Structure Explain?: Group-Level Effects and Item-Level Ceilings in NLI](https://arxiv.org/abs/2607.15870)

**<font color=#1a73e8>作者：</font>** Haram Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human label variation in natural language inference is increasingly treated as signal rather than noise, but how much of it formal semantic structure explains has not been measured directly. We measure it on the 3,113 SNLI and MNLI items of ChaosNLI, using a rule-based operator and monotonicity tagger validated against MED (0.883 agreement at the edit site, 0.807 on the sentence-level summary our analyses consume), three preregistered analysis blocks, and full reporting of negative results. Three bounds emerge. First, a group-level boundary: hypotheses that are not purely upward monotone show reliably higher label entropy (Cliff's delta = -0.284), and rank-based tests defend the effect against operator-presence and length reductions, though a bounded-outcome sensitivity check weakens the regression form of the length defense. Second, an item-level ceiling: the same formal profiles explain only 3.3 to 3.6 percent of entropy variance and reach a median-split AUC of 0.606, too weak to identify high-disagreement items. Third, composition invariance: across the boundary, three high-powered preregistered contrasts on validated error shares and explanation-type shares (VariErr, LiTEx) all return null results. In this sample, formal semantic structure shifts how much annotators disagree by a small amount and does not detectably change what they disagree about. ChaosNLI-S/M consists of items selected for low original agreement, and every claim is conditioned on that scope. All analyses were preregistered in a version-controlled research log, whose audit trail, including one corrected interpretation rule, the paper discloses.

---


### 102. [DECODEM: Data Extraction from Corporate Organizational Documents via Enhanced Methods](https://arxiv.org/abs/2607.15879)

**<font color=#1a73e8>作者：</font>** Jens Frankenreiter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Much empirical legal research depends on translating unstructured text into structured variables. In corporate governance research as elsewhere, this translation has traditionally relied on human coding of documents such as charters and bylaws, a process that is costly, difficult to scale, and often opaque. This paper introduces DECODEM, a set of benchmark datasets for evaluating the automated extraction of corporate governance variables from organizational documents. The benchmarks pair randomly sampled corporate charters and bylaws with high-quality human annotations covering a range of governance provisions commonly studied in empirical work.
Using these datasets, the paper evaluates several large-language-model extraction pipelines that vary in prompt design, task decomposition, and document handling. The underlying task consists of a set of document-level binary classification problems, one for each governance variable. The results show that automated extraction is feasible at a high level of accuracy for many provisions, with median performance near the upper bound across approaches. At the same time, performance varies systematically across variables, with a small number of provisions accounting for most of the remaining errors. More elaborate prompting strategies and cascading pipelines do not consistently improve performance for frontier models, but substantially narrow the gap between frontier and efficiency-oriented models in some settings, suggesting that pipeline design can partly substitute for model capability.
By providing a standardized benchmark and a systematic evaluation of extraction methods, the paper demonstrates that current frontier models can extract legally meaningful information from complex corporate documents with high accuracy and suggests an important future role for automated feature extraction in constructing corporate governance datasets.

---


### 103. [Perceived AGI: Believability as Dimensional Completeness, Not Capability](https://arxiv.org/abs/2607.15883)

**<font color=#1a73e8>作者：</font>** Sebastian Cochinescu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are broadly capable, yet in sustained one-to-one conversation they still read as flat: competent, responsive, and somehow not quite the presence of a mind. We hypothesize that a central missing ingredient is not more capability but dimensional completeness. We propose that the believability of an artificial interlocutor -- the degree to which a user attributes an inner life to it, which we call perceived mind -- is governed by whether the agent expresses a small set of first-person stances that humans use as evidence of mind, and that this is separable from task intelligence. We name four such dimensions -- time, truth, entropy, and love -- each defined as a behavioral stance rather than a benchmark competency, each with a human analog and a concrete emulation path; the time dimension already has an author-reported prototype. We identify an observable behavior layer -- initiative (unprompted action) and cadence (the shape and timing of turns) -- through which the stances surface in conversation, both partially realized as deployed features in a production companion application. We state six falsifiable predictions that a later pre-registered study will test, separating those that are pre-registrable now from those that remain conjectures pending operationalization. This is a conceptual framework: it reports no human-subjects data, and its central comparative claims are predictions, not findings. Throughout we hold a firm boundary -- the object is inferrable interiority, not interiority; this is perception engineering, not a theory of machine consciousness -- and we treat the resulting attachment and manipulation risks as load-bearing rather than incidental.

---


### 104. [MDND: Unsupervised Learning Guided by Non-Differentiable Refinement for Shape Correspondence](https://arxiv.org/abs/2607.15887)

**<font color=#1a73e8>作者：</font>** Qinsong Li, Jing Meng, Haibo Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep functional map frameworks (DFM) for shape correspondence are powerful, yet fundamentally limited by their reliance on end-to-end differentiability. This constraint prevents the integration of highly accurate, non-differentiable refinement techniques, capping their overall performance, especially on challenging non-isometric shapes. To overcome this, we introduce MDND, a novel DFM paradigm built on the principle of merging differentiable and non-differentiable components. Our framework facilitates unsupervised learning guided by an internal, non-differentiable refinement. Specifically, MDND employs a dual-branch architecture: a non-differentiable refinement branch leverages a novel, multiscale iterative solver to produce highly robust correspondences, acting as a refined target. Concurrently, a fully differentiable branch learns to predict correspondences from features. The entire system is trained end-to-end without supervision by enforcing a consistency loss that compels the differentiable branch to learn from the superior, refined results of the non-differentiable branch. Extensive experiments show that MDND sets a new state-of-the-art, demonstrating remarkable robustness on shapes with non-isometric deformations and topological noise.

---


### 105. [Hardware-triggered Time Synchronization of Roadside Multi-lidar, Multi-camera Measurement System for Accurate Data Alignment](https://arxiv.org/abs/2607.15889)

**<font color=#1a73e8>作者：</font>** Shiva Agrawal, Savankumar Bhanderi, Zhiran Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate temporal alignment of heterogeneous sensors is necessary for reliable environment perception in roadside multi-lidar, multi-camera systems, particularly in dense urban traffic. For this purpose, an open-source, simple, modular, and configurable hardware-triggered time-synchronization circuit is presented in this work to perform temporal alignment or accurate time synchronization between a lidar and multiple cameras. In the designed circuit, a lidar synchronization pulse is used as a reference input, and independently programmable, time-delayed trigger pulses are generated for each camera, allowing flexible adaptation to varying sensor setups and mounting geometries. A series of experiments is conducted on a roadside-mounted perception system comprised of lidar and three cameras, in which the trigger delay is systematically varied, and its impact on spatial-temporal alignment is evaluated. For different classes of road users, the overlap between lidar point cloud measurements and camera measurements is quantified to identify delay configurations that maximize cross-sensor consistency. The proposed circuit is shown to achieve robust and repeatable synchronization while remaining straightforward to deploy, reconfigure, and extend due to its simple and open-source design. Following validation on a three-camera roadside system, the circuit is extended to a vehicle platform with seven cameras and a lidar, providing a low-cost, extensible solution for multi-sensor synchronization across infrastructure and vehicle setups. All hardware circuit design files and source codes are available at this https URL.

---


### 106. [A Semiparametric Framework for Stochastic Fundamental Diagram Modeling](https://arxiv.org/abs/2607.15907)

**<font color=#1a73e8>作者：</font>** Pengnan Chi, Xiaoliang Ma, Magnus Jansson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The stochastic fundamental diagram (SFD) provides a probabilistic description of the relationship between traffic density and flow or speed, enabling uncertainty-aware traffic modeling. However, existing stochastic models frequently struggle to accommodate rigorous physical constraints while retaining sufficient flexibility to capture complex nonlinear patterns. To address this, we propose a novel semiparametric SFD modeling framework by leveraging specially designed functional forms. These functions intrinsically satisfy physical constraints defined on the moments of the conditional flow distribution given traffic density while incorporating neural-network-based structures to capture complex empirical patterns. We derive a system of moment-matching equations to convert physical constraints into the parameterization of the conditional distribution, proving that a unique solution exists for the location-scale family of distributions, thereby guaranteeing model well-posedness. Furthermore, we demonstrate that the framework can be extended to non-location-scale distributions, including those requiring additional boundary constraints. Empirical evaluations on a real-world dataset reveal that our approach consistently outperforms representative baselines, delivering superior probabilistic accuracy and robust uncertainty quantification, particularly in congested regimes. Overall, the proposed framework provides a theoretically grounded and flexible foundation for stochastic traffic flow modeling.

---


### 107. [(MPO)$^2$: Multivariate Polynomial Optimization based on Matrix Product Operators](https://arxiv.org/abs/2607.15916)

**<font color=#1a73e8>作者：</font>** Niccolò Ciolli, Anders Vestergaard Nørskov, Michael Kastoryano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Central to machine learning and signal processing is the ability to perform universal function approximation and learn complex input-output relationships from limited numbers of observations. Multivariate polynomial models offer a natural way to express such relationships through multiplicative feature interactions, but their coefficient tensors grow exponentially in size with the polynomial degree. Existing tensorized polynomial models reduce this cost, yet canonical polyadic decompositions have rank-limited expressivity, and tensor train formulations are feature order dependent. We introduce Multivariate Polynomial Optimization based on Matrix Product Operators (MPO)$^2$, a framework that combines learned MPO feature embeddings with compact polynomial weight tensors. This yields feature order independent polynomial representations that can incorporate structured operators such as projections, convolutions, and masks for weight tensor symmetries. Across regression and classification benchmarks, (MPO)$^2$ improves over existing tensor decomposition based polynomial models and provides a flexible alternative for efficient polynomial function approximation.

---


### 108. [On the Failure of Boundary-Seeking Distillation in Bottlenecked Generative Architectures](https://arxiv.org/abs/2607.15919)

**<font color=#1a73e8>作者：</font>** Mohamed Amine Kina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-free knowledge distillation transfers the knowledge encoded in a teacher model to a student model without access to the original training data. Prior work such as Contrastive Abductive Knowledge Extraction (CAKE) achieves this for classifiers by synthesizing samples near the teacher's decision boundary. In this work, we investigate whether this boundary-seeking principle extends to autoencoder distillation through experiments on the MNIST dataset . To enable a direct comparison, we reformulate continuous reconstruction as a dense, per-feature classification task, allowing the decoder to output categorical logits. We show that boundary-seeking objectives are fundamentally ill-posed in bottlenecked generative architectures. CAKE operates on a single, instance-level objective, but a decoder acts as an array of tightly coupled, feature-level classifiers constrained by a shared low-dimensional bottleneck. Independently sampling contrastive targets for these coupled outputs violates the geometry of the learned latent manifold and produces severe gradient conflicts instead of informative boundary samples. Manifold-aware synthesis bypasses these conflicts entirely and establishes an effective baseline for data-free generative distillation.

---


### 109. [Distributional Matching for Vector Quantization: A Unified Theoretical and Empirical Framework](https://arxiv.org/abs/2607.15933)

**<font color=#1a73e8>作者：</font>** Xianghong Fang, Litao Guo, Hengchao Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The effectiveness of modern visual representation learning and autoregressive models critically depends on vector quantization (VQ), which discretizes continuous feature representations using a learnable codebook. Despite its widespread use, existing VQ methods often suffer from training instability and codebook collapse, arising from gradient mismatch induced by the straight-through estimator and the under-utilization of code vectors. In this work, we show that both issues can be traced to a fundamental mismatch between the distributions of feature vectors and code vectors, leading to inefficient representation and information loss. Building on this observation, we propose a distributional matching framework for vector quantization. We introduce principled criteria for desirable VQ behavior and demonstrate through theoretical analysis and empirical evaluation that aligning feature and code vector distributions provides a unifying mechanism for mitigating training instability and codebook collapse. We instantiate this framework using a Wasserstein-based objective with an efficient closed-form under a mild Gaussian approximation, and further show that a nonparametric alternative based on maximum mean discrepancy yields comparable performance. Extensive experiments on visual tokenization benchmarks support the effectiveness and robustness of the proposed approach.

---


### 110. [Handwritten and Printed Text Segmentation via Region-Aware Human-Writing Descriptor Engineering](https://arxiv.org/abs/2607.15936)

**<font color=#1a73e8>作者：</font>** Zhixian Lu, Jianwei Zhang, Lei Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the increasing demand for reusing paper documents in educational and office settings, accurate segmentation of handwritten and printed text has become a crucial step in document digitization. Although numerous deep learning models have been developed for this task, their high computational cost limits deployment on resource-constrained edge devices. To address this challenge, we present a lightweight framework optimized for efficient performance on devices with severely limited computational capacity. Our approach begins with the Sentence-level Connected Component Segmentation algorithm, aimed at extracting coherent sentence-level segments from document images. We then design a novel Region-aware Handwriting Descriptor (RHD) to capture the intrinsic variability of human handwriting at the sentence level. A simple conventional classifier can then be seamlessly integrated with our designed descriptor, demonstrating strong classification performance for distinguishing handwritten and printed sentence-level text images, highlighting that the proposed descriptor is agnostic to the choice of classifier. Extensive experiments are performed on our self-constructed Multilingual High-Quality Annotated Dataset for Handwritten and Printed Text Segmentation (MAD-HPTS) and a public benchmark PHD-AS, and the experimental results demonstrate that the proposed framework outperforms current state-of-the-art methods in both accuracy and computational efficiency. On MAD-HPTS, our method sacrifices only 1.4% accuracy compared to the leading deep neural network baseline, yet achieves more than 8 times speedup in inference, making it well-suited for lightweight deployment.

---


### 111. [More with Less: a Large Scale Remote Sensing VLM with a Simple Recipe](https://arxiv.org/abs/2607.15942)

**<font color=#1a73e8>作者：</font>** Stefan Maria Ailuro, Mario Markov, Mohammad Mahdi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing vision-language models are increasingly expected to support open-ended reasoning over Earth Observation data and a variety of tasks. Most recent progress in this area has been driven by remote-sensing-specific architectural designs, often introducing new encoders, alignment modules, or task-specific fusion mechanisms. In this work, we challenge the necessity of such architectural specialization. We show that a generally capable vision-language model can achieve competitive or state-of-the-art performance at challenging remote sensing benchmarks, provided that it is trained at sufficient scale across diverse data and tasks. Our model uses a single language policy that can either answer directly in text or invoke a localization tool for segmentation and grounding. To train this heterogeneous behaviour, we employ a multi-task reinforcement learning framework with adaptive task rewards covering multiple-choice VQA, free-form VQA, captioning, detection, and segmentation across a large variety of input types. Our approach achieves competitive results across a broad set of benchmarks, including high-resolution, multi-temporal, multi-modal and multi-view tasks. Further, as training data scales, our experiments show consistent improvements across most tasks both in and out of distribution, which correlate with per-task data diversity. These findings suggest that, for remote sensing VLMs, data scale is more important than architectural novelty.

---


### 112. [When Not to Automate: A Formal Protocol for Human Preservation in AI-Optimized Organizations](https://arxiv.org/abs/2607.15944)

**<font color=#1a73e8>作者：</font>** Jose Manuel de la Chica Rodriguez, Jairo Rodriguez Arias, Spyridon Chouliaras  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Standard automation ROI misses four categories of systemic risk -- tacit knowledge erosion, resilience reduction, regulatory exposure, and socio-institutional capital degradation -- that affect long-term organizational performance. PHP-AIO (Protocol for Human Preservation in AI-Optimized Organizations) is a five-gate sequential decision protocol with a final composite check that quantifies these unpriced systemic risks at the role level and produces auditable automation decisions. A closed-form automation-debt measure ($\rho(P)$) formalises how role-level decisions accumulate across multi-step processes; its warning is neutralised only by a regulator-mandated human-in-the-loop anchor. Applied to stylised profiles of representative internal roles, PHP-AIO produces distinct outcomes -- automate, augment, hybrid, and preserve -- for candidates that standard cost-benefit analysis would uniformly automate. Threshold sensitivity analysis confirms the gate decisions are robust to upward perturbations of at least 14% in three of four representative cases.
Keywords: AI governance, automation decision, human oversight, tacit knowledge, organizational resilience, financial services

---


### 113. [Code-Poisoning Property Inference Attacks](https://arxiv.org/abs/2607.15970)

**<font color=#1a73e8>作者：</font>** Xukun Luan, Yuhui Gong, Gang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The flourishing code hosting platforms and coding agents enable even beginners with private data to build tailored Machine Learning (ML) models using available code quickly. The training data for ML models, often regarded as private property (e.g., clinical records, transaction information), is at significant risk of information leakage. Property Inference Attacks (PIAs), as a significant type of privacy attack, aim to expose global property information of the training set. In this paper, we present Code-Poisoning Property Inference Attack (CPPIA), the first code-level PIA, which overcomes four limitations of existing works: insufficient attack performance, severe degradation of model accuracy, high computational overhead, and failure under defenses. We consider malicious code providers from code hosting platforms (GitHub) and coding agents (Codex). Upon downloading the poisoned code, data holders train models with their private data without professional auditing, subsequently releasing label-only APIs to the public. The adversary embeds the properties into secret samples during training and queries the trained model on these samples later to leak privacy. CPPIA offers 100\% attack accuracy without degrading model accuracy. It is also computationally lightweight and requires no shadow models. We evaluate the attack performance across four datasets, eight model architectures, eighteen properties, and under three defense mechanisms, demonstrating the universality and effectiveness of CPPIA.

---


### 114. [An Exploratory Study of Single Channel Surface Electromyography for Hand Gesture Classification](https://arxiv.org/abs/2607.15972)

**<font color=#1a73e8>作者：</font>** Daanish Hindustani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate hand gesture recognition using surface electromyography (sEMG) typically relies on multichannel sensor arrays and computationally intensive models. This limits practical deployment in low-power and embedded systems. This study investigates the feasibility of classifying ten hand gestures using a single sEMG channel combined with lightweight machine learning architectures. Raw sEMG signals were transformed into a comprehensive feature-based representation, including time-domain, frequency-domain, higher-order-crossing, and relative-intensity features. Feature redundancy was reduced using Pearson correlation filtering and the removal of highly correlated features, while dimensionality-reduction techniques (LDA and PCA) were applied selectively. Three classifiers, a feed-forward neural network (NN), k-nearest neighbors (KNN), and a support vector machine (SVM), were systematically evaluated across four experiments. Results demonstrate that combining time and frequency features with Pearson filtering and a compact NN can achieve up to 90 percent accuracy, even with limited temporal and spatial information. These findings highlight the potential of single-channel sEMG systems for cost-effective, low-power gesture-recognition applications.

---


### 115. [DebrisTracer: Reliable Tracking in Hypervelocity Impact Fast Imaging](https://arxiv.org/abs/2607.15986)

**<font color=#1a73e8>作者：</font>** Théophane Loloum, Fabien Vivodtzev, David Hébert 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This application paper presents DebrisTracer, a framework for the reliable tracking of debris in hypervelocity impact fast imaging. These noisy and highly specific datasets capture the ejection of a large number of debris fragments after the impact of a projectile launched at hypervelocity into a target material. The reliable estimation of debris mass and speed distributions is of major importance in aerospace applications. We document how to extend an off-the-shelf topology tracking framework based on critical point extraction and matching, in order to incorporate domain knowledge and physical assumptions. Our approach automatically produces an accurate and reliable debris tracking, enabling an interpretable visual analysis of this complex space-time phenomenon. Extensive experiments demonstrate the accuracy improvements provided by our approach over established tools used by domain experts in terms of physical validation, specifically via the prediction of the experimental ejected mass and crater depth profiles. We illustrate the utility of our approach across several use cases (with varying impact angles and physics). We show that our statistical summaries enable the visual identification of distinct regimes within the debris population, corroborating and refining prior expectations of domain experts. Our database and our C++ implementation are available at this address: this https URL.

---


### 116. [A Formally Grounded ODRL Evaluator: Implementation and Comparison](https://arxiv.org/abs/2607.15987)

**<font color=#1a73e8>作者：</font>** Jaime Osvaldo Salas, Paolo Pareti, Adeel Aslam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The ODRL policy language is emerging as the de-facto standard for policy modelling data access and usage preferences, AI governance policies and data workflows in European dataspaces. The current standard has no mathematical formal semantics to describe how a system should implement policy evaluation. This has resulted in a variety of systems and tools that implement their own interpretation of the language, which limits interoperability and cannot guarantee consistent results. Based on an existing semantic model of ODRL, we formalise the problems of ODRL evaluation for the access control and monitoring scenarios, in both static and streaming settings, and we provide a novel, efficient algorithm and implementation. We present the first ODRL Evaluator with transparent formal semantics and supporting all rule types. We experimentally measure its performance, analysing different scalability dimensions related to policy complexity and size of the data on which a policy is evaluated. We compare our system with the state-of-the-art by providing a comparative review of existing ODRL evaluators, which highlights the differences in supported ODRL features and evaluation modes.

---


### 117. [Closing the AI Trust Gap: The Case for Independent Certification for Trustworthy AI](https://arxiv.org/abs/2607.15992)

**<font color=#1a73e8>作者：</font>** Trisevgeni Papakonstantinou, Cansu Canca, Farah Nanji 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Over the past decade, responsible AI (RAI) has produced a substantial body of practice for identifying and mitigating the risks AI poses in high-stakes settings. Yet this work has not produced a market that rewards trustworthiness. Firms that invest seriously in safety, fairness, and oversight cannot consistently prove to consumers, regulators, and shareholders that their systems go beyond the bare minimum of compliance. What is missing is a way for society to recognize or compare the difference. The result is a trust gap: a structural condition in which responsible development efforts happen inside organizations but produce no external, independently recognized and verifiable signal of trustworthy outcomes. We argue this gap is sustained in part because of a focus on responsible AI (a matter of internal process) as opposed to trustworthy AI (a matter of independently verifiable real-world outcomes), and that it persists because of three compounding failures: (1) the market cannot distinguish trustworthy systems from their imitations; (2) evaluation targets models and outputs rather than deployed sociotechnical systems and their outcomes; (3) the measurement ecosystem is oriented toward avoiding harm rather than demonstrating benefit. Reviewing existing AI governance instruments and comparing them to certification regimes in healthcare, sustainability, and security, we show that none integrate a governance baseline, independently verified positive-outcome evidence, and market signaling in a single framework. We propose independent, outcome-oriented certification as the connective layer that can close the trust gap, complementing regulation and internal governance by making trustworthiness measurable, comparable, and commercially rewarded.

---


### 118. [CanonicalPhys: Pose-Robust Remote Photoplethysmography via Canonical-Space Priors](https://arxiv.org/abs/2607.15995)

**<font color=#1a73e8>作者：</font>** Hui Wei, Seyedata Jodeiri Seyedian, Xiaobai Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep remote photoplethysmography (rPPG) attains sub-bpm heart-rate error on frontal, stationary faces yet degrades sharply under head pose: on MMPD, the state-of-the-art FactorizePhys backbone's MAE grows $1.60\times$ from frontal ($|\text{yaw}|{<}15^\circ$) to large-yaw ($|\text{yaw}|{\geq}45^\circ$) frames. We argue that pose is a \emph{coordinate-structural} nuisance rather than a data-augmentation problem: in image coordinates the same pixel maps to different anatomy at different poses, blocking three priors otherwise natural for rPPG, namely the dichromatic reflection model, pulse-phase invariance across skin regions, and the POS/CHROM chromaticity projection, each of which presumes a stable anatomy-to-pixel mapping. We introduce \textbf{CanonicalPhys}, which prepends a differentiable four-point homography that fixes four facial anchors at canonical positions; in this canonical frame the three priors become expressible as a per-pixel Lambertian weight, a cross-ROI temporal consistency loss, and knowledge distillation from windowed POS, none of which adds trainable parameters over the backbone. At an identical parameter count, CanonicalPhys reduces MMPD's frontal-to-large-yaw MAE degradation from $1.60\times$ to $1.33\times$ and flattens the mild-yaw bin from $1.32\times$ to $1.07\times$ (across CanonicalPhys variants), with matched cross-dataset MAE reductions of up to $32\%$ on pose-rich targets. Code: this https URL

---


### 119. [Beyond Unfolding: 60x Faster One-Stage Unmixing for Closely-Spaced Infrared Small Targets](https://arxiv.org/abs/2607.16007)

**<font color=#1a73e8>作者：</font>** Ximeng Zhai, Zheng Wang, Yaohong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to the optical diffraction limit and long imaging distances, Closely-Spaced Infrared Small Targets (CSIST) typically exhibit energy overlap, manifesting as indistinguishable blobs in infrared images. This ambiguity invalidates the one-to-one mapping assumption of traditional detection, thereby necessitating a paradigm shift towards CSIST Unmixing, which decomposes these blobs into discrete sub-targets. However, the dominant paradigm deep unfolding networks are shackled by the high latency and structural inflexibility intrinsic to their repetitively iterative architecture. To this end, we propose the Fast One-stage CSIST Unmixing Scheme (FOCUS), a one-stage lightweight paradigm which demonstrates that deep unfolding is not necessary. Motivated by the key observation that image super-resolution (SR) and CSIST Unmixing share an isomorphic degradation model, our insight is that it is possible to achieve a paradigm shift from image SR to CSIST Unmixing via completely transforming the label space, loss functions, and evaluation criteria. Specifically, to avoid entangling geometric recovery with artifact suppression, FOCUS adopts a single pass mapping with an internal coarse-to-fine flow that progressively refines target localization from coarse spatial distributions to finer sub-pixel precision. While sparsity regularization suppresses background clutter, it also attenuates target intensities. To compensate for this attenuation of valid signals, flux conservation is introduced as a competing constraint that restores signal energy back to target centers. To the best of our knowledge, this work is the first attempt to address this task via a lightweight one-stage framework without the DUN paradigm. Experiments demonstrate that our method matches or surpasses the state-of-the-art unfolding approaches in both localization and unmixing accuracy, while boosting the inference speed by 60x.

---


### 120. [AI Watermark Evidence Fails Forensic Readiness: An Empirical Evaluation](https://arxiv.org/abs/2607.16010)

**<font color=#1a73e8>作者：</font>** Saifur Rahman Tamim, Amir Labib Khan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Governments are increasingly mandating that LLM-generated content carry watermarks. The EU AI Act calls for markings that are "sufficiently reliable and robust." California's SB 942 requires disclosure that is "permanent or extraordinarily difficult to remove." Both mandates rest on an untested assumption: that watermark detection yields evidence reliable enough for courts. This paper tests that assumption directly.
We evaluate three representative LLM watermarking methods -- KGW, Unigram, and the MarkLLM implementation of SynthID-Text -- against the Daubert admissibility criteria and the NIST SP 800-86 digital forensic process. To structure this evaluation, we propose a Forensic Readiness Score (FRS) framework with 12 criteria, three mandatory gates, and a 60-point scoring system. We focus on meaning-preserving paraphrase as the attack vector, since it is both legally realistic and difficult to dismiss as evidence tampering.
The results raise serious evidentiary concerns. Out of 846 valid paraphrase runs across 15 diverse prompts per method, every single initially-detected KGW and Unigram text lost its watermark after paraphrasing -- 100% conditional removal. SynthID fared only slightly better at 98.3%. Even before any attack, false-negative rates were already high: 70% for KGW, 83% for Unigram, 80% for SynthID. The SynthID configuration also flagged 5.4% of paraphrased human-written controls as AI-generated and showed an 18.6% paradox rate, with 80% of its own pristine watermarked output landing in the uncertainty deadband. None of the three methods satisfy more than two of five Daubert factors. We also find that the FRS point-based scoring system, despite working as designed, cannot fully capture forensic uselessness -- a limitation worth noting for future framework design.
These configurations, as tested, do not meet the evidentiary bar that courts require.

---


### 121. [DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction](https://arxiv.org/abs/2607.16012)

**<font color=#1a73e8>作者：</font>** Jehun Kang, Jungha Wang, Youngjun Hwang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-Task Learning (MTL) in robotics perception systems supports comprehensive 3D spatial scene understanding by integrating semantic segmentation and depth estimation. While Vision Foundation Models (VFMs) are increasingly adopted as robust feature encoders, existing decoding strategies present a critical bottleneck. To address this, we propose DPNeXt, a streamlined multi-scale feature fusion decoder and efficient alternative to the standard Dense Prediction Transformer (DPT). DPNeXt uses dual depthwise separable inverted bottlenecks to improve frozen VFM utilization through fusion-centric decoding and independent task modularization. To further mitigate negative inductive transfer between tasks, we introduce the Multi-Task Boundary Guidance (MTBG) strategy. Unlike prior boundary-aware methods that add fusion modules or gating, MTBG applies symmetric boundary-focused supervision to encourage geometric consistency without extra annotation or inference cost. Experiments on Cityscapes show that DPNeXt-S outperforms prior state-of-the-art (SOTA) MTL models, while DPNeXt-B further improves the overall performance and achieves the best results among the compared methods. On NYUv2, DPNeXt-B also achieves the best semantic segmentation and depth estimation results among the compared methods while requiring substantially fewer trainable parameters than prior large-scale MTL models. Compared with the standard DPT, DPNeXt-S reduces trainable parameters by 78.6% and achieves the fastest inference speed among the compared models on resource-constrained laptop hardware. The source code, model checkpoints, and a demo video will be made available at this https URL.

---


### 122. [PIXIE: A Zero-Shot texture-invariant 6D pose estimation framework for unseen objects with assembly defects](https://arxiv.org/abs/2607.16015)

**<font color=#1a73e8>作者：</font>** Leon Jungemeyer, Alejandro Magaña, Gautham Mohan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 6D pose estimation remains a key challenge in robotics and computer vision, particularly in industrial environments. The deployment of currently available data-driven methods is often limited by resource-intensive data pipelines, reliance on textured 3D models, and sensitivity to geometric deviations caused by damages or assembly defects. We present PIXIE, a zero-shot framework that estimates the 6D pose of an object from an RGB image using only an untextured 3D model. Synthetic depth and normal maps are rendered from sampled reference viewpoints and matched to the query image via a pretrained cross-modality feature matcher. Matched keypoints are back-projected to obtain 2D--3D correspondences for PnP-based pose estimation. Relying exclusively on geometry makes the method inherently robust to lighting and texture variation, while correspondence filtering handles geometric deviations between the model and physical object. We evaluate on widely-used public benchmarks, reporting state-of-the-art results on texture-less objects without object-specific training, and introduce a novel dataset with assembly defects, texture variations, and occlusion to demonstrate real-world applicability.

---


### 123. [Presentation, Not Mechanism: A Render Confound in Deprecation-Aware Memory Evaluation](https://arxiv.org/abs/2607.16019)

**<font color=#1a73e8>作者：</font>** Zhaoyang Jiang, Zhizhong Fu, Zicheng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly retrieve from records that revise themselves: issue threads, encyclopedic histories, policy logs, and long conversations. The challenge is not only finding relevant evidence, but deciding which claims remain in force, which were superseded, and when to abstain. Structured memories promise to solve this with typed edges, temporal updates, and conflict status, yet evaluations often change mechanism and prompt presentation together. We study this as Evidence-State Revision, comparing flat retrieval, coarse edge invalidation, and fine-grained RevisionLedger on 2,907 high-agreement questions from GitHub, multi-repo issue histories, Wikipedia, and DyKnow-style temporal streams. A render-matched control (same layout, deprecation disabled) reveals the central confound: when a value is changed and later restored, RevisionLedger appears to beat a flat baseline by +0.182, but almost all the gain comes from easier presentation; the fine-grained mechanism residual is indistinguishable from zero (+0.021 to +0.025 across two judge families). After presentation is controlled, coarse invalidation is the only mechanism that pays for current-state queries, beating the fine ledger by 0.084; the same query-sufficiency principle says provenance mainly needs retained invalidated evidence, not richer typing. Memory evaluations should hold render fixed, and deprecation-aware systems should deploy the coarsest retained state that covers their queries.

---


### 124. [Candidate Attended Dialogue State Tracking Using BERT](https://arxiv.org/abs/2607.16021)

**<font color=#1a73e8>作者：</font>** Junyuan Zheng, Onkar Salvi, John Chan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialogue state tracking (DST) is one of the core components in task-oriented dialogue systems. At each turn in a conversation, DST estimates the user belief or dialogue state, which is used as input for downstream modules to predict system actions and generate responses. The increasingly popular dialogue system applications like Google Assistant, Siri and Alexa need to support a large number of services and APIs, resulting in growing attention to the scalability of such systems. Especially for some domains with little or no training data, the capability of transferring existing knowledge of other domains is highly desired. In this paper, we present a novel scalable framework for multi-domain dialogue state tracking. The proposed system leverages the pretrained BERT model to achieve zero-shot generalization, making it easy to quickly adapt to new domains without additional training. The performance of our model is evaluated on recently released schema-based dialogue (SGD) dataset, showing significant improvement compared to previous baseline.

---


### 125. [Constrained Hebbian Learning Supports Efficient Representational Allocation under Structural Constraints](https://arxiv.org/abs/2607.16027)

**<font color=#1a73e8>作者：</font>** Patrick Inoue, Florian Röhrbein, Andreas Knoblauch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Introduction: Biological systems face anatomical and metabolic constraints, including costly synaptic maintenance and limited connectivity. These constraints favor neural codes that compress behaviorally relevant information into low-redundancy patterns. We test whether an excitatory competitive Hebbian rule can support synaptic resource allocation under such constraints and whether the resulting representations occupy a more favorable cost-performance regime than reference learning rules.
Methods: Representational cost is quantified using mutual-information-based measures derived from the Variational Information Bottleneck. Experiments use fixed audiovisual embeddings from three audiovisual benchmarks (AVE, Kinetics-Sounds, VGGSound100) to isolate downstream associative plasticity. Hebbian learning is compared with Dense Difference Target Propagation (DDTP) and backpropagation (BP) under matched sparsity and architectural constraints.
Results: Hebbian learning achieves lower task-information cost (CTI) than sparse BP and DDTP in the main compressed comparisons, while reaching CTI values comparable to shallow BP with nonnegative weights. Rather than uniformly improving classification performance, Hebbian learning shifts the trade-off between task-relevant information and representational cost, yielding lower CTI at comparable functional performance in several settings.
Discussion: The results indicate a cost-performance trade-off rather than uniform accuracy gains. For a given level of task-relevant information, Hebbian representations retain less input information while preserving functional performance, although accuracy is slightly reduced on some datasets. These findings support interpreting Hebbian learning as a mechanism for synaptic resource allocation rather than as a general strategy for maximizing audiovisual classification accuracy.

---


### 126. [CLaC@FinMMEval 2026 Task 3: Sentiment-Augmented Deep Reinforcement Learning for Active Trading -- An Alpha-Reward Approach](https://arxiv.org/abs/2607.16028)

**<font color=#1a73e8>作者：</font>** Andrei Neagu, Eeham Khan, Leila Kosseim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents our system for Task 3 of the CLEF 2026 FinMMEval Lab, which requires daily long, flat, or short trading decisions for Bitcoin (BTC) and Tesla (TSLA) using news and historical market data. We formulate the problem as a discrete-action Markov Decision Process and compare four deep reinforcement learning algorithms: Policy Gradient (PG), Proximal Policy Optimization (PPO), Deep Q-Learning (DQL), and Deep Deterministic Policy Gradient (DDPG). The agents use technical indicators, cyclical calendar encodings, and daily news sentiment scores produced by LLaMA 3.2 1B. To reduce overfitting and align training with the objective of outperforming buy-and-hold, we introduce an alpha reward based on excess market return and randomize episode start dates. Hyperparameters are optimized with Ray Tune over 180 trials per algorithm-asset pair, with early stopping and model selection based on validation Sharpe ratio. On the CLEF Task 3 test set, DDPG achieves the strongest overall performance. DQL was selected a priori for the live endpoint because it obtained the highest validation Sharpe ratio, with selection performed without access to the test period. For TSLA, DDPG and DQL achieve cumulative returns of 54.96% and 52.62%, respectively, compared with 16.45% for buy-and-hold. For BTC, DDPG achieves a positive return of 1.58% while buy-and-hold declines by -34.27%. The results also reveal a substantial validation-to-test generalization gap, highlighting the difficulty of transferring policies selected in bull-market conditions to a bear-market regime.

---


### 127. [Loop the Loopies!](https://arxiv.org/abs/2607.16051)

**<font color=#1a73e8>作者：</font>** Zitian Gao, Yilong Chen, Yihao Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Loopie, the most powerful looped Transformer to date. The Loopie series consists of two Mixture-of-Experts (MoE) models: a 20B-parameter model with 2B active parameters and a 6Bparameter model with 0.6B active parameters. Looped Transformers have long faced a challenge: given an N-fold increase in pre-training compute, increasing the parameter count by a factor of N usually outperforms looping a model N times. Loopie addresses this challenge. Extensive ablation studies, including comparisons with a vanilla 30B-A3B model, show that Loopie substantially outperforms vanilla Transformer baselines trained with the same compute budget. Our novel post-training pipeline equips Loopie with strong reasoning abilities. At the 2025 IMO and IPhO, Loopie achieves gold-medal performance without tools.

---


### 128. [Gasp: A DeFi Application Specic Rollup as a Consolidation Layer for All Assets](https://arxiv.org/abs/2607.16052)

**<font color=#1a73e8>作者：</font>** Stanislav Vozarik, Mateusz Nowakowski, Shoeb Siddiqui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Gasp is a decentralized exchange designed as an application-specific Layer 2 (L2) rollup with omnichain connectivity, leveraging EigenLayer's restaked ETH for computation correctness and finalization. With a goal of being a consolidation layer for all crypto assets, the Gasp platform employs optimistic rollup technology to facilitate gas-free, native cross-chain swaps without reliance on traditional bridges, ensuring tokens retain their original L1 grade security. By combining an app-chain architecture with escape hatch mechanisms, Gasp guarantees withdrawal, while MEV minimization through Themis architecture reduces value extraction risks. Gasp's proof-of-liquidity framework unlocks staked liquidity, enhancing capital efficiency and liquidity depth by integrating staking with liquidity provisioning. Additionally, the protocol introduces a time-based reward mechanism, incentivizing long-term liquidity commitment via an asymptotic reward curve. This paper examines the current challenges in cross-chain communication, delineates Gasp's architectural innovations and security guarantees, and examines novel approaches to optimizing DeFi ecosystems.

---


### 129. [Multi-Modal Semantic Segmentation of Electrolyzer Components for Sustainable Hydrogen Technologies: A Dual-Branch Deep Learning Approach](https://arxiv.org/abs/2607.16056)

**<font color=#1a73e8>作者：</font>** Wasimul Karim, Nur Mohammad Fahad, Abdul Hasib Siddique 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of electrolyzer materials is essential for automated disassembly, sustainable recycling, and circular manufacturing in hydrogen technologies. However, this task is challenging due to strong visual similarity between materials, spectral overlap, irregular shapes, and severe class imbalance. To address these challenges, we propose an AI-driven dual-branch framework, Hyperspectral-RGB Electrolyzer Materials Network (HREM-Net), that combines hyperspectral imaging (HSI) and RGB images for electrolyzer material segmentation. We implemented several innovative modules, including Efficient Channel Attention, Coordinate Attention, Mobile Inverted Bottleneck blocks, and Atrous Spatial Pyramid Pooling to capture spectral and spatial features from HSI, and RGB images. With an adaptive gated cross-modal fusion module and composite loss function, HREM-Net achieves a mean class accuracy of 91.66% and a mean Intersection over Union (mIoU) of 0.82 on the Electrolyzers-HSI dataset, outperforming baseline segmentation models. Cross-dataset validation on the PCB-Vision dataset demonstrates strong generalization with 96.91% accuracy and 0.93 mIoU. This work poses its potential as an industrial application to improve electrolyzer efficiency, thereby improving the predictive maintenance of hydrogen production.

---


### 130. [ArtChart: A Benchmark for Faithful Artistic Chart Generation with Integrated Text Rendering](https://arxiv.org/abs/2607.16060)

**<font color=#1a73e8>作者：</font>** Meijia Huang, Yingjie Yin, Shihao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artistic charts make data memorable and visually engaging, but generating them faithfully demands simultaneously preserving numerical geometry, rendering exact in-image text, binding labels to correct marks, and maintaining coherent artistic style. Current text-to-image and image editing models frequently fail on these coupled constraints, producing distorted geometries, hallucinated text, misbound labels, or over-stylized marks that undermine readability and mathematical integrity. This paper introduces ArtChart, a framework for artistic chart generation with integrated text rendering, encompassing a task definition, benchmark, and evaluation protocol. This is the first work to simultaneously address mathematically faithful chart synthesis, accurate in-image text rendering, and artistic stylization of chart elements. ArtChart features a chart-specific plug-and-play module conditioned on text-free grayscale chart layouts, ensuring mathematical and logical fidelity. A RL learning strategy with OCR accuracy, layout quality, and aesthetic rewards refines generation, while a multi-expert distillation framework resolves inter-reward conflicts through specialized expert optimization. We construct ArtChart-Bench, a bilingual 2K-prompt benchmark spanning four chart types and diverse label formats. We further design ArtChart-Eval, a six-axis evaluation suite covering mathematical logic, text accuracy, text layout, aesthetics, instruction following, and readability, supporting comparison across T2I, image-editing, controllable-generation, and closed-source API models. Extensive experiments demonstrate that ArtChart consistently outperforms open-source baselines, producing charts that are both visually appealing and math faithful.

---


### 131. [When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector Geometry Analysis](https://arxiv.org/abs/2607.16062)

**<font color=#1a73e8>作者：</font>** S. Aaron McClendon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging is promoted as a substitute for joint multi-task training, yet in the reinforcement-learning setting this substitution is essentially never tested against the baseline it claims to replace: methods merge independently released agents precisely because a joint model is unavailable. We build the missing comparison. Training difficulty-1 and difficulty-2 Qwen3-8B specialists on the AppWorld agent benchmark with LOOP, we merge them (TIES, RAM+) and pit the result against a jointly trained model on the same data. On task-goal completion, merging matches joint RL -- and every merge variant is statistically indistinguishable. To explain why merge method does not matter here, we measure the geometry of the specialists' task vectors, which carries no task-sampling noise: they are near-orthogonal (cosine 0.06 - 0.10) despite ~65% support overlap, a small, shared direction that grows over training and that we calibrate against a random-init floor and a same-run ceiling to confirm it reflects learning, not the low-rank parameterization. Because direction and support are decoupled, support and sign-based merging (RAM, TIES) collapse to near-uniform averaging. We release all code and statistics.

---


### 132. [Spatial Normalization for Cross-Domain Retinal Layer Segmentation in Optical Coherence Tomography](https://arxiv.org/abs/2607.16065)

**<font color=#1a73e8>作者：</font>** Iker Moran-Cavero, Monica Hernandez, Elvira Mayordomo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retinal layer segmentation in Optical Coherence Tomography (OCT) is a fundamental step for extracting quantitative biomarkers of retinal structure. Indeed, there is a growing interest in the analysis of OCTs in the context of neurodegenerative diseases. However, segmentation remains challenging due to speckle noise, shadowing artifacts, low contrast between adjacent layers, anatomical variability across subjects, and domain shifts arising from different acquisition protocols and clinical populations. While deep learning methods have achieved remarkable performance, their robustness and generalization across heterogeneous datasets remain limited. In this work, we investigate the role of spatial normalization as a preprocessing strategy to mitigate geometric domain shifts and improve the consistency of retinal layer segmentation. Inspired by standard practices in neuroimaging, we introduce a fovea-centered normalization framework that aligns OCT volumes into a common anatomical reference. We perform a comprehensive evaluation of state-of-the-art deep learning architectures. To provide a comprehensive assessment of segmentation quality, we combine conventional overlap-based metrics at B-scan level with topology-aware metrics at A-scan level and thickness-based measures at the en-face level. In cases where a ground truth is not available, we propose topology violation quantitative metrics that do not require ground truth annotations and a thickness-based qualitative assessment that captures structural consistency and clinically relevant patterns at the en-face level. The results demonstrate the importance of spatial normalization in OCT segmentation pipelines toward the development of robust and clinically meaningful retinal analysis tools, enabling reliable biomarker extraction and downstream computational analysis in neurodegenerative research.

---


### 133. [Adaptive Contrast Enhancement and Optimised Feature Matching for RootSIFT-Based Palm-Vein Recognition](https://arxiv.org/abs/2607.16077)

**<font color=#1a73e8>作者：</font>** Kaveen Perera, Fouad Khelifi, Ammar Belatreche  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Palm-vein recognition is a highly secure biometric modality due to the uniqueness and subcutaneous nature of vein patterns. However, low contrast in palm-vein images, caused by NIR light scattering and sensor limitations, remains a significant challenge. To address this, we propose the Intensity-Limited Adaptive Contrast Stretching with Bidirectional Gaussian-weighted Overlapping Tiles (ILACS-BGOT) method, an enhancement of the previously developed ILACS with Layered Gaussian-weighted Overlapping Tiles (ILACS-LGOT) technique. ILACS enhances local contrast, while BGOT mitigates blocky artefacts. This study further integrates RootSIFT features with KNN+RT and incorporates the previously introduced Mean and Median Distance (MMD) filter to investigate the parameter variations of both MMD and RT, and their impact on recognition performance. A comprehensive analysis was conducted across three benchmark datasets (CASIA, PolyU, and PUT), using 42 combinations of MMD filter thresholds and RT values. Results were evaluated using EER and Accuracy. Findings reveal that higher template sizes improve performance, while varying MMD thresholds reflect dataset-specific rotational variations. The proposed system demonstrates superior generalisability, achieving significant improvements in both EER and Accuracy over existing methods. Furthermore, the underlying ILACS-BGOT mechanism suggests potential applicability beyond palm vein recognition to other biometric modalities such as finger vein and palmprint recognition, and more generally to low-contrast image enhancement across computer vision applications.

---


### 134. [Physics-Based Deep Spatiotemporal Hyperlocal Radar Nowcasting with a Multi-Variable U-Net for High-Resolution Precipitation Forecasting](https://arxiv.org/abs/2607.16080)

**<font color=#1a73e8>作者：</font>** Akshay Sunil, Muhammed Rashid, Raja Sekhar Sivaraju 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Precipitation nowcasting over the immediate 10-90 min period is important for flood management and real-time decision-making in urban regions. Conventional short-range forecasting with high-resolution numerical weather prediction requires frequent data assimilation, model initialization, and spin-up, introducing computational latency. Machine learning provides an alternative by learning storm evolution directly from high-frequency observations and producing forecasts quickly after training. This is particularly relevant for Mumbai, India, where monsoon convection, land-sea interactions, and localized intense rainfall make short-term prediction difficult. Here, we develop a compact radar-only nowcasting framework that combines multi-elevation reflectivity, Doppler radial velocity, and radial-velocity-gradient proxy features within an encoder-decoder U-Net. Using the most recent radar volume scan, the model predicts 12 future composite reflectivity fields at 7.5-min intervals up to 90 min lead time. The derived velocity magnitude, divergence-like, directional-shear, and vorticity-like channels represent kinematic signatures associated with convergence and boundary interactions without requiring full wind-field retrieval. A high-reflectivity attention module improves sensitivity to convective cores, and physics-guided attribution examines whether the learned sensitivities are meteorologically meaningful. The model is trained using Mumbai Doppler radar observations from May to August 2023 and evaluated on temporally independent events. At 90 min lead time, Critical Success Index values are 0.437, 0.332, and 0.193 for $\geq$10, $\geq$20, and $\geq$30 dBZ thresholds, respectively. Compared with persistence, the model gives lower RMSE and higher spatial correlation at longer lead times. Once trained, it runs on a standard computer, generating nowcasts within seconds for real-time use.

---


### 135. [Controlling Implicit Shortcut Reliance in L2 Spoken English Auto-markers](https://arxiv.org/abs/2607.16085)

**<font color=#1a73e8>作者：</font>** Shilin Gao, Mark J. F. Gales, Kate M. Knill  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Increasingly, speech and language processing tasks take either audio or text directly rather than extracting features from these as the input to the classifier or regressor. Often these systems make use of complex, for example transformer-based, processes that have the ability to derive highly non-linear mappings between the input and the output. Unfortunately these systems can also learn ''shortcuts'' where the classifier is overly reliant on particular aspects of the input to yield the output. For the task of language proficiency assessment, this over-reliance can enable learners to increase their score by exploiting the shortcut rather than improving their ability. This paper introduces a novel training criterion that is able to reduce the classifier's reliance on shortcuts, thus for example limiting this option for malpractice in language assessment. This process is illustrated on two forms of assessment system, one based on the audio the other on the speech recognition text. The results show that, for both systems, there is higher correlations with features that could be exploited for malpractice than expected from the human reference, indicating an over-reliance on these features. By introducing the modified training criterion, this correlation can be reduced to be closer to the reference correlation.

---


### 136. [Neural spectroscopy of AlphaFold2 reveals encoded protein conformational landscapes](https://arxiv.org/abs/2607.16087)

**<font color=#1a73e8>作者：</font>** Kaustav Mehta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AlphaFold2's 93 million parameters, shaped by the evolutionary record of protein structure encoded in the Protein Data Bank and in sequence alignments, are conventionally treated only as machinery for converting sequence to structure. We propose they are also a scientific object that can be analyzed directly: a learned encoding of protein conformational organization that can be probed and characterized. By smoothing the Evoformer's weight tensors with a Gaussian convolution and scaling the result, we show that the trained model produces physically structured conformational landscapes. Under perturbation, ubiquitin's native contacts break in the order established by decades of folding experiments. For KaiB, five independently trained models agree that the alternative fold is not recovered under perturbation. For alpha-synuclein, five models produce five different but coherent landscapes, mapping where the training signal has determined the representation and where it has not. Matched-power noise controls confirm that random corruption of equal magnitude produces debris, not conformations. The model learned to predict static structures; the conformational organization visible under perturbation was not an explicit training target, suggesting it emerged as a byproduct of that objective. AlphaFold2's weights appear to encode structural constraints, shaped by evolutionary and structural training data, that extend beyond what unperturbed inference reveals. We call the approach of reading them neural spectroscopy, and Scaled Gaussian Convolution one such protocol.

---


### 137. [DADiff: Diffusion-Driven Cross-Domain Policy Adaptation for Reinforcement Learning](https://arxiv.org/abs/2607.16090)

**<font color=#1a73e8>作者：</font>** Hanyang Chen, Anirudh Satheesh, Longchao Da 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transferring policies across domains poses a vital challenge in reinforcement learning, due to the dynamics mismatch between the source and target domains. In this paper, we consider the setting of online dynamics adaptation, where policies are trained in the source domain with sufficient data, while only limited interactions with the target domain are allowed. There are a few existing works that address the dynamics mismatch by employing domain classifiers, value-guided data filtering, or representation learning. Instead, we study the domain adaptation problem from a generative modeling perspective. Specifically, we introduce DADiff, a diffusion-based framework that leverages the discrepancy between source and target domain generative trajectories in the generation process of the next state to estimate the dynamics mismatch. Both reward modification and data selection variants are developed to adapt the policy to the target domain. We also provide a theoretical analysis to show that the performance difference of a given policy between the two domains is bounded by the generative trajectory deviation. More discussions on the applicability of the variants and the connection between our theoretical analysis and the prior work are further provided. We conduct extensive experiments in environments with various shifts to validate the effectiveness of our method. The results demonstrate that our method provides superior performance compared to existing approaches, effectively addressing the dynamics mismatch. We provide the code of our method at this https URL

---


### 138. [DoSQ: A Cross-Layer Denial of Service Quality Attack by Exploiting Side Channels in 5G NR](https://arxiv.org/abs/2607.16102)

**<font color=#1a73e8>作者：</font>** Mahmudul Hassan Ashik, Moinul Hossain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The 3rd Generation Partnership Project (3GPP)'s Fifth Generation New Radio (5G NR) is critical to supporting mission-critical services. However, 5G systems are vulnerable to smart jamming attacks that can propagate to applications running on top of these networks (i.e., cross-layer). The 5G gNB broadcasts resource scheduling information for the legitimate UEs over the air interface, with a prevailing assumption that this surface alone reveals nothing useful about a user device. However, we show that using the Downlink Control Information (DCI) is sufficient to degrade Application layer service quality, i.e., Denial of Service Quality (DoSQ), by inferring the Application layer Goodput (i.e., via side-channel analysis). Therefore, we present DoSQ, a protocol-aware attack that decodes per-slot DCI to inject interference onto the victim UE's Physical Resource Blocks (PRBs) within the same 1 ms slot, while a cross-layer classifier estimates the victim's Goodput state and trend from DCI features alone, without observing a single encrypted byte. Evaluated on a private 5G NR testbed against YouTube Live, DoSQ drives the target's Goodput down by up to 50% at sparse hit-rates, while a co-located non-target UE remains largely unaffected. Moreover, the classifier achieves a precision of 0.87 at the top 1% of attack-now confidence, a 4.21 times lift over the base rate. Furthermore, we propose an SSB frequency-time-hopping countermeasure that increases the attacker's resynchronization cost. The result is the first empirical measurement of a radio-to-application side channel that any protocol-aware adversary can exploit.

---


### 139. [Attention-Guided Saliency Maps for Interpreting Visualization Literacy in VLMs](https://arxiv.org/abs/2607.16105)

**<font color=#1a73e8>作者：</font>** Maeve Hutchinson, Abderrahmane Wassim Mehdaoui, Pranava Madhyastha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding how vision-language models (VLMs) interpret data visualizations remains an open problem, and is increasingly important as these models are used for analytical tasks where reliable reasoning is essential. We introduce a lightweight, diagnostic saliency map method tailored for text generation over images using transformer models, the current state-of-the-art models in visualization interpretation. Our approach aggregates the language model's attention over the visual tokens across all heads and layers, then maps this attention back onto the vision encoder's patch grid to localise it over the image, producing a direct correspondence between each generated answer token and the image regions it attended to. This yields fast, gradient-free saliency maps that expose how VLMs allocate focus across visual elements during answer generation, enabling inspection of whether model attention aligns with semantically relevant components. We evaluate our approach using a deletion metric which validates the causal faithfulness of our saliency maps to the model's behavior.

---


### 140. [Harmonizing AI Safety Thresholds](https://arxiv.org/abs/2607.16112)

**<font color=#1a73e8>作者：</font>** Wilber Sean Anterola, Matthew Ball, Luis F. Lafuerza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier AI companies have published capability thresholds that differ substantially, making it difficult for third parties to verify whether a threshold has been crossed or to compare requirements across companies. Moreover, without common minimum thresholds, risk mitigation may be inconsistent, creating a potential race to the bottom in safety standards. We develop a methodology for deriving harmonized thresholds across three risk domains. For misuse risks (cyber and biological), we take expected harm as the key primitive and use an explicit risk-modeling approach that accounts for risk channels and model release conditions. For automated AI R&D, we base our proposed threshold on the observed rate of AI progress rather than expected harm. Our analysis expands upon prior work and highlights existing empirical gaps and limitations.

---


### 141. [Rate-Utility Frontiers for Language Encodings: Comparing Tokens, Bytes, and Pixels Under Controlled Linguistic Content](https://arxiv.org/abs/2607.16117)

**<font color=#1a73e8>作者：</font>** Ingo Ziegler, Martin Krebs, Desmond Elliott  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models encode text as subword tokens, raw bytes, or rendered pixels, but these encodings are usually compared under modeling constraints that expose different amounts of linguistic content to models across different languages. We instead ask what each encoding preserves when both the content and the downstream capacity are controlled. Using verified parallel sentences across thirteen languages and five scripts, we compare tokens, bytes, and pixels through a shared bottleneck whose width is swept to trace rate-utility frontiers. This separates three quantities that are often conflated: the number of input positions an encoding creates, the latent capacity available after encoding, and the task-relevant information that survives compression. We evaluate three utilities: surface form preservation, cross-lingual sentence alignment, and topic classification. No encoding dominates across tasks or capacity regimes. Pixels preserve surface form best, bytes preserve cross-lingual alignment best, especially in same-script multilingual settings, and tokens support topic prediction best. These performances are not explained by sequence length alone. Short inputs can discard useful meaning, while long inputs can preserve information that compresses well. Choosing an encoding is therefore not a fixed preference for tokens, bytes, or pixels, but a rate-utility tradeoff that depends on the task, language mix, capacity regime, and compute budget.

---


### 142. [Toward Semantic Communication for Real-time Mobile 3D Reconstruction](https://arxiv.org/abs/2607.16128)

**<font color=#1a73e8>作者：</font>** Fangzhou Zhao, Yao Sun, Xuesong Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time mobile 3D reconstruction is fundamental to many emerging applications such as autonomous navigation and digital twin construction, where a moving platform continuously captures an image stream and transmit to a computing server for scene understanding. Unlike offline reconstruction, camera poses and scene geometry are estimated on-the-fly during acquisition, making multi-view consistency a real-time requirement and rendering geometric estimation highly sensitive to communication-induced distortions. Semantic communication (SemCom) transmits compact semantic information, offering a promising way to preserve task-critical data over unreliable links. However, existing designs are optimized at the image or single-view level and without providing explicit reliability information for geometric estimation, limiting their applicability to real-time mobile 3D reconstruction. In this context, we propose a SemCom framework for real-time mobile 3D reconstruction. The framework includes a semantic transceiver that outputs a reconstructed image alongside a pixel-wise confidence map, quantifying the reliability of each region. We further introduce a confidence-guided geometric estimation method, incorporating confidence into RANSAC-based pose initialization and bundle adjustment to reduce the influence of unreliable regions and enhance robustness under noisy channels. Simulations show that, compared to existing SemCom and traditional seperate source and channel coding, our framework maintains high image quality while significantly improving pose estimation accuracy and 3D structural consistency.

---


### 143. [When Do Multi-Agent Systems Help? An Information Bottleneck Perspective](https://arxiv.org/abs/2607.16133)

**<font color=#1a73e8>作者：</font>** Wendi Yu, Lianhao Zhou, Xiangjue Dong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM powered multi-agent systems (MAS) have emerged as a promising paradigm for complex tasks. However, their advantages over single-agent systems (SAS) remain unclear, with performance varying inconsistently across settings. Here, we provide an information bottleneck perspective on elucidating the differences between MAS and SAS. Specifically, our key observation is that a SAS accumulates its full reasoning trace in one shared context, while a MAS uses isolated local contexts connected by bounded relay messages. We show that, under infinite relay bandwidth, any SAS can be simulated by a MAS that transmits the full upstream context. Thus, the nontrivial advantage of MAS arises under bounded relays, where compression introduces a fundamental trade-off: reducing redundant context can improve efficiency, but may also incur loss of task-relevant information. We formalize this trade-off as an information bottleneck controlled by an effective parameter $\beta$, which captures how the balance shifts with model capability, and shows that MAS gains arise when context reduction outweighs relay information loss. We conduct 18 controlled experiments across five benchmarks and three model scales to validate our theoretical studies. We observe that MAS consistently helps when relays are near-sufficient, especially for weaker models. In contrast, MAS gains shrink or reverse when relays incur information loss, especially for stronger models that can already extract useful information from redundant context and thus gain little from compression. Our study shows that multi-agent design is fundamentally an information-bottleneck optimization problem. This perspective explains when bounded inter-agent communication helps or hurts.

---


### 144. [Improving Improved Kernel PLS](https://arxiv.org/abs/2607.16138)

**<font color=#1a73e8>作者：</font>** Ole-Christian Galbo Engstrøm  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Improved Kernel Partial Least Squares (IKPLS) algorithms 1 and 2 are among the fastest PLS calibration algorithms. This article focuses on two shared steps, the computation of the $\mathbf{X}$ rotations, $\mathbf{R}$, and the $\mathbf{Y}$ loadings, $\mathbf{Q}$, and accelerates both. For $\mathbf{R}$, term-by-term accumulation is replaced by a direct evaluation strategy that requires the same number of multiplications but parallelizes better on modern hardware. For $\mathbf{Q}$, I identify - to the best of my knowledge, for the first time - equivalences showing that each $\mathbf{Y}$ loading is obtainable, up to explicitly derived constants, from quantities already computed earlier in the same iteration, and I exploit them in IKPLS to reduce the cost of each loading from $\Theta\left(KM\right)$ to $\Theta\left(M\right)$ operations whenever $M = 1$ or $2 \leq M < K$, with $K$ predictor variables (number of columns in $\mathbf{X}$) and $M$ response variables (number of columns in $\mathbf{Y}$). Both improvements provably yield exactly the same $\mathbf{W}$, $\mathbf{P}$, $\mathbf{Q}$, $\mathbf{R}$, and $\mathbf{T}$ as the original algorithms. Benchmarks with NumPy (CPU) and JAX (GPU) show speedups of up to two orders of magnitude for the isolated steps and of approximately $2\times$ (CPU) and $6\times$ (GPU) for entire fits. Both improvements are implemented in the free, open-source Python package \texttt{ikpls}.

---


### 145. [CLIFE: Camera-LiDAR Fusion Framework for Edge-Deployable Roadside VRU Perception](https://arxiv.org/abs/2607.16154)

**<font color=#1a73e8>作者：</font>** Tam Bang, Hoang H. Nguyen, Lei Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable roadside perception of vulnerable road users (VRUs) remains challenging under occlusions, variable lighting, and diverse weather conditions, particularly under strict edge-computing and latency constraints. Existing multi-sensor fusion systems rely on cloud or server-grade infrastructure, creating a deployment gap at real-world intersections. We present CLIFE, an edge-native camera-LiDAR fusion framework that integrates targetless online calibration and lightweight late-fusion tracking entirely on a single embedded device, without cloud offloading. CLIFE adaptively refines camera-LiDAR alignment on demand and performs multi-sensor fusion and track association with O(N log N) per-frame cost. We deploy CLIFE across 12 signalized intersections in Chattanooga and conduct an in-depth evaluation at a representative intersection using synchronized camera-LiDAR data that spans diverse daytime, nighttime, and weather conditions. Our experiments demonstrate that the fusion architecture substantially enhances the perceptual range and robustness of the individual sensors under varied environmental and traffic conditions. The late-fusion core operates at 53.2 FPS on the Jetson AGX Thor, ensuring high throughput for real-time intersection-scale applications. By centering perception at the edge, CLIFE provides a deployable foundation for downstream safety applications, while reducing bandwidth and calibration overhead for agencies operating multi-intersection corridors.

---


### 146. [PRISA: Proactive Infrastructure LiDAR Framework for Intersection Safety Assessment](https://arxiv.org/abs/2607.16156)

**<font color=#1a73e8>作者：</font>** Tam Bang, Hussam Abubakr, Emiliano de la Garza Villarreal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban intersections are among the most hazardous locations in road networks, posing significant risks to vehicles and vulnerable road users (VRUs) such as pedestrians and cyclists. The complexity of multi-agent interactions demands continuous, real-time monitoring systems capable of anticipating conflicts before they escalate into crashes. We present PRISA, a modular infrastructure LiDAR framework leveraging privacy-preserving, low-light-robust roadside sensors for long-term traffic observation and real-time risk detection at the edge. The framework comprises two core components: a sensing and perception layer and a plug-and-play risk assessment module. The latter automatically curates site-specific training data from accumulated perception outputs to train a trajectory prediction model without manual annotation. It then deploys the trained model for continuous motion forecasting and dual surrogate safety evaluation, using Time-to-Collision (TTC) for longitudinal conflicts and Predicted Post-Encroachment Time (PPET) for crossing and VRU-involved interactions. PRISA is evaluated on the public R-LiViT dataset and deployed on an NVIDIA Jetson AGX Thor at a live signalized intersection in Chattanooga, Tennessee. PPET-based assessment operates at 194~ms end-to-end latency over a 2.4-second predictive horizon, with TTC-based detection and perception remaining within real-time constraints, demonstrating practical feasibility for proactive multi-agent intersection safety monitoring.

---


### 147. [Behaviour-Conditioned Neural Processes for Adaptive Residential Short-Term Load Forecasting](https://arxiv.org/abs/2607.16168)

**<font color=#1a73e8>作者：</font>** Ramin Soleimani, Andrea Visentin, Dirk Pesch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residential short-term load forecasting (STLF) is challenging because household demand is heterogeneous, temporally variable, and shaped by diverse behavioural routines. This work investigates whether inferred behavioural structure can be embedded within the forecasting mechanism of a Neural Process-based probabilistic model, rather than used only as an external grouping signal, for context-conditioned residential STLF. We propose a behaviour-conditioned Attentive Neural Process framework that treats each load profile as a forecasting task. Behavioural structure is represented by a discrete latent variable inferred from the available context and used for behaviour-conditioned decoder conditioning, while a continuous latent variable captures shared functional uncertainty across heterogeneous profiles. To enable conditioning without ground-truth behavioural labels, clustering-derived information provides weak supervision during training, whereas test-time conditioning relies only on context-inferred class distributions. Experiments on the Smart Grid, Smart City (SGSC) dataset use user-disjoint train/validation/test splits, variable context lengths, and multi-step forecast horizons, with comparisons against a label-agnostic ANP baseline and fixed-window deterministic STLF baselines. The proposed variants improve MAE and CRPS over ANP across horizons and context settings, with the largest gains under limited context. The best-performing variant achieves average reductions of 7.9% in MAE and 6.9% in CRPS relative to ANP. Compared with fixed-window baselines, this variant achieves lower RMSE across all evaluated horizons while maintaining competitive MAE, suggesting fewer large prediction deviations under heterogeneous consumption patterns. These results support single-model, uncertainty-aware forecasting across heterogeneous households, contexts, and horizons.

---


### 148. [Physics-enhanced reinforcement learning for real-time optimal control of dynamical systems](https://arxiv.org/abs/2607.16177)

**<font color=#1a73e8>作者：</font>** Matteo Tomasetto, Nicolò Botteghi, Gabriele Bruni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has recently emerged as a promising feedback control strategy for nonlinear and complex dynamical systems. However, RL algorithms are sample inefficient and require a large number of interaction with the environment to synthesize optimal control strategies. Consequently, applications of RL are typically limited to sparse sensors and actuators due to the curse of dimensionality entailed by the exploration-exploitation dilemma in high-dimensional spaces. In this work, we bridge RL and traditional optimal control for dynamical system with a novel Physics-EnhAnced Reinforcement Learning (PEARL) paradigm tailored to the control of high-dimensional and parametric dynamical systems, exploiting the differentibility of their dynamics. Specifically, PEARL employs an actor-adjoint algorithm that leverages automatic differentiation to compute policy gradients over short horizons and adjoint-based sensitivities of future returns approximated via neural networks, significantly reducing the number of environment interactions, while mitigating long-term gradient instabilities. Through two challenging parametric navigation problems in unsteady flows, we show that PEARL (i) effectively exploits differentiable environments to outperform state-of-the-art RL algorithms, (ii) is sample efficient, thanks to the physics-guided policy learning, (iii) generalizes across multiple scenarios, which is crucial when dealing with parametric systems, and (iv) enables scaling RL to high-dimensional state and action spaces, without requiring low-dimensional state representations or multi-agent strategies.

---


### 149. [A Blueprint for Equilibrium-Based Differentiable Continuous-Variable Thermodynamic Computing](https://arxiv.org/abs/2607.16183)

**<font color=#1a73e8>作者：</font>** Owen Lockwood, Jérémy Béjanin, Joost Bus 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To address the escalating energy and latency demands of machine-learning workloads, we introduce a blueprint for an energy-efficient and fast thermodynamic computing stack that leverages stochastic analog processes in physical hardware. In this work, we focus on energy-based thermodynamic computing where the stochastic process is well described by Langevin dynamics with tunable energy potentials. The implementation of such potentials in physical hardware enables us to generate and sample from basic parameterized energy-based models. We demonstrate how to construct and train popular classes of machine learning models based on these hardware-native energy-based models, using the framework of probabilistic graphical models. We analyze the runtime and energy consumption of different models in this thermodynamic paradigm based on theoretical considerations and numerical studies. As a preliminary experimental realization of such hardware, we present our stochastic analog superconducting circuits driven by thermal noise. Together, these results outline a path toward energy-efficient thermodynamic hardware for probabilistic machine learning.

---


### 150. [Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video QA](https://arxiv.org/abs/2607.16189)

**<font color=#1a73e8>作者：</font>** Ce Zhang, Ziyang Wang, Yulu Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounded long-video question answering (Grounded LVQA) requires answering a question about a long video while localizing the short evidence interval that supports the answer. Recent agentic methods frame this task as multi-turn exploration with a single crop_video(start, end) action, which supports coarse-to-fine narrowing but provides no primitive for fine-to-coarse backtracking. As a result, these agents typically converge prematurely and cannot recover from an early mistake. We propose VideoTreeSearch (VTS), a framework that casts grounded LVQA as iterative self-correcting search over an adaptive temporal tree. VTS constructs a non-uniform tree from visual scene boundaries so that each node corresponds to a semantically coherent segment, and trains an agent to navigate the tree through four discrete operations: zoom_in, zoom_out, shift, and answer. These operations expose backtracking and recovery as explicit, learnable primitives rather than implicit behaviors. To train this navigation, we introduce a trajectory synthesis pipeline that produces multi-step paths through the tree, including deliberate detours into incorrect branches followed by recovery. We use these trajectories for supervised fine-tuning, followed by reinforcement learning with grounding and answer-accuracy rewards. On three Grounded LVQA benchmarks (CG-Bench, Haystack-LVBench, Haystack-Ego4D), VTS outperforms the strongest prior agentic methods by +12.5 mIoU on CG-Bench and +7.4 T-F1 on Haystack-Ego4D. The learned policy also transfers to general long-video QA, surpassing all prior agentic baselines on Video-MME, MLVU, and LVBench by up to +7.1 accuracy points. Ablations confirm that self-correcting hierarchical search is the central mechanism behind these gains: removing either adaptive descent or explicit backtracking substantially degrades performance. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-152](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
