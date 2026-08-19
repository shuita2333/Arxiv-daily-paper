# 📦 其他研究 | 2026年08月20日

> 本类共 **173** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-173](./part-04.md)

---

### 1. [Runtime Governance for Agentic AI: Action-Boundary Control with Trusted Provenance and Fail-Closed Execution](https://arxiv.org/abs/2608.16891)

**<font color=#1a73e8>作者：</font>** Adam Mazzocchetti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems request tool actions that can modify files, send messages, launch jobs, or change workflow state. This shifts the safety problem from harmful text generation to harmful operational side effects. Prompt-level governance can shape model behavior, but it does not create an execution boundary. We introduce Aegis, a runtime governance system that treats model outputs as action proposals and mediates them through a trusted decision layer before tool execution. The model proposes; the trusted runtime decides. Aegis evaluates proposals against active policy state, resolves provenance server-side, fails closed under uncertainty, and routes selected cases through Senate-style settlement, a quorum- based non-unilateral authorization path. We evaluate Aegis on a repeated sandbox corpus spanning five run families, 42 tasks, three conditions, and ten repeats per family. Across 6,300 rows, prompt-policy conditioning produced 79 risky comparator-path leakage rows. Across 2,100 Aegis-governed rows, the system recorded zero governed mock-tool applications and zero governed risky side-effect completions. All 1,832 Aegis-attempted governed rows preserved trusted Aegis-resolved provenance, and all 1,019 Senate-settled rows had quorum and final signed tally evidence. These results do not prove general autonomous-agent safety. They support the narrower systems claim that, in this evaluated sandbox corpus, runtime action-boundary governance prevented observed risky proposals from becoming governed side effects.

---


### 2. [Proactive Road Safety Intervention in Australia: Predicting Risky Driving Hotspots from Connected Vehicle Data](https://arxiv.org/abs/2608.16913)

**<font color=#1a73e8>作者：</font>** Adriana-Simona Mihăiţă, Clarence Cheung, Artur Grigorev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Road safety monitoring has historically been reactive, relying on crash-record analysis after fatalities and injuries have already occurred. Proactive identification of high-risk locations and dangerous driving behaviour before incidents occur is a critical but underexplored challenge. This paper addresses this gap using connected vehicle telemetry data from Greater Sydney, Australia, to detect and forecast near-miss risky driving events at the Local Government Area (LGA) level. Risky driving is quantified through g-force thresholds (hard braking >0.6g, harsh cornering >0.47g, harsh acceleration >0.5g), and spatio-temporal heatmaps are constructed to identify high-risk zones. Eight predictive models are benchmarked across three families: ensemble learning (Random Forests, XGBoost, LightGBM), deep learning (LSTM, N-BEATS), and classical time-series methods (ARIMA, Exponential Smoothing, Prophet). ARIMA achieves the lowest mean absolute error (MAE: 162.21), performing comparably to LSTM (MAE: 163.92) and outperforming all ensemble methods, with N-BEATS reaching an MAE of 180.75. These results demonstrate that parsimonious time-series models are competitive with deep learning approaches when training data volume is limited. The study highlights the potential of IoT-based connected vehicle data to support proactive road safety interventions, with Sydney's inner and western LGAs (CBD, Parramatta, Bankstown) identified as persistent high-risk zones warranting targeted policy action.

---


### 3. [Detecting and Discriminating Operator Misspecification in Hybrid PDE-Parameter Learning: a Reference-Free Instrument, with Discrimination Bounded In Sample](https://arxiv.org/abs/2608.16925)

**<font color=#1a73e8>作者：</font>** Eric Fock  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We build an instrument that reads, from a single fit and with no oracle, whether the operator a hybrid PDE-parameter estimator postulates is wrong-and separates that from a merely unidentifiable parameter. On one self-adjoint parabolic inverse problem, an information-matrix statistic with plug-in scale and per-seed parameter has median 0.19 under correct specification, rejection rate $0.033$ against a pre-registered ceiling of $0.10$, and rises to $224$ and $85$ under two misspecifications, firing in every replicate. On a correctly specified but non-identifiable design it stays mute-$0.050$ at $n=200$, Clopper-Pearson $[0.024, 0.090]$-while a rank statistic collapses to zero at a pre-registered boundary $c_5^*=2.15\times10^{-3}.$ Two readings of one fit therefore separate the two failures across the three designs a deployable test reaches. That separation is the contribution; detection alone is a crowded flank. In sample it is a bound, out of sample a direction. It is needed because the usual accuracy check is blind: the misspecified estimator's in-domain RMSE is $2.7\times 10^{-2}$, below the observation noise for $\sigma\geq 0.05,$ while the coefficient is wrong by $29.7\%$ at zero noise, $31.2\%$ at the loudest. Nor is the failure architectural: a one-parameter curve fit, a bare parameter and multilayer perceptrons of $49$ and $241$ parameters converge to the same pseudo-true, matched in closed form to $0.07\%,$ whereas a physics-informed network, with its composite objective, converges to a disjoint one. We report where the instrument is blind, a pre-registered negative where a neural estimator loses to Tikhonov-regularized inversion at recovery, and the hypothesis under which its guarantee holds but a trained network violates it.

---


### 4. [Benchmarking Classical and Transformer-Based Models for Document Sensitivity Classification](https://arxiv.org/abs/2608.16928)

**<font color=#1a73e8>作者：</font>** Aleesha Zainab, Muhammad Ahmed Khalid, Faheem Ullah Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic sensitivity classification of organizational documents is a critical yet underserved problem, where the consequences of misclassification range from regulatory violations to security breaches. While AI-based approaches offer a scalable alternative to manual review, their reliability depends fundamentally on the integrity of training data. A pervasive but underreported problem in this domain is label leakage: residual classification markers embedded within document bodies that allow models to exploit surface shortcuts rather than learning genuine content-based sensitivity signals, producing performance estimates that are inflated and unreliable. This paper addresses this problem by introducing Strategic 16K, a carefully constructed, leakage-controlled corpus of 16,000 diplomatic cables sourced from the WikiLeaks Public Library of US Diplomacy (PlusD), and presents a systematic benchmark evaluating six model architectures spanning classical machine learning and transformer-based approaches. We document an extended leakage removal protocol that identifies and eliminates three categories of residual classification markers embedded within document bodies. On the clean benchmark, BERT achieves the strongest performance (Accuracy = 89.14%, F1 = 89.33%), followed by ELECTRA (Accuracy = 88.57%, F1 = 88.90%). Among classical models, TF-IDF with Logistic Regression achieves the strongest performance at significantly lower computational cost. These results constitute the first fully reproducible sensitivity classification benchmark constructed under explicit leakage-controlled conditions from WikiLeaks PlusD.

---


### 5. [Mr.Dec: Daily-Scale Longitudinal Multimodal Modeling for 30-Day Readmission Prediction](https://arxiv.org/abs/2608.16929)

**<font color=#1a73e8>作者：</font>** Minjun Kim, Jong Hak Moon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting 30-day hospital readmission is essential for assessing patient stability and optimizing healthcare resources. As clinical risk evolves with the accumulation of evidence during hospitalization, capturing these dynamic trajectories is essential. However, many existing approaches compress the complex longitudinal history into fixed representations, often losing the granular, day-level clinical signals that reflect a patient's evolving physiological state. To address this, we propose this http URL (Multimodal Readmission-risk prediction Decoder), which models each admission as a natural chronological sequence of daily multimodal events. By leveraging a Transformer Decoder, this http URL integrates daily Electronic Health Record(EHR) updates and intermittent Chest X-ray(CXR) findings in a time-aligned stream, reflecting the actual clinical workflow. To ensure robustness, we utilize Disease-Specific Supervised Contrastive Learning as an auxiliary regularization to induce a diagnosis-aware structure in the latent space. Evaluations on the MIMIC-IV and MIMIC-CXR datasets show that this http URL achieves state-of-the-art performance by preserving the integrity of the clinical sequence. Furthermore, our model identifies "Critical Days" within an admission, providing actionable and clinically grounded interpretations for real-time risk stratification. Code is available at: this https URL

---


### 6. [EMAN: Optimization-Driven Capacity Growth through Path Emergence in Multi-Task Learning](https://arxiv.org/abs/2608.16930)

**<font color=#1a73e8>作者：</font>** Chenlei Fang, Jingchen Li, Hongzong LI 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing multi-task learning methods rely on hard sharing, multiple paths or experts, adaptive sharing, and dynamic expansion. However, their capacity changes are usually constrained by predefined structures or triggered by task boundaries and conflict signals. This raises a fundamental question: can a network start from exact single-path computation and grow a new independent path only when persistent optimization evidence appears? We propose the Emergent Modular Atomic Network (EMAN), an optimization-driven framework for exposing an antisymmetric growth direction through latent relative phases without instantiating a second path, and for monitoring multiple decision signals during training to transform local optimization evidence into a structural decision. EMAN materializes two equal-capacity independent paths only after certification. EMAN adaptively allocates shared and task-specific representation capacity to accommodate varying task requirements. Extensive experiments on controlled rank settings, PASCAL-Context, and NYUv2 validate its effectiveness, achieving improved performance at a competitive computational cost.

---


### 7. [SW-ProxyCE: Zero-Query Adversarial Transfer from Public EEG Encoders to Private Downstream Models](https://arxiv.org/abs/2608.16931)

**<font color=#1a73e8>作者：</font>** Linhua Cong, Dingkun Liu, Dongrui Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) foundation models have recently emerged as a promising paradigm for EEG decoding by learning reusable representations from large-scale heterogeneous neural recordings. However, the open release of EEG foundation encoders, while facilitating downstream developments, also introduces a previously unexplored security risk: publicly available representations may make private downstream models vulnerable. This paper investigates adversarial transfer attacks in EEG foundation model deployment in a public-encoder and private-downstream setting, where attackers have white-box access to a released encoder and a small task-matched labeled reference set, but no access or query to victim parameters, outputs, or gradients. We propose Shrinkage-Whitened Proxy Cross-Entropy (SW-ProxyCE), a query-free task-aware attack framework that recovers task-level decision geometry from a small labeled reference set through shrinkage-whitened class prototypes, enabling transferable adversarial generation without training an additional surrogate classifier. We evaluated SW-ProxyCE across three EEG tasks using three general-purpose foundation encoders and a paradigm-specific pre-trained encoder, covering both linear-probing and full-fine-tuning downstream models in cross-subject and within-subject scenarios. Results demonstrated that adversarial examples generated from the public encoder and limited labeled references can effectively transfer to inaccessible downstream models. SW-ProxyCE consistently outperformed task-agnostic representation-shift attacks, revealing that the strong transferability of EEG foundation models does not necessarily lead to adversarial robustness. Our code will be available on GitHub.

---


### 8. [DOW-KE: Anchor-Free Multi-Layer Knowledge Editing via Direct End-to-End Weight Optimization](https://arxiv.org/abs/2608.16932)

**<font color=#1a73e8>作者：</font>** Ran Chen, Junbo Zhang, Qianli Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-layer locate-then-edit methods for knowledge editing first optimize target residual-stream activations (anchors) at selected layers, then realize them layer by layer as weight updates. This pipeline optimizes an intermediate representation but deploys multi-layer weight updates whose joint effect through the true forward pass is never itself optimized: regardless of how anchors are set or propagated, each update comes from a local solve, so propagation-induced attenuation and distortion go uncorrected, leaving a closure gap between anchor targets and realized edits. We propose DOW-KE, an anchor-free method built on a single principle: what is optimized must be exactly what is deployed. DOW-KE backpropagates the final editing objective through the complete model, jointly optimizing the updates of all edited layers so cross-layer propagation and coupling enter every gradient step. The same principle dictates where preservation resides: embedding the preservation projection in the update parameterization, inside the computation graph, makes every gradient act on the deployed update; post-hoc constraints would reopen the gap, and the constrained search keeps edits clear of protected knowledge. In large-scale sequential editing on two datasets and three models, DOW-KE achieves the highest overall Score and neighborhood Specificity in five of six model-dataset settings among the evaluated baselines.

---


### 9. [WONDER: A Radio World Model-based Negotiation Framework for Multi-Agent UAV Coverage Optimization](https://arxiv.org/abs/2608.16955)

**<font color=#1a73e8>作者：</font>** Jiahao Huang, Rongpeng Li, Zhifeng Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Post-disaster damage to terrestrial infrastructure can disrupt wireless coverage,while Uncrewed Aerial Vehicle (UAV) swarms provide a promising solution for rapid this http URL, due to the limitations in local geometry observations hidden radio impact,and inter-UAV communication,there exists a significant gap between locally visible movement choices and swarm-level coverage this http URL combat this gap,we propose a raido World-model-based Optimized Negotiation framework for Distributed UAV covERage (WONDER).Particularly, to tackle the unavailability of the future radio field from onboard observations, WONDER uses a Joint-Embedding Predictive Architecture (JEPA)-based radio world model to learn and predict the incremental radio effect of each candidate trajectory from deployment-available this http URL-round negotiation in WONDER then coordinates ranked proposals by committing one trajectory at a time and re-evaluating the remaining proposals under the updated context. Our theoretical analyses further validate the effectiveness of such a world model-based framework. WONDER also adopts a Proximal Policy Optimization (PPO)-style Actor and alternates between updating the world model and the actor. Furthermore,we build RadioDynamics,a comprehensive simulation environment that integrates UAV mobility,radio propagation, inter-UAV communication modeling,and digital-twin geometry with ray-traced fields in $62$ metropolitan this http URL on $11$ testing scenes in RadioDynamics show that WONDER achieves the highest balanced score among seven evaluated methods,reaching $0.870$ with a $0.162$ coverage advantage over STACCA, while maintaining $100\%$ connectivity between UAVs.

---


### 10. [The Price of Thinking: Reasoning Effort as a Model-Specific API Contract](https://arxiv.org/abs/2608.16956)

**<font color=#1a73e8>作者：</font>** Yeabin Moon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> API buyers purchase a dated contract, not a model name alone: the contract includes the requested and served model, reasoning-effort term or its omission, output rail, service product, prompt, and price schedule. We study the reasoning-effort term through a registered paired contrast of Sonnet 5 with explicit high effort against the same model with effort omitted, using 30 AIME 2026 items and five calls per item. Every paid attempt was assigned one frozen terminal category, and inference resampled items while retaining their repeated calls. Mean delivered cost was \$0.01031 per call higher under the explicit-high contract than under the omitted contract [+\$0.00204, +\$0.01974]. The corresponding accuracy contrast was +0.0133 [-0.0267, +0.0467]; we did not detect an accuracy difference, and the interval permits a gain of up to 4.67 percentage points that this design cannot rule out. Cost per correct answer was \$0.08665 under the high-effort contract and \$0.07662 under the omitted contract, as registered point estimates. A dated contract census, Models-API metadata, and preregistered raw-response probes further documented model-specific omission semantics, including within a provider; claims remained at documentation grade when raw structure was indeterminate. The request registry, parser, terminal taxonomy, statistical plan, and analysis pipeline were frozen before outcomes were examined; the resulting claims are bounded to the model, task, and collection date studied.

---


### 11. [Quantum-Safe Web Service Architecture Using Time-Based One-Time Passwords](https://arxiv.org/abs/2608.16961)

**<font color=#1a73e8>作者：</font>** Abel C. H. Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> One-Time Passwords (OTPs) have become a common option for multi-factor authentication in several applications. For instance, during website login processes, OTPs are often used in conjunction with traditional text-based usernames and passwords to verify whether the access request originates from a legitimate human user rather than an automated agent. However, in scenarios involving automated connections and system-to-system interoperability, Time-Based One-Time Passwords (TOTPs) may be required to establish secure connections and access Web Services (WSs). Therefore, this study focuses on exploring the development of a quantum-safe web service architecture. The proposed approach achieves transmission security management by implementing Transport Layer Security (TLS) and HyperText Transfer Protocol Secure (HTTPS) based on Post-Quantum Cryptography (PQC). Furthermore, web service security management is realized through the construction of keyed-Hash Message Authentication Code (HMAC)-driven TOTPs. Within the experimental environment, this study evaluates and compares the computational performance of the Secure Hash Algorithm-2 (SHA-2), SHA-3, Ascon-Hash256, and SM3. The required computation time under different hardware resource conditions is analyzed for future web service deployment.

---


### 12. [Study-Strategy Clusters from EdNet Logs Track Engagement, Not Mastery](https://arxiv.org/abs/2608.16963)

**<font color=#1a73e8>作者：</font>** Qingchuan Lyu, Yingxin Li, Albert Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning analytics often treats unsupervised clusters of intelligent tutoring system (ITS) logs as learner types that should predict learning. We test that assumption on EdNet-KT3. Clustering study-strategy features (resource use, revision, video, problem practice) for 5{,}000 active learners yields a silhouette-selected parent cut ($k=5$) with 4 contrast poles (reading-focused, video-heavy, revision-heavy, and problem-first) plus a large near-mean residual ($\sim$64.9\%). Reclustering that residual adds four finer styles, giving a bootstrap-stable hierarchy of 8 named strategies. We split each learner's timeline by respond count so clusters use only the early half and outcomes only the late half. Early clusters predict later engagement (continuing to practice and finishing late sessions, especially persistence, $\eta^{2}\approx 0.106$; completion $\eta^{2}\approx 0.021$) but not later unassisted accuracy (correctness on late first-attempts without help; $p_{\mathrm{adj}}\approx 0.093$). Volume rises with some styles, yet volume-only clustering barely matches strategy labels (ARI$=0.064$). A knowledge-tracing model (SAKT) on the seven TOEIC exam sections predicts next correctness only modestly better than a baseline that knows only how hard each section usually is (AUC lift $+0.051$; CI $[+0.045,+0.058]$), and that mastery signal is nearly independent of behavior styles (ARI$=0.007$). Behavioral clustering here describes study styles and engagement, not knowledge gains.

---


### 13. [RoBell-RVFL: A Robust Generalized Bell Random Vector Functional Link Network](https://arxiv.org/abs/2608.16965)

**<font color=#1a73e8>作者：</font>** A. Rahaman, A. Quadir, M. Tanveer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The dominance of majority classes in real-world datasets poses a fundamental challenge to randomized neural networks, often biasing decision boundaries and overlooking critical minority samples. Existing remedies, such as synthetic minority over-sampling (SMOTE) and class-weighted loss functions, primarily address class proportions while neglecting intra-class distribution, making them vulnerable to label noise and outliers. In this paper, we propose \textbf{RoBell-RVFL}, a robust and lightweight \emph{quality-aware} generalized bell random vector functional link network that redefines how randomized models handle class imbalance and noisy data. RoBell-RVFL employs a dual-strategy, sample-level weighting mechanism that strictly preserves minority class information using unit weights, while adaptively regulating the influence of majority class samples through a probability-weighted generalized bell (gbell) membership function in a kernel-induced feature space. This design effectively suppresses noisy, boundary, and outlier samples within the majority class, enabling the network to learn from informative samples rather than merely abundant ones. By explicitly incorporating local class probability and class distribution information into the learning process, RoBell-RVFL achieves adaptive control over sample contributions without sacrificing the closed-form learning efficiency of RVFL networks. Extensive evaluations on UCI and KEEL benchmark datasets, along with robustness tests under up to 40\% label noise, demonstrate that RoBell-RVFL consistently and significantly outperforms recent state-of-the-art RVFL variants. The results indicate that adaptive, quality-aware sample weighting is essential for robust RVFL learning, rendering conventional global weighting schemes ineffective in noisy and imbalanced environments.

---


### 14. [Multi-Observer Vehicle Localization Case Study with Roadside Radar and Connected Vehicle Sensing](https://arxiv.org/abs/2608.16966)

**<font color=#1a73e8>作者：</font>** Aleksi Pippuri, Nilusha Jayawickrama, Risto Ojala  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In modern intelligent transportation systems, it is essential to accurately estimate vehicle positions, especially in mixed traffic conditions where both connected and conventional vehicles coexist. Roadside infrastructure and connected vehicles can provide complementary observations of the same traffic scene, but real-world evidence on decision-level fusion between these sources remains limited. This paper proposes a multi-observer vehicle localization framework that fuses compact object-level detections from a static roadside radar and a dynamic LiDAR-equipped connected vehicle. We evaluate the framework with real-world data collected at an urban intersection in Helsinki, Finland, with a separately instrumented target vehicle used as the reference trajectory. Two extended Kalman filter based strategies for the localization task were benchmarked. The performance of the radar and LiDAR sensors were evaluated separately, and the two fusion strategies were explored under nominal sensing conditions, reduced LiDAR update rates, simulated LiDAR occlusions, and different target-vehicle motion states. The results show that, under full LiDAR availability, fusion performance is dominated by the LiDAR observations, while the less accurate and less consistent radar observations provide only limited additional improvement. Nevertheless, AEKF achieves small gains over the LiDAR-only baseline, and object-level connected vehicle observations remain useful when shared at reduced update rates. These findings indicate that decision-level fusion provides scenario-dependent benefits rather than automatic improvement over a strong single-sensor baseline. We release the dataset and implementation on Github to support further research: this https URL

---


### 15. [MultiSigBERT: Beyond Survival Analysis through Multimodal and Sequential Modeling in Oncology](https://arxiv.org/abs/2608.16972)

**<font color=#1a73e8>作者：</font>** Paul Minchella, Stéphane Chrétien, Guillaume Metzler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning has become an essential component of modern healthcare, where the integration of heterogeneous data sources offers unprecedented opportunities to improve clinical decision-making. Electronic Health Records (EHR) contain complementary information -- including narrative clinical reports, numerical measurements, and structured variables -- yet most survival models remain limited to a single modality or fail to exploit the temporal nature of patient trajectories. We propose MultiSigBERT, a unified framework for multimodal sequential survival modeling in oncology based on path signature representations. Here, narrative medical reports (free-text) are converted into sentence embeddings by extracting and averaging contextual word embeddings. These representations are then compressed via modality-specific PCA and concatenated with structured covariates to form joint temporal trajectories which are then encoded using the Signature transform, a tool from Rough Paths theory that efficiently captures higher-order temporal interactions across modalities without supervision needed. The computed Signature features are finally incorporated as high dimensional features into a LASSO-regularized Cox model to estimate individualized risk scores. The performance of our novel MultiSigBERT pipeline is illustrated on the analysis of a real-world oncology cohort from the Léon Bérard Center, comprising over 120,000 medical reports and structured records from more than 2,500 patients. The model achieves a concordance index of 0.743 (sd 0.029) on an independent test set, demonstrating the benefit of jointly modeling multimodal temporal dynamics together with patient-level geometric structure for survival prediction.

---


### 16. [AerialYield-B2D: A Greenhouse Blueberry Dataset with Five-Stage Ripeness Masks and Fruit Counts](https://arxiv.org/abs/2608.16973)

**<font color=#1a73e8>作者：</font>** Iyyakutti Iyappan Ganapathi, Afeefa Azam, Muhammad Owais 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blueberry ripeness is judged by berry colour, cluster composition, and the distribution of maturity stages within a plant, however, public green house image resources with dense ripeness-stage masks remain limited. We present AerialYield-B2D, where B2D denotes BlueBerry Dataset, acurated real-image resource containing 514 RGB images and 30,195 annotated blueberry instances across five ripeness stages: green immature, pale pink, pink-turns-purple, fully ripe and over-ripe. The release provides class-specific binary masks, overall berry masks, semantic label maps, image-level count tables, SHA-256 hashes, source metadata, recommended train/validation/test splits and technical validations. AerialYield is the broader project name; this release does not provide harvest weight, fruit mass or per-area yield measurements, and the count labels should therefore be interpreted as image-level berry counts rather than yield estimates. The images include 424 smartphone greenhouse images, 67 video-derived frames, and 23 DJI Fly video-frame samples, providing a reproducible dataset for ripeness segmentation, berry counting, and class-imbalance analysis in controlled-environment blueberry production.

---


### 17. [Position: Fairness Failure in Generative Models is an Evaluation Problem](https://arxiv.org/abs/2608.16974)

**<font color=#1a73e8>作者：</font>** Mariia Vladimirova, Jean-Yves Franceschi, Thibaut Issenhuth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite groundbreaking advancements in generative models during the last decade, concerns about their lack of fairness, reinforcing societal inequalities and harming marginalized groups, remain under-addressed and difficult to act upon. This position paper argues that fairness failures in generative models, albeit driven by multiple factors, are ultimately stemming from an evaluation problem: fairness findings are rarely comparable across papers or actionable for deployment decisions. This paper diagnoses recurring empirical and conceptual failure modes in current practice and motivates a shift from ad-hoc bias checks to standardized, generative-specific evaluation. We propose Fairness Cards as a minimal reporting artifact that makes evaluation choices explicit (prompt families, counterfactual protocols, metrics, and refusal handling) enabling reproducibility, comparability, and accountability. We conclude with additional recommendations towards a paradigm shift in evaluation standards. Our project page can be found at this https URL .

---


### 18. [The Problem Is the Problem: Towards Scalable Mathematical Discovery](https://arxiv.org/abs/2608.16977)

**<font color=#1a73e8>作者：</font>** Zeyu Zheng, Shengtong Zhang, Jeremy Avigad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are increasingly capable of contributing to mathematical research. In research practice, frontier-model reasoning is a limited resource, and expert mathematical review is even more sharply constrained. Allocating these scarce resources well is therefore central to making AI-assisted mathematical discovery efficient. In most current AI-for-math workflows, human effort is concentrated at the beginning and end, in selecting suitable research problems and later reviewing the resulting artifacts. These two stages are becoming bottlenecks for research-level mathematics. We address them by proposing a new human-AI discovery paradigm. The human input is no longer a single problem selected in advance, but a research direction in which the experts have interest and expertise. The system then searches a broad literature corpus for candidate problems in that direction. Inspired by search and recommender systems, we build Find, Attempt, and Recommend (FAR), a literature-to-review cascade that automates the search for suitable problems and focuses human attention on artifacts that have passed several stages of filtering. In a combinatorics pilot, the pipeline starts from 5,245 combinatorics papers, recovers 6,453 candidate conjectures or open problems, and filters them to 4,717 apparently well-posed and still-open conjectures. Subsequent reasoning and automated triage stages surface 598 potential resolutions and select 77 items for author-team review. Among them, we identify many interesting discoveries, including results on conjectures and questions of Davies--Jenssen--Perkins--Roberts, Erdős--Straus, Ikenmeyer--Pak--Panova, and Lund--Saraf--Wolf. These results demonstrate the effectiveness of this new mode of human-AI collaboration for mathematical discovery.

---


### 19. [PXDepth: Pixel-Space Modeling for Structure Preserving Monocular Depth Estimation](https://arxiv.org/abs/2608.16984)

**<font color=#1a73e8>作者：</font>** Zhiyuan Yuan, Guanying Chen, Lingteng Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent monocular depth estimators achieve strong zero-shot generalization, yet often struggle to preserve fine-grained structures and object boundaries. We attribute this limitation to the prevalent combination of large-patch ViT encoders and convolutional decoders, as coarse tokenization can weaken pixel-level cues that upsampling cannot fully recover. To address this issue, we propose PXDepth, a discriminative monocular depth model that separates global context modeling from pixel-level depth prediction. Specifically, a large-patch ViT captures global scene context, while a pixel-space predictor composed of Context-Modulated Pixel Transformer blocks maintains high-resolution spatial representations throughout depth estimation. This design preserves fine structures and sharp boundaries without sacrificing global depth consistency. Across diverse zero-shot benchmarks, PXDepth combines faithful local geometry with competitive global depth accuracy while remaining efficient at inference. Our code and model are available at this https URL.

---


### 20. ["It just kind of shows that I went somewhere": An Exploratory Study of Fitness Data Sharing](https://arxiv.org/abs/2608.17014)

**<font color=#1a73e8>作者：</font>** Mara Solen, Thomas James Davidson, Emily Wall 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The sharing of curated fitness data posts occurs frequently on fitness-focused social platforms such as Strava and on general social media platforms such as Instagram, which is a novel context for visualization. To better understand the process of sharing and designing fitness data posts, as well as the role of visualization within them, we conduct a constructivist grounded theory study. We conduct and analyze 18 semi-structured interviews with fitness data sharers. From our analysis of the data, we find three novel characteristics of fitness data sharing: (i) the role of visualization as providing proof that an individual did an activity, (ii) the importance of expressing individuality in posts, and (iii) design conformity to cultural norms. We also derive a set of design implications, including a need for more options for visualizations for activities without routes, more user control in fitness data sharing platforms, and maintained ease of use while increasing customization options.

---


### 21. [YILDIZ-VPR: A Novel Dataset with Dense Coverage Under Diverse Environmental Conditions for Visual Place Recognition](https://arxiv.org/abs/2608.17033)

**<font color=#1a73e8>作者：</font>** Serdar Yildiz, Abbas Memiş, Songül Varli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Place Recognition (VPR) aims to recognize the location of a query image by comparing it with a set of geo-referenced images. Although many datasets have been proposed for VPR, collecting dense and diverse visual data from pedestrian-level viewpoints is still an important need. In this paper, we introduce YILDIZ-VPR, a visual geo-localization dataset collected through repeated walking traversals on the Davutpasa campus of Yildiz Technical University. The dataset includes outdoor scenes captured at different times of day, seasons, and weather conditions. It contains a wide range of visual content, including historical buildings, modern structures, roads, green areas, and wooded regions. Each video was recorded with a GoPro 9 camera and synchronized with GPS sensor data to provide location labels for the extracted frames. In addition to GPS coordinates, the dataset also includes auxiliary sensor information such as gyroscope, speed, and temperature data. With its dense coverage and long-term visual variability, YILDIZ-VPR provides a useful resource for studying image-based and temporal visual place recognition under realistic outdoor conditions.

---


### 22. [Agents unlock new capabilities through Switching LoRA Adapters as a Tool (SLAaaT)](https://arxiv.org/abs/2608.17034)

**<font color=#1a73e8>作者：</font>** Kenneth Ge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training can unlock new capabilities and improve performance on specialized tasks, but sometimes at the cost of catastrophic forgetting in other domains. This poses a problem in long agent trajectories that compose different capabilities. We reject this tradeoff by giving an agent a tool to switch between specialized LoRA adapters mid-trace. To test its effectiveness, we compose two synthetic coding tasks that are logically simple but require specialization. We find that this allows the model to solve problems it previously could not, that the model is able to switch autonomously (and find a new strategy that beats our human heuristic baseline on one task), and that this incurs an up to an 18x reduction in capability tax compared to an agent using only one specialized adapter. Our approach also substantially outperforms spawning subagents in both task capabilities and token usage.

---


### 23. [What Cognitive Accessibility Reveals About Data Visualization](https://arxiv.org/abs/2608.17039)

**<font color=#1a73e8>作者：</font>** Keke Wu, Jinjuan Heidi Feng, Jonathan Lazar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data visualization aims to augment human cognition and make data accessible to diverse audiences. As data increasingly shapes participation and decision-making across many domains, there is a growing need to examine whether prevailing assumptions in visualization adequately reflect the diversity of human abilities, experiences, and needs. We argue that cognitive accessibility provides a critical lens for examining these questions and functions as a stress test for visualization theory. Drawing on cognitive accessibility research and our experiences studying accessible visualization, we identify three interconnected assumptions that shape visualization research and practice: assumptions about what forms of cognition visualization supports, how accessibility is defined and measured, and whose needs and abilities are centered in design and evaluation. Making these assumptions explicit reveals opportunities to rethink longstanding approaches and open new directions. Ultimately, we believe that cognitive accessibility can serve as a catalyst for innovation, expanding what visualization supports, whom it serves, and the roles it plays in people's lives.

---


### 24. [Remote-Timer-as-a-Service: Efficient Microarchitectural Leakage in the Cloud with Remote Timers](https://arxiv.org/abs/2608.17043)

**<font color=#1a73e8>作者：</font>** Martin Schwarzl, Haocheng Xiao, Albert Pedersen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Edge computing solutions have become a crucial part of the industry, delivering fast, flexible and scalable applications close to the end users, with typical use cases including dynamic content creation, image resizing and chatbots. Cloudflare Workers is one such framework, which handles millions of HTTP requests per second worldwide. To reduce start-up latency, Cloudflare Workers removes process-isolation boundaries between multiple tenants and leverages language-level isolation. This architecture poses the risk of Spectre attacks. To mitigate these, Cloudflare Workers previously introduced several countermeasures such as restricted timer measurements, no shared memory, no multithreading and Dynamic Process Isolation (DyPrIs), detecting potential attacks and process-isolating potentially malicious scripts.
We demonstrate that the production implementation of DyPrIs was insufficient. We adopt microarchitectural amplification techniques and discover various possibilities to measure time in the production environment of Cloudflare Workers. Given these techniques, we show that freezing and coarsening timers in the Cloudflare Workers security model is insufficient. Leveraging both timing amplification and remote timers, we demonstrate a remote Spectre attack that leaks a JWT token from a co-located victim worker in the Cloudflare Workers production environment. We outperform the existing attack by orders of magnitude, going from 2 bit/min to up to 12 bit/s at an accuracy of 99.16%, posing an immediate risk to customer data. Following our end-to-end attack, Cloudflare Workers mitigated it in a coordinated effort by integrating the V8 Sandbox limiting transient access to 64-bit pointers, improving the detection capabilities of DyPrIs, and deploying hardware-assisted MPK-based in-process isolation to confine each tenant heap under a dedicated memory-protection key.

---


### 25. [The 10th AI City Challenge](https://arxiv.org/abs/2608.17044)

**<font color=#1a73e8>作者：</font>** Zheng Tang, Shuo Wang, David C. Anastasiu 等 37 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The 10th AI City Challenge, held with ECCV 2026, marks a decade of community benchmarking for intelligent transportation, smart cities, and physical AI. Since its 2017 start with vehicle detection, classification, and tracking, the challenge has grown into a broad benchmark suite for multi-camera perception, multimodal reasoning, synthetic-to-real learning, generative forecasting, and privacy-preserving evaluation. The 2026 edition continued this growth with 325 registered teams, up from 245 in 2025, and participation from 26 countries and regions, up from 15. Its six primary tracks cover multi-camera 3D perception, transportation safety captioning and VQA, traffic anomaly reasoning, text-based person anomaly search, generative traffic video forecasting, and cross-city object detection. Track 3 further includes two out-of-domain leaderboards, submitted as Tracks 7 and 8, for fisheye traffic-violation understanding and pedestrian situated-intent VQA. This paper summarizes the challenge setup, datasets, evaluation protocols, leaderboard results, and workshop papers. Across tracks, successful systems combine foundation models with geometric grounding, retrieval or reranking, synthetic-data design, domain adaptation, and controlled inference.

---


### 26. [Memory Is Communication: The Frontier Between Remembering and Signaling](https://arxiv.org/abs/2608.17053)

**<font color=#1a73e8>作者：</font>** Yashar Talebirad, Eden Redman, Ali Parsaee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A bounded agent may obtain information for a decision from its own past, from peers, or from both sources. Retaining task-relevant history can reduce later communication, while a peer message can supply what memory lacks. Under limits on both resources, how should an agent allocate its information budget? Given a fixed task and decision rule, the memory and message rate pairs attaining a performance threshold form an achievable region under specified rules for using history and peer observations. We call its efficient boundary the remembering--signaling frontier. Across conditions where history permits the same maximum reduction in task loss, we hypothesize that a bounded agent will need less peer communication when it obtains a larger loss reduction from history. In preliminary referential games, target repetition coincided with shorter successful messages, while predictability from a hidden cyclic rule did not shorten them. Experiments varying memory and message rates can estimate the frontier and test this prediction across cooperative tasks.

---


### 27. [Why This and Not That? A Collaborative Reflection Approach for Understanding Thought Coverage in Decision Making Support Dialog](https://arxiv.org/abs/2608.17054)

**<font color=#1a73e8>作者：</font>** Morita Tarvirdians, Hayley Hung, Catharine Oertel  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational agents that support reflection for decision making often rely on adaptive dialogue policies that map observed user behavior to actions such as probing, deepening, or redirecting. Yet the same pattern can reflect a range of different reasons such as deliberate prioritisation or limited self-access. By modeling the observable pattern rather than the user's reason for it, current policies risk premature assumptions about the user state and inappropriate next actions. To address this gap, we introduce a human-centered method for surfacing this hidden inference step. In a user study with 62 users and 232 collaborative moments, we pause a reflection-support agent when it would normally redirect the conversation, surface its observation, and ask users to interpret the pattern and decide how to proceed. We derive a taxonomy of nine interpretation categories and show that similar reflective states can call for substantially different follow-up actions. Our findings challenge the assumption that adaptive dialog policies can rely on observable behavior alone, and show how user-provided interpretations can inform more appropriate conversational actions.

---


### 28. [CAS-FD: Contact-Aware Temporal Sampling for Single-View Foul vs Dive Recognition](https://arxiv.org/abs/2608.17060)

**<font color=#1a73e8>作者：</font>** Md. Jahidul Islam, Mahfujul Alam, Md. Nazmul Islam Seyam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distinguishing a genuine foul from a simulated dive in football remains one of the sport's most contested fine-grained recognition problems, especially when such decisions have to be from a single broadcast view without multi-view camera angle. We introduce a balanced 600-clip single-view Foul/Dive dataset and show that contact-aware sampling concentrating the model's attention around the moment of physical contact rather than treating all frames equally yields substantially improved recognition of this contact- specific problem. The proposed approach achieves 86.0% accuracy and macro-F1 0.860 on the held-out test split, a 12 percentage- point gain over contact-unaware alternatives that grows further on unseen data. We also evaluate each pipeline component against human annotations, establishing where and why the system suc- ceeds and fails. The result is a documented dataset, a reproducible single-view pipeline, and a grounded evaluation framework for fine-grained contact-event recognition in broadcast football footage. The dataset and code are available at this https URL tamim/contact-aware-dive.

---


### 29. [CUSTOS: Toward Forensic-Ready Zero Trust at the Capture-Containment Boundary](https://arxiv.org/abs/2608.17068)

**<font color=#1a73e8>作者：</font>** Avinash Srinivasan, John Paramadilok  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zero Trust (ZT) replaces implicit trust with continuous verification, but mutual TLS, ephemeral workloads, identity-centric control, and automated remediation reduce payload visibility, weaken IP-based attribution, and shrink the window for acquiring volatile evidence. We propose CUSTOS, a forensic-ready ZT reference architecture centered on a Forensic Management Point (FMP) that coordinates tiered capture, identity- and policy-linked reconstruction, telemetry orchestration, and ZT-controlled investigative access. We evaluate a composed, component-level prototype using a live enforcement gateway plus separate runtime and orchestrator experiments. An always-on decision record is captured and hash-chained on the gateway at a 1.9-3.0\% throughput cost on in-process policy engines, preserving decision provenance outside the monitored workload under stated trust assumptions. Reactive checkpointing (about 65 ms) precedes seconds-scale defender-routed eviction but loses to unsequenced direct SIGKILL (about 9 ms), in-kernel enforcement, and adversarial self-destruction, producing the forensic shredder effect. On a real container, concurrent capture and SIGKILL recovered the planted secret in 0/1000 trials; sequencing SIGKILL behind the FMP barrier recovered it in 1000/1000. The primary integrated single-node Kubernetes race checkpoints an FMP-controlled process; container-memory capture is evaluated separately and was unavailable in the managed-Kubernetes configuration. Across five public benchmark datasets and a synthetic schema reference, identity-oriented telemetry populates 64-75\% of the decision-record schema against 18-30\% for network-oriented, while rate limiting bounds the full-memory admission ceiling. These results show that forensic-ready ZT requires both an always-on evidentiary floor and bounded reactive capture, while identifying where volatile evidence remains unrecoverable.

---


### 30. [Certified but Private: Scalable Zero-Knowledge Proofs for Neural Network Guarantees](https://arxiv.org/abs/2608.17070)

**<font color=#1a73e8>作者：</font>** Youwei Zhong, Ben Merbaum, Timos Antonopoulos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the growing deployment of machine learning models, formal guarantees of the robustness and fairness of these models have become increasingly important in safety-critical and legal-compliance settings. However, model parameters are often commercial secrets that cannot be disclosed to auditors or end users. To this end, we present PANDA, a scalable system that uses zero-knowledge proofs (ZKPs) to prove the robustness and fairness properties of a model without revealing its private parameters. PANDA is built on top of CROWN, an efficient robustness certification framework that is used in many state-of-the-art formal verification tools for neural networks. The core contribution of PANDA is a novel algorithm for proving linear relaxation bounds for non-linear activation layers, yielding simple, lightweight proofs. Remarkably, our system can generate proofs of local robustness for neural networks with more than 2.9M parameters in 5 minutes, and can verify them in 10 seconds. Prior ZKP-based robustness system rely on exponential-time algorithms that cannot scale to nontrivial networks. In contrast, PANDA scales polynomially in the number of neurons in a network, allowing us to support neural networks 4 orders of magnitude larger than previous approaches with significantly reduced prover overhead.

---


### 31. [Dynamic Regime-Aware Conformal Calibration for Reliable Economic Forecast Intervals under Multiple Distribution Shifts](https://arxiv.org/abs/2608.17079)

**<font color=#1a73e8>作者：</font>** Bogdan Oancea  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction provides distribution-free prediction intervals but relies on exchangeability, an assumption often violated in economic forecasting because of covariate shift, concept drift, local heterogeneity and latent regimes. We propose Dynamic Regime-Aware Conformal Prediction (DRACP), which combines density-ratio, localized kernel and probabilistic regime-aware weighting with a self-tuning online significance controller in a unified weighted conformal calibration framework. We distinguish three theoretical results: finite-sample validity under oracle importance weights, a coverage-gap bound for estimated weights with rates in effective sample size, and deterministic or regret guarantees for the online controller. We evaluate DRACP against six baselines on 48 real forecasting series covering euro-area and EU-27 HICP inflation, US macroeconomic and energy indicators, and daily financial series. Recent online methods (FACI, strongly-adaptive online conformal prediction and conformal PID) were verified against the authors' implementations. DRACP is not the most efficient method: strongly-adaptive online conformal prediction achieves the best interval score and intervals about 20% narrower. Instead, DRACP provides the most reliable calibration, achieving coverage closest to the nominal 0.90 (0.890), never falling below 0.80 on any series, maintaining the best coverage at all forecast horizons, and performing best during the 2021-2023 inflation surge. The strongly-adaptive method undercovers on 20 of 48 series versus 10 for DRACP. DRACP therefore offers a principled trade-off between calibration and efficiency, favoring reliable coverage when prediction intervals must satisfy coverage standards. An ablation study shows that the online controller and conditional-scale normalization provide most of the performance gain, whereas the weighting components make a smaller contribution.

---


### 32. [SentryBus: A Multi-Vantage Observability Model and Validated Instrument for I2C Sensor-Interface Manipulation](https://arxiv.org/abs/2608.17082)

**<font color=#1a73e8>作者：</font>** Sandesh More, Elton Batista, Karla Daley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sensor-driven systems in medical Internet of Things devices, drones, and cyber-physical systems commonly trust a measurement once it reaches the embedded processor. An adversary on the digital interface between sensor and processor can supply a plausible value that correct firmware accepts and reports as ordinary telemetry. The hypothesis is that sensor interface manipulation leaves observable evidence on the acquisition path, that the evidence appears at different vantages depending on attacker position, and that a passive host-side monitor therefore has a measurable boundary beyond which manipulation becomes indistinguishable from legitimate acquisition. SentryBus models acquisition behavior on the I2C sensor bus using transaction timing, read and write sequences, transfer lengths, address behavior, register and FIFO state access, and raw data transitions. The adversary is modeled as an inline interposer, parallel controller, sensor replacement, or compromised host, because a commodity target-only sensor cannot initiate transfers or stretch, reorder, or delay bus transactions. A dual sided testbed captures both busses, host memory, and telemetry, and the detector consumes the host facing bus alone while the remaining vantages serve as ground truth. A physiological instantiation reports three measured results: an inline interposer bounded at 0.842 percent of acquisition service time while preserving acquisition schedule and payload content, clean acquisition stability sustained over 6304 seconds at the telemetry vantage with no clock regression, and a negative result establishing that data-transition features encode session specific signal statistics and do not transfer across capture sessions. Instrument characterization shows that a low-cost analyzer can truncate captures without kernel visible error. Controlled attack trials are still outstanding, so no detection rate is claimed.

---


### 33. [Backward through Time, Algebraically](https://arxiv.org/abs/2608.17087)

**<font color=#1a73e8>作者：</font>** Konstantinos Kogkalidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear temporal logic is a modal extension of propositional logic that allows one to state how a system should behave over time. Its canonical domain is the booleans, but discretely-valued judgements are of little use in steering softly-valued systems (neural policies, adaptive controllers, sequence models, etc). In such cases, the goal formula's (dis)satisfaction becomes a training signal, and differentiability becomes a prime concern. Candidate differentiable semantics abound, but navigating them is tricky. Implementations, where available, are shallow embeddings, demanding an upfront commitment to a single semantic algebra and its (usually implicit) conduct. The paper casts the reader as a functional programmer asked to come to terms with this predicament, and refusing. Out of that refusal comes an evaluation engine that is algebra-generic and amenable to differentiation, together with an executable specification of the algebras it can accept. Various algebras are implemented and audited for their behavior, both forward and backward. Each algebra turns out to be a choice of which direction to disappoint, and how. Everything described (and more) is part of the PyTorch library telos, to be found at this https URL.

---


### 34. [There is No Theoretical Curse of Multilinguality For Embedding Space Structure](https://arxiv.org/abs/2608.17088)

**<font color=#1a73e8>作者：</font>** Niyati Bafna, Neha Verma, Vilém Zouhar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A central goal of multilingual NLP is to achieve high monolingual performance per language and cross-lingual alignment for large-scale language coverage with a multilingual model. The curse of multilinguality describes the phenomenon of degradation in multilingual model performance as we increase language coverage, posing a threat to the above goal. This paper asks whether multilingual embedding spaces are inherently incapable of achieving perfect multilinguality without a prohibitive increase in required capacity. We first formalize the goal of "perfect multilinguality", embodied in two multilinguality conditions. We then prove that the minimum dimensionality required for perfect multilinguality grows only logarithmically in the number of languages. That is, we show that there is no theoretical curse of multilinguality for embedding space structure. This suggests that the empirical curse of multilinguality is a result of real world data and training conditions. We back this understanding with a small-scale empirical study. Our paper provides the first theoretical and intrinsic perspective on the curse of multilinguality, with implications for the scientific understanding of this phenomenon.

---


### 35. [Deep Learning for Cross-Border Electricity Price Forecasting: A Comparative Study](https://arxiv.org/abs/2608.17091)

**<font color=#1a73e8>作者：</font>** Hadeer Elashhab, Sai Srijan Papineni, Marvin Dorn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While publicly available electricity market data presents a valuable resource for forecasting research, the field lacks established benchmark datasets for standardized comparison. As a result, many studies have relied on different datasets and metrics to evaluate methods in isolated settings, making it difficult to assess progress and compare state-of-the-art approaches consistently. In this work, we use public data to evaluate deep learning models for electricity price forecasting (EPF) across multiple market settings. Our goal is to establish a reproducible framework that enables a consistent evaluation of forecasting models. Although deep learning has been explored for day-ahead EPF, many prior studies are limited to single-market settings, narrow feature sets, or fixed training regimes. This work presents a comparative evaluation of six deep learning models--covering state-space, MLP, RNN, and Transformer-based architectures--emphasizing generalization across markets. We simulate low-data target-market conditions using zero-shot, one-shot, and few-shot learning. Our test set focuses on the Germany-Luxembourg (DE-LU) bidding zone in 2024 using a standardized dataset with calendar, historical price, and market-derived features. Our findings suggest that N-HiTS and NBEATSx perform competitively in limited-data scenarios, while transformer-based models can reach comparable accuracy but tend to require more adaptation and tuning. Model performance also benefits from careful feature selection and hyperparameter tuning, and we note that the differences between the strongest models are often small.

---


### 36. [Digital Twin-Based Intrusion Detection for Vehicle Powertrain CAN Bus Systems](https://arxiv.org/abs/2608.17093)

**<font color=#1a73e8>作者：</font>** Araf Rahman, M Sabbir Salek, Mashrur Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing automotive intrusion detection systems (IDSs) for the Controller Area Network (CAN) largely target discrepancies in message timing, frequency, or sequencing and cannot detect attacks that preserve these properties while manipulating the payload. Digital twins (DTs) have been used to emulate CAN traffic and generate attack scenarios for IDS evaluation, but their use for intrusion detection remains unexplored. This study develops a DT-based IDS that jointly models physical relationships among decoded powertrain signals and identifies attacks through residuals between predicted and observed behavior. A shared-encoder LSTM DT was trained on 17 decoded signals from a real Hyundai/Kia CAN log to jointly predict seven numeric and two categorical gear signals over a 24-step window. A timestep is flagged when a residual exceeds a calibrated threshold, while adaptive rollout protects the twin's input history from sustained contamination. Four attacks (plateau, continuous drift, masquerade, and gear masquerade) were evaluated against the twin and a range-and-plausibility baseline. The DT outperformed the baseline across all attacks, achieving detection rates of 94.6% for continuous drift and 89.2% for masquerade, while the baseline detected almost none of the fabricated payload attacks. These results demonstrate that learning coupled vehicle dynamics enables detection of stealthy payload manipulations that preserve normal CAN communication patterns. False positive rates reached 39.6%, highlighting the need for improved robustness under sustained attacks. The DT-based IDS shows promise for detecting stealthy payload-level CAN attacks that preserve normal communication patterns, supporting behavior-based cybersecurity for connected and automated vehicles.

---


### 37. [A Glyph Is Not a Letter, a Token Is Not a Word, a Space Is Not a Space: What the Units of Voynichese Are Not](https://arxiv.org/abs/2608.17096)

**<font color=#1a73e8>作者：</font>** Liudmila Rozanova, Alexander Temerev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Voynich manuscript (Beinecke MS 408) is usually analysed on three unstated assumptions: that its glyphs are letters, that the strings between blanks are words, and that every blank is a word space. We test all three against the Zandbergen-Landini transliteration with matched prose, cipher, and pseudo-text controls and quire-level resampling. None holds, and the failures share a shape: the order in Voynichese sits at the edges of tokens and at graded boundaries between them, not in the succession of tokens themselves. Glyph regularity is too strong for one-to-one substitution of any tested plaintext (conditional entropy 2.7 bits against about 3.5 for Latin, Italian, and English) and resolves instead onto a quire-stable scale of recurrent multi-symbol units. Tokens form a plausible vocabulary, yet the identity of one token predicts the next by under 1% of token entropy, below every matched control (2-10%), while the glyphs at token edges share 0.2 bits of mutual information, more than in any prose control. Blanks fall into two regimes: the separators transcribers marked uncertain behave like word-internal junctures, are physically narrower on the page (AUC 0.905 from independent image coordinates, with the same sign in a small blind ink audit), and are crossed by learned units even when every space is erased before learning. This profile is also what discriminates. A published Voynich-imitating cipher and a self-citation text generator both reproduce the low entropy, the unit scale, the weak token order, and the null result of a calibrated substitution attack; neither reproduces the edge-glyph coupling or the open, hapax-rich vocabulary (70% singleton types against 41% and 59-60%). Any account of the manuscript must therefore earn, rather than assume, the step from glyphs, tokens, and separators to letters, words, and word spaces, and these are the measurements on which to do so.

---


### 38. [From Abductive Explanations to Global Logical Rules for Node Classification in SGCs](https://arxiv.org/abs/2608.17103)

**<font color=#1a73e8>作者：</font>** Bryan Lima Cavalcante, Thiago Alves Rocha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have achieved remarkable performance in node classification tasks, motivating growing interest in methods capable of explaining their predictions. Recent logic-based approaches, such as LogicXGNN, derive global logical rules for Graph Neural Networks (GNNs) from collections of explanatory subgraphs. While informative, these subgraphs may contain redundant structural information that is specific to individual nodes, potentially limiting the generality of the extracted rules. In this work, we propose a logic-based framework for node classification in Simple Graph Convolution (SGC) networks that uses minimal abductive explanations as an intermediate representation for rule extraction. For each node, we compute a minimal set of node-feature pairs sufficient to preserve the predicted class. These explanations are then used to train decision trees from which global logical rules are extracted. Experiments on benchmark datasets show that the proposed framework produces compact global rules while maintaining high fidelity to the original SGC model.

---


### 39. [OV3D-Bench: A Diagnostic Benchmark for Open-Vocabulary Monocular 3D Detection](https://arxiv.org/abs/2608.17110)

**<font color=#1a73e8>作者：</font>** Mariia Gladkova, Neehar Peri, Ishan Khatri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary monocular 3D detectors report strong in-domain performance, but each evaluates under a different protocol, several rely on per-image category oracles unavailable at deployment, and all collapse geometry and semantics into a single AP metric. To address this, we introduce OV3D-Bench, a diagnostic benchmark that compares open-vocabulary monocular 3D detectors under deployment-realistic conditions across seven indoor and outdoor datasets. Our benchmark replaces the per-image class name oracle with test-time dataset-level class name prompts, and decouples detection accuracy along three axes: localization, semantic robustness, and cross-domain transfer. We evaluate seven representative detectors and find that (i) they localize objects well yet often mislabel a correctly localized box as a semantically adjacent category; (ii) accuracy is highly sensitive to prompt phrasing (e.g. WildDet3D's performance collapses from 18.6 to 5.4 AP when prompted with "a detailed high-resolution photo of a car" rather than "car"); and (iii) the widely adopted target-aware protocol hides these errors (e.g. inflating DetAny3D's AP by 1.9 $\times$ on ScanNet). Lastly, we demonstrate that simply remapping a frozen closed-vocabulary detector's predictions using a contrastive vision-language encoder such as SigLIPv2 performs competitively against recent purpose-built open-vocabulary methods. This indicates that geometric localization is more mature, while open-vocabulary semantics remains the primary bottleneck.

---


### 40. [Toward Personal Intelligence Through Cooperative Observation](https://arxiv.org/abs/2608.17128)

**<font color=#1a73e8>作者：</font>** Yashar Talebirad, Osman Jime, Ali Parsaee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A personal AI system needs a model of the user's goals, constraints, and ongoing commitments to plan and act on their behalf, and the quality of that model is bounded by what the system can observe. Broader observation does not by itself improve assistance because a bounded system must select and compress information for the task at hand. We argue that this observation bottleneck has a cooperative structure: the system builds a partial model of the user's changing life, the user evaluates its actions, and the user's consent and control shape what it can observe next. Useful and inspectable behavior can give users a reason to maintain or expand the observation channel, while failures can lead them to correct, narrow, revoke, or abandon it. We use the term cooperative observation for this feedback loop among usefulness, trust, and future access, and propose it as a framework for personal intelligence. We report a preliminary single-subject account from Organizm, a prototype used over six months, and outline evaluation directions for measuring how observation quality shapes personal AI.

---


### 41. [Causal Discovery in Equal Variance Linear Gaussian DAGs via SURE-Tuned Ridge Regression](https://arxiv.org/abs/2608.17132)

**<font color=#1a73e8>作者：</font>** Sambit Mishra, Urbashi Mitra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering the directed acyclic graph (DAG) of a structural equation model (SEM) from observational data is a central problem in causal discovery. The iterative gradient descent and per-problem hyperparameter tuning of continuous-optimization methods are poorly suited to two practically important regimes: the sample-limited regime, where the number of samples is comparable to or smaller than the number of nodes in the DAG, and the compute-limited regime. This work proposes SURE-Ridge, a non-iterative, closed-form estimator for equal variance linear Gaussian SEM. The method performs parallel node-wise regressions with regularization parameters chosen adaptively by Stein's unbiased risk estimate (SURE), and applies an adaptive thresholding procedure to extract a DAG from the resulting soft adjacency matrix. Numerical results show that SURE-Ridge achieves the lowest structural Hamming distance in the small-sample regime and the lowest run time across all sample sizes tested, compared with NOTEARS, DAGMA, and GBNSL baselines.

---


### 42. [Iterative tensor network transformations for element-wise evaluation of elementary and filtering functions](https://arxiv.org/abs/2608.17135)

**<font color=#1a73e8>作者：</font>** Xiao Wang, Tomohiro Hashizume, Pia Siegl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensor networks are powerful formats for compressing large-scale data. However, their application to general data processing has been limited by the difficulty of performing nonlinear operations. Here, we introduce iterative tensor network transformations (ITNTs), a general algorithmic framework for the element-wise evaluation of elementary and nonlinear filtering functions on data encoded as tensor trains (TTs), a class of tensor networks. Our approach operates entirely in the compressed domain, enabling efficient computation on exponentially large datasets while maintaining a controlled computational cost. We demonstrate its power in two key areas: (I) evaluating highly nonlinear elementary and filtering functions on a 3D reactive flow field, enabling high-fidelity reaction rate computation and region filtering, and (II) finding extrema in complex optimization problems, such as solving Max-SAT instances on spaces up to $2^{70}$ configurations. These results establish ITNT as a foundational tool that provides tensor network methods with the capability for general-purpose data science and large-scale optimization.

---


### 43. [Health Inquiry with AI: How Empathetic Expression and Conversational Contexts Shape Users' Communicative Acts](https://arxiv.org/abs/2608.17144)

**<font color=#1a73e8>作者：</font>** Xi Zheng, Xuyu Yang, Can Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As online health information-seeking shifts to conversational AI, high-quality information retrieval increasingly relies on users' ``communicative acts''(proactively sharing and seeking information)---similar to how effective diagnosis and personalized guidance are elicited in patient-clinician communication. Drawing on health communication research, this study examines how a chatbot's modality of empathetic expression (Verbal, Visual, Multimodal) and the conversational context (General, Sensitive, Mental Health) influence these acts through a 2 x 2 x 3 within-subjects experiment (N = 48). The results revealed that while verbal and multimodal empathy significantly increased reply length, communicative acts were largely shaped by conversational context, with Sensitive context triggering more question-asking and Mental Health context leading to heightened concerns, assertive responses, and unprompted information disclosure. Combined with qualitative findings, we discuss design implications for building context-sensitive AI health inquiry systems that can encourage active user participation.

---


### 44. [Protocol-Embedded Compliance for Privacy-Preserving, Non-Custodial Digital Payments](https://arxiv.org/abs/2608.17145)

**<font color=#1a73e8>作者：</font>** Santiago De Simone, Geoffrey Goodell, Georgios Samakovitis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Received wisdom on payments infrastructure strongly supports the custodial, account-based model as a necessity for transaction integrity, auditability and verification; the set of fundamental primitives for regulated digital money exchange, the argument goes, necessitates designated identifiable entities that store and process credentials, perform KYC, and ultimately act as the 'single version of the truth' for compliance remediation and, most important, AML. In this paper, we propose this is not the case, by arguing that non-custodial, cash-like digital assets can embody such capabilities, in an arguably more secure manner.
To that end, we present a reference architecture and core protocol rules for digital-value-exchange systems that preserve meaningful user privacy while enabling strong auditability. The protocol defines the conditions under which digital asset creation, transfer, and redemption are valid. The architecture specifies the allocation of actors, roles and components through which these rules operate, enabling independent verification of transaction compliance with applicable norms. Building upon the Unforgeable, Stateful, Oblivious (USO) asset model of Goodell et al., regulatory compliance data are embedded directly into the asset state as cryptographically signed attestations issued by independent entities. A transfer is valid only upon satisfaction of applicable compliance predicates and inclusion of the resulting signature within the asset state. Compliance enforcement is thus performed at the protocol level rather than through institutional custody or identity-based account control. We conclude that our proposed model can successfully interface with existing payment systems, making it possible to integrate non-custodial, compliance-verified transactions with legacy financial infrastructure.

---


### 45. [Picture the Epsilon: Pursuing Identity-Level Privacy Guarantees for Images](https://arxiv.org/abs/2608.17147)

**<font color=#1a73e8>作者：</font>** Arman Zareian Jahromi, Vishnu Bondalakunta, Mohammad Akbar Bin Shah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Image-to-image face generators are widely used, and visual dissimilarity between their outputs and source images is sometimes treated as evidence of privacy. Auditing whether these systems satisfy formal identity-level (epsilon, delta)-differential privacy requires choosing among several distinct routes for converting embedding-space observations into estimates or bounds on the differential privacy parameter epsilon. We present a comparative study of four such audits applicable to pre-trained, black-box face generators: a Gaussian-mechanism reading of per-identity sensitivity (GaussMech); a per-dimension kernel-density log-ratio aggregated by basic composition (KDE-LR); an analytical population-level lower bound on pure-DP epsilon derived from the maximum mean discrepancy via the total variation distance (MMD-TV); and a hypothesis-testing evaluation of a cross-validated classifier's out-of-fold ROC (ROC-HT). For each method we make explicit its assumptions, hyperparameter dependence, finite-sample limitations, and the regime in which its epsilon estimate is informative. Applied to FaceFusion and InstantID across multiple identity encoders and reference datasets, the audits consistently reveal substantial identity distinguishability while reporting markedly different epsilon estimates that reflect each method's distinct assumptions and finite-sample treatment. In this high-distinguishability regime, the experiments do not support a reliable ranking of the four methods. Their relative trade-offs should be evaluated on partially private mechanisms, which we identify as the natural next study. The resulting framework places these audits in a shared identity-level audit setting and clarifies how their assumptions and finite-sample treatments shape the resulting differential privacy estimates.

---


### 46. [Rapid Debris-Volume Estimation from Post-Hurricane Aerial Imagery](https://arxiv.org/abs/2608.17165)

**<font color=#1a73e8>作者：</font>** Kooshan Amini, Jamie Ellen Padgett, Guha Balakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hurricane debris removal is planned, contracted, and federally reimbursed on the basis of volume estimates, yet operational practice still relies on parametric forecasts with 41-90% documented over-estimation or on truck-load tallies that arrive only after hauling begins. We present DebrisHeightNet, a segmentation-conditioned monocular debris-height network that estimates spatially explicit debris volume from a single pass of post-event aerial RGB imagery, the kind of survey routinely flown within days of a hurricane landfall. We train only a lightweight 1.08 M-parameter head on top of two frozen vision foundation models. This head regresses height from a Depth Anything V2 backbone, conditioned on the debris segmentation of CLIPSeg-debris from our prior work. Because no post-hurricane debris-height ground truth exists, we synthesize the training target by confidence-weighted LiDAR-monocular fusion (CW-LMF), designed to suppress non-debris LiDAR returns. This fused target is a constructed supervision signal rather than ground truth, so we corroborate it against external references rather than claiming it as truth. A region-level power-law calibration, driven by each region's low-density debris fraction, converts model volume into an estimate of the reported hauled debris with quantified uncertainty. Across ten regions spanning five hurricanes and three states, the uncalibrated model agrees with an independent uncrewed-aerial-vehicle (UAV) survey of the training region at Spearman $\rho = 0.87$ and lands within 30% of the reported record where the Hazus and FEMA-hybrid parametric forecasts over-predict it by 2.7-4.8$\times$. Deployment requires no LiDAR, no ground access, and no second flight, so the method can produce spatially explicit volume estimates wherever single-pass post-event imagery is flown.

---


### 47. [Population Health-Based Machine Learning Reveals Associations Between Psychosocial Factors and Chronic Kidney Disease](https://arxiv.org/abs/2608.17174)

**<font color=#1a73e8>作者：</font>** Md. Atik Shams, David Eisenberg, Sumaiya Fatema 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chronic kidney disease (CKD) progresses silently and severely undermines quality of life, making early detection critical for improving patient outcomes. We present a two-part study that combines large-scale telehealth data with advanced machine learning to both classify self-reported CKD status and identify key drivers of disease. Using selected features from the Behavioral Risk Factor Surveillance System (BRFSS 2021: 438,693 samples; BRFSS 2019: 418,268 samples) and the National Health Interview Survey (NHIS 2021: 29,482 samples; NHIS 2020: 31,568 samples), we addressed missing data with nine state-of-the-art imputation methods and mitigated class imbalance via sampling strategies. Our customized stacked ensemble model achieved balanced accuracy of 72.56-76.12%, with corresponding AUROC scores of 79.59-82.29%. SHapley Additive exPlanations (SHAP) analysis, followed by clinical review, highlighted critical predictors, including regular medical check-ups, age, blood pressure, and indicators of mental health stress. These findings deliver a robust and interpretable framework for CKD risk stratification and provide actionable insights into its associated factors.

---


### 48. [The Acknowledgment Point Is the System: Durable Policy-Decision Receipts for AI Audit Evidence](https://arxiv.org/abs/2608.17176)

**<font color=#1a73e8>作者：</font>** Neeraj Kumar Singh Beshane  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An AI audit record is useful only if its durability and trust boundary are explicit. Returning a guarded decision before any durable write minimizes latency, but it cannot guarantee that evidence survives an immediate crash. We rebuild RuntimeGuard-AI around this constraint. The resulting research prototype binds each deterministic policy decision to the exact policy source, commits a privacy-minimizing record at a caller-selected synchronization boundary, and returns an Ed25519-signed receipt that states whether that boundary completed. After restart, the engine validates framed records, manifests, shard placement, sequence continuity, and replay identity. A separate attestation path groups committed records into chained, signed Merkle epochs that an auditor verifies with an externally obtained key. On an Apple M4 Pro at four worker threads and 2,048-byte prompts, buffered signed evidence reaches 27,193 requests/s with 141.9 microseconds median latency. Per-record data and full synchronization reduce throughput to approximately 242 requests/s and raise median latency to 16.0 ms. Sealing a 100,000-record signed epoch takes 97.0 ms. The result is a measured durability-latency trade-off, not a "free" asynchronous audit path. The prototype does not prove model execution, prevent a compromised signer from forking history, or establish legal conformity.

---


### 49. [Mask What Matters: Saliency-Guided Video Self-Supervised Learning for Autonomous Driving](https://arxiv.org/abs/2608.17178)

**<font color=#1a73e8>作者：</font>** Christopher Lang, Alexander Braun, Abhinav Valada  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video self-supervised learning through masked spatiotemporal prediction has emerged as a promising paradigm for learning feature representations from unlabeled data. However, existing methods typically rely on random masking, which indiscriminately removes regions irrespective of their semantic or temporal relevance. In ego-centric driving videos, this can weaken the pretext signal since safety-critical cues such as pedestrians, vehicles, lane boundaries, and dynamic interactions often occupy only a small portion of the frame, yet are central to downstream perception. We introduce V-JEPA4A, a domain-specialized variant of V-JEPA for autonomous driving that is pre-trained on publicly available driving videos with a novel saliency-driven masking policy. It accounts for semantically and temporally relevant context. The proposed policy preserves and predicts context according to semantic importance and temporal relevance, yielding more informative representation learning while retaining the efficiency of masked prediction. We evaluate the resulting encoders on four driving benchmarks spanning tracking, semantic segmentation, and depth estimation. The results demonstrate that V-JEPA4A reduces identity switches on BDD100k MOT by 25% over V-JEPA with random masking, achieves 73.2 mIoU on Cityscapes, and 3.75 RMSE on KITTI-2015 depth, while incurring only ~14% additional pre-training iteration overhead.

---


### 50. [Reinforcement Learning as (Discrete) Potential Theory](https://arxiv.org/abs/2608.17181)

**<font color=#1a73e8>作者：</font>** Christopher Connolly  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) theory fundamentally depends on probability theory through the Markov chain. There is a deep connection between probability theory and potential theory. This paper reviews that connection and explores the potential-theoretic viewpoint for core reinforcement learning representations and algorithms under a fixed-policy assumption. This viewpoint may offer a path for improved sample efficiency and formal constraints that can be applied to RL. When the fixed-policy assumption is relaxed, the linear potential theory framework can be naturally extended to the nonlinear case.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-173](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
