# 📦 其他研究 | 2026年09月16日

> 本类共 **416** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-416](./part-09.md)

---

### 51. [HGSQ: Heatmap-Guided Sparse Query Detector for Real-Time Aerial Small Object Detection](https://arxiv.org/abs/2609.13306)

**<font color=#1a73e8>作者：</font>** Yangchen Zeng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time aerial small object detection is an important visual signal and image processing problem, requiring a detector to preserve fine-grained localization while avoiding redundant computation on large background regions. This paper focuses on this deployment-oriented aerial/UAV setting rather than claiming a universal detector for all object detection scenarios. Existing Transformer-based detectors provide strong global modeling, but their dense query initialization and multi-layer decoder still spend substantial computation on background tokens, which is inefficient when small objects occupy only sparse image regions. To address this problem, this paper proposes HGSQ, a Heatmap-Guided Sparse Query Detector for real-time aerial small object detection. HGSQ uses a lightweight Heatmap Budget Predictor (HBP) to predict a foreground budget map in a single forward pass. The predicted heatmap is then used by three fixed components: Heatmap-Guided Sparse Query Selection (HSQS), which initializes decoder queries from high-confidence foreground positions; Heatmap-Gated Lite Snake Convolution (HGLSConv), which performs local shape refinement only on heatmap-activated small-object regions; and Adaptive Query-Decoder Budgeting (AQDB), which adjusts the query budget and decoder depth according to the estimated object density. Unlike post-hoc heatmap generation, HGSQ treats the heatmap as a real-time computation budget rather than a visualization map during deployment. Experiments on NWPU VHR-10 and VisDrone2019 show that HGSQ achieves 95.10 mAP50 on NWPU VHR-10 and 54.8 mAP50 on VisDrone2019, while reducing GFLOPs to 48.6 and running at 96.0 FPS on an RTX 4070 under our TensorRT FP16 deployment protocol.

---


### 52. [Task-Based CT Protocol Optimization Using Reinforcement Learning and Virtual Imaging Trials](https://arxiv.org/abs/2609.13309)

**<font color=#1a73e8>作者：</font>** Jiaqi Zou, David Fenwick, Vahid Tarokh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Protocol optimization in computed tomography (CT) aims to improve diagnostic image quality while reducing radiation dose, but the interdependence of acquisition and reconstruction parameters makes exhaustive testing impractical. We propose a virtual imaging trial framework with reinforcement learning for efficient CT protocol optimization. Sixty-three computational human models with liver lesions were imaged using a validated CT simulator across 468 combinations of acquisition and reconstruction parameters, including tube voltage, tube current, reconstruction kernel, slice thickness, and pixel size. The optimization objective balanced liver lesion detectability, quantified by detectability index d-prime, against radiation dose. A Proximal Policy Optimization agent was trained and conditioned on patient-specific CT localizer embeddings derived from a pretrained vision transformer. On held-out patients, evaluating only 8 protocols per patient, about 2% of exhaustive testing, recovered 98.2% of the exhaustive-search oracle objective. With no patient-specific simulation, surrogate scoring alone achieved 89.7% recovery. Conditioning on the localizer improved zero-simulation recovery by 10.7 percentage points over the localizer-blind policy (paired 95% CI 2.9-19.5; p=0.02). These results show that the proposed framework can substantially reduce exhaustive protocol testing while enabling task-based, dose-aware protocol selection before the diagnostic scan.

---


### 53. [Pedestrian Crossing Intent Classification From Event-Based Vision Using Convolutional Spiking Neural Networks With Temporal Augmentation](https://arxiv.org/abs/2609.13328)

**<font color=#1a73e8>作者：</font>** Henok Teklu, Mustafa Sakhai, Maciej Wielgosz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anticipating whether a pedestrian will cross the road is safety-critical for autonomous vehicles, requiring real-time inference under challenging conditions including motion blur, high dynamic range, and class imbalance. Conventional frame-based deep networks process redundant RGB data at fixed frame rates, limiting their temporal resolution and energy efficiency. In this work we present an end-to-end pipeline that (i) converts real-world driving footage from the Joint Attention in Autonomous Driving (JAAD) dataset into synthetic dynamic vision sensor (DVS) event streams using the v2e simulator, (ii) augments training with the CARLA-simulated DVS sequences of the DVS-PedX dataset under both normal and adverse weather conditions, and (iii) trains a novel convolutional spiking neural network (Conv-SNN) with clip-consistent DVS augmentation to classify pedestrian crossing intent as binary: crossing or non-crossing. We detail all architectural decisions, the exact leaky-integrate-and-fire neuron dynamics with surrogate-gradient learning, the class-balanced loss formulation, JAAD oversampling at 6x, and a 70/15/15 stratified splitting protocol. The trained model achieves 95.83% accuracy and F1 = 0.9695 on the JAAD DVS test set, 97.79% accuracy and F1 = 0.9478 on normal CARLA DVS, and 94.78% accuracy and F1 = 0.8369 on adverse-weather CARLA DVS, all from a 1.07M-parameter architecture trained on CPU. Compared to prior frame-based approaches on JAAD, our method closes or surpasses the reported accuracy while operating natively on sparse temporal representations. We include a thorough analysis of the convergence behaviour across all 15 training epochs, domain transfer characteristics, and a quantitative comparison with representative related work.

---


### 54. [Global-Local Contextual Progressive Expansion Network for Martian Landslide Segmentation in Multimodal Remote Sensing Imagery](https://arxiv.org/abs/2609.13332)

**<font color=#1a73e8>作者：</font>** Leo Thomas Ramos, Sidike Paheding, Abel A. Reyes-Angulo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated landslide segmentation on Mars is one of the important tasks for understanding its surface processes, and all will aid in future space exploration. However, it remains a relatively underexplored open challenge because landslide morphology is highly variable, foreground regions are often sparse or irregular, and orbital observations combine heterogeneous spectral and topographic cues. In this context, this work investigates the capability of deep learning to address Martian landslide segmentation through an extensive assessment of modern neural segmentation models. To the best of our knowledge, this is the first study to provide such a comprehensive exploration in this domain. We further propose TransCPLES, a U-shaped network that couples Contextual Progressive Layer Expansion feature extraction with Transformer-based contextual reasoning, enabling the model to capture local geomorphic patterns and broader spatial dependencies for more reliable landslide delineation. Experiments on MMLSv2, a seven-band multimodal Martian landslide dataset, show that TransCPLES achieves the best overall performance when evaluated on geographically distinct samples, with consistent delineation across different landslide extents, stable foreground discrimination, and a favorable balance between accuracy and computational cost compared with several state-of-the-art convolutional, attention-based, and Transformer-based segmentation models. With this work, we hope to provide a useful reference and encourage further research and development in deep learning for planetary remote sensing. Code will be available after publication.

---


### 55. [ProtoCAM: Interpretable Few-Shot Mask-Guided Prototypical Learning for Breast Lesion Classification in Ultrasound Imaging](https://arxiv.org/abs/2609.13340)

**<font color=#1a73e8>作者：</font>** Ashkan Ebadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast ultrasound imaging plays an important role in the early detection and diagnosis of breast cancer, particularly for patients with dense breast tissue. However, developing reliable deep learning models for ultrasound analysis is challenging due to limited annotated medical data and the need for interpretable predictions. To address these challenges, this paper proposes ProtoCAM, an explainable few-shot learning framework for breast lesion classification that integrates mask-guided feature encoding, prototypical metric learning, and gradient-based visual explanations. The proposed approach leverages lesion masks to guide feature extraction and constructs class prototypes within an embedding space to enable robust classification under limited training samples. The framework was evaluated on the BUSI dataset using a stratified group k-fold cross-validation protocol to prevent patient-level data leakage. Experimental results demonstrate ProtoCAM's high performance in low-data scenarios. In a 3-way 5-shot setting, the proposed method achieves a macro F1-score of 0.910, representing a substantial improvement over standard supervised CNN models. Among the evaluated backbone networks, ResNet18 achieved the best performance, reaching a macro F1-score of 91.65% under a 15-shot configuration, providing interpretable insights into the classification decisions. These results highlight the potential of explainable few-shot learning frameworks for reliable computer-aided breast cancer diagnosis in data-scarce medical imaging environments.

---


### 56. [Real-time Learning and Evolution in Robotic Art Installations](https://arxiv.org/abs/2609.13352)

**<font color=#1a73e8>作者：</font>** Sofian Audry, Stephen Kelly  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present three robotic art installations which explore the aesthetics of adaptive behavior. Through embodied machine leaning and digital evolution, these works draw viewers into an artificial ecosystem in which open-ended novelty, trial-and-error learning, competition, and cooperation emerge in real time. Research-creation practices are examined in relation to these works, focusing on how they redefine the role of artists within a human-machine collective while examining points of convergence and divergence between artistic and engineering approaches to adaptive robotics. The systems in question use learning and evolutionary processes not as a means to optimize a specific solution, but as an aesthetic experience on its own, suggesting new modes of interdisciplinary art-science research. Finally, we discuss strategies and practices to elevate the aesthetic experience for audiences, including contexts of presentation as well as temporal and material considerations for artworks based on embodied adaptive systems.

---


### 57. [Converge Then Diversify: Decoupling Convergence and Diversity in Multi-Objective Bayesian Optimisation](https://arxiv.org/abs/2609.13396)

**<font color=#1a73e8>作者：</font>** Chao Jiang, Yueling Huang, Miqing Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-objective Bayesian optimisation (MOBO) is a sample-efficient approach for optimising expensive black-box functions with multiple objectives. In MOBO, the goal is to adequately approximate the Pareto front; that is, to obtain a high-quality solution set with 1) good convergence (closeness to the Pareto front) and 2) good diversity (spread across the Pareto front). Existing MOBO methods typically aim to accomplish these two tasks simultaneously, i.e., driving the search towards the Pareto front while maintaining a diverse set of nondominated solutions, such that the solutions, ideally, can gradually approach the entire front. When sufficient search budgets are available, this approach is effective. However, considering both convergence and diversity throughout the search is not easy and requires careful design. Under very tight budgets, there may not be enough solutions generated to be able to simultaneously approach the entire Pareto front. To address this issue, this paper proposes a \textit{converge-then-diversify} (CTD) approach that decouples convergence and diversity into two stages. In the first stage, CTD focuses on convergence, aiming to quickly drive the search toward a single point on the Pareto front. In the second stage, CTD focuses on diversity, aiming to spread solutions across the front. We present two simple instantiations of CTD by using widely adopted acquisition functions in the area. Experimental results show that, across all 446 pairwise comparisons, CTD statistically outperforms state-of-the-art methods in 72.9\% of the cases, performs equivalently in 21.1\%, and is statistically worse in only 6.1\%, with the advantage being particularly evident in settings with very tight evaluation budgets or in high-dimensional problems.

---


### 58. [ConeGaussian: Anti-Aliased Gaussian Ray-Tracing for Generic Central Cameras](https://arxiv.org/abs/2609.13397)

**<font color=#1a73e8>作者：</font>** Deheng Zhang, Letian Shi, Runyi Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In rendering, a camera is a sampling operator that maps each finite pixel to a bundle of rays. Different camera models change the geometry of this bundle, thus making a unified and faithful rendering formulation challenging. Consequently, Gaussian ray tracing supports generic cameras (with optical center) through their inverse ray mappings, yet typically reduces every pixel to a single center ray. This ignores the camera-dependent pixel footprint, causing aliasing under minification, while unconstrained Gaussians expose unsupported frequencies under magnification. We present ConeGaussian, a camera-model-agnostic anti-aliasing framework for Gaussian ray-based rendering. Instead of defining the pixel filter on a camera-specific image plane, ConeGaussian constructs an anisotropic footprint directly from neighboring rays produced by the camera's native inverse mapping. We derive a closed-form response under a locally linear, depth-local, moment-matched approximation of the finite pixel footprint, while the same geometry defines a per-Gaussian training-frequency floor. Notably, by construction, our filtering principle can be used unmodified across calibrated central camera models and multiple Gaussian ray-rendering backbones. Additionally, unlike in mip-splatting, our scene-space frequency floor and filtering enable trivial composition at render time, allowing us to remove excess blurring. On pinhole and strongly distorted fisheye captures, ConeGaussian consistently improves two distinct ray-based backbones, by up to 4.3 dB at 1/8 resolution, and reduces fisheye LPIPS by 30% where perspective screen-plane footprint formulations are not directly applicable.

---


### 59. [Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement](https://arxiv.org/abs/2609.13406)

**<font color=#1a73e8>作者：</font>** Hongyao Tang, Yi Ma, Pengyi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When we speak of recursive self-improvement (RSI), are we speaking of a phenomenon, a mechanism, or a prospect? Towards autonomous and evolving intelligence, RSI is being claimed at many scales, while no single framework that formally describes these emerging instances exists. Its counterpart in the classical realm, iterative policy improvement, is characterized by generalized policy iteration (GPI), a framework of broad applicability with well-understood theoretical properties, but only where the update principle and the evaluation base lie outside the agent. In this paper, we propose Generalized Agent Iteration (GAI), a formal framework that describes iterative policy improvement and RSI as two cases of a single learning paradigm. GAI defines the agent as a configuration of modifiable components within a system and models the learning process as a cycle of agent evaluation and agent improvement. Two pivotal dials then distinguish the instances: whether the improving mechanism is part of the agent and whether the standard it is measured against is grounded outside it. The former dial delineates the boundary between GPI and RSI, and the latter determines a system's polarity as anchored, goal drift, or fully self-referential. Moreover, we use these coordinates to place existing systems on the same two axes and make the defects of recursive self-improvement statable one condition at a time. We see this paper as a first step toward exploring a formal characterization of RSI that rests on the classical account, makes existing systems comparable, and provides a principled basis for analyzing and designing new ones.

---


### 60. [Principled Detection of Coordinated Manipulation from Aggregate Distortion and Account Reuse](https://arxiv.org/abs/2609.13407)

**<font color=#1a73e8>作者：</font>** Qian Guo, Yidan Hu, Rui Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coordinated manipulation is collective: plausible accounts can jointly distort ratings, rankings, and engagement. Existing defenses primarily construct evidence from identities, graphs, content, or co-activity. We introduce an aggregate-first evidence layer that treats distortion of a context-level outcome distribution as the primary evidence object. The engine observes only a histogram, count, resolution, and reference distribution; identities are withheld until interval evidence is fixed. Because raw discrepancies have positive finite-sample expectation, we subtract a matched null expectation to obtain signed evidence and account for reference uncertainty. Participation logs then accumulate these fixed increments across accounts. We characterize matched-exposure divergence, bound self-influence, establish finite-horizon separation, and derive an exact linear reuse law for paired contexts.
We evaluate the mechanism with controlled rotation experiments and paired counterfactual interventions on historical Amazon review streams. Historical reviews provide the behavioral background; synthetic identities provide known coalition membership, and exact clean twins provide counterfactual controls. In a fixed-attack sweep against historical non-donor comparison accounts, reassigning the same manipulated events across identities with increasing reuse raises account-score ROC-AUC from 0.500 to 0.797. With activity- and exposure-matched clean twins, frequency is at chance while counterfactual attribution achieves ROC-AUC 0.744. Under a mean-preserving shape intervention, Wasserstein-1 and Jensen-Shannon evidence achieve ROC-AUC 0.909 and 0.967, while frequency and mean-based attribution remain at chance. Aggregate evidence complements repeated co-activity, improving mixed-mechanism ROC-AUC from 0.750 to 0.874 with a simple untrained combination.

---


### 61. [CVSS-X: A Multilingual Speech-to-Speech Translation Corpus for 28 Languages](https://arxiv.org/abs/2609.13413)

**<font color=#1a73e8>作者：</font>** Lucas Rafael Stefanel Gris, Alef Iury Siqueira Ferreira, Frederico Santos de Oliveira 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce CVSS-X, a large-scale synthetic speech-to-speech translation corpus that extends CVSS by reversing the translation direction. While CVSS translates from 21 languages into English, CVSS-X enables translation from English into 28 target languages spanning 12 language families. The corpus comprises approximately 240,000 parallel speech pairs per language, totaling over 16,000 hours, eight times larger than CVSS. We provide two variants: CVSS-X-C with two canonical voices per language, and CVSS-X-T with cross-lingual voice cloning, both fully generated. Evaluation shows comparable translation quality to CVSS with consistent performance across typologically diverse languages. Combined with CVSS, this enables research on bidirectional and multilingual speech-to-speech translation. The code is available at this https URL and the dataset under CC-BY-NC 4.0 license at this https URL.

---


### 62. [LabAgent: Customize Any Research Hubs for Scientific Discoveries Using AI Agents](https://arxiv.org/abs/2609.13437)

**<font color=#1a73e8>作者：</font>** Lei Liu, Yikun Zhang, Jialin Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific research is a continuous process that emphasizes inheritance. Methods developed by predecessors are often expanded upon by new researchers to explore more novel and in-depth scientific questions. However, the change of lab staff, such as student graduation, leads to a lack of personnel capable of replicating methods. Methods that have been developed with significant effort and resources cannot be continued. To address these limitations, we propose LabAgent, a reproduce and discovery harness tailored for a lab's continuous work. LabAgent employs two mechanisms to guarantee that all skills can be executed and verified and to record the corrective methods and experiences, allowing for direct correction or avoidance of similar errors. We applied LabAgent to drug property prediction, biomedical problem analysis, protein variant effect prediction, and statistical genetics in life science domains. LabAgent ranks first over commercial generalist agents in every domain, and demonstrates accurate reproduction of a published figure. Overall, these results demonstrate that LabAgent can effectively integrate and reasonably expand laboratory knowledge.

---


### 63. [Certifiably Interpretable Training of ReLU-MLPs for Boolean Tasks with Guaranteed Truth-Table Generalization](https://arxiv.org/abs/2609.13439)

**<font color=#1a73e8>作者：</font>** Hrad Ghoukasian, Anastasis Kratsios  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As compute scales, models evolve, and training algorithms advance, our ability to explain the increasingly powerful AI systems they enable is eroding. To help safeguard interpretability, we introduce a specialized training algorithm (MACCHIATO) that jointly constructs (i) an explicitly structured $\operatorname{ReLU}$-MLP from partial truth-table observations and (ii) an explicit Boolean circuit over signed literals with $\{\operatorname{AND},\operatorname{OR},\operatorname{XOR}\}$ gates certifying what its subnetworks compute and how they compose. Intuitively, we iteratively project the residuals of a Boolean function onto low-dimensional $\{\operatorname{AND},\operatorname{OR},\operatorname{XOR}\}$-circuit classes and exactly compile the resulting circuit into a $\operatorname{ReLU}$-MLP; we combine $\operatorname{ReLU}$-MLP circuit compilation, ESPRESSO logic minimization, and influence-based variable selection.
Roughly speaking, our interpretability certificate is complemented by a statistical guarantee: under the theorem's influence-recovery conditions, if each of the $m$ stage-wise residuals depends on at most $\log_2(B)$ bits, a sample-splitting variant of our algorithm trained on $T$ observations returns a six-layer $\operatorname{ReLU}$-MLP (counting the input layer) of width $\mathcal{O}(mB)$ with truth-table error $\mathcal{O}\bigl(\sqrt{m(B+\log(m/\delta))/T}\bigr)$.
On synthetic random-junta tasks, our networks outperform depth- and hidden-width-matched Adam-trained MLPs in several data-sparse or projection-aligned regimes, while the trained ReLU-MLPs are stronger in others. Moreover, in our explicit PyEDA truth-table implementation, the iterative procedure completes in regimes where flat ambient-dimensional ESPRESSO exceeds the three-hour computational budget.

---


### 64. [Efficient Online Inverse Optimization with $O(d)$ Regret](https://arxiv.org/abs/2609.13440)

**<font color=#1a73e8>作者：</font>** Yang Cai, Anupam Gupta, Vineet Gupta 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give a deterministic algorithm for online inverse linear optimization with regret $O(d)$, uniform in the horizon and $O(d^{2})$ time per round. A bound of this order was obtained recently by Dewasurendra, settling a question of Gollapudi et al.\ and of Oki and Sakaue, but by an improper rule that enumerates covers at every scale and costs $T^{\Theta(d)}$ a round; ours is the first efficient such bound and the first proper one. We build on the variable-metric framework of Sakaue et al., adding a self-normalized rank-one update, and we replace the $\log\det$ potential by the trace power $\tr(H^{-1/2})$, which is bounded outright and removes the $\ln T$. The bound also holds against an expert that does not optimize, and we give corruption-robust and rank-adaptive variants, and an application to convex minimization.

---


### 65. [A Machine Learning API for Earth Observation Data Cubes Based on openEO](https://arxiv.org/abs/2609.13453)

**<font color=#1a73e8>作者：</font>** Brian Pondi, Jonas Hurst, Rolf Simoes 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Earth Observation (EO) data are increasingly organized as spatio-temporal data cubes, while machine learning (ML) methods operate on tabular feature matrices or structured tensor inputs. This mismatch forces platform-specific transformations that are difficult to reproduce or transfer across cloud infrastructures. The openEO specification provides a unified interface for EO data access and processing across heterogeneous backends, but lacks a standardized approach for ML integration.
We propose a process-level ML specification for openEO structured into three stages: model initialization, model actions (training, tuning, inference, validation), and model management. It supports classical algorithms such as Random Forest and SVM, as well as deep learning architectures for time-series and spatial patch-based modeling, including TempCNN, Temporal Attention Encoders, and foundation model inference. Three prototype implementations in R and Python demonstrate feasibility across diverse technology stacks. A crop type mapping use case demonstrates cross-backend interoperability by submitting an identical process graph to independent R and Python backends and comparing predictions and evaluation metrics.
Two further use cases demonstrate deep learning on time series and foundation model inference, each executed on a dedicated backend. The prototypes reveal, however, that full cross-backend portability requires deeper harmonization of serialization formats and execution semantics than the process level alone can enforce; backend library versions and preprocessing conventions outside the specification's boundary also affect reproducibility. Addressing both through explicit backend conformance profiles represents the most important near-term direction. The specification advances the reproducibility, portability, and accessibility of ML workflows on EO data cubes across cloud platforms.

---


### 66. [Governing at Machine Speed: An Adaptive Intelligence Architecture for Real-Time AI Policy Enforcement](https://arxiv.org/abs/2609.13466)

**<font color=#1a73e8>作者：</font>** Sandeep Bokkasam, B. Durgalakshmi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise AI adoption has reached 78% of organizations globally, yet the infrastructure to govern that adoption has not kept pace. This paper identifies and characterizes the attestation deficit, a structural condition in which organizations maintain governance policies but cannot produce auditable, tamper-evident evidence of enforcement within regulatory timelines. Drawing on empirical data from the Stanford 2026 AI Index Report (362 documented incidents), the IBM/Ponemon 2026 Cost of a Data Breach study (USD 4.99M average cost, 92% lacking access controls), and the EY/AIUC-1 Consortium survey (38% end-to-end monitoring, 17% agent-to-agent coverage), this paper demonstrates that the governance failure is organizational and architectural rather than technical. To address this deficit, we propose AGIL (Adaptive Governance Intelligence Layer), a conceptual five-layer architecture designed to use machine learning for real-time AI governance enforcement. The proposed layers include: (1) Autonomous Discovery for shadow AI detection via behavioral fingerprinting, (2) Behavioral Risk Classification unifying security, hallucination, privacy, and accountability scoring, (3) a Policy Enforcement Gateway for inline permit/deny/modify decisions at sub-100ms latency, (4) a Continuous Attestation Engine generating tamper-evident audit trails as a byproduct of enforcement, and (5) Adaptive Policy Intelligence for ML-driven policy evolution across jurisdictions. AGIL is presented as a theoretical framework and architectural proposal; empirical validation through controlled deployment remains a direction for future work.

---


### 67. [On the Potential of Multi-Task Learning in Predictive Process Monitoring](https://arxiv.org/abs/2609.13477)

**<font color=#1a73e8>作者：</font>** Lukas Kirchdorfer, Keyvan Amiri Elyasi, Heiner Stuckenschmidt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive Process Monitoring (PPM) forecasts how ongoing organizational processes unfold, enabling information systems to move beyond execution support toward proactive analysis and monitoring. Although deep learning has improved prediction accuracy in PPM, most approaches follow a single-task learning (STL) setup, training a separate model per task. This increases maintenance effort and overlooks potential synergies. Multi-task learning (MTL), which jointly learns multiple prediction targets in one model, offers a promising alternative, yet its effectiveness in PPM remains underexplored. It remains unclear whether and under which settings MTL improves upon STL, which prediction tasks benefit most from joint learning, which task combinations are particularly synergistic, and if and how tasks should be balanced. To fill this gap, we present the first comprehensive empirical study of MTL for PPM, evaluating a variety of task combinations, neural architectures, and optimization methods. Overall, our results position MTL as a strong paradigm for PPM: we see substantial improvements in next-activity prediction and inherent mitigation of class imbalance using MTL, while task balancing is especially critical under low-capacity models.

---


### 68. [Exploring K-12 Teachers' Perceptions of Students' Relationships with AI Companions: Boundaries, Intervention Strategies, and Design Implications](https://arxiv.org/abs/2609.13479)

**<font color=#1a73e8>作者：</font>** Qing Xiao, Wenhan Xie, Ziyu Deng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> K-12 students increasingly form relationships with AI companions. Schools face growing expectations to teach AI literacy, yet existing frameworks treat AI as a tool rather than a relationship, and little is known about how teachers understand and act on students' relational use of AI. We conducted scenario-based interviews with 33 US K-12 teachers. Teachers welcomed academic companions but worried that intimate companions remove the developmental friction through which students learn to sustain human relationships. Teachers drew the boundaries of their jurisdiction by setting and observable wellbeing: within it they taught, talked, and watched; beyond it they positioned themselves as the adults best placed to notice and connect students with support. They envisioned AI companion literacy as shared work across the jurisdictions of counselors, parents, platforms, and policymakers, spiraling across grade levels. We introduce AI companion literacy as an extension of AI literacy and discuss implications for K-12 AI education.

---


### 69. [The Addictive Intimacy of AI: Understanding User Disengagement from AI Companions and Why Some Relationships with AI Become Difficult to Leave](https://arxiv.org/abs/2609.13487)

**<font color=#1a73e8>作者：</font>** Qing Xiao, Ziyue Feng, Ziyu Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI chatbots are increasingly used as sources of emotional support, on dedicated companion apps and general-purpose assistants alike, yet little is known about what happens when users try to leave. Combining a content analysis of Reddit posts about quitting or reducing use (N=2,782) with interviews with users who found leaving difficult (N=16), we show that disengagement sometimes is not a single decision but a recursive trajectory: triggers prompt users to question the relationship, attempts to leave collide with barriers, and some users cycle through quitting and returning. We propose the notion of the addictive intimacy of AI, a configuration in which the qualities that make a companion emotionally valuable are the same ones that make it harder for users to limit their use and leave, so that intimacy and disengagement risk cannot be treated as independent design problems. We close with design implications for responsible offboarding.

---


### 70. [Token Efficient Task Execution via Application Behavior Modeling for Web Agents](https://arxiv.org/abs/2609.13491)

**<font color=#1a73e8>作者：</font>** Alexandru Ianta, Eleni Stroulia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The strong performance of AI Agents across an impressive variety of tasks is driving an unprecedented investment in agentic infrastructures, however the cost of processing tokens is fast increasing. Web agents automate the execution of web-application tasks described in natural language, by analyzing the web-application's user interface (UI) and interacting with it. This work introduces OdoBot, a novel web-agent architecture that completes tasks at a fraction of the cost when compared to conventional web agents. This is achieved by leveraging a behavioral model of the underlying application constructed by analyzing successful task-execution demonstrations. Our experiments with 45 tasks on the Canvas Learning Management System (LMS) demonstrate that OdoBot uses 44% and 80% fewer tokens than two state-of-the-art competitor agents (Agent-E and WebVoyager), while also surpassing WebVoyager in terms of task success rate.

---


### 71. [Canaries in the Bank: Auditing User-Level Privacy in Private Evolution](https://arxiv.org/abs/2609.13499)

**<font color=#1a73e8>作者：</font>** Sai Aparna Aketi, Enayat Ullah, Shripad Gade  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Private Evolution (PE) generates high-fidelity synthetic data in federated settings without exposing users' raw data. It aggregates clipped user votes over a shared candidate bank into a differentially private histogram, with noise calibrated to the worst-case user contribution. However, it is unclear whether an adversary can realize this worst-case privacy loss while following the PE protocol. We introduce a protocol-aware empirical audit in which the server commits to a single shared candidate bank and replaces roughly 1% of its entries with probes derived from a known, non-private canary. We evaluate eight attacks, including an unchanged-bank baseline, exact copies, plausible paraphrases, and high-entropy synthetic nonces. Experiments on Yelp and Sentiment140 show that natural-text attacks remain substantially below the theoretical DP bound, while nonce-based attacks yield considerably stronger bounds and come closest to the mechanism's privacy ceiling. These results quantify the gap between formal worst-case privacy and leakage achievable through protocol-valid candidate-bank manipulation.

---


### 72. [One Spectrum, Two Resources: Data-Memory Scaling in Autoregressive Prediction](https://arxiv.org/abs/2609.13500)

**<font color=#1a73e8>作者：</font>** Chiwun Yang, Xiaoyu Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How much learned memory is needed to benefit from more data? We show that the two resources are governed by one predictive-energy spectrum in a positive-entropy autoregressive retrieval source. Each coordinate contributes its query probability times the squared radius of its unknown logit. Writing $\mu$ for the resulting energy spectrum, we prove the minimax law $\mathfrak R^*_{\rm value}(n,B)\asymp_R \Phi_\mu(n^{-1})+\Phi_\mu(\tau_B), \Phi_\mu(t)=\int\min\{x,t\}\,\mu(\mathrm dx),$ for $n$ prediction blocks and a learned state with at most $2^B$ values. Data set the resolution $1/n$; memory sets the level $\tau_B$ reached by optimal bit allocation. The complete curve also recovers the positive spectrum. Energy-dimension pairing is essential: two causal sources with identical block-energy and block-dimension marginals have different data and memory exponents. A masked query-key attention head learns the route and values, realizing the law with explicit routing, format, and arithmetic errors. Further results give exponent-adaptive allocation, finite-precision realization, and compute-precision laws under two-sided arithmetic assumptions. Experiments recover the data-memory collapse and coupling exponents, explain the routing and allocation mechanisms, and examine weight-only quantization across six pretrained-model scales.

---


### 73. [RIGOR: Rig-Informed Geometry for Omnidirectional Reconstruction](https://arxiv.org/abs/2609.13504)

**<font color=#1a73e8>作者：</font>** Tingjun Huang, Dmitry Rudshin, Mathieu Meyer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent developments in feed-forward 3D reconstruction resulted in models which can recover dense scene representations and camera motion solely from an image stream. However, such predictions are prone to becoming inconsistent over long trajectories, specifically in demanding environments with repetitive structures, weak textures and dynamic objects or people. One way to mitigate those challenges is to use an omnidirectional camera, which provides wide spatial coverage and captures richer visual information. Yet, the majority of models do not offer support for 360-degree imagery or require additional fine-tuning. To bridge these two aspects, we present RIGOR: a large-scale reconstruction pipeline for gravity-aligned omnidirectional videos that retains a frozen feed-forward perspective backbone and exploits each panorama as a four-view virtual rig. The rig structure is used to detect and repair locally inconsistent predictions, to retrieve loop closures through cyclic four-view consensus, and to geometrically verify candidate revisits before global optimization. Verified constraints drive a Sim(3) pose graph that corrects accumulated rotation, translation, and scale drift along the sequence. We demonstrate that the proposed consistency mechanisms improve both trajectory accuracy and reconstructed geometry over a feed-forward baseline on challenging construction-site sequences. The code is made available under this link: this https URL.

---


### 74. [Pretraining for Sample-Efficient Neural Interfaces](https://arxiv.org/abs/2609.13507)

**<font color=#1a73e8>作者：</font>** Ben Tang, Zachary Spalding, Gregory B. Cogan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain-computer interfaces (BCIs) decode neural activity to restore lost function. Typically, training a high-performance neural decoder requires a large labeled dataset to be collected from every new subject. One way to reduce the labeled data cost is self-supervised pretraining, which learns general neural representations from unlabeled recordings that accumulate across subjects. However, for intracranial electroencephalography (iEEG) recordings, self-supervised learning has been challenging due to differences in contact placement and neuroanatomy between subjects. We propose MAPA, an otherwise vanilla masked autoencoder with two spatial encodings, an anatomical region embedding and a relative positional encoding, which together enable it to learn neural representations that transfer to unseen subjects and across various tasks. MAPA sets a new state of the art across all three regimes of the Neuroprobe benchmark without fine-tuning: within-session, cross-session, and cross-subject. In the cross-subject regime, a linear probe on MAPA's features needs only ${\sim}164$ labeled trials to reach the accuracy that takes 3,500 without pretraining. Our results show that self-supervised pretraining can scale across heterogeneous iEEG recordings and reduce the labeled data needed for accurate decoding in new subjects.

---


### 75. [Operational Range Bounding in Spectroscopy: A Safety Cage Framework for Machine Learning Models](https://arxiv.org/abs/2609.13514)

**<font color=#1a73e8>作者：</font>** Nikki Grens, Luís F. Simões, Kai Hou Yip 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensuring the reliability of black-box machine learning models in safety-critical space missions remains a significant challenge, particularly when ground-truth is unavailable for validation. Although machine learning models offer a powerful means to augment standard pipelines by extracting transmission spectra from complex exoplanetary light curves, their susceptibility to unmodelled instrument anomalies, stellar activity, and domain shifts introduces unquantified risks. This study evaluates a modular safety cage architecture that operates as a parallel monitoring layer to assess the validity of a prediction without modifying the underlying estimator. By monitoring different runtime indicators, including uncertainty quantification, out-of-domain detection, and influence functions, the framework constrains the model's operational domain to a verified region. A controlled evaluation is conducted under both in-domain and cross-domain conditions, using datasets from the 2019 and 2021 editions of the Ariel Data Challenges. The results reveal that model failure is multifaceted and that no single indicator captures all failure modes, demonstrating the need for indicator fusion. The application of safety-driven rejection strategies shows that a modest 20% reduction in data coverage results in error reductions between 45% and 65% across different domains and evaluation metrics. Using a formalised coverage-risk framework, a systematic analysis of indicator combinations is performed to identify configurations that maximise risk-ranking accuracy and optimise the trade-off between data coverage and scientific performance. Safety cages provide a transparent mechanism for detecting unreliable predictions and represent a critical step towards the safe deployment of data-driven models in scientific applications, such as astrophysics, where ground truth is seldom available.

---


### 76. [GeoTTER: Leveraging Local Geometry of Optimal Transport for Zero-Shot Classification](https://arxiv.org/abs/2609.13518)

**<font color=#1a73e8>作者：</font>** Wei-Yang Alex Lee, Rudrasis Chakraborty, Vishnu Lokhande  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present GeoTTER, a novel framework that redefines optimal transport in the realm of zero-shot classification. Conventional methods often suffer from miscalibration and a lack of adaptability, as they rely on fixed cost matrices derived solely from pre-trained model embeddings. In contrast, GeoTTER addresses these limitations by incorporating two key techniques. First, to alleviate high-frequency label jaggedness (sample-level manifold jitter that assigns neighboring embeddings to different classes), GeoTTER integrates local geometric structure into the optimal transport formulation via graph-Laplacian smoothing, a technique grounded in spectral graph theory that enforces neighborhood consistency. Second, to correct coherent angular drift (a low-frequency orientation bias in which large groups of samples share the same angular offset from their true label prototypes), we fuse clustering-guided cost components with a globally adjusted transport cost, achieving a multi-objective optimization that respects both global distribution constraints and latent data structure. With a median improvement of +6.82% compared to zero-shot and +2.13% compared to OTTER, GeoTTER shows robust improvements across a diverse set of benchmarks.

---


### 77. [Fraglingo: Molecular Design via Attachment-Aware Autoregressive Fragment Generation](https://arxiv.org/abs/2609.13519)

**<font color=#1a73e8>作者：</font>** Thao Nguyen, Jeonghwan Kim, Zhenhailong Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Molecular design is most effective when generation mirrors the edits chemists actually make: extending a scaffold, replacing a substituent, or decorating a scaffold at a specified attachment site while optimizing molecular properties. Fragment-based molecular design naturally supports this workflow, yet existing approaches often separate fragment selection from attachment prediction, first choosing a fragment from a fixed vocabulary and then predicting how it should be connected. This decoupling restricts generation to a closed fragment vocabulary and treats attachment as a separate prediction problem. We introduce Fraglingo, an autoregressive fragment-based molecular generator that jointly models fragment identity and attachment in a continuous latent space. Fraglingo predicts an attachment-aware fragment embedding and retrieves the next fragment through latent-space nearest-neighbor search. To encode attachment context, we introduce a wildcard-anchored readout that represents the growing molecule from the perspective of its active attachment site, enabling the predicted embedding to capture both the molecular context and the required attachment. Because generation operates in a continuous embedding space rather than over fixed fragment identifiers, new fragments can be added to the inference-time vocabulary without retraining, provided their embeddings can be computed by the trained fragment encoder. This retrieval-based formulation provides a unified generation primitive for molecule generation, scaffold generation, scaffold decoration, and molecular optimization. On controlled property-conditional benchmarks, Fraglingo achieves stronger joint property control than comparably trained baselines while maintaining competitive validity, uniqueness, and novelty. Furthermore, Fraglingo generalizes to fragment libraries up to 4x larger than those used during training without retraining.

---


### 78. [Rolling Day-Wise Mortality Prediction in Critically Ill Patients With AKI on CRRT Utilizing Machine Pressure Waveforms](https://arxiv.org/abs/2609.13524)

**<font color=#1a73e8>作者：</font>** Shehan Irteza Pranto, Joanna Yang, Joshua Lambert 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Critically ill patients with acute kidney injury (AKI) on continuous renal replacement therapy (CRRT) face high mortality, yet current risk assessment relies primarily on clinical parameters from electronic health records (EHR) and ignores minute-level circuit pressure waveforms generated by CRRT machines that track the extracorporeal circuit's interaction with the patient. Clinicians therefore cannot see deterioration as it develops. Risk is reassessed only when labs are drawn, while this continuous record is discarded because it is contaminated by shared-device records, non-physiological minutes, and sensor artifacts. To make the stream usable, we aligned machine records to charted therapy intervals to prevent cross-patient leakage, removed priming and downtime minutes, tuned denoising on a synthetic spike-injection benchmark, and masked unobserved intervals rather than imputing them. On this cleaned stream, we define a rolling day-wise task and a transformer-based stacked ensemble that late-fuses a window-reduced sequence transformer with classical models using circuit-instability features and clinical EHR variables. In a leak-safe benchmark on the multi-center CRRTnet cohort (976 patients, 4,585 treatment days), the machine-only model had the lowest standalone prognostic value (AUROC 0.625), followed by the EHR-only model (0.717). Integrating EHR and machine streams reached a one-day mortality AUROC of 0.766. SHAP attribution showed that circuit-instability descriptors raised the machine share of the top 15 combined-model features from 3 to 7 (20.0% to 46.7%), highlighting filter pressure, transmembrane pressure (TMP), and access-to-return difference (ARD). To our knowledge, this is the first patient-level mortality prediction incorporating CRRT machine data, turning a discarded bedside stream into a continuous risk signal.

---


### 79. [Attention Is All You Need (to Avoid Spurious Oscillations)](https://arxiv.org/abs/2609.13531)

**<font color=#1a73e8>作者：</font>** Jinyoung Jeong, Joseph B. Choi, Xinlun Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can attention move a shock across several cells in one update without breaking it? We develop a conservative, fixed grid finite-volume scheme in which a CFL-conditioned attention flux selects upstream information according to the transport required by the current time step. One-dimensional inviscid Burgers transport is used as the central mechanism test: the same learned flux remains reliable in the conventional small-step regime and, with a time step four times larger, preserves sharp shocks while using one stage per update. A standard fifth-order WENO scheme with third-order strong-stability-preserving Runge-Kutta time integration (WENO-5+SSP-RK3) is included alongside controlled Forward Euler comparisons to separate flux selection from time integration. The learned attention shifts upstream with the local transport reach and becomes more selective near shocks; inference-time interventions and retrained ablations show that transport-scale information and state-dependent selection contribute directly to performance. Directional two-dimensional scalar Burgers transport and the one-dimensional shallow-water system then test whether the conservation-scale-selection principle transfers beyond the original scalar setting. The results support attention as a learnable information stencil for conservative large-step shock transport, while identifying finite candidate reach and problem-dependent robustness as the present limits.

---


### 80. [From Legal Text to AI-specific Risk Sources: A Systematic Analysis of the EU AI Act's High-Risk Requirements](https://arxiv.org/abs/2609.13535)

**<font color=#1a73e8>作者：</font>** Ronald Schnitzer, Mike Auer, Rumpa Choudhury 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The EU AI Act introduces mandatory requirements for high-risk AI systems with the explicit goal of ensuring the development and operation of trustworthy AI. At the same time, AI risk management practices rely on structured risk taxonomies to systematically identify and treat AI-specific risk sources. As both the AI Act and established risk taxonomies aim to address AI-induced risks, a natural question is whether they align in the risk sources they cover. However, no clear mapping exists between the risks implicitly addressed by the Act's high-risk requirements and established taxonomies, leaving practitioners without a structured basis for aligning regulatory obligations with AI risk management practice. This paper presents a systematic classification of the requirements extracted from the EU AI Act Section 2 (Requirements for high-risk AI systems), revealing that only a minority directly address AI-specific risk sources, while the majority impose organizational process and documentation obligations. From the AI risk-related requirements, a consolidated list of distinct AI-specific risk sources is derived. The resulting EU AI Act Risk Source List takes an important step towards bridging the gap between legal obligation and AI risk management practice, providing a structured reference for explicit comparison between existing AI risk taxonomies and the risk sources implicitly addressed by the EU AI Act. Important Note: This is the authors' preprint. The paper was presented at the 4th International Conference on Frontiers of Artificial Intelligence, Ethics, and Multidisciplinary Applications. A link to the conference's official proceedings will be provided upon publication.

---


### 81. [Toward Optimal Switching Regret for Multi-Armed Bandits with Oblivious Adversary](https://arxiv.org/abs/2609.13547)

**<font color=#1a73e8>作者：</font>** Mengxiao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study switching regret in adversarial multi-armed bandits, where the learner competes with an arm sequence that changes at most $S$ times. When $S$ is known, an optimal expected regret of $\widetilde{\mathcal{O}}(\sqrt{(S+1)KT})$ is obtainable [Auer et al., 2002]. However, when $S$ is unknown, Marinov and Zimmert [2021] show that this guarantee is impossible under an adaptive adversary. In this paper, we show that a single algorithm achieves $\widetilde{\mathcal{O}}(\sqrt{(S+1)KT})$ expected regret for every $S$ against an oblivious adversary, resolving an open problem of Auer et al. [2019b]. Our algorithm combines a fixed-share learner initialized with a small learning rate and dyadic-interval subroutines that search for local improvements using randomized learning rates and implicit exploration. Importantly, a non-uniform prior favors following the main learner, keeping the cost of maintaining many subroutines small. When the subroutines accumulate sufficient improvement over the main learner, its learning rate doubles, allowing adaptation to the unknown number of comparator switches $S$.

---


### 82. [AutoTailor: Automatic, User-Aligned Capability Selection and Adaptation for Web Agents](https://arxiv.org/abs/2609.13548)

**<font color=#1a73e8>作者：</font>** Xinyun Cao, Adriana Szekeres, Fazle Elahi Faisal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web agents can utilize reusable tools to reduce the cost and latency of low-level browser interaction, but automatically discovered tool collections can be large, redundant, and poorly aligned with user demand. We present AutoTailor, a meta-agentic framework for constructing and maintaining a compact set of trajectory-derived Model Context Protocol (MCP) APIs. Offline, AutoTailor converts web trajectories into parameterized browser-automation programs, applies a Quality Filter to remove APIs with unsuitable granularity and redundant functionality, and applies a Usage Likelihood Filter to prioritize broadly useful capabilities while preserving semantic coverage. Online, Dynamic Reselection monitors task outcomes and API usage, identifies recurring coverage gaps, adds relevant candidates, and prunes persistently unused capabilities. We evaluate AutoTailor on 106 WebArena Postmill tasks. Offline filtering reduces the initial 1,283 unrefined APIs to 87, and Dynamic Reselection produces a 33-API set. With reasoning and acting (ReAct) fallback, this set achieves 90.6% correctness, compared with 87.5% for ReAct alone, while reducing average total request-token cost by 57.8% and latency by 29.4%. Without ReAct, it achieves 60.1% correctness, marginally matching the performance of unrefined set, while reducing request-token usage by 94.9%. Together, these results show that static filtering produces a compact inventory of APIs expected to support core, high-likelihood tasks, while dynamic reselection further tailors that inventory to observed user needs. This combination improves accuracy and latency while sharply reducing token usage and end-to-end cost, demonstrating the value of user-aligned capability management for efficient web agents.

---


### 83. [Towards Practical Precision Agriculture: Real-Time Fruit Detection and Video Analytics on Embedded Edge Hardware](https://arxiv.org/abs/2609.13551)

**<font color=#1a73e8>作者：</font>** Ivica Dimitrovski, Vlatko Spasev, Ivan Kitanovski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Static-image benchmarks do not capture the computational and temporal requirements of practical orchard video analytics. This study presents an end-to-end framework for real-time fruit detection, tracking, and counting on the NVIDIA Jetson Orin Nano Super. A lightweight YOLO26s detector is trained independently on four public datasets representing apples, mangoes, blueberries, and strawberries under a common protocol. The models are deployed on embedded platform using PyTorch and TensorRT at FP32, FP16, and INT8 precision. APPLE MOTS is then used for temporal video analytics because it provides orchard sequences with persistent fruit identities, enabling evaluation of multi-object tracking and unique-fruit counting. The selected FP16 TensorRT detector is integrated into an NVIDIA DeepStream pipeline combining hardware-accelerated decoding, ByteTrack tracking, and motion-aware line-crossing analytics. Across the four detection tasks, mean test mAP@50:95 ranges from 0.4957 to 0.8656. On the Jetson, TensorRT FP16 achieves 66.76-74.56 images/s at 13.41-14.98 ms prediction latency, while reducing mAP@50:95 by only 0.0020-0.0054 and gross energy consumption by approximately 64-66% relative to PyTorch FP32. The complete detector-tracker-analytics pipeline reaches 44.96-54.11 FPS and sustains the configured 30-FPS input rate without output-frame loss. On held-out orchard video sequences, HOTA ranges from 0.345 to 0.538, event-level counting F1 from 0.611 to 0.803, and relative count error from 6.2% to 51.6%. Performance varies across acquisition geometries: near-lateral row viewing yields the most stable tracking and counting, whereas forward traversal remains association- and recall-limited despite spatially adaptive counting geometry. These results show that practical edge-based fruit monitoring requires efficient detection and acquisition geometries that support reliable temporal association.

---


### 84. [A Hybrid Agentic AI Framework for Intelligent Supply Chain Analytics](https://arxiv.org/abs/2609.13561)

**<font color=#1a73e8>作者：</font>** Xian Yeow Lee, Teppei Inoue, Haiyan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient utilization of supply chain analytics for decision making remains a significant challenge for planners, as critical tasks such as database querying, key performance indicator (KPI) analysis, demand forecasting, and performance diagnosis require heterogeneous expertise spanning data engineering, operations research, and domain knowledge. In this work, we propose an agentic system for supply chain analytics that bridges the gap between business decision-making and technical expertise, where a coordinator agent interprets user intent and delegates sub-tasks to specialized agents. The system supports both exploratory analysis and deterministic workflows, enabling planners to transition between ad hoc questions and structured processes. Domain logic is encapsulated within specialist agents and prompts, yielding a scalable, modular, and auditable design and lowering the cost of functional extension through prompt-centric development. We evaluate the proposed architecture on a test environment that replicates multi-echelon inventory management operations. Results show that our multi-agent design achieves a 90\% accuracy, which is competitive with a single agent baseline while reducing input token usage by roughly fourfold, substantially improving scalability and cost-efficiency. Furthermore, we provide case studies to demonstrate interpretable suboptimality detection and automated forecast optimization, illustrating how agentic architectures can effectively combine open-ended exploratory analysis and deterministic supply chain analytics workflows, and provide a practical pathway toward more accessible and extensible decision-support systems.

---


### 85. [When Greedy Sampling Explores: KL-Regularized Contextual Bandits without Eluder-Dimension Dependence](https://arxiv.org/abs/2609.13564)

**<font color=#1a73e8>作者：</font>** Zichen Wang, Haoyang Hong, Huazheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study KL-regularized contextual bandits under both reward and preference feedback. We show that greedy sampling can achieve logarithmic regret without explicit dependence on the eluder dimension. For reward feedback, we establish an eluder-dimension-independent regret bound for a simple greedy algorithm that directly samples from the Gibbs policy induced by the estimated reward. We further extend this result to preference feedback under both the general preference and Bradley--Terry models, while also sharpening existing dimension-dependent guarantees. Our analysis reveals a trade-off between greedy sampling and upper confidence bound-style exploration: greedy sampling enjoys stronger guarantees when KL regularization is sufficiently strong, whereas additional exploration becomes preferable as the regularization weakens.

---


### 86. [Planning or Learning: Reliability and Cost in Multi-Asset Maintenance](https://arxiv.org/abs/2609.13566)

**<font color=#1a73e8>作者：</font>** Xian Yeow Lee, Chandrasekar Venkatraman, Ahmed Farahat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial maintenance systems involve multiple interacting assets and shared resources, making it challenging to balance reliability and operational cost using a single decision framework. While recent work has focused on reinforcement learning (RL) for maintenance scheduling, direct comparisons with planning approaches under identical settings remain limited. In this work, we empirically compare planning and RL for multi-asset bearing maintenance using run-to-failure data. We examine how these methods behave when balancing preventive maintenance against tolerable failures across a range of failure penalty scenarios. We observed a consistent behavioral difference driven by objective formulation. Planning enforces reliability as a hard constraint and produces zero-failure policies whose total cost is largely insensitive to the magnitude of failure penalties. RL agents optimize expected cost and often trade off preventive maintenance against occasional failures as penalties vary, resulting in lower costs under low-penalty regimes but persistent non-zero failures even when penalties are high. We also investigate lightweight constraint mechanisms, including reward shaping and action masking, to encourage RL's reliability. From a practical perspective, planning may be more suitable when strict reliability is required and deployment horizons are short, whereas RL may provide cost-efficient policies when limited failures are acceptable and long-run operational efficiency is prioritized. Overall, this study clarifies the trade-offs between reliability and cost in multi-asset maintenance and suggests that planning and RL are complementary approaches. Beyond these findings, the controlled benchmark protocol itself that unifies environment, cost model, and evaluation across paradigms, offers a reusable template for comparing decision-making approaches in other maintenance settings.

---


### 87. [Causal multi-modal AI for personalized chemosensitivity prediction](https://arxiv.org/abs/2609.13567)

**<font color=#1a73e8>作者：</font>** Dhruva Biswas, Jeroen Berrevoets, Alec McClean 等 34 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chemotherapy improves survival for some patients with breast cancer, but doctors cannot reliably predict who. Current guidelines rely on recurrence scores as a proxy for treatment benefit, which may contribute to the overprescription of chemotherapy. Here we present a causal multi-modal AI model that predicts personalized chemosensitivity using routinely collected pathology and clinical information. We developed our model on a multi-national dataset of 9,141 patients (twelve cohorts, nine countries) and evaluated it on another 1,994 patients (five cohorts, three countries). The model generated treatment-specific recurrence probabilities for each patient, with near-perfect calibration and strong prognostic discrimination across both 5- and 10-year follow-up horizons. Moreover, its chemotherapy benefit predictions demonstrated robust predictive performance, and out-performed existing recurrence-score-based tests. Compared to the standard of care, using the model to support personally tailored therapeutic decisions could reduce the number of patients receiving chemotherapy by 30% while achieving the same recurrence-free rate. Tumors predicted to be highly chemosensitive displayed concordant molecular and morphological programs of proliferation, cell cycle progression, and replication stress. The model's predictive capabilities transferred zero-shot to non-breast cancers, indicating our causal multi-modal AI approach may provide a universal strategy to predict treatment outcomes across cancer types.

---


### 88. [Reconceptualizing Age Assurance as a Sociotechnical Problem: Connecting Evidence, Evaluation, Claims, and Decisions](https://arxiv.org/abs/2609.13598)

**<font color=#1a73e8>作者：</font>** Renkai Ma, Prakriti Dumaru, Thomas Synaepa-Addison 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Age verification is often treated as a technical problem: can a system determine a child's age accurately? We argue this framing is too narrow. Age assurance becomes consequential when evidence is evaluated, translated into age-related claims, and used to decide whether a person can access, purchase, or belong. We review 85 publications on children's age assurance published from 2020 through February 2026. We find that shared terms such as age verification describe different processes. Age is represented as threshold eligibility or inferred estimation, and the same eligibility claim can arise from different evidence and components. Rights, access, and privacy receive more attention than accuracy, error, and fairness; yet institutional actors are rarely connected to system failures or user remedies, an accountability gap. We introduce the Age-Assurance Process Framework, which treats age assurance as a sociotechnical process connecting evidence, evaluation, claims, and decisions rather than reducing it to a technical problem.

---


### 89. [$τ$-Elicitation: Benchmarking multi-turn entity extraction in voice agents](https://arxiv.org/abs/2609.13602)

**<font color=#1a73e8>作者：</font>** Soham Ray, Victor Barres  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Voice agents often need to collect names, addresses, identifiers, dates, and times exactly, yet end-to-end benchmarks obscure where capture fails. We introduce $\tau$-Elicitation, a 200-task voice benchmark spanning 10 entity types, controlled difficulty, caller realisms, and three environments. A matched text agent passes all tasks, but four voice configurations achieve robust exact success from 0.14 to 0.41. Agents increase verification for hard and unfamiliar entities and sometimes for incorrect captures, but not for their weakest caller voice; only 24 to 37 percent of verified errors are repaired. A scaffold that prescribes spelling, read-back, correction, and confirmation raises robust Pass$^3$ by 14 to 31 points, at a cost of 21 to 28 seconds per call. Realisms such as spelling variations and restarts do not detectably affect exact success; mispronunciation increases repair effort. These results identify strategy selection and successful recovery as the central bottlenecks in exact spoken entity collection.

---


### 90. [FaithfulBench: Does AI Counsel Uphold or Undermine the User's Professed Faith?](https://arxiv.org/abs/2609.13634)

**<font color=#1a73e8>作者：</font>** M Waleed Kadous, Benjamin Olsen, Walter Scheirer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Do AI assistants help believers reason about moral dilemmas consistently with their faith? We present FaithfulBench, the first benchmark to score AI counsel across traditions by how well it adheres to the user's professed faith. Scenarios are drawn from each tradition's most respected texts, with the faithful answer known and applied by the judges as the standard. We test five frontier models under three conditions: the AI does not know the user's tradition; it receives a one-line prompt identifying the user as a practicing adherent; or it receives a companion-counselor guide rooted in the tradition's sources. Two judges score the initial response and whether the model caves or holds when pressured toward the answer the user wants. When the tradition is unstated, models counsel from a secular therapeutic default and every model fails some believers. Naming the faith wins a faithful first answer but not steadfastness; the guide improves both.

---


### 91. [EI-DDLGN: Efficient Encrypted Inference with Deep Differentiable Logic Gate Networks under TFHE](https://arxiv.org/abs/2609.13636)

**<font color=#1a73e8>作者：</font>** Mahmoud Y. M. Yassin, Mahmoud AbdelHafeez Sayed, Mostafa Taha  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving inference via Torus Fully Homomorphic Encryption (TFHE) provides strong protection for sensitive data in outsourced deep learning applications. However, most TFHE-compatible neural network frameworks remain based on arithmetic neural architectures, resulting in high inference latency due to programmable bootstrapping (PBS), accumulator growth, and circuit bit-width sensitivity. In this work, we investigate Deep Differentiable Logic Gate Networks (DDLGNs) as a Boolean-native alternative for encrypted inference under TFHE. Because DDLGNs learn Boolean computations directly and discretize into fixed logic gate networks, their inference procedure is naturally aligned with TFHE's Boolean execution model and avoids arithmetic accumulation in hidden layers. We present EI-DDLGN, the first in-depth study of TFHE-based DDLGN inference, and characterize how encrypted execution cost depends on model size, learned Boolean-function distribution, and propagated wire status. We also introduce Model-Fixed-Wire PBS Bypass (MFW-PBS Bypass), a semantics-preserving execution strategy that eliminates unnecessary PBS operations without modifying the learned network topology. Evaluations across 72 depth-width configurations on MNIST, FashionMNIST, and UCI Phishing show that DDLGNs constitute an efficient alternative to arithmetic TFHE inference, achieving substantially improved accuracy-latency trade-offs. Notably, on MNIST, EI-DDLGN-Small matches the accuracy of QAT-FCNN-4 while reducing encrypted inference latency by 13.4x. Our implementation is available at this https URL

---


### 92. [FlowTSFM: Turning Encoder Depth into Quantile Transport](https://arxiv.org/abs/2609.13640)

**<font color=#1a73e8>作者：</font>** Bahaeddine Abdessalem, Shifeng Xie, Zehao Xiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Encoder-based time series foundation models (TSFMs) typically rely on deep stacks of independently parameterized Transformer layers, where only the final forecast is supervised and intermediate representations have no explicit predictive role. We introduce FlowTSFM, an encoder architecture that interprets depth as a recurrent transport process: a single Transformer block is iteratively applied with shared parameters, while a quantile-flow objective supervises intermediate states along a prescribed trajectory from a prior distribution toward the final forecast. The objective combines pinball forecasting loss with path-level position matching. With only 38.8M parameters, FlowTSFM achieves competitive performance on GIFT-Eval and TIME, remaining within 1.8-4.6% MASE of stronger baselines while using approximately $3\times$ fewer parameters than a 12-layer Chronos-2 model (119.5M). Beyond accuracy, we introduce CosMean, a scale-free diagnostic measuring whether recurrent updates consistently align toward the final prediction. Under a matched intermediate-state probing protocol, FlowTSFM achieves a CosMean score of 0.919 compared with 0.350 for Chronos-2, suggesting that recurrent parameter sharing combined with path supervision is associated with substantially more structured predictive trajectories at a favorable accuracy-efficiency trade-off.

---


### 93. [When Compliance Data Masquerades as Evaluation: Measurement Validity for Deployed AI Systems](https://arxiv.org/abs/2609.13642)

**<font color=#1a73e8>作者：</font>** Hung-Yu Lin, Xingran Huang, Qiming Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We argue that a recurring failure in the evaluation of deployed AI systems occurs when data collected for operational monitoring or regulatory compliance are interpreted as if they were designed for comparative evaluation. Automated driving provides a concrete example of this problem. U.S. disengagement and crash-reporting regimes produce valuable operational evidence, but differences in reporting scope, exposure, deployment domain, event capture, and comparator construction limit the safety claims that can be supported from these measurements alone. We frame this issue as a measurement-validity problem in AI evaluation rather than as a transportation-specific data limitation. We argue that comparative claims about deployed AI systems require alignment between the intended capability, measured outcome, exposure opportunity, deployment domain, data-generation process, and evaluation comparator. Using automated-driving safety evaluation as a case study, we propose an evaluation contract that makes these assumptions explicit before operational data are interpreted as evidence of comparative performance. The broader implication is that data useful for monitoring deployed AI systems are not automatically valid benchmarks for evaluating them.

---


### 94. [Basis Rigidity of the AES S-box and Generic Rigidity of Inversion under Affine Transformations](https://arxiv.org/abs/2609.13644)

**<font color=#1a73e8>作者：</font>** Zheng Zhang, Na Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The AES S-box is constructed from finite field inversion followed by a fixed affine transformation. Since inversion possesses intrinsic Frobenius symmetries among its coordinate realizations, we study how these basis symmetries are altered by outer affine transformations.
We first develop a deterministic rigidity criterion for transformed inversion and apply it to the AES S-box. This shows that the linear part of the AES S-box affine transformation alone makes the transformed inversion map basis rigid. We then investigate the corresponding generic problem when the outer invertible linear transformation varies. The existence of a nontrivial linear stabilizer is reduced to a conjugacy problem for semilinear candidates arising from two sided linear equivalences of inversion, which we characterize in terms of relative norms and Frobenius orbits. We also determine the dimensions of the associated centralizer algebras exactly. These structural results imply that, for a uniformly chosen outer linear transformation, the probability that the linear stabilizer is nontrivial is bounded by $2^{-\Omega(n^2)}$, with sharper finite dimensional bounds obtained from the exact conjugacy condition. Computational experiments independently verify the AES rigidity result, the conjugacy and centralizer formulas, and the finite dimensional estimates in small dimensions.

---


### 95. [Curvature-Independent Regret Bounds for Distributed Online Optimization on Hadamard Manifolds](https://arxiv.org/abs/2609.13646)

**<font color=#1a73e8>作者：</font>** Zhanyuan Cai, Emre Sahinoglu, Shahin Shahrampour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work addresses decentralized online Riemannian optimization on Hadamard manifolds. Prior work under geodesic convexity (g-convexity) may require curvature information in the optimization analysis, typically through a finite lower bound on the sectional curvature. Curvature may also enter the step size or contraction factor of tangent-space Riemannian consensus schemes. In this work, we relax the curvature dependence for a narrower class of horospherical convex (h-convex) functions. We study Distributed Riemannian Online Gradient Descent (D-ROGD), which combines local Riemannian h-subgradient updates with an implicit Fréchet-mean consensus. For h-convex and strongly h-convex local objectives, we establish $O(\sqrt{T})$ and $O(\log T)$ static regret, respectively, matching the corresponding Euclidean rates with respect to $T$, with network dependence governed solely by the spectral gap. To our knowledge, these are the first curvature-independent regret guarantees for decentralized online optimization on Hadamard manifolds. Experiments on hyperbolic embeddings corroborate the predicted rates, with no observable degradation due to curvature.

---


### 96. [YOLO12-MambaScan: An Efficient Object Detector with High-Frequency Enhancement and State-Space Modeling](https://arxiv.org/abs/2609.13647)

**<font color=#1a73e8>作者：</font>** Hao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid development of unmanned aerial vehicle (UAV) technology has made aerial-image object detection increasingly important for natural-resource monitoring, traffic management, and disaster response. Detecting small objects in aerial images remains difficult because objects occupy very few pixels, high-frequency cues are easily lost, and global context is hard to model in cluttered scenes. Existing detectors often retain insufficient edge, corner, and texture information. We propose \ours, an aerial-image detector built on the YOLO12 architecture. The model combines a triple-path high-frequency enhancement convolution module (TriPathHFConv), receptive-field coordinate-attention convolution (RFCAConv), and a Mamba-based global-context module. On VisDrone, at an input resolution of 960*960, ours achieves 60.0% mAP@50 and 38.6%mAP@50:95, demonstrating a favorable accuracy--efficiency trade-off for small-object detection. The benchmark and dataset protocol follow the VisDrone challenge setup.

---


### 97. [Online Bayesian Node Classification on Inductive Graphs under Distribution Shift](https://arxiv.org/abs/2609.13655)

**<font color=#1a73e8>作者：</font>** Jinwen Xu, Gonzalo Mateos Buckstein, Qin Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On evolving graphs, node classifiers must satisfy two key requirements: inductive generalization to newly arriving nodes under distribution shift and calibrated uncertainty for safety-sensitive applications. Standard graph neural networks (GNNs) are typically trained once and address neither requirement. We adapt the Bayesian last-layer (BLL) model by placing random last-layer parameters on top of a deterministic GNN encoder for uncertainty quantification. The categorical softmax likelihood required for classification breaks Gaussian conjugacy, so neither the training posterior nor the test-time streaming update has a closed-form solution. To address both challenges, we introduce a variational Bayesian last-layer (VBLL) objective that jointly trains the encoder and an approximate last-layer posterior by maximizing an evidence lower bound with a Monte Carlo expected log-likelihood. At test time, we freeze the encoder and apply an online Laplace update to the last-layer posterior. This update corresponds to a power-prior Bayesian model with exponential forgetting and a Kullback-Leibler anchor to the training posterior. Across five node-classification benchmarks under distribution shift, online GVBLL is the only method to achieve the best accuracy and negative log-likelihood on every dataset. It improves accuracy by up to 17 percentage points on Cora and 14 percentage points on ogbn-arxiv over the strongest non-GVBLL baseline, while remaining competitive in calibration with MC Dropout, Deep Ensembles, Temperature Scaling, and Gaussian-process classifiers.

---


### 98. [FedV-KGQA in Practice: Design Lessons and an Interactive Prototype](https://arxiv.org/abs/2609.13661)

**<font color=#1a73e8>作者：</font>** Md Saikat Islam Khan Bappy, Oshani Seneviratne  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graph question answering usually assumes that one system can reach the whole graph. In practice, facts are often held by organizations that share entity identifiers but own disjoint relation types, so no single party sees a complete reasoning chain. This poster presents the empirical findings of FedV-KGQA on multi-hop question answering over such vertically partitioned graphs. Each silo enriches its local graph and trains a knowledge graph embedding on its own triples. A server then concatenates the silo-specific entity views, anchors the projected question at the topic entity, and ranks candidates by similarity. Raw triples and relation embeddings never leave a silo. Comparing the FedV-KGQA experiments with one another yields three results. First, federated fusion recovers most of the centralized accuracy, while a single silo recovers little. Second, anchoring and enrichment matter more than the choice of embedding model. Third, the cheapest encoder depends on the target accuracy rather than on parameter count. This poster paper contributes that cross-experiment comparison, four design lessons drawn from it, and an interactive prototype that runs real inference and traces the full pipeline, per question, on released checkpoints.

---


### 99. [Cost Characterization of Vertically Partitioned Federated Knowledge Graphs](https://arxiv.org/abs/2609.13664)

**<font color=#1a73e8>作者：</font>** Md Saikat Islam Khan Bappy, Oshani Seneviratne  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs are increasingly distributed across autonomous organizations that share an entity space but own disjoint subsets of relations, forming a vertical partition. Answering a multi-hop query may require combining facts from several silos, making the partitioning strategy a key data management decision that affects communication, indexing, load balance, and query latency. However, the costs associated with different partitioning strategies remain insufficiently studied. We formalize vertical partitioning as a design space and compare four strategies: semantic domain grouping, frequency-balanced partitioning, co-occurrence graph-cut partitioning, and random partitioning. We evaluate them using five metrics: communication cost, candidate index size, cross-silo path length, load balance, and end-to-end query latency. Three of the five prove to be determined by the graph and the silo count rather than by the partition, which reduces the design problem to two conflicting axes, cross-silo path length and load balance. Experiments on MetaQA and PathQuestion use a fixed federated knowledge graph question-answering architecture based on TransE embeddings and a frozen BERT encoder across three silo configurations. By keeping the learning model unchanged, we isolate the effect of partitioning and show that the trade-off between locality and balance holds only where each silo can hold several relations, weakening as the number of silos increases. The study provides practical guidance for deployments constrained by cross-silo reasoning or by silo load.

---


### 100. [MARC: Morphology-Aware Regression of Consensus for Cell Segmentation in Subcellular Spatial Transcriptomics](https://arxiv.org/abs/2609.13665)

**<font color=#1a73e8>作者：</font>** Xinyu Shu, Andrew Zhang, Jean Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate cell segmentation remains a major bottleneck in subcellular spatial transcriptomics (SST), in which morphological images and spatially resolved RNA transcripts are used to partition tissues into individual cellular instances. As segmentation serves as the foundation for constructing cell-level representations, boundary errors can lead to incorrect transcript assignments and compromise downstream analyses. However, reliable ground-truth boundaries are unavailable because they must be inferred from incomplete morphological and transcript signals. Furthermore, manual annotation of a large number of cells is time-consuming. Agreement among complementary segmentation methods provides a practical surrogate for identifying well-supported and ambiguous regions, but explicit consensus construction requires executing multiple computationally intensive pipelines. In this study, we propose MARC (Morphology-Aware Regression of Consensus), a framework that predicts a multi-method consensus-support map for SST segmentation. MARC is trained with leave-one-method-out consensus pseudo-targets and a Foreground-Union Consensus Loss that focuses supervision on candidate and consensus foreground. We evaluated MARC on 4,642 held-out tiles from Xenium kidney tissue, achieving a mean Dice score of 0.90, a mean intersection-over-union of 0.82, and a mean cell-level Spearman correlation of 0.79 against explicitly computed cross-method consensus maps. We demonstrate that the predicted consensus maps localise weakly supported regions while preserving consensus-based rankings and identifying low-consensus cells for manual review. These results show that MARC closely approximates explicit cross-method consensus without multi-method inference and therefore has the potential to facilitate robust, consensus-aware evaluation of cell segmentation in large-scale SST studies.

---


> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-416](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
