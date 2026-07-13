# 📦 其他研究 | 2026年07月14日

> 本类共 **147** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-147**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-147**

---

### 101. [Learning Physics-Informed Surrogate Model of Linear Elastic Displacement Fields from Geometry](https://arxiv.org/abs/2607.09382)

**<font color=#1a73e8>作者：</font>** Rodolphe Barlogis, Ferhat Tamssaouet, Quentin Falcoz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work aims to develop a fast and physically consistent surrogate model for real-time structural health monitoring of fractured elastic domains. We propose a physics-informed DeepONet framework that predicts displacement fields from both boundary conditions and fracture geometry, using a dedicated encoding strategy for the latter and without relying on finite-element-generated training data. The traction-free condition on the fracture boundary is imposed weakly through a localized penalty term. The presented numerical example focuses on one representative fracture geometry, demonstrating the feasibility of the formulation and laying the groundwork for extensions to surrogate modeling across diverse fracture geometries.

---


### 102. [Federated Learning Architecture: Data Privacy and System Security Approaches](https://arxiv.org/abs/2607.09391)

**<font color=#1a73e8>作者：</font>** Cagdas Karatas, Hibanur Karadogan, Ahmet Yasin Ertug 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This study explores the integration of homomorphic encryption and differential privacy techniques to enhance data privacy and security in Federated Learning (FL) systems. FL allows data to remain on local devices, eliminating the need for centralized data collection; however, sensitive information may still be leaked during model updates. To address this issue, homomorphic encryption enables computations on encrypted data, while differential privacy prevents the extraction of individual information through statistical techniques applied to model outputs. The proposed architecture was tested on the Framingham, Pima Indians Diabetes, and Bank Marketing datasets, revealing that enhanced privacy can be achieved without significantly compromising model accuracy. Furthermore, the impact of data heterogeneity among clients on model performance was analyzed, and it was concluded that strategies such as the careful selection of differential privacy parameters and training settings, along with the use of larger datasets, can improve the efficiency of FL. The findings demonstrate that privacy-preserving and high-performance artificial intelligence systems can be securely applied in sensitive domains such as healthcare and finance.

---


### 103. [Fully Trainable Deep Differentiable Logic Gate Networks and Lookup Table Networks](https://arxiv.org/abs/2607.09399)

**<font color=#1a73e8>作者：</font>** Wout Mommen, Lars Keuninckx, Matthias Hartmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a novel method for both partial and full optimization of the connections in deep differentiable logic gate networks (LGNs) and lookup table networks (LUTNs). Our training method utilizes a probability distribution over a set of connections per gate/lookup table (LUT) input pin, selecting the connection with highest merit, all whilst the optimal gate types or LUT-entries are learned in parallel. We show that the connection-optimized LGNs outperform standard fixed-connection LGNs on the Yin-Yang, MNIST Handwritten Digits and Fashion-MNIST benchmarks, while requiring only a fraction of the number of logic gates. We achieve 98.92% on the MNIST dataset with two layers of 8000 gates. With only one layer of 8000 gates, we obtain 98.45%, showing that our method requires almost 50 times fewer gates compared to fixed-connection LGNs. Training stability up to ten layers has been ensured by employing a high learning rate, straight-through estimators and trimming constant-output gate types. Additionally, we present a LUT neuron description that enables stable training with backpropagation, tested up to 6-layer deep networks. The model requires four times fewer trainable parameters and still achieves a higher accuracy compared to the fixed-connection LGN training algorithm. Our connection-training algorithm also works well for the LUTNs, achieving an accuracy of 98.88% for two layers of 2000 6-input LUTs.

---


### 104. [On-Device Adaptive Battery Power Prediction for Electric Vehicles](https://arxiv.org/abs/2607.09400)

**<font color=#1a73e8>作者：</font>** Avik Bhatnagar, Anton Paule, Tobias Schuermann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive power management in Electric Vehicles (EVs) requires accurate power prediction. Although deep learning models have emerged as highly effective for time-series forecasting in this domain, their performance is prone to degradation when exposed to data with distributions different from the training data. We introduce a novel approach that enables on-device learning in resource-constrained EV systems to continuously adapt pretrained battery prediction models to new, unseen data. We leverage existing pretrained models by transforming them into adaptable versions that retain critical hyperparameter knowledge from their initial training. We comprehensively investigate both online and offline model adaptation strategies. Our results demonstrate significant improvements in forecasting performance across various models and time horizons, achieving mean absolute error reductions of up to 7.49\% and 14.88\% with online and offline adaptation techniques, respectively. This study highlights the substantial benefit of on-device adaptation, resulting in enhanced battery power predictions than unadapted model deployments in real-world EV scenarios.

---


### 105. [Data-Efficient Deep Learning: Empirical Guidelines for Training Set Size Estimation in Inertial Sensor Classification](https://arxiv.org/abs/2607.09402)

**<font color=#1a73e8>作者：</font>** Ofir Kruzel, Itzik Klien  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models dependency on large-scale inertial datasets presents a significant bottleneck in inertial sensor-based classification tasks, such as human activity recognition and smartphone location recognition. In these domains, data collection requires massive recording campaigns that are complex, time-consuming, and difficult to scale. Currently, data-driven guidelines for determining the minimum sample size required to reach a desired accuracy level do not exist. To address this gap, this study presents a systematic empirical evaluation of learning curve convergence rates in inertial classification. We introduce a unified framework that analyzes classification performance under both binary and multi-class scenarios, and derive an empirical formula to estimate performance relative to dataset size. Testing across six diverse, real-world datasets totaling 102.7 hours of inertial measurements demonstrates that accuracy follows a consistent logarithmic growth pattern, regardless of task complexity. Leveraging this finding, we propose a quantitative stability point metric, defined as the sample size required for the learning curve to stabilize within a predefined mean absolute percentage deviation of its asymptotic maximum. Our analysis reveals that models often reach practical stability with substantially fewer samples than traditional heuristics suggest. Ultimately, we offer a generalizable framework to extrapolate total data requirements from small-scale pilot studies, optimizing the tradeoff between recording effort and model reliability. These findings shift the prevailing paradigm from maximizing data volume toward optimizing data efficiency, offering concrete, data-backed guidelines for planning recording campaigns in inertial sensing applications.

---


### 106. [SYNRARE: Synthetic Rare Disease EHR Generation for ML Benchmarking](https://arxiv.org/abs/2607.09404)

**<font color=#1a73e8>作者：</font>** Nicolai Dinh Khang Truong, Richard Röttger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivation: Rare disease (RD) diagnosis is frequently delayed due to the similarities in symptoms to common disease variants. Machine Learning Algorithms applied to Electronic Health Records show promise for accelerating the diagnosis; however, legal and privacy concerns pose significant barriers. To address these issues, Synthetic Data Generation is an alternative method for obtaining Electronic Health Records and can be applied with any Machine Learning algorithm for benchmarking and development purposes. Despite the availability of Synthetic Data Generation algorithms, support for generating a subset of patients that differ in a definable degree from the majority to simulate patients with RD is often lacking.
Results: We present SYNRARE, a graphical user interface based on the Synthea framework that enables easier modification and generation of synthetic Electronic Health Records of RD patients, which differ only to a definable degree from patients with common diseases, thereby enabling the benchmarking and testing of algorithms under controlled technical conditions. SYNRARE enables researchers to rapidly benchmark their Machine Learning algorithms across any scenario.
Availability and implementation: SYNRARE, including detailed instructions for installing, is available at this https URL.

---


### 107. [Similarity search generalisation in contrastive learning with InfoNCE loss](https://arxiv.org/abs/2607.09405)

**<font color=#1a73e8>作者：</font>** Nick Whiteley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Similarity search is a primary application of embedding models trained by contrastive learning. For one of the most popular contrastive learning loss functions, InfoNCE, we show that the population risk with $k$ negative samples is $O(1/k)$ close to an expected cross-entropy which quantifies deviation between i) a softmax similarity search over unseen data using the learned embedding function, and ii) an idealised softmax search over the same data but using similarity implicitly represented in the positive sample generator. This complements existing interpretations of InfoNCE in the $k\to\infty$ limit which are phrased in terms of mutual information, and alignment versus uniformity in embeddings. To quantify generalisation performance, we introduce a new continuity bound for the InfoNCE loss, obtained via Gâteaux differentiation. The bound preserves the structure of averaging over negative samples present in the loss function and features an ``inverse temperature'' parameter which can be tuned to account for the algorithmic temperature. For embedding functions which are Lipschitz in a parameter, this yields a simple demonstration that the averaging effect of $k$ negative samples in the InfoNCE loss carries over to stabilisation of the generalisation error as $k$ grows.

---


### 108. [Action-Factored Multi-Agent Reinforcement Learning for Scalable Quantum Device Tuning](https://arxiv.org/abs/2607.09422)

**<font color=#1a73e8>作者：</font>** Edwin De Nicolo, Rahul Marchand, Cornelius Carlsson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-agent reinforcement learning is well suited to problems with large parameter spaces and exploitable local structure, such as the tuning of electrostatically-defined quantum-dot arrays. However, if parameter cross-talk is strong, a non-stationary environment from the perspective of any individual agent can destabilize learning - the same effect that plagues manual tuning of such systems. We propose using a factored representation of the action space, learned online, to decouple agents and minimize their interference. Our framework, QADAPT, uses this factorization to efficiently learn shared policies based on local measurements and rewards. With this modular strategy, we achieve zero-shot generalization to unseen quantum device sizes and maintain an approximately constant number of convergence steps to reach target regimes. This work provides a scalable route toward the rapid calibration of large-scale quantum processors.

---


### 109. [Parameter-Efficient Vision-Language Adaptation with Continuous Metadata Conditioning for Animal Re-Identification](https://arxiv.org/abs/2607.09443)

**<font color=#1a73e8>作者：</font>** Anil Osman Tur, Tonje Knutsen Sordalen, Kim Tallaksen Halvorsen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term animal re-identification (ReID) must remain robust to gradual morphological evolution and seasonal appearance shifts. Although recent vision-language models provide strong pretrained visual representations, adapting them to longitudinal ecological settings remains challenging, particularly under identity and temporal distribution shifts. We present a parameter-efficient CLIP adaptation framework for animal ReID and introduce a continuous metadata-conditioning mechanism that incorporates numerical attributes directly into the prompt representation during training. While low-rank visual adaptation, prompt-based supervision, and cross-modal alignment provide the adaptation framework, the proposed metadata-conditioning strategy constitutes the primary methodological contribution. By preserving the continuous structure of numerical metadata rather than discretizing it into textual categories, the proposed approach enables smooth modulation of the embedding space during training while maintaining a purely visual inference pipeline. Experiments on a seven-year longitudinal fish dataset and multiple wildlife benchmarks demonstrate improved performance under closed-set, open-set, and time-aware evaluation protocols. The results demonstrate that continuous metadata conditioning improves robustness to longitudinal appearance variation and temporal distribution shifts, while parameter-efficient adaptation enables a purely visual inference pipeline without requiring metadata at test time. Code and evaluation splits can be found at: this https URL.

---


### 110. [How Does Bayesian Causal Discovery Fail? Characterising Structural Consequences in Linear Gaussian Networks under Latent Confounding](https://arxiv.org/abs/2607.09449)

**<font color=#1a73e8>作者：</font>** Debargha Ghosh, Silja Renooij, Anna Kononova  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bayesian causal discovery is widely used for its ability to quantify epistemic uncertainty over directed acyclic graphs (DAGs) through posterior inference. However, its behaviour under latent confounding remains poorly understood, as existing work typically notes that confounding breaks identifiability without characterising how the posterior distribution over DAGs responds. In this work, we analyse posterior behaviour under latent confounding in linear Gaussian causal models, focusing on additive latent confounding between exactly two observed variables. We derive a critical correlation threshold above which the score function favours graphs with a spurious edge between the confounded variables, and show that this threshold decreases with sample size -- more data lowers the correlation required for the spurious edge to be favoured. Beyond this threshold, we characterize two distinct posterior failure regimes determined by the local structure around the confounded variables. Our findings are supported by exact posterior computations on multiple graph structures, demonstrating both the predicted failure regimes.

---


### 111. [Hydra++: Real-Time Hierarchical 3D Scene Graph Construction With Object-Level Shape Estimation](https://arxiv.org/abs/2607.09455)

**<font color=#1a73e8>作者：</font>** Hyungtae Lim, Nathan Hughes, Xihang Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene graphs provide a hierarchical abstraction of environments by encoding spatial entities, such as objects and places, and their relationships. However, existing scene graph systems model object geometry coarsely, relying on partial point clouds or class-level CAD templates, which limits instance-specific shape detail. This paper presents Hydra++, a system-level investigation into how learning-based object shape estimators can be integrated into a hierarchical 3D scene graph pipeline. Hydra++ incorporates category-agnostic shape estimation and a reprojection-mask consistency check to reject degenerate predictions from partial observations or imprecise segmentation. In its default CRISP-based configuration, Hydra++ performs online scene graph construction; slower estimators such as SAM3D are evaluated as modular alternatives to demonstrate generalization-latency trade-offs. Furthermore, to address the challenges of sparse and noisy depth measurements in outdoor environments, Hydra++ supports a hybrid LiDAR-camera configuration for large-scale operation, improving scene-level reconstruction quality. Experiments in both simulation and real-world outdoor campus scenarios demonstrate that Hydra++ improves object- and scene-level reconstruction quality. Project page is available at this https URL.

---


### 112. [Active rejection enables reliable generalization of universal machine-learning interatomic potentials](https://arxiv.org/abs/2607.09456)

**<font color=#1a73e8>作者：</font>** Mingxiang Luo, Xinnan Mao, Lu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Universal machine learning interatomic potentials (uMLIPs) bridge quantum-mechanical accuracy and large-scale molecular dynamics, but the cost of high-accuracy calculations such as r$^2$SCAN limits training to datasets that remain small relative to the open materials space. Strong average benchmark performance also does not guarantee reliable energy--force predictions for every structure. We propose Adaptive Multi-Teacher Routing (ATR), which reformulates high-fidelity data construction as a structure-wise decision problem under uncertainty. Using a small set of real r$^2$SCAN labels, ATR calibrates multiple pretrained uMLIP teachers and combines structural descriptors, teacher identity, and inter-teacher disagreement to estimate the reliability of each structure--teacher pair. It selects high-confidence predictions for pseudo-label generation and rejects structures for which no teacher is sufficiently reliable. With real r$^2$SCAN labels for only 0.2\% of candidate structures, ATR distils 2.89 million traceable r$^2$SCAN-level pseudo-labels for pretraining. On held-out r$^2$SCAN structures and the MP-r$^2$SCAN benchmark, a lightweight CHGNet trained on the ATR-generated dataset consistently outperforms the baseline and non-routed controls. Finite-temperature molecular dynamics further shows that ATR improves dynamical robustness across multiple material systems, maintaining stable trajectories where baseline simulations undergo catastrophic structural collapse. These results establish active rejection as an effective mechanism for converting multiple pretrained uMLIPs into a scalable and reliable data-construction system for high-fidelity uMLIPs.

---


### 113. [Triggering Stealthy Feature Map Backdoors via Physical Fault Injection in Embedded Neural Networks](https://arxiv.org/abs/2607.09473)

**<font color=#1a73e8>作者：</font>** Steyn Hommes, Vincent Dankbaar, Tanguy Stekke 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fault injection (FI) attacks on embedded neural network (NN) implementations primarily focus on inducing misclassification by corrupting weights or intermediate computations, overlooking their interaction with algorithmic adversarial threats. In this work, we present a cross-level attack that bridges implementation-level physical faults to algorithm-level adversarial attacks. By characterizing fault-induced data perturbations during NN inference, we connect FI with backdoor learning, enabling system-level attacks that jointly exploit implementation- and algorithm-level vulnerabilities. Specifically, we propose a precise fault-injection method that reliably manipulates targeted register values to tractable states during execution. Leveraging this level of FI precision, we propose a novel end-to-end feature map-level backdoor attack, where physically induced intermediate perturbations serve as stealthy triggers. Unlike conventional input-based backdoors, our trigger is activated only under physical faults, causing the NN to exhibit adversarial behavior that compromises system integrity while remaining benign during normal operation. We demonstrate that such physically triggered backdoors can be mounted on embedded NN platforms and remain effective against existing backdoor defenses that typically assume input-space triggers. We showcase the attack practicality using electromagnetic FI on convolutional neural networks implemented on ARM Cortex-M4 microcontroller, which is a common platform for constrained embedded applications. Our results highlight a novel attack vector at the intersection of hardware and algorithmic levels, stressing the need for defenses across abstraction levels.

---


### 114. [Foveation-Guided Dynamic Token Selection for Robust and Efficient Vision Transformers](https://arxiv.org/abs/2607.09480)

**<font color=#1a73e8>作者：</font>** Ibrahim Batuhan Akkaya, Kishaan Jeeveswaran, Bahram Zonooz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The human visual system (HVS) employs foveated sampling and eye movements to achieve efficient perception, conserving both metabolic energy and computational resources. Drawing inspiration from this robustness and adaptability, we introduce the Foveated Dynamic Transformer (FDT), a foveation-guided dynamic token-selection architecture that integrates these mechanisms into a vision transformer framework. The FDT exhibits strong resilience to various types of noise and adversarial attacks, despite not being explicitly trained for such challenges. This inherent robustness is achieved through the use of fixation and foveation modules: the fixation module identifies fixation points to filter out irrelevant information, while the foveation module generates foveated embeddings with multi-scale information. At the 50% fixation-budget setting, FDT achieves higher accuracy than DeiT-S (81.9% vs. 80.9%) while reducing multiply-accumulate operations by 34.57%, highlighting one operating point on its accuracy-efficiency trade-off. These attributes position FDT as an HVS-inspired step toward artificial neural networks that combine adaptive computation with improved resilience.

---


### 115. [Decoupling Language Guidance from Backbones for Text-Guided Medical Segmentation](https://arxiv.org/abs/2607.09481)

**<font color=#1a73e8>作者：</font>** Yungeng Liu, Xuanzi Fang, Haijin Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided medical image segmentation leverages clinical semantics to improve lesion delineation, yet many existing models bind cross-modal fusion, supervision, and decoder design into a task-specific architecture. Such tight coupling makes it difficult to reuse language guidance modules across heterogeneous vision and text backbones, and often requires redesigning the network when the encoder pair changes. This paper presents BTHA, a backbone-transferable hierarchical adapter framework for text-guided medical image segmentation. BTHA is built around a stable feature-level interface: given multi-scale visual features and a text representation, it injects semantic guidance through shape-preserving adapters while maintaining the decoder-side tensor contract. To make this interface effective, we introduce a Hierarchical Coarse-to-Fine Supervision Strategy that decomposes learning into global image-text alignment, multi-scale auxiliary localization, and boundary-aware final mask refinement. We further design a Scale-Adaptive Gated Semantic Guidance (SAGSG) adapter, where resolution-specific gates adaptively control textual injection and channel recalibration suppresses redundant cross-modal responses. Evaluations across diverse vision and text backbones show that the same adapter and supervision design remains effective across convolutional and transformer-based visual encoders as well as different language encoders. Experiments on four public datasets further demonstrate that BTHA improves strong text-guided baselines with modest computational overhead.

---


### 116. [SigLIP-HD by Fine-to-Coarse Supervision](https://arxiv.org/abs/2607.09488)

**<font color=#1a73e8>作者：</font>** Lihe Yang, Zhen Zhao, Hengshuang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality visual representation is a long-standing pursuit in computer vision. In the context of multimodal LLMs (MLLMs), feeding higher-resolution images can produce more fine-grained visual tokens. However, it introduces additional computational and design complexity, due to multiple forward passes and post-processing of increased tokens. Before simply adopting a higher resolution, have we truly unlocked the model's full perception capability at a standard resolution? Therefore, we study an interesting problem: how to achieve fine visual perception under lower cost without larger images. We present SigLIP-HD in this work. The core is a highly simple fine-to-coarse supervision design. We enforce the coarse feature of a mid-resolution image to mimic the fine-grained feature of its high-resolution version. We build this framework on the advanced SigLIP 2 model. Our final model produces better visual tokens at exactly the same inference budget. It is validated on extensive MLLM benchmarks and consistently delivers stronger results than our baseline model, especially on OCR-related tasks.

---


### 117. [Ceci n'est pas une pipe: AI systems as semantic abstractions](https://arxiv.org/abs/2607.09489)

**<font color=#1a73e8>作者：</font>** Jade Alglave, Patrick Cousot  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An AI system's output is not the fact or world state it appears to describe, but rather an engineered representation. We propose a semantic framework to describe AI systems, to be able to examine the correctness of such representations. To do so, we distinguish what is justified by accepted domain knowledge, what reference sources say, and what the system can currently use. This allows us to give precise definitions to common failures: extrapolation, refuted or unsupported assertion, sources versus knowledge mismatch, stale or refuted source, added hypotheses, unsupported use... We hope our framework gives a useful vocabulary for specifying and checking AI systems whose outputs, citations, tool calls, and world-changing actions must be justified by reliable claims and explicit authority rather than apparent fluency.

---


### 118. [Normalisation-Based Likelihood Ratio Estimation for Forensic Authorship Verification](https://arxiv.org/abs/2607.09501)

**<font color=#1a73e8>作者：</font>** Sadie Barlow, Andrea Nini, Edoardo Manino  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Authorship verification (AV) is the task of determining whether two texts were written by the same author. In a forensic context, the strength of AV evidence can be quantified using likelihood ratios. Most AV methods are score-based and deriving well-calibrated likelihood ratios from these scores requires a separate calibration model. This, in turn, requires additional amounts of case-relevant data, which is often time-consuming to obtain and prepare. This study proposes two novel normalisation techniques, the Square Root Correction and the Hapax Correction, for deriving likelihood ratios from the AV method LambdaG without the need of a calibration model (Nini et al. 2026). These corrections are designed to mitigate the overestimation of evidential strength that may result from long or highly repetitive texts. Performance is evaluated against logistic regression calibration across fifteen corpora and a range of text lengths (100-9,500 tokens), using the log-likelihood ratio cost (Cllr). The proposed methods achieve performance comparable to logistic regression calibration, with the Hapax Correction outperforming it in approximately 45% of tests (weighted by corpora). Furthermore, performance was more frequently close (within 5%) when the Hapax Correction was outperformed by logistic regression calibration, compared with the reverse comparison. Eliminating the need to train a calibration model reduces data-requirements, time and complexity, thereby increasing the accessibility and transparency of forensic text comparison. This combination of empirical performance and practical advantages supports the adoption of the proposed methods in forensic settings.

---


### 119. [DGSfM: Depth-Guided Scale-Aware Global Structure-from-Motion](https://arxiv.org/abs/2607.09507)

**<font color=#1a73e8>作者：</font>** Sithu Aung, Viktor Kocur, Yaqing Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Global Structure-from-Motion (SfM) is an efficient paradigm for recovering camera poses and sparse 3D structure from unordered images. However, its reliance on scale-ambiguous epipolar geometry makes global positioning sensitive to noisy baseline estimates and weak view-graph constraints, while false edges from visually ambiguous pairs can further degrade reconstruction. We propose DGSfM, a depth-aware global SfM pipeline that uses monocular depth maps as a scalable prior while preserving explicit multi-view optimization. For each image pair, we use a depth-aware relative pose solver to convert scale-ambiguous epipolar constraints into scale-aware relative pose constraints. We further improve robustness through view-graph filtering and depth-consistency-based correspondence pruning, which suppress false edges and matches that remain plausible under epipolar geometry alone. Finally, global scale averaging and depth-guided pose-point initialization align monocular depth maps into a common reconstruction scale and provide stable initialization for global positioning and bundle adjustment. Experiments on ETH3D and IMC2021 show that DGSfM consistently improves over strong global SfM baselines across sparse and dense matching front-ends, achieving substantial gains in pose accuracy. Code is available at this https URL.

---


### 120. [Learning When to Intervene on Habitual Behaviors: A Case Study in Oral Health Care](https://arxiv.org/abs/2607.09518)

**<font color=#1a73e8>作者：</font>** Bhanu Teja Gullapalli, Vivek Shetty, Anna L. Trella 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A central challenge for digital health interventions aimed at improving habitual behaviors is deciding when to deliver an intervention prompt. For many daily habits, such as tooth brushing or eating, individuals tend to act around a usual time of day, but this timing is not fixed and can shift as routines evolve. When intervention timing is selected in advance and held constant throughout a study, it can gradually become misaligned with behavior, causing interventions to potentially arrive after the behavior has already occurred or too early to be effective. In this work, we address this habitual timing misalignment in digital health interventions by proposing an online decision-making framework that continuously adapts intervention timing as individual behavior patterns change. Rather than treating intervention timing as a static design choice, our framework adapts it over time and integrates it into a sequential process that determines both when and whether to deliver an intervention. Using data from a deployed oral health intervention trial as a case study, we evaluate our approach using both observed data and simulated settings to assess how well different intervention timing strategies align with the timing of brushing events. Across these evaluations, we measure performance using a coverage-based metric that captures whether an intervention is delivered sufficiently close to a subsequent brushing event. We find that adaptive intervention timing consistently improves coverage compared to fixed intervention times based on user-provided input. The proposed framework is currently deployed in an ongoing randomized controlled trial of a digital oral health intervention, with preliminary results that are consistent with and further support our prior evaluations.

---


### 121. [Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference](https://arxiv.org/abs/2607.09520)

**<font color=#1a73e8>作者：</font>** Junfei Zhan, Haoxun Shen, Mingang Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are the perceptual backbone of embodied AI, but their energy footprint on edge hardware remains poorly understood. Existing efficiency efforts focus predominantly on reducing visual tokens, implicitly treating visual processing as the dominant energy cost. We overturn this implicit assumption through the first systematic energy profiling of on-device VLM inference, spanning five models across three architecture families, four input resolutions, and two hardware platforms (NVIDIA RTX 3070 and Jetson Orin NX). Our analysis yields three findings. First, average inference power is a model-intrinsic constant, invariant to input resolution, image complexity, and prompt type, with less than 5% variation across all conditions. This means that all energy variation across inputs must arise from variation in inference time, not from variation in power draw. Second, each output token costs 11 to 39x more wall-clock time than each input token due to the compute-bound and memory-bound asymmetry between prefill and decode, making output token count the dominant driver of both latency and energy. Third, image complexity, measured by the number of objects in an image, induces up to 4.1x energy differences at identical resolution. This variation arises not from increased visual processing cost, but from differences in output length. These findings expose a fundamental limitation of visual token pruning: even removing all visual tokens saves at most 10% of total energy for fixed-token models. Across models spanning 1 billion to 8 billion parameters, controlling output length saves up to 97% of total energy, with the energy dominance of decoding growing stronger at larger model scale. In short, the true energy bottleneck in edge VLM inference is not what the model sees, but how much it says.

---


### 122. [TSAI-MetaFraud: A Benchmark Dataset for Financial Fraud Transaction and Behavioral Risk Detection in Metaverse Ecosystems](https://arxiv.org/abs/2607.09528)

**<font color=#1a73e8>作者：</font>** Refat Ishrak Hemel, Ehsan Hallaji, Roozbeh Razavi-Far  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The emergence of metaverse platforms has created virtual economies that introduce new challenges related to fraud, bot activity, and illicit financial behavior. Despite growing interest in trustworthy metaverse analytics, existing datasets typically focus on user behavior, authentication, or financial transactions in isolation, limiting the development and reproducible evaluation of multimodal fraud detection methods. To address this gap, we present TSAI-MetaFraud, a multimodal, multi-task benchmark dataset for fraud analytics in virtual economies. TSAI-MetaFraud integrates behavioral, transactional, and graph-structured information while incorporating realistic fraud and automated bot scenarios. We define benchmark tasks including transaction fraud detection, cross-modal node classification, temporal link prediction, and weakly supervised fraud detection, and provide baseline evaluations using machine learning models and graph neural networks. By jointly capturing behavioral activity, financial interactions, and relational structure within a unified virtual economy, TSAI-MetaFraud provides a benchmark for advancing multimodal learning, graph mining, fraud analytics, and trustworthy AI in emerging metaverse ecosystems.

---


### 123. [FreyaTTS Technical Report](https://arxiv.org/abs/2607.09530)

**<font color=#1a73e8>作者：</font>** Ahmet Erdem Pamuk, Ömer Yentür, Ahmet Tunga Bayrak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Freya-TTS, a compact, tokenizer-free, Turkish-first text-to-speech model designed for highly reliable and efficient conversational synthesis. Freya-TTS is a 183.2M-parameter non-autoregressive conditional flow-matching Diffusion Transformer (DiT) that operates in the frozen continuous latent space of AudioVAE2 (16 kHz encode, 48 kHz decode), allowing the model to focus its capacity on text-to-latent mapping while inheriting high-quality 48 kHz reconstruction. We advance the framework along three key dimensions: (1) rule-free end-to-end modeling from a 92-symbol Turkish character vocabulary without a phonemizer, grapheme-to-phoneme frontend, or discrete speech tokenizer; (2) non-autoregressive parallel denoising, which predicts the entire latent sequence simultaneously over a predicted duration; and (3) a production-oriented two-stage post-training recipe consisting of single-speaker voice locking and short-utterance coverage, improving speaker consistency and robustness on short inputs. On the Freya-TR-Eval benchmark, Freya-TTS achieves a band-matched word error rate (WER) of 8.0% and character error rate (CER) of 3.0%, outperforming substantially larger open-source systems while using a fraction of their parameters. The model achieves a real-time factor of 0.11 on consumer GPUs and runs faster than real time on a laptop CPU, making it well suited for resource-constrained edge deployment. We release the model weights, training and inference code, and evaluation benchmark under the Apache-2.0 license.

---


### 124. [Statistically Undetectable Backdoors in Deep Neural Networks](https://arxiv.org/abs/2607.09532)

**<font color=#1a73e8>作者：</font>** Andrej Bogdanov, Alon Rosen, Neekon Vafa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show how an adversarial model trainer can plant backdoors in a large class of deep, feedforward neural networks. These backdoors are statistically undetectable in the white-box setting, meaning that the backdoored and honestly trained models are close in total variation distance, even given the full descriptions of the models (e.g., all of the weights). The backdoor provides access to invariance-based adversarial examples for every input, mapping distant inputs to unusually close outputs. However, without the backdoor, it is provably impossible (under standard cryptographic assumptions) to generate any such adversarial examples in polynomial time. Our theoretical and preliminary empirical findings demonstrate a fundamental power asymmetry between model trainers and model users.

---


### 125. [GatedLinear: Adaptive Routing of Complementary Linear Bases for Time Series Forecasting](https://arxiv.org/abs/2607.09537)

**<font color=#1a73e8>作者：</font>** Qitai Tan, Ruiwen Gu, Yilin Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting requires models to capture diverse, often mutually exclusive, temporal dynamics, from smooth trend continuation to nonstationary drift and strict phase-aligned recurrence. While recent deep learning models have improved accuracy, they typically force these diverse patterns through a single computational backbone governed by fixed algorithmic inductive biases (e.g., self-attention or spectral filtering). This single-mechanism approach often struggles with the profound heterogeneity of real-world series, where different variables and forecast horizons necessitate fundamentally different predictive treatments. To address this, we propose GatedLinear: a lightweight framework that frames forecasting as the adaptive routing of complementary linear bases. GatedLinear leverages a pool of three specialized mechanisms: a global trend-seasonal basis for smooth projection, a difference-based incremental basis for nonstationary drift, and a phase-aligned recurrence basis for explicit cyclic reuse. To dynamically orchestrate these distinct behaviors, we introduce a Tri-Factorized Fusion Gate that disentangles routing decisions into channel-specific preferences, horizon-aware offsets, and phase-indexed biases derived from known future time marks. This design allows the model to perform highly granular, point-wise soft routing across different predictive regimes without stacking computationally heavy neural modules. Experiments on standard benchmarks show that our method achieves state-of-the-art or highly competitive accuracy against recent complex foundational models, while offering explicitly interpretable routing patterns and operating with a substantially smaller parameter footprint.

---


### 126. [Portable Acceleration of Learning With Errors KEMs for Post-Quantum Cryptography](https://arxiv.org/abs/2607.09541)

**<font color=#1a73e8>作者：</font>** Tiziana Liberati, Nitin Shukla, Simone Rizzo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The transition to post-quantum cryptography (PQC) is driving demand for implementations that can meet the computational requirements of real-world applications. Among the proposed PQC constructions, Learning With Errors (LWE) based key encapsulation mechanisms (KEMs) are particularly attractive due to their strong security foundations, but they incur substantial computational costs from matrix operations and large-scale cryptographically secure random number generation. These characteristics position GPU acceleration as an effective approach for lowering the computational overhead of lattice based cryptographic schemes. In this work, we present a portable GPU implementation of a plain LWE based KEM using OpenMP Target offloading. Unlike most existing GPU implementations, which rely on CUDA specific optimizations, our approach uses a single source code base that executes on both NVIDIA and AMD accelerators. We evaluate the proposed implementation on different accelerator architectures, analyzing performance benchmarking, runtime profiling, scalability analysis, and energy to solution measurements. Experimental results show that OpenMP Target offloading delivers substantial acceleration over a multicore CPU baseline while preserving source level portability across heterogeneous GPU ecosystems. Cross platform analysis identifies NVIDIA GH200 and AMD MI300X as the most effective platforms for this memory bound workload, while profiling indicates that memory system organization and CPU GPU interaction play a more critical role than peak compute capability alone. These findings demonstrate that portable GPU acceleration can significantly reduce the computational overhead of PQC while avoiding vendor lock in, thereby facilitating the deployment of quantum resistant cryptographic infrastructures.

---


### 127. [CoCoT-EEG: Contrastive-Pretrained Multiscale Convolutional Transformer for EEG Decoding](https://arxiv.org/abs/2607.09543)

**<font color=#1a73e8>作者：</font>** Gabriel Mahuas, Victoria Shevchenko, Ugo Tanielian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised pretrained foundation models (FM) have shown early promise for non-invasive electroencephalogram (EEG) decoding applications. Many recent large-scale models converged on the approach of tokenizing raw EEG followed by masked reconstruction pretraining. However, this recipe has been shown to be suboptimal for data, like EEG, with high noise amplitude and information confined to limited dimensions such as narrow frequency bands. Building on this insight, we develop a novel contrastive-pretrained EEG model with multiscale temporal convolution input layers and Transformer encoder blocks (CoCoT). CoCoT matches or beats state-of-the-art reconstruction-pretrained EEG models on extensive benchmark decoding tasks with heterogeneous electrode configurations. Furthermore, CoCoT trained from scratch outperforms previous single-task decoding models and even rivals pretrained models, showcasing the architecture's flexibility and data efficiency. Through systematic ablations, including model architecture and pretraining objective, we demonstrate the viability of contrastive learning for building EEG FMs while suggesting key architectural design considerations, prompting further investigations in alternative large-scale pretraining strategies.

---


### 128. [The Count Is There, but Misaligned: Understanding and Correcting Counting Failures in VLMs](https://arxiv.org/abs/2607.09544)

**<font color=#1a73e8>作者：</font>** Ahmed Oumar El-Shangiti, Abzal Nurgazy, Hilal AlQuabeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite strong performance on many multimodal tasks, vision-language models (VLMs) still struggle with basic object counting. We investigate whether this reflects missing internal knowledge or a gap between internal representations and verbalized outputs. Training simple probes on activations from four VLMs across five counting datasets reveals that nonlinear probes can reliably detect counting errors, suggesting that VLMs often encode the correct count even when they output the wrong answer. SVCCA analysis shows that probes trained on ground-truth counts and probes trained on model outputs occupy a partially shared activation subspace but read out along misaligned directions. We further validate our findings using a causal steering intervention, proving that strengthening the direction of count-identified probes does improve model counting performance. Motivated by this result, we propose a detector-guided self-correction method that selectively re-prompts the model only when an internal error detector predicts failure. This simple inference-time intervention improves counting accuracy by up to 15.6 absolute percentage points, without any parameter updates. Our results establish activation-based error probing as both a practical tool for improving VLM counting and a mechanistic lens on the gap between internal knowledge and model outputs.

---


### 129. [Graph-Regularized Low-Rank Matrix Completion by Variable Projection](https://arxiv.org/abs/2607.09546)

**<font color=#1a73e8>作者：</font>** Benoît Loucheur, P.-A. Absil, Michel Journée  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the low-rank matrix completion problem by incorporating graph regularization into the existing Riemannian Trust-Region Matrix Completion (RTRMC) framework. The latter uses the geometry of the low-rank constraint to remodel the problem as an unconstrained optimization problem on a single Grassmann manifold. Our approach, named Graph-Regularized RTRMC (GR-RTRMC), exploits the inherent relationships between rows and columns of the matrix. By using these relationships, we aim to improve the accuracy and robustness of matrix completion, particularly in scenarios where the underlying data exhibits strong correlations between rows or columns.

---


### 130. [Beyond Fixed Representations: The Vocabulary and Verifier Gaps in Open-Ended AI](https://arxiv.org/abs/2607.09560)

**<font color=#1a73e8>作者：</font>** Yuan Cao, Haiqian Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern AI systems are increasingly being evaluated for their ability to reason, code, prove theorems, use tools, and long-horizon research tasks. These are powerful capabilities, but they share a structural limitation: the representational frame within which the model operates, including its conceptual vocabulary, the space of admissible solutions it can search, and the criteria by which success is evaluated, is typically fixed and supplied in advance. This paper argues that building stronger intelligent systems capable of open-ended innovation requires additional classes of operations: the creation, stabilization, and reuse of new representational primitives, which alter the space being searched rather than simply searching within it.
We characterize the distance between current AI systems and genuinely open-ended intelligence through two gaps. The first is the vocabulary gap, the difficulty of inventing and stabilizing new representational primitives rather than merely recombining existing ones. The second is the verifier gap, the difficulty of judging the value of a new primitive when its full payoff may be visible only after future reuse. We interpret both gaps through a unified framework of intelligence as cognitive discrepancy reduction. By viewing intelligent behaviors as a sequence of cognitive transformations, we distinguish intra-space transformations which operate within a fixed representational frame, from generative transformations which may modify the frame itself. On this basis, we propose a ladder of innovation autonomy and outline several directions for advancing open-ended AI, including objectives that reward useful representational change, persistent memory architectures for invented primitives, and adaptive verification mechanisms capable of evolving alongside the representations they evaluate.

---


### 131. [Conceptual Networks for Cross-Linguistic Idiomatic Expressions:A Feature-Based Graph Approach](https://arxiv.org/abs/2607.09576)

**<font color=#1a73e8>作者：</font>** Kiran Pala, Punam Silu, Lixun Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present an interpretable network-based framework for representing idiomatic and figurative meaning across eight typologically diverse languages, totaling 160 conventional expressions, the large majority of which are idiomatic. Each expression is annotated with binary conceptual features (containment, concealment, emotional, social, etc.) derived from cognitive-linguistic theory, and pairwise Jaccard similarities define a weighted graph. Community detection reveals that idioms cluster by conceptual schema rather than by language, producing a structure consistent with cognitive-linguistic predictions. The conceptual network captures unique semantic information not present in distributional embeddings, can be scaled via automatic annotation with LLMs, improves downstream idiom detection, and remains robust when enriched with corpus frequencies. Cross-lingual transfer experiments show that conceptual proximity alone can identify acceptable translation equivalents across five language families, with substantial gains over embedding-based baselines. Ablation studies demonstrate that all three feature dimensions -- schemas, roles, and valence -- contribute non-redundantly to both the network's organizational properties and its performance on idiom detection, and that specific graph-derived signals (community membership, neighbor similarity) are particularly informative. The framework offers an interpretable, cross-linguistically stable representation of idiomatic meaning, combining theoretical grounding with practical utility.

---


### 132. [Knowledge Graphs and Explainable AI as Complementary Resources for Urban Mining](https://arxiv.org/abs/2607.09578)

**<font color=#1a73e8>作者：</font>** Jan Gronewald, Andreas Emrich, Nijat Mehdiyev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pre-demolition assessment, the regulated audit process at the heart of urban mining, is an information process in which AI support must serve qualified auditors who remain accountable for the decisions taken. The relevant unit of value is not prediction accuracy alone, but the defensibility of the supported decisions: their legibility, plausibility, sourcing, and contestability. Explainable AI techniques and domain knowledge graphs each address parts of this requirement, and existing taxonomies have catalogued their integration. The literature is descriptively rich but structurally under-specified: what remains less developed is a structural account of why specific integrations produce artefacts neither resource can provide alone. This paper offers a complementarity-theoretic interpretation grounded in the IS resource-based tradition. We propose four consolidated KG-XAI integration modes (Lifting, Constraining, Typing, and Revising), each defined as a typed operation over XAI artefacts and knowledge-graph substrate structures. Each mode unlocks a distinct property of defensibility and contributes to the kind of regulatory artefact pre-demolition assessment demands. A fire-door example from the urban-mining process illustrates the modes using the W3C Linked Building Data stack and valuation extensions.

---


### 133. [Wan-Dancer: A Hierarchical Framework for Minute-scale Coherent Music-to-Dance Generation](https://arxiv.org/abs/2607.09581)

**<font color=#1a73e8>作者：</font>** Mingyang Huang, Peng Zhang, Li Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating long-duration, high-definition, and rhythmically synchronized dance videos directly from music remains a significant challenge, primarily due to the temporal constraints of current diffusion models, which typically fail beyond 20 seconds. Existing approaches, whether they rely on intermediate 3D skeletons or on end-to-end video synthesis, suffer from temporal drift, identity inconsistency, and repetitive motion patterns when extended to longer horizons. To address these limitations, we propose a novel hierarchical framework for minute-scale coherent music-to-dance generation. Our method decouples the process into global keyframe planning and local temporal refinement, leveraging full-track musical context to ensure long-range coherence. Key innovations include dynamic frame rate adaptation via time-mapped RoPE embeddings for precise alignment, an optical-flow-based loss function to enhance motion continuity, and motion-speed control to preserve high-fidelity details during rapid movements. Extensive experiments demonstrate that our framework surpasses the conventional duration barrier, generating stable, 720p/30fps videos exceeding one minute with superior temporal stability. Furthermore, the model exhibits robust versatility across five distinct dance genres, conditioned on both audio and textual prompts, establishing a new state-of-the-art in coherent, long-form dance video synthesis.

---


### 134. [KnitID: Machine-Knitted RFID Antennas for Battery-Free Authentication, Localization and Interaction](https://arxiv.org/abs/2607.09584)

**<font color=#1a73e8>作者：</font>** Weiye Xu, Yue Xu, Devin Murphy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Battery-free RFID systems offer a scalable and maintenance-free approach to interaction. We present KnitID, a machine-knitted textile RFID antenna design that enables on-body authentication, localization, and interaction. Unlike prior antenna designs, KnitID achieves a compact antenna form factor (60mm by 8mm) by integrating magnet wire into the unique loop-over-loop structure of machine knitting. This structure reduces the size of conventional loop antennas by around 90\%, while also providing 30\% longer sensing ranges than standard dipole designs with similar size on the human body. The compact form factor creates new opportunities to embed multiple RFID tags across the human body, enriching backscatter signals and supporting a broader range of battery-free on-body interactions. To demonstrate this capability, we build an interactive sleeve to support wearer authentication, spatial localization, and interaction detection. Through technical evaluations, we show the feasibility of KnitID to provide diverse and battery-free interactions on knitted user interfaces.

---


### 135. [Tokenizer Transplantation: Mitigating Autoregressive Collapse in Edge-Efficient Bengali ASR](https://arxiv.org/abs/2607.09598)

**<font color=#1a73e8>作者：</font>** Sanjid Hasan, Md. Abdur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lightweight speech recognition models are critical for edge deployment, yet highly optimized architectures like Moonshine often fail on morphologically rich, non-Latin languages such as Bengali. This study identifies the root cause of this failure as the model's English-centric byte-level tokenizer, which fragments Bengali words into high-fertility byte chains and triggers catastrophic autoregressive collapse during inference. To resolve this, a novel vocabulary transplantation pipeline is proposed to replace the decoder vocabulary with the native-script BanglaBERT WordPiece vocabulary and resize the corresponding token embedding matrix. Experimental results demonstrate a reduction in token fertility from 9.16 to 1.30. By decreasing autoregressive sequence length by 85.8%, decoding instability is entirely mitigated. When evaluated on the 882-hour Lipi-Ghor dataset, the modified architecture achieves a competitive 21.54% Word Error Rate (WER) and a Real-Time Factor (RTF) of 0.0053. Ultimately, this research provides a scalable, reproducible blueprint for cross-script adaptation of compact ASR models without the need for resource-intensive pre-training.

---


### 136. [Mosaic: Runtime-Efficient Multi-Agent Embodied Planning](https://arxiv.org/abs/2607.09603)

**<font color=#1a73e8>作者：</font>** Kunjal Panchal, Saayan Mitra, Sunav Choudhary 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent embodied planning remains impractical due to prohibitively high execution latency. We identify failed actions as the dominant bottleneck, stemming from two core challenges: inaccurate state tracking under partial observability and inefficient coordination that produces redundant or conflicting actions. We introduce Mosaic, a runtime-efficient multi-agent planning framework that addresses both challenges. Mosaic maintains accurate yet lightweight state tracking through agent-centric semantic memory that stores objects in relative coordinates, enabling geometric transformations and coordination. It ensures efficient coordination through Integer Linear Programming that allocates actions at every planning step, enforcing physical feasibility and inter-agent coordination constraints. Across AI2-THOR and search-and-rescue benchmarks, Mosaic achieves 27-32% faster execution, 30-33% fewer LLM calls, 25-31% fewer steps, and 4-10% points higher success rates. These results demonstrate that efficient memory and constraint-guided coordination are critical for scalable, low-latency multi-agent planning.

---


### 137. [Toward Real-Time Sentence-Level Sign Language Translation](https://arxiv.org/abs/2607.09611)

**<font color=#1a73e8>作者：</font>** Thanh-Hoang Nguyen Doan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most sign language understanding systems operate at the level of isolated signs, limiting their usefulness in natural communication. We study sentence-level sign language translation (SLT) with the primary goal of real-time deployment rather than proposing a new translation architecture. We fine-tune a SHuBERT-ByT5 translation stack on a uniformly sampled 9,872-example subset of How2Sign, selected because of compute and storage constraints, using QLoRA while keeping SHuBERT frozen. The model obtains a validation BLEU of 16.7 and, on the test split, BLEU 15.9 and BLEURT 44.7. The main contribution is a hardware-aware streaming system: a Raspberry Pi 4B reference client provides camera capture, local text display, and speech output, while compute-intensive perception and translation run on a CPU/GPU backend. The capture protocol remains client-agnostic, so the same backend can serve a browser, phone, or laptop. Chunked ingestion, bounded queues, parallelized perception, temporal reordering, and a sentence-boundary state machine reduce mean post-finalization response latency from 1.873 to 1.354 seconds (27.71%) and P95 latency from 2.919 to 2.130 seconds (27.03%) over the complete 9,872-example working subset.

---


### 138. [Indirect and Direct AI Scaffolding for Computational Problem Posing: A Pilot Experience Report](https://arxiv.org/abs/2607.09628)

**<font color=#1a73e8>作者：</font>** Shayla Sharmin, Mohammad Fahim Abrar, Mohammad Al-Ratrout 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Problem posing is a valuable learning activity in computing education, encouraging learners to actively construct, refine, and reflect on problems rather than simply solving them. This experience report presents the design and pilot deployment of two LLM-powered scaffolding systems for supporting problem posing across two computational scenarios with different levels of task openness. Both systems assessed student-generated problems using Bloom's Taxonomy-based criteria and applied the same assessment framework, differing only in output modality: one provided guiding questions (Indirect scaffolding), while the other offered worked examples (Direct scaffolding). We conducted a within-subjects, counterbalanced pilot study with 20 graduate students and collected problem-quality ratings, user-experience surveys, and post-session interviews. Our deployment showed that both systems supported problem refinement in complementary ways, each offering distinct benefits. Direct scaffolding produced greater immediate improvements, while interviews showed that participants valued Indirect scaffolding for promoting deeper reflection on their own problem design. Based on these findings, we suggest sequencing the two modalities by beginning with Indirect scaffolding to promote reflection, then shifting to Direct scaffolding when learners become stuck. These lessons offer an initial practical strategy for integrating LLM-based scaffolding into computing classrooms.

---


### 139. [4DR360: State Reasoning for Joint 3D Detection and Occupancy Prediction in 4D Radar-Camera Full-Scene Perception](https://arxiv.org/abs/2607.09629)

**<font color=#1a73e8>作者：</font>** Xiaokai Bai, Lianqing Zheng, Runwei Guan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable autonomous driving requires full-scene perception that couples foreground objects with dense semantic layout. Recently, 4D millimeter-wave radar has emerged as a robust and affordable sensor, yet its sparse returns make radar-camera fusion necessary for comprehensive scene understanding. Existing radar-camera methods mainly optimize detection, while dual-task systems usually decode boxes and occupancy with limited interaction. To address this gap and advance radar-based multi-task learning, we propose \method, a 4D radar-camera framework for 360$^\circ$ full-scene perception, which models semantic occupancy as a persistent scene state rather than a terminal output. \method{} follows a cross-modal state reasoning paradigm, where the occupancy state is modeled and propagated through stages for coarse-to-fine feature aggregation. Specifically, State-guided BEV Enhancement (SBE) strengthens intra-frame BEV representation, while Doppler-guided Temporal Fusion (DTF) preserves state evidence over longer temporal horizons. Beyond the model, we further extend ManTruckScenes with satellite-map-based generated occupancy labels and pair it with OmniHD-Scenes in a unified cross-dataset detection-and-occupancy protocol. The resulting experiments cover accuracy, robustness, ablation, and efficiency under one radar-camera multi-task evaluation framework. Code and labels will be released upon acceptance.

---


### 140. [The Effects of Synthetic Data and Label Distribution on Canola Branch Counting](https://arxiv.org/abs/2607.09630)

**<font color=#1a73e8>作者：</font>** Amirsalar Darvishpour, Mikolaj Cieslak, Adam Runions  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collecting annotated plant images for automated phenotyping is often slow and expensive. Plant models simulating growth and development can generate unlimited synthetic images with exact labels. However, previous work has established that whether incorporating synthetic data improves performance depends on the ratio of synthetic to real images and the label distribution of the synthetic dataset. To systematically quantify both factors, we train ResNet-18 models on a canola branch-counting task using a calibrated L-system plant model. We vary each factor independently. Synthetic-to-real ratios of 1:5 to 1:22 broadly improve performance; the best ratio (1:7) reduces mean absolute difference by 7.6% over real-only training. For label distribution, a uniform synthetic distribution is strongly suboptimal (abs. diff. of approximately 1.70); interpolating 90% toward the real distribution yields abs. diff. 0.927, whereas Gaussian smoothing of the real label distribution yields the best overall result (abs. diff. 0.912, a 14.7% improvement over real-only). A minimum of 10 synthetic images per label offers a simpler alternative with modest gains, while 100 per label over-corrects and hurts performance.

---


### 141. [Semantic Pareto-DQN: A Multi-Objective Reinforcement Learning Framework for Financial Anomaly Detection](https://arxiv.org/abs/2607.09641)

**<font color=#1a73e8>作者：</font>** Cláudio Lúcio do Val Lopes, Lucca Machado da Silva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial anomaly detection suffers from extreme class imbalance, causing traditional single-objective algorithms to exhibit ``fraud collapse'', defaulting to the majority class and failing to balance anomaly interdiction with customer friction. To overcome this without distortive data resampling, we propose the Semantic Pareto-DQN, a multi-objective reinforcement learning framework. Our approach synthesizes heterogeneous transaction features into cohesive natural-language narratives, encoded by large language models, thereby producing a robust, scale-invariant state representation. The agent optimizes a vectorial reward that explicitly decouples financial efficacy, operational friction, and semantic discovery. By mapping the continuous Pareto frontier, the system dynamically navigates the asymmetric costs of missed anomalies versus false positives. Empirical evaluations across E-Commerce fraud and UCI Credit datasets show that semantic Pareto-DQN successfully shatters the zero-recall trap. It achieves superior minority-class recall compared to scalarized baselines, providing an alternative to trade bounded operational friction for financial anomaly discovery.

---


### 142. [ConceptSMILE: Auditing the Trustworthiness of Concept-Based Explainable AI](https://arxiv.org/abs/2607.09649)

**<font color=#1a73e8>作者：</font>** Mohadeseh Mollapour, Koorosh Aslansefat, Zeinab Dehghani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Concept-based explainable artificial intelligence (AI) can make model reasoning more human-understandable, but concept-level outputs are not automatically trustworthy. We introduce ConceptSMILE, a model-agnostic perturbation-based auditing framework for evaluating the reliability of concept-based explanations. Rather than replacing SMILE, ConceptSMILE extends its perturbation-based logic from feature- or region-level attribution to the auditing of human-understandable concept explanations. The framework perturbs input regions, measures concept-response shifts, applies locality weighting, and fits an XGBoost surrogate to approximate local concept behaviour. Reliability is assessed through attribution accuracy, surrogate fidelity, faithfulness, stability, and consistency. We evaluate ConceptSMILE on retinal fundus images by comparing MedSAM-derived visual concepts with VLM-based semantic concepts. Results show that reliability varies across concepts and pathways: MedSAM achieves stronger spatial attribution and the highest surrogate fidelity ($R^2 = 0.8503$, $R_w^2 = 0.8465$), while the VLM pathway shows stronger vessel faithfulness and stronger stability under selected artefact conditions. ConceptSMILE provides an independent audit layer for evaluating the trustworthiness of concept-based XAI.

---


### 143. [Revisiting Euler-Angle Regression with Kolmogorov-Arnold Networks](https://arxiv.org/abs/2607.09650)

**<font color=#1a73e8>作者：</font>** Yangting Sun, Zijun Cui, Yufei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In many real-world systems, including articulated robots and biomechanical models, rotations are defined in joint space and naturally parameterized by Euler angles with bounded ranges. Yet regressing Euler angles remains challenging, as their discontinuities and singularities often destabilize training. In this work, we revisit Euler-angle regression and show that its effectiveness depends critically on the interaction between rotation representation, regression architecture, and domain constraints. We introduce a new framework that combines range-aware Euler modeling with Kolmogorov-Arnold Networks (KAN), which replace fixed node-wise activations with learnable univariate functions on edges. We further provide theoretical analysis indicating that bounded Euler ranges motivate a near-additive structure in the regression function, which favors the additive functional form of KAN, and we confirm this trend empirically. Extensive experiments on controlled rotation regression, object pose estimation, and robotic and human inverse kinematics demonstrate consistent improvements in accuracy, convergence, and efficiency. The code will be publicly available.

---


### 144. [OpenLongTail: Generative Scaling of Long-Tail Driving Data](https://arxiv.org/abs/2607.09655)

**<font color=#1a73e8>作者：</font>** Lulin Liu, Nuo Chen, Yan Wang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling robust driving policies is fundamentally bottlenecked by the scarcity of edge cases in curated datasets. While the real world continuously captures these critical events, such long-tail events remain underutilized when collected from heterogeneous sources. Specifically, diverse but valuable in-the-wild long-tail videos lack the full view coverage required for training policy models, often missing multi-view poses or originating solely from monocular dash cameras. This modality gap prevents these ubiquitous observations from being converted into scalable training data for long-tail generalization. We introduce OpenLongTail, an open-source generative data engine for scaling autonomous driving policies under long-tail events. To transform heterogeneous data sources into view-aligned and temporally coherent multi-view assets that are useful for policy learning, we develop a pose-informed extrapolative view synthesis pipeline that generates the missing views. We further enhance cross-view consistency and the temporal alignment for the newly generated views by injecting Plücker ray geometry into the scalable generation engine. By synthesizing heterogeneous long-tail data, we observe a significant improvement in closed-loop driving robustness in handling long-tail events. By measuring the extrapolative view synthesis and pose metrics, we validate the effectiveness of OpenLongTail in visual fidelity, cross-view consistency, and ego-trajectory recovery.

---


### 145. [Scalable Visual Pretraining for Language Intelligence](https://arxiv.org/abs/2607.09657)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Zhonghan Zhao, Wenwei Zhang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid progress of large foundation models has been driven predominantly by pretraining on large-scale text corpora. However, many forms of knowledge are conveyed through visual representations, where figures, typeset equations, and page layouts carry rich information that cannot be faithfully or completely captured by text alone. Yet current pretraining approaches discard these visual cues by converting visually rich sources, such as documents and web pages, into plain text for learning language intelligence. This paper challenges the default assumption that language models must be trained on text-only representations and shows that Visual Pretraining is a scalable learner for foundation model intelligence. To this end, we conduct a systematic study of unsupervised visual pretraining paradigms that directly leverage visual documents without text extraction. Across multiple backbones and benchmarks, visual pretraining on the same underlying corpora consistently outperforms text-only pretraining, offering an efficient pathway to scalable language intelligence.

---


### 146. [Impact of Benign Connectivity Variations on Intrusion Detection for Encrypted OPC UA Traffic in Industrial Private 5G Networks](https://arxiv.org/abs/2607.09659)

**<font color=#1a73e8>作者：</font>** Song Son Ha, Florian Foerster, Henry Beuster 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML)-based intrusion detection systems (IDSs) are increasingly used to monitor encrypted industrial communication. However, their behavior under realistic private 5G operating conditions remains insufficiently understood. This paper investigates the impact of benign connectivity variations on ML-based IDSs for encrypted Open Platform Communications Unified Architecture (OPC UA) traffic in industrial private 5G networks. Experimental results show that legitimate connectivity events can noticeably increase false positive activity despite the absence of attacks. Furthermore, elevated IDS anomaly scores frequently coincide with periods of control-plane (CP) activity associated with these events. The findings highlight the importance of considering CP context when interpreting IDS outputs in industrial private 5G environments.

---


### 147. [PanoWorld: Real-World Panoramic Generation](https://arxiv.org/abs/2607.09661)

**<font color=#1a73e8>作者：</font>** Haoyuan Li, Dizhe Zhang, Yuemei Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we aim to address the challenge of long-range memory in panoramic world models by exploiting the rotation-equivariant property of omnidirectional representations, where rotation can be treated as an implicit geometric this http URL on this insight, we propose PanoWorld, which simplifies camera trajectories into translations via fixed headings for both current-action modeling and long-range memory through Dense Panoramic Ray-Conditioning (DPRC) and Geometry-aware Memory Augmentation (GMA).Then, a three-stage training pipeline is introduced to progressively optimize each component. To better evaluate physical consistency under large-scale spatial variations and diverse illumination conditions, where existing datasets are relatively stable, we construct World360, a large-scale dataset consisting of both real-world video clips collected via panoramic unmanned aerial vehicles and high-quality simulated clips generated by this http URL experiments on World360 demonstrate the effectiveness of PanoWorld, outperforming alternative methods by a large this http URL models, training code, and dataset will be publicly available. More information can be found on our project page: this https URL.

---


> [!TIP]
> 当前位于：**101-147**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-147**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
