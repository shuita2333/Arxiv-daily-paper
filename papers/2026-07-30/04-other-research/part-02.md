# 📦 其他研究 | 2026年07月30日

> 本类共 **229** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-229](./part-05.md)

---

### 51. [ObjectEMS: Electrical Muscle Stimulation Without Electrodes on the User](https://arxiv.org/abs/2607.25084)

**<font color=#1a73e8>作者：</font>** Yun Ho, Zhechen Zhao, Romain Nith 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interactive electrical muscle stimulation (EMS) has revealed its promise as a portable interface for force-feedback. However, while much ink has been spilled about the advantages of EMS, few have investigated one of its central limitations: the need to attach electrodes to users. This has dramatically limited the application of EMS, especially in brief interactions or physical assistance with tools. To explore an alternative, we propose embedding electrodes (and stimulator) inside objects that the user interacts with. This is made possible because we identified multiple novel electrode placements that can elicit four distinct finger movements from the palm (no forearm stimulation). To illustrate this new way of implementing electrical muscle stimulation, we developed a set of self-contained interactive objects that use capacitive sensing to determine if a user's hand is in poses conducive to stimulation and then actuate the fingers from contact points between the hand and the grasped object. In our user study, we found that participants spent less time calibrating ObjectEMS than traditional EMS, and they felt less tethered while engaging with an EMS application via this novel approach. Our approach frees up the user's body from wearing electrodes and EMS stimulators, providing a new pathway for researching, implementing, or deploying actuated tangible interfaces. We demonstrate its potential via exemplary applications, such as a game controller with finger-level force feedback, a door handle with force feedback to prevent push-pull confusion, and more.

---


### 52. [Matryoshka Agent: Unfolding Sub-Agents for Long-Horizon Machine Learning Engineering](https://arxiv.org/abs/2607.25090)

**<font color=#1a73e8>作者：</font>** Rushi Qiang, Changhao Li, Haotian Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning engineering (MLE) tasks require long-horizon decision making over iterative solution debugging and refinement, under expensive and feedback-driven environment interactions. Developing and training a monolithic agent for such tasks is fundamentally challenging, as it must simultaneously manage extremely long and noisy contexts, explore vast solution spaces, and remain effective under limited model capacity and computational budgets. To address these challenges, we propose Matryoshka Agent, a unified hierarchical agent framework for complex long-horizon tasks. Matryoshka Agent decomposes agentic problem solving into a coordinated hierarchy of decision making and execution: a high-level Orchestrator maintains compact, long-horizon exploration states and issues strategic instructions, while lower-level Sub-Agents execute concrete solution attempts through direct environment interaction, mediated by standardized Tool interface. This design decouples strategic exploration from costly execution, substantially reducing the burden of long-context reasoning and enabling efficient iterative refinement. We further develop an efficient training paradigm for Matryoshka Agent. Experimental results on a broad range of MLE tasks with diverse model types and scales demonstrate that Matryoshka Agent is an effective and scalable paradigm for long-horizon MLE tasks and complex agentic problem solving. Notably, Matryoshka Agent enables Qwen3-4B-Instruct to reach Orchestrator performance comparable to o4-mini. Applying Matryoshka Agent to Qwen3-30B-Coder results in at most 36.7% relative performance gain.

---


### 53. [MorphUNet: Alpha-Controlled Biometric Transport for Diffusion-Based Face Morphing Attacks](https://arxiv.org/abs/2607.25092)

**<font color=#1a73e8>作者：</font>** Taimoor Rizwan, Sara Atito, Zhenhua Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face morphing attacks create synthetic images verifiable against multiple identities, threatening border control and identity verification systems. We introduce MorphUNet, a diffusion morphing framework formulating two-parent generation as alpha-controlled biometric transport: each parent is decomposed into CLIP appearance and ArcFace identity evidence, aligned into a CLIP-compatible token space, with the two contributors preserved as separate identity-aware token banks. To our knowledge, MorphUNet is the first diffusion-based morphing framework using trainable parent-separated dual cross-attention inside the denoising U-Net: a Biometric Transport Layer carrying parent-specific identity evidence through denoising, attending to each parent separately before combining residuals via the morphing parameter alpha. DDIM-inverted latent interpolation gives a coherent denoising start, while weaker-parent-guided selection favours morphs maximising the lower parent-similarity score, reducing collapse toward one contributor. We evaluate MorphUNet against three state-of-the-art baselines (StableMorph, MIPGAN-II, and MorDIFF) on FEI and FRLL using six recognition systems, and propose CFD-based unseen-identity stress testing across gender and ethnicity pairing, demographic shifts, and parent-similarity extremes. MorphUNet achieves the best Morphing Attack Potential (MAP) when at least three of six systems are fooled by one morph, reaching 0.919 on FEI and 0.886 on FRLL, and obtains the best FID on both datasets (35.19 FEI, 44.86 FRLL). It also gives the highest APCER at 5% BPCER in the same-dataset setting, and remains highly difficult to detect under cross-dataset transfer, with APCER 0.996 on FEI and 0.946 on FRLL. The full evaluation analyses MAP, MAD, per-system vulnerability, identity balance, image quality, top/bottom-similarity stress tests, and CFD unseen-identity robustness.

---


### 54. [Memdora: Designing Cognitively-Grounded Flashcard Interactions for AI-Powered Spaced Repetition](https://arxiv.org/abs/2607.25096)

**<font color=#1a73e8>作者：</font>** Ruiyang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Spaced repetition systems (SRS) have demonstrated robust effects on long-term retention, yet existing tools reduce the flashcard interaction to a single binary gesture: flip and self-rate. This impoverished interaction model fails to leverage decades of cognitive science evidence on retrieval practice, and requires learners to context-switch out of their reading flow to create cards manually. We present Memdora, a cross-platform AI spaced repetition system that addresses these limitations through four contributions: (1) a taxonomy of 17 cognitively-grounded interaction types across three learning categories -- Language (6 types), By Heart (1 type with 3 retrieval modes), and Exam (10 types) -- each mapped to peer-reviewed cognitive science evidence displayed on every card; (2) a unified AI generation pipeline that collapses card creation to a single gesture at the point of reading across web, mobile, and three browser extensions (Chrome, Edge, Firefox); (3) a collaborative classroom layer enabling teachers to publish decks, assign them to students, and track learning outcomes at the individual card level; and (4) an effort-based behavioral reward system that incentivizes actual cognitive engagement rather than mere app presence. Memdora integrates FSRS-6, the current state-of-the-art spaced repetition algorithm, and is deployed publicly on iOS, Android, Web, and three browser extensions. We describe the design rationale for each interaction type, discuss how the system advances beyond prior AI flashcard systems, and outline implications for educational technology design.

---


### 55. [IMPRINT: Image-Conditioned Query Enrichment for Long-Tail Object Goal Navigation](https://arxiv.org/abs/2607.25106)

**<font color=#1a73e8>作者：</font>** Jelin Raphael Akkara, Filippo Ziliotto, Luciano Serafini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied AI increasingly relies on queryable semantic maps built from pre-trained vision-language models to enable zero-shot Object Goal Navigation (ObjectNav). However, existing approaches typically depend on text-only queries, which become less reliable as semantic specificity increases toward fine-grained object categories. We introduce IMPRINT, a zero-shot plug-and-play framework that enriches textual object queries with web-sourced images to improve grounding in queryable maps. Retrieved images are encoded using a vision-language model, matched against the semantic map to produce similarity maps, and aggregated to yield context-aware localization. Notably, this requires no training or modification of the underlying navigation policy. To explicitly evaluate long-tail behavior, we present HSSD-rare, a new ObjectNav benchmark built on Habitat Synthetic Scenes and featuring semantically specific subcategories. Across both OVON and HSSD-rare, image-conditioned queries consistently improve object grounding and yield end-to-end navigation gains. Further analysis reveals that translating localization gains to navigation performance depends critically on downstream detection quality, highlighting a key systems bottleneck in long-tail embodied navigation.

---


### 56. [MOSAIC-FL, a micro-service based privacy-preserving framework with application to genomics](https://arxiv.org/abs/2607.25107)

**<font color=#1a73e8>作者：</font>** Paul Largillier, Karl Paygambar, Cédric Gouy-Pailler 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security and privacy are primordial requirements for Federated Learning (FL), especially in fields such as healthcare and genomics where sensitive information has to be analyzed. Our FL framework is designed to address these challenges while proposing a modular, flexible and micro-service architecture. More precisely, it integrates an efficient gRPC communication layer and a Finite State Machine to ensure robust component synchronization and threat detection, while relying on a fault-tolerant secure aggregation protocol using a Threshold variant of the CKKS homomorphic cryptosystem. This allows blind model aggregation by an orchestration server, requiring a minimum of $t$-out-of-$N$ active clients for decryption while minimizing communication overhead thanks to both cryptographic and network protocols. We ensure IND-CPA-D security through noise flooding and mitigate the recent key-recovery attack on synchronized decryptors by renewing the collective key material at every round. We demonstrate the framework's effectiveness through diverse use cases, ranging from standard image recognition (EMNIST) to complex genomic classification including breast cancer subtyping on TCGA, evaluating system performance across different threshold values and model scales.

---


### 57. [OPERA: Offline Policy-guided Expert Routing and Adaptation for Universal Biomedical Image Analysis](https://arxiv.org/abs/2607.25108)

**<font color=#1a73e8>作者：</font>** Zihan Li, Feiyang Liu, Dandan Shan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biomedical image analysis spans diverse modalities and tasks, yet real-world deployment is hindered by severe distribution shifts across scanners, protocols, and patient populations. High-performing models consequently require repeated domain-specific fine-tuning, which is a costly cycle that becomes impractical when labels are scarce or privacy constraints limit data sharing. We propose OPERA (Offline Policy-guided Expert Routing and Adaptation), a multi-agent ensemble framework that addresses this deployment bottleneck by treating expert weight assignment as an offline policy learning problem: a routing policy is learned from a small validation set without gradient updates to any expert agent, then deployed with test-time adaptation to handle distribution shift. OPERA coordinates heterogeneous specialist agents through complementary mechanisms. The expert profiling module learns selection policies offline, enabling informed allocation of expertise. Each agent undergoes confidence calibration through temperature adjustment, ensuring more reliable probabilistic outputs. OPERA also incorporates distribution aware adaptation, where class weights are dynamically adjusted at the batch level using statistics derived from unlabeled test data. Instance level routing assigns each sample to the most suitable expert by leveraging inter model agreement and predictive entropy. We evaluate OPERA on 9 datasets covering fundus photography, chest X-ray, CT, MRI, and multimodal diagnostic benchmarks, comparing against 30+ baselines across classification, segmentation, and multimodal settings. OPERA consistently improves performance and calibration quality, demonstrating that offline policy-guided expert agents coordination is a practical path to deployable biomedical AI without retraining. Code is on \href{this https URL}{GitHub}.

---


### 58. [Score-Based Stabilization for Time-Dependent Problems](https://arxiv.org/abs/2607.25119)

**<font color=#1a73e8>作者：</font>** Eshed Gal, Eldad Haber, Uri Ascher  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a score-based stabilization framework for numerical simulation of partial differential equations, in which a learned score model defines a stabilization operator applied to provisional numerical updates. This operator augments standard time-stepping schemes by enforcing structure and physical consistency through a correction that drives iterates toward the manifold of admissible states. We show that the stabilization operator acts as a contraction toward this manifold, yielding a correction mechanism with basin-conditional stability. Numerical experiments on Advection, Korteweg-de Vries (KdV), Nonlinear Schrodinger (NLS), and Burgers' equations demonstrate improved robustness, suppression of nonphysical instabilities, and preservation of qualitative dynamics.

---


### 59. [Semantic Space Search Trajectory Networks](https://arxiv.org/abs/2607.25122)

**<font color=#1a73e8>作者：</font>** Julian Agudelo, Alberto Tonda, Gabriela Ochoa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Search Trajectory Networks (STNs) are a graph-based tool for visualizing and characterizing the behavior of optimization algorithms. STNs' reliance on discretization of the search space has largely confined them to low-dimensional or combinatorial settings. We introduce a methodology for constructing STNs in semantic spaces, defined as the space of a model's predictions on a fixed sample set. Our approach discretizes semantic vectors and aggregates them into network nodes via agglomerative clustering with complete linkage under a normalized Hamming distance. Since any predictor can be summarized by its semantic vector, this method enables comparison of learning dynamics across otherwise incomparable algorithm families. We apply semantic space STNs to classification and regression tasks solved using different machine learning algorithms, recovering known qualitative differences between them. Additionally, we use semantic space STNs to study neural network generalization by contrasting standard training with the label randomization regime of Zhang et al. (2017). The resulting STNs exhibit consistent structural differences, training on real labels produces denser, more efficient and more centralized graphs than training on shuffled labels. Together, our results show that semantic space STNs capture functional training dynamics arising from the interaction between learning algorithms and data, providing a tool for analyzing and comparing learning dynamics across machine learning models and training regimes.

---


### 60. [Endpoint Replay: Compressing the Recency Buffer in Deep Reinforcement Learning](https://arxiv.org/abs/2607.25123)

**<font color=#1a73e8>作者：</font>** Parham Mohammad Panahi, Armin Ashrafi, Haoyu Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Experience replay remains one of the most practical and useful algorithmic tools in the deep reinforcement learning (DRL) toolbox. Aside from the limited success of prioritized replay and specialized approaches for large asynchronous systems, most DRL algorithms make use of a large, uniformly sampled recency buffer---even the size, one million, remains unchanged. Could we store less data, reduce redundancy, or more effectively chain experience together to speed up value propagation and still retain the performance of large buffers? In this paper, we investigate a simple compression approach that stores representative transitions derived from the end-points of a chain of connected $n$-step sequences. By curating these end-points in a smaller recency buffer, our method maintains an effective memory horizon comparable to a standard large buffer while requiring an order of magnitude less storage. Through empirical evaluation, we demonstrate that this approach prevents the systematic bias inherent in naive compression strategies and matches the performance of traditional large buffers in the Pinball environment and the Atari 2600 benchmark.

---


### 61. [Deep Label-Wise Attentive Temporal Convolutional Networks Improve Medical Coding](https://arxiv.org/abs/2607.25129)

**<font color=#1a73e8>作者：</font>** Muhammed Yavuz Nuzumlalı, Alexander Fabbri, Irene Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical coding is the task of assigning a set of diagnosis and procedure codes for a hospitalization using recorded notes. It requires aggregating information from different parts of the text and focus to different sections for each individual code, making it a very difficult problem even for professional human coders. We model the task as a multi-label text classification problem. To overcome the mentioned difficulties, we propose a deep neural model consisting of a multi-layer temporal convolution network (TCN) followed by label-wise attention. While multi-layer TCN helps extract a global document representation with the ability to learn relations over very long sequences, label-specific attention mechanism allows the model to focus on different aspects of the same document for each individual label. Our method achieves significantly better F-1 scores (9% increase) compared to the previous state-of-the-art model, with a remarkable increase in recall score (28% increase), which we believe is the more important metric for a clinical decision support setting.

---


### 62. [Beyond the Post Hoc User Study: Modeling Visual Decision-Making with Active Inference](https://arxiv.org/abs/2607.25131)

**<font color=#1a73e8>作者：</font>** Harrison J. Goldwyn, Graham Johnson, Christopher Ibarra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Empirical user studies are essential for evaluating visual encodings and can reveal perceptual and cognitive mechanisms, but they do not by themselves provide causal, predictive accounts of interpretation errors. Evaluations are therefore often post hoc: they measure performance after a design has been specified rather than predicting how attention, uncertainty, memory, and bias may produce accurate or erroneous judgments. To address this mechanistic gap, we translate a cognitive theory of visualization interpretation into executable simulation using Active Inference, a probabilistic framework for perception, learning, and action. We model chart reading as dynamic visual search in which agents update beliefs and choose actions that balance uncertainty reduction against cognitive effort. As a proof of concept, we implement Fast, heuristic (Type 1) and Slow, analytic (Type 2) agents for a bar-chart average-estimation task. The Fast agent is vulnerable to tick-salience bias, whereas the Slow agent is more vulnerable to working-memory decay. Both produce inspectable cognitive traces, including evolving belief uncertainty and fixation sequences. By expressing these hypothesized failure mechanisms as interpretable parameters, the architecture provides a framework for formalizing and testing mechanistic hypotheses about visualization interpretation. Empirical studies can then parameterize, refine, or falsify these simulations, supporting earlier and more predictive in silico evaluation of visualization efficacy.

---


### 63. [Interpretable GOHR Agents via Sparse Autoencoders](https://arxiv.org/abs/2607.25132)

**<font color=#1a73e8>作者：</font>** Shiwei Tan, Yusong Zhao, Weiyi Qin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central challenge in interpreting learned decision-making systems is to determine whether their internal representations contain concepts that help explain their behavior. We report interpretability experiments for a tokenized autoregressive Transformer agent in the Game of Hidden Rules (GOHR). We focus on a compact two-rule task in which both hidden rules map object shapes to target buckets, but with different permutations. The policy is trained on episodes sampled from these two hidden rules and then evaluated with fixed weights. It is never given a rule label and does not use an explicit rule classifier; any rule information must be inferred implicitly from interaction history. In this setting, the correct rule is not identifiable before the agent tries an informative move and observes accept/reject feedback. Sparse autoencoders (SAEs) trained on the agent's decision-token embeddings recover this structure. When held-out decisions are labeled by simple concepts such as the chosen shape or bucket, SAE dimensions that are highly selective for a concept cover most decisions where that concept is present. Individual SAE dimensions also correspond to interpretable strategies such as probing one rule hypothesis and switching after negative feedback.

---


### 64. [FIDAC: An Easy-to-use Pipeline to Extract and Interpret Interpersonal Distance From Video](https://arxiv.org/abs/2607.25146)

**<font color=#1a73e8>作者：</font>** Keshav Rastogi, Eugy Han, Jeremy N. Bailenson  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The distance between persons reveals significant information about their perception of each other. However, such information is not easily extractable and interpretable from video input. We developed an open-sourced library, Facial Interpersonal Distance Analysis and Coding (FIDAC) that transforms facial detection results into actionable data about location and interpersonal distance. This tool merges data from multiple open-source facial detection models, strategically compensating for gaps in any individual model. In addition, we include methods for more accurate tracking, such as a pipeline for human coding of the selection of faces and a benchmarking tool to reduce depth distortion. For next steps, we plan on building upon FIDAC by evaluating its effectiveness at measuring interpersonal distance at various depths and orientations while further integrating features of proxemic analysis such as synchrony into its software.

---


### 65. [Inferring Missing Trajectory Data with Temporal Convolutional Networks](https://arxiv.org/abs/2607.25147)

**<font color=#1a73e8>作者：</font>** Ilinca Tiriblecea, Gabriel Turinici  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trajectory data collected in real-world settings is frequently incomplete due to sensor failure, communication loss, or occlusion. We address the task of \emph{trajectory inpainting}: reconstructing contiguous missing segments from observed context. We propose a Temporal Convolutional Network (TCN) with symmetric dilation that relaxes the standard causality constraint, allowing each time step to draw on both past and future observations, a property that is essential for inpainting, but absent from forecasting-oriented architectures. The model is trained with a composite loss that combines weighted mean squared error, boundary--continuity penalties, and a smoothness regularizer. Trained on a synthetic dataset of $1,000$ (train), $200$ (validation), and $300$ (test) two-dimensional trajectories with randomly placed 20% masked segments, the model achieves good R$^{2}$, MSE and MAE metrics.

---


### 66. [Physics-Informed CNN-LSTM for Street-Scale Urban Flood Prediction: Reconciling Aggregate Accuracy and Street-Level Plausibility](https://arxiv.org/abs/2607.25148)

**<font color=#1a73e8>作者：</font>** Luc DCosta, Yidi Wang, Jonathan L. Goodall 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning surrogate models trained with mean-squared-error loss produce statistically accurate but physically unconstrained flood predictions: water may flow uphill, appear spontaneously, or smooth over street-level corridors. We develop a physics-informed training framework for CNN-LSTM models that predict urban flood depths at 15 min intervals over a 128x128 spatial grid. Three differentiable penalty terms are embedded into the loss: (i) a gravity loss penalizing depth increases against the water-surface-elevation gradient, (ii) a continuity loss enforcing local mass conservation with rainfall-adaptive thresholds, and (iii) a topography-aware false-alarm penalty modulated by the topographic wetness index (TWI). We evaluate on the Norfolk, Virginia flood dataset spanning two storm events (August 2017 and September 2022, 300 samples), with all variants trained on identical splits and robustness assessed over repeated random splits and leave-one-storm-out tests. A road-proximal evaluation restricted to a TWI-derived street mask quantifies street-level skill. The physics-constrained model achieves near-zero gravity violations (order 1e-6) and the highest street-channel recall (0.77 +/- 0.09 vs 0.44 +/- 0.10 for the unconstrained baseline), the capability most relevant to traffic routing, and its advantage more than doubles on a held-out storm; a uniform false-alarm variant attains 16% lower mean absolute error but suppresses street recall to 0.25. The TWI-modulated penalty reconciles this trade-off: it improves on the uniform variant on every metric, recovering 60% higher street recall at the lowest MAE among constrained variants and the best street-level F1. These results expose a fundamental tension between aggregate pixel-level error and application-specific physical plausibility, and show that terrain-aware loss modulation offers a principled resolution.

---


### 67. [OpenPVMapper: A Multi-source, Nationwide Database of Rooftop Photovoltaic Systems in France](https://arxiv.org/abs/2607.25153)

**<font color=#1a73e8>作者：</font>** Gabiel Kasmi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rooftop photovoltaic (PV) systems account for the vast majority of PV grid connections, yet no open, comprehensive, installation-level dataset of these systems exists: public registries aggregate data only above a capacity threshold, and remote sensing-based detection efforts, while extensive, are typically confined to a single method, a limited geographic scope, or a single point in time. We introduce OpenPVMapper, a nationwide, multi-source database of rooftop PV installations in mainland France, built by aggregating and reconciling complementary sources: a deep learning-based detection pipeline deployed on nationwide aerial imagery, OpenStreetMap and a probabilistic building-level detection dataset. The resulting database contains 1,135,850 installations, totaling approximately 15.01~GWp of installed capacity, each documented with its provenance, detection method, and, where available, a manual validation flag. Manual review of a stratified sample of 1,862 installations places the database's overall precision at approximately 74--75\%, with corroboration across independent sources bringing a substantial, quantified precision gain. By aggregating independent sources rather than relying on any single detection method, OpenPVMapper reaches a level of confidence beyond what any one source could provide on its own, while remaining extensible to further sources as they become available. It is released under an open (CC-BY) license alongside the full source code used to build it.

---


### 68. [Accurate structural modeling of chemically diverse molecular interfaces with Vilya-2](https://arxiv.org/abs/2607.25156)

**<font color=#1a73e8>作者：</font>** Vilya Research, Pascal Sturmfels, Naozumi Hiranuma 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structure-prediction networks built on co-evolutionary statistics have transformed protein-based drug discovery, yet their accuracy does not extend to peptide therapeutics--an increasingly important modality defined by non-canonical residues, macrocyclization, and complex topologies. We introduce Vilya-2, a diffusion transformer that extends the all-atom representation of Vilya-1 from modeling individual molecules to modeling their interactions with protein targets. This all-atom representation enables transfer learning between different molecular types, and delivers highly accurate structural modeling of peptides across sizes, classes, and compositions bound to therapeutically relevant targets. By generating diverse structural ensembles and ranking them with calibrated confidence, Vilya-2 recovers 59.1% of peptide interfaces to sub-2 Å backbone RMSD, far exceeding the performance of a representative co-folding model even when that model is given the bound receptor as a template. In addition, Vilya-2 is state-of-the-art at small-molecule docking, and generalizes to novel protein-small molecule complexes unlike those seen in training. It also generalizes to modeling molecular conformations of diverse macrocycles and disulfide-stapled miniproteins several-fold larger than any molecule seen in training. Finally, Vilya-2 can be used as a foundation model, and fine-tuned to enrich for active compounds in hit-to-lead campaigns. By unifying predictive accuracy with broad generalizability across chemical space, Vilya-2 is the structure-prediction oracle that de novo peptide design pipelines require--establishing the all-atom approach as a general foundation for the design and evaluation of de novo peptide therapeutics.

---


### 69. [Observing sycophantic AI validate others reduces its appeal but not its persuasiveness](https://arxiv.org/abs/2607.25166)

**<font color=#1a73e8>作者：</font>** Meryl Ye, Robert Kraut, Steve Rathje  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI chatbots can be ``sycophantic,'' or overly agreeable and flattering toward users. Sycophantic AI has been shown to entrench attitudes, yet users frequently fail to recognize it (a phenomenon we call ``sycophancy blindness''). We tested whether increasing users' awareness of sycophancy protects them from its harmful effects. In one preregistered experiment (n = 940), participants received a brief written warning about sycophancy before conversing with a sycophantic chatbot. In a second preregistered experiment (n = 650), participants watched a video of a sycophantic AI validating several other users, including users on opposite sides of the same conflict, before interacting with it themselves. Both interventions changed how participants evaluated the AI. The warning reduced the AI's perceived objectivity, and the video reduced enjoyment of the AI, an effect mediated by the reduced belief that its validation was uniquely earned. We then pooled our experiments with two prior studies of sycophancy awareness interventions (six interventions total, n = 3,982). The pattern was consistent: interventions made the sycophantic AI appear less objective and trustworthy, and none of the six reduced its persuasiveness. These results suggest that individual-level interventions, such as warning labels or AI literacy, may not be enough to protect users from AI harms.

---


### 70. [CondPSE: A Polynomial-Filtered Structural Encoder with Conditional Modulation for Graphs](https://arxiv.org/abs/2607.25169)

**<font color=#1a73e8>作者：</font>** Woohyun Lee, Hogun Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Message-passing graph neural networks are bounded by the 1-WL test and can miss topological structure that distinguishes non-isomorphic graphs. Positional and structural encodings (PSE) inject such topology-derived signals, and learned PSE encoders such as GPSE pretrain a single encoder to produce these signals from random node probes, which can then be frozen and reused as inputs across downstream graph models. We present CondPSE, a learned PSE encoder that applies a learnable polynomial graph filter bank to standard Gaussian node probes and refines the resulting structural-response branches through FiLM-style modulation conditioned on cross-filter, local message-passing, and graph-level signals. CondPSE is pretrained to reconstruct node-level positional/structural targets and graph-level invariants, and is then frozen for use as a downstream input encoding. On synthetic structural-discrimination benchmarks, CondPSE separates graph structures that 1-WL-bounded message passing cannot: it raises CSL accuracy from 42.9% to 97.3% and EXP accuracy from 68.3% to 99.9% relative to GPSE, and ablations show that the polynomial filter bank accounts for most of this gain. On real molecular property prediction, the picture is more limited. With a hybrid local-message-passing/global-attention backbone, CondPSE performs comparably to GPSE without surpassing it, and a ZINC backbone sweep shows no consistent ordering between the two encoders. We report these results and discuss why strong synthetic structural discrimination does not, on its own, yield a downstream advantage for frozen learned PSE encoders, including the role of downstream integration and possible mismatch between structural pretraining targets and molecular property labels.

---


### 71. [TabRank: Chain-of-Thought Distillation for Table Re-Rankers](https://arxiv.org/abs/2607.25182)

**<font color=#1a73e8>作者：</font>** Adarsh Singh, Kushal Raj Bhandari, Jianxi Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The ability to retrieve relevant tables for answering questions is a key task for structured information retrieval. Multi-stage retrieval systems rely heavily on rerankers to refine candidate lists produced by efficient first-stage retrievers. As a result, neural rerankers and LLM-based reranking methods have become increasingly important due to their superior capacity for semantic understanding and reasoning compared to conventional sparse or dense retrieval models. Recently, Large Reasoning Models (LRMs) equipped with explicit chain-of-thought (CoT) reasoning have shown strong improvements in ranking quality in unstructured passage retrieval. In this work, we present TabRank, a framework for training reasoning rerankers for Tabular Retrieval. We first present a comprehensive dataset of 6728 reasoning traces for tabular reranking on the Natural Questions Tables dataset. We then explore two variants of training a compact reasoning model on these reasoning traces: explicit CoT distillation and conditioning the student reranker on the teacher's reasoning trace within the prompt. We stress-test TabRank on several out-of-distribution generalization settings on diverse domains and multi-table scenarios. Our approach significantly improves performance across a variety of table retrieval datasets, increasing Acc@10 by 30.5% on HybridQA, 15.2% on SQA, 52.9% on TabFact, and 13.1% on TATQA subsets of the Multi-Table QA Benchmark compared to the base model. Notably, TabRank generalizes effectively to multi-table reasoning. Our code, data and models are available at this https URL

---


### 72. [A scaling law of contextual persistence in human language](https://arxiv.org/abs/2607.25184)

**<font color=#1a73e8>作者：</font>** Elan Barenholtz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human language exhibits lawful structure at the level of words (frequency, vocabulary growth) and word pairs (co-occurrence across distance). Here we show that the arrangement of words in sequence -- a central determinant of meaning -- obeys a comparable law. Using large language models as probabilistic probes, we measured the reduction in target perplexity conferred by prior context at distance d beyond that of the same words scrambled; this difference, the contextual persistence function P(d), isolates the influence of arrangement. Across ten corpora spanning six language families and written and spoken modalities, P(d) decayed approximately as 1/d ($P(d) \propto d^{-\alpha}$, mean $\alpha = 1.04$; median $r^2 = 0.96$). The effect vanished in scrambled and synthetic controls, replicated across independent probes, and did not appear in genomic or protein sequences under domain-native models. An exponent near 1 distributes contextual influence approximately uniformly across logarithmic timescales. The results establish a scaling law of contextual persistence in human language.

---


### 73. [LGFNet: A CTC-Guided Local-Global Fusion Framework for Single-Channel Sleep Staging](https://arxiv.org/abs/2607.25197)

**<font color=#1a73e8>作者：</font>** Chongjian Wang, Zhenghang Hou, Junjie Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sleep staging remains challenging due to long-range temporal dependencies, ambiguous stage transitions-particularly in N1-and substantial distribution shifts across subjects, sampling rates, and EEG montages. These difficulties are further amplified in single-channel, low-latency scenarios required by wearable and real-world applications. To address these issues, we propose LGFNet, a CTC-guided sequence-to-sequence framework for robust sleep staging. LGFNet introduces a Local-Global Fusion encoder that jointly models fine-grained temporal dynamics and long-range sleep structure, overcoming the limitations of conventional serial hybrid architectures. A CTC-Attention joint training paradigm is adopted to unify temporal alignment with context-dependent modeling, enabling more accurate recognition of stage boundaries and transitions. Furthermore, a three-stage decoding strategy is devised, leveraging CTC-guided decoding and Viterbi-based smoothing to reduce error accumulation and enforce physiological consistency. Extensive cross-dataset evaluations on five public benchmarks demonstrate that LGFNet consistently outperforms state-of-the-art single-channel methods. In particular, on Sleep-EDF-78, LGFNet surpasses DMIN by +1.27% accuracy, +1.74% macro-F1, and +1.93% kappa, with pronounced gains on N1 and transition segments, highlighting its robustness and strong generalization across diverse sampling rates, montages, and recording environments.

---


### 74. [Algorithmic Separation between Constant-Depth and Logarithmic-Depth Neural Networks](https://arxiv.org/abs/2607.25200)

**<font color=#1a73e8>作者：</font>** Yunwei Ren, Zihao Wang, Jason D. Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the empirical advantages of deep networks over shallow ones, theoretical depth separations largely concern approximation power, while algorithmic results are mostly limited to comparisons between two- and three-layer networks. In this work, we prove the first algorithmic separation between constant-depth and logarithmic-depth networks.
Specifically, we identify a class of Boolean functions with hierarchically structured Fourier spectra that logarithmic-depth networks can learn efficiently using layerwise coordinate descent by reconstructing the spectra hierarchically and adaptively. We also exhibit a subclass for which every constant-depth, polynomial-width network with sufficiently regular activations and controlled spectral norms must incur constant $L^2$ approximation error under the uniform distribution over the hypercube.

---


### 75. [A Cross-lingual Comparison of Human and Classification Model Entrainment Behavior in Code-switched Speech Settings](https://arxiv.org/abs/2607.25202)

**<font color=#1a73e8>作者：</font>** Debasmita Bhattacharya, Siying Ding, Alayna Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational entrainment is well-studied in monolingual and written contexts, but remains underexplored in spoken code-switching (CSW). We present a novel cross-lingual analysis of entrainment in Mandarin-English, Hindi-English, and Spanish-English dialogue and show that, while lexical entrainment generalizes across language pairs, entrainment over acoustic-prosodic and CSW style aspects exhibits context-specific variation. We build on these findings by asking whether classification models capture these human behavioral patterns. Applying feature importance and ablation analyses, we find that classical and Transformer-based classifiers detect entrainment reasonably well but consistently prioritize features other than those most salient to human entraining behavior. Our approach introduces a human-grounded framework for evaluating model decision-making in multilingual stylistic contexts, and suggests future challenges for developing conversational agents capable of producing naturalistic code-switched speech.

---


### 76. [A Unified Algorithmic Framework for Hybrid Reinforcement Learning in Tabular MDPs with Shifted Transition Dynamics](https://arxiv.org/abs/2607.25207)

**<font color=#1a73e8>作者：</font>** Zheshun Wu, Renjie Zheng, Jinhang Zuo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates a hybrid reinforcement learning setting in tabular Markov Decision Processes (MDPs), where an agent aims to learn an optimal policy by combining online interactions with a target environment and offline data from a source environment. A central challenge is that offline data may be collected from outdated environments with shifted transition dynamics, making naive integration of historical data ineffective. To address this, we propose a unified algorithmic framework featuring two algorithms: MIN-UCB-VI for regret minimization and MAX-LCB-VI for best policy identification. Both algorithms leverage fine-grained bias information to more effectively exploit offline data under general transition shifts. We provide theoretical guarantees for our framework, including both instance-dependent and independent upper bounds on regret and sub-optimality gap. Furthermore, we establish matching lower bounds to demonstrate the optimality of our approach and validate our theoretical findings through extensive experiments.

---


### 77. [ObliCity: A Benchmark and Baseline for Roof-to-Ground Projection Displacement Correction](https://arxiv.org/abs/2607.25210)

**<font color=#1a73e8>作者：</font>** Kai Li, Yupeng Deng, Ligao Deng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Oblique-view urban remote sensing imagery inevitably exhibits geometric projection displacements between building roofs and footprints, leading to significant distortions in spatial structure. Existing approaches either ignore these deformations or handle them implicitly within segmentation-based frameworks, where progress is dominated by general segmentation advances rather than improvements in geometric correction. In this work, we explicitly define roof-to-footprint offset vector (RFOV) extraction as an independent learning task that decouples geometric alignment from semantic segmentation. To support this task, we introduce the Oblique City dataset (ObliCity), the first large-scale benchmark that integrates high-resolution UAV imagery and globally distributed satellite data, covering diverse city morphologies and camera perspectives. Methodologically, we reformulate DragOSM into DragRoof, an ODE-based framework inspired by human annotation behavior. By simulating the continuous process of dragging roofs toward their footprints, DragRoof learns deterministic, geometry-consistent offset fields and adaptively determines convergence through an end token. Extensive experiments on ObliCity demonstrate that DragRoof achieves state-of-the-art RFOV extraction performance, requiring fewer inference steps while delivering superior directional and length accuracy. Our dataset and model establish a principled foundation for studying projection displacement correction in oblique remote sensing imagery. The source code and dataset will be avaliable at this https URL.

---


### 78. [How to Watermark the RLWE Homomorphic Ciphertexts](https://arxiv.org/abs/2607.25222)

**<font color=#1a73e8>作者：</font>** Yufei Zhou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In recent years, homomorphic encryption (HE) schemes based on the Ring Learning with Errors (RLWE) problem have rapidly developed and been widely applied to secure computation tasks, including privacy-preserving deep learning inference, privacy-preserving database queries, and related applications. However, most existing HE schemes focus primarily on the feasibility and efficiency of homomorphic computation, often neglecting practical requirements such as copyright protection of ciphertexts, source authentication, and supervision during computation. To address these issues, we propose a watermarking technique for RLWE-based HE ciphertexts. The algebraic structure of RLWE polynomials allows us to embed small noise as watermarking information into the ciphertext polynomials without affecting the plaintext values. However, HE ciphertexts typically undergo multiple homomorphic operations, which can distort or even remove the embedded watermark information. To address this challenge, we propose two practical solutions. The first, ARWMark, is a watermarking scheme based on noise stratification and is robust to homomorphic additive operations. The second scheme, MRWMark, is constructed using the roots of a linear equation and is resilient to both homomorphic additive and multiplicative operations, while supporting zero-bit watermarking. We provide a detailed theoretical analysis, proving that our schemes do not compromise the original security of HE, while ensuring the correctness and robustness of the proposed watermarking techniques. Furthermore, we conduct extensive experiments to demonstrate the effectiveness of both watermarking schemes.

---


### 79. [SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code](https://arxiv.org/abs/2607.25225)

**<font color=#1a73e8>作者：</font>** Narayanaswami Natraj Bharadwaj, Dhivya Chandramouleeswaran  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used for code generation in critical infrastructure, yet the security effect of domain-specific prompting is understudied. We present SecDrift, a benchmark measuring sector-conditioned security drift: the change in static-analysis vulnerability rates when prompts are conditioned on industry contexts versus neutral baselines. We evaluate 7 LLMs (6 producing analyzable code) across 8 CISA critical infrastructure sectors and 9 CWE categories with 5 replicates (5,355 evaluations), using a 5-dimension transformation with a matched-baseline condition that holds the task fixed while substituting only domain terminology. Industry prompts naively appear more secure (14.0% vs. 11.4%, -2.7pp), but the gap is not statistically significant (Fisher's exact p = 0.24, Cohen's h = -0.08) and is a composition artifact of two CWE categories: excluding CWE-502 and CWE-22 eliminates and slightly reverses it (+0.4pp, p = 1.00). A mixed-effects logistic regression confirms sector identity is not a moderator and localizes the only detectable condition effect to those two vulnerability types. 0 of 8 sectors show drift distinguishable from baseline, corrected or uncorrected (|h| < 0.15). A placebo on two non-CISA sectors (e-commerce, online education) reproduces the CISA industry rate almost exactly (10.5% vs. 11.4%, p = 0.63): the small pooled pattern reflects generic industry-framing specificity, not critical-infrastructure identity. In contrast, model selection has a large and consistent effect: among full-output models vulnerability rates range from 11.6% to 16.1%, and these differences persist across conditions. Model choice, not prompt framing, is the more reliable security lever. We release the framework, prompts, generated code, findings, human-validation verdicts, and analysis scripts.

---


### 80. [Beyond Single-Episode Optimization: Sliding-Window Aware Generative Auto-Bidding for Long-Term Advertising Effectiveness](https://arxiv.org/abs/2607.25233)

**<font color=#1a73e8>作者：</font>** Binglin Wu, Chuan Yue, Yingyi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auto-bidding systems optimize bids to maximize value under efficiency constraints such as Cost-Per-Action (CPA). Existing methods treat each day as an independent episode. However, many advertisers produce value so sparsely that per-day efficiency ratios become statistically unreliable, undermining advertiser retention. Platforms therefore evaluate window-level efficiency over sliding windows of $W{=}7$ days, ensuring fair evaluation and long-term advertising effectiveness. This creates cross-episode coupling: each day's bidding decisions affect up to $W$ overlapping windows, so setting daily targets requires anticipating future market conditions. We propose SWAG-Bid (Sliding-Window Aware Generative Auto-Bidding), a hierarchical framework decomposing this challenge into episode-level planning and step-level execution. The planner uses a Masked Trajectory Model to forecast markets and generate candidate plans, scored across all overlapping windows by Multi-Window Model Predictive Control Sampling (MWMS) with exponential confidence decay. The controller adjusts reliance on this guidance through a state-adaptive gate, Per-Step Gated Adaptive Layer Normalization (PSG-AdaLN), complemented by Return-to-Go and Cost-to-Go channels carrying budget and constraint information. Experiments on AuctionNet-Sparse and online A/B tests on AliExpress show that SWAG-Bid achieves competitive constraint satisfaction and value acquisition under sliding-window evaluation.

---


### 81. [WHTMix: Efficient Stereo Depth Estimation via Walsh-Hadamard Token Mixing](https://arxiv.org/abs/2607.25234)

**<font color=#1a73e8>作者：</font>** Prathyush Sajith, Emadeldeen Hamdan, Ahmet Enis Cetin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereo depth estimation for driving, robotics and augmented reality must run at high resolution under tight latency budgets, yet in transformer-based matchers the global self-attention that aggregates scene context grows quadratically with the number of pixels and comes to dominate runtime. We show that the joint self-attention stage of a stereo transformer, whose role is to spread context across both views, can be replaced by a data-independent Walsh-Hadamard token mixer that mixes tokens globally in the transform domain at log-linear cost, while the data-dependent cross-attention that performs left-right correspondence is retained. On synthetic driving data the mixer matches the attention baseline in end-point error while reducing model compute by a factor of 2.46 and single-image inference latency by a factor of 2.65. A complexity analysis shows the benefit is governed by the ratio of sequence length to channel width, which explains why high-resolution stereo matching is a particularly favorable setting and why classification transformers are not; we confirm this token-to-channel scaling on non-stereo long-sequence benchmarks. Furthermore, we introduce a hybrid log-disparity loss function designed to up-weight small-disparity pixels corresponding to long-range objects. This approach reduces the error on distant objects without incurring any additional computational overhead.

---


### 82. [CD-RMOT-Bench: Benchmarking the Cross-Domain Referring Multi-Object Tracking](https://arxiv.org/abs/2607.25239)

**<font color=#1a73e8>作者：</font>** Xiangqun Zhang, Likai Wang, Zekun Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring multi-object tracking (RMOT) extends tracking from category-driven perception to language-guided understanding by grounding object trajectories in natural-language expressions. Despite recent progress, existing RMOT studies are largely conducted under in-domain settings, leaving the robustness of language-conditioned tracking under inevitable visual domain shifts unexplored. In this paper, we study Cross-Domain Referring Multi-Object Tracking (CD-RMOT), a new and challenging problem that evaluates whether an RMOT model trained on a labeled source domain can reliably follow natural-language expressions in an unlabeled target domain with different visual conditions. To support systematic study, we construct CD-RMOT-Bench, a unified benchmark that combines real clear-domain referring tracking data, aligned digital-twin variants, and real adverse-domain videos. CD-RMOT-Bench enables both controlled weather/viewpoint shift analysis and realistic synthetic-real transfer evaluation under a shared RMOT protocol. Further, we provide a Query-Centric Adaptation (QCA) framework, designed to stabilize the query space that bridges visual trajectories and referring expressions. Extensive experiments reveal that domain shifts severely degrade RMOT performance, where the failure is not merely caused by object detection errors but more critically by unstable expression-conditioned temporal association and target selection. QCA establishes a strong baseline, while CD-RMOT-Bench opens a new direction for robust language-guided tracking across visual domains.

---


### 83. [SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems](https://arxiv.org/abs/2607.25255)

**<font color=#1a73e8>作者：</font>** Haowen Dai, Zonghao Ying, Wenfeng Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems improve capability through task decomposition and role specialization, but these same mechanisms introduce an important safety blind spot: a harmful objective can be fragmented into locally plausible subtasks, allowing malicious intent to evade detection by any single agent. This is a growing social-impact challenge: systems handling sensitive information or consequential tools can turn routine delegation into unauthorized disclosure or unsafe action. We argue that this failure mode is better understood as a semantic information-flow problem than as a single-turn prompt classification task. To address this, we propose SafeFlow, a defense framework for multi-agent systems that formalizes malicious cross-agent propagation as a semantic information-flow problem. SafeFlow attaches structured semantic taints to root requests, propagates them through a dynamic collaboration graph, and performs workflow-level validation to reconstruct the global risk context before irreversible actions are committed. Evaluated on four benchmarks spanning prompt injection, jailbreak-based unsafe tool use, risky code execution, and harmful web-agent behavior, SafeFlow reduces attack success rates compared to undefended baselines and external defenses while retaining high benign task completion and a high paired safe--harm success rate. Our findings show that multi-agent systems still lack mechanisms for preserving risk semantics across delegation boundaries. This gap can turn routine delegation into privacy harms or unsafe actions that affect people and organizations. SafeFlow keeps this risk visible throughout the workflow, before it results in harm.

---


### 84. [Where Steering Signals Come From: Activation Source Selection in Activation Steering](https://arxiv.org/abs/2607.25270)

**<font color=#1a73e8>作者：</font>** Jiaran Ye, Lingxu Ran, Zijun Yao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering controls language models by adding vectors or features to hidden states at inference time, but the upstream source of these steering signals is often treated as a secondary detail. We study this source choice as activation source selection: the combination of source context and activation readout policy used to collect the hidden states from which a steering signal is built. Holding the downstream intervention fixed, we show across three instruction-tuned models and four steering task families that changing only the source activations substantially changes steering success. We further find that effective steering is not explained simply by whether the desired behavior appears in the source text. Instead, strong signals come from execution-boundary states, where the model is about to produce or continue the target behavior. This pre-/post-realization distinction explains why answer-based sources sometimes work: their useful component aligns with execution-boundary directions rather than target appearance alone. Building on this view, we introduce tail subtraction, which removes shared prompt and continuation semantics from boundary states and yields cleaner, more stable steering signals. Overall, our results suggest that steering depends on representations of what the model is about to do, not merely on what has already appeared.

---


### 85. [Bridging Compute- and Data-Optimal Pretraining](https://arxiv.org/abs/2607.25271)

**<font color=#1a73e8>作者：</font>** Tian Qin, Kimia Hamidieh, David Alvarez-Melis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical compute-optimal scaling laws assume an unbounded supply of fresh pretraining data, yet pretraining is increasingly entering a regime in which compute grows faster than the availability of high-quality data. We propose Compute-Data (CD) scaling laws, a unified framework that bridges compute-optimal scaling, where data scales freely with compute, and data-optimal scaling, where the corpus is fixed while compute can grow without bound. CD scaling extends classical scaling laws by introducing a token-effectiveness function, $\eta$, which quantifies the value of a derived token-produced, for example, through multi-epoch repetition or paraphrasing-relative to a fresh token, ranging from a perfect substitute to having no value. We fit $\eta$ for two data-expansion strategies, multi-epoch repetition and paraphrasing, across model sizes from 14M to 600M parameters using the Dolma-3 corpus. We find that token effectiveness is far from constant: it depends jointly on model size, the tokens-per-parameter ratio, and the amount of derived data, and it saturates as the corpus is expanded. The functional form of $\eta$ implies diminishing returns when substituting compute for data as either model size or data availability increases. It also partitions training into three operational regimes---compute-bound, data-bound, and model-bound---and shows that classical compute-optimal allocation is suboptimal across most practically relevant settings.

---


### 86. [HeAD-CP: Heterophily-Aware Diffused Conformal Prediction Sets for Graph Neural Networks](https://arxiv.org/abs/2607.25273)

**<font color=#1a73e8>作者：</font>** Phan Binh Nguyen Lam, Nguyen Thai Anh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction (CP) provides distribution-free uncertainty quantification, and its extension to graphs is an active research direction. Diffused Adaptive Prediction Sets (DAPS) is a widely used graph-aware diffusion baseline, propagating Adaptive Prediction Sets (APS) non-conformity scores along edges with a uniform coefficient $\lambda$. We identify a fundamental shortcoming of this design: the uniform low-pass diffusion presupposes graph homophily and proves detrimental on heterophilic graphs, enlarging the mean prediction-set size by up to 10.6% relative to plain APS. To mitigate this, we propose HeAD-CP, a family of node-wise diffusion variants whose coefficients are determined by a label-free local-homophily estimate derived from the GNN softmax. Three variants, namely signed-$\gamma$, edge-compatibility, and a DAPS-baseline-with-correction, are most effective at extreme heterophily, intermediate heterophily, and moderate-to-high homophily, respectively, and all preserve the marginal coverage guarantee. On ten benchmarks, the HeAD-CP family stays at or below plain APS on every dataset, while DAPS exceeds APS on six. The post-hoc oracle over the family improves over DAPS on 8/10 datasets at $p<0.01$ (paired Wilcoxon), with the largest gains on heterophilic graphs (10.3% on Texas); on the two homophilic datasets where DAPS still wins (CiteSeer, PubMed), it retains a marginal advantage of at most 0.002, statistically insignificant on CiteSeer ($p=0.23$). Designing a calibrated label-free selector that approaches this oracle is the main outstanding empirical question.

---


### 87. [ScaleResfusion: Residual Rectified Flow based on Residual Vector Field](https://arxiv.org/abs/2607.25275)

**<font color=#1a73e8>作者：</font>** Zhenning Shi, Chen Xu, Junhao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world Image Restoration (Real-IR) aims to recover high-quality (HQ) images from complex and unknown degradations. Although recent diffusion-based methods have substantially improved perceptual quality, their current designs leave two key challenges unresolved. Methods that start from Gaussian noise are slow and often less faithful to the degraded input. Residual-based methods usually train from scratch, which makes it hard to exploit modern pre-trained generative priors. In this paper, we present ScaleResfusion, a scalable diffusion framework for real-world image restoration built on pre-trained text-to-image rectified-flow models. The core of our method is Residual Rectified Flow, which introduces the residual term R into Standard Rectified Flow. Instead of starting from pure noise, it uses a residual transport path that starts from noisy low-quality (LQ) images and admits an exact acceleration point. By learning the residual vector field, Residual Rectified Flow keeps the output distribution and linear diffusion process consistent with the pre-trained rectified-flow models. This makes parameter-efficient fine-tuning possible at scale. We further introduce a knowledge-distillation pipeline to reduce sampling cost while maintaining restoration quality. Extensive experiments on multiple real-world restoration tasks show that ScaleResfusion achieves state-of-the-art performance with much higher efficiency. These results suggest a practical and scalable way to adapt large pre-trained diffusion models to real-world image restoration. Our code and models are available at this https URL.

---


### 88. [FunnelAL: Retrieve-then-Rank Active Learning for Single-Class Discovery](https://arxiv.org/abs/2607.25276)

**<font color=#1a73e8>作者：</font>** Reihaneh Rostami, Brian Goodwin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FunnelAL, a retrieve-then-rank active learning system for single-class discovery, which adapts the multi-stage funnel architecture of industrial recommender systems to data annotation. Large-scale supervised learning faces two challenges: efficiently finding relevant samples in a massive corpus, and distinguishing true positives from visually confusable negatives when embeddings do not cleanly separate classes. Conventional active learning offers a principled framework for reducing annotation cost, yet it treats sample selection as a single-stage process that addresses neither challenge efficiently. FunnelAL decomposes the problem into cascaded stages. Starting from a single positive and negative example, the system iterates through: (1) embedding-based retrieval scoring that narrows the corpus to a manageable candidate set; (2) a precision-triggered ranking stage that exploits a learned ranker (RankNet) while batch precision remains high, then automatically blends in committee-based exploration (QBC) once returns diminish; and (3) feedback from the annotator's labels that refines both stages in subsequent iterations. We evaluate on three diverse image classification benchmarks. With a perfect annotator, FunnelAL attains the best final F1 on all three benchmarks, the best annotation efficiency (first in AULC), and the fewest annotation rounds. The most recent single-class discovery methods (GAL, PF-MA) at best match its final quality, and only at consistently higher labeling cost. Under annotator labeling errors at realistic rates, FunnelAL remains first or statistically tied for first while classical uncertainty-based methods degrade two to three times faster. Our work provides a concrete bridge between multi-stage recommender systems and active learning.

---


### 89. [ContractHIL-HLS: Contract-Aligned Multi-Agent Workflow with Hardware-in-the-Loop Feedback for HLS Design](https://arxiv.org/abs/2607.25283)

**<font color=#1a73e8>作者：</font>** Jingbo Zhang, Haoxiang Sun, Wenbo Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents ContractHIL-HLS, a contract-aligned multi-agent workflow for practical high-level synthesis (HLS) engineering. The workflow makes three contributions. First, it introduces a structured contract as the semantic-alignment and task-execution artifact that translates natural language requirements into explicit interfaces, constraints, validation checks, and rollback rules. Second, it incorporates hardware information into the feedback loop by feeding HLS, Vivado, PYNQ runtime, power, and failure evidence back into generation, thereby extending LLM-assisted HLS from kernel code toward system- and board-level closure. Third, it decomposes agents by semantic lowering and execution tasks rather than by conversational roles: a Contract Agent lowers natural language into the contract, an HTML Agent renders the contract as persistent structured HTML, and a Hardware-in-the-Loop Agent implements and revises the design with measured evidence. We evaluate ContractHIL-HLS in two parts. On 94 locally executable HLS-Eval tasks, the structured contract provides the largest small design gain, improving the estimated single-sample testbench pass rate from 64.0% to 70.2%; the full flow reaches 70.4% pass@1 and 76.6% pass@5. Because HLS-Eval does not exercise board-level design, we also validate ContractHIL-HLS on a board tested ML-KEM/ML-DSA post-quantum cryptography (PQC) secure-message accelerator, where the retained dual-bitstream organization reduces six-message average text runtime from 207.3 ms to 52.4 ms with positive routed WNS on both images while preserving decrypted-message verification. We open-source our work at BJUT-CS316-LAB/ContractHIL-HLS (this https URL).

---


### 90. [When Does Deep Representation Learning Help Single-Cell Clustering? A Sensitivity-Aware Diagnostic Benchmark for Biomedical AI Pipelines](https://arxiv.org/abs/2607.25288)

**<font color=#1a73e8>作者：</font>** Nguyen Thanh Phong, Truong Viet Vu, Nguyen Ha Thu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell ribonucleic acid sequencing (scRNA-seq) is a foundational technology for precision-medicine workflows that contribute to United Nations Sustainable Development Goal 3 on Good Health and Well-being, and unsupervised clustering is the analytical step that turns raw expression matrices into interpretable cell populations. Practitioners therefore face a recurring engineering decision: is an additional deep representation stage worth its compute and tuning cost, or do classical principal component analysis (PCA) pipelines already suffice? We address this question with a diagnostic benchmark of nine clustering pipelines on ten real datasets (90-5,685 cells, 19,046-41,480 genes, 4-11 cell types), augmented by a partial scVI V2 specialized comparison on seven datasets. The protocol integrates Optuna hyperparameter search, repeated-run robustness, Friedman/Wilcoxon-Holm/TOST testing, and Sobol total-order sensitivity analysis. The contrastive autoencoder achieved the highest mean Adjusted Rand Index (0.7872), but Holm-corrected tests did not establish dominance over the strongest baselines. Per-dataset analysis reveals three reproducible regimes: probabilistic variational autoencoder (VAE) variants help on the smallest datasets, deep autoencoders win on mid-scale data with multi-batch or many-type structure, and classical PCA pipelines remain competitive when linear projection already captures the dominant variation. Sobol indices identify learning rate ($S_T=0.70$) and latent dimensionality ($S_T=0.56$) as the dominant variance contributors, indicating where limited tuning budgets should be allocated. The contribution is therefore a dataset-aware and compute-conscious decision framework for biomedical AI pipelines supporting sustainable healthcare analytics, rather than a universal superiority claim.

---


### 91. [AMRD: Adaptive Multi-Teacher Relational Distillation for Lightweight Speech Emotion Recognition](https://arxiv.org/abs/2607.25289)

**<font color=#1a73e8>作者：</font>** Yuqi Li, Yi-Cheng Lin, Xianglong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device speech emotion recognition (SER) is critical for real-time applications, yet large self-supervised models that excel at SER are too costly for edge devices. Multi-teacher knowledge distillation can compress them into a lightweight student, but two challenges remain: teacher reliability varies across batches, and logit-level distillation ignores inter-sample relational structure. We propose Adaptive Multi-teacher Relational Distillation (AMRD) to address both. A one-class SVM on each teacher's logit similarity matrix assigns per-batch weights favoring more coherent teachers. A relational distillation loss aligns teacher and student similarity matrices, capturing structure that logit matching misses. On IEMOCAP and CREMA-D datasets across four student architectures, AMRD outperforms single-teacher distillation baselines in most settings, and ablations confirm both components yield complementary gains.

---


### 92. [CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention](https://arxiv.org/abs/2607.25291)

**<font color=#1a73e8>作者：</font>** Yufei Xue, Lin Niu, Hong Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The quadratic cost of self-attention makes long-context inference prohibitively expensive, and proxy-based block-sparse attention has become a practical remedy. Existing methods typically rely on a proxy to predict a binary sparse mask and a kernel to consume this mask and perform sparse attention computation. Such an approach is effective under moderate budgets. However, as the budget tightens, the estimated proxy inevitably drops some salient blocks, while the kernel can only apply the sparse mask mechanically, leading to an evident drop in model accuracy. We propose CoSA, a two-stage training-free Sparse Attention under proxy-kernel CO-design, which couples a Kernel-Aware Proxy (KAP) with an Ordered-Skipping Kernel (OSK). In the first stage, the KAP selects blocks under a moderate budget and produces an ordered mask that prescribes the order in which KV pages are visited in the kernel inner loop. In the second stage, the OSK applies this mask and skips more blocks under a tightened budget given online-softmax statistics. Across mainstream LLM backbones and long-context benchmarks, CoSA attains higher accuracy at lower budgets. Impressively, CoSA achieves a 4.93$\times$ attention speedup and reduces end-to-end Time-to-First-Token by 2.53$\times$ under a context length of 128K with negligible performance degradation.

---


### 93. [Breaking the Periodicity Assumption: Robust Tensorial Multi-View Clustering via Graph-Spectral Low-Rank Learning](https://arxiv.org/abs/2607.25295)

**<font color=#1a73e8>作者：</font>** Jintian Ji, Xingsu Li, Songhe Feng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensorial multi-view clustering (TMC) has achieved strong performance due to its ability to capture high-order correlations across multiple views. Most existing t-SVD-based TMC frameworks apply the Fast Fourier Transform (FFT) along the sample mode to impose frequency-domain low-rank constraints. However, we reveal that this widely adopted design critically relies on an implicit ``periodicity assumption'' induced by the sample arrangement. When samples are ordered by class, neighboring indices tend to be semantically similar, creating artificial local continuity along the sample mode and a favorable spectral structure for FFT-based low-rank regularization. Once this ordering is removed by random permutation, existing t-SVD-based TMC methods suffer severe performance degradation. This strong sensitivity to class ordering conflicts with the permutation-invariant nature of clustering and indicates that part of the reported performance may be attributed to a privileged sample arrangement rather than genuine high-order structure modeling. In this paper, we systematically investigate this phenomenon and its underlying algebraic and spectral mechanisms. To address this fundamental flaw, we further propose a graph-spectral low-rank tensor learning framework based on the Graph Fourier Transform (GFT), which replaces the fixed Fourier basis along the sample mode with a data-driven graph spectral basis, thereby capturing the intrinsic manifold structure without relying on a particular sample ordering. Moreover, we develop an anchor-based variant to address large-scale datasets efficiently. Extensive experiments on various benchmarks validate our findings and demonstrate the competitive or superior performance of the proposed methods compared with state-of-the-art TMC approaches.

---


### 94. [Zhinv: Real-time hub-height wind field reconstruction using only local sparse observations](https://arxiv.org/abs/2607.25298)

**<font color=#1a73e8>作者：</font>** Zongwei Zhang, Chin Chun Ooi, Lianlei Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The high proportion of wind power connected to the grid places higher demands on fine-grained knowledge of regional wind fields. Since the wind information directly obtainable in actual operations is mostly sparse, discrete, and irregularly distributed local observations, it is difficult to directly meet the needs of tasks such as wind power regulation, wind resource assessment, and low-altitude environmental perception of continuous regional wind fields. Therefore, we propose Zhinv, an end-to-end reconstruction framework that directly weaves sparse and irregular observations into a fine-grid wind field at hub-height. Experiments in Northeast China, Europe, and Southeast Asia demonstrate that Zhinv can accurately, robustly, and efficiently reconstruct fine-grid wind fields from sparse observations, reducing the error by about 66% compared with Kriging. With local wind-power observations as input, Zhinv enables wind power centers to bypass NWP and complex assimilation processes, supporting direct and real-time wind resource assessment from locally available data.

---


### 95. [MEDit-Bench: A Dataset for Evaluating Message-Driven Narrative Video Editing](https://arxiv.org/abs/2607.25300)

**<font color=#1a73e8>作者：</font>** Katsuya Ogata, Zongshang Pang, Mayu Otani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video editing is fundamentally message-driven: even from the same source footage, the selected shots change depending on the narrative the editor wishes to convey. Benchmarks for a closely related task, video summarization, reduce editorial intent to a single, message-agnostic notion of saliency and thus do not account for this diversity. For evaluating message-driven video editing, we present \textbf{MEDit-Bench}, a dataset and benchmark, which pairs long-form videos with multiple editing messages and multiple professionally produced edits per message, demonstrating that different messages yield substantially different edits from the same source. We define an automatic evaluation protocol based on temporal alignment metrics, and find that an LLM-as-a-judge preference, a natural proxy for narrative quality, is unreliable for this task due to severe position bias. We additionally annotate each message with ambiguity and contextfulness scores, and show that both dimensions negatively correlate with model performance, establishing message difficulty as a meaningful stratification factor. Experiments with state-of-the-art MLLMs and reinforcement fine-tuned baselines show that while strong models approach human temporal alignment at lenient thresholds, all models fall behind humans at stricter criteria. A human perceptual study further confirms a large quality gap, with professional human edits remaining consistently preferred over model outputs.

---


### 96. [Toward a systematic method for identifying language areas](https://arxiv.org/abs/2607.25305)

**<font color=#1a73e8>作者：</font>** Hiram Ring  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Macroareas are geographical areas used in typological research for grouping variables of interest. In linguistic typology, languages in a given macroarea are considered to have potential for contact, in contrast to those outside the area, where contact is less likely. Along with language family membership, macroareas are used as controls for models in linguistic typology, in an attempt to address the problem of autocorrelation - the observation that historical developments or typological patterns may be due to contact between neighboring languages and/or inheritance from a common ancestral language. Macroareas are therefore a central aspect of research that seeks to separate universal properties of language from local (or language-specific) properties. Existing macroareas largely depend on expert determinations of what constitutes a geographical area of potential contact, and to date have mainly aligned with continents or landmasses (Hammarström and Donohue 2014; Nichols, Witzlack-Makarevich, and Bickel 2013). While there are various historical and theoretical reasons for these groupings, there as of yet has been no systematic approach to identifying such areas for a given region. This paper attempts to address such a gap and move beyond macroarea to identification of language areas of relatively arbitrary size, presenting a simple geographical clustering method for identifying groupings over any area. The method produces a set of worldwide macroareas that largely align with existing groupings, as well as local groupings for a well-known sprachbund.

---


### 97. [Human-in-the-Loop Signature Bootstrapping for UAV Hyperspectral PFM-1 Mine Detection](https://arxiv.org/abs/2607.25310)

**<font color=#1a73e8>作者：</font>** Sagar Lekhak, Prasanna Reddy Pulakurthi, Emmett J. Ientilucci  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral imaging (HSI) is useful for material discrimination, but operational mine screening also depends on how many false alarms must be inspected before targets are found. This paper studies PFM-1 landmine detection in unmanned aerial vehicle (UAV) visible and near-infrared (VNIR) HSI using spectral angle mapper (SAM), matched filter (MF), adaptive coherence estimator (ACE), and constrained energy minimization (CEM). We compare a ground-measured SVC signature, a fully informed in-scene core-pixel signature, and a simulated human-in-the-loop signature bootstrap. Besides receiver operating characteristic area under the curve and average precision, we report target-discovery curves and spatial candidate-review counts. Full-review bootstrapping reaches the fully informed in-scene signature case after all seven target regions are verified, but the required inspection effort varies strongly: ACE confirms all regions in two rounds and nine candidate inspections, whereas the SAM variants need thousands of candidate reviews for their final target locations. Code is available at this https URL.

---


### 98. [Guiding Posterior Exploration with Optimizer-Derived Geometry](https://arxiv.org/abs/2607.25312)

**<font color=#1a73e8>作者：</font>** Moritz Schlager, Emanuel Sommer, Thomas Möllenhoff 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling-based methods offer a principled approach to uncertainty quantification in Bayesian neural networks. Their practical use, however, is often challenged by the computational cost of exploring high-dimensional and multimodal posterior distributions. To overcome these difficulties, Bayesian Deep Ensembles, i.e., warmstarting the sampling from several optimized solutions, have proven to be an effective strategy. In this paper, we demonstrate that curvature estimates computed during the warmstart as a byproduct in adaptive optimizers such as AdamW can inform the sampling phase at negligible additional cost. Specifically, our proposed preconditioned sampling strategy based on optimizer-derived geometries can substantially reduce or even eliminate the need for a lengthy sampling burn-in phase and leads to greater numerical stability. This approach consistently maintains or improves predictive performance and uncertainty quantification without any additional computational costs. We confirm the consistency of our findings across various datasets and network architectures.

---


### 99. [Sense it with your eyes: Sensation Generation and Understanding for Advertisements](https://arxiv.org/abs/2607.25314)

**<font color=#1a73e8>作者：</font>** Aysan Aghazadeh, Sina Malakouti, Adriana Kovashka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sensory advertising evokes human senses through visual cues, enabling audiences to mentally simulate experiences and increasing persuasive impact. Despite the recent increase in using AI in generating and understanding creative and persuasive content, how advertisements visually evoke sensations remains largely unexplored. In this work, we introduce the first study of understanding, evaluating, and generating sensory ads. We introduce the Sensory Ad dataset, and define sensation classification tasks (SenseClass) to benchmark LLMs and MLLMs. We further propose SenseScore, an automated evaluation metric for sensation evocation achieving strong agreement with human judgments. Finally, we introduce the Sensory Ad Generation (SenseGen) task and propose SAGA, a multi-agent framework that improves message image alignment, sensory evocation, and persuasion. Our work establishes a foundation for sensory-aware visual persuasion.

---


### 100. [Physics-Grounded Fluid Video Generation with a Simulation Dataset and Dual-Stream Optical-Flow Supervision](https://arxiv.org/abs/2607.25321)

**<font color=#1a73e8>作者：</font>** Ruijie Su, Yuanzhi Liang, Xiaohua Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video diffusion models generate visually compelling content but routinely violate elementary physics when the subject involves fluids: liquid columns break apart in mid-air, container water levels fail to rise as liquid is poured in, and splashes disperse without regard to momentum or gravity. We attribute this gap to the fact that large-scale video-text corpora contain almost no explicit motion supervision, so models learn to imitate fluid appearance rather than dynamics. We address this with two contributions. First, we build a physics-simulation fluid dataset combining 1,638 MPM-simulated pouring/sloshing videos with 2,320 keyword-filtered real pouring videos mined from stock footage, plus two held-out test sets: a 1,515-video real-video benchmark and an 18-prompt text-to-first-frame generalization benchmark. Second, we introduce a dual-stream image-to-video architecture built on a pretrained diffusion-transformer video generator. It augments the standard RGB decoder with a lightweight Optical-Flow Decoder branch trained with explicit end-point-error and smoothness losses, fused into the RGB stream via zero-initialized convolutions so the pretrained backbone starts undisturbed. Only the two decoders are updated; the encoder, temporal transformer, and text encoder remain frozen. Across two model scales (1.3B and 14B) and two test sets, our method improves VideoPhy-2 Physical-Commonsense and Video-Quality scores over the frozen backbone by up to 8.75 and 4.65 points, outperforms a leading open competitor, and is preferred by human raters in a blind study. A direct optical-flow read-out evaluation further shows an end-point error as low as 0.54 pixels in-distribution, confirming the model has internalized a coherent motion prior rather than merely improving surface appearance.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-229](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
