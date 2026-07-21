# 📦 其他研究 | 2026年07月22日

> 本类共 **386** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-386](./part-08.md)

---

### 101. [NOWJ@COLIEE 2026: Adaptive Pipelines for Legal Retrieval and Reasoning](https://arxiv.org/abs/2607.16603)

**<font color=#1a73e8>作者：</font>** Thuong-Hieu Ngo, Hoang-Trung Nguyen, Huu-Dong Nguyen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents the methodologies and results of the NOWJ team's participation across all five tasks of the COLIEE 2026 competition. For Task 1 (Legal Case Retrieval), we propose a four-stage pipeline comprising candidate filtering, dense retrieval with complementary embedding models, cross-encoder reranking via fine-tuned generative rerankers and MLP-based pairwise classification, and adaptive per-query cutoff prediction. For Task 2 (Legal Case Entailment), we combine BM25 filtering, T5-based reranking, and LLM-based entailment verification with consensus ensemble. For Task 3 (Statute Law Retrieval and Entailment), we adopt a retrieval-augmented generation framework with dense retrieval, attention-based reranking, and few-shot-prompted LLM reasoning. For Task 4 (Legal Textual Entailment), we introduce a dynamic routing pipeline that classifies query difficulty and dispatches cases to either a balanced few-shot solver or a structured zero-shot chain-of-thought solver. For the Pilot Task (Legal Judgment Prediction), we combine hierarchical transformers with CRF layers, argument relation mining, and probabilistic argumentation graph reasoning.

---


### 102. [Privacy Cost as Equity Input: A Group Fairness Criterion for Differentially Private Machine Learning](https://arxiv.org/abs/2607.16620)

**<font color=#1a73e8>作者：</font>** Rakshit Naidu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differential privacy (DP) is increasingly deployed to limit membership inference risk in machine-learning systems. Prior work has shown that DP-SGD can widen accuracy disparities across demographic groups, but this framing treats fairness as a purely outcome-side concern. We argue that privacy cost, the information leakage borne by each group, is itself a form of harm, and adopt a compensatory-fairness framework in which a group that involuntarily bears greater privacy exposure is owed proportionally greater benefit from the system. From this principle we derive the \emph{Privacy-Cost Equity Ratio} (PCER), a group fairness metric defined as a group's positive prediction rate normalized by its per-group overfitting gap. By a standard membership inference bound, this overfitting gap upper-bounds each group's vulnerability to inference attacks, making PCER a conservative measure of benefit relative to exposure. PCER needs only per-group train and test accuracy (no shadow models), making it a practical post-hoc audit tool. We evaluate PCER alongside standard fairness metrics across six benchmark--attribute combinations spanning tabular and NLP domains, under DP-SGD at a range of privacy budgets, and validate the overfitting-gap proxy against a direct threshold membership-inference attack. The results reveal patterns that outcome-based metrics miss. On COMPAS, PCER uncovers a persistent double disadvantage: the protected group bears both greater privacy exposure and worse predictive outcomes, something demographic parity gap masks entirely. Sensitivity analysis shows very strong privacy guarantees collapse both groups' overfitting to a numerical floor, rendering exposure-based audits uninformative in that regime. Together, these findings show that fairness audits of privacy-preserving systems must account for who bears the cost of protection, not only who benefits from its outcomes.

---


### 103. [SPARE-GS: Structural Parsimony and Resource Efficiency for 3D Gaussian Splatting](https://arxiv.org/abs/2607.16624)

**<font color=#1a73e8>作者：</font>** Zhang Chen, Shuai Wan, Fuzheng Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) achieves high-fidelity novel view synthesis in real-time; however its training efficiency and representation compactness are hindered by excessive primitive proliferation. To address this challenge, we formulate the structural evolution of 3DGS as a global budget-constrained optimization problem and derive an optimality condition, which requires the marginal utility of structural resources to be balanced across spatial regions under a finite primitive budget. Based on this formulation, we propose SPARE-GS, a general plug-and-play framework that dynamically aligns the distribution of 3D Gaussian primitives with regional representational demand. SPARE-GS estimates capacity-normalized regional demand, assigns adaptive target quotas, and uses regional budget deviations to coordinate densification, pruning and adaptive termination toward a more balanced structural allocation. Extensive experiments across standard, accelerated, and structure-enhanced 3DGS pipelines demonstrate that SPARE-GS reduces the Gaussian count and training time by an average of 30.38% and 23.81%, respectively, while improving the average PSNR. Moreover, the resulting compact representations reduce downstream processing time and improve the rate-distortion performance of diverse compression and pruning methods, demonstrating the broad applicability of global structural budget regulation.

---


### 104. [DARA: Degradation-Aware Low-Rank Residual Adaptation with Original-to-Corrupted Distillation for Corruption-Robust Animal Re-Identification](https://arxiv.org/abs/2607.16644)

**<font color=#1a73e8>作者：</font>** Cynthia Xie, Talia Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Animal re-identification (Re-ID) relies on fine-grained identity cues that can be disrupted by blur, noise, compression, and other visual degradations. Existing robustness strategies based on degradation-augmented training or pixel-level restoration improve robustness indirectly, but do not explicitly repair shifts in the identity retrieval space. We study corruption-robust animal Re-ID as input-conditioned feature-space repair and introduce DARA, a lightweight retrofit for compact Re-ID models. DARA freezes the fine-tuned backbone and learns routed low-rank residual experts to adapt degraded-input embeddings without corruption-type annotations. To stabilize this adaptive repair, original-to-corrupted distillation uses an original-image teacher to preserve individual embeddings and retrieval relations. Experiments on ATRW, FriesianCattle2017, MPDD, and SeaStarReID2023 show that DARA improves corrupted-query retrieval over standard and augmentation-based fine-tuning, generalizes to unseen corruptions and cross-domain evaluation, and recovers 77.0% of the corrupted-query mAP gap to full corrupted fine-tuning while adding only 0.49% parameters and 0.05% FLOPs.

---


### 105. [DRIFT: Difficulty-aware Rectified Flows for Through-plane MRI Super-Resolution](https://arxiv.org/abs/2607.16649)

**<font color=#1a73e8>作者：</font>** Yoonseok Choi, Eun-Gyu Ha, Daniel Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic Resonance Imaging (MRI) is often acquired with anisotropic resolution to reduce scan time, producing stair-step artifacts along the through-plane direction. In through-plane MRI super-resolution, an efficiency-fidelity trade-off arises: feed-forward regressors are fast but oversmooth at large slice-thicknesses, while sampling-based methods improve fidelity at high inference cost. We propose DRIFT, a two-stage thickness-conditioned rectified flow framework for through-plane MRI super-resolution with continuous input slice-thickness. Stage 1 employs an Anatomical Projection Network (APN) to map low-resolution patches to a coarse high-resolution manifold, providing a deterministic anatomical initialization that shortens the residual transport of Stage 2 and stabilizes slice-wise refinement. Stage 2 refines details via rectified flow and introduces a Physics-Aware Difficulty (PAD) metric derived from slice-thickness induced through-plane bandwidth deficit to guide an Adaptive Integration Scheduler (AIS), allocating ODE steps by thickness. A Consistent Endpoint Trajectory Alignment (CETA) loss enforces thickness-consistent reconstructions. Experiments show that DRIFT outperforms super-resolution baselines while reducing inference cost. Code, models, and interactive demos are available at this https URL.

---


### 106. [VIGIL: Verifying Identity via Gated Intermittent Likelihoods for Continuous Biometric Authentication](https://arxiv.org/abs/2607.16651)

**<font color=#1a73e8>作者：</font>** Aldridge Fonseca, Udayan Atreya, Amith Kamath Belman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Continuous multi-modal authentication has emerged as a necessity for securing modern environments against persistent threats. Existing temporal fusion techniques fail to identify a persistent attacker from a genuine user with poor signal strength. In this study, we propose VIGIL (Verifying Identity via Gated Intermittent Likelihoods for Continuous Biometric Authentication), a highly adaptive continuous authentication framework. We introduce configurable cross-modal fusion with per-modality weighting, enabling operators to select their choice of integration strategy. We improve temporal fusion using dual-state State Transition Machines (STM) with unidirectional transition matrices. A three-zone verification decision model that enables multi-round verification when evidence is inconclusive is used in combination with an adaptive shrinking verification window. Monotonic decay, backflow elimination and analytical evaluation demonstrate that the proposed framework effectively addresses the limitations of existing approaches and reduces the time to detect intrusions while maintaining high usability for legitimate users.

---


### 107. [Position: Explanation Stability Is a Property of the Model Method Pair, Not the Model](https://arxiv.org/abs/2607.16652)

**<font color=#1a73e8>作者：</font>** Kabilan Elangovan, Daniel Ting  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This position paper argues that claims about explanation stability are scientifically invalid without cross method validation. Just as statistical significance requires the test statistic to be specified, stability should either be evaluated across multiple attribution paradigms or explicitly scoped to the computational objective of a single method. In controlled chest X ray experiments, DenseNet201, ResNet50V2, and InceptionV3 achieved AUC values above 99%, yet their stability rankings reversed across attribution methods. LayerCAM ranked InceptionV3 as the most stable model, with an IoU of 0.777, whereas GradCAM++ favored DenseNet201 and reduced InceptionV3 stability score by 17.3%. These findings demonstrate that explanation stability is an emergent property of the model method pair rather than an intrinsic characteristic of the model alone. We therefore argue that explanation based claims should be validated across multiple attribution methods and that regulatory submissions should explicitly specify the attribution operators used to avoid creating illusory safety assurances.

---


### 108. [DORS: Dynamic Attention Routing for Diffusion-based Object Removal in Dense Scenes](https://arxiv.org/abs/2607.16656)

**<font color=#1a73e8>作者：</font>** Haitong Tang, Haipeng Liu, Yang Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object removal aims to eliminate target objects specified by a mask while preserving visual consistency with the surrounding regions. Existing methods typically rely on contextual information from surrounding regions. However, in dense scenes where the surrounding regions contain instances visually similar to the removal target, such reliance often leads to semantic interference, resulting in incomplete removal. This problem arises from erroneous information propagation in the attention space, where masked queries tend to align with such instances due to global similarity matching in self-attention. To address this challenge, we propose a Diffusion-based Object Removal framework for dense Scenes, dubbed DORS, built upon a Dynamic Attention Routing mechanism comprising two complementary components: Instance-Filtered Attention (IFA), which suppresses misleading semantic information from similar instances through dynamically constructed mask-guided attention constraints, and Context-Guided Routing (CGR), which dynamically routes complementary scene information to maintain visual consistency. We further introduce DOR-Bench, a benchmark tailored for object removal in dense scenes. Extensive experiments demonstrate that DORS outperforms state-of-the-art methods, particularly in reducing incomplete removal and duplicate artifacts. The code will be available at this https URL.

---


### 109. [OpenLanguageModel: Readable and Composable Small-Language-Model Pretraining for Education and Research](https://arxiv.org/abs/2607.16669)

**<font color=#1a73e8>作者：</font>** Tavish Mankash, Vardhaman Kalloli, Keshava Prasad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> OpenLanguageModel (OLM) is an open-source PyTorch library for building and pretraining small language models while keeping their machinery visible. In OLM, model code reads like the architecture: components are ordinary modules, while Block, Residual, Repeat, and Parallel describe how they are wired. The resulting model can move unchanged from a teaching notebook to a complete pretraining run or a research ablation. OLM connects this readable model layer to tokenizers, local and streaming datasets, optimization, mixed precision, callbacks, checkpoints, and hardware-aware CPU, single-GPU, and single-node multi-GPU execution. We demonstrate the full path by tracing GPT-2 from diagram to code, launching a FineWeb-Edu training script, replacing one attention component, and letting AutoTrainer configure the available machine. The package includes 27 presets across nine familiar model families and documentation that progresses from LM fundamentals to architecture research. Validation shows close agreement with independent reference implementations, 90.6% four-GPU weak-scaling efficiency for a 348M-parameter workload, compact architecture edits, and positive early usability results. OLM is MIT-licensed and available through PyPI, GitHub, and its documentation site.

---


### 110. [Foundation-Assisted Active Learning for Object Detection Annotation](https://arxiv.org/abs/2607.16671)

**<font color=#1a73e8>作者：</font>** Jinchang Zhang, Arnold Zumbrun, Jing Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The annotation cost for remote sensing object detection is high, while existing active learning methods still face several challenges in object detection scenarios, including the coupling of localization and classification uncertainty, severe localization noise in the cold-start stage, and pseudo-diversity caused by high-recall candidate proposals. To address these issues, we propose a foundation-model-collaborative active learning and semi-automatic annotation framework for efficient construction of remote sensing object detection datasets. We build a dual-source mechanism consisting of a reference localization source (SA-source) based on UPN+SAM2 and a detector prediction source (OD-source), and further propose a Foundation-model-enhanced Dual-Source Uncertainty estimation to improve sample selection quality in the cold-start stage by jointly modeling localization consistency and classification confidence. Furthermore, we propose Object-Centric Diversity Sampling, which constructs object-level representations using DINOv2 features and SAM2 masks to improve sample coverage while suppressing pseudo-diversity. To address geometric noise in the semi-automatic annotation stage, we design Dual-Source Box Switching, which replaces noisy detector boxes with matched refined boxes from the SA-source, thereby reducing the manual burden of box refinement. Experiments on DIOR, HRSC2016, DOTAv2, and FAIR1M show that our method achieves superior or comparable results under most annotation budgets, with notably stronger cold-start sample efficiency in the low-budget regime.

---


### 111. [SpecLA: Efficient Speculative Decoding for Linear-Attention Models](https://arxiv.org/abs/2607.16673)

**<font color=#1a73e8>作者：</font>** Zhibin Wang, Xuying Han, Zhaohua Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear-attention models replace the growing KV cache with recurrent states, but autoregressive decoding still reads, updates, and writes these states one token at a time. Speculative decoding can reduce this cost by verifying several draft tokens in one target pass, yet existing speculative systems are designed for Transformer KV caches. For stateful linear-attention targets, verification must follow recurrent dependencies across chains and branches, acceptance must update only the accepted state trajectory, and the drafter must avoid submitting candidates that waste stateful verification work. This paper presents SpecLA, a speculative decoding runtime for stateful linear-attention models. SpecLA verifies chains and trees with topology-aware kernels, stores compact factors produced during verification to recover accepted states, and uses confidence pruning plus a target-aligned EAGLE-style drafter to feed useful candidates to the verifier. On an NVIDIA H100 with a public GDN-1.3B target, SpecLA achieves up to 1.70x end-to-end speedup over autoregressive decoding.

---


### 112. [CLDRoute: Conditional Latent Diffusion for Routability Map Generation in Physical Design](https://arxiv.org/abs/2607.16674)

**<font color=#1a73e8>作者：</font>** Kiran Thorat, Nicole Meng, Caiwen Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate routability estimation during physical design is important for reducing costly post-routing iterations. Prior learning-based methods treat this task as deterministic prediction, mapping placement-stage features to a single congestion or DRC outcome. We instead formulate routability estimation as a conditional generation problem, where both routing congestion and DRC violations are modeled as spatially structured routability fields. Our framework, Conditional Latent Diffusion for Routeability estimation (CLDRoute), uses physics-aware conditioning and task-specific latent modeling to handle the different characteristics of congestion and DRC maps. This allows our method to supports sample-based inference, producing both a mean prediction and a spatial uncertainty estimate for the same input design. On CircuitNet 2.0 (N28), our method achieves, for DRC violation generation, an SSIM of 0.9678, an MAE of 0.0028, and a TopK@1% of 0.3494; for congestion generation, it achieves an SSIM of 0.9031, an MAE of 0.0286, and an NZ-Pearson of 0.3692. Overall, our framework provides a more practical view of routability at placement by generating both the expected outcome and its uncertainty.

---


### 113. [A Framework for Early Sepsis Prediction via Self-Supervised (JEPA) and Federated Representation Learning](https://arxiv.org/abs/2607.16681)

**<font color=#1a73e8>作者：</font>** Umair bin Mansoor, Munaf Rashid, Roomi Naqvi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early sepsis prediction from electronic health records is challenged by irregular sampling, high missingness, and class imbalance. We systematically compare four modeling paradigms -- self-supervised Joint Embedding Predictive Architecture (JEPA) via masked latent prediction, self-supervised VICReg (variance-invariance-covariance regularization) with two-view augmentation, semi-supervised fine-tuning of a VICReg-pretrained encoder, and supervised Temporal Convolutional Network (TCN) -- alongside raw-feature baselines. All models share a common preprocessing pipeline of hourly binning with forward-fill imputation applied to 7 biomarkers selected via sparsity analysis from the MIMIC-III dataset. Our best model (JEPA + XGBoost + mean pooling) achieves AUPRC 0.636 at the time of onset (H0), approaching the SupMix benchmark (0.667) while using 83\% fewer biomarkers. The Tier 1 pipeline -- VICReg pretraining followed by semi-supervised fine-tuning and XGBoost -- achieves AUPRC 0.510 at H0, a 3.1$\times$ improvement over the raw-feature baseline (0.165) and a 7.6\% improvement over the end-to-end supervised TCN (0.474). Crucially, the fine-tuned VICReg encoder exhibits the most temporally persistent representations, degrading only 16.8\% from H0 to H10 compared to 47.5\% for supervised TCN and 65.3\% for JEPA, demonstrating that self-supervised pretraining with task-aware fine-tuning yields features that are both sharp near onset and robust across prediction horizons.

---


### 114. [Building a Neural Network from Scratch: Implementation, Evaluation, and Optimization](https://arxiv.org/abs/2607.16682)

**<font color=#1a73e8>作者：</font>** Yuanzhe Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of high-level deep learning libraries, while accelerating model development, has increasingly abstracted away the internal mechanics of neural networks, creating a gap between practical usage and fundamental understanding. To address this, the paper presents a self-contained neural network framework implemented entirely from scratch -- without relying on automatic differentiation or pre-built deep learning modules. The implementation encompasses all essential components, including multi-layer architectures, diverse activation functions, regularization techniques, and state-of-the-art optimizers. Beyond serving as a pedagogical instrument that demystifies forward/backward propagation, gradient dynamics, and optimization landscapes, the framework demonstrates robust performance when applied to a multi-class classification task, successfully validating its correctness, numerical stability, and generalization across varied configurations. The extensible design and clean modularity further position it as a reliable baseline for educational purposes and future research exploration.

---


### 115. [OFD-Net: Teacher-Free Reliable Semi-supervised Medical Image Segmentation with Orthogonal Feature Disentanglement Net of Foreground-Background](https://arxiv.org/abs/2607.16705)

**<font color=#1a73e8>作者：</font>** Shao-feng Jiang, Zhe-yang Jing, Qin Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised learning (SSL) is an effective solution for medical image segmentation with limited annotations. Existing SSL methods mainly rely on pseudo-labels generated by teacher-student supervision or cross-network consistency. However, these methods lack an explicit structural reference for judging pseudo-label quality. Low-quality pseudo-labels may lead to unreliable training, error accumulation and confirmation bias when processing unlabeled data with substantial appearance variations. To address this issue, we proposed OFD-Net, a teacher-free single-network framework for reliable semi-supervised medical image segmentation. OFD-Net employs an Orthogonal Feature Disentanglement Module (OFDM) to capture OFD features for reliable SSL by disentangling unlabeled data into background and foreground representations with a reliable structural distribution, thereby effectively reducing error accumulation and alleviating confirmation bias among unlabeled data. Specifically, OFD-Net explicitly employs a Disentanglement Guidance Module (DGM) to inject the resulting structural priors of foreground-background into the decoder by deformable convolution processing, and outputs predictions with clearer foreground representations. Based on DGM and the OFDM, we further develop a reliability-aware pseudo-label learning mechanism that evaluates unlabeled supervision according to the structural consistency between the main prediction and the disentangled foreground-background responses, and then down-weights unreliable regions during training. Extensive experiments on four public medical image segmentation benchmarks, namely ISIC-2016, Kvasir-SEG, Synapse, and ACDC, validate the effectiveness of OFD-Net. These results confirm that orthogonal foreground-background disentanglement enables OFD-Net to establish an efficient and reliable training paradigm within a teacher-free single-network framework.

---


### 116. [Laplacian Spectral Shaping for Non-Uniform Scaling Formation Control of Open Multi-Agent Systems](https://arxiv.org/abs/2607.16709)

**<font color=#1a73e8>作者：</font>** Tao He, Gangshan Jing  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Non-uniform scaling control enables a multi-agent formation to adjust its shape by compressing or stretching independently along different coordinate axes through inter-agent interactions, offering high flexibility in complex environments. The fundamental idea is encoding the desired formation shape as the kernel of a matrix-valued Laplacian. In open multi-agent systems, however, changes in number of agents, number of edges, and leader selection dynamically alter this Laplacian, destroying the required spectral properties: positive semidefiniteness, correct kernel, and positive definiteness of the follower block (we summarize these properties as the formation spectrum). In this paper, we develop distributed protocols to strategically adjust partial weights of the Laplacian matrix for formation control in arbitrary dimensional space. By implementing the protocols, the desired formation spectrum can be preserved under dynamic topology changes including agent joining, edge addition, agent leaving, and edge removal, while any pair of agents can serve as leaders. Unlike existing Laplacian design methods for affine formation control under topology changes, the proposed approach requires a sparser sensing graph, avoids a predefined parent-child hierarchical structure, and supports leader reassignment. The effectiveness of the proposed protocols is validated through both theoretical analysis and numerical simulations.

---


### 117. [Tractable Query Answering under Epistemic Confidentiality Policies in DL Ontologies (extended version)](https://arxiv.org/abs/2607.16715)

**<font color=#1a73e8>作者：</font>** Lorenzo Marconi, Daniela Rieti, Riccardo ROsati  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study Controlled Query Evaluation (CQE), a declarative approach to confidentiality-preserving data access, in the context of Description Logic (DL) ontologies, and for confidentiality policies expressed through Epistemic Dependencies (EDs). We first address the problem of answering queries (specifically, Boolean unions of conjunctive queries) under known semantics for CQE (GA- and IGA-entailment). Our results show that if the TBox is expressed in $\text{DL-Lite}_{\mathcal{R}}$, CQE is computationally intractable in general. Moreover, in the presence of EDs, the IGA semantics has recently been proven not to satisfy an important confidentiality preservation property known as indistinguishability. With the goal of defining computationally easier and confidentiality-preserving forms of CQE, we introduce a new semantics for CQE, based on the notion of minimal policy violation (MPV). We show that the new semantics provides a sound approximation of the previous ones, while satisfying the indistinguishability property. We also prove that, in the case of $\text{DL-Lite}_{\mathcal{R}}$ ontologies, query entailment under the MPV semantics can be decided in polynomial time in data complexity. Finally, we present a software implementation of our framework that we used to evaluate the feasibility of this new approach using an existing benchmark for OWL 2 QL.

---


### 118. [RECON: Benchmarking Agent Memory for Compositional Reasoning over Long Contexts](https://arxiv.org/abs/2607.16716)

**<font color=#1a73e8>作者：</font>** Mihir Shriniwas Arya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models and LLM-based agents are widely used as personal chat assistants, enterprise copilots, and autonomous workflow agents. In all these applications, memory (the ability to retain, access, and reason over information accumulated over long contexts and multiple interactions) plays a crucial role in determining the reliability of any agent. We introduce RECON (Reasoning over Extended Contexts with Obfuscated Narratives), a benchmark for evaluating compositional reasoning over long contexts. RECON spans 24 case files across three domains (criminal, medical, and financial), each ranging from 50k to 100k tokens, and tests agents on six memory intensive tasks: reconstructing multi-hop evidence chains, propagating cascading invalidations, resolving source conflicts, counterfactual reasoning, satisfying temporal constraints, and temporal fact retrieval. Recent memory benchmarks evaluate whether agents can retrieve scattered facts or detect if a fact has changed whereas RECON evaluates what happens after the change, whether agents can trace which downstream conclusions are affected, which survive through independent support, and how alternative timelines would have unfolded. Our evaluation reveals substantial limitations across current architectures: even the strongest non-Oracle system reaches only 22.4% Accuracy, with retrieval and reasoning each surfacing as challenges.

---


### 119. [Effects of width-dependent model hyperparameters and $\ell_2$-regularization on the loss landscape of two-layer ReLU networks](https://arxiv.org/abs/2607.16720)

**<font color=#1a73e8>作者：</font>** Haruka Eshima, Makoto Yamada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding deep neural networks remains a central challenge in machine learning. In particular, the theoretical properties of even two-layer ReLU networks, especially in the presence of weight decay, remain poorly understood. To this end, we derive a sufficient condition on the hyperparameter settings under which the global minima collapse to the zero solution. Interestingly, our experiments reveal that using AdamW as an optimizer prevents the collapse of the learned parameters, whereas using SGD does not, which may help explain the success of AdamW in deep learning training. In addition, when restricting the input dimension to one, we derive an analytical solution for the globally optimal parameter sets of two-layer ReLU networks and show that $\ell_2$-regularization has a width-invariant effect on connectivity, but its dimensionality-reducing effect becomes stronger as the network width increases. These results provide insight into how width-dependent hyperparameters influence the geometry of regularized loss landscapes.

---


### 120. [Graph-Embedded Intuitionistic Fuzzy Broad Learning System: A Multi-view Framework](https://arxiv.org/abs/2607.16728)

**<font color=#1a73e8>作者：</font>** Yogesh Kumar, Manju, Mudasir Ganaie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Broad Learning System (BLS) has been widely used for data classification and is based on a layer-by-layer feed-forward structure. However, it gives the same importance to all data points, which reduces its effectiveness on real-world datasets with noise and outliers. In addition, it does not consider the geometric structure of the data and has limitations in handling data from multiple sources. To address these challenges, we propose a Multi-View Graph-Embedded Intuitionistic Fuzzy Broad Learning System (MVGIFBLS) that integrates multi-view learning, graph embedding, and intuitionistic fuzzy theory into the BLS framework. This design enables the model to combine information from multiple sources and learn more discriminative representations. Graph embedding captures the geometric relationships among samples and improves class separation through intrinsic and penalty subspaces based on local Fisher discriminant analysis. Intuitionistic fuzzy theory enhances robustness to noise, while kernel-based neighborhood analysis captures local data structures. We evaluate the proposed framework on several UCI, KEEL, and AwA benchmark datasets using comparative evaluation, Gaussian feature noise analysis, ablation studies, and statistical analysis. The results demonstrate that each component contributes positively to the overall framework and that the proposed MVGIFBLS consistently achieves higher Area Under the Curve (AUC) scores and maintains robust performance under Gaussian feature noise.

---


### 121. [BG4Sea: Biogeochemical Seasonal Forecastability via Progressive Information Scaling](https://arxiv.org/abs/2607.16731)

**<font color=#1a73e8>作者：</font>** Gabriela Martinez Balbontin, Anastase Charantonis, Dominique Bereziat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Marine biogeochemical forecasting is increasingly important for managing marine ecosystems and the carbon cycle, yet global, seasonal forecast products lag far behind physical oceanography, held back by the complexity of the processes involved and by data scarcity. We introduce BG4Sea, which to our knowledge is the first global, data-driven system to produce multivariate seasonal forecasts of the marine biogeochemical state. BG4Sea is a modular architecture with a column autoencoder that compresses the vertical column into a low-dimensional latent space, a latent forecaster propagates this representation forward in time, a surface-forcing conditioner that injects physical boundary information via Feature-wise Linear Modulation (FiLM), and a horizontal-coupling module that incorporates neighboring-column context through cross-attention. The model is trained and evaluated on the global ocean reanalysis BIORYS4 (NEMO/PISCES), and produces six-month forecasts at 1/4 degree, monthly resolution for dissolved chemistry, biology, and carbon-pool variables, outperforming persistence and climatology across most variables and lead times. We position BG4Sea as an interpretable baseline for future, more expressive approaches, and discuss predictability attribution to each component, alongside the model's structural limitations.

---


### 122. [Supporting Autonomous Process Execution within a Multi-Perspective Constraint Frame via Numeric Planning](https://arxiv.org/abs/2607.16738)

**<font color=#1a73e8>作者：</font>** Paul Wittlinger, Giacomo Acitelli, Anti Alman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-Augmented Business Process Management Systems (ABPMS) enhance traditional BPMS by leveraging advanced AI techniques to define, execute, and monitor complex process structures. Within this landscape, Framed Autonomy denotes the capability of a system to autonomously advance the execution of a Business Process (BP) instance while strictly adhering to a predefined frame, i.e., a set of constraints that may span multiple perspectives. Existing research on framed autonomy has predominantly focused on control-flow constraints, either declarative or procedural, and typically relies on their transformation into automata-based representations. In this study, we extend this line of work by introducing a novel tool for what-if analysis that augments the process frame with multi-perspective constraints, including data-aware and temporal conditions. Given a partial process execution, the proposed approach exploits this enriched frame to recommend optimal continuations in compliance with the underlying process specifications. We additionally report an empirical evaluation demonstrating the scalability and effectiveness of the technique, thereby highlighting its potential for supporting autonomous and constraint-aware decision making in ABPMS.

---


### 123. [Retrofitting Existing 3D Objects with Surface-Conforming Capacitive Sensing](https://arxiv.org/abs/2607.16739)

**<font color=#1a73e8>作者：</font>** Andela Ilic, Junpeng Gao, Zhipeng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Augmenting the surface of 3D objects with capacitive sensing is challenging when their volumes cannot be modified. In this paper, we present a generative computational fabrication pipeline that retrofits surface-only sensor layouts to 3D geometries for multi-touch interaction. Our method scans a real-world object to obtain its 3D mesh, generates and optimizes a 3D sensor design of drive and sense lines for mutual-capacitance sensing under physical and hardware constraints, and unfolds the design into individual 2D stencils that can be cut from conductive material. Our fabrication pipeline cuts these stencils from thin copper foil with a vinyl cutter and then assists manual sensor attachment by projecting the sensor design onto the dynamically registered real-world object. We connect the resulting electrode mesh to a mutual-capacitance scanning controller and resolve touch interaction in real time. We demonstrate our approach with four 3D geometries and evaluate our method and fabrication pipeline on them.

---


### 124. [RELIC: Revealed Principles for Learning Interpretable Composable Skills in Multi-Agent Planning](https://arxiv.org/abs/2607.16745)

**<font color=#1a73e8>作者：</font>** Nguyen Viet Tuan Kiet, Bui Dinh Pham, Duong Quoc Chinh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent planning becomes substantially harder when agents must improve specialized decision-making skills while keeping their internal implementations private. This regime arises when agents are developed independently, expose different interfaces and capabilities, and must nevertheless coordinate without sharing executable policies. Prior research has largely assumed centralized optimization, shared policy access, or common skill representations, making it poorly suited to privacy-constrained cooperation. We introduce RELIC, a framework for learning interpretable and composable skills via revealed principles. Each agent refines its own programmatic skill through private LLM-guided search, while a trusted orchestrator evaluates proposed updates solely through team-level performance. Successful behaviors are not broadcast as code; instead, they are abstracted into portable principles that other agents can instantiate within their own interfaces and recombine with local strategies. This separates coordination from implementation sharing, enabling cross-agent transfer under heterogeneous skill signatures. RELIC thus introduces a new paradigm for privacy-preserving skill learning and coordination in multi-agent planning.

---


### 125. [VisionAssist: An Open-Source Smartphone Assistant for AI-Based Visual Accessibility](https://arxiv.org/abs/2607.16750)

**<font color=#1a73e8>作者：</font>** Ayşe Özlem Çalışkan, Jordi Sanchez-Riera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> People with low vision often face challenges in performing everyday tasks that require interpreting visual information. We present \textbf{VisionAssist}, an open-source mobile application designed to improve independence by providing AI-powered visual assistance through a smartphone. The application integrates three complementary functionalities within a single interface. First, it enables users to locate specific objects by analyzing the live camera feed. Second, it generates spoken descriptions of captured images, allowing users to identify visual content such as food labels, documents, and everyday objects. Third, it integrates with the smartphone's contacts and calendar to facilitate emergency calls and provide voice-based reminders. The application supports hands-free interaction through voice commands and delivers all feedback using text-to-speech synthesis, making it fully accessible to users with visual impairments. By combining multiple assistive services into a unified platform and releasing the project as open-source software, the proposed solution aims to encourage community contributions and accelerate the development of accessible technologies. The source code is publicly available at: this https URL

---


### 126. [Hybrid Machine Learning for Articulation Angle Estimation of Truck-Semitrailer Combinations](https://arxiv.org/abs/2607.16758)

**<font color=#1a73e8>作者：</font>** Qixuan Zhang, Jonas Boettcher, Simon F. G. Ehlers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate articulation angle estimation of trucks with trailers is critical for autonomous driving and advanced driver assistance system (ADAS). Existing methods either require manual initialization, additional sensors, or prior knowledge and signals from trailers, or they lack real-world validation, limiting practical deployment. This paper presents multiple learning-based models to directly estimate articulation angles from visual and kinematic inputs, eliminating the need for dedicated driving maneuvers for initialization, bounding box annotations, trailer-mounted sensor signals, or prior knowledge of trailer parameters. Two learning-based models are integrated with a kinematic model within an extended Kalman filter (EKF) framework, and an adaptive weighting scheme based on uncertainty quantification is applied for measurements involving visual input. Extensive real-world experiments with different trailer types demonstrate the approaches' robustness and generalization under out-of-domain conditions, including new trailers, varying colors, and lighting conditions. Results show that the hybrid method achieves accurate and reliable articulation angle estimation while maintaining reduced implementation requirements and practical deployment advantages.

---


### 127. [Spatiotemporal Facial Action Unit Detection using Twin Cycle Autoencoders for Driver Monitoring](https://arxiv.org/abs/2607.16760)

**<font color=#1a73e8>作者：</font>** Sai Sidharth D  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driver monitoring systems (DMS) increasingly rely on facial cues to infer drowsiness, distraction, and cognitive load in real time. Facial Action Units (AUs), grounded in the Facial Action Coding System (FACS), provide an objective and interpretable representation of such states, but their automatic detection in the driving context is complicated by low and variable illumination, partial occlusion, head-pose variation, and the subtlety and short duration of relevant AU activations. Existing AU detectors largely treat spatial appearance and temporal dynamics separately, limiting their ability to exploit self-supervisory signal from abundant unlabeled driving video. We propose the Twin Cycle Autoencoder (TCA), a spatiotemporal architecture composed of two coupled cycle-consistent autoencoder branches: a Spatial Cycle Autoencoder that disentangles AU-relevant appearance from identity through image-level cycle consistency, and a Temporal Cycle Autoencoder that enforces forward-backward consistency over latent AU trajectories to capture onset-apex-offset dynamics. The two branches are coupled through a cross-branch latent alignment loss and fused via an attention module before multi-label AU classification. We evaluate TCA on the DISFA and BP4D benchmarks and on an in-cabin naturalistic driving dataset, and observe consistent improvements over CNN-RNN, 3D-CNN, and graph-based AU baselines, particularly for low-intensity and rapidly transitioning AUs relevant to fatigue (AU45, AU43) and yawning (AU26). We further show the model sustains real-time throughput on an embedded Jetson Xavier NX platform, supporting its use in production-grade advanced driver assistance systems (ADAS).

---


### 128. [When Is Heterogeneous Distance-Decay Facility Location Tractable? A Structural Classification, Exact Methods, and a Real-World Study](https://arxiv.org/abs/2607.16764)

**<font color=#1a73e8>作者：</font>** Zhou He, T.C.E. Cheng, Jichang Dong  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study continuous planar facility location in which a demand point's captured value decays with distance, with the per-point decay scale varying across points. This heterogeneity is ubiquitous yet underexploited, and one nearest-facility objective unifies decay, clustering, and median goals, containing k-means, the Weber/p-median problem, and maximum covering as special cases. We make four contributions. (i) A tractability classification: the discrete objective is always monotone submodular, so the (1-1/e) greedy guarantee holds regardless of decay shape or heterogeneity, and the continuous cooperative objective is concave if and only if the decay is concave in distance; the clip max(0,d) in common coverage specifications is what destroys concavity, and the classification is tight. (ii) An exact discrete method: the candidate-discretized maximum-cover MIP has an empirically tight LP relaxation (~0% gap) and is solved by branch-and-bound in seconds for n <= 500. (iii) A force-as-gradient / large-neighborhood-search heuristic, within 0.5% of the discrete optimum, that outperforms the (1-1/e) greedy, Cooper-style alternating location-allocation, particle swarm optimization, and weighted k-means (30/30 per-instance wins at K=30, p<10^-9) and is competitive with bespoke solvers on k-means, Weber/p-median, and shape-demand instances. (iv) A real-world study: on 592,667 urban-delivery orders, ignoring the calibrated decay variation loses up to 9.7% of captured demand and relocates facilities by up to 37% of the map; a retail dataset calibrates the decay as exponential with scale R ~ 1.4 km.

---


### 129. [Robust Losses from Univariate Base Functions for Noisy-Label Learning](https://arxiv.org/abs/2607.16768)

**<font color=#1a73e8>作者：</font>** Peng Hu, Jianwei Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning with noisy labels is a fundamental problem in training reliable deep neural networks. Robust loss functions provide a direct and effective way to mitigate the adverse effects of label noise. However, most existing robust losses are designed directly at the level of the final multiclass objective, which makes it difficult to systematically characterize and extend their robustness properties. In this paper, we propose a general framework that constructs robust multiclass losses from univariate base functions. By defining mapping operators from base functions to multiclass losses, the robustness of the induced losses can be characterized through simple properties of the base functions. We develop two complementary construction schemes, Target Separation and Binary Reduction, corresponding to inter-class independent and inter-class dependent formulations, respectively. For both schemes, we analyze their symmetry and asymmetry properties and derive corresponding sufficient conditions, which provide theoretical criteria for noise-robust loss design. The proposed framework also provides a new route to constructing symmetric losses, serving as a complement to normalization-based symmetric loss designs. Extensive experiments on synthetic and real-world noisy-label benchmarks demonstrate that the proposed losses achieve competitive or superior performance under various noise settings.

---


### 130. [On the Potential of Graph Neural Networks as Metamodels for Supply Chain Optimization: Dataset, Architectures, and Directions](https://arxiv.org/abs/2607.16769)

**<font color=#1a73e8>作者：</font>** Tushar Lone, Neha Karanjkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have emerged as a powerful, differentiable class of learning models for graph-structured systems. Their ability to generalize across topologies opens the prospect of a surrogate for combined structural and parametric optimization, which classical metamodels cannot offer. Supply chains are a natural target, yet the use of GNN surrogates for supply chain problems is largely unexplored. This paper lays the foundation, presents initial steps, and discusses key research directions. As a foundation, we formulate the problem and create a large public training dataset of programmatically generated supply chain graphs with input parameters and steady-state performance metrics obtained using our SupplyNetPy simulation library. As initial steps, we explore GNN architectures that work well as surrogates for node- and network-level predictions, and analyze their accuracy-compute trade-off against simulation. Most importantly, we outline the exciting directions this opens, namely gradient-based optimization over topology, fast design-space exploration, and sensitivity analysis.

---


### 131. [SABLE: Minimalist Instruction-Level Authenticated Encryption for Constrained Confidential Computing](https://arxiv.org/abs/2607.16771)

**<font color=#1a73e8>作者：</font>** Hamid Noori, Carlton Shepherd  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Conventional processor designs expose code and data as plaintext throughout execution, rendering them inherently vulnerable to attacks that recover intellectual property or modify security/safety checks. Instruction-level encryption (ILE) enables CPU-level decryption, execution, and optionally authentication of individual encrypted program instructions at runtime. However, existing proposals depend on specific micro-architectures, detect corrupted instructions after they have executed, rely on non-standard ciphers, or require complex analyses of program state. In this work, we introduce and present a design exploration of a RISC-V processor architecture (SABLE) that enables minimally invasive instruction-level authenticated encryption of programs. SABLE is agnostic to the underlying micro-architecture, remaining compatible with the standard RISC-V toolchain with minor changes to post-process compiled ELF binaries. We integrate a decrypt-and-verify stage at two points (the instruction-memory wrapper and the CPU frontend) and explore seven ILE micro-architectures from a single-cycle (combinational) design to six multi-cycle (sequential) variants. We implement and evaluate the designs using ASCON-128a on a Xilinx Artix-7 FPGA with the open-source NEORV32 system on chip. Relative to baseline performance, the configurations span LUT, performance, power, and energy-per-instruction overheads of 1.6-9.3$\times$, 4.1-10.0$\times$, 1.5-8.0$\times$, and 10.4-80.0$\times$, respectively, using the Dhrystone benchmarking suite. Finally, we discuss design trade-offs, highlighting area-, performance-, and energy-aware design points.

---


### 132. [HTT-Net: Hierarchical Text-guided Transition Modeling for Surgical Video Phase Recognition](https://arxiv.org/abs/2607.16787)

**<font color=#1a73e8>作者：</font>** Kunjie Deng, Jinghui Zhang, Weidong Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical video phase recognition is a fundamental task in computer-assisted intervention, supporting workflow understanding, intraoperative guidance, and surgical quality assessment. Although recent visual-temporal models have achieved promising progress, accurate and temporally coherent phase recognition remains challenging due to local visual ambiguity, transient prediction noise, and insufficient use of procedural semantics. To address these challenges, we propose HTT-Net, a Hierarchical Text-guided Transition modeling Network for surgical video phase recognition. The key idea is to introduce structured surgical semantic knowledge into phase-aware segment construction and semantic refinement. Specifically, we construct a hierarchical surgical semantic memory with intra-phase descriptions, inter-phase transition descriptions, and fine-grained semantic units. Based on this memory, the proposed Transition-Aware Segment Construction (TAS-Con) organizes frame-level evidence into coherent segment representations and handles boundary clips with inter-phase transition descriptions. Furthermore, we introduce Transition-Aware Segment Calibration (TAS-Calib), which calibrates phase-aware segment representations through hierarchical surgical semantics and improves discrimination under visual ambiguity without dense frame-level vision-language fusion. Experiments on Cholec80 and LCRS-100 demonstrate the effectiveness of HTT-Net for robust surgical video phase recognition.

---


### 133. [Cascading versus Joint Modeling for Hierarchical Offensive Language Detection](https://arxiv.org/abs/2607.16790)

**<font color=#1a73e8>作者：</font>** Ruixing Ren, Junhui Zhao, Xiaoke Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-grained offensive language detection organizes labels into a hierarchical structure, for which two modeling paradigms exist: cascaded decomposition and joint multi-task modeling. Prior work rarely provides a direct, controlled comparison of the two paradigms in terms of accuracy, parameter count, and inference latency, and rarely verifies whether a chosen class-imbalance handling strategy is actually optimal. This paper proposes a three-level cascaded detection system whose training strategy is customized per subtask, together with two verification mechanisms. First, a controlled ablation study determines the best class-imbalance handling strategy for each subtask. Second, a joint multi-task model with a shared encoder is trained as an architectural control, yielding real measurements along the dimensions of accuracy, parameter count, and inference latency. Experiments show that the cascaded system attains macro-F1 scores of 0.795, 0.716, and 0.557 on the three subtasks of the official test set. The ablation study reveals that configuring the loss function purely by imbalance-severity intuition is suboptimal; reconfiguring based on the ablation results improves both performance and stability. End-to-end cascade evaluation shows that roughly one-fifth of the errors in the cascade pipeline originate from the first-stage filter and cannot be corrected by subsequent stages. Relative to the joint multi-task model, the cascaded architecture achieves higher accuracy on all three subtasks, with a 7.1-point macro-F1 gain on the most severely imbalanced subtask, at the cost of three times the parameters and 1.67 times the inference latency. Together, these results establish an explicit, quantifiable trade-off between the accuracy advantage of cascaded architectures and their deployment cost.

---


### 134. [Diagnosing Correctness Probes under Self-Judgement Confounding](https://arxiv.org/abs/2607.16799)

**<font color=#1a73e8>作者：</font>** Yi-Long Lu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hidden-state readouts can predict whether language-model outputs are correct, but objective correctness (OC) usually agrees with the model's own self-judgement (SJ), leaving the decoded signal semantically ambiguous. We construct conflict cases in which OC and SJ predict opposite readout orderings. On high-confidence disagreements, conventional correctness-labelled contrasts often rank incorrect/self-endorsed responses above correct/self-rejected responses, following SJ rather than OC. We estimate factorial SJ- and OC-associated directions and evaluate their polarity across mathematical reasoning and factual recall. Across four instruction-tuned models up to 14B parameters, the SJ-associated direction transfers above chance in both cross-domain directions for every model, whereas the OC-associated direction has a below-chance point estimate for the expected OC ordering in every corresponding condition. This transfer asymmetry develops across middle-to-late layers, persists under answer-likelihood, sequence-length, and null-direction controls, and extends to MMLU and binary TruthfulQA without target-domain direction fitting. Across the studied models and diagnostic subsets, the most reliably transferable component preserves SJ-associated polarity. Transferability alone therefore does not establish objective-correctness semantics.

---


### 135. [Value-Monotonicity Matters: A Concordance Loss for Deep Survival Prediction](https://arxiv.org/abs/2607.16802)

**<font color=#1a73e8>作者：</font>** Meixu Chen, Kai Wang, Jing Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep survival models are evaluated almost exclusively by the concordance index (C-index), yet they are commonly trained using likelihood objectives such as the Cox partial likelihood, discrete-time negative log-likelihood, and DeepHit likelihood. This mismatch is usually considered acceptable because the C-index can be recomputed on validation data during training. However, for end-to-end training of high-capacity encoders on small, heavily censored oncology cohorts, frequent C-index evaluation is computationally expensive, making the loss value itself an important signal for monitoring, early stopping, and model selection. We show that likelihood losses are unreliable for this purpose and propose a value-monotone concordance loss. We prove that every strictly proper survival likelihood admits directions where the loss decreases while the C-index remains unchanged, causing the loss value to decouple from ranking performance. We then study a sigmoid concordance loss (SCL), whose value approximates one minus the C-index up to a temperature term, ensuring that lower loss corresponds to higher C-index during optimization. The loss is architecture agnostic and reduces to a convex survival ranking support vector machine for linear models. Across eighteen datasets from four modalities using a unified five-fold cross-validation protocol, SCL achieves discrimination comparable to standard likelihood losses and is the best or within one standard deviation of the best C-index. Unlike likelihood losses, SCL maintains a strong correlation between loss value and C-index during training, with rank correlations of 0.96 to 0.99 compared with -0.03 to 0.53 for likelihood losses. Calibration measured by the integrated Brier score is comparable. SCL provides a value-monotone optimization objective whose value can serve as a reliable surrogate for the C-index during expensive end-to-end training.

---


### 136. [Interpretable Anomaly and Drift Detection with Gaussian Mixture Models](https://arxiv.org/abs/2607.16811)

**<font color=#1a73e8>作者：</font>** Behnam Asadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We revisit Gaussian Mixture Models (GMMs) as a lightweight, interpretable tool for anomaly detection and, in particular, for detecting distributional drift in data streams. We make three practical choices explicit and evaluate them on seven public benchmarks. First, the number of mixture components is selected automatically by the Bayesian Information Criterion, initialised by k-means, removing the need to fix it in advance. Second, individual observations are scored by their negative log-likelihood under a GMM fitted to normal data, with thresholds set at a target false-alarm rate using Extreme Value Theory. Third, the same interpretable model extends to distributional drift: each Gaussian component is a named "regime," and the fraction of a stream window that matches no regime -- its unexplained mass -- is a drift signal that is itself the explanation. We benchmark this against a model-free kernel two-sample test (Maximum Mean Discrepancy, MMD) and against two GMM-to-GMM divergences (a closed-form Cauchy-Schwarz divergence and a matching-based KL surrogate). Across seven benchmarks ranging from 3 to 64 dimensions and five random splits, the GMM point detector is competitive with -- though rarely more accurate than -- Isolation Forest, Local Outlier Factor, one-class SVM, ECOD, COPOD and an autoencoder, while uniquely yielding an interpretable model. For drift, MMD is the strongest pure detector, but the interpretable unexplained-mass statistic matches it when anomalies form novel regimes (and honestly fails, as MMD does not, when drift is a pure re-weighting of existing regimes). Every alarm is explainable: anomalies lie a median of 3-10 sigma outside their nearest regime vs. about 1 sigma for normal points, and a drift alarm reports the fraction of the window matching no known regime. All code and experiments are released.

---


### 137. [Honest Physical-Support Inference after Latent Dictionary Learning: Collision Singularities and Minimax Resolution](https://arxiv.org/abs/2607.16813)

**<font color=#1a73e8>作者：</font>** Guan-Ju Peng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse-support uncertainty is usually quantified by treating the dictionary as known, an assumption that can produce overconfident, label-dependent conclusions when the dictionary is learned from latent sparse mixtures. Near collisions of coherent atoms, a test signal may identify the active physical group even though the training data cannot distinguish the physical rays within it.
We develop inference for active physical rays, unit atoms modulo sign, after latent dictionary learning. In a fixed-dimensional Gaussian train-test experiment, we retain all dictionaries compatible with a robust training-moment region, profile the test representation over them, and project surviving configurations onto a permutation-invariant support space. The resulting confidence correspondence can report cross-sheet inconclusiveness, group resolution with child ambiguity, or fine-support resolution.
We characterize both its statistical cost and decision-theoretic benefit. Residual block orientation first affects the latent training density at cubic order, yielding information of order $s^6$, where $s$ is the within-block collision scale. The correspondence provides high-probability-over-training conditional test coverage, with resolution governed separately by parent detectability, test-time support separation, and learned-dictionary orientation. In the resolved fixed-shell regime, its projective Hausdorff diameter contracts at the minimax-optimal rate $s \wedge (\sqrt{N}s^2)^{-1}$, up to constants. A restricted-task theorem further determines when coefficient asymmetry allows test replication to supplement training information and when calibration uncertainty remains irreducible. The framework thus yields honest, resolution-adaptive support statements and guides the allocation of training versus test measurements.

---


### 138. [Test-Time Registers as Global Priors for Tokenized Image Generation](https://arxiv.org/abs/2607.16824)

**<font color=#1a73e8>作者：</font>** Cheng-Yao Hong, Yifan Wang, Yuewei Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attention-based models often develop attention sinks, where a small number of tokens repeatedly attract attention and accumulate unusually large activations. In vision transformers, these outliers are closely related to registers, which have been diagnostically linked to global, low-frequency image structure. Existing work has largely studied registers through interpretability analyses and linear probes, leaving open whether they can be operationalized as plug-and-play signals for generation without retraining. We revisit this question in tokenized image generation. Using OpenCLIP and DINOv2 on ImageNet, we find that test-time register features exhibit stronger low-frequency concentration than both [CLS] readouts and patch-mean features, and show a consistent (albeit moderate) correlation with pixel-space DCT low-frequency energy. Motivated by these diagnostics, we introduce RegToken, a training-free procedure that converts register structure into a small set of global prior tokens by (i) NFN-based layer localization, (ii) TokenRank-guided subspace extraction, and (iii) a projection-and-conservation update on the register subspace. Inserted into a frozen compact 1D token generation pipeline, RegToken improves ImageNet generation and alignment metrics (e.g., FID-5k 20.5 to 20.1, SigLIP 3.6 to 3.9) without modifying pretrained weights, and accelerates test-time optimization (Steps@$\tau$ 74 to 52). Overall, our results suggest that structures often viewed as attention artifacts can be repurposed as lightweight global priors for tokenized generation.

---


### 139. [Spatially-Aware Class-Agnostic Object Counting](https://arxiv.org/abs/2607.16826)

**<font color=#1a73e8>作者：</font>** Robert Wijaya, Md. Tanvir Hossain, Amanda Kau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalised object counting aims to estimate the number of instances of an arbitrary object category from a single image, but many recent methods can struggle on structurally complex objects due to limited spatial modelling. We present \textit{UpCount}, a class-agnostic counter designed to better preserve spatial structure. UpCount strengthens the visual representation by extracting multi-layer features from a ViT-B/16 encoder and reassembling them into a refined multi-scale pyramid that is spatially refined using Dense Prediction Transformers and FeatUp, yielding features with improved structural and spatial sensitivity; a proposal--verification counting head then identifies repeated patterns and produces a density map for the final count. On FSC-147, UpCount achieves 12.39 MAE and 100.89 RMSE on the test set, and it transfers effectively to vehicle counting on CARPK (6.27 MAE, 8.79 RMSE). Code: this https URL

---


### 140. [Robust PnP on a Neuromorphic Processor for Object Pose Estimation](https://arxiv.org/abs/2607.16834)

**<font color=#1a73e8>作者：</font>** Tam Ngoc-Bang Nguyen, Mohsi Jawaid, Tat-Jun Chin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neuromorphic computing is gaining attention in robotic perception due to its higher energy efficiency. While neural network-based methods can more readily exploit the distributed and parallelized structure of neuromorphic computers, crafting neuromorphic solutions for non-learning tasks is less straightforward. This hampers the usage of neuromorphic computing for perception pipelines that depend on both learning and non-learning components, such as object pose estimation (OPE) where state-of-the-art methods use a deep network to predict 2D landmarks and nonlinear optimization to solve perspective-n-point (PnP). In this paper, we propose a novel neuromorphic-deployable formulation for robust PnP, where given outlier-prone 2D-3D correspondences, the object pose with the largest number of inliers is determined. Underpinning our method is a distributed algorithm for robust least squares estimation of rigid body pose that can be executed on a neuromorphic processor. We also design a spiking neural network (SNN) to predict 2D landmarks from event data, where the main layers of the SNN were designed according to the principles of spiking neurons. Overall, our work enables neuromorphic treatment of the major stages of an OPE pipeline, from event sensing and learned landmark prediction, to geometric optimization for robust PnP. Results on neuromophic hardware (Intel Loihi 2) indicate the higher energy efficiency our neuromorphic robust PnP, while achieving competitive accuracy.

---


### 141. [TopoGS: Planar Reconstruction via Topology-aware 3D Gaussian Splatting](https://arxiv.org/abs/2607.16838)

**<font color=#1a73e8>作者：</font>** Shanshan Pan, Jiale Chen, Yilin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extracting structured, parametric 3D representations from raw images remains a fundamental challenge in computer vision and graphics. While recent advancements in the 3D Gaussian Splatting (3DGS) pipeline integrate planar primitives to yield compact and editable geometry, these approaches typically treat planes as isolated, discrete sets. This lack of topological connectivity hinders robust geometric reasoning, leading to fragmented reconstructions and misaligned boundaries that fall short of the precision for rigorous spatial analysis and professional design workflows. To address this, we introduce TopoGS, the first 3DGS framework to explicitly integrate both planar and topological constraints for coherent 3D reconstruction. Specifically, we extract global 2D topological relationships from multi-view image segmentations and anchor Gaussian primitives to these structural elements. This formulation enables the joint optimization of plane parameters, rendering fidelity, and topological adjacency. By enforcing strict multi-view consistency alongside these topological constraints, our method significantly mitigates geometric misalignments and produces connected, structured 3D models. Extensive evaluations on the ScanNet++ dataset demonstrate that TopoGS achieves state-of-the-art performance, providing a highly robust solution for generating accurate, topologically sound, and visually faithful scene representations.

---


### 142. [From Overload to Insights: How AI Agents Can Support Scientists in Analyzing Complex Data](https://arxiv.org/abs/2607.16845)

**<font color=#1a73e8>作者：</font>** Tim Fuchs, Luca Gelisio, Steffen Hauf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientists at European XFEL conduct experiments that generate very large and complex datasets. The subsequent data analysis is challenging as scientists must combine their domain expertise with facility- and software-specific knowledge scattered across documentation, tools, and support channels. To address this problem, we designed and evaluated an agentic AI system tailored to the scientists' needs and integrated with the high-performance computing environment of European XFEL. Using a design science research approach, we conducted a rapid literature review, a systematic evaluation of 16 AI tools, multiple interviews, a focus group, and a user study with experts at European XFEL to develop and evaluate two prototypes. Our study identifies key knowledge challenges in scientific data analysis, derives requirements for an AI agent that supports knowledge retrieval and source code generation, and proposes design recommendations for a specialized system adaptable to the evolving AI tool landscape. These findings provide guidance for developing maintainable AI support in highly specialized scientific environments.

---


### 143. [Beyond Memory Leaderboards: Evaluating Scientific Memory as Budgeted Context Restoration](https://arxiv.org/abs/2607.16848)

**<font color=#1a73e8>作者：</font>** Maksim Sheverev, David Finkelstein, Sergey Nikolenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term memory is becoming a core component of LLM agents, but most memory benchmarks evaluate conversations or compact summaries, while research agents need to restore evidence from full scientific papers. We introduce two full-text scientific-memory benchmarks, Public AI Memory (PAIM; 81 papers, 66 questions) and Public Transformers (PTr; 252 papers, 98 questions). We evaluate eight memory/retrieval systems, including our own proposed Theoria, plus a no-retrieval baseline. Our results show that memory leaderboards are not interpretable without the full protocol: ingestion granularity, raw-text preservation, retrieval budget, retrieval modality, rubric audit, and judge choice all affect the outcome. For example, on PAIM Graphiti wins convincingly but uses 2.6M characters of retrieved context per query, and after controlling for retrieval budget the lead disappears. On PTr, for the systems where BM25 retrieval can be added cleanly, the sparse-dense hybrid is the single most significant intervention: hybrid variants of Simple RAG, Mem0, and Theoria tie for the lead within 0.03 points. Multi-judge and human side-by-side calibration show that LLM-as-a-judge rankings are consistent across frontier judges and agree with human evaluation, with an effective resolution of roughly one point on a ten-point scale. We argue that scientific memory should be evaluated as budgeted, modality-aware context restoration rather than as an unconstrained architecture leaderboard, and we release the datasets, harness, raw outputs, judgments, and scripts to reproduce our results and serve as tools for such evaluation. Our code is available at this http URL , and the datasets are available at this http URL .

---


### 144. [Principled Direction-Free Intrinsic Motivation through Model-Free Epistemic Free-Energy Estimators](https://arxiv.org/abs/2607.16858)

**<font color=#1a73e8>作者：</font>** Alireza Furutanpey, Schahram Dustdar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Across environments with mixed sources of uncertainty, unsupervised reinforcement learning requires intrinsic motivation that does not precommit to a particular direction of surprise. Surprise minimization is scoped by design to ``unstable'' environments. Prediction-error curiosity rewards total expected surprise, including irreducible noise. Bandit or mixture switching between surprise-minimizing and surprise-maximizing rewards reintroduces non-stationarity by construction. We propose a single intrinsic reward, stationary within each window, derived from the novelty contribution of a preference-free Expected Free Energy objective, expressed in reward-maximization form. Our claim is that parameter information gain, the expected surprise of the next state minus its irreducible part, is the appropriate intrinsic signal in both high-entropy and low-entropy components of the state space. Maximizing it seeks exactly the surprise the model can explain away. In regions of unresolved dynamics, this epistemic term drives exploration. As dynamics become resolved, the epistemic term vanishes, while an aleatoric penalty favors lower-variance transitions, all without fitting an explicit next-state predictor. A pseudocount supplies epistemic value, a probe-based penalty captures aleatoric variance, and a short-horizon gate protects informative successors. A window-based freeze of all reward-defining objects yields a stationary Bellman operator, explicit bounds on learning targets, and a conditional uniform-concentration result for the nonparametric estimators under mixing, smoothness, bandwidth, and capacity assumptions. In active-inference terms, the agent is preference-free where novelty is retained, standard likelihood ambiguity vanishes under full observability, a nonstandard transition-entropy penalty is added, and surprise minimization emerges in resolved regions of the state space.

---


### 145. [Dataset Distillation by Influence Matching](https://arxiv.org/abs/2607.16859)

**<font color=#1a73e8>作者：</font>** Haoru Tan, Wang Wang, Sitong Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We revisit dataset distillation from an outcome-centric perspective. Rather than aligning process surrogates (per-step gradients or training trajectories), Influence Matching (Inf-Match) aligns the final outcome of training: it learns a compact synthetic set whose effect on the converged parameters matches that of the full dataset. Concretely, we introduce a fully differentiable, sample-level influence estimator that quantifies parameter shifts from adding or removing data, without time-consuming inverse-Hessian products or convexity assumptions. The estimator runs in linear time by unrolling the optimization dynamics and applying a first-order Taylor approximation. We then learn the synthetic set by minimizing the mismatch between its influence and that of the real dataset, yielding outcome alignment rather than heuristic process imitation. Inf-Match delivers the best accuracy across standard classification benchmarks. For instance, on Tiny-ImageNet (IPC=10), Inf-Match attains 31.5\%, a +4.7\% improvement over NCFM. Beyond classification, Inf-Match scales to vision-language distillation on Flickr30K, outperforming strong process-matching baselines. For instance, with 200 to 1000 synthetic samples, our method achieved a leading impressive average on image/text retrieval tasks, higher than NCFM by 2.5\%. The code will be released via this https URL.

---


### 146. [InLiER: Learning-Free Heterogeneous LiDAR Place Recognition via Intermediate Mixed-Radix Structural Keypoint Tokenization](https://arxiv.org/abs/2607.16862)

**<font color=#1a73e8>作者：</font>** Nikolaos Stathoulopoulos, George Nikolakopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR place recognition supports loop closure, relocalization, and multi-agent map management. As robotic platforms increasingly combine LiDARs with different fields of view, resolutions, and scanning patterns, existing descriptors degrade because they are tightly coupled to sensor-specific characteristics. We present InLiER, a learning-free pipeline based on an intermediate tokenization step. Height-sliced keypoints from structural elements receive mixed-radix token IDs encoding height, radial distance, local shape, and azimuth from local 3D geometry, in a compact sub-2KB representation. The same vocabulary is reorganized across three retrieval stages: height-ceiling histogram intersection for fast rotation-invariant shortlisting, binary bitmask alignment for yaw estimation and reranking, and token-guided geometric verification for 6-DoF pose estimation. InLiER achieves state-of-the-art performance on the HeLiPR dataset and in real-world field experiments, among modern handcrafted methods and outperforms the learning-based baseline on most cross-sensor configurations.

---


### 147. [Bridging battery design and health assessment through virtual sensing and physics-informed learning](https://arxiv.org/abs/2607.16864)

**<font color=#1a73e8>作者：</font>** Wendi Guo, Søren Byg Vilsen, Daniel Ioan Stroe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supercharging of lithium-ion batteries (LiBs) requires robust health monitoring to ensure durability, safety, and user confidence, particularly for emerging vehicle-to-grid applications with bidirectional energy flows. Yet battery management remains largely disconnected from the material and structural origins of aging, limiting both interpretable health assessment and informed battery design. Here we propose a physics-informed learning framework with virtual sensing that infers hard-to-measure design parameters, including solid-state diffusion coefficient, electrode thickness, ion concentration, and particle size, directly from standard battery management system (BMS) measurements. Across diverse fast-charging strategies and driving profiles, embedding a digital-twin-derived particle-cracking mechanism as a soft constraint reduces trajectory and lifetime prediction errors by 6-8 times relative to state-of-the-art machine learning baselines using only 2% early-life observations. We further show that accurate degradation extrapolation does not require fully resolved governing equations; validated partial mechanisms, jointly refined with limited data, provide sufficient guidance. Virtual sensing transforms standard charging signals into latent design variables without additional sensors, bridging observable battery behavior and underlying aging processes while reducing capacity loss error by up to 39%, end-of-life (EOL) error by 17%, and prediction variability by up to 54%, enabling real-time exploration of new battery configurations. More broadly, the proposed framework establishes a practical feedback loop between deployment and development, demonstrating how real-world operation can continuously inform upstream design decisions across complex multiphysics systems.

---


### 148. [InfoDense: Density-Aware Regional Decisive Replay for Memory-Efficient Incremental Face Forgery Detection](https://arxiv.org/abs/2607.16873)

**<font color=#1a73e8>作者：</font>** Jikang Cheng, Hao Shen, Xueyi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of face forgery techniques has introduced an increasing variety of manipulations. Incremental Face Forgery Detection (IFFD), which incrementally adds new forgery data to fine-tune previously trained models, has emerged as a promising approach to handle evolving forgery threats. However, conventional replay-based IFFD methods suffer from catastrophic forgetting. Storing full historical images under limited memory often either fails to preserve subtle forgery cues or introduces domain bias, reducing the model's ability to learn intrinsic and transferable manipulation characteristics. In this paper, we propose a Density-Aware Regional Decisive replay strategy, termed InfoDense, to address these challenges. InfoDense prioritizes artifact-dense and forgery-critical regions, significantly reducing storage requirements while maintaining high-fidelity forgery evidence. We first introduce InfoDense Cut to localize decisive patches using CLIP-based embeddings. Then, InfoDense Select ranks candidate segments by combining latent-space representativeness and decisive patch counts, ensuring both diversity and information density in the replay buffer. Finally, InfoDense Fuse reconstructs unbiased training inputs by adaptively merging stored segments with current-task samples, enhancing knowledge retention and generalization. Extensive experiments on challenging incremental deepfake benchmarks demonstrate that InfoDense effectively mitigates catastrophic forgetting while improving cross-domain generalization.

---


### 149. [HyBDM: Multi-Scale Hybrid Experts for Time Series Forecasting with Bidirectional Dependency Modeling](https://arxiv.org/abs/2607.16882)

**<font color=#1a73e8>作者：</font>** Wenqiang Ma, Chen Cheng, Xue Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting (TSF) is vital to many applications, yet existing models often struggle to capture the heterogeneous long-range global patterns and short-range local variations in multivariate time series. While some approaches partially model these dependencies, they often do not jointly exploit temporal and feature-wise information. To address this challenge, we propose HyBDM, a multi-scale hybrid model that decomposes temporal dynamics into global patterns and local variations, which are modeled by two specialized experts. The Global Patterns Expert employs an enhanced BiConv-Mamba module that integrates bidirectional convolutions, an M-SSM layer, a forgetting mechanism, and a GDD-MLP module for cross-channel modeling. The Local Variations Expert uses a Local Window Transformer (LWT) to perform efficient locality-aware attention with reduced computational complexity. In addition, a Multi-Scale Patcher and a Long-Short Router enable multi-resolution representations and adaptive fusion of the two experts. Experiments on six benchmark datasets show that HyBDM outperforms state-of-the-art methods in both forecasting accuracy and computational efficiency, demonstrating its effectiveness in bridging global-local dependencies for multivariate TSF.

---


### 150. [Transferable Low-Rank Convolutional Bases for Onboarding Unseen Medical Imaging Modalities](https://arxiv.org/abs/2607.16888)

**<font color=#1a73e8>作者：</font>** Ranat Das Prangon, Istiaque Ahmed, Shajid Hasan Naim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying a medical imaging model that must later accommodate a modality it has never seen is a recurring practical problem: retraining the shared representation is expensive and destroys performance on the modalities already in service. We study this \emph{onboarding} problem under a strict leave-one-domain-out protocol, in which a convolutional backbone is pre-trained on source modalities (Kidney CT and Brain MRI), frozen permanently, and then required to accommodate an unseen modality (Chest X-ray). Under this protocol we establish three findings. First, decision-layer parameter-efficient fine-tuning is insufficient when the backbone has never observed the target modality: a linear probe and fully-connected LoRA both fall well short, whereas convolutional LoRA recovers most of the achievable accuracy, showing that adaptation must reach the convolutional features. Second, and centrally, the low-rank convolutional \emph{basis} learned on the source modalities \emph{transfers}: freezing that basis and training only its up-projections onboards the unseen modality using just $0.78\%$ of full fine-tuning's parameters, at an accuracy $6.11$ percentage points above a random basis of identical size, while an equivalent decision-layer basis exhibits no reliable transfer. Third, adapter-based onboarding leaves source-modality accuracy exactly unchanged ($\Delta = 0.00$ pp), whereas full fine-tuning reaches the highest target accuracy only by catastrophically degrading the source modalities. A Mahalanobis score on frozen backbone features detects the unseen modality with high sensitivity at a strict source-retention threshold, providing a practical trigger for when onboarding is required. All results are reported over three seeds with paired bootstrap confidence intervals.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-386](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
