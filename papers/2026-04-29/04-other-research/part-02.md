# 📦 其他研究 | 2026年04月29日

> 本类共 **437** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-437](./part-09.md)

---

### 51. [VS-DDPM: Efficient Low-Cost Diffusion Model for Medical Modality Translation](https://arxiv.org/abs/2604.22942)

**<font color=#1a73e8>作者：</font>** Nikoo Moradi, Gijs Luijten, Behrus Hinrichs-Puladi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models produce high-quality synthetic data but suffer from slow inference. We propose 3D Variable-Step Denoising Diffusion Probabilistic Model (VS-DDPM) a framework engineered to maintain generative quality while accelerating inference by several factors. We tested our approach on four tasks (missing MRI, tumor removal, MRI-to-sCT, and CBCT-to-sCT) within the BraTS2025 and SynthRAD2025 challenges. Designed for high efficiency under hardware and time constrains imposed by both challenges. VS-DDPM achieved state-of-the-art (SOTA) performance in missing MRI synthesis, yielding Dice scores of 0.80, 0.83, and 0.88 for the enhancing tumor, tumor core, and whole tumor regions, respectively, alongside a structural similarity index (SSIM) of 0.95. For MRI tumor removal, the model attained a root mean squared error (RMSE) of 0.053, a peak signal-to-noise ratio (PSNR) of 26.77, and an SSIM of 0.918. While the framework demonstrated competitive performance in MRI-to-sCT and CBCT-to-sCT tasks, it did not reach SOTA benchmarks, potentially due to sensitivities in data pre and post-processing pipelines or specific loss function configurations. These results demonstrate that VS-DDPM provides a robust and tunable solution for high-fidelity 3D medical image synthesis. The code is available in this https URL.

---


### 52. [Score-Repellent Monte Carlo: Toward Efficient Non-Markovian Sampler with Constant Memory in General State Spaces](https://arxiv.org/abs/2604.22948)

**<font color=#1a73e8>作者：</font>** Jie Hu, Lingyun Chen, Geeho Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> History-dependent sampling can reduce long-run Monte Carlo variance by discouraging redundant revisits, but existing schemes typically encode history through empirical measure on finite state spaces, which is infeasible in high-dimensional discrete configuration spaces or ill-posed in continuous domains. We propose Score-Repellent Monte Carlo (SRMC) framework that summarizes trajectory history by a running average of score evaluations in $R^d$, where $d$ is the dimension of the score and state representation. This history is converted into a surrogate target through an exponential score tilt, indexed with $\alpha$ that represents the strength of repellence in controlling the magnitude of the history-based repulsion. The surrogate family is normalization-free in the standard MCMC sense, yielding a generic wrapper: at each iteration, any base kernel targeting $\pi$ can instead be run on the current surrogate $\pi_{\theta_n}$ while the history is updated online. We analyze the coupled evolution of the history recursion and Monte Carlo estimators using stochastic approximation with controlled Markovian noise, establishing almost sure convergence and a joint central limit theorem. We further identify regimes in which the asymptotic covariance decreases as $\alpha$ increases, with scaling $O(1/\alpha)$, extending the near-zero-variance effect of finite-state history-dependent samplers to general state spaces with constant memory. Experiments on continuous targets and discrete energy-based models demonstrate improved estimator variance and mode coverage, while retaining $O(d)$ memory usage and modest per-iteration overhead.

---


### 53. [The Power of Power Law: Asymmetry Enables Compositional Reasoning](https://arxiv.org/abs/2604.22951)

**<font color=#1a73e8>作者：</font>** Zixuan Wang, Xingyu Dang, Jason D. Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural language data follows a power-law distribution, with most knowledge and skills appearing at very low frequency. While a common intuition suggests that reweighting or curating data towards a uniform distribution may help models better learn these long-tail skills, we find a counterintuitive result: across a wide range of compositional reasoning tasks, such as state tracking and multi-step arithmetic, training under power-law distributions consistently outperforms training under uniform distributions. To understand this advantage, we introduce a minimalist skill-composition task and show that learning under a power-law distribution provably requires significantly less training data. Our theoretical analysis reveals that power law sampling induces a beneficial asymmetry that improves the pathological loss landscape, which enables models to first acquire high-frequency skill compositions with low data complexity, which in turn serves as a stepping stone to efficiently learn rare long-tailed skills. Our results offer an alternative perspective on what constitutes an effective data distribution for training models.

---


### 54. [On the Existence of an Inverse Solution for Preference-Based Reductions in Argumentation](https://arxiv.org/abs/2604.22958)

**<font color=#1a73e8>作者：</font>** Alessio Zaninotto, Bruno Yun, Nir Oren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Preference-based argumentation frameworks (PAFs) extend Dung's approach to abstract argumentation (AAFs) by encoding preferences over arguments. Such preferences control the transformation of attacks into defeats, and different approaches to doing so result in different reductions from a PAF to an AAF. In this paper we consider a PAF inverse problem which takes an argumentation graph, a labelling and a semantics as an input, and outputs a ``yes" or ``no" as to whether there is a preference relation between the arguments which can yield the desired labelling. This inverse problem has applications in areas including preference elicitation and explainability. We consider this problem in the context of the four most widely-used preference based reductions under the complete semantics. We show that in most cases, the problem can be answered in polynomial time.

---


### 55. [Understanding teens' self-beliefs when learning to construct and deconstruct AI/ML systems: Developing a survey instrument](https://arxiv.org/abs/2604.22959)

**<font color=#1a73e8>作者：</font>** Luis Morales-Navarro, Deborah Fields, Michael T. Giang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite growing calls to foster AI literacy, there are few available survey instruments designed for children and youth that study computational empowerment alongside construction and deconstruction activities. In such activities, learners' beliefs about their abilities and attributes can impact their engagement. In this paper, we introduce and validate a survey instrument with constructs related to construction (creative expression and problem-solving self-beliefs) and deconstruction (auditing self-efficacy and fascination with auditing), along with more general self-beliefs related to design justice and the value of learning about AI/ML. We administered the instrument to 124 teenagers and assessed the six-factor structure of the instrument using confirmatory factor analysis. In addition to confirming the structure, we found that design justice beliefs strongly correlated with problem-solving, auditing self-efficacy, and creative expression.

---


### 56. [AnemiaVision: Non-Invasive Anemia Detection via Smartphone Imagery Using EfficientNet-B3 with TrivialAugmentWide, Mixup Augmentation, and Persistent Patient History Management](https://arxiv.org/abs/2604.22964)

**<font color=#1a73e8>作者：</font>** Rahul Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anemia affects over one billion people globally and remains severely under-diagnosed in low-resource regions where laboratory blood tests are inaccessible. This paper presents AnemiaVision, an end-to-end web-based system for non-invasive anemia screening from smartphone photographs of the palpebral conjunctiva and fingernail beds. The proposed pipeline fine-tunes a pre-trained EfficientNet-B3 backbone with a redesigned three-layer classifier head incorporating BatchNorm, GELU activations, and high-rate Dropout (0.45/0.35). Training employs four orthogonal accuracy-boosting techniques: TrivialAugmentWide for policy-free image augmentation, RandomErasing for spatial regularisation, Mixup (alpha=0.2) for inter-class smoothing, and cosine-annealing scheduling with linear warmup. Early stopping is governed by peak validation accuracy rather than validation loss to prevent premature termination on high-variance epochs. The deployed Flask application integrates persistent patient-history management backed by PostgreSQL on Render, with an automated database-migration entrypoint ensuring zero data loss across redeploys. Ablation experiments demonstrate that accuracy-first early stopping contributes +1.6% and Mixup contributes +2.8% to final validation accuracy. Overall, the proposed system achieves a validation accuracy of 96.2% and AUC-ROC of 0.98, compared with 44.9% validation accuracy and AUC-ROC of 0.58 from the three-epoch CPU-only baseline. Sensitivity for the anemic class reaches 0.96, making the system suitable as a first-line screening tool for community health workers in rural settings. The system is publicly accessible and source code is openly available.

---


### 57. [Towards Causally Interpretable Wi-Fi CSI-Based Human Activity Recognition with Discrete Latent Compression and LTL Rule Extraction](https://arxiv.org/abs/2604.22979)

**<font color=#1a73e8>作者：</font>** Luca Cotti, Luca Lavazza, Marco Cominelli 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We address Human Activity Recognition (HAR) utilizing Wi-Fi Channel State Information (CSI) under the joint requirements of causal interpretability, symbolic controllability, and direct operation on high-dimensional raw signals. Deep neural models achieve strong predictive performance on CSI-based HAR (CHAR), yet rely on continuous latent representations that are opaque and difficult to modify; purely symbolic approaches, in contrast, cannot process raw CSI streams. We propose a fully automatic and strictly decoupled pipeline in which CSI magnitude windows are compressed by a categorical variational autoencoder with Gumbel-Softmax latent variables under a capacity-controlled objective, yielding a compact discrete representation. The encoder is then frozen and used as a deterministic mapping to one-hot latent trajectories. Causal discovery is performed on these trajectories to estimate class-conditional temporal dependency graphs. Statistically supported lagged dependencies are translated into Linear Temporal Logic (LTL) rules, producing a fully symbolic and deterministic classifier based solely on rule evaluation and aggregation, without any learned discriminative head. Because rules are defined over discrete latent variables, antenna-specific rule sets can in principle be combined at the symbolic level, enabling structured multi-antenna fusion without retraining the encoder. Results from CHAR Latent Temporal Rule Extraction (CHARL-TRE) indicate competitive performance while preserving explicit temporal and causal structure, showing that deterministic symbolic classification grounded in unsupervised discrete latent representations constitutes a viable alternative to end-to-end black-box models for wireless HAR.

---


### 58. [Reward Models Are Secretly Value Functions: Temporally Coherent Reward Modeling](https://arxiv.org/abs/2604.22981)

**<font color=#1a73e8>作者：</font>** Alex Nikulkov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward models in RLHF are trained to score only the final token of a response - a choice that discards rich signal from every intermediate position and produces models whose token-level outputs are noise. We argue this is a missed opportunity: a well-trained reward model's output at any token should represent the conditional expectation of the final reward given the response so far. We introduce Temporally Coherent Reward Modeling (TCRM), which induces this property via two regularization terms on top of the standard Bradley-Terry loss, with minimizers provably equal to conditional expectations. The regularizers correspond to Monte Carlo and TD value-learning objectives, establishing a direct connection to RL value functions. TCRM requires zero changes to architecture, data, or inference, yet unlocks three capabilities from one principle: interpretable token-level reward trajectories (middle-token pairwise accuracy improved from 50% to 88.9%, final-token accuracy preserved); state-of-the-art PRM performance on ProcessBench (44.9% average F1) among models trained only on outcome data; and unified reward/value modeling in PPO, reducing peak GPU memory by 27% and step time by 19% with matching LLM quality.

---


### 59. [BrickNet: Graph-Backed Generative Brick Assembly](https://arxiv.org/abs/2604.22984)

**<font color=#1a73e8>作者：</font>** Peter Kulits, Cordelia Schmid  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We train a language model to generate LEGO-brick build sequences. While prior work has been restricted to discrete, voxel-like towers, we consider a much broader set of pieces, encompassing thousands of part types with diverse connection semantics. To enable this, we first collect a large-scale dataset of over 100,000 human-designed LDraw brick objects and scenes. The complexity of our setting makes it challenging to autoregressively assemble structures that satisfy physical constraints. When predicting block pose directly, build sequences quickly become invalid after a small number of steps. Although pieces are placed in 3D space, it is the spatial relationships of the parts which define the whole. With this in mind, we design a graph-based program representation that parametrizes structure through connectivity, improving the physical grounding of generated sequences. To enable future applications, we make our dataset and models available for research purposes. this https URL

---


### 60. [Hard to See, Hard to Label: Generative and Symbolic Acquisition for Subtle Visual Phenomena](https://arxiv.org/abs/2604.22990)

**<font color=#1a73e8>作者：</font>** Renjith Prasad, Rishabh Sharma, Andrew E. Shao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subtle visual anomalies such as hairline cracks, sub-millimeter voids, and low-contrast inclusions are structurally atypical yet visually ambiguous, making them both difficult to annotate and easy to overlook during active learning. Standard acquisition heuristics based on discriminative uncertainty or feature diversity often overselect dominant patterns while underexploring sparse yet important regions of the data space. This failure mode is especially severe in industrial defect inspection, where anomalies may be both low-prevalence and difficult to distinguish from surrounding structure. To resolve this, we propose GSAL, an active learning framework for object detection that combines a diffusion-based difficulty signal with a hierarchical semantic coverage prior. The diffusion component scores images and proposals using reconstruction discrepancy and denoising variability, prioritizing visually atypical or ambiguous examples. However, diffusion alone does not prevent acquisition from repeatedly favoring hard samples within dominant semantic modes. The semantic component therefore organizes candidate samples in a three-level concept graph and promotes coverage of underrepresented semantic regions while providing interpretable acquisition rationales. By balancing visual difficulty with semantic coverage, GSAL improves retrieval of subtle and rare targets that are often missed by uncertainty-only selection. Experiments on a proprietary thin-film defect, Pascal VOC and MS COCO dataset show consistent gains in label efficiency and rare-class retrieval over uncertainty-, diversity-, and hybrid-based baselines

---


### 61. [Efficient Image Annotation via Semi-Supervised Object Segmentation with Label Propagation](https://arxiv.org/abs/2604.22992)

**<font color=#1a73e8>作者：</font>** Vitalii Tutevych, Raphael Memmesheimer, Luca Eichler 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable object perception is necessary for general-purpose service robots. Open-vocabulary detectors struggle to generalize beyond a few classes and fully supervised training of object detectors requires time-intensive annotations. We present a semi-supervised label propagation approach for household object segmentation. A segment proposer generates class-agnostic masks, and an ensemble of Hopfield networks assigns labels by learning representative embeddings in complementary foundation model embedding spaces (CLIP, ViT, Theia). Our approach scales to 50 object classes with limited annotation overhead and can automatically label 60% of the data in a RoboCup@Home setting, where preparation time is severely constrained. Dataset and code are publicly available at this https URL.

---


### 62. [Collocation-based Robust Physics Informed Neural Networks for time-dependent simulations of pollution propagation under thermal inversion conditions on Spitsbergen](https://arxiv.org/abs/2604.23003)

**<font color=#1a73e8>作者：</font>** Leszek Siwik, Maciej Sikora, Natalia Leszczyńska 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a Physics-Informed Neural Network framework for time-dependent simulations of pollution propagation originating from moving emission sources. We formulate a robust variational framework for the time-dependent advection-diffusion problem and establish the boundedness and inf-sup stability of the corresponding discrete weak formulation. Based on this mathematical foundation, we construct a robust loss function that is directly related to the true approximation error, defined as the difference between the neural network approximation and the (unknown) exact solution. Additionally, a collocation-based strategy is introduced to speed up neural network training. As a case study, we investigate pollution propagation caused by snowmobile traffic in Longyearbyen, Spitsbergen, supported by detailed in-field measurements collected using dedicated sensors. The proposed framework is applied to analyze the effects of thermal inversion on pollutant accumulation. Our results demonstrate that thermal inversion traps dense and humid air masses near the ground, significantly enhancing particulate matter (PM) concentration and worsening local air quality.

---


### 63. [GenAssets: Generating in-the-wild 3D Assets in Latent Space](https://arxiv.org/abs/2604.23010)

**<font color=#1a73e8>作者：</font>** Ze Yang, Jingkang Wang, Haowei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality 3D assets for traffic participants are critical for multi-sensor simulation, which is essential for the safe end-to-end development of autonomy. Building assets from in-the-wild data is key for diversity and realism, but existing neural-rendering based reconstruction methods are slow and generate assets that render well only from viewpoints close to the original observations, limiting their usefulness in simulation. Recent diffusion-based generative models build complete and diverse assets, but perform poorly on in-the-wild driving scenes, where observed actors are captured under sparse and limited fields of view, and are partially occluded. In this work, we propose a 3D latent diffusion model that learns on in-the-wild LiDAR and camera data captured by a sensor platform and generates high-quality 3D assets with complete geometry and appearance. Key to our method is a "reconstruct-then-generate" approach that first leverages occlusion-aware neural rendering trained over multiple scenes to build a high-quality latent space for objects, and then trains a diffusion model that operates on the latent space. We show our method outperforms existing reconstruction and generation based methods, unlocking diverse and scalable content creation for simulation.

---


### 64. [On-Device Vision Training, Deployment, and Inference on a Thumb-Sized Microcontroller](https://arxiv.org/abs/2604.23012)

**<font color=#1a73e8>作者：</font>** Jeremy Ellis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a complete, end-to-end on-device vision machine learning pipeline, comprising data acquisition, two-layer CNN training with Adam optimization, and real-time inference, executing entirely on a microcontroller-class device costing $15-40 USD. Unlike cloud-based workflows that require external infrastructure and conceal the computational pipeline from the practitioner, this system implements every step of the core ML lifecycle in approximately 1,750 lines of readable C++ that compiles in under one minute using the Arduino IDE, with no external ML dependencies. Running on the Seeed Studio ESP32-S3 XIAO ML Kit (8 MB PSRAM), the firmware achieves three-class 64x64 image classification in approximately 9 minutes per training run, with real-time inference at 6.3 FPS. Key contributions include: correct batch-level gradient accumulation; pre-computed resize lookup tables for inference; dual-format weight export for SD-free baked-in deployment; a three-tier weight priority system (SD binary > baked-in header > He-initialization) resolved automatically at boot; a single-constant network reconfiguration interface; and PSRAM-aware memory management suited to microcontroller constraints. All source code and reference datasets are released under the MIT License at this https URL

---


### 65. [DeepSignature: Digitally Signed, Content-Encoding Watermarks for Robust and Transparent Image Authentication](https://arxiv.org/abs/2604.23016)

**<font color=#1a73e8>作者：</font>** Mathias Graf, Marco Willi, Melanie Mathys 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-powered generative models have significantly expanded the possibilities for editing, manipulating, and creating high-quality images. Particularly, images that falsely appear to originate from trusted sources pose a serious threat, undermining public trust in image authenticity. We propose DeepSignature, a novel approach that integrates the guarantees of digital signatures with the capabilities of deep neural networks. Neural networks are used both to generate content-encoding watermarks and to embed them imperceptibly into images while ensuring robust extraction. These watermarks are cryptographically verifiable, enabling source attribution and image integrity validation. DeepSignature is compatible with existing image formats and requires no special handling of signed images. It supports client-side verification, requiring only the signer's public key. Additionally, we introduce a novel latent-space verification approach to detect and localize tampering attempts. We evaluate DeepSignature in terms of imperceptibility, robustness to benign transformations, forgery detection, and its resilience against various attack scenarios. Our results highlight the inherent trade-offs between imperceptibility, robustness, and integrity verification. We demonstrate that DeepSignature reliably identifies significant forgery attempts -- achieving near 100\% in our experiments. Finally, we emphasize DeepSignature's modularity and tunable parameters, allowing adaptation to application-specific requirements. Code and model weights will be published.

---


### 66. [Complex SGD and Directional Bias in Reproducing Kernel Hilbert Spaces](https://arxiv.org/abs/2604.23017)

**<font color=#1a73e8>作者：</font>** Natanael Alpay, Emeric Battaglia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic Gradient Descent (SGD) is a known stochastic iterative method popular for large-scale convex optimization problems due to its simple implementation and scalability. Some objectives, such as those found in complex-valued neural networks, benefit from updates like in SGD and Gradient Descent (GD) with a newly defined ``gradient'' that allows for complex parameters. This complex variant of the SGD/GD methods has already been proposed, but convergence guarantees without analyticity constraints have not yet been provided. We propose a variant of SGD (complex SGD) that allows for complex parameters, and we provide convergence guarantees under assumptions that parallel those from the real setting. Notably, these results extend to GD as well, and with the same set of assumptions, we confirm that some directional bias results extend from the real to the complex setting for kernel regression problems. We provide empirical results demonstrating the efficacy of the complex SGD in kernel regression problems utilizing complex reproducing kernel Hilbert spaces. In particular, we demonstrate we may recover superoscillation functions and Blaschke products from the Fock Space and Hardy Space, respectively, as the optimal functions for a particular choice of a loss function.

---


### 67. [AmaraSpatial-10K: A Spatially and Semantically Aligned 3D Dataset for Spatial Computing and Embodied AI](https://arxiv.org/abs/2604.23018)

**<font color=#1a73e8>作者：</font>** Mohammad Sadegh Salehi, Alex Perkins, Igor Maurell 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Web-scale 3D asset collections are abundant, but rarely deployment-ready. Assets ship with arbitrary metric scale, incorrect pivots and forward axes, brittle geometry, and textures that do not support relighting, which limits their utility for embodied AI, robotics simulation, game development, and AR/VR. We present AmaraSpatial-10K, a dataset of over 10,000 synthetic 3D assets designed for downstream use rather than volume alone. Each asset is released as a metric-scaled, semantically anchored .glb with separated PBR material maps, a convex collision hull, a paired reference image, and rich multi-sentence text metadata. The dataset spans indoor objects, vehicles, architecture, creatures, and props under a unified spatial convention. Alongside the dataset, we introduce an evaluation suite for 3D asset banks. The suite comprises a continuous Scale Plausibility Score (SPS) with an LLM-as-Judge interval protocol, an LLM Concept Density score for metadata, an anchor-error metric, and a cross-modal CLIP coherence protocol, and we use it to audit AmaraSpatial-10K alongside matched subsets from Objaverse, HSSD, ABO, and GSO. Compared with Objaverse-sourced assets, we demonstrate that AmaraSpatial-10K substantially improves text-based retrieval precision (CLIP Recall@5 of 0.612 vs 0.181, a 3.4x improvement with median rank falling from 267 to 3), and we establish that it satisfies the spatial and semantic prerequisites for physics-aware scene composition and embodied-AI asset banks, leaving those downstream evaluations to future work. AmaraSpatial-10K is publicly available on Hugging Face.

---


### 68. [Self-Supervised Learning for Android Malware Detection on a Time-Stamped Dataset](https://arxiv.org/abs/2604.23025)

**<font color=#1a73e8>作者：</font>** Annan Fu, Hao Pei, Maryam Tanha  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Android malware detectors built with machine learning often suffer from temporal bias: models are trained and evaluated without respecting apps' actual release times, inflating accuracy and weakening real-world robustness. We address this by constructing a time-stamped dataset of benign and malicious Android apps and introducing a timestamp-verification procedure to ensure temporal accuracy. We then propose a detection framework that uses Bootstrap Your Own Latent (BYOL) for self-supervised pre-training to learn obfuscation-resilient representations, followed by supervised classification. Under time-aware evaluation, the method attains 98% accuracy and 89% F1. We further characterize malware behavior by analyzing true positives and false negatives using VirusTotal and the MITRE ATT&CK framework. To support reproducibility and further innovation, we release our dataset and source code.

---


### 69. [Within-person prediction of depressive symptom change using year-long Screenome data and CES-D assessments](https://arxiv.org/abs/2604.23040)

**<font color=#1a73e8>作者：</font>** Merve Cerit, Andrea Mock, Vryan Almanon Feliciano 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Predicting whether an individual's depressive symptoms will worsen, remain stable, or improve over the coming weeks can enable earlier and more targeted care, yet prospective within-person trajectory prediction remains largely unaddressed in digital phenotyping. We combine fortnightly CES-D assessments with over 100 million screenshots captured every five seconds via the Stanford Screenomics platform from 96 adults followed for approximately one year (M = 20.9, SD = 3.9 assessments per participant, 2,002 total observations). We frame prediction as a within-person classification task: whether symptoms will worsen, remain stable, or improve over the subsequent fortnight, operationalized in three ways to capture clinically meaningful change. Under temporal holdout, XGBoost achieves an AUC of 0.906 for crossings of established CES-D severity bands and 0.755 for change relative to each participant's own within-person variability, generalizing to unseen individuals (AUC = 0.821). Each person's typical symptom level was the only statistically significant predictor above the most recent CES-D score; without it, the most consequential worsening transitions go undetected. Screenome-derived behavioral features revealed prodromal patterns of worsening, including escalating social media use, fragmented device engagement, and changes in overnight activity, with substantial individual heterogeneity. These findings establish a proof-of-concept foundation for monitoring systems that could identify individuals approaching clinical deterioration before symptoms reach a crisis point.

---


### 70. [A Differentiable Framework for Global Circulation Model Precipitation Bias Correction](https://arxiv.org/abs/2604.23045)

**<font color=#1a73e8>作者：</font>** Kamlesh Sawadekar, Seth McGinnis, Peijun Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Systematic biases in Global Circulation Model (GCM) outputs limit their direct applicability in regional planning, necessitating bias correction. Correcting precipitation is particularly challenging due to its non-Gaussian distribution, intermittent nature, and non-linear extremes. However, traditional statistical methods cannot learn from big data and easily address systematic biases in the GCMs, and while machine learning does provide this flexibility, their black-box type functionality hinders us from understanding these biases completely which also further prevents generalization across different GCMs and locations, especially for precipitation. In this study, we propose a differentiable bias adjustment framework called {\delta}CLIMBA (or dCLIMBA), that learns a spatiotemporally adaptive parametric bias adjustment procedure between historical CMIP6 model outputs and reference reanalysis datasets (Livneh). Results demonstrate that the proposed method accurately corrects both the magnitude and distribution of extreme storm events, with particularly strong performance in capturing extremes. The quantile distribution of precipitation is well reproduced across diverse U.S. cities, and spatial patterns perform comparably to the widely used LOCA2 statistical downscaling technique. In addition, the framework showed future trend preservation unlike pure quantile based methods and LOCA2; and results from bias correction over unseen regions showed that the marginal biases were attenuated. This work presents a modular, computationally efficient and extensible bias correction approach that is physically informed, scalable, and compatible with both historical and future applications. Its flexibility makes it suitable for integration into Earth system post-processing pipelines and impact workflows.

---


### 71. [Shape of Memory: a Geometric Analysis of Machine Unlearning in Second-Order Optimizers](https://arxiv.org/abs/2604.23046)

**<font color=#1a73e8>作者：</font>** Kennon Stewart  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We argue that current definitions of machine unlearning are underspecified for second-order optimizers. We compare first-order and second-order learners for their ability to handle the data deletion task with varying degrees of eigendecomposition to mimic the loss model memory. While both first and second-order methods realign with the ideal counterfactul in terms of performance and gradient, the second-order optimizer shows significant volatility in the optimizer state. This indicates residual information, supposedly deleted, that isn't detectable by first-order analysis. Various eigendecay treatments show that stability and information loss is regained only under controlled state pertubation where geometric information (or memory) is erased.

---


### 72. [ML-Guided Primal Heuristics for Mixed Binary Quadratic Programs](https://arxiv.org/abs/2604.23053)

**<font color=#1a73e8>作者：</font>** Weimin Huang, Natalie M. Isenberg, Ján Drgoňa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed Binary Quadratic Programs (MBQPs) are an important and complex set of problems in combinatorial optimization. As solving large-scale combinatorial optimization problems is challenging, primal heuristics have been developed to quickly identify high-quality solutions within a short amount of time. Recently, a growing body of research has also used machine learning to accelerate solution methods for challenging combinatorial optimization problems. Despite the increasing popularity of these ML-guided methods, a large body of work has focused on Mixed-Integer Linear Programs (MILPs). MBQPs are challenging to solve due to the combinatorial complexity coupled with nonlinearities. This work proposes ML-guided primal heuristics for Mixed Binary Quadratic Programs (MBQPs) by adapting and extending existing work on ML-guided MILP solution prediction to MBQPs. We introduce a new neural network architecture for MBQP solution prediction and a new training data collection procedure. Moreover, we extend existing loss functions in solution prediction and propose to combine contrastive and weighted cross-entropy losses. We evaluate the methods on standard and real-world MBQP benchmarks and show that the developed ML-guided methods significantly outperform existing primal heuristics and state-of-the-art solvers. Furthermore, models trained with our proposed extension with combined losses outperform other ML-based methods adapted from MILPs and improve generalization in cross-regional inference on a real-world wind farm layout optimization problem.

---


### 73. [K-Score: Kalman Filter as a Principled Alternative to Reward Normalization in Reinforcement Learning](https://arxiv.org/abs/2604.23056)

**<font color=#1a73e8>作者：</font>** Zixuan Xia, Quanxi Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a simple yet effective alternative to reward normalization in policy gradient reinforcement learning by integrating a 1D Kalman filter for online reward estimation. Instead of relying on fixed heuristics, our method recursively estimates the latent reward mean, smoothing high-variance returns and adapting to non-stationary environments. This approach incurs minimal overhead and requires no modification to existing policy architectures. Experiments on \textit{LunarLander} and \textit{CartPole} demonstrate that Kalman-filtered rewards significantly accelerate convergence and reduce training variance compared to standard normalization techniques. Code is available at this https URL.

---


### 74. [Urban Flood Observations (UFO): A hand-labeled training and validation dataset of post-flood inundation](https://arxiv.org/abs/2604.23066)

**<font color=#1a73e8>作者：</font>** Rohit Mukherjee, Hannah K. Friedrich, Beth Tellman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban flooding affects lives and infrastructure worldwide. Mapping inundation in complex urban environments from satellite imagery remains challenging due to limited spatial resolution, infrequent acquisitions, and cloud cover. We present Urban Flood Observations (UFO), a global, hand-labeled dataset of post-flood inundation in diverse urban settings. UFO comprises 215 image chips (1024 by 1024 pixels) from 14 flood events between 2017 and 2021, derived from 3 m PlanetScope imagery. Each chip is annotated with two classes: 'inundated' (all visible surface water, including floodwater and pre-existing water bodies (permanent or seasonal)) and 'non-inundated'. To demonstrate the dataset's utility, we trained a segmentation model using leave-one-event-out cross-validation, achieving a mean Intersection over Union (IoU) of 77.3. We also used UFO to evaluate two widely used surface water products, the Sentinel-1-based NASA IMPACT model and Google's 10 m Dynamic World water class, which yielded IoUs of 44.1 and 48.1, respectively. UFO is publicly available to support the development and validation of urban inundation mapping methods.

---


### 75. [Training a General Purpose Automated Red Teaming Model](https://arxiv.org/abs/2604.23067)

**<font color=#1a73e8>作者：</font>** Aishwarya Padmakumar, Leon Derczynski, Traian Rebedea 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated methods for red teaming LLMs are an important tool to identify LLM vulnerabilities that may not be covered in static benchmarks, allowing for more thorough probing. They can also adapt to each specific LLM to discover weaknesses unique to it. Most current automated red teaming methods are intended for tackling safety and content moderation. Thus, they make use of content safety models as evaluators and optimize for circumventing them, and as such, have not been tested with other adversarial intents not typically captured by these. We propose a pipeline for training a red teaming model that can generalize to arbitrary adversarial goals, including objectives it has not been directly trained on, and that does not depend on the existence of a pre-existing evaluator available at training time. We demonstrate that finetuning small models, such as Qwen3-8B, using this pipeline results in a substantial improvement in their ability to generate attacks for both in and out of domain adversarial goals.

---


### 76. [RL Token: Bootstrapping Online RL with Vision-Language-Action Models](https://arxiv.org/abs/2604.23073)

**<font color=#1a73e8>作者：</font>** Charles Xu, Jost Tobias Springenberg, Michael Equi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models can learn to perform diverse manipulation skills "out of the box," but achieving the precision and speed that real-world tasks demand requires further fine-tuning -- for example, via reinforcement learning (RL). We introduce a lightweight method that enables sample-efficient online RL fine-tuning of pretrained VLAs using just a few hours of real-world practice. We (1) adapt the VLA to expose an "RL token," a compact readout representation that preserves task-relevant pretrained knowledge while serving as an efficient interface for online RL, and (2) train a small actor-critic head on this RL token to refine the actions, while anchoring the learned policy to the VLA. Online RL with the RL token (RLT) makes it possible to fine-tune even large VLAs with RL quickly and efficiently. Across four real-robot tasks (screw installation, zip tie fastening, charger insertion, and Ethernet insertion), RLT improves the speed on the hardest part of the task by up to 3x and raises success rates significantly within minutes to a few hours of practice. It can even surpass the speed of human teleoperation on some of the tasks.

---


### 77. [Usable Agent Discovery for Decentralized AI Systems](https://arxiv.org/abs/2604.23080)

**<font color=#1a73e8>作者：</font>** Patrizio Dazzi, Emanuele Carlini, Matteo Mordacchini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large-scale agentic systems run on distributed infrastructures where many software agents share physical hosts and are discovered via peer-to-peer mechanisms. Discovery must handle node-level churn from failures and host departures and agent-level churn from demand-driven activation, deactivation, and state changes. Their interaction reshapes classic trade-offs between structured and unstructured overlays. We study decentralized agent discovery under this two-level churn, assuming nodes host multiple agents, overlays are structured or gossip-based, and agents switch between warm and cold states. Using Kademlia as a structured and Cyclon+Vicinity as a gossip baseline, we compare stable, node-churn-only, agent-cooling-only, and combined regimes to see when routing efficiency, resilience, and service readiness align or favor different designs. Structured overlays are more robust and efficient in stable and node-churn regimes, while gossip-based overlays remain competitive and can be faster when readiness dominates.

---


### 78. [Visual Accessibility in a Virtual Kitchen: Effects of Open Shelving on Performance, Cognitive Load, and Experience in Older Adults with and without MCI](https://arxiv.org/abs/2604.23081)

**<font color=#1a73e8>作者：</font>** Ibrahim Bilau, Eunhwa Yang, Hyeokhyen Kwon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examines how visual accessibility through cabinet design influences task performance, cognitive load, physical activity level, motivation, and user experience in a virtual kitchen among older adults with and without mild cognitive impairment (MCI). Seventeen older adults (7 with MCI, 10 without) completed a repeated-measures item retrieval task under two conditions, closed cabinets and open shelving, using a counterbalanced within-subjects design. Measures included task duration, physical activity level (ENMO), cognitive load (NASA-TLX and gaze entropy), intrinsic motivation (IMI), and post-task interviews. Open shelving significantly reduced task duration (beta = -291.20, p < .001) and physical activity level (beta = -0.00615, p = .008). Gaze entropy increased (beta = 1.29, p = .001), with a significant Setting x MCI interaction (p = .009) and moderation by MoCA score (p < .001). NASA-TLX and intrinsic motivation did not differ significantly between conditions. Qualitative findings indicated reduced reliance on memory-based search and highlighted themes related to independence, aesthetics, safety, and adoption. Overall, visual accessibility improved efficiency and reduced movement demands while altering visual-search organization, with divergence between subjective and objective indicators of cognitive load. These findings support visually accessible design strategies to enhance functional performance and inform cognitively supportive built environments for aging populations.

---


### 79. [Toward Real-World Adoption of Portrait Relighting via Hybrid Domain Knowledge Fusion](https://arxiv.org/abs/2604.23094)

**<font color=#1a73e8>作者：</font>** Qian Huang, Mayoore Selvarasa Jaiswal, Zhen Zhong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The real-world adoption of portrait relighting is hindered by dataset domain gaps, camera sensitivity, and computational costs. We address these challenges with Hybrid Domain Knowledge Fusion, a paradigm that fuses the specialized strengths of synthetic, One-Light-at-A-Time (OLAT), and real-world datasets into a compact model. Our approach features specialized prior models hardened by domain-aware adaptation, followed by augmented knowledge distillation into a lightweight student model with multi-domain expertise. Our method demonstrates a 6x to 240x inference speedup while maintaining state-of-the-art (SOTA) visual quality in the experiments. Additionally, we construct a massive, high-fidelity synthetic dataset with diverse ground-truth intrinsics to support our training pipeline.

---


### 80. [INSIGHT: Indoor Scene Intelligence from Geometric-Semantic Hierarchy Transfer for Public~Safety](https://arxiv.org/abs/2604.23095)

**<font color=#1a73e8>作者：</font>** Alexander Nikitas Dimopoulos, Joseph Grasso, John Beltz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Indoor environments lack the spatial intelligence infrastructure that GPS provides outdoors; first responders arriving at unfamiliar buildings typically have no machine-readable map of safety equipment. Prior work on 3D semantic segmentation for public safety identified two barriers: scarcity of labeled indoor training data and poor recognition of small safety-critical features by native point-cloud methods. This paper presents INSIGHT, a zero-target-domain-annotation pipeline that projects 2D image understanding into 3D metric space via registered RGB-D data. Two interchangeable vision stacks share a common 3D back end: a SAM3 foundation-model stack for text-prompted segmentation, and a traditional CV stack (open-set detection, VQA, OCR) whose intermediate outputs are independently inspectable. Evaluated on all seven subareas of Stanford 2D-3D-S (70{,}496 images), the pipeline produces Pointcept-schema-compatible labeled point clouds and ISO~19164-compliant scene graphs with ${\sim}10^{4}{\times}$ compression; role-filtered payloads transmit in ${<}15$\,s at 1\,Mbps over FirstNet Band~14. We report per-point labeling accuracy on 7 shared classes, detection sensitivity for 15 safety-critical classes absent from public 3D benchmarks alongside code-capped deployable estimates, and inter-pipeline complementarity, demonstrating that 2D-to-3D semantic transfer addresses the labeled-data bottleneck while scene graphs provide building intelligence compact enough for field deployment.

---


### 81. [ProEval: Proactive Failure Discovery and Efficient Performance Estimation for Generative AI Evaluation](https://arxiv.org/abs/2604.23099)

**<font color=#1a73e8>作者：</font>** Yizheng Huang, Wenjun Zeng, Aditi Kumaresan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating generative AI models is increasingly resource-intensive due to slow inference, expensive raters, and a rapidly growing landscape of models and benchmarks. We propose ProEval, a proactive evaluation framework that leverages transfer learning to efficiently estimate performance and identify failure cases. ProEval employs pre-trained Gaussian Processes (GPs) as surrogates for the performance score function, mapping model inputs to metrics such as the severity of errors or safety violations. By framing performance estimation as Bayesian quadrature (BQ) and failure discovery as superlevel set sampling, we develop uncertainty-aware decision strategies that actively select or synthesize highly informative inputs for testing. Theoretically, we prove that our pre-trained GP-based BQ estimator is unbiased and bounded. Empirically, extensive experiments on reasoning, safety alignment, and classification benchmarks demonstrate that ProEval is significantly more efficient than competitive baselines. It requires 8-65x fewer samples to achieve estimates within 1% of the ground truth, while simultaneously revealing more diverse failure cases under a stricter evaluation budget.

---


### 82. [Unstable Rankings in Bayesian Deep Learning Evaluation](https://arxiv.org/abs/2604.23102)

**<font color=#1a73e8>作者：</font>** Qishi Zhan, Minxuan Hu, Guansu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard evaluations of Bayesian deep learning methods assume that metric estimates are reliable, but we show this assumption fails under data scarcity. Method rankings are not only unreliable at small $n$, but also dataset-dependent in ways that point estimates cannot reveal: the same method comparison yields $P(\mathrm{MCD} \prec \mathrm{Ensemble}) = 1.000$ at $n = 50$ on one dataset and remains below $0.95$ even at $n = 500$ on another. Across the datasets we consider, no universal sample size threshold exists, which is precisely why dataset-specific posterior inference is necessary. To address this, we use a Bayesian hierarchical model with method-specific variances to treat evaluation metrics as random variables across data realizations, and we use a predictive Minimum Detectable Difference curve to assess whether an observed gap would be detectable at a given training size. Across six Bayesian deep learning methods and five regression datasets, our results show that uncertainty-aware evaluation is necessary in low-data settings, because current evidence for method superiority and predictive detectability at the same training size can diverge substantially. Our framework provides practitioners with principled tools to determine whether their evaluation data is sufficient before drawing conclusions about method superiority.

---


### 83. [Transferable Physical-World Adversarial Patches Against Object Detection in Autonomous Driving](https://arxiv.org/abs/2604.23105)

**<font color=#1a73e8>作者：</font>** Zihui Zhu, Ziqi Zhou, Yichen Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning drives major advances in autonomous driving (AD), where object detectors are central to perception. However, adversarial attacks pose significant threats to the reliability and safety of these systems, with physical adversarial patches representing a particularly potent form of attack. Physical adversarial patch attacks pose severe risks but are usually crafted for a single model, yielding poor transferability to unseen detectors. We propose AdvAD, a transfer-based physical attack against object detection in autonomous driving. Instead of targeting a specific detector, AdvAD optimizes adversarial patches over multiple detection models in a unified framework, encouraging the learned perturbations to capture shared vulnerabilities across architectures. The optimization process adaptively balances model contributions and enforces robustness to physical variations. It further employs data augmentation and geometric transformations to maintain patch effectiveness under diverse physical conditions. Experiments in both digital and real-world settings show that AdvAD consistently outperforms state-of-the-art (SOTA) attacks in performance and transferability.

---


### 84. [Conditional Imputation for Within-Modality Missingness in Multi-Modal Federated Learning](https://arxiv.org/abs/2604.23112)

**<font color=#1a73e8>作者：</font>** Wugeng Zheng, Ziwen Kan, Katie Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Federated Learning (MMFL) enables privacy-preserving collaborative training, but real-world clinical applications often suffer from within-modality missingness caused by sensor intermittency or irregular sampling. Existing methods implicitly represent unobserved data via architectural alignment or missing embeddings, often failing to recover the true distribution and yielding sub-optimal performance. We propose CondI, a federated framework explicitly addressing this missingness using conditional diffusion models. CondI employs a two-phase training pipeline: first, imputing unobserved temporal components using available multimodal context and conditional embeddings; second, optimizing modality-specific extractors and joint embedding spaces. During inference, imputed raw data pass through trained extractors to generate robust features, providing a holistic representation for downstream tasks. Explicit data imputation ensures models operate on complete semantic structures, significantly enhancing resilience against severe data incompleteness. Experiments on three clinical datasets (PTB-XL, SLEEP-EDF, MIMIC-IV) demonstrate CondI achieves comparable results to state-of-the-art baselines. Code: this https URL

---


### 85. [A Tale of Two Variances: When Single-Seed Benchmarks Fail in Bayesian Deep Learning](https://arxiv.org/abs/2604.23114)

**<font color=#1a73e8>作者：</font>** Qishi Zhan, Minxuan Hu, Liang He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In limited-data settings, a single endpoint mean of an evaluation metric such as the Continuous Ranked Probability Score (CRPS) is itself a random variable, yet it is routinely reported as if it were a stable property of the method. We study when this practice fails. Using 50 independent repetitions across six regression datasets, we show that CRPS variance trajectories differ substantially across methods and are not always well described by a smooth power-law decay. Methods with a learned heteroscedastic variance head, namely MAP and Deep Ensembles, can develop pronounced, reproducible variance peaks at intermediate training sizes on real datasets, whereas MC Dropout and Bayes by Backprop typically show smooth variance contraction. These peaks have direct practical consequences: at the variance peak on Seoul Bike, the relative RMSE of a single-seed MAP estimate reaches 93.6\%, and the probability of falling within \(\pm 10\%\) of the repeated-run mean drops to 5.9\%. We show that local CRPS variance provides a direct signal of single-seed estimation error, with Spearman correlations above 0.96 on every real dataset. Power-law fit quality and monotonicity together provide compact method-level summaries of trajectory regularity. Finally, replacing the standard heteroscedastic objective with \(\beta\)-NLL substantially reduces the irregular behavior, consistent with the view that the heteroscedastic training objective contributes to the instability. Practitioners should report trajectory summaries alongside endpoint means and concentrate repeated evaluation in high-variance regions.

---


### 86. [HBGSA: Hydrogen Bond Graph with Self-Attention for Drug-Target Binding Affinity Prediction](https://arxiv.org/abs/2604.23115)

**<font color=#1a73e8>作者：</font>** Junxiao Kong, Chupei Tang, Di Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of drug-target binding affinity accelerates drug discovery by prioritizing compounds for experimental validation. Current methods face three limitations: sequence-based approaches discard spatial geometric constraints, structure-based methods fail to exploit hydrogen bond features, and conventional loss functions neglect prediction-target correlation, a key factor for identifying high-affinity compounds in virtual screening. We developed HBGSA (Hydrogen Bond Graph with Self-Attention), a 3.06M-parameter model that encodes hydrogen bond spatial features. HBGSA uses graph neural networks to model hydrogen bond spatial topology with self-attention enhancement and Pearson correlation loss. Experimental results on PDBbind Core Set and CSAR-HiQ dataset demonstrate that HBGSA outperforms baseline methods with strong generalization capability. Ablation studies confirm the effectiveness of hydrogen bond modeling and Pearson correlation loss.

---


### 87. [Learning from Imperfect Text Guidance: Robust Long-Tail Visual Recognition with High-Noise Label](https://arxiv.org/abs/2604.23125)

**<font color=#1a73e8>作者：</font>** Mengke Li, Haiquan Ling, Yiqun Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world data often exhibit long-tailed distributions with numerous noisy labels, substantially degrading the performance of deep models. While prior research has made progress in addressing this combined challenge, it overlooks the severe label-image mismatch inherent to high-noise settings, thereby limiting their effectiveness. Given that observed labels, though mismatched with images, still retain category information, we propose employing auxiliary text information from labels to address label-image inconsistencies in long-tailed noisy data. Specifically, we leverage the intrinsic cross-modal alignment in pre-trained visual-language models to correct the label-image inconsistencies. This supervisory signal, referred to as Weak Teacher Supervision (WTS), is unaffected by label noise and data distribution biases, albeit exhibits limited accuracy. Therefore, the activation of WTS is determined by evaluating the discrepancy between text-predicted labels and observed labels. Extensive experiments demonstrate the superior performance of WTS across synthetic and real-world datasets, particularly under high-noise conditions. The source code is available at this https URL.

---


### 88. [MindTrellis: Co-Creating Knowledge Structures with AI through Interactive Visual Exploration](https://arxiv.org/abs/2604.23129)

**<font color=#1a73e8>作者：</font>** Xiang Li, Cara Li, Emily Kuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Knowledge workers face increasing challenges in synthesizing information from multiple documents into structured conceptual understanding. This process is inherently iterative: users explore content, identify relationships between concepts, and continuously reorganize their mental models. However, current approaches offer limited support. LLM-based systems let users query information but not shape how knowledge is organized; manual tools like mind maps support structure creation but lack intelligent assistance. This leaves an open opportunity: supporting collaborative construction where users and AI jointly develop an evolving knowledge representation. We present MindTrellis, an interactive visual system where users and AI collaboratively build a dynamic knowledge graph. Users can query the graph to retrieve document-grounded information, and contribute by introducing new concepts, modifying relationships, and reorganizing the hierarchy to reflect their developing understanding. In a user study where 12 participants created slide decks, MindTrellis outperformed retrieval-only baselines in knowledge organization and cognitive load, as measured by expert ratings of content coverage and structural quality.

---


### 89. [h-MINT: Modeling Pocket-Ligand Binding with Hierarchical Molecular Interaction Network](https://arxiv.org/abs/2604.23134)

**<font color=#1a73e8>作者：</font>** Yanru Qu, Yijie Zhang, Wenjuan Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate molecular representations are critical for drug discovery, and a central challenge lies in capturing the chemical environment of molecular fragments, as key interactions, such as H-bond and {\pi} stacking, occur only under specific local conditions. Most existing approaches represent molecules as atom-level graphs; however, atom-level representations can hardly express higher-order chemical context (e.g., stereochemistry, lone pairs, conjugation). Fragment-based methods (e.g., principal subgraph, predefined functional groups) fail to preserve essential information such as chirality, aromaticity, and ionic states. This work addresses these limitations from two aspects. (i) OverlapBPE tokenization. We propose a novel data-driven molecule tokenization method. Unlike existing approaches, our method allows overlapping fragments, reflecting the inherently fuzzy boundaries of small-molecule substructures and, together with enriched chemical information at the token level, thereby preserving a more complete chemical context. (ii) h-MINT model. OverlapBPE induces many-to-many atom-fragment mappings, which necessitate a new hierarchical architecture. We therefore develop a hierarchical molecular interaction network capable of jointly modeling interactions at both atom and fragment levels. By supporting fragment overlaps, the model naturally accommodates the many-to-many atom-fragment mappings introduced by the OverlapBPE scheme. Extensive evaluation against state-of-the-art methods shows our method improves binding affinity prediction by 2-4% Pearson/Spearman correlation on PDBBind and LBA, enhances virtual screening by 1-3% in key metrics on DUD-E and LIT-PCBA, and achieves the best overall HTS performance on PubChem assays. Further analysis demonstrates that our method effectively captures interactive information while maintaining good generalization.

---


### 90. [Surface Sensitivity in Lean 4 Autoformalization](https://arxiv.org/abs/2604.23135)

**<font color=#1a73e8>作者：</font>** William Feng, Ethan Lou, Aryan Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural-language variation poses a key challenge in Lean autoformalization: semantically equivalent paraphrases of the same theorem statements can induce divergent formal outputs, yet it remains unclear whether this variation reflects semantic disagreements or shallower failures. We investigate this question in Lean 4 using 60 deterministic paraphrase rules applied to ProofNet\# and miniF2F. Across four GPT-family models and three open-weight 7B autoformalizers, we find that the observed paraphrase sensitivity reflects compilation-boundary failures rather than semantic divergence among successful formalizations. In particular, when both baseline and perturbed outputs compile, paired predictions are semantically equivalent under BEq+ and structurally near-identical under GTED. By contrast, paraphrasing substantially affects whether outputs compile, with failure modes varying across datasets and perturbation classes. Our results suggest that future training-time interventions should target the compile boundary rather than the semantic layer, and that benchmarks should separate compile-conditional equivalence from surface consistency.

---


### 91. [CNN-ViT Fusion with Adaptive Attention Gate for Brain Tumor MRI Classification: A Hybrid Deep Learning Model](https://arxiv.org/abs/2604.23137)

**<font color=#1a73e8>作者：</font>** Syed Ibad Hasnain, Muhammad Faris, Hafiza Syeda Yusra Tirmizi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early detection and classifying brain tumors using Magnetic Resonance Imaging (MRI) images is highly important but difficult to extract in medical images. Convolutional Neural Networks (CNNs) are good at capturing both local texture and spatial information whereas Vision Transformers (ViTs) are good at capturing long-range global dependencies. We propose a new hybrid architecture that combines a SqueezeNet-style CNN branch with a MobileViT-style global transformer branch, through an Adaptive Attention Gate mechanism, in this paper. The gate learns dynamically per-sample, per-feature weights to weight the contribution of each branch, allowing context-sensitive merging of local and global representations. The proposed model has a test accuracy of 97.60, a precision of 97.30, a recall of 97.50, an F1-score of 97.40, and a macro-average area under the curve (AUC) of 0.9946 with a trained and evaluated on the Brain Tumor MRI Dataset (Kaggle). These scores are higher than single CNN and ViT baselines, and current competitive fusion methods, showing that dynamic feature weighting is an effective way to classify medical images.

---


### 92. [BSViT: A Burst Spiking Vision Transformer for Expressive and Efficient Visual Representation Learning](https://arxiv.org/abs/2604.23165)

**<font color=#1a73e8>作者：</font>** Hongxiang Peng, Dewei Bai, Hong Qu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spiking Vision Transformers (S-ViTs) offer a promising framework for energy-efficient visual learning. However, existing designs remain limited by two fundamental issues: the restricted information capacity of binary spike coding and the dense token interactions introduced by global self-attention. To address these challenges, this work proposes BSViT, a burst spiking-driven Vision Transformer featuring a Dual-Channel Burst Spiking Self-Attention (DBSSA) mechanism. DBSSA encodes queries with binary spikes and keys with burst spikes to enhance representational capacity. The value pathway adopts dual excitatory and inhibitory binary channels, enabling signed modulation and richer spike interactions. Importantly, the entire attention operation preserves addition-only computation, ensuring compatibility with energy-efficient neuromorphic hardware. To further reduce spike activity and incorporate spatial priors, a patch adjacency masking strategy is introduced to restrict attention to local neighborhoods, resulting in structure-aware sparsity and reduced computational overhead. In addition, burst spike coding is systematically integrated across the network to increase spike-level representational capacity beyond conventional binary spiking. Extensive experiments on both static and event-based vision benchmarks demonstrate that BSViT consistently outperforms existing spiking Transformers in accuracy while maintaining competitive energy efficiency.

---


### 93. [A Topology fixated Shape Gradient Framework for Non Simple Boundary Extraction for CIE Lab color images with Repulsive Energy](https://arxiv.org/abs/2604.23167)

**<font color=#1a73e8>作者：</font>** Shafeequdheen Palengara, Jyotiranjan Nayak, Vijayakrishna Rowthu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A levelset free but a hybrid image segmentation approach based on a modified version of the piece wise constant shape gradient of an Mumford Shah shape functional and a repulsive function is considered. The segmentation is performed a non-local shape based through an evolution of discrete curves driven by a non local shape based energy to segment images containing disjoint regions and multiple boundaries. This formulation has a novel additional component as a multivariable function dependent on a few sampled points of the curves that handles the occurrence of self intersection during boundary curves evolution. The method is applied to a few gray scale and color images, including images with nested structures and astronomical objects. The results indicate effective segmentation in complex scenarios with absolute control on the topology of the segments and self-intersections of the boundaries

---


### 94. [Core Logic and Algorithmic Performance Enhancements for a System Vulnerability Analysis Technique for Complex Mission Critical Systems Implementation](https://arxiv.org/abs/2604.23170)

**<font color=#1a73e8>作者：</font>** Matthew Tassava, Cameron Kolodjski, Jordan Milbrath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Core logic and processing improvements were made to the software for operations and network attack results review (SONARR) and are presented, herein. Previous SONARR versions' Boolean-only logic, derived from the Blackboard Architecture, was replaced with generic logic that allows any .NET type (e.g., integers, decimals, strings) to be utilized within facts. This allows calculations and equality operations with all data types to drive the algorithm's processing of network models. Additionally, multi-compute capabilities were implemented to increase the processing power for larger workloads. In this paper, the new logic objects are described, examples are presented to illustrate the efficacy of creating digital-twin systems using the new generic logic, and performance test results are presented that illustrate the expanded processing capability from the multi-compute functionality.

---


### 95. [Efficient VQ-QAT and Mixed Vector/Linear quantized Neural Networks](https://arxiv.org/abs/2604.23172)

**<font color=#1a73e8>作者：</font>** Terry Gou, Puneet Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we developed and tested 3 techniques for vector quantization (VQ) based model weight compression. To mitigate codebook collapse and enable end-to-end training, we adopted cosine similarity-based assignment. Building on ideas from attention-based formulations in Differentiable K-Means (DKM), we further improved this approach by using cosine similarity for assignment combined with top-1 sampling and a straight-through estimator, thereby eliminating the need for weighted-average reconstruction. Finally, we investigated the use of differentiable neural architecture search (NAS) to adaptively select layer-wise quantization configurations, further optimizing the compression process. Although our method does not consistently outperform existing approaches across all quantization levels, it provides useful insights into the design trade-offs and behaviors of VQ-based model compression methods.

---


### 96. [DyABD: The Abdominal Muscle Segmentation in Dynamic MRI Benchmark](https://arxiv.org/abs/2604.23187)

**<font color=#1a73e8>作者：</font>** Niamh Belton, Victoria Joppin, Aonghus Lawlor 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work introduces DyABD, a novel and complex benchmark dataset of dynamic abdominal MRIs from patients with abdominal hernias and associated high quality abdominal muscle annotations. DyABD is the first-of-its-kind in four key ways; (1) it proposes the first abdominal muscle segmentation task, (2) the dynamic MRIs are acquired whilst the patients perform various exercises, introducing extreme anatomical variability, making it one of the most challenging segmentation datasets to date, (3) it includes both pre and post corrective MRIs and (4) DyABD promotes clinical research into the high recurrence rates of abdominal hernias. Beyond dataset introduction, this work provides a comprehensive evaluation of the generalisation capabilities of existing segmentation models across Supervised, Few Shot and Zero Shot paradigms on the unseen DyABD dataset. This work reveals that there is still room for substantial improvement in the field of medical image segmentation, with the majority of techniques achieving a Dice Coefficient of 0.82. This work therefore sheds light on the true progress of the field and redefines the benchmark for progress in medical image segmentation.

---


### 97. [Follow the TRACE: Exploiting Post-Click Trajectories for Online Delayed Conversion Rate Prediction](https://arxiv.org/abs/2604.23197)

**<font color=#1a73e8>作者：</font>** Xinyue Zhang, Yuanhao Ding, Xiang Ao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Delayed feedback poses a core challenge for online CVR prediction, forcing a trade-off between label accuracy and data freshness. Existing methods address this through delay modeling or sample reweighting, yet neglect how post-click behaviors evolve over the observation period. To overcome this limitation, we formalize this evolution as feedback trajectory and propose TRACE. Instead of forcing hard labels on unrevealed samples, our method evaluates how well the accumulated feedback status aligns with conversion versus non-conversion, dynamically refining posteriors without waiting for final outcomes. To counteract early-stage trajectory sparsity, we further design a reliability-gated retrospective completer that leverages full-lifecycle data to provide adaptive posterior guidance for unrevealed samples. Extensive experiments validate TRACE's superiority over state-of-the-art baselines and confirm the retrospective completion module as a model-agnostic enhancer for existing systems. Our code is available at this https URL.

---


### 98. [StoryTR: Narrative-Centric Video Temporal Retrieval with Theory of Mind Reasoning](https://arxiv.org/abs/2604.23198)

**<font color=#1a73e8>作者：</font>** Xuanyue Zhong, Yuqiang Xie, Guanqun Bi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current video moment retrieval excels at action-centric tasks but struggles with narrative content. Models can see \textit{what is happening} but fail to reason \textit{why it matters}. This semantic gap stems from the lack of \textbf{Theory of Mind (ToM)}: the cognitive ability to infer implicit intentions, mental states, and narrative causality from surface-level observations. We introduce \textbf{StoryTR}, the first video moment retrieval benchmark requiring ToM reasoning, comprising 8.1k samples from narrative short-form videos (shorts/reels). These videos present an ideal testbed. Their high information density encodes meaning through subtle multimodal cues. For instance, a glance paired with a sigh carries entirely different semantics than the glance alone. Yet multimodal perception alone is insufficient; ToM is required to decode that a character ``smiling'' may actually be ``concealing hostility.'' To teach models this reasoning capability, we propose an \textbf{Agentic Data Pipeline} that generates training data with explicit three-tier ToM chains (intent decoding, narrative reasoning, boundary localization). Experiments reveal the severity of the reasoning gap: Gemini-3.0-Pro achieves only 0.53 Avg IoU on StoryTR. However, our 7B \textbf{Shorts-Moment} model, trained on ToM-guided data, improves +15.1\% relative IoU over baselines, demonstrating that \textit{narrative reasoning capability matters more than parameter scale}.

---


### 99. [Tessera: Secure, Near-Line-Rate Weight Streaming for UMA Edge Accelerators](https://arxiv.org/abs/2604.23205)

**<font color=#1a73e8>作者：</font>** Animan Naskar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deploying proprietary Deep Neural Networks (DNNs) on commodity edge devices demands hardware-backed Digital Rights Management (DRM) capable of withstanding both software-level and physical adversaries. In Unified Memory Architecture (UMA) systems, the host CPU and Neural Processing Unit (NPU) share physical DRAM, leaving plaintext model weights directly readable by a compromised OS kernel. Existing defenses fail in this constrained setting: trusted execution environments monopolize scarce memory with permanently reserved regions, while full-memory encryption operates at page granularity. This forces the system to fetch massive 4 KB memory pages for sub-page tensor tiles, severely crippling bandwidth.
We present Tessera, a reference architecture for inline, cache-line granularity weight decryption on UMA edge accelerators. The design intercepts 64-byte AXI bursts, computing AES-256-CTR keystreams in parallel with DRAM fetches. This streams plaintext directly into isolated NPU SRAM, creating a transient memory footprint confined to the active tile and eliminating the need for permanent memory carve-outs. Measurements across three distinct SoC platforms demonstrate that this parallelization hides cryptographic latency behind standard DRAM fetch times, a condition that holds even under worst-case timing variations. Consequently, Tessera is projected to achieve 98.4\% of the theoretical memory bandwidth ceiling (a mere 1.6\% overhead). Across standard vision and language models, page-level memory encryption suffers up to a 32x bandwidth penalty, whereas Tessera maintains an optimal 1x footprint for all layer geometries. Finally, Tessera neutralizes major UMA-specific attack vectors -- including physical DRAM extraction, rogue DMA, and compute hijacking -- and formally prevents plaintext leakage across sparse tensors.

---


### 100. [DARC-CLIP: Dynamic Adaptive Refinement with Cross-Attention for Meme Understanding](https://arxiv.org/abs/2604.23214)

**<font color=#1a73e8>作者：</font>** Qiyuan Jin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memes convey meaning through the interaction of visual and textual signals, often combining humor, irony, and offense in subtle ways. Detecting harmful or sensitive content in memes requires accurate modeling of these multimodal cues. Existing CLIP-based approaches rely on static fusion, which struggles to capture fine grained dependencies between modalities. We propose DARC-CLIP, a CLIP-based framework for adaptive multimodal fusion with a hierarchical refinement stack. DARC-CLIP introduces Adaptive Cross-Attention Refiners to for bidirectional information alignment and Dynamic Feature Adapters for task-sensitive signal adaptation. We evaluate DARC-CLIP on the PrideMM benchmark, which includes hate, target, stance, and humor classification, and further test generalization on the CrisisHateMM dataset. DARC-CLIP achieves highly competitive classification accuracy across tasks, with significant gains of +4.18 AUROC and +6.84 F1 in hate detection over the strongest baseline. Ablation studies confirm that ACAR and DFA are the main contributors to these gains. These results show that adaptive cross-signal refinement is an effective strategy for multimodal content analysis in socially sensitive classification.

---


> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-437](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
