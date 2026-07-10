# 📦 其他研究 | 2026年07月11日

> 本类共 **189** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-189](./part-04.md)

---

### 101. [HSA: Hierarchical Slot Attention for Multi-granularity Scene-Decomposition](https://arxiv.org/abs/2607.08249)

**<font color=#1a73e8>作者：</font>** Neelu Madan, Rongzhen Zhao, Andreas Mogelmose 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Slot attention is a powerful framework for object-centric learning, decomposing visual scenes into latent slots through iterative competitive attention. However, existing methods share two critical limitations: they decompose scenes into a flat set of slots at a single granularity, and this decomposition is based on appearance rather than semantics. Yet humans understand scenes through semantic hierarchies: separating foreground from background, recognizing object categories, and identifying individual instances. Crucially, such semantic hierarchies cannot emerge without supervision, because category names are human constructs, not visual patterns. We propose Hierarchical Slot Attention (HSA), which learns multi-granularity semantic scene decomposition from a single model. HSA decomposes scenes at three levels: holistic (foreground/background), semantic (object categories), and panoptic (individual instances). Using only 10\% labeled data, combined with hierarchical alignment loss, HSA learns all three levels jointly. We further introduce grouping purity and containment to measure whether the hierarchy is encoded in representation space, not just output masks. Experiments on COCO and PASCAL VOC demonstrate that HSA outperforms the strongest flat baseline by up to \textbf{$+$41.5} ARI at holistic, \textbf{$+$14.6} at semantic, and \textbf{$+$10.4} at panoptic level on COCO, with even larger gains on Pascal VOC, while requiring a single model instead of three. Code will be made available upon acceptance.

---


### 102. [On the Design of Mixture-of-Experts for Dynamic Gaussian Splatting](https://arxiv.org/abs/2607.08250)

**<font color=#1a73e8>作者：</font>** In-Hwan Jin, Hyeongju Mun, Joonsoo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic scene reconstruction remains challenging due to the heterogeneous and spatially varying nature of real-world motion. Although recent 3D Gaussian Splatting methods have introduced diverse deformation formulations for dynamic novel view synthesis, each method typically relies on a single deformation model within its representation, which limits robustness across diverse dynamic scenarios. In this work, we study a fundamental problem-multi-deformation modeling for dynamic 3D Gaussian representations-under two distinct integration constraints that differ in when and how multiple deformation experts interact during training. From a Mixture-of-Experts (MoE) perspective, we view multi-deformation modeling as the problem of combining multiple specialized deformation models within a unified 3D representation. We first introduce Mixture of Deformation Experts (MoDE), which integrates multiple deformation experts directly into the deformable Gaussian Splatting pipeline through joint optimization. In MoDE, experts operate on a shared canonical Gaussian representation, enabling multi-deformation modeling without introducing additional training stages or modifying the original optimization schedule. In contrast, we further present Mixture of Experts for Dynamic Gaussian Splatting (MoE-GS) under a different integration constraint, where deformation experts are optimized independently and combined through a separate routing stage. As a result, expert interaction occurs over non-canonical Gaussian representations after individual optimization. Together, these two approaches provide alternative strategies for multi-deformation modeling, clarifying how integration constraints shape the design and behavior of deformation experts in dynamic 3D Gaussian representations. Our code is available at: this https URL.

---


### 103. [AutoPersonas: A Multi-Timescale Loop Engine for Open-Ended Persona Evolution](https://arxiv.org/abs/2607.08252)

**<font color=#1a73e8>作者：</font>** Mengchen Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term persona agents must remain identifiable while adapting to new events, relationships, evidence, and social conditions. We identify self-locking as a runtime failure mode in continuing persona-life loops: locally plausible events keep appearing while the generated life collapses toward familiar environments, weak relationships, suspended decisions, and stale life stages. We trace this failure to model-level convergence toward high-probability behavioral channels and system-level context gravity from State, memory, history, and environment summaries. We introduce AutoPersonas, a multi-timescale life-environment engine for bounded persona-level recursive self-evolution. It separates environment-side Occurrences, accumulated Observations, and persona State. Its OSO loop admits divergent future-facing material while requiring evidence-governed absorption before State or reachability changes. A three-year compressed simulation exposed environment watermark shells, occurrence-hardening gaps, slow-change accumulation failures, recursive indecision, and weak relationship persistence. An eight-model 40-day stress test generated 1,600 events and found mean rolling 5-day action-category repetition of 95.2%-97.6%, with all models crossing 90% by day 11. Semantic re-keeping found 79.0%-88.0% macro-theme repetition across all direct-loop runs. In a same-runtime 40-day A/B, context-slice masking plus per-sample divergence targeting reduced macro-theme repetition from 61.8% to 36.3% and roughly doubled cumulative theme count. A juvenile-goblin fictional-world run reproduced the anti-fixation regime without hard real-world intrusions. These results support a bounded claim: separating controlled divergence from evidence-governed absorption can reduce persona-environment self-locking while preserving identity continuity.

---


### 104. [CASL-VAE: Learning Structured Latent Variables from Unpaired Data for Semi-supervised Clustering and Paired Sample Generation](https://arxiv.org/abs/2607.08254)

**<font color=#1a73e8>作者：</font>** Sai Spandana Chintapalli, Pratik Chaudhari, Christos Davatzikos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantifying variability in a target population relative to a reference population is central to many scientific and clinical problems (e.g., diseased vs. healthy). Yet, without paired data and in the presence of heterogeneous target variation, existing methods struggle to separate multiple modes of target-specific variation. We propose \textit{CASL-VAE}, a deep contrastive latent variable model that learns structured latent generative factors from unpaired data. CASL-VAE factorizes variation into continuous common latent factors shared across populations and hierarchical salient latent factors that model target-specific heterogeneity as discrete subtypes and continuous within-subtype variation. Using variational inference, we show how approximate joint likelihood optimization over reference and target domains can be performed using unpaired data, providing a principled basis for paired-sample generation and cross-domain analysis. We validate CASL-VAE on semi-synthetic neuroimaging data, demonstrating improved subtype recovery and paired-sample generation compared to baseline clustering and generative models. We also validate its ability to reveal biologically plausible heterogeneity in Alzheimer's disease.

---


### 105. [Different Teachers, Different Capabilities: Sub-1B On-Device Distillation for Structured Text Enrichment](https://arxiv.org/abs/2607.08268)

**<font color=#1a73e8>作者：</font>** Vinay Kumar Chaganti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-volume structured extraction pays a large model's latency on every item, so distilling the task into a small on-device model is attractive: comparable output at a fraction of the time and cost. We measure what that distillation actually delivers, per sub-task. Each news article is mapped to one JSON object with a short summary and five categorical labels. We distill an 8B reasoning teacher (deepseek-r1:8b) into a 0.6B student (Qwen3-0.6B; QLoRA, three seeds), and add two teacher controls: a same-size non-reasoning teacher and a larger managed pipeline. A blinded, reference-free, three-judge panel scores every arm against the full article, alongside two non-distillation baselines, few-shot prompting and constrained decoding. The student runs at about 0.8 s per article against the teacher's 39 s, and recovers 58% of the base-to-teacher gap on summary quality, beating its primary baseline (constrained decoding) by +16.8 points and few-shot prompting by a secondary +4.9. A same-size non-reasoning teacher trains a student no better than the untuned base, so the summary gain follows from the teacher's reasoning nature rather than its scale. Capabilities then split by teacher: the reasoning teacher transfers writing quality and the managed pipeline transfers label diversity, while a same-size instruction teacher's students stay more grounded on the 22 short, thin-source articles in the 93-item test set (74 versus 55 faithful), where the reasoning-lineage student fabricates. That grounding difference is a consistent ordering rather than a significant aggregate effect, and the subgroup is small, so we report it as a direction. Because no single engine wins every field, the deliverable is a per-field routing map for on-device enrichment.

---


### 106. [Progression as Latent Drift: Generative Forecasting of Slow-Evolving Pathologies](https://arxiv.org/abs/2607.08270)

**<font color=#1a73e8>作者：</font>** Yuxiang Feng, Juncheng Wang, Chao Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forecasting the future anatomy of slow-evolving neurodegenerative diseases could enable earlier, more targeted intervention and improve clinical trial design, but it remains challenging because true progression signals are subtle in longitudinal MRI. In this low-signal regime, transferring modern generative sequence models directly is unreliable: training is dominated by stable baseline anatomy and confounded by dense, sample-specific nuisance variation. We first provide a theoretical analysis that explains these failures through two modes. Identity collapse occurs when optimization is driven toward reproducing the current anatomy, which prevents the model from learning faint temporal change. The continuous interpolation trap arises when standard smooth networks cannot separate localized biological drift from pervasive noise, which leads to spurious changes that diffuse across the volume. To address both issues, we propose Latent Drift, a progressive generative framework that learns change in a compressed semantic representation rather than synthesizing full-resolution anatomy. This design removes pixel-level identity from the prediction target and concentrates model capacity on progression-relevant dynamics. We further apply Finite Scalar Quantization to the learned change representation, which suppresses small, high-frequency nuisance fluctuations while preserving consistent structural drift. Experiments on longitudinal 3D brain MRI show that Latent Drift improves patient-specific neuro-forecasting over diffusion and autoregressive transformer baselines across generative fidelity and clinically relevant evaluation metrics. Project page: \href{this https URL}{this https URL}.

---


### 107. [How Analysts Use AI in High-Stakes Crime Linkage: An Industrial Study](https://arxiv.org/abs/2607.08274)

**<font color=#1a73e8>作者：</font>** Jessica Woodhams, Amy Burrell, Wanyin Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Crime linkage analysis is used in many countries to identify series of offences that may have been committed by the same individual. In practice, specialist analysts manually search for behavioural and situational connections across large crime databases, an effort that is time-consuming, cognitively demanding, and can involve repeated exposure to disturbing material. To support this work, an Artificial Intelligence (AI)-enabled decision-support tool was co-developed with a UK law enforcement agency to assist analysts in identifying likely crime linkages.
This paper reports an industrial evaluation of the crime-linkage tool. We conducted a mixed-methods usability study combining direct observation, eye-tracking, mouse-tracking, and surveys to examine how analysts engage with AI predictions and with the model features presented as explanations. Our findings show that analysts used the AI predictions selectively and frequently validated them against behavioural (non-AI) evidence, reflecting partial trust and an ongoing reliance on established analytical practices. We also found that analysts attended to the presented model features and valued their availability, while identifying opportunities to improve how explanations are presented and integrated into the workflow. Overall, our results highlight the need for AI-enabled decision-support tools to better integrate explanations and traditional analytical methods, and demonstrate the importance of in-situ evaluation for engineering usable and trustworthy AI in high-stakes settings.

---


### 108. [Enhancing the KidSat Model: Integrating Geographical Encoding and Data Quality Assessment for Childhood Poverty Prediction](https://arxiv.org/abs/2607.08281)

**<font color=#1a73e8>作者：</font>** Hou Hin Ip, Ka Nam Lam, Joshua Man Yu Ng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate poverty mapping using satellite imagery is often hindered by (i) noisy and sparse survey-derived supervision, (ii) image quality issues such as cloud cover and image corruption, and (iii) lack of explicit spatial structure in image-only models. Building on the KidSat framework, we develop an enhanced pipeline that improves predictive accuracy via refined data preprocessing, systematic image quality assessment, and mathematically defined geographic encoding. First, we refine the fine-tuning target matrix by resolving high-cardinality sparsity and reducing one-hot dimensionality from 103 to 51 via DHS re-aggregation. Second, we introduce a simple two-stage quality-screening procedure to filter heavily clouded or corrupted observations. Third, we fuse DINOv2 visual embeddings with Spherical Harmonics (SH) location features. Across extensive experiments, these changes reduce MAE from 0.2167 to 0.1759, corresponding to an 18.83% relative reduction on the cluster-level severe-deprivation proportion scale. When extended from 16 to 33 African countries, the best-performing configuration achieves an overall MAE of 0.1658. We find that SH features consistently improve performance over the image-only backbone, whereas higher-capacity coordinate Multi Layer Perception augmentation (SH+SIREN) can underperform without carefully designed objectives. Finally, gradient-boosted tree heads (XGBoost/LightGBM) most effectively exploit nonlinear interactions in the fused visual-geographic representation. These findings provide a scalable and principled recipe for improving satellite-based socioeconomic predictions using only publicly accessible data.

---


### 109. [Psychological Competence as a Missing Dimension in AI Evaluation](https://arxiv.org/abs/2607.08285)

**<font color=#1a73e8>作者：</font>** Marcos Economides, Paul M. Sacher, Samuel Salzer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current AI evaluation frameworks focus primarily on technical performance, including accuracy, robustness, reasoning ability, and policy compliance. These measures remain essential, but they are not sufficient for systems that interact directly with users through natural language. Human-facing AI systems are increasingly used as advisors, coaches, tutors, and companions. In these roles, their responses can shape how users reason, interpret emotions, form beliefs, calibrate trust, and make decisions. The relevant unit of evaluation is therefore not only the model, but the human-AI interaction. This paper introduces psychological competence as a missing dimension in AI evaluation. We define psychological competence as the capacity of a human-facing AI system to support user cognition, emotional interpretation, and behavioral decision-making in ways that are appropriate to the user, context, and purpose of the interaction. This includes interaction properties such as framing, tone, perceived authority, responsiveness, uncertainty handling, and conversational guidance. Existing evaluation approaches capture parts of this problem but rarely assess these psychological effects directly. Drawing on behavioral science and human-AI interaction research, we outline a conceptual framework for psychological competence and its core domains. Rather than proposing a specific benchmark, we define the construct, clarify its boundaries, and describe how it may be assessed through scenario-based probes, structured human evaluation, and model-assisted evaluation methods. We argue that psychological competence should become a core consideration for model providers, deploying organizations, researchers, and regulators concerned with the real-world effects of human-facing AI systems.

---


### 110. [From Legacy Documentation to OSCAL: An MCP-Based Agent Pipeline for Threat-Informed Continuous Compliance in Critical Infrastructure](https://arxiv.org/abs/2607.08288)

**<font color=#1a73e8>作者：</font>** Lea Roxanne Muth, Marian Margraf  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In critical infrastructure, operational technology environments often cannot be actively scanned, and yet active system feedback is needed for risk assessment and compliance. This paper presents a non-invasive, MCP-grounded multi-agent pipeline that converts natural-language system descriptions into source-verified knowledge graph and audit-ready artifacts in the NIST OSCAL format for continuous automated compliance management. The architecture decouples LLM-based reasoning from deterministic knowledge retrieval against authoritative threat-intelligence sources, reducing the risk of fabricated vulnerabilities and hallucinated attack paths.
In an evidence-based synthetic scenario of a water utility, the pipeline achieves 0.90 CVE recall and perfect D3FEND recall. It generates a schema-valid OSCAL System Security Plan and an OSCAL Security Assessment Report. Nevertheless, the core insight is not that grounding via MCP eliminates errors (e.g., hallucinations) entirely from the pipeline, but that it shifts errors into the first phase of asset extraction from the natural language description. Here, a single incorrectly extracted entity can lead to genuine but irrelevant CVEs in subsequent stages of the pipeline, which consumes time and resources. However, it makes the remaining risk visible, verifiable, and suitable for a time-efficient manual review, since the infrastructure (e.g., version numbers, OS, etc.) is typically known.

---


### 111. [Reverse Engineering Compliance: A Dual-Graph Verification Framework for Auditing Legacy IT Security Concepts](https://arxiv.org/abs/2607.08292)

**<font color=#1a73e8>作者：</font>** Lea Roxanne Muth, Marian Margraf  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The NIS-2 Directive increases the need for continuous, auditable compliance evidence and motivates a shift from document-based compliance toward machine-readable compliance artifacts. The Open Security Controls Assessment Language (OSCAL) is a standard for this purpose, which the German Federal Office for Information Security (BSI) is adapting with Grundschutz++. However, companies are still managing extensive legacy IT security concepts (IT-SCs), and migrating them without verification could transfer outdated assets into the new format. While existing research primarily addresses the generation of new concepts, there is a lack of a verification framework that extracts legacy IT-SCs into an auditable intermediate representation, deterministically compares the extracted graph with an independently constructed reference state, and exports schema-valid OSCAL artifacts.
This paper introduces the Automated Security Concept Structure Extraction and Reverse Topology-checking (ASSERT) Framework, which addresses this gap by using ontology-based extraction of legacy documents into formal document graphs, a five-class graph difference against a verified reference graph, and the export into schema-valid OSCAL outputs for system description and assessment evidence. Using the BSI's RecPlast dataset, we compare a local open-weight model and a commercial model across three configurations with different levels of reference-ontology exposure. The evaluation shows that ASSERT makes document-infrastructure inconsistencies measurable, but reveals a trade-off between discovering undocumented entities and enforcing a schema.

---


### 112. [ARGUS: Accelerated, Robust, General, and Unsupervised Cell Tracking Solutions](https://arxiv.org/abs/2607.08297)

**<font color=#1a73e8>作者：</font>** Noah Jaitner, Kandice Tanner, Ingolf Sack 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background and Objective: Quantitative analysis of cell dynamics is central to modern biological research, providing critical insights into immune cell interactions, disease progression, and drug mechanisms. Automated cell tracking in time-lapse microscopy remains challenging due to noise, morphological variations, overlapping cells, and dynamic events such as divisions and fusions.
Methods: We present ARGUS, a framework for Accelerated, Robust, General, and Unsupervised Cell Tracking Solutions. ARGUS combines adaptive cell detection, dense Farneback optical-flow prediction, frame-to-frame linear assignment, and a sequence-level tracklet-refinement step that reconnects trajectory fragments across short temporal gaps.
Results: On publicly available Cell Tracking Challenge datasets, ARGUS achieved detection accuracy of 0.905-0.971 and tracking accuracy of 0.897-0.964, with runtimes within 1 minute (5-6 seconds for 3 frames).
Conclusions: ARGUS is a modular, interpretable framework that can be adapted to different imaging modalities and biological applications without training data or GPU infrastructure. The implementation is publicly available at this https URL

---


### 113. [Classifier Chain-based Pathological Test Recommendation](https://arxiv.org/abs/2607.08299)

**<font color=#1a73e8>作者：</font>** Abu Rafe Md Jamil, Nayan Malakar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate and timely diagnoses are essential for quality patient care. However, delayed recommendation of diagnostic tests and physicians' subjective interpretations can hinder effective care. This study introduces a pathological test recommendation system that speeds up the test selection process using patient symptoms before physician consultation. The recommendation task is framed as a multi-label classification problem utilising the Classifier Chain (CC) technique to consider dependencies between tests. We collected data from the this http URL pathology and then created a custom dataset with the help of the expertise. Multiple machine learning algorithms, including Logistic Regression, Decision Tree, and Random Forest, were applied to compare models and identify the best fit for our study context. The Logistic Regression with CC model had the highest overall accuracy at 98.83%, while the Majority Voting ensemble model provided the best balance with a precision of 0.93, recall of 0.85, and F1-score of 0.89. To ensure transparency of the models and clinical interpretability, we used Explainable AI (XAI) techniques utilising SHAP (SHapley Additive Explanations), which identifies how each symptom is contributing to a test recommendation. The diagnostic reasoning revealed by the model was consistent with established medical knowledge of symptoms for the recommended tests, which further adds confidence to the model's reliability for diagnostic purposes. The reasoning could help physicians make logical decisions in critical scenarios. Overall, our findings suggest that CC can improve the efficiency of the traditional algorithms in diagnostic process providing accurate test recommendations.

---


### 114. [Learning $\mathsf{AC}^0$ under Locally Sampleable Graphical Models](https://arxiv.org/abs/2607.08303)

**<font color=#1a73e8>作者：</font>** Weiming Feng, Xiongxin Yang, Yixiao Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The problem of learning constant-depth circuits holds profound implications for computational learning theory. In a seminal result, by introducing the low-degree algorithm, Linial, Mansour, and Nisan (J. ACM 1993) presented a quasipolynomial-time learner for $\mathsf{AC}^0$ under the uniform distribution. However, obtaining comparable learning guarantees for broader classes of correlated distributions has remained a longstanding challenge. Recently, Chandrasekaran, Gaitonde, Moitra, and Vasilyan (arXiv 2026) extended these guarantees to Gibbs distributions on bounded-degree graphical models with both strong spatial mixing and polynomial growth.
In this paper, we give a quasipolynomial-time learner for $\mathsf{AC}^0$ under graphical models that admit efficient local samplers, circumventing the polynomial-growth requirement in prior work. The key ingredient is a new low-degree approximation for Gibbs distributions, established by simulating and suitably truncating the classical Glauber dynamics. As applications, this framework yields learners for two-spin systems, including the hard-core model and Ising model, on arbitrary bounded-degree graphs, in regimes approaching their respective sampling thresholds.

---


### 115. [INTENT: An LSTM Framework for Vehicle Intention Prediction in Intersection Scenarios with Comprehensive Ablation Analysis](https://arxiv.org/abs/2607.08316)

**<font color=#1a73e8>作者：</font>** Logine M. Zaki, Catherine M. Elias  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vehicle intention prediction is a pivotal aspect in the agility and safety of autonomous vehicles in all driving scenarios; if genuine enhancement of autonomous vehicles are required, we need to make them adopt human interpretation of driver's intention especially in cases that require a lot of human interaction as well as complex driving behaviors like the ones at intersections, roundabouts and emergency cases such as sudden stops where vehicle intention prediction helps in taking the correct evasive action within a real time period where every second of action makes an impact and can prevent a catastrophe from taking place. In the worst case, it helps minimize the damage and make safety a priority. Intention prediction can also be used to enhance trajectory prediction (intention conditioned trajectory prediction). In this study, The INTENT framework is proposed using LSTM model to predict the vehicle's intention at intersections 2 seconds ahead of the event occurrence to predict whether the cars in intersections are going straight, turning left, or turning right. Various model experiments and ablation study are thoroughly tested on InD dataset achieving 99.71% accuracy.

---


### 116. [Texture Representations in Deep Vision Models: Comparing CNNs, Vision Transformers, and Human Perception](https://arxiv.org/abs/2607.08321)

**<font color=#1a73e8>作者：</font>** Ludovica de Paolis, Marco Baroni, Alessandro Laio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In computational vision science, Convolutional Neural Networks (CNNs) have emerged as a popular model of biological vision because of the alignment they can exhibit with neural and behavioral data in humans and animals. However, it remains unclear to what extent this alignment persists for visual tasks that extend beyond the canonical object recognition paradigm based on well defined semantic content. In this study, we diverge from the common object-centric view by focusing on another aspect of vision: texture perception. We consider textures of different complexity generated with three different algorithms from the same source images. Using a rank-based statistic, we quantify the information encoded in the internal representations of a CNN and three Vision Transformers (ViTs), and we compare the similarity of these representations to those inferred from human psychophysics data. We find that the representation of textures is aligned in different ViTs, but not between the ViTs and the CNN; that ViTs form similar representations for textures of different complexity; that human performance in recognizing textures can be better predicted from ViTs representations rather than CNN representations. Taken together, these results suggest that ViTs may capture more faithfully than CNNs how texture patterns are visually processed by humans, and that the representations of texture stimuli in computational models may be driven by the network architecture.

---


### 117. [ArtMine: Discovering and Formalizing Artistic Processes](https://arxiv.org/abs/2607.08331)

**<font color=#1a73e8>作者：</font>** Kaustubh Kumar, Ashutosh Ranjan, Vivek Srivastava 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how artworks are created requires reasoning about the iterative decisions, material operations, and contextual influences that shape artistic production. While recent generative AI systems can synthesize artworks with high fidelity, they primarily model distributions over finished artifacts rather than the creative processes underlying their creation. In practice, artistic workflows are only partially documented through fragmented sources such as archival records, preparatory studies, correspondence, etc., making process-level understanding difficult to formalize computationally. In this work, we introduce ArtMine, a framework for discovering and formalizing artistic processes from heterogeneous historical evidence. Our approach synthesizes heterogeneous artwork evidence into a structured repository, from which a Peircean abductive agent infers evidence-grounded production steps. These steps are converted into a compositional graph and rendering prompt, then optimized through self-reflection over deviations between the generated and reference artworks. We provide a preliminary proof-of-concept case study using open-domain historical sources across multiple artists and artistic movements, demonstrating that fragmented documentary evidence can support coherent, interpretable, and auditable representations of artistic workflows. By modeling creative processes rather than only final artifacts, our work moves toward process-centred human-AI co-creativity systems that can support artistic interpretation, creative education, reflective collaboration, and computational studies of cultural production.

---


### 118. [XALPHA: A Memory-Driven AI Quant Researcher for Hypothesis-to-Code Alpha Discovery](https://arxiv.org/abs/2607.08332)

**<font color=#1a73e8>作者：</font>** Fengyuan Liu, Yuchen Fu, Yuqi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial markets are noisy, non-stationary, and high-dimensional, making it difficult to discover predictive and robust trading signals. Alpha discovery has evolved from manual factor design to machine learning, evolutionary search, and recent LLM-based frameworks, improving the efficiency of factor generation, search, and evaluation. However, existing methods still mostly automate isolated steps, rather than functioning as end-to-end quant researchers that can absorb external knowledge, close the hypothesis-to-code validation loop, and learn from accumulated discovery feedback. To fill this gap, we introduce XAlpha, a memory-driven AI Quant Researcher for continuous hypothesis-to-code alpha discovery. XAlpha maintains a multi-source research memory system that integrates report-grounded financial knowledge with discovery feedback from prior generations and research cycles. Guided by this memory system, a Macro Brain plans research themes and selects suitable Archetypes; a Micro Brain transforms the planned hypothesis pool into executable factor code and verifies ex-ante tri-alignment among the hypothesis idea, code logic, and financial plausibility; and a Cross Brain consolidates empirical outcomes into generation-level feedback, cycle-level summaries, and archetype-level research cues for future exploration. In this way, XAlpha turns alpha mining from isolated factor generation into a closed-loop research process that continuously reads, hypothesizes, implements, validates, reflects, and evolves. Experiments on CSI300 show that XAlpha achieves stronger overall alpha discovery performance than representative baselines.

---


### 119. [AutoAnchor: Stable Diffusion Unlearning Using Cross-Attention as a Manifold Surrogate](https://arxiv.org/abs/2607.08337)

**<font color=#1a73e8>作者：</font>** Siyuan Wen, Jiahao Zeng, Ningning Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion unlearning is essential for mitigating the generation of harmful or copyrighted content in text-to-image models. Current diffusion unlearning techniques determine the model update direction by either using alternatives of the target concept as an anchor or using empty prompts. The anchor-based method relies on manually and semantically-chosen anchors that risk biased unlearning, while the anchor-free method inherently suffers from unrobust unlearning due to unconstrained latent updates. In this work, we theoretically formalize such unstable diffusion unlearning issues under the manifold hypothesis and prove that lacking a manifold-proximal anchor inevitably induces significant normal-space drift that degrades unlearning performance. To achieve stable unlearning, we propose \mysysn, a two-stage framework that automatically synthesizes manifold-proximal anchors. However, direct geometric manifold optimization is computationally intractable. To address this challenge, \mysys introduces a novel cross-attention consistency loss which serves as a highly efficient surrogate of manifold proximity. Experimental results demonstrate that \mysys effectively achieves robust and unbiased unlearning across various state-of-the-art baselines, significantly improving targeted concept removal (by up to 31.04\% in CLIP score) and non-target utility (by up to 4.18\% in CLIP score). Moreover, \mysys can also be easily integrated into existing diffusion unlearning methods to enhance their unlearning performance (by 6.30\% for concept removal and 6.65\% for utility on average).

---


### 120. [TypeProbe: Recovering Type Representations from Hidden States of Pre-trained Code Models](https://arxiv.org/abs/2607.08339)

**<font color=#1a73e8>作者：</font>** Giuliano Gorgone, Fausto Carcassi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> State-of-the-art code models achieve impressive performance, yet the extent to which they internally encode type information remains poorly understood. We probe the residual streams of pretrained code models for internal type representations using a parallel dataset of Java and Python code examples. Our results show that cross-lingual type representations emerge even from untyped code. Moreover, we test whether hidden states linearly encode the result type implied by typed function application by training probes on one language to infer argument and result types in the other. Finally, we find that this structure is partly robust to lexical perturbations and cross-language syntactic variations. To the best of our knowledge, prior work on interpretability of code models has not directly targeted formal type semantics or cross-lingual type representations. We release our code and datasets.

---


### 121. [Spectral Analysis of Dueling Q-Learning](https://arxiv.org/abs/2607.08340)

**<font color=#1a73e8>作者：</font>** Donghwan Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Q-learning is a fundamental algorithm in reinforcement learning (RL) for solving discounted Markov decision processes (MDPs) when the transition kernel is unknown. The deep Q-network (DQN) extends Q-learning by using a deep neural network for Q-function approximation, which makes Q-learning applicable to more practical high-dimensional problems. Dueling Q-learning decomposes the Q-function into a value function and an advantage function and learns the two components jointly, which can improve learning efficiency. However, the theoretical understanding of dueling Q-learning is still limited. Recent work has initiated an analysis of tabular dueling Q-learning, but existing guarantees focus on a regularized formulation and leave the pure tabular update less completely understood. This paper strengthens that line of analysis by adding a direct interpretation of the centered tabular decomposition and by establishing convergence guarantees for the unregularized, unprojected constant step-size recursion. In particular, we derive an exact switching linear system representation for deterministic dueling Q-learning and a finite-time error bound in expectation for the sampled stochastic version. The analysis clarifies how the value and advantage updates act as different gains on the action-common (value function) and action-differential (advantage function) components of the Q-function.

---


### 122. [Grounded Event Extraction from SEC 8-K Filings with a Fine-Grained Taxonomy](https://arxiv.org/abs/2607.08346)

**<font color=#1a73e8>作者：</font>** Rian Dolphin, Joe Dursun, Jarrett Blankenship 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Form 8-K filings are the primary channel through which U.S. public companies disclose material events, but the SEC item codes attached to them are coarse: a single item spans routine administrative changes and chief executive departures, and many of the most market-moving disclosures fall into a catch-all item. Large language models make fine-grained labelling feasible at corpus scale, but only if the labels can be traced to the source text and shown to be reliable. We present a two-stage system that tags 8-K disclosures against a three-tier taxonomy of 119 event types. The first stage constrains output to valid taxonomy entries and anchors every tag to a verbatim quote via fuzzy n-gram validation; the second re-grades each cited quote against the category definition to produce a quality score. Applying the system to 292,984 filings from 2022 to 2026 yields 601,088 grounded event tags, which we release. Over 5,125 stratified tags, an LLM judge finds precision rises monotonically with the quality score, from 12% to 96%, while unsupported tags fall from 8% to near zero. Ablation shows the score is calibrated only when assigned in a dedicated second pass. An event study on unsigned abnormal returns confirms, without any language model, that the taxonomy separates economically distinct events sharing an item code.

---


### 123. [Certified Interventional Fidelity: Anytime-Valid, Adaptive Evaluation of Causal Claims in Mechanistic Interpretability](https://arxiv.org/abs/2607.08349)

**<font color=#1a73e8>作者：</font>** Amir Asiaee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability often evaluates explanations by intervening on a model: swapping hidden states, patching activations, ablating components, or comparing a compressed model to the original one. These experiments are usually summarized by a point estimate, even though the evaluation may be monitored while it runs or adapted toward suspected failures. This makes it hard to tell whether a reported fidelity or patching effect is a stable causal claim or a consequence of finite sampling and evaluation choices. We introduce Certified Interventional Fidelity (CIF), a statistical layer for interventional interpretability evaluations. CIF first writes the quantity being reported as a causal estimand: an expectation of a bounded score over a stated input distribution and a stated intervention distribution. It then provides confidence intervals and anytime-valid confidence sequences for this estimand, including under adaptive intervention sampling via bounded mixture importance weighting. We instantiate CIF with Hoeffding-style sequences and variance-adaptive betting sequences, the latter reducing certification cost by 10-30x in our experiments. On MNIST abstractions and GPT-2 Small IOI circuits, CIF certifies high-fidelity claims, shows when apparent method differences are not statistically supported, and makes sensitivity to the intervention distribution explicit.

---


### 124. [MobiDiff: Semantic-Aware Multi-Channel Discrete Diffusion for Human Mobility Data Generation](https://arxiv.org/abs/2607.08357)

**<font color=#1a73e8>作者：</font>** Rongchao Xu, Lin Jiang, Dahai Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human mobility data are essential for transportation optimization, urban planning, and resource allocation, yet real-world mobility data are costly to collect and difficult to share due to privacy concerns. Recent diffusion-based methods have shown promise in synthesizing realistic mobility patterns, but they typically rely on continuous or latent spatio-temporal traces, limiting their ability to natively model discrete semantic events with explicit region, activity, time, and interval structures. To address this issue, we introduce MobiDiff, an end-to-end discrete diffusion framework that efficiently generates mobility data by directly denoising multi-channel semantic skeletons, avoiding the costly interpolation, latent trace construction, and coarse-to-fine realization pipelines widely used in existing diffusion-based methods. Specifically, MobiDiff decomposes each human check-in event into spatial, activity, and temporal channels, and employs structured event-, group-, and channel-level masking to jointly capture trajectory-level mobility patterns and within-event dependencies. We evaluate generation fidelity, privacy-preserving, and efficiency on three large-scale real-world datasets from Atlanta, Boston, and Seattle. Results show that MobiDiff effectively preserves trajectory length and temporal interval distributions while remaining competitive across broader mobility statistics; it is also much faster than state-of-the-art methods, e.g., 5.3$\times$ faster than GeoGen on average during inference. These findings suggest that discrete diffusion offers an interpretable and efficient framework for synthetic mobility data generation.

---


### 125. [Echoes Across Vietnam's Highlands, Delta, and Coast: A Multilingual Corpus for Cham, Khmer, and Tay-Nung](https://arxiv.org/abs/2607.08362)

**<font color=#1a73e8>作者：</font>** Anh Trac Duc Dinh, Khang Nhat Hoang Vo, Vinh Cong Doan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vietnam's ethnic minority languages are almost absent from the field of Natural Language Processing (NLP), and the challenge goes beyond data scarcity: Cham, Khmer, and Tay-Nung differ sharply in script, Vietnamese contact, and standardization, conditions under which standard multilingual adaptation can learn the wrong signals. We introduce CKTN, the first corpus and benchmark for these languages (44,367 documents, 24M subword tokens), spanning continued pretraining, category classification, and summary-document retrieval. We show that existing multilingual encoders severely fragment these languages, and that common adaptation metrics can mislead: models may lower language-modeling loss or excel at lexical-overlap retrieval while still failing at semantic generalization across documents. We address this with a script-aware adaptation recipe - vocabulary augmentation combined with calibrated replaced-token pretraining - that prevents the discriminator from exploiting trivial script mismatches. The result is an encoder with substantially less fragmentation and the strongest classification performance among evaluated models, exposing the limits of lexical-overlap retrieval as an evaluation signal.

---


### 126. [FedOPAL: One-Shot Federated Learning via Analytic Visual Prompt Tuning](https://arxiv.org/abs/2607.08368)

**<font color=#1a73e8>作者：</font>** Lingyu Qiu, Daniela Annunziata, Stefano Izzo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the widespread deployment of basic models in edge intelligence, communication bandwidth has become a core bottleneck restricting the scalability of federated learning. Although one-shot federated learning alleviates this problem by minimizing communication rounds, existing iterative fine-tuning or knowledge distillation methods still face challenges such as high server-side computational costs and hyperparameter sensitivity. Analytical federated learning achieves efficient gradientfree aggregation using least-squares closed-form solutions, but in environments with non-independent and identically distributed data, its static feature assumptions fail, leading to feature manifold misalignment and severely impairing model performance. To address this contradiction, this paper proposes the FedOPAL framework. This framework adapts the visual prompts as feature rectifiers, actively correcting the feature distribution of heterogeneous data to a linearly separable space by applying local proximal constraints, thereby satisfying the theoretical assumptions of analytical federated learning. Experimental results show that FedOPAL not only significantly outperforms the original analytical methods on several benchmarks, but also achieves accuracy comparable to state-of-the-art iterative methods while maintaining zero server-side training costs, providing a new engineering paradigm for efficient collaboration of large models on the edge.

---


### 127. [Self-Adaptive Anomaly Detection with Reinforcement Learning and Human Feedback in Connected Vehicles](https://arxiv.org/abs/2607.08373)

**<font color=#1a73e8>作者：</font>** Matthias Weiß, Athreya Hosahalli Prakash, Maurice Artelt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Connected vehicles are autonomous cyber-physical systems whose behavior must be continuously monitored during operation to detect deviations from normal operation before they propagate into failures. Such evaluation is challenging because the systems themselves evolve: over-the-air updates, configuration changes, and shifting workloads alter the definition of normal behavior, causing static diagnostic methods to degrade silently over time. Existing approaches typically address either automated model adaptation or operator integration in isolation, rather than as a single coordinated supervisory loop.
This paper presents an online anomaly detection framework for autonomous CPS that integrates three coordinated mechanisms. A factorized deep Q-network with self-attention selects the most suitable detector from a candidate pool for each monitored service, exploiting inter-service dependencies in the microservice topology. An ensemble of three statistical drift detectors monitors the input distribution and raises an alarm only when all three concur, prioritizing precision over recall. A human-in-the-loop retraining mechanism, built around a pending transition buffer and a 60/40 prioritized replay strategy, allows the operator to incorporate expert knowledge while preserving the system's learned response to prior data distributions.
The framework is evaluated on a connected-vehicle testbed running an automated valet parking application across seven backend microservices. The attention-augmented agent achieves an F1 score of 0.69, compared to at most 0.11 for any single detector applied uniformly. Following a real software update that induces measurable concept drift, F1 drops to 0.52; after operator-triggered retraining, performance recovers to 0.65 on the new distribution while remaining at 0.69 on the prior one, demonstrating sustained adaptation without catastrophic forgetting.

---


### 128. [WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.08375)

**<font color=#1a73e8>作者：</font>** Xuerun Yan, Zhexi Lian, Nuoheng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving. However, existing methods either lack comprehensive world cognition or suffer from fragmented world foresight, inherently confining these models to reactive driving. To address this limitation, we propose WCog-VLA, a novel dual-level World-Cognitive VLA framework that successfully bridges semantic world forecasting with generative world evolution to achieve proactive autonomous driving. At the semantic level, WCog-VLA unifies world cognition and reasoning by incorporating 3D spatial perception and injecting agent tokens to capture the world dynamics, while concurrently enabling Game-theoretic Chain-of-Thought (Game-CoT) reasoning. At the generative level, we introduce the Aligned Decoupled Diffusion Transformer (ADDT) as a powerful generative world model that synthesizes physically-plausible joint multi-agent trajectories. Through scene representation alignment, ADDT reduces the number of denoising steps required and thus significantly accelerates inference. To facilitate strategic reasoning, we further construct a large-scale dataset featuring 85k Game-CoT annotations. Extensive experiments on the NAVSIM benchmark demonstrate that WCog-VLA achieves a State-Of-The-Art (SOTA) PDMS score of 92.9.

---


### 129. [Classical versus Deep Mirror-Symmetry Scoring: A Benchmark of Thirteen Methods](https://arxiv.org/abs/2607.08379)

**<font color=#1a73e8>作者：</font>** Maximilian Woehrer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantifying how mirror-symmetric an image is about a given axis (symmetry scoring) underpins applications from visual aesthetics to medical imaging, yet proposed scoring methods have never been compared on a common, statistically grounded protocol. We benchmark 13 scoring methods (nine collected from literature, four introduced here) spanning from classical features to frozen deep features, across four single-axis and five multi-axis datasets under a reflection-exact protocol with a chance-anchored, significance-tested discrimination skill. Deep backbones perform best on single-axis and harder multi-axis protocols. However, a classical histogram-of-oriented-gradients (HOG) descriptor trails the best frozen-network readout by a small (but significant) margin, is not statistically separable from the runner-up (a CNN-filter measure), and runs ~300x faster on CPU. Our results show that discrimination concentrates in mid-scale oriented features, where deep backbones peak at a low or mid stage, and HOG peaks at a mid cell size. Among existing methods, frozen deep features thus offer little over a tuned classical descriptor for measuring symmetry; whether task-trained deep scorers can do better remains open. We release the scorers and harness in imgsym, an open toolkit for image symmetry detection and measurement.

---


### 130. [Dynamics of Gradient Descent with Large Step Size Near a Manifold of Flat Minima](https://arxiv.org/abs/2607.08380)

**<font color=#1a73e8>作者：</font>** Lachlan Ewen MacDonald, René Vidal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An important quantity in the theory of gradient descent (GD) is the \emph{sharpness}, defined as the largest eigenvalue of the objective Hessian. Classical analyses typically require the step size to be uniformly smaller than twice the reciprocal of the sharpness, but this condition is frequently violated in the training of deep neural networks. Recent work bridges this gap in the setting of overparametrised least-squares with a \emph{single scalar output}, providing a normal form for large-step GD in a neighbourhood of an \emph{isolated} flat minimum and establishing three corresponding convergence results. In this paper, we extend this theory in two directions: (1) to overparametrised least-squares with \emph{vector-valued outputs} (including regression with arbitrarily many observations), and (2) to a neighbourhood of a \emph{manifold} of flat minima (which we show is essential for applications such as matrix factorisation). We generalise both the normal form and all three convergence theorems of \cite{macdonaldeos} to this broader setting, overcoming several technical challenges, including the solution of a singular partial differential equation via a novel method that may be of independent interest. We further show that our framework applies to deep matrix factorisation under mild assumptions, yielding several new structural results. In particular, we prove that the set of flat minima forms a fibre bundle over a product of spheres, and that the sharpness is Morse-Bott along this manifold.

---


### 131. [Secure QR Codes: Authenticity Verification via EdDSA Signatures and CBOR Certificates](https://arxiv.org/abs/2607.08383)

**<font color=#1a73e8>作者：</font>** Wojciech Jonderko, Wojciech Wodo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> QR codes are a ubiquitous part of daily life, widely trusted by millions. However, their lack of inherent security features has given rise to critical attack vectors, such as spoofing (quishing) on public infrastructure like self-service parking machines. To address this, we present a comprehensive evolution of secure QR code architectures. First, we evaluate a fully offline proof-of-concept leveraging EdDSA signatures (instantiated on the Ed25519 curve), CBOR-encoded certificates, and ZLIB compression, demonstrating that robust cryptographic integrity can be achieved within the QR code's strict static capacity. However, recognizing the scalability limitations of fully offline models-specifically the inability to perform immediate key revocation in massive smart-city IoT deployments-we subsequently propose a scalable Hybrid Web PKI architecture. This forward-looking model utilizes standardized JWKS endpoints, a Central Trust Registry, and URL fragments to ensure seamless backward compatibility with standard native cameras while providing dynamic, real-time validation for compliant applications. This dual-mode approach offers a practical, deployable path toward eliminating QR spoofing.

---


### 132. [Prompt Compression via Activation Aggregation](https://arxiv.org/abs/2607.08399)

**<font color=#1a73e8>作者：</font>** Thibaud Ardoin, Semira Einsele, Evis Bregu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models process prompts by propagating activations through dozens of layers before generating a response. We ask whether the task-relevant information contained in an instruction prompt can be compressed into a single activation vector and re-injected into the model, replacing the original token sequence? We show this is achievable using a learned weighted sum of activations extracted at an intermediate layer and injected at an early layer of the target LLM. The compressed vector preserves task-relevant information, incurring an accuracy drop of under $2\%$ relative to full prompt processing. Beyond its practical implications, including reducing per-query computation for fixed instruction prompts without reprocessing the original token sequence, our analysis reveals structure in the activation space of LLMs: (i) mid-layer representations transfer meaningfully to early layers, suggesting a degree of cross-layer compatibility in how information is encoded; (ii) a single activation vector encodes a quantifiable and recoverable amount of semantic information; (iii) a weighted sum of activations is a robust representation compressor.

---


### 133. [Swapping Faces, Saving Features: A Dual-Purpose Pipeline for Pedestrian Privacy in ITS](https://arxiv.org/abs/2607.08402)

**<font color=#1a73e8>作者：</font>** Roba H. Farouk, Catherine M. Elias  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale and diverse datasets are needed to train AI models to take real-time decisions for autonomous vehicles (AVs), an intelligent transportation system (ITS) application. Pedestrian intention and trajectory prediction are critical models used in AVs, requiring datasets involving diverse pedestrian images. Unrestricted access to these datasets imposes serious security risks, like identity theft and pedestrian tracking. The challenge is to apply privacy preservation procedures while maintaining the image attributes needed to train the models. Existing privacy methods may preserve the pedestrian's privacy, but degrade the image usability, which hinders the models' effectiveness. This work's focus is to implement a five-stage pipeline to protect pedestrians' privacy through face swapping while keeping the essential facial attributes intact. It should be tailored to satisfy the privacy needs of the Egy-DRiVeS dataset. Moreover, Roop and Ghost-v2 face-swapping models are evaluated. Provenly, Roop outperforms Ghost-v2 in various aspects, as will be discussed. Consequently, Roop is the face-swapping model to be used in the pipeline to strike the balance between pedestrian privacy via identity concealment and data usability via facial attribute preservation.

---


### 134. [Beyond Backpropagation: Monte Carlo Method Can Train Deep Neural Networks](https://arxiv.org/abs/2607.08406)

**<font color=#1a73e8>作者：</font>** Hong Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backpropagation (BP) dominates deep learning training, but its reliance on gradients brings inherent troubles -- vanishing and exploding gradients. The pursuit of gradient-free methods has long been a goal in the field of artificial intelligence. This paper shows that indeed the simplest Monte Carlo algorithm implemented on a single GPU -- randomly mutate a parameter, keep it if the loss decreases, otherwise retry -- can practically train deep networks. This gradient-free method does not even need common techniques such as batch normalization or residual connections to directly train sufficiently deep networks. More remarkably, its flexibility extends to several nontrivial scenarios: it enables pure pruning training, supports discrete weights, accommodates unconventional transfer functions such as Gaussian, and reveals the substantial redundancy of deep networks. We have demonstrated its feasibility on deep networks with more than 20 layers, single-hidden-layer wide networks with up to 16,384 hidden neurons, and even a simple Transformer architecture trained on both image classification (MNIST) and character-level language modeling (Tiny Shakespeare). This simple gradient-free method may offer a complementary perspective for understanding the self-organization and learning mechanisms of neural networks, and also provides an alternative route for building physically inspired deep learning systems.

---


### 135. [Track2Map: Online Deformable SLAM with Motion-Aware Pose Optimization in Robotic Surgery](https://arxiv.org/abs/2607.08408)

**<font color=#1a73e8>作者：</font>** Tianyi Song, Sierra Bonilla, Xinwei Ju 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian splatting is the current state-of-the-art for dense, deformable 3D anatomy reconstruction in robot-assisted minimally invasive surgery (RAMIS); however, most pipelines are offline and depend on accurate camera trajectory priors (often from robotic kinematics), limiting applicability when priors are missing or noisy. To address these limitations, we propose Track2Map, an online 3D Gaussian Splatting pipeline that jointly optimizes camera trajectory and 3D deformable scene representation directly from surgical video. Track2Map is therefore capable of robust 3D reconstructions when camera trajectory priors are either absent or noisy, and due to its online nature it effectively works as a Simultaneous Localisation and Mapping (SLAM) method. To stabilize optimization in the presence of tissue motion and ambiguous visual cues, we introduce a track-anchored deformation initialization using dense 2D point tracks. Track statistics are further utilized to disentangle camera motion from scene deformation by detecting static camera periods and reducing drift during incremental mapping. Experiments on StereoMIS show improved reconstruction quality and camera trajectory against competing SLAM methods, as well as compared to non-SLAM methods that utilize camera trajectory priors. The code is available at this https URL.

---


### 136. [Detecting Ladder Logic Bombs in IEC 61131-3 PLC Programs using ESBMC-PLC+: A Formal Verification Approach with Trigger Synthesis](https://arxiv.org/abs/2607.08417)

**<font color=#1a73e8>作者：</font>** Pierre Dantas, Lucas Cordeiro, Waldir Junior  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A Ladder Logic Bomb (LLB) is malicious control logic in a Programmable Logic Controller (PLC) program that lies dormant until a trigger activates a payload to manipulate actuators, forge sensor readings, or deny operator control. We observe that real malicious logic hides inside function-block bodies, which existing ladder-diagram verifiers drop from their intermediate representation (IR), making bombs invisible to provers. We present ESBMC-LLB, which uses ESBMC-PLC+ as its verification engine and adds a modeling layer that exposes function-block logic and recasts bomb detection as a formal verification problem: a scan-watchdog exposes non-termination payloads, and output wiring exposes actuator-forgery payloads as safety violations. k-induction gives an unbounded proof of bomb-absence across all scans, and the bounded model checker returns a counterexample that is the trigger - guarantees that signature, anomaly, and CFG-triage detectors lack. On the public Iacobelli 2024 dataset, ESBMC-LLB detects all 30 bombs and recovers every trigger; it also detects adaptive triggers (computed, opaque-arithmetic, multi-scan) that evade CFG-triage. We also report the first semantic model-checker evaluation on PLC-Defuser's SWaT corpus: our analog extension makes the full corpus parseable; on v1.0.0, it detects 149/150 bombs (99%) with zero false positives, recovering each trigger; on a later version with nonlinear non-termination bombs, detection drops to 49% as the SMT solver times out. We conclude that semantic model checking and CFG-triage are complementary - the former gives unbounded proofs, adaptive-trigger robustness, and handles Boolean/integer and linear analog logic; the latter leads to nonlinear analog non-termination, and we delineate where each wins.

---


### 137. [Predicting Male Fertility Using Machine Learning: A Semen Parameters Based Analysis with the VISEM Dataset](https://arxiv.org/abs/2607.08429)

**<font color=#1a73e8>作者：</font>** Shahnawaz Qureshi, Raja Khurram Shahzad, Muhammad Fozan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Male infertility is a significant yet often underdiagnosed aspect of reproductive health, with semen analysis serving as the cornerstone of clinical evaluation. To address this problem, this study investigates the use of machine learning algorithms to classify male fertility status based on key semen parameters, i.e., sperm concentration, motility, and morphology, using the VISEM dataset. This dataset includes semen samples from 85 participants, classified into three categories, i.e., Fertile, Sub-Fertile, and Infertile, according to the World Health Organization's criteria. After pre-processing and feature engineering, the dataset was used to train and assess multiple classification models using the LazyPredict framework. Among the more than 40 algorithms tested, the Nearest Centroid classifier achieved an accuracy of 94.2%, outperforming other models such as Support Vector Machines and Quadratic Discriminant Analysis. The model's robustness was validated using 5-fold cross-validation and multiclass ROC-AUC analysis. This study illustrates that machine learning models can provide fast, accurate, and objective assessments of semen quality, potentially supporting clinical decision-making in andrology and assisted reproductive technologies. These findings emphasize the growing potential of machine learning to enhance fertility diagnostics and inform patient-specific treatment strategies.

---


### 138. [Applying JEPA-Style Predictive Learning to JA4-Derived Network Fingerprints](https://arxiv.org/abs/2607.08465)

**<font color=#1a73e8>作者：</font>** Javier Izquierdo, Aygul Zagidullina  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> I-JEPA and V-JEPA learn by matching latent predictions to target encoder outputs rather than regenerating the original input, and this has worked well for images and video. We explore whether the same objective works for compact network fingerprints. We built JA4-JEPA, a Transformer-based model trained on JA4, JA4H, JA4S, and JA4X subfields drawn from JA4DB and CIC-IDS- 2017. The training data combines roughly 397K samples from both sources, though no single sample contains all four view families. We evaluated the learned representations with a frozen kNN probe on protocol-family classification across TLS, DNS, and SSH. On 39,416 heldout samples the model achieved a cosine similarity of 0.9899 and a kNN accuracy of 0.9220. These results indicate that JEPA-style predictive learning can produce useful embeddings from JA4-derived fingerprints, even with incomplete view overlap across sources.
Keywords: JA4, network fingerprinting, JEPA, predictive representation learning, self-supervised learning

---


### 139. [Frequency-Domain Multi-Modality Transportation Modeling](https://arxiv.org/abs/2607.08475)

**<font color=#1a73e8>作者：</font>** Jiewen Deng, Hangchen Liu, Junchen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-modality transportation refers to urban systems composed of multiple transportation modes, such as traffic flow and public transit, whose dynamics are coupled by shared temporal patterns. Accurate multi-modality transportation forecasting remains challenging because (1) different modalities exhibit distinct spectral characteristics and (2) interact unevenly across frequencies, whereas most existing methods operate primarily in the time domain or rely on coarse feature fusion. To address these limitations, we propose a lightweight yet effective Frequency-Domain Multi-Modality modeling (FreMo) that explicitly exploits the frequency domain to enable adaptive and selective cross-modality synergy. FreMo disentangles modality-wise spectral refinement from cross-modality synergy and supports plug-and-play integration with general time series backbones. Specifically, FreMo introduces a Modality-Wise Frequency Filter (MFF) to adaptively refine spectral components within each modality, emphasizing informative frequencies while suppressing noise. FreMo further incorporates a Frequency-Guided Synergy Integrator (FSI) that selectively aggregates information across modalities based on their relative contribution at each frequency, facilitating effective cross-modality knowledge sharing while mitigating negative transfer. Extensive experiments on real-world datasets show that FreMo consistently outperforms state-of-the-art baselines, with superior performance and generalization across diverse forecasting scenarios. The code is available at this https URL.

---


### 140. [VEGAS: Human-Aligned Video Caption Evaluation via Gaze](https://arxiv.org/abs/2607.08489)

**<font color=#1a73e8>作者：</font>** Shenghui Chen, Po-han Li, Ximeng Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models excel at video captioning, yet typically generate descriptions that fail to capture individual viewers' attention. We propose VEGAS (Video caption Evaluation via GAze Score), a training-free metric that leverages test-time gaze to sample personalized, attention-aligned text. It is a cross-modal, information-theoretic metric that quantifies how well a candidate caption matches a viewer's focus. To evaluate VEGAS, we curate a dataset of egocentric activities and instructional slides paired with synchronized gaze and reference annotations. We then select captions based on VEGAS via rejection sampling without model retraining. Experiments show that VEGAS-selected captions align significantly better with human focus and improve downstream caption-to-video retrieval, demonstrating the practical utility of incorporating viewer attention during inference.

---


### 141. [Drift-Aware Temporal Graph Rewiring (DATGR) for Adaptive Semantic Modeling in Biomedical Text](https://arxiv.org/abs/2607.08490)

**<font color=#1a73e8>作者：</font>** Bharathwaj Vijayakumar, Sahana K. Varadaraju  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical language evolves rapidly as new discoveries emerge, causing traditional text models to lose semantic fidelity over time. Static embeddings and co-occurrence graphs cannot capture such evolution, leading to performance degradation in retrieval and knowledge discovery tasks. This paper introduces a Drift-Aware Temporal Graph Rewiring (DATGR) framework that models concept evolution by dynamically updating co-occurrence edges based on estimated semantic drift. Instead of retraining embeddings for each time slice, DATGR performs lightweight, feedback-driven rewiring using a logistic update rule applied to edge weights. Evaluated on the Biomedical Multi-Relation Corpus (BIOMRC), the method achieved a mean Area Under the Receiver Operating Characteristic (AUROC) improvement of approximately 0.066 absolute difference (0.699 vs. 0.633) over a static baseline. Area Under the Precision-Recall Curve (AUPRC) remained comparable (0.738 vs. 0.744), showing that drift-aware adaptation enhances link-prediction recall without a loss in precision. These results demonstrate that edge-level adaptation effectively captures temporal semantic change in evolving biomedical text while remaining computationally efficient and interpretable.

---


### 142. [Ensemble Diversity Optimization for Subjective Supervision](https://arxiv.org/abs/2607.08493)

**<font color=#1a73e8>作者：</font>** Xia Cui, Ziyi Huang, N. R. Abeynayake  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subjective NLP tasks often exhibit systematic annotator disagreement, requiring models that represent uncertainty rather than collapse it. We introduce Ensemble Diversity Optimization (EDO), a prediction-space framework that jointly optimizes ensemble weights, effective cardinality, and calibration through a unified differentiable objective. EDO learns ensemble composition and size end-to-end via Gumbel-Softmax relaxation and incorporates a signed diversity regularizer, tuned on validation data, to steer optimization toward either preserving or suppressing disagreement. This regularization prevents ensemble collapse and enables controlled navigation of the utility-calibration trade-off. The framework integrates a soft F1 surrogate, class-weighted cross-entropy to address imbalance, and reliability-weighted diversity to regulate intra-ensemble variability. Experiments on four subjective text-classification benchmarks (ArMIS, ConvAbuse, HS-Brexit, MD-Agreement) show that EDO substantially improves probabilistic calibration, reducing cross-entropy (40-78% depending on baseline) and lowering Brier scores relative to Soft-CE, Soft-MD, Top-5 Voting, and WEL, while maintaining competitive F1 and better alignment with annotator distributions. These results demonstrate that jointly optimizing ensemble structure with a signed diversity regularizer provides an efficient, model-agnostic approach for modeling human subjectivity in supervised learning.

---


### 143. [Cross-seed explainability using Procrustes-conditioned Joint End-to-end Top-K Sparse Autoencoders](https://arxiv.org/abs/2607.08499)

**<font color=#1a73e8>作者：</font>** Bendegúz Váradi, Zoltán Kmetty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a Procrustes-conditioned Joint End-to-end Top-K Sparse Autoencoder (SAE) for extracting cross-seed universal features from independently trained BERT models. Cross-seed feature universality is a fundamental challenge in mechanistic interpretability: because dictionary learning is non-convex, independently trained networks learn misaligned feature spaces, so apparently identical features may differ by random initialization. We address this by computing an orthogonal Procrustes rotation between seeds' activation spaces before joint SAE training, combining Top-K sparsity, end-to-end downstream optimization, and an auxiliary dead-feature revival loss based on previous SAE literature. Evaluating on five independent seed pairs (ten BERT models) across three benchmark datasets (SST-2, Stanford Politeness, TweetEval Emotion), our full pipeline produces more universal features (Pearson r $\geq$ 0.70 across seeds) than post-hoc alignment baselines on all three datasets. A minimal qualitative analysis confirms that high-universality features encode interpretable sociolinguistic patterns.

---


### 144. [Early to Share, Late to Save: Synchronisation-Driven Communication Gating in Bandwidth-Constrained Cooperative VLN](https://arxiv.org/abs/2607.08504)

**<font color=#1a73e8>作者：</font>** Arav Gupta, Nivedan Yakolli, Avinash Gautam  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Most cooperative Vision-Language Navigation (VLN) methods assume unlimited communication, not considering real-world applications where bandwidth is restricted and information efficiency is critical. We introduce \textbf{bandwidth-constrained cooperative VLN} and propose \textbf{hindsight gating}: a lightweight supervised gate that labels communication-critical steps post-hoc from navigation failures, avoiding the high variance of REINFORCE. Contrary to the intuition that agents should communicate when uncertain, we observe a consistent counter-intuitive pattern: trained gates fire predominantly in early episode steps and more often when agents are confident, across all budget levels ($B \in \{1,3,5\}$). We explain this through \textbf{recurrent hidden-state alignment}: early communication injects grounded trajectory representations that persist and compound through subsequent Gated Recurrent Unit (GRU) updates, achieving $+0.072$ cumulative alignment gain with $B{=}3$ transmissions, approaching unconstrained communication ($+0.078$) at 260\% greater alignment efficiency than random gating ($+0.020$) and 320\% greater efficiency than entropy-based gating ($+0.017$). Our results establish a new communication regime for bandwidth-limited embodied agents: synchronise representations early, navigate independently later. Our codebase is available at: this https URL

---


### 145. [Systematic Evaluation of Learning Rate Scheduling Strategies Across Heterogeneous Architectures](https://arxiv.org/abs/2607.08511)

**<font color=#1a73e8>作者：</font>** Hafsa Mateen, Radu Timofte, Dmitry Ignatov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Choosing a learning rate scheduling strategy is critical to neural network training, but manual selection is costly and rarely exhaustive. While classical AutoML approaches often treat the scheduler as a secondary hyperparameter, we systematically investigate its impact on classification accuracy across a diverse pool of architectures. We evaluated 30 representative architectures from convolutional and transformer families within the LEMUR neural network dataset. Through automated source-code injection, we applied 25 scheduler configurations across nine PyTorch families, evaluating a total of 3,938 model variants on CIFAR-10. Our best configuration achieved a top-1 accuracy of 86.45%, with 237 variants exceeding 80%. The results show that the choice of scheduler depends heavily on the architecture: CosineAnnealingWarmRestarts and CyclicLR consistently outperform basic decay strategies. The resulting accuracy landscape, contributed to the LEMUR nn-dataset, provides a practical reference for principled scheduler selection.

---


### 146. [Beyond wheelchairs and blindfolds: Investigating disability stereotypes in T2I models with INCLUDE-BENCH](https://arxiv.org/abs/2607.08515)

**<font color=#1a73e8>作者：</font>** Sophia Lichtenberg, Albert Gatt, Judith Masthoff  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models have been shown to exhibit social biases. Prior work has mainly focused on gender, skin tone, and cultural representation within restricted occupational associations, and emerging benchmarks increasingly incorporate these dimensions. However, disability remains systematically underexplored. Current evaluation practices often fail to align with sociologically grounded definitions of stereotyping, limiting principled assessment of representational harms toward people with disabilities (PWD). To address this, we introduce INCLUDE-BENCH, the first large-scale benchmark for evaluating disability-related bias in T2I models. INCLUDE-BENCH comprises 119K generated images based on prompt design across multiple bias dimensions and both static and dynamic contexts. We evaluate 15 open-source and 2 closed-source models. Our key findings reveal that: (1) mobility-impaired and default disability prompts predominantly yield wheelchair depictions across all models; (2) disability-conditioned generations consistently exhibit less diversity; (3) stereotypical portrayals demonstrate stronger disability-text alignment; and (4) we introduce the Stereotype Content Model (SCM) Score, demonstrating that T2I models reflect real-world stereotypical associations.

---


### 147. [Stop Guessing When to Stop Testing: Efficient Model Evaluation with Just Enough Data](https://arxiv.org/abs/2607.08522)

**<font color=#1a73e8>作者：</font>** Ofir Arviv, Kristjan Greenewald, Yotam Perlitz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The inherent rigidity of fixed-size benchmarks makes them an inefficient tool for model evaluation. Diverse evaluation objectives, including model ranking, model selection and testing throughout development, demand varying levels of statistical power. The mismatch between fixed sample sizes and these diverse needs results in either excessive computational cost or compromised reliability - a critical concern for model evaluation. To overcome these limitations, we call for adoption of sequential testing in our field. We provide an adaptive evaluation framework, that provides a principled way to navigate the trade-off between efficiency and reliability in model evaluation. Our framework combines the established statistical paradigm of sequential testing with stopping criteria tailored to common evaluation needs such as diminishing returns detection, and minimum detectable effect size. We demonstrate its ability to adaptively manage the efficiency-reliability trade-off on the Open VLM Leaderboard, including, for example, a 80% reduction in computational cost compared to fixed-size evaluation (with a 2.5-point CI width allowance) while maintaining statistical significance.

---


### 148. [AI-guided stimuli discovery and generation to optimize facial emotion perception studies in autism](https://arxiv.org/abs/2607.08533)

**<font color=#1a73e8>作者：</font>** Kushin Mukherjee, Na Yeon Kim, Maren Wehrheim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding perceptual differences between autistic and neurotypical adults requires behavioral assays that are sensitive, reliable, and mechanistically informative. Facial emotion perception is a useful test case because group differences have been reported, but findings vary across studies. Here we show that this variability may reflect image-level sparsity: autistic-neurotypical differences in emotion judgments were concentrated in a small subset of diagnostic facial expressions rather than spread uniformly across stimuli. We trained population-specific artificial neural network models to predict image-level judgments for autistic and neurotypical participants, then used these models to select novel faces predicted to maximize group separation. In an independent cohort, model-selected images produced larger behavioral differences than matched random images. We then used the same models with a generative adversarial network to transform diagnostic images toward greater predicted group agreement. In phenotype-matched validation, synthesized images reduced behavioral separation relative to their matched originals. These results establish a model-guided framework for discovering and transforming stimuli that reveal population-specific perceptual differences. More broadly, they show how behavioral phenotyping can move beyond averaging across fixed stimulus sets toward optimized assays that identify the conditions under which neurodivergent perception diverges or converges.

---


### 149. [Whareformer: Learning to Track What is Where in Long Egocentric Videos](https://arxiv.org/abs/2607.08537)

**<font color=#1a73e8>作者：</font>** Jacob Chalk, Saptarshi Sinha, Dima Damen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The recently established 'Out of Sight, Not out of Mind' (OSNOM) task for egocentric videos focuses on tracking objects that are moved by the camera wearer, online, maintaining knowledge of instance locations throughout the video even when they leave the field of view or become heavily occluded. In this paper, we propose the first learning-based solution to the OSNOM task: Whareformer, a transformer-based model with two components: an updatable memory of established tracks and a track assignment module that associates observations with existing tracks in a feed-forward manner. Whareformer jointly reasons over evolving object appearance (what) and updated 3D location (where), and employs a dedicated New Track token to reason about novel objects.
Thanks to its design choices of using relative distances and evolving track representations, Whareformer is trained on a small set of 56 videos but achieves SOTA performance on 260 long test videos from three datasets: EPIC-KITCHENS-100 (unseen videos), IT3DEgo, and HD-EPIC, with significant absolute improvements over prior work.

---


### 150. [VocaDet: Sample-Driven Open-Vocabulary Object Detection and Segmentation via Visual Tokenization and Vector Database Retrieval](https://arxiv.org/abs/2607.08541)

**<font color=#1a73e8>作者：</font>** ZhiXin Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary object detection and segmentation aim to recognize arbitrary objects beyond predefined categories. Although recent vision-language and reference-based approaches have significantly advanced this field, they often rely on text prompts, limited visual examples, or expensive feature matching procedures, making them difficult to scale to large and continuously expanding object repositories. In this work, we propose VocaDet, a sample-driven open-vocabulary object detection and segmentation framework that learns object concepts directly from user-provided positive and negative sample collections without model retraining. The key idea is to transform continuous visual representations into discrete visual vocabularies and perform efficient retrieval-based recognition through a scalable vector database. Specifically, we employ DINOv3 as the visual feature extractor and apply agglomerative clustering with adaptive clustering sensitivity to generate multi-granularity visual tokens. These visual tokens, together with position-debiased representations and spatial topology information, are stored as expandable object memories in a vector database. During inference, query images are converted into visual tokens and efficiently matched against the stored object memories for object localization and segmentation. Furthermore, a background filtering mechanism is introduced to remove frequently occurring background patterns and reduce redundant retrieval operations in practical fixed-camera scenarios. Experiments on the UA-DETRAC dataset demonstrate that VocaDet achieves effective open-vocabulary detection performance without conventional detector training, while supporting continuously expandable recognition capability as additional positive and negative samples are accumulated.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-189](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
