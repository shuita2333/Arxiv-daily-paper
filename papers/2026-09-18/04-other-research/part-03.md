# 📦 其他研究 | 2026年09月18日

> 本类共 **223** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-223](./part-05.md)

---

### 101. [CapMap-MS-TTA: 3rd Place Solution for the MUMU Track of the 8th LSVOS Challenge at ECCV 2026](https://arxiv.org/abs/2609.18206)

**<font color=#1a73e8>作者：</font>** Chengfeng Qiu, Kaifeng Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The MUMU track of the 8th Large-scale Video Object Segmentation (LSVOS) Challenge requires a single unified multimodal model to jointly solve image tagging (Task A), open-vocabulary object detection (Task B), and English captioning (Task C) under strict resource constraints (<=0.5B parameters and <=8 GB peak GPU memory). We present CapMap-MS-TTA, a training-free submission built on Microsoft Florence-2-base (~231M parameters), combining caption keyword mapping with multi-scale flip test-time augmentation. Task C uses the native <DETAILED_CAPTION> pathway with length/token sanitization. Task A maps the same detailed caption into the official quality/scene/event vocabularies via an expanded keyword lexicon with whole-word matching and a lightweight expand-hints stage. Task B runs Florence-2 open detection (<OD>) with multi-scale and horizontal-flip test-time augmentation (TTA), followed by label-aware non-maximum suppression (NMS). Without fine-tuning, the system improves our reproduced Florence-2 baseline from 15.16 to a best public score of 16.4815, and ranks 3rd on the final MUMU leaderboard.

---


### 102. [A Lightweight CNN Integrated Compact Convolutional Transformer for Multi-Scale Feature Learning and reducing computational complexity for breast cancer mammography image detection and classification](https://arxiv.org/abs/2609.18212)

**<font color=#1a73e8>作者：</font>** Md Taimur Ahad, Ainuddin Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Over the years, Convolutional Neural Networks (CNNs) have demonstrated strong capability in cancer detection and classification using medical images. However, CNN-based models often struggle to capture long-range contextual dependencies. In such scenarios, integrating Compact Convolutional Transformer (CCT) architectures after the CCT layer allows CNN-extracted features to reshape into compact patch tokens using a CCT tokenizer, followed by the addition of positional embeddings to preserve spatial structure. Using 5-fold cross-validation, the model was tested on 3 sets of breast cancer mammography. With only 250,435 parameters, the model achieved 99%-100% accuracy across 3 datasets, indicating robust generalization. Explainable AI (XAI) was integrated into the model to explain the breast cancer classification process to enhance clinical trust. The results indicate that the proposed framework is suitable for computer-aided diagnosis systems, particularly in resource-constrained clinical environments. The novelty of the proposed CNN-integrated CCT overcomes the limitation of CNN's gradient degradation in the last layers by integrating convolutional tokenization with transformer-based learning. Lighter than ViT, which is effective in capturing long-range dependencies, the model has also proven efficient in breast cancer classification by capturing long-range dependencies among breast tissue regions.

---


### 103. [APGEM: Adaptive Policy-Guided Error Mitigation for Quantum Reinforcement Learning on a Real-World CVRP Case Study](https://arxiv.org/abs/2609.18219)

**<font color=#1a73e8>作者：</font>** Shabir Ahmad Sofi, Bisma Majid, Mir Mohammad Yousuf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum Reinforcement Learning (QRL) represents policies as variational quantum circuits (VQCs), making it attractive for combinatorial optimization such as the Capacitated Vehicle Routing Problem (CVRP). On noisy intermediate-scale quantum (NISQ) hardware, however, decoherence degrades fidelity and destabilizes learning, and conventional error mitigation is applied statically without regard to the learning context. We introduce Adaptive Policy-Guided Error Mitigation (APGEM), a controller that selects among Zero-Noise Extrapolation (ZNE), Probabilistic Error Cancellation (PEC), Clifford Data Regression (CDR), and Readout Error Mitigation (REM) online, driven by a fidelity, entropy, and cost aware utility function and an epsilon-greedy rule over temporal-difference Q-scores. We evaluate on a realistic urban-logistics testbed, a Delhi-based CVRP over real landmarks with geodesic inter-node costs, exercised across five noise families and four severity levels. On this instance, the QRL agent outperforms constructive heuristics and approaches metaheuristics, while mitigation restores approximation ratios from 0.84-0.87 to 0.92-0.94 under high noise. The controller shifts from a CDR-dominated regime under short training horizons to a balanced deployment across all four techniques under longer horizons, indicating genuine regime-dependent selection. These preliminary results position adaptive, learning-aware mitigation as a practical route to noise-resilient QRL.

---


### 104. [ABM-SIRTEM: A Hybrid Agent-Based and Epidemiological Model for Pandemic Response](https://arxiv.org/abs/2609.18223)

**<font color=#1a73e8>作者：</font>** Sheryl Paul, Samuel Williams, Preetom K. Biswas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The COVID-19 pandemic has had profound impacts on global health, social structures, and economies. It disproportionately affected lower socioeconomic groups and those reliant on interaction-based jobs. Regulatory bodies faced the challenge of designing policies that preserve public health while limiting disruption to economic stability and productivity. Epidemiological models such as SIR and agent-based models (ABMs) have been used to study disease dynamics and the socioeconomic impacts of disease and interventions. Population-level models often simplify individual heterogeneity, while detailed ABMs can become computationally expensive as the numbers of agents and interactions increase. We propose ABM-SIRTEM, a hybrid model that incorporates occupation categories, economic productivity, and welfare at the individual level while dynamically modeling compliance with government interventions. We calibrate the model against historical positive and negative test counts from four U.S. states and examine the resulting compliance dynamics. This framework provides a basis for studying the interaction between disease spread and socioeconomic behavior in pandemic-response planning.

---


### 105. [WISE: A Lightweight, Weakly-Supervised Model for Onboard Fire Smoke Detection and Localization](https://arxiv.org/abs/2609.18227)

**<font color=#1a73e8>作者：</font>** Sha Lu, Yu Sun, Liang Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wildfire smoke detection from satellite imagery is critical for early warning and rapid response. For onboard satellite deployment, detection systems must operate under strict memory and latency constraints while providing spatially informative outputs for downstream decision-making. Existing tile-level classification methods are computationally efficient but lack spatial localization, whereas pixel-level segmentation approaches provide detailed masks yet are typically too computationally demanding for real-time onboard execution. To address this gap, we propose WISE (Weakly-supervised Inference-efficient Smoke Extraction), a deployment-oriented framework for onboard fire smoke detection and localization. WISE leverages only tile-level annotations through a teacher-student distillation strategy, where an offline teacher provides soft spatial supervision to a lightweight WISE-Student optimized for efficient onboard inference. The student jointly predicts tile-level smoke presence and smoke probability maps within a single forward pass, enabling spatially informative detection under strict computational constraints. WISE was evaluated through in-orbit execution aboard the ISS-mounted IMAGIN-e payload. Three model variants achieve average inference times of 0.10 s, 0.14 s, and 0.26 s per tile, indicating near-real-time per-tile inference within onboard resource limits. Ground-based experiments on Landsat 5 and Landsat 8 imagery further indicate effective detection and spatially informative localization. The best-performing variant achieves a mean tile-level F1 score of 0.964 and a mean pixel-level F1 score of 0.750 across 10 runs, while containing only 0.12M parameters and requiring approximately 3 GFLOPs. Together, these results indicate that WISE is a practical candidate for low-latency wildfire smoke monitoring from space under onboard resource constraints.

---


### 106. [Anomaly Detection in General Ledger Data: Results from a Hybrid Approach](https://arxiv.org/abs/2609.18228)

**<font color=#1a73e8>作者：</font>** Jan Gronewald, Alexander Michael Rombach, Sebastian Stephan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Journal Entry Tests (JETs) are a mandatory part of annual audits to evaluate and assess both highrisk audit areas and potential material misstatements. However, as JETs are designed to detect known patterns based on domain knowledge, the resulting lists are often very large and require substantial additional effort from the auditor. To ensure the economic efficiency of the audit, the number of false positives in JET result lists must be reduced. Especially machine learning (ML) methods represent a promising approach to improve anomaly detection in this field. In this research in progress paper, we investigate different approaches on how to combine JETs with ML-methods in a hybrid manner. We present specialized models to increase the detection performance and validity of anomaly detection results to improve audit efficiency. The experiments are based on synthetic data consisting of different normal and anomalous journal entries.

---


### 107. [SmartFlex: An Adaptive Lumbar Support System Based on Posture Recognition and Air Bag Array](https://arxiv.org/abs/2609.18234)

**<font color=#1a73e8>作者：</font>** Ben Xiaolu Huang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Low back pain (LBP) is a leading cause of disability worldwide and affects populations ranging from working adults to students with prolonged sitting habits. Conventional lumbar support belts are generally static and non-adaptive, which limits their ability to accommodate dynamic postural changes and individualized comfort requirements. This paper presents SmartFlex, an intelligent wearable lumbar support system that integrates real-time posture recognition with an adaptive air bag array. The system uses a JY901S gyroscope sensor to detect user posture and a lightweight TinyML neural network deployed on an Arduino R4 UNO to process posture data at the edge. Based on the recognized posture state, a closed-loop pneumatic control system dynamically inflates or deflates 14 distributed air bags through four independent micro air pumps to provide targeted biomechanical support. Evaluation results show that SmartFlex achieves over 94% posture recognition accuracy and generates corresponding pressure-control commands with a sensing-to-command delay of less than 120 ms. The pneumatic system operates within a calibrated pressure range of 15-85 kPa. A user study with 20 participants produced a 4.5/5 rating for support effectiveness, suggesting that adaptive wearable support may improve daily sitting comfort and reduce lumbar fatigue.

---


### 108. [F-DACE: Fuzzy Disagreement-Aware Causal Evidence Fusion for Abstention-Safe Conversational Retail Decision Support](https://arxiv.org/abs/2609.18238)

**<font color=#1a73e8>作者：</font>** Sourish Dey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Observational decision-support systems often expose one causal estimate as a recommendation even when plausible estimators disagree. The inherent engine of the proposed system is causal machine learning: a conditional-average-treatment-effect estimand identified by backdoor adjustment, estimated by an EconML DML causal forest and DoWhy linear regression, checked by two-way fixed effects, and converted into candidate levers by constrained optimisation. F-DACE is the decision layer on that engine. It represents precision, propensity overlap, placebo-refutation stability, interval overlap, and directional agreement as fuzzy memberships. Hard vetoes force abstention after estimand mismatch, failed diagnostics, informative sign conflict, or weak evidence. In 180 panel simulations spanning six identification conditions, F-DACE made a decision in 67.2% of runs and limited false recommendations to 17.2%; the corresponding rates were 33.3% for the causal forest and 35.6% for backdoor regression, matching deterministic unanimity rather than dominating it. Nearly all (30 of 31) false recommendations occurred under shared unmeasured confounding, which no fusion rule can diagnose when every component shares the omitted variable. The retail application aggregates a public Walmart panel to 6,435 store-weeks across 45 stores. F-DACE abstains for all five markdown indicators: some estimates are imprecise, one refutation fails, and MarkDown5 has a direct sign conflict. A LangGraph conversational agent exposes impact, what-if, and lever-optimization tools while a deterministic verifier preserves causal-layer status. On 24 live questions it achieved 100.0% tool-routing accuracy, 100.0% status fidelity, and 0.983 mean groundedness. On ten adversarial questions it resisted all injected instructions.

---


### 109. [Unified Response Geometry for Structured Pruning](https://arxiv.org/abs/2609.18239)

**<font color=#1a73e8>作者：</font>** Kaixiang Shu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structured pruning is commonly formulated as ranking individual channels, although channel responses can be complementary or cancel through downstream mixing. Motivated by these response interactions, we formulate pruning as the selection of a subset with large joint response capacity, followed by a separate functional realization step. Our unified response geometry maps each candidate set to \(M(D,R)=D^{1/2}RD^{1/2}\) and uses its determinant together with Schur-greedy residuals to select non-redundant coordinates. The same construction yields two information-conditioned instances: an unlabeled instance based on activation covariance, and a task-conditioned instance that combines activation and gradient variance for response scale with gradient correlation for complementarity. To convert the selected subset into an executable network, we fold predictable removed responses into successor weights through ridge compensation and recalibrate batch-normalization statistics, without fine-tuning the network. On ImageNet ResNet-50, the unlabeled instance reaches \(65.4\%\) and \(53.9\%\) Top-1 accuracy at 30\% and 40\% deletion, versus \(59.8\%\) and \(43.1\%\) for strength-only selection; the task-conditioned instance reaches \(67.7\%\) and \(56.3\%\) under the same protocol. A six-family screen shows architecture-dependent behavior, with positive relative contrasts in several convolutional and expansion-layer settings and clear boundary cases in windowed attention. These results support response geometry as a conditional principle for structured pruning, with its benefit determined jointly by the observed response and the architecture in which that response is realized.

---


### 110. [Re2A: Situated Conversational Recommendation via Rubric-based Preference Reasoning and Alignment](https://arxiv.org/abs/2609.18249)

**<font color=#1a73e8>作者：</font>** Dongding Lin, Jian Wang, Xiaoyan Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world recommendation scenarios are commonly grounded in shared physical environments during user-recommender interactions. This motivates situated conversational recommendation (SCR), a complex task requiring recommender assistants to jointly reason over dialogue history, co-observed scenes, and in-scene item attributes. However, current approaches struggle with this setting due to two intertwined challenges: accurately understanding situated user preferences throughout the conversation and generating responses that simultaneously satisfy user needs and grounded situations. To this end, we propose Re2A, a framework that formulates SCR as a structured reason-then-align process. We introduce rubric-based preference reasoning, which uses automated rubrics to guide the model toward producing explicit preference states. Based on these states, we propose a preference-conditioned optimization to align response generation with dual objectives: user preference satisfaction and situation consistency. Extensive experiments on two SCR datasets demonstrate that Re2A consistently outperforms state-of-the-art methods, delivering more precise, context-aware conversational recommendations. Our code is available at this https URL.

---


### 111. [Evolving Error States: Failure-Aware Progressive Repair for Ultrasound Lesion Segmentation](https://arxiv.org/abs/2609.18256)

**<font color=#1a73e8>作者：</font>** Ziliang Wang, XuJiang Tang, Lu Yuting 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliability under sparse and heterogeneous failures remains a fundamental challenge for medical image segmentation. High average accuracy can conceal a small set of structurally distinct and clinically consequential errors. Existing post-hoc correction methods alleviate this problem, but typically estimate false-positive and false-negative corrections from the same fixed prediction. This ignores the dynamic evolution of error states and limits the correction of complex cases. Inspired by iterative error feedback in structured prediction, we propose Failure-Aware Progressive Repair (FAPR). FAPR represents the current segmentation mask as a dynamic failure state and models each repair operation as a state-transition operator. Each accepted correction forms a new prediction state for subsequent error diagnosis and repair, enabling later operations to adapt to preceding changes. Conditional routing selectively activates necessary state transitions, while failure replay exposes the model to rare error states. By keeping the base segmentor frozen, FAPR preserves its established segmentation capability while improving difficult cases. Across three public ultrasound lesion segmentation benchmarks, FAPR improves mean DSC by 1.52%. On the very-hard subsets of BUSI and TN3K, the average gain reaches 13.77%.

---


### 112. [MS-RFD: Multi-Signal Release Frame Detection in Hammer Throw from Reconstructed 3D Trajectories](https://arxiv.org/abs/2609.18260)

**<font color=#1a73e8>作者：</font>** Ahmed Endris Hasen, Nikolaos Passalis, Tomi Vanttinen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in artificial intelligence and computer vision are reshaping sports performance analysis by enabling automated detection, tracking, and performance analysis. In hammer throw, performance is strongly determined by the kinematic conditions at release, particularly release speed, release angle, and release height. However, identifying the release instant from video typically requires manual frame-by-frame inspection, which is subjective and cumbersome in real-world training scenarios. In this paper, we present a fully automatic multi-signal release frame detection (MS-RFD) method for hammer throw using reconstructed 3D hammer trajectories. The proposed method integrates four complementary kinematic signals: speed dynamics, angular velocity transition, radial distance relative to the rotation center, and post-release trajectory linearity. These signals are fused to score and verify candidate release frames. MS-RFD is evaluated through the throwing-distance estimation error obtained from the release parameters estimated at the detected frame. An ablation study analyzes the contribution of each signal and compares alternative candidate selection strategies. The results show that speed dynamics and radial expansion provide the strongest signals for release frame detection, while angular velocity and post-release linearity provide smaller refinements.

---


### 113. [Who Audits Whom, on What Substrate, with What Evidence? An Independence-Graded Audit Protocol for Agentic AI](https://arxiv.org/abs/2609.18272)

**<font color=#1a73e8>作者：</font>** Mohamed Chahine Ghanem  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems plan, invoke tools and act with limited supervision; they are now both the subject of audits and, increasingly, the auditor. Independence, the foundation of assurance,is still applied to them as a binary. We argue that it must be graded along three orthogonal axes: principal independence (who controls the auditor), substrate independence (an auditor sharing the auditee's foundation-model family, toolchain or guardrails fails with it) and evidence independence (whether evidence is attestable rather than self-reported). Each axis has precedent; the contribution is to grade all three on a single audit, aggregate them by the weakest link, and apply the same rubric when the auditor is itself an agent. We give the model a formal basis by transplanting the beta-factor model of common-cause failure from reliability engineering, a seven-step protocol whose outputs a third party can verify, a structural detectability analysis of a procurement-controls agent audited at three grades, and a Monte Carlo study of the model in which a conventional internal audit of an agent-a real audit team, a second agent, provider logsp-surfaces 5.9% of the faults it could in principle see and none at all in half the fault classes. We map the triple to the EU AI Act as amended, ISO/IEC 42006, UK public-sector risk-management guidance and audit-regulator practice.

---


### 114. [Witness Encryption via Prime-Order Generic Groups](https://arxiv.org/abs/2609.18275)

**<font color=#1a73e8>作者：</font>** Isaac M Hair, Amit Sahai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We unconditionally construct witness encryption for NP in the classical generic-group model, using an ordinary cyclic group of prime order. For SAT instances of size $n$, the encryption algorithm runs in time poly$(n)$, and any satisfying assignment can be used to decrypt in poly$(n)$ time with correctness error $2^{-n^{\Omega(1)}}$. If no satisfying assignment exists, then every generic adversary making at most $n^{\Theta(\log n)}$ group queries has distinguishing advantage at most $n^{-\Theta(\log n)}$.
Along the way, we prove the first superconstant-factor NP-hardness of approximation result for homogeneous MinRank under randomized polynomial-time reductions, achieving a logarithmic gap even when the rank-one witness has a Boolean right factor.

---


### 115. [Building Trust in Artificial Intelligence: A Necessity for Railway Applications](https://arxiv.org/abs/2609.18278)

**<font color=#1a73e8>作者：</font>** Lefebvre Renard Clément, Lébé Vincent, Da Silva Ribeiro Pereira Ricardo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) is currently only applied to non-safety critical applications due to the strict standards and regulations for railway industries. We propose to review the three main fields necessary to increase trust in data science and AI algorithms and reach compliance: robustness, Operational Design Domain (ODD), and explainability. Robustness is the ability of an AI system to maintain its level of performance under any circumstances (ISO24029). ODDs allow the explicit definition of operating conditions under which a system is intended to operate, according to the recently published DIN DKE SPEC 99004. Explainability is the property of an AI system to express important factors influencing the AI system results in a way that humans can understand. Those 3 domains of research are already well investigated by nonrailway actors, with algorithms and methods ready to use for railway applications. A system view is necessary to ensure all trustworthy requirements interact continuously in a safe MLOps environment thereby fostering acceptance from regulators, operators and the public. Beyond safeguarding safety-critical applications, we aim to show that fostering deep trust in AI, as now required by regulatory frameworks worldwide, will unlock its full potential and transform the pace of adoption across mission-critical domains.

---


### 116. [Decoder-Agnostic Token Merging for Vision Transformers: A Systematic Study of G2TM](https://arxiv.org/abs/2609.18279)

**<font color=#1a73e8>作者：</font>** Victor Bercy, Martyna Poreba, Michal Szczepanski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have achieved state-of-the-art performance across a range of computer vision tasks, mainly thanks to the self-attention mechanism. However, its complexity, increasing quadratically with the number of tokens, remains the major obstacle to ViT efficiency and deployment at scale. Token merging reduces this cost by aggregating redundant tokens. Yet existing methods are typically evaluated within a single architecture, leaving open whether their effectiveness stems from the merging mechanism itself or from the specific decoder they are paired with. We extend Graph-Guided Token Merging (G2TM), a single module inserted early in a ViT-based network, beyond its original Segmenter setting. We evaluate G2TM across three semantic segmentation frameworks (Segmenter, SETR, EoMT) and three decoder families (Linear, Transformer-, convolution-based), as well as standard ViT image classification. Our results show that G2TM's behavior and accuracy-efficiency trade-off are consistent across every tested architecture for a given backbone size, indicating that its effectiveness is a property of the encoder rather than the decoder. G2TM also generalizes well to image classification, achieving an even smaller degradation in accuracy compared to semantic segmentation. We further find that G2TM's optimal hyperparameters, resulting in a consistent drop in GFLOPs of 22-47% and an increase in throughput by up to 74% for segmentation models on ADE20K dataset, depend primarily on the backbone's pre-training recipe and on the target dataset, rather than on the decoder choice.

---


### 117. [A GAN-Based Framework for Robust DDoS Attack Detection](https://arxiv.org/abs/2609.18281)

**<font color=#1a73e8>作者：</font>** Makram Chehayeb, Walid Fahs, Amina Rizk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The availability and consistency of online services remain vulnerable due to Distributed Denial of Service (DDoS) attacks. These attacks are evolving by adopting more complex strategies to evade traditional network security systems. Despite the effectiveness of machine learning models in detecting DDoS traffic, targeted adversarial attacks can degrade their classification accuracy. This work proposes a robust detection framework that integrates generative adversarial modelling with advanced machine learning models. We trained Random Forests, Deep Neural Ensembles, and Transformer-based models using the CICDDoS2019 dataset to establish the frameworks baseline performance. To enhance the models defensive capacity, we generated synthetic adversarial flows that simulate potential evasion attempts and adversarial traffic using a Wasserstein Generative Adversarial Network with Gradient Penalty (WGAN-GP). Then, we combined the generated traffic with benign and malicious traffic to construct hybrid datasets to train the models to learn more generalizable decision boundaries. The experimental results indicate that the proposed methodology significantly enhances detection accuracy and resilience, especially against unseen adversarial traffic. We also tested the designed framework using real-world generated traffic, which demonstrates its capability in practical settings. The scalable and efficient solution against adversarial DDoS attacks, introduced in this work, paves the way towards more resilient and adaptive network defense systems that combine generative adversarial augmentation with recent advances in learning models.

---


### 118. [Visual Autoregressive Priors for RAW-to-sRGB Image Signal Processing](https://arxiv.org/abs/2609.18302)

**<font color=#1a73e8>作者：</font>** Tailai Chen, Xiaotong Luo, Yuan Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RAW-to-sRGB image signal processing (ISP) must recover perceptually faithful colors and fine details from sensor measurements, often under imperfect spatial alignment and missing camera metadata. This paper presents, to the best of our knowledge, the first application of visual autoregressive (VAR) next-scale prediction over a discrete image codebook to the RAW-to-sRGB ISP task. We adapt a frozen 1.10\,B-parameter VAR backbone for RAW-conditioned ISP with only 32.93\,M trainable parameters (2.99\%), and propose a frequency-decomposed color loss that separately supervises low-frequency tone via wavelet LL cosine similarity and chromatic edges via detail-band $\ell_1$. On the Zurich RAW-to-sRGB benchmark, the method improves PSNR-Y from 21.31 to 21.89\,dB and reduces LPIPS from 0.276 to 0.218 on the full 1,204-image test set. Diagnostic experiments show that the VAR prior preserves structure well, but continuous color transfer remains the dominant bottleneck: oracle affine correction recovers 3.8\,dB, while learned color heads yield marginal gains.

---


### 119. [Beyond Quadratic Loss: The Stability Phase Diagram of Adam](https://arxiv.org/abs/2609.18314)

**<font color=#1a73e8>作者：</font>** Gaoxiang Tang, Huanran Chen, Ziming Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Loss spikes are recurrent instabilities in neural-network training and can arise from multiple mechanisms. For Adam in particular, macroscopic loss spikes have been linked to optimizer dynamics, yet how its two momentum timescales govern them remains unclear. We investigate this dependence by mapping training dynamics across the $(\beta_1,\beta_2)$ plane. Across a range of model--task settings, an approximately linear boundary, $1-\beta_2=C(1-\beta_1)$, separates spiky from non-spiky dynamics, whereas a one-dimensional quadratic loss produces approximately cubic slope. A one-dimensional superquadratic loss $L(x)\propto|x|^n$ recovers the near-linear scaling and links the boundary coefficient to the effective loss exponent $n$. We further show that confident cross-entropy losses develop a core--wall landscape comprising a narrow quadratic core followed by a steep wall, which produces effective superquadratic behavior at the scale of an optimizer update. Together, these results connect Adam loss spikes to both the mismatch between momentum timescales and finite-scale superquadratic loss geometry beyond the Hessian.

---


### 120. [Can MiniMax-H3 Reason About the Physical World? An Evaluation of Omni-Modal Generative Model](https://arxiv.org/abs/2609.18323)

**<font color=#1a73e8>作者：</font>** Haoyu Zhao, Zihao Zhao, Tianyu Deng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Omni-Modal Generative Models (Omni-Models) have advanced content generation toward unified modeling of text, images, video, and audio. MiniMax-H3 exemplifies this transition by combining multimodal context understanding with joint audio-visual generation in a shared latent framework. Its unified architecture raises a fundamental question: Can multimodal alignment improve the model's world reasoning, and what new evaluation paradigms do omni-modal inputs enable? To investigate this question, this work introduces a comprehensive evaluation framework organized around four complementary dimensions of physical world reasoning. Unlike existing evaluation frameworks for video generation and world models, which are often constrained by limited input modalities and evaluation settings where prompts closely match the target video content, our evaluation is specifically designed to exploit the multimodal inputs of Omni-Model. We construct a diverse set of novel tasks that require models to integrate complementary information across modalities. Specifically, we consider four scenarios, including implicit prompts paired with multiple frames, audio-image, prefix-videos, and audio-video inputs. Every single modality provides only partial evidence about the underlying event, requiring the model to jointly reason over the complementary semantic cues to infer latent event states and future dynamics. Across 517 evaluation instances, MiniMax-H3 achieves an overall success rate of 41.97%. Video-based Decision Reasoning yields the highest success rate at 56.00%, while Audio-based Disambiguation Reasoning is the weakest, reaching only 27.40%. These results indicate that effective multimodal integration remains key to fully exploiting the benefits of diverse input modalities. The project is available at this https URL.

---


### 121. [PDA++: Field-Aligned Planning and Scene-Adaptive Insertion in Remote Sensing](https://arxiv.org/abs/2609.18329)

**<font color=#1a73e8>作者：</font>** Xianchi Dong, Yingyan Hou, Chao Ren 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing recognition is often constrained by scarce observations of rare targets and costly annotations, making realistic synthetic augmentation particularly valuable for few-shot and long-tailed scenarios. Object insertion provides an efficient way to increase target diversity while preserving authentic background scenes, but realistic insertion in overhead imagery requires the generated target to adapt coherently to its surrounding environment. To this end, we propose PDA++, a unified environment-aware object insertion framework organized as Plan, Decouple, and Assimilate. Planning determines scene-compatible poses through an affordance field that combines geometric clearance with structure- and scale-aware cues. Decoupling introduces a pose-conditioned background that provides precise spatial guidance together with target-scene context, allowing the reference object to preserve its identity while adapting to the target observation. This construction also naturally provides pixel-level masks for segmentation augmentation. Assimilation further improves local coherence by aligning multi-scale texture distributions through optimal transport. On the optical benchmark, PDA++ achieves a whole-image FID of 6.28 and improves average few-shot recognition mAP50 by 17.69 points, corresponding to a 28.8% relative gain over the real-data baseline. On SAR imagery, it improves ship detection by 4.10 mAP50 points and remains effective under cross-dataset transfer and amorphous-target insertion. Code is available at this https URL.

---


### 122. [Pose2Muscle: Structured Spatio-Temporal Decoding for Discrete Muscle Activity Estimation from Human Pose](https://arxiv.org/abs/2609.18336)

**<font color=#1a73e8>作者：</font>** Yuepeng Chen, Jiehong Shi, Kaili Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Muscle activity is fundamental to human movement, and understanding its patterns is critical for injury prevention and rehabilitation. Conventional muscle activity monitoring relies on specialized sensors such as surface electromyography, which limits its practicality for long-term real-world use. Existing studies suggest that muscle-related information can be inferred from human pose. However, the substantial gap between externally observable pose and internal muscle activation, limits the accuracy and generalization of current approaches. In this study, we propose Pose2Muscle, a pose-driven framework for discrete muscle activity estimation without requiring sEMG signals at inference time. Instead of directly regressing continuous sEMG signals, Pose2Muscle reformulates muscle estimation as a structured prediction problem over discrete muscle activity states, yielding a more stable and interpretable target space. The framework combines multi-scale spatio-temporal attention to capture motion patterns at complementary spatial and temporal scales with a directed acyclic graph-based decoder that maintains multiple candidate muscle-state hypotheses and performs structured trajectory inference over time. To support this task, we construct PoseEMG-43, a synchronized pose-sEMG dataset containing 2,992 movement instances from 43 daily-life actions performed by 14 participants. Experiments show that Pose2Muscle consistently outperforms representative retrieval- and pose-based baselines. It achieves an Adjacent-level Accuracy of 86.36% and a Pearson correlation coefficient of 0.8821 under the Random Split, and 63.97% and 0.6795, respectively, under the Subject-Level Split. These results demonstrate the feasibility of inferring structured muscle-state patterns from human pose and suggest the potential of Pose2Muscle for muscle-aware movement analysis when direct physiological sensing is impractical

---


### 123. [Detecting Logic Vulnerabilities Across the Contract and Device Layers of Blockchain-Enabled IoT With Multi-Agent Heterogeneous Graph Attention](https://arxiv.org/abs/2609.18344)

**<font color=#1a73e8>作者：</font>** Minfeng Qi, Jialin Li, Tianqing Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain-enabled Internet of Things (IoT) systems integrate smart contracts with embedded devices to support decentralized device management and access control. Their security therefore depends jointly on the logic of on-chain contracts and off-chain device firmware. Logic flaws in either layer can violate the same system invariants, such as unauthorized access, improper state changes, or unguarded privileged operations. Existing approaches rely on contract analysis, firmware analysis, and graph-based vulnerability detection. However, these methods typically focus on a single layer or artifact and often depend on predefined vulnerability patterns, emulation fidelity, or homogeneous representations that obscure security-relevant component roles. They also lack a unified architecture that supports different security tasks while remaining deployable on resource-constrained gateways. To address these limitations, we extend MA-HGAT into a cross-layer multi-agent heterogeneous graph attention framework that models contracts, firmware artifacts, device fleets, and transaction streams with a unified four-role, nine-relation schema. Role-aligned agents exchange heterogeneous evidence through cross-attention, while graph-, link-, and node-level heads support multiple detection tasks and a role-based gateway--cloud partition enables lightweight edge inference. MA-HGAT thus provides a unified and deployable framework for detecting logic vulnerabilities across the contract and device layers of blockchain-enabled IoT systems.

---


### 124. [Online Multi-Camera 3D Tracking via ID Prediction over Recurrent Sparse Queries](https://arxiv.org/abs/2609.18363)

**<font color=#1a73e8>作者：</font>** Pragyan Shrestha, Haruto Nakayama, Atom Scott  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online multi camera 3D tracking must maintain scene global identities across synchronized views, yet query-based trackers carry these identities only implicitly in the instance bank, where they fragment upon query interruption. We present an online architecture that recovers association accuracy by predicting IDs explicitly over recurrent sparse queries. An outside-in Sparse4D detector fuses calibrated views into world frame 3D detections while propagating a sparse query bank, and a causal MOTIP ID decoder associates detections against a finite trajectory memory. We adapt MOTIP's relative-ID prediction and recycled slot runtime to globally fused 3D observations, and introduce metric spatial gating and proximity based newborn recovery. On the official 2026 AI City Challenge Track 1 test set, our method raises HOTA from 29.63 with native instance bank identities to 38.01, primarily through an AssA increase from 20.83 to 31.10, and ranks third on the public leaderboard. Full-sequence validation over all 9,000 frames of each scene shows that decoupled ID training improves HOTA over native identities, whereas continuing detector training alongside the detached ID objective produces scene-dependent gains and losses.

---


### 125. [Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts](https://arxiv.org/abs/2609.18366)

**<font color=#1a73e8>作者：</font>** Guojun Zhu, Xunheng Huang, Peng Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable agent evaluation is complicated by automatic harness optimization, which repeatedly uses a released benchmark $B_{\mathrm{rel}}$ to guide a Proposer that edits prompts, memory, retrieval, tools, and control code around a fixed target agent. Task holdout varies semantic tasks but leaves the benchmark protocol fixed, so a "bad genius" Proposer can produce a cheating harness whose released-benchmark gain depends on a benchmark-wide shortcut. We introduce Counterfactual Harness Search and Evolution (CHASE), which casts harness evolution as constraint generation over validity-preserving benchmark counterfactuals. After each Proposer update, a Challenger searches for an executable protocol transformation with large gain destruction. A validity firewall checks that task semantics are preserved, while a confirmation set determines whether the counterfactual enters a finite archive. We formalize an exact shortcut-neutralized benchmark $B_0$ and establish statistical guarantees linking finite counterfactual archives to $B_0$ and characterizing sequential Challenger search. We evaluate CHASE on a synthetic benchmark and on OfficeQA, where CHASE retains strong released-benchmark gains while substantially reducing gain destruction under valid protocol changes.

---


### 126. [JigSync: Gauge-Resolved Synchronization for Jigsaw Reassembly under Unknown Piece Orientation](https://arxiv.org/abs/2609.18379)

**<font color=#1a73e8>作者：</font>** Soham Pahari, Antik Aich Roy, Ujjwal Bhattacharya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Square jigsaw reassembly requires recovering the spatial arrangement of shuffled fragments from their visual content and pairwise relationships. While recent studies have made substantial progress, existing benchmarks typically assume that all fragments are provided upright, reducing reassembly to a permutation problem. We study the generalized problem in which each fragment may also have gone through an unknown rotation. For this setting we establish a gauge-unobservability theorem: the minimum of the weighted least-squares objective is exactly invariant under a uniform global rotation of arbitrary magnitude, so no residual-based criterion can recover the global orientation. The theorem further identifies how the issue of global orientation can be resolved: an orientation anchor estimated from the content of a single fragment, lying outside its scope, suffices. To address the above, we propose JigSync, which attains 63.8% and 31.8% absolute accuracy (AA) on GAP-3 and GAP-5, respectively, the highest reported on both, while additionally recovering a rotation per piece that neither benchmark requires. We release JigSync, a degradation protocol that sweeps shape, erosion, photometry, grid size, and rotation independently.

---


### 127. [Every Fixed Metric Has a Blind Spot: A Learned Atmospheric Critic for Scoring Forecast Realism](https://arxiv.org/abs/2609.18381)

**<font color=#1a73e8>作者：</font>** Younes Elberkennou, Dmitri Demler, Thierry Meier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their high accuracy on point-wise metrics, machine learning weather forecasting models can exhibit different failure modes such as blurring, periodic irregularities, and other unphysical spatial artifacts. This has motivated a variety of metrics to detect known failure cases. Existing metrics fix a representation or transformation in advance, and that choice limits the artifacts they can detect. We propose to train a discriminator for separating reference data from the model's output, and using its output logit to obtain a divergence-like realism score. The discriminator learns whatever separates the model's fields from real weather, adapting to whichever failure mode that model exhibits. We compare our learned atmospheric critic to existing metrics using various synthetic corruptions applied to ERA5 reanalysis data. Our method successfully identifies the corruptions and ranks their severity, while existing metrics fail on at least one corruption. Additionally, we evaluate forecasts from real weather models, and find that the realism score degrades with longer lead times and the metric generally assigns higher realism to numerical models than to machine learning models.

---


### 128. [Emotion Experience, Expression, and Perception: Emotion Analysis on Multimodal Social Media Posts](https://arxiv.org/abs/2609.18385)

**<font color=#1a73e8>作者：</font>** Christopher Bagdon, Carina Silberer, Roman Klinger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotions are an essential aspect of human communication, particularly on social media, where authors frequently combine text and images to convey their emotions. Yet prior work on emotion analysis of social media posts has overlooked two important aspects in regard to measuring how well readers can reconstruct the authors' intent: (1)~the image modality, with most work focusing solely on text, and (2)~the real-world events that trigger the expressed emotions, and their relationship to the post content. We therefore study the relation between (a) the author's experience of the event that caused them to write a social media post and (b) the content of the post, with a focus on readers' capability to reconstruct that emotion expression. To do that, we introduce the Multimodal Multi-Emotion-Model dataset Mult2EMo, created by collecting annotations from both authors and readers on the posts and their triggering events. We find that reconstruction is possible but challenging for both human readers and computational models. We show that understanding the triggering event is crucial for accurate reconstruction, and that reconstruction is particularly challenging when posts rely heavily on the image to express emotion.

---


### 129. [MSR: Multiple Subject Reference for Video Generation](https://arxiv.org/abs/2609.18393)

**<font color=#1a73e8>作者：</font>** Guannan Li, Jiaji Chen, Jingyuan Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conditioning a video generator on multiple images requires preserving appearance while associating each reference with its intended role. We present MSR (Multiple Subject Reference), a slot-aware conditioning scheme for LTX-based video generation. Each reference image is independently encoded as a static clip and represented by a separate latent-token group. A compact Fourier-feature multilayer perceptron adds a numeric slot embedding, while slot-dependent temporal offsets modify the group's rotary coordinates. The reference groups are prepended to noisy target tokens and serve as clean context during target-only flow-matching training. We implement this scheme through low-rank adaptation and release the resulting weights and inference workflows. Qualitative examples demonstrate compositions containing distinct characters and referenced environments in realistic and stylized scenes. Development observations suggest reduced reference confusion relative to an earlier continuous-reference baseline, while similar clothing, complex garments, and viewpoint changes remain challenging. We describe the conditioning mechanism, the retained training configuration, and the observed strengths and limitations of the released system. A supplementary audio-reference experiment adds voice conditioning while keeping the visual parameters frozen.

---


### 130. [Reliable Virtual Sensing: A Multi-Domain Benchmark for Robustness Under Sensor Failures](https://arxiv.org/abs/2609.18396)

**<font color=#1a73e8>作者：</font>** Jens U. Brandt, Noah C. Puetz, Alexander Windmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Virtual sensing, the estimation of hard-to-measure quantities from available sensor measurements, is a critical enabler for control and monitoring in cyber-physical systems. However, when sensors fail, learning-based predictors can produce physically implausible estimates that propagate to system-level failures. We argue that real-world deployment demands robustness and introduce MuViS-C, the first multi-domain benchmark of robustness against common sensor failures in learning-based virtual sensing. Building on an existing nominal-performance benchmark and established corruption taxonomies, it covers ten sensor failure modes, from subtle drifts to catastrophic signal dropouts, at multiple severities. These are paired with complementary robustness measures capturing average error under corruption, relative degradation, and worst-case fragility. Across nine datasets from six domains, we benchmark six architectures spanning gradient-boosted trees and the major inductive biases for sequence modeling: convolution, recurrence, attention, and MLP-mixing. On the attention-based architecture, we further probe three robustification strategies. We find that (i) every model degrades substantially under corruption, becoming worse than a naïve predictor on at least one corruption setting, (ii) gradient-boosted tree ensembles achieve strong robustness, and (iii) dedicated robustification closes the gap between the attention-based architecture and the most robust models, though each strategy hurts nominal performance. The benchmark's multi-domain design proves essential, as model rankings shift across datasets, and no single domain captures the full robustness picture. MuViS-C is open-source and extensible to new datasets, failure modes, measures, and models.

---


### 131. [A Non-Linear Neuron Based Detection of Isolated Pixels in Binary and Grayscale Images using Contrast Sensitive Receptive Fields](https://arxiv.org/abs/2609.18399)

**<font color=#1a73e8>作者：</font>** Nassir Mohammad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identifying isolated points is important in image processing applications such as medical imaging, astronomy and quality control management. Other domains, such as cybersecurity, also present challenges that can be framed as image processing problems. One example of particular interest is the identification of anomalous single nodes in spatially organised networks where groups of nodes in different regions share similar feature values. This task can involve both binary and more complex grayscale images. However, existing methods face limitations: template matching is infeasible for grayscale images, while 2nd order derivative based methods are highly sensitive to noise and require user-specified thresholds. To overcome these issues, a novel method is proposed for detecting meaningful single-pixel deviations in images. This approach modifies and extends a neuron model, originally designed for anomaly detection, to operate on spatially diameter limited receptive fields that incorporate excitatory and inhibitory regions. The result is a method that is free from user-specified thresholds and parameters, and can be applied to both binary and grayscale images, providing an effective, robust and efficient solution.

---


### 132. [Prosthesis-Aware 3D Human Pose Estimation: A Dataset and Benchmark for RSP Users](https://arxiv.org/abs/2609.18406)

**<font color=#1a73e8>作者：</font>** Yilin Wen, Kechuan Dong, Fumiya Suginaka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering 3D human body motion from video is important for applications such as rehabilitation assessment and sports performance evaluation. For prosthesis users, this requires capturing both natural body joints and the geometry of the prosthetic device, a challenge that existing methods are not designed to address. Model-based estimators rely on body models trained on non-amputee individuals and cannot represent prosthesis geometry, while model-free methods lack body kinematic priors and are unreliable under occlusion. This challenge is particularly prominent for users of running-specific prostheses (RSPs), where the RSP has a complex curved geometry and moves dynamically during exercise. To fill this gap, we collect RSP3D, the first 3D dataset of RSP users, covering essential daily-life and exercise actions from participants with varied amputation conditions, using a multi-camera marker-based motion capture setup. We formally define the task of prosthesis-aware 3D pose estimation, evaluate representative methods in a zero-shot setting, and confirm their individual limitations. We further propose a hybrid baseline combining model-based body joint estimation with model-free RSP shape recovery, establishing a starting point for future research.

---


### 133. [TERN: A Delta-rule Memory with a Seasonal Reference and Online Adaptation for Epidemic Forecasting](https://arxiv.org/abs/2609.18407)

**<font color=#1a73e8>作者：</font>** Shunya Nagashima, Yuta Funayama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weekly influenza surveillance counts guide vaccine distribution and public-health alerts, yet they are hard to forecast. Each region offers only a few seasons, waves shift in timing and height every year, and information that helps while a wave grows misleads after its peak, whereas last season's shape stays informative for a year. Existing epidemic graph models and general forecasters read a short fixed window and treat all past information alike, so they neither exploit earlier seasons nor discard stale associations when the epidemic phase changes. To address these limitations, we propose TERN, a forecaster built around a delta-rule fast-weight memory that decays channel-wise and erases along a learned address under gates driven by local epidemic-phase features, combined with an explicit seasonal reference and online adaptation. On three Cola-GNN influenza benchmarks, TERN outperformed epidemic graph models and general forecasters, matched or exceeded seasonal references, and a controlled comparison confirmed the contribution of the memory itself.

---


### 134. [HPOQuest: A Rare-Disease Diagnostic Agent Using Active Phenotype Acquisition](https://arxiv.org/abs/2609.18431)

**<font color=#1a73e8>作者：</font>** Kamilia Zaripova, Nassir Navab, Azade Farshad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> More than 300 million people worldwide are affected by one of over 7,000 known rare diseases, yet diagnosis remains difficult because patients initially present with incomplete and heterogeneous phenotypes. We present HPOQuest, a training-free framework for sequential phenotype acquisition in rare-disease diagnosis. Starting from a small set of observed patient phenotypes, HPOQuest maintains a probabilistic disease ranking and iteratively selects informative follow-up questions to support clinicians during patient assessment. Confirmed phenotypes update the disease ranking, while all responses update the candidate question set. Across four benchmark cohorts, HPOQuest substantially improves diagnosis from sparse initial phenotypes, with gains of up to 30% points at Recall@1 and 45% points at Recall@5. These results demonstrate that sequential phenotype acquisition can substantially improve rare-disease diagnosis from limited initial clinical evidence.

---


### 135. [Risk-Aware World Modeling with Flow-Guided Occupancy Evolution for Selective Trajectory Planning in Automated Driving](https://arxiv.org/abs/2609.18442)

**<font color=#1a73e8>作者：</font>** Rongxiang Zeng, Linsen Cai, Jiafu Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safe motion planning in automated driving requires anticipating evolving traffic risks and deciding when to revise the current planned trajectory. We introduce RiskWorld, a risk-aware world modeling framework for shared occupancy forecasting and selective trajectory replacement. Spatial risk fields and temporal actor context are fused with visual bird's-eye-view features. Flow-guided evolution transports occupancy and scene features, while signed residuals correct occupancy after transport. One forecast is generated per planning step and reused across candidates. Each candidate is compared with a current-state persistence reference, yielding a nonnegative collision-score correction. The trajectory selected by current-world evaluation serves as the planning anchor and is replaced only when additional predicted risk triggers intervention and an alternative satisfies component-wise constraints on predicted risk and trajectory error. Candidate geometries remain unchanged. We evaluate RiskWorld for open-loop planning on nuScenes using camera features, annotation-derived current and historical actor states, and dataset-provided map context. RiskWorld achieves the lowest collision rate at a long evaluation horizon of 3 s, and the second-best average L2 error among various state-of-the-art baselines, while running at 11.5 FPS on a single NVIDIA RTX 4090 with 90.81 M parameters. Within-setting ablations show that RiskWorld achieves lower collision rates than the current-state rescoring baseline, while forecast reuse enables additional candidates to be evaluated at low marginal computational cost.

---


### 136. [DR.WILSS: Diffusion-Based Replay for Weakly Supervised Continual Semantic Segmentation](https://arxiv.org/abs/2609.18444)

**<font color=#1a73e8>作者：</font>** Leon Arthur Marx, Francesco Barbato, Matteo Caligiuri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised class-incremental semantic segmentation (WILSS) aims to train a segmentation model over multiple steps, each introducing new concepts to be learned with only image-level supervision. We introduce DR$.$WILSS, an innovative approach to address catastrophic forgetting in continual learning using diffusion-based generative replay. Our framework leverages language clues to guide the diffusion process, employing self-inpainting and regularization techniques to efficiently produce replay data, aiding the learning process. By generating high-quality replay data, the information from previously learned classes can be preserved during continual updates, a critical challenge in incremental learning scenarios. To further align the statistics of replay data with those of training samples, we apply LoRAs to the generative model. Experimental results demonstrate state-of-the-art performance across multiple benchmarks and generative architectures, while avoiding storage of training data and the use of additional resource-demanding tools during training. The proposed technique enables an optimal tradeoff between training complexity and inference-time accuracy, making DR$.$WILSS a promising solution for real-world applications.

---


### 137. [SEEK: Secure and Efficient Encrypted Keyword Search For Privacy-Preserving Messaging Protocols](https://arxiv.org/abs/2609.18459)

**<font color=#1a73e8>作者：</font>** Soumyadyuti Ghosh, Michail Maniatakos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Encrypted communication protects sensitive user data but can facilitate harmful or unlawful exchanges, creating a trade-off between detecting dangerous messages and preserving end-user privacy. To address this, we propose SEEK, a practical and efficient encrypted keyword-search protocol for privacy-preserving messaging that combines homomorphic encryption with secure two-party computation (2PC). SEEK first partitions messages into ciphertext fragments with the minimum sufficient overlap, then homomorphically correlates them using encrypted keyword trapdoors. For long messages, this design can reduce sender-side encryption and upload overhead by up to two orders of magnitude over state-of-the-art baselines. It supports ASCII case-insensitive matching with one fixed-size encrypted trapdoor and one homomorphic multiplication per fragment, yielding up to 5.47x faster correlation computation than the strongest fragmentation-based baselines. SEEK then invokes 2PC-based selected decoding, blinded zero testing, and secure aggregation, revealing only the keyword presence-or-absence bit while hiding the keyword, its length, message contents, match counts, and locations. SEEK achieves 100% accuracy under case variations that result in exact-matching failures, without requiring additional trapdoors or online communication. We further realize SEEK as an end-to-end web and cross-platform mobile application. Prototype evaluation on a weekly messaging history yields an online computation time of 1.92 s per search, demonstrating the practical feasibility and efficiency of SEEK.

---


### 138. [Disentangling Long-Term Memory via Latent Neuro-Symbolic Reasoning](https://arxiv.org/abs/2609.18461)

**<font color=#1a73e8>作者：</font>** Cai Ke, Xinghao Chen, Xiaoyu Shen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized agents are required to reason over long-term history interactions to infer both explicit preferences and implicit behavioral evidence. While early flat retrieval methods score memory fragments independently and neglect the distributed information, current structured memory frameworks rely on query-agnostic static graphs that fail to capture the context-dependent relations. Crucially, raw textual memories are inherently entangled and noisy, making fine-grained personalization and cross-session reasoning computationally prohibitive. To this end, we present LGM, a novel neuro-symbolic framework that shifts long-term memory disentanglement into a continuous latent space. Specifically, (i) instead of persisting fixed graphs, we design a tailored latent graph construction with a sparse autoencoder. Subject to each query, it maps historical interactions into latent memory nodes and disentangles the memory traces into sparse concept activations, dynamically synthesizing query-aware relational edge weights. (ii) A graph encoder then treats the query embedding as a conditioning preference to direct non-linear message passing across the task-specific latent subgraph. This yields a highly expressive memory representation for effective activations. Extensive experiments on long-term personalization benchmarks demonstrate that LGM significantly outperforms state-of-the-art baselines in capturing both explicit and implicit preferences while enabling personalized responses.

---


### 139. [CSWAM: Better Causal Semantic Representations for Out-of-Distribution Generalization in World Action Models](https://arxiv.org/abs/2609.18462)

**<font color=#1a73e8>作者：</font>** Tianbin Liu, Jian Zhu, Taiyi Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> FastWAM-style world action models enable efficient action-only inference, but generalize poorly under visual distribution shifts. Their reconstruction-oriented representations emphasize appearance-specific details, limiting generalization to unseen scenes and objects. Without observation history, the model also lacks temporal evidence for robustly identifying task-relevant state changes and motion in unfamiliar visual conditions. To address these limitations, we present the Causal Semantic World Action Model (CSWAM), which augments FastWAM with a causal semantic expert built on V-JEPA 2.1. V-JEPA provides temporally grounded representations of semantic state changes and motion with less dependence on appearance-specific details. The expert learns their future evolution from a sparse history of current and past observations and shares the history-derived context with both the video and action streams through causal attention. At inference, CSWAM conditions action denoising on the current video state and observed semantic history, retaining efficient action-only inference. We conduct simulation and real-robot experiments to evaluate generalization under distribution shifts. With embodied pretraining, CSWAM raises Randomized success on RoboTwin 2.0 Clean-to-Randomized transfer from 10.16% to 45.18%, a gain of 35.02 percentage points over FastWAM. Across two real-robot tasks and three OOD difficulty levels, CSWAM improves average success over FastWAM by 42.5 percentage points, from 27.5% to 70.0%.

---


### 140. [GeoCond: A Conditioning-Aware Reliability Adapter for Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2609.18465)

**<font color=#1a73e8>作者：</font>** David Ahmedt-Aristizabal, Mohammad Ali Armin, Russell Tsuchida 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D foundation models such as VGGT predict cameras, depth, and point maps in a single pass, but can fail silently under low overlap, low parallax, and extreme relative rotation. Stratified analyses over these factors show that these failures are governed by geometric conditioning and are poorly captured by native aleatoric confidence. We introduce GeoCond, a lightweight reliability adapter for frozen feed-forward 3D backbones. GeoCond reads the backbone's predicted geometry and outputs pose-level uncertainty and a refinement gate. During training, it can be supervised by frame-permutation orbit variance, ground-truth pose error when labels are available, or cycle residuals from unlabelled independent pose graphs. At inference, the default head requires only one backbone pass and a small MLP. On VGGT, GeoCond improves out-of-distribution (OOD) AUSE (area under the sparsification-error curve; lower is better) from $0.32$ to $0.20$ over native confidence, transfers zero-shot to outdoor extreme-view scenes, and avoids the collapse caused by applying bundle adjustment uniformly. Across multiple backbones, cycle-distilled variants provide a ground-truth-free adaptation route, including cases where permutation variance vanishes on equivariant models. The same reliability signal supports gated refinement, pose-graph weighting, calibration, curation, and capture decisions. Reliable feed-forward 3D reconstruction requires not only predicting geometry, but also knowing when that geometry should be trusted.

---


### 141. [Spatially Adaptive Noise Injection](https://arxiv.org/abs/2609.18466)

**<font color=#1a73e8>作者：</font>** Frantzeska Lavda, Maciej Falkiewicz, Van Khoa Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion samplers reverse a learned noising process using either stochastic (DDPM) or deterministic (DDIM) updates, which represent endpoints of a single family controlled by a scalar noise-injection variance that is applied identically at every spatial location. This uniform approach neglects the geometry of natural images: high-curvature regions such as edges and textures, where the denoiser is uncertain, benefit from stochastic correction, whereas smooth regions, where the score is precise, are degraded by injected noise. This work investigates whether each pixel requires stochastic correction at a given timestep and introduces Spatially Adaptive Noise Injection (SANI), a novel sampling framework that dynamically adjusts noise application on a per-pixel basis. SANI integrates a probabilistic gating mechanism with a derived spatially adaptive variance, ensuring that noise is injected precisely where needed to refine complex features while preserving well-formed structures. Experimental results and decoupling ablations demonstrate that SANI consistently improves Fréchet Inception Distance (FID) over the vanilla DDPM and DDIM endpoint samplers across diverse sampling timesteps, while remaining competitive with variance-learning baselines, highlighting the importance of spatial adaptivity in diffusion sampling.

---


### 142. [CADSplat: Sparse-View 3D Gaussian Splatting Aided by CAD Models for Robust, Photorealistic Digital-Twin Reconstruction](https://arxiv.org/abs/2609.18473)

**<font color=#1a73e8>作者：</font>** Kristof Overdulve, Lode Jorissen, Nick Michiels  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present CADSplat, a framework that reconstructs photorealistic, geometrically accurate digital twins from sparse ($<15$ views), wide-baseline posed images of an object by regularizing 3D Gaussian Splatting (3DGS) with an explicit CAD shape prior. Using such a prior requires finding a CAD model whose shape resembles the object depicted in the images and determining the pose of each camera relative to the object. We obtain both by matching segmented object silhouettes against silhouettes rendered from a CAD library and keeping the camera-to-object poses of the best-matching model. We then anchor 3D Gaussian primitives to the surface of the retrieved model and jointly optimize the 3DGS parameters, the camera-to-object registration, and a non-rigid deformation field to account for shape differences between the physical object and the CAD model. Across two real-world datasets, CADSplat outperforms unconstrained, few-shot, and mesh-texturing baselines and degrades gracefully to as few as 3 views. Our experiments show that most of the gain in rendering quality comes from how the splats are constrained---a fixed set of splats tied to a surface and moved by a single smooth deformation field---rather than from the CAD shape itself. The CAD model adds shape knowledge where views are scarcest, in the sparsest captures and on strongly self-occluded objects, and it places every camera in the object's own frame. This enables applications beyond novel-view synthesis, such as markerless augmented reality registration, per-image object pose estimation, physical simulations, and the transfer of part labels from the design to the reconstruction.

---


### 143. [A Global Readiness and Sovereignty Capability Model for Post-Quantum Cryptography Migration](https://arxiv.org/abs/2609.18477)

**<font color=#1a73e8>作者：</font>** Mohamed Aly Bouke  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographic dependence predates the quantum era, but the migration to post-quantum cryptography (PQC) opens a rare window to reshape it, because the algorithms, implementations, hardware, and standards adopted now can lock in dependence or sovereignty for decades. This paper introduces the Readiness-Sovereignty Capability Model (RSCM), a national measurement model that operationalizes PQC readiness together with cryptographic sovereignty, which current maturity models score only as readiness and the sovereignty literature defines without measuring. RSCM decomposes sovereignty into three distinct constructs, indigenous cryptographic capacity, indigenous post-quantum control, and external dependency, and certifies a post-quantum maker only through a gate requiring demonstrated, institutionally sustained creation in at least one core layer, whether design, implementation, or validation. Applying it to fifty-seven documented cryptographic actors coded from cited public evidence, and testing that coding with an independent second coder, a plausible-state bootstrap, and convergent-validity checks, we find that twenty countries clear the gate, fifteen as full-stack makers and five as research makers, eleven hold strong general capacity without post-quantum control, one is a ready adopter, and twenty-five are dependent. The gate cells show substantial weighted agreement, a quadratic-weighted kappa of 0.71, and the maker classification is stable in its core though uncertain at the threshold. Readiness tracks independent cyber indices at rank correlations up to 0.70, while post-quantum creation shows no significant correlation with the commitment index, a rank correlation of only 0.22 that separates control from readiness. The paper contributes the framework, the evidence-graded assessment, and policy directions for building indigenous quantum-safe capacity.

---


### 144. [Hyperbolic Graph Representation Learning for Differential Diagnosis on Biomedical Knowledge Graphs](https://arxiv.org/abs/2609.18481)

**<font color=#1a73e8>作者：</font>** Pietro Miotto, Lucia Mellini, Tommaso Marzi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical knowledge graphs combine ontology-derived hierarchies with transversal associations among heterogeneous entities such as phenotypes, diseases, genes, proteins, and patients. This hybrid structure raises the question of whether hyperbolic embeddings, which naturally capture tree-like organization, remain useful beyond purely hierarchical graphs. We present a preliminary study of hyperbolic graph representation learning for Mendelian-disease differential diagnosis on a patient-integrated biomedical graph. Experiments on isolated ontology subgraphs show that hyperbolic models achieve strong performance in substantially lower dimensions than Euclidean baselines. We then evaluate the models on a link-prediction task that ranks candidate diseases for each patient. Results suggest that hyperbolic embeddings can exploit biomedical hierarchical structure while supporting diagnostic reasoning over heterogeneous patient-level graphs.

---


### 145. [EasyFashion: A Human-AI Co-Creation System for Personalized Fashion Design and Sewing Pattern Generation](https://arxiv.org/abs/2609.18483)

**<font color=#1a73e8>作者：</font>** Hong Qu, Zhaoxiang Xu, Jinbo Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People often want garments that reflect their aesthetic preferences, fit their bodies, and meet their sizing needs, yet turning these requirements into physical garments remains difficult. Ready-to-wear options provide limited personalization, while custom tailoring is costly and time-consuming. Recent generative artificial intelligence (AI) systems can visualize garment ideas but often stop short of supporting downstream production. To address this gap, we present EasyFashion, a human-AI co-creation system that enables users to iteratively refine design intent for personalized garment style and size, evaluate designs through virtual try-on on reconstructed personal avatars, and generate sewing patterns for garment production. Using reference images, text descriptions, and body photos as input, EasyFashion translates user intent into structured garment specifications and try-on results. Technical experiments, user studies, and a real-world production case demonstrate the value of EasyFashion for multimodal design expression, body-specific evaluation, and production-oriented outputs in personalized garment design.

---


### 146. [Beyond Random Couplings: Contrastive Noise Alignment in Generative Flows](https://arxiv.org/abs/2609.18488)

**<font color=#1a73e8>作者：</font>** Lennart Wittke, Vinicius Azevedo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow-matching models are typically trained by corrupting data through independently sampled Gaussian noise. While simple and scalable, this forward process induces arbitrary data-noise couplings, forcing the network to learn high-curvature transports between unrelated endpoints. Existing optimal-transport methods reduce this burden by reassigning fixed noise samples to data, but the source noise distribution itself remains passive. To address this, we introduce Contrastive Noise Alignment (CNA), a training-time method that creates dynamic, contrastive couplings by optimizing the noise representations directly. By modeling the noise batch as an interacting particle system, CNA employs a cross-modal InfoNCE objective to align noise particles with their paired data targets. To prevent spatial collapse, this alignment is regularized using an angular entropy term and a radial norm penalty. We show theoretically that this equilibrium asymptotically preserves Gaussian structures, maintaining tractability during inference. Empirically, CNA improves the alignment between noise and data, reduces flow curvature, and provides better generation quality with fewer required sampling steps. For few-step, pixel-space generation (2-4 NFEs), CNA reduces FID by over 50\% compared to standard rectified flow, and by at least 24\% against Optimal Transport baselines.

---


### 147. [Learning A Unified Template for Gait Recognition](https://arxiv.org/abs/2609.18490)

**<font color=#1a73e8>作者：</font>** Panjian Huang, Saihui Hou, Junzhou Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> "What I cannot create, I do not understand."Human wisdom reveals that creation is one of the highest forms of learning. For example, Diffusion Models have demonstrated remarkable semantic structure and memory in image generation, understanding, and restoration, which intuitively benefits representation learning. However, current gait networks rarely embrace this perspective, relying primarily on learning by contrasting gait samples under varying complex conditions, leading to semantic inconsistency and uniformity issues. To address these issues, we propose Origins with generative capabilities whose underlying philosophy is that different entities are generated from a unified template, inherently regularizing gait representations within a consistent and diverse semantic space to capture accurate gait differences. Admittedly, learning this unified template is exceedingly challenging, as it requires the comprehensiveness of the template to encompass gait representations with various conditions. Inspired by Diffusion Models, Origins diffuses the unified template into timestep templates for gait generative learning, and meanwhile transfers the unified template for gait representation learning. Especially, gait generative and representation learning serve as a unified framework for end-to-end joint training. Extensive experiments on CASIA-B, CCPG,SUSTech1K, Gait3D, GREW and CCGR-MINI demonstrate that Origins performs unified generative and representation learning, achieving superior performance.

---


### 148. [Semantic-ITC: A Frame-wise Indoor Mobile Laser Scanning Dataset and Benchmark for Semantic Segmentation](https://arxiv.org/abs/2609.18493)

**<font color=#1a73e8>作者：</font>** Haiyang Wu, Muhammad Affan, George Vosselman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic labels for indoor mobile laser scanning (MLS) frames remain largely absent from current point cloud semantic segmentation benchmarks, which mainly focus on reconstructed indoor scenes or outdoor LiDAR perception. This paper introduces Semantic-ITC, to the best of our knowledge the first public dataset and benchmark for frame-wise indoor MLS semantic segmentation. The dataset contains 52 indoor sequences, 79,108 MLS frames, and 1.23 billion labeled points collected in classrooms, corridors, meeting rooms, offices, and study areas. Labels are attached directly to measured LiDAR points in each frame using 16 semantic classes covering structural elements, furniture, room equipment, vegetation, and other indoor objects. Semantic-ITC preserves the sparse, non-uniform, and frame-wise sampling pattern of indoor MLS, making it distinct from scene-level reconstructed point clouds and mesh-based indoor datasets. The annotations are produced by a hybrid workflow that combines predictions from a visual foundation model applied to synchronized RGB images, structural information from BIM, and manual refinement, with the final labels assigned to the original LiDAR frames. A single-frame benchmark is provided, and the best baseline reaches 79.27\% mIoU. Remaining errors are concentrated around object boundaries and ambiguous indoor classes, indicating the challenges of indoor MLS segmentation under sparse frame geometry and long-tailed class distributions. The dataset provides a public benchmark for evaluating semantic segmentation directly on measured indoor MLS frames and supports future studies on frame-wise indoor MLS semantic segmentation.

---


### 149. [DiT-Garment: Garment Dynamics with Diffusion Transformers](https://arxiv.org/abs/2609.18510)

**<font color=#1a73e8>作者：</font>** Antoine Dumoulin, Laurence Boissieux, Joao Regateiro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DiT-Garment to model dynamic 3D clothing over human body models in arbitrary motion. Unlike existing methods, DiT-Garment can animate garments with unseen designs and physical materials, while allowing for direct inference of deformations for any target pose. To achieve this, we leverage a 2D diffusion transformer architecture to learn 3D deformations in a 2D UV-space. As the result is non-deterministic, our generative model learns the distribution of possible outcomes. The template garment is represented as a 3D triangle mesh spatially aligned with a 3D human body model in a standardized pose. To work with different garment designs without the need of a common template or complex graph convolution operations, the diffusion transformer is conditioned on a 3D position map of the template, represented in UV-space, which allows to implicitly learn a deformation of the 3D space around the body in standard pose. Further conditioning on body motion and physical parameters allows to physically ground the model. We quantitatively and qualitatively evaluate DiT-Garment on both synthetic and real data. While only trained on synthetic simulations of automatically generated cloth designs, our method generalizes to captured and artist-made garment designs. Code and data are available for research purposes at this https URL.

---


### 150. [Learning from Distributed Eyes: Leveraging Collaborative Perception for Automated Model Adaptation](https://arxiv.org/abs/2609.18511)

**<font color=#1a73e8>作者：</font>** Yanan Ma, Yihang Tao, Zhengru Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In autonomous driving, perception models often struggle to generalize to new environments due to domain shifts. While unsupervised model adaptation offers a feasible solution without labor-intensive manual labeling, existing methods that rely solely on the ego-vehicle's data often lead to inferior pseudo-labeling performance. To address this critical issue, we propose LDE, Learning from Distributed ``Eyes", a novel framework that transforms collaborative perception (CP) into a source of high-quality supervision for model adaptation. This pseudo-labeling approach is hyperparameter-insensitive and relatively reliable, assuming CP often outperforms single-agent's perception. However, naively implementing this approach encounters (1) the communication bottleneck of sharing rich features under time and bandwidth constraints, (2) the view discrepancy between the CP view and the learner's Field of View (FoV), and (3) the unreliability even in CP-generated labels. To address these issues, we design an adaptation-oriented feature sharing mechanism that selectively transmits the most critical information for adaptation, an FoV filtering method that meticulously eliminates mismatched labels, and a curriculum learning strategy to progressively exploit pseudo labels. Extensive experiments on 3D object detection tasks demonstrate that LDE consistently outperforms both the pre-trained models and state-of-the-art unsupervised adaptation methods.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-223](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
