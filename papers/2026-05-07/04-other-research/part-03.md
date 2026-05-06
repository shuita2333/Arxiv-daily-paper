# 📦 其他研究 | 2026年05月07日

> 本类共 **213** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-213](./part-05.md)

---

### 101. [Enhancing Self-Supervised Talking Head Forgery Detection via a Training-Free Dual-System Framework](https://arxiv.org/abs/2605.03390)

**<font color=#1a73e8>作者：</font>** Ke Liu, Jiwei Wei, Shuchang Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised talking head forgery detection faces severe generalization challenges due to the continuous evolution of generators. By reducing reliance on generator-specific forgery patterns, self-supervised detectors offer stronger cross-generator robustness. However, existing research has mainly focused on building stronger detectors, while the discriminative capacity of trained detectors remains insufficiently exploited. In particular, for score-based self-supervised detectors, the limited discriminative ability on hard cases is often reflected in unreliable anomaly ordering, leaving room for further refinement. Motivated by this observation, we draw inspiration from the dual-system theory of human cognition and propose a Training-Free Dual-System (TFDS) framework to further exploit the latent discriminative capacity of existing score-based self-supervised detectors. TFDS treats anomaly-like scores as the basis of System-1, using lightweight threshold-based routing to partition samples into confident and uncertain subsets. System-2 then revisits only the uncertain subset, performing fine-grained evidence-guided reasoning to refine the relative ordering of ambiguous samples within the original score distribution. Extensive experiments demonstrate consistent improvements across datasets and perturbation settings, with the gains arising mainly from corrected ordering within the uncertain subset. These findings show that existing self-supervised talking head forgery detectors still contain underexploited discriminative cues that can be effectively unlocked through training-free dual-system reasoning.

---


### 102. [PODiff: Latent Diffusion in Proper Orthogonal Decomposition Space for Scientific Super-Resolution](https://arxiv.org/abs/2605.03399)

**<font color=#1a73e8>作者：</font>** Onkar Jadhav, Tim French, Matthew Rayson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic super-resolution of high-dimensional spatial fields using diffusion models is often computationally prohibitive due to the cost of operating directly in pixel space. We propose PODiff, a structured conditional generative framework that performs diffusion in a fixed, variance-ordered Proper Orthogonal Decomposition (POD) coefficient space, exploiting the orthogonality of POD modes to impose an interpretable, variance-ordered latent geometry. This design enables efficient ensemble generation, preserves dominant spatial structure, and yields spatially interpretable, well-calibrated uncertainty at substantially lower computational cost. We evaluate PODiff on sea surface temperature downscaling over the West Australian coast and on a controlled advection-diffusion benchmark. PODiff achieves reconstruction accuracy comparable to pixel-space diffusion while requiring significantly less memory and producing more reliable uncertainty estimates than deterministic and Monte Carlo Dropout baselines.

---


### 103. [TsallisPGD: Adaptive Gradient Weighting for Adversarial Attacks on Semantic Segmentation](https://arxiv.org/abs/2605.03405)

**<font color=#1a73e8>作者：</font>** Alexander Matyasko, Xin Lou, Indriyati Atmosukarto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attacking semantic segmentation models is significantly harder than image classification models because an attacker must flip thousands of pixel predictions simultaneously. Standard pixel-wise cross-entropy (CE) is ill-suited to this setting: it tends to overemphasize already-misclassified pixels, which slows optimization and overstates model robustness. To address these issues, we introduce TsallisPGD, an adversarial attack built on the Tsallis cross-entropy, a generalization of CE parameterized by $q$, which adaptively reshapes the gradient landscape by controlling gradient concentration across pixels. By varying $q$, we steer the attack toward pixels at different confidence levels. We first show that no single fixed-$q$ is universally optimal, as its effectiveness depends on the dataset, model architecture, and perturbation budget. Motivated by this, we propose a dynamic $q$-schedule that sweeps $q$ during optimization. Extensive experiments on Cityscapes, Pascal VOC, and ADE20K show that TsallisPGD, using a single validation-selected schedule, achieves the best average attack rank across all evaluated settings and improves over CEPGD, SegPGD, CosPGD, JSPGD, and MaskedPGD in reducing accuracy and mIoU on both standard and robust models.

---


### 104. [Robust Agent Compensation (RAC): Teaching AI Agents to Compensate](https://arxiv.org/abs/2605.03409)

**<font color=#1a73e8>作者：</font>** Srinath Perera, Kaviru Hapuarachchi, Frank Leymann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Robust Agent Compensation (RAC), a log-based recovery paradigm (providing a safety net) implemented through an architectural extension that can be applied to most Agent frameworks to support reliable executions (avoiding unintended side effects). Users can choose to enable RAC without changing their current agent code (e.g., LangGraph agents). The proposed approach can be implemented in most existing agent frameworks via their existing extension points. We present an implementation based on LangChain, demonstrate its viability through the $\tau$-bench and REALM-Bench, and show that when solving complex problems, RAC is 1.5-8X or more better in both latency and token economy compared to state-of-the-art LLM-based recovery approaches.

---


### 105. [Geometry over Density: Few-Shot Cross-Domain OOD Detection](https://arxiv.org/abs/2605.03410)

**<font color=#1a73e8>作者：</font>** Shawn Li, You Qin, Jiate Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) detection identifies test samples that fall outside a model's training distribution, a capability critical for safe deployment in high-stakes applications. Standard OOD detectors are trained on a specific in-distribution (ID) dataset and detect deviations from that single domain. In contrast, we study few-shot cross-domain OOD detection: given a \emph{single} pre-trained model, can we perform OOD detection on \emph{arbitrary} new ID-OOD task pairs using only a handful of ID samples at inference time, with no additional training? We propose \textbf{UFCOD}, a unified framework that achieves this goal through information-geometric analysis of diffusion trajectories. Our key insight is that diffusion noise predictions are score functions (gradients of log-density), and we extract two energy features: \emph{Path Energy} (integrated score magnitude) and \emph{Dynamics Energy} (score smoothness), that form a discrete Sobolev norm capturing how samples interact with the learned diffusion process. The central contribution is a \textbf{train-once, deploy-anywhere} paradigm: a diffusion model trained on a single dataset (e.g., CelebA) serves as a universal feature extractor for OOD detection across semantically unrelated domains (e.g., CIFAR-10, SVHN, Textures). At deployment, each new task requires only $\sim$100 unlabeled ID samples for inference: no retraining, no fine-tuning, no task-specific adaptation. Using 100 ID samples per task, UFCOD achieves 93.7\% average AUROC across 12 cross-domain benchmarks, competitive with methods trained on 50k--163k samples, demonstrating $\sim$500$\times$ improvement in sample efficiency. See our code in this https URL.

---


### 106. [Learning to Theorize the World from Observation](https://arxiv.org/abs/2605.03413)

**<font color=#1a73e8>作者：</font>** Doojin Baek, Gyubin Lee, Junyeob Baek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What does it mean to understand the world? Contemporary world models often operationalize understanding as accurate future prediction in latent or observation space. Developmental cognitive science, however, suggests a different view: human understanding emerges through the construction of internal theories of how the world works, even before mature language is acquired. Inspired by this theory-building view of cognition, we introduce Learning-to-Theorize, a learning paradigm for inferring explicit explanatory theories of the world from raw, non-textual observations. We instantiate this paradigm with the Neural Theorizer (NEO), a probabilistic neural model that induces latent programs as a learned Language of Thought and executes them through a shared transition model. In NEO, a theory is represented as an executable, compositional program whose learned primitives can be systematically recombined to explain novel phenomena. Experiments show that this formulation enables explanation-driven generalization, allowing observations to be understood in terms of the programs that generate them.

---


### 107. [Geolocating News about Extreme Climate Events: A Comparative Analysis of Off-the-Shelf Tools for Toponym Identification in German](https://arxiv.org/abs/2605.03414)

**<font color=#1a73e8>作者：</font>** Brielen Madureira, Mariana Madruga de Brito, Andreas Niekler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Determining the geolocation of extreme climate events and disasters in texts is a common problem in climate impact and adaptation research. Named-entity recognition (NER) tools are typically used to identify a pool of toponyms that serve as candidate event locations. In this study, we conduct a comparative analysis of three off-the-shelf NER tools, namely Flair, Spacy and Stanza. We describe and quantify differences between their outputs for German news articles and evaluate them extrinsically based on three methods to determine the country where events took place. We show how their contrasts are propagated into downstream tasks and can yield distinct decisions about a document's geographical focus, which, in turn, can impact conclusions about countries' prominence in German media.

---


### 108. [Adaptive Dual-Path Framework for Covert Semantic Communication](https://arxiv.org/abs/2605.03423)

**<font color=#1a73e8>作者：</font>** Xi Yu, Weicai Li, Lin Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes a novel adaptive dual-path framework for covert semantic communication (SemCom), which integrates covert information transmission with task-oriented semantic coding. Unlike conventional covert communication methods that embed hidden messages through power-domain signal superposition, our framework embeds covert data within task-specific features via semantic-level intrinsic encoding. This new architecture introduces dual encoding paths with adaptive block selection: an Explicit path for public task execution and a Stego path that jointly encodes both public and covert information through contrastive representation alignment. A Gumbel-Softmax enabled adaptive path selection mechanism dynamically activates network blocks based on task require- ments. We formulate a multi-objective optimization framework that simultaneously ensures accurate semantic understanding and reliable covert transmission. We rigorously evaluate our framework's security against a powerful, independently trained attacker. Experimental results on the Cityscapes dataset demon- strate a state-of-the-art level of covertness: our method suppresses the attacker's detection accuracy to a near-random guessing level of 56.12%. This robust security is achieved while simultaneously maintaining superior performance on the primary semantic tasks compared to the baselines.

---


### 109. [FIBER: A Differentially Private Optimizer with Filter-Aware Innovation Bias Correction](https://arxiv.org/abs/2605.03425)

**<font color=#1a73e8>作者：</font>** Duc Dm, Thao Do, Minh Son Hoang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private (DP) training protects individual examples by adding noise to gradients, but the injected noise interacts nontrivially with adaptive optimizers. Recent DP methods temporally filter privatized gradients to reduce variance; however, filtering also changes the DP noise statistics seen by AdamW's second-moment accumulator. As a result, bias corrections derived for unfiltered DP noise, such as subtracting sigma_w squared, can become miscalibrated when filtering is present.
We propose FiBeR, a DP optimizer designed for temporally filtered privatized gradients. FiBeR (i) performs denoising in innovation space by filtering the residual stream and integrating it to form the filtered gradient estimate, (ii) decouples the two-point observation geometry from the innovation gain to enable independent tuning, and (iii) introduces a filter-aware second-moment calibration that subtracts the attenuated DP noise contribution A(omega) sigma_w squared, where A(omega) is derived in closed form for the innovation filter and can be computed for general stable linear filters.
Across vision and language benchmarks, FiBeR consistently demonstrates substantial improvements in the performance of DP optimizers, surpassing state-of-the-art results under equivalent privacy constraints on multiple tasks.

---


### 110. [DynaTab: Dynamic Feature Ordering as Neural Rewiring for High-Dimensional Tabular Data](https://arxiv.org/abs/2605.03430)

**<font color=#1a73e8>作者：</font>** Al Zadid Sultan Bin Habib, Gianfranco Doretto, Donald A. Adjeroh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional tabular data lacks a natural feature order, limiting the applicability of permutation-sensitive deep learning models. We propose DynaTab, a dynamic feature ordering-enabled architecture inspired by neural rewiring. We introduce a lightweight criterion that predicts when feature permutation will benefit a dataset by quantifying its intrinsic complexity. DynaTab dynamically reorders features via a neural rewiring algorithm and processes them through a compact, dynamic order-aware combination of separate learned positional embedding, importance-based gating, and masked attention layers, compatible with any sequence-sensitive backbone. Trained end-to-end with bespoke dynamic feature ordering (DFO) and dispersion losses, DynaTab achieves statistically significant gains, particularly on high-dimensional datasets, where it is benchmarked against 45 state-of-the-art baselines across 36 different real-world tabular datasets. Our results position DynaTab as a compelling new paradigm for high-dimensional tabular deep learning.

---


### 111. [MK-ResRecon: Multi-Kernel Residual Framework for Texture-Aware 3D MRI Refinement from Sparse 2D Slices](https://arxiv.org/abs/2605.03432)

**<font color=#1a73e8>作者：</font>** Prajyot Pyati, Sapna Sachan, Amulya Kumar Mahto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic Resonance Imaging (MRI) acquisition remains a time-intensive and patient-straining process, as prolonged scan dura- tions increase the likelihood of motion artifacts, which degrade image quality and frequently require repeated scans. To address these chal- lenges, we propose a novel framework with two models MK-ResRecon and IdentityRefineNet3D to reconstruct high-fidelity 3D MRI volumes from sparsely sampled 2D slices-requiring only 12.5% of the axial slices for full resolution 3D reconstruction. MK-ResRecon predicts missing in- termediate 2D slices using a multi-kernel texture-aware loss, preserving fine anatomical details. IdentityRefineNet3D refines the predicted slices and the original sparse slices as a single 3D volume to obtain a smooth anatomical structure. We train the models on a large T1-sequence POST- contrast brain MRI dataset and evaluate on a large heterogeneous brain MRI cohort. The work provides accurate, hallucination-free, generaliz- able and clinically validated framework for 3D MRI reconstruction from highly sparse inputs and enables a clinically viable path towards faster and more patient-friendly MRI imaging.

---


### 112. [Quantum Hierarchical Reinforcement Learning via Variational Quantum Circuits](https://arxiv.org/abs/2605.03434)

**<font color=#1a73e8>作者：</font>** Yu-Ting Lee, Samuel Yen-Chi Chen, Fu-Chieh Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is one of the most challenging learning paradigms where efficacy and efficiency gains are extremely valuable. Hierarchical reinforcement learning is a variant that leverages temporal abstraction to structure decision-making. While parametrized quantum computations have shown success in non-hierarchical reinforcement learning, whether these advantages adapt to hierarchical decision-making remains a critical open question. In this work, we develop a hybrid hierarchical agent based on the option-critic architecture. This hybrid agent substitutes classical components with variational quantum circuits for feature extractors, option-value functions, termination functions, and intra-option policies. Evaluated on standard benchmarking environments, results show that a hybrid agent utilizing a quantum feature extractor can outperform classical baselines while saving up to 66\% trainable parameters. We also identify an architectural bottleneck that quantum option-value estimation severely degrades performance. Further ablation studies reveal how architectural choices of the quantum circuits affect performance. Our work establishes design principles for parameter-efficient hybrid hierarchical agents.

---


### 113. [Learning Discriminative Signed Distance Functions from Multi-scale Level-of-detail Features for 3D Anomaly Detection](https://arxiv.org/abs/2605.03437)

**<font color=#1a73e8>作者：</font>** Haibo Xiao, Hanzhe Liang, Jie Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting anomalies from 3D point clouds has received increasing attention in the field of computer vision, with some group-based or point-based methods achieving impressive results in recent years. However, learning accurate point-wise representations for 3D anomaly detection faces great challenges due to the large scale and sparsity of point clouds. In this study, a surface-based method is proposed for 3D anomaly detection, which learns a discriminative signed distance function using multi-scale level-of-detail features. We first present a Noisy Points Generation (NPG) module to generate different types of noise, thereby facilitating the learning of discriminative features by exposing abnormal points. Then, we introduce a Multi-scale Level-of-detail Feature (MLF) module to capture multi-scale information from a point cloud, which provides both fine-grained local and coarse-grained global feature information. Finally, we design an Implicit Surface Discrimination (ISD) module that leverages the extracted multi-scale features to learn an implicit surface representation of point clouds, which effectively trains a signed distance function to distinguish between abnormal and normal points. Experimental results demonstrate that the proposed method achieves an average object-level AUROC of 92.1\% and 85.9\% on the Anomaly-ShapeNet and Real3D-AD datasets, outperforming the current best approach by 2.1\% and 3.6\%, respectively. Codes are available at this https URL.

---


### 114. [A Comparison of Traditional Machine Learning Algorithms and LSTM-Based Deep Learning Models for Email Sentiment Analysis](https://arxiv.org/abs/2605.03440)

**<font color=#1a73e8>作者：</font>** Virdio Samuel Saragih, Baruna Abirawa, Kartini Lovian Simbolon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid growth of electronic communication has necessitated more robust systems for email classification and sentiment detection. This study presents a comparative performance analysis between traditional machine learning algorithms and deep learning architectures, specifically focusing on Support Vector Machines (SVMs), Logistic Regression, Naive Bayes, and Long Short-Term Memory (LSTM). Utilizing Word2Vec embeddings for feature representation, our experimental results indicate that the SVM model with a linear kernel achieves the highest efficiency and accuracy, reaching a peak performance of 98.74%. While the LSTM model demonstrates exceptional recall capabilities in detecting spam-related sentiments, it requires significantly more computational time compared to discriminative statistical models. Detailed evaluations via confusion matrices further reveal that traditional classifiers remain highly robust for dense vector spaces. This research concludes that for email detection tasks, SVM offers the most optimal balance between predictive precision and processing speed. These findings provide critical insights for developing high-performance automated email filtering systems in professional and academic environments.

---


### 115. [Sentiment Analysis of Indonesian Spotify Reviews Using Machine Learning and BiLSTM](https://arxiv.org/abs/2605.03443)

**<font color=#1a73e8>作者：</font>** Uliano Wilyam Purba, Andre Hadiman Rotua Parhusip, Sahid Maulana 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper benchmarks classical machine learning and deep learning approaches for three-class sentiment classification of Indonesian Spotify reviews. Using 100,000 scraped reviews and 70,155 cleaned samples, the study compares Support Vector Machine, Multinomial Naive Bayes, and Decision Tree models with a two-layer BiLSTM. Both approaches use the same preprocessing pipeline, including slang normalization, stopword removal, and stemming. Decision Tree achieves the best performance among the classical models, while BiLSTM attains the highest weighted F1-score overall but fails on the minority neutral class. The paper concludes that BiLSTM is stronger for overall sentiment detection, whereas machine learning with SMOTE provides more balanced three-class performance.

---


### 116. [An ERP Study of Recursive Possessive Parsing in ASD Children and Its Cognitive Neuro Mechanisms](https://arxiv.org/abs/2605.03447)

**<font color=#1a73e8>作者：</font>** Fu Chenxi, Wang Xiaoyi, Zhuang Ziman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recursive structures are a core property of human language, yet little is known about how children with autism spectrum disorder (ASD) process complex recursion. This ERP study investigated the online processing of two-level recursive possessive structures in Mandarin-speaking children with ASD (n = 12) compared to typically developing (TD) peers (n = 12) using a sentence-picture matching paradigm. ERPs were analyzed for P200 (150-250 ms), N400 (300-500 ms), and P600 (500-1000 ms). Results showed that ASD children exhibited significantly reduced P200 amplitudes and failed to show the typical posterior grammaticality effect, indicating atypical early perceptual processing. No robust N400 violation effect was observed in either group, confirming the mismatch was not a semantic anomaly; however, ASD children showed a reversed anterior effect and an attenuated posterior effect. For the P600, ASD children had significantly reduced amplitudes, no posterior grammaticality effect, and a trend toward delayed latency, reflecting a core deficit in syntactic reanalysis. These findings demonstrate that while lexical-semantic processing is relatively preserved in ASD, the online syntactic computation required for recursion is severely impaired, supporting modular dissociation accounts of language in autism.

---


### 117. [Retrieving Floods without Floodlights: Topic Models as Binary Classifiers for Extreme Climate Events in German News](https://arxiv.org/abs/2605.03450)

**<font color=#1a73e8>作者：</font>** Brielen Madureira, Mariana Madruga de Brito, Andreas Niekler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In studies of media coverage of extreme climate events, NLP methods have become indispensable for identifying relevant texts in large news databases. Still, enough annotated data to train accurate deep learning-based classifiers from scratch is often not available. Topic Models have the advantage of being both unsupervised and interpretable, but are typically used only for exploratory analysis or data characterisation. In this study, we investigate how to employ Topic Models as binary classifiers for refining the retrieval of relevant news about seven types of extreme climate events in the German media. Our method relies on the posterior distributions estimated by Topic Models to select relevant documents, without modifying their training procedure. Using an annotated sample to guide the evaluation, we show that the probabilities assigned to keywords used to query news databases can also be informative for selecting relevant topics and improve sample precision. We compare our results to a fine-tuned text embedding classifier and an open-weight LLM, discussing observed trade-offs, e.g. the LLM's lowest precision. Moreover, we show that results are hazard-dependent, which speaks against considering climate events as a single category in NLP tasks.

---


### 118. [VL-SAM-v3: Memory-Guided Visual Priors for Open-World Object Detection](https://arxiv.org/abs/2605.03456)

**<font color=#1a73e8>作者：</font>** Chih-Chung Liu, Zhiwei Lin, Yongtao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world object detection aims to localize and recognize objects beyond a fixed closed-set label space. It is commonly divided into two categories, i.e., open-vocabulary detection, which assumes a predefined category list at test time, and open-ended detection, which requires generating candidate categories during the inference. Existing methods rely primarily on coarse textual semantics and parametric knowledge, which often provide insufficient visual evidence for fine-grained appearance variation, rare categories, and cluttered scenes. In this paper, we propose VL-SAM-v3, a unified framework that augments open-world detection with retrieval-grounded external visual memory. Specifically, once candidate categories are available, VL-SAM-v3 retrieves relevant visual prototypes from a non-parametric memory bank and transforms them into two complementary visual priors, i.e., sparse priors for instance-level spatial anchoring and dense priors for class-aware local context. These priors are integrated with the original detection prompts via Memory-Guided Prompt Refinement, enabling a shared retrieval-and-refinement mechanism that supports open-vocabulary and open-ended this http URL zero-shot experiments on LVIS show that VL-SAM-v3 consistently improves detection performance under both open-vocabulary and open-ended inference, with particularly strong gains on rare this http URL, experiments with a stronger open-vocabulary detector (i.e., SAM3) validate the generality of the proposed retrieval-and-refinement mechanism.

---


### 119. [First Shape, Then Meaning: Efficient Geometry and Semantics Learning for Indoor Reconstruction](https://arxiv.org/abs/2605.03463)

**<font color=#1a73e8>作者：</font>** Remi Chierchia, Léo Lebrat, David Ahmedt-Aristizabal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural Surface Reconstruction has become a standard methodology for indoor 3D reconstruction, with Signed Distance Functions (SDFs) proving particularly effective for representing scene geometry. A variety of applications require a detailed understanding of the scene context, driving the need for object-level semantic signals. While recent methods successfully integrate semantic labels, they often inherit the slow training time and limited scalability of multi-SDF learning. In this paper, we introduce FSTM, a unified approach for learning geometry and semantics through a two-step process: a geometry warm-up using RGB inputs and geometric cues, followed by semantic field estimation. By first optimising geometry without semantic supervision, we observe substantial improvements compared to the standard joint optimisation. Rather than relying on specialised modules or complex multi-SDF designs, FSTM shows that a streamlined formulation is sufficient to achieve strong geometric and semantic reconstructions. Experiments on both synthetic and real-world indoor datasets show that our method outperforms multi-SDF approaches. It trains 2.3x faster on Replica, improves robustness to real-world imperfections on ScanNet++, and achieves higher recall by recovering the surfaces of more objects in the scene. The code will be made available at this https URL.

---


### 120. [Detecting Stealth Sycophancy in Mental-Health Dialogue with Dynamic Emotional Signature Graphs](https://arxiv.org/abs/2605.03472)

**<font color=#1a73e8>作者：</font>** Tianze Han, Beining Xu, Hanbo Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As conversational AI therapists are increasingly used in psychological support settings, reliable offline evaluation of therapeutic response quality remains an open problem. This paper studies multi-domain support-dialogue evaluation without relying on large language models as final judges. We use a direct LLM judge as a baseline that reads raw dialogue text and predicts whether the target response is harmful, productive, or neutral. We find that direct LLM judges and symmetric text-similarity metrics are poorly aligned with therapeutic quality because the target label depends on clinical direction: whether the response moves the user state toward regulation or reframing, leaves it broadly unchanged, or reinforces deterioration through higher risk affect or cognitive-distortion mass. To address this issue, we propose Dynamic Emotional Signature Graphs (DESG), a model-agnostic evaluator that represents dialogue windows with decoupled clinical states and scores them using asymmetric clinical geometry. We evaluate DESG on a constructed diagnostic stress-test benchmark of 3{,}000 dialogue windows from EmpatheticDialogues, ESConv, and CRADLE-Dialogue, covering peer support, counseling dialogue, and crisis-oriented interaction. On the 600-window held-out test aggregate, DESG-Ensemble achieves 0.9353 macro-F1, exceeding ConcatANN by 1.51 percentage points, BERTScore by 19.63 points, and TRACT by 33.81 points. Feature ablations, artifact controls, a 100-window blinded adjudicator audit, and qualitative disagreement cases indicate that the clinical state manifold is the main discriminative substrate, while graph-based trajectory components provide asymmetric scoring and interpretable diagnostics rather than serving as the sole source of performance.

---


### 121. [WorldJen: An End-to-End Multi-Dimensional Benchmark for Generative Video Models](https://arxiv.org/abs/2605.03475)

**<font color=#1a73e8>作者：</font>** Karthik Inbasekar, Guy Rom, Omer Shlomovits  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating generative video models remains an open problem. Reference-based metrics such as Structural Similarity Index Measure (SSIM) and Peak Signal to Noise Ratio (PSNR) reward pixel fidelity over semantic correctness, while Frechet Video Distance (FVD) favors distributional textures over physical plausibility. Binary Visual Question Answering (VQA) based benchmarks like VBench~2.0 are prone to yes-bias and rely on low-resolution auditors that miss temporal failures. Moreover, their prompts target a single dimension at a time, multiplying the number of videos required while still not guaranteeing reliable results.
WorldJen addresses these limitations directly. Binary VQA is replaced with Likert-scale questionnaires graded by a VLM that receives frames at native video resolution. Video generation costs are addressed by using adversarially curated prompts that are designed to exercise up to 16 quality dimensions simultaneously. The framework is built around two interlocking contributions. First, A blind human preference study is conducted, accumulating (2,696 pairwise annotations from 7 annotators with 100% pair coverage over 50 of the curated prompts $\times$ 6 state-of-the-art video models. A mean inter-annotator agreement of 66.9% is achieved and the study establishes a human ground-truth Bradley-Terry (BT) rating with a three-tier structure. Second, A VLM-as-a-judge evaluation engine using prompt-specific, dimension-specific Likert questionnaires (10 questions per dimension, 47,160 scored responses) judges the videos and reproduces the human-established three-tier BT rating structure independently. The VLM achieves a Spearman $\hat{\rho}=1.000,~p=0.0014$ that is interpreted as tier agreement with the human results. Six focused ablation studies validate the robustness of the VLM evaluation framework.

---


### 122. [MEMSAD: Gradient-Coupled Anomaly Detection for Memory Poisoning in Retrieval-Augmented Agents](https://arxiv.org/abs/2605.03482)

**<font color=#1a73e8>作者：</font>** Ishrith Gowda  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Persistent external memory enables LLM agents to maintain context across sessions, yet its security properties remain formally uncharacterized. We formalize memory poisoning attacks on retrieval-augmented agents as a Stackelberg game with a unified evaluation framework spanning three attack classes with escalating access assumptions. Correcting an evaluation protocol inconsistency in the triggered-query specification of Chen et al. (2024), we show faithful evaluation increases measured attack success by $4\times$ (ASR-R: $0.25 \to 1.00$). Our primary contribution is MEMSAD (Semantic Anomaly Detection), a calibration-based defense grounded in a gradient coupling theorem: under encoder regularity, the anomaly score gradient and the retrieval objective gradient are provably identical, so any continuous perturbation that reduces detection risk necessarily degrades retrieval rank. This coupling yields a certified detection radius guaranteeing correct classification regardless of adversary strategy. We prove minimax optimality via Le Cam's method, showing any threshold detector requires $\Omega(1/\rho^2)$ calibration samples and MEMSAD achieves this up to $\log(1/\delta)$ factors. We further derive online regret bounds for rolling calibration at rate $O(\sigma^{2/3}\Delta^{1/3})$, and formally characterize a discrete synonym-invariance loophole that marks the boundary of what continuous-space defenses can guarantee. Experiments on a $3 \times 5$ attack-defense matrix with bootstrap confidence intervals, Bonferroni-corrected hypothesis tests, and Clopper-Pearson validation ($n=1{,}000$) confirm: composite defenses achieve TPR $= 1.00$, FPR $= 0.00$ across all attacks, while synonym substitution evades detection at $\Delta$ ASR-R $\approx 0$, exposing a gap existing embedding-based defenses cannot close.

---


### 123. [Orientation-Aware Unsupervised Domain Adaptation for Brain Tumor Classification Across Multi-Modal MRI](https://arxiv.org/abs/2605.03490)

**<font color=#1a73e8>作者：</font>** Sapna Sachan, Amulya Kumar Mahto, Prashant Wagambar Patil  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The clinical integration of deep learning models for brain tumor diagnosis in neuro-oncology is severely constrained by limited expert-annotated MRI data and substantial inter-institutional domain shift arising from variations in scanners, imaging protocols, and contrast settings. These challenges significantly impair model generalization in real-world settings. To address this, we propose a novel orientation-aware unsupervised domain-adaptive framework for automated brain tumor classification using mixed 2D MRI slices. Initially, a CNN with large receptive field first categorizes input slices into axial, sagittal, and coronal views. For each orientation, a CNN architecture with ResNet50 backbone augmented with four fully connected layers is trained to extract discriminative features for tumor classification. To mitigate annotation scarcity and domain discrepancies, we introduce a slice-wise unsupervised domain adaptation strategy that transfers knowledge from the multi-modal such as T1, T2, and FLAIR source domain to the post-contrast T1 target domain. Feature-level alignment is enforced using maximum mean discrepancy loss, complemented by pseudo-label guided adaptation to preserve class discriminability. Extensive experiments demonstrate improved target-domain performance over prior approaches, highlighting the benefits of orientation-specific learning, multi-modal knowledge transfer, pseudo-label-guided adaptation, and unsupervised domain adaptation.

---


### 124. [Real-Time Evaluation of Autonomous Systems under Adversarial Attacks](https://arxiv.org/abs/2605.03491)

**<font color=#1a73e8>作者：</font>** Adithya Mohan, Xujun Xie, Venkatesh Thirugnana Sambandham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most evaluations of autonomous driving policies under adversarial conditions are conducted in simulation, due to cost efficiency and the absence of physical risk. However, purely virtual testing fails to capture structural inconsistencies, supervision constraints, and state-representation effects that arise in real-world data and fundamentally shape policy robustness. This work presents an offline trajectory-learning and adversarial robustness evaluation framework grounded in real-world intersection driving data. Within a controlled data contract, we train and compare three trajectory-learning paradigms: Multi-Layer Perceptron (MLP)-based Behavior Cloning (BC), Transformer-based object-tokenized BC, and inverse reinforcement learning (IRL) formulated within a Generative Adversarial Imitation Learning (GAIL) framework. Models are evaluated using Average Displacement Error (ADE) and Final Displacement Error (FDE).
Inference-time robustness is assessed by subjecting trained policies to gradient-based adversarial perturbations across multiple intersection scenarios, yielding a structured robustness evaluation matrix. Results show that state-structure design and architectural inductive biases critically influence adversarial stability, leading to markedly different robustness profiles despite comparable nominal prediction accuracy (ADE < 0.08). Inference-time Projected Gradient Descent (PGD) attacks induce final displacement errors of up to approximately 8 meters. The proposed framework establishes a scalable benchmark for studying offline trajectory learning and adversarial robustness in real-world autonomous driving settings.

---


### 125. [From TinyGo to gc Compiler: Extending Zorya's Concolic Framework to Real-World Go Binaries](https://arxiv.org/abs/2605.03492)

**<font color=#1a73e8>作者：</font>** Karolina Gorna, Nicolas Iooss, Yannick Seurin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zorya is a concolic execution framework that lifts compiled binaries to Ghidra's P-Code intermediate representation and uses the Z3 SMT solver to detect vulnerabilities by reasoning over both concrete and symbolic values. Previous versions supported only single-threaded TinyGo binaries. In this paper, we extend Zorya to multi-threaded binaries produced by Go's standard gc compiler. This is achieved by restoring OS thread states from gdb dumps, neutralizing runtime preemption, and introducing overlay path analysis with copy-on-write semantics to detect silent vulnerabilities on untaken branches. We rigorously assess Zorya on 11 real-world vulnerabilities from production Go projects such as Kubernetes, Go-Ethereum, and CoreDNS. Our evaluation shows that Zorya detects seven bugs at the binary level, including a silent integer overflow detects no other evaluated tool finds without a manually written oracle.

---


### 126. [Bandits on graphs and structures](https://arxiv.org/abs/2605.03493)

**<font color=#1a73e8>作者：</font>** Michal Valko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The goal of this thesis is to investigate the structural properties of certain sequential problems in order to bring the solutions closer to a practical use. In the first part, we put a special emphasis on structures that can be represented as graphs on actions. In the second part, we study the large action spaces that can be of exponential size in the number of base actions or even infinite. For graph bandits, we consider the settings of smoothness of rewards (spectral bandits), side observations, and influence maximization. For large structured domains, we cover kernel bandits, polymatroid bandits, bandits for function optimization (including unknown smoothness), and infinitely many-arms bandits. The thesis aspires to be a survey of the author's contributions on graph and structured bandits.

---


### 127. [Design of Memristive Lightweight Encryption For In-Memory Image Steganography](https://arxiv.org/abs/2605.03494)

**<font color=#1a73e8>作者：</font>** Seyed Erfan Fatemieh, Reza Shahdi Alizadeh, Esmail Zarezadeh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the expansion of data-intensive applications and increasing data volumes, providing an efficient solution to address growing energy consumption and performance degradation caused by the transfer of large amounts of data between the processor and the main memory has become a severe challenge. The frequent transfer of large amounts of data between internal chip units, memories, and their interconnections exacerbates the vulnerability of the data being accessed. Employing a memristive Computation In-Memory-Array (CIM-A) architecture limits data transfer, thereby addressing both challenges. Furthermore, by integrating lightweight cryptography, developed to secure data in hardware-constrained devices, with CIM-A architectures, the security of data in transit, especially across interconnections, can be ensured. This paper implements two standard lightweight stream ciphers, Trivium and Grain-128a, for CIM using stateful material implication (IMPLY) logic to address these combined security and performance challenges. In addition to redesigning the cryptographic structures, we reduce the hardware complexity of conventional IMPLY-based implementations by proposing an efficient method for shifting data within the shift registers. Applying the proposed data-shifting method to the registers of these ciphers reduces the number of computational steps and decreases energy consumption by up to 42% and 44%, respectively, compared to conventional implementations. Finally, the performance of the proposed circuits is evaluated in a steganography application, demonstrating their practical efficiency.

---


### 128. [Adaptive graph-based algorithms for conditional anomaly detection and semi-supervised learning](https://arxiv.org/abs/2605.03495)

**<font color=#1a73e8>作者：</font>** Michal Valko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop graph-based methods for semi-supervised learning based on label propagation on a data similarity graph. When data is abundant or arrive in a stream, the problems of computation and data storage arise for any graph-based method. We propose a fast approximate online algorithm that solves for the harmonic solution on an approximate graph. We show, both empirically and theoretically, that good behavior can be achieved by collapsing nearby points into a set of local representative points that minimize distortion. Moreover, we regularize the harmonic solution to achieve better stability properties. We also present graph-based methods for detecting conditional anomalies and apply them to the identification of unusual clinical actions in hospitals. Our hypothesis is that patient-management actions that are unusual with respect to the past patients may be due to errors and that it is worthwhile to raise an alert if such a condition is encountered. Conditional anomaly detection extends standard unconditional anomaly framework but also faces new problems known as fringe and isolated points. We devise novel nonparametric graph-based methods to tackle these problems. Our methods rely on graph connectivity analysis and soft harmonic solution. Finally, we conduct an extensive human evaluation study of our conditional anomaly methods by 15 experts in critical care.

---


### 129. [Bandits attack function optimization](https://arxiv.org/abs/2605.03496)

**<font color=#1a73e8>作者：</font>** Philippe Preux, Rémi Munos, Michal Valko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider function optimization as a sequential decision making problem under budget constraint. This constraint limits the number of objective function evaluations allowed during the optimization. We consider an algorithm inspired by a continuous version of a multi-armed bandit problem which attacks this optimization problem by solving the tradeoff between exploration (initial quasi-uniform search of the domain) and exploitation (local optimization around the potentially global maxima). We introduce the so-called Simultaneous Optimistic Optimization (SOO), a deterministic algorithm that works by domain partitioning. The benefit of such approach are the guarantees on the returned solution and the numerical efficiency of the algorithm. We present this machine learning approach to optimization, and provide the empirical assessment of SOO on the CEC'2014 competition on single objective real-parameter numerical optimization test-suite.

---


### 130. [GRIFDIR: Graph Resolution-Invariant FEM Diffusion Models in Function Spaces over Irregular Domains](https://arxiv.org/abs/2605.03497)

**<font color=#1a73e8>作者：</font>** James Rowbottom, Elizabeth L. Baker, Nick Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based diffusion models in infinite-dimensional function spaces provide a mathematically principled framework for modelling function-valued data, offering key advantages such as resolution invariance and the ability to handle irregular discretisations. However, practical implementations have struggled to fully realise these benefits. Existing backbones like Fourier neural operators are often biased towards regular grids and fail to generalise to complex domain topologies. We propose a novel architecture for function-space diffusion models that represents generalised graph convolutional kernels as finite element functions, enabling the model to naturally handle unstructured meshes and complex geometries. We demonstrate the efficacy of our network architecture through a series of unconditional and conditional sampling experiments across diverse geometries, including non-convex and multiply-connected domains. Our results show that the proposed method maintains resolution invariance and achieves high fidelity in capturing functional distributions on non-trivial geometries.

---


### 131. [A Hierarchical Sampling Framework for bounding the Generalization Error of Federated Learning](https://arxiv.org/abs/2605.03499)

**<font color=#1a73e8>作者：</font>** Dario Filatrella, Ragnar Thobaben, Mikael Skoglund  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study expected generalization bounds for the Hierarchical Federated Learning (HFL) setup using Wasserstein distance. We introduce a generalized framework in which data is sampled hierarchically, and we model it with a multi-layered tree structure that induces dependencies among the clients' datasets. We derive generalization bounds in terms of Wasserstein distance under the Lipschitz assumption on the loss function, by applying a supersample construction that allows us to measure the sensitivity of the algorithm to the change of a single node in the sampling tree. By leveraging the FL structure, we recover and strictly imply existing state-of-the-art conditional mutual information (CMI) bounds in the case of bounded losses. We also show that our bound can be applied together with Differential Privacy assumptions, to recover generalization bounds based on algorithmic privacy. To assess the tightness of our bounds, we study the Gaussian Location Model (GLM) and show that we recover the actual asymptotic rate of the generalization error.

---


### 132. [BFORE: Butterfly-Firefly Optimized Retinex Enhancement for Low-Light Image Quality Improvement](https://arxiv.org/abs/2605.03509)

**<font color=#1a73e8>作者：</font>** Ahmed Cherif  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light image enhancement is a fundamental challenge in computer vision and multimedia applications, as images captured under insufficient illumination suffer from poor visibility, low contrast, and color distortion. Existing Retinex-based methods rely on manually tuned parameters that fail to generalize across diverse lighting conditions. This paper proposes BFORE (Butterfly-Firefly Optimized Retinex Enhancement), a novel hybrid metaheuristic-optimized framework that automatically tunes the parameters of a multi-stage Retinex-based pipeline. The proposed method converts the input image to HSV color space and applies Adaptive Gamma Correction with Weighted Distribution (AGCWD) to the luminance channel, followed by adaptive denoising. A Butterfly Optimization Algorithm (BOA) optimizes the Multi-Scale Retinex with Color Restoration (MSRCR) parameters, while a Firefly Algorithm (FA) optimizes the AGCWD and denoising parameters. A hybrid BOA-FA switching strategy dynamically balances global exploration and local exploitation. Experimental evaluation on the LOL benchmark dataset (15 paired test images) demonstrates that BFORE achieves the highest PSNR (17.22 dB) among all traditional enhancement methods, with 20.3% improvement over Histogram Equalization and 17.5% over MSRCR. BFORE produces the most naturally balanced mean brightness (129.97), closest to the ideal mid-tone value. Notably, BFORE outperforms RetinexNet -- a deep learning baseline -- in both PSNR (17.22 vs. 16.77 dB) and SSIM (0.5417 vs. 0.4252) without requiring any training data. The hybrid BOA-FA optimization contributes a 12.3% PSNR improvement and 14.8% SSIM improvement over the unoptimized pipeline.

---


### 133. [Rational Communication Shapes Morphological Composition](https://arxiv.org/abs/2605.03510)

**<font color=#1a73e8>作者：</font>** Fengyuan Yang, Yongqian Peng, Yuxi Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human languages expand vocabularies by combining existing morphemes rather than inventing arbitrary forms. Communicative efficiency shapes lexical systems at multiple levels (Gibson et al., 2019), yet morphological composition -- combining morphemes through compounding or affixation -- has rarely been modeled as a historically situated speaker choice among competing morpheme sequences, leaving unanswered why a language settles on one morpheme combination over other plausible alternatives. We ask whether a trade-off between listener recoverability and speaker production cost can predict attested compositions over contemporaneously available alternatives. Here we show, within the Rational Speech Act (RSA) framework (Frank & Goodman, 2012; Goodman & Frank, 2016) using a time-indexed lexicon constructed from Corpus of Historical American English (COHA) and Corpus of Contemporary American English (COCA), that across 4323 naturally occurring English compounds and derivations spanning 1820--2019, attested compositions are systematically ranked above unattested alternatives generated from contemporaneously available morphemes. Models integrating semantic informativeness with production cost outperform semantic-only and cost-only baselines on Mean Reciprocal Rank (MRR) and top-k accuracy (Acc@k), with the advantage of the Pragmatic Speaker model ($S_1$) over the semantic-only baseline growing as the candidate set expands, where meaning alone leaves morphological choice underdetermined. These findings suggest that lexicalization reflects a communicative trade-off between expressiveness and efficiency, extending rational accounts of communication from utterance-level choice to the internal structure of words.

---


### 134. [Meta-Inverse Physics-Informed Neural Networks for High-Dimensional Ordinary Differential Equations](https://arxiv.org/abs/2605.03511)

**<font color=#1a73e8>作者：</font>** Zhao Wei, Kenneth Hor Cheng Koh, Sheng Yuan Chin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving inverse problems in dynamical systems governed by high-dimensional coupled ordinary differential equations (ODEs) is a ubiquitous challenge in scientific machine learning. In many real-world applications, researchers seek to uncover unknown parameters or model unknown dynamics even as the underlying physics is only partially characterized, and observations are sparse and limited to specific measurable channels. While physics-informed neural networks (PINNs) are ideal for inverse inference under partial observability, existing PINNs typically rely on task-specific joint optimization, which suffers from optimization difficulties and poor generalization. In this paper, we propose a meta-inverse physics-informed neural network (MI-PINN) that reformulates inverse modeling as a two-stage meta-learning problem. MI-PINN first learns a physics-aware representation across multiple tasks, and then performs inverse modeling by optimizing task-specific unknowns while keeping the learned representation fixed. This two-stage formulation significantly reduces the parameter search dimension, thereby improving sample efficiency and enabling accurate inference. To handle multi-scale dynamics common in these high-dimensional ODE systems, we further introduce an adaptive clustering-based multi-branch learning scheme. We demonstrate the effectiveness of MI-PINN on whole-body physiologically based pharmacokinetic (PBPK) models with up to 33 coupled ODEs, using paracetamol and theophylline under intravenous and oral dosing scenarios. Experimental results show that MI-PINN enables accurate recovery of masked kinetic parameters and reconstruction of missing mechanistic terms despite limited clinical observations.

---


### 135. [Understanding Self-Supervised Learning via Latent Distribution Matching](https://arxiv.org/abs/2605.03517)

**<font color=#1a73e8>作者：</font>** Fabian A Mikulasch, Friedemann Zenke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) excels at finding general-purpose latent representations from complex data, yet lacks a unifying theoretical framework that explains the diverse existing methods and guides the design of new ones. We cast SSL as latent distribution matching (LDM): learning representations that maximize their log-probability under an assumed latent model (alignment), while maximizing latent entropy to prevent collapse (uniformity). This view unifies independent component analysis with contrastive, non-contrastive, and predictive SSL methods, including stop gradient approaches. Leveraging LDM, we derive a nonlinear, sampling-free Bayesian filtering model with a Kalman-based predictor for high-dimensional timeseries. We further prove that predictive LDM yields identifiable latent representations under mild assumptions, even with nonlinear predictors. Overall, LDM clarifies the assumptions behind established SSL methods and provides principled guidance for developing new approaches.

---


### 136. [DALPHIN: Benchmarking Digital Pathology AI Copilots Against Pathologists on an Open Multicentric Dataset](https://arxiv.org/abs/2605.03544)

**<font color=#1a73e8>作者：</font>** Carlijn Lems, Sander Moonemans, Natálie Klubíčková 等 56 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models with visual question answering capabilities for digital pathology are emerging. Such unprecedented technology requires independent benchmarking to assess its potential in assisting pathologists in routine diagnostics. We created DALPHIN, the first multicentric open benchmark for pathology AI copilots, comprising 1236 images from 300 cases, spanning 130 rare to common diagnoses, 6 countries, and 14 subspecialties. The DALPHIN design and dataset are introduced alongside a human performance benchmark of 31 pathologists from 10 countries with varying expertise. We report results for two general-purpose (GPT-5, Gemini 2.5 Pro) and one pathology-specific copilot (PathChat+) for sequential and independent answer generation. We observed no statistically significant difference from expert-level performance in four of six tasks for PathChat, 2/6 tasks for Gemini, and 1/6 tasks for GPT. DALPHIN is publicly released with sequestered, indirectly accessible ground truth to foster robust and enduring benchmarking. Data, methods, and the evaluation platform are accessible through this http URL.

---


### 137. [PerFlow: Physics-Embedded Rectified Flow for Efficient Reconstruction and Uncertainty Quantification of Spatiotemporal Dynamics](https://arxiv.org/abs/2605.03548)

**<font color=#1a73e8>作者：</font>** Hao Zhou, Rui Zhang, Han Wan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing PDE-governed fields from sparse and irregular measurements is challenging due to their ill-posed nature. Deterministic surrogates are trained on dense fields that struggle with limited measurements and uncertainty quantification. Generative models, by learning distributions over spatiotemporal fields, can better handle sparsity and uncertainty. However, existing generative approaches enforce data consistency and PDE constraints simultaneously via sampling-time gradient guidance, resulting in slow and unstable inference. To this end, we propose PerFlow, a Physics-embedded rectified Flow for efficient sparse reconstruction and uncertainty quantification of spatiotemporal dynamics. PerFlow decouples observation conditioning from physics enforcement, performing guidance-free conditioning by feeding observations into rectified-flow dynamics while embedding hard physics via a constraint-preserving projection (e.g., incompressibility or conservation). Theoretically, we establish invariance guarantees to ensure that trajectories remain on the physics-consistent manifold throughout sampling. Experiments on various PDE systems demonstrate competitive reconstruction accuracy with sound physics consistency, while enabling efficient conditional sampling (e.g., 50 steps) and up to 320 faster inference than 2000-step guided diffusion baselines.

---


### 138. [MILE: Mixture of Incremental LoRA Experts for Continual Semantic Segmentation across Domains and Modalities](https://arxiv.org/abs/2605.03555)

**<font color=#1a73e8>作者：</font>** Shishir Muralidhara, Didier Stricker, René Schuster  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual semantic segmentation requires models to adapt to new domains or modalities without sacrificing performance on previously learned tasks. Expert-based learning, in which task-specific modules specialize in different domains, has proven effective in mitigating forgetting. These methods include dynamic expansion, which suffers from scalability issues, or parameter isolation, which constrains the ability to learn new tasks. We introduce Mixture of Incremental LoRA Experts (MILE), a modular and parameter-efficient framework for continual segmentation across both domains and modalities. MILE leverages Low-Rank Adaptation (LoRA) to instantiate lightweight experts for each new task while keeping the pretrained base network frozen. Each expert is trained exclusively on its task data, thus avoids overwriting previously learned information. A prototype-guided gating mechanism dynamically selects the most appropriate expert at inference. MILE achieves the benefits of expert-based learning while overcoming its scalability limitations. It requires only a marginal parameter increase per task and tens of LoRA adapters are needed before matching the size of a single full model, making it highly efficient in both training and storage. Across domain- and modality-incremental benchmarks, MILE achieves strong performance while ensuring better stability, plasticity, and scalability.

---


### 139. [Enhance the after-discharge mortality rate prediction via learning from the medical notes](https://arxiv.org/abs/2605.03560)

**<font color=#1a73e8>作者：</font>** Zijiang Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the increase of the Electronic Health Records (EHR) data, more and more researchers are developing machine learning models to learn from the medical notes. These unstructured text data pose significant challenges on the learning process as the quality of data is low. These data are often messy, repetitive and redundant. We have shown these notes data to be informative by conducting the after-discharge mortality rate prediction task. The AUC-ROC for models using the medical note information is generally 0.1 higher than those without the medical notes. Furthermore, we propose the Deep Neural Network(DNN) model with 'pooling' mechanism to enhance the mortality prediction. Based on the experimental results, we demonstrate that the proposed model outperforms the traditional machine learning models like the tree-based models. The proposed method learns from the most informative medical notes and improves the prediction accuracy significantly. The AUC-ROC for the proposed model is 2% to 14% higher than the traditional ones in 15-days, 30-days, 60-days, 365-days after-discharge mortality prediction tasks. Moreover, we can discover some interesting knowledge through the traditional and proposed models. These knowledge are inspiring but also consistent with the previous findings. The models are able to reveal the relationships between the informative keywords and documents from the medical notes and the severity of the patients.

---


### 140. [HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization](https://arxiv.org/abs/2605.03562)

**<font color=#1a73e8>作者：</font>** Jorge L. Ruiz Williams  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV-cache quantizers usually optimize storage-space reconstruction, even though attention reads keys through logits and values through attention-weighted readout. We argue that persistent cache error should be measured in model-visible coordinates. For keys, the visible object is score error modulo constant shifts; this yields HeadQ, a key-side method that stores a low-rank residual side code in a calibration-learned query basis and applies it as an additive logit correction. For values, fixed-attention readout gives an $A^2$-weighted token-distortion surrogate. Across six models, Fisher/score-space error predicts attention KL far better than raw key MSE; same-budget counterexamples, null-space interventions, query-PCA controls, and wrong-sign HeadQ falsify storage-MSE alternatives. Matched Pythia checkpoints localize the main anomaly to a small-model low-entropy route-flip boundary. In K-only WikiText-103 decode experiments with dense values, HeadQ removes roughly $84$--$94\%$ of the excess perplexity on the strongest 2-bit rows; in an auxiliary full-KV 2-bit composition, HeadQ plus an $A^2$ value policy improves all six models.

---


### 141. [Disentangling Shared and Task-Specific Representations from Multi-Modal Clinical Data](https://arxiv.org/abs/2605.03570)

**<font color=#1a73e8>作者：</font>** He Lyu, Huolin Zeng, Junren Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world clinical data is inherently multimodal, providing complementary evidence that mirrors the practical necessity of jointly assessing multiple related outcomes. Although multi-task learning can improve efficiency by sharing information across outcomes, existing approaches often fail to balance shared representation learning with outcome-specific modeling. Hard parameter sharing can trigger negative transfer when task gradients conflict, while flexible sharing may still entangle shared and task-specific signals. To address this, we propose a multi-task framework built on a unified Transformer for multimodal fusion, augmented with Orthogonal Task Decomposition (OrthTD) to split patient representations into shared and task-specific subspaces and impose a geometric orthogonality constraint to reduce redundancy and isolate task-specific signals. We evaluated OrthTD on a real-world cohort of 12,430 surgical patients for predicting four outcomes. OrthTD achieved average AUC (area under the receiver operating characteristic curve) of 87.5% and average AUPRC (area under the precision-recall curve) of 37.2%, consistently outperformed advanced tabular and multi-task methods. Notably, OrthTD achieves substantial gains in AUPRC, indicating superior performance in identifying rare events within imbalanced clinical data. These results suggest that enforcing non-redundant shared and task-specific representations can improve multi-outcome prediction from multimodal clinical data.

---


### 142. [PatRe: A Full-Stage Office Action and Rebuttal Generation Benchmark for Patent Examination](https://arxiv.org/abs/2605.03571)

**<font color=#1a73e8>作者：</font>** Qiyao Wang, Xinyi Chen, Longze Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Patent examination is a complex, multi-stage process requiring both technical expertise and legal reasoning, increasingly challenged by rising application volumes. Prior benchmarks predominantly view patent examination as discriminative classification or static extraction, failing to capture its inherently interactive and iterative nature, similar to the peer review and rebuttal process in academic publishing. In this paper, we introduce PatRe, the first benchmark that models the full patent examination lifecycle, including Office Action generation and applicant rebuttal. PatRe comprises 480 real-world cases and supports both oracle and retrieval-simulated evaluation settings. Our benchmark reframes patent examination as a dynamic, multi-turn process of justification and response. Extensive experiments across various LLMs reveal critical insights into model performance, including differences between proprietary and open-source models, as well as task asymmetries between examiner analysis and applicant-side rebuttal. These findings highlight both the potential and current limitations of LLMs in modeling complex, real-world legal reasoning and technical novelty judgment in patent examination. We release our code and dataset to facilitate future research on patent examination modeling.

---


### 143. [ZK-Value: A Practical Zero-Knowledge System for Verifiable Data Valuation](https://arxiv.org/abs/2605.03581)

**<font color=#1a73e8>作者：</font>** Zhaoyu Wang, Pingchuan Ma, Zhantong Xue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Data valuation is a foundational task in data marketplaces, where a Shapley-value attribution determines how a buyer's payment is distributed among data providers. Typically, the marketplace operator runs this attribution alone, requiring participants and external auditors to trust scores they cannot independently recompute on the underlying private data. While zero-knowledge proofs (ZKPs) can theoretically reconcile this conflict between privacy and verifiability, existing ZK valuation systems fail to scale to real-world marketplace demands due to prohibitive proving times or the requirement to disclose validation cohorts.
We present ZK-Value, a practical, end-to-end ZK data-valuation system. Our solution bridges the scalability gap through a fully co-designed architecture: (1) LSH-Shapley, a locality-based valuation primitive that replaces expensive pairwise distance metrics with per-bucket collision counts; (2) ZK-LSH-Shapley, a tailored ZKP protocol that drastically reduces witness size by encoding these counts into bucket-level histograms rather than naive per-pair tensors; and (3) structural proof-system optimizations, specifically super-oracle batching and sparsity skipping. Evaluated across 12 standard datasets, ZK-Value delivers valuation quality on par with state-of-the-art baselines (within 0.033 AUROC of exact KNN-Shapley), while generating proofs in seconds to minutes and outperforming specialized ZK baselines by 12.6x to 68.1x in proving time, with verification in under 4.6 s.

---


### 144. [Flow Matching on Symmetric Spaces](https://arxiv.org/abs/2605.03588)

**<font color=#1a73e8>作者：</font>** Francesco Ruscelli, Ferdinando Zanchetta, Rita Fioresi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a general framework for training flow matching models on Riemannian symmetric spaces, a large class of manifolds that includes the sphere, hyperbolic space and Grassmannians. We exploit their algebraic structure to reformulate flow matching on symmetric spaces as flow matching on a subspace of the Lie algebra of their isometry group, thus linearizing the problem and greatly simplifying the handling of geodesics. As an application, we showcase our framework on the real Grassmannians $\operatorname{SO}(n) / \operatorname{SO}(k) \times \operatorname{SO}(n-k)$.

---


### 145. [Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies](https://arxiv.org/abs/2605.03596)

**<font color=#1a73e8>作者：</font>** Zirui Tang, Xuanhe Zhou, Yumou Liu 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Workspace learning requires AI agents to identify, reason over, exploit, and update explicit and implicit dependencies among heterogeneous files in a worker's workspace, enabling them to complete both routine and advanced tasks effectively. Despite its importance, existing relevant benchmarks largely evaluate agents on pre-specified or synthesized files with limited real-world dependencies, leaving workspace-level evaluation underexplored. To this end, we introduce Workspace-Bench, a benchmark for evaluating AI agents on Workspace Learning invOlving Large-Scale File Dependencies. We construct realistic workspaces with 5 worker profiles, 74 file types, 20,476 files (up to 20GB) and curate 388 tasks, each with its own file dependency graph, evaluated across 7,399 total rubrics that require cross-file retrieval, contextual reasoning, and adaptive decision-making. We further provide Workspace-Bench-Lite, a 100-task subset that preserves the benchmark distribution while reducing evaluation costs by about 70%. We evaluate 4 popular agent harnesses and 7 foundation models. Experimental results show that current agents remain far from reliable workspace learning, where the best reaches only 68.7%, substantially below the human result of 80.7%, and the average performance across agents is only 47.4%.

---


### 146. [Most ReLU Networks Admit Identifiable Parameters](https://arxiv.org/abs/2605.03601)

**<font color=#1a73e8>作者：</font>** Moritz Grillo, Guido Montúfar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the realization map of deep ReLU networks, focusing on when a function determines its parameters up to scaling and permutation. To analyze hidden redundancies beyond these standard symmetries, we introduce a framework based on weighted polyhedral complexes. Our main result shows that for every architecture whose input and hidden layers have width at least two, there exists an open set of identifiable parameters. This implies that the functional dimension of every such architecture is exactly the number of parameters minus the number of hidden neurons. We further show that minimal functional representations can still have non-trivial parameter redundancies. Finally, we establish a generic depth hierarchy, whereby for an open set of parameters the realized function cannot be represented generically by any shallower network.

---


### 147. [deSEO: Physics-Aware Dataset Creation for High-Resolution Satellite Image Shadow Removal](https://arxiv.org/abs/2605.03610)

**<font color=#1a73e8>作者：</font>** Lorenzo Beltrame, Jules Salzinger, Filip Svoboda 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shadows cast by terrain and tall structures remain a major obstacle for high-resolution satellite image analysis, degrading classification, detection, and 3D reconstruction performance. Public resources offering geometry-consistent paired shadow/shadow-free satellite imagery are essentially missing, and most Earth-observation datasets are designed for shadow detection or 3D modelling rather than removal. Existing deep shadow-removal datasets either target ground-level or aerial scenes or rely on unpaired and weakly supervised formulations rather than explicit satellite pairs. We address this gap with deSEO, a geometry-aware and physics-informed methodology that, to the best of our knowledge, is the first to derive paired supervision for satellite shadow removal from the S-EO shadow detection dataset through a fully replicable pipeline. For each tile, deSEO selects a minimally shadowed acquisition as a weak reference and pairs it with shadowed counterparts using temporal and geometric filtering, Jacobian-based orientation normalisation, and LoFTR-RANSAC registration. A per-pixel validity mask restricts learning to reliably aligned regions, enabling supervision despite residual off-nadir parallax. In addition to this paired dataset, we develop a DSM-aware deshadowing model that combines residual translation, perceptual objectives, and mask-constrained adversarial learning. In contrast, a direct adaptation of a UAV-based SRNet/pix2pix architecture fails to converge under satellite viewpoint variability. Our model consistently reduces the visual impact of cast shadows across diverse illumination and viewing conditions, achieving improved structural and perceptual fidelity on held-out scenes. deSEO therefore provides the first reproducible, geometry-aware paired dataset and baseline for shadow removal in satellite Earth observation.

---


### 148. [Uncertainty Estimation in Instance Segmentation of Affordances via Bayesian Visual Transformers](https://arxiv.org/abs/2605.03614)

**<font color=#1a73e8>作者：</font>** Lorenzo Mur-Labadia, Ruben Martinez-Cantina, Jose J.Guerrero  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual affordances identify regions in an image with potential interactions, offering a novel paradigm for scene understanding. Recognizing affordances allows autonomous robots to act more naturally, could enhance human-robot interactions, enrich augmented reality systems, and benefit prosthetic vision devices. Accurate and localized prediction of affordance regions, rather than general saliency maps is crucial for these applications. We present a model for instance segmentation of affordances by adopting sample-based and ensembles approaches for uncertainty estimation. We extend an attention-based architecture for our novel task, showing with detailed ablation experiments the effects of each component. By comparing the distribution of these different detections, we extract pixel-wise epistemic and aleatoric variances at both the semantic and spatial levels. In addition, we propose a novel measure called Probability-based Mask Quality, which enables a comprehensive analysis of semantic and spatial variations in a probabilistic instance segmentation model. Our results show that the global consensus of multiple sub-networks of Bayesian models improve deterministic networks due to a better mask refinement and generalization. This fact, joined with the more powerful features extracted by attention-based mechanisms, represent an improvement of +7.4 p.p on the $F_{\beta}^w$ score in the challenging IIT-Aff dataset. Bayesian models are also better calibrated, producing less overconfident probabilities and with a better uncertainty estimation. Qualitative results show that aleatoric variance appears in the contour of the objects, while the epistemic variance is observed in visual challenging pixels, adding interpretability to the neural network.

---


### 149. [PriorNet: Prior-Guided Engagement Estimation from Face Video](https://arxiv.org/abs/2605.03615)

**<font color=#1a73e8>作者：</font>** Alexander Vedernikov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Engagement estimation from face video remains challenging because facial evidence is often incomplete, labeled data are limited, and engagement annotations are subjective. We present PriorNet, a prior-guided framework that injects task-relevant priors at three stages of the pipeline: preprocessing, model adaptation, and objective design. PriorNet converts face-detection failures into explicit zero-frame placeholders so that missing-face events remain represented in the input sequence, adapts a frozen Self-supervised Video Facial Affect Perceiver (SVFAP) backbone through a Prior-guided Low-Rank Adaptation module (Prior-LoRA) for parameter-efficient specialization, and trains with a Dirichlet-evidential, uncertainty-weighted objective under hard-label supervision. We evaluate PriorNet on EngageNet, DAiSEE, DREAMS, and PAFE using each dataset's native evaluation protocol. Across these benchmarks, PriorNet improves over the strongest listed prior reference within each dataset's evaluation framing, while component ablations on EngageNet and DAiSEE indicate that the gains arise from complementary contributions of preprocessing, adaptation, and objective-level priors. These results support explicit prior injection as a useful design principle for face-video engagement estimation under the benchmark conditions studied in this work.

---


### 150. [A Few-Step Generative Model on Cumulative Flow Maps](https://arxiv.org/abs/2605.03623)

**<font color=#1a73e8>作者：</font>** Zhiqi Li, Duowen Chen, Yuchen Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a unified, few-step generative modeling framework based on \emph{cumulative flow maps} for long-range transport in probability space, inspired by flow-map techniques for physical transport and dynamics. At its core is a cumulative-flow abstraction that connects local, instantaneous updates with finite-time transport, enabling generative models to reason about global state transitions. This perspective yields a unified few-step framework built on cumulative transport and \revise{cumulative} parameterization that applies broadly to existing diffusion- and flow-based models without being tied to a specific prediction \revise{instantiation}. Our formulation supports few-step and even one-step generation while preserving synthesis quality, requiring only minimal changes to time embeddings and training objectives, and no increase in model capacity. We demonstrate its effectiveness across diverse tasks, including image generation, geometric distribution modeling, joint prediction, and SDF generation, with reduced inference cost.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-213](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
