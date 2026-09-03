# 📦 其他研究 | 2026年09月04日

> 本类共 **187** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-187**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-187**

---

### 151. [Source Distribution Estimation by Posterior Averaging](https://arxiv.org/abs/2609.02622)

**<font color=#1a73e8>作者：</font>** Trung-Dung Hoang, Lisa M. Koch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulation-based science often requires a distribution over simulator parameters whose push-forward reproduces a set of real observations: this is the source distribution estimation (SDE) problem. Existing methods fit the source against a likelihood surrogate trained once from a fixed proposal prior. Their objective is therefore stated only in terms of the surrogate instead of the true simulator, which may fail for inaccurate areas in parameter space where the surrogate was never trained. We instead solve SDE by expectation maximization: an E-step trains an amortized posterior on fresh simulations from the current source estimate, and an M-step refits the source to the average of that posterior over the observed data. We give two parameterizations, (1) separate source and posterior flows and (2) a single shared conditional flow. We evaluate our method on three benchmark tasks under both broad and misspecified initial priors. Both improve on existing fixed surrogate approaches and on iterated variants of each, most clearly on Lotka--Volterra, where no baseline falls below 0.96 data-space C2ST while our methods reach 0.64-0.68 in three of four initial-prior settings.

---


### 152. [Oracle, will I ever learn? A study of prediction convergence and complementarity across link prediction models](https://arxiv.org/abs/2609.02638)

**<font color=#1a73e8>作者：</font>** Guillaume Méroué, Fabien Gandon, Pierre Monnin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs have become an important source of structured knowledge for Web applications, including search, question answering, and recommender systems. In these applications, link prediction can serve either as a prediction task itself or as a means to enrich incomplete knowledge graphs for downstream tasks. Interestingly, different link prediction models, or even different training runs of the same model, can produce substantially different predictions for the same query. This suggests a variability in the capture of the underlying knowledge by models, thus raising a fundamental question: to what extent do different models capture complementary knowledge, and how much of this knowledge could be recovered by combining them? We propose to measure model complementarity through the performance of an oracle that, for each query, selects the best prediction among a considered set of models, hence providing an upper bound on the performance achievable through model combination. Across several architectures and benchmarks, we find a substantial gap between individual models and their oracle, revealing that different models capture complementary knowledge. Yet, this complementarity rapidly saturates as more models are added, leaving a persistent subset of queries unsolved even by a large number of models. These findings reveal both the potential of model complementarity and a fundamental limit to what current link prediction models can collectively recover; thereby highlighting the need for further research to build robust Web applications.

---


### 153. [TaRA: Training-Aware Low-Rank Adaptation Initialization](https://arxiv.org/abs/2609.02639)

**<font color=#1a73e8>作者：</font>** Taehyeon Kim, Eunhyeok Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) has become a de facto standard for parameter-efficient fine-tuning (PEFT), yet its performance is highly sensitive to initialization due to the information bottleneck imposed by low-rank decomposition. Existing approaches attempt to construct high-quality LoRA initializations by exploiting principal components of pretrained weights, activations, or gradients. However, these methods do not directly account for the training dynamics of the full-rank model. In this paper, we propose Training-aware Low-Rank Adaptation Initialization (TaRA), a method that initializes LoRA such that the gradients induced by the low-rank factors closely approximate the gradient of the corresponding full-rank weight matrix. Derived from a mathematical formulation, TaRA improves gradient fidelity at the start of training while introducing negligible computational overhead. Across diverse and challenging fine-tuning tasks, TaRA consistently outperforms prior state-of-the-art methods, establishing a simple, robust, and scalable solution for effective LoRA initialization.

---


### 154. [From Detection to Localization: A Unified Forensics Framework for Fully Synthetic and Tampered Images](https://arxiv.org/abs/2609.02640)

**<font color=#1a73e8>作者：</font>** Annalisa Gallina, Marco Fiorucci, Marco Brigo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative models has significantly worsened the problem of manipulated image detection, as these methods are capable of producing highly realistic forgeries, reinforcing the importance of multimedia forensics. Conventional approaches typically frame image manipulation detection as a binary classification task (real vs. generated), which limits the capability to distinguish and localize different forms of manipulation. To address these constraints, this work extends an existing detector by introducing a unified multiclass framework (real vs. fully generated vs. tampered). In addition to classifying image authenticity, the framework incorporates a segmentation branch to enable pixel-level localization of tampered regions. The proposed approach outperforms selected recent benchmarks, offering an efficient solution with improved classification accuracy and higher IoU scores for the localization task. Find the code at this https URL.

---


### 155. [Learning to Attract and Repel: Dual Quality Margin Learning for Face Recognition (DQM-Face)](https://arxiv.org/abs/2609.02644)

**<font color=#1a73e8>作者：</font>** El Ouanas Belabbaci, Bhavesh Wani, Philipp Terhörst  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition in unconstrained environments remains highly challenging due to diverse and extreme variations encountered in real-world scenarios. To mitigate these effects, existing margin-based approaches model sample quality through feature magnitude. However, magnitude-based modeling alone is susceptible to identity-agnostic noise, which can degrade the reliability and discriminative power of learned representations. In this paper, we propose Dual Quality Margin Learning for Face Recognition (DQM-Face), a novel framework that enables refined attraction and repulsion dynamics during representation learning. Our approach unifies conventional magnitude-based quality estimation with a newly introduced semantic quality learning mechanism, realized via squeeze-and-excitation semantic attention. By jointly leveraging magnitude and semantic cues, we construct enhanced quality-aware margins that adaptively strengthen intra-class compactness through improved attraction during learning. To further enhance inter-class discrimination, we introduce a repulsion margin formulation that explicitly enlarges inter-class separation. The unified integration of semantic quality modeling with dual attraction-repulsion margin optimization results in a more structured and discriminative feature geometry. Extensive experiments on multiple challenging benchmarks demonstrate that DQM-Face consistently outperforms state-of-the-art face recognition methods. Moreover, we show that the quality learned for margin optimization is highly effective for face image quality assessment within the proposed framework, demonstrating that the learned quality signal is intrinsically aligned with the recognition objective. The code is publicly available: this https URL

---


### 156. [Differentiable Electricity-Market Clearing for Gradient-Based Planning](https://arxiv.org/abs/2609.02646)

**<font color=#1a73e8>作者：</font>** Luca Mungo, Maarten P. Scholl, Arnau Quera-Bofarull  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Planning a large data center is difficult because a facility big enough to matter changes the electricity prices it will pay. Those prices are set by market clearing, a constrained optimization problem solved anew in every operating condition. However, simulating the market tells a planner how a candidate plan performs but not how to improve it. Here we treat market clearing as a differentiable optimization layer: each forward pass solves the market, and reverse-mode automatic differentiation propagates the planning cost back through the cleared prices to the plan. After validating these gradients against finite differences, we apply them to a concrete problem: allocating 50 MW of data-center load across six candidate buses in two synthetic networks, under a fixed cost per active site, evaluated over 36 operating states. Judged against exhaustive enumeration of all site combinations, gradient optimization recovers the continuous allocations almost exactly, with worst-case objective gaps of 2.3\% and 8.5\% of the cost difference between the best and worst single site. Its one systematic error is instructive: near the costs at which a site should close, the smooth relaxation of the discrete site count shrinks the site rather than closing it, so discrete transitions arrive late. Differentiable market clearing thus turns market-aware planning into a problem gradients can search.

---


### 157. [PrimSynth: An Agentic Approach to Discover, Validate, and Synthesize Exploit Primitives for Linux Kernel Vulnerabilities](https://arxiv.org/abs/2609.02647)

**<font color=#1a73e8>作者：</font>** Pengfei Wang, Anying Chen, Danjun Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Linux kernel vulnerabilities are critical to downstream systems. Despite extensive research on automated kernel exploitation, a fundamental challenge remains the conceptual gap between abstract exploit strategies and concrete technical operations. To fill this gap, this paper introduces a systematic characterization that formalizes six classes of exploit primitives from logical capability to validatable effect. Then, an extended exploit strategy representation is proposed, which couples primitive upgrading strategies with primitive path code synthesis rules governing object constraints, temporal sequencing, environment prerequisites, and validation constraints. Building upon this foundation, this paper presents \textsc{PrimSynth}, a multi-agent framework that encapsulates these representations through coordinated agents to discover, validate, and synthesize exploit primitives for memory corruption vulnerabilities in the Linux kernel. These agents operate in an iterative closed loop until valid primitives are found, leveraging validation signals as evidence of exploitable state transitions to ground primitive synthesis decisions. An automated method for extracting and validating primitives is also proposed based on vulnerability-directed execution and a rebootable validation environment. \textsc{PrimSynth} is evaluated on 16 real-world Linux kernel CVEs spanning 5 vulnerability types. Experimental results show that PrimSynth achieves reliable primitive extraction, maintaining a 100% primitive match rate. For primitive synthesis, PrimSynth successfully synthesizes multi-primitive exploitation chains with 82.4% strategy synthesis rate (SSR) when the public PoC is available and a 61.3% SSR without the guidance of primitive hypotheses.

---


### 158. [Physics-Driven Independent Pair Generation for Iterative Self-Supervised Low-Dose CT Denoising](https://arxiv.org/abs/2609.02654)

**<font color=#1a73e8>作者：</font>** Xianlei Han, Shaoyu Wang, Jiancheng Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-dose computed tomography (LDCT) measurements contain mixed Poisson-Gaussian noise. However, most self-supervised methods rely on generic image statistics and do not explicitly model this noise, which may limit their ability to effectively suppress realistic LDCT noise. To address this issue, we propose a physics-driven framework with cross-domain iteration for self-supervised LDCT denoising. The proposed framework proceeds in three main steps. First, a learned sinogram prior and the LDCT noise model guide posterior inference of photon counts, enabling separation of the Poisson and Gaussian components. Second, the separated Poisson and Gaussian components are respectively processed by binomial thinning and Gaussian data thinning to construct two branches, and residual scaling matches each branch's noise level to that of the observation, yielding a training pair with approximately independent noise realizations from one low-dose measurement. Finally, the pair is used to train an image-domain network whose forward-projected outputs update the prior. Through cross-domain iteration, the prior and the training pair are progressively refined while maintaining consistency with CT acquisition physics. Experiments on simulated data from AAPM, LIDC-IDRI, and LoDoPaB-CT and on real LDCT data show consistent gains over the evaluated self-supervised baselines across dose levels, with performance comparable to the evaluated supervised baseline.

---


### 159. [oHC: Orthogonal Hyper-Connections on SO(4) via Quaternions](https://arxiv.org/abs/2609.02672)

**<font color=#1a73e8>作者：</font>** Haoqiang Guo, Xuyi Chen, Bo Ke 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hyper-Connections (HC) replace the single residual stream of a Transformer with $n$ parallel ones, mixing them at every layer with a learned $n \times n$ residual matrix. Leaving that matrix unconstrained places no limit on the factor by which the mixing step rescales the residual streams, and that factor compounds across layers, which destabilizes training. Manifold-constrained Hyper-Connections (mHC) address this by restricting the matrix to the doubly stochastic matrices. That caps the factor at one, so the mixing can no longer amplify any direction, but nothing bounds it from below. We prove that inside this set the mixing step can reduce the norm of the residual streams only by shrinking the differences between the streams, while their mean is left unchanged; and since the reduction accumulates over layers, the streams grow more alike and their diversity is spent with depth. We therefore propose Orthogonal Hyper-Connections (oHC), restricting the residual matrix to the rotation group $SO(n)$, so that the mixing step can neither amplify nor attenuate the residual streams in any direction, which keeps training stable and no longer forces the differences between the streams to contract. Specifically, at the four streams used by recent HC models we parameterize the group in closed form by a pair of unit quaternions, which adds no parameters, replaces the iterative projection with a fixed pattern of signed additions, and can be constructed faster than mHC. We evaluate oHC across a comprehensive set of downstream tasks, where it outperforms the single-stream residual baseline, mHC and iHC, which fixes the residual matrix to the identity.

---


### 160. [Genesis: A Generative Engine for Hierarchical Satellite Image Synthesis](https://arxiv.org/abs/2609.02683)

**<font color=#1a73e8>作者：</font>** Subash Khanal, Yangzhi Cui, Daniel Cher 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth observation is fundamentally multi-scale; geospatial tasks span varied resolutions, and satellite imagery is organized into cascading tile pyramids that nest fine detail within wide coverage. Current generative models of satellite imagery, however, operate along a single axis: they either zoom to enhance a single tile's resolution or pan to extend imagery at a fixed scale. As a result, no existing method produces a complete pyramid that stays consistent across both scale and space, where a high-zoom tile must agree with the coarse context it refines and with the neighbors it meets. Motivated by this gap, we introduce a new task, multi-scale tile completion: given a sparse set of seed tiles at arbitrary zoom levels and positions, synthesize a complete, uniform quadtree that is globally consistent across both scale and space. We approach this task with Genesis, a generative engine that brings both axes together by composing two specialized operators over the quadtree: a vertical super-resolution model and a horizontal mask-based outpainting model, producing pyramids that are consistent across zoom levels and seamless across neighboring tiles. Each operator achieves state-of-the-art results on its subtask, and the engine propagates sparse seeds into seamless, multi-resolution maps from any initial configuration. To evaluate the task and benchmark Genesis, we introduce dense500, a fully observed multi-scale pyramid dataset spanning diverse geographic regions, together with a suite of pyramid-level metrics. Code, models, and our dataset are available at this https URL.

---


### 161. [H3DNAS: Hardware-Aware ONNX-Native 3D Point Cloud Model Compression](https://arxiv.org/abs/2609.02684)

**<font color=#1a73e8>作者：</font>** Anchit Mulye, Rhythm Baghel, Sujay Kumar Ingle 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying 3D point cloud models on edge hardware such as the NVIDIA Jetson Orin Nano is severely constrained by compute and memory budgets. Existing compression methods require access to the model's original source code, rendering them inapplicable to the Open Neural Network Exchange (ONNX) binaries commonly distributed by vendors and model repositories. We present \textbf{H3DNAS}, a hardware-aware model compression framework that operates directly on ONNX computational graphs without requiring original source code, architecture class definition, or gradient access during search. H3DNAS makes three contributions: (1) a \textbf{Channel Dependency Graph (CDG)} that classifies ONNX operators into four constraint classes and formally establishes that the free parameter fraction $\rho_f$ is topological invariant, a provable compression ceiling computable in $\mathcal{O}(|V|+|E|)$; (2) a \textbf{Two-Stage Hierarchical Search} that prunes candidate architectures by $L_1$-importance channel selection, ranks them by output fidelity as a zero-shot label-free proxy, and applies GhostConv structural mutation to Pareto-optimal candidates; and (3) the \textbf{first source-code-free compression pipeline for 3D point cloud models}, operating entirely via ONNX graph surgery with no original architecture definition required. On ModelNet40, H3DNAS reduces the number of parameters in PointNet, PointNet++, and PointMLP by $65.5\%$, $43.2\%$, and $49.1\%$, respectively, while achieving $1.99\times$, $1.29\times$, and $1.67\times$ inference speedups with negligible loss in accuracy. The source code is publicly available\footnote{this https URL}.

---


### 162. [GaLe: memory-efficient Global Approximate and Local Exact features](https://arxiv.org/abs/2609.02689)

**<font color=#1a73e8>作者：</font>** Alberto Ancilotto, Elisabetta Farella  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embedded devices typically lack the resources of GPU-equipped machines, and existing inference methods suffer from either high computational overhead (patch-based) or accuracy loss (approximation-based). We propose GaLe, a memory-efficient technique that enables the deployment of pretrained networks on constrained devices without retraining. GaLe partitions feature maps into two components: a local exact (Le) representation that preserves fine details and a global approximate (Ga) representation that retains long-range dependencies. Unlike standard tiling, GaLe supports global operations and attention mechanisms found in hybrid CNN-transformer models. Validated on ImageNet, our method matches exact-inference performance while achieving up to 65% speedup and 90% RAM reduction on a Cortex-M33 compared to patch-based inference. We further demonstrate GaLe's versatility across classification, detection, and generation tasks, highlighting its potential as a foundation for resource-efficient architecture design.

---


### 163. [Generating Medical Image Counterfactuals using Causal Explanations](https://arxiv.org/abs/2609.02697)

**<font color=#1a73e8>作者：</font>** David A. Kelly, Tom Yaacov, Nathan Blake 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models have achieved impressive performance in medical image diagnosis, yet their deployment in clinical settings remains constrained by limited explainability. Counterfactual images provide one means of auditing model behavior by showing how an image would need to change for a classifier to produce a different prediction. Existing approaches typically generate such explanations using auxiliary models, including generative adversarial networks and diffusion models. While often capable of producing visually realistic images, these methods explain one black-box model using another, making it difficult to separate the classifier's decision-making process from the inductive biases of the generator.
We propose a novel counterfactual-generation framework that requires no generative model. Instead, counterfactuals are constructed directly from causal evidence extracted from the classifier. The resulting approach is deterministic, requires no additional model training, and enables controllable edits within user-specified regions of interest. Experiments on real-world medical imaging datasets demonstrate that the proposed method successfully changes classifier predictions while remaining closer to the original image than generative baselines, providing a more direct and transparent view of the classifier's decision boundary.

---


### 164. [The PIONEER Project: A PrIvacy companion for mOtivatioN and knowlEdge transfER](https://arxiv.org/abs/2609.02700)

**<font color=#1a73e8>作者：</font>** Simon Althaus, Nina Gerber, Sara Hahn 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Remaining control over their private data is one of the key challenges in this century for users. We know from prior work that users are often neither in a position to fully grasp the content of the usually complicated texts, nor are they motivated to spend the time necessary to do so. We report on the progress made by the PIONEER project on a privacy support tool that combines knowledge transfer and persuasive elements to increase users' privacy awareness and motivation; thus empowering them to more privacy sovereignty. Throughout the research and design process, we consider user group specifics that may result in different requirements, e.g., for children, adolescents, parents, or elderly people. We further target sustainable behavior change by addressing different states of change, precisely: spark initial motivation, facilitate the creation of new habits, and encourage habituation of these habits in the long term (volition). Finally, we provide a privacy support tool demonstrator that can be utilized for research and education purposes, e.g., in school contexts.

---


### 165. [A Top-Down Framework for Metric-Scale Athlete Localization from Single Broadcast Frames](https://arxiv.org/abs/2609.02705)

**<font color=#1a73e8>作者：</font>** Thanh-Khoi Nguyen, Hoang-Phuc Nguyen, Linh-Huynh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate world-coordinate localization of athletes from single-frame broadcast footage is inherently challenging due to extreme scale disparities in ultra-high-resolution imagery. In this paper, we propose a top-down framework for metric-scale athlete localization from a single calibrated frame. Our approach centers on three key contributions. First, we propose Boundary-Aware Adaptive Tiling, a semantics-guided extension of standard sliced inference. By iteratively expanding tile boundaries based on coarse bounding-box predictions, it systematically ensures full object containment, effectively mitigating boundary-splitting artifacts through a lightweight pipeline adaptation without architectural modifications. By substantially mitigating recall degradation under extreme scale variance, Boundary-Aware Adaptive Tiling enables us to isolate perspective distortion as the primary source of residual localization error. Second, we adapt the RTMPose-X architecture into a specialized two-keypoint estimator (pelvis and ground projection), employing a reformulated Gated Attention Unit optimized for this geometrically coupled point pair, and then deterministically lift the 2D ground projections into world coordinates via camera-calibrated ray casting. On the public test set, our method achieves a LocSim score of 97.44 and an mAP of 0.9128, outperforming the baseline by over 21 \% and establishing a robust solution for high-resolution scale variance.

---


### 166. [Card-Based Computation in the Virtual Player Simulation Model](https://arxiv.org/abs/2609.02716)

**<font color=#1a73e8>作者：</font>** Suthee Ruangwises  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Player simulation has recently emerged as a new direction in card-based cryptography, with protocols developed for simulating virtual players in physical card games such as Old Maid, UNO, and President. Unlike conventional card-based secure computation, player simulation imposes additional constraints: the cards represent a persistent game state, the remaining cards in a virtual player's hand must be preserved after each action, and it is desirable to represent each card in the game by a single physical card. In this paper, we study generic card-based computation in the virtual player simulation model. We focus on games whose cards admit a publicly known ranking and propose two fundamental protocols. First, we present the Play-Minimum protocol, which securely selects and plays the minimum-value card from a virtual player's hand when all cards in the deck have distinct values. By symmetry, the protocol can also be used to play the maximum-value card. Second, we present the Sorting protocol, which securely arranges a virtual player's hand in nondecreasing order and remains applicable when multiple cards have the same value. These protocols provide generic computational primitives independent of any particular card game and constitute a step toward understanding the computational capabilities of the virtual player simulation model.

---


### 167. [MV-dVRK: A Multi-Viewpoint Benchmark for Spatial Surgical Perception](https://arxiv.org/abs/2609.02717)

**<font color=#1a73e8>作者：</font>** Guido Caccianiga, Sergey Prokudin, Yutong Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale training and refined optimization techniques have greatly improved sparse multi-view 3D reconstruction. Despite their relevance to surgery, such methods have never before been rigorously evaluated on real endoscopic images. Current clinical telerobots deploy a single stereo camera inside the patient, making multi-viewpoint data extremely rare. This paper presents MV-dVRK, the first ex-vivo surgical dataset to combine multiple exposure-synchronized stereo viewpoints with accurate surface geometry and camera poses. The static subset of the benchmark provides dense SfM reference geometry, validated against an industrial 3D scanner, together with ground-truth camera poses and sparse-view test sets. We use MV-dVRK to systematically compare zero-shot monocular, stereo, multi-stereo, and multi-view 3D reconstruction methods as the number of viewpoints increases. With two endoscopes, multi-stereo reconstruction achieves the highest coverage. With a third viewpoint, optimization-based multi-view methods perform best, covering 67% of ground-truth surface points within a 1 mm tolerance and recovering highly accurate relative camera poses. By contrast, feed-forward foundation models cover only 43% of the ground-truth surface in the same setting. MV-dVRK also includes ten dynamic sequences spanning multiple surgical tasks, with increasing kinematic complexity and tissue deformation, providing a basis for future research in multi-viewpoint surgical perception. The project is available at: this https URL.

---


### 168. [SPADE: SPaT Attack Detection from the Connected Vehicle's Perspective](https://arxiv.org/abs/2609.02741)

**<font color=#1a73e8>作者：</font>** James Di Novo, Hany Ragab, Sylvain P. Leblanc  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Signal Phase and Timing (SPaT) messages are a cornerstone of connected vehicle (CV) safety, enabling CVs to perceive and respond to intersection state through Vehicle-to-Infrastructure (V2I) and Vehicle-to-Vehicle (V2V) communication. The integrity of these messages is threatened by a range of application-layer attacks that can bypass conventional authentication when a roadside unit or peer vehicle is compromised. Existing intrusion detection research either defends the infrastructure side or targets V2V Basic Safety Message (BSM) / Cooperative Awareness Message (CAM) misbehavior, leaving the onboard CV perspective on SPaT integrity this http URL close this gap, we introduce SPADE --- the SPaT Attack Detection and Evaluation dataset --- a labelled, multi-modal, simulation-based dataset designed specifically for deep learning IDS research in this space. SPADE is generated through Eclipse MOSAIC using runtime attack injection at the SAE J2735 application layer across six attack classes and one benign class. By combining four intersection geometries, six operating conditions, and five independent random-seed repetitions, SPADE comprises 180 unique base scenario runs, yielding $\sim$1,890,000 labelled timestep records (270,000 per class). Each record fuses SPaT message fields, onboard camera confidence scores, and cooperative V2V peer data across 40 features, reflecting the multi-modal signal space required to distinguish deliberate attacks from environmental degradation. The dataset, generation code, and scenario configurations are released publicly to support reproducible and comparative IDS research in C-V2X security. The developed toolbox, instructions, and dataset link are publicly available on GitHub: this https URL.

---


### 169. [InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling](https://arxiv.org/abs/2609.02747)

**<font color=#1a73e8>作者：</font>** Tianheng Lu, Guangyu Wang, Ruqi Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving truly immersive large-scale scene digitization necessitates consistent and visually pleasing rendering across all possible viewing perspectives. However, collecting multi-view images covering every fine detail of a large-scale scene is prohibitive due to scene complexity, capture cost, negligence, or accessibility constraints. As a result, the sampled views tend to be highly unstructured -- the majority of the scene is well covered yet certain regions inevitably lack sufficient observations. Existing reconstruction based methods are vulnerable to view scarcity while generation based approaches suffer from generalization, controllability, and 3D consistency issues. To address this challenge, we propose InceptionGS, which bootstraps Gaussian splatting by subtly balancing reconstruction and generation. Starting from an initial Gaussian splatting, InceptionGS reasonably rethinks and repairs problematic regions caused by view scarcity while preserving the quality elsewhere, by softly incorporating scene- and view-adaptive generative priors. Extensive experiments on real-world large-scale scenes demonstrate the superiority and broad applicability of our approach in handling unstructured imagery and boosting high-fidelity Gaussian splatting. Please refer to the supplementary video for better visual demonstrations.

---


### 170. [Balancing Frequencies and Pixels in Flow Matching](https://arxiv.org/abs/2609.02748)

**<font color=#1a73e8>作者：</font>** Lucas Degeorge, Paul Couairon, Arijit Ghosh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural images follow a $1/f^2$ spectral distribution: most signal energy lies in the low spatial frequencies, while the perceptually important structures such as textures and edges occupy sparse high-frequency bands. Pixel-space reconstruction objectives, however, treat all spatial errors uniformly, causing low frequencies to dominate the optimization signal and delaying the learning of fine-scale details. In this work, we identify this objective-level spectral imbalance as a key inefficiency in training pixel-space flow models. To address it, we propose a Focal Log-Frequency Loss (f-loss), a spectrally balanced objective that equalizes the learning signal across frequencies, emphasizing high-frequency components that are otherwise underrepresented in pixel-space objectives. Building on this, we introduce a simple training strategy that combines frequency and pixel supervision: we first emphasize frequency-domain learning early to capture all frequencies, and then transition to standard pixel-space v-loss for spatial refinement. This balancing mitigates the low-frequency bias of pixel losses and aligns the training signal with the evolving needs of the model. Our approach is conceptually simple, requires no architectural changes, and acts as a drop-in replacement for flow matching losses. Across multiple model scales, it accelerates convergence by up to 40% while consistently improving FID and perceptual fidelity. We will release code and models.

---


### 171. [Measurement-Driven Sub-Network Selection for On-Premise Retrieval-Augmented Factory Agents](https://arxiv.org/abs/2609.02760)

**<font color=#1a73e8>作者：</font>** Vasileios Rizeakos, Georgios Paisios, Alexandros Machairas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-premise assistants can give factory workers conversational access to machine documentation, but models capable of the task rarely fit shop-floor hardware. We show that after structural compression and retrieval-grounded adaptation, model size is no longer a reliable predictor of adapted answer quality: general capability falls almost linearly with parameter count, while judged retrieval-augmented answer quality does not. We therefore treat deployment as a post-adaptation selection problem, committing one sub-network per device on judged answer quality and measured on-device throughput under a configurable general-capability floor and memory budget; rules that optimize size, speed, or quality alone each give up capability or throughput. A weight-shared supernetwork trained with sandwich-style in-place distillation keeps this selection inexpensive. In a manufacturing-manual case study, extraction costs 13.7 percent of the unpruned model's judged quality and retrieval-grounded distillation returns it to within 4.6 percent, recovering two thirds of the loss, and the same assistant runs across three heterogeneous edge tiers at 1.3 to 5 watts standby.

---


### 172. [CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation](https://arxiv.org/abs/2609.02774)

**<font color=#1a73e8>作者：</font>** Varun Gadey, Ziad Marey, Alexandra Dmitrienko  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Code Generation (RACG) improves LLM-based software development by retrieving external code artifacts, documentation, and patches, and incorporating them into the generation context. This reliance on external knowledge introduces a critical trust boundary: poisoned artifacts can influence generated code without modifying the underlying LLM. Prior work shows that selecting existing vulnerable examples can increase the general vulnerability rate of RACG outputs, but leaves open whether a black-box attacker can construct a single task-matched artifact that propagates an attacker-selected weakness. We introduce CodePoisonRAG, a targeted upstream knowledge-poisoning framework that transforms benign fixed-code entries into poisoned artifacts. Its attack chain combines CWE-specific Vulnerability Injection, which embeds a selected source-to-sink flow while retaining task alignment, with Semantic Mislabeling, which adds false safety claims without repairing the vulnerable behavior. The attacker has no access to the victim's deployed knowledge base, retriever, re-ranker, generator, prompt, or defense mechanism and injects at most one artifact per anticipated programming task. We construct 85 poisoned artifacts covering ten CWE classes across Java and C, yielding an aggregate corpus-poisoning ratio of 0.7%. Across three generators, all 85 artifacts appear among the Top-3 results for their corresponding queries, and CodePoisonRAG achieves attack success rates between 0.80 and 0.93. Against CodeGuarder, which injects vulnerability-specific security knowledge into the generation context, the attack retains success rates between 0.40 and 0.71. These results show that RACG poisoning extends beyond the incidental propagation of existing vulnerabilities to the targeted construction and propagation of attacker-selected weaknesses.

---


### 173. [Video-Based Palm-Vein Authentication under Challenging Conditions](https://arxiv.org/abs/2609.02776)

**<font color=#1a73e8>作者：</font>** Xiaofeng Yan, Kechen Liu, Abhilash Venkatesh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Palm-vein biometrics are increasingly used for secure, contactless authentication. Yet real-world deployment exposes them to surface noise (sweat, dirt), illumination and motion variation, and temperature-driven changes in vascular visibility, which remain underexplored for lack of data captured under such conditions. To study these effects, we introduce the Columbia University Palm-vein (CUP) dataset, to our knowledge the first public video-based palm-vein dataset. CUP records every palm under four surface conditions (a clean baseline, warm, wet, and dirty) and pairs each subject with physiological and demographic metadata. On it we benchmark twenty-one recognizers spanning static, video, and multi-frame aggregation architectures. Models that verify reliably on clean palms lose most of their accuracy on dirty ones, and the mean equal error rate (EER) roughly quadruples. We recover much of that robustness along both axes of the capture. Temporally, a consensus over the few frames the sensor already returns cancels transient corruption; spatially, a test-time matcher that adds no learned parameters fuses the global cosine with a saliency-steered region-level optimal transport that routes the comparison around corrupted regions. The full design leads on every surface of CUP in EER, TAR@FAR=0.01, and Rank-1, at 4.3M parameters and 3.1 GFLOPs, a fraction of the video models' cost. Attached to four frozen state-of-the-art backbones it cuts their mean EER by 29-37% without retraining, and on four public single-image datasets the regional matching alone still helps. A preliminary audit across ten demographic and physiological traits finds two warm-condition gaps, along body water and gender, that survive multiple-comparison correction. CUP will be released for non-commercial research use at this https URL upon publication.

---


### 174. [AutoCompass: Accurate Visual Localization on Public Maps by Learning from Weak Labels](https://arxiv.org/abs/2609.02798)

**<font color=#1a73e8>作者：</font>** Javier Tirado-Garín, Alan Savio Paul, Shuai Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural map matchers estimate an image's 3-DoF pose relative to a 2D map. These models are trained on large-scale datasets of geo-referenced images, whose position and heading labels often contain noise that affects the trained models. To address this, we present AutoCompass, a supervision approach for training neural map matchers from inaccurate absolute pose labels. First, we show that heading labels are unnecessary: trained from raw GPS labels, models learn to predict accurate headings, automatically. Second, defining a tolerance region around raw GPS improves positional accuracy. Third, if available, our supervision uses relative poses between training images, obtained via SLAM or SfM, which provide a more accurate training signal. Across driving and egocentric benchmarks, AutoCompass consistently outperforms counterparts trained with the usual strong reliance on absolute pose labels.

---


### 175. [GDB-Reward: From Evaluation Metrics to Training Rewards for Graphic Design](https://arxiv.org/abs/2609.02813)

**<font color=#1a73e8>作者：</font>** Adrienne Deganutti, Purvanshi Mehta, Simon Hadfield 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models excel at natural image synthesis but struggle with graphic design, where success depends on satisfying precise constraints on typography, layout, color, and visual communication. While prompt optimization offers an attractive alternative to expensive diffusion model fine-tuning, learning prompts for frozen image generators requires informative reward functions despite the entirely non-differentiable generation process. Reinforcement learning does not require differentiable objectives; it requires only scalar rewards capable of ranking candidate outputs. This raises a simple question: can design evaluation metrics themselves become reinforcement learning rewards? Our central contribution is GDB-Reward, a framework that systematically transforms heterogeneous graphic design evaluation metrics into a unified reinforcement learning reward. Experiments demonstrate that GDB-Reward provides an effective optimization objective, substantially improving adherence to the design specification in perceptual quality, rendering fidelity, and spatial accuracy while keeping the image generator entirely frozen. More broadly, our results demonstrate that heterogeneous, non-differentiable evaluation metrics can move beyond passive benchmarking to become effective optimization objectives for reinforcement learning in domains where differentiable supervision is unavailable.

---


### 176. [AI Contextual Measurement for Recovering Individual and Group-Level Effects: Validation Against Survey Measures and an Occupational Application](https://arxiv.org/abs/2609.02821)

**<font color=#1a73e8>作者：</font>** Wenxin Jiang, Xuyang Wang, Yuxiao Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Researchers increasingly use artificial intelligence to construct measures of social, organizational, and occupational characteristics that are absent from conventional surveys. We propose AICOME, AI COntextual MEasurement, a framework for evaluating whether AI-derived respondent-level measures can recover individual and group-level effects in contextual models. The key idea is that an AI measure constructed at the respondent level can be used to derive its group-level aggregate and its individual deviation, allowing researchers to estimate both between-group and within-group associations rather than treating AI measurement as response prediction alone.
We validate the framework using the 2022 China Family Panel Studies (CFPS), where occupations provide the empirical grouping structure and several job-related survey variables provide validation benchmarks. For computer use, foreign-language use, weekly hours, and management responsibilities, we compare survey measures with AI-derived measures in response-level, model-level, contextual, and boundary-condition validations. The results show that AI contextual measurement can recover much of the contextual-model information contained in observed survey variables when rich respondent and job characteristics are available. Weekly hours provides the strongest validation case, with AI-derived measures reproducing the large negative between- and within-occupation associations with satisfaction observed in CFPS. The framework also identifies clear boundary conditions: performance deteriorates when information is restricted to occupation and basic demographics, and recovery is weaker when several related concepts are treated as simultaneously unobserved. The findings suggest that AICOME is most useful for recovering a limited number of theoretically important constructs from rich existing datasets.

---


### 177. [Benchmarking RAW and RGB Restoration in Image Signal Processors](https://arxiv.org/abs/2609.02831)

**<font color=#1a73e8>作者：</font>** Zihao Lu, Radu Timofte, Marcos V. Conde  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern cameras transform RAW sensor measurements into sRGB images through an image signal processor (ISP). We benchmark two placements for blind restoration around a fixed ISP: (A) pre-ISP restoration in the RAW domain and (B) post-ISP restoration in the sRGB domain. The benchmark covers four smartphone device groups, two learned ISPs, three degradation regimes--noise, blur, and joint noise and blur--, and several representative RAW and RGB restoration models. Our results show that placement alone does not determine performance. The RAW restoration strategy outperforms the best generic RGB restoration models. However, RGB restoration models trained considering the ISP transformations, achieve the best overall performance. Our novel benchmark demonstrates that the image reconstruction performance strongly depends on the alignment between the restoration model and the target imaging pipeline. We consequently recommend reporting restoration placement and ISP-aware supervision as key experimental factors. Our code is available at this https URL

---


### 178. [Efficient All-in-One Weather Restoration using Spectral Harmonization](https://arxiv.org/abs/2609.02839)

**<font color=#1a73e8>作者：</font>** Paula Garrido-Mellado, Daniel Feijoo, Yuning Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adverse weather conditions such as rain, haze, and snow significantly degrade image quality, posing challenges for both human perception and physical AI. Existing restoration methods require large computational budgets, struggling to process high-resolution images and handle different degradations. In this paper, we present Frequency Reconstruction via Spectral Harmonization, a novel lightweight all-in-one restoration method that explicitly decomposes feature representations into high- and low-frequency components at each scale of a hierarchical encoder-decoder architecture. By combining spectral decomposition with spatial processing through Fourier-based skip connections, FReSH-IR captures complementary frequency information without sacrificing spatial detail. Our approach achieves similar restoration quality with 80% fewer parameters and operations than transformer-based models. Extensive experiments demonstrate that our method offers a great efficiency-performance trade-off, highlighting its practical applications in constrained-resource systems.

---


### 179. [RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation](https://arxiv.org/abs/2609.02847)

**<font color=#1a73e8>作者：</font>** Xiaolei Lang, Ze Kang, Zehao Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis from sparse inputs requires both geometric grounding from the observed views and generative priors of unobserved regions, motivating recent hybrid methods that combine reconstruction and generation. However, existing methods bridge the two with rendered images or explicit 3D representations such as point maps or 3D Gaussians. Generation is thus conditioned on a lossy and imperfect projection of the scene, inheriting its errors, and reconstruction receives no signal from generation to correct them. We present RoGe, an end-to-end unified reconstruction and generation framework that removes this explicit bridge. It targets roaming within a scene anchored by sparse views: given a few posed images and a camera trajectory, it synthesizes a temporally coherent video along that trajectory. From the sparse input views, RoGe builds an implicit scene representation with a feed-forward reconstruction model, and queries it with target camera rays to obtain per-view geometric features. These features are injected into a video diffusion model as conditioning, without any 3D intermediate. Both modules are trained jointly, so the generation objective directly shapes its own geometric conditioning. We conduct experiments on DL3DV, where RoGe outperforms reconstruction-based, generation-based, and hybrid baselines on image-level metrics and video-level temporal consistency. Ablations confirm that ray-queried implicit features outperform both raw reconstruction tokens and rendered RGB as conditioning, and that joint training brings further gains.

---


### 180. [MuyBridge: Mobile Human Center-of-Mass Estimation from Monocular Video via Sparse Fusion](https://arxiv.org/abs/2609.02854)

**<font color=#1a73e8>作者：</font>** Aidan Bradshaw, Marco Giordano, David Rode 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The 3D center of mass (CoM) is a primary quantity in the biomechanical analysis of sport, rehabilitation, and clinical movement, yet existing 3D pose tracking, mesh recovery, and multi-view triangulation methods either optimize 3D keypoint accuracy without anatomical constraints or carry compute and capture infrastructure too heavy to deploy where CoM tracking is most useful. As a result, the metric CoM remains difficult for coaches and movement analysts to measure from a single camera where athletes train and compete. In this work, we introduce MuyBridge, an on-device system that estimates the athlete's segmental center of mass trajectory from a single phone camera video stream. MuyBridge couples a compact 2D pose network and a distilled single-step monocular depth network through an analytic metric fusion that uses anatomical and physical priors to anchor the metric CoM, requiring no 3D or task-specific supervision. Evaluated on the athletic movements of AthletePose3D (running, track and field, and figure skating), MuyBridge achieves 33-41 mm vertical CoM error and 2.3-6.6% absolute-relative range error (AbsRel) under a one-time calibration, and produces CoM estimates at the 63 FPS pose-estimation rate using asynchronous 2.86 Hz depth updates on iPhone 15. Code is available at: this https URL

---


### 181. [PlantC2USeg: Cross-Scale Consistent Pre-Training for Few-Shot Unified Plant Point Cloud Segmentation](https://arxiv.org/abs/2609.02860)

**<font color=#1a73e8>作者：</font>** Yu Tian, Xintong Jiang, Jan Franklin Adamowski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern crop breeding demands precise organ-level analysis for trait quantification, making plant point cloud segmentation (PPCS) increasingly important. However, conventional deep learning approaches rely heavily on densely annotated datasets that are labor-intensive to acquire. Unified PPCS adaptation from distribution-shifted examples with minimal additional training remains challenging. To address this, we propose PlantC2USeg, a deep transfer learning framework featuring cross-scale consistency learning to explicitly align features across spatial scales and an information-restricted decoding strategy that prevents reconstruction shortcuts and promotes robust adaptation. The resulting pre-training enables stable few-shot generalization across species and sensing conditions, while unified fine-tuning with inherited thresholds further reduces adaptation overhead. Under full supervision on Soybean3D, PlantC2USeg achieves the highest semantic IoU and instance mWCov among compared methods, at 91.91% and 94.62%. With 20 labeled samples, it leads both metrics at 89.78% and 90.27%; with only 10 samples, it retains the highest mWCov of 83.23% while achieving 83.19% IoU. Across HR3D, 10-shot transfer to tobacco, tomato, and sorghum averages 78.41% IoU and 79.42% mWCov, while 22-shot transfer to SYAU-Maize achieves the highest IoU and mRec at 92.75% and 93.51%. Furthermore, a leading category-averaged mIoU of 85.0% on ShapeNet Part demonstrates the framework's capability to handle diverse shape variations beyond agricultural domains. These results demonstrate that PlantC2USeg reduces overall adaptation effort under distribution shifts, enabling scalable plant phenotyping and transferable 3D representation learning beyond agriculture.

---


### 182. [Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation](https://arxiv.org/abs/2609.02864)

**<font color=#1a73e8>作者：</font>** Yutong Liu, Nan Huang, Xu Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in unified generative models (UGMs) and world simulators have achieved unprecedented results in visual perception and synthesis. However, these models primarily rely on surface-level event alignment, leaving the capacity for high-level visual reasoning underexplored. True visual generative intelligence demands "Reasoning-to-Generation", an ability to infer latent rules from visual inputs and manifest solutions through precise, logically constrained visual outcomes. We introduce RIG-BENCH, a novel comprehensive benchmark that systematically evaluates Reasoning-driven Image Generation (RIG) across four cognitively demanding domains: Concept-based, Transformation-based, Pattern & Structure, and Scenario-based. Featuring 2000 curated samples, RIG-BENCH serves as a rigorous stress test for RIG. Our extensive evaluations of state-of-the-art UGMs and image/video generation models reveal a significant reasoning-generation gap, wherein models frequently produce locally plausible but globally illogical outputs. RIG-BENCH provides a vital diagnostic framework to guide the development of next-generation, logically grounded UGMs and world simulators.

---


### 183. [When Does Authorization End? Effect Closure at Provider Boundaries](https://arxiv.org/abs/2609.02866)

**<font color=#1a73e8>作者：</font>** Igor Santos-Grueiro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Revocation completion, clean state, or operation success can leave authorized work able to cause an effect the application rejects while the provider stays within its contract. We call the absence of all such paths policy-relative effect closure, or effect closure for short. Thus, a grant is closed when its existing authorizations retain no such path, and it cannot issue any new ones.
We present EFFECTBOUND, which uses an evidence-supported finite contract to decide whether an interface can truthfully report closure while required work completes. It reduces this to finite control with hidden state and returns a strategy, an impossibility certificate, or no verdict when evidence is insufficient. Machine-checked proofs establish the reduction and checker soundness; the checker derives closure results and validates certificates. Across GitHub, Kubernetes, NATS, and Kafka, closure fails in three ways: an interface lacks a needed control, clean visible state hides active work, or the model stops before the effect frontier---the last point where the effect can be prevented. The GitHub tool cannot bind a merge to the reviewed commit; a controlled run confirms that it may merge a different commit. NATS can report no stored or pending messages while dispatched work can still publish downstream. In Kafka, all fixed-set brokers had applied the revocation, yet an earlier authorized request could still append. We add a gate that blocks new use of revoked authority and delays return until earlier in-flight work completes. In a fixed-set Kafka~4.3.1 test deployment, this closes the studied synchronous, nontransactional write path without blocking unrelated requests. For a grant, authorization ends only when issuance stops and no earlier authorization can reach an effect the application rejects.

---


### 184. [Overcoming the Randomness-Utility Trade-off in Answering Differentially Private Linear Queries](https://arxiv.org/abs/2609.02880)

**<font color=#1a73e8>作者：</font>** Surendra Ghentiyala, Pritish Kamath, Ravi Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study the question of answering linear queries with differential privacy using few (expected) random bits. We provide a randomness-efficient analog of the $\| \cdot \|_K$-norm mechanism of Hardt and Talwar [HT10]. For the $\ell_\infty$-error, our algorithm can answer $d$ linear queries with $O(d / \varepsilon)$ error using $O(\log d)$ random bits, improving upon algorithms of Canonne et al. and Ghentiyala [CSV25, Ghe26]; this is optimal when $\varepsilon \le 1/d$. We also provide a computationally efficient version of our algorithm, albeit with an $O(\log d)$ multiplicative increase in the error.

---


### 185. [Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885)

**<font color=#1a73e8>作者：</font>** Kelvin Li, Dhruv Pendharkar, Anish Pahilajani 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent web agents use world models for test-time action selection by sampling candidate actions, predicting the resulting web states, and ranking them with a ranker model or a Process Reward Model (PRM). These world models are typically trained via supervised next-state prediction to generate fixed representations like HTML or AXTree snapshots. However, this objective is misaligned with the downstream ranker, which relies on predicted states being discriminative across candidates to accurately score them. To address this, we introduce predicted-state matching, a training objective where the predicted representation must distinguish the true resulting state from those reached by alternative actions. We train these models using a branching web-agent dataset derived from WebArena Go-Browse trajectories, where every decision point contains multiple alternative actions and their resulting states. Experiments on our held-out predicted-state matching benchmark show that our approach outperforms world models trained with supervised next-state prediction. We further show that our approach improves PRM-style action ranking on WebPRMBench compared with action-only PRMs and PRMs augmented with supervised-next-state world models. Finally, on WebArena-Lite, using our world model for test-time action selection improves end-to-end task success. Our project page is available at: this https URL.

---


### 186. [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](https://arxiv.org/abs/2609.02886)

**<font color=#1a73e8>作者：</font>** Junchao Huang, Guian Fang, Shengju Qian 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference. Training across heterogeneous data sources and video backbones is challenging: datasets differ in temporal scale, camera geometry, visual quality, motion, and captioning styles, while video generators use distinct representations and architectures. Naive data mixing and model-specific implementations therefore produce inconsistent supervision and make results difficult to reproduce and compare. SolarWM addresses this coupling with a reconfigurable multi-source data engine and a backbone-native adaptation framework. The engine converts 1.43 million canonical clips from 10 datasets into a unified, frame-aligned contract covering visual observations, metric camera geometry, captions, quality metadata, selection decisions, and provenance, while decoupling source processing from mixture construction. Under shared camera-conditioning, training, and inference interfaces, we instantiate four 5B--33B models based on Wan2.2, LTX-2.5, and MiniMax-H3 while preserving their native representations and objectives. A unified three-stage recipe combines bidirectional adaptation, teacher-forced autoregressive initialization, and distribution matching distillation. The resulting causal models enable real-time interaction over rollouts ranging from minutes to hours after being trained on only 5s sequences. By releasing the resulting data, pipeline, recipes, weights, and framework, SolarWM provides a reproducible and extensible foundation for interactive world-model research.

---


### 187. [A Common Measure of Communication for Speech Brain-Computer Interfaces](https://arxiv.org/abs/2609.02887)

**<font color=#1a73e8>作者：</font>** Dulhan Jayalath, Benjamin Ballyk, Oiwi Parker Jones  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speech brain-computer interfaces (speech BCIs) translate neural activity into language, offering a path towards restoring speech for people with paralysis and, more broadly, enabling new forms of natural human-computer interaction. Despite this promise, the field lacks a common measure of progress because systems use different datasets, recording methods, types of speech, and vocabularies, so their reported scores are rarely comparable. Underlying this measurement problem are two unresolved questions: (i) what distribution of words should a speech BCI enable a user to communicate, and (ii) how much information from this distribution can a system convey. We address both by deriving open-vocabulary mutual information (OVMI), an information-theoretic quantity that measures the information conveyed by a decoder relative to a reference distribution over the words a user may wish to communicate. This allows capabilities measured under different conditions, such as distinct vocabularies, to be evaluated on a common communication scale. We show that ordinarily reported accuracy, word error rate (WER), and other metrics computed only over the words a system supports can overstate how much of a user's intended speech the system can communicate. We then use OVMI to compare existing systems, expose trade-offs between how much of the user's language a system supports and how accurately it decodes those words, show that these comparisons depend on what the user is expected to communicate, and demonstrate that selecting a vocabulary to maximise OVMI yields up to 16.3% relative improvement in accuracy across three speech domains. OVMI therefore provides the speech BCI community with a principled way to compare heterogeneous systems, improve vocabulary design, and measure progress in the field.

---


> [!TIP]
> 当前位于：**151-187**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-187**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
