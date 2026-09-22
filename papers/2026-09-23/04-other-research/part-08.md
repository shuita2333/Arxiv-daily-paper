# 📦 其他研究 | 2026年09月23日

> 本类共 **463** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-463](./part-10.md)

---

### 351. [Pharmacokinetic State Space Models for Unbiased Prediction of Haemodynamic Collapse](https://arxiv.org/abs/2609.24338)

**<font color=#1a73e8>作者：</font>** Rithin Nagaraj, Sudiksha Chindula, Bhaskarjyoti Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An Intraoperative Hypotension (IOH) event is a frequent complication during administration of general anaesthesia with serious downstream consequences, yet clinical management remains reactive and not predictive. Existing predictive models, however, ignore drug infusion history as a valuable signal for prediction despite its direct pharmacological relevance. Our model achieves an Area Under the Receiver Operating Characteristic curve (AUROC) of 0.7360 and an Area Under the Precision-Recall Curve (AUPRC) of 0.1794, representing a 2.73-fold lift over the random guessing AUPRC baseline (0.0657), with the removal of propofol and remifentanil effect-site concentrations resulting in a 13.9% AUPRC drop compared to the full model. This is consistent with the hypothesis that pharmacokinetic trajectories encode impending haemodynamic changes before they manifest in the Mean Arterial Pressure (MAP). Additionally, this paper shows that training without lead-gap filtering degraded AUROC by 16.7%, empirically confirming that unfiltered models learn to detect ongoing hypotension rather than predict future events. Finally, a Mamba-based architecture achieves the aforementioned high prediction performance while maintaining a constant memory footprint across a range of sequence lengths, unlike the quadratic VRAM overhead typical of vanilla Transformers, making it the more practical choice for continuous intraoperative deployment.

---


### 352. [Explainable Neuro-Fuzzy Prediction for Trustworthy Decision-Making in Maritime](https://arxiv.org/abs/2609.24358)

**<font color=#1a73e8>作者：</font>** Dionisis Kalogeropoulos, Georgia Sovatzidi, Dimitris K. Iakovidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting when maritime systems require maintenance can be critical, avoiding hazards and costly consequences. To address this problem, this paper proposes an explainable decision-making framework that integrates a neuro-fuzzy prediction model with a two-stage explainable component. The first stage of this component produces feature-attribution explanations, using gradient-based saliency maps, and the second stage extracts local rules using a fuzzy decision tree. The proposed framework is generic and can be integrated into any deep learning-based approach, rendering it explainable. To the best of our knowledge, this is the first fuzzy logic-based framework enabling both feature-level and local rule-based explanations of black box models. This approach aims to foster trustworthiness in decision making through user-understandable machine inferences. The performance of the proposed framework using a deep residual-based neural backbone is evaluated on various general-purpose public benchmark datasets, and its utility in maritime is demonstrated in the context of early fault detection in a naval propulsion system dataset. The results indicate that it can provide predictions outperforming relevant state-of-the-art approaches, with an average AUC-ROC (Area Under the Receiver Operating Characteristic Curve) value, reaching up to 99%, while offering the advantage of explainability.

---


### 353. [TReViS: Temporal Repetition Structure Aware Video Synthesis for Self-supervised Repetitive Action Counting](https://arxiv.org/abs/2609.24367)

**<font color=#1a73e8>作者：</font>** Fanqi Yu, Shengming Ma, Stefano Fiorini 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fully supervised repetitive action counting (RAC) has achieved strong performance, but requires dense temporal annotations that are costly and difficult to scale. We propose TReViS, a self-supervised video synthesis framework that enables training RAC models without any repetition labels. TReViS estimates the underlying temporal repetition structure of an unlabeled video via a Temporal Self-Similarity Matrix, infers its cycle statistics, and synthesizes new training sequences that preserve realistic repetition patterns while introducing controlled temporal variability. These synthesized videos are paired with pseudo-labels and used to train existing RAC architectures from scratch. Across multiple datasets and backbones, TReViS consistently outperforms prior self-supervised methods and achieves performance competitive with several supervised baselines, while remaining fully label-free, demonstrating the effectiveness of structure-aware video synthesis for label-free RAC. The source code is available at this https URL.

---


### 354. [Prescriptive SVD-Inspired Attention via Spectral Energy Retention](https://arxiv.org/abs/2609.24370)

**<font color=#1a73e8>作者：</font>** Vasileios Arampatzakis, Vasileios Sevetlidis, George Pavlidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-attention is central to modern Transformer architectures, but its dense dot-product formulation makes it difficult to identify which internal directions are structurally important and which can be modified without disrupting the model. SVD-Inspired Attention (SVDA) addresses part of this problem by introducing a learned diagonal spectrum into the query-key score interaction, making latent attention directions explicitly inspectable through indicators such as spectral entropy, effective rank, sparsity, alignment, selectivity, and perturbation response. This paper examines the transition from diagnostic interpretation to operational intervention. A diagnosis--intervention--verification framework is proposed, and one intervention is evaluated: spectral energy retention in the attention-score pathway. Across FashionMNIST, CIFAR-10, CIFAR-100, and Food-101, the $\rho=0.90$ prescription removes 24.5--53.7\% of score directions, reduces parameters by 2.6--4.3\%, and reduces estimated MACs by 2.8--5.4\%. The paired mean accuracy change of the dimension-reduced model ranges from $-0.03$ to $+0.05$ percentage points over three seeds. These results support SVDA as an intrinsically interpretable attention mechanism whose learned spectrum exposes an operational coordinate system for deterministic and verifiable modification of attention-score formation.

---


### 355. [Topographic Training Concentrates Causal Circuits Without Improving Neuron Monosemanticity](https://arxiv.org/abs/2609.24379)

**<font color=#1a73e8>作者：</font>** Gautam Ranka, Shubham Santosh Pandere, Aiden Dsouza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability of vision transformers seeks to decompose model computation into human-readable units, but learned representations entangle many concepts in each neuron. Feature superposition is widely treated as the central obstacle to this decomposition, yet most mitigations (sparse autoencoders, dictionary learning) are post-hoc and leave the underlying network unchanged. We ask whether a spatial-locality training loss (TopoLoss) can act as a lightweight, training-time prior that improves interpretability of standard mech-interp tools. Training ViT on ImageNet-100 across multiple TopoLoss weights $\alpha$, we measure causal sufficiency of topographic clusters via activation patching and feature geometry via sparse autoencoders fit to the same residual stream. At $\alpha=1.0$, topographic clusters are 2.79$\times$ more causally sufficient than random unit sets of the same size, with the effect increasing monotonically in $\alpha$. SAE L0 sparsity decreases by 11% and dead-feature fraction rises 19-fold, yet standard neuron-level monosemanticity scores are unchanged, indicating that topographic pressure acts at circuit level, concentrating causal mass into spatially local structures without disentangling individual neurons. This dissociation suggests current neuron-level monosemanticity metrics are insensitive to a class of real interpretability gains, and positions cheap architectural priors as a viable training-time complement to post-hoc tooling.

---


### 356. [Credit Access is Associated with Improved Food Security in the Horn of Africa](https://arxiv.org/abs/2609.24382)

**<font color=#1a73e8>作者：</font>** Jordi Cerdà-Bautista, Vasileios Sitokonstantinou, José Manuel Veiga López-Peña 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The intensification of climate change poses a growing threat to food security, especially in vulnerable communities. This study employs an observational machine-learning framework to estimate the causal association between access to credit and acute food insecurity in Somalia and across the Horn of Africa, drawing on a harmonized dataset spanning key environmental, socioeconomic, and conflict-related factors from 2015 to 2022. Results indicate that greater credit access is associated with a 2% reduction in acute food insecurity at the population level over the study period. Given that, on average, 16% of the population is in crisis, this effect represents a meaningful shift within the at-risk group. We interpret these estimates under explicit identification assumptions and complement them with robustness and refutation tests. The results provide context-specific evidence on how financial access correlates with food security outcomes in data-scarce, crisis-affected settings, and offer a transparent framework for integrating heterogeneous data sources when randomized evaluations are infeasible.

---


### 357. [A Lightweight Convolutional Neural Network for Real-Time Recognition of Hand-Drawn Geometric Shapes](https://arxiv.org/abs/2609.24384)

**<font color=#1a73e8>作者：</font>** Shahir Abdullah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing hand-drawn geometric shapes is a foundational sub-problem of sketch recognition, with applications in education, human-computer interaction, and diagram digitization. This paper presents the design, implementation, and evaluation of a desktop application that recognizes four basic hand-drawn geometric shapes, circle, square, rectangle, and triangle using a compact Convolutional Neural Network (CNN). A dataset of 2,000 labeled 28x28-pixel shape images was collected independently and released publicly. The classifier consists of three convolutional blocks (16, 32, and 64 filters) with max-pooling, an in-model data-augmentation stage (random horizontal flip, rotation, and zoom), a dropout-regularized dense layer of 128 units, and a 4-way linear output layer, totaling 97{,}956 trainable parameters. The network is trained with the Adam optimizer on a sparse categorical cross-entropy objective computed directly on logits. On an 80/20 train-validation split, the model achieves 94.80% training accuracy and 96.01% validation accuracy with a validation loss of 0.1437. A Tkinter-based graphical interface allows a user to draw a shape with the mouse and receive an immediate class prediction with a confidence score. We situate this system within the broader sketch and shape-recognition literature, compare its accuracy against related hand-drawn shape classification studies, and discuss the limitations inherent to a small, single-contributor dataset. The complete source code, trained model, and per-class datasets are released publicly to support reproducibility.

---


### 358. [Machine Learning-Based Prediction of Childhood Stunting in Bangladesh: Fairness and Temporal Robustness Assessment](https://arxiv.org/abs/2609.24386)

**<font color=#1a73e8>作者：</font>** Md Ahshanul Haque, Muhammad Ashad Kabir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Childhood stunting remains a major public health concern in Bangladesh and reflects long-term growth failure influenced by child, maternal, household, socioeconomic, and health-service factors. This study used nationally representative Bangladesh Demographic and Health Survey data from 2007 to 2022 to develop machine learning models for population-level prediction of childhood stunting and to assess temporal robustness and subgroup fairness. Children aged 0-59 months with complete anthropometric and predictor data were included. Data from the 2007, 2011, and 2014 survey rounds were used for model development, while the 2018 and 2022 rounds were retained as temporal test datasets. Twelve feature-selection approaches were assessed, and the KNN permutation importance-selected predictor set was used for final model evaluation. Eleven machine learning models were evaluated: ten conventional algorithms and one pretrained tabular foundation model, TabPFN. Performance was assessed using balanced accuracy, AUROC, F1-score, Brier score, and expected calibration error. Subgroup fairness was examined by child sex, place of residence, and socioeconomic status. The final analytic sample included 18,844 children, of whom 35.05% were stunted. In the development hold-out test dataset, TabPFN showed the highest observed balanced accuracy overall at 67.58%, while AdaBoost showed the highest observed balanced accuracy among conventional models at 67.51%. In temporal testing, the highest observed balanced accuracy was found for Gradient Boosting in BDHS 2018 and XGBoost in BDHS 2022. Model performance varied across survey rounds and subgroups, highlighting the importance of temporal validation, subgroup fairness assessment, and transparent interpretation in public health prediction modeling.

---


### 359. [Name2Pkg: Lightweight One-Class Android Malware Screening via Name-Package Correspondence Modeling](https://arxiv.org/abs/2609.24389)

**<font color=#1a73e8>作者：</font>** Changyeop Sung, Yeonjae Kang, Jaeho Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep learning-based malware detection has been widely adopted in security-critical services. Most detection methods rely on internal features extracted from APK files or runtime behavior. However, extracting these features is computationally expensive. This limits their use in large-scale, early-stage screening. Malicious apps may exhibit weak correspondence between their user-facing app names and package names, providing a low-cost screening signal. We present Name2Pkg, a lightweight one-class classification method. It leverages only the app name and the package name. We formulate malware screening as a sequence anomaly detection problem. A character-level sequence-to-sequence model estimates the conditional likelihood of a package name given the app name. The length-normalized negative log-likelihood serves as the anomaly score. We train the model and calibrate the threshold using only benign data. Using a dataset of 67,129 real-world applications, Name2Pkg achieves an area under the receiver operating characteristic curve (ROC-AUC) of 0.982 and malware recall of 0.885 at an achieved false-positive rate of 0.044 on held-out test data. It has a 3.57 MiB checkpoint and a CPU inference latency of 28.20 ms per sample. Name2Pkg provides an efficient and effective pre-filtering signal for large-scale security systems.

---


### 360. [NAVIR: Neuromorphic Audio-Visual Speech Recognition for Robust Human-Robot Interaction on Edge Hardware](https://arxiv.org/abs/2609.24391)

**<font color=#1a73e8>作者：</font>** Leonidas Delimpasis, Panagiota Moraiti, Antonis Porichis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Voice-controlled interaction in industrial settings is hampered by acoustic noise, which severely degrades audio-only speech recognition. Audio-visual speech recognition (AVSR) addresses this by fusing lip-motion cues with the audio stream, but state-of-the-art pipelines rely on three-dimensional convolutions, recurrent units, and attention modules that exceed the budget of typical edge devices. We present NAVIR, an end-to-end AVSR system targeting the BrainChip Akida neuromorphic processor, which natively supports only sequential two-dimensional convolutional inference. The pipeline factorises spatial and temporal encoding into separate AkidaNet-based modules: a per-frame visual encoder, a temporal video encoder, and a spectrogram audio encoder, fused by a lightweight predictor head and decoded by constrained beam search. Models are trained with connectionist temporal classification on noise-augmented audio and then fine-tuned with quantization-aware training. On the GRID benchmark, the quantized audio-visual model reaches 14.0% word error rate (WER) under noise on the unseen-speaker split and 3.3% WER on the overlapped-speaker split, against 22.5% and 11.8% for audio-only baselines, and it attains 98.6% command accuracy at 1.5% WER on a task-specific industrial-command corpus. Operation-count analysis indicates a 13-fold energy advantage of the spiking formulation over its artificial neural network counterpart at 27.6% mean firing rate. On-board measurements show roughly 5-fold lower energy per inference than a Raspberry Pi central processing unit on the lip-reading model, and over 100-fold lower than a laptop graphics processing unit, while sustaining 14.5 inferences per second. To the best of our knowledge, this is the first complete multimodal AVSR pipeline running on neuromorphic hardware of this class.

---


### 361. [Passive Hybrid Network-Based Intrusion Detection System (Hybrid-NIDS) Combining Suricata and Random Forest](https://arxiv.org/abs/2609.24393)

**<font color=#1a73e8>作者：</font>** Quoc-Cuong Tang, Hoang-Lam Huynh, Van-Tri Phan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper evaluates a passive Hybrid Network-based Intrusion Detection System (Hybrid-NIDS) prototype that combines Suricata with Random Forest flow classification and centralized ELK-based alert handling. The study explicitly separates benchmark evaluation from PCAP/live operational validation and controls exact feature-duplicate leakage using feature hashing and group-aware splitting. From 2,540,047 UNSW-NB15 records, 453 conflicting-label hash groups containing 1,879 rows were removed; the resulting Development and Hold-out sets have zero exact feature-hash overlap. RF-41 achieved F1 = 0.971360 and ROC-AUC = 0.999671, while the NFStream-compatible RF-21 achieved F1 = 0.970148 on the same prepared hold-out boundary. However, operational validation revealed substantial benchmark-to-deployment domain shift: on a labeled laboratory PCAP, RF-21 and the strictly correlated branch achieved recall of only 0.0095, and RF-21 produced no alerts in five additional 60-second attack sessions. An unlabeled normal-traffic test produced 439 alerts from 2,375 flows; this value is reported only as an alert ratio and is not interpreted as a false-positive rate. These results show that strong performance on a public benchmark does not directly translate into operational effectiveness. Accordingly, the current Hybrid-NIDS should be interpreted as a passive prototype and evaluation framework, and the reported experiments do not demonstrate that Suricata-Random Forest correlation provides better operational detection than Suricata alone.

---


### 362. [Climate Variability Modulates the Impact of Price Spikes on Food Insecurity](https://arxiv.org/abs/2609.24394)

**<font color=#1a73e8>作者：</font>** Jordi Cerdà-Bautista, Vasileios Sitokonstantinou, Homer Durand 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Climate variability influences whether a market disruption escalates into a food crisis, yet broad climate patterns like El Niño, tracked months before they alter hydro-climatic conditions, are still not incorporated as an early-warning component in food-security responses. We address this gap by introducing sensitivity regimes, a stratification of regions by the direction and strength of their vegetation response to the El Niño Southern Oscillation, and using them to estimate how food price spikes affect acute food insecurity across sub-Saharan Africa. Integrating remote sensing, socioeconomic data, and causal machine learning, we find that in regions where ENSO systematically suppresses vegetation, a price spike raises the share of the population at acute risk by 5.4 percentage points in the following month. In regions where vegetation is unaffected by or positively linked to ENSO, the estimated effect is smaller (around 2 percentage points) and statistically insignificant. These results demonstrate that climate context is critical for understanding food security vulnerabilities. Sensitivity regimes can be combined with operational price-spike triggers to stage anticipatory action: the ENSO state flags vulnerable regions months ahead, and a pre-positioned response in those regions to a price spike would avert the largest jump in acute food insecurity.

---


### 363. [Probabilistic Modelling of Operational Design Domains, A New Approach for Testing AI Systems](https://arxiv.org/abs/2609.24397)

**<font color=#1a73e8>作者：</font>** Hans-Werner Wiesbrock  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The conventional testing process quickly fails when applied to ML-based systems such as obstacle detection in vehicles: if an obstacle is not detected in a test, classical bug fixing is impossible and an AI system will always retain shortcomings. Test results can therefore only be interpreted statistically, which in turn requires test sets that are not only complete with respect to the operational design domain (ODD) of the system, but also representative of it. To this end, we introduce probabilistically extended ontologies (PEONs): ontologies describing the ODD, augmented with a probability distribution over the partitioning they induce. Instead of unmaintainable conditional probability tables, only marginal distributions and functionally described dependencies need to be specified; algorithms based on couplings and optimal transport complete this specification to a Bayesian network. From a PEON we derive the sampling of representative test cases, rigorous end-of-test criteria for given quality targets and significance levels, and methods for re-evaluating existing test results and for assessing the balance of training data. We demonstrate the practical modelling of a complex ODD using the example of automatic train operation.

---


### 364. [Artificial Structure Function Search: Preserving Artificial Functional Connectivity for Structured Pruning](https://arxiv.org/abs/2609.24401)

**<font color=#1a73e8>作者：</font>** Mindula Illeperuma, Rafael Pina, Charuka Herath 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured pruning is a model compression technique that is used to reduce the computational cost of deploying deep neural networks on resource-constrained devices. Popular methods of pruning rely on opaque heuristics or weight-based criteria that give no indication as to the structural dependencies in the network. To address these limitations we present Artificial Structure Function Search (ASF-S): a novel structured pruning framework. ASF-S utilizes Principle Gradient Importance (PGI): a novel prune-candidate selection criteria that is inspired by structure-function relationships in the brain. By ensuring the pruned structure of the model respects topographical organization of the output layer, we define Artificial Functional Connectivity (AFC) for artificial neural networks. AFC provides evidence to demonstrate that accurate smaller networks can be found using careful prune candidate selection criteria. We present results for PGI as a selection criterion and for ASF-S as a pruning framework against recent benchmarks, demonstrating that our method yields model variants with 70\% parameter reduction, that can recover baseline accuracy without re-training the pruned layers.

---


### 365. [Can Spiking Neural Networks play pinball? A neuromorphic motion detector for target tracking](https://arxiv.org/abs/2609.24403)

**<font color=#1a73e8>作者：</font>** Mazdak Fatahi, Šárka Pryjmaková, Pierre Boulet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biological visual systems achieve continuous, low-latency motion perception by processing sparse, asynchronous spiking signals, enabling real-time tracking under strict energy constraints. Event-based cameras, inspired by the mammalian retina, replicate this efficiency by capturing only local brightness changes as asynchronous events, offering a natural substrate for spiking neural networks (SNNs) to parallelise computation and adapt to fast-changing scenes. Pinball provides a controlled yet dynamic testbed, requiring precise motion estimation and fast reaction to a small, rapidly moving target.
This work presents a fully spiking, real-time perception-to-action pipeline for closed-loop pinball gameplay. A dynamic vision sensor observes a small, fast-moving ball, and a network of spiking Time-Difference Encoders on the SpiNNaker neuromorphic platform jointly estimates its position, speed, and direction. The system is characterised across receptive field size, accumulation window, and angular tuning width for real-time operation, and benchmarked in closed loop against human players across two flipper regimes of increasing physical realism. It achieves a hit rate of 56.1%, nearly double the human average, reacting within 21.7 ms (5 ms network latency) and consuming an estimated 148 {\mu}W using fewer than 25k neurons, among the fastest and most energy-efficient event-based closed-loop demonstrators benchmarked. Under more realistic flipper dynamics, tuning a single interpretable policy parameter reproduces the full spectrum of human play styles, from cautious to aggressive, with no change to the perception pipeline. A physical demonstrator, tracking a real ball and actuating real flippers in closed loop, confirms the principle operates beyond simulation. Its fully spiking, learning-free design offers a compact, energy-efficient example of real-time neuromorphic perception-to-action.

---


### 366. [SkelOT: Reusing AOT Compilation Across EVM Contract Families](https://arxiv.org/abs/2609.24404)

**<font color=#1a73e8>作者：</font>** Sipeng Xie, Qianhong Wu, Minghang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ahead-of-time (AOT) compilers (e.g., revmc, evmone, and DTVM) for the Ethereum Virtual Machine (EVM) reuse compilation artifacts at contract-code-hash granularity. This granularity is poorly matched to real EVM workloads dominated by \emph{contract families}: factory-, proxy-, and template-driven deployments that share instruction structure but differ in a small set of embedded constants. Across four EVM chains (Base, Ethereum, BSC, and Arbitrum), we find that 23.1--47.6\% of unique compilable bytecodes map to shared family skeletons within 10K-block windows. Per-hash AOT therefore redundantly recompiles structurally equivalent code, inflating compile time and artifact footprint while reducing workload coverage under finite compile budgets.
We present \textsc{SkelOT}, an AOT framework that lifts the unit of compilation reuse from code hash to family skeleton. \textsc{SkelOT} compiles one native artifact per family, bakes invariant constants into the artifact, and reads variant constants from a per-contract runtime table. Built on revmc/LLVM and evaluated on a 10K-block Base mainnet corpus (3.52M transactions), \textsc{SkelOT} reduces compilation units by 47.5\%, artifact footprint by 57.4\%, and compile time by $2.19\times$, while preserving byte-identical execution outcomes versus per-hash AOT. At runtime, \textsc{SkelOT} delivers a $1.31\times$ median per-contract speedup across family members. Under a compile budget targeting 75\% execution-time coverage, \textsc{SkelOT} needs far fewer artifacts than per-hash AOT, and the advantage holds at every coverage target.

---


### 367. [End-to-end Jordanian dialect speech-to-text self-supervised learning framework](https://arxiv.org/abs/2609.24410)

**<font color=#1a73e8>作者：</font>** Ali A. Safieh, Ibrahim Abu Alhaol, Rawan Ghnemat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-text engines are extremely needed nowadays for different applications, representing an essential enabler in human-robot interaction. Still, some languages suffer from the lack of labeled speech data, especially in the Arabic dialects or any low-resource languages. The need for a self-supervised training process and self-training using noisy training is proven to be one of the up-and-coming feasible solutions. This article proposes an end-to-end, transformers-based model with a framework for low-resource languages. In addition, the framework incorporates customized audio-to-text processing algorithms to achieve a highly efficient Jordanian Arabic dialect speech-to-text system. The proposed framework enables ingesting data from many sources, making the ground truth from external sources possible by speeding up the manual annotation process. The framework allows the training process using noisy student training and self-supervised learning to utilize the unlabeled data in both pre- and post-training stages and incorporate multiple types of data augmentation. The proposed self-training approach outperforms the fine-tuned Wav2Vec model by 5% in terms of word error rate reduction. The outcome of this work provides the research community with a Jordanian-spoken data set along with an end-to-end approach to deal with low-resource languages. This is done by utilizing the power of the pretraining, post-training, and injecting noisy labeled and augmented data with minimal human intervention. It enables the development of new applications in the field of Arabic language speech-to-text area like the question-answering systems and intelligent control systems, and it will add human-like perception and hearing sensors to intelligent robots.

---


### 368. [Prior-Amortized In-Context Bayesian Inference for Generalized Linear Mixed-Effects Models](https://arxiv.org/abs/2609.24422)

**<font color=#1a73e8>作者：</font>** Alex Kipnis, Marcel Binz, Eric Schulz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical data is ubiquitous in the empirical sciences and is most commonly analyzed with generalized linear mixed-effects models (GLMMs). Bayesian inference for GLMMs yields calibrated uncertainty but requires MCMC; the No-U-Turn Sampler (NUTS) is the gold standard but is slow and must restart from scratch for every new dataset, model and prior. We introduce metabeta, a pretrained neural network for prior-amortized in-context Bayesian inference over GLMMs. Unlike previous neural posterior estimators that fix the prior at training time, metabeta accepts prior families and hyperparameters as inputs at test time, enabling zero-shot generalization. Two set transformers and conditional normalizing flows mirror the posterior's two-level structure (global parameters shared across groups, local parameters per group). The model is trained on millions of realistic simulated datasets spanning continuous, binary, and count outcomes. By default, the flow posterior is refined by Independence Metropolis-Hastings against the unnormalized posterior, so its correctness rests on the sampler rather than the network; this yields tuning-free inference two to three orders of magnitude faster than NUTS. Alternatively, the flow can warm-start NUTS, giving nearly identical inference with substantially increased speed and stability. On controlled benchmarks with ground-truth parameters, metabeta matches NUTS in parameter recovery, calibration and out-of-sample prediction. On out-of-distribution real datasets, its posteriors closely match those of NUTS across all parameter types, and they remain faithful under misspecified likelihoods and priors, out-of-distribution predictors, collinear designs, and data-poor regimes. The model is open-source and open-weights and thus immediately deployable.

---


### 369. [Estimating Accurate Hand Pose in Camera Space with Vision Transformer](https://arxiv.org/abs/2609.24424)

**<font color=#1a73e8>作者：</font>** Kaiwen Ren, Yiran Jiang, Yongjing Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular RGB-based hand pose estimation has emerged as a critical research frontier in computer vision. The local hand pose estimation methods predict hand poses relative to the wrist, while global hand pose estimation also requires estimating the wrist's position in the camera coordinate system. However, this camera-space estimation confronts two fundamental challenges: (1) depth ambiguity in monocular settings, and (2) the coupling effect of hand local poses and global wrist positions in the perspective projections. In particular, this coupling reflects that the projections are jointly determined by local hand poses, wrist positions, and camera intrinsics. To overcome these challenges, our framework proposes two key innovations: Transformation-Isomorphism Supervision for hand-depth information extraction and Perspective Information Embedding for resolving above coupling effect of local pose and wrist position, both integrated within the mainstream encoder-decoder architecture. Besides, we propose a novel framerate-aware multi-dataset training strategy for sequential pose refinement. Our fully integrated approach achieves at most 37.1\% superiority in CS-MJE over SOTA on HO3D. Project page: this https URL.

---


### 370. [Comparing Latent Concept Formation in State Space Models and Transformers via Sparse Autoencoders](https://arxiv.org/abs/2609.24440)

**<font color=#1a73e8>作者：</font>** Rithin Nagaraj, Rupa Laalasa Oruganti, Prerna Subhashchandra Kunder 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quadratic scaling of Transformer self-attention has driven the adoption of sub-quadratic Selective State Space Models (SSMs) like Mamba, which compress past context into a fixed-size recurrent hidden state. This strict informational bottleneck raises a foundational question for mechanistic interpretability: do SSMs and Transformers learn fundamentally distinct latent representations? In this work, we employ Sparse Autoencoders (SAEs) to conduct a large-scale, feature-level correspondence analysis between Mamba-130m and Pythia-70m over a 10-million token corpus. Contrary to hypotheses predicting widespread architectural divergence, we find no evidence of systematic representational divergence between architectures: across the observed Jaccard distribution, 99.98% of Mamba features cluster toward the upper alignment boundary, providing preliminary feature-level support for the Universality Hypothesis. We further identify and qualitatively characterize this microscopic fraction (0.02%) of diverging features, finding patterns consistent with the hypothesis that the recurrent bottleneck selectively limits the parsing of rigid syntax rather than broad semantic ontology. We demonstrate that while Pythia's unconstrained attention permits the monosemantic decomposition of distinct formatting edge-cases, Mamba is forced to compress unrelated syntactical anomalies into polysemantic "junk drawer" neurons to preserve state capacity. Collectively, these results suggest that architectural routing mechanisms may have negligible impact on core semantic understanding, with representational divergence confined to extreme structural margins.

---


### 371. [MUSE: Dependency-Aware Adaptation of a Frozen Vision Backbone for Multivariate Time Series Forecasting](https://arxiv.org/abs/2609.24441)

**<font color=#1a73e8>作者：</font>** Xinying Cai, Junkai Lu, Yuhan Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time-series forecasting is essential to many real-world applications. Recent large vision models (LVMs) offer a promising paradigm by transferring cross-domain visual priors to time-series forecasting. However, existing LVM-based methods face two key challenges: balancing independent visual representation spaces with cross-variable dependency modeling, and adapting vision backbones pretrained on natural images to the distinct temporal semantics of time-series images. To address these challenges, we propose MUSE, a dependency-aware adaptation framework built on a fully frozen pretrained MAE. First, the Variable Context Refinement Module (VCR) aggregates shared temporal information within each variable and models cross-variable contextual dependencies while preserving independent visual spaces. Second, the Temporal-Periodic Refinement Module (TPR) performs lightweight refinement at different encoder depths and explicitly models across-period temporal dependencies and within-period periodic dependencies. The two modules independently produce forecasts, which are fused through a learnable prediction-level gate. Experiments on 10 real-world datasets demonstrate that MUSE achieves state-of-the-art performance.

---


### 372. [WPBench: A Comprehensive Benchmark for Wind Power Forecasting](https://arxiv.org/abs/2609.24444)

**<font color=#1a73e8>作者：</font>** Yuhan Zhu, Jilin Hu, Xinying Cai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate, reliable, and deployable wind power forecasting is critical for power system dispatch, renewable energy integration, and electricity market operations. Progress in this field hinges on the ability to empirically and comprehensively benchmark forecasting methods. Yet existing benchmarks fall short of supporting systematic evaluation in four key aspects: 1) limited coverage of wind power scenarios across turbine scale, variable composition, and spatial structure; 2) incomplete coverage of forecasting model families; 3) evaluation metrics misaligned with wind power requirements; and 4) limited structure-aware diagnostics beyond individual temporal patterns. To address these limitations, we propose WPBench, a comprehensive, fair, and extensible benchmark for wind power forecasting. WPBench integrates 26 public datasets organized by turbine scale and variable composition, spanning single-turbine, multi-turbine, univariate, and multivariate settings. Under unified processing, training, and evaluation protocols, it benchmarks 19 representative models covering traditional methods, deep temporal models, spatio-temporal models, and foundation models. Beyond point-wise errors, WPBench assesses forecast-curve fidelity and computational efficiency, and delivers structure-aware diagnostics across temporal, variable-dependency, and spatial-dependency perspectives. Together, these capabilities enable systematic model comparison across diverse wind scenarios and provide a reusable platform for future research.

---


### 373. [Predicting Postprandial Glycemic Response from Meal Images, Clinical Variables, and Gut Microbiome Information](https://arxiv.org/abs/2609.24453)

**<font color=#1a73e8>作者：</font>** Varvara Kondratyeva, Kamilia Zaripova, Nassir Navab 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting postprandial glycemic response (PPGR) is fundamental to personalized nutrition and type 2 diabetes management, yet existing approaches typically rely on manually reported dietary intake, limiting their scalability in free-living settings. We propose a multimodal framework that replaces manual dietary logging with image-derived macronutrient estimates and integrates them with clinical variables and gut microbiome information for personalized PPGR prediction. The framework jointly performs image-based macronutrient estimation and glucose prediction, while an attention-based prediction module models interactions between dietary and host-specific information. We evaluate the proposed approach on a real-world dataset comprising meal images, continuous glucose monitoring, clinical variables, and gut microbiome profiles. The proposed model outperforms existing PPGR baselines using image-derived nutritional inputs and approaches the performance of methods that rely on manually reported macronutrients despite using automatically estimated nutritional information. These results demonstrate that combining image-derived nutrition with complementary clinical and gut microbiome information provides a practical foundation for scalable personalized PPGR prediction.

---


### 374. [A Leader-Driven Open Collaboration Platform for Exploring New Domains](https://arxiv.org/abs/2609.24466)

**<font color=#1a73e8>作者：</font>** Michael Weiss, Ibrahim AbuAlhaol, Mohamed Amin  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper describes the design and initial evaluation of a leader-driven open collaboration platform for exploring new domains. The goal of this platform is to enable the collaboration of subject matter experts across knowledge boundaries. Traditionally, new domains are explored from within a single specialist or a focused group perspective. However, this often introduces bias. Collaboration helps reduce such bias by providing access to a broader range of information sources, increasing the chances for producing new insights in a new domain. However, it also introduces a new problem: variance between the contributions made. Variance makes it difficult to produce a coherent document. In this paper, we report on our observations from developing an initial prototype of the open collaboration platform, and derive propositions about how leader-driven open collaboration helps reduce bias while containing variance.

---


### 375. [MIGA:Shared-Geometry Gaussian Representation with Implicit Amplitude Modeling for Accelerated 3D Multi-Echo MRI](https://arxiv.org/abs/2609.24468)

**<font color=#1a73e8>作者：</font>** Jingran Xu, Yuanyuan Liu, Yanjie Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional multi-echo MRI provides rich anatomical and quantitative information, but repeated volumetric encoding prolongs acquisition and motivates k-space undersampling. Reconstructing undersampled multi-echo data requires exploiting shared anatomy while preserving echo-dependent signal variation; full-volume modeling also introduces substantial computational and memory demands. We propose MIGA, a scan-specific framework comprising shared anisotropic Gaussian geometry, a coordinate-conditioned multi-output amplitude network, and explicit echo-specific phase variables. The Gaussian geometry provides common spatial support across echoes, the implicit network models spatially structured amplitude variations, and the phase variables retain echo-specific complex signal information. All components are jointly optimized using only the acquired multi-coil k-space, requiring no fully sampled training data. Experiments showed that MIGA consistently outperformed the comparison methods across imaging tasks and acceleration factors, with larger improvements under stronger undersampling. MIGA also achieved a favorable quality-cost balance among the evaluated full-volume multi-echo methods. These results support the effectiveness of combining shared Gaussian geometry with implicit echo-dependent amplitude modeling for accelerated 3D multi-echo MRI reconstruction.

---


### 376. [Mixed-integer flow formulations for motion planning and decision-making of networked multi-agent systems](https://arxiv.org/abs/2609.24474)

**<font color=#1a73e8>作者：</font>** Angelo Caregnato-Neto, Paul-Louis Delacour, Raf Van de Plas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This work investigates the use of flow-based connectivity maintenance constraints in mixed-integer linear programming (MILP) trajectory planning and decision-making models for networked multi-agent systems (MAS). We integrate flow-based encodings for standard and k-hop connectivity into MILP multi-vehicle maneuvering models that are widely used alongside receding horizon planning strategies. Their necessity and sufficiency is demonstrated, guaranteeing full coverage of potential network topologies. The flow formulation for standard connectivity decreases the growth of the required inequality constraints from exponential to polynomial w.r.t. the size of the MAS when compared to the state-of-the-art subtour elimination (SEC) method. The flow-based k-hop connectivity constraints decrease the number of required binary variables and decouple its growth from the number of hops. However, the impact of these formulations in performance is not straightforward due to the introduction of a substantial number of continuous flow optimization variables and, in the case of k-hop connectivity, additional inequality constraints. We investigate this trade-off through a statistical evaluation of costs and optimization times using a conventional branch-and-bound commercial solver and trials performed with randomized environments for increasingly larger MAS. The results show that the flow formulation outperforms SEC in standard connectivity problems, enabling the solutions to be computed for larger MAS considering the imposed optimization time limit. The reduction in number of binary variables enabled by the k-hop flow formulations decreases the theoretical worst-case number of iterations required by the branch-and-bound algorithm to compute the global optimal solution. Our results show that this advantage did not translate into improvements in the average performance when compared to the baseline.

---


### 377. [Beyond Screen Time: Demonstrating the Value of App Activity Logs to Understand User Behavior Further](https://arxiv.org/abs/2609.24477)

**<font color=#1a73e8>作者：</font>** Ole Schmitt, Pauline Gieseler, Frederik Riedel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Research on smartphone use remains fragmented, with studies differing in measures, methods, and platforms, limiting what we know about everyday behavior. We argue that event-level app activity logs should form the backbone of research on actual rather than recalled smartphone use. We conduct a secondary analysis of 4,571,252 app events from 1,972 participants across three longitudinal cohorts differing in age, country, recruitment, and platform, complemented by a published reference cohort. We reproduce established aggregate and micro-usage measures and examine temporal structure, application composition, transitions, and individual distinctiveness. Aggregate usage varies less than the organization of activity: adolescent use, for example, is structured around school schedules, while other cohorts show weaker within-day patterns. Application and transition patterns reveal behavioral differences obscured by screen time; an intervention reduced daily usage while increasing mean session duration. Activity traces also enabled 15-22% top-1 participant re-identification. We discuss methodological, reproducibility, and privacy implications for HCI.

---


### 378. [STA-TFM: Spatio-Temporal Aggregation Across Views TransForMer for Pose Estimation](https://arxiv.org/abs/2609.24482)

**<font color=#1a73e8>作者：</font>** Mena Kamel, Natalie Won, Amrut Sarangi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 3D human pose estimation (HPE) remains challenging due to depth ambiguity, occlu- sions, and the need for temporal consistency. While multi-view methods provide superior accuracy over monocular approaches, they often require complex setups. We introduce STA-TFM, a transformer-based architecture that combines spatial and temporal information for multi-view pose estimation. The approach leverages DSTformer, a monocular feature extractor, to capture long-range pose dependencies within each view. A fusion transformer then aggregates information across views to produce coherent 3D estimates. To address training data scarcity, we use a data generation pipeline that transforms any existing 3D pose dataset into multi-view setups with controllable parameters. Experiments on various datasets demonstrate that STA-TFM outperforms existing camera-parameter-free multi-view methods. STA-TFM achieves 50.9% and 49.5% reductions in mean per joint position error (MPJPE) and mean per joint velocity error (MPJVE) on the DHP19 dataset. Furthermore, it achieves 6.7% and 7.7% respective reductions on HAA4D, and a 15.2% MPJPE reduction on TotalCapture. STA-TFM handles noisy and missing 2D inputs, supporting potential deployment in healthcare monitoring, athletic assessment, and immersive technologies. Code, training checkpoints, and data are available at this https URL.

---


### 379. [Lifted Bellman Linear Programming for Offline Reinforcement Learning](https://arxiv.org/abs/2609.24489)

**<font color=#1a73e8>作者：</font>** Hyukjun Yang, Jongchan Park, Narim Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) typically trains a critic by minimizing a regression loss against bootstrapped value targets stabilized by target networks with exponential moving average (EMA) updates. Multi-step targets incorporate behavior-policy actions and therefore require off-policy correction. We instead impose in-sample Bellman optimality on the critic through inequality constraints. We formulate the Lifted Bellman Linear Program (LBLP), which lifts the linear programming characterization of Bellman optimality to the joint $(Q,V)$ space so that every constraint involves only state-action pairs in the dataset. Its unique minimizer is the in-sample optimal pair, and constraints along $K$-step segments of dataset trajectories leave this minimizer unchanged for any rollout policy and horizon. Under deterministic dynamics, this minimizer lies between the best dataset return and the optimal value. Relaxing the constraints into hinge penalties recovers the same solution above a finite penalty coefficient in the tabular case. Approximate Lifted Bellman Unconstrained Minimization (ALBUM) implements this relaxation with neural networks and detaches the $K$-step rollout targets by stop gradient. Its objective contains no squared regression onto bootstrapped targets, so it can be trained without target networks or EMA updates. Under deterministic dynamics, the LBLP solution is a stationary point of the detached update under a coefficient condition independent of $\gamma$ and $K$, and the inequality constraints allow discounted returns along dataset trajectories to serve as lower bounds without off-policy correction or action chunking. On OGBench, ALBUM uses a single critic with a Gaussian policy, matches the average performance of FQL, and is comparable to recent action-chunking methods, while using the fewest parameters and the least peak GPU memory among all compared methods.

---


### 380. [Identity-Consistent Analysis of Long-Shot Windsurfing Video: A Domain-Specific Offline Tracking System](https://arxiv.org/abs/2609.24492)

**<font color=#1a73e8>作者：</font>** Bertil Braun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-shot windsurfing video combines small targets, large camera pans, prolonged overlaps, and rapidly changing backgrounds. The desired output is not a generic MOT trace but a separate, stable rider-relative video for each surfer; one false identity merge can invalidate an otherwise useful result. We present an offline analysis system that detects surfers, forms conservative local tracklets, links them globally with camera-compensated motion and a foreground-masked sail-color descriptor, and uses two pose keypoints on the rig to drive a rider-relative virtual camera. The tracking stage is evaluated on 21 manually reconstructed development videos containing 41,004 retained observations. On this fixed-observation protocol, the production system achieves 0.957 pairwise precision, 0.918 recall, and 0.937 F1, compared with 0.792 F1 for OC-SORT and 0.828 for BoT-SORT. Compared with OC-SORT, it reduces fragmentation excess from 845 to 42, but nine of its 95 output tracks mix rider identities and these errors affect seven of the 21 videos.

---


### 381. [CMAMBADEPTH: Self-supervised Monocular Depth Estimation with Channel Mamba and Hybrid Attention](https://arxiv.org/abs/2609.24494)

**<font color=#1a73e8>作者：</font>** Xuezhi Xiang, Jiayao Liu, Heqi Xiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate monocular depth estimation serves as a core enabler for single camera scene understanding. However, existing self-supervised monocular depth estimation methods generally suffer from the bottleneck of inefficient cross-scale information interaction and difficulty in balancing local and global spatial modeling. In this paper, we propose CMambaDepth, a self-supervised framework that achieves efficient multi-scale feature fusion and fine-grained contextual modeling via channel-wise selective state propagation. Specifically, Bidirectional Channel Mamba (Bi-CMamba) aligns encoder features across scales and enables bidirectional information exchange among ordered scale groups. Unidirectional Channel Mamba (Uni-CMamba) progressively aggregates decoder features and retains fine-grained scale groups through a group selection mechanism for subsequent fusion. Furthermore, a Hybrid Attention Module (HAM) is introduced to combine large-kernel local context and Manhattan self-attention for complementary spatial modeling. Experimental results demonstrate that our method achieves highly competitive performance. Specifically, our model achieves an AbsRel of 0.094 and an RMSE of 4.156 on KITTI, and an AbsRel of 0.140 on DDAD. In the zero-shot cross-dataset generalization test on NYUv2, it attains an AbsRel of 0.232, outperforming the baseline RA-Depth by 7.2%.

---


### 382. [Prefix Puncturable Signatures with Smaller Signing Key from HIBS](https://arxiv.org/abs/2609.24503)

**<font color=#1a73e8>作者：</font>** Masayuki Tezuka, Keisuke Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Puncturable signatures, proposed by Bellare et al. (EUROCRYPT 2016), allow a signing key to be punctured (updated) so that it loses the ability to sign particular messages while retaining the ability to sign all others. Halevi et al. (ASIACRYPT 2017) introduced prefix puncturable signatures, in which the signing key can be punctured with respect to a target prefix so that it cannot sign messages whose prefixes match the target prefix. So far, several generic constructions of prefix puncturable signature schemes have been proposed, including constructions based on identity-based signatures (IBS) (ESORICS 2022) and delegated constrained signatures (IEEE Trans. Inf. Forensics Secure. 2024). However, these constructions suffer from drawbacks in terms of key size. When the prefix space is the set of all l-bit strings, the former construction requires a signing key consisting of 2^{l} IBS signing keys. The latter construction, when instantiated with a lattice-based delegated constrained signature scheme, yields a punctured signing key whose size grows quadratically with the number of puncturing operations Q^{Punc}. In this paper, we present a generic construction of prefix puncturable signatures from hierarchical identity-based signature (HIBS) schemes. When the prefix space is {0,1}^{l} and our construction is instantiated with the lattice-based HIBS scheme HIBS^{GPV} by Ruckert (PQC 2010), our construction achieves a punctured signing key size bounded by O(lQ^{Punc}).

---


### 383. [On Emergent Capabilities and Model Merging](https://arxiv.org/abs/2609.24504)

**<font color=#1a73e8>作者：</font>** Luca Zhou, Emanuele Rodolà  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuned checkpoints and adapters now fill public repositories, and the most common operation applied to these artifacts is model merging: arithmetic on their weights that assembles capabilities cheaply. We ask what this operation does to emergent capabilities: behaviors an artifact carries that were never an explicit training target. Studying two independent testbeds (activation oracles and emergent-misaligned models) across three model families, we find that the answer is threefold. First, merging preserves an emergent capability that both parents carry: merging two misaligned checkpoints retains most of their broad misalignment across the whole mixing range. Second, merging cannot create an emergent capability that is superadditive in its parents: no weighted merge of two single-task oracles reaches the jointly-trained oracle's auditing ability. Third, when only one parent carries the capability, merging dilutes it faster than the trained capability that accompanies it: the gap is significant in most settings. In short, emergent behaviors of an artifact do not compose the way its trained capability does.

---


### 384. [0.5\%>100\%: Bidirectional Reciprocal Learning for Referring Image Segmentation](https://arxiv.org/abs/2609.24510)

**<font color=#1a73e8>作者：</font>** Xiaoqiang Lu, Licheng Jiao, Lingling Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision foundation models (VFMs) have shown remarkable capabilities across diverse unimodal visual tasks. However, adapting VFMs to referring image segmentation (RIS) typically necessitates precise vision-language alignment via full fine-tuning, incurring substantial computational overhead and risking catastrophic forgetting. While existing parameter-efficient fine-tuning (PEFT) methods enable safe knowledge transfer with minimal training costs, they predominantly operate independently within individual modalities or focus exclusively on unidirectional guidance from language to vision, overlooking progressive cross-modal interaction and visual feedback for textual refinement. To address these limitations, we propose Bidirectional Reciprocal Learning (BRL), a novel adapter-based PEFT framework that facilitates hierarchical, bidirectional information flow within both token-mixing and channel-mixing layers of frozen foundation models. Specifically, BRL introduces two complementary lightweight modules. The Reciprocal Attention Adapter (RAA) performs cross-modal query-key exchanges at the token level, enabling visual and linguistic tokens to mutually attend to each other for fine-grained spatial grounding. The Reciprocal Gate Adapter (RGA) generates cross-modal gating signals at the channel level, allowing global semantic context from one modality to adaptively recalibrate channel activations of the other. Extensive experiments on RefCOCO, RefCOCO+, and RefCOCOg benchmarks demonstrate the superiority of BRL over prior RIS methods, achieving state-of-the-art performance while requiring less than 0.5% backbone parameter updates. Code and models will be released at this https URL.

---


### 385. [Not All Task Vectors Need Equal Rank: Energy-Proportional Allocation for Model Merging](https://arxiv.org/abs/2609.24517)

**<font color=#1a73e8>作者：</font>** Hyunjoong Cho, Jinhyeok Jang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model merging aims to combine multiple fine-tuned models derived from a common pretrained model into a single multi-task model without additional joint training. Recent spectral merging methods improve over simple weight averaging by exploiting low-rank structures of task-specific updates, but they commonly assign the same rank capacity to every task. This uniform allocation ignores that task vectors can have heterogeneous spectral complexity, causing the shared merging space to be used suboptimally. In this paper, we propose Spectral Energy-proportional Rank Allocation (SERA), a simple task-adaptive strategy that allocates ranks according to the singular-value energy structure of each task vector. By assigning richer spectral capacity to complex or isolated tasks and fewer directions to compact tasks, SERA extends SVD-based model merging from uniform-capacity merging to task-dependent capacity allocation. Experiments under standard vision model merging protocols show that SERA improves multi-task merging performance while preserving the same total rank budget as existing spectral merging methods. Further analysis demonstrates that task-level spectral concentration is closely related to the per-task effect of adaptive rank allocation, providing insight into when and why SERA is effective.

---


### 386. [Preoperative Prediction of Microvascular Invasion in Hepatocellular Carcinoma by Integrating Multimodal Ultrasound and Clinical Data: A Multicenter Study](https://arxiv.org/abs/2609.24524)

**<font color=#1a73e8>作者：</font>** Jun Cheng, Yuanyuan Kong, Qing Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Microvascular invasion (MVI) predicts recurrence and survival in hepatocellular carcinoma (HCC) but requires postoperative histopathology for diagnosis. We developed and validated a model integrating multimodal ultrasound and clinical data for preoperative MVI prediction. Methods: This multicenter study included 489 patients with HCC from eight centers. All patients had B-mode ultrasound (BUS), color Doppler flow imaging (CDFI), dynamic contrast-enhanced ultrasound (DCE-US), and clinical information. Data from seven centers (n = 421) were used for model development with five-fold cross-validation; data from the remaining center (n = 68) formed an independent external validation cohort. The proposed multimodal information fusion network used modality-specific encoders, a hemodynamic temporal change module for bidirectional DCE-US perfusion changes, and a representation consistency learning module to align heterogeneous ultrasound representations before Transformer-based fusion. Results: In external validation, DCE-US achieved the highest single-modality area under the receiver operating characteristic curve (AUC; 0.8545+/-0.0198), versus clinical information (0.6715+/-0.0156), CDFI (0.6435+/-0.0344), and BUS (0.6087+/-0.0417). Pixel-difference sampling and the proposed temporal module outperformed alternative sampling and video representation methods. The full model achieved the best performance, with an AUC of 0.8953+/-0.0180, accuracy of 81.18%+/-2.83%, sensitivity of 86.40%+/-6.69%, and specificity of 78.14%+/-6.28. Conclusions: Integrating multimodal ultrasound and clinical information enabled promising preoperative MVI prediction in HCC. DCE-US was the main source of predictive information, while BUS, CDFI, and clinical information provided complementary value. The proposed framework may support preoperative risk stratification and individualized clinical decision-making.

---


### 387. [Finger-to-Ear ECG: Systematic Evaluation of an Earbud-Based Cardiac Monitoring Approach](https://arxiv.org/abs/2609.24530)

**<font color=#1a73e8>作者：</font>** Philipp Lepold, Paula Breitling, Jonas Hummel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Ear-ECG enables unobtrusive cardiac monitoring, but existing approaches often struggle with low signal amplitudes and limited morphology preservation. We evaluate a finger-to-ear ECG paradigm that combines an in-ear electrode with a rear housing finger-contact electrode in a speaker-equipped earbud. A study with 30 participants investigated four finger-to-ear electrode geometries against chest-reference ECG and additionally assessed robustness under music playback, talking, and walking disturbances. Left-finger configurations achieved R peak detection F1-scores >99% with high agreement of key ECG morphology features. In contrast, right finger configurations as well as walking led to severe signal degradation. The results reveal a trade-off: while cross-body setups provided the highest signal fidelity, users preferred same-side contacts for comfort reasons. This establishes finger-to-ear ECG as a robust, morphology-aware paradigm for opportunistic sensing in earables.

---


### 388. [Dynamic Thermal Gaussians: Multimodal 4D Gaussian Splatting](https://arxiv.org/abs/2609.24531)

**<font color=#1a73e8>作者：</font>** Rongfeng Lu, Lifeng Lin, Xiaobao Wei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermography plays a vital role in military and broader thermal analysis applications. Recent progress in 3D thermal reconstruction has extended temperature analysis from 2D to 3D space, yet most existing works assume static temperature distributions, neglecting the temporal dynamics of heat transfer in real-world environments. To address this limitation, we propose the first dynamic RGB-Thermal reconstruction framework for complex scenes. Our method jointly models RGB appearance, thermal observations, and scene geometry as they change over time. Specifically, we introduce a multimodal dynamic scene representation that anchors both the color and thermal modalities to a shared geometric substrate, ensuring their consistency under spatiotemporal deformations. We further design multimodal embeddings to enhance the motion expressiveness for each modality, and propose a multimodal routing mechanism that retains a unified set of shared multimodal Gaussians as the geometric backbone while adaptively spawning modality-specific Gaussians to strengthen the representational capacity in detail-rich regions of each individual modality. In addition, we contribute a novel benchmark dataset featuring high-frequency temperature variations to facilitate the evaluation of 4D reconstruction. Extensive experiments demonstrate that our method achieves high-fidelity spatiotemporal reconstruction of both appearance and temperature. Our code and dataset are available at: this https URL.

---


### 389. [MIRAGE: Full-Body Bystander Privacy for Smart Glasses with Consent-Based Restoration](https://arxiv.org/abs/2609.24537)

**<font color=#1a73e8>作者：</font>** Muhammad Umair, Muhammad Danial Maqbool, Fatima Arshad Cheema 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video recording on smart glasses exposes more than faces. Continuous capture reveals full-body biometric signatures, including gait, posture, and silhouette, that enable person re-identification (ReID) even after conventional face sanitization.
We present MIRAGE, a three-tier architecture for privacy-preserving smart glasses that enforces full-body privacy, supports synthetic full-body replacement, and retains encrypted recovery material for consent-based restoration. We implement MIRAGE on a Raspberry Pi~5 (a CPU-only proxy for smart-glasses compute), companion phones, and a cloud generative backend. Compared to prior systems, MIRAGE achieves 0.948 AP and 0.976 AR while accurately detecting the complete visible body. Its bounding box masking reduces learned silhouette-based ReID to essentially random guessing, with 10.86% Rank-1 accuracy compared with an 11.12% measured chance level. Even against an adaptive adversary retrained on MIRAGE's sanitized pose signals, Rank-1 gait identification drops from 90.25% to 26.20%, removing 72.5% of the adversary's identification advantage.

---


### 390. [Incentive Noise and Structural Prior Infusion for Multi-modal Object Re-Identification](https://arxiv.org/abs/2609.24539)

**<font color=#1a73e8>作者：</font>** Weixiang Zhou, Yuhao Wang, Xingguo Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal object Re-Identification (ReID) benefits from complementary information across heterogeneous imaging modalities. To further enrich semantic representation, text descriptions have recently been incorporated as an additional modality. However, recent vision-language approaches often treat text descriptions as clean, deterministic signals and overlook their inherent noise, including modality-mismatched phrases and semantically ambiguous expressions. Moreover, prevailing methods lack explicit mechanisms to reconcile fine-grained structural discrepancies between modalities, even after high-level semantic alignment. To address these challenges, we propose a novel framework centered on Positive-Incentive Noise ({\pi}-noise) and structured prompt modulation. First, the Semantic Cross-Modal Modulator harnesses task-aware {\pi}-noise, sampled from a distribution conditioned on both visual and text inputs, to perturb global tokens and enable semantics-guided cross-modal compensation. Second, the Structure-Aware Prompt Adapter injects learnable geometric priors via prompts to enhance spatial consistency. Third, the Context-Aware Sparse Fusion module distills structural context to guide adaptive fusion while shielding identity features from noisy local details. Experiments on three multi-modal ReID benchmarks demonstrate the effectiveness and robustness of our approach. The code is available at this https URL.

---


### 391. [Toward a Unified Mathematics of Concepts](https://arxiv.org/abs/2609.24554)

**<font color=#1a73e8>作者：</font>** Chen Shani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Concepts are commonly defined as abstract, compact representations of knowledge and treated as basic units of intelligent behavior. Yet, cognition, psychology, and AI lack a shared mathematical language for them. Modern systems represent concepts as vectors, distributions, symbols, graphs, and other structures, but these formalisms are typically treated as competing rather than as solutions to a common problem. We propose an operation-based view that evaluates mathematical frameworks by the conceptual operations they support, identifying thirteen operations (including similarity, composition, generalization, and grounding) that recur across cognition, psychology, and AI. We show that ten frameworks embody distinct commitments to concepts as self-contained content, relational structure, or evolving process, and that these commitments determine which operations each supports naturally. For example, vector-based models facilitate graded similarity and generalization but struggle with explicit composition, whereas symbolic models support composition but offer but generalize poorly. No single framework we examined naturally supports all operations without extension. We test this account empirically using categorization as a case study, operationalizing nine theories on the same items against human judgments. Despite addressing the same conceptual question, the theories produce different procedures and results, demonstrating that mathematical commitment shapes what a theory can explain. We call for hybrid formalisms that treat content, relation, and process as jointly primary.

---


### 392. [The Endless Exam: Mathematical Constructions from Today's Models toward Superintelligence](https://arxiv.org/abs/2609.24555)

**<font color=#1a73e8>作者：</font>** Muhan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce the Endless Exam, a benchmark for measuring mathematical progress from today's models toward artificial superintelligence through fourteen parameterised construction families. Each submitted object is checked automatically for validity and assigned a relative quality score against a published frontier or construction baseline, without capping improvements at $1$. The families draw on open mathematical problems for long-term targets and generate new instances at larger parameters, where compact certificates keep large constructions verifiable. Across eight models evaluated on 69 distinct instances, continuous quality scores distinguish performance even though no evaluated system surpasses a published frontier. Size-quality curves show how construction quality changes as problem size increases. We release the generators, verifiers, references, model responses and analysis to support continued measurement before and beyond human frontiers.

---


### 393. [Evaluating Transformation Models for pCLE Mosaic Registration](https://arxiv.org/abs/2609.24560)

**<font color=#1a73e8>作者：</font>** Ahmed Aboelela, Johannes Barcsay, Jana Friedhof 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Confocal Laser Endomicroscopy (CLE) provides real-time, cellular-resolution optical biopsy but has a narrow field of view, which image mosaicing can extend to provide anatomical context. Because of line-by-line acquisition, probe motion, and probe-tissue interaction, frame alignment generally requires a non-linear transformation whose accuracy is difficult to quantify: flexible transformation models can fit intensity features and noise, so appearance-based metrics such as Normalized Cross-Correlation (NCC) can improve without a genuine gain in geometric accuracy. We therefore establish a dataset of 132 frame pairs across fourteen pCLE sequences from 4 patients with manually annotated landmark correspondences, so that Target Registration Error (TRE) can serve as a geometrically grounded complement to NCC. We assess the effect of progressively increasing the transformation model's degrees of freedom, from translation to Thin Plate Spline (TPS), and of six feature-matching backends spanning classical (Shi-Tomasi, Lucas-Kanade) and learned (SuperPoint, SuperGlue, LightGlue, LoFTR, RoMa) approaches. Translation and rigid models prove insufficient under tissue deformation, while TPS with random sampling achieves the strongest landmark-derived alignment of the evaluated configurations; among the learned matchers, used without fine-tuning, only RoMa offers a robust, if modest, advantage over other methods. At the sequence level, pairwise registration quality proved an unreliable predictor of final mosaic quality, so mosaic quality must be evaluated directly rather than inferred from pairwise metrics.

---


### 394. [Active Visual Sampling with a Connectome-Constrained Fly Model for One-Shot Hatch Recognition in Architectural Drawings](https://arxiv.org/abs/2609.24565)

**<font color=#1a73e8>作者：</font>** Dmitry Kuklev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Architectural drawings encode material classes through repeated hatch patterns. We test whether a connectome-constrained fly visual network, pretrained for motion, can be repurposed without task-specific weight updates as a descriptor for one-shot hatch matching. Each 64 x 64 patch is translated over eight scan trajectories and summarized across 57 cell types; query descriptors are then matched to one legend strip per class. On 400 development sheets from a synthetic benchmark built on CubiCasa5K geometry, the frozen fly pipeline reaches 0.857 area-weighted accuracy and 0.910 with an extended legend. On an equal-brightness orientation condition it reaches 0.840 versus 0.299 for eleven pixel statistics, while a Gabor bank reaches 0.900. Replacing drift with a repeated still frame lowers the combined equal-condition score by 0.089 [0.066, 0.112]. However, a receptors-only descriptor reaches 0.891 and a task-trained 5,888-parameter CNN averages 0.959, so the current evidence supports transfer and the usefulness of active sampling, but not an advantage of the biological wiring. We separate project-recorded results from recomputed checks and report a small real-drawing audit. The supported claim is therefore narrow: motion-oriented biological vision can be repurposed as a useful texture representation for architectural hatch matching, while the topology contribution and end-to-end BIM utility remain open questions.

---


### 395. [Universal Multi-Modal Traceformer: Integrating Heterogeneous Context for Process Event Prediction](https://arxiv.org/abs/2609.24579)

**<font color=#1a73e8>作者：</font>** Fabian Spaeh, Jingxing Fang, Shandian Zhe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Event logs arise in a wide range of real-world processes, capturing not only event activities and timestamps but also multi-modal contextual information. Existing event-sequence models, including many temporal point process approaches, primarily model event activities and timestamps while overlooking heterogeneous context, such as numerical measurements, categorical attributes, textual descriptions, and metadata associated with individual events and entire traces. In this paper, we propose Universal Multi-Modal Traceformer (UMT), a unified framework for incorporating heterogeneous process context into next-event prediction. Built on a Transformer backbone, UMT introduces a universal feature encoder that maps diverse feature types into a shared representation space and handles contextual information at both the event and trace levels. UMT further develops a per-event Perceiver module that dynamically weights contextual features and adaptively integrates them into event-token representations. To accommodate the heavy-tailed and potentially multi-modal distribution of inter-arrival times, UMT represents each interval at multiple temporal scales and jointly predicts the corresponding scale-specific quantities. Experiments on 13 real-world event logs show that UMT improves both next-event activity and time prediction over existing approaches.

---


### 396. [Overlay\_dx - Automating forecasting evaluation](https://arxiv.org/abs/2609.24586)

**<font color=#1a73e8>作者：</font>** Long Ngo, Mohammed Amine Chamli, Jonathan Rivalan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional evaluation metrics provides numerical values but often lack comprehensibility, hindering effective differentiation of model performances. Our work addresses this challenge by introducing overlay\_dx, a novel evaluation metric measuring the performance of time series prediction models. Overlay\_dx is a visual metric that represents the percentage of predictions falling within a confidence interval around actual values. Additionally, once evaluation results are plotted, overlay\_dx computes the area under the overlay curve, providing a quantitative measure of alignment between predicted and actual values across different thresholds and predictions. Through extensive experiments, we demonstrate that our approach offers a unified evaluation framework that combines both visual and numerical assessments, enabling improved model comparison and providing valuable insights for further research and optimization efforts in time series prediction.

---


### 397. [Taking a Second Look: Correcting Sea Ice Forecasts with Sparse Observations](https://arxiv.org/abs/2609.24591)

**<font color=#1a73e8>作者：</font>** Tianshuo Zhang, Xianglei Xing, Aowen Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sea ice forecasts are issued several days ahead, allowing errors to accumulate while new, often sparse sea ice concentration (SIC) observations become available. We find that fixed-propagation errors concentrate near structured, high-gradient ice edges, whereas homogeneous interiors require limited propagation, suggesting that propagation distance should be state dependent. We therefore introduce ECHO (Evidence-guided Correction with Heterogeneous prOpagation), where ECHO-Scale adapts propagation distance while preserving correction geometry, and ECHO-Delta learns a bounded residual around fixed propagation. Across all 96 standard evaluation settings spanning diverse priors, observation times, sparsity levels, geometries, and noise conditions, both outperform fixed propagation. ECHO-Delta achieves the best average accuracy, while ECHO-Scale is more robust to geometry shifts. Code is available at this https URL.

---


### 398. [Applications of Neural Cellular Automata: State of the Art, Challenges and Opportunities](https://arxiv.org/abs/2609.24595)

**<font color=#1a73e8>作者：</font>** Nick Lemke, Niklas Ihm, John Kalkhof 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural Cellular Automata (NCAs) are a new type of neural network architecture which enable accurate and robust inference at extremely small model sizes. Recently, NCAs have advanced to become interesting low-resource alternatives to convolution- and attention-based architectures for various tasks such as image analysis, synthetic image generation, and simulation. The rapid development and increased research interest necessitate a comprehensive review of the emerging technology. This review provides an overview of the fundamentals of NCAs, applications to medical imaging, as well as insights into the state of the art. We analyze recent modifications to the originally proposed NCA architecture with respect to their efficiency and accuracy. Furthermore, we review practical applications in real-world scenarios with a focus on medical image analysis, segmentation, classification, registration, depth estimation, and image synthesis. Finally, we identify several advantages of NCAs, research gaps, and conclude with an analysis of future opportunities for NCAs in medical applications in confined settings or areas that have particular demands for robustness or efficient data processing.

---


### 399. [GraphToolbox: A Configurable Python Framework for Graph Neural Network Forecasting](https://arxiv.org/abs/2609.24609)

**<font color=#1a73e8>作者：</font>** Eloi Campagne, Yvenn Amara-Ouali, Yannig Goude 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electricity forecasting often involves spatially related signals observed over regions, substations, and feeders, and Graph Neural Networks (GNNs) provide a natural way to represent these relations. Building a complete GNN forecasting experiment is nonetheless laborious, because graph construction, model selection, training, aggregation, and interpretation sit in incompatible tools. We present GraphToolbox, an open-source Python framework that unifies these stages in one configurationdriven pipeline built on PyTorch Geometric. It offers data-driven graph construction, an adapter that instantiates and trains 51 of the 65 PyTorch Geometric convolutions together with the recurrent cells of PyTorch Geometric Temporal, online expert aggregation, forecasting interpretability, and significance testing on cached forecasts. We evaluate the pipeline in two case studies. On French regional load, the 48 convolutions included in the complete forecasting sweep fall in a band from 1.14% to 1.60% error, online aggregation lowers this to 0.98%, and the graph models improve on classical additive and boosting baselines. On net-load, direct graph models are less accurate than a classical additive model, while forecasting each physical component separately improves them without closing that gap. Both comparisons use the same experimental interface, illustrating the role of GraphToolbox in systematic architectural evaluation.

---


### 400. [Beyond Uniform Subspaces: Spectrum-Aware and Depth-Adaptive Fusion for Multi-Task Model Merging](https://arxiv.org/abs/2609.24612)

**<font color=#1a73e8>作者：</font>** Ruxi Gu, Zilei Wang, Wei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model merging aims to consolidate multiple task-specific models without access to extra training process. However, existing subspace-based methods largely rely on a uniform treatment of task updates, overlooking their intrinsic spectral and depth-wise heterogeneity. We identify two key deviations from this assumption: different tasks require different subspace capacity and exhibit different tolerance to spectral transformation, while subspace projection introduces depth-dependent distortion. Based on these observations, we propose SADA-Merging, a spectrum-aware and depth-adaptive framework for data-free model merging. SADA-Merging allocates task-specific subspace capacity according to spectral complexity, adapts spectral preservation according to task-wise plasticity, and applies depth-dependent anchoring to compensate for projection-induced distortion. This enables the fusion process to adapt to both the intrinsic geometry of each task and its sensitivity across network depth. SADA-Merging operates directly on task updates and is applicable to both full fine-tuning and LoRA settings. Extensive experiments demonstrate consistent improvements over existing data-free merging methods across different task scales and adaptation settings.

---


> [!TIP]
> 当前位于：**351-400**（第 8/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-463](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
