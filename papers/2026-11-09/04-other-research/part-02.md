# 📦 其他研究 | 2026年11月09日

> 本类共 **237** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-237](./part-05.md)

---

### 51. [Energy Measurement and Optimization of TinyML in Resource-Constrained Embedded Systems: A Systematic Mapping Study](https://arxiv.org/abs/2611.07264)

**<font color=#1a73e8>作者：</font>** Clariele Almeida, Renan Beserra, Rafael Moura 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of the Internet of Things (IoT) has increased the volume of data generated at the network edge, where many devices operate under severe memory, processing, and energy constraints. In this context, Tiny Machine Learning (TinyML) enables machine learning (ML) tasks to be executed on microcontrollers, smart sensors, and other resource-constrained platforms. However, the literature remains heterogeneous regarding the algorithms evaluated, energy-measurement methods, reported metrics, influencing factors, and optimization strategies. This study presents a systematic mapping of energy-aware TinyML research. It identifies the main models and learning approaches, classifies energy-evaluation methodologies and metrics, examines the technical factors affecting energy consumption, and organizes the reported optimization techniques into a structured taxonomy. The findings highlight the frequent use of convolutional and lightweight architectures, direct measurements and analytical estimations, and factors related to model architecture, hardware, communication, numerical precision, and input characteristics. The optimization strategies were grouped into model compression, hardware-aware design, system and communication optimization, and data and processing optimization. The results also reveal limited standardization in experimental platforms, measurement procedures, and reporting practices, limiting reproducibility and direct comparison across studies. This mapping provides an updated overview of the field and guidance for developing and evaluating more energy-efficient TinyML solutions.

---


### 52. [How Deep is the Signal? Time-Context up to 30 Years for Colorectal Cancer Prediction in a Primary-Care EHR Model](https://arxiv.org/abs/2611.07265)

**<font color=#1a73e8>作者：</font>** Achille Raviez, Lan Wang, Brendan Delaney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EHR foundation models read medical events within a fixed context window, and long context has so far been measured only in tokens. How far back in time a model must look to capture the earliest predictive signal is unknown. We introduce time-context, the calendar lookback window before the prediction point, and provide, to our knowledge, the first systematic evaluation of decade-scale time-context for an EHR foundation model. We pretrained a decoder-only transformer (34.6M parameters) on 1.4B coded events from 3.6M primary-care patients in North West London and fine-tuned it to predict incident colorectal cancer under a 12-month pre-diagnostic buffer. A frozen cohort of 1,008 cases and 9,582 matched controls, all registered for at least 30 years, was evaluated at 15 nested lookback windows from 2 to 30 years, so that every truncation is compared within the same patients. Discrimination rose from an AUROC of 0.551 at 2 years to 0.590 at 18 years, then plateaued, with about 80% of the gain reached within 10 years; an XGBoost baseline converged to the same level (peak AUROC 0.589). A simulation further suggests that rotary position embeddings (RoPE) over elapsed time alias beyond about 20 years at the default base frequency, motivating a retuned $\theta$. Time-context is a measurable design axis for clinical prediction models, distinct from token-context, and should be reported.

---


### 53. [Satisficing as competitive Bayesian weighting: a minimal model of goal-directed choice under an unattained target](https://arxiv.org/abs/2611.07270)

**<font color=#1a73e8>作者：</font>** Moto Shinriki, Yu Kono, Tatsuji Takahashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Animals and humans often do not maximize; they act relative to goals (aspiration levels) that are frequently not yet met. How can a goal that is not (yet) realized organize choice? Deacon (2012) calls such absence-referenced organization \emph{ententional}, and García-Valdecasas and Deacon (2024) argue that ends are best understood as constraints rather than as particular states. We examine this idea in a minimal formal setting: Risk-sensitive Satisficing (RS), a bandit learning rule that values each action by its share of past trials multiplied by its surplus or shortfall relative to an aspiration level. We show that RS can be rewritten as a Bayesian-like estimator, Attention Competitive Bayes (ACB), in which the aspiration level is the prior mean of every action and the finite budget of trials sets how strongly evidence can override it. Two consequences follow. First, actions that are no longer sampled are partially overridden by the goal rather than by past observations: their estimates relax toward the aspiration level without any data being discarded. This ``pseudo-forgetting'' distinguishes ACB from models with an explicit forgetting rate. Second, when the aspiration is unattainable, exploration does not settle; in Bernoulli bandit simulations, adjusting the aspiration level from evidence reduced regret (expected loss). ACB offers an analyzable model in which an unattained goal and a limited attentional resource jointly constrain behavior, and it yields testable predictions about how organisms revalue options they have abandoned.

---


### 54. [Graph Neural Networks for Resource Allocation in Integrated Sensing and Communication](https://arxiv.org/abs/2611.07277)

**<font color=#1a73e8>作者：</font>** Junyu Liao, Lili Chen, Tian Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In vehicular integrated sensing and communication (ISAC) networks, each service-provider vehicle uses a limited power budget to serve multiple sensing targets and communication receivers. Maximizing the communication sum-rate subject to sensing signal-to-interference-plus-noise ratio (SINR) constraints is nonconvex, and iterative optimization is costly to rerun for every network layout. This paper proposes a graph neural network (GNN)-based power allocation algorithm, termed GNN-ISAC. Concretely, GNN-ISAC addresses the aforementioned problem by considering two distinct edge types in the graph representation, one capturing the inter-provider interference, the other representing the intra-provider power-budget sharing. GNN-ISAC is trained without labels using a sensing-penalized sum-rate loss. We also adapt the weighted mean-square error minimization (WMMSE) algorithm to this problem by introducing a sensing-power reservation step. Simulation results show that GNN-ISAC achieves communication sum-rates close to WMMSE with low sensing-link violation rates and much less computation. It also outperforms an existing heterogeneous GNN and a channel-blind baseline, and generalizes to larger networks without retraining.

---


### 55. [Scenario Augmentation for Rare Financial Events via Multimodal Latent Diffusion](https://arxiv.org/abs/2611.07282)

**<font color=#1a73e8>作者：</font>** Mahdi Arab Loodaricheh, Anita Raja, Indranil SenGupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extreme market movements are scarce, heterogeneous, and difficult to learn from imbalanced historical data. We study whether generative augmentation can improve the representation and classification of CVaR-labeled rare financial windows while retaining the complementary structure exposed by different financial representations. Each market window is expressed through three aligned modalities: structured market variables, a spatial image transformation, and a sequence of portfolio returns. Separate variational autoencoders map the modalities to compact latent codes, and a class-conditional diffusion model learns their joint latent distribution. Conditional Value-at-Risk (CVaR) provides a risk-aware definition of rare windows and directs generation toward the minority regime. Across four window lengths on U.S. technology equities, the resulting synthetic samples improve fidelity and support relative to tabular diffusion baselines. An XGBoost classifier trained with real and generated samples attains AUCs of 0.953 - 0.960, exceeding both tabular generators and the corresponding real-only baselines. These results show that multimodal latent generation can provide useful synthetic stress scenarios for data-scarce financial risk models.

---


### 56. [Householder Motion Embedding: Noise Modulation for Motion-Controllable Video Generation](https://arxiv.org/abs/2611.07294)

**<font color=#1a73e8>作者：</font>** Tao Jun Lin, Jinhong Ni, Ruyi Zha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models for video generation have achieved remarkable success, yet precise motion control under explicit user guidance remains challenging. Recent noise-warping methods introduce temporal correlations by warping the noise according to the user-provided motion signal. However, standard spatial warping generally disrupts the noise's i.i.d. Gaussian structure, requiring distribution correction, such as Jacobian-based correction, but at a substantial computational overhead. We propose Householder Motion Embedding (HME), which encodes the motion signal into the noise through a sequence of Householder reflections that together form an orthogonal transformation applied to each location's channel vector. HME exactly preserves the spatial Gaussian structure within each frame while introducing cross-frame correlations that promote temporally consistent video. HME is agnostic to the network architecture and integrates directly into standard video diffusion fine-tuning pipelines. Experiments on different scenarios show that HME matches or outperforms the state of the art, while achieving a 2.7x speedup over noise warping. These results demonstrate that channel-space Householder transformations offer a principled and efficient alternative to noise warping for motion-controllable video generation.

---


### 57. [Provably Efficient Representation Learning for Low-Rank CMDPs](https://arxiv.org/abs/2611.07295)

**<font color=#1a73e8>作者：</font>** Kaixuan Liu, Guojun Xiong, Shengpu Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study representation learning in low-rank Constrained Markov Decision Processes (CMDPs), where both value and reward functions are approximated by a set of unknown representation vectors, and the transition dynamics admit a low-rank factorization. The objective is to maximize expected cumulative rewards while complying with constraints on the expected cumulative utility. To achieve this, we propose \texttt{MFRLC} (Model-Free Representation Learning for Low-Rank CMDP), a model-free algorithm that uses a primal-dual scheme to effectively balance reward regret and constraint violations. To the best of our knowledge, \texttt{MFRLC} is the first representation-learning method for low-rank CMDPs that combines the Least-Squares Value Iteration with Upper Confidence Bound (LSVI-UCB) and primal-dual techniques. \texttt{MFRLC} further enhances value function estimation with bonuses for function approximation and learns the mapping from representations to value functions directly, avoiding explicit estimation of the transition kernel. We prove that, with high probability, \texttt{MFRLC} achieves $\widetilde O(K^{3/4})$ reward regret and cumulative constraint violation over $K$ deployment rounds, independent of the size of the state space. To our knowledge, these are the first sublinear regret and violation guarantees for CMDPs with unknown features.

---


### 58. [Robust Ranking of Port Impacts from Impending Tropical Cyclones: A Two-Stage Recommendation System](https://arxiv.org/abs/2611.07296)

**<font color=#1a73e8>作者：</font>** Chenchen Kuai, Shixuan Tang, Chaolun Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a tropical cyclone (TC) threatens several ports, preparedness planning depends on anticipating which ports are likely to be affected and where disruptions may last longest. Limited historical observations at individual ports and uncertainty in landfall location make these relative impacts difficult to estimate. We use a two-stage recommendation framework that first selects candidate ports based on their proximity to the expected landfall location and then ranks them by their estimated number of impact days. Using AIS-derived impact days for 37 ports and 31 TCs in the Gulf of Mexico study region, we compare three ways of representing port--cyclone interactions: pairwise feature interactions, tree-based feature combinations, and explicit feature crosses combined with learned embeddings. In tests on Hurricanes Nicole and Ian, the retrieval stage consistently identifies all observed affected ports under landfall uncertainty. Among the ranking models, Wide & Deep Learning achieves the closest agreement with the observed port rankings. Its mean ranking agreement exceeds that of the distance-based baseline by 85.5% for Nicole and 55.5% for Ian and is less sensitive to uncertainty in the landfall location. These rankings could help port authorities prioritize post-cyclone inspections and allocate recovery resources across ports threatened by the same event.

---


### 59. [ArtiVidRM: Verifiable Artifact-as-Rubric Reward Modeling for Explicit Quality Articulation in Video Generation](https://arxiv.org/abs/2611.07301)

**<font color=#1a73e8>作者：</font>** Caorui Li, Yangguang Ji, Shuxia Lin 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become an effective approach for improving video generation, but its success depends heavily on reliable reward models. Existing methods either map videos directly to opaque scalar scores or generate free-form rationales that are not explicitly optimized as the basis of the final judgment. We propose ArtiVidRM, a verifiable, artifact-as-rubrics video reward model that follows an observe-then-score paradigm. It first identifies visible generation artifacts and organizes them into a structured artifact list, then uses these artifacts as explicit rubrics for quality assessment. This intermediate representation grounds each score in concrete video-level evidence, making the reward more interpretable and informative for optimization. We further introduce a multi-reward reinforcement learning strategy to jointly optimize artifact prediction and quality assessment. The reward decomposes into complementary objectives that evaluate artifact prediction quality, including semantic coverage and prediction efficiency, together with a pairwise preference objective that supervises quality ranking through score differences. By jointly optimizing the intermediate artifact representation and the downstream preference prediction, the model learns to produce informative artifact lists while improving the accuracy of video quality assessment. Experiments show that ArtiVidRM achieves state-of-the-art performance on video preference benchmarks, provides effective signals for video diffusion optimization, and enables artifact-guided refinement of closed-source video generators.

---


### 60. [Permanent and Transient Representations for Continual Reinforcement Learning](https://arxiv.org/abs/2611.07327)

**<font color=#1a73e8>作者：</font>** Nishanth Anand, Doina Precup  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual Reinforcement Learning (CRL) agents struggle to adapt to new situations while retaining prior knowledge, leading to a stability-plasticity trade-off. One approach to solving this problem is by using complementary learning systems: one for slow, long-term learning and another for quick, transient adaptation. Anand & Precup (2023) instantiated this idea using permanent and transient value functions, but used the same features in both systems. Intuitively, long-term learning should rely more on parametric representations for broad generalization, while transient learning would be best served by non-parametric representations for situation-specific adaptation. In this paper, we explore this idea both theoretically and empirically. By introducing a novel non-parametric approximation for estimating the transient value function in complex tasks, we demonstrate that our method enables online learning and outperforms competitive baselines on image-based tasks and Craftax-Classic, underscoring the effectiveness of our system-level decomposition.

---


### 61. [Slide to Report: Continuous Reporting Symptom-Specific Cybersickness in VR](https://arxiv.org/abs/2611.07345)

**<font color=#1a73e8>作者：</font>** Purnata Saha, Rifatul Islam, Qiliang He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cybersickness is often assessed during VR exposure through discrete overall sickness, which cannot capture specific symptoms or their changes over time. Post-exposure questionnaires such as the Simulator Sickness Questionnaire provide symptom-specific measures but cannot be collected during immersion. We investigate whether separating cybersickness into three symptom-specific dimensions -- nausea, oculomotor discomfort, and disorientation -- during immersion provides more informative continuous measurements. We conducted a between-subjects study with 52 participants in a VR-rollercoaster, comparing a three-slider interface with a single-slider interface. Concurrently, participants also completed an auditory Simon task to measure attention. We additionally collected multimodal set of physiological signals, including GSR, ECG, PPG, eye and head tracking. Results show that each slider correlated most strongly with its corresponding SSQ subscale, whereas the single slider correlated with all SSQ subscales. Using three sliders did not significantly affect usability, workload, or attention. We publicly release the multimodal dataset to support future cybersickness research.

---


### 62. [AtlasULP: Domain-aware Universal Link Prediction via Relation Atlas](https://arxiv.org/abs/2611.07347)

**<font color=#1a73e8>作者：</font>** Yujing Liu, Yixin Liu, Yu Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Link prediction (LP) is a widely applied task in graph learning. Conventional LP approaches typically follow a dataset-specific paradigm, requiring independent training for each graph and incurring high computational and maintenance costs in large-scale applications. Motivated by these limitations, recent work explores Universal Link Prediction (ULP), aiming to enable training-free inference on arbitrary unseen graphs. However, existing methods primarily rely on subgraph sampling strategies to construct universal representations, which are unable to capture higher-order information due to the exponential growth of higher-order neighborhoods. As a result, they often under-perform on graphs where long-range signals are essential, such as biological networks. Moreover, their prediction models are typically domain-agnostic and lack the ability to adapt to different graph domains, leading to limited generalization. To address these challenges, we propose an Atlas-based Universal Link Prediction framework (AtlasULP), which introduces the relation atlas to capture structural associations between node pairs from both global and local perspectives, enabling a comprehensive characterization of connectivity signals across diverse graph domains. Building upon this representation, we develop a domain-guided prompting ULP model, which generates domain-aware prompt tokens from contextual structures and performs prompt-guided in-context prediction for adaptive link inference. Extensive experiments demonstrate that AtlasULP consistently outperforms state-of-the-art methods across diverse graph domains.

---


### 63. [MIKU: Material Invariance and Knowledge Unification for PBR Generation](https://arxiv.org/abs/2611.07354)

**<font color=#1a73e8>作者：</font>** Yajie Bao, Jiaye Fu, Youtian Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality material generation for physically based rendering (PBR) remains challenging because datasets and synthesis pipelines lack standardized representations. Differences in material definitions, rendering conventions, and parameterizations lead to unstable and physically implausible results. We propose MIKU, a unified framework for standardized PBR asset representation and physically consistent material generation across diverse 3D content domains. Its core is a unified processing pipeline that standardizes the workflow from data preprocessing to final texture synthesis, maintaining consistent geometry and texture representations. A normalization scheme harmonizes heterogeneous material parameterizations in a common representation space, enabling robust cross-dataset training and inference. Building on this formulation, we train a novel physically aware diffusion model for PBR texture generation within a two-stage multi-view synthesis framework. First, geometry-aware albedo generation synthesizes multi-view albedo maps under explicit geometric guidance to ensure cross-view appearance consistency. Second, metallic-roughness generation uses the diffusion model to predict physically plausible roughness and metallic maps conditioned on the generated albedo and unified representation. Trained end-to-end on standardized data, the model learns to generate materials that respect category-level material priors and semantic part boundaries. By decoupling representation standardization from appearance synthesis, MIKU substantially improves material generation stability and physical consistency. Extensive experiments demonstrate state-of-the-art texture quality and semantic consistency across object parts, advancing automated material generation for 3D content creation.

---


### 64. [Acoustic Anomaly Detection for Early Identification of Drill Jamming](https://arxiv.org/abs/2611.07356)

**<font color=#1a73e8>作者：</font>** Maria Beatriz Silva, Lucas Edson Silva de Araújo, Sergio F. Chevtchenko 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the context of Industry 4.0, predictive maintenance is essential to minimize unplanned downtime and ensure operational safety. In machining processes, drill jamming is a critical failure that compromises both workpiece quality and tool integrity. This work proposes an acoustic anomaly detection system using ultrasonic sensors to identify pre-failure patterns in Computer Numerical Control (CNC) machining. We release a public dataset of time- and frequency-domain acoustic features from 17 drills, and benchmark semi-supervised autoencoder-based normality modelling against supervised XGBoost classification using Leave-One-Drill-Out validation. The results demonstrate that the Autoencoder is highly effective for industrial safety, achieving a Recall of 1.00 and a consolidated F1-score of 0.81. Furthermore, the threshold-independent analysis shows that the Autoencoder better separates normal and pre-failure acoustic patterns, achieving a consolidated AUC of 0.8294, compared with 0.7559 for the supervised model under inter-tool covariate shift. In contrast, the supervised XGBoost achieved an average F1-score of 0.55 and failed to detect failures in some of the evaluated drills. The findings highlight that the ultrasonic spectrum provides a reliable window for identifying incipient mechanical instabilities, and the AE model offers a robust safety envelope by anticipating all jamming events across the tested drill bits.

---


### 65. [Breaking $\mathsf{TraintoDefend}$ via Adaptive Neuron Clustering in Cryptanalytic Model Extraction](https://arxiv.org/abs/2611.07370)

**<font color=#1a73e8>作者：</font>** Haojie Wu, Haolin Liu, Tianshuo Cong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptanalytic model extraction poses a fundamental threat to deep learning model confidentiality by enabling precise parameter recovery with theoretical guarantees of functional equivalence. To counter this growing threat, $\mathsf{TraintoDefend}$ (NeurIPS 2025) was proposed as the first dedicated defense against cryptanalytic extraction and remains the only defense believed to be effective to date. It encourages neurons to learn similar weights so that they switch activation states together, making their individual contributions harder to distinguish. However, we notice that neurons with similar weights need not switch activation states together under small perturbations. Instead, weight similarity can cause the original clustering rule to merge signatures from distinct neurons when only a subset of their normalized weight coordinates agree. Motivated by this observation, we introduce $\mathsf{SimBreak}$, an adaptive clustering rule that breaks the weight-similarity defense of $\mathsf{TraintoDefend}$. $\mathsf{SimBreak}$ estimates a relative scale from all jointly observed weight coordinates and uses the same scale to test both weight direction and bias consistency. Across six protected fully connected networks trained on MNIST, $\mathsf{SimBreak}$ raises target layer signature recovery from $0\%$ to $100\%$, with a maximum relative recovery error of $2^{-22.27}$. Our work challenges the use of neuron weight similarity as a sufficient basis for protection and establishes adaptive evaluation as essential to assessing cryptanalytic extraction defenses.

---


### 66. [Design of Multi-UAV Cooperative Deep Semantic Autoencoders for Communication Networks](https://arxiv.org/abs/2611.07374)

**<font color=#1a73e8>作者：</font>** Xiaoling Han, Bin Lin, Nan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Driven by the rapid development of the low-altitude economy, Uncrewed Aerial Vehicle (UAV) networks have become increasingly important for executing tasks such as search, rescue, and monitoring. However, under bandwidth-constrained scenarios, UAV networks still face significant challenges in task execution efficiency and intelligent processing capabilities. To address these issues, we propose Multi-UAV Cooperative Deep Semantic Autoencoders (MC-DSA) for communication networks. The architecture comprises one Task UAV (T-UAV) and multiple Support UAVs (S-UAVs), which jointly enhance communication efficiency and data-processing capability via semantic communication and cooperation. Specifically, we introduce a semantic matching and source selection mechanism, enabling the proposed MC-DSA to handle low-quality images while ensuring effective utilization of high-quality images. The T-UAV broadcasts a task query, and each S-UAV computes the semantic similarity between its local image and the query. Communication links are established only when the similarity exceeds a predefined threshold. The training algorithm optimizes network parameters through gradient descent, improving semantic feature extraction accuracy. The testing algorithm evaluates UAV collaboration efficiency and communication quality. Experimental results demonstrate that, compared with benchmarks, the proposed MC-DSA improves image semantic segmentation accuracy while maintaining task execution efficiency. As a result, it reduces redundant transmissions and offers an effective solution for multi-UAV communication networks.

---


### 67. [When Scores Conflict with Preferences: Pre-Alignment Diagnosis and Adaptive Correction of Constraint Drift in DPO](https://arxiv.org/abs/2611.07375)

**<font color=#1a73e8>作者：</font>** Ping Liu, Yan Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) is increasingly used in settings where pairwise preferences coexist with pointwise criteria such as response length, answer correctness, or safety scores. When the two disagree, standard DPO treats pairs whose preferred output scores worse on the pointwise criterion (conflict pairs) in the same way as the remaining (matching) pairs. We characterize a systematic failure mode, constraint drift: for sufficiently small updates, conflict pairs tend to increase constraint cost while matching pairs tend to repair it, and the net change depends on their balance. This balance yields a closed-form pre-alignment diagnostic, $\rho^{*}_{\mathrm{eq}}$, computable from dataset statistics, that indicates whether a dataset is self-correcting or requires intervention. Building on this diagnostic, we propose Conflict-aware DPO (CoDPO), which down-weights conflict pairs with a strength set from $\rho^{*}_{\mathrm{eq}}$ rather than tuned, and adds an adaptive margin shift that addresses residual drift during training. Empirically, drift grows monotonically with conflict exposure on the conflict-dominated domains, and the intervention decision given by $\rho^{*}_{\mathrm{eq}}$ matches the observed drift on every domain, including one that it identifies as self-correcting. On all four domains of the main comparison, CoDPO reduces drift while largely preserving the preference learning of vanilla DPO. Compared with hard filtering and recent constrained and multi-objective baselines, CoDPO also achieves a more favorable drift-preference trade-off.

---


### 68. [Designing with Cinematic Language: An Intent-Driven Approach to Human-AI Video Clip Co-Creation](https://arxiv.org/abs/2611.07377)

**<font color=#1a73e8>作者：</font>** Yi He, Zhengxi Yu, Feilin Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Generative video models have made video creation more accessible, yet creators still struggle to translate high-level narrative intentions into coherent cinematic expressions. Existing systems primarily rely on prompt refinement or expose isolated camera controls, leaving a gap between what to express and how to film it. We present CineAssist, a human-AI co-creation system that treats cinematic language as an interactive design medium connecting creative intentions with executable video controls. We construct a Cinematic Language Design Space and an annotated dataset from 107 filmmaking sources and 1,436 film clips, linking communicative intentions to cinematic parameter values. CineAssist combines a multi-agent workflow for intent alignment and strategy recommendation with an interactive cinematic editor and a context-sensitive preference learner for user-controlled personalization. We evaluate the system through three studies examining end-to-end usability, cinematic quality, and preference evolution. Results show that CineAssist facilitates efficient, controllable, and personalized intent-driven cinematic video creation.

---


### 69. [Breaking the Modality Barrier: Multimodal Fusion With Missing Modalities for Cybersickness Prediction](https://arxiv.org/abs/2611.07386)

**<font color=#1a73e8>作者：</font>** Purnata Saha, Rifatul Islam, John Quarles  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cybersickness is a major barrier to comfortable VR use, and reliable prediction often requires multiple physiological and behavioral sensors. However, existing models typically assume a fixed set of modalities, making them vulnerable when sensors are unavailable and difficult to generalize across datasets with different sensor configurations. We adapt a transformer-based model that handles arbitrary sensor combinations without imputing missing data. Anchor-based contrastive learning maps heterogeneous sensor embeddings into a shared latent space using eye tracking as the anchor modality, while masked self-attention excludes unavailable sensors during fusion. We evaluate our approach on three publicly available cybersickness datasets: this http URL, SIM21, and Blur-Rollercoaster, collected using different VR systems and sensor configurations. Across single-sensor dropout conditions, prediction error changes by less than 0.09 MAE. Joint training across all datasets achieves 0.51 MAE and 0.63 Pearson correlation, substantially outperforming single-dataset models. These results demonstrate robust and generalizable cybersickness prediction across diverse VR systems.

---


### 70. [Vis2State: Visual Reasoning through Executable State Abstractions](https://arxiv.org/abs/2611.07397)

**<font color=#1a73e8>作者：</font>** Sheng Jin, Wentao Liu, Chen Qian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Solving visual puzzles requires both accurate interpretation of visual evidence and reliable computation under task-specific rules. Embedding visual assumptions and task constraints directly in solving code makes the represented problem difficult to inspect and revise independently. We introduce Vis2State, a training-free agentic framework that abstracts visual puzzles into explicit, revisable problem states linking visual inspection and execution. Visual inspection guides state construction and refinement, while generated programs solve the represented problem. The model constructs both the state and the program without predefined puzzle schemas or solving procedures. Inspection and execution feedback allow it to revise the problem representation and solving procedure independently. Vis2State achieves the state-of-the-art performance on four benchmarks. Cross-model evaluation further demonstrates consistent gains. Ablations, error analyses, and fixed-program state interventions further support the effectiveness of the state-centered design. The code will be made publicly available to facilitate future research.

---


### 71. [FreePath: Neural Mean Free Path for Image Dehazing](https://arxiv.org/abs/2611.07398)

**<font color=#1a73e8>作者：</font>** Rongrong Gao, Jingxuan Feng, Wenyu Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single image dehazing requires recovering scene radiance from visual responses that are weakened and veiled by participating media. Existing methods either invert explicit scattering variables, which can be unstable under complex scenes, or learn direct restoration mappings, which often discard the physical organization of haze formation. We present \emph{FreePath}, a neural mean free path framework for image dehazing. Instead of estimating atmospheric parameters, FreePath represents dehazing as feature space path state restoration, inspired by the expected distance a visual response can propagate before interacting with haze. Within a residual encoder and decoder, the Mean Free Path Residual Block learns path and collision fields to guide haze constrained correction, while FreePath State Conservation Integration preserves restored path states during deep feature aggregation. Experiments on paired CDD-11 haze images and real RTTS scenes show that FreePath consistently improves full reference fidelity, no reference perceptual quality, and visual faithfulness over representative dehazing baselines.

---


### 72. [Spectral symmetry fingerprints in equivariant representations](https://arxiv.org/abs/2611.07410)

**<font color=#1a73e8>作者：</font>** Jiacheng Cen, Anyi Li, Ning Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symmetry governs the organization of physical structures, while symmetry breaking reveals their transformations. In geometric deep learning, symmetry imposes rank constraints on equivariant representations, limiting the expressive capacity of equivariant graph neural networks (GNNs). Here we show that these constraints can instead be exploited: the singular-value spectra of equivariant representations provide a unified fingerprint of structural symmetry. We introduce spectral symmetry fingerprints (SymFP), which enable discrete point-group identification through rank-template matching and continuous symmetry analysis by quantifying spectral energy beyond target rank constraints. SymFP is orientation invariant and architecture agnostic, enabling a parameter-free GNN implementation. Its spectra can be reused across multiple target groups, and the resulting leakage scores satisfy subgroup monotonicity. Across synthetic structures, molecules, coordination complexes and large biological assemblies, SymFP accurately identifies point groups, tracks controlled symmetry breaking and reveals local and degree-resolved symmetry changes that can be obscured by global geometric measures. These results establish the spectral structure of equivariant representations as a general framework for characterizing symmetry across physical systems.

---


### 73. [TRiST: Topology-Reinforced Swin Transformer for Medical Image Analysis](https://arxiv.org/abs/2611.07431)

**<font color=#1a73e8>作者：</font>** Pengfei Gu, Huimin Li, Guangyu Meng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical images contain topological patterns, such as connected components and loops, at scales ranging from small lesions to organ boundaries. Although hierarchical Vision Transformers have advanced medical image analysis, they do not explicitly incorporate topology throughout their multiscale representations. We propose Topology-Reinforced Swin Transformer (TRiST), a framework that integrates topological information into feature construction, refinement, and attention. First, a Hierarchical Multi-Scale Topology Representation algorithm computes 2D persistent homology (H0 and H1) independently at four native Swin stages, producing descriptors aligned with each stage's token grid rather than downsampling fine-scale topology. Second, a Band-Aware H0/H1 Residual Refinement module uses gated residual networks to process short-, medium-, and long-persistence information separately. Third, a Persistence-Band Progressive Attention Bias converts stage-specific descriptors into learned key-saliency scores that directly modify shifted-window attention logits. We instantiate TRiST as Topo-SwinV2-B for classification and Topo-Swin-UNet for segmentation, preserving the underlying Swin-based backbones. Experiments on five medical image datasets show consistent improvements over Swin-based baselines and competitive performance relative to existing topology-augmented methods.

---


### 74. [VIPA: View-Invariant Projector-Based Adversarial Attack](https://arxiv.org/abs/2611.07443)

**<font color=#1a73e8>作者：</font>** Jiyu Han, Qingyue Deng, Bingyao Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Projector-based adversarial attack aims to physically manipulate real-world scenes by projecting adversarial patterns, thereby causing deep image classifiers to produce incorrect predictions. However, existing stealthy projector-based adversarial attack methods model the project-and-capture process in a single and static view, limiting their view-invariant capability and practical applicability in dynamic environments. In this paper, we introduce View-Invariant Projector-Based Adversarial Attack (VIPA), a novel method designed to overcome these limitations by achieving both view-invariant and classifier-agnostic adversarial attacks in the physical world. We first leverage a view-invariant projector-camera system simulation method to model the physical interactions between projected patterns and real-world surfaces. To ensure robustness and stealthiness of the attack across different views, VIPA optimizes adversarial projections by aggregating simulated attack losses from multiple views. This joint optimization across diverse views helps maintain robustness regardless of the viewpoints. Finally, the optimized patterns are physically projected into real-world scenes, where they successfully fool various classifiers from different viewpoints, thereby enabling robust and practical view-invariant adversarial attacks. Our experiments in both targeted and untargeted attacks demonstrate that VIPA consistently achieves higher attack success rates than existing methods, while also enhancing stealthiness and ensuring minimal perceptual degradation across all tested views.

---


### 75. [Two-stage residual learning for calibrated uncertainty in solar irradiance forecasts](https://arxiv.org/abs/2611.07444)

**<font color=#1a73e8>作者：</font>** RR Flanagan, E Kasha, PW Talbot 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of renewable generation requires not only point predictions but also reliable estimates of the uncertainty attached to them, particularly at extended horizons. Machine learning models are increasingly used to predict solar output, but they typically report a single value and capture the associated uncertainty poorly. The standard remedy is to train a model to predict the parameters of an assumed probability distribution directly. Here we develop an alternative two-stage method, motivated by synthetic solar signal generation, in which the forecast error is modeled separately from the expected irradiance. A first long short-term memory (LSTM) network predicts the expected global horizontal irradiance, and a second network models the distribution of the forecast error, which is added back to the mean to give both the forecast and its uncertainty. Using historical weather data from the National Solar Radiation Database and a probability integral transform evaluation, we show that explicitly modeling the error brings the predicted standard deviation markedly closer to the historical value, reducing the deviation between the two by 34.6 percent for a standalone LSTM and by 56.5 percent when the LSTM is coupled to Gaussian process regression, the most reliable of the configurations tested. Because the method models the total forecast error directly, it captures the full predictive uncertainty that matters for decisions, rather than only the model contribution that dropout-based approaches estimate.

---


### 76. [Recursive Self-Improvement for Long-Horizon Role-Playing Dialogue](https://arxiv.org/abs/2611.07469)

**<font color=#1a73e8>作者：</font>** Y. L. Li, Y. H. Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon role-playing dialogue requires consistent character identity, reliable memory, and context-sensitive interaction. We present a bounded recursive self-improvement (RSI) framework that revises original-character memory, stable persona instructions, and a policy for constructing turn-level prompts. Repair outcomes also inform revisions to the updater's diagnostic rules, edit routing, and candidate selection. We specify the updater as a versioned policy with explicit inputs, editable fields, acceptance gates, and stopping conditions. An internal evaluation covers 50 original characters and five models, with two 100-round conversations per character-model pair: 500 conversations per condition. Across the pooled evaluated replies, the bad-response rate decreases from 14.00% (6,973/49,824) to 4.94% (2,459/49,793), a 9.06-percentage-point reduction and a 64.71% relative reduction. In 600 blinded human comparisons, RSI receives 294 wins, 187 ties, and 119 losses, yielding a 71.19% win rate among decisive judgments. The results support improved aggregate dialogue quality for the complete framework on the internal test distribution.

---


### 77. [Echoes of Error: Residual-Directional Local Rollout Consistency for Timeseries Forecasting](https://arxiv.org/abs/2611.07473)

**<font color=#1a73e8>作者：</font>** Zheng Wang, Kaixuan Zhang, Xiaonan Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In time-series forecasting, rollout errors are not merely one-step fitting discrepancies: once fed back into the evolving state, they can perturb future predictions. We formalize this effect through local rollout consistency, which compares the next prediction produced under teacher forcing with that produced under free running. In principle, this consistency can be enforced directly by tracking the residual-induced perturbation of the next state. In practice, however, the residual-to-state alignment operator is often difficult to design when the input state and output block have different dimensions, heterogeneous components, or architecture-dependent layouts. We therefore use a first-order local surrogate that penalizes the Jacobian-vector product of the predictor along the actual feedback perturbation, suppressing precisely the directions through which self-generated errors remain visible to future predictions. We further give the same loss a geometric interpretation near a predictive manifold: by controlling residual-induced directions that probe the normal bundle, the objective yields theoretical conditions under which free-running trajectories remain inside a stability tube around the manifold. Experiments on time series forecasting tasks support this view, showing that the proposed regularization improves predictive accuracy. More broadly, our results suggest a training principle for time-series forecasters and sequential predictors: a model should not only make small one-step errors, but also learn not to let its own errors echo into the future. Code is available at this https URL.

---


### 78. [Adversarial Robustness of Kernel Machines: A Comprehensive Analysis](https://arxiv.org/abs/2611.07474)

**<font color=#1a73e8>作者：</font>** Rahul Kumar Yadav, Tunir Ghosh, Sudhendu Ahir 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernel machines are an important class of models in machine learning. However, the question of how robust modern kernel machines are to adversarial examples has not been studied comprehensively. In this paper, we provide a thorough empirical investigation of the adversarial robustness of kernel-based models for both binary and multiclass classification tasks, via white-box and black-box evasion attacks. We evaluate the native robustness of kernel machines, random feature classifiers, and the relatively newer Recursive Feature Machines. In addition, we provide an algorithm for approximate adversarial training of kernel machines. Our experiments on classification tasks on image and tabular datasets strongly indicate that kernel machines are natively more robust than neural networks, i.e., their performance degrades more gracefully against adversarial perturbations.

---


### 79. [AMORT-V1: Checkpointed Post-Quantum Attestation for Industrial Controllers](https://arxiv.org/abs/2611.07476)

**<font color=#1a73e8>作者：</font>** Rishabh Das, Gerald Agendia, Jibriel Adjei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Programmable logic controllers often remain deployed for decades, making post-quantum attestation a long-term requirement. Prior measurements of OpenPLC attestation show that post-quantum signing can consume 88--99% of round-trip latency and that durable state can further limit throughput. We introduce AMORT-V1, a checkpointed attestation protocol that moves public-key signing and durable commitment from individual reports to periodic checkpoints. An ML-KEM epoch establishes per-device evidence keys, devices authenticate reports with MACs, and the controller commits ordered evidence through hash-chained Merkle checkpoints signed with ML-DSA or SLH-DSA. Because shared MACs do not provide transferable proof of device origin, AMORT-V1 adds a device-held disclosure chain whose keys are released after checkpoint commitment. We validate the protocol with a 27-case attack matrix, 149 differential-test vectors, and a seven-node Raspberry Pi 5 testbed with five physical OpenPLC provers. Checkpointing reduces controller cost by 90 times relative to per-report ML-DSA without durable logging and by 878 times when durable logging is required. Transferable device-origin verification costs 2.95micro sec per report, while controller-side scaling to 10,000 identities requires 6.18 micro sec and 155 octets per report. AMORT-V1 also supports rollback-resistant restart through TPM-backed monotonic state without placing durable hardware operations on the per-report path.

---


### 80. [Compact Motion Embeddings for Feed-forward Unified Human Animation](https://arxiv.org/abs/2611.07481)

**<font color=#1a73e8>作者：</font>** Seonwook Park, Hyunsoo Cha, Amrita Mazumdar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Animating a reference image with a driver's motion requires a motion representation that captures face, hand, and body articulation but excludes the driver's appearance. Most body animation methods take motion from external pose estimators and render it with many denoising steps; compact learned motion representations mostly cover the face. We present FUHA, a real-time-capable feed-forward transformer that learns a compact motion embedding of the whole human and uses it for face, upper-body, and full-body animation. A Q-Former compresses the driver's features from a frozen visual encoder into this embedding. To disentangle motion from appearance, a novel contrastive loss pulls it toward the motion embedding of the driver's rendered keypoint image and away from that of the same person in another pose. At inference time, FUHA needs no external pose estimators, keypoints, or parametric body models. As a retrieval key, the motion embedding matches body pose better than the learned global embeddings of ten vision encoders. Its same-person retrieval rate is 0.1%, against 9.5% for its own DINOv3 backbone. On our upper-body benchmark, FUHA outperforms all baselines on every self-reenactment metric and on cross-reenactment identity similarity. It is competitive on face and full-body and runs at up to 38.9 FPS at 512x512 on a single RTX 4090.

---


### 81. [Degree-Equalized View-Graph Selection under Tight Pair Budgets](https://arxiv.org/abs/2611.07498)

**<font color=#1a73e8>作者：</font>** Minhyeok Im, Jongseong Brad Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fully matching all image pairs in Structure-from-Motion is quadratic in the number of images, so practical pipelines pass a budgeted subset to the final matching and reconstruction backend. One-shot selectors score candidates with image retrieval, cheap geometric probes, or a learned prior and finalize B pairs before full matching. Their priorities do not account for the degree already allocated to each image, which can concentrate edges on a few images. Across nine large 1DSfM internet photo collections at B=2N, the coverage top-B selector leaves 54% of covered images with realized degree at most two. Reconstruction can then fail even when the selected graph is nearly connected and almost fully verified. Our training-free greedy rule, Degree-Equalized Allocation (DEAL), exponentially downweights pairs whose endpoints are already well covered. On these collections, DEAL improves the one-shot selector built on the same prior (from 0.776 to 0.929) and matches the mean registered-image ratio of an SfM-supervised edge prior under the shared backend (0.929 vs 0.930), without training. On the largely saturated 38-scene standard benchmark suite, DEAL gives the highest mean among the evaluated training-free selectors (0.875 vs 0.858 one-shot).

---


### 82. [RLGPA: A Reinforcement Learning-Guided Granularity Planning Attack for Decision-Based Sparse Adversarial Examples](https://arxiv.org/abs/2611.07512)

**<font color=#1a73e8>作者：</font>** Chao Zhou, Shenghua He, Jiaxin Mo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-based sparse attacks must reduce perturbation support using only the victim's predicted label. The best restoration strategy varies as support contracts: coarse removal works early, while tail states need finer, history-aware tests. We propose RLGPA, an online reinforcement learning method that schedules support-reduction executors and their granularity under a hard query budget. A masked Dueling Double DQN selects among seven stable policy--scale actions; each action produces support-relative restoration groups that are rebuilt after every macro decision. A feasibility-preserving executor commits only adversarial restorations and feeds support gain and query cost back to the planner. Under the matched top-1-label oracle, RLGPA reaches 61\% targeted ASR at sparsity 0.01 on CIFAR-10 (vs. 25\% SparseEvo, 0\% Pointwise), and 75.5\%/73.0\% on ResNet50/ViT at sparsity 0.005 (vs. 29.0\%/15.5\%). A fixed-probe test reduces median \(L_0\) from 165 to 23 after 40 images without any update. State-blind and state-shuffled controls degrade significantly, confirming that the learned policy uses attack state; the main gains come from state-conditioned executor scheduling and dynamic repartition. The source code is publicly available at this https URL.

---


### 83. [Graph learning-assisted logic-based Benders decomposition for distributionally robust in-station train rescheduling under disruptions](https://arxiv.org/abs/2611.07520)

**<font color=#1a73e8>作者：</font>** Xiaobin Li, Yanbin Gao, Jianing Long 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Uncertainty in resource reopening times complicates train holding and rerouting decisions when resource closures coincide with arrival delays and processing-time extensions. We develop a rolling-horizon distributionally robust model that updates predictions of the remaining closure duration as observations of disruption resolution become available. The model jointly optimizes train routes, sequences, and timings. It minimizes the worst-case expected total completion delay over an ambiguity set of scenario probabilities. The solution algorithm, GNN-LBBD, uses logic-based Benders decomposition to coordinate routing and resource scheduling. Conditional cuts are constructed from resource-use patterns, and a graph neural network guides the order in which resource relaxation subproblems are solved. Across 28 test instances for a five-track station, GNN-LBBD achieved a mean total completion delay of 61.13 train-min. This was 16.63\% lower than tabu search and 20.06\% lower than variable neighborhood search, with a mean total computation time close to that of tabu search. Information comparisons on six representative instances showed that using observations of disruption resolution reduced mean total completion delay by approximately 21.7\%. Scenario-based and conditional-mean predictions produced similar overall results under the same information conditions. The benefits of information were more pronounced in some instances with alternative routes. This suggests a relationship between the use of observations, the station resource structure, and the scope for schedule adjustments.

---


### 84. [Understanding Data Influence in Transportation Networks: A Physics-Constrained Influence-Function Framework](https://arxiv.org/abs/2611.07526)

**<font color=#1a73e8>作者：</font>** Hamidreza Attari, Yueyue Fan, Johannes Royset  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how individual training observations influence model predictions is important for developing reliable and interpretable data-driven transportation systems. Existing influence-function methods, however, are primarily formulated for unconstrained learning and do not explicitly account for physical constraints that couple different components of a transportation network. Under such constraints, perturbing a training observation can affect model parameters and predictions only through physically feasible directions, potentially changing how its influence propagates across the network. This paper develops a hard physics-informed influence-function framework for constrained learning, in which training-data influence is characterized within the physically feasible space defined by network constraints. The analytical results reveal how physical constraints alter the magnitude, direction, and spatial distribution of training-sample influence relative to conventional influence measures. Using traffic prediction under flow-conservation constraints as a case study, we show that influential observations identified by the proposed framework differ systematically from those identified by classical influence functions. Through orthogonal decomposition, we quantitatively characterize how much of a perturbation in the training data is propagated through the network via the flow-conservation constraints and how much is removed by the constraint projection. The proposed influence framework provides a physically consistent approach for evaluating training-data influence in constrained transportation learning problems, with potential applications to data diagnostics, sensor evaluation, and targeted data collection.

---


### 85. [Goal-Branching LaCAM: Temporary Goals as Search Branches in Dense Multi-Agent Pathfinding](https://arxiv.org/abs/2611.07528)

**<font color=#1a73e8>作者：</font>** Stephen Chang, Daniel Harabor  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LaCAM is a search-based solver for multi-agent pathfinding (MAPF) that runs a depth-first search over joint configurations, using PIBT to generate successors and lazily adding single-agent constraints to explore alternatives. Although LaCAM is complete, it can struggle on dense, corridor-heavy instances because extracting blocking agents from deadlocks requires coordinated moves of several agents, often away from their goals, which PIBT's greedy one-step successors rarely propose and which LaCAM can only reach by enumerating constraints one agent at a time. This paper proposes Goal-Branching, where blocking agents are given temporary goals, each tried as an additional branch of LaCAM's search. We examine random and corridor-aware rules for choosing these temporary goals and show that completeness is preserved for any such rule. On dense instances (60-90% of free cells occupied) of three maze and room maps, Goal-Branching solves 89% of instances against 44% for LaCAM*, and, on instances both solve, it finds a first solution 10-14x faster on maze-32-32-2 and room-32-32-4, and nearly 200x faster in median time at 75% density on room-32-32-4. Solution cost increases by 15-22% on instances both solve, while on open maps and the full MovingAI benchmark its solutions cost no more than those of LaCAM* and it is at most 3% slower.

---


### 86. [Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion](https://arxiv.org/abs/2611.07551)

**<font color=#1a73e8>作者：</font>** Jia Li, Xurui Peng, Xing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step autoregressive (AR) video diffusion models generate videos chunk by chunk and have made efficient video generation practical. However, further accelerating these models toward real-time generation remains challenging, as few-step distillation leaves little cross-step redundancy for existing training-free caching methods to exploit. We revisit this regime and identify two token-level redundancy patterns: cross-frame redundancy from static content shared across adjacent frames, and cross-step redundancy from tokens that converge early during denoising. Crucially, we find that early clean estimates along the model's own denoising trajectory provide an effective online signal for locating both patterns, requiring no retraining, auxiliary predictor, or reference video. Based on these findings, we propose PreSTP (Predictive Spatio-Temporal Token Pruning), a training-free framework that constructs a unified token-wise redundancy mask from cross-frame similarity and cross-step convergence. Tokens marked as redundant skip subsequent computation under a consistent last-computed-value restoration rule, and a content-adaptive mask reuse strategy further reduces dense probing cost. On 5-second generation, PreSTP achieves 1.52x-3.20x speedups and a better efficiency-fidelity trade-off than coarse-grained caching baselines such as TeaCache and FlowCache. On 30-second generation, it reaches up to 1.96x speedup while improving VBench-Long and suppressing long-horizon drift. Notably, it continues to reduce inference cost even in the extreme one-step regime, where cross-step redundancy vanishes entirely and coarse step-wise caching is no longer applicable.

---


### 87. [SPARE: Fast Linear Attention Decoding with Compact Recurrent States](https://arxiv.org/abs/2611.07552)

**<font color=#1a73e8>作者：</font>** Ke Wan, Zaiyi Zheng, Chen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear attention reduces the quadratic sequence-length complexity of softmax attention by maintaining fixed-size recurrent states. However, these states scale quadratically with the representation dimension and require repeated data transfers during decoding, creating a substantial GPU memory bottleneck. Recent studies have revealed significant low-rank redundancy in recurrent states, suggesting opportunities for more efficient representations. We introduce SPARE (State Projection for Accelerated Recurrent Execution), a training-free method that exploits this redundancy through fixed low-dimensional subspaces, heterogeneous rank allocation, and lightweight write compensation. By performing recurrent reads and updates directly on compact states, SPARE reduces memory traffic without online decomposition or dense-state reconstruction. SPARE achieves 2.55x full-model decoding speedup, 7.49x lower recurrent-kernel DRAM traffic, and 3.31x lower peak GPU memory, while preserving better associative-retrieval accuracy than structured pruning at matched memory budgets.

---


### 88. [Improving Long-Tail Detection via Layout-Instruction Conditioned Diffusion Synthesis](https://arxiv.org/abs/2611.07553)

**<font color=#1a73e8>作者：</font>** Xinyu Zhang, Xiaodi Wang, Yanpeng Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic data from diffusion models can improve object detection, but long-tail performance is still limited by scarce rare classes and inflexible conditioning (e.g., text-only or layout-only inputs). In this paper, we propose Tail-SD, a layout-instruction conditioned stable diffusion framework that supports text, layouts, or their hybrid, enabling controllable synthesis from boxes, masks, and/or prompts to better cover the long-tail objects. To train a single model across heterogeneous conditions, we introduce a multi-task cross-attention module and multi-task embedding tokens, improving generation quality and diversity. Extensive experiments on COCO and LVIS demonstrate that diffusion synthesis with hybrid conditioning consistently benefits detection, e.g., on LVIS val, it achieves +4.89% / +5.68% rare Box/Mask AP, highlighting strong potential for addressing long-tail challenges.

---


### 89. [MetricTrail: Revisiting the Power of Metric Depth and Local Optimization for Long-Sequence Streaming 3D Reconstruction](https://arxiv.org/abs/2611.07555)

**<font color=#1a73e8>作者：</font>** Jingnan Gao, Jiahui Huang, Sven Elflein 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MetricTrail, a streaming system for accurate camera motion estimation and dense reconstruction from long monocular videos. To keep inference efficient over long sequences, we revisit DPVO's sparse local estimator. We find that single-image metric depth substantially improves its trajectory accuracy, without retraining the correspondence network or enlarging the optimization window. Metric predictions initialize patch depths and remain as soft constraints during optimization. We further improve correspondence estimation through learned adapters that augment matching features and recurrent context with frozen DINOv3 representations. The correspondence estimator and adapters are trained on diverse short clips without additional long-sequence training. This modular design also allows the depth provider to be independently upgraded and supports supplied camera intrinsics and calibrated stereo observations without retraining. Under the reported RGB-only protocols, MetricTrail achieves the lowest average trajectory error among evaluated methods on KITTI, Oxford Spires, and VBR. Pairing the estimated poses with single-image depth predictions also produces strong dense reconstruction on indoor and outdoor benchmarks and coherent reconstructions of in-the-wild videos. With supplied intrinsics, the system processes KITTI-02 at 12.70 FPS with 3.21 GB peak GPU memory.

---


### 90. [Guidance Is a Field, Not a Scalar: Interval-Integrated Classifier-Free Guidance for One-Step Video Generation](https://arxiv.org/abs/2611.07566)

**<font color=#1a73e8>作者：</font>** Zijie Meng, Xixin Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-step generators built on MeanFlow synthesize a video in a single function evaluation, yet inherit a rigid treatment of classifier-free guidance (CFG): the guidance scale is frozen during training or, at best, exposed as a single scalar. This conflicts with mounting evidence that the optimal guidance is not a constant but a field that varies with the noise level, with spatial content, and, for video, with frame position. Every existing remedy presupposes a multi-step sampler along which guidance can be re-scheduled--an assumption one-step models violate by construction. We resolve this tension through a single observation: because the MeanFlow target is an integral over a noise interval, an arbitrary guidance field can be absorbed into the target itself and compiled into one evaluation. We formalize this as the interval-integrated CFG identity, prove that the compiled guidance carries no schedule-discretization error and can thus match or exceed any finite multi-step sampler, and instantiate it as AGAVE, which equips the average-velocity field with a learnable temporal schedule, a free motion-saliency spatial modulation, and a frame-position asymmetry. Adding fewer than ten scalars at zero inference cost, AGAVE surpasses all one-step baselines on VBench, UCF-101 and MSR-VTT while matching multi-step guided sampling. Project repository: this https URL.

---


### 91. [MambaTG: Candidate-Aware State Space Modeling for Future Link Prediction on Temporal Graphs](https://arxiv.org/abs/2611.07569)

**<font color=#1a73e8>作者：</font>** Nguyen Hong Quan, Sitao Luan, Yilun Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Future link prediction on temporal graphs involves both repeated interactions between previously connected node pairs and first-time interactions between pairs with no prior interaction. While repeated-edge prediction can exploit direct pairwise evidence, unseen-edge prediction must generalize beyond historical recurrence. Existing temporal graph models often exploit signals tied to recurring interactions or historical overlap, which are highly informative for repeated edges but become limited or unavailable for unseen edges, contributing to substantial performance degradation on unseen-edge prediction. Based on this observation, we identify two complementary signals for modeling sequential dynamics beyond historical recurrence: (1) historical-sequence evolution, which captures dependencies among the source node's chronologically ordered interactions, and (2) candidate--history compatibility, which captures how well a candidate fits the source node's evolving history. Based on the decomposition, we propose MambaTG, a candidate-aware Mamba-based framework that jointly models these two signals. Mamba provides a natural mechanism for this design: its selective recurrence captures the evolution of ordered interaction histories, while its input-dependent state transitions allow the history state to adapt to different candidate inputs. Extensive experiments on 13 temporal graph datasets against 13 representative baselines show that MambaTG achieves strong and consistent performance across both repeated and unseen edges while remaining computationally efficient.

---


### 92. [Integrating Learned Priors through Prior-Space Reparameterization for Physically Based Inverse Rendering](https://arxiv.org/abs/2611.07573)

**<font color=#1a73e8>作者：</font>** Hun Hwangbo, Minjun Park, Yongsung Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physically based inverse rendering decomposes appearance into materials and illumination, an ambiguous problem for which learned material predictions provide useful prior information. Most existing methods incorporate these cues through auxiliary regularization losses, which alter the optimization objective and require balancing their influence against photometric fitting. We propose a prior-guided material reparameterization that uses the predicted feature relationships to restrict the optimization space while leaving the objective unchanged. We fuse multi-view material predictions onto a mesh and construct a permutohedral lattice in the resulting prior feature space. Surface points with similar predictions share material variables, which are optimized jointly with geometry and illumination using a purely photometric objective. Experiments with two learned predictors on three synthetic benchmarks and Stanford-ORB demonstrate improved material decomposition and relighting. Our method improves relighting PSNR by 1.5-2.5 dB over the strongest evaluated mesh-based baseline on Synthetic4Relight and TensoIR-Synthetic, and outperforms a regularization loss using the same prior in controlled comparisons. We further show that our reparameterization pools noisy photometric gradients, producing updates that are more consistent across sampled views. This consistency enables a shortened joint optimization schedule that takes less than a minute while retaining relighting quality above all evaluated baselines on TensoIR-Synthetic.

---


### 93. [Georeferenced Cross-View 3D Reconstruction from Ground and Satellite Images](https://arxiv.org/abs/2611.07575)

**<font color=#1a73e8>作者：</font>** David G. Shatwell, Mubarak Shah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Georeferenced 3D reconstruction from ground images requires recovering not only the local scene geometry, but also localizing every camera center and 3D point in a geographic coordinate frame. Existing cross-view geo-localization methods are able to estimate the GPS coordinate of a single ground camera, but do not reconstruct dense 3D geometry, while recent feed-forward multi-view 3D reconstruction models predict point maps and camera poses only in a local coordinate frame. We introduce X-VGGT, a feed-forward cross-view geometry transformer that unifies these tasks by jointly processing a set of ground-level images and a georeferenced satellite image to predict ground-view camera poses, dense 3D point maps, and a scene-level transform parameterized by gravity, scale, yaw and translation. This transform projects the local reconstruction into the satellite plane, resulting in the geo-registration of all ground images with the georeferenced satellite image. We further propose an evaluation protocol for this joint task and show that, across multiple cross-view datasets, X-VGGT produces accurate georeferenced reconstructions and outperforms prior cross-view geo-localization and multi-view 3D reconstruction models.

---


### 94. [Subspace Learning with Outlier Exposure for Out-of-Distribution Detection](https://arxiv.org/abs/2611.07580)

**<font color=#1a73e8>作者：</font>** Hongxu Shen, Kun Fang, Jiahui Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Out-of-Distribution (OoD) detection is pivotal for reliable deployments of Deep Neural Networks (DNNs), aiming to distinguish anomalous samples from the In-Distribution (InD) data in training. By introducing outliers as surrogate OoD data to finetune DNNs, Outlier Exposure (OE) has greatly advanced OoD detection in recent years. Existing OE-based research remains predominantly logit-centric, either by generating diverse outliers or by regularizing them with objectives operating at the prediction-output level. Nonetheless, these approaches leave much of the rich information in feature spaces untapped. In this work, we propose an OE-based detection framework, named RecOE, that learns appropriate feature subspaces from InD data and auxiliary outliers, such that the InD-OoD discrepancy can be effectively characterized through the learned feature subspaces. Specifically, the feature subspaces are optimized to capture the dominant variations of InD and outliers by minimizing reconstruction errors therein. Besides, a sample-level objective discourages reconstruction in the opposing subspace, while an orthogonality regularizer reduces subspace overlap, further promoting discriminative subspaces. At inference, the difference in reconstruction errors between the learned subspaces serves as the OoD detection score. Extensive experiments show the superiority of RecOE on multiple benchmarks, in which significant performance gains are achieved over recent strong baselines with only slight extra overhead from two small-size matrices of subspace bases. The source code is available at this https URL.

---


### 95. [Fine-Tuning a Transducer for Impaired Speech: Where the Gains Appear and What They Mean for Evaluation](https://arxiv.org/abs/2611.07587)

**<font color=#1a73e8>作者：</font>** Kien Nguyen, Tuan Dinh, Bao Phan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech recognition still works poorly for many people whose speech is affected by conditions such as ALS, Parkinson's disease, cerebral palsy, Down syndrome or stroke. We took part in the Speech Accessibility Project Challenge 2 (SAPC2) with a public speech recognizer that we fine-tuned on the challenge data. Our best entry scored 7.81% character error rate on Test1, the first of two hidden test sets (official baseline 15.26%). Our live entries ran on CPUs with a combined median latency of about 0.9 seconds at 7.96-8.07% error. On new speakers, fine-tuning reduced errors most for the speakers that an off-the-shelf recognizer finds hardest to understand. Sentences already seen in training had far lower error rates than new ones (2.58% vs 6.42%), a larger difference than being a familiar speaker made. We close with lessons for evaluating such systems.

---


### 96. [FisherDistill: Diffusion Distribution Distillation via Closed-Form Fisher Critics](https://arxiv.org/abs/2611.07604)

**<font color=#1a73e8>作者：</font>** Mahesh Bhosale, Yuanhao Zhai, Siwei Lyu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in diffusion distillation have enabled high-quality image generation in only one or a few network function evaluations (NFEs). Despite their efficiency, aggressively distilled generators often retain a residual distribution gap from their multi-step teachers, motivating recent methods to introduce adversarial refinement with a learned discriminator. In this work, we ask whether such refinement necessarily requires a learned adversarial discriminator. We introduce \textbf{FisherDistill}, a simple alternative based on Fisher linear discriminant analysis. Using intermediate representations from the frozen teacher, we estimate the first- and second-order statistics of real and generated samples and derive a closed-form Fisher direction that maximally separates their feature distributions relative to within-class variation. This direction provides a lightweight refinement signal that complements the original distillation objective without requiring an additional adversarial discriminator or its optimization loop. Across multiple distillation frameworks, our approach consistently improves generation quality over their respective distilled baselines and substantially closes the gap to adversarially refined counterparts. Code: this https URL

---


### 97. [Towards Real-Time Full-Waveform LiDAR Transformers via Intensity-Guided Token Reduction and Physics-Aware Augmentation](https://arxiv.org/abs/2611.07613)

**<font color=#1a73e8>作者：</font>** Kotaro Oishi, Kazuma Ikeda, Ryosei Hara 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR is a critical sensor for autonomous driving and robotics, yet it remains vulnerable to adverse conditions such as fog, rain, transparent objects, and low-reflectance surfaces. Full-waveform LiDAR (FWL) addresses these limitations by capturing the complete return waveform as a histogram, preserving rich reflection characteristics including multi-path echoes and weak signals. While recent Transformer-based approaches have demonstrated promise on FWL data, two fundamental bottlenecks remain: high computational cost from redundant tokens in low-intensity background regions, and limited generalization due to scarce annotated training data. We address both bottlenecks by exploiting the physical structure inherent to FWL data. First, we propose FWL-ToPM, a token pruning and merging mechanism that leverages intensity distributions to selectively reduce tokens while retaining critical waveform content. Second, we introduce FWLAug, a data augmentation framework designed as a regularization method that preserves waveform structure, retaining the Time-of-Flight waveform of each ray and the frustum geometry, to improve generalization to unseen scenes. Evaluated on the Ghost-FWL benchmark, FWL-ToPM achieves over 8 times speedup at real-time throughput alongside a nearly 9-point F1 gain over the prior state of the art, establishing the first real-time FWL Transformer that simultaneously improves accuracy. FWLAug further improves performance on both the standard benchmark and an out-of-distribution test set of unseen scenes. Together, these methods push FWL-based perception toward practical deployment. The code and the OOD dataset are publicly available and can be accessed via the project page: this https URL

---


### 98. [Monotone Viability Learning for Offline Safe Reinforcement Learning](https://arxiv.org/abs/2611.07616)

**<font color=#1a73e8>作者：</font>** Ziqian Wang, Zhen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline safe reinforcement learning requires reliable long-horizon safety estimates from fixed data. Learning Hamilton-Jacobi (HJ) viability in this setting calls for semantic preservation, convergence, and numerical stability. To address these challenges, we propose Monotone Viability Learning (MoViL), which learns viable sets from offline transitions through monotone finite-horizon set recursion. The recursion preserves finite-horizon safety semantics and converges to the infinite-horizon viability kernel. Binary supervision maintains a fixed target scale across horizons, avoiding discount-induced numerical attenuation. We further establish sufficient conditions for recovering behavior-supported viable subsets. The learned viability estimates are used to certify actions at deployment. Dubins car experiments validate the numerical accuracy of the learned viable sets. Evaluations on safe RL benchmarks demonstrate state-of-the-art reward-cost performance. MoViL satisfies the average cost constraint on every task and achieves the lowest average cost among the compared methods. These results highlight MoViL's potential to extend long-horizon HJ viability analysis to safety-critical systems where reliable dynamics models are unavailable and online exploration is unsafe.

---


### 99. [Online Learning with Ordered Experts (via Two-point Feedback)](https://arxiv.org/abs/2611.07629)

**<font color=#1a73e8>作者：</font>** Shiliang Zuo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study adversarial online learning with expert recommendations in a totally ordered action space, where the experts' recommendations may change and be reordered arbitrarily. Our focus is two-point feedback: on each round the learner plays two current recommendations, observes both, and pays their average. We study two problems. In the separated monotone problem, the loss is the sum of a hidden nondecreasing component and a hidden nonincreasing component, and a query reveals the two components separately. In the BV problem, the losses are bounded and have bounded variation (BV) along the order, and a query reveals only the loss.
In the separated monotone problem, two paid observations achieve \[ O\bigl(\log(|\cF|T)\sqrt{T\log|\cF|}\bigr) \] regret against the best of $|\cF|$ experts, within a logarithmic factor of the classical full-information bound. For the BV problem, we obtain $\wtO(\sqrt T+|\cF|)$ regret. We give an application in dynamic pricing with expert advice, showing that two-option menus matches the full information rate up to $\log$ factors.
The main technical ingredient is a marginal-preserving endpoint flow estimator. Two observations reveal a loss increment along the order; random paths supply telescoping identities that turn this local information into unbiased loss estimates for all current recommendations. A reversible pair sampler preserves the learner's intended marginal at both played actions. The estimator's second-moment and stability bounds support online updates for both feedback models.

---


### 100. [TRACEMARK: Editor-Aware Watermarking for User Attribution in Text-Guided Image Editing](https://arxiv.org/abs/2611.07632)

**<font color=#1a73e8>作者：</font>** Xiaodong Wu, Xiangman Li, Jianbing Ni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An image editing service records which user requests each edit, but the edited image itself does not contain this account information. Once the image is downloaded and shared, the service cannot identify the requesting user from the image alone. Embedding a user-specific watermark could enable such attribution, but semantic editing may erase the signal. We propose Tracemark, an editor-aware watermarking framework for identifying users from edited images. A shared encoder embeds a user-specific signal before editing, and a shared detector recovers the user by comparing features of the edited image with learned reference vectors. Both components are trained jointly through an editor with fixed parameters. User identification errors encourage the encoder to produce watermarks that survive editing, while fidelity losses limit changes to the input image and intended edit. Each image domain and editing instruction uses a separately trained model shared across registered users. Experiments on three image domains show that editor-aware training improves user recovery with both reference-vector matching and binary watermark decoding. Separately trained models reach 87.5% mean identification accuracy among 500 users. When tested with a different editor without retraining, the watermark modules still recover user information. These results demonstrate that learning watermarks through the editing process enables user attribution without modifying the editor.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-237](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
