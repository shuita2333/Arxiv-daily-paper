# 📦 其他研究 | 2026年09月14日

> 本类共 **189** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-189](./part-04.md)

---

### 101. [Bio-inspired Learning and Decision-Making with Probabilistic In-Memory Computing Hardware: Part 1](https://arxiv.org/abs/2609.11281)

**<font color=#1a73e8>作者：</font>** Thomas Dalgaty, Eiji Kawasaki, Miguel de Prado 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning and decision-making in animals are often modeled as Bayesian processes, where sensory evidence is integrated with prior beliefs to guide behavior in the face of uncertainty. But what are the inherent neural dynamics that give rise to this ability, and how could they be replicated in computing systems? This abstract discusses a biologically grounded framework in which noisy neural and synaptic dynamics perform inference and learning via stochastic sampling from an internal energy function, capturing uncertainty over latent states and model parameters through neural and synaptic variability, respectively. This enables approaches such as predictive coding networks to account for epistemic uncertainty via Markov chain Monte Carlo sampling. Drawing a parallel between intrinsic noise in biological systems and electrical noise in emerging probabilistic analogue memory technologies, we highlight how analogue in-memory computing hardware naturally emerges as the solution for massively scalable and energy-efficient probabilistic inference.

---


### 102. [When Does Text Inform? Benchmarking Information-Theoretic Metrics for Multimodal Time-Series Forecasting](https://arxiv.org/abs/2609.11282)

**<font color=#1a73e8>作者：</font>** Emma Andrews, Gianmarco Mengaldo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal forecasting models that combine time series with text annotations promise richer prediction through textual context, but how do we know whether a text annotation meaningfully contributes to the forecasters prediction? This is an information-theoretic question, but to evaluate whether information-theoretic metrics can reliably measure the predictive value an annotation provides, a ground truth benchmark is needed, and none currently exist. We create a synthetic time series signal with annotations in three categories: semantically correct, incorrect, and irrelevant. Because the data generation process is fully controlled, ground-truth information content is known exactly, enabling principled evaluation of six complementary mutual information estimators (KSG, MINE, InfoNCE, CCA, PID and V-information). We show that all six estimators identify correct annotations as most informative, and are able to audit the quality of mixed text corpora, choosing the annotations that result in the best downstream forecasting results without the need for model training. Our benchmark identifies limitations of each estimator, and these are validated on seven real-world datasets, which show how estimator performance differs on weak signals. Finally, we establish practical rules for implementing these metrics for annotation auditing and fusion selection.

---


### 103. [Generating a Consistent Enterprise: Synthesis and Reference-Free Evaluation of Multi-System Business Data](https://arxiv.org/abs/2609.11286)

**<font color=#1a73e8>作者：</font>** Benjamin Gruenbaum, Doron Porat, Assaf Natanzon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Synthetic relational data is normally produced by a model trained on a real dataset, and its quality is measured as the distance to that dataset. This paper describes a generator that has no real dataset at either end. Given an industry, a company size, a business model, a set of business applications, and a random seed, it produces a complete fictional enterprise: a workforce, a customer base, sales deals, support tickets, recorded calls, chat messages, and documents, all consistent with one another. One entity graph is projected into the native formats of 66 business products, so the same customer appears in the CRM, the support desk, and the call system under one identity. Because no real counterpart exists, realism is built in from cited reference statistics and verified by reference-free measurement: a five-axis scorecard of 28 statistical checks, an adversarial detector that hunts for the marks of synthetic generation, and a set of soundness checks that include a classifier test against an independently shuffled copy of the data. Because these instruments existed before the generator was tuned, progress is measured under a fixed yardstick: over 23 generated companies, mean realism climbed from 60.3 to 99.1, the weakest company from 41.1 to 94.9, and the detector, which initially flagged 55.2% of all records, now flags none. The scores hold on a seed never used during development. A second generator builds relational databases from a list of business questions. It forces qualifying rows for each answerable question, adds controlled near misses, and computes exact labels from the finished tables. The generator runs as a hosted service at this https URL. A company built there to a specification is served through its simulators over MCP and REST, and the simulators are also published as container images for offline use

---


### 104. [Automatic Lyric Transcription for Greek Songs: Scaling and Task Composition Effects in Whisper Adaptation](https://arxiv.org/abs/2609.11302)

**<font color=#1a73e8>作者：</font>** Maria Frangiadaki, Dimitrios Damianos, Kosmas Kritsis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Lyric Transcription (ALT) remains substantially more challenging than speech recognition due to melodic variability, rhythmic irregularity, and accompaniment interference. This is heightened in low-resource languages like Greek, where no prior benchmark for ALT exists. We present the first controlled study of Whisper adaptation for Greek ALT, investigating model scaling effects, task composition via multitask training in transcribe-translate ratios, and two-stage speech-to-singing adaptation. We also curate a segment-level aligned singing dataset based on the Greek Audio Dataset (GAD) using source separation and CTC forced alignment. Results show that scaling consistently improves performance, while multitask learning acts as a beneficial regularizer primarily for smaller-capacity models. The 2-stage adaptation in Whisper Large-v3 achieves a Word Error Rate (WER) of 27.2%, a significant improvement over zero-shot baselines, establishing the first Greek ALT benchmark.

---


### 105. [GRIPNet: Gaussian Radial Intensity Prior Guided Architecture for Pulmonary Nodule Detection in CT](https://arxiv.org/abs/2609.11312)

**<font color=#1a73e8>作者：</font>** Haojie Yang, Ran Su  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lung cancer causes more deaths than any other malignancy, and low-dose CT screening is the main pathway to early diagnosis. That pathway hinges on the smallest lesions, yet nodules below six millimeters remain hard to detect, because most methods treat a nodule as a generic object and ignore the imaging physics behind its appearance. We show that this appearance is highly regular. Intensity peaks at the geometric center of a nodule and decays radially in a Gaussian pattern, and a fit to 18,218 annotated lesions from three public benchmarks yields a mean radial coefficient of determination above 0.86 in every dataset and size stratum. A square convolution samples both axes uniformly and is mismatched to this radial signal, most severely for small nodules. Guided by this evidence, we propose GRIPNet (Gaussian Radial Intensity Prior Network), a detector in which every module maps to a measurable property of the intensity distribution. Pinwheel convolutions decompose radial gradients, a dual-frequency module separates boundary detail from structural context, dilated masked attention matches the decay extent, and an adaptive loss reweights samples by conspicuity. GRIPNet raises mAP@0.5 to 95.3, 91.6 and 97.9 percent on KanserSet, LUNA16 and Lung-PET-CT-Dx while sharpening high-IoU localization at real-time speed.

---


### 106. [Mi-Ripple: Restoring Images Degraded by Iterative AI Editing](https://arxiv.org/abs/2609.11317)

**<font color=#1a73e8>作者：</font>** Jiayin Chen, Yicheng Xu, Muting Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iterative reference-conditioned image editing can introduce grid-like and granular textures, commonly described as digital ripple. We present Mi-Ripple, a diagnosis-guided restoration workflow that suppresses this digital ripple while protecting image structure. Mi-Ripple separates periodic lattice artifacts from content-entangled granular texture, then combines selective spectral notching, structure-aware smoothing, and cleaned-reference regeneration. This separation enables low-distortion filtering when artifacts are spectrally isolated and visual reconstruction when filtering would erase legitimate detail. Across fourteen notch-only executions, whole-image residual standard deviation is 0.08--0.44 in CIELAB lightness units. In a paired regeneration example, reference cleaning reduces output debris density by 45\%. Mi-Ripple links measurable artifact reduction to visibly cleaner generated images, rather than optimizing a spectral score alone.

---


### 107. [Mr.LHDR: A Benchmark for Multimodal Real-World Long-Horizon Deep Research Agents](https://arxiv.org/abs/2609.11318)

**<font color=#1a73e8>作者：</font>** Minghao Guo, Meng Cao, Sui Zhao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research agents are increasingly capable of web search, tool use, multimodal evidence analysis, and information synthesis. However, existing benchmarks mainly evaluate medium-horizon exploration and rarely test whether agents can sustain long, dependency-heavy research processes. We introduce this http URL (Multimodal real-world Long-Horizon Deep Research), a benchmark for evaluating real-world deep research over long, irreducible chains of interdependent evidence across eight categories. Each question is constructed from a hidden Node-Relation graph and requires an average of 12.1 necessary intermediate conclusions with a mean dependency depth of 10.4 before reaching a short, unique, and verifiable answer. Questions incorporate multimodal evidence, including images, maps, PDFs, logos, charts, tables, and video frames, with at least one non-text element that changes the reasoning state. this http URL evaluates both final answers and the correctness of intermediate conclusions under annotated dependencies. We evaluate general models, deep research systems, and agent frameworks using Overall Accuracy (OA), Strict Accuracy (SA), Checklist Score (CS), and Dependency-Aware Checklist Score (DACS). Results show that even the strongest system achieves only 43.1% OA and 34.3% SA, indicating that final-answer accuracy substantially overestimates complete research success. Removing images reduces DACS by 12.6 points, demonstrating the importance of multimodal evidence, while SA consistently declines as reasoning chains become longer. These findings reveal sustained, dependency-consistent evidence integration, rather than isolated fact retrieval, as a key bottleneck for current deep research agents.

---


### 108. [AI Exposure and AI Resilience: A Two-Dimensional Assessment Framework for Software and Software-Based Business Model](https://arxiv.org/abs/2609.11321)

**<font color=#1a73e8>作者：</font>** Paul Darius Mandl, Peter Mandl, Martin Häusl  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is changing both software production and the economics of software-based business models. Classical technology due diligence mainly examines technical properties such as architecture, scalability, and technical debt. These criteria do not fully capture how AI can affect a company's value proposition, competitive position, margins, or access to customers. This paper develops Artificial Intelligence Exposure and Resilience (AI-ER) as a two-dimensional assessment framework. AI exposure describes the pressure for change that AI creates for a business model. AI resilience describes the company's ability to absorb that pressure, adapt to changed conditions, and use AI in an economically viable way. Metrics for both dimensions are derived from current AI capabilities, their deployment conditions, and relevant research on business models and organizational adaptability. The model keeps exposure and resilience separate and adds an explicit assessment of evidence quality and confidence. It can be applied first with public information and later refined with internal evidence. The result is a traceable company profile that supports comparison without concealing uncertainty in the underlying evidence. The paper also specifies an initial score logic and a procedure for empirical validation.

---


### 109. [MultiHuSE: A Multimodal Dataset for Humour Styles and Emotions](https://arxiv.org/abs/2609.11322)

**<font color=#1a73e8>作者：</font>** Mary Ogbuka Kenneth, Foaad Khosmood, Abbas Edalat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational recognition of verbal humour remains a challenging task, requiring an understanding of language, delivery style, emotions, and cultural context. Most existing approaches focus on binary classification and lack datasets that capture psychological dimensions of humour alongside variations in expression. We introduce MultiHuSE, a multimodal dataset comprising 2,407 high-definition videos of 50 demographically diverse actors performing 1,463 text samples across four psychological humour styles (affiliative, aggressive, self-enhancing, and self-deprecating), as well as neutral content. A subset is additionally annotated for underlying emotions. The dataset uniquely captures multiple actor interpretations of the same texts, enabling systematic analysis of expressive diversity. Baseline experiments show that multimodal fusion outperforms unimodal approaches (80.1% vs. 77.4% accuracy) in humour style classification, with particularly strong gains for affiliative humour (66% to 74%). While text provides the strongest individual signal, fusion models deliver meaningful improvements. We hope that MultiHuSE provides empirical support for psychological theories linking humour and emotion, while also opening new avenues for research in human communication, well-being, and AI-driven interaction. The dataset is available for academic use under an End-User Licence Agreement.

---


### 110. [Predictive Multi-Landmark OCT Tracking for Increased Motion Robustness](https://arxiv.org/abs/2609.11330)

**<font color=#1a73e8>作者：</font>** Konrad Reuter, Suresh Guttikonda, Chaitali Uday Karekar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical coherence tomography is a promising modality for markerless motion tracking due to its high spatial resolution and inherent depth perception. However, existing OCT-based tracking approaches are limited in terms of trackable velocity, particularly when multiple landmarks are tracked sequentially for 6D pose estimation. In this work, we present a predictive tracking approach that propagates positional updates between multiple tracked landmarks to obtain a global pose prediction. This enables more robust tracking under high velocities. Our results demonstrate RMSEs below 1 mm for velocities up to 100 mm/s and up to nine consecutively tracked landmarks, highlighting the potential of global motion propagation and prediction for improving the robustness of OCT-based tracking.

---


### 111. [Estimating Inconsistency Response Surfaces under Uncertainty in Cyber-Physical System Development](https://arxiv.org/abs/2609.11331)

**<font color=#1a73e8>作者：</font>** Johannes Mäkelburg, Tim Schwabe, Maribel Acosta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cyber-Physical Systems (CPS) are commonly represented through multiple interconnected models. During development, CPS consistency requires that shared model elements remain compatible across these models. Uncertainty, for example, due to sensor noise or model abstraction, changes the admissible values of model elements and can introduce inconsistencies, i.e., situations in which models can no longer be jointly satisfied. While existing approaches can determine consistency for a given uncertainty configuration, they provide limited support for systematically exploring, analyzing, and explaining inconsistency across large uncertainty spaces. We address this challenge by reformulating inconsistency as an intervention response modeling problem. Using Saltelli sampling and multi-fidelity Monte Carlo estimation, we generate intervention-response datasets and train a surrogate model that directly predicts inconsistency from the propagated uncertainty geometry. Experiments on 48 scenarios and 10 CPS domains show that the surrogate matches Monte Carlo estimates while reducing evaluation time from milliseconds to microseconds, enabling orders-of-magnitude more response-surface evaluations within fixed computational budgets. Building on the learned response surfaces, we perform sensitivity analysis to identify dominant uncertainty drivers and introduce a gradient-based consistency recourse method to determine minimal uncertainty interventions that restore consistency. The results show that inconsistency under uncertainty can be effectively learned, analyzed, and repaired through response-surface modeling, providing a scalable foundation for uncertainty-aware consistency management in CPS development.

---


### 112. [Exploring Diffusion Transformers for Cross-Modal Augmentation in Multimodal Brain State Decoding](https://arxiv.org/abs/2609.11341)

**<font color=#1a73e8>作者：</font>** Ziwei Wang, Xingyi He, Hongbin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal brain state decoding has largely focused on fusing paired modalities for prediction, but has rarely explored how their correspondence can be further exploited to enrich training data and improve multimodal representation learning. To address this gap, we propose CoMA-DiT, a bidirectional cross-modal Diffusion Transformer for latent augmentation that treats paired modalities as sources of mutual generative supervision rather than merely as inputs to be fused. CoMA-DiT conditions velocity prediction on the paired modality through cross-modal attention and adaptively injects the resulting variation via a reliability-gated residual mechanism. Experiments on multimodal auditory attention decoding and emotion recognition showed that CoMA-DiT consistently outperformed 20 representative baselines, achieving absolute gains of 4.28% and 6.70% in accuracy and macro-F1 over the no-augmentation baseline, respectively. Extensive ablation, sensitivity, visualization, and interpretability analyses further demonstrated its robustness, generalizability, and ability to capture functionally relevant cross-modal interactions. These findings support a broader view of multimodal learning: Paired modalities can serve not only as inputs for fusion but also as supervision sources that augment one another.

---


### 113. [Reification as a Transferable Vocabulary: Zero-Shot Link Prediction with Vanilla GNNs](https://arxiv.org/abs/2609.11347)

**<font color=#1a73e8>作者：</font>** Camille Pradel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph foundation models such as ULTRA achieve zero-shot link prediction on unseen graphs through dedicated architectures that hard-code a transfer mechanism. In this work we move that mechanism out of the architecture and into the representation, by \emph{reifying} the input graph: every fact becomes a node, connected to its subject, object, and relation type through a fixed vocabulary of six meta-relations, with relation types as anonymous shared nodes rather than model parameters. On this representation, five textbook GNNs (GAT, GINE with sum and with mean+max aggregation, GraphSAGE, R-GCN), each trained on a single knowledge graph of 4,245 triples for 30 minutes on one NVIDIA A100, transfer zero-shot to 40 inductive link-prediction benchmarks. The best of them, an off-the-shelf GAT, matches ULTRA, a dedicated foundation model pretrained on three graphs, across ULTRA's own evaluation suite. The same fixed vocabulary extends to relational databases, a row becoming an entity and a foreign-key column a relation type; a preliminary probe on two unseen databases, with no cell values, schema text or in-context labels, shows a model of this family pretrained on three knowledge graphs ranking foreign-key targets far above random-initialization and degree controls. We release the code, the checkpoints, and the evaluation pipeline for all 40 benchmarks.

---


### 114. [Local Robustness Quantification for Naive Bayes Classifiers and Generative Forests: a General Approach](https://arxiv.org/abs/2609.11366)

**<font color=#1a73e8>作者：</font>** Adrián Detavernier, Jasper De Bock  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We provide methods for calculating the robustness of the predictions of two types of generative classifiers whose underlying distribution is a Probabilistic Graphical Model (PGM): naive Bayes classifiers and generative forests (a probabilistic extension of random forests). Following the paradigm of robustness quantification, we define the robustness of a prediction as the extent to which the distribution of the classifier can be perturbed without changing this prediction. We consider perturbations obtained by varying the local models of the PGMs within general neighborhoods and focus in particular on epsilon-contamination, total variation distance and chi-squared divergence balls. We test our methods on benchmark datasets, demonstrate that the robustness value of a prediction serves as an indicator for its trustworthiness and compare our approach with other such indicators.

---


### 115. [RAMamba-Net: A Reliability-Aware and Mamba-Based Multimodal Fusion Network for Auditory Attention Detection](https://arxiv.org/abs/2609.11372)

**<font color=#1a73e8>作者：</font>** Xingyi He, Ziwei Wang, Dongrui Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Auditory attention decoding (AAD) identifies the attended speaker from physiological signals, supporting neuro-steered hearing devices and natural human-machine interaction. Electroencephalography (EEG) is the dominant modality for AAD but provides incomplete evidence in naturalistic audio-visual scenes, motivating EEG and electrooculography (EOG) fusion. Existing approaches remain limited by weak cross-modal interaction, inefficient temporal modeling, and low robustness to sample variations. To address the limitations, we propose RAMamba-Net, a reliability-aware Mamba-based multimodal fusion network for AAD. RAMamba-Net employs a Mamba-enhanced band-aware convolutional Transformer to capture band-specific EEG patterns and long-range temporal dynamics. A dual-branch temporal-spatial encoder models EOG temporal and inter-channel dependencies. Cross-modal attention enables explicit modality interaction. Then, a reliability-aware module is introduced to estimate sample-wise modality weights for feature and prediction consistency, thereby enhancing multimodal fusion. Experiments on two AAD benchmarks demonstrate that RAMamba-Net effectively exploits complementary EEG-EOG information, yielding accuracy gains of 5.76% over unimodal baselines, together with more robust decoding and discriminative representations. Further analyses show that explicit cross-modal interaction improves multimodal alignment, while the reliability-aware module suppresses unreliable modality evidence and is robust to signal perturbation and parameter variation.

---


### 116. [Vision Transformer-Based Multi-Level Feature Fusion for Multi-Label Sewer Defect Classification](https://arxiv.org/abs/2609.11375)

**<font color=#1a73e8>作者：</font>** Xu Fang, Zhuoran Wang, Qing Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated classification of sewer defects is essential for infrastructure condition assessment and maintenance decision-making, but existing deep learning methods struggle to balance classification accuracy and computational complexity in large-scale multi-label scenarios. This study develops Sewer-Transformer-ML, a hierarchical vision Transformer with multi-level feature fusion, together with two lightweight architectures, Sewer-MobileNet-ML and Sewer-Mobile-TransNet, for resource-constrained inspection scenarios. On the Sewer-ML test set, Sewer-Transformer-ML-Base achieved an $F2_{\text{CIW}}$ of 65.68% and an $F1_{\text{Normal}}$ of 92.68%, ranking first on the public leaderboard and exceeding the second-ranked method by 7.6 percentage points in $F2_{\text{CIW}}$. Sewer-MobileNet-ML achieved an $F2_{\text{CIW}}$ of 65.73% with only 17 M parameters, representing an approximately 95% parameter reduction relative to the base model. Under the standard Sewer-Capsule data split, Sewer-Mobile-TransNet achieved 96.43% classification accuracy. When the training set was reduced to 1,177 images, pretraining on Sewer-ML consistently improved model performance. Ablation experiments further showed that direct concatenation was more effective for Transformer features, whereas attention-based fusion better supported multiscale CNN features. These findings provide a computational basis for automated sewer inspection, lightweight model design, and adaptation across civil infrastructure inspection platforms.

---


### 117. [Brain-PACE: A Deep Siamese MRI Framework for Modelling Longitudinal Brain Acceleration](https://arxiv.org/abs/2609.11378)

**<font color=#1a73e8>作者：</font>** Samuel Maddox, Jacob Newman, Saber Sami 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain age estimation has become a popular research proxy for assessing brain health and disease, yet longitudinal trajectories of brain ageing are still poorly defined, and clinical use is limited. Building on existing Siamese longitudinal frameworks, we develop Brain-Predicted Age Acceleration (Brain-PACE) to directly estimate the pace of structural brain ageing from paired T1-weighted MRI. Brain-PACE identified accelerated ageing in $42.6$% of participants with mild cognitive impairment. Faster Brain-PACE was associated with greater functional and cognitive impairment (FAQ; $r=0.35$, ADAS13; $r=0.30$, CDR-SB; $r=0.32$) and greater regional tau burden in the posterior cingulate ($r=0.59$), precuneus ($r=0.47$), and entorhinal cortex ($r=0.37$). These associations were stronger than those observed when pace was calculated indirectly from repeated cross-sectional brain age estimates, suggesting that direct longitudinal modelling captures complementary information relevant to ongoing pathological change. Methodologically, Brain-PACE extends the LILAC framework by combining spatial attention with soft label distribution learning and a Cramér distance objective, improving probabilistic performance and reducing prediction bias while providing measures of predictive uncertainty. Together, these findings support Brain-PACE as a complementary longitudinal imaging phenotype with sensitivity to relevant clinical and biological changes in early neurodegeneration.

---


### 118. [DINO-Med: A Unified Patch-Based Adaptation Framework for Multi-Modal Medical Image Analysis Applied to Liver Fibrosis Staging](https://arxiv.org/abs/2609.11380)

**<font color=#1a73e8>作者：</font>** Boya Wang, Ruizhe Li, Chao Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting natural-image foundation models like DINOv3 to multi-modal medical imaging is challenging due to the significant domain gap between natural color images and multi-channel medical scans. We present a unified, patch-based framework that processes raw multimodal imaging through training-free registration, automated localization, and mask-filtered patch extraction. This architecture culminates in a hierarchical strategy that aggregates patch-level insights into subject-level diagnostics. Using liver fibrosis staging as a case study, we evaluate four patch-level feature representations: handcrafted Radiomics features, learned ResNet features, pre-trained foundation model SAM-Med2D features, and frozen DINOv3 features. To ensure a controlled comparison, all models utilize the same lightweight MLP head and are evaluated across both rigid and deformable registration settings. Our training protocol focuses on mild fibrosis (S1) and cirrhosis (S4) classes only, enabling a single classifier to address both substantial fibrosis detection and cirrhosis staging. Evaluated via 10 random train (90%)/ test (10%) splits on 360 subjects from the CARE 2025 Liver Track 4 cohort, our DINOv3-based framework significantly outperforms all baselines, achieving the best classification accuracy of 78.4% for S1 and 75.8% for S4.

---


### 119. [From Queries to Narratives: Cultural Heritage Data Stories for Knowledge Graph Exploration and Quality Assessment](https://arxiv.org/abs/2609.11403)

**<font color=#1a73e8>作者：</font>** Tabea Tietz, Torsten Schrade, Etienne Posthumus 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cultural-heritage KGs such as the NFDI4Culture-KG contain millions of triples about artworks, music, inscriptions, historical events, and the people and places connected to them. For many users, however, discovering this knowledge can be difficult. While SPARQL can be learned, writing meaningful queries first requires an in-depth understanding of the graph's data model, an investment many domain researchers and practitioners are unwilling to make. Even with existing user interfaces, a starting point and some guidance are usually needed, because the data contained in the graph is highly specialized, heterogeneous, and constantly growing, making it challenging to know what it contains or which questions it can answer. In this paper, we present data stories as a way not only to lower this barrier, but also to turn exploration into data-quality assessment, and thus combine accessible querying with the discovery of issues that remain hidden in aggregate statistics. In this contribution, a data story is understood as a narrative document that integrates explanatory text and images with executable SPARQL queries and their visualized results. It is described how they are authored against the graph and how they serve several purposes: guiding users through an unfamiliar graph, creating reproducible narratives, and surfacing data-quality issues previously hidden in aggregate statistics. The authoring platform LODEON including its Sparnatural and AI-supported authoring assistants is introduced as a proof-of-concept. Within the authoring environment, every claim made about the data can be backed by an explicit query, making these narratives transparent and reproducible. This paper also reflects on lessons learned from hands-on seminars and workshops. Early experience suggests that such data stories make cultural-heritage knowledge graphs more accessible for both exploration and quality assessment.

---


### 120. [Deep-Fake CAPTCHA: Mitigating Next-Generation Social Engineering Attacks](https://arxiv.org/abs/2609.11404)

**<font color=#1a73e8>作者：</font>** Guy Frankovits, Lior Yasur, Fred M. Grabovski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents DF-CAPTCHA, an active defense against real-time deepfake impersonation in voice and video calls. Instead of passively searching for artifacts, DF-CAPTCHA prompts the caller to perform simple challenge-response tasks that are easy for humans but difficult for current real-time deepfake systems to generate convincingly. The framework verifies the response using four criteria: realism, identity consistency, task completion, and response time. We evaluate the approach across both audio and video modalities using user studies and experiments with real-time deepfake models. Results show that people often struggle to distinguish real-time deepfakes from authentic media, while DF-CAPTCHA substantially improves detection performance over passive methods, reaching high accuracy in both modalities. These findings suggest that active challenge-based verification is a practical and robust defense against next-generation social engineering attacks based on real-time deepfakes.

---


### 121. [Are Caption Metrics Broken? Latency, Deaf and Hard of Hearing User Ratings, and Bias across Technologies](https://arxiv.org/abs/2609.11408)

**<font color=#1a73e8>作者：</font>** Bernard Thompson, James Waller, Luz Fanny Calderon Torres 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Live captions on TV often contain errors and timing issues, making it hard for deaf and hard-of-hearing (DHH) viewers to follow dialog. It is essential that caption quality metrics reflect the lived DHH TV viewing experience. To this end, we describe a U.S.-based large-scale online survey with 216 validated participants, who provided 302 responses containing a cumulative 4,832 data points. Participants viewed videos drawn from a pool of 70 clips recorded from live TV, and were asked to rate the caption quality and subjective understanding of the content across four conditions: TV captions as originally recorded with up to 7-12 seconds delay, TV captions synchronized with audio, Automatic Speech Recognition (ASR)-generated captions synchronized with audio, and ASR captions with an average two-second delay. All captions were evaluated against the Word Error Rate (WER), Automated Caption Evaluation (ACE2) and Number, Edition and Recognition (NER) metrics. Results show that TV and ASR captions were rated similarly. For TV captions, all three metrics were moderately-to-highly correlated with viewer ratings, but far less so for ASR captions, making them far from technology-neutral. Additionally, caption latencies significantly impact the viewer experience, especially typical 7-12-second TV delays. We discuss the implications for the adoption of caption quality metrics.

---


### 122. ["They don't care about this": A Systematic Study of TEE Build Reproducibility in the Wild](https://arxiv.org/abs/2609.11411)

**<font color=#1a73e8>作者：</font>** Annika Wilde, Marco Gutfleisch, Felix Reichmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs) have become a cornerstone of modern cloud computing, providing strong confidentiality and integrity guarantees for both code and data. A critical component of this trust model is remote attestation, which enables external entities to verify the authenticity and integrity of code executing within a TEE through cryptographic measurements. However, the effectiveness of remote attestation fundamentally depends on the verifier's ability to trace the reported measurement back to the original source code - a property that can only be guaranteed through reproducible builds.
In this paper, we investigate the reproducibility of TEE builds through a technical analysis of 115 TEE deployments. Our analysis spans popular TEEs such as Intel SGX, Intel TDX, and AMD SEV, and reveals that a striking 91% of those deployments were not reproducible, with 80% failing to provide both source code and a reference build, the two essential prerequisites for reproducibility. To explore the root causes, we contacted the maintainers of 50 SGX projects and managed to recruit 12 developers from industry and academia for interviews. Only one of our participants reported that reproducibility is a priority during development, effectively confirming our technical findings. Beyond technical barriers (e.g., timestamps included in the binary) that can be readily addressed, we identify broader ecosystem-level challenges, such as the lack of control over the build environment in projects involving multiple stakeholders. We argue that achieving reproducibility in TEEs requires a holistic development approach that extends beyond individual developers and calls for stronger commitments - rather than treating TEEs as a "security badge".

---


### 123. [Heterogeneous Cross-Chain Transaction Tracing for Solana Bridges via Candidate-Set Selective Decision](https://arxiv.org/abs/2609.11413)

**<font color=#1a73e8>作者：</font>** Wenjie Dou, Zheng Che, Meng Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Solana is a rapidly growing high-throughput blockchain platform that has attracted substantial liquidity and user activity. However, this expansion has also drawn the attention of illicit actors, who frequently leverage cross-chain bridges to route illicit funds onto Solana to obfuscate transaction lineage. Unlike EVM-compatible platforms, Solana features distinct execution dynamics and lacks standard event logs, creating severe semantic gaps that prevent existing tracing methods from reliably correlating cross-ledger transactions. In this paper, we formalize four types of Solana-bound cross-chain transaction modes and propose a candidate-set selective decision-based tracing method called SolTracer. SolTracer maps disparate execution semantics into a unified event space and employs candidate-set selective decision-making to reliably associate target transactions while abstaining when valid targets are absent. Extensive experiments demonstrate that SolTracer outperforms state-of-the-art (SOTA) methods across three representative scenarios: closed-world association, open-world association, and cross-source-chain generalization. In particular, under the challenging open-world setting with a 50% TA ratio, SolTracer improves the F1 score by 20.16% over the strongest SOTA baseline. Utilizing SolTracer, we conduct an empirical analysis on real-world cross-chain transfers to investigate ecosystem dynamics. Our analysis explores the stark count-value divergence across bridge mechanisms, the prevalence of cross-asset shifts, and the decoupling between on-chain settlement and explorer visibility.

---


### 124. [Multi-Modal Controlled Coherent Motion Generation](https://arxiv.org/abs/2609.11439)

**<font color=#1a73e8>作者：</font>** Yifei Liu, Qiong Cao, Hongwei Yi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> It is natural for humans to walk and talk simultaneously. This paper tackles the challenge of replicating such natural behaviors in 3D avatar motion generation driven by concurrent multimodal inputs, such as a text description of a man walking alongside speech audio. Existing methods, constrained by the scarcity of aligned multimodal data, typically combine motions from individual modalities sequentially or through weighted sums. However, they often result in mismatched or unrealistic movements. To overcome these limitations, we propose MOCO, a novel diffusion-based framework capable of processing multiple simultaneous inputs, including speech audio, text descriptions, and trajectory data, to generate coherent and lifelike motions without requiring aligned multimodal data. Our key innovation lies in decoupling the motion generation process. During each denoising step, the diffusion model independently generates motions for each modality from the input noise and assembles the body parts according to predefined spatial rules. The resulting combined motion is then diffused and serves as the input noise for the subsequent denoising step. This iterative approach enables each modality to refine its contribution within the context of the overall motion, progressively harmonizing movements across modalities. Consequently, the generated motions become increasingly natural and fluid with each iteration, achieving coherent and synchronized behaviors. We evaluate our approach using a purpose-built multimodal benchmark. Experimental results demonstrate that MOCO outperforms existing baselines, advancing the field of multimodal motion generation for 3D avatars.

---


### 125. [Chypothermia: Clock Freezing for Static Side-channel Attacks](https://arxiv.org/abs/2609.11442)

**<font color=#1a73e8>作者：</font>** Fatemeh Khojasteh Dana, Mehmet Ali Cetin, Xinrui Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static side-channel attacks, which exploit halted-clock conditions to extract sensitive information, pose an increasing threat to chip security. To counter these attacks, various defenses have been proposed that monitor for abnormal clock behavior and trigger the clearing of sensitive data when clock anomalies are detected. In this work, we demonstrate that exposing a chip to cryogenic temperatures interferes with on-chip mixed-signal components, responsible for signal sensing and generation. Based on this observation, we develop Chypothermia, an attack that, without any electrical tampering with the system, disables the target clock sensor, the clock generation circuit, and the voltage sensors, while preserving the secret data.
While effective at halting the clock, cooling is a slow process and, on its own, is often insufficient against systems equipped with temperature sensors designed to detect thermal anomalies. To bypass these protections, we combine Chypothermia with Chypnosis (Mitard et al., IEEE SP 2026) and show that, even within a moderately low-temperature operating range, this combination can halt the clock while evading detection. We implement Chypothermia on multiple FPGA/SoC platforms and demonstrate successful disabling of both soft-IP and hard-IP sensor implementations. Finally, we apply Chypothermia to the alert handler of the OpenTitan root of trust, which incorporates a state-of-the-art clock sensor, and show that the attack evades detection and prevents key zeroization. Finally, we introduce and implement an FPGA-compatible self-heating sensor as a countermeasure and demonstrate its robustness against Chypothermia.

---


### 126. [Calibration-Aware Uncertainty Cascades for Efficient Heterogeneous Model Collaboration](https://arxiv.org/abs/2609.11446)

**<font color=#1a73e8>作者：</font>** Yilin Zhang, Han Jiang, Cai Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Heterogeneous model collaboration seeks to exploit the complementary strengths of different models to balance predictive performance and inference cost. Existing approaches typically rely either on trained routers, which tie routing decisions to a fixed task and model pool, or on raw-confidence cascades, whose thresholds lack consistent reliability semantics across heterogeneous models. Consequently, these approaches adapt poorly to changing model pools and deployment budgets. We propose Calibration-Aware Uncertainty Cascades (CAUC), a simple post-hoc framework that independently calibrates each model's confidence and selects deployment policies using validation data. The resulting calibrated confidence scores establish a common reliability scale for accepting an early prediction, invoking a stronger model, or selectively combining model outputs. This unified decision criterion decouples deployment policies from any particular model pool or operating budget. We further show theoretically that calibration gives confidence thresholds an explicit selective-risk interpretation, whereas uncalibrated scores offer no comparable reliability guarantee. Extensive experiments demonstrate that, across six language benchmarks, CAUC achieves an average relative accuracy improvement of 1.9% over strong-model-only inference while avoiding approximately 47% of strong-model calls. On image classification benchmarks, it maintains or improves predictive performance while reducing measured GFLOPs by up to 57%.

---


### 127. [Prevalence Determines Precision:Silent Contamination in Detector-Defined Datasets](https://arxiv.org/abs/2609.11449)

**<font color=#1a73e8>作者：</font>** Jia Huang, Yankai Wan, Yangjun Ou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many ML datasets are constructed by running a detector, heuristic, or model over candidate pools; accepted items become labels. Dataset precision is then governed by true-positive prevalence in each pool via Bayes, not solely by detector quality. Using one instrument and period, we hold a detector-defined event dataset plus an independent official index labeling every detected item as real or phantom. One detector, three pools yield phantom rates 81.7%, 9.0%, and 0.0%. Transferring precision from the two high-rate pools to the low-rate pool predicts 0.955 versus measured 0.183, a +422% error; the Bayes expression predicts all three within 3.3%. The detected response curve is an exact convex combination of a true-event and a phantom component (residual 1.1e-16), with phantoms outnumbering true events 473 to 308, so contamination is a second signal with detector-inherited shape, not additive noise. Contamination direction depends on the estimator: on identical windows one statistic is diluted and another inflated because its denominator is also contaminated. A common normalization turns the estimator into a mean of ratios whose expectation need not exist; on the same 335 events it returns 0.40 where the well-defined estimator returns 0.10.

---


### 128. [Flexible and Interpretable Accent Distance Measurements](https://arxiv.org/abs/2609.11458)

**<font color=#1a73e8>作者：</font>** Charles McGhee, Mark J. F. Gales, Kate M. Knill  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Determining the differences between two speakers' accents is a fundamental task in linguistics and speech technology research. The methodology used to measure these differences depends on the specific research area. A phonetics researcher may demonstrate accent variation by comparing vowel formants in paired recordings of individual words. These results will be interpretable, but the recordings will be time-consuming to collect and may not be representative of connected speech. Accented Text-to-Speech (TTS) research has pushed towards using accent embeddings derived from accent classification tasks. These embeddings can be produced from any speech recording, but are not readily interpretable. In this paper, we demonstrate that articulatory representations created through articulatory inversion can be used as an interpretable basis for accent comparison and that optimal transport provides a framework for accent comparison across arbitrary recording types.

---


### 129. [ReGround: Grounding Reviewer Comments in Multimodal Evidence](https://arxiv.org/abs/2609.11460)

**<font color=#1a73e8>作者：</font>** Serwar Basch, Lizhen Qu, Iryna Gurevych  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reviewer comments naturally relate to specific parts of the reviewed paper, yet grounding these comments to the underlying evidence is difficult due to long multimodal documents. Existing benchmarks do not capture this setting and largely focus on explicit, information-seeking queries. We introduce ReGround, a large-scale dataset for reviewer comment grounding that links 10,267 reviewer comments to 16,274 evidence in the original anonymous submission of 3,656 papers. We build on a simple observation: author rebuttals often include explicit references to content of the submission used to address reviewer comments, providing a high-precision annotation source. We cast grounding as a retrieval task and evaluate a wide range of retrieval methods. Results show that retrieval over the entire paper content performs poorly, evidence-type inference is a major bottleneck, and multimodal evidence provides complementary signals that text alone misses. Our dataset exposes grounding reviewer comments as a difficult and practically important problem for scientific document understanding.

---


### 130. [BridgeMatch: Conditional Transport Bridges in Matching Matrix Space for 3D Deformable Registration](https://arxiv.org/abs/2609.11472)

**<font color=#1a73e8>作者：</font>** Qianliang Wu, Haobo Jiang, Guangwei Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable non-rigid point cloud correspondences are important for deformable anatomical registration, embodied perception and manipulation, and dynamic 3D reconstruction. Coarse-to-fine methods reduce computational cost by selecting the top-\(K\) coarse regions. However, this pruning may remove weak but correct hypotheses and restrict fine matching to an incomplete search space. We present \paper, a two-stage generative solver that maintains the complete soft matching matrix at both coarse and high resolutions. Stage~I uses denoising diffusion to estimate a global matching matrix in the compact coarse-resolution space. We then lift this matrix to high resolution while preserving its hierarchy. The lifted matrix is rank-bounded and block-constant. Stage~II refines it through a conditional transport bridge. We implement the bridge with two types of dynamics: a deterministic endpoint-parameterized conditional Flow Matching (CFM) ODE and a stochastic Brownian-bridge SDE inspired by Schrödinger bridges. Both variants share the lifted source, a time-conditioned transformer, and a matching-matrix endpoint predictor. Experiments on 4DMatch and 4DLoMatch show that both variants produce more accurate correspondences than the compared methods and improve downstream registration, with larger gains in low-overlap cases. They also improve cross-dataset generalization on CAPE and DeepDeform without target-domain adaptation while using the same deformation solver.

---


### 131. [Pre- and Post-Treatment Brain Metastases Segmentation Using nnU-Net with Post-Processing for BraTS 2026](https://arxiv.org/abs/2609.11477)

**<font color=#1a73e8>作者：</font>** Haobin Liu, Xin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain metastases exhibit high inter-lesion variability in size, enhancement pattern, and post-treatment appearance, making volumetric segmentation of both pre- and post-treatment cases the central challenge of the BraTS 2026 Task 1 (Brain Metastases). We build a pragmatic pipeline on a 5-fold nnU-Net ResEnc-L ensemble, in which each fold is trained independently for 1,000 epochs with the standard Dice + cross-entropy loss on 1,296 four-modality training cases. This ensemble is followed by a rule-based post-processing cascade tuned for the lesion-wise Dice similarity coefficient (LW-DSC), a detection-oriented metric that behaves very differently from the traditional global Dice. The final pipeline reaches an LW-DSC of 0.733 / 0.751 / 0.713 / 0.549 on the enhancing tumour (ET), tumour core (TC), whole tumour (WT), and resection cavity (RC) sub-regions on the official validation leaderboard. Rather than trusting these leaderboard gains, we audit every post-processing stage with a five-fold out-of-fold (OOF) analysis with no model-training leakage over all 1,296 training cases, scored with the official BraTS evaluation code (BraTS_evaluation): it confirms two stages as robust, per-fold-consistent improvements while the third improves only the leaderboard and does not reproduce out-of-fold. We further provide a mechanistic analysis of the LW-DSC metric that explains why recall-recovering post-processing carries low risk whereas component deletion does not, and we report thirteen negative results spanning loss engineering, alternative backbones, and inference-time settings, several of which run counter to widely held intuitions. Source code is released under Apache-2.0 at this https URL.

---


### 132. [FreeFlow: A Bias-free Hierarchical Transformer for Optical Flow Estimation](https://arxiv.org/abs/2609.11486)

**<font color=#1a73e8>作者：</font>** Vladislav Bargatin, Alexander Yakovenko, Khaled Abud 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical flow methods typically rely on task-specific inductive biases, such as correlation volumes, feature warping, and iterative refinement, among others, to reach high accuracy. While effective, such biases constrain the model to predefined heuristics, which can limit its expressivity and lead to more complex pipelines and additional computational cost. We present FreeFlow, a hierarchical transformer built without any flow-specific components, using instead a single feed-forward encoder--decoder. FreeFlow combines three attention variants: window attention for local processing, shifted-window attention for cross-window information exchange, and a global attention operating at a reduced resolution. The resulting architecture scales naturally with model capacity, enabling a consistent accuracy gain from small to large variants. Despite the absence of standard inductive biases, FreeFlow achieves state-of-the-art results on major benchmarks, including Sintel (0.68/1.48 EPE on Clean/Final), KITTI-2015 (3.23 Fl-all), and Spring (3.192 1px), while remaining memory efficient at 1080p inference.

---


### 133. [The Convention Gap: Towards Measuring Implicit Communication in Cooperative AI Evaluation](https://arxiv.org/abs/2609.11489)

**<font color=#1a73e8>作者：</font>** Makoto Fukushima, Hua-Dong Xiong, Ehsan Moradi Pari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cooperative AI agents are evaluated against other AIs, yet human cooperation relies on implicit conventions---shared protocols for reading meaning beyond the literal message---which AI-AI benchmarks may not capture. We propose the \emph{convention gap}, the difference between the failure probability predicted from the literal content of communication and the observed failure rate, as a metric of implicit communication. In the card game Hanabi, the finite deck and deterministic hint constraints make this posterior exactly computable. We replayed about 101,000 play actions from three public datasets of human-human (this http URL), AI-AI (HOAD), and human-AI (HanabiData) games. The gap was +26.2 percentage points (pp) in human pairs, $-$0.7~pp in AI pairs, and +16.4~pp in human-AI pairs, and was concentrated on plays of cards that had received no hints (+46~pp in human pairs). Within human-AI play, the literal information available to humans was similar across the three AI partners (mean predicted failure 38--41\%), but human failure rates ranged from 14.4\% to 34.4\% and the gap from +24.1 to +6.2~pp; the partner eliciting the largest gap produced the fewest human failures. Game score carried different information: it depended on each corpus's roster composition, whereas the gap separated human from AI play at the agent level. As a known-answer check, Off-Belief Learning agents, whose convention content is controlled by construction, gave a gap of +1.6~pp at the convention-free level, rising monotonically to +21.7~pp. These results suggest that convention compatibility, rather than AI-AI performance, may predict an AI's effectiveness with human partners.

---


### 134. [Published Unlearning Numbers Move Per Checkpoint, and Not Because the Removed Data Survives: An Audit of 263 Released Batch-Normalized Checkpoints](https://arxiv.org/abs/2609.11490)

**<font color=#1a73e8>作者：</font>** Junlong Shen Xingyu Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An unlearning audit reads its verdict off numbers that an unlearned model and its retrained reference each publish, and both also ship batch-normalization statistics that no gradient step wrote and no release records. Refitting them on kept data at bit-identical weights moves 47 of 221 released checkpoints past the spread their own release's seeds show, several inside a method whose average does not move: what moves is the checkpoint's property, not its method's. What does the moving is not the removed data surviving in the state: exchanging kept records for removed ones inside a fixed fitting pool moves a published cell by almost nothing, while how far a checkpoint's shipped state has drifted from any refit does track it. The consequence for a published decision is real but narrow: twelve verdicts cross, four clear a measured recalibration budget, two clear it on every replicate, and a population we trained and sited near its own criterion yields none. A release should therefore name the fitting convention beside the number, on the batch-normalized vision models where this channel exists.

---


### 135. [DeFiFlowBench: Benchmarking and Improving Safe Executability in Natural-Language DeFi Workflow Synthesis](https://arxiv.org/abs/2609.11504)

**<font color=#1a73e8>作者：</font>** Abhinav Rajeev Kumar, Harshit Arora, Varun Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A structurally valid DeFi workflow can still authorize a costly trade. We introduce DeFiFlowBench, a benchmark of 207 team-authored prompts for natural-language DeFi workflow synthesis. It measures graph coverage, configuration completeness, and declared safety predicates, then tests supported trade configurations on a local EVM. Direct, constrained, and few-shot prompting produce 14-19 unsafe held-out executions per configuration under a fixed 5% price-impact cap. A slippage bound derived from a quote does not prevent the price impact of the order itself. We propose Koan-Safe, which combines a prompt-only intent parser, a replaceable generator, and structural repair with default safety parameters. On 75 held-out workflow prompts, its hybrid variant scores 0.67 on the static safety proxy, compared with 0.33 for the best baseline. Koan-Safe records no unsafe executions on the saved benchmark outputs. A matched-candidate ablation produces 14-17 unsafe executions when enforcement is disabled. Additional tests expose the limits of default injection: permissive existing thresholds can still authorize unsafe trades. A separately evaluated policy cap addresses this failure on a 36-case diagnostic grid. These results support explicit trade protections and execution-based evaluation, while distinguishing declared safety from a general guarantee.

---


### 136. [UBone3D: Physics-Rectified Conditional Flow Matching for Anatomical 3D Shape Completion from Ultrasound](https://arxiv.org/abs/2609.11506)

**<font color=#1a73e8>作者：</font>** Weiying Chen, Yuchong Gao, Siyuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional ultrasound (US) is a safe, radiation-free complementary modality to CT and X-rays for longitudinal monitoring, yet its segmentation-derived partial point clouds are extremely artifact-laden. Consequently, it is challenging to recover a clean and complete anatomical structure from such US point clouds. In this paper, we present UBone3D, a novel framework based on physics-rectified conditional flow matching (CFM) that performs point cloud completion directly from partial US observations. UBone3D models deterministic physics artifacts (e.g., surface thickening, streaking, dropouts) via a simulated physics proxy, and introduces test-time physics rectification to steer the shape completion. At inference, the completion is jointly steered by two decoupled forces: (1) anatomical plausibility enforced by a CT-trained generative shape prior, BoneFM, and (2) physics consistency enforced by USimNet in the ultrasound formation space. Extensive experiments on simulated and in-vivo data demonstrate significant improvements in reconstruction accuracy and anatomical fidelity over existing baselines.

---


### 137. [Harnessing Intrinsic Subject-Aware Attention for Controllable Multi-Subject Video Generation](https://arxiv.org/abs/2609.11507)

**<font color=#1a73e8>作者：</font>** Niange Yu, Ye Tian, Biaolong Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-subject video generation faces two key challenges: uncontrollable fidelity strength and potential semantic drift. We address these by analyzing the internal mechanisms of Diffusion Transformers (DiTs). We found that certain attention blocks naturally form an Intrinsic Spatial Grounding Map (ISGM) that precisely locates reference subjects. Building on this insight, we propose Dual-phase Intrinsic Attention Leveraging (DIAL), a framework that uses these internal signals for both training and inference. In low-noise stages, we use ISGM to guide the attention mechanism, allowing precise control over fidelity strength during inference without retraining. In high-noise stages, we use these same maps to automatically build preference pairs at no additional cost for Reinforcement Learning (RL). This RL procedure effectively anchors the model's attention to reference subjects and mitigates semantic drift. Extensive experiments show that DIAL significantly outperforms baseline models on the OpenS2V-Eval benchmark, consistently improving identity consistency and enabling controllable fidelity strength.

---


### 138. [Extending SMT Solving with Non-Ground Clause Learning](https://arxiv.org/abs/2609.11509)

**<font color=#1a73e8>作者：</font>** Yasmine Briefs, Christoph Weidenbach  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantifier instantiation is currently the main approach to non-ground SMT solving: solvers generate ground instances and solve the resulting ground SMT problems with CDCL(T)-style reasoning. When a conflict is found, conflict analysis learns only a ground clause, even though the conflict comes from instances of non-ground clauses. Yet non-ground reasoning can give exponentially shorter proofs than purely ground reasoning. We propose a calculus that consists of ground instantiations, CDCL(T)-style rules, and non-ground conflict analysis. The solver reasons on ground instances, but the resolution steps of conflict analysis are performed on their original non-ground clauses. This produces learned clauses that are typically more general than the ground conflict. With a suitable strategy, the learned clauses are even non-redundant. We also show how chronological backtracking can be included in SMT solving. Our calculus gives a common setting for CDCL(T)-style SMT solving, a range of instantiation-based procedures, and non-ground clause learning, and we prove that it simulates CDCL, SCL(FOL), SCL(T), and even Resolution.

---


### 139. [Prototype Matters: Modality-unified Prototype Self-distillation for Unsupervised Visible-infrared Person Re-identification](https://arxiv.org/abs/2609.11514)

**<font color=#1a73e8>作者：</font>** Menglin Wang, Xiaojin Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating reliable cross-modality association is crucial to unsupervised visible-infrared person re-ID. While optimal transport is shown to be a practical solution for cross-modality association, it suffers from the rigidness of hard label assignment without considering the impact of cluster noise. Moreover, enforcing only cross-modality contrast is also suboptimal, as it fails to jointly optimize the similarity relation within and across modality. In this paper, we propose a novel framework for cross-modality learning by well exploitation of prototypes: First, instead of contrasting with cross-modality prototypes, we show that modality-unified prototypical contrast facilitates better modality invariance by jointly and simultaneously optimizing similarity relation within and across-modality. Taking self-prototype as a steady teacher, we further refine the instance-prototype online relation through prototype-guided self-distillation. The two components are optimized in a unified framework, leading to a simple yet effective model. On standard VI-ReID benchmarks, we perform extensive comparison and analysis, validating the effectiveness of our proposed method. Code is available at: this https URL.

---


### 140. [LoopVAE: Recurrent Depth Across Scales for Visual Tokenization](https://arxiv.org/abs/2609.11516)

**<font color=#1a73e8>作者：</font>** Zhiying Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hierarchical visual tokenizers typically allocate different processing blocks to different spatial scales. We ask how much of this computation can use the same parameters. LoopVAE reuses a scale- and loop-conditioned core within and across scales, while keeping resolution-changing transitions independent. A four-block core executes 28 block applications per encoder or decoder. On ImageNet-256, the 29M-parameter convolutional model reaches 0.28 rFID and 32.54 dB PSNR under an approximately 30-epoch two-stage training budget, using approximately 65% fewer parameters than the 84M reference VAEs. A non-adversarial Transformer ablation with the same execution graph finds competitive PSNR and SSIM under global sharing, although unshared blocks improve LPIPS. Targeted loop interventions show that completing the trained recurrence improves reconstruction and that even small feature updates can have substantial downstream effects. Truncation also exposes output-range errors, distinguishing useful recurrent computation from reliable early exit. Runtime profiling reveals the execution tradeoff: fewer stored weights require more arithmetic and longer runtime in the tested configurations. With convolutional and Transformer operators and single- or multi-resolution latent interfaces, LoopVAE establishes recurrent depth across scales as a parameter-sharing design axis for visual tokenization.

---


### 141. [Learning Interaction between Image and Layout Priors for Joint Image-Layout Generation in Design Templates](https://arxiv.org/abs/2609.11519)

**<font color=#1a73e8>作者：</font>** Shirong Yang, Bo Yang, Ying Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we address the problem of graphic design template creation, which generates a background image and a layout of foreground elements over the background to form a harmonious composition from an input text.
Prior work on graphic design generation mostly adopts a sequential paradigm, where design elements are generated sequentially. We argue that such a sequential scheme falls short of faithfully capturing the dependency between the background and layout (and thus the joint image-layout distribution), which limits the quality of generated design templates.
To overcome this limitation, we propose a model, InterIL, which jointly generates the two modalities, background image and layout, in a single generative process. The novel design of our joint model connects the backbones of pretrained image and layout diffusion models with a learnable communication module to explicitly model bidirectional image-layout interaction. During training, the image and layout backbones are frozen to maintain and leverage the vast pretrained single-modality prior knowledge, while only the communication module is updated, so that the model can focus on learning image-layout interaction and thereby better capture the joint image-layout distribution for improved composition harmony.
Our model has no design-specific inductive bias, which allows it to better preserve the original characteristics of realistic designs. We further introduce a test-time guidance strategy to enable users to impose their specific preferences on generated results.
Our experiments show that, compared with prior approaches, our model can generate significantly better results in terms of image, layout and image-layout harmonization, producing outputs closer to real samples. We also demonstrate the flexibility of our model in enforcing user preferences at inference without retraining.

---


### 142. [Generalized Score Matching for Parameter Estimation on Convex Domains](https://arxiv.org/abs/2609.11521)

**<font color=#1a73e8>作者：</font>** Nishanth Shetty, Saisuchith Mahajan, Chandra Sekhar Seelamantula  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Maximum likelihood (ML) estimation is a principled and statistically efficient approach for learning probabilistic models. However, for unnormalized models, ML estimation requires evaluating the partition function and differentiating through it, which may not always be tractable. Score matching provides a practically viable alternative that circumvents this obstacle by fitting the score in a way that eliminates dependence on the normalizing constant. We derive the generalized score matching objective on a convex subset of $\mathbb{R}^{d}$ constructively starting from Minimum Probability Flow (MPF) learning, and show how classical score matching as well as domain-adapted variants for non-negative data arise naturally within the proposed framework. We show that the resulting objective is a {\it proper local scoring rule} of second-order, which provides the theoretical guarantee that the true density is recovered when the objective is minimized. Furthermore, for a model belonging to the exponential family, we establish convexity of the objective together with consistency of the finite-sample estimator under standard regularity conditions. Our derivation sheds new light on the scope and applicability of generalized score matching in various problem settings. We compare generalized score matching-based estimators on constrained domains, where the partition function is analytically intractable. We provide experimental results on parameter estimation for model densities belonging to the exponential family defined over convex subsets of $\mathbb{R}^{d}$, and a generative modeling use-case to demonstrate broader applicability of the proposed generalized score matching framework.

---


### 143. [Lightweight LiDAR-Based Cone Detection Framework Using Random Forest for Formula Student Driverless](https://arxiv.org/abs/2609.11527)

**<font color=#1a73e8>作者：</font>** Márk Mező-Kerekes, Péter Praksz, Chang Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable, low-latency perception is crucial for Formula Student Driverless vehicles, yet many existing pipelines rely on deep learning and multi-sensor fusion, often requiring GPU acceleration. This paper presents a lightweight LiDAR-only perception pipeline tailored for CPU execution, combining ground removal, IMU-based motion compensation, DBSCAN clustering, and geometric feature-based Random Forest classification. Feature importance analysis reduced the model input from 12 to 7 features while preserving performance. Evaluated on 2,371 labeled clusters collected from real FSD events, the pipeline achieves an F1-score of 98.33% and an end-to-end runtime of 3.13 ms on CPU-only hardware. The released dataset, labeling tool, and trained models provide a practical and reproducible baseline for other resource-constrained autonomous racing teams.

---


### 144. [On Identifying Sound Conditions for Frontrunning Resistance](https://arxiv.org/abs/2609.11535)

**<font color=#1a73e8>作者：</font>** Sebastian Holler, Anna Piscitelli, Jannik Albrecht 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchains enable decentralized applications through smart contracts---interactive programs executed through consensus. However, the inherently asynchronous nature of blockchain transaction ordering introduces a class of vulnerabilities known as frontrunning attacks, which have caused millions of dollars in losses in major blockchains, such as Ethereum. Frontrunning attacks arise because users interact with smart contracts through transactions, which are added to the blockchain by designated nodes called miners. Miners can exploit their ability to reorder, delay, or insert transactions to gain an advantage over honest users, effectively frontrunning them.
Yet, to date, the field lacks a rigorous definition of what it even means for a contract to resist such attacks. Worse, we show that existing dynamic detection approaches are fundamentally inadequate: in a large-scale study comprising 287 smart contract audits, 55% of the 393 reported vulnerabilities identified by leading smart contract auditors fall outside the scope of state-of-the-art detection criteria. To address this gap, we propose the first formal definition of frontrunning vulnerability for smart contracts. Our definition captures a key insight: resistance to frontrunning is not an intrinsic property of a contract alone, but depends critically on how honest users interact with it. Grounded in this observation, we develop a sound algorithm for synthesizing secure interaction conditions, alongside a prototype implementation that we apply to audited real-world contracts---revealing previously undiscovered vulnerabilities in two Ethereum contracts.

---


### 145. [Particle GFlowNets: Rethinking Generative Marginalization Models](https://arxiv.org/abs/2609.11538)

**<font color=#1a73e8>作者：</font>** Tiago da Silva, Diego Mesquita, Salem Lahlou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative Marginalization Models (MaMs) have been recently introduced as efficient neural sampling models for any-order autoregressive modelling of discrete distributions. By learning both the marginal and conditional probabilities of a persistent-block Gibbs sampler, MaMs enable fast posterior evaluation with a single neural network forward pass. While prior work has considered MaMs to be distinct from Generative Flow Networks (GFlowNets), a well-established paradigm for inference in discrete stochastic models, we show that they are equivalent. Then, we also extend MaMs' sampling strategy to non-autoregressive generative processes. In particular, we describe an automatic criterion for full-state rejuvenation of the Gibbs sampler, derived from the Gelman-Rubin statistic, which plays a key role in speeding up learning convergence. Our experiments show that our method, called Particle GFlowNets, markedly accelerates training in large combinatorial spaces.

---


### 146. [Complex-Text Robustness Evaluation and Failure Diagnosis for Low-Resource Multilingual Text-to-Speech](https://arxiv.org/abs/2609.11545)

**<font color=#1a73e8>作者：</font>** Tianlun Zuo, Ziyu Zhang, Tingzhi Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource multilingual text-to-speech (TTS) systems have expanded language coverage, but their robustness under complex text inputs remains insufficiently diagnosed. Existing evaluations mainly focus on naturalness, speaker similarity, and content consistency using regular test sentences, while providing limited insight into how multilingual TTS systems fail when handling challenging inputs such as numbers, dates, named entities, long sentences, code-switched expressions, and punctuation-related structures. This paper proposes a complex-text robustness diagnosis framework for low-resource multilingual TTS. We evaluate robustness from three dimensions: content consistency, language consistency, and generation stability. A multilingual robustness testing scheme is designed for Thai, Vietnamese, Swahili, and Indonesian, covering ordinary sentences and multiple types of complex text inputs. We further introduce automatic diagnostic metrics, including character error rate, language identification accuracy, and duration abnormal rate. To support input-level risk analysis before speech generation, we propose a lightweight Text Risk Score (TRS), which estimates synthesis risk from interpretable text features without manual annotation or model training. Experiments on three representative multilingual TTS systems, including OmniVoice, VoxCPM2, and MMS-TTS, show that complex text inputs expose systematic failure patterns that are not fully reflected by ordinary short-sentence evaluation. Different systems exhibit distinct vulnerabilities in number normalization, named entity handling, long-text generation, and code-switched input processing. Furthermore, TRS shows a positive correlation with content errors and duration abnormalities, demonstrating its usefulness as a low-cost pre-synthesis indicator for complex-text risk diagnosis in low-resource multilingual TTS.

---


### 147. [World in World: Explore the World with World Models](https://arxiv.org/abs/2609.11548)

**<font color=#1a73e8>作者：</font>** Chenxi Song, Yanming Yang, Chi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video world models enable interactive, long-horizon exploration, but flexible control remains challenging. Exploring a source video from new viewpoints requires the generated rollout to remain synchronised with the recorded event, place observed content in the requested view, plausibly complete newly exposed regions, and recover previously generated appearance on revisits. Existing methods typically address these requirements through task-specific modules or additional training. We present World in World, a training-free inference-time interface that converts heterogeneous control evidence into camera- and time-labelled clean visual states, which are read through the native self attention of a frozen causal video model. The evidence comprises source-video observations, target-view scene projections, geometry renderings that guide completion of newly exposed subject regions, and retrieved generated states beyond the rolling cache. Each evidence source carries token-level support and its own availability schedule. A correspondence router combines persistent point identities with geometry to establish token correspondences, guiding supported queries towards matching source-video tokens. Evidence-wise attention CFG (EWA) then independently regulates each auxiliary channel's additional contribution using attention responses from the same denoising forward pass. The shared interface supports camera-controlled rerendering, long-horizon revisiting, and human-motion transfer with the same frozen backbone. We evaluate World in World on camera-controlled video rerendering under diverse viewpoint changes, assessing perceptual quality, temporal consistency, and camera-following accuracy.

---


### 148. [A Comparative Evaluation of Pre-trained Convolutional Neural Networks for Melanoma Detection](https://arxiv.org/abs/2609.11550)

**<font color=#1a73e8>作者：</font>** Wagner Moreno Schmitz, Marco Antonio de Castro Barbosa, Thiago Magalhães Amaral 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early diagnosis of melanoma is critical for improving patient survival rates. However, accurately distinguishing melanoma from other skin lesions remains a significant clinical challenge due to the high visual similarity among lesion types and variability in image acquisition conditions. Artificial intelligence, particularly machine learning, has emerged as a promising tool to support dermatological diagnosis by automating feature extraction from medical images. Among the available approaches, convolutional neural networks (CNNs) have demonstrated strong performance in image classification tasks, making them well-suited for analyzing both dermatoscopic and histopathological images, given their ability to capture hierarchical visual patterns relevant to lesion characterization. Nevertheless, despite numerous pre-trained CNN architectures having been proposed, selecting the most appropriate one for a given imaging modality remains an open challenge. In this study, we evaluate pre-trained convolutional neural networks (CNNs) for skin lesion classification using dermatoscopic and histopathological image datasets. Experiments were conducted on the HAM10000, ISIC 2018, and CR-AI4SkIN datasets, evaluating the ResNet50, VGG16, VGG19, MobileNet, and InceptionV3 architectures under the same training protocol. The experimental evaluation showed that the models achieved accuracies ranging from 71% (InceptionV3 on ISIC 2018) to 84% (ResNet50 on HAM10000) on dermatoscopic images. For histopathological images, accuracies ranged from 72% (VGG19) to 83% (ResNet50) on the CR-AI4SkIN dataset. The results demonstrate that model performance differs between dermatoscopic and histopathological image modalities, showing that architectures exhibiting similar performance on dermatoscopic images exhibit different performance on histopathological data.

---


### 149. [Accountability in Certificate Transparency and Variants](https://arxiv.org/abs/2609.11552)

**<font color=#1a73e8>作者：</font>** Timo Treitz, Robert Künnemann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Certificate Transparency (CT) aims to reduce the trust required in Certificate Authorities (CAs) within the TLS certificate ecosystem. It is supported by all major browsers. The protocol obliges all CAs to record the certificates they issue in a public log, which itself is monitored for compliance and consistency by third parties. Given this complex set of checks between the four roles-CA, loggers, monitor but also the end user's client-it is very hard to provide a precise account of how CT eliminates trust assumptions in exchange for complex infrastructure. Analyses both in the Dolev-Yao paradigm and the computational paradigm only regard a very simplified model and feature definitions adapted specifically to CAs, essentially capturing design features rather than the target property. The present paper posits accountability as the main goal of CT and presents a thorough analysis in the Dolev-Yao model. We start with the vanilla PKI and, step by step, move to CT, finally analyzing proposed extensions for SCT Auditing and Gossiping. We show that plain CT relies on an honest log, but provides accountability under this assumption. Furthermore, we show that the SCT Auditing extension can eliminate this assumption, while the Gossiping extension cannot.

---


### 150. [Learn the Solid, Not the File: Canonical Inputs for Neural Networks on CAD Boundary Representations](https://arxiv.org/abs/2609.11573)

**<font color=#1a73e8>作者：</font>** Heinrich Jiang, Hager Yasser Mohamed, Alexander Hitt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Boundary representation (B-rep) is the standard format used by modern CAD systems for parametric 3D models. It turns out, the exact same solid can be represented by different B-reps: for example, two engineers using different operations, a geometry kernel rebuilding the file, and an export setting repartitioning faces will lead to different B-reps even though the underlying solid remains the same.
We show that existing B-rep encoders are not robust to variation in the B-rep with the same solid on perturbations applied to standard benchmarks, naturally occurring variations inherent to CAD software, and differences in how designers model the same part via a human dataset we created in FreeCAD. The performance of popular B-rep encoders often collapses catastrophically.
We propose the canonical region graph, an input representation whose nodes, features and coordinate frame are derived from the solid itself and show theoretical invariance guarantees on repartitioning and rigid motions. It matches the strongest baseline on standard benchmarks, and is stable under every perturbation we test.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-189](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
