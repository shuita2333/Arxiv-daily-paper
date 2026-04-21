# 📦 其他研究 | 2026年04月22日

> 本类共 **535** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

---

### 1. [BASIS: Balanced Activation Sketching with Invariant Scalars for "Ghost Backpropagation"](https://arxiv.org/abs/2604.16324)

**<font color=#1a73e8>作者：</font>** Vladimer Khasia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The activation memory required for exact backpropagation scales linearly with network depth, context length, and feature dimensionality, forming an O(L * BN ) spatial bottleneck (where B is the sequence-batch cardinality and N is the feature dimension). This constraint historically throttles the scaling of deep neural networks. While randomized automatic differentiation attempts to mitigate this, it historically suffers from catastrophic variance. In this paper, we introduce BASIS (Balanced Activation Sketching with Invariant Scalars), an efficient backpropagation algorithm that fully decouples activation memory from the batch and sequence dimensions. BASIS propagates the exact error signal (dX) to preserve flawless gradient flow, but computes the weight updates (dW) using massively compressed rank-R tensors. To solve the foundational instability of sketched gradients, we propose two novel mechanisms: Balanced Hashing, which strictly eliminates off-diagonal collision variance, and Invariant Scalars, a principled bias-variance tradeoff that deterministically preserves the exact continuous energy norm of the spatial geometry. Theoretically, BASIS reduces activation memory to O(L * RN ) and heavily decreases the backward pass matrix-multiplication footprint. Empirically, training a GPT architecture for 50,000 steps validates our theoretical guarantees: at R = 32, BASIS achieves parity with (and marginally outperforms) exact backpropagation validation loss (6.575 vs. 6.616), acting as an implicit regularizer. Remarkably, the stabilized magnitude trajectory allows the model to converge smoothly even under extreme spatial compression (R = 1), proving the extreme robustness of the estimator. The code is available at this https URL

---


### 2. [UniMamba: A Unified Spatial-Temporal Modeling Framework with State-Space and Attention Integration](https://arxiv.org/abs/2604.16325)

**<font color=#1a73e8>作者：</font>** Xingsheng Chen, Xianpei Mu, Deyu Yi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series forecasting is fundamental to numerous domains such as energy, finance, and environmental monitoring, where complex temporal dependencies and cross-variable interactions pose enduring challenges. Existing Transformer-based methods capture temporal correlations through attention mechanisms but suffer from quadratic computational cost, while state-space models like Mamba achieve efficient long-context modeling yet lack explicit temporal pattern recognition. Therefore we introduce UniMamba, a unified spatial-temporal forecasting framework that integrates efficient state-space dynamics with attention-based dependency learning. UniMamba employs a Mamba Variate-Channel Encoding Layer enhanced with FFT-Laplace Transform and TCN to capture global temporal dependencies, and a Spatial Temporal Attention Layer to jointly model inter-variate correlations and temporal evolution. A Feedforward Temporal Dynamics Layer further fuses continuous and discrete contexts for accurate forecasting. Comprehensive experiments on eight public benchmark datasets demonstrate that UniMamba consistently outperforms state-of-the-art forecasting models in both forecasting accuracy and computational efficiency, establishing a scalable and robust solution for long-sequence multivariate time-series prediction.

---


### 3. [Preventing overfitting in deep learning using differential privacy](https://arxiv.org/abs/2604.16334)

**<font color=#1a73e8>作者：</font>** Alizishaan Anwar Hussein Khatri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The use of Deep Neural Network based systems in the real world is growing. They have achieved state-of-the-art performance on many image, speech and text datasets. They have been shown to be powerful systems that are capable of learning detailed relationships and abstractions from the data. This is a double-edged sword which makes such systems vulnerable to learning the noise in the training set, thereby negatively impacting performance. This is also known as the problem of \emph{overfitting} or \emph{poor generalization}. In a practical setting, analysts typically have limited data to build models that must generalize to unseen data. In this work, we explore the use of a differential-privacy based approach to improve generalization in Deep Neural Networks.

---


### 4. [Distributed Human Identity: AI-Enabled Multi-Existence Through Cognitive Replication and Robotic Embodiments](https://arxiv.org/abs/2604.16336)

**<font color=#1a73e8>作者：</font>** A S M Touhidul Islam, John Tookey  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human presence has traditionally been constrained by the limits of physical embodiment, allowing individuals to exist in only one place at a time. This article introduces Multi-Existence Identity (MEI)- a socio-technical framework that replicates cognitive, behavioral, and emotional attributes into AI-enabled embodiments capable of acting across digital and physical contexts in parallel. MEI advances beyond digital twins, telepresence, and multipresence avatars by embedding cognitive fidelity, affective resonance, and contextual responsiveness into distributed agents that function not only for, but as, the original individual. The framework integrates personality modeling, cognitive simulation, and a synchronization layer to maintain identity coherence across three embodiment channels: digital avatars, robotic embodiments, and agentic software agents. Differentiating itself from simulated assistants, MEI positions replicated identity as a dynamic and culturally situated extension of selfhood, foregrounding tacit engagement and relational authenticity. Application domains span professional work, education, healthcare, governance, family life, and media, offering transformative potential for productivity, caregiving, leadership, and creativity. Yet these opportunities also surface profound challenges concerning authenticity, consent, legal accountability, privacy, and the psychological meaning of presence. The article proposes a phased empirical roadmap to operationalize MEI through personality modeling, synchronization testing, robotic embodiment trials, and ethical stress-testing. By conceptualizing MEI as both a technological and cultural construct, the study reframes debates on identity and presence in digitally augmented societies, highlighting opportunities for human-AI integration while underscoring the need for inclusive ethical governance.

---


### 5. [How Can Explainable Artificial Intelligence Improve Trust and Transparency in Medical Diagnosis Systems?](https://arxiv.org/abs/2604.16340)

**<font color=#1a73e8>作者：</font>** Altynbek Seitenov, Ainur Nurzhanova, Azhar Bekbussinova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The growing adoption of artificial intelligence in healthcare has raised concerns about the transparency and trustworthiness of AI-driven medical diagnosis systems. Many existing models operate as black boxes, limiting clinicians' ability to understand how decisions are made. Explainable Artificial Intelligence (XAI) has been proposed as a solution to improve transparency, interpretability, and trust in AI-assisted medical tools.
This study investigates the relationship between explainability and trust in AI-based diagnostic systems. A structured survey of 30 medical students was conducted to examine the influence of XAI understanding, confidence in AI decisions, perceived usefulness, and adoption intentions. The results indicate that explanations significantly increase trust, clarity, and perceived safety of AI recommendations. Knowledge of XAI showed a positive correlation with trust (r = 0.48, p = 0.01) and perceived usefulness (r = 0.60, p = 0.001).
The findings suggest that explainability is a key factor for successful integration of AI in healthcare decision support systems. While AI explanations improve transparency and trust, participants still prefer AI to function as a support tool rather than replacing human clinical judgment.

---


### 6. [Deep Learning for Virtual Reality User Identification: A Benchmark](https://arxiv.org/abs/2604.16341)

**<font color=#1a73e8>作者：</font>** Davide Frizzo, Fabrizio Genilotti, David Petrovic 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual Reality (VR) applications require robust user identification systems to ensure secure access to equipment and protect worker identities. Motion tracking data from VR headsets and controllers has emerged as a powerful behavioral biometric, with recent studies demonstrating identification accuracies exceeding 94% across a large user base. However, the application of modern deep learning architectures, particularly State Space Models (SSM), to VR scenarios remains largely unexplored. In this work, we benchmark user identification performance across the large-scale Who is Alyx VR dataset, gathering data from 71 users playing the popular Half-Life:Alyx game. We evaluate both established architectures (Long Short-Term Memory (LSTM), Gated Recurrent Unit (GRU), Convolutional Neural Network (CNN), Temporal Convolutional Network (TCN), Transformer) and the emerging SSMs on time series motion data. Our results provide the first comprehensive benchmark of state-of-the-art and novel architectures for VR user identification, establishing baseline performance metrics for future privacy preserving authentication systems in manufacturing environments.

---


### 7. [Elder-Sim: A Psychometrically Validated Platform for Personality-Stable Elderly Digital Twins](https://arxiv.org/abs/2604.16343)

**<font color=#1a73e8>作者：</font>** Jiaqing Wang, Zhongfang Yang, Xingyuan Zhu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background: LLMs enable patient-facing conversational agents, creating a pathway toward digital twins that capture older adults' lived experiences and behavioral responses across time. A central barrier is personality drift -- inconsistent trait expression across repeated interactions -- which undermines reliability of generated trajectories and intervention-response simulation in geriatric care.
Objective: To develop ELDER-SIM, a multi-role elderly-care conversational platform for building personality-stable digital twin agents, and to propose a psychometric validation framework for quantifying personality consistency in LLM-based agents.
Methods: ELDER-SIM was implemented via n8n workflow orchestration with local LLM inference (Ollama/vLLM), integrating (1) Big Five (OCEAN) trait specifications, (2) a Cognitive Conceptualization Diagram (CCD) grounded in Beck's CBT framework, and (3) a MySQL-based long-term memory module. Ablation studies across four conditions -- Baseline, +Memory, +CCD, and +LoRA (fine-tuned on 19,717 instruction pairs from CHARLS) -- were evaluated via Cronbach's $\alpha$, ICC, and role discrimination accuracy.
Results: Reliability was acceptable to excellent across conditions (Cronbach's $\alpha$: 0.70--0.94; ICC: 0.85--0.96). Role discrimination improved from 83.3% (Baseline) to 88.9% (+Memory), 94.4% (+CCD), and 97.2% (+LoRA). CCD produced the largest consistency gain (mean $\alpha$ 0.702$\to$0.892), while LoRA achieved the highest overall consistency ($\alpha$ 0.940; ICC 0.958).
Conclusions: ELDER-SIM provides a psychometrically validated approach for constructing personality-consistent elderly digital twin agents. Structured cognitive modeling and domain adaptation reduce personality drift, supporting reliable longitudinal simulation for elderly mental health care and reproducible in silico evaluation before clinical deployment.

---


### 8. [Discovering the Latency-Elastic Trust Window: A Patentable UX Governor for Real-Time Payment Confirmation in WebRTC Streaming](https://arxiv.org/abs/2604.16344)

**<font color=#1a73e8>作者：</font>** Anton Malinovskiy  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Live streaming platforms increasingly embed payments into the interaction loop. In these systems, payment confirmation latency is not merely a back-end performance metric but a front-end UX variable that shapes user behavior, trust, and retention. This paper introduces a novel invention candidate - the Latency-Elastic Trust Window (LETW) - a control layer that computes a per-session latency budget, adapts UX feedback, and enforces jitter-aware thresholds to protect conversational rhythm. We model confirmation latency as a behavioral driver in WebRTC streaming, quantify its effect on conversion and engagement, and propose a telemetry-driven framework to manage latency thresholds. We combine a hazard model with a behavioral elasticity curve and present simulated, calibration-based results that mirror real-world response patterns. Our findings indicate that latency beyond two seconds materially reduces tip completion and repeat engagement, and that latency variance is as important as mean latency. We further formalize the LETW as a patentable UX governor that maps network conditions to user-facing modes, and we provide operational thresholds for engineering teams to enforce trust-preserving payment feedback.

---


### 9. [Lean Atlas: An Integrated Proof Environment for Scalable Human-AI Collaborative Formalization](https://arxiv.org/abs/2604.16347)

**<font color=#1a73e8>作者：</font>** Banri Yanahama, Akiyoshi Sannai  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-driven autoformalization of mathematics is advancing rapidly. However, the type checker of a proof assistant guarantees only the logical correctness of proofs; it does not verify whether propositions and definitions faithfully capture their intended mathematical content. Consequently, AI-generated formal proofs can exhibit semantic hallucination-passing the type checker yet failing to express the intended mathematics. We propose a human-in-the-loop approach in which human scientists and AI collaboratively produce formal proofs, with humans responsible for the semantic verification of propositions and definitions. To realize this approach, we develop Lean Atlas, a Lean 4 tool that visualizes the dependency graph of a Lean 4 project as an interactive web viewer, enabling human scientists to grasp the overall structure of a formalization efficiently. Its core feature, Lean Compass, is an algorithm that, given a selected theorem set, automatically extracts the project-specific nodes whose semantic correctness can affect those target statements, thereby reducing the candidate set for semantic review in large-scale formalizations. We further define *aligned Lean code* as formalization code that has undergone human semantic verification, and propose it as a quality standard for AI-generated formalizations. We evaluate the tool on six Lean 4 formalization projects with different structural characteristics; proof-heavy projects (PrimeNumberTheoremAnd, Carleson, Brownian Motion) achieved 94-99% average node reduction, a 6-theorem milestone subset of FLT achieved 59.8%, mixed PhysLib 69.0%, and definition-heavy XMSS 27.3%. Lean Atlas is available as open-source software at this https URL .

---


### 10. [MDwAIstScheduler: A Low-Cost, Voice-Activated Device for Hands-Free Clinical Scheduling](https://arxiv.org/abs/2604.16352)

**<font color=#1a73e8>作者：</font>** Diego Mardien, Frank Liu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Physicians spend nearly half their workday on EHR tasks and administrative work, contributing to burnout and reducing time for direct patient care. We present MDwAIstScheduler, a low-cost, belt-worn voice assistant that allows hands-free calendar management during patient encounters. Hidden beneath a lab coat, the device avoids the eye-contact disruptions caused by visible screens or wrist-worn devices. Running on a Raspberry Pi with cloud-based speech recognition and LLM intent extraction, the system lets clinicians simply say 'Schedule a follow-up with Mr. Smith next Tuesday at 2' and automatically creates the calendar event. Our demo show-cases this end-to-end pipeline.

---


### 11. [Hidden Technical Debt in Generative (GenUI) and Malleable User Interfaces](https://arxiv.org/abs/2604.16354)

**<font color=#1a73e8>作者：</font>** Besjon Cifliku  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Malleable software can profoundly change how users interact with digital content, enabling non-experts to create their own customized tools. However, the practical adoption of GenUI systems faces several barriers, which I unpack in this paper, including a lack of adaptable data formats, "old" security protocols, and gaps in users' cognitive and creative skills for building their own interfaces. I advocate new evaluation strategies and scientific methods to measure the impact of malleable software in user studies, document usage patterns, and ensure their practical adoption.

---


### 12. [A Multi-Technique Approach for Improving Summary Polar Diagrams](https://arxiv.org/abs/2604.16355)

**<font color=#1a73e8>作者：</font>** Aleksandar Anžel, Zewen Yang, Georges Hattab  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While the polar system may lack the universal familiarity of its Cartesian counterpart, it remains indispensable for certain tasks. Summary polar diagrams, such as Taylor and mutual information diagrams, address tasks like discovering relationships, visualizing data similarity, and quantifying correspondence. Although these diagrams are invaluable tools for uncovering data relationships, their polar nature can hinder intuitiveness and lead to issues like overplotting. We present a hybrid approach that combines overview+detail, aggregation, interactive filtering, Cartesian linking, and small multiples to enhance the clarity, comprehensiveness, and functionality of summary polar diagrams. We performed a user study to assess this approach's effectiveness, noting comparable response times among participants. Additionally, three domain experts with varying visualization experience reviewed an implemented solution applying summary polar diagrams to climate, data science (novel), and machine learning, refining the approach prior to the user study. The findings underscore the versatility of our approach in enhancing comprehension, accessibility, and utility.

---


### 13. [SetFlow: Generating Structured Sets of Representations for Multiple Instance Learning](https://arxiv.org/abs/2604.16362)

**<font color=#1a73e8>作者：</font>** Nikola Jovišić, Milica Škipina, Vanja Švenda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data scarcity and weak supervision continue to limit the performance of machine learning models in many real-world applications, such as mammography, where Multiple Instance Learning (MIL) often offers the best formulation. While recent foundation models provide strong semantic representations out of the box, effective augmentation of such representations of MIL data remains limited, as existing methods operate at the instance level and fail to capture intra-bag dependencies. In this work, we introduce SetFlow, a generative architecture that models entire MIL bags (i.e., sets) directly in the representation space. Our approach leverages the flow matching paradigm combined with a Set Transformer-inspired design, enabling it to handle permutation-invariant inputs while capturing interactions between instances within each bag. The model is conditioned on both class labels and input scale, allowing it to generate coherent and semantically consistent sets of representations. We evaluate SetFlow on a large-scale mammography benchmark using a state-of-the-art MIL-PF classification pipeline. The generated samples are shown to closely match the original data distribution and even improve downstream performance when used for augmentation. Furthermore, training on synthetic data alone shows competitive results, demonstrating the effectiveness of representation-space generative modeling for data-scarce and privacy-sensitive tasks.

---


### 14. [CSF: Black-box Fingerprinting via Compositional Semantics for Text-to-Image Models](https://arxiv.org/abs/2604.16363)

**<font color=#1a73e8>作者：</font>** Junhoo Lee, Mijin Koo, Nojun Kwak  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text-to-image models are commercially valuable assets often distributed under restrictive licenses, but such licenses are enforceable only when violations can be detected. Existing methods require pre-deployment watermarking or internal model access, which are unavailable in commercial API deployments. We present Compositional Semantic Fingerprinting (CSF), the first black-box method for attributing fine-tuned text-to-image models to protected lineages using only query access. CSF treats models as semantic category generators and probes them with compositional underspecified prompts that remain rare under fine-tuning. This gives IP owners an asymmetric advantage: new prompt compositions can be generated after deployment, while attackers must anticipate and suppress a much broader space of fingerprints. Across 6 model families (FLUX, Kandinsky, SD1.5/2.1/3.0/XL) and 13 fine-tuned variants, our Bayesian attribution framework enables controlled-risk lineage decisions, with all variants satisfying the dominance criterion.

---


### 15. [Brain-CLIPLM: Decoding Compressed Semantic Representations in EEG for Language Reconstruction](https://arxiv.org/abs/2604.16370)

**<font color=#1a73e8>作者：</font>** Xiaoli Yang, Huiyuan Tian, Yurui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decoding natural language from non-invasive electroencephalography (EEG) remains fundamentally limited by low signal-to-noise ratio and restricted information bandwidth. This raises a fundamental question regarding whether sentence-level linguistic structure can be reliably recovered from such signals. In this work, we suggest that this assumption may not hold under realistic information constraints, and instead propose a semantic compression hypothesis in which EEG signals encode a compressed set of semantic anchors rather than full linguistic structure. Under our new perspective, direct sentence reconstruction becomes an overparameterized objective relative to the intrinsic information capacity of EEG. To address this mismatch, we introduce Brain-CLIPLM, a two-stage framework that decomposes EEG-to-text decoding into semantic anchor extraction via contrastive learning and sentence reconstruction using a retrieval-grounded large language model (LLM) with Chain-of-Thought (CoT) reasoning, following a granularity matching principle that aligns decoding complexity with neural information capacity. Evaluated on the Zurich Cognitive Language Processing Corpus, Brain-CLIPLM achieves 67.55\% top-5 and 85.00\% top-25 sentence retrieval accuracy, significantly outperforming direct decoding baseline, while cross-subject evaluation confirms robust generalization. Control analyses, including permutation testing, further demonstrate that EEG-derived representations carry sentence-specific information beyond language model priors. These results suggest that EEG-to-text decoding is better framed as recovering compressed semantic content rather than reconstructing full sentences, providing a biologically grounded and data-efficient pathway for non-invasive brain-computer interfaces.

---


### 16. [Foundational Study on Authorship Attribution of Japanese Web Reviews for Actor Analysis](https://arxiv.org/abs/2604.16376)

**<font color=#1a73e8>作者：</font>** Hiroshi Matsubara, Shingo Matsugaya, Taichi Aoki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates the applicability of authorship attribution based on stylistic features to support actor analysis in threat intelligence. As a foundational step toward future application to dark web forums, we conducted experiments using Japanese review data from clear web sources. We constructed datasets from Rakuten Ichiba reviews and compared four methods: TF-IDF with logistic regression (TF-IDF+LR), BERT embeddings with logistic regression (BERT-Emb+LR), BERT fine-tuning (BERT-FT), and metric learning with $k$-nearest neighbors (Metric+kNN). Results showed that BERT-FT achieved the best performance; however, training became unstable as the number of authors scaled to several hundred, where TF-IDF+LR proved superior in terms of accuracy, stability, and computational cost. Furthermore, Top-$k$ evaluation demonstrated the utility of candidate screening, and error analysis revealed that boilerplate text, topic dependency, and short text length were primary factors causing misclassification.

---


### 17. [Computational Hermeneutics: Evaluating generative AI as a cultural technology](https://arxiv.org/abs/2604.16403)

**<font color=#1a73e8>作者：</font>** Cody Kommers, Ruth Ahnert, Maria Antoniak 等 38 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI systems are increasingly recognized as cultural technologies, yet current evaluation frameworks often treat culture as a variable to be measured rather than fundamental to the system's operation. Drawing on hermeneutic theory from the humanities, we argue that GenAI systems function as "context machines" that must inherently address three interpretive challenges: situatedness (meaning only emerges in context), plurality (multiple valid interpretations coexist), and ambiguity (interpretations naturally conflict). We present computational hermeneutics as an emerging framework offering an interpretive account of what GenAI systems do, and how they might do it better. We offer three principles for hermeneutic evaluation -- that benchmarks should be iterative, not one-off; include people, not just machines; and measure cultural context, not just model output. This perspective offers a nascent paradigm for designing and evaluating contemporary AI systems: shifting from standardized questions about accuracy to contextual ones about meaning.

---


### 18. [Heterogeneous Self-Play for Realistic Highway Traffic Simulation](https://arxiv.org/abs/2604.16406)

**<font color=#1a73e8>作者：</font>** Jinkai Qiu, Alessandro Saviolo, Chaojie Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Realistic highway simulation is critical for scalable safety evaluation of autonomous vehicles, particularly for interactions that are too rare to study from logged data alone. Yet highway traffic generation remains challenging because it requires broad coverage across speeds and maneuvers, controllable generation of rare safety-critical scenarios, and behavioral credibility in multi-agent interactions. We present PHASE, Policy for Heterogeneous Agent Self-play on Expressway, a context-aware self-play framework that addresses these three requirements through explicit per-agent conditioning for controllability, synthetic scenario generation for broad highway coverage, and closed-loop multi-agent training for realistic interaction dynamics. PHASE further supports different vehicle profiles, for example, passenger cars and articulated trailer trucks, within a single policy via vehicle-aware dynamics and context-conditioned actions, and stabilizes self-play with early termination of unrecoverable states, at-fault collision attribution, highway-aware reward shaping, coupled curricula, and robust policy optimization. Despite being trained only on synthetic data, PHASE transfers zero-shot to 512 unseen high-interaction real scenarios in exiD, achieving a 96.3% success rate and reducing ADE/FDE from 6.57/12.07 m to 2.44/5.25 m relative to a prior self-play baseline. In a learned trajectory embedding space, it also improves behavioral realism over IDM, reducing Frechet trajectory distance by 13.1% and energy distance by 20.2%. These results show that synthetic self-play can provide a scalable route to controllable and realistic highway scenario generation without direct imitation of expert logs.

---


### 19. [Matched-Learning-Rate Analysis of Attention Drift and Transfer Retention in Fine-Tuned CLIP](https://arxiv.org/abs/2604.16410)

**<font color=#1a73e8>作者：</font>** Ruize Xia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> CLIP adaptation can improve in-domain accuracy while degrading out-of-domain transfer, but comparisons between Full Fine-Tuning (Full FT) and LoRA are often confounded by different learning-rate conventions. We study how adaptation method and optimization scale jointly shape attention drift and transfer retention in CLIP using a controlled matched-learning-rate comparison of Full FT and LoRA. The completed matrix contains 80 runs on CLIP ViT-B/32 across EuroSAT and Oxford-IIIT Pets, spanning four shared learning rates ($10^{-6}$, $5{\times}10^{-6}$, $10^{-5}$, $5{\times}10^{-5}$) and five seeds, and evaluates attention-drift metrics, best validation accuracy, and adapter-aware CIFAR-100 zero-shot accuracy. Learning rate strongly modulates structural change: on EuroSAT, Full FT moves from mild entropy broadening at $10^{-6}$ to marked contraction at $5{\times}10^{-5}$, whereas LoRA remains entropy-positive across the full matched grid. At matched learning rates, LoRA preserves substantially more zero-shot transfer than Full FT, averaging $45.13\%$ versus $11.28\%$ CIFAR-100 accuracy on EuroSAT and $58.01\%$ versus $8.54\%$ on Pets. Oxford-IIIT Pets also reveals a regime effect: low-learning-rate LoRA underfits in-domain, so method-only averages can obscure when LoRA becomes competitive. Supporting rollout, patch-to-patch, and CKA analyses are directionally consistent with the controlled matrix. Overall, matched-learning-rate evaluation materially changes the interpretation of Full FT versus LoRA, and attention drift is most useful as a descriptive diagnostic of representation preservation rather than a causal explanation of transfer behavior.

---


### 20. [CGCMA: Conditionally-Gated Cross-Modal Attention for Event-Conditioned Asynchronous Fusion](https://arxiv.org/abs/2604.16411)

**<font color=#1a73e8>作者：</font>** Yunxiang Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study asynchronous alignment, a first-class multimodal learning setting in which a dense primary stream must be fused with sporadic external context whose value depends on when it arrives. Unlike standard multimodal benchmarks that assume structural synchrony, this setting requires models to reason explicitly about freshness and trust. We focus on the event-conditioned case in which continuous market states are paired with delayed web intelligence, and we use high-frequency cryptocurrency markets only as a timestamped, high-noise stress test for this broader problem. We propose CGCMA (Conditionally-Gated Cross-Modal Attention), whose central design principle is to separate text-conditioned grounding from lag-aware trust control. Text first attends over price sequences to identify event-relevant market states, after which a conditional gate uses modality agreement, web features, and lag $\tau_{\mathrm{lag}}$ to regulate residual injection and fall back toward unimodal prediction when external context is stale or contradictory. We introduce CMI (Crypto Market Intelligence), an asynchronous evaluation corpus with 27,914 real-news samples pairing high-frequency price sequences with lagged web intelligence. On the current short real-news corpus, CGCMA attains the highest mean downstream Sharpe ratio ($+0.449 \pm 0.257$) among the evaluated baselines under a shared zero-cost threshold-trading evaluation on news-available bars. Additional controls show that the gain is not explained by web scalars alone and is not recovered by simple freshness heuristics. The resulting evidence supports problem validity and a promising asynchronous multimodal gain on this stress-test setting.

---


### 21. [Safety, Security, and Cognitive Risks in State-Space Models: A Systematic Threat Analysis with Spectral, Stateful, and Capacity Attacks](https://arxiv.org/abs/2604.16424)

**<font color=#1a73e8>作者：</font>** Manoj Parmar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> State-Space Models (SSMs) -- structured SSMs (S4, S4D, DSS, S5), selective SSMs (Mamba, Mamba-2), and hybrid architectures (Jamba) -- are deployed in safety-critical long-context applications: genomic analysis, clinical time-series forecasting, and cybersecurity log processing. Their linear-time scaling is compelling, yet the security properties of their compressed-state recurrent architectures remain unstudied.
We present the first systematic treatment of SSM safety, security, and cognitive risks. Seven contributions: (1) Formal threat framework -- SSM Attack Surface (five layers), State Integrity Violation (StIV), Cross-Context Amplification Ratio $\mathcal{X}_\mathcal{S}$, and a Spectral Sensitivity Proposition grounded in the $H_\infty$ norm. (2) Three novel attack classes: spectral adversarial attacks (transfer-function gain exploitation), delayed-trigger stateful backdoors (activate thousands of steps after injection), and state capacity saturation (entropy flooding forces silent forgetting). (3) 14 MITRE ATLAS technique extensions across the full tactic chain. (4) Six-profile attacker taxonomy with kill chains for genomics, clinical, and cybersecurity domains. (5) Four cognitive risk hypotheses grounded in state-compression mechanics. (6) Governance-aligned mitigations mapped to CREST, NIST AI 600-1, and EU AI Act. (7) Empirical evaluation: targeted genomic injection achieves $\mathrm{StIV}=0.519$ vs. $0.086$ random ($6.0\times$, $p<0.001$); PGD state injection achieves $156\times$ output perturbation over random; SSD-structured extraction confirmed at $O(N^2)$ vs. $O(N^3)$ query complexity ($N\times$ speedup). Validation on pretrained checkpoints is detailed in the Appendix.

---


### 22. [Functional Similarity Metric for Neural Networks: Overcoming Parametric Ambiguity via Activation Region Analysis](https://arxiv.org/abs/2604.16426)

**<font color=#1a73e8>作者：</font>** Kutomanov Hennadii  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As modern deep learning architectures grow in complexity, representational ambiguity emerges as a critical barrier to their interpretability and reliable merging. For ReLU networks, identical functional mappings can be achieved through entirely different weight configurations due to algebraic symmetries: neuron permutation and positive diagonal scaling. Consequently, traditional parameter-based comparison methods exhibit extreme instability to slight weight perturbations during training. This paper proposes a mathematically grounded approach to constructing a stable canonical representation of neural networks and a robust functional similarity metric. We shift focus from comparing raw weights to analyzing the topology of neuron activation regions. The algorithm first eliminates scaling ambiguity via L2-normalization of weight vectors with subsequent layer compensation. Next, discrete approximations of activation regions are generated as binary functional signatures evaluated over a data sample. To overcome the computational bottleneck of comparing large binary vectors, we adapt Locality-Sensitive Hashing, specifically MinHash, providing a fast and statistically precise approximation of the Jaccard index. The final cross-network neuron matching is formulated as a linear sum assignment problem solved via the Hungarian algorithm. We demonstrate theoretically and experimentally that our metric mitigates the neuron "flickering" effect and exhibits exceptional robustness to minor weight perturbations. This framework provides a solid foundation for model merging, transfer learning, objective assessment during pruning, and Explainable AI paradigms.

---


### 23. [Refunded but Rewarded: The Double Dip Attack on Cashback Reward Engines](https://arxiv.org/abs/2604.16427)

**<font color=#1a73e8>作者：</font>** S M Zia Ur Rashid, Suman Rath  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cashback reward programs now serve as central instruments in the competitive landscape of cards, digital wallets, and payment platforms. Despite their financial significance, the business logic governing these programs is seldom treated as a security critical surface. In this paper, we study a class of reward abuse attacks that arise from flaws in how reward systems accrue, redeem, and adjust incentives when underlying transactions are reversed through refunds. Using controlled, small scale experiments on six issuer accounts we legitimately hold, we document a spectrum of real world behaviors in production systems. At one extreme, a debit based cashback program (Issuer A) never adjusts rewards when refunded transactions post, enabling a deterministic double dip cashback reward abuse attack. A credit card program (Issuer B) exhibits an analogous reward integrity violation through a statement cycle timing gap that allows reward redemption before the merchant return window closes. At an intermediate tier, a credit card issuer (Issuer F) creates negative reward entries on refunds at statement close but makes rewards redeemable immediately upon settlement, creating a timing asymmetry that allows users to extract reward value before clawback occurs. At the robust end, three credit card issuers (C, D, and E) implement indefinite negative balance enforcement with proportional clawback. We formalize reward engines as state machines, introduce two integrity invariants (Reward Integrity and Refund Reward Consistency), develop a taxonomy of vulnerability classes mapped to CWE and OWASP, and present defensive pseudo algorithms with a semi formal correctness argument that close the identified loopholes. The primary vulnerability (Issuer A) was reported through a private bug bounty program and has been acknowledged by the vendor; good faith disclosure efforts for Issuer B are detailed in Section 8.

---


### 24. [(Sparse) Attention to the Details: Preserving Spectral Fidelity in ML-based Weather Forecasting Models](https://arxiv.org/abs/2604.16429)

**<font color=#1a73e8>作者：</font>** Maksim Zhdanov, Ana Lucic, Max Welling 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Mosaic, a probabilistic weather forecasting model that addresses two principal sources of spectral degradation in ML-based weather prediction: (1) deterministic training against ensemble means and (2) compressive encoding creating an information bottleneck. Mosaic generates ensemble members through learned functional perturbations and operates on native-resolution grids via block-sparse attention, a hardware-aligned mechanism that captures long-range dependencies at linear cost by sharing keys and values across spatially adjacent queries. At 1.5$°$ resolution with 214M parameters, Mosaic matches or outperforms models trained on 6 times finer data on headline upper-air variables and achieves state-of-the-art results among 1.5$°$ models, producing well-calibrated ensembles whose individual members exhibit near-perfect spectral alignment across all resolved frequencies. A 24-member, 10-day forecast takes under 12 seconds on a single H100 GPU.

---


### 25. [Dimensional Criticality at Grokking Across MLPs and Transformers](https://arxiv.org/abs/2604.16431)

**<font color=#1a73e8>作者：</font>** Ping Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Abrupt transitions between distinct dynamical regimes are a hallmark of complex systems. Grokking in deep neural networks provides a striking example -- an abrupt transition from memorization to generalization long after training accuracy saturates -- yet robust macroscopic signatures of this transition remain elusive. Here we introduce \textbf{TDU--OFC} (Thresholded Diffusion Update--Olami-Feder-Christensen), an offline avalanche probe that converts gradient snapshots into cascade statistics and extracts a \emph{macroscopic observable} -- the time-resolved effective cascade dimension $D(t)$ -- via grokking-aligned finite-size scaling. Across Transformers trained on modular addition and MLPs trained on XOR, we discover a localized dynamical crossing of the Gaussian diffusion baseline $D=1$ precisely at the generalization transition. The crossing direction is task-dependent: modular addition descends through $D=1$ (approaching from $D>1$), while XOR ascends (from $D<1$). This opposite-direction convergence is consistent with attraction toward a candidate shared critical manifold, rather than trivial residence near $D \approx 1$. Negative controls confirm this picture: ungrokked runs remain supercritical ($D>1$) and never enter the post-transition regime. In addition, avalanche distributions exhibit heavy tails and finite-size scaling consistent with the dimensional exponent extracted from $D(t)$. Shadow-probe controls ($\alpha_{\mathrm{train}}=0$) confirm that $D(t)$ is non-invasive, and grokked trajectories diverge from ungrokked ones in $D(t)$ some $100$--$200$ epochs before the behavioral transition.

---


### 26. [Support Sufficiency as Consequence-Sensitive Compression in Belief Arbitration](https://arxiv.org/abs/2604.16434)

**<font color=#1a73e8>作者：</font>** Mark Walsh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a system commits to a hypothesis, much of the evidential structure behind that commitment is lost to compression. Standard accounts assume that selected content and scalar confidence suffice for downstream control. This paper argues that they do not, and that determining what must survive compression is itself a consequence-sensitive problem. We develop a recurrent arbitration architecture in which active constraint fields jointly determine a hypothesis geometry over candidates. Rather than carrying that geometry forward in full, the system compresses it into a support-aware control state whose resolution is regulated by current consequence geometry, arbitration memory, and resource constraints.
A bounded objective formalizes the tradeoff. Too little retained support collapses policy-relevant distinctions, producing controllers that select content adequately while misrouting verification, abstention, and recovery. Too much retained support fragments learning across overly fine contexts, degrading adaptation even as discrimination improves. These failure modes yield ordered controller predictions confirmed by a minimal repeated-interaction simulation. Adaptive controllers that regulate support resolution outperform all fixed-resolution controllers in cumulative utility. Agile adaptive control outperforms sluggish adaptive control. Fixed high-resolution control achieves the best commitment accuracy but still trails adaptive controllers because resource cost and learning fragmentation offset the gains from richer retention.
Support sufficiency should be understood not as a static representational threshold, but as a dynamic compression criterion. Robust arbitration depends on preserving the smallest support structure adequate for policy under the current consequence landscape, and on regulating that structure as conditions change across repeated cycles of inference and action.

---


### 27. [A High-Accuracy Optical Music Recognition Method Based on Bottleneck Residual Convolutions](https://arxiv.org/abs/2604.16446)

**<font color=#1a73e8>作者：</font>** Junwen Ma, Huhu Xue, Xingyuan Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Music Recognition (OMR) aims to convert printed or handwritten music score images into editable symbolic representations. This paper presents an end-to-end OMR framework that combines residual bottleneck convolutions with bidirectional gated recurrent unit (BiGRU)-based sequence modeling. A convolutional neural network with ResNet-v2-style residual bottleneck blocks and multi-scale dilated convolutions is used to extract features that encode both fine-grained symbol details and global staff-line structures. The extracted feature sequences are then fed into a BiGRU network to model temporal dependencies among musical symbols. The model is trained using the Connectionist Temporal Classification loss, enabling end-to-end prediction without explicit alignment annotations. Experimental results on the Camera-PrIMuS and PrIMuS datasets demonstrate the effectiveness of the proposed framework. On Camera-PrIMuS, the proposed method achieves a sequence error rate (SeER) of $7.52\%$ and a symbol error rate (SyER) of $0.45\%$, with pitch, type, and note accuracies of $99.33\%$, $99.60\%$, and $99.28\%$, respectively. The average training time is 1.74~s per epoch, demonstrating high computational efficiency while maintaining strong recognition performance. On PrIMuS, the method achieves a SeER of $8.11\%$ and a SyER of $0.49\%$, with pitch, type, and note accuracies of $99.27\%$, $99.58\%$, and $99.21\%$, respectively. A fine-grained error analysis further confirms the effectiveness of the proposed model.

---


### 28. [EchoChain: A Full-Duplex Benchmark for State-Update Reasoning Under Interruptions](https://arxiv.org/abs/2604.16456)

**<font color=#1a73e8>作者：</font>** Smit Nautambhai Modi, Gandharv Mahajan, Marc Wetter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-time voice assistants must revise task state when users interrupt mid-response, but existing spoken-dialog benchmarks largely evaluate turn-based interaction and miss this failure mode. We introduce EchoChain, a controlled benchmark for evaluating full-duplex state-update reasoning under mid-speech interruptions. EchoChain identifies three recurring failure patterns in post-interruption continuations: contextual inertia, interruption amnesia, and objective displacement. The benchmark generates scenario-driven conversations and injects interruptions at a standardized point relative to assistant speech onset, enabling controlled cross-model comparison. In a paired half-duplex control, total failures drop by 40.2% relative to interrupted runs, indicating that many errors are driven by state-update reasoning under interruption rather than task difficulty alone. Across evaluated real-time voice models, no system exceeds a 50% pass rate, showing substantial room for improvement in mid-generation state revision. EchoChain provides a reproducible benchmark for diagnosing state-update reasoning failures in full-duplex voice interaction.

---


### 29. [Healthcare AI for Automation or Allocation? A Transaction Cost Economics Framework](https://arxiv.org/abs/2604.16465)

**<font color=#1a73e8>作者：</font>** Ari Ercole  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare productivity is shaped not only by clinical complexity but by the costs of coordinating work under uncertainty. Transaction-cost economics offers a theory of these coordination frictions, yet has rarely been operationalised at task level across health occupations. Using task statements and frequency weights from the O*NET occupational database, we characterised healthcare work at task granularity and coded each unique task using a constrained large language model into one dominant transaction-cost category (information search, decision and bargaining, monitoring and enforcement, or adaptation and coordination) together with an overall transaction-cost intensity score. Aggregating to the occupation level, clinician roles exhibited substantially higher transaction-cost intensity than non-clinician roles, driven primarily by greater burdens of information search and decision-related coordination, while dispersion of transaction costs within occupations did not differ. These findings demonstrate systematic heterogeneity in the nature of coordination work across healthcare roles and suggest that the opportunities for digital and AI interventions are unevenly distributed, shaped less by technical task complexity than by underlying coordination structure.

---


### 30. [Multi-Label Phase Diagram Prediction in Complex Alloys via Physics-Informed Graph Attention Networks](https://arxiv.org/abs/2604.16468)

**<font color=#1a73e8>作者：</font>** Eunjeong Park, Amrita Basak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate phase equilibria are foundational to alloy design because they encode the underlying thermodynamics governing stability, transformations, and processing windows. However, while the CALculation of Phase Diagrams (CALPHAD) provides a rigorous thermodynamic framework, exploring multicomponent composition-temperature space remains computationally expensive and is typically limited to sparse section. To enable rapid phase mapping and alloy screening, we propose a physics-informed graph attention network (GAT) that learns element-aware representations and couples them with thermodynamic constraints for multi-label phase-set prediction in the Ag-Bi-Cu-Sn alloy system. Using about 25,000 equilibrium states generated with pycalphad, each composition-temperature point is represented as a four-node element graph with atomic fractions and elemental descriptors as node features. The model combines graph attention, global pooling, and a multilayer perceptron to predict nine relevant phases. To improve physical consistency, we incorporate thermodynamic constraints, applied as training penalties or as an inference-time projection. Across six binary and three ternary subsystems, the baseline model achieves a macro-F1 score of 0.951 and 93.98% exact-set match, while physics-informed decoding improves robustness and raises exact-set accuracy to about 96% on dense in-domain grids. The surrogate also generalizes to an unseen ternary section with 99.32% exact-set accuracy and to a quaternary section at 700 °C with 91.78% accuracy. These results demonstrate that attention-based graph learning coupled with thermodynamic constraint enforcement provides an effective and physically consistent surrogate for high-resolution phase mapping and extrapolative alloy screening.

---


### 31. [Latent-Compressed Variational Autoencoder for Video Diffusion Models](https://arxiv.org/abs/2604.16479)

**<font color=#1a73e8>作者：</font>** Jiarui Guan, Wenshuai Zhao, Zhengtao Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video variational autoencoders (VAEs) used in latent diffusion models typically require a sufficiently large number of latent channels to ensure high-quality video reconstruction. However, recent studies have revealed that an excessive number of latent channels can impede the convergence of latent diffusion models and deteriorate their generative performance, even when reconstruction quality remains high. We propose a latent compression method that removes high-frequency components in video latent representations rather than directly reducing the number of channels, which often compromises reconstruction fidelity. Experimental results demonstrate that the proposed method achieves superior video reconstruction quality compared to strong baselines while maintaining the same overall compression ratio.

---


### 32. [Positioning radiata pine branches requiring pruning by drone stereo vision](https://arxiv.org/abs/2604.16480)

**<font color=#1a73e8>作者：</font>** Yida Lin, Bing Xue, Mengjie Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a stereo-vision-based system mounted on a drone for detecting and localising radiata pine branches to support autonomous pruning. The proposed pipeline comprises two stages: branch segmentation and depth estimation. For segmentation, YOLOv8, YOLOv9, and Mask R-CNN variants are compared on a custom dataset of 71 stereo image pairs captured with a ZED Mini camera. For depth estimation, both a traditional method (SGBM with WLS filtering) and deep-learning-based methods (PSMNet, ACVNet, GWCNet, MobileStereoNet, RAFT-Stereo, and NeRF-Supervised Deep Stereo) are evaluated. A centroid-based triangulation algorithm with MAD outlier rejection is proposed to compute branch distance from the segmentation mask and disparity map. Qualitative evaluation at distances of 1-2 m indicates that the deep learning-based disparity maps produce more coherent depth estimates than SGBM, demonstrating the feasibility of low-cost stereo vision for automated branch positioning in forestry.

---


### 33. [Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models](https://arxiv.org/abs/2604.16481)

**<font color=#1a73e8>作者：</font>** Hoigi Seo, Byung Hyun Lee, Jaehyun Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale text-to-image (T2I) diffusion models deliver remarkable visual fidelity but pose safety risks due to their capacity to reproduce undesirable content, such as copyrighted ones. Concept erasure has emerged as a mitigation strategy, yet existing approaches struggle to balance scalability, precision, and robustness, which restricts their applicability to erasing only a few hundred concepts. To address these limitations, we present Erasing Thousands of Concepts (ETC), a scalable framework capable of erasing thousands of concepts while preserving generation quality. Our method first models low-rank concept distributions via a Student's t-distribution Mixture Model (tMM). It enables pin-point erasure of target concepts via affine optimal transport while preserving others by anchoring the boundaries of target concept distributions without pre-defined anchor concepts. We then train a Mixture-of-Experts (MoE)-based module, termed MoEraser, which removes target embeddings while preserving the anchor embeddings. By injecting noise into the text embedding projector and fine-tuning MoEraser for recovery, our framework achieves robustness to white-box attack such as module removal. Extensive experiments on over 2,000 concepts across heterogeneous domains and diffusion models demerate state-of-the-art scalability and precision in large-scale concept erasure.

---


### 34. [A Survey of Spatial Memory Representations for Efficient Robot Navigation](https://arxiv.org/abs/2604.16482)

**<font color=#1a73e8>作者：</font>** Ma. Madecheen S. Pangaliman, Steven S. Sison, Erwin P. Quilloy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As vision-based robots navigate larger environments, their spatial memory grows without bound, eventually exhausting computational resources, particularly on embedded platforms (8-16GB shared memory, $<$30W) where adding hardware is not an option. This survey examines the spatial memory efficiency problem across 88 references spanning 52 systems (1989-2025), from occupancy grids to neural implicit representations. We introduce the $\alpha = M_{\text{peak}} / M_{\text{map}}$, the ratio of peak runtime memory (the total RAM or GPU memory consumed during operation) to saved map size (the persistent checkpoint written to disk), exposing the gap between published map sizes and actual deployment cost. Independent profiling on an NVIDIA A100 GPU reveals that $\alpha$ spans two orders of magnitude within neural methods alone, ranging from 2.3 (Point-SLAM) to 215 (NICE-SLAM, whose 47,MB map requires 10GB at runtime), showing that memory architecture, not paradigm label, determines deployment feasibility. We propose a standardized evaluation protocol comprising memory growth rate, query latency, memory-completeness curves, and throughput degradation, none of which current benchmarks capture. Through a Pareto frontier analysis with explicit benchmark separation, we show that no single paradigm dominates within its evaluation regime: 3DGS methods achieve the best absolute accuracy at 90-254,MB map size on Replica, while scene graphs provide semantic abstraction at predictable cost. We provide the first independently measured $\alpha$ reference values and an $\alpha$-aware budgeting algorithm enabling practitioners to assess deployment feasibility on target hardware prior to implementation.

---


### 35. [Dynamic Eraser for Guided Concept Erasure in Diffusion Models](https://arxiv.org/abs/2604.16483)

**<font color=#1a73e8>作者：</font>** Qinghui Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure in Text-To-Image (T2I) diffusion models is vital for safe content generation, but existing inference-time methods face significant limitations. Feature-correction approaches often cause uncontrolled over-correction, while token-level interventions struggle with semantic granularity and context. Moreover, both types of methods are prone to severe semantic drift or even complete representation collapse. To address these challenges, we present Dynamic Semantic Steering (DSS), a lightweight, training-free framework for interpretable and controllable concept erasure. DSS introduces: 1) Sensitive Semantic Boundary Modeling (SSBM) to automate the discovery of safe semantic anchors, and 2) Sensitive Semantic Guidance (SSG), which leverages cross-attention features for precise detection and performs correction via a closed-form solution derived from a well-posed objective. This ensures optimal suppression of sensitive content while preserving benign semantics. DSS achieves an average erasure rate of 91.0\%, significantly outperforming SOTA methods (from 18.6\% to 85.9\%) with minimal impact on output fidelity.

---


### 36. [Saccade Attention Networks: Using Transfer Learning of Attention to Reduce Network Sizes](https://arxiv.org/abs/2604.16485)

**<font color=#1a73e8>作者：</font>** Marc Estafanous  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One of the limitations of transformer networks is the sequence length due to the quadratic nature of the attention matrix. Classical self attention uses the entire sequence length, however, the actual attention being used is sparse. Humans use a form of sparse attention when analyzing an image or scene called saccades. Focusing on key features greatly reduces computation time. By using a network (Saccade Attention Network) to learn where to attend from a large pre-trained model, we can use it to pre-process images and greatly reduce network size by reducing the input sequence length to just the key features being attended to. Our results indicate that you can reduce calculations by close to 80% and produce similar results.

---


### 37. [Aletheia: Physics-Conditioned Localized Artifact Attention (PhyLAA-X) for End-to-End Generalizable and Robust Deepfake Video Detection](https://arxiv.org/abs/2604.16486)

**<font color=#1a73e8>作者：</font>** Devendra Ghori  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art deepfake detectors achieve near-perfect in-domain accuracy yet degrade under cross-generator shifts, heavy compression, and adversarial perturbations. The core limitation remains the decoupling of semantic artifact learning from physical invariants: optical-flow discontinuities, specular-reflection inconsistencies, and cardiac-modulated reflectance (rPPG) are treated either as post-hoc features or ignored.
We introduce PhyLAA-X, a novel physics-conditioned extension of Localized Artifact Attention (LAA-X). PhyLAA-X injects three end-to-end differentiable physics-derived feature volumes - optical-flow curl, specular-reflectance skewness, and spatially-upsampled rPPG power spectra - directly into the LAA-X attention computation via cross-attention gating and a resonance consistency loss. This forces the network to learn manipulation boundaries where semantic inconsistencies and physical violations co-occur - regions inherently harder for generative models to replicate consistently.
PhyLAA-X is embedded across an efficient spatiotemporal ensemble (EfficientNet-B4+BiLSTM, ResNeXt-101+Transformer, Xception+causal Conv1D) with uncertainty-aware adaptive weighting. On FaceForensics++ (c23), Aletheia reaches 97.2% accuracy / 0.992 AUC-ROC; on Celeb-DF v2, 94.9% / 0.981; on DFDC, 90.8% / 0.966 - outperforming the strongest published baseline (LAA-Net [1]) by 4.1-7.3% in cross-generator settings and maintaining 79.4% accuracy under epsilon = 0.02 PGD-10 attacks. Single-backbone ablations confirm PhyLAA-X alone delivers a 4.2% cross-dataset AUC gain. The full production system is open-sourced at this https URL (v1.2, April 2026) with pretrained weights, the adversarial corpus (referred to as ADC-2026 in this work), and complete reproducibility artifacts.

---


### 38. [An Uncertainty-Aware Loss Function Incorporating Fuzzy Logic: Application to MRI Brain Image Segmentation](https://arxiv.org/abs/2604.16490)

**<font color=#1a73e8>作者：</font>** Hanuman Verma, Akshansh Gupta, Pranabesh Maji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate brain image segmentation, particularly for distinguishing various tissues from magnetic resonance imaging (MRI) images, plays a pivotal role in finding the neurological dis ease and medical image computing. In deep learning approaches, loss functions are very crucial for optimizing the model. In this study, we introduce a novel loss function integrating fuzzy logic to deals uncertainty issues in brain image segmentation into various tissues. It integrates the well-known categorical cross-entropy (CCE) loss function and fuzzy entropy based on fuzzy logic. By employing fuzzy logic, this loss function accounts for the inherent uncertainties in pixel classifications. The proposed loss function has been evaluated on two publicly available benchmark datasets, IBSR and OASIS, using two widely recognised architectures, U-Net and U-Net++. Experimental results demonstrate that the trained model with proposed loss function provided better results in comparison to the CCE optimisation function in terms of various performance metrics. Additionally, it effectively enhances segmentation performance while handling meaningful uncer tainty during training. The findings suggest that this approach not only improves segmentation outcomes but also contributes to the reliability of model predictions.

---


### 39. [A Lightweight Transformer for Pain Recognition from Brain Activity](https://arxiv.org/abs/2604.16491)

**<font color=#1a73e8>作者：</font>** Stefanos Gkikas, Christian Arzate Cruz, Yu Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pain is a multifaceted and widespread phenomenon with substantial clinical and societal burden, making reliable automated assessment a critical objective. This paper presents a lightweight transformer architecture that fuses multiple fNIRS representations through a unified tokenization mechanism, enabling joint modeling of complementary signal views without requiring modality-specific adaptations or increasing architectural complexity. The proposed token-mixing strategy preserves spatial, temporal, and time-frequency characteristics by projecting heterogeneous inputs onto a shared latent representation, using a structured segmentation scheme to control the granularity of local aggregation and global interaction. The model is evaluated on the AI4Pain dataset using stacked raw waveform and power spectral density representations of fNIRS inputs. Experimental results demonstrate competitive pain recognition performance while remaining computationally compact, making the approach suitable for real-time inference on both GPU and CPU hardware.

---


### 40. [LayerCache: Exploiting Layer-wise Velocity Heterogeneity for Efficient Flow Matching Inference](https://arxiv.org/abs/2604.16492)

**<font color=#1a73e8>作者：</font>** Guandong Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow Matching models achieve state-of-the-art image generation quality but incur substantial inference cost due to iterative denoising through large Transformer networks. We observe that different layer groups within a Transformer exhibit markedly heterogeneous velocity dynamics: shallow layers are highly stable and amenable to aggressive caching, while deep layers undergo large velocity changes that demand full computation. Existing caching methods, however, treat the entire Transformer as a monolithic unit, applying a single caching decision per timestep and thus failing to exploit this heterogeneity. Based on this finding, we propose LayerCache, a layer-aware caching framework that partitions the Transformer into layer groups and makes independent, per-group caching decisions at each denoising step. LayerCache introduces an adaptive JVP span K selection mechanism that leverages per-group stability measurements to balance estimation accuracy and computational savings. We formulate a three-dimensional scheduling problem over timesteps, layer groups, and JVP span, and solve it with a greedy budget allocation algorithm. On Qwen-Image (1024x1024, 50 steps), LayerCache achieves PSNR 37.46 dB (+5.38 dB over MeanCache), SSIM 0.9834, and LPIPS 0.0178 (a 70% reduction over MeanCache) at 1.37x speedup, dominating all prior caching methods on the quality-speed Pareto frontier.

---


### 41. [HQA-VLAttack: Towards High Quality Adversarial Attack on Vision-Language Pre-Trained Models](https://arxiv.org/abs/2604.16499)

**<font color=#1a73e8>作者：</font>** Han Liu, Jiaqi Li, Zhi Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Black-box adversarial attack on vision-language pre-trained models is a practical and challenging task, as text and image perturbations need to be considered simultaneously, and only the predicted results are accessible. Research on this problem is in its infancy, and only a handful of methods are available. Nevertheless, existing methods either rely on a complex iterative cross-search strategy, which inevitably consumes numerous queries, or only consider reducing the similarity of positive image-text pairs but ignore that of negative ones, which will also be implicitly diminished, thus inevitably affecting the attack performance. To alleviate the above issues, we propose a simple yet effective framework to generate high-quality adversarial examples on vision-language pre-trained models, named HQA-VLAttack, which consists of text and image attack stages. For text perturbation generation, it leverages the counter-fitting word vector to generate the substitute word set, thus guaranteeing the semantic consistency between the substitute word and the original word. For image perturbation generation, it first initializes the image adversarial example via the layer-importance guided strategy, and then utilizes contrastive learning to optimize the image adversarial perturbation, which ensures that the similarity of positive image-text pairs is decreased while that of negative image-text pairs is increased. In this way, the optimized adversarial images and texts are more likely to retrieve negative examples, thereby enhancing the attack success rate. Experimental results on three benchmark datasets demonstrate that HQA-VLAttack significantly outperforms strong baselines in terms of attack success rate.

---


### 42. [Semantically Stable Image Composition Analysis via Saliency and Gradient Vector Flow Fusion](https://arxiv.org/abs/2604.16500)

**<font color=#1a73e8>作者：</font>** Armin Dadras, Robert Sablatnig, Franziska Proksa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The reliable computational assessment of photographic composition requires features that are discriminative of spatial layout yet robust to semantic content. This paper proposes a low-level representation grounded in the assumption that composition can be understood as the flow of visual attention across geometric structure. We introduce VFCNet, which fuses saliency and edge information into a gradient vector flow (GVF) field. The model computes dual-stream GVF representations, integrates them via attention, and extracts multi-scale flow features with a DINOv3 backbone. VFCNet achieves state-of-the-art performance on the PICD benchmark (CDA-1: 0.683, CDA-2: 0.629), improving by 33.1\% and 36.1\% over the previous best method. We also show that a simple classifier on self-supervised DINOv3 features substantially outperforms more sophisticated, composition-specialized models. Code is available at this https URL

---


### 43. [Motif-Video 2B: Technical Report](https://arxiv.org/abs/2604.16503)

**<font color=#1a73e8>作者：</font>** Junghwan Lim, Wai Ting Cheung, Minsu Ha 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training strong video generation models usually requires massive datasets, large parameter counts, and substantial compute. In this work, we ask whether strong text-to-video quality is possible at a much smaller budget: fewer than 10M clips and less than 100,000 H200 GPU hours. Our core claim is that part of the answer lies in how model capacity is organized, not only in how much of it is used. In video generation, prompt alignment, temporal consistency, and fine-detail recovery can interfere with one another when they are handled through the same pathway. Motif-Video 2B addresses this by separating these roles architecturally, rather than relying on scale alone. The model combines two key ideas. First, Shared Cross-Attention strengthens text control when video token sequences become long. Second, a three-part backbone separates early fusion, joint representation learning, and detail refinement. To make this design effective under a limited compute budget, we pair it with an efficient training recipe based on dynamic token routing and early-phase feature alignment to a frozen pretrained video encoder. Our analysis shows that later blocks develop clearer cross-frame attention structure than standard single-stream baselines. On VBench, Motif-Video~2B reaches 83.76\%, surpassing Wan2.1 14B while using 7$\times$ fewer parameters and substantially less training data. These results suggest that careful architectural specialization, combined with an efficiency-oriented training recipe, can narrow or exceed the quality gap typically associated with much larger video models.

---


### 44. [Predicting Blastocyst Formation in IVF: Integrating DINOv2 and Attention-Based LSTM on Time-Lapse Embryo Images](https://arxiv.org/abs/2604.16505)

**<font color=#1a73e8>作者：</font>** Zahra Asghari Varzaneh, Niclas Wölner-Hanssen, Reza Khoshkangini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The selection of the optimal embryo for transfer is a critical yet challenging step in in vitro fertilization (IVF), primarily due to its reliance on the manual inspection of extensive time-lapse imaging data. A key obstacle in this process is predicting blastocyst formation from the limited number of daily images available. Many clinics also lack complete time-lapse systems, so full videos are often unavailable. In this study, we aimed to predict which embryos will develop into blastocysts using limited daily images from time-lapse recordings. We propose a novel hybrid model that combines DINOv2, a transformer-based vision model, with an enhanced long short-term memory (LSTM) network featuring a multi-head attention layer. DINOv2 extracts meaningful features from embryo images, and the LSTM model then uses these features to analyze embryo development over time and generate final predictions. We tested our model on a real dataset of 704 embryo videos. The model achieved 96.4% accuracy, surpassing existing methods. It also performs well with missing frames, making it valuable for many IVF laboratories with limited imaging systems. Our approach can assist embryologists in selecting better embryos more efficiently and with greater confidence.

---


### 45. [Medial Axis Aware Learning of Signed Distance Functions](https://arxiv.org/abs/2604.16512)

**<font color=#1a73e8>作者：</font>** Samuel Weidemaier, Christoph Norden-Smoch, Martin Rumpf  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a novel variational method to compute a highly accurate global signed distance function (SDF) to a given point cloud. To this end, the jump set of the gradient of the SDF, which coincides with the medial axis of the surface, is explicitly taken into account through a higher-order variational formulation that enforces linear growth along the gradient direction away from this discontinuity set. The eikonal equation and the zero-level set of the SDF are enforced as constraints. To make this variational problem computationally tractable, a phase field approximation of Ambrosio-Tortorelli type is employed. The associated phase field function implicitly describes the medial axis. The method is implemented for surfaces represented by unoriented point clouds using neural network approximations of both the SDF and the phase field. Experiments demonstrate the method's accuracy both in the near field and globally. Quantitative and qualitative comparisons with other approaches show the advantages of the proposed method.

---


### 46. [SynthPID: P&ID digitization from Topology-Preserving Synthetic Data](https://arxiv.org/abs/2604.16513)

**<font color=#1a73e8>作者：</font>** Suraj Prasad, Pinak Mahapatra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automating the digitization of Piping and Instrumentation Diagrams (P&IDs) into structured process graphs would unlock significant value in plant operations, yet progress is bottlenecked by a fundamental data problem: engineering drawings are proprietary, and the entire community shares a single public benchmark of just 12 annotated images. Prior attempts at synthetic augmentation have fallen short because template-based generators scatter symbols at random, producing graphs that bear little resemblance to real process plants and, accordingly, yield only approximately 33% edge detection accuracy under synth-only training. We argue the failure is structural rather than visual and address it by introducing SynthPID, a corpus of 665 synthetic P&IDs whose pipe topology is seeded directly from real drawings. Paired with a patch-based Relationformer adapted for high-resolution diagrams, a model trained on SynthPID alone achieves 63.8 +/- 3.1% edge mAP on PID2Graph OPEN100 without seeing a single real P&ID during training, closing within 8 pp of the real-data oracle. These gains hold up under a controlled comparison against the template-based regime, confirming that generation quality drives performance rather than model choice. A scaling study reveals that gains flatten beyond roughly 400 synthetic images, pointing to seed diversity as the binding constraint.

---


### 47. [Operationalizing Fairness in Text-to-Image Models: A Survey of Bias, Fairness Audits and Mitigation Strategies](https://arxiv.org/abs/2604.16516)

**<font color=#1a73e8>作者：</font>** Megan Smith, Venkatesh Thirugnana Sambandham, Florian Richter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-Image (T2I) generation models have been widely adopted across various industries, yet are criticized for frequently exhibiting societal stereotypes. While a growing body of research has emerged to evaluate and mitigate these biases, the field at present contends with conceptual ambiguity, for example terms like "bias" and "fairness" are not always clearly distinguished and often lack clear operational definitions. This paper provides a comprehensive systematic review of T2I fairness literature, organizing existing work into a taxonomy of bias types and fairness notions. We critically assess the gap between "target fairness" (normative ideals in T2I outputs) and "threshold fairness" (normative standards with actionable decision rules). Furthermore, we survey the landscape of mitigation strategies, ranging from prompt engineering to diffusion process manipulation. We conclude by proposing a new framework for operationalizing fairness that moves beyond descriptive metrics towards rigorous, target-based testing, offering an approach for more accountable generative AI development.

---


### 48. [Positive-Only Drifting Policy Optimization](https://arxiv.org/abs/2604.16519)

**<font color=#1a73e8>作者：</font>** Qi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the field of online reinforcement learning (RL), traditional Gaussian policies and flow-based methods are often constrained by their unimodal expressiveness, complex gradient clipping, or stringent trust-region requirements. Moreover, they all rely on post-hoc penalization of negative samples to correct erroneous actions. This paper introduces Positive-Only Drifting Policy Optimization (PODPO), a likelihood-free and gradient-clipping-free generative approach for online RL. By leveraging the drifting model, PODPO performs policy updates via advantage-weighted local contrastive drifting. Relying solely on positive-advantage samples, it elegantly steers actions toward high-return regions while exploiting the inherent local smoothness of the generative model to enable proactive error prevention. In doing so, PODPO opens a promising new pathway for generative policy learning in online settings.

---


### 49. [AgentClick: A Skill-Based Human-in-the-Loop Review Layer for Terminal AI Agents](https://arxiv.org/abs/2604.16520)

**<font color=#1a73e8>作者：</font>** Haomin Zhuang, Hanwen Xing, Xiangliang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent autonomous AI agents such as Codex, and Claude Code have made it increasingly practical for users to delegate complex tasks, including writing emails, executing code, issuing shell commands, and carrying out multi-step plans. However, despite these capabilities, human-agent interaction still largely happens through terminal interfaces or remote text-based channels such as Discord. These interaction modes are often inefficient and unfriendly: long text outputs are difficult to read and review, proposed actions lack clear structure and visual context, and users must express feedback by typing detailed corrections, which is cumbersome and often discourages effective collaboration. As a result, non-expert users in particular face a high barrier to working productively with agents. To address this gap, we present AgentClick, an interactive review layer for terminal-based agents. AgentClick is implemented as a localhost npm server paired with a skill-based plugin that connects the running agent to a browser interface, allowing users to supervise and collaborate with agents through a structured web UI rather than raw terminal text alone. The system supports a range of human-in-the-loop workflows, including email drafting and revision, plan review and modification, memory management, trajectory inspection and visualization, and error localization during agent execution. It also turns code generation and execution into a reviewable process, enabling users to inspect and intervene before consequential actions are taken. In addition, AgentClick supports persistent preference capture through editable memory and remote access over HTTP, allowing users to review agents running on servers from their personal devices. Our goal is to lower the barrier for non-expert users and improve the efficiency and quality of human-agent co-work.

---


### 50. [Fast Online 3D Multi-Camera Multi-Object Tracking and Pose Estimation](https://arxiv.org/abs/2604.16522)

**<font color=#1a73e8>作者：</font>** Linh Van Ma, Tran Thien Dat Nguyen, Moongu Jeon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a fast and online method for jointly performing 3D multi-object tracking and pose estimation using multiple monocular cameras. Our algorithm requires only 2D bounding box and pose detections, eliminating the need for costly 3D training data or computationally expensive deep learning models. Our solution is an efficient implementation of a Bayes-optimal multi-object tracking filter, enhancing computational efficiency while maintaining accuracy. We demonstrate that our algorithm is significantly faster than state-of-the-art methods without compromising accuracy, using only publicly available pre-trained 2D detection models. We also illustrate the robust performance of our algorithm in scenarios where multiple cameras are intermittently disconnected or reconnected during operation.

---


> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
