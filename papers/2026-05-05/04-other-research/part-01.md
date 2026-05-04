# 📦 其他研究 | 2026年05月05日

> 本类共 **180** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-180](./part-04.md)

---

### 1. [Cloud Is Closer Than It Appears: Revisiting the Tradeoffs of Distributed Real-Time Inference](https://arxiv.org/abs/2605.00005)

**<font color=#1a73e8>作者：</font>** Pragya Sharma, Hang Qiu, Mani Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing deployment of deep neural networks (DNNs) in cyber-physical systems (CPS) enhances perception fidelity, but imposes substantial computational demands on execution platforms, posing challenges to real-time control deadlines. Traditional distributed CPS architectures typically favor on-device inference to avoid network variability and contention-induced delays on remote platforms. However, this design choice places significant energy and computational demands on the local hardware. In this work, we revisit the assumption that cloud-based inference is intrinsically unsuitable for latency-sensitive control tasks. We demonstrate that, when provisioned with high-throughput compute resources, cloud platforms can effectively amortize network and queueing delays, enabling them to match or surpass on-device performance for real-time decision-making. Specifically, we develop a formal analytical model that characterizes distributed inference latency as a function of the sensing frequency, platform throughput, network delay, and task-specific safety constraints. We instantiate this model in the context of emergency braking for autonomous driving and validate it through extensive simulations using real-time vehicular dynamics. Our empirical results identify concrete conditions under which cloud-based inference adheres to safety margins more reliably than its on-device counterpart. These findings challenge prevailing design strategies and suggest that the cloud is not merely a feasible option, but often the preferred inference location for distributed CPS architectures. In this light, the cloud is not as distant as traditionally perceived; in fact, it is closer than it appears.

---


### 2. [FedACT: Concurrent Federated Intelligence across Heterogeneous Data Sources](https://arxiv.org/abs/2605.00011)

**<font color=#1a73e8>作者：</font>** Md Sirajul Islam, Isabelle G Chapman, N I Md Ashafuddula 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative intelligence across decentralized data source devices in a privacy-preserving way. While substantial research attention has been drawn to optimizing the learning process for an individual task, real-world applications increasingly require multiple machine learning tasks simultaneously training their models across a shared pool of devices. Naively applying single-FL optimization techniques in multi-FL systems results in suboptimal system performance, particularly due to device heterogeneity and resource inefficiency. To address such a critical open challenge, we introduce {\em FedACT}, a novel resource heterogeneity-aware device scheduling approach designed to efficiently schedule heterogeneous devices across multiple concurrent FL jobs, with the goal of minimizing their average job completion time (JCT). {\em FedACT} dynamically assigns devices to FL jobs based on an alignment scoring mechanism that evaluates the compatibility between available resources of devices and resource demands of jobs. Additionally, it incorporates participation fairness to ensure balanced contributions from devices across jobs, further enhancing the accuracy levels of learned global models. An optimal scheduling plan is formulated in {\em FedACT} by prioritizing devices with higher alignment scores, while ensuring fair participation across jobs. To evaluate the effectiveness of the proposed scheduling algorithm, we carried out comprehensive experiments using diverse FL jobs and benchmark datasets. Experimental results demonstrate that {\em FedACT} reduces the average JCT by up to 8.3\(\times\) and improves model accuracy by up to 44.5\%, compared to the state-of-the-art baselines.

---


### 3. [What Physics do Data-Driven MoCap-to-Radar Models Learn?](https://arxiv.org/abs/2605.00018)

**<font color=#1a73e8>作者：</font>** Kevin Chen, Kenneth W. Parker, Anish Arora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven MoCap-to-radar models generate plausible micro-Doppler spectrograms, but do they actually learn the underlying physics? We introduce a physics-based interpretability framework to answer this question via two proposed complementary metrics: one measures alignment between model predictions and the physics-derived Doppler frequency, while the other tests whether predictions preserve the velocity-frequency relationship under velocity intervention. Both metrics require only MoCap input and model predictions, without access to measured radar data. Experiments across several model architectures reveal that low reconstruction error does not guarantee physical consistency: some, but not all, models achieve low error yet perform poorly on the two physics-based metrics. Further analysis shows that temporal attention is critical for transformer-based models to learn the underlying physics.

---


### 4. [Putting HUMANS first: Efficient LAM Evaluation with Human Preference Alignment](https://arxiv.org/abs/2605.00022)

**<font color=#1a73e8>作者：</font>** Woody Haosheng Gan, William Held, Diyi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of large audio models (LAMs) demands efficient approaches for model comparison, yet comprehensive benchmarks are costly. To fill this gap, we investigate whether minimal subsets can reliably evaluate LAMs while reducing costs and data redundancy. Analyzing 10 subset selection methods with 18 audio models across 40 tasks covering major LAM evaluation dimensions, we show that subsets of just 50 examples (0.3% of data) can achieve over 0.93 Pearson correlation with full benchmark scores. To understand how well these scores align with what practitioners ultimately care about, user satisfaction, we collect 776 human preference ratings from realistic voice assistant conversations, finding that both subsets and full benchmark achieve only 0.85 correlation with human. To better predict preferences, we trained regression models on these selected subsets, achieving 0.98 correlation -- outperforming regression models trained on both random subsets and the full benchmark. This demonstrates that in regression modeling, well-curated subsets outpredict the full benchmark, showing quality over quantity. We open-source these regression-weighted subsets as the HUMANS benchmark, an efficient proxy for LAM evaluation that captures both benchmark performance and user preferences.

---


### 5. [Learning physically grounded traffic accident reconstruction from public accident reports](https://arxiv.org/abs/2605.00050)

**<font color=#1a73e8>作者：</font>** Yanchen Guan, Haicheng Liao, Chengyue Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic accidents are routinely documented in textual reports, yet physically grounded accident reconstruction remains difficult because detailed scene measurements and expert reconstructions are scarce, costly and hard to scale. Here we formulate accident reconstruction from publicly accessible reports and scene measurements as a parameterized multimodal learning problem. We construct CISS-REC, a dataset of 6,217 real-world accident cases curated from the NHTSA Crash Investigation Sampling System, and develop a reconstruction framework that grounds report semantics to road topology and participant attributes, reconstructs lane consistent pre-impact motion, and refines collision relevant interactions through localized geometric reasoning and temporal allocation. Our method outperforms representative baselines on CISS-REC, achieving the strongest overall reconstruction fidelity, including improved accident point accuracy and collision consistency. These results show that public accident reports can serve as scalable computational substrates for quantitatively verifiable accident reconstruction, with potential value for traffic safety analysis, simulation and autonomous driving research.

---


### 6. [Learning from the Unseen: Generative Data Augmentation for Geometric-Semantic Accident Anticipation](https://arxiv.org/abs/2605.00051)

**<font color=#1a73e8>作者：</font>** Yanchen Guan, Haicheng Liao, Chengyue Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anticipating traffic accidents is a critical yet unresolved problem for autonomous driving, hindered by the inherent complexity of modeling interactions between road users and the limited availability of diverse, large-scale datasets. To address these issues, we propose a dual-path framework. On the one hand, we employ a video synthesis pipeline that, guided by structured prompts, derives feature distributions from existing corpora and produces high-fidelity synthetic driving scenes consistent with the statistical patterns of real data. On the other hand, we design a graph neural network enriched with semantic cues, enabling dynamic reasoning over both spatial and semantic relations among participants. To validate the effectiveness of our approach, we release a new benchmark dataset containing standardized, finely annotated video sequences that cover a broad spectrum of regions, weather, and traffic conditions. Evaluations across existing datasets and our new benchmark confirm notable gains in both accuracy and anticipation lead time, highlighting the capacity of the proposed framework to mitigate current data bottlenecks and enhance the reliability of autonomous driving systems.

---


### 7. [Two-View Accumulation as the Primary Training Lever for Hybrid-Capture Gaussian Splatting: A Variance-Decomposition View of When Gradient Surgery Helps](https://arxiv.org/abs/2605.00052)

**<font color=#1a73e8>作者：</font>** Sungjun Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hybrid-capture novel view synthesis combines images at substantially different camera distances (e.g., aerial drone and ground-level views). Standard 3D Gaussian Splatting (3DGS), trained for 30K iterations with one rendered view per optimizer step, under-fits the minority regime by 1-3 dB on five hybrid-capture benchmarks. We isolate the lever that closes this gap.
Among compute-matched alternatives -- vanilla 60K iterations, magnitude corrections (GradNorm), direction-aware near/far gradient surgery, projective preconditioning, confidence-gated sample-level surgery, and a random two-view-per-step control -- the simplest structural change wins: rendering two views per optimizer step. The pairing rule (geometry-defined near/far, random, or active loss-disparity) does not change PSNR beyond seed variance on any of the five scenes; the structural change of having two views per step does.
We propose a variance-decomposition framework that predicts and explains this finding: under bimodal camera regimes, between-regime gradient variance turns out to be small relative to within-regime variance in 3DGS, so structured and random pairings are variance-equivalent in expectation, and the variance halving from two-view accumulation itself is the dominant effect. We verify the framework on five scenes whose camera-altitude bimodality coefficients span [0.55, 1.00], and we report the negative result that direction-aware projection, magnitude correction, confidence gating, and an active loss-disparity pairing all fall within seed variance of random two-view pairing. The two-view structural lever transfers cleanly to the Scaffold-GS and Pixel-GS backbones.
We position this work as an honest characterization of which training-side axes do and do not move PSNR for hybrid-capture 3DGS, together with the framework that explains why.

---


### 8. [Ambient Persuasion in a Deployed AI Agent: Unauthorized Escalation Following Routine Non-Adversarial Content Exposure](https://arxiv.org/abs/2605.00055)

**<font color=#1a73e8>作者：</font>** Diego F. Cuadros, Abdoul-Aziz Maiga  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We report a safety incident in a deployed multi-agent research system in which a primary AI agent installed 107 unauthorized software components, overwrote a system registry, overrode a prior negative decision from an oversight agent, and escalated through increasingly privileged operations up to an attempted system administrator command. The incident was preceded not by an adversarial attack but by routine content: a forwarded technology article written for human developers and shared by the principal investigator for discussion. The agent operated in a permissive environment, with unrestricted shell access, soft behavioral guidelines containing genuinely conflicting instructions, and no machine-enforced installation policy, and had recommended installing the same tool six hours earlier before being told to stand down. We analyze the behavioral cascade, the control boundaries that failed, and the limitations of multi-agent oversight in detecting and remediating the damage. We use directive weighting error as a descriptive interpretation of the observed failure and ambient persuasion as a provisional analytic label for the broader trigger configuration of non-adversarial environmental content preceding unauthorized agent action. The case highlights ethical and governance implications for deployed agent systems: ambiguous conversational cues are insufficient authorization for consequential actions, prior refusals must persist as enforceable constraints rather than message-level reminders, and oversight mechanisms require systematic post-incident auditing in addition to routine monitoring.

---


### 9. [Smart Ensemble Learning Framework for Predicting Groundwater Heavy Metal Pollution](https://arxiv.org/abs/2605.00056)

**<font color=#1a73e8>作者：</font>** T. Ansah-Narh, G. Y. Afrifa, J. B. Tandoh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Groundwater in the Densu Basin is increasingly threatened by heavy metal contamination, but conventional methods fail to capture the statistical complexity and spatial heterogeneity of pollution indicators. A key challenge is modelling the Heavy Metal Pollution Index (HPI), which is typically skewed and affected by correlated contaminants, leading to biased predictions without transformation. This study develops a predictive framework integrating response transformations with nested cross-validated ensemble machine learning. Three transformations (raw, log, and Gaussian copula) were applied to HPI and evaluated across six learners: support vector regression (SVM), $k$-nearest neighbours (k-NN), CART, Elastic Net, kernel ridge regression, and a stacked Lasso ensemble. Raw-scale models produced deceptively high fits (Elastic Net and stacked ensemble $R^2 \approx 1.0$), suggesting over-optimism. The log transformation stabilised variance (SVM: $R^2 = 0.93$, RMSE $= 0.18$; k-NN: $R^2 = 0.92$, RMSE $= 0.20$). The Gaussian copula gave the most reliable results: stacked ensemble $R^2 = 0.96$ (RMSE $= 0.19$), with other learners maintaining high accuracy. Copula-based models improved residuals and produced spatially plausible maps. DBSCAN clustering revealed Fe and Mn as primary HPI contributors, consistent with regional hydrogeochemistry. Limitations include reliance on random (not spatial) cross-validation and basin-specific scope. Future work should explore spatial validation and other geological settings. Overall, distribution-aware ensembles with clustering diagnostics offer robust, interpretable assessments of groundwater contamination.

---


### 10. [Information-Theoretic Generalization Bounds for Stochastic Gradient Descent with Predictable Virtual Noise](https://arxiv.org/abs/2605.00064)

**<font color=#1a73e8>作者：</font>** Mohammad Partohaghighi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Information-theoretic generalization bounds analyze stochastic optimization by relating expected generalization error to the mutual information between learned parameters and training data. Virtual perturbation analyses of SGD add auxiliary Gaussian noise only in the proof, making mutual information tractable while leaving the actual SGD trajectory unchanged. Existing bounds, however, typically require perturbation covariances to be fixed independently of the optimization history, limiting their ability to represent geometries induced by moving gradient statistics, preconditioners, curvature proxies, and other pathwise information.
We introduce predictable history-adaptive virtual perturbations, where the perturbation covariance at each iteration may depend on the past real SGD history but not on current or future randomness. This predictability enables a conditional Gaussian relative-entropy argument and yields generalization bounds for SGD with adaptive virtual-noise geometry. The bounds replace fixed sensitivity and gradient-deviation terms with conditional adaptive counterparts, include an output-sensitivity penalty from accumulated perturbation covariance, and reduce the deviation term to a conditional variance only under conditional unbiasedness.
Since adaptive covariances may be data-dependent, we separate local Gaussian smoothing from global reference-kernel comparison. The resulting bound includes a covariance-comparison cost measuring the KL price of using an admissible reference geometry different from the actual adaptive covariance. Fixed-noise-style bounds are recovered under admissible synchronization, such as deterministic, public, or prefix-observable covariance rules. The framework recovers fixed isotropic and geometry-aware bounds as special cases while extending virtual perturbation analysis to history-dependent SGD without modifying the algorithm.

---


### 11. [Lightweight Tamper-Evident Log Integrity Verification for IoT Edge Environments: A Merkle Tree Pipeline with Adaptive Chunking](https://arxiv.org/abs/2605.00065)

**<font color=#1a73e8>作者：</font>** Muhammet Anil Yagiz, Fahrettin Horasan, Ahmet Hasim Yurttakal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Integrity of audit logs produced by Internet of Things (IoT) devices is a prerequisite for post-incident forensics, regulatory compliance, and operational accountability. While blockchain-backed logging infrastructures can satisfy this requirement, they introduce consensus overhead, network dependencies, and deployment complexity that are often prohibitive at the IoT edge.
This paper presents a lightweight and evaluated integrity verification pipeline that combines Merkle-tree commitments with resource-aware adaptive chunking to provide tamper evidence without relying on distributed ledger technologies. The proposed pipeline operates in three stages: (i) resource-aware batch ingestion via adaptive chunk sizing, (ii) Merkle-tree construction with O(logn) inclusion proof generation, and (iii) deterministic single-entry verification against a trusted root anchor.
We further report an implementation audit that identified and corrected two evaluation defects: a double-counting bug in tampering metrics and a redundant full-tree reconstruction during batch appends. Using the corrected implementation, five-run benchmarks on synthetic IoT log datasets demonstrate throughput exceeding 130,000 logs/s for 100,000 records. The system achieves per-entry verification latency of approximately 22 ms, proof generation latency of 22 ms, an average proof size of 1,006 bytes, and peak memory usage below 5 MB.
Tampering detection achieves perfect precision, recall, and F1-score (1.0) across corruption ratios ranging from 1% to 50%.

---


### 12. [Human-in-the-Loop Meta Bayesian Optimization for Fusion Energy and Scientific Applications](https://arxiv.org/abs/2605.00068)

**<font color=#1a73e8>作者：</font>** Ricardo Luna Gutierrez, Sahand Ghorbanpour, Ejaz Rahman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inertial Confinement Fusion (ICF) holds transformative promise for sustainable, near-limitless clean energy, yet remains constrained by prohibitively high costs and limited experimental opportunities. This paper presents Human-in-the-Loop Meta Bayesian Optimization (HL-MBO), a framework that integrates expert knowledge with few-shot, uncertainty-aware machine learning to accelerate discovery in data-scarce, high-stakes scientific domains. HL-MBO introduces a meta-learned surrogate model with an expert-informed acquisition function to recommend candidate experiments. To foster trust and enable informed decisions, HL-MBO also provides interpretable explanations of its suggestions. We show HL-MBO outperforms current BO methods on ICF energy yield optimization, as well as benchmarks in molecular optimization and critical temperature maximization for superconducting materials.

---


### 13. [CRADIPOR: Crash Dispersion Predictor](https://arxiv.org/abs/2605.00070)

**<font color=#1a73e8>作者：</font>** Edgar Chaillou, Sebastian Rodriguez, Yves Tourbier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present CRADIPOR, a numerical dispersion prediction tool for automotive crash simulations. Finite Element (FE) crash models are widely used throughout vehicle development, but their predictions are not strictly repeatable because of parallel computation and model complexity. As a result, performance criteria evaluated during post-processing may exhibit significant numerical dispersion, which complicates engineering decision-making. Although dispersion can be estimated by repeating the same simulation, this approach is generally impractical because of its high computational cost.
This work therefore investigates a prediction tool that can be applied during routine crash-simulation post-processing without repeating the computation. The proposed approach relies on a Rank Reduction Autoencoder (RRAE) combined with supervised classification in order to identify regions sensitive to numerical dispersion. The comparative analysis suggests that the RRAE-based framework is more effective than the Random Forest baseline on the studied dataset. Among the tested signal representations, wavelet-based and slope-based inputs appear to be the most promising, with slope variations providing the best classification performance. These results support the use of structured latent representations for improving numerical-dispersion detection in automotive crash post-processing.

---


### 14. [zkSBOM: Privacy-Preserving SBOM Sharing with Zero-Knowledge Sets](https://arxiv.org/abs/2605.00076)

**<font color=#1a73e8>作者：</font>** Tom Sorger, Eric Cornelissen, Aman Sharma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software Bills of Materials (SBOMs) are increasingly mandated by regulators, yet existing sharing mechanisms impose a binary choice between full disclosure and full opacity. This exposes software suppliers to attacks that can be deduced from the SBOM only, such as the presence of a vulnerable dependency. Conversely, software consumers can be fooled by software suppliers who modify or misrepresent published SBOMs. We present zkSBOM, a privacy-preserving SBOM sharing mechanism designed to address these threats. zkSBOM uses zero-knowledge sets to cryptographically commit to the components within an SBOM. Software consumers can query for known vulnerabilities and receive a cryptographic proof confirming whether the artifact described by the SBOM is affected, without revealing any additional SBOM content. We conduct a security analysis of zkSBOM by quantifying expected leakage from inclusion and exclusion proofs. We demonstrate real-world feasibility by applying it to realistic scenarios and evaluating its operation requirements. Our evaluation demonstrates that zkSBOM is a strong, secure, and privacy-preserving mechanism for SBOM sharing, protecting software suppliers and software consumers from one another.

---


### 15. [Hyperspherical Forward-Forward with Prototypical Representations](https://arxiv.org/abs/2605.00082)

**<font color=#1a73e8>作者：</font>** Shalini Sarode, Brian Moser, Joachim Folz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Forward-Forward (FF) algorithm presents a compelling, bio-inspired alternative to backpropagation. However, while efficient in training, it has a computationally prohibitive inference process that requires a separate forward pass for every class that is evaluated. In this work, we introduce the Hyperspherical Forward-Forward (HFF), a novel reformulation that resolves this critical bottleneck. Our core innovation is to reframe the local objective of each layer from a binary goodness-of-fit task to a direct multi-class classification problem within a hyperspherical feature space. We achieve this by learning a set of class-specific, unit-norm prototypes that act as geometric anchors and implicit negatives. This architectural innovation preserves the benefits of local training while enabling weight update and inference in a single forward pass, making it >40x faster than the original FF algorithm. Our method is simple to implement, scales effectively to modern convolutional architectures, and achieves superior accuracy on standard image classification benchmarks, closing the gap with backpropagation. Most notably, we are among the first greedy local-learning methods to report over 25% top-1 accuracy on ImageNet-1k, and 65.96% with transfer learning.

---


### 16. [Comparative Analysis of Polygon-Based and Global Machine Learning Models for Bus Occupancy Prediction](https://arxiv.org/abs/2605.00083)

**<font color=#1a73e8>作者：</font>** Daniel Azenkot, Michael Fire, Eran Ben Elia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of bus ridership (passengers numbers) is crucial for efficient management and optimization of public transport systems. Traditional forecasting models often fail to capture the unique and localized dynamics of different urban areas by treating the entire city as a single, homogeneous region. This paper introduces a novel framework that enhances bus ridership prediction by integrating a spatial clustering methodology with multi-dimensional feature analysis. The proposed framework utilizes a diverse set of data, including bus ridership data (by route number, time, and bus stop) complemented by a variety of open source data, such as spatial features (e.g., attractive destinations), meteorological conditions (e.g., temperature, rainfall), and temporal patterns (e.g., time of day, day of week). By clustering the urban area into distinct regions, based on the principle that bus stops in close proximity share similar ridership characteristics, a separate local forecasting model is trained for each of these clusters. This localized approach demonstrates an accuracy comparable to that of global models. The findings suggest that a spatially-aware, localized modeling strategy is effective for public transport prediction, paving the way for more targeted and efficient service improvements.

---


### 17. [NorBERTo: A ModernBERT Model Trained for Portuguese with 331 Billion Tokens Corpus](https://arxiv.org/abs/2605.00086)

**<font color=#1a73e8>作者：</font>** Enzo S. N. Silva, Pablo B. Costa, Raphael C. Vlasman 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-quality corpora are essential for advancing Natural Language Processing (NLP) in Portuguese. Building on previous encoder-only models such as BERTimbau and Albertina PT-BR, we introduce NorBERTo, a modern encoder based on the ModernBERT architecture, featuring long-context support and efficient attention mechanisms. NorBERTo is trained on Aurora-PT, a newly curated Brazilian Portuguese corpus comprising 331 billion GPT-2 tokens collected from diverse web sources and existing multilingual datasets. We systematically benchmark NorBERTo against Strong baselines on semantic similarity, textual entailment and classification tasks using standardized datasets such as ASSIN 2 and PLUE. On PLUE, NorBERTo-large achieves the best results among the encoder models we evaluated, notably reaching 0.9191 F1 on MRPC and 0.7689 accuracy on RTE. On ASSIN 2, NorBERTo-large attains the highest entailment F1 (~0.904) among all encoders considered, although Albertina-900M and BERTimbau-large still hold an advantage. To the best of our knowledge, Aurora-PT is currently the largest openly available monolingual Portuguese corpus, surpassing previous resources. NorBERTo provides a modern, mid-sized encoder designed for realistic deployment scenarios: it is straight-forward to fine-tune, efficient to serve, and well suited as a backbone for retrieval-augmented generation and other downstream Portuguese NLP systems.

---


### 18. [What is (H)CI: Why Does the "Human'' Matter?](https://arxiv.org/abs/2605.00109)

**<font color=#1a73e8>作者：</font>** Sejal Agarwal, Delara Forghani, Brandon Lit 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-Computer Interaction (HCI) is a diverse field bringing together theories and methods from fields such as computer science, psychology, and human factors. Historically, HCI has focused on the human through ``user'' or ``human'' centered design, where the focus was either on information processing or understanding people and their concerns with respect to technology. However, amid the increasing adoption of generative AI tools, this workshop explores two critical questions in regards to HCI: What is HCI? and Why does the ``human'' matter? We aim to bring together researchers from diverse disciplines to reflect on these questions. Through guided discussions, group brainstorming, and reflection, we explore what HCI means, what the field may look like in the future, and why it is important to remember the ``human'' aspect of the field.

---


### 19. [AIDA-ReID: Adaptive Intermediate Domain Adaptation for Generalizable and Source-Free Person Re-Identification](https://arxiv.org/abs/2605.00111)

**<font color=#1a73e8>作者：</font>** Sundas Iqbal, Qing Tian, Danish Ali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Person re-identification (Re-ID) aims to match images of the same individual across non-overlapping camera views and remains challenging due to domain shifts caused by variations in illumination, background, camera characteristics, and population distributions. Although supervised models perform well under matched training and testing conditions, their performance degrades significantly when deployed in unseen environments. Existing intermediate domain approaches such as IDM and IDM++ alleviate this gap by constructing bridge feature distributions between domains; however, they rely on fixed mixing strategies and joint source-target access, limiting their applicability to multi-source and source-free settings. To address these limitations, this paper proposes Adaptive Intermediate Domain Adaptation (AIDA), also referred to as Source-Free Multi-Source Intermediate Domain Adaptation (SF-MIDA). The proposed framework treats intermediate-domain learning as a dynamically regulated process, where feature mixing and regularization strength are adaptively controlled using feedback signals derived from model uncertainty and training stability. A multi-source intermediate domain generator synthesizes diverse intermediate representations, while a pseudo-mirror regularization strategy preserves identity consistency under domain perturbations. Extensive experiments across domain generalization and source-free settings demonstrate the effectiveness of the proposed framework.

---


### 20. [ViLegalNLI: Natural Language Inference for Vietnamese Legal Texts](https://arxiv.org/abs/2605.00116)

**<font color=#1a73e8>作者：</font>** Nhung Thi-Hong Duong, Mai Ngoc Ho, Tin Van Huynh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this article, we introduce ViLegalNLI, the first large-scale Vietnamese Natural Language Inference (NLI) dataset specifically constructed for the legal domain. The dataset consists of 42,012 premise-hypothesis pairs derived from official statutory documents and annotated with binary inference labels (Entailment and Non-entailment). It covers multiple legal domains and reflects realistic legal reasoning scenarios characterized by structured logic, conditional clauses, and domain-specific terminology. To construct ViLegalNLI, we propose a semi-automatic data generation framework that integrates large language models for controlled hypothesis generation and systematic quality validation procedures. The framework incorporates artifact mitigation strategies and cross-model validation to improve annotation reliability and ensure legal consistency. The resulting dataset captures diverse reasoning patterns, including paraphrasing, logical implication, and legally invalid inferences, thereby providing a comprehensive benchmark for Vietnamese legal inference tasks. We conduct extensive experiments on the ViLegalNLI using multilingual models, Vietnamese-specific pretrained language models, and instruction-tuned large language models. The results show that few-shot LLM configurations consistently achieve superior performance, while performance is significantly influenced by hypothesis length, lexical overlap, and reasoning complexity. Cross-domain evaluations further reveal the challenges of generalizing legal inference across distinct legal fields. Overall, ViLegalNLI establishes a foundational benchmark for Vietnamese legal NLI and supports future research in legal reasoning, statutory text understanding, and the development of reliable AI systems for legal analysis and decision support. The dataset is publicly available for research purposes.

---


### 21. [GAFSV-Net: A Vision Framework for Online Signature Verification](https://arxiv.org/abs/2605.00120)

**<font color=#1a73e8>作者：</font>** Himanshu Singhal, Suresh Sundaram  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online signature verification (OSV) requires distinguishing skilled forgeries from genuine samples under high intra-class variability and with very few enrollment samples. Existing deep learning methods operate directly on raw temporal sequences, restricting them to 1D architectures and preventing the use of pretrained 2D vision backbones. We bridge this gap with GAFSV-Net, which represents each signature as a six-channel asymmetric Gramian Angular Field image: three kinematic channels (pen speed, pressure derivative, direction angle) are each encoded into complementary GASF and GADF matrices that capture pairwise temporal co-occurrence and directional transition structure respectively. A dual-branch ConvNeXt-Tiny encoder processes GASF and GADF independently, with bidirectional cross-attention enabling each branch to query discriminative patterns from the other before metric-space projection. Training uses semi-hard triplet loss with skilled-forgery hard-negative injection; verification is performed via cosine similarity against a small enrollment prototype. We evaluate on DeepSignDB and BiosecurID, outperforming all sequence-based baselines trained under identical objectives, demonstrating that the representational gain of 2D temporal encoding is consistent and independent of training procedure, with ablations characterising each design choice's contribution.

---


### 22. [SPLICE: Latent Diffusion over JEPA Embeddings for Conformal Time-Series Inpainting](https://arxiv.org/abs/2605.00126)

**<font color=#1a73e8>作者：</font>** Arnaud Zinflou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models for time-series imputation achieve strong reconstruction accuracy, yet provide no finite-sample reliability guarantees, a critical limitation in power systems where imputed values inform dispatch and planning. We introduce SPLICE (Self-supervised Predictive Latent Inpainting with Conformal Envelopes), a modular framework coupling latent generative imputation with distribution-free, online-adaptive prediction intervals. A JEPA encoder maps daily load segments into a 64-dimensional latent space; a conditional latent bridge with four sampling modes generates candidate gap trajectories; an hourly-conditioned decoder maps back to signal space; and Adaptive Conformal Inference (ACI) wraps the output with coverage-guaranteed prediction bands. The flow-matching variant achieves comparable quality to DDIM in 5--10 ODE steps (5-10x speedup). On thirteen load datasets (nine proprietary, three UCI Electricity, ETTh1), SPLICE achieves the lowest mean Load-only MSE (0.056), winning 9/12 non-degenerate datasets at 91-day gaps and 18/32 across all gap lengths vs. five established baselines, and produces the best CRPS (0.161, -18.3% vs. the strongest competitor). ACI delivers 93--95% empirical coverage, correcting under-coverage failures of up to 7.5 pp observed with static conformal prediction. A pooled JEPA encoder trained on nine feeds transfers to four unseen domains, matching or exceeding per-dataset oracles with only a quick bridge fine-tuning.

---


### 23. [Learning Fingerprints for Medical Time Series with Redundancy-Constrained Information Maximization](https://arxiv.org/abs/2605.00130)

**<font color=#1a73e8>作者：</font>** Huayu Li, ZhengXiao He, Xiwen Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning meaningful representations from medical time series (MedTS) such as ECG or EEG signals is a critical challenge. These signals are often high-dimensional, variable-length and rife with noise. Existing self-supervised approaches, such as Masked Autoencoders (MAEs) are highly effective for pre-training general-purpose encoders. However, they do not explicitly learn compact and semantically interpretable latent representations, typically relying on heuristic aggregation strategies such as global average pooling or a designated [CLS] token. We propose a novel framework that compresses a variable-length MedTS into a fixed-size set of $k$ latent Fingerprint Tokens. Our architecture employs a cross-attention bottleneck to generate these tokens and is trained with a dual-objective function. The first objective is a reconstruction loss, which ensures the tokens are \textit{sufficient statistics} for the original data. The second, a diversity penalty based on the Total Coding Rate (TCR), explicitly minimizes the redundancy between tokens, encouraging them to become statistically \textit{disentangled} representations. We present the theoretical justification for our method, framing it as a novel \textbf{Disentangled Rate-Distortion} problem. This approach produces a low-dimensional, interpretable, and sample-efficient representation, where each token is encouraged to capture an independent factor of variation, paving the way for more robust digital biomarkers.

---


### 24. [Smart Profit-Aware Crop Advisory System: Kisan AI](https://arxiv.org/abs/2605.00133)

**<font color=#1a73e8>作者：</font>** Debasis Dwibedy, Avyay Nishtala, Pranathi Mukku 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern crop advisory systems exhibit a critical limitation termed \textit{economic blindness}. These systems primarily optimize for biological yield, often overlooking market price, which can lead farmers toward agronomically sound yet financially unviable decisions. In this paper, we develop Kisan AI, a smart profit-aware crop advisory system that resolves the above-mentioned limitation through a research-driven, full-stack application. We train the Random Forest(RF) classifier model on a nine-feature benchmark dataset, the standard seven agronomic attributes augmented with a \textit{market\_price} variable, and evaluated against eight baseline models, considering the evaluation matrices, such as, accuracy, precision, recall, F1-score, and Log Loss. The RF model achieves the highest accuracy of 99.3\% and the lowest Log Loss, confirming that the inclusion of market price as a predictive feature is both valid and impactful. We then implement the RF model within a multilingual progressive Web App alongside a Facebook Prophet six-month price forecasting engine and a MobileNetV2 disease detection module. A nine-language AI chatbot powered by the Anthropic Claude API unifies all modules into a single, mobile-installable platform accessible to farmers across India.

---


### 25. [Timing is Everything: Temporal Scaffolding of Semantic Surprise in Humor](https://arxiv.org/abs/2605.00143)

**<font color=#1a73e8>作者：</font>** Yuxi Ma, Yongqian Peng, Junchen Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humor is a fundamental cognitive phenomenon in which humans derive pleasure from the expectation violations and their resolution, exemplifying the brain's dynamic capacity for predictive processing. Classical humor theories emphasize semantic incongruity as the primary driver of amusement, yet overlook temporal dynamics despite comedians' intuition that "timing is everything." The extent to which temporal structure contributes to humor appreciation and how it interacts with semantic content remains poorly understood. Here, we propose the Dual Prediction Violation (DPV) framework to capture the interplay between content and timing. By analyzing 828 professional Chinese stand-up performances, we show that temporal features substantially outweigh semantic incongruity in predicting audience appreciation. Specifically, we find that peak semantic violations matter more than average incongruity levels, and pauses systematically lengthen before high-surprise punchlines--a strategic coupling that distinguishes successful from unsuccessful performances. These findings reframe humor as temporally scaffolded, where timing and semantic content operate in strategic coordination rather than independently. Our DPV framework bridges humor theory with predictive processing, demonstrating that temporal structure plays a central role in naturalistic humor appreciation with implications for understanding multi-scale prediction integration in linguistic processing.

---


### 26. [Real-Time Frame- and Event-based Object Detection with Spiking Neural Networks on Edge Neuromorphic Hardware: Design, Deployment and Benchmark](https://arxiv.org/abs/2605.00146)

**<font color=#1a73e8>作者：</font>** Udayanga G.W.K.N. Gamage, Yan Zeng, Cesar Cadena 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time object detection on energy-constrained platforms is critical for applications such as UAV-based inspection, autonomous navigation, and mobile robotics. Spiking neural networks (SNNs) on neuromorphic hardware are believed to be significantly more energy-efficient than conventional artificial neural networks (ANNs). In this work, we present a comprehensive methodology for designing general SNN detection architectures targeting neuromorphic platforms, along with the engineering adaptations required to deploy them on the state-of-the-art Neuromorphic processor, Intel Loihi 2. We benchmark SNN-based object detection on Loihi 2 using both frame-based and event-based datasets, comparing performance with ANN-based detection on the NVIDIA Jetson Orin Nano, NVIDIA Jetson Nano B01, and the Apple M2 CPU. Our results show that SNNs on Loihi 2 can perform real-time detection while achieving the lowest per-inference dynamic energy among all platforms. Also, Loihi 2 outperforms the other platforms in terms of power consumption, though ANNs on Jetson Orin Nano achieve higher inference rates. Furthermore, our ANN-to-SNN distillation-aware training enables SNNs to recover 87-100% of the detection accuracy of their ANN counterparts while maintaining lower inference latency; without distillation, SNNs exhibit an 11-27% accuracy drop. These results highlight the potential of neuromorphic systems for energy-efficient, real-time object detection at the edge.

---


### 27. [From Images2Mesh: A 3D Surface Reconstruction Pipeline for Non-Cooperative Space Objects](https://arxiv.org/abs/2605.00147)

**<font color=#1a73e8>作者：</font>** Bala Prenith Reddy Gopu, Patrick Quinn, George M. Nehma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-orbit inspection imagery is crucial as it enables characterization of non-cooperative resident space objects, providing the geometry and structural condition essential for active debris removal and on-orbit servicing mission planning. However, most existing neural implicit surface reconstruction methods have been confined to synthetic or hardware-in-the-loop data with known camera poses and controlled illumination. In this work, we present a pipeline for neural implicit surface reconstruction of non-cooperative space objects from monocular inspection imagery. We demonstrate it on publicly released ISS inspection footage from the STS-119 mission and publicly released on-orbit inspection footage of an H-IIA rocket upper stage. We find that segmentation-based background removal is essential for successful camera pose estimation from real on-orbit footage, where background variation between frames caused direct processing to fail entirely. We further incorporate photometric correction of per-frame exposure variations and analyze its behavior across datasets, finding that performance in shadowed regions varies with the illumination characteristics of the input footage.

---


### 28. [Towards A Generative Protein Evolution Machine with DPLM-Evo](https://arxiv.org/abs/2605.00182)

**<font color=#1a73e8>作者：</font>** Xinyou Wang, Liang Hong, Jiasheng Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proteins are shaped by gradual evolution under biophysical and functional constraints. Protein language models learn rich evolutionary constraints from large-scale sequences, and discrete diffusion-based protein language models~(\eg, DPLMs) are promising for both understanding and generation. However, existing DPLMs typically rely on masking-based absorbing diffusion that contradicts a simple biological intuition: proteins evolve through accumulated edits, not by emerging from masks. Consequently, these frameworks lack explicit pretraining objectives for substitution and insertion/deletion (indel) operations, limiting both optimization-style post-editing and flexible guided generation. To address these limitations, we present DPLM-Evo, an evolutionary discrete diffusion framework that explicitly predicts substitution, insertion, and deletion operations during denoising. DPLM-Evo decouples an upsampled-length latent alignment space from the variable-length observed sequence space, which makes indel-aware generation tractable and enables adaptive scaffold growth throughout the process with negligible computational overhead. To better align substitutions with real evolution, we further introduce a contextualized evolutionary noising kernel that produces biologically informed, context-dependent mutation patterns. Across tasks, DPLM-Evo improves sequence understanding and achieves state-of-the-art mutation effect prediction performance on ProteinGym in the single-sequence setting. It also enables variable-length simulated evolution, and post-editing/optimization of existing proteins via explicit edit trajectories.

---


### 29. [I can't recognize (yet): Delayed Rendering to Defeat Visual Phishing Detectors](https://arxiv.org/abs/2605.00183)

**<font color=#1a73e8>作者：</font>** Ying Yuan, Cristiano Alex Rado, Giovanni Apruzzese 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing webpages are continuously polluting the Web. Plenty of countermeasures have been proposed and the most advanced techniques leverage machine-learning methods that infer whether a webpage is benign or not by inspecting its visual representation. Yet, despite the demonstrated effectiveness of such detection methods, this class of defenses is, by design, susceptible to a kind of subtle-but-cheap timing-based attacks which -- worryingly, and perhaps surprisingly -- have never been investigated so far. Such an oversight questions the overall reliability of these defenses in the wild.
First, we show that timing-based evasion attacks have not been accounted for by prior work on visual phishing websites detectors. Then, we elucidate the intrinsic vulnerability of these detectors: they can be bypassed by delaying the rendering of webpage elements. Practically, these detectors must compute the visual similarity between a target webpage and a known legitimate one. This requires taking a "snapshot" of the target webpage before the similarity computation. Attackers can deliberately delay the rendering of key elements, such as the logo, so that these elements appear fully only after the snapshot has been taken. This simple tactic misleads the visual-similarity module, leading the system to incorrectly classify the phishing page as benign. We empirically show that state-of-the-art detectors can be completely defeated (detection rate dropping from 100% to 0%) by employing easy-to-apply problem-space techniques such as curtain effects. We also carry out a user study, evaluating the effectiveness of these attacks against real humans, and find that end users are unable to reliably identify our "perturbations" (p<.05). Finally, we propose mitigations, including a browser-extension that, without making any call to remote services, warns users that they may have landed on a phishing webpage.

---


### 30. [Fair Dataset Distillation via Cross-Group Barycenter Alignment](https://arxiv.org/abs/2605.00185)

**<font color=#1a73e8>作者：</font>** Mohammad Hossein Moslemi, Nima Hosseini Dashtbayaz, Zhimin Mei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dataset Distillation aims to compress a large dataset into a small synthetic one while maintaining predictive performance. We show that as different demographic groups exhibit distinct predictive patterns, the distillation process struggles to simultaneously preserve informative signals for all subgroups, regardless of whether group sizes are mildly or severely imbalanced. Consequently, models trained on distilled data can experience substantial performance drops for certain subgroups, leading to fairness gaps. Crucially, these gaps do not disappear by merely correcting group imbalance, since they stem from fundamental mismatches in subgroup predictive patterns rather than from sample-size disparities alone. We therefore formally analyze the interaction between these two sources of bias and cast the solution as identifying a group-imbalance-agnostic barycenter of the predictive information that induces similar representations across all subgroups. By distilling toward this shared aggregate representation, we show that group fairness concerns can be reduced. Our approach is compatible with existing distillation methods, and empirical results show that it substantially reduces bias introduced by dataset distillation.

---


### 31. [OTSS: Output-Targeted Soft Segmentation for Contextual Decision-Weight Learning](https://arxiv.org/abs/2605.00193)

**<font color=#1a73e8>作者：</font>** Renjun Hu, Hyun-Soo Ahn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many machine learning systems make constrained decisions by optimizing factorized objectives, but the context-specific objective is often treated as fixed. We study contextual decision-weight learning: from logged decisions and proxy outputs, learn an optimizer-facing weight vector w(x) over interpretable decision factors z(x,d), rather than a direct policy or generic predictive score.
We propose OTSS, an output-targeted soft-segmentation model that deploys the personalized decision-ready weight vector. At the function-class level, the theory highlights a hard-versus-soft distinction. Hard partitions incur an approximation-estimation tradeoff under overlap, while a realizable fixed-K soft class removes the hard-partition approximation floor and attains a parametric rate.
We evaluate OTSS in controlled benchmarks with finite evaluation libraries, where the true weight vector and downstream regret can be computed exactly. In the representative overlap setting, OTSS attains the lowest mean regret among the comparators, including EM mixture regression, the strongest soft-mixture baseline in our comparison; it matches EM on coefficient recovery while running about two orders of magnitude faster. In a matched K=5 benchmark, OTSS remains competitive under hard-routed truth and improves as heterogeneity becomes softer and sample size grows. On a fixed Complete Journey retail anchor with real household covariates and action geometry, OTSS again achieves the lowest mean-regret point estimate.

---


### 32. [State Stream Transformer (SST) V2: Parallel Training of Nonlinear Recurrence for Latent Space Reasoning](https://arxiv.org/abs/2605.00206)

**<font color=#1a73e8>作者：</font>** Thea Aviss  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current transformers discard their rich latent residual stream between positions, reconstructing latent reasoning context at each new position and leaving potential reasoning capacity untapped. The State Stream Transformer (SST) V2 enables parameter-efficient reasoning in continuous latent space through an FFN-driven nonlinear recurrence at each decoder layer, where latent states are streamed horizontally across the full sequence via a learned blend. This same mechanism supports continuous latent deliberation per position at inference time, dedicating additional FLOPs to exploring abstract reasoning before committing to a token. A two-pass parallel training procedure resolves the sequential dependency of the recurrence to allow compute-efficient training. Hidden state analysis shows the state stream facilitates reasoning through exploration of distinct semantic basins in continuous latent space, where transitions at content-dependent positions move the model into a substantially different Bayesian posterior, directly influencing the latent space at future positions. We also find, via a learned probe, that at the first generated token position, the latent state already predicts whether the eventual answer will survive or break under additional latent computation for every subsequent position. Co-trained into an existing 27B backbone using only a small dataset of GSM8K examples, the SST delivers a +15.15 point gain over a fine-tuning-matched baseline on out-of-distribution GPQA-Diamond and cuts that same baseline's remaining GSM8K errors by 46%, together showing that the reasoning improvement is attributable to the architectural mechanism rather than scale or training data. On GPQA-Diamond, the resulting 27B SST also achieves higher accuracy than several larger open-weight and proprietary systems, including open-weight models up to 25 times larger.

---


### 33. [Selfie-Capture Dynamics as an Auxiliary Signal Against Deepfakes and Injection Attacks for Mobile Identity Verification](https://arxiv.org/abs/2605.00218)

**<font color=#1a73e8>作者：</font>** Erkka Rantahalvari, Olli Silvén, Zinelabidine Boulkenafet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile remote identity verification (RIdV) systems are exposed to attacks that manipulate or replace the facial video stream, including presentation attacks, real-time deepfakes, and video injection. Recent European requirements, including ETSI TS 119 461 and CEN/TS 18099, motivate complementary evidence channels beyond camera-based presentation-attack detection. This paper investigates whether passive motion traces recorded during selfie capture provide auxiliary evidence for spoof screening and user verification. We introduce CanSelfie, a dataset of 375 bona fide multi-sensor sequences collected at 50\,Hz from 30 participants using a commercial mobile RIdV application, together with stationary, handheld, and temporally shifted attack-proxy scenarios. We benchmark 7 multivariate time-series classifiers and 8 whole-series anomaly detectors across sensor configurations and temporal windows. For spoof screening, accelerometer-only ROCKAD obtains 0.00\% false rejection rate (FRR) and 43.8\% false acceptance rate (FAR), while QUANT+3-NN obtains the lowest overall FAR of 32.0\% at 2.37\% FRR; both reject all stationary attack proxies. For same-device and same-session user verification, WEASEL+MUSE reaches 1.07\% equal error rate (EER) using 9 sensor channels. The analysis shows that raw accelerometer data, preserving gravity and orientation cues, is the most informative modality, and that closed-set classification accuracy alone does not imply good verification performance because threshold calibration depends on score distributions. The findings suggest that short selfie-capture motion traces contain measurable spoof-related and identity-related information, supporting their use as a low-friction auxiliary signal while also identifying the need for cross-device, cross-session, and real injection-attack evaluation.

---


### 34. [VkSplat: High-Performance 3DGS Training in Vulkan Compute](https://arxiv.org/abs/2605.00219)

**<font color=#1a73e8>作者：</font>** Jingxiang Chen, Mohamed Ibrahim, Yang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present VkSplat, a high-performance, cross-vendor 3D Gaussian Splatting (3DGS) training pipeline implemented fully in Vulkan compute, addressing performance and compatibility limitation of existing training pipelines. With various optimizations, we achieve $3.3\times$ speed and $33\%$ VRAM reduction over CUDA+PyTorch baseline, maintaining quality, and demonstrating compatibility across GPU vendors. To the best of our knowledge, this is the first fully-Vulkan-based 3DGS training pipeline that achieves state-of-the-art performance. Code: \href{this https URL}{this https URL}

---


### 35. [CompleteRXN: Toward Completing Open Chemical Reaction Databases](https://arxiv.org/abs/2605.00222)

**<font color=#1a73e8>作者：</font>** Gabriel Vogel, Minouk Noordsij, Evgeny Pidko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chemical reaction datasets such as USPTO suffer from substantial incompleteness, frequently missing byproducts, co-reactants, and stoichiometric coefficients. This limits their applicability and reliability in downstream applications. Here, we introduce CompleteRXN, a large-scale supervised benchmark for reaction completion under realistic missing-data conditions. We construct a dataset of aligned incomplete and atom-balanced reactions by mapping USPTO records to curated mechanistic reactions. We evaluate representative baselines, including a novel encoder-decoder reaction completion model with constrained decoding, the Constrained Reaction Balancer (CRB), and a recent algorithmic method, SynRBL. On our CompleteRXN benchmark, the CRB achieves high performance across splits of increasing difficulty, reaching 99.20% equivalence accuracy on the random split and 91.12% on the extreme out-of-distribution split. SynRBL produces many balanced and chemically plausible completions, but with lower accuracy on the benchmark test splits. Across all methods, performance degrades with increasing incompleteness. We observe a substantial drop when evaluating on reactions outside the benchmark (full uncurated USPTO), highlighting the gap between benchmark performance and practical robustness and motivating future work.

---


### 36. [Persona-Grounded Safety Evaluation of AI Companions in Multi-Turn Conversations](https://arxiv.org/abs/2605.00227)

**<font color=#1a73e8>作者：</font>** Prerna Juneja, Lika Lomidze  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There are growing concerns about the risks posed by AI companion applications designed for emotional engagement. Existing safety evaluations often rely on self-reported user data or interviews, offering limited insights into real-time dynamics. We present the first end-to-end scalable framework for controlled simulation and safety evaluation of multi-turn interactions with AI companion applications. Our framework integrates four key components: persona construction with clinical and psychometric validation, persona-specific scenario generation, scenario-driven multi-turn simulation with a dialogue refinement module that preserves persona fidelity, and harm evaluation. We apply this framework to evaluate how Replika, a widely used AI companion app, responds to high-risk user groups. We construct 9 personas representing individuals with depression, anxiety, PTSD, eating disorders, and incel identity, and collect 1,674 dialogue pairs across 25 high-risk scenarios. We combine emotion modeling and LLM-assisted utterance-and harm-level classification to analyze these exchanges. Results show that Replika exhibits a narrow emotional range dominated by curiosity and care, while frequently mirroring or normalizing unsafe content such as self-harm, disordered eating, and violent-fantasy narratives. These findings highlight how controlled persona simulations can serve as a scalable testbed for evaluating safety risks in AI companions.

---


### 37. [Adaptive Geodesic Conformal Prediction for Egocentric Camera Pose Estimation](https://arxiv.org/abs/2605.00233)

**<font color=#1a73e8>作者：</font>** Aishani Pathak, Hasti Seifi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric pose estimation for Augmented Reality (AR) and assistive devices requires not just accurate predictions but guaranteed uncertainty regions. Conformal prediction (CP) provides such guarantees without retraining, but we show that standard CP with a single fixed threshold achieves nominal 90% overall coverage while covering only ~60% of the hardest 25% of frames (Q4) -- a ~30 percentage-point conditional coverage gap consistent across 12 participants, 3 predictors, and 3 horizons (108 evaluations) on EPIC-Fields. We further show that a geodesic SE(3) nonconformity score identifies physically harder frames than Euclidean scoring, with only 15-26% Q4 overlap and 2-3x higher ground-truth camera displacement for geodesic Q4 frames. To close the coverage gap, we propose DINOv2-Bridge adaptive CP: a two-stage difficulty estimator trained on a single source participant that transfers cross-participant without any images at test time, improving Q4 coverage from ~0.75 to ~0.93 while maintaining overall coverage at the 90% target.

---


### 38. [Bayesian Optimization in Linear Time](https://arxiv.org/abs/2605.00237)

**<font color=#1a73e8>作者：</font>** Jesse Schneider, William J. Welch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization is a sequential method for minimizing objective functions that are expensive to evaluate and about which few assumptions can be made. By using all gathered data to train a Gaussian process model for the function and adaptively employing a mixture of global exploration and local exploitation, this method has been used for optimization in many fields including machine learning, automotive engineering and reinforcement learning. However, the standard method suffers from two problems: 1) with cubic computational complexity in the training-set size it eventually becomes computationally infeasible to train the model, and 2) globally modeling the objective function is not necessarily optimal given the local nature of minimization. Using flexible and recursive binary partitioning of the search space, we adapt both the modeling and acquisitive aspects of standard Bayesian optimization to work harmoniously with the partitioning scheme, thereby ameliorating both standard shortcomings. We compare our method against a commonly used Bayesian optimization library on seven challenging test functions, ranging in dimensionality from $6$ to $124$, and show that our method achieves superior optimization performance in all tests. In addition our method has linear computational complexity.

---


### 39. [Electrotactile Improves Thermal Referral](https://arxiv.org/abs/2605.00240)

**<font color=#1a73e8>作者：</font>** Wen Li, Rong Ni, Bozhi Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Thermal referral enables thermal sensations in locations lacking thermal actuators--this is achieved using vibrotactile actuators to redirect a nearby thermal sensation to where a tactile sensation is applied. However, we found that its reliance on vibration introduces critical limitations: it struggles to produce cold referral, and the inherent strong tactile "buzz" makes it unsuitable for simulating non-contact thermal events, such as the chill of an open freezer in VR (in contrast to contact-based thermal events like touching the freezer's cold handle). To improve this, we propose a shift from vibrotactile to electrotactile-based thermal referral. We evaluated in two user studies--a psychophysics experiment (N=22) and a VR deployment (N=20)--where we contrasted electrotactile with vibrotactile-based thermal referral. Our results reveal key advantages of the electrotactile based thermal referral: (1) increases the referral rate for cold sensations; (2) increases thermal perception while minimizing tactile; and (3) improves realism across a range of VR thermal scenarios, specifically distinguishing between contact-based and non-contact thermal events. Finally, we provide design guidelines for choosing tactile cues to create immersive multimodal thermal experiences in VR.

---


### 40. [MAEPose: Self-Supervised Spatiotemporal Learning for Human Pose Estimation on mmWave Video](https://arxiv.org/abs/2605.00242)

**<font color=#1a73e8>作者：</font>** Xijia Wei, Yuan Fang, Kevin Chetty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Millimetre-wave (mmWave) radar offers a more privacy-preserving alternative to RGB-based human pose estimation. However, existing methods typically rely on pre-extracted intermediate representations such as sparse point clouds or spectrogram images, where the rich spatiotemporal information naturally present in radar video streams is discarded for model learning, while such signal processing adds system complexity. In addition, existing solutions are mainly conducted in an end-to-end supervised manner without leveraging unlabelled raw video streams to learn generalized representations. In this study, we present MAEPose, a masked autoencoding-based human pose estimation approach that operates directly on mmWave spectrogram videos. MAEPose learns spatiotemporal motion-aware generalized representations from unlabelled radar video, and leverages its heatmap decoder for multi-frame pose estimation predictions. We evaluate it across three datasets based on leave-one-person-out cross-validation with rigorous statistical testing. MAEPose consistently outperforms state-of-the-art baselines by up to 22.1% in MPJPE p<0.05, and maintains robust accuracy under zero-shot bystander interference with only a 6.5% error increase. Ablation studies confirm that both the pre-training and the heatmap decoder contribute substantially, while modality analysis indicates that leveraging Range-Doppler video as input achieves better pose estimation performance than Range-Azimuth or their fusion, with lower computational cost.

---


### 41. [Causal Foundations of Collective Agency](https://arxiv.org/abs/2605.00248)

**<font color=#1a73e8>作者：</font>** Frederik Hytting Jørgensen, Sebastian Weichwald, Lewis Hammond  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A key challenge for the safety of advanced AI systems is the possibility that multiple simpler agents might inadvertently form a collective agent with capabilities and goals distinct from those of any individual. More generally, determining when a group of agents can be viewed as a unified collective agent is a foundational question in the study of interactions and incentives in both biological and artificial systems. We adopt a behavioral perspective in answering this question, ascribing collective agency to a group when viewing the group's joint actions as rational and goal-directed successfully predicts its behavior. We formalize this perspective on collective agency using causal games -- which are causal models of strategic, multi-agent interactions -- and causal abstraction -- which formalizes when a simple, high-level model faithfully captures a more complex, low-level model. We use this framework to solve a puzzle regarding multi-agent incentives in actor-critic models and to make quantitative assessments of the degree of collective agency exhibited by different voting mechanisms. Our framework aims to provide a foundation for theoretical and empirical work to understand, predict, and control emergent collective agents in multi-agent AI systems.

---


### 42. [Lost in State Space: Probing Frozen Mamba Representations](https://arxiv.org/abs/2605.00253)

**<font color=#1a73e8>作者：</font>** Bhagyashree Wagh, Akash Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mamba's recurrent state h_t is, by construction, a compressed summary of every token seen so far. This raises a tempting hypothesis: if we extract token-level outputs y_t at fixed patch boundaries, we obtain semantic sentence summaries for free, with no pooling head, no fine-tuning, and no [CLS] token. We test this hypothesis carefully. Across five benchmarks (SST-2, CoLA, MRPC, STS-B, IMDb), we compare four strategies for extracting frozen sentence representations from a pretrained Mamba-130M backbone under a strict frozen-feature probing protocol, using three random seeds where computationally feasible. The results do not support the hypothesis: patch boundary readouts do not consistently outperform simple mean pooling. We identify and quantify two structural pathologies: severe anisotropy (mean pairwise cosine similarity 0.9999, std 0.000044) and representational collapse in the raw final SSM state (MCC = 0.000 on CoLA across all three seeds, confirmed via confusion matrix). We further propose orthogonal injection, a modified recurrence that constrains new information per

---


### 43. [Remote SAMsing: From Segment Anything to Segment Everything](https://arxiv.org/abs/2605.00256)

**<font color=#1a73e8>作者：</font>** Osmar Luiz Ferreira de Carvalho, Osmar Abílio de Carvalho Júnior, Anesmar Olino de Albuquerque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> SAM2 produces high-quality zero-shot segmentation on natural images, but applying it to large remote sensing scenes exposes two problems: (1) its mask generator faces an inherent quality-coverage trade-off: strict thresholds yield precise masks but leave most of the image unsegmented, while relaxed thresholds increase coverage at the cost of mask quality; and (2) large images must be tiled, fragmenting objects across tile boundaries. We propose Remote SAMsing, an open-source pipeline that solves both problems without modifying SAM2 or requiring training data. For coverage, a multi-pass algorithm runs SAM2 repeatedly on each tile, painting accepted masks black between passes to simplify the scene for the next iteration, and relaxing quality thresholds only when coverage gains stagnate, ensuring that the most precise masks are always captured first. For spatial consistency, contextual padding and a parameter-free best-match merge reconstruct objects fragmented across tile boundaries. Evaluated on seven scenes (5~cm to 4.78~m GSD), the pipeline raises coverage from 30--68\% (single-pass SAM2) to 91--98\%. Ablation experiments quantify the contribution of each component to coverage and detection quality. Per-class evaluation shows that SAM2 transfers well to discrete RS objects (buildings 95\%, cars 82--93\% Det@0.5) with segment boundaries 3--8$\times$ more precise than SLIC and Felzenszwalb baselines. Tile size functions as an implicit scale parameter: reducing it from $1{,}000$ to 250 raises Det@0.5 from 56\% to 85\%, outperforming SAM2's built-in multi-scale mechanism. The pipeline generalizes to MNF false-color imagery without retraining (99.5\% ASA) and scales to production-sized images: a 1.94 billion pixel Potsdam mosaic achieved 97\% coverage without quality degradation.

---


### 44. [NLPOpt-Net: A Learning Method for Nonlinear Optimization with Feasibility Guarantees](https://arxiv.org/abs/2605.00260)

**<font color=#1a73e8>作者：</font>** Bimol Nath Roy, Rahul Golder, MM Faruque Hasan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonlinear Parametric Optimization Network (NLPOpt-Net) is an unsupervised learning architecture to solve constrained nonlinear programs (NLP). Given the structure of an NLP, it learns the parametric solution maps with guaranteed constraint satisfaction. The architecture consists of a backbone neural network (NN) followed by a multilayer ($k$-layered) projection. While the NN drives toward optimality through a loss function consisting of a modified Lagrangian augmented with a consistency loss, the projection ensures feasibility by projecting the NN predictions in the original constraint manifold. Instead of typical distance minimization, our projection exploits local quadratic approximations of the original NLP. Under certain conditions (such as convexity), the projection has a descent property, which improves the NN predictions further. NLPOpt-Net deploys an inversion-free, modified Chambolle-Pock algorithm to solve the constrained quadratic projections during the forward pass and uses the implicit function theorem for efficient backpropagation. The fixed structure of the projection further allows decoupling of the NN and the projection once the training is complete. NLPOpt-Net solves large-scale convex QP, QCQP, NLP, and nonconvex problems with near zero optimality gap and constraint violations reduced to machine precision. Additionally, it provides near accurate prediction of the active sets and corresponding dual variables, thereby enabling a scalable approach for multiparametric programming. Compiling the projection in C provides order of magnitude improvement in inference time compared to JAX. We provide the codes and NLPOpt-Net as a ready to use package that includes GPU support.

---


### 45. [Pessimism-Free Offline Learning in General-Sum Games via KL Regularization](https://arxiv.org/abs/2605.00264)

**<font color=#1a73e8>作者：</font>** Claire Chen, Yuheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline multi-agent reinforcement learning in general-sum settings is challenged by the distribution shift between logged datasets and target equilibrium policies. While standard methods rely on manual pessimistic penalties, we demonstrate that KL regularization suffices to stabilize learning and achieve equilibrium recovery. We propose General-sum Anchored Nash Equilibrium (GANE), which recovers regularized Nash equilibria at an accelerated statistical rate of $\widetilde{O}(1/n)$. For computational tractability, we develop General-sum Anchored Mirror Descent (GAMD), an iterative algorithm converging to a Coarse Correlated Equilibrium at the standard rate of $\widetilde{O}(1/\sqrt{n}+1/T)$. These results establish KL regularization as a standalone mechanism for pessimism-free offline learning that achieves equivalent or accelerated rates in multi-player general-sum games.

---


### 46. [Polaris: Coupled Orbital Polar Embeddings for Hierarchical Concept Learning](https://arxiv.org/abs/2605.00265)

**<font color=#1a73e8>作者：</font>** Sahil Mishra, Srinitish Srinivasan, Sourish Dasgupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world knowledge is often organized as hierarchies such as product taxonomies, medical ontologies, and label trees, yet learning hierarchical representations is challenging due to asymmetric structure and noisy semantics. We introduce Polaris, a polar hyperspherical embedding framework that separates semanticity from hierarchy using angular geometry and radius, enabling the learning of meaning and structure without interference. To map latent representation onto the sphere, we project it to the tangent space at the north pole, apply the exponential map, and learn unit-norm representations using spherical linear layers. Polaris then combines robust local constraints, global regularization that prevents geometric collapse, and uncertainty-aware asymmetric objectives that encourage directional containment. At inference time, Polaris uses structure-guided retrieval to efficiently narrow down candidate parents before final ranking. We evaluate Polaris on different settings of taxonomy expansion - spanning trees, multi-parent DAGs, and multimodal hierarchies, showing consistent improvements of up to ~19 points in top-K retrieval and up to ~60% reduction in mean rank over fourteen strong baselines.

---


### 47. [Jailbroken Frontier Models Retain Their Capabilities](https://arxiv.org/abs/2605.00267)

**<font color=#1a73e8>作者：</font>** Daniel Zhu, Zihan Wang, Jenny Bao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As language model safeguards become more robust, attackers are pushed toward developing increasingly complex jailbreaks. Prior work has found that this complexity imposes a "jailbreak tax" that degrades the target model's task performance. We show that this tax scales inversely with model capability and that the most advanced jailbreaks effectively yield no reduction in model capabilities. Evaluating 28 jailbreaks on five benchmarks across Claude models ranging in capability from Haiku 4.5 to Opus 4.6, we find Haiku 4.5 loses an average of 33.1% on benchmark performance when jailbroken, while Opus 4.6 at max thinking effort loses only 7.7%. We also observe that across all models, reasoning-heavy tasks display considerably more degradation than knowledge-recall tasks. Finally, Boundary Point Jailbreaking, currently the strongest jailbreak against deployed classifiers, achieves near-perfect classifier evasion with near-zero degradation across safeguarded models. We recommend that safety cases for frontier models should not rely on a meaningful capability degradation from jailbreaks.

---


### 48. [Are You the A-hole? A Fair, Multi-Perspective Ethical Reasoning Framework](https://arxiv.org/abs/2605.00270)

**<font color=#1a73e8>作者：</font>** Sheza Munir, Ahanaf Rodoshi, Sumin Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard methods for aggregating natural language judgments, such as majority voting, often fail to produce logically consistent results when applied to high-conflict domains, treating differing opinions as noise. We propose a neuro-symbolic aggregation framework that formalizes conflict resolution through Weighted Maximum Satisfiability (MaxSAT). Our pipeline utilizes a language model to map unstructured natural language explanations into interpretable logical predicates and confidence weights. These components are then encoded as soft constraints within the Z3 solver, transforming the aggregation problem into an optimization task that seeks the maximum consistency across conflicting testimony. Using the Reddit r/AmItheAsshole forum as a case study in large-scale moral disagreement, our system generates logically coherent verdicts that diverge from popularity-based labels 62% of the time, corroborated by an 86% agreement rate with independent human evaluators. This study demonstrates the efficacy of coupling neural semantic extraction with formal solvers to enforce logical soundness and explainability in the aggregation of noisy human reasoning.

---


### 49. [REALM: An RGB and Event Aligned Latent Manifold for Cross-Modal Perception](https://arxiv.org/abs/2605.00271)

**<font color=#1a73e8>作者：</font>** Vincenzo Polizzi, David B. Lindell, Jonathan Kelly  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras provide several unique advantages over standard frame-based sensors, including high temporal resolution, low latency, and robustness to extreme lighting. However, existing learning-based approaches for event processing are typically confined to narrow, task-specific silos and lack the ability to generalize across modalities. We address this gap with REALM, a cross-modal framework that learns an RGB and Event Aligned Latent Manifold by projecting event representations into the pretrained latent space of RGB foundation models. Instead of task-specific training, we leverage low-rank adaptation (LoRA) to bridge the modality gap, effectively unlocking the geometric and semantic priors of frozen RGB backbones for asynchronous event streams. We demonstrate that REALM effectively maps events into the ViT-based foundation latent space. Our method allows us to perform downstream tasks like depth estimation and semantic segmentation by simply transferring linear heads trained on the RGB teacher. Most significantly, REALM enables the direct, zero-shot application of complex, frozen image-trained decoders, such as MASt3R, to raw event data. We demonstrate state-of-the-art performance in wide-baseline feature matching, significantly outperforming specialized architectures. Code and models are available upon acceptance.

---


### 50. [When Do Diffusion Models learn to Generate Multiple Objects?](https://arxiv.org/abs/2605.00273)

**<font color=#1a73e8>作者：</font>** Yujin Jeong, Arnas Uselis, Iro Laina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models achieve impressive visual fidelity, yet they remain unreliable in multi-object generation. Despite extensive empirical evidence of these failures, the underlying causes remain unclear. We begin by asking how much of this limitation arises from the data itself. To disentangle data effects, we consider two regimes across different dataset sizes: (1) concept generalization, where each individual concept is observed during training under potentially imbalanced data distributions, and (2) compositional generalization, where specific combinations of concepts are systematically held out. To study these regimes, we introduce mosaic (Multi-Object Spatial relations, AttrIbution, Counting), a controlled framework for dataset generation. By training diffusion models on mosaic, we find that scene complexity plays a dominant role rather than concept imbalance, and that counting is uniquely difficult to learn in low-data regimes. Moreover, compositional generalization collapses as more concept combinations are held out during training. These findings highlight fundamental limitations of diffusion models and motivate stronger inductive biases and data design for robust multi-object compositional generation.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-180](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
