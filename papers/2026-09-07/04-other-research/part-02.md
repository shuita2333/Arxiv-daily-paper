# 📦 其他研究 | 2026年09月07日

> 本类共 **194** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-194](./part-04.md)

---

### 51. [PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations](https://arxiv.org/abs/2609.03341)

**<font color=#1a73e8>作者：</font>** Yanshu Zhang, George Shramko, Pratul P. Srinivasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PointGT, a point-based 3D representation that enables simultaneous editing of object geometry and appearance. Existing reconstruction and view synthesis techniques produce volumetric 3D representations that are high-quality and photorealistic, but are difficult to edit. In particular, recent efforts to enable texture editing for 3D Gaussian Splatting representations are not compatible with geometry edits and deformations. Our method combines a point-based representation that is well-suited for geometry deformations with a learned UV mapping technique that enables high-resolution texture editing. We show that PointGT enables fine-grained editing of both geometry and texture in point-based neural representations with high rendering quality.

---


### 52. [P-CORE: Self-Supervised Surface Consistency for Point-Based Neural Editing](https://arxiv.org/abs/2609.03349)

**<font color=#1a73e8>作者：</font>** Yanshu Zhang, Shichong Peng, Mehran Aghabozorgi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in neural rendering have enabled high-fidelity multi-view reconstruction of 3D scenes. However, free-form non-rigid shape editing remains a significant challenge. Point-based neural representations are highly desirable for multi-view reconstruction because they lack fixed connectivity, which does not constrain the learned surface topology to that of the initialization. Yet this same property causes point-based representations to struggle with holes and surface discontinuities under large deformations. To address this, we propose a novel self-supervised method to enable point-based representations to adapt to large deformations without requiring ground truth multi-view images of deformed geometry. The key idea is to generate random deformations and to ensure consistency in the predicted surface before and after deformation. In particular, the surface prediction from the deformed point cloud should be the same as the deformation applied to the surface prediction from the original point cloud. We incorporate our approach into attention-based point representations, which differ from splatting-based point representations in their use of a learned interpolation kernel between points as opposed to a Gaussian kernel around each point. This learned interpolation kernel can learn to adapt to large deformations, without requiring addition or removal of points. We show that our framework significantly enhances its robustness to large deformations. Experiments on synthetic geometry editing benchmarks (Neural Editor, Objaverse) demonstrate that our approach outperforms existing point-based methods in zero-shot editing and significantly reduces artifacts. Furthermore, qualitative results on the DTU and Mip-NeRF 360 datasets demonstrate our method's effectiveness on real-world scenes.

---


### 53. [Time Without Timesteps: Simulating Coupled Dynamical Systems via Self-Consistency](https://arxiv.org/abs/2609.03358)

**<font color=#1a73e8>作者：</font>** Liyu Zerihun, Mark Shinyoung Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Numerical simulation of dynamical systems is usually organized as a causal march through time: each state is computed from the previous one. We explore a different formulation for coupled systems. For each subsystem type we train a neural surrogate mapping a full driving trajectory and initial condition directly to a full output trajectory; following classical waveform relaxation, coupled systems are assembled by enforcing self-consistency among these trajectories: simulation becomes a fixed-point problem over complete trajectories rather than a stepwise rollout. On coupled van der Pol oscillators and Hodgkin-Huxley neuron networks, sequential depth becomes the number of solver iterations: 4-10 Newton iterations where the reference integrator takes 1500 steps. The gradient likewise loses its time recursion: it becomes a linear system solved by GMRES at memory independent of solver depth. A single scalar measured from the learned operator, the spectral radius of its Jacobian, predicts in advance where the coupled solve will converge; past that boundary, unrolled backpropagation diverges and a Neumann adjoint fails, while the implicit gradient remains correct to 0.04%. We report where the approach succeeds and where surrogate error degrades it.

---


### 54. [SimpleDesign: A Joint Model for Protein Sequence and Structure Codesign](https://arxiv.org/abs/2609.03377)

**<font color=#1a73e8>作者：</font>** Jiarui Lu, Yuyang Wang, Yizhe Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proteins are fundamental to biological processes, with their function determined by the complex interplay between the amino acid sequence and the three-dimensional structure. Developing generative models capable of understanding this intrinsically multi-modal relationship is crucial for fields like drug discovery and protein engineering. Existing models often rely on a multi-stage training process where autoencoders that tokenize data into latent representations are trained in a first stage. Secondly, a generative model is trained on the latent representation of the autoencoder(s), i.e., generative modeling in a latent space. We hypothesize that this multi-stage training is not necessary to obtain performant co-design models and thus present SimpleDesign, an effective multi-modal protein design model trained directly in the data space. SimpleDesign leverages a single-stage end-to-end objective that combines discrete cross-entropy for sequences and a regression objective for structures. In order to effectively model the difference in sequence and structure modalities, we develop a Mixture-of-Transformer architecture that allows modality-specific processing while keeping global self-attention over both modalities. We train SimpleDesign on over 2M sequence-structure pairs achieving strong performance across co-design and unconditional sequence/structure generation benchmarks.

---


### 55. [When Depth Hurts: Reliability-Aware Geometry Distillation for Depth-Free RGB-D Salient Object Detection](https://arxiv.org/abs/2609.03378)

**<font color=#1a73e8>作者：</font>** Xuehao Wang, Jiaxin Hua, Runmei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth can resolve appearance ambiguity in RGB-D salient object detection (SOD), yet sensor depth is not uniformly reliable. Missing regions, blurred boundaries, and structural artifacts can propagate through multimodal fusion and make an RGB-D detector less accurate than its RGB-only counterpart. Existing quality-aware approaches regulate observed depth but remain dependent on the same potentially defective modality. We propose \method, a reliability-aware geometry distillation framework developed for RGB-D SOD benchmarks without using dataset-provided depth during training or inference. A frozen Depth Anything V2 model serves only as a training-time teacher, transferring dense relative geometry, hierarchical spatial attention, and boundary structure to a compact edge-aware geometry branch. Pooled bidirectional interaction aligns geometry with appearance, and a pixel-wise reliability estimator selectively injects geometry that is compatible with the current RGB representation. The teacher is removed after training, leaving an RGB-only inference network. Trained on 2,985 RGB-mask pairs, \method{} achieves the best or tied-best result in 26 of 36 metric-dataset comparisons against ten recent RGB-D SOD methods, including a 13.4\% relative MAE reduction on ReDWeb-S. When retrained on DUTS-TR, it also improves the strongest prior $F$-measure by 4.2\% on PASCAL-S, showing that the distilled geometry transfers beyond a particular sensor or dataset domain. Code will be released upon publication.

---


### 56. [FoRIS: Progressive Foreground Refinement for Training-Free In-Context Segmentation](https://arxiv.org/abs/2609.03384)

**<font color=#1a73e8>作者：</font>** Ming Hu, Jianfu Yin, Mingyu Dou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-Context Segmentation (ICS) aims to precisely segment arbitrary semantic concepts, such as objects or parts, given one or a few annotated visual exemplars. In this paper, we revisit ICS from a more classical segmentation perspective, viewing it as a coarse-to-fine progressive refinement process. Rather than directly predicting the final mask through reference-query matching, we progressively refine the segmentation from coarse and ambiguous foreground responses to precise and complete foreground structures. Building upon this perspective, we propose a training-free in-context segmentation framework, termed FoRIS. Specifically, FoRIS consists of three key stages: Foreground Purification, Foreground Localization, and Foreground Consolidation, which progressively suppress background distractions, localize discriminative target regions, and recover complete foreground structures through semantic aggregation. Experimental results demonstrate that FoRIS achieves SOTA performance across semantic and part segmentation tasks, with average improvements of 4.5 and 4.8 mIoU points over existing approaches in the 1-shot and 5-shot settings, respectively. Code: this https URL.

---


### 57. [Exploring the Potential of Contrastive Language-Image Pre-training for Multi-Source Remote Sensing Data](https://arxiv.org/abs/2609.03391)

**<font color=#1a73e8>作者：</font>** Xiangyang Miao, Kelu Yao, Yekai Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive language-image learning (CLIP) has become a key paradigm for remote sensing vision-language understanding. However, existing remote sensing contrastive learning methods are mostly built on RGB-oriented CLIP architectures, making it difficult to exploit heterogeneous sensors such as SAR, multi-spectral imaging (MSI), and hyperspectral imaging (HSI). To address this limitation, we propose OmniRSCLIP, an end-to-end contrastive learning framework that supports multi-source sensor inputs for remote sensing vision-language modeling. The key idea is to extend CLIP beyond its fixed RGB input interface without breaking the pretrained visual knowledge. To this end, OmniRSCLIP introduces Spectral-Spatial Basis Decomposition (SSBD), which formulates arbitrary-channel adaptation as a basis recomposition problem: pretrained CLIP patch embeddings provide transferable spatial bases, while wavelength-conditioned coefficients span sensor-specific embedding kernels within a constrained visual prior space. This design avoids forcing heterogeneous sensors into a fixed-channel input space, while aligning them in a unified image-text semantic space. We further introduce a spectral-context-aware mask-based contrastive learning scheme to suppress modality-specific redundant features and enhance fine-grained image-text alignment. Finally, to support multi-modal training, we construct OmniRS5M, the first large-scale remote sensing image-text corpus covering RGB, SAR, MSI, and HSI. Experiments on retrieval, zero-shot classification, and semantic localization show that OmniRSCLIP preserves strong RGB-domain performance while effectively extending CLIP to heterogeneous remote sensing modalities.

---


### 58. [Neural-Collapse-guided Task-Free Continual Anomaly Detection](https://arxiv.org/abs/2609.03406)

**<font color=#1a73e8>作者：</font>** Xiaotong Kong, Chaoyang Song, Ziai Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed growing interest in continual anomaly detection for industrial visual inspection. However, real-world manufacturing environments exhibit unpredictable shifts in data distributions, rendering task-dependent continual learning assumptions impractical. To address this limitation, we formulate industrial anomaly detection as a task-free continual learning problem and propose NC-TFAD, a neural-collapse-inspired, geometry-driven framework for learning from non-stationary data streams without task boundaries. NC-TFAD freezes a pretrained backbone and aligns streaming features to a simplex Equiangular Tight Frame (ETF) prototype space to stabilize representation geometry under non-stationary streams. To satisfy the NC-inspired geometric construction in the absence of real anomalies, we generate synthetic anomaly samples as auxiliary anchors during training. Building on this geometry, we further introduce inter- and intra-class regularization together with a Focal Neural Collapse Contrastive (FNCC) loss to suppress representation drift and improve normal-anomaly separability. Finally, a normal-patch-prototype-guided localization branch constructs calibrated patch-wise deviation maps from normal training samples and fuses them with a weak self-attention prior, producing anomaly heatmaps without pixel-level annotations. Extensive experiments on MVTec AD and VisA show that NC-TFAD consistently outperforms representative task-free continual learning methods adapted from general vision, as well as unified anomaly detection baselines, in both image-level detection and pixel-level localization under the task-free continual learning protocol. These results highlight that geometry-driven modeling offers an effective and robust solution for task-free continual anomaly detection in real-world industrial applications.

---


### 59. [Mudragen: Geometrically Supervised Generation of Interacting Two-Hand Mudras for Preserving Indian Classical Dance Heritage](https://arxiv.org/abs/2609.03415)

**<font color=#1a73e8>作者：</font>** Jagadish Kashinath Kamble, Jayanta Mukhopadhyay, Debaditya Roy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic generation of hand gestures is essential for the transmission of Indian classical dance and critical for its preservation. Indian classical dance gesture datasets are inherently low-resource, and the canonical Sanskrit definitions of many mudras lack precise textual descriptions, limiting the effectiveness of conventional text-conditioned image generation models. We present \textbf{MudraGen}, a conditional diffusion framework that synthesizes realistic RGB images of \textit{Samyukta Hasta Mudras} -- interactive two-hand gestures from Bharatanatyam (an Indian classical dance form). Unlike prior work on simple hand signs or single-hand gestures, MudraGen introduces geometry-aware supervision to capture the precise coordination, anatomical validity, and cultural nuance of interacting hands. We formulate three geometry-aware objectives: Keypoint Loss for 3D joint alignment, Joint Offset Loss for inter-hand spatial coherence, and Shape Consistency, which serves as an anatomical regularizer by encouraging consistent hand morphology while allowing independent hand poses. Together, these objectives guide the diffusion model toward anatomically plausible and well-coordinated hand configurations, enabling the synthesis of photorealistic and pose-accurate gesture images. Experimental results show that MudraGen surpasses existing state-of-the-art generative approaches in visual realism, anatomical correctness, and preservation of fine hand-pose structure, enabling faithful reproduction of complex Samyukta Hasta mudras. Beyond quantitative gains, its ability to generate culturally grounded and structurally consistent gestures highlights practical applications in cultural preservation and dance education.

---


### 60. [Privacy, Robustness, and Fairness Trade-offs in Federated Intrusion Detection: Geometric Indistinguishability at the Aggregation Interface](https://arxiv.org/abs/2609.03420)

**<font color=#1a73e8>作者：</font>** Adrita Rahman Tory, ABM Shawkat Ali, Md Abu Layek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning enables privacy-conscious collaboration for network intrusion detection without centralizing sensitive traffic data, yet its deployment in operational environments must simultaneously satisfy three competing requirements: formal differential privacy guaranties, tolerance to Byzantine-adversarial participants, and reliable detection coverage across severely imbalanced attack categories. Existing literature treats these properties as independently composable, an assumption that this paper challenges both theoretically and empirically. In this paper, we study how these requirements interact in class-imbalanced federated NIDS and introduce geometric indistinguishability as a conceptual lens for a regime in which privacy-induced dispersion in client updates can make minority-class signals harder for robust aggregation to preserve. Using UNSW-NB15 as a case study, we evaluate DP-SGD combined with coordinate-wise median under label-flip and model-poisoning attacks, with threat coverage assessed across attack categories. Our results provide initial evidence that the joint use of privacy noise and robust aggregation can disproportionately degrade detection of rare attacks relative to majority classes. We also show that part of the observed collapse under strong privacy can arise from training miscalibration, while a residual performance floor may remain for ultra-rare categories even after epsilon-dependent tuning. These findings motivate studying privacy, robustness, and rare-attack coverage jointly rather than as independently composable properties, and suggest that aggregation-aware modeling and sample-aware evaluation are promising directions for trustworthy federated NIDS.

---


### 61. [The Civilization Framework: Sovereign-Anchored Communication Between Personal Multi-Agent Systems](https://arxiv.org/abs/2609.03425)

**<font color=#1a73e8>作者：</font>** Guangjun Liu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Humans are the transport layer between AI systems, losing context at every hop. We present the Civilization Framework, whose addressable party is the civilization, not the agent (one human sovereign, a persistent ledger, and interchangeable agents), and the Embassy Protocol, a carrier-agnostic overlay: messages arrive asynchronously at a resident ledger endpoint, any online agent of the receiver handles them, and commitment state on both ledgers, not delivery, is ground truth. Authority derives from memory: an agent's power to act for its civilization is capped by the memory it can access and externalized through signed credentials, separate from civilization-level reputation. We identify the temporal-weight effect, a hazard in AI-to-AI communication where what arrives first acquires unearned authority, and test it in one frontier model in a preregistered 1,908-trial experiment. With verification removed, an incorrect upstream claim arriving first captures 54.2% of answers (4.2% under full verification), while the same claim arriving after the receiver has sealed its own answer captures 31.6% (the two prompt shells are not length-matched, so part of that gap may reflect shell form; see Section 7), and both registered question-set specifications agree on these two verdicts (the exclusion specification is preregistered as under-powered). Two secondary results, the mitigation from instruction-level provenance labeling and sealed-answer accuracy equivalence, are specification-dependent, holding only under the all-questions specification. Because a registered check of tool use failed its call-budget condition, the registration classifies the round as inconclusive and every result above, primary and secondary, is reported as exploratory; a replication with harness-enforced budgets is planned. The framework's intra-civilization layer has a working implementation.

---


### 62. [TraveL: Transformer-based Multi-view Path Distributional Representation Learning](https://arxiv.org/abs/2609.03427)

**<font color=#1a73e8>作者：</font>** Fang He, Tao-yang Fu, Wang-chien Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Path representation learning (PRL) for road networks has received increasing research attention, due to various path-related applications. Existing works on PRL typically exploit the co-occurrence relationship among road segments and paths to learn a vector as the path representation, without exploring the varied traveler behaviors and the regional correlation on the path. In this work, we propose to learn distributional representations, which provide valuable information for use in path-related applications, by capturing the varied traveler behaviors as well as the various dependencies within regions of road segments. We propose a novel Transformer-based Multi-view Distributional Representation Learning (TraveL) framework to encode a path along with a travel starting time to a distributional representation, which can be used to decode possible samples of on-path traveler behavior. Moreover, by analyzing the regional correlation which reveals various road segment relationships, we propose a regional attention to encode these correlations in a path. Also, we explore the idea of Kolmogorov-Smirnov (K-S) test to compare the sampled traveler behavior against the collected ground truth to facilitate training. Experimental results show that the proposed TraveL model outperforms the state-of-the-art methods on both synthetic and real-world datasets, by 14.7% in Mean K-S distance for travel time distribution estimation, 16.7% in Mean Absolute Error (MAE) for path similarity prediction, and 3.97% in MAE for destination prediction.

---


### 63. [Do GUI Agents Know When Not to Act? Enabling Conflict-Aware Termination for Multimodal GUI Agents](https://arxiv.org/abs/2609.03438)

**<font color=#1a73e8>作者：</font>** Zhaoyuan Huang, Tianjie Ju, Pengzhou Cheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical user interface (GUI) agents are increasingly used to execute natural-language instructions on user interfaces, yet real users may issue infeasible instructions due to benign mistakes. A reliable agent should not only know how to act, but also when not to act. In this work, we introduce CONFLICTGUI, a benchmark covering instruction-internal conflicts and instruction-GUI context conflicts to study conflict-aware termination. Our evaluation reveals severe execution-biased overcompliance: agents that perform well on feasible tasks often continue to execute blindly under conflicting instructions. To mitigate this behavior, we propose CONFLICTGUARD, an inference-time framework that aligns an agent's feasibility awareness with its action generation. CONFLICTGUARD contains two coupled components: a feasibility verification protocol that guides the agent to assess instruction logic and GUI-side evidence before acting, and a conditional action modulation mechanism that steers agents from over-compliant execution into termination-oriented behavior. Experiments across five widely-used agents demonstrate that CONFLICTGUARD improves average conflict task success rate significantly, while preserving normal GUI-task performance. These results validate that a lightweight inference-time intervention can substantially boost GUI Agent's competence to identify inappropriate execution scenarios and refrain from unnecessary actions.

---


### 64. [Guide, Not Bind: Why Defeasible Priors Fail in Augmented Lagrangian Causal Discovery](https://arxiv.org/abs/2609.03442)

**<font color=#1a73e8>作者：</font>** Sairam Sundararaman, Sara Girdhar, Manit Narasimha Murthy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentiable causal discovery methods increasingly encode expert priors as forbidden-edge constraints enforced by an Augmented Lagrangian (ALM) penalty, on the assumption that a data-adaptive relaxation mechanism will discount and eventually override a rule the data consistently contradicts. We show this design, which we call \emph{guide, not bind}, fails for two independent, precisely characterized reasons, and that directly repairing both restores it only partially. First, sequential penalty-ramping ALM suppresses a wrongly-forbidden true edge before any counterfactual check can detect it: we give three necessary conditions any adaptive relaxation must satisfy to avoid this (Proposition~\ref{prop:conditions}), prove that DADU---the natural relaxation rule this paper introduces as the object of study---violates all three (Corollary~\ref{cor:dadu_failure}), and confirm the failure across 3{,}072 training runs spanning graphs from 4 to 32 nodes, where a single wrong prior suppresses a true edge in 87--97\% of trials under DADU. Second, and independent of any fix to the mechanism, we prove in closed form that the standard correlation-matching objective ties a true edge and its reverse to an identical cost of exactly $2r^2$ (Lemma~\ref{lem:tie}), not because the underlying equal-variance model is unidentifiable, but because normalizing to correlation discards exactly the variance information that would make it identifiable; covariance matching instead separates the two directions by a provable margin of at least $w_0^4$ (Lemma~\ref{lem:separation}).

---


### 65. [Beyond Straightness: Non-Crossing Flow Matching via Quantile AlignTree Coupling](https://arxiv.org/abs/2609.03443)

**<font color=#1a73e8>作者：</font>** Junyi Lin, Mengyu Li, Jingxuan Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The performance of Flow Matching largely depends on the quality of the coupling between the source and target distributions. However, independent coupling often leads to path crossings and local velocity ambiguity, while OT-based couplings typically incur high construction costs. To address this challenge, we propose Quantile AlignTree Flow Matching (QAT-FM), an efficient structured coupling strategy that constructs a hierarchical coupling between a Gaussian prior and the target data distribution via a quantile-aligned tree structure. QAT-FM constructs the coupling in $\mathcal{O}(Nd\log N)$ time and supports per-pair source sampling with $\mathcal{O}(d)$ complexity, enabling scalable training for large-scale high-dimensional generative tasks. Theoretically, we prove that the QAT coupling satisfies marginal consistency, induces non-crossing linear interpolation paths, and consistently improves path separation at intermediate times compared with independent coupling, thereby alleviating local velocity ambiguity. QAT-FM further extends naturally to conditional generation, enabling structured conditional coupling while preserving global Gaussian alignment. Experiments across diverse benchmark datasets demonstrate that QAT-FM achieves competitive generative performance while substantially reducing coupling construction cost.

---


### 66. [OCR-EDR: Rendering-Aware Diagnosis and Repair for Closed-Loop OCR Improvement](https://arxiv.org/abs/2609.03445)

**<font color=#1a73e8>作者：</font>** Linnan Zhao, Kang Liu, Hao Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although document OCR systems perform increasingly well on routine documents, complex formulas, structured text, and long-tail formats remain error-prone. OCR predictions may omit fine-grained content or hallucinate unsupported outputs, while equivalent encodings of the same visible content must be accommodated. Existing OCR evaluation methods mostly report aggregate metrics, offering limited support for analyzing case-level errors and improving OCR performance. We propose OCR-EDR (OCR Error Diagnosis and Repair), a rendering-aware framework that advances from fine-grained diagnosis to iterative repair. Given a source image, an editable OCR prediction, and its rendered image, OCR-EDR first jointly assesses whether the prediction and its rendering are consistent with the source, preserving valid predictions, including rendering-equivalent ones, while diagnosing and localizing genuine errors. It then applies executable edits and may request an updated rendering for iterative reassessment. We construct OCRErrBench from diverse real OCR predictions, covering text and formulas, exact and rendering-equivalent positives, and genuine errors, and develop the DocEDR model to execute the diagnosis--repair loop. On OCRErrBench, DocEDR achieves 94.78% diagnostic accuracy. It repairs 86.23% of erroneous inputs to visual consistency, raises formula Case-F1 by 30.99 percentage points over DOCR-Inspector-7B on DOCRcaseBench, and improves formula CDM by up to 4.62 percentage points on the identified Bad subsets of four OCR systems on UniMER-Test. These results show that OCR-EDR turns fine-grained OCR analysis into verified corrections and performance gains.

---


### 67. [Preserving Knowledge across Space and Time for Continual Video Deepfake Detection](https://arxiv.org/abs/2609.03446)

**<font color=#1a73e8>作者：</font>** Taehoon Kim, Jongwook Choi, Heejae Jo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The continuous emergence of high-quality video deepfakes requires detectors that continually adapt to new forgery patterns, yet existing approaches, which are designed for deepfake images, fail to capture video-specific cues. Unlike deepfake images that contain only spatial artifacts, deepfake videos leave distinct evidence along both spatial and temporal axes, necessitating the separate preservation of each modality during sequential model updates. To overcome this limitation, we introduce a continual deepfake video detection framework, Modality-Specific Frequency Distillation (MSFD), that explicitly decomposes video features into spatial, temporal, and spatiotemporal modalities in the frequency domain. This decomposition enables independent preservation of each modality, as different deepfake video types exhibit varying reliance on spatial and temporal cues across tasks. Furthermore, MSFD adopts a cross-modality decorrelation loss that encourages spatiotemporal representations to remain orthogonal to single-modality cues. Extensive experiments show that our framework achieves stronger adaptation and preserves performance more effectively than state-of-the-art methods across diverse continual deepfake video scenarios.

---


### 68. [STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction](https://arxiv.org/abs/2609.03447)

**<font color=#1a73e8>作者：</font>** Bocheng Li, Wenjuan Zhang, Jie Pan.Dongxu Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale 3D surface reconstruction from aerial imagery is fundamental to geospatial mapping and urban modeling. Recent advances in 3D Gaussian Splatting (3DGS) have demonstrated considerable potential for this task. However, existing methods still face three major challenges in large and complex scenes: scene partitioning may split continuous scene elements across independently optimized sub-regions; geometric constraints mainly focus on the attributes of individual Gaussians while overlooking their local organization; and uniform regularization struggles to accommodate heterogeneous geometric structures. To address these issues, we propose STARS-GS, a structure-aware 3DGS framework for large-scale surface reconstruction. First, we introduce a structure-aware scene partitioning strategy that better preserves continuous scene structures during partitioning and reduces cross-region geometric inconsistencies and stitching artifacts through boundary refinement. Second, we develop neighborhood-aware Gaussian organization that extends geometric constraints from individual primitives to their neighborhood organization, encouraging Gaussians to better conform to local surface geometry. Third, we introduce adaptive surface regularization that adjusts the regularization strength according to local geometric characteristics, promoting geometric consistency in structured regions while preserving plausible variations in unstructured regions. Extensive experiments on large-scale aerial photogrammetry benchmarks demonstrate that STARS-GS consistently outperforms the evaluated Gaussian-based methods in surface reconstruction. It increases the average F1-score from 0.640 for the second-best method to 0.698, corresponding to a relative improvement of approximately 9.1\%, demonstrating effective improvements in geometric accuracy and surface completeness.

---


### 69. [Preprocessing Failure and Adversarial Detection in Depthwise-Separable Edge Vision Systems](https://arxiv.org/abs/2609.03453)

**<font color=#1a73e8>作者：</font>** Jannatul Masruk Mukta, Rifa Sanjida, Adrita Rahman Tory 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preprocessing-based defenses are the standard first-line response to adversarial attacks on edge vision systems, requiring no retraining, no architectural changes, and widely recommended as model-agnostic mitigations. Yet the foundational evaluations of these defenses were conducted on residual or Inception-class architectures, not on the depthwise-separable CNNs that dominate edge deployments. This untested assumption leaves a gap in the security evaluation literature. This paper closes that gap by evaluating six preprocessing defenses against adversarial perturbations across both architecture families. Across all perturbation levels and defenses tested, the two depthwise-separable architectures show consistently poor recovery while the residual architecture shows partial recovery; ablation results are consistent with an architectural rather than parametric explanation, though only three architectures and one attack family are evaluated. Crucially, this failure is not merely a negative result. The same output divergence that disqualifies preprocessing as a recovery mechanism reveals a detection opportunity: preprocessing consistently disrupts clean predictions while leaving adversarial predictions largely unchanged, an asymmetry that is directly measurable without retraining or architectural modification. We further show that standard image quality metrics are unreliable proxies for defense effectiveness, a methodological gap in current evaluation practice. A practitioner decision framework is provided for adversarially resilient edge vision deployment.

---


### 70. [A Two-Stage Forecasting System for CPU Workload Prediction in Private Clouds](https://arxiv.org/abs/2609.03457)

**<font color=#1a73e8>作者：</font>** Ashir Javeed, Anton Borg, Håkan Grahn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate cloud resource forecasting is essential for proactive resource provisioning, maintaining Quality of Service (QoS), and reducing operational costs in dynamic cloud environments. The existing forecasting approaches predominantly estimate future CPU workload directly from historical resource traces, which often overlook the relationship between customer service demand and subsequent resource consumption. This study proposes a two-stage integrated forecasting model that explicitly models this dependency by first forecasting customer service requests, expressed as Transactions Per Second (TPS), and subsequently estimating future CPU workload from the TPS forecast. Both the forecasting component and resource prediction component employed the XGBoost model within a cascaded learning architecture, complemented by adaptive online retraining using an expanding-window strategy to address concept drift in continuously evolving cloud workloads. The proposed work was evaluated using real-world traces collected from a private cloud environment comprising ten applications. Experimental results demonstrate robust forecasting performance by achieving Symmetric Mean Absolute Percentage Error (SMAPE) below $7\%$ for most applications, with the best-performing application achieving an MAE of $0.7372$, RMSE of $1.1866$, SMAPE of $3.57\%$, and an R2 of $0.9185$. Horizon-wise drift analysis confirmed stable recursive forecasting behavior with controlled error accumulation across a 60-step prediction horizon. Compared with the conventional direct CPU forecasting method, the proposed two-stage integrated model gives improved forecasting robustness, computational efficiency, and interpretability, making it well-suited for proactive resource management and intelligent auto-scaling in cloud computing environments.

---


### 71. [BMCTrack-d: Pig re-identification and tracking via back marks in challenging camera settings](https://arxiv.org/abs/2609.03463)

**<font color=#1a73e8>作者：</font>** David Brunner, Maciej Oczak, Marie Bordes 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated pig monitoring is essential for assessing their health, behaviour, and welfare. To date, most pig monitoring solutions operate on the group-level, because individual-level monitoring requires reliable long-term identification and tracking of each animal. For domesticated pigs this remains challenging because pigs of the same breed often have highly uniform appearances. Moreover, research on pig monitoring is almost exclusively reported in top-down view camera settings, which considerably ease tracking, but are not always an option in practice. In this work, BMCTrack-d is presented, a novel tracking-by-detection approach that leverages unique back marks to enable robust pig re-identification and tracking in a challenging side-view camera setting, afflicted by rapidly moving pigs, severe occlusions and low resolution. The method first predicts the detected pigs' identities using a neural network-based back mark classifier. To improve re-identification reliability over time, two dedicated post-processing stages are introduced: a temporal prediction consistency check, which validates the identity assignments against the recent prediction history, and deduplication, which resolves conflicting identity assignments in each time step. By explicitly prioritising accurate, appearance-based re-identification over continuous tracking, the proposed approach addresses a key limitation of existing trackers for individual-level monitoring scenarios. On a demanding test set BMCTrack-d outperforms two strong baselines, BoT-SORT-ReID and TrackTrack-ReID, by 9.11% and 1.03%, respectively, in higher-order tracking accuracy. These results demonstrate the effectiveness of back mark-based re-identification and tracking for robust individual-level pig monitoring in challenging settings.

---


### 72. [SafeRestore: Detector-Relative Risk Certificates for Selective Industrial Image Restoration](https://arxiv.org/abs/2609.03475)

**<font color=#1a73e8>作者：</font>** Shaoliang Yang, Jun Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial inspection pipelines often restore a measured image before a detector acts on it, yet restoration can suppress detector-supported defect structure or create clean-region activations. We formulate restoration as a selective action problem over the measured display, five restored candidates, and review. SafeRestore ranks candidates with action-specific fitted scores, chooses a gate on threshold-tuning data, and evaluates the fixed gate on a disjoint certification sample with two one-sided exact binomial bounds: one for the positive-conditional evidence-loss incident rate and one for the all-accepted excess-activation incident rate. The guarantee is marginal for one policy fixed before its certification outcomes are observed, under an image-level i.i.d. working model. In a retrospective split-sample study of 4,591 public Carinthia-S images, the protocol yields auditable risk-coverage behavior. The primary all-action policy passes in one of five training repetitions (12.0% +/- 26.9% pass-gated test coverage when failures count as zero), whereas fixed bicubic and reduced-complexity variants pass more often. On reserved morphologies, evidence-loss incidence rises to 81.1-90.3%, and KolektorSDD lacks both detector competence and enough positive certification images for the stated target. The contribution is therefore an auditable, detector-relative framework for deciding when a transformed image may be returned automatically and when review remains necessary -- not a claim that adaptive routing outperforms simpler policies on the present evidence.

---


### 73. [Pattern Over-Generalization of Knowledge Graph Embedding](https://arxiv.org/abs/2609.03487)

**<font color=#1a73e8>作者：</font>** Junsik Kim, Kangil Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graph embedding (KGE) demonstrates its effectiveness for predicting missing links in knowledge graphs (KGs) by projecting entities and relations into a low-dimensional vector space. It is crucial for KGE models to effectively capture inference patterns (patterns) inherent in KGs, such as symmetry/antisymmetry, inversion and composition. Although recent KGE models exhibit strong capabilities in modeling such diverse patterns, they suffer from inherent limitations stemming from pattern over-generalization, where embeddings learned from only a single pattern instance inevitably generalize that pattern to all related instances, i.e., generalize the pattern universally. To address this issue, we propose PogRE (Pattern Over-Generalization Robust Embedding), a simple but effective method that utilizes dense linear transformations and compound operations for relation representation. Our theoretical analysis demonstrates that a dense linear transformation allows a pattern to become progressively universal as more triples are observed in the pattern. Furthermore, after observing d+1 linearly independent entities (d+1 denotes the dimension of entity), the linear transformation guarantees universal generalization of the pattern across all related instances. Experimental results on three standard benchmark datasets show that PogRE outperforms existing state-of-the-art KGE models in link prediction. Moreover, our empirical results indicate that PogRE effectively addresses the negative impact of over-generalization.

---


### 74. [Spectral characteristics of autoencoder parameters as a vector representation of data](https://arxiv.org/abs/2609.03495)

**<font color=#1a73e8>作者：</font>** Maria Nikitina, Anton Bishuk, Oleg Bakhteev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper examines the relationship between the parameters of autoencoder models and the statistical properties of the data on which they are trained. Autoencoders are defined as models with an encoder-decoder architecture, trained to reconstruct input data through a compressed latent representation. It is proposed that the model parameters can be viewed as a dense vector representation of the corresponding sample. To test this hypothesis, a theoretical and experimental study is conducted in which a vector representation is formed based on the spectral characteristics of the autoencoder parameter matrices. Theoretical analysis shows that the singular values of the model parameter matrices are related to the eigenvalues of the covariance matrix of the training data, ensuring the transfer of information between the data space and the parameter space. Experimental results on the CIFAR-10 and FashionMNIST datasets confirm that the resulting vector representations allow for a high degree of accuracy in distinguishing between models trained on different data subsets, without resorting to complex vector generation algorithms or using the original samples. These results suggest that the parameters of trained autoencoders can be viewed as sample representations.

---


### 75. [PPO-STGNN: A Proximal Policy Optimization Approach with Spatio-Temporal Graph Neural Networks for DAG Task Scheduling in Cloud-Edge-End Computing](https://arxiv.org/abs/2609.03503)

**<font color=#1a73e8>作者：</font>** Yangshuo Qi, Chenwei Wang, Zihan Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid development of the Internet of Things, computation intensive directed acyclic graph (DAG) tasks have become increasingly common in cloud-edge-end collaborative environments. However, cloud, edge, and end nodes are highly heterogeneous in computing capacity, network bandwidth, and energy consumption, which makes the efficient scheduling of tasks with complex dependencies an NP-hard problem. Traditional heuristic algorithms and conventional reinforcement-learning methods often fail to capture the spatio-temporal dynamics of system resources. This paper proposes PPO-STGNN, a DAG task-scheduling algorithm that integrates proximal policy optimization (PPO) with spatio-temporal graph neural networks (STGNNs). The method uses an STGNN to extract features from both the DAG task topology and the physical cloud-edge-end resource graph, and then optimizes the scheduling policy through PPO to minimize makespan and schedule length ratio (SLR) while improving CPU and memory load balancing. To accelerate convergence, a multi-teacher behavior-cloning mechanism is introduced for pretraining. Experimental results show that PPO-STGNN significantly improves load balancing while maintaining a low completion time, making it suitable for dynamic and heterogeneous cloud-edge- end DAG scheduling scenarios.

---


### 76. [Restricted Eigenvalues Beyond Gaussian Width: Threshold Occupancy under Heavy Tails](https://arxiv.org/abs/2609.03504)

**<font color=#1a73e8>作者：</font>** Shi Fu, Huibo Xu, Qixin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Restricted eigenvalue (RE) bounds govern stable recovery by norm-regularized estimators. For isotropic sub-Gaussian measurements, the benchmark sample size is $1+w(A)^2$, where $w(A)$ is the Gaussian width of the normalized descent cone. The COLT 2015 open-problem note (Banerjee et al., 2015) asked whether the same law follows for heavy-tailed designs from a uniform small-ball condition alone. We give an explicit and systematic negative answer to the general question as formulated there: the proposed law fails in its full dimension-free, arbitrary-set form, and the missing obstruction is simultaneous threshold occupancy. A constant-width polyhedral descent cone with fixed small-ball constants has zero empirical RE on every sample path up to half the ambient dimension. More generally, every finite range space admits exact threshold encoding in an arbitrarily narrow spherical cap and a lift to a full polyhedral descent-cone section. For every fixed threshold VC dimension $d$, as $\beta\downarrow0$, the sharp worst-case sample complexity is $\Theta(\beta^{-1}[d\log(1/\beta)+\log(1/\delta)])$. The separation persists under exact isotropy and all finite moments: on the same constant-width cone, Gaussian measurements succeed with $O(1+\log(1/\delta))$ samples, whereas an isotropic heavy-tailed design fails pathwise for $n\lesssim\sqrt{p/\log p}$. Gaussian smoothing yields an everywhere-positive $C^\infty$ density while retaining arbitrarily poor RE. Under isotropy, a distribution-free fallback governed by affine dimension times squared enclosing radius is sharp on this family.

---


### 77. [An Adversarial Zero-Shot Learning Approach for Anomaly Detection in Multivariate IoT Traffic Data](https://arxiv.org/abs/2609.03505)

**<font color=#1a73e8>作者：</font>** Mahshid Rezakhani, Tolunay Seyfi, Fatemeh Afghah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection in Internet of Things (IoT) networks presents unique challenges due to the diversity of devices, lack of labeled data, and domain variability across environments. In this paper, we propose a novel framework for multivariate time-series anomaly detection that leverages adversarial learning and contrastive loss within a sequence-based Variational Autoencoder (VAE) architecture. Our method enables zero-shot domain adaptation by jointly optimizing domain-invariant latent representations and semantically structured embedding spaces, without requiring labeled data or raw feature transfer. To address the heterogeneity of IoT deployments, we introduce encoder and decoder adaptor layers that align feature distributions across domains while preserving contextual semantics. Additionally, we propose a destination-based segmentation strategy to better model real-world communication structures in IoT traffic. Our framework is comprehensively evaluated on six distinct datasets spanning industrial, enterprise, general-purpose, smart home, and military automation domains across 44 transfer scenarios. Experimental results demonstrate strong zero-shot generalization in several cross-domain settings and competitive performance against a contrastive domain-adaptation baseline under realistic, heterogeneous, and privacy-constrained IoT conditions.

---


### 78. [LongCounsel-8: A Benchmark Suite for Longitudinal Depression Tracking from Multi-Session Counseling Dialogues](https://arxiv.org/abs/2609.03507)

**<font color=#1a73e8>作者：</font>** Jiayi Li, Zhaomin Wu, Bingsheng He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tracking depression from multi-session counseling dialogues requires estimating both current symptom severity and how it changes across sessions. Yet progress on this task is constrained by the scarcity of longitudinal counseling data with standardized session-level depression labels. Existing resources typically provide either multi-session conversations without depression labels or labeled interviews in a single session. Building such a benchmark poses three challenges: maintaining longitudinal consistency and diversity, grounding symptom progression in empirical patterns, and expressing controlled depression states naturally without exposing target labels. To address these challenges, we introduce LongCounsel-8, a benchmark suite of three independently generated datasets totaling 7,749 five-session counseling trajectories, grounded in real-world client profiles, depression trajectories, symptom compositions, and counseling patterns. We combine profile-grounded simulation, empirically informed state construction, and indirect behavioral realization to address these challenges. Across the benchmark, simulated self-reports closely recover the controlled states, supporting label fidelity. Experiments on existing depression tracking methods reveal three key findings: (1) lower single-session score error does not guarantee accurate identification of trend, i.e., improvement or worsening; (2) existing methods are consistently less reliable on worsening trajectories; and (3) additional session history may reduce the accuracy of trend prediction. Together, these findings establish LongCounsel-8 as a foundation for advancing depression assessment from static, single-session prediction toward reliable longitudinal tracking of mental-health change.

---


### 79. [Residual Optimal Transport-Based Experts Collaboration Towards Modality-Aware Infrared-Visible Object Detection](https://arxiv.org/abs/2609.03516)

**<font color=#1a73e8>作者：</font>** Yue Zhao, Hua Yu, Yukun Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared-visible object detection (IVOD) integrates complementary evidence from visible and infrared sensors for reliable perception in challenging scenes. In practice, sensors may fail or drop frames, leaving one modality unavailable or intermittent. Existing methods for IVOD assume both modalities are always present, and fixed fusion collapses when one stream is missing. Furthermore, it remains a critical challenge to reliably estimate semantic correlation across heterogeneous modalities, especially under spectral distribution discrepancy. We present FlexibleFusion, a unified and adaptive method that flexibly allocates integration pathways and fusion strength, operating seamlessly across complete and missing-modality regimes. At its core, the Modality-Aware Experts Collaboration (MAEC) mechanism selectively activates and aggregates cross-modal or intra-modal expert pathways. It allows cross-modal fusion when full modalities are available and falls back to self-fusion under missing conditions. Additionally, we design Residual Self-Paced Entropic Optimal Transport (RSPEOT) to align heterogeneous feature distributions from a transport perspective. Instead of relying on the fixed sparsity coefficient in standard entropic optimal transport (EOT), RSPEOT introduces a residual-driven self-paced update that prioritizes reliable matches and progressively refines harder ones. This design alleviates the additional optimization burden of standard EOT while preserving reliable semantic alignment. Comprehensive experiments under complete and missing-modality protocols show consistent performance across arbitrary modality configurations. Code will be released upon publication.

---


### 80. [Neural Video Compression Based on Deformable Temporal Alignment and Difference-aware Fusion](https://arxiv.org/abs/2609.03520)

**<font color=#1a73e8>作者：</font>** Chuyue Shan, Songlin Sun, Wang Chenwei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In conditional coding-based neural video compression, the quality of temporal context directly affects compression per- formance. Existing methods mostly construct context from prop- agated reference features, but they are vulnerable to motion esti- mation and local alignment errors in regions with complex mo- tion, occlusion, and high-frequency textures, resulting in inaccu- rate temporal information. To address this issue, this paper pro- poses a method combining deformable temporal alignment and difference-aware spatial selective fusion. A Context-aware Tem- poral Alignment Module is used to generate complementary tem- poral context, while a Difference-aware Spatial Selective Fusion module adaptively selects reliable temporal information and sup- presses misalignment. Experiments show that the proposed method achieves certain rate-distortion performance improve- ment over DCVC-DC.

---


### 81. [LeanGRPO: Eliminating Redundant Recomputation in Diffusion RL](https://arxiv.org/abs/2609.03528)

**<font color=#1a73e8>作者：</font>** Sijie Wang, Zhiqiang Tan, Xinrui Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion reinforcement learning (RL) has recently achieved significant success in post-training image and video generative models. However, most diffusion RL methods, including DanceGRPO and FlowGRPO, recompute selected timesteps with gradient tracking after rollout. Under on-policy training with the same backend for rollout and update, this recomputation is mathematically redundant. Intuitively, the rollout and policy update steps can reuse the same feed-forward backbone to avoid redundant computation, but doing so can incur a large memory overhead during rollout. To address the issue, we present LeanGRPO by restructuring the data-parallel layout and introducing two recompute-free training schedules for trajectory-logprob diffusion RL: (1) LeanGRPO-Retain enables gradient tracking during rollout and directly reuses the resulting computation graphs and saved activations for backward during update, requiring no recomputation; and (2) LeanGRPO-Reweight also enables gradients during rollout, but immediately backpropagates each selected step using a provisional advantage and delays gradient synchronization, then corrects the provisional gradients with the true advantage after the trajectory is completed. These schedules target different model scales and input sizes. Across FlowGRPO/DanceGRPO with FLUX.1-dev and Wan, LeanGRPO achieves up to 1.83x end-to-end speedup while preserving the original optimization objective.

---


### 82. [Coupled Scaling: A Representational Accessibility Framework for Neural Scaling Laws](https://arxiv.org/abs/2609.03533)

**<font color=#1a73e8>作者：</font>** Jie Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing theories derive neural scaling from data geometry or a specified data-model spectrum, but systems trained on the same data can scale differently when architecture or optimization changes the representations they can efficiently reach. We introduce Coupled Scaling, a task-conditioned framework in which finite-budget scaling depends on the relation between task structure and the geometry accessible to an architecture-optimization system. In a solvable mode-truncation model, loss separates into target energy outside architectural support and an unresolved supported tail. For an arbitrary priority order, the residual lies between the best-N supported tail and the tail beyond the largest completed high-value prefix. If the cumulative-tail and coverage log-rates are $\gamma_{A,T}$ and $\rho_{A,O,T}$, the residual exponent lies in $[\rho_{A,O,T}\gamma_{A,T},\gamma_{A,T}]$. Under bounded off-prefix gain, the completed prefix is rate-determining and $\alpha_{A,O,T}=\rho_{A,O,T}\gamma_{A,T}$; for $a_{A,T,j}\asymp j^{-b_{A,T}}$, this gives $\alpha_{A,O,T}=\rho_{A,O,T}(b_{A,T}-1)$. A fixed-kernel specialization derives the training-time exponent from the near-zero tail of a task-weighted spectral measure defined independently of the loss fit. The framework separates architectural support from finite-budget acquisition and motivates two tests: static task-relevant geometry should track loss at a common budget, while multiscale geometry should track coupling-specific exponent ordering, including reversal across contrasting tasks. An audit of released emergence trajectories identifies the controls needed for a direct factorial test that measures geometry separately from the scaling fit.

---


### 83. [TruncGradGS: Improved 3D Gaussian Splatting via Truncated Gradient Updates](https://arxiv.org/abs/2609.03534)

**<font color=#1a73e8>作者：</font>** Theo Morales, Nhat-Quynh Le-Pham, Robin Atkins 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting has become a de facto scene representation for novel view synthesis, yet robustly learning 3D Gaussian primitives from visual input remains challenging. Standard optimization relies on gradient-based updates, but a common issue is the gradient vanishing phenomenon: a pixel far from a Gaussian primitive often has diminishing gradient magnitudes to influence primitive attributes, resulting in suboptimal scene reconstruction. In this paper, we propose a method to address gradient vanishing with a piecewise truncated gradient formulation that improves the optimization stability and robustness to initializations. We show that our method consistently improves 3D Gaussian Splatting with random and COLMAP initializations while being generalizable across static and dynamic Gaussian Splatting. As a by-product, we also examine the limitations of current benchmarks for dynamic scenes, and introduce a novel dataset for benchmarking dynamic Gaussian Splatting using synthetic 3D scenes. We demonstrate the effectiveness of our method in both static and dynamic settings for the public benchmarks and our proposed dataset.

---


### 84. [The Native-Signature Boundary in Post-Quantum Distributed Authorization](https://arxiv.org/abs/2609.03547)

**<font color=#1a73e8>作者：</font>** Dariia Porechna  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-quantum signature migration poses a distinct systems problem when authorization is distributed among multiple parties. In native threshold signing, the signature algorithm may determine key generation, share state, preprocessing, interaction, combination, refresh, and recovery. Architectures that evaluate threshold policy outside the native signing relation can reduce this coupling, but their authorization evidence is not accepted by an unchanged native verifier unless a trusted complete-key signer translates approval into a native signature.
This paper organizes that design boundary through three properties: native-signature compatibility, unilateral-signing resistance, and threshold-layer agility. We classify specialized threshold signatures, generic MPC signing, distributed hash-based constructions, programmable multisignature and dual-gate authorization, and threshold-authorized HSM signing. A migration impact surface identifies which components change with the signature algorithm. Across the surveyed families, no design simultaneously provides native output, unilateral-signing resistance, and threshold-layer agility. This is an architectural tension, not an impossibility claim, and it clarifies why a replaceable API alone does not make distributed authorization cryptographically agile.

---


### 85. [WIDE: Wildcard Inference with Dynamic Expansion for Cross-Modal Generative Retrieval](https://arxiv.org/abs/2609.03554)

**<font color=#1a73e8>作者：</font>** Teng Guo, Xin Wang, Jiayou Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative retrieval has demonstrated significant success by unifying representation learning and search into a single sequence-to-sequence generation task. However, extending this paradigm to cross-modal retrieval reveals a critical challenge arising from the inherent information asymmetry across different modalities, such as the gap between concise text queries and dense visual candidates. This structural mismatch causes the autoregressive decoder to suffer from forced hallucination when generating identifiers via standard trie-constrained beam search, where the model is severely penalized for failing to guess fine-grained details absent from the query, allowing irrelevant candidates to hijack top rankings. To address this issue, we propose Wildcard Inference with Dynamic Expansion (WIDE). WIDE employs Adaptive Entropy Thresholding (AET) to calibrate layer-specific uncertainty boundaries offline. During the decoding generation phase, Asymmetry-aware Wildcard Decoding (AWD) detects semantic blind spots and emits wildcards instead of forced deterministic identifiers, dynamically expanding the search space without incurring log-probability penalties. Finally, Blind-Spot Re-ranking (BSR) evaluates the expanded candidate pool using a hybrid scoring mechanism that combines discrete generation confidence with continuous semantic similarity. Extensive experiments on the M-BEIR benchmark demonstrate that WIDE outperforms state-of-the-art generative retrieval methods, effectively suppressing forced hallucination while maintaining compact index structures.

---


### 86. [Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation](https://arxiv.org/abs/2609.03557)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Songchun Zhang, Haoran Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-conditioned video models require large-scale visual data paired with control signals that are temporally aligned with the resulting scene transitions. Such supervision is difficult to obtain from ordinary real-world video because the actions that caused each visual change are typically unknown. We present a large-scale synthetic data production pipeline built on Unreal Engine for generating action-conditioned, multi-view video. To accommodate the different execution requirements of real-time physics and high-quality offline rendering, the pipeline executes trajectory generation and final rendering in two stages: Stage I runs real physics in PIE and records per-frame character states, control inputs, and camera states into an intermediate trajectory representation; Stage II replays those trajectories in a new engine process and renders them offline with Movie Render Queue (MRQ). Around this core, we develop a distributed production system with cache-aware task partitioning, node-local slot scheduling, automated scene screening, aesthetic and luminance filtering, partial-output recovery, asynchronous upload, and continuous cluster health monitoring. The production cluster contains 25 servers with eight NVIDIA RTX 5090 GPUs per server. From 2,384 asset packs, 429 levels were retained for production together with a pool of 40 humanoid characters. The pipeline has produced 2,691 hours of 1080p video and 6,076 hours of 720p video. We describe the system architecture, the implementation decisions that emerged from production failures, and the limitations of using perceptual quality proxies for world-model data curation. The pipeline described in this report constitutes the Unreal Engine synthetic-data production component used in EchoWM.

---


### 87. [FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow](https://arxiv.org/abs/2609.03563)

**<font color=#1a73e8>作者：</font>** Byeongjun Park, Byung-Hoon Kim, Hyungjin Chung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FlashRender, a few-step generative rendering framework that retakes a source video along a target camera trajectory in seconds. We identify sampling-step-dependent camera control as a prominent manifestation of discretization error in existing multi-step generative rendering models and show that resolving this inconsistency substantially lowers denoising trajectory curvature, facilitating subsequent step distillation. To this end, we introduce Representation Transformation and Alignment (RETA), which aligns hidden source-video representations with target-video features from a frozen visual geometry model. This directly encodes the geometric transformation within the source-video stream, enabling sampling-step-consistent camera control. We then fine-tune the model with the MeanFlow objective on the lower-curvature denoising trajectory induced by RETA, allowing the model to more effectively address discretization error. Finally, we apply on-policy flow map distillation to correct self-rollout errors under fixed few-step sampling. Extensive experiments show that RETA, MeanFlow, and on-policy flow map distillation play complementary roles in few-step generative rendering. Together, they enable our approach to match multi-step baselines in video quality and geometric consistency at 25x lower sampling cost while achieving superior camera controllability, even under out-of-distribution target camera trajectories.

---


### 88. [Occlusion-Robust Multimodal Emotion Recognition in VR via Fusion of Facial Images and EMG](https://arxiv.org/abs/2609.03569)

**<font color=#1a73e8>作者：</font>** Birgit Nierula, Karam Tomotaki-Dawoud, Mert Akguel 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Head-mounted displays (HMDs) fundamentally limit emotion recognition in virtual reality (VR): by occluding the upper face, they render conventional image-based facial expression analysis incomplete, particularly for applications requiring real-time affective assessment. We address this challenge by fusing lower-face video with facial electromyography (EMG) from the occluded upper face to classify seven emotional categories (six basic emotions plus neutral). We introduce a synchronized multimodal dataset from 20 participants, pairing lower-face video with seven-channel upper-face EMG elicited by validated emotion stimuli. Under subject-independent test, our proposed late-fusion architecture merging convolutional visual embeddings with RBF-kernel EMG representations achieves 51% macro-F1, outperforming both image-only (41%) and EMG-only (43%) baselines. These results demonstrate that upper-face EMG provides robust complementary information under HMD-induced visual occlusion and establish a foundation for multimodal emotion recognition in naturalistic VR environments. This approach facilitates affect-adaptive applications, including communication training and therapeutic interventions. The dataset will be shared upon request under an ethical-use agreement.

---


### 89. [Drive-HWM: Hierarchical World Models for Dynamic-Latent Guided Autonomous Driving](https://arxiv.org/abs/2609.03572)

**<font color=#1a73e8>作者：</font>** Zhaoxin Fan, Tianbao Zhang, Wenjun Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models offer a promising paradigm for autonomous driving by predicting how traffic scenes may evolve and using such predictions to support action generation. However, existing approaches either separate future prediction from action generation or jointly predict them at the same temporal scale, making it difficult to simultaneously achieve long-horizon anticipation and responsive, observation-grounded decision making. We present Drive-HWM, a hierarchical slow--fast world modeling framework that organizes future representation prediction and action generation at complementary temporal scales. The slow world model predicts multi-step future representations to capture extended scene evolution. To explicitly model the abundant motion dynamics in driving environments, we introduce Dynamic-Aware Latents learned through optical-flow prediction. Guided by these future representations, the fast model uses a lightweight multimodal backbone and an autoregressive expert to jointly predict the next frame and the immediate action from the latest observation. Next-frame prediction encourages the fast model to capture imminent scene evolution, while one-step action generation allows decisions to be continuously updated as new observations arrive. Extensive experiments on NAVSIM v1 and v2 demonstrate the strong driving performance of Drive-HWM. Comprehensive ablation studies further validate the effectiveness of the hierarchical slow--fast design, dynamics-aware future representations, and joint next-frame and action prediction.

---


### 90. [WeatherNext 3: Increasing resolution and performance of global weather models with raw observations](https://arxiv.org/abs/2609.03582)

**<font color=#1a73e8>作者：</font>** Stephan Rasp, Boris Babenko, Dominic Masters 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-of-the-art AI weather models have shown impressive medium-range forecast skill and computational efficiency, but suffer two key shortcomings: their forecasts have lower spatial and temporal resolution than the best physics-based models and they are exclusively initialized with and trained on analysis data. As a result, they cannot directly make use of observations, and any biases in the analysis are inherited by the forecast. WeatherNext 3 addresses these shortcomings and establishes a new state-of-the-art for probabilistic medium-range forecasting skill. First, WeatherNext 3 generates new forecasts every hour (rather than every 6 hours like traditional global models) by ingesting low-latency geostationary satellite data. Second, WeatherNext 3's temporal and spatial resolution are on par with physics-based global models, with hourly time steps and 0.1 degree resolution for single-level variables, including solar radiation and cloud cover. Third, WeatherNext 3 moves beyond traditional analysis variables by learning to predict satellite-derived precipitation estimates, as well as tropical cyclone and station observations. Modelling sparse station data allows WeatherNext 3 to make 2m temperature and dewpoint predictions at any location and time, conditioned on local geographical features, with substantially lower error than competing global models, even when evaluated against unseen stations. Together, WeatherNext 3's capabilities move operational AI-based weather forecasting beyond emulating the traditionally distinct stages of data assimilation, forecasting and post-processing, which helps to further push the frontier of performance and granularity for global weather prediction.

---


### 91. [Text2Thermal: Physics-Aware Thermal Image Synthesis from Textual Priors](https://arxiv.org/abs/2609.03585)

**<font color=#1a73e8>作者：</font>** Tayeba Qazi, Brejesh Lall, Prerana Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal infrared imaging offers reliable perception in darkness and adverse weather, but thermal datasets remain scarce, motivating extensive work on translating abundant RGB images into thermal. Such translation is fundamentally ill-posed as thermal appearance is governed by surface emissivity and object temperature, neither of which is observable in the visible spectrum, so a single RGB image is consistent with many valid thermal outputs. We argue that language offers a natural means of resolving this ambiguity, and propose Text2Thermal, a framework for physics-aware thermal image synthesis from textual priors. Rather than inferring the unobservable radiometric factors from RGB, we supply them explicitly through thermally grounded captions encoding material, weather, time-of-day, and heat-emission state, and adapt a pretrained Stable Diffusion backbone to the thermal domain. Because the radiometric content is determined entirely by the prompt, Text2Thermal synthesizes thermal imagery without requiring a registered RGB image at inference; where spatial guidance is desired, an optional control signal imparts scene geometry without disturbing the prompt-specified radiometry. Experiments on M3FD, FLIR, and FMB show that Text2Thermal achieves state-of-the-art FID among thermal image synthesis methods while offering text-level control that translation-based approaches cannot provide.

---


### 92. [The Attention Triangle in Audio-Video Models](https://arxiv.org/abs/2609.03586)

**<font color=#1a73e8>作者：</font>** Sagi Polaczek, Noa Kraicer, Gal Metzer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Audio-video diffusion models rely on cross-modal attention to coordinate text, sound, and visual content, yet this same mechanism can introduce subtle and systematic semantic leakage. We study these models by probing and analyzing the ``attention triangle,'' comprising the three cross-attention edges connecting the text, audio, and video streams, and examine how semantic information is routed across modalities during generation. Our analysis reveals that routing along the audio-video edge is bidirectional: audio can influence video generation, while video can influence audio generation. This edge is shaped by biases encoded in the model's parameters and emerges as a major contributor to leakage: when prompts are in tension with learned priors, cross-modal interactions may override the intended conditioning and reroute semantics toward visually canonical but incorrect outcomes. These effects suggest that semantic artifacts arise not merely from attention spreading beyond its intended target, but from structured, bias-driven interactions along specific pathways. Building on this perspective, we extract attention-derived signals that expose how semantics are distributed and grounded across modalities, and use them as a diagnostic tool to both analyze and deliberately incur leakage under controlled conditions. This enables us to probe the internal dynamics of cross-modal routing and isolate the role of individual interactions. We further leverage these signals to guide inference-time interventions that encourage more consistent cross-modal alignment. Extensive experiments support our analysis and demonstrate improved semantic grounding while preserving generation quality.

---


### 93. [How Far Can Synthetic Data Take Thai OCR?](https://arxiv.org/abs/2609.03595)

**<font color=#1a73e8>作者：</font>** Kunat Pipatanakul  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate what makes synthetic OCR supervision transfer to real Thai documents and use the resulting insights to build Wayu-Paxa-OCR-Zero, a Thai OCR model adapted without OCR labels from real Thai document pages. Synthetic data provide exact labels at scale, but "realism" conflates source domain, page context, typography, spatial structure, and glyph variation. We disentangle these factors with a controlled document-reconstruction pipeline and evaluate each variant under page- and crop-level training on printed and handwritten Thai documents. Non-text context has little consistent effect, whereas typeface diversity, two-dimensional structure, and real handwriting glyphs improve transfer; moreover, source-domain matching depends on training granularity, with in-domain reconstruction approaching real printed supervision under page-level training (1.82% versus 1.31% median character error rate) but underperforming out-of-domain reconstruction under crop-level training (15.59% versus 5.52%). Guided by these findings, we adapt the 0.9B-parameter PaddleOCR-VL-1.6 into Wayu-Paxa-OCR-Zero using 45,723 synthetic pages: relative to its base checkpoint, it reduces median character error rate from 6.64% to 1.24% on printed pages and from 74.87% to 20.55% on handwriting and outperforms Typhoon OCR v1 7B on all five evaluation sets, showing that synthetic-only training can be competitive.

---


### 94. [SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.03602)

**<font color=#1a73e8>作者：</font>** Jinyang Wang, Shiwei Li, Junjian Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models (WMs) have demonstrated strong potential for end-to-end autonomous driving by learning predictive representations of future scene dynamics. However, generating future videos during inference introduces substantial computational overhead, leading many recent driving WMs to adopt a single front camera as input for efficient deployment. This design restricts spatial coverage in safety-critical maneuvers such as lane changes, merges, and turns. To address this limitation, we propose SV-WAM, a surround-view world-action model (WAM) that preserves full six-camera observations while maintaining efficient inference. SV-WAM leverages future-video prediction as dense training supervision for action learning within a shared generative model, rather than as an inference-time output. At the core of this design is an action-centered causal mask that prevents action tokens from attending to future-video tokens during joint action-video denoising. Consequently, the video branch can be discarded at deployment, enabling efficient action-only planning. Furthermore, we introduce a differentiable drivable-area compliance regularizer that penalizes vehicle-footprint corners approaching or crossing drivable boundaries, improving planning safety and boundary awareness. Extensive experiments on the closed-loop NAVSIMv2 benchmark and the open-loop nuScenes benchmark demonstrate that SV-WAM achieves state-of-the-art planning performance with low inference latency and competitive zero-shot transfer capability.

---


### 95. [Neural-Network Maxent: a general extension with learned nonlinearity, applied to time-series for Desert Locust distribution modelling](https://arxiv.org/abs/2609.03603)

**<font color=#1a73e8>作者：</font>** Alessandro Grassi, Edoardo Kimani Bellotto, Wassim El Azami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Species Distribution Modelling (SDM) is essential for understanding how environmental conditions shape biodiversity, particularly for destructive pests such as the Desert Locust (Schistocerca gregaria), whose breeding dynamics are tightly coupled to rapidly evolving environmental conditions. Maxent has become the dominant method for presence-only data, but its reliance on a linear combination of hand chosen feature transforms limits its ability to capture the nonlinear, temporal relationships common in ecological monitoring, where covariates such as precipitation, soil moisture, and vegetation indices evolve meaningfully over time. Standard implementations flatten time-series covariates into independent features, discarding sequential structure that carries critical signal. We introduce RNN Maxent, an extension of the Maxent framework that replaces the fixed feature dictionary with a neural network, specifically a Gated Recurrent Unit (GRU), trained end to end via backpropagation. The approach preserves Maxent's presence only statistical foundations, background normalization, and probability calibration, differing only in that the nonlinearity is learned from data rather than fixed in advance. We apply RNN Maxent to map suitable habitat for the Desert Locust using 50 day environmental time series derived from ERA5 Land, MODIS, and Sentinel 3, maintaining a 7 day gap between covariates and presence records to yield forecasting behavior. Compared against standard Maxent, RNN Maxent improves performance across metrics (ROC AUC 0.862 std 0.036 vs. 0.792; F1 0.671 std 0.056 vs. 0.590).

---


### 96. [On the Interaction Between Model Compression and Test-Time Adaptation](https://arxiv.org/abs/2609.03604)

**<font color=#1a73e8>作者：</font>** Francesco Corti, Dong Wang, Young D. Kwon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks deployed in the wild must be both efficient and adaptable, requiring model compression and test-time adaptation (TTA). While both are well studied in isolation, their interaction remains poorly understood. We systematically analyze how structured compression affects a model's ability to adapt under distribution shift. Using ResNet-18 and ViT-Base on CIFAR-10-C and ImageNet-C, we evaluate multiple compression methods combined with standard TTA techniques. We introduce a diagnostic framework that examines representational expressivity and adaptation subspace compatibility. Our results reveal a consistent gap: although compressed models retain high accuracy under supervised adaptation, their TTA performance degrades significantly with increasing compression. We show that this stems from reduced representational diversity and structural constraints that limit recoverability. These effects strongly depend on the compression method, highlighting the need to design compression strategies that preserve adaptability.

---


### 97. [A computable representation of the physical laboratory enables verifiable workflows](https://arxiv.org/abs/2609.03621)

**<font color=#1a73e8>作者：</font>** Xiaobo Li, Luyao Ge, Xiaohui Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Making science computable requires representations of both scientific knowledge and the physical world in which scientific claims are tested. A computable representation of the physical laboratory is established through typed research objects, capability-bound operations and a compositional workflow algebra. It provides the physical-world counterpart to machine-readable knowledge, expressing workflows as programs over evolving laboratory states with explicit dependencies, decisions, iteration and concurrency. The representation was implemented in a modular agentic robotic laboratory by binding formal operations to executable Function Skills. For diverse scientific intents, capability-relative workflows were generated, while stateful simulation propagated object transformations and verified operation preconditions and laboratory constraints before dispatch. The proposed representation and its engineering framework jointly establish a general computational interface between agent reasoning and capability-bound physical transformations, providing a foundation for end-to-end autonomous scientific discovery.

---


### 98. [EraseSAE: Surgical Concept Erasure in Text-to-Video Diffusion Models via Sparse Autoencoders](https://arxiv.org/abs/2609.03629)

**<font color=#1a73e8>作者：</font>** Xinghao Wang, Dong Li, Wei Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-to-video (T2V) diffusion models have demonstrated remarkable generative capabilities, yet their reliance on loosely curated training data raises pressing safety and copyright concerns. Concept erasure offers a principled remedy by removing unwanted semantics from pretrained models while preserving remaining concepts. However, existing approaches typically operate at a coarse granularity misaligned with the fine-grained, distributed nature of concept representations, leading to incomplete removal or degraded generation quality. We argue that surgical erasure fundamentally requires intervention at the level of monosemantic features, where each unit encodes a single interpretable concept. To this end, we propose EraseSAE, a novel framework that leverages sparse autoencoders to achieve surgical concept erasure in DiT-based T2V diffusion models via a principled decompose-attribute-erase pipeline. We first introduce the Partitioned Convolutional Sparse Autoencoder, which decomposes dense spatiotemporal activations into disentangled, interpretable sparse features while preserving spatiotemporal coherence. A contrastive attribution mechanism then contrasts activations from paired prompts to isolate concept-specific feature kernels. At inference, timestep-resolved spatiotemporal masks derived from the identified kernels confine erasure to regions where the target concept is active, leaving unrelated content intact. Extensive experiments across diverse diffusion models and concept erasure tasks demonstrate that EraseSAE achieves precise and robust concept removal with minimal quality degradation, substantially outperforming state-of-the-art methods. The code is available at this https URL.

---


### 99. [Analysis of Prompt Engineering for Drug Toxicity Prediction](https://arxiv.org/abs/2609.03635)

**<font color=#1a73e8>作者：</font>** Mia MacGregor, Aakash Welgamage Don, Mark Bartlett  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical trials in the UK can cost up to £1.3 million, with approximately 90% drug failure rate. Toxicity is a major contributing factor in drug failure. Testing is time and cost intensive. In recent years, the use of artificial intelligence has been increasingly explored to aid in the prediction of drug toxicity, with extensive use of large language models (LLMs). However, LLMs can show considerable variation when minor changes are made to prompts, which raises concerns about their sensitivity to prompt engineering. Prompt engineering is used to optimise a prompt given to an LLM to generate the desired output. This paper proposes a method to analyse prompt engineering for drug toxicity prediction. The aim of the paper is to investigate the importance of prompt phrasing for drug toxicity prediction. LLMs were prompted to identify chemical properties of significance when predicting drug toxicity. Prompts were constructed to investigate; job role, prompt structuring, and rule interpretation. LLMs were then used to generate datasets, using the identified features from initial prompting, which were then passed to machine learning algorithms. The experiments show that the natural variance which occurs in LLMs outweighs any fine-tuning of prompts. There were, however, substantial improvements in model performance when using chemoinformatic code to extract features instead of using LLM-generated values. The proposed analysis methodology is applicable to a wide range of prompt types across different areas of bioinformatics.

---


### 100. [Stabilizing Camera-Controlled Novel View Synthesis at Inference Time](https://arxiv.org/abs/2609.03639)

**<font color=#1a73e8>作者：</font>** Prajwal Singh, Arjun Badola, Seema Kumari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free, camera-controlled novel view synthesis from a single image using pre-trained video diffusion models often becomes unstable under large camera motion and long generation horizons. Existing approaches commonly combine several inference-time components, making it unclear which design choices are most important for stability. We show that the main source of stability is simple. Decomposing camera motion into small autoregressive steps limits per-step geometric distortion and reduces error accumulation. A controlled camera-step study shows that performance remains stable for small motions and degrades more strongly as the per-step motion approaches $18$-$20^\circ$. We further evaluate geometry-constrained spatial attention and low-frequency appearance anchoring as supporting refinements, together with an efficient registration-free warping pipeline. Across RealEstate10K and MegaScene, CamTrol++ improves temporal and geometric consistency, downstream 3D reconstruction quality, and generation efficiency over training-free baselines. The method remains effective for 56-frame generation and under substantial controlled depth corruption. These results show that careful control of camera motion at inference time can substantially improve the stability of camera-controlled novel view synthesis without retraining or modifying the diffusion backbone.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-194](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
