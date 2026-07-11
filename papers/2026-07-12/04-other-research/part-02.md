# 📦 其他研究 | 2026年07月12日

> 本类共 **189** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-189](./part-04.md)

---

### 51. [SAGA: Stable Acceleration Guidance for Autoregressive Video Generation](https://arxiv.org/abs/2607.08020)

**<font color=#1a73e8>作者：</font>** Thanh-Nhan Vo, Trong-Thuan Nguyen, Trung-Hoang Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion enables efficient streaming and long-horizon video generation, but repeatedly reusing generated latents as causal context can amplify temporal errors, resulting in flickering, motion jitter, and structural drift. In this paper, we investigate this failure mode from a spectral kinematic perspective and identify discrete latent acceleration as an effective signal for revealing unstable high-frequency temporal perturbations. To this end, we propose SAGA, a training-free \textbf{\textit{s}}table \textbf{\textit{a}}cceleration \textbf{\textit{g}}uidance approach for \textbf{\textit{a}}utoregressive video generation. SAGA integrates an acceleration domain spectral guidance objective based on finite-window Slepian projections with a structured autoregressive noise initialization strategy that suppresses short-range temporal correlations while preserving long-range motion structure. Without retraining or modifying the backbone, SAGA can be directly applied to existing chunk-wise autoregressive diffusion models, which is the prevalent setting for high-quality generation. Extensive experiments show that SAGA consistently improves temporal quality across multiple autoregressive diffusion models. On Self-Forcing, SAGA improves Temporal Quality from 97.30 to 97.91 and Image Quality from 69.60 to 70.51. Moreover, spectral analysis and human preference studies demonstrate that SAGA reduces temporal instability while maintaining visual fidelity.

---


### 52. [APIVOT: Adaptive Planning with Interleaved Vision-Language Thoughts](https://arxiv.org/abs/2607.08024)

**<font color=#1a73e8>作者：</font>** Emily Jin, Joy Hsu, Yiqing Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon robot planning requires jointly reasoning over semantic task structure and geometric feasibility. To successfully execute a task, a robot must decompose goals, select task-relevant objects, and sequence actions, while ensuring that plans satisfy spatial constraints such as limited free space and object collisions. In this work, we propose APIVOT, a VLM-based planner that adaptively interleaves language and visual thoughts for long-horizon planning. APIVOT learns to leverage language for semantic reasoning, while using visual thoughts as imagined future states for internal verification of geometric feasibility. On long-horizon kitchen tasks, APIVOT outperforms general-purpose VLMs and prior planning frameworks, achieving the largest gains in spatially constrained settings. We find that APIVOT learns meaningful modality selection behavior, demonstrating that adaptive interleaving of vision-language thoughts improves both planning success and reasoning efficiency.

---


### 53. [PGD-NO: A Neural Operator with Precomputed Geometry Decomposition for 3D Million-scale Physics Simulations](https://arxiv.org/abs/2607.08025)

**<font color=#1a73e8>作者：</font>** Weiheng Zhong, Jing Bi, Victor Oancea 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While neural PDE solvers have demonstrated significant potential for accelerating engineering simulations, existing architectures remain constrained by high memory consumption and the single node bottleneck, where the maximum processable mesh resolution is strictly limited by the VRAM of a single compute unit. To address these challenges, we propose PGD-NO, a neural operator with Precomputed Geometry Decomposition, that relocates the computational overhead of geometric encoding to a deterministic pre-computation phase. By utilizing an iterative geometry decomposition algorithm to extract geometry tokens, our model decouples feature extraction from solution querying. This architecture enables linear memory scalability, allowing high fidelity learning on meshes exceeding 10 million nodes, a scale where existing architectures typically encounter memory exhaustion. PGD-NO demonstrates competitive predictive accuracy across diverse industrial benchmarks and provides intrinsic interpretability through attention mechanisms. By effectively overcoming traditional mesh-size constraints, PGD-NO offers a robust and efficient solution for the next generation of large-scale, high-fidelity industrial design applications.

---


### 54. [An exact information theory of generalization phase transitions in Bayesian diffusion models](https://arxiv.org/abs/2607.08041)

**<font color=#1a73e8>作者：</font>** Henry Hunt, Mason Kamb, Surya Ganguli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How diffusion models circumvent the curse of dimensionality to learn complex distributions over high dimensional spaces from a finite training set, instead of memorizing it, remains a fundamental mystery. To address this, we introduce analytically tractable Bayesian information restricted diffusion (BIRD) models, in which each pixel observes restricted information about noisy data. A BIRD model time-reverses diffusion by inferring which past training sample produced its current restricted observation using the Bayesian posterior. This model class generalizes existing analytical diffusion models that use spatially local information restriction. We show that spatially local BIRD models closely approximate trained diffusion models \textit{early in training}, across different architectures such as UNets and DiTs. Under minimal assumptions on the data distribution, we identify an information-theoretic phase boundary between memorization and generalization in the joint space of amount of training data, time in the reverse generative process, and amount of information restriction: a BIRD model memorizes when the mutual information between its restricted noisy observations and the training data exceeds the log number of training points, and it generalizes otherwise. Experiments across a range of datasets confirm our theoretically predicted location for the transition. We find that generation proceeds near the edge of memorization: both spatially local BIRD models and early-training diffusion models track the memorization-generalization phase boundary by increasingly restricting information over time. Overall, our results reveal a fundamental role for information restriction in generative AI to circumvent the curse of dimensionality.

---


### 55. [Degree-Constrained Interval Optimization for Minimax Polynomial Approximation in Homomorphic Encryption](https://arxiv.org/abs/2607.08042)

**<font color=#1a73e8>作者：</font>** Jiheon Woo, Donggyun Ryu, Yongjune Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Homomorphic encryption (HE) enables privacy-preserving inference under arithmetic constraints that restrict encrypted evaluation to additions and multiplications. As a result, non-polynomial activation functions must be replaced by polynomial approximations. Among polynomial approximation methods, minimax approximation, typically computed by the Remez algorithm, is a standard approach because it minimizes the maximum approximation error over a given design interval. For minimax polynomial design, the approximation interval is a critical hyperparameter: a wider interval improves robustness to large-magnitude inputs while increasing the minimax approximation error under a fixed degree budget. In this paper, we formulate this trade-off as a distribution-aware interval optimization problem, where the approximation interval is chosen to minimize the mean-squared error (MSE) with respect to the pre-activation distribution of interest. To effectively control outside-interval inputs, we combine minimax polynomials with domain extension functions (DEFs) and their HE-realizable polynomial counterparts, domain extension polynomials (DEPs), which approximate a clipping operation outside the design interval and thereby suppress uncontrolled polynomial extrapolation. We first derive an analytically tractable DEF-based proxy objective that captures the trade-off between within-interval minimax approximation error and outside-interval clipping error. We then connect this idealized objective to HE-realizable DEP constructions through an implementation-error decomposition with an accompanying upper bound.

---


### 56. [Holographic Neural PCFG for Unsupervised Parsing](https://arxiv.org/abs/2607.08063)

**<font color=#1a73e8>作者：</font>** Ryosuke Yamaki, Daichi Mochihashi, Nobutaka Shimada 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unsupervised constituency parsing aims to accurately induce latent tree structures from raw text alone. Recent neural parameterizations of PCFGs achieve strong performance in both supervised and unsupervised parsing, yet rely on high-capacity black-box networks for rule scoring -- as exemplified by the Neural PCFG family -- leaving rule probabilities without an interpretable mathematical form. In this paper, we propose Holographic Neural PCFG (Hol-PCFG), which recasts PCFG rule scoring as algebraic relation modeling among grammar-symbol embeddings. Hol-PCFG adapts Holographic Embeddings (Nickel et al., 2016), which scores knowledge-graph triples via circular correlation, to the left-child, right-child, and lexical-emission relations over torus-constrained embeddings, giving every rule probability a closed form that carries the intrinsic structure of grammar rules by construction. Hol-PCFG achieves state-of-the-art parsing performance in six languages while cutting rule-scoring parameters by 99.94% relative to the baseline model and training more stably. Additionally, we demonstrate that Hol-PCFG can parse Japanese directly from characters without any morphological segmentation, retaining nearly the same morpheme-level performance.

---


### 57. [COBART: Controlled, Optimized, Bidirectional and Auto-Regressive Transformer for Ad Headline Generation](https://arxiv.org/abs/2607.08071)

**<font color=#1a73e8>作者：</font>** Yashal Shakti Kanungo, Gyanendra Das, Pooja A 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online ads are essential to all businesses and ad headlines are one of their core creative component. Existing methods can generate headlines automatically and also optimize their click-through-rate (CTR) and quality. However, evolving ad formats and changing creative requirements make it difficult to generate optimized & customized headlines. We propose a novel method that uses prefix control tokens along with BART fine-tuning. It yields the highest CTR and also allows users to control the length of generated headlines for use across different ad formats. The method is also flexible and can easily be adapted to other architectures, creative requirements and optimization criteria. Our experiments demonstrate a 25.82% increment in Rouge-L and a 5.82% increment in estimated CTR over previously published strong ad headline generation baseline.

---


### 58. [Cross-Modal Generative Framework for Signal Translation from Fetal-Maternal Electrocardiograms to Fetal Doppler Waveforms](https://arxiv.org/abs/2607.08073)

**<font color=#1a73e8>作者：</font>** Tongli Su, Alireza Rafiei, Marly van Assen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fetal electrocardiogram (fECG) and Doppler ultrasound provide complementary views of fetal cardiovascular function: fECG captures electrical activity while Doppler reflects mechanical hemodynamics shaped by factors such as placental resistance and vascular compliance. Understanding the recoverable and unrecoverable Doppler components through reconstruction from fECG offers insight into the relative contributions of electrical versus mechanical factors in fetal circulation, thereby informing clinical decisions. In addition, clinical evidence of maternal-fetal cardiac coupling suggests that maternal cardiovascular dynamics may also inform fetal hemodynamics. To computationally model these relationships, we propose a cross-modal generative framework combining dilated convolutions with cross-modal attention to selectively incorporate maternal ECG and self-attention to capture long-range temporal dependencies. Trained on 885 synchronized fetal/maternal ECG and Doppler envelope segments from 39 pregnancies, our model synthesizes Doppler envelopes with power spectral density mean squared error (PSD MSE) of 49.9 +/- 15.8 dB^2 (51% lower than two-channel baseline) and heart-rate error of 4.71 +/- 0.77 bpm (1.5% better than baseline; negligible relative to the 110-160 bpm physiological range). Cross-modal attention yields a 39% PSD MSE reduction over naive dual-channel concatenation, quantifying the contribution of maternal-fetal coupling. Our proposed framework advances computational modeling of the maternal-fetal cardiovascular system by enabling the synthesis of Doppler envelopes from dual-lead ECG. By analysis of both recoverable and residual Doppler components, this approach enables quantification of the purely mechanical contributions to Doppler waveforms -- those not recoverable from electrical recordings -- ultimately facilitating a more comprehensive fetal assessment.

---


### 59. [UAV-OVVIS: Unmanned Aerial Vehicles Also Need Open-Vocabulary Video Instance Segmentation](https://arxiv.org/abs/2607.08075)

**<font color=#1a73e8>作者：</font>** Mingyu Dou, Shi Qiu, Ming Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned Aerial Vehicle (UAV) videos are widely used in traffic monitoring, urban management, and emergency rescue. However, existing UAV video perception mainly relies on box-level localization and trajectory association under predefined categories, making it difficult to simultaneously support flexible queries and fine-grained instance-level dynamic understanding in open scenarios. To this end, we introduce a new task, UAV Open-Vocabulary Video Instance Segmentation (UAV-OVVIS), which discovers targets in UAV videos according to open-vocabulary queries and outputs instance-level segmentation trajectories with globally consistent identities. Considering the scarcity of instance-level annotations in UAV scenarios, we propose AeroTrack, a training-free unified framework. AeroTrack centers on periodic open-vocabulary detection, short-segment mask propagation, and cross-segment identity unification, reusing existing visual foundation models to enable UAV-OVVIS. Based on this framework, we instantiate five AeroTrack variants and construct AeroVIS, an evaluation benchmark for UAV-OVVIS containing 9 UAV object categories and 8,279 trajectories. Experiments show that AeroTrack substantially outperforms existing general video instance segmentation methods in UAV scenarios and demonstrates strong open-vocabulary robustness and generalization. To support future research, we release AeroTrack and AeroVIS as a unified framework and benchmark for UAV-OVVIS.

---


### 60. [LDFE: Laplacian Decoupled Feature Enhancement Block for Dual-Stream CNN-based RGB-IR Object Detection](https://arxiv.org/abs/2607.08076)

**<font color=#1a73e8>作者：</font>** Wenhao Dong, Xiaoyan Luo, Linlin Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The complementary information between RGB and IR images can significantly enhance object detection performance under extreme conditions. Existing methods prefer dual-stream CNN backbones built upon YOLO for feature extraction and focus on the design of feature fusion. In this paper, we introduce the Laplacian Decoupled Feature Enhancement block (LDFE) to fuse features from different stages of the dual-stream CNN backbone. By design, LDFE simultaneously considers the characteristics of modalities and structures for feature fusion by employing global-local decomposition, denoising, fusion, and reconstruction, sequentially. The LDFE first separates features into global and local components based on Laplacian Pyramid, and then performs denoising and fusion based on Global State Space Enhancement module (GS2E) and Local Convolutional Correlation Enhancement module (LC2E) separately. Specifically, the GS2E conducts a two-branch architecture for the main and auxiliary modalities. It dynamically suppresses noise in the main modality through cross-modal attention derived from the auxiliary modality, while employing a State Space Model to capture long-range dependencies within the global feature representations of the main modality. To obtain bidirectional interaction, the two modalities systematically alternate their main/auxiliary roles. Moreover, the LC2E suppresses noise in local features and leverages spatial and channel dimension along with triple convolution to extract fine-grained details for fusion. These innovative designs achieve a significant performance improvement, with mAP surpassing the SOTA methods 6.2%, 3.7%, 4.7%, 2.3%, 4.1% and 2.0% on M3FD, DroneVehicle, LLVIP, FLIR-Aligned, KAIST and VEDAI datasets,respectively.

---


### 61. [Modular Pretraining Enables Access Control](https://arxiv.org/abs/2607.08077)

**<font color=#1a73e8>作者：</font>** Ethan Roland, Murat Cubuktepe, Erick Martinez 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI developers face a dual-use dilemma. An AI capability that helps one user cure a disease can help another synthesize one. This dilemma could be resolved with access control, limiting dual-use AI capabilities to trusted deployments with a legitimate need. A gold standard for access control would be to serve separate models with different capabilities to different users. However, training and deploying multiple models is prohibitively expensive. To address this challenge, we propose gradient-routed auxiliary modules (GRAM), a pre-training method that adds modules to a neural network and selectively updates them to induce specialization. Ablating a module at inference time removes its capability from the network, approximating a model trained on filtered data. We evaluate GRAM on synthetic stories and realistic dual-use data spanning virology, cybersecurity, nuclear physics, and specialized code. These experiments show that GRAM disables targeted capabilities while preserving the rest, and resists their recovery under finetuning better than post-hoc unlearning. Most importantly, a Chinchilla-optimal scaling analysis from 50M to 5B parameters shows that the gap between data-filtered and full-data models widens with scale on removed capabilities but stays small on retained ones, and that GRAM closely tracks data filtering. GRAM's training cost is independent of the number of supported capability profiles, yielding a 5x reduction over data filtering in our 5-profile setting.

---


### 62. [HeadRoom: Lightweight, Edge-deployable Pipeline for Adaptive Notification Routing](https://arxiv.org/abs/2607.08083)

**<font color=#1a73e8>作者：</font>** Dinithi Dissanayake, Prasanth Sasikumar, Suranga Nanayakkara  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Emerging wearables, such as smart glasses, can deliver notifications through multiple sensory channels, but there is still a limited understanding of how to choose the right channel at the right moment. We propose HeadRoom, a lightweight, edge-deployable pipeline that estimates the availability of visual and auditory channels in real time from egocentric video and audio. Our controlled user study (N=25) shows that, under high perceptual load, routing notifications to the more available channel reduces response time relative to routing them to the less available channel. This work opens up a new possibility for adaptive routing of notifications in wearable and immersive systems.

---


### 63. [Mixture of Enhanced-View Experts for Multi-Query Vehicle ReID and A Large-Scale Benchmark](https://arxiv.org/abs/2607.08085)

**<font color=#1a73e8>作者：</font>** Aihua Zheng, Jie Zhen, Chenglong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-query vehicle ReID aims to leverage complementary information from diverse views for robust feature learning. However, current methods suffer from simplistic feature fusion and thus easily ignores some important view information and cross-view relationships. To handle these problems, this work presents a novel approach called Mixture of Enhanced-View Experts (EV-MoE), which enhances the feature representation of each view and efficiently integrate the view-specific enhanced features by MoE, for robust multi-query ReID. In particular, we design a mixture of enhanced-view experts module, which consists of two parts including view-specific feature enhancement sub-Module (VFEM) and dynamic multi-view fusion sub-Module (DMFM). Moreover, we further introduce Multi-view Alignment Loss (MAL), which aligns features through bidirectional crossview contrastive learning and reconstruction constraints, addressing the challenges of consistency between multi-query features and single-image features. In addition, to evaluate multi-query ReID in real-world environments, we collect LCRI-1K, a largescale vehicle ReID dataset with 1,090 identities, 107,805 images, across 23,637 cameras, where each vehicle appears in an average of 67.5 cameras, providing a comprehensive benchmark to test the robustness in complex environments. Extensive experiments demonstrate the robustness of CAFNet in addressing the multiquery vehicle ReID problem. The code is available at https: //github.com/xiaozhen28/CAFNet.

---


### 64. [GRE-Diff: Gaussian Room Embeddings for Structured Layout Diffusion](https://arxiv.org/abs/2607.08086)

**<font color=#1a73e8>作者：</font>** Jing Wang, Haoran Xiong, Zihao Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Designing functional and aesthetically coherent floor plans requires exploring a vast space of possible room arrangements, a task that quickly becomes overwhelming for human designers. In this paper, we propose GRE-Diff, a controllable and interactive diffusion-based framework that automates the creation and editing of apartment floor plans under user-specified constraints.
By combining AI-generated suggestions with real-time, human-in-the-loop editing, the system enables users to specify room types, room counts, boundary shapes, and editing operations through LLM-parsed instructions or GUI-based interaction.
It then generates a diverse set of plausible and well-structured designs for refinement.
At the core of our approach is Gaussian Room Embedding (GRE), a continuous latent representation that models each room as a spatial Gaussian distribution capturing its location and extent.
Extensive experiments on the RPLAN dataset show that GRE-Diff produces high-quality, constraint-aware, and editable polygonal layouts, offering a practical step toward bridging AI-driven automation and human creativity in spatial design.

---


### 65. [Deep Learning Method for Stationary Distribution of Reflected Brownian Motion](https://arxiv.org/abs/2607.08091)

**<font color=#1a73e8>作者：</font>** Jim Dai, Zhanhao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The stationary distribution of reflected Brownian motion (RBM) plays an important role in the analysis of high-dimensional stochastic systems, yet closed-form solutions are known only for a few special cases. Computing important performance metrics, such as tail probabilities, is even more intractable, despite their practical relevance. In this paper, we develop a deep learning approach that accurately and efficiently learns the Laplace transform of high-dimensional RBMs based on the basic adjoint relationship (BAR). Our framework combines a careful design of the loss function, training data sampling procedure, and neural network architecture. We evaluate the proposed method on RBM instances with known ground-truth tail probabilities and demonstrate near-perfect prediction in high-dimensional settings, highlighting its potential as a general tool for analyzing stochastic systems beyond analytically tractable regimes. Our code can be found at this https URL.

---


### 66. [zkComposer: Decomposing Proof Construction to Scale zkML](https://arxiv.org/abs/2607.08095)

**<font color=#1a73e8>作者：</font>** Pawan Kumar Sanjaya, Christina Giannoula, Valdy Oktavian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zero-knowledge machine learning (zkML) enables a server to perform verifiable inference while keeping model parameters private from the client. However, existing zkML systems incur prohibitive proof-generation costs. We observe that proof generation exhibits limited parallelism; that is, prover time does not decrease significantly as the number of threads increases. This limitation is because existing systems rely on monolithic proof computation, constructing a single proof for the entire machine learning model. We introduce zkComposer, a modular proof-construction framework that unlocks an additional dimension of parallelism, in addition to the parallelism in existing proof kernels. zkComposer decomposes the zkML proof of correct inference into independent sub-proofs, each covering a subset of the computation for inference e.g., each independent sub-proof can cover a subset of contiguous layers in the ML model. Adjacent sub-proofs are cryptographically linked through shared commitments to the activations from the boundary layer. zkComposer provides the same guarantees as the monolithic proof without requiring additional linking proofs or changes to the underlying cryptographic primitives. We implement zkComposer and evaluate it on three CNNs and GPT-2. We show that, on CNN workloads, zkComposer reduces prover time and response time by up to 3.25x relative to zkCNN [1]. On GPT-2, zkComposer reduces these times by up to 4.83x relative to zkGPT [2], when partitioning along the model layers. When partitioning across both model layers and input sequences in GPT-2, we show that zkComposer reduces prover time and response time by up to 6.84x relative to zkGPT [2].

---


### 67. [EVIS: A Physics-Grounded Event Camera Plugin for NVIDIA Isaac Sim](https://arxiv.org/abs/2607.08098)

**<font color=#1a73e8>作者：</font>** Linli Shi, Ruijun Zhang, Ziyun Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras offer microsecond temporal resolution, low latency, and high dynamic range, making them attractive for robotics. However, labeled event-camera data for a specific robot and scene is scarce and expensive to collect, which slows the development of event-based perception and control. We present EVIS: a physics-grounded event camera plugin for NVIDIA Isaac Sim that generates high-rate, fully labeled event streams directly inside a physics simulator. The plugin implements a faithful log-intensity contrast event model with per-pixel asynchronous reference updates; it migrates from a normal RGB camera with few changes and integrates into any Isaac Sim / Isaac Lab scene, inheriting the simulator's physics and frame-perfect ground truth. It is fully configurable, and offers an interpolation option that renders only sparse keyframes and synthesizes the in-between frames through bidirectional motion-vector warping, making real-time generation on a single GPU possible. Optional sensor noise and motion blur further narrow the gap to real cameras. The generated streams are directly usable by pretrained event networks for downstream tasks. Code repository: this https URL

---


### 68. [Stochastic Order Learning: An Approach to Rank Estimation Using Noisy Data](https://arxiv.org/abs/2607.08103)

**<font color=#1a73e8>作者：</font>** Chaewon Lee, Seon-Ho Lee, Chang-Su Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rank estimation under label noise poses a fundamental challenge, as ordinal annotations often exhibit structured uncertainty rather than simple label corruption. In this paper, we reformulate rank estimation with noisy ordinal labels as a stochastic ordering problem, in which each instance is inherently associated with multiple plausible ranks instead of a single deterministic label. Based on this view, we propose stochastic order learning (SOL), a learning framework that captures ordinal label uncertainty and learns an embedding space through two complementary objectives: a discriminative loss that structures instance--centroid interactions and a stochastic order loss that enforces probabilistic ordering relations between instances. Extensive experiments across diverse datasets demonstrate that SOL enables reliable rank estimation under various types and levels of label noise. The source code is available at this https URL.

---


### 69. [Vanilla SGD with Momentum Survives Heavy-Tailed Noise: Convergence Analysis without Gradient Clipping or Normalization](https://arxiv.org/abs/2607.08104)

**<font color=#1a73e8>作者：</font>** Ryusei Yamada, Naoki Sato, Hideaki Iiduka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic gradient descent (SGD) is a cornerstone of modern optimization. While its performance under heavy-tailed noise is often addressed through specialized modifications such as gradient clipping or normalization, we investigate a more fundamental question: how does vanilla SGD, particularly with momentum, perform in the presence of heavy-tailed noise? In this paper, we refine existing convergence results for vanilla SGD and, more importantly, provide the first comprehensive convergence analysis of vanilla SGD with momentum for strongly convex, convex, and nonconvex objectives, without employing any gradient control mechanisms. Our results demonstrate that the obtained convergence rates are inferior to the optimal rates achieved by clipped or normalized variants of SGD, thereby revealing inherent limitations of vanilla methods under heavy-tailed noise. The theoretical findings are supported by experiments on synthetic functions.

---


### 70. [Contrastive Order Learning: A General Framework for Ordinal Regression](https://arxiv.org/abs/2607.08109)

**<font color=#1a73e8>作者：</font>** Chaewon Lee, BeomJun Shim, Kwang Pyo Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose contrastive order learning (ConOrd), a contrastive learning framework for ordinal regression that integrates the strengths of contrastive learning and order learning. While contrastive learning effectively leverages all samples in a batch, it typically ignores the inherent ordering among rank labels. Conversely, order learning explicitly models label ordinality but often relies on local, margin-based comparisons, limiting its ability to capture global ordinal structure. ConOrd addresses these limitations by introducing a contrastive order loss with soft affinity and disparity weights based on rank differences, enabling fine-grained modeling of ordinal relationships across all sample pairs within a batch. Extensive experiments on a range of ordinal regression tasks, including facial age estimation, blind image quality assessment, and blind video quality assessment, demonstrate that ConOrd consistently achieves state-of-the-art performance and generalizes well across diverse ordinal regression scenarios. The source code is available at this https URL.

---


### 71. [Workload-Preserving Differentially Private Synthetic Data for Causal Inference via Maximum-Entropy Calibration](https://arxiv.org/abs/2607.08122)

**<font color=#1a73e8>作者：</font>** Amir Asiaee, Kaveh Aryan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Workload-based differentially private (DP) synthetic data methods privately measure aggregate queries and post-process the noisy answers into synthetic records. Generic workloads can achieve strong distributional fidelity, but causal estimands such as the average treatment effect (ATE) depend on treatment-arm balance and outcome moments that generic marginals need not preserve. We propose causal workloads: DP query sets designed around the orthogonal moments used by doubly robust causal estimators. The released workload can be used directly by stable moment-map estimators or reconstructed by maximum-entropy calibration into reusable synthetic data; our theory decomposes ATE error into sampling, privacy, workload-approximation, Monte Carlo, and calibration terms. We also introduce Causal-AIM, an adaptive workload selector, and a noise-aware multiple-imputation (NA+MI) procedure for confidence intervals from DP synthetic data. Because the workload is released once, the same DP synthetic table can support ATE, ATT, and subgroup analyses without additional privacy spending. Empirically, causal workloads are most useful at strict privacy budgets and for calibrated uncertainty, while generic workloads often retain an advantage for point RMSE as privacy relaxes. The broader lesson is a tradeoff: distributional fidelity can help point accuracy, but valid causal inference requires preserving causal moments and propagating DP noise rather than treating synthetic rows as real.

---


### 72. [Understanding and Mitigating the Video-Action Generalization Gap via Temporal Ratio](https://arxiv.org/abs/2607.08127)

**<font color=#1a73e8>作者：</font>** Utkarsh A. Mishra, Yongxin Chen, Danfei Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative video foundation models exhibit strong compositional priors, yet world-action models (WAMs) and video-action models (VAMs) often lose these priors after finetuning on robotic action data. We refer to this discrepancy as the video-action generalization gap. In this paper, we systematically investigate this gap by evaluating a comprehensive design space of VAMs, demonstrating that standard design choices yield no emergent explanation pattern. To explain this behavior, we introduce the Temporal Ratio (TR), an attention-based measure of how strongly the action head relies on future latent rollouts relative to the anchored current frame. TR has two key properties: first, a model's structural reliance on future-predictive latents, measured via TR, acts as a predictor of its compositional generalization capacity; second, it natively fluctuates based on task phase, shifting attention to future frames during planning and reverting to the present frame for precise manipulation. Finally, based on these findings, we propose an inference-time adaptive guidance method, which exploits this intrinsic feature attention pattern to dynamically amplify compositional video conditioning signals precisely when the policy relies on future rollouts. Evaluated on the LIBERO benchmark and real-world tasks, our approach mitigates the OOD-ID compositional generalization gap. More details: this https URL

---


### 73. [Answer Set Programming Energised! End-to-End Neurosymbolic Reasoning and Learning with ASP and Energy Based Models](https://arxiv.org/abs/2607.08136)

**<font color=#1a73e8>作者：</font>** Jakob Suchan, Julius Monsen, Salim Baloch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a general neurosymbolic reasoning and learning methodology based on a modular integration of answer set programming with an energy based model substrate. Key contributions are: (1) supporting joint optimisation in the continuous latent space through explicit ASP-based declarative semantics fully incorporating background knowledge, constraints, non-monotonic inference; and (2) advancing recent works at the interface of answer sets, probabilistic logic, and answer set modulo theories by providing a generalised model and practical platform for ASP-centric robust, end-to-end training for applications in dynamic domains (e.g., involving perception and interaction). We provide a practical implementation, and demonstrate basic use and application (with MNIST), and evaluate with the visual question-answering benchmark Clevr and the multi-object tracking benchmark MOT.

---


### 74. [Securing Autonomous Vehicle Systems via Twin-Aware Federated Reinforcement Learning](https://arxiv.org/abs/2607.08137)

**<font color=#1a73e8>作者：</font>** Zifan Zhang, Minghong Fang, Dianwei Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated reinforcement learning (FRL) is crucial for enabling collaborative learning across multiple agents without sharing raw data, thereby enhancing privacy and scalability in the decision-making process within dynamic vehicular environments. However, poisoning attacks pose a significant threat to the security and reliability of FRL-based systems, particularly in safety-critical autonomous driving, where this vulnerability remains largely unexplored. These attacks can compromise the global control model by subtly injecting malicious system parameters, leading to potential hazards. To counter these challenges, we present \alg (\underline{Sec}ure \underline{A}ggregation with \underline{p}oisoning-\underline{p}revention and historical reinforcement) as a defensive framework aimed at enhancing the robustness of FRL systems designed for safety-critical driving scenarios. \alg strategically integrates digital twins for rehearsal-based learning and leverages historical aggregated model parameters along with a selected central gradient to ensure that only benign data is aggregated, effectively mitigating the influence of malicious agents. Theoretical guarantees are provided for the convergence performance of \alg in the presence of poisoning attacks. We also validate the effectiveness of \alg using developed digital twins that model realistic highway environments to evaluate the control of autonomous vehicles under adversarial conditions.

---


### 75. [Prismata: Confining Cross-Site Prompt Injection in Web Agents](https://arxiv.org/abs/2607.08147)

**<font color=#1a73e8>作者：</font>** Corban Villa, Alp Eren Ozdarendeli, Sijun Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous web agents promise to automate everyday browsing tasks, but inherit one of the web's oldest attack surfaces. Cross-Site Scripting proved that mixing trusted and untrusted content is dangerous, even on benign pages. Agents resurface this risk by interpreting natural language as instructions, allowing third-party and user-generated content to hijack the agent via prompt injection. The core challenge is that deriving a task-specific security policy requires reasoning over page structure that is entangled with the attacker's content.
We present Prismata, a defense enforcing contextual least privilege for web agents, constraining both what the agent sees and what it can do. Prismata's dynamic trust derivation produces permission labels for page content, with structural confinement guarantees, inspired by classical integrity models, that bound any labeling errors so that labels can only decrease in privilege and mislabelings are bounded. Prismata's mechanical confinement enforces these labels by redacting content and restricting agent capabilities. Importantly, these mechanisms require no developer annotations, so Prismata supports the long tail of websites. Across recent published web agent attacks, including adaptive variants, Prismata substantially reduces attack success while preserving benign task utility.

---


### 76. [DeepPySR -- A Symbolic Regression Framework with Dynamic Pruning, Pareto Selection, and Hierarchical Composition for Real-World Scientific Discovery](https://arxiv.org/abs/2607.08150)

**<font color=#1a73e8>作者：</font>** Fuling Chen, Kevin Vinsen, Phillip Melton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) discovers analytical equations from data, yielding glass-box models with directly interpretable formulas, unlike black-box methods that rely on unstable post-hoc tools such as SHAP or LIME. This transparency is crucial in clinical medicine and social science, but SR faces three challenges: high-dimensional inputs, principled selection of Pareto-front formulae, and data irregularities such as multicollinearity and class imbalance. We introduce DeepPySR, which addresses these issues with a dynamic variable-pruning schedule to remove irrelevant features during search, an exponential Pareto selection criterion that eliminates trade-offs between accuracy and complexity, and a multi-layer architecture for hierarchical symbolic composition. On four Feynman physics benchmarks and seven biomedical and social-science datasets, DeepPySR outperforms PySR and baselines on body fat (R$^2$: 0.794 vs.\ 0.702), heart disease (F1: 0.898 vs.\ 0.787), student performance (R$^2$: 0.964 vs.\ 0.948), and Raine BMI (R$^2$: 0.525 vs.\ 0.370), producing interpretable formulas aligned with domain risk factors.

---


### 77. [LEXIC: Lightweight Eye-tracking eXtension via Injected Complexity](https://arxiv.org/abs/2607.08152)

**<font color=#1a73e8>作者：</font>** Sumin Lee, Kyeonghun Kim, Subeen Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On the recent EyeBench benchmark, predicting reading comprehension from eye movements exposes a stark gap: text-aware models using pretrained language models reach 56--63% AUROC, while gaze-only models operate at chance. We ask how far a gaze-only model can be pushed by lightweight, language-model-free conditioning. Building on the EyeBench AhnCNN baseline, LEXIC-Base, we propose two mechanisms to inject three precomputed word-level difficulty signals, GPT-2 surprisal, word frequency, and word length, into the per-fixation input: direct concatenation, LEXIC-Concat, and a residual mechanism, LEXIC-Res, where a small head predicts typical-reader gaze response and the encoder is conditioned on the deviation. On the OneStop reading comprehension task, with K=5 seed-ensemble training across ten folds, both mechanisms produce statistically consistent AUROC gains on Unseen Text, +1.8 to +2.2 percentage points, Wilcoxon p <= 0.065. LEXIC-Concat additionally lifts Unseen Reader by +2.9 percentage points, p = 0.010. We trace an architectural boundary in LEXIC-Res on Unseen Reader, +1.8 percentage points, p = 0.19, to the prediction head being calibrated to training readers, transferring imperfectly to out-of-distribution readers.

---


### 78. [Unified Face Attack Detection via Fine-Grained Semantic Guidance](https://arxiv.org/abs/2607.08156)

**<font color=#1a73e8>作者：</font>** Ning Jiang, Shijie Yu, Dingheng Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing applications of facial recognition systems are accompanied by increasingly diverse security threats. Existing datasets lack detailed textual descriptions of forgery cues, leading most prior methods to treat face attack detection primarily as a visual recognition task. In this paper, building upon the large-scale MS-UFAD dataset which contains over 8 million attack images, we enrich each image with a fine-grained textual description of forgery cues. Furthermore, we propose a Dual Alignment Forgery Network(DAF-Net) to better leverage these textual information. Extensive experiments demonstrate that our approach extracts more generalizable and semantically meaningful forgery representations from attack images, outperforming both vision-only methods and approaches based on coarse-grained descriptions.

---


### 79. [ProsMAE: Multi-Source MAE Pretraining for ISUP Grade Classification](https://arxiv.org/abs/2607.08162)

**<font color=#1a73e8>作者：</font>** Anna Jung, Kyeonghun Kim, Youngung Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole slide images (WSIs) provide rich diagnostic information for computational pathology, but their gigapixel scale, stain variation, scanner differences, tissue artifacts, and limited expert annotation make robust model training challenging. This paper presents a multi-source Masked Autoencoder (MAE) framework, named ProsMAE, for histopathology representation learning. Tiles from Prostate cANcer graDe Assessment (PANDA), CAncer MEtastases in LYmph nOdes challeNge 2017 (CAMELYON17), and BReAst Carcinoma Subtyping (BRACS) are used for ProsMAE pretraining to expose the encoder to diverse tissue morphology and acquisition conditions. The learned encoder is transferred for International Society of Urological Pathology (ISUP) grade classification through ProsCLS, using a frozen encoder and a linear classification head. ProsMAE achieved a higher mean validation quadratic weighted kappa (QWK) than the vanilla MAE frozen linear-probe baseline under the evaluated disjoint PANDA split. Repeated-split evaluation remains necessary to further establish robustness across split compositions.

---


### 80. [Continual Test-Time Adaptation in Computer Vision: Methods, Benchmarks, and Future Directions](https://arxiv.org/abs/2607.08164)

**<font color=#1a73e8>作者：</font>** Sarthak Kumar Maharana, Shambhavi Mishra, Yunbei Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural nets achieve remarkable performance when training and test data share the same distribution, but this assumption frequently breaks in real-world deployment, where data undergoes continual distributional shifts. Continual Test-Time Adaptation (CTTA) addresses this challenge by adapting pretrained models to non-stationary target distributions on-the-fly, without access to source data or labeled targets, while mitigating two critical failure modes: catastrophic forgetting of source knowledge and error accumulation from noisy pseudo-labels over extended time horizons. In this comprehensive survey, we formally define the CTTA problem, analyze the diverse continual domain shift patterns that characterize different evaluation protocols, and propose a hierarchical taxonomy that categorizes existing methods into three families: optimization-based strategies (entropy minimization, pseudo-labeling, parameter restoration), parameter-efficient methods (normalization layer adaptation, adaptive parameter selection), and architecture-based approaches (teacher-student frameworks, adapters, visual prompting, masked modeling). We systematically review representative methods within each category and present comparative benchmarks and experimental results across standard evaluation settings. Finally, we discuss limitations of current approaches and highlight emerging research directions, including adaptation of foundation models and black-box systems, providing a roadmap for future research in robust continual test-time adaptation. We encourage visiting our repository at [this https URL](this https URL)

---


### 81. [Understanding Layer Patching in Model Size Interpolation](https://arxiv.org/abs/2607.08170)

**<font color=#1a73e8>作者：</font>** Sara Kangaslahti, Jonathan Geuter, Nihal V. Nayak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-shot model size interpolation aims to create new models of intermediate target sizes by combining existing models without additional training. Recent work on boomerang distillation [Kangaslahti et al., 2026] shows that a student language model distilled from a larger teacher can be expanded by iteratively patching its layers, replacing student layers with contiguous blocks of teacher layers to obtain models whose size and performance interpolate between the student and the teacher. In this work, we provide the first systematic study of student-layer selection for model size interpolation. We cast finding the optimal layer subset for each model size as an optimization problem and prove it can be viewed as a shortest-path problem in a certain acyclic graph. In experiments, we show that patching strongly shapes interpolation behavior, with effects that vary substantially across model families. We find that simple sequential strategies--patching either from the first layer to the last or from the last to the first--often achieve surprisingly strong performance in practice. We further introduce KLPatch, a greedy patching algorithm based on KL divergence, which often improves over last-to-first patching and approximately solves the optimization problem. Together, our results provide a principled understanding of how layer patching affects model size interpolation and offer practical guidance for constructing near-optimal interpolated models.

---


### 82. [Attention-Based Segmentation of WMHs and Differentiation of Vascular vs. Demyelinating Lesions](https://arxiv.org/abs/2607.08171)

**<font color=#1a73e8>作者：</font>** Aina Tur-Serrano, Gabriel Moyà-Alcover, Francisco J. Perales López  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> White Matter Hyperintensities (WMHs) are commonly observed in brain Magnetic Resonance Imaging (MRI) scans. They are associated with various neurological conditions, including vascular and inflammatory demyelinating diseases. Despite differing in etiology, WMHs from these conditions often appear similar on Fluid Attenuated Inversion Recovery (FLAIR) images. This similarity makes differential diagnosis challenging. In this work, we highlight the potential of combining attention-based segmentation with feature-driven classification. This approach supports more accurate and efficient classification between vascular and demyelinating white matter pathologies. For segmentation, we evaluate the effectiveness of attention mechanisms, specifically the Bottleneck Attention Module (BAM) and the Convolutional Block Attention Module (CBAM). We also test different architectures, particularly Attention U-Net. In addition, we explore advanced training strategies, such as patch-based learning and a 2.5D approach, to enhance lesion detection. After segmentation, we extract morphological features from the lesion masks. We then use them to classify WMHs based on their underlying cause. Our experiments utilize five publicly available datasets with diverse imaging protocols to promote model generalizability, despite limited sample sizes. The results suggest that attention-based segmentation and feature-driven classification offer a promising direction for discriminating vascular and demyelinating white matter lesions. Further validation in larger clinical cohorts is still needed.

---


### 83. [Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets](https://arxiv.org/abs/2607.08173)

**<font color=#1a73e8>作者：</font>** Jack Hopkins, Dipika Khullar, Fabien Roger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Black box auditing of language models is an essential pre-deployment tool, but it may miss subtle forms of misalignment and hidden information. To better elicit hidden information during an auditing process, we introduce \emph{overthinking}: the process of using reasoning task vectors to amplify the propensity to think out loud of reasoning models. Given the parameters of a non-reasoning instruct model $M$ and reasoning-distilled model $R$, we define the \emph{overthinking model} as $\boldsymbol{\theta}_{\mathcal{O}_\alpha} = \boldsymbol{\theta}_{\mathcal{M}} + \alpha(\boldsymbol{\theta}_{\mathcal{R}} - \boldsymbol{\theta}_{\mathcal{M}})$, where $\alpha > 1$ amplifies reasoning beyond the pure reasoning model $R$. Additionally, we introduce new layer-wise attenuation strategies that selectively amplify reasoning without losing quality and coherence of model outputs. We demonstrate that overthinking models are more likely to reveal hidden information across four experimental settings, across 2B-32B models. Our findings suggest that reasoning amplification may surface secrets or unintended behaviors acquired during training up to $10\times$ more frequently than the original reasoning model. How secrets surface depends on the secret type: some require perturbation along the reasoning direction, while others yield to any sufficiently large weight perturbation.

---


### 84. [LEEVLA: Seeing What Matters in Latent Environment Evolution for Vision-Language-Action](https://arxiv.org/abs/2607.08182)

**<font color=#1a73e8>作者：</font>** Qi Lyu, Baicheng Liu, Xudong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models aim to map multimodal inputs to robot actions. However, most existing approaches struggle to cover complex dynamic scenarios due to treating all visual tokens uniformly and reasoning with human-selected factors, which lack mechanisms to emphasize task-critical evidence and ignore underlying factors. To address this issue, we propose LEEVLA, a VLA architecture for seeing what matters in Latent Environment Evolution that explicitly guides the model toward informative regions while preserving the structured evolution of latent world representations. To identify salient and instruction-relevant regions, we introduce drift-guided dynamic prioritization (DGDP), which combines dynamic position prioritization (DPP) with semantic drift guidance (SDG) to guide the VLA agent where to attend during training. On top of this, we introduce structured feature flow generation (SFFG), which models how these prioritized features should evolve in latent space via prototype-to-periphery (P2P) prediction, and a mutual-neighborhood contrastive (MC) loss to maintain topological consistency among neighborhoods. Together, DGDP and SFFG form a task-aware "where-how" training framework. Extensive experiments on VLA benchmarks show that LEEVLA consistently outperforms prior methods, confirming that explicit task-evidence guidance and structured latent reasoning are both crucial for scalable VLA. Our code is available at this https URL.

---


### 85. [Dual-Correlation Hypergraph Network for Unaligned RGBT Video Object Detection and A Large-scale Benchmark](https://arxiv.org/abs/2607.08191)

**<font color=#1a73e8>作者：</font>** Qishun Wang, Yapeng Li, Bin Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-Thermal (RGBT) Video Object Detection (VOD) has gained significant traction due to its ability to overcome the limitations of conventional RGB-based VOD under challenging conditions. However, spatial misalignment commonly exists between RGBT image pairs. To address this, we propose a Dual-Correlation Hypergraph Network (DHNet) that captures high-dimensional complementary information by explicitly modeling two types of correlations: temporal correlation across consecutive frames and spatial correlation from cross-modal features. Specifically, we first design a Patch-based Spatial Alignment Module (PSAM) to sequentially align the multimodal features at the local region level. Subsequently, we introduce a Dual Hypergraph Fusion Module (DHFM), which constructs separate temporal and multimodal hypergraphs to enhance object discriminability through dual-correlation learning. Furthermore, the field currently lacks a large-scale, scene-diverse benchmark dataset for comprehensive evaluation. To address this gap, we construct DVT-VOD1000, a large-scale RGBT VOD dataset containing 1,000 video sequences with 103,464 RGBT image pairs. The dataset covers diverse scenarios, including campuses, parks, transportation, rural areas, night scenes, rain, and snow. Comprehensive experiments on VT-VOD50 and our DVT-VOD1000 demonstrate that DHNet achieves state-of-the-art detection accuracy. The dataset and source code will be made publicly available on this https URL to support academic research.

---


### 86. [A First-Principles Theory of Slow Thinking and Active Perception](https://arxiv.org/abs/2607.08196)

**<font color=#1a73e8>作者：</font>** Hongkang Yang, Zhi-Qin John Xu, Feiyu Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As part of a series on first-principles modeling of cognitive functions, this paper attempts to provide a mathematical formulation of thinking and perception. It formally derives slow thinking or more generally, active perception, and encompasses the design, training and inference of slow thinking large language models. Our starting point is the lifting and projection of probability distributions on the observable and latent spaces, with the objective of representing complex data distributions by simple function families such as neural networks. A theory called "active lifting" is proposed, based on the sampling of latent sequences and an intrinsic drive to reduce uncertainty with maximum rate. It derives a large design space, containing the slow thinking models in a subspace that we call the static theory. These models are positioned on the representation hierarchy and sampler hierarchy induced by the static theory, and can be upgraded by climbing the two hierarchies. Active lifting further derives an inference process with an internal time axis, and a training objective that resembles minimum-length coding as well as the invention of languages. Thus, it characterizes the agency of perception, including the emergence of the slow thinking formats. Technical by-products of this theory include a three-stage pathway for improving slow thinking models, a unified approach to constructing encoders and generative models for all data modalities, a priori formation of human-like visual representations, and a possible solution to policy collapse.

---


### 87. [MLQENABLER: Enabling Secure Machine Learning Queries over Encrypted Database in Cloud Computing](https://arxiv.org/abs/2607.08197)

**<font color=#1a73e8>作者：</font>** Xu Zhou, Haoyang Chen, Xinyu Lei  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In cloud computing, the public cloud service providers (CSPs) can provide cloud storage as the primary service while providing additional machine learning (ML)-based services by using the clients' data in storage. This business model extends the border of cloud computing services and brings in new business growth possibilities. Although it is promising, the model also brings in security concerns since the public commercial cloud cannot be fully trusted. For example, the public commercial clouds may sell clients' sensitive data to the government or other companies. To address the security concerns, an immediate solution is to require clients to encrypt their datasets before outsourcing to the cloud. However, if a database is formally encrypted, then the database contains only pseudorandom numbers, making it impossible to enable ML over it. In this project, we propose MLQENABLER (ML Queries Enabler) scheme to enable secure ML queries over encrypted database in cloud storage. MLQENABLER employs an index-aid approach to achieve security and ML capability simultaneously. Our initial experiments show that MLQENABLER achieves an acceptable security level while incurring only a slight ML performance degradation.

---


### 88. [Unpaired Joint Distribution Modeling via Multi-Scale Image Representations](https://arxiv.org/abs/2607.08198)

**<font color=#1a73e8>作者：</font>** Yihang Zou, Hui Zhang, Zuowei Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies the problem of learning a joint distribution from marginal observations, which is inherently ill-posed due to the ambiguity of feasible couplings. We propose LUD-MSR, a latent-variable probabilistic framework that models the joint distribution via auxiliary representations and optimizes evidence lower bounds using only marginal data. Under mild assumptions, we establish an upper bound on the distribution approximation error. This analysis reveals a trade-off in representation learning between domain consistency and information preservation. To address this trade-off, we introduce a Multi-Scale image Representation (MSR) mapping that exploits structural similarity at coarse scales while suppressing domain-specific variations. We show that MSR achieves a more favorable balance of this trade-off compared to existing approaches. Experiments on real-world denoising benchmarks, including cryo-electron microscopy (cryo-EM), demonstrate the effectiveness of the proposed framework.

---


### 89. [TMI: Text-to-Image Meets Image-to-Image for Complementary Data Synthesis to Boost Long-Tailed Instance Segmentation](https://arxiv.org/abs/2607.08201)

**<font color=#1a73e8>作者：</font>** Hyeonseop Song, Seokhun Choi, Hoseok Do  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-vocabulary instance segmentation is constrained by long-tailed category distributions and fine-grained inter-class ambiguity. While data synthesis offers a promising alternative, current paradigms have complementary limitations: text-to-image (T2I) methods inherit noisy pseudo-labels and struggle on rare classes, whereas copy-paste methods compromise contextual realism. To address these issues, we propose a hybrid pipeline coupling T2I generation with context-aware image-to-image (I2I) editing. The T2I branch provides broad category and scene diversity, while a teacher-student scheme ensures label reliability by selectively retaining only prompt-specified categories. To strengthen supervision for rare classes, we introduce VRAIN (Verified Rare-class Augmentation via INstructed editing), a novel I2I editor. VRAIN inserts high-confidence instances at semantically appropriate locations within in-the-wild scenes, yielding semantically coherent and visually natural edits that reduce domain gaps and enable targeted augmentation. On the LVIS benchmark, our method surpasses existing baselines, improving overall AP by up to +4.0 points and rare-class AP by up to +9.5 points, while scaling effectively with backbone capacity. Our project page is available at this https URL

---


### 90. [PIT-SUN: A Deployable Empirical Marginal Transform Framework with Expectation-Consistent Recovery for Regression in Recommender Systems](https://arxiv.org/abs/2607.08202)

**<font color=#1a73e8>作者：</font>** Mingyu Zhao, Zhaohan Li, Zhenxiong Miao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating original-space conditional expectations is central to value-driven recommender systems, including dwell time, GMV, and LTV forecasting. Standard MSE is expectation-consistent in principle, but its gradients become unstable on heavy-tailed, zero-inflated, and multimodal targets, causing mean collapse and tail shrinkage. Target transformation alleviates this scale conflict, yet any useful nonlinear marginal transform loses expectation consistency under direct inversion. This is not an implementation oversight: a direct inverse-transform estimator is universally expectation-consistent only when the inverse transform is affine, which cannot simultaneously provide bounded tail compression. Existing conditionally linear recovery methods restore expectation consistency, but still leave open which coordinate, inverse lookup, recovery base, and deployment monitor should be selected for sparse complex marginals. We propose \textbf{P}robability-\textbf{I}ntegral-\textbf{TranS}formed \textbf{Un}biased recovery (\textbf{PIT-SUN}), a deployable empirical marginal recovery framework. PIT-SUN uses one empirical marginal table to define a bounded normal-score coordinate, its inverse-quantile lookup, a variance-controlled recovery base, and drift monitoring, then applies multiplicative SUN recovery to estimate the original-space expectation instead of directly inverting transformed predictions. Experiments on synthetic distributions, public benchmarks, large-scale industrial datasets, and online deployment show robust improvements in point accuracy, calibration, and ranking quality with lightweight deployment overhead.

---


### 91. [Benchmark Evaluation of Feredated Learning on Multi-organ Images](https://arxiv.org/abs/2607.08219)

**<font color=#1a73e8>作者：</font>** Junbin Mao, Xu Tian, Jianchun Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The privacy requirements of medical data and its substantial variations across organs and modalities hinder the clinical implementation of medical AI. Federated learning (FL) is a feasible approach to overcome these challenges. Due to the continuous emergence of FL algorithms and the highly heterogeneous nature of medical data, objectively evaluating their performance in real-world clinical settings remains difficult. Therefore, a comprehensive federated medical imaging benchmark, serving as a unified evaluation standard, is crucial for advancing the technology toward reliable clinical application. Existing federated medical imaging benchmarks have not yet adequately incorporated state-of-the-art algorithms, are limited to data from single organs or modalities, and overly emphasize model accuracy, making it difficult to comprehensively assess the overall efficacy of FL in real-world medical environments. To address these challenges, we developed the MobenFL benchmark. This benchmark integrates 20 cutting-edge FL algorithms and 22 medical imaging datasets, covering 12 critical organs across the human body, surpassing existing benchmark in breadth. In terms of evaluation dimensions, MobenFL not only assesses performance but also systematically incorporates key metrics such as algorithmic efficiency and privacy protection capabilities. Additionally, it conducts specialized evaluations for complex real-world clinical scenarios involving different diseases, devices, and imaging modalities, thereby providing a comprehensive and in-depth evaluation framework for the clinical application of FL in the medical field.

---


### 92. [Threshold Authorization Without Threshold Signatures: Signature-Agnostic MPC Custody](https://arxiv.org/abs/2607.08226)

**<font color=#1a73e8>作者：</font>** Dariia Porechna  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital-asset custody has been built on threshold multi-party approval: no operation proceeds unless $t$ of $n$ parties approve, and fewer than t compromised parties can neither authorize nor learn the authorization secret. Threshold signature schemes (TSS) have been the standard mechanism, but the post-quantum transition disrupts this model: standardized hash-based signatures resist efficient threshold signing, and lattice-based threshold protocols remain an emerging research track.
We present a dual-gate architecture that separates member authentication from threshold authorization. Each member signs its approval with an ordinary signature under any EUF-CMA scheme; the quorum jointly produces a threshold seal from Shamir-shared secrets bound to the operation. The seal is the base instance of a programmable authorization computation: simple quorum is the minimal policy, while richer policies can evaluate secret-shared state without making the member-signature scheme part of that computation. The signature scheme is a deployment parameter: migrating from ECDSA to SLH-DSA or ML-DSA is a key rotation, not a protocol redesign, and members holding keys in commodity HSMs participate through the standard sign API. The architecture can be deployed wherever the asset-control path supports programmable verification, such as smart contracts, vault modules, or HSMs guarding a master key, and produces an enforcement-layer authorization rather than a native chain signature. Below-threshold secrecy is information-theoretic; an adversary holding $\geq t$ signing keys but no coefficient shares still cannot produce the seal.

---


### 93. [Mini-Programs, Mega-Problems: Unveiling OAuth-based Authentication Misuses in Mini-Programs via Dynamic Analysis](https://arxiv.org/abs/2607.08232)

**<font color=#1a73e8>作者：</font>** Zidong Zhang, Zhentao Xie, Lingyun Ying 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mini-programs have become a dominant paradigm for lightweight application deployment within super apps such as WeChat. To support seamless integration, super apps provide OAuth mechanisms for user login. However, improper integration of OAuth-based Authentication (OBA) flows by third-party developers can lead to critical security flaws. In this paper, we discover three new types of runtime OBA misuses that differ from prior static-code-based studies, enabling attackers to impersonate victims. To assess their real-world impact, we design and implement MINIAUTH, the first analysis framework for systematically analyzing OBA misuse at scale. MINIAUTH automatically pinpoints the OBA login page of a mini-program, executes the workflow dynamically, and analyzes its runtime behaviors. This enables it to handle obfuscated mini-programs and uncover vulnerabilities that existing approaches cannot detect. Applying MINIAUTH to 44,273 WeChat and 2,721 Baidu mini-programs, we uncover 1,834 misuse cases, including critical logic flaws that enable client-side identity forgery via exposed credentials and authentication bypass through static or plaintext identifiers. Our cross-platform evaluation further shows that such misuses are not confined to a single ecosystem but consistently appear across different mini-program platforms. We also identify a cryptographic design flaw in Baidu's OBA APIs that allows brute-forcing of session keys. We responsibly disclosed our findings to the developers and platforms, receiving acknowledgments and assigned CNVD/CNNVD IDs. These results underscore the need for more robust developer guidance and enhanced platform-level safeguards.

---


### 94. [Playing ZendoWorld: Challenging AI Agents on Active Visual Concept Induction](https://arxiv.org/abs/2607.08233)

**<font color=#1a73e8>作者：</font>** Sophia Koehler, Antonia Wüst, Inga Ibs 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A central challenge in building intelligent systems is enabling agents to jointly perceive complex inputs, form hypotheses about hidden patterns, and design informative experiments to test them. To study this problem, we propose ZendoWorld, a controlled interactive environment in which agents must infer a logical rule about visual game observations, acquire information by proposing new scenes, and refine their hypotheses based on feedback from the game environment. We evaluate several agents spanning pure VLM reasoning, Bayesian particle filtering, dynamic concept discovery, and neuro-symbolic methods. Our main findings are: (1) high accuracy in predicting labels for observed examples does not imply recovery of the underlying rule; (2) perception and induction are distinct bottlenecks for different agent classes; and (3) VLM-based agents propose near-uninformative experiments, failing to actively reduce hypothesis uncertainty. To compare these results, we collect human data on the task, which reveals a gap in inductive reasoning, particularly for more complex rules. Overall, ZENDOWORLD takes an important step toward evaluating intelligent agents and identifies concrete avenues for improvement, particularly in domains like scientific discovery.

---


### 95. [RhyMix: A Lightweight Adaptive Multi-Rhythm Network for Long-Term Time Series Forecasting](https://arxiv.org/abs/2607.08234)

**<font color=#1a73e8>作者：</font>** Sumit Satishrao Shevtekar, Chandresh Kumar Maurya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time series exhibit complex dynamics characterized by multiple simultaneous temporal patterns: short-term fluctuations, periodic seasonal cycles, long-term trends, and irregular abrupt changes. However, many existing forecasting architectures rely on single-path temporal modeling--transformers capture long-range dependencies but smooth local variations, convolutions capture local patterns but have limited receptive fields, and linear models are efficient but cannot capture nonlinear dynamics. To address this, we introduce RhyMix (RHYthm MIXture), a hybrid neural architecture designed around a parallel dual-path modeling paradigm with adaptive gating mechanisms. RhyMix integrates two complementary encoding branches: (i) a Cyclic Path that incorporates explicit seasonal inductive bias through learnable cyclic embeddings, capturing predictable rhythmic patterns; and (ii) a lightweight Multi-Scale Temporal Convolutional Network with Channel Attention Path that employs multi-scale depthwise dilated convolutions to capture temporal dependencies across different receptive fields. A key innovation is the use of adaptive gating at multiple levels: a path gate dynamically combines four specialized forecasting heads (Direct, Trend-Seasonal Decomposition, Local Convolution, and Periodic Fusion) per sample and channel, while a hybrid gate adaptively balances the Cyclic and MSTCN-CA Paths based on input characteristics. This design ensures the model adapts to specific temporal patterns while maintaining linear complexity in sequence length, channels, and prediction horizon. Across extensive benchmarks on 12 real-world datasets for long-term forecasting, RhyMix achieves state-of-the-art performance on 10 of 12 datasets. The model remains lightweight (~40K params) with linear complexity and low-latency inference (<5ms),suitable for resource-constrained edge devices and real-time deployment.

---


### 96. [TVTA: Trajectory-Aware Viseme-Guided Temporal Aggregation for Event-Based Lip Reading](https://arxiv.org/abs/2607.08236)

**<font color=#1a73e8>作者：</font>** Jingrong Zheng, Hongwei Ren, Xiangqian Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based lip reading has recently emerged as a promising direction for visual speech recognition, benefiting from the high temporal resolution and motion sensitivity of event cameras. However, existing methods typically perform spatial compression before sufficient temporal modeling, which may suppress sparse and localized motion trajectories that are crucial for distinguishing similar lip movements. Moreover, most current approaches optimize temporal representations mainly at the word-classification level, leaving the underlying articulatory structure weakly constrained. To address these limitations, we propose a temporally enhanced framework for event-based lip reading. First, we introduce Trajectory-Aware Differential Aggregation (TDA), which performs local temporal modeling at each spatial location before adaptive spatial aggregation. Second, we propose Viseme-Guided Aggregation (VGA), a unified temporal module composed of a CTC decoder and a viseme-guided gated aggregation branch, which injects viseme-aware sequence supervision and improves final temporal aggregation for word recognition. Third, we incorporate an EMA teacher--student training strategy to enhance robustness under strong event perturbations. Experiments on the DVS-Lip benchmark verify the effectiveness of the proposed design, and extensive ablation studies further validate the contributions of TDA, VGA, and teacher--student consistency. Qualitative decoding results also demonstrate that the proposed CTC-based temporal modeling learns meaningful viseme-aware structure from event streams.

---


### 97. [Structure Learning on Clustered Data](https://arxiv.org/abs/2607.08238)

**<font color=#1a73e8>作者：</font>** Ryan Thompson, Matt P. Wand, Veerabhadran Baladandayuthapani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent algorithmic advances have made directed acyclic graph (DAG) structure learning scalable for causal discovery. Yet, the currently available techniques assume a completely homogeneous population, precluding their application to clustered data where cluster-specific variations (e.g., patient-specific effects) are common. We address this issue by introducing a new approach that estimates a global structure while accounting for local cluster-level effects. The key idea is to extend the fixed- and random-effects framework of classical mixed models to the structure learning setting. Towards this end, we present a differentiable graph coupling mechanism that guarantees the union of the fixed- and random-effects graphs remains acyclic. Computationally, we provide a provably convergent first-order method and leverage efficient batched updates across clusters. Statistically, we establish identifiability of the model and show that our approach recovers the true structure asymptotically. In experiments on real and synthetic data, our proposal detects dependencies missed by alternative estimators, underscoring its value for structure learning in clustered settings.

---


### 98. [Closing the Null Space: Guidance-Aware Quantization for Classifier-Free Diffusion](https://arxiv.org/abs/2607.08241)

**<font color=#1a73e8>作者：</font>** Abdullah Al Shafi, Sumaiya Rahim Suma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying classifier-free guidance (CFG) diffusion models under real-world compute budgets requires quantization, yet existing post-training quantization (PTQ) methods treat CFG models as single-branch networks, ignoring the paired conditional/unconditional structure that CFG inference fundamentally relies on. This structural blind spot has two consequences. At the system level, the two-pass CFG execution pattern imposes a latency overhead that parameter-count and bit-operation metrics conceal entirely, and commodity INT8 inference stacks fail to realize the theoretical efficiency gains that BOPs calculations promise. At the algorithmic level, calibrating against the guidance gap alone admits an exact null space: a quantized model can achieve perfect gap-fidelity diagnostics while the unconditional branch drifts arbitrarily, corrupting every guided prediction at inference time. This paper terms this the branch-drift trap, proves its existence analytically, and confirms it empirically through a false-positive result in which the best-calibrated model by standard diagnostics simultaneously produces the worst sample quality. To close the trap, Guidance-Aware Mixed Precision (GAMP) is proposed, which calibrates directly on the guided prediction, derives per-layer activation-bit sensitivity from guided-output degradation, and allocates bits via a greedy knapsack -- provably preventing unconditional branch drift by construction.

---


### 99. [An interpretable Good--Turing restart criterion for k-means++](https://arxiv.org/abs/2607.08243)

**<font color=#1a73e8>作者：</font>** Renato Cordeiro de Amorim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The k-means++ algorithm is commonly restarted multiple times to avoid poor local optima, yet the number of restarts is almost always chosen arbitrarily and applied uniformly regardless of data set difficulty. This undermines any comparison relying on such a choice and wastes computation on easy data sets while potentially under-serving hard ones. We introduce GTRC, a restart criterion combining a Good-Turing estimate, a proven unconditional bound, and a confidence-based bound on the probability that a further restart would improve on the current result, stopping once this probability falls below a user-specified tolerance $\varepsilon$. Across 36 data sets, GTRC reached clustering quality competitive with well-chosen fixed restart counts, while the number of restarts used varied considerably and appropriately with data set difficulty, governed by an interpretable, data-dependent signal rather than a fixed rule. GTRC offers a principled and reportable alternative to fixing the number of $k$-means++ restarts in advance. Software:this https URL.

---


### 100. [SkelGen4D: Weakly-Supervised Skeleton-Based 4D Generation for Text-Driven Mesh Animation](https://arxiv.org/abs/2607.08246)

**<font color=#1a73e8>作者：</font>** Hao Feng, Zhi Zuo, Jia-Hui Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study 4D generation to synthesize temporally coherent sequences of 3D geometry for animation and content creation. In contrast to existing SDS-based optimization methods and video-driven animation approaches, we adopt a skeleton-driven animation framework aligned with standard industrial pipelines, which enables explicit control and editing. To this end, we propose SkelGen4D, a weakly supervised feed-forward framework for text-driven mesh animation that generates explicit skeleton motions without requiring per-frame skeleton annotations. SkelGen4D first recovers temporally consistent pseudo-skeletons from animated meshes via differentiable fitting, and then generates text-conditioned skeleton motion sequences in a feed-forward manner, further refined with Motion-GRPO to ensure temporally coherent, physically plausible, and articulated animation. We evaluate our method on two large-scale benchmarks, Truebones Zoo and Diffusion4D. Our results show that our weakly supervised skeleton modeling matches or surpasses fully supervised baselines while scaling to diverse object categories for high-quality text-driven mesh animation. Further, our method supports flexible motion editing and is aligned with standard animation production pipelines.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-189](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
