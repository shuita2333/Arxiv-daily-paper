# 📦 其他研究 | 2026年06月18日

> 本类共 **205** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-205](./part-05.md)

---

### 51. [The Discrete-Log Clock: How a Transformer Learns Modular Multiplication](https://arxiv.org/abs/2606.17399)

**<font color=#1a73e8>作者：</font>** Huu Danh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When small transformers grok modular multiplication, prior work reports that the learned embedding has a "dense" Fourier spectrum requiring all frequencies. This contrasts with modular addition, where only a sparse set of key frequencies suffices. We show this density is an artifact of analyzing in the wrong basis. The natural Fourier transform for multiplication is not the standard additive DFT but the multiplicative character transform, which decomposes functions on the multiplicative group $(\mathbb{Z}/p\mathbb{Z})^*$ into its irreducible representations. Applying this transform to a grokked transformer trained on $a \cdot b \bmod 113$, we find the embedding spectrum becomes highly sparse (Gini coefficient 0.58 vs. 0.07 in the additive basis) with only 4 key frequencies carrying significant energy. Furthermore, 96.9% of MLP neurons are cleanly tuned to a single multiplicative frequency, and neuron activation heatmaps reveal 2D-periodic structure when reordered by the discrete logarithm. These results demonstrate the transformer reduces multiplication to addition in discrete-log space, implementing a "Discrete-Log Clock" algorithm analogous to Nanda et al.'s Clock algorithm for addition. The methodology generalizes: matching the analysis basis to the algebraic structure of the task reveals interpretable structure where standard tools see noise.

---


### 52. [Bridging Spatial And Frequency Views For Disaster Assessment: Benefits And Limitations](https://arxiv.org/abs/2606.17403)

**<font color=#1a73e8>作者：</font>** Shikha V. Chandel, Yadav Raj Ghimire, Timothy Agboada 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid assessment of building damage from satellite imagery is essential for effective disaster response and recovery. While most deep learning methods rely on spatial-domain features, frequency-domain representations can capture complementary structural cues such as debris patterns and collapse-induced textures. This study presents a controlled comparison of spatial-domain, frequency-domain, and dual-domain deep learning approaches for multi-class building damage classification using post-disaster imagery from the xView2 (xBD) dataset. To ensure fairness, all models are built on an EfficientNet-B0 backbone and trained under identical settings, differing only in their input representations and fusion strategies. Performance is evaluated using accuracy, macro F1-score, per-class metrics, and confusion matrices. Results show that dual-domain models provide measurable improvements over single-domain approaches. The dual spatial configuration achieves the highest test accuracy (0.4688) and lowest loss, while the spatial-only model attains the best macro F1-score (0.4254), indicating more balanced class performance. In contrast, frequency-only models perform worst and exhibit overfitting, suggesting limited generalization. Despite these gains, all models struggle to detect subtle damage levels, particularly the Minor class, due to class imbalance and fine-grained visual ambiguity. While dual-domain approaches improve detection of severe damage, challenges remain. These findings highlight the benefits and limitations of hybrid representations and motivate future work on data balancing, advanced fusion, and regularization.

---


### 53. [Treatment Response Optimized Clinical Decision Support AI System via Digital Twin Simulation](https://arxiv.org/abs/2606.17405)

**<font color=#1a73e8>作者：</font>** Xinyu Qin, Anil K. Sood, Ruiheng Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical decision support AI systems (CDSASs) must adapt to evolving patient conditions in real-time while adhering to strict safety constraints. We present an online adaptive framework that integrates Treatment Effect (TE) estimation to quantify clinical benefits, a patient Digital Twin (DT) to simulate treatment trajectories, and Reinforcement Learning (RL) for sequential decision-making. The AI system is initially trained on historical medical records and operates in a continuous learning loop. To ensure safety, a rule-based module monitors vital signs and blocks contraindicated treatments. Cases with strong internal model disagreement are flagged for clinician review, simulated in our experiments via a pre-trained outcome model. We validate our framework using both a synthetic clinical simulator and a real-world ovarian cancer dataset from The Cancer Genome Atlas (TCGA). In both simulated and clinical settings, our method demonstrated superior effectiveness and stability in recommending treatments compared to standard computational baselines. Furthermore, the AI system maintains low latency and requires expert consultation for only a minority of cases in our experimental validation, demonstrating its potential as a safe, clinician-supervised tool for personalized medicine that continuously improves through practical use.

---


### 54. [Graph Neural Networks for Semi-Supervised Image Classification with Multi-Feature Aggregation](https://arxiv.org/abs/2606.17406)

**<font color=#1a73e8>作者：</font>** Marina Chagas Bulach Gapski, Vinicius Atsushi Sato Kawai, Gustavo Rosseto Leticio 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature extraction involves the identification and extraction of salient characteristics or patterns, including edges, textures, shapes, and color attributes. Contemporary feature extractors predominantly leverage deep learning architectures, such as Convolutional Neural Networks (CNNs) and Vision Transformers (VITs). The availability of diverse feature extractors in the literature provides a wide range of feature representations. Features extracted from an image depend on the specific application, the chosen extractor, and its configuration. Therefore, integrating complementary information by combining distinct extractors offers a promising way to enhance performance. Graph Neural Networks (GNNs), particularly Graph Convolutional Networks (GCNs), have emerged as powerful and widely adopted approaches for semi-supervised image classification, as they effectively leverage both labeled and unlabeled data while exploiting the underlying graph structures that capture relationships among samples. This study proposes a novel approach for GNNs in scenarios where labeled data is scarce, by integrating diverse sets of feature and graph representations derived from various extractors in classification scenarios. Experimental investigations were conducted, encompassing combinations of distinct feature and graph extractors, as well as rank aggregation strategies. The primary contributions of this work are underscored by the experimental findings, which demonstrate that the strategic combination of feature and graph representations, coupled with the application of manifold learning for graph processing, leads to significant improvements in classification accuracy across the majority of experimental conditions. Furthermore, the utilization of rank aggregation techniques to integrate features from different extractors was shown to enhance classification accuracy.

---


### 55. [Discrete Autoregressive Transformer for Generative Mechanism Synthesis](https://arxiv.org/abs/2606.17409)

**<font color=#1a73e8>作者：</font>** Anar Nurizada, Anurag Purwar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Planar path synthesis requires mechanisms whose coupler curves match a prescribed trajectory; the mapping from curve to linkage is inherently one-to-many across four-, six-, and eight-bar topologies. We address this design problem with simulation-grounded evaluation on a curated corpus of over one million mechanisms, reporting Chamfer distance and dynamic time warping after forward kinematics and geometric alignment. We formulate synthesis as conditional autoregressive sequence modeling: joint coordinates are uniformly quantized to tokens and generated by a decoder-only transformer with a variational-autoencoder (VAE) latent of the target curve and an explicit mechanism-type token. Training combines token cross-entropy with a Gaussian-smoothed bin auxiliary loss that respects ordinal structure among bins. At inference, a bounded latent-noise schedule decodes all mechanism types at each noise level; we retain the top five candidates by geometric error, yielding diverse accurate families without dataset lookup. On held-out tests, aggregate mean Chamfer distance is $0.0132$ and mean dynamic time warping is $0.153$; a latent $k$-nearest-neighbor baseline that conditions on training-set neighbor latents in VAE space achieves matched-topology mean Chamfer distance $0.0071$ and mean dynamic time warping $0.117$ using the same decoder.

---


### 56. [Enhancing Pathological VLMs with Cross-scale Reasoning](https://arxiv.org/abs/2606.17412)

**<font color=#1a73e8>作者：</font>** Chi Phan, Tianyi Zhang, Qiaochu Xue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathological images are inherently multi-scale, requiring pathologists to integrate evidence from global tissue architecture at low magnification to cellular morphology at higher magnification for accurate diagnosis. While existing pathological datasets for vision-language model (VLM) include various scales, they often lack an explicit cross-scale reasoning objective. This limitation prevents VLMs from capturing essential cross-scale representations and learning evidence-based reasoning. To bridge this gap, we introduce the first cross-scale training and evaluation paradigm that formulates pathology interpretation as multi-magnification reasoning. However, creating such a task reveals a critical challenge: multi-image visual question answering (VQA) is prone to text-only shortcuts, which allow models to guess answers using magnification-dependent artifacts rather than visual evidence. To address this, we propose a leakage-aware curation pipeline that combines adversarial text-only screening with constraint-guided question design. Using this pipeline, we construct Scale-VQA, a high-quality benchmark with 4,685 multiple-choice questions grounded in 2,537 pathology images across multiple magnification levels. Finally, we present ScaleReasoner-R1, a model trained via reinforcement learning to optimize performance on the cross-scale VQA task. ScaleReasoner-R1 achieves state-of-the-art performance on our cross-scale reasoning benchmark and generalizes to SOTA performance on established single-scale benchmarks. Findings suggest that even the limited cross-scale supervision can significantly improve pathological understanding. The code and demos will be open-sourced.

---


### 57. [Amortized Probabilistic Retrieval of Atmospheric CO2 from OCO-2 Spectra Using Deep Learning with Laplace Approximations and Normalizing Flows](https://arxiv.org/abs/2606.17413)

**<font color=#1a73e8>作者：</font>** Alejandro Calle-Saldarriaga, Felix Jimenez, Jack Grosskreuz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Space-based monitoring of atmospheric carbon dioxide (CO2) is essential for constraining the global carbon budget. NASA's Orbiting Carbon Observatory-2 (OCO-2) estimates column-averaged dry-air mole fractions of CO2 (XCO2) using high-resolution spectra. However, current operational retrieval algorithms are computationally expensive and do not properly quantify uncertainties. We present a novel deep learning framework that addresses these challenges. Due to the difficulties of ground-truth data for real satellite observations, we develop and validate our approach using a high-fidelity simulation dataset. This dataset, created to support OCO-2 uncertainty quantification (UQ), incorporates realistic forward model errors. Our architecture encodes spectral bands using a multi-branch neural network and estimates posteriors of the full CO2 column or desired summaries thereof using two scalable UQ methods: Laplace approximations and normalizing flows. Our approach has five key advantages relative to operational "full-physics" solvers: (1) Amortization: Inference is orders of magnitude faster, enabling real-time processing of massive data streams; (2) Model error robustness: By training on simulations that explicitly include model discrepancies, our method accounts for systematic errors often neglected by standard inversions; (3) Point estimate accuracy: We achieve superior predictive accuracy compared to baseline methods; (4) Improved UQ: The probabilistic outputs yield better-calibrated uncertainty estimates; and (5) Non-Gaussian posteriors: When utilizing normalizing flows, our framework successfully models complex, asymmetric posterior distributions, overcoming the limitations of the Gaussian assumption. These results suggest that simulation-based deep learning is a viable path toward next-generation operational processing systems.

---


### 58. [Memory-Efficient Meta-Reinforcement Learning for Adaptive Safety-Critical Control in Adversarial Spacecraft Proximity Operations](https://arxiv.org/abs/2606.17414)

**<font color=#1a73e8>作者：</font>** Alejandro Posadas-Nava, Richard Linares, Minduli Wijayatunga  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous spacecraft rendezvous and proximity operations (RPO) require controllers that guarantee safety under thrust constraints while minimizing fuel expenditure. Input-constrained control barrier functions (ICCBFs) provide a control method for nonlinear systems with actuation constraints that construct a forward-invariant safe set. Previous work has shown that learning class-$\mathcal{K}$ functions defining the ICCBF recursion via meta reinforcement learning (meta-RL) yields a robust, non-greedy approach to safety-critical control in RPO. This paper extends that framework further by investigating the performance of three recurrent network architectures (Long Short Term Memory (LSTM), Gated Recurrent Unit (GRU), Selective State Space Model (Mamba)) and two training algorithms (Proximal Policy Optimization (PPO) and Soft Actor Critic (SAC)) to identify the best setup for tuning ICCBF class-K functions via meta-RL. In addition to cooperative test cases, performance is evaluated in the presence of adversarial behavior where the target spacecraft behaves in a way that worsens the safety of the chaser spacecraft. Results indicate that state space models such as Mamba when used with PPO achieve superior task completion, safety, and fuel-savings compared to other architectures, across all cooperative and uncooperative scenarios tested.

---


### 59. [Generalization Guarantees for Multi-Input Neural Operator Learning in Sobolev Spaces](https://arxiv.org/abs/2606.17419)

**<font color=#1a73e8>作者：</font>** Yahong Yang, Zecheng Zhang, Wei Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop approximation and generalization error estimates for multi-input neural operators, with the output error measured in Sobolev norms. In contrast to standard operator-learning settings with a single input function, our framework allows multiple input functions defined on possibly different domains, with different dimensions and Sobolev regularities. The derived rates explicitly quantify the contribution of each input space to the final error bound. In particular, in the balanced regime, the approximation and generalization rates are governed by the interaction between the input dimensions, regularities, and Sobolev orders, while the dependence on the model complexity retains a \(\log\log/\log\)-type structure. Our analysis provides a general theoretical framework for multi-input operator learning, including Sobolev training, and is applicable to operator learning problems arising from partial differential equations and scientific computing.

---


### 60. [Impact of Hand Impairment and Occlusions on Hand Pose Estimation Accuracy in Augmented Reality Applications](https://arxiv.org/abs/2606.17427)

**<font color=#1a73e8>作者：</font>** Damian M. Manzone, Mathew Szymanowski, Olga Taran 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mixed reality applications can be designed for hand rehabilitation. Augmented reality (AR) head mounted displays (HMDs) specifically allow for ecologically valid tasks because individuals can see their real environment and interact with real objects while receiving additional cues on the HMD. While these applications rely on accurate hand pose estimation, there is a gap in investigating the influence of hand impairment or occlusion from real-object interactions on pose estimation accuracy. Further, comparisons between AR HMD predictions and state-of-the-art pose estimation methods have not been established. The current study assessed pose estimation accuracy of the HoloLens 2 HMD and state-of-the-art pose estimation algorithms (WiLoR, HaMeR, WildHands, and MediaPipe) while individuals with cervical spinal cord injury (cSCI; n = 13, Neurological Level of Injury: C3-C6; American Spinal Injury Association Impairment Scale: A-D) and 15 uninjured controls interacted with clear and opaque objects. Ground truth estimates of 3D joint positions were generated via triangulation from a multi-camera setup. Pose estimation accuracy did not differ between the cSCI and uninjured control groups suggesting that 3D joint predictions from the HoloLens 2 and pose estimation algorithms can generalize to populations with hand impairment. Further, clear objects provided a small accuracy advantage over opaque objects (0.1 mm) and predictions from both WiLoR and HaMeR were slightly more accurate than the HoloLens 2 (2 mm). Overall, these results suggest that the HoloLens 2 may be viable for hand rehabilitation applications and the dataset generated can be used to refine pose estimation methods for hand-impaired populations.

---


### 61. [MorphStrata: Layer-Specific Perturbations for Generating Morphence Students in Time-Series Moving Target Defense](https://arxiv.org/abs/2606.17435)

**<font color=#1a73e8>作者：</font>** Abhishek Bhardwaj, Arnav Doshi, Anusri Nagarajan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting models remain vulnerable to gradient-based adversarial attacks while existing defense mechanisms typically incur a trade-off in robustness for bounded response and compute cost. The problem is pronounced in Moving Target Defense where maintaining multiple randomized model instances substantially exacerbates the training overhead. In this work, we introduce MorphStrata, a student generation strategy with selective, layer-specific stochastic noise injection that extends the traditional Morphence defense. MorphStrata uses a Transformer backbone as the teacher and perturbs randomly selected architectural blocks to create structured heterogeneity across student models in response to varied data distributions and threat models. We evaluate against vanilla Transformer and Morphence backbones on a suite of benchmarks including the Jena Climate, Electricity Load Diagrams, and Appliances Energy Prediction using FGSM, BIM and PGD attacks across multiple attack strengths. Across datasets and attack regimes, the proposed ensemble maintains comparable adversarial RMSE. Specifically, for high entropy, periodic datasets as in the case of the AEP data, MorphStrata achieves the lowest RMSE across all attacks and perturbation budgets, improving over the static baseline by up to 24.11% and 97.97% under FGSM and BIM respectively at an epsilon value of 0.5 over 30 randomized trials. Targeting the layers to generate MorphStrata students accounts for less than 1% increase in train-times over the Morphence MTD baseline for most of the experiments, while accounting for double digit gains in adversarial RMSE reduction. We also observe a positive correlation between higher pairwise L2 distance (among generated students) and overall defense effectiveness. In summary, MorphStrata maintains adversarial robustness as an MTD defense at marginal cost deltas when compared to existing baselines.

---


### 62. [Spatio-Temporal Fusion Model for Standard View Classification of Echocardiographic Videos](https://arxiv.org/abs/2606.17437)

**<font color=#1a73e8>作者：</font>** Bo Gou, Jicheng Zhang, Jianlong Xiong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated classification of standard echocardiographic views is crucial for efficient clinical workflow but faces three main challenges. First, publicly available datasets are scarce and limited in scale and view coverage. Second, the performance of some modern video-level architectures for echocardiographic view classification remains underexplored. Third, some view categories exhibit highly similar spatial appearances, making single-frame features insufficient for discrimination, while heterogeneous frame quality complicates robust temporal information fusion. To address these challenges, we release the Echocardiographic Videos of Nine Views (EV9V) dataset, comprising 5,138 videos, 910,579 frames, and 9 standard views, which is, to the best of our knowledge, the largest publicly available echocardiography video dataset. Using EV9V, we systematically benchmark representative video classification architectures, including Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and Transformers. Furthermore, we propose a Spatio-Temporal Fusion Model (STFM), an efficient dual-stream CNN-LSTM (Long Short-Term Memory) framework that jointly captures spatial anatomical structures and temporal cardiac dynamics. The proposed framework leverages uncertainty-aware learning to preferentially sample representative video segments during training and evidence-based fusion during inference, improving robustness to variations in frame quality across echocardiographic videos. Extensive experiments demonstrate that our method achieves competitive performance across diverse video classification models, validating the effectiveness of uncertainty-aware spatio-temporal learning for echocardiographic view classification. The code is available at this https URL.

---


### 63. [Contact-Based Fringe Projection Profilometry for High-Resolution 3-D Surface Measurement of Reflective and Transparent Objects](https://arxiv.org/abs/2606.17438)

**<font color=#1a73e8>作者：</font>** Ingu Yeo, Hyung-Gun Chi, Jae-Sang Hyun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a contact-based 3-D surface measurement method based on a Digital Fringe Projection (DFP) system, belonging to the vision-based tactile sensing family pioneered by the commercially successful GelSight sensor. Such sensors have proven effective for robotic fingertip manipulation and contact sensing. However, because GelSight employs photometric stereo with RGB LEDs, it does not measure absolute depth directly but instead infers it by integrating estimated surface gradients, which can accumulate reconstruction errors; in addition, it becomes increasingly difficult to calibrate as the sensing area grows, and its depth accuracy is challenged on highly reflective or transparent objects. To overcome these drawbacks, we propose a fringe-projection-based contact measurement technique that performs triangulation-based 3-D reconstruction on a coated silicone contact surface, providing dense per-pixel surface geometry and full-field 3-D shape measurement over the contact region. By integrating high-accuracy digital fringe projection into the sensor, our approach simplifies calibration over larger areas and enhances depth precision for complex surfaces. Experimental results, including a direct comparison with a GelSight Mini sensor, a sphere-fitting accuracy evaluation, and an uncertainty analysis, confirm that the proposed method significantly improves the accuracy and stability of structured-light-based 3-D measurements, allowing reliable reconstruction of objects with diverse optical properties.

---


### 64. [Patients With Personality: Realistic Patient Simulation through Controlled Diversity and Selective Disclosure](https://arxiv.org/abs/2606.17441)

**<font color=#1a73e8>作者：</font>** Moritz Schlager, Friederike Jungmann, Samuel Schmidgall 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Simulating realistic patient interactions is a key requirement to testing clinical applications of LLMs at scale without time-consuming and expensive user studies. However, existing approaches often lack realism and controllability, often oversharing information unprompted, and failing to capture the wide variability of patient behavior. Here, we introduce PatientsWithPersonality (PWP), a patient simulation framework that generates realistic yet diverse virtual patient responses through explicit personality parametrization over a latent patient state. Grounded in HEXACO, a six-dimensional personality space used to quantify and parameterize human behavioral traits, our approach enables fine-grained control over conversational style, cooperativeness, and information disclosure within a unified framework. In a clinician evaluation, PWP is judged nearly as realistic as recorded human actors and clearly ahead of prior simulators, while being flagged as "too informative" far less often. Conditioning on HEXACO axes yields personas whose configured traits are recoverable by both clinicians and an autorater, span a substantially wider behavioral footprint than the closest baseline, and prevent oversharing. Altogether, our framework paves the way for more accurate and informative LLM benchmarking through our realistic and steerable patient simulator.

---


### 65. [Toward Controllable Catalyst Inverse Design via Large-Scale Autoregressive Pretraining](https://arxiv.org/abs/2606.17445)

**<font color=#1a73e8>作者：</font>** Dong Hyeon Mok, Jonggeol Na, Seoin Back  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse design of heterogeneous catalysts remains challenging because catalyst surfaces exhibit substantial structural complexity with coupled surface-adsorbate interactions across a vast chemical space that is difficult to explore efficiently through conventional screening alone. Although machine learning-based high-throughput screening has accelerated catalyst discovery, its efficiency inevitably declines as the search space grows, motivating the development of generative models that can directly construct catalysts with target properties. Here, we present a conditional catalyst generative model based on the Generative Pretrained Transformer architecture with a numerical embedding layer that enables the generation of catalyst structures conditioned on both categorical and continuous properties within a single autoregressive framework. The model was pretrained on 133 million catalyst structures and subsequently fine-tuned on approximately 460,000 optimized structures with associated categorical properties and binding energies for conditional generation. The resulting model achieved 98% structural validity, 95% optimization validity, and high categorical condition fidelity, with a 93 % joint match rate for adsorbate type and composition. For binding energy conditioning, the match rate of approximately 20% represents a four-fold improvement over the baseline training distribution, and the generated distributions shift systematically toward the target values, enabling a 1.5 to 4-fold improvement in screening efficiency for reaction-targeted catalyst discovery without additional fine-tuning. These results show that large-scale autoregressive pre-training, combined with explicit property conditioning, provides a practical route toward controllable catalyst generation and accelerated catalysts discovery.

---


### 66. [A Machine-Learned Comorbidity Index](https://arxiv.org/abs/2606.17450)

**<font color=#1a73e8>作者：</font>** Suleman Baloch, Kishlay Jha, Alberto M. Segre 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional comorbidity scores (e.g., Charlson and Elixhauser) are widely used for risk adjustment and patient stratification, but they have two key limitations: (i) they are largely mortality-centric and do not align well with other clinical outcomes, and (ii) their linear, rule-based structure cannot capture nonlinear, outcome-specific risk relationships. We propose a Machine-Learned Comorbidity Index (MLCI) that maps diagnosis codes to a single scalar by maximizing the normalized Hilbert-Schmidt Independence Criterion (nHSIC) between the learned score and multiple clinical outcomes. MLCI captures nonlinear risk-outcome dependence and is supported by a theory that characterizes when a unified, informative admission-level ordering can be achieved across outcomes. Empirical results on multiple benchmark electronic health record (EHR) datasets show that MLCI outperforms strong baselines across multiple evaluation metrics.

---


### 67. [Credibility-Weighted Pricing of Autonomous Vehicle Liability Under Operational Design Domain Shift](https://arxiv.org/abs/2606.17451)

**<font color=#1a73e8>作者：</font>** Doyeon Jang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated Driving System deployments create a foundational ratemaking challenge: sparse experience, shifting operational design domains, and non-stationary risk across software releases. We propose a hierarchical Bayesian credibility framework pooling across cities, software versions, and territories via a learned ODD-similarity kernel, nesting Buhlmann-Straub as a limiting case. Demonstrated on 648 verified-engaged Waymo crashes across four U.S. metros from the NHTSA Standing General Order database against 116 million matched miles, city-aggregate credibility weights are moderate (0.12-0.46), partial pooling decisively outperforms no pooling, and a power analysis shows the learned kernel's advantage becomes detectable at approximately twelve deployed cities.

---


### 68. [MapSatisfyBench: Benchmarking Satisfaction-Aware Map Agents through Behavior-Grounded Implicit Decision Factors](https://arxiv.org/abs/2606.17453)

**<font color=#1a73e8>作者：</font>** Lubin Bai, Mengyu Cao, Sixue Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly integrated into map services. Since map services are embedded in everyday-life scenarios rather than professional task settings, users often express their needs informally, resulting in underspecified queries with many unspoken needs, namely, implicit decision factors that are critical for user satisfaction. Although clarification is an effective way to mitigate this issue, it increases user burden in daily interaction, and a capable agent should first proactively recover such factors from available information sources. However, evaluating this ability is challenging. The first challenge is to determine which implicit decision factors are suitable for evaluation. A factor is evaluable only if it affects user acceptance and can be recovered from information available to the agent before it responds. Second, user satisfaction cannot be reliably represented by a single reference answer, requiring a benchmark that converts satisfaction-relevant factors into objective and quantifiable evaluation targets. To address these challenges, we propose a restore-identify-filter framework that reconstructs complete user needs from behavior-chain evidence, identifies implicit decision factors, and retains only those supported by pre-query evidence. Building on this methodology, we construct MapSatisfyBench from large-scale, real-world anonymized user data and annotate ground truth from five dimensions and enables full-chain evaluation of satisfaction-aware map agents. Experiments show that current agents generally perform well on explicit task completion, but remain limited in satisfying implicit decision factors and proactively acquiring the evidence needed for satisfaction-aware decisions. These findings establish MapSatisfyBench as a benchmark for shifting map-agent evaluation from task completion toward satisfaction-aware spatial decision making.

---


### 69. [Operator Boosting Produces Pareto-Efficient PDE Surrogates](https://arxiv.org/abs/2606.17460)

**<font color=#1a73e8>作者：</font>** Lennon J. Shikhman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators are widely used as surrogate solution maps for partial differential equations (PDEs), but full-size models can be costly to store, deploy, and evaluate in many-query scientific workflows. This work introduces Operator Boosting, a stagewise residual-learning framework for constructing compact neural-operator surrogates directly, rather than training a large model and compressing it afterward. Starting from the empirical mean predictor in normalized output coordinates, the method trains a sequence of tiny same-family neural operators on residual fields and incorporates each correction through validation-selected shrinkage. We instantiate the framework with Fourier neural operators (FNOs), DeepONets, and convolutional neural operators (CNOs), and compare boosted tiny stacks against full-size monolithic baselines across one-, two-, and three-dimensional PDE benchmarks from PDEBench, APEBench, and The Well. Across 30 dataset-architecture pairs, 21 show positive mean accuracy gains and 17 have positive confidence intervals, while all boosted stacks reduce trainable parameter count by approximately 72-95%. Best-model comparisons show empirical Pareto improvements on 7 of 10 completed PDE benchmarks, including two-dimensional Navier-Stokes, shallow-water dynamics, Darcy flow, one-dimensional transport and reaction systems, and three-dimensional compressible Navier-Stokes. These results show that Operator Boosting often improves the empirical accuracy-parameter Pareto frontier of neural PDE surrogates, while also exposing PDE- and architecture-dependent regimes where residual boosting fails to offset compression.

---


### 70. [ResAware: Cross-Environment Website Fingerprinting via Resource-Privileged Distillation](https://arxiv.org/abs/2606.17462)

**<font color=#1a73e8>作者：</font>** Chongru Fan, Wei Wang, Wentao Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Website Fingerprinting (WF) attacks achieve high accuracy in controlled laboratory settings, they often degrade substantially in real-world environments due to spatio-temporal drift, browser heterogeneity, proxy obfuscation and etc. This limitation stems from their sole reliance on low-level traffic features that are noisy and highly sensitive to environmental perturbations. To address this problem, we propose \textbf{ResAware}, a cross-environment resource-aware distillation framework under a \textit{training-rich/inference-poor} asymmetric setting. Specifically, ResAware trains a teacher model on resource-level features, and then distills the resulting privileged knowledge into a student model through heterogeneous knowledge distillation. At deployment time, the student model performs inference using only encrypted traffic, incurring zero additional cost. We evaluate ResAware on a large-scale dataset collected over five months from six globally distributed vantage points, comprising more than $160{,}000$ paired samples. The results show that ResAware significantly enhances the cross-environment robustness of diverse WF baselines. Under a 150-day temporal drift, for example, ResAware improves the F1-score of Var-CNN from $72.77\%$ to $81.49\%$ and the open-world $TPR@1\%FPR$ from $22.40\%$ to $27.20\%$. Our results demonstrate that resource-level supervision improves WF robustness without expanding online observation capabilities.

---


### 71. [WeaveLA: Event Driven Cross-Subtask Latent Memory Weaving for Repetitive Robot Manipulation](https://arxiv.org/abs/2606.17463)

**<font color=#1a73e8>作者：</font>** Shoujing Zhu, Zhenyang Liu, Fungmiu Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) policies have achieved remarkable single-step manipulation, yet they remain brittle precisely where each stage depends on what was just completed. The core issue is structural: short-window VLAs lack an explicit channel for rouxting information across sub-task boundaries, and existing memory-augmented variants either write at every frame, retrieve from demonstration-time stages, or fire at sub-goal events without performing an explicit sub-task-to-sub-task hand-off into the action expert. We identify the sub-goal completion event as the natural temporal unit for cross-subtask memory hand-off, and present WeaveLA (Weave Latent memory for Vision-Language-Action policies), a cross-subtask memory interface that, on top of a frozen VLA backbone, compresses each completed segment into latent tokens via query-driven attention pooling and routes them directly into the action-generation path of the next sub-task. This event-triggered, action-side design preserves the base policy's short-window interface while adding a lightweight cross-subtask channel. Through stratified evaluation on RoboMME with a $\pi_{0.5}$ backbone, WeaveLA's gains land exactly where the channel is needed: on the hardest repetition slice (SwingXtimes, $N{=}3$), success rises from $0\%$ to $47.8\%$, while single-execution episodes remain unchanged. Per-episode paired analysis confirms the gains are confined to tasks whose causal structure requires cross-subtask information.

---


### 72. [Perron--Frobenius Operator Matching for Generative Modeling](https://arxiv.org/abs/2606.17465)

**<font color=#1a73e8>作者：</font>** Shiqi Zhang, Wuwei Wu, Jaemin Oh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Perron--Frobenius Operator Matching (PFOM), a generative framework that matches density evolution via the integral PF operator, subsuming flow, diffusion, and jump models. We prove that among Bregman divergences, only Kullback--Leibler divergence preserves equality between density-level and sample-conditioned objectives, yielding a practical loss equivalent to Koopman path matching. We further develop Nesterov-accelerated training and sampling that stabilize discretization and accelerate convergence. %On Gaussian mixtures and two-moons, PFOM achieves faster KL/$W_2$/MMD decrease and improved wall-clock efficiency with empirical validation. PFOM unifies operator-theoretic identification with modern generative modeling and opens paths to adaptive dictionaries and high-dimensional applications.

---


### 73. [ReRAM-aware Model Finetuning addressing I-V Non-linearity and Retention Errors](https://arxiv.org/abs/2606.17471)

**<font color=#1a73e8>作者：</font>** Ching-Yi Lin, Shamik Kundu, Arnab Raha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional CPU, GPU, and NPU architectures are increasingly limited by the von Neumann bottleneck. While In-Memory Computing (IMC) using ReRAM crossbar arrays offers a high-density, energy-efficient alternative, its practical deployment is constrained through their non-idealities. Existing hardware-aware training frameworks often require training from scratch, which is computationally prohibitive for modern large-scale models. In this work, we propose a finetuning-based hardware-aware training algorithm that enables robust DNN deployment on ReRAM with minimal training overhead. Our approach mitigates I-V non-linearity by applying a range-shrunk sinh transformation and incorporates retention errors directly into a regularization loss during the finetuning process. We evaluate our framework across models and tasks such as image classification and question-answering (QA). Experimental results demonstrate that our method achieves similar accuracy on large-scale models like ResNet18 and DeiT-Tiny as the base model. In-case of ImageNet for MobileNetV3 families the technique has only less than 2% accuracy degradation. Further, applying the technique on the SQuAD v2 dataset results in only 1 point degradation of F-1 score.

---


### 74. [StereoFactory: A Unified Merging Framework for Robust Stereo Matching](https://arxiv.org/abs/2606.17475)

**<font color=#1a73e8>作者：</font>** Xianda Guo, Pinhan Fu, Ruilin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereo matching has advanced through foundation models trained on large-scale datasets, yet this paradigm suffers from a scalability bottleneck: incorporating new data requires costly joint retraining. Model merging offers a scalable post-hoc alternative by integrating knowledge from specialized models after source checkpoints are available. However, existing merging methods typically retain all available models or rely on greedy inclusion, which can preserve harmful task-vector interference. We propose StereoFactory, a coarse-to-fine evolutionary framework for adaptive model merging. Stage~1 employs a genetic algorithm to search the combinatorial space of model subsets, determining which models should participate. Stage~2 addresses module-level knowledge specialization (different functional modules exhibit distinct preferences for knowledge sources) through CMA-ES optimization of architecture-adaptive routing over the selected task vectors, with optional module-level scaling. Experiments across two architectures and four benchmarks demonstrate that StereoFactory consistently achieves the best four-benchmark average under the same checkpoint pool, reducing the average error from 3.80 to 3.30 on NMRF and from 2.88 to 2.19 on FoundationStereo relative to the strongest controlled baseline. The post-hoc search requires only 2.7--3.7\% of the corresponding joint-retraining wall-clock time. Analysis reveals that knowledge contributions are inherently module-specific, and selected subsets can transfer across architectures with minimal degradation. Code will be publicly released upon acceptance at: this https URL.

---


### 75. [Multi-Adapter PPO: A Cross-Attention Enhanced Wavelength Selection Framework for LIBS Quantitative Analysis](https://arxiv.org/abs/2606.17476)

**<font color=#1a73e8>作者：</font>** Hao Li, Man Fung Zhuo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Laser-induced breakdown spectroscopy (LIBS) quantitative analysis faces critical challenges in wavelength selection due to high-dimensional spectral data and the fundamental trade-off between prediction accuracy and feature efficiency. This paper presents a novel Multi-Adapter PPO framework that transforms wavelength selection into a reinforcement learning problem, leveraging cross-attention mechanisms and multiple specialized adapters to capture complex spectral relationships. Our approach outperforms traditional Particle Swarm Optimization (PSO) by an average of 28.4\% in comprehensive score and 45.2\% in prediction accuracy across steel and coal datasets. The proposed method demonstrates superior performance in balancing prediction accuracy with feature efficiency, achieving state-of-the-art results in LIBS quantitative analysis while maintaining interpretability and computational efficiency. We released our code and dataset here: this https URL

---


### 76. [Theoretical Grounding of Out-Of-Distribution Detection With Reinforcement Learning Optimizer](https://arxiv.org/abs/2606.17477)

**<font color=#1a73e8>作者：</font>** Salimeh Sekeh, Xin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) detection in dynamic open-world environments requires a model to continually adapt to evolving data distributions while generalizing to covariate-shifted inputs and rejecting semantic-shifted OOD examples. Most existing OOD detection methods optimize only the current-step objective and do not explicitly account for how post-deployment environment changes affect future OOD behavior. In this paper, we establish a theoretical grounding for dynamic OOD detection using a reinforcement learning (RL)-guided optimizer that explicitly favors updates that reduce the semantic OOD false positive rate over time. We develop a novel augmented optimizer that uses an RL-guided correction term on top of standard gradient descent (GD) and show its improvement over both future-domain generalization and semantic-OOD rejection. We analyze temporal error decomposition in terms of model-change and environment-change generalization errors and develop a new theoretical framework for comparing the generalization errors under both GD and RL-guided optimizers.

---


### 77. [GeneralVLA-2: Geometry-Aware Reconstruction and Governed Memory for Robot Planning](https://arxiv.org/abs/2606.17480)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Guoqing Ma, Zeyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalist vision-language-action systems need object-centric 3D evidence and reusable manipulation experience to plan reliable robot trajectories. GeneralVLA provides a hierarchical interface for converting language and RGB-D observations into 3D end-effector paths, but two bottlenecks remain. First, monocular SAM3D-style object reconstruction can hallucinate pose and unseen geometry, while manipulation benefits from stable object shape when calibrated multi-view observations are available. Second, the original KnowledgeBank mainly retrieves semantically similar snippets and appends new knowledge, which makes it difficult to control memory quality, conflicts, confidence, and geometric relevance. To address the first challenge, we introduce GeoFuse-MV3D, a geometry-prior-guided MV-SAM3D reconstruction branch that verifies external geometry cues with input-view masks, applies soft visual-hull support, performs axis-wise refinement, and fuses only geometry while preserving appearance. To address the second challenge, we upgrade KnowledgeBank into a governed long-term memory system with explicit quality, confidence, lifecycle, verifier, and conflict metadata, together with precision-oriented retrieval. Finally, we evaluate the reconstruction branch on GSO-30 and the memory module on Terminal-Bench 2.0 and SWE-Bench Verified; GeoFuse-MV3D improves over the MV-SAM3D baseline by reducing CD and LPIPS by 2.20% and 2.02% while increasing PSNR and SSIM by 2.36% and 1.03%, and KnowledgeBank improves over ReasoningBank by 4.53% on Terminal-Bench SR and 3.73% on SWE-Bench resolve rate, while reducing AS by 4.95% and 5.65%, respectively. Code: this https URL. Website: this https URL.

---


### 78. [Reconfigurable Computing Challenge: Transformer for Jet Tagging on Versal AI Engines](https://arxiv.org/abs/2606.17500)

**<font color=#1a73e8>作者：</font>** Gram Koski, Sean Lipps, Zhenghua Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based models achieve strong performance for jet tagging at the CERN LHC, but deploying them in low-latency, resource-constrained trigger systems is challenging. We present an initial implementation of a quantized, integer-only transformer for jet tagging on the AMD Versal AI Engine (AIE), mapping dense and multi-head attention (MHA) layers to AIE tiles. The main contribution is a reusable software framework that represents transformer layers as composable AIE building blocks and automatically generates the corresponding Vitis graph code from a high-level Python model description. This framework provides a foundation for future research and is released as open-source software at this https URL.

---


### 79. [When the Next Step Is Not One Step: Distribution-Aware Execution Modeling for Concurrent Go Programs](https://arxiv.org/abs/2606.17508)

**<font color=#1a73e8>作者：</font>** Kaviru Hapuarachchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training a model to predict the next step in a concurrent program is harder than it looks: two runs of the same program from the same trace prefix can produce different next events, both valid, because the scheduler is nondeterministic. A model trained against a single label is learning to guess one outcome of a random process. We turn this around and use the nondeterminism as a training signal. We run each program many times, aggregate the observed next events into an empirical distribution, and fine-tune a 7B model to match that distribution with a KL objective. On 798 held-out predictions drawn from real production Go bugs (CockroachDB, Kubernetes, gRPC, etcd), fine-tuning on fewer than a thousand traces reaches 36.2% accuracy, ahead of Gemini 3.5 Flash used zero-shot (34.8%) and the same model without fine-tuning (28.6%). Distribution training matches cross-entropy on accuracy (35.8% vs. 36.2%) while reducing Expected Calibration Error from 0.205 to 0.169. We also derive a formal goroutine-leak signature for a class of select-blocked goroutines where P(GoUnblock)=0 holds by scheduler semantics, not by learning. We release the dataset, trained adapters, and all tooling.

---


### 80. [MedEasy: Designing AI Standardized Patients for Clinical Consultation Training](https://arxiv.org/abs/2606.17512)

**<font color=#1a73e8>作者：</font>** Zhiqi Gao, Huarui Luo, Guo Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI standardized patients are becoming a setting for professional training in clinical consultation. This paper presents MedEasy, a multi-agent system that organizes virtual-patient practice through patient dialogue, clinical actions, decision submission, documentation, and feedback. We first conducted a formative study with 12 clinical-year medical students through interviews and three co-design workshops. The findings informed a staged workflow, structured case records, action-contingent findings, and trajectory-based review. We then conducted an evaluative user study with a separate cohort of 12 clinical-year medical students, with each participant completing two counterbalanced cases. Learners interpreted MedEasy as a connected consultation environment. They used patient responses, examination findings, available actions, and feedback together to judge whether the represented case remained coherent. They valued repeatable practice and recorded review, while questioning missing actions and feedback criteria. The paper contributes design implications for AI-supported professional training systems that use case-specific standards to connect situated practice.

---


### 81. [Geometry-Aware Post-Hoc Uncertainty Quantification in Operator Learning](https://arxiv.org/abs/2606.17513)

**<font color=#1a73e8>作者：</font>** Oriol Vendrell-Gallart, Nima Negarandeh, Ramin Bostanabad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators provide fast surrogates for PDEs but their deterministic predictions limit their use in tasks requiring uncertainty quantification (UQ), especially under geometric variability. Existing approaches primarily model uncertainty in network parameters, largely overlooking the geometry-aware representations learned by the operator itself. We propose REEF-GP (Residual on Embedded Features Gaussian Process), a post-hoc UQ framework that fits a GP to the residuals of a frozen neural operator whose internal embeddings define the kernel feature space. Rather than learning a separate feature map, REEF-GP adapts the operator's intrinsic coordinate-feature representations to construct geometry-aware uncertainties. To ensure stability and scalability on unstructured domains, REEF-GP incorporates spectral-normalized projections, heteroscedastic geometry-aware noise, and efficient subset-based training that avoids restrictive low-rank approximations. Across five PDE benchmarks with varying geometries, REEF-GP preserves predictive accuracy while achieving calibrated uncertainty estimates competitive with deep ensembles but at a fraction of their cost. Our approach remains robust under geometric distribution shift, with uncertainty concentrating in physically meaningful regions (e.g., shock fronts). Our results demonstrate that accurate and scalable post-hoc UQ for neural operators can be achieved directly in their learned feature space, offering a practical alternative to parameter-centric approaches.

---


### 82. [FoundCause: Causal Discovery with Latent Confounders from Observational Data](https://arxiv.org/abs/2606.17516)

**<font color=#1a73e8>作者：</font>** Patrick Blöbaum, Krishnakumar Balasubramanian, Shiva Prasad Kasiviswanathan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery from observational data remains challenging due to the need to recover directed structure and latent confounding without interventions. We propose FoundCause, an amortized causal discovery model trained entirely on synthetic data that maps datasets directly to causal graphs in a single forward pass. By learning from large collections of simulated structural causal models, FoundCause captures transferable statistical patterns that generalize beyond individual datasets. The architecture incorporates several key inductive biases for causal discovery. It uses a permutation-invariant transformer encoder with alternating attention over samples and variables to jointly model cross-variable dependence and per-variable distributions. Pairwise statistical features derived from classical asymmetry measures are injected through statistics-conditioned attention, guiding the model toward known causal signals. A factorized decoder separates edge existence from direction, while a triangular refinement module enables reasoning over higher-order causal motifs such as chains and colliders. In addition, a dedicated confounder module based on learnable latent tokens explicitly models hidden common causes, and the model explicitly handles missing data via its masked input representation. To our knowledge, FoundCause is the first amortized causal discovery approach to explicitly model latent confounding. FoundCause outperforms 11 classical non-amortized methods (e.g., PC, GES, NOTEARS-style optimization) and 4 amortized causal discovery methods on 15 real-world datasets, achieving +9.6% improvement in $F_1$, +1.2% in AUROC, and an 18.9% reduction in structural Hamming distance relative to the strongest non-amortized methods, while performing inference in a single forward pass.

---


### 83. [Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery](https://arxiv.org/abs/2606.17519)

**<font color=#1a73e8>作者：</font>** Kellen Gillespie, Robyn Perry  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production LLM assistants route user requests to growing libraries of specialized tools, but how does routing accuracy degrade as the catalog scales? We study single-step routing on a 110-agent, 584-tool catalog from a deployed enterprise productivity assistant, evaluating three frontier models from 10 to 110 agents. Routing F1 on under-specified requests drops 16--23 percentage points across models. An oracle analysis decomposes the degradation into a \emph{retrieval} gap (the model cannot surface the right tool) and a \emph{confusion} gap (even with perfect retrieval, the oracle ceiling drops 10pp). Embedding-based shortlisting recovers +10--11pp F1 at full scale across all three models and two providers. A production annotation study (1,435 human-labeled utterances, three annotators) confirms the recovery on real traffic at +10--17pp despite 10--15pp lower absolute performance.

---


### 84. [An expressivity analysis of hierarchical modelling in deep transformers via bounded-depth grammars](https://arxiv.org/abs/2606.17522)

**<font color=#1a73e8>作者：</font>** Vinoth Nandakumar, Qiang Qu, Pramod Thebe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are widely believed to derive their expressive power from their ability to form \textbf{hierarchical representations}, capturing progressively more abstract and compositional features across layers. In language modeling, \textbf{transformers} have emerged as the dominant architecture, with early layers capturing local syntactic patterns and later layers encoding more complex clause-level dependencies. While this intuition has shaped model design, there remains a lack of rigorous theoretical work demonstrating \textbf{how} deep transformers represent such hierarchical structures. In this work, we analyze the expressiveness of deep transformer models through the formal lens of bounded-depth, non-recursive context-free grammars. For this class of grammars, we explicitly construct transformers with positional attention whose depth grows linearly with grammar depth, while the neuron count scales with the number of derivation-tree shapes and quadratically with the number of production rules. Our theoretical results support the linear representation hypothesis by demonstrating that these architectures possess the structural capacity to encode abstract grammatical states into low-dimensional, linearly separable subspaces within the residual stream.

---


### 85. [Non-negative Matrix Factorisation with Topological Regularisation](https://arxiv.org/abs/2606.17531)

**<font color=#1a73e8>作者：</font>** Matias de Jong van Lier, Shizuo Kaji, Keunsu Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the learning of interpretable bases in non-negative matrix factorisation (NMF) by regularising the topology of the learned basis functions. Our approach is motivated by the observation that many data modalities can be viewed as non-negative functions on a structured domain, where the quality of a basis is intrinsically linked to its topology. However, naive methods for incorporating the topology of the support are often hindered by discreteness and threshold dependence, rendering them unsuitable for continuous optimisation. We address these challenges by employing persistent homology as a stable, threshold-free topological quantifier and by designing topological scores that integrate into the NMF objective as regularisers. The resulting framework encompasses spatially coherent image components, periodic time-series structures, and clique-like graph signals within a unified modelling language.

---


### 86. [SNAS: A Multi-Layer Defense-in-Depth Architecture for Secure Egress in Sandboxed Workloads](https://arxiv.org/abs/2606.17533)

**<font color=#1a73e8>作者：</font>** Niranjan Kumar Sharma, S Muralidhar, Samy Boshra-Riad 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Snowpark enables data engineering and AI/ML workloads in Snowflake by executing user-defined functions in secure sandboxes. Many of these workloads require external connectivity to access cloud APIs, external databases, or feature stores, creating a dependability challenge: how to provide transparent network access while preserving strict multi-tenant isolation and resource fairness. This paper presents Secure Network Access in Snowpark (SNAS), a production architecture for secure external communication from sandboxed workloads. SNAS combines Extended Berkeley Packet Filter (eBPF) packet filtering, Generic Network Virtualization Encapsulation (GENEVE) overlay networks, and distributed egress proxies for policy-driven egress control with low overhead. We describe the design, deployment, and measured production behavior of SNAS, including an eBPF-based bandwidth limiter using the Earliest Departure Time (EDT) algorithm, dual-tier policy enforcement, and safeguards for connection limiting and port exhaustion. SNAS is deployed across all Snowflake regions and supports large-scale production workloads including petabyte-scale data transfer and latency-sensitive external integrations.

---


### 87. [TaFD: Threat-Aware Frequency Decoupling for Adversarial Robustness against Heterogeneous Attacks](https://arxiv.org/abs/2606.17540)

**<font color=#1a73e8>作者：</font>** Mengda Xie, Yiling He, Meie Fang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-threat robustness remains a fundamental challenge in deep learning. Although joint adversarial training (JAT) is widely adopted, it suffers from negative transfer under heterogeneous threats, particularly between $\ell_p$-bounded and semantic attacks. Through first-order gradient analysis, we formalize this as gradient incompatibility and theoretically establish the necessity of decoupled optimization. We further reveal that these conflicting threats exhibit separable spectral characteristics in the frequency domain. Motivated by this observation, we propose Threat-aware Frequency Decoupling (TaFD), a two-stage defense framework that reformulates JAT as a frequency-domain divide-and-conquer paradigm. TaFD first discovers latent threat domains via unsupervised clustering of attack spectral prototypes and trains a lightweight classifier for inference-time threat domain identification. Conditioned on the prediction, TaFD employs a Frequency-Conditional Convolution that learns threat-domain-specific spectral masks and routes each sample to the corresponding expert, enforcing structural parameter separation and alleviating optimization conflicts.
We validate TaFD on three representative image-classification benchmarks (CIFAR-10, CIFAR-100, and Tiny-ImageNet) and on two representative architectures (the convolutional ResNet and the hybrid-transformer MobileViT). Extensive results demonstrate that TaFD achieves more balanced robustness against heterogeneous attacks than existing JAT and frequency-domain baselines, improving average robust accuracy by approximately 11\% over the strongest baseline while maintaining leading clean accuracy.

---


### 88. [Offline Preference-Based Trajectory Evaluation](https://arxiv.org/abs/2606.17541)

**<font color=#1a73e8>作者：</font>** Fernando Diaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline evaluation of agentic systems often collapses trajectories to terminal success, discarding information about partial progress and inducing widespread ties, creating substantial statistical inefficiency by reducing effective sample size and weakening the ability to distinguish systems. We propose preference-based trajectory evaluation, which compares trajectories directly through temporal preferences over progress and time-to-return profiles. We find that, across diverse agentic and interactive benchmarks, standard success-based metrics produce tied comparisons on roughly 75% of instances, whereas trajectory-aware preferences reduce ties to roughly 35%, improving discriminative power, ranking stability, and data efficiency. Our results suggest that benchmark saturation, often attributed to poor data collection or problem difficulty, may also be explained by the choice of evaluation measure.

---


### 89. [Continuous-time Optimal Stopping through Deep Reinforcement Learning](https://arxiv.org/abs/2606.17545)

**<font color=#1a73e8>作者：</font>** Cosmin Borsa, Michael Ludkovski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulation based solvers for optimal stopping problems must discretize the stopping decision. Under classical dynamic programming, a coarse exercise grid with only a few stopping opportunities can materially undervalue the optimal expected reward, whereas on a very fine grid, approximation errors accumulate through the backward recursion. To remove this limitation, we develop a new reinforcement-learning inspired algorithm that enables us to learn the exercise rule at arbitrarily fine time resolution. Our CARLOS (Continuous-time Adaptive Reinforcement Learning for Optimal Stopping) algorithm utilizes an aggregate deep neural network (ADNN) to learn a joint space-time decision boundary. Starting from a coarse time grid, we progressively increase the frequency of stopping opportunities, while in parallel training the ADNN to refine its timing-value estimates. We moreover design an adaptive sampling strategy that gradually concentrates training effort near the stopping boundary. Benchmarked results show that CARLOS delivers higher prices than existing Bermudan solvers, approaching the American upper bound, and achieves high computational efficiency relative to non-RL comparators.

---


### 90. [Reversal Q-Learning](https://arxiv.org/abs/2606.17551)

**<font color=#1a73e8>作者：</font>** Aditya Oberai, Seohong Park, Sergey Levine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative generative modeling techniques, such as flow matching, provide powerful tools to model complex behaviors for effective offline reinforcement learning (RL). In this work, we propose a new off-policy RL algorithm that trains a flow policy based on prior data. Our idea starts from the "expanded" Markov decision process (MDP) framework, which treats individual flow refinement steps as separate actions in an MDP. To enable off-policy RL within this framework, we apply two techniques: we generate virtual on-policy trajectories (by "reversing" flows) to make this framework compatible with prior data, and we apply a bias-and-variance reduction technique to mitigate the curse of horizon in off-policy RL. We call the resulting algorithm Reversal Q-learning (RQL). RQL has several advantages over previous flow-based RL methods: it does not suffer from backpropagation through time, makes better use of the learned value function, and directly trains the full, expressive flow policy. Through our experiments on 50 challenging simulated robotic tasks, we show that RQL leads to the best average offline RL performance compared to state-of-the-art flow-based offline RL algorithms.

---


### 91. [SpatioTemporal Causal Network Diagnostics for Geographic Tipping Point Early Warning](https://arxiv.org/abs/2606.17553)

**<font color=#1a73e8>作者：</font>** Zhaoyuan Yu, Zhangyong Liang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geographic tipping points in ecosystems, climate subsystems, or ice sheets pose severe challenges for localized early warning. Classical spatial indicators such as Moran's I summarize global spatial structure, but they struggle with three issues: spatial dilution, Euclidean assumptions, and correlated noise. This paper introduces SpatioTemporal Causal Network Diagnostics (ST-CND), a framework that addresses these three issues by representing the geographic field as a time-evolving directed causal network. The core workflow is as follows: (1) infer which spatial nodes help predict other nodes via transfer entropy, replacing fixed Euclidean neighborhoods with data-driven information-flow topology; (2) estimate local recovery rates within each candidate subnetwork via dynamic mode decomposition; and (3) identify the most vulnerable subnetwork by combining three signals, namely high internal fluctuation, high internal synchronization, and low external coupling, thereby suppressing false alarms from spatially correlated noise. Validated on synthetic bifurcations and two observational sea-surface temperature benchmarks, namely Indo-Pacific SST and North Atlantic AMOC, ST-CND delivers localized and interpretable warnings. On the AMOC task, it achieves an AUROC of 0.783 and a critical-subnetwork IoU of 0.378, outperforming recurrence-network and lambda-AR1 baselines. The framework provides an interpretable and scalable pipeline for spatial early warning in Earth system science.

---


### 92. [An AI Security Agent for Banking: Multi-Vector Fraud and AML Detection Across Retail and Corporate Accounts](https://arxiv.org/abs/2606.17555)

**<font color=#1a73e8>作者：</font>** Joseph Walusimbi, Joshua Benjamin Ssentongo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Banks simultaneously face signature-based fraud (card-not-present attacks, account takeover, ATM cloning) and behavioural financial crime (structuring, layering, mule networks, business email compromise) -- two threat families with fundamentally different detection requirements. Static rule engines that reliably catch brute-force and high-velocity events are structurally blind to business-email-compromise (BEC) payment redirection, session hijacking, and money-laundering layering, which are engineered to appear indistinguishable from legitimate activity at the individual transaction or session level. This paper presents an AI security agent for retail and corporate banking that addresses this gap through a three-component fusion architecture operating on two parallel event streams: a transaction stream (card fraud, ACH/wire fraud, AML categories) and a session stream (account takeover, session hijacking, SIM-swap, insider abuse). Each stream combines an LSTM sequence model capturing per-account behavioural history, a statistical velocity/threshold monitor, and a graph/network module capturing account-counterparty relationship patterns (fan-in, fan-out, pass-through ratio) for money-laundering detection. Experiments on a synthetic event log of 237,669 transactions and 113,508 sessions across 13 threat categories and 3,470 simulated accounts demonstrate overall F1 of 0.787 (transaction stream) and 0.867 (session stream) for the proposed model, versus 0.562/0.733 for a rule-based baseline and 0.655/0.713 for an LSTM-only baseline. The agent includes a customer-facing transaction-verification chatbot (96.6% identity verification accuracy, 86.8% mass-reset attack detection) and an analyst case-summary assistant (99.3% action-recommendation F1), with Critical-tier automated response latency under 0.43 ms at the 95th percentile.

---


### 93. [Universal Image Restoration via Internalized Chain-of-Thought Reasoning](https://arxiv.org/abs/2606.17557)

**<font color=#1a73e8>作者：</font>** Yu Guo, Zhengru Fang, Shengfeng He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration seeks to recover high-quality images from degraded inputs but becomes highly ill-posed under complex, mixed degradations. While unified all-in-one models are common, their performance declines as degradation complexity increases. Recent works adopt Chain-of-Thought (CoT) reasoning for multi-round restoration using specialized modules. However, this approach faces two key limitations: (i) increased computational cost due to multi-step processing, and (ii) weak modeling of interactions between degradations during stepwise inference. We introduce CoTIR, a universal image restoration framework that internalizes CoT reasoning within a single model. Concretely, we view image restoration as a specialized subtask of image editing, which implies that a large-scale pre-trained editing model provides a more favorable optimization starting point. Building on this, we fine-tune the model for restoration and further encode structured CoT-style reasoning into the learning objective via a differentiable formulation inspired by Lagrangian optimization, enabling holistic restoration without chaining specialized restorers. To facilitate training and evaluation, we further present CoTIR-Bench, a large-scale benchmark comprising 5.2 million samples with CoT-style reasoning traces. Extensive experiments on CoTIR-Bench and broad real composite degradation scenes show that CoTIR achieves stronger perceptual quality and more competitive fidelity than both all-in-one models and multi-round restoration methods. The source code is available at this https URL.

---


### 94. [RT-Counter: Real-Time Text-Guided Open-Vocabulary Object Counting](https://arxiv.org/abs/2606.17561)

**<font color=#1a73e8>作者：</font>** Hao-Yuan Ma, Li Zhang, Zhiwei Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided open-vocabulary object counting (TOOC) aims to count objects belonging to the categories specified by natural language descriptions. Although vision-language pre-trained models have been successful applied to TOOC tasks, they still struggle with fine-grained spatial understanding and real-time inference requirements in counting scenarios. To address these limitations, this paper proposes a real-time TOOC framework, called the Real-Time Counter (RT-Counter), that achieves not only good counting accuracy but also high computational efficiency. RT-Counter designs a novel Visual Prototype Textualization (VPT) module that can project learned visual features into a text feature space and then generate features containing the abstract information that is hard to capture with visual prototypes and the detailed prototype information that is difficult to describe in text, enhancing the object-level visual-language model's counting capabilities. Additionally, RT-Counter incorporates our Weaving Transformer (Weaformer) layers, maintaining high descriptive power at a fraction of the computational cost. The Weaformer layer adopts a novel hybrid attention mechanism that can efficiently weave together local and global visual features. Extensive experiments on three public datasets show that RT-Counter successfully breaks the accuracy-speed trade-off in TOOC. While achieving a competitive MAE of 13.30 on FSC147, RT-Counter operates at 112.48 FPS, making it 7.4x faster and over 4$\times$ more parameter-efficient than the existing leading methods in TOOC. Our work aims at balancing high accuracy and real-time performance in TOOC. Code is available at: this https URL.

---


### 95. [Anywhere, Any-Stymie: Remote Activation of Trojan Malware on LiDAR with Modulated Signals](https://arxiv.org/abs/2606.17562)

**<font color=#1a73e8>作者：</font>** R. Spencer Hallyburton, Miroslav Pajic  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LiDAR sensors are widely deployed in autonomous systems for 3D perception and safety-critical decision-making. We identify a previously unexplored attack surface in which dormant malware embedded in the LiDAR sensing pipeline remains inactive during normal operation and can be externally triggered after deployment, without requiring access to sensor hardware or networking at attack time. To operationalize this threat, we design malware capable of low-level point-cloud manipulation and embed it into LiDAR firmware. This malware was developed in a closed research test environment with vendor technical support, rather than by exploiting an inherent production supply-chain vulnerability. To selectively trigger attack activation, we design and implement an optical trigger that remotely activates the malware by delivering a modulated signal into the sensing environment. Once triggered, the malware performs real-time point cloud manipulation, and we demonstrate false object injection and real object suppression on static and mobile victim platforms. Our evaluation first establishes attack feasibility, including static operation at 300~ft and recorded drive-by runs reaching 35~mph. We then illustrate quantitatively that injected person-like artifacts can remain semantically detectable by a state-of-the-art 3D object detector. Finally, we demonstrate multiple modes of safety-critical impact on a deployed tactical autonomous vehicle. Together, these results highlight the need for stronger integrity guarantees throughout the LiDAR sensor development and deployment pipeline.

---


### 96. [Reducing Learner Redundancy in Boosting via Residual Orthogonalization](https://arxiv.org/abs/2606.17567)

**<font color=#1a73e8>作者：</font>** Ye Su, Jipeng Guo, Yong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While sequential residual fitting is the bedrock of standard boosting frameworks, it inherently breeds learner redundancy by repeatedly revisiting correlated error components. To address this bottleneck, we propose a shift from residual fitting to \textit{residual orthogonalization} and introduce SCBoost. Our framework tackles redundancy through two complementary mechanisms: Spectral Residual Projection (SRP) and Covariance-Regularized Weighting (CRW). During training, SRP projects each residual target onto the orthogonal complement of the historical prediction subspace, forcing successive learners to capture only novel empirical innovations. During aggregation, CRW optimizes ensemble weights on a validation set with an explicit covariance penalty to mitigate remaining correlations. Theoretically, we provide a finite-sample geometric characterization proving that SRP yields an exact additive residual-energy decomposition. Furthermore, under an isotropic-noise assumption, we rigorously establish the conditions under which this projection improves the effective Signal-to-Noise Ratio. Extensive experiments across ten benchmark datasets demonstrate that SCBoost delivers strong out-of-the-box performance, particularly in accuracy and F1 score. This work reinterprets boosting through a geometric lens, suggesting that explicit redundancy control is a principled and necessary step toward more efficient ensemble architectures.

---


### 97. [When Dynamics Models Read the Wrong Time Steps: Label-Free Event Credit Re-Anchoring for Robust Global Readouts](https://arxiv.org/abs/2606.17572)

**<font color=#1a73e8>作者：</font>** Yifan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned dynamics models often answer global physical questions, such as fault severity or impact stiffness, by pooling a per-step feature sequence into one readout vector. This sequence-to-global interface creates an under-studied temporal credit problem: with only trajectory-level supervision, a model can predict accurately in training conditions while reading from abundant smooth correlates rather than the brief physical events that determine the target. We call this failure temporal credit dilution. It is not exposed by the training loss and is not removed by standard physics-informed residuals, because the error lies in where the global readout assigns functional credit. We introduce Credit-in-Event, an interface-level probe for measuring how much pooled credit lands on event steps, and prove in closed form that a pooled linear reader routes credit to a spurious background channel as the event fraction shrinks. We then propose CREST, a training-free and label-free readout that estimates a transient event core from learned features and re-anchors the pooled representation through event-versus-rest contrast. Across simulated gear and impact systems, recurrent and attention encoders, and public bearing vibration data, CREST reduces out-of-distribution error while restoring event credit. Ablations show that stable-step selection and receptive-field shrinking fail, confirming that the gain comes from event-core credit re-anchoring rather than a generic locality or stability prior.

---


### 98. [DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack](https://arxiv.org/abs/2606.17574)

**<font color=#1a73e8>作者：</font>** Siyi Li, Chunyu Sun, Jiahao Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating a Physical AI stack spans operators that differ by more than three orders of magnitude -- from a single foundation-model decoding step to thousands of physics ticks of whole-body control -- varying orthogonally in modality, reward semantics, and resource profile. No existing framework spans this range, so the stack is evaluated today by stitching together separate harnesses that share neither runtime nor scoring, preserving each segment's local validity but losing the shared identity needed to diagnose cross-layer regressions. We present DeepInsight, an evaluation infrastructure that serves this full spectrum on a single runtime. Rather than homogenize the regimes, it preserves their heterogeneity behind three narrow abstractions -- task, resource, and result -- each realized as one invariant shared by every subsystem: one episode driver, one resource-handle protocol implemented by every expensive backend (LLM inference and sandboxed runtimes alike), and one trace identity scheme under which every event is written. Deployed in production across all three layers of an embodied humanoid stack, this single set of invariants onboards new benchmarks largely by configuration. Where mature peer orchestrators exist -- at the foundation-model end -- it reproduces published references and peer-framework readings within their own spread, runs the same suites faster on a single node, and scales near-linearly across nodes. Its distinctive return is diagnostic: because every layer writes into one shared trace, a regression that begins in one layer and surfaces in another stays localizable on that trace -- a cross-layer payoff no federation of per-segment harnesses can reproduce.

---


### 99. [Root-Selecting Fixed-Point Inversion for Rectified Flows via Trajectory Straightness](https://arxiv.org/abs/2606.17584)

**<font color=#1a73e8>作者：</font>** Semin Kim, Jihwan Yoon, Seunghoon Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finding the initial noise that generates a given data sample, known as inversion, is a key component for downstream applications such as training-free image editing. Existing fixed-point inversion methods improve inversion accuracy by formulating each inversion step as a fixed-point problem, but they lack a principled mechanism for selecting among multiple fixed-point solutions that can arise in practice. We observe that different selections induce different inversion trajectories, leading to substantial variation in reconstruction and editing quality. For rectified flows, we further find that this variation is closely associated with trajectory straightness, motivating straightness as a principled selection criterion. We propose SelFix, a fixed-point inversion method that selects fixed-point solutions inducing straighter inverse trajectories while retaining convergence to an exact inverse root under standard local assumptions. Experiments on FLUX.1-dev and PIE-Bench show that SelFix improves fixed-point inversion, achieving stronger real-image reconstruction and better source-preserving prompt-based editing than prior inversion baselines. The code is available at this https URL.

---


### 100. [TivTok: Broadcasting Time-Invariant Tokens for Scalable Video Tokenization](https://arxiv.org/abs/2606.17590)

**<font color=#1a73e8>作者：</font>** Weiliang Chen, Yuanhui Huang, Xuebo Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video tokenization is fundamental to scalable video generation, as the number of tokens directly determines the computational cost and the length of videos that can be modeled. Existing tokenizers mainly improve scalability by compressing videos into fewer tokens, but they often continue to represent persistent content, such as static backgrounds and consistent object appearances, repeatedly across frames and chunks. In this paper, we propose \textbf{TivTok} (\textit{Time-Invariant Tokenizer}), a reuse-aware video tokenizer that makes persistent information reusable across time. TivTok represents a clip with Time-Invariant (TIV) tokens that encode information shared across frames and Time-Variant (TV) tokens that encode frame-specific residuals. To obtain this factorization, we introduce Scope-Induced Factorization (SIF), which assigns different attention scopes to the two token groups: TIV tokens attend to the full clip, whereas each TV token only accesses its corresponding frame together with the TIV tokens. In the decoder, Invariant Broadcasting (IB) reuses the same TIV tokens across frames and chunks for parallel reconstruction and long-video tokenization. Experiments show that TivTok achieves an rFVD of 12.65 on the standard $16{\times}256{\times}256$ benchmark and improves compression efficiency by 2.91$\times$ for 128-frame videos compared with the evaluated baselines, while using only 1.1\% of the tokens required by downsample-based tokenizers in our evaluation.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-205](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
