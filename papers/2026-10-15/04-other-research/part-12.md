# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**551-600**（第 12/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 551. [Welcome to the Age of Agent Ads: Using On-Policy Attacks to Steer Agentic Decisions](https://arxiv.org/abs/2610.17195)

**<font color=#1a73e8>作者：</font>** Tim R. Davidson, Marija Šakota, Joshua Joseph 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> People increasingly delegate option-ranking tasks (e.g., shopping, job search, travel) to AI agents, which creates incentives to steer agentic decisions via "agent ads." To defend against such steering attacks, people count on models' alignment training and platforms' terms of service, and consequently the most effective existing attacks are designed to trigger off-policy behaviors. Exposing a new attack surface, we introduce on-policy attacks, which steer agentic decisions without pushing individually aligned behaviors off policy. Our example attack consists of two steps: To remain compliant with platforms' terms of service, we first inject a truthful negation about a fictitious concept ("Does not contain blizyester") into a product description. This triggers an agent to search the web ("What is blizyester?"), which surfaces planted websites full of fabricated information associating the fictitious concept with harmful implications ("Blizyester linked to dementia"). Trained to keep users safe from harm, the agent penalizes every option missing the truthful negation. Evaluating our attack across four real-world listing datasets, we find some frontier models exposed, enabling an adversarial actor to penalize competitors without violating existing platform-listing guidelines. We discuss the broader challenge of regulating advertising aimed at AI agents and provide recommendations to model developers and platform providers.

---


### 552. [Multics: Generative Multi-Player World Model with Hierarchical Communication](https://arxiv.org/abs/2610.17201)

**<font color=#1a73e8>作者：</font>** Kaiyi Huang, Wangbo Yu, Yukun Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-player interactive world models aim to simulate shared environments from multiple players' perspectives, but achieving robust generation while scaling to more players remains challenging. Existing approaches that rely on fully-connected communication (e.g., Solaris) incur quadratic attention costs as the number of players grows, while centralized approaches (e.g., $\gamma$-World) suffer from interference between unrelated events in a shared global representation. To address these challenges, we present Multics, a multi-player video generation framework with hierarchical communication that structures information exchange across player, group, and global levels. This hierarchy introduces group tokens into self-attention as intermediate group-level representations that aggregate locally relevant player information. These tokens connect to global tokens for cross-group communication, while the hierarchical topology limits direct mixing between unrelated local events. Group-token parameters are shared across group slots, allowing the same communication module to accommodate varying numbers of players without introducing new group-specific parameters. We further propose budget-constrained dynamic grouping based on recent camera trajectories, which adaptively groups relevant players while limiting unnecessary communication. Experiments demonstrate that Multics achieves state-of-the-art performance in 4- and 6-player settings, with improved cross-player consistency, player-specific action and camera controllability, and interference robustness. Moreover, Multics generalizes from 4-player training to 6-, 8-, and 10-player inference without retraining, while reducing self-attention computation compared with fully-connected communication.

---


### 553. [Compute-optimal data scaling for neural surrogates via multi-fidelity training](https://arxiv.org/abs/2610.17221)

**<font color=#1a73e8>作者：</font>** Paul Setinek, Fabian Paischer, Nils Thuerey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogates for Partial Differential Equations (PDEs) are usually trained on synthetic data from numerical simulators. As models grow and scaling laws demand larger datasets, the cost of data generation often outweighs the training cost and becomes the bottleneck in the scaling quest. Unlike data in other domains, however, each PDE sample has a tunable cost that depends on its numerical fidelity, with the resulting cost-accuracy trade-off governed by known convergence rates. We exploit this property by formalizing neural surrogate training as a function of both data quantity and fidelity under a fixed data generation compute budget, treating fidelity as a fine-grained discrete spectrum rather than a binary distinction. Building on this, we show that multi-fidelity training enables Pareto-optimal error scaling against data generation compute. By using simulations at lower fidelities as an additional training signal, training on the optimal fidelity mixture matches the accuracy of high-fidelity-only training, with up to $6.3\times$ less data generation compute across our settings. We validate these findings across six PDE problems spanning structured grids and unstructured meshes, two distinct error sources (discretization and iterative-solver error), and four surrogate architectures, totaling over 7,000 training runs.

---


### 554. [CodeLift: Your Test Suite Is Secretly a Dense SWE Curriculum](https://arxiv.org/abs/2610.17224)

**<font color=#1a73e8>作者：</font>** Junjielong Xu, Huachao Zhu, Alyssa Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The pass-all-test binary reward has become a standard recipe for training software engineering agents, but its sparsity eliminates difference of partially correct patches. The test pass-rate is a natural alternative. However, we find that it is not a reliable indicator of patch quality. A functionality being tested can be covered by either one challenging test or one hundred trivial tests, where the majority might be already satisfied pass-to-pass tests. We introduce CodeLift, a reinforcement learning method that dynamically calibrates pass-rate rewards, turning the test suite into an adaptive curriculum. At each iteration, CodeLift groups tests that kill the same patches and patches that pass the same tests, then gives more weight to test groups that fewer patch groups pass. This reduces the impact of majority simple tests and focuses more on what is still challenging. Within each rollout, CodeLift applies the same scoring rule to repository snapshots, assigning credit to useful actions even when later ones introduce regressions. Experiments on SWE benchmarks show that CodeLift consistently improves pass@1/2/4/8 over binary and pass-rate baselines. Analyses show that CodeLift provides dense, stable learning signals and unlocks the inherent curriculum in the test suite.

---


### 555. [AReA: Adaptive Receptive-Field Attention for Efficient High-Resolution Diffusion Transformers](https://arxiv.org/abs/2610.17227)

**<font color=#1a73e8>作者：</font>** Javad Rajabi, Koorosh Roohi, David B. Lindell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating images beyond the training resolution of Diffusion Transformers (DiTs) remains challenging, as the number of tokens grows rapidly with resolution, full attention becomes expensive, and outputs often suffer from structural distortions and degraded detail. We identify uniform full attention as the common source of both problems. Attending to all tokens at every step causes quadratic cost and exposes the model to more tokens and relative distances beyond the training range, pushing the model out of distribution. We observe that attention's effective receptive field narrows during denoising, from global in early steps that form structure to local in later steps that refine details. We propose AReA, a training-free attention mechanism whose receptive field evolves from coarse to fine, following the denoising progression. In early steps, AReA applies cross-scale coarse attention over downsampled keys and values, capturing global context, while in later steps it applies local attention within progressively shrinking windows. Without additional parameters or training, experiments show that AReA consistently outperforms state-of-the-art training-free baselines across target resolutions and different models, while also being faster and more efficient.

---


### 556. [Beyond Sparse Captions: Aligning Slide-Level Text and Patch-Level Vision in Pathology](https://arxiv.org/abs/2610.17233)

**<font color=#1a73e8>作者：</font>** Daniel Shao, Dongmin Bang, Luca L. Weishaupt 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive vision-language (VL) pretraining in computational pathology has generally relied on curated image-caption datasets sourced from social media, educational videos, and research publications. These corpora are sparse relative to the diversity of tissue morphology and difficult to scale further, as pathologists do not routinely produce descriptive captions in clinical practice. We propose to instead leverage slide-level pathology reports which can be generated during routine diagnostic workflows in a scalable manner. A key challenge in this weakly-supervised setting is that pathology reports describe macroscopic, diagnostic findings while patch-level visual features describe microscopic findings. We introduce Locked Image Multiple Instance PreTraining (LIMIT), which addresses this gap by freezing a pretrained vision encoder and fine-tuning only the text encoder: report embeddings serve as cross-attention queries over bags of patch features, producing report-conditioned slide representations optimized via InfoNCE. Using LIMIT, we establish CONCH-Z, which aligns the text encoder of CONCH v1.5 to 335k clinical reports. Evaluated across 22 tasks spanning patch-level classification, tumor detection, and slide-level subtyping, CONCH-Z establishes state-of-the-art zero-shot performance over VL encoders trained on curated caption datasets, while simultaneously closing the gap with slide-level foundation models trained with substantially more parameters and compute. The code and model is available at this https URL.

---


### 557. [IsoVRBench: Video Reward Modeling Without Human Feedback](https://arxiv.org/abs/2610.17234)

**<font color=#1a73e8>作者：</font>** Shuyue Stella Li, Jacqueline He, Jiahui Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video reward models are trained and evaluated on human preferences between videos that often differ simultaneously on properties such as prompt alignment, visual fidelity, motion, and generator identity. As a result, aggregate accuracy does not reveal which video properties a reward model can reliably distinguish. We construct preference pairs by controlled interventions that change one property of a generated video while holding the rest fixed. The resulting pairs, by construction, provide preferences for how the videos differ along a specific dimension, without requiring any human annotation. We propose IsoVRBench, a video generation reward modeling benchmark of 8,000 such pairs across eight interventions, and show that state-of-the-art models separate broad quality differences between generators but miss important features such as temporal order. The best reward model reaches only 60.8% on reordered frames against 100% for humans, and rankings on existing benchmarks do not predict this failure. Using the synthetic isolated intervation pairs as training data leads to 1) IsoVRM, a reward model outperforming its counterpart trained with a larger human labeled preference dataset by 3.8 points on VBench-2.0, 2) IsoWan, the video generator post-trained with IsoVRM, outperforming its human-data counterpart in human preferences, and 3) gains that stack when combined with human data. Because intervention pairs are automatically generated rather than collected, the benchmark and training data can be easily extended as generators evolve.

---


### 558. [MIRRA: Fast, High-Fidelity Molecular Generation with Chemistry-Informed Discrete Flow Matching](https://arxiv.org/abs/2610.17244)

**<font color=#1a73e8>作者：</font>** Ge Sun, Juan J. de Pablo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast, high-fidelity molecular generation requires accurate chemical choices and efficient sampling. Chemical building blocks reduce graph size, but make each node a choice among tens of thousands of related identities. We introduce MIRRA (Molecular Identity Representation, Refresh and Assembly), a discrete flow-matching generator that learns from chemical knowledge and evaluates identity probabilities only when needed, while keeping every identity in its vocabulary available. Chemical features share information across related blocks, and learned identity corrections distinguish them in molecular context. By deciding which positions will refresh before computing their probabilities, the sampler avoids unused predictions while preserving each sampling transition. Against the strongest baselines in each task, MIRRA reduces chemical and graph distribution errors on ZINC250k by 29-31% and 53-60%, respectively, with generation up to 8.6 times faster. Property targeting yields an estimated 7.8-20.8 times more distinct novel hits per second. On a held-out polymer test set, MIRRA achieves 100% periodic validity with known chain topology, versus 57.0% for a polymer variational autoencoder. These results demonstrate fast, high-fidelity generation with the full chemical vocabulary available throughout sampling.

---


### 559. [Tight End-to-End Accounting for Differentially Private Synthetic Data](https://arxiv.org/abs/2610.17249)

**<font color=#1a73e8>作者：</font>** Georgi Ganev, Vadym Doroshenko, Arun Ganesh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differentially private (DP) pipelines often combine heterogeneous mechanisms, yet their guarantees are best analyzed using different notions of privacy (e.g., bounded range, zCDP, ADP). When composing them, we have to analyze the guarantees through a reduced common representation that loses accounting precision. This issue is particularly relevant in DP synthetic data generation, where data preprocessing, generation algorithms, and DP-SGD could appear within the same pipeline. We develop novel tools for tight end-to-end accounting of such compositions using privacy loss distributions (PLD), $f$-DP, and Gaussian DP (GDP). In particular, we derive PLD and GDP analyses of bounded-range mechanisms such as the Exponential mechanism. Building on these theoretical results, we introduce AIM-GDP, a GDP-native variant of AIM (a state-of-the-art DP synthetic data mechanism) that enables easy composability with complex pipelines via PLD, attack-aware risk calibration, and tight end-to-end auditing while consistently achieving better utility; and MixCal, an algorithm for calibrating adaptive mixed compositions using PLD accounting. Overall, our tools enable tighter end-to-end accounting and thus less noise at the same privacy level in DP synthetic data pipelines.

---


### 560. [HybridDualPathNet: Cross-Fusion Attention of EfficientNetV2 and Swin Transformer for Brain MRI Classification of Alzheimer's and Parkinson's Disease](https://arxiv.org/abs/2610.17251)

**<font color=#1a73e8>作者：</font>** Jarpula Nirjala, Rahul Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Separating Alzheimer's Disease (AD), Parkinson's Disease (PD), and Healthy Controls (HC) using structural MRI remains challenging because disease signatures overlap and model performance can be strongly affected by data partitioning. We present HybridDualPathNet, a hybrid architecture combining EfficientNetV2-S for local features and Swin-Tiny for global context through a Cross-Fusion Attention (CFA) module. We evaluate the model in two experiments. First, on the Kaggle APD-3-Class dataset using an image-level split, the model achieves 98.25% accuracy. Second, on a combined Kaggle and Alzheimer's Disease Neuroimaging Initiative (ADNI) dataset containing 17,859 slices, we use a per-source split with patient-wise separation for ADNI subjects. In this setting, the model achieves 73.37% standard accuracy and a macro AUC of 0.880. Source-stratified evaluation reveals a substantial domain gap, with 91.2% accuracy on Kaggle test images and 59.2% on ADNI test images. Temperature scaling reduces expected calibration error from 0.130 to 0.015, while split-conformal prediction achieves 89.5% coverage. Saliency analyses using Grad-CAM++, Integrated Gradients, and occlusion indicate that model activations concentrate on brain tissue. These results highlight the importance of patient-level separation, cross-dataset evaluation, and uncertainty estimation when assessing MRI classification systems. The findings also show that strong performance on a single dataset does not necessarily translate to reliable generalization across imaging cohorts.

---


### 561. [Protocol Choices Matter More Than the Aggregation Algorithm: Federated Learning for In-Hospital Mortality Prediction in Care-Unit and Multi-Hospital Federations](https://arxiv.org/abs/2610.17265)

**<font color=#1a73e8>作者：</font>** Rodrigo Tertulino, Ricardo Almeida, Laércio Alencar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning allows hospitals to train a shared mortality model without pooling their records, but published comparisons of aggregation strategies rarely control the evaluation protocol. This study compared seven strategies (FedAvg, FedProx, SCAFFOLD, FedAdagrad, FedAdam, FedYogi and FedCluster) on two federations built with one pipeline: 12 care units of a hospital in MIMIC-IV and 49 hospitals in eICU-CRD. Each strategy was tuned and selected on validation data by the same rule, and every comparison was repeated across 10 seeds with Friedman and Holm-corrected tests. SCAFFOLD ranked first in both federations (AUC-ROC 0.886 and 0.819) and in 17 of 18 variants, but its margin over the runner-up never exceeded 0.008, and a control sharing its local optimizer attributed most of its margin over FedAvg to drift correction. On the multi-hospital federation, federated training matched centralized training. In the care-unit federation, three protocol choices changed discrimination by more than the choice of strategy did: discharge-coded predictors (+0.038 in AUC-ROC), client-level SMOTE (up to -0.074), and evaluating the last instead of the best validation round (up to -0.084). Platt scaling on validation data repaired the risks distorted by imbalance corrections without loss of discrimination. Studies should therefore fix the protocol before ranking algorithms.

---


### 562. [Measuring Learned Equivariance: An Information Theoretic Approach](https://arxiv.org/abs/2610.17269)

**<font color=#1a73e8>作者：</font>** Claire Schlesinger, Wolfgang Gatterbauer, Robin Walters  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning symmetries through data augmentation offers an alternative to architectural equivariance, but does not guarantee that a network respects those symmetries. Measuring learned equivariance is especially difficult for intermediate representations, whose group actions are not specified. In a finite discrete setting, we show that equivariance requires representations of original and transformed inputs to determine one another exactly, yielding a test based on normalized mutual information (NMI). For high-dimensional activations, we use centered kernel alignment (CKA) as a scalable test, with an exact guarantee for orthogonal feature transformations. Across architectures and tasks, augmentation usually increases transformation consistency, showing that learned equivariance can be probed directly from representations without recovering the hidden transformation rules that relate them.

---


### 563. [Reasoning for Propaganda Detection via Label-Guided CoT Optimisation](https://arxiv.org/abs/2610.17271)

**<font color=#1a73e8>作者：</font>** Zeba Afroz, Harsh Vardhan, Md. Shad Akhtar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Propaganda detection systems usually operate as black boxes, lacking explanations. To address this, we hypothesise that persuasive techniques contain definitional characteristics with respect to their social-political setting. We introduce ReCoT, a reasoning-conditioned detection framework that captures definitional cues of persuasive techniques via population-level refinement and performance-guided resampling, without requiring additional explanation annotations. On INDI-PROPspan, ReCoT achieves a macro F1_LCS of 0.364, surpassing baselines and reaching 88% of the SFT upper bound on Avg F1_LCS. Similarly, on PTC, ReCoT reaches 85% of the SFT upper bound on Avg F1_LCS, closing much of this gap while remaining interpretable. Importantly, the analysis of the reasoning pool's convergence and update pattern for ReCoT shows effective refinement of reasoning CoTs.

---


### 564. [Nufo: A Benchmark for Ewe Automatic Speech Recognition](https://arxiv.org/abs/2610.17278)

**<font color=#1a73e8>作者：</font>** Christ Kekeli Keli, Steve Sanogo, Patrice Sebastiano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) remains challenging for low-resource languages, where the scarcity of transcribed speech limits the development of accurate systems. This challenge is particularly acute for African languages such as Ewe, which has millions of speakers but remains underrepresented in publicly available ASR resources and benchmarks. In this work, we consolidate, normalize, and partition existing Ewe speech resources into a standardized 174-hour Ewe ASR benchmark, the largest to date to our knowledge. We fine-tune and evaluate pretrained speech models, including Whisper and AfriHuBERT, to establish strong baselines on our benchmark. Whisper-medium achieves a word error rate (WER) of 37.98%, while AfriHuBERT achieves 39.70% on the test set. We further provide a qualitative analysis of common recognition errors. We release the benchmark under the name Nufo, derived from the Ewe word for "talk", accompanied by models and evaluation resources, to facilitate future research on Ewe and other underrepresented African languages.

---


### 565. [Towards Resilience: Slice-Driven Orchestration of Mobile IoMT in 6G-Edge-Continuum](https://arxiv.org/abs/2610.17296)

**<font color=#1a73e8>作者：</font>** Muhammad Zeeshan, Hafiz Faheem Shahid, Erkki Harjula  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emerging healthcare services, such as real-time diagnostics, remote health monitoring and computer-assisted surgery, require stringent Quality of Service (QoS) guarantees while operating under limited and heterogeneous edge resources. Existing Internet of Medical Things (IoMT) orchestration methods primarily focus on communication metrics such as latency and bandwidth, while overlooking edge resource constraints and dynamic adaptation to workload and user mobility. This paper presents a novel resource-slicing-based adaptive orchestration framework that integrates 5G network slicing (NS), resource-aware orchestration, and mobility-aware task offloading into a single adaptive system. IoMT services are assigned to distinct 5G network slices while jointly considering CPU capacity, memory availability and amount of storage, enabling more efficient service placement and execution. In addition, the system supports user mobility and dynamic task offloading to maintain service continuity under changing network conditions. SimPy-based simulation demonstrates that the proposed method enhances service deployment efficiency, reduces request blocking, and improves user acceptance while maintaining reliable performance across diverse IoMT scenarios.

---


### 566. [TouchTwin: Human-AI Haptic Authoring for 3D-Scanned Tabletop Scenes through Language and Touch](https://arxiv.org/abs/2610.17302)

**<font color=#1a73e8>作者：</font>** Wanli Qian, Xinlei Yu, Heather Culbertson  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Creating haptic experiences from real-world environments remains difficult: visual scans capture appearance but not material feel, while manual haptic authoring requires specialized expertise. We present TouchTwin, a human-AI approach that turns phone scans of tabletop scenes into editable haptic scenes. TouchTwin uses AI to propose material regions that users can experience and revise through language and spatial edits. A model trained on measured tool-surface interactions generates the haptic responses, allowing users to work with material descriptions rather than low-level signal parameters. In a study with N=12 participants and physical reference objects present, automatic drafts scored 4.0/7 for realism and 5.4/7 as useful starting points. After a median of 6.6 minutes of editing, realism increased to 5.6/7, while scoring the saved material layers against ground truth showed material-family accuracy improving from 52% to 92%. Participants also used the same workflow to author material feels without a physical reference.

---


### 567. [StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions](https://arxiv.org/abs/2610.17309)

**<font color=#1a73e8>作者：</font>** Xialie Zhuang, Zunhai Su, Jia Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce StartLux-Decision, decision models from 0.8B to 27B parameters that combine efficient single-pass prediction with adaptive, confidence-guided reasoning. The Instant models use bidirectional attention in full-attention layers to improve decision accuracy while keeping single-pass inference. The AutoThink models invoke explicit reasoning for uncertain decisions and answer confident cases directly. A three-stage training pipeline establishes shared decision capabilities, specializes the two variants, and equips AutoThink with reasoning through reasoning supervision and reinforcement learning. We introduce Reinforcement Learning for Calibrated Deliberative Decisions (RLCD$^2$), which uses a frozen model and proper scoring rules to reward improvements in decision probability quality and applies a soft penalty to overlong reasoning traces. RLCD$^2$ raises the share of reasoning traces that terminate within the generation limit by up to 48 percentage points and cuts average reasoning length by up to 65%, while largely preserving decision accuracy. On the public subset of Decision Index 0.3, the Instant models outperform the strongest evaluated comparable-scale open-weight decision models by 7.4-16.9 points, and the 27B AutoThink model reaches 73.4. We also introduce DecisionPivot, a programmatically verifiable benchmark of computational decisions built from contrast pairs that differ in a single answer-changing detail. On DecisionPivot, AutoThink outperforms its Instant counterparts by 11.5-18.4 points in pair accuracy and leads among evaluated systems. The models run on vLLM, this http URL and MLX, with quantized variants for lower memory use.

---


### 568. [A Geometrical Approach to Constructing Neural Networks for Perfect Training-set Classification](https://arxiv.org/abs/2610.17312)

**<font color=#1a73e8>作者：</font>** Akos Hajnal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a method for constructing a neural network that achieves perfect classification of all samples in a given training set, without taking regularization into account. The network is constructed on-demand, with its layer sizes and neuron parameters determined through a geometrical analysis of the input data, in which separating hyperplanes are created and mapped to neurons with step activation functions. The proposed architecture consists of two hidden layers with distinct roles: inter-class separation and transformation of the data into a linearly separable representation. Inter-class separation requires every bi-chromatic pair of samples belonging to different classes to be separated by at least one hyperplane. We show that when this separation is achieved through a hierarchical partitioning of the data, the leaf nodes of the oblique decision tree, obtained as a byproduct, directly define the neurons of the linear separability layer, whose size is only one neuron greater than that of the inter-class separation layer. Experiments on the MNIST dataset demonstrate that the proposed method achieves perfect training-set classification, and compact models. The direct correspondence between the decision tree and network neurons enhances interpretability and explainability, while the construction procedure offers opportunities for parallel implementation and improved scalability.

---


### 569. [Joint Embedding with Dynamic Integration network (JEDI-net)](https://arxiv.org/abs/2610.17314)

**<font color=#1a73e8>作者：</font>** Rishav Mukherjee, Jeffrey Ahearn Thompson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has become the dominant form of machine learning due in part, to its ability to automatically engineer complex meta features from data. However, even deep learning features can perform erratically because of unobserved latent factors. incorporating latent factor information explicitly, can improve performance by letting the model alter its behavior based on such inferred factors. Because neural networks often capture such complexity inherently, external clustering of the original feature space offers limited benefit. clustering observations by feature importance profiles, rather than raw features, offers a principled way to uncover latent structure, since observations with similar importance patterns may share predictive dynamics. In a prior work, Feature Oriented Representation with Clustering and Explanation (FORCE) we showed that this approach measurably improved neural network performance. In this article, we present JEDI-net(Joint Embedding with Dynamic Integration Network) a unified architecture that periodically clusters SHAP values during optimization to identify latent subgroups with similar feature importance patterns, embed their identities directly into the network, allowing predictions to adapt to each observations predictive structure.

---


### 570. [Near-Optimal Regret Bounds for Monotone Stochastic Optimization under Semi-Bandit Feedback](https://arxiv.org/abs/2610.17320)

**<font color=#1a73e8>作者：</font>** Tao Hu, Rohan Ghuge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic optimization models sequential decision-making under uncertainty, typically assuming known input distributions. When these distributions are unknown, \citet{agarwal2026semibandit} give an online-to-offline reduction for monotone stochastic optimization under semi-bandit feedback, where only probed variables are observed. Its expected regret relative to the offline guarantee is $\widetilde O(n\sqrt T)$, where $n$ is the number of variables and $T$ the horizon. For optimal stopping and Pandora's box, \citet{liu2025improved} achieve $\widetilde O(\sqrt{nT})$ using problem-specific algorithms. \emph{Can a general online-to-offline reduction achieve this improved rate?}
We give such a reduction for strongly monotone stochastic optimization, answering the corresponding open question. Strong monotonicity is defined relative to the chosen offline algorithm. Our oracle-efficient reduction achieves $\widetilde O(\sqrt{nT})$ expected regret while preserving approximation guarantees for oracles satisfying the same condition. It combines Bernstein-type optimistic distribution estimates with a Hellinger stability bound for adaptive policy transcripts, aggregating squared marginal errors weighted by the executed policy's probing probabilities. The rate is optimal up to logarithmic factors for $T\ge n$, even under full feedback.
Under monotonicity and uniformly bounded coordinate-wise variation, the same algorithm achieves $\widetilde O(n^{3/4}\sqrt T)$ expected approximation regret, improving the previous linear dependence on $n$. The exponent $3/4$ is sharp for its ordinary regret over instances and exact oracle choices. Our framework applies to prophet inequality, Pandora's box, best-of-$K$ selection, stochastic knapsack, stochastic orienteering, and stochastic submodular maximization.

---


### 571. [SSM-Attack: Learning Where to Perturb for Black-Box Face Privacy](https://arxiv.org/abs/2610.17323)

**<font color=#1a73e8>作者：</font>** Tunahan Parlayıcı, Erchan Aptoula, Yücel Saygın  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition systems are deployed widely enough that a photograph shared online can be matched without its subject's consent. Generator-based protection methods rely on heavy pretrained backbones, multi-stage inference or visible semantic edits. We introduce SSM-Attack, a black-box face privacy framework built on Selective State Space Models. Rather than synthesizing the perturbation, the state-space model predicts in one linear-time pass a spatial allocation of the perturbation budget, marking which facial locations carry identity evidence; a short projected refinement then sets the values within this per-pixel budget. Against published benchmark results, SSM-Attack attains the highest average black-box attack success rate on all three evaluation sets: 87.10 percent on CelebA-HQ, 86.90 on LADN and 81.15 on FFHQ, the last from a network that never saw that dataset. The allocation network holds 5.73 million parameters, or 16.13 million with the frozen networks used by its quality terms. Under the same cap of 0.10 on the maximum per-pixel change, allocation improves structural similarity by 0.044, peak signal-to-noise ratio by 1.62 decibels and Frechet Inception Distance by 11.2 points over a uniform map while spending 37 percent of its capacity. Strong facial privacy protection therefore does not require a large generative prior; it requires knowing where to spend a small one.

---


### 572. [Thinking Outside the Bots: Human Ideas in AI's Semantic Blind Spots Are Not Inferior](https://arxiv.org/abs/2610.17324)

**<font color=#1a73e8>作者：</font>** Kibum Moon, Dan R. Johnson, Kostadin Kushlev 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-generated outputs are frequently perceived as highly creative, but also tend to be more similar to each other (homogenized) than human ideas. Does the human heterogeneity that extends beyond AI reflect valuable thinking that AI misses? Alternatively, is greater human heterogeneity driven by lower-quality ideas and less effective thinking that AI avoids? We developed Expansion of Divergent Generative Expression (EDGE) to map AI's semantic "blind spots" by assessing how strongly/weakly individual human ideas were represented in a task-matched AI semantic comparison set. Specifically, we compared human-generated vs. AI-generated ideas across three open-ended tasks: college admissions essays, alternative uses for everyday objects, and interpersonal advice. Across all three tasks, human responses extended into semantic regions sparsely covered by AI outputs. These distinctively human responses showed no meaningful deficits in creativity, quality, or effectiveness, were associated with equal-or-better academic performance, and with credibly superior ratings and achievement for some outcomes. These ideas were thus not merely poor-performing variation; they performed as well as or better than ideas that overlapped more strongly with AI ideas. More distinctive human ideas tended to receive higher creativity ratings, but this relationship was weak or reversed for AI ideas. Taken together, these results suggest that differentiation among human-generated ideas does not reflect poor thinking that AI can safely omit, and instead may afford both individual and population-level advantages.

---


### 573. [Human Situational Awareness and Workload during Heterogeneous Autonomous Vehicle Hazard Monitoring: A Cross-Platform Study](https://arxiv.org/abs/2610.17339)

**<font color=#1a73e8>作者：</font>** Ziyue Wang, Yang Xing, Argyrios Zolotas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As autonomous ground and aerial vehicles become increasingly capable, human operators are transitioning from direct control to supervisory monitoring roles. Maintaining Situational Awareness (SA) during rare but safety critical hazard events remains a fundamental challenge, particularly when operators must monitor heterogeneous autonomous platforms with different spatial and cognitive demands. This study develops a unified experimental framework for investigating human SA and workload during supervisory monitoring of autonomous ground and aerial vehicles under hazard conditions. Eighteen participants completed six within-subject conditions combining three interface modalities, namely, visual-only, haptic-only, and visual-haptic, with two platform types, ground vehicle and aerial drone. SA was measured using Situation Awareness Rating Technique (SART), while workload was assessed using the NASA Task Load Index (NASA-TLX). The key findings are: 1) Aerial monitoring produced significantly lower overall SA, higher situational demand, and greater workload than ground monitoring, driven by elevated Demand and reduced Understanding rather than diminished Supply. 2) Workload was consistently coupled with situational demand across all conditions, suggesting a stable SA-workload mechanism. 3) Both haptic-only and visual-haptic significantly improved overall SA relative to visual-only without increasing workload, demonstrating that interface design can enhance awareness within the existing workload envelope. These findings establish a cross-platform behavioural baseline for designing multimodal interfaces that enhance operator SA without elevating workload in heterogeneous autonomous vehicle systems.

---


### 574. [On the Statistical Mechanics of Attention](https://arxiv.org/abs/2610.17347)

**<font color=#1a73e8>作者：</font>** Jerry Yao-Chieh Hu, Yu-An Chen, Maojiang Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We revisit the statistical mechanics of Transformer attention via modern Hopfield models. We present a free-energy formalism to characterize parameter regimes and critical thresholds for robust attention inference. The resulting free-energy landscape incorporates randomness in query states and attention weights. Attention then emerges as the equation of motion of the corresponding statistical-mechanical system (i.e., modern Hopfield model) through the standard free-energy minimization principle. This allows us to identify first-order phase transitions in attention between glassy and robust-inference phases. We further extend to attentions with stochastic queries and keys. Together, our results provide a rigorous statistical-mechanics framework for characterizing phase structure and inference reliability across a family of Transformer attention mechanisms.

---


### 575. [HairFlow: Modeling 3D Hair Strands with Multi-Modal Conditioned Diffusion](https://arxiv.org/abs/2610.17348)

**<font color=#1a73e8>作者：</font>** Yating Wang, Kui Wu, Ran Yi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling 3D hair strands is challenging due to complex hairstyle geometry, scarce high-quality training data, and incomplete or noisy input observations. Foundation models offer broader hairstyle priors, but their outputs are not directly usable for strand-based rendering and simulation. Existing approaches require costly per-instance optimization to fit hair priors to meshes from foundation models and 2D orientations from specialized predictors trained on limited hair data, restricting efficiency and generalization. We present HairFlow, a multimodal conditioned diffusion framework for efficient and controllable hair strands modeling. HairFlow conditions strand generation on two complementary representations: a coarse mesh that constrains global shape and multi-view sketches that specify local strand flow. HairFlow combines an Orientation VAE with a conditioned diffusion transformer to generate volumetric fields that are traced into explicit strands. To overcome the lack of paired sketch-strand training data, we introduce an automatic synthesis pipeline that generates geometrically aligned multi-view sketches with diverse styles representative of inference-time inputs. Experiments show that HairFlow generates plausible 3D strands that faithfully follow the input conditions across diverse hairstyles, substantially reduces inference time, and supports flexible multimodal control.

---


### 576. [MID: Mask-Image Distributional Divergence for Evaluating Medical Image Segmentation](https://arxiv.org/abs/2610.17354)

**<font color=#1a73e8>作者：</font>** Vincenzo Marcianò, Xiaoming Zhang, Gianluca Guglielmo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current evaluation protocols for medical image segmentation remain largely anchored in sample-wise comparisons, e.g., Dice and Hausdorff distance, which require each prediction to be paired with a ground-truth mask. Yet two limitations arise in practice: they are inapplicable when predictions are made on unlabeled data; and even when annotations are available, they cannot assess whether a collection of predictions matches the distributional structure of the ground-truth population. We introduce MID (Mask-Image Distributional Divergence), a distribution-level evaluation metric for medical image segmentation. MID builds upon the observation that segmentation quality is a property of the joint image-mask distribution: a mask may be anatomically plausible in isolation yet incorrect for the image it accompanies. MID compares the joint distribution of images and masks between a reference set and a set of predictions, without requiring sample-wise correspondence. This captures both mask realism and image-mask consistency. We evaluate MID across 13 publicly available datasets spanning CT, MRI, and MRA. Under anatomically realistic corruptions across 56 organ groups, MID tracks mean Dice and Hausdorff distance without per-sample ground-truth pairing. MID also detects distributional shifts across modalities and anatomies, identifies image-mask misalignment through controlled shuffling experiments, and produces reliable model rankings across real segmentation models. Official implementation available at this http URL

---


### 577. [Brain2Face: A Study on the Relation of EEG Signals and Spatio-temporal Head Avatars](https://arxiv.org/abs/2610.17356)

**<font color=#1a73e8>作者：</font>** Camilo Andrés Martínez Martínez, Olaf Dünkel, Kartik Teotia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving digital head avatars is classically done by hand-crafted artist design or by image-based facial performance capture. In this work, we ask whether spatio-temporal tracking of the humans's head geometry and appearance can be performed solely from brain signals, i.e., Electroencephalography (EEG). Since prior work mostly focused on activity and emotion recognition, this task is relatively unexplored without even having publicly available high-quality datasets and benchmarks. Thus, we contribute a dataset featuring paired EEG and human head geometry as well as appearance annotations. We synchronize 64-channel EEG with per-frame expression latent codes of a personalized Gaussian head avatar. Second, we introduce a baseline to the task of expression recovery of a head avatar from EEG signals. To this end, we propose a dedicated EEG-to-expression model that takes a temporal sequence of EEG signals as input and regresses the latent expression parameters of the 3D Gaussian head avatar. Lastly, we validate our capture and algorithmic design choices through a benchmark protocol that we introduce to this task. We believe this work paves the way towards better understanding of the relation between EEG signals and facial surface as well as appearance changes.

---


### 578. [What Makes a Latent Space Shared? Direct and Recoverable Compatibility in Motion VAEs](https://arxiv.org/abs/2610.17376)

**<font color=#1a73e8>作者：</font>** Iago Brito, Walcy Rios, Lucas Fernandes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A shared latent space is often assumed to make representations from different schemas directly interchangeable, yet sharing parameters, dimensionality, or a prior does not determine how corresponding instances are expressed in latent coordinates. We show that this assumption conflates recoverable correspondence, direct compatibility, and decoder reuse. In a controlled multi-schema motion VAE on HumanML3D, even identical inputs yield only $5.9$--$17.7\%$ raw Recall@1 and $0.221$--$0.484$ paired-token cosine, despite correspondence being almost perfectly recoverable after linear calibration. Cycle consistency strengthens recoverability but still leaves direct retrieval and token agreement near zero. In contrast, only $64$ paired clips raise raw Recall@1 to $88.4$--$90.3\%$ and token cosine to approximately $0.82$, making most post-hoc alignment unnecessary, although crossed decoding remains substantially worse than native reconstruction. We further find that reducing measured marginal discrepancy does not imply schema invariance. These results show that a shared backbone or prior does not ensure directly compatible latent coordinates, while limited paired correspondence can substantially improve direct compatibility in the tested setting.

---


### 579. [Get In, Decide, Prove: A Merchant-Side Readiness Benchmark for Agentic Commerce](https://arxiv.org/abs/2610.17378)

**<font color=#1a73e8>作者：</font>** Adrian de Valois-Franklin, Alex Bogdan, Anas Ibrahim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents now browse and buy on people's behalf, and benchmarks measure how well the agents perform. Far less is known about the other side of the transaction: whether a merchant's website lets an agent in, publishes terms precise enough to decide a purchase, and leaves evidence of what was agreed. This paper presents a merchant-side benchmark built on those three questions and reports a pilot of it. The central measurement, decision sufficiency, rates each criterion of a concrete buyer mandate (total cost, cancellation or return terms, service date, variant identity) as determinate, indeterminate, or unknown from the merchant's own published evidence. Readiness scores carry their evidence coverage and missingness bounds; access is reported separately for a declared bot, a declared headless browser, and a user-present browser; and each observed term is mapped to the RAILS admissibility class of the evidence that could support it in a dispute. Four large merchants received the full assessment: three refused the declared profiles at their offer pages, and no mandate could be confirmed as met, because each merchant left a total or a refund term undetermined. An access census of 555 sites of merchants that two payment processors publicly name as clients found the home page unreadable to both declared profiles at 105 sites (18.9%). A declared assessment of 330 merchants, scored by deterministic rules without a rater, found that evidence coverage rather than the score decides who can be ranked: 115 merchants (35%) reached the ranking threshold, rankable profiles scored a median of 89 to 90, and material terms was the one pillar well below the others, because the all-in total was decidable at 18 merchants. The pilot shows that the measurements can be taken; it does not validate them or rank merchants, and the weights and the projected clearing band await validation against outcomes.

---


### 580. [Robustly Reliable Learning for Regression](https://arxiv.org/abs/2610.17381)

**<font color=#1a73e8>作者：</font>** Avrim Blum, Anh Tuan Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the problem of robustly reliable learning for the regression setting in adversarial environments. Given a test point $x_{test}$, a training dataset $S$ of $n$ data points, a corruption budget $b \ll n$, and a real-valued hypothesis class $\mathcal H$, our goal is to output the optimal prediction range $I^*_{x_{test}}(S, b)$, such that any $L$-Lipschitz predictor consistent with all but at most $b$ points in $S$ must predict a value $h(x_{test}) \in I$. We then instantiate the analysis for $L$-Lipschitz hypothesis classes, a natural and widely studied class in the regression setting, focusing on two key scenarios. First, for the restricted case where the corrupted dataset is guaranteed to be $L$-Lipschitz consistent, we propose a simple and efficient $b^{th}$-best heuristic algorithm and prove its correctness in computing the tightest possible range $I^*_{x_{test}}(S, b)$. We then establish its computational complexity of $O(n)$ and show that it is computationally optimal in this scenario. Building on this foundation, we address the general scenario where the dataset $S$ is no longer $L$-Lipschitz consistent. We demonstrate that computing the optimal range in this setting reduces to analyzing a violation graph, which models the pairwise $L$-Lipschitz violations among data points. By leveraging the structural properties of this graph's kernel, we propose a Fixed-Parameter Tractable (FPT) algorithm that computes the exact optimal range in $O(n^2 + b^4)$ time. Furthermore, under the Strong Exponential Time Hypothesis (SETH), we establish a computational lower bound of $\Omega(n^{2 - o(1)})$, proving that our algorithm is computationally optimal. Finally, we discuss open directions for the problem of robustly reliable learning for regression.

---


### 581. [Mitigating Black-Box Score-Based Query Attacks via Gradient Confusion](https://arxiv.org/abs/2610.17382)

**<font color=#1a73e8>作者：</font>** Ali Javeri, Javad Hezareh, Radin Shahdaei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based black-box adversarial attacks pose a serious threat to deployed machine learning systems by exploiting repeated model queries to craft adversarial examples, requiring neither access to model parameters nor architecture. Existing defenses predominantly rely on stochastic output perturbations, which fail to prevent determined attackers from recovering stable gradient estimates by increasing query budgets or averaging over randomness. In this work, we propose the Gradient Confusion Defense (GCD), a retraining-free, deterministic test-time wrapper that actively shapes the probability vector returned to querying adversaries. By solving a constrained optimization problem grounded in the model's Jacobian, GCD aligns the exposed logit-gradient with a target confusion direction that is maximally misaligned with the true adversarial loss gradient---increasing the query complexity of attacks without sacrificing predictive utility or top-1 accuracy. We provide rigorous theoretical analysis demonstrating that GCD provably slows gradient-estimation-based attacks and induces systematic accept/reject errors in random search-based attacks, with the confusion effect amplifying as the fraction of defended queries increases. Extensive experiments on CIFAR-10 and ImageNet across multiple architectures (ResNet-18, ResNet-50, ViT-B/16) and four state-of-the-art attacks confirm these predictions: GCD achieves state-of-the-art robustness, while incurring zero clean accuracy degradation. %Crucially, unlike randomization-based defenses, GCD's deterministic structure provides resilience against adaptive attacks that exploit stochasticity, making it well-suited for security-critical deployment settings.

---


### 582. [Variable Input Masked Autoencoders for Wrist-Worn Accelerometry](https://arxiv.org/abs/2610.17383)

**<font color=#1a73e8>作者：</font>** Harish Haresamudram, Wanting Mao, Aditya Radhakrishnan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale repositories of wearable sensor data have enabled the development of foundation models for human activities and behavior. However, existing models are pretrained using fixed input durations and sampling rates, despite substantial heterogeneity in recording conditions, downstream tasks, and deployment constraints. We introduce VarMAE, a variable input masked autoencoder that learns a single representation across sampling rates and temporal contexts. During pretraining we construct two views of the same signal: a long duration high frequency view, and a short duration lower frequency view, obtained via random cropping and downsampling. We perform masked reconstruction within each view and introduce a cross-resolution masked reconstruction objective that uses visible tokens from the long view to predict masked tokens from the short view. Cropping and downsampling impose complementary information bottlenecks, encouraging the model to learn representations that remain effective across input durations and sampling rate changes. We pretrain VarMAE on the large-scale NHANES dataset, producing a single pretrained encoder matching or outperforming controlled foundation model baselines on eight benchmark datasets. With only 3.82M parameters, VarMAE is parameter efficient and shows that a single foundation model can achieve broad transfer capabilities across sensing configurations.

---


### 583. [Measure Neural Mappings](https://arxiv.org/abs/2610.17384)

**<font color=#1a73e8>作者：</font>** Ricardo Baptista, Edoardo Calvello, Bohan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce and define measure neural mappings (MNMs), which combine measure-dependent neural transport with ensemble consistency for learning operators on probability measures. Ensemble consistency requires outputs from growing ensembles sampled from an input law to converge to the specified population output in probability. We establish quantitative continuum limits for attention on noncompact laws under strong sub-Gaussian and tail-integrability assumptions. These laws accommodate unbounded state spaces in scientific machine learning, including Bayesian inference and uncertainty quantification. For fixed self-attention transformers, the expected output Wasserstein error is bounded by the empirical input Wasserstein error plus an additional $N^{-1/2}$ attention term. These self-attention transformers are MNMs under the stated assumptions: pre-norm architectures follow from compact stability after normalization, while post-norm architectures are covered under the stated tail conditions. We prove corresponding cross-attention estimates and extend the results to multihead attention and grouped transformer evaluation, with convergence as the group size grows. For Set Transformers viewed as measure-to-vector mappings, we obtain an $N^{-1/2}$ bound on the expected Euclidean output error under the stated assumptions. Experiments on seven operators in dimensions $d=1,2,3,5,10$ support the predicted particle-count dependence, using one-dimensional Wasserstein computations and Sinkhorn approximations in higher dimensions. The observed Wasserstein and sliced Wasserstein decay rates are close to their respective theoretical sampling benchmarks.

---


### 584. [Cross-Market Meta-Learning for Electricity Price Forecasting](https://arxiv.org/abs/2610.17387)

**<font color=#1a73e8>作者：</font>** Delaram Pirhayatifard, Terrence Alsup  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Day-ahead (DA) electricity price forecasting is usually posed per market, with a separate model fitted to each grid's own history. This caps accuracy: statistical and tree-based baselines saturate, while higher-capacity sequence models need more training data than a single market's few years of hourly prices can supply. Such methods also treat each node as an independent series, discarding the spatial dependencies induced by network topology and congestion. Because price formation across independent system operators (ISOs) is driven by shared physics and largely common market design, we instead treat cross-market history as a pretraining corpus. We present MetaGrid, a topology-aware transformer, meta-trained across markets so that a single zone-count-independent parameter set adapts to an unseen grid. On a leak-free benchmark of five U.S. ISOs, where every model receives the same prices, DA load forecasts and calendar features, MetaGrid attains the lowest average MAE, improving on the best baseline by 3.1\% and on the same architecture trained from scratch by 7.7\%.

---


### 585. [Learning to Play: Reinforcement Learning and Games](https://arxiv.org/abs/2610.17391)

**<font color=#1a73e8>作者：</font>** Aske Plaat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Amazing breakthroughs in reinforcement learning have taken place. Computers teach themselves to play Chess and Go and beat world champions. There is talk about expanding application areas towards general artificial intelligence (AI). The breakthroughs in Backgammon, Checkers, Chess, Atari, Go, Poker, and StarCraft have shown that we can build machines that exhibit intelligent game playing of the highest level. These successes have been widely publicized in the media, and inspire AI entrepreneurs and scientists alike. Reinforcement learning in games has become a mainstream AI research topic. It is a broad topic, and the successes build on a range of diverse techniques, from exact planning algorithms, to adaptive sampling, deep function approximation, and ingenious self-play methods. Perhaps because of the breadth of these technologies, or because of the recency of the breakthroughs, there are few books that explain these methods in depth. This book covers all methods in one comprehensive volume, explaining the latest research, bringing you as close as possible to working implementations, with many references to the original research papers. The programming examples in this book are in Python, the language in which most current reinforcement learning research is conducted. We help you to get started with machine learning frameworks such as Gym, TensorFlow, and Keras, and provide exercises to help understand how AI is learning to play.

---


### 586. [Generalizable field of view extension for diffusion MRI via conditional flow matching](https://arxiv.org/abs/2610.17401)

**<font color=#1a73e8>作者：</font>** Gaurav Rudravaram, Lianrui Zuo, Ema Topolnjak 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Incomplete field-of-view (FOV) diffusion MRI (dMRI) acquisitions compromise whole-brain white matter analysis by excluding brain regions from tractography and connectivity studies. While deep generative models for dMRI FOV extension have been proposed, their generalizability remains limited by the acquisition-dependent nature of dMRI, where signal intensity varies with b-value, gradient direction, and scanner protocol, and the inherent 4D complexity of the data, making it difficult to train models that transfer across sites or acquisition schemes without retraining. We propose a flow-matching generative model that extends the dMRI FOV in both the superior and inferior directions by predicting apparent diffusion coefficients (ADC) in six directions, conditioned on the two nearest acquired slices and the full-FOV T1w image to enforce both local diffusion continuity and anatomical consistency. The ADC representation decouples the model from acquisition-specific b-values and gradient directions, providing a middle-ground across protocols. The model was trained on 3,103 subjects (5,105 sessions) across five different datasets spanning diverse acquisition schemes (b = 500 and 1000 s/mm$^2$; 21--192 gradient directions), four single-shell (b = 1000) and one multi-shell (b = 500/1000). Evaluated on 299 subjects across five independent datasets spanning b = 750--1500 s/mm$^2$ and 32--90 gradient directions, with single- and multi-shell schemes unseen during training, the proposed method achieves significantly improved bundle Dice score on downstream tractography (p < 0.01).

---


### 587. [Cross-View Time-Frequency Diffusion for Extreme-Aware Time-Series Generation](https://arxiv.org/abs/2610.17407)

**<font color=#1a73e8>作者：</font>** Lin Jiang, Rongchao Xu, Guang Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating realistic time-series requires faithfully reproducing rare but high-impact extreme events. Existing approaches often rely on specialized representations or extreme-focused training objectives, which may restrict the diversity of captured extremes or compromise overall distributional fidelity. We propose Cross-View Time-Frequency Diffusion (CrossTF), a framework that exploits discrepancies between time- and frequency-view denoisers for extreme-aware time-series generation. Our key empirical finding is extreme-sensitive cross-view asymmetry: moving along the direction connecting the two views' clean-sample estimates substantially changes extreme fidelity while having limited effects on overall generation quality. We further identify a late-stage cross-view window in which this discrepancy stabilizes and cross-view adjustments have a particularly strong effect on extreme fidelity. These findings motivate a staged optimization strategy in CrossTF: after training and freezing both denoisers, it only needs to learn step-specific fusion parameters within this window using an Extreme Value Theory-based objective under an energy-distance constraint. This formulation supports interpolation between and extrapolation beyond the view-specific estimates while limiting degradation in overall generation quality. Extensive experiments on seven real-world datasets against 11 baselines show that CrossTF improves extreme fidelity by 26.1% and overall performance by 7.4% relative to the strongest baselines. These results highlight cross-view discrepancy as an effective basis for low-dimensional optimization in extreme-aware time-series generation.

---


### 588. [Position: Beyond Training Time, Test-Time Coordination is Essential for Cooperative MARL](https://arxiv.org/abs/2610.17409)

**<font color=#1a73e8>作者：</font>** Dongsu Lee, Sooraj Sathish, Joonkyung Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We argue that cooperative multi-agent reinforcement learning (MARL) should treat test-time coordination as part of the problem definition rather than a deployment artifact. Our focus is on long-horizon, centrally monitored cooperative systems such as warehouse robotics, automated storage-and-retrieval systems, and cloud-resource scheduling, where teams share a reward, operate under shifting objectives, and already run with global telemetry at deployment. The dominant paradigm in this regime, centralized training with decentralized execution (CTDE), uses global information only during training and provides no coordination channel at execution. This is sufficient when agents are weakly coupled or the environment is stationary, but it fails when the team must realign after conditions change. The limitation is structural rather than algorithmic, and more training cannot add a channel that does not exist at execution time. We call this the recoverability gap. To address it, we name the underexplored design space of intermittent test-time coordination as centralized training with mixed execution (CTME), in which a coordinator observes global state and emits high-level signals while agents act locally. CTME is not a particular learning algorithm, but a cooperative MARL problem setting that makes test-time information structure explicit. It specifies team-level information, high-level signals, and update frequency after training, with CTDE recovered as a limit case. We do not argue that CTDE is obsolete. We argue that removing the test-time channel is a modeling choice, not a necessity, and the wrong default when global telemetry is available and teams must recover from drift.

---


### 589. [Agency as a New Organizing Abstraction for Computer Science](https://arxiv.org/abs/2610.17410)

**<font color=#1a73e8>作者：</font>** Ian Foster  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in large-scale machine learning have enabled agentic AI systems: persistent, autonomous computational entities that pursue goals, initiate actions, and interact with open environments. These systems are often framed as applications of foundation models. We argue that this framing is incomplete: agency is also a candidate new organizing abstraction for computer science. What is new is not the concept of an agent, nor runtime policy generation per se, but its general-purpose, open-ended form, in which systems can synthesize courses of action from goals, observations, and memory, over tools and environments for which no complete task-specific model was specified in advance. Thus agency becomes a systems-level abstraction as well as an AI modeling concept. Where the process abstraction organizes computation around executing programs, agency organizes it around pursuing goals under bounded resources: a process executes a program; an agent pursues a goal. From this perspective, the recurring failures of deployed agentic systems (runaway resource consumption, behavior redirected by adversarial content, opaque continuous operation) are symptoms of structural abstraction gaps, not isolated engineering defects. We examine these gaps across six dimensions (execution, interfaces, correctness, oversight, coordination, and persistence) and argue that closing them requires coordinated advances in systems,

---


### 590. [Bottlenecked semantic compression by representation reconstruction](https://arxiv.org/abs/2610.17412)

**<font color=#1a73e8>作者：</font>** Xiaoya Tang, Shilong Liu, Daniel Smolyak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers incur high computational costs when processing long visual token sequences. Existing reduction methods typically rank tokens independently and discard those deemed unimportant or redundant. We propose a reconstruction-guided framework for visual token condensation (ReConV), which summarizes the complete visual sequence with a compact Summary Bank (SMB) and retains tokens whose information is not adequately captured by the SMB, as indicated by their reconstruction residuals. At each compression layer, a lightweight position-conditioned decoder reconstructs the current tokens, leaving shared information compressed in the SMB while explicitly preserving poorly reconstructed details. Experiments on image classification and multimodal understanding demonstrate favorable performance-efficiency trade-offs: ReConV surpasses the uncompressed baseline with 48\% fewer GMACs on ImageNet and enables reusable image-level representations for efficient multi-turn inference. Code is available at TokenDrop.

---


### 591. [On Making $\mathrm{SE}(2)$-Invariant Networks Optimal](https://arxiv.org/abs/2610.17424)

**<font color=#1a73e8>作者：</font>** Tomas Karella, Emily Shinkle, Alice Elisabeth Anastasia Allen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Respecting a-priori known symmetries of underlying data is a key principle in designing efficient neural architectures. Convolutional neural networks are a canonical example, encoding translation equivariance. Extending this inductive bias to richer symmetry groups such as $\mathrm{SE}(2)$ in the most effective way possible is an ongoing architectural and computational challenge. Building on classical invariant theory, we derive invariant feature maps that are provably optimal: minimal and information-preserving with respect to the symmetry group. Our construction is designed to integrate seamlessly into standard architectures, requiring no modification to nonlinearities or normalization layers. As a concrete implementation, we introduce a plug-and-play module for convolutional neural networks that enforces $\mathrm{SE}(2)$ invariance, capturing both translations and rotations within standard architectures. The resulting models are both efficient and expressive. Experiments show competitive or improved accuracy compared to state-of-the-art equivariant methods at significantly lower computational cost. Finally, we provide a theoretical and empirical analysis of the relationship between equivariance and invariance, offering insight into their roles in controlling robustness and flexibility.

---


### 592. [When Sparsity Breaks Connectivity: Functional Reachability and Guided Topology Dynamics in Extreme Sparse Training](https://arxiv.org/abs/2610.17425)

**<font color=#1a73e8>作者：</font>** Mohammad Pasande, Mateusz Jaworski, Jeroen Rook 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic Sparse Training (DST) periodically prunes and regrows connections, inducing a discrete dynamical mechanism over network topologies. At extreme sparsity ($\ge 99\%$), this dynamic tends to destroy input-output information pathways, and performance with standard magnitude/random updates degrades sharply. We formalize forward, backward, and functional reachability on layered sparse graphs, derive closed-form expectations for reachable neurons and edges, and show that Monte Carlo realizations match the theory. Guided by this reachability-based structure, we bias pruning toward non-functional edges and regrowth toward functionally consistent candidates. We introduce this reachability-driven modification of topology evolution as Reachability-guided in DST, referred to as guided DST. On CIFAR-10/100 and Tiny ImageNet, guided DST recovers large accuracy gaps versus unguided DST (up to $+14.4$ points at $99.9\%$ sparsity on CIFAR-100), and on MLP-Mixer guided DST remains trainable at $99.99\%$ sparsity while unguided random regrowth degrades sharply. These results cast extreme-sparse training as a connectivity-preserving dynamical process. Our implementation is publicly available at this https URL.

---


### 593. [World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models](https://arxiv.org/abs/2610.17434)

**<font color=#1a73e8>作者：</font>** Junyi Wu, Zekun Li, Chenhongyi Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video world models have enabled plausible interactive environments, yet long-horizon generation places a fundamental demand on visual memory: the previously observed world must remain consistent as the model continues to generate. Existing autoregressive approaches often implicitly rely on the generative model itself to retain such information, leading to spatial memory decay beyond the active context. We introduce World-T3, a camera-controlled video world model with a test-time training memory that consolidates past observations into dedicated model parameters. To robustly update this memory, we propose a recursive least-squares rule that incrementally absorbs novel visual features via online pose-keyed memory updates. Our TTT memory reads out previously observed scene features from the fast-weight state by camera pose, enabling consistent generation with constant storage and per-step computation regardless of rollout length. To facilitate real-time interactive generation with this robust memory, we further distill the autoregressive model into a few-step generator via dual-teacher distribution matching. On a long-horizon revisit benchmark, World-T3 raises revisit PSNR from 13.52 to 18.31 dB and reduces absolute rotation error from 3.344 to 1.075 relative to the strongest baseline on both metrics, while sustaining 20.6 FPS at 1280 x 704 on a single NVIDIA B200 GPU.

---


### 594. [TableVision: Recovering Verified Structure from Historical Tables](https://arxiv.org/abs/2610.17448)

**<font color=#1a73e8>作者：</font>** Todd Y. Zhou, James M. Snyder Jr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaps, skips, and mistakes are the normal state of a historical register: rows go missing, tables cross page breaks, columns slip under wrong names, and column sums disagree with the corresponding row entries. Readers read digits correctly but lose the table structure. On seven clean panels of election returns, the best open-source reader reproduces 99.0\% of the digits but files only 83.7\% of the figures in the correct cells and gets 11 of 30 columns correct. TableVision treats table structure recovery as the problem. On three degraded 1888 pages, Amazon Textract files only 1 of 1494 figures correctly; TableVision correctly files 99.2\%, and all 51 columns its exact-total check releases are correct. A dynamic program cuts a volume into blocks by how many columns sum to their last line; witnesses read the cells; the gate classifies each column as exactly reconciling, flagged as faithful to a page whose arithmetic is wrong, or withheld. A theory of the sum check says which errors it cannot see and why its optimal block is about $\theta^{-1/2}$ rows at defect rate $\theta$. On 2201 columns of Wisconsin electoral data, the gate accepts 2042, flags 118, and withholds 41; failure rises with column length $R$ as $1-(1-\theta)^R$ at 1.1 defects per 1000 cells in general elections; official returns confirm 933 of 934 testable accepted sums and all 35 testable flagged totals; and the deployment added 491\,359 gated precinct rows to a 9.3-million-row dataset. One implication is that the design of the verification block is critical.

---


### 595. [On Sleep-Wake Disorder Identification from Polysomnographic Representations](https://arxiv.org/abs/2610.17451)

**<font color=#1a73e8>作者：</font>** Alvise Dei Rossi, Luigi Fiorillo, Giuliana Monachino 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised polysomnography foundation models (PSG FMs) aim to capture clinically useful information beyond sleep staging, yet are rarely compared with sleep-staging encoders pretrained at comparable scale and modality coverage. Using a common whole-night, missingness-aware state-space downstream modeling framework, we compared frozen representations from prominent large-scale, multi-cohort sleep-stage-supervised encoders and self-supervised PSG FMs for multilabel identification of six sleep-wake and circadian disorder groups in 7,906 PSGs from an unseen registry. Although PSG FMs outperformed an EEG-only, single-cohort supervised baseline, this ordering reversed when supervised pretraining approached comparable scale and modality coverage. Transfer learning from neural sleep scorers achieved higher overall performance while exhibiting greater downstream data efficiency. These findings underscore the need for scale- and modality-matched pretrained supervised baselines when assessing PSG FMs' downstream potential.

---


### 596. [Effect of Spherical Parameter Space on Number of Non-Forgetting Tasks and Capacity of Continual Learning](https://arxiv.org/abs/2610.17453)

**<font color=#1a73e8>作者：</font>** Nazanin Mirhosseini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a continuous learning formulation for $T$ non-forgetting tasks with the spherical parameter space $\mathbb{S}^{d-1}(\sqrt{d})$ in asymptotic regime $d\rightarrow \infty$. Each task $i$ has an optimum $\bm{\Theta}_i$, minimizing its corresponding loss function $R_i(\bm{w})$ on sphere. We reduce each task $i$ to an acceptable loss region modeled by a geodesic ball $B_{\bm{\Theta}_i}(r_i(d))$ on $\mathbb{S}^{d-1}(\sqrt{d})$ centered at $\bm{\Theta}_i$ with radius $r_i(d)$. To model task dependencies (similarities), task optima $\bm{\Theta}_i$ are distributed by a Neyman-Scott clustered point process $\Phi$. Cluster centers $\{\bm{Y}_j\}_{j=1}^{N_p}$ form a homogeneous Poisson point process on sphere, while intra-cluster task optima follow a von Mises-Fisher distribution with mean $\bm{Y}_j$ and concentration $\kappa$. Each task $t\in \{1, ..., T\}$ learning algorithm is considered to be a channel $Q_{t}(\mathrm{d}\bm{w}_t | \bm{w}_{t-1}, \mathcal{K}_{t-1}(\bm{\theta}_{1:t-1}), \bm{\theta}_t)$, where $\bm{W}_t$ is the learned parameter of task $t$ and $\mathcal{K}_{t-1}(\bm{\Theta}_{1:t-1})=\bigcap_{i=1}^{t-1}B_{\bm{\Theta}_i}(r_i(d))$. Since in continual learning, the learner does not need to reach $\bm{\Theta}_t$ exactly to successfully learn task $t$, to avoid forgetting as well as reliable learning, it only needs for the learned parameter vector $\bm{W}_{t}$ to enter $B_{\bm{\Theta}_t}(r_t(d)) \cap \mathcal{K}_{t-1}(\bm{\Theta}_{1:t-1})$. Using this model, we derive an upper bound on $T$ ensuring $\mathbb{P}[\mathcal{K}_{T}(\bm{\Theta}_{1:T}) \neq \emptyset] \rightarrow 1$ as $d\rightarrow \infty$ and $\kappa/d \rightarrow \alpha$, where $\alpha>0$ is a constant. Finally, for $T$ tasks sampled uniformly from $\Phi$, we derive an upper bound for total information theoretic capacity under the non-forgetting constraint for each task.

---


### 597. [An FPGA-Based Spiking Neural Network for Spatiotemporal Pattern Learning and Classification](https://arxiv.org/abs/2610.17463)

**<font color=#1a73e8>作者：</font>** Jingang Jin, Yue Ma, Zhenhang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) are promising for energy-efficient spatiotemporal pattern recognition at the edge, but efficient deployment and on-device adaptation require specialized hardware. In this work, we present an FPGA implementation of multilayer SNNs for spatiotemporal pattern classification, in which both inference and training take place on the same hardware. Our design adopts a temporal-forward-only training algorithm that avoids the memory and latency overhead associated with traditional Backpropagation Through Time (BPTT). A mixed-precision scheme balances training stability with resource efficiency, and architectural optimization maximizes hardware and memory utilization. We further identify and resolve hazards that arise when inference and learning share the same memory, including port conflicts between the forward and backward access patterns and read-after-write dependencies in floating-point potential accumulation. Experimental evaluations on MNIST and five multivariate time-series classification datasets demonstrate that, with fully on-chip training, our SNN model achieves accuracy comparable to SNN or LSTM trained with BPTT. Compared to CPU and GPU based implementations, our FPGA design delivers 2.5 to 6 times higher throughput while consuming an order of magnitude less energy per sample.

---


### 598. [Efficient Fréchet Distributional Decoder Alignment for Latent Generative Models](https://arxiv.org/abs/2610.17466)

**<font color=#1a73e8>作者：</font>** Xianghong Fang, Jiajun Zhu, Esma Aimeur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fréchet Distributional (FD) objectives provide an effective distribution-level signal for post-training generative models. For latent generative models, however, existing FD-based post-training methods optimize only the latent generator while keeping the decoder frozen: the decoder is trained on reconstruction latents obtained from real images but deployed on generator-produced latents at generation time. When these latent distributions differ, this \textbf{decoder train-generation mismatch} means that the decoder is deployed on inputs drawn from a distribution it was not directly trained on. We introduce \textbf{Fréchet Distributional Decoder Alignment (FDDA)}, an efficient post-training method that freezes the latent generator and directly optimizes the decoder on generation-time latents using an FD objective. A single epoch of FDDA consistently improves gFID and gFDr$^6$ across diverse flow-based and autoregressive latent generative models. Across all 11 evaluated models, FDDA reduces gFDr$^6$ by 34.0-59.6\% from the original pretrained models and provides a further 10.2-57.2\% reduction after generator-side FD post-training. FDDA also reduces total wall-clock time by factors of $3.6\times$-$328.7\times$ relative to generator-side FD post-training across these models. These results show that generator-side post-training alone does not exhaust the benefits of FD optimization, and that further gains can be obtained by adapting the decoder at substantially lower cost.

---


### 599. [Assessing the Performance of AI Models in Misinformation Detection Using Predefined Social Noise Constructs](https://arxiv.org/abs/2610.17469)

**<font color=#1a73e8>作者：</font>** Manar Alsaid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Social media platforms generate vast volumes of user-generated content that often obscure meaningful discourse, a phenomenon conceptualized as social noise. While existing misinformation detection methods primarily focus on factual verification, they largely overlook the role of social noise in amplifying misinformation. This study assesses the performance of six text-based models and a graph neural network (GNN) in mitigating the effects of misinformation using predefined social noise constructs. The dataset consists of 500,000 tweets collected from the X platform using the Ukraine hashtag during the Russia-Ukraine conflict from March 2024 to March 2025. Advanced machine learning models achieve strong performance, with accuracies ranging from 79.94% to 97.17%. RoBERTa demonstrates the highest performance, with an accuracy of 97.17%, Cohen's kappa of 0.9660, MCC of 0.9660, and AUC of 0.9977. The GNN achieves an accuracy of 64.52% and an AUC of 0.899, demonstrating performance above random-chance classification by exploiting the relational structure between tweets. All text-based models achieve kappa values greater than 0.75, indicating substantial overall agreement. Explainable AI analysis using LIME reveals that 89.6% of predictive weight is attributed to contextual features rather than isolated keywords. The findings highlight that integrating social noise into AI pipelines enhances misinformation detection and supports more effective mitigation strategies in large-scale social media environments.

---


### 600. [Structure-preserving fidelity diagnostics for partial differential equations](https://arxiv.org/abs/2610.17483)

**<font color=#1a73e8>作者：</font>** Kyriakos Flouris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning surrogates of partial differential equations (PDEs) are commonly trained on data generated by numerical solvers. Therefore, the training data obey not the PDE but the modified equation of the numerical scheme, and the test loss, computed on data from the same solver, cannot distinguish a model that learned the physics from one that learned the discretization error. Here, we show that the difference is nevertheless visible in the trained model. We propose a suite of structure-preserving fidelity diagnostics, simple scores that measure whether a learned model respects one known property of the physics, such as a conserved quantity, a symmetry or a Hamiltonian structure, without access to the training data or the governing equation. Over five systems, the diagnostics track the error with respect to the true dynamics with a rank correlation of up to $0.94$, while the test loss is uncorrelated or anti-correlated with it. For the Burgers, Korteweg-de Vries and Navier-Stokes equations, the diagnostics separate numerical schemes that the test loss ranks as equivalent, including schemes of the same order. order.

---


> [!TIP]
> 当前位于：**551-600**（第 12/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
