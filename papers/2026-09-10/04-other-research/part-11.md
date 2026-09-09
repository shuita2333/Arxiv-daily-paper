# 📦 其他研究 | 2026年09月10日

> 本类共 **542** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-542**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-542**

---

### 501. [A New Backscattering Dual-Polarized Rectenna for Wireless Power Transfer and IoT Applications](https://arxiv.org/abs/2609.08833)

**<font color=#1a73e8>作者：</font>** Taki Eddine Djidjekh, Quentin Bernyer, Alexandru Takacs  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper proposes an innovative dual-polarized backscattering rectenna that operates in two distinct modesenergy harvesting and backscattering modulation-driven by two-bit digital control signals. By utilizing two orthogonal (co-and cross-) polarizations, the design represents a versatile candidate for IoT applications such as battery-free wireless sensing, identification, localization, and communication. The rectenna's dual functionality is validated through its integration into a proofof-concept battery-free wireless sensor, where it operates both as an energy harvester and as a dual-polarized backscattering modulator. As a proof of concept, a 16-byte AES-128 encrypted payload is backscattered over the wireless power transfer link to enhance the resilience of a battery-free Bluetooth Low Energy (BLE) wireless sensor against replay, relay, and eavesdropping attacks.

---


### 502. [Leveraging Visual and Geometric Priors for Metric-scale and Complete Vehicle Gaussian Reconstruction from Limited Views](https://arxiv.org/abs/2609.08841)

**<font color=#1a73e8>作者：</font>** Jinyu Miao, Jiusi Li, Yifei He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity vehicle assets are essential for controllable traffic scene generation, particularly for synthesizing rare and safety-critical long-tail scenarios. However, reconstructing a reusable vehicle representation from in-the-wild onboard images remains challenging for two reasons. First, image-to-3D generation methods generally produce models without reliable metric scale. Second, onboard cameras usually observe only one side of a target vehicle, making conventional multi-view reconstruction incomplete on unobserved regions. To solve these problems, we propose a feed-forward vehicle asset reconstruction method, which leverages two complementary priors to reconstruct 3D Gaussian representations for vehicles using sparse one-sided observations. To achieve metric-scale reconstruction, a visual foundation model is first utilized to serve as a visual prior for Gaussian initialization. The Gaussian attributes are then estimated by a learnable encoder-decoder module. A symmetry-aware cloning strategy is presented to complete the unobserved side directly in Gaussian space, which exploits the bilateral structure of vehicles as a geometric prior. Experiments on the public dataset demonstrate that the proposed method significantly outperforms existing approaches in both vehicle asset completeness and geometric accuracy.

---


### 503. [FIRE3D: Feed-forward Interactive 3D Scene Reconstruction Within A Minute](https://arxiv.org/abs/2609.08848)

**<font color=#1a73e8>作者：</font>** Hongchi Xia, Tianhang Cheng, Wei-Chiu Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FIRE3D, a unified framework that takes a single RGB image or casual RGB video and transforms it into simulation-ready 3D scene assets for games and interactive applications in under a minute. At the core of FIRE3D is a feed-forward, end-to-end network that predicts a compositional scene representation from posed RGB-D observations estimated from the RGB capture, including the 6-DoF pose, bounding box, mesh, and texture for every object. By modeling the scene as a collection of discrete entities, FIRE3D produces amodally complete and simulation-ready environments where objects are physically decoupled and ready for interaction. Our framework requires no test-time optimization, runs orders of magnitude faster than prior interaction-ready methods, and provides object-level completeness beyond existing feed-forward 3D approaches. We demonstrate competitive or state-of-the-art results across pose accuracy, geometry completeness, and texture quality across various datasets while being orders of magnitudes faster. Project page: this https URL

---


### 504. [Length Generalization for Transformers via Compression](https://arxiv.org/abs/2609.08851)

**<font color=#1a73e8>作者：</font>** Georg Zetzsche, Hongjian Jiang, Andy Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advancements in transformer length generalization theory enable us to reliably predict when a transformer can learn to solve a task. In particular, the C-RASP hypothesis (a formalized version of the so-called RASP-l conjecture) posits that transformers length-generalize on a task if and only if a solution is expressible in the C-RASP language. While this hypothesis has strong empirical validation, theoretical problems arise from the fact that no computable length generalization bounds exist for C-RASP, alongside the discovery of seemingly contradictory experiments. To address these problems, we refine the C-RASP hypothesis utilizing the recently-proposed fragments C-RASP+ and C-RASP1. These fragments have computable length generalization bounds, though in the worst case requiring an extremely large (double exponential) sample size. It is an open question whether these sample size bounds are tight. In this paper, we resolve this open question by providing an exponentially tighter bound. In doing so, we show a polynomial length generalization bound for transformers if we adopt compressed strings, via a novel connection to power words. As an application, we show how this yields a fine-grained analysis of the C-RASP conjecture that resolves contradicting experimental evidence against it.

---


### 505. [Earth System World Model for What-If Simulations: A Case Study for Terrestrial Ecosystems](https://arxiv.org/abs/2609.08855)

**<font color=#1a73e8>作者：</font>** Zhihao Wang, Ruichen Wang, Ruohan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning emulators have become essential for accelerating expensive Earth-system simulations, but most existing approaches remain passive forecasters: they reproduce simulator trajectories under prescribed forcings without an explicit interaction mechanism for user-specified interventions. This limits their use in interactive scientific workflows and Earth-system digital twins, where users often need to explore how a system would respond if selected state components were changed. We propose an action-conditioned world-modeling framework for Earth-system emulation that reformulates simulator trajectories as supervision for controllable state-transition learning. The key idea is transition-action pretraining: naturally observed state changes are treated as label-free action supervision, allowing the model to learn both prescribed dynamics and action-conditioned responses without manually annotated interventions. We further introduce masked response learning to infer unobserved variables under partial state edits and learn coupled system dependencies. We test this framework on ecosystem dynamics across six global regions and multiple stand ages. Experiments show that the model preserves competitive long-horizon emulation accuracy while enabling controllable structural interventions and coherent responses in coupled ecosystem-cycle variables. These results suggest a practical route from passive Earth-system emulators toward interactive, intervention-aware scientific surrogates.

---


### 506. [Towards Standardized Evaluation of GPU Memory Safety with GMSBench](https://arxiv.org/abs/2609.08871)

**<font color=#1a73e8>作者：</font>** Saurabh Singh, Jaewon Lee, Seonjin Na 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As GPUs become increasingly integral to high-performance computing and machine learning, ensuring memory safety in GPU programs has become crucial for reliable and secure execution. However, evaluating GPU memory safety techniques remains challenging due to the lack of comprehensive and standardized benchmarks. In this paper, we present GMSBench, a GPU memory safety benchmark designed to evaluate a broad range of memory safety violations across different GPU memory spaces and execution scenarios. GMSBench comprises 149 self-contained CUDA tests spanning spatial, temporal, and concurrency errors. The suite provides a standardized foundation for the evaluation and comparative analysis of GPU memory safety mechanisms and helps expose gaps in their detection coverage. We demonstrate the utility of GMSBench by evaluating Compute Sanitizer, a widely used GPU memory error detection tool across multiple GPU architectures.

---


### 507. [Medical AI Encodes a "Feeling of Error": Verifying Cancer Segmentation via Internal Concepts](https://arxiv.org/abs/2609.08879)

**<font color=#1a73e8>作者：</font>** Mengmeng Ma, Yunxiang Peng, Tang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cancer segmentation models can fail silently, generating plausible but incorrect masks that risk missed findings or unnecessary biopsies. A critical question arises: Do AI models "know" when they are wrong, and if so, can we use the signal to predict their own failures? Humans do have a "Feeling of Error" (FOE): a spontaneous sense of unease that flags a potential error during thinking. We investigate whether cancer segmentation models exhibit an analogous internal signal. Unlike output-level cues (e.g., prediction confidence or uncertainty), which offer no insight into why a failure occurs and suffer from a sensitivity-quality tradeoff where high detection sensitivity could degrade overall segmentation quality. We instead propose to capture the model's FOE from its inner workings. Using mechanistic interpretability tools, specifically Sparse Autoencoders, we decompose internal neural activations into a dictionary of human-interpretable concepts and show that failure cases exhibit a distinct latent signature: fewer active concepts with lower activation magnitudes compared to successful segmentation. By training a classifier on these concept activations, we achieve accurate failure detection along with explanations for the model's mistakes. Experiments on prostate, pancreatic, and brain cancer segmentation demonstrate that our approach outperforms output-based methods in failure detection while preserving segmentation quality.

---


### 508. [FRAME: Factored Retrieval via Attribute Readouts for Object-Centric Scene Memory](https://arxiv.org/abs/2609.08886)

**<font color=#1a73e8>作者：</font>** Woosang Jeon, Sanghyeok Choi, Minwoo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-guided robots need persistent scene memories to follow instructions, revisit objects, and resolve references to objects encountered over time. While much of language-guided scene-memory retrieval has emphasized spatial or relational references, many everyday object references specify objects by multiple persistent attributes, such as category, material, size, or surface appearance. We formalize this problem as attribute-compositional retrieval, where a fixed object-centric scene memory is queried with natural language to retrieve the object satisfying the requested attributes. To investigate this capability directly, we introduce a controlled evaluation protocol with fixed scene memories and attribute-defined targets, separating retrieval from perception and annotation ambiguities. We then propose FRAME, which turns language into query-relevant attribute weights, uses learned readouts to estimate per-attribute evidence from object embeddings, and ranks objects by aggregating this evidence according to the query. Across held-out scenes and object assets, FRAME outperforms representative scene-memory retrieval baselines while reducing post-decomposition object scoring to lightweight matrix-vector computation. These results position attribute-compositional retrieval as a complementary scene-memory capability for language-guided robots, showing that persistent object attributes can be exposed as composable evidence for accurate and efficient multi-attribute retrieval.

---


### 509. [Healthcare Utilization, Chronic Condition Management, and Workplace Functioning Among Users of a Purpose-Built Mental Health AI (Ash): Cross-Sectional Study](https://arxiv.org/abs/2609.08890)

**<font color=#1a73e8>作者：</font>** Kristen M. Van Swearingen, Thomas D. Hull, Jeffrey Swigert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mental health challenges can exacerbate physical symptoms and complicate management of chronic conditions. Purpose-built artificial intelligence (AI) tools may offer scalable support for co-occurring mental and physical health concerns. This cross-sectional study compared past-6-month healthcare utilization, chronic condition management, physical health behaviors, mental health change, and workplace functioning between active (n = 169) and non-users (n = 73) of a mental health AI (Ash). Participants had at least one chronic condition (e.g. hypertension, chronic pain). Binary outcomes were modeled as adjusted risk differences (RDs) using linear probability models and continuous outcomes were modeled with linear regression; all models were adjusted for hypertension. Relative to non-users, active users were more likely to report improved mental health (61.4% vs. 34.3%; RD = 0.27), higher medication adherence (91.7% vs. 76.4%, RD = 0.15), fewer skipped or delayed chronic-condition care activities (b = -0.44), and were less likely to report repeat urgent care visits (9.5% vs. 23.3%; RD = -0.15) and monthly-or-more absenteeism (24.2% vs. 45.2%; RD = -0.20, all ps < .05). Findings provide preliminary evidence that use of purpose-built AI may be associated with positive symptom-based and utilization outcomes for those managing co-occurring mental and physical concerns.

---


### 510. [The BatchNorm Illusion: Diagnosing Normalization Artifacts in Machine Unlearning Evaluation](https://arxiv.org/abs/2609.08901)

**<font color=#1a73e8>作者：</font>** Aaryaman Kalani, Murari Mandal, Dhruv Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Approximate machine unlearning aims to remove the influence of specific training data from a trained model without retraining from scratch. We identify a previously undocumented confound in how unlearning is evaluated on BatchNorm-based architectures: a single forward pass over retain data, an operation that modifies no weight, can deterministically rewrite the model's normalization state and reverse the apparent surface-metric forgetting. We formalize this operation as a weight-preserving fixed-point operator and prove that any pre-versus-post gap it induces is provably attributable to BN running statistics rather than to any modification the unlearning method made to the weights. This attribution claim cleanly separates measurement failure (BN artifact) from encoder failure (residual weight-encoded information, recently documented in concurrent work), and the same operator framework yields a unique decomposition of linear-probe elevation into BN-measurement-bias and encoder-geometry components. Empirically, the artifact reverses headline forget accuracy by up to 78 pp across nine evaluated methods on standard benchmarks; an attacker with as few as 10 unlabeled images recovers most of the masked accuracy; and a strict GroupNorm control reduces the artifact to zero across all methods. The tested membership-inference attacks change little under recalibration, locating the observed evaluation failure in forget accuracy and linear probing.

---


### 511. [To Stop or Not to Stop: Exploring the Intention-Behavior Gaps in Smartphone Usage](https://arxiv.org/abs/2609.08909)

**<font color=#1a73e8>作者：</font>** Jian Zheng, Eun Kyoung Choe  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As smartphones become integral to daily life, researchers have sought to identify when the use becomes problematic. Previous studies have operationalized problematic smartphone usage (PSU) from either an intention or a behavior perspective. Both risk delivering interventions not welcomed by users. We propose a novel approach to operationalizing PSU as the intention-behavior gap (IBG). We collected self-reported data on intentions to stop phone usage, alongside usage behavior data, from 37 participants over two weeks. We calculated IBG, examined effects of demographic and contextual variables, and developed machine learning models to predict IBG in real time. We found that IBG was explained by gender, time, app, and input interactions, among other factors. Intention was predicted most accurately with only personal data, whereas behavior and IBG were predicted most accurately with both personal and global data. Our findings can inform the design of future intervention tools optimized for timing and adaptive intensity.

---


### 512. [CoSA: Correlation-Guided Change A ttention with Learnable Residual Gating for Remote Sensing Change Detection](https://arxiv.org/abs/2609.08914)

**<font color=#1a73e8>作者：</font>** Abdirashid Omar, Jonghyuk Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-level annotation of fixed traffic-camera imagery is expensive, while crosswalk models trained from street-level imagery face a substantial viewpoint and appearance shift when applied to elevated CCTV. We investigate a data-efficient target-domain pipeline using 241 manually annotated CCTV images and 5,926 unlabeled CCTV frames. A source-domain experiment trains a 31.0M-parameter custom U-Net on 3,300 first-person-view (FPV) images and obtains 93.05% IoU on its 330-image FPV test split. This result is a source baseline, not transferred performance: the released CCTV notebook instantiates a 42.0M-parameter DeepLabV3-ResNet50 from torchvision weights, and no compatible mapping from the U-Net checkpoint is implemented. Training on 201 manual CCTV images and selecting on 40 held-out manual masks yields 88.91% IoU. The model then predicts all unlabeled frames; image-level certainty and a largest-component area prior rank the candidates, and the top 1,000 attain mean certainty 0.976 and mean combined score 0.988. A repository audit shows that the reported second-stage 98.52% IoU was measured on a 150-image split containing only teacher-generated pseudo-masks. Because of a directory-layout mismatch, the executed combined-data loader found zero manual samples and split 1,000 pseudo-labeled samples into 850 training and 150 evaluation samples. We therefore report 98.52% as internal pseudo-label agreement rather than human-ground-truth accuracy. The defensible target-domain result is 88.91% IoU on the 40 manual validation images. Batch-one FP32 inference at 512 x 512 requires 12.98 ms, corresponding to 77.03 FPS, on an NVIDIA RTX A6000 48 GB GPU. These findings support the practicality of confidence-and-geometry filtering while also showing why pseudo-label evaluation must remain isolated from the labels used for self-training.

---


### 513. [Prior-free relative 6D pose estimation of multiple object instances](https://arxiv.org/abs/2609.08949)

**<font color=#1a73e8>作者：</font>** Behdad Khodabandehloo, Andrea Caraffa, Davide Boscaini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object 6D pose estimation formulations have progressively reduced reliance on object-specific priors, evolving from explicit 3D models to multi-view object captures to single reference images. We take this progression to its extreme by introducing prior-free relative 6D pose estimation, which lifts the assumption of knowing which object is to be posed within the scene. This novel setting aims to estimate the relative poses of multiple instances of an unknown object within the same image, without requiring CAD models, templates, or reference images. We solve this by formulating a novel method (PROSE) that finds coarse correspondences between object instances using multimodal foundation features, thus requiring no training. We refine these correspondences by imposing cycle consistency across tuples of instances, and leverage the resulting globally consistent correspondences to estimate the relative 6D pose between any pair of instances. To enable systematic evaluation, we design a novel benchmark (PRENCH) built from three multi-instance BOP datasets and enriched with task-specific metadata. PROSE consistently outperforms baselines obtained by adapting state-of-the-art single-image methods to the proposed setting, while requiring neither task-specific supervision nor additional learned components. Project website: this https URL

---


### 514. [On APN Functions with Boomerang Uniformity One over $\mathbb F_{3^n}$: Differential and Boomerang Spectra and CCZ-Inequivalence](https://arxiv.org/abs/2609.08968)

**<font color=#1a73e8>作者：</font>** Namhun Koo, Soonhak Kwon, Minwoo Ko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Let $q=3^n$, where $n>1$ is odd, and let $g:\Fq\to\Fq$ be a perfect nonlinear (PN) function represented by a Dembowski--Ostrom (DO) polynomial. Put $\tau=g(1)$, let $\epsilon$ be the indicator of $\Fthree^*$, and, for $c\in\Fq$, define $\widetilde G_c(x):=g(x+c)+\tau\epsilon(x)$. We prove that every $\widetilde G_c$ is APN and has boomerang uniformity either one or two. More precisely, \[
\beta_{\widetilde G_c}=1
\quad\Longleftrightarrow\quad
c\in\mathcal C_g
:=\{c\in\Fq\setminus\Fthree:g(c)+\tau\notin g(\Fq)\},
\qquad
|\mathcal C_g|=\frac{q-3}{2}, \] whereas $\beta_{\widetilde G_c}=2$ for the remaining $(q+3)/2$ parameters. We determine the common differential spectrum and complete boomerang spectra of all the functions $\widetilde G_c$. Since boomerang uniformity one is the least possible for an APN function over a finite field of odd characteristic, this gives, to the best of our knowledge, the first general construction yielding infinite families of APN functions attaining this optimum.
This common differential spectrum rules out CCZ equivalence with every power function and every Ness--Helleseth-type binomial. We also prove that CCZ equivalence between sign-switches of DO PN functions forces EA equivalence between the original PN functions. Using the orders of the nuclei of the associated presemifields, we exhibit, for infinitely many odd $n$, three pairwise CCZ-inequivalent PN functions over $\F_{3^n}$, one from each of the Gold $f_1$, Ding--Yuan $f_3$, and Bierbrauer $f_5$ families. Consequently, over each such field, our construction produces three pairwise CCZ-inequivalent APN functions with boomerang uniformity one. The smallest extension degree obtained in this way is $n=45$.

---


### 515. [GraphFAS: A Distributed System for Automated Graph Feature Generation and Selection in Industrial Transaction Networks](https://arxiv.org/abs/2609.08970)

**<font color=#1a73e8>作者：</font>** Yice Luo, Yun Zhu, Xi Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial fraud detection often relies on costly expert-crafted features that overlook graph-structured relational signals, while GNNs often do not meet the interpretability and deployment requirements of financial risk control. We propose GraphFAS (Graph Feature Automated Selection), a distributed feature selection procedure based on Boruta that bridges this gap through: (1) a non-parametric graph feature generation module that constructs explicit, interpretable structural features via multi-hop subgraph extraction and multi-scale aggregation without learned parameters; and (2) an automated distributed feature selection algorithm extending Boruta with median-based aggregation across partitions to robustly identify informative features at scale with minimal domain expertise. Compared with end-to-end GNN pipelines, GraphFAS decouples feature aggregation from model training, enabling direct integration with tabular models and direct compatibility with TreeSHAPbased explanations. Deployed in Alipay, GraphFAS delivers orderof-magnitude improvements in engineering efficiency while showing strong performance against expert-driven and graph-learning baselines on large-scale graphs.

---


### 516. [Embedded Human-Centered Data Science in a Graduate Programming Course: A Framework and Case Study](https://arxiv.org/abs/2609.08982)

**<font color=#1a73e8>作者：</font>** Victoria Chui, Kelly McConvey, Daniel Chui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI and data-driven systems pervade practice, there is an imperative for instructors to embed societal impact and ethics content into computing courses. In response, we present the Human-Centered Education for Learning in Information and eXplainable Computing (HELIX) framework for information science programs, organized around three iterative pillars - knowledge building, decision-making, and empowerment - with concrete actions for instructors and students. We applied the framework in a graduate, introductory programming course using readings, algorithmic design activities, and scenario-based reflections. We present a pilot implementation of this framework to examine changes in students' (n=22) knowledge acquisition, decision-making processes, and self-reflection regarding human-centered perspectives in data science. We release an anonymized materials kit (survey, assignments, analysis code) to support adoption. We discuss design tensions (workload, assessment, relevance to diverse information science learners) and provide guidelines for integrating human-centered content without overwhelming technical outcomes. Findings suggest that the HELIX Framework is feasible in information science contexts and future work should use comparative survey assessment to strengthen causal inferences.

---


### 517. [Physics-Informed Deep Learning for False Ventricular Tachycardia Alarm Reduction in the ICU](https://arxiv.org/abs/2609.08992)

**<font color=#1a73e8>作者：</font>** Athanasios Papastathopoulos-Katsaros, Alexandra Stavrianidi, Zhandong Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> False ventricular tachycardia (VT) alarms are a leading contributor to alarm fatigue in intensive care units. We propose a deep learning framework combining a 1D SE-ResNet with ICU-realistic data augmentations and a physics-informed auxiliary reconstruction task based on the three-element Windkessel hemodynamic model, implemented as a differentiable forward simulation. By requiring the network's latent representation to produce physiologically plausible arterial pressure waveforms, artifact-driven ECG patterns are penalized while true VT remains coherent across modalities. Evaluated on the VTaC benchmark under a strict real-time protocol (10-second pre-alarm window), our method achieves a 5-point Challenge Score improvement over prior state-of-the-art. Ablation studies confirm that the physics-informed objective is the primary performance driver, providing gains in accuracy, 2x label efficiency, and more localized and clinically meaningful ECG segments.

---


### 518. [Concentrate After Imagination: Text-Conditioned Evidence Grounding for Partially Relevant Video Retrieval](https://arxiv.org/abs/2609.08999)

**<font color=#1a73e8>作者：</font>** Shuaiqi Cheng, Siyu You, Yanbi Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Partially Relevant Video Retrieval (PRVR) retrieves untrimmed videos when queries describe only short moments. Although recent methods improve local representations, uncertainty modeling, and global context, final ranking often still trusts the strongest local response; a coincidentally similar fragment can therefore produce an unsupported peak. We identify this failure as the query-agnostic concentration bottleneck and propose TRACE, a score-level evidence verification operator for PRVR. Given a query and global video registers, TRACE activates query-relevant registers, routes their support to frame-level evidence, and smoothly marginalizes alternative query-to-register-to-frame paths before localized temporal selection. Unlike representation-level feature fusion, TRACE uses this evidence only as a query-conditioned residual calibration of the original local score. On ActivityNet Captions, Charades-STA, and TVR, TRACE achieves the best SumR on all three benchmarks and improves the DreamPRVR backbone by 1.2, 1.1, and 1.5 points, respectively. Ablation, routing-corruption, hard-negative, and cross-backbone transfer analyses support the interpretation that the gains arise from query-conditioned evidence verification rather than a generic score offset.

---


### 519. [Let It Go or Learn to Self-Correct: Continuous Diffusion for Constrained Discrete Tasks](https://arxiv.org/abs/2609.09009)

**<font color=#1a73e8>作者：</font>** Mariia Drozdova, Stéphane Liem Nguyen, François Fleuret  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Denoising Diffusion Probabilistic Models (DDPMs) generate samples by starting from noise and repeatedly denoising while keeping each update close to the current noisy state. This behavior is effective in many continuous domains, but its role is less clear for globally constrained discrete tasks, such as Sudoku, graph connectivity, Latin squares, and N-queens. In such settings, early discrete errors can be difficult to undo. As a result, standard diffusion sampling may preserve early mistakes, even when the model's clean predictions are informative. We compare standard samplers to sampling directly from the model's clean prediction. Without retraining, this single change improves Sudoku validity from 31% to 95%, with consistent gains across the other discrete tasks. We hypothesize that staying close to the current noisy state is harmful because the reverse trajectory can drift off the forward noising distribution the model was trained on. To reduce this train-test mismatch, we further introduce self-correction training, which exposes the model to its own predictions, improving robustness to errors that arise during inference. This substantially improves the performance of standard samplers. Our results suggest that continuous diffusion models can learn nontrivial global constraints, but discrete reasoning tasks require better alignment between training and inference: either through samplers that reduce commitment to early decisions, or through training that teaches the model to correct its own inference-time errors.

---


### 520. [A Joint 2D-3D Statistical Shape Model for Orthopedic Reconstruction](https://arxiv.org/abs/2609.09010)

**<font color=#1a73e8>作者：</font>** Florence Dell'Aniello Picard, Pranav Poudel, Nairouz Shehata 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional femoral reconstruction from radiographs supports surgical planning, implant sizing, and post-operative follow-up, but remains ill-posed as X-ray projections discard depth information. Existing methods often incorporate a 3D statistical shape model (SSM) as a shape prior to guide reconstructions toward anatomically plausible shapes, relying on iterative 3D-to-2D projection matching. Yet, these approaches are computationally expensive and constrain their SSM to a single dimensionality, leaving the statistical relationship between 2D observations and 3D geometry largely unexploited and unexplored. We instead propose a joint 2D-3D SSM that explicitly captures the co-variation between 2D and 3D segmentations in a shared latent space. During training, 2D and 3D segmentations are registered to a common 3D template and its corresponding 2D projections, and the resulting stationary velocity fields are jointly decomposed using principal component analysis (PCA). This joint modeling allows the 2D-to-3D mapping to be learned directly from data rather than computing correspondences at inference time. For unseen subjects, the 3D shape is recovered directly by lifting the 2D latent coordinates to the 3D PCA subspace, thereby eliminating the need for iterative 3D-to-2D projection. Experiments on NMDID demonstrate that the proposed joint 2D-3D SSM outperforms a widely-used 3D-only SSM baseline while achieving inference approximately 4 times faster, at under 3 seconds per subject. The code is available at: this https URL.

---


### 521. [Spheriverse: 3D Scene Understanding from Spherical Observations in the Wild](https://arxiv.org/abs/2609.09012)

**<font color=#1a73e8>作者：</font>** Fei Teng, Sheng Wu, Mengfei Duan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spherical observations provide global visual context for 3D scene understanding. However, visual information is encoded in an angular domain, whereas the physical world is represented in Cartesian coordinates. This cross-space representation gap complicates geometric correspondence and semantic evidence aggregation. To delve into this challenge, we introduce Spheriverse, comprising $64,400$ temporally aligned spherical image-LiDAR pairs organized into 644 sequences. The dataset spans diverse scenes, illumination, and weather conditions, with fine-grained semantic classes. We further establish benchmarks for semantic occupancy prediction, semantic mapping, and 3D object detection, evaluating 30+ methods through overall and scene-wise comparisons. For dense prediction, we propose SphereOcc, an occupancy framework that couples spherical geometry modeling with semantic evidence retrieval. Cartesian-Spherical Representation Remodeling (CSRR) incorporates spherical range-azimuth geometry into Cartesian voxel features through region-wise modulation. Spherical Evidence Re-querying (SER) then conditions queries on voxel content and range-height-azimuth geometry to adaptively retrieve relevant semantic evidence from source spherical image features. SphereOcc achieves 13.91% mIoU and 24.65% GeoIoU, outperforming the respective best-performing methods, TPVFormer and SurroundOcc, by 1.70 and 2.10 percentage points. It also ranks first in both metrics across all five scenes, with consistent advantages across the evaluated spatial partitions and reduced fields of view. The established benchmark and source code will be available at this https URL.

---


### 522. [PIC: Revisiting INR for Image Coding with Fast Encoding and Sub-Millisecond Decoding](https://arxiv.org/abs/2609.09020)

**<font color=#1a73e8>作者：</font>** Xiang Liu, Jinxiang Wang, Bin Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representation (INR) has achieved remarkable progress in novel view synthesis and image/video coding in recent this http URL to conventional end-to-end image codecs, INR-based compressors demonstrate significant advantages in decoding complexity. However, their practical application has been hindered by the inferior encoding speed and underutilized decoding this http URL this work, we propose a feedforward INR image coding architecture, Practical INR Image Codec (PIC), that computes all the necessary information for INR network in a single forward pass, achieving an encoding speed of 20 FPS. Additionally, we implement a highly optimized decoder that reaches 2000 FPS decoding speed, significantly surpassing JPEG's performance at comparable rate-distortion (RD) performance. To the best of our knowledge, this work presents the first learning-based image codec that simultaneously outperforms or is comparable with JPEG in both RD performance and decoding speed while maintaining practical encoding speed. Code is available at this https URL.

---


### 523. [Task-driven Processing with Coarse-to-Fine Glimpse-based Active Perception](https://arxiv.org/abs/2609.09025)

**<font color=#1a73e8>作者：</font>** Oleh Kolner, Thomas Ortner, Stanisław Woźniak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art vision models process images in their entirety, lacking the ability to selectively zoom in on relevant regions. This limitation is particularly acute in scenarios where processing must be conditioned on a specific task - such as instance detection, which requires localizing a specific object in a high-resolution, cluttered scene. In such settings, critical details are easily lost as images are often resized to match the model dimensions and computational constraints. We introduce Coarse-to-Fine Glimpse-based Active Perception (CF-GAP), a task-driven front-end that enhances high-resolution processing of existing instance detectors. CF-GAP selectively directs a sequence of limited view glimpses across the scene, utilizing task information to iteratively refine focus on the most relevant regions. These localized regions are then processed at high resolution by a downstream instance detector. By avoiding full-image processing and eliminating irrelevant confounding information, CF-GAP improves Average Precision (AP) by up to 20% across various state-of-the-art instance detectors on the HR-InsDet and Robotools benchmarks, while further enabling lightweight detectors to outperform their larger counterparts.

---


### 524. ["World Knowledge" in the Weights: Reading Concept Circuits of Vision Transformers](https://arxiv.org/abs/2609.09055)

**<font color=#1a73e8>作者：</font>** Yanlin Chen, Tang Li, Xi Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision transformers (ViTs) have achieved remarkable generalization across visual domains, yet little is known about how they internally represent the structure of the world. To address this gap, we use Cross-Layer Transcoders (CLTs) to read concept circuits from ViTs: directed graphs whose nodes correspond to sparse, interpretable concepts and edges capture concept interactions across layers. Our method yields two complementary views of model behavior. The global concept circuit is input-invariant and can be recovered directly from learned cross-layer weights, exposing the reusable "world knowledge" encoded in the model. The instance concept circuit is input-dependent and identifies the concepts and pathways actually used for a specific prediction, enabling faithful example-level explanations. We demonstrate the utility of concept circuits in three ways: (1) Automatic spurious correlation discovery: leveraging the statistics of our global concept circuits to identify shortcut dependencies within the model. (2) Spurious correlation removal: intervening on the instance concept circuit to steer the model towards correct predictions. Empirical results show that our method outperforms existing counterparts by 11.0% on the Waterbird dataset. (3) Model comparison: contrasting the global concept circuits of different foundation models (e.g., CLIP vs. DINO) to reveal how supervision paradigms shape representational structure. Our code is available at this https URL

---


### 525. [Time-Varying Data as Sheaves: an Invitation to Narratives](https://arxiv.org/abs/2609.09056)

**<font color=#1a73e8>作者：</font>** Wilmer Leal, Benjamin Merlin Bumpus, Jana K. Nickel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern science and engineering increasingly rely on time-varying data, yet the mathematical tools used to model temporal phenomena are often developed within separate disciplines, obscuring common principles and limiting the transfer of ideas across fields. This chapter presents the theory of narratives, an abstract framework for time-varying objects of any mathematical kind that supports both theoretical investigations and applications. To illustrate this perspective, the chapter develops three vignettes, each illustrating a different research direction. The first addresses a general concern: What information loss can occur when switching between different representations of temporal data? The second concerns structural and algorithmic approaches: How can we systematically decompose time-varying data into simple pieces and obtain invariants describing its structural complexity? The third is an application to control theory: How can we model multi-agent systems with switching communication topologies? More important than any individual vignette, the central message of this invitation is that a suitable abstract perspective can organize and guide research across remarkably diverse mathematical and scientific domains.

---


### 526. [Location-Independent Robot-Assisted Finishing Using Digital Twins and Extended Reality](https://arxiv.org/abs/2609.09061)

**<font color=#1a73e8>作者：</font>** Jose Outeiro, Jia Holt, Tero Kaarlela 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents a cyber-physical system (CPS) for location-independent programming, supervision, training, and teleoperation of a Robot-Assisted Finishing (RAF) system used to post-process metal additive-manufactured (AM) components. A digital twin (DT) built in Unity is delivered to the operator as a WebGL application that supports both desktop and immersive modes through WebXR-compatible devices. Moreover, it exchanges robot state and pose commands with a collaborative robot through a Message Queuing Telemetry Transport (MQTT) broker. The DT enforces kinematic and collision constraints before a pose is released to the physical robot, and augments the virtual component with a color map of the surface topography that supports operator decisions on part repositioning or process termination. The architecture was validated on a specially designed physical RAF system. A steady-state joint synchronization error of 0.12 deg and a mean round-trip latency of 563 ms were measured, which is adequate for supervisory programming and intermittent teleoperation.

---


### 527. [Multi-Task Learning for Sparsely-Labeled Time Series: A Case Study on Cold-Hardiness Modeling](https://arxiv.org/abs/2609.09062)

**<font color=#1a73e8>作者：</font>** Aseem Saxena, Paola Pesántez-Cabrera, Jonathan Magby 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a real-world case study of multi-task learning (MTL) for temporal process modeling from limited data with temporally sparse labels. Specifically, we investigate multi-task learning for the important agricultural problem of predicting grape cold hardiness, which is the temperature at which lethal freezing occurs. Cold hardiness changes in response to weather and is difficult to measure directly in the field. Thus, growers rely on predictions to decide when to apply costly frost mitigation measures. We apply recurrent neural networks (RNNs) for daily cold-hardiness prediction from time series weather data. A major challenge is that the cold hardiness response varies across plant cultivars and ground-truth data for each cultivar is temporally sparse and limited. To address this challenge, we investigate multi-task learning (MTL) approaches for combining data, where different tasks correspond to different cultivars. We develop a variety of MTL architectures and evaluate them in both MTL and transfer learning settings. Our results show significant differences between architectures and that certain architectures are able to consistently outperform single-task learning and state-of-the-art scientific models. Additionally, we show similar results for the qualitatively different, but related, task of budbreak prediction. Further, improved accuracy for budbreak and cold hardiness is achieved by a single MTL model that simultaneously learns both tasks.

---


### 528. [The Surprising Effectiveness of Approximate Value Iteration in Self-Play](https://arxiv.org/abs/2609.09094)

**<font color=#1a73e8>作者：</font>** Raphael Boige, Amine Boumaza, Bruno Scherrer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Combining search with function approximation has driven major advances in game-playing programs, making self-play algorithms more competitive than ever. Still, the computational overhead of the most popular methods, based on Monte Carlo Tree Search (MCTS), can be substantial. In this work, we investigate whether simpler methods remain competitive in non-trivial, moderately sized games such as Connect Four, Hex(7x7) and synthetic games. We train a minimal self-play implementation of Approximate Value Iteration (AVI) and use ground-truth oracles for exact evaluation. Contrary to expectations, our results demonstrate the surprising effectiveness of AVI: it learns more accurate value functions than those learned by AlphaZero, while its one-step-lookahead greedy policies remain competitive with MCTS-based policies at substantially lower training and inference costs. Preliminary experiments on Othello and Go(9x9) show that AVI trains stably on larger games and learns effective value functions. These findings suggest that the success of MCTS-based methods may have eclipsed simpler approaches that have become increasingly practical with modern deep-learning tools.

---


### 529. [Curriculum Learning as Transport: Understanding Curricula with Wasserstein Geodesics](https://arxiv.org/abs/2609.09099)

**<font color=#1a73e8>作者：</font>** Changho Shin, David Alvarez-Melis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Curriculum learning is governed by several coupled design choices---how difficulty is defined, how examples are ordered, how much exposure each level receives, and how quickly training moves across levels---making it hard to isolate what actually helps. We present Wasserstein curriculum paths, a simple transport-based framework that decouples these factors by representing curricula as trajectories of training distributions over discrete difficulty levels. Across a calibrated synthetic suite with 12 tasks and 33 difficulty axes, we use this framework to isolate the effects of ordering, matched exposure, endpoint smoothness, and pacing under fixed training budgets. We find that curriculum effects are strongly context-dependent: no single strategy dominates across tasks, difficulty axes, and budgets, and curricula mainly change where a fixed budget is spent most effectively. Within this framework, easy-to-hard ordering improves hard-level performance relative to exposure-matched static sampling, showing that the benefit is not explained by cumulative exposure alone. We further show that endpoint smoothness and pacing substantially affect where along the difficulty spectrum a curriculum is effective. Finally, we show that the same transport view naturally supports extensions to learned pacing through geometry and to structured difficulty spaces beyond one-dimensional orderings.

---


### 530. [Travel Package Booking Application with API Bot](https://arxiv.org/abs/2609.09112)

**<font color=#1a73e8>作者：</font>** K Sai Karthik, CH Naveen Aaditya, Ravi Kiran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> These days we are witnessing many mobile applications based on the recommended systems, which have become a great technology which is been used by the various mobile applications according to the situation. Recommendation provided by the mobile application is a key element for the person who is traveling to several places. For any tourist information application contextual information is much needed to guide the user on his interests this can be achieved by the Context-aware computing. Which provides the user most interactive system with the suggestions provided by it based on the input from the user in a certain location, here context includes the user's mental, social, physical environments. To achieve this contextual information, we will design and implement the context-aware user interface based on the user for which we have to study the user and design a rich user interface. The final outcome for which users have the satisfaction when using context-aware functionality will be much better than non-context-aware application.

---


### 531. [Mask Forcing: Improving Autoregressive Video Diffusion Distillation via Dual-Noise Masking Rollout](https://arxiv.org/abs/2609.09123)

**<font color=#1a73e8>作者：</font>** Zhuoran Zhao, Shengju Qian, Tongtong Liang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) video diffusion models have shown great potential in real-time video generation. Recent methods distill pretrained bidirectional video diffusion models into causal AR students through Distribution Matching Distillation (DMD), but the generated videos often suffer from over-saturation and over-smoothing issues, resulting in limited visual quality and realism. The key contributing factor is the mode-seeking behavior of the reverse KL objective in DMD, which can cause the student distribution to collapse onto only a few modes of the teacher distribution. To address this, we propose Mask Forcing, a Dual-Noise Masking Rollout strategy that perturbs the AR student self-rollout to mitigate mode collapse induced by reverse-KL mode seeking. The core idea is to inject cleaner signals into noisy rollout inputs via random masks along spatial and temporal axes during the self-rollout process of AR diffusion distillation. Such perturbations encourage the student rollouts to explore more regions of the teacher distribution, allowing DMD to provide learning signals beyond the modes already covered by the student. Moreover, the cleaner tokens act as denoising guidance for other noisier tokens, improving the intermediate rollout predictions and reducing error accumulation. Extensive experiments demonstrate that our method improves multiple AR video diffusion distillation methods with higher visual quality efficiently, without incorporating real video data or additional post-training stages.

---


### 532. [A Generalization of Amari's Bayesian Duality](https://arxiv.org/abs/2609.09126)

**<font color=#1a73e8>作者：</font>** Mohammad Emtiyaz Khan, Thomas Möllenhoff  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Amari's contributions to information geometry and machine learning are well known. Here, we revisit Amari's work on Bayesian duality which has not received as much attention. We connect Amari's Bayesian duality to a convex duality of Bayes' rule. Using this connection, we present a generalization of Amari's Bayesian duality and discuss its relevance for modern artificial intelligence.

---


### 533. [Nearly Tight Rademacher Bounds for Sparsely Activated Neural Networks](https://arxiv.org/abs/2609.09130)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li, Zhizhou Sha, Jiaojiao Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An input may activate few hidden units even when different inputs collectively use an entire network. We study the statistical complexity of this input-dependent sparsity in the one-hidden-layer ReLU model of Awasthi et al. (COLT 2024). For width $s$, at most $k$ active units per input, and effective weight and bias bounds $W,B$, every size-$m$ sample in the class's fixed radius-$R$ input domain satisfies $\mathcal{R}(S)\le CWR\min\{k,\sqrt{sk/m}\log^{3/2}(2m)\}+kB/\sqrt m$. A support-preserving cover and a single normalized chaining argument remove the previous explicit dimension factor, up to logarithms. Lower bounds on appropriate i.i.d. marginals match up to those logarithms, showing how changing active units across inputs retains a width dependence. The input domain matters: zero-bias networks sparse on the entire ball have at most $2k$ nonzero units and complexity $O(kWR/\sqrt m)$, whereas bias bounds comparable to $WR$ restore the worst-case rate on that same domain in only logarithmic dimension. A spherical-cap construction proves the latter claim without assuming sparsity merely on the sampling support. For a specified normalized bounded loss and biases comparable to $WR$, we also obtain agnostic minimax excess-risk bounds of order $\min\{1,\sqrt{s/(km)}\}$ up to logarithms.

---


### 534. [Entropy-Regularized Rank-Masked Policy Optimization for Test-Time Reinforcement Learning in Code Generation](https://arxiv.org/abs/2609.09135)

**<font color=#1a73e8>作者：</font>** Jiacheng Xu, Feng Chen, Xiuneng Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing methods for test-time reinforcement learning (TTRL) derive rewards from answer-level self-voting on unlabeled test-time tasks with canonical answers, but this breaks down for code generation because programs cannot be compared by surface form and therefore do not directly provide a usable training signal. To make TTRL applicable to code generation, we propose probe-driven TTRL, which constructs output-free probe inputs from the problem statement, executes candidate programs on these probes, and defines a Probe Consensus Reward (PCR) from the resulting behavioral agreement. PCR provides a behavioral training signal for open-vocabulary programs, but it is not a fully reliable verifier and remains susceptible to reward hacking through spurious consensus. We therefore introduce Entropy-Regularized Rank-Masked Policy Optimization (ERPO), which converts low PCR into conservative negative updates through rank masking and controls policy drift with an entropy ceiling. On coding benchmarks, ERPO substantially improves pass@1 and pass@k in both in-domain adaptation and zero-shot transfer.

---


### 535. [A Data-Driven Framework for Identifying and Prioritizing RPA Opportunities in Healthcare Processes](https://arxiv.org/abs/2609.09137)

**<font color=#1a73e8>作者：</font>** Maria Alejandra Gomez, Juan Manuel Castillo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robotic Process Automation (RPA) is widely used to reduce administrative burden in United States hospitals, yet an estimated 30-50% of RPA initiatives underperform because processes are selected informally, without a repeatable method to catalogue candidates, prioritize them, match each to an automation tier -- a Python bot, an open-source orchestrator such as n8n, or an enterprise platform such as UiPath -- and forecast financial return before committing resources. We propose a four-module, data-driven framework unifying these decisions: a Process Taxonomy of twenty recurring hospital processes across five value streams; a Prioritization module deriving an Automation Suitability Index from an Analytic Hierarchy Process matrix with an explicit consistency check; a Tool-Tier Selection module recommending the least-cost technology sufficient for a process complexity, integration, and compliance profile; and a Return-on-Investment module quantifying labor savings, error-cost avoidance, payback, and net present value. Applied to a synthetic portfolio spanning all twenty processes, plus a reference data-flow architecture linking it to hospital EHR/payer/ERP systems: 12 of 20 clear the prioritization threshold; the ranking is robust to +/-20% weight perturbation (Spearman correlation 0.83, top-5 set preserved 97.7%, 2,000 Monte Carlo trials); an Automation Risk Index flags four qualifying processes as Critical risk; a budget-constrained portfolio optimization shows diminishing marginal NPV as spend scales from $400K to $1.03M; and a second Monte Carlo analysis shows portfolio NPV stays positive at its 5th percentile. The framework is a conceptual synthesis of the literature rather than an instrument calibrated on primary hospital data; we discuss HIPAA governance and a research agenda for empirical validation. A supplementary Python implementation accompanies the paper.

---


### 536. [NOAH: Learning the Full Patient Journey. A Longitudinal Multimodal Time-Aware Model for Representation and Forecasting](https://arxiv.org/abs/2609.09140)

**<font color=#1a73e8>作者：</font>** Tobias Susetzky, Raphael Rehms, Dmitrii Seletkov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The digitization of healthcare has generated vast, longitudinal, and multimodal patient records over a lifetime, yet fully exploiting these data to represent and predict patient state trajectories remains a critical challenge. Current AI models often struggle to capture the complex, irregular temporal dynamics and inherent stochasticity of real-world multimodal patient data. Existing AI approaches for modeling longitudinal patient records are predominantly discriminative, limited to a few modalities, constrained by closed categorical vocabularies, treating time as a monotonic inductive bias, or they are limited in forecasting future patient states. We introduce NOAH, a time-aware, task-agnostic, generative transformer model representing and forecasting the full multimodal patient journey. NOAH features a novel bidirectional time integration and a variational latent space to capture the continuous evolution of patient states and the stochasticity of clinical trajectories. Built from over 559 million clinical events from 431,000 hospital visits of 299,000 patients across the MIMIC dataset family, NOAH natively processes medical images, time-series and numeric signals, categorical events, as well as structured and unstructured clinical records. NOAH is the first truly holistic generative model in its field, enabling autoregressive forecasting with optional time control, zero-shot classification, and counterfactual intervention simulation. It generates highly informative and predictive patient state representations that demonstrate strong performance in probing for clinical outcomes, 15 ICD chapters, and 29 comorbidities, as well as in time-to-event prediction. Seamlessly handling diverse modalities and complex temporal dynamics, NOAH provides a versatile, task-agnostic, scalable foundation for intelligent predictive systems in personalized clinical care and digital medicine.

---


### 537. [Studying Image Tokenizers as Visual Languages in Unified Multimodal Models](https://arxiv.org/abs/2609.09143)

**<font color=#1a73e8>作者：</font>** Siting Li, Zhengyang Wang, Simon Shaolei Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image tokenizers define the ``visual language'' of unified multimodal models, yet are commonly studied through isolated metrics or generation-/understanding-only evaluations. These evaluations do not fully capture how visual tokens behave when modeled jointly with text. We build a controlled pure-autoregressive testbed and track task-specific validation losses during multimodal continual pretraining across text, image, text-to-image (T2I), and image-to-text (I2T) prediction. We examine how these losses scale and relate to downstream performance, then use them to study multimodal learnability---how well image and text tokens are jointly modeled---and tokenizer design. We find that (1) losses should be analyzed by task, since they exhibit distinct scaling behavior and rank tokenizers differently. (2) The loss--performance relationship depends on the predicted token space: for a fixed tokenizer, T2I and I2T losses correlate with generation quality, but across tokenizers, the T2I loss--performance relationship shifts with the image-token space, whereas I2T loss, computed over a shared text vocabulary, provides a more consistent signal. I2T loss also correlates with both generation and visual understanding performance after supervised finetuning. Using losses as a lens, we show that (3) better reconstruction does not necessarily yield lower task-specific losses or stronger downstream performance, and that (4) image tokenizer choice can affect text modeling under joint optimization. As case studies, we revisit three tokenizer design axes---the discriminator, semantic supervision, and vocabulary size---to examine their effects on joint modeling and downstream performance. Together, our testbed offers a complementary perspective on image tokenizers as visual languages, highlighting their interplay with text in joint multimodal training.

---


### 538. [Point4D: Long-range 4D Motion Reconstruction](https://arxiv.org/abs/2609.09145)

**<font color=#1a73e8>作者：</font>** Minsik Jeon, Jay Karhade, Deva Ramanan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Point4D, a feed-forward model for 4D reconstruction of long-range video sequences. Point4D is able to reliably infer dense per-point 3D trajectories across multi-hundred-frame videos, unlike existing 4D methods that are limited to short input windows of at most a few dozen frames. A key innovation that enables this is our flexible 3D query-based motion decoder that decouples trajectory prediction from image-plane visibility. The predicted 3D endpoints are then directly re-queried in the next chunk without re-projection or matching. Furthermore, we show that extracting and reusing a visual descriptor from an arbitrary frame where the point is visible leads to better performance than relying solely on the source patch. Overall, Point4D achieves state-of-the-art performance across diverse long-video tracking benchmarks spanning over 200 frames and largely outperforms previous feed-forward 4D method. Project page: this https URL

---


### 539. [Copying explains the collective behavior of AI agents in the wild](https://arxiv.org/abs/2609.09150)

**<font color=#1a73e8>作者：</font>** Giordano De Marzo, Nicola Alboré, David Garcia  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In June 2026, thousands of AI agents found that a small public wiki would accept edits from inside their sandboxes, and started using it to help one another pass a timed test. Each agent lived for about an hour and remembered nothing afterwards. Nobody asked them to cooperate, and the wiki had not been built for them. The complete record of what they wrote is public, and it is unusually informative, because it preserves not only what each agent wrote but what that agent could see before writing. We use it to follow the three decisions an agent had to make on arrival: where to write, what to call itself, and how to word its message. One rule governs all three. An agent takes an option with a probability close to the share of that option in what it can see, and the share that matters is the one on the page in front of it, then the one in the stream of recent edits, and only weakly anything older. Three minimal copying models, one per decision and with a single free parameter each, reproduce the heavy-tailed distribution of how many agents met on a page, the frequency of the pieces from which the agents built their names, and the patchwork of pages that are internally consistent and different from one another. Copying whatever the environment happens to show is enough to produce most of the collective structure of this population. It is also what makes such a population easy to steer, since whoever writes first, or writes while the others are quiet, sets the convention for everyone who comes later.

---


### 540. [SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators](https://arxiv.org/abs/2609.09155)

**<font color=#1a73e8>作者：</font>** Yuncong Yang, Zhengtao Han, Furkan Ozyurt 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models are increasingly used as policy-in-the-loop imagination environments, where reliable rollouts require fine-grained controllability with respect to low-level robot actions. A key obstacle to scaling such models in robotics is that actions are not a universal language in pixel space: changes in visual environment, camera view, robot placement, or embodiment alter how the same numerical action manifests visually, leading to conflicting supervision under mixed training and brittle generalization at deployment. We introduce SyncWorld, an action-conditioned world model that serves as a zero-shot simulator across unseen environments without any additional training. SyncWorld leverages a visual calibration episode---paired frames and actions that showcase all the controllable degrees of freedom---to specify the setup-specific Action--Visual Mapping in context. Training with visual calibration contexts teaches the model to interpret actions through visual evidence and to leverage interaction history when explicit calibration is unavailable. Experiments show that SyncWorld can accurately simulate action outcomes in previously unseen settings, and that its capability of simulating rollouts enables test-time policy improvement without training.

---


### 541. [ReCite: Agentic Reasoning for Faithful Citation](https://arxiv.org/abs/2609.09156)

**<font color=#1a73e8>作者：</font>** Yuyang Huang, Bobo Li, Jiajia Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate citations are the foundation of academic writing, tracing intellectual origins and substantiating core claims. However, manually navigating the growing volume of scientific literature is increasingly difficult, prompting reliance on automatic citation recommendation. While modern retrieval-augmented architectures have largely mitigated the fabrication of non-existent papers, current systems relying on semantic similarity struggle with misattribution, often citing authentic papers that fail to logically support the author's claim. To address this challenge, we argue that accurate citation requires a shift from similarity-based search to active, claim-level reasoning. We propose ReCite, a decoupled agentic framework that orchestrates location perception, intent-aware query planning, and reflective verification. Trained on synthesized reasoning trajectories, our agent verifies claim-evidence consistency and triggers self-correction loops when retrieved candidates lack logical support. Experiments demonstrate that our lightweight framework outperforms state-of-the-art massive generative models in strict citation accuracy. By grounding literature matching in verifiable logic rather than semantic overlap, ReCite establishes a reliable foundation for automated academic writing.

---


### 542. [Learning Length-Extrapolatable Recurrent Models](https://arxiv.org/abs/2609.09157)

**<font color=#1a73e8>作者：</font>** Hanwen Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent models provide a natural path to long-context modeling, yet models trained with backpropagation through time (BPTT) often fail beyond their training horizon. Classical analyses emphasize gradients that vanish or explode along temporal paths. However, dense per-token losses can still train a shared recurrent rule despite severe decay, showing that decay alone does not determine whether learning fails. We instead study state credit: the signal through which future losses reach earlier recurrent states before contributing to parameter updates. Accordingly, we intervene directly on state credit and propose Credit Stabilization through Time (CST). During backward propagation, CST locally rescales the state-credit signal to stabilize its norm without rotating the component being corrected, while leaving the forward computation unchanged. Because controlled synthetic tasks and real data exhibit different credit dynamics, we specialize CST to each regime. In both settings, CST improves performance beyond the training horizon, with gains observed at up to 128x the training length.

---


> [!TIP]
> 当前位于：**501-542**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-542**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
