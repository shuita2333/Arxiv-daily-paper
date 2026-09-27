# 📦 其他研究 | 2026年09月28日

> 本类共 **266** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 51. [PlenoCI: Plenoptic CharacterIstics for View Dependence Aware Change Classification](https://arxiv.org/abs/2609.28930)

**<font color=#1a73e8>作者：</font>** Jason Lai, Chamuditha Jayanga Galappaththige, Niko Suenderhauf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiance field representations such as 3D Gaussian Splatting (3DGS) natively encode complex visual phenomena such as occlusions and view dependence, but they are inherently underconstrained. Independently optimized reconstructions converge to different primitive configurations, even in unchanged regions. We introduce Plenoptic CharacterIstics (PlenoCI), a novel feature built from the plenoptic field these representations approximate. PlenoCI directly captures rich visual behaviors while ignoring Lambertian textures. By deriving closed-form analytic plenoptic derivatives from a 3DGS representation, we efficiently detect these 5D structures. Our approach is robust to underconstrained representations by construction, reporting two orders of magnitude fewer false positives between independent reconstructions of unchanged scenes than concurrent work. We demonstrate PlenoCI's utility on change classification. First, we detect changes with an instance-aware 3DGS pipeline, achieving state-of-the-art results on CL-Splats with a 25.7% mIoU gain over the strongest competitor, while remaining competitive on the more challenging PASLCD benchmark. Leveraging PlenoCI, we classify changes as geometric or appearance-based with a balanced accuracy of 0.735, comparable to the best performing baseline. We believe plenoptic derivatives and PlenoCI open new directions for view dependence aware understanding in visually complex environments. Code and data are available at this https URL.

---


### 52. [HelloWorld: Towards Practical Applications of Generative Driving World Models](https://arxiv.org/abs/2609.28931)

**<font color=#1a73e8>作者：</font>** Fan Lu, Hanshi Wang, Zijing Wang 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving world models provide a promising route toward scalable counterfactual data generation and interactive simulation beyond recorded driving logs. Realizing this potential requires a system that can generalize across diverse scenes, respond faithfully to prescribed controls, generate coherent multi-sensor observations, and operate efficiently under repeated inference. We present \textbf{HelloWorld}, a 2B driving world model system designed around these requirements. HelloWorld progressively specializes broad visual and motion priors from heterogeneous video data into controllable driving generation using ego pose, HD maps, and 3D boxes. A block-causal generation interface, together with adaptation to self-generated context, aligns the model with sequential simulation. The system further supports synchronized seven-camera RGB generation and conditional LiDAR synthesis, and is distilled toward few-step inference for efficient deployment. Experiments evaluate visual quality, control fidelity, cross-view consistency, robustness under repeated generation, inference efficiency, and LiDAR synthesis. Together, HelloWorld provides a unified framework for scalable driving data generation and interactive simulation.

---


### 53. [Response-state Learning for Transferable Vibrational Spectroscopic Characterization with Electron Prior](https://arxiv.org/abs/2609.28935)

**<font color=#1a73e8>作者：</font>** Zetong Li, Zhuosong Xie, Hengyu Fan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vibrational spectral prediction can become inaccurate when localized stereoelectronic environments perturb intermediate response states and high-risk response units dominate characteristic spectral fingerprints, making prediction across external chemical space difficult. SO(3) Equivariant Neural Kalman Networks (SENK) form a response-state cascade that combines an equivariant transformer backbone for Hessian, dipole-derivative and polarizability-derivative learning, an Equivariant Neural Kalman bridge for state-dependent refinement and reliability sensing, and an NBO-informed electronic-prior pathway coupling consistency regularization with bounded, branch-specific guided spectral calibration. SENK outperforms DetaNet on QM9S and QMe14S while preserving full-spectrum IR and Raman fidelity from small molecules to drug-like systems. SENK remains stable and selectively improves spectrally sensitive features in biomolecular systems with complex stereoelectronic effects. It therefore integrates tensor prediction, reliability diagnosis and physics-informed calibration, supporting transferable vibrational spectroscopy from molecular systems to functional molecular materials.

---


### 54. [AnomaSense: Anomaly-based Sensor Activation for Fine-Grained Human Activity Recognition](https://arxiv.org/abs/2609.28936)

**<font color=#1a73e8>作者：</font>** Xue Wang, Yang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Audio carries rich cues about human activities, and microphones are already built into most wearable devices. However, microphones also capture speech, and this privacy risk limits their use in Human Activity Recognition (HAR). We present AnomaSense, a sensor activation approach for wrist wearables that keeps the microphone off by default and turns it on for at most one second when an unsupervised anomaly detector flags an IMU segment that is likely to produce sound. The captured audio is further masked before it reaches the recognition model. We study 20 activities from 15 participants, organized into five groups in which activities share similar wrist motion but differ in the object or material involved. With IMU data alone, our recognition model reaches 78.98% accuracy in leave-one-participant-out validation. With the short, masked audio windows added, accuracy reaches 96.89% with no masking and stays above 86% when 90% of each one-second audio window is removed. On the same data, the anomaly detector triggers the microphone with 86.46% precision and 74.28% recall relative to sound events. We also report a small preliminary check of automatic speech recognition on masked speech, which shows that contiguous masking degrades recognition far more than point-wise masking at the same masking ratio. Our evaluation is a controlled, offline feasibility study. We describe the threat model, what the approach does and does not protect, and the steps needed before deployment.

---


### 55. [Passive LWIR Hyperspectral Ranging via Transmittance Extraction and Distance Alignment](https://arxiv.org/abs/2609.28967)

**<font color=#1a73e8>作者：</font>** Zhihe Chen, Chen Fan, Shuo Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Passive long-wave infrared (LWIR) hyperspectral ranging enables distance estimation in low-light and nighttime scenes by exploiting atmospheric absorption features in thermal radiance received through the this http URL estimation of temperature, emissivity, and distance is computationally expensive. Reference-range joint inversion also uses a distance-invariant effective attenuation coefficient, which can bias range this http URL introduce transmittance extraction and distance alignment (TEDA), which decouples range estimation from temperature--emissivity inversion. In the first stage, a baseline estimator with a data-fidelity term invariant to the known absorption direction yields two closed-form smoothing branches for the slowly varying thermal continuum. An observation-derived gate combines the branches, and subtracting the blended baseline in the log domain recovers atmospheric transmittance. The second stage estimates range by matching the recovered transmittance to sensor-domain transmittance models recomputed for each candidate distance. Monte Carlo simulations show that TEDA effectively reduces the ranging bias caused by the distance-invariant attenuation coefficient approximation. In a measured scene, TEDA's mean range estimates are closer to the LiDAR medians than those of reference-range joint inversion in both evaluated patches. TEDA processes a complete $256\times256$ region of interest in 8.19~s versus 159.47~s for reference-range joint inversion, an approximately 20-fold speedup.

---


### 56. [Spectral Graph Neural Networks with Hermite Polynomials: A Comprehensive Study](https://arxiv.org/abs/2609.28979)

**<font color=#1a73e8>作者：</font>** Shuang Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study spectral graph neural networks built from Hermite polynomials and propose HermNet, a simple model that combines a nodewise predictor with normalized Hermite propagation. Its sparse recurrence requires neither eigendecomposition nor a learned basis. We distinguish the basic model from optional coordinate calibration, response normalization and Gaussian derivative regularization. Hermite and other complete polynomial bases span the same degree-bounded filter space, but their coordinates can produce different optimization behavior under limited training budgets. We analyze this behavior through spectral signal energy, label sampling, changes in learned features and the bias--variance trade-off of regularization. Controlled synthetic experiments identify a regime in which plain HermNet outperforms matched polynomial-basis alternatives, including with a jointly trained nonlinear predictor. Curvature regularization further improves HermNet when the same functional penalty is available to every comparator. Fixed-predictor controls support the advantage under short training budgets, but longer training removes the plain-model lead. Matched real-data comparisons show accuracy deficits, and architectural and numerical studies identify further limits. Together, the analysis and experiments clarify when Hermite propagation is useful and how calibration and regularization affect its performance.

---


### 57. [Only What Was Seen: Observation-Gram Compaction of View-Dependent Appearance in 3D Gaussian Splatting](https://arxiv.org/abs/2609.28997)

**<font color=#1a73e8>作者：</font>** Krzysztof Pietroszek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most of the memory of a 3D Gaussian Splatting model holds spherical-harmonic colour coefficients, yet each Gaussian is seen only from the narrow cone of directions of the training cameras. We turn this into a distortion metric that other compressors can adopt: a per-Gaussian observation Gram matrix, accumulated from viewing directions and blending weights, is the exact first-order map from coefficient changes to squared image error and needs only the model and the camera poses. Under it, degree reduction becomes a closed-form projection that generalises truncation, degree allocation a Lagrangian rate-distortion problem, and vector quantisation the matrix-weighted Lloyd algorithm, of which Compressed3D's quantiser is the scalar case. Swapped into Compressed3D with everything else unchanged, the metric raises PSNR by +0.49 dB before fine-tuning, with SSIM and LPIPS following, and at matched rate still gains +0.32 dB without a single training image. A training-free stack built on the metric alone is 15% smaller than the image-free GSICO at equal quality on Mip-NeRF 360.

---


### 58. [Learning from Mixed-Quality Deployment Experience for Robot Manipulation](https://arxiv.org/abs/2609.29000)

**<font color=#1a73e8>作者：</font>** Yangang Ren, Yujie Yan, Zirui Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robot policies deployed in real environments naturally accumulate mixed-quality experience, including successful executions, partial progress, and failures. Although these rollouts provide valuable information for further learning, directly incorporating them into imitation learning may reinforce undesirable behaviors, while offline reinforcement learning often suffers from unreliable value estimation under sparse rewards and limited data coverage. We consider a practical post-deployment setting where learning relies only on naturally accumulated autonomous rollouts, without additional human corrections or exploratory interaction. To effectively exploit such experience, we propose Predictive Action Chunk Learning (PACL). PACL first learns a predictive chunk-level critic that evaluates temporally extended action sequences and augments temporal difference learning with future latent prediction, providing richer supervision for long-horizon value estimation. The learned critic then converts chunk-level Q-values into discrete quality conditions, which guide a diffusion actor to learn jointly from these mixed-quality experiences without treating all behaviors as equivalent supervision. At inference, the actor generates multiple action chunks and the critic selects the highest valued candidate. Experiments across simulated and real-world robot manipulation tasks show that PACL consistently improves the pretrained policy and outperforms strong imitation learning and offline reinforcement learning baselines.

---


### 59. [FluidRain: Incompressible Rain Flow as an Attention Bias for Loop-in-Loop Video Deraining](https://arxiv.org/abs/2609.29006)

**<font color=#1a73e8>作者：</font>** Pu Wang, Yongcong Wang, Wenhao Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing video deraining methods typically exploit neighboring frames through either explicit alignment or implicit spatiotemporal aggregation. Explicit alignment relies on accurate motion estimation, which can become unreliable under dense rain, while implicit aggregation avoids alignment but lacks explicit guidance on the directional and temporally coherent structure of rain. This leaves a gap between reliable temporal aggregation and explicit modeling of rain motion. To address these limitations, we propose FluidRain, a lightweight video derainer that uses divergence-free rain flow to guide Loop-in-Loop attention across scales and neighboring frames. Motivated by fluid mechanics, we model rain motion as a divergence-free image-space flow and use it to organize multi-scale and temporal aggregation. Specifically, FluidRain first estimates a rain-flow field for each frame and projects it onto the divergence-free subspace. The resulting flow steers window attention along rain streaks, enabling neighboring frames to be aggregated without explicit alignment. Since rain-flow structure is preserved across scales and nearby frames, Loop-in-Loop reuses the same attention operator across both dimensions, resulting in a three-frame model with only 0.80M parameters. Experiments on four benchmarks show that FluidRain remains competitive with substantially larger restoration models. We further examine how temporal evidence scales with different input views. To evaluate whether the model remains reliable when rain motion changes across frames, we introduce RainSyn-Gust, which injects controlled changes in rain-streak direction into existing benchmarks. We also develop a physics-based no-reference metric that evaluates real-rain removal without requiring clean targets.

---


### 60. [Growth-Inspired Graph Generation and Inverse Design of Mechanical Lattices via Dot Matrices Database Augmentation and GCNN](https://arxiv.org/abs/2609.29024)

**<font color=#1a73e8>作者：</font>** Weiyun Xu, Jiamu Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural load-bearing and transport networks are not assembled in a single step; they emerge through a temporally ordered process of growth, branching, reinforcement, and loop formation. Inspired by this developmental logic, this work introduces a morphogenetic graph-generation framework for mechanical lattices in which a discrete dot matrix provides potential nodes and the final architecture is created by sequential cross-layer and intra-layer growth. The same rule is visualized in two dimensions as a leaf-vein-like developmental sequence and implemented in three dimensions on a 3x3x3 nodal matrix containing 27 candidate nodes. A dataset of distinct three-dimensional lattices was evaluated by beam-based finite element analysis and represented directly as graphs. A graph convolutional neural network (GCNN) with three graph-convolution layers and dual global pooling learns the topology-property mapping and predicts effective compressive stiffness. Coupling the GCNN surrogate with rapid structural sampling enables inverse design: for a target stiffness of 1000 MPa, the selected design was predicted at 1042.43 MPa and validated by finite element analysis at 1027.49 MPa. Beyond straight members, the framework has also been extended to parameterized horseshoe-shaped curved beams made of nonlinear materials, enabling topology-geometry design toward prescribed deformation shapes. Our work provides a paradigm for augmenting the database of mechanical metamaterials, and the resulting perspective links biological morphogenesis, graph learning, and nonlinear shape programming in a unified generative design framework for architected materials.

---


### 61. [Generative Atmospheric Super-Resolution from Heterogeneous In Situ Observations through Composable Interfaces](https://arxiv.org/abs/2609.29027)

**<font color=#1a73e8>作者：</font>** Yang Xu, Dibyajyoti Chakraborty, Haiwen Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Atmospheric observations are sparse, heterogeneous, and unevenly distributed, whereas many generative atmospheric models learn distributions over regularly gridded multivariate states. Once pretrained, diffusion models can supply atmospheric priors that can be combined with observation-derived likelihood factors in a Bayesian formulation. However, these observation sources differ substantially in geometry and sampling density, complicating the consistent use of their observations within a common inference framework. Here, we formulate this reconstruction problem as generative atmospheric super-resolution and introduce composable observation interfaces for conditioning a single pretrained 13-variable atmospheric diffusion model. The interfaces convert sparse radiosonde (R), clustered aircraft (A), and dense irregular surface-station (S) observations into source-specific likelihood factors that specify where observations constrain the gridded state, how residuals are counted under uneven sampling, and how strongly each source guides posterior sampling. We developed the aircraft and surface observation interfaces using 2019 observations and evaluated the selected interfaces throughout 2020 without further tuning. Compared with reconstructions conditioned only on radiosonde observations, the composed R+A+S interface reduces RMSE evaluated against ERA5 by $9.24\%$ across all 13 state variables over the CONUS domain. The aircraft and surface factors provide complementary improvements in upper-air and surface variables. The R+A+S combination also lowers the Continuous Ranked Probability Score (CRPS), while evaluations at held-out aircraft and surface-station observations show reduced prediction errors. Together, these results demonstrate a modular route for conditioning a pretrained atmospheric generative prior on heterogeneous in situ observations without retraining the underlying model.

---


### 62. [RGBD20K: A Large-Scale Benchmark for RGB-D Semantic Segmentation](https://arxiv.org/abs/2609.29028)

**<font color=#1a73e8>作者：</font>** Shaohua Dong, Zexuan Meng, Haiyan Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose RGBD20K, a novel dataset for facilitating the development of more robust and general RGB-D semantic segmentation by encompassing abundant categories and high-quality annotations. RGBD20K possesses several attractive properties: (1) Expanded Semantic Space. In particular, it covers 160 fine-grained categories, largely surpassing the category diversity of existing popular RGB-D benchmarks (e.g., NYUv2 with 40 classes and SUN RGB-D with 37 classes). With such enriched semantic coverage, we expect to promote the learning of more generalizable segmentation models. (2) Larger Scale. Compared with current benchmarks, RGBD20K offers 20,000 RGB-D image pairs, providing a substantially larger training resource that benefits the development of more powerful deep models. (3) High-Fidelity Annotation. We perform rigorous re-evaluation and correction of existing labels to resolve long-standing annotation noise, resulting in a clean and reliable ground-truth foundation. Furthermore, we propose a novel score-purified fusion (SPF) method, which achieves state-of-the-art performance across all evaluated benchmarks, demonstrating the effectiveness of our approach in leveraging high-quality multimodal information for RGB-D semantic segmentation. The dataset is here: this https URL.

---


### 63. [Empath: Tracing Multi-Level Emotion Dynamics in Crisis Counseling Dialogues](https://arxiv.org/abs/2609.29056)

**<font color=#1a73e8>作者：</font>** Ziwei Gong, Yuchen Huang, Wen Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion dynamics are critical for understanding crisis-support conversations, yet most computational work treats emotion as static utterance-level labels. We introduce EMPATH, a framework for understanding affective dynamics in mental health dialogues across three granularities: turn-level labels, transition probabilities, and global conversation archetypes. Applying EMPATH to text-based crisis conversations with self-identified Black texters discussing grief, we find persistent negative affect, gradual hope-ward transitions, distinct texter-volunteer emotional roles, and heterogeneous recovery trajectories. These results highlight the informative patterns that emerge from computationally understanding crisis support and expressions of grief as dynamic processes within conversations, as well as the overall value of emotion-dynamic analysis for analyzing and comparing affect in dialogues.

---


### 64. [A Procedure for Classifying Attachments and Affective Social Bonds in Human-Robot Dyads](https://arxiv.org/abs/2609.29063)

**<font color=#1a73e8>作者：</font>** Imran Khan, Elisabeth Blagrove  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-robot interaction (HRI) claims that people form attachments and social bonds with artificial agents, yet the terms are often applied without the behavioural and physiological criteria that give them content in their source disciplines. Without this empirical grounding, studies deploy widely divergent methods, frequently producing expansive relational claims that far outstrip their underlying evidence. To address this, we propose a standardised four-question procedure, grounded in criteria established in the developmental, ethological, and neuroendocrine literatures, that classifies a given human-robot tie as an attachment, an affective social bond, or no relationship, with intermediate classifications when evidence is incomplete. We specify minimum evidential requirements for each question, and provide candidate HRI study designs, adapted from validated human-human, human-animal, and animal-animal paradigms. We then demonstrate the procedure by applying it to a representative set of published HRI studies, showing how often relational claims outstrip what the reported designs can establish. Finally, we discuss the ethical and regulatory burdens created when artificial agents engage human biobehavioural systems. By replacing the divergent operationalisations with a unified, criterion-based classification, this paper gives HRI practitioners a standardised basis for evaluating, classifying, and comparing human-robot relationships, and sets out the experimental rigour that each classification demands. We therefore call on researchers of human-robot relationships to adopt such rigour, or to consider alternative terminology in their descriptions of these ties.

---


### 65. [EIB-Net: Entropy-Guided Information Bottleneck for Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2609.29064)

**<font color=#1a73e8>作者：</font>** Zhida Zhang, Xinlei Ma, Jie Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proliferation of photorealistic AI-generated images demands robust detection methods that generalize across diverse generative models. While existing approaches target manipulation-based forgeries with local artifacts, generation-based images (e.g., from diffusion models) lack such traces, posing a fundamental challenge. We observe that generative models prioritize global semantics at the expense of local texture fidelity, making low-texture regions key indicators of synthetic origin. To exploit this, we propose EIB-Net, an Entropy-guided Information Bottleneck Network. EIB-Net introduces a novel Image Entropy (IE) metric to automatically select the most informative (lowest-entropy) patch, then processes it with a Variational Information Bottleneck (VIB) to learn compact, generalizable features. Extensive experiments on DIFF, DiffusionForensics, and GenImage benchmarks demonstrate state-of-the-art performance: EIB-Net achieves 85.7\% accuracy using only 2\% of training data, outperforming full-image baselines by over 15\%, and maintains robust cross-generator generalization (83.5\% average accuracy on GenImage). Furthermore, our entropy-guided patch selection (EGPL) consistently enhances diverse backbones (CNNs and Transformers), proving its practical value for data-efficient detection.

---


### 66. [BranchShine-CR: Compact Multilingual IPA Transcription with Self-Conditioned CTC and Consistency Regularization](https://arxiv.org/abs/2609.29069)

**<font color=#1a73e8>作者：</font>** Nikhil Navas, Sergio Chevtchenko, Talisson Damiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce BranchShine-CR, a 25M-parameter model for multilingual transcription into the International Phonetic Alphabet (IPA). It combines log-mel features, a rotary-position E-Branchformer encoder, intermediate self-conditioned connectionist temporal classification (CTC), and consistency regularization across augmented views. On 16,646 shared IPApack++ test utterances, it achieves 4.47% IPA character error rate, a 22.3% relative reduction from ZIPA-CTC-NS, with approximately one-twelfth as many parameters while being trained from scratch. BranchShine-CR also outperforms a similarly sized NeMo Conformer baseline across all 41 dataset language labels. Ablation studies indicate the individual components synergetically acting in model performance contribution. These findings support compact IPA recognition capabilities under limited compute budget, for applications in low-resource on-device pronunciation assessment.

---


### 67. [A Rapid Pipeline for Training and Deploying ML Models on WeBe Band](https://arxiv.org/abs/2609.29084)

**<font color=#1a73e8>作者：</font>** Ehsan Kourkchi, Asmita Asmita, Houman Homayoun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing optimized machine-learning algorithms for edge devices with limited computational and memory resources is challenging, time-consuming, and highly dependent on device-specific constraints. In this work, we streamline an edge ML workflow to enable rapid development, optimization, and deployment of machine-learning (ML) models directly on the WeBe Band, a wrist-worn wearable device designed for multimodal physiological data monitoring. The proposed system automatically generates hardware-efficient ML models that can be easily integrated into the WeBe core firmware, supporting AutoML, hardware-aware quantization, and performance profiling to build models that meet desired latency targets while remaining compatible with device memory and power limitations.
The proposed framework tightly integrates the open-source Piccolo AI ecosystem with an automated pipeline that generates deployable firmware artifacts, performs hardware-aware model compilation, and supports over-the-air (OTA) deployment. The system supports multiple lightweight model classes, including classical machine-learning algorithms and neural networks, and provides built-in on-device profiling tools to evaluate inference latency and memory footprint under realistic execution conditions. Experimental results demonstrate clear trade-offs between model complexity and deployability on a microcontroller, showing that classical models offer strong real-time performance while lightweight neural networks require careful resource management.
Rather than proposing new learning architectures, the current work mainly focuses on system-level automation, deployability, and enabling researchers and developers to rapidly iterate on models and evaluate them directly on target hardware. Although demonstrated on the WeBe Band platform, the workflow is designed to be extensible to other ML-powered edge devices.

---


### 68. [Physics and Data Driven Transformer-Mamba Framework for Flow Field](https://arxiv.org/abs/2609.29087)

**<font color=#1a73e8>作者：</font>** Zhuo Zhang, Shun Zou, Canqun Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While deep learning accelerates expensive partial differential equation solving in computational fluid dynamics (CFD), existing methods like PINNs and FNOs often struggle with generalization, noise robustness, and physical consistency. We introduce the Transformer-Mamba for Flow Field (TM4FF) framework, a physics-constrained operator learning model with three key innovations: a Residual Wavelet Mamba (RWM) layer for feature denoising, a Transformer-based attention mechanism for enhanced feature fusion, and a physics-informed loss using Fourier derivatives to enforce the Navier-Stokes equations. Experiments on four CFD datasets show TM4FF achieves high accuracy and robust generalization across varying flow conditions.

---


### 69. [Can Classical Semantic-Extractive Summarization Be Evaluated in Hindi? A Replication Study](https://arxiv.org/abs/2609.29090)

**<font color=#1a73e8>作者：</font>** Showket Ahmad Khan, Mudasir Mohd, Nasrullah Sheikh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We replicate the distributional-semantics extractive summarisation method of Mohd, Jan and Shah (2020) and adapt it to Hindi, substituting a Devanagari-appropriate component at every language-specific step. The system is evaluated on two independent corpora --- the Hindi portion of XL-Sum and FIRE ILSUM 2.0 Hindi --- under a Devanagari-aware ROUGE implementation validated against the XL-Sum authors' own multilingual scorer, with all comparisons drawn as 1000-resample paired bootstraps. In its published equal-weight configuration the replicated system is significantly worse than a three-sentence lead baseline on both corpora, trailing Lead-3 by 0.042 ROUGE-1 Fon XL-Sum and by 0.265 on ILSUM. A feature ablation shows that sentenceposition is the only feature that contributes: position alone reproduces the lead baseline exactly, removing position gives the weakest configuration,and a validation-tuned weighting can at best equal Lead-3 and never exceed it. TextRank fails identically, making this a class-level rather than an implementation-level result. A selection analysis shows the remaining features steer extraction towards long, entity-dense body sentences while the references reuse the article this http URL Hindi benchmarks therefore cannot reward non-lead content selection, motivating purpose-built evaluation resources.

---


### 70. [Downside-Controlled Online Forecast Combination under Delayed and Revised Outcomes](https://arxiv.org/abs/2609.29096)

**<font color=#1a73e8>作者：</font>** Minkyoung Kim, Hyunjung Byun, Yohan Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc correction adjusts a forecaster that cannot be retrained, such as a foundation model, but a correction fitted where errors are stable can hurt where they shift. We aim for downside control: not much worse than the starting forecast. We combine the frozen forecaster, a static corrector and an online corrector on the simplex, using only losses that mature after the horizon. Across seven benchmarks and four base models, two of them foundation models, the worst deterioration over 28 pairs at the main horizon is 0.15% and gains reach 11.5%. On day-ahead load for seven European bidding zones it lowers mean MSE in all seven zones, while single correctors raise mean MSE by up to 102% where the published forecast is most accurate. Three empirical conditions on expert speed, stream length and outcome alignment, each fixed by a documented failure, delimit its scope. Learning from the provisional outcome improves four zones on the settled one; learning on the settled outcome restores all seven.

---


### 71. [Functional Architecture of European Electricity Trading Markets: Requirements for AI Supported Trading Systems under Regulatory Constraints](https://arxiv.org/abs/2609.29108)

**<font color=#1a73e8>作者：</font>** Walter Kurz, Wojtek Stricker  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> European electricity trading in the EU operates as a constrained multi-layer system in which legal design, exchange microstructure, and network physics are executed jointly across forward, day-ahead, intraday, and balancing horizons. This paper develops a functional architecture for AI-supported trading that is aligned with market-coupling mechanics, cross-zonal transfer constraints, and compliance obligations under REMIT, MiFID II, MiFIR, and EMIR. The contribution is a formal system specification composed of a decision-state vector, residual-exposure accounting, constrained optimization objective, executable-action permission gate, and fail-closed AI control logic with auditable records. The analysis maps major Nominated Electricity Market Operator (NEMO) venues and related exchange operators into an operational venue topology and identifies where cross-border coordination fails in practice: interface-level timing, permission heterogeneity, and balancing-layer coupling. The resulting framework proposes how AI can be deployed as a bounded decision component inside regulated market operation with explicit governance, rather than as an unconstrained prediction layer.

---


### 72. [Spectral Amplitude Purification in Distribution Matching for Diffusion Distillation](https://arxiv.org/abs/2609.29116)

**<font color=#1a73e8>作者：</font>** Zhenyu Zhou, Can Wang, Chun Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution Matching Distillation (DMD) enables high-quality diffusion sampling in only a few steps, but its optimization dynamics remain dominated by coarse, low-frequency signals, delaying the recovery of fine-grained details. We identify a pronounced concentration of spectral amplitudes at low frequencies in the DMD directional error, where dominant low-frequency components overwhelm weaker mid- and high-frequency signals. To address this issue, we propose Spectral Amplitude Purification for Distribution Matching Distillation (SAP-DMD), a plug-and-play approach that adaptively modulates the amplitude spectrum of the DMD directional field. By suppressing the dominant tail of the amplitude spectrum, SAP-DMD reduces low-frequency dominance and promotes more effective recovery of fine structures and textures. Experiments on PixArt-$\alpha$, SD3, and SD3.5 demonstrate that SAP-DMD accelerates training convergence and improves generation quality under both 2-step and 4-step sampling.

---


### 73. [A Concentration Bound for Two-Timescale Actor-Critic Algorithm](https://arxiv.org/abs/2609.29117)

**<font color=#1a73e8>作者：</font>** Prashansa Panda, Shalabh Bhatnagar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Significant research effort has been directed in recent years towards establishing both asymptotic and non-asymptotic convergence guarantees for two-timescale actor--critic algorithms, where the actor recursion is run on a slower timescale than the critic recursion. This work derives a uniform all-time concentration bound for the actor--critic algorithm with function approximation in the long-run average-reward setting. This bound helps us analyze the behavior of the actor parameter with high probability. We show that, after some finite time, the actor parameter enters a safe region and remains within it thereafter with high probability. Specifically, with probability at least $1-\epsilon_1-\epsilon_2$, the actor error $\Vert \theta_k-\theta^{*}\Vert$ is $O\left(\frac{n_0^{3/4}}{k}\frac{1}{\sqrt{\epsilon_2}}+\left(\frac{1}{n_0}\right)^{1/4}\log^{1/4}\left(\frac{1}{\epsilon_1}\right)+\left(\frac{1}{n_0}\right)^{1/4}\right)$ for all $k\geq n_0$ and sufficiently large $n_0$. We also present experimental results demonstrating that the aforementioned actor error diminishes with the number of actor-parameter updates.

---


### 74. [UpDown-SC: Gravity-Canonicalized Dual-Envelope Scan Context for Indoor LiDAR Place Recognition](https://arxiv.org/abs/2609.29118)

**<font color=#1a73e8>作者：</font>** Jie Xu, Yongxin Yang, Ziyi Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR place recognition is a key front end for loop closure and global relocalization, yet indoor retrieval remains difficult when attitude or sensor mounting height changes between mapping and query sessions. Scan Context stores the maximum height in each polar cell; indoors, broad ceilings can suppress the lower and mid-level geometry that distinguishes adjacent rooms and corridors. We present UpDown-SC, a training-free polar descriptor that first canonicalizes gravity and then represents two complementary surfaces: the upper envelope of lower/middle structures and the lower envelope of overhead structures. Their physical split is estimated once from a cell-balanced map height distribution and reused by every query. A mask-aware, non-uniform two-channel distance retains discriminative lower-level evidence while limiting sensitivity to its cross-session variation, without treating unobserved cells as zero-height measurements. Conventional Scan Context shortlisting and circular yaw alignment are retained, so retrieved hypotheses directly initialize geometric verification. Experiments across repeated indoor sessions, mounting-height changes, mixed outdoor-to-indoor trajectories, and an outdoor transfer sequence show more reliable first-choice retrieval on the indoor and mounting-height-varied sessions. A paired test finds a significant gain over Scan Context on the in-house sessions. UpDown-SC also gives the best or second-best F1max and AUPR under threshold-based acceptance while retaining a lightweight CPU front end. Continuous replay confirms that the retrieved hypotheses support metric prior-map localization. Code and evaluation artifacts: this https URL.

---


### 75. [Less is More: Encoder-only Audio-Visual Segmentation](https://arxiv.org/abs/2609.29121)

**<font color=#1a73e8>作者：</font>** Ilpo Viertola, Vladimir Iashin, Sophie Tötterström 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-Visual Semantic Segmentation (AVSS) aims to identify, segment, and classify sound-emitting objects in video frames. Previous Transformer-based AVSS approaches largely inherit design principles from image segmentation models. Recent studies show that these image segmentation models contain redundant components that contribute little to the segmentation performance. Following this insight, we propose Encoder-only Audio-Visual Segmentation (EASE). EASE runs at up to 365 FPS, 3x faster than prior State-of-the-Art (SotA) AVS models at comparable accuracy, and trains in under 11 GPU-hours. Furthermore, we achieve SotA AVSS performance across different backbones and input resolutions. Our results demonstrate that AVSS can be both simpler and faster, providing a scalable foundation for future research and real-time applications. Code, model weights, and samples are available at this https URL

---


### 76. [FoCal: Frequency-Oriented Cross-Modal Interaction and Spectral Calibration for Aerial Visible-Infrared Object Detection](https://arxiv.org/abs/2609.29125)

**<font color=#1a73e8>作者：</font>** Ben Liang, Chao Sui, Junqi Bai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In aerial RGB--IR object detection, effectively exploiting complementary information across modalities is critical for robust perception under complex illumination and environmental conditions. Existing multimodal detectors mainly focus on spatial-domain interaction or frequency-specific feature enhancement, while the cross-modal interaction patterns of different frequency components remain insufficiently explored. Moreover, spectral discrepancy itself may contain both useful complementary cues and unreliable modality-specific responses, making indiscriminate frequency fusion suboptimal. To address these issues, we propose FoCal, a frequency-oriented framework for aerial RGB--IR object detection. First, a Frequency-Aware Dual-Domain Calibration (FADC) module is developed to explicitly model frequency-dependent cross-modal interaction. Low-frequency components are collaboratively consolidated into a shared structural consensus, whereas high-frequency components preserve modality-specific information through selective cross-modal exchange. The resulting frequency-aware cues are further transferred to the original feature domain to regulate cross-modal calibration. Second, we introduce a Discrepancy-Guided Spectral Modulation (DGSM) module, which characterizes cross-modal spectral imbalance using confidence-weighted relative amplitude discrepancy and transforms it into a bounded signed gate for adaptive enhancement, preservation, or attenuation of the joint multimodal spectrum. Extensive experiments on DroneVehicle, ESCVehicle, and ATR-UMOD demonstrate the effectiveness of FoCal, yielding $\mathrm{mAP}_{50}$ values of 83.5\%, 54.8\%, and 64.6\%, respectively. Meanwhile, with only 3.0M parameters, FoCal achieves 113.6 FPS while preserving leading detection accuracy, highlighting a favorable accuracy--efficiency trade-off. Code is available at {this https URL.

---


### 77. [The Fly That Stopped: Mushroom-Body-Inspired Habituation as a Reward-Free Scheduling Prior for Autonomous Penetration Testing](https://arxiv.org/abs/2609.29126)

**<font color=#1a73e8>作者：</font>** Theodoros Moutesidis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous security-testing agents can spend much of a fixed action budget repeating earlier tool selections. We evaluate a reward-free scheduler inspired by mushroom-body novelty processing in Drosophila. It combines sparse state encoding with decaying habituation counters over structural URL classes and tool families. The counters penalize repeated clean or error outcomes without updating weights from scalar reward. Four matched campaigns motivated this design by exposing reward-accounting errors and tool-failure loops; reward-driven components did not improve the tested primary outcomes over the reward-free MB condition. A pre-registered pilot and two confirmatory stages then evaluated repeated (tool, URL) selections. In the second confirmatory stage, 8 of 10 screened lab targets remained measurable after two error-heavy slow-XSS exclusions. The habituation-enabled scheduler lowered duplicate-action ratios in all 6 non-tied target pairs (exact one-sided p=0.015625), with two ties; the largest reduction was 51 to 18 duplicate steps within a 60-step budget. This is evidence for the complete scheduler on the measurable budget-hold population, not an isolated habituation ablation or a vulnerability-discovery gain. A complementary study on a 13,498-neuron MaleCNS-derived circuit (501,267 synaptic edges with weight at least 5) found no action selectivity from the five tested local-plasticity approaches under a fixed readout; readout plasticity produced qualified positive results in synthetic tasks without establishing a biological-topology advantage. We report the population bounds, remaining input-integrity dependencies, and an internal AI-assisted review protocol alongside the results.

---


### 78. [Sharp Limits for Honest Uncertainty in Hard-Budget Repeated Evaluation](https://arxiv.org/abs/2609.29140)

**<font color=#1a73e8>作者：</font>** Yezhou Cheng, Runjia Du, Zeming Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Repeated evaluation can estimate a benchmark score accurately while still requiring replication to certify narrow uncertainty. We characterize that requirement on a fixed grid of $M$ tasks with $L$ binary paths per task under the hard budget $(M+t)K$, where each path costs at most $K$ responses or episodes. For fixed $L \ge 3$ and $0 < \alpha \le 1/12$, the optimal expected width on the worst pure cohort is $\Theta_{\alpha,L}([M(t+1)]^{-1/2})$ when every task is observed and $\Theta_{\alpha,L}([M(t+\sqrt{M})]^{-1/2})$ when omission is allowed. The lower bounds cover adaptive hard-budget policies, and fixed random-subset designs attain both rates through disagreement certificates. A joint mean/disagreement interval turns the task-covering law into practical finite-budget inference. In an equal-budget LiveCodeBench replay with 16 models, 880 tasks, and five outputs per task, the task-covering design reduces median point-estimation MSE by 87.0\% relative to pooled uniform sampling, while the Joint certificate produces narrower confidence intervals in 15/16 panels and reduces median interval width by 30.6\%. Finite-regime analyses identify task coverage as the effective choice at the evaluated scale and characterize how cohort size and within-task agreement determine the useful operating region. Together, the sharp laws and fixed-budget evidence make replication and task coverage explicit design variables for information-efficient repeated evaluation.

---


### 79. [Claim-Gated Source-Risk Auditing for Generative Search](https://arxiv.org/abs/2609.29145)

**<font color=#1a73e8>作者：</font>** Kainan Zhou, Chuhong Xu, Gangzhen Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A generative search answer can cite a supported passage yet omit a source relationship that changes its interpretation. We specify a claim-gated audit of the query-source-answer tuple. An omission is resolved only when relationship evidence, answer adoption, materiality, and disclosure are all observed; incomplete evidence remains unresolved rather than being treated as independence. The specification separates this endpoint from citation support and review priority, and binds decisions to versioned evidence spans. A reference checker makes the record contract executable. On an exhaustive synthetic suite, it reproduces all 81 three-state predicate combinations and rejects 192 deliberately malformed records. Common-guard baselines and predicate ablations isolate endpoint logic from missing-evidence handling, while controlled transitions check support separation and evidence removal. These are finite contract-conformance results, not detector accuracy or evidence of improved user outcomes. We define the independent annotation, held-out evaluation, and paired utility tests still required to establish semantic validity and deployment benefit.

---


### 80. [BanglaKontho: Closing the Long-Form Gap in Bangla Text-to-Speech](https://arxiv.org/abs/2609.29146)

**<font color=#1a73e8>作者：</font>** Mizbaul Haque Maruf  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bangla, the seventh most spoken language in the world, remains under-resourced for neural text-to-speech. Public Bangla speech corpora are dominated by short read-prompt utterances collected for speech recognition, leaving long-form prosody and consistent single-speaker narration uncovered. We present BanglaKontho, a single-speaker Bangla TTS corpus of 20 hours derived from professional audiobook recordings: 7,050 segmented utterances with verified transcripts at 24 kHz. We also release a reusable Bangla text normalizer covering Bangladeshi-style digit grouping, currency and date expressions, Danda punctuation and Unicode normalization, together with the full preprocessing pipeline. An MB-iSTFT-VITS baseline trained from scratch reaches 9.5% WER and 4.46 naturalness MOS, against 16.0% and 3.16 for the same architecture retrained on the 12-hour IndicTTS-Bn corpus. The corpus is released openly under CC BY-NC 4.0.

---


### 81. [A Particle-Swarm-Assisted Gradient Meta-Learning Algorithm for Joint Transmit Precoding and STAR-RIS Coefficient Optimization](https://arxiv.org/abs/2609.29150)

**<font color=#1a73e8>作者：</font>** Kang Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates the joint optimization of the transmit precoder and the transmission/reflection coefficients of a simultaneously transmitting and reflecting reconfigurable intelligent surface (STAR-RIS) to maximize the weighted sum rate (WSR) in a multi-user downlink. We propose a particle-swarm-assisted gradient meta-learning (PSA-GML) algorithm for this non-convex problem. The original problem is first equivalently transformed via an amplitude-split parameterization and a collapsed precoder representation, which automatically satisfy the energy-conservation constraint and reduce the search dimension. Particle swarm optimization (PSO) then performs a global search over the STAR-RIS coefficients to yield a high-quality, initialization-robust warm start, with the transmit precoder obtained in closed form. Departing from conventional alternating optimization (AO), a coordinate-wise long short-term memory (LSTM) meta-optimizer trained by first-order gradient meta-learning further refines the coefficients and precoder jointly, learning per-coordinate adaptive update rules from data. The meta-optimizer is trained offline and applied to unseen channels without further adaptation. Numerical results show that PSA-GML attains an 11.06 bits/s/Hz WSR at 10 dB with N=32 elements and K=4 users, exceeding AO by 13.1% (and by 6.2% even with multiple random restarts) and the random-phase scheme by 35.1%. In the interference-limited regime it reaches 83.9% of the hand-designed Adam refinement without manual hyper-parameter tuning, and it transfers zero-shot across regimes, indicating that the learned update rule captures the intrinsic WSR landscape structure.

---


### 82. [Recoverable Geographic Location Information in Earth-Observation Embeddings](https://arxiv.org/abs/2609.29151)

**<font color=#1a73e8>作者：</font>** Peiwen Zhang, Kristie Hu, Jovana Knezevic 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth-observation (EO) foundation models provide reusable embeddings, yet downstream task accuracy does not reveal whether these representations encode geographic information, which may be beneficial for location-aware applications but potentially detrimental when representations invariant to geographic location are desired. We therefore evaluate the geographic coordinate robustness of Tessera v1, Tessera v1.1, and AlphaEarth by testing whether coordinates can be predicted from the embedding representations using 284 quality-verified European solar farms from 2024. We assessed geographic information content information through the association between cosine and geodesic distances and through prediction of projected coordinates in EPSG:3035. Embeddings from all three EO foundation models contain recoverable geographic information. All prediction models significantly outperform training-range uniform random sampling baselines, with AlphaEarth exhibiting the strongest distance association and lowest mean geodesic error. Both Tessera variants also yielded higher geographic distance correlations than the Sentinel-2 controls. These findings motivate geographic information content as an additional criterion for auditing EO foundation models.

---


### 83. [Edge AI on Constrained Devices for Binary Sleep-Wake Classification in Dynamic Environments](https://arxiv.org/abs/2609.29163)

**<font color=#1a73e8>作者：</font>** Stefan Reitmann, Lena Oden  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents an Edge AI-based system for detecting sleep and wake states in non-stationary mobile environments using resource-constrained embedded hardware. Conventional approaches relying on accelerometer-based activity metrics are highly susceptible to motion and vibration artifacts and are limited by strict compute and energy budgets of wearable and IoT devices. To address these challenges, a multimodal pipeline is designed and implemented on an ESP32-S3 microcontroller.
The system combines inertial sensing for head movement analysis and visual pose classification. A dual-core architecture with FreeRTOS enables parallel execution of real-time data acquisition and on-device inference. Sleep detection follows a two-stage strategy: low-movement detection over a temporal window, followed by visual validation of poses.
Experimental results show accuracies of 96.5% for motion-based detection and 89% for pose classification, yielding robust binary sleep-wake classification. Field tests confirmed feasibility in representative mobile scenarios. The results demonstrate that privacy-preserving, local sleep detection is achievable on edge hardware through careful co-design, while highlighting limitations in sensing intrusiveness, dataset scale, and system integration.

---


### 84. [Through Human Eyes and Machine Eyes: Understanding View Mismatch in Video See-Through Extended Reality](https://arxiv.org/abs/2609.29173)

**<font color=#1a73e8>作者：</font>** Yanming Xiu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Video see-through extended reality (VST XR) systems commonly use headset screenshots or captured frames as proxies for the user's first-person visual context. However, the system-captured view and the user's effective visible field do not necessarily coincide: a screenshot records a rectangular machine-readable frame, whereas the user's effective visible region can be more constrained and non-rectangular. This paper studies this human-system view mismatch in VST XR. We formalize the relationship between the system-captured region and the human-visible region by defining their co-visible, system-only, and human-only regions. \rev{We then conduct a pilot-level boundary measurement on Meta Quest 3, revealing a clear mismatch between the rectangular screenshot frame and the approximate human-visible boundary. Building on this model, we analyze how view mismatch can affect screenshot-based XR sensing and downstream vision-language model tasks. Through four representative case studies, we illustrate potential risks and failure modes including prompt injection, privacy leakage, human-invisible information bias, and missing human-visible information. Our results show that view mismatch is not only a geometric artifact, but can also introduce security, privacy, and reliability concerns for AI-integrated VST XR systems.

---


### 85. [A Human-Like Pedestrian Model for Automated Driving Simulations](https://arxiv.org/abs/2609.29175)

**<font color=#1a73e8>作者：</font>** Ruofeng Wang, Patrick Ebel, Philipp Wintersberger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Automated vehicles must be able to interact with pedestrians safely and efficiently across diverse traffic situations. Although driving simulators offer a scalable testbed for learning such capabilities, existing theory-inspired pedestrian models are narrow in scope and limited to go/no-go crossing decisions in single-lane settings. While data-driven approaches can predict pedestrian behavior in complex situations, they lack sufficient observations in rare, safety-critical scenarios. Here, we propose an approach to training pedestrian models in simulators so that learned policies generate demonstrably human-like behavior in realistic, complex traffic scenarios, including multiple lanes, heavy traffic, and dangerous driving styles. Our technical contribution is a novel definition of pedestrian-vehicle interaction as a partially observable Markov decision process (POMDP) with theory-grounded perceptual, cognitive, and motor constraints. It accounts for the highly adaptive nature of human behavior in traffic and simulates how people adjust their responses according to perceived danger, time pressure, and the complexity of the situation. When trained via deep reinforcement learning (RL) with domain randomization in a simulator, the model reproduces the broadest range of empirical findings shown so far on human crossing behavior, including gap acceptance, yielding acceptance, hesitation, and evasive speed adjustment. We show that learned policies transfer to unseen traffic environments, and can be further adapted to local traffic norms with finetuning. Together, these results establish a blueprint for simulator-ready pedestrian models that can support the development and evaluation of automated driving systems.

---


### 86. [Poster: FedWM-Guard: Thwarting Imagination Poisoning in Federated World Model-based Autonomous Driving](https://arxiv.org/abs/2609.29178)

**<font color=#1a73e8>作者：</font>** Sheng Liu, Panos Papadimitratos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) can improve world model (WM)-based autonomous driving (AD) without centralizing raw private vehicle data, but it also turns model aggregation into a safety-critical integrity boundary. We introduce a new threat in federated WM-AD, namely \emph{imagination poisoning}: compromised vehicles submit bounded WM updates that preserve benign short-horizon predictions yet corrupt long-horizon rollouts (e.g., trigger-conditioned) during training, thereby misleading a downstream planner. We present \emph{FedWM-Guard}, to the best of our knowledge, the first defense to characterize planner-facing rollouts in federated WM-AD, screen authenticated updates in hidden-canary scenarios, audit predicted futures against later observations, and invoke a WM-independent safety shield when persistent inconsistency is detected. Unlike parameter-space defenses, it scores what an update makes the model \emph{imagine}, not only how the update looks. We also outline how we plan to evaluate it under non-IID (not independent and identically distributed) data, adaptive attacks, and benign distribution shift. This work highlights an unexplored domain, federated WM-AD, and its threat surface and potential countermeasures.

---


### 87. [Right Choice of Classification Algorithms Based on Reinforcement Learning for Prediction of Non-Alcoholic Fatty Liver](https://arxiv.org/abs/2609.29181)

**<font color=#1a73e8>作者：</font>** Hasan Samadbin, Arman Daliri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There are many complex issues in the world of artificial intelligence. Some of these problems are solved using other artificial intelligence methods, which are called artificial intelligence for artificial intelligence. Finding an appropriate classifier algorithm is a time-consuming task. For this reason, an algorithm that can automatically learn the choice of classification algorithms is very important. Classification algorithms are useful in predicting various diseases. Also, Primary Biliary Cirrhosis is one of the most well-known diseases that have been predicted by classification algorithms. This research's most significant achievement and novelty is the automatic increase in learning through a scoring method of reinforcement learning is called square learning (SL). In this research, an algorithm is presented that learns to automatically select the appropriate classification algorithm to predict Primary Biliary Cirrhosis. In this article, with inspiration from four evaluation metrics in classification algorithms, a new reinforcement learning method by the name of Fourth Degree Learning has been presented. In this research, we increased the performance of the classification algorithms used in this method from 63% of accuracy and achieved 98% accuracy.

---


### 88. [Predicting Emerging Topics from Outliers: A Prospective Study of Weak Signals in Embedding Space](https://arxiv.org/abs/2609.29183)

**<font color=#1a73e8>作者：</font>** Evangelia Zve, Gauvain Bourgne, Jean-Gabriel Ganascia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Some documents that embedding-based topic models initially classify as noise later become founding members of emerging topics. At publication time, however, they appear as scattered points in embedding space and are difficult to distinguish from ordinary noise without the benefit of hindsight. We study whether such anticipatory outliers can be predicted prospectively, using only information available when a document first appears. We derive labels from the subsequent trajectories of outlier documents, distinguishing those that anticipate new topics from those that reinforce existing topics or remain isolated, and estimate label confidence through agreement across multiple embedding models. On two French news corpora, anticipatory outliers prove predictable at publication time. Under cross-validation, $F_1$ rises from about 0.77 over the full eligible population to above 0.90 on high-consensus subsets, and remains at 0.76-0.80 under a strictly chronological evaluation. Predictive performance is driven mainly by geometric features capturing each outlier's position in embedding space.

---


### 89. [An Automated Georeferencing Technique for Multi-Temporal Stope Point Clouds for Downstream Geotechnical Analysis](https://arxiv.org/abs/2609.29186)

**<font color=#1a73e8>作者：</font>** Dibyayan Patra, Simit Raval, Pasindu Ranasinghe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The increasing use of UAV laser scanning in underground mines has enabled frequent acquisition of 3D point clouds from challenging environments such as stopes, generating large volumes of multi-temporal spatial data throughout successive excavation stages. However, in GNSS-denied underground environments, independently acquired stope point clouds are generated within local scanner reference frames and require registration and georeferencing before integration with mine reference data for downstream geotechnical analysis, monitoring, and mine planning. This process is commonly performed manually by aligning individual stope scans with mine reference drives, making repeated georeferencing time-consuming and potentially limiting the utilisation of routinely acquired data. This study proposes the 3D Tag-based Automated Registration and Georeferencing Technique (3D-TARGeT), an automated framework using low-cost, generic, non-unique rectangular tags to establish spatial correspondence between stope point clouds and the mine reference coordinate system. The framework combines automated tag identification, geometric tag matching, and rigid transformation estimation. It was evaluated as a proof of concept using four multi-temporal point-cloud scans of an underground mine stope, with the proposed tags simulated under representative scanning conditions. 3D-TARGeT achieved consistent centimetre-level georeferencing accuracy, with median cloud-to-cloud distance and root mean square error below 0.03 m across all scans, while substantially outperforming widely used automatic point-cloud registration techniques. Overall, 3D-TARGeT provides an accurate and robust approach for automating stope point-cloud georeferencing, reducing reliance on manual alignment and facilitating multi-temporal datasets for downstream geological and geotechnical applications.

---


### 90. [The Entropy Triangle Method (ETM): A novel framework for the prevention of cardiac arrhythmia with a review of more than 10,000 patients](https://arxiv.org/abs/2609.29187)

**<font color=#1a73e8>作者：</font>** Arman daliri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> One of the most important problems in medicine is to facilitate prediction. In this study, we propose entropy triangle method, a novel framework for predicting heart rhythms using a novel machine learning technique. This framework includes three steps: feature engineering, entropy triangle oversampling, and disease prediction. The dataset used in this study is a 12-lead electrocardiogram (ECG) arrhythmia research database with 10,646 patients. This dataset contains 11 different heart rhythms (5 sinus rhythms and 6 non-sinus rhythms). In this article, we introduce two firsts in machine learning and medicine that can predict non-sinus rhythm with over 85% accuracy. Our experimental results show, among others, that the most accurate classifier based on entropy triangles and the most useful oversampling are the supported vector classifiers and oversampling techniques for shark scent.

---


### 91. [When Honesty is Not Enough in AI Debate](https://arxiv.org/abs/2609.29189)

**<font color=#1a73e8>作者：</font>** Rayne Holland, Liming Zhu, Jason Xue  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scalable oversight aims to verify the behaviour of agents whose capabilities exceed those of their overseers. AI debate has been proposed as an oversight solution in which competing agents help a resource-limited verifier assess claims that it cannot reliably evaluate unaided. Much of its promise rests on incentivizing honest arguments that lead to correct verdicts. Yet a correct verdict need not uniquely determine the arguments used to support it. Agents may retain discretion over which correct claims to present, how to frame them, and in what order to disclose them. This residual freedom can allow agents to shape what the verifier learns beyond the task-relevant conclusion, pursuing latent objectives without compromising verdict correctness. To study this phenomenon, we introduce the framework strategic interactive oversight (SIO), which treats oversight jointly as a verification mechanism and a strategic communication channel. Within this framework, we formalise the notion of task-admissible latent optimisation, which entails the pursuit of latent objectives while maintaining a prescribed task performance. As proof-of-concept, we instantiate SIO in the establish protocol debate with cross-examination and quantify a tradeoff between task success and information disclosure about a hidden variable. The trade-off identifies a strategic window in which substantial disclosure remains compatible with task admissibility. Towards mitigation, we reduce admissible bias by expanding the cross-examiner's role to mitigate persistent disclosure over finite interaction horizons. Our results highlight the need to evaluate oversight not only by the correctness of its verdicts, but also by the information conveyed through its transcripts.

---


### 92. [ASIRF: An Agentic Framework for Context-Dependent Sensitive Information Redaction](https://arxiv.org/abs/2609.29191)

**<font color=#1a73e8>作者：</font>** Sudha Priyadarshini, Mohamed Chahine Ghanem  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sensitive information is defined by domain and intent, not a universal category, yet redaction systems such as privacy filters and named-entity recognizers fix a taxonomy at training time, requiring retraining for each new domain. We introduce ASIRF (Agentic Sensitive Information Redaction Framework), which retrieves domain-specific definitions based on the input's domain from a flexible knowledge base at inference time, needing no retraining to adapt. Two architectures, a three-call multi-agent pipeline and a single-agent variant, are evaluated across ten small open-weight models and eight datasets, including out-of-distribution fictional domains, against the OpenAI Privacy Filter (OPF) as a trained-classifier baseline. With only a few dozen expert-authored definitions per domain and no training data, ASIRF's recall exceeds OPF's in 68 of 80 model-domain combinations (85 percent), by at least one of the two architectures, with shortfalls confined mostly to OPF's training-distribution domains.

---


### 93. [ImCorr: Sub-pixel Semantic Correspondence via Implicit Feature Decoding](https://arxiv.org/abs/2609.29193)

**<font color=#1a73e8>作者：</font>** Yusung Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The strong performance that modern semantic correspondence methods achieve at standard thresholds plateaus sharply at fine-grained thresholds. We argue that this plateau stems not from the representational capacity of backbone features, but from a grid-tied readout. Patch-based vision transformers tokenize images onto discrete grids, introducing two forms of quantization error: querying nearest patch features instead of exact keypoints on the source side, and the absence of grid features representing precise ground-truth locations on the target side. We quantify this quantization ceiling across all 499,188 keypoints in SPair-71k: under the standard 448x448, patch-14 setting, 84.9% of ground-truth keypoints have no grid feature representing their precise location at PCK@0.01. This is a structural limitation at the representation level, independent of the matching strategy. We address this with ImCorr: Sub-pixel Semantic Correspondence via Implicit Feature Decoding, which formulates correspondence estimation over a continuous feature field queryable at arbitrary continuous coordinates. A FiLM-conditioned decoder is trained to embed sub-pixel positional information into the feature field. Querying the field directly at exact keypoint coordinates theoretically eliminates representation-level quantization error on the source side, while decoding onto a grid denser than the backbone grid substantially reduces quantization error on the target side. On SPair-71k and AP-10K (intra-species, cross-species, and cross-family), ImCorr improves performance at fine-grained thresholds (PCK@0.01-0.05), achieving a 6.2 percentage point gain over the prior state of the art at PCK@0.01 on SPair-71k. These results demonstrate that representational continuity is an effective solution for precise semantic correspondence. Code is available at this https URL.

---


### 94. [FB-GDM: Fully-Bayesian Guided Diffusion Models for High-Dimensional Linear Inverse Problems via Unsupervised Variational Inference](https://arxiv.org/abs/2609.29216)

**<font color=#1a73e8>作者：</font>** Gatien Séguy, Thomas Rodet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are powerful priors for linear inverse problems, but the reference guidance methods, Diffusion Posterior Sampling (DPS) and Pseudoinverse-Guided Diffusion Models ($\Pi$GDM), rely on scalar hyperparameters tuned per task, usually against the ground truth. We introduce FB-GDM, a fully-Bayesian guided diffusion method that removes this calibration step. Starting from the Gaussian approximation of $\Pi$GDM, we derive a closed-form conditional score that depends on two precision parameters (inverse variances), one associated with the denoising approximation and one with the observation likelihood, and treat them as latent variables inferred by variational inference at each reverse step. A separable factorization makes each update scale linearly with the number of pixels, so the inference stays tractable at full image resolution, at a cost comparable to one $\Pi$GDM run. FB-GDM requires neither the noise level nor the ground truth: its only inputs are the observation and the forward operator. Experiments on CelebA-HQ inverse problems establish two results. (i) The precision parameters, inferred from the observation alone, allow FB-GDM to outperform $\Pi$GDM at its nominal setting, even when the latter is given the true noise level, by up to 14 dB depending on the operator, and to match the ground-truth-calibrated $\Pi$GDM oracle within 0.1 dB. (ii) FB-GDM is robust when the forward operator, the noise level, or the image distribution changes: it stays close to a per-problem $\Pi$GDM oracle throughout and does not exhibit the hallucinations observed with DPS, whereas DPS substantially degrades at a fixed scale and $\Pi$GDM stays competitive only if it is re-tuned against the ground truth for each new problem. When the prior is applied to images outside its training set, this re-balancing between data and prior keeps FB-GDM faithful where a fixed face-prior guidance can otherwise hallucinate.

---


### 95. [Security Limits of Mining Before Validation in Nakamoto Consensus](https://arxiv.org/abs/2609.29222)

**<font color=#1a73e8>作者：</font>** Yifan Zhou, Jiang Xiao, Kaihua Qin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mining before validation allows miners to extend a newly received block before completing its validity checks, giving them a head start in the race for the next block reward. This head start, however, comes with a security risk: rejecting one invalid block also discards the honest work built on it, an effect missed when validation is treated as instantaneous. We quantify this risk in a model of Nakamoto consensus with bounded network delay and a validation-time bound independent of processing load. We establish an explicit threshold on adversarial mining power below which honest miners' fully validated chains continue to grow and agree on a stable history with high probability over any fixed observation period. We also construct an attack that repeatedly draws honest mining onto invalid branches. When the adversary produces more than one block on average during the allowed validation time, the attack can eventually remove a target block at any fixed initial confirmation depth. Combined with ordinary private mining, this attack yields a matching asymptotic bound in the fully decentralized regime, where each honest miner has negligible mining power. The results show how validation latency limits the security of mining before validation, beyond the constraint imposed by network delay.

---


### 96. [FounRef: Robust, Structure-Preserving, and Fast Metric Refinement of Frozen Monocular Foundation Priors with Sparse Anchors](https://arxiv.org/abs/2609.29224)

**<font color=#1a73e8>作者：</font>** Dan Halperin, Mirko Mählisch  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense metric depth from cameras is essential to real-world 3D applications, yet achieving accuracy, faithful surface geometry, and fast inference simultaneously remains challenging. Monocular foundation models provide rich, transferable geometric priors but lack reliable metric scale, while depth-completion networks recover metric depth at the cost of geometric fidelity, cross-domain robustness, or speed. We present FounRef, a training-free method that aligns a frozen monocular foundation prior with sparse metric anchors to produce dense metric depth. FounRef is modular by design: its depth prior, anchor source, and refinement solver can each be replaced independently. We instantiate FounRef with MoGe-2 and LiDAR anchors. FounRef validates each anchor against the prior's dense depth prediction, rejecting inconsistencies caused by cross-sensor misalignment that geometry-only filters cannot detect. It then applies global and local metric corrections through a structure-preserving solver, retaining the prior's fine-grained geometry. FounRef requires no task-specific training and operates out of the box across unfamiliar cameras and scenes. On out-of-domain data, it delivers up to 24% lower depth error, 92% lower surface-normal noise, and almost 15x faster inference than DMD3C, a state-of-the-art depth-completion network. By decoupling metric alignment from geometry prediction, FounRef provides an accurate, geometrically faithful, and efficient approach to dense metric depth that can directly benefit from future advances in foundation models and metric sensors.

---


### 97. [ComplexSync: High-Fidelity and Real-Time Lip Sync in Complex Scenarios](https://arxiv.org/abs/2609.29225)

**<font color=#1a73e8>作者：</font>** Jiaran Cai, Xingpei Ma, Shenneng Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lip synchronization aims to generate visual lip dynamics that align precisely with speech audio. Despite the high generation quality of diffusion models, they often struggle in complex scenarios and suffer from prohibitive inference latency, limiting real-world deployment. We present ComplexSync, a unified diffusion-based framework that enables real-time, high-fidelity lip sync under complex conditions. First, we introduce a dual-stream joint training strategy to mitigate information leakage from reference frames while preserving natural dynamics. Second, we develop a distillation-based acceleration scheme for single-step denoising, achieving a throughput of over 70 FPS. Third, we propose a relational alignment loss that leverages structural priors from Vision Foundation Models (VFMs) to enhance robustness against complex scene factors. Furthermore, we present the first benchmark specifically designed for complex lip synchronization, comprising over 200 challenging video sequences and specialized metrics. Extensive experiments demonstrate that ComplexSync achieves state-of-the-art performance across both standard and complex scenarios while enabling real-time inference.

---


### 98. [SARFusion: Scene-Aware Routing Fusion for Robust Camera-LiDAR 3D Object Detection](https://arxiv.org/abs/2609.29235)

**<font color=#1a73e8>作者：</font>** Yuting Zhao, Ziyi Zheng, Shuxiao Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-LiDAR fusion has become a prevailing paradigm for 3D object detection in autonomous driving. However, existing fusion detectors often establish strong inter-modality dependencies by decoding object queries from tightly coupled multimodal representations. Under corrupted driving conditions, such dependencies make the detector vulnerable to unreliable modalities, where degraded observations may interfere with reliable modality-specific evidence and lead to suboptimal predictions. Moreover, modality reliability can vary across both global driving scenes and individual object queries, requiring adaptive fusion decisions at a finer granularity. To bridge this gap, we reformulate robust camera-LiDAR fusion as a scene-aware branch routing problem and propose SARFusion, a robust 3D object detector. Instead of producing detections from a single fused representation, SARFusion decouples object-query decoding into three parallel reasoning branches: a camera branch, a LiDAR branch, and a camera-LiDAR fusion branch. Guided by a Scene Reliability Prior estimated from the global driving context, SARFusion further incorporates object-level evidence to route each query to the most suitable branch. This query-wise routing strategy alleviates harmful cross-modal interference while preserving the benefits of multimodal fusion when complementary cues are trustworthy. On the nuScenes test set, SARFusion achieves strong performance with 72.5 mAP and 74.4 NDS. Extensive analyses demonstrate its robustness under challenging conditions, including sensor corruptions and environmental changes.

---


### 99. [TOLA: Text-aware One-Step Latent Adaptation for Diffusion-based Text Image Super-Resolution](https://arxiv.org/abs/2609.29240)

**<font color=#1a73e8>作者：</font>** Yike Xu, Yue Shi, Yong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text image super-resolution (TSR) aims to recover visually faithful and readable text under unknown degradations. Existing diffusion-based methods typically rely on multi-step prediction of either the high-resolution image or its text prior, resulting in prohibitive computational cost and inference latency. More critically, an erroneous text prior may be repeatedly injected into the denoising process, causing image and text predictions to reinforce each other and progressively amplify an early recognition error into a sharp yet semantically incorrect character. To address these limitations, we propose TOLA, a Text-aware One-step Latent Adaptation framework without iterative image-text diffusion. TOLA consists of two key modules. First, a confidence-weighted text conditioning module constructs the semantic condition only once and suppresses unreliable OCR predictions before they contaminate image reconstruction. Second, a lightweight latent residual correction module explicitly estimates and corrects the structured residual errors to recover missing or distorted stroke details. Extensive experiments demonstrate our state-of-the-art performance across all evaluation metrics on both CTR-TSR-Test ($\times 4$) and RealCE-200 benchmarks. It is worth noting that our TOLA consistently surpasses existing diffusion-based TSR methods by at least 2.72 dB in PSNR on CTR-TSR-Test.

---


### 100. [No More Free Lunch: Corpus Task Complexity Matters as Corpora Grow](https://arxiv.org/abs/2609.29245)

**<font color=#1a73e8>作者：</font>** Prasann Singhal, Amanda Bertsch, Jacob Steinhardt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Given a large corpus, the questions one might ask can vary -- from "When was the first human heart transplant?" to "What are all the contradictory claims in this literature?" -- but what makes some questions more challenging than others? In this work, we define a notion of Corpus Task Complexity (CTC) that characterizes tasks by how their difficulty grows with corpus size; for instance, a retrieval query only requires a single linear pass over a corpus, while finding contradictions requires checking a quadratically growing set of claim pairs. Observing that prior work has largely only studied tasks whose difficulty grows linearly with corpus size, which we call low CTC tasks, we introduce 10 new tasks belonging to a class of high CTC whose difficulty grows quadratically or more in corpus size. We find that high-CTC tasks not only grow much more challenging on average at longer contexts for LCLMs, they reverse many modeling conclusions drawn solely from low-CTC evaluations. For instance, efficient block-sparse and hybrid attention approaches consistently match full attention performance on low-CTC tasks, but degrade much more on high-CTC tasks. Large-corpus high-CTC reasoning thus remains an open challenge as full attention is too costly to scale, motivating future research on these tasks. We release our code, data, and 22-task suite (CTC-Bench), to facilitate future research in this area.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
