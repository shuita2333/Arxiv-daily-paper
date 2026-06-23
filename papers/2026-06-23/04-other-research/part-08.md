# 📦 其他研究 | 2026年06月23日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

---

### 351. [What Changes When the Interlocutor Is an AI? Interactional Fluency and Linguistic Uptake in L2 Spoken Dialogue](https://arxiv.org/abs/2606.22225)

**<font color=#1a73e8>作者：</font>** Russell Scheinberg, Ameeta Agrawal, Tetyana Sydorenko 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Voice-based AI systems are increasingly used for L2 speaking practice, but evaluations rarely characterize the interactional processes they create. We analyze 78 university learners of German across four sites completing a counterbalanced spot-the-difference task with both a human peer and a real-time AI partner. From diarized ASR transcripts, we extract measures of interactional fluency, linguistic uptake, and learner experience. Human dialogue was faster and more balanced, with many short turns; AI dialogue resembled supported monologue, with fewer, longer turns, reduced learner floor share, and greater within-turn fluency. The AI's verbose, syntactically regular input was associated with greater short-term uptake and stronger syntactic priming after controlling for input volume. Attitudes toward AI improved after the task, and satisfaction was predicted by production fluency rather than uptake. The results show complementary affordances for AI and human dialogue in L2 practice.

---


### 352. [Investigating The Security of Modern AI and Cloud Infrastructure](https://arxiv.org/abs/2606.22237)

**<font color=#1a73e8>作者：</font>** Andrew Adiletta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The widespread deployment of Deep Neural Networks and Large Language Models (LLMs) relies on a foundational assumption of isolation that this dissertation challenges. This work systematically deconstructs security assumptions around AI and modern cloud infrastructure through a taxonomy of interaction levels that ranges from physical memory co-location to remote service interfaces. While significant research has addressed individual attack surfaces in isolation, the security community lacks a unified framework for reasoning about how physical, architectural, and algorithmic vulnerabilities manifest across the modern AI stack. This dissertation addresses that gap by demonstrating practical attacks that exploit assumptions at each layer of abstraction.

---


### 353. [SamatNext v0.2-B: An Exploratory Study of RMS-Normalized Hybrid Decoders for Curriculum Retention in Small Code Models](https://arxiv.org/abs/2606.22248)

**<font color=#1a73e8>作者：</font>** Samat Zharassov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard autoregressive Transformer decoders can often exhibit substantial forgetting under sequential fine-tuning on shifting curriculum distributions. This technical report evaluates SamatNext v0.2-B, an experimental 356M-parameter hybrid sequence decoder that alternates Differential-Attention-style layers with DeltaNet-inspired simplified linear-state mixer layers using RMS normalization and output scale calibration. We study the model under a controlled staged Python code curriculum and compare it with a parameter-matched Transformer baseline. In this setting, SamatNext v0.2-B achieves a 100.0% pass rate on the controlled Stage 5 holdout while retaining 98.8% of adjacent Stage 3 semantic behavior and reaching 12.0% on the Stage 2E early syntax holdout. The strongest Transformer baseline reaches 97.6% on Stage 5 but retains only 6.0% of Stage 3 behavior. Both architectures remain weak on long-horizon early-stage retention, so the result should be interpreted as evidence of an altered retention/plasticity tradeoff in this controlled setting, not as a general solution to catastrophic forgetting. Code, model specifications, evaluation scripts, and result tables are provided for independent verification.

---


### 354. [Evolving Spatial Weights for Cartographic Synthesis](https://arxiv.org/abs/2606.22252)

**<font color=#1a73e8>作者：</font>** Gesiel R. Lopes, Roberto F. da Silva, Mellina Yamamura 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The integration of multiple thematic data layers into a single composite map, known as the cartographic synthesis problem, is typically addressed through expert-driven weighting schemes. This study presents a multi-objective formulation of cartographic synthesis grounded in spatial autocorrelation structure. We develop a bi-objective evolutionary framework, GIS-moGA, that estimates layer weights by simultaneously maximizing global spatial structure, measured by Global Moran's I, and minimizing local spatial heterogeneity, measured by the variance of Local Indicators of Spatial Association (LISA). Because naive evaluation of spatial relationships requires O(N^2) operations, direct computation becomes impractical for larger datasets. We address this challenge by exploiting the 97.7% sparsity of queen contiguity matrices, reducing effective complexity to O(N k) and enabling scalable municipal-level analysis. The framework is evaluated on a high-dimensional spatial epidemiology dataset with N = 523 units from Araraquara, Brazil. A 64-scenario experimental design is used to examine evolutionary behavior across parameter settings. Results show that higher mutation rates are important for maintaining population diversity and preventing premature convergence in spatially autocorrelated fitness landscapes, where crossover operators can disrupt geographically coherent structures. Compared with expert-derived Analytic Hierarchy Process baselines, the resulting Pareto fronts show substantial hypervolume gains and significant improvements in spatial coherence (p < 0.001, Cliff's delta = 0.87). These findings provide a systematic and scalable framework for data-driven geographic multi-criteria decision analysis.

---


### 355. [From Handcrafted Features to Functional Edge Learning: Evolution of EEG Seizure Detection Frameworks](https://arxiv.org/abs/2606.22258)

**<font color=#1a73e8>作者：</font>** Sepideh Kheirollahi, Mohammad Rasoul Roshanshah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalogram (EEG) analysis remains the clinical gold standard for epilepsy diagnosis and seizure detection. While Deep Learning (DL) has significantly advanced automated EEG interpretation, its transition from controlled experimental settings to routine clinical deployment is severely bottlenecked by fundamental architectural flaws. Standard DL models operate as opaque black-boxes lacking clinical interpretability, demand massive amounts of balanced annotated data, and incur steep computational costs incompatible with resource-constrained wearable or implantable neuromodulation devices. This paper presents a comprehensive review of these prevailing limitations and explores Kolmogorov-Arnold Networks (KANs) as a emerging paradigm for EEG-based seizure detection. By replacing the fixed activation functions of traditional neurons with flexible, learnable functions along the network's connections, KANs bridge the critical gap between predictive accuracy and mathematical transparency. We systematically analyze how KAN architectures resolve the shortcomings of traditional DL-based models by offering exceptional parameter efficiency, inherent interpretability for physician trust, and robust performance under data scarcity. Ultimately, this review establishes KANs not merely as an incremental algorithmic update, but as a fundamental paradigm shift necessary to actualize next-generation, patient-specific, and thoroughly transparent clinical EEG monitoring systems.

---


### 356. [MixedPEFT: Combining Multiple PEFT Methods with Mixed Objectives for Unsupervised Domain Adaptation](https://arxiv.org/abs/2606.22272)

**<font color=#1a73e8>作者：</font>** Mohammed Rawhani, Dervis Karaboga, Ozkan Ufuk Nalbantoglu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pre-trained language models struggle when applied to new domains, as full fine-tuning is computationally expensive and prone to catastrophic forgetting. This study addresses this challenge by presenting a novel parameter-efficient strategy for unsupervised domain adaptation that combines custom PEFT architectures with mixed-objective training. Our approach simultaneously optimizes classification performance on labeled source domain data and masked language modeling (MLM) on unlabeled target domain data, preserving target domain knowledge while adapting to source domain tasks. Our method employs a custom union of invertible adapters and Low-Rank Adaptation (LoRA) within a unified parameter-efficient framework. Through comprehensive evaluation on the Multi-Genre Natural Language Inference (MNLI) dataset across 20 domain shifts, our approach achieves significant improvements over existing methods: 1.41 percentage points over the current parameter-efficient state-of-the-art UDapter, 1.26 percentage points over the fully-tuned DANN baseline, and 0.86 percentage points over DSN, while utilizing only 7% of the model's trainable parameters. These results establish new benchmarks for parameter-efficient unsupervised domain adaptation and demonstrate that carefully designed PEFT combinations with concurrent optimization can outperform both existing parameter-efficient methods and traditional fully-tuned approaches.

---


### 357. [From Speech to Text Corpora: Evaluating ASR-Based Data Acquisition for Low-Resource Fongbe and Hausa](https://arxiv.org/abs/2606.22274)

**<font color=#1a73e8>作者：</font>** Mahounan Pericles Adjovi, Victor Olufemi, Roald Eiselen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource African languages lack text corpora needed for language model training. We investigate whether ASR pipelines can extend text resources for two typologically distinct West African languages: Fongbe (tonal, diacritic-rich) and Hausa (non-tonal). We fine-tune MMS-300M on a curated 12.3-hour Fongbe dataset, achieving 9.48% WER on the ALFFA benchmark - a 78% relative reduction from the prior 44.04% baseline - while preserving tonal diacritics critical to the language. For Hausa, we apply an existing fine-tuned Whisper-Small model. We catalog 1,553 YouTube videos (236 hours) and process a subset of 424 videos (45.49 hours) selected to balance domain diversity with available computational resources, producing 6,770 transcribed segments. Human evaluation on 50 randomly sampled segments per language shows mean quality scores of 57.4/100 for Hausa and 36.5/100 for Fongbe, indicating that while Hausa transcriptions approach acceptable quality for corpus construction, Fongbe transcriptions require post-processing or improved models for production use. We release the curated dataset, fine-tuned model, transcribed corpus, and full video catalog following platform terms and ethical guidelines.

---


### 358. [Efficient Document Tampering Localization with Multi-Level Discrepancy Features and Unified DCT-Quantization Embedding](https://arxiv.org/abs/2606.22285)

**<font color=#1a73e8>作者：</font>** Mohamed Dhouib, Ye Zhu, Sonia Vanier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Localizing document tampering is extremely challenging, as manipulations are crafted to appear visually consistent and often leave only subtle traces that are nearly invisible to the human eye. In prior work, evaluation has been largely dominated by synthetic benchmarks that closely match the training distribution, and methods have shown steady progress under this setting. However, these gains often translate poorly to human-made forgeries and to cross-domain evaluation, where both the source documents and the tampering pipeline can change, leading to a distribution shift. In addition, since the introduction of the Frequency Perception Head for the discrete cosine transform (DCT) modality, it has become a standard choice, and subsequent work has largely focused on downstream modules and fusion strategies rather than revisiting the backbone itself. To help close this gap in cross-domain performance and improve the DCT backbone design, we propose \textbf{DiffNet}, a relatively simple yet effective RGB--DCT early-fusion architecture driven by two key design choices. First, to ensure that the decoder aggregates multi-scale inconsistency evidence rather than operating on raw, content-heavy activations, we apply a lightweight multi-level discrepancy transformation at the output of each backbone stage, replacing features with magnitude-only responses to learned zero-sum filters. Second, we design an efficient DCT-domain backbone that relies on a lightweight frequency-index-aware DCT--quantization joint embedding. Our approach achieves state-of-the-art performance on cross-domain and human-made document tampering localization, outperforming prior methods by around 30\%, with up to $7\times$ higher throughput than the previous best model.

---


### 359. [Control-Aware Manipulation of ArduPilot via Legitimate MAVLink Commands: Simulation and Hardware Validation](https://arxiv.org/abs/2606.22289)

**<font color=#1a73e8>作者：</font>** Feras Benchellal andLotfi Ben Othmane, Yasaswini Konapalli, Cihan Tunc 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper investigates control-aware attacks against ArduPilot-based Unmanned Aerial Vehicles (UAVs), inwhich an adversary exploits the sensitivity of flight-controller dynamics to parameter changes to cause loss of control and crashes. It describes six attacks that exploit interactions among multi-layer controllers by modifying Proportional-Integral-Derivative (PID) gains, altering Extended Kalman Filter (EKF) estimation configuration, and violating failsafe assumptions, thereby forcing ArduPilot into unsafe operating conditions. We evaluate the attacks in Software-in-the-Loop (SITL) simulation and validate them on a Pixhawk 2.4.8 hardware platform. The results show that short sequences of well-formed MAVLink messages can exploit controller sensitivity to parameter values and updates frequency, affecting controller states and degrading attitude stability, angular-rate behavior, trajectory tracking, and estimator health. We demonstrate that when multiple effects are combined, the vehicle can enter an unsafe state and crashes. These findings show that security gaps in input-parameter handling, command trust, and controller-state validation can be exploited to cause loss of control and crashes in UAVs.

---


### 360. [SCENIC: Semantic-Conditioned Edge-Aware Neural Framework for Structured IoT Command Generation](https://arxiv.org/abs/2606.22296)

**<font color=#1a73e8>作者：</font>** Luke Ztz Hu, Hongbing Lang, Songping Mai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge Internet of Things (IoT) agents are often constrained by memory capacity, privacy requirements, communication latency, and recurring inference cost. Current smart-home assistants commonly rely on API-level command interfaces or cloud-based language models that remain difficult to deploy on edge devices. This paper addresses edge IoT command generation as a many-to-one structured output task, where multiple natural-language instructions map to the same canonical command string for deterministic smart-home parsing. To support this setting, we propose Semantic-Conditioned Edge-Aware Neural Framework for Structured IoT Command Generation (SCENIC), an end-to-end framework covering model architecture selection, Smart Home Instruct data generation, triplet-loss contrastive supervised fine-tuning, pruning and quantization, and deployment-oriented export. We evaluate sub-0.2B-scale transformer backbones, which are, to the best of our knowledge, among the smallest language-model backbones studied for edge IoT structured command generation. On Smart Home Instruct-Bench, the strongest dense decoder-only row reaches 99.0% EM@1, while the encoder-decoder model retains stronger high-sparsity behavior. A representative pruned INT8 encoder-decoder export preserves 91.0% EM@1 and 99.0% EM@5 while reducing exported model size by 25.38%. TensorRT profiling of the NVIDIA 2:4 sparse encoder export further shows up to 1.8x encoder-component speedup, indicating that the selected encoder-decoder deployment path can retain structured command accuracy under edge-oriented compression while hardware acceleration evidence remains component-level. The SCENIC code and experimental artifacts are open sourced to support reproducibility.

---


### 361. [Towards Accurate and Robust Surveillance Roadside IVD via Trackletized Audio-Visual Reasoning](https://arxiv.org/abs/2606.22299)

**<font color=#1a73e8>作者：</font>** Xiwen Li, Xiaoya Tang, Bodong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Idling Vehicle Detection (IVD) seeks to determine, at the final frame of a video clip, whether any vehicle is idling, meaning the vehicle is stationary with its engine running, using synchronized video from a remote surveillance camera and multichannel audio captured by spatially distributed wireless microphones along the roadside. Prior full-image, clip-level fusion approaches tend to overfit scene background and full-frame context, produce unstable temporal decisions, and lack an explicit spatial prior to align vehicles with microphones, which makes them brittle under domain shift and data inefficient. Instead, we introduce TAVR-IVD, an audio-visual framework guided by multi-object tracking. Our method detects vehicles, links detections into tracklets, and classifies each vehicle by operating on its tracklet. This design raises the effective signal-to-noise ratio, stabilizes temporal decisions through tracklets, enforces an explicit spatial prior to align vehicles with microphones, and adapts across domains with limited calibration annotations while remaining detector agnostic and efficient. To evaluate deployment robustness, we further curate two evaluation extensions, AVIVD-LT and AVIVD-M, covering inter-day and cross-site shifts.

---


### 362. [Enhancing Protein Representation Learning via Manifold Restore Mixing](https://arxiv.org/abs/2606.22307)

**<font color=#1a73e8>作者：</font>** Yizhou Dang, Chuang Zhao, Lianbo Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data augmentation (DA) has been proven to be an effective means for improving protein representation learning (PRL) by generating additional training samples. Although mainstream perturbation- and sampling-based augmentation methods can produce data containing sufficient variations, they carry the risk of disrupting the protein structure and function. Some crafted protein homology modeling tools can generate conformations, but reduce structural diversity. The above dilemmas lead us to a question: Can we restore the disrupted structure caused by DA operations, providing data with both the original structure and diverse variations? In this work, we first analyze and empirically reveal the structure defect and performance degradation issues of existing DA methods. Based on the findings, we propose a simple yet effective DA method, Manifold Restore Mixing (MRM), for protein representation learning. Specifically, inspired by manifold mixup, we mix the hidden representations of original and augmented protein data to generate new samples that restore structural information lost in DA while introducing diverse variations. Furthermore, we develop a sample difficulty scheduler that adjusts the beta distribution in mixup to provide models with progressively challenging mixed samples during training, which improves the final performance. Comprehensive experiments on various PRL backbones and downstream tasks demonstrate the effectiveness and generalization of our method. The complete code and weights will be released upon acceptance. We provide a implementation at this https URL.

---


### 363. [Semantic Non-Assembly: Privacy by Architectural Inertness Under Component Exposure](https://arxiv.org/abs/2606.22311)

**<font color=#1a73e8>作者：</font>** Sam Ryan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing privacy frameworks emphasize confidentiality, access control, appropriate information flow, or statistical disclosure limitation. We introduce a complementary class of privacy guarantee (Semantic Non-Assembly) in which privacy is characterized not by the difficulty of achieving exposure but by the information yield of exposure when it occurs. SNA prevents evaluation of a designated predicate by preventing any sub-threshold coalition from assembling a sufficient assignment to its input domain. An architecture satisfies Semantic Non-Assembly when no coalition of fewer than a defined threshold of components can assemble such an assignment: complete exposure and decryption of any sub-threshold component yields no actionable data. In the base protocol, the guarantee is structural: it operates through architecture, not policy, and its privacy properties degrade predictably under component compromise rather than collapsing at a single point. The reference instantiation combines this structural guarantee with audited organizational constraints, as characterized in Appendix A. This paper formalizes the guarantee and establishes four ProVerif-verified properties: Device Non-Correlation, Registry Observer Non-Identification, Submission Server Blindness, and Active Defense Gate correctness, the first three through a two-channel provenance architecture. The Birthmark Standard instantiates the guarantee on constrained capture hardware, demonstrating deployability where ZK-based approaches are computationally infeasible. All formal properties and scope limitations are documented in Appendix A.

---


### 364. [Diffusion Integrated Gradients: Controllable Path Generation for Flexible Feature Attribution](https://arxiv.org/abs/2606.22314)

**<font color=#1a73e8>作者：</font>** Soyeon Kim, Kyowoon Lee, Jaesik Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Path-based attribution methods such as Integrated Gradients (IG) are widely adopted for their strong axiomatic properties and effectiveness in attributing model predictions to input features by integrating gradients along a path from a baseline to the input. However, the choice of the attribution path largely affects the quality of explanations, and existing approaches rely on fixed or hand-crafted paths that often produce noisy or distorted attributions. To address this limitation, we propose Diffusion Integrated Gradients (DiffIG), a novel method that reformulates path generation as a conditional generative modeling problem. DiffIG first trains a diffusion model to learn a distribution over paths generated from a Stick-Breaking Process, then employs guided sampling to embed user guidance during the sampling procedure. We demonstrate that DiffIG quantitatively matches or outperforms existing path-based methods, achieving perceptually aligned explanations. This work introduces a new generative perspective for flexible, inference-time controllable Explainable Artificial Intelligence (XAI) methods.

---


### 365. [All Routes Lead to Collapse](https://arxiv.org/abs/2606.22325)

**<font color=#1a73e8>作者：</font>** K. R. Balasubramanian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention sinks, representation collapse, and norm stratification are treated as transformer-specific pathologies. We show they are not specific to attention: they are what content-based routing does under a fixed similarity metric. We give a reframing identity: softmax attention is Boltzmann-weighted aggregation over Euclidean distances with constant key norms, so its score omits a $-\|k\|^2$ term and is blind to key magnitude. This predicts that any router whose metric is ill-matched to its representations should compensate, by concentrating its routing and collapsing the routed representations. We test it on routers that score and aggregate over different axes: softmax attention over tokens (nine pretrained transformers), graph attention over nodes, a selective state-space model and a recurrent mixer over time, and learned residuals over depth. All develop the same signature, and two within-model ablations show it is caused by the routing mechanism rather than by incidental dynamics. The form is contingent, set by the strength of the positional brake each router carries alongside its content score; we sweep that brake and move the onset across its whole range. The mechanism is not contingent, and it does not require norm stratification: a router with norm-normalized keys concentrates just the same. We do not claim these models implement Riemannian geometry; the geometric view is a diagnostic that names the inadequacy of the flat, norm-blind metric.

---


### 366. [T-IMPACT: A Severity-Aware Benchmark for Contextual Image-Text Manipulation](https://arxiv.org/abs/2606.22339)

**<font color=#1a73e8>作者：</font>** Gagandeep Singh, Aaditya Yadav, Priyanka Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision-language models and generative editing systems have made it increasingly easy to produce persuasive multimodal misinformation by altering images, text, or both jointly. However, existing datasets focus mainly on authenticity, out-of-context mismatch, or manipulation type, and rarely capture how strongly an edit changes the likely interpretation of a post. We introduce T-IMPACT, a first-release severity-aware benchmark for manipulated news-style image-text pairs. T-IMPACT contains 98,786 examples spanning pristine, image-only, text-only, and joint manipulations, with a calibrated continuous severity signal, coarse low/medium/high labels, and supporting grounding metadata. Starting from a news image-text pair, the pipeline extracts semantic anchors, grounds them spatially, performs localized image edits and constrained caption rewrites, and calibrates contextual-impact scores using limited human ratings. In this release, the calibrated continuous score is the primary severity target, while the low/medium/high bands should be interpreted as coarse operating buckets rather than balanced classes. Experiments show that current models recover some authenticity signal, but severity prediction remains substantially harder and only weakly aligned with human judgment. T-IMPACT provides an initial benchmark for studying multimodal manipulation beyond binary real/fake classification toward graded contextual impact.

---


### 367. [A Post-Quantum Secure Lattice-Based Forward-Secure Identity Based Encryption with Applications to Internet of Things Architecture](https://arxiv.org/abs/2606.22340)

**<font color=#1a73e8>作者：</font>** Abhishek Kumar, Vikas Srivastava, Sumit Kumar Debnath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of the Internet of Things (IoT) has led to an unprecedented scale of data exchange across heterogeneous and resource-constrained devices. Ensuring confidentiality and secure key management in such environments is challenging. Traditional public-key infrastructures require heavy certificate-handling overhead. Identity-Based Encryption (IBE) offers a lightweight alternative by deriving public keys directly from device identities, making it attractive for IoT deployments. However, IoT devices are highly vulnerable to side-channel and key-extraction attacks, motivating the need for Forward-Secure IBE(FS-IBE), where the compromise of a current secret key does not threaten past communications. Existing FS-IBE constructions based on classical hardness assumptions are not secure in the era of post-quantum, while the lattice-based (LWE-based) forward-secure scheme suffer from large key and ciphertext sizes, limiting their suitability for constrained IoT systems. Here, we propose a new lattice-based fs-IBE scheme in the ring setting, relying on the RLWE assumption to achieve post-quantum security and significant efficiency gains. Our design uses trapdoor delegation with a minimal-cover mechanism over a binary tree. It results in compact public parameters and efficient per-epoch key updates. Compared to prior LWE-based constructions, our scheme reduces public key, secret key, and ciphertext sizes, and thus, making it better suited for practical IoT environments.

---


### 368. [How Does Research Evolve? Tracing Cross-Domain Trajectories in NLP, ML, and CV with Claim-Grounded Typed Citations](https://arxiv.org/abs/2606.22342)

**<font color=#1a73e8>作者：</font>** Abdul Muntakim, Md Abdullah Al Hafiz Khan, Sadid Hasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How does research evolve, and what substrate would let us forecast where it goes next? Scientific progress is not simply a uniform accumulation of facts: ideas extend prior methods, address known limitations, realize proposed future directions, and sometimes dispute earlier claims. Existing citation graphs usually collapse these roles into a single homogeneous edge type, limiting how we can analyze scientific progress. We address this gap by proposing the SciTraj corpus, the first claim-grounded typed citation graph in which each edge is linked to the specific claim sentence that motivates it. Claim-bearing sentences are extracted from paper sections; four claim-driven relations are verified by NLI entailment against in-paper context, while two similarity-only relations are gated by abstract cosine and year-gap rules. SciTraj contains 32,559 papers from NLP, ML, and Vision (2015--2024), connected by 573,126 directed edges across six relation types, with NLI-verified claim seeds. Using SciTraj, we identify disciplinary siloing in typed citation flow and topic emergence concentrated in Vision and LLM-related work. The corpus also contains 287M typed trajectories of length $\geq 3$, covering 72.8% of papers, and supports a temporally split typed link-prediction benchmark. A year-shuffle falsifiability test separates temporal structure from year-correlated content, and a 3-annotator pilot reports $\kappa = 0.74$ with 79.9% precision.

---


### 369. [Customizing Video Portraits via Identity-ActionDecoupling](https://arxiv.org/abs/2606.22347)

**<font color=#1a73e8>作者：</font>** Junxiong Lin, Haoran Wang, Xinji Mai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity-Preserving Text-to-Video Generation (IPT2V) seeks to synthesize a temporally coherent video from a reference image and a textual description, while simultaneously preserving the subject's identity and allowing fine-grained control over facial dynamics. Although recent methods such as ID-Animator and ConsisID inject identity features only at inference time, they ignored the ID-irrelevant information contained in Facial embedding, leading to monotonous or inaccurate facial movements that poorly follow the prompt. We introduce Identity-Action Decoupling (IaD) framework as well as two loss function Identity Decoupling Loss and Text Alignment Loss to solve this problem. Without any subject-specific fine-tuning, IaD yields videos that (1) maintain cross-temporal identity consistency and (2) exhibit rich, controllable expressions and scene variations that closely match the input text.

---


### 370. [Select-to-Act: Hierarchical Reinforcement Learning via Adaptive Language Guidance](https://arxiv.org/abs/2606.22350)

**<font color=#1a73e8>作者：</font>** Hanping Zhang, Adam Koziak, Yuhong Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has been widely applied to sequential decision-making, yet it often suffers from poor sample efficiency due to costly interactions with the environment. A limited line of recent work has started exploring improving RL efficiency by leveraging external knowledge expressed in natural-language instructions. However, the few existing approaches typically treat the entire instruction as a single conditioning input, failing to account for the stage-dependent nature of language guidance, especially in complex environments. In this paper, we propose \emph{Hierarchical Reinforcement Learning with Language Instructions (HRLLI)}, a hierarchical RL framework that explicitly models natural-language instructions as dynamically selectable semantic guidance during decision-making. HRLLI decomposes instructions into a set of piecewise guidance elements, where each instruction piece may become relevant at different stages of interaction with the environment. A novel hierarchical RL policy structure is then formulated in a \emph{Select-to-Act} paradigm: a high-level semantic policy acts as a guidance selector that selects the most relevant instruction piece to the current state to guide the low-level agent's decision, while a low-level policy executes environment actions conditioned on the selected guidance. The two-level policies are learned simultaneously to maximize augmented expected returns from interactions with the environment. This design enables the agent to adaptively ground language instructions into stage-specific decisions during interaction. Experiments on the instruction-intensive RTFM benchmark show that HRLLI consistently outperforms strong instruction-conditioned RL baselines, demonstrating that explicitly modeling adaptive instruction selection significantly improves the effectiveness of RL.

---


### 371. [Reliability-Guided Adaptive Ensembling for Robust Test-Time Adaptation](https://arxiv.org/abs/2606.22351)

**<font color=#1a73e8>作者：</font>** Adam Koziak, Yuhong Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) can mitigate domain shift without source data, but it is highly brittle under adversarially contaminated test streams, where corrupted inputs also destabilize online updates. We study robust test-time adaptation (RTTA) in the adversarial-stream setting, which remains comparatively underexplored relative to standard TTA, and propose SAFER (Stochastic Augmentation Framework for Enhanced Robustness), a training-free reliability-guided augmentation wrapper for RTTA. SAFER preserves the wrapped TTA objective while replacing brittle single-view predictions with a reliability-guided pooled predictor. For each test sample, SAFER generates stochastic augmentations and aggregates their predictions through correlation-weighted pooling with outlier detection. We further study an adaptive-mixing extension that improves clean-performance retention by adjusting original-versus-augmentation weighting using feature disagreement signals. We evaluate on PACS, VLCS, and OfficeHome under PGD attacks at various attack rates. Across benchmarks, SAFER improves resilience of TTA methods to adversarial attacks while maintaining competitive clean performance.

---


### 372. [Interest Entanglement: The Hidden Barrier to Blind Super-Resolution Optimization](https://arxiv.org/abs/2606.22353)

**<font color=#1a73e8>作者：</font>** Junxiong Lin, Xinji Mai, Qianyu Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fidelity and perceptual quality are two inherently competing and conflicting objectives in the image super-resolution (SR) task. Different loss functions focus on these objectives to varying extents. Regression losses enhance the model's fidelity but lack sufficient attention to high-frequency details, resulting in a loss of fine details. In contrast, perception losses improve the model's visual quality but may introduce undesirable artifacts. Balancing these two optimization goals can be viewed as a Multi-Objective Optimization problem. Existing methods are limited to cautiously adjusting weight parameters between these losses, overlooking the underlying Interest Entanglement problem. To address this problem, we explore the inherent frequency-domain conflict between the regression objective and the perceptual objective, and analyze the causes of Interest Entanglement in SR tasks. According to our findings, we propose the Shared-Feature-Representation based Super-Resolution framework (SFR), which decouples the learning process of different optimization objectives, allowing the model to explore a common optimization direction for both goals and achieve an effective balance between them. To better leverage shared features, we also proposed the InfoSqueeze module, which filters redundant information through a dimensionality reduction and expansion process, effectively transforming features into a consistent space. Quantitative and qualitative experiments across five representative datasets affirm the superiority of SFR.

---


### 373. [ORBIT: Training-Free Multi-Attribute Behavioral Steering via Orthogonal Subspace Rotation](https://arxiv.org/abs/2606.22357)

**<font color=#1a73e8>作者：</font>** Narges Ghasemi, Amir Ziashahabi, Salman Avestimehr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are widely used in assistant settings, where controlling behavioral attributes is often essential. Activation steering modifies hidden-state representations at inference time, providing a lightweight, training-free mechanism that can be toggled at runtime. Existing methods, however, have focused primarily on steering a single attribute at a time. When multiple attributes must be controlled simultaneously, naive summation of per-attribute steering vectors suffers from norm imbalance and directional cancellation, while classifier-based approaches require retraining whenever the attribute set changes. We introduce ORBIT (Orthogonal Rotation-Based Intervention Technique), a training-free extension of rotation-based steering to the multi-attribute setting. Our method constructs a joint subspace from per-attribute steering planes via singular value decomposition and applies a single norm-preserving rotation within that subspace toward a combined target direction. Adaptive per-token gating identifies which attributes need correction at each position, and an optional additive boost strengthens attributes with weak initial projection. We also introduce TraitFactory, a new multi-attribute benchmark that focuses on behavioral tendencies rather than surface-level style. We evaluate ORBIT on TraitFactory and ToneBank across three models (Llama-3.2-3B, Qwen-2.5-7B, Llama-3.1-8B) while steering multiple attributes simultaneously, showing that it achieves stronger and more balanced multi-attribute steering than existing training-free baselines while better preserving output coherence.

---


### 374. [Multigrid Training for Molecular Generation using Graph Neural Networks](https://arxiv.org/abs/2606.22377)

**<font color=#1a73e8>作者：</font>** Zixuan Ling, Paula Mercurio, Di Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has demonstrated significant success for modeling biochemical molecular systems, where inputs are commonly represented as graphs or 3D grids. A major challenge is that computational cost scales with resolution, making full graph/grid computation of molecular densities expensive and often unstable. We introduce a multigrid training strategy that leverages low-resolution optimization to accelerate learning at higher resolution through parameter transfer across discretizations. For graph molecular representations, we progressively transfer parameters learned from a coarse graph to a sequence of increasingly finer graphs via biased random walk upsampling. For 3D molecular generation, we voxelize the molecular structures at multiple resolutions, pretrain a coarse-resolution conditional Variational Autoencoder (CVAE), and initialize a fine-resolution CVAE by transferring shape compatible convolutional parameters from the coarse model. Numerical experiments on receptor-conditioned 3D Ligand generation show that multigrid training accelerates convergence and improves generalization compared to training from scratch.

---


### 375. [Following the Flow: Advection-Consistent Modeling for Event-based Small Object Detection](https://arxiv.org/abs/2606.22378)

**<font color=#1a73e8>作者：</font>** Wen Guo, Fulong Cai, Wuzhou Quan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras enable high-frequency visual perception with microsecond latency, offering advantages for dynamic scenes. However, event-based small object detection remains challenging due to sparse asynchronous measurements and weak object responses that are easily disrupted by noise. Limited spatial support causes small-object signals to lose temporal continuity, resulting in fragmented and unstable predictions. To address this issue, we propose a physics-guided advection-consistent modeling framework, termed PACT, which formulates event evolution as a motion-driven feature transport process. Instead of relying solely on local spatio-temporal aggregation, PACT propagates features along estimated velocity fields and enforces trajectory-level consistency through advection constraints. This design preserves weak event responses over time and prevents their degradation under complex background interference. Technically, PACT integrates motion-aware feature extraction with a differentiable advection-based transport operator, enabling coherent motion representation and effective noise suppression during temporal evolution. Extensive experiments on benchmark event-based datasets demonstrate that PACT consistently outperforms state-of-the-art methods, achieving improvements of 20.72\% in IoU and 15.03\% in accuracy while maintaining comparable computational efficiency. The code is publicly available at this https URL.

---


### 376. [Bypassing Minimization Bias: A Shift-Invariant Variance Estimator for Off-Equilibrium Local Learning Coefficients](https://arxiv.org/abs/2606.22389)

**<font color=#1a73e8>作者：</font>** Yingjia Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Singular Learning Theory leverages the Local Learning Coefficient (LLC) to quantify the geometry of neural network loss landscapes. However, mean-energy LLC estimators depend explicitly on an additive loss baseline, typically an estimate of the local minimum. During transient, off-equilibrium training phases, this minimum is unknown; substituting it with the lowest noisy mini-batch loss induces a systematic minimization bias that distorts the geometric measurement. In this paper, we propose the Shift-Invariant Variance Estimator (SIVE), a variance-based local LLC probe that structurally eliminates the unknown additive baseline through the variance operator. Combining this shift-invariant observable with an explicit correction derived from the Law of Total Variance, SIVE separates geometric loss fluctuations from mini-batch evaluation noise. Controlled experiments on analytically tractable toy models show that SIVE recovers the expected finite-temperature geometric signal in regimes where anchored mean estimators fail. Applied to deep neural networks, SIVE provides a robust, localized online diagnostic for tracking structural phase transitions throughout training.

---


### 377. [Curvature-Adaptive Consistency Flow Matching: Autonomous Trajectory Optimization via Reinforcement Learning](https://arxiv.org/abs/2606.22394)

**<font color=#1a73e8>作者：</font>** Songtao Tian, Guhan Chen, Bohan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Consistency distillation has significantly accelerated the inference of diffusion models. In this work, we reveal an intriguing asymmetry: while Logit-Normal sampling priors are highly efficacious for standard iterative generation, consistency distillation exhibits a distinctly different difficulty profile (e.g., U-shaped). We identify that the primary optimization bottlenecks reside at the boundary stages (initialization or final refinement) rather than the intermediate steps. To address the limitations of static sampling in accommodating evolving learning requirements, we propose Curvature-Adaptive Consistency Flow Matching (CACFM). By formulating distillation as a dynamic decision process, CACFM employs a lightweight Reinforcement Learning agent to actively probe Probability Flow ODE trajectories, automatically constructing an efficiency-oriented curriculum that prioritizes critical regions without manual scheduling. Integrated with a novel Flow Distribution Matching Distillation (DMD) objective, our approach achieves new state-of-the-art results on large-scale models such as FLUX and SDXL. It effectively mitigates structural deformities and preserves high-frequency details in extreme few-step regimes, achieving unprecedented visual fidelity.

---


### 378. [Multi-cancer detection using a computationally efficient CNN with transfer learning](https://arxiv.org/abs/2606.22400)

**<font color=#1a73e8>作者：</font>** Vasileios E. Papageorgiou, Georgios Petmezas, Dimitrios-Panagiotis Papageorgiou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study introduces a computationally efficient convolutional neural network (CNN) architecture enhanced with transfer learning for multi-cancer detection using biomedical images. The proposed lightweight CNN model is designed to reduce computational complexity while maintaining high classification performance, making it suitable for deployment in resource-constrained environments. We evaluate this approach on three distinct tumor datasets comprising brain magnetic resonance imaging (MRI) and lung and kidney computed tomography (CT) scans. The model achieves test accuracy of 90.85 +- 2.22%, 98.64 +- 2.43% and 99.92 +- 0.08% for brain, lung, and kidney cancer classification, respectively, using 5-fold stratified cross-validation (CV). Transfer learning is employed by pretraining the model on one cancer type and fine-tuning it on the others, requiring only 20 additional epochs to achieve performance comparable to models trained from scratch. The fine-tuning process involves updating the classification part of the CNN and requires approximately 0.014 seconds per image per epoch using an NVIDIA GeForce GTX 960. Comparative evaluations show that the proposed model outperforms several state-of-the-art pretrained architectures, such as Xception, VGG16, VGG19, MobileNetV2 and DenseNet121. Overall, the model's effectiveness is evaluated across three types of cancer with distinct morphological characteristics, assessing its performance on both MRI and CT imaging modalities and demonstrating robust performance across diverse tasks and data types. These findings underscore the potential of streamlined deep learning (DL) frameworks in accelerating cancer diagnosis without sacrificing accuracy, especially in settings with limited computational resources.

---


### 379. [Asymptotic Signal Subspace Recovery in Softmax Attention Models](https://arxiv.org/abs/2606.22406)

**<font color=#1a73e8>作者：</font>** Lan V. Truong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention mechanisms have demonstrated remarkable empirical success in identifying relevant information from large collections of tokens, yet the theoretical principles underlying this behavior remain poorly understood. We study a stylized softmax-attention model in which a query vector is learned by stochastic gradient ascent from a collection of informative and nuisance tokens. Exploiting the symmetry of the model, we derive a population objective and characterize the limiting ordinary differential equation governing the learning dynamics. Using tools from stochastic approximation and dynamical systems theory, we establish a rigorous connection between the stochastic learning algorithm and its deterministic limit. Our main result shows that, under suitable high-dimensional scaling assumptions and standard step-size conditions, the learned query converges almost surely to the one-dimensional signal subspace spanned by the latent informative direction. Equivalently, the query asymptotically recovers the latent signal up to the intrinsic sign ambiguity. These results provide a rigorous theoretical foundation for understanding attention mechanisms as signal extraction procedures in high-dimensional noisy environments and offer a dynamical-systems perspective on how attention discovers relevant information in the presence of substantial noise.

---


### 380. [Gen2Balance: Generative Balancing for Long-Tailed Video Action Recognition](https://arxiv.org/abs/2606.22416)

**<font color=#1a73e8>作者：</font>** Prajwal Gatti, Simon Jenni, Fabian Caba Heilbron 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the problem of training on long-tailed data for video action recognition. We propose to augment the training set using a text-to-video generative model, conditioned on diverse text prompts grounded in action profiles and training exemplars. Our approach, called Gen2Balance, converts an imbalanced training set into a balanced combination of real and generated video clips. To effectively learn from such data, we employ a two-stage training strategy that mitigates domain shift and yields significant improvements. We evaluate on long-tailed versions of standard benchmarks: UCF-101 (UCF-LT) and a 100-class subset of Kinetics (K100-LT) selected to prioritise temporally challenging actions. Gen2Balance improves accuracy over the strongest baselines for long-tailed learning by 5.1% and 7.0% on the respective datasets. On rare actions from the RareAct dataset (e.g., cut keyboard), Gen2Balance improves accuracy by 31.9%, demonstrating effectiveness for scarce actions. By varying the amount of synthetic data added, we show that partial balancing already achieves 79% of the performance gains at 27% of the compute cost on K100-LT, highlighting the practical scalability of Gen2Balance.

---


### 381. [Code Isn't Memory: A Structural Codebase Index Inside a Coding Agent](https://arxiv.org/abs/2606.22417)

**<font color=#1a73e8>作者：</font>** Ishaan Bhola, Adithyan Krishnan, Sravanth Kurmala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents now interleave LLMs with retrieval over the working repository, and retrieval implementations vary widely across deployed harnesses. Inside a fixed coding-agent harness on a fixed model, does adding a structural codebase index actually change cost or resolve? We ran three arms (the harness with the index, the same harness without it, and an agentic-grep comparator) on SWE-PolyBench Verified and SWE-bench Pro with Claude Opus 4.7 held fixed throughout, across three seeds, inside a leak-audited per-task sandbox. The within-harness ablation produces a large localization gain and a statistically separated resolve gain, with no cost penalty per cell and lower cost per solve. The cross-harness check shows that the index does not regress against an agentic-grep baseline on resolve or localization, again at no cost penalty. We release the per-cell exclusion ledger, the leak-audit script, the localization extractor, and the results database. The deployment question for a structural codebase index is thus not whether it is too expensive to run (across seeds, the index lands at a lower $/solved than agentic grep) but whether the workload includes multi-file changes where structural ranking pays off.

---


### 382. [QeHDC: Hyperdimensional Computing based on Quantum-enhanced binding and SuperClass Construction](https://arxiv.org/abs/2606.22421)

**<font color=#1a73e8>作者：</font>** Yangjie Xu, Hui Huang, Li Ning 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperdimensional Computing (HDC) is a robust computational framework inspired by human cognition characterized by simple and efficient operations within high-dimensional vector spaces. Quantum-enhanced Hyperdimensional Computing (QeHDC) extends classical HDC by leveraging quantum mechanical properties to enhance computational efficiency. In this paper, we propose a novel Quantum HDC framework featuring a one-pass training method, leveraging sinusoidal and quantum encoding to project classical data into quantum amplitude states efficiently. Our framework introduces an innovative reference-state-based quantum binding operation realized via quantum circuits. Furthermore, we propose a density-matrix-based superclass generation strategy employing eigenvalue decomposition to extract critical quantum state features effectively, enabling a more accurate and robust class representation. Experimental evaluations conducted on standard benchmark datasets demonstrate our approach's superior performance, robustness to noise, and computational feasibility compared to traditional classical and existing quantum-enhanced approaches. The results highlight the practical benefits and potential of Quantum HDC for quantum-enhanced classification tasks and pave the way for future advancements in quantum-inspired computational paradigms.

---


### 383. [FlowDec: Temporal Conditional Flow Decorruptor for Robust Continuous Vision-Language Navigation](https://arxiv.org/abs/2606.22424)

**<font color=#1a73e8>作者：</font>** Yufei Zhang, Changhao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires agents to follow natural-language instructions in unseen scenes. While Large Models (LMs) have advanced VLN-CE, their performance remains severely degraded by real-world visual corruptions, a critical yet underexplored domain constraint. We introduce Temporal Conditional Flow Decorruptor (FlowDec), a novel image restoration framework tailored for LM-based VLN-CE. FlowDec integrates a hybrid temporal conditioning strategy to align the generative flow path with historical context and employs action-centroid guided filtering to dynamically assess and integrate outputs. Extensive experiments demonstrate that FlowDec outperforms state-of-the-art decorruption methods in both navigation accuracy and generation latency. Our approach establishes a robust, efficient paradigm for resilient embodied navigation in unpredictable real-world conditions.

---


### 384. [SVGym (SciVerseGym): An Environment for Reinforcement Learning and Bayesian Optimization in Crystal Discovery](https://arxiv.org/abs/2606.22425)

**<font color=#1a73e8>作者：</font>** Bin Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine-learned interatomic potentials now enable efficient atomistic evaluation for interactive materials discovery, yet closed-loop crystal search methods remain fragmented across bespoke pipelines for editing, relaxation, scoring, constraints, and bookkeeping. We introduce SciVerseGym, a Gymnasium-compatible environment for sequential crystal discovery that frames crystal design as a Markov decision process. Agents observe an atomistic structure, apply chemically meaningful edits, and receive feedback from a configurable evaluator. SciVerseGym supports local and global actions, including elemental substitution, lattice perturbation, atomic displacement, vacancy creation, and atom insertion, along with configurable chemical spaces, structure pools, atomistic and graph-based observations, custom rewards, optional relaxation, and stability or phonon-related diagnostics. Each step applies an edit, evaluates the candidate using a machine-learned interatomic potential or any ASE-compatible calculator, and returns the standard (obs, reward, terminated, truncated, info) tuple. By decoupling agent logic from materials infrastructure, SciVerseGym provides an open, reproducible, and extensible testbed for reinforcement learning, Bayesian optimization, evolutionary search, and language-agent workflows in closed-loop crystal discovery. Code is available at: this https URL.

---


### 385. [Escaping the Variance Trap: Jacobian-Free Dynamics for Root-Finding Bilevel Optimization](https://arxiv.org/abs/2606.22433)

**<font color=#1a73e8>作者：</font>** Zhiyu Li, Xi Xuan, Davide Carbone  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many central machine learning tasks, from entropy tuning in reinforcement learning to equilibrating generative adversarial networks, are fundamentally stochastic root-finding problems rather than loss minimization. Yet, they are frequently forced into a minimization framework via squared residuals, introducing a critical flaw we identify as the Variance Trap. Standard bilevel minimization algorithms require estimating hypergradients involving implicit Jacobians; in stochastic settings, these terms act as noise amplifiers, destabilizing convergence. We formalize Root-Finding Bilevel Optimization (RF-BO) as a distinct problem class that bypasses this pathology. We propose a Jacobian-free solution using Two-Time-Scale Stochastic Approximation (TTSA) that updates directly along the root error, structurally avoiding variance amplification. We provide the first non-asymptotic convergence guarantees for TTSA in this setting under Markovian noise. Extensive experiments demonstrate the decisive advantage of this paradigm: compared to squared-residual and implicit-gradient baselines, our framework achieves a 2.6\% top-1 accuracy gain in SimCLR, 17$\times$ faster convergence in non-linear ODE control where baselines fail, significantly improved entropy stability in reinforcement learning, and an 11.1\% quality improvement in generative modeling.

---


### 386. [Distribution-Aware Robust Bilevel Optimization: Quantile-Guided Huber Updates in Two-Timescale Stochastic Approximation](https://arxiv.org/abs/2606.22436)

**<font color=#1a73e8>作者：</font>** Zhiyu Li, Xi Xuan, Davide Carbone  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bilevel optimization (BLO) is fundamental to hierarchical decision-making but suffers from critical instability under heavy-tailed stochastic noise. Existing variance-reduction techniques typically rely on myopic magnitude checks, which fail to distinguish informative geometric signals from impulsive outliers. To resolve this, we propose \textbf{RQ-TTSA} (Robust Quantile-guided TTSA), a distribution-aware framework that leverages historical gradient buffers to estimate rolling quantiles for adaptive Huber-style clipping, effectively preserving local optimization geometry while strictly bounding effective variance. Theoretically, we provide a convergence analysis for quantile-guided TTSA under nonconvex-strongly convex assumptions with infinite-variance noise ($p \in (1,2]$), deriving a rate of $\mathcal{O}(T^{-\frac{p-1}{3p-2}})$ that recovers optimal dependence on the heavy-tailed parameter. Empirically, across six diverse tasks, spanning heterogeneous vision benchmarks, dynamic games under momentum poisoning, and offline reinforcement learning, RQ-TTSA consistently outperforms state-of-the-art baselines by eliminating divergence spikes and ensuring stable convergence. Our method demonstrates significant robustness to hyperparameter variations and incurs negligible computational overhead ($\approx 2.7\%$ increase), validating distribution-aware gradient control as a practical and necessary component for reliable bilevel learning.

---


### 387. [Curvature-aware 3D length estimation of greenhouse cucumbers using RGB-D imaging and cubic spline arc-length integration](https://arxiv.org/abs/2606.22439)

**<font color=#1a73e8>作者：</font>** Manveen Kaur, Rajmeet Singh, Saeed Mozaffri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Commercial greenhouse cucumber production is graded by fruit length, which drives harvest scheduling, labour allocation, and logistics. Manual measurement with thread or caliper is accurate but infeasible at commercial scale. This paper presents CucumberVision, a non-contact length estimation framework using an Intel RealSense D435 RGB-D camera. A YOLO26n instance segmentation model locates cucumbers, and SAM (ViT-B backbone) refines each detection to a pixel-precise mask. Five methods are evaluated under matched conditions: (M1) a dominant-axis skeleton scan-line baseline; (M2) PCA on the bounding-box depth point cloud; (M3) SAM mask with medial-axis skeletonisation; (M4) a hybrid keypoint-guided approach using a YOLO26-pose model predicting five anatomical landmarks (KP0--KP4) with piecewise 3D arc-length; and (M5) a novel medial arc spline method fitting a cubic spline through the 3D medial axis of the SAM mask and computing arc length by trapezoidal integration -- the first such application to elongated vegetable measurement. All methods share five-frame burst depth averaging, colour-stream intrinsic alignment, and adaptive method selection with cascading fallbacks ensuring 100% coverage. A benchmark of 48 captures across seven cucumbers in three size categories (small ~8 cm, medium ~13 cm, large ~25 cm) with thread-based ground truth establishes a significant accuracy hierarchy: M1 (MAPE 9.68%) > M2 (5.31%) > M4 (5.51%) > M3 (5.82%) > M5 (4.13%). M5 significantly outperforms all competitors at Bonferroni-corrected alpha=0.0125. A secondary contribution is identifying a 12--18% length underestimation caused by using depth-stream rather than colour-stream intrinsics after this http URL(this http URL) -- an under-reported error source. The complete system is released open source and runs in real time on a single consumer-grade GPU.

---


### 388. [DreamUV: Unwrap Artist-like UV by End-to-End Flow Matching](https://arxiv.org/abs/2606.22445)

**<font color=#1a73e8>作者：</font>** Quanyuan Ruan, Jiabao Lei, Xingyi Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UV parameterization is a fundamental step in 3D content creation, yet producing production-ready UV layouts remains challenging due to the gap between geometric distortion objectives and the stylistic preferences of professional artists. While classical methods optimize handcrafted energy functions, artist-authored UVs exhibit structural patterns such as straightened seams, axis-aligned islands, and flexible interior deformation, properties that are difficult to explicitly formulate. In this work, we present DreamUV, an end-to-end learning framework that formulates UV unwrapping as a generative Flow Matching problem. Rather than predicting a single optimal parameterization, DreamUV learns a mesh-conditioned transport process that maps noise samples to a distribution of artist-like UV layouts. To reflect real-world authoring practices, we introduce a boundary-aware training strategy that prioritizes seam geometry, and a Model-in-the-Loop Finetuning(MITL) scheme that explicitly accounts for discretization errors during sampling and stabilizes transport dynamics under heterogeneous supervision. We evaluate DreamUV on a large-scale dataset of professionally authored UV layouts. Experiments demonstrate that our method produces significantly straighter boundaries and tighter axis-aligned islands than both classical and learning-based baselines, while maintaining competitive distortion metrics. Qualitative results and a user study with professional artists further confirm that DreamUV generates UV layouts that are not only valid, but aligned with practical production requirements.

---


### 389. [A Differentiable Atari VCS:A Complex, Fully Known Ground Truth for Explainable AI](https://arxiv.org/abs/2606.22447)

**<font color=#1a73e8>作者：</font>** Andreas Maier, Siming Bayer, Patrick Krauss  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explanation requires ground truth: to verify an account of a system we must know its inner functioning-just what is missing where explainable AI (XAI) is most needed. Systems we can study fall into two camps. Simple, procedural one-decision trees, rule lists, sparse linear models-have a known but trivial mechanism, so explaining them tests nothing; genuinely complex ones-deep networks, real-world tasks-need XAI but have no ground-truth inner functioning, so an explanation can be plausible, confident, and wrong with no way to tell. We remove this dichotomy with a study object both genuinely complex and fully specified-inspectable by construction-and, so gradient methods apply, fully differentiable. We reimplement the Atari 2600 Video Computer System (VCS)-a real computer architecture, and the cradle of deep reinforcement learning-as two independent end-to-end differentiable emulators in Julia (jutari) and JAX (jaxtari), each validated bit-for-bit against xitari. Both reproduce xitari on all 64 supported Arcade Learning Environment (ALE) games: 64/64 byte-identical RAM and 64/64 pixel-identical screens. Treating the cartridge ROM as a weight tensor, RAM as a soft tape, and control flow as gates, we prove the differentiable (soft) execution equals the original (hard) one bit-for-bit in the forward pass at any finite temperature, while exposing surrogate gradients where the bit logic has none. The JAX port also opens a GPU path: batched differentiable rollouts reach millions of environment-steps/s on one commodity GPU. The system was built in roughly 137 active hours over 29 calendar days, much of it written autonomously by coding agents. This paper builds and validates the foundation, showing-theoretically and in a qualitative gradient study-that gradient-based XAI on it is feasible. Both ports' full code is available under the MIT license at this https URL.

---


### 390. [Cross-Layer Intrusion Detection in 5G O-RAN: Gains and Limits of Fusing Radio Telemetry with Network Flow Records](https://arxiv.org/abs/2606.22450)

**<font color=#1a73e8>作者：</font>** Hamed Fard, Ilya Komarov, Gerhard Wunder  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open RAN disaggregation enables joint analysis of DU radio telemetry and CU-side network-flow records, motivating cross-layer intrusion detection. We evaluate whether fusing these two modalities improves over each individually across seven architectures, using run-disjoint splits over ten seeds on a live 5G O-RAN dataset. Radio features match or outperform network flows on ROC-AUC and run-level detection rate across all architectures. Fusion yields selective ROC-AUC gains but at a one-percent false-positive operating point improves detection rate only for GRU and Transformer, reducing it for the other five models. The benefit is confined to architectures where both single-modality detection rates fall below 0.75. A DoS-to-Benign confusion of 27 to 46 percent persists across all 42 tested configurations of architecture, modality, and window duration, pointing to a limitation in the tested windowed statistical aggregation rather than in model capacity. Code is publicly available.

---


### 391. [Adaptive Recurrent Message Passing for Test Time Computing on Graphs](https://arxiv.org/abs/2606.22462)

**<font color=#1a73e8>作者：</font>** Junshu Sun, Wanxing Chang, Qingming Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-trained foundation models have demonstrated remarkable success in many domains, enabling a unified backbone to generalize across diverse downstream tasks. However, extending this paradigm to graph learning remains challenging due to the intrinsic mismatch between graph data and fixed architectural designs. In this work, we show that this limitation can be overcome via recurrent graph models. To achieve this, we conduct a systematic theoretical analysis, rigorously deriving step dependence as a necessary and sufficient condition for an adaptively convergent recurrent process. Building on this foundation, we propose AdaR, an Adaptive Recurrent graph model, empowering flexible test-time computing on various downstream tasks without changing model parameters. To enable adaptive inference, AdaR explicitly encodes normalized step information and representation-target relations into the recurrent updates. To ensure convergence of the recurrent process, AdaR employs gradient-based supervision signals that guide representation updates throughout the recurrence. Empirical results demonstrate that AdaR consistently outperforms strong baselines in both inductive and transductive settings.

---


### 392. [Federated learning with heavy-tailed gradient noise and communication noise: a variance-reduction based algorithm](https://arxiv.org/abs/2606.22466)

**<font color=#1a73e8>作者：</font>** Shengchao Zhao, Yongchao Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is an emerging distributed machine learning paradigm that enables local devices to jointly train a global model while keeping data decentralized and private. We propose a variance-reduction based algorithm, VRA-FedSGD, for FL in the presence of heavy-tailed gradient noise and communication noise, where these noises are prevalent in large-scale machine learning over wireless networks and Internet of Things deployments. VRA-FedSGD employs a momentum variance reduction technique together with a nonlinear mapping to mitigate heavy-tailed gradient noise, and uses a variance-reduced aggregation mechanism to suppress heavy-tailed communication noise. In the mean sense, VRA-FedSGD achieves a convergence rate of {\small$\mathcal{O}\left(K^{-(p-1)/(2p-1)}\right)$} for nonconvex objective functions, where $p$ is the tail index of heavy-tailed noise. In the almost sure sense, VRA-FedSGD achieves a convergence rate of $\tilde{\mathcal{O}}\left(K^{-(1-1/(p-\epsilon))}\right)$ for strongly convex objective functions, where $\epsilon$ is an arbitrarily small constant. Simulated experiments on a logistic regression problem with real-world data verify the effectiveness of VRA-FedSGD.

---


### 393. [Not All Claims Are Equally Risky: FACTOR for Adaptive Verification in Factual Long-Form Generation](https://arxiv.org/abs/2606.22474)

**<font color=#1a73e8>作者：</font>** Areeba Hassan, Arooj Kausar, Syeda Kisaa Fatima 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) generate fluent long-form text, however, often add unsupported factual claims. Existing verification techniques improve factuality by grounding generation in external evidence. However, the same verification policy usually applies to all claims despite being differences in hallucination risks. We propose \textit{FACTOR} (\textit{FACTuality-Oriented Risk-aware Verification}), an inference-time model that adapts verification criteria according to claim-level uncertainty. FACTOR combines uncertainty estimation, adaptive language inference verification, and candidate re-ranking to allocate verification effort where it is most needed. We evaluate \textit{FACTOR} on FactScore benchmark showing that adaptive verification improves factuality while reducing verification cost simultaneously. We further perform different ablation studies to identify the primary driver of these gains. Our results show the effective and model-agnostic performance of \textit{FACTOR} for improving factuality in long-form generation.

---


### 394. [CVSBench: A Comprehensive Benchmark for Cross-view Spatial Reasoning and Dreaming](https://arxiv.org/abs/2606.22476)

**<font color=#1a73e8>作者：</font>** Ruixun Liu, Lingyu Zhang, Lanxuan Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans can effortlessly reason about scenes across different viewpoints, yet it remains unclear whether Vision-Language Models (VLMs) possess similar cross-view spatial abilities. Satellite-street scene pairs, with their complex contexts and extreme viewpoint variations, provide an ideal testbed. Motivated by this, we introduce CVSBench, a large-scale benchmark for evaluating cross-view spatial reasoning through satellite-street pairs.
This benchmark supports multiple tasks, including cross-view VQA, cross-view grounding, and viewpoint identification. CVSBench comprises 3,297 cross-view image groups with 9,468 object-level annotations and 40,679 question-answer (QA) pairs, enabling systematic and controlled evaluation of cross-view spatial reasoning. Extensive evaluations reveal that advanced VLMs struggle to maintain object-level and layout consistency under drastic viewpoint changes. To bridge this gap towards human-like spatial cognition, we investigate two categories of approaches: spatially grounded reasoning and the incorporation of cognitive map inputs.
Our findings demonstrate that language-only reasoning yields marginal improvements, while incorporating visual spatial imagination via a 3D scene imagination pipeline substantially improves cross-view reasoning. These results highlight the necessity of explicit visual-spatial representations for robust spatial cognition in VLMs. Our data and code are released at this https URL.

---


### 395. [Physically-guided Image Generation for Multi-Projection Mapping](https://arxiv.org/abs/2606.22477)

**<font color=#1a73e8>作者：</font>** Xingyun Liu, Yuqi Li, Jinhui Xiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Projection Mapping (PM) enables seamless superimposition of digital content onto real-world 3D objects, serving as a fundamental technique for immersive visualization, digital twins, and interactive art. Although text-to-image diffusion models have greatly facilitated customized content creation, directly integrating them into practical PM pipelines remains challenging due to the mismatch between idealized 2D generation and physical constraints. To bridge this gap, this paper formalizes two application-level generative paradigms: the cooperative paradigm (harmonizing generated semantics with physical attributes) and the adversarial paradigm (eliminating surface interference via radiometric compensation). Based on this, we propose ConPhyG, a unified controllable physically-guided generative multi-projection mapping framework that enables creators to interactively adjust physical constraints and flexibly switch generative paradigms. In cooperative mode, multi-dimensional physical priors (per-pixel gamut, depth, and edges) are injected into the diffusion process. In adversarial mode, the framework releases the generative potential and applies bounded numerical optimization for multi-projector radiometric compensation. It allows users to dynamically switch constraints to balance artistic freedom with physical feasibility. Furthermore, we extend ConPhyG to 360-degree multi-view consistent PM using a sequential generation strategy. Quantitative and qualitative evaluations on a real-world four-projector setup demonstrate that ConPhyG significantly outperforms state-of-the-art methods in geometric alignment, gamut utilization, and semantic fidelity.

---


### 396. [Human and AI collaboration for pulmonary nodule segmentation](https://arxiv.org/abs/2606.22486)

**<font color=#1a73e8>作者：</font>** Hongqiao Dong, Wenhao Chi, Ruobing Liang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical expert annotators are scarce, and blind reliance on artificial intelligence (AI) can be misleading, motivating approaches in which humans, particularly junior medical trainees or even non-medical personnel, collaborate with AI to achieve robust medical segmentation. Although the Segment Anything Model (SAM) shows promise for general-purpose image segmentation, its performance in human-AI collaboration for specialized medical tasks has not been thoroughly evaluated. Here we present Hi-Seg, a human-in-the-loop segmentation framework for pulmonary nodules built on SAM. Humans iteratively refine prompts through trial-and-error learning and semantic reasoning, progressively guiding SAM toward higher-quality masks. Using chest CT scans from 1,179 patients across 12 centers, we conducted the first large-scale external validation of collaborative human-SAM segmentation. Across all annotator groups, Hi-Seg achieved a mean Dice score of almost 85%, outperforming five state-of-the-art deep learning models by 10-22% and 13 SAM variants by 1-29%. Hi-Seg improved segmentation accuracy while reducing annotation time for medical annotators, and briefly trained non-medical annotators achieved performance comparable to that of the junior medical student. These findings suggest that human-in-the-loop segmentation can reduce clinician workload, enable scalable crowdsourced annotation, and transform clinical workflows by facilitating the safe and efficient integration of foundation models into routine clinical practice.

---


### 397. [FetSelect: Task-Specific Architectures and Self-Supervised Learning for Automated Fetal Ultrasound Frame Selection](https://arxiv.org/abs/2606.22487)

**<font color=#1a73e8>作者：</font>** Mahmood Alzubaidi, Raden Muaz, Uzair Shah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated frame selection for fetal biometry remains under addressed, with most prior work targeting generic quality assessment or downstream measurement pipelines that assume suitable frames are available. We introduce FetSelect, a task-specific framework that pairs a frozen vision foundation backbone with a hybrid multi-head design: a Task-Gated classification head and a Detection-derived quality head combined via learned fusion. We curate 6,486 expert-labeled frames across four targets: Crown-Rump Length (CRL), Nuchal Translucency (NT), Nasal Bone (NB), and Scalebar, and adapt the backbone with BYOL pretraining on 19,019 unlabeled images. On a held-out test set (974 frames), FetSelect achieves mean AUROC 0.956 and mean correlation 0.818 with expert quality annotations. Ablations confirm that hybrid fusion surpasses single-head variants, and ultrasound-specific self-supervision yields consistent gains. Evaluation on external clinical videos and 509 external CRL images demonstrates task-specific discrimination.

---


### 398. [SCOPE: Evolving Symbolic World for Planning in Open-Ended Environments](https://arxiv.org/abs/2606.22488)

**<font color=#1a73e8>作者：</font>** Yundaichuan Zhan, Minghe Gao, Zhongqi Yue 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent works have explored integrating Vision-Language Models (VLMs) with classical planners that rely on symbolic representations of planning problems to generate long-horizon plans for complex embodied tasks. However, in open-ended environments, these symbolic representations obtained from perception are often incomplete, leading to suboptimal performance. To address this, we introduce SCOPE, a self-adaptive symbolic planning framework that supports refining action plans and evolving the symbolic world, i.e., the symbolic representations of open-ended environments. SCOPE comprises two synergistic modules: a Symbolic Execution Simulator (SESim) that conducts symbolic validation and real execution of action plans, leveraging the feedback to refine the plans and evolve the symbolic world; and a Self-Adaptive Symbolic Memory (SASMem) that further distills feedback into evolving symbolic knowledge to enhance long-horizon planning and modeling of the symbolic world. Experiments in open-ended environments show that SCOPE significantly improves the completeness of the symbolic world, the success rate of plans under environment perturbations, and cross-task grounding and adaptability across diverse embodied scenarios.

---


### 399. [Deep Learning-Based Sign Language Recognition from Videos and Cross-Lingual Translation to Indian Vernaculars](https://arxiv.org/abs/2606.22494)

**<font color=#1a73e8>作者：</font>** Chandranath Adak, Ramesh Nandipalli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sign language is a primary mode of communication for the global deaf and hard-of-hearing community, yet automated tools that recognize sign gestures from video and translate them into natural language text remain limited, particularly for low-resource Indian languages. We present a two-stage deep learning pipeline that (i) classifies short sign language video clips into English word labels using a fine-tuned VideoMAE video transformer, and (ii) translates the predicted English label into Hindi, Telugu, and Bengali using Meta AI's No Language Left Behind (NLLB-200) multilingual translation model. The classification model is fine-tuned on a 13-class subset of the AI4Bharat Indian Sign Language video corpus from IIT Madras, processing 16-frame clips sampled uniformly from each video at 224 x 224 resolution. Under a small-scale academic setting (13 classes, 197 clips, 80-20 split), the fine-tuned model reaches 99% training accuracy and 78% validation accuracy after 15 epochs. We provide a per-class breakdown via a confusion matrix and classification report, identify the dominant failure modes (confusable adjective pairs such as ugly, deaf, blind, hat, and dress), and describe a Streamlit-based inference demo that takes a user-uploaded video and returns the predicted English label alongside its Hindi, Telugu, and Bengali translations. We discuss the scope, limitations (small label set, isolated-word rather than continuous signing, single-signer style sensitivity, ambiguity of single-word machine translation), and directions for future work, including expanding to sentence-level generation and a larger vocabulary. Code is released to support reproducibility.

---


### 400. [Lingering Authority: Revocable Resource-and-Effect Capabilities for Coding Agents](https://arxiv.org/abs/2606.22504)

**<font color=#1a73e8>作者：</font>** Igor Santos-Grueiro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents often receive broad tool access for an entire task, even when a resource is needed only for one subgoal. We call this gap lingering authority: a temporary resource/effect capability remains exposed after the episode that justified it has closed.
PORTICO is a reference monitor for revocable capabilities exposed to the planner. It compiles an explicit task contract into initial capabilities, grant rules, trusted closure predicates, and global deny rules. A request-grant-invoke lifecycle materializes expansions as opaque, epoch-bound handles. Closure removes those handles from the next planner interface and rejects stale replay before side effects. The monitor assumes mediated tools and a sound typed catalog.
In controlled coding-agent tasks, PORTICO records no executed contract-forbidden effects in the evaluated runs, while controlled grants recover boundary work blocked by a fixed narrow envelope. A non-revoking comparator receives the same initial envelope and the same grants at the same turns. On the closure slice, both systems match task success, scope compliance, and all pre-closure decisions; PORTICO then rejects 10/10 post-closure reuses, while the comparator permits 10/10. A deterministic stale-write audit records 0/6 versus 6/6 executed forbidden effects. Scripted traces and six live model traces over file writes, git mutation, and network egress show the same split. In a four-episode same-policy diagnostic, broad request exposure preserves zero executed forbidden effects but raises blocked proposals from 67 to 84. Frozen real-repository runs, with commits and traces recorded, exercise the same lifecycle on real project layouts.

---


> [!TIP]
> 当前位于：**351-400**（第 8/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
