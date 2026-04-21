# 📦 其他研究 | 2026年04月22日

> 本类共 **535** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-535](./part-11.md)

---

### 401. [CFSR: Geometry-Conditioned Shadow Removal via Physical Disentanglement](https://arxiv.org/abs/2604.18032)

**<font color=#1a73e8>作者：</font>** Pan Wang, Yihao Hu, Xiujin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional shadow removal networks often treat image restoration as an unconstrained mapping, lacking the physical interpretability required to balance localized texture recovery with global illumination consistency. To address this, we propose CFSR, a multi-modal prior-driven framework that reframes shadow removal as a physics-constrained restoration process. By seamlessly integrating 3D geometric cues with large-scale foundation model semantics, CFSR effectively bridges the 2D-3D domain gap. Specifically, we first map observations into a custom HVI color space to suppress shadow-induced noise and robustly fuse RGB data with estimated depth priors. At its core, our Geometric & Semantic Dual Explicit Guided Attention mechanism utilizes DINO features and 3D surface normals to directly modulate the attention affinity matrix, structurally enforcing physical lighting constraints. To recover severely degraded regions, we inject holistic priors via a frozen CLIP encoder. Finally, our Frequency Collaborative Reconstruction Module (FCRM) achieves an optimal synthesis by decoupling the decoding process. Conditioned on geometric priors, FCRM seamlessly harmonizes the reconstruction of sharp high-frequency occlusion boundaries with the restoration of low-frequency global illumination. Extensive experiments demonstrate that CFSR achieves state-of-the-art performance across multiple challenging benchmarks.

---


### 402. [SignDPO: Multi-level Direct Preference Optimisation for Skeleton-based Gloss-free Sign Language Translation](https://arxiv.org/abs/2604.18034)

**<font color=#1a73e8>作者：</font>** Muxin Pu, Xiao-Ming Wu, Mei Kuan Lim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present SignDPO, a novel multi-level Direct Preference Optimisation (DPO) framework designed to enhance the alignment of skeleton-based Sign Language Translation. While current skeleton-based models have made significant progress using Maximum Likelihood Estimation, they are primarily constrained by an imitation-based paradigm that lacks discriminative sensitivity to the fine-grained spatio-temporal nuances of sign language, often leading to semantic drift. To address this, SignDPO shifts the optimisation goal from simple sequence mimicry to structured preference alignment across spatial, temporal, and linguistic dimensions. Our framework involves three key designs. First, we introduce a hierarchical perturbation strategy to construct spatial and temporal non-preferred samples at both global and local granularities automatically. Second, we propose a self-guiding mechanism that leverages decoder cross-attention scores to identify and perturb semantically salient skeletal regions, forcing the model to distinguish genuine sign signals from structural distortions. Third, we establish an automated language-level preference generator by fine-tuning a dedicated perturbation model, capturing complex output-level failure modes without manual annotation. Extensive experiments on three widely adopted benchmarks, CSL-Daily, How2Sign, and OpenASL, demonstrate that SignDPO consistently outperforms state-of-the-art gloss-free methods and even rivals established gloss-based ones. Our results suggest that multi-level preference alignment is a powerful paradigm for bridging the gap between high-entropy skeletal trajectories and discrete linguistic semantics.

---


### 403. [Variational Autoencoder Domain Adaptation for Cross-System Generalization in ML-Based SOP Monitoring](https://arxiv.org/abs/2604.18035)

**<font color=#1a73e8>作者：</font>** Leyla Sadighi, Stefan Karlsson, Carlos Natalino 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) models trained to detect physical-layer threats on one optical fiber system often fail catastrophically when applied to a different system, due to variations in operating wavelength, fiber properties, and network architecture. To overcome this, we propose a Domain Adaptation (DA) framework based on a Variational Autoencoder (VAE) that learns a shared representation capturing event signatures common to both systems while suppressing system-specific differences. The shared encoder is first trained on the combined data from two distinct optical systems: a 21 km O-band dark-fiber testbed (System 1) and a 63.4 km C-band live metro ring (System 2). The encoder is then frozen, and a classifier is trained using labels from an individual system. The proposed approach achieves 95.3% and 73.5% cross-system accuracy when moving from System 1 to System 2 and vice versa, respectively. This corresponds to gains of 83.4% and 51% over a fully supervised Deep Neural Network (DNN) baseline trained on a single system, while preserving intra-system performance.

---


### 404. [HABIT: Chrono-Synergia Robust Progressive Learning Framework for Composed Image Retrieval](https://arxiv.org/abs/2604.18037)

**<font color=#1a73e8>作者：</font>** Zixu Li, Yupeng Hu, Zhiwei Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) is a flexible image retrieval paradigm that enables users to accurately locate the target image through a multimodal query composed of a reference image and modification text. Although this task has demonstrated promising applications in personalized search and recommendation systems, it encounters a severe challenge in practical scenarios known as the Noise Triplet Correspondence (NTC) problem. This issue primarily arises from the high cost and subjectivity involved in annotating triplet data. To address this problem, we identify two central challenges: the precise estimation of composed semantic discrepancy and the insufficient progressive adaptation to modification discrepancy. To tackle these challenges, we propose a cHrono-synergiA roBust progressIve learning framework for composed image reTrieval (HABIT), which consists of two core modules. First, the Mutual Knowledge Estimation Module quantifies sample cleanliness by calculating the Transition Rate of mutual information between the composed feature and the target image, thereby effectively identifying clean samples that align with the intended modification semantics. Second, the Dual-consistency Progressive Learning Module introduces a collaborative mechanism between the historical and current models, simulating human habit formation to retain good habits and calibrate bad habits, ultimately enabling robust learning under the presence of NTC. Extensive experiments conducted on two standard CIR datasets demonstrate that HABIT significantly outperforms most methods under various noise ratios, exhibiting superior robustness and retrieval performance. Codes are available at this https URL

---


### 405. [HolmeSketcher: Generative 3D Sketch Mapping for Spatial Reconstruction in Crime Scene Investigation](https://arxiv.org/abs/2604.18039)

**<font color=#1a73e8>作者：</font>** Tianyi Xiao, Yizi Chen, Sidi Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Sketch mapping is widely used in crime scene investigation (CSI) to document, interpret, and communicate spatial information. However, it is typically performed on 2D media, which limits its ability to represent 3D spatial relationships. We present HolmeSketcher, a generative 3D sketch mapping system that combines a front-end 3D drawing interface with a back-end deep learning pipeline to support object generation and scene reconstruction in extended reality. In a within-subject user study (N = 15), HolmeSketcher improved the spatial accuracy and interpretability of reconstructed scenes, but with a clear trade-off of higher task load and lower usability compared with paper-based 2D sketch mapping. By integrating findings from the user study and expert interviews (N = 3), we further derive three design implications for next-generation 3D sketch mapping tools for CSI.

---


### 406. [GS-STVSR: Ultra-Efficient Continuous Spatio-Temporal Video Super-Resolution via 2D Gaussian Splatting](https://arxiv.org/abs/2604.18047)

**<font color=#1a73e8>作者：</font>** Mingyu Shi, Xin Di, Long Peng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous Spatio-Temporal Video Super-Resolution (C-STVSR) aims to simultaneously enhance the spatial resolution and frame rate of videos by arbitrary scale factors, offering greater flexibility than fixed-scale methods that are constrained by predefined upsampling ratios. In recent years, methods based on Implicit Neural Representations (INR) have made significant progress in C-STVSR by learning continuous mappings from spatio-temporal coordinates to pixel values. However, these methods fundamentally rely on dense pixel-wise grid queries, causing computational cost to scale linearly with the number of interpolated frames and severely limiting inference efficiency. We propose GS-STVSR, an ultra-efficient C-STVSR framework based on 2D Gaussian Splatting (2D-GS) that drives the spatiotemporal evolution of Gaussian kernels through continuous motion modeling, bypassing dense grid queries entirely. We exploit the strong temporal stability of covariance parameters for lightweight intermediate fitting, design an optical flow-guided motion module to derive Gaussian position and color at arbitrary time steps, introduce a Covariance resampling alignment module to prevent covariance drift, and propose an adaptive offset window for large-scale motion. Extensive experiments on Vid4, GoPro, and Adobe240 show that GS-STVSR achieves state-of-the-art quality across all benchmarks. Moreover, its inference time remains nearly constant at conventional temporal scales (X2--X8) and delivers over X3 speedup at extreme scales X32, demonstrating strong practical applicability.

---


### 407. [The Topological Dual of a Dataset: A Logic-to-Topology Encoding for AlphaGeometry-Style Data](https://arxiv.org/abs/2604.18050)

**<font color=#1a73e8>作者：</font>** Anthony Bordg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AlphaGeometry represents a milestone in neuro-symbolic reasoning, yet its architecture faces a log-linear scaling bottleneck within its symbolic deduction engine that limits its efficiency as problem complexity increases. Recent technical reports suggest that current domain-specific languages may be isomorphic as input representations to natural language, interchanging them acts as a performance-invariant transformation, implying that current neural guidance relies on superficial encodings rather than structural understanding. This paper addresses this representation bottleneck by proposing a logic-to-topology encoding designed to reveal the structural invariants of a model's latent space under a transformation of its input space. By leveraging the Logic of Observation, we utilize the duality between provability in observable theories and topologies to propose a logic-to-topology encoder for the input space. We introduce the concept of the "topological dual of a dataset", a transformation that bridges formal logic, topology, and neural processing. This framework serves as a Rosetta Stone for neuro-symbolic AI, providing a principled pathway for the mechanistic interpretability of how models navigate complex discovery paths.

---


### 408. [INTENT: Invariance and Discrimination-aware Noise Mitigation for Robust Composed Image Retrieval](https://arxiv.org/abs/2604.18051)

**<font color=#1a73e8>作者：</font>** Zhiwei Chen, Yupeng Hu, Zhiheng Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) is a challenging image retrieval paradigm that enables to retrieve target images based on multimodal queries consisting of reference images and modification texts. Although substantial progress has been made in recent years, existing methods assume that all samples are correctly matched. However, in real-world scenarios, due to high triplet annotation costs, CIR datasets inevitably contain annotation errors, resulting in incorrectly matched triplets. To address this issue, the problem of Noisy Triplet Correspondence (NTC) has attracted growing attention. We argue that noise in CIR can be categorized into two types: cross-modal correspondence noise and modality-inherent noise. The former arises from mismatches across modalities, whereas the latter originates from intra-modal background interference or visual factors irrelevant to the coarse-grained modification annotations. However, modality-inherent noise is often overlooked, and research on cross-modal correspondence noise remains nascent. To tackle above issues, we propose the Invariance and discrimiNaTion-awarE Noise neTwork (INTENT), comprising two components: Visual Invariant Composition and Bi-Objective Discriminative Learning, specifically designed to handle the two-aspect noise. The former applies causal intervention on the visual side via Fast Fourier Transform (FFT) to generate intervened composed features, enforcing visual invariance and enabling the model to ignore modality-inherent noise during composition. The latter adopts collaborative optimization with both positive and negative samples, and constructs a scalable decision boundary that dynamically adjusts decisions based on the loyalty degree, enabling robust correspondence discrimination. Extensive experiments on two widely used benchmark datasets demonstrate the superiority and robustness of INTENT.

---


### 409. [ExAI5G: A Logic-Based Explainable AI Framework for Intrusion Detection in 5G Networks](https://arxiv.org/abs/2604.18052)

**<font color=#1a73e8>作者：</font>** Saeid Sheikhi, Panos Kostakos, Lauri Loven  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intrusion detection systems (IDSs) for 5G networks must handle complex, high-volume traffic. Although opaque "black-box" models can achieve high accuracy, their lack of transparency hinders trust and effective operational response. We propose ExAI5G, a framework that prioritizes interpretability by integrating a Transformer-based deep learning IDS with logic-based explainable AI (XAI) techniques. The framework uses Integrated Gradients to attribute feature importance and extracts a surrogate decision tree to derive logical rules. We introduce a novel evaluation methodology for LLM-generated explanations, using a powerful evaluator LLM to assess actionability and measuring their semantic similarity and faithfulness. On a 5G IoT intrusion dataset, our system achieves 99.9\% accuracy and a 0.854 macro F1-score, demonstrating strong performance. More importantly, we extract 16 logical rules with 99.7\% fidelity, making the model's reasoning transparent. The evaluation demonstrates that modern LLMs can generate explanations that are both faithful and actionable, indicating that it is possible to build a trustworthy and effective IDS without compromising performance for the sake of marginal gains from an opaque model.

---


### 410. [Towards a Foundation-Model Paradigm for Aerodynamic Prediction in Three-dimensional Design](https://arxiv.org/abs/2604.18062)

**<font color=#1a73e8>作者：</font>** Yunjia Yang, Babak Gholami, Caglar Gurbuz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate machine-learning models for aerodynamic prediction are essential for accelerating shape optimization, yet remain challenging to develop for complex three-dimensional configurations due to the high cost of generating training data. This work introduces a methodology for efficiently constructing accurate surrogate models for design purposes by first pre-training a large-scale model on diverse geometries and then fine-tuning it with a few more detailed task-specific samples. A Transformer-based architecture, AeroTransformer, is developed and tailored for large-scale training to learn aerodynamics. The methodology is evaluated on transonic wings, where the model is pre-trained on SuperWing, a dataset of nearly 30000 samples with broad geometric diversity, and subsequently fine-tuned to handle specific wing shapes perturbed from the Common Research Model. Results show that, with 450 task-specific samples, the proposed methodology achieves 0.36% error on surface-flow prediction, reducing 84.2% compared to training from scratch. The influence of model configurations and training strategies is also systematically studied to provide guidance on effectively training and deploying such models under limited data and computational budgets. To facilitate reuse, we release the datasets and the pre-trained models at this https URL. An interactive design tool is also built on the pre-trained model and is available online at this https URL.

---


### 411. [Understanding Human Actions through the Lens of Executable Models](https://arxiv.org/abs/2604.18064)

**<font color=#1a73e8>作者：</font>** Rimvydas Rubavicius, Manisha Dubey, N. Siddharth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-centred systems require an understanding of human actions in the physical world. Temporally extended sequences of actions are intentional and structured, yet existing methods for recognising what actions are performed often do not attempt to capture their structure, particularly how the actions are executed. This, however, is crucial for assessing the quality of the action's execution and its differences from other actions. To capture the internal mechanics of actions, we introduce a domain-specific language EXACT that represents human motions as underspecified motion programs, interpreted as reward-generating functions for zero-shot policy inference using forward-backwards representations. By leveraging the compositional nature of EXACT motion programs, we combine individual policies into an executable neuro-symbolic model that uses program structure for compositional modelling. We evaluate the utility of the proposed pipeline for creating executable action models by analysing motion-capture data to understand human actions, for the tasks of human action segmentation and action anomaly detection. Our results show that the use of executable action models improves data efficiency and captures intuitive relationships between actions compared with monolithic, task-specific approaches.

---


### 412. [Enhancing Anomaly-Based Intrusion Detection Systems with Process Mining](https://arxiv.org/abs/2604.18066)

**<font color=#1a73e8>作者：</font>** Francesco Vitale, Francesco Grimaldi, Massimiliano Rak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Anomaly-based Intrusion Detection Systems (IDSs) ensure protection against malicious attacks on networked systems. While deep learning-based IDSs achieve effective performance, their limited trustworthiness due to black-box architectures remains a critical constraint. Despite existing explainable techniques offering insight into the alarms raised by IDSs, they lack process-based explanations grounded in packet-level sequencing analysis. In this paper, we propose a method that employs process mining techniques to enhance anomaly-based IDSs by providing process-based alarm severity ratings and explanations for alerts. Our method prioritizes critical alerts and maintains visibility into network behavior, while minimizing disruption by allowing misclassified benign traffic to pass. We apply the method to the publicly available USB-IDS-TC dataset, which includes anomalous traffic affected by different variants of the Slowloris DoS attack. Results show that our method is able to discriminate between low- to very-high-severity alarms while preserving up to 99.94% recall and 99.99% precision, effectively discarding false positives while providing different degrees of severity for the true positives.

---


### 413. [Towards Real-Time ECG and EMG Modeling on $μ$ NPUs](https://arxiv.org/abs/2604.18067)

**<font color=#1a73e8>作者：</font>** Josh Millar, Ashok Samraj Thangarajan, Soumyajit Chatterjee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The miniaturisation of neural processing units (NPUs) and other low-power accelerators has enabled their integration into microcontroller-scale wearable hardware, supporting near-real-time, offline, and privacy-preserving inference. Yet physiological signal analysis has remained infeasible on such hardware; recent Transformer-based models show state-of-the-art performance but are prohibitively large for resource- and power-constrained hardware and incompatible with $\mu$ NPUs due to their dynamic attention operations. We introduce PhysioLite, a lightweight, NPU-compatible model architecture and training framework for ECG/EMG signal analysis. Using learnable wavelet filter banks, CPU-offloaded positional encoding, and hardware-aware layer design, PhysioLite reaches performance comparable to state-of-the-art Transformer-based foundation models on ECG and EMG benchmarks, while being <10% of the size ($\sim$370KB with 8-bit quantization). We also profile its component-wise latency and resource consumption on both the MAX78000 and HX6538 WE2 $\mu$ NPUs, demonstrating its viability for signal analysis on constrained, battery-powered hardware. We release our model(s) and training framework at: this https URL.

---


### 414. [Modeling Human Perspectives with Socio-Demographic Representations](https://arxiv.org/abs/2604.18069)

**<font color=#1a73e8>作者：</font>** Leixin Zhang, Cagri Coltekin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans often hold different perspectives on the same issues. In many NLP tasks, annotation disagreement can reflect valid subjective perspectives. Modeling annotator perspectives and understanding their relationship with other human factors, such as socio-demographic attributes, have received increasing attention. Prior work typically focuses on single demographic factors or limited combinations. However, in real-world settings, annotator perspectives are shaped by complex social contexts, and finer-grained socio-demographic attributes can better explain human perspectives. In this work, we propose Socio-Contrastive Learning, a method that jointly models annotator perspectives while learning socio-demographic representations. Our method provides an effective approach for the fusion of socio-demographic features and textual representations to predict annotator perspectives, outperforming standard concatenation-based methods. The learned representations further enable analysis and visualization of how demographic factors relate to variation in annotator perspectives. Our code is available at GitHub: this https URL

---


### 415. [Architectural Design Decisions in AI Agent Harnesses](https://arxiv.org/abs/2604.18071)

**<font color=#1a73e8>作者：</font>** Hu Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agent systems increasingly rely on reusable non-LLM engineering infrastructure that packages tool mediation, context handling, delegation, safety control, and orchestration. Yet the architectural design decisions in this surrounding infrastructure remain understudied. This paper presents a protocol-guided, source-grounded empirical study of 70 publicly available agent-system projects, addressing three questions: which design-decision dimensions recur across projects, which co-occurrences structure those decisions, and which typical architectural patterns emerge. Methodologically, we contribute a transparent investigation procedure for analyzing heterogeneous agent-system corpora through source-code and technical-material reading. Empirically, we identify five recurring design dimensions (subagent architecture, context management, tool systems, safety mechanisms, and orchestration) and find that the corpus favors file-persistent, hybrid, and hierarchical context strategies; registry-oriented tool systems remain dominant while MCP- and plugin-oriented extensions are emerging; and intermediate isolation is common but high-assurance audit is rare. Cross-project co-occurrence analysis reveals that deeper coordination pairs with more explicit context services, stronger execution environments with more structured governance, and formalized tool-registration boundaries with broader ecosystem ambitions. We synthesize five recurring architectural patterns spanning lightweight tools, balanced CLI frameworks, multi-agent orchestrators, enterprise systems, and scenario-verticalized projects. The result provides an evidence-based account of architectural regularities in agent-system engineering, with grounded guidance for framework designers, selectors, and researchers.

---


### 416. [Class-specific diffusion models improve military object detection in a low-data domain](https://arxiv.org/abs/2604.18076)

**<font color=#1a73e8>作者：</font>** Ella P. Fokkinga, Jan Erik van Woerden, Thijs A. Eker 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based image synthesis has emerged as a promising source of synthetic training data for AI-based object detection and classification. In this work, we investigate whether images generated with diffusion can improve military vehicle detection under low-data conditions. We fine-tuned the text-to-image diffusion model FLUX.1 [dev] using LoRA with only 8 or 24 real images per class across 15 vehicle categories, resulting in class-specific diffusion models, which were used to generate new samples from automatically generated text prompts. The same real images were used to fine-tune the RF-DETR detector for a 15-class object detection task. Synthetic datasets generated by the diffusion models were then used to further improve detector performance. Importantly, no additional real data was required, as the generative models leveraged the same limited training samples. FLUX-generated images improved detection performance, particularly in the low-data regime (up to +8.0% mAP$_{50}$ with 8 real samples). To address the limited geometric control of text prompt-based diffusion, we additionally generated structurally guided synthetic data using ControlNet with Canny edge-map conditioning, yielding a FLUX-ControlNet (FLUX-CN) dataset with explicit control over viewpoint and pose. Structural guidance further enhanced performance when data is scarce (+4.1% mAP$_{50}$ with 8 real samples), but no additional benefit was observed when more real data is available. This study demonstrates that object-specific diffusion models are effective for improving military object detection in a low-data domain, and that structural guidance is most beneficial when real data is highly limited. These results highlight generative image data as an alternative to traditional simulation pipelines for the training of military AI systems.

---


### 417. [Dynamic Risk Assessment by Bayesian Attack Graphs and Process Mining](https://arxiv.org/abs/2604.18080)

**<font color=#1a73e8>作者：</font>** Francesco Vitale, Simone Guarino, Stefano Perone 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While attack graphs are useful for identifying major cybersecurity threats affecting a system, they do not provide operational support for determining the likelihood of having a known vulnerability exploited, or that critical system nodes are likely to be compromised. In this paper, we perform dynamic risk assessment by combining Bayesian Attack Graphs (BAGs) and online monitoring of system behavior through process mining. Specifically, the proposed approach applies process mining techniques to characterize malicious network traffic and derive evidence regarding the probability of having a vulnerability actively exploited. This evidence is then provided to a BAG, which updates its conditional probability tables accordingly, enabling dynamic assessment of vulnerability exploitation. We apply our method to a cybersecurity testbed instantiating several machines deployed on different subnets and affected by several CVE vulnerabilities. The testbed is stimulated with both benign traffic and malicious behavior, which simulates network attack patterns aimed at exploiting the CVE vulnerabilities. The results indicate that our proposal effectively detects whether vulnerabilities are being actively exploited, allowing for an updated assessment of the probability of system compromise.

---


### 418. [Implicit neural representations as a coordinate-based framework for continuous environmental field reconstruction from sparse ecological observations](https://arxiv.org/abs/2604.18083)

**<font color=#1a73e8>作者：</font>** Agnieszka Pregowska, Hazem M. Kalaji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing continuous environmental fields from sparse and irregular observations remains a central challenge in environmental modelling and biodiversity informatics. Many ecological datasets are heterogeneous in space and time, making grid-based approaches difficult to scale or generalise across domains. Here, we evaluate implicit neural representations (INRs) as a coordinate-based modelling framework for learning continuous spatial and spatio-temporal fields directly from coordinate inputs. We analyse their behaviour across three representative modelling scenarios: species distribution reconstruction, phenological dynamics, and morphological segmentation derived from open biodiversity data. Beyond predictive performance, we examine interpolation behaviour, spatial coherence, and computational characteristics relevant for environmental modelling workflows, including scalability, resolution-independent querying, and architectural inductive bias. Results show that neural fields provide stable continuous representations with predictable computational cost, complementing classical smoothers and tree-based approaches. These findings position coordinate-based neural fields as a flexible representation layer that can be integrated into environmental modelling pipelines and exploratory analysis frameworks for large, irregularly sampled datasets.

---


### 419. [Mix and Match: Context Pairing for Scalable Topic-Controlled Educational Summarisation](https://arxiv.org/abs/2604.18087)

**<font color=#1a73e8>作者：</font>** Nathikan Yodthapa, Thanapong Intharah, Sahan Bulathwela  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Topic-controlled summarisation enables users to generate summaries focused on specific aspects of source documents. This paper investigates a data augmentation strategy for training small language models (sLMs) to perform topic-controlled summarisation. We propose a pairwise data augmentation method that combines contexts from different documents to create contrastive training examples, enabling models to learn the relationship between topics and summaries more effectively. Using the SciTLDR dataset enriched with Wikipedia-derived topics, we systematically evaluate how augmentation scale affects model performance. Results show consistent improvements in win rate and semantic alignment as the augmentation scale increases, while the amount of real training data remains fixed. Consequently, a T5-base model trained with our augmentation approach achieves competitive performance relative to larger models, despite using significantly fewer parameters and substantially fewer real training examples.

---


### 420. [Autonomous Unmanned Aircraft Systems for Enhanced Search and Rescue of Drowning Swimmers: Image-Based Localization and Mission Simulation](https://arxiv.org/abs/2604.18088)

**<font color=#1a73e8>作者：</font>** Sascha Emanuel Zell, Toni Schneidereit, Armin Fügenschuh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Drowning is an omnipresent risk associated with any activity on or in the water, and rescuing a drowning person is particularly challenging because of the time pressure, making a short response time important. Further complicating water rescue are unsupervised and extensive swimming areas, precise localization of the target, and the transport of rescue personnel. Technical innovations can provide a remedy: We propose an Unmanned Aircraft System (UAS), also known as a drone-in-a-box system, consisting of a fleet of Unmanned Aerial Vehicles (UAVs) allocated to purpose-built hangars near swimming areas. In an emergency, the UAS can be deployed in addition to Standard Rescue Operation (SRO) equipment to locate the distressed person early by performing a fully automated Search and Rescue (S&R) operation and dropping a flotation device. In this paper, we address automatically locating distressed swimmers using the image-based object detection architecture You Only Look Once (YOLO). We present a dataset created for this application and outline the training process. We evaluate the performance of YOLO versions 3, 5, and 8 and architecture sizes (nano, extra-large) using Mean Average Precision (mAP) metrics mAP@.5 and mAP@.5:.95. Furthermore, we present two Discrete-Event Simulation (DES) approaches to simulate response times of SRO and UAS-based water rescue. This enables estimation of time savings relative to SRO when selecting the UAS configuration (type, number, and location of UAVs and hangars). Computational experiments for a test area in the Lusatian Lake District, Germany, show that UAS assistance shortens response time. Even a small UAS with two hangars, each containing one UAV, reduces response time by a factor of five compared to SRO.

---


### 421. [Towards E-Value Based Stopping Rules for Bayesian Deep Ensembles](https://arxiv.org/abs/2604.18089)

**<font color=#1a73e8>作者：</font>** Emanuel Sommer, Rickmer Schulte, Sarah Deubner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian Deep Ensembles (BDEs) represent a powerful approach for uncertainty quantification in deep learning, combining the robustness of Deep Ensembles (DEs) with flexible multi-chain MCMC. While DEs are affordable in most deep learning settings, (long) sampling of Bayesian neural networks can be prohibitively costly. Yet, adding sampling after optimizing the DEs has been shown to yield significant improvements. This leaves a critical practical question: How long should the sequential sampling process continue to yield significant improvements over the initial optimized DE baseline? To tackle this question, we propose a stopping rule based on E-values. We formulate the ensemble construction as a sequential anytime-valid hypothesis test, providing a principled way to decide whether or not to reject the null hypothesis that MCMC offers no improvement over a strong baseline, to early stop the sampling. Empirically, we study this approach for diverse settings. Our results demonstrate the efficacy of our approach and reveal that only a fraction of the full-chain budget is often required.

---


### 422. [Decision-Aware Attention Propagation for Vision Transformer Explainability](https://arxiv.org/abs/2604.18094)

**<font color=#1a73e8>作者：</font>** Sehyeong Jo, Gangjae Jang, Haesol Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have become a dominant architecture in computer vision, yet their prediction process remains difficult to interpret because information is propagated through complex interactions across layers and attention heads. Existing attention based explanation methods provide an intuitive way to trace information flow. However, they rely mainly on raw attention weights, which do not explicitly reflect the final decision and often lead to explanations with limited class discriminability. In contrast, gradient based localization methods are more effective at highlighting class specific evidence, but they do not fully exploit the hierarchical attention propagation mechanism of transformers. To address this limitation, we propose Decision-Aware Attention Propagation (DAP), an attribution method that injects decision-relevant priors into transformer attention propagation. By estimating token importance through gradient based localization and integrating it into layer wise attention rollout, the method captures both the structural flow of attention and the evidence most relevant to the final prediction. Consequently, DAP produces attribution maps that are more class sensitive, compact, and faithful than those generated by conventional attention based methods. Extensive experiments across Vision Transformer variants of different model scales show that DAP consistently outperforms existing baselines in both quantitative metrics and qualitative visualizations, indicating that decision aware propagation is an effective direction for improving ViT interpretability.

---


### 423. [DSAINet: An Efficient Dual-Scale Attentive Interaction Network for General EEG Decoding](https://arxiv.org/abs/2604.18095)

**<font color=#1a73e8>作者：</font>** Zhiyuan Ma, Zeyuan Li, Zihao Qiu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In real-world applications of noninvasive electroencephalography (EEG), specialized decoders often show limited generalizability across diverse tasks under subject-independent settings. One central challenge is that task-relevant EEG signals often follow different temporal organization patterns across tasks, while many existing methods rely on task-tailored architectural designs that introduce task-specific temporal inductive biases. This mismatch makes it difficult to adapt temporal modeling across tasks without changing the model configuration. To address these challenges, we propose DSAINet, an efficient dual-scale attentive interaction network for general EEG decoding. Specifically, DSAINet constructs shared spatiotemporal token representations from raw EEG signals and models diverse temporal dynamics through parallel convolutional branches at fine and coarse scales. The resulting representations are then adaptively refined by intra-branch attention to emphasize salient scale-specific patterns and by inter-branch attention to integrate task-relevant features across scales, followed by adaptive token aggregation to yield a compact representation for prediction. Extensive experiments on five downstream EEG decoding tasks across ten public datasets show that DSAINet consistently outperforms 13 representative baselines under strict subject-independent evaluation. Notably, this performance is achieved using the same architecture hyperparameters across datasets. Moreover, DSAINet achieves a favorable accuracy-efficiency trade-off with only about 77K trainable parameters and provides interpretable neurophysiological insights. The code is publicly available at this https URL.

---


### 424. [The Collaboration Gap in Human-AI Work](https://arxiv.org/abs/2604.18096)

**<font color=#1a73e8>作者：</font>** Varad Vishwarupe, Marina Jirotka, Nigel Shadbolt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly presented as collaborators in programming, design, writing, and analysis. Yet the practical experience of working with them often falls short of this promise. In many settings, users must diagnose misunderstandings, reconstruct missing assumptions, and repeatedly repair misaligned responses. This poster introduces a conceptual framework for understanding why such collaboration remains fragile. Drawing on a constructivist grounded theory analysis of 16 interviews with designers, developers, and applied AI practitioners working on LLM-enabled systems, and informed by literature on human-AI collaboration, we argue that stable collaboration depends not only on model capability but on the interaction's grounding conditions. We distinguish three recurrent structures of human-AI work: one-shot assistance, weak collaboration with asymmetric repair, and grounded collaboration. We propose that collaboration breaks down when the appearance of partnership outpaces the grounding capacity of the interaction and contribute a framework for discussing grounding, repair, and interaction structure in LLM-enabled work.

---


### 425. [Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models](https://arxiv.org/abs/2604.18107)

**<font color=#1a73e8>作者：</font>** Zehua Zang, Xi Wang, Fuchun Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action models (VLAs) achieve remarkable performance in sequential decision-making but remain fragile to subtle environmental shifts, such as small changes in object pose. We attribute this brittleness to trajectory overfitting, where VLAs over-attend to the spurious correlation between actions and entities, then reproduce memorized action patterns. We propose Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model. PDF mitigates the spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency. To further improve stability, PDF learns a lightweight perturbation module that retrospectively adjusts action logits guided by delayed feedback, correcting overconfidence issue. Experiments on LIBERO (+7.4\% success rate) and Atari (+10.3 human normalized score) demonstrate consistent gains of PDF in task success over vanilla VLA and VLA with test-time adaptation, establishing a practical path toward reliable test-time adaptation in multimodal decision-making agents. The code is available at \href{this https URL}{this https URL}.

---


### 426. [LoRaQ: Optimized Low Rank Approximation for 4-bit Quantization](https://arxiv.org/abs/2604.18117)

**<font color=#1a73e8>作者：</font>** Yann Bouquet, Alireza Khodamoradi, Sophie Yáng Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is essential for deploying large diffusion transformers on resource-constrained hardware, but aggressive 4-bit quantization significantly degrades generative performance. Low-rank approximation methods have emerged as a promising solution by appending auxiliary linear branches to restore performance. However, current state-of-the-art approaches assume these branches must retain high precision (W16A16) and rely on heavy, data-dependent calibration for initialization. We challenge both limitations with LoRaQ (Low-Rank Approximated Quantization), a simple, data-free calibration approach that optimizes quantization error compensation. By overcoming the need for high-precision branches, LoRaQ enables the first fully sub-16 bit pipeline, allowing the low-rank branch itself to be quantized. We demonstrate that, at equal memory overhead, LoRaQ outperforms the state-of-the-art methods in their native implementations on Pixart-$\Sigma$ and SANA. We also analyze mixed-precision configurations, showing that setups such as W8A8, W6A6, and W4A8 for the low-rank branch, alongside a W4 main layer, yield superior results while maintaining a fully quantized architecture compatible with modern mixed-precision hardware.

---


### 427. [Enabling Sensitive Conversations with Consent Boundaries: Moa, a Platform for Discussing PhD Advising Relationships](https://arxiv.org/abs/2604.18121)

**<font color=#1a73e8>作者：</font>** Jane Im, Kentaro Toyama  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When an individual is harmed by someone in power, such as a workplace manager, it can help to identify allies--people who would offer sympathy, advice, or supportive action. However, ally discovery is fraught because the very people who might be most relevant--e.g., someone who reports to the same manager--might not be sympathetic and could potentially exacerbate the harm. We examine this problem in the specific context of PhD students navigating advising challenges and present a social media platform called "Moa" that brings together a number of features that we believe facilitate ally discovery. Moa's most novel element is an audience selection process that uses what we call consent boundaries, which allow users to flexibly define each post or comment's audience based on factors such as common social identity or lived experience, all while preserving anonymity--neither senders nor recipients learn each other's identities, even as the post reaches the right audience. A 3-week field study with 47 real-world users showed that the features in combination facilitated sensitive conversations about advising, with 22.6% of users using consent boundaries. We discuss both our overall "recipe" for systems for ally discovery and the benefits of a consent-centered approach to design.

---


### 428. [Decisive: Guiding User Decisions with Optimal Preference Elicitation from Unstructured Documents](https://arxiv.org/abs/2604.18122)

**<font color=#1a73e8>作者：</font>** Akriti Jain, Anish Mulay, Divyansh Verma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decision-making is a cognitively intensive task that requires synthesizing relevant information from multiple unstructured sources, weighing competing factors, and incorporating subjective user preferences. Existing methods, including large language models and traditional decision-support systems, fall short: they often overwhelm users with information or fail to capture nuanced preferences accurately. We present Decisive, an interactive decision-making framework that combines document-grounded reasoning with Bayesian preference inference. Our approach grounds decisions in an objective option-scoring matrix extracted from source documents, while actively learning a user's latent preference vector through targeted elicitation. Users answer pairwise tradeoff questions adaptively selected to maximize information gain over the final decision. This process converges efficiently, minimizing user effort while ensuring recommendations remain transparent and personalized. Through extensive experiments, we demonstrate that our approach significantly outperforms both general-purpose LLMs and existing decision-making frameworks achieving up to 20% improvement in decision accuracy over strong baselines across domains.

---


### 429. [ConventionPlay: Capability-Limited Training for Robust Ad-Hoc Collaboration](https://arxiv.org/abs/2604.18123)

**<font color=#1a73e8>作者：</font>** Abhishek Sriraman, Eleni Vasilaki, Robert Loftin  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Ad-hoc collaboration often relies on identifying and adhering to shared conventions. However, when partners can follow multiple conventions, agents must do more than simply adapt; they must actively steer the team toward the most effective joint strategy. We present ConventionPlay, a reinforcement learning-based approach that extends cognitive hierarchies to include a diverse population of adaptive followers. By training against partners with varied capability limits, our agent learns to probe its partner's repertoire, leading the team when possible and following when necessary. Our results in canonical coordination tasks show that ConventionPlay achieves superior coordination efficiency, particularly in settings where conventions have differentiated payoffs.

---


### 430. [Depth Registers Unlock W4A4 on SwiGLU: A Reader/Generator Decomposition](https://arxiv.org/abs/2604.18128)

**<font color=#1a73e8>作者：</font>** Ziyang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study post-training W4A4 quantization in a controlled 300M-parameter SwiGLU decoder-only language model trained on 5B tokens of FineWeb-Edu, and ask which input-activation sites dominate the error. Naive round-to-nearest W4A4 collapses validation perplexity from FP16 23.6 to 1727. A simple residual-axis training-time intervention -- Depth Registers with a register-magnitude hinge loss (DR+sink) -- reduces this to 119 (about 14x) at matched FP16 PPL and matched zero-shot capacity, and composes with SmoothQuant to 39.9 PPL. The residual ~2 PPL gap to FP16 is the diagnostic core. We decompose W4A4 damage by input-activation site: the five trainable linears in a SwiGLU block split into residual-axis readers (qkv, w1, w3) and block-internal generators (o_proj, w2). Elementary norm arguments show residual-axis magnitude control bounds readers tightly but leaves w2's bilinear input bounded only by the trivial product of factor bounds; empirically, DR+sink collapses reader kurtosis while leaving generators essentially unchanged, and the reader-rescued W4A4 residue is flat at ~0.28 nats across three matched checkpoints with Delta-remove(w2) dominating. We present DR+sink as a training-time probe rather than a deployment proposal: a post-hoc alternative (Per-Linear QuaRot) nearly matches it on the reader axis. Full QuaRot -- adding online per-head value Hadamard plus online w2-input rotation -- does not close the gap either, directly testing the prediction that orthogonal rotation cannot bound the bilinear SwiGLU tail. Claims are specific to our 300M, 5B-token, single-seed setting, and our experiments do not isolate the partition from the hinge.

---


### 431. [An `Inverse' Experimental Framework to Estimate Market Efficiency](https://arxiv.org/abs/2604.18130)

**<font color=#1a73e8>作者：</font>** Thomas Asikis, Heinrich Nax  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital marketplaces processing billions of dollars annually represent critical infrastructure in sociotechnical ecosystems, yet their performance optimization lacks principled measurement frameworks that can inform algorithmic governance decisions regarding market efficiency and fairness from complex market data. By looking at orderbook data from double auction markets alone, because bids and asks do not represent true maximum willingnesses to buy and true minimum willingnesses to sell, there is little an economist can say about the market's actual performance in terms of allocative efficiency. We turn to experimental data to address this issue, `inverting' the standard induced value approach of double auction experiments. Our aim is to predict key market features relevant to market efficiency, particularly allocative efficiency, using orderbook data only -- specifically bids, asks and price realizations, but not the induced reservation values -- as early as possible. Since there is no established model of strategically optimal behavior in these markets, and because orderbook data is highly unstructured, non-stationary and non-linear, we propose quantile-based normalization techniques that help us build general predictive models. We develop and train several models, including linear regressions and gradient boosting trees, leveraging quantile-based input from the underlying supply-demand model. Our models can predict allocative efficiency with reasonable accuracy from the earliest bids and asks, and these predictions improve with additional realized price data. The performance of the prediction techniques varies by target and market type. Our framework holds significant potential for application to real-world market data, offering valuable insights into market efficiency and performance, even prior to any trade realizations.

---


### 432. [Soft Label Pruning and Quantization for Large-Scale Dataset Distillation](https://arxiv.org/abs/2604.18135)

**<font color=#1a73e8>作者：</font>** Xiao Lingao, Yang He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale dataset distillation requires storing auxiliary soft labels that can be 30-40x larger on ImageNet-1K and 200x larger on ImageNet-21K than the condensed images, undermining the goal of dataset compression. We identify two fundamental issues necessitating such extensive labels: (1) insufficient image diversity, where high within-class similarity in synthetic images requires extensive augmentation, and (2) insufficient supervision diversity, where limited variety in supervisory signals during training leads to performance degradation at high compression rates. To address these challenges, we propose Label Pruning and Quantization for Large-scale Distillation (LPQLD). We enhance image diversity via class-wise batching and batch-normalization supervision during synthesis. For supervision diversity, we introduce Label Pruning with Dynamic Knowledge Reuse to improve label-per-augmentation diversity, and Label Quantization with Calibrated Student-Teacher Alignment to improve augmentation-per-image diversity. Our approach reduces soft label storage by 78x on ImageNet-1K and 500x on ImageNet-21K while improving accuracy by up to 7.2% and 2.8%, respectively. Extensive experiments validate the superiority of LPQLD across different network architectures and dataset distillation methods. Code is available at this https URL.

---


### 433. [Region-Grounded Report Generation for 3D Medical Imaging: A Fine-Grained Dataset and Graph-Enhanced Framework](https://arxiv.org/abs/2604.18145)

**<font color=#1a73e8>作者：</font>** Cong Huy Nguyen, Son Dinh Nguyen, Guanlin Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated medical report generation for 3D PET/CT imaging is fundamentally challenged by the high-dimensional nature of volumetric data and a critical scarcity of annotated datasets, particularly for low-resource languages. Current black-box methods map whole volumes to reports, ignoring the clinical workflow of analyzing localized Regions of Interest (RoIs) to derive diagnostic conclusions. In this paper, we bridge this gap by introducing VietPET-RoI, the first large-scale 3D PET/CT dataset with fine-grained RoI annotation for a low-resource language, comprising 600 PET/CT samples and 1,960 manually annotated RoIs, paired with corresponding clinical reports. Furthermore, to demonstrate the utility of this dataset, we propose HiRRA, a novel framework that mimics the professional radiologist diagnostic workflow by employing graph-based relational modules to capture dependencies between RoI attributes. This approach shifts from global pattern matching toward localized clinical findings. Additionally, we introduce new clinical evaluation metrics, namely RoI Coverage and RoI Quality Index, that measure both RoI localization accuracy and attribute description fidelity using LLM-based extraction. Extensive evaluation demonstrates that our framework achieves SOTA performance, surpassing existing models by 19.7% in BLEU and 4.7% in ROUGE-L, while achieving a remarkable 45.8% improvement in clinical metrics, indicating enhanced clinical reliability and reduced hallucination. Our code and dataset are available on GitHub.

---


### 434. [Attention-ResUNet for Automated Fetal Head Segmentation](https://arxiv.org/abs/2604.18148)

**<font color=#1a73e8>作者：</font>** Ammar Bhilwarawala, Mainak Bandyopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated fetal head segmentation in ultrasound images is critical for accurate biometric measurements in prenatal care. While existing deep learning approaches have achieved a reasonable performance, they struggle with issues like low contrast, noise, and complex anatomical boundaries which are inherent to ultrasound imaging. This paper presents Attention-ResUNet. It is a novel architecture that synergistically combines residual learning with multi-scale attention mechanisms in order to achieve enhanced fetal head segmentation. Our approach integrates attention gates at four decoder levels to focus selectively on anatomically relevant regions while suppressing the background noise, and complemented by residual connections which facilitates gradient flow and feature reuse. Extensive evaluation on the HC18 Challenge dataset where n = 200 demonstrates that Attention ResUNet achieves a superior performance with a mean Dice score of 99.30 +/- 0.14% against similar architectures. It significantly outperforms five baseline architectures including ResUNet (99.26%), Attention U-Net (98.79%), Swin U-Net (98.60%), Standard U-Net (98.58%), and U-Net++ (97.46%). Through statistical analysis we confirm highly significant improvements (p < 0.001) with effect sizes that range from 0.230 to 13.159 (Cohen's d). Using Saliency map analysis, we reveal that our architecture produces highly concentrated, anatomically consistent activation patterns, which demonstrate an enhanced interpretability which is crucial for clinical deployment. The proposed method establishes a new state of the art performance for automated fetal head segmentation whilst maintaining computational efficiency with 14.7M parameters and a 45 GFLOPs inference cost. Code repository: this https URL

---


### 435. [AI-based Waste Mapping for Addressing Climate-Exacerbated Flood Risk](https://arxiv.org/abs/2604.18151)

**<font color=#1a73e8>作者：</font>** Steffen Knoblauch, Levi Szamek, Iddy Chazua 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban flooding is a growing climate change-related hazard in rapidly expanding African cities, where inadequate waste management often blocks drainage systems and amplifies flood risks. This study introduces an AI-powered urban waste mapping workflow that leverages openly available aerial and street-view imagery to detect municipal solid waste at high resolution. Applied in Dar es Salaam, Tanzania, our approach reveals spatial waste patterns linked to informal settlements and socio-economic factors. Waste accumulation in waterways was found to be up to three times higher than in adjacent urban areas, highlighting critical hotspots for climate-exacerbated flooding. Unlike traditional manual mapping methods, this scalable AI approach allows city-wide monitoring and prioritization of interventions. Crucially, our collaboration with local partners ensured culturally and contextually relevant data labeling, reflecting real-world reuse practices for solid waste. The results offer actionable insights for urban planning, climate adaptation, and sustainable waste management in flood-prone urban areas.

---


### 436. [State Transfer Reveals Reuse in Controlled Routing](https://arxiv.org/abs/2604.18158)

**<font color=#1a73e8>作者：</font>** Yanzhen Lu, Zhicheng Qian, Muchen Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt-based interventions can change model behavior, but trained success alone does not identify where the behaviorally relevant state is represented. We study this question in controlled routing tasks using interfaces chosen on support data, held-out query evaluation, and matched necessity, sufficiency, and wrong-interface controls. On GPT-2 triop, an early interface supports exact transfer under these tests. On GPT-2 add/sub, zero-retrain compiled transfer at the fixed interface recovers most of donor routing accuracy, while trainable prompt slots can relearn the same behavior at several other positions only after additional support examples and optimization. These results distinguish fixed-interface reuse from prompt relocation in a setting where the two can be tested directly. Qwen routing provides a cross-architecture consistency check for the same matched-interface pattern at the operator token, although donor-specific identity on the local V-path remains unresolved. Generation and reasoning branches are used to map scope: they show broader transport or weaker controller identifiability once control depends on longer trajectories or harder selection. In controlled routing, fixed-interface transfer is therefore stronger evidence of reuse than trained prompt success alone.

---


### 437. [Does "Do Differentiable Simulators Give Better Policy Gradients?'' Give Better Policy Gradients?](https://arxiv.org/abs/2604.18161)

**<font color=#1a73e8>作者：</font>** Ku Onoda, Paavo Parmas, Manato Yaguchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In policy gradient reinforcement learning, access to a differentiable model enables 1st-order gradient estimation that accelerates learning compared to relying solely on derivative-free 0th-order estimators. However, discontinuous dynamics cause bias and undermine the effectiveness of 1st-order estimators. Prior work addressed this bias by constructing a confidence interval around the REINFORCE 0th-order gradient estimator and using these bounds to detect discontinuities. However, the REINFORCE estimator is notoriously noisy, and we find that this method requires task-specific hyperparameter tuning and has low sample efficiency. This paper asks whether such bias is the primary obstacle and what minimal fixes suffice. First, we re-examine standard discontinuous settings from prior work and introduce DDCG, a lightweight test that switches estimators in nonsmooth regions; with a single hyperparameter, DDCG achieves robust performance and remains reliable with small samples. Second, on differentiable robotics control tasks, we present IVW-H, a per-step inverse-variance implementation that stabilizes variance without explicit discontinuity detection and yields strong results. Together, these findings indicate that while estimator switching improves robustness in controlled studies, careful variance control often dominates in practical deployments.

---


### 438. [Audit-or-Cast: Enforcing Honest Elections with Privacy-Preserving Public Verification](https://arxiv.org/abs/2604.18163)

**<font color=#1a73e8>作者：</font>** Aman Rojjha, Gaurang Tandon, Varul Srivastava 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electronic voting systems must balance public verifiability with voter privacy and coercion resistance. Existing cryptographic protocols typically achieve end-to-end verifiability by revealing vote distributions, relying on trusted clients, or enabling transferable receipts - design choices that often compromise trust or privacy in real-world deployments.
We present ACE, a voting protocol that reconciles public auditability with strong privacy guarantees. The protocol combines a publicly verifiable, tally-hiding aggregation mechanism with an Audit-or-Cast challenge that enforces cast-as-intended even under untrusted client assumptions. Tallier-side re-randomization eliminates persistent links between voters and public records, yielding information-theoretic receipt-freeness assuming at least one honest tallier.
We formalize the security of ACE and show that it simultaneously achieves end-to-end verifiability, publicly tally-hiding results, and strong receipt-freeness without trusted clients.

---


### 439. [Embedding Arithmetic: A Lightweight, Tuning-Free Framework for Post-hoc Bias Mitigation in Text-to-Image Models](https://arxiv.org/abs/2604.18167)

**<font color=#1a73e8>作者：</font>** Venkatesh Thirugnana Sambandham, Torsten Schön  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image (T2I) models amplify harmful societal biases, challenging their ethical deployment. We introduce an inference-time method that reliably mitigates social bias while keeping prompt semantics and visual context (background, layout, and style) intact. This ensures context persistency and provides a controllable parameter to adjust mitigation strength, giving practitioners fine-grained control over fairness-coherence trade-offs. Using Embedding Arithmetic, we analyze how bias is structured in the embedding space and correct it without altering model weights, prompts, or datasets. Experiments on FLUX 1.0-Dev and Stable Diffusion 3.5-Large show that the conditional embedding space forms a complex, entangled manifold rather than a grid of disentangled concepts. To rigorously assess semantic preservation beyond the circularity and bias limitations of of CLIP scores, we propose the Concept Coherence Score (CCS). Evaluated against this robust metric, our lightweight, tuning-free method significantly outperforms existing baselines in improving diversity while maintaining high concept coherence, effectively resolving the critical fairness-coherence trade-off. By characterizing how models represent social concepts, we establish geometric understanding of latent space as a principled path toward more transparent, controllable, and fair image generation.

---


### 440. [Extending One-Step Image Generation from Class Labels to Text via Discriminative Text Representation](https://arxiv.org/abs/2604.18168)

**<font color=#1a73e8>作者：</font>** Chenxi Zhao, Chen Zhu, Xiaokun Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step generation has been a long-standing goal, with recent one-step generation methods exemplified by MeanFlow achieving remarkable results. Existing research on MeanFlow primarily focuses on class-to-image generation. However, an intuitive yet unexplored direction is to extend the condition from fixed class labels to flexible text inputs, enabling richer content creation. Compared to the limited class labels, text conditions pose greater challenges to the model's understanding capability, necessitating the effective integration of powerful text encoders into the MeanFlow framework. Surprisingly, although incorporating text conditions appears straightforward, we find that integrating powerful LLM-based text encoders using conventional training strategies results in unsatisfactory performance. To uncover the underlying cause, we conduct detailed analyses and reveal that, due to the extremely limited number of refinement steps in the MeanFlow generation, such as only one step, the text feature representations are required to possess sufficiently high discriminability. This also explains why discrete and easily distinguishable class features perform well within the MeanFlow framework. Guided by these insights, we leverage a powerful LLM-based text encoder validated to possess the required semantic properties and adapt the MeanFlow generation process to this framework, resulting in efficient text-conditioned synthesis for the first time. Furthermore, we validate our approach on the widely used diffusion model, demonstrating significant generation performance improvements. We hope this work provides a general and practical reference for future research on text-conditioned MeanFlow generation. The code is available at this https URL.

---


### 441. [Alleviating Linguistic and Interactional Anxiety of Non-Native Speakers in Multilingual Communication](https://arxiv.org/abs/2604.18171)

**<font color=#1a73e8>作者：</font>** Peinuan Qin, Justin Peng, Zhengtao Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Non-native speakers (NNSs) frequently encounter speaking difficulties in multilingual communication, where existing approaches have shown promise in facilitating NNSs' comprehension and participation in real-time communication. However, they often overlook providing direct speaking support, where anxiety stemming from linguistic inadequacy and uncertain communication dynamics are core issues. To address this, we introduce an AI tool with translation for real-time speaking support. It also builds a channel for mutual understanding with native speakers (NSs) to mitigate interactional anxiety. Through a within-subjects experiment involving 25 NNS-NS pairs (N = 50) on collaborative tasks, our findings suggest that the tool improved NNSs' speaking self-efficacy, reduced their interactional anxiety, and decreased their workload, particularly for NNSs with below-average language proficiency. Furthermore, NNSs reported a significant sense of support from their NS partners via the mutual understanding channel, and NSs also clearly perceived the NNSs' need for assistance and displayed a strong sense of communicative responsibility. This research underscores the potential of AI support in real-time NNS communication and the importance of promoting mutual understanding, culminating in actionable design insights for future work.

---


### 442. [CanonSLR: Canonical-View Guided Multi-View Continuous Sign Language Recognition](https://arxiv.org/abs/2604.18184)

**<font color=#1a73e8>作者：</font>** Xu Wang, Shengeng Tang, Wan Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous Sign Language Recognition (CSLR) has achieved remarkable progress in recent years; however, most existing methods are developed under single-view settings and thus remain insufficiently robust to viewpoint variations in real-world scenarios. To address this limitation, we propose CanonSLR, a canonical-view guided framework for multi-view CSLR. Specifically, we introduce a frontal-view-anchored teacher-student learning strategy, in which a teacher network trained on frontal-view data provides canonical temporal supervision for a student network trained on all viewpoints. To further reduce cross-view semantic discrepancy, we propose Sequence-Level Soft-Target Distillation, which transfers structured temporal knowledge from the frontal view to non-frontal samples, thereby alleviating gloss boundary ambiguity and category confusion caused by occlusion and projection variation. In addition, we introduce Temporal Motion Relational Enhancement to explicitly model motion-aware temporal relations in high-level visual features, strengthening stable dynamic representations while suppressing viewpoint-sensitive appearance disturbances. To support multi-view CSLR research, we further develop a universal multi-view sign language data construction pipeline that transforms original single-view RGB videos into semantically consistent, temporally coherent, and viewpoint-controllable multi-view sign language videos. Based on this pipeline, we extend PHOENIX-2014T and CSL-Daily into two seven-view benchmarks, namely PT14-MV and CSL-MV, providing a new experimental foundation for multi-view CSLR. Extensive experiments on PT14-MV and CSL-MV demonstrate that CanonSLR consistently outperforms existing approaches under multi-view settings and exhibits stronger robustness, especially on challenging non-frontal views.

---


### 443. [Scalable Neighborhood-Based Multi-Agent Actor-Critic](https://arxiv.org/abs/2604.18190)

**<font color=#1a73e8>作者：</font>** Tim Goppelsroeder, Rasmus Jensen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose MADDPG-K, a scalable extension to Multi-Agent Deep Deterministic Policy Gradient (MADDPG) that addresses the computational limitations of centralized critic approaches. Centralized critics, which condition on the observations and actions of all agents, have demonstrated significant performance gains in cooperative and competitive multi-agent settings. However, their critic networks grow linearly in input size with the number of agents, making them increasingly expensive to train at scale. MADDPG-K mitigates this by restricting each agent's critic to the $k$ closest agents under a chosen metric which in our case is Euclidean distance. This ensures a constant-size critic input regardless of the total agent count. We analyze the complexity of this approach, showing that the quadratic cost it retains arises from cheap scalar distance computations rather than the expensive neural network matrix multiplications that bottleneck standard MADDPG. We validate our method empirically across cooperative and adversarial environments from the Multi-Particle Environment suite, demonstrating competitive or superior performance compared to MADDPG, faster convergence in cooperative settings, and better runtime scaling as the number of agents grows. Our code is available at this https URL .

---


### 444. [How Do People Accept Robot in Public Space? A Cross-Cultural Study in Germany and Japan](https://arxiv.org/abs/2604.18193)

**<font color=#1a73e8>作者：</font>** Zhe Zeng, Clara Ayumi Fechner, Fei Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the increasing deployment of robots in public spaces, encounters between robots and incidentally copresent persons (InCoPs) are becoming more frequent. However, InCoPs remain largely underexplored in the literature, particularly from a cross-cultural perspective. Therefore, the present study investigates cultural differences in InCoPs' existence acceptance (EA) of autonomous cleaning robots in public spaces among Japanese and German participants. Online survey results revealed that Germans showed significantly higher EA. Social Norms and Trust were the strongest positive EA predictors across cultures. More specifically, for Germans, EA was directly influenced by Usefulness, Interest and Anger, showing a functional-affective pattern where functional perceptions boost EA and anger suppresses it. For Japanese participants, Trust, Surprise and Fear were the direct associational factors, forming a trust-emotion pattern. These findings reveal cultural influences on cognitive and emotional drivers of public robot acceptance, emphasizing the need for culturally adaptive robot design.

---


### 445. [Attraction, Repulsion, and Friction: Introducing DMF, a Friction-Augmented Drifting Model](https://arxiv.org/abs/2604.18194)

**<font color=#1a73e8>作者：</font>** Arkadii Kazanskii, Tatiana Petrova, Konstantin Bagrianskii 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drifting Models [Deng et al., 2026] train a one-step generator by evolving samples under a kernel-based drift field, avoiding ODE integration at inference. The original analysis leaves two questions open. The drift-field iteration admits a locally repulsive regime in a two-particle surrogate, and vanishing of the drift ($V_{p,q}\equiv 0$) is not known to force the learned distribution $q$ to match the target $p$. We derive a contraction threshold for the surrogate and show that a linearly-scheduled friction coefficient gives a finite-horizon bound on the error trajectory. Under a Gaussian kernel we prove that the drift-field equilibrium is identifiable: vanishing of $V_{p,q}$ on any open set forces $q=p$, closing the converse of Proposition 3.1 of Deng et al. Our friction-augmented model, DMF (Drifting Model with Friction), matches or exceeds Optimal Flow Matching on FFHQ adult-to-child domain translation at 16x lower training compute.

---


### 446. [Continuous Focus Groups: A Longitudinal Method for Clinical HRI in Autism Care](https://arxiv.org/abs/2604.18197)

**<font color=#1a73e8>作者：</font>** Ghiglino Davide, Foglino Caterina, Wykowska Agnieszka  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Qualitative methods are important to use alongside quantitative methods to improve Human-Robot Interaction (HRI), yet they are often applied in static or one-off formats that cannot capture how stakeholder perspectives evolve over time. This limitation is especially evident in clinical contexts, where families and patients face heavy burdens and cannot easily participate in repeated research encounters. To address this gap, we introduce continuous focus groups, a longitudinal and co-agential method designed to sustain dialogue with assistive care professionals working with children with autism spectrum disorder (ASD). Three focus groups were organized across successive phases of a robot-assisted therapeutic protocol, enabling participants to revisit and refine earlier views as the intervention progressed. Results show that continuity fostered trust, supported the integration of tacit clinical expertise into design decisions, and functioned as an ethical safeguard by allowing participants to renegotiate involvement and surface new concerns. By bridging the therapeutic iteration of families, children, and clinicians with the research-design iteration of researchers and developers, continuous focus groups provide a methodological contribution that is both feasible in practice and rigorous in design. Beyond autism care, this approach offers a transferable framework for advancing qualitative research in HRI, particularly in sensitive domains where direct user participation is limited and continuity is essential.

---


### 447. [DiffuSAM: Diffusion Guided Zero-Shot Object Grounding for Remote Sensing Imagery](https://arxiv.org/abs/2604.18201)

**<font color=#1a73e8>作者：</font>** Geet Sethi, Panav Shah, Ashutosh Gandhe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have emerged as powerful tools for a wide range of vision tasks, including text-guided image generation and editing. In this work, we explore their potential for object grounding in remote sensing imagery. We propose a hybrid pipeline that integrates diffusion-based localization cues with state-of-the-art segmentation models such as RemoteSAM and SAM3 to obtain more accurate bounding boxes. By leveraging the complementary strengths of generative diffusion models and foundational segmentation models, our approach enables robust and adaptive object localization across complex scenes. Experiments demonstrate that our pipeline significantly improves localization performance, achieving over a 14% increase in Acc@0.5 compared to existing state-of-the-art methods.

---


### 448. [Hard to Be Heard: Phoneme-Level ASR Analysis of Phonologically Complex, Low-Resource Endangered Languages](https://arxiv.org/abs/2604.18204)

**<font color=#1a73e8>作者：</font>** V.S.D.S.Mahesh Akavarapu, Michael Daniel, Gerhard Jäger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a phoneme-level analysis of automatic speech recognition (ASR) for two low-resourced and phonologically complex East Caucasian languages, Archi and Rutul, based on curated and standardized speech-transcript resources totaling approximately 50 minutes and 1 hour 20 minutes of audio, respectively. Existing recordings and transcriptions are consolidated and processed into a form suitable for ASR training and evaluation. We evaluate several state-of-the-art audio and audio-language models, including wav2vec2, Whisper, and Qwen2-Audio. For wav2vec2, we introduce a language-specific phoneme vocabulary with heuristic output-layer initialization, which yields consistent improvements and achieves performance comparable to or exceeding Whisper in these extremely low-resource settings. Beyond standard word and character error rates, we conduct a detailed phoneme-level error analysis. We find that phoneme recognition accuracy strongly correlates with training frequency, exhibiting a characteristic sigmoid-shaped learning curve. For Archi, this relationship partially breaks for Whisper, pointing to model-specific generalization effects beyond what is predicted by training frequency. Overall, our results indicate that many errors attributed to phonological complexity are better explained by data scarcity. These findings demonstrate the value of phoneme-level evaluation for understanding ASR behavior in low-resource, typologically complex languages.

---


### 449. [A Comparative Evaluation of Geometric Accuracy in NeRF and Gaussian Splatting](https://arxiv.org/abs/2604.18205)

**<font color=#1a73e8>作者：</font>** Mikolaj Zielinski, Eryk Vykysaly, Bartlomiej Biesiada 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in neural rendering have introduced numerous 3D scene representations. Although standard computer vision metrics evaluate the visual quality of generated images, they often overlook the fidelity of surface geometry. This limitation is particularly critical in robotics, where accurate geometry is essential for tasks such as grasping and object manipulation. In this paper, we present an evaluation pipeline for neural rendering methods that focuses on geometric accuracy, along with a benchmark comprising 19 diverse scenes. Our approach enables a systematic assessment of reconstruction methods in terms of surface and shape fidelity, complementing traditional visual metrics.

---


### 450. [A Control Architecture for Training-Free Memory Use](https://arxiv.org/abs/2604.18206)

**<font color=#1a73e8>作者：</font>** Yanzhen Lu, Muchen Jiang, Zhicheng Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt-injected memory can improve reasoning without updating model weights, but it also creates a control problem: retrieved content helps only when it is applied in the right state. We study this problem in a strict training-free setting and formulate it as applicability control: when to trigger a memory-assisted second pass, when to trust it, and how to maintain the memory bank over time. Our method combines uncertainty-based routing, confidence-based selective acceptance, bank selection across rule and exemplar memory, and evidence-based governance of the memory bank over time. Under a locked training-free protocol with compute-matched controls, it improves two core arithmetic benchmarks by +7.0 points on SVAMP and +7.67 points on ASDiv over baseline. The same architecture also transfers to QA and agent benchmarks with smaller positive effects and shows the same positive direction on a second checkpoint for the main arithmetic tasks. On arithmetic, the main empirical pattern is that the control architecture, rather than raw memory exposure, drives the improvements on SVAMP and ASDiv. Mechanistically, confidence separates helpful from harmful rule-bank interventions, and under fixed retrieval the repair-versus-corrupt difference localizes to rows whose retrieved set actually contains the edited entries.

---


> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-535](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
