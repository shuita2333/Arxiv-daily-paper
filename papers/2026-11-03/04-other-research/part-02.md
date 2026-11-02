# 📦 其他研究 | 2026年11月03日

> 本类共 **193** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-193](./part-04.md)

---

### 51. [Differential rank preservation manifold learning](https://arxiv.org/abs/2610.41107)

**<font color=#1a73e8>作者：</font>** Henry Han, Luyu Niu, Diane Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Manifold learning methods like t-SNE and UMAP preserve local neighborhoods, but they do not preserve the ranking of the neighbors inside them. Two embeddings can return the same neighbor set while disagreeing on which point is closest. This loss of order degrades downstream applications that value the order in the embedding. We propose Smooth Rank t-SNE (SR-tSNE), which adds a differentiable rank term to the standard t-SNE loss. To enable efficient training, this term uses a sigmoid rank approximation to explicitly force a point's true high-dimensional neighbors to outrank unrelated intruders and retain their original order. We also introduce Ordinal DLP (O-DLP), an extension of the Degree of Locality Preservation (DLP) metric that credits a neighbor only when it returns at its original rank. Across eight benchmarks spanning image, text, speech, remote-sensing and single-cell data, SR-tSNE outperforms 12 baselines in rank preservation and neighborhood overlap. Ablation studies demonstrate our rank term alone boosts O-DLP by 5% to 28%, a gain not achievable using standard pairwise loss. This advantage transfers to downstream applications. SR-tSNE achieves the best label-transfer performance across seven vision datasets. For cell-type discovery across six single-cell datasets, it ranks first in 17 of 18 dataset-metric combinations, whether clustering resolution is selected with or without cell-type labels. In intraday trading, SR-tSNE achieves higher returns, lower risk, and lower turnover than the baselines. To our knowledge, SR-tSNE is the first t-SNE-family method with explicit order preservation.

---


### 52. [An Empirical Study on Learning Rooftop Solar Potential from Satellite Imagery Directly Without Explicit Geometry](https://arxiv.org/abs/2610.41111)

**<font color=#1a73e8>作者：</font>** Joshua Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rooftop solar potential estimation often relies on LiDAR, digital surface models (DSMs), or pipelines that explicitly reconstruct roof geometry before estimating solar potential. We propose Direct Rooftop Solar Prediction (DRSP), an end-to-end formulation that maps satellite imagery and coarse regional sunlight information directly to application-level solar outputs. DRSP neither requires explicit geometric representations as input nor predicts roof orientation, slope, height, DSMs, or other geometric quantities as intermediate outputs, and therefore requires no geometric intermediate supervision. To enable large-scale study of this formulation, we develop a programmatic data-curation pipeline that converts per-panel information from the Google Solar API into usable-rooftop masks and spatial solar-energy targets, yielding two geographically distinct datasets containing approximately 60K rooftops from the U.S. Midwest and 87K from Texas. We demonstrate the feasibility of DRSP and systematically characterize the effects of geographic training distribution, model depth, image resolution, regional sunlight conditioning, and heatmap regression objectives. Overall, our results suggest that useful rooftop-scale solar information can be learned directly from 2D imagery without explicit geometric intermediate representations, offering a simpler path toward large-scale solar assessment. Our code and dataset are available at this https URL.

---


### 53. [MotorSense: A Video-EMG Dataset of Motoric Representations for Action Understanding](https://arxiv.org/abs/2610.41127)

**<font color=#1a73e8>作者：</font>** Eadom Dessalene, Michael Maynord, Amir-Hossein Shahidzadeh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer vision models learn hand action only from its visual consequences, without access to the underlying embodied motor signals. We address this absence with MotorSense, the first large-scale paired egocentric video and surface electromyography (EMG) dataset. MotorSense pairs bimanual EMG bands with egocentric video and yields synchronized video, bimanual EMG and IMU, and audio across 100 hours of unscripted manipulation. EMG offers a powerful scalable alternative to manual annotation: it captures finger movement, hand configuration, and the forces exerted between hand and environment as a dense signal free of occlusion and labeler bias, whereas manual annotation is costly, subjective, and unreliable under occlusion. We use MotorSense to learn sensorimotor alignment, producing an organization of action that is shared across the visual and motoric spaces, through cross-modal pre-training between video and EMG. The resultant vision models are then transferred to downstream tasks that benefit from sensorimotor alignment: in this case, action recognition, 3D hand reconstruction, and 3D contact reconstruction. We further demonstrate a generative application in which EMG motor signals are used to condition a video diffusion model, yielding videos of fine-grained hand manipulation. Across four action-centric computer vision tasks and eight popular video datasets, we demonstrate that sensorimotor alignment provides a stronger foundation for visual representation learning than conventional self-supervised learning methods over video, outperforming every baseline across all tasks and datasets evaluated.

---


### 54. [Who Swept My ETH? Uncovering EIP-7702-Based Ether Redirection Attacks on Ethereum](https://arxiv.org/abs/2610.41153)

**<font color=#1a73e8>作者：</font>** Ziwei Li, Tianwei Chen, Jiajing Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> EIP-7702 introduces a new transaction type that allows Externally Owned Accounts (EOAs) on major EVM-compatible chains to delegate execution to arbitrary contract codes temporarily. While enhancing functionality, this mechanism facilitates a novel threat: the \underline{E}IP-7702-Based \underline{E}ther \underline{R}edirection \underline{A}ttack (EERA). In such an attack, a victim is delegated to a malicious sweeper contract, which automatically redirects incoming ETH transfers to an address controlled by the attacker. As a nascent attack paradigm arising from protocol evolution, the underlying mechanisms and security implications of EERA remain systematically unexplored. To bridge this gap, we provide the first formal analysis of the EERA attack model and propose SweeperHunter, a framework that detects these attacks through transaction analysis. By evaluating transactions from the first ten months following the introduction of EIP-7702 on Ethereum mainnet, we have identified 4,668,209 malicious delegations, 20,443 attack transactions and 508 ETH sweeper contracts, forming the first EERA dataset. Finally, we analyze this attack from both attacker and victim perspectives, derive key insights, and propose corresponding mitigation strategies. We reveal the prevalence of EERA, as approximately 70\% of the observed delegations point toward ETH sweeper contracts. Furthermore, we observe a notable lack of effective responses from victims; specifically, over 600,000 accounts failed to revoke or update their malicious delegations promptly, thereby remaining in a state of vulnerability. Our research is expected to facilitate understanding and mitigation of this emerging threat posed by EIP-7702.

---


### 55. [Lifelong Learning of Scheduling Rules with Surrogate-assisted Genetic Programming for Dynamic Flexible Job Shop Scheduling](https://arxiv.org/abs/2610.41158)

**<font color=#1a73e8>作者：</font>** Luyao Zhu, Fangfang Zhang, Yi Mei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Genetic programming (GP) has been widely used to learn scheduling rules for dynamic flexible job shop scheduling (DFJSS). However, trained rules tend to only generalise to tasks of similar scales and distributions, and when task characteristics change, learned rules often suffer significant performance degradation. Moreover, fine-tuning pre-trained rules on new tasks often leads to catastrophic forgetting, where prior knowledge is lost. This motivates the need for GP methods that can adapt to new tasks while preserving past knowledge, leading to a lifelong learning paradigm. However, lifelong learning in GP for DFJSS remains largely under-explored. To address this gap, this paper proposes a surrogate-assisted GP method for lifelong learning to handle sequential heterogeneous DFJSS tasks with job or batch arrivals. The framework includes three key components: an adaptive two-stage training strategy to balance plasticity and stability, a task-similarity-based weighting mechanism to regulate knowledge reuse, and an improved surrogate model with distance constraints to enhance estimation accuracy. Experimental results show that the proposed method effectively mitigates catastrophic forgetting while maintaining strong adaptability, outperforming several compared methods and demonstrating the potential of lifelong GP in dynamic scheduling environments.

---


### 56. [MATS: A Multi-Agent Framework for Controllable and Reflective Tumor Synthesis](https://arxiv.org/abs/2610.41159)

**<font color=#1a73e8>作者：</font>** Zhongnan Shi, Keyang Zhou, Siyi Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing realistic tumors on medical images helps address data scarcity for clinical AI. Existing diffusion-based methods, however, lack fine-grained attribute-level controllability, closed-loop quality verification, and awareness of which morphological patterns are underrepresented in the target distribution. We present MATS, a multi-agent framework for text-controllable, cross-organ tumor synthesis. Given a target disease, MATS first profiles its morphological distribution over a fine-grained attribute space covering tumor geometry and appearance, and constructs a generation plan that amplifies underrepresented subtypes while keeping common ones dominant. It then localizes the target organ, proposes anatomically valid placement, and executes two-stage diffusion to produce the tumor mask and render texture, each conditioned on the corresponding attributes. A closed-loop reflective mechanism verifies attribute alignment at three checkpoints throughout synthesis and provides targeted feedback to guide re-generation when misalignment is detected. Trained exclusively on a single-source pancreatic neuroendocrine tumor dataset, MATS consistently improves downstream segmentation both in-domain and across LiTS, KiTS, and MSD-Pancreas benchmarks, whereas most prior generative augmentation methods fall below real-only training.

---


### 57. [CAP: Learning to Optimize from Sparse Observations of Related Tasks](https://arxiv.org/abs/2610.41173)

**<font color=#1a73e8>作者：</font>** Lin Fu, Siwei Fu, Dong Ni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In experiment-driven black-box optimization, each evaluation can consume materials, equipment time, and other resources, limiting the number of experiments available for a new task. Records from completed related optimization campaigns could help, but learning a sequential query policy remains challenging when task-specific experience consists of only a few sparse histories. We propose CAP (Candidate Acquisition Policy), which models shared structure and task-specific variation in fixed historical records to sample interactive practice functions. On these functions, CAP learns a feedback-conditioned query policy aimed at final optimization performance under a fixed evaluation budget. At deployment, its parameters remain fixed while each new observation informs the next query. Across five synthetic task families spanning 6 and 20 dimensions and two engineering simulation benchmarks, BOPTEST and SU2, CAP attains the lowest median final-budget value among the reported methods on four synthetic families and both engineering benchmarks. These results indicate that sparse records from completed related tasks can support adaptive query decisions on new tasks, making more effective use of limited, costly experimental evaluations.

---


### 58. [S2TDR: Structured Multimodal Reconstruction for Sticker-Aware Dialogue Understanding](https://arxiv.org/abs/2610.41176)

**<font color=#1a73e8>作者：</font>** Yuanchen Shi, Fang Kong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stickers are widely used in social media dialogues to express affect, stance, and intent beyond literal text. Their meanings are often non-literal and context-dependent, making them difficult to handle with generic visual fusion or standalone captioning. We propose Sticker-to-Text Dialogue Reconstruction (S2TDR), a structured multimodal reconstruction framework that converts sticker turns into contextually appropriate textual utterances. S2TDR decomposes sticker interpretation into visual cue extraction, affective-intent inference, and context-aware dialogue reconstruction, using OCR text only as an auxiliary cue when available. The reconstructed dialogue can then be consumed by existing text-based dialogue models. Experiments on sentiment analysis, intent recognition, and dialogue summarization show that S2TDR generally improves multiple downstream models over direct sticker integration methods. Further analyses on component ablations, OCR-empty stickers, and reconstruction quality indicate that structured reconstruction provides an interpretable and effective way to integrate sticker semantics into dialogue understanding.

---


### 59. [General Frequency Principle for Linear Approximation Classes](https://arxiv.org/abs/2610.41179)

**<font color=#1a73e8>作者：</font>** Yujun Wang, Yiqi Gu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study a general frequency principle under gradient descent training for the finite linear approximation classes. Under suitable assumptions, we prove that the learner amplitude relative to the target amplitude vanishes at high frequencies, uniformly throughout training. We also establish sufficient conditions for low-frequency priority, covering single-frequency targets trained separately and two frequency components trained in the same run. This general frequency principle does not imply that lower frequencies always converge faster. Instead, for two frequencies that satisfy certain comparison conditions, one component will take longer to learn than the other; and in common cases, the longer component has higher frequency. Numerical experiments with Legendre and trigonometric bases validate the theoretical results.

---


### 60. [FlowMoDE: Coarse-to-fine Flow Matching for Detail-aware Sim-to-Real Monocular Depth Estimation](https://arxiv.org/abs/2610.41190)

**<font color=#1a73e8>作者：</font>** Liangjing Shao, Wanhao Liu, Jinsong Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation is a fundamental capability for 3D spatial perception in robotic and intelligent systems. While data-driven discriminative methods have achieved compelling performance for monocular depth estimation, generative approaches can reconstruct fine structural details with stronger generalization. However, most existing generative diffusion models suffer from low inference efficiency caused by multi-step sampling, whereas single-step diffusion models struggle to recover high-fidelity depth maps. To mitigate these drawbacks, this paper presents FlowMoDE, a coarse-to-fine flow-matching-based framework for efficient, structure-aware monocular depth estimation supporting sim-to-real and cross-scene generalization. The core architecture first conducts coarse-level decoding conditioned on diffused features extracted from a pre-trained semantic encoder, and subsequently restores fine-grained structural patterns via expanded decoding layers. Trained exclusively on a single synthetic indoor dataset, our proposed method outperforms prior methods across five real-world indoor and outdoor datasets, yielding an average 14.1% reduction in relative error against state-of-the-art works as well as 9.9\% reduction in chamfer distance for point cloud reconstruction. We further validate the generalization capability of FlowMoDE on realistic robotic scenes, with qualitative comparisons against state-of-the-art methods. The project page is this https URL

---


### 61. [Role-Aware Server Optimization for Multimodal Federated Learning with Missing Modalities](https://arxiv.org/abs/2610.41193)

**<font color=#1a73e8>作者：</font>** Liuyin Shi, Wenbo He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal federated learning (MFL) trains a shared model by aggregating client updates without exchanging raw data. Under missing modalities, clients adapt active modality encoders and a shared prediction block (fusion and classifier) to different input subsets. This raises two server-side questions: which clients should contribute to each component, and how should their aggregates be incorporated across rounds? We observe that an absent-modality encoder can still adapt through missing-input handling. Availability- based aggregation can therefore omit its update while retaining jointly learned prediction-block updates. Contributor selection also shapes server momentum, a weighted history of aggregated updates. We observe that prediction-block momentum can improve or reduce performance depending on the encoder update policy. We therefore propose Role-Aware Server Optimization (RASO), which coordinates contributor selection with role-specific server updates. RASO selects contributors through prediction dependence and inclusion in local optimization, retains encoder momentum, and synchronizes the shared prediction block to its current aggregate. Experiments across datasets and fusion architectures demonstrate the effectiveness of RASO under missing modalities.

---


### 62. [Beyond CLIP: Calibrated (Few-Shot) Defect Detection With System One Decision Models](https://arxiv.org/abs/2610.41199)

**<font color=#1a73e8>作者：</font>** Fadel M. Megahed, Ying-Ju Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cameras and vision sensors are widely used for product and process inspection in manufacturing environments. Traditionally, this process required thousands of images of both nominal and defective products to train such models. Recent research shows that vision transformer (ViT) models, such as CLIP, can reduce this requirement to 50-100 images per nominal and defective class. However, collecting even 50 defective images can be difficult in high-yield or low-volume manufacturing processes. In this paper, we examine the utility of two recently proposed structured decision models (Jev and Clef-Flash) in applications using as few as k=2 reference images per class at inference. In the process, we provide three main contributions: (a) a framework for k-shot learning of these models for image classification/inspection applications; (b) an agentic approach for automatically refining the text descriptions that guide image classification in these decision models; and (c) an approach to calibrate the resulting defect probabilities to improve their reliability for inspection decisions. We test these contributions in five manufacturing case studies. Using two reference images per class, both Jev and Clef-Flash outperform CLIP's test accuracies with the same references (0.75-1.00 [Jev] and 0.71-0.99 [Clef-Flash] vs 0.67-0.84 [CLIP]). Furthermore, we show that our agentic refinement of text descriptions significantly improves accuracy across 6 of 8 model-application combinations, and our calibration approach reduces the Brier score in 13 of the 15 model-application configurations. To support the reproducibility of our work, we provide our replication code and have created the R "decisions" package for evaluating additional models. We also provide a publicly available web app that allows practitioners to inspect their own images with no code.

---


### 63. [Shifting Focus by Reliability: Geometric Fusion Modulation for Robust RGB-T Detection](https://arxiv.org/abs/2610.41204)

**<font color=#1a73e8>作者：</font>** Liuyin Shi, Chengqi Li, Wenbo He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-thermal (RGB-T) object detectors combine visible and thermal imagery for robust detection, but signal corruption in either stream can substantially degrade accuracy. Restoration-based methods incur significant latency and do not consistently improve downstream accuracy, raising a more direct question: rather than restoring corrupted inputs, can we efficiently adapt the detector to their varying signal quality? Conventional PEFT offers an efficient route, but its input-independent corrections cannot track diverse test-time corruptions. Our controlled corruption sweeps show that corruption types have similar effects near clean conditions but diverge increasingly with severity, motivating corruption-aware, per-input adaptation. We therefore propose PG-FM (Prompt-Guided Feature Modulation), which adapts RGB-T object detectors to the estimated corruption type and severity of each modality. Under controlled RGB-T corruption simulations, PG-FM preserves clean-set performance, improves mAP50 by up to 20.8 points on FLIR and 19.9 points on KAIST, and transfers without retraining to unmodified, naturally acquired external RGB-T datasets.

---


### 64. [Beyond Scarcity: When Encoder Adaptation Is Worthwhile](https://arxiv.org/abs/2610.41213)

**<font color=#1a73e8>作者：</font>** Zexing Zhang, Jichao Li, Tianyang Lei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-tailed recognition often learns a shared representation before correcting the classifier for class imbalance. Once the classifier has been rebalanced, however, final accuracy does not reveal whether further encoder adaptation remains worthwhile. Standard imbalance benchmarks obscure this question because they jointly vary the number of distinct examples available to rare classes and the frequency with which those examples shape the representation. We introduce a controlled evaluation framework that separates unique support from representation allocation and estimates the incremental value of encoder updates through matched classifier-only and full-network continuations from a common corrected model. The framework combines stage-specific controls, multiple representation and adaptation objectives, whole-distribution metrics, and hierarchical inference over class assignments, support reconstructions, and optimization runs. Across the controlled study, the same low-support regime moves from one in which classifier-only training is adequate to one in which encoder adaptation yields a practically meaningful benefit solely as representation allocation becomes more imbalanced. The transition persists across classifier corrections, representation objectives, normalization and augmentation controls, and ImageNet-scale evaluation, while preserving frequent-class accuracy. Under the prespecified one-percentage-point operating margin, the two regimes are separated by simultaneous confidence bounds. These results show that benchmark construction can alter a post-correction training decision and that support size alone does not characterize the remaining value of representation adaptation.

---


### 65. [A Positional Realizability Theory of Length Generalization in Single-Head Attention](https://arxiv.org/abs/2610.41218)

**<font color=#1a73e8>作者：</font>** Jiasong Han, Yunkai Chai, Jintao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Why does length generalization (LG) depend so sharply on the positional encoding (PE)? Relative schemes extrapolate fixed offsets, absolute schemes fix positions, and neither handles growing offsets. We give a realizability theory for a deliberately controlled abstraction, a single positional-only attention head, that derives this well-documented empirical pattern and says precisely where it holds and breaks. The device is a simulation transfer operator $T_L$ that re-evaluates a selected length-$L_0$-realizing positional kernel on the longer grid, with a scalar $\alpha_L \in [0,1]$ read off before any training from $(\Phi, t_n)$ alone. Here $\alpha_L$ serves as the computable witness of that taxonomy's derivation, not as a stronger empirical predictor. Our results are a relative-head deep-row characterization for kernels with a strict unique global maximizer (Theorem 2), an absolute/relative duality that derives the pattern (Proposition 4), a learned-absolute underdetermination result, and a static expressivity bound; a sufficiency theorem (Theorem 1) bridges $\alpha_L$ to LG, and the general deterministic case is a precise open conjecture (correcting a tempting but invalid "outside-colspan" argument). Experiments confirm the structure: in the controlled single-head regime $\alpha_L$ exactly separates the taxonomy's generalizing and non-generalizing (PE, task) cells (2625 trained-model measurements; stable at vocab 64/d=128). Together, these results turn the received PE taxonomy into a positional-kernel transfer theorem, and identify the content and depth mechanisms that escape it. The theory concerns the positional channel alone: tasks whose targets depend on token content, including the standard length-generalization suite such as addition and sorting, fall outside Theorem 2.

---


### 66. [Corroborative Learning: Mutual Enhancement through Task-Response Reconstruction](https://arxiv.org/abs/2610.41222)

**<font color=#1a73e8>作者：</font>** Zexing Zhang, Jichao Li, Tianyang Lei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In pattern analysis, models trained independently for the same task often develop complementary capabilities through differences in architecture, data, and optimization. Exploiting complementarity while retaining independent deployment is central to collaborative learning. Most methods establish transfer by reducing differences in predictions, relations, or representations between target and collaborator, although these differences also underlie complementarity. This creates a structural trade-off between reducing differences for knowledge exchange and preserving them for complementarity. We therefore propose Corroborative Learning (CL). Each model forms task-driven responses, with cross-group support from its collaborator. Source-excluded reconstruction of response increments from collaborator representations separates fitting and evaluation across disjoint groups and selectively constrains directions by cross-group reconstructability. The process requires no direct output or feature matching or additional inference dependency. Furthermore, with linear reconstruction and fixed collaborator representations, the loss equals a positive semidefinite directional regularizer, constraining less reconstructable directions more strongly. Signal and noise conditions characterize when directional shrinkage reduces response-estimation error. Across six language tasks, 24 models, and 36 pairs, CL improves over capacity-matched independent adaptation on every task, with positive gains across most directed model combinations. Pairwise comparisons show broad advantages over transfer and mutual-learning methods and different gains from complementarity across collaboration rules. Low-label language and vision results support cross-domain applicability. Task-relevant differences can support mutual enhancement without eliminating disagreement.

---


### 67. [Imputing Missing Data in Longitudinal Life-Logging Athlete Data](https://arxiv.org/abs/2610.41226)

**<font color=#1a73e8>作者：</font>** Saaz Kaur Sahdra, Kalina Yacef, HaeJin Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Long-term, diverse personal informatics data enables athletes to understand and act on their health and performance goals, whether assessing readiness right now, tracking how soreness relates to training load over time, or predicting how sleep affects next-day performance. However, the inherent missingness in longitudinal data, if handled inappropriately, can bias these analyses. To our knowledge, no prior work has systematically benchmarked classical and deep learning imputation methods on long-term self-tracking data from athlete populations. We evaluate six imputation methods across four missingness mechanisms at missingness rates spanning 10-80%. Using seven diverse long-term self-tracking datasets from 231 individuals, we assess both point accuracy and the preservation of temporal and multivariate structure. Our results show that no single method dominates across all conditions and reveal a critical trade-off: while PAIN is superior on point-wise accuracy, deep learning methods (BRITS, GRU-D, and GRIN) are better at preserving multivariate and temporal structure, particularly under higher missingness. Our findings offer a practical, goal-conditioned framework that guides researchers in selecting imputation strategies aligned with both the underlying missingness mechanism and the specific analytical goal of long-term self-tracking studies.

---


### 68. [Coarse3D: Controllable and Faithful Sparse Structure Generation for Image-to-3D](https://arxiv.org/abs/2610.41231)

**<font color=#1a73e8>作者：</font>** Gaige Wang, Bowen Pan, Hao Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coarse-to-fine 3D-native generation relies heavily on the first-stage sparse structure, which determines the global orientation and overall geometry for subsequent refinement. However, existing coarse generators suffer from two key limitations: their orientation is difficult to control due to ambiguous semantic canonicalization, and their structures are often inconsistent with input images due to weak 2D-3D grounding. We propose Coarse3D, a sparse-structure generation model that produces orientation-controllable and structurally faithful voxel geometry from arbitrary unposed images. Coarse3D introduces three designs: a first-frame anchored canonical space that aligns generation with the first input view while preserving object-centric normalization; a dual-tower DiT that couples generation with auxiliary feed-forward reconstruction to learn spatially grounded features; and spatial-prior guided attention that regularizes cross-attention with pixel-to-voxel correspondence. Coarse3D can directly replace the coarse stage of existing pipelines. Experiments show that it substantially improves sparse structure quality and consistently enhances final 3D generation, achieving state-of-the-art performance.

---


### 69. [Generative SDEs with Trainable Diffusion and Density-Based Losses](https://arxiv.org/abs/2610.41243)

**<font color=#1a73e8>作者：</font>** Angxiu Ni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a divergence-kernel method for jointly optimizing neural SDE drift and diffusion fields and the initial Gaussian distribution, using losses that depend directly on the terminal density. In two- and eight-dimensional Gaussian-mixture experiments, we learn time-independent fields and obtain far fewer off-mode samples than score-based generators with similar parameter counts. The drift attracts samples toward the modes, while the diffusion helps disperse excess probability between them.

---


### 70. [A Unified Framework for Probability Estimation of Data-Dependent Events](https://arxiv.org/abs/2610.41244)

**<font color=#1a73e8>作者：</font>** Vitaly Feldman, Satyen Kale, Vinod Raman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the general problem of estimating $D(\dde(S))$, the probability that an unknown distribution $D$ assigns to an event determined by a sample $S$ of $n$ i.i.d.\ draws from $D$ through a known mapping $\dde$. The estimation algorithm knows $\dde$ and $S$ but does not have access to any additional samples from $D$. This formulation captures classical missing mass, the data-dependent targets of adaptive data analysis and post-selection inference, and the test error of a data-trained predictor, whose estimation was recently studied by \new{Gastpar et al.\ (2024a,b)}. Within this framework we examine the two classical approaches to estimation. The error of the empirical plug-in estimator is exactly a generalization gap, so generalization bounds transfer to it directly. The leave-one-out estimator, which recovers the Good--Turing estimator, is accurate for every mapping that is stable under the deletion of one sample point, including new structured examples such as neighborhoods of the sample and pierced sets.
The main application of our framework is to error estimation for a predictor that combines a base classifier with memorized exceptions, a structure common in theory and in practice. For it, the test error is exactly the missing mass restricted to the error region of the base classifier, a region selected by the same sample. We formulate the general problem of \emph{adaptive missing mass estimation} to address such dependence and propose a natural hybrid estimator, the Good--Turing estimator restricted to the selected region. We show that the generalization of the base classifier alone does not guarantee the accuracy of this estimator, and derive two bounds on its error: the first one based on the VC dimension of possible error regions and another based on the mutual information of the selected region with the sample.

---


### 71. [From 1D Benchmarks to Complex 3D Geometries: Can Agents Reliably Specify Problems for Automated PDE Simulation?](https://arxiv.org/abs/2610.41267)

**<font color=#1a73e8>作者：</font>** Akshat Jani, Sakhinana Sagar Srinivas, Venkataramana Runkana  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Turning an engineering request into a simulation requires consistent geometry, physics, boundary conditions, and numerical settings. Recent agent-assisted systems automate simulation setup, but successful execution alone does not establish whether the specification preserves the intended problem or correctly handles missing information. We study whether agents can reliably construct complete executable JSON specifications for automated geometry creation, meshing, PDE solving, and result export. Our workflow combines model extraction with deterministic scientific and capability checks, explicit clarification, and validated local patches that preserve unrelated accepted fields. We evaluate specification correctness, execution completion, and numerical verification separately. On 120 template-related requests, the full workflow achieves 98.3% correct first-turn specification and decision outcomes, compared with 92.5% for schema-assisted single shot and 82.5% for model-only: gains of 5.8 and 15.8 percentage points, respectively. It makes no false-ready decisions among the 42 requests requiring clarification or rejection. Component ablations identify contributions from scientific checks and conditional repair. Separate downstream studies cover 1D, 2D, and 3D steady and unsteady, linear and nonlinear problems, including flow and elasticity with complex three-dimensional wing geometries. A 30-case gallery demonstrates automated execution from retained JSON specifications, while 9 of 12 selected live user-to-results tests achieve joint specification, execution, export, and numerical-reference success (75.0%). These results support traceable, engineer-reviewed simulation assistance within the tested scope, while fresh-response regressions identify consistency as a priority for further improvement.

---


### 72. [SPT-Flow: One Integration, Many Futures in Continuous-Time World Models](https://arxiv.org/abs/2610.41273)

**<font color=#1a73e8>作者：</font>** Mingyang Lyu, Yinqian Sun, Gongce Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time world models generate a latent trajectory through a single ODE integration, but adding stochastic conditioning does not ensure that the model uses it. In our teacher-forced baseline, posterior means vary by only about 1% of the prior scale, and matched and swapped latents yield indistinguishable reconstruction PSNR at the reported precision. We study a supervision-shortcut hypothesis: ground-truth intermediate states can reduce the need for trajectory-associated latent information. We introduce SPT-Flow, which samples one latent per trajectory and matches a free-running ODE rollout to demonstration states at multiple readout times. Re-anchoring experiments support the proposed mechanism. On LIBERO, with both models trained for 30k optimizer steps, SPT-Flow improves best-of-10 PSNR over our retrained ODEWorld baseline by 2.0 and 2.4 dB at the mid-trajectory and final frames and reduces mean LPIPS by 23%, with comparable per-sample inference cost. The rollout control recovers most of the accuracy gain; learned latent conditioning adds diversity and best-of-K gains while reducing mean sample accuracy relative to this control. The diagnostics support trajectory-associated latent utilization; semantic mode coverage under matched conditions in the robotic setting remains unverified.

---


### 73. [SciGraphSelect: Auditable Scientific Data Selection through Knowledge--Reasoning Graphs](https://arxiv.org/abs/2610.41280)

**<font color=#1a73e8>作者：</font>** MiHyeon Kim, Ji-Eun Han, Eunkyeong Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific data selection is typically driven by relevance or utility scores, providing limited insight into why a document is retained. We introduce SciGraphSelect, a reference-grounded framework for auditable scientific data selection. SciGraphSelect organizes domain-specific knowledge, reusable reasoning operations, and reference-attested relations into a typed knowledge--reasoning graph, then scores candidate documents using concept coverage, relation and path co-support, and directional alignment. To avoid over-interpreting document embeddings, rich relational structure is preserved on the reference side while candidate-side evidence is treated conservatively without assuming relation entailment. By exposing the reference-grounded evidence behind each selection, SciGraphSelect brings traceability to the upstream construction of scientific training corpora and complements downstream scientific verification.

---


### 74. [SAT-ACT: Learning CDCL Branching from Outcome-Derived Action Preferences](https://arxiv.org/abs/2610.41290)

**<font color=#1a73e8>作者：</font>** Zhenchao Sun, Chongyang Tao, Ping Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning-based approaches have increasingly been explored for SAT solving, with particular attention to improving branching decisions in conflict-driven clause learning (CDCL) solvers. These approaches derive branching guidance either from static structural properties of SAT formulas or from dynamic signals obtained through solver feedback and execution traces. However, these forms of supervision provide limited evidence about state-dependent branching effects, while different outcome measures may favor different branching choices. To address these limitations, we propose SAT-ACT, an outcome-derived learning framework for CDCL branching. We design three complementary outcome comparison criteria to extract action preferences from independent branching action rollouts initiated at the same solver state. The criteria identify preferences supported by the outcomes and leave comparisons unresolved when the evidence is insufficient or conflicting, instead of forcing an ordering using a predefined scalar metric. A state-conditioned network learns branching priorities from the extracted preferences and uses them to guide CDCL search directly without online action rollouts. We further introduce non-dominated heuristic action supervision, which retains the solver-selected action as a training target only when it remains non-dominated under these preferences. Solver-level experiments show that SAT-ACT consistently reduces CDCL search costs on three SAT families and improves PAR-2 on the SAT Competition benchmarks.

---


### 75. [Toward Low-Burden Image-Based Dietary Assessment Through Human-AI Collaborative Correction](https://arxiv.org/abs/2610.41300)

**<font color=#1a73e8>作者：</font>** Darren Liu, Andrew Lu, Zhiyuan "Ryan" Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Image-based dietary assessment can automate initial food logging, but meal photographs often leave food identity, hidden ingredients, preparation, and portion uncertain, making correction a recurring part of use. We introduce Human-AI Collaborative Correction, which reframes correction as communicate intent $\rightarrow$ regenerate $\rightarrow$ verify: users express what should change through text, voice, or guided clarification, the AI regenerates the linked dietary record, and users verify the result. In a within-participant study with 30 participants, compared with conventional Manual Search-and-Edit Correction, collaborative correction was associated with lower workload (Raw TLX: 35.83 vs. 55.00; p < .001), 21.0% lower recorded usage time, 51.1% fewer recorded clicks, and more favorable user-experience ratings; 90.0% preferred it overall. An exploratory nutrient analysis also found lower energy MAE. These findings support intent-driven regeneration as a promising interaction pattern for reducing correction burden while preserving user verification and making image-based dietary tracking easier to sustain.

---


### 76. [rl_rob: A transparent, from-scratch Python library for teaching reinforcement learning from tabular methods to deep policy gradients](https://arxiv.org/abs/2610.41303)

**<font color=#1a73e8>作者：</font>** Abdulrahman Altahhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> rl_rob is an open-source Python library for teaching reinforcement learning. It implements the arc of a modern course, from tabular temporal-difference learning through linear function approximation to deep value-based and policy-gradient methods, with every algorithm written from first principles so that its update rule is visible in a few lines of code. All agents share one interface, so learners can compare methods directly across stages and trace a deep reinforcement learning update from the temporal-difference error to the weight change. The library supports teaching and assessment in which students implement, modify and explain update rules, rather than only produce working code.

---


### 77. [STAR-FER: Adaptive Selective Restoration for Edge-Based Low-Resolution Facial Expression Recognition](https://arxiv.org/abs/2610.41310)

**<font color=#1a73e8>作者：</font>** ZhongYang Wu, ZhenFeng Gan, Di Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Variable interaction distances continuously degrade facial resolution in edge-based affective interaction, making low-resolution facial expression recognition (FER) difficult under limited computation. Full-face image or feature restoration incurs substantial overhead, whereas lightweight recognition pipelines may miss local cues that remain discriminative after degradation. We propose STAR-FER, a scale-and-task-adaptive selective restoration framework that balances recognition performance and resource constraints. A lightweight image-scale conditioned Gate jointly predicts a pixel-wise spatial ranking and a continuous restoration budget, then applies exact-support projection to obtain an input-dependent free-form mask. The mask-conditioned restorer retains complete facial context while concentrating sparse restoration and residual insertion on the selected support. Across seven degradation scales from x2 to x8 on the complete RAF-DB test set, STAR-FER achieves 80.92% mean accuracy and 71.64% Macro-F1, improving the low-resolution ResNet-18 baseline by 2.25 and 2.71 percentage points, respectively. It surpasses SR-FER by 1.04 accuracy points while requiring 8.84 GFLOPs, a 54.29% reduction, with 28.01% mean mask coverage, and maintains effective recognition at unseen non-integer scales. These results show that spatial-ranking and continuous-budget driven selective restoration reduces spatial modification and computation while maintaining low-resolution FER performance, offering an efficient path to resource-constrained affective interaction.

---


### 78. [Transferring Peptide-Target Interaction Patterns to Small Molecules by Joint Guidance for Diffusion and Flow Matching](https://arxiv.org/abs/2610.41322)

**<font color=#1a73e8>作者：</font>** Jian Lee, Changyun Cho, Sun Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating small molecules to target protein-protein interactions (PPIs) remains one of the most challenging yet high-reward frontiers in drug discovery. Unlike traditional small-molecule drugs that bind to deep, well-defined pockets, PPI interfaces often comprise broad, shallow binding surfaces. A natural strategy is to leverage known peptide-target interactions, as peptide ligands provide rich interface-level constraints. However, a major algorithmic challenge is that rigid atom-level conditioning on peptide structures can over-constrain the generative space and exclude valid small-molecule solutions. To address this challenge, we present PIFT (Peptide InterFace Transfer), a novel framework that transfers peptide-target interaction patterns to small molecules through joint sampling-time guidance of masked discrete diffusion and continuous flow matching. PIFT first maps peptide-target and small-molecule-target interfaces into a shared, target-conditioned interaction space, capturing transferable interface information across molecular modalities. The resulting peptide-derived reference then jointly steers building-block logits and 3D coordinates toward peptide-compatible molecules while preserving a strong adapted molecular prior. Extensive experiments across diverse PPI targets show that the learned representation captures cross-modal interaction compatibility, while peptide guidance improves interface recovery and achieves strong docking performance and favorable molecular properties.

---


### 79. [OrionLink: Single Sign-On with Oblivious Identity Brokers](https://arxiv.org/abs/2610.41323)

**<font color=#1a73e8>作者：</font>** Yijia Fang, Bingyu Li, Luchao Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Single Sign-On (SSO) is a federated authentication mechanism that improves user experience by enabling access to multiple services, or Relying Parties (RPs), through a single authentication at an Identity Provider (IdP). To reduce integration complexity, many RPs rely on third-party Identity Brokers (Brokers) that aggregate numerous IdPs into a unified interface, thereby simplifying protocol management and interoperability. However, while brokers ease development, they introduce a fundamental security and privacy risk: sensitive authentication credentials and user behavioral data are exposed to the broker, creating a high-value single point of failure. Existing SSO solutions provide limited protection against these risks. With the goal of achieving broker obliviousness, we address these challenges at their root and present OrionLink, a comprehensive privacy-enhancing SSO pipeline that is compatible with existing brokered SSO architectures and systematically mitigates broker-induced risks without sacrificing usability. OrionLink incorporates two core components: (a) an anonymous pseudonym derivation scheme that generates unlinkable, per-RP identifiers to prevent cross-service user tracking; (b) an anonymous key exchange protocol that establishes end-to-end encrypted channels to protect user data from broker visibility. We further instantiate OrionLink with two new features, preserving broker functionality and deployability. We implemented a prototype of OrionLink within a brokered SSO environment, and experimental evaluation shows that the framework achieves substantial security and privacy improvements with acceptable performance overhead.

---


### 80. [Efficient cross-domain multi-factor authentication](https://arxiv.org/abs/2610.41342)

**<font color=#1a73e8>作者：</font>** Yongjiao Li, Zhenlei Wang, Zhu Cao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Secure cross-domain authentication is crucial for protecting information exchange across terminals in different security domains. However, existing cross-domain authentication models suffer from inflexibility, high storage and computational consumption. In response to these problems, a cross-domain multi-factor authentication protocol with improved efficiency (CDAuth) is proposed. CDAuth employs a universally applicable multi-factor authentication approach, integrating pseudo-identity, attribute concealment, and biometric hiding. The authentication information sets can be freely added or modified to accommodate various access scenarios. This boosts privacy, flexibility, and applicability compared to traditional methods. Furthermore, multi-edge servers as Certification Authorities (CAs) store only the union of terminal attributes and a verification token per user in their subdomains, instead of each user's attribute and biometric sets as in traditional schemes, significantly reducing storage consumption. Additionally, replacing the bilinear pairing operations with the native group operations, while maintaining security, significantly reduces computational consumption. Our analysis shows that CDAuth can resist common security attacks and is more efficient than the previous schemes.

---


### 81. [Quantile Propagation Planning for Budgeted Tail-Risk Evaluation](https://arxiv.org/abs/2610.41351)

**<font color=#1a73e8>作者：</font>** Weijia Han, Zhi Huang, Lisha Qu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Risk-aware planning must identify rare, costly outcomes using only a limited number of model evaluations. Monte Carlo rollouts spend this budget on noisy tail estimates, while planning from the mean can miss the tail entirely. We introduce quantile propagation planning (QPP), which propagates a small, fixed set of disturbance quantiles through the dynamics and integrates the resulting cost curve to evaluate both mean and tail risk. The method is exact at the propagated levels, converges as the quantile grid is refined, and admits a one-sided conservatism guarantee under stated structural conditions. In controlled overload and inventory tasks, QPP reduces realized tail cost and constraint violations relative to mean-rollout planning. On overload, it remains competitive with sampled evaluators that use substantially more trajectories. These results position QPP as a transparent, budget-controlled approach to tail-risk evaluation.

---


### 82. [Task-Performance Routing for Multi-Teacher Distillation in CT Medical Image Segmentation](https://arxiv.org/abs/2610.41362)

**<font color=#1a73e8>作者：</font>** Jiaye Yang, Yao Liu, Die Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained models offer complementary strengths in CT organ segmentation, but their relative accuracy varies across organs and spatial regions. Multi-teacher knowledge distillation can combine these strengths in a single student, yet global or instance-level teacher weights overlook variation within a 3D volume. We propose Task-Performance Routing (TPR), which uses region-wise segmentation errors to determine teacher weights during training without learned routing parameters. In hard regions, TPR favors teachers with lower prediction errors; in easy regions, it uses uniform weights to combine their knowledge. A hierarchical spatial partition provides fine-grained routing in shallow encoder stages and coarse-grained routing in deep stages. Experiments on BTCV, MSD-Liver, and MSD-Pancreas with two teacher pairs and two backbone architectures show higher Dice scores than the individual teachers, adaptive ensembles, and evaluated multi-teacher distillation baselines. On MSD-Pancreas, TPR achieves Dice scores of 65.40% with SwinUNETR and 68.25% with U-Net, compared with 64.38% and 67.45% for the corresponding adaptive ensembles. Inference uses the student alone, with no routing or teacher overhead. Code is available at this https URL.

---


### 83. [Generated storm lifecycles fill the rare-event tail of short rainfall records](https://arxiv.org/abs/2610.41365)

**<font color=#1a73e8>作者：</font>** Valerie Tsao, Nathaniel W. Chaney, Manolis Veveakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Historically rare ''one-in-a-generation'' storms are occurring with unprecedented frequency, causing catastrophic damage and mounting casualties, and exposing the vulnerability of infrastructure designed around short observational records. To overcome the limitations of sparse data, we present StormGen, a generative machine-learning model that transforms an observed storm's initial hours into complete, physically plausible hourly rainfall lifecycles in minutes. Evaluated on a decade of southeast Texas rainfall, StormGen produced close counterparts for 4\5% of the most severe 2\% of storms--compared to just 3\% for stochastic storm transposition--and maintained spatial coherence over full 24-hour sequences. Crucially, from a single hour of initial rainfall, the model successfully reconstructed the specific lifecycle, spatial pattern, and extreme catchment totals of Hurricane Harvey itself, despite the event being entirely absent in training. Because storm timing alone can more than double peak flows, these complete generated scenarios provide a vital mechanism to stress-test flood protections against unprecedented extremes.

---


### 84. [BlindStep: A Secure One-Step Kernel for Privacy-Preserving Collaborative Reasoning](https://arxiv.org/abs/2610.41369)

**<font color=#1a73e8>作者：</font>** Xiaoxian Liu, Xingyu Tan, Chen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A recurring step in two-party collaborative workflows combines a private candidate frontier with a partner's compatible evidence, scores the resulting candidates, and retains only a small frontier. Direct execution can expose intermediate candidates, local scores, or unauthorized evidence provenance. Existing MPC platforms and PSI protocols provide useful building blocks, but they do not define a unified post-alignment boundary for bounded-slot aggregation, fail-closed overflow handling, retained-frontier selection, and downstream disclosure. We present BlindStep, a fixed-shape MPC-online kernel for one such post-alignment step between two semi-honest parties. Given a frontend realizing the bounded-slot contract and an application enforcing the reveal policy $\rho$, BlindStep provides a per-invocation simulation-based guarantee in the $F_{\mathrm{align}}$-hybrid model: the kernel leaks only public setup parameters, fixed execution-shape metadata, a global overflow bit, and $\rho$-authorized Layer-2 disclosures. The guarantee excludes malicious security and multi-invocation composition, and treats frontend leakage and offline preprocessing separately.
Within this kernel boundary, we implement six semi2k realizations in MP-SPDZ, crossing two sharing styles and three top-K strategies: H-variants compare over arithmetic shares, while B-variants convert packed ranking values to Boolean shares before selection. Under LAN, B-Queue is 6-7 times faster and uses about 40 times less communication than H-Queue at N = 256 and 2048. Against H-Sort on the same backend, B-Queue achieves speedups of 21 and 30 times and communication reductions of 204 and 290 times at N = 2048 and 8192, respectively. Under the evaluated N = 256, 100 ms RTT WAN profile, H-Sort becomes fastest, showing that round complexity can dominate backend choice for the measured MPC-online kernel.

---


### 85. [Online Evidence-Containment Prediction over Text Spans under Distinct Queries](https://arxiv.org/abs/2610.41384)

**<font color=#1a73e8>作者：</font>** Xiang Liu, Haochen Ding  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evidence-grounded NLP systems often verify nested text regions sequentially, so verifying one region constrains others. We formalize this as Online Evidence-Containment Prediction (OECP): each candidate is predicted before exact verification and queried at most once. Span containment is exactly a triangular 2D product order, making OECP distinct-query online isotonic regression. With multiple admissible targets, worst-case regret is near-linear, $\widetilde{\Theta}(m_{\mathrm{eff}})$, in the effective scale given by endpoint-rank compression; a single fixed target, as in standard QA, admits an explicit polynomial-time learner with optimal $\Theta(\log m_{\mathrm{eff}})$ regret, run on real NQ episodes. On Natural Questions, containment yields a large deductive gain plus a smaller learned gain on unresolved candidates, reproduced across two backbones and DPR hierarchies. Expected Search-space Reduction (ESR) turns these probabilities into decisions, localizing evidence in fewer verifier calls on SciFact, ERASER, and DPR hierarchies; on DPR hierarchies under call budgets it outperforms four recent external selectors and raises fixed-reader F1 over learned and generator-greedy scheduling.

---


### 86. [Anomalies as Residuals: Cauchy Displacement Networks](https://arxiv.org/abs/2610.41387)

**<font color=#1a73e8>作者：</font>** Yang Cao, Zihao Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neighbourhood-based detectors such as KNN, LOF and LUNAR remain among the most accurate methods for tabular anomaly detection, but they compare every query with the stored training set, so their inference cost and memory grow with the data and the data must be kept at deployment. We ask whether the neighbourhood geometry these detectors exploit can be compiled into a small network that scores a query with a single forward pass. We propose the Cauchy Displacement Network (CDN), which regresses each normal point onto the mean of its $k$ nearest training neighbours with a single-hidden-layer network of Cauchy activations and scores a query by the length of its predicted displacement. This displacement is an empirical mean-shift vector, whose fixed-radius population counterpart locally approximates a scaled gradient of the log density. We show that Cauchy units exactly represent the score fields of a structured family of Student-$t$ expert densities, and establish a constructive approximation bound for the corresponding population neighbourhood-mean map using a single-hidden-layer Cauchy network. We further show that the bounded network output guarantees asymptotically linear residual-score growth along every fixed direction. On 46 benchmark datasets against 28 baselines, CDN obtains the best mean rank under both AUC-ROC and AUC-PR, while scoring $10^4$ queries in a few milliseconds on a single CPU thread, up to three orders of magnitude faster than neighbourhood-based detectors, with a model whose size does not depend on the training set.

---


### 87. [DUGO: Dual-Scale Gaussian Memory for Online Temporal Action Localization in Egocentric Procedural Videos](https://arxiv.org/abs/2610.41402)

**<font color=#1a73e8>作者：</font>** Mohammed Aman Bhuiyan, Md. Sazzad Hossain Adib, Samiul Basir Bhuiyan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online Temporal Action Localization (OnTAL) aims to detect and localize action instances from untrimmed streaming videos in real time. Unlike offline approaches, OnTAL models have no access to future frames and cannot go back and refine earlier predictions, which makes the task considerably harder given the strict real-time constraints and narrow temporal window available. Most existing OnTAL methods lean on either brief anchor-based context or a single-scale memory of past frames, which limits how well they can capture actions unfolding across multiple time scales or requiring long-range reasoning in Procedural Videos. To address these gaps, we present DUGO (Dual-Scale Encoding and Gaussian Memory Online), a new OnTAL framework that jointly models local motion dynamics and long-range temporal dependencies. At its core, DUGO uses a Dual-Scale Temporal Encoder, pairing depth-wise local representations with global self-attention so it can pick up both fine-grained temporal patterns and broader contextual cues. We also introduce a Gaussian Memory Bank, which represents action memory as stochastic, input-conditioned Gaussian prototypes, allowing for richer temporal memory through gated cross-attention applied at both the encoder and anchor-query stages. Extensive experiments on procedural egocentric datasets (EGTEA, EPIC-Kitchens-100) demonstrate that DUGO achieves state-of-the-art performance while also providing substantial improvements on non-egocentric benchmarks such as Muses. The project page is available at: this https URL

---


### 88. [Certifying Retraining Regret through Residual Structure](https://arxiv.org/abs/2610.41410)

**<font color=#1a73e8>作者：</font>** Peida Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We certify a fixed ridge predictor's regret against full-feature retraining over every continuous completion of an interval-valued table. Our main theorem gives verifiable original-row residual conditions for a uniform error bound independent of nuisance-feature scale and rank, with an asymptotically sharp leading constant and quantitative leakage stability. Full-rank constructions separate certification dimension from feature dimension, including examples requiring directions beyond the candidate. Observed-row anchors make the conditions computable, while exact row geometry and global search return valid upper bounds and feasible original-table witnesses. A finite-scale contraction and common-domain moment fallback implement the structural result. Four real-world tasks retain all model features and certify twenty rank-three instances to width $10^{-5}$. Their primary median widths improve over centered moments. Joint residual refinement additionally certifies all twenty new response-independent masks to the same precision within 76.21 seconds. For a concrete fixed-point predictor contract, pure energy certifies thirteen of fifteen stopping decisions in ten seconds, versus five for moments. Refinement certifies all fifteen within 91.68 seconds at the same objective threshold.

---


### 89. [CryoAtlas: A Large Curated Dataset and Unified Benchmark for Cryo-EM Atomic Model Building](https://arxiv.org/abs/2610.41411)

**<font color=#1a73e8>作者：</font>** Mingrui Li, Minzhang Li, Weichen Qin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning has accelerated automated atomic model building from cryo-EM maps, yet progress remains limited by the lack of large, high-quality datasets and standardized evaluation benchmarks. We address this gap by introducing CryoAtlas, a rigorously curated dataset and unified benchmark for density-guided atomic model building of protein chains. By integrating and filtering EMDB and PDB entries (up to March 2026), CryoAtlas provides 17,809 map-model-sequence entries, including a curated 16,657-entry training split. From this resource, we construct a 618-target benchmark with a shared evaluation protocol that jointly assesses structural accuracy, model-to-map fit, and stereochemical validity. Using this framework, we benchmark state-of-the-art learning-based methods against Phenix and AlphaFold3, comprehensively analyzing the impact of map resolution, sequence length, protein category and sequence identity on modeling accuracy. As a case study, retraining the ModelAngelo CNN component on CryoAtlas improves performance on the benchmark. CryoAtlas provides an open, reproducible foundation for future cryo-EM atomic model building research. Project details and resource release updates are available at this https URL.

---


### 90. [A Unified XAI-NSAI Analytical Framework for Trustworthy IoT Anomaly Detection](https://arxiv.org/abs/2610.41424)

**<font color=#1a73e8>作者：</font>** Hugues Leger, Giovani R. Abuaitah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The widespread deployment of Internet of Things (IoT) devices in critical environments makes anomaly detection essential for identifying abnormal behaviors and supporting timely investigation and response. However, accurate detection alone is insufficient. Practical IoT deployments must also provide explanations, incorporate domain knowledge and reasoning, operate under IoT constraints, and support human decision making. Although recently proposed approaches increasingly incorporate Explainable Artificial Intelligence (XAI) or Neuro-Symbolic Artificial Intelligence (NSAI), XAI and NSAI methods are often considered independently. We argue that they should be considered together to better understand their complementary roles in supporting trustworthy IoT anomaly detection. To address this gap, we propose a unified analytical framework organized around five complementary dimensions. The framework provides a structured basis for characterizing existing approaches, identifying capability gaps and design trade-offs, and guiding the design of new anomaly detection systems for different IoT applications. We demonstrate the framework's analytical utility by applying it to three representative studies and illustrate its design utility through its application to a Medical IoT anomaly detection system.

---


### 91. [FlexReader: Towards Adaptive Decoding Paths for Efficient Arbitrary-Length Scene Text Recognition](https://arxiv.org/abs/2610.41426)

**<font color=#1a73e8>作者：</font>** Zhibin Ma, Pengwen Dai, Zhigang Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Scene Text Recognition (STR) models are inherently coupled with a specific decoding strategy by their training paradigms, limiting their flexibility in deployment across diverse recognition scenarios. In this paper, we propose FlexReader, an STR model that supports multiple decoding strides, enabling a single model to achieve an optimal accuracy-efficiency trade-off across different datasets. Specifically, we first introduce a Sub-string Perception module to perceive the target sub-string from visual features, followed by multiple parallel decoding blocks that independently decode each character in the sub-string. During inference, FlexReader supports decoding with arbitrary strides within the perceived sub-string range. Furthermore, we propose Adaptive Prefix Decoding, which adaptively selects the decoding stride at each step based on the model's confidence in the decoded characters, thereby identifying the optimal decoding path for each input. Experimental results demonstrate that FlexReader exhibits robust recognition capability across a diverse range of benchmarks, including those featuring long text, curved text, and occlusions. It consistently outperforms existing decoding strategies in recognition accuracy while achieving up to 6-flod decoding speedup over autoregressive decoding.

---


### 92. [BlindToChange: AI Agents Can Find Changes When Asked But Do They Look When Needed?](https://arxiv.org/abs/2610.41435)

**<font color=#1a73e8>作者：</font>** Anirudh Phukan, Tanya Goyal, Danish Pruthi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Given that AI agents can search the web broadly and deeply in real time, it is tempting to conclude that their outputs account for recent world events. We show that this conclusion does not hold in practice. While agents can search and easily find recent changes, the correctness of their responses depends on whether they search and what they search for. Popular agentic search benchmarks like BrowseComp cannot expose failures wherein agents do not recognize their own assumptions that should be verified, since these benchmarks explicitly state what needs to be found. In contrast, many user requests state only the final information need (e.g., an itinerary for a trip), leaving the agent to discover relevant changes (e.g., the temporary closure of a museum) and account for their consequences. To highlight such gaps, we introduce BlindToChange, a benchmark that measures whether agents proactively discover recent events that affect their responses. Our benchmark comprises requests for recommendations where an obvious candidate is no longer applicable due to a recent real-world event. These events are drawn automatically from Wikidata, allowing BlindToChange to be periodically refreshed. Strikingly, we find a big gap -- as high as 27.5 points, even at high reasoning effort -- in systems' performance, when the recent event is not explicitly mentioned compared to when we ask about it directly. Analyzing search trajectories, we learn that more than half of the failures can be attributed to the fact that agents do not directly search to verify whether a relevant fact has changed. Our benchmark highlights, and tracks, a new axis of progress, wherein systems account for recent information that is not explicitly mentioned in the user request.

---


### 93. [GESIS Surf: An Open-Source Infrastructure for Privacy-Preserving Longitudinal Web Browsing Data Collection](https://arxiv.org/abs/2610.41441)

**<font color=#1a73e8>作者：</font>** Mario Alberto Ramirez, Frank Mangold, Sebastian Stier  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Understanding how people navigate digital media environments requires behavioral data beyond survey self-reports. However, existing infrastructures for collecting such data reproducibly, sustainably, and with strong privacy guarantees remain limited: commercial solutions lack transparency and data governance, while academic tools are typically designed for narrow, short-term use cases and do not support general-purpose academic panel data collections. We address this gap with GESIS Surf, a research infrastructure for large-scale longitudinal collection of web behavioral data in naturalistic environments. The system consists of a browser extension (Chrome and Firefox), a backend with a REST application programming interface (API), and a relational database. It passively captures user interactions, page metadata, and full HTML snapshots of each rendered page, embedding each observation within a hierarchical session model that preserves the structure of browsing behavior. GESIS Surf implements privacy-by-design through strict opt-in participation, per-domain collection rules, and client-side data minimization, ensuring that sensitive data are controlled at the point of collection. The system has been deployed with more than 1,000 participants in a large-scale academic panel infrastructure that includes surveys of participants, and supports reproducible, content-level, and structurally rich analysis of digital behavior. By combining hierarchical session modeling, content-level capture, and integrated privacy enforcement within a unified system, GESIS Surf provides a general-purpose infrastructure for studying digital behavior in a reproducible manner over time.

---


### 94. [Beyond Trial-and-Error: A Geospatial-Guided Active Reasoning Framework for Robust Aerial Vision-and-Language Navigation](https://arxiv.org/abs/2610.41446)

**<font color=#1a73e8>作者：</font>** Jiawei Ge, Wenkang Gong, Jiuxin Cao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial Vision-and-Language Navigation (VLN) requires UAVs to locate language-specified goals in large-scale urban environments, where objects often appear small and visually ambiguous from high-altitude viewpoints. Existing methods largely follow a reactive paradigm common in indoor VLN, repeatedly updating navigation states from local observations while underutilizing the geospatial structure that remains stable during navigation. As a result, visually similar distractors can cause a reactive goal search to repeatedly reinforce locally plausible goal hypotheses based on passively accumulated evidence, leading to unreliable localization. To address this, we propose GeoReasoner, a robust framework that shifts the paradigm of Aerial VLN from reactive trial-and-error to geospatial-guided active reasoning. Specifically, GeoReasoner first performs pre-search geospatial reasoning to derive region-level priors and constrain the goal hypothesis space. Building on these, it further conducts hypothesis-driven exploration to actively acquire discriminative evidence and refine competing goal hypotheses. Finally, consistency-aware goal verification adversarially assesses complementary evidence sources before stopping, hence reducing premature or erroneous goal confirmations. Experiments on the real-world CityNav benchmark demonstrate that GeoReasoner sets a new SOTA among zero-shot Aerial VLN methods while competing favorably with supervised approaches.

---


### 95. [Evidence-Guided Recovery for AI Agents with Ambiguous Tool Outcomes and Partial Execution](https://arxiv.org/abs/2610.41453)

**<font color=#1a73e8>作者：</font>** Genliang Zhu, Xiaobo Chen, Ziyuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool timeouts can leave AI agents facing ambiguous tool outcomes and partial execution: an action may have failed, committed or remained in flight while other workflow steps have already completed. We formulate evidence-guided task recovery over approved obligations, provider capabilities and states compatible with public evidence. A shared admissibility check handles key expiry, authorization timing, dependencies and residual effects; a terminal certificate separates actual goal satisfaction from publicly supported safe completion. The known-model implementation combines standard observation-contingent planning with a separately implemented effect-history adjudicator. In a finite study of 37 assignments, planning and three active controls each certify 28 completions; four saved synthetic fee units incur additional computation. A preregistered assignment-held-out comparison then evaluates planning advice against evidence prompting with two local model bundles. Across 58 paired units in 19 previously developed task families, advice certifies 30 completions versus 9, a 36.2-percentage-point difference (exact family sign-flip p=0.0078), using 272 proposals versus 399. All 116 trajectories pass independent replay. Both models exhibit a positive completion difference. The comparison measures the evaluated advice interface under a common shield; search-versus-rule advice requires a separate matched comparison. Unknown and handoff outcomes remain explicit, with guarantees tied to the declared provider capabilities rather than arbitrary third-party exactly-once execution.

---


### 96. [When Everyone Can Build a Model: Mechanistic Inference in the Age of AI](https://arxiv.org/abs/2610.41454)

**<font color=#1a73e8>作者：</font>** Marvin van Aalst, Adèle H. Ribeiro, Anna Matuszyńska  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep learning and AI-assisted code generation are lowering the technical barrier to building mathematical models of biological systems that reproduce complex observations. This lets researchers with domain expertise build semi-mechanistic, hybrid models constrained by prior knowledge and augmented with learned structure without extensive training in modelling. However, easier construction does not make interpretation easier: predictive success of such so-called grey-box models does not establish that an inferred mechanism corresponds to the one that generated the data, and the learned component can absorb errors in the mechanistic part. Many biological modelling problems are underdetermined, so several, possibly infinitely many, models may reproduce the same data equally well. This ambiguity enters at two modelling choices: which variables can affect others, and which response function describes the underlying mechanism. For the first choice, causal inference provides a formal framework stating which causal relationships and intervention effects are identifiable from the data and available knowledge. For the second, ensemble analyses quantify the uncertainty and the range of behaviours still allowed by models that fit equally well. Together, they turn a single good fit into an explicit account of what is supported, what remains open, and which experiment would decide.

---


### 97. [Improving the Optimization Landscape of Matrix Completion with $ε$-close Surrogates](https://arxiv.org/abs/2610.41455)

**<font color=#1a73e8>作者：</font>** Ziye Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-convex optimization is central to machine learning and AI, yet unlike its convex counterpart, it still lacks a general and principled framework. In this work, we try to highlight the importance of combining noisy perturbations with over-parametrization mathematically under the classic setting of matrix completion (MC). Matrix completion is an important non-convex recovery problem in which only a subset of a matrix's entries is observed, and the remaining entries must be recovered using low-rank constraints. This problem is notoriously difficult because observations are limited. However, we show that by injecting $\epsilon$-level perturbations into the nullspace of the observation mask, we can construct noisy matrix sensing surrogates whose solutions remain $\mathcal{O}(\epsilon)$-close to the ground truth with valid restricted isometry property (RIP) constants. The existence of RIP further enables powerful tensor frameworks to be applied with theoretical guarantees. This approach reflects a broader empirical trend in which stochasticity or noise improves the curvature of the optimization landscape, allowing over-parameterized (a.k.a large) models to better separate signal from noise. Assuming each matrix entry is observed independently, we establish quantitative recovery guarantees without explicit requirements on sampling rate or incoherence, and discuss how such assumptions can further strengthen our results.

---


### 98. [RetryRoute: Retry-Aware Model Routing for Agentic Image Editing Services](https://arxiv.org/abs/2610.41460)

**<font color=#1a73e8>作者：</font>** Hanshuai Cui, Zhiqing Tang, Zhi Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Web agents increasingly edit images by calling open editing models in a critique-and-retry loop, and these models differ in cost by more than an order of magnitude. After every rejected edit, a service must decide whether to retry the same model, escalate to another or give up. Existing routers pick one model per request, and cascades escalate in a fixed order. However, both treat a retry as an independent draw. We identify sticky failures, meaning that a retry after a failure succeeds only 17-53% as often as a first try across six open models, three benchmarks and two judges. Based on this finding, we propose RetryRoute, a retry-aware router that estimates each model's chance of success given the request's failure history. It plans retries, escalations and abandonment over failure states and adds live queue waits to the cost, so the same plan becomes load-aware dispatch. At the main budget, RetryRoute's success under the in-loop judge exceeds the strongest of eleven prior baselines by 2.8 points on average over eight groups. On a GPU serving testbed it raises the share of edits delivered within the service-level objective by 5.0-6.3 points over the best prior baseline at every load.

---


### 99. [Spectral Haar Binarizer: Compact Boolean Contrast Representations for Hyperspectral Classification](https://arxiv.org/abs/2610.41478)

**<font color=#1a73e8>作者：</font>** Michał Romaszewski, Przemysław Głomb  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tsetlin Machines offer an interpretable, hardware-friendly alternative to conventional machine learning models, but applying them to continuous hyperspectral measurements requires converting spectral signals into Boolean representations. Standard binarisation methods typically discretise each spectral band independently, potentially discarding important relationships between neighbouring wavelengths. In this paper, we introduce the Spectral Haar Binarizer (SHB), a contrast-based spectral representation method that constructs Boolean predicates from differences between selected spectral intervals. Inspired by Haar-like contrast features, the method uses an AdaBoost-style selection procedure to obtain a compact set of discriminative spectral predicates. We evaluate SHB on five heterogeneous hyperspectral datasets covering forensic blood detection, agricultural and urban remote sensing, and rainforest tree-species classification. Across binary and multiclass tasks, SHB consistently outperforms standard per-band binarisation strategies and provides the strongest or near-strongest results across classifiers. In binary tasks, TM-SHB achieves the best average performance, while RF-SHB is strongest in multiclass settings. Bayesian and rank-based analyses confirm that SHB's advantage is robust across datasets and not driven by isolated cases. The results show that representing continuous hyperspectral measurements is a central processing step for efficient classification. That contrast-based Boolean features provide an effective bridge between information-rich sensor measurements and compact, logic-based processing.

---


### 100. [EvoMCP: Co-evolving MCP agents and training data](https://arxiv.org/abs/2610.41479)

**<font color=#1a73e8>作者：</font>** Xuanang Gao, Kepeng Lin, Xinyan Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning of Model Context Protocol (MCP) agents is typically conducted on a static data distribution, which fails to adapt to the student's evolving capabilities and leaves newly exposed weaknesses insufficiently addressed. To address these challenges, we propose \method, an agent--data mutual evolution framework that enables MCP agents to improve through a closed loop of task evolution, trajectory evolution, and supervised fine-tuning. Specifically, \method\ assesses the student's established capabilities and capability gaps from rollout feedback to identify learning targets. Task evolution then translates these targets into executable tasks by adapting the instructions and observable environment states of compatible verified seed tasks while keeping their verifiers aligned. To provide reliable and efficient demonstrations for these tasks, trajectory evolution uses reusable skills to recover failed teacher rollouts and refine successful ones. The resulting task--trajectory pairs are used to fine-tune the student, while accepted tasks seed subsequent evolution. To close the loop, we re-evaluate the updated student and use its feedback to guide the next round of data evolution. Experiments on Toolathlon, MCPMark, and MCP-Atlas demonstrate consistent improvements over the initial student, yielding absolute gains of 16.5\%, 10.2\%, and 12.6\%, respectively. Project page: this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-193](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
